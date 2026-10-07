// Renders a subject batch for review (English E1, Physics P1, …):
//   content/{subject}/REVIEW.md    a sample lesson in teach mode, then every draft (cards, worked examples, practice, paper tasks)
//   content/{subject}/AUTHORED.md  every answer fixed by a person (keys, tables, statement pools), with sources
//   content/{subject}/figures/     the drawings (SVG) shown in REVIEW.md
//   node tools/content/render_subject.mjs english|physics|chemistry|geography   (npm run review:<subject>)
// Everything shown is produced by the engine itself, so the reviewer sees exactly what pupils will see.
import { readFileSync, readdirSync, writeFileSync, mkdirSync, rmSync } from "node:fs";
import * as maths from "../../src/engine/lib/maths.js";
import * as english from "../../src/engine/lib/english.js";
import * as physics from "../../src/engine/lib/physics.js";
import * as chemistry from "../../src/engine/lib/chemistry.js";
import * as geography from "../../src/engine/lib/geography.js";
import * as homeeconomics from "../../src/engine/lib/homeeconomics.js";
import { render } from "../../src/engine/expr.js";
import { instantiate, renderWorked } from "../../src/engine/template.js";
import { renderCard, cardCheckTemplate, practicePlan, renderPaper, isDeferred } from "../../src/engine/teach.js";

const SUBJECT = process.argv[2];
const CONF = {
  english: { name: "English", batch: "Batch E1", spine: "english-language", lib: { ...maths, ...english }, sample: 3, lessons: "1–16" },
  physics: { name: "Physics", batch: "Batch P1", spine: "physics", lib: { ...maths, ...english, ...physics }, sample: 16, lessons: "1–19" },
  chemistry: { name: "Chemistry", batch: "Batch C1", spine: "chemistry", lib: { ...maths, ...english, ...physics, ...chemistry }, sample: 20, lessons: "1–21" },
  // Geography is numbered by place in the year (spine seq): PW1–PW3 have no lesson number on the sheet.
  geography: { name: "Geography", batch: "Batch G1", spine: "geography", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography }, sample: 8, lessons: "1–10", bySeq: true },
  "home-economics": { name: "Home Economics", batch: "Batch H1", spine: "home-economics", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics }, sample: 13, lessons: "1–7, 10–17, 20–21" },
}[SUBJECT];
if (!CONF) throw new Error("usage: node tools/content/render_subject.mjs english|physics|chemistry|geography|home-economics");
const lib = CONF.lib;
const DIR = new URL(`../../content/${SUBJECT}/`, import.meta.url);
// Drawings are saved as files (GitHub does not show SVG written inside Markdown).
const FIG = new URL("figures/", DIR);
rmSync(FIG, { recursive: true, force: true });
let figCount = 0;
const figure = (svg, name) => {
  if (!svg) return [];
  mkdirSync(FIG, { recursive: true });
  const file = `${name}-${++figCount}.svg`;
  writeFileSync(new URL(file, FIG), svg.replace(/currentColor/g, "#222"), "utf8");
  return [`![drawing](figures/${file})`, ""];
};
const lessons = readdirSync(DIR).filter((f) => /^\d+\.json$/.test(f))
  .map((f) => JSON.parse(readFileSync(new URL(f, DIR), "utf8"))).sort((a, b) => a.lesson_no - b.lesson_no);
const sources = JSON.parse(readFileSync(new URL("sources.json", DIR), "utf8"));
const spine = JSON.parse(readFileSync(new URL(`../../data/spine/${CONF.spine}.json`, import.meta.url), "utf8"));
const meta = Object.fromEntries(spine.terms.flatMap((t) => t.lessons).map((l) => [CONF.bySeq ? l.seq : l.lesson_no, l]));
const SAMPLE_LESSON = CONF.sample, SAMPLE_SEED = 2026;
const quote = (t) => String(t).split("\n").map((l) => `> ${l}`).join("\n");
const TYPE_NAME = { numeric: "number", mcq: "multiple choice", spot_error: "spot the error", ordering: "ordering", cloze: "fill the blank", word_order: "word order", matching: "matching" };

