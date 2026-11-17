/* scoring.js (pure): the rules of ARCHITECTURE.md section 7.1.
   No browser global, no storage, no clock. Loaded by node in tests. */
(function (SAA) {
  "use strict";

  var CAUSES = ["K", "C", "W", "T", "D"];
  var ROUTE_RANK = { fast: 0, pass: 1, full: 2 };

  /* ---------- small helpers ---------- */

  function map() { return Object.create(null); }

  function setOf(list) {
    var s = map(), i;
    list = list || [];
    for (i = 0; i < list.length; i++) s[String(list[i])] = 1;
    return s;
  }

  function pct(c, n) { return n ? Math.round(100 * c / n) : 0; }

  function last(str) { return str ? str.charAt(str.length - 1) : ""; }

  function count(str, ch) {
    var n = 0, i;
    str = str || "";
    for (i = 0; i < str.length; i++) if (str.charAt(i) === ch) n++;
    return n;
  }

  /* A seeded generator (mulberry32), so that a mix is the same for one day. */
  function rng(seed) {
    var a = (Number(seed) || 0) >>> 0;
    return function () {
      a = (a + 0x6D2B79F5) >>> 0;
      var t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function shuffled(list, rnd) {
    var a = list.slice(), i, j, x;
    for (i = a.length - 1; i > 0; i--) {
      j = Math.floor(rnd() * (i + 1));
      x = a[i]; a[i] = a[j]; a[j] = x;
    }
    return a;
  }

  /* The local day number of a time in whole seconds. Uses U.day when util.js is loaded. */
  function dayOf(now) {
    var ms = now * 1000;
    if (SAA.U && typeof SAA.U.day === "function") return SAA.U.day(ms);
    return Math.floor((ms - new Date(ms).getTimezoneOffset() * 60000) / 86400000);
  }

  /* qindex row: [slug, domain, layer, pool, concept, keyRev, [topics]] */
  function rowOf(qindex, id) {
    var q = qindex && qindex.q;
    return q && Object.prototype.hasOwnProperty.call(q, id) ? q[id] : null;
  }

  /* A record counts only when the question exists and the answer key did not change. */
  function validRec(rec, row) {
    if (!rec || !row || typeof rec.h !== "string" || !rec.h) return false;
    return rec.kr == null || row[5] == null || rec.kr === row[5];
  }

  function records(qstats, qindex) {
    var out = [], qs = (qstats && qstats.q) || {}, ids = Object.keys(qs).sort(), i, row;
    for (i = 0; i < ids.length; i++) {
      row = rowOf(qindex, ids[i]);
      if (validRec(qs[ids[i]], row)) out.push({ id: ids[i], rec: qs[ids[i]], row: row });
    }
    return out;
  }

  /* ---------- answers ---------- */

  function correctIds(q) {
    var out = [], i, o = (q && q.options) || [];
    for (i = 0; i < o.length; i++) if (o[i] && o[i].ok === true) out.push(String(o[i].id));
    return out;
  }

  function isCorrect(q, picked) {
    var want = setOf(correctIds(q)), n = Object.keys(want).length, seen = map(), m = 0, i, id;
    if (!n || !Array.isArray(picked)) return false;
    for (i = 0; i < picked.length; i++) {
      id = String(picked[i]);
      if (seen[id]) continue;
      seen[id] = 1;
      if (!want[id]) return false;
      m++;
    }
    return m === n;
  }

  function domainBreakdown(questions, answers) {
    var out = { d1: { c: 0, n: 0 }, d2: { c: 0, n: 0 }, d3: { c: 0, n: 0 }, d4: { c: 0, n: 0 } };
    var i, q, key, a;
    answers = answers || {};
    for (i = 0; i < questions.length; i++) {
      q = questions[i];
      key = "d" + (q.d || 0);
      if (!out[key]) out[key] = { c: 0, n: 0 };
      a = answers[q.id];
      out[key].n++;
      if (a && isCorrect(q, a.p)) out[key].c++;
    }
    return out;
  }

  function scoreAttempt(questions, answers, meta) {
    var doc, i, j, q, a, ok, u, topics = {}, t, correct = 0, sure = 0, out = {};
    answers = answers || {};
    meta = meta || {};
    for (i = 0; i < questions.length; i++) {
      q = questions[i];
      a = answers[q.id] || {};
      ok = isCorrect(q, a.p);
      u = a.u ? 1 : 0;
      if (ok) { correct++; if (!u) sure++; }
      t = q.topics || [];
      for (j = 0; j < t.length; j++) {
        if (!topics[t[j]]) topics[t[j]] = { c: 0, n: 0 };
        topics[t[j]].n++;
        if (ok) topics[t[j]].c++;
      }
      out[q.id] = { p: Array.isArray(a.p) ? a.p.slice() : [], ok: ok ? 1 : 0, u: u, ms: Math.round(a.ms || 0) };
    }
    doc = {
      v: 1,
      id: meta.id,
      kind: meta.kind,
      ref: meta.ref == null ? null : meta.ref,
      first: meta.first ? 1 : 0,
      over: meta.over ? 1 : 0,
      startedAt: meta.startedAt || 0,
      submittedAt: meta.submittedAt || 0,
      activeSec: Math.round(meta.activeSec || 0),
      limitSec: meta.limitSec == null ? null : meta.limitSec,
      build: meta.build == null ? null : meta.build,
      total: questions.length,
      correct: correct,
      pct: pct(correct, questions.length),
      sureCorrect: sure,
      domains: domainBreakdown(questions, answers),
      topics: topics,
      order: Array.isArray(meta.order) ? meta.order.slice() : questions.map(function (x) { return x.id; }),
      answers: out
    };
    return doc;
  }

  /* ---------- the question record (qstats) ---------- */

  function nextBox(rec, ok, unsure, day) {
    var box = (rec && rec.box) || 0;
    if (!ok) return 0;
    if (unsure) return Math.min(box, 1);
    if (rec && rec.d != null && rec.d === day) return box;
    return box + 1;
  }

  function record(rec, q, picked, ok, unsure, now, cause) {
    var kr = q && q.keyRev != null ? q.keyRev : null, day = dayOf(now), out;
    if (rec && rec.kr != null && kr != null && rec.kr !== kr) rec = null;
    out = {
      h: (((rec && rec.h) || "") + (ok ? "1" : "0")).slice(-8),
      u: (((rec && rec.u) || "") + (unsure ? "1" : "0")).slice(-8),
      t: now,
      d: ok ? day : (rec && rec.d != null ? rec.d : null),
      box: nextBox(rec, ok, unsure, day),
      pick: (Array.isArray(picked) ? picked.slice() : []).map(String).sort(),
      c: null,
      kr: kr
    };
    if (cause && CAUSES.indexOf(cause) >= 0) out.c = cause;
    else if (ok && rec && rec.c) out.c = rec.c;
    return out;
  }

  function inMistakes(rec) {
    if (!rec) return false;
    return ((rec.h || "").indexOf("0") >= 0 || (rec.u || "").indexOf("1") >= 0) && (rec.box || 0) < 2;
  }

  /* Why the question is in the log: the latest wrong answer or not-sure mark. */
  function lastReason(rec) {
    var h = rec.h || "", u = rec.u || "", i;
    for (i = Math.max(h.length, u.length) - 1; i >= 0; i--) {
      if (h.charAt(i) === "0") return "wrong";
      if (u.charAt(i) === "1") return "unsure";
    }
    return "wrong";
  }

  function mistakes(qstats, qindex) {
    var list = records(qstats, qindex), rows = [], i, r, rec;
    for (i = 0; i < list.length; i++) {
      rec = list[i].rec;
      if (!inMistakes(rec)) continue;
      r = {
        id: list[i].id, slug: list[i].row[0], d: list[i].row[1], box: rec.box || 0,
        last: lastReason(rec), c: rec.c || null, t: rec.t || 0
      };
      r.rank = (last(rec.h) === "0" && last(rec.u) !== "1") ? 0 : (r.box === 0 ? 1 : 2);
      rows.push(r);
    }
    rows.sort(function (a, b) {
      return a.rank - b.rank || a.t - b.t || (a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
    });
    for (i = 0; i < rows.length; i++) delete rows[i].rank;
    return rows;
  }

  function retryList(qstats, qindex, n) {
    n = n == null ? 20 : n;
    return mistakes(qstats, qindex).slice(0, n).map(function (r) { return r.id; });
  }

  /* ---------- question choice ---------- */

  function buildMix(qindex, qstats, readSlugs, order, day, n) {
    var qi = (qindex && qindex.q) || {}, qs = (qstats && qstats.q) || {};
    var read = setOf(readSlugs), pos = map(), fresh = [], older = [], missed, inMk, ids, i, id, row, rec;
    var out = [], used = map(), groups, quota, g, progress;
    n = n == null ? 10 : n;
    for (i = 0; i < (order || []).length; i++) pos[order[i]] = i;
    missed = mistakes(qstats, qindex).filter(function (r) { return rowOf(qindex, r.id)[3] !== 2; })
      .map(function (r) { return r.id; });
    inMk = setOf(missed);
    ids = Object.keys(qi).sort();
    for (i = 0; i < ids.length; i++) {
      id = ids[i]; row = qi[id];
      if (row[3] === 2) continue;
      rec = validRec(qs[id], row) ? qs[id] : null;
      if (!rec) {
        if (row[3] === 0 && row[2] === 0 && read[row[0]]) fresh.push(id);
      } else if (!inMk[id] && last(rec.h) === "1") {
        older.push(id);
      }
    }
    function place(x) { return pos[qi[x][0]] == null ? 1e9 : pos[qi[x][0]]; }
    fresh.sort(function (a, b) { return place(a) - place(b) || (a < b ? -1 : a > b ? 1 : 0); });
    older.sort(function (a, b) { return (qs[a].t || 0) - (qs[b].t || 0) || (a < b ? -1 : a > b ? 1 : 0); });
    groups = [fresh, older, missed];
    quota = [Math.round(n * 0.4), Math.round(n * 0.3), 0];
    quota[2] = Math.max(0, n - quota[0] - quota[1]);
    function take(list, k) {
      while (k > 0 && list.length && out.length < n) {
        var x = list.shift();
        if (used[x]) continue;
        used[x] = 1; out.push(x); k--;
      }
    }
    for (g = 0; g < 3; g++) take(groups[g], quota[g]);
    do {
      progress = out.length;
      for (g = 0; g < 3; g++) take(groups[g], 1);
    } while (out.length < n && out.length > progress);
    return shuffled(out, rng(day));
  }

  function returnQuestions(slug, order, qindex, qstats, n) {
    var qi = (qindex && qindex.q) || {}, qs = (qstats && qstats.q) || {};
    var at = (order || []).indexOf(slug), back = [1, 3, 6], out = [], i, s, ids, best;
    n = n == null ? 3 : n;
    if (at < 0) return out;
    function score(id) {
      var rec = validRec(qs[id], qi[id]) ? qs[id] : null;
      if (rec && inMistakes(rec)) return [0, rec.t || 0];
      if (!rec) return [1, 0];
      return [2, rec.t || 0];
    }
    for (i = 0; i < back.length && out.length < n; i++) {
      s = order[at - back[i]];
      if (!s) continue;
      ids = Object.keys(qi).sort().filter(function (id) {
        return qi[id][0] === s && qi[id][3] === 0 && qi[id][2] === 0;
      });
      if (!ids.length) continue;
      best = ids.map(function (id) { return { id: id, s: score(id) }; }).sort(function (a, b) {
        return a.s[0] - b.s[0] || a.s[1] - b.s[1] || (a.id < b.id ? -1 : 1);
      })[0];
      out.push(best.id);
    }
    return out;
  }

  function confusions(qstats, qindex) {
    var list = records(qstats, qindex), wrong = (qindex && qindex.wrong) || {}, pairs = map(), out = [], i, j, r, w, a, b, key, p;
    for (i = 0; i < list.length; i++) {
      r = list[i];
      if (last(r.rec.h) !== "0") continue;
      w = wrong[r.id] || {};
      a = r.row[4];
      p = r.rec.pick || [];
      for (j = 0; j < p.length; j++) {
        b = w[p[j]];
        if (!a || !b || a === b) continue;
        key = a < b ? a + "|" + b : b + "|" + a;
        if (!pairs[key]) pairs[key] = { a: a < b ? a : b, b: a < b ? b : a, n: 0 };
        pairs[key].n++;
      }
    }
    for (key in pairs) out.push(pairs[key]);
    out.sort(function (x, y) { return y.n - x.n || (x.a < y.a ? -1 : x.a > y.a ? 1 : (x.b < y.b ? -1 : 1)); });
    return out;
  }

  /* ---------- readiness gate (her study rule, numbers from shell.json) ---------- */

  function gate(attempts, cfg) {
    var needed, list, strong = 0, soft = true, i, k, d, state = "not-yet";
    cfg = cfg || {};
    needed = cfg.needed || 2;
    list = (attempts || []).filter(function (a) {
      return a && a.kind === "mock" && a.first === 1 && !a.over;
    }).sort(function (a, b) { return (b.submittedAt || 0) - (a.submittedAt || 0); }).slice(0, needed);
    for (i = 0; i < list.length; i++) {
      if (list[i].pct >= cfg.strong) strong++;
      if (!(list[i].pct >= cfg.soft)) soft = false;
      d = list[i].domains || {};
      for (k in d) if (d[k] && d[k].n > 0 && pct(d[k].c, d[k].n) < cfg.domainMin) soft = false;
    }
    if (list.length >= needed) {
      if (strong === list.length) state = "go";
      else if (soft) state = "go-soft";
    }
    return {
      state: state, strong: strong, counted: list.length, needed: needed,
      text: strong + " of " + needed + " mocks at " + cfg.strong + "%"
    };
  }

  /* ---------- coach document (read by Claude) ---------- */

  /* The same rule as Content.routeSections, on the manifest rows
     [sid, part, kind, route, minutes, title, parent, role]. */
  function routeRows(rows, route) {
    var max = ROUTE_RANK[route] == null ? 1 : ROUTE_RANK[route], hasKids = map(), i, r, out = [];
    rows = rows || [];
    for (i = 0; i < rows.length; i++) if (rows[i][2] === 3 && rows[i][6]) hasKids[rows[i][6]] = 1;
    for (i = 0; i < rows.length; i++) {
      r = rows[i];
      if (r[2] !== 2 && r[2] !== 3) continue;
      if ((ROUTE_RANK[r[3]] == null ? 2 : ROUTE_RANK[r[3]]) > max) continue;
      if (r[2] === 2 && hasKids[r[0]]) continue;
      out.push(r);
    }
    return out;
  }

  function buildCoach(state, qindex, manifest, now) {
    var settings = state.settings || {}, progress = state.progress || {}, speak = state.speak || {};
    var attempts = state.attempts || [], qstats = state.qstats || {};
    var list = records(qstats, qindex), i, j, r, ok, unsure, key, t;
    var seen = 0, right = 0, sureN = 0, sureRight = 0, dom = {}, topics = map(), why = { K: 0, C: 0, W: 0, T: 0, D: 0 };
    var missed = [], lucky = [], weak = [], unread = [], speakWeak = [], mocks = [], limit, chapters, ch, rows, rd, items, ids;
    limit = (state.cfg && state.cfg.gate && state.cfg.gate.strong) || 80;
    for (i = 0; i < list.length; i++) {
      r = list[i];
      ok = last(r.rec.h) === "1";
      unsure = last(r.rec.u) === "1";
      seen++;
      if (ok) right++;
      if (!unsure) { sureN++; if (ok) sureRight++; }
      key = "d" + r.row[1];
      if (!dom[key]) dom[key] = { c: 0, n: 0 };
      dom[key].n++;
      if (ok) dom[key].c++;
      t = r.row[6] || [];
      for (j = 0; j < t.length; j++) {
        if (!topics[t[j]]) topics[t[j]] = { c: 0, n: 0, ch: map() };
        topics[t[j]].n++;
        if (ok) topics[t[j]].c++; else topics[t[j]].ch[r.row[0]] = 1;
      }
      if (r.rec.c && why[r.rec.c] != null && inMistakes(r.rec)) why[r.rec.c]++;
      if (inMistakes(r.rec) && count(r.rec.h, "0") > 0) {
        missed.push({ id: r.id, wrong: count(r.rec.h, "0"), lastPick: (r.rec.pick || []).slice(), c: r.rec.c || null, t: r.rec.t || 0 });
      }
      if (ok && unsure) lucky.push(r.id);
    }
    for (key in dom) dom[key] = { acc: pct(dom[key].c, dom[key].n), n: dom[key].n };
    for (key in topics) {
      if (topics[key].n >= 3 && pct(topics[key].c, topics[key].n) < limit) {
        weak.push({ topic: key, acc: pct(topics[key].c, topics[key].n), n: topics[key].n, chapters: Object.keys(topics[key].ch).sort() });
      }
    }
    weak.sort(function (a, b) { return a.acc - b.acc || b.n - a.n || (a.topic < b.topic ? -1 : 1); });
    missed.sort(function (a, b) { return b.wrong - a.wrong || b.t - a.t || (a.id < b.id ? -1 : 1); });
    missed = missed.slice(0, 20).map(function (m) { return { id: m.id, wrong: m.wrong, lastPick: m.lastPick, c: m.c }; });
    attempts.filter(function (a) { return a && a.kind === "mock"; })
      .sort(function (a, b) { return (a.submittedAt || 0) - (b.submittedAt || 0); })
      .slice(-6).forEach(function (a) { mocks.push({ ref: a.ref, pct: a.pct }); });
    chapters = (manifest && manifest.chapters) || [];
    for (i = 0; i < chapters.length; i++) {
      ch = chapters[i];
      if (ch.status === "planned") continue;
      rows = routeRows(ch.sections, "pass");
      rd = (progress.chapters && progress.chapters[ch.slug] && progress.chapters[ch.slug].read) || {};
      for (j = 0; j < rows.length; j++) {
        if (!(rd[rows[j][0]] > 0)) { unread.push(ch.slug); break; }
      }
    }
    items = speak.items || {};
    ids = Object.keys(items).sort();
    for (i = 0; i < ids.length && speakWeak.length < 10; i++) {
      if (items[ids[i]] && Array.isArray(items[ids[i]].missing) && items[ids[i]].missing.length) {
        speakWeak.push({ id: ids[i], missing: items[ids[i]].missing.slice() });
      }
    }
    return {
      v: 1,
      updatedAt: now,
      examDate: settings.examDate == null ? null : settings.examDate,
      overall: {
        seen: seen,
        bank: (manifest && manifest.counts && manifest.counts.questions) || Object.keys((qindex && qindex.q) || {}).length,
        accuracy: pct(right, seen),
        sureAccuracy: pct(sureRight, sureN),
        mocks: mocks
      },
      domains: dom,
      weakTopics: weak.slice(0, 8),
      missed: missed,
      confusions: confusions(qstats, qindex).slice(0, 10),
      luckyGuesses: lucky.slice(0, 30),
      whyCounts: why,
      unreadPass: unread,
      speakWeak: speakWeak
    };
  }

  /* ---------- a drill question written by Claude (DQ, section 5.2) ---------- */

  var DQ_KEYS = { id: 1, type: 1, select: 1, stem: 1, kw: 1, d: 1, options: 1, expl: 1, take: 1, facts: 1 };
  var DQ_OPT_KEYS = { id: 1, text: 1, ok: 1, why: 1 };

  function text(v, need) { return typeof v === "string" && (!need || v.trim().length > 0); }

  function validQuestion(dq) {
    var k, i, o, ids = map(), okN = 0;
    if (!dq || typeof dq !== "object" || Array.isArray(dq)) return false;
    for (k in dq) if (!DQ_KEYS[k]) return false;
    if (!text(dq.id, true) || !/^[a-z0-9-]+$/.test(dq.id)) return false;
    if (dq.type !== "single" && dq.type !== "multi") return false;
    if (typeof dq.select !== "number" || dq.select % 1 !== 0 || dq.select < 1) return false;
    if (dq.type === "single" && dq.select !== 1) return false;
    if (dq.type === "multi" && dq.select < 2) return false;
    if (!text(dq.stem, true)) return false;
    if (dq.d != null && [1, 2, 3, 4].indexOf(dq.d) < 0) return false;
    if (dq.expl != null && !text(dq.expl)) return false;
    if (dq.take != null && !text(dq.take)) return false;
    if (dq.kw != null && !(Array.isArray(dq.kw) && dq.kw.every(function (x) { return text(x); }))) return false;
    if (dq.facts != null && !(Array.isArray(dq.facts) && dq.facts.every(function (x) { return text(x); }))) return false;
    if (!Array.isArray(dq.options) || dq.options.length < 2 || dq.options.length > 6) return false;
    if (dq.options.length <= dq.select) return false;
    for (i = 0; i < dq.options.length; i++) {
      o = dq.options[i];
      if (!o || typeof o !== "object" || Array.isArray(o)) return false;
      for (k in o) if (!DQ_OPT_KEYS[k]) return false;
      if (!text(o.id, true) || ids[o.id]) return false;
      ids[o.id] = 1;
      if (!text(o.text, true)) return false;
      if (typeof o.ok !== "boolean") return false;
      if (o.why != null && !text(o.why)) return false;
      if (o.ok) okN++;
    }
    return okN === dq.select;
  }

  SAA.Scoring = {
    CAUSES: CAUSES,
    isCorrect: isCorrect,
    correctIds: correctIds,
    scoreAttempt: scoreAttempt,
    domainBreakdown: domainBreakdown,
    nextBox: nextBox,
    record: record,
    inMistakes: inMistakes,
    mistakes: mistakes,
    retryList: retryList,
    buildMix: buildMix,
    returnQuestions: returnQuestions,
    confusions: confusions,
    gate: gate,
    buildCoach: buildCoach,
    validQuestion: validQuestion,
    /* extras used by the practice views */
    pct: pct,
    dayOf: dayOf,
    validRec: validRec,
    routeRows: routeRows
  };
})(globalThis.SAA = globalThis.SAA || {});
