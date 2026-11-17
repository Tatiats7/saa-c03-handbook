/* cards.js (owner C): quick card review without scheduling, ARCHITECTURE.md section 7.6.
   View cards; Cards.render(el, card, {flipped, facts}). */
(function (SAA) {
  "use strict";

  var U = SAA.U, h = U.h, QV = SAA.QView;
  var CLOZE = /\{\{c\d+::(.*?)(?:::.*?)?\}\}/g;
  var KIND = { number: "Number", cannot: "Can or cannot", decide: "Decision", trap: "Trap", word: "Exam word", say: "Say it", compare: "Compare" };

  function kindWord(card) {
    var k = KIND[card.type] || (card.type ? String(card.type).charAt(0).toUpperCase() + String(card.type).slice(1) : "Card");
    return k + (card.deck && card.deck !== "core" ? " · " + card.deck : "");
  }

  /* The front with each cloze as a blank (or filled and marked after the flip). */
  function cloze(text, filled) {
    var parts = [], at = 0, m;
    text = String(text || "");
    CLOZE.lastIndex = 0;
    while ((m = CLOZE.exec(text))) {
      if (m.index > at) parts.push(h`${text.slice(at, m.index)}`);
      parts.push(filled ? h`<mark class="fc-fill">${m[1]}</mark>` : h`<span class="fc-blank"><span class="vh">blank</span><span aria-hidden="true">_____</span></span>`);
      at = m.index + m[0].length;
    }
    if (at < text.length) parts.push(h`${text.slice(at)}`);
    return parts;
  }

  function hasCloze(card) { CLOZE.lastIndex = 0; return CLOZE.test(String(card.front || "")); }

  function render(el, card, opts) {
    var flipped, sec, isCloze = hasCloze(card), back;
    opts = opts || {};
    flipped = !!opts.flipped;
    if (opts.facts && SAA.Evidence && SAA.Evidence.register) SAA.Evidence.register(opts.facts);
    sec = flipped ? QV.secHref(card.sec) : null;
    back = !flipped ? null : h`<div class="fc-back">
      <p class="fc-l">Answer</p>
      ${isCloze ? h`<p class="fc-a">${cloze(card.front, true)}</p>` : null}
      ${card.back ? h`<p class="fc-a">${card.back}</p>` : null}
      ${card.extra_h ? h`<p class="fc-extra">${U.raw(card.extra_h)}</p>` : null}
      ${card.changed ? h`<p class="fc-chg"><span class="pill note">Changed recently</span> Older questions may assume the old value.</p>` : null}
      ${sec ? h`<p class="fc-link"><a class="xr" href="${sec}">Review: ${QV.secTitle(card.sec)}</a></p>` : null}
    </div>`;
    U.set(el, h`<div class="fc${flipped ? " is-flipped" : ""}" data-card="${card.id}">
      <p class="eyebrow fc-kind">${kindWord(card)}</p>
      <div class="fc-front"><p>${isCloze ? cloze(card.front, false) : card.front}</p></div>
      ${back}
    </div>`);
  }

  /* ---------- the round ---------- */

  function round(root, slug, data, startFlipped) {
    var cards = ((data && data.cards) || []).slice(), facts = (data && data.facts) || {}, title = QV.chapterTitle(slug);
    var queue, again = {}, i = 0, known = 0, flipped = !!startFlipped, total;
    cards = cards.filter(function (c) { return c.deck === "core"; }).concat(cards.filter(function (c) { return c.deck !== "core"; }));
    total = cards.length;
    queue = cards.slice();

    if (!total) {
      U.set(root, h`<div class="fcv"><h1 tabindex="-1">Cards: ${title}</h1><p class="notice">This chapter has no cards yet.</p>
        <p><a class="btn" href="${"#ch." + slug}">Back to the chapter</a></p></div>`);
      return;
    }

    function frame() {
      U.set(root, h`<div class="fcv">
        <h1 tabindex="-1">Cards: ${title}</h1>
        <p class="fc-prog mono" role="status"></p>
        <div class="fc-slot"></div>
        <p class="fc-btns"></p>
        <p class="fc-anki">For daily review with spacing, use the Anki deck (<a class="xr" href="#files">Get files</a>).</p>
      </div>`);
      var r = root.firstElementChild;
      U.on(r, "click", "[data-act=\"fc-flip\"]", function () { flipped = true; card(true); });
      U.on(r, "click", "[data-act=\"fc-yes\"]", function () { answer(true); });
      U.on(r, "click", "[data-act=\"fc-no\"]", function () { answer(false); });
      U.on(r, "click", "[data-act=\"fc-again\"]", function () { round(root, slug, data, false); focus(root, "h1"); });
    }

    function focus(scope, sel) {
      var el = scope.querySelector(sel);
      if (el) { try { el.focus({ preventScroll: true }); } catch (e) { /* older engines */ } }
    }

    function card(moveFocus) {
      var c = queue[i];
      root.querySelector(".fc-prog").textContent = "Card " + (i + 1) + " of " + queue.length + (queue.length > total ? " (" + (queue.length - total) + " again)" : "");
      render(root.querySelector(".fc-slot"), c, { flipped: flipped, facts: facts });
      U.set(root.querySelector(".fc-btns"), flipped
        ? h`<button type="button" class="btn primary" data-act="fc-yes">I knew it</button> <button type="button" class="btn" data-act="fc-no">Not yet</button>`
        : h`<button type="button" class="btn primary" data-act="fc-flip">Show answer</button>`);
      if (moveFocus) focus(root, flipped ? "[data-act=\"fc-yes\"]" : "[data-act=\"fc-flip\"]");
    }

    function answer(yes) {
      var c = queue[i];
      if (yes) { if (!again[c.id]) known++; }
      else if (!again[c.id]) { again[c.id] = 1; queue.push(c); }
      i++;
      flipped = false;
      if (i < queue.length) { card(true); return; }
      if (SAA.Store && SAA.Store.stamp) SAA.Store.stamp("progress", ["cards", slug], true);
      U.set(root.querySelector(".fc-slot"), h`<div class="fc fc-done"><p class="eyebrow">Round finished</p>
        <p>You knew ${known} of ${total} ${total === 1 ? "card" : "cards"} at the first try.</p></div>`);
      root.querySelector(".fc-prog").textContent = "";
      U.set(root.querySelector(".fc-btns"), h`<button type="button" class="btn" data-act="fc-again">Start again</button> <a class="btn primary" href="${"#quiz." + slug}">Go to the quiz</a> <a class="btn quiet" href="${"#ch." + slug}">Back to the chapter</a>`);
      U.announce("Round finished. You knew " + known + " of " + total + " cards at the first try.");
      focus(root, "[data-act=\"fc-again\"]");
    }

    frame();
    card(false);
  }

  var view = {
    mount: function (el, args) {
      var slug = args[0] || "", root = QV.root(el, "pv");
      return SAA.Content.data(slug).then(function (data) { round(root, slug, data, false); });
    },
    title: function (args) { return "Cards: " + QV.chapterTitle(args[0] || ""); }
  };

  function shot(el) {
    var root = QV.root(el, "pv");
    if (SAA.Store && SAA.Store.reset) SAA.Store.reset();
    return SAA.Content.manifest().then(function (m) {
      var hit = null;
      (m.chapters || []).forEach(function (c) { if (!hit && c.status !== "planned" && c.counts && c.counts.cards > 0) hit = c; });
      if (!hit) { round(root, "", null, false); return null; }
      return SAA.Content.data(hit.slug).then(function (data) { round(root, hit.slug, data, true); });
    });
  }

  SAA.Cards = { render: render };

  if (SAA.Router) SAA.Router.register("cards", view);
  if (SAA.Test && SAA.Test.register) SAA.Test.register("cards", shot);
})(globalThis.SAA = globalThis.SAA || {});
