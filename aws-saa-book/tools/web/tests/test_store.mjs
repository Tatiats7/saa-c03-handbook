// Node test of store.js together with the stub (stubs/claude-stub.js): every degraded mode of
// ARCHITECTURE.md 5.6 without a browser. Run: node aws-saa-book/tools/web/tests/test_store.mjs
// Timers and the clock are virtual, so the file runs in well under a second.
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
function firstDir(list) {
  for (const p of list) { try { if (fs.statSync(p).isDirectory()) return p; } catch (e) { /* next */ } }
  return list[0];
}
const JS = firstDir([path.resolve(HERE, "../js"), path.resolve(HERE, "../web/js"), path.resolve("aws-saa-book/tools/web/js")]);
const STUB = path.join(firstDir([path.resolve(HERE, "../stubs"), path.resolve(HERE, "../web/stubs"),
  path.resolve("aws-saa-book/tools/web/stubs")]), "claude-stub.js");

let passed = 0, failed = 0, fails = [];
function ok(v, msg) { if (!v) fails.push(msg || "expected a true value"); }
function eq(a, b, msg) {
  const x = JSON.stringify(a), y = JSON.stringify(b);
  if (x !== y) fails.push((msg ? msg + ": " : "") + "got " + x + ", expected " + y);
}
async function test(name, fn) {
  fails = [];
  try { await fn(); } catch (e) { fails.push("threw " + (e && e.stack ? e.stack : JSON.stringify(e))); }
  if (fails.length) { failed++; process.exitCode = 1; console.log("FAIL " + name); fails.forEach((f) => console.log("     " + f)); }
  else { passed++; console.log("ok   " + name); }
}

function fakeStorage(seed) {
  const map = new Map(Object.entries(seed || {}));
  const s = {
    broken: false, writes: 0, map,
    getItem(k) { if (s.broken) throw new Error("blocked"); return map.has(k) ? map.get(k) : null; },
    setItem(k, v) { if (s.broken) throw new Error("blocked"); s.writes++; map.set(k, String(v)); },
    removeItem(k) { if (s.broken) throw new Error("blocked"); map.delete(k); }
  };
  return s;
}

// One page: its own storage (or a shared one, for "the same browser"), virtual timers, the stub, then the modules.
function makeEnv(opts = {}) {
  const ls = opts.ls || fakeStorage(opts.seed);
  if (opts.mode) ls.map.set("saaStub", opts.mode);
  if (opts.uid) ls.map.set("saaStubUid", opts.uid);
  ls.broken = !!opts.broken;
  const ss = fakeStorage();
  let now = opts.now || 1790000000000, seq = 0;
  const timers = [];
  const handlers = {};
  const events = [];
  const win = {
    localStorage: ls, sessionStorage: ss, console,
    location: { reload() {} },
    addEventListener(type, fn) { (handlers[type] = handlers[type] || []).push(fn); }
  };
  if (opts.broken) {
    // the stub must still read its own keys: only saa1: keys are blocked, as in the browser switch
    const g = ls.getItem, s = ls.setItem, r = ls.removeItem;
    ls.broken = false;
    const guard = (k) => { if (String(k).indexOf("saa1:") === 0) throw new Error("blocked"); };
    ls.getItem = (k) => { guard(k); return g(k); };
    ls.setItem = (k, v) => { guard(k); return s(k, v); };
    ls.removeItem = (k) => { guard(k); return r(k); };
  }
  const sandbox = {
    console, window: win, localStorage: ls,
    setTimeout(fn, ms) { const id = ++seq; timers.push({ id, at: now + (ms || 0), fn }); return id; },
    clearTimeout(id) { const i = timers.findIndex((t) => t.id === id); if (i >= 0) timers.splice(i, 1); },
    AbortSignal, AbortController, TextEncoder, Blob
  };
  const ctx = vm.createContext(sandbox);
  vm.runInContext("globalThis.SAA = {};", ctx);
  vm.runInContext(fs.readFileSync(STUB, "utf8"), ctx, { filename: STUB });
  for (const f of ["util.js", "merge.js", "store.js"]) {
    vm.runInContext(fs.readFileSync(path.join(JS, f), "utf8"), ctx, { filename: f });
  }
  const SAA = vm.runInContext("globalThis.SAA", ctx);
  SAA.Test.clock = () => now;
  SAA.state = { build: "testbuild", caps: {}, uid: null };
  SAA.bus.on("store:status", (d) => events.push(["status", d.status, d.consent]));
  SAA.bus.on("store:change", (d) => events.push(["change", d.doc, d.source]));
  const drain = () => new Promise((r) => setImmediate(r));
  async function tick(ms = 0) {
    const end = now + ms;
    for (let guard = 0; guard < 10000; guard++) {
      await drain();
      timers.sort((a, b) => a.at - b.at || a.id - b.id);
      if (!timers.length || timers[0].at > end) break;
      const t = timers.shift();
      now = Math.max(now, t.at);
      t.fn();
    }
    now = end;
    await drain();
  }
  const key = (k) => { const v = ls.map.get(k); return v === undefined ? null : JSON.parse(v); };
  // use() of the stub resolves on a timer, as on the platform; this wrapper moves the virtual clock for it
  const claude = {
    real: win.claude,
    get hot() { return win.claude.hot; },
    async use(name) { const p = win.claude.use(name); await tick(1); return p; }
  };
  return { SAA, Store: SAA.Store, claude, stub: win.claude.__stub, ls, win, tick, key, events, handlers,
    setNow(v) { now = v; }, now: () => now };
}

