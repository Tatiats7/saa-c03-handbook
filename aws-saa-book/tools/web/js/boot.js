/* boot.js (owner B). App.start, the hot snapshot, capabilities, the contents list and the header state. */
(function (SAA) {
  "use strict";

  var U = SAA.U, bus = SAA.bus, Content = SAA.Content, Router = SAA.Router;
  var App = SAA.App = SAA.App || {};

  var started = false;
  var attachArgs = null;       /* {db, uid} kept for the "Save online too" click */
  var manifestAt = 0;
  var REFRESH_MS = 600000;
  var NAV = {home: "home", plan: "plan", speak: "speak", progress: "progress", mistakes: "practice", quiz: "practice",
             drill: "practice", retry: "practice", mix: "practice", mock: "practice", attempt: "practice",
             cards: "practice"};

  SAA.state = SAA.state || {};
  var state = SAA.state;
  if (!state.route) state.route = {view: "", args: [], hash: ""};
  if (state.manifest === undefined) state.manifest = null;
  if (!state.caps) state.caps = {user: undefined, db: undefined, sample: undefined, downloads: undefined, permissions: undefined};
  if (state.uid === undefined) state.uid = null;
  if (!state.status) state.status = "memory";
  if (!state.cfg) state.cfg = {};
  if (!state.build) state.build = "";
  state.single = !!state.single;
  state.preview = !!state.preview;
  App.caps = state.caps;

  function $(id) { return document.getElementById(id); }
  function step(name, fn) {
    try { return fn(); } catch (e) { console.error("boot: " + name, e); return undefined; }
  }
  function sget(name) {
    try { return SAA.Store ? SAA.Store.get(name) : null; } catch (e) { return null; }
  }
  function isPhone() {
    try { return globalThis.matchMedia("(max-width: 759px)").matches; } catch (e) { return false; }
  }

  /* ---------- settings that change the shell ---------- */

  App.textSize = function (n) {
    var root = $("saa");
    if (!root) return;
    n = n === 0 || n === 2 ? n : 1;
    root.classList.remove("ts-0", "ts-1", "ts-2");
    root.classList.add("ts-" + n);
  };

  /* ---------- contents list ---------- */

  function routeOf(slug, s) {
    var r = (s.routeBy && s.routeBy[slug]) || s.route || "pass";
    return r === "fast" || r === "full" ? r : "pass";
  }

  function chapterRow(ch, curSlug, curPart, s, progress) {
    var num = U.h`<span class="toc-n mono">${ch.id}</span>`;
    if (ch.status === "planned") {
      return U.h`<li class="toc-ch is-planned">${num}<span class="toc-t">${ch.title}</span><span class="toc-st">Not written yet</span></li>`;
    }
    var cur = ch.slug === curSlug;
    var p = Content.progress(ch.slug, routeOf(ch.slug, s), progress);
    var done = p.total > 0 && p.read >= p.total;
    var word = ch.status === "draft" ? "Draft" : done ? "Read" : p.total ? p.read + "/" + p.total : "";
    var bar = p.total
      ? U.h`<progress class="toc-bar" max="${p.total}" value="${p.read}" aria-label="${p.read + " of " + p.total + " sections read"}"></progress>`
      : "";
    var parts = cur
      ? U.h`<ol class="toc-parts">${(ch.files || []).map(function (f) {
          var on = f.key === curPart;
          return U.h`<li><a href="${Router.href("ch", ch.slug, f.key)}"${on ? U.raw(" aria-current=\"page\"") : ""}>${f.title}</a></li>`;
        })}</ol>`
      : "";
    return U.h`<li class="toc-ch${cur ? " is-cur" : ""}${done ? " is-done" : ""}"><a class="toc-a" href="${Router.href("ch", ch.slug)}"${cur && !curPart ? U.raw(" aria-current=\"page\"") : ""}>${num}<span class="toc-t">${ch.title}</span></a><span class="toc-st">${word}</span>${bar}${parts}</li>`;
  }

  function tocHtml(m) {
    var cur = Router.current();
    var curSlug = cur.view === "ch" ? cur.args[0] : "";
    var curPart = "";
    if (curSlug) {
      var tab = document.querySelector("#saa-view .tab[aria-current='page']");
      curPart = cur.args[1] || (tab ? tab.getAttribute("data-part") : "");
    }
    var s = sget("settings") || {}, progress = sget("progress");
    var seen = {};
    var groups = (m.parts || []).map(function (part) {
      var rows = (m.chapters || []).filter(function (ch) { return ch.part === part.id; });
      rows.forEach(function (ch) { seen[ch.slug] = true; });
      if (!rows.length) return "";
      return U.h`<section class="toc-part"><h2 class="toc-pt">${part.title}</h2><ol class="toc-l">${rows.map(function (ch) { return chapterRow(ch, curSlug, curPart, s, progress); })}</ol></section>`;
    });
    var rest = (m.chapters || []).filter(function (ch) { return !seen[ch.slug]; });
    if (rest.length) {
      groups.push(U.h`<section class="toc-part"><h2 class="toc-pt">More</h2><ol class="toc-l">${rest.map(function (ch) { return chapterRow(ch, curSlug, curPart, s, progress); })}</ol></section>`);
    }
    var aliases = m.aliases || {};
    var ref = [["glossary", "Glossary", true], ["numbers", "Numbers", !!aliases.numbers], ["traps", "Traps", !!aliases.traps],
               ["changed", "Changed recently", !!aliases.changed], ["files", "Get files", true], ["about", "About", true]];
    return U.h`<div class="toc-top"><p class="eyebrow">Contents</p><button type="button" class="btn quiet toc-x" data-act="toc">Close</button></div>
      ${groups}
      <section class="toc-part toc-ref"><h2 class="toc-pt">Reference</h2><ul class="toc-l">${ref.filter(function (r) { return r[2]; }).map(function (r) {
        return U.h`<li><a class="toc-a" href="#${r[0]}"${cur.view === r[0] ? U.raw(" aria-current=\"page\"") : ""}>${r[1]}</a></li>`;
      })}</ul></section>`;
  }

  function drawToc() {
    var toc = $("saa-toc"), m = state.manifest;
    if (!toc || !m) return;
    var top = toc.scrollTop;
    U.set(toc, tocHtml(m));
    toc.scrollTop = top;
    var cur = toc.querySelector(".toc-ch.is-cur");
    if (cur && toc.scrollHeight > toc.clientHeight + 4) {
      var box = toc.getBoundingClientRect(), r = cur.getBoundingClientRect();
      if (r.top < box.top || r.bottom > box.bottom) toc.scrollTop += r.top - box.top - 60;
    }
  }
  var drawTocSoon = U.debounce(drawToc, 250);

  function setDrawer(open) {
    var toc = $("saa-toc"), menu = $("saa-menu");
    if (!toc) return;
    toc.classList.toggle("is-open", open);
    if (menu) menu.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) { try { toc.focus({preventScroll: true}); } catch (e) { /* older engines */ } }
  }

  Router.act("toc", function (el, ev, forceOpen) {
    var toc = $("saa-toc");
    if (!toc) return;
    if (isPhone()) {
      var open = forceOpen ? true : !toc.classList.contains("is-open");
      setDrawer(open);
      if (!open && $("saa-menu")) $("saa-menu").focus();
    } else {
      try { toc.focus({preventScroll: true}); } catch (e) { /* older engines */ }
      toc.scrollIntoView({block: "nearest"});
    }
  });

  Router.act("search", function () {
    if (SAA.Search && SAA.Search.open) SAA.Search.open();
    else U.toast("Search is not built yet.");
  });

  function markNav() {
    var cur = Router.current();
    var key = NAV[cur.view] || "";
    var nav = $("saa-nav");
    if (!nav) return;
    Array.prototype.forEach.call(nav.querySelectorAll("a"), function (a) {
      if (a.getAttribute("data-nav") === key) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    });
  }

  /* ---------- capabilities ---------- */

  function use(name) {
    try {
      var c = globalThis.claude;
      if (!c || typeof c.use !== "function") return Promise.resolve(null);
      return Promise.resolve(c.use(name)).then(function (ns) { return ns || null; }, function () { return null; });
    } catch (e) { return Promise.resolve(null); }
  }

  function settle(name) {
    return use(name).then(function (ns) {
      state.caps[name] = ns;
      bus.emit("caps", state.caps);
      return ns;
    });
  }

  /* The click on "Save online too" (and Store itself) may call this. */
  App.attach = function () {
    var St = SAA.Store;
    if (!St || !St.attach) return Promise.resolve();
    var a = attachArgs || {db: null, uid: null};
    return Promise.resolve(St.attach(a.db, a.uid));
  };

  function capabilities() {
    var names = ["user", "db", "sample", "downloads", "permissions"];
    var all = {};
    names.forEach(function (n) { all[n] = settle(n); });
    Promise.all([all.user, all.db, all.permissions]).then(function (r) {
      var user = r[0], db = r[1], perms = r[2];
      var St = SAA.Store;
      var idP = user && user.id ? Promise.resolve().then(function () { return user.id(); }).then(null, function () { return null; })
                                : Promise.resolve(null);
      return idP.then(function (uid) {
        state.uid = uid || null;
        if (!St) return;
        if (!db || !uid) { attachArgs = null; St.attach(null, null); return; }
        attachArgs = {db: db, uid: uid};
        if (!perms || !perms.state) { St.attach(db, uid); return; }
        return Promise.resolve().then(function () { return perms.state("db"); }).then(function (answer) {
          if (answer === "granted") St.attach(db, uid);
          else if (answer === "prompt") { if (St.consent) St.consent("prompt"); }
          else if (answer === "denied") { if (St.consent) St.consent("denied"); }
        }, function () { /* stay local */ });
      });
    }).then(null, function (e) { console.error("boot: capabilities", e); });
  }

  /* ---------- start ---------- */

  function readBoot() {
    var el = $("saa-boot");
    if (!el) return;
    var text = el.textContent || "";
    var a = text.indexOf("{"), b = text.lastIndexOf("}");
    if (a === -1 || b <= a) return;
    var boot = JSON.parse(text.slice(a, b + 1));
    state.build = boot.build || "";
    state.single = !!boot.single;
    state.preview = !!boot.preview;
    state.cfg = boot.cfg || {};
    state.title = boot.title || "SAA-C03 Handbook";
  }

  function loadManifest() {
    manifestAt = U.nowMs();
    return Content.manifest().then(function () { drawToc(); }, function () { /* the view shows the retry line */ });
  }

  App.start = function (data) {
    if (started) return;
    started = true;
    data = data || {};
    if (data.v !== 1) data = {};

    step("state", function () {
      readBoot();
      if (SAA.Store && SAA.Store.init) SAA.Store.init(data.store);
      var s = sget("settings") || {};
      App.textSize(s.textSize);
    });

    step("events", function () {
      bus.on("manifest", function () { drawToc(); });
      bus.on("route", function () { setDrawer(false); markNav(); drawToc(); });
      bus.on("section:read", drawTocSoon);
      bus.on("store:change", drawTocSoon);
      bus.on("settings", function (s) { App.textSize(s && s.textSize); drawTocSoon(); });
      document.addEventListener("keydown", function (ev) {
        var toc = $("saa-toc");
        if (ev.key === "Escape" && toc && toc.classList.contains("is-open")) {
          setDrawer(false);
          if ($("saa-menu")) $("saa-menu").focus();
        }
      });
      var sync = $("saa-sync");
      if (sync) {
        sync.addEventListener("click", function (ev) {
          var btn = ev.target && ev.target.closest ? ev.target.closest("button") : null;
          if (btn && !ev.defaultPrevented && (btn.getAttribute("data-act") || "attach") === "attach") App.attach();
        });
      }
      document.addEventListener("visibilitychange", function () {
        if (document.hidden || !state.manifest || state.single) return;
        if (U.nowMs() - manifestAt < REFRESH_MS) return;
        manifestAt = U.nowMs();
        Content.manifest(true).then(null, function () {});
      });
    });

    try {
      Router.start({hash: data.route, view: data.view});
    } catch (e) {
      console.error("boot: router", e);
      var view = $("saa-view");
      if (view) {
        var p = document.createElement("p");
        p.className = "notice";
        p.setAttribute("role", "alert");
        p.textContent = "The page could not start. Reload to try again.";
        view.appendChild(p);
      }
    }

    step("manifest", loadManifest);
    step("capabilities", capabilities);
  };

  App.snapshot = function () {
    var cur = Router.current();
    var def = Router.view(cur.view);
    var data = null;
    try { data = def && def.snapshot ? def.snapshot() : null; } catch (e) { data = null; }
    var store = null;
    try { store = SAA.Store && SAA.Store.snapshot ? SAA.Store.snapshot() : null; } catch (e2) { store = null; }
    return JSON.parse(JSON.stringify({v: 1, route: cur.hash, view: {name: cur.view, data: data === undefined ? null : data},
                                      store: store}));
  };

  /* ---------- shot states (preview only; they need Store.reset of the practice build) ---------- */

  function shotChapter(el, part) {
    var def = Router.view("ch");
    if (SAA.Store && SAA.Store.reset) SAA.Store.reset();
    return Content.manifest().then(function (m) {
      var ch = (m.chapters || []).filter(function (c) {
        return c.status !== "planned" && (!part || (c.files || []).some(function (f) { return f.key === part; }));
      })[0];
      if (!ch || !def) return null;
      return Promise.resolve(def.mount(el, part ? [ch.slug, part] : [ch.slug], {hot: null})).then(function () { return el; });
    });
  }

  function shotProse(el) {
    return shotChapter(el, "deep").then(function (root) {
      var fonts = document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
      return fonts.then(function () { return root; }, function () { return root; });
    }).then(function (root) {
      if (!root) return null;
      var sub = root.querySelector(".sub .co");
      var target = sub ? sub.closest(".sub") : root.querySelector(".sec");
      if (target) {
        /* Headless Chrome paints a blank band when the window itself is scrolled, so the shot
           moves the view up under the sticky header instead of scrolling. */
        var top = $("saa-top");
        var want = (top ? top.getBoundingClientRect().bottom : 0) + 14;
        el.style.marginTop = Math.round(want - target.getBoundingClientRect().top) + "px";
      }
      return target || root;
    });
  }

  SAA.Test.register("chapter", function (el) { return shotChapter(el, "fast"); });
  SAA.Test.register("prose", shotProse);
  SAA.Test.register("evidence", function (el) {
    return shotProse(el).then(function (root) {
      var chip = root && root.querySelector("a.ev");
      if (chip && SAA.Evidence) SAA.Evidence.show(chip, chip.getAttribute("data-fact"));
    });
  });
  SAA.Test.register("glossary", function (el) {
    return shotProse(el).then(function (root) {
      var term = (root && root.querySelector("a.term")) || el.querySelector("a.term");
      if (term && SAA.Glossary) SAA.Glossary.show(term, term.getAttribute("data-term"));
    });
  });
  SAA.Test.register("toc", function (el) {
    return shotChapter(el, "fast").then(function () {
      drawToc();
      /* after the route event of the test view, which closes the drawer */
      setTimeout(function () { if (isPhone()) setDrawer(true); }, 40);
    });
  });

  /* ---------- go ---------- */

  if (typeof document !== "undefined") {
    var hot = globalThis.claude && globalThis.claude.hot;
    try { if (hot && hot.snapshot) hot.snapshot(function () { return SAA.App.snapshot(); }); } catch (e) { /* no viewer */ }
    if (hot && hot.ready) hot.ready(SAA.App.start); else SAA.App.start((hot && hot.data) || {});
  }

})(globalThis.SAA = globalThis.SAA || {});
