// node aws-saa-book/tools/web/tests/test_scoring.mjs [built folder]
// Covers scoring.js (ARCHITECTURE.md 7.1 and 9.1). Uses the built d/ and q/ files when they exist,
// the question files of the fixture book, and a small synthetic bank.
import fs from "node:fs";
import path from "node:path";
import { load, fixture, built, test, eq, ok, BOOK_DIR, JS_DIR } from "./harness.mjs";

const SAA = load(["scoring.js"]);
const S = SAA.Scoring;

/* ---------- question sources ---------- */

function synthetic() {
  const out = [];
  const domains = [1, 1, 1, 2, 2, 3, 3, 4];
  for (let i = 0; i < 8; i++) {
    const multi = i % 4 === 3;
    const three = i === 7;
    const ids = multi ? ["a", "b", "c", "d", "e"].concat(three ? ["f"] : []) : ["a", "b", "c", "d"];
    const right = multi ? (three ? ["b", "d", "f"] : ["b", "e"]) : [ids[i % 4]];
    out.push({
      id: "syn-q00" + (i + 1), ch: "syn", pool: "chapter", layer: i < 5 ? "core" : "extended", d: domains[i],
      topics: i % 2 ? ["identity"] : ["storage", "network"], concept: "c" + i, type: multi ? "multi" : "single",
      select: right.length, keyRev: 1,
      options: ids.map((id) => ({ id, text: "Option text " + id, ok: right.includes(id), concept: "c" + i + id }))
    });
  }
  return out;
}

// The raw question files of the fixture book, in the Q shape that the build emits.
function fromFixtureBook() {
  const dir = path.join(BOOK_DIR, "tools/tests/fixtures/book/data");
  const out = [];
  if (!fs.existsSync(dir)) return out;
  for (const name of fs.readdirSync(dir).sort()) {
    const file = path.join(dir, name, "questions.json");
    if (!fs.existsSync(file)) continue;
    const doc = JSON.parse(fs.readFileSync(file, "utf8"));
    for (const it of doc.items || []) {
      out.push({
        id: it.id, ch: it.chapter, pool: it.pool, layer: it.layer, d: it.domain, topics: it.topics || [],
        concept: it.concept, type: it.type, select: it.select, keyRev: it.keyRev,
        options: (it.options || []).map((o) => ({ id: o.id, text: o.text, ok: o.correct === true, concept: o.concept }))
      });
    }
  }
  return out;
}

function fromBuild() {
  const out = [];
  for (const rel of built("d").concat(built("q"))) {
    const doc = fixture(rel);
    for (const q of (doc && doc.questions) || []) out.push(Object.assign({ _file: rel }, q));
  }
  return out;
}

const BUILT = fromBuild();
const BANK = BUILT.concat(fromFixtureBook(), synthetic());
console.log("questions: " + BANK.length + " (" + BUILT.length + " from the built site)");

function rightIds(q) { return q.options.filter((o) => o.ok === true).map((o) => o.id); }

function subsets(list) {
  const out = [];
  for (let mask = 0; mask < (1 << list.length); mask++) {
    out.push(list.filter((_, i) => mask & (1 << i)));
  }
  return out;
}

/* ---------- isCorrect ---------- */

test("every question has exactly `select` correct options", () => {
  ok(BANK.length > 0, "no questions");
  for (const q of BANK) {
    eq(rightIds(q).length, q.select, q.id + " correct options");
    ok(q.type === "multi" ? q.select >= 2 : q.select === 1, q.id + " select does not fit type " + q.type);
  }
});

test("isCorrect: the correct set is true, in any order", () => {
  for (const q of BANK) {
    const right = rightIds(q);
    ok(S.isCorrect(q, right), q.id + " correct set");
    ok(S.isCorrect(q, right.slice().reverse()), q.id + " reversed");
    ok(S.isCorrect(q, right.concat(right)), q.id + " with repeated ids");
    const shuffled = Object.assign({}, q, { options: q.options.slice().reverse() });
    ok(S.isCorrect(shuffled, right), q.id + " with options in another order");
  }
});

