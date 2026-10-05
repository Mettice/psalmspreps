// Prototype UI: Lesson 0 readiness (once) → lesson menu (Lessons 1–16) → teach mode (cards, worked example,
// practice, note) → results. Uses the real engine (inlined by build.mjs).
// Progress is saved in this browser only (localStorage, decision 2026-10-05); nothing is sent anywhere.
/* global ENGINE, CONTENT, TITLES, LESSONS, BUILD */
const { lib, template, teach, readiness } = ENGINE;
const { check, DONT_KNOW, renderWorked, normaliseInput, inputModeFor } = template;
const L0 = CONTENT[0];

// ---------------------------------------------------------------- saved progress (this browser only)
// { v, readiness: {score, rows, at} | null, lessons: {n: {done, at, rows, review}}, current: {lesson, flow} | null }
const KEY = "psalmspreps-maths-v1";
const fresh = () => ({ v: 1, readiness: null, lessons: {}, current: null });
function load() {
  try {
    const s = JSON.parse(localStorage.getItem(KEY));
    return s && s.v === 1 ? { ...fresh(), ...s } : fresh();
  } catch { return fresh(); }  // private mode, blocked storage or a broken value: start fresh
}
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch { /* still works, just forgets */ } };
const state = load();
const newSeed = () => Math.floor(Math.random() * 1e6);  // a new set of numbers each time a lesson starts

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
const button = (label, onclick, cls = "") => el("button", { class: cls, onclick }, label);
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
/** Shows q; calls onAnswer({result, ms}) when the pupil answers or presses "I don't know". */
function askQuestion(q, { kicker, title, onAnswer, bar = null, back = null }) {
  const t0 = performance.now();
  const finish = (response) => onAnswer({ result: check(q, response), ms: Math.round(performance.now() - t0) });
  const body = [bar, header(kicker, title), el("div", { class: "prompt" }, q.prompt)];
  if (q.type === "numeric") {
    const input = el("input", { type: "text", inputmode: inputModeFor(q), autocomplete: "off", autocorrect: "off", spellcheck: "false", "aria-label": "Your answer" });
    const go = () => { const v = normaliseInput(input.value, q); if (v) finish(v); };
    input.addEventListener("keydown", (e) => e.key === "Enter" && go());
    body.push(el("div", { class: "answer" }, input, q.unit ? el("span", { class: "unit" }, q.unit) : null), button("Check", go, "primary"));
    setTimeout(() => input.focus(), 50);
  } else if (q.type === "mcq" || q.type === "spot_error") {
    if (q.type === "spot_error") body.push(para("Tap the one that is wrong.", "muted"));
    body.push(el("div", { class: "options" }, q.options.map((o, i) => button(o.text, () => finish(i), "option"))));
  } else if (q.type === "ordering") {
    const chosen = [];
    const list = el("ol", { class: "chosen" });
    const pool = el("div", { class: "options" });
    const redraw = () => {
      list.replaceChildren(...chosen.map((i) => el("li", {}, q.items[i])));
      pool.replaceChildren(...q.items.map((t, i) => (chosen.includes(i) ? null : button(t, () => { chosen.push(i); redraw(); }, "option"))));
      if (chosen.length === q.items.length) finish([...chosen]);
    };
    body.push(para("Tap them in order.", "muted"), list, pool, button("Start again", () => { chosen.length = 0; redraw(); }, "link"));
    redraw();
  }
  body.push(button("I don't know", () => finish(DONT_KNOW), "idk"), back);
  screen(...body);
}

const recordOf = (q, r, ms, phase) => ({
  phase, id: q.id, level: q.level, result: r.correct ? "right" : r.dontKnow ? "idk" : "wrong",
  seconds: Math.round(ms / 100) / 10, misconception: r.misconception?.id || "",
});
const toMenu = () => button("Back to the lessons", menu, "link");

// ---------------------------------------------------------------- 1. first visit: readiness check
function start() {
  screen(
    header("Form One Maths", "Before we start"),
    ...lines(L0.note.text),
    para("Nothing you type leaves this phone. There is no name to enter.", "muted"),
    button("Start the check", () => readinessQ(readiness.buildReadiness(L0, newSeed(), lib), 0, []), "primary"),
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
    para("Now we begin Form One Maths, one small idea at a time."),
    button("See the lessons", menu, "primary"),
  );
}

// ---------------------------------------------------------------- 2. lesson menu
const nextLesson = () => LESSONS.find((n) => !state.lessons[n]?.done);

