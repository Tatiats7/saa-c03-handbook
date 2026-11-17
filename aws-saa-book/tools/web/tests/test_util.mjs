// Tests of util.js, router.js (parse and href) and content.js (section counting), ARCHITECTURE.md 9.1.
// Run: node aws-saa-book/tools/web/tests/test_util.mjs
import { load, test, eq, ok } from "./harness.mjs";

const SAA = load(["util.js", "router.js"], { location: { hash: "" } });
const U = SAA.U;
const R = SAA.Router;

test("esc escapes the five characters and tolerates null", () => {
  eq(U.esc("<a href=\"x\">'&'</a>"), "&lt;a href=&quot;x&quot;&gt;&#39;&amp;&#39;&lt;/a&gt;");
  eq(U.esc(null), "");
  eq(U.esc(undefined), "");
  eq(U.esc(0), "0");
});

test("h escapes plain values and returns SafeHtml", () => {
  const out = U.h`<p class="${"a\"b"}">${"<b>x</b>"}</p>`;
  ok(out.__safe === true, "has __safe");
  eq(out.s, "<p class=\"a&quot;b\">&lt;b&gt;x&lt;/b&gt;</p>");
  eq(String(out), out.s, "toString gives s");
});

test("h inserts nested h, arrays of SafeHtml and raw without escaping", () => {
  const li = ["a<", "b"].map((t) => U.h`<li>${t}</li>`);
  const out = U.h`<ul>${li}</ul>${U.h`<i>${"&"}</i>`}${U.raw("<hr>")}`;
  eq(out.s, "<ul><li>a&lt;</li><li>b</li></ul><i>&amp;</i><hr>");
});

test("h gives an empty string for null, undefined and false, and keeps 0", () => {
  eq(U.h`[${null}${undefined}${false}${0}${""}]`.s, "[0]");
});

test("h escapes a plain object that only looks safe", () => {
  eq(U.h`${{ __safe: true, s: 5 }}`.s, "[object Object]");
  eq(U.h`${["<", U.raw("<br>")]}`.s, "&lt;<br>", "a mixed array escapes its plain members");
});

test("join joins SafeHtml values and drops empty ones", () => {
  eq(U.join([U.h`<b>a</b>`, null, U.h`<b>b</b>`], ", ").s, "<b>a</b>, <b>b</b>");
  eq(U.join(["<", ">"], U.raw("<br>")).s, "&lt;<br>&gt;");
});

test("set refuses a plain string", () => {
  const el = { innerHTML: "", textContent: "x" };
  let threw = false;
  try { U.set(el, "<b>no</b>"); } catch (e) { threw = true; }
  ok(threw, "threw on a string");
  U.set(el, U.h`<b>${"yes"}</b>`);
  eq(el.innerHTML, "<b>yes</b>");
  U.set(el, null);
  eq(el.textContent, "");
});

test("norm lowers case, straightens quotes and joins spaces", () => {
  eq(U.norm("  The “NAT”  gateway’s\n zone "), "the \"nat\" gateway's zone");
  eq(U.norm(null), "");
});

test("bytes counts UTF-8 bytes", () => {
  eq(U.bytes("abc"), 3);
  eq(U.bytes("é"), 2);
  eq(U.bytes("€"), 3);
  eq(U.bytes("😀"), 4);
  eq(U.bytes(""), 0);
});

test("now and nowMs follow Test.clock", () => {
  SAA.Test.clock = () => 1790000000999;
  eq(U.nowMs(), 1790000000999);
  eq(U.now(), 1790000000);
  SAA.Test.clock = null;
  ok(Math.abs(U.nowMs() - Date.now()) < 2000, "real clock without Test.clock");
});

test("fmtClock and fmtMin", () => {
  eq(U.fmtClock(0), "0:00");
  eq(U.fmtClock(65), "1:05");
  eq(U.fmtClock(3725), "1:02:05");
  eq(U.fmtMin(20), "20 min");
  eq(U.fmtMin(150), "150 min");
  eq(U.fmtMin(200), "3 h 20 min");
});

