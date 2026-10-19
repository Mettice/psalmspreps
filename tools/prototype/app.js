// Pupil UI: home (streak, stars, one tile per subject) → a subject's lesson path → teach mode (cards, worked example,
// practice or a paper task, note) → results with stars and badges. Lesson 0 readiness is offered on the Maths path. Uses the real engine (inlined by build.mjs).
// Progress is saved in this browser only (localStorage, decisions 2026-10-05 and 2026-10-06); nothing is sent anywhere.
/* global ENGINE, CONTENT, TITLES, LESSONS, SUBJECTS, BUILD, VERSIONS, PAPER, MODE */
const { libs, template, teach, readiness } = ENGINE;
const { check, DONT_KNOW, renderWorked, normaliseInput, inputModeFor } = template;
const L0 = () => CONTENT.maths[0];  // Maths is loaded before the readiness check starts

// ---------------------------------------------------------------- saved progress (this browser only)
// v2 { readiness: {score, rows, at} | null, subject,
//      lessons: {"maths:3": {done, at, rows, review, paper?}}, current: {maths?: {lesson, flow, rows, paper?}, english?: …} }
// v1 (Maths only, 2026-10-05) had lessons keyed by number and one current lesson; it is upgraded in place.
const KEY = "psalmspreps-maths-v1";  // kept so existing progress survives the upgrade
const fresh = () => ({ v: 2, readiness: null, subject: "maths", lessons: {}, current: {} });
/** A saved lesson in progress is kept only if its flow is usable; a damaged one is dropped, never a blank page. */
const usable = (c) => c && c.flow && Array.isArray(c.flow.steps) && Array.isArray(c.rows) && Number.isInteger(c.lesson);
const cleanCurrent = (cur) => Object.fromEntries(Object.entries(cur || {}).filter(([, c]) => usable(c)));
function upgrade(s) {
  if (s.v === 2) return { ...fresh(), ...s, current: cleanCurrent(s.current) };
  if (s.v !== 1) return fresh();
  const lessons = Object.fromEntries(Object.entries(s.lessons || {}).map(([n, x]) => [`maths:${n}`, x]));
  return { ...fresh(), readiness: s.readiness || null, lessons, current: cleanCurrent({ maths: s.current }) };
}
function load() {
  try {
    const s = JSON.parse(localStorage.getItem(KEY));
    return s ? upgrade(s) : fresh();
  } catch { return fresh(); }  // private mode, blocked storage or a broken value: start fresh
}
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch { /* still works, just forgets */ } };
const state = load();
const newSeed = () => Math.floor(Math.random() * 1e6);  // a new set of numbers each time a lesson starts
const lessonKey = (subject, n) => `${subject}:${n}`;

const app = document.getElementById("app");
const el = (tag, attrs = {}, ...kids) => {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) k.startsWith("on") ? e.addEventListener(k.slice(2), v) : e.setAttribute(k, v);
  for (const k of kids.flat()) if (k != null) e.append(k.nodeType ? k : document.createTextNode(String(k)));
  return e;
};
/** Replaces the page. The wrapper is new each time, so its entrance animation replays (off under reduced motion). */
const screen = (...kids) => {
  app.replaceChildren(el("div", { class: "screen" }, ...kids.flat().filter((k) => k != null)));
  window.scrollTo(0, 0);
};
/** Replaces a node's children, skipping empty slots (a placed tile leaves null behind; it must not show as "null"). */
const fill = (node, kids) => node.replaceChildren(...kids.filter((k) => k != null));
const button = (label, onclick, cls = "") => el("button", { type: "button", class: cls, onclick }, label);
const para = (t, cls = "") => el("p", { class: cls }, t);
const lines = (text) => text.split("\n").map((l) => (l.trim() ? para(l) : null));
const header = (kicker, title) => el("header", {}, el("div", { class: "kicker" }, kicker), el("h1", {}, title));
/** Progress bar: a filled segment plus "2 / 13". */
const progress = (cur, total) => el("div", { class: "progress", role: "progressbar", "aria-valuemin": "0", "aria-valuemax": String(total), "aria-valuenow": String(cur) },
  el("div", { class: "track" }, el("div", { class: "fill", style: `width:${Math.round((100 * cur) / total)}%` })),
  el("span", { class: "count" }, `${cur} / ${total}`));
/** A drawing made by the engine from the question's own numbers (an SVG string from our library, never from input). */
const figureBox = (svg) => {
  if (!svg) return null;
  const box = el("div", { class: "figure" });
  box.innerHTML = svg;
  return box;
};
const checkIcon = () => {
  const ns = "http://www.w3.org/2000/svg";
  const svg = document.createElementNS(ns, "svg");
  svg.setAttribute("viewBox", "0 0 24 24"); svg.setAttribute("class", "tick"); svg.setAttribute("aria-hidden", "true");
  const path = document.createElementNS(ns, "path");
  path.setAttribute("d", "M5 12.5l4.5 4.5L19 7.5");
  svg.append(path);
  return svg;
};

