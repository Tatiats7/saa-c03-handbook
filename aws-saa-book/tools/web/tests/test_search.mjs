// Tests of js/search-worker.js and Search.jump (owner E). Run: node aws-saa-book/tools/web/tests/test_search.mjs [built folder]
import fs from "node:fs";
import path from "node:path";
import { load, test, eq, ok, fixture, BUILT_DIR } from "./harness.mjs";

function worker() {
  const out = [];
  const self = { postMessage: (m) => out.push(m) };
  load(["search-worker.js"], { self });
  return {
    send(m) { out.length = 0; self.onmessage({ data: m }); return out[out.length - 1]; }
  };
}

const corpus = {
  v: 1,
  docs: [
    ["ch.vpc.fast.in-one-breath", "Amazon VPC", "In one breath", "s", "A VPC is your own network in one Region. A subnet lives in one Availability Zone."],
    ["ch.vpc.deep.nat-gateways", "Amazon VPC", "NAT gateways give private subnets a way out", "s", "A NAT gateway lets instances in a private subnet reach the internet. It needs a route & an Elastic IP <address>."],
    ["ch.vpc.deep.network-acls", "Amazon VPC", "Network ACLs are stateless", "s", "A network ACL checks every packet in both directions. Allow the request and the reply."],
    ["glossary.nat-gateway", "Glossary", "NAT gateway", "g", "A managed service that lets private subnets send traffic out."],
    ["fact.vpc-natgw-bandwidth", "Amazon VPC", "vpc-natgw-bandwidth", "f", "A NAT gateway supports a bandwidth that scales automatically."],
    ["quiz.vpc", "Amazon VPC", "Question", "q", "A company runs instances in private subnets that must download patches. Which gateway fits?"],
    ["ch.s3.fast.in-one-breath", "Amazon S3", "In one breath", "s", "Amazon S3 stores objects in buckets. Lifecycle rules move objects to colder storage."]
  ],
  aliases: { "network-acl": ["network ACL", "NACL"], "nat-gateway": ["NAT gateway", "NAT GW"] }
};

// The corpus above as the build emits it: aliases from search/index.json, then one shard per chapter.
function loaded(c) {
  const w = worker();
  w.send({ t: "aliases", aliases: c.aliases });
  w.send({ t: "shard", data: JSON.stringify({ v: 1, chapter: "vpc", docs: c.docs.slice(0, 6) }) });
  w.send({ t: "shard", data: JSON.stringify({ v: 1, chapter: "s3", docs: c.docs.slice(6) }) });
  return w;
}

test("aliases answer ready; each shard answers added with the docs so far; a broken shard is skipped", () => {
  const w = worker();
  eq(w.send({ t: "q", id: 1, text: "vpc" }).t, "error", "a query before any message is an error");
  eq(w.send({ t: "aliases", aliases: corpus.aliases }), { t: "ready", n: 0 });
  eq(w.send({ t: "q", id: 2, text: "vpc" }), { t: "r", id: 2, rows: [] }, "0 shards: no rows, no error");
  eq(w.send({ t: "shard", data: JSON.stringify({ v: 1, chapter: "vpc", docs: corpus.docs.slice(0, 6) }) }), { t: "added", n: 6 });
  eq(w.send({ t: "shard", data: "{broken" }).t, "skipped");
  eq(w.send({ t: "shard", data: JSON.stringify({ v: 1, chapter: "x" }) }).t, "skipped", "a shard without docs");
  eq(w.send({ t: "shard", docs: corpus.docs.slice(6) }), { t: "added", n: 7 }, "docs may be posted as an array");
});

