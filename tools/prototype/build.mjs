// Builds tools/prototype/form1.html: one self-contained file (engine + content + UI), works offline.
// Maths: Lesson 0 (readiness) and Lessons 1–16. English: Batch E1 (Lessons 1–16, speech work left out).
// Progress is saved in the browser.
//   node tools/prototype/build.mjs
// The engine modules are inlined unchanged except for import/export lines, so the prototype runs
// exactly the code the tests cover.
import { readFileSync, writeFileSync } from "node:fs";
import { posix } from "node:path";

const ROOT = new URL("../../", import.meta.url);
const read = (p) => readFileSync(new URL(p, ROOT), "utf8");
const ENGINE = ["rng.js", "expr.js", "lib/maths.js", "lib/english.js", "template.js", "state.js", "teach.js", "readiness.js"];  // dependency order
// 120 KB for Lesson 3 alone (2026-10-03); 256 KB for Maths 1–16 (2026-10-05); 448 KB with English E1 (2026-10-06).
// The Phase 3 budget for the whole app is 2 MB.
const MAX_BYTES = 448 * 1024;
const SUBJECTS = { maths: "Maths", english: "English" };
const SPINE = { maths: "mathematics", english: "english-language" };
const BATCH = Array.from({ length: 16 }, (_, i) => i + 1);

function bundleModule(path) {
  const src = read(`src/engine/${path}`);
  const exports = [];
  let code = src.replace(/^import\s+\{([^}]+)\}\s+from\s+"([^"]+)";\s*$/gm, (_, names, spec) => {
    const target = posix.normalize(posix.join(posix.dirname(path), spec));
    if (!ENGINE.includes(target)) throw new Error(`${path}: cannot inline ${spec}`);
    return `const {${names}} = __mods[${JSON.stringify(target)}];`;
  });
  if (/^import\s/m.test(code)) throw new Error(`${path}: unsupported import form`);
  code = code.replace(/^export\s+(async\s+function|function|const|let|class)\s+([A-Za-z_$][\w$]*)/gm, (_, kind, name) => {
    exports.push(name);
    return `${kind} ${name}`;
  });
  if (/^export\s/m.test(code)) throw new Error(`${path}: unsupported export form`);
  return `__mods[${JSON.stringify(path)}] = (() => {\n${code}\nreturn { ${exports.join(", ")} };\n})();`;
}

// Display only (the spine keeps the sheet's text): "Number bases :Convert" → "Number bases: Convert",
// "Line segment.- Midpoint" → "Line segment: Midpoint", "Vocabulary-countable …;" → "Vocabulary: countable …".
const tidy = (t) => t
  .replace(/^(Speaking|Reading|Writing|Vocabulary|Grammar|Listening)\s*[-:]?\s*/, "$1: ")
  .replace(/\s*\.?\s*-\s+/g, ": ").replace(/\s*:\s*/g, ": ").replace(/[;\s]+$/, "").replace(/\s+/g, " ").trim();
const titles = {}, content = {}, lessons = {};
for (const s of Object.keys(SUBJECTS)) {
  const spine = JSON.parse(read(`data/spine/${SPINE[s]}.json`));
  titles[s] = Object.fromEntries(spine.terms.flatMap((t) => t.lessons).filter((l) => l.kind === "lesson" && l.lesson_no <= 16).map((l) => [l.lesson_no, tidy(l.title)]));
  const all = Object.fromEntries((s === "maths" ? [0, ...BATCH] : BATCH).map((n) => [n, JSON.parse(read(`content/${s}/${n}.json`))]));
  // Deferred lessons (speech work: needs audio) are not shipped at all: hidden from the pupil (TR-E22).
  content[s] = Object.fromEntries(Object.entries(all).filter(([, l]) => l.status !== "deferred"));
  lessons[s] = BATCH.filter((n) => content[s][n]);
  titles[s] = Object.fromEntries(Object.entries(titles[s]).filter(([n]) => content[s][n]));
  for (const n of lessons[s]) if (!titles[s][n]) throw new Error(`no spine title for ${s} Lesson ${n}`);
}
const build = new Date().toISOString().slice(0, 10);
const safeJson = (x) => JSON.stringify(x).replace(/</g, "\\u003c");