// ---------------------------------------------------------------- French lessons are in French (TR-F12)
// Inside a French lesson the pupil's buttons and headings are in French; the menu and the grown-up text stay English.
const FR = {
  "Check": "Vérifier", "Your answer": "Ta réponse", "blank": "espace vide", "Tap the words below.": "Touche les mots ci-dessous.",
  "Tap a word to add it. Tap a word in your sentence to take it out.": "Touche un mot pour l’ajouter. Touche un mot de ta phrase pour l’enlever.",
  "Tap an item on the left, then its partner on the right. Tap a pair to undo it.": "Touche un élément à gauche, puis son partenaire à droite. Touche une paire pour l’annuler.",
  "Tap a word, then tap its group. Tap a word in a group to take it out.": "Touche un mot, puis touche son groupe. Touche un mot dans un groupe pour l’enlever.",
  "Tap the one that is wrong.": "Touche celle qui est fausse.", "Tap them in order.": "Touche-les dans l’ordre.", "Start again": "Recommencer",
  "I don't know": "Je ne sais pas", "Back to the lessons": "Retour aux leçons", "Worked example": "Exemple expliqué", "Answer: {a}": "Réponse : {a}",
  "Example": "Exemple", "Hint: ": "Indice : ", "Lesson {n} · Idea {a} of {b}": "Leçon {n} · Idée {a} sur {b}", "Lesson {n} · Practice {a} of {b}": "Leçon {n} · Exercice {a} sur {b}",
  "I'm ready for a question": "Je passe à la question", "A new question": "Une nouvelle question", "Quick check": "Petite vérification", "Level {a}": "Niveau {a}",
  "Correct!": "Bravo !", "Next": "Suivant", "Lesson {n} · Worked example": "Leçon {n} · Exemple expliqué", "Follow each step": "Suis chaque étape",
  "Now write": "Maintenant, écris", "Now practise": "À toi de t’exercer", "Lesson {n} · Summary": "Leçon {n} · Résumé", "Finish": "Terminer",
  "These are not right yet: {a}.": "Ce n’est pas encore juste pour : {a}.", "This one is not right yet: {a}.": "Ce n’est pas encore juste pour : {a}.",
  "That's fine. Let's look at it together.": "Ce n’est pas grave. Regardons ensemble.", "✗ Not quite": "✗ Pas tout à fait",
  "Look at the example again, then try a new question.": "Regarde encore l’exemple, puis essaie une nouvelle question.", "Let's try again": "Essayons encore",
  "Try a new question": "Essayer une nouvelle question", "Here are the right answers.": "Voici les bonnes réponses.", "The answer is: {a}": "La réponse est : {a}",
  "Here is how to do it": "Voici comment faire", "Full working": "La solution complète", "We will come back to this one later.": "Nous reviendrons sur cette question plus tard.",
  "Continue": "Continuer", "Lesson {n} done": "Leçon {n} terminée", "You completed {a} questions.": "Tu as répondu à {a} questions.",
  "Here is one like it": "En voici un pareil", "Here is how to do this one": "Voici comment faire celui-ci", "Show the next step": "Voir l’étape suivante",
  "Step by step": "Étape par étape", "Fill in each box, then check.": "Remplis chaque case, puis vérifie.", "Box {a}": "Case {a}",
  "Next: Lesson {a}": "Suivant : Leçon {a}", "🔥 {a}-day streak": "🔥 {a} jours d’affilée", "New badge: {a}": "Nouveau badge : {a}", "All subjects": "Toutes les matières", "You have done every {a} lesson. Well done!": "Tu as fini toutes les leçons de français. Bravo !",
};
/** A label for the pupil: in French inside a French lesson, otherwise English. {x} are filled from v. */
const T = (text, v = {}) => ((S === "french" && FR[text]) || text).replace(/\{(\w)\}/g, (_, k) => v[k]);

// ---------------------------------------------------------------- one question, any type
/** A typed answer box (numbers or words): Enter or "Check" submits; the engine picks the keyboard. */
function answerBox(q, finish, inline = false) {
  const input = el("input", { type: "text", inputmode: inputModeFor(q), autocomplete: "off", autocorrect: "off", autocapitalize: "off",
    spellcheck: "false", "aria-label": T("Your answer"), class: inline ? "blank-input" : "" });
  const go = () => { const v = normaliseInput(input.value, q); if (v) finish(v); };
  input.addEventListener("keydown", (e) => e.key === "Enter" && go());
  setTimeout(() => input.focus(), 50);
  return { input, check: button(T("Check"), go, "primary") };
}

/** Cloze: the sentence with its blank inline. Typed: a box in the gap. Choose: a dotted gap, options below. */
function clozeSentence(q, box = null) {
  const [before, after] = q.sentence.split("___");
  return el("div", { class: "sentence" }, before, box || el("span", { class: "blank", "aria-label": "blank" }, " "), after);
}

/** Word order: tap a word to place it; tap a placed word to send it back. The final . ? or ! is fixed. */
function wordOrder(q, finish) {
  const placed = [];
  const line = el("div", { class: "built", "aria-live": "polite" });
  const pool = el("div", { class: "tiles" });
  const done = button(T("Check"), () => placed.length === q.items.length && finish([...placed]), "primary");
  const redraw = () => {
    line.replaceChildren(...(placed.length
      ? [...placed.map((i, k) => button(q.items[i], () => { placed.splice(k, 1); redraw(); }, "tile placed")), ...(q.end ? [el("span", { class: "end" }, q.end)] : [])]
      : [el("span", { class: "muted" }, T("Tap the words below."))]));
    fill(pool, q.items.map((t, i) => (placed.includes(i) ? null : button(t, () => { placed.push(i); redraw(); }, "tile"))));
    done.disabled = placed.length !== q.items.length;
  };
  redraw();
  return [para(T("Tap a word to add it. Tap a word in your sentence to take it out."), "muted"), line, pool, done];
}

/** Matching: tap a left item, then a right item, to pair them; tap a pair to undo it. */
function matching(q, finish) {
  const pairOf = q.left.map(() => null);  // left index → right index
  let picked = null;
  const done = button(T("Check"), () => pairOf.every((r) => r !== null) && finish([...pairOf]), "primary");
  const wrap = el("div", {});
  const redraw = () => {
    const rightUsed = new Map(pairOf.map((r, l) => [r, l]).filter(([r]) => r !== null));
    const badge = (n) => el("span", { class: "badge", "aria-hidden": "true" }, String(n + 1));
    const lefts = q.left.map((t, i) => {
      const paired = pairOf[i] !== null;
      return button([paired ? badge(i) : null, t], () => {
        if (paired) pairOf[i] = null; else picked = picked === i ? null : i;
        redraw();
      }, `match${paired ? " paired" : ""}${picked === i ? " picked" : ""}`);
    });
    const rights = q.right.map((t, r) => {
      const l = rightUsed.get(r);
      return button([l !== undefined ? badge(l) : null, t], () => {
        if (l !== undefined) pairOf[l] = null;
        else if (picked !== null) { pairOf[picked] = r; picked = null; }
        redraw();
      }, `match${l !== undefined ? " paired" : ""}${picked !== null && l === undefined ? " ready" : ""}`);
    });
    wrap.replaceChildren(el("div", { class: "match-cols" }, el("div", { class: "col" }, ...lefts), el("div", { class: "col" }, ...rights)));
    done.disabled = pairOf.some((r) => r === null);
  };
  redraw();
  return [para(T("Tap an item on the left, then its partner on the right. Tap a pair to undo it."), "muted"), wrap, done];
}