test("the index builds from two shard messages and finds a term from each", () => {
  const w = worker();
  w.send({ t: "aliases", aliases: corpus.aliases });
  w.send({ t: "shard", data: JSON.stringify({ v: 1, chapter: "vpc", docs: corpus.docs.slice(0, 6) }) });
  eq(w.send({ t: "q", id: 1, text: "buckets" }).rows, [], "the second shard is not in yet");
  ok(w.send({ t: "q", id: 2, text: "subnet" }).rows.length > 0, "a query answers over the shards so far");
  w.send({ t: "shard", data: JSON.stringify({ v: 1, chapter: "s3", docs: corpus.docs.slice(6) }) });
  eq(w.send({ t: "q", id: 3, text: "buckets" }).rows.map((x) => x.route), ["ch.s3.fast.in-one-breath"], "a term of the second shard");
  eq(w.send({ t: "q", id: 4, text: "stateless" }).rows.map((x) => x.route), ["ch.vpc.deep.network-acls"], "a term of the first shard");
  eq(w.send({ t: "q", id: 5, text: "region" }).rows.map((x) => x.route), ["ch.vpc.fast.in-one-breath"]);
  const both = w.send({ t: "q", id: 6, text: "in one breath" }).rows.map((x) => x.route).slice(0, 2);
  eq(both, ["ch.vpc.fast.in-one-breath", "ch.s3.fast.in-one-breath"], "equal rank: doc ids follow the order of the shards");
  eq(w.send({ t: "q", id: 7, text: "NACL" }).rows.map((x) => x.route), ["ch.vpc.deep.network-acls"], "aliases apply to every shard");
});

test("query: exact, prefix, rank and the row shape", () => {
  const w = loaded(corpus);
  const r = w.send({ t: "q", id: 7, text: "NAT gateway" });
  eq(r.t, "r"); eq(r.id, 7);
  eq(r.rows[0].route, "ch.vpc.deep.nat-gateways", "two terms and heading matches come first, sections before glossary");
  eq(r.rows[1].route, "glossary.nat-gateway");
  eq(r.rows[2].route, "fact.vpc-natgw-bandwidth", "then facts");
  eq(Object.keys(r.rows[0]).sort(), ["chapter", "heading", "kind", "route", "snippet"]);
  ok(r.rows[0].snippet.includes("<mark>NAT</mark>"), "the hit is marked: " + r.rows[0].snippet);
  const p = w.send({ t: "q", id: 8, text: "lifecy" });
  eq(p.rows.map((x) => x.route), ["ch.s3.fast.in-one-breath"], "prefix match");
  ok(p.rows[0].snippet.includes("<mark>Lifecycle</mark>"), "the whole word is marked");
  eq(w.send({ t: "q", id: 9, text: "   " }).rows, [], "an empty query has no rows");
  eq(w.send({ t: "q", id: 10, text: "zzzzzz" }).rows, []);
});

test("query: one edit of distance and aliases", () => {
  const w = loaded(corpus);
  eq(w.send({ t: "q", id: 1, text: "gatway" }).rows.length >= 3, true, "a missing letter");
  eq(w.send({ t: "q", id: 2, text: "bukets" }).rows.map((x) => x.route), ["ch.s3.fast.in-one-breath"], "one edit");
  eq(w.send({ t: "q", id: 3, text: "stor" }).rows.length, 1, "four letters: prefix only");
  const a = w.send({ t: "q", id: 4, text: "NACL" });
  eq(a.rows.map((x) => x.route), ["ch.vpc.deep.network-acls"], "an alias finds the documents that use the other form");
  const b = w.send({ t: "q", id: 5, text: "nat gw" });
  ok(b.rows.some((x) => x.route === "glossary.nat-gateway"), "a two-word alias");
});

test("snippets are escaped and short; at most 30 rows", () => {
  const w = loaded(corpus);
  const r = w.send({ t: "q", id: 1, text: "elastic" });
  ok(r.rows[0].snippet.includes("&amp;") && r.rows[0].snippet.includes("&lt;address&gt;"), "escaped: " + r.rows[0].snippet);
  ok(!/<(?!\/?mark>)/.test(r.rows[0].snippet), "no tag other than mark");
  const many = { v: 1, docs: [], aliases: {} };
  for (let i = 0; i < 80; i++) many.docs.push(["ch.x.deep.s" + i, "X", "Heading " + i, "s", "filler ".repeat(60) + "needle " + "filler ".repeat(60)]);
  const w2 = worker();
  w2.send({ t: "aliases", aliases: {} });
  w2.send({ t: "shard", docs: many.docs });
  const rows = w2.send({ t: "q", id: 1, text: "needle" }).rows;
  eq(rows.length, 30);
  const plain = rows[0].snippet.replace(/<\/?mark>/g, "");
  ok(plain.length <= 142 && plain.includes("needle"), "about 140 characters around the hit, got " + plain.length);
});

