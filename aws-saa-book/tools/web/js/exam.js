/* exam.js (owner C): the timed mock and the results page, ARCHITECTURE.md sections 7.4 and 7.5.
   A port of the engine of saa-c03-diagnostic.html: shuffled order, timer on active time, flag,
   answer sheet, resume, domain breakdown. Views mock and attempt. */
(function (SAA) {
  "use strict";

  var U = SAA.U, h = U.h, QV = SAA.QView, Sc = SAA.Scoring;
  var WARN_MIN = [30, 10, 5];

  var R = null;       // the running exam view: {root, entry, file, byId, last, tickN, timer, confirm, warned, offs}
  var intro = null;   // the mounted intro: {start()}
  var memDoc = null;  // the exam document when there is no Store (never in the real page)

  function cfg() { return (SAA.state && SAA.state.cfg) || {}; }

  function X() {
    var d = SAA.Store ? SAA.Store.get("exam") : memDoc;
    return d && !d.none && d.phase === "run" && Array.isArray(d.order) ? d : null;
  }

  function patchExam(p) { if (SAA.Store) SAA.Store.patch("exam", p); }

  function mockEntry(manifest, n) {
    var hit = null;
    ((manifest && manifest.mocks) || []).forEach(function (m) { if (String(m.n) === String(n)) hit = m; });
    return hit;
  }

  function mockBySlug(manifest, slug) {
    var hit = null;
    ((manifest && manifest.mocks) || []).forEach(function (m) { if (m.slug === slug) hit = m; });
    return hit;
  }

  function entryOf(x, id) {
    if (!x.ans) x.ans = {};
    if (!x.ans[id]) x.ans[id] = { p: [], u: 0, ms: 0 };
    return x.ans[id];
  }

  function answered(x) {
    var n = 0;
    x.order.forEach(function (id) { if (x.ans && x.ans[id] && x.ans[id].p && x.ans[id].p.length) n++; });
    return n;
  }

  function unsureCount(x) {
    var n = 0;
    x.order.forEach(function (id) { if (x.ans && x.ans[id] && x.ans[id].u) n++; });
    return n;
  }

  /* ---------- intro ---------- */

  function noMock(root, n, manifest) {
    var drills = (manifest && manifest.drills) || [];
    U.set(root, h`<div class="ex-intro"><h1 tabindex="-1">Mock exam ${n || ""}</h1>
      <p class="notice">Mock exam ${n || ""} is not written yet.</p>
      ${drills.length ? h`<p>Practise with a domain drill until it is ready:</p>
        <ul class="ex-links">${drills.map(function (d) { return h`<li><a class="xr" href="${"#drill.d" + d.domain}">${d.title}</a></li>`; })}</ul>`
        : h`<p><a class="xr" href="#mistakes">Open the mistakes log</a></p>`}</div>`);
  }

  function lastAttempt(slug) {
    var hit = null;
    ((SAA.Store && SAA.Store.attempts()) || []).forEach(function (a) { if (!hit && a.kind === "mock" && a.ref === slug) hit = a; });
    return hit;
  }

  function drawIntro(root, entry, manifest) {
    var settings = (SAA.Store && SAA.Store.get("settings")) || {}, facts = (manifest && manifest.examFacts) || {};
    var other = X(), otherEntry = other && other.ref !== entry.slug ? mockBySlug(manifest, other.ref) : null;
    var last = lastAttempt(entry.slug), domains = (manifest && manifest.domains) || [], split = entry.split || [];
    var armed = false, busy = false;
    if (other && other.ref === entry.slug) other = null;

    function draw() {
      var otherName = otherEntry ? otherEntry.title : "Another mock exam";
      U.set(root, h`<div class="ex-intro">
        <p class="eyebrow">Timed mock exam</p>
        <h1 tabindex="-1">${entry.title}</h1>
        <p class="lede">${entry.count} questions in ${U.fmtMin(entry.minutes)}, split across the four domains like the real exam. Take it in one sitting, without notes.</p>
        ${entry.synthetic ? h`<p class="notice">Preview mock: it is built from chapter questions to test this page. It is not one of the two mock exams of the book.</p>` : null}
        ${domains.length ? h`<div class="tw" role="region" tabindex="0" aria-label="Table: Exam domain"><table class="tb tb-plain">
          <thead><tr><th scope="col">Exam domain</th><th scope="col">Exam weight</th><th scope="col">Questions here</th></tr></thead>
          <tbody>${domains.map(function (d, i) { return h`<tr><td data-th="Exam domain">${d.title}</td><td data-th="Exam weight" class="mono">${d.weight}%</td><td data-th="Questions here" class="mono">${split[i] == null ? "" : split[i]}</td></tr>`; })}</tbody></table></div>` : null}
        ${last ? h`<p>Last result: <a class="xr" href="${"#attempt." + last.id}">${last.pct}% on ${QV.fmtDate(last.submittedAt)}</a></p>` : null}
        <h2>Rules</h2>
        <ul class="ex-rules">
          <li>Answers are final after Submit. There is no feedback before it.</li>
          <li>An unanswered question counts as wrong. Guess, and tick "I am not sure about this one".</li>
          <li>The timer counts only while this page is open. You can close the page and continue later.</li>
        </ul>
        <p class="ex-extra"><label for="ex-extra"><input type="checkbox" id="ex-extra"${settings.extraTime ? h` checked` : null}> Add extra time (ESL accommodation)${facts.esl && facts.esl.text ? ": " + facts.esl.text : ""}</label></p>
        ${other ? h`<div class="notice ex-other"><p>${otherName} is in progress (${answered(other)} of ${other.order.length} answered). Finish it or discard it before you start this one.</p>
          <p>${otherEntry ? h`<a class="btn primary" href="${"#mock." + otherEntry.n}">Resume mock ${otherEntry.n}</a> ` : null}<button type="button" class="btn" data-act="ex-discard">${armed ? "Confirm: discard it and lose its answers" : "Discard it"}</button></p></div>`
          : h`<p><button type="button" class="btn primary ex-start" data-act="ex-start"${busy ? h` disabled` : null}>Start</button></p>`}
        <p class="ex-foot">Questions are original and written for practice. They are not real exam questions.</p>
      </div>`);
      var r = root.firstElementChild;
      U.on(r, "change", "#ex-extra", function (e, box) {
        settings.extraTime = box.checked ? 1 : 0;
        if (SAA.Store) SAA.Store.patch("settings", { extraTime: box.checked ? 1 : 0 });
      });
      U.on(r, "click", "[data-act=\"ex-start\"]", function () { start(); });
      U.on(r, "click", "[data-act=\"ex-discard\"]", function () {
        var b;
        if (!armed) { armed = true; draw(); b = root.querySelector("[data-act=\"ex-discard\"]"); if (b) b.focus(); return; }
        if (SAA.Store) SAA.Store.replace("exam", null); else memDoc = null;
        other = null; armed = false; draw();
        U.announce("The mock exam in progress was discarded.");
      });
    }

    function start() {
      if (busy || other) return Promise.resolve(null);
      busy = true;
      return SAA.Content.mock(entry.slug).then(function (file) {
        var list = (file && file.questions) || [], doc, extra, box = root.querySelector("#ex-extra");
        if (!list.length) { busy = false; noMock(root, entry.n, manifest); return null; }
        extra = box ? box.checked : !!settings.extraTime;
        doc = {
          v: 1, id: U.uid("a"), kind: "mock", ref: entry.slug, build: (SAA.state && SAA.state.build) || null, phase: "run",
          startedAt: U.now(), limitSec: ((file.minutes || entry.minutes || 0) + (extra ? (cfg().extraMinutes || 0) : 0)) * 60,
          activeMs: 0, cur: 0, order: U.shuffle(list.map(function (q) { return q.id; })), oo: {}, ans: {}
        };
        list.forEach(function (q) { doc.oo[q.id] = U.shuffle(q.options.map(function (o) { return o.id; })); });
        if (SAA.Store) SAA.Store.replace("exam", doc); else memDoc = doc;
        intro = null;
        begin(root, entry, file);
        focusTitle(root);
        return doc;
      }, function () { busy = false; QV.fail(root, function () { drawIntro(root, entry, manifest); }); return null; });
    }

    intro = { start: start };
    draw();
  }

  function focusTitle(root) {
    var h1 = root.querySelector("h1");
    if (h1) { try { h1.focus({ preventScroll: true }); } catch (e) { /* older engines */ } }
    try { globalThis.scrollTo(0, 0); } catch (e2) { /* no window */ }
  }

  /* ---------- in progress ---------- */

  function begin(root, entry, file) {
    var x = X(), byId = {}, r, left, app = document.getElementById("saa");
    (file.questions || []).forEach(function (q) { byId[q.id] = q; });
    stop();
    R = { root: root, entry: entry, file: file, byId: byId, last: U.nowMs(), tickN: 0, timer: null, confirm: false, warned: {}, offs: [], up: false };
    left = x.limitSec - Math.floor((x.activeMs || 0) / 1000);
    WARN_MIN.forEach(function (m) { if (left <= m * 60) R.warned[m] = 1; });
    R.up = left <= 0;
    U.set(root, h`<div class="ex">
      <h1 class="vh" tabindex="-1">${entry.title}</h1>
      <div class="ex-bar" role="group" aria-label="Exam controls">
        <span class="ex-title">${entry.title}</span>
        <span class="ex-prog mono"></span>
        <span class="timer" role="timer" aria-label="Time remaining"></span>
        <button type="button" class="btn ex-sheet-btn" data-act="ex-sheet" aria-expanded="false">Answer sheet</button>
        <button type="button" class="btn primary" data-act="ex-submit">Submit</button>
      </div>
      <p class="ex-up notice" role="alert" hidden>Time is up. The real exam ends here. You can still submit.</p>
      <div class="ex-grid">
        <div class="ex-main"><div class="ex-confirm"></div><div class="ex-q"></div></div>
        <aside class="ex-sheet" aria-label="Answer sheet"></aside>
      </div>
    </div>`);
    r = root.firstElementChild;
    R.offs.push(U.on(r, "click", "[data-act=\"ex-submit\"]", function () { askSubmit(true); }));
    R.offs.push(U.on(r, "click", "[data-act=\"ex-keep\"]", function () { askSubmit(false); }));
    R.offs.push(U.on(r, "click", "[data-act=\"ex-do\"]", function () { submit(); }));
    R.offs.push(U.on(r, "click", "[data-act=\"ex-go\"]", function (e, b) { go(Number(b.getAttribute("data-i"))); }));
    R.offs.push(U.on(r, "click", "[data-act=\"ex-sheet\"]", function (e, b) { openSheet(b); }));
    R.offs.push(U.on(globalThis, "pagehide", null, function () { saveNow(); }));
    R.timer = setInterval(tick, 1000);
    drawQ();
    drawSheet();
    paintTimer();
    if (app) {
      var bar = r.querySelector(".ex-bar"), fixed = false;
      try { fixed = globalThis.getComputedStyle(bar).position === "fixed"; } catch (e) { fixed = false; }
      if (fixed) app.style.setProperty("--ex-h", bar.offsetHeight + "px");
    }
  }

  function stop() {
    var app;
    if (!R) return;
    if (R.timer) clearInterval(R.timer);
    R.offs.forEach(function (off) { try { off(); } catch (e) { /* gone */ } });
    R = null;
    app = typeof document !== "undefined" ? document.getElementById("saa") : null;
    if (app) app.style.removeProperty("--ex-h");
  }

  /* The cloud write: on answer, flag, navigation and pagehide. */
  function saveNow() {
    var x = X(), id, p;
    if (!x) return;
    id = x.order[x.cur];
    p = { activeMs: x.activeMs, cur: x.cur, ans: {} };
    p.ans[id] = U.clone(entryOf(x, id));
    patchExam(p);
  }

  function drawQ(focus) {
    var x = X(), id, q, a, state, qEl;
    if (!R || !x) return;
    id = x.order[x.cur];
    q = R.byId[id];
    qEl = R.root.querySelector(".ex-q");
    if (!q) { U.set(qEl, h`<p class="notice">This question is no longer in the book. Go to the next one.</p>`); paintBar(); return; }
    a = entryOf(x, id);
    state = { order: (x.oo && x.oo[id]) || q.options.map(function (o) { return o.id; }), picked: a.p.slice(), unsure: a.u ? 1 : 0, checked: false, stage: "opts" };
    QV.render(qEl, q, state, {
      mode: "exam", stemFirst: false, n: x.cur + 1, of: x.order.length, focus: focus || null,
      onChange: function (s) {
        var live = X(), e;
        if (!live) return;
        e = entryOf(live, id);
        e.p = s.picked.slice();
        e.u = s.unsure ? 1 : 0;
        saveNow();
        paintBar();
        drawSheet();
        if (R && R.confirm) askSubmit(true, true);
      },
      onNav: function (d) { var live = X(); if (live) go(live.cur + d); }
    });
    paintBar();
  }

  function paintBar() {
    var x = X(), el;
    if (!R || !x) return;
    el = R.root.querySelector(".ex-prog");
    if (el) el.textContent = "Answered " + answered(x) + "/" + x.order.length;
  }

  function cells(x) {
    return h`<div class="cells">${x.order.map(function (id, i) {
      var a = (x.ans && x.ans[id]) || {}, done = !!(a.p && a.p.length), cls = "cell" + (done ? " ans" : "") + (a.u ? " uns" : "") + (i === x.cur ? " cur" : "");
      var label = "Question " + (i + 1) + (done ? ", answered" : ", unanswered") + (a.u ? ", not sure" : "") + (i === x.cur ? ", current" : "");
      return h`<button type="button" class="${cls}" data-act="ex-go" data-i="${i}" aria-label="${label}">${i + 1}</button>`;
    })}</div>
    <p class="ex-legend"><span>Filled: answered</span><span>?: not sure</span><span>Ring: current</span></p>`;
  }

  function drawSheet() {
    var x = X(), el;
    if (!R || !x) return;
    el = R.root.querySelector(".ex-sheet");
    if (el) U.set(el, h`<h2 class="ex-sheet-t">Answer sheet</h2>${cells(x)}`);
  }

  /* On a phone the answer sheet opens as a sheet; on desktop it is the right column and the button is hidden. */
  function openSheet(btn) {
    var x = X(), body, aside;
    if (!R || !x) return;
    if (SAA.Pop && SAA.Pop.sheet) {
      body = SAA.Pop.sheet(cells(x), { label: "Answer sheet" });
      if (body) {
        U.on(body, "click", "[data-act=\"ex-go\"]", function (e, b) {
          var i = Number(b.getAttribute("data-i"));
          SAA.Pop.closeSheet(true);
          go(i);
        });
        return;
      }
    }
    aside = R.root.querySelector(".ex-sheet");
    if (aside) {
      aside.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", aside.classList.contains("is-open") ? "true" : "false");
    }
  }

  function go(i) {
    var x = X(), h1;
    if (!R || !x || !(i >= 0) || i >= x.order.length || i === x.cur) return;
    saveNow();
    x.cur = i;
    saveNow();
    drawQ();
    drawSheet();
    try { globalThis.scrollTo(0, 0); } catch (e) { /* no window */ }
    U.announce("Question " + (i + 1) + " of " + x.order.length);
    h1 = R.root.querySelector(".q-stem");
    if (h1) { h1.setAttribute("tabindex", "-1"); try { h1.focus({ preventScroll: true }); } catch (e2) { /* older engines */ } }
  }

  /* ---------- timer: active time only ---------- */

  function tick() {
    var x = X(), now, d;
    if (!R) return;
    if (!x) { stop(); return; }
    now = U.nowMs();
    d = now - R.last;
    R.last = now;
    if (d > 0 && d < 90000) {
      x.activeMs = (x.activeMs || 0) + d;
      entryOf(x, x.order[x.cur]).ms += d;
    }
    paintTimer();
    R.tickN++;
    if (R.tickN % 10 === 0 && SAA.Store && SAA.Store.save) SAA.Store.save("exam");
  }

  function paintTimer() {
    var x = X(), t, up, left;
    if (!R || !x) return;
    t = R.root.querySelector(".timer");
    up = R.root.querySelector(".ex-up");
    left = x.limitSec - Math.floor((x.activeMs || 0) / 1000);
    if (!t) return;
    if (left >= 0) {
      t.textContent = U.fmtClock(left);
      t.classList.remove("over");
      t.setAttribute("aria-label", "Time remaining");
    } else {
      t.textContent = "+" + U.fmtClock(-left) + " over";
      t.classList.add("over");
      t.setAttribute("aria-label", "Time over the limit");
    }
    if (up) up.hidden = left > 0;
    WARN_MIN.forEach(function (m) {
      if (left <= m * 60 && left > 0 && !R.warned[m]) { R.warned[m] = 1; U.announce(m + " minutes left."); }
    });
    if (left <= 0 && !R.up) { R.up = true; U.announce("Time is up. The real exam ends here."); }
  }

  /* ---------- submit ---------- */

  function askSubmit(open, quiet) {
    var x = X(), box, blank, unsure, hd;
    if (!R || !x) return;
    R.confirm = !!open;
    box = R.root.querySelector(".ex-confirm");
    if (!open) { U.set(box, null); return; }
    blank = x.order.length - answered(x);
    unsure = unsureCount(x);
    U.set(box, h`<div class="ex-ask" role="group" aria-label="Submit the exam">
      <h2 tabindex="-1">Submit and score the exam?</h2>
      <p>${blank ? h`<strong>${blank} unanswered</strong> ${blank === 1 ? "question counts" : "questions count"} as wrong. ` : h`All ${x.order.length} questions are answered. `}${unsure ? unsure + " marked not sure. " : ""}You cannot change answers after you submit.</p>
      <p class="ex-ask-b"><button type="button" class="btn primary" data-act="ex-do">Submit and score</button> <button type="button" class="btn" data-act="ex-keep">Keep working</button></p>
    </div>`);
    if (!quiet) {
      try { globalThis.scrollTo(0, 0); } catch (e) { /* no window */ }
      hd = box.querySelector("h2");
      if (hd) { try { hd.focus({ preventScroll: true }); } catch (e2) { /* older engines */ } }
    }
  }

  function submit() {
    var x = X(), list, first, doc, now, stats, patch, byId, i, q, a, ok;
    if (!R || !x) return null;
    byId = R.byId;
    now = U.now();
    list = x.order.map(function (id) { return byId[id]; }).filter(Boolean);
    first = !((SAA.Store && SAA.Store.attempts()) || []).some(function (t) { return t.kind === "mock" && t.ref === x.ref; });
    doc = Sc.scoreAttempt(list, x.ans || {}, {
      id: x.id, kind: "mock", ref: x.ref, startedAt: x.startedAt, submittedAt: now,
      activeSec: Math.round((x.activeMs || 0) / 1000), limitSec: x.limitSec, build: x.build,
      over: (x.activeMs || 0) / 1000 > x.limitSec ? 1 : 0, first: first,
      order: x.order.filter(function (id) { return !!byId[id]; })
    });
    if (SAA.Store) SAA.Store.addAttempt(doc);
    stats = (SAA.Store && SAA.Store.get("qstats")) || {};
    patch = { q: {} };
    for (i = 0; i < list.length; i++) {
      q = list[i];
      a = doc.answers[q.id];
      ok = a.ok === 1;
      patch.q[q.id] = Sc.record((stats.q && stats.q[q.id]) || null, q, a.p, ok, !!a.u, now);
      SAA.bus.emit("answer", { qid: q.id, ok: ok, unsure: !!a.u, kind: "mock" });
    }
    if (SAA.Store) { SAA.Store.patch("qstats", patch); SAA.Store.replace("exam", null); } else memDoc = null;
    stop();
    if (SAA.Router) SAA.Router.go("#attempt." + doc.id, { replace: true });
    return doc;
  }

  /* ---------- view: mock ---------- */

  var mockView = {
    mount: function (el, args) {
      var n = args[0] || "", root = QV.root(el, "pv");
      intro = null;
      return SAA.Content.manifest().then(function (manifest) {
        var entry = mockEntry(manifest, n), x = X();
        if (!entry) { noMock(root, n, manifest); return null; }
        if (x && x.ref === entry.slug) {
          return SAA.Content.mock(entry.slug).then(function (file) {
            if (!file || !(file.questions || []).length) { noMock(root, n, manifest); return; }
            begin(root, entry, file);
          });
        }
        drawIntro(root, entry, manifest);
        return null;
      });
    },
    unmount: function () {
      if (R) { saveNow(); stop(); }
      intro = null;
    },
    title: function (args) { return "Mock exam " + (args[0] || ""); },
    snapshot: function () {
      var x = X();
      return R && x ? { ref: x.ref, cur: x.cur, confirm: !!R.confirm } : null;
    }
  };

  /* ---------- view: attempt (results and review of any kind of attempt) ---------- */

  function attemptTitle(a, manifest) {
    var hit = null;
    if (a.kind === "mock") { hit = mockBySlug(manifest, a.ref); return hit ? hit.title : "Mock exam"; }
    if (a.kind === "chapter") return "Quiz: " + QV.chapterTitle(a.ref);
    if (a.kind === "drill") {
      ((manifest && manifest.drills) || []).forEach(function (d) { if (d.id === a.ref) hit = d; });
      return hit ? hit.title : "Drill";
    }
    if (a.kind === "mix") return "Daily mix";
    return a.ref === "w" ? "Ten stem-first questions" : "Retry my mistakes";
  }

  function level(p) {
    var g = cfg().gate || {};
    if (g.strong == null) return "";
    return p >= g.strong ? "is-good" : p >= g.domainMin ? "is-warn" : "is-bad";
  }

  function levelWord(cls) { return cls === "is-good" ? "strong" : cls === "is-warn" ? "close" : cls === "is-bad" ? "weak" : ""; }

  function summaryText(a, manifest) {
    var L = [], domains = (manifest && manifest.domains) || [], wrong = [], blank = [], unsure = [], topics;
    (a.order || []).forEach(function (id) {
      var x = (a.answers || {})[id];
      if (!x) return;
      if (!x.ok) { if (x.p && x.p.length) wrong.push(id); else blank.push(id); }
      if (x.u) unsure.push(id + (x.ok ? "*" : ""));
    });
    L.push("SAA-C03 Handbook, " + attemptTitle(a, manifest) + ", attempt " + a.id + (a.submittedAt ? ", " + QV.fmtDate(a.submittedAt) : ""));
    L.push("Overall: " + a.correct + "/" + a.total + " (" + a.pct + "%), sure and correct: " + a.sureCorrect + ", time: " + Math.round((a.activeSec || 0) / 60) + " min" + (a.over ? " (over the limit)" : ""));
    L.push("Domains: " + domains.map(function (d) {
      var r = (a.domains || {})["d" + d.id] || { c: 0, n: 0 };
      return "D" + d.id + " " + r.c + "/" + r.n + " (" + Sc.pct(r.c, r.n) + "%)";
    }).join(" | "));
    topics = Object.keys(a.topics || {}).sort();
    if (topics.length) L.push("Topics: " + topics.map(function (t) { return t + " " + a.topics[t].c + "/" + a.topics[t].n; }).join("; "));
    if (a.answers) {
      L.push("Wrong (id): " + (wrong.join(", ") || "none"));
      L.push("Unanswered (id): " + (blank.join(", ") || "none"));
      L.push("Not sure (id, * = still correct): " + (unsure.join(", ") || "none"));
    }
    return L.join("\n");
  }

  function saveLine() {
    var s = SAA.Store && SAA.Store.status ? SAA.Store.status() : "memory";
    if (s === "cloud") return "This result is saved online. Claude can read it in your session.";
    if (s === "local") return "This result is saved on this device only. Copy the summary to give it to Claude.";
    return "This result is not saved on this device. Copy the summary to keep it.";
  }

  function drawAttempt(root, a, manifest) {
    var domains = (manifest && manifest.domains) || [], facts = (manifest && manifest.examFacts) || {}, title = attemptTitle(a, manifest);
    var pcts = {}, filter = "wrong", loaded = null, loading = false, has = !!a.answers, counts = { wrong: 0, unsure: 0, all: 0 };
    var mins = Math.round((a.activeSec || 0) / 60), back;
    domains.forEach(function (d) { var r = (a.domains || {})["d" + d.id]; if (r && r.n) pcts[d.id] = Sc.pct(r.c, r.n); });
    (a.order || []).forEach(function (id) {
      var x = has ? a.answers[id] : null;
      if (!x) return;
      counts.all++;
      if (!x.ok) counts.wrong++;
      if (x.u) counts.unsure++;
    });
    back = a.kind === "chapter" ? h`<a class="btn quiet" href="${"#ch." + a.ref}">Back to the chapter</a>` : h`<a class="btn quiet" href="#progress">Open your progress</a>`;
    U.set(root, h`<div class="at">
      <p class="eyebrow">Result${a.submittedAt ? " · " + QV.fmtDate(a.submittedAt) : ""}</p>
      <h1 tabindex="-1">${title}</h1>
      <div class="score">
        <p class="bigscore"><span class="vh">Score: </span>${a.pct}<small>%</small></p>
        <ul class="score-f">
          <li>${a.correct} of ${a.total} correct</li>
          <li>Sure and correct: ${a.sureCorrect}</li>
          <li>Time used: ${U.fmtMin(mins)}${a.limitSec ? " of " + U.fmtMin(a.limitSec / 60) : ""}${a.over ? " (over the limit)" : ""}</li>
          ${a.kind === "mock" && facts.pass && facts.pass.text ? h`<li class="score-pass">Passing score of the real exam: ${facts.pass.text}. This page shows the percent of correct answers, which is a different scale.</li>` : null}
          ${a.correct - a.sureCorrect > 0 ? h`<li>${a.correct - a.sureCorrect} correct ${a.correct - a.sureCorrect === 1 ? "answer was" : "answers were"} marked not sure. Treat ${a.correct - a.sureCorrect === 1 ? "that topic" : "those topics"} as not known yet.</li>` : null}
        </ul>
      </div>
      ${domains.length ? h`<h2>By exam domain</h2>
        <div class="drows">${domains.map(function (d) {
          var r = (a.domains || {})["d" + d.id] || { c: 0, n: 0 }, p = Sc.pct(r.c, r.n), cls = r.n ? level(p) : "";
          return h`<div class="drow"><div class="drow-n">${d.title} <span class="drow-w">${d.weight}% of the exam</span></div>
            <div class="mono drow-v">${r.n ? r.c + "/" + r.n + " · " + p + "%" + (levelWord(cls) ? " · " + levelWord(cls) : "") : "no questions"}</div>
            <div class="bar" aria-hidden="true"><div class="bar-f ${cls}" style="${"width:" + (r.n ? p : 0) + "%"}"></div></div></div>`;
        })}</div>` : null}
      <h2>Review</h2>
      ${has ? h`<div class="at-filters" role="group" aria-label="Filter questions">
          <button type="button" class="chip" data-act="at-filter" data-f="wrong" aria-pressed="true">Wrong (${counts.wrong})</button>
          <button type="button" class="chip" data-act="at-filter" data-f="unsure" aria-pressed="false">Not sure (${counts.unsure})</button>
          <button type="button" class="chip" data-act="at-filter" data-f="all" aria-pressed="false">All (${counts.all})</button>
        </div><div class="at-list"></div>`
        : h`<p class="notice">The answers of this attempt are no longer stored on this device.</p>`}
      <h2>Send the numbers to Claude</h2>
      <p class="at-save">${saveLine()}</p>
      <label class="vh" for="at-summary">Result summary</label>
      <textarea id="at-summary" class="at-sum mono" readonly rows="7">${summaryText(a, manifest)}</textarea>
      <p><button type="button" class="btn" data-act="at-copy">Copy summary</button> <span class="at-note" role="status"></span></p>
      <p class="at-end">${has && counts.wrong && SAA.Quiz ? h`<button type="button" class="btn primary" data-act="at-retry">Retry the wrong ones</button> ` : null}${back}</p>
    </div>`);
    var r = root.firstElementChild;

    function list() {
      var box = r.querySelector(".at-list"), ids, stats = (SAA.Store && SAA.Store.get("qstats")) || {}, missing = 0;
      if (!box || !loaded) return;
      ids = a.order.filter(function (id) {
        var x = a.answers[id];
        if (!x) return false;
        return filter === "all" ? true : filter === "unsure" ? !!x.u : !x.ok;
      });
      box.textContent = "";
      ids.forEach(function (id) {
        var q = loaded.q[id], d;
        if (!q) { missing++; return; }
        d = document.createElement("div");
        d.className = "at-item";
        box.appendChild(d);
        QV.review(d, q, a.answers[id], { n: a.order.indexOf(id) + 1, cause: true, c: (stats.q && stats.q[id] && stats.q[id].c) || null, facts: loaded.facts });
      });
      if (!ids.length) U.set(box, h`<p class="at-none">Nothing in this filter.</p>`);
      else if (missing) {
        d0(box, missing);
      }
    }

    function d0(box, n) {
      var p = document.createElement("p");
      p.className = "notice";
      p.textContent = n + (n === 1 ? " question of this attempt is" : " questions of this attempt are") + " no longer in the book.";
      box.appendChild(p);
    }

    function loadList() {
      var box = r.querySelector(".at-list");
      if (!has || loaded || loading || !box) return Promise.resolve();
      loading = true;
      return SAA.Content.questions(a.order).then(function (res) { loaded = res; loading = false; list(); },
        function () { loading = false; QV.fail(box, loadList); });
    }

    U.on(r, "click", "[data-act=\"at-filter\"]", function (e, b) {
      var all = r.querySelectorAll("[data-act=\"at-filter\"]"), i;
      filter = b.getAttribute("data-f");
      for (i = 0; i < all.length; i++) all[i].setAttribute("aria-pressed", all[i] === b ? "true" : "false");
      list();
    });
    U.on(r, "click", "[data-act=\"at-copy\"]", function () {
      var ta = r.querySelector("#at-summary"), note = r.querySelector(".at-note");
      U.copy(ta.value).then(function (ok) {
        if (!ok) { try { ta.focus(); ta.select(); } catch (e) { /* nothing to select */ } }
        note.textContent = ok ? "Copied." : "Copy is blocked here. The text is selected: press copy on your keyboard.";
      });
    });
    U.on(r, "click", "[data-act=\"at-retry\"]", function () {
      var ids = a.order.filter(function (id) { return a.answers[id] && !a.answers[id].ok; });
      if (SAA.Quiz && ids.length) SAA.Quiz.start({ kind: "retry", ref: a.id, ids: ids, title: "Retry: " + title });
    });
    QV.bindReview(r, function (qid) { return loaded ? loaded.q[qid] : null; });
    return loadList();
  }

  var attemptView = {
    mount: function (el, args) {
      var id = args[0] || "", root = QV.root(el, "pv"), a = null;
      ((SAA.Store && SAA.Store.attempts()) || []).forEach(function (t) { if (t.id === id) a = t; });
      if (!a) {
        U.set(root, h`<div class="at"><h1 tabindex="-1">Result</h1><p class="notice">This result is not stored on this device.</p>
          <p><a class="btn" href="#progress">Open your progress</a></p></div>`);
        return null;
      }
      return SAA.Content.manifest().then(function (manifest) { drawAttempt(root, a, manifest); });
    },
    title: function () { return "Result"; }
  };

  /* ---------- screenshots (preview only) ---------- */

  function shotClock() { if (SAA.Test) SAA.Test.clock = function () { return 1791000000000; }; }

  function scripted(file, x) {
    /* a fixed pattern: about three of four right, some not sure, the last ones unanswered */
    x.order.forEach(function (id, i) {
      var q = null, right, wrong;
      file.questions.forEach(function (c) { if (c.id === id) q = c; });
      if (!q || i >= x.order.length - 4) return;
      right = Sc.correctIds(q);
      wrong = q.options.filter(function (o) { return !o.ok; })[0];
      x.ans[id] = { p: i % 4 === 3 ? [wrong.id] : right, u: i % 7 === 2 ? 1 : 0, ms: 60000 + (i % 5) * 9000 };
    });
  }

  function shotDoc(file, entry) {
    var doc = {
      v: 1, id: "a-shot-1", kind: "mock", ref: entry.slug, build: (SAA.state && SAA.state.build) || null, phase: "run",
      startedAt: U.now() - 3000, limitSec: (file.minutes || entry.minutes || 0) * 60, activeMs: 2520000, cur: 0,
      order: file.questions.map(function (q) { return q.id; }), oo: {}, ans: {}
    };
    file.questions.forEach(function (q) { doc.oo[q.id] = q.options.map(function (o) { return o.id; }); });
    return doc;
  }

  function shot(mode) {
    return function (el) {
      var root = QV.root(el, "pv");
      shotClock();
      if (SAA.Store && SAA.Store.reset) SAA.Store.reset();
      return SAA.Content.manifest().then(function (manifest) {
        var entry = (manifest.mocks || [])[0];
        if (!entry) { noMock(root, 1, manifest); return null; }
        return SAA.Content.mock(entry.slug).then(function (file) {
          var doc = shotDoc(file, entry), half = Math.floor(doc.order.length / 3), attempt, map = {};
          scripted(file, doc);
          if (mode === "run") {
            doc.order.forEach(function (id, i) { if (i >= half) delete doc.ans[id]; });
            doc.cur = Math.min(half, doc.order.length - 1);
            if (SAA.Store) SAA.Store.load({ exam: doc }); else memDoc = doc;
            begin(root, entry, file);
            if (R) { clearInterval(R.timer); R.timer = null; }
            return;
          }
          attempt = Sc.scoreAttempt(file.questions, doc.ans, {
            id: doc.id, kind: "mock", ref: doc.ref, startedAt: doc.startedAt, submittedAt: U.now(), activeSec: 6120,
            limitSec: doc.limitSec, build: doc.build, over: 0, first: 1, order: doc.order
          });
          map[attempt.id] = attempt;
          if (SAA.Store) SAA.Store.load({ attempts: map });
          return drawAttempt(root, attempt, manifest);
        });
      });
    };
  }

  SAA.Exam = {
    /* used by selftest.js to drive the real code */
    start: function () { return intro ? intro.start() : Promise.resolve(null); },
    tick: tick,
    go: go,
    submit: submit,
    askSubmit: askSubmit,
    doc: X,
    running: function () { return !!R; },
    summaryText: summaryText
  };

  if (SAA.Router) {
    SAA.Router.register("mock", mockView);
    SAA.Router.register("attempt", attemptView);
  }
  if (SAA.Test && SAA.Test.register) {
    SAA.Test.register("mock-run", shot("run"));
    SAA.Test.register("mock-results", shot("results"));
  }
})(globalThis.SAA = globalThis.SAA || {});
