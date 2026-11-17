/* files.js: views "files" (Get files) and "about". ARCHITECTURE.md sections 8.5 and 5.6. */
(function (SAA) {
  "use strict";

  var U = SAA.U;
  var Files = SAA.Files = {};
  var noSave = false;      /* true after a failure that means saving cannot work in this visit */

  function manifest() { return (SAA.state && SAA.state.manifest) || null; }
  function caps() { return (SAA.state && SAA.state.caps) || {}; }
  function paint(root, safe) { SAA.Plan.paint(root, safe); }

  function size(bytes) {
    if (!(bytes > 0)) return "";
    if (bytes < 1024 * 1024) return Math.max(1, Math.round(bytes / 1024)) + " KB";
    return (Math.round(bytes / (1024 * 1024) * 10) / 10) + " MB";
  }

  function ext(name) { var m = /\.([a-z0-9]+)$/i.exec(name || ""); return m ? m[1].toLowerCase() : ""; }

  function kind(name) {
    var e = ext(name);
    if (e === "zip") return "Anki deck (zip): unzip it, then open the .apkg file with Anki.";
    if (e === "pdf") return "PDF to read or print from your own device.";
    if (e === "txt") return "Plain text file.";
    return "File.";
  }

  /* The message for a rejected downloads.save. hide: no Save button can work in this visit. */
  function saveError(code, repo) {
    var at = repo ? " On your laptop it is at " + repo + "." : "";
    if (code === "declined") return {text: "", hide: false};
    if (code === "rate_limited") return {text: "A save prompt is already open.", hide: false};
    if (code === "extension_not_enabled" || code === "rejected_extension") return {text: "This file type cannot be saved here." + at, hide: false};
    if (code === "too_large") return {text: "This file is too large to save here." + at, hide: false};
    if (code === "bad_request" || code === "transform_error" || code === "request_unknown") return {text: "The file could not be saved.", hide: false, log: true};
    return {text: "Saving does not work in this view." + at, hide: true};
  }

  /* "Save my progress": resolves the line to show (an empty string for nothing). */
  Files.saveProgress = function () {
    var dl = caps().downloads;
    if (!dl || noSave) return Promise.resolve("Saving a file does not work in this view. Use Copy summary for Claude.");
    var data;
    try { data = JSON.stringify(SAA.Store.exportAll()); } catch (e) { return Promise.resolve("The file could not be made."); }
    return dl.save({filename: "saa-progress.json", data: data}).then(function (res) {
      return res && res.status === "saved" ? "Saved saa-progress.json. Keep it: Restore progress on the About page reads it." : "";
    }, function (e) {
      var r = saveError((e && e.code) || "unavailable", "");
      if (r.hide) noSave = true;
      if (r.log && typeof console !== "undefined") console.error("downloads.save", e);
      return r.text;
    });
  };

  /* ---------- Get files ---------- */

  var F = {root: null, offs: [], notes: {}, busy: ""};

  function drawFiles() {
    if (!F.root) return;
    var man = manifest();
    var head = U.h`<header class="files-head"><p class="eyebrow">Reference</p><h1 id="files-h1" tabindex="-1">Get files</h1></header>`;
    if (!man) { paint(F.root, U.h`${head}<p class="files-note">Loading the list…</p>`); return; }
    var list = man.exports || [], single = !!(SAA.state && SAA.state.single);
    var can = !!caps().downloads && !noSave && !single;
    var hasZip = list.some(function (x) { return ext(x.name) === "zip"; });
    var rows = list.map(function (x, i) {
      var note = F.notes[x.path] || "";
      return U.h`<li class="files-row"><div class="files-row-m"><p class="files-name mono">${x.name}</p><p class="files-kind">${kind(x.name)} <span class="mono">${size(x.bytes)}</span></p>${!can && x.repo ? U.h`<p class="files-repo">On your laptop: <code>${x.repo}</code></p>` : ""}<p class="files-note" role="status">${note}</p></div>${can ? U.h`<button type="button" class="btn" id="${"files-save-" + i}" data-act="files-save" data-i="${i}" ${F.busy === x.path ? U.h`disabled` : ""}>${F.busy === x.path ? "Loading…" : "Save"}</button>` : ""}</li>`;
    });
    var body = list.length
      ? U.h`<ul class="files-list">${rows}</ul>`
      : U.h`<p class="files-note">No files are published with this build yet.</p>`;
    var why = "";
    if (list.length && !can) {
      why = single ? "This build is one file, so the files are not attached. They are on your laptop."
        : "Saving files does not work in this view. The files are on your laptop.";
    }
    paint(F.root, U.h`${head}
      <p class="files-lede">The printable pack and the card deck, made from the same sources as this page.</p>
      ${why ? U.h`<p class="notice">${why}</p>` : ""}
      ${body}
      <p class="files-foot">On your laptop these files are in <code>aws-saa-book/exports/</code>.${hasZip ? "" : " The Anki deck (.apkg) is only there for now; it cannot be saved from this page."}</p>
      ${can && list.some(function (x) { return ext(x.name) === "pdf"; }) ? U.h`<p class="files-foot">For a paper copy, save the PDF and print it from your own device.</p>` : ""}`);
  }

  function saveFile(i) {
    var man = manifest(), x = man && (man.exports || [])[i], dl = caps().downloads;
    if (!x || !dl || F.busy) return;
    F.busy = x.path;
    F.notes[x.path] = "";
    drawFiles();
    function done(text) { F.busy = ""; F.notes[x.path] = text; drawFiles(); }
    SAA.Content.blob(x.path).then(function (blob) {
      if (!blob || !blob.size) { done("The file could not be loaded."); return null; }
      return dl.save({filename: x.name, data: blob}).then(function (res) {
        done(res && res.status === "saved" ? "Saved." : "");
      }, function (e) {
        var r = saveError((e && e.code) || "unavailable", x.repo);
        if (r.hide) noSave = true;
        if (r.log && typeof console !== "undefined") console.error("downloads.save", e);
        done(r.text);
      });
    }, function () { done("The file could not be loaded. Check your connection and try again."); });
  }

  function redrawFiles() { drawFiles(); }

  var filesView = {
    mount: function (el) {
      F.root = document.createElement("div");
      F.root.className = "files";
      el.appendChild(F.root);
      F.notes = {};
      F.busy = "";
      F.offs = [U.on(F.root, "click", "button[data-act=\"files-save\"]", function (ev, btn) { saveFile(Number(btn.getAttribute("data-i"))); })];
      SAA.bus.on("caps", redrawFiles);
      SAA.bus.on("manifest", redrawFiles);
      drawFiles();
      return SAA.Content.manifest().then(drawFiles);
    },
    unmount: function () {
      F.offs.forEach(function (off) { off(); });
      F.offs = [];
      SAA.bus.off("caps", redrawFiles);
      SAA.bus.off("manifest", redrawFiles);
      F.root = null;
    },
    title: function () { return "Get files"; }
  };

  /* ---------- About ---------- */

  var A = {root: null, offs: [], note: "", restore: "", summary: "", perm: "", report: ""};

  function savingBlock() {
    var St = SAA.Store, info = St.info ? St.info() : {status: St.status(), memory: false, consent: null}, c = caps();
    var line, more = "", canSave = !!c.downloads && !noSave;
    if (info.status === "cloud") {
      line = info.memory ? "Your progress is saved online only. This browser does not let the page keep a copy."
        : "Your progress is saved online and on this device.";
    } else if (info.memory) {
      line = "Progress is not being saved on this device. It stays until you close this tab. " + (canSave ? "Save a file to keep it." : "Copy the summary to keep your numbers.");
    } else {
      line = "Your progress is saved on this device only. Claude cannot read it from here. To share it, copy the summary" + (canSave ? "; to keep a copy, save a file." : ".");
    }
    if (info.status !== "cloud" && info.consent === "prompt" && c.db) {
      more = U.h`<p><button type="button" class="btn" id="about-sync" data-act="about-sync">Save online too</button> <span class="about-note">Claude asks for permission the first time.</span></p>`;
    } else if (info.status !== "cloud" && info.consent === "denied" && c.permissions) {
      more = U.h`<p>Saving online is turned off for this page. <button type="button" class="btn" id="about-perm" data-act="about-perm">Open permissions</button></p>`;
    }
    return U.h`<section class="about-sec" aria-labelledby="about-save-h"><h2 id="about-save-h">Saving your progress</h2>
      <p>${line}</p>${more}${A.perm ? U.h`<p class="about-note" role="status">${A.perm}</p>` : ""}
      <div class="ds-acts"><button type="button" class="btn" id="about-copy" data-act="about-copy">Copy summary for Claude</button>${canSave ? U.h`<button type="button" class="btn" id="about-save" data-act="about-save">Save my progress</button>` : ""}</div>
      <p class="about-note" id="about-note" role="status">${A.note}</p>
      ${A.summary ? U.h`<label for="about-summary">Select this text and copy it</label><textarea id="about-summary" class="ds-summary" rows="8" readonly>${A.summary}</textarea>` : ""}
      <h3>Restore progress</h3>
      <p class="about-note">Choose the file <span class="mono">saa-progress.json</span> that "Save my progress" made. Restoring adds to what is here; it does not delete anything.</p>
      <p><label for="about-restore">Progress file</label> <input type="file" id="about-restore" accept=".json,application/json"></p>
      <p><label for="about-restore-text">or paste the file's text here</label></p>
      <textarea id="about-restore-text" rows="4" spellcheck="false"></textarea>
      <p><button type="button" class="btn" id="about-restore-go" data-act="about-restore">Restore</button></p>
      <p class="about-note" id="about-restore-note" role="status">${A.restore}</p>
    </section>`;
  }

  function drawAbout() {
    if (!A.root) return;
    var man = manifest(), st = SAA.state || {}, settings = SAA.Store.get("settings"), c = caps();
    var sizes = ["Smaller", "Normal", "Larger"].map(function (label, i) {
      var id = "about-ts-" + i;
      return U.h`<div class="about-ts-o"><input type="radio" name="about-ts" id="${id}" value="${i}" data-on="${Number(settings.textSize) === i ? "1" : "0"}"><label for="${id}">${label}</label></div>`;
    });
    var aiOff = c.sample && SAA.AI && SAA.AI.available && !SAA.AI.available();
    var keepText = A.root.querySelector("#about-restore-text"), kept = keepText ? keepText.value : "";
    var keepRep = A.root.querySelector("#about-report"), keptRep = keepRep ? keepRep.value : "";
    paint(A.root, U.h`<header class="about-head"><p class="eyebrow">Reference</p><h1 id="about-h1" tabindex="-1">About this handbook</h1></header>
      <section class="about-sec" aria-labelledby="about-build-h"><h2 id="about-build-h">This copy</h2>
        <p>Build <span class="mono">${st.build || (man && man.build) || "unknown"}</span>${man && man.date ? U.h`, content checked up to <span class="mono">${man.date}</span>` : ""}.</p>
        <p>Every fact in the book links to the AWS page it comes from. The practice questions are original.</p>
      </section>
      ${savingBlock()}
      <section class="about-sec" aria-labelledby="about-read-h"><h2 id="about-read-h">Who can read your progress</h2>
        <p>${SAA.Store.status() === "cloud" ? "The owner of this page, and Claude in the owner's session, can read study progress. Nobody else can."
          : "Your progress is not saved online, so nobody else can read it. Claude sees your numbers only when you copy the summary and paste it into a chat."}</p>
      </section>
      <section class="about-sec" aria-labelledby="about-ts-h"><h2 id="about-ts-h">Text size</h2>
        <fieldset class="about-ts"><legend class="vh">Text size</legend>${sizes}</fieldset>
      </section>
      ${aiOff && c.permissions ? U.h`<section class="about-sec" aria-labelledby="about-ai-h"><h2 id="about-ai-h">Claude features</h2><p>Claude features are off for this page. <button type="button" class="btn" id="about-perm-ai" data-act="about-perm">Open permissions</button></p></section>` : ""}
      <section class="about-sec" aria-labelledby="about-rep-h"><h2 id="about-rep-h">Report a problem</h2>
        <p><label for="about-report">What is wrong, and where?</label></p>
        <textarea id="about-report" rows="3" maxlength="500"></textarea>
        <p><button type="button" class="btn" id="about-report-go" data-act="about-report">Send</button></p>
        <p class="about-note" role="status">${A.report}</p>
      </section>`);
    var t = A.root.querySelector("#about-restore-text");
    if (t && kept) t.value = kept;
    var rp = A.root.querySelector("#about-report");
    if (rp && keptRep) rp.value = keptRep;
  }

  function restoreText(text) {
    var obj = null, res;
    try { obj = JSON.parse(text); } catch (e) { obj = null; }
    res = obj ? SAA.Store.importAll(obj) : {ok: false};
    if (res.ok) {
      A.restore = "Restored " + res.counts.answers + " " + (res.counts.answers === 1 ? "answer" : "answers") + " and " +
        res.counts.attempts + " " + (res.counts.attempts === 1 ? "attempt" : "attempts") + ".";
      var t = A.root && A.root.querySelector("#about-restore-text");
      if (t) t.value = "";
    } else A.restore = "This is not a progress file of this book.";
    drawAbout();
  }

  function restoreFile(input) {
    var file = input.files && input.files[0];
    if (!file) return;
    var reader = new FileReader();
    reader.onload = function () { restoreText(String(reader.result || "")); };
    reader.onerror = function () { A.restore = "The file could not be read. Paste its text below."; drawAbout(); };
    reader.readAsText(file);
  }

  function openPermissions() {
    var p = caps().permissions;
    if (!p) return;
    p.manage().then(function () {
      return p.state("db").then(function (state) {
        if (state === "granted" && caps().db && SAA.state.uid) { SAA.Store.consent(null); SAA.Store.attach(caps().db, SAA.state.uid); }
        A.perm = "";
        drawAbout();
      });
    }, function () {
      A.perm = "Open the Permissions menu of this page to allow saving.";
      drawAbout();
    });
  }

  function copySummary() {
    var text = SAA.Store.summaryText();
    U.copy(text).then(function (ok) {
      A.note = ok ? "Summary copied. Paste it into a chat with Claude." : "Copy did not work here. Select the text below and copy it.";
      A.summary = ok ? "" : text;
      drawAbout();
      if (!ok) {
        var ta = document.getElementById("about-summary");
        if (ta) { ta.focus(); ta.select(); }
      }
    });
  }

  function onStore(d) { if (!d || (d.doc !== "ui" && d.doc !== "progress" && d.doc !== "qstats")) drawAbout(); }
  function redrawAbout() { drawAbout(); }

  var aboutView = {
    mount: function (el) {
      A.root = document.createElement("div");
      A.root.className = "about";
      el.appendChild(A.root);
      A.note = A.restore = A.summary = A.perm = A.report = "";
      A.offs = [
        U.on(A.root, "click", "button[data-act=\"about-copy\"]", copySummary),
        U.on(A.root, "click", "button[data-act=\"about-save\"]", function () {
          Files.saveProgress().then(function (text) { A.note = text || ""; drawAbout(); });
        }),
        U.on(A.root, "click", "button[data-act=\"about-sync\"]", function () {
          SAA.Store.attach(caps().db || null, (SAA.state && SAA.state.uid) || null).then(drawAbout);
        }),
        U.on(A.root, "click", "button[data-act=\"about-perm\"]", openPermissions),
        U.on(A.root, "click", "button[data-act=\"about-restore\"]", function () {
          var t = A.root.querySelector("#about-restore-text");
          restoreText(t ? t.value : "");
        }),
        U.on(A.root, "change", "#about-restore", function (ev, input) { restoreFile(input); }),
        U.on(A.root, "change", "input[name=\"about-ts\"]", function (ev, input) {
          if (input.checked) SAA.Store.patch("settings", {textSize: Number(input.value)});
        }),
        U.on(A.root, "click", "button[data-act=\"about-report\"]", function () {
          var t = A.root.querySelector("#about-report"), text = t ? t.value.trim() : "";
          if (!text) { A.report = "Write a few words first."; drawAbout(); return; }
          SAA.Store.flag("section", "about", text);
          t.value = "";
          A.report = SAA.Store.status() === "cloud" ? "Report saved." : "Report saved on this device. It is sent when online saving is on.";
          drawAbout();
        })
      ];
      SAA.bus.on("store:status", redrawAbout);
      SAA.bus.on("store:change", onStore);
      SAA.bus.on("caps", redrawAbout);
      SAA.bus.on("manifest", redrawAbout);
      drawAbout();
      if (SAA.Store.refreshCoach) SAA.Store.refreshCoach();
    },
    unmount: function () {
      A.offs.forEach(function (off) { off(); });
      A.offs = [];
      SAA.bus.off("store:status", redrawAbout);
      SAA.bus.off("store:change", onStore);
      SAA.bus.off("caps", redrawAbout);
      SAA.bus.off("manifest", redrawAbout);
      A.root = null;
    },
    title: function () { return "About"; }
  };

  if (SAA.Router && SAA.Router.register) {
    SAA.Router.register("files", filesView);
    SAA.Router.register("about", aboutView);
  }

  if (SAA.Test && SAA.Test.register) {
    SAA.Test.register("files", function (el) {
      SAA.Store.reset();
      return filesView.mount(el, [], {hot: null});
    });
    SAA.Test.register("about", function (el) {
      SAA.Store.reset();
      return aboutView.mount(el, [], {hot: null});
    });
  }
})(globalThis.SAA = globalThis.SAA || {});
