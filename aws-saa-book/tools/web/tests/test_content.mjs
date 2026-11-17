// Tests of the fact shards of content.js (owner B; ARCHITECTURE.md 2.4 and 3.2): Content.factService,
// Content.fact, Content.factShard, the memory cache, the inline backend, and the shards of a built site.
// Run: node aws-saa-book/tools/web/tests/test_content.mjs [built folder]
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { load, test, eq, ok, fixture, BUILT_DIR } from "./harness.mjs";

// A page with a fake fetch: `serve(path)` returns the file text or null (404). `calls` counts requests per path.
function app(serve) {
  const calls = {};
  const fetch = (p) => {
    calls[p] = (calls[p] || 0) + 1;
    const text = serve(p);
    if (text === null) return Promise.resolve({ ok: false, status: 404, json: () => Promise.reject(new Error("404")) });
    return Promise.resolve({ ok: true, status: 200, json: () => Promise.resolve(JSON.parse(text)), text: () => Promise.resolve(text) });
  };
  return { C: load(["util.js", "content.js"], { fetch }).Content, calls };
}

// Runs an async block; test() is synchronous, so the result is awaited first and asserted after.
async function run(fn) {
  try { return { value: await fn() }; } catch (e) { return { error: e && e.stack ? e.stack : JSON.stringify(e) }; }
}

function card(claim) {
  return { service: null, claim, values: [], scope: "", quotes: [], checked: "2026-10-12", changed: null, kind: "fact" };
}

const SHARDS = {
  "s3": { "s3-bucket-names": card("A bucket name is global."), "s3-object-size": card("An object is at most a size.") },
  "s3-glacier": { "s3-glacier-vault-lock": card("A vault lock policy is fixed.") },
  "vpc": { "vpc-peering-odd": card("A fact of vpc whose id starts like vpc-peering."), "vpc-cidr": card("A VPC has a CIDR block.") },
  "vpc-peering": { "vpc-peering-transitive": card("Peering is not transitive.") }
};

function synthetic(sha) {
  const files = {};
  const index = { v: 1, count: 6, shards: {}, stray: { "vpc-peering-odd": "vpc" } };
  for (const [svc, facts] of Object.entries(SHARDS)) {
    const text = JSON.stringify({ v: 1, service: svc, facts });
    files["f/" + svc + ".json"] = text;
    index.shards[svc] = { path: "f/" + svc + ".json", bytes: text.length, sha256: svc + sha, count: Object.keys(facts).length };
  }
  files["facts-index.json"] = JSON.stringify(index);
  files["manifest.json"] = JSON.stringify({ v: 1, build: "b" + sha, chapters: [],
    factsIndex: { path: "facts-index.json", bytes: 1, sha256: "idx" + sha, shards: 4, count: 6 } });
  return { files, index };
}

// ---------------------------------------------------------------- the rule (pure)

const RULE = synthetic("1").index;
const P = app(() => null).C;

test("factService: the longest service key that the id starts with, then a dash", () => {
  eq(P.factService("s3-bucket-names", RULE), "s3");
  eq(P.factService("s3-glacier-vault-lock", RULE), "s3-glacier", "s3-glacier wins over s3");
  eq(P.factService("vpc-peering-transitive", RULE), "vpc-peering");
  eq(P.factService("vpc-cidr", RULE), "vpc");
});

test("factService: a stray id goes to the shard the index names", () => {
  eq(P.factService("vpc-peering-odd", RULE), "vpc");
  const bad = { shards: RULE.shards, stray: { "vpc-peering-odd": "nowhere" } };
  eq(P.factService("vpc-peering-odd", bad), "vpc-peering", "a stray entry that names no shard is ignored");
});

test("factService: no service for an unknown prefix, a bare key, an empty id or no index", () => {
  eq(P.factService("kms-key-rotation", RULE), null);
  eq(P.factService("s3", RULE), null, "the key itself is not an id");
  eq(P.factService("s3glacier-x", RULE), null, "the dash is required");
  eq(P.factService("", RULE), null);
  eq(P.factService(undefined, RULE), null);
  eq(P.factService("s3-bucket-names", null), null);
});

// ---------------------------------------------------------------- loading (network backend)

const one = synthetic("1");
const two = synthetic("2");
let served = one.files;
const N = app((p) => (Object.prototype.hasOwnProperty.call(served, p) ? served[p] : null));

const loaded = await run(async () => {
  const out = {};
  out.glacier = await N.C.fact("s3-glacier-vault-lock");
  out.afterGlacier = { ...N.calls };
  out.bucket = await N.C.fact("s3-bucket-names");
  out.size = await N.C.fact("s3-object-size");
  out.odd = await N.C.fact("vpc-peering-odd");
  out.unknown = await N.C.fact("kms-key-rotation");
  out.missing = await N.C.fact("s3-no-such-fact");
  out.noShard = await N.C.factShard("nope");
  out.shard = await N.C.factShard("vpc-peering");
  out.calls = { ...N.calls };
  await N.C.manifest(true);                                 // a refresh with the same index keeps the shards
  await N.C.fact("s3-bucket-names");
  out.sameCalls = { ...N.calls };
  served = two.files;                                       // a republish: a new index hash drops the index and the shards
  await N.C.manifest(true);
  await N.C.fact("s3-bucket-names");
  out.newCalls = { ...N.calls };
  return out;
});