test("isCorrect: every single wrong pick is false", () => {
  for (const q of BANK) {
    for (const o of q.options) {
      if (o.ok === true) continue;
      ok(!S.isCorrect(q, [o.id]), q.id + " wrong pick " + o.id);
    }
    ok(!S.isCorrect(q, []), q.id + " empty");
    ok(!S.isCorrect(q, null), q.id + " null");
    ok(!S.isCorrect(q, undefined), q.id + " undefined");
    ok(!S.isCorrect(q, ["zz"]), q.id + " unknown id");
  }
});

test("isCorrect: for multi, every strict subset and every superset is false", () => {
  let multi = 0;
  for (const q of BANK) {
    if (q.type !== "multi") continue;
    multi++;
    const right = rightIds(q);
    const all = q.options.map((o) => o.id);
    for (const pick of subsets(all)) {
      const same = pick.length === right.length && pick.every((id) => right.includes(id));
      eq(S.isCorrect(q, pick), same, q.id + " pick " + pick.join(","));
    }
  }
  ok(multi > 0, "no multi question in the bank");
});

test("isCorrect: a single question with a correct and a wrong pick is false", () => {
  for (const q of BANK) {
    if (q.type !== "single") continue;
    const wrong = q.options.find((o) => o.ok !== true);
    ok(!S.isCorrect(q, rightIds(q).concat([wrong.id])), q.id);
  }
});

/* ---------- scoreAttempt, domainBreakdown ---------- */

function answersFor(questions, fn) {
  const a = {};
  questions.forEach((q, i) => { const x = fn(q, i); if (x) a[q.id] = x; });
  return a;
}

const META = { id: "a-test-1", kind: "mock", ref: "mock-exam-1", startedAt: 1000, submittedAt: 2000, activeSec: 900,
  limitSec: 7800, build: "abc", over: 0, first: 1 };

test("scoreAttempt: all correct gives 100 and the domain counts add up", () => {
  // one attempt per source file (the same question can be in a d/ file and in a drill file)
  const groups = new Map();
  for (const q of BANK) {
    const key = q._file || q.ch || "other";
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(q);
  }
  for (const [name, qs] of groups) {
    eq(new Set(qs.map((q) => q.id)).size, qs.length, name + ": repeated question ids in one file");
    const doc = S.scoreAttempt(qs, answersFor(qs, (q) => ({ p: rightIds(q), u: 0, ms: 1200 })), META);
    eq(doc.pct, 100, name);
    eq(doc.correct, qs.length, name);
    eq(doc.total, qs.length, name);
    eq(doc.sureCorrect, qs.length, name);
    let n = 0, c = 0;
    for (const k of Object.keys(doc.domains)) { n += doc.domains[k].n; c += doc.domains[k].c; }
    eq(n, qs.length, name + " domain n sum");
    eq(c, qs.length, name + " domain c sum");
    for (const k of ["d1", "d2", "d3", "d4"]) ok(doc.domains[k], name + " missing " + k);
    eq(doc.order, qs.map((q) => q.id), name);
    eq(Object.keys(doc.answers).length, qs.length, name);
    // a mock file: the domain counts are the split of the file
    const file = name.startsWith("q/") ? fixture(name) : null;
    if (file && Array.isArray(file.split)) {
      eq(["d1", "d2", "d3", "d4"].map((k) => doc.domains[k].n), file.split, name + " domain split");
    }
  }
});

