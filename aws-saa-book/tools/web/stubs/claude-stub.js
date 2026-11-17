/* claude-stub.js: a fake window.claude for the local preview. Never published. ARCHITECTURE.md section 9.4.
   Mode: localStorage.saaStub = ok (default) | none | errors | hot | consent.
   Other switches (all optional):
     localStorage.saaStubCode   the code that sample rejects with in mode errors (default rate_limited)
     localStorage.saaStubUid    the id that user.id() resolves (default stub-user)
     localStorage.saaStubCaps   comma list of capabilities that resolve null in any mode, for example "db,downloads"
     sessionStorage.saaStubNoLs = "1"   makes every read and write of a saa1: key throw (the "memory" status)
   In the console: claude.__stub.setMode("errors"), claude.__stub.breakStorage(true), claude.__stub.reset(). */
(function () {
  "use strict";
  if (typeof window === "undefined" || window.claude) return;

  function read(store, key) {
    try { return store.getItem(key); } catch (e) { return null; }
  }
  function write(store, key, value) {
    try { if (value === null) store.removeItem(key); else store.setItem(key, value); return true; } catch (e) { return false; }
  }
  function local() { try { return window.localStorage; } catch (e) { return null; } }
  function session() { try { return window.sessionStorage; } catch (e) { return null; } }
  function lget(key) { var s = local(); return s ? read(s, key) : null; }
  function lset(key, value) { var s = local(); return s ? write(s, key, value) : false; }
  function sget(key) { var s = session(); return s ? read(s, key) : null; }
  function sset(key, value) { var s = session(); return s ? write(s, key, value) : false; }

  var MODES = ["ok", "none", "errors", "hot", "consent"];
  var mode = lget("saaStub");
  if (MODES.indexOf(mode) < 0) mode = "ok";
  var off = (lget("saaStubCaps") || "").split(",").map(function (s) { return s.trim(); }).filter(Boolean);

  /* Break the saa1: keys before the page script runs, when asked. */
  if (sget("saaStubNoLs") === "1" && typeof Storage !== "undefined") {
    var proto = Storage.prototype, g = proto.getItem, s0 = proto.setItem, r0 = proto.removeItem;
    var guard = function (key) {
      if (String(key).indexOf("saa1:") === 0) throw new DOMException("stub: storage is blocked", "SecurityError");
    };
    proto.getItem = function (key) { guard(key); return g.call(this, key); };
    proto.setItem = function (key, value) { guard(key); return s0.call(this, key, value); };
    proto.removeItem = function (key) { guard(key); return r0.call(this, key); };
  }

  function clone(x) { return x === undefined ? undefined : JSON.parse(JSON.stringify(x)); }
  function isObj(x) { return x !== null && typeof x === "object" && !Array.isArray(x); }
  function freeze(x) {
    if (x && typeof x === "object") { Object.keys(x).forEach(function (k) { freeze(x[k]); }); Object.freeze(x); }
    return x;
  }
  function err(code, message) { return {code: code, message: message || code}; }
  function soon(fn) { setTimeout(fn, 0); }

  /* ---------- db ---------- */

  var data = {};              /* path -> document body; the object identity never changes */
  var listeners = [];         /* {kind: "doc"|"query", path, q, next, error, last} */
  var writes = 0, touchedDb = false;

  (function loadDb() {
    var raw = lget("saaStubDb");
    if (!raw) return;
    try {
      var o = JSON.parse(raw);
      if (isObj(o)) Object.keys(o).forEach(function (k) { data[k] = o[k]; });
    } catch (e) { /* a broken mirror is ignored */ }
  })();

  function mirror() { lset("saaStubDb", JSON.stringify(data)); }

  function segments(path, want) {
    if (typeof path !== "string" || !path) throw new TypeError("db: the path must be a non-empty string");
    var segs = path.split("/");
    if (segs.length > 16 || path.length > 1000) throw new TypeError("db: the path is too long: " + path);
    segs.forEach(function (s) {
      if (!s || s === "." || s === ".." || !/^[A-Za-z0-9_\-.~:@+]+$/.test(s) || s.length > 200) {
        throw new TypeError("db: bad path segment \"" + s + "\" in " + path);
      }
    });
    if (want === "doc" && segs.length % 2 !== 0) {
      throw new TypeError("db: a document path needs an even number of segments, got " + segs.length + ": " + path);
    }
    if (want === "collection" && segs.length % 2 !== 1) {
      throw new TypeError("db: a collection path needs an odd number of segments, got " + segs.length + ": " + path);
    }
    return segs;
  }

  function used() { touchedDb = true; }

  function writeGate() {
    writes++;
    if (mode !== "errors") return null;
    return writes === 1 ? err("unavailable", "stub: the first write fails") : err("revoked", "stub: the grant was withdrawn");
  }

  function docSnap(path, pending) {
    var body = data[path];
    var frozen = body === undefined ? undefined : freeze(clone(body));
    return freeze({id: path.split("/").pop(), exists: body !== undefined,
      data: function () { return frozen; },
      metadata: {fromCache: false, hasPendingWrites: !!pending}});
  }

  function matches(body, f) {
    var v = body ? body[f.field] : undefined, w = f.value;
    switch (f.op) {
      case "==": return v === w;
      case "!=": return v !== undefined && v !== w;
      case "<": return v < w;
      case "<=": return v <= w;
      case ">": return v > w;
      case ">=": return v >= w;
      case "in": return Array.isArray(w) && w.indexOf(v) >= 0;
      case "not-in": return Array.isArray(w) && v !== undefined && w.indexOf(v) < 0;
      case "array-contains": return Array.isArray(v) && v.indexOf(w) >= 0;
      default: return false;
    }
  }

  function runQuery(q) {
    var prefix = q.path + "/", depth = q.path.split("/").length + 1;
    var paths = Object.keys(data).filter(function (p) {
      return p.indexOf(prefix) === 0 && p.split("/").length === depth &&
        q.filters.every(function (f) { return matches(data[p], f); });
    }).sort();
    if (q.order) {
      var f = q.order.field, sign = q.order.dir === "desc" ? -1 : 1;
      paths.sort(function (a, b) {
        var x = data[a][f], y = data[b][f];
        if (x === undefined && y === undefined) return a < b ? -1 : 1;
        if (x === undefined) return 1;
        if (y === undefined) return -1;
        if (x === y) return a < b ? -1 : 1;
        return (x < y ? -1 : 1) * sign;
      });
    }
    if (q.max) paths = paths.slice(0, q.max);
    return paths;
  }

  function querySnap(q, pending, prev) {
    var paths = runQuery(q), docsOut = paths.map(function (p) { return docSnap(p, pending); });
    var before = prev || {};
    return freeze({docs: docsOut, size: docsOut.length, empty: !docsOut.length,
      docChanges: function () {
        var out = [];
        paths.forEach(function (p, i) {
          if (!(p in before)) out.push({type: "added", doc: docsOut[i], oldIndex: -1, newIndex: i});
          else if (before[p] !== JSON.stringify(data[p])) out.push({type: "modified", doc: docsOut[i], oldIndex: i, newIndex: i});
        });
        return out;
      },
      metadata: {fromCache: false, hasPendingWrites: !!pending}});
  }

  function deliver(l, pending) {
    if (l.dead) return;
    try {
      if (l.kind === "doc") l.next(docSnap(l.path, pending));
      else {
        var snap = querySnap(l.q, pending, l.last);
        var now = {};
        runQuery(l.q).forEach(function (p) { now[p] = JSON.stringify(data[p]); });
        l.last = now;
        l.next(snap);
      }
    } catch (e) { if (window.console) window.console.error("stub: a snapshot callback threw", e); }
  }

  function notify(path) {
    listeners.forEach(function (l) {
      var hit = l.kind === "doc" ? l.path === path : path.indexOf(l.q.path + "/") === 0;
      if (!hit) return;
      deliver(l, true);                       /* latency compensation: the page's own write */
      soon(function () { deliver(l, false); });
    });
  }

  function subscribe(l) {
    used();
    if (listeners.length >= 64) {
      soon(function () { if (l.error) l.error(err("resource_exhausted", "stub: 64 subscriptions")); });
      return function () {};
    }
    listeners.push(l);
    soon(function () { deliver(l, false); });
    return function () {
      l.dead = true;
      var i = listeners.indexOf(l);
      if (i >= 0) listeners.splice(i, 1);
    };
  }

  function checkBody(body) {
    if (!isObj(body)) return err("invalid_argument", "stub: a document body must be a plain object");
    var text;
    try { text = JSON.stringify(body); } catch (e) { return err("invalid_argument", "stub: the body is not JSON"); }
    if (text.length > 262144) return err("invalid_argument", "stub: the document is over 256 KiB");
    return null;
  }

  function merge(target, patch) {
    Object.keys(patch).forEach(function (k) {
      if (isObj(patch[k])) {
        if (!isObj(target[k])) target[k] = {};
        merge(target[k], patch[k]);
      } else target[k] = clone(patch[k]);
    });
  }

  var minted = 0;
  function mint() { minted++; return "s" + minted.toString(36) + Math.random().toString(36).slice(2, 8); }

  function docRef(path) {
    segments(path, "doc");
    return {
      id: path.split("/").pop(),
      path: path,
      get: function () { used(); return Promise.resolve().then(function () { return docSnap(path, false); }); },
      set: function (body) {
        used();
        return Promise.resolve().then(function () {
          var bad = checkBody(body) || writeGate();
          if (bad) throw bad;
          data[path] = clone(body);
          mirror();
          notify(path);
        });
      },
      update: function (body) {
        used();
        return Promise.resolve().then(function () {
          var bad = checkBody(body) || writeGate();
          if (bad) throw bad;
          if (data[path] === undefined) throw err("invalid_argument", "stub: update of a missing document: " + path);
          merge(data[path], body);
          mirror();
          notify(path);
        });
      },
      delete: function () {
        used();
        return Promise.resolve().then(function () {
          var bad = writeGate();
          if (bad) throw bad;
          delete data[path];
          mirror();
          notify(path);
        });
      },
      acquire: function (options) {
        used();
        return Promise.resolve({acquired: true, version: 1, holder: options && options.holder});
      },
      onSnapshot: function (next, error) { return subscribe({kind: "doc", path: path, next: next, error: error}); },
      collection: function (sub) { return collRef(path + "/" + sub); }
    };
  }

  function queryRef(q) {
    return {
      where: function (field, op, value) {
        return queryRef({path: q.path, filters: q.filters.concat([{field: field, op: op, value: value}]), order: q.order, max: q.max});
      },
      orderBy: function (field, dir) { return queryRef({path: q.path, filters: q.filters, order: {field: field, dir: dir || "asc"}, max: q.max}); },
      limit: function (n) { return queryRef({path: q.path, filters: q.filters, order: q.order, max: n}); },
      get: function () { used(); return Promise.resolve().then(function () { return querySnap(q, false, null); }); },
      onSnapshot: function (next, error) { return subscribe({kind: "query", q: q, next: next, error: error, last: null}); }
    };
  }

  function collRef(path) {
    segments(path, "collection");
    var ref = queryRef({path: path, filters: [], order: null, max: 0});
    ref.path = path;
    ref.doc = function (id) { return docRef(path + "/" + (id || mint())); };
    ref.add = function (body) { var d = ref.doc(); return d.set(body).then(function () { return d; }); };
    return ref;
  }

  var db = Object.freeze({doc: docRef, collection: collRef});

  /* ---------- user ---------- */

  function uidNow() { return lget("saaStubUid") || "stub-user"; }
  function viewer() {
    return {id: uidNow(), name: "", avatarUrl: "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
      color: "currentColor", email: null, isOwner: true, canEdit: true};
  }
  var user = Object.freeze({
    id: function () { return Promise.resolve(uidNow()); },
    isOwner: function () { return Promise.resolve(true); },
    canEdit: function () { return Promise.resolve(true); },
    can: function () { return Promise.resolve(true); },
    me: function () { return Promise.resolve(viewer()); },
    name: function () { return Promise.resolve(""); },
    email: function () { return Promise.resolve(null); },
    avatarUrl: function () { return Promise.resolve(viewer().avatarUrl); },
    search: function () { return Promise.resolve([]); },
    profiles: function (ids) {
      var out = {};
      (Array.isArray(ids) ? ids : [ids]).forEach(function (id) {
        var v = viewer();
        out[id] = {id: id, name: "", avatarUrl: v.avatarUrl, color: v.color, email: null, isMe: id === v.id, guest: false};
      });
      return Promise.resolve(out);
    }
  });

  /* ---------- sample ---------- */

  function between(text, a, b) {
    var i = text.indexOf(a);
    if (i < 0) return "";
    var j = b ? text.indexOf(b, i + a.length) : -1;
    return text.slice(i + a.length, j < 0 ? undefined : j);
  }

  function cannedSpeak(text) {
    var kp = [];
    between(text, "Key points", "Model answer").split("\n").forEach(function (line) {
      var parts = line.split("|").map(function (s) { return s.trim(); });
      if (parts.length >= 3 && /^[a-z0-9-]+$/i.test(parts[0]) && parts[0] !== "id") kp.push({id: parts[0], point: parts[2]});
    });
    var answer = between(text, "ANSWER\n<<<", ">>>").trim() || between(text, "<<<", ">>>").trim();
    var words = answer.split(/\s+/).filter(Boolean);
    var quote = words.slice(0, 6).join(" ");
    var half = Math.max(1, Math.ceil(kp.length / 2));
    return {
      verdict: "almost",
      covered: kp.slice(0, half).map(function (k) { return {kp: k.id, quote: quote}; }),
      missing: kp.slice(half).map(function (k) { return {kp: k.id, say: "Add this point: " + k.point}; }),
      errors: [],
      unverified: words.length > 12 ? [{quote: words.slice(-5).join(" ")}] : [],
      terms: [],
      clarity: ["Put the answer in the first sentence.", "Use shorter sentences."],
      improved: answer ? answer + " (Stub: this is where the improved version shows.)" : "Stub: improved version.",
      next: "Say the trade-off in one sentence.",
      moves: {answer: 2, how: 1, watch: 1, you: 0},
      heard_as: [],
      follow_up: "What would you change if the traffic doubled?"
    };
  }

  function cannedAsk(text) {
    var book = between(text, "\nBOOK\n", "\n[summary]") || between(text, "BOOK", "FACTS");
    var lines = book.split("\n").map(function (s) { return s.trim(); }).filter(function (s) { return s && s.charAt(0) !== "["; });
    var first = (lines[0] || "").split(/(?<=[.?!])\s/)[0] || "";
    if (first.length < 12) return {status: "not_in_book", answer: "", support: [], missing: "Stub: the section text was empty.", see: []};
    return {status: "answered", answer: "Stub answer. The section says: " + first,
      support: [{quote: first, from: "section"}], missing: "", see: []};
  }

  function inputText(input) {
    if (typeof input === "string") return input;
    return input.map(function (t) { return t.content; }).join("\n");
  }

  function checkInput(input, options) {
    if (options !== undefined && !isObj(options)) return err("invalid_request", "stub: options must be a plain object");
    if (typeof input === "string") { if (!input) return err("invalid_request", "stub: empty input"); }
    else if (Array.isArray(input) && input.length) {
      for (var i = 0; i < input.length; i++) {
        var t = input[i];
        if (!isObj(t) || (t.role !== "user" && t.role !== "assistant") || typeof t.content !== "string" || !t.content) {
          return err("invalid_request", "stub: turn " + i + " is malformed");
        }
      }
      if (input[0].role !== "user" || input[input.length - 1].role !== "user") {
        return err("invalid_request", "stub: turns must start and end on a user turn");
      }
    } else return err("invalid_request", "stub: input must be a string or a list of turns");
    if (options && options.signal !== undefined && !(typeof AbortSignal !== "undefined" && options.signal instanceof AbortSignal)) {
      return err("invalid_request", "stub: signal must be an AbortSignal");
    }
    var bytes = typeof TextEncoder !== "undefined" ? new TextEncoder().encode(inputText(input)).length : inputText(input).length;
    if (bytes > 262144) return err("prompt_too_large", "stub: over 256 KiB");
    return null;
  }

  var sampleCalls = [];
  function answer(input, options, asJson) {
    return new Promise(function (resolve, reject) {
      var bad = checkInput(input, options);
      if (bad) { reject(bad); return; }
      var signal = options && options.signal, text = inputText(input);
      sampleCalls.push({json: asJson, tier: (options && options.modelTier) || "default", bytes: text.length});
      setTimeout(function () {
        if (signal && signal.aborted) { reject(err("cancelled", "stub: aborted")); return; }
        if (mode === "errors") { reject(err(lget("saaStubCode") || "rate_limited", "stub: forced error")); return; }
        var value, raw;
        if (text.indexOf("speaking coach") >= 0) value = cannedSpeak(text);
        else if (text.indexOf("one section of a study book") >= 0) value = cannedAsk(text);
        else value = asJson ? {stub: true} : "Stub reply.";
        raw = typeof value === "string" ? value : JSON.stringify(value);
        if (options && typeof options.onText === "function") {
          try { options.onText({text: raw, delta: raw}); } catch (e) { /* reported, not fatal */ }
        }
        resolve(asJson ? value : {text: raw, truncated: false, modelTierApplied: (options && options.modelTier) || "default"});
      }, 20);
    });
  }
  var sample = function (input, options) { return answer(input, options, false); };
  sample.json = function (input, options) { return answer(input, options, true); };
  sample.limits = function () { return Promise.resolve({maxPromptBytes: 262144}); };
  Object.freeze(sample);

  /* ---------- downloads ---------- */

  var EXT = ["gif", "png", "jpg", "jpeg", "webp", "mp4", "webm", "txt", "json", "md", "docx", "pptx", "epub", "csv",
    "ttf", "html", "svg", "pdf", "xlsx", "zip"];
  window.__saaDownloads = [];
  var downloads = Object.freeze({
    save: function (req) {
      return Promise.resolve().then(function () {
        if (mode === "errors") throw err("declined", "stub: the viewer said no");
        if (!isObj(req) || typeof req.filename !== "string" || !req.filename || req.filename.length > 512) {
          throw err("bad_request", "stub: bad filename");
        }
        var d = req.data, size = -1;
        if (typeof d === "string") size = d.length;
        else if (typeof Blob !== "undefined" && d instanceof Blob) size = d.size;
        else if (d && typeof d.byteLength === "number") size = d.byteLength;
        if (size <= 0) throw err("bad_request", "stub: bad or empty data");
        var m = /\.([A-Za-z0-9]+)$/.exec(req.filename);
        if (!m || EXT.indexOf(m[1].toLowerCase()) < 0) throw err("rejected_extension", "stub: extension not allowed");
        window.__saaDownloads.push({filename: req.filename, size: size, text: typeof d === "string" ? d : null});
        return {status: "saved"};
      });
    }
  });

  /* ---------- permissions ---------- */

  function dbState() { return mode === "consent" && !touchedDb ? "prompt" : "granted"; }
  function allStates() {
    var out = {};
    ["db", "user", "sample", "downloads"].forEach(function (n) {
      if (off.indexOf(n) < 0) out[n] = n === "db" ? dbState() : "granted";
    });
    return out;
  }
  var permissions = Object.freeze({
    state: function (name) {
      var all = allStates();
      if (name === undefined) return Promise.resolve(all);
      return Promise.resolve(all[String(name).split(":")[0]] || "unavailable");
    },
    request: function (names) {
      if (mode === "consent") touchedDb = true;
      var all = allStates();
      if (!names) return Promise.resolve(all);
      var out = {};
      names.forEach(function (n) { out[n] = all[n] || "unavailable"; });
      return Promise.resolve(out);
    },
    manage: function () {
      if (mode === "errors") return Promise.reject(err("unavailable", "stub: the panel did not open"));
      return Promise.resolve();
    }
  });

  /* ---------- use ---------- */

  var spaces = {db: db, user: user, sample: sample, downloads: downloads, permissions: permissions};
  var memo = {};
  function use(name) {
    if (mode === "none" || !spaces[name] || off.indexOf(name) >= 0) return Promise.resolve(null);
    if (!memo[name]) memo[name] = new Promise(function (resolve) { soon(function () { resolve(spaces[name]); }); });
    return memo[name];
  }

  var claude = {use: use};

  claude.__stub = {
    mode: mode,
    db: data,
    sampleCalls: sampleCalls,
    reset: function () {
      Object.keys(data).forEach(function (k) { delete data[k]; });
      writes = 0;
      touchedDb = false;
      sampleCalls.length = 0;
      lset("saaStubDb", null);
      sset("saaStubHot", null);
      window.__saaDownloads = [];
    },
    setMode: function (m, reload) {
      if (MODES.indexOf(m) < 0) throw new Error("stub: mode is one of " + MODES.join(", "));
      lset("saaStub", m === "ok" ? null : m);
      if (reload !== false) window.location.reload();
    },
    breakStorage: function (on, reload) {
      sset("saaStubNoLs", on ? "1" : null);
      if (reload !== false) window.location.reload();
    }
  };

  if (mode === "hot") {
    var snapFn = null;
    claude.hot = {
      data: undefined,
      snapshot: function (fn) { snapFn = fn; },
      ready: function (cb) {
        soon(function () {
          var d = {};
          try { d = JSON.parse(sget("saaStubHot") || "{}"); } catch (e) { d = {}; }
          claude.hot.data = d;
          cb(d);
        });
      }
    };
    window.__saaRepublish = function () {
      var value = snapFn ? snapFn() : {};
      sset("saaStubHot", JSON.stringify(value === undefined ? {} : value));
      window.location.reload();
    };
  }

  window.claude = claude;
})();
