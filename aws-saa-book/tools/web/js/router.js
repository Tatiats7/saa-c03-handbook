/* router.js (owner B). Hash routes, view mounting and the one click handler on #saa. */
(function (SAA) {
  "use strict";

  var U = SAA.U, bus = SAA.bus;
  var Router = SAA.Router = SAA.Router || {};

  var views = {};
  var acts = {};                 /* B's data-act controls: name -> fn(el, event) */
  var cur = {view: "", args: [], hash: ""};
  var mounted = null;            /* {name, def, args} */
  var pendingHot = null;         /* {name, data} from a republish, used once */
  var seq = 0;
  var started = false;
  var RESTORE_SEC = 43200;

  /* Views of the contract. A known view that no module registered shows "not built yet". */
  var KNOWN = ["home", "ch", "quiz", "drill", "retry", "mix", "mock", "attempt", "mistakes", "cards", "speak",
               "glossary", "fact", "plan", "progress", "files", "about", "t"];

  Router.register = function (view, def) { views[view] = def; };

  /* The registered definition of a view, or null (used by shot states and tests). */
  Router.view = function (name) { return views[name] || null; };

  /* B's modules add their data-act handlers here (copy, zoom, describe, toc, search, ask). */
  Router.act = function (name, fn) { acts[name] = fn; };

  Router.parse = function (hash) {
    var s = String(hash === null || hash === undefined ? "" : hash);
    if (s.charAt(0) === "#") s = s.slice(1);
    s = s.replace(/[^A-Za-z0-9._~-]/g, "");
    var tokens = s.split(".").filter(function (t) { return t !== ""; });
    if (!tokens.length) return {view: "home", args: []};
    return {view: tokens[0], args: tokens.slice(1)};
  };

  Router.href = function (view) {
    var tokens = [view || "home"];
    for (var i = 1; i < arguments.length; i++) {
      var a = arguments[i];
      if (a !== null && a !== undefined && a !== "") tokens.push(String(a));
    }
    return "#" + tokens.join(".");
  };

  function toHash(route) {
    return Router.href.apply(null, [route.view].concat(route.args || []));
  }

  Router.current = function () {
    return {view: cur.view, args: cur.args.slice(), hash: cur.hash};
  };

  function store() { return SAA.Store || null; }

  function viewEl() { return document.getElementById("saa-view"); }

  function notice(title, text, link) {
    return U.h`<div class="notice-page"><h1 tabindex="-1">${title}</h1><p>${text}</p>${link || ""}</div>`;
  }

  /* The retry line that every view shows when a file could not be loaded. */
  Router.loadError = function (el) {
    U.set(el, U.h`<div class="notice-page"><h1 tabindex="-1">This page could not be loaded</h1>
      <p class="notice" role="alert">This page could not be loaded. Check your connection and try again.
      <button type="button" class="btn" data-act="retry-load">Retry</button></p></div>`);
  };

  function focusTitle(el, title) {
    var h1 = el.querySelector("h1");
    if (h1) {
      if (!h1.hasAttribute("tabindex")) h1.setAttribute("tabindex", "-1");
      try { h1.focus({preventScroll: true}); } catch (e) { /* older engines */ }
    }
    if (title) U.announce(title);
  }

  function unmount() {
    if (mounted && mounted.def && mounted.def.unmount) {
      try { mounted.def.unmount(); } catch (e) { console.error("unmount", e); }
    }
    mounted = null;
  }

  function show(route, opts) {
    opts = opts || {};
    var el = viewEl();
    if (!el) return Promise.resolve();
    var hash = toHash(route);
    var def = views[route.view];
    if (SAA.Pop) { try { SAA.Pop.close(true); SAA.Pop.closeSheet(true); } catch (e) { /* nothing open */ } }

    /* the same view can move inside itself (the reader scrolls to a section) */
    if (mounted && def && mounted.def === def && def.update) {
      var handled = false;
      try { handled = def.update(route.args, {hot: null}); } catch (e) { handled = false; }
      if (handled) {
        cur = {view: route.view, args: route.args.slice(), hash: hash};
        mounted.args = cur.args;
        after(route, def, el, false);
        return Promise.resolve();
      }
    }

    var my = ++seq;
    unmount();
    cur ={view: route.view, args: route.args.slice(), hash: hash};
    if (SAA.state) SAA.state.route = Router.current();
    var rail = document.getElementById("saa-rail");
    if (rail) { rail.hidden = true; rail.textContent = ""; }
    el.textContent = "";
    el.setAttribute("data-view", route.view);
    if (!opts.keepScroll) { try { globalThis.scrollTo(0, 0); } catch (e) { /* no window */ } }

    if (!def) return unknown(route, el, my);

    var hot = null;
    if (pendingHot && pendingHot.name === route.view) { hot = pendingHot.data || null; pendingHot = null; }
    mounted = {name: route.view, def: def, args: cur.args};
    var result;
    try { result = def.mount(el, route.args.slice(), {hot: hot}); }
    catch (e) { result = Promise.reject(e); }
    return Promise.resolve(result).then(function () {
      if (my !== seq) return;
      after(route, def, el, true);
    }, function (err) {
      if (my !== seq) return;
      if (!(err && err.path)) console.error("view " + route.view, err);
      Router.loadError(el);
      after(route, def, el, true);
    });
  }

  function after(route, def, el, focus) {
    var title = "";
    try { title = def && def.title ? def.title(route.args.slice()) : ""; } catch (e) { title = ""; }
    if (focus) focusTitle(el, title);
    var St = store();
    if (St && route.view !== "t") {
      try { St.patch("ui", {route: cur.hash.slice(1), t: U.now()}); } catch (e) { /* storage is optional */ }
    }
    bus.emit("route", Router.current());
  }

  function unknown(route, el, my) {
    if (KNOWN.indexOf(route.view) !== -1) {
      U.set(el, notice("Not built yet", "This part is not built yet.",
        U.h`<p><a href="#home">Go to Today</a></p>`));
      focusTitle(el, "Not built yet");
      bus.emit("route", Router.current());
      return Promise.resolve();
    }
    function missing() {
      if (my !== seq) return;
      U.set(el, notice("This page does not exist", "The link may be old, or the page has moved.",
        U.h`<p><a href="#home">Go to Today</a></p>`));
      focusTitle(el, "This page does not exist");
      bus.emit("route", Router.current());
    }
    if (!SAA.Content) { missing(); return Promise.resolve(); }
    return SAA.Content.manifest().then(function (m) {
      if (my !== seq) return;
      var target = m && m.aliases && route.args.length === 0 ? m.aliases[route.view] : null;
      if (target) { Router.go("#" + target, {replace: true}); return; }
      missing();
    }, missing);
  }

  function writeHash(hash, replace) {
    try {
      if (globalThis.location.hash === hash || (hash === "#home" && !globalThis.location.hash)) return;
      if (replace && globalThis.history && history.replaceState) history.replaceState(null, "", hash);
      else globalThis.location.hash = hash;
    } catch (e) { /* the host may ignore hash writes; navigation already happened */ }
  }

  function openToc() {
    if (acts.toc) acts.toc(document.getElementById("saa-menu"), null, true);
  }

  Router.go = function (hashOrRoute, opts) {
    opts = opts || {};
    var route = typeof hashOrRoute === "string" ? Router.parse(hashOrRoute)
      : {view: hashOrRoute.view, args: (hashOrRoute.args || []).slice()};
    if (route.view === "toc") {
      var first = mounted ? Promise.resolve() : show({view: "home", args: []}, opts);
      return first.then(openToc);
    }
    var hash = toHash(route);
    if (mounted && hash === cur.hash && !opts.force) return Promise.resolve();
    var p = show(route, opts);
    writeHash(hash, opts.replace);
    return p;
  };

  /* Mounts the current route again (after a file changed, or for Retry). */
  Router.reload = function () {
    var route = {view: cur.view, args: cur.args.slice()};
    unmount();
    return show(route, {keepScroll: true});
  };

  function onHashChange() {
    var route = Router.parse(globalThis.location.hash);
    if (route.view === "toc") { openToc(); return; }
    if (mounted && toHash(route) === cur.hash) return;
    show(route, {});
  }

  function onClick(ev) {
    if (ev.defaultPrevented) return;
    var t = ev.target;
    if (t && t.nodeType !== 1) t = t.parentElement;
    if (!t || !t.closest) return;
    var plain = !(ev.button || ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey);

    var ev1 = t.closest("a.ev");
    if (ev1 && plain) {
      if (SAA.Evidence) {
        ev.preventDefault();
        SAA.Evidence.show(ev1, ev1.getAttribute("data-fact") || Router.parse(ev1.getAttribute("href")).args[0]);
      }
      return;
    }
    var term = t.closest("a.term");
    if (term && plain) {
      if (SAA.Glossary) {
        ev.preventDefault();
        SAA.Glossary.show(term, term.getAttribute("data-term") || Router.parse(term.getAttribute("href")).args[0]);
      }
      return;
    }
    var ctl = t.closest("[data-act]");
    if (ctl) {
      var name = ctl.getAttribute("data-act");
      if (name === "retry-load") { ev.preventDefault(); Router.reload(); return; }
      if (acts[name]) { ev.preventDefault(); acts[name](ctl, ev); return; }
    }
    var a = t.closest("a[href^='#']");
    if (a && plain) {
      ev.preventDefault();
      var href = a.getAttribute("href");
      if (href === "#saa-main") {
        var main = document.getElementById("saa-main");
        if (main) main.focus();
        return;
      }
      Router.go(href);
    }
  }

  Router.start = function (opts) {
    opts = opts || {};
    if (!started) {
      started = true;
      var root = document.getElementById("saa");
      if (root) root.addEventListener("click", onClick);
      globalThis.addEventListener("hashchange", onHashChange);
    }
    pendingHot = opts.view && opts.view.name ? {name: opts.view.name, data: opts.view.data || null} : null;
    var hash = opts.hash;
    if (hash === undefined || hash === null || hash === "") {
      try { hash = globalThis.location.hash; } catch (e) { hash = ""; }
    }
    var route = Router.parse(hash);
    var bare = String(hash || "").replace(/^#/, "") === "";
    if (bare) {
      var St = store(), ui = null;
      try { ui = St ? St.get("ui") : null; } catch (e) { ui = null; }
      if (ui && ui.route && ui.t && U.now() - ui.t < RESTORE_SEC) route = Router.parse(ui.route);
    }
    if (route.view === "toc") route = {view: "home", args: []};
    var p = show(route, {keepScroll: true});
    if (!bare) writeHash(toHash(route), true);
    return p;
  };

})(globalThis.SAA = globalThis.SAA || {});
