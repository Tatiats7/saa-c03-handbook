/* content.js (owner B). Loads the published JSON files, from the network or from the inline block. */
(function (SAA) {
  "use strict";

  var U = SAA.U, bus = SAA.bus;
  var Content = SAA.Content = SAA.Content || {};

  var RANK = {fast: 0, pass: 1, full: 2};
  var CACHE_MAX = 5;
  var SHARD_DIR = "f/";

  var inline;            /* undefined: not looked up yet; null: network mode; object: inline map */
  var single = {};       /* path -> promise of the files that are kept for the visit */
  var cache = [];        /* [{path, slug, hash, promise}] for c/, d/ and q/ files, newest last */
  var manifestP = null, manifestObj = null;
  var metaBySlug = {}, secBySlug = {};
  var spriteP = null;

  function inlineMap() {
    if (inline !== undefined) return inline;
    inline = null;
    try {
      var el = document.getElementById("saa-inline");
      if (el && el.textContent) inline = JSON.parse(el.textContent);
    } catch (e) { inline = null; }
    return inline;
  }

  function fail(path) {
    bus.emit("content:error", {path: path});
    return Promise.reject({path: path});
  }

  /* kind: "json" | "text" | "blob". Resolves null (never rejects) for a file that is absent from the inline map. */
  function load(path, kind) {
    var map = inlineMap();
    if (map) {
      if (!Object.prototype.hasOwnProperty.call(map, path)) {
        return kind === "json" ? Promise.resolve(null) : fail(path);
      }
      var v = map[path];
      if (kind === "json") return Promise.resolve(typeof v === "string" ? safeParse(v, path) : v);
      var text = typeof v === "string" ? v : JSON.stringify(v);
      if (kind === "text") return Promise.resolve(text);
      return Promise.resolve(new Blob([text]));
    }
    var req;
    try { req = fetch(path, {cache: "no-cache"}); } catch (e) { return fail(path); }
    return req.then(function (res) {
      if (!res.ok) throw new Error("status " + res.status);
      return kind === "json" ? res.json() : kind === "text" ? res.text() : res.blob();
    }).then(null, function () { return fail(path); });
  }

  function safeParse(text, path) {
    try { return JSON.parse(text); } catch (e) { bus.emit("content:error", {path: path}); throw {path: path}; }
  }

  function once(path) {
    if (!single[path]) {
      single[path] = load(path, "json").then(null, function (err) { delete single[path]; throw err; });
    }
    return single[path];
  }

  function cached(path, slug) {
    for (var i = 0; i < cache.length; i++) {
      if (cache[i].path === path) {
        var hit = cache.splice(i, 1)[0];
        cache.push(hit);
        return hit.promise;
      }
    }
    var meta = slug ? metaBySlug[slug] : null;
    var entry = {path: path, slug: slug || null, hash: meta ? meta.hash : null, promise: null};
    entry.promise = load(path, "json").then(null, function (err) {
      var j = cache.indexOf(entry);
      if (j !== -1) cache.splice(j, 1);
      throw err;
    });
    cache.push(entry);
    while (cache.length > CACHE_MAX) cache.shift();
    return entry.promise;
  }

  function index(manifest) {
    var oldHash = {};
    Object.keys(metaBySlug).forEach(function (slug) { oldHash[slug] = metaBySlug[slug].hash; });
    metaBySlug = {};
    secBySlug = {};
    (manifest.chapters || []).forEach(function (ch) { metaBySlug[ch.slug] = ch; });
    var dropped = [];
    cache = cache.filter(function (entry) {
      if (!entry.slug) return true;
      var meta = metaBySlug[entry.slug];
      var keep = meta && meta.hash === entry.hash;
      if (!keep && dropped.indexOf(entry.slug) === -1) dropped.push(entry.slug);
      return keep;
    });
    Object.keys(oldHash).forEach(function (slug) {
      var meta = metaBySlug[slug];
      if ((!meta || meta.hash !== oldHash[slug]) && dropped.indexOf(slug) === -1) dropped.push(slug);
    });
    return dropped;
  }

  /* Content.manifest() resolves the cached manifest. Content.manifest(true) fetches it again,
     drops the cached files of chapters whose hash changed and emits "content:drop" {slugs}. */
  Content.manifest = function (refresh) {
    if (manifestP && !refresh) return manifestP;
    var first = !manifestObj;
    var p = load("manifest.json", "json").then(function (m) {
      if (!m) return fail("manifest.json");
      var changed = !manifestObj || manifestObj.build !== m.build;
      if (manifestObj) dropFacts(manifestObj.factsIndex, m.factsIndex);
      manifestObj = m;
      var dropped = index(m);
      if (SAA.state) SAA.state.manifest = m;
      if (first || changed) bus.emit("manifest", m);
      if (!first && dropped.length) bus.emit("content:drop", {slugs: dropped});
      return m;
    });
    if (first || !manifestP) {
      manifestP = p.then(null, function (err) { if (!manifestObj) manifestP = null; throw err; });
      return manifestP;
    }
    return p.then(function (m) { manifestP = Promise.resolve(m); return m; });
  };

  Content.meta = function (slug) { return metaBySlug[slug] || null; };

  function rowObject(row) {
    return {sid: row[0], part: row[1], kind: row[2], route: row[3], min: row[4], title: row[5],
            parent: row[6] === undefined ? null : row[6], role: row[7] === undefined ? null : row[7]};
  }

  function sections(slug) {
    if (secBySlug[slug]) return secBySlug[slug];
    var meta = metaBySlug[slug];
    if (!meta) return null;
    var list = (meta.sections || []).map(rowObject), map = {}, kids = {};
    list.forEach(function (s) {
      if (!map[s.part + "." + s.sid]) map[s.part + "." + s.sid] = s;
      if (!map[s.sid]) map[s.sid] = s;
      if (s.kind === 3 && s.parent) kids[s.part + "." + s.parent] = true;
    });
    secBySlug[slug] = {list: list, map: map, kids: kids};
    return secBySlug[slug];
  }

  /* Content.section(slug, sid) or Content.section(slug, "part.sid"). */
  Content.section = function (slug, sid) {
    var s = sections(slug);
    return (s && s.map[sid]) || null;
  };

  /* Every section row of a chapter as objects, in document order (optionally of one part). */
  Content.sections = function (slug, part) {
    var s = sections(slug);
    if (!s) return [];
    return part ? s.list.filter(function (r) { return r.part === part; }) : s.list.slice();
  };

  Content.routeSections = function (slug, route) {
    var s = sections(slug);
    if (!s) return [];
    var max = RANK[route] === undefined ? RANK.pass : RANK[route];
    return s.list.filter(function (r) {
      if (r.kind !== 2 && r.kind !== 3) return false;
      if ((RANK[r.route] === undefined ? RANK.full : RANK[r.route]) > max) return false;
      if (r.kind === 2 && s.kids[r.part + "." + r.sid]) return false;
      return true;
    });
  };

  Content.progress = function (slug, route, progress) {
    var rows = Content.routeSections(slug, route);
    var ch = progress && progress.chapters && progress.chapters[slug];
    var stamps = (ch && ch.read) || {};
    var read = 0;
    for (var i = 0; i < rows.length; i++) if (stamps[rows[i].sid] > 0) read++;
    return {read: read, total: rows.length};
  };

  Content.chapter = function (slug) {
    return Content.manifest().then(function () {
      var meta = metaBySlug[slug];
      if (!meta || meta.status === "planned" || !meta.files || !meta.files.length) return null;
      return cached("c/" + slug + ".json", slug);
    });
  };

  Content.data = function (slug) {
    return Content.manifest().then(function () {
      var meta = metaBySlug[slug];
      if (!meta || meta.status === "planned" || !meta.d) return null;
      return cached("d/" + slug + ".json", slug);
    });
  };

  Content.mock = function (slug) {
    return Content.manifest().then(function (m) {
      var hit = (m.mocks || []).filter(function (x) { return x.slug === slug; })[0];
      return hit ? cached(hit.file || ("q/" + slug + ".json"), null) : null;
    });
  };

  Content.drill = function (id) {
    return Content.manifest().then(function (m) {
      var hit = (m.drills || []).filter(function (x) { return x.id === id; })[0];
      return hit ? cached(hit.file || ("q/" + id + ".json"), null) : null;
    });
  };

  Content.glossary = function () { return once("glossary.json"); };
  Content.plan = function () { return once("plan.json"); };
  Content.qindex = function () { return once("qindex.json"); };

  /* ---- facts: one shard per service (f/<service>.json), found through facts-index.json (ARCHITECTURE 2.4) */

  /* After a manifest refresh: forget the index and every shard when the index changed (a republish). */
  function dropFacts(oldRow, newRow) {
    if (!oldRow || (newRow && newRow.sha256 === oldRow.sha256)) return;
    Object.keys(single).forEach(function (path) {
      if (path === oldRow.path || path.indexOf(SHARD_DIR) === 0) delete single[path];
    });
  }

  /* Resolves facts-index.json: {v, count, shards: {service: {path, bytes, sha256, count}}, stray: {id: service}}, or null. */
  Content.factsIndex = function () {
    return Content.manifest().then(function (m) {
      var row = m && m.factsIndex;
      return row && row.path ? once(row.path) : null;
    });
  };

  /* The service whose shard holds fact `id` (pure): stray[id] when listed, else the longest service key k
     of the index with the id starting "k-" (fact ids are "<service>-<topic>"). Null when no key fits. */
  Content.factService = function (id, index) {
    var shards = (index && index.shards) || {}, stray = (index && index.stray) || {}, best = null;
    id = String(id || "");
    if (Object.prototype.hasOwnProperty.call(stray, id) && Object.prototype.hasOwnProperty.call(shards, stray[id])) return stray[id];
    Object.keys(shards).forEach(function (key) {
      if (id.indexOf(key + "-") === 0 && (best === null || key.length > best.length)) best = key;
    });
    return best;
  };

  /* Resolves the shard of one service ({v, service, facts: {id: fact card}}), loaded once per visit; null when unknown. */
  Content.factShard = function (service) {
    return Content.factsIndex().then(function (index) {
      var row = index && index.shards && Object.prototype.hasOwnProperty.call(index.shards, service) ? index.shards[service] : null;
      return row && row.path ? once(row.path) : null;
    });
  };

  /* Resolves the fact card of one id, or null. Loads at most one shard. */
  Content.fact = function (id) {
    return Content.factsIndex().then(function (index) {
      var service = Content.factService(id, index);
      if (!service) return null;
      return Content.factShard(service).then(function (shard) {
        var facts = (shard && shard.facts) || {};
        return Object.prototype.hasOwnProperty.call(facts, id) ? facts[id] : null;
      });
    });
  };
  Content.sindex = function () {
    return Content.qindex().then(function (qi) { return (qi && qi.s) || {}; });
  };

  Content.text = function (path) { return load(path, "text"); };
  Content.blob = function (path) { return load(path, "blob"); };

  /* Loads the d/ and q/ files that hold the given question ids. */
  Content.questions = function (ids) {
    ids = ids || [];
    return Promise.all([Content.manifest(), Content.qindex()]).then(function (both) {
      var manifest = both[0], qi = (both[1] && both[1].q) || {};
      var mockSlugs = {};
      (manifest.mocks || []).forEach(function (x) { mockSlugs[x.slug] = x.file || ("q/" + x.slug + ".json"); });
      var files = {}, order = [];
      ids.forEach(function (id) {
        var row = qi[id];
        if (!row) return;
        var path = row[3] === 2 ? (mockSlugs[row[0]] || ("q/" + row[0] + ".json")) : "d/" + row[0] + ".json";
        if (!files[path]) { files[path] = row[3] === 2 ? null : row[0]; order.push(path); }
      });
      /* one file at a time, so that the small cache is never asked for more than it holds */
      var out = {q: {}, facts: {}}, want = {};
      ids.forEach(function (id) { want[id] = true; });
      return order.reduce(function (chain, path) {
        return chain.then(function () { return cached(path, files[path]); }).then(function (file) {
          if (!file) return;
          (file.questions || []).forEach(function (q) { if (want[q.id]) out.q[q.id] = q; });
          var facts = file.facts || {};
          Object.keys(facts).forEach(function (fid) { out.facts[fid] = facts[fid]; });
        });
      }, Promise.resolve()).then(function () { return out; });
    });
  };

  Content.prefetch = function (slug) {
    function run() {
      var meta = metaBySlug[slug];
      if (!meta || meta.status === "planned") return;
      Content.chapter(slug).then(null, function () {});
    }
    if (inlineMap()) return;
    if (typeof requestIdleCallback === "function") requestIdleCallback(run, {timeout: 4000});
    else setTimeout(run, 2000);
  };

  /* Puts the icon sprite into #saa-sprite once. Resolves true when the sprite is in the page. */
  Content.sprite = function () {
    if (spriteP) return spriteP;
    var host = document.getElementById("saa-sprite");
    if (!host) return Promise.resolve(false);
    if (host.childNodes.length) { spriteP = Promise.resolve(true); return spriteP; }
    spriteP = load("assets/icons.svg", "text").then(function (text) {
      var body = String(text).replace(/<\?xml[^>]*\?>/, "").replace(/<![A-Za-z][^>]*>/, "");   /* a document type line; the literal is not written here (the page must not hold it) */
      U.set(host, U.raw(body));
      return true;
    }).then(null, function () { spriteP = null; return false; });
    return spriteP;
  };

  /* For tests: forget everything that was loaded. */
  Content._reset = function () {
    inline = undefined; single = {}; cache = []; manifestP = null; manifestObj = null;
    metaBySlug = {}; secBySlug = {}; spriteP = null;
  };

})(globalThis.SAA = globalThis.SAA || {});
