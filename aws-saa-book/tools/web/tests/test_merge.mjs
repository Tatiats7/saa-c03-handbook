// Node test of merge.js (ARCHITECTURE.md 9.1). Run: node aws-saa-book/tools/web/tests/test_merge.mjs
import { load, test, eq, ok } from "./harness.mjs";

const SAA = load(["merge.js"]);
const M = SAA.Merge;

test("deep: objects recurse, arrays and scalars replace, inputs stay unchanged", () => {
  const a = { x: { y: 1, z: [1, 2] }, k: 1 };
  const b = { x: { z: [3], w: 2 }, n: null };
  eq(M.deep(a, b), { x: { y: 1, z: [3], w: 2 }, k: 1, n: null });
  eq(a, { x: { y: 1, z: [1, 2] }, k: 1 });
  eq(M.deep(null, { a: 1 }), { a: 1 });
  eq(M.deep({ a: 1 }, undefined), { a: 1 });
});

test("stamps: union of keys, larger absolute value wins, recursive", () => {
  eq(M.stamps({ a: 10, b: 5 }, { b: 7, c: 3 }), { a: 10, b: 7, c: 3 });
  eq(M.stamps({ d03: { t1: 100 } }, { d03: { t2: 50 }, d04: { t1: 1 } }), { d03: { t1: 100, t2: 50 }, d04: { t1: 1 } });
  eq(M.stamps(null, { a: 1 }), { a: 1 });
  eq(M.stamps({ a: 1 }, undefined), { a: 1 });
});

test("stamps: the undo case (a later negative stamp beats an earlier tick, on both sides)", () => {
  eq(M.stamps({ t1: 100 }, { t1: -120 }), { t1: -120 });
  eq(M.stamps({ t1: -120 }, { t1: 100 }), { t1: -120 });
  eq(M.stamps({ t1: -120 }, { t1: 130 }), { t1: 130 });
  eq(M.stamps({ t1: 100 }, { t1: -100 }), { t1: -100 }, "a tie goes to undone");
  eq(M.stamps({ t1: -100 }, { t1: 100 }), { t1: -100 }, "a tie is the same from both sides");
});

test("doc progress: stamps merge, last by later t, chapter last by later updatedAt", () => {
  const l = {
    v: 1, updatedAt: 200,
    chapters: { vpc: { read: { a: 100, b: -150 }, last: "deep.x", skips: { s1: 5 } }, iam: { read: { p: 1 } } },
    plan: { a: { d01: { t1: 10 } } }, daily: { "20000": { pages: 10 } }, labs: { "vpc-t02": { steps: { "1": 5 }, cleaned: 0 } },
    cards: { vpc: 9 }, terms: {}, last: { route: "ch.vpc.deep.x", t: 180 }
  };
  const r = {
    v: 1, updatedAt: 150,
    chapters: { vpc: { read: { b: 140, c: 20 }, last: "fast.y" }, s3: { read: { q: 2 } } },
    plan: { a: { d01: { t1: -20, t2: 30 } } }, daily: { "20000": { words: 12 } }, labs: { "vpc-t02": { steps: { "2": 6 }, cleaned: 99 } },
    cards: {}, terms: { idempotent: 3 }, last: { route: "ch.s3.fast", t: 190 }
  };
  const m = M.doc("progress", l, r);
  eq(m.updatedAt, 200);
  eq(m.chapters.vpc.read, { a: 100, b: -150, c: 20 });
  eq(m.chapters.vpc.last, "deep.x", "the newer document gives the chapter's last");
  eq(m.chapters.vpc.skips, { s1: 5 });
  eq(m.chapters.iam, { read: { p: 1 } });
  eq(m.chapters.s3, { read: { q: 2 } });
  eq(m.plan, { a: { d01: { t1: -20, t2: 30 } } });
  eq(m.daily, { "20000": { pages: 10, words: 12 } });
  eq(m.labs, { "vpc-t02": { steps: { "1": 5, "2": 6 }, cleaned: 99 } });
  eq(m.terms, { idempotent: 3 });
  eq(m.last, { route: "ch.s3.fast", t: 190 }, "last by its own t, not by updatedAt");
  const back = M.doc("progress", r, l);
  ok(M.same(back.chapters, m.chapters), "chapters merge the same from both sides (key order aside)");
  ok(M.same(back.plan, m.plan), "plan stamps merge the same from both sides");
  eq(back.last, m.last);
});