const css = `
:root { --bg:#fbfaf7; --fg:#1d1c1a; --muted:#5f5b53; --card:#ffffff; --line:#d9d4c9; --accent:#1f6f4a; --accent-press:#185a3c; --accent-fg:#ffffff;
  --good-bg:#e7f4ec; --good:#1a6340; --flash:#9fe0bb; --bad-bg:#fdeceb; --bad:#a3322a; --soft:#f2efe8; --idk-border:#8a857b; --track:#e6e1d6; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#161513; --fg:#ece9e2; --muted:#b3ada2; --card:#211f1c;
  --line:#3a3732; --accent:#4fb487; --accent-press:#43a077; --accent-fg:#0d1f16; --good-bg:#1b3327; --good:#8fdcb2; --flash:#2f7a52;
  --bad-bg:#3a1f1d; --bad:#f0a59e; --soft:#26241f; --idk-border:#8f897e; --track:#33302b; } }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--fg); font: 18px/1.5 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }
#app { max-width: 520px; margin: 0 auto; padding: 16px 16px 48px; }
.screen { animation: enter 200ms ease-out both; }
@keyframes enter { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
.progress { display: flex; align-items: center; gap: 12px; margin: 0 0 14px; }
.progress .track { flex: 1; height: 12px; border-radius: 6px; background: var(--track); overflow: hidden; }
.progress .fill { height: 100%; border-radius: 6px; background: var(--accent); transition: width 300ms ease-out; }
.progress .count { font-size: 1.05rem; font-weight: 700; font-variant-numeric: tabular-nums; white-space: nowrap; }
header { margin: 4px 0 16px; } h1 { font-size: 1.3rem; line-height: 1.3; margin: 2px 0 0; }
.kicker { font-size: .8rem; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); }
p { margin: 0 0 10px; } .muted { color: var(--muted); font-size: .95rem; } .strong { font-weight: 600; }
.prompt { font-size: 1.15rem; font-weight: 600; margin: 8px 0 16px; overflow-wrap: anywhere; }
.idea { font-size: 1.1rem; background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 14px; margin-bottom: 12px; }
.example, .note, .hint { background: var(--soft); border-radius: 12px; padding: 14px; margin-bottom: 14px; overflow-wrap: anywhere; }
.example ol { padding-left: 1.2em; margin: 6px 0; }
button { display: block; width: 100%; min-height: 48px; margin: 10px 0 0; padding: 10px 14px; border-radius: 12px; font: inherit;
  border: 1px solid var(--line); background: var(--card); color: var(--fg); text-align: left; cursor: pointer;
  transition: transform 90ms ease-out, background-color 90ms ease-out, box-shadow 90ms ease-out; -webkit-tap-highlight-color: transparent; }
button:active { transform: scale(.97); background: var(--soft); }
button:focus-visible, input:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }
button.primary { background: var(--accent); color: var(--accent-fg); border-color: var(--accent); text-align: center; font-weight: 700;
  box-shadow: 0 2px 0 var(--accent-press); }
button.primary:active { background: var(--accent-press); box-shadow: none; transform: translateY(2px) scale(.99); }
/* Secondary but readable: full-contrast text on a plain outlined button, below the filled Check button. */
button.idk { text-align: center; color: var(--fg); background: transparent; border: 1.5px solid var(--idk-border); font-weight: 500; margin-top: 18px; }
button.link { text-align: center; background: transparent; border: 0; color: var(--muted); text-decoration: underline; }
.options { display: grid; gap: 0; }
.answer { display: flex; gap: 8px; align-items: center; }
input, textarea { width: 100%; font: inherit; font-size: 1.3rem; min-height: 52px; padding: 10px 12px; border-radius: 12px; border: 1.5px solid var(--line);
  background: var(--card); color: var(--fg); }
textarea { font-size: .8rem; font-family: ui-monospace, Menlo, Consolas, monospace; margin-top: 10px; min-height: 0; }
.unit { color: var(--muted); white-space: nowrap; }
.chosen { min-height: 24px; padding-left: 1.4em; } .chosen li { margin: 4px 0; font-weight: 600; }
.fb { border-radius: 12px; padding: 14px; margin: 8px 0 14px; } .fb strong { display: block; margin-bottom: 6px; font-size: 1.1rem; }
.fb.good { background: var(--good-bg); color: var(--good); display: flex; align-items: center; gap: 12px; } .fb.good strong { margin: 0; font-size: 1.3rem; }
.fb.bad { background: var(--bad-bg); color: var(--fg); } .fb.bad strong { color: var(--bad); }
.fb.soft { background: var(--soft); color: var(--fg); }
.flash { animation: flash 600ms ease-out; }
@keyframes flash { 0% { background: var(--flash); transform: scale(.96); } 40% { transform: scale(1.02); } 100% { background: var(--good-bg); transform: none; } }
.tick { width: 36px; height: 36px; flex: none; fill: none; stroke: currentColor; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round;
  stroke-dasharray: 24; stroke-dashoffset: 0; animation: draw 350ms ease-out 100ms both; }
@keyframes draw { from { stroke-dashoffset: 24; } to { stroke-dashoffset: 0; } }
.shake { animation: shake 320ms ease-in-out; }
@keyframes shake { 0%, 100% { transform: none; } 20% { transform: translateX(-6px); } 40% { transform: translateX(6px); } 60% { transform: translateX(-4px); } 80% { transform: translateX(3px); } }
.done { text-align: center; margin: 48px 0 24px; } .done-title { font-size: 2rem; font-weight: 800; } .done-sub { font-size: 1.15rem; }
.confetti { position: fixed; left: 50%; top: 22%; width: 0; height: 0; pointer-events: none; z-index: 10; }
.confetti i { position: absolute; width: 8px; height: 12px; border-radius: 2px; background: var(--c); opacity: 0;
  animation: burst 1100ms cubic-bezier(.2,.7,.3,1) var(--d) forwards; }
@keyframes burst { 0% { opacity: 1; transform: translate(0, 0) rotate(0); }
  80% { opacity: 1; } 100% { opacity: 0; transform: translate(var(--x), calc(var(--y) + 140px)) rotate(var(--r)); } }
details.grownup { margin-top: 12px; } details.grownup summary { min-height: 48px; display: flex; align-items: center; cursor: pointer; color: var(--muted); }
.pre, .prompt { white-space: pre-line; }
/* subjects */
.subjects { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin: 0 0 14px; }
button.subject { margin: 0; text-align: center; font-weight: 700; }
button.subject.on { background: var(--accent); color: var(--accent-fg); border-color: var(--accent); }
button:disabled { opacity: .45; cursor: default; box-shadow: none; }
/* cloze: the blank sits inside the sentence */
.sentence { font-size: 1.2rem; line-height: 2.1; margin: 0 0 14px; overflow-wrap: anywhere; }
.blank { display: inline-block; min-width: 4.5em; border-bottom: 3px dotted var(--accent); line-height: 1.2; }
input.blank-input { display: inline-block; width: 9em; max-width: 100%; min-height: 48px; padding: 6px 10px; font-size: 1.15rem; vertical-align: middle; }
/* word tiles (word order, sorting): tap, never drag */
.tiles { display: flex; flex-wrap: wrap; gap: 8px; margin: 8px 0; }
button.tile { display: inline-flex; align-items: center; justify-content: center; width: auto; min-width: 48px; min-height: 48px; margin: 0; padding: 8px 14px; text-align: center; }
button.tile.placed { background: var(--soft); border-color: var(--accent); animation: pop 160ms ease-out; }
button.tile.picked, button.match.picked { outline: 3px solid var(--accent); outline-offset: 1px; background: var(--good-bg); }
@keyframes pop { from { transform: scale(.85); } to { transform: none; } }
.built { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; min-height: 64px; padding: 8px; margin: 8px 0 12px;
  border: 1.5px dashed var(--idk-border); border-radius: 12px; }
.built .end { font-size: 1.4rem; font-weight: 700; padding: 0 2px; }
/* matching: two columns at 360px, words wrap */
.match-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin: 8px 0; }
.match-cols .col { display: flex; flex-direction: column; gap: 8px; }
button.match { display: flex; gap: 8px; align-items: center; margin: 0; min-height: 48px; padding: 8px 10px; font-size: 1rem; overflow-wrap: anywhere; }
button.match.paired { background: var(--soft); border-color: var(--accent); }
button.match.ready { border-style: dashed; border-color: var(--accent); }
.badge { flex: none; display: inline-grid; place-items: center; width: 26px; height: 26px; border-radius: 50%; background: var(--accent);
  color: var(--accent-fg); font-size: .85rem; font-weight: 700; }
.group { border: 1.5px solid var(--line); border-radius: 12px; padding: 10px; margin-top: 10px; min-height: 76px; background: var(--card); cursor: pointer; }
.group.ready { border-style: dashed; border-color: var(--accent); }
.group-name { font-size: .85rem; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); font-weight: 700; }
/* paper task self-check */
.ticks { margin: 8px 0 12px; }
label.tickrow { display: flex; gap: 12px; align-items: center; min-height: 48px; padding: 6px 2px; border-bottom: 1px solid var(--line); cursor: pointer; }
label.tickrow input { flex: none; width: 28px; height: 28px; min-height: 0; margin: 0; padding: 0; accent-color: var(--accent); }
.areas { padding-left: 1.2em; } .areas .weak { color: var(--bad); font-weight: 600; }
.lessons { margin: 14px 0; }
button.lesson { display: flex; gap: 12px; align-items: center; margin-top: 8px; }
button.lesson .mark { flex: none; width: 36px; height: 36px; border-radius: 50%; display: grid; place-items: center; font-weight: 700;
  background: var(--soft); color: var(--muted); font-variant-numeric: tabular-nums; }
button.lesson.is-done .mark { background: var(--good-bg); color: var(--good); }
button.lesson .lt { display: flex; flex-direction: column; min-width: 0; overflow-wrap: anywhere; }
button.lesson .ln { font-size: .8rem; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); }
button.lesson .sub { font-size: .9rem; color: var(--muted); }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
  .confetti { display: none; }
  button:active, button.primary:active { transform: none; }
}
`;

