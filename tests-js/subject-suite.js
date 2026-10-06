// A content test suite shared by subjects after Maths and English (first used by Physics, 2026-10-07).
// Same rules: every template across 1000 seeds, notes ≤ 150 words, 3–4 draft cards with a level-1 check,
// worked examples and working with no typed numbers, levels 1–3 in every auto-marked lesson, sources exist.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import { instantiate, check, renderWorked } from "../src/engine/template.js";
import { renderCard, cardCheckTemplate, renderPaper, isDeferred, isAutoMarked } from "../src/engine/teach.js";

const BAD_TEXT = /NaN|undefined|\[object Object\]|Infinity|\{|\}/;
const words = (t) => t.split(/\s+/).filter((w) => /[\p{L}\p{N}]/u.test(w)).length;
/**
 * Literal digits outside {…}. A bare 1 in front of a unit is allowed ("1 km = {factor('km', 'm')} m"): it is the
 * definition, not a result. Every other number must be computed (TR-P01).
 */
const literalDigits = (t) => t.replace(/(^|[^\d.,])1 (?=[A-Za-zµ°{])/g, "$1").replace(/\{[^{}]*(\{[^{}]*\}[^{}]*)*\}/g, "").match(/[0-9]/g);
const SVG = /^<svg [^>]*role="img"[\s\S]*<\/svg>$/;

export function subjectSuite({ subject, spine, lib, batch, prefix }) {
  const DIR = new URL(`../content/${subject}/`, import.meta.url);
  const lessons = Object.fromEntries(readdirSync(DIR).filter((f) => /^\d+\.json$/.test(f))
    .map((f) => JSON.parse(readFileSync(new URL(f, DIR), "utf8"))).map((l) => [l.lesson_no, l]));
  const spineLessons = JSON.parse(readFileSync(new URL(`../data/spine/${spine}.json`, import.meta.url), "utf8")).terms.flatMap((t) => t.lessons);
  const sources = JSON.parse(readFileSync(new URL("sources.json", DIR), "utf8"));
  const TAUGHT = Object.values(lessons).filter((l) => !isDeferred(l));
  const AUTO = TAUGHT.filter(isAutoMarked);
  const cardTemplates = (l) => l.teach.cards.filter((c) => !c.check.ref).map((c) => c.check);
  const allTemplates = TAUGHT.flatMap((l) => [...l.questions, ...cardTemplates(l)].map((t) => [l, t]));
  const figureOk = (f, where) => { assert.match(f, SVG, `${where}: figure is not an SVG`); assert.doesNotMatch(f, /NaN|undefined|Infinity/, where); };

  test(`${subject}: the batch is complete and matches the spine`, () => {
    assert.deepEqual(Object.keys(lessons).map(Number).sort((a, b) => a - b), batch);
    for (const l of Object.values(lessons)) {
      assert.equal(l.subject, subject);
      assert.equal(l.class, "Form 1");
      assert.ok(spineLessons.some((s) => s.lesson_no === l.lesson_no && s.kind === "lesson"), `lesson ${l.lesson_no} is not in the spine`);
    }
  });

  test(`${subject}: prerequisites point to earlier lessons; one skill per lesson with the subject prefix`, () => {
    const skills = new Set();
    for (const l of TAUGHT) {
      for (const p of l.prerequisites) assert.ok(p < l.lesson_no && lessons[p], `lesson ${l.lesson_no}: prerequisite ${p}`);
      assert.equal(l.skills.length, 1);
      assert.ok(new RegExp(`^${prefix}\\d+$`).test(l.skills[0].id) && !skills.has(l.skills[0].id), l.skills[0].id);
      skills.add(l.skills[0].id);
    }
  });

  test(`${subject}: notes are draft and at most 150 words`, () => {
    for (const l of TAUGHT) {
      assert.equal(l.note.status, "draft");
      assert.ok(words(l.note.text) <= 150, `lesson ${l.lesson_no} note has ${words(l.note.text)} words`);
    }
  });

  test(`${subject}: worked examples are draft, with no typed numbers, checks pass and figures draw`, () => {
    for (const l of TAUGHT) {
      const we = l.worked_example;
      assert.equal(we.status, "draft");
      for (const t of [we.problem, we.answer, ...we.steps]) assert.equal(literalDigits(t), null, `lesson ${l.lesson_no}: "${t}"`);
      const r = renderWorked(we, lib);
      assert.deepEqual(r.failedChecks, [], `lesson ${l.lesson_no}`);
      for (const t of [r.problem, r.answer, ...r.steps]) assert.ok(!BAD_TEXT.test(t), `lesson ${l.lesson_no}: ${t}`);
      if (we.figure) figureOk(r.figure, `lesson ${l.lesson_no} worked example`);
      if (l.paper_task) assert.deepEqual(renderPaper(l, lib).failedChecks, []);
    }
  });

  test(`${subject}: 3–4 draft cards per lesson, no typed numbers, checks pass, level-1 check question`, () => {
    const ids = new Set();
    for (const l of TAUGHT) {
      assert.ok(l.teach.cards.length >= 3 && l.teach.cards.length <= 4, `lesson ${l.lesson_no}`);
      for (const c of l.teach.cards) {
        assert.ok(!ids.has(c.id), `duplicate card ${c.id}`);
        ids.add(c.id);
        assert.equal(c.status, "draft", c.id);
        for (const t of [c.idea, ...c.example]) assert.equal(literalDigits(t), null, `${c.id}: "${t}"`);
        const r = renderCard(c, lib);
        assert.deepEqual(r.failedChecks, [], c.id);
        for (const t of [r.idea, ...r.example]) assert.ok(!BAD_TEXT.test(t), `${c.id}: ${t}`);
        if (c.figure) figureOk(r.figure, c.id);
        assert.equal(cardCheckTemplate(l, c).level, 1, `${c.id}: check question must be level 1`);
        const seen = new Set();
        for (let seed = 1; seed <= 20; seed++) {
          const q = instantiate(cardCheckTemplate(l, c), seed, lib, l.lesson_no);
          seen.add(JSON.stringify([q.prompt, q.sentence, q.options?.map((o) => o.text), q.items, q.left, q.figure]));
        }
        assert.ok(seen.size > 1, `${c.id}: every variant of its check looks the same`);
      }
    }
  });

  test(`${subject}: template ids, types, levels 1–3 per lesson, sources`, () => {
    const ids = new Set();
    for (const [, t] of allTemplates) {
      assert.ok(!ids.has(t.id), `duplicate id ${t.id}`);
      ids.add(t.id);
      assert.ok(t.id.startsWith(prefix), `${t.id}: ids start with "${prefix}"`);
      assert.ok([1, 2, 3].includes(t.level), `${t.id}: level ${t.level}`);
      assert.ok(["authored", "rule"].includes(t.review), `${t.id}: review`);
      assert.ok(t.sources?.length, `${t.id} has no sources`);
      for (const s of t.sources) assert.ok(sources[s]?.ref && sources[s]?.checked, `${t.id}: unknown source ${s}`);
      for (const m of t.misconceptions || []) assert.ok(m.explain, `${t.id}: ${m.id} has no explanation`);
      for (const s of [...(t.solution || []), t.hint].filter(Boolean)) assert.equal(literalDigits(s), null, `${t.id}: "${s}"`);
    }
    for (const l of AUTO) assert.deepEqual([...new Set(l.questions.map((t) => t.level))].sort(), [1, 2, 3], `lesson ${l.lesson_no}`);
  });

  for (const [l, tpl] of allTemplates) {
    test(`${tpl.id}: 1000 seeds give correct, well-formed questions with full working`, () => {
      const positions = new Set();
      for (let seed = 1; seed <= 1000; seed++) {
        const q = instantiate(tpl, seed, lib, l.lesson_no);
        const where = `${tpl.id} seed ${seed}`;
        assert.equal(q.verified, true, `${where}: not verified (${q.answer})`);
        for (const t of [q.prompt, q.sentence, String(q.answer), q.hint, q.unit].filter((x) => x !== undefined)) assert.ok(!BAD_TEXT.test(t), `${where}: "${t}"`);
        if (q.figure) figureOk(q.figure, where);
        if (q.type === "numeric") {
          assert.deepEqual(check(q, q.answer), { correct: true }, where);
          assert.deepEqual(check(q, String(q.answerValue)), { correct: true }, where);
          for (const m of q.misconceptions) {
            const r = check(q, m.value);
            assert.equal(r.correct, false, `${where}: misconception ${m.id} gives the right answer`);
            assert.ok(r.misconception?.explain && !BAD_TEXT.test(r.misconception.explain), `${where}: ${m.id}`);
          }
        } else if (q.type === "cloze" && q.mode === "type") {
          assert.deepEqual(check(q, q.answer), { correct: true }, where);
        } else if (q.options) {
          const texts = q.options.map((o) => o.text);
          // tapped options are compared exactly: "Cu", "CU" and "cu" are different answers to a question about capitals
          assert.equal(new Set(texts).size, texts.length, `${where}: repeated option in ${texts}`);
          for (const t of texts) assert.ok(!BAD_TEXT.test(t), `${where}: ${t}`);
          q.options.forEach((o, i) => {
            const r = check(q, i);
            assert.equal(r.correct, i === q.correctIndex, `${where}: option ${i}`);
            if (!r.correct && q.type !== "spot_error") assert.ok(r.misconception?.explain && !BAD_TEXT.test(r.misconception.explain), `${where}: no feedback for "${o.text}"`);
          });
          positions.add(q.correctIndex);
        } else if (q.type === "ordering" || q.type === "word_order") {
          assert.equal(check(q, q.correctOrder).correct, true, where);
          assert.equal(check(q, q.items.map((_, i) => i)).correct, false, `${where}: shown already in order`);
        } else if (q.type === "matching") {
          for (const t of [...q.left, ...q.right]) assert.ok(!BAD_TEXT.test(t), `${where}: ${t}`);
          assert.deepEqual(check(q, q.correctMatch), { correct: true }, where);
        }
        assert.ok(q.solution?.length, `${where}: no working`);
        for (const line of q.solution) assert.ok(line.trim() && !BAD_TEXT.test(line), `${where}: "${line}"`);
        const shown = q.solution.join("\n");
        if (q.type === "matching") q.left.forEach((x, i) => assert.ok(shown.includes(`${x} → ${q.right[q.correctMatch[i]]}`), where));
        else assert.ok(shown.includes(String(q.answer)), `${where}: working does not show the answer "${q.answer}": ${shown}`);
      }
      if (positions.size) assert.ok(positions.size > 1, `${tpl.id}: the right answer is always in position ${[...positions]}`);
    });
  }
}
