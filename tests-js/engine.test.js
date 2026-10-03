// Engine and library tests: known answers plus independent round trips.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as lib from "../src/engine/lib/maths.js";
import { evaluate, render } from "../src/engine/expr.js";
import { parseNumber, normalize, instantiate, check, normaliseInput, inputModeFor } from "../src/engine/template.js";
import { makeRng } from "../src/engine/rng.js";

test("expression language: precedence, strings, ternary, power", () => {
  const s = { a: 3, b: 4, name: "Enow", list: [5, 6] };
  assert.equal(evaluate("a + b * 2", s, lib), 11);
  assert.equal(evaluate("(a + b) * 2", s, lib), 14);
  assert.equal(evaluate("2 ^ 3 ^ 2", s, lib), 512);
  assert.equal(evaluate("a + 2 * b ^ 2", s, lib), 35);
  assert.equal(evaluate("-a + b", s, lib), 1);
  assert.equal(evaluate("17 % 5", s, lib), 2);
  assert.equal(evaluate("a > 2 && b < 4 || name == 'Enow'", s, lib), true);
  assert.equal(evaluate("a == 3 ? 'yes' : 'no'", s, lib), "yes");
  assert.equal(evaluate("list[1] + len(list)", s, lib), 8);
  assert.equal(evaluate("'x' + a", s, lib), "x3");
  assert.equal(evaluate("0.1 + 0.2 == 0.3", s, lib), true);
  assert.equal(render("{a}{{b}} = {a * b}", s, lib), "3{b} = 12");
});

test("expression language cannot reach outside its library", () => {
  for (const bad of ["process", "constructor", "eval('1')", "a.constructor", "toBase.call(1)", "globalThis"]) {
    assert.throws(() => evaluate(bad, { a: 1 }, lib), bad);
  }
});

test("roman numerals", () => {
  const known = { 1: "I", 4: "IV", 9: "IX", 14: "XIV", 40: "XL", 90: "XC", 400: "CD", 900: "CM", 1948: "MCMXLVIII", 1994: "MCMXCIV", 2026: "MMXXVI", 3999: "MMMCMXCIX" };
  for (const [n, r] of Object.entries(known)) assert.equal(lib.roman(Number(n)), r);
  for (let n = 1; n <= 3999; n++) assert.equal(lib.fromRoman(lib.roman(n)), n);
  for (const bad of ["IIII", "VV", "IC", "XM", "ABC", ""]) assert.ok(Number.isNaN(lib.fromRoman(bad)), bad);
  assert.equal(lib.romanAdditive(94), "LXXXXIIII");
  assert.equal(lib.romanAddAll("XL"), 60);
  assert.equal(lib.egyptianList(3205), "3 lotus flowers, 2 coils of rope and 5 strokes");
});

test("numbers in words (British) and the independent parser", () => {
  const known = {
    0: "zero", 7: "seven", 15: "fifteen", 45: "forty-five", 100: "one hundred", 105: "one hundred and five",
    110: "one hundred and ten", 999: "nine hundred and ninety-nine", 1000: "one thousand", 3005: "three thousand and five",
    40307: "forty thousand three hundred and seven", 1000100: "one million one hundred",
    2405012: "two million four hundred and five thousand and twelve",
  };
  for (const [n, w] of Object.entries(known)) assert.equal(lib.words(Number(n)), w);
  for (let n = 0; n <= 120000; n++) assert.equal(lib.fromWords(lib.words(n)), n);
  const rng = makeRng(7);
  for (let i = 0; i < 20000; i++) { const n = rng.int(0, 999999999); assert.equal(lib.fromWords(lib.words(n)), n); }
});

test("number bases", () => {
  assert.equal(lib.toBase(13, 2), "1101");
  assert.equal(lib.toBase(45, 3), "1200");
  assert.equal(lib.toBase(0, 5), "0");
  assert.equal(lib.fromBase("201", 4), 33);
  assert.ok(Number.isNaN(lib.fromBase("25", 5)));
  for (let b = 2; b <= 10; b++) for (let n = 0; n <= 5000; n++) {
    const s = lib.toBase(n, b);
    assert.equal(lib.fromBase(s, b), n);
    assert.ok([...s].every((c) => Number(c) < b));
  }
  assert.equal(lib.decAdd("34", "23"), "57");  // the wrong-on-purpose helper really is base-ten
});