test("scoreAttempt: document shape, copied meta, missing and empty answers are wrong", () => {
  const qs = synthetic();
  const answers = answersFor(qs, (q, i) => {
    if (i === 0) return null;                              // missing
    if (i === 1) return { p: [], u: 1, ms: 10 };            // empty
    if (i === 2) return { p: rightIds(q), u: 1, ms: 50 };   // correct, not sure
    return { p: rightIds(q), u: 0, ms: 70.4 };
  });
  const order = qs.map((q) => q.id).reverse();
  const doc = S.scoreAttempt(qs, answers, Object.assign({}, META, { order, over: 1, first: 0 }));
  eq(doc.v, 1);
  eq([doc.id, doc.kind, doc.ref, doc.first, doc.over], ["a-test-1", "mock", "mock-exam-1", 0, 1]);
  eq([doc.startedAt, doc.submittedAt, doc.activeSec, doc.limitSec, doc.build], [1000, 2000, 900, 7800, "abc"]);
  eq(doc.total, 8);
  eq(doc.correct, 6);
  eq(doc.sureCorrect, 5);
  eq(doc.pct, 75);
  eq(doc.order, order);
  eq(doc.answers[qs[0].id], { p: [], ok: 0, u: 0, ms: 0 });
  eq(doc.answers[qs[1].id], { p: [], ok: 0, u: 1, ms: 10 });
  eq(doc.answers[qs[2].id].ok, 1);
  eq(doc.answers[qs[3].id].ms, 70);
  eq(doc.domains, { d1: { c: 1, n: 3 }, d2: { c: 2, n: 2 }, d3: { c: 2, n: 2 }, d4: { c: 1, n: 1 } });
  eq(doc.topics.identity, { c: 3, n: 4 });
  eq(doc.topics.storage, { c: 3, n: 4 });
  eq(JSON.parse(JSON.stringify(doc)), doc, "plain JSON");
});

test("scoreAttempt: pct is rounded, an empty attempt is 0", () => {
  const qs = synthetic().slice(0, 3);
  const doc = S.scoreAttempt(qs, answersFor(qs, (q, i) => (i < 2 ? { p: rightIds(q), u: 0, ms: 0 } : null)), META);
  eq(doc.pct, 67);
  eq(S.scoreAttempt([], {}, META).pct, 0);
});

test("domainBreakdown: n adds up to the total with wrong answers", () => {
  const seen = new Set();
  const qs = BANK.filter((q) => (seen.has(q.id) ? false : seen.add(q.id)));
  const d = S.domainBreakdown(qs, {});
  let n = 0, c = 0;
  for (const k of Object.keys(d)) { n += d[k].n; c += d[k].c; }
  eq(n, qs.length);
  eq(c, 0);
});

/* ---------- nextBox, record, inMistakes ---------- */

test("nextBox rules", () => {
  eq(S.nextBox(null, false, 0, 10), 0, "wrong, no record");
  eq(S.nextBox({ box: 3, d: 5 }, false, 0, 10), 0, "wrong resets");
  eq(S.nextBox({ box: 3, d: 5 }, true, 1, 10), 1, "correct but unsure caps at 1");
  eq(S.nextBox({ box: 0, d: 5 }, true, 1, 10), 0, "correct but unsure keeps 0");
  eq(S.nextBox({ box: 1, d: 5 }, true, 0, 10), 2, "correct and sure on another day");
  eq(S.nextBox({ box: 1, d: 10 }, true, 0, 10), 1, "correct and sure on the same day");
  eq(S.nextBox(null, true, 0, 10), 1, "first correct answer");
  eq(S.nextBox({ box: 0 }, true, 0, 10), 1, "no day of a correct answer yet");
});

test("record: history, flags, day, pick, cause, keyRev", () => {
  const q = { id: "x-q001", keyRev: 2, options: [] };
  const day = 86400;
  let now = 100 * day + 43200;
  let r = S.record(null, q, ["b"], false, 0, now, "W");
  eq([r.h, r.u, r.t, r.box, r.pick, r.c, r.kr], ["0", "0", now, 0, ["b"], "W", 2]);
  eq(r.d, null, "no correct answer yet");
  const r2 = S.record(r, q, ["a"], true, 1, now + 10);
  eq([r2.h, r2.u, r2.box, r2.c], ["01", "01", 0, "W"], "correct keeps the cause of the last wrong answer");
  eq(r2.d, S.dayOf(now + 10));
  const r3 = S.record(r2, q, ["a"], true, 0, now + 20);
  eq(r3.box, 0, "same day: no promotion");
  const r4 = S.record(r3, q, ["a"], true, 0, now + 2 * day);
  eq(r4.box, 1, "another day: promotion");
  const r5 = S.record(r4, q, ["c"], false, 0, now + 3 * day);
  eq([r5.box, r5.c, r5.d], [0, null, r4.d], "a new wrong answer clears the cause and keeps the day");
  const r6 = S.record(r5, q, ["c"], false, 0, now + 3 * day, "Z");
  eq(r6.c, null, "unknown cause code ignored");
  let long = null;
  for (let i = 0; i < 12; i++) long = S.record(long, q, ["a"], i % 2 === 0, 0, now + i);
  eq(long.h.length, 8);
  eq(long.h, "10101010");
  eq(long.h.slice(-1), "0");
  const fresh = S.record({ h: "0000", u: "0000", box: 0, kr: 1, c: "K", d: 3 }, q, ["a"], true, 0, now);
  eq([fresh.h, fresh.kr, fresh.c], ["1", 2, null], "a record of another keyRev is overwritten");
  const m = S.record(null, { id: "m", keyRev: 1 }, ["e", "b"], true, 0, now);
  eq(m.pick, ["b", "e"], "pick is sorted");
});