/** Sorting (matching with groups): tap a word, then tap its group; tap a word inside a group to take it out. */
function sorting(q, finish) {
  const groupOf = q.left.map(() => null);
  let picked = null;
  const done = button(T("Check"), () => groupOf.every((g) => g !== null) && finish([...groupOf]), "primary");
  const wrap = el("div", {});
  const redraw = () => {
    const loose = q.left.map((t, i) => (groupOf[i] === null ? button(t, () => { picked = picked === i ? null : i; redraw(); }, `tile${picked === i ? " picked" : ""}`) : null));
    const groups = q.right.map((g, gi) => el("div", { class: `group${picked !== null ? " ready" : ""}`, role: "button", tabindex: "0",
      onclick: (e) => { if (e.target.closest(".tile") || picked === null) return; groupOf[picked] = gi; picked = null; redraw(); },
      onkeydown: (e) => { if ((e.key === "Enter" || e.key === " ") && picked !== null) { e.preventDefault(); groupOf[picked] = gi; picked = null; redraw(); } } },
      el("div", { class: "group-name" }, g),
      el("div", { class: "tiles" }, ...q.left.map((t, i) => (groupOf[i] === gi ? button(t, () => { groupOf[i] = null; redraw(); }, "tile placed") : null)))));
    wrap.replaceChildren(el("div", { class: "tiles" }, ...loose), ...groups);
    done.disabled = groupOf.some((g) => g === null);
  };
  redraw();
  return [para(T("Tap a word, then tap its group. Tap a word in a group to take it out."), "muted"), wrap, done];
}

/** Shows q; calls onAnswer({result, ms}) when the pupil answers or presses "I don't know". */
function askQuestion(q, { kicker, title, onAnswer, bar = null, back = null }) {
  const t0 = performance.now();
  const finish = (response) => onAnswer({ result: check(q, response), ms: Math.round(performance.now() - t0) });
  const body = [bar, header(kicker, title), el("div", { class: "prompt" }, q.prompt), figureBox(q.figure)];
  if (q.type === "blanks") {
    // a step-by-step line: one small box per blank, all checked together (2026-10-19)
    const inputs = q.answers.map((_, i) => el("input", { type: "text", inputmode: "numeric", autocomplete: "off", class: "blank-input", "aria-label": T("Box {a}", { a: i + 1 }) }));
    const go = () => { const v = inputs.map((x) => normaliseInput(x.value, q)); if (v.every(Boolean)) finish(v); else inputs[v.findIndex((x) => !x)].focus(); };
    inputs.forEach((x, i) => x.addEventListener("keydown", (e) => { if (e.key === "Enter") (i < inputs.length - 1 && !inputs[i + 1].value ? inputs[i + 1].focus() : go()); }));
    setTimeout(() => inputs[0].focus(), 50);
    body.push(para(T("Fill in each box, then check."), "muted"),
      el("div", { class: "sentence blanks" }, q.parts.flatMap((p, i) => (i < inputs.length ? [p, inputs[i]] : [p]))), button(T("Check"), go, "primary"));
  } else if (q.type === "numeric") {
    const { input, check: go } = answerBox(q, finish);
    body.push(el("div", { class: "answer" }, input, q.unit ? el("span", { class: "unit" }, q.unit) : null), go);
  } else if (q.type === "cloze" && q.mode === "type") {
    const { input, check: go } = answerBox(q, finish, true);
    body.push(clozeSentence(q, input), go);
  } else if (q.type === "cloze") {
    body.push(clozeSentence(q), el("div", { class: "options" }, q.options.map((o, i) => button(o.text, () => finish(i), "option"))));
  } else if (q.type === "mcq" || q.type === "spot_error") {
    if (q.type === "spot_error") body.push(para(T("Tap the one that is wrong."), "muted"));
    body.push(el("div", { class: "options" }, q.options.map((o, i) => button(o.text, () => finish(i), "option"))));
  } else if (q.type === "ordering") {
    const chosen = [];
    const list = el("ol", { class: "chosen" });
    const pool = el("div", { class: "options" });
    const redraw = () => {
      list.replaceChildren(...chosen.map((i) => el("li", {}, q.items[i])));
      fill(pool, q.items.map((t, i) => (chosen.includes(i) ? null : button(t, () => { chosen.push(i); redraw(); }, "option"))));
      if (chosen.length === q.items.length) finish([...chosen]);
    };
    body.push(para(T("Tap them in order."), "muted"), list, pool, button(T("Start again"), () => { chosen.length = 0; redraw(); }, "link"));
    redraw();
  } else if (q.type === "word_order") {
    body.push(...wordOrder(q, finish));
  } else if (q.type === "matching") {
    body.push(...(q.groups ? sorting(q, finish) : matching(q, finish)));
  }
  body.push(button(T("I don't know"), () => finish(DONT_KNOW), "idk"), back);
  screen(...body);
}

const recordOf = (q, r, ms, phase) => ({
  phase, id: q.id, level: q.level, result: r.correct ? "right" : r.dontKnow ? "idk" : "wrong",
  seconds: Math.round(ms / 100) / 10, misconception: r.misconception?.id || "",
});
const toMenu = () => button(T("Back to the lessons"), menu, "link");

// ---------------------------------------------------------------- 1. first visit: readiness check (Primary 6 maths)
function start() {
  withSubject("maths", () => screen(
    header("Form One", "Before we start"),
    ...lines(L0().note.text),
    para("Nothing you type leaves this phone. There is no name to enter.", "muted"),
    button("Start the check", () => readinessQ(readiness.buildReadiness(L0(), newSeed(), libs.maths), 0, []), "primary"),
    toMenu(),
  ));
}

// No feedback during the check, and no score at the end (TR-C19, approved 2026-10-03):
// the pupil sees a neutral "Let's start"; scores and weak areas appear only in "Copy results".
function readinessQ(qs, i, rows) {
  if (i >= qs.length) return readinessDone(rows);
  askQuestion(qs[i], {
    bar: progress(i + 1, qs.length), kicker: "Getting ready", title: "Primary School maths",
    onAnswer: ({ result, ms }) => {
      rows.push({ ...recordOf(qs[i], result, ms, "readiness"), template: qs[i].id, correct: result.correct });
      readinessQ(qs, i + 1, rows);
    },
  });
}

function readinessDone(rows) {
  state.readiness = { score: readiness.scoreReadiness(L0(), rows), rows, at: new Date().toISOString() };
  save();
  screen(
    header("Thank you", "Let's start"),
    para("Now we begin Form One, one small idea at a time."),
    button("See the Maths lessons", () => { state.subject = "maths"; save(); menu(); }, "primary"),
  );
}

