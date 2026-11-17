/* evidence.js (owner B). The evidence card of a fact: popover from a chip, and the page #fact.<id>. */
(function (SAA) {
  "use strict";

  var U = SAA.U;
  var Evidence = SAA.Evidence = SAA.Evidence || {};

  var known = {};                       /* id -> fact card */
  var ids = typeof WeakMap === "function" ? new WeakMap() : null;

  Evidence.register = function (factsMap) {
    if (!factsMap) return;
    Object.keys(factsMap).forEach(function (id) {
      var f = factsMap[id];
      if (!f || typeof f !== "object") return;
      known[id] = f;
      if (ids) ids.set(f, id);
    });
  };

  Evidence.get = function (id) { return known[id] || null; };

  function host(url) {
    var m = /^https:\/\/([^/]+)/.exec(String(url || ""));
    return m ? m[1] : "";
  }

  function safeUrl(url) {
    return /^https:\/\//.test(String(url || "")) ? String(url) : "";
  }

  /* Evidence.card(fact) or Evidence.card(fact, id). */
  Evidence.card = function (fact, id) {
    if (!fact) return U.h`<div class="evc"><p class="notice">This fact is not in the book.</p></div>`;
    id = id || fact.id || (ids && ids.get(fact)) || "";
    var quotes = (fact.quotes || []).map(function (q) {
      var url = safeUrl(q.url);
      var src = url
        ? U.h`<a class="ext" href="${url}" target="_blank" rel="noopener">${q.title || host(url)}</a>`
        : U.h`${q.title || "AWS"}`;
      return U.h`<figure class="evc-q"><blockquote>${q.q}</blockquote><figcaption class="evc-src">${src}${q.header ? U.h`, section ${q.header}` : ""}${url ? U.h` <span class="evc-host">${host(url)}</span>` : ""}</figcaption></figure>`;
    });
    var changed = fact.changed && fact.changed.date
      ? U.h`<p class="evc-chg"><span class="pill warn">Changed</span> <time>${fact.changed.date}</time>${fact.changed.was ? U.h`. Before: ${fact.changed.was}` : ""}</p>`
      : "";
    return U.h`<div class="evc" data-fact-id="${id}">
      <p class="evc-id mono">${id}${fact.kind ? U.h` <span class="evc-kind">${fact.kind}</span>` : ""}</p>
      <p class="evc-claim">${fact.claim}</p>
      ${fact.scope ? U.h`<p class="evc-scope"><span class="bf-l">Scope</span> ${fact.scope}</p>` : ""}
      ${quotes}
      ${changed}
      <p class="evc-foot"><span class="evc-date">${fact.checked ? U.h`Checked <time>${fact.checked}</time>` : "Not dated"}</span>
      <button type="button" class="linkbtn" data-act="ev-report">Report a problem</button></p>
      <form class="evc-form" hidden>
        <label for="evc-note">What is wrong with this fact?</label>
        <textarea id="evc-note" rows="3" maxlength="500"></textarea>
        <button type="submit" class="btn">Send</button>
      </form>
    </div>`;
  };

  function wire(root) {
    if (!root || root.__evWired) return;
    root.__evWired = true;
    U.on(root, "click", "[data-act='ev-report']", function (ev, btn) {
      var form = btn.closest(".evc").querySelector(".evc-form");
      if (!form) return;
      form.hidden = !form.hidden;
      if (!form.hidden) form.querySelector("textarea").focus();
    });
    U.on(root, "submit", ".evc-form", function (ev, form) {
      ev.preventDefault();
      var card = form.closest(".evc");
      var note = form.querySelector("textarea").value.trim().slice(0, 500);
      if (!note) return;
      if (SAA.Store && SAA.Store.flag) SAA.Store.flag("fact", card.getAttribute("data-fact-id"), note);
      else U.toast("Reports cannot be saved right now.");
      form.hidden = true;
      form.querySelector("textarea").value = "";
    });
  }

  /* A fact that no open file registered: Content.fact loads the shard of its service once (f/<service>.json). */
  function lookup(id) {
    if (known[id]) return Promise.resolve(known[id]);
    if (!SAA.Content || !SAA.Content.fact) return Promise.resolve(null);
    return SAA.Content.fact(id).then(function (f) {
      if (f) { var one = {}; one[id] = f; Evidence.register(one); }
      return f || null;
    });
  }

  Evidence.show = function (anchorEl, id) {
    if (!id) return;
    wire(document.getElementById("saa-pop"));
    if (known[id]) {
      SAA.Pop.open(anchorEl, Evidence.card(known[id], id), {label: "Source", wide: true});
      return;
    }
    lookup(id).then(function (f) {
      if (f) SAA.Pop.open(anchorEl, Evidence.card(f, id), {label: "Source", wide: true});
      else SAA.Router.go({view: "fact", args: [id]});
    }, function () { SAA.Router.go({view: "fact", args: [id]}); });
  };

  if (SAA.Router) {
    SAA.Router.register("fact", {
      title: function (args) { return "Fact " + (args[0] || ""); },
      mount: function (el, args) {
        var id = args[0] || "";
        wire(el);
        return lookup(id).then(function (f) {
          U.set(el, U.h`<article class="page"><p class="eyebrow">Fact</p><h1 tabindex="-1">${f ? "Fact " + id : "This fact is not in the book"}</h1>
            ${f ? Evidence.card(f, id) : U.h`<p>No fact has the id <span class="mono">${id}</span>.</p>`}
            <p><a href="#home">Go to Today</a></p></article>`);
        });
      }
    });
  }

})(globalThis.SAA = globalThis.SAA || {});