function menu() {
  const cur = state.current, next = nextLesson();
  const done = LESSONS.filter((n) => state.lessons[n]?.done).length;
  const row = (n) => {
    const s = state.lessons[n], inProgress = cur?.lesson === n;
    const mark = s?.done ? "✓" : inProgress ? "…" : String(n);
    const sub = s?.done ? "Done · tap to practise again" : inProgress ? "Started · tap to carry on" : "";
    return el("button", { class: `lesson${s?.done ? " is-done" : ""}`, onclick: () => openLesson(n) },
      el("span", { class: "mark", "aria-hidden": "true" }, mark),
      el("span", { class: "lt" }, el("span", { class: "ln" }, `Lesson ${n}`), TITLES[n], sub ? el("span", { class: "sub" }, sub) : null));
  };
  const lead = cur && !teach.isDone(cur.flow)
    ? button(`Carry on with Lesson ${cur.lesson}`, () => openLesson(cur.lesson), "primary")
    : next ? button(`Start Lesson ${next}: ${TITLES[next]}`, () => openLesson(next), "primary") : null;
  screen(
    header("Form One Maths", done ? `${done} of ${LESSONS.length} lessons done` : "Your lessons"),
    lead,
    el("div", { class: "lessons" }, LESSONS.map(row)),
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

/** Opens lesson n: carries on a saved, unfinished flow, otherwise starts it fresh. */
function openLesson(n) {
  const cur = state.current;
  if (cur?.lesson === n && !teach.isDone(cur.flow)) return lesson(resumable(cur.flow));
  state.current = { lesson: n, flow: teach.startTeach(CONTENT[n], newSeed()), rows: [] };
  save();
  lesson(state.current.flow);
}
/** A flow saved mid-feedback resumes on a question: "retry" → the fresh variant, "reveal" → the next step. */
const resumable = (flow) => (flow.phase === "retry" || flow.phase === "reveal" ? teach.nextPhase(flow) : flow);

// ---------------------------------------------------------------- 3. teach mode
const L = () => CONTENT[state.current.lesson];
const N = () => state.current.lesson;
const workedBlock = () => {
  const w = renderWorked(L().worked_example, lib);
  return el("div", { class: "example" }, el("div", { class: "kicker" }, "Worked example"), para(w.problem, "strong"),
    el("ol", {}, w.steps.map((s) => el("li", {}, s))), para(`Answer: ${w.answer}`, "strong"));
};
const cardExample = (c) => el("div", { class: "example" }, el("div", { class: "kicker" }, "Example"), ...c.example.map((t) => para(t)));
const hintBlock = (q) => (q.hint ? el("div", { class: "hint" }, el("strong", {}, "Hint: "), q.hint) : null);

/** Every screen of a lesson goes through here, so the flow is saved at each step. */
function lesson(flow, previous = null) {
  state.current.flow = flow;
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
    const c = teach.renderCard(Ln.teach.cards[step.card], lib);
    return screen(bar, header(kicker, TITLES[n]), el("div", { class: "idea" }, c.idea), cardExample(c),
      button("I'm ready for a question", go(teach.nextPhase(flow)), "primary"), toMenu());
  }
  if (step.kind === "card" || step.kind === "practice") {
    const q = teach.itemQuestion(Ln, flow, lib, previous);
    return askQuestion(q, {
      bar, kicker, back: toMenu(), title: flow.attempt ? "A new question" : step.kind === "card" ? "Quick check" : `Level ${q.level}`,
      onAnswer: ({ result, ms }) => {
        state.current.rows.push({ ...recordOf(q, result, ms, step.kind), card: step.kind === "card" ? Ln.teach.cards[step.card].id : "", attempt: flow.attempt + 1 });
        const next = teach.answerItem(flow, result, ms);
        state.current.flow = next;
        save();
        if (next.phase === "reveal") return reveal(q, next, kicker, bar, result);
        if (next.phase === "retry") return retry(q, result, next, kicker, bar);
        // Teach mode only: green flash + check icon (readiness shows no right/wrong cues).
        return screen(bar, el("div", { class: "fb good flash", role: "status" }, checkIcon(), el("strong", {}, "Correct!")), button("Next", go(next), "primary"));
      },
    });
  }
  if (step.kind === "worked_example") {
    return screen(bar, header(`Lesson ${n} · Worked example`, "Follow each step"), workedBlock(), button("Now practise", go(teach.nextPhase(flow)), "primary"), toMenu());
  }
  if (step.kind === "note") {
    return screen(bar, header(`Lesson ${n} · Summary`, TITLES[n]), el("div", { class: "note" }, ...lines(Ln.note.text)),
      button("Finish", go(teach.nextPhase(flow)), "primary"));
  }
}

/** First miss: feedback without the answer, then a fresh variant. */
function retry(q, result, flow, kicker, bar) {
  const step = flow.steps[flow.step];
  const box = result.dontKnow
    // "I don't know": no misconception feedback, only the hint and the worked example (spec §4)
    ? el("div", { class: "fb soft", role: "status" }, el("strong", {}, "That's fine. Let's look at it together."))
    : el("div", { class: "fb bad shake", role: "status" }, el("strong", {}, "✗ Not quite"),
      result.misconception?.explain ? para(result.misconception.explain) : para("Look at the example again, then try a new question."));
  const help = step.kind === "card"
    ? [result.dontKnow ? hintBlock(q) : null, cardExample(teach.renderCard(L().teach.cards[step.card], lib))]
    : result.dontKnow ? [hintBlock(q), workedBlock()] : [];
  screen(bar, header(kicker, "Let's try again"), box, ...help, button("Try a new question", () => lesson(teach.nextPhase(flow), q), "primary"));
}

/** Second miss: the correct answer with full working, then move on (marked "needs review"). */
function reveal(q, flow, kicker, bar, result) {
  screen(bar, header(kicker, "Here is how to do it"),
    el("div", { class: result.dontKnow ? "fb soft" : "fb bad shake", role: "status" }, el("strong", {}, `The answer is: ${q.answer}${q.unit ? " " + q.unit : ""}`)),
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
function lessonText(n, s) {
  const cards = s.rows.filter((r) => r.phase === "card"), practice = s.rows.filter((r) => r.phase === "practice");
  const secs = s.rows.reduce((t, r) => t + r.seconds, 0);
  return [`Lesson ${n} (${TITLES[n]}) · ${s.at.slice(0, 16).replace("T", " ")} · ${Math.round(secs)}s · "I don't know" ${count(s.rows, "idk")}`,
    `  cards: ${count(cards, "right")} right, ${count(cards, "wrong")} wrong, ${count(cards, "idk")} IDK · practice: ${count(practice, "right")} right, ${count(practice, "wrong")} wrong, ${count(practice, "idk")} IDK`,
    `  needs review (missed twice): ${s.review.join(", ") || "none"}`];
}
const stamp = () => `Form One Maths prototype ${BUILD} · ${new Date().toISOString().slice(0, 16).replace("T", " ")}`;

function lessonResultsText(n) {
  const s = state.lessons[n];
  return [stamp(), ...readinessText(), ...lessonText(n, s), "", TABLE_HEAD, ...s.rows.map(row)].join("\n");
}
function allResultsText() {
  const done = LESSONS.filter((n) => state.lessons[n]?.done);
  return [stamp(), ...readinessText(), `Lessons done: ${done.length} of ${LESSONS.length}`, ...done.flatMap((n) => lessonText(n, state.lessons[n])),
    "", TABLE_HEAD, ...(state.readiness?.rows || []).map(row), ...done.flatMap((n) => state.lessons[n].rows.map(row))].join("\n");
}

async function copyText(text, status, details = null, area = null) {
  try { await navigator.clipboard.writeText(text); status.textContent = "Copied. Paste it into WhatsApp or a message."; }
  catch {
    if (details && area) { details.open = true; area.select(); document.execCommand("copy"); status.textContent = "Copied (or select the text below and copy it)."; }
    else status.textContent = "Could not copy on this phone.";
  }
}

function results(flow) {
  const n = N(), Ln = L();
  const review = teach.needsReview(flow).map((s) => (s.kind === "card" ? Ln.teach.cards[s.card].id : s.template));
  // The latest finished run of a lesson replaces the previous one.
  state.lessons[n] = { done: true, at: new Date().toISOString(), rows: state.current.rows, review };
  state.current = null;
  save();
  const text = lessonResultsText(n);
  const area = el("textarea", { readonly: "", rows: "10", "aria-label": "Results" });
  // The text holds the readiness score and weak areas, so it stays folded away from the pupil (TR-C30).
  const details = el("details", { class: "grownup" }, el("summary", {}, "Show the text (for a grown-up)"), area);
  area.value = text;
  const status = para("", "muted");
  const completed = flow.steps.filter((s) => s.kind === "card" || s.kind === "practice").length;
  const next = nextLesson();
  screen(confetti(), el("div", { class: "done" }, el("div", { class: "done-title" }, `Lesson ${n} done`),
    para(`You completed ${completed} questions.`, "done-sub")),
    next ? button(`Next: Lesson ${next}`, () => openLesson(next), "primary") : para("You have done every lesson. Well done!", "strong"),
    button("Back to the lessons", menu, next ? "" : "primary"),
    para("For a grown-up: these results stay on this phone until you copy them.", "muted"),
    button("Copy results", () => copyText(text, status, details, area), ""), status, details);
}

// First visit: the readiness check. After that: straight to the lessons.
state.readiness ? menu() : start();