// ---------------------------------------------------------------- 2. home, subjects, streaks, stars and badges
// Design of 2026-10-17 (Dion: "colourful and interactive, with streaks"): a home screen with the streak, stars and
// one coloured tile per subject; each subject shows its lessons as a path. Streaks are forgiving (ghost towns, power
// cuts, no data): up to two days off in a row never break a streak.
const subj = () => state.subject in SUBJECTS ? state.subject : "maths";
const nextLesson = (s) => LESSONS[s].find((n) => !state.lessons[lessonKey(s, n)]?.done);
const inProgress = (s) => { const c = state.current[s]; return c && !teach.isDone(c.flow) ? c : null; };

// Each subject's colour (dark enough for white text: contrast 4.5:1 or more) and icon.
const STYLE = {
  maths: ["#1d4ed8", "🔢"], english: ["#6d28d9", "📖"], physics: ["#b45309", "⚡"], chemistry: ["#0f766e", "🧪"], geography: ["#2e7d32", "🌍"],
  "home-economics": ["#b42318", "🍲"], history: ["#7c4a1e", "🏛️"], biology: ["#3f7d20", "🌱"], "computer-science": ["#334e9c", "💻"], french: ["#ad1457", "💬"],
};
const colourOf = (s) => (STYLE[s] || ["#1f6f4a"])[0];
const iconOf = (s) => (STYLE[s] || ["", "📘"])[1];
const tinted = (s, ...kids) => { const e = el(...kids); e.style.setProperty("--subj", colourOf(s)); return e; };

// Lesson content is loaded one subject at a time in the installed app (subjects/<id>.js); the single-file copy has
// everything already. withSubject() shows the screen as soon as the subject is ready.
const loading = {};
function loadSubject(s) {
  if (CONTENT[s]) return Promise.resolve();
  if (!loading[s]) loading[s] = new Promise((ok, fail) => {
    const tag = document.createElement("script");
    tag.src = `subjects/${s}.js?v=${VERSIONS[s] || BUILD}`;  // the file's content fingerprint: new lessons, new address
    tag.onload = () => (CONTENT[s] ? ok() : fail(new Error("empty")));
    tag.onerror = () => { delete loading[s]; tag.remove(); fail(new Error("offline")); };
    document.head.append(tag);
  });
  return loading[s];
}
function withSubject(s, show) {
  if (CONTENT[s]) return show();
  screen(header(`${iconOf(s)} ${SUBJECTS[s]}`, "Getting the lessons ready…"), para("This takes a moment the first time.", "muted"));
  loadSubject(s).then(show, () => screen(header(`${iconOf(s)} ${SUBJECTS[s]}`, "No connection"),
    para("These lessons are not saved on this phone yet. Connect to the internet once, then they will work offline.", "muted"),
    button("Try again", () => withSubject(s, show), "primary"), button("Back to all subjects", home, "link")));
}
const loadAll = (list) => Promise.all(list.map(loadSubject));

// ---- days, streak, stars, badges (all on this phone only)
const dayOf = (d = new Date()) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
const dayNum = (s) => Math.round(Date.UTC(+s.slice(0, 4), +s.slice(5, 7) - 1, +s.slice(8, 10)) / 86400000);
/** Marks today as a learning day (called on every answer in a lesson). */
function recordDay() {
  state.days = state.days || [];
  const t = dayOf();
  if (state.days[state.days.length - 1] !== t) state.days.push(t);
}
/** Learning days in the current run; a run survives up to two days off in a row. 0 if the last learning day was too long ago. */
function streak() {
  const days = [...new Set(state.days || [])].map(dayNum).sort((a, b) => a - b);
  if (!days.length || dayNum(dayOf()) - days[days.length - 1] > 3) return 0;
  let n = 1;
  for (let i = days.length - 1; i > 0 && days[i] - days[i - 1] <= 3; i--) n++;
  return n;
}
/** Stars for a finished lesson: 3 if at least 80% of first tries were right, 2 if at least half, otherwise 1. */
function starsOf(r) {
  if (!r?.done) return 0;
  if (r.stars) return r.stars;
  const first = r.rows.filter((x) => x.phase === "practice" && x.attempt === 1);
  const asked = first.length || r.rows.filter((x) => x.attempt === 1).length;
  if (!asked) return 3;
  const right = (first.length ? first : r.rows.filter((x) => x.attempt === 1)).filter((x) => x.result === "right").length / asked;
  return right >= 0.8 ? 3 : right >= 0.5 ? 2 : 1;
}
const doneIn = (s) => LESSONS[s].filter((n) => state.lessons[lessonKey(s, n)]?.done);
const totalDone = () => Object.keys(SUBJECTS).reduce((t, s) => t + doneIn(s).length, 0);
const totalStars = () => Object.keys(SUBJECTS).reduce((t, s) => t + doneIn(s).reduce((u, n) => u + starsOf(state.lessons[lessonKey(s, n)]), 0), 0);
const starText = (k) => "★".repeat(k) + "☆".repeat(3 - k);
const BADGES = [
  ["first", "🎉", "First lesson", "Finish one lesson", () => totalDone() >= 1],
  ["five", "📚", "Bookworm", "Finish 5 lessons", () => totalDone() >= 5],
  ["ten", "🏅", "Ten lessons", "Finish 10 lessons", () => totalDone() >= 10],
  ["twentyfive", "🏆", "Champion", "Finish 25 lessons", () => totalDone() >= 25],
  ["fifty", "👑", "Fifty!", "Finish 50 lessons", () => totalDone() >= 50],
  ["streak3", "🔥", "On fire", "A 3-day streak", () => streak() >= 3],
  ["streak7", "🌟", "One week", "A 7-day streak", () => streak() >= 7],
  ["streak14", "💪", "Two weeks", "A 14-day streak", () => streak() >= 14],
  ["stars30", "⭐", "Star collector", "Collect 30 stars", () => totalStars() >= 30],
  ["stars100", "🌠", "Star shower", "Collect 100 stars", () => totalStars() >= 100],
  ["explorer", "🌈", "Explorer", "Finish a lesson in every subject", () => Object.keys(SUBJECTS).every((s) => doneIn(s).length)],
  ...Object.keys(SUBJECTS).map((s) => [`all-${s}`, iconOf(s), `All of ${SUBJECTS[s]}`, `Finish every ${SUBJECTS[s]} lesson`, () => doneIn(s).length === LESSONS[s].length]),
];
/** Badges earned now that were not earned before; they are kept for ever once earned. */
function newBadges() {
  state.badges = state.badges || {};
  const fresh = BADGES.filter(([id, , , , ok]) => !state.badges[id] && ok());
  for (const [id] of fresh) state.badges[id] = dayOf();
  if (fresh.length) save();
  return fresh;
}