const UID = "stub-user";
const P = (p) => "study/" + UID + "/" + p;

await test("local only (db = null): patches are kept in memory and in browser storage", async () => {
  const e = makeEnv({ mode: "none" });
  const db = await e.claude.use("db");
  eq(db, null, "mode none: use() resolves null");
  e.Store.init();
  eq(e.Store.status(), "local");
  eq(await e.Store.attach(null, null), false);
  eq(e.Store.status(), "local");
  e.Store.patch("settings", { plan: "b", routeBy: { vpc: "full" } });
  e.Store.stamp("progress", ["chapters", "vpc", "read", "predict"], true);
  e.Store.stamp("progress", ["plan", "a", "d01", "t1"], true);
  e.Store.stamp("progress", ["plan", "a", "d01", "t1"], false);
  eq(e.Store.get("settings").plan, "b");
  eq(e.Store.get("settings").textSize, 1, "defaults stay");
  ok(e.Store.get("progress").chapters.vpc.read.predict > 0);
  ok(e.Store.get("progress").plan.a.d01.t1 < 0, "an undone stamp is negative");
  eq(e.key("saa1:progress"), null, "the save is debounced");
  await e.tick(450);
  eq(e.key("saa1:settings").settings.plan, "b", "saa1:settings holds the whole root");
  ok(e.key("saa1:settings").updatedAt > 0 && e.key("saa1:settings").createdAt > 0);
  ok(e.key("saa1:progress").chapters.vpc.read.predict > 0);
  e.Store.patch("ui", { route: "ch.vpc.deep", t: 5 });
  e.Store.draft("ask-q", "why is a NAT gateway zonal?");
  await e.tick(450);
  eq(e.key("saa1:ui").route, "ch.vpc.deep");
  eq(e.key("saa1:ui").updatedAt, undefined, "ui has no updatedAt");
  eq(e.Store.draft("ask-q"), "why is a NAT gateway zonal?");
  const e2 = makeEnv({ mode: "none", ls: e.ls });
  e2.Store.init();
  eq(e2.Store.get("settings").plan, "b", "a reload reads it back");
  eq(e2.Store.get("ui").route, "ch.vpc.deep");
  eq(e2.Store.draft("ask-q"), "why is a NAT gateway zonal?");
  e2.Store.draft("ask-q", "");
  eq(e2.Store.draft("ask-q"), "", "an empty string removes the draft");
});

