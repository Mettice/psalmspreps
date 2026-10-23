// Pupil state, Lesson 0 readiness, teach-mode flow and "I don't know" (decisions 2026-10-02 and 2026-10-03).
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import * as lib from "../src/engine/lib/maths.js";
import { instantiate, check, DONT_KNOW } from "../src/engine/template.js";
import { buildReadiness, scoreReadiness, readinessValidity } from "../src/engine/readiness.js";
import { emptyState, applyChecklist, applyReadiness, masteryOf, coverageOf, skillOf, skillsOf } from "../src/engine/state.js";
import { startTeach, nextPhase, answerItem, isDone, lessonSteps, practicePlan, cardCheckTemplate, itemQuestion, needsReview, renderLearn, isStuck, easyStep } from "../src/engine/teach.js";

const DIR = new URL("../content/maths/", import.meta.url);
const lessons = Object.fromEntries(readdirSync(DIR).filter((f) => /^\d+\.json$/.test(f))
  .map((f) => JSON.parse(readFileSync(new URL(f, DIR), "utf8"))).map((l) => [l.lesson_no, l]));
const l0 = lessons[0];

// ---------------------------------------------------------------- coverage and mastery
test("every lesson starts not_taught and mastery unknown; only the checklist changes coverage", () => {
  const s = emptyState();
  for (let n = 0; n <= 68; n++) assert.equal(coverageOf(s, n), "not_taught");
  assert.equal(masteryOf(s, "m8"), "unknown");
  const s1 = applyChecklist(s, { 3: true, 4: false });
  assert.deepEqual([coverageOf(s1, 3), coverageOf(s1, 4), coverageOf(s1, 5)], ["taught", "not_taught", "not_taught"]);
  assert.equal(s1.coverageSource[3], "checklist");
  assert.deepEqual(s1.mastery, s.mastery);
});

test("skills: multi-skill lessons tag every template and card", () => {
  for (const l of Object.values(lessons)) {
    if (!l.skills) continue;
    const ids = skillsOf(l);
    for (const t of l.questions) assert.ok(ids.includes(t.skill), `${t.id}: skill ${t.skill}`);
    for (const c of l.teach.cards) {
      assert.ok(ids.includes(c.skill), `${c.id}: skill ${c.skill}`);
      assert.equal(skillOf(l, cardCheckTemplate(l, c)), c.skill, `${c.id}: check question trains another skill`);
    }
  }
});

// ---------------------------------------------------------------- Lesson 0 readiness
const resultsFor = (pattern) => l0.readiness.items.map((it, i) => ({ template: it.template, correct: pattern(it, i) }));

test("readiness: score, per-area results and weak foundations", () => {
  const all = scoreReadiness(l0, resultsFor(() => true));
  assert.deepEqual([all.right, all.asked, all.percent, all.weak], [15, 15, 100, []]);
  const none = scoreReadiness(l0, resultsFor(() => false));
  assert.deepEqual(none.weak.sort(), ["operations", "place_value", "remainders", "tables", "word_problems"]);
  // tables all wrong, everything else right: only tables is weak
  const area = (id) => l0.questions.find((t) => t.id === id).area;
  const tablesWeak = scoreReadiness(l0, resultsFor((it) => area(it.template) !== "tables"));
  assert.deepEqual(tablesWeak.weak, ["tables"]);
  assert.equal(tablesWeak.areas.tables.right, 0);
  // 2 of 3 right is not weak; 1 of 3 is
  const twoOfThree = scoreReadiness(l0, resultsFor((it, i) => !(area(it.template) === "place_value" && i === 0)));
  assert.equal(twoOfThree.areas.place_value.weak, false);
});

test("readiness sets no Form 1 mastery and no coverage", () => {
  const before = applyChecklist(emptyState(), { 3: true });
  const after = applyReadiness(before, scoreReadiness(l0, resultsFor(() => false)), "2026-10-02");
  assert.deepEqual(after.mastery, before.mastery);
  assert.deepEqual(after.coverage, before.coverage);
  assert.deepEqual(after.readiness.weak.length, 5);
  assert.equal(masteryOf(after, "m3"), "unknown");
});

test("readiness skipped through is not used: 80% or more \"I don't know\" or under 3 seconds (2026-10-24)", () => {
  const rows = (k, result, seconds) => Array.from({ length: k }, () => ({ result, seconds }));
  assert.equal(readinessValidity([]).valid, false);
  assert.equal(readinessValidity(rows(13, "idk", 1)).valid, false);
  assert.equal(readinessValidity(rows(13, "wrong", 1.2)).valid, false);             // tapped through
  assert.equal(readinessValidity([...rows(11, "idk", 6), ...rows(2, "wrong", 20)]).valid, false);  // 11 of 13 skipped
  assert.equal(readinessValidity(rows(13, "wrong", 25)).valid, true);              // tried and got them wrong: real
  assert.equal(readinessValidity([...rows(10, "idk", 6), ...rows(5, "right", 20)]).valid, true);   // 10 of 15
  assert.deepEqual(readinessValidity(rows(13, "idk", 1)), { valid: false, skipped: 13, asked: 13 });
});

