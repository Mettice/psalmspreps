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

test("Term 2 library: fractions, rounding, significant figures, intervals, money, polygons, angles, circles", () => {
  assert.equal(m.frac(6, 8), "3/4"); assert.equal(m.frac(-3, 6), "−1/2"); assert.equal(m.frac(8, 4), "2");
  assert.equal(m.mixed(7, 4), "1 3/4");
  assert.equal(m.fAdd(1, 2, 1, 3), "5/6"); assert.equal(m.fSub(3, 4, 1, 6), "7/12"); assert.equal(m.fMul(2, 3, 9, 10), "3/5"); assert.equal(m.fDiv(3, 4, 9, 8), "2/3");
  assert.equal(m.fAddWrong(1, 2, 1, 3), "2/5");
  assert.equal(m.sigFig(0.030549, 3), 0.0305); assert.equal(m.sigFig(45678, 2), 46000); assert.equal(m.sigFigStr(0.05, 3), "0.0500"); assert.equal(m.sigFigStr(2.996, 3), "3.00");
  assert.equal(m.countSig("0.0305"), 3); assert.equal(m.countSig("4500"), 2); assert.equal(m.countSig("4.50"), 3);
  assert.equal(m.roundTo(347, 10), 350); assert.equal(m.roundTo(3.456, 0.01), 3.46); assert.equal(m.dec(0.1 + 0.2), 0.3);
  assert.equal(m.interval(-2, 5, true, false), "[−2, 5)"); assert.equal(m.interval(3, null, true, false), "[3, +∞)"); assert.equal(m.intervalIneq(-2, 5, true, false), "−2 ≤ x < 5");
  assert.deepEqual(m.intsIn(-2, 5, true, false), [-2, -1, 0, 1, 2, 3, 4]);
  assert.equal(m.simpleInterest(50000, 5, 3), 7500); assert.equal(m.compound(100000, 10, 2), 121000); assert.equal(m.pctChange(2000, 2500), 25);
  assert.equal(m.angleSum(5), 540); assert.equal(m.interiorRegular(6), 120); assert.equal(m.exteriorRegular(8), 45);
  assert.equal(m.anglePair(0, 3), "vertically opposite"); assert.equal(m.anglePair(1, 5), "corresponding"); assert.equal(m.anglePair(2, 5), "alternate"); assert.equal(m.anglePair(2, 4), "co-interior");
  assert.equal(m.angleAt(70, 5), 110); assert.ok(m.pairEqual(2, 5) && !m.pairEqual(2, 4));
  for (const [a, b, c] of m.TRIPLES) assert.ok(m.isRightTriangle(a, b, c));
  assert.equal(m.circlesPos(3, 2, 6), "separate (outside each other)"); assert.equal(m.circlesPos(3, 2, 5), "touching externally");
  assert.equal(m.circlesPos(3, 2, 4), "intersecting in two points"); assert.equal(m.circlesPos(3, 2, 1), "touching internally"); assert.equal(m.circlesPos(3, 2, 0.5), "one inside the other");
  for (const f of [m.parallelFig(70, 0, 5), m.crossFig(40, 1), m.triangleFig(50, 60, "x"), m.rightTriFig(3, 4, "?"), m.regularFig(6), m.trapeziumFig(9, 5, 4), m.parallelogramFig(8, 5)])
    assert.match(f, /^<svg class="fig"[^>]+role="img"/);
});

test("fraction answers: 3/4, 1 3/4, −1/2 accepted; the right value not simplified gets a hint", async () => {
  const { instantiate, check, inputModeFor } = await import("../src/engine/template.js");
  const lib = { ...maths, ...m };
  const q = instantiate({ id: "f", type: "numeric", level: 1, answer_kind: "fraction", prompt: "p", answer: "fAdd(a, b, c, d)", vars: { a: 1, b: 2, c: 1, d: 4 }, solution: ["s"] }, 1, lib);
  assert.equal(q.answer, "3/4"); assert.equal(inputModeFor(q), "text");
  for (const r of ["3/4", " 3 / 4 "]) assert.equal(check(q, r).correct, true, r);
  assert.equal(check(q, "6/8").misconception.id, "not-simplified");
  assert.equal(check(q, "2/3").correct, false);
  const q2 = instantiate({ id: "g", type: "numeric", level: 1, answer_kind: "fraction", prompt: "p", answer: "fAdd(a, b, c, d)", vars: { a: 3, b: 4, c: 1, d: 2 }, solution: ["s"] }, 1, lib);
  assert.equal(q2.answer, "5/4");
  for (const r of ["5/4", "1 1/4"]) assert.equal(check(q2, r).correct, true, r);
  assert.equal(check(q2, "1 2/8").misconception.id, "not-simplified");
  const q3 = instantiate({ id: "h", type: "numeric", level: 1, answer_kind: "fraction", prompt: "p", answer: "fSub(a, b, c, d)", vars: { a: 1, b: 4, c: 3, d: 4 }, solution: ["s"] }, 1, lib);
  assert.equal(q3.answer, "−1/2");
  for (const r of ["−1/2", "-1/2", "1/-2"]) assert.equal(check(q3, r).correct, true, r);
});


