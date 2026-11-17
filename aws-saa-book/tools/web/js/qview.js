/* qview.js (owner C): the question component, ARCHITECTURE.md section 7.2.
   QView.render draws the one interactive question; QView.review draws a checked question read-only. */
(function (SAA) {
  "use strict";

  var U = SAA.U, h = U.h;
  var LETTERS = ["A", "B", "C", "D", "E", "F"];
  var COUNT_WORD = { 2: "TWO", 3: "THREE", 4: "FOUR" };
  var CAUSE = {
    K: "Did not know",
    C: "Confused two things",
    W: "Missed a word",
    T: "Ran out of time",
    D: "Old limit in the question"
  };
  var CAUSE_ORDER = ["K", "C", "W", "T", "D"];
  var CHIPS = [["cost", "Cost"], ["ops", "Operational overhead"], ["perf", "Performance"],
    ["resil", "Resilience"], ["sec", "Security"], ["none", "Nothing special"]];

  var cur = null;        // the interactive question: {el, q, state, opts}
  var keysOn = false;

  /* ---------- helpers shared by the practice views ---------- */

  function secHref(sec) {
    if (!sec || !sec.slug) return null;
    return "#ch." + sec.slug + (sec.part ? "." + sec.part + (sec.sid ? "." + sec.sid : "") : "");
  }

  function secTitle(sec) {
    var row = null;
    try { row = sec && sec.sid && SAA.Content ? SAA.Content.section(sec.slug, sec.sid) : null; } catch (e) { row = null; }
    if (row && row.title) return row.title;
    try { row = SAA.Content ? SAA.Content.meta(sec.slug) : null; } catch (e2) { row = null; }
    return row && row.title ? row.title : "the section";
  }

  function chapterTitle(slug) {
    var m = null;
    try { m = SAA.Content ? SAA.Content.meta(slug) : null; } catch (e) { m = null; }
    return m && m.title ? m.title : slug;
  }

  function fmtDate(sec) {
    if (!sec) return "";
    try {
      return new Date(sec * 1000).toLocaleDateString("en-US", { year: "numeric", month: "short", day: "numeric" });
    } catch (e) { return ""; }
  }

  /* The line of ARCHITECTURE 3.2 for a failed load, with a Retry button. */
  function fail(el, retry) {
    U.set(el, h`<div class="notice" role="alert"><p>This page could not be loaded. Check your connection and try again.</p>
      <p><button type="button" class="btn" data-act="q-retry">Retry</button></p></div>`);
    if (retry && el.firstElementChild) U.on(el.firstElementChild, "click", "[data-act=\"q-retry\"]", function () { retry(); });
  }

  /* A fresh child of a view element. Listeners are bound to it, so they go when the view goes. */
  function root(el, cls) {
    var d = document.createElement("div");
    d.className = cls || "pv";
    el.textContent = "";
    el.appendChild(d);
    return d;
  }

  function rightIds(q) { return SAA.Scoring.correctIds(q); }

  function optionById(q, id) {
    for (var i = 0; i < q.options.length; i++) if (String(q.options[i].id) === String(id)) return q.options[i];
    return null;
  }

  /* An `_h` field is used only for a question that came from Content (never for a DQ, 5.2). */
  function rich(q, obj, name) {
    if (!q.dq && typeof obj[name + "_h"] === "string" && obj[name + "_h"]) return U.raw(obj[name + "_h"]);
    var plain = obj[name];
    return typeof plain === "string" && plain ? h`${plain}` : null;
  }

  /* ---------- the stem: deciding phrases and words ---------- */

  function kwRanges(stem, kw) {
    var low = String(stem).toLowerCase(), out = [], merged = [], i, k, at;
    kw = kw || [];
    for (i = 0; i < kw.length; i++) {
      k = String(kw[i] || "").toLowerCase().trim();
      if (!k) continue;
      at = low.indexOf(k);
      while (at >= 0) { out.push([at, at + k.length]); at = low.indexOf(k, at + k.length); }
    }
    out.sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; });
    for (i = 0; i < out.length; i++) {
      if (merged.length && out[i][0] <= merged[merged.length - 1][1]) {
        merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], out[i][1]);
      } else merged.push(out[i].slice());
    }
    return merged;
  }

  function stemMarked(stem, ranges) {
    var parts = [], at = 0, i;
    stem = String(stem);
    for (i = 0; i < ranges.length; i++) {
      if (ranges[i][0] > at) parts.push(h`${stem.slice(at, ranges[i][0])}`);
      parts.push(h`<mark class="q-kw">${stem.slice(ranges[i][0], ranges[i][1])}</mark>`);
      at = ranges[i][1];
    }
    if (at < stem.length) parts.push(h`${stem.slice(at)}`);
    return parts;
  }

  function stemWords(stem) {
    var out = [], re = /\S+/g, m;
    while ((m = re.exec(String(stem)))) out.push({ w: m[0], a: m.index, b: m.index + m[0].length });
    return out;
  }

  function wordHits(word, ranges) {
    for (var i = 0; i < ranges.length; i++) if (word.a < ranges[i][1] && word.b > ranges[i][0]) return true;
    return false;
  }

  function chipLabel(key) {
    for (var i = 0; i < CHIPS.length; i++) if (CHIPS[i][0] === key) return CHIPS[i][1];
    return "";
  }

  /* ---------- cause buttons and the repair line ---------- */

  function repair(q, code) {
    var sec = secHref(q.sec), atlas = null;
    if (code === "K" && sec) {
      return h`<a class="xr" href="${sec}">Read the section again: ${secTitle(q.sec)}</a>`;
    }
    if (code === "C") {
      try { atlas = SAA.Content ? SAA.Content.meta("decision-atlas") : null; } catch (e) { atlas = null; }
      if (atlas && atlas.status !== "planned") return h`<a class="xr" href="#ch.decision-atlas">Compare the two in the decision atlas</a>`;
      if (sec) return h`<a class="xr" href="${sec}">Read the section again: ${secTitle(q.sec)}</a>`;
    }
    if (code === "W") return h`<a class="xr" href="#retry.w">Practise ten stem-first questions</a>`;
    return h`Saved in your mistakes log.`;
  }

  function causePanel(q, chosen) {
    var buttons = CAUSE_ORDER.map(function (c) {
      return h`<button type="button" class="btn quiet" data-act="q-cause" data-q="${q.id}" data-c="${c}" aria-pressed="${chosen === c ? "true" : "false"}"><span class="mk-code">${c}</span> ${CAUSE[c]}</button>`;
    });
    return h`<div class="q-cause" data-q="${q.id}">
      <p class="q-cause-l">Why did you miss it?</p>
      <div class="q-cause-b">${buttons}</div>
      <p class="q-fix">${chosen ? repair(q, chosen) : null}</p>
    </div>`;
  }

  function setCause(qid, code) {
    var stats;
    if (!CAUSE[code] || !SAA.Store) return false;
    stats = SAA.Store.get("qstats");
    if (!stats || !stats.q || !stats.q[qid]) return false;
    var patch = { q: {} };
    patch.q[qid] = { c: code };
    SAA.Store.patch("qstats", patch);
    return true;
  }

  /* For a list of reviewed questions: one handler for all cause buttons under `rootEl`.
     `lookup(qid)` returns the question. */
  function bindReview(rootEl, lookup) {
    return U.on(rootEl, "click", ".q-rev [data-act=\"q-cause\"]", function (e, btn) {
      var box = btn.closest(".q-cause"), code = btn.getAttribute("data-c"), qid = btn.getAttribute("data-q");
      var q = lookup ? lookup(qid) : null, all, i;
      setCause(qid, code);
      all = box.querySelectorAll("[data-act=\"q-cause\"]");
      for (i = 0; i < all.length; i++) all[i].setAttribute("aria-pressed", all[i] === btn ? "true" : "false");
      if (q) U.set(box.querySelector(".q-fix"), repair(q, code));
      U.announce("Saved: " + CAUSE[code]);
    });
  }

  /* ---------- the checked parts (shared by render and review) ---------- */

  function trapLink(q, opt) {
    var meta = null, at;
    if (!opt.trap || q.dq || !q.ch) return null;
    try { meta = SAA.Content ? SAA.Content.meta(q.ch) : null; } catch (e) { meta = null; }
    at = meta && meta.traps ? meta.traps[opt.trap] : null;
    if (!at) return null;
    return h` <a class="xr opt-trap" href="${"#ch." + q.ch + "." + at}">See the trap</a>`;
  }

  function tagWords(right, mine) {
    if (right && mine) return "Correct answer · Your pick";
    if (right) return "Correct answer";
    if (mine) return "Your pick";
    return "";
  }

  function extras(q, withTools) {
    var expl = rich(q, q, "expl"), twin = q.dq ? null : rich(q, q, "twin"), take = rich(q, q, "take");
    var steps = q.worked && Array.isArray(q.worked.steps) ? q.worked.steps : null;
    var sec = !q.dq ? secHref(q.sec) : null;
    return h`<div class="q-ex">
      ${expl ? h`<div class="q-ex-b"><p class="q-ex-l">Why</p><p>${expl}</p></div>` : null}
      ${twin ? h`<div class="q-ex-b"><p class="q-ex-l">If the question changes</p><p>${twin}</p></div>` : null}
      ${take ? h`<div class="q-ex-b q-take"><p class="q-ex-l">Remember</p><p>${take}</p></div>` : null}
      ${steps && steps.length ? h`<div class="q-ex-b"><p class="q-ex-l">Think aloud</p><ol class="q-steps">${steps.map(function (s) { return h`<li>${s}</li>`; })}</ol></div>` : null}
      ${sec ? h`<p class="q-rev-link"><a class="xr" href="${sec}">Review: ${secTitle(q.sec)}</a></p>` : null}
      ${withTools ? h`<details class="q-rep"><summary>Report a problem</summary>
        <form class="q-rep-f" data-q="${q.id}">
          <label for="${"q-" + q.id + "-note"}">What is wrong with this question?</label>
          <textarea id="${"q-" + q.id + "-note"}" name="note" rows="3" maxlength="500"></textarea>
          <p><button type="submit" class="btn">Send</button></p>
        </form></details>` : null}
    </div>`;
  }

  /* ---------- QView.render ---------- */

  function isMulti(q) { return q.type === "multi" || q.select > 1; }

  function selectWord(q) { return "Select " + (COUNT_WORD[q.select] || q.select); }

  function sfPanel(c, ranges) {
    var q = c.q, s = c.state, words = stemWords(q.stem), needChip = q.opt != null, needWord = ranges.length > 0;
    var chips = !needChip ? null : h`<fieldset class="q-sf-chips"><legend>What does the question optimize?</legend>
      <div class="q-sf-row">${CHIPS.map(function (ch) {
        var id = "q-" + q.id + "-sf-" + ch[0];
        return h`<label class="chip" for="${id}"><input type="radio" name="${"q-" + q.id + "-sf"}" id="${id}" value="${ch[0]}" data-chip="${ch[0]}"${s.sfChip === ch[0] ? h` checked` : null}> ${ch[1]}</label>`;
      })}</div></fieldset>`;
    var tap = !needWord ? null : h`<div class="q-sf-tap"><p class="q-sf-l" id="${"q-" + q.id + "-sf-l"}">Tap the phrase that decides the answer</p>
      <p class="q-stem q-stem-tap" aria-labelledby="${"q-" + q.id + "-sf-l"}">${words.map(function (w, i) {
        return h`<span class="q-w${s.sfWord === i ? " is-on" : ""}" role="button" tabindex="0" data-i="${i}">${w.w}</span> `;
      })}</p></div>`;
    return h`<div class="q-sf">
      <p class="eyebrow">Stem first</p>
      ${chips}${tap}
      <p><button type="button" class="btn quiet" data-act="q-show">Show the options</button></p>
    </div>`;
  }

  function sfResult(c, ranges) {
    var q = c.q, s = c.state, words, w, chipOk, wordOk;
    if (!s.sfDone) return null;
    words = stemWords(q.stem);
    w = s.sfWord == null ? null : words[s.sfWord];
    chipOk = q.opt == null || s.sfChip == null ? null : s.sfChip === q.opt;
    wordOk = w ? wordHits(w, ranges) : null;
    return h`<div class="q-sf q-sf-done">
      ${q.opt != null ? h`<p><span class="q-sf-l">The question optimizes</span> <strong>${chipLabel(q.opt)}</strong>${chipOk === null ? null : h` <span class="pill ${chipOk ? "good" : "bad"}">${chipOk ? "You were right" : "You chose " + chipLabel(s.sfChip)}</span>`}</p>` : null}
      ${ranges.length ? h`<p><span class="q-sf-l">Deciding phrases</span> are marked in the question${wordOk === null ? null : h` <span class="pill ${wordOk ? "good" : "bad"}">${wordOk ? "Your word is in one" : "Your word, \"" + w.w + "\", is not in one"}</span>`}</p>` : null}
    </div>`;
  }

  function html(c) {
    var q = c.q, s = c.state, o = c.opts, multi = isMulti(q), right = rightIds(q);
    var ranges = kwRanges(q.stem, q.kw), inSf = s.stage === "sf" && !s.checked;
    var showKw = s.checked ? o.mode !== "exam" : !!s.sfDone;
    var ok = s.checked ? SAA.Scoring.isCorrect(q, s.picked) : false;
    var learn = o.mode !== "exam";
    var opts = s.order.map(function (id, i) {
      var opt = optionById(q, id), inputId = "q-" + q.id + "-o-" + id;
      var mine = s.picked.indexOf(id) >= 0, isRight = right.indexOf(String(id)) >= 0;
      var cls = "opt" + (mine ? " sel" : "") + (s.checked && learn ? (isRight ? " ok" : mine ? " no" : "") : "");
      var why = s.checked && learn ? rich(q, opt, "why") : null;
      var tag = s.checked && learn ? tagWords(isRight, mine) : "";
      return h`<div class="${cls}">
        <label class="opt-l" for="${inputId}"><input type="${multi ? "checkbox" : "radio"}" name="${"q-" + q.id}" id="${inputId}" value="${id}" data-opt="${id}"${mine ? h` checked` : null}${s.checked ? h` disabled` : null}>
          <span class="bubble" aria-hidden="true">${LETTERS[i] || ""}</span><span class="opt-t">${opt ? opt.text : ""}</span></label>
        ${s.checked && learn ? h`<div class="opt-x">${tag ? h`<span class="opt-tag">${tag}</span>` : null}${why ? h`<div class="opt-why">${why}${trapLink(q, opt)}</div>` : trapLink(q, opt)}</div>` : null}
      </div>`;
    });
    var verdict = !s.checked || !learn ? null : h`<p class="q-verdict" role="status"><span class="pill ${ok ? "good" : "bad"}">${ok ? "Correct" : "Wrong"}</span>${ok && s.unsure ? h` <span class="pill note">Not sure</span>` : null}</p>`;
    var nav;
    if (learn) {
      nav = s.checked
        ? h`<button type="button" class="btn primary" data-act="q-next">${o.last ? "See the result" : "Next question"}</button>`
        : h`<button type="button" class="btn primary" data-act="q-check"${s.picked.length ? null : h` disabled`}>Check</button>`;
    } else {
      nav = h`<button type="button" class="btn" data-act="q-prev"${o.n <= 1 ? h` disabled` : null}>Previous</button>
        <button type="button" class="btn${o.n >= o.of ? "" : " primary"}" data-act="q-next"${o.n >= o.of ? h` disabled` : null}>Next</button>`;
    }
    return h`<div class="q${multi ? " q-multi" : ""}" data-q="${q.id}">
      <div class="q-meta"><span class="eyebrow">${o.n ? "Question " + o.n + (o.of ? " of " + o.of : "") : "Question"}</span>${multi ? h`<span class="pill warn">${selectWord(q)}</span>` : null}</div>
      ${inSf ? null : h`<p class="q-stem">${showKw ? stemMarked(q.stem, ranges) : q.stem}</p>`}
      ${inSf ? sfPanel(c, ranges) : sfResult(c, ranges)}
      <fieldset class="q-opts"${inSf ? h` hidden` : null}><legend class="vh">${multi ? "Answer options. " + selectWord(q) + "." : "Answer options"}</legend>${opts}</fieldset>
      ${s.limit && !s.checked ? h`<p class="q-limit" role="status">This question takes ${q.select} answers. Untick one to change your selection.</p>` : null}
      <label class="q-unsure" for="${"q-" + q.id + "-unsure"}"${inSf ? h` hidden` : null}><input type="checkbox" id="${"q-" + q.id + "-unsure"}" data-act="q-unsure"${s.unsure ? h` checked` : null}${s.checked ? h` disabled` : null}> I am not sure about this one</label>
      ${verdict}
      ${inSf ? null : h`<div class="q-nav">${nav}</div>`}
      ${s.checked && learn && (!ok || s.unsure) ? causePanel(q, s.cause || null) : null}
      ${s.checked && learn ? extras(q, true) : null}
      ${s.checked || inSf ? null : h`<p class="q-keys">Keys: A to ${LETTERS[Math.max(0, s.order.length - 1)]} pick an option.</p>`}
    </div>`;
  }

  function changed(c) { if (c.opts.onChange) c.opts.onChange(c.state); }

  function pick(c, id, focusId) {
    var q = c.q, s = c.state, at;
    if (s.checked || s.stage === "sf") return;
    s.limit = 0;
    if (!isMulti(q)) s.picked = [id];
    else {
      at = s.picked.indexOf(id);
      if (at >= 0) s.picked.splice(at, 1);
      else if (s.picked.length >= q.select) s.limit = 1;
      else s.picked.push(id);
    }
    changed(c);
    draw(c, focusId);
  }

  function sfStep(c) {
    var q = c.q, s = c.state, ranges = kwRanges(q.stem, q.kw);
    var chipDone = q.opt == null || s.sfChip != null, wordDone = !ranges.length || s.sfWord != null;
    if (chipDone && wordDone) { s.sfDone = 1; s.stage = "opts"; }
    changed(c);
    draw(c, s.stage === "opts" ? "q-" + q.id + "-o-" + s.order[0] : null);
  }

  function draw(c, focusId) {
    var el = c.el, q = c.q, s = c.state, o = c.opts, r, f;
    U.set(el, html(c));
    r = el.firstElementChild;
    U.on(r, "change", "input[data-opt]", function (e, inp) { pick(c, inp.getAttribute("data-opt"), inp.id); });
    U.on(r, "change", "[data-act=\"q-unsure\"]", function (e, inp) { s.unsure = inp.checked ? 1 : 0; changed(c); });
    U.on(r, "click", "[data-act=\"q-check\"]", function () { if (s.picked.length && o.onCheck) o.onCheck(); });
    U.on(r, "click", "[data-act=\"q-next\"]", function () { if (o.onNav) o.onNav(1); });
    U.on(r, "click", "[data-act=\"q-prev\"]", function () { if (o.onNav) o.onNav(-1); });
    U.on(r, "change", "input[data-chip]", function (e, inp) { s.sfChip = inp.getAttribute("data-chip"); sfStep(c); });
    U.on(r, "click", ".q-stem-tap .q-w", function (e, w) { s.sfWord = Number(w.getAttribute("data-i")); sfStep(c); });
    U.on(r, "keydown", ".q-stem-tap .q-w", function (e, w) {
      if (e.key !== "Enter" && e.key !== " ") return;
      e.preventDefault(); s.sfWord = Number(w.getAttribute("data-i")); sfStep(c);
    });
    U.on(r, "click", "[data-act=\"q-show\"]", function () {
      s.stage = "opts"; changed(c); draw(c, "q-" + q.id + "-o-" + s.order[0]);
    });
    U.on(r, "click", "[data-act=\"q-cause\"]", function (e, btn) {
      s.cause = btn.getAttribute("data-c");
      setCause(q.id, s.cause);
      if (o.onCause) o.onCause(s.cause);
      changed(c);
      draw(c);
      f = el.querySelector(".q-fix a");
      if (f) f.focus();
    });
    U.on(r, "submit", ".q-rep-f", function (e, form) {
      var ta = form.querySelector("textarea"), note = ta ? ta.value.trim().slice(0, 500) : "";
      e.preventDefault();
      if (!note) return;
      if (SAA.Store && SAA.Store.flag) SAA.Store.flag("question", q.id, note);
      U.set(form, h`<p role="status">Report saved. Thank you.</p>`);
    });
    if (focusId) { f = document.getElementById(focusId); if (f) f.focus(); }
  }

  function onKey(e) {
    var c = cur, tag, s, i;
    if (!c || !c.el || !c.el.isConnected || e.metaKey || e.ctrlKey || e.altKey || e.defaultPrevented) return;
    tag = e.target && e.target.tagName;
    if (tag === "TEXTAREA" || tag === "SELECT") return;
    if (tag === "INPUT" && !/^(radio|checkbox)$/.test(e.target.type)) return;
    if (e.target && e.target.closest && e.target.closest("[role=\"dialog\"]")) return;
    s = c.state;
    if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
      if (tag === "INPUT") return;
      if (c.opts.onNav && (c.opts.mode === "exam" || s.checked)) c.opts.onNav(e.key === "ArrowRight" ? 1 : -1);
      return;
    }
    if (/^[a-fA-F]$/.test(e.key) && !s.checked && s.stage !== "sf") {
      i = e.key.toLowerCase().charCodeAt(0) - 97;
      if (i < s.order.length) { e.preventDefault(); pick(c, s.order[i], "q-" + c.q.id + "-o-" + s.order[i]); }
    }
  }

  function render(el, q, state, opts) {
    opts = opts || {};
    if (!Array.isArray(state.order) || !state.order.length) state.order = q.options.map(function (o) { return o.id; });
    if (!Array.isArray(state.picked)) state.picked = [];
    if (!state.stage) state.stage = opts.stemFirst && !state.checked ? "sf" : "opts";
    if (opts.mode === "exam") state.stage = "opts";
    if (opts.facts && SAA.Evidence && SAA.Evidence.register) SAA.Evidence.register(opts.facts);
    var c = { el: el, q: q, state: state, opts: opts };
    if (opts.keys !== false) cur = c;   // an inline question inside prose takes no letter keys
    draw(c, opts.focus || null);
    if (!keysOn && typeof document !== "undefined") { keysOn = true; U.on(document, "keydown", null, onKey); }
  }

  /* ---------- QView.review: read-only, no form control, no id ---------- */

  function review(el, q, answer, opts) {
    var order, right = rightIds(q), picked, ok, blank, ranges = kwRanges(q.stem, q.kw), items;
    opts = opts || {};
    answer = answer || {};
    picked = (answer.p || []).map(String);
    ok = answer.ok != null ? !!answer.ok : SAA.Scoring.isCorrect(q, picked);
    blank = !picked.length;
    order = Array.isArray(opts.order) && opts.order.length ? opts.order : q.options.map(function (o) { return o.id; });
    if (opts.facts && SAA.Evidence && SAA.Evidence.register) SAA.Evidence.register(opts.facts);
    items = order.map(function (id, i) {
      var opt = optionById(q, id), mine = picked.indexOf(String(id)) >= 0, isRight = right.indexOf(String(id)) >= 0;
      var why = opt ? rich(q, opt, "why") : null, tag = tagWords(isRight, mine);
      return h`<li class="opt${isRight ? " ok" : mine ? " no" : ""}"><span class="bubble" aria-hidden="true">${LETTERS[i] || ""}</span>
        <div class="opt-t">${opt ? opt.text : ""}<div class="opt-x">${tag ? h`<span class="opt-tag">${tag}</span>` : null}${why ? h`<div class="opt-why">${why}${opt ? trapLink(q, opt) : null}</div>` : null}</div></div></li>`;
    });
    U.set(el, h`<article class="q q-rev" data-q="${q.id}">
      <div class="q-meta"><span class="eyebrow">${opts.n ? "Question " + opts.n : "Question"}</span>
        <span class="pill ${ok ? "good" : blank ? "warn" : "bad"}">${ok ? "Correct" : blank ? "Unanswered" : "Wrong"}</span>${answer.u ? h`<span class="pill note">Not sure</span>` : null}${isMulti(q) ? h`<span class="pill warn">${selectWord(q)}</span>` : null}</div>
      <p class="q-stem">${stemMarked(q.stem, ranges)}</p>
      <ul class="q-opts">${items}</ul>
      ${opts.cause && (!ok || answer.u) ? causePanel(q, opts.c || null) : null}
      ${extras(q, false)}
    </article>`);
  }

  SAA.QView = {
    render: render,
    review: review,
    /* extras shared by quiz.js, exam.js, mistakes.js, cards.js and selftest.js */
    bindReview: bindReview,
    setCause: setCause,
    CAUSE: CAUSE,
    CAUSE_ORDER: CAUSE_ORDER,
    fail: fail,
    root: root,
    fmtDate: fmtDate,
    secHref: secHref,
    secTitle: secTitle,
    chapterTitle: chapterTitle,
    kwRanges: kwRanges
  };
})(globalThis.SAA = globalThis.SAA || {});