await test("browser storage throws: status memory, everything still works until the tab closes", async () => {
  const e = makeEnv({ mode: "none", broken: true });
  e.Store.init();
  eq(e.Store.status(), "memory");
  eq(e.SAA.state.status, "memory");
  e.Store.patch("settings", { textSize: 2 });
  e.Store.patch("qstats", { sf: 3, q: { "vpc-q001": { h: "1", u: "0", t: 5, kr: 1, box: 1, pick: ["a"] } } });
  e.Store.replace("exam", { v: 1, id: "a-1", kind: "mock", ref: "mock-exam-1", phase: "run", cur: 0, ans: {} });
  e.Store.addAttempt({ v: 1, id: "a-1", kind: "mock", ref: "mock-exam-1", submittedAt: 100, pct: 70, total: 2, correct: 1, answers: { x: { p: ["a"], ok: 1 } } });
  e.Store.draft("d1", "text");
  e.Store.flag("question", "vpc-q001", "typo");
  await e.tick(3000);
  eq(e.Store.get("settings").textSize, 2);
  eq(e.Store.get("exam").phase, "run");
  eq(e.Store.attempts().length, 1);
  eq(e.Store.draft("d1"), "text");
  const snap = e.Store.snapshot();
  eq(snap.v, 1);
  ok(snap.attempts && snap.attempts["a-1"], "memory: the hot snapshot carries the attempts");
  eq(snap.drafts, { d1: "text" }, "and the drafts");
  ok(Object.keys(snap.outbox).some((k) => k.indexOf("flags/") === 0), "the flag waits in the outbox");
  const file = e.Store.exportAll();
  eq(file.qstats.q["vpc-q001"].h, "1", "Save my progress still has the data");
  eq(await e.Store.attach(null, null), false, "memory and no db together");
  eq(e.Store.status(), "memory");
  // a republish in the same tab: the snapshot is the only copy
  const e2 = makeEnv({ mode: "none", broken: true });
  e2.Store.init(JSON.parse(JSON.stringify(snap)));
  eq(e2.Store.get("exam").phase, "run", "the hot snapshot restores a running mock");
  eq(e2.Store.attempts().length, 1);
  eq(e2.Store.draft("d1"), "text");
  eq(e2.Store.get("settings").textSize, 2);
});

await test("export then import: a new browser gets everything back, and a second import changes nothing", async () => {
  const a = makeEnv({ mode: "none" });
  a.Store.init();
  a.Store.patch("settings", { plan: "c" });
  a.Store.stamp("progress", ["chapters", "iam", "read", "predict"], true);
  a.Store.patch("qstats", { sf: 2, q: { q1: { h: "01", u: "00", t: 9, kr: 1, box: 1 }, q2: { h: "0", u: "0", t: 8, kr: 1, box: 0, c: "W" } } });
  a.Store.patch("speak", { items: { s1: { t: 4, tries: 1, self: "10110" } } });
  a.Store.addAttempt({ v: 1, id: "a-9", kind: "chapter", ref: "iam", submittedAt: 50, pct: 50, total: 2, correct: 1, answers: {} });
  const file = JSON.parse(JSON.stringify(a.Store.exportAll()));
  eq(file.v, 1);
  eq(file.build, "testbuild");
  const b = makeEnv({ mode: "none", broken: true });
  b.Store.init();
  const res = b.Store.importAll(file);
  eq(res.ok, true);
  eq(res.counts.answers, 2);
  eq(res.counts.attempts, 1);
  eq(b.Store.get("settings").plan, "c");
  ok(b.Store.get("progress").chapters.iam.read.predict > 0);
  eq(Object.keys(b.Store.get("qstats").q).sort(), ["q1", "q2"]);
  eq(b.Store.get("speak").items.s1.self, "10110");
  eq(b.Store.attempts()[0].id, "a-9");
  const before = JSON.stringify(b.Store.exportAll().qstats);
  eq(b.Store.importAll(file).ok, true);
  eq(JSON.stringify(b.Store.exportAll().qstats), before, "importing twice changes nothing");
  eq(b.Store.importAll({ hello: 1 }).ok, false, "another JSON file is refused");
  eq(b.Store.importAll({ v: 1, qstats: [] }).ok, false);
  eq(b.Store.importAll(null).ok, false);
});