test("Term 3: prisms, pyramids, spheres and averages", () => {
  assert.deepEqual([m.prismFaces(5), m.prismEdges(5), m.prismVertices(5)], [7, 15, 10]);
  assert.deepEqual([m.pyramidFaces(4), m.pyramidEdges(4), m.pyramidVertices(4)], [5, 8, 5]);
  for (const n of [3, 4, 5, 6]) assert.equal(m.prismFaces(n) + m.prismVertices(n) - m.prismEdges(n), 2);
  for (const n of [3, 4, 5, 6]) assert.equal(m.pyramidFaces(n) + m.pyramidVertices(n) - m.pyramidEdges(n), 2);
  assert.equal(m.baseName(4, "pyramid"), "square");
  assert.equal(m.baseName(4, "prism"), "rectangular");
  assert.equal(m.prismTotalArea(12, 10, 6), 132);
  assert.equal(m.sqPyramidArea(6, 5), 96);
  assert.equal(m.sphereArea(5), 314);
  assert.equal(m.sphereVolume(3), 113.04);
  assert.equal(m.sphereVolume(6), 904.32);
  assert.equal(m.meanOf([3, 7, 2, 7, 6]), 5);
  assert.equal(m.medianOf([3, 7, 2, 7, 6]), 6);
  assert.equal(m.medianOf([1, 8, 4, 6]), 5);
  assert.equal(m.modeOf([3, 7, 2, 7, 6]), 7);
  assert.equal(m.modeOf([2, 2, 3, 3]), "none");
  assert.equal(m.freqMean([0, 1, 2, 3], [4, 6, 7, 3]), 1.45);
  assert.equal(m.freqMode([0, 1, 2, 3], [4, 6, 7, 3]), 2);
  assert.equal(m.pieAngle(15, 60), 90);
  for (const n of [3, 4, 5, 6]) assert.match(m.prismFig(n) + m.pyramidFig(n), /^<svg/);
  assert.match(m.barChartFig(["A", "B"], [3, 7]) + m.pieFig(["A", "B"], [1, 3]) + m.sphereFig(5), /role="img"/);
});

test("Form 3: trigonometry in degrees, logarithms, 2 × 2 matrices and their drawings", () => {
  const near = (a, b) => assert.ok(Math.abs(a - b) < 1e-9, `${a} vs ${b}`);
  near(m.sinD(30), 0.5); near(m.cosD(60), 0.5); near(m.tanD(45), 1); near(m.asinD(0.5), 30); near(m.acosD(0.5), 60); near(m.atanD(1), 45);
  assert.equal(m.logb(2, 8), 3); assert.equal(m.logb(10, 1000), 3); assert.equal(m.logb(3, 1 / 9), -2); near(m.log10(2), 0.3010299956639812);
  const A = [[2, 3], [1, 4]], B = [[0, -1], [5, 2]];
  assert.equal(m.det2(A), 5);
  assert.deepEqual(m.matAdd(A, B), [[2, 2], [6, 6]]); assert.deepEqual(m.matSub(A, B), [[2, 4], [-4, 2]]);
  assert.deepEqual(m.matScale(3, A), [[6, 9], [3, 12]]); assert.deepEqual(m.matMul(A, B), [[15, 4], [20, 7]]);
  assert.deepEqual(m.matT(A), [[2, 1], [3, 4]]); assert.deepEqual(m.adj2(A), [[4, -3], [-1, 2]]);
  assert.deepEqual(m.matMul(A, m.adj2(A)), [[5, 0], [0, 5]], "A × adj A = det A × I");
  assert.equal(m.matStr([[2, -3], [1, 4]]), "(2  −3 ; 1  4)");
  for (const f of [m.matFig([["A", A], ["B", B]]), m.trigFig(12, 5, "x", 30), m.trigFig("adj", "opp", "hyp"), m.thalesFig(4, 6, "x", 9, "", 15)]) {
    assert.match(f, /^<svg [^>]*role="img"/); assert.doesNotMatch(f, /NaN|undefined/);
  }
});
