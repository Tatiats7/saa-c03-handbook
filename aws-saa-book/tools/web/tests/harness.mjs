// Test harness for the pure modules of the web version (ARCHITECTURE.md 9.1).
// No dependencies. Run a test file with: node aws-saa-book/tools/web/tests/test_<name>.mjs [built folder]
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));

function firstDir(list) {
  for (const p of list) {
    try { if (fs.statSync(p).isDirectory()) return p; } catch (e) { /* next */ }
  }
  return list[0];
}

// The js/ folder: next to tests/ (tools/web/js), or tools/web/js when the tests are moved to tools/tests/.
export const JS_DIR = firstDir([
  path.resolve(HERE, "../js"),
  path.resolve(HERE, "../web/js"),
  path.resolve("aws-saa-book/tools/web/js")
]);

// The book folder (aws-saa-book).
export const BOOK_DIR = firstDir([
  path.resolve("aws-saa-book"),
  path.resolve(HERE, "../../.."),
  path.resolve(HERE, "../..")
]);

// The built site that fixture() reads: the first command-line argument, else the selftest build.
export const BUILT_DIR = path.resolve(process.argv[2] || path.join(BOOK_DIR, "_build/tmp/web-selftest"));

// Evaluates the named files of js/ in one context without a DOM and returns SAA.
export function load(files, globals) {
  const sandbox = { console, setTimeout, clearTimeout };
  Object.assign(sandbox, globals || {});
  const context = vm.createContext(sandbox);
  vm.runInContext("globalThis.SAA = {};", context);
  for (const name of files) {
    const file = path.join(JS_DIR, name);
    vm.runInContext(fs.readFileSync(file, "utf8"), context, { filename: file });
  }
  return vm.runInContext("globalThis.SAA", context);
}

// Reads one built JSON file. Returns null when the file does not exist.
export function fixture(rel) {
  const file = path.join(BUILT_DIR, rel);
  if (!fs.existsSync(file)) return null;
  return JSON.parse(fs.readFileSync(file, "utf8"));
}

// Lists the built JSON files of one folder ("d", "q"), as paths for fixture().
export function built(folder) {
  const dir = path.join(BUILT_DIR, folder);
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter((f) => f.endsWith(".json")).sort().map((f) => folder + "/" + f);
}

let passed = 0;
let failed = 0;
let current = "";
let currentFailed = false;

function fail(message) {
  if (!currentFailed) console.log("FAIL " + current);
  currentFailed = true;
  console.log("     " + message);
}

export function ok(value, message) {
  if (!value) fail(message || "expected a true value");
}

export function eq(actual, expected, message) {
  const a = JSON.stringify(actual);
  const b = JSON.stringify(expected);
  if (a !== b) fail((message ? message + ": " : "") + "got " + a + ", expected " + b);
}

export function test(name, fn) {
  current = name;
  currentFailed = false;
  try {
    fn();
  } catch (e) {
    fail("threw " + (e && e.stack ? e.stack : e));
  }
  if (currentFailed) {
    failed++;
    process.exitCode = 1;
  } else {
    passed++;
    console.log("ok   " + name);
  }
}

process.on("exit", () => {
  console.log((failed ? "FAILED " : "PASSED ") + passed + "/" + (passed + failed));
});
