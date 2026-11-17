/* speak.js (owner E). Speak practice: view "speak", mount "speak", Speak.render. Works without Claude. */
(function (SAA) {
  "use strict";

  var U = SAA.U, bus = SAA.bus, Core = SAA.AICore, AI = SAA.AI;
  var h = U.h;
  var Speak = SAA.Speak = SAA.Speak || {};

  var STARTERS = ["The short answer is…", "It works like this…", "The thing to watch is…", "In your case…"];
  var MOVE_NAMES = [["answer", "Answer first"], ["how", "How it works"], ["watch", "Trade-off or limit"],
                    ["you", "Example and question"]];
  var KIND = {explain: "Explain", compare: "Compare", decide: "Decide"};
  var LOAD_ERROR = "This page could not be loaded. Check your connection and try again.";

  var rehearsal = null;   /* {ids: [[slug, id]], i} while a rehearsal runs */

  /* ---------- helpers ---------- */

  function cfg() { return (SAA.state && SAA.state.cfg) || {}; }
  function arr(v) { return Array.isArray(v) ? v : []; }

  function spItems() {
    try {
      var d = SAA.Store && SAA.Store.get("speak");
      return (d && d.items) || {};
    } catch (e) { return {}; }
  }

  function draft(id, text) {
    try {
      if (!SAA.Store || !SAA.Store.draft) return "";
      if (text === undefined) return SAA.Store.draft(id) || "";
      SAA.Store.draft(id, text);
    } catch (e) { /* drafts are a convenience */ }
    return "";
  }

  function ones(s) { return String(s || "").split("1").length - 1; }

  function selfChecks() {
    var limit = Number(cfg().speakSeconds) || 0;
    return [
      "I answered in my first sentence.",
      "I used the must-say terms, and no wrong term.",
      "I gave cause and effect, not only a definition.",
      "I named one trade-off or limit.",
      "I gave an example, ended with a question, and stayed " +
        (limit ? "under " + limit + " seconds." : "inside the time.")
    ];
  }

  function bandClass(band) {
    if (band === "Customer-ready") return "good";
    if (band === "Correct but incomplete") return "warn";
    return "bad";
  }

  function chip(id, facts) {
    if (!id || !facts || !facts[id]) return "";
    return h` <a class="ev" href="#fact.${id}" data-fact="${id}">AWS source</a>`;
  }

  function secLink(item) {
    var s = item.sec;
    if (!s || !s.slug || !s.sid) return "";
    var row = null;
    try { row = SAA.Content && SAA.Content.section ? SAA.Content.section(s.slug, s.sid) : null; } catch (e) { row = null; }
    var href = "#ch." + s.slug + "." + (s.part || (row && row.part) || "deep") + "." + s.sid;
    return h`<p class="sp-again"><a class="xr" href="${href}">Read this section again${row && row.title ? ": " + row.title : ""}</a></p>`;
  }

  function saveItem(id, fields, counted) {
    var prev = spItems()[id] || {};
    var rec = {t: U.now(), tries: (prev.tries || 0) + (counted ? 0 : 1)};
    Object.keys(fields).forEach(function (k) { rec[k] = fields[k]; });
    if (!rec.self && !prev.self) rec.self = "00000";
    try {
      var items = {};
      items[id] = rec;
      SAA.Store.patch("speak", {items: items});
      SAA.Store.stamp("progress", ["daily", String(U.day()), "speak"], true);
    } catch (e) { /* nothing is stored without the store */ }
    return {self: rec.self || prev.self || "00000", score: rec.score === undefined ? null : rec.score};
  }

  /* ---------- one prompt ---------- */

  function cuesHtml(item) {
    var starters = STARTERS.slice();
    if (item.kind === "compare") starters[0] = "Both… The difference is…";
    return h`<details class="rv sp-cues"><summary>Show the four cues</summary><div class="rv-b"><ol class="sp-cue-list">${
      arr(item.skeleton).map(function (cue, i) {
        return h`<li><span class="sp-st">${starters[i] || ""}</span> <span class="sp-cue">${cue}</span></li>`;
      })}</ol><p class="sp-tip">Remember the first sentence and the cues, not the script.</p></div></details>`;
  }

  function modelHtml(item, facts) {
    return h`<details class="rv rv-answer sp-model"><summary>Show the model answer</summary><div class="rv-b">
      <h4 class="sp-h4">10 seconds</h4>
      <p>${item.ten_second}</p>
      <h4 class="sp-h4">60 seconds</h4>
      <div class="sp-lines">${arr(item.sixty_second).map(function (l) { return h`<p>${l}</p>`; })}</div>
      <h4 class="sp-h4">Do not say</h4>
      <ul class="sp-not">${arr(item.must_not_say).map(function (m) {
        return h`<li><span class="sp-wrong"><span class="bf-l">Wrong</span> ${m.error}</span> <span class="sp-right"><span class="bf-l">Correct</span> ${m.correct}${chip(m.fact, facts)}</span></li>`;
      })}</ul>
      ${arr(item.terms).length ? h`<h4 class="sp-h4">Words to use</h4><ul class="sp-terms">${item.terms.map(function (t) {
        return h`<li>Say <strong>${t.say}</strong>${arr(t.avoid).length ? ", not " + t.avoid.join(" or ") : ""}.</li>`;
      })}</ul>` : ""}
      <h4 class="sp-h4">Follow-up questions</h4>
      <ul class="sp-follow">${arr(item.follow_ups).map(function (f) {
        return h`<li><p>${f.question}</p><details class="rv"><summary>Answer</summary><div class="rv-b"><p>${f.answer}${chip(arr(f.facts)[0], facts)}</p></div></details></li>`;
      })}</ul>
      ${secLink(item)}
    </div></details>`;
  }

  function itemHtml(item, facts, opts) {
    var id = item.id;
    var limit = Number(cfg().speakSeconds) || 0;
    var cap = Core.CAPS.answer;
    var must = arr(item.key_points).filter(function (k) { return k.kind === "must"; });
    var prev = spItems()[id];
    var last = "";
    if (prev && prev.band) last = h`<span class="pill ${bandClass(prev.band)}">Last check: ${prev.band}, ${prev.score} of 10</span>`;
    else if (prev && prev.self) last = h`<span class="pill">Last self-check: ${ones(prev.self)} of 5</span>`;

    return h`<article class="sp" data-sp="${id}">
      <header class="sp-h">
        <p class="eyebrow">A customer asks <span class="pill">${KIND[item.kind] || item.kind}</span>${opts.extra ? h` <span class="pill">extra</span>` : ""} ${last}</p>
        <h2 class="sp-q" id="sp-${id}" tabindex="-1">${item.prompt}</h2>
        <p class="sp-who">${item.persona}</p>
        ${cuesHtml(item)}
      </header>

      <section class="sp-step sp-ans" aria-labelledby="sp-ans-h-${id}">
        <h3 class="sp-h3" id="sp-ans-h-${id}">Your answer</h3>
        <div class="sp-timer" data-on="0">
          <span class="sp-clock mono" role="timer" aria-label="Time spoken">0:00</span>
          ${limit ? h`<span class="sp-limit mono">of ${U.fmtClock(limit)}</span>` : ""}
          <span class="sp-over" hidden>Over time</span>
          <button type="button" class="btn" data-act="sp-timer">Start timer</button>
          <button type="button" class="btn quiet" data-act="sp-reset">Reset</button>
        </div>
        <label class="sp-label" for="sp-answer-${id}">Say your answer out loud. Type it here if you want to keep it or have Claude check it.</label>
        <textarea class="sp-text" id="sp-answer-${id}" rows="7" maxlength="${cap}" autocomplete="off" spellcheck="true"></textarea>
        <p class="sp-count mono" data-cap="${cap}">0 / ${cap.toLocaleString("en-US")} characters</p>
        <p class="sp-hint">Use the microphone key of your keyboard, or type.</p>
        <div class="sp-actions">
          <button type="button" class="btn primary" data-act="sp-self">Check myself</button>
          <span class="sp-ai ai-only" hidden>
            <button type="button" class="btn" data-act="sp-check" disabled>Check my explanation</button>
            ${AI.busyHtml(true)}
          </span>
        </div>
        <div class="sp-ai ai-only" hidden>${AI.notice()}</div>
        <p class="sp-err" role="alert" hidden></p>
      </section>

      <section class="sp-step sp-self" aria-labelledby="sp-self-h-${id}" hidden>
        <h3 class="sp-h3" id="sp-self-h-${id}" tabindex="-1">Self-check</h3>
        <fieldset class="sp-boxes">
          <legend>Five questions</legend>
          ${selfChecks().map(function (text, i) {
            return h`<label class="sp-box" for="sp-self-${id}-${i}"><input type="checkbox" id="sp-self-${id}-${i}" data-self="${i}"> <span>${text}</span></label>`;
          })}
        </fieldset>
        <fieldset class="sp-boxes">
          <legend>Must-say points</legend>
          <ul class="sp-kps">${must.map(function (k) {
            return h`<li class="sp-kp"><label class="sp-box" for="sp-kp-${id}-${k.id}"><input type="checkbox" id="sp-kp-${id}-${k.id}" data-kp="${k.id}"> <span>${k.point}</span></label></li>`;
          })}</ul>
        </fieldset>
        <div class="sp-actions">
          <button type="button" class="btn primary" data-act="sp-save">Save self-check</button>
          <span class="sp-saved" role="status"></span>
        </div>
        ${modelHtml(item, facts)}
      </section>

      <section class="sp-res" aria-label="Result of the check" hidden></section>
    </article>`;
  }

  function markedAnswer(answer, data) {
    var spans = [];
    function add(quote, kind) {
      var loc = Core.locate(quote, answer);
      if (loc) spans.push({s: loc.start, e: loc.end, kind: kind});
    }
    data.errors.forEach(function (e) { if (e.hit) add(e.quote, "err"); });
    data.covered.forEach(function (c) { if (c.hit) add(c.quote, "ok"); });
    spans.sort(function (a, b) { return a.s - b.s; });
    var out = [], pos = 0;
    spans.forEach(function (sp) {
      if (sp.s < pos) return;
      out.push(h`${answer.slice(pos, sp.s)}`);
      var text = answer.slice(sp.s, sp.e);
      out.push(sp.kind === "err"
        ? h`<mark class="mk-hit is-err">${text}<span class="vh"> (error)</span></mark>`
        : h`<mark class="mk-hit">${text}</mark>`);
      pos = sp.e;
    });
    out.push(h`${answer.slice(pos)}`);
    return out;
  }

  function resultHtml(item, facts, data, score) {
    var id = item.id;
    var covered = {}, missing = {};
    data.covered.forEach(function (c) { covered[c.kp] = c; });
    data.missing.forEach(function (m) { missing[m.kp] = m; });
    var stats = [score.coverage.hit + " of " + score.coverage.total + " must-say points", score.words + " words"];
    if (score.seconds) stats.push("about " + score.seconds + " seconds at speaking pace");
    if (score.longest) stats.push("longest sentence " + score.longest + " words");

    return h`<h3 class="sp-h3" tabindex="-1">Claude's check</h3>
      <p class="sp-band is-${bandClass(score.band)}"><span class="sp-band-w">${score.band}</span> <span class="sp-score mono">${score.score} / 10</span></p>
      <p class="sp-stats">${stats.join(" · ")}</p>
      <ul class="sp-moves">${MOVE_NAMES.map(function (m) {
        return h`<li><span class="mono">${data.moves[m[0]]}/2</span> ${m[1]}</li>`;
      })}</ul>

      <h4 class="sp-h4">Your answer</h4>
      <p class="sp-mine">${markedAnswer(data.answer, data)}</p>
      <p class="sp-legend">Marked words cover a key point. Underlined words hold an error.</p>

      <h4 class="sp-h4">Key points</h4>
      <ul class="sp-kps">${arr(item.key_points).map(function (k) {
        var hit = !!covered[k.id];
        var word = hit ? "Covered" : (k.kind === "must" ? "Missing" : "Not said, nice to have");
        var say = missing[k.id] && missing[k.id].say;
        return h`<li class="sp-kp${hit ? " is-hit" : ""}${!hit && k.kind === "must" ? " is-miss" : ""}"><span class="sp-kp-s">${word}</span> <span class="sp-kp-t">${k.point}</span>${say ? h` <span class="sp-add">Add: ${say}</span>` : ""}</li>`;
      })}</ul>

      ${data.errors.length ? h`<h4 class="sp-h4">Errors</h4><ul class="sp-errs">${data.errors.map(function (e) {
        return h`<li>${e.quote ? h`<q>${e.quote}</q> ` : ""}${e.problem} <span class="sp-right"><span class="bf-l">Correct</span> ${e.correct}${chip(e.fact, facts)}</span></li>`;
      })}</ul>` : ""}

      ${data.unverified.length ? h`<h4 class="sp-h4">Not checked</h4><p class="sp-sub">The reference does not cover these statements, so they were not checked.</p><ul class="sp-unv">${data.unverified.map(function (u) {
        return h`<li><q>${u.quote}</q></li>`;
      })}</ul>` : ""}

      ${data.terms.length ? h`<h4 class="sp-h4">Better words</h4><ul class="sp-terms">${data.terms.map(function (t) {
        return h`<li>You said <q>${t.said}</q>. Say <strong>${t.better}</strong>.</li>`;
      })}</ul>` : ""}

      ${data.heard_as.length ? h`<h4 class="sp-h4">Heard as</h4><p class="sp-sub">Dictation may have typed another word than you said.</p><ul class="sp-terms">${data.heard_as.map(function (t) {
        return h`<li><q>${t.said}</q> was probably <strong>${t.meant}</strong>.</li>`;
      })}</ul>` : ""}

      ${data.clarity.length ? h`<h4 class="sp-h4">Clarity</h4><ul class="sp-tips">${data.clarity.map(function (c) {
        return h`<li>${c}</li>`;
      })}</ul>` : ""}

      ${data.improved ? h`<h4 class="sp-h4">Your answer, repaired</h4>
      <p class="sp-improved" id="sp-imp-${id}">${data.improved}</p>
      <p><button type="button" class="btn" data-act="sp-copy">Copy</button></p>` : ""}

      ${data.next ? h`<h4 class="sp-h4">Practise next</h4><p>${data.next}</p>` : ""}
      ${data.follow_up ? h`<h4 class="sp-h4">Follow-up question</h4><p class="sp-fu">${data.follow_up}</p>` : ""}`;
  }

  Speak.render = function (el, item, opts) {
    opts = opts || {};
    var facts = opts.facts || {};
    var id = item.id;
    var limit = Number(cfg().speakSeconds) || 0;
    var st = {dead: false, timer: null, t0: 0, base: 0, shown: -1, counted: false, announced: false};

    try { if (SAA.Evidence && SAA.Evidence.register) SAA.Evidence.register(facts); } catch (e) { /* chips fall back to their route */ }
    U.set(el, itemHtml(item, facts, opts));
    var root = el.querySelector(".sp");
    var ta = root.querySelector(".sp-text");
    var clock = root.querySelector(".sp-clock");
    var timerBox = root.querySelector(".sp-timer");
    var timerBtn = root.querySelector("[data-act=sp-timer]");
    var overEl = root.querySelector(".sp-over");
    var countEl = root.querySelector(".sp-count");
    var checkBtn = root.querySelector("[data-act=sp-check]");
    var busyEl = root.querySelector(".ai-busy");
    var errEl = root.querySelector(".sp-err");
    var selfEl = root.querySelector(".sp-self");
    var resEl = root.querySelector(".sp-res");
    var savedEl = root.querySelector(".sp-saved");

    function elapsedMs() { return st.base + (st.timer ? U.nowMs() - st.t0 : 0); }

    function paintClock() {
      var sec = Math.floor(elapsedMs() / 1000);
      if (sec === st.shown) return;
      st.shown = sec;
      clock.textContent = U.fmtClock(sec);
      var over = limit > 0 && sec >= limit;
      overEl.hidden = !over;
      timerBox.classList.toggle("over", over);
      if (over && !st.announced) {
        st.announced = true;
        U.announce("Time. " + U.fmtClock(limit) + " reached.");
      }
    }

    function stopTimer() {
      if (!st.timer) return;
      st.base = elapsedMs();
      clearInterval(st.timer);
      st.timer = null;
      timerBox.setAttribute("data-on", "0");
      timerBtn.textContent = "Start timer";
      paintClock();
    }

    function startTimer() {
      if (st.timer) return;
      st.t0 = U.nowMs();
      st.timer = setInterval(paintClock, 250);
      timerBox.setAttribute("data-on", "1");
      timerBtn.textContent = "Stop timer";
    }

    function paintCount() {
      var text = ta.value;
      var words = Core.words(text);
      var wpm = Number(cfg().wordsPerMinute) || 0;
      var line = text.length.toLocaleString("en-US") + " / " + Core.CAPS.answer.toLocaleString("en-US") + " characters";
      if (words) line += " · " + words + " words";
      if (words && wpm) line += " · about " + Math.round(words * 60 / wpm) + " seconds spoken";
      countEl.textContent = line;
      if (checkBtn) checkBtn.disabled = !text.trim();
    }

    function syncAI() {
      var on = AI.available();
      var list = root.querySelectorAll(".sp-ai");
      for (var i = 0; i < list.length; i++) list[i].hidden = !on;
    }

    function setBusy(on) {
      checkBtn.hidden = on;
      busyEl.hidden = !on;
    }

    function showErr(text) {
      errEl.textContent = text || "";
      errEl.hidden = !text;
    }

    function openSelf(focus) {
      selfEl.hidden = false;
      if (focus) {
        var hd = selfEl.querySelector("h3");
        if (hd) hd.focus();
      }
    }

    function selfString() {
      var s = "";
      var boxes = root.querySelectorAll("[data-self]");
      for (var i = 0; i < boxes.length; i++) s += boxes[i].checked ? "1" : "0";
      return s;
    }

    function spokenSeconds(fallback) {
      var sec = Math.round(elapsedMs() / 1000);
      return sec > 0 ? sec : (fallback || 0);
    }

    function saveSelf() {
      stopTimer();
      var self = selfString();
      var words = Core.words(ta.value);
      var out = saveItem(id, {self: self, words: words, seconds: spokenSeconds(0)}, st.counted);
      st.counted = true;
      savedEl.textContent = "Saved. " + ones(self) + " of 5.";
      bus.emit("speak:done", {id: id, self: ones(self), score: out.score});
    }

    function check() {
      var text = ta.value.trim();
      if (!text || !AI.available()) return;
      showErr("");
      stopTimer();
      var promptText = Core.speakPrompt(item, facts, text);
      setBusy(true);
      AI.call(promptText, {tier: "default"}).then(function (r) {
        if (st.dead) return;
        setBusy(false);
        if (!r.ok) {
          if (r.code === "refused") { U.set(resEl, null); resEl.hidden = true; }
          if (r.hide) syncAI();
          showErr(r.message);
          return;
        }
        var v = Core.validSpeak(r.data, item, text);
        if (!v.ok) { showErr(Core.message("invalid_json").text); return; }
        var score = Core.speakScore(v.data, item);
        U.set(resEl, resultHtml(item, facts, v.data, score));
        resEl.hidden = false;
        var hd = resEl.querySelector("h3");
        if (hd) hd.focus();
        var must = arr(item.key_points).filter(function (k) { return k.kind === "must"; });
        var got = {};
        v.data.covered.forEach(function (c) { got[c.kp] = 1; });
        var out = saveItem(id, {
          score: score.score, band: score.band, words: score.words,
          missing: must.filter(function (k) { return !got[k.id]; }).map(function (k) { return k.id; }),
          seconds: spokenSeconds(score.seconds)
        }, st.counted);
        st.counted = true;
        bus.emit("speak:done", {id: id, self: ones(out.self), score: score.score});
      });
    }

    U.on(root, "click", "[data-act]", function (ev, btn) {
      var act = btn.getAttribute("data-act");
      if (act === "sp-timer") { if (st.timer) stopTimer(); else startTimer(); }
      else if (act === "sp-reset") {
        stopTimer();
        st.base = 0; st.shown = -1; st.announced = false; st.counted = false;
        paintClock();
      }
      else if (act === "sp-self") { stopTimer(); openSelf(true); }
      else if (act === "sp-save") saveSelf();
      else if (act === "sp-check") check();
      else if (act === "ai-stop") AI.stop();
      else if (act === "sp-copy") {
        var imp = root.querySelector(".sp-improved");
        if (!imp) return;
        U.copy(imp.textContent).then(function (ok) {
          if (ok) U.toast("Copied.");
          else { U.select(imp); U.toast("Press copy on your keyboard."); }
        });
      }
    });
    U.on(root, "input", ".sp-text", function () {
      paintCount();
      draft("sp-answer-" + id, ta.value);
    });
    U.on(root, "change", "[data-kp]", function (ev, box) {
      var li = box.closest(".sp-kp");
      if (li) li.classList.toggle("is-hit", box.checked);
    });

    var kept = (opts.text !== undefined && opts.text !== null) ? opts.text : draft("sp-answer-" + id);
    if (kept) ta.value = String(kept).slice(0, Core.CAPS.answer);
    paintCount();
    paintClock();
    syncAI();
    if ((opts.step || 1) >= 3) openSelf(false);

    var onCaps = bus.on("caps", syncAI);
    var onOff = bus.on("ai:off", syncAI);

    return function cleanup() {
      st.dead = true;
      if (st.timer) { clearInterval(st.timer); st.timer = null; }
      bus.off("caps", onCaps);
      bus.off("ai:off", onOff);
    };
  };

  /* ---------- several prompts of one chapter (mount and chapter view) ---------- */

  function orderItems(items) {
    return items.slice().sort(function (a, b) {
      return (b.pass_route ? 1 : 0) - (a.pass_route ? 1 : 0);
    });
  }

  function renderChapter(el, data, focusId, route, hot) {
    var items = orderItems(arr(data && data.speak));
    var cleanups = [];
    if (!items.length) {
      U.set(el, h`<p class="notice">This chapter has no speaking prompts yet.</p>`);
      return function () {};
    }
    U.set(el, h`<p class="sp-intro">Answer out loud first. Then check yourself against the must-say points and the model answer.</p>${
      items.map(function (it) { return h`<div class="sp-slot" data-slot="${it.id}"></div>`; })}`);
    items.forEach(function (it) {
      var slot = el.querySelector("[data-slot=\"" + it.id + "\"]");
      var extra = !it.pass_route && route && route !== "full";
      var text = hot && hot.text ? hot.text["sp-answer-" + it.id] : undefined;
      cleanups.push(Speak.render(slot, it, {facts: data.facts || {}, extra: extra, text: text}));
    });
    if (focusId) {
      var target = el.querySelector("#sp-" + focusId);
      if (target && target.scrollIntoView) target.scrollIntoView();
    }
    return function () { cleanups.forEach(function (fn) { try { fn(); } catch (e) { /* keep going */ } }); };
  }

  function unsent(el) {
    var out = {};
    if (!el) return out;
    var list = el.querySelectorAll(".sp-text");
    for (var i = 0; i < list.length; i++) if (list[i].value) out[list[i].id] = list[i].value;
    return out;
  }

  if (SAA.Reader && SAA.Reader.registerMount) {
    SAA.Reader.registerMount("speak", function (el, id, ctx) {
      var dead = false, inner = null;
      ctx = ctx || {};
      Promise.resolve(ctx.data ? ctx.data() : null).then(function (data) {
        if (dead) return;
        inner = renderChapter(el, data, id || "", ctx.route || "pass", ctx.hot);
      }, function () {
        if (!dead) U.set(el, h`<p class="notice">${LOAD_ERROR}</p>`);
      });
      return function () { dead = true; if (inner) inner(); };
    });
  }

  /* ---------- view "speak" ---------- */

  var view = {el: null, cleanup: null, token: 0};

  function lastPill(rec) {
    if (rec && rec.band) return h`<span class="pill ${bandClass(rec.band)}">${rec.band}, ${rec.score} of 10</span>`;
    if (rec && rec.self) return h`<span class="pill">Self-check ${ones(rec.self)} of 5</span>`;
    return h`<span class="pill sp-new">Not practised</span>`;
  }

  function rowHtml(id, e, items) {
    return h`<li class="sp-row"><a class="sp-row-a" href="#speak.${e[0]}.${id}">${e[4]}</a> <span class="sp-row-m"><span class="pill">${KIND[e[1]] || e[1]}</span> ${lastPill(items[id])}</span></li>`;
  }

  function listHtml(manifest, sindex) {
    var items = spItems();
    var ids = Object.keys(sindex).sort();
    if (!ids.length) return h`<p class="notice">No speaking prompts are ready yet. They appear when a chapter is ready.</p>`;
    var pack = ids.filter(function (id) { return sindex[id][3]; });
    var by = {};
    ids.forEach(function (id) { (by[sindex[id][0]] = by[sindex[id][0]] || []).push(id); });
    var titles = {};
    arr(manifest && manifest.chapters).forEach(function (c) { titles[c.slug] = c.title; });
    var order = arr(manifest && manifest.order).filter(function (s) { return by[s]; });
    Object.keys(by).sort().forEach(function (s) { if (order.indexOf(s) === -1) order.push(s); });
    var done = ids.filter(function (id) { return items[id]; }).length;

    return h`<p class="sp-intro">${done} of ${ids.length} prompts practised. Ten minutes a day is enough: answer out loud, then check yourself.</p>
      ${ids.length > 1 ? h`<p class="sp-actions"><button type="button" class="btn" data-act="sp-rehearse">Rehearsal: ${Math.min(10, ids.length)} random prompts</button></p>` : ""}
      ${pack.length ? h`<section class="sp-group"><h2 class="sp-h3">Speaking pack</h2><ul class="sp-list">${
        pack.map(function (id) { return rowHtml(id, sindex[id], items); })}</ul></section>` : ""}
      ${order.map(function (slug) {
        return h`<section class="sp-group"><h2 class="sp-h3"><a href="#speak.${slug}">${titles[slug] || slug}</a></h2><ul class="sp-list">${
          by[slug].map(function (id) { return rowHtml(id, sindex[id], items); })}</ul></section>`;
      })}`;
  }

  function rehearsalHtml(slug, id) {
    if (!rehearsal) return "";
    var i = -1;
    rehearsal.ids.forEach(function (p, k) { if (p[1] === id) i = k; });
    if (i === -1) return "";
    var next = rehearsal.ids[i + 1];
    return h`<p class="sp-reh">Rehearsal: prompt ${i + 1} of ${rehearsal.ids.length}. ${next
      ? h`<a class="btn" href="#speak.${next[0]}.${next[1]}">Next prompt</a>`
      : h`<a class="btn" href="#speak">Finish</a>`}</p>`;
  }

  function mountView(el, args, ctx) {
    var token = ++view.token;
    var slug = args[0] || "", id = args[1] || "";
    var Content = SAA.Content;
    view.el = el;
    if (view.cleanup) { view.cleanup(); view.cleanup = null; }
    var meta = null;
    try { meta = slug && Content.meta ? Content.meta(slug) : null; } catch (e) { meta = null; }
    var title = slug ? "Say it: " + ((meta && meta.title) || slug) : "Speak practice";
    U.set(el, h`<div class="sp-view"><h1 tabindex="-1">${title}</h1>${slug ? h`<p class="sp-back"><a href="#speak">All prompts</a>${id ? h` · <a href="#speak.${slug}">Prompts of this chapter</a>` : ""}</p>` : ""}<div class="sp-body"><p class="sp-wait">Loading…</p></div></div>`);
    var wrap = el.querySelector(".sp-view");
    var body = el.querySelector(".sp-body");

    function failed() {
      if (token !== view.token) return;
      U.set(body, h`<p class="notice">${LOAD_ERROR} <button type="button" class="btn" data-act="sp-retry">Retry</button></p>`);
    }

    U.on(wrap, "click", "[data-act=sp-retry]", function () { mountView(el, args, ctx); });
    U.on(wrap, "click", "[data-act=sp-rehearse]", function () {
      Content.sindex().then(function (s) {
        var picks = U.shuffle(Object.keys(s)).slice(0, 10).map(function (k) { return [s[k][0], k]; });
        if (!picks.length) return;
        rehearsal = {ids: picks};
        SAA.Router.go("#speak." + picks[0][0] + "." + picks[0][1]);
      }, function () { /* the list already shows the error */ });
    });

    if (!slug) {
      rehearsal = null;
      return Promise.all([Content.manifest(), Content.sindex()]).then(function (r) {
        if (token !== view.token) return;
        U.set(body, listHtml(r[0], r[1] || {}));
      }, failed);
    }

    return Promise.all([Content.manifest(), Content.data(slug)]).then(function (r) {
      if (token !== view.token) return;
      var data = r[1];
      var h1 = el.querySelector("h1");
      var m = null;
      try { m = Content.meta(slug); } catch (e) { m = null; }
      if (h1 && m && m.title) h1.textContent = "Say it: " + m.title;
      if (!id) {
        view.cleanup = renderChapter(body, data, "", "full", ctx && ctx.hot);
        return;
      }
      var item = arr(data && data.speak).filter(function (it) { return it.id === id; })[0];
      if (!item) {
        U.set(body, h`<p class="notice">This prompt does not exist. <a href="#speak">See all prompts</a></p>`);
        return;
      }
      U.set(body, h`${rehearsalHtml(slug, id)}<div class="sp-slot"></div>`);
      var hot = ctx && ctx.hot;
      view.cleanup = Speak.render(body.querySelector(".sp-slot"), item, {
        facts: data.facts || {}, step: 1,
        text: hot && hot.text ? hot.text["sp-answer-" + id] : undefined
      });
    }, failed);
  }

  if (SAA.Router && SAA.Router.register) {
    SAA.Router.register("speak", {
      mount: mountView,
      unmount: function () {
        view.token++;
        if (view.cleanup) { view.cleanup(); view.cleanup = null; }
        view.el = null;
      },
      title: function (args) {
        var meta = null;
        try { meta = args && args[0] ? SAA.Content.meta(args[0]) : null; } catch (e) { meta = null; }
        return args && args[0] ? "Say it: " + ((meta && meta.title) || args[0]) : "Speak practice";
      },
      snapshot: function () { return {text: unsent(view.el)}; }
    });
  }

  /* ---------- screenshot states ---------- */

  var SHOT_ANSWER = "The short answer is: a shelf keeps your widgets in one Region. It works like this. " +
    "You choose the Region when you create the shelf, and the widgets stay there. " +
    "You can move the shelf later if you need to. In your case, I would keep one shelf in Frankfurt. " +
    "Do you expect customers in a second Region this year?";

  function shotItem() {
    var Content = SAA.Content;
    return Content.sindex().then(function (s) {
      var id = Object.keys(s).sort()[0];
      if (!id) return null;
      return Content.data(s[id][0]).then(function (d) {
        var item = arr(d && d.speak).filter(function (it) { return it.id === id; })[0];
        return item ? {item: item, facts: d.facts || {}} : null;
      });
    });
  }

  function shot(el, step, after) {
    try { if (SAA.Store && SAA.Store.reset) SAA.Store.reset(); } catch (e) { /* preview only */ }
    U.set(el, h`<div class="sp-view"><h1 tabindex="-1">Say it</h1><div class="sp-body"><div class="sp-slot"></div></div></div>`);
    return shotItem().then(function (r) {
      if (!r) { U.set(el.querySelector(".sp-body"), h`<p class="notice">No speaking prompt in this build.</p>`); return; }
      var slot = el.querySelector(".sp-slot");
      Speak.render(slot, r.item, {facts: r.facts, step: step, text: SHOT_ANSWER});
      after(slot);
    });
  }

  if (SAA.Test && SAA.Test.register) {
    SAA.Test.register("speak-self", function (el) {
      return shot(el, 3, function (slot) {
        var boxes = slot.querySelectorAll("[data-self], [data-kp]");
        for (var i = 0; i < boxes.length; i++) {
          if (i === 2 || i === 6) continue;
          boxes[i].checked = true;
          var li = boxes[i].closest(".sp-kp");
          if (li) li.classList.add("is-hit");
        }
        var model = slot.querySelector(".sp-model");
        if (model) model.open = true;
      });
    });
    SAA.Test.register("speak-result", function (el) {
      return shot(el, 1, function (slot) {
        var btn = slot.querySelector("[data-act=sp-check]");
        var clicked = false;
        /* a headless screenshot of a scrolled page is shifted, so the shot goes back to the top */
        bus.on("speak:done", function () { try { globalThis.scrollTo(0, 0); } catch (e) { /* no window */ } });
        function go() {
          if (clicked || !btn || btn.disabled || !AI.available()) return;
          clicked = true;
          btn.click();
        }
        go();
        if (!clicked) bus.on("caps", go);
      });
    });
  }

})(globalThis.SAA = globalThis.SAA || {});
