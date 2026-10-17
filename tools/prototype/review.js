// Teacher review mode (2026-10-17): open the app with ?review in the link. A teacher sees every lesson with its answers
// shown, marks each part ✓ OK or ✗ Problem with an optional comment, then sends the review as one message
// (WhatsApp or any app, through the phone's share sheet, or copied). Marks are kept on this phone only; nothing is sent
// unless the teacher sends it. Pupils never see this mode. Every mark carries the item's id, so fixes are exact.
/* global ENGINE, CONTENT, TITLES, LESSONS, SUBJECTS, BUILD, MODE */

const REVIEW_KEY = "psalmspreps-review-v1";
const loadReview = () => {
  try { return { name: "", marks: {}, ...JSON.parse(localStorage.getItem(REVIEW_KEY)) }; } catch { return { name: "", marks: {} }; }
};
const review = loadReview();
const saveReview = () => { try { localStorage.setItem(REVIEW_KEY, JSON.stringify(review)); } catch { /* still works, just forgets */ } };
const markKey = (s, n, id) => `${s}:${n}:${id}`;
let RS = Object.keys(SUBJECTS)[0];  // subject shown in review mode

/** Every reviewable part of a lesson, in teaching order: note, cards (with their check), worked example, practice. */
function reviewItems(s, n) {
  const l = CONTENT[s][n];
  const items = [{ id: "note", kind: "Note (summary)" }];
  for (const c of l.teach.cards) items.push({ id: c.id, kind: "Teach card", card: c });
  items.push({ id: "worked", kind: "Worked example" });
  if (l.paper_task) items.push({ id: "paper", kind: "Writing task" });
  for (const t of l.questions || []) items.push({ id: t.id, kind: `Practice · level ${t.level}`, tpl: t });
  return items;
}
const lessonCounts = (s, n) => {
  const items = reviewItems(s, n), marks = items.map((it) => review.marks[markKey(s, n, it.id)]).filter(Boolean);
  return { total: items.length, done: marks.length, problems: marks.filter((m) => !m.ok).length };
};

/** One generated question with its answer and working shown. */
function shownQuestion(q, tpl) {
  const out = [el("div", { class: "prompt pre" }, q.prompt || ""), figureBox(q.figure)];
  if (q.sentence) out.push(el("div", { class: "sentence" }, q.sentence));
  if (q.options) {
    out.push(el("ul", { class: "rv-options" }, q.options.map((o, i) => el("li", { class: i === q.correctIndex ? "rv-right" : "" },
      `${i === q.correctIndex ? (q.type === "spot_error" ? "✗ (the wrong one) " : "✓ ") : "• "}${o.text}`,
      o.explain && i !== q.correctIndex ? el("div", { class: "muted" }, `Feedback if chosen: ${o.explain}`) : null))));
  } else if (q.type === "numeric") {
    out.push(para(`Answer: ${q.answer}${q.unit ? " " + q.unit : ""}`, "strong"),
      ...q.misconceptions.map((m) => para(`If the pupil types ${m.value}: ${m.explain}`, "muted")));
  } else if (q.type === "cloze") {
    out.push(para(`Accepted answer: ${q.accept.join(" or ")}`, "strong"), ...q.misconceptions.map((m) => para(`If the pupil types ${m.value}: ${m.explain}`, "muted")));
  } else if (q.type === "ordering" || q.type === "word_order") {
    out.push(para(`Shown mixed up: ${q.items.join(" · ")}`, "muted"), para(`Right answer: ${q.answer}`, "strong"));
  }
  out.push(el("div", { class: "example" }, el("div", { class: "kicker" }, "Working shown after a second miss"), el("ol", {}, q.solution.map((x) => el("li", {}, x)))));
  out.push(para(tpl.review === "rule" ? "Answer computed by the app’s rules." : "Answer written by a person: please check it.", "rv-tag"));
  return out;
}

