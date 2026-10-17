// Form 2 Maths library (src/engine/lib/maths2.js): checked on known answers, like the Form 1 libraries.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as m from "../src/engine/lib/maths2.js";
import { instantiate, inputModeFor } from "../src/engine/template.js";
import * as maths from "../src/engine/lib/maths.js";

test("integers and powers are written as in the textbook", () => {
  assert.equal(m.br(-3), "(−3)");
  assert.equal(m.br(4), "4");
  assert.equal(m.pw(2, 3), "2³");
  assert.equal(m.pw(-2, 3), "(−2)³");
  assert.equal(m.pw("a", 12), "a¹²");
  assert.equal(m.powExpand(-2, 3), "(−2) × (−2) × (−2)");
  assert.equal(m.signWord(-6), "negative");
});

test("primes, factorisation, HCF and LCM", () => {
  assert.deepEqual([2, 3, 4, 9, 11, 15, 97, 1].map(m.isPrime), [true, true, false, false, true, false, true, false]);
  assert.deepEqual(m.primeFactors(360), [2, 2, 2, 3, 3, 5]);
  assert.equal(m.factorProduct(60), "2 × 2 × 3 × 5");
  assert.equal(m.factorise(360), "2³ × 3² × 5");
  assert.deepEqual(m.ladder(60), ["60 ÷ 2 = 30", "30 ÷ 2 = 15", "15 ÷ 3 = 5", "5 ÷ 5 = 1"]);
  assert.equal(m.factorsOf(12), "1, 2, 3, 4, 6, 12");
  assert.equal(m.multiplesOf(4, 3), "4, 8, 12");
  assert.equal(m.hcf(24, 36), 12);
  assert.equal(m.lcm(24, 36), 72);
  assert.equal(m.lcm3(4, 6, 10), 60);
  assert.ok(m.isSquare(144) && !m.isSquare(50) && m.isCube(27) && !m.isCube(30));
});

test("sequences, triangle inequality, coordinates", () => {
  assert.equal(m.seqTerms(3, 4, 4), "3, 7, 11, 15");
  assert.equal(m.seqTerms(20, -3, 4), "20, 17, 14, 11");
  assert.equal(m.geoTerms(2, 3, 4), "2, 6, 18, 54");
  assert.ok(m.triangleOk(4, 5, 7) && !m.triangleOk(3, 4, 8) && !m.triangleOk(3, 4, 7));
  assert.equal(m.pt(3, -2), "(3, −2)");
});

test("algebraic expressions: signs, ones and zeros", () => {
  assert.equal(m.poly([3, "x"], [-1, "y"], [5, ""]), "3x − y + 5");
  assert.equal(m.poly([-1, "x"], [0, "y"], [-7, ""]), "−x − 7");
  assert.equal(m.poly([0, "x"]), "0");
  assert.equal(m.mono(1, "x²"), "x²");
  assert.equal(m.bracket(-2, [1, "x"], [-4, ""]), "−2(x − 4)");
});

test("inequalities: truth, signs turned round, whole-number solutions", () => {
  assert.ok(m.holds(3, "≤", 3) && !m.holds(3, "<", 3) && m.holds(-1, ">", -2));
  assert.equal(m.flipOp("≤"), "≥");
  assert.equal(m.solutionsIn(-3, 3, "≤", 1), "−3, −2, −1, 0, 1");
  assert.equal(m.solutionsIn(0, 3, ">", 5), "none");
  assert.match(m.ineqLine("≥", 2), /fill="currentColor"\/><\/svg>$/, "≥: filled circle");
  assert.match(m.ineqLine("<", 2), /style="fill: var\(--card, #fff\)"\/><\/svg>$/, "<: open circle");
});

test("drawings are SVG with no repeated attribute and reject points off the grid", () => {
  for (const svg of [m.coordPlane([["A", 3, -2]]), m.numberLine(-5, 5, [["P", -3]]), m.ineqLine(">", -1), m.bisectorFig(5, "?"), m.segmentFig(4, "?")]) {
    assert.match(svg, /^<svg [^>]*role="img"/);
    for (const tag of svg.match(/<[a-z]+ [^>]*>/g)) {
      const names = [...tag.matchAll(/ ([a-z-]+)=/g)].map((x) => x[1]);
      assert.equal(new Set(names).size, names.length, tag);
    }
  }
  assert.throws(() => m.coordPlane([["A", 6, 0]]));
  assert.throws(() => m.numberLine(0, 20, []));
});

test("a question whose answer can be negative always gets a keyboard with a minus sign", () => {
  const tpl = { id: "t", type: "numeric", level: 1, prompt: "{a} − {b}", vars: { a: { int: [1, 9] }, b: { int: [1, 9] } }, answer: "a - b", signed: true, solution: ["{answer}"] };
  const lib = { ...maths, ...m };
  for (let seed = 1; seed <= 30; seed++) assert.equal(inputModeFor(instantiate(tpl, seed, lib)), "text");
  assert.equal(inputModeFor(instantiate({ ...tpl, signed: undefined }, 3, lib)), "numeric", "unsigned whole numbers keep the number pad");
});
