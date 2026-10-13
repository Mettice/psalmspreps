// French engine tests (written before content): articles, possessives, conjugation, numbers, alphabetical order.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as f from "../src/engine/lib/french.js";

const idx = (w) => [...Array(f.frNounCount()).keys()].find((i) => f.frNoun(i) === w);

test("articles, with elision before a vowel or silent h, not before h aspiré", () => {
  assert.equal(f.frDef(idx("livre")), "le livre");
  assert.equal(f.frDef(idx("table")), "la table");
  assert.equal(f.frDef(idx("école")), "l’école");
  assert.equal(f.frDef(idx("homme")), "l’homme");
  assert.equal(f.frDef(idx("haricot")), "le haricot");
  assert.equal(f.frDef(idx("tableau"), true), "les tableaux");
  assert.equal(f.frIndef(idx("orange")), "une orange");
  assert.equal(f.frIndef(idx("oiseau"), true), "des oiseaux");
});

test("possessives: mon before a feminine noun starting with a vowel", () => {
  assert.equal(f.frPoss(0, idx("livre")), "mon livre");
  assert.equal(f.frPoss(0, idx("table")), "ma table");
  assert.equal(f.frPoss(0, idx("école")), "mon école");
  assert.equal(f.frPoss(2, idx("amie")), "son amie");
  assert.equal(f.frPoss(1, idx("chaise"), true), "tes chaises");
  assert.equal(f.frPoss(3, idx("maison")), "notre maison");
  assert.equal(f.frPoss(5, idx("enfant"), true), "leurs enfants");
});

test("conjugation in the present: avoir, s'appeler, -er verbs; elision with je", () => {
  assert.deepEqual([0, 1, 2, 4, 5, 6].map((p) => f.frConj("avoir", p)), ["j’ai", "tu as", "il a", "nous avons", "vous avez", "ils ont"]);
  assert.deepEqual([0, 1, 3, 4, 5, 7].map((p) => f.frConj("s’appeler", p)),
    ["je m’appelle", "tu t’appelles", "elle s’appelle", "nous nous appelons", "vous vous appelez", "elles s’appellent"]);
  assert.deepEqual([0, 1, 2, 4, 5, 6].map((p) => f.frConj("travailler", p)),
    ["je travaille", "tu travailles", "il travaille", "nous travaillons", "vous travaillez", "ils travaillent"]);
  assert.equal(f.frConj("laver", 7), "elles lavent");
});

test("numbers in words (traditional spelling) and the 1990 spelling", () => {
  const want = { 1: "un", 16: "seize", 17: "dix-sept", 20: "vingt", 21: "vingt et un", 22: "vingt-deux", 31: "trente et un", 44: "quarante-quatre",
    50: "cinquante", 61: "soixante et un", 70: "soixante-dix", 71: "soixante et onze", 77: "soixante-dix-sept", 80: "quatre-vingts",
    81: "quatre-vingt-un", 90: "quatre-vingt-dix", 91: "quatre-vingt-onze", 99: "quatre-vingt-dix-neuf", 100: "cent" };
  for (const [n, w] of Object.entries(want)) assert.equal(f.frNumber(Number(n)), w, n);
  assert.equal(f.frNumber1990(21), "vingt-et-un");
  assert.equal(f.frNumber1990(44), "quarante-quatre");
});

test("alphabet: vowels, letters, alphabetical order ignoring accents", () => {
  assert.ok(f.frIsVowel("y") && f.frIsVowel("E") && !f.frIsVowel("b"));
  assert.equal(f.frLetter(0), "a");
  const list = ["maison", "école", "arbre", "livre"];
  assert.deepEqual(list.map((w) => f.frAlphaRank(w, list)), [3, 1, 0, 2]);
});

test("typical mistakes used as wrong options", () => {
  assert.equal(f.frNumberNoEt(31), "trente-un");
  assert.equal(f.frNumberSpaces(17), "dix sept");
  assert.equal(f.frEnding(4), "ons");
  assert.equal(f.frPossWrongVowel(0, idx("école")), "ma école");
  assert.ok(f.frStartsH(idx("hibou")) && !f.frStartsH(idx("livre")));
});