/** The content of one item, generated with `seed` (a new seed shows another example of the same question). */
function itemBody(s, n, it, seed) {
  const l = CONTENT[s][n], lib = libs[s];
  if (it.id === "note") return [el("div", { class: "note" }, ...lines(l.note.text))];
  if (it.id === "worked") {
    const w = renderWorked(l.worked_example, lib);
    return [el("div", { class: "strong pre" }, w.problem), figureBox(w.figure), el("ol", {}, w.steps.map((x) => el("li", {}, x))), para(`Answer: ${w.answer}`, "strong")];
  }
  if (it.id === "paper") {
    const p = teach.renderPaper(l, lib);
    return [el("div", { class: "pre" }, p.prompt), el("div", { class: "kicker" }, "Model answer"), ...p.model.map((m) => para(m)),
      el("div", { class: "kicker" }, "Self-check list"), el("ul", {}, p.checklist.map((c) => el("li", {}, c)))];
  }
  if (it.card) {
    const c = teach.renderCard(it.card, lib), tpl = teach.cardCheckTemplate(l, it.card);
    return [el("div", { class: "idea" }, c.idea), cardExample(c), el("div", { class: "kicker" }, `Check question (${tpl.id})`),
      ...shownQuestion(template.instantiate(tpl, seed, lib, n), tpl)];
  }
  return shownQuestion(template.instantiate(it.tpl, seed, lib, n), it.tpl);
}

function reviewItem(s, n, it) {
  const key = markKey(s, n, it.id);
  let seed = 1;
  const box = el("section", { class: "rv-item" });
  const draw = () => {
    const m = review.marks[key];
    const note = el("textarea", { rows: "2", class: "rv-note", placeholder: "Comment (what is wrong, or the correction)", "aria-label": `Comment on ${it.id}` });
    note.value = m?.note || "";
    const mark = (ok) => { review.marks[key] = { ok, note: note.value.trim(), at: new Date().toISOString() }; saveReview(); draw(); };
    note.addEventListener("change", () => { if (review.marks[key]) { review.marks[key].note = note.value.trim(); saveReview(); } });
    box.className = `rv-item${m ? (m.ok ? " rv-is-ok" : " rv-is-bad") : ""}`;
    fill(box, [
      el("div", { class: "rv-head" }, el("span", { class: "kicker" }, it.kind), el("code", {}, it.id)),
      ...itemBody(s, n, it, seed),
      it.tpl || it.card ? button("Show another example", () => { seed += 1; draw(); }, "link") : null,
      note,
      el("div", { class: "rv-buttons" }, button("✓ OK", () => mark(true), m?.ok === true ? "primary" : ""), button("✗ Problem", () => mark(false), m?.ok === false ? "rv-bad-on" : "")),
      m ? para(m.ok ? "Marked OK." : "Marked as a problem.", "muted") : null,
    ]);
  };
  draw();
  return box;
}

function reviewLesson(s, n) {
  if (!CONTENT[s]) return withSubject(s, () => reviewLesson(s, n));
  const c = lessonCounts(s, n);
  screen(header(`Review · ${SUBJECTS[s]} · Lesson ${n}`, TITLES[s][n]),
    para(`${c.done} of ${c.total} parts checked${c.problems ? ` · ${c.problems} problem${c.problems === 1 ? "" : "s"}` : ""}. Answers are shown. Mark each part, and add a comment when something is wrong.`, "muted"),
    reviewItems(s, n).map((it) => reviewItem(s, n, it)),
    button("Back to the review list", reviewHome, "primary"));
}

