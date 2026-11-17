/* popover.js (owner B). One popover (anchored on desktop, bottom sheet on a phone) and one sheet. */
(function (SAA) {
  "use strict";

  var U = SAA.U;
  var Pop = SAA.Pop = SAA.Pop || {};

  var pop = null;      /* {anchor, offKey, offClick, offResize} */
  var sheet = null;    /* {opener, onClose, offKey} */
  var FOCUSABLE = "a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), " +
                  "textarea:not([disabled]), summary, [tabindex]:not([tabindex='-1'])";

  function $(id) { return document.getElementById(id); }

  function isPhone() {
    try { return globalThis.matchMedia("(max-width: 759px)").matches; } catch (e) { return false; }
  }

  function refocus(el) {
    if (el && el.isConnected && el.focus) {
      try { el.focus({preventScroll: true}); } catch (e) { /* older engines */ }
    }
  }

  /* ---------- popover ---------- */

  function place() {
    var el = $("saa-pop"), app = $("saa");
    if (!pop || !el || !app) return;
    if (isPhone() || !pop.anchor || !pop.anchor.isConnected) {
      el.style.left = ""; el.style.top = ""; el.style.width = "";
      return;
    }
    var a = pop.anchor.getBoundingClientRect();
    var rects = pop.anchor.getClientRects();
    if (rects && rects.length > 1) a = rects[rects.length - 1];   /* a chip that wraps: use its last line */
    var box = app.getBoundingClientRect();
    var w = el.offsetWidth, h = el.offsetHeight;
    var viewW = document.documentElement.clientWidth, viewH = document.documentElement.clientHeight;
    var left = Math.min(Math.max(a.left, 12), Math.max(12, viewW - w - 12));
    var below = a.bottom + 8, above = a.top - 8 - h;
    var top = (below + h > viewH - 8 && above > 60) ? above : below;
    el.style.left = Math.round(left - box.left) + "px";
    el.style.top = Math.round(top - box.top) + "px";
  }

  Pop.open = function (anchorEl, html, opts) {
    opts = opts || {};
    var layer = $("saa-pop-layer"), el = $("saa-pop");
    if (!layer || !el) return;
    if (pop && pop.anchor === anchorEl && anchorEl) { Pop.close(); return; }
    Pop.close(true);
    var label = opts.label || "Details";
    el.setAttribute("aria-label", label);
    el.classList.toggle("wide", !!opts.wide);
    U.set(el, U.h`<div class="pop-h"><span class="eyebrow">${label}</span><button type="button" class="pop-x" data-act="pop-close">Close</button></div><div class="pop-b">${html}</div>`);
    layer.hidden = false;
    pop = {anchor: anchorEl || null};
    if (anchorEl) anchorEl.setAttribute("aria-expanded", "true");
    place();
    pop.offKey = function (ev) { if (ev.key === "Escape") { ev.stopPropagation(); Pop.close(); } };
    pop.offClick = function (ev) {
      var t = ev.target;
      if (!pop) return;
      if (t && t.closest && t.closest("[data-act='pop-close']")) { ev.preventDefault(); Pop.close(); return; }
      if (el.contains(t)) return;
      if (pop.anchor && pop.anchor.contains(t)) return;
      Pop.close(true);
    };
    pop.offResize = U.debounce(place, 60);
    document.addEventListener("keydown", pop.offKey, true);
    document.addEventListener("click", pop.offClick, true);
    globalThis.addEventListener("resize", pop.offResize);
    try { el.focus({preventScroll: true}); } catch (e) { /* older engines */ }
    return el;
  };

  /* quiet: do not move the focus back (another control is taking it). */
  Pop.close = function (quiet) {
    var layer = $("saa-pop-layer"), el = $("saa-pop");
    if (!pop) return;
    var old = pop;
    pop = null;
    document.removeEventListener("keydown", old.offKey, true);
    document.removeEventListener("click", old.offClick, true);
    globalThis.removeEventListener("resize", old.offResize);
    if (old.anchor) old.anchor.removeAttribute("aria-expanded");
    var hadFocus = el && el.contains(document.activeElement);
    if (layer) layer.hidden = true;
    if (el) { el.textContent = ""; el.style.left = ""; el.style.top = ""; }
    if (hadFocus && quiet !== true) refocus(old.anchor);
  };

  Pop.isOpen = function () { return !!pop; };

  /* ---------- sheet ---------- */

  function trap(ev) {
    var el = $("saa-sheet");
    if (!sheet || !el) return;
    if (ev.key === "Escape") { ev.stopPropagation(); Pop.closeSheet(); return; }
    if (ev.key !== "Tab") return;
    var list = Array.prototype.filter.call(el.querySelectorAll(FOCUSABLE), function (n) {
      return n.offsetParent !== null || n === document.activeElement;
    });
    if (!list.length) { ev.preventDefault(); return; }
    var first = list[0], last = list[list.length - 1], active = document.activeElement;
    if (ev.shiftKey && (active === first || !el.contains(active))) { ev.preventDefault(); last.focus(); }
    else if (!ev.shiftKey && (active === last || !el.contains(active))) { ev.preventDefault(); first.focus(); }
  }

  function sheetClick(ev) {
    var el = $("saa-sheet"), t = ev.target;
    if (!sheet || !el) return;
    if (t === el || (t && t.closest && t.closest("[data-act='sheet-close']"))) {
      ev.preventDefault();
      Pop.closeSheet();
    }
  }

  Pop.sheet = function (html, opts) {
    opts = opts || {};
    var el = $("saa-sheet");
    if (!el) return null;
    var opener = sheet ? sheet.opener : document.activeElement;
    if (sheet) Pop.closeSheet(true);
    Pop.close(true);
    var label = opts.label || "Details";
    el.classList.toggle("full", !!opts.full);
    el.setAttribute("aria-label", label);
    U.set(el, U.h`<div class="sheet-p"><div class="sheet-h"><h2 class="sheet-t">${label}</h2><button type="button" class="btn quiet sheet-x" data-act="sheet-close">Close</button></div><div class="sheet-b">${html || ""}</div></div>`);
    el.hidden = false;
    sheet = {opener: opener, onClose: opts.onClose || null};
    document.addEventListener("keydown", trap, true);
    el.addEventListener("click", sheetClick);
    var root = $("saa");
    if (root) root.classList.add("has-sheet");
    try { el.focus({preventScroll: true}); } catch (e) { /* older engines */ }
    return el.querySelector(".sheet-b");
  };

  Pop.closeSheet = function (keepFocus) {
    var el = $("saa-sheet");
    if (!sheet) return;
    var old = sheet;
    sheet = null;
    document.removeEventListener("keydown", trap, true);
    if (el) {
      el.removeEventListener("click", sheetClick);
      el.hidden = true;
      el.textContent = "";
      el.classList.remove("full");
    }
    var root = $("saa");
    if (root) root.classList.remove("has-sheet");
    if (old.onClose) { try { old.onClose(); } catch (e) { console.error("sheet onClose", e); } }
    if (keepFocus !== true) refocus(old.opener);
  };

  Pop.sheetOpen = function () { return !!sheet; };

})(globalThis.SAA = globalThis.SAA || {});
