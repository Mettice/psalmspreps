// Prototype UI: Lesson 0 readiness (once) → lesson menu (Maths and English) → teach mode (cards, worked example,
// practice or a paper task, note) → results. Uses the real engine (inlined by build.mjs).
// Progress is saved in this browser only (localStorage, decisions 2026-10-05 and 2026-10-06); nothing is sent anywhere.
/* global ENGINE, CONTENT, TITLES, LESSONS, SUBJECTS, BUILD */
const { libs, template, teach, readiness } = ENGINE;
const { check, DONT_KNOW, renderWorked, normaliseInput, inputModeFor } = template;
const L0 = CONTENT.maths[0];

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
const checkIcon = () => {
  const ns = "http://www.w3.org/2000/svg";
  const svg = document.createElementNS(ns, "svg");
  svg.setAttribute("viewBox", "0 0 24 24"); svg.setAttribute("class", "tick"); svg.setAttribute("aria-hidden", "true");
  const path = document.createElementNS(ns, "path");
  path.setAttribute("d", "M5 12.5l4.5 4.5L19 7.5");
  svg.append(path);
  return svg;
};

// ---------------------------------------------------------------- one question, any type
/** A typed answer box (numbers or words): Enter or "Check" submits; the engine picks the keyboard. */
function answerBox(q, finish, inline = false) {
  const input = el("input", { type: "text", inputmode: inputModeFor(q), autocomplete: "off", autocorrect: "off", autocapitalize: "off",
    spellcheck: "false", "aria-label": "Your answer", class: inline ? "blank-input" : "" });
  const go = () => { const v = normaliseInput(input.value, q); if (v) finish(v); };
  input.addEventListener("keydown", (e) => e.key === "Enter" && go());
  setTimeout(() => input.focus(), 50);
  return { input, check: button("Check", go, "primary") };
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
  const done = button("Check", () => placed.length === q.items.length && finish([...placed]), "primary");
  const redraw = () => {
    line.replaceChildren(...(placed.length
      ? [...placed.map((i, k) => button(q.items[i], () => { placed.splice(k, 1); redraw(); }, "tile placed")), ...(q.end ? [el("span", { class: "end" }, q.end)] : [])]
      : [el("span", { class: "muted" }, "Tap the words below.")]));
    fill(pool, q.items.map((t, i) => (placed.includes(i) ? null : button(t, () => { placed.push(i); redraw(); }, "tile"))));
    done.disabled = placed.length !== q.items.length;
  };
  redraw();
  return [para("Tap a word to add it. Tap a word in your sentence to take it out.", "muted"), line, pool, done];
}

/** Matching: tap a left item, then a right item, to pair them; tap a pair to undo it. */
function matching(q, finish) {
  const pairOf = q.left.map(() => null);  // left index → right index
  let picked = null;
  const done = button("Check", () => pairOf.every((r) => r !== null) && finish([...pairOf]), "primary");
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
  return [para("Tap an item on the left, then its partner on the right. Tap a pair to undo it.", "muted"), wrap, done];
}

/** Sorting (matching with groups): tap a word, then tap its group; tap a word inside a group to take it out. */
function sorting(q, finish) {
  const groupOf = q.left.map(() => null);
  let picked = null;
  const done = button("Check", () => groupOf.every((g) => g !== null) && finish([...groupOf]), "primary");
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
  return [para("Tap a word, then tap its group. Tap a word in a group to take it out.", "muted"), wrap, done];
}

/** Shows q; calls onAnswer({result, ms}) when the pupil answers or presses "I don't know". */
function askQuestion(q, { kicker, title, onAnswer, bar = null, back = null }) {
  const t0 = performance.now();
  const finish = (response) => onAnswer({ result: check(q, response), ms: Math.round(performance.now() - t0) });
  const body = [bar, header(kicker, title), el("div", { class: "prompt" }, q.prompt)];
  if (q.type === "numeric") {
    const { input, check: go } = answerBox(q, finish);
    body.push(el("div", { class: "answer" }, input, q.unit ? el("span", { class: "unit" }, q.unit) : null), go);
  } else if (q.type === "cloze" && q.mode === "type") {
    const { input, check: go } = answerBox(q, finish, true);
    body.push(clozeSentence(q, input), go);
  } else if (q.type === "cloze") {
    body.push(clozeSentence(q), el("div", { class: "options" }, q.options.map((o, i) => button(o.text, () => finish(i), "option"))));
  } else if (q.type === "mcq" || q.type === "spot_error") {
    if (q.type === "spot_error") body.push(para("Tap the one that is wrong.", "muted"));
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
    body.push(para("Tap them in order.", "muted"), list, pool, button("Start again", () => { chosen.length = 0; redraw(); }, "link"));
    redraw();
  } else if (q.type === "word_order") {
    body.push(...wordOrder(q, finish));
  } else if (q.type === "matching") {
    body.push(...(q.groups ? sorting(q, finish) : matching(q, finish)));
  }
  body.push(button("I don't know", () => finish(DONT_KNOW), "idk"), back);
  screen(...body);
}

