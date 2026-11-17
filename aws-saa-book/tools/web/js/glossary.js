/* glossary.js (owner B). Glossary popover and the view #glossary. */
(function (SAA) {
  "use strict";

  var U = SAA.U;
  var Glossary = SAA.Glossary = SAA.Glossary || {};

  var byName = null;   /* lower-case term or short name -> id */

  function names(terms) {
    if (byName) return byName;
    byName = {};
    Object.keys(terms).forEach(function (id) {
      var t = terms[id];
      byName[id] = id;
      if (t.term) byName[String(t.term).toLowerCase()] = id;
      if (t.short) byName[String(t.short).toLowerCase()] = id;
    });
    return byName;
  }

  function other(terms, name) {
    var id = names(terms)[String(name).toLowerCase()];
    return id
      ? U.h`<a class="term" href="#glossary.${id}" data-term="${id}">${terms[id].term}</a>`
      : U.h`${name}`;
  }

  function card(terms, id, opts) {
    var t = terms[id];
    opts = opts || {};
    if (!t) return U.h`<div class="glc"><p class="notice">This word is not in the glossary.</p></div>`;
    var facts = (t.facts || []).map(function (fid) {
      return U.h`<a class="ev" href="${SAA.Router.href("fact", fid)}" data-fact="${fid}">${fid}</a>`;
    });
    return U.h`<div class="glc" data-term-id="${id}">
      <p class="glc-t">${t.term}${t.short && t.short !== t.term ? U.h` <span class="glc-short">(${t.short})</span>` : ""}</p>
      ${t.say ? U.h`<p class="glc-say"><span class="bf-l">Say</span> <span class="mono">${t.say}</span></p>` : ""}
      <p class="glc-m">${t.meaning}</p>
      ${t.with && t.with.length ? U.h`<div class="glc-with"><p class="bf-l">Words that go with it</p><ul>${t.with.map(function (w) { return U.h`<li>${w}</li>`; })}</ul></div>` : ""}
      ${t.not && t.not.length ? U.h`<p class="glc-not"><span class="bf-l">Do not confuse with</span> ${U.join(t.not.map(function (n) { return other(terms, n); }), ", ")}</p>` : ""}
      ${opts.page && facts.length ? U.h`<p class="glc-facts"><span class="bf-l">Facts</span> ${U.join(facts, ", ")}</p>` : ""}
      ${opts.page ? "" : U.h`<p class="glc-foot"><a href="#glossary.${id}">Open the glossary</a></p>`}
    </div>`;
  }

  function stamp(id) {
    try {
      if (SAA.Store && SAA.Store.stamp) SAA.Store.stamp("progress", ["terms", id], true);
    } catch (e) { /* progress is optional */ }
  }

  Glossary.show = function (anchorEl, id) {
    if (!id || !SAA.Content) return;
    SAA.Content.glossary().then(function (file) {
      var terms = (file && file.terms) || {};
      if (!terms[id]) { SAA.Router.go("#glossary." + id); return; }
      SAA.Pop.open(anchorEl, card(terms, id), {label: "Glossary"});
      stamp(id);
    }, function () { U.toast("The glossary could not be loaded. Check your connection."); });
  };

  /* ---------- view ---------- */

  var view = {el: null, off: [], terms: null};

  function sorted(terms) {
    return Object.keys(terms).sort(function (a, b) {
      return String(terms[a].term).toLowerCase() < String(terms[b].term).toLowerCase() ? -1 : 1;
    });
  }

  function focusTerm(id) {
    if (!view.el || !id) return;
    var row = view.el.querySelector("[data-term-id='" + id.replace(/[^a-z0-9-]/g, "") + "']");
    Array.prototype.forEach.call(view.el.querySelectorAll(".glc.is-cur"), function (n) { n.classList.remove("is-cur"); });
    if (!row) return;
    row.classList.add("is-cur");
    row.scrollIntoView({block: "start"});
    stamp(id);
  }

  function applyFilter(text) {
    var q = U.norm(text), shown = 0;
    Array.prototype.forEach.call(view.el.querySelectorAll(".gl-list > li"), function (li) {
      var hit = !q || U.norm(li.textContent).indexOf(q) !== -1;
      li.hidden = !hit;
      if (hit) shown++;
    });
    var none = view.el.querySelector(".gl-none");
    if (none) none.hidden = shown !== 0;
  }

  if (SAA.Router) {
    SAA.Router.register("glossary", {
      title: function () { return "Glossary"; },
      mount: function (el, args) {
        view.el = el;
        return SAA.Content.glossary().then(function (file) {
          var terms = view.terms = (file && file.terms) || {};
          byName = null;
          var list = sorted(terms);
          U.set(el, U.h`<article class="page gl">
            <p class="eyebrow">Reference</p>
            <h1 tabindex="-1">Glossary</h1>
            <p class="lede">${list.length} words of the exam and of this book, in plain English. One word for one thing.</p>
            <form class="gl-form" role="search">
              <label for="gl-filter">Filter the words</label>
              <input type="search" id="gl-filter" autocomplete="off" spellcheck="false">
            </form>
            <p class="gl-none notice" hidden>No word matches. Clear the filter to see every word.</p>
            <ul class="gl-list">${list.map(function (id) { return U.h`<li>${card(terms, id, {page: true})}</li>`; })}</ul>
          </article>`);
          view.off.push(U.on(el, "input", "#gl-filter", function (ev, input) { applyFilter(input.value); }));
          view.off.push(U.on(el, "submit", ".gl-form", function (ev) { ev.preventDefault(); }));
          if (args[0]) setTimeout(function () { focusTerm(args[0]); }, 0);
        });
      },
      update: function (args) {
        if (!view.el || !view.terms) return false;
        if (args[0]) focusTerm(args[0]);
        return true;
      },
      unmount: function () {
        view.off.forEach(function (off) { off(); });
        view = {el: null, off: [], terms: null};
      }
    });
  }

  /* A term link inside the glossary page moves inside the page: no popover there. */
  Glossary.card = function (terms, id) { return card(terms, id); };

})(globalThis.SAA = globalThis.SAA || {});