const manifest = {
  chapters: [
    { slug: "vpc", id: "10", title: "Amazon VPC", status: "ready", sections: [
      ["nat-gateways", "deep", 3, "pass", 4, "NAT gateways give private subnets a way out", "how-it-works", "how"],
      ["network-acls", "deep", 3, "full", 4, "Network ACLs are stateless", "how-it-works", "how"]] },
    { slug: "nat-and-egress", id: "11", title: "NAT and egress", status: "planned", sections: [] }
  ],
  terms: [["nat-gateway", "NAT gateway"], ["network-acl", "network ACL"], ["alternate", "alternate"]]
};

test("Search.jump ranks prefix before substring, over titles, headings and glossary", () => {
  const SAA = load(["util.js", "search.js"]);
  const rows = SAA.Search.jump("nat", manifest);
  eq(rows.map((r) => r.route), ["ch.nat-and-egress", "glossary.nat-gateway", "ch.vpc.deep.nat-gateways", "glossary.alternate"],
    "prefix matches first (chapter, term, section), then the substring match");
  eq(rows[0].sub, "Not written yet", "a planned chapter says so");
  eq(rows[2], { route: "ch.vpc.deep.nat-gateways", title: "NAT gateways give private subnets a way out", sub: "Amazon VPC", kind: "section" });
  eq(SAA.Search.jump("ACL", manifest).map((r) => r.kind), ["term", "section"], "a word inside a title");
  eq(SAA.Search.jump("", manifest), []);
  eq(SAA.Search.jump("nat"), [], "no manifest yet: no rows");
  SAA.state = { manifest };
  eq(SAA.Search.jump("amazon").map((r) => r.route), ["ch.vpc"], "reads the manifest of the state");
});

// The page side (search.js): a fake sheet, a Worker that runs the real worker file, and Content files
// of which "late" ones resolve only when release() is called.
const wait = (ms) => new Promise((r) => setTimeout(r, ms));

function page(files) {
  const handlers = {}, box = { innerHTML: "", textContent: "" };
  const input = { value: "", nodeType: 1, focus() {}, closest: (sel) => (sel === ".srch-in" ? input : null) };
  const el = {
    querySelector: (sel) => ({ ".srch-full": box, ".srch-in": input })[sel] || { innerHTML: "", textContent: "" },
    addEventListener: (type, fn) => { handlers[type] = fn; }, contains: () => true
  };
  class Worker {
    constructor() {
      this.self = { postMessage: (m) => setTimeout(() => this.onmessage({ data: m }), 0) };
      load(["search-worker.js"], { self: this.self });
    }
    postMessage(m) { setTimeout(() => this.self.onmessage({ data: m }), 0); }
    terminate() {}
  }
  const late = [];
  const SAA = load(["util.js", "search.js"], { Worker, document: { addEventListener() {}, getElementById: () => null } });
  SAA.state = { manifest: { chapters: [], terms: [] } };
  SAA.Pop = { sheet: () => el };
  SAA.Content = {
    text: (p) => {
      const f = files[p];
      if (f === undefined) return Promise.reject({ path: p });
      if (!f.late) return Promise.resolve(f);
      return new Promise((resolve) => late.push(() => resolve(f.text)));
    }
  };
  SAA.Search.open();
  return {
    box, release: () => late.splice(0).forEach((go) => go()),
    type: async (text) => { input.value = text; handlers.input({ target: input }); await wait(250); }
  };
}