test("readiness questions build and verify for many seeds", () => {
  for (let seed = 1; seed <= 300; seed++) {
    const qs = buildReadiness(l0, seed, lib);
    assert.equal(qs.length, l0.readiness.items.length);
    assert.ok(qs.every((q) => q.verified));
  }
});

// ---------------------------------------------------------------- teach mode flow
test("teach flow: cards → worked example → one practice step per template (easiest first) → note", () => {
  const steps = lessonSteps(lessons[3]);
  const plan = practicePlan(lessons[3]);
  assert.deepEqual(steps.map((s) => s.kind), ["card", "card", "card", "worked_example", ...plan.map(() => "practice"), "note"]);
  assert.deepEqual(steps.filter((s) => s.kind === "practice").map((s) => s.template), plan);
  const levels = plan.map((id) => lessons[3].questions.find((t) => t.id === id).level);
  assert.deepEqual(levels, [...levels].sort());
});

test("teach flow: Learn screens come first, one per section plus key words; they are read, not answered", () => {
  const learn = { status: "draft", vars: { a: 3, b: 4 }, sections: [{ heading: "Adding", text: "{a} + {b} = {a + b}" }, { heading: "Order", text: "Either order works." }],
    key_words: [{ word: "sum", meaning: "the answer to an addition" }], mistake: { wrong: "{a} + {b} = {a * b}", right: "{a} + {b} = {a + b}", why: "Add, do not multiply." } };
  const l = { ...lessons[3], learn };
  const steps = lessonSteps(l);
  assert.deepEqual(steps.slice(0, 4).map((s) => s.kind), ["learn", "learn", "learn", "card"]);
  const r = renderLearn(l, lib);
  assert.equal(r.pages.length, 3);
  assert.equal(r.pages[0].text, "3 + 4 = 7");
  assert.equal(r.pages[2].mistake.wrong, "3 + 4 = 12");
  let f = startTeach(l, 1);
  assert.equal(f.phase, "read");
  f = nextPhase(nextPhase(nextPhase(f)));
  assert.deepEqual([f.step, f.phase], [3, "idea"]);
  const noWords = lessonSteps({ ...lessons[3], learn: { ...learn, key_words: undefined, mistake: undefined } });
  assert.equal(noWords.filter((s) => s.kind === "learn").length, 2);
});

test("teach flow: right moves on; 1st miss → retry with a fresh variant; 2nd miss → reveal working, needs review", () => {
  let f = startTeach(lessons[3], 100);
  assert.equal(f.phase, "idea");
  f = nextPhase(f);                                    // card 1: idea read -> question
  assert.equal(f.phase, "check");
  f = answerItem(f, { correct: true }, 4000);
  assert.deepEqual([f.step, f.phase, f.attempt], [1, "idea", 0]);

  f = nextPhase(f);
  const first = itemQuestion(lessons[3], f, lib);
  f = answerItem(f, { correct: false }, 9000);
  assert.deepEqual([f.step, f.phase, f.attempt], [1, "retry", 1], "1st miss: feedback + the card's example again");
  f = nextPhase(f);
  assert.equal(f.phase, "check");
  const second = itemQuestion(lessons[3], f, lib, first);
  assert.notEqual(second.prompt + JSON.stringify(second.options?.map((o) => o.text)), first.prompt + JSON.stringify(first.options?.map((o) => o.text)));
  f = answerItem(f, { correct: false, dontKnow: true }, 7000);
  assert.deepEqual([f.step, f.phase], [1, "reveal"], "2nd miss (IDK counts): show the answer with full working");
  assert.ok(second.solution.length && second.solution.join(" ").includes(second.answer));
  assert.throws(() => answerItem(f, { correct: true }), "no third attempt");
  f = nextPhase(f);                                    // working read -> move on
  assert.deepEqual([f.step, f.phase], [2, "idea"]);
  assert.deepEqual(needsReview(f), [{ kind: "card", card: 1 }]);

  f = answerItem(nextPhase(f), { correct: true }, 2000);    // card 3
  assert.equal(f.steps[f.step].kind, "worked_example");
  f = nextPhase(f);                                    // -> first practice question
  assert.equal(f.steps[f.step].kind, "practice");
  assert.equal(f.phase, "check", "practice starts straight at the question");
  f = answerItem(f, { correct: false }, 1);
  assert.equal(f.phase, "retry", "practice: 1st miss -> feedback, then a fresh variant");
  f = answerItem(nextPhase(f), { correct: false }, 1);
  assert.equal(f.phase, "reveal", "practice: 2nd miss -> full working");
  const practiceStep = f.steps[f.step];
  f = nextPhase(f);
  assert.ok(needsReview(f).some((s) => s === practiceStep));
  while (!isDone(f)) f = f.phase === "check" ? answerItem(f, { correct: true }, 1) : nextPhase(f);
  assert.equal(needsReview(f).length, 2);
});

