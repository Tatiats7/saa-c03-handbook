/* plan.js: view "plan", mount "plan", and the helpers that Today and the dashboard share (SAA.Plan).
   ARCHITECTURE.md section 8.1. */
(function (SAA) {
  "use strict";

  var U = SAA.U;
  var Plan = SAA.Plan = {};

  /* ---------- dates ---------- */

  Plan.parseDate = function (str) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(String(str || ""));
    if (!m) return null;
    var d = new Date(Number(m[1]), Number(m[2]) - 1, Number(m[3]), 12);
    return isNaN(d.getTime()) ? null : d;
  };

  Plan.dateStr = function (ms) {
    var d = new Date(ms), mo = d.getMonth() + 1, day = d.getDate();
    return d.getFullYear() + "-" + (mo < 10 ? "0" : "") + mo + "-" + (day < 10 ? "0" : "") + day;
  };

  Plan.fmtDate = function (date, long) {
    try {
      return date.toLocaleDateString("en-US", long ? {weekday: "long", month: "long", day: "numeric"}
        : {weekday: "short", month: "short", day: "numeric"});
    } catch (e) { return Plan.dateStr(date.getTime()); }
  };

  /* "Plan A: title", without saying "Plan A" twice when the title already starts with it. */
  Plan.label = function (p) {
    var name = "Plan " + String(p.id).toUpperCase(), title = String(p.title || "");
    return title.toLowerCase().indexOf(name.toLowerCase()) === 0 ? title : name + ": " + title;
  };

  /* ---------- the model of one plan ---------- */

  /* Returns null without plan data. today: index of the calendar day (null after the last day);
     current: index of the first day, up to today, with an open task (section 8.1). */
  Plan.model = function (data, settings, progress, planId) {
    if (!data || !Array.isArray(data.plans) || !data.plans.length) return null;
    var id = planId || (settings && settings.plan) || "a";
    var plan = data.plans.filter(function (p) { return p.id === id; })[0] || data.plans[0];
    var stamps = (progress && progress.plan && progress.plan[plan.id]) || {};
    var start = Plan.parseDate(settings && settings.planStart);
    var todayN = start ? U.day() - U.day(start.getTime()) + 1 : 1;
    var days = (plan.days || []).map(function (d, i) {
      var st = stamps[d.id] || {}, open = 0;
      var tasks = (d.tasks || []).map(function (t) {
        var done = st[t.id] > 0;
        if (!done) open++;
        return {id: t.id, text: t.text, chapter: t.chapter || null, route: t.route || null, minutes: t.minutes || 0, done: done};
      });
      return {id: d.id, n: i + 1, minutes: d.minutes || 0, tasks: tasks, open: open,
        date: start ? new Date(start.getFullYear(), start.getMonth(), start.getDate() + i, 12) : null,
        gates: (data.gates || []).filter(function (g) { return g.day === d.id; })};
    });
    var len = days.length, current = null, i;
    for (i = 0; i < Math.min(todayN, len); i++) if (days[i].open) { current = i; break; }
    var finished = todayN > len && current === null;
    if (current === null && !finished) current = Math.max(1, Math.min(todayN, len)) - 1;
    return {plan: plan, days: days, started: !!start, start: start, todayN: todayN,
      today: todayN > len ? null : Math.max(todayN, 1) - 1, current: current, finished: finished,
      startsIn: todayN < 1 ? 1 - todayN : 0};
  };

  /* ---------- drawing ---------- */

  /* U.set, then the ticks, then the focus goes back to the control that had it (every control has an id). */
  Plan.paint = function (root, safe) {
    var act = document.activeElement, id = act && act.id && root.contains(act) ? act.id : "";
    U.set(root, safe);
    var on = root.querySelectorAll("input[data-on=\"1\"]");
    for (var i = 0; i < on.length; i++) on[i].checked = true;
    if (id) {
      var again = document.getElementById(id);
      if (again) { try { again.focus({preventScroll: true}); } catch (e) { /* older engines */ } }
    }
  };

  Plan.taskItem = function (planId, day, t) {
    var id = "pl-" + planId + "-" + day.id + "-" + t.id;
    var meta = t.chapter && SAA.Content ? SAA.Content.meta(t.chapter) : null;
    var link = "";
    if (t.chapter) {
      var word = meta ? "Open " + meta.title : "Open the chapter";
      if (meta && meta.status === "planned") word += " (not written yet)";
      link = U.h`<a class="pl-open" href="${"#ch." + t.chapter}" data-act="pl-open" data-slug="${t.chapter}" data-route="${t.route || ""}">${word}</a>`;
    }
    var min = t.minutes ? U.h`<span class="pl-min mono">${U.fmtMin(t.minutes)}</span>` : "";
    return U.h`<li class="${"pl-task" + (t.done ? " is-done" : "")}"><input type="checkbox" id="${id}" data-act="pl-tick" data-plan="${planId}" data-day="${day.id}" data-task="${t.id}" data-on="${t.done ? "1" : "0"}"><label for="${id}">${t.text}</label>${link}${min}</li>`;
  };

  Plan.taskList = function (planId, day, onlyOpen) {
    var tasks = onlyOpen ? day.tasks.filter(function (t) { return !t.done; }) : day.tasks;
    return U.h`<ul class="pl-tasks">${tasks.map(function (t) { return Plan.taskItem(planId, day, t); })}</ul>`;
  };

  Plan.gates = function (day) {
    return day.gates.map(function (g) {
      return U.h`<p class="pl-gate"><span class="eyebrow">Readiness gate</span> ${g.text}</p>`;
    });
  };

  Plan.startBlock = function (m) {
    var value = m.start ? Plan.dateStr(m.start.getTime()) : "";
    var line = m.started
      ? (m.startsIn ? "Day 1 is " + Plan.fmtDate(m.start, true) + "." : "Day 1 was " + Plan.fmtDate(m.start, true) + ".")
      : "The plan has no start date yet. Days show without dates until you set one.";
    return U.h`<div class="pl-start"><p>${line}</p><div class="pl-start-c">${m.started ? "" : U.h`<button type="button" class="btn primary" data-act="pl-start">Start Day 1 today</button>`}<label for="pl-start-date">${m.started ? "Change the date of Day 1" : "or pick the date of Day 1"}</label><input type="date" id="pl-start-date" value="${value}"></div></div>`;
  };

  /* The handlers of every plan control under root. Returns a function that removes them. */
  Plan.bind = function (root) {
    var St = function () { return SAA.Store; };
    var offs = [
      U.on(root, "change", "input[data-act=\"pl-tick\"]", function (ev, el) {
        St().stamp("progress", ["plan", el.getAttribute("data-plan"), el.getAttribute("data-day"), el.getAttribute("data-task")], el.checked);
      }),
      U.on(root, "click", "a[data-act=\"pl-open\"]", function (ev, el) {
        var slug = el.getAttribute("data-slug"), route = el.getAttribute("data-route");
        if (!slug || !route) return;
        var by = {};
        by[slug] = route;
        St().patch("settings", {routeBy: by});
      }),
      U.on(root, "click", "button[data-act=\"pl-start\"]", function () {
        St().patch("settings", {planStart: Plan.dateStr(U.nowMs())});
      }),
      U.on(root, "change", "#pl-start-date", function (ev, el) {
        St().patch("settings", {planStart: Plan.parseDate(el.value) ? el.value : null});
      }),
      U.on(root, "change", "input[name=\"pl-plan\"]", function (ev, el) {
        if (el.checked) St().patch("settings", {plan: el.value});
      })
    ];
    return function () { offs.forEach(function (off) { off(); }); };
  };

  function dayBlock(m, day, i, opts) {
    var cls = "pl-day", marks = [];
    if (m.started && m.today === i) { cls += " is-today"; marks.push(U.h`<span class="pill note">Today</span>`); }
    if (!day.open) marks.push(U.h`<span class="pill good">Done</span>`);
    else if (m.current === i && m.today !== i) marks.push(U.h`<span class="pill warn">Open tasks</span>`);
    var meta = [];
    if (day.date) meta.push(Plan.fmtDate(day.date));
    if (day.minutes) meta.push(U.fmtMin(day.minutes));
    return U.h`<li class="${cls}" id="${opts.prefix + day.id}"><div class="pl-day-h"><h2>Day ${day.n}</h2><span class="pl-day-m mono">${meta.join(" · ")}</span>${marks}</div>${Plan.taskList(m.plan.id, day)}${Plan.gates(day)}</li>`;
  }

  Plan.dayList = function (m, prefix) {
    var items = m.days.map(function (d, i) { return dayBlock(m, d, i, {prefix: prefix}); });
    return U.h`<ol class="pl-days">${items}</ol>${m.finished || m.today === null ? U.h`<p class="pl-done">Plan finished.</p>` : ""}`;
  };

  /* ---------- view ---------- */

  var V = {root: null, offs: [], data: undefined};

  function draw() {
    if (!V.root) return;
    var St = SAA.Store, settings = St.get("settings"), progress = St.get("progress");
    var head = U.h`<header class="pl-head"><p class="eyebrow">Study calendar</p><h1 id="pl-h1" tabindex="-1">Plan</h1></header>`;
    if (V.data === undefined) { Plan.paint(V.root, U.h`${head}<p class="pl-wait">Loading the plan…</p>`); return; }
    var m = Plan.model(V.data, settings, progress);
    if (!m) { Plan.paint(V.root, U.h`${head}<p class="notice">The study plan is not written yet.</p>`); return; }
    var pick = V.data.plans.map(function (p) {
      var id = "pl-plan-" + p.id;
      return U.h`<div class="pl-pick-o"><input type="radio" name="pl-plan" id="${id}" value="${p.id}" data-on="${p.id === m.plan.id ? "1" : "0"}"><label for="${id}"><span class="pl-pick-t">${Plan.label(p)}</span>${p.note ? U.h`<span class="pl-pick-n">${p.note}</span>` : ""}</label></div>`;
    });
    var done = 0, total = 0;
    m.days.forEach(function (d) { total += d.tasks.length; done += d.tasks.length - d.open; });
    Plan.paint(V.root, U.h`${head}
      <fieldset class="pl-pick"><legend>Which plan</legend>${pick}</fieldset>
      ${Plan.startBlock(m)}
      <p class="pl-sum">${done} of ${total} tasks done.${m.started && m.today !== null ? U.h` <button type="button" class="btn quiet" id="pl-jump" data-act="pl-jump">Go to today</button>` : ""}</p>
      ${Plan.dayList(m, "pl-day-")}`);
  }

  function jump() {
    var el = V.root && V.root.querySelector(".pl-day.is-today");
    if (el && el.scrollIntoView) el.scrollIntoView({block: "start"});
  }

  function onChange(d) { if (!d || d.doc !== "ui") draw(); }

  var view = {
    mount: function (el) {
      V.root = document.createElement("div");
      V.root.className = "pl";
      el.appendChild(V.root);
      V.data = undefined;
      V.offs = [Plan.bind(V.root), U.on(V.root, "click", "button[data-act=\"pl-jump\"]", function () { jump(); })];
      SAA.bus.on("store:change", onChange);
      SAA.bus.on("manifest", onChange);
      draw();
      return SAA.Content.plan().then(function (data) { V.data = data || null; draw(); });
    },
    unmount: function () {
      V.offs.forEach(function (off) { off(); });
      V.offs = [];
      SAA.bus.off("store:change", onChange);
      SAA.bus.off("manifest", onChange);
      V.root = null;
    },
    title: function () { return "Plan"; }
  };

  if (SAA.Router && SAA.Router.register) SAA.Router.register("plan", view);

  /* ---------- mount "plan" (calendar.md): the day list of one plan, with live ticks ---------- */

  function planMount(el, id) {
    var data, alive = true, off = Plan.bind(el);
    function paint() {
      if (!alive || data === undefined) return;
      var m = Plan.model(data, SAA.Store.get("settings"), SAA.Store.get("progress"), id || undefined);
      if (!m) { el.hidden = true; return; }
      el.hidden = false;
      Plan.paint(el, U.h`<div class="pl pl-in">${Plan.dayList(m, "plm-" + m.plan.id + "-")}</div>`);
    }
    function on(d) { if (!d || d.doc !== "ui") paint(); }
    SAA.bus.on("store:change", on);
    SAA.Content.plan().then(function (d) { data = d || null; paint(); }, function () { el.hidden = true; });
    return function () { alive = false; off(); SAA.bus.off("store:change", on); };
  }

  if (SAA.Reader && SAA.Reader.registerMount) SAA.Reader.registerMount("plan", planMount);

  /* ---------- shot state ---------- */

  if (SAA.Test && SAA.Test.register) {
    SAA.Test.register("plan", function (el) {
      var St = SAA.Store;
      St.reset();
      SAA.Test.clock = function () { return new Date(2026, 9, 7, 10, 0, 0).getTime(); };
      return SAA.Content.plan().then(function (data) {
        var ticks = {};
        var days = (data && data.plans && data.plans[0] && data.plans[0].days) || [];
        days.slice(0, 3).forEach(function (d, i) {
          ticks[d.id] = {};
          d.tasks.forEach(function (t, j) { if (i < 2 || j === 0) ticks[d.id][t.id] = 1790000000; });
        });
        St.load({settings: {plan: "a", planStart: "2026-10-05"}, progress: {plan: {a: ticks}}});
        return view.mount(el, [], {hot: null});
      });
    });
  }
})(globalThis.SAA = globalThis.SAA || {});
