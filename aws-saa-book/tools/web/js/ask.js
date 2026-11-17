/* ask.js (owner E). "Ask about this section": a sheet that asks Claude with the section as the only source. */
(function (SAA) {
  "use strict";

  var U = SAA.U, Core = SAA.AICore, AI = SAA.AI;
  var h = U.h;
  var Ask = SAA.Ask = SAA.Ask || {};

  var FIXED = [
    ["Explain more simply", "Explain this section more simply, in short sentences."],
    ["Give an analogy", "Give one everyday analogy for the main idea of this section."],
    ["What would the exam ask?", "What would the exam ask about this section? Name the words in a question that point to it."],
    ["Quiz me", "Quiz me: ask me one question about this section. Then give the answer on a new line that starts with \"Answer:\"."]
  ];
  var OFF_TEXT = "Claude features are off for this page.";

  var hist = {};     /* "<slug>.<sid>" -> [{q, a, view}] ; memory only */
  var cur = null;    /* the open sheet */

  function arr(v) { return Array.isArray(v) ? v : []; }

  function draft(text) {
    try {
      if (!SAA.Store || !SAA.Store.draft) return "";
      if (text === undefined) return SAA.Store.draft("ask-q") || "";
      SAA.Store.draft("ask-q", text);
    } catch (e) { /* drafts are a convenience */ }
    return "";
  }

  /* ---------- marking a sentence in the reader ---------- */

  function sectionEl(sid) { return document.getElementById("sec-" + sid); }

  function textNodes(root) {
    var out = [], raw = "", node;
    var walker = document.createTreeWalker(root, 4, null);   /* 4 = NodeFilter.SHOW_TEXT */
    while ((node = walker.nextNode())) {
      out.push({node: node, start: raw.length});
      raw += node.nodeValue;
    }
    return {nodes: out, raw: raw};
  }

  function locate(sid, quote) {
    var root = sectionEl(sid);
    if (!root) return null;
    var map = textNodes(root);
    var loc = Core.locate(quote, map.raw);
    return loc ? {map: map, loc: loc} : null;
  }

  function clearMarks() {
    var list = document.querySelectorAll("mark.mk-hit[data-ask]");
    for (var i = 0; i < list.length; i++) {
      var m = list[i], parent = m.parentNode;
      if (!parent) continue;
      parent.replaceChild(document.createTextNode(m.textContent), m);
      parent.normalize();
    }
  }

  function markQuote(sid, quote) {
    clearMarks();
    var found = locate(sid, quote);
    if (!found) return null;
    var first = null;
    var nodes = found.map.nodes;
    for (var i = nodes.length - 1; i >= 0; i--) {
      var n = nodes[i], len = n.node.nodeValue.length;
      var s = Math.max(found.loc.start, n.start) - n.start;
      var e = Math.min(found.loc.end, n.start + len) - n.start;
      if (e <= s || !n.node.nodeValue.slice(s, e).trim()) continue;
      try {
        var range = document.createRange();
        range.setStart(n.node, s);
        range.setEnd(n.node, e);
        var mark = document.createElement("mark");
        mark.className = "mk-hit";
        mark.setAttribute("data-ask", "1");
        range.surroundContents(mark);
        first = mark;
      } catch (err) { /* this piece stays unmarked */ }
    }
    return first;
  }

  function showQuote(sid, quote) {
    if (SAA.Pop) SAA.Pop.closeSheet(true);
    var mark = markQuote(sid, quote);
    if (!mark) { U.toast("This sentence could not be found on the page."); return; }
    var p = mark.parentElement;
    while (p && p.id !== "saa-view") {
      if (p.tagName === "DETAILS") p.open = true;
      p = p.parentElement;
    }
    mark.setAttribute("tabindex", "-1");
    try {
      var top = mark.getBoundingClientRect().top;
      globalThis.scrollBy(0, Math.round(top - globalThis.innerHeight * 0.35));
    } catch (e) { mark.scrollIntoView(); }
    try { mark.focus({preventScroll: true}); } catch (e2) { /* older engines */ }
    U.announce("The sentence is marked in the text.");
  }

  /* ---------- rendering ---------- */

  function answerHtml(text) {
    var out = [], list = [];
    function flush() {
      if (list.length) out.push(h`<ul>${list.map(function (l) { return h`<li>${l}</li>`; })}</ul>`);
      list = [];
    }
    String(text || "").split(/\n+/).forEach(function (l) {
      l = l.trim();
      if (!l) return;
      if (/^[-*•]\s+/.test(l)) { list.push(l.replace(/^[-*•]\s+/, "")); return; }
      flush();
      out.push(h`<p>${l}</p>`);
    });
    flush();
    return out;
  }

  function fromWord(from) {
    if (/^fact:/.test(from)) return "from a fact of this chapter";
    if (/^glossary:/.test(from)) return "from the glossary";
    if (/^figure:/.test(from)) return "from a figure";
    if (from === "summary") return "from the chapter summary";
    return "";
  }

  function supportHtml(view, sid, turnIndex) {
    var hits = view.support.filter(function (s) { return s.hit; });
    if (!hits.length) return "";
    return h`<p class="ask-src-l">Sentences this answer rests on</p><ul class="ask-src">${hits.map(function (s) {
      var i = view.support.indexOf(s);
      if (locate(sid, s.quote)) {
        return h`<li><button type="button" class="ask-quote" data-act="ask-quote" data-turn="${turnIndex}" data-i="${i}">${s.quote}</button> <span class="ask-from">Show in the text</span></li>`;
      }
      return h`<li><q>${s.quote}</q> <span class="ask-from">${fromWord(s.from)}</span></li>`;
    })}</ul>`;
  }

  function turnHtml(turn, sid, i, isLast) {
    var v = turn.view, body;
    if (v.status === "not_in_book") {
      var titles = {};
      arr(SAA.state && SAA.state.manifest && SAA.state.manifest.chapters).forEach(function (c) { titles[c.slug] = c.title; });
      body = h`<div class="ask-a is-none">
        <h3 class="ask-h">This section does not cover that.</h3>
        ${v.missing ? h`<p>${v.missing}</p>` : ""}
        ${v.see.length ? h`<p>Try: ${U.join(v.see.map(function (slug) {
          return h`<a class="xr" href="#ch.${slug}">${titles[slug] || slug}</a>`;
        }), ", ")}</p>` : ""}
        <p><button type="button" class="btn" data-act="ask-search" data-turn="${i}">Search the book</button></p>
      </div>`;
    } else if (v.grounded === "none") {
      body = h`<div class="ask-a is-unverified">
        <h3 class="ask-h">Not verified against the chapter</h3>
        <div class="ask-text">${answerHtml(v.answer)}</div>
        ${v.status === "partly" && v.missing ? h`<p class="ask-miss"><span class="bf-l">Not in the chapter</span> ${v.missing}</p>` : ""}
        <p class="ask-warn">No sentence of the chapter could be matched to this answer. Check it against the text before you rely on it.</p>
        ${isLast ? h`<p><button type="button" class="btn" data-act="ask-careful">Answer more carefully</button></p>` : ""}
      </div>`;
    } else {
      body = h`<div class="ask-a">
        <h3 class="ask-h">From this chapter</h3>
        <div class="ask-text">${answerHtml(v.answer)}</div>
        ${v.status === "partly" && v.missing ? h`<p class="ask-miss"><span class="bf-l">Not in the chapter</span> ${v.missing}</p>` : ""}
        ${v.grounded === "some" ? h`<p class="ask-warn">Some of this could not be matched to the chapter.</p>` : ""}
        ${supportHtml(v, sid, i)}
      </div>`;
    }
    return h`<div class="ask-turn"><p class="ask-q"><span class="bf-l">You</span> ${turn.label || turn.q}</p>${body}</div>`;
  }

  function sheetHtml(ctx) {
    var cap = Core.CAPS.question;
    return h`<div class="ask">
      <p class="ask-sec"><span class="eyebrow">${ctx.chapter}</span> <strong>${ctx.title}</strong></p>
      <p class="ask-rule">Claude answers only from this section and its facts. It says so when the section does not cover your question.</p>
      <div class="ask-log"></div>
      <div class="ask-quick" role="group" aria-label="Ready questions">${FIXED.map(function (f, i) {
        return h`<button type="button" class="btn" data-act="ask-fixed" data-i="${i}">${f[0]}</button>`;
      })}</div>
      <form class="ask-form" novalidate>
        <label class="ask-label" for="ask-q">Your question</label>
        <textarea class="ask-in" id="ask-q" rows="3" maxlength="${cap}" autocomplete="off"></textarea>
        <div class="ask-actions">
          <button type="submit" class="btn primary" data-act="ask-send" disabled>Send</button>
          ${AI.busyHtml(true)}
          <span class="ask-count mono">0 / ${cap}</span>
        </div>
      </form>
      <p class="ask-err" role="alert" hidden></p>
      ${AI.notice()}
    </div>`;
  }

  /* ---------- the open sheet ---------- */

  function paintLog(s) {
    var log = s.el.querySelector(".ask-log");
    var turns = hist[s.key] || [];
    U.set(log, turns.map(function (t, i) { return turnHtml(t, s.sid, i, i === turns.length - 1); }));
    var last = log.lastElementChild;
    if (last && last.scrollIntoView) { try { last.scrollIntoView({block: "nearest"}); } catch (e) { /* older engines */ } }
  }

  function setBusy(s, on) {
    var busy = s.el.querySelector(".ai-busy");
    var send = s.el.querySelector("[data-act=ask-send]");
    var ta = s.el.querySelector(".ask-in");
    if (!busy || !send || !ta) return;
    busy.hidden = !on;
    send.hidden = on;
    var quick = s.el.querySelectorAll("[data-act=ask-fixed], [data-act=ask-careful]");
    for (var i = 0; i < quick.length; i++) quick[i].disabled = on;
    if (!on) send.disabled = !ta.value.trim();
  }

  function showErr(s, text) {
    var el = s.el.querySelector(".ask-err");
    el.textContent = text || "";
    el.hidden = !text;
  }

  function build(s, history, question) {
    var cap = Core.CAPS.section;
    var ctx = Core.askContext(s.chapter, s.slug, s.sid, s.manifest, s.glossary, {section: cap});
    var turns = Core.askTurns(ctx.first, history, question);
    while (Core.turnBytes(turns) > Core.CAPS.promptBytes && cap > 1500) {
      cap = Math.floor(cap / 2);
      ctx = Core.askContext(s.chapter, s.slug, s.sid, s.manifest, s.glossary, {section: cap});
      turns = Core.askTurns(ctx.first, history, question);
    }
    return {turns: turns, sent: ctx.sent};
  }

  /* replace: true repeats the last question on the stronger tier and replaces its answer. */
  function ask(s, question, label, replace) {
    question = String(question || "").trim();
    if (!question || AI.busy()) return;
    var list = hist[s.key] = hist[s.key] || [];
    var before = replace ? list.slice(0, -1) : list.slice();
    var req = build(s, before.map(function (t) { return {q: t.q, a: t.a}; }), question);
    showErr(s, "");
    setBusy(s, true);
    AI.call(req.turns, {tier: replace ? "default" : "quick", cache: false}).then(function (r) {
      if (s.dead) return;
      if (!r.ok && r.hide) {
        var box = s.el.querySelector(".ask");
        if (box) U.set(box, h`<p class="notice">${OFF_TEXT}</p>`);
        return;
      }
      setBusy(s, false);
      if (!r.ok) {
        if (r.code === "busy") return;
        if (r.code === "refused" && replace) { list.pop(); paintLog(s); }
        showErr(s, r.message);
        return;
      }
      var v = Core.validAsk(r.data, req.sent, s.manifest);
      if (!v.ok) { showErr(s, Core.message("invalid_json").text); return; }
      var turn = {
        q: question, label: label || "", view: v.data,
        a: JSON.stringify({status: v.data.status, answer: v.data.answer, support: [], missing: v.data.missing, see: v.data.see})
      };
      if (replace) list[list.length - 1] = turn; else list.push(turn);
      if (list.length > 12) list.splice(0, list.length - 12);
      if (!label) {
        var ta = s.el.querySelector(".ask-in");
        ta.value = "";
        draft("");
        paintCount(s);
      }
      paintLog(s);
    });
  }

  function paintCount(s) {
    var ta = s.el.querySelector(".ask-in");
    s.el.querySelector(".ask-count").textContent = ta.value.length + " / " + Core.CAPS.question;
    var send = s.el.querySelector("[data-act=ask-send]");
    send.disabled = !ta.value.trim();
  }

  function wire(s) {
    var el = s.el;
    U.on(el, "submit", ".ask-form", function (ev) {
      ev.preventDefault();
      ask(s, el.querySelector(".ask-in").value, "", false);
    });
    U.on(el, "input", ".ask-in", function (ev, ta) {
      paintCount(s);
      draft(ta.value);
    });
    U.on(el, "keydown", ".ask-in", function (ev, ta) {
      if (ev.key === "Enter" && (ev.metaKey || ev.ctrlKey)) { ev.preventDefault(); ask(s, ta.value, "", false); }
    });
    U.on(el, "click", "[data-act]", function (ev, btn) {
      var act = btn.getAttribute("data-act");
      var turns = hist[s.key] || [];
      if (act === "ask-fixed") {
        var f = FIXED[Number(btn.getAttribute("data-i"))];
        if (f) ask(s, f[1], f[0], false);
      } else if (act === "ai-stop") {
        AI.stop();
      } else if (act === "ask-careful") {
        var last = turns[turns.length - 1];
        if (last) ask(s, last.q, last.label, true);
      } else if (act === "ask-quote") {
        var t = turns[Number(btn.getAttribute("data-turn"))];
        var sup = t && t.view.support[Number(btn.getAttribute("data-i"))];
        if (sup) showQuote(s.sid, sup.quote);
      } else if (act === "ask-search") {
        var t2 = turns[Number(btn.getAttribute("data-turn"))];
        var text = t2 ? (t2.label ? "" : t2.q) : "";
        if (SAA.Pop) SAA.Pop.closeSheet(true);
        if (SAA.Search) SAA.Search.open(text);
      }
    });
  }

  Ask.open = function (slug, sid) {
    var Content = SAA.Content;
    if (!AI.available()) {
      U.toast(AI.hidden() ? OFF_TEXT : "Claude is not available on this page.");
      return Promise.resolve(false);
    }
    var glossary = Content.glossary().then(function (g) { return g; }, function () { return null; });
    return Promise.all([Content.chapter(slug), Content.manifest(), glossary]).then(function (r) {
      var s = {slug: slug, sid: sid, key: slug + "." + sid, chapter: r[0], manifest: r[1], glossary: r[2], dead: false, el: null};
      var ctx = r[0] ? Core.askContext(s.chapter, slug, sid, s.manifest, s.glossary) : null;
      if (!ctx || !ctx.sent.length) { U.toast("This section has no text to ask about."); return false; }
      s.el = SAA.Pop.sheet(sheetHtml(ctx), {
        label: "Ask about this section",
        onClose: function () { s.dead = true; if (cur === s) cur = null; AI.stop(); }
      });
      if (!s.el) return false;
      cur = s;
      wire(s);
      var ta = s.el.querySelector(".ask-in");
      var kept = draft();
      if (kept) ta.value = String(kept).slice(0, Core.CAPS.question);
      paintCount(s);
      paintLog(s);
      try { ta.focus({preventScroll: true}); } catch (e2) { /* older engines */ }
      return true;
    }, function () {
      U.toast("This section could not be loaded. Check your connection and try again.");
      return false;
    });
  };

  /* For tests and the screenshot state: asks one of the four ready questions in the open sheet. */
  Ask.quick = function (i) {
    if (cur && FIXED[i]) ask(cur, FIXED[i][1], FIXED[i][0], false);
  };

  if (SAA.bus) {
    SAA.bus.on("ai:off", function () {
      if (cur && cur.el) {
        var box = cur.el.querySelector(".ask");
        if (box) U.set(box, h`<p class="notice">${OFF_TEXT}</p>`);
      }
    });
  }

  if (SAA.Test && SAA.Test.register) {
    SAA.Test.register("ask", function (el) {
      var Content = SAA.Content;
      U.set(el, h`<h1 tabindex="-1">Ask about this section</h1><p class="notice">Preview of the Ask sheet.</p>`);
      return Content.manifest().then(function (m) {
        var pick = null;
        arr(m.chapters).forEach(function (c) {
          if (pick || c.status === "planned") return;
          arr(c.sections).forEach(function (r) { if (!pick && r[2] === 2 && r[7] !== "predict") pick = [c.slug, r[0]]; });
        });
        if (!pick) return false;
        var started = false;
        function go() {
          if (started || !AI.available()) return;
          started = true;
          Ask.open(pick[0], pick[1]).then(function (ok) { if (ok) Ask.quick(0); });
        }
        go();
        if (!started) SAA.bus.on("caps", go);
        return true;
      });
    });
  }

})(globalThis.SAA = globalThis.SAA || {});