function renderQuestion(q) {
  const out = [quote(q.prompt), "", ...figure(q.figure, q.id)];
  if (q.type === "cloze") {
    out.push(`Sentence: **${q.sentence}**`);
    if (q.mode === "choose") q.options.forEach((o, i) => out.push(`- ${i === q.correctIndex ? "✅" : "◻️"} ${o.text}${o.explain ? `  \n  _↳ feedback if chosen: ${o.explain}_` : ""}`));
    else {
      out.push(`Typed answer accepted (case and extra spaces ignored): ${q.accept.map((a) => `**${a}**`).join(" or ")}`);
      for (const m of q.misconceptions) out.push(`- Typed **${m.value}** (${m.id}) → “${m.explain}”`);
    }
  } else if (q.options) {
    q.options.forEach((o, i) => out.push(`- ${i === q.correctIndex ? "✅" : "◻️"} ${o.text}${o.explain ? `  \n  _↳ ${q.type === "spot_error" ? "explanation" : "feedback if chosen"}: ${o.explain}_` : ""}`));
  } else if (q.type === "word_order") {
    out.push(`Tiles: ${q.items.join(" · ")}${q.end ? ` (then “${q.end}”)` : ""}`, `Answer: **${q.answer}**`);
  } else if (q.type === "ordering") {
    out.push(`Shown as: ${q.items.join(" · ")}`, `Correct order: ${q.answer}`);
  } else if (q.type === "matching") {
    out.push(`${q.groups ? "Groups" : "Right-hand side (shuffled)"}: ${q.right.join(" · ")}`, ...q.left.map((l, i) => `- ${l} → **${q.right[q.correctMatch[i]]}**`));
  }
  if (q.type === "numeric") {
    out.push(`Answer: **${q.answer}${q.unit ? " " + q.unit : ""}**`);
    for (const m of q.misconceptions) out.push(`- Typed **${m.value}** (${m.id}) → “${m.explain}”`);
  }
  if (q.hint) out.push("", `Hint (draft): ${q.hint}`);
  if (q.solution) out.push("", "Full working after a second miss:", "", ...q.solution.map((x) => `> ${x}  `));
  return out.join("\n");
}
const tplHead = (t, extra = "") => `\`${t.id}\` · ${TYPE_NAME[t.type]}, level ${t.level} · ${t.review === "authored" ? "**authored key**" : "computed by rule"}${extra}`;
const cardBlock = (l, c, seed) => {
  const r = renderCard(c, lib);
  const tpl = cardCheckTemplate(l, c);
  return [`**Card ${c.id}** (draft)`, "", `> ${r.idea}`, ">", ...r.example.map((x) => `> _${x}_  `), "", ...figure(r.figure, c.id),
    `Check question: ${tplHead(tpl, c.check.ref ? ", reused from practice" : "")}`, "", renderQuestion(instantiate(tpl, seed, lib, l.lesson_no)), ""];
};
const workedBlock = (l) => {
  const w = renderWorked(l.worked_example, lib);
  return ["**Worked example** (draft)", "", quote(w.problem), "", ...figure(w.figure, `worked-${l.lesson_no}`), ...w.steps.map((s, i) => `${i + 1}. ${s}`), "", `**Answer:** ${w.answer}`, ""];
};
const paperBlock = (l) => {
  const p = renderPaper(l, lib);
  return ["**Paper task** (draft; not marked by the app, mastery stays unknown)", "", quote(p.prompt), "", "Model answer, shown after the pupil has written:", "",
    ...p.model.map((m) => `> ${m}  `), "", "Self-check list:", "", ...p.checklist.map((c) => `- [ ] ${c}`), ""];
};

