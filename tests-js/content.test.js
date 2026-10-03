// Content tests: every Maths template (lessons, teach-card checks, Lesson 0) across 1000 seeds,
// worked examples, teach cards, notes, number style, sources.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import * as lib from "../src/engine/lib/maths.js";
import { evaluate } from "../src/engine/expr.js";
import { instantiate, check, renderWorked } from "../src/engine/template.js";
import { renderCard, cardCheckTemplate } from "../src/engine/teach.js";

const SEEDS = 1000;
const DIR = new URL("../content/maths/", import.meta.url);
const lessons = Object.fromEntries(readdirSync(DIR).filter((f) => /^\d+\.json$/.test(f))
  .map((f) => JSON.parse(readFileSync(new URL(f, DIR), "utf8"))).map((l) => [l.lesson_no, l]));
const spine = JSON.parse(readFileSync(new URL("../data/spine/mathematics.json", import.meta.url), "utf8"));
const spineLessons = spine.terms.flatMap((t) => t.lessons);
const BATCH = Array.from({ length: 17 }, (_, i) => i);  // Lesson 0 + Lessons 1-16
const FORM1 = Object.values(lessons).filter((l) => !l.kind);
const TYPES = new Set(["mcq", "numeric", "spot_error", "ordering"]);
const BAD_TEXT = /NaN|undefined|\[object Object\]|Infinity/;

const words = (t) => t.split(/\s+/).filter((w) => /[\p{L}\p{N}]/u.test(w)).length;
/** Literal digits outside {…}: every number in worked examples and teach cards must be computed. */
const literalDigits = (t) => t.replace(/\{\{|\}\}/g, "").replace(/\{[^{}]*\}/g, "").match(/[0-9⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉]/g);
/** Inline card check templates (cards that use {ref} reuse a lesson template). */
const cardTemplates = (l) => (l.teach?.cards || []).filter((c) => !c.check.ref).map((c) => c.check);
/** Every template the app can show: lesson questions, inline card checks (and Lesson 0's). */
const allTemplates = Object.values(lessons).flatMap((l) => [...(l.questions || []), ...cardTemplates(l)].map((t) => [l, t]));

test("the batch is complete and matches the spine", () => {
  assert.deepEqual(Object.keys(lessons).map(Number).sort((a, b) => a - b), BATCH);
  for (const l of Object.values(lessons)) {
    assert.equal(l.subject, "mathematics");
    assert.equal(l.class, "Form 1");
    assert.ok(spineLessons.some((s) => s.lesson_no === l.lesson_no), `lesson ${l.lesson_no} is not in the spine`);
  }
});

test("prerequisites point to earlier lessons in the spine order", () => {
  const order = Object.fromEntries(spineLessons.map((s) => [s.lesson_no, s.seq]));
  for (const l of Object.values(lessons)) for (const p of l.prerequisites) {
    assert.ok(p in order, `lesson ${l.lesson_no}: unknown prerequisite ${p}`);
    assert.ok(order[p] < order[l.lesson_no], `lesson ${l.lesson_no}: prerequisite ${p} comes later`);
  }
});

test("notes: draft, at most 150 words, numeric claims checked by code", () => {
  for (const l of Object.values(lessons)) {
    assert.equal(l.note.status, "draft", `lesson ${l.lesson_no}`);
    assert.ok(words(l.note.text) <= 150, `lesson ${l.lesson_no} note has ${words(l.note.text)} words`);
    for (const c of l.note.checks) assert.equal(evaluate(c, {}, lib), true, `lesson ${l.lesson_no} note check failed: ${c}`);
  }
});

test("worked examples: draft, every number computed by code, all checks pass", () => {
  for (const l of FORM1) {
    const we = l.worked_example;
    assert.equal(we.status, "draft");
    for (const t of [we.problem, we.answer, ...we.steps]) {
      assert.equal(literalDigits(t), null, `lesson ${l.lesson_no}: type the number as a {var} so code computes it: "${t}"`);
    }
    const r = renderWorked(we, lib);
    assert.deepEqual(r.failedChecks, [], `lesson ${l.lesson_no}`);
    for (const t of [r.problem, r.answer, ...r.steps]) assert.ok(!BAD_TEXT.test(t), `lesson ${l.lesson_no}: ${t}`);
  }
});