// ---- screens
const statPill = (icon, value, label) => el("div", { class: "pill" }, el("span", { class: "pill-icon", "aria-hidden": "true" }, icon), el("strong", {}, String(value)), el("span", {}, label));
let installPrompt = null;  // Android: the browser's "Install app" prompt, kept until the pupil taps Install
addEventListener("beforeinstallprompt", (e) => { e.preventDefault(); installPrompt = e; });

function home() {
  document.documentElement.lang = "en";
  newBadges();
  const st = streak();
  const going = Object.keys(SUBJECTS).map((s) => [s, inProgress(s)]).filter(([, c]) => c).sort((a, b) => (b[1].at || "").localeCompare(a[1].at || ""))[0];
  const tiles = Object.entries(SUBJECTS).map(([s, name]) => {
    const done = doneIn(s).length, all = LESSONS[s].length;
    return tinted(s, "button", { type: "button", class: `tile-subject${done === all ? " complete" : ""}`, onclick: () => { state.subject = s; save(); menu(); } },
      el("span", { class: "ts-icon", "aria-hidden": "true" }, iconOf(s)), el("span", { class: "ts-name" }, name),
      el("span", { class: "ts-bar", "aria-hidden": "true" }, el("span", { style: `width:${Math.round((100 * done) / all)}%` })),
      el("span", { class: "ts-count" }, done === all ? "All done ✓" : `${done} of ${all}`));
  });
  const earned = Object.keys(state.badges || {}).length;
  screen(
    el("header", { class: "hello" }, el("div", { class: "kicker" }, "Form One"), el("h1", {}, st ? "Welcome back! Keep it going" : "Hello! Ready to learn?")),
    el("div", { class: "pills" }, statPill("🔥", st, st === 1 ? "day" : "days"), statPill("⭐", totalStars(), "stars"), statPill("✓", totalDone(), "lessons")),
    st ? para(st >= 2 ? `A ${st}-day streak. Up to two days off won't break it.` : "Your streak has started. Come back tomorrow!", "muted streak-note") : null,
    going ? tinted(going[0], "button", { type: "button", class: "primary continue", onclick: () => openLesson(going[0], going[1].lesson) },
      `${iconOf(going[0])} Carry on: ${SUBJECTS[going[0]]} · Lesson ${going[1].lesson}`) : null,
    installPrompt ? button("📲 Install the app on this phone", async () => { installPrompt.prompt(); installPrompt = null; }, "") : null,
    el("div", { class: "tiles-subjects" }, tiles),
    button(`🏅 My badges (${earned} of ${BADGES.length})`, badgesScreen, "badges-link"),
    para("These lessons are drafts: a teacher has not checked them all yet.", "muted"),
    el("details", { class: "grownup" }, el("summary", {}, "For a grown-up"), grownUp()),
  );
}

function badgesScreen() {
  newBadges();
  screen(header("My badges", `${Object.keys(state.badges || {}).length} of ${BADGES.length} earned`),
    el("div", { class: "badges" }, BADGES.map(([id, icon, name, how]) => {
      const got = state.badges?.[id];
      return el("div", { class: `badge-card${got ? " got" : ""}` }, el("span", { class: "b-icon", "aria-hidden": "true" }, got ? icon : "🔒"),
        el("strong", {}, name), el("span", { class: "muted" }, got ? `Earned ${got}` : how));
    })),
    button("Back to all subjects", home, "primary"));
}

/** One subject: its lessons as a path, the next one highlighted. (Called "menu" since the first prototype.) */
function menu() {
  document.documentElement.lang = "en";
  const s = subj();
  withSubject(s, () => {
    const cur = inProgress(s), next = nextLesson(s);
    const done = doneIn(s).length, stars = doneIn(s).reduce((t, n) => t + starsOf(state.lessons[lessonKey(s, n)]), 0);
    const row = (n) => {
      const r = state.lessons[lessonKey(s, n)], going = cur?.lesson === n, isNext = !cur && n === next;
      const mark = r?.done ? "✓" : going ? "…" : String(n);
      const sub = r?.done ? `${starText(starsOf(r))} · tap to practise again` : going ? "Started · tap to carry on" : PAPER[s]?.includes(n) ? "Writing on paper" : "";
      return el("li", { class: `step${r?.done ? " is-done" : ""}${going || isNext ? " is-next" : ""}` },
        el("button", { type: "button", class: `lesson${r?.done ? " is-done" : ""}`, onclick: () => openLesson(s, n) },
          el("span", { class: "mark", "aria-hidden": "true" }, mark),
          el("span", { class: "lt" }, el("span", { class: "ln" }, `Lesson ${n}`), TITLES[s][n], sub ? el("span", { class: "sub" }, sub) : null)),
        // a finished or started lesson can be reset, so the pupil starts it again from the first card
        r?.done || going ? el("button", { type: "button", class: "link reset", "aria-label": `Start Lesson ${n} again from the beginning`, onclick: () => resetLesson(s, n) }, "↺ Start again") : null);
    };
    // The Primary 6 readiness check belongs to Maths only: it is offered first on the Maths tab until it is done
    // (2026-10-07; before, it blocked the whole app on a first visit). It never blocks a lesson or the English tab.
    const check = s === "maths" && !state.readiness;
    const lead = check ? [button("Before Maths: a short check (13 questions)", start, "primary"),
        para("It looks at the Primary School maths you need. About 10 minutes, no marks.", "muted")]
      : cur ? button(`Carry on with Lesson ${cur.lesson}`, () => openLesson(s, cur.lesson), "primary")
      : next ? button(`Start Lesson ${next}: ${TITLES[s][next]}`, () => openLesson(s, next), "primary") : null;
    screen(tinted(s, "div", { class: "subject-page" },
      button("← All subjects", home, "link back"),
      el("header", { class: "subject-head" }, el("span", { class: "sh-icon", "aria-hidden": "true" }, iconOf(s)),
        el("div", {}, el("div", { class: "kicker" }, `Form One ${SUBJECTS[s]}`), el("h1", {}, done ? `${done} of ${LESSONS[s].length} lessons done` : "Your lessons"))),
      progress(done, LESSONS[s].length),
      stars ? para(`⭐ ${stars} stars in ${SUBJECTS[s]}`, "muted") : null,
      lead,
      el("ol", { class: "path" }, LESSONS[s].map(row)),
      para("These lessons are drafts: a teacher has not checked them all yet.", "muted")));
  });
}