test("rng is stable for a seed and shuffle keeps the members", () => {
  const a = U.rng(42), b = U.rng(42);
  eq([a(), a(), a()], [b(), b(), b()]);
  const s1 = U.shuffle([1, 2, 3, 4, 5, 6], U.rng("day-1"));
  const s2 = U.shuffle([1, 2, 3, 4, 5, 6], U.rng("day-1"));
  eq(s1, s2);
  eq(s1.slice().sort(), [1, 2, 3, 4, 5, 6]);
});

test("clone, uid, debounce exist and behave", () => {
  const o = { a: [1, { b: 2 }] };
  const c = U.clone(o);
  eq(c, o);
  ok(c.a !== o.a, "deep copy");
  ok(U.uid("a") !== U.uid("a"), "two ids differ");
  ok(/^a-[a-z0-9]+-[a-z0-9]+$/.test(U.uid("a")), "id matches the route alphabet");
  ok(typeof U.debounce(() => {}, 10).cancel === "function");
});

test("bus delivers, removes, and survives a throwing listener", () => {
  let n = 0;
  const quiet = console.error;
  console.error = () => {};
  const bad = SAA.bus.on("x", () => { throw new Error("boom"); });
  const fn = SAA.bus.on("x", (d) => { n += d; });
  SAA.bus.emit("x", 2);
  SAA.bus.off("x", fn);
  SAA.bus.off("x", bad);
  SAA.bus.emit("x", 5);
  console.error = quiet;
  eq(n, 2);
});

const DOMAINS = [
  { id: 1, title: "Design Secure Architectures", weight: 30 },
  { id: 2, title: "Design Resilient Architectures", weight: 26 },
  { id: 3, title: "Design High-Performing Architectures", weight: 24 },
  { id: 4, title: "Design Cost-Optimized Architectures", weight: 20 }
];

