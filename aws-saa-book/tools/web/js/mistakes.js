/* mistakes.js (owner C): the mistakes log, ARCHITECTURE.md section 7.6. View mistakes; reader mount mistakes. */
(function (SAA) {
  "use strict";

  var U = SAA.U, h = U.h, QV = SAA.QView, Sc = SAA.Scoring;
  var PAGE = 20, SHORT = 5, STEM = 80;

  function stats() { return (SAA.Store && SAA.Store.get("qstats")) || {}; }

  function stemStart(q) {
    var s = String((q && q.stem) || "");
    return s.length > STEM ? s.slice(0, STEM).replace(/\s+\S*$/, "") + "…" : s;
  }

  function conceptName(id, names) {
    return names[id] || String(id || "").replace(/-/g, " ");
  }

  function draw(root, qindex, manifest, short) {
    var filterC = "", filterD = "", shown = short ? SHORT : PAGE, cache = { q: {}, facts: {} }, names = {}, alive = true;
    var domains = (manifest && manifest.domains) || [];
    ((manifest && manifest.terms) || []).forEach(function (t) { names[t[0]] = t[1]; });

    function rows() {
      return Sc.mistakes(stats(), qindex).filter(function (r) {
        if (filterC === "none" ? !!r.c : (filterC && r.c !== filterC)) return false;
        if (filterD && String(r.d) !== filterD) return false;
        return true;
      });
    }

    function rowHtml(r) {
      var q = cache.q[r.id];
      return h`<li class="mk-row" data-q="${r.id}">
        <button type="button" class="mk-open" data-act="mk-open" data-q="${r.id}" aria-expanded="false"><span class="mk-stem">${q ? stemStart(q) : r.id}</span></button>
        <p class="mk-meta"><span class="mk-ch">${QV.chapterTitle(r.slug)}</span>
          <span class="pill ${r.last === "wrong" ? "bad" : "warn"}">${r.last === "wrong" ? "Wrong" : "Right but not sure"}</span>
          <span class="mk-cause">${r.c ? h`<span class="mk-code">${r.c}</span> ${QV.CAUSE[r.c]}` : h`<span class="mk-code">?</span> No cause yet`}</span>
          <span class="mono">Box ${r.box}</span>
          <span class="mono">${QV.fmtDate(r.t)}</span></p>
        <div class="mk-rev" hidden></div>
      </li>`;
    }

    /* The next step when the log is empty: the quiz of the chapter she reads, else the first chapter with a quiz. */
    function firstQuiz() {
      var progress = (SAA.Store && SAA.Store.get("progress")) || {}, tok = String((progress.last && progress.last.route) || "").split(".");
      var chapters = (manifest && manifest.chapters) || [], hit = null, i;
      function has(c) { return c && c.status !== "planned" && c.counts && c.counts.q > 0; }
      if (tok[0] === "ch" && tok[1]) chapters.forEach(function (c) { if (c.slug === tok[1] && has(c)) hit = c; });
      for (i = 0; !hit && i < chapters.length; i++) if (has(chapters[i])) hit = chapters[i];
      return hit;
    }

    function emptyNote() {
      var c = firstQuiz();
      return h`<p class="notice">Your mistakes log is empty. Questions that you miss or mark as not sure appear here.${c ? h` Start with the quiz of the chapter you are reading: <a class="xr" href="${"#quiz." + c.slug}">${c.title}</a>.` : null}</p>`;
    }

    function phRow(title, state, action) {
      return h`<li class="ph-row"><p class="ph-m"><span class="ph-t">${title}</span> <span class="ph-s">${state}</span></p>${action}</li>`;
    }
    function go(href, text, primary) { return h`<a class="${primary ? "btn primary" : "btn"}" href="${href}">${text}</a>`; }
    function off(text) { return h`<button type="button" class="btn" disabled>${text}</button>`; }

    /* The hub above the log: every way to practise, with its state. */
    function hub() {
      var box = root.querySelector(".ph-box"), n, attempts, today, mixDone = null, exam, drills, mocks, top;
      if (!alive || !box) return;
      n = Sc.mistakes(stats(), qindex).length;
      attempts = (SAA.Store && SAA.Store.attempts()) || [];
      today = U.day();
      attempts.forEach(function (a) { if (!mixDone && a.kind === "mix" && U.day((a.submittedAt || 0) * 1000) === today) mixDone = a; });
      exam = SAA.Store ? SAA.Store.get("exam") : null;
      if (!(exam && !exam.none && exam.phase === "run" && Array.isArray(exam.order))) exam = null;
      drills = (manifest && manifest.drills) || [];
      mocks = (manifest && manifest.mocks) || [];
      top = [
        mixDone ? phRow("Daily mix", "Done today: " + mixDone.pct + "%", go("#attempt." + mixDone.id, "Open the result"))
          : phRow("Daily mix", "New questions, older questions and your mistakes", go("#mix", "Start", true)),
        n ? phRow("Retry my mistakes", n + (n === 1 ? " question" : " questions") + " in your mistakes log", go("#retry", "Retry"))
          : phRow("Retry my mistakes", "Off: your mistakes log is empty", off("Retry")),
        n ? phRow("Ten stem-first questions", "Read the stem and say what it asks, before you see the options", go("#retry.w", "Start"))
          : phRow("Ten stem-first questions", "Off: it uses the questions that you missed", off("Start"))
      ];
      U.set(box, h`<ul class="ph">${top}</ul>
        ${drills.length ? h`<h2>Domain drills</h2>
          <ul class="ph">${drills.map(function (d) {
            var dom = null;
            domains.forEach(function (x) { if (x.id === d.domain) dom = x; });
            return phRow(d.title, (dom ? dom.title + " · " : "") + d.count + (d.count === 1 ? " question" : " questions"), go("#drill.d" + d.domain, "Start"));
          })}</ul>` : null}
        <h2>Mock exams</h2>
        ${mocks.length ? h`<ul class="ph">${mocks.map(function (m) {
          var last = null, done = 0;
          if (exam && exam.ref === m.slug) {
            exam.order.forEach(function (id) { if (exam.ans && exam.ans[id] && exam.ans[id].p && exam.ans[id].p.length) done++; });
            return phRow(m.title, "In progress: " + done + " of " + exam.order.length + " answered", go("#mock." + m.n, "Resume", true));
          }
          attempts.forEach(function (a) { if (!last && a.kind === "mock" && a.ref === m.slug) last = a; });
          if (last) return phRow(m.title, h`Last result: <a class="xr" href="${"#attempt." + last.id}">${last.pct}% on ${QV.fmtDate(last.submittedAt)}</a>`, go("#mock." + m.n, "Take it again"));
          return phRow(m.title, "Not started · " + m.count + " questions in " + U.fmtMin(m.minutes), go("#mock." + m.n, "Start"));
        })}</ul>` : h`<p class="ph-none">No mock exam is written yet.</p>`}`);
    }

    function list() {
      var all = rows(), page = all.slice(0, shown), need = page.map(function (r) { return r.id; }).filter(function (id) { return !cache.q[id]; });
      var box = root.querySelector(".mk-box"), btns = root.querySelector(".mk-btns");
      if (btns) btns.hidden = !Sc.mistakes(stats(), qindex).length;
      hub();
      function paint() {
        var pairs;
        if (!alive || !box) return;
        if (!all.length) {
          U.set(box, filterC || filterD ? h`<p class="notice">No question matches these filters.</p>` : emptyNote());
          return;
        }
        U.set(box, h`<p class="mk-count" role="status">${all.length} ${all.length === 1 ? "question" : "questions"}${short && all.length > SHORT ? ", the first " + SHORT + " shown" : ""}</p>
          <ul class="mk">${page.map(rowHtml)}</ul>
          ${!short && all.length > shown ? h`<p><button type="button" class="btn" data-act="mk-more">Show ${Math.min(PAGE, all.length - shown)} more</button></p>` : null}`);
        if (short) return;
        pairs = Sc.confusions(stats(), qindex).slice(0, 5);
        U.set(root.querySelector(".mk-pairs-box"), pairs.length ? h`<h2>Pairs you confuse</h2>
          <ul class="mk-pairs">${pairs.map(function (p) { return h`<li>${conceptName(p.a, names)} <span class="mk-vs">and</span> ${conceptName(p.b, names)} <span class="mono">${p.n} ${p.n === 1 ? "time" : "times"}</span></li>`; })}</ul>` : null);
      }
      if (!need.length) { paint(); return Promise.resolve(); }
      return SAA.Content.questions(need).then(function (res) {
        Object.keys(res.q || {}).forEach(function (id) { cache.q[id] = res.q[id]; });
        Object.keys(res.facts || {}).forEach(function (id) { cache.facts[id] = res.facts[id]; });
        paint();
      }, function () { if (alive && box) QV.fail(box, list); });
    }

    U.set(root, h`<div class="mkv${short ? " mkv-short" : ""}">
      ${short ? null : h`<h1 tabindex="-1">Practice</h1>
        <div class="ph-box"></div>
        <h2 id="mk-log">Mistakes log</h2>
        <p class="lede">Questions that you missed or marked as not sure. A question leaves the log after two sure, correct answers on two different days.</p>`}
      ${short ? h`<p class="mk-btns" hidden><a class="btn primary" href="#retry">Retry these</a> <a class="btn" href="#retry.w">Ten stem-first questions</a> <a class="btn quiet" href="#mistakes">Open the full log</a></p>` : null}
      ${short ? null : h`<div class="mk-filters">
        <p><label for="mk-f-c">Cause</label> <select id="mk-f-c">
          <option value="">All causes</option>
          ${QV.CAUSE_ORDER.map(function (c) { return h`<option value="${c}">${c}: ${QV.CAUSE[c]}</option>`; })}
          <option value="none">No cause yet</option></select></p>
        <p><label for="mk-f-d">Domain</label> <select id="mk-f-d">
          <option value="">All domains</option>
          ${domains.map(function (d) { return h`<option value="${d.id}">Domain ${d.id}: ${d.title}</option>`; })}</select></p>
      </div>`}
      <div class="mk-box"></div>
      <div class="mk-pairs-box"></div>
    </div>`);
    var r = root.firstElementChild;
    U.on(r, "change", "#mk-f-c", function (e, sel) { filterC = sel.value; shown = PAGE; list(); });
    U.on(r, "change", "#mk-f-d", function (e, sel) { filterD = sel.value; shown = PAGE; list(); });
    U.on(r, "click", "[data-act=\"mk-more\"]", function () { shown += PAGE; list(); });
    U.on(r, "click", "[data-act=\"mk-open\"]", function (e, btn) {
      var id = btn.getAttribute("data-q"), li = btn.closest(".mk-row"), rev = li.querySelector(".mk-rev"), rec = (stats().q || {})[id], q = cache.q[id];
      if (!rev.hidden) { rev.hidden = true; rev.textContent = ""; btn.setAttribute("aria-expanded", "false"); return; }
      if (!q || !rec) return;
      QV.review(rev, q, { p: rec.pick || [], ok: /1$/.test(rec.h || "") ? 1 : 0, u: /1$/.test(rec.u || "") ? 1 : 0 },
        { cause: true, c: rec.c || null, facts: cache.facts });
      rev.hidden = false;
      btn.setAttribute("aria-expanded", "true");
    });
    U.on(r, "click", ".mk-rev [data-act=\"q-cause\"]", function (e, btn) {
      var li = btn.closest(".mk-row"), c = btn.getAttribute("data-c"), cell = li ? li.querySelector(".mk-cause") : null;
      if (cell && QV.CAUSE[c]) U.set(cell, h`<span class="mk-code">${c}</span> ${QV.CAUSE[c]}`);
    });
    QV.bindReview(r, function (qid) { return cache.q[qid] || null; });
    return { ready: list(), stop: function () { alive = false; } };
  }

  var live = null;

  var view = {
    mount: function (el) {
      var root = QV.root(el, "pv");
      return Promise.all([SAA.Content.qindex(), SAA.Content.manifest()]).then(function (r) {
        live = draw(root, r[0], r[1], false);
        return live.ready;
      });
    },
    unmount: function () { if (live) live.stop(); live = null; },
    title: function () { return "Practice"; }
  };

  /* The short form inside chapter 00 (mistakes.md). */
  function mount(el) {
    var ctl = null, gone = false;
    if (!SAA.Content) return undefined;
    Promise.all([SAA.Content.qindex(), SAA.Content.manifest()]).then(function (r) {
      if (gone) return;
      ctl = draw(QV.root(el, "pv"), r[0], r[1], true);
    }).catch(function () { el.hidden = true; });
    return function () { gone = true; if (ctl) ctl.stop(); };
  }

  function shot(el) {
    var root = QV.root(el, "pv");
    if (SAA.Test) SAA.Test.clock = function () { return 1791000000000; };
    if (SAA.Store && SAA.Store.reset) SAA.Store.reset();
    return Promise.all([SAA.Content.qindex(), SAA.Content.manifest()]).then(function (r) {
      var ids = Object.keys((r[0] && r[0].q) || {}).sort().filter(function (id) { return r[0].q[id][3] === 0; }).slice(0, 6);
      var q = {}, now = U.now(), pattern = [["0", "0", 0, "W"], ["10", "00", 0, "K"], ["1", "1", 0, null], ["01", "00", 1, "C"], ["0", "1", 0, null], ["00", "00", 0, "D"]];
      ids.forEach(function (id, i) {
        var p = pattern[i % pattern.length], wrong = Object.keys((r[0].wrong && r[0].wrong[id]) || {});
        q[id] = { h: p[0], u: p[1], t: now - (i + 1) * 86400, d: null, box: p[2], pick: wrong.slice(0, 1), c: p[3], kr: r[0].q[id][5] };
      });
      if (SAA.Store && SAA.Store.load) SAA.Store.load({ qstats: { v: 1, updatedAt: now, sf: 0, q: q } });
      live = draw(root, r[0], r[1], false);
      return live.ready.then(function () {
        var b = root.querySelector("[data-act=\"mk-open\"]");
        if (b) b.click();
      });
    });
  }

  if (SAA.Router) SAA.Router.register("mistakes", view);
  if (SAA.Reader && SAA.Reader.registerMount) SAA.Reader.registerMount("mistakes", mount);
  if (SAA.Test && SAA.Test.register) SAA.Test.register("mistakes", shot);
})(globalThis.SAA = globalThis.SAA || {});