await test("cloud: attach merges, patches reach the db through the outbox, one document per path", async () => {
  const e = makeEnv({ mode: "ok" });
  const [db, user] = await Promise.all([e.claude.use("db"), e.claude.use("user")]);
  e.Store.init();
  e.Store.patch("settings", { plan: "b" });
  e.Store.stamp("progress", ["chapters", "vpc", "read", "predict"], true);
  eq(e.Store.status(), "local", "local until attach resolves");
  const uid = await user.id();
  eq(uid, UID);
  eq(await e.Store.attach(db, uid), true);
  eq(e.Store.status(), "cloud");
  await e.tick(100);
  eq(e.stub.db["study/" + UID].settings.plan, "b", "local settings from before the attach are sent");
  ok(e.stub.db["study/" + UID].lastSeenAt > 0 && e.stub.db["study/" + UID].createdAt > 0);
  ok(e.stub.db[P("state/progress")].chapters.vpc.read.predict > 0);
  ok(!(P("state/qstats") in e.stub.db), "an untouched default document is not written");
  ok(!(P("state/exam") in e.stub.db));
  e.Store.patch("qstats", { sf: 1, q: { q1: { h: "1", u: "0", t: 9, kr: 1, box: 1, pick: ["a"] } } });
  await e.tick(100);
  ok(!(P("state/qstats") in e.stub.db), "qstats waits 2 s after the last patch");
  await e.tick(2100);
  eq(e.stub.db[P("state/qstats")].q.q1.h, "1");
  e.Store.patch("qstats", { q: { q1: { h: "10", t: 12, pick: ["b", "c"] } } });
  await e.tick(2100);
  eq(e.stub.db[P("state/qstats")].q.q1, { h: "10", u: "0", t: 12, kr: 1, box: 1, pick: ["b", "c"] }, "update merges fields; arrays replace");
  e.Store.replace("exam", { v: 1, id: "a-2", kind: "mock", ref: "mock-exam-1", phase: "run", cur: 0, ans: {} });
  await e.tick(10);
  eq(e.stub.db[P("state/exam")].phase, "run", "exam is written at once");
  e.Store.patch("exam", { cur: 2, ans: { q7: { p: ["c"], u: 0, ms: 1000 } } });
  await e.tick(10);
  eq(e.stub.db[P("state/exam")].cur, 2);
  e.Store.addAttempt({ v: 1, id: "a-2", kind: "mock", ref: "mock-exam-1", first: 1, over: 0, submittedAt: 1790000100, pct: 72, total: 1, correct: 1, answers: {} });
  e.Store.replace("exam", null);
  e.Store.flag("fact", "vpc-natgw-bandwidth", "x".repeat(600));
  await e.tick(10);
  eq(e.stub.db[P("attempts/a-2")].pct, 72);
  eq(e.stub.db[P("state/exam")].none, 1, "a finished mock leaves {none: 1}");
  ok(!("phase" in e.stub.db[P("state/exam")]), "replace is a whole-document write");
  const flag = Object.keys(e.stub.db).filter((k) => k.indexOf(P("flags/")) === 0);
  eq(flag.length, 1);
  eq(e.stub.db[flag[0]].note.length, 500, "the note is cut to 500 characters");
  eq(e.stub.db[flag[0]].build, "testbuild");
  eq(e.Store.info().pending, 0, "the outbox is empty after the flush");
  ok(!Object.keys(e.stub.db).some((k) => k.indexOf("study/" + UID) !== 0), "every path is under study/<uid>");
  ok(e.events.some((x) => x[0] === "status" && x[1] === "cloud"));
});

await test("cloud with broken browser storage: saved online only", async () => {
  const e = makeEnv({ mode: "ok", broken: true });
  const db = await e.claude.use("db");
  e.Store.init();
  eq(e.Store.status(), "memory");
  eq(await e.Store.attach(db, UID), true);
  eq(e.Store.status(), "cloud");
  eq(e.Store.info().memory, true);
  e.Store.stamp("progress", ["daily", "20000", "pages"], true);
  await e.tick(2100);
  ok(e.stub.db[P("state/progress")].daily["20000"].pages > 0);
  // the next visit has nothing local and gets it back from the db
  const e2 = makeEnv({ mode: "ok", broken: true, ls: e.ls });
  e2.Store.init();
  eq(await e2.Store.attach(await e2.claude.use("db"), UID), true);
  ok(e2.Store.get("progress").daily["20000"].pages > 0, "progress comes back from the cloud");
});

await test("a new device never overwrites cloud settings or a running mock", async () => {
  const seedDb = {};
  seedDb["study/" + UID] = { v: 1, createdAt: 100, lastSeenAt: 1789999999, updatedAt: 500, settings: { plan: "c", route: "full", routeBy: { vpc: "full" }, textSize: 2 } };
  seedDb[P("state/exam")] = { v: 1, updatedAt: 600, id: "a-7", kind: "mock", ref: "mock-exam-1", phase: "run", cur: 11, activeMs: 99000, ans: {} };
  seedDb[P("state/progress")] = { v: 1, updatedAt: 550, chapters: { vpc: { read: { predict: 540 } } }, plan: {}, daily: {}, labs: {}, cards: {}, terms: {}, last: { route: "ch.vpc.fast", t: 540 } };
  seedDb[P("attempts/a-1")] = { v: 1, id: "a-1", kind: "mock", ref: "mock-exam-2", submittedAt: 400, pct: 81 };
  const e = makeEnv({ mode: "ok", seed: { saaStubDb: JSON.stringify(seedDb) } });
  const db = await e.claude.use("db");
  e.Store.init();
  eq(e.Store.get("settings").plan, "a", "defaults before the attach");
  eq(await e.Store.attach(db, UID), true);
  await e.tick(100);
  eq(e.Store.get("settings").plan, "c", "cloud settings arrive");
  eq(e.Store.get("settings").textSize, 2);
  eq(e.Store.get("exam").cur, 11, "the running mock arrives");
  ok(e.Store.get("progress").chapters.vpc.read.predict > 0);
  eq(e.Store.attempts().map((a) => a.id), ["a-1"]);
  eq(e.stub.db["study/" + UID].settings.plan, "c", "and the cloud copy is untouched");
  eq(e.stub.db["study/" + UID].updatedAt, 500, "lastSeenAt does not change updatedAt");
  eq(e.stub.db[P("state/exam")].cur, 11);
  eq(e.stub.db[P("state/exam")].updatedAt, 600);
  ok(e.events.some((x) => x[0] === "change" && x[2] === "remote"));
  // a write from another device arrives through onSnapshot and causes no write back
  const other = JSON.parse(JSON.stringify(e.stub.db[P("state/progress")]));
  other.updatedAt = 700;
  other.chapters.vpc.read.nat = 690;
  await db.doc(P("state/progress")).set(other);
  await e.tick(50);
  eq(e.Store.get("progress").chapters.vpc.read.nat, 690, "a remote change is merged into memory");
  eq(e.Store.info().pending, 0, "a snapshot never causes a write");
});

