/* today.js: view "home" (Today). ARCHITECTURE.md section 8.2. Draws at once from local state. */
(function (SAA) {
  "use strict";

  var U = SAA.U;
  var VISIBLE = 5;
  var V = {root: null, offs: [], plan: undefined, qindex: null, more: false, fresh: null};

  function manifest() { return (SAA.state && SAA.state.manifest) || null; }
  function cfg() { return (SAA.state && SAA.state.cfg) || {}; }

  function card(cls, id, title, body) {
    return U.h`<section class="${"td-card" + (cls ? " " + cls : "")}" aria-labelledby="${id}"><h2 id="${id}">${title}</h2>${body}</section>`;
  }

  /* Accuracy per domain from the last answer of every question: {1: 58, ...}; null without answers. */
  function domainPct(qstats, qindex) {
    if (!qindex || !qindex.q) return null;
    var dom = {}, any = false;
    Object.keys(qstats.q || {}).forEach(function (id) {
      var rec = qstats.q[id], row = qindex.q[id];
      if (!row || !rec || !rec.h || (rec.kr !== undefined && row[5] !== undefined && rec.kr !== row[5])) return;
      var d = row[1];
      dom[d] = dom[d] || {c: 0, n: 0};
      dom[d].n++;
      if (rec.h.charAt(rec.h.length - 1) === "1") dom[d].c++;
      any = true;
    });
    if (!any) return null;
    var pct = {};
    Object.keys(dom).forEach(function (d) { pct[d] = Math.round(100 * dom[d].c / dom[d].n); });
    return pct;
  }

  function dayCard(m) {
    var P = SAA.Plan;
    if (!m) return null;
    var len = m.days.length, day = m.today === null ? null : m.days[m.today], parts = [];
    var eyebrow = P.label(m.plan);
    var title = day ? "Day " + day.n + " of " + len : "Plan finished";
    if (day) {
      var sub = [];
      if (day.date && m.started) sub.push(P.fmtDate(day.date, true));
      if (day.minutes) sub.push(U.fmtMin(day.minutes));
      if (sub.length) parts.push(U.h`<p class="td-sub mono">${sub.join(" · ")}</p>`);
      if (m.startsIn) parts.push(U.h`<p class="td-note">Day 1 starts in ${m.startsIn} ${m.startsIn === 1 ? "day" : "days"}. You can begin now.</p>`);
      parts.push(P.taskList(m.plan.id, day));
      parts.push(P.gates(day));
    } else {
      parts.push(U.h`<p class="td-note">You are past the last day of the plan.</p>`);
    }
    var before = m.days.slice(0, m.today === null ? len : m.today).filter(function (d) { return d.open; });
    before.slice(-3).forEach(function (d) {
      parts.push(U.h`<h3 class="td-left">Left from Day ${d.n}</h3>${P.taskList(m.plan.id, d, true)}`);
    });
    if (before.length > 3) parts.push(U.h`<p class="td-note">${before.length - 3} earlier ${before.length - 3 === 1 ? "day has" : "days have"} open tasks too.</p>`);
    if (!m.started) {
      parts.push(U.h`<p class="td-start"><button type="button" class="btn primary" id="td-start" data-act="pl-start">Start Day 1 today</button> <span class="td-note">This sets the dates of the plan. You can change the date in the plan.</span></p>`);
    }
    parts.push(U.h`<p class="td-more-l"><a href="#plan">Open the full plan</a></p>`);
    return U.h`<section class="td-card is-main" aria-labelledby="td-day-h"><p class="eyebrow">${eyebrow}</p><h2 id="td-day-h">${title}</h2>${parts}</section>`;
  }

  function minimums(progress) {
    var list = cfg().minimums || [];
    if (!list.length) return null;
    var key = String(U.day()), st = (progress.daily && progress.daily[key]) || {};
    var items = list.map(function (m) {
      var done = st[m.id] > 0;
      if (m.id === "speak") {
        return U.h`<li class="td-min-i"><span class="${"pill " + (done ? "good" : "")}">${done ? "Done" : "Not yet"}</span> <a href="#speak">${m.label}</a></li>`;
      }
      var id = "td-min-" + m.id;
      return U.h`<li class="td-min-i"><input type="checkbox" id="${id}" data-act="td-min" data-id="${m.id}" data-on="${done ? "1" : "0"}"><label for="${id}">${m.label}</label></li>`;
    });
    return card("td-min", "td-min-h", "Daily minimums", U.h`<ul class="td-min-l">${items}</ul>`);
  }

  function continueCard(progress) {
    var last = progress.last;
    if (!last || !last.route) return null;
    var tok = String(last.route).split("."), label = "Your last page";
    if (tok[0] === "ch" && tok[1] && SAA.Content) {
      var meta = SAA.Content.meta(tok[1]);
      var sec = tok[3] ? (SAA.Content.section(tok[1], tok[2] + "." + tok[3]) || SAA.Content.section(tok[1], tok[3])) : null;
      if (meta) label = meta.title + (sec ? ": " + sec.title : "");
    }
    return card("", "td-cont-h", "Continue reading", U.h`<p><a href="${"#" + last.route}">${label}</a></p>`);
  }

  function mixCard() {
    if (!SAA.Quiz) return null;
    var today = U.day();
    var done = SAA.Store.attempts().filter(function (a) { return a.kind === "mix" && U.day((a.submittedAt || 0) * 1000) === today; })[0];
    var body = done
      ? U.h`<p><span class="pill good">Done today</span> <a href="${"#attempt." + done.id}">${done.pct}% on today's mix</a></p>`
      : U.h`<p><a href="#mix">10 questions, about 15 minutes</a></p>`;
    return card("", "td-mix-h", "Daily mix", body);
  }

  function mistakesCard(qstats) {
    if (!SAA.Scoring || !V.qindex) return null;
    var n = SAA.Scoring.mistakes(qstats, V.qindex).length;
    if (!n) return null;
    return card("", "td-mk-h", "Mistakes", U.h`<p>${n} ${n === 1 ? "question" : "questions"} in your mistakes log. <a href="#retry">Retry them</a> or <a href="#mistakes">open the log</a>.</p>`);
  }

  function sayCard(m, speak) {
    var s = V.qindex && V.qindex.s;
    if (!s || !m) return null;
    var day = m.days[m.today === null ? m.days.length - 1 : m.today], slugs = {};
    day.tasks.forEach(function (t) { if (t.chapter) slugs[t.chapter] = 1; });
    var ids = Object.keys(s).filter(function (id) { return slugs[s[id][0]] && !(speak.items && speak.items[id]); });
    ids.sort(function (a, b) { return (s[b][2] || 0) - (s[a][2] || 0) || (a < b ? -1 : 1); });
    if (!ids.length) return null;
    var row = s[ids[0]], text = String(row[4] || "");
    if (text.length > 140) text = text.slice(0, 137) + "…";
    return card("", "td-say-h", "Say it", U.h`<p class="td-quote">${text}</p><p><a href="${"#speak." + row[0] + "." + ids[0]}">Answer this out loud</a></p>`);
  }

  function labsCard(progress) {
    var labs = progress.labs || {}, rows = [];
    Object.keys(labs).sort().forEach(function (id) {
      var lab = labs[id] || {}, steps = lab.steps || {};
      var began = Object.keys(steps).some(function (k) { return steps[k] > 0; });
      if (!began || lab.cleaned > 0) return;
      var slug = id.replace(/-t\d+$/, ""), meta = SAA.Content ? SAA.Content.meta(slug) : null;
      rows.push(meta
        ? U.h`<li><a href="${"#ch." + slug + ".do." + id}">${meta.title}: cleanup steps of task <span class="mono">${id}</span></a></li>`
        : U.h`<li>Task <span class="mono">${id}</span></li>`);
    });
    if (!rows.length) return null;
    return card("", "td-lab-h", "Not cleaned up", U.h`<p class="td-note">You started these tasks and did not tick "Cleaned up". Resources that stay can cost money.</p><ul>${rows}</ul>`);
  }

  /* Computed once per visit of Today, so the list stays while she reads it. */
  function freshList() {
    var m = manifest();
    if (!m) return null;
    if (V.fresh) return V.fresh;
    var seen = SAA.Store.get("ui").seen || {}, first = !Object.keys(seen).length, upd = {}, list = [], changed = false;
    (m.chapters || []).forEach(function (ch) {
      if (ch.status === "planned") return;
      var mark = ch.status + ":" + (ch.rev || 0);
      if (seen[ch.slug] === mark) return;
      upd[ch.slug] = mark;
      changed = true;
      if (!first) list.push({slug: ch.slug, title: ch.title, isNew: !seen[ch.slug], status: ch.status});
    });
    V.fresh = list;
    if (changed) SAA.Store.patch("ui", {seen: upd});
    return list;
  }

  function freshCard() {
    var list = freshList();
    if (!list || !list.length) return null;
    var rows = list.slice(0, 8).map(function (c) {
      return U.h`<li><a href="${"#ch." + c.slug}">${c.title}</a> <span class="pill">${c.isNew ? "New" : "Updated"}</span>${c.status === "draft" ? U.h` <span class="pill warn">Draft</span>` : ""}</li>`;
    });
    return card("", "td-new-h", "New since your last visit", U.h`<ul>${rows}</ul>${list.length > 8 ? U.h`<p class="td-note">And ${list.length - 8} more in the contents.</p>` : ""}`);
  }

  function drillsCard() {
    if (!SAA.Quiz) return null;
    var list = SAA.Store.drills();
    if (!list.length) return null;
    var rows = list.slice(0, 5).map(function (d, i) {
      return U.h`<li><button type="button" class="btn" id="${"td-drill-" + i}" data-act="td-drill" data-id="${d.id}">${d.title}</button>${d.why ? U.h` <span class="td-note">${String(d.why).slice(0, 160)}</span>` : ""}</li>`;
    });
    return card("", "td-dr-h", "Drills from Claude", U.h`<ul class="td-drills">${rows}</ul>`);
  }

  function draw() {
    if (!V.root) return;
    var St = SAA.Store, P = SAA.Plan;
    var settings = St.get("settings"), progress = St.get("progress"), qstats = St.get("qstats"), speak = St.get("speak");
    var m = P && V.plan ? P.model(V.plan, settings, progress) : null;
    var man = manifest(), pct = domainPct(qstats, V.qindex), strip = "";
    if (man && man.domains && pct) strip = U.h`<div class="td-strip"><p class="td-strip-l">Your accuracy by exam domain</p>${U.bstrip(man.domains, {pct: pct})}</div>`;
    var date = P ? P.fmtDate(new Date(U.nowMs()), true) : "";
    var cards = [dayCard(m), minimums(progress), continueCard(progress), mixCard(), mistakesCard(qstats),
      sayCard(m, speak), labsCard(progress), freshCard(), drillsCard()].filter(Boolean);
    var rest = cards.slice(VISIBLE);
    P.paint(V.root, U.h`<header class="td-head"><p class="eyebrow">${date}</p><h1 id="td-h1" tabindex="-1">Today</h1>${strip}</header>
      <div class="td-cards">${cards.slice(0, VISIBLE)}</div>
      ${rest.length ? U.h`<details class="td-more"><summary>More</summary><div class="td-cards">${rest}</div></details>` : ""}`);
    var det = V.root.querySelector("details.td-more");
    if (det && V.more) det.open = true;
  }

  function onChange(d) { if (!d || d.doc !== "ui") draw(); }
  function onAny() { draw(); }

  function load() {
    var C = SAA.Content;
    if (!C) return;
    C.manifest().then(draw, function () { /* Today works without the manifest */ });
    C.plan().then(function (p) { V.plan = p || null; draw(); }, function () { V.plan = null; });
    C.qindex().then(function (q) { V.qindex = q || null; draw(); }, function () { V.qindex = null; });
  }

  var view = {
    mount: function (el) {
      V.root = document.createElement("div");
      V.root.className = "td";
      el.appendChild(V.root);
      V.fresh = null;
      V.offs = [
        SAA.Plan.bind(V.root),
        U.on(V.root, "change", "input[data-act=\"td-min\"]", function (ev, box) {
          SAA.Store.stamp("progress", ["daily", String(U.day()), box.getAttribute("data-id")], box.checked);
        }),
        U.on(V.root, "toggle", "details.td-more", function (ev, det) { V.more = det.open; }),
        U.on(V.root, "click", "button[data-act=\"td-drill\"]", function (ev, btn) {
          var id = btn.getAttribute("data-id");
          var d = SAA.Store.drills().filter(function (x) { return x.id === id; })[0];
          if (d && SAA.Quiz && SAA.Quiz.start) SAA.Quiz.start({kind: "drill", ref: d.id, ids: d.items, title: d.title});
        })
      ];
      SAA.bus.on("store:change", onChange);
      SAA.bus.on("manifest", onAny);
      SAA.bus.on("caps", onAny);
      SAA.bus.on("speak:done", onAny);
      draw();
      load();
    },
    unmount: function () {
      V.offs.forEach(function (off) { off(); });
      V.offs = [];
      SAA.bus.off("store:change", onChange);
      SAA.bus.off("manifest", onAny);
      SAA.bus.off("caps", onAny);
      SAA.bus.off("speak:done", onAny);
      V.root = null;
    },
    title: function () { return "Today"; }
  };

  if (SAA.Router && SAA.Router.register) SAA.Router.register("home", view);

  /* Shot state: Day 3 with ticks, a mix done, two mistakes. */
  if (SAA.Test && SAA.Test.register) {
    SAA.Test.register("home", function (el) {
      var St = SAA.Store, C = SAA.Content;
      St.reset();
      SAA.Test.clock = function () { return new Date(2026, 9, 7, 10, 0, 0).getTime(); };
      var now = U.now(), day = U.day();
      return Promise.all([C.plan(), C.qindex(), C.manifest()]).then(function (r) {
        var plan = r[0], qi = (r[1] && r[1].q) || {}, ticks = {}, q = {}, daily = {};
        var days = (plan && plan.plans && plan.plans[0] && plan.plans[0].days) || [];
        days.slice(0, 3).forEach(function (d, i) {
          ticks[d.id] = {};
          d.tasks.forEach(function (t, j) { if (i === 0 || (i === 1 && j > 0) || (i === 2 && j === 0)) ticks[d.id][t.id] = now - 3600; });
        });
        Object.keys(qi).filter(function (id) { return qi[id][3] === 0; }).sort().slice(0, 12).forEach(function (id, i) {
          var wrong = i < 2;
          q[id] = {h: wrong ? "0" : "1", u: "0", t: now - 7200 + i, d: wrong ? 0 : day - 1, box: wrong ? 0 : 1, pick: ["a"], kr: qi[id][5]};
          if (wrong) q[id].c = i ? "W" : "C";
        });
        daily[String(day)] = {pages: now - 1800};
        var first = (r[2].chapters || []).filter(function (c) { return c.status !== "planned" && c.sections && c.sections.length; })[0];
        var last = first ? {route: "ch." + first.slug + "." + first.sections[0][1] + "." + first.sections[0][0], t: now - 900} : null;
        St.load({
          settings: {plan: "a", planStart: "2026-10-05"},
          progress: {plan: {a: ticks}, daily: daily, last: last},
          qstats: {sf: 12, q: q},
          attempts: [{v: 1, id: "a-shot-mix", kind: "mix", ref: "mix", first: 1, over: 0, startedAt: now - 5400, submittedAt: now - 4800,
            activeSec: 560, limitSec: 0, build: "", total: 10, correct: 8, pct: 80, sureCorrect: 7, domains: {}, topics: {}}]
        });
        view.mount(el, [], {hot: null});
      });
    });
  }
})(globalThis.SAA = globalThis.SAA || {});
