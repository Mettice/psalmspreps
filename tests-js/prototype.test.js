// The prototype (readiness + Lessons 1–16) builds from the real engine and content, offline, under 256 KB.
import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";

const ROOT = new URL("../", import.meta.url);

test("prototype: builds under 256 KB, no external resources, engine runs", () => {
  execFileSync(process.execPath, [new URL("tools/prototype/build.mjs", ROOT).pathname.replace(/^\/([A-Za-z]:)/, "$1")]);
  const html = readFileSync(new URL("tools/prototype/maths.html", ROOT), "utf8");
  assert.ok(Buffer.byteLength(html) < 256 * 1024, `${Buffer.byteLength(html)} bytes`);
  assert.doesNotMatch(html, /<script[^>]+src=|<link[^>]+href=|https?:\/\/(?!www\.w3\.org)/, "must not load anything from the network");
  assert.doesNotMatch(html, /indexedDB|fetch\(|XMLHttpRequest|sendBeacon|WebSocket/, "must not send data");
  // Progress is saved in this browser only (2026-10-05): one key, every access wrapped in try/catch.
  const uses = html.match(/localStorage\.\w+\([^)]*\)/g) || [];
  assert.ok(uses.length >= 2, "saves and loads progress");
  for (const u of uses) assert.match(u, /^localStorage\.(getItem|setItem|removeItem)\(KEY(, JSON\.stringify\(state)?\)$/, u);
  // Run the inlined engine (everything before the content) and build the readiness check with it.
  const script = html.split("<script>")[1].split("const CONTENT")[0];
  const ENGINE = new Function(`${script}; return ENGINE;`)();
  const l0 = JSON.parse(readFileSync(new URL("content/maths/0.json", ROOT), "utf8"));
  const qs = ENGINE.readiness.buildReadiness(l0, 3, ENGINE.lib);
  assert.equal(qs.length, 13);
  assert.ok(qs.every((q) => q.verified));
  // every lesson 1–16 is in the page, with its spine title
  const content = JSON.parse(html.match(/const CONTENT = (.*);\n/)[1]);
  const titles = JSON.parse(html.match(/const TITLES = (.*);\n/)[1]);
  for (let n = 1; n <= 16; n++) {
    assert.equal(content[n]?.lesson_no, n, `Lesson ${n} content`);
    assert.ok(titles[n], `Lesson ${n} title`);
  }
});

test("prototype: motion is switched off under prefers-reduced-motion; tap targets and number pad", () => {
  const html = readFileSync(new URL("tools/prototype/maths.html", ROOT), "utf8");
  const reduced = html.match(/@media \(prefers-reduced-motion: reduce\) \{([\s\S]*?)\n\}/);
  assert.ok(reduced, "needs a prefers-reduced-motion block");
  assert.match(reduced[1], /animation: none !important/);
  assert.match(reduced[1], /transition: none !important/);
  assert.match(reduced[1], /\.confetti \{ display: none; \}/);
  assert.match(html, /button \{[^}]*min-height: 48px/, "buttons at least 48px tall");
  assert.match(html, /input, textarea \{[^}]*min-height: 52px/, "answer box at least 48px tall");
  assert.match(html, /inputmode: inputModeFor\(q\)/, "number pad chosen by the engine");
  assert.match(html, /normaliseInput\(input\.value, q\)/, "typed answers normalised before checking");
  // readiness must stay neutral: no flash, shake or check icon on that path
  const readinessCode = html.slice(html.indexOf("function readinessQ"), html.indexOf("function readinessDone"));
  assert.doesNotMatch(readinessCode, /flash|shake|checkIcon|Correct/);
  // the results text (readiness score, weak areas) is folded away on the pupil's end screen
  assert.match(html, /el\("details", \{ class: "grownup" \}/);
});