await test("errors mode: unavailable, one retry, then revoked: sync stops, nothing is lost", async () => {
  const e = makeEnv({ mode: "errors" });
  const db = await e.claude.use("db");
  e.Store.init();
  eq(await e.Store.attach(db, UID), true, "reads work, so the attach itself succeeds");
  await e.tick(50);
  eq(e.Store.status(), "cloud", "the first failed write is retried, the status stays");
  ok(e.Store.info().pending > 0);
  e.Store.stamp("progress", ["chapters", "s3", "read", "predict"], true);
  await e.tick(3200);
  eq(e.Store.status(), "local", "revoked ends cloud sync for the visit");
  eq(e.Store.info().stopped, true);
  ok(e.Store.info().pending > 0, "the outbox is kept");
  ok(e.Store.get("progress").chapters.s3.read.predict > 0, "the data is still in memory");
  await e.tick(500);
  ok(e.key("saa1:progress").chapters.s3.read.predict > 0, "and on this device");
  ok(e.key("saa1:outbox") && Object.keys(e.key("saa1:outbox")).length > 0, "the outbox is saved too");
  e.Store.stamp("progress", ["chapters", "s3", "read", "more"], true);
  await e.tick(5000);
  eq(Object.keys(e.stub.db).length, 0, "no write got through, and none is tried again");
  eq(await e.Store.attach(db, UID), false, "a stopped store does not attach again");
});

await test("another person on the same browser: local data moves to a backup and comes back", async () => {
  const a = makeEnv({ mode: "ok" });
  a.Store.init();
  eq(await a.Store.attach(await a.claude.use("db"), "u-anna"), true);
  a.Store.patch("settings", { plan: "b" });
  a.Store.stamp("progress", ["chapters", "vpc", "read", "predict"], true);
  await a.tick(2500);
  eq(a.key("saa1:uid"), "u-anna");
  const b = makeEnv({ mode: "ok", ls: a.ls });
  b.Store.init();
  eq(b.Store.get("settings").plan, "b", "before the id is known, the local data shows");
  eq(await b.Store.attach(await b.claude.use("db"), "u-ben"), true);
  await b.tick(500);
  eq(b.Store.get("settings").plan, "a", "the other person starts from defaults");
  eq(Object.keys(b.Store.get("progress").chapters).length, 0);
  eq(b.key("saa1:uid"), "u-ben");
  eq(b.key("saa1:bak:u-anna").docs.root.settings.plan, "b", "one backup of the first person's data");
  ok(!("study/u-ben/state/progress" in b.stub.db), "nothing of the first person is written under the second id");
  b.Store.patch("settings", { plan: "c" });
  await b.tick(2500);
  eq(b.stub.db["study/u-ben"].settings.plan, "c");
  eq(b.stub.db["study/u-anna"].settings.plan, "b");
  const c = makeEnv({ mode: "ok", ls: a.ls });
  c.Store.init();
  eq(await c.Store.attach(await c.claude.use("db"), "u-anna"), true);
  await c.tick(500);
  eq(c.Store.get("settings").plan, "b", "the first person gets her own data again");
  ok(c.Store.get("progress").chapters.vpc.read.predict > 0);
  eq(c.key("saa1:bak:u-anna"), null, "her backup is merged and removed");
});

