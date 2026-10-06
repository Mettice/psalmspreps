// Physics engine tests (written before content): units, conversions, weight, density, and the drawn instruments
// (each drawing must show exactly the reading the question's numbers say).
import { test } from "node:test";
import assert from "node:assert/strict";
import * as maths from "../src/engine/lib/maths.js";
import * as physics from "../src/engine/lib/physics.js";
import { instantiate, renderWorked } from "../src/engine/template.js";
import { makeRng } from "../src/engine/rng.js";

const lib = { ...maths, ...physics };

test("conversions: known answers in length, mass, capacity and time", () => {
  const known = [
    [2.5, "kg", "g", 2500], [750, "g", "kg", 0.75], [3, "g", "mg", 3000], [4500, "mg", "g", 4.5], [2, "t", "kg", 2000],
    [1.2, "km", "m", 1200], [35, "mm", "cm", 3.5], [1.75, "m", "cm", 175],
    [1.5, "L", "mL", 1500], [250, "mL", "L", 0.25], [1, "L", "cm³", 1000], [1, "m³", "L", 1000], [500, "cm³", "mL", 500], [2, "dm³", "L", 2],
    [2, "h", "min", 120], [90, "s", "min", 1.5], [1, "h", "s", 3600],
  ];
  for (const [v, a, b, r] of known) assert.equal(physics.convertUnit(v, a, b), r, `${v} ${a} → ${b}`);
  assert.equal(physics.factor("kg", "g"), 1000);
  assert.equal(physics.factor("cm", "mm"), 10);
  assert.throws(() => physics.convertUnit(1, "kg", "m"), RangeError);
  assert.throws(() => physics.convertUnit(1, "N", "kg"), RangeError);
});

test("conversions: round trips are exact (no floating-point noise) across 5000 random values", () => {
  const rng = makeRng(42);
  const units = { length: ["km", "m", "cm", "mm"], mass: ["t", "kg", "g", "mg"], capacity: ["L", "mL", "cL", "cm³", "dm³", "m³"], time: ["h", "min", "s"] };
  for (let i = 0; i < 5000; i++) {
    const q = rng.pick(Object.keys(units));
    const [a, b] = rng.sample(units[q], 2);
    const v = rng.int(1, 9999) / 100;
    const there = physics.convertUnit(v, a, b);
    if (q === "time") { assert.ok(Math.abs(physics.convertUnit(there, b, a) - v) < 1e-8); continue; }  // may repeat: known answers above
    assert.equal(physics.convertUnit(there, b, a), v, `${v} ${a} → ${b} → ${a}`);
    assert.ok(!/e/.test(String(there)) || Math.abs(there) < 1e-6 || Math.abs(there) > 1e15, `${there}`);
    // metric conversions are exact; seconds to minutes may genuinely repeat (17.84 s = 0.2973… min)
    if (q !== "time") assert.equal(String(there).replace(/\d+\.(\d*)/, "$1").length < 12, true, `${v} ${a} → ${b} gave ${there}`);
  }
});

test("temperature, weight, density (TR-P03, TR-P04)", () => {
  assert.equal(physics.toKelvin(0), 273);
  assert.equal(physics.toKelvin(100), 373);
  assert.equal(physics.toCelsius(310), 37);
  assert.equal(physics.weight(5), 50);
  assert.equal(physics.weight(0.25), 2.5);
  assert.equal(physics.weight(5, 9.8), 49);
  assert.equal(physics.density(54, 20), 2.7);
  assert.equal(physics.floatsInWater(0.8), true);
  assert.equal(physics.floatsInWater(2.7), false);
  assert.equal(physics.cuboid(5, 4, 3), 60);
});

// ---------------------------------------------------------------- drawings
const wellFormed = (s) => {
  assert.match(s, /^<svg [^>]*role="img"[^>]*>[\s\S]*<\/svg>$/);
  assert.doesNotMatch(s, /NaN|undefined|Infinity/);
  const open = (s.match(/<(rect|line|text|path|circle|svg)\b[^>]*[^/]>/g) || []).length;
  const close = (s.match(/<\/(rect|line|text|path|circle|svg)>/g) || []).length;
  assert.equal(open, close, "every open tag is closed");
};
const attr = (tag, name) => Number(new RegExp(`${name}="([-\\d.]+)"`).exec(tag)[1]);