const shard = (chapter, docs) => JSON.stringify({ v: 1, chapter, docs });
const pageFiles = {
  "search/index.json": JSON.stringify({ v: 1, count: 7, aliases: corpus.aliases, shards: [
    { chapter: "vpc", path: "search/vpc.json", bytes: 0, count: 6 }, { chapter: "s3", path: "search/s3.json", bytes: 0, count: 1 }] }),
  "search/vpc.json": shard("vpc", corpus.docs.slice(0, 6)),
  "search/s3.json": { late: true, text: shard("s3", corpus.docs.slice(6)) }
};
const seen = {};
{
  const p = page(pageFiles);
  await p.type("NAT gateway");                     // the s3 shard is still on its way
  seen.loading = p.box.innerHTML;
  p.release();
  await wait(50);
  seen.done = p.box.innerHTML;
  await p.type("buckets");
  seen.second = p.box.innerHTML;
  const empty = page({ "search/index.json": JSON.stringify({ v: 1, count: 0, aliases: {}, shards: [] }) });
  await empty.type("buckets");
  seen.none = empty.box.innerHTML;
  const broken = page({});
  await broken.type("buckets");
  seen.broken = broken.box.textContent + broken.box.innerHTML;
}

test("page: answers over the shards so far, says 'Indexing n of m chapters', then the whole book", () => {
  ok(seen.loading.includes("Indexing 1 of 2 chapters") && seen.loading.includes('href="#ch.vpc.deep.nat-gateways"'),
    "first shard in: " + seen.loading.slice(0, 200));
  ok(!seen.done.includes("Indexing") && seen.done.includes('href="#ch.vpc.deep.nat-gateways"'), "all shards in: " + seen.done.slice(0, 200));
  ok(seen.second.includes('href="#ch.s3.fast.in-one-breath"'), "a term of the late shard: " + seen.second.slice(0, 200));
  ok(seen.none.includes("No text matches.") && !seen.none.includes("Indexing"), "0 shards: " + seen.none);
  ok(seen.broken.includes("Full-text search is not available right now."), "no index: " + seen.broken);
});

// With a built folder (the default selftest build, or the folder given as argument): the shards of the real book.
const index = fixture("search/index.json");
if (!index) {
  console.log("note: no search/index.json at " + BUILT_DIR + "; the tests of the built search shards are skipped");
} else {
  test("built: the index lists every built chapter; each shard parses and holds only its chapter's docs", () => {
    ok(!fs.existsSync(path.join(BUILT_DIR, "search/corpus.json")), "search/corpus.json must not be emitted");
    const manifest = fixture("manifest.json");
    const listed = index.shards.map((r) => r.chapter);
    manifest.chapters.filter((c) => c.status !== "planned").forEach((c) => ok(listed.includes(c.slug), "no shard for " + c.slug));
    let total = 0;
    index.shards.forEach((row) => {
      eq(row.path, "search/" + (row.chapter || "book") + ".json");
      eq(fs.statSync(path.join(BUILT_DIR, row.path)).size, row.bytes, row.path + " bytes");
      const shard = fixture(row.path);
      eq([shard.v, shard.chapter, shard.docs.length], [1, row.chapter, row.count], row.path);
      shard.docs.forEach((d) => {
        if (d[3] === "s") ok(d[0].indexOf("ch." + row.chapter + ".") === 0, row.path + ": " + d[0]);
        else if (d[3] === "q") eq(d[0], "quiz." + row.chapter, row.path);
        else if (d[3] === "g") eq(row.chapter, null, d[0] + " belongs to the book shard");
        else eq(d[3], "f", row.path + ": kind of " + d[0]);
      });
      total += row.count;
    });
    eq(index.count, total, "count of the index");
  });

  test("built: the worker indexes every shard in order and finds a heading of the first and of the last chapter", () => {
    const w = worker();
    eq(w.send({ t: "aliases", aliases: index.aliases }).t, "ready");
    let n = 0;
    index.shards.forEach((row) => {
      const text = fs.readFileSync(path.join(BUILT_DIR, row.path), "utf8");
      n += row.count;
      eq(w.send({ t: "shard", data: text }), { t: "added", n }, row.path);
    });
    const chapters = index.shards.filter((r) => r.chapter && fixture(r.path).docs.some((d) => d[3] === "s"));
    [chapters[0], chapters[chapters.length - 1]].filter(Boolean).forEach((row) => {
      const doc = fixture(row.path).docs.find((d) => d[3] === "s" && d[2]);
      const r = w.send({ t: "q", id: 1, text: doc[2] });
      ok(r.rows.some((x) => x.route.indexOf("ch." + row.chapter + ".") === 0), "heading '" + doc[2] + "' finds " + row.chapter);
    });
  });
}