test("teach cards: 3-4 per lesson, draft, no typed numbers, checks pass, level-1 check question", () => {
  const ids = new Set();
  for (const l of FORM1) {
    const cards = l.teach?.cards || [];
    assert.ok(cards.length >= 3 && cards.length <= 4, `lesson ${l.lesson_no} has ${cards.length} cards`);
    for (const c of cards) {
      assert.ok(!ids.has(c.id), `duplicate card ${c.id}`);
      ids.add(c.id);
      assert.equal(c.status, "draft", c.id);
      for (const t of [c.idea, ...c.example]) assert.equal(literalDigits(t), null, `${c.id}: type the number as a {var}: "${t}"`);
      const r = renderCard(c, lib);
      assert.deepEqual(r.failedChecks, [], c.id);
      for (const t of [r.idea, ...r.example]) assert.ok(!BAD_TEXT.test(t) && !/[{}]{2}/.test(t), `${c.id}: ${t}`);
      const tpl = cardCheckTemplate(l, c);
      assert.equal(tpl.level, 1, `${c.id}: check question must be level 1 (${tpl.id})`);
    }
  }
});

test("teach cards: a wrong answer gets a fresh variant (different numbers or a new option order)", () => {
  for (const l of FORM1) for (const c of l.teach.cards) {
    const tpl = cardCheckTemplate(l, c);
    const seen = new Set();
    for (let seed = 1; seed <= 20; seed++) {
      const q = instantiate(tpl, seed, lib, l.lesson_no);
      seen.add(JSON.stringify([q.prompt, q.options?.map((o) => o.text), q.items]));
    }
    assert.ok(seen.size > 1, `${c.id}: every variant of ${tpl.id} looks the same`);
  }
});

test("question templates: ids, types, levels 1-3 in every Form 1 lesson", () => {
  const ids = new Set();
  for (const [, t] of allTemplates) {
    assert.ok(!ids.has(t.id), `duplicate id ${t.id}`);
    ids.add(t.id);
    assert.ok(TYPES.has(t.type), `${t.id}: type ${t.type}`);
    assert.ok([1, 2, 3].includes(t.level), `${t.id}: level ${t.level}`);
  }
  for (const l of FORM1) assert.deepEqual([...new Set(l.questions.map((t) => t.level))].sort(), [1, 2, 3], `lesson ${l.lesson_no}`);
});

for (const [l, tpl] of allTemplates) {
  test(`${tpl.id}: ${SEEDS} seeds give correct, well-formed questions`, () => {
    const positions = new Set();
    for (let seed = 1; seed <= SEEDS; seed++) {
      const q = instantiate(tpl, seed, lib, l.lesson_no);
      const where = `${tpl.id} seed ${seed}`;
      assert.equal(q.verified, true, `${where}: verify failed for answer ${q.answer}`);
      assert.ok(!BAD_TEXT.test(q.prompt), `${where}: ${q.prompt}`);
      assert.ok(!BAD_TEXT.test(String(q.answer)), `${where}: answer ${q.answer}`);
      if (q.hint) assert.ok(!BAD_TEXT.test(q.hint), `${where}: hint ${q.hint}`);
      if (q.type === "numeric") {
        assert.deepEqual(check(q, q.answer), { correct: true }, where);
        assert.deepEqual(check(q, String(q.answerValue)), { correct: true }, where);
        for (const m of q.misconceptions) {
          const r = check(q, m.value);
          assert.equal(r.correct, false, `${where}: misconception ${m.id} gives the right answer`);
          assert.ok(r.misconception && r.misconception.explain && !BAD_TEXT.test(r.misconception.explain), `${where}: ${m.id}`);
        }
      } else if (q.type === "mcq" || q.type === "spot_error") {
        const texts = q.options.map((o) => o.text);
        assert.equal(new Set(texts).size, texts.length, `${where}: repeated option in ${texts}`);
        if (tpl.correct !== undefined) assert.equal(q.options.length, tpl.show || 4, where);
        for (const t of texts) assert.ok(!BAD_TEXT.test(t), `${where}: ${t}`);
        q.options.forEach((o, i) => assert.equal(check(q, i).correct, i === q.correctIndex, `${where}: option ${i}`));
        positions.add(q.correctIndex);
      } else if (q.type === "ordering") {
        assert.deepEqual([...q.correctOrder].sort(), q.items.map((_, i) => i), where);
        assert.equal(check(q, q.correctOrder).correct, true, where);
        assert.equal(check(q, q.items.map((_, i) => i)).correct, false, `${where}: shown already in order`);
      }
    }
    if (positions.size) assert.ok(positions.size > 1, `${tpl.id}: the right answer is always in position ${[...positions]}`);
  });
}