function grownUp() {
  const status = para("", "muted");
  const subjectsWithWork = () => Object.keys(SUBJECTS).filter((s) => doneIn(s).length);
  return el("div", {},
    para("Results stay on this phone until you copy them.", "muted"),
    button("Copy all results", () => loadAll(subjectsWithWork()).then(() => copyText(allResultsText(), status), () => { status.textContent = "Connect to the internet once to copy every result."; }), "primary"), status,
    MODE === "pwa" ? button("Save every subject for offline use", () => {
      status.textContent = "Saving…";
      loadAll(Object.keys(SUBJECTS)).then(() => { status.textContent = "Every subject is saved on this phone. It works without internet now."; },
        () => { status.textContent = "Some subjects could not be saved. Connect to the internet and try again."; });
    }, "") : null,
    MODE === "pwa" ? el("a", { class: "button-link", href: "offline.html", download: "psalmspreps-form-one.html" }, "Download one file to share by Bluetooth or a flash drive") : null,
    button("Do the readiness check again", start, ""),
    button("Clear all progress on this phone", () => {
      if (!confirm("Clear all saved progress on this phone? This cannot be undone.")) return;
      try { localStorage.removeItem(KEY); } catch { /* nothing saved */ }
      location.reload();
    }, "link"));
}

// ---------------------------------------------------------------- 3. teach mode
let S = "maths";                            // the subject of the lesson on screen
const C = () => state.current[S];
const L = () => CONTENT[S][C().lesson];
const N = () => C().lesson;
const LIB = () => libs[S];

/** Opens lesson n: carries on a saved, unfinished flow, otherwise starts it fresh. */
function openLesson(s, n) {
  withSubject(s, () => {
    S = s;
    document.documentElement.lang = s === "french" ? "fr" : "en";  // screen readers read French lessons in French
    const cur = state.current[s];
    if (cur?.lesson === n && !teach.isDone(cur.flow)) { cur.at = new Date().toISOString(); return lesson(resumable(cur.flow)); }
    state.current[s] = { lesson: n, flow: teach.startTeach(CONTENT[s][n], newSeed()), rows: [], at: new Date().toISOString() };
    save();
    lesson(state.current[s].flow);
  });
}
/** Starts lesson n again from its first card: clears its saved run (stars, answers) and any unfinished flow,
 *  after the pupil confirms. Badges already earned and other lessons are kept. */
function resetLesson(s, n) {
  if (!confirm(`Start Lesson ${n} again from the beginning?\nYour stars and saved answers for this lesson will be cleared.`)) return;
  delete state.lessons[lessonKey(s, n)];
  if (state.current[s]?.lesson === n) delete state.current[s];
  save();
  openLesson(s, n);
}
/** A flow saved mid-feedback resumes on a question: "retry" → the fresh variant, "reveal" → the next step. */
const resumable = (flow) => (flow.phase === "retry" || flow.phase === "reveal" ? teach.nextPhase(flow) : flow);

const workedBlock = () => {
  const w = renderWorked(L().worked_example, LIB());
  return el("div", { class: "example" }, el("div", { class: "kicker" }, T("Worked example")), el("div", { class: "strong pre" }, w.problem),
    figureBox(w.figure), el("ol", {}, w.steps.map((s) => el("li", {}, s))), para(T("Answer: {a}", { a: w.answer }), "strong"));
};
const cardExample = (c) => el("div", { class: "example" }, el("div", { class: "kicker" }, T("Example")), ...c.example.map((t) => para(t)), figureBox(c.figure));
const hintBlock = (q) => (q.hint ? el("div", { class: "hint" }, el("strong", {}, T("Hint: ")), q.hint) : null);

/** Every screen of a lesson goes through here, so the flow is saved at each step. */
function lesson(flow, previous = null) {
  C().flow = flow;
  save();
  if (teach.isDone(flow)) return results(flow);
  const Ln = L(), n = N();
  const step = flow.steps[flow.step];
  const nCards = Ln.teach.cards.length;
  const nPractice = flow.steps.filter((s) => s.kind === "practice").length;
  const practiceNo = flow.steps.slice(0, flow.step + 1).filter((s) => s.kind === "practice").length;
  const kicker = step.kind === "card" ? T("Lesson {n} · Idea {a} of {b}", { n, a: step.card + 1, b: nCards }) : T("Lesson {n} · Practice {a} of {b}", { n, a: practiceNo, b: nPractice });
  const go = (next, prev = null) => () => lesson(next, prev);
  const bar = progress(flow.step + 1, flow.steps.length);

  if (step.kind === "card" && flow.phase === "idea") {
    const c = teach.renderCard(Ln.teach.cards[step.card], LIB());
    return screen(bar, header(kicker, TITLES[S][n]), el("div", { class: "idea" }, c.idea), cardExample(c),
      button(T("I'm ready for a question"), go(teach.nextPhase(flow)), "primary"), toMenu());
  }
  if (step.kind === "card" || step.kind === "practice") {
    const q = teach.itemQuestion(Ln, flow, LIB(), previous);
    return askQuestion(q, {
      bar, kicker, back: toMenu(), title: q.type === "blanks" ? T("Step by step") : flow.attempt ? T("A new question") : step.kind === "card" ? T("Quick check") : T("Level {a}", { a: q.level }),
      onAnswer: ({ result, ms }) => {
        C().rows.push({ ...recordOf(q, result, ms, step.kind), card: step.kind === "card" ? Ln.teach.cards[step.card].id : "", attempt: flow.attempt + 1 });
        recordDay();
        const next = teach.answerItem(flow, result, ms);
        C().flow = next;
        save();
        if (next.phase === "reveal") return reveal(q, next, kicker, bar, result);
        if (next.phase === "retry") return retry(q, result, next, kicker, bar);
        // Teach mode only: green flash + check icon (readiness shows no right/wrong cues).
        return screen(bar, el("div", { class: "fb good flash", role: "status" }, checkIcon(), el("strong", {}, T("Correct!")),
          // 517 typed for 51₇: right, with a gentle word that the base is not typed
          result.baseTyped ? para(`Well done. You don't need to type the base: ${q.answer} is enough (the small ${q.base} only shows it is base ${q.base}).`) : null),
          button(T("Next"), go(next), "primary"));
      },
    });
  }
  if (step.kind === "worked_example") {
    return screen(bar, header(T("Lesson {n} · Worked example", { n }), T("Follow each step")), workedBlock(),
      button(T(Ln.paper_task ? "Now write" : "Now practise"), go(teach.nextPhase(flow)), "primary"), toMenu());
  }
  if (step.kind === "paper") return paperTask(flow, bar);
  if (step.kind === "note") {
    return screen(bar, header(T("Lesson {n} · Summary", { n }), TITLES[S][n]), el("div", { class: "note" }, ...lines(Ln.note.text)),
      button(T("Finish"), go(teach.nextPhase(flow)), "primary"));
  }
}