test("bstrip with on: four weighted segments and a label in words", () => {
  const s = U.bstrip(DOMAINS, { on: [1, 3] }).s;
  eq((s.match(/class="bstrip-s/g) || []).length, 4);
  ok(s.startsWith("<div class=\"bstrip\" role=\"img\" aria-label=\""), "wrapper");
  ok(s.includes("class=\"bstrip-s is-on\" style=\"flex-grow:30\" data-d=\"1\""), "D1 on with weight");
  ok(s.includes("class=\"bstrip-s\" style=\"flex-grow:26\" data-d=\"2\""), "D2 off");
  ok(s.includes(">D1</span>") && s.includes(">D4</span>"), "segment text");
  ok(s.includes("Domain 1, Design Secure Architectures: covered by this chapter"), "label says on");
  ok(s.includes("Domain 2, Design Resilient Architectures: not covered by this chapter"), "label says off");
});

test("bstrip with pct: percent as text and a state class from the gate", () => {
  const gate = { strong: 80, soft: 75, domainMin: 65, needed: 2 };
  const s = U.bstrip(DOMAINS, { pct: { 1: 58, 2: 71, 3: 80 }, gate }).s;
  ok(s.includes("bstrip-s is-bad") && s.includes(">D1 58%</span>"), "below domainMin is bad");
  ok(s.includes("bstrip-s is-warn") && s.includes(">D2 71%</span>"), "between is warn");
  ok(s.includes("bstrip-s is-good") && s.includes(">D3 80%</span>"), "at strong is good");
  ok(s.includes(">D4</span>") && s.includes("no answers yet"), "a domain without data has no percent");
  SAA.state = { cfg: { gate } };
  ok(U.bstrip(DOMAINS, { pct: { d1: 90 } }).s.includes("is-good"), "gate from SAA.state.cfg, keys d1..d4 accepted");
  SAA.state = undefined;
});

test("Router.parse", () => {
  eq(R.parse(""), { view: "home", args: [] });
  eq(R.parse("#"), { view: "home", args: [] });
  eq(R.parse("#home"), { view: "home", args: [] });
  eq(R.parse("#ch.vpc"), { view: "ch", args: ["vpc"] });
  eq(R.parse("ch.vpc.deep.nat-gateways"), { view: "ch", args: ["vpc", "deep", "nat-gateways"] });
  eq(R.parse("#attempt.a-mgq3k2-x7"), { view: "attempt", args: ["a-mgq3k2-x7"] });
  eq(R.parse("#t.shot.quiz-open"), { view: "t", args: ["shot", "quiz-open"] });
  eq(R.parse("#ch..vpc."), { view: "ch", args: ["vpc"] }, "empty tokens are dropped");
  eq(R.parse("#ch.vpc?x=1&y"), { view: "ch", args: ["vpcx1y"] }, "characters outside the route alphabet are dropped");
  eq(R.parse(null), { view: "home", args: [] });
});

test("Router.href and the round trip", () => {
  eq(R.href("ch", "vpc", "deep", "nat-gateways"), "#ch.vpc.deep.nat-gateways");
  eq(R.href("home"), "#home");
  eq(R.href("ch", "vpc", "", null, undefined), "#ch.vpc", "empty arguments are dropped");
  const routes = [["home"], ["ch", "iam"], ["ch", "vpc", "do", "vpc-t02"], ["quiz", "vpc", "all"], ["drill", "d1"],
                  ["mock", "1"], ["glossary", "nat-gateway"], ["fact", "vpc-natgw-bandwidth"], ["speak", "vpc", "vpc-s01"]];
  for (const r of routes) {
    const parsed = R.parse(R.href(...r));
    eq([parsed.view, ...parsed.args], r, "round trip of " + r.join("."));
    eq(R.href(parsed.view, ...parsed.args), R.href(...r));
  }
});

test("router.js touches no window or document at load, and current() is plain", () => {
  eq(R.current(), { view: "", args: [], hash: "" });
  ok(typeof R.register === "function" && typeof R.go === "function" && typeof R.start === "function");
});

// content.js: the two functions that count sections (pure once the manifest is in).
const C = load(["util.js", "content.js"], {
  document: { getElementById: (id) => (id === "saa-inline" ? { textContent: JSON.stringify({ "manifest.json": {
    v: 1, build: "t", chapters: [{ slug: "vpc", id: "10", status: "ready", hash: "h1",
      files: [{ key: "fast", title: "Fast" }, { key: "deep", title: "In depth" }],
      sections: [
        ["predict", "fast", 2, "fast", 1, "Predict", null, "predict"],
        ["signals", "fast", 2, "fast", 2, "Signals and traps", null, "signals"],
        ["traps", "fast", 0, "fast", 0, "Traps", "signals", null],
        ["how", "deep", 2, "full", 6, "How it works", null, "how"],
        ["nat", "deep", 3, "pass", 3, "NAT gateways", "how", null],
        ["peering", "deep", 3, "full", 3, "Peering", "how", null],
        ["numbers", "deep", 2, "full", 1, "Numbers", null, "numbers"]
      ] }, { slug: "s3", id: "11", status: "planned", files: [], sections: [] }] } }) } : null) }
}).Content;

await C.manifest();

test("Content.section returns a row object, or null", () => {
  eq(C.section("vpc", "nat"), { sid: "nat", part: "deep", kind: 3, route: "pass", min: 3, title: "NAT gateways", parent: "how", role: null });
  eq(C.section("vpc", "missing"), null);
  eq(C.section("nope", "nat"), null);
  eq(C.meta("s3").status, "planned");
});

test("Content.routeSections: route order, kind 0 left out, a parent with tracked children left out", () => {
  eq(C.routeSections("vpc", "fast").map((r) => r.sid), ["predict", "signals"]);
  eq(C.routeSections("vpc", "pass").map((r) => r.sid), ["predict", "signals", "nat"]);
  eq(C.routeSections("vpc", "full").map((r) => r.sid), ["predict", "signals", "nat", "peering", "numbers"]);
});

test("Content.progress counts positive read stamps only", () => {
  const progress = { chapters: { vpc: { read: { predict: 1790000000, nat: 1790000001, peering: -1790000002, traps: 5, how: 5 } } } };
  eq(C.progress("vpc", "fast", progress), { read: 1, total: 2 });
  eq(C.progress("vpc", "pass", progress), { read: 2, total: 3 });
  eq(C.progress("vpc", "full", progress), { read: 2, total: 5 });
  eq(C.progress("vpc", "pass", null), { read: 0, total: 3 });
  eq(C.progress("s3", "pass", progress), { read: 0, total: 0 });
});

// awaited outside test(), because test() is synchronous
const planned = await C.chapter("s3");
test("Content.chapter of a planned chapter is null", () => { eq(planned, null); });
