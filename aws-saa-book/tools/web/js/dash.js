/* dash.js: view "progress" (the dashboard). ARCHITECTURE.md section 8.3. */
(function (SAA) {
  "use strict";

  var U = SAA.U;
  var V = {root: null, offs: [], plan: null, qindex: null, note: "", summary: ""};
  var KIND = {mock: "Mock exam", chapter: "Chapter quiz", drill: "Drill", retry: "Retry", mix: "Daily mix"};
  var CAUSE = {K: "Did not know", C: "Confused two things", W: "Missed a word", T: "Ran out of time", D: "Old limit in the question"};
  var GATE = {"go": "Ready by your rule", "go-soft": "Close: ready by your softer rule", "not-yet": "Not ready yet by your rule"};

  function manifest() { return (SAA.state && SAA.state.manifest) || null; }
  function cfg() { return (SAA.state && SAA.state.cfg) || {}; }
  function pct(c, n) { return n ? Math.round(100 * c / n) : 0; }

  function bar(value, label) {
    var v = Math.max(0, Math.min(100, Math.round(value || 0)));
    return U.h`<div class="pbar" role="img" aria-label="${label || v + " percent"}"><div class="pbar-f" style="${"width:" + v + "%"}"></div></div>`;
  }

  function block(id, title, body) {
    return U.h`<section class="ds-sec" aria-labelledby="${id}"><h2 id="${id}">${title}</h2>${body}</section>`;
  }

  function gateBlock(attempts) {
    var g = cfg().gate, body = [];
    if (SAA.Scoring && g) {
      var r = SAA.Scoring.gate(attempts, g);
      var cls = r.state === "go" ? "good" : r.state === "go-soft" ? "warn" : "";
      body.push(U.h`<p class="ds-gate-n">${r.text}</p><p><span class="${"pill " + cls}">${GATE[r.state] || r.state}</span></p>`);
      body.push(U.h`<p class="ds-note">Your rule: ${g.needed} first attempts of a mock, finished in time, at ${g.strong}% or more. The softer rule: both at ${g.soft}% or more and no domain under ${g.domainMin}%. These numbers are your study rule, not an AWS rule.</p>`);
    }
    var gates = (V.plan && V.plan.gates) || [];
    if (gates.length) {
      body.push(U.h`<ul class="ds-gates">${gates.map(function (x) {
        return U.h`<li class="pl-gate"><span class="eyebrow">Day ${Number(String(x.day).slice(1))}</span> ${x.text}</li>`;
      })}</ul>`);
    }
    if (!body.length) return "";
    return U.h`<section class="ds-gate" aria-labelledby="ds-gate-h"><h2 id="ds-gate-h">Readiness gate</h2>${body}</section>`;
  }

  function domainBlock(qstats) {
    var man = manifest(), qi = V.qindex && V.qindex.q;
    if (!man || !man.domains) return "";
    var dom = {};
    if (qi) {
      Object.keys(qstats.q || {}).forEach(function (id) {
        var rec = qstats.q[id], row = qi[id];
        if (!row || !rec || !rec.h || (rec.kr !== undefined && row[5] !== undefined && rec.kr !== row[5])) return;
        dom[row[1]] = dom[row[1]] || {c: 0, n: 0};
        dom[row[1]].n++;
        if (rec.h.charAt(rec.h.length - 1) === "1") dom[row[1]].c++;
      });
    }
    var rows = man.domains.map(function (d) {
      var x = dom[d.id] || {c: 0, n: 0}, p = pct(x.c, x.n);
      return U.h`<li class="ds-row"><div class="ds-row-h"><span class="ds-row-t"><span class="mono">D${d.id}</span> ${d.title}</span><span class="ds-row-v mono">${x.n ? p + "%" : "no answers yet"}</span></div>${bar(p, "Domain " + d.id + ": " + (x.n ? p + " percent correct" : "no answers yet"))}<p class="ds-note">${x.n} answered · ${d.weight}% of the exam</p></li>`;
    });
    return block("ds-dom-h", "Domains", U.h`<ul class="ds-rows">${rows}</ul>`);
  }

  function coverageBlock(settings, progress, qstats) {
    var man = manifest(), C = SAA.Content;
    if (!man || !C) return "";
    var rows = [];
    (man.parts || []).forEach(function (part) {
      var chapters = (man.chapters || []).filter(function (c) { return c.part === part.id && c.status !== "planned"; });
      var planned = (man.chapters || []).filter(function (c) { return c.part === part.id && c.status === "planned"; }).length;
      if (!chapters.length && !planned) return;
      var done = 0, read = 0, total = 0;
      chapters.forEach(function (c) {
        var route = (settings.routeBy && settings.routeBy[c.slug]) || settings.route || "pass";
        var p = C.progress(c.slug, route, progress);
        read += p.read;
        total += p.total;
        if (p.total && p.read >= p.total) done++;
      });
      var words = chapters.length ? done + " of " + chapters.length + " chapters read" : "not written yet";
      rows.push(U.h`<li class="ds-row"><div class="ds-row-h"><span class="ds-row-t">${part.title}</span><span class="ds-row-v mono">${words}</span></div>${chapters.length ? bar(pct(read, total), part.title + ": " + read + " of " + total + " sections read") : ""}<p class="ds-note">${chapters.length ? read + " of " + total + " sections on your route" : ""}${planned ? (chapters.length ? " · " : "") + planned + " not written yet" : ""}</p></li>`);
    });
    var qi = V.qindex && V.qindex.q, seen = 0;
    /* the bank is every question outside the mocks (pool 2), so a mock does not count as "seen" */
    var bank = 0;
    if (qi) {
      Object.keys(qi).forEach(function (id) {
        if (qi[id][3] === 2) return;
        bank++;
        if (qstats.q && qstats.q[id] && qstats.q[id].h) seen++;
      });
    } else bank = (man.counts && man.counts.questions) || 0;
    var qline = bank ? U.h`<p class="ds-q">${seen} of ${bank} questions seen.</p>${bar(pct(seen, bank), seen + " of " + bank + " questions seen")}` : "";
    if (!rows.length && !bank) return "";
    return block("ds-cov-h", "Coverage", U.h`<ul class="ds-rows">${rows}</ul>${qline}`);
  }

  function attemptsBlock(attempts) {
    if (!attempts.length) return block("ds-att-h", "Mocks and attempts", U.h`<p class="ds-note">No attempts yet. A chapter quiz, a drill or a mock exam shows here when you finish it.</p>`);
    var P = SAA.Plan, man = manifest();
    var rows = attempts.slice(0, 30).map(function (a) {
      var name = KIND[a.kind] || a.kind, ref = a.ref || "";
      if (a.kind === "chapter" && SAA.Content && SAA.Content.meta(a.ref)) ref = SAA.Content.meta(a.ref).title;
      if (a.kind === "mock" && man) {
        var mk = (man.mocks || []).filter(function (x) { return x.slug === a.ref; })[0];
        if (mk) ref = mk.title;
      }
      if (a.kind === "mix" || a.kind === "retry") ref = "";
      var when = P ? P.fmtDate(new Date((a.submittedAt || 0) * 1000)) : "";
      return U.h`<tr><th scope="row" data-th="Attempt"><a href="${"#attempt." + a.id}">${name}${ref && ref !== name ? ": " + ref : ""}</a>${a.over ? U.h` <span class="pill warn">Over time</span>` : ""}</th><td data-th="Date">${when}</td><td data-th="Score" class="mono">${a.pct}% (${a.correct}/${a.total})</td><td data-th="Time" class="mono">${U.fmtClock(a.activeSec || 0)}</td></tr>`;
    });
    return block("ds-att-h", "Mocks and attempts", U.h`<div class="tw" role="region" tabindex="0" aria-label="Table: attempts"><table class="tb tb-log tb-stack"><thead><tr><th scope="col">Attempt</th><th scope="col">Date</th><th scope="col">Score</th><th scope="col">Time</th></tr></thead><tbody>${rows}</tbody></table></div>${attempts.length > 30 ? U.h`<p class="ds-note">The newest 30 of ${attempts.length} attempts.</p>` : ""}`);
  }

  function speakBlock(speak) {
    var items = speak.items || {}, bands = {}, plain = 0, n = 0;
    Object.keys(items).forEach(function (id) {
      n++;
      if (items[id] && items[id].band) bands[items[id].band] = (bands[items[id].band] || 0) + 1;
      else plain++;
    });
    if (!n) return "";
    var rows = Object.keys(bands).sort().map(function (b) { return U.h`<li>${b}: <span class="mono">${bands[b]}</span></li>`; });
    if (plain) rows.push(U.h`<li>Self-check only: <span class="mono">${plain}</span></li>`);
    return block("ds-sp-h", "Speaking", U.h`<p class="ds-note">${n} ${n === 1 ? "prompt" : "prompts"} practised.</p><ul class="ds-list">${rows}</ul><p><a href="#speak">Open Speak</a></p>`);
  }

  function coachBlock() {
    var c = SAA.Store.coach && SAA.Store.coach(), out = [];
    if (!c) return "";
    if (c.weakTopics && c.weakTopics.length) {
      out.push(block("ds-weak-h", "Weak topics", U.h`<ul class="ds-rows">${c.weakTopics.map(function (t) {
        var links = (t.chapters || []).map(function (slug) {
          var meta = SAA.Content && SAA.Content.meta(slug);
          return meta ? U.h` <a href="${"#ch." + slug}">${meta.title}</a>` : null;
        }).filter(Boolean).slice(0, 3);
        return U.h`<li class="ds-row"><div class="ds-row-h"><span class="ds-row-t">${t.topic}</span><span class="ds-row-v mono">${t.acc}% of ${t.n}</span></div>${bar(t.acc, t.topic + ": " + t.acc + " percent correct")}${links.length ? U.h`<p class="ds-note">Review:${links}</p>` : ""}</li>`;
      })}</ul>`));
    }
    var why = c.whyCounts || {}, total = 0;
    Object.keys(CAUSE).forEach(function (k) { total += why[k] || 0; });
    if (total) {
      out.push(block("ds-why-h", "Why you missed questions", U.h`<ul class="ds-rows">${Object.keys(CAUSE).map(function (k) {
        var n = why[k] || 0;
        return U.h`<li class="ds-row"><div class="ds-row-h"><span class="ds-row-t"><span class="mono">${k}</span> ${CAUSE[k]}</span><span class="ds-row-v mono">${n}</span></div>${bar(pct(n, total), CAUSE[k] + ": " + n + " of " + total)}</li>`;
      })}</ul><p><a href="#mistakes">Open the mistakes log</a></p>`));
    }
    return out;
  }

  function draw() {
    if (!V.root) return;
    var St = SAA.Store, caps = (SAA.state && SAA.state.caps) || {};
    var settings = St.get("settings"), progress = St.get("progress"), qstats = St.get("qstats"), speak = St.get("speak");
    var attempts = St.attempts();
    var buttons = U.h`<div class="ds-acts"><button type="button" class="btn" id="ds-copy" data-act="ds-copy">Copy summary for Claude</button>${caps.downloads && SAA.Files ? U.h`<button type="button" class="btn" id="ds-save" data-act="ds-save">Save my progress</button>` : ""}</div>
      <p class="ds-note" id="ds-note" role="status">${V.note}</p>
      ${V.summary ? U.h`<label for="ds-summary">Select this text and copy it</label><textarea id="ds-summary" class="ds-summary" rows="8" readonly>${V.summary}</textarea>` : ""}`;
    SAA.Plan.paint(V.root, U.h`<header class="ds-head"><p class="eyebrow">Dashboard</p><h1 id="ds-h1" tabindex="-1">Progress</h1></header>
      ${gateBlock(attempts)}${domainBlock(qstats)}${coverageBlock(settings, progress, qstats)}${attemptsBlock(attempts)}${speakBlock(speak)}${coachBlock()}
      <section class="ds-sec" aria-labelledby="ds-share-h"><h2 id="ds-share-h">Share or keep your progress</h2>${buttons}</section>`);
  }

  function onChange(d) { if (!d || d.doc !== "ui") draw(); }
  function onAny() { draw(); }

  function copy() {
    var text = SAA.Store.summaryText();
    U.copy(text).then(function (ok) {
      V.note = ok ? "Summary copied. Paste it into a chat with Claude." : "Copy did not work here. Select the text below and copy it.";
      V.summary = ok ? "" : text;
      draw();
      if (!ok) {
        var ta = document.getElementById("ds-summary");
        if (ta) { ta.focus(); ta.select(); }
      }
    });
  }

  var view = {
    mount: function (el) {
      V.root = document.createElement("div");
      V.root.className = "ds";
      el.appendChild(V.root);
      V.note = "";
      V.summary = "";
      V.offs = [
        U.on(V.root, "click", "button[data-act=\"ds-copy\"]", copy),
        U.on(V.root, "click", "button[data-act=\"ds-save\"]", function () {
          if (!SAA.Files) return;
          SAA.Files.saveProgress().then(function (text) { V.note = text || ""; draw(); });
        })
      ];
      SAA.bus.on("store:change", onChange);
      SAA.bus.on("manifest", onAny);
      SAA.bus.on("caps", onAny);
      draw();
      var C = SAA.Content;
      if (!C) return undefined;
      C.plan().then(function (p) { V.plan = p || null; draw(); }, function () { V.plan = null; });
      C.qindex().then(function (q) { V.qindex = q || null; draw(); }, function () { V.qindex = null; });
      if (SAA.Store.refreshCoach) SAA.Store.refreshCoach().then(draw);
      return C.manifest().then(draw);
    },
    unmount: function () {
      V.offs.forEach(function (off) { off(); });
      V.offs = [];
      SAA.bus.off("store:change", onChange);
      SAA.bus.off("manifest", onAny);
      SAA.bus.off("caps", onAny);
      V.root = null;
    },
    title: function () { return "Progress"; }
  };

  if (SAA.Router && SAA.Router.register) SAA.Router.register("progress", view);

  /* Shot state: the dashboard with a gate (one mock at the strong level, one under it). */
  if (SAA.Test && SAA.Test.register) {
    SAA.Test.register("progress", function (el) {
      var St = SAA.Store, C = SAA.Content;
      St.reset();
      SAA.Test.clock = function () { return new Date(2026, 9, 20, 10, 0, 0).getTime(); };
      var now = U.now(), day = U.day();
      return Promise.all([C.qindex(), C.manifest()]).then(function (r) {
        var qi = (r[0] && r[0].q) || {}, man = r[1], q = {}, chapters = {}, items = {};
        Object.keys(qi).sort().forEach(function (id, i) {
          var wrong = i % 4 === 1;
          q[id] = {h: wrong ? "10" : "1", u: i % 7 === 0 ? "1" : "0", t: now - 86400 - i, d: wrong ? 0 : day - 1, box: wrong ? 0 : 1, pick: ["b"], kr: qi[id][5]};
          if (wrong) q[id].c = "KCWTD".charAt(i % 5);
        });
        (man.chapters || []).filter(function (c) { return c.status !== "planned"; }).forEach(function (c, i) {
          var read = {};
          (c.sections || []).forEach(function (row, j) { if (i === 0 || j % 2 === 0) read[row[0]] = now - 90000; });
          chapters[c.slug] = {read: read};
        });
        Object.keys((r[0] && r[0].s) || {}).slice(0, 3).forEach(function (id, i) {
          items[id] = {t: now - 4000, tries: 1, self: "11010", score: i ? 8 : 5, band: i ? "Customer-ready" : "Repair and repeat", missing: i ? [] : ["kp2"]};
        });
        var mock = (man.mocks || [])[0], ref = mock ? mock.slug : "mock-exam-1";
        function att(id, kind, refv, p, ago, first) {
          return {v: 1, id: id, kind: kind, ref: refv, first: first, over: 0, startedAt: now - ago - 6000, submittedAt: now - ago,
            activeSec: kind === "mock" ? 6120 : 540, limitSec: 0, build: "", total: 20, correct: Math.round(p / 5), pct: p, sureCorrect: Math.round(p / 6),
            domains: {d1: {c: Math.round(p / 20), n: 5}, d2: {c: 4, n: 5}, d3: {c: 4, n: 5}, d4: {c: 5, n: 5}}, topics: {}};
        }
        St.load({
          settings: {plan: "a", planStart: "2026-10-05"},
          progress: {chapters: chapters},
          qstats: {sf: 40, q: q},
          speak: {items: items},
          attempts: [att("a-shot-m2", "mock", ref + "-b", 85, 86400, 1), att("a-shot-m1", "mock", ref, 70, 5 * 86400, 1), att("a-shot-c1", "mix", "mix", 80, 2 * 86400, 1)]
        });
        return view.mount(el, [], {hot: null});
      });
    });
  }
})(globalThis.SAA = globalThis.SAA || {});