/**
 * Writing lessons: the task → the pupil writes in the exercise book → "I've written it" → model answer and a
 * self-check list. The ticks are kept for the parent summary only; the app does not mark the writing (TR-E25).
 */
function paperTask(flow, bar) {
  const p = teach.renderPaper(L(), LIB()), n = N();
  const ticks = C().paper?.ticks || p.checklist.map(() => false);
  const write = () => screen(bar, header(`Lesson ${n} · Your turn to write`, "Write in your exercise book"),
    el("div", { class: "idea pre" }, p.prompt),
    para("Take your time. When you have finished writing, tap the button.", "muted"),
    button("I've written it", () => { C().paper = { written: true, ticks }; save(); review(); }, "primary"), toMenu());
  const review = () => {
    const boxes = p.checklist.map((item, i) => {
      const box = el("input", { type: "checkbox", id: `tick${i}` });
      box.checked = !!ticks[i];
      box.addEventListener("change", () => { ticks[i] = box.checked; C().paper = { written: true, ticks }; save(); });
      return el("label", { class: "tickrow", for: `tick${i}` }, box, el("span", {}, item));
    });
    screen(bar, header(`Lesson ${n} · Check your writing`, "Compare with this example"),
      el("div", { class: "example" }, el("div", { class: "kicker" }, "An example answer"), ...p.model.map((m) => para(m))),
      para("Look at your own writing. Tick each thing you did.", "strong"),
      el("div", { class: "ticks" }, boxes),
      para("There is no score for writing. A grown-up can look at your exercise book.", "muted"),
      button("Done", () => lesson(teach.nextPhase(flow)), "primary"));
  };
  return C().paper?.written ? review() : write();
}

/**
 * First miss, then a fresh variant (asked step by step when the template has a scaffold). Since 2026-10-19:
 *  - "I don't know": the hint, then this question's own working, one step per tap, then a new question;
 *  - a wrong answer: what the mistake was (a known misconception when the answer matches one), then for computed
 *    questions "one like it": another variant of the same shape with its working, so the example fits the question.
 */
function retry(q, result, flow, kicker, bar) {
  const step = flow.steps[flow.step];
  const again = (seen) => button(T("Try a new question"), () => lesson(teach.nextPhase(flow), seen), "primary");
  const workingBox = (title, x, list) => el("div", { class: "example" }, el("div", { class: "kicker" }, title), el("div", { class: "strong pre" }, x.prompt), figureBox(x.figure), list);
  if (result.dontKnow && q.solution?.length) {
    const list = el("ol", { "aria-live": "polite" }), tail = el("div", {});
    let shown = 0;
    const more = () => {
      list.append(el("li", {}, q.solution[shown++]));
      fill(tail, [shown < q.solution.length ? button(T("Show the next step"), more, "primary") : again(q)]);
    };
    screen(bar, header(kicker, T("Let's try again")),
      el("div", { class: "fb soft", role: "status" }, el("strong", {}, T("That's fine. Let's look at it together."))),
      hintBlock(q), workingBox(T("Here is how to do this one"), q, list), tail);
    return more();
  }
  const wrongPairs = result.wrongPairs?.length
    ? para(T(result.wrongPairs.length === 1 ? "This one is not right yet: {a}." : "These are not right yet: {a}.", { a: result.wrongPairs.map((i) => q.left[i]).join(", ") })) : null;
  const box = result.dontKnow
    // "I don't know" on a question without written working: the hint and the worked example (spec §4)
    ? el("div", { class: "fb soft", role: "status" }, el("strong", {}, T("That's fine. Let's look at it together.")))
    : el("div", { class: "fb bad shake", role: "status" }, el("strong", {}, T("✗ Not quite")),
      result.misconception?.explain ? para(result.misconception.explain) : wrongPairs || para(T("Look at the example again, then try a new question.")));
  const like = result.dontKnow ? null : teach.exampleLike(L(), flow, LIB(), q);
  const help = like ? [workingBox(T("Here is one like it"), like, el("ol", {}, like.solution.map((s) => el("li", {}, s))))]
    : step.kind === "card" ? [result.dontKnow ? hintBlock(q) : null, cardExample(teach.renderCard(L().teach.cards[step.card], LIB()))]
    : result.dontKnow ? [hintBlock(q), workedBlock()] : [];
  screen(bar, header(kicker, T("Let's try again")), box, ...help, again(like ? [q, like] : q));
}

/** Second miss: the correct answer with full working, then move on (marked "needs review"). */
function reveal(q, flow, kicker, bar, result) {
  const shown = q.type === "matching" ? T("Here are the right answers.")
    : T("The answer is: {a}", { a: `${q.answer}${q.base ? LIB().sub(q.base) : ""}${q.unit ? " " + q.unit : ""}` });  // 51₇, not 51
  screen(bar, header(kicker, T("Here is how to do it")),
    el("div", { class: result.dontKnow ? "fb soft" : "fb bad shake", role: "status" }, el("strong", {}, shown)),
    el("div", { class: "example" }, el("div", { class: "kicker" }, T("Full working")), el("ol", {}, q.solution.map((s) => el("li", {}, s)))),
    para(T("We will come back to this one later."), "muted"),
    button(T("Continue"), () => lesson(teach.nextPhase(flow)), "primary"));
}