test("inMistakes", () => {
  ok(!S.inMistakes(null));
  ok(!S.inMistakes({ h: "111", u: "000", box: 1 }), "never wrong, never unsure");
  ok(S.inMistakes({ h: "011", u: "000", box: 1 }), "wrong once, box 1");
  ok(S.inMistakes({ h: "111", u: "010", box: 0 }), "unsure once");
  ok(!S.inMistakes({ h: "011", u: "000", box: 2 }), "box 2 leaves the log");
  ok(S.inMistakes({ h: "0", u: "0", box: 0 }));
});

/* ---------- mistakes, retryList, confusions ---------- */

function indexOf(questions, poolOf) {
  const qi = { v: 1, q: {}, wrong: {}, s: {} };
  for (const q of questions) {
    const pool = poolOf ? poolOf(q) : 0;
    qi.q[q.id] = [q.ch, q.d, q.layer === "core" ? 0 : 1, pool, q.concept, q.keyRev, q.topics];
    qi.wrong[q.id] = {};
    for (const o of q.options) if (!o.ok) qi.wrong[q.id][o.id] = o.concept;
  }
  return qi;
}

const SYN = synthetic();
const QI = indexOf(SYN);

test("mistakes: rows and order (sure but wrong, then box 0, then box 1, oldest first)", () => {
  const qstats = { v: 1, q: {
    "syn-q001": { h: "10", u: "00", t: 500, box: 0, pick: ["b"], c: "W", kr: 1 },   // sure but wrong
    "syn-q002": { h: "0", u: "0", t: 300, box: 0, pick: ["a"], c: null, kr: 1 },     // sure but wrong, older
    "syn-q003": { h: "0", u: "1", t: 100, box: 0, pick: ["a"], c: "K", kr: 1 },      // wrong and unsure: box 0 group
    "syn-q004": { h: "1", u: "1", t: 200, box: 0, pick: ["b", "e"], c: null, kr: 1 }, // right but not sure, box 0
    "syn-q005": { h: "01", u: "00", t: 50, box: 1, pick: ["a"], c: "C", kr: 1 },     // box 1
    "syn-q006": { h: "11", u: "00", t: 10, box: 2, pick: ["b"], c: null, kr: 1 },    // not a mistake
    "syn-q007": { h: "0", u: "0", t: 5, box: 0, pick: ["a"], c: null, kr: 9 },       // other keyRev: ignored
    "gone-q001": { h: "0", u: "0", t: 1, box: 0, pick: ["a"], c: null, kr: 1 }       // not in qindex
  } };
  const rows = S.mistakes(qstats, QI);
  eq(rows.map((r) => r.id), ["syn-q002", "syn-q001", "syn-q003", "syn-q004", "syn-q005"]);
  eq(rows[0], { id: "syn-q002", slug: "syn", d: 1, box: 0, last: "wrong", c: null, t: 300 });
  eq(rows.map((r) => r.last), ["wrong", "wrong", "wrong", "unsure", "wrong"]);
  eq(rows[1].c, "W");
  eq(S.retryList(qstats, QI), rows.map((r) => r.id));
  eq(S.retryList(qstats, QI, 2), ["syn-q002", "syn-q001"]);
  eq(S.mistakes({ v: 1, q: {} }, QI), []);
  eq(S.mistakes(null, QI), []);
});

