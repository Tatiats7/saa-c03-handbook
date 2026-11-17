/* reader.js (owner B). View "ch": chapter header, route switch, part tabs, the part itself,
   read tracking, the section rail, figures, and the mounts task, tasks and sources. */
(function (SAA) {
  "use strict";

  var U = SAA.U, bus = SAA.bus, Content = SAA.Content, Router = SAA.Router;
  var Reader = SAA.Reader = SAA.Reader || {};

  var RANK = {fast: 0, pass: 1, full: 2};
  var ROUTE_NAME = {fast: "Fast", pass: "Pass", full: "Full"};
  var SYN = {"do": "tasks", say: "speak", quiz: "quiz", sources: "sources"};
  var RETURN_TIERS = {deep: 1, medium: 1, light: 1};
  var READ_DELAY_MS = 8000;
  var TEXT_SIZES = ["Small", "Medium", "Large"];

  var mounts = {};
  var st = null;        /* state of the mounted chapter view */
  var live = null;      /* state of the part that mountHtml drew last: {el, slug, part, items, cur, ...} */

  /* ---------- small helpers ---------- */

  function qsa(root, sel) { return Array.prototype.slice.call(root.querySelectorAll(sel)); }
  function rank(route) { return RANK[route] === undefined ? RANK.full : RANK[route]; }
  function run(fn) { if (typeof fn === "function") { try { fn(); } catch (e) { console.error("cleanup", e); } } }

  function sget(name) {
    try { return SAA.Store ? SAA.Store.get(name) : null; } catch (e) { return null; }
  }
  function spatch(name, patch) {
    try { if (SAA.Store) SAA.Store.patch(name, patch); } catch (e) { console.error("store", e); }
  }
  function sstamp(path, done) {
    try {
      if (SAA.Store && SAA.Store.stamp) SAA.Store.stamp("progress", path, done);
    } catch (e) { console.error("store", e); }
  }
  function settings() { return sget("settings") || {}; }
  function routeOf(slug) {
    var s = settings();
    var r = (s.routeBy && s.routeBy[slug]) || s.route || "pass";
    return RANK[r] === undefined ? "pass" : r;
  }
  function readStamps(slug) {
    var p = sget("progress");
    var ch = p && p.chapters && p.chapters[slug];
    return (ch && ch.read) || {};
  }
  function skipStamps(slug) {
    var p = sget("progress");
    var ch = p && p.chapters && p.chapters[slug];
    return (ch && ch.skips) || {};
  }
  function make(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text !== undefined) n.textContent = text;
    return n;
  }
  function child(el, sel) {
    for (var n = el.firstElementChild; n; n = n.nextElementSibling) if (n.matches(sel)) return n;
    return null;
  }
  function headerBottom() {
    var top = document.getElementById("saa-top");
    return top ? Math.max(0, top.getBoundingClientRect().bottom) : 0;
  }

  /* ---------- mounts ---------- */

  Reader.registerMount = function (name, fn) { mounts[name] = fn; };

  Reader.runMount = function (name, el, id, ctx) {
    var fn = mounts[name];
    if (!el) return undefined;
    if (!fn) { el.textContent = ""; el.hidden = true; return undefined; }
    el.hidden = false;
    try {
      var cleanup = fn(el, id || "", ctx || {});
      return typeof cleanup === "function" ? cleanup : undefined;
    } catch (e) {
      console.error("mount " + name, e);
      el.textContent = "";
      el.hidden = true;
      return undefined;
    }
  };

  Reader.hasMount = function (name) { return !!mounts[name]; };

  /* ---------- route, gates, read marks ---------- */

  function isTracked(sec, slug) {
    if (sec.getAttribute("data-role") === "sheet") return false;
    var row = slug ? Content.section(slug, sec.getAttribute("data-sid")) : null;
    return !row || row.kind !== 0;
  }

  function ensureNote(sec, cls, text, act, label) {
    var note = child(sec, "." + cls);
    if (!note) {
      note = make("p", cls + " fold-n");
      note.appendChild(make("span", "fold-t", text));
      var btn = make("button", "btn quiet", label);
      btn.type = "button";
      btn.setAttribute("data-act", act);
      note.appendChild(btn);
      var head = child(sec, ".sec-h, .sub-h");
      if (head && head.nextSibling) sec.insertBefore(note, head.nextSibling);
      else sec.appendChild(note);
    } else {
      note.querySelector(".fold-t").textContent = text;
    }
    return note;
  }

  function applyRoute(el, slug, route) {
    var max = rank(route);
    var text = "Not on the " + ROUTE_NAME[route] + " route.";
    function setOff(sec, off) {
      sec.classList.toggle("is-offroute", off);
      if (off) ensureNote(sec, "offr", text, "rd-open", "Open");
    }
    qsa(el, ".sec").forEach(function (sec) {
      var subs = qsa(sec, ".sub");
      if (!isTracked(sec, slug)) { setOff(sec, false); subs.forEach(function (s) { setOff(s, false); }); return; }
      var anyOn = subs.some(function (s) { return rank(s.getAttribute("data-route")) <= max; });
      var secOff = rank(sec.getAttribute("data-route")) > max && !anyOn && !sec.__open;
      setOff(sec, secOff);
      subs.forEach(function (s) {
        setOff(s, !secOff && rank(s.getAttribute("data-route")) > max && !s.__open && !sec.__open);
      });
    });
  }

  function openStops(sub, skips) {
    return qsa(sub, ".pr-stop").filter(function (pr) {
      var d = pr.querySelector("details");
      var pid = pr.getAttribute("data-pid");
      return d && !d.open && !pr.__skip && !(skips[pid] > 0);
    });
  }

  function applyGates(el, slug, readAtMount) {
    var skips = slug ? skipStamps(slug) : {};
    qsa(el, ".sec[data-role='how']").forEach(function (sec) {
      var body = child(sec, ".sec-b");
      if (!body) return;
      var subs = qsa(body, ".sub").filter(function (s) { return s.parentNode === body; });
      subs.forEach(function (sub, i) {
        var prev = subs[i - 1], gated = false;
        if (prev && !sub.__open && !readAtMount[sub.getAttribute("data-sid")] &&
            !readAtMount[prev.getAttribute("data-sid")] &&
            !sub.classList.contains("is-offroute") && !prev.classList.contains("is-offroute") &&
            !prev.classList.contains("is-gated")) {
          gated = openStops(prev, skips).length > 0;
        }
        sub.classList.toggle("is-gated", gated);
        if (gated) ensureNote(sub, "gate-n", "Answer the question above first, or skip it.", "rd-skip", "Skip");
      });
    });
  }

  function markRead(sec) {
    sec.classList.add("is-read");
    var head = child(sec, ".sec-h, .sub-h");
    var mark = head && head.querySelector(".read-m");
    if (mark) mark.hidden = false;
  }

  function decorate(el, slug) {
    var read = slug ? readStamps(slug) : {};
    qsa(el, ".sec, .sub").forEach(function (sec) {
      var sid = sec.getAttribute("data-sid");
      var head = child(sec, ".sec-h, .sub-h");
      var body = child(sec, ".sec-b, .sub-b");
      if (head && !head.querySelector(".read-m")) {
        var mark = make("span", "read-m", "Read");
        mark.hidden = true;
        var before = head.querySelector(".sec-ask");
        if (before) head.insertBefore(mark, before); else head.appendChild(mark);
      }
      if (head && sec.classList.contains("sec") && !head.querySelector(".skim-all")) {
        var all = make("button", "btn quiet skim-all", "Show all");
        all.type = "button";
        all.setAttribute("data-act", "rd-all");
        head.appendChild(all);
      }
      if (body && isTracked(sec, slug)) {
        var sen = make("span", "sen");
        sen.setAttribute("data-sen", sid);
        sen.setAttribute("aria-hidden", "true");
        body.appendChild(sen);
      }
      if (read[sid] > 0) markRead(sec);
    });
  }

  function askButtons(el) {
    var on = !!(SAA.Ask && SAA.state && SAA.state.caps && SAA.state.caps.sample);
    qsa(el, ".sec-ask").forEach(function (b) { b.hidden = !on; });
  }

  /* ---------- read tracking ---------- */

  function track(el, slug, onRead) {
    if (!slug || typeof IntersectionObserver !== "function") return null;
    var openedAt = U.nowMs(), visible = [], done = false;
    function stamp(sen) {
      var sec = sen.closest(".sub, .sec");
      if (!sec || sec.classList.contains("is-read")) return;
      var sid = sec.getAttribute("data-sid");
      markRead(sec);
      sstamp(["chapters", slug, "read", sid], true);
      onRead(sid);
      bus.emit("section:read", {slug: slug, sid: sid});
    }
    var io = new IntersectionObserver(function (entries) {
      if (done) return;
      entries.forEach(function (e) {
        var i = visible.indexOf(e.target);
        if (e.isIntersecting) {
          if (i === -1) visible.push(e.target);
          if (U.nowMs() - openedAt >= READ_DELAY_MS) stamp(e.target);
        } else if (i !== -1) visible.splice(i, 1);
      });
    });
    qsa(el, ".sen").forEach(function (sen) { io.observe(sen); });
    var timer = setTimeout(function () {
      visible.slice().forEach(function (sen) { if (sen.offsetParent !== null) stamp(sen); });
    }, READ_DELAY_MS + 60);
    return function () { done = true; clearTimeout(timer); io.disconnect(); };
  }

  /* ---------- rail, scroll-spy, resume ---------- */

  function railItems(el) {
    return qsa(el, ".sec, .sub, .h3").map(function (n) {
      var isSec = n.classList.contains("sec"), isSub = n.classList.contains("sub");
      var head = isSec ? n.querySelector(".sec-h h2") : isSub ? n.querySelector(".sub-h h3") : n;
      var box = isSec ? child(n, ".sec-h") : isSub ? child(n, ".sub-h") : null;
      var tbox = box ? box.querySelector(".tbox") : null;
      return {el: n, sid: n.getAttribute("data-sid") || "", level: isSec ? 2 : 3, tracked: isSec || isSub,
              title: head ? head.textContent.trim() : "", min: tbox ? tbox.textContent.trim() : ""};
    }).filter(function (it) { return it.sid && it.title; });
  }

  function railHtml(items, slug, part) {
    return U.h`<p class="eyebrow rail-h">On this page</p><ol class="rail-l">${items.map(function (it) {
      var read = it.el.classList.contains("is-read");
      return U.h`<li><a class="rail-i rail-i${it.level}${read ? " is-read" : ""}" href="${Router.href("ch", slug, part, it.sid)}" data-sid="${it.sid}"><span class="rail-t">${it.title}</span>${it.min ? U.h`<span class="tbox">${it.min}</span>` : ""}<span class="rail-r vh">${read ? "Read" : ""}</span></a></li>`;
    })}</ol>`;
  }

  function drawRail() {
    var rail = document.getElementById("saa-rail");
    if (!rail || !live) return;
    if (!live.items.length || !live.slug) { rail.hidden = true; rail.textContent = ""; return; }
    U.set(rail, railHtml(live.items, live.slug, live.part));
    rail.hidden = false;
    setCur(live.cur, true);
  }

  function setCur(sid, force) {
    if (!live || (!force && live.cur === sid)) return;
    live.cur = sid;
    var rail = document.getElementById("saa-rail");
    if (!rail) return;
    qsa(rail, ".rail-i").forEach(function (a) {
      var on = a.getAttribute("data-sid") === sid;
      a.classList.toggle("is-cur", on);
      if (on) a.setAttribute("aria-current", "location"); else a.removeAttribute("aria-current");
    });
  }

  function currentPos() {
    if (!live || !live.items.length) return null;
    var line = headerBottom() + 24, hit = null;
    for (var i = 0; i < live.items.length; i++) {
      var it = live.items[i];
      if (it.el.offsetParent === null && !it.el.getClientRects().length) continue;
      var top = it.el.getBoundingClientRect().top;
      if (top <= line) hit = {sid: it.sid, off: Math.max(0, Math.round(line - top))};
      else break;
    }
    return hit || {sid: live.items[0].sid, off: 0};
  }

  function spy(el, slug, part) {
    var items = railItems(el);
    live = {el: el, slug: slug, part: part, items: items, cur: "", moved: false};
    var mine = live;
    drawRail();
    var ticking = false;
    var save = U.debounce(function () {
      if (live !== mine || !slug || !part) return;
      var pos = currentPos();
      if (!pos) return;
      var patch = {pos: {}};
      patch.pos[slug + "." + part] = pos;
      spatch("ui", patch);
    }, 500);
    function onScroll() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        ticking = false;
        if (live !== mine) return;
        var pos = currentPos();
        if (!pos) return;
        var changed = pos.sid !== mine.cur;
        setCur(pos.sid);
        if (mine.ready && slug && part) {
          save();
          if (changed) {
            var chapters = {};
            chapters[slug] = {last: part + "." + pos.sid};
            spatch("progress", {chapters: chapters,
                                last: {route: Router.href("ch", slug, part, pos.sid).slice(1), t: U.now()}});
          }
        }
      });
    }
    globalThis.addEventListener("scroll", onScroll, {passive: true});
    var pos0 = currentPos();
    if (pos0) setCur(pos0.sid);
    /* positions are saved only after the first real scroll, not while the part is being placed */
    var arm = setTimeout(function () { mine.ready = true; }, 700);
    return function () {
      clearTimeout(arm);
      save.cancel();
      globalThis.removeEventListener("scroll", onScroll);
      if (live === mine) live = null;
    };
  }

  function reveal(node) {
    for (var n = node; n && n !== document.body; n = n.parentElement) {
      if (n.tagName === "DETAILS" && !n.open) n.open = true;
      if (n.classList && (n.classList.contains("is-offroute") || n.classList.contains("is-gated"))) {
        n.__open = true;
        n.classList.remove("is-offroute", "is-gated");
      }
    }
  }

  function scrollToSid(root, sid, off) {
    if (!root || !sid) return false;
    var safe = String(sid).replace(/[^A-Za-z0-9._~-]/g, "");
    var target = root.querySelector("#sec-" + safe) || root.querySelector("[data-sid='" + safe + "']") ||
                 root.querySelector("#task-" + safe);
    if (!target) return false;
    reveal(target);
    target.scrollIntoView({block: "start"});
    if (off) globalThis.scrollBy(0, off);
    return true;
  }

  /* Mounts above the target (a task, the return questions) load after the first scroll and push the
     target down. Scroll again when the part changes height, until she touches the page or 3 s pass. */
  function keepAt(root, sid, off) {
    if (typeof ResizeObserver === "undefined") return;
    var done = false, offs = [], ro;
    function end() {
      if (done) return;
      done = true;
      try { ro.disconnect(); } catch (e) { /* gone */ }
      offs.forEach(function (fn) { try { fn(); } catch (e) { /* gone */ } });
    }
    ro = new ResizeObserver(function () {
      if (done) return;
      if (!root.isConnected) { end(); return; }
      scrollToSid(root, sid, off);
    });
    ro.observe(root);
    ["wheel", "touchstart", "keydown", "mousedown"].forEach(function (type) { offs.push(U.on(globalThis, type, null, end)); });
    setTimeout(end, 3000);
  }

  /* ---------- Reader.mountHtml ---------- */

  Reader.mountHtml = function (el, html, facts, ctx) {
    ctx = ctx || {};
    var slug = ctx.slug || "", part = ctx.part || "", route = RANK[ctx.route] === undefined ? "full" : ctx.route;
    var cleanups = [];
    if (SAA.Evidence) SAA.Evidence.register(facts);
    U.set(el, html);
    el.classList.add("prose");

    var readAtMount = {};
    var stamps = slug ? readStamps(slug) : {};
    Object.keys(stamps).forEach(function (sid) { if (stamps[sid] > 0) readAtMount[sid] = true; });

    decorate(el, slug);
    applyRoute(el, slug, route);
    applyGates(el, slug, readAtMount);
    askButtons(el);

    var state = {route: route, readAtMount: readAtMount};
    el.__reader = {
      setRoute: function (r) {
        state.route = r;
        qsa(el, ".sec, .sub").forEach(function (s) { s.__open = false; });
        applyRoute(el, slug, r);
        applyGates(el, slug, readAtMount);
      },
      regate: function () { applyGates(el, slug, readAtMount); }
    };

    cleanups.push(U.on(el, "toggle", "details", function () { applyGates(el, slug, readAtMount); }));
    var onCaps = bus.on("caps", function () { askButtons(el); });
    cleanups.push(function () { bus.off("caps", onCaps); });

    qsa(el, ".mount[data-mount]").forEach(function (m) {
      cleanups.push(Reader.runMount(m.getAttribute("data-mount"), m, m.getAttribute("data-id") || "", ctx));
    });

    if (el.querySelector(".fig use")) Content.sprite();

    cleanups.push(spy(el, slug, part));
    cleanups.push(track(el, slug, function (sid) {
      var rail = document.getElementById("saa-rail");
      var a = rail && rail.querySelector(".rail-i[data-sid='" + sid + "']");
      if (a) { a.classList.add("is-read"); var r = a.querySelector(".rail-r"); if (r) r.textContent = "Read"; }
    }));

    return function () {
      cleanups.forEach(run);
      cleanups = [];
      el.__reader = null;
    };
  };

  /* ---------- actions (the #saa click handler of router.js calls these) ---------- */

  function partHost(node) {
    for (var n = node; n; n = n.parentElement) if (n.__reader) return n;
    return null;
  }

  Router.act("rd-open", function (btn) {
    var sec = btn.closest(".sec, .sub"), host = partHost(btn);
    if (!sec) return;
    sec.__open = true;
    sec.classList.remove("is-offroute");
    qsa(sec, ".sub").forEach(function (s) { s.__open = true; s.classList.remove("is-offroute"); });
    if (host) host.__reader.regate();
    var head = sec.querySelector("h2, h3");
    if (head) { head.setAttribute("tabindex", "-1"); head.focus({preventScroll: true}); }
  });

  Router.act("rd-skip", function (btn) {
    var sub = btn.closest(".sub"), host = partHost(btn);
    if (!sub) return;
    var prev = sub.previousElementSibling;
    while (prev && !prev.classList.contains("sub")) prev = prev.previousElementSibling;
    var slug = live && live.slug;
    if (prev) {
      qsa(prev, ".pr-stop").forEach(function (pr) {
        pr.__skip = true;
        var pid = pr.getAttribute("data-pid");
        if (slug && pid) sstamp(["chapters", slug, "skips", pid], true);
      });
    }
    sub.__open = true;
    sub.classList.remove("is-gated");
    if (host) host.__reader.regate();
    var head = sub.querySelector("h3");
    if (head) { head.setAttribute("tabindex", "-1"); head.focus({preventScroll: true}); }
  });

  Router.act("rd-all", function (btn) {
    var sec = btn.closest(".sec");
    if (sec) sec.classList.add("is-full");
  });

  Router.act("rd-sections", function () {
    if (!live || !live.items.length || !SAA.Pop) return;
    var body = SAA.Pop.sheet(U.h`<nav class="rail rail-sheet" aria-label="On this page">${railHtml(live.items, live.slug, live.part)}</nav>`,
      {label: "Sections"});
    var cur = body && body.querySelector(".rail-i[data-sid='" + live.cur + "']");
    if (cur) { cur.classList.add("is-cur"); cur.setAttribute("aria-current", "location"); }
  });

  Router.act("copy", function (btn) {
    var box = btn.closest(".code");
    var code = box && box.querySelector("code");
    if (!code) return;
    U.copy(code.textContent).then(function (ok) {
      if (ok) {
        btn.textContent = "Copied";
        U.announce("Copied");
        setTimeout(function () { btn.textContent = "Copy"; }, 1600);
      } else {
        U.select(code);
        U.toast("Press copy on your keyboard.");
      }
    });
  });

  var zoomScale = 1;
  function setZoom(body, scale) {
    zoomScale = Math.min(3, Math.max(0.5, Math.round(scale * 4) / 4));
    var z = body.querySelector(".zoom"), v = body.querySelector(".zoom-v");
    if (z) z.style.setProperty("--zoom", String(zoomScale));
    if (v) v.textContent = Math.round(zoomScale * 100) + "%";
  }

  Router.act("zoom", function (btn) {
    var fig = btn.closest(".fig");
    var stage = fig && fig.querySelector(".fig-s");
    var first = stage && stage.firstElementChild;
    if (!first || !SAA.Pop) return;
    var title = fig.querySelector(".fig-t"), n = fig.querySelector(".fig-n");
    var label = ((n ? n.textContent + " " : "") + (title ? title.textContent : "")).trim() || "Figure";
    var body = SAA.Pop.sheet(U.h`<div class="zoom-bar"><button type="button" class="btn" data-act="rd-zoom-out" aria-label="Zoom out">&minus;</button><span class="zoom-v mono" aria-live="polite">100%</span><button type="button" class="btn" data-act="rd-zoom-in" aria-label="Zoom in">+</button></div><div class="zoom" role="region" tabindex="0" aria-label="${label}, zoomed. Scroll to see all of it."></div>`,
      {label: label, full: true});
    if (!body) return;
    body.querySelector(".zoom").appendChild(first.cloneNode(true));
    setZoom(body, 1);
  });
  Router.act("rd-zoom-in", function (btn) { setZoom(btn.closest(".sheet-b"), zoomScale + 0.25); });
  Router.act("rd-zoom-out", function (btn) { setZoom(btn.closest(".sheet-b"), zoomScale - 0.25); });

  Router.act("describe", function (btn) {
    var fig = btn.closest(".fig");
    if (!fig) return;
    var box = fig.querySelector(".fig-desc");
    if (!box) {
      var id = fig.getAttribute("data-fig");
      var meta = st && st.chapter && st.chapter.figures && st.chapter.figures[id];
      var alt = fig.querySelector(".fig-alt");
      var text = (meta && (meta.desc || meta.alt)) || (alt ? alt.textContent : "") || "This figure has no description yet.";
      box = make("p", "fig-desc", text);
      box.hidden = true;
      fig.appendChild(box);
    }
    box.hidden = !box.hidden;
    btn.setAttribute("aria-expanded", box.hidden ? "false" : "true");
    btn.textContent = box.hidden ? "Describe" : "Hide description";
  });

  Router.act("ask", function (btn) {
    var sec = btn.closest(".sec");
    if (sec && SAA.Ask && live) SAA.Ask.open(live.slug, sec.getAttribute("data-sid"));
  });

  /* ---------- mounts: task, tasks, sources ---------- */

  function codeBlock(text, cls) {
    return U.h`<div class="code${cls ? " " + cls : ""}" data-lang="bash"><button type="button" class="code-copy" data-act="copy">Copy</button><pre tabindex="0"><code>${text}</code></pre></div>`;
  }

  function taskHtml(t, ctx) {
    var labs = (sget("progress") || {}).labs || {};
    var mine = labs[t.id] || {};
    var done = mine.steps || {};
    var kind = t.type === "lab" ? "Lab" : t.type === "try" ? "Try" : "Look";
    var extra = ctx && ctx.route && ctx.route !== "full" && !t.pass_route && t.type !== "look";
    var steps = (t.steps || []).map(function (s, i) {
      var n = i + 1, id = "task-" + t.id + "-s" + n, ok = done[n] > 0;
      return U.h`<li class="task-step${ok ? " is-done" : ""}${s.break_it ? " is-break" : ""}">
        <div class="task-chk"><input type="checkbox" id="${id}" data-step="${n}"${ok ? U.raw(" checked") : ""}><label for="${id}"><span class="task-n mono">${n}</span> ${s.text}</label></div>
        ${s.break_it ? U.h`<p class="task-break"><span class="pill warn">Break it</span> This step fails on purpose.</p>` : ""}
        ${s.predict ? U.h`<p class="task-pred"><span class="bf-l">Predict first</span> ${s.predict}</p>` : ""}
        ${s.shown || s.command ? codeBlock(s.shown || s.command, "task-cmd") : ""}
        ${s.expect ? U.h`<p class="task-exp"><span class="bf-l">You should see</span> ${s.expect}</p>` : ""}
        ${s.explain_h ? U.h`<details class="rv rv-answer"><summary>Why</summary><div class="rv-b"><p>${U.raw(s.explain_h)}</p></div></details>` : ""}
      </li>`;
    });
    var cleanup = (t.cleanup || []).map(function (c) {
      return U.h`<li><p>${c.text}</p>${c.command ? codeBlock(c.shown || c.command, "task-cmd") : ""}</li>`;
    });
    var cleanedId = "task-" + t.id + "-cleaned";
    return U.h`<article class="task" id="task-${t.id}" data-task="${t.id}">
      <header class="task-h">
        <p class="eyebrow">${kind}${t.minutes ? U.h` · ${U.fmtMin(t.minutes)}` : ""}${extra ? U.h` · <span class="tab-x">extra</span>` : ""} · <span class="mono">${t.id}</span></p>
        <h3>${t.title}</h3>
        ${t.kills ? U.h`<p class="task-kills"><span class="bf-l">The wrong belief this removes</span> ${t.kills}</p>` : ""}
        ${t.label ? U.h`<p class="task-label">${t.label.charAt(0).toUpperCase() + t.label.slice(1)}${t.checked ? U.h`, <time>${t.checked}</time>` : ""}. Run it in AWS CloudShell.</p>` : ""}
      </header>
      ${t.cost ? U.h`<aside class="co co-cost hue-amber" data-label="Cost"><p class="co-l">Cost</p><div class="co-b"><p>${t.cost}${t.cost_if_forgotten ? U.h`. If you forget the cleanup: ${t.cost_if_forgotten}` : ""}.</p></div></aside>` : ""}
      ${t.careful ? U.h`<aside class="co co-careful hue-amber" data-label="Careful"><p class="co-l">Careful</p><div class="co-b"><p>${t.careful}</p></div></aside>` : ""}
      ${t.permissions && t.permissions.length ? U.h`<p class="task-perm"><span class="bf-l">Permissions you need</span> ${U.join(t.permissions.map(function (p) { return U.h`<code>${p}</code>`; }), ", ")}</p>` : ""}
      ${t.template ? U.h`<p class="task-tpl"><span class="bf-l">Template on your laptop</span> <code>${t.template}</code></p>` : ""}
      <ol class="task-steps">${steps}</ol>
      ${cleanup.length || t.verify ? U.h`<aside class="co co-cleanup hue-amber" data-label="Clean up"><p class="co-l">Clean up</p><div class="co-b">
        ${cleanup.length ? U.h`<ol class="task-clean">${cleanup}</ol>` : ""}
        ${t.verify ? U.h`<p><span class="bf-l">Check that nothing is left</span></p>${t.verify.command ? codeBlock(t.verify.command, "task-cmd") : ""}${t.verify.expect ? U.h`<p class="task-exp"><span class="bf-l">You should see</span> ${t.verify.expect}</p>` : ""}` : ""}
        ${t.still_costs && t.still_costs.length ? U.h`<p class="task-warn"><span class="bf-l">Still costs money if left</span> ${t.still_costs.join(" ")}</p>` : ""}
        <p class="task-chk task-done"><input type="checkbox" id="${cleanedId}" data-cleaned="1"${mine.cleaned > 0 ? U.raw(" checked") : ""}><label for="${cleanedId}">Cleaned up</label></p>
      </div></aside>` : ""}
      ${t.read_only_alternative ? U.h`<p class="task-alt"><span class="bf-l">Without an account</span> ${t.read_only_alternative}</p>` : ""}
    </article>`;
  }

  function wireTasks(el) {
    return U.on(el, "change", ".task input[type='checkbox']", function (ev, input) {
      var task = input.closest(".task");
      var id = task && task.getAttribute("data-task");
      if (!id) return;
      if (input.hasAttribute("data-cleaned")) {
        var labs = {};
        labs[id] = {cleaned: input.checked ? U.now() : 0};
        spatch("progress", {labs: labs});
      } else {
        sstamp(["labs", id, "steps", input.getAttribute("data-step")], input.checked);
        var li = input.closest(".task-step");
        if (li) li.classList.toggle("is-done", input.checked);
      }
    });
  }

  function loadData(ctx) {
    if (ctx && typeof ctx.data === "function") return Promise.resolve(ctx.data());
    if (ctx && ctx.slug) return Content.data(ctx.slug);
    return Promise.resolve(null);
  }

  function mountError(el) {
    U.set(el, U.h`<p class="notice" role="alert">This page could not be loaded. Check your connection and try again. <button type="button" class="btn" data-act="retry-load">Retry</button></p>`);
  }

  Reader.registerMount("task", function (el, id, ctx) {
    var alive = true;
    var off = wireTasks(el);
    loadData(ctx).then(function (d) {
      if (!alive) return;
      var t = d && (d.tasks || []).filter(function (x) { return x.id === id; })[0];
      if (!t) { el.hidden = true; return; }
      if (SAA.Evidence) SAA.Evidence.register(d.facts);
      U.set(el, taskHtml(t, ctx));
    }, function () { if (alive) mountError(el); });
    return function () { alive = false; off(); };
  });

  Reader.registerMount("tasks", function (el, id, ctx) {
    var alive = true;
    var off = wireTasks(el);
    loadData(ctx).then(function (d) {
      if (!alive) return;
      var list = ((d && d.tasks) || []).filter(function (t) { return t.type === "try" || t.type === "lab"; });
      if (!list.length) { U.set(el, U.h`<p class="notice">This chapter has no hands-on task yet.</p>`); return; }
      if (SAA.Evidence) SAA.Evidence.register(d.facts);
      U.set(el, U.h`<p class="lede">Run each task in AWS CloudShell. Tick a step when it is done. Your ticks are saved.</p>${list.map(function (t) { return taskHtml(t, ctx); })}`);
      if (id) scrollToSid(el, id, 0);
    }, function () { if (alive) mountError(el); });
    return function () { alive = false; off(); };
  });

  Reader.registerMount("sources", function (el, id, ctx) {
    var ch = (ctx && ctx.chapter) || {};
    var list = ch.sources || [], facts = ch.facts || {};
    if (SAA.Evidence) SAA.Evidence.register(facts);
    if (!list.length) { U.set(el, U.h`<p class="notice">This chapter lists no sources yet.</p>`); return undefined; }
    U.set(el, U.h`<p class="lede">Every fact in this chapter is a sentence of one of these AWS pages. Open a fact to read the sentence.</p>
      <ol class="srcs">${list.map(function (s) {
        var url = /^https:\/\//.test(String(s.url || "")) ? s.url : "";
        var chips = (s.facts || []).map(function (fid) {
          var f = facts[fid];
          var text = f && f.values && f.values[0] ? f.values[0] : fid;
          return U.h`<li><a class="ev" href="${Router.href("fact", fid)}" data-fact="${fid}">${text}</a></li>`;
        });
        return U.h`<li class="src"><p class="src-t">${url ? U.h`<a class="ext" href="${url}" target="_blank" rel="noopener">${s.title || url}</a>` : U.h`${s.title}`}</p>
          <p class="src-m">${s.checked ? U.h`Checked <time>${s.checked}</time> · ` : ""}${chips.length} ${chips.length === 1 ? "fact" : "facts"}</p>
          ${chips.length ? U.h`<ul class="src-f">${chips}</ul>` : ""}</li>`;
      })}</ol>`);
    return undefined;
  });

  /* ---------- the chapter view ---------- */

  function fileOf(meta, key) {
    return (meta.files || []).filter(function (f) { return f.key === key; })[0] || null;
  }

  function partExtra(slug, key, route) {
    if (route === "full" || key === "sources") return false;
    if (SYN[key]) return route === "fast";
    var rows = Content.sections(slug, key).filter(function (r) { return r.kind === 2 || r.kind === 3; });
    if (!rows.length) return false;
    return !rows.some(function (r) { return rank(r.route) <= rank(route); });
  }

  function progressText(slug, route) {
    var p = Content.progress(slug, route, sget("progress"));
    if (!p.total) return "";
    return p.read + " of " + p.total + " sections read on the " + ROUTE_NAME[route] + " route";
  }

  function headerHtml(meta, manifest, route) {
    var partRow = (manifest.parts || []).filter(function (p) { return p.id === meta.part; })[0];
    var mins = meta.minutes || {};
    var s = settings();
    var size = s.textSize === 0 || s.textSize === 2 ? s.textSize : 1;
    var routes = ["fast", "pass", "full"].map(function (r) {
      return U.h`<label class="rsw-o" for="rd-route-${r}"><input type="radio" name="rd-route" id="rd-route-${r}" value="${r}"${r === route ? U.raw(" checked") : ""}><span class="rsw-n">${ROUTE_NAME[r]}</span>${mins[r] ? U.h`<span class="rsw-m">${U.fmtMin(mins[r])}</span>` : ""}</label>`;
    });
    var sizes = TEXT_SIZES.map(function (name, i) {
      return U.h`<label class="aa-o" for="rd-ts-${i}"><input type="radio" name="rd-ts" id="rd-ts-${i}" value="${i}"${i === size ? U.raw(" checked") : ""}> ${name}</label>`;
    });
    var tabs = (meta.files || []).map(function (f) {
      return U.h`<a class="tab" href="${Router.href("ch", meta.slug, f.key)}" data-part="${f.key}">${f.title}<span class="tab-x" hidden>extra</span></a>`;
    });
    return U.h`<header class="chh">
      <p class="eyebrow chh-eye"><span>Chapter ${meta.id}</span>${partRow ? U.h`<span>${partRow.title}</span>` : ""}${meta.status === "draft" ? U.h`<span class="pill warn">Draft</span>` : ""}</p>
      <h1 tabindex="-1">${meta.title}</h1>
      <div class="chh-meta">
        ${U.bstrip(manifest.domains || [], {on: meta.domains || []})}
        <p class="chh-prog" id="rd-prog"></p>
      </div>
      ${meta.status === "draft" ? U.h`<p class="notice chh-draft">Draft: not reviewed yet. Facts are linked to AWS sources. ${meta.counts && meta.counts.q > 0 ? "The practice questions can still change." : "Practice questions appear when the chapter is ready."}</p>` : ""}
      <div class="chh-ctl">
        <fieldset class="rsw"><legend>Reading route</legend>${routes}</fieldset>
        <button type="button" class="btn quiet chh-sections" data-act="rd-sections">Sections</button>
        <details class="aa"><summary aria-label="Text size and skim mode">Aa</summary>
          <div class="aa-p">
            <fieldset class="aa-f"><legend>Text size</legend>${sizes}</fieldset>
            <label class="aa-o" for="rd-skim"><input type="checkbox" id="rd-skim"${s.skim ? U.raw(" checked") : ""}> Skim mode: key lines only</label>
          </div>
        </details>
      </div>
      <nav class="tabs" aria-label="Parts of this chapter">${tabs}</nav>
    </header>
    <div class="part" id="rd-part"></div>
    <nav class="pn" id="rd-pn" aria-label="Previous and next"></nav>`;
  }

  function refreshHeader() {
    if (!st) return;
    var route = routeOf(st.slug);
    var prog = st.el.querySelector("#rd-prog");
    if (prog) prog.textContent = progressText(st.slug, route);
    qsa(st.el, ".tab").forEach(function (a) {
      var key = a.getAttribute("data-part");
      var on = key === st.part;
      if (on) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
      var x = a.querySelector(".tab-x");
      if (x) x.hidden = !partExtra(st.slug, key, route);
    });
    var btn = st.el.querySelector(".chh-sections");
    if (btn) btn.hidden = !(live && live.items.length);
  }

  function prevNextHtml() {
    var meta = st.meta, manifest = st.manifest, route = routeOf(st.slug);
    var files = meta.files || [];
    var idx = files.map(function (f) { return f.key; }).indexOf(st.part);
    var next = null, prev = idx > 0 ? files[idx - 1] : null;
    for (var i = idx + 1; i < files.length; i++) {
      if (!partExtra(st.slug, files[i].key, route) && files[i].key !== "sources") { next = files[i]; break; }
    }
    var order = manifest.order || [], at = order.indexOf(st.slug), nextCh = null;
    for (var j = at + 1; at !== -1 && j < order.length; j++) {
      var m = Content.meta(order[j]);
      if (m && m.status !== "planned") { nextCh = m; break; }
    }
    st.nextSlug = nextCh ? nextCh.slug : null;
    var items = [];
    if (next) items.push(U.h`<a class="pn-a pn-next" href="${Router.href("ch", st.slug, next.key)}"><span class="eyebrow">Next on the ${ROUTE_NAME[route]} route</span><span class="pn-t">${next.title}</span></a>`);
    if (nextCh) items.push(U.h`<a class="pn-a${next ? "" : " pn-next"}" href="${Router.href("ch", nextCh.slug)}"><span class="eyebrow">Next chapter</span><span class="pn-t">${nextCh.id} ${nextCh.title}</span></a>`);
    if (prev) items.push(U.h`<a class="pn-a pn-prev" href="${Router.href("ch", st.slug, prev.key)}"><span class="eyebrow">Previous part</span><span class="pn-t">${prev.title}</span></a>`);
    return U.h`${items}`;
  }

  function openPart(key, sid, pos) {
    if (!st) return false;
    var scrolled = false;
    run(st.partCleanup);
    st.partCleanup = null;
    st.part = key;
    var host = st.el.querySelector("#rd-part");
    if (!host) return false;
    host.textContent = "";
    host.className = "part";
    var rail = document.getElementById("saa-rail");
    if (rail) { rail.hidden = true; rail.textContent = ""; }
    live = null;
    var route = routeOf(st.slug);
    var slug = st.slug;
    var ctx = {slug: slug, part: key, meta: st.meta, chapter: st.chapter, route: route, hot: st.hot || null,
               data: function () { return Content.data(slug); }};
    st.hot = null;
    var file = fileOf(st.meta, key);
    var md = st.chapter.parts && st.chapter.parts[key];

    if (file && SYN[key] && !(md && md.html)) {
      U.set(host, U.h`<section class="syn"><h2 class="syn-h">${file.title}</h2><div class="mount" data-mount="${SYN[key]}" data-id="${sid || ""}"></div></section>`);
      if (SAA.Evidence) SAA.Evidence.register(st.chapter.facts);
      var m = host.querySelector(".mount");
      if (!Reader.hasMount(SYN[key])) {
        U.set(m, U.h`<p class="notice">This part is not built yet.</p>`);
      } else {
        st.partCleanup = Reader.runMount(SYN[key], m, sid || "", ctx) || null;
      }
    } else if (md && md.html) {
      var pre = key === "fast" && RETURN_TIERS[st.meta.tier] ? "<div class=\"mount\" data-mount=\"return\" data-id=\"\"></div>" : "";
      st.partCleanup = Reader.mountHtml(host, U.raw(pre + md.html), st.chapter.facts, ctx);
      var first = live && live.items[0];
      if (sid) { scrolled = scrollToSid(host, sid, 0); if (scrolled) keepAt(host, sid, 0); }
      else if (pos && pos.sid && !(first && first.sid === pos.sid && (pos.off || 0) < 200)) {
        scrolled = scrollToSid(host, pos.sid, pos.off || 0);
        if (scrolled) keepAt(host, pos.sid, pos.off || 0);
      }
    } else {
      U.set(host, U.h`<p class="notice">This part does not exist. <a href="${Router.href("ch", slug)}">Open the chapter</a></p>`);
    }

    var pn = st.el.querySelector("#rd-pn");
    if (pn) U.set(pn, prevNextHtml());
    refreshHeader();
    if (st.nextSlug) Content.prefetch(st.nextSlug);
    return scrolled;
  }

  function defaultPart(meta, slug) {
    var files = meta.files || [];
    var p = sget("progress");
    var last = p && p.chapters && p.chapters[slug] && p.chapters[slug].last;
    var key = last ? String(last).split(".")[0] : "";
    if (key && fileOf(meta, key)) return key;
    return files.length ? files[0].key : "";
  }

  function savedPos(slug, part) {
    var ui = sget("ui");
    return (ui && ui.pos && ui.pos[slug + "." + part]) || null;
  }

  function simplePage(el, eyebrow, title, text) {
    U.set(el, U.h`<article class="page"><p class="eyebrow">${eyebrow}</p><h1 tabindex="-1">${title}</h1><p>${text}</p><p><a href="#toc">Open the contents</a></p></article>`);
  }

  function applySkim(el) {
    el.classList.toggle("is-skim", !!settings().skim);
  }

  var view = {
    title: function (args) {
      var meta = Content.meta(args[0]);
      return meta ? meta.title : "Chapter";
    },

    mount: function (el, args, ctx) {
      var slug = args[0] || "";
      var hot = ctx && ctx.hot && ctx.hot.slug === slug ? ctx.hot : null;
      return Content.manifest().then(function (manifest) {
        var meta = Content.meta(slug);
        if (!meta) { simplePage(el, "Chapter", "This page does not exist", "No chapter has this address."); return null; }
        if (meta.status === "planned") {
          simplePage(el, "Chapter " + meta.id, meta.title, "This chapter is not written yet.");
          return null;
        }
        return Content.chapter(slug).then(function (chapter) {
          if (!chapter) { simplePage(el, "Chapter " + meta.id, meta.title, "This chapter is not written yet."); return; }
          st = {el: el, slug: slug, meta: meta, manifest: manifest, chapter: chapter, part: "", partCleanup: null,
                off: [], hot: hot, nextSlug: null};
          U.set(el, headerHtml(meta, manifest, routeOf(slug)));
          applySkim(el);

          st.off.push(U.on(el, "change", "input[name='rd-route']", function (ev, input) {
            var by = {};
            by[slug] = input.value;
            spatch("settings", {routeBy: by});
            var host = el.querySelector("#rd-part");
            if (host && host.__reader) host.__reader.setRoute(input.value);
            else openPart(st.part, null, null);
            var pn = el.querySelector("#rd-pn");
            if (pn) U.set(pn, prevNextHtml());
            refreshHeader();
            U.announce(ROUTE_NAME[input.value] + " route. " + progressText(slug, input.value));
          }));
          st.off.push(U.on(el, "change", "input[name='rd-ts']", function (ev, input) {
            var n = Number(input.value);
            spatch("settings", {textSize: n});
            if (SAA.App && SAA.App.textSize) SAA.App.textSize(n);
          }));
          st.off.push(U.on(el, "change", "#rd-skim", function (ev, input) {
            spatch("settings", {skim: input.checked ? 1 : 0});
            el.classList.toggle("is-skim", input.checked);
            if (!input.checked) qsa(el, ".sec.is-full").forEach(function (s) { s.classList.remove("is-full"); });
          }));
          var onRead = bus.on("section:read", function (d) { if (st && d.slug === st.slug) refreshHeader(); });
          var onDrop = bus.on("content:drop", function (d) {
            if (!st || !d || (d.slugs || []).indexOf(st.slug) === -1) return;
            var pos = currentPos();
            Content.chapter(st.slug).then(function (fresh) {
              if (!st || !fresh) return;
              st.chapter = fresh;
              st.meta = Content.meta(st.slug) || st.meta;
              openPart(st.part, null, pos);
            }, function () {});
          });
          st.off.push(function () { bus.off("section:read", onRead); bus.off("content:drop", onDrop); });

          var part = args[1] || (hot && hot.part) || defaultPart(meta, slug);
          var pos = args[2] ? null : (hot && hot.part === part ? hot : savedPos(slug, part));
          openPart(part, args[2] || "", pos);
        });
      });
    },

    update: function (args) {
      if (!st || args[0] !== st.slug) return false;
      var part = args[1] || st.part;
      if (part !== st.part) {
        var saved = args[2] ? null : savedPos(st.slug, part);
        if (!openPart(part, args[2] || "", saved)) {
          var tabs = st.el.querySelector(".tabs");
          if (tabs && tabs.getBoundingClientRect().top < headerBottom()) tabs.scrollIntoView({block: "start"});
        }
        return true;
      }
      var host = st.el.querySelector("#rd-part");
      if (args[2] && host) {
        if (!scrollToSid(host, args[2], 0)) return true;
        var target = host.querySelector("#sec-" + args[2].replace(/[^A-Za-z0-9._~-]/g, ""));
        var head = target && (target.matches("h3") ? target : target.querySelector("h2, h3"));
        if (head) { head.setAttribute("tabindex", "-1"); head.focus({preventScroll: true}); }
      }
      return true;
    },

    unmount: function () {
      if (!st) return;
      run(st.partCleanup);
      st.off.forEach(run);
      st = null;
      live = null;
      var rail = document.getElementById("saa-rail");
      if (rail) { rail.hidden = true; rail.textContent = ""; }
    },

    snapshot: function () {
      if (!st) return null;
      var pos = currentPos();
      return {slug: st.slug, part: st.part, sid: pos ? pos.sid : "", off: pos ? pos.off : 0};
    }
  };

  Router.register("ch", view);

})(globalThis.SAA = globalThis.SAA || {});