test("fact loads only the shard of its service", () => {
  ok(!loaded.error, loaded.error);
  const v = loaded.value || {};
  eq(v.glacier && v.glacier.claim, "A vault lock policy is fixed.");
  eq(Object.keys(v.afterGlacier || {}).sort(), ["f/s3-glacier.json", "facts-index.json", "manifest.json"]);
});

test("fact: each shard and the index are fetched once per visit", () => {
  const v = loaded.value || {};
  eq(v.bucket && v.bucket.claim, "A bucket name is global.");
  eq(v.size && v.size.claim, "An object is at most a size.");
  eq(v.odd && v.odd.claim, "A fact of vpc whose id starts like vpc-peering.", "a stray id is read from the shard the index names");
  eq(v.calls, { "manifest.json": 1, "facts-index.json": 1, "f/s3-glacier.json": 1, "f/s3.json": 1, "f/vpc.json": 1, "f/vpc-peering.json": 1 });
  ok(!("facts.json" in (v.calls || {})), "the retired facts.json is never requested");
});

test("fact: null for an unknown service or an id that is not in its shard; factShard of an unknown service is null", () => {
  const v = loaded.value || {};
  eq(v.unknown, null);
  eq(v.missing, null);
  eq(v.noShard, null);
  eq(Object.keys((v.shard && v.shard.facts) || {}), ["vpc-peering-transitive"]);
});

test("a manifest refresh keeps the shards, unless the index hash changed", () => {
  const v = loaded.value || {};
  eq((v.sameCalls || {})["f/s3.json"], 1, "same index: no new request");
  eq((v.sameCalls || {})["facts-index.json"], 1);
  eq((v.newCalls || {})["facts-index.json"], 2, "new index: fetched again");
  eq((v.newCalls || {})["f/s3.json"], 2, "new index: the shard is fetched again");
});

// ---------------------------------------------------------------- the inline backend (--single)

const inlineMap = {};
for (const [p, text] of Object.entries(one.files)) inlineMap[p] = JSON.parse(text);
const I = load(["util.js", "content.js"], {
  fetch: () => { throw new Error("no network in --single"); },
  document: { getElementById: (id) => (id === "saa-inline" ? { textContent: JSON.stringify(inlineMap) } : null) }
}).Content;
const inl = await run(async () => ({
  peering: await I.fact("vpc-peering-transitive"),
  unknown: await I.fact("kms-key-rotation")
}));

test("--single: a fact is read from the inlined shard without a request", () => {
  ok(!inl.error, inl.error);
  eq(inl.value && inl.value.peering && inl.value.peering.claim, "Peering is not transitive.");
  eq(inl.value && inl.value.unknown, null);
});

// ---------------------------------------------------------------- a built site (the selftest preview)

const manifest = fixture("manifest.json");
if (!manifest) {
  console.log("note: no built site at " + BUILT_DIR + "; the tests of the built shards are skipped");
} else {
  const sha = (rel) => crypto.createHash("sha256").update(fs.readFileSync(path.join(BUILT_DIR, rel))).digest("hex");
  const size = (rel) => fs.statSync(path.join(BUILT_DIR, rel)).size;
  const row = manifest.factsIndex || {};
  const index = row.path ? fixture(row.path) : null;

  test("built: the manifest lists facts-index.json with its bytes, hash and counts; facts.json is gone", () => {
    eq(row.path, "facts-index.json");
    ok(!!index, "facts-index.json is missing");
    if (!index) return;
    eq([row.bytes, row.sha256], [size(row.path), sha(row.path)]);
    eq([row.shards, row.count], [Object.keys(index.shards).length, index.count]);
    eq(index.count, Object.values(index.shards).reduce((n, s) => n + s.count, 0), "count is the sum of the shards");
    ok(!fs.existsSync(path.join(BUILT_DIR, "facts.json")), "facts.json must not be emitted");
  });

  test("built: every shard matches its index row, and every id resolves to its own shard", () => {
    for (const [svc, s] of Object.entries((index && index.shards) || {})) {
      eq(s.path, "f/" + svc + ".json");
      const doc = fixture(s.path);
      ok(!!doc, s.path + " is missing");
      if (!doc) continue;
      eq([doc.v, doc.service], [1, svc]);
      eq([s.bytes, s.sha256, s.count], [size(s.path), sha(s.path), Object.keys(doc.facts).length], s.path);
      for (const id of Object.keys(doc.facts)) eq(P.factService(id, index), svc, id);
    }
  });

  const B = app((p) => {
    const file = path.join(BUILT_DIR, p);
    return fs.existsSync(file) ? fs.readFileSync(file, "utf8") : null;
  });
  const chapterFiles = fs.existsSync(path.join(BUILT_DIR, "c")) ? fs.readdirSync(path.join(BUILT_DIR, "c")).filter((f) => f.endsWith(".json")) : [];
  const found = await run(async () => {
    const rows = [];
    for (const name of chapterFiles.sort()) {
      const c = fixture("c/" + name);
      for (const [id, want] of Object.entries((c && c.facts) || {})) rows.push([id, want, await B.C.fact(id)]);
    }
    return rows;
  });

  test("built: every fact of the chapter files is found through Content.fact, each shard fetched once", () => {
    ok(!found.error, found.error);
    for (const [id, want, got] of found.value || []) eq(got, want, id);
    for (const [p, n] of Object.entries(B.calls)) ok(n === 1, p + " was fetched " + n + " times");
  });
}
