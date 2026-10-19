// Help after a miss (2026-10-19): the usual wrong answers are diagnosed, the retry is asked step by step
// (scaffold → blanks), the example shown has the same shape as the question, and the place values are drawn.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import * as lib from "../src/engine/lib/maths.js";
import { instantiate, check, scaffoldTemplate, DONT_KNOW, inputModeFor } from "../src/engine/template.js";
import * as teach from "../src/engine/teach.js";

const L8 = JSON.parse(readFileSync(new URL("../content/maths/8.json", import.meta.url), "utf8"));
const card = L8.teach.cards.find((c) => c.id === "c8-2");
const toTen = L8.questions.find((t) => t.id === "m8-to-ten");
const fixed = (tpl, vars) => ({ ...tpl, vars, where: undefined });  // one known question

test("library: place values, the scaffold line and its answers, the usual wrong answers", () => {
  assert.deepEqual(lib.placeValues("22", 4), [4, 1]);
  assert.deepEqual(lib.placeValues("123", 5), [25, 5, 1]);
  assert.equal(lib.placeBlanks("22"), "2 × ___ + 2 × ___ = ___");
  assert.deepEqual(lib.placeAnswers("22", 4), [4, 1, 10]);
  assert.equal(lib.digitSum("22"), 4);
  assert.equal(lib.digitProduct("22"), 4);
  assert.equal(lib.placeReversed("31", 4), 7);
  assert.equal(lib.placeHeads("123", 5), "25s, 5s, 1s");
  assert.deepEqual(lib.placeSteps("22", 4).split("\n"), ["In base 4 the places are worth 4s, 1s.",
    "Multiply each digit by its place value: 2 × 4 = 8, 2 × 1 = 2.", "Add: 8 + 2 = 10.", "So 22₄ = 10 in base ten."]);
  const svg = lib.placeTable("22", 4);
  assert.match(svg, /^<svg[^>]+role="img"/);
  assert.ok(svg.includes(">4s<") && svg.includes(">1s<") && svg.includes(">2<"));
  assert.ok(!svg.includes("10"), "the drawing does not give the answer");
});

test("22 in base four: 22, 4 (added) and 4 (multiplied) each get their own hint, without the answer", () => {
  const q = instantiate(fixed(card.check, { b: 4, n: 10, s: "22" }), 1, lib);
  assert.equal(q.answer, "10");
  const as = (x) => check(q, x);
  assert.equal(as("10").correct, true);
  assert.equal(as("22").misconception.id, "read-as-ten");
  assert.match(as("22").misconception.explain, /left digit is worth 4s, not 10s/);
  assert.equal(as("4").misconception.id, "added-digits");   // 2 + 2 and 2 × 2 are both 4: the same step is missing
  assert.match(as("4").misconception.explain, /multiplied by its place value first \(4s, 1s\)/);
  assert.equal(as("7").misconception, null);                // anything else: no diagnosis, the scaffold follows
  for (const m of q.misconceptions) assert.ok(!m.explain.includes(" 10.") && !m.explain.includes("= 10"), m.explain);
  assert.ok(q.figure.includes(">4s<"), "the card check shows the place values above the digits");
});

test("multiplied digits and reversed places are diagnosed too", () => {
  const q = instantiate(fixed(card.check, { b: 5, n: 17, s: "32" }), 1, lib);
  assert.equal(check(q, "6").misconception.id, "multiplied-digits");
  assert.equal(check(q, "5").misconception.id, "added-digits");
  assert.equal(check(q, "13").misconception.id, "places-reversed");  // 2 × 5 + 3
});

test("blanks: every box is checked; the full line is the answer", () => {
  const q = instantiate(scaffoldTemplate(fixed(card.check, { b: 4, n: 10, s: "22" })), 1, lib);
  assert.equal(q.type, "blanks");
  assert.deepEqual(q.parts, ["22₄ = 2 × ", " + 2 × ", " = ", ""]);
  assert.equal(q.answer, "22₄ = 2 × 4 + 2 × 1 = 10");
  assert.equal(inputModeFor(q), "numeric");
  assert.equal(check(q, ["4", "1", "10"]).correct, true);
  assert.deepEqual(check(q, ["4", "1", "8"]).wrongBlanks, [2]);
  assert.deepEqual(check(q, ["10", "1", "22"]).wrongBlanks, [0, 2]);
  assert.equal(check(q, DONT_KNOW).dontKnow, true);
  assert.ok(q.solution.length && q.figure.includes(">4s<"));
});

test("scaffolds of lesson 8: 1000 variants each, answers consistent with the full question", () => {
  for (const tpl of [card.check, toTen]) {
    for (let seed = 0; seed < 1000; seed++) {
      const full = instantiate(tpl, seed, lib), steps = instantiate(scaffoldTemplate(tpl), seed, lib);
      assert.equal(steps.prompt, full.prompt, "same numbers for the same seed");
      assert.equal(steps.answerValues.at(-1), full.answerValue);
      const digits = [...steps.prompt.match(/Convert (\d+)/)[1]].map(Number);
      assert.equal(digits.reduce((t, d, i) => t + d * steps.answerValues[i], 0), full.answerValue, steps.answer);
      assert.equal(check(steps, steps.answers).correct, true);
      assert.ok(!/NaN|undefined|\{|\}/.test(steps.answer + full.misconceptions.map((m) => m.explain).join(" ")));
    }
  }
});

test("teach flow: the retry asks the scaffold; the example after a miss has the same shape and differs", () => {
  const lesson = { ...L8, teach: { cards: [card] }, questions: [toTen] };
  let flow = teach.startTeach(lesson, 42);
  flow = teach.nextPhase(flow);                              // card idea → its check
  const q1 = teach.itemQuestion(lesson, flow, lib);
  assert.equal(q1.type, "numeric");
  flow = teach.answerItem(flow, { correct: false }, 1000);   // first miss
  assert.equal(flow.phase, "retry");
  const like = teach.exampleLike(lesson, flow, lib, q1);
  assert.equal(like.type, "numeric");
  assert.notEqual(like.prompt, q1.prompt);
  assert.equal(like.prompt.match(/Convert (\d+)/)[1].length, 2, "two digits, like the card check");
  assert.ok(like.figure.includes("s<"), "the example shows the place values");
  flow = teach.nextPhase(flow);
  const q2 = teach.itemQuestion(lesson, flow, lib, [q1, like]);
  assert.equal(q2.type, "blanks");
  assert.ok(![q1.prompt, like.prompt].includes(q2.prompt), "a fresh question, not the one answered or the example");
});

test("templates without a scaffold or a computed answer are unchanged", () => {
  const mcq = L8.questions.find((t) => t.id === "m8-valid-digits");
  assert.equal(scaffoldTemplate(mcq), mcq);
  const lesson = { ...L8, teach: { cards: [] }, questions: [mcq] };
  let flow = teach.nextPhase(teach.startTeach(lesson, 7));  // worked example → the practice question
  flow = teach.answerItem(flow, { correct: false }, 10);
  assert.equal(teach.exampleLike(lesson, flow, lib, null), null);
});