test("column subtraction working: plain steps, no negative intermediates, correct every time (TR-C31)", () => {
  const rng = makeRng(31);
  let acrossZero = 0;
  for (let k = 0; k < 20000; k++) {
    const b = rng.int(2, 9), a = rng.int(1, b ** 5), c = rng.int(0, a);
    const xs = lib.toBase(a, b), ys = lib.toBase(c, b);
    const lines = lib.columnSub(xs, ys, b).split("\n");
    for (const line of lines) {
      // A negative number is a minus sign attached to a digit ("−1"); the operator " − " has a space after it.
      assert.doesNotMatch(line, /(^|[\s=:(])[−-]\d/, `negative number in "${line}" (${xs} − ${ys}, base ${b})`);
      for (const [, x, y, z] of line.matchAll(/(\d+) − (\d+) = (\d+)/g)) assert.equal(Number(x) - Number(y), Number(z), line);
      for (const [, x, y, z] of line.matchAll(/(\d+) \+ (\d+) = (\d+)/g)) assert.equal(Number(x) + Number(y), Number(z), line);
      const then = line.match(/Then (\d+) − (\d+) = (\d+)\.$/);
      if (then) assert.ok(Number(then[3]) < b, `column result must be a base-${b} digit: ${line}`);
      if (line.includes("This 0 already lent 1")) {
        acrossZero++;
        assert.match(line, new RegExp(`This 0 already lent 1 to the right and has nothing left, so it borrows from the next column\\. In base ${b}, borrowing gives ${b}\\. ${b} − 1 \\(what it lent\\) = ${b - 1}\\. Then ${b - 1} − \\d+ = \\d+\\.$`));
      }
    }
    assert.equal(lines.at(-1), `Answer: ${lib.toBase(a - c, b)}${lib.sub(b)}`);
  }
  assert.ok(acrossZero > 100, "borrowing across a zero must be exercised");
  assert.equal(lib.columnSub("1002", "3", 4).split("\n")[1],
    "Column 2 from the right: This 0 already lent 1 to the right and has nothing left, so it borrows from the next column. In base 4, borrowing gives 4. 4 − 1 (what it lent) = 3. Then 3 − 0 = 3.");
});

test("place value, ordinals, units, lines, formatting", () => {
  assert.equal(lib.placeValue(45372, 3), 5000);
  assert.equal(lib.digitAt(45372, 0), 2);
  assert.equal(lib.posOf(762418, 6), 4);
  assert.equal(lib.stripZeros(40307), 437);
  for (const [n, o] of [[1, "1st"], [2, "2nd"], [3, "3rd"], [4, "4th"], [11, "11th"], [12, "12th"], [13, "13th"], [21, "21st"], [22, "22nd"], [101, "101st"], [111, "111th"], [112, "112th"]]) assert.equal(lib.ordinal(n), o);
  assert.equal(lib.convert(3.5, "km", "m"), 3500);
  assert.equal(lib.convert(45, "cm", "m"), 0.45);
  assert.equal(lib.convert(7, "mm", "km"), 0.000007);
  for (const u of ["km", "hm", "dam", "m", "dm", "cm", "mm"]) for (const v of ["km", "hm", "dam", "m", "dm", "cm", "mm"]) {
    for (const x of [1, 7, 45, 950, 2.4]) assert.equal(Number(lib.convert(lib.convert(x, u, v), v, u).toFixed(9)), x);
  }
  assert.equal(lib.lineRule("//", "//"), "//");
  assert.equal(lib.lineRule("⊥", "⊥"), "//");
  assert.equal(lib.lineRule("//", "⊥"), "⊥");
  assert.equal(lib.lineRule("⊥", "//"), "⊥");
  assert.equal(lib.fmt(1234567.5), "1 234 567.5");
  assert.equal(lib.fmt(999), "999");
  assert.equal(lib.fmt(-3), "−3");
  assert.equal(lib.fmt(0.1 + 0.2), "0.3");
});

test("answer parsing accepts the ways pupils type numbers", () => {
  assert.equal(parseNumber("1 500"), 1500);
  assert.equal(parseNumber("1 500"), 1500);
  assert.equal(parseNumber("1,500"), 1500);
  assert.equal(parseNumber("2,5"), 2.5);
  assert.equal(parseNumber("0.45"), 0.45);
  assert.equal(parseNumber("−3"), -3);
  assert.ok(Number.isNaN(parseNumber("12a")));
  assert.ok(Number.isNaN(parseNumber("")));
  assert.equal(normalize("0101₂", "base"), "101");
  assert.equal(normalize(" mcm ", "roman"), "MCM");
});

test("typed answers: spaces, thin spaces and commas are stripped for whole numbers", () => {
  const tpl = { id: "t-big", type: "numeric", level: 1, vars: { n: 9038766 }, prompt: "Write {n}.", answer: "n" };
  const q = instantiate(tpl, 1, lib);
  assert.equal(inputModeFor(q), "numeric");
  for (const typed of ["9038766", "9 038 766", "9,038,766", "9 038 766", "9 038 766", "9 038 766", " 9 038 766 "]) {
    assert.equal(normaliseInput(typed, q), "9038766", typed);
    assert.deepEqual(check(q, normaliseInput(typed, q)), { correct: true }, typed);
  }
  assert.equal(check(q, normaliseInput("9 038 767", q)).correct, false);
  // decimals keep their decimal comma; base numerals get the number pad too
  const dec = instantiate({ id: "t-dec", type: "numeric", level: 1, vars: {}, prompt: "x", answer: "2.5" }, 1, lib);
  assert.equal(inputModeFor(dec), "decimal");
  assert.equal(check(dec, normaliseInput("2,5", dec)).correct, true);
  const base = instantiate({ id: "t-base", type: "numeric", level: 1, answer_kind: "base", vars: {}, prompt: "x", answer: "'1101'" }, 1, lib);
  assert.equal(inputModeFor(base), "numeric");
});

test("check() recognises a misconception and explains it", () => {
  const tpl = {
    id: "t", type: "numeric", level: 1, vars: { n: 45, b: 3 }, prompt: "Convert {n} to base {b}.", answer: "toBase(n, b)", answer_kind: "base",
    misconceptions: [{ id: "reversed", wrong: "reverse(toBase(n, b))", explain: "Read from the bottom." }],
  };
  const q = instantiate(tpl, 1, lib);
  assert.deepEqual(check(q, "1200"), { correct: true });
  assert.deepEqual(check(q, " 01200 "), { correct: true });
  assert.deepEqual(check(q, "0021"), { correct: false, misconception: { id: "reversed", explain: "Read from the bottom." } });
  assert.deepEqual(check(q, "999"), { correct: false, misconception: null });
});