const recordOf = (q, r, ms, phase) => ({
  phase, id: q.id, level: q.level, result: r.correct ? "right" : r.dontKnow ? "idk" : "wrong",
  seconds: Math.round(ms / 100) / 10, misconception: r.misconception?.id || "",
});
const toMenu = () => button("Back to the lessons", menu, "link");

// ---------------------------------------------------------------- 1. first visit: readiness check (Primary 6 maths)
function start() {
  screen(
    header("Form One", "Before we start"),
    ...lines(L0.note.text),
    para("Nothing you type leaves this phone. There is no name to enter.", "muted"),
    button("Start the check", () => readinessQ(readiness.buildReadiness(L0, newSeed(), libs.maths), 0, []), "primary"),
    state.readiness ? toMenu() : null,
  );
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
  state.readiness = { score: readiness.scoreReadiness(L0, rows), rows, at: new Date().toISOString() };
  save();
  screen(
    header("Thank you", "Let's start"),
    para("Now we begin Form One, one small idea at a time."),
    button("See the lessons", menu, "primary"),
  );
}

// ---------------------------------------------------------------- 2. lesson menu (one subject at a time)
const subj = () => state.subject in SUBJECTS ? state.subject : "maths";
const nextLesson = (s) => LESSONS[s].find((n) => !state.lessons[lessonKey(s, n)]?.done);
const inProgress = (s) => { const c = state.current[s]; return c && !teach.isDone(c.flow) ? c : null; };

function menu() {
  const s = subj(), cur = inProgress(s), next = nextLesson(s);
  const done = LESSONS[s].filter((n) => state.lessons[lessonKey(s, n)]?.done).length;
  const tabs = el("div", { class: "subjects", role: "tablist" }, Object.entries(SUBJECTS).map(([id, name]) =>
    el("button", { type: "button", role: "tab", "aria-selected": String(id === s), class: `subject${id === s ? " on" : ""}`,
      onclick: () => { state.subject = id; save(); menu(); } }, name)));
  const row = (n) => {
    const r = state.lessons[lessonKey(s, n)], going = cur?.lesson === n;
    const mark = r?.done ? "✓" : going ? "…" : String(n);
    const sub = r?.done ? "Done · tap to practise again" : going ? "Started · tap to carry on" : CONTENT[s][n].paper_task ? "Writing on paper" : "";
    return el("button", { type: "button", class: `lesson${r?.done ? " is-done" : ""}`, onclick: () => openLesson(s, n) },
      el("span", { class: "mark", "aria-hidden": "true" }, mark),
      el("span", { class: "lt" }, el("span", { class: "ln" }, `Lesson ${n}`), TITLES[s][n], sub ? el("span", { class: "sub" }, sub) : null));
  };
  const lead = cur ? button(`Carry on with Lesson ${cur.lesson}`, () => openLesson(s, cur.lesson), "primary")
    : next ? button(`Start Lesson ${next}: ${TITLES[s][next]}`, () => openLesson(s, next), "primary") : null;
  screen(
    tabs,
    header(`Form One ${SUBJECTS[s]}`, done ? `${done} of ${LESSONS[s].length} lessons done` : "Your lessons"),
    lead,
    el("div", { class: "lessons" }, LESSONS[s].map(row)),
    para("These lessons are drafts: a teacher has not checked them all yet.", "muted"),
    el("details", { class: "grownup" }, el("summary", {}, "For a grown-up"), grownUp()),
  );
}