test("confusions: pairs of the question concept and the picked option's concept", () => {
  const qstats = { v: 1, q: {
    "syn-q001": { h: "0", u: "0", t: 1, box: 0, pick: ["b"], kr: 1 },
    "syn-q002": { h: "10", u: "00", t: 2, box: 0, pick: ["a"], kr: 1 },
    "syn-q003": { h: "01", u: "00", t: 3, box: 1, pick: ["c"], kr: 1 }
  } };
  const out = S.confusions(qstats, QI);
  eq(out.length, 2);
  eq(out[0], { a: "c0", b: "c0b", n: 1 });
  eq(out[1], { a: "c1", b: "c1a", n: 1 });
});

/* ---------- buildMix ---------- */

function bigBank() {
  const out = [];
  const chapters = ["iam", "vpc", "s3", "ec2"];
  for (const ch of chapters) {
    for (let i = 1; i <= 12; i++) {
      out.push({ id: ch + "-q" + String(i).padStart(3, "0"), ch, d: 1 + (i % 4), layer: i <= 8 ? "core" : "extended",
        concept: ch + "-c" + i, keyRev: 1, topics: ["t" + (i % 3)],
        options: [{ id: "a", ok: true }, { id: "b", ok: false, concept: "x" }] });
    }
  }
  for (let i = 1; i <= 6; i++) {
    out.push({ id: "mock-exam-1-q" + String(i).padStart(3, "0"), ch: "mock-exam-1", d: 1, layer: "core", concept: "m" + i,
      keyRev: 1, topics: [], options: [{ id: "a", ok: true }, { id: "b", ok: false, concept: "x" }] });
  }
  return out;
}

const BIG = bigBank();
const BIG_QI = indexOf(BIG, (q) => (q.ch === "mock-exam-1" ? 2 : 0));
const ORDER = ["iam", "vpc", "s3", "ec2"];

function bigStats() {
  const q = {};
  // answered correctly a while ago (older group): iam core 1..5
  for (let i = 1; i <= 5; i++) q["iam-q00" + i] = { h: "1", u: "0", t: 100 + i, box: 2, d: 1, pick: ["a"], kr: 1 };
  // mistakes: vpc 1..4, and one mock question
  for (let i = 1; i <= 4; i++) q["vpc-q00" + i] = { h: "0", u: "0", t: 200 + i, box: 0, pick: ["b"], kr: 1 };
  q["mock-exam-1-q001"] = { h: "0", u: "0", t: 1, box: 0, pick: ["b"], kr: 1 };
  return { v: 1, sf: 0, q };
}

test("buildMix: 4 new core, 3 older, 3 mistakes; never pool mock; no repeats", () => {
  const stats = bigStats();
  const mix = S.buildMix(BIG_QI, stats, ["iam", "vpc"], ORDER, 20000);
  eq(mix.length, 10);
  eq(new Set(mix).size, 10, "repeated ids");
  ok(mix.every((id) => BIG_QI.q[id][3] !== 2), "a mock question is in the mix");
  const fresh = mix.filter((id) => !stats.q[id]);
  const older = mix.filter((id) => stats.q[id] && stats.q[id].h === "1");
  const missed = mix.filter((id) => stats.q[id] && stats.q[id].h === "0");
  eq([fresh.length, older.length, missed.length], [4, 3, 3]);
  ok(fresh.every((id) => BIG_QI.q[id][2] === 0), "new questions are core");
  ok(fresh.every((id) => ["iam", "vpc"].includes(BIG_QI.q[id][0])), "new questions come from chapters she has read");
  eq(fresh.slice().sort(), ["iam-q006", "iam-q007", "iam-q008", "vpc-q005"], "new questions in study order");
  eq(older.slice().sort(), ["iam-q001", "iam-q002", "iam-q003"], "largest age first");
  eq(missed.slice().sort(), ["vpc-q001", "vpc-q002", "vpc-q003"], "from the mistakes order");
});