// ---------------------------------------------------------------- REVIEW.md
const R = [`# ${CONF.name} Form 1, ${CONF.batch}: drafts for review (Lessons ${CONF.lessons})`, "",
  `Generated by \`npm run review:${SUBJECT}\` from \`content/${SUBJECT}/*.json\`. Every question and drawing below was built by the engine.`,
  "All notes, teach cards, worked examples and paper tasks are **status: draft**. “Authored key” means a person fixed the",
  "right answer (see `AUTHORED.md`); “computed by rule” means code worked it out (a formula, a conversion, a spelling rule).", "",
  "Teach mode: cards (idea + example + 1 level-1 check) → worked example → practice (levels 1–3) → the note as a summary.",
  ...(SUBJECT === "english" ? ["Writing lessons replace practice with a paper task. Speech-work lessons are deferred (they need audio).", ""] : [""]),
  `## Sample rendered lesson: Lesson ${SAMPLE_LESSON} in teach mode`, ""];
const sample = lessons.find((l) => l.lesson_no === SAMPLE_LESSON);
R.push(`### Lesson ${SAMPLE_LESSON}: ${meta[SAMPLE_LESSON].title}`, "");
sample.teach.cards.forEach((c, i) => R.push(...cardBlock(sample, c, SAMPLE_SEED + i)));
R.push(...workedBlock(sample), "**Practice** (one generated question per template, easiest first)", "");
practicePlan(sample).forEach((id, i) => {
  const t = sample.questions.find((x) => x.id === id);
  R.push(`Practice ${i + 1}: ${tplHead(t)}`, "", renderQuestion(instantiate(t, SAMPLE_SEED + 50 + i, lib, SAMPLE_LESSON)), "");
});
R.push("**Summary (the note)**", "", quote(sample.note.text), "", "## All drafts", "");
R.push("| Lesson | Title (sheet) | Status | Cards | Practice | Paper task |", "|---|---|---|---|---|---|");
for (const l of lessons) {
  R.push(`| ${l.lesson_no} | ${meta[l.lesson_no].title} | ${isDeferred(l) ? "**deferred** (speech work: needs audio; hidden, not in coverage)" : "draft"} | ${l.teach?.cards.length ?? "—"} | ${l.questions?.length ?? "—"} | ${l.paper_task ? "yes" : "—"} |`);
}
R.push("");
for (const l of lessons) {
  R.push(`## Lesson ${l.lesson_no}: ${meta[l.lesson_no].title}`, "");
  if (isDeferred(l)) { R.push(`**Deferred.** ${l.deferred_reason}`, ""); continue; }
  R.push(`Prerequisites: ${l.prerequisites.join(", ") || "none"} · Skill: ${l.skills.map((s) => `${s.id} (${s.name})`).join(", ")}`, "", "**Note** (draft)", "", quote(l.note.text), "");
  l.teach.cards.forEach((c, i) => R.push(...cardBlock(l, c, 7 + i)));
  R.push(...workedBlock(l));
  if (l.paper_task) R.push(...paperBlock(l));
  for (const t of l.questions) {
    R.push(`**Practice** ${tplHead(t)}`, "");
    for (const seed of [3, 41]) R.push(renderQuestion(instantiate(t, seed, lib, l.lesson_no)), "");
  }
}
writeFileSync(new URL("REVIEW.md", DIR), R.join("\n") + "\n", "utf8");

