// Renders a subject batch for review (English E1, Physics P1, …):
//   content/{subject}/REVIEW.md    a sample lesson in teach mode, then every draft (cards, worked examples, practice, paper tasks)
//   content/{subject}/AUTHORED.md  every answer fixed by a person (keys, tables, statement pools), with sources
//   content/{subject}/figures/     the drawings (SVG) shown in REVIEW.md
//   node tools/content/render_subject.mjs english|physics|chemistry|geography   (npm run review:<subject>)
// Everything shown is produced by the engine itself, so the reviewer sees exactly what pupils will see.
import { readFileSync, readdirSync, writeFileSync, mkdirSync, rmSync } from "node:fs";
import * as maths from "../../src/engine/lib/maths.js";
import * as maths2 from "../../src/engine/lib/maths2.js";
import * as science2 from "../../src/engine/lib/science2.js";
import * as english from "../../src/engine/lib/english.js";
import * as physics from "../../src/engine/lib/physics.js";
import * as chemistry from "../../src/engine/lib/chemistry.js";
import * as geography from "../../src/engine/lib/geography.js";
import * as homeeconomics from "../../src/engine/lib/homeeconomics.js";
import * as history from "../../src/engine/lib/history.js";
import * as biology from "../../src/engine/lib/biology.js";
import * as computerscience from "../../src/engine/lib/computerscience.js";
import * as french from "../../src/engine/lib/french.js";
import * as french2 from "../../src/engine/lib/french2.js";
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
  history: { name: "History", batch: "Batch Y1", spine: "history", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history }, sample: 3, lessons: "1–10", bySeq: true },
  biology: { name: "Biology", batch: "Batch B1", spine: "biology", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology }, sample: 7, lessons: "1–9, 13–21", bySeq: true },
  "computer-science": { name: "Computer Science", batch: "Batch S1", spine: "computer-science", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience }, sample: 11, lessons: "1–6, 8–11, 13–14, 16–18" },
  french: { name: "French", batch: "Batch F1", spine: "french", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...french }, sample: 15, lessons: "1–15" },
  // Form 2 (2026-10-17, form-2 branch): its own folder, numbered by place in the year (proposal G1)
  "f2-maths": { name: "Maths", cls: "Form 2", dir: "form-2/maths", batch: "Batches M2-1, M2-2", spine: "form-2/mathematics", lib: { ...maths, ...maths2 }, sample: 21, lessons: "1–54, Terms 1 and 2", bySeq: true },
  "f2-francais-intensif": { name: "Français intensif", cls: "Form 2", dir: "form-2/francais-intensif", batch: "Batch FI2-1", spine: "form-2/francais-intensif", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...french, ...french2 }, sample: 28, lessons: "1–25, 27–51, Term 1", bySeq: true },
  "f2-french": { name: "French", cls: "Form 2", dir: "form-2/french", batch: "Batches FR2-1, FR2-2", spine: "form-2/french", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...french, ...french2 }, sample: 21, lessons: "1–15, 18–32, 36–52, 54–68, Terms 1 and 2", bySeq: true },
  "f2-home-economics": { name: "Home Economics", cls: "Form 2", dir: "form-2/home-economics", batch: "Batches H2-1, H2-2", spine: "form-2/home-economics", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...maths2, ...science2 }, sample: 7, lessons: "1–9, 12–21, 24–33, 36–46, Terms 1 and 2", bySeq: true },
  "f2-geography": { name: "Geography", cls: "Form 2", dir: "form-2/geography", batch: "Batches G2-1, G2-2", spine: "form-2/geography", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...maths2, ...science2 }, sample: 7, lessons: "1–19, Terms 1 and 2", bySeq: true },
  "f2-history": { name: "History", cls: "Form 2", dir: "form-2/history", batch: "Batches Y2-1, Y2-2", spine: "form-2/history", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...maths2, ...science2 }, sample: 9, lessons: "1–21, Terms 1 and 2", bySeq: true },
  "f2-computer-science": { name: "Computer Science", cls: "Form 2", dir: "form-2/computer-science", batch: "Batches S2-1, S2-2", spine: "form-2/computer-science", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...maths2, ...science2 }, sample: 15, lessons: "1, 2, 4–6, 8, 9, 11, 12, 14–16, 18, 19, 21, 22, 24, 26, 27, 29–34, 36–40, Terms 1 and 2", bySeq: true },
  "f2-accounting": { name: "Accounting", cls: "Form 2", dir: "form-2/accounting", batch: "Batches A2-1, A2-2", spine: "form-2/accounting", lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...maths2, ...science2 }, sample: 4, lessons: "1–8, 10–18, Terms 1 and 2", bySeq: true },
  "f2-physics": { name: "Physics", cls: "Form 2", dir: "form-2/physics", batch: "Batches P2-1, P2-2", spine: "form-2/physics", lib: { ...maths, ...english, ...physics, ...chemistry, ...biology, ...maths2, ...science2 }, sample: 6, lessons: "1–31, Terms 1 and 2", bySeq: true },
  "f2-chemistry": { name: "Chemistry", cls: "Form 2", dir: "form-2/chemistry", batch: "Batches C2-1, C2-2", spine: "form-2/chemistry", lib: { ...maths, ...english, ...physics, ...chemistry, ...biology, ...maths2, ...science2 }, sample: 10, lessons: "1–4, 6–11, 13–17, 20–27, 29–38, 40–45, Terms 1 and 2", bySeq: true },
  "f2-biology": { name: "Biology", cls: "Form 2", dir: "form-2/biology", batch: "Batches B2-1, B2-2", spine: "form-2/biology", lib: { ...maths, ...english, ...physics, ...chemistry, ...biology, ...maths2, ...science2 }, sample: 7, lessons: "1–9, 13–21, 25–33, 37–46, Terms 1 and 2", bySeq: true },
  "f2-english": { name: "English", cls: "Form 2", dir: "form-2/english", batch: "Batches E2-1, E2-2", spine: "form-2/english-language", lib: { ...maths, ...english }, sample: 3, lessons: "1–76, Terms 1 and 2", bySeq: true },
}[SUBJECT];
if (!CONF) throw new Error("usage: node tools/content/render_subject.mjs english|physics|chemistry|geography|home-economics|history|biology|computer-science|french|f2-maths|f2-english|f2-physics|f2-chemistry|f2-biology|f2-home-economics|f2-geography|f2-history|f2-computer-science|f2-accounting|f2-french|f2-francais-intensif");
const lib = CONF.lib;
const FOLDER = CONF.dir || SUBJECT, CLS = CONF.cls || "Form 1";
const DIR = new URL(`../../content/${FOLDER}/`, import.meta.url);
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
const R = [`# ${CONF.name} ${CLS}, ${CONF.batch}: drafts for review (Lessons ${CONF.lessons})`, "",
  `Generated by \`npm run review:${SUBJECT}\` from \`content/${FOLDER}/*.json\`. Every question and drawing below was built by the engine.`,
  "All notes, teach cards, worked examples and paper tasks are **status: draft**. “Authored key” means a person fixed the",
  "right answer (see `AUTHORED.md`); “computed by rule” means code worked it out (a formula, a conversion, a spelling rule).", "",
  "Teach mode: cards (idea + example + 1 level-1 check) → worked example → practice (levels 1–3) → the note as a summary.",
  ...(SUBJECT === "english" || SUBJECT === "f2-english" ? ["Writing lessons replace practice with a paper task. Speech-work lessons are deferred (they need audio).", ""] : [""]),
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
  "f2-francais-intensif": () => ["## Part 1 : règles calculées (french2.js, TR-Z01, TR-Z06, TR-Z07)", "",
    `- **Imparfait** : je ${french2.fr2Imparfait("manger", 0)}, nous ${french2.fr2Imparfait("manger", 4)}, je ${french2.fr2Imparfait("commencer", 0)}, il ${french2.fr2Imparfait("finir", 2)}, j’${french2.fr2Imparfait("être", 0)}.`,
    `- **Passé simple** : il ${french2.fr2PasseSimple("manger", 2)}, ils ${french2.fr2PasseSimple("parler", 6)}, il ${french2.fr2PasseSimple("finir", 2)}, il ${french2.fr2PasseSimple("être", 2)}, ils ${french2.fr2PasseSimple("venir", 6)}.`,
    `- **Participe présent / gérondif** : ${["manger", "commencer", "finir", "faire", "être", "avoir"].map((v) => french2.fr2ParticipePresent(v)).join(", ")} ; ${french2.fr2Gerondif("lire")}.`,
    `- **Pluriels** : ${["cheval", "festival", "travail", "détail", "bijou", "trou", "bateau", "pneu"].map((n) => `${n} → ${french2.fr2NounPlural(n)}`).join(", ")}.`,
    `- **Adverbes** : ${french2.fr2AdvList().map((a) => `${a} → ${french2.fr2Adverb(a)}`).join(", ")}.`, ""],
  "f2-french": () => ["## Part 1 : règles calculées (french2.js, TR-Z01 et TR-Z02)", "",
    `- **Présent** : nous ${french2.fr2Present("manger", 4)}, nous ${french2.fr2Present("commencer", 4)}, j’${french2.fr2Present("appeler", 0)}, j’${french2.fr2Present("acheter", 0)}, je ${french2.fr2Present("préférer", 0)} ; nous ${french2.fr2Present("choisir", 4)}, nous ${french2.fr2Present("sentir", 4)}, vous ${french2.fr2Present("dire", 5)}.`,
    `- **Passé composé** : ${french2.fr2PasseCompose("manger", 0)}, ${french2.fr2PasseCompose("aller", 7)}, ${french2.fr2PasseCompose("venir", 3)}, ${french2.fr2PasseCompose("prendre", 6)}.`,
    `- **Adjectifs** : des jeux ${french2.fr2Adj("national", "m", true)}, des matchs ${french2.fr2Adj("final", "m", true)}, des fêtes ${french2.fr2Adj("national", "f", true)} ; des robes ${french2.fr2Adj("vert", "f", true)}, des chemises ${french2.fr2Adj("orange", "f", true)}, des robes ${french2.fr2Adj("rose", "f", true)}.`, ""],
  "f2-home-economics": () => ["## Part 1: rules and drawings (homeeconomics.js, as in Form One)", "", "- **Energy values (TR-U02)**: carbohydrate and protein 4 kcal (17 kJ) per gram, fat 9 kcal (37 kJ).",
    "- **Kitchen drawings and the work triangle**: the Form One drawings and rule (TR-H01, TR-H02).", ""],
  "f2-geography": () => ["## Part 1: formulae (computed by code)", "", "- BR = births ÷ population × 1000; DR likewise; NI = BR − DR (‰), ÷ 10 for %; density = population ÷ area.", ""],
  "f2-history": () => ["## Part 1", "", "Every answer in History is authored: see Part 2 and the sources.", ""],
  "f2-computer-science": () => ["## Part 1: rules the computed answers use (science2.js, maths.js)", "",
    `- **Hexadecimal and binary**: ${[10, 15, 26, 255].map((n) => `${n} = ${science2.toHex(n)}₁₆`).join(", ")}; bytes as 8 bits (${science2.bits8(13)} = 13).`,
    `- **ASCII**: A = ${science2.asciiOf("A")}, a = ${science2.asciiOf("a")}, 0 = ${science2.asciiOf("0")}, space = ${science2.asciiOf(" ")}.`,
    `- **Storage (TR-T05 decision)**: 1 byte = 8 bits; 1 KB = ${science2.storageFactor("KB", "byte")} bytes; 1 MB = ${science2.storageFactor("MB", "KB")} KB; 1 GB = ${science2.storageFactor("GB", "MB")} MB.`, ""],
  "f2-accounting": () => ["## Part 1: rules", "", "- Assets = Liabilities + Owner's equity (computed). Assets increase on the debit side; capital and liabilities on the credit side; expenses debited, revenues credited (authored).", ""],
  "f2-physics": () => ["## Part 1: rules the computed answers use (src/engine/lib/science2.js, physics.js)", "",
    `- **Speed**: v = d ÷ t; km/h ÷ 3.6 = m/s (${science2.kmhToMs(72)} m/s for 72 km/h). **Density**: mass ÷ volume, to 2 decimals. **Temperature**: T(K) = T(°C) + 273.`,
    "- **Data**: the mean of repeated readings; an anomalous reading is left out; graphs are drawn from the question's own numbers (lineGraph).", ""],
  "f2-chemistry": () => ["## Part 1: tables and rules the computed answers use (src/engine/lib/science2.js, chemistry.js)", "",
    `- **Electron shells (TR-J01)**: 2, 8, 8, 2 for atomic numbers 1–20 (sodium ${science2.shells(11)}, calcium ${science2.shells(20)}); group = outer electrons (helium in group 8), period = number of shells.`,
    `- **Mass numbers (TR-J02, authored)**: ${science2.firstTwenty().map((s) => `${s} ${science2.massNumber(s)}`).join(", ")}.`,
    `- **Valencies (TR-J03, authored)**: ${[...science2.positives(), ...science2.negatives()].map((x) => `${x} ${science2.valency(x)}`).join(", ")}. Formulae swap the valencies and simplify (${["Al-SO4", "Mg-O", "Ca-OH", "NH4-SO4"].map((p) => { const [a, b] = p.split("-"); return `${a} + ${b} → ${science2.compoundFormula(a, b)}`; }).join("; ")}).`, ""],
  "f2-biology": () => ["## Part 1: drawings (src/engine/lib/science2.js)", "",
    `- **Flower (TR-V01)**: eight lettered parts: ${science2.FLOWER_PARTS.join(", ")}. **Bean seed (TR-V02)**: ${science2.SEED_PARTS.join(", ")}. The letters are shuffled by the question's numbers; the code that draws a letter also gives the answer.`, ""],
  "f2-maths": () => ["## Part 1: rules the computed answers use (src/engine/lib/maths2.js, tested in tests-js/maths2.test.js)", "",
    `- **Integers**: negative numbers in brackets inside a calculation (${maths2.br(-3)} × ${maths2.br(4)}); same signs give a positive product or quotient, different signs a negative one. Answers that can be negative get the full keyboard (with a minus sign) on every variant.`,
    `- **Powers**: ${maths2.pw(-2, 3)} = ${maths2.powExpand(-2, 3)} = ${(-2) ** 3}; laws of indices for the same base only.`,
    `- **Prime factorisation** by repeated division (${maths2.ladder(60).join("; ")}), written ${maths2.factorProduct(60)} or ${maths2.factorise(60)}; HCF and LCM computed (HCF(24, 36) = ${maths2.hcf(24, 36)}, LCM = ${maths2.lcm(24, 36)}).`,
    `- **Expressions**: ${maths2.poly([3, "x"], [-1, "y"], [5, ""])}; a coefficient 1 is not written; ${maths2.bracket(-2, [1, "x"], [-4, ""])} = ${maths2.poly([-2, "x"], [8, ""])}.`,
    "- **Inequalities on the number line**: filled circle for ≤ and ≥, open circle for < and >, thick line and arrow towards the solutions.",
    "- **Notation** as in Form 1: (AB) line, [AB) half line, [AB] segment, AB length; (Δ) for the perpendicular bisector.", ""],
  "f2-english": () => ["## Part 1: word tables and rules", "",
    "Verb forms (past, participle, -ing, -s) and spellings come from the English library already checked for Form 1 (TR-E01 to TR-E05; see content/english/AUTHORED.md). "
    + "British spelling, as in Cameroonian schools (travelling, cancelled).", ""],
  chemistry: () => ["## Part 1: tables and rules the computed answers use (src/engine/lib/chemistry.js, physics.js)", "",
    "**Elements (TR-K02)**: atomic number, symbol, name, kind.", "",
    "| Z | Symbol | Name | Kind |", "|---|---|---|---|", ...chemistry.ELEMENTS.map((e) => `| ${e.z} | ${e.symbol} | ${e.name} | ${e.kind} |`), "",
    `**Symbols from Latin (TR-K02)**: ${Object.entries(chemistry.LATIN).map(([s, l]) => `${s} (${l})`).join(", ")}.`, "",
    "- **Formulas (TR-K03)**: the small number after a symbol counts the atoms of that symbol; no number means one; a bracket multiplies everything inside it (Ca(OH)₂: 1 Ca, 2 O, 2 H). Counted by `parseFormula()`, tested on known answers.",
    "- **Measurement**: the unit conversions, °C → K (+ 273), the measuring cylinder and thermometer drawings are the same as in Physics (TR-P04, TR-P05, TR-P08).", ""],
  french: () => {
    const nouns = Array.from({ length: french.frNounCount() }, (_, i) => i);
    return ["## Part 1: tables and rules the computed answers use (src/engine/lib/french.js)", "",
      "Everything the pupil reads in French lessons is in French, including the working the engine writes (`lang: \"fr\"`).", "",
      "**Nouns (TR-F01)**: definite and indefinite article, plural, and the possessive “à moi”.", "",
      "| Nom | Genre | Défini | Indéfini | Pluriel | À moi |", "|---|---|---|---|---|---|",
      ...nouns.map((i) => `| ${french.frNoun(i)} | ${french.frGender(i)} | ${french.frDef(i)} | ${french.frIndef(i)} | ${french.frDef(i, true)} | ${french.frPoss(0, i)} |`), "",
      `- **Conjugation (TR-F02)**: ${["avoir", "s’appeler", "travailler", "laver"].map((v) => `${v}: ${[0, 1, 2, 4, 5, 6].map((p) => french.frConj(v, p)).join(", ")}`).join("; ")}.`,
      `- **Numbers (TR-F03)**: traditional spelling taught; the 1990 spelling is also accepted when typed. ${[17, 21, 22, 31, 41, 44, 50].map((n) => `${n} → ${french.frNumber(n)} (1990 : ${french.frNumber1990(n)})`).join("; ")}.`,
      "- **Alphabetical order (TR-F04)**: accents are ignored when ordering (école sorts with e).", ""];
  },
  "computer-science": () => ["## Part 1: rules, table and drawings the answers use (src/engine/lib/computerscience.js)", "",
    `- **Patterns (TR-S01)**: number patterns add the same amount (${computerscience.firstTerms(3, 4, 4)} → ${computerscience.nthTerm(3, 4, 5)}) or double (${computerscience.firstDoubles(3, 4)} → ${computerscience.nthDouble(3, 5)}); shape patterns repeat a group, and shape n is found from the remainder of n ÷ the group length.`,
    "- **Tracing (TR-S01)**: “start with x, add b, n times” gives x + b × n; “double n times” gives x × 2ⁿ; IF x > L THEN “big” ELSE “small” (equal counts as small).",
    `- **History (TR-S02)**: ${[0, 1, 2, 3, 4, 5, 6].map((i) => `${computerscience.historyYear(i) < 0 ? "ancient times" : computerscience.historyYear(i)}: ${computerscience.historyStep(i)}`).join("; ")}.`,
    `- **Generations (TR-S02)**: ${[1, 2, 3, 4, 5].map((g) => `${g}: ${computerscience.generationTech(g)} (${computerscience.generationWhen(g)})`).join("; ")}.`,
    `- **Drawings**: repeating shapes (${[0, 1, 2, 3].map(computerscience.patternShape).join(", ")}) and three laboratory layouts (${computerscience.LAYOUTS.join(", ")}).`, ""],
  biology: () => ["## Part 1: rules, table and drawings the answers use (src/engine/lib/biology.js)", "",
    `- **Magnification (TR-L01)**: total = eyepiece × objective (${[[10, 4], [10, 40], [15, 100]].map(([e, o]) => `×${e} and ×${o} → ×${biology.magnification(e, o)}`).join("; ")}).`,
    `- **Cell discoveries (TR-L02)**: ${[0, 1, 2, 3].map((i) => `${biology.discoveryYear(i)}: ${biology.discoverer(i)} ${biology.discoveryWhat(i)}`).join("; ")}.`,
    `- **Drawings with lettered parts (TR-L03)**: microscope (${biology.MICRO_PARTS.join(", ")}); plant cell (${biology.PLANT_PARTS.join(", ")}); animal cell (${biology.ANIMAL_PARTS.join(", ")}); soil profile (${biology.SOIL_LAYERS.join(", ")}).`, ""],
  history: () => ["## Part 1: rules and the table the computed answers use (src/engine/lib/history.js)", "",
    `- **Writing years (TR-Y01)**: ${[-500, -1, 1, 476, 2026].map(history.year).join(", ")}; there is no year 0 (1 BC is followed by AD 1).`,
    `- **Years between (TR-Y01)**: same era, subtract; across BC and AD, add and take away 1: ${[[1884, 1961], [-500, -200], [-50, 50], [-1, 1]].map(([a, b]) => `${history.year(a)} → ${history.year(b)}: ${history.yearsBetween(a, b)}`).join("; ")}.`,
    `- **Centuries (TR-Y01)**: ${[111, 1884, 1900, 1901, 2026, -500, -501].map((y) => `${history.year(y)} → ${history.century(y)}`).join("; ")}.`, "",
    "**Early humans (TR-Y03)**, oldest first (estimates; only the order and these rounded dates are used):", "",
    "| Name | First appears | Known for | Important finds |", "|---|---|---|---|",
    ...[0, 1, 2, 3, 4].map((i) => `| ${history.homininName(i)} | ${history.ago(history.homininAgo(i))} | ${history.homininNote(i)} | ${history.homininPlace(i)} |`), ""],
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
const A = [`# ${CONF.name} ${CLS}, ${CONF.batch}: authored answers for review`, "",
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
  const tryRend = (x) => { try { return rend(x); } catch { return x; } };  // pairs that use the question's numbers stay as written
  if (Array.isArray(t.pool)) A.push(`Pairs (${t.pick} shown each time${t.groups ? ", sorted into groups" : ""}):`, "", ...t.pool.map((p) => `- ${tryRend(p.left)} → **${tryRend(p.right)}**`), "");
  if (t.items) A.push("Items in the right order:", "", ...t.items.map((it, i) => `${i + 1}. ${it.text}`), "");
  if (t.correct !== undefined) A.push(`Right answer: \`${t.correct}\`; wrong choices: ${t.distractors.map((d) => `\`${typeof d === "string" ? d : d.text}\``).join(", ")}`, "");
  if (t.choices) A.push(`Choices: ${t.choices.map((c) => `\`${typeof c === "string" ? c : c.text}\``).join(", ")}`, "");
  for (const m of t.misconceptions || []) A.push(`- Feedback \`${m.id}\`${m.wrong ? ` (typed \`${[].concat(m.wrong).join("` or `")}\`)` : ""}: “${m.explain}”`);
  A.push("", "Three generated variants:", "");
  for (const seed of [1, 2, 3]) A.push(renderQuestion(instantiate(t, seed, lib, l.lesson_no)), "");
  A.push(`Sources: ${t.sources.map((s) => `${s} (${sources[s].ref})`).join("; ")}`, "");
}
writeFileSync(new URL("AUTHORED.md", DIR), A.join("\n") + "\n", "utf8");
console.log(`wrote content/${FOLDER}/REVIEW.md, AUTHORED.md and ${figCount} figures (${authored.length} authored templates)`);
