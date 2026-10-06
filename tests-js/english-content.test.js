// English Batch E1 content tests (Lessons 1–16): every template across 1000 seeds, worked examples, teach
// cards, notes, paper tasks, deferred speech-work lessons, sources. Same rules as the Maths content tests.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import { instantiate, check, renderWorked, normaliseText } from "../src/engine/template.js";
import { renderCard, cardCheckTemplate, lessonSteps, renderPaper, isDeferred, isAutoMarked } from "../src/engine/teach.js";
import { checklistLessons } from "../src/engine/state.js";

const lib = { ...maths, ...english };
const SEEDS = 1000;
const DIR = new URL("../content/english/", import.meta.url);
const lessons = Object.fromEntries(readdirSync(DIR).filter((f) => /^\d+\.json$/.test(f))
  .map((f) => JSON.parse(readFileSync(new URL(f, DIR), "utf8"))).map((l) => [l.lesson_no, l]));
const spine = JSON.parse(readFileSync(new URL("../data/spine/english-language.json", import.meta.url), "utf8"));
const spineLessons = spine.terms.flatMap((t) => t.lessons);
const titleOf = (n) => spineLessons.find((s) => s.lesson_no === n).title;
const BATCH = Array.from({ length: 16 }, (_, i) => i + 1);
const TAUGHT = Object.values(lessons).filter((l) => !isDeferred(l));
const AUTO = TAUGHT.filter(isAutoMarked);
const TYPES = new Set(["mcq", "spot_error", "ordering", "cloze", "word_order", "matching"]);
const BAD_TEXT = /NaN|undefined|\[object Object\]|Infinity|\{|\}/;
const words = (t) => t.split(/\s+/).filter((w) => /[\p{L}\p{N}]/u.test(w)).length;
const literalDigits = (t) => t.replace(/\{\{|\}\}/g, "").replace(/\{[^{}]*(\{[^{}]*\}[^{}]*)*\}/g, "").match(/[0-9]/g);
const cardTemplates = (l) => (l.teach?.cards || []).filter((c) => !c.check.ref).map((c) => c.check);
const allTemplates = TAUGHT.flatMap((l) => [...(l.questions || []), ...cardTemplates(l)].map((t) => [l, t]));

test("E1 is complete: Lessons 1–16, matching the spine", () => {
  assert.deepEqual(Object.keys(lessons).map(Number).sort((a, b) => a - b), BATCH);
  for (const l of Object.values(lessons)) {
    assert.equal(l.subject, "english-language");
    assert.equal(l.class, "Form 1");
    assert.equal(l.language, "en");
    assert.ok(spineLessons.some((s) => s.lesson_no === l.lesson_no && s.kind === "lesson"), `lesson ${l.lesson_no} is not in the spine`);
  }
});

test("speech-work lessons are deferred (and only they); writing lessons are paper tasks (and only they)", () => {
  for (const l of Object.values(lessons)) {
    const title = titleOf(l.lesson_no);
    assert.equal(isDeferred(l), /^Speech/i.test(title), `lesson ${l.lesson_no}: ${title}`);
    if (isDeferred(l)) {
      assert.ok(l.deferred_reason && !l.teach && !l.questions && !l.note, `lesson ${l.lesson_no}: a deferred lesson has no content`);
      assert.throws(() => lessonSteps(l));
    } else {
      assert.equal(!!l.paper_task, /^Writing/i.test(title), `lesson ${l.lesson_no}: ${title}`);
    }
  }
  assert.deepEqual(checklistLessons(Object.values(lessons).sort((a, b) => a.lesson_no - b.lesson_no)), BATCH.filter((n) => ![4, 8, 12].includes(n)));
});

test("prerequisites point to earlier taught lessons; one skill per lesson, ids unique", () => {
  const skills = new Set();
  for (const l of TAUGHT) {
    for (const p of l.prerequisites) {
      assert.ok(p < l.lesson_no && lessons[p] && !isDeferred(lessons[p]), `lesson ${l.lesson_no}: prerequisite ${p}`);
    }
    assert.equal(l.skills.length, 1);
    assert.ok(/^e\d+$/.test(l.skills[0].id) && !skills.has(l.skills[0].id));
    skills.add(l.skills[0].id);
  }
});

test("notes: draft, at most 150 words", () => {
  for (const l of TAUGHT) {
    assert.equal(l.note.status, "draft", `lesson ${l.lesson_no}`);
    assert.ok(words(l.note.text) <= 150, `lesson ${l.lesson_no} note has ${words(l.note.text)} words`);
  }
});

