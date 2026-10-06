// The prototype (readiness + Maths 1–16 + English Batch E1) builds from the real engine and content, offline, under 448 KB.
import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";

const ROOT = new URL("../", import.meta.url);
const FILE = new URL("tools/prototype/form1.html", ROOT);
const page = () => readFileSync(FILE, "utf8");
const constant = (html, name) => JSON.parse(html.match(new RegExp(`const ${name} = (.*);\\n`))[1]);

test("prototype: builds under 448 KB, no external resources, engine runs", () => {
  execFileSync(process.execPath, [new URL("tools/prototype/build.mjs", ROOT).pathname.replace(/^\/([A-Za-z]:)/, "$1")]);
  const html = page();
  assert.ok(Buffer.byteLength(html) < 448 * 1024, `${Buffer.byteLength(html)} bytes`);
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
  const qs = ENGINE.readiness.buildReadiness(l0, 3, ENGINE.libs.maths);
  assert.equal(qs.length, 13);
  assert.ok(qs.every((q) => q.verified));
  // English questions build with the inlined English library.
  const e3 = JSON.parse(readFileSync(new URL("content/english/3.json", ROOT), "utf8"));
  const q = ENGINE.template.instantiate(e3.questions.find((t) => t.id === "e3-form"), 5, ENGINE.libs.english, 3);
  assert.deepEqual(ENGINE.template.check(q, q.answer), { correct: true });
});

test("prototype: Maths 1–16 and English E1 are in the page; deferred speech work is not", () => {
  const html = page();
  const content = constant(html, "CONTENT"), titles = constant(html, "TITLES"), lessons = constant(html, "LESSONS");
  assert.deepEqual(lessons.maths, Array.from({ length: 16 }, (_, i) => i + 1));
  assert.deepEqual(lessons.english, [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16]);
  for (const s of ["maths", "english"]) for (const n of lessons[s]) {
    assert.equal(content[s][n]?.lesson_no, n, `${s} ${n}`);
    assert.ok(titles[s][n], `${s} ${n} title`);
  }
  for (const n of [4, 8, 12]) {
    assert.equal(content.english[n], undefined, `English ${n} is deferred and must not ship`);
    assert.equal(titles.english[n], undefined);
  }
  assert.doesNotMatch(JSON.stringify(titles.english), /Speech Work/);
});

test("prototype: motion off under prefers-reduced-motion; 48px tap targets; text and number keyboards", () => {
  const html = page();
  const reduced = html.match(/@media \(prefers-reduced-motion: reduce\) \{([\s\S]*?)\n\}/);
  assert.ok(reduced, "needs a prefers-reduced-motion block");
  assert.match(reduced[1], /animation: none !important/);
  assert.match(reduced[1], /transition: none !important/);
  assert.match(reduced[1], /\.confetti \{ display: none; \}/);
  assert.match(html, /button \{[^}]*min-height: 48px/, "buttons at least 48px tall");
  for (const cls of ["button.tile", "button.match", "label.tickrow", "input.blank-input"]) {
    assert.match(html, new RegExp(`${cls.replace(".", "\\.")} \\{[^}]*min-height: 48px`), `${cls} at least 48px tall`);
  }
  assert.match(html, /input, textarea \{[^}]*min-height: 52px/, "answer box at least 48px tall");
  assert.match(html, /inputmode: inputModeFor\(q\)/, "keyboard chosen by the engine (number pad or text)");
  assert.match(html, /normaliseInput\(input\.value, q\)/, "typed answers normalised before checking");
  assert.match(html, /autocorrect: "off", autocapitalize: "off",\s*spellcheck: "false"/, "the phone must not correct spelling for the pupil");
  // no dragging anywhere: tap only
  assert.doesNotMatch(html, /draggable|dragstart|ondrop|touchmove|pointermove/);
  // a placed tile leaves an empty slot: lists of tiles go through fill(), never straight into replaceChildren
  // (that showed the word "null" in ordering questions until 2026-10-06)
  assert.doesNotMatch(html, /replaceChildren\(\.\.\.[^;]*\? null/);
  // readiness must stay neutral: no flash, shake or check icon on that path
  const readinessCode = html.slice(html.indexOf("function readinessQ"), html.indexOf("function readinessDone"));
  assert.doesNotMatch(readinessCode, /flash|shake|checkIcon|Correct/);
  // the results text (readiness score, weak areas) is folded away on the pupil's end screen
  assert.match(html, /el\("details", \{ class: "grownup" \}/);
  // paper-task ticks go to the results only: no score, no mastery
  const paper = html.slice(html.indexOf("function paperTask"), html.indexOf("function retry"));
  assert.match(paper, /I've written it/);
  assert.doesNotMatch(paper, /answerItem|check\(/);
});
