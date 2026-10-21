// Builds tools/prototype/form1.html: one self-contained file (engine + content + UI), works offline; and
// tools/prototype/pwa/: the installable app (core page, one file per subject, service worker, manifest, icons).
// Maths: Lesson 0 (readiness) and Lessons 1–16. English: Batch E1 (Lessons 1–16, speech work left out).
// Progress is saved in the browser.
//   node tools/prototype/build.mjs
// The engine modules are inlined unchanged except for import/export lines, so the prototype runs
// exactly the code the tests cover.
import { readFileSync, writeFileSync, mkdirSync, rmSync, copyFileSync, readdirSync } from "node:fs";
import { posix } from "node:path";
import { createHash } from "node:crypto";

const ROOT = new URL("../../", import.meta.url);
const read = (p) => readFileSync(new URL(p, ROOT), "utf8");
const ENGINE = ["rng.js", "expr.js", "lib/maths.js", "lib/maths2.js", "lib/english.js", "lib/physics.js", "lib/chemistry.js", "lib/geography.js", "lib/homeeconomics.js", "lib/history.js", "lib/biology.js", "lib/computerscience.js", "lib/french.js", "lib/french2.js", "lib/science2.js", "template.js", "state.js", "teach.js", "readiness.js"];  // dependency order
// 120 KB for Lesson 3 alone (2026-10-03); 256 KB for Maths 1–16 (2026-10-05); 448 KB with English E1 (2026-10-06).
// The Phase 3 budget for the whole app is 2 MB.
const MAX_BYTES = 2048 * 1024;  // the single shareable file, one per class: within the 2 MB Bluetooth budget (Form Two with French, 2026-10-18)
const SHELL_MAX = 400 * 1024;   // the installable app's core page (engine, screens, titles): content comes per subject  // 900 KB with Home Economics; 1.3 MB with History, Biology and Computer Science (Dion, 2026-10-07); app budget 2 MB
const SUBJECTS = { maths: "Maths", english: "English", physics: "Physics", chemistry: "Chemistry", geography: "Geography", "home-economics": "Home Economics", history: "History", biology: "Biology", "computer-science": "Computer Science", french: "French",
  "f2-maths": "Maths", "f2-english": "English", "f2-physics": "Physics", "f2-chemistry": "Chemistry", "f2-geography": "Geography", "f2-home-economics": "Home Economics",
  "f2-history": "History", "f2-biology": "Biology", "f2-computer-science": "Computer Science", "f2-french": "French", "f2-francais-intensif": "Français intensif", "f2-accounting": "Accounting" };
// Classes (Form 2 from 2026-10-17, on the form-2 branch): a Form 2 subject id starts with "f2-"; its lessons are in
// content/form-2/<subject>/ and its sheet in data/spine/form-2/. Form One stays the default class.
const CLASSES = { "form-1": "Form One", "form-2": "Form Two" };
const CLASS_OF = Object.fromEntries(Object.keys(SUBJECTS).map((s) => [s, s.startsWith("f2-") ? "form-2" : "form-1"]));
const DIR = { "f2-maths": "form-2/maths", "f2-english": "form-2/english", "f2-physics": "form-2/physics", "f2-chemistry": "form-2/chemistry", "f2-biology": "form-2/biology",
  "f2-home-economics": "form-2/home-economics", "f2-geography": "form-2/geography", "f2-history": "form-2/history", "f2-computer-science": "form-2/computer-science", "f2-french": "form-2/french", "f2-francais-intensif": "form-2/francais-intensif", "f2-accounting": "form-2/accounting" };
const SPINE = { maths: "mathematics", english: "english-language", physics: "physics", chemistry: "chemistry", geography: "geography", "home-economics": "home-economics", history: "history", biology: "biology", "computer-science": "computer-science", french: "french",
  "f2-maths": "form-2/mathematics", "f2-english": "form-2/english-language", "f2-physics": "form-2/physics", "f2-chemistry": "form-2/chemistry", "f2-biology": "form-2/biology",
  "f2-home-economics": "form-2/home-economics", "f2-geography": "form-2/geography", "f2-history": "form-2/history", "f2-computer-science": "form-2/computer-science", "f2-french": "form-2/french", "f2-francais-intensif": "form-2/francais-intensif", "f2-accounting": "form-2/accounting" };
