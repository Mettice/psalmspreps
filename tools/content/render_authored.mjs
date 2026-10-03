// Lists only the templates whose answers are authored (not computed), with every variant,
// every answer and its sources, into content/maths/AUTHORED.md.
//   node tools/content/render_authored.mjs
import { readFileSync, readdirSync, writeFileSync } from "node:fs";
import * as lib from "../../src/engine/lib/maths.js";
import { render, evaluate } from "../../src/engine/expr.js";
import { sampleScope, instantiate } from "../../src/engine/template.js";
import { makeRng } from "../../src/engine/rng.js";

const DIR = new URL("../../content/maths/", import.meta.url);
const lessons = readdirSync(DIR).filter((f) => /^\d+\.json$/.test(f))
  .map((f) => JSON.parse(readFileSync(new URL(f, DIR), "utf8"))).sort((a, b) => a.lesson_no - b.lesson_no);
const sources = JSON.parse(readFileSync(new URL("sources.json", DIR), "utf8"));
const spine = JSON.parse(readFileSync(new URL("../../data/spine/mathematics.json", import.meta.url), "utf8"));
const title = Object.fromEntries(spine.terms.flatMap((t) => t.lessons).map((l) => [l.lesson_no, l.title]));

const show = (v) => (typeof v === "number" ? lib.fmt(v) : String(v));
const R = (t, scope) => render(t, scope, lib, show).replace(/ /g, " ");
const deep = (x, scope) => (typeof x === "string" ? R(x, scope)
  : x && typeof x === "object" ? Object.fromEntries(Object.entries(x).map(([k, v]) => [k, deep(v, scope)])) : x);

// Practice templates and inline teach-card check questions.
const authored = lessons.flatMap((l) => [...(l.questions || []), ...(l.teach?.cards || []).filter((c) => !c.check.ref).map((c) => ({ ...c.check, card: c.id }))]
  .filter((t) => t.review === "authored").map((t) => [l, t]));
const out = [
  "# Authored answers for review (Maths Form 1, Lessons 1–16: practice and teach-card checks)", "",
  `These ${authored.length} templates have answers fixed by the author (facts, definitions, notation), not computed by code.`,
  "Each one lists every variant a pupil can see, the answer the app accepts, the feedback for each wrong choice, and the sources.",
  "Letters such as P and Q are drawn at random in the app; one sample is shown here.", "",
  "Regenerate with `node tools/content/render_authored.mjs`.", "",
  "| # | Template | Lesson | Type, level | Sources |", "|---|---|---|---|---|",
  ...authored.map(([l, t], i) => `| ${i + 1} | \`${t.id}\`${t.card ? ` (card ${t.card})` : ""} | ${l.lesson_no} | ${t.type}, ${t.level} | ${t.sources.join(", ")} |`), "",
];

authored.forEach(([l, t], i) => {
  const scope = sampleScope(t.vars, t.where, makeRng(1), lib);
  const miscExplain = Object.fromEntries((t.misconceptions || []).map((m) => [m.id, m.explain]));
  out.push(`## ${i + 1}. \`${t.id}\` (Lesson ${l.lesson_no}: ${title[l.lesson_no]})`, "", `Type: ${t.type}, level ${t.level}.`, "");
  // A `pick` of objects or strings means several variants of the same question: list them all.
  const pickVar = Object.entries(t.vars || {}).find(([, spec]) => spec && spec.pick && t.type !== "ordering");
  const variants = pickVar ? pickVar[1].pick.map((opt) => ({ ...scope, [pickVar[0]]: deep(opt, scope) })) : [scope];
  if (t.type === "mcq" && t.correct !== undefined) {
    out.push("| Question | Answer accepted | Wrong choices and the feedback each one gets |", "|---|---|---|");
    for (const s of variants) {
      const answer = R(t.correct, s);
      const wrong = t.distractors.map((d) => [R(d.text, s), R(miscExplain[d.misconception] || "", s)]).filter(([x]) => x !== answer);
      out.push(`| ${R(t.prompt, s)} | **${answer}** | ${wrong.map(([x, e]) => `${x}: _${e}_`).join("<br>")} |`);
    }
  } else if (t.type === "numeric") {
    out.push("| Question | Answer accepted | Recognised wrong answers and feedback |", "|---|---|---|");
    for (const s of variants) {
      const answer = evaluate(t.answer, s, lib);
      const wrong = t.misconceptions.map((m) => [evaluate(m.wrong, s, lib), R(m.explain, s)]).filter(([x]) => x !== answer);
      out.push(`| ${R(t.prompt, s)} | **${show(answer)}** | ${wrong.map(([x, e]) => `${show(x)}: _${e}_`).join("<br>")} |`);
    }
  } else if (t.pool) {
    const ask = t.type === "mcq" ? "choose the TRUE statement" : "choose the FALSE statement";
    out.push(`**${R(t.prompt, scope)}** (${ask}; the app shows ${t.pick.right} true and ${t.pick.wrong} false, picked at random)`, "",
      "| Statement | True or false (as authored) | Feedback |", "|---|---|---|");
    for (const s of t.pool.right) out.push(`| ${R(s.text, scope)} | true | |`);
    for (const s of t.pool.wrong) out.push(`| ${R(s.text, scope)} | **false** | ${R(s.explain || "", scope)} |`);
  } else if (t.type === "ordering") {
    out.push(`**${R(t.prompt, scope)}**`, "", "Correct order (as authored):", "", ...t.items.map((it, k) => `${k + 1}. ${R(it.text, scope)}`));
  }
  const sample = instantiate(t, 1, lib, l.lesson_no);
  if (sample.solution) out.push("", "**Full working shown after a second miss** (sample):", "", ...sample.solution.map((x) => `> ${x.replace(/ /g, " ")}  `));
  out.push("", "**Sources**", "");
  for (const id of t.sources) {
    const s = sources[id];
    out.push(`- ${s.url ? `[${s.ref}](${s.url})` : s.ref}. Supports: ${s.supports} _Checked: ${s.checked}_`);
  }
  out.push("", "Decision: ☐ approve ☐ change: ____________", "");
});
writeFileSync(new URL("AUTHORED.md", DIR), out.join("\n"), "utf8");
console.log(`wrote content/maths/AUTHORED.md (${authored.length} templates)`);
