// Teach mode (decision 2026-10-02: the app is the pupil's main teacher).
//
//   cards (3-4: one idea + a tiny example + 1 level-1 check question each)
//   → worked example → practice (one question per template, levels 1 to 3) → the note, as a summary.
//
// Every card check and practice question follows the same two-try rule:
//   1st miss (wrong or "I don't know") → feedback (cards: the card's example again) → a fresh variant
//   2nd miss → the correct answer with full working → move on, marked "needs review"   (2026-10-03)
// Pure functions; the UI holds the flow object.

import { render, evaluate } from "./expr.js";
import { sampleScope, instantiate } from "./template.js";
import { makeRng } from "./rng.js";

const show = (lib) => (v) => (typeof v === "number" ? lib.fmt(v) : String(v));

/** A card's check question: a level-1 template of the lesson ({ref}) or an inline one. */
export function cardCheckTemplate(lesson, card) {
  const tpl = card.check.ref ? lesson.questions.find((t) => t.id === card.check.ref) : card.check;
  if (!tpl) throw new Error(`card ${card.id}: no template ${card.check.ref}`);
  return tpl;
}

/** Renders a card's idea and example from its fixed vars: every number is computed. */
export function renderCard(card, lib) {
  const scope = sampleScope(card.vars, null, makeRng(1), lib);
  const R = (t) => render(t, scope, lib, show(lib));
  return {
    id: card.id,
    idea: R(card.idea),
    example: card.example.map(R),
    failedChecks: (card.checks || []).filter((c) => evaluate(c, scope, lib) !== true),
  };
}

/** Practice list: every template of the lesson once, easiest first. */
export function practicePlan(lesson) {
  return [...lesson.questions].sort((a, b) => a.level - b.level).map((t) => t.id);
}

export function lessonSteps(lesson) {
  return [
    ...lesson.teach.cards.map((_, i) => ({ kind: "card", card: i })),
    { kind: "worked_example" },
    ...practicePlan(lesson).map((id) => ({ kind: "practice", template: id })),
    { kind: "note" },
  ];
}

/** The template behind a card or practice step. */
export function stepTemplate(lesson, step) {
  return step.kind === "card" ? cardCheckTemplate(lesson, lesson.teach.cards[step.card])
    : lesson.questions.find((t) => t.id === step.template);
}

const isItem = (step) => step?.kind === "card" || step?.kind === "practice";

/**
 * phase:
 *   "idea"   card only: read the idea and the example
 *   "check"  answer a question (attempt 0, then 1 on the fresh variant)
 *   "retry"  after a first miss: feedback, and for cards the example again, then a fresh variant
 *   "reveal" after a second miss: the correct answer with full working, then move on
 */
export function startTeach(lesson, seed) {
  const steps = lessonSteps(lesson);
  return { lesson: lesson.lesson_no, steps, step: 0, attempt: 0, phase: phaseFor(steps[0]), seed, log: [] };
}

function phaseFor(step) {
  if (step?.kind === "card") return "idea";
  if (step?.kind === "practice") return "check";
  return "read";
}

/** Seed for the current question: a new attempt starts from a different seed. */
export const checkSeed = (flow) => flow.seed + flow.step * 1000 + flow.attempt * 97;

const signature = (q) => JSON.stringify([q.prompt, q.options?.map((o) => o.text), q.items]);

/**
 * The question for the current card or practice step. On a retry, seeds are tried until the
 * question differs from the one just answered (templates with few variants could repeat it).
 */
export function itemQuestion(lesson, flow, lib, previous = null) {
  const tpl = stepTemplate(lesson, flow.steps[flow.step]);
  let q;
  for (let k = 0; k < 50; k++) {
    q = instantiate(tpl, checkSeed(flow) + k, lib, lesson.lesson_no);
    if (!previous || signature(q) !== signature(previous)) return q;
  }
  return q;  // a template with a single variant: same question, options reshuffled where possible
}
export const cardQuestion = itemQuestion;

const advance = (flow, extra = {}) => {
  const step = flow.step + 1;
  return { ...flow, ...extra, step, attempt: 0, phase: phaseFor(flow.steps[step]) };
};

/** The pupil pressed "Next" / "I'm ready" / "Try a new question" / "Continue". */
export function nextPhase(flow) {
  const step = flow.steps[flow.step];
  if (step?.kind === "card" && flow.phase === "idea") return { ...flow, phase: "check" };
  if (isItem(step) && flow.phase === "retry") return { ...flow, phase: "check" };
  if (isItem(step) && flow.phase === "check") throw new Error("answer the question first");
  return advance(flow);  // "reveal", the worked example and the note all move on
}

/**
 * Records the answer to the current card or practice question.
 * result: {correct, dontKnow?}. The new flow's phase tells the UI what to show next:
 * the next step, "retry" (feedback then a fresh variant) or "reveal" (answer with full working).
 */
export function answerItem(flow, result, ms) {
  const step = flow.steps[flow.step];
  if (!isItem(step) || flow.phase !== "check") throw new Error("answerItem outside a question");
  const entry = { step: flow.step, kind: step.kind, attempt: flow.attempt, correct: !!result.correct, dontKnow: !!result.dontKnow, ms };
  if (result.correct) return advance(flow, { log: [...flow.log, entry] });
  if (flow.attempt === 0) return { ...flow, log: [...flow.log, entry], attempt: 1, phase: "retry" };
  return { ...flow, log: [...flow.log, { ...entry, needsReview: true }], phase: "reveal" };
}
export const answerCard = answerItem;

export const isDone = (flow) => flow.step >= flow.steps.length;

/** Steps the pupil missed twice, for the results and for later review. */
export const needsReview = (flow) => flow.log.filter((e) => e.needsReview).map((e) => flow.steps[e.step]);
