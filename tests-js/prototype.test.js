// The prototype (readiness + Maths 1–16 + English E1 + Physics P1 + Chemistry C1 + Geography G1 + Home Economics H1 + History Y1 + Biology L1 + Computer Science S1 + French F1) builds from the real engine and content, offline, under 1.5 MB.
// Form 2 (2026-10-17, form-2 branch): one shareable file per term, form2-term-1.html …; the installable app has both classes.
import { createHash } from "node:crypto";
import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";

const ROOT = new URL("../", import.meta.url);
const FILE = new URL("tools/prototype/form1.html", ROOT);
const page = () => readFileSync(FILE, "utf8");
const constant = (html, name) => JSON.parse(html.match(new RegExp(`const ${name} = (.*);\\n`))[1]);
const FORM1 = ["maths", "english", "physics", "chemistry", "geography", "home-economics", "history", "biology", "computer-science", "french"];
// Form 3 on: content/classes.json, the subjects with at least one lesson (2026-10-23)
const LATER = (await import("../tools/classes.mjs")).registrySubjects().filter((r) => r.lessons.length);
const FORM2 = ["f2-maths", "f2-english", "f2-physics", "f2-chemistry", "f2-geography", "f2-home-economics", "f2-history", "f2-biology", "f2-computer-science", "f2-french", "f2-francais-intensif", "f2-accounting"];