// ---------------------------------------------------------------- 4. results + copy
/** A simple CSS confetti burst: each piece gets a direction, spin, colour and delay. Hidden under reduced motion. */
function confetti() {
  const colours = ["#1f6f4a", "#e0a526", "#2f6fd6", "#d0473b", "#7c4dbd", "#2aa198"];
  const box = el("div", { class: "confetti", "aria-hidden": "true" });
  for (let i = 0; i < 28; i++) {
    const angle = (Math.PI * 2 * i) / 28 + Math.random() * 0.3, dist = 90 + Math.random() * 90;
    box.append(el("i", { style: `--x:${Math.round(Math.cos(angle) * dist)}px;--y:${Math.round(Math.sin(angle) * dist - 40)}px;` +
      `--r:${Math.round(Math.random() * 540 - 270)}deg;--c:${colours[i % colours.length]};--d:${Math.round(Math.random() * 120)}ms` }));
  }
  return box;
}

const count = (rows, k) => rows.filter((r) => r.result === k).length;
const row = (x) => `${x.phase}\t${x.card ? x.card + "#" + x.attempt : x.attempt ? "#" + x.attempt : ""}\t${x.id}\tL${x.level}\t${x.result}\t${x.seconds}s\t${x.misconception}`;
const TABLE_HEAD = "phase\tcard#try\ttemplate\tlevel\tresult\ttime\tmisconception";

function readinessText() {
  const r = state.readiness?.score;
  return [`Readiness (not shown to the pupil): ${r ? `${r.right}/${r.asked} (${r.percent}%) · ${state.readiness.at.slice(0, 10)}` : "not done"}`,
    ...(r ? Object.values(r.areas).map((a) => `  ${a.name}: ${a.right}/${a.asked}${a.weak ? " · WEAK" : ""}`) : [])];
}
function lessonText(s, n, r) {
  const cards = r.rows.filter((x) => x.phase === "card"), practice = r.rows.filter((x) => x.phase === "practice");
  const secs = r.rows.reduce((t, x) => t + x.seconds, 0);
  const out = [`${SUBJECTS[s]} Lesson ${n} (${TITLES[s][n]}) · ${r.at.slice(0, 16).replace("T", " ")} · ${Math.round(secs)}s · "I don't know" ${count(r.rows, "idk")}`,
    `  cards: ${count(cards, "right")} right, ${count(cards, "wrong")} wrong, ${count(cards, "idk")} IDK · practice: ${count(practice, "right")} right, ${count(practice, "wrong")} wrong, ${count(practice, "idk")} IDK`,
    `  needs review (missed twice): ${r.review.join(", ") || "none"}`];
  if (r.paper) {
    const items = teach.renderPaper(CONTENT[s][n], libs[s]).checklist;
    out.push(`  paper task (not marked; self-check by the pupil): ${r.paper.ticks.filter(Boolean).length} of ${items.length} ticked`,
      ...items.map((t, i) => `    ${r.paper.ticks[i] ? "[x]" : "[ ]"} ${t}`));
  }
  return out;
}
const stamp = () => `Form One prototype ${BUILD} · ${new Date().toISOString().slice(0, 16).replace("T", " ")}`;

function lessonResultsText(s, n) {
  const r = state.lessons[lessonKey(s, n)];
  return [stamp(), ...readinessText(), ...lessonText(s, n, r), "", TABLE_HEAD, ...r.rows.map(row)].join("\n");
}
function allResultsText() {
  const out = [stamp(), ...readinessText()];
  const tables = [...(state.readiness?.rows || []).map(row)];
  for (const s of Object.keys(SUBJECTS)) {
    const done = LESSONS[s].filter((n) => state.lessons[lessonKey(s, n)]?.done);
    out.push(`${SUBJECTS[s]}: lessons done ${done.length} of ${LESSONS[s].length}`, ...done.flatMap((n) => lessonText(s, n, state.lessons[lessonKey(s, n)])));
    tables.push(...done.flatMap((n) => state.lessons[lessonKey(s, n)].rows.map(row)));
  }
  return [...out, "", TABLE_HEAD, ...tables].join("\n");
}

async function copyText(text, status, details = null, area = null) {
  try { await navigator.clipboard.writeText(text); status.textContent = "Copied. Paste it into WhatsApp or a message."; }
  catch {
    if (details && area) { details.open = true; area.select(); document.execCommand("copy"); status.textContent = "Copied (or select the text below and copy it)."; }
    else status.textContent = "Could not copy on this phone.";
  }
}

function results(flow) {
  const s = S, n = N(), Ln = L();
  const review = teach.needsReview(flow).map((x) => (x.kind === "card" ? Ln.teach.cards[x.card].id : x.template));
  // The latest finished run of a lesson replaces the previous one.
  const record = { done: true, at: new Date().toISOString(), rows: C().rows, review, ...(C().paper ? { paper: C().paper } : {}) };
  record.stars = starsOf(record);
  state.lessons[lessonKey(s, n)] = record;
  delete state.current[s];
  save();
  const text = lessonResultsText(s, n);
  const area = el("textarea", { readonly: "", rows: "10", "aria-label": "Results" });
  // The text holds the readiness score and weak areas, so it stays folded away from the pupil (TR-C30).
  const details = el("details", { class: "grownup" }, el("summary", {}, "Show the text (for a grown-up)"), area);
  area.value = text;
  const status = para("", "muted");
  const completed = flow.steps.filter((x) => x.kind === "card" || x.kind === "practice").length;
  const next = nextLesson(s);
  const badges = newBadges(), st = streak();
  screen(confetti(), el("div", { class: "done" }, el("div", { class: "done-title" }, T("Lesson {n} done", { n })),
    el("div", { class: "done-stars", "aria-label": `${record.stars} of 3 stars` }, [1, 2, 3].map((k) => el("span", { class: k <= record.stars ? "star on" : "star", style: `--k:${k}` }, "★"))),
    para(Ln.paper_task ? `You completed ${completed} questions and a writing task.` : T("You completed {a} questions.", { a: completed }), "done-sub"),
    st ? para(T("🔥 {a}-day streak", { a: st }), "done-streak") : null),
    badges.map(([, icon, name]) => el("div", { class: "new-badge" }, el("span", { "aria-hidden": "true" }, icon), el("strong", {}, T("New badge: {a}", { a: name })))),
    next ? button(T("Next: Lesson {a}", { a: next }), () => openLesson(s, next), "primary") : para(T("You have done every {a} lesson. Well done!", { a: SUBJECTS[s] }), "strong"),
    button(T("Back to the lessons"), menu, next ? "" : "primary"),
    button(T("All subjects"), home, "link"),
    para("For a grown-up: these results stay on this phone until you copy them.", "muted"),
    button("Copy results", () => copyText(text, status, details, area), ""), status, details);
}

// Start-up is at the end of review.js (pupils: the lesson menu; teachers with ?review: the review list).
