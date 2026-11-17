/* selftest.js (owner C, preview builds only): the test routes of ARCHITECTURE.md section 9.2.
   #t.render-all, #t.exam-sim, #t.hot, #t.shot.<name>. Each test writes its result into
   <pre id="saa-selftest"> as its last step: "SELFTEST PASS n/n name" or "SELFTEST FAIL ok/n name". */
(function (SAA) {
  "use strict";

  var U = SAA.U, h = U.h;
  var SYN = { "do": "tasks", say: "speak", quiz: "quiz", sources: "sources" };
  var VIEWS = ["home", "ch", "quiz", "drill", "retry", "mix", "mock", "attempt", "mistakes", "cards", "speak",
    "glossary", "fact", "plan", "progress", "files", "about", "toc"];
  var BAD_TEXT = ["undefined", "[object Object]", "](", "<" + "!--"];
  var LETTER_REF = /\b(?:options?|answers?|choices?)\s+\(?[A-F]\)?(?![\w'-])/;
  var T0 = 1791000000000;

  var hotPhase = null;   // set before the republish of #t.hot, so that the snapshot carries the first results
  var busy = false;

  /* ---------- result collector ---------- */

  function tester(name) {
    return {
      name: name, n: 0, pass: 0, skipped: 0, fails: [], notes: [],
      ok: function (cond, message) {
        this.n++;
        if (cond) { this.pass++; return true; }
        if (this.fails.length < 60) this.fails.push(String(message || "failed"));
        return false;
      },
      eq: function (a, b, message) {
        var x = JSON.stringify(a), y = JSON.stringify(b);
        return this.ok(x === y, (message || "value") + ": got " + clip(x) + ", expected " + clip(y));
      },
      skip: function (what) { this.skipped++; if (this.notes.indexOf("skipped: " + what) < 0) this.notes.push("skipped: " + what); },
      note: function (text) { this.notes.push(text); }
    };
  }

  function clip(s) { s = String(s); return s.length > 160 ? s.slice(0, 160) + "…" : s; }

  function report(T) {
    var pre = document.getElementById("saa-selftest"), host = document.getElementById("saa") || document.body, lines = [];
    if (!pre) { pre = document.createElement("pre"); pre.id = "saa-selftest"; pre.className = "selftest"; host.appendChild(pre); }
    lines.push("SELFTEST " + (T.fails.length ? "FAIL" : "PASS") + " " + T.pass + "/" + T.n + " " + T.name);
    T.fails.forEach(function (f) { lines.push("  " + f); });
    if (T.skipped) lines.push("skipped " + T.skipped);
    T.notes.forEach(function (x) { lines.push("note: " + x); });
    pre.textContent = lines.join("\n");
    busy = false;
  }

  function sleep(ms) { return new Promise(function (resolve) { setTimeout(resolve, ms); }); }

  function until(fn, tries) {
    var left = tries || 40;
    function step() {
      var v = null;
      try { v = fn(); } catch (e) { v = null; }
      if (v || left-- <= 0) return Promise.resolve(v);
      return sleep(25).then(step);
    }
    return step();
  }

  function resetAll() {
    try { if (globalThis.claude && globalThis.claude.__stub) globalThis.claude.__stub.reset(); } catch (e) { /* no stub */ }
    if (SAA.Store && SAA.Store.reset) SAA.Store.reset();
  }

  function stubDb() {
    var s = globalThis.claude && globalThis.claude.__stub;
    return s && s.db ? s.db : null;
  }

  /* ---------- #t.render-all ---------- */

  function textProblems(el) {
    var out = [], walker = document.createTreeWalker(el, 4, null), node, text, i;
    while ((node = walker.nextNode())) {
      text = node.nodeValue || "";
      if (!text.trim()) continue;
      if (node.parentElement && node.parentElement.closest("pre, code, textarea, script, style")) continue;
      for (i = 0; i < BAD_TEXT.length; i++) if (text.indexOf(BAD_TEXT[i]) >= 0) out.push(BAD_TEXT[i] + " in \"" + clip(text.trim()).slice(0, 60) + "\"");
      if (out.length > 3) break;
    }
    return out;
  }

  function phone() { return (globalThis.innerWidth || 1280) < 760; }

  function widthProblem(el) {
    var doc = document.documentElement, all, i, w = doc.clientWidth, r;
    if (doc.scrollWidth > w) return "the page scrolls sideways (" + doc.scrollWidth + " > " + w + ")";
    all = el.querySelectorAll("*");
    for (i = 0; i < all.length; i++) {
      r = all[i].getBoundingClientRect();
      if (r.width > w + 0.5 && !all[i].closest(".tw, .code pre, .fig-s, .zoom")) {
        return "wider than the screen: " + all[i].tagName.toLowerCase() + (all[i].className && typeof all[i].className === "string" ? "." + all[i].className.split(" ").join(".") : "");
      }
    }
    return tableProblem(el);
  }

  /* A table that hides columns on the phone must have at least four columns and the edge shade of .tw. */
  function tableProblem(el) {
    var list = el.querySelectorAll(".tw"), i, tw, row, cols, bg;
    for (i = 0; i < list.length; i++) {
      tw = list[i];
      if (tw.scrollWidth <= tw.clientWidth + 1) continue;
      row = tw.querySelector("tr");
      cols = row ? row.children.length : 0;
      if (cols < 4) return "a table of " + cols + " columns hides a column on the phone: " + (tw.getAttribute("aria-label") || "table");
      bg = "";
      try { bg = globalThis.getComputedStyle(tw).backgroundImage || ""; } catch (e) { bg = ""; }
      if (bg.indexOf("gradient") < 0) return "a table scrolls sideways without the edge shade: " + (tw.getAttribute("aria-label") || "table");
    }
    return null;
  }

  function checkLinks(T, el, where, facts, manifest, part) {
    var list = el.querySelectorAll("a.ev"), i, id, route, row, href, slug;
    for (i = 0; i < list.length; i++) {
      id = list[i].getAttribute("data-fact");
      T.ok(!!(facts && facts[id]), where + ": evidence chip without a fact: " + id);
    }
    list = el.querySelectorAll("a.xr");
    for (i = 0; i < list.length; i++) {
      href = list[i].getAttribute("href") || "";
      route = SAA.Router.parse(href);
      if (route.view === "ch") {
        slug = route.args[0];
        if (!T.ok(!!SAA.Content.meta(slug), where + ": link to an unknown chapter: " + href)) continue;
        if (route.args[2] && !SYN[route.args[1]]) {
          row = SAA.Content.section(slug, route.args[2]);
          T.ok(!!row, where + ": link to an unknown section: " + href);
        }
      } else {
        T.ok(VIEWS.indexOf(route.view) >= 0 || !!(manifest.aliases && manifest.aliases[route.view]), where + ": link to an unknown page: " + href);
      }
    }
    list = el.querySelectorAll(".mount[data-mount]");
    for (i = 0; i < list.length; i++) {
      id = list[i].getAttribute("data-mount");
      T.ok(!SAA.Reader || !SAA.Reader.hasMount || SAA.Reader.hasMount(id), where + ": mount without a renderer: " + id);
    }
    void part;
  }

  function checkMounted(T, el, where, facts, manifest) {
    var probs = textProblems(el), w;
    T.ok(!probs.length, where + ": bad text: " + probs.join("; "));
    checkLinks(T, el, where, facts, manifest);
    if (phone()) {
      w = widthProblem(el);
      T.ok(!w, where + ": " + w);
    }
  }

  function plain(htmlText) {
    var d = document.createElement("div");
    U.set(d, U.raw(htmlText || ""));
    return d.textContent || "";
  }

  function checkQuestion(T, work, q, facts, manifest, where) {
    var state, okN = 0, i, o, body;
    where = where + " " + q.id;
    T.ok(Array.isArray(q.options) && q.options.length >= 4 && q.options.length <= 6, where + ": option count " + (q.options || []).length);
    for (i = 0; i < q.options.length; i++) {
      o = q.options[i];
      if (o.ok === true) okN++;
      T.ok(typeof o.why_h === "string" && plain(o.why_h).trim().length > 0, where + ": option " + o.id + " has no explanation");
      T.ok(!LETTER_REF.test(plain(o.why_h)), where + ": option " + o.id + " refers to a letter");
    }
    T.eq(okN, q.select, where + ": correct options");
    body = plain(q.expl_h) + " " + plain(q.take_h) + " " + plain(q.twin_h);
    T.ok(!LETTER_REF.test(body), where + ": the explanation refers to a letter");
    T.ok(plain(q.expl_h).trim().length > 0, where + ": no explanation");
    if (!SAA.QView) { T.skip("QView"); return; }
    try {
      state = { order: q.options.map(function (x) { return x.id; }), picked: [], unsure: 0, checked: false, stage: "opts" };
      SAA.QView.render(work, q, state, { mode: "learn", stemFirst: false, keys: false, n: 1, of: 1, facts: facts });
      T.eq(work.querySelectorAll(".q-opts .opt").length, q.options.length, where + ": rendered options");
      T.eq(work.querySelectorAll(".q-opts input").length, q.options.length, where + ": rendered inputs");
      checkMounted(T, work, where + " (open)", facts, manifest);
      state.stage = "sf";
      SAA.QView.render(work, q, state, { mode: "learn", stemFirst: true, keys: false, n: 1, of: 1, facts: facts });
      T.ok(!!work.querySelector(".q-sf"), where + ": no stem-first panel");
      if (phone()) checkMounted(T, work, where + " (stem first)", facts, manifest);
      state.stage = "opts";
      state.picked = [q.options.filter(function (x) { return !x.ok; })[0].id];
      state.unsure = 1;
      state.checked = true;
      SAA.QView.render(work, q, state, { mode: "learn", stemFirst: false, keys: false, n: 1, of: 1, facts: facts });
      T.ok(work.querySelectorAll(".opt-why").length === q.options.length, where + ": not every option shows its explanation");
      T.ok(work.querySelectorAll(".opt.ok").length === q.select, where + ": marked correct options");
      T.ok(!!work.querySelector(".q-cause"), where + ": no cause buttons after a wrong answer");
      checkMounted(T, work, where + " (checked)", facts, manifest);
      SAA.QView.review(work, q, { p: state.picked, ok: 0, u: 1, ms: 1 }, { n: 1, cause: true, facts: facts });
      T.eq(work.querySelectorAll(".q-opts .opt").length, q.options.length, where + ": reviewed options");
      T.eq(work.querySelectorAll("input, select, textarea, [id]").length, 0, where + ": the review form holds a form control or an id");
      checkMounted(T, work, where + " (review)", facts, manifest);
    } catch (e) {
      T.ok(false, where + ": threw " + (e && e.message ? e.message : e));
    }
    work.textContent = "";
  }

  /* Every shard of facts-index.json loads with its count and holds only ids that resolve to it; every fact
     of the chapter files (`seen`) is found again through Content.fact, the path of the evidence view. */
  function factShards(T, seen) {
    var C = SAA.Content;
    if (!C.factsIndex || !C.factShard || !C.fact || !C.factService) { T.skip("Content.fact"); return Promise.resolve(); }
    return C.factsIndex().then(function (index) {
      var shards = (index && index.shards) || {}, chain = Promise.resolve();
      T.ok(!!index, "facts-index.json could not be loaded");
      Object.keys(shards).forEach(function (svc) {
        chain = chain.then(function () { return C.factShard(svc); }).then(function (shard) {
          var ids = Object.keys((shard && shard.facts) || {});
          var wrong = ids.filter(function (id) { return C.factService(id, index) !== svc; });
          T.eq(ids.length, shards[svc].count, shards[svc].path + ": fact count of the index");
          T.ok(!wrong.length, shards[svc].path + ": ids that resolve to another shard: " + wrong.slice(0, 3).join(", "));
        });
      });
      Object.keys(seen).forEach(function (id) {
        chain = chain.then(function () { return C.fact(id); }).then(function (f) {
          T.ok(!!f && f.claim === seen[id].claim, id + ": the evidence view does not find this fact in its shard");
        });
      });
      return chain;
    });
  }

  function renderAll(root) {
    var T = tester("render-all"), work = document.createElement("div"), manifest, seen = {};
    resetAll();
    root.appendChild(work);

    function fresh() { work.textContent = ""; work.className = "selftest-work"; work.hidden = false; return work; }

    function chapter(meta) {
      var slug = meta.slug;
      return Promise.all([SAA.Content.chapter(slug), SAA.Content.data(slug)]).then(function (r) {
        var c = r[0], d = r[1], facts = {}, ctx, files = meta.files || [], chain = Promise.resolve();
        Object.keys((c && c.facts) || {}).forEach(function (k) { facts[k] = c.facts[k]; });
        Object.keys((d && d.facts) || {}).forEach(function (k) { facts[k] = d.facts[k]; });
        Object.keys(facts).forEach(function (k) { seen[k] = facts[k]; });
        T.ok(!!c, slug + ": the chapter file is missing");
        if (!c) return null;
        files.forEach(function (f) {
          chain = chain.then(function () {
            var key = f.key, md = c.parts && c.parts[key], el = fresh(), cleanup = null, where = slug + "/" + key, m;
            ctx = { slug: slug, part: key, meta: meta, chapter: c, route: "full", hot: null, data: function () { return Promise.resolve(d); } };
            if (!SAA.Reader) { T.skip("Reader"); return null; }
            try {
              if (md && typeof md.html === "string") cleanup = SAA.Reader.mountHtml(el, U.raw(md.html), facts, ctx);
              else if (SYN[key]) {
                if (!SAA.Reader.hasMount(SYN[key])) { T.skip("mount " + SYN[key]); return null; }
                U.set(el, h`<div class="mount" data-mount="${SYN[key]}" data-id=""></div>`);
                m = el.firstElementChild;
                cleanup = SAA.Reader.runMount(SYN[key], m, "", ctx);
              } else { T.ok(false, where + ": the part has no content"); return null; }
            } catch (e) { T.ok(false, where + ": threw " + (e && e.message ? e.message : e)); return null; }
            return sleep(0).then(function () {
              T.ok((el.textContent || "").trim().length > 0 || key === "do", where + ": rendered nothing");
              checkMounted(T, el, where, facts, manifest);
              try { if (typeof cleanup === "function") cleanup(); } catch (e2) { T.ok(false, where + ": cleanup threw"); }
            });
          });
        });
        return chain.then(function () {
          var el;
          ((d && d.questions) || []).forEach(function (q) { checkQuestion(T, fresh(), q, facts, manifest, slug); });
          ((d && d.cards) || []).forEach(function (card) {
            if (!SAA.Cards) { T.skip("Cards"); return; }
            el = fresh();
            try {
              T.ok(typeof card.front === "string" && card.front.trim().length > 0, slug + " " + card.id + ": empty front");
              SAA.Cards.render(el, card, { flipped: false, facts: facts });
              T.ok((el.textContent || "").trim().length > 0, slug + " " + card.id + ": the front renders nothing");
              SAA.Cards.render(el, card, { flipped: true, facts: facts });
              T.ok(!!el.querySelector(".fc-back .fc-a"), slug + " " + card.id + ": the back has no answer");
              checkMounted(T, el, slug + " " + card.id, facts, manifest);
            } catch (e) { T.ok(false, slug + " " + card.id + ": threw " + (e && e.message ? e.message : e)); }
          });
          ((d && d.speak) || []).forEach(function (item) {
            var stop = null;
            if (!SAA.Speak || !SAA.Speak.render) { T.skip("Speak"); return; }
            el = fresh();
            try {
              T.ok(typeof item.prompt === "string" && item.prompt.trim().length > 0, slug + " " + item.id + ": empty prompt");
              stop = SAA.Speak.render(el, item, { facts: facts, step: 1 });
              T.ok((el.textContent || "").trim().length > 0, slug + " " + item.id + ": renders nothing");
              checkMounted(T, el, slug + " " + item.id, facts, manifest);
              if (typeof stop === "function") stop();
            } catch (e) { T.ok(false, slug + " " + item.id + ": threw " + (e && e.message ? e.message : e)); }
          });
          ((d && d.tasks) || []).forEach(function (task) {
            var stop = null;
            if (!SAA.Reader || !SAA.Reader.hasMount("task")) { T.skip("mount task"); return; }
            el = fresh();
            try {
              T.ok(typeof task.title === "string" && task.title.trim().length > 0, slug + " " + task.id + ": empty title");
              stop = SAA.Reader.runMount("task", el, task.id, { slug: slug, part: "do", meta: meta, chapter: c, route: "full", hot: null, data: function () { return Promise.resolve(d); } });
              if (typeof stop === "function") stop();
            } catch (e) { T.ok(false, slug + " " + task.id + ": threw " + (e && e.message ? e.message : e)); }
          });
          fresh();
        });
      });
    }

    function bank(file, where) {
      T.ok(!!file && Array.isArray(file.questions) && file.questions.length > 0, where + ": no questions");
      ((file && file.questions) || []).forEach(function (q) { checkQuestion(T, fresh(), q, (file && file.facts) || {}, manifest, where); });
    }

    return SAA.Content.manifest().then(function (m) {
      var chain = Promise.resolve();
      manifest = m;
      (m.chapters || []).forEach(function (meta) {
        if (meta.status === "planned") return;
        chain = chain.then(function () { return chapter(meta); });
      });
      (m.mocks || []).forEach(function (x) {
        chain = chain.then(function () { return SAA.Content.mock(x.slug); }).then(function (file) {
          bank(file, x.slug);
          T.eq(((file && file.questions) || []).length, x.count, x.slug + ": question count of the manifest");
        });
      });
      (m.drills || []).forEach(function (x) {
        chain = chain.then(function () { return SAA.Content.drill(x.id); }).then(function (file) { bank(file, x.id); });
      });
      return chain.then(function () { return factShards(T, seen); });
    }).then(function () {
      work.remove();
      U.set(root, h`<h1 tabindex="-1">Self test: render all</h1>`);
      report(T);
    }, function (e) {
      T.ok(false, "stopped: " + (e && e.path ? "could not load " + e.path : (e && e.message ? e.message : e)));
      report(T);
    });
  }

  /* ---------- #t.exam-sim ---------- */

  function clickId(id) {
    var el = document.getElementById(id);
    if (el) el.click();
    return !!el;
  }

  /* Drives one mock through the real Exam code. `script(q, i)` returns {p: [ids]|null, u: 0|1}. */
  function drive(T, entry, file, script, clock) {
    var x, byId = {};
    (file.questions || []).forEach(function (q) { byId[q.id] = q; });
    return SAA.Router.go("#mock." + entry.n, { force: true }).then(function () {
      return SAA.Exam.start();
    }).then(function () {
      x = SAA.Exam.doc();
      if (!T.ok(!!x && x.phase === "run" && x.ref === entry.slug, "the exam did not start")) return null;
      T.eq(x.order.length, file.questions.length, "questions in the exam order");
      T.eq(x.limitSec, file.minutes * 60, "time limit from the mock file");
      x.order.forEach(function (id, i) {
        var q = byId[id], plan = script(q, i, x.order), live;
        if (i > 0) SAA.Exam.go(i);
        clock.t += 20000;
        SAA.Exam.tick();
        if (plan.p) plan.p.forEach(function (oid) { T.ok(clickId("q-" + id + "-o-" + oid), "no input for " + id + " option " + oid); });
        if (plan.u) T.ok(clickId("q-" + id + "-unsure"), "no not-sure box for " + id);
        live = SAA.Exam.doc();
        if (plan.p) T.eq(((live.ans[id] || {}).p || []).slice().sort(), plan.p.slice().sort(), "stored answer of " + id);
      });
      return x;
    });
  }

  function simScript(file) {
    /* all correct in domain 1, all wrong in domain 2, the first half of domain 3 correct, domain 4 unanswered */
    return function (order) {
      var byId = {}, d3 = [], firstHalf = {}, marked = {}, n = 0;
      file.questions.forEach(function (q) { byId[q.id] = q; });
      order.forEach(function (id) { if (byId[id].d === 3) d3.push(id); });
      d3.slice(0, Math.floor(d3.length / 2)).forEach(function (id) { firstHalf[id] = 1; });
      order.forEach(function (id) { if (byId[id].d !== 4 && n < 5) { marked[id] = 1; n++; } });
      return function (q) {
        var right = SAA.Scoring.correctIds(q), wrong = q.options.filter(function (o) { return !o.ok; }).map(function (o) { return o.id; });
        var u = marked[q.id] ? 1 : 0;
        if (q.d === 1) return { p: right, u: u, ok: 1 };
        if (q.d === 2) return { p: wrong.slice(0, right.length), u: u, ok: 0 };
        if (q.d === 3) return firstHalf[q.id] ? { p: right, u: u, ok: 1 } : { p: wrong.slice(0, right.length), u: u, ok: 0 };
        return { p: null, u: 0, ok: 0 };
      };
    };
  }

  function examSim(root) {
    var T = tester("exam-sim"), clock = { t: T0 }, manifest, entry, file;
    void root;
    resetAll();
    SAA.Test.clock = function () { return clock.t; };

    function once(expectFirst) {
      var plans = {}, expect = { correct: 0, sure: 0, domains: { d1: { c: 0, n: 0 }, d2: { c: 0, n: 0 }, d3: { c: 0, n: 0 }, d4: { c: 0, n: 0 } } }, x, make = simScript(file), inner = null;
      return drive(T, entry, file, function (q, i, order) {
        var p;
        if (!inner) inner = make(order);
        p = inner(q);
        plans[q.id] = p;
        expect.domains["d" + q.d].n++;
        if (p.ok) { expect.correct++; expect.domains["d" + q.d].c++; if (!p.u) expect.sure++; }
        return p;
      }, clock).then(function (doc) {
        var btn;
        x = doc;
        if (!x) return null;
        T.eq(x.activeMs, 20000 * x.order.length, "active time on the timer");
        SAA.Exam.askSubmit(true);
        btn = document.querySelector("[data-act=\"ex-do\"]");
        if (!T.ok(!!btn, "no Submit button in the confirmation panel")) return null;
        btn.click();
        return sleep(0);
      }).then(function () {
        var a, stats, ex, total, ids, bad = 0, badU = 0;
        if (!x) return null;
        a = (SAA.Store.attempts() || [])[0];
        if (!T.ok(!!a && a.id === x.id, "the attempt was not stored")) return null;
        total = file.questions.length;
        T.eq(SAA.Router.current().hash, "#attempt." + x.id, "route after submit");
        T.eq([a.kind, a.ref, a.total], ["mock", entry.slug, total], "attempt kind, ref, total");
        T.eq(a.correct, expect.correct, "score");
        T.eq(a.pct, Math.round(100 * expect.correct / total), "percent");
        T.eq(a.sureCorrect, expect.sure, "sure and correct");
        T.eq(a.domains, expect.domains, "domain breakdown");
        T.eq(a.first, expectFirst, "first");
        T.eq(a.over, 0, "over");
        T.eq(a.activeSec, 20 * total, "active seconds");
        T.eq(a.order, x.order, "order");
        ex = SAA.Store.get("exam");
        T.ok(!ex || ex.none === 1 || ex.phase !== "run", "the exam document was not cleared");
        T.ok(!SAA.Exam.doc(), "Exam.doc() still returns a running exam");
        stats = SAA.Store.get("qstats").q || {};
        ids = Object.keys(plans);
        ids.forEach(function (id) {
          var rec = stats[id];
          if (!rec || rec.h.slice(-1) !== (plans[id].ok ? "1" : "0")) bad++;
          if (!rec || rec.u.slice(-1) !== (plans[id].u ? "1" : "0")) badU++;
        });
        T.eq(bad, 0, "question records with the wrong result");
        T.eq(badU, 0, "question records with the wrong not-sure flag");
        T.ok(!!document.querySelector("#saa-view .bigscore"), "the results page does not show the score");
        return until(function () { var c = SAA.Store.get("coach"); return c && c.overall && c.overall.mocks && c.overall.mocks.length ? c : null; }).then(function (c) {
          T.ok(!!c, "no coach document after the attempt");
          if (c) T.eq(c.overall.mocks[c.overall.mocks.length - 1], { ref: entry.slug, pct: a.pct }, "coach: last mock");
          if (!stubDb() || SAA.Store.status() !== "cloud") { T.skip("stub database (status " + SAA.Store.status() + ")"); return null; }
          return until(function () { return stubDb()["study/stub-user/attempts/" + a.id]; }).then(function (remote) {
            T.ok(!!remote, "the attempt is not in the stub database at study/stub-user/attempts/" + a.id);
            if (remote) T.eq([remote.correct, remote.total, remote.first], [a.correct, a.total, a.first], "attempt in the stub database");
          });
        });
      });
    }

    return SAA.Content.manifest().then(function (m) {
      manifest = m;
      entry = (m.mocks || [])[0];
      if (!entry) { T.note("no mock"); return null; }
      return SAA.Content.mock(entry.slug).then(function (f) {
        file = f;
        /* wait a moment for cloud sync of the stub, so that the database assert can run */
        return until(function () { return SAA.Store.status() === "cloud"; }, 20);
      }).then(function () { return once(1); }).then(function () { return once(0); });
    }).then(function () { report(T); }, function (e) {
      T.ok(false, "stopped: " + (e && e.path ? "could not load " + e.path : (e && e.message ? e.message : e)));
      report(T);
    });
  }

  /* ---------- #t.hot ---------- */

  function hotTest(root, ctx) {
    var T = tester("hot"), clock = { t: T0 }, entry, file, before = null, snap = null, prior = ctx && ctx.hot && ctx.hot.pass === 1 ? ctx.hot : null;
    void root;

    if (prior) {
      /* second pass, after the stub's republish reloaded the page */
      T.n = prior.n; T.pass = prior.ok; T.fails = prior.fails || [];
      var x2 = SAA.Exam ? SAA.Exam.doc() : null;
      T.ok(!!x2, "after the republish: no running exam");
      if (x2) {
        T.eq(x2.cur, prior.cur, "after the republish: cur");
        T.eq(x2.activeMs, prior.activeMs, "after the republish: activeMs");
        T.eq(Object.keys(x2.ans || {}).sort(), prior.ans, "after the republish: answered questions");
      }
      report(T);
      return Promise.resolve();
    }

    resetAll();
    SAA.Test.clock = function () { return clock.t; };
    return SAA.Content.manifest().then(function (m) {
      entry = (m.mocks || [])[0];
      if (!entry) { T.note("no mock"); return null; }
      if (!SAA.App || !SAA.App.snapshot) { T.skip("App.snapshot"); return null; }
      return SAA.Content.mock(entry.slug).then(function (f) {
        file = f;
        var n = 0;
        return drive(T, entry, { questions: f.questions, minutes: f.minutes }, function (q, i) {
          if (i >= 3) return { p: null, u: 0 };
          n++;
          return { p: SAA.Scoring.correctIds(q), u: i === 1 ? 1 : 0 };
        }, clock);
      }).then(function (x) {
        if (!x) return null;
        SAA.Exam.go(2);
        x = SAA.Exam.doc();
        snap = JSON.parse(JSON.stringify(SAA.App.snapshot()));
        before = { route: SAA.Router.current().hash, cur: x.cur, ans: U.clone(x.ans), activeMs: x.activeMs, id: x.id };
        T.eq(snap.v, 1, "snapshot version");
        T.eq(snap.route, "#mock." + entry.n, "snapshot route");
        T.ok(!!snap.store && !!snap.store.docs && !!snap.store.docs.exam, "the snapshot holds no exam document");
        T.ok(JSON.stringify(snap).length < 300000, "the snapshot is larger than 300 KB");
        /* clear everything, then start again from the snapshot */
        return SAA.Router.go("#about", { force: true }).then(function () {
          SAA.Store.reset();
          T.ok(!SAA.Exam.doc(), "the exam survived Store.reset()");
          SAA.Store.init(snap.store);
          /* read at once: with cloud sync on, the restored outbox is flushed a moment later */
          T.eq(Object.keys(SAA.Store.snapshot().outbox || {}).sort(), Object.keys(snap.store.outbox || {}).sort(), "restored outbox paths");
          return SAA.Router.start({ hash: snap.route, view: snap.view });
        }).then(function () { return sleep(0); }).then(function () {
          var y = SAA.Exam.doc();
          T.eq(SAA.Router.current().hash, before.route, "restored route");
          if (!T.ok(!!y, "no running exam after the restore")) return;
          T.eq(y.id, before.id, "restored exam id");
          T.eq(y.cur, before.cur, "restored cur");
          T.eq(y.ans, before.ans, "restored answers");
          T.eq(y.activeMs, before.activeMs, "restored activeMs");
          T.ok(SAA.Exam.running(), "the exam view is not running after the restore");
        });
      });
    }).then(function () {
      var stub = globalThis.claude && globalThis.claude.__stub, x = SAA.Exam ? SAA.Exam.doc() : null;
      if (stub && stub.mode === "hot" && typeof globalThis.__saaRepublish === "function" && x && !T.fails.length) {
        hotPhase = { pass: 1, n: T.n, ok: T.pass, fails: T.fails, cur: x.cur, activeMs: x.activeMs, ans: Object.keys(x.ans || {}).sort() };
        return SAA.Router.go("#t.hot", { force: true }).then(function () { globalThis.__saaRepublish(); });
      }
      report(T);
      return null;
    }, function (e) {
      T.ok(false, "stopped: " + (e && e.path ? "could not load " + e.path : (e && e.message ? e.message : e)));
      report(T);
    });
  }

  /* ---------- the view ---------- */

  var view = {
    mount: function (el, args, ctx) {
      var name = args[0] || "", root = document.createElement("div"), fn;
      el.textContent = "";
      el.appendChild(root);
      if (name === "shot") {
        fn = SAA.Test && SAA.Test.states ? SAA.Test.states[args[1]] : null;
        if (!fn) { U.set(root, h`<h1 tabindex="-1">Self test</h1><p class="notice">There is no screenshot state called "${args[1] || ""}".</p>`); return null; }
        return fn(root);
      }
      if (hotPhase) { U.set(root, h`<h1 tabindex="-1">Self test: hot</h1>`); return null; }
      if (busy) return null;
      U.set(root, h`<h1 tabindex="-1">Self test: ${name}</h1><p>Running…</p>`);
      busy = true;
      /* the tests leave this view (they open the mock), so they are not tied to the mount promise */
      if (name === "render-all") { renderAll(root); return null; }
      if (name === "exam-sim") { examSim(root); return null; }
      if (name === "hot") { hotTest(root, ctx); return null; }
      busy = false;
      U.set(root, h`<h1 tabindex="-1">Self test</h1><p class="notice">Unknown test. Use render-all, exam-sim, hot or shot.</p>`);
      return null;
    },
    title: function (args) { return "Self test " + (args[0] || ""); },
    snapshot: function () { return hotPhase; }
  };

  if (SAA.Router) SAA.Router.register("t", view);
})(globalThis.SAA = globalThis.SAA || {});
