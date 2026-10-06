// Chemistry engine tests (written before content): the element table and chemical formulas.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as chem from "../src/engine/lib/chemistry.js";

test("element table: the first 20 elements in order, plus common metals; symbols unique and well formed", () => {
  const first20 = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"];
  assert.deepEqual(chem.ELEMENTS.slice(0, 20).map((e) => e.symbol), first20);
  assert.deepEqual(chem.ELEMENTS.slice(0, 20).map((e) => e.z), Array.from({ length: 20 }, (_, i) => i + 1));
  const symbols = chem.ELEMENTS.map((e) => e.symbol);
  assert.equal(new Set(symbols).size, symbols.length);
  for (const s of symbols) assert.match(s, /^[A-Z][a-z]?$/, s);
  for (const e of chem.ELEMENTS) {
    assert.equal(chem.symbolOf(e.name), e.symbol);
    assert.equal(chem.nameOf(e.symbol), e.name);
  }
  assert.equal(chem.nameOf("Al"), "aluminium");
  assert.equal(chem.nameOf("S"), "sulfur");
  for (const s of Object.keys(chem.LATIN)) assert.ok(chem.isSymbol(s), s);
  assert.deepEqual(["Na", "Mg", "Al", "K", "Ca", "Fe", "Cu", "Zn", "Hg"].map(chem.kindOf), Array(9).fill("metal"));
  assert.deepEqual(["H", "C", "N", "O", "S", "Cl", "I"].map(chem.kindOf), Array(7).fill("non-metal"));
});

test("formulas: atoms counted correctly, including brackets", () => {
  const known = {
    H2O: { H: 2, O: 1 }, CO2: { C: 1, O: 2 }, NaCl: { Na: 1, Cl: 1 }, CaCO3: { Ca: 1, C: 1, O: 3 }, H2SO4: { H: 2, S: 1, O: 4 },
    NH3: { N: 1, H: 3 }, CH4: { C: 1, H: 4 }, C6H12O6: { C: 6, H: 12, O: 6 }, "Ca(OH)2": { Ca: 1, O: 2, H: 2 }, Fe2O3: { Fe: 2, O: 3 },
    "Al2(SO4)3": { Al: 2, S: 3, O: 12 }, O2: { O: 2 }, MgO: { Mg: 1, O: 1 }, CuSO4: { Cu: 1, S: 1, O: 4 },
  };
  for (const [f, atoms] of Object.entries(known)) assert.deepEqual(chem.parseFormula(f), atoms, f);
  assert.equal(chem.atomCount("H2SO4", "O"), 4);
  assert.equal(chem.atomCount("H2O", "C"), 0);
  assert.equal(chem.totalAtoms("H2SO4"), 7);
  assert.equal(chem.totalAtoms("C6H12O6"), 24);
  assert.equal(chem.elementCount("CaCO3"), 3);
  assert.equal(chem.elementNames("H2SO4"), "hydrogen, sulfur and oxygen");
  assert.equal(chem.elementNames("NaCl"), "sodium and chlorine");
  assert.equal(chem.formula("C6H12O6"), "C₆H₁₂O₆");
  assert.equal(chem.atomList("CO2"), "C: 1, O: 2");
});

test("formulas: bad input is refused (CO is carbon monoxide, Co is cobalt, co is nothing)", () => {
  for (const bad of ["co", "h2o", "Xy2", "H2O)", "(OH", "", "2H2O", "H 2O"]) assert.throws(() => chem.parseFormula(bad), SyntaxError, bad);
  assert.deepEqual(chem.parseFormula("CO"), { C: 1, O: 1 });
  assert.throws(() => chem.parseFormula("Co"), SyntaxError, "cobalt is not in the Form 1 table");
});
