/* search-worker.js (owner E). Full-text search over the shards of search/ (one per chapter). Published as assets/search-worker.js.
   Protocol: {t:"aliases", aliases} -> {t:"ready", n};
             {t:"shard", data: <text of search/<slug>.json>} or {t:"shard", docs} -> {t:"added", n} | {t:"skipped", message};
             {t:"q", id, text} -> {t:"r", id, rows} over the shards added so far | {t:"error", message}.
   The index grows with each shard; n is the number of docs so far. The worker never fetches; the page posts the texts. */
(function (G) {
  "use strict";

  if (typeof document !== "undefined") return;   /* a worker file: never runs inside the page script */

  var MAX_ROWS = 30;
  var SNIPPET = 140;
  var KIND_ORDER = {s: 0, g: 1, f: 2, q: 3};

  var docs = [];        /* [route, chapter, heading, kind, text] */
  var post = {};        /* token -> [doc ids], ascending (heading or text) */
  var hpost = {};       /* token -> {doc id: 1} (heading only) */
  var vocab = [];       /* every token */
  var groups = [];      /* alias groups: [[tokens of form 1], [tokens of form 2], ...] */
  var byForm = {};      /* "tokens joined by space" -> [group ids] */
  var ready = false;

  function tokens(text) {
    var m = String(text === null || text === undefined ? "" : text).toLowerCase().match(/[a-z0-9]+/g);
    return m || [];
  }

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function has(o, k) { return Object.prototype.hasOwnProperty.call(o, k); }

  function index(tk, i, head) {
    if (!has(post, tk)) { post[tk] = []; vocab.push(tk); }
    var list = post[tk];
    if (list[list.length - 1] !== i) list.push(i);
    if (head) {
      if (!has(hpost, tk)) hpost[tk] = {};
      hpost[tk][i] = 1;
    }
  }

  /* Appends the docs of one shard to the index. */
  function addDocs(list) {
    for (var k = 0; k < list.length; k++) {
      var d = list[k];
      if (!Array.isArray(d)) continue;
      var i = docs.length, j, words;
      docs.push(d);
      words = tokens(d[2]);
      for (j = 0; j < words.length; j++) index(words[j], i, true);
      words = tokens(d[4]);
      for (j = 0; j < words.length; j++) index(words[j], i, false);
    }
  }

  /* Replaces the alias groups: {"<term id>": ["form", ...]}. */
  function setAliases(aliases) {
    groups = []; byForm = {};
    aliases = aliases && typeof aliases === "object" ? aliases : {};
    Object.keys(aliases).forEach(function (id) {
      var forms = [tokens(id.replace(/-/g, " "))];
      (Array.isArray(aliases[id]) ? aliases[id] : []).forEach(function (f) {
        var t = tokens(f);
        if (t.length) forms.push(t);
      });
      var g = groups.length, keys = {};
      groups.push(forms);
      forms.forEach(function (f) {
        var key = f.join(" ");
        if (has(keys, key)) return;
        keys[key] = 1;
        if (!has(byForm, key)) byForm[key] = [];
        byForm[key].push(g);
      });
    });
  }

  /* True when a and b differ by one insertion, deletion, substitution or swap of neighbours. */
  function oneEdit(a, b) {
    var la = a.length, lb = b.length;
    if (la === lb) {
      var diff = [], i;
      for (i = 0; i < la; i++) if (a.charCodeAt(i) !== b.charCodeAt(i)) { diff.push(i); if (diff.length > 2) return false; }
      if (diff.length === 1) return true;
      return diff.length === 2 && diff[1] === diff[0] + 1 &&
        a.charAt(diff[0]) === b.charAt(diff[1]) && a.charAt(diff[1]) === b.charAt(diff[0]);
    }
    if (Math.abs(la - lb) !== 1) return false;
    var s = la < lb ? a : b, l = la < lb ? b : a, k = 0, skipped = false;
    for (var p = 0; p < l.length; p++) {
      if (k < s.length && s.charCodeAt(k) === l.charCodeAt(p)) k++;
      else if (skipped) return false;
      else skipped = true;
    }
    return true;
  }

  /* The docs that match one query term: {doc id: {w: weight, tok: matched token}}. */
  function matchTerm(term) {
    var out = {}, i;
    function add(tok, w) {
      var list = post[tok];
      if (!list) return;
      var heads = has(hpost, tok) ? hpost[tok] : null;
      for (var k = 0; k < list.length; k++) {
        var d = list[k];
        var inHead = !!(heads && heads[d]);
        if (!has(out, d)) out[d] = {w: w, tok: tok, h: inHead};
        else {
          if (out[d].w < w) { out[d].w = w; out[d].tok = tok; }
          if (inHead) out[d].h = true;
        }
      }
    }
    if (has(post, term)) add(term, 3);
    if (term.length >= 2) {
      for (i = 0; i < vocab.length; i++) {
        var v = vocab[i];
        if (v.length > term.length && v.lastIndexOf(term, 0) === 0) add(v, 2);
      }
    }
    if (term.length >= 5 && /^[a-z]+$/.test(term)) {
      for (i = 0; i < vocab.length; i++) {
        var c = vocab[i];
        if (c !== term && Math.abs(c.length - term.length) <= 1 && c.charCodeAt(0) === term.charCodeAt(0) && oneEdit(term, c)) add(c, 1);
      }
    }
    return out;
  }

  /* The docs that hold every token of one alias form. */
  function matchForm(form) {
    var acc = null;
    for (var i = 0; i < form.length; i++) {
      var list = post[form[i]] || [];
      var next = {};
      for (var k = 0; k < list.length; k++) if (acc === null || has(acc, list[k])) next[list[k]] = 1;
      acc = next;
    }
    return acc || {};
  }

  /* Alias expansion: other forms of every group that has the key as one of its forms. */
  function viaAlias(key, out, tok) {
    var ids = byForm[key];
    if (!ids) return;
    ids.forEach(function (g) {
      groups[g].forEach(function (form) {
        if (form.join(" ") === key) return;
        var hit = matchForm(form);
        Object.keys(hit).forEach(function (d) {
          if (!has(out, d)) out[d] = {w: 2, tok: form[0] || tok, h: false};
        });
      });
    });
  }

  function snippet(doc, toks) {
    var text = String(doc[4] || "");
    var low = text.toLowerCase();
    var at = -1, len = 0;
    for (var i = 0; i < toks.length && at < 0; i++) {
      var re = new RegExp("(^|[^a-z0-9])" + toks[i].replace(/[^a-z0-9]/g, ""), "");
      var m = re.exec(low);
      if (m) { at = m.index + m[1].length; len = toks[i].length; }
    }
    if (at < 0) {
      var head = text.slice(0, SNIPPET);
      return esc(head) + (text.length > SNIPPET ? "…" : "");
    }
    var end = at + len;
    while (end < low.length && /[a-z0-9]/.test(low.charAt(end))) end++;
    var from = Math.max(0, at - Math.floor((SNIPPET - (end - at)) / 2));
    if (from > 0) {
      var sp = text.indexOf(" ", from);
      if (sp !== -1 && sp < at) from = sp + 1;
    }
    var to = Math.min(text.length, from + SNIPPET);
    return (from > 0 ? "…" : "") + esc(text.slice(from, at)) + "<mark>" + esc(text.slice(at, end)) + "</mark>" +
      esc(text.slice(end, Math.max(end, to))) + (to < text.length ? "…" : "");
  }

  function query(text) {
    var terms = tokens(text);
    var uniq = [], seen = {};
    terms.forEach(function (t) { if (!has(seen, t)) { seen[t] = 1; uniq.push(t); } });
    uniq = uniq.slice(0, 8);
    if (!uniq.length) return [];

    var score = {};   /* doc -> {n, w, h, toks} */
    uniq.forEach(function (term) {
      var hit = matchTerm(term);
      viaAlias(term, hit, term);
      Object.keys(hit).forEach(function (d) {
        var s = score[d] || (score[d] = {n: 0, w: 0, h: 0, toks: []});
        s.n += 1;
        s.w += hit[d].w;
        s.toks.push(hit[d].tok);
        if (hit[d].h) s.h += 1;
      });
    });
    if (uniq.length > 1) {
      var whole = {};
      viaAlias(uniq.join(" "), whole, uniq[0]);
      Object.keys(whole).forEach(function (d) {
        var s = score[d] || (score[d] = {n: 0, w: 0, h: 0, toks: []});
        if (s.n < uniq.length) { s.n = uniq.length; s.w += 2 * uniq.length; s.toks.push(whole[d].tok); }
      });
    }

    var ids = Object.keys(score).map(Number);
    ids.sort(function (a, b) {
      var x = score[a], y = score[b];
      if (x.n !== y.n) return y.n - x.n;
      if (x.h !== y.h) return y.h - x.h;
      var ka = KIND_ORDER[docs[a][3]], kb = KIND_ORDER[docs[b][3]];
      ka = ka === undefined ? 9 : ka; kb = kb === undefined ? 9 : kb;
      if (ka !== kb) return ka - kb;
      if (x.w !== y.w) return y.w - x.w;
      return a - b;
    });
    return ids.slice(0, MAX_ROWS).map(function (d) {
      var doc = docs[d];
      return {route: String(doc[0]), chapter: String(doc[1] || ""), heading: String(doc[2] || ""),
              kind: String(doc[3] || "s"), snippet: snippet(doc, score[d].toks)};
    });
  }

  function send(msg) { G.postMessage(msg); }

  function message(e) { return String(e && e.message ? e.message : e); }

  G.onmessage = function (ev) {
    var m = ev && ev.data ? ev.data : {};
    if (m.t === "aliases") {
      setAliases(m.aliases);
      ready = true;
      send({t: "ready", n: docs.length});
    } else if (m.t === "shard") {
      var shard;
      try { shard = typeof m.data === "string" ? JSON.parse(m.data) : m; }
      catch (e) { send({t: "skipped", message: message(e)}); return; }
      if (!shard || !Array.isArray(shard.docs)) { send({t: "skipped", message: "not a search shard"}); return; }
      addDocs(shard.docs);
      ready = true;
      send({t: "added", n: docs.length});
    } else if (m.t === "q") {
      if (!ready) { send({t: "error", message: "not loaded"}); return; }
      try { send({t: "r", id: m.id, rows: query(m.text)}); }
      catch (e2) { send({t: "error", message: message(e2)}); }
    }
  };

})(typeof self !== "undefined" ? self : globalThis);