await test("hot snapshot: a republish keeps documents, a running mock and the outbox", async () => {
  const e = makeEnv({ mode: "none" });
  e.Store.init();
  e.Store.replace("exam", { v: 1, id: "a-3", kind: "mock", ref: "mock-exam-1", phase: "run", cur: 2, activeMs: 61000, ans: { q1: { p: ["a"], u: 0, ms: 9 } } });
  e.Store.patch("exam", { cur: 3 });
  e.Store.get("exam").activeMs = 75000;      // the timer ticks without a patch
  e.Store.flag("section", "vpc.deep.nat", "unclear");
  const snap = JSON.parse(JSON.stringify(e.Store.snapshot()));
  ok(JSON.stringify(snap).length < 300000);
  ok(!("attempts" in snap), "with working storage the attempts are not in the snapshot");
  e.Store.reset();
  eq(e.Store.get("exam").none, 1, "reset returns the defaults");
  eq(e.key("saa1:exam"), null, "and clears the keys");
  e.Store.init(snap);
  eq(e.Store.get("exam").cur, 3);
  eq(e.Store.get("exam").activeMs, 75000);
  eq(e.Store.get("exam").ans, { q1: { p: ["a"], u: 0, ms: 9 } });
  ok(Object.keys(e.Store.snapshot().outbox).some((k) => k.indexOf("flags/") === 0), "the outbox is restored");
  e.Store.init({ v: 2, docs: { exam: { v: 1, updatedAt: 9e9, phase: "run", cur: 50 } } });
  eq(e.Store.get("exam").cur, 3, "a snapshot of another version is ignored");
});

await test("a finished mock stays finished: replace(null) wins over an older running copy", async () => {
  const e = makeEnv({ mode: "none" });
  e.Store.init();
  e.Store.replace("exam", { v: 1, id: "a-4", phase: "run", cur: 0, activeMs: 5000 });
  e.Store.patch("exam", { cur: 1 });
  e.Store.replace("exam", null);            // the same second as the patch
  await e.tick(500);
  eq(e.key("saa1:exam").none, 1);
  eq(e.Store.get("exam").phase, undefined);
  const e2 = makeEnv({ mode: "none", ls: e.ls });
  e2.Store.init();
  eq(e2.Store.get("exam").none, 1);
});

await test("two tabs: a save reads the key again and merges; the storage event updates memory", async () => {
  const e = makeEnv({ mode: "none" });
  e.Store.init();
  e.Store.stamp("progress", ["chapters", "vpc", "read", "a"], true);
  await e.tick(500);
  const other = e.key("saa1:progress");
  other.chapters.vpc.read.b = 1790000050;
  other.updatedAt = 1790000050;
  e.ls.map.set("saa1:progress", JSON.stringify(other));          // the other tab wrote
  e.Store.stamp("progress", ["chapters", "vpc", "read", "c"], true);
  await e.tick(500);
  eq(Object.keys(e.key("saa1:progress").chapters.vpc.read).sort(), ["a", "b", "c"], "nothing of the other tab is overwritten");
  eq(Object.keys(e.Store.get("progress").chapters.vpc.read).sort(), ["a", "b", "c"]);
  const again = e.key("saa1:progress");
  again.chapters.vpc.read.d = 1790000090;
  e.events.length = 0;
  (e.handlers.storage || []).forEach((fn) => fn({ key: "saa1:progress", newValue: JSON.stringify(again) }));
  ok(e.Store.get("progress").chapters.vpc.read.d > 0, "the storage event merges into memory");
  ok(e.events.some((x) => x[0] === "change" && x[1] === "progress" && x[2] === "remote"));
});

await test("attempts: newest first, the newest 40 keep their answers", async () => {
  const e = makeEnv({ mode: "none" });
  e.Store.init();
  for (let i = 1; i <= 45; i++) {
    e.Store.addAttempt({ v: 1, id: "a-" + i, kind: "mix", ref: "mix", submittedAt: 1000 + i, pct: 50, total: 1, correct: 0, order: ["q"], answers: { q: { p: [], ok: 0 } } });
  }
  const list = e.Store.attempts();
  eq(list.length, 45);
  eq(list[0].id, "a-45");
  eq(list.filter((a) => a.answers).length, 40);
  ok(!list[44].answers && list[44].pct === 50, "an older attempt keeps its summary");
  await e.tick(500);
  eq(Object.keys(e.key("saa1:attempts")).length, 45);
  ok(Object.keys(e.key("saa1:outbox")).filter((k) => k.indexOf("attempts/") === 0).length <= 40, "the outbox does not grow without a db");
});

