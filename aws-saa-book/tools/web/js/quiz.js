/* quiz.js (owner C): learn-mode sessions, ARCHITECTURE.md section 7.3.
   Views quiz, drill, retry, mix; reader mounts quiz and return; Quiz.start(spec). */
(function (SAA) {
  "use strict";

  var U = SAA.U, h = U.h, QV = SAA.QView, Sc = SAA.Scoring;
  var ROUTE = { chapter: "quiz", drill: "drill", retry: "retry", mix: "mix" };

  var live = null;      // the session in progress (plain JSON)
  var pending = null;   // a spec handed to Quiz.start, waiting for its view
  var here = null;      // {name, key, root, questions, facts} of the mounted view

  function store(name) { return SAA.Store ? SAA.Store.get(name) || {} : {}; }
  function cfg() { return (SAA.state && SAA.state.cfg) || {}; }

  /* ---------- which questions ---------- */

  function readSlugs() {
    var ch = store("progress").chapters || {}, out = [], slug, sid, rd;
    for (slug in ch) {
      rd = (ch[slug] && ch[slug].read) || {};
      for (sid in rd) if (rd[sid] > 0) { out.push(slug); break; }
    }
    return out.sort();
  }

  function chapterSpec(slug, all) {
    return SAA.Content.data(slug).then(function (data) {
      var settings = store("settings"), route = (settings.routeBy && settings.routeBy[slug]) || settings.route || "pass";
      var list = ((data && data.questions) || []).filter(function (q) { return q.pool === "chapter"; });
      var worked, rest, map = {};
      if (!all && route !== "full") list = list.filter(function (q) { return q.worked || q.layer === "core"; });
      worked = list.filter(function (q) { return !!q.worked; });
      rest = list.filter(function (q) { return !q.worked; });
      if (all || route === "full") rest = rest.filter(function (q) { return q.layer === "core"; })
        .concat(rest.filter(function (q) { return q.layer !== "core"; }));
      list = worked.concat(rest);
      list.forEach(function (q) { map[q.id] = q; });
      return {
        kind: "chapter", ref: slug, title: "Quiz: " + QV.chapterTitle(slug),
        ids: list.map(function (q) { return q.id; }), loaded: { q: map, facts: (data && data.facts) || {} },
        empty: "This chapter has no practice questions yet. They appear when the chapter is ready.",
        back: "#ch." + slug
      };
    });
  }

  function drillSpec(id) {
    var doc = null, m = /^d([1-4])$/.exec(id || "");
    if (m) {
      return SAA.Content.drill("drill-" + id).then(function (file) {
        var map = {}, list = (file && file.questions) || [];
        list.forEach(function (q) { map[q.id] = q; });
        return {
          kind: "drill", ref: "drill-" + id, title: (file && file.title) || "Domain " + m[1] + " drill",
          ids: list.map(function (q) { return q.id; }), loaded: { q: map, facts: (file && file.facts) || {} },
          empty: "This drill is not written yet."
        };
      });
    }
    ((SAA.Store && SAA.Store.drills && SAA.Store.drills()) || []).forEach(function (d) { if (d && d.id === id) doc = d; });
    return Promise.resolve(doc ? drillDocSpec(doc) : { kind: "drill", ref: id, title: "Drill", ids: [], empty: "This drill is not stored on this device." });
  }

  /* A drill document written by Claude (5.2): ids of the book, or plain-text questions (DQ). */
  function drillDocSpec(doc) {
    var ids = [], dq = {};
    (doc.items || []).forEach(function (it) {
      if (typeof it === "string") { ids.push(it); return; }
      if (!Sc.validQuestion(it)) return;
      dq[it.id] = cleanDq(it);
      ids.push(it.id);
    });
    return { kind: "drill", ref: doc.id || null, title: typeof doc.title === "string" && doc.title ? doc.title : "Drill from Claude", ids: ids, dq: dq, empty: "This drill has no questions that can be shown." };
  }

  function cleanDq(it) {
    return {
      id: it.id, dq: 1, ch: null, sec: null, pool: "drill", d: it.d || 0, topics: [], type: it.type, select: it.select,
      stem: it.stem, kw: it.kw || [], opt: null, keyRev: null,
      options: it.options.map(function (o) { return { id: o.id, text: o.text, ok: o.ok === true, why: o.why || "" }; }),
      expl: it.expl || "", take: it.take || "", facts: []
    };
  }

  function retrySpec(words) {
    return SAA.Content.qindex().then(function (qi) {
      var stats = store("qstats"), rows, ids;
      if (!words) {
        return { kind: "retry", ref: null, title: "Retry my mistakes", ids: Sc.retryList(stats, qi),
          empty: "Your mistakes log is empty. Questions that you miss or mark as not sure appear here." };
      }
      rows = Sc.mistakes(stats, qi);
      ids = rows.filter(function (r) { return r.c === "W"; }).concat(rows.filter(function (r) { return r.c !== "W"; }))
        .slice(0, 10).map(function (r) { return r.id; });
      return { kind: "retry", ref: "w", title: "Ten stem-first questions", ids: ids, sf: 1,
        empty: "Your mistakes log is empty. Stem-first practice uses the questions that you missed." };
    });
  }

  function mixSpec() {
    return Promise.all([SAA.Content.manifest(), SAA.Content.qindex()]).then(function (r) {
      var ids = Sc.buildMix(r[1], store("qstats"), readSlugs(), (r[0] && r[0].order) || [], U.day());
      return { kind: "mix", ref: "d" + U.day(), title: "Daily mix", ids: ids,
        empty: "The daily mix uses chapters that you have read. Read a section first, then come back." };
    });
  }

  function specFor(name, args) {
    if (name === "quiz") return chapterSpec(args[0] || "", args[1] === "all");
    if (name === "drill") return drillSpec(args[0] || "");
    if (name === "retry") return retrySpec(args[0] === "w");
    return mixSpec();
  }

  /* ---------- the session ---------- */

  function load(spec) {
    var dq = spec.dq || {}, need;
    if (spec.loaded) return Promise.resolve(spec.loaded);
    need = spec.ids.filter(function (id) { return !dq[id]; });
    if (!need.length) return Promise.resolve({ q: {}, facts: {} });
    return SAA.Content.questions(need);
  }

  function newSession(spec, name, key, found) {
    return {
      v: 1, id: U.uid("a"), view: name, key: key, kind: spec.kind, ref: spec.ref == null ? null : spec.ref,
      title: spec.title || "Quiz", ids: found, dq: spec.dq || {}, sf: spec.sf ? 1 : 0, back: spec.back || null,
      i: 0, startedAt: U.now(), activeMs: 0, states: {}, answers: {}, done: 0
    };
  }

  function stemFirst(sess, q) {
    var s = store("settings"), limit = cfg().stemFirstCount;
    if (q.dq && !(q.kw && q.kw.length)) return false;
    if (sess.sf) return true;
    if (s.stemFirst === "on") return true;
    if (s.stemFirst === "off") return false;
    return (s.stemFirst == null || s.stemFirst === "auto") && typeof limit === "number" && (store("qstats").sf || 0) < limit;
  }

  function emptyPage(root, spec) {
    U.set(root, h`<div class="qz"><h1 tabindex="-1">${spec.title || "Quiz"}</h1>
      <p class="notice">${spec.empty || "There are no questions here yet."}</p>
      <p><a class="btn" href="${spec.back || "#home"}">${spec.back ? "Back to the chapter" : "Go to Today"}</a> <a class="btn quiet" href="#mistakes">Open the mistakes log</a></p></div>`);
  }

  function show(ctx) {
    var sess = live, root = ctx.root, id = sess.ids[sess.i], q = ctx.questions[id], state, qEl, startMs;
    if (!sess.states[id]) {
      sess.states[id] = { order: U.shuffle(q.options.map(function (o) { return o.id; })), picked: [], unsure: 0, checked: false, stage: null };
    }
    state = sess.states[id];
    U.set(root, h`<div class="qz">
      <h1 tabindex="-1">${sess.title}</h1>
      <p class="qz-prog"><span class="mono">Answered ${Object.keys(sess.answers).length} of ${sess.ids.length}</span>
        <progress class="qz-bar" max="${sess.ids.length}" value="${Object.keys(sess.answers).length}" aria-label="Questions answered"></progress></p>
      <div class="qz-q"></div>
    </div>`);
    qEl = root.querySelector(".qz-q");
    startMs = U.nowMs();
    function draw(focus) {
      QV.render(qEl, q, state, {
        mode: "learn", stemFirst: !state.checked && stemFirst(sess, q), n: sess.i + 1, of: sess.ids.length,
        last: sess.i === sess.ids.length - 1, facts: ctx.facts, focus: focus || null,
        onChange: function () {},
        onCheck: function () {
          var n, t = root.querySelector(".qz-prog .mono"), bar = root.querySelector(".qz-bar");
          check(ctx, q, state, U.nowMs() - startMs);
          n = Object.keys(sess.answers).length;
          if (t) t.textContent = "Answered " + n + " of " + sess.ids.length;
          if (bar) bar.value = n;
          draw(); focusVerdict(qEl);
        },
        onNav: function (delta) { if (delta > 0 && state.checked) next(ctx); }
      });
    }
    draw();
  }

  function focusVerdict(qEl) {
    var b = qEl.querySelector("[data-act=\"q-next\"]");
    if (b) { try { b.focus({ preventScroll: true }); } catch (e) { b.focus(); } }
  }

  function check(ctx, q, state, ms) {
    var sess = live, ok = Sc.isCorrect(q, state.picked), stats = store("qstats"), old, patch;
    if (state.checked) return;
    state.checked = true;
    ms = Math.max(0, Math.min(ms || 0, 3600000));
    sess.activeMs += ms;
    sess.answers[q.id] = { p: state.picked.slice(), u: state.unsure ? 1 : 0, ms: ms };
    if (!q.dq && SAA.Store) {
      old = (stats.q && stats.q[q.id]) || null;
      patch = { q: {} };
      patch.q[q.id] = Sc.record(old, q, state.picked, ok, !!state.unsure, U.now());
      if (state.sfDone) patch.sf = (stats.sf || 0) + 1;
      SAA.Store.patch("qstats", patch);
    }
    SAA.bus.emit("answer", { qid: q.id, ok: ok, unsure: !!state.unsure, kind: sess.kind });
    U.announce(ok ? "Correct." : "Wrong. The correct answer is marked.");
  }

  function next(ctx) {
    var sess = live, h1;
    if (!sess) return;
    if (sess.i >= sess.ids.length - 1) { finish(ctx); return; }
    sess.i++;
    show(ctx);
    try { globalThis.scrollTo(0, 0); } catch (e) { /* no window */ }
    h1 = ctx.root.querySelector("h1");
    U.announce("Question " + (sess.i + 1) + " of " + sess.ids.length);
    if (h1) { try { h1.focus({ preventScroll: true }); } catch (e2) { /* older engines */ } }
  }

  function finish(ctx) {
    var sess = live, list, first, doc;
    if (!sess || sess.done) return;
    sess.done = 1;
    list = sess.ids.map(function (id) { return ctx.questions[id]; });
    first = !((SAA.Store && SAA.Store.attempts()) || []).some(function (a) { return a.kind === sess.kind && a.ref === sess.ref; });
    doc = Sc.scoreAttempt(list, sess.answers, {
      id: sess.id, kind: sess.kind, ref: sess.ref, startedAt: sess.startedAt, submittedAt: U.now(),
      activeSec: Math.round(sess.activeMs / 1000), limitSec: null, build: (SAA.state && SAA.state.build) || null,
      over: 0, first: first, order: sess.ids
    });
    live = null;
    if (SAA.Store) SAA.Store.addAttempt(doc);
    if (SAA.Router) SAA.Router.go("#attempt." + doc.id, { replace: true });
    return doc;
  }

  /* Runs a spec inside `root`. `name` and `key` say which view owns the session. */
  function run(spec, root, name, key) {
    var resume = live && !live.done && live.view === name && live.key === key && !spec.explicit;
    var use = resume ? { ids: live.ids, dq: live.dq, loaded: spec.loaded && sameIds(spec.ids, live.ids) ? spec.loaded : null } : spec;
    return load(use).then(function (res) {
      var questions = {}, found, dq = use.dq || {}, ctx;
      use.ids.forEach(function (id) {
        if (dq[id]) questions[id] = dq[id];
        else if (res.q && res.q[id]) questions[id] = res.q[id];
      });
      found = use.ids.filter(function (id) { return !!questions[id]; });
      if (!found.length) { if (resume) live = null; emptyPage(root, spec); return null; }
      if (resume) {
        live.ids = found;
        if (live.i >= found.length) live.i = found.length - 1;
      } else {
        live = newSession(spec, name, key, found);
      }
      ctx = { name: name, key: key, root: root, questions: questions, facts: res.facts || {} };
      here = ctx;
      show(ctx);
      return ctx;
    });
  }

  function sameIds(a, b) {
    var sa = (a || []).slice().sort().join(","), sb = (b || []).slice().sort().join(",");
    return sa === sb;
  }

  /* ---------- views ---------- */

  function makeView(name) {
    return {
      mount: function (el, args, ctx) {
        var key = args.join("."), root = QV.root(el, "pv"), spec = null, hot = ctx && ctx.hot && ctx.hot.sess;
        if (pending && pending.view === name && pending.key === key) spec = pending.spec;
        pending = null;
        if (!spec && hot && hot.v === 1 && hot.view === name && hot.key === key && !hot.done) live = hot;
        return (spec ? Promise.resolve(spec) : specFor(name, args)).then(function (s) { return run(s, root, name, key); });
      },
      unmount: function () { here = null; },
      title: function (args) {
        if (live && live.view === name && live.key === args.join(".")) return live.title;
        if (name === "quiz") return "Quiz: " + QV.chapterTitle(args[0] || "");
        if (name === "drill") return "Drill";
        if (name === "retry") return args[0] === "w" ? "Ten stem-first questions" : "Retry my mistakes";
        return "Daily mix";
      },
      snapshot: function () {
        return here && live && live.view === here.name && live.key === here.key ? { sess: U.clone(live) } : null;
      }
    };
  }

  /* Quiz.start({kind, ref, ids, title}): opens the view of that kind with exactly these questions.
     Extra spec fields: sf (force stem-first), dq (map of plain-text questions), doc (a drill document). */
  function start(spec) {
    var name, key, s;
    spec = spec || {};
    s = spec.doc ? drillDocSpec(spec.doc) : {
      kind: spec.kind || "retry", ref: spec.ref == null ? null : spec.ref, title: spec.title || "Quiz",
      ids: (spec.ids || []).slice(), dq: spec.dq || null, sf: spec.sf ? 1 : 0
    };
    s.explicit = 1;
    name = ROUTE[s.kind] || "retry";
    if (name === "quiz") key = String(s.ref || "");
    else if (name === "drill") key = String(s.ref || "x").replace(/^drill-/, "");
    else if (name === "retry") key = "x";
    else key = "";
    pending = { view: name, key: key, spec: s };
    if (SAA.Router) return SAA.Router.go("#" + name + (key ? "." + key : ""), { force: true });
    return Promise.resolve();
  }

  /* ---------- reader mounts ---------- */

  function quizMount(el, id, ctx) {
    var slug = ctx.slug, meta = ctx.meta || {}, counts = meta.counts || {}, last = null, mock = null, manifest = SAA.state && SAA.state.manifest;
    ((SAA.Store && SAA.Store.attempts()) || []).forEach(function (a) { if (!last && a.kind === "chapter" && a.ref === slug) last = a; });
    if (meta.tier === "mock") {
      ((manifest && manifest.mocks) || []).forEach(function (m) { if (m.slug === slug) mock = m; });
      U.set(el, mock
        ? h`<div class="qz-card"><p>${mock.count} questions, timed. No feedback until you submit.</p><p><a class="btn primary" href="${"#mock." + mock.n}">Open ${mock.title}</a></p></div>`
        : h`<div class="qz-card"><p class="notice">This mock exam is not written yet.</p></div>`);
      return undefined;
    }
    if (!counts.q) {
      U.set(el, h`<div class="qz-card"><p class="notice">Practice questions appear when the chapter is ready.</p></div>`);
      return undefined;
    }
    U.set(el, h`<div class="qz-card">
      <p>${counts.q} ${counts.q === 1 ? "question" : "questions"}${counts.core != null ? h`: <span class="mono">${counts.core}</span> core, <span class="mono">${Math.max(0, counts.q - counts.core)}</span> extended` : null}. Each one shows why every option is right or wrong.</p>
      ${last ? h`<p>Last result: <a class="xr" href="${"#attempt." + last.id}">${last.pct}% on ${QV.fmtDate(last.submittedAt)}</a></p>` : null}
      <p class="qz-btns"><a class="btn primary" href="${"#quiz." + slug}">Core questions</a> <a class="btn" href="${"#quiz." + slug + ".all"}">All questions</a> <a class="btn quiet" href="${"#cards." + slug}">Quick cards</a></p>
    </div>`);
    return undefined;
  }

  /* Up to three questions from earlier chapters, at the top of the fast part (P1). */
  function returnMount(el, id, ctx) {
    var alive = true, slug = ctx.slug;
    el.hidden = true;
    if (!SAA.Content) return undefined;
    Promise.all([SAA.Content.manifest(), SAA.Content.qindex()]).then(function (r) {
      var order = (r[0] && r[0].order) || [], at = order.indexOf(slug), read = readSlugs(), ids, k, back = [1, 3, 6];
      if (!alive || at < 0) return null;
      for (k = 0; k < back.length; k++) if (!order[at - back[k]] || read.indexOf(order[at - back[k]]) < 0) return null;
      ids = Sc.returnQuestions(slug, order, r[1], store("qstats"), 3);
      if (ids.length < 3) return null;
      return SAA.Content.questions(ids).then(function (res) {
        var list = ids.map(function (x) { return res.q[x]; }).filter(Boolean), i = 0, right = 0, qEl;
        if (!alive || list.length < 3) return;
        U.set(el, h`<div class="qz-ret"><p class="eyebrow">Before you start: three questions from earlier chapters</p><div class="qz-q"></div></div>`);
        qEl = el.querySelector(".qz-q");
        el.hidden = false;
        function one() {
          var q = list[i], state = { order: U.shuffle(q.options.map(function (o) { return o.id; })), picked: [], unsure: 0, checked: false, stage: "opts" };
          function draw() {
            QV.render(qEl, q, state, {
              mode: "learn", stemFirst: false, keys: false, n: i + 1, of: list.length, last: i === list.length - 1, facts: res.facts,
              onCheck: function () {
                var ok = Sc.isCorrect(q, state.picked), stats = store("qstats"), patch = { q: {} };
                state.checked = true;
                if (ok) right++;
                patch.q[q.id] = Sc.record((stats.q && stats.q[q.id]) || null, q, state.picked, ok, !!state.unsure, U.now());
                if (SAA.Store) SAA.Store.patch("qstats", patch);
                SAA.bus.emit("answer", { qid: q.id, ok: ok, unsure: !!state.unsure, kind: "return" });
                draw();
              },
              onNav: function (d) {
                if (d < 0 || !state.checked) return;
                i++;
                if (i < list.length) one();
                else U.set(qEl, h`<p role="status">Done: ${right} of ${list.length} correct. Missed questions are in your <a class="xr" href="#mistakes">mistakes log</a>.</p>`);
              }
            });
          }
          draw();
        }
        one();
      });
    }).catch(function () { el.hidden = true; });
    return function () { alive = false; };
  }

  /* ---------- screenshots (preview only) ---------- */

  function firstChapter() {
    return SAA.Content.manifest().then(function (m) {
      var hit = null;
      (m.chapters || []).forEach(function (c) { if (!hit && c.status !== "planned" && c.counts && c.counts.q > 0) hit = c; });
      return hit ? chapterSpec(hit.slug, true) : null;
    });
  }

  function shot(mode) {
    return function (el) {
      if (SAA.Store && SAA.Store.reset) SAA.Store.reset();
      live = null;
      return firstChapter().then(function (spec) {
        var root = QV.root(el, "pv");
        if (!spec) { emptyPage(root, { title: "Quiz" }); return null; }
        spec.explicit = 1;
        spec.sf = mode === "stemfirst" ? 1 : 0;
        if (mode !== "stemfirst") spec.noSf = 1;
        return run(spec, root, "quiz", spec.ref).then(function (ctx) {
          var q, state, wrong;
          if (!ctx) return;
          q = ctx.questions[live.ids[0]];
          state = live.states[q.id];
          if (mode !== "stemfirst") { state.stage = "opts"; state.sfDone = 0; }
          if (mode === "checked") {
            wrong = q.options.filter(function (o) { return !o.ok; })[0];
            state.picked = [wrong.id];
            check(ctx, q, state, 42000);
          }
          show(ctx);
        });
      });
    };
  }

  SAA.Quiz = { start: start };

  if (SAA.Router) ["quiz", "drill", "retry", "mix"].forEach(function (name) { SAA.Router.register(name, makeView(name)); });
  if (SAA.Reader && SAA.Reader.registerMount) {
    SAA.Reader.registerMount("quiz", quizMount);
    SAA.Reader.registerMount("return", returnMount);
  }
  if (SAA.Test && SAA.Test.register) {
    SAA.Test.register("quiz-open", shot("open"));
    SAA.Test.register("quiz-stemfirst", shot("stemfirst"));
    SAA.Test.register("quiz-checked", shot("checked"));
  }
})(globalThis.SAA = globalThis.SAA || {});
