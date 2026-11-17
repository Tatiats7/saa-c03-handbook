/* merge.js (pure): merge rules of the state documents. ARCHITECTURE.md section 5.3. */
(function (SAA) {
  "use strict";

  function isObj(x) {
    return x !== null && typeof x === "object" && !Array.isArray(x);
  }

  function clone(x) {
    return x === undefined ? undefined : JSON.parse(JSON.stringify(x));
  }

  function same(a, b) {
    if (a === b) return true;
    if (isObj(a) && isObj(b)) {
      var ka = Object.keys(a), kb = Object.keys(b);
      if (ka.length !== kb.length) return false;
      for (var i = 0; i < ka.length; i++) {
        if (!Object.prototype.hasOwnProperty.call(b, ka[i]) || !same(a[ka[i]], b[ka[i]])) return false;
      }
      return true;
    }
    if (Array.isArray(a) && Array.isArray(b)) {
      if (a.length !== b.length) return false;
      for (var j = 0; j < a.length; j++) if (!same(a[j], b[j])) return false;
      return true;
    }
    return false;
  }

  /* A new object: b merged into a. Objects recurse; every other value (arrays too) replaces. */
  function deep(a, b) {
    if (!isObj(b)) return b === undefined ? clone(a) : clone(b);
    var out = isObj(a) ? clone(a) : {};
    Object.keys(b).forEach(function (k) {
      if (b[k] === undefined) return;
      out[k] = isObj(b[k]) ? deep(isObj(out[k]) ? out[k] : {}, b[k]) : clone(b[k]);
    });
    return out;
  }

  /* Union of keys; for a stamp on both sides the larger absolute value wins (a tie goes to "undone"). */
  function stamps(a, b) {
    if (a === undefined || a === null) return clone(b);
    if (b === undefined || b === null) return clone(a);
    if (typeof a === "number" && typeof b === "number") {
      var x = Math.abs(a), y = Math.abs(b);
      if (x === y) return Math.min(a, b);
      return x > y ? a : b;
    }
    if (isObj(a) && isObj(b)) {
      var out = {};
      Object.keys(a).forEach(function (k) { out[k] = stamps(a[k], b[k]); });
      Object.keys(b).forEach(function (k) { if (!(k in out)) out[k] = clone(b[k]); });
      return out;
    }
    if (isObj(a)) return clone(a);
    if (isObj(b)) return clone(b);
    return clone(a);
  }

  function at(doc) {
    return (doc && typeof doc.updatedAt === "number") ? doc.updatedAt : 0;
  }

  function later(l, r) {
    /* The whole document with the later updatedAt; untouched defaults (0) never win. */
    var lt = at(l), rt = at(r);
    if (rt > lt) return clone(r);
    if (lt > rt) return clone(l);
    var la = (l && typeof l.activeMs === "number") ? l.activeMs : 0;
    var ra = (r && typeof r.activeMs === "number") ? r.activeMs : 0;
    return clone(ra > la ? r : l);
  }

  function progress(l, r) {
    var newer = at(r) > at(l) ? r : l, older = newer === l ? r : l;
    var out = deep(older, newer);
    ["plan", "daily", "labs", "cards", "terms"].forEach(function (k) {
      var s = stamps(l[k], r[k]);
      if (s !== undefined) out[k] = s;
    });
    var lc = isObj(l.chapters) ? l.chapters : {}, rc = isObj(r.chapters) ? r.chapters : {};
    var ch = {};
    Object.keys(lc).concat(Object.keys(rc)).forEach(function (slug) {
      if (ch[slug]) return;
      var a = lc[slug], b = rc[slug];
      if (!isObj(a) || !isObj(b)) { ch[slug] = clone(isObj(a) ? a : b) || {}; return; }
      var c = deep(newer === l ? b : a, newer === l ? a : b);
      ["read", "skips"].forEach(function (k) {
        var s = stamps(a[k], b[k]);
        if (s !== undefined) c[k] = s;
      });
      ch[slug] = c;
    });
    out.chapters = ch;
    var ll = isObj(l.last) ? l.last : null, rl = isObj(r.last) ? r.last : null;
    out.last = clone(!ll ? rl : !rl ? ll : ((rl.t || 0) > (ll.t || 0) ? rl : ll));
    return out;
  }

  function qstats(l, r, opts) {
    var newer = at(r) > at(l) ? r : l, older = newer === l ? r : l;
    var out = deep(older, newer);
    var kr = opts && opts.kr ? opts.kr : null;
    var lq = isObj(l.q) ? l.q : {}, rq = isObj(r.q) ? r.q : {}, q = {};
    function live(id, rec) {
      if (!isObj(rec)) return null;
      if (kr && kr[id] !== undefined && rec.kr !== undefined && rec.kr !== kr[id]) return null;
      return rec;
    }
    Object.keys(lq).concat(Object.keys(rq)).forEach(function (id) {
      if (id in q) return;
      var a = live(id, lq[id]), b = live(id, rq[id]), pick;
      if (!a || !b) pick = a || b;
      else if ((a.kr || 0) !== (b.kr || 0)) pick = (b.kr || 0) > (a.kr || 0) ? b : a;
      else pick = (b.t || 0) > (a.t || 0) ? b : a;
      if (pick) q[id] = clone(pick);
    });
    out.q = q;
    out.sf = Math.max(l.sf || 0, r.sf || 0);
    return out;
  }

  function speak(l, r) {
    var newer = at(r) > at(l) ? r : l, older = newer === l ? r : l;
    var out = deep(older, newer);
    var li = isObj(l.items) ? l.items : {}, ri = isObj(r.items) ? r.items : {}, items = {};
    Object.keys(li).concat(Object.keys(ri)).forEach(function (id) {
      if (id in items) return;
      var a = li[id], b = ri[id];
      items[id] = clone(!isObj(a) ? b : !isObj(b) ? a : ((b.t || 0) > (a.t || 0) ? b : a));
    });
    out.items = items;
    return out;
  }

  function root(l, r) {
    var out = later(l, r);
    var lc = l.createdAt > 0 ? l.createdAt : 0, rc = r.createdAt > 0 ? r.createdAt : 0;
    out.createdAt = lc && rc ? Math.min(lc, rc) : (lc || rc || 0);
    out.lastSeenAt = Math.max(l.lastSeenAt || 0, r.lastSeenAt || 0);
    return out;
  }

  /* name: root, progress, qstats, exam, speak. opts.kr (qstats only): {question id: keyRev of qindex}. */
  function doc(name, l, r, opts) {
    if (!isObj(l)) return isObj(r) ? clone(r) : null;
    if (!isObj(r)) return clone(l);
    var out;
    if (name === "progress") out = progress(l, r);
    else if (name === "qstats") out = qstats(l, r, opts);
    else if (name === "speak") out = speak(l, r);
    else if (name === "root" || name === "settings") out = root(l, r);
    else out = later(l, r);
    out.updatedAt = Math.max(at(l), at(r));
    return out;
  }

  function toMap(x) {
    var m = {};
    if (Array.isArray(x)) x.forEach(function (a) { if (isObj(a) && a.id) m[a.id] = a; });
    else if (isObj(x)) Object.keys(x).forEach(function (id) { if (isObj(x[id])) m[id] = x[id]; });
    return m;
  }

  /* Union by id (maps or arrays in, a map out). An attempt is immutable; a copy with answers beats a trimmed one. */
  function attempts(a, b) {
    var ma = toMap(a), mb = toMap(b), out = {};
    Object.keys(ma).forEach(function (id) { out[id] = clone(ma[id]); });
    Object.keys(mb).forEach(function (id) {
      if (!out[id] || (!out[id].answers && mb[id].answers)) out[id] = clone(mb[id]);
    });
    return out;
  }

  /* The smallest patch p with deep(base, p) equal to next. Keys that next dropped are not expressed. */
  function diff(base, next) {
    if (!isObj(next)) return clone(next);
    if (!isObj(base)) return clone(next);
    var p = {};
    Object.keys(next).forEach(function (k) {
      var a = base[k], b = next[k];
      if (b === undefined || same(a, b)) return;
      if (isObj(a) && isObj(b)) p[k] = diff(a, b);
      else p[k] = clone(b);
    });
    return p;
  }

  SAA.Merge = {deep: deep, stamps: stamps, doc: doc, attempts: attempts, diff: diff, same: same, isObj: isObj};
})(globalThis.SAA = globalThis.SAA || {});