test("worked examples and paper tasks: draft, no typed numbers, checks pass, nothing left unrendered", () => {
  for (const l of TAUGHT) {
    const we = l.worked_example;
    assert.equal(we.status, "draft");
    for (const t of [we.problem, we.answer, ...we.steps]) assert.equal(literalDigits(t), null, `lesson ${l.lesson_no}: "${t}"`);
    const r = renderWorked(we, lib);
    assert.deepEqual(r.failedChecks, [], `lesson ${l.lesson_no}`);
    for (const t of [r.problem, r.answer, ...r.steps]) assert.ok(!BAD_TEXT.test(t), `lesson ${l.lesson_no}: ${t}`);
    if (l.paper_task) {
      const p = l.paper_task;
      assert.equal(p.status, "draft");
      for (const t of [p.prompt, ...p.model, ...p.checklist]) assert.equal(literalDigits(t), null, `lesson ${l.lesson_no} paper: "${t}"`);
      const rp = renderPaper(l, lib);
      assert.deepEqual(rp.failedChecks, []);
      assert.ok(rp.model.length >= 3 && rp.checklist.length >= 4, `lesson ${l.lesson_no}: model answer and checklist`);
      for (const t of [rp.prompt, ...rp.model, ...rp.checklist]) assert.ok(!BAD_TEXT.test(t), `lesson ${l.lesson_no} paper: ${t}`);
      assert.deepEqual(l.questions, [], `lesson ${l.lesson_no}: a paper lesson has no auto-marked practice`);
    }
  }
});

test("teach cards: 3–4 per lesson, draft, no typed numbers, checks pass, level-1 check question", () => {
  const ids = new Set();
  for (const l of TAUGHT) {
    const cards = l.teach.cards;
    assert.ok(cards.length >= 3 && cards.length <= 4, `lesson ${l.lesson_no} has ${cards.length} cards`);
    for (const c of cards) {
      assert.ok(!ids.has(c.id), `duplicate card ${c.id}`);
      ids.add(c.id);
      assert.equal(c.status, "draft", c.id);
      for (const t of [c.idea, ...c.example]) assert.equal(literalDigits(t), null, `${c.id}: "${t}"`);
      const r = renderCard(c, lib);
      assert.deepEqual(r.failedChecks, [], c.id);
      for (const t of [r.idea, ...r.example]) assert.ok(!BAD_TEXT.test(t), `${c.id}: ${t}`);
      assert.equal(cardCheckTemplate(l, c).level, 1, `${c.id}: check question must be level 1`);
    }
  }
});

test("teach cards: a wrong answer gets a fresh variant", () => {
  for (const l of TAUGHT) for (const c of l.teach.cards) {
    const tpl = cardCheckTemplate(l, c);
    const seen = new Set();
    for (let seed = 1; seed <= 20; seed++) {
      const q = instantiate(tpl, seed, lib, l.lesson_no);
      seen.add(JSON.stringify([q.prompt, q.sentence, q.options?.map((o) => o.text), q.items, q.left, q.right]));
    }
    assert.ok(seen.size > 1, `${c.id}: every variant of ${tpl.id} looks the same`);
  }
});

test("question templates: ids, types, levels 1–3 in every auto-marked lesson; authored ones cite sources", () => {
  const ids = new Set();
  const sources = JSON.parse(readFileSync(new URL("sources.json", DIR), "utf8"));
  for (const [, t] of allTemplates) {
    assert.ok(!ids.has(t.id), `duplicate id ${t.id}`);
    ids.add(t.id);
    assert.ok(TYPES.has(t.type), `${t.id}: type ${t.type}`);
    assert.ok([1, 2, 3].includes(t.level), `${t.id}: level ${t.level}`);
    assert.ok(["authored", "rule"].includes(t.review), `${t.id}: review must be "authored" or "rule"`);
    assert.ok(t.sources?.length, `${t.id} has no sources`);
    for (const s of t.sources) assert.ok(sources[s]?.ref && sources[s]?.checked, `${t.id}: unknown source ${s}`);
    for (const m of t.misconceptions || []) assert.ok(m.explain, `${t.id}: ${m.id} has no explanation`);
  }
  for (const l of AUTO) assert.deepEqual([...new Set(l.questions.map((t) => t.level))].sort(), [1, 2, 3], `lesson ${l.lesson_no}`);
});

