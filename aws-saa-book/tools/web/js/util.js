/* util.js (owner B). Pure except U.on, U.ls, U.toast, U.announce, U.copy, U.set. */
(function (SAA) {
  "use strict";

  var U = SAA.U = SAA.U || {};
  var Test = SAA.Test = SAA.Test || {};
  if (!Test.states) Test.states = {};
  if (Test.clock === undefined) Test.clock = null;
  Test.register = function (name, fn) { Test.states[name] = fn; };

  /* ---------- safe HTML ---------- */

  var ESC = {"&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#39;"};

  U.esc = function (s) {
    if (s === null || s === undefined) return "";
    return String(s).replace(/[&<>"']/g, function (c) { return ESC[c]; });
  };

  function SafeHtml(s) { this.s = s; }
  SafeHtml.prototype.__safe = true;
  SafeHtml.prototype.toString = function () { return this.s; };

  function isSafe(v) { return !!v && typeof v === "object" && v.__safe === true && typeof v.s === "string"; }

  U.raw = function (string) {
    return new SafeHtml(string === null || string === undefined ? "" : String(string));
  };

  function part(v) {
    if (v === null || v === undefined || v === false) return "";
    if (isSafe(v)) return v.s;
    if (Array.isArray(v)) {
      var out = "";
      for (var i = 0; i < v.length; i++) out += part(v[i]);
      return out;
    }
    return U.esc(v);
  }

  U.h = function (strings) {
    var out = strings[0];
    for (var i = 1; i < strings.length; i++) out += part(arguments[i]) + strings[i];
    return new SafeHtml(out);
  };

  U.isSafe = isSafe;

  /* Joins a list of SafeHtml values with a SafeHtml or plain-text separator. */
  U.join = function (list, sep) {
    var s = part(sep === undefined ? "" : sep);
    var out = [];
    for (var i = 0; i < list.length; i++) {
      var p = part(list[i]);
      if (p) out.push(p);
    }
    return new SafeHtml(out.join(s));
  };

  U.set = function (el, safe) {
    if (!el) return;
    if (safe === null || safe === undefined) { el.textContent = ""; return; }
    if (!isSafe(safe) && !(Array.isArray(safe) && safe.every(isSafe))) {
      throw new Error("U.set needs SafeHtml (use U.h)");
    }
    el.innerHTML = part(safe);
  };

  /* ---------- time ---------- */

  U.nowMs = function () {
    if (typeof Test.clock === "function") return Test.clock();
    return Date.now();
  };
  U.now = function () { return Math.floor(U.nowMs() / 1000); };

  U.day = function (ms) {
    var t = ms === undefined || ms === null ? U.nowMs() : ms;
    var offsetMin = new Date(t).getTimezoneOffset();
    return Math.floor((t - offsetMin * 60000) / 86400000);
  };

  function two(n) { return n < 10 ? "0" + n : String(n); }

  U.fmtClock = function (sec) {
    sec = Math.max(0, Math.floor(sec || 0));
    var h = Math.floor(sec / 3600), m = Math.floor((sec % 3600) / 60), s = sec % 60;
    return h ? h + ":" + two(m) + ":" + two(s) : m + ":" + two(s);
  };

  U.fmtMin = function (n) {
    n = Math.max(0, Math.round(n || 0));
    if (n < 180) return n + " min";
    var h = Math.floor(n / 60), m = n % 60;
    return m ? h + " h " + m + " min" : h + " h";
  };

  /* ---------- small helpers ---------- */

  U.bytes = function (s) {
    s = String(s === null || s === undefined ? "" : s);
    var n = 0;
    for (var i = 0; i < s.length; i++) {
      var c = s.charCodeAt(i);
      if (c < 0x80) n += 1;
      else if (c < 0x800) n += 2;
      else if (c >= 0xD800 && c <= 0xDBFF && i + 1 < s.length &&
               s.charCodeAt(i + 1) >= 0xDC00 && s.charCodeAt(i + 1) <= 0xDFFF) { n += 4; i++; }
      else n += 3;
    }
    return n;
  };

  U.debounce = function (fn, ms) {
    var timer = null;
    function run() {
      var self = this, args = arguments;
      if (timer) clearTimeout(timer);
      timer = setTimeout(function () { timer = null; fn.apply(self, args); }, ms);
    }
    run.cancel = function () { if (timer) clearTimeout(timer); timer = null; };
    return run;
  };

  U.clone = function (o) {
    return o === undefined ? undefined : JSON.parse(JSON.stringify(o));
  };

  var uidCount = 0;
  U.uid = function (prefix) {
    uidCount = (uidCount + 1) % 1296;
    var r = Math.floor(Math.random() * 1679616).toString(36);
    return (prefix ? prefix + "-" : "") + U.nowMs().toString(36) + "-" + r + uidCount.toString(36);
  };

  U.rng = function (seed) {
    var a = 0;
    if (typeof seed === "number") a = seed >>> 0;
    else {
      var s = String(seed);
      a = 2166136261;
      for (var i = 0; i < s.length; i++) { a ^= s.charCodeAt(i); a = Math.imul(a, 16777619); }
      a >>>= 0;
    }
    return function () {
      a = (a + 0x6D2B79F5) >>> 0;
      var t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  };

  U.shuffle = function (arr, rng) {
    var out = arr.slice(), rand = rng || Math.random;
    for (var i = out.length - 1; i > 0; i--) {
      var j = Math.floor(rand() * (i + 1));
      var t = out[i]; out[i] = out[j]; out[j] = t;
    }
    return out;
  };

  U.norm = function (s) {
    return String(s === null || s === undefined ? "" : s)
      .replace(/[‘’‚′]/g, "'")
      .replace(/[“”„″]/g, "\"")
      .replace(/\s+/g, " ")
      .trim()
      .toLowerCase();
  };

  /* ---------- blueprint strip ---------- */

  U.bstrip = function (domains, opts) {
    opts = opts || {};
    domains = domains || [];
    var gate = opts.gate || (SAA.state && SAA.state.cfg && SAA.state.cfg.gate) || null;
    var on = opts.on || null, pct = opts.pct || null;
    var words = [], segs = [];
    for (var i = 0; i < domains.length; i++) {
      var d = domains[i], cls = "bstrip-s", text = "D" + d.id, word = "";
      if (on) {
        var isOn = on.indexOf(d.id) !== -1;
        if (isOn) cls += " is-on";
        word = isOn ? "covered by this chapter" : "not covered by this chapter";
      } else if (pct) {
        var p = pct[d.id];
        if (p === undefined || p === null) p = pct["d" + d.id];
        if (p === undefined || p === null) word = "no answers yet";
        else {
          p = Math.round(p);
          text += " " + p + "%";
          var state = "";
          if (gate) state = p >= gate.strong ? "good" : (p >= gate.domainMin ? "warn" : "bad");
          if (state) cls += " is-" + state;
          word = p + " percent" + (state === "good" ? ", strong" : state === "warn" ? ", close" : state === "bad" ? ", weak" : "");
        }
      } else {
        word = d.weight + " percent of the exam";
      }
      words.push("Domain " + d.id + ", " + d.title + ": " + word);
      /* the short name (Secure, Resilient, Performing, Cost) is drawn by CSS from 760px */
      var short = String(d.title || "").replace(/^Design\s+/, "").split(/\s+/)[0].replace(/^High-/, "").split("-")[0];
      segs.push(U.h`<span class="${cls}" style="flex-grow:${Number(d.weight) || 1}" data-d="${d.id}" data-n="${short}" title="${d.title}">${text}</span>`);
    }
    return U.h`<div class="bstrip" role="img" aria-label="${"Exam domains. " + words.join(". ") + "."}">${segs}</div>`;
  };

  /* ---------- event bus ---------- */

  var listeners = {};
  var bus = SAA.bus = SAA.bus || {};
  bus.on = function (name, fn) { (listeners[name] = listeners[name] || []).push(fn); return fn; };
  bus.off = function (name, fn) {
    var list = listeners[name];
    if (!list) return;
    var i = list.indexOf(fn);
    if (i !== -1) list.splice(i, 1);
  };
  bus.emit = function (name, detail) {
    var list = (listeners[name] || []).slice();
    for (var i = 0; i < list.length; i++) {
      try { list[i](detail); } catch (e) {
        if (typeof console !== "undefined") console.error("bus " + name, e);
      }
    }
  };

  /* ---------- DOM helpers (not pure) ---------- */

  /* Delegated listener. Returns a function that removes it. fn(event, matchedElement). */
  U.on = function (root, type, selector, fn) {
    if (!root) return function () {};
    function handler(ev) {
      var t = ev.target;
      if (t && t.nodeType !== 1) t = t.parentElement;
      var hit = selector ? (t && t.closest ? t.closest(selector) : null) : root;
      if (!hit || (selector && !root.contains(hit))) return;
      fn(ev, hit);
    }
    var capture = type === "focus" || type === "blur" || type === "toggle" || type === "scroll";
    root.addEventListener(type, handler, capture);
    return function () { root.removeEventListener(type, handler, capture); };
  };

  U.ls = {
    get: function (key) {
      try {
        var v = globalThis.localStorage.getItem(key);
        return v === null || v === undefined ? null : JSON.parse(v);
      } catch (e) { return null; }
    },
    set: function (key, value) {
      try {
        if (value === null || value === undefined) globalThis.localStorage.removeItem(key);
        else globalThis.localStorage.setItem(key, JSON.stringify(value));
        return true;
      } catch (e) { return false; }
    }
  };

  var toastTimer = null;
  U.toast = function (text) {
    var el = document.getElementById("saa-toast");
    if (!el) return;
    el.textContent = text;
    el.hidden = false;
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.hidden = true; el.textContent = ""; }, 3200);
  };

  U.announce = function (text) {
    var el = document.getElementById("saa-live");
    if (!el) return;
    el.textContent = "";
    setTimeout(function () { el.textContent = text; }, 30);
  };

  U.copy = function (text) {
    try {
      if (globalThis.navigator && navigator.clipboard && navigator.clipboard.writeText) {
        return navigator.clipboard.writeText(String(text)).then(
          function () { return true; },
          function () { return false; });
      }
    } catch (e) { /* fall through */ }
    return Promise.resolve(false);
  };

  /* Selects the text of an element, the fallback when copy is refused. */
  U.select = function (el) {
    try {
      var range = document.createRange();
      range.selectNodeContents(el);
      var sel = globalThis.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
    } catch (e) { /* nothing to do */ }
  };

})(globalThis.SAA = globalThis.SAA || {});
