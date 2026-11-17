/* ai.js (owner E). The one place that calls the sample capability. */
(function (SAA) {
  "use strict";

  var U = SAA.U, bus = SAA.bus, Core = SAA.AICore;
  var AI = SAA.AI = SAA.AI || {};

  var running = null;   /* {ctl} while a call runs */
  var off = false;      /* true after a "hide" failure, until reload */

  function sampleFn() {
    var caps = SAA.state && SAA.state.caps;
    return (caps && caps.sample) || null;
  }

  AI.available = function () { return !off && !!sampleFn(); };

  /* True after Claude features were switched off by a failure (About reads it). */
  AI.hidden = function () { return off; };

  AI.busy = function () { return !!running; };

  function hideAll() {
    off = true;
    try {
      var list = document.querySelectorAll(".sec-ask, .ai-only");
      for (var i = 0; i < list.length; i++) list[i].hidden = true;
    } catch (e) { /* no document */ }
    bus.emit("ai:off", {});
  }

  function fail(code, raw) {
    var m = Core.message(code);
    if (m.bug && typeof console !== "undefined") console.error("sample", code, raw && raw.message);
    if (m.hide) hideAll();
    return {ok: false, code: code, message: m.text, hide: m.hide, retry: m.retry};
  }

  AI.call = function (input, opts) {
    opts = opts || {};
    var sample = sampleFn();
    if (off || !sample) return Promise.resolve({ok: false, code: "not_granted", message: "", hide: true, retry: false});
    if (typeof sample.json !== "function") return Promise.resolve(fail("capability_removed"));
    if (running) return Promise.resolve({ok: false, code: "busy", message: "", hide: false, retry: false});
    if (Core.turnBytes(input) > Core.CAPS.promptBytes) return Promise.resolve(fail("prompt_too_large"));

    var ctl = new AbortController();
    var mine = running = {ctl: ctl};
    var onState = typeof opts.onState === "function" ? opts.onState : function () {};
    var options = {modelTier: opts.tier || "default", signal: ctl.signal};
    if (opts.cache === false) options.cache = false;

    function done() {
      if (running === mine) running = null;
      try { onState("idle"); } catch (e) { /* caller's problem */ }
    }

    try { onState("busy"); } catch (e) { /* caller's problem */ }
    var p;
    try { p = Promise.resolve(sample.json(input, options)); }
    catch (e) { p = Promise.reject(e); }
    return p.then(function (data) {
      done();
      return {ok: true, data: data};
    }, function (err) {
      done();
      var code = err && typeof err.code === "string" ? err.code : "upstream_error";
      return fail(code, err);
    });
  };

  AI.stop = function () {
    if (!running) return;
    try { running.ctl.abort(); } catch (e) { /* already settled */ }
  };

  AI.notice = function () {
    return U.h`<p class="ai-note">This uses your Claude usage. Claude asks for permission the first time.</p>`;
  };

  /* The "Checking…" line with its Stop button; callers handle data-act="ai-stop" with AI.stop(). */
  AI.busyHtml = function (hidden) {
    return U.h`<span class="ai-busy" role="status"${hidden ? U.raw(" hidden") : ""}><span class="ai-busy-t">Checking…</span> <button type="button" class="btn quiet" data-act="ai-stop">Stop</button></span>`;
  };

})(globalThis.SAA = globalThis.SAA || {});