// ---------------------------------------------------------------- full working and hints (decision 2026-10-03)
const FORM1_TEMPLATES = allTemplates.filter(([l]) => !l.kind);
const answerShown = (q) => (q.type === "numeric" ? String(q.answer) : q.answer);

test("full working and hints: no typed numbers (every number computed)", () => {
  for (const [, t] of FORM1_TEMPLATES) {
    for (const s of t.solution || []) assert.equal(literalDigits(s), null, `${t.id} solution: type the number as a {var}: "${s}"`);
    if (t.hint) assert.equal(literalDigits(t.hint), null, `${t.id} hint: type the number as a {var}: "${t.hint}"`);
  }
});

test("full working: every Form 1 question has it, and it ends at the computed answer", () => {
  for (const [l, tpl] of FORM1_TEMPLATES) {
    if (tpl.type === "numeric" || (tpl.type === "mcq" && tpl.correct !== undefined)) assert.ok(tpl.solution?.length, `${tpl.id} needs a "solution"`);
    for (let seed = 1; seed <= SEEDS; seed++) {
      const q = instantiate(tpl, seed, lib, l.lesson_no);
      const where = `${tpl.id} seed ${seed}`;
      assert.ok(q.solution?.length, `${where}: no working`);
      for (const line of q.solution) assert.ok(line.trim() && !BAD_TEXT.test(line), `${where}: "${line}"`);
      assert.ok(q.solution.join("\n").includes(answerShown(q)), `${where}: working does not show the answer ${q.answer}: ${q.solution.join(" / ")}`);
    }
  }
});

test("misconceptions: every distractor or wrong value is explained", () => {
  for (const [, t] of allTemplates) {
    const ids = new Set((t.misconceptions || []).map((m) => m.id));
    for (const d of t.distractors || []) if (d.misconception) assert.ok(ids.has(d.misconception), `${t.id}: ${d.misconception} has no explanation`);
    for (const m of t.misconceptions || []) assert.ok(m.explain, `${t.id}: ${m.id} has no explanation`);
  }
});

test("Lesson 0: Primary 6 readiness only, at most 15 questions, every area covered", () => {
  const l0 = lessons[0];
  const spec = l0.readiness;
  assert.equal(l0.kind, "readiness");
  assert.ok(spec.items.length <= 15 && spec.max_questions === 15);
  assert.ok(spec.items.length * spec.seconds_per_question <= spec.time_limit_minutes * 60);
  const areas = new Set(spec.items.map((it) => l0.questions.find((t) => t.id === it.template).area));
  assert.deepEqual([...areas].sort(), Object.keys(spec.areas).sort());
  // It reuses no Form 1 template: it cannot set Form 1 mastery.
  const form1Ids = new Set(FORM1.flatMap((l) => l.questions.map((t) => t.id)));
  for (const it of spec.items) assert.ok(!form1Ids.has(it.template), it.template);
});