const upTo = (n) => Array.from({ length: n }, (_, i) => i + 1);
const BATCH = { maths: upTo(16), english: upTo(16), physics: upTo(19), chemistry: upTo(21), geography: upTo(10), "home-economics": [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21],
  history: upTo(10), biology: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21], "computer-science": [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 16, 17, 18], french: upTo(15),
  "f2-maths": upTo(54), "f2-english": upTo(76), "f2-physics": upTo(31), "f2-chemistry": [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45],
  "f2-biology": [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 25, 26, 27, 28, 29, 30, 31, 32, 33, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
  "f2-home-economics": [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], "f2-geography": upTo(19), "f2-history": upTo(21),
  "f2-computer-science": [1, 2, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16, 18, 19], "f2-accounting": [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12],
  "f2-french": [...upTo(15), ...Array.from({ length: 15 }, (_, i) => i + 18)], "f2-francais-intensif": [...upTo(25), ...Array.from({ length: 25 }, (_, i) => i + 27)] };  // Form 2 sciences: integration, evaluation, remediation and review rows are not lessons  // released lessons per subject (Form 2: Term 1, Batches M2-1 and E2-1)
// Geography is numbered by place in the year (spine seq): its practicals have no lesson number (TR-G14).
const BY_SEQ = new Set(["geography", "history", "biology", "f2-maths", "f2-english", "f2-physics", "f2-chemistry", "f2-biology", "f2-home-economics", "f2-geography", "f2-history", "f2-computer-science", "f2-french", "f2-francais-intensif", "f2-accounting"]);  // biology: practicals have kind "practical" (numbers equal the rows); every Form 2 subject (proposal G1)

// The names each engine module really exports (Node imports it), to check the bundled copy below: a declaration like
// "export const a = …, b = …" once bundled only a, and the page failed while every Node test passed (2026-10-21).
const REAL_EXPORTS = Object.fromEntries(await Promise.all(ENGINE.map(async (p) => [p, Object.keys(await import(new URL(`src/engine/${p}`, ROOT))).sort()])));
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
  const missing = REAL_EXPORTS[path].filter((n) => !exports.includes(n));
  if (missing.length) throw new Error(`${path}: the page bundle would lose ${missing.join(", ")} (write one export per declaration)`);
  return `__mods[${JSON.stringify(path)}] = (() => {\n${code}\nreturn { ${exports.join(", ")} };\n})();`;
}

// Display only (the spine keeps the sheet's text): "Number bases :Convert" → "Number bases: Convert",
// "Line segment.- Midpoint" → "Line segment: Midpoint", "Vocabulary-countable …;" → "Vocabulary: countable …",
// "under- nutrition" → "under-nutrition".
const tidy = (t) => t
  .replace(/(\p{L})- (?=\p{Ll})/gu, "$1-")  // a word split by the sheet: "under- nutrition" → "under-nutrition"
  .replace(/^((?:Speaking|Reading|Writing|Vocabulary|Grammar|Listening)(?: and (?:Speaking|Reading|Writing|Listening))?)\s*[-:]?\s*/, "$1: ")  // "Speaking and Reading- Talking …" (Form 2) → "Speaking and Reading: Talking …"
  .replace(/\s*\.?\s*-\s+/g, ": ").replace(/\s*:\s*/g, ": ").replace(/[;\s]+$/, "").replace(/\s+/g, " ").trim();