await test("consent mode: no db call before the click; the status event carries the consent state", async () => {
  const e = makeEnv({ mode: "consent" });
  const [db, perms] = await Promise.all([e.claude.use("db"), e.claude.use("permissions")]);
  e.Store.init();
  eq(await perms.state("db"), "prompt");
  e.Store.consent("prompt");
  eq(e.events[e.events.length - 1], ["status", "local", "prompt"]);
  eq(e.Store.info().consent, "prompt");
  e.Store.patch("settings", { plan: "b" });
  await e.tick(3000);
  eq(await perms.state("db"), "prompt", "patching does not touch the db");
  eq(await e.Store.attach(db, UID), true);          // the "Save online too" click
  eq(await perms.state("db"), "granted");
  eq(e.Store.info().consent, null);
  await e.tick(100);
  eq(e.stub.db["study/" + UID].settings.plan, "b");
  const d = makeEnv({ mode: "ok" });
  d.Store.init();
  d.Store.consent("denied");
  eq(d.events[d.events.length - 1], ["status", "local", "denied"]);
});

await test("stub: path parity, update of a missing document, snapshots, queries", async () => {
  const e = makeEnv({ mode: "ok" });
  const db = await e.claude.use("db");
  let threw = "";
  try { db.doc("study/u1/state"); } catch (x) { threw = x.constructor.name + ":" + x.message; }
  ok(/TypeError/.test(threw) && /even/.test(threw), "an odd document path throws a TypeError: " + threw);
  threw = "";
  try { db.collection("study/u1"); } catch (x) { threw = x.message; }
  ok(/odd/.test(threw), "an even collection path throws");
  let code = "";
  try { await db.doc("a/b").update({ x: 1 }); } catch (x) { code = x.code; }
  eq(code, "invalid_argument", "update of a missing document");
  code = "";
  try { await db.doc("a/b").set([1]); } catch (x) { code = x.code; }
  eq(code, "invalid_argument", "a body must be an object");
  const seen = [];
  const un = db.doc("a/b").onSnapshot((s) => seen.push([s.exists, s.metadata.hasPendingWrites, s.exists ? s.data().n : null]), () => {});
  await e.tick(5);
  eq(seen, [[false, false, null]], "fires soon after subscribe");
  await db.doc("a/b").set({ n: 1, deep: { x: [1, 2], y: 1 } });
  await e.tick(5);
  eq(seen.slice(1), [[true, true, 1], [true, false, 1]], "own write: pending, then confirmed");
  await db.doc("a/b").update({ deep: { x: [3] } });
  await e.tick(5);
  const snap = await db.doc("a/b").get();
  eq(snap.data(), { n: 1, deep: { x: [3], y: 1 } }, "deep merge with arrays replaced");
  ok(Object.isFrozen(snap.data()) && Object.isFrozen(snap.data().deep), "snapshot data is frozen");
  un();
  await db.doc("a/b").set({ n: 2 });
  await e.tick(5);
  eq(seen.length, 5, "nothing after unsubscribe");
  await db.doc("a/c").set({ n: 5 });
  await db.doc("a/d").set({ n: 3 });
  await db.doc("a/d/sub/x").set({ n: 99 });
  const q = await db.collection("a").orderBy("n", "desc").limit(2).get();
  eq(q.docs.map((d) => d.id), ["c", "d"], "orderBy and limit; nested documents are not in the collection");
  eq((await db.collection("a").where("n", "<", 4).get()).size, 2);
  eq(JSON.parse(e.ls.map.get("saaStubDb"))["a/c"], { n: 5 }, "mirrored to saaStubDb");
  e.stub.reset();
  eq(Object.keys(e.stub.db).length, 0);
  eq(e.ls.map.has("saaStubDb"), false);
});