test("teach flow: the fresh variant really differs from the first question, for every card and practice step", () => {
  const sig = (q) => JSON.stringify([q.prompt, q.options?.map((o) => o.text), q.items]);
  for (const l of Object.values(lessons).filter((x) => x.teach)) {
    lessonSteps(l).forEach((step, i) => {
      if (step.kind !== "card" && step.kind !== "practice") return;
      for (const seed of [1, 7, 42, 99, 2026]) {
        let f = { ...startTeach(l, seed), step: i, phase: "check" };
        const a = itemQuestion(l, f, lib);
        f = nextPhase(answerItem(f, { correct: false }, 1));
        const b = itemQuestion(l, f, lib, a);
        assert.notEqual(sig(b), sig(a), `lesson ${l.lesson_no} step ${i} seed ${seed}: the retry repeated the same question`);
      }
    });
  }
});

// ---------------------------------------------------------------- I don't know
test("I don't know: incorrect, no misconception, shows hint (if any) and worked example", () => {
  const withHint = lessons[8].questions.find((t) => t.id === "m8-to-base");
  const q = instantiate(withHint, 5, lib, 8);
  assert.deepEqual(check(q, DONT_KNOW), { correct: false, dontKnow: true, misconception: null, show: ["hint", "worked_example"] });
  const noHint = instantiate(lessons[7].questions.find((t) => t.id === "m7-power"), 5, lib, 7);
  assert.deepEqual(check(noHint, DONT_KNOW).show, ["worked_example"]);
  const mcq = instantiate(lessons[3].questions.find((t) => t.id === "m3-value-of-digit"), 5, lib, 3);
  assert.equal(check(mcq, DONT_KNOW).misconception, null);
});

// ---------------------------------------------------------------- stuck guard and step-by-step run (2026-10-24)
// A pupil spent 33 minutes on Lesson 8 and missed 4 of 5 card questions: the lesson now stops kindly instead.
const answerAs = (flow, results) => results.reduce((f, [ok, ms]) => {
  let g = f.phase === "idea" || f.phase === "retry" ? nextPhase(f) : f;
  g = answerItem(g, { correct: ok }, ms);
  return g.phase === "reveal" ? nextPhase(g) : g;
}, flow);

test("stuck guard: two cards missed twice stop the lesson; one is not enough", () => {
  const l8 = lessons[8];
  const one = answerAs(startTeach(l8, 1), [[true, 8000], [false, 5000], [false, 45000]]);
  assert.equal(isStuck(one), false);
  const two = answerAs(one, [[false, 287000], [false, 183000]]);
  assert.equal(isStuck(two), true);
  // the easy question to end on: the level-1 card he got right (card 1)
  assert.equal(easyStep(l8, two), 0);
});

test("stuck guard: 15 minutes with fewer than half right stops the lesson; slow but mostly right does not", () => {
  const l8 = lessons[8];
  const slowWrong = answerAs(startTeach(l8, 1), [[true, 300000], [false, 300000], [true, 300000], [false, 300000]]);
  assert.equal(isStuck(slowWrong), false, "half right is not fewer than half");
  const worse = answerAs(slowWrong, [[false, 60000]]);
  assert.equal(isStuck(worse), true);
  const slowRight = answerAs(startTeach(l8, 1), [[true, 400000], [true, 400000], [true, 400000]]);
  assert.equal(isStuck(slowRight), false);
});

test("step-by-step run: a lesson that came back asks scaffolded questions from the first try", () => {
  const l8 = lessons[8];
  const plain = startTeach(l8, 5), guided = startTeach(l8, 5, { guided: true });
  const atCard = (f, i) => ({ ...f, step: f.steps.findIndex((s) => s.kind === "card" && s.card === i), phase: "check" });
  // card 2 (base b to base ten) and card 3 (base ten to base b) have a step-by-step form; card 1 does not
  assert.equal(itemQuestion(l8, atCard(plain, 1), lib).type, "numeric");
  assert.equal(itemQuestion(l8, atCard(guided, 1), lib).type, "blanks");
  assert.equal(itemQuestion(l8, atCard(guided, 2), lib).type, "blanks");
  assert.equal(itemQuestion(l8, atCard(guided, 0), lib).type, "mcq");
});