test("ruler: the object starts and ends exactly where the numbers say; the label does not give the reading", () => {
  assert.throws(() => physics.ruler(2, 9), RangeError, "an object longer than the ruler is a content error");
  const rng = makeRng(7);
  for (let i = 0; i < 500; i++) {
    const startMm = rng.int(0, 25), lenMm = rng.int(15, 55);  // the ruler shows 0 to 8 cm (readable at 360px)
    const start = startMm / 10, end = (startMm + lenMm) / 10;
    const s = physics.ruler(start, end);
    wellFormed(s);
    const obj = s.match(/<rect x="[\d.]+" y="18"[^>]*>/)[0];
    assert.equal(Math.round((attr(obj, "x") - 15) / 2), startMm, "object starts at the right millimetre");
    assert.equal(Math.round(attr(obj, "width") / 2), lenMm, "object has the right length");
    assert.equal((s.match(/<line /g) || []).length, 81 + 2, "81 marks (0 to 8 cm in mm) and two guide lines");
    assert.doesNotMatch(s.match(/aria-label="[^"]*"/)[0], /\d/);
  }
});

test("measuring cylinder: the bottom of the meniscus sits on the reading", () => {
  for (const [level, max, step] of [[46, 100, 2], [73, 100, 1], [35, 50, 1], [85, 100, 5], [130, 250, 10]]) {
    const s = physics.cylinder(level, max, step, step >= 5 ? 50 : 10);
    wellFormed(s);
    const y = (v) => 236 - (220 * v) / max;
    const surface = s.match(/<path d="M[\d.]+ ([\d.]+) Q[\d.]+ ([\d.]+) [\d.]+ [\d.]+" stroke-width/);
    // The quadratic curve's lowest point is halfway between its ends and its control point.
    const lowest = (Number(surface[1]) + Number(surface[2])) / 2;
    assert.ok(Math.abs(lowest - y(level)) <= 0.6, `${level} mL: meniscus at ${lowest}, mark at ${y(level)}`);
    const marks = (s.match(/<line /g) || []).length;
    assert.equal(marks, Math.round(max / step));
  }
  const d = physics.displacement(40, 58);
  wellFormed(d);
  assert.match(d, /before \(mL\)/);
  assert.match(d, /after \(mL\)/);
});

test("thermometers: the red column ends exactly at the temperature", () => {
  const X = (c, from, span) => 34 + (284 * (c - from)) / span;
  for (const [t, from] of [[25, 0], [37, 20], [-5, -10], [48, 0], [100, 60]]) {
    const s = physics.thermometer(t, from);
    wellFormed(s);
    const col = s.match(/<rect x="26" y="[\d.]+" width="([\d.]+)" height="5"/);
    assert.ok(Math.abs(26 + Number(col[1]) - X(t, from, 50)) <= 0.06, `${t} °C`);
  }
  for (const t of [36.6, 37, 38.4, 39.9, 35.2]) {
    const s = physics.clinical(t);
    wellFormed(s);
    const col = s.match(/<rect x="26" y="[\d.]+" width="([\d.]+)" height="5"/);
    assert.ok(Math.abs(26 + Number(col[1]) - X(t, 35, 7)) <= 0.06, `${t} °C`);
    assert.equal((s.match(/<line /g) || []).length, 71, "a mark every 0.1 °C from 35 to 42");
    for (const d of [35, 36, 37, 38, 39, 40, 41, 42]) assert.match(s, new RegExp(`>${d}</text>`));
  }
});

test("figures travel with questions and worked examples", () => {
  const tpl = { id: "t-ruler", type: "numeric", level: 1, vars: { a: { int: [0, 20] }, l: { int: [20, 55] } },
    prompt: "How long is the pencil?", figure: "ruler(a / 10, (a + l) / 10)", answer: "l / 10", unit: "cm" };
  for (let seed = 1; seed <= 50; seed++) {
    const q = instantiate(tpl, seed, lib);
    wellFormed(q.figure);
  }
  const we = renderWorked({ vars: { v: 46 }, problem: "Read the cylinder.", steps: ["Read at the bottom of the curve."], answer: "{v} mL", figure: "cylinder(v)" }, lib);
  wellFormed(we.figure);
});

test("changes of state: names and heat flow for all six changes (TR-P07)", () => {
  const known = { "solid>liquid": ["melting", "taken in"], "liquid>solid": ["freezing", "given out"], "liquid>gas": ["evaporation", "taken in"],
    "gas>liquid": ["condensation", "given out"], "solid>gas": ["sublimation", "taken in"], "gas>solid": ["deposition", "given out"] };
  for (const [k, [name, heat]] of Object.entries(known)) {
    const [a, b] = k.split(">");
    assert.equal(physics.processName(a, b), name, k);
    assert.equal(physics.heatFlow(a, b), heat, k);
  }
  assert.throws(() => physics.processName("solid", "solid"), RangeError);
});

test("label dates: a product is still good only before its date", () => {
  assert.equal(physics.stillGood(7, 10, 2026, 8, 10, 2026), true);
  assert.equal(physics.stillGood(7, 10, 2026, 7, 10, 2026), false);
  assert.equal(physics.stillGood(7, 10, 2026, 30, 9, 2026), false);
  assert.equal(physics.stillGood(31, 12, 2026, 1, 1, 2027), true);
  assert.equal(physics.dateNum(7, 10, 2026), 20261007);
});