test("doc qstats: the record with the later t wins; sf is the larger", () => {
  const l = { v: 1, updatedAt: 10, sf: 12, q: { a: { h: "01", t: 100, kr: 1 }, b: { h: "1", t: 50, kr: 1 } } };
  const r = { v: 1, updatedAt: 20, sf: 7, q: { a: { h: "0", t: 90, kr: 1 }, c: { h: "1", t: 5, kr: 1 } } };
  const m = M.doc("qstats", l, r);
  eq(m.q.a, { h: "01", t: 100, kr: 1 });
  eq(Object.keys(m.q).sort(), ["a", "b", "c"]);
  eq(m.sf, 12);
  eq(m.updatedAt, 20);
});

test("doc qstats: a record of another keyRev is ignored", () => {
  const l = { v: 1, updatedAt: 10, sf: 0, q: { a: { h: "111", t: 500, kr: 1 }, b: { h: "1", t: 9, kr: 1 } } };
  const r = { v: 1, updatedAt: 20, sf: 0, q: { a: { h: "0", t: 100, kr: 2 } } };
  eq(M.doc("qstats", l, r).q.a, { h: "0", t: 100, kr: 2 }, "the newer key revision wins over a later t");
  eq(M.doc("qstats", r, l).q.a, { h: "0", t: 100, kr: 2 });
  const withIndex = M.doc("qstats", l, r, { kr: { a: 3, b: 1 } });
  ok(!("a" in withIndex.q), "both records belong to an old key: dropped");
  eq(withIndex.q.b, { h: "1", t: 9, kr: 1 });
  const keepOne = M.doc("qstats", l, r, { kr: { a: 1 } });
  eq(keepOne.q.a, { h: "111", t: 500, kr: 1 }, "qindex decides which record is live");
});

test("doc speak: per item the later t; tries travel with the item", () => {
  const l = { v: 1, updatedAt: 5, items: { s1: { t: 10, tries: 3, self: "11111" }, s2: { t: 1, tries: 1 } } };
  const r = { v: 1, updatedAt: 9, items: { s1: { t: 8, tries: 2, self: "00000" }, s3: { t: 2, tries: 1 } } };
  const m = M.doc("speak", l, r);
  eq(m.items.s1, { t: 10, tries: 3, self: "11111" });
  eq(Object.keys(m.items).sort(), ["s1", "s2", "s3"]);
  eq(m.updatedAt, 9);
});

test("doc root and exam: the whole document with the later updatedAt", () => {
  const l = { v: 1, createdAt: 50, lastSeenAt: 300, updatedAt: 100, settings: { plan: "a", route: "pass", routeBy: { vpc: "full" } } };
  const r = { v: 1, createdAt: 40, lastSeenAt: 200, updatedAt: 120, settings: { plan: "b", route: "fast", routeBy: {} } };
  const m = M.doc("root", l, r);
  eq(m.settings, { plan: "b", route: "fast", routeBy: {} }, "settings are not merged field by field");
  eq(m.createdAt, 40);
  eq(m.lastSeenAt, 300);
  eq(m.updatedAt, 120);
  const e1 = { v: 1, updatedAt: 100, phase: "run", cur: 3, activeMs: 5000 };
  const e2 = { v: 1, updatedAt: 101, none: 1 };
  eq(M.doc("exam", e1, e2), e2);
  eq(M.doc("exam", e2, e1), e2);
  const e3 = { v: 1, updatedAt: 100, phase: "run", cur: 3, activeMs: 9000 };
  eq(M.doc("exam", e1, e3).activeMs, 9000, "same updatedAt: the copy with more active time");
  eq(M.doc("exam", e3, e1).activeMs, 9000);
});

test("a default document with updatedAt 0 never wins over an existing root or exam", () => {
  const defRoot = { v: 1, createdAt: 0, lastSeenAt: 0, updatedAt: 0, settings: { plan: "a", route: "pass" } };
  const cloudRoot = { v: 1, createdAt: 10, lastSeenAt: 20, updatedAt: 15, settings: { plan: "c", route: "full" } };
  eq(M.doc("root", defRoot, cloudRoot).settings, cloudRoot.settings);
  eq(M.doc("root", cloudRoot, defRoot).settings, cloudRoot.settings);
  eq(M.doc("root", defRoot, cloudRoot).createdAt, 10, "createdAt 0 is not a time");
  const defExam = { v: 1, updatedAt: 0, none: 1 };
  const running = { v: 1, updatedAt: 77, phase: "run", id: "a-1", cur: 4 };
  eq(M.doc("exam", defExam, running), running);
  eq(M.doc("exam", running, defExam), running);
});