test("prototype: builds under 1.5 MB, no external resources, engine runs", () => {
  execFileSync(process.execPath, [new URL("tools/prototype/build.mjs", ROOT).pathname.replace(/^\/([A-Za-z]:)/, "$1")]);
  const html = page();
  assert.ok(Buffer.byteLength(html) < 1500 * 1024, `${Buffer.byteLength(html)} bytes`);
  assert.doesNotMatch(html, /<script[^>]+src=|<link[^>]+href=|https?:\/\/(?!www\.w3\.org)/, "must not load anything from the network");
  assert.doesNotMatch(html, /indexedDB|fetch\(|XMLHttpRequest|sendBeacon|WebSocket/, "must not send data");
  // Progress is saved in this browser only (2026-10-05): one key, every access wrapped in try/catch.
  const uses = html.match(/localStorage\.\w+\([^)]*\)/g) || [];
  assert.ok(uses.length >= 2, "saves and loads progress");
  // Teacher review mode keeps its marks under its own key (2026-10-17).
  for (const u of uses) assert.match(u, /^localStorage\.(getItem|setItem|removeItem)\((KEY(, JSON\.stringify\(state)?|REVIEW_KEY(, JSON\.stringify\(review)?)\)$/, u);
  // Run the inlined engine (everything before the content) and build the readiness check with it.
  const script = html.split("<script>")[1].split("const CONTENT")[0];
  const ENGINE = new Function(`${script}; return ENGINE;`)();
  const l0 = JSON.parse(readFileSync(new URL("content/maths/0.json", ROOT), "utf8"));
  const qs = ENGINE.readiness.buildReadiness(l0, 3, ENGINE.libs.maths);
  assert.equal(qs.length, l0.readiness.items.length);
  assert.ok(qs.length <= l0.readiness.max_questions);
  assert.ok(qs.every((q) => q.verified));
  // English questions build with the inlined English library.
  const e3 = JSON.parse(readFileSync(new URL("content/english/3.json", ROOT), "utf8"));
  const q = ENGINE.template.instantiate(e3.questions.find((t) => t.id === "e3-form"), 5, ENGINE.libs.english, 3);
  assert.deepEqual(ENGINE.template.check(q, q.answer), { correct: true });
  // Physics questions build with the inlined Physics library, drawings included.
  const p16 = JSON.parse(readFileSync(new URL("content/physics/16.json", ROOT), "utf8"));
  const pq = ENGINE.template.instantiate(p16.questions.find((t) => t.id === "p16-cyl"), 5, ENGINE.libs.physics, 16);
  assert.match(pq.figure, /^<svg /);
  assert.deepEqual(ENGINE.template.check(pq, pq.answer), { correct: true });
  // Chemistry: atom counts come from the inlined formula parser.
  const c20 = JSON.parse(readFileSync(new URL("content/chemistry/20.json", ROOT), "utf8"));
  const cq = ENGINE.template.instantiate(c20.questions.find((t) => t.id === "ch20-count"), 5, ENGINE.libs.chemistry, 20);
  assert.deepEqual(ENGINE.template.check(cq, cq.answer), { correct: true });
  // Geography: grid maps are drawn and local times computed by the inlined library.
  const g5 = JSON.parse(readFileSync(new URL("content/geography/5.json", ROOT), "utf8"));
  const gq = ENGINE.template.instantiate(g5.questions.find((t) => t.id === "g5-four"), 5, ENGINE.libs.geography, 5);
  assert.match(gq.figure, /^<svg /);
  assert.deepEqual(ENGINE.template.check(gq, gq.answer), { correct: true });
  // Home Economics: the work triangle is drawn and totalled by the inlined library.
  const h13 = JSON.parse(readFileSync(new URL("content/home-economics/13.json", ROOT), "utf8"));
  const hq = ENGINE.template.instantiate(h13.questions.find((t) => t.id === "he13-total"), 5, ENGINE.libs["home-economics"], 13);
  assert.match(hq.figure, /^<svg /);
  assert.deepEqual(ENGINE.template.check(hq, hq.answer), { correct: true });
  // History, Biology, Computer Science: dates, magnification and patterns come from the inlined libraries.
  for (const [s, n, id] of [["history", 3, "hi3-across"], ["biology", 7, "b7-mag"], ["computer-science", 9, "cs9-shape"], ["french", 15, "f15-poss"]]) {
    const l = JSON.parse(readFileSync(new URL(`content/${s}/${n}.json`, ROOT), "utf8"));
    const x = ENGINE.template.instantiate(l.questions.find((t) => t.id === id), 5, ENGINE.libs[s], n);
    assert.equal(x.verified, true, id);
  }
});

test("prototype: Maths 1–16, English E1, Physics P1, Chemistry C1, Geography G1, Home Economics H1, History Y1, Biology L1, Computer Science S1 and French F1 are in the page; deferred speech work is not", () => {
  const html = page();
  const content = constant(html, "CONTENT"), titles = constant(html, "TITLES"), lessons = constant(html, "LESSONS");
  assert.deepEqual(lessons.maths, Array.from({ length: 16 }, (_, i) => i + 1));
  assert.deepEqual(lessons.english, [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16]);
  assert.deepEqual(lessons.physics, Array.from({ length: 19 }, (_, i) => i + 1));
  assert.deepEqual(lessons.chemistry, Array.from({ length: 21 }, (_, i) => i + 1));
  assert.deepEqual(lessons.geography, Array.from({ length: 10 }, (_, i) => i + 1));
  assert.match(titles.geography[4], /^PW1/, "Geography is numbered by place in the year: Lesson 4 is PW1");
  assert.deepEqual(lessons["home-economics"], [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21]);
  assert.deepEqual(lessons.history, Array.from({ length: 10 }, (_, i) => i + 1));
  assert.deepEqual(lessons.biology, [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21]);
  assert.deepEqual(lessons["computer-science"], [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 16, 17, 18]);
  assert.deepEqual(lessons.french, Array.from({ length: 15 }, (_, i) => i + 1));
  for (const s of ["maths", "english", "physics", "chemistry", "geography", "home-economics", "history", "biology", "computer-science", "french"]) for (const n of lessons[s]) {
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
  // the app opens on the lesson menu; the readiness check is offered on the Maths tab only, until done (2026-10-07)
  // (since 2026-10-17 the last line also sends teachers with ?review to the review list)
  // (since 2026-10-17 pupils start on the home screen: streak, stars, one tile per subject)
  assert.match(html, /\nif \(new URLSearchParams\(location\.search\)\.has\("review"\)\) reviewHome\(\); else home\(\);\s*<\/script>/);
  // (since 2026-10-24 also when the saved check was skipped through: readinessValidity)
  assert.match(html, /const check = s === "maths" && \(!state\.readiness \|\| !readiness\.readinessValidity\(state\.readiness\.rows\)\.valid\);/);
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

test("prototype: inside French lessons the pupil's labels are French; elsewhere English", () => {
  const html = page();
  assert.ok(html.includes("const T = (text, v = {}) => ((inFrench(S) && FR[text]) || text)"), "the label helper is in the page");
  const inFrench = new Function(`${html.match(/const inFrench = [^;\n]*;/)[0]} return inFrench;`)();
  for (const s of ["french", "f2-french", "f2-francais-intensif", "f3-french", "f3-francais-intensif", "l6-french", "u6-francais-intensif"]) assert.ok(inFrench(s), `${s} uses the French labels`);
  for (const s of ["maths", "f2-english", "f3-physics", "frenchy"]) assert.ok(!inFrench(s), `${s} stays English`);
  for (const fr of ["Vérifier", "Je ne sais pas", "Retour aux leçons", "Leçon {n} · Idée {a} sur {b}", "Bravo !"]) assert.ok(html.includes(fr), fr);
  for (const en of ['button("Check"', "button(\"I don't know\"", '{}, "Correct!")']) assert.ok(!html.includes(en), `still hard-coded: ${en}`);
});

test("prototype: every answer screen has a way back to the lessons", () => {
  const html = page();
  for (const t of ['button(T("Next"), go(next), "primary"), toMenu());', 'workingBox(T("Here is how to do this one"), q, list), tail, toMenu());',
    'again(like ? [q, like] : q), toMenu());', 'button(T("Continue"), () => lesson(teach.nextPhase(flow)), "primary"), toMenu());']) assert.ok(html.includes(t), t);
});

test("prototype: a finished or started lesson can be reset after a confirmation", () => {
  const html = page();
  assert.ok(html.includes("function resetLesson(s, n)"), "the reset helper is in the page");
  assert.ok(html.includes("Your stars and saved answers for this lesson will be cleared."), "the pupil is asked to confirm");
  assert.ok(html.includes("delete state.lessons[lessonKey(s, n)];") && html.includes("if (state.current[s]?.lesson === n) delete state.current[s];"), "only that lesson's record and flow are cleared");
  assert.ok(html.includes('r?.done || going ? el("button", { type: "button", class: "link reset"'), "the link shows only on finished or started lessons");
});

test("prototype: teacher review mode opens with ?review, shows answers and builds the message from marks", () => {
  const html = page();
  assert.ok(html.includes('if (new URLSearchParams(location.search).has("review")) reviewHome(); else home();'), "start-up chooses review or home");
  for (const t of ["Teacher review", "✓ OK", "✗ Problem", "Send my review", "Answer written by a person: please check it."]) assert.ok(html.includes(t), t);
});

// ---- the installable app (2026-10-17): a small core page, one file per subject, a service worker, a manifest
const PWA = new URL("tools/prototype/pwa/", ROOT);
const pwaFile = (p) => readFileSync(new URL(p, PWA), "utf8");

test("installable app: the core page has the engine and screens but no lesson content, and registers the service worker", () => {
  const core = pwaFile("index.html");
  assert.ok(Buffer.byteLength(core) < 400 * 1024, `${Buffer.byteLength(core)} bytes`);
  assert.match(core, /const CONTENT = \{\};/);
  assert.match(core, /const MODE = "pwa";/);
  assert.match(core, /<link rel="manifest" href="manifest\.webmanifest">/);
  assert.match(core, /navigator\.serviceWorker\.register\("sw\.js"\)/);
  assert.doesNotMatch(core, /"worked_example":{/, "no lesson content in the core page");
  assert.doesNotMatch(core, /__mods\["lib\//, "no subject library in the core page (2026-10-23)");
  assert.doesNotMatch(core, /https?:\/\/(?!www\.w3\.org)/, "loads nothing from other sites");
  const lessons = constant(core, "LESSONS"), titles = constant(core, "TITLES");
  assert.deepEqual(Object.keys(lessons), [...FORM1, ...FORM2, ...LATER.map((r) => r.id)]);
  for (const s of Object.keys(lessons)) for (const n of lessons[s]) assert.ok(titles[s][n], `${s} ${n} title in the core page`);
});

test("installable app: one file per subject defines exactly that subject's lessons", () => {
  const core = pwaFile("index.html"), lessons = constant(core, "LESSONS");
  for (const s of Object.keys(lessons)) {
    const js = pwaFile(`subjects/${s}.js`);
    // the libraries the subject uses (2026-10-23: not in the core page), then its lessons
    const m = js.match(/\nCONTENT\[("[a-z0-9-]+")\] = (.*);\n$/s);
    assert.ok(m, `${s}: subject file format`);
    assert.ok(js.includes(`ENGINE.libs[${JSON.stringify(s)}] = `), `${s}: sets its library`);
    assert.match(js, /^if \(!__mods\["lib\/maths\.js"\]\) __mods\["lib\/maths\.js"\] = /, `${s}: maths library first`);
    assert.equal(JSON.parse(m[1]), s);
    const content = JSON.parse(m[2]);
    for (const n of lessons[s]) assert.equal(content[n]?.lesson_no, n, `${s} ${n}`);
  }
});

test("installable app: manifest, icons, service worker and the shareable single file", () => {
  const manifest = JSON.parse(pwaFile("manifest.webmanifest"));
  assert.equal(manifest.display, "standalone");
  assert.equal(manifest.start_url, "./");
  for (const icon of manifest.icons) assert.ok(readFileSync(new URL(icon.src, PWA)).length > 500, icon.src);
  assert.ok(manifest.icons.some((i) => i.sizes === "512x512" && i.purpose === "any") && manifest.icons.some((i) => i.purpose === "maskable"));
  const sw = pwaFile("sw.js");
  for (const part of ['addEventListener("install"', 'addEventListener("activate"', 'addEventListener("fetch"', 'req.mode === "navigate"', "caches.match"]) assert.ok(sw.includes(part), part);
  assert.equal(pwaFile("offline.html"), page(), "the shareable file is the single-file app");
  assert.equal(pwaFile("offline-form-2-term-1.html"), readFileSync(new URL("tools/prototype/form2-term-1.html", ROOT), "utf8"), "Form Two has its own shareable file");
  assert.ok(sw.includes(String.raw`subjects\/([a-z0-9-]+)\.js$`),"saved subjects are fetched again after an update, Form 2 ids (f2-maths) included");
});

test("installable app: each subject file is addressed by its content fingerprint, so changed lessons arrive at once", () => {
  const core = pwaFile("index.html"), sw = pwaFile("sw.js"), versions = constant(core, "VERSIONS");
  assert.deepEqual(Object.keys(versions), Object.keys(constant(core, "SUBJECTS")));
  const hash = (t) => createHash("sha256").update(t).digest("hex").slice(0, 12);
  for (const [s, v] of Object.entries(versions)) assert.equal(v, hash(pwaFile(`subjects/${s}.js`)), s);
  assert.ok(core.includes("tag.src = `subjects/${s}.js?v=${VERSIONS[s] || BUILD}`;"), "the app asks for the fingerprinted address");
  assert.ok(sw.includes(`const VERSIONS = ${JSON.stringify(versions)};`) && sw.includes("?v=${VERSIONS[m[1]]}"), "an update saves the new files again");
  assert.match(sw, /const CACHE = "psalmspreps-\d{4}-\d{2}-\d{2}-[0-9a-f]{12}";/, "a new core page gives a new cache, even on the same day");
});

test("design: home with streak, stars and subject tiles; lesson path; forgiving streak; stars and badges at the end", () => {
  const html = page();
  for (const t of ["function home()", "function badgesScreen()", "function streak()", "function starsOf(", "function newBadges()", 'class: "path"', "tile-subject", "Up to two days off won't break it."])
    assert.ok(html.includes(t), t);
  assert.match(html, /dayNum\(dayOf\(\)\) - days\[days\.length - 1\] > 3/, "a streak survives two days off");
  assert.match(html, /right >= 0\.8 \? 3 : right >= 0\.5 \? 2 : 1/, "stars from first tries");
  assert.match(html, /\.done-stars \.star \{[^}]*animation/);
});

test("installable app: the teacher review list works when only some subjects are on the phone", () => {
  const core = pwaFile("index.html");
  const text = core.slice(core.indexOf("function reviewText()"), core.indexOf("async function sendReview"));
  assert.match(text, /Object\.keys\(SUBJECTS\)\.filter\(\(x\) => CONTENT\[x\]\)/, "review text skips subjects not loaded yet (bug of 2026-10-17)");
  assert.match(core, /function reviewHome\(\) \{\r?\n  if \(!CONTENT\[RS\]\) return withSubject\(RS, reviewHome\);/);
  assert.match(core, /function reviewLesson\(s, n\) \{\r?\n  if \(!CONTENT\[s\]\) return withSubject\(s, \(\) => reviewLesson\(s, n\)\);/);
});

test("classes: Form One stays the default; Form Two has its own subjects, file and progress keys", () => {
  const one = page(), two = readFileSync(new URL("tools/prototype/form2-term-1.html", ROOT), "utf8"), core = pwaFile("index.html");
  assert.deepEqual(Object.keys(constant(one, "SUBJECTS")), FORM1, "the Form One file has only Form One");
  assert.deepEqual(Object.keys(constant(two, "SUBJECTS")), FORM2, "the Form Two file has only Form Two");
  assert.deepEqual(Object.keys(constant(two, "CONTENT")), FORM2);
  assert.ok(Buffer.byteLength(two) < 2048 * 1024, "Form Two file within the 2 MB budget");
  const classOf = constant(core, "CLASS_OF");
  for (const s of FORM1) assert.equal(classOf[s], "form-1");
  for (const s of FORM2) assert.equal(classOf[s], "form-2");
  for (const r of LATER) assert.equal(classOf[r.id], r.cls);
  assert.deepEqual(constant(core, "CLASSES"), { "form-1": "Form One", "form-2": "Form Two", ...Object.fromEntries(LATER.map((r) => [r.cls, r.className])) });
  const app = readFileSync(new URL("tools/prototype/app.js", ROOT), "utf8");
  assert.ok(app.includes("const form = () => (classesHere().includes(state.form) ? state.form : classesHere()[0]);"), "no saved class: the first class, Form One");
  assert.ok(app.includes('classesHere().length > 1 ? el("div", { class: "subjects class-switch"'), "the switch shows only when there are two classes");
  assert.ok(app.includes("const lessonKey = (subject, n) => `${subject}:${n}`;"), "progress is kept per subject id, so f2-maths:5 never mixes with maths:5");
});