test("buildMix: stable for the day, and shortfalls are filled from the other groups", () => {
  const stats = bigStats();
  const a = S.buildMix(BIG_QI, stats, ["iam", "vpc"], ORDER, 20000);
  const b = S.buildMix(BIG_QI, stats, ["vpc", "iam"], ORDER, 20000);
  eq(a, b, "same day, same mix");
  const c = S.buildMix(BIG_QI, stats, ["iam", "vpc"], ORDER, 20001);
  eq(c.slice().sort(), a.slice().sort(), "another day picks the same set from the same state");
  let differs = false;
  for (let day = 20001; day < 20012 && !differs; day++) {
    differs = JSON.stringify(S.buildMix(BIG_QI, stats, ["iam", "vpc"], ORDER, day)) !== JSON.stringify(a);
  }
  ok(differs, "the order never changes with the day");
  // nothing answered yet: all ten are new core questions of the read chapter, then the next read chapter
  const start = S.buildMix(BIG_QI, { v: 1, q: {} }, ["vpc", "s3"], ORDER, 5);
  eq(start.length, 10);
  eq(start.filter((id) => id.startsWith("vpc-")).length, 8);
  eq(start.filter((id) => id.startsWith("s3-")).length, 2);
  // nothing read and nothing answered: empty
  eq(S.buildMix(BIG_QI, { v: 1, q: {} }, [], ORDER, 5), []);
  // only mistakes exist
  const only = S.buildMix(BIG_QI, { v: 1, q: bigStats().q }, [], ORDER, 5);
  eq(only.length, 9, "5 older and 4 mistakes, no mock question");
  eq(S.buildMix(BIG_QI, stats, ["iam", "vpc"], ORDER, 20000, 5).length, 5);
});

test("returnQuestions: core questions from 1, 3 and 6 places back", () => {
  const order = ["a", "b", "c", "d", "e", "f", "g"];
  const bank = [];
  for (const ch of order) {
    for (let i = 1; i <= 3; i++) {
      bank.push({ id: ch + "-q00" + i, ch, d: 1, layer: i < 3 ? "core" : "extended", concept: "k", keyRev: 1, topics: [],
        options: [{ id: "a", ok: true }, { id: "b", ok: false, concept: "x" }] });
    }
  }
  const qi = indexOf(bank);
  eq(S.returnQuestions("g", order, qi, { q: {} }), ["f-q001", "d-q001", "a-q001"]);
  eq(S.returnQuestions("b", order, qi, { q: {} }), ["a-q001"]);
  eq(S.returnQuestions("a", order, qi, { q: {} }), []);
  eq(S.returnQuestions("zz", order, qi, { q: {} }), []);
  const stats = { q: { "f-q001": { h: "1", u: "0", t: 9, box: 2, kr: 1 }, "d-q002": { h: "0", u: "0", t: 9, box: 0, kr: 1 } } };
  eq(S.returnQuestions("g", order, qi, stats), ["f-q002", "d-q002", "a-q001"], "mistakes first, then never answered");
});

/* ---------- gate ---------- */

const CFG = { strong: 80, soft: 75, domainMin: 65, needed: 2 };

function mock(id, pct, t, extra) {
  const d = { c: pct, n: 100 };
  return Object.assign({ id, kind: "mock", ref: id, first: 1, over: 0, submittedAt: t, pct,
    domains: { d1: d, d2: d, d3: d, d4: d } }, extra || {});
}

test("gate: go, go-soft, not-yet", () => {
  eq(S.gate([], CFG).state, "not-yet");
  eq(S.gate([mock("m1", 90, 1)], CFG).state, "not-yet", "one mock is not enough");
  const go = S.gate([mock("m1", 82, 1), mock("m2", 80, 2)], CFG);
  eq([go.state, go.strong], ["go", 2]);
  eq(go.text, "2 of 2 mocks at 80%");
  const soft = S.gate([mock("m1", 76, 1), mock("m2", 85, 2)], CFG);
  eq([soft.state, soft.strong], ["go-soft", 1]);
  eq(soft.text, "1 of 2 mocks at 80%");
  eq(S.gate([mock("m1", 74, 1), mock("m2", 90, 2)], CFG).state, "not-yet", "one under the soft line");
  const weak = mock("m1", 78, 1, { domains: { d1: { c: 12, n: 20 }, d2: { c: 17, n: 17 }, d3: { c: 15, n: 15 }, d4: { c: 13, n: 13 } } });
  eq(S.gate([weak, mock("m2", 79, 2)], CFG).state, "not-yet", "a domain under the minimum blocks go-soft");
  const strongWeak = mock("m1", 85, 1, { domains: { d1: { c: 12, n: 20 }, d2: { c: 17, n: 17 }, d3: { c: 15, n: 15 }, d4: { c: 13, n: 13 } } });
  eq(S.gate([strongWeak, mock("m2", 85, 2)], CFG).state, "go", "both strong is go");
});