test("doc: a missing side gives the other side, as a copy", () => {
  const d = { v: 1, updatedAt: 3, q: { a: { t: 1 } }, sf: 0 };
  const m = M.doc("qstats", d, null);
  eq(m, d);
  ok(m !== d && m.q !== d.q, "a copy, not the same object");
  eq(M.doc("qstats", null, d), d);
  eq(M.doc("qstats", null, null), null);
});

test("attempts: union by id; an attempt is immutable; a copy with answers beats a trimmed one", () => {
  const a = { x: { id: "x", pct: 70, answers: { q: 1 } }, y: { id: "y", pct: 50 } };
  const b = [{ id: "y", pct: 50, answers: { q: 2 } }, { id: "z", pct: 90 }, { id: "x", pct: 1 }];
  const m = M.attempts(a, b);
  eq(Object.keys(m).sort(), ["x", "y", "z"]);
  eq(m.x.pct, 70);
  eq(m.y.answers, { q: 2 });
  eq(M.attempts(null, null), {});
});

test("diff then deep is a round trip", () => {
  const cases = [
    [{ a: 1, b: { c: 2, d: [1, 2] } }, { a: 1, b: { c: 3, d: [1, 2], e: { f: 1 } }, g: "x" }],
    [{}, { a: { b: { c: 1 } } }],
    [{ a: [1, 2, 3] }, { a: [1, 2] }],
    [{ a: { b: 1 } }, { a: { b: 1 } }],
    [{ a: 1 }, { a: { b: 1 } }],
    [{ a: { b: 1 } }, { a: 5 }],
    [null, { a: 1 }]
  ];
  for (const [base, next] of cases) {
    const p = M.diff(base, next);
    eq(M.deep(base, p), next);
  }
  eq(M.diff({ a: 1, b: { c: 2 } }, { a: 1, b: { c: 2 } }), {}, "no change gives an empty patch");
  eq(M.diff({ a: 1, b: { c: 2, d: 3 } }, { a: 1, b: { c: 2, d: 4 } }), { b: { d: 4 } }, "the smallest patch");
});

test("exportAll then importAll, through the merge functions that importAll uses", () => {
  const state = {
    root: { v: 1, createdAt: 5, lastSeenAt: 9, updatedAt: 8, settings: { plan: "b", routeBy: { vpc: "full" } } },
    progress: { v: 1, updatedAt: 7, chapters: { vpc: { read: { a: 3 } } }, plan: { b: { d01: { t1: 4 } } }, daily: {}, labs: {}, cards: {}, terms: {}, last: { route: "ch.vpc", t: 6 } },
    qstats: { v: 1, updatedAt: 7, sf: 3, q: { q1: { h: "10", u: "00", t: 6, kr: 1, box: 0 } } },
    speak: { v: 1, updatedAt: 2, items: { s1: { t: 2, tries: 1, self: "10101" } } },
    attempts: { a1: { id: "a1", kind: "mock", pct: 72, answers: { q1: { p: ["a"], ok: 1 } } } }
  };
  const file = JSON.parse(JSON.stringify({ v: 1, build: "x", exportedAt: 10, ...state, coach: null }));
  const fresh = {
    root: { v: 1, createdAt: 0, lastSeenAt: 0, updatedAt: 0, settings: { plan: "a", routeBy: {} } },
    progress: { v: 1, updatedAt: 0, chapters: {}, plan: {}, daily: {}, labs: {}, cards: {}, terms: {}, last: null },
    qstats: { v: 1, updatedAt: 0, sf: 0, q: {} },
    speak: { v: 1, updatedAt: 0, items: {} }
  };
  for (const name of ["root", "progress", "qstats", "speak"]) {
    eq(M.doc(name, fresh[name], file[name]), state[name], name + " comes back on a new device");
    eq(M.doc(name, state[name], file[name]), state[name], name + " is unchanged when imported twice");
  }
  eq(M.attempts({}, file.attempts), state.attempts);
  const later = JSON.parse(JSON.stringify(state.progress));
  later.updatedAt = 20;
  later.chapters.vpc.read.b = 19;
  eq(M.doc("progress", later, file.progress).chapters.vpc.read, { a: 3, b: 19 }, "an import adds, it does not remove newer work");
});