// ---------------------------------------------------------------- AUTHORED.md
const show = (v) => (typeof v === "number" ? maths.fmt(v) : String(v));
const rend = (t, scope = {}) => render(t, scope, lib, show);
const PART1 = {
  chemistry: () => ["## Part 1: tables and rules the computed answers use (src/engine/lib/chemistry.js, physics.js)", "",
    "**Elements (TR-K02)**: atomic number, symbol, name, kind.", "",
    "| Z | Symbol | Name | Kind |", "|---|---|---|---|", ...chemistry.ELEMENTS.map((e) => `| ${e.z} | ${e.symbol} | ${e.name} | ${e.kind} |`), "",
    `**Symbols from Latin (TR-K02)**: ${Object.entries(chemistry.LATIN).map(([s, l]) => `${s} (${l})`).join(", ")}.`, "",
    "- **Formulas (TR-K03)**: the small number after a symbol counts the atoms of that symbol; no number means one; a bracket multiplies everything inside it (Ca(OH)₂: 1 Ca, 2 O, 2 H). Counted by `parseFormula()`, tested on known answers.",
    "- **Measurement**: the unit conversions, °C → K (+ 273), the measuring cylinder and thermometer drawings are the same as in Physics (TR-P04, TR-P05, TR-P08).", ""],
  "home-economics": () => ["## Part 1: the rule and drawings the answers use (src/engine/lib/homeeconomics.js)", "",
    `- **Work triangle (TR-H01)**: the path sink → cooker → fridge → sink. Total = the three sides added. Well planned when every side is ${homeeconomics.sideMin()} m to ${homeeconomics.sideMax()} m and the total is ${homeeconomics.totalMin()} m to ${homeeconomics.totalMax()} m. The reason shown: ${["1.8, 2.1, 2.4", "3.2, 2, 2", "0.9, 2, 2", "2.6, 2.7, 2.7", "1.2, 1.3, 1.4"].map((t) => { const [a, b, c] = t.split(", ").map(Number); return `${t} m → “${homeeconomics.triangleVerdict(a, b, c)}”`; }).join("; ")}. Practice sides run from 0.9 m to 3.2 m.`,
    `- **Drawings with lettered parts (TR-H02)**: traditional kitchen (${homeeconomics.TRAD_PARTS.join(", ")}); fireplaces (${homeeconomics.FIRE_TYPES.join(", ")}); kitchen front (${homeeconomics.UNIT_PARTS.join(", ")}); kitchen shapes seen from above (${homeeconomics.SHAPES.join(", ")}). The letters are shuffled by the question's numbers; the code that draws a letter also gives the answer.`, ""],
  geography: () => ["## Part 1: tables and rules the computed answers use (src/engine/lib/geography.js)", "",
    "- **Local time (TR-G01)**: 360° in 24 hours, so 15° = 1 hour and 1° = 4 minutes; east of a place is ahead (add), west is behind (subtract). Difference in longitude: same side of 0°, subtract; opposite sides, add. Questions stay within one day (no midnight crossed).",
    `- **Clock style (TR-G01)**: 12-hour times: ${[0, 30, 545, 720, 860].map(geography.clock).join(", ")}.`,
    `- **Time zones (TR-G08)**: standard meridians are multiples of 15°: ${[-30, -15, 0, 15, 45].map((d) => `${geography.lon(d)} → ${geography.zone(d)}`).join(", ")}. Cameroon uses ${geography.zone(15)} (West Africa Time).`,
    `- **Main parallels (TR-G02)**: ${geography.PARALLELS.map(([n, d]) => `${n} ${geography.halfLat(d)}`).join(", ")}.`,
    "- **Positions (TR-G05)**: latitude first, then longitude, each with N/S or E/W (4°N, 12°E); 0° has no letter.",
    "- **Grid references (TR-G06)**: a 4-figure reference names the square by the easting on its left and the northing below it, easting first; a 6-figure reference adds tenths across and up (253347).",
    "- **Map scale (TR-G07)**: real km = map cm × scale number ÷ 100 000; map cm = km × 100 000 ÷ scale number. Scales used: 1 : 25 000, 50 000, 100 000, 200 000, 250 000, 500 000.",
    "- **Leap years (TR-G09)**: the Form 1 rule, divisible by 4; only years 2001–2099 are used, where it agrees with the full calendar rule.", "",
    "**Planets (TR-G03)**, in order from the Sun, average distance in millions of km:", "",
    "| # | Planet | Distance |", "|---|---|---|", ...[0, 1, 2, 3, 4, 5, 6, 7].map((i) => `| ${i + 1} | ${geography.planetName(i)} | ${geography.planetDistance(i)} |`), "",
    "**Continents and oceans (TR-G04)**, largest first, area in millions of km² (rounded; only the order is used in questions):", "",
    "| Continent | Area | | Ocean | Area |", "|---|---|---|---|---|",
    ...[0, 1, 2, 3, 4, 5, 6].map((i) => `| ${geography.continentName(i)} | ${geography.continentArea(i)} | | ${i < 5 ? geography.oceanName(i) : ""} | ${i < 5 ? geography.oceanArea(i) : ""} |`), ""],
  physics: () => ["## Part 1: conventions and rules the computed answers use (src/engine/lib/physics.js)", "",
    "- **g = 10 N/kg on Earth (TR-P03)**; on the Moon about 1.6 N/kg. Weight = mass × g.",
    "- **T(K) = T(°C) + 273 (TR-P04)**; 0 °C = 273 K; 100 °C = 373 K; a change of 1 °C is a change of 1 K.",
    "- **Unit ladders (TR-P05)**: length km hm dam m dm cm mm; mass t (= 1000 kg) kg hg dag g dg cg mg; capacity kL hL daL L dL cL mL; 1 L = 1 dm³ = 1000 cm³; 1 m³ = 1000 L; 1 mL = 1 cm³; time 1 h = 60 min = 3600 s.",
    "- **Density (TR-P06)**: density = mass ÷ volume, shown to 2 decimals; water 1 g/cm³; 1 g/cm³ = 1000 kg/m³; floats if less than 1 g/cm³.",
    "- **Changes of state (TR-P07)**: melting, freezing, evaporation, condensation, sublimation (solid → gas), deposition (gas → solid); heat is taken in going solid → liquid → gas and given out the other way.",
    "- **Drawings (TR-P08)**: rulers (0–15 cm, mm marks), measuring cylinders (marks every 2 mL, numbers every 10 mL, read at the bottom of the meniscus), thermometers (0–50 °C, marks every 1 °C) are drawn by code from the question's own numbers; tests check that each drawing shows exactly the reading.", ""],
  english: () => ["## Part 1: word tables and rules (src/engine/lib/english.js)", "",
    "**Irregular verbs (TR-E01)**: base → simple past → past participle", "",
  "| Verb | Simple past | Past participle |", "|---|---|---|",
  ...Object.entries(english.IRREGULAR).map(([v, [p, pp]]) => `| ${v} | ${p} | ${pp} |`), "",
  "**Spelling rules (TR-E02, TR-E03)**, checked on known answers in `tests-js/english.test.js`:", "",
  "- he/she/it form: add -es after s, sh, ch, x, z, o (washes, goes); consonant + y → -ies (carries); have → has.",
  "- -ing: ie → ying (lying); drop a final e after a consonant (making), but see → seeing, be → being; double the last consonant (below).",
  "- -ed: a final e adds -d (liked); consonant + y → -ied (carried); double the last consonant (below).",
  "- Doubling: one-syllable verbs ending consonant + one vowel + consonant (not w, x, y): stop → stopped, run → running.",
  "  Two-syllable verbs stressed on the last syllable: admit, begin, commit, control, forget, occur, permit, prefer, refer, regret, submit, upset.",
  "  British English also doubles a final l after one vowel: travel → travelled, cancel → cancelled.",
  "  Never doubled: visit, open, listen, happen, enter, answer, offer, order, wonder, remember, cover, suffer.", "",
  `**a / an (TR-E04)**: by the first sound. “an” although a consonant letter: hour, honest, honour, heir. “a” although a vowel letter: university, uniform, unit, union, unique, user, useful, usual, utensil, European, one, once, ewe.`, "",
  `**Irregular plurals (TR-E05)**: ${Object.entries(english.IRREGULAR_PLURAL).map(([a, b]) => `${a} → ${b}`).join(", ")}; -es after s, sh, ch, x, z and for tomato, potato, mango, hero, echo; consonant + y → -ies.`, "",
  "**Ordinal words (TR-E12)**: first, second, third, fifth, eighth, ninth, twelfth are special; -y → -ieth (twentieth); the rest add -th.", "",
  "**Dates (TR-E16)**: dd/mm/yyyy (British order).", ""],
}[SUBJECT];
const A = [`# ${CONF.name} Form 1, ${CONF.batch}: authored answers for review`, "",
  "Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.",
  "Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.",
  `Regenerate with \`npm run review:${SUBJECT}\`. Item IDs (TR-…) match \`docs/teacher-review.md\`.`, "",
  ...PART1(),
  "## Part 2: authored question templates", "",
  "| # | Template | Lesson | Type, level | Sources |", "|---|---|---|---|---|"];