// Form Two French titles keep French typography (a space before the colon); Form One titles are unchanged.
const FR_TITLES = new Set(["f2-french", "f2-francais-intensif"]);
const frSpace = (t) => t
  .replace(/(^|[:;.]\s*)-\s*/g, "$1").replace(/\s-(?=\p{Lu})/gu, ", ")    // the sheet's list dashes: "Ecoute :-Textes", ". -Texte"
  .replace(/\s*;\s*/g, " ; ").replace(/\s+,/g, ",").replace(/(\S)\(\s*/g, "$1 (")  // French spacing around ; , (
  .replace(/\/(\S+?)\s+\//g, "/$1/").replace(/\/et\//g, "/ et /").replace(/'/g, "’").replace(/\bEcoute\b/g, "Écoute")
  .replace(/: /g, " : ");
const titles = {}, content = {}, lessons = {}, termOf = {};
for (const s of Object.keys(SUBJECTS)) {
  const spine = JSON.parse(read(`data/spine/${SPINE[s]}.json`));
  const num = (l) => (BY_SEQ.has(s) ? l.seq : l.kind === "lesson" ? l.lesson_no : null);
  titles[s] = Object.fromEntries(spine.terms.flatMap((t) => t.lessons).filter((l) => BATCH[s].includes(num(l))).map((l) => [num(l), FR_TITLES.has(s) ? frSpace(tidy(l.title)) : tidy(l.title)]));
  termOf[s] = Object.fromEntries(spine.terms.flatMap((t) => t.lessons.map((l) => [num(l), t.term])).filter(([n]) => n != null));
  const all = Object.fromEntries((s === "maths" ? [0, ...BATCH[s]] : BATCH[s]).map((n) => [n, JSON.parse(read(`content/${DIR[s] || s}/${n}.json`))]));
  // Deferred lessons (speech work: needs audio) are not shipped at all: hidden from the pupil (TR-E22).
  content[s] = Object.fromEntries(Object.entries(all).filter(([, l]) => l.status !== "deferred"));
  lessons[s] = BATCH[s].filter((n) => content[s][n]);
  titles[s] = Object.fromEntries(Object.entries(titles[s]).filter(([n]) => content[s][n]));
  for (const n of lessons[s]) if (!titles[s][n]) throw new Error(`no spine title for ${s} Lesson ${n}`);
}
// A subject with no released lesson yet is left out of the app.
for (const s of Object.keys(SUBJECTS)) if (!lessons[s].length) for (const x of [SUBJECTS, CLASS_OF, titles, content, lessons, termOf]) delete x[s];
const build = new Date().toISOString().slice(0, 10);
const safeJson = (x) => JSON.stringify(x).replace(/</g, "\\u003c");

const css = `
:root { --bg:#fbfaf7; --fg:#1d1c1a; --muted:#5f5b53; --card:#ffffff; --line:#d9d4c9; --accent:#1f6f4a; --accent-press:#185a3c; --accent-fg:#ffffff;
  --good-bg:#e7f4ec; --good:#1a6340; --flash:#9fe0bb; --bad-bg:#fdeceb; --bad:#a3322a; --soft:#f2efe8; --idk-border:#8a857b; --track:#e6e1d6;
  --fig-liquid:#6aa9e9; --fig-object:#c98b3a; --fig-red:#d0473b; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#161513; --fg:#ece9e2; --muted:#b3ada2; --card:#211f1c;
  --line:#3a3732; --accent:#4fb487; --accent-press:#43a077; --accent-fg:#0d1f16; --good-bg:#1b3327; --good:#8fdcb2; --flash:#2f7a52;
  --bad-bg:#3a1f1d; --bad:#f0a59e; --soft:#26241f; --idk-border:#8f897e; --track:#33302b;
  --fig-liquid:#3f7fc0; --fig-object:#b07a32; --fig-red:#e0635a; } }
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
/* drawings made by the engine (rulers, cylinders, thermometers): readable at 360px, never taller than the screen */
.figure { margin: 4px 0 14px; color: var(--fg); }
.figure svg { display: block; width: 100%; height: auto; max-height: 300px; margin: 0 auto; }
/* subjects */
.subjects { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin: 0 0 14px; }  /* two per row at 360px */
.subjects > :last-child:nth-child(odd) { grid-column: 1 / -1; }  /* an odd last tab takes the whole row */
/* teacher review mode (?review) */
.rv-item { border: 2px solid var(--line); border-radius: 14px; padding: 12px; margin: 0 0 14px; background: var(--card); overflow-wrap: anywhere; }
.rv-item.rv-is-ok { border-color: var(--accent); } .rv-item.rv-is-bad { border-color: var(--bad); background: var(--bad-bg); }
.rv-head { display: flex; justify-content: space-between; gap: 8px; align-items: baseline; margin-bottom: 6px; } .rv-head code { font-size: .8rem; color: var(--muted); }
.rv-options { padding-left: 0; list-style: none; margin: 6px 0 10px; } .rv-options li { padding: 6px 0; border-bottom: 1px solid var(--line); }
.rv-options li.rv-right { font-weight: 700; color: var(--good); }
.rv-tag { font-size: .85rem; color: var(--muted); font-style: italic; }
.rv-note, .rv-name { width: 100%; font: inherit; padding: 10px; border: 1px solid var(--line); border-radius: 10px; background: var(--bg); color: var(--fg); margin: 8px 0; }
.rv-buttons { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; } .rv-buttons button { margin: 0; }
button.rv-bad-on { background: var(--bad); color: #fff; border-color: var(--bad); font-weight: 700; }
button.subject { padding: 10px 6px; }
button.subject { margin: 0; text-align: center; font-weight: 700; }
button.subject.on { background: var(--accent); color: var(--accent-fg); border-color: var(--accent); }
button:disabled { opacity: .45; cursor: default; box-shadow: none; }
/* cloze: the blank sits inside the sentence */
.sentence { font-size: 1.2rem; line-height: 2.1; margin: 0 0 14px; overflow-wrap: anywhere; }
.blank { display: inline-block; min-width: 4.5em; border-bottom: 3px dotted var(--accent); line-height: 1.2; }
input.blank-input { display: inline-block; width: 9em; max-width: 100%; min-height: 48px; padding: 6px 10px; font-size: 1.15rem; vertical-align: middle; }
.sentence.blanks input.blank-input { width: 3.6em; margin: 2px 2px; text-align: center; }
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
/* ---- design of 2026-10-17: home, subject colours, lesson path, streak, stars, badges ---- */
.hello { margin: 4px 0 12px; } .hello h1 { font-size: 1.5rem; }
.pills { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin: 0 0 8px; }
.pill { display: flex; flex-direction: column; align-items: center; padding: 10px 4px; border-radius: 14px; background: var(--card); border: 1px solid var(--line); }
.pill strong { font-size: 1.4rem; line-height: 1.1; } .pill span:last-child { font-size: .8rem; color: var(--muted); } .pill-icon { font-size: 1.2rem; }
.streak-note { text-align: center; }
button.continue { background: var(--subj, var(--accent)); border-color: var(--subj, var(--accent)); color: #fff; box-shadow: 0 3px 0 rgba(0,0,0,.25); }
.tiles-subjects { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 14px 0 6px; }
button.tile-subject { margin: 0; display: flex; flex-direction: column; align-items: flex-start; gap: 4px; min-height: 112px; padding: 12px;
  border: 2px solid var(--subj); border-radius: 16px; background: var(--card); background: color-mix(in srgb, var(--subj) 12%, var(--card)); }
button.tile-subject:active { transform: scale(.96); }
.ts-icon { font-size: 1.8rem; line-height: 1; } .ts-name { font-weight: 800; line-height: 1.2; } .ts-count { font-size: .85rem; color: var(--muted); }
.ts-bar { display: block; width: 100%; height: 8px; border-radius: 4px; background: var(--track); overflow: hidden; margin-top: auto; }
.ts-bar span { display: block; height: 100%; background: var(--subj); border-radius: 4px; }
button.tile-subject.complete .ts-count { color: var(--subj); font-weight: 700; }
button.badges-link { text-align: center; font-weight: 700; margin-top: 14px; }
.badges { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 14px; }
.badge-card { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 2px; padding: 14px 8px; border-radius: 16px;
  border: 1px dashed var(--line); background: var(--soft); opacity: .75; }
.badge-card.got { opacity: 1; border: 2px solid #e0a526; background: var(--card); }
.badge-card .b-icon { font-size: 2rem; } .badge-card .muted { font-size: .8rem; }
.subject-head { display: flex; gap: 12px; align-items: center; margin: 4px 0 12px; } .sh-icon { font-size: 2.4rem; line-height: 1; }
.subject-page .progress .fill { background: var(--subj); }
button.link.back { text-align: left; margin: 0 0 6px; padding-left: 0; }
.path { list-style: none; padding: 0; margin: 14px 0; position: relative; }
.path::before { content: ""; position: absolute; left: 25px; top: 18px; bottom: 18px; width: 4px; border-radius: 2px; background: var(--track); }
.path .step { position: relative; }
.path button.reset { display: block; min-height: 36px; margin: -4px 0 6px 58px; padding: 4px 8px; font-size: .9rem; text-align: left; }
.path button.lesson .mark { position: relative; z-index: 1; width: 40px; height: 40px; border: 3px solid var(--subj); background: var(--card); color: var(--subj); }
.path .is-done button.lesson .mark { background: var(--subj); color: #fff; }
.path .is-next button.lesson { border: 2px solid var(--subj); background: color-mix(in srgb, var(--subj) 10%, var(--card)); }
.path .is-next button.lesson .mark { animation: pulse 1.6s ease-in-out infinite; }
@keyframes pulse { 0%, 100% { box-shadow: 0 0 0 0 color-mix(in srgb, var(--subj) 45%, transparent); } 50% { box-shadow: 0 0 0 8px transparent; } }
.done-stars { display: flex; justify-content: center; gap: 10px; margin: 10px 0; }
.done-stars .star { font-size: 2.6rem; color: var(--track); animation: starpop 420ms cubic-bezier(.2,.9,.3,1.4) calc(var(--k) * 180ms) both; }
.done-stars .star.on { color: #e0a526; }
@keyframes starpop { from { transform: scale(0) rotate(-40deg); opacity: 0; } to { transform: none; opacity: 1; } }
.done-streak { font-weight: 700; }
.new-badge { display: flex; gap: 10px; align-items: center; justify-content: center; padding: 10px; margin: 8px 0; border-radius: 14px;
  border: 2px solid #e0a526; background: var(--card); animation: starpop 420ms ease-out 700ms both; } .new-badge span { font-size: 1.6rem; }
a.button-link { display: block; min-height: 48px; margin: 10px 0 0; padding: 12px 14px; border-radius: 12px; border: 1px solid var(--line);
  background: var(--card); color: var(--fg); text-align: center; text-decoration: none; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
  .confetti { display: none; }
  button:active, button.primary:active { transform: none; }
}
`;

const ENGINE_LIBS = `{ libs: { maths: __mods["lib/maths.js"], english: { ...__mods["lib/maths.js"], ...__mods["lib/english.js"] },
    "f2-maths": { ...__mods["lib/maths.js"], ...__mods["lib/maths2.js"] }, "f2-english": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"] },
    
    "f2-francais-intensif": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"], ...__mods["lib/biology.js"], ...__mods["lib/computerscience.js"], ...__mods["lib/french.js"], ...__mods["lib/french2.js"] },
    "f2-french": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"], ...__mods["lib/biology.js"], ...__mods["lib/computerscience.js"], ...__mods["lib/french.js"], ...__mods["lib/french2.js"] },
    "f2-home-economics": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"], ...__mods["lib/biology.js"], ...__mods["lib/computerscience.js"], ...__mods["lib/maths2.js"], ...__mods["lib/science2.js"] }, "f2-geography": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"], ...__mods["lib/biology.js"], ...__mods["lib/computerscience.js"], ...__mods["lib/maths2.js"], ...__mods["lib/science2.js"] }, "f2-history": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"], ...__mods["lib/biology.js"], ...__mods["lib/computerscience.js"], ...__mods["lib/maths2.js"], ...__mods["lib/science2.js"] }, "f2-computer-science": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"], ...__mods["lib/biology.js"], ...__mods["lib/computerscience.js"], ...__mods["lib/maths2.js"], ...__mods["lib/science2.js"] }, "f2-accounting": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"], ...__mods["lib/biology.js"], ...__mods["lib/computerscience.js"], ...__mods["lib/maths2.js"], ...__mods["lib/science2.js"] },
    "f2-physics": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/biology.js"], ...__mods["lib/maths2.js"], ...__mods["lib/science2.js"] }, "f2-chemistry": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/biology.js"], ...__mods["lib/maths2.js"], ...__mods["lib/science2.js"] }, "f2-biology": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/biology.js"], ...__mods["lib/maths2.js"], ...__mods["lib/science2.js"] },
    physics: { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"] },
    chemistry: { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"] },
    geography: { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"] },
    "home-economics": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"] },
    history: { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"] },
    biology: { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"], ...__mods["lib/biology.js"] },
    "computer-science": { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"], ...__mods["lib/biology.js"], ...__mods["lib/computerscience.js"] },
    french: { ...__mods["lib/maths.js"], ...__mods["lib/english.js"], ...__mods["lib/physics.js"], ...__mods["lib/chemistry.js"], ...__mods["lib/geography.js"], ...__mods["lib/homeeconomics.js"], ...__mods["lib/history.js"], ...__mods["lib/biology.js"], ...__mods["lib/computerscience.js"], ...__mods["lib/french.js"] } }`;
const paper = Object.fromEntries(Object.entries(content).map(([s, ls]) => [s, Object.values(ls).filter((l) => l.paper_task).map((l) => l.lesson_no)]));
// Each page bundles only the libraries its subjects use, and the libraries those import (2026-10-21): a class's
// shareable file must not grow when another class adds a library (Form One's file stays as it was).
const LIB_ENTRIES = Object.fromEntries([...ENGINE_LIBS.matchAll(/(?:"([a-z0-9-]+)"|\b([a-z][a-z0-9]*)): (\{[^{}]*\}|__mods\["[^"]+"\])/g)]
  .map((m) => [m[1] || m[2], m[3]]).filter(([k]) => k !== "libs"));
function libsFor(only) {
  const need = new Set(only.flatMap((s) => [...(LIB_ENTRIES[s] || "").matchAll(/lib\/[a-z0-9]+\.js/g)].map((m) => m[0])));
  for (let grew = true; grew;) {
    grew = false;
    for (const p of [...need]) for (const m of read(`src/engine/${p}`).matchAll(/from "\.\/([a-z0-9]+\.js)"/g)) if (!need.has(`lib/${m[1]}`)) { need.add(`lib/${m[1]}`); grew = true; }
  }
  return need;
}
const engineFor = (only) => { const need = libsFor(only); return ENGINE.filter((p) => !p.startsWith("lib/") || need.has(p)); };
const engineLibsFor = (only) => `{ libs: { ${only.map((s) => {
  if (!LIB_ENTRIES[s]) throw new Error(`no library list for ${s}`);
  return `${JSON.stringify(s)}: ${LIB_ENTRIES[s]}`;
}).join(", ")} }`;
// `only`: the subjects a page carries (the single shareable file holds one class, so it stays small enough for
// Bluetooth); the installable app's core page lists every subject and loads their lessons one at a time.
const pick = (obj, only) => Object.fromEntries(Object.entries(obj).filter(([s]) => only.includes(s)));
const page = ({ mode, contentJs, only = Object.keys(SUBJECTS), head = "", tail = "", versions = {}, term = null, lessonsJs = safeJson(pick(lessons, only)) }) => `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#1f6f4a">
<title>${only.every((s) => CLASS_OF[s] === "form-2") ? "Form Two Lessons" : "Form One Lessons"}${term ? ` · Term ${term}` : ""}</title>
${head}<style>${css}</style>
</head>
<body>
<main id="app"><noscript>This page needs JavaScript.</noscript></main>
<script>
"use strict";
const __mods = {};
${engineFor(only).map(bundleModule).join("\n")}
const ENGINE = ${engineLibsFor(only)},
  template: __mods["template.js"], teach: __mods["teach.js"], readiness: __mods["readiness.js"] };
const CONTENT = ${contentJs};
const TITLES = ${safeJson(pick(titles, only))};
const LESSONS = ${lessonsJs};
const SUBJECTS = ${safeJson(pick(SUBJECTS, only))};
const CLASSES = ${safeJson(CLASSES)};
const CLASS_OF = ${safeJson(pick(CLASS_OF, only))};
const PAPER = ${safeJson(pick(paper, only))};
const MODE = ${JSON.stringify(mode)};
const BUILD = ${JSON.stringify(build)};
const VERSIONS = ${safeJson(versions)};
const SHARE = ${safeJson(mode === "pwa" ? share : {})};
const TERM = ${JSON.stringify(term)};
${read("tools/prototype/app.js")}
${read("tools/prototype/review.js")}
</script>
${tail}</body>
</html>
`;
// Shareable files (Bluetooth, flash drive): Form One is one file, form1.html, as before. From Form Two a whole year
// does not fit in one file, so there is one file per term (2026-10-21): form2-term-1.html, form2-term-2.html …
// Lesson numbers are the same in every file, so progress carries over in the installable app.
const ofClass = (c) => Object.keys(SUBJECTS).filter((s) => CLASS_OF[s] === c);
const termsOf = (c) => [...new Set(ofClass(c).flatMap((s) => lessons[s].map((n) => termOf[s][n])))].sort();
// The single-file page of some subjects of a class, for one term (term null: every lesson, as for Form One).
const singlePage = (only, term) => {
  const inTerm = (s) => lessons[s].filter((n) => term === null || termOf[s][n] === term);
  return page({ mode: "single", only, term, lessonsJs: safeJson(Object.fromEntries(only.map((s) => [s, inTerm(s)]))),
    contentJs: safeJson(Object.fromEntries(only.map((s) => [s, Object.fromEntries(inTerm(s).map((n) => [n, content[s][n]]))]))) });
};
const fits = (html) => Buffer.byteLength(html, "utf8") <= MAX_BYTES;
// A term that does not fit in one file is split into parts of whole subjects, halving until every part fits (2026-10-21).
function termParts(c, term) {
  const go = (subs) => {
    const html = singlePage(subs, term);
    if (fits(html)) return [{ subs, html }];
    if (subs.length === 1) throw new Error(`${c} term ${term}: ${subs[0]} alone is over the ${MAX_BYTES} limit`);
    const h = Math.ceil(subs.length / 2);
    return [...go(subs.slice(0, h)), ...go(subs.slice(h))];
  };
  const parts = go(ofClass(c).filter((s) => lessons[s].some((n) => termOf[s][n] === term)));
  return parts.map((p, i) => ({ ...p, c, term, part: parts.length > 1 ? i + 1 : null,
    file: `offline-${c}-term-${term}${parts.length > 1 ? `-part-${i + 1}` : ""}.html`,
    local: `${c.replace("-", "")}-term-${term}${parts.length > 1 ? `-part-${i + 1}` : ""}.html` }));
}
const html = singlePage(ofClass("form-1"), null);
if (!fits(html)) throw new Error(`form-1 single file is ${Buffer.byteLength(html, "utf8")} bytes, over the ${MAX_BYTES} limit`);
console.log(`form-1: one file of ${(Buffer.byteLength(html, "utf8") / 1024).toFixed(1)} KB (limit ${MAX_BYTES / 1024} KB)`);
writeFileSync(new URL("tools/prototype/form1.html", ROOT), html, "utf8");
const termFiles = Object.keys(CLASSES).filter((c) => c !== "form-1" && ofClass(c).length).flatMap((c) => termsOf(c).flatMap((t) => termParts(c, t)));
for (const f of readdirSync(new URL("tools/prototype/", ROOT))) if (/^form\d-term-.*\.html$/.test(f)) rmSync(new URL(`tools/prototype/${f}`, ROOT));  // stale term files
for (const f of termFiles) {
  writeFileSync(new URL(`tools/prototype/${f.local}`, ROOT), f.html, "utf8");
  console.log(`${f.c} term ${f.term}${f.part ? ` part ${f.part}` : ""}: one file of ${(Buffer.byteLength(f.html, "utf8") / 1024).toFixed(1)} KB (${f.subs.length} subjects)`);
}
const share = { "form-1": [{ file: "offline.html" }],
  ...Object.fromEntries(Object.keys(CLASSES).filter((c) => c !== "form-1" && ofClass(c).length)
    .map((c) => [c, termFiles.filter((f) => f.c === c).map((f) => ({ term: f.term, part: f.part, subjects: f.subs.map((s) => SUBJECTS[s]), file: f.file }))])) };
console.log(`wrote tools/prototype/form1.html${termFiles.map((f) => `, ${f.local}`).join("")}`);

// ---- the installable app (2026-10-17): tools/prototype/pwa/ → published as the site's root
const PWA = new URL("tools/prototype/pwa/", ROOT);
rmSync(PWA, { recursive: true, force: true });
mkdirSync(new URL("subjects/", PWA), { recursive: true });
mkdirSync(new URL("icons/", PWA), { recursive: true });
// Each subject file is named by a fingerprint of its own content (2026-10-19; before, by the build date, so two
// updates on the same day kept the same name and a phone could reuse the old lessons until the next opening).
// A changed subject gets a new address and is fetched on the first opening; an unchanged one stays saved.
const fingerprint = (text) => createHash("sha256").update(text).digest("hex").slice(0, 12);
const subjectJs = Object.fromEntries(Object.keys(SUBJECTS).map((s) => [s, `CONTENT[${JSON.stringify(s)}] = ${safeJson(content[s])};\n`]));
const versions = Object.fromEntries(Object.entries(subjectJs).map(([s, js]) => [s, fingerprint(js)]));
const register = `<script>if ("serviceWorker" in navigator) addEventListener("load", () => navigator.serviceWorker.register("sw.js"));</script>\n`;
const shell = page({ mode: "pwa", contentJs: "{}", tail: register, versions,
  head: `<link rel="manifest" href="manifest.webmanifest">\n<link rel="icon" href="icons/icon-192.png">\n<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">\n` });
const shellBytes = Buffer.byteLength(shell, "utf8");
if (shellBytes > SHELL_MAX) throw new Error(`app core is ${shellBytes} bytes, over the ${SHELL_MAX} limit`);
writeFileSync(new URL("index.html", PWA), shell, "utf8");
const sizes = {};
for (const [s, js] of Object.entries(subjectJs)) {
  writeFileSync(new URL(`subjects/${s}.js`, PWA), js, "utf8");
  sizes[s] = Buffer.byteLength(js, "utf8");
}
writeFileSync(new URL("offline.html", PWA), html, "utf8");
for (const f of termFiles) writeFileSync(new URL(f.file, PWA), f.html, "utf8");
for (const f of ["icon-192.png", "icon-512.png", "maskable-192.png", "maskable-512.png", "apple-touch-icon.png"]) copyFileSync(new URL(`tools/prototype/icons/${f}`, ROOT), new URL(`icons/${f}`, PWA));
writeFileSync(new URL("manifest.webmanifest", PWA), JSON.stringify({
  name: "Psalms Preps: Form One lessons", short_name: "Form One", description: "Form One lessons that work offline: Maths, English, sciences, humanities and French.",
  start_url: "./", scope: "./", display: "standalone", orientation: "portrait", background_color: "#fbfaf7", theme_color: "#1f6f4a",
  icons: [
    { src: "icons/icon-192.png", sizes: "192x192", type: "image/png", purpose: "any" }, { src: "icons/icon-512.png", sizes: "512x512", type: "image/png", purpose: "any" },
    { src: "icons/maskable-192.png", sizes: "192x192", type: "image/png", purpose: "maskable" }, { src: "icons/maskable-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
  ],
}, null, 2), "utf8");
// The service worker keeps the app working offline. The core page is checked online first (so updates arrive) and
// falls back to the saved copy; subject files are versioned by build and served from the phone once saved.
// On an update, the subjects already saved are fetched again in their new version, so they stay offline.
writeFileSync(new URL("sw.js", PWA), `// Psalms Preps service worker, build ${build} (generated by tools/prototype/build.mjs)
const CACHE = "psalmspreps-${build}-${fingerprint(shell)}";
const VERSIONS = ${JSON.stringify(versions)};
const SHELL = ["./", "manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png", "icons/maskable-192.png", "icons/apple-touch-icon.png"];
self.addEventListener("install", (e) => { e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener("activate", (e) => { e.waitUntil((async () => {
  const keep = await caches.open(CACHE);
  for (const name of await caches.keys()) {
    if (name === CACHE) continue;
    const old = await caches.open(name);
    for (const req of await old.keys()) {
      const m = new URL(req.url).pathname.match(/subjects\\/([a-z0-9-]+)\\.js$/);
      if (m && VERSIONS[m[1]]) try { await keep.add(\`subjects/\${m[1]}.js?v=\${VERSIONS[m[1]]}\`); } catch { /* offline now: fetched again when opened */ }
    }
    await caches.delete(name);
  }
  await self.clients.claim();
})()); });
self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET" || new URL(req.url).origin !== location.origin) return;
  if (req.mode === "navigate") {
    e.respondWith(fetch(req).then((res) => { const copy = res.clone(); caches.open(CACHE).then((c) => c.put("./", copy)); return res; })
      .catch(() => caches.match("./")));
    return;
  }
  e.respondWith(caches.match(req).then((hit) => hit || fetch(req).then((res) => {
    if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); }
    return res;
  })));
});
`, "utf8");
console.log(`wrote tools/prototype/pwa/ (core ${(shellBytes / 1024).toFixed(1)} KB, limit ${SHELL_MAX / 1024} KB; subjects ${Object.entries(sizes).map(([s, b]) => `${s} ${(b / 1024).toFixed(0)} KB`).join(", ")})`);