await test("stub: none, errors, user, downloads, sample, permissions", async () => {
  const none = makeEnv({ mode: "none" });
  for (const n of ["db", "user", "sample", "downloads", "permissions"]) eq(await none.claude.use(n), null, n + " is null in mode none");
  ok(!("hot" in none.claude.real), "no hot outside mode hot");

  const okEnv = makeEnv({ mode: "ok" });
  const user = await okEnv.claude.use("user");
  eq([await user.id(), await user.isOwner(), await user.canEdit(), await user.can("data.write")], ["stub-user", true, true, true]);
  ok(okEnv.claude.real.use("db") === okEnv.claude.real.use("db"), "use() is memoized");
  eq(await okEnv.claude.use("room"), null, "an unknown name resolves null");
  const dl = await okEnv.claude.use("downloads");
  eq(await dl.save({ filename: "saa-progress.json", data: "{}" }), { status: "saved" });
  eq(okEnv.win.__saaDownloads.length, 1);
  eq(okEnv.win.__saaDownloads[0].filename, "saa-progress.json");
  let code = "";
  try { await dl.save({ filename: "deck.apkg", data: "x" }); } catch (x) { code = x.code; }
  eq(code, "rejected_extension", ".apkg is not allowed");
  code = "";
  try { await dl.save({ filename: "a.txt", data: "" }); } catch (x) { code = x.code; }
  eq(code, "bad_request", "empty data");
  eq(await dl.save({ filename: "deck.zip", data: new Blob(["zip"]) }), { status: "saved" });
  const perms = await okEnv.claude.use("permissions");
  eq(await perms.state("db"), "granted");
  eq(await perms.state("nothing"), "unavailable");
  await perms.manage();

  const sample = await okEnv.claude.use("sample");
  const speakPrompt = "You are a speaking coach for an AWS Solutions Architect.\nREFERENCE\nKey points (id | must or nice | point)\nkp1 | must | A NAT gateway is zonal | accept: one per AZ\nkp2 | must | Private subnets route to it\nkp3 | nice | It is managed\nModel answer\nA NAT gateway...\nANSWER\n<<<\nA NAT gateway lives in one Availability Zone so I put one in each zone.\n>>>\nReply with one JSON object";
  const p1 = sample.json(speakPrompt, { modelTier: "default" });
  await okEnv.tick(30);
  const speak = await p1;
  eq(speak.covered.map((c) => c.kp).concat(speak.missing.map((m) => m.kp)), ["kp1", "kp2", "kp3"], "the speak reply uses the key point ids of the prompt");
  ok("A NAT gateway lives in one Availability Zone".indexOf(speak.covered[0].quote) === 0, "quotes come from the answer");
  eq(Object.keys(speak.moves).sort(), ["answer", "how", "watch", "you"]);
  const turns = [{ role: "user", content: "You answer questions about one section of a study book for the AWS SAA-C03 exam.\n\nBOOK\n[section] Amazon VPC > NAT gateways\nA NAT gateway is created in one Availability Zone. It needs an Elastic IP address.\n[summary]\nShort.\nFACTS\n" }, { role: "user", content: "Explain more simply" }];
  const p2 = sample.json(turns, { modelTier: "quick", cache: false });
  await okEnv.tick(30);
  const ask = await p2;
  eq(ask.status, "answered");
  eq(ask.support[0].quote, "A NAT gateway is created in one Availability Zone.", "the ask reply quotes the first sentence of BOOK");
  const ctl = new AbortController();
  const p3 = sample("hello", { signal: ctl.signal }).then(() => "resolved", (x) => x.code);
  ctl.abort();
  await okEnv.tick(30);
  eq(await p3, "cancelled");
  code = "";
  try { await sample.json([{ role: "assistant", content: "x" }]); } catch (x) { code = x.code; }
  eq(code, "invalid_request", "turns must start on a user turn");
  const p4 = sample("plain");
  await okEnv.tick(30);
  eq((await p4).truncated, false);

  const bad = makeEnv({ mode: "errors", seed: { saaStubCode: "refused" } });
  const s2 = await bad.claude.use("sample");
  const p5 = s2.json("x").then(() => "resolved", (x) => x.code);
  await bad.tick(30);
  eq(await p5, "refused", "errors mode rejects with saaStubCode");
  code = "";
  try { await (await bad.claude.use("downloads")).save({ filename: "a.txt", data: "x" }); } catch (x) { code = x.code; }
  eq(code, "declined");

  const part = makeEnv({ mode: "ok", seed: { saaStubCaps: "db, downloads" } });
  eq(await part.claude.use("db"), null, "saaStubCaps switches single capabilities off");
  ok((await part.claude.use("user")) !== null);

  const hot = makeEnv({ mode: "hot" });
  ok(hot.claude.hot && typeof hot.claude.hot.snapshot === "function" && typeof hot.win.__saaRepublish === "function");
  hot.claude.hot.snapshot(() => ({ v: 1, route: "#plan" }));
  hot.win.__saaRepublish();
  let got = null;
  hot.claude.hot.ready((d) => { got = d; });
  await hot.tick(5);
  eq(got, { v: 1, route: "#plan" }, "ready() gives back what __saaRepublish stored");
});

console.log((failed ? "FAILED " : "PASSED ") + passed + "/" + (passed + failed));