// ---------------------------------------------------------------- number style (decision 2026-10-02)
// 4-digit numbers are never grouped (7750, 1948); 5+ digits are grouped with a space (12 500).
const GROUPED_FOUR = /(?<!\d)(?<!\d[  ])\d[  ]\d{3}(?!\d)(?![  ]\d{3})/;
const UNGROUPED_FIVE = /(?<![\d.,₀-₉])\d{5,}(?![\d₀-₉])/;
const DISPLAY_KEYS = new Set(["text", "prompt", "correct", "explain", "problem", "steps", "name", "m", "s", "unit", "hint", "idea", "example"]);
const SKIP_KEYS = new Set(["checks", "vars", "where", "verify", "truth", "wrong", "when", "key"]);

/** Literal display text in a lesson file, with {expressions} removed (code formats those). */
function displayText(node, key = "", out = []) {
  if (typeof node === "string") {
    if (DISPLAY_KEYS.has(key)) out.push(node.replace(/\{\{|\}\}/g, "").replace(/\{[^{}]*\}/g, "{…}"));
  } else if (Array.isArray(node)) node.forEach((x) => displayText(x, key, out));
  else if (node && typeof node === "object") {
    for (const [k, v] of Object.entries(node)) if (!SKIP_KEYS.has(k)) displayText(v, k, out);
    if (node.problem && typeof node.answer === "string") out.push(node.answer.replace(/\{[^{}]*\}/g, "{…}"));  // worked-example answer
  }
  return out;
}

test("number style: no grouped 4-digit numbers, no ungrouped 5+ digit numbers in written content", () => {
  assert.equal(lib.fmt(7750), "7750");
  assert.equal(lib.fmt(1948), "1948");
  assert.equal(lib.fmt(12500), "12 500");
  for (const l of Object.values(lessons)) for (const t of displayText(l)) {
    assert.ok(!GROUPED_FOUR.test(t), `lesson ${l.lesson_no}: 4-digit number grouped in "${t.slice(0, 120)}"`);
    const allowed = (l.lint_allow || []).reduce((s, a) => s.replaceAll(a, ""), t);
    assert.ok(!UNGROUPED_FIVE.test(allowed), `lesson ${l.lesson_no}: 5+ digit number not grouped in "${t.slice(0, 120)}"`);
  }
});

test("number style: generated questions and cards never group a 4-digit number", () => {
  for (const [l, tpl] of allTemplates) {
    for (let seed = 1; seed <= 300; seed++) {
      const q = instantiate(tpl, seed, lib, l.lesson_no);
      const texts = [q.prompt, q.answer, q.hint, ...(q.options || []).flatMap((o) => [o.text, o.explain]),
        ...(q.items || []), ...(q.misconceptions || []).flatMap((m) => [m.value, m.explain])].filter(Boolean);
      for (const t of texts) assert.ok(!GROUPED_FOUR.test(t), `${tpl.id} seed ${seed}: "${t}"`);
    }
  }
  for (const l of FORM1) for (const c of l.teach.cards) {
    const r = renderCard(c, lib);
    for (const t of [r.idea, ...r.example]) assert.ok(!GROUPED_FOUR.test(t), `${c.id}: "${t}"`);
  }
});

test("authored templates (lesson questions and card checks) cite sources that exist", () => {
  const sources = JSON.parse(readFileSync(new URL("sources.json", DIR), "utf8"));
  const authored = allTemplates.filter(([, t]) => t.review === "authored").map(([, t]) => t);
  assert.equal(authored.length, 19);
  for (const t of authored) {
    assert.ok(t.sources?.length, `${t.id} has no sources`);
    for (const id of t.sources) assert.ok(sources[id]?.ref && sources[id]?.checked, `${t.id}: unknown source ${id}`);
  }
});

test("Lesson 16 note stays draft until 'orthogonal' is checked", () => {
  assert.equal(lessons[16].note.status, "draft");
  assert.match(lessons[16].note.review, /orthogonal/);
});
