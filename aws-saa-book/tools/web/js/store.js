/* store.js: local-first state with an outbox and optional cloud sync. ARCHITECTURE.md sections 5.2 to 5.6.
   Browser storage is reached only through SAA.U.ls; the database only through the object given to attach. */
(function (SAA) {
  "use strict";

  var M = SAA.Merge;
  var NAMES = ["root", "progress", "qstats", "exam", "speak"];
  var KEY = {root: "saa1:settings", progress: "saa1:progress", qstats: "saa1:qstats", exam: "saa1:exam",
    speak: "saa1:speak", ui: "saa1:ui", attempts: "saa1:attempts", outbox: "saa1:outbox",
    drafts: "saa1:drafts", uid: "saa1:uid", bakid: "saa1:bakid", probe: "saa1:probe"};
  var PATH = {root: ".", progress: "state/progress", qstats: "state/qstats", exam: "state/exam", speak: "state/speak"};
  var KEEP = 40;            /* attempts that keep their answers */
  var SNAP_MAX = 300000;    /* characters of the hot snapshot */
  var STOP = {invalid_argument: 1, transform_error: 1, not_granted: 1, revoked: 1, capability_disabled: 1, capability_removed: 1};

  var docs = {}, ui = {}, attempts = {}, drafts = {}, outbox = {}, baks = {};
  var memory = false, cloud = "off", dead = false, consent = null, uid = null, db = null;
  var known = {}, drills = [], coach = null, inflight = null, unsubs = [];
  var dirty = {}, saveT = null, flushT = null, savedT = null, flushP = null, again = false, retried = false;
  var pauseUntil = 0, attachP = null, wired = false;

  function clone(x) { return x === undefined ? undefined : JSON.parse(JSON.stringify(x)); }

  function defaults(name) {
    if (name === "root") {
      return {v: 1, createdAt: 0, lastSeenAt: 0, updatedAt: 0,
        settings: {textSize: 1, route: "pass", routeBy: {}, plan: "a", planStart: null, examDate: null,
          extraTime: 0, stemFirst: "auto", skim: 0}};
    }
    if (name === "progress") return {v: 1, updatedAt: 0, chapters: {}, plan: {}, daily: {}, labs: {}, cards: {}, terms: {}, last: null};
    if (name === "qstats") return {v: 1, updatedAt: 0, sf: 0, q: {}};
    if (name === "exam") return {v: 1, updatedAt: 0, none: 1};
    if (name === "speak") return {v: 1, updatedAt: 0, items: {}};
    if (name === "ui") return {route: "", t: 0, pos: {}, seen: {}, tab: {}};
    return {};
  }

  function shaped(name, value) {
    if (!M.isObj(value)) return defaults(name);
    if (name === "exam") return clone(value);
    return M.deep(defaults(name), value);
  }

  function lsGet(key) {
    if (memory) return null;
    try { return SAA.U.ls.get(key); } catch (e) { return null; }
  }

  function lsSet(key, value) {
    if (memory) return false;
    try { return SAA.U.ls.set(key, value) !== false; } catch (e) { return false; }
  }

  function emit(name, detail) {
    try { if (SAA.bus && SAA.bus.emit) SAA.bus.emit(name, detail); } catch (e) { /* a listener failed; the store goes on */ }
  }

  function changed(doc, source) {
    emit("store:change", {doc: doc, source: source});
    if (doc === "settings" || doc === "root" || doc === "*") emit("settings", docs.root.settings);
  }

  function mergeInto(target, patch) {
    Object.keys(patch).forEach(function (k) {
      var v = patch[k];
      if (v === undefined) return;
      if (M.isObj(v)) {
        if (!M.isObj(target[k])) target[k] = {};
        mergeInto(target[k], v);
      } else target[k] = clone(v);
    });
  }

  /* ---------- local save ---------- */

  function touch(what, mode) {
    if (dirty[what] !== 2) dirty[what] = mode === "force" ? 2 : 1;
    if (mode === "now" || mode === "force") { saveNow(); return; }
    if (saveT === null) saveT = setTimeout(saveNow, 400);
  }

  function saveNow() {
    if (saveT !== null) { clearTimeout(saveT); saveT = null; }
    var d = dirty, remote = [];
    dirty = {};
    if (memory) return;
    Object.keys(d).forEach(function (what) {
      var stored;
      if (NAMES.indexOf(what) >= 0) {
        if (d[what] !== 2) {
          /* another tab may have written since: read again and merge before the write */
          stored = lsGet(KEY[what]);
          if (M.isObj(stored)) {
            var merged = M.doc(what, docs[what], stored);
            if (!M.same(merged, docs[what])) { docs[what] = merged; remote.push(what); }
          }
        }
        lsSet(KEY[what], docs[what]);
      } else if (what === "ui") {
        stored = d[what] !== 2 ? lsGet(KEY.ui) : null;
        if (M.isObj(stored)) ui = M.deep(stored, ui);
        lsSet(KEY.ui, ui);
      } else if (what === "attempts") {
        stored = d[what] !== 2 ? lsGet(KEY.attempts) : null;
        if (M.isObj(stored)) attempts = M.attempts(attempts, stored);
        trim();
        lsSet(KEY.attempts, attempts);
      } else if (what === "outbox") lsSet(KEY.outbox, outboxView());
      else if (what === "drafts") lsSet(KEY.drafts, drafts);
      else if (what === "uid") lsSet(KEY.uid, uid);
    });
    remote.forEach(function (name) { changed(name === "root" ? "settings" : name, "remote"); });
  }

  function trim() {
    var list = attemptList();
    for (var i = KEEP; i < list.length; i++) {
      delete attempts[list[i].id].answers;
      delete attempts[list[i].id].order;
    }
    if (cloud !== "on") {
      for (var j = KEEP; j < list.length; j++) delete outbox["attempts/" + list[j].id];
    }
  }

  function attemptList() {
    return Object.keys(attempts).map(function (id) { return attempts[id]; }).sort(function (a, b) {
      return (b.submittedAt || 0) - (a.submittedAt || 0) || (a.id < b.id ? 1 : -1);
    });
  }

  /* ---------- outbox ---------- */

  function combine(older, newer) {
    if (!older) return newer;
    if (!newer) return older;
    if (newer.op === "set") return newer;
    return {op: older.op, data: M.deep(older.data, newer.data)};
  }

  function outboxView() {
    var out = clone(outbox);
    if (inflight) out[inflight.key] = clone(combine(inflight.entry, outbox[inflight.key]));
    return out;
  }

  function queue(key, op, data) {
    outbox[key] = combine(outbox[key], {op: op, data: clone(data)});
    retried = false;
    touch("outbox");
  }

  function nameOf(key) {
    for (var i = 0; i < NAMES.length; i++) if (PATH[NAMES[i]] === key) return NAMES[i];
    return null;
  }

  function docRef(key) {
    return db.doc(key === "." ? "study/" + uid : "study/" + uid + "/" + key);
  }

  function localDoc(key, entry) {
    var name = nameOf(key);
    return clone(name ? docs[name] : entry.data);
  }

  async function write(key, entry) {
    var ref = docRef(key);
    if (entry.op === "set") { await ref.set(clone(entry.data)); return; }
    if (known[key]) {
      try { await ref.update(clone(entry.data)); return; } catch (e) {
        if (!e || e.code !== "invalid_argument") throw e;
      }
      await ref.get();
      await ref.set(localDoc(key, entry));
      return;
    }
    var snap = await ref.get();
    if (!snap.exists) await ref.set(localDoc(key, entry));
    else await ref.update(clone(entry.data));
  }

  async function run() {
    var wrote = false;
    for (;;) {
      if (cloud !== "on") return wrote;
      var keys = Object.keys(outbox).sort();
      if (!keys.length) return wrote;
      var key = keys[0], entry = outbox[key];
      delete outbox[key];
      inflight = {key: key, entry: entry};
      try {
        await write(key, entry);
      } catch (e) {
        outbox[key] = combine(entry, outbox[key]);
        inflight = null;
        fail(e);
        return wrote;
      }
      inflight = null;
      known[key] = true;
      wrote = true;
      touch("outbox");
    }
  }

  function fail(e) {
    var code = (e && e.code) || "unavailable";
    if (STOP[code]) { stopCloud(); return; }
    if (code === "quota_exceeded") {
      stopCloud();
      try { SAA.U.toast("Online storage is full. Progress stays on this device."); } catch (x) { /* no toast */ }
      return;
    }
    if (code === "resource_exhausted") { pauseUntil = SAA.U.nowMs() + 30000; return; }
    again = false;
    if (!retried) {
      retried = true;
      if (flushT !== null) clearTimeout(flushT);
      flushT = setTimeout(function () { flushT = null; flush(); }, 1000 + Math.floor(Math.random() * 2000));
    }
  }

  function flush() {
    if (cloud !== "on" || !db) return Promise.resolve(false);
    if (flushP) { again = true; return flushP; }
    if (pauseUntil && SAA.U.nowMs() < pauseUntil) return Promise.resolve(false);
    pauseUntil = 0;
    flushP = run().then(function (wrote) {
      flushP = null;
      if (wrote && cloud === "on") showSaved();
      if (again) { again = false; return flush(); }
      return wrote;
    }, function () { flushP = null; return false; });
    return flushP;
  }

  function flushSoon(ms) {
    if (cloud !== "on") return;
    if (!ms) { flush(); return; }
    if (flushT !== null) clearTimeout(flushT);
    flushT = setTimeout(function () { flushT = null; flush(); }, ms);
  }

  /* ---------- status line ---------- */

  function statusName() { return cloud === "on" ? "cloud" : memory ? "memory" : "local"; }

  function setStatus() {
    if (SAA.state) SAA.state.status = statusName();
    emit("store:status", {status: statusName(), consent: consent});
    renderSync(false);
  }

  function renderSync(saved) {
    if (typeof document === "undefined") return;
    var el = document.getElementById("saa-sync");
    if (!el) return;
    var text = "";
    if (cloud === "on") text = memory ? "Saved online only" : (saved ? "Saved" : "");
    else if (memory) text = "Progress is not being saved on this device";
    else text = "Saved on this device only";
    el.textContent = text;
    if (cloud !== "on" && consent === "prompt" && !dead) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "btn quiet";
      b.setAttribute("data-act", "sync-on");
      b.textContent = "Save online too";
      el.appendChild(document.createTextNode(" "));
      el.appendChild(b);
    }
    el.hidden = !text;
  }

  function showSaved() {
    renderSync(true);
    if (savedT !== null) clearTimeout(savedT);
    savedT = setTimeout(function () { savedT = null; renderSync(false); }, 2000);
  }

  function stopCloud() {
    cloud = "off";
    dead = true;
    consent = consent === "prompt" ? null : consent;
    unsubs.forEach(function (un) { try { un(); } catch (e) { /* already closed */ } });
    unsubs = [];
    setStatus();
  }

  /* ---------- init ---------- */

  function wire() {
    if (wired || typeof window === "undefined" || !window.addEventListener) return;
    wired = true;
    window.addEventListener("storage", onStorage);
    window.addEventListener("pagehide", function () { saveNow(); flush(); });
    if (typeof document !== "undefined") {
      document.addEventListener("visibilitychange", function () {
        if (document.visibilityState === "hidden") { saveNow(); flush(); }
      });
      document.addEventListener("click", function (e) {
        var t = e.target && e.target.closest ? e.target.closest("#saa-sync [data-act=\"sync-on\"]") : null;
        if (!t) return;
        var caps = (SAA.state && SAA.state.caps) || {};
        attach(caps.db || null, (SAA.state && SAA.state.uid) || null);
      });
    }
  }

  function onStorage(e) {
    if (!e || !e.key || e.key.indexOf("saa1:") !== 0 || memory) return;
    var val;
    try { val = e.newValue ? JSON.parse(e.newValue) : null; } catch (x) { return; }
    if (!M.isObj(val)) return;
    NAMES.forEach(function (name) {
      if (KEY[name] !== e.key) return;
      var merged = M.doc(name, docs[name], val);
      if (M.same(merged, docs[name])) return;
      docs[name] = merged;
      changed(name === "root" ? "settings" : name, "remote");
    });
    if (e.key === KEY.attempts) {
      var n = Object.keys(attempts).length;
      attempts = M.attempts(attempts, val);
      if (Object.keys(attempts).length !== n) changed("attempts", "remote");
    }
  }

  function cancelTimers() {
    [saveT, flushT, savedT].forEach(function (t) { if (t !== null) clearTimeout(t); });
    saveT = flushT = savedT = null;
    dirty = {};
  }

  function init(hot) {
    cancelTimers();
    memory = false;
    memory = !lsSet(KEY.probe, 1);
    NAMES.forEach(function (name) { docs[name] = shaped(name, lsGet(KEY[name])); });
    ui = shaped("ui", lsGet(KEY.ui));
    attempts = M.attempts(lsGet(KEY.attempts), null);
    var d = lsGet(KEY.drafts), o = lsGet(KEY.outbox), u = lsGet(KEY.uid);
    drafts = M.isObj(d) ? d : {};
    outbox = M.isObj(o) ? o : {};
    uid = typeof u === "string" && u ? u : uid;
    coach = null;
    if (M.isObj(hot) && hot.v === 1) {
      if (M.isObj(hot.docs)) {
        NAMES.forEach(function (name) {
          if (!M.isObj(hot.docs[name])) return;
          docs[name] = M.doc(name, docs[name], hot.docs[name]);
          touch(name);
        });
      }
      if (M.isObj(hot.outbox)) {
        Object.keys(hot.outbox).forEach(function (k) {
          if (!outbox[k] && M.isObj(hot.outbox[k])) { outbox[k] = clone(hot.outbox[k]); touch("outbox"); }
        });
      }
      if (!uid && typeof hot.uid === "string") uid = hot.uid;
      if (hot.attempts) { attempts = M.attempts(attempts, hot.attempts); touch("attempts"); }
      if (M.isObj(hot.drafts)) {
        Object.keys(hot.drafts).forEach(function (k) { if (!(k in drafts)) drafts[k] = hot.drafts[k]; });
      }
      saveNow();
    }
    wire();
    setStatus();
  }

  /* ---------- reads and writes ---------- */

  function get(name) {
    if (name === "settings") return docs.root ? docs.root.settings : defaults("root").settings;
    if (name === "ui") return ui;
    if (name === "coach") return coach;
    return docs[name] || null;
  }

  function patch(name, p) {
    if (!M.isObj(p)) return;
    if (!docs.root) init();
    var now = SAA.U.now();
    if (name === "ui") {
      mergeInto(ui, p);
      touch("ui");
      emit("store:change", {doc: "ui", source: "local"});
      return;
    }
    if (name === "settings") {
      var r = docs.root, ob = {settings: p};
      mergeInto(r.settings, p);
      r.updatedAt = Math.max(now, r.updatedAt || 0);
      ob.updatedAt = r.updatedAt;
      if (!r.createdAt) { r.createdAt = now; ob.createdAt = now; ob.v = 1; }
      queue(".", "merge", ob);
      touch("root");
      flushSoon(2000);
      changed("settings", "local");
      return;
    }
    if (name === "root" || NAMES.indexOf(name) < 0) return;
    var d = docs[name], q = clone(p);
    if (name === "exam" && d.none && !("none" in q)) q.none = 0;
    mergeInto(d, q);
    d.updatedAt = Math.max(now, d.updatedAt || 0);
    q.updatedAt = d.updatedAt;
    queue(PATH[name], "merge", q);
    touch(name, name === "exam" ? "now" : undefined);
    flushSoon(name === "exam" ? 0 : 2000);
    changed(name, "local");
  }

  function replace(name, doc) {
    if (name === "root" || NAMES.indexOf(name) < 0) return;
    if (!docs.root) init();
    var prev = (docs[name] && docs[name].updatedAt) || 0;
    var d = M.isObj(doc) ? clone(doc) : (name === "exam" ? {v: 1, none: 1} : defaults(name));
    d.updatedAt = Math.max(SAA.U.now(), prev + 1);
    docs[name] = d;
    queue(PATH[name], "set", d);
    touch(name, "force");
    flushSoon(0);
    changed(name, "local");
  }

  function stamp(name, path, done) {
    var t = SAA.U.now(), p = {}, cur = p;
    for (var i = 0; i < path.length - 1; i++) { cur[path[i]] = {}; cur = cur[path[i]]; }
    cur[path[path.length - 1]] = done === false ? -t : t;
    patch(name, p);
  }

  /* Saves the live document to this device without a cloud write or a new updatedAt (the exam timer). */
  function save(name) {
    if (name === "ui" || NAMES.indexOf(name) >= 0) touch(name, "now");
  }

  function draft(id, text) {
    if (arguments.length < 2) return typeof drafts[id] === "string" ? drafts[id] : "";
    if (text) drafts[id] = String(text); else delete drafts[id];
    touch("drafts");
    return undefined;
  }

  function setConsent(state) {
    consent = state === "prompt" || state === "denied" ? state : null;
    setStatus();
  }

  function addAttempt(a) {
    if (!M.isObj(a) || !a.id) return;
    attempts[a.id] = clone(a);
    queue("attempts/" + a.id, "set", a);
    trim();
    touch("attempts", "now");
    emit("attempt", attempts[a.id]);
    emit("store:change", {doc: "attempts", source: "local"});
    flushSoon(0);
    refreshCoach().then(function (c) {
      if (!c) return;
      queue("state/coach", "set", c);
      flushSoon(0);
    });
  }

  function refreshCoach() {
    var Sc = SAA.Scoring, C = SAA.Content;
    if (!Sc || !Sc.buildCoach || !C || !C.qindex || !C.manifest) return Promise.resolve(coach);
    return Promise.all([C.qindex(), C.manifest()]).then(function (r) {
      coach = Sc.buildCoach({settings: docs.root.settings, progress: docs.progress, qstats: docs.qstats,
        speak: docs.speak, attempts: attemptList()}, r[0], r[1], SAA.U.now());
      return coach;
    }).catch(function () { return coach; });
  }

  function flag(kind, ref, note) {
    var id = SAA.U.uid("f");
    queue("flags/" + id, "set", {v: 1, id: id, at: SAA.U.now(), kind: kind, ref: ref,
      build: (SAA.state && SAA.state.build) || "", note: String(note || "").slice(0, 500)});
    flushSoon(0);
    try { SAA.U.toast("Report saved."); } catch (e) { /* no toast */ }
  }

  /* ---------- import, export ---------- */

  function exportAll() {
    return {v: 1, build: (SAA.state && SAA.state.build) || "", exportedAt: SAA.U.now(), root: clone(docs.root),
      progress: clone(docs.progress), qstats: clone(docs.qstats), speak: clone(docs.speak),
      attempts: clone(attempts), coach: clone(coach)};
  }

  function importAll(obj) {
    var bad = {ok: false, counts: {answers: 0, attempts: 0}, error: "This is not a progress file of this book."};
    if (!M.isObj(obj) || obj.v !== 1) return bad;
    var names = ["root", "progress", "qstats", "speak"], any = false, i;
    for (i = 0; i < names.length; i++) {
      var v = obj[names[i]];
      if (v === undefined || v === null) continue;
      if (!M.isObj(v)) return bad;
      any = true;
    }
    if (obj.root && !M.isObj(obj.root.settings)) return bad;
    if (obj.qstats && obj.qstats.q !== undefined && !M.isObj(obj.qstats.q)) return bad;
    if (obj.attempts !== undefined && obj.attempts !== null && !M.isObj(obj.attempts) && !Array.isArray(obj.attempts)) return bad;
    if (!any && !obj.attempts) return bad;
    if (!docs.root) init();
    names.forEach(function (name) {
      if (!M.isObj(obj[name])) return;
      var before = docs[name], after = M.doc(name, before, shaped(name, obj[name]));
      if (M.same(before, after)) return;
      docs[name] = after;
      var p = M.diff(before, after);
      if (Object.keys(p).length) queue(PATH[name], "merge", p);
      touch(name);
    });
    var incoming = M.attempts(obj.attempts || null, null), added = 0;
    Object.keys(incoming).forEach(function (id) {
      if (attempts[id]) return;
      attempts[id] = incoming[id];
      queue("attempts/" + id, "set", incoming[id]);
      added++;
    });
    trim();
    touch("attempts");
    saveNow();
    changed("*", "remote");
    flushSoon(0);
    refreshCoach();
    return {ok: true, counts: {answers: obj.qstats && obj.qstats.q ? Object.keys(obj.qstats.q).length : 0,
      attempts: Object.keys(incoming).length, newAttempts: added}};
  }

  function pct(c, n) { return n ? Math.round(100 * c / n) : 0; }

  function summaryText() {
    var lines = [], list = attemptList(), c = coach;
    lines.push("SAA-C03 Handbook: my study progress (build " + ((SAA.state && SAA.state.build) || "unknown") + ")");
    if (c && c.overall) {
      lines.push("Overall: " + c.overall.seen + " of " + c.overall.bank + " questions seen, accuracy " +
        c.overall.accuracy + "%, accuracy when sure " + c.overall.sureAccuracy + "%");
    } else {
      var seen = 0, right = 0;
      Object.keys(docs.qstats.q).forEach(function (id) {
        var h = docs.qstats.q[id].h || "";
        if (!h) return;
        seen++;
        if (h.charAt(h.length - 1) === "1") right++;
      });
      lines.push("Overall: " + seen + " questions seen, last answer correct on " + pct(right, seen) + "%");
    }
    var mocks = list.filter(function (a) { return a.kind === "mock"; });
    if (mocks.length) {
      lines.push("Mock exams: " + mocks.map(function (a) { return a.ref + " " + a.pct + "%" + (a.over ? " (over time)" : ""); }).join(", "));
    }
    if (c && c.domains) {
      lines.push("Domains: " + Object.keys(c.domains).sort().map(function (k) {
        return k.toUpperCase() + " " + c.domains[k].acc + "% of " + c.domains[k].n;
      }).join(", "));
    } else if (list.length) {
      var dom = {};
      list.forEach(function (a) {
        Object.keys(a.domains || {}).forEach(function (k) {
          dom[k] = dom[k] || {c: 0, n: 0};
          dom[k].c += a.domains[k].c || 0;
          dom[k].n += a.domains[k].n || 0;
        });
      });
      lines.push("Domains (from attempts): " + Object.keys(dom).sort().map(function (k) {
        return k.toUpperCase() + " " + pct(dom[k].c, dom[k].n) + "% of " + dom[k].n;
      }).join(", "));
    }
    if (c && c.weakTopics && c.weakTopics.length) {
      lines.push("Weak topics: " + c.weakTopics.map(function (t) { return t.topic + " " + t.acc + "% of " + t.n; }).join(", "));
    }
    if (c && c.missed && c.missed.length) {
      lines.push("Missed questions: " + c.missed.slice(0, 30).map(function (m) { return m.id + (m.c ? " (" + m.c + ")" : ""); }).join(", "));
    }
    if (c && c.confusions && c.confusions.length) {
      lines.push("Pairs I confuse: " + c.confusions.slice(0, 5).map(function (x) { return x.a + " / " + x.b + " (" + x.n + ")"; }).join(", "));
    }
    if (c && c.whyCounts) {
      lines.push("Why I missed (K did not know, C confused, W missed a word, T time, D old limit): " +
        ["K", "C", "W", "T", "D"].map(function (k) { return k + " " + (c.whyCounts[k] || 0); }).join(", "));
    }
    if (c && c.unreadPass && c.unreadPass.length) lines.push("Chapters with unread Pass sections: " + c.unreadPass.join(", "));
    var s = docs.root.settings;
    if (s.examDate) lines.push("Exam date: " + s.examDate);
    lines.push("Plan " + String(s.plan || "a").toUpperCase() + (s.planStart ? ", Day 1 was " + s.planStart : ", not started"));
    return lines.join("\n");
  }

  function snapshot() {
    var snap = {v: 1, docs: clone(docs), outbox: outboxView(), uid: uid};
    if (memory) { snap.attempts = clone(attempts); snap.drafts = clone(drafts); }
    if (JSON.stringify(snap).length > SNAP_MAX) {
      if (memory) {
        Object.keys(snap.attempts).forEach(function (id) { delete snap.attempts[id].answers; delete snap.attempts[id].order; });
        Object.keys(snap.outbox).forEach(function (k) { if (k.indexOf("attempts/") === 0) delete snap.outbox[k]; });
      } else {
        snap.docs = {exam: snap.docs.exam};
      }
    }
    return snap;
  }

  /* ---------- preview helpers ---------- */

  function load(given) {
    if (!docs.root) init();
    Object.keys(given || {}).forEach(function (k) {
      if (k === "settings") docs.root.settings = M.deep(defaults("root").settings, given[k]);
      else if (k === "ui") ui = shaped("ui", given[k]);
      else if (k === "attempts") attempts = M.attempts(given[k], null);
      else if (k === "coach") coach = clone(given[k]);
      else if (k === "drills") drills = clone(given[k]) || [];
      else if (NAMES.indexOf(k) >= 0) docs[k] = shaped(k, given[k]);
    });
    outbox = {};
    changed("*", "remote");
  }

  function reset() {
    cancelTimers();
    NAMES.forEach(function (name) { docs[name] = defaults(name); });
    ui = defaults("ui");
    attempts = {}; drafts = {}; outbox = {}; known = {}; drills = []; coach = null; baks = {};
    retried = false; pauseUntil = 0;
    Object.keys(KEY).forEach(function (k) { if (k !== "probe") lsSet(KEY[k], null); });
    changed("*", "remote");
  }

  /* ---------- cloud ---------- */

  function switchUser(next) {
    var old = uid;
    if (old && old !== next) {
      var bak = {docs: clone(docs), attempts: clone(attempts), outbox: outboxView()};
      var prev = lsGet(KEY.bakid);
      if (typeof prev === "string" && prev && prev !== old) lsSet("saa1:bak:" + prev, null);
      baks = {};
      baks[old] = bak;
      lsSet("saa1:bak:" + old, bak);
      lsSet(KEY.bakid, old);
      NAMES.forEach(function (name) { docs[name] = defaults(name); touch(name, "force"); });
      attempts = {}; outbox = {}; coach = null; known = {};
      touch("attempts", "force");
      touch("outbox");
    }
    var mine = baks[next] || lsGet("saa1:bak:" + next);
    if (old !== next && M.isObj(mine)) {
      NAMES.forEach(function (name) {
        if (mine.docs && M.isObj(mine.docs[name])) { docs[name] = M.doc(name, docs[name], mine.docs[name]); touch(name, "force"); }
      });
      attempts = M.attempts(attempts, mine.attempts || null);
      Object.keys(mine.outbox || {}).forEach(function (k) { if (!outbox[k]) outbox[k] = mine.outbox[k]; });
      touch("attempts", "force");
      touch("outbox");
      delete baks[next];
      lsSet("saa1:bak:" + next, null);
      lsSet(KEY.bakid, null);
    }
    uid = next;
    touch("uid", "now");
    if (old && old !== next) changed("*", "remote");
  }

  function fetchAll() {
    var jobs = NAMES.map(function (name) { return docRef(PATH[name]).get(); });
    jobs.push(db.collection("study/" + uid + "/attempts").orderBy("submittedAt", "desc").limit(200).get());
    return Promise.all(jobs);
  }

  function applyRemote(res) {
    NAMES.forEach(function (name, i) {
      var snap = res[i], key = PATH[name];
      var remote = snap && snap.exists ? clone(snap.data()) : null;
      known[key] = !!remote;
      var local = docs[name], merged = M.doc(name, local, remote ? shaped(name, remote) : null);
      docs[name] = merged;
      delete outbox[key];
      if ((local.updatedAt || 0) > 0) {
        if (!remote) outbox[key] = {op: "merge", data: clone(merged)};
        else {
          var p = M.diff(remote, merged);
          if (Object.keys(p).length) outbox[key] = {op: "merge", data: p};
        }
      }
      if (!M.same(local, merged)) touch(name);
    });
    var q = res[NAMES.length], remoteAtt = {};
    ((q && q.docs) || []).forEach(function (s) {
      var a = clone(s.data());
      if (M.isObj(a) && a.id) { remoteAtt[a.id] = a; known["attempts/" + a.id] = true; }
    });
    var before = Object.keys(attempts).length;
    Object.keys(attempts).forEach(function (id) {
      if (!remoteAtt[id]) outbox["attempts/" + id] = {op: "set", data: clone(attempts[id])};
      else delete outbox["attempts/" + id];
    });
    attempts = M.attempts(attempts, remoteAtt);
    trim();
    if (Object.keys(attempts).length !== before) touch("attempts");
    touch("outbox");
    changed("*", "remote");
  }

  function subErr(e, resub, second) {
    var code = (e && e.code) || "unavailable";
    if (code === "unavailable" && !second) { setTimeout(function () { if (cloud === "on") resub(); }, 5000); return; }
    if (code === "revoked" || code === "not_granted") stopCloud();
  }

  function subDoc(name, second) {
    var un = docRef(PATH[name]).onSnapshot(function (snap) {
      if (cloud !== "on" || !snap || (snap.metadata && snap.metadata.hasPendingWrites) || !snap.exists) return;
      known[PATH[name]] = true;
      var merged = M.doc(name, docs[name], shaped(name, clone(snap.data())));
      if (M.same(merged, docs[name])) return;
      docs[name] = merged;
      touch(name);
      changed(name, "remote");
    }, function (e) { subErr(e, function () { subDoc(name, true); }, second); });
    unsubs.push(un);
  }

  function subDrills(second) {
    var un = db.collection("study/" + uid + "/drills").onSnapshot(function (snap) {
      if (cloud !== "on" || !snap || !snap.docs) return;
      drills = snap.docs.map(function (s) {
        var d = clone(s.data());
        if (M.isObj(d)) d.id = s.id;
        return d;
      }).filter(function (d) { return M.isObj(d) && d.v === 1 && typeof d.title === "string" && Array.isArray(d.items) && d.items.length; });
      emit("store:change", {doc: "drills", source: "remote"});
    }, function (e) { subErr(e, function () { subDrills(true); }, second); });
    unsubs.push(un);
  }

  function seen() {
    var now = SAA.U.now(), r = docs.root;
    if (now - (r.lastSeenAt || 0) <= 86400) return;
    r.lastSeenAt = now;
    if (!r.createdAt) r.createdAt = now;
    if (known["."]) queue(".", "merge", {lastSeenAt: now});
    else queue(".", "merge", clone(r));
    touch("root");
  }

  function wait(ms) { return new Promise(function (ok) { setTimeout(ok, ms); }); }

  async function doAttach(d, u) {
    if (!docs.root) init();
    db = d;
    switchUser(u);
    var res;
    try { res = await fetchAll(); } catch (e) {
      var code = (e && e.code) || "unavailable";
      if (STOP[code] || code === "quota_exceeded" || code === "resource_exhausted") throw e;
      await wait(1000 + Math.floor(Math.random() * 2000));
      res = await fetchAll();
    }
    applyRemote(res);
    cloud = "on";
    consent = null;
    subDoc("progress");
    subDoc("qstats");
    subDoc("exam");
    subDrills();
    seen();
    setStatus();
    flush();
    return true;
  }

  function attach(d, u) {
    if (!d || !u || dead) { setStatus(); return Promise.resolve(false); }
    if (attachP) return attachP;
    attachP = doAttach(d, u).then(function (ok) { return ok; }, function (e) {
      var code = (e && e.code) || "unavailable";
      attachP = null;
      if (STOP[code]) stopCloud(); else setStatus();
      return false;
    });
    return attachP;
  }

  SAA.Store = {
    init: init, get: get, patch: patch, replace: replace, stamp: stamp, save: save, draft: draft,
    consent: setConsent, importAll: importAll, exportAll: exportAll, summaryText: summaryText,
    load: load, reset: reset, addAttempt: addAttempt,
    attempts: function () { return attemptList(); },
    drills: function () { return drills.slice(); },
    flag: flag, attach: attach, flush: flush, snapshot: snapshot,
    status: statusName,
    info: function () {
      return {status: statusName(), memory: memory, consent: consent, cloud: cloud === "on", stopped: dead,
        pending: Object.keys(outboxView()).length};
    },
    coach: function () { return coach; },
    refreshCoach: refreshCoach
  };
})(globalThis.SAA = globalThis.SAA || {});