test("gate: an over attempt, a repeat and other kinds are ignored; the newest two count", () => {
  eq(S.gate([mock("m1", 90, 1), mock("m2", 95, 2, { over: 1 })], CFG).state, "not-yet", "over ignored");
  eq(S.gate([mock("m1", 90, 1), mock("m1", 95, 2, { first: 0 })], CFG).state, "not-yet", "repeat ignored");
  eq(S.gate([mock("m1", 90, 1), mock("x", 95, 2, { kind: "chapter" })], CFG).state, "not-yet", "quiz ignored");
  const newest = S.gate([mock("m1", 50, 1), mock("m2", 85, 2), mock("m3", 88, 3)], CFG);
  eq([newest.state, newest.strong], ["go", 2]);
  const old = S.gate([mock("m1", 90, 1), mock("m2", 91, 2), mock("m3", 60, 3)], CFG);
  eq(old.state, "not-yet", "the newest two decide");
});

/* ---------- buildCoach ---------- */

test("buildCoach: the coach document", () => {
  const stats = { v: 1, sf: 3, q: {
    "syn-q001": { h: "0", u: "0", t: 5, box: 0, pick: ["b"], c: "W", kr: 1 },
    "syn-q002": { h: "00", u: "00", t: 6, box: 0, pick: ["a"], c: "K", kr: 1 },
    "syn-q003": { h: "1", u: "1", t: 7, box: 0, pick: ["c"], c: null, kr: 1 },
    "syn-q004": { h: "1", u: "0", t: 8, box: 1, pick: ["b", "e"], c: null, kr: 1 },
    "syn-q005": { h: "1", u: "0", t: 9, box: 1, pick: ["a"], c: null, kr: 7 }
  } };
  const manifest = {
    counts: { questions: 640 },
    chapters: [
      { slug: "syn", status: "ready", sections: [
        ["predict", "fast", 2, "fast", 1, "Predict", null, "predict"],
        ["how", "deep", 2, "pass", 9, "How", null, "how"],
        ["how-a", "deep", 3, "pass", 3, "A", "how", "how"],
        ["how-b", "deep", 3, "full", 3, "B", "how", "how"],
        ["traps", "fast", 0, "fast", 0, "Traps", "predict", null]] },
      { slug: "done", status: "ready", sections: [["one", "fast", 2, "fast", 1, "One", null, "predict"]] },
      { slug: "later", status: "planned", sections: [] }]
  };
  const state = {
    settings: { examDate: "2026-11-20" },
    progress: { chapters: { syn: { read: { predict: 10, how: 10, "how-a": -12 } }, done: { read: { one: 3 } } } },
    qstats: stats,
    speak: { items: { "syn-s01": { t: 1, missing: ["kp2"] }, "syn-s02": { t: 1, missing: [] } } },
    attempts: [mock("mock-exam-1", 72, 50), { id: "a2", kind: "chapter", ref: "syn", pct: 40, submittedAt: 60 }]
  };
  const c = S.buildCoach(state, QI, manifest, 1234);
  eq([c.v, c.updatedAt, c.examDate], [1, 1234, "2026-11-20"]);
  eq(c.overall, { seen: 4, bank: 640, accuracy: 50, sureAccuracy: 33, mocks: [{ ref: "mock-exam-1", pct: 72 }] });
  eq(c.domains, { d1: { acc: 33, n: 3 }, d2: { acc: 100, n: 1 } });
  eq(c.missed, [{ id: "syn-q002", wrong: 2, lastPick: ["a"], c: "K" }, { id: "syn-q001", wrong: 1, lastPick: ["b"], c: "W" }]);
  eq(c.luckyGuesses, ["syn-q003"]);
  eq(c.whyCounts, { K: 1, C: 0, W: 1, T: 0, D: 0 });
  eq(c.unreadPass, ["syn"], "how-a is on the Pass route and its stamp is negative");
  eq(c.speakWeak, [{ id: "syn-s01", missing: ["kp2"] }]);
  eq(c.confusions.length, 2);
  ok(Array.isArray(c.weakTopics));
  eq(JSON.parse(JSON.stringify(c)), c, "plain JSON");
  const empty = S.buildCoach({}, QI, manifest, 1);
  eq(empty.overall.seen, 0);
  eq(empty.overall.accuracy, 0);
});