for (const [l, tpl] of allTemplates) {
  test(`${tpl.id}: ${SEEDS} seeds give correct, well-formed questions with full working`, () => {
    const positions = new Set();
    for (let seed = 1; seed <= SEEDS; seed++) {
      const q = instantiate(tpl, seed, lib, l.lesson_no);
      const where = `${tpl.id} seed ${seed}`;
      assert.equal(q.verified, true, `${where}: not verified (${q.answer})`);
      for (const t of [q.prompt, q.sentence, String(q.answer), q.hint].filter((x) => x !== undefined)) assert.ok(!BAD_TEXT.test(t), `${where}: "${t}"`);
      if (q.type === "cloze" && q.mode === "type") {
        assert.deepEqual(check(q, q.answer), { correct: true }, where);
        assert.deepEqual(check(q, `  ${q.answer.toUpperCase()} `), { correct: true }, `${where}: case and spaces`);
        for (const a of q.accept) assert.equal(check(q, a).correct, true, `${where}: accepted "${a}"`);
        for (const m of q.misconceptions) {
          const r = check(q, m.value);
          assert.equal(r.correct, false, `${where}: misconception ${m.id} "${m.value}" is accepted`);
          assert.ok(r.misconception?.explain && !BAD_TEXT.test(r.misconception.explain), `${where}: ${m.id}`);
        }
        assert.ok(q.sentence.includes("___") && q.full.includes(q.answer), where);
      } else if (q.type === "mcq" || q.type === "spot_error" || (q.type === "cloze" && q.mode === "choose")) {
        const texts = q.options.map((o) => o.text);
        assert.equal(new Set(texts.map(normaliseText)).size, texts.length, `${where}: repeated option in ${texts}`);
        for (const t of texts) assert.ok(!BAD_TEXT.test(t), `${where}: ${t}`);
        q.options.forEach((o, i) => {
          const r = check(q, i);
          assert.equal(r.correct, i === q.correctIndex, `${where}: option ${i}`);
          if (!r.correct && q.type !== "spot_error") assert.ok(r.misconception?.explain && !BAD_TEXT.test(r.misconception.explain), `${where}: no feedback for "${o.text}"`);
        });
        positions.add(q.correctIndex);
      } else if (q.type === "ordering") {
        assert.equal(check(q, q.correctOrder).correct, true, where);
        assert.equal(check(q, q.items.map((_, i) => i)).correct, false, `${where}: shown already in order`);
      } else if (q.type === "word_order") {
        for (const t of q.items) assert.ok(!BAD_TEXT.test(t), `${where}: ${t}`);
        assert.equal(check(q, q.correctOrder).correct, true, where);
        assert.equal(check(q, q.items.map((_, i) => i)).correct, false, `${where}: shown already in order`);
      } else if (q.type === "matching") {
        for (const t of [...q.left, ...q.right]) assert.ok(!BAD_TEXT.test(t), `${where}: ${t}`);
        assert.deepEqual(check(q, q.correctMatch), { correct: true }, where);
        if (!q.groups) assert.equal(new Set(q.right).size, q.right.length, where);
      }
      assert.ok(q.solution?.length, `${where}: no working`);
      for (const line of q.solution) assert.ok(line.trim() && !BAD_TEXT.test(line), `${where}: "${line}"`);
      const shown = q.solution.join("\n");
      if (q.type === "matching") q.left.forEach((x, i) => assert.ok(shown.includes(`${x} → ${q.right[q.correctMatch[i]]}`), where));
      else assert.ok(shown.includes(q.answer), `${where}: working does not show the answer "${q.answer}": ${shown}`);
    }
    if (positions.size) assert.ok(positions.size > 1, `${tpl.id}: the right answer is always in position ${[...positions]}`);
  });
}

test("full working and hints: no typed numbers", () => {
  for (const [, t] of allTemplates) for (const s of [...(t.solution || []), t.hint].filter(Boolean)) {
    assert.equal(literalDigits(s), null, `${t.id}: "${s}"`);
  }
});

test("typed answers: case- and space-insensitive, but the letters must be right", () => {
  const tpl = lessons[3].questions.find((t) => t.id === "e3-form");
  const q = instantiate(tpl, 7, lib, 3);
  assert.equal(check(q, q.answer.toUpperCase()).correct, true);
  assert.equal(check(q, ` ${q.answer}   `).correct, true);
  assert.equal(check(q, q.answer + "x").correct, false);
});