const authored = lessons.filter((l) => !isDeferred(l)).flatMap((l) => [...l.questions, ...l.teach.cards.filter((c) => !c.check.ref).map((c) => ({ ...c.check, card: c.id }))]
  .filter((t) => t.review === "authored").map((t) => [l, t]));
authored.forEach(([l, t], i) => A.push(`| ${i + 1} | \`${t.id}\`${t.card ? ` (card ${t.card})` : ""} | ${l.lesson_no} | ${TYPE_NAME[t.type]}, ${t.level} | ${t.sources.join(", ")} |`));
A.push("");
const objTable = (rows) => {
  const keys = [...new Set(rows.flatMap((r) => Object.keys(r)))];
  return [`| ${keys.join(" | ")} |`, `|${keys.map(() => "---").join("|")}|`,
    ...rows.map((r) => `| ${keys.map((k) => (Array.isArray(r[k]) ? r[k].join(" · ") : String(r[k] ?? "")).replace(/\|/g, "/")).join(" | ")} |`)];
};
for (const [l, t] of authored) {
  A.push(`### \`${t.id}\` · Lesson ${l.lesson_no} · ${TYPE_NAME[t.type]}, level ${t.level}`, "", `Prompt: ${t.prompt.replace(/\n/g, " / ")}`);
  if (t.text) A.push(`Sentence: ${t.text}`);
  if (t.answer !== undefined && t.type !== "word_order") A.push(`Right answer: \`${t.answer}\`${t.accept ? `; also accepted: ${t.accept.map((a) => `\`${a}\``).join(", ")}` : ""}`);
  A.push("");
  for (const [name, spec] of Object.entries(t.vars || {})) {
    if (spec?.pick && typeof spec.pick[0] === "object") A.push(`Table \`${name}\` (one row is picked each time):`, "", ...objTable(spec.pick), "");
    else if (spec?.pick) A.push(`\`${name}\`: ${spec.pick.join(" · ")}`, "");
  }
  if (t.type === "word_order") A.push(`Sentence(s): ${t.answer}${t.accept ? ` (also accepted: ${t.accept.join(", ")})` : ""}`, "");
  if (t.pool && !Array.isArray(t.pool)) {
    A.push(`Shows ${t.pick.right} ${t.type === "spot_error" ? "correct" : "true"} and ${t.pick.wrong} ${t.type === "spot_error" ? "wrong" : "false"} statement(s), drawn from:`, "");
    for (const s of t.pool.right) A.push(`- ✅ ${s.text}`);
    for (const s of t.pool.wrong) A.push(`- ❌ ${s.text}${s.explain ? `  \n  _↳ ${s.explain}_` : ""}`);
    A.push("");
  }
  if (Array.isArray(t.pool)) A.push(`Pairs (${t.pick} shown each time${t.groups ? ", sorted into groups" : ""}):`, "", ...t.pool.map((p) => `- ${rend(p.left)} → **${rend(p.right)}**`), "");
  if (t.items) A.push("Items in the right order:", "", ...t.items.map((it, i) => `${i + 1}. ${it.text}`), "");
  if (t.correct !== undefined) A.push(`Right answer: \`${t.correct}\`; wrong choices: ${t.distractors.map((d) => `\`${typeof d === "string" ? d : d.text}\``).join(", ")}`, "");
  if (t.choices) A.push(`Choices: ${t.choices.map((c) => `\`${typeof c === "string" ? c : c.text}\``).join(", ")}`, "");
  for (const m of t.misconceptions || []) A.push(`- Feedback \`${m.id}\`${m.wrong ? ` (typed \`${[].concat(m.wrong).join("` or `")}\`)` : ""}: “${m.explain}”`);
  A.push("", "Three generated variants:", "");
  for (const seed of [1, 2, 3]) A.push(renderQuestion(instantiate(t, seed, lib, l.lesson_no)), "");
  A.push(`Sources: ${t.sources.map((s) => `${s} (${sources[s].ref})`).join("; ")}`, "");
}
writeFileSync(new URL("AUTHORED.md", DIR), A.join("\n") + "\n", "utf8");
console.log(`wrote content/${SUBJECT}/REVIEW.md, AUTHORED.md and ${figCount} figures (${authored.length} authored templates)`);