function grownUp() {
  const status = para("", "muted");
  return el("div", {},
    para("Results stay on this phone until you copy them.", "muted"),
    button("Copy all results", () => copyText(allResultsText(), status), "primary"), status,
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
  S = s;
  const cur = state.current[s];
  if (cur?.lesson === n && !teach.isDone(cur.flow)) return lesson(resumable(cur.flow));
  state.current[s] = { lesson: n, flow: teach.startTeach(CONTENT[s][n], newSeed()), rows: [] };
  save();
  lesson(state.current[s].flow);
}
/** A flow saved mid-feedback resumes on a question: "retry" → the fresh variant, "reveal" → the next step. */
const resumable = (flow) => (flow.phase === "retry" || flow.phase === "reveal" ? teach.nextPhase(flow) : flow);

const workedBlock = () => {
  const w = renderWorked(L().worked_example, LIB());
  return el("div", { class: "example" }, el("div", { class: "kicker" }, "Worked example"), el("div", { class: "strong pre" }, w.problem),
    el("ol", {}, w.steps.map((s) => el("li", {}, s))), para(`Answer: ${w.answer}`, "strong"));
};
const cardExample = (c) => el("div", { class: "example" }, el("div", { class: "kicker" }, "Example"), ...c.example.map((t) => para(t)));
const hintBlock = (q) => (q.hint ? el("div", { class: "hint" }, el("strong", {}, "Hint: "), q.hint) : null);

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
  const kicker = step.kind === "card" ? `Lesson ${n} · Idea ${step.card + 1} of ${nCards}` : `Lesson ${n} · Practice ${practiceNo} of ${nPractice}`;
  const go = (next, prev = null) => () => lesson(next, prev);
  const bar = progress(flow.step + 1, flow.steps.length);

  if (step.kind === "card" && flow.phase === "idea") {
    const c = teach.renderCard(Ln.teach.cards[step.card], LIB());
    return screen(bar, header(kicker, TITLES[S][n]), el("div", { class: "idea" }, c.idea), cardExample(c),
      button("I'm ready for a question", go(teach.nextPhase(flow)), "primary"), toMenu());
  }
  if (step.kind === "card" || step.kind === "practice") {
    const q = teach.itemQuestion(Ln, flow, LIB(), previous);
    return askQuestion(q, {
      bar, kicker, back: toMenu(), title: flow.attempt ? "A new question" : step.kind === "card" ? "Quick check" : `Level ${q.level}`,
      onAnswer: ({ result, ms }) => {
        C().rows.push({ ...recordOf(q, result, ms, step.kind), card: step.kind === "card" ? Ln.teach.cards[step.card].id : "", attempt: flow.attempt + 1 });
        const next = teach.answerItem(flow, result, ms);
        C().flow = next;
        save();
        if (next.phase === "reveal") return reveal(q, next, kicker, bar, result);
        if (next.phase === "retry") return retry(q, result, next, kicker, bar);
        // Teach mode only: green flash + check icon (readiness shows no right/wrong cues).
        return screen(bar, el("div", { class: "fb good flash", role: "status" }, checkIcon(), el("strong", {}, "Correct!")), button("Next", go(next), "primary"));
      },
    });
  }
  if (step.kind === "worked_example") {
    return screen(bar, header(`Lesson ${n} · Worked example`, "Follow each step"), workedBlock(),
      button(Ln.paper_task ? "Now write" : "Now practise", go(teach.nextPhase(flow)), "primary"), toMenu());
  }
  if (step.kind === "paper") return paperTask(flow, bar);
  if (step.kind === "note") {
    return screen(bar, header(`Lesson ${n} · Summary`, TITLES[S][n]), el("div", { class: "note" }, ...lines(Ln.note.text)),
      button("Finish", go(teach.nextPhase(flow)), "primary"));
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

/** First miss: feedback without the answer, then a fresh variant. */
function retry(q, result, flow, kicker, bar) {
  const step = flow.steps[flow.step];
  const wrongPairs = result.wrongPairs?.length
    ? para(`${result.wrongPairs.length === 1 ? "This one is" : "These are"} not right yet: ${result.wrongPairs.map((i) => q.left[i]).join(", ")}.`) : null;
  const box = result.dontKnow
    // "I don't know": no misconception feedback, only the hint and the worked example (spec §4)
    ? el("div", { class: "fb soft", role: "status" }, el("strong", {}, "That's fine. Let's look at it together."))
    : el("div", { class: "fb bad shake", role: "status" }, el("strong", {}, "✗ Not quite"),
      result.misconception?.explain ? para(result.misconception.explain) : wrongPairs || para("Look at the example again, then try a new question."));
  const help = step.kind === "card"
    ? [result.dontKnow ? hintBlock(q) : null, cardExample(teach.renderCard(L().teach.cards[step.card], LIB()))]
    : result.dontKnow ? [hintBlock(q), workedBlock()] : [];
  screen(bar, header(kicker, "Let's try again"), box, ...help, button("Try a new question", () => lesson(teach.nextPhase(flow), q), "primary"));
}

/** Second miss: the correct answer with full working, then move on (marked "needs review"). */
function reveal(q, flow, kicker, bar, result) {
  const shown = q.type === "matching" ? "Here are the right answers." : `The answer is: ${q.answer}${q.unit ? " " + q.unit : ""}`;
  screen(bar, header(kicker, "Here is how to do it"),
    el("div", { class: result.dontKnow ? "fb soft" : "fb bad shake", role: "status" }, el("strong", {}, shown)),
    el("div", { class: "example" }, el("div", { class: "kicker" }, "Full working"), el("ol", {}, q.solution.map((s) => el("li", {}, s)))),
    para("We will come back to this one later.", "muted"),
    button("Continue", () => lesson(teach.nextPhase(flow)), "primary"));
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
  state.lessons[lessonKey(s, n)] = { done: true, at: new Date().toISOString(), rows: C().rows, review, ...(C().paper ? { paper: C().paper } : {}) };
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
  screen(confetti(), el("div", { class: "done" }, el("div", { class: "done-title" }, `Lesson ${n} done`),
    para(Ln.paper_task ? `You completed ${completed} questions and a writing task.` : `You completed ${completed} questions.`, "done-sub")),
    next ? button(`Next: Lesson ${next}`, () => openLesson(s, next), "primary") : para(`You have done every ${SUBJECTS[s]} lesson. Well done!`, "strong"),
    button("Back to the lessons", menu, next ? "" : "primary"),
    para("For a grown-up: these results stay on this phone until you copy them.", "muted"),
    button("Copy results", () => copyText(text, status, details, area), ""), status, details);
}

// First visit: the readiness check. After that: straight to the lessons.
state.readiness ? menu() : start();
