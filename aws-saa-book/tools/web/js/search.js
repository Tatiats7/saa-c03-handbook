/* search.js (owner E). Jump-to over titles, headings and glossary; full text in a worker. */
(function (SAA) {
  "use strict";

  var U = SAA.U;
  var h = U.h;
  var Search = SAA.Search = SAA.Search || {};

  var JUMP_ROWS = 12;
  var KIND_WORD = {chapter: "Chapter", section: "Section", term: "Glossary", s: "Text", g: "Glossary", f: "Fact", q: "Question"};
  var NO_FULL = "Full-text search is not available right now.";

  /* worker state: "idle" | "loading" | "ready" | "failed"; done of total shards are in the worker's index */
  var W = {state: "idle", worker: null, seq: 0, waiting: null, done: 0, total: 0};
  var open = null;   /* {el, text} while the sheet shows */

  /* ---------- jump-to (no worker) ---------- */

  function rank(title, needle) {
    var t = U.norm(title);
    if (!t) return 0;
    if (t === needle) return 4;
    if (t.lastIndexOf(needle, 0) === 0) return 3;
    var at = t.indexOf(needle);
    if (at === -1) return 0;
    return /[^a-z0-9]/.test(t.charAt(at - 1)) ? 2 : 1;
  }

  /* rows: [{route, title, sub, kind}], best first. manifest: optional (default SAA.state.manifest). */
  Search.jump = function (text, manifest) {
    var needle = U.norm(text);
    var m = manifest || (SAA.state && SAA.state.manifest) || null;
    if (!needle || !m) return [];
    var rows = [];
    function add(score, order, row) { row.score = score; row.order = order; row.n = rows.length; rows.push(row); }

    (m.chapters || []).forEach(function (c) {
      var r = rank(c.title, needle);
      if (!r && c.id && U.norm(c.id) === needle) r = 3;
      if (r) {
        add(r, 0, {route: "ch." + c.slug, title: c.title, kind: "chapter",
                   sub: c.status === "planned" ? "Not written yet" : (c.id ? "Chapter " + c.id : "")});
      }
      (c.sections || []).forEach(function (s) {
        var rs = rank(s[5], needle);
        if (rs) add(rs, 2, {route: "ch." + c.slug + "." + s[1] + "." + s[0], title: s[5], kind: "section", sub: c.title});
      });
    });
    (m.terms || []).forEach(function (t) {
      var r = rank(t[1], needle);
      if (r) add(r, 1, {route: "glossary." + t[0], title: t[1], kind: "term", sub: ""});
    });

    rows.sort(function (a, b) {
      if (a.score !== b.score) return b.score - a.score;
      if (a.order !== b.order) return a.order - b.order;
      if (a.title.length !== b.title.length) return a.title.length - b.title.length;
      return a.n - b.n;
    });
    return rows.slice(0, JUMP_ROWS).map(function (r) {
      return {route: r.route, title: r.title, sub: r.sub, kind: r.kind};
    });
  };

  /* ---------- the worker ---------- */

  function failWorker() {
    W.state = "failed";
    if (W.worker) { try { W.worker.terminate(); } catch (e) { /* already gone */ } }
    W.worker = null;
    W.waiting = null;
    paintFull(null);
  }

  /* One more shard is in the index (or was skipped): ask the open query again over the larger index. */
  function shardDone() {
    W.done += 1;
    if (W.state === "ready" && open && U.norm(open.text).length >= 3) post(open.text);
  }

  function onMessage(ev) {
    var m = ev && ev.data ? ev.data : {};
    if (m.t === "ready") {
      W.state = "ready";
      if (W.waiting) { var w = W.waiting; W.waiting = null; post(w); }
    } else if (m.t === "added" || m.t === "skipped") {
      shardDone();
    } else if (m.t === "r") {
      if (m.id === W.seq) paintFull(Array.isArray(m.rows) ? m.rows : []);
    } else if (m.t === "error") {
      failWorker();
    }
  }

  function post(text) {
    W.seq += 1;
    try { W.worker.postMessage({t: "q", id: W.seq, text: text}); }
    catch (e) { failWorker(); }
  }

  function startWorker() {
    W.state = "loading";
    try {
      var single = !!(SAA.state && SAA.state.single);
      var url = "assets/search-worker.js";
      if (single) {
        var src = document.getElementById("saa-worker");
        if (!src || !src.textContent) { failWorker(); return; }
        url = URL.createObjectURL(new Blob([src.textContent], {type: "text/javascript"}));
      }
      W.worker = new Worker(url);
      W.worker.onmessage = onMessage;
      W.worker.onerror = function (ev) { if (ev && ev.preventDefault) ev.preventDefault(); failWorker(); };
    } catch (e) { failWorker(); return; }
    SAA.Content.text("search/index.json").then(function (text) {
      if (W.state !== "loading" || !W.worker) return;
      var index = JSON.parse(text);
      var shards = Array.isArray(index.shards) ? index.shards : [];
      W.total = shards.length;
      W.worker.postMessage({t: "aliases", aliases: index.aliases || {}});
      /* every shard is fetched at once; each is posted in the order of the index, so the doc ids are stable */
      var texts = shards.map(function (row) {
        return SAA.Content.text(String(row.path)).then(null, function () { return null; });
      });
      texts.reduce(function (chain, got) {
        return chain.then(function () { return got; }).then(function (shard) {
          if (W.state === "failed" || !W.worker) return;
          if (shard === null) { shardDone(); return; }      /* a shard that cannot be loaded is left out */
          try { W.worker.postMessage({t: "shard", data: shard}); }
          catch (e) { failWorker(); }
        });
      }, Promise.resolve());
    }).then(null, function () { failWorker(); });
  }

  function fullText(text) {
    if (W.state === "failed") { paintFull(null); return; }
    if (W.state === "idle") startWorker();
    if (W.state === "ready") post(text);
    else if (W.state === "loading") { W.waiting = text; paintFull("wait"); }
  }

  /* ---------- the sheet ---------- */

  function rowHtml(route, kind, title, sub, snippet) {
    return h`<li><a class="srch-row" href="#${route}"><span class="srch-k mono">${KIND_WORD[kind] || "Text"}</span><span class="srch-t"><span class="srch-hit">${title}</span>${sub ? h` <span class="srch-sub">${sub}</span>` : ""}${snippet ? h`<span class="srch-snip">${snippet}</span>` : ""}</span></a></li>`;
  }

  function paintJump(text) {
    if (!open) return;
    var box = open.el.querySelector(".srch-jump");
    var rows = Search.jump(text);
    if (!U.norm(text)) { U.set(box, h`<p class="srch-empty">Type a service, a term or a heading.</p>`); return; }
    if (!rows.length) {
      U.set(box, h`<p class="srch-empty">${SAA.state && SAA.state.manifest ? "No title, heading or glossary term matches." : "The contents list is still loading."}</p>`);
      return;
    }
    U.set(box, h`<h3 class="srch-h">Go to</h3><ul class="srch-list">${rows.map(function (r) {
      return rowHtml(r.route, r.kind, r.title, r.sub, "");
    })}</ul>`);
  }

  /* rows: array of worker rows; "wait" while the index loads; null when full text is unavailable. */
  function paintFull(rows) {
    if (!open) return;
    var box = open.el.querySelector(".srch-full");
    if (!box) return;
    if (U.norm(open.text).length < 3) { U.set(box, null); return; }
    if (rows === null) { U.set(box, h`<p class="srch-empty">${NO_FULL}</p>`); return; }
    if (rows === "wait") { U.set(box, h`<p class="srch-empty" role="status">Searching the text…</p>`); return; }
    var loading = W.done < W.total;
    var more = loading ? h`<p class="srch-empty">Indexing ${W.done} of ${W.total} chapters…</p>` : "";
    if (!rows.length) { U.set(box, h`<h3 class="srch-h">In the text</h3>${more}<p class="srch-empty">No text matches.</p>`); return; }
    U.set(box, h`<h3 class="srch-h">In the text</h3>${more}<ul class="srch-list">${rows.map(function (r) {
      /* the snippet is escaped by the worker; it is the only worker output passed to U.raw */
      return rowHtml(r.route, r.kind, r.heading || r.chapter, r.heading ? r.chapter : "", U.raw(String(r.snippet || "")));
    })}</ul>`);
    /* announced once per query text, and once more when the last shard is in */
    if (!loading || open.said !== open.text) U.announce(rows.length + " results in the text.");
    open.said = open.text;
  }

  var runFull = U.debounce(function (text) {
    if (open && open.text === text) fullText(text);
  }, 160);

  function onInput(text) {
    if (!open) return;
    open.text = text;
    paintJump(text);
    if (U.norm(text).length >= 3) runFull(text);
    else paintFull([]);
  }

  function moveFocus(el, from, step) {
    var rows = Array.prototype.slice.call(el.querySelectorAll(".srch-row"));
    if (!rows.length) return;
    var i = rows.indexOf(from);
    var next = i === -1 ? (step > 0 ? 0 : rows.length - 1) : i + step;
    if (next < 0) { el.querySelector(".srch-in").focus(); return; }
    if (next >= rows.length) next = rows.length - 1;
    rows[next].focus();
  }

  Search.open = function (prefill) {
    if (!SAA.Pop) return;
    var text = typeof prefill === "string" ? prefill : "";
    var el = SAA.Pop.sheet(h`<div class="srch">
      <form class="srch-form" role="search" novalidate>
        <label class="srch-label vh" for="srch-q">Search the book</label>
        <input class="srch-in" id="srch-q" type="search" autocomplete="off" autocapitalize="off" spellcheck="false" maxlength="80" placeholder="NAT gateway, least privilege, S3 lifecycle">
      </form>
      <div class="srch-jump" aria-live="polite"></div>
      <div class="srch-full"></div>
    </div>`, {label: "Search", onClose: function () { open = null; }});
    if (!el) return;
    open = {el: el, text: ""};
    var input = el.querySelector(".srch-in");
    U.on(el, "input", ".srch-in", function () { onInput(input.value); });
    U.on(el, "submit", ".srch-form", function (ev) {
      ev.preventDefault();
      var first = el.querySelector(".srch-row");
      if (first) first.click();
    });
    U.on(el, "keydown", ".srch", function (ev) {
      if (ev.key !== "ArrowDown" && ev.key !== "ArrowUp") return;
      var from = ev.target && ev.target.closest ? ev.target.closest(".srch-row") : null;
      if (!from && ev.target !== input) return;
      ev.preventDefault();
      moveFocus(el, from, ev.key === "ArrowDown" ? 1 : -1);
    });
    input.value = text.slice(0, 80);
    onInput(input.value);
    try { input.focus({preventScroll: true}); } catch (e) { /* older engines */ }
    if (!(SAA.state && SAA.state.manifest) && SAA.Content) {
      SAA.Content.manifest().then(function () { if (open) paintJump(open.text); }, function () { /* jump-to stays empty */ });
    }
  };

  /* ---------- wiring ---------- */

  if (typeof document !== "undefined") {
    U.on(document, "keydown", null, function (ev) {
      if (ev.key !== "/" || ev.metaKey || ev.ctrlKey || ev.altKey || ev.defaultPrevented) return;
      var t = ev.target;
      if (t && t.nodeType === 1 && (/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName) || t.isContentEditable)) return;
      if (SAA.Pop && SAA.Pop.sheetOpen && SAA.Pop.sheetOpen()) return;
      ev.preventDefault();
      Search.open();
    });
  }

  if (SAA.Test && SAA.Test.register) {
    SAA.Test.register("search", function (el) {
      U.set(el, h`<h1 tabindex="-1">Search</h1><p class="notice">Preview of the search sheet.</p>`);
      return SAA.Content.manifest().then(function (m) {
        var word = "";
        (m.chapters || []).forEach(function (c) {
          if (!word && c.status !== "planned" && c.sections && c.sections.length) word = String(c.sections[0][5] || c.title).split(/\s+/)[0];
        });
        Search.open(word || "s3");
      });
    });
  }

})(globalThis.SAA = globalThis.SAA || {});
