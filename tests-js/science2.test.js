// Form 2 science library: the Term 2 chemistry equations, oxides, Rf values and states (2026-10-21).
import { test } from "node:test";
import assert from "node:assert/strict";
import * as s from "../src/engine/lib/science2.js";

test("every equation in the table balances, and each wrong form does not", () => {
  for (let i = 0; i < s.nEquations(); i++) {
    assert.ok(s.eqBalanced(i), s.eqStr(i));
    for (const e of s.eqElements(i)) assert.equal(s.eqAtoms(i, 0, e), s.eqAtoms(i, 1, e), `${s.eqStr(i)} ${e}`);
  }
  assert.equal(s.eqStr(6), "4Fe + 3O₂ → 2Fe₂O₃");
  assert.equal(s.eqSkeleton(6), "Fe + O₂ → Fe₂O₃");
  assert.equal(s.eqBlank(6, s.eqKeyTerm(6)), "___Fe + 3O₂ → 2Fe₂O₃");
  assert.equal(s.eqCoef(6, 0), 4);
  assert.equal(s.eqWrong(6, 0, 1), "5Fe + 3O₂ → 2Fe₂O₃");
  assert.equal(s.eqStr(19), "CaO + H₂O → Ca(OH)₂");
  assert.equal(s.eqAtoms(15, 1, "O"), 4);
  assert.equal(s.eqAtomsNoCoef(15, 1, "O"), 3);
  assert.equal(s.eqTermFormula(17, 2), "O2");
});

test("the equation groups used by the balancing lessons all need a coefficient other than one", () => {
  for (const i of [0, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 15, 17, 18]) assert.notEqual(s.eqStr(i), s.eqSkeleton(i), s.eqStr(i));
  for (const i of s.binaryEquations()) assert.ok(s.eqTerms(i) <= 3);
});

test("oxides, Rf values and states", () => {
  assert.equal(s.oxideType("Mg"), "basic");
  assert.equal(s.oxideType("S"), "acidic");
  assert.equal(s.rf(3, 6), 0.5);
  assert.equal(s.rf(1, 4), 0.25);
  assert.equal(s.stateAt(25, -114, 78), "liquid");
  assert.equal(s.stateAt(-150, -114, 78), "solid");
  assert.equal(s.stateAt(100, 0, 100), "gas");
});

test("body mass index, food energy and heat taken in by water", () => {
  assert.equal(s.bmi(60, 1.6), 23.4);
  assert.equal(s.bmiClass(18.4), "underweight");
  assert.equal(s.bmiClass(18.5), "normal weight");
  assert.equal(s.bmiClass(25), "overweight");
  assert.equal(s.bmiClass(30), "obese");
  assert.equal(s.foodEnergy(10, 37), 370);
  assert.equal(s.heatToWater(20, 15), 1260);
  assert.equal(s.energyPerGram(20, 15, 0.5), 2520);
});

test("Term 3 heating and electrolysis equations balance", () => {
  for (const i of [...s.heatEquations(), 28, 29, 30]) assert.ok(s.eqBalanced(i), s.eqStr(i));
  assert.equal(s.eqStr(25), "2Cu(NO₃)₂ → 2CuO + 4NO₂ + O₂");
  assert.equal(s.eqCoef(27, 0), 2);
  assert.equal(s.eqCoef(30, 0), 2);
});