/** The message a teacher sends: every problem with its comment, then the OKs counted per lesson. */
function reviewText() {
  const out = [`Psalms Preps teacher review · ${review.name || "(name not given)"} · app ${BUILD} · ${new Date().toISOString().slice(0, 16).replace("T", " ")}`];
  // In the installed app only the subjects opened so far are on the phone: skip the others (sendReview loads every
  // subject that has marks before building the text).
  for (const s of Object.keys(SUBJECTS).filter((x) => CONTENT[x])) for (const n of LESSONS[s]) {
    const items = reviewItems(s, n).map((it) => [it, review.marks[markKey(s, n, it.id)]]).filter(([, m]) => m);
    if (!items.length) continue;
    const ok = items.filter(([, m]) => m.ok);
    out.push("", `${SUBJECTS[s]} Lesson ${n} (${TITLES[s][n]}): ${items.length} of ${reviewItems(s, n).length} checked, ${items.length - ok.length} problem(s)`);
    for (const [it, m] of items) if (!m.ok || m.note) out.push(`  ${m.ok ? "✓" : "✗"} ${s}:${n}:${it.id}${m.note ? ` — ${m.note}` : ""}`);
  }
  return out.join("\n");
}

async function sendReview(status) {
  const marked = [...new Set(Object.keys(review.marks).map((k) => k.split(":")[0]))].filter((s) => SUBJECTS[s]);
  try { await loadAll(marked); } catch { status.textContent = "Connect to the internet once, then send again."; return; }
  const text = reviewText();
  try {
    if (navigator.share) { await navigator.share({ title: "Teacher review", text }); status.textContent = "Shared."; return; }
  } catch { /* cancelled or not allowed: fall back to copying */ }
  try { await navigator.clipboard.writeText(text); status.textContent = "Copied. Paste it into WhatsApp or a message to Dion."; }
  catch { status.textContent = "Could not copy: select the text below and copy it."; }
}

function reviewHome() {
  if (!CONTENT[RS]) return withSubject(RS, reviewHome);
  // the subjects this teacher has marked are loaded too, so the review text below is complete
  const missing = [...new Set(Object.keys(review.marks).map((k) => k.split(":")[0]))].find((s) => SUBJECTS[s] && !CONTENT[s]);
  if (missing) return withSubject(missing, reviewHome);
  document.documentElement.lang = "en";
  const name = el("input", { type: "text", class: "rv-name", placeholder: "Your name", "aria-label": "Your name", autocomplete: "name" });
  name.value = review.name;
  name.addEventListener("change", () => { review.name = name.value.trim(); saveReview(); });
  const tabs = el("div", { class: "subjects", role: "tablist" }, Object.entries(SUBJECTS).map(([id, label]) =>
    el("button", { type: "button", role: "tab", "aria-selected": String(id === RS), class: `subject${id === RS ? " on" : ""}`, onclick: () => { RS = id; reviewHome(); } }, label)));
  const rows = LESSONS[RS].map((n) => {
    const c = lessonCounts(RS, n);
    const mark = c.done === c.total ? (c.problems ? "!" : "✓") : c.done ? "…" : String(n);
    return el("button", { type: "button", class: `lesson${c.done === c.total && !c.problems ? " is-done" : ""}`, onclick: () => reviewLesson(RS, n) },
      el("span", { class: "mark", "aria-hidden": "true" }, mark),
      el("span", { class: "lt" }, el("span", { class: "ln" }, `Lesson ${n}`), TITLES[RS][n],
        el("span", { class: "sub" }, `${c.done} of ${c.total} checked${c.problems ? ` · ${c.problems} problem${c.problems === 1 ? "" : "s"}` : ""}`)));
  });
  const status = para("", "muted");
  const area = el("textarea", { readonly: "", rows: "8", "aria-label": "Review text" });
  area.value = reviewText();
  screen(header("Teacher review", "Check the lessons"),
    para("Thank you for reviewing. Open a lesson: every answer is shown. Mark each part ✓ OK or ✗ Problem, and write a comment when something is wrong. Your marks stay on this phone until you send them.", "muted"),
    name, tabs, el("div", { class: "lessons" }, rows),
    button("Send my review", () => sendReview(status), "primary"), status,
    el("details", { class: "grownup" }, el("summary", {}, "Show the review text"), area),
    button("Open the app as a pupil", () => { location.href = location.pathname; }, "link"));
}

// Start: teachers open the link with ?review; everyone else gets the pupil's lesson menu.
if (new URLSearchParams(location.search).has("review")) reviewHome(); else home();