test("buildCoach: weak topics need three answers and list the chapters", () => {
  const q = {};
  for (let i = 1; i <= 8; i++) q["iam-q00" + i] = { h: i <= 6 ? "0" : "1", u: "0", t: i, box: 0, pick: ["b"], kr: 1 };
  const c = S.buildCoach({ qstats: { q } }, BIG_QI, { chapters: [] }, 1);
  ok(c.weakTopics.length > 0);
  for (const w of c.weakTopics) {
    ok(w.n >= 3 && w.acc < 80, JSON.stringify(w));
    eq(w.chapters, ["iam"]);
  }
  eq(c.overall.bank, Object.keys(BIG_QI.q).length, "bank falls back to the index size");
});

/* ---------- validQuestion ---------- */

test("validQuestion", () => {
  const dq = { id: "dr-a1", type: "single", select: 1, stem: "A company needs X. Which solution meets the requirement?",
    kw: ["needs X"], d: 1, options: [{ id: "a", text: "One", ok: true, why: "Because." }, { id: "b", text: "Two", ok: false, why: "No." }],
    expl: "Text", take: "Text", facts: [] };
  ok(S.validQuestion(dq));
  const edit = (fn) => { const c = JSON.parse(JSON.stringify(dq)); fn(c); return c; };
  ok(!S.validQuestion(null));
  ok(!S.validQuestion("iam-q003"));
  ok(!S.validQuestion(edit((c) => { c.options[1].ok = true; })), "two correct options for select 1");
  ok(!S.validQuestion(edit((c) => { c.options[0].ok = false; })), "no correct option");
  ok(!S.validQuestion(edit((c) => { c.expl_h = "<b>x</b>"; })), "an _h field on the question");
  ok(!S.validQuestion(edit((c) => { c.options[0].why_h = "<b>x</b>"; })), "an _h field on an option");
  ok(!S.validQuestion(edit((c) => { c.stem = " "; })), "empty stem");
  ok(!S.validQuestion(edit((c) => { c.options[1].id = "a"; })), "repeated option id");
  ok(!S.validQuestion(edit((c) => { c.options[0].ok = 1; })), "ok must be a boolean");
  ok(!S.validQuestion(edit((c) => { c.type = "multi"; })), "multi with select 1");
  ok(!S.validQuestion(edit((c) => { c.d = 5; })), "domain out of range");
  ok(!S.validQuestion(edit((c) => { c.options = [c.options[0]]; })), "one option");
  ok(!S.validQuestion(edit((c) => { c.stem = { html: "x" }; })), "stem is not text");
  ok(S.validQuestion(edit((c) => {
    c.type = "multi"; c.select = 2;
    c.options = [{ id: "a", text: "1", ok: true }, { id: "b", text: "2", ok: true }, { id: "c", text: "3", ok: false }];
  })), "a valid multi question");
  ok(S.validQuestion(edit((c) => { delete c.kw; delete c.d; delete c.expl; delete c.take; delete c.facts; })), "optional fields");
});

/* ---------- purity ---------- */

test("scoring.js adds only SAA.Scoring and reads no clock", () => {
  eq(Object.keys(SAA), ["Scoring"]);
  const src = fs.readFileSync(path.join(JS_DIR, "scoring.js"), "utf8");
  ok(!/\b(window|document)\s*[.[]|\b(localStorage|sessionStorage)\b/.test(src), "touches a browser global");
  ok(!/Date\.now\(|new Date\(\)/.test(src), "reads the clock");
});