const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Form One Lessons</title>
<style>${css}</style>
</head>
<body>
<main id="app"><noscript>This page needs JavaScript.</noscript></main>
<script>
"use strict";
const __mods = {};
${ENGINE.map(bundleModule).join("\n")}
const ENGINE = { libs: { maths: __mods["lib/maths.js"], english: { ...__mods["lib/maths.js"], ...__mods["lib/english.js"] } },
  template: __mods["template.js"], teach: __mods["teach.js"], readiness: __mods["readiness.js"] };
const CONTENT = ${safeJson(content)};
const TITLES = ${safeJson(titles)};
const LESSONS = ${safeJson(lessons)};
const SUBJECTS = ${safeJson(SUBJECTS)};
const BUILD = ${JSON.stringify(build)};
${read("tools/prototype/app.js")}
</script>
</body>
</html>
`;

const bytes = Buffer.byteLength(html, "utf8");
if (bytes > MAX_BYTES) throw new Error(`prototype is ${bytes} bytes, over the ${MAX_BYTES} limit`);
writeFileSync(new URL("tools/prototype/form1.html", ROOT), html, "utf8");
console.log(`wrote tools/prototype/form1.html (${(bytes / 1024).toFixed(1)} KB, limit ${MAX_BYTES / 1024} KB)`);
