// Home Economics engine tests (written before content): lettered drawings and the kitchen work triangle.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as h from "../src/engine/lib/homeeconomics.js";

const SVG = /^<svg [^>]*role="img"[\s\S]*<\/svg>$/;

test("arrangements: every k gives each letter once; all n! arrangements differ", () => {
  for (const n of [3, 5, 6]) {
    const seen = new Set();
    const total = [1, 1, 2, 6, 24, 120, 720][n];
    for (let k = 0; k < total; k++) {
      const a = h.arrangement(k, n);
      assert.deepEqual([...a].sort(), "ABCDEF".slice(0, n).split(""));
      seen.add(a.join(""));
    }
    assert.equal(seen.size, total);
  }
});

test("fireplaces: the letter under each type and the type at each letter agree", () => {
  for (let k = 0; k < 6; k++) for (let i = 0; i < 3; i++) assert.equal(h.fireAt(k, h.fireLetter(k, i)), h.fireType(i));
});

test("work triangle: total, the 1.2–2.7 m / 4–7.9 m rule, and the reason given", () => {
  assert.equal(h.triangleTotal(1.8, 2.1, 2.4), 6.3);
  assert.equal(h.goodTriangle(1.8, 2.1, 2.4), true);
  assert.equal(h.triangleVerdict(1.8, 2.1, 2.4), "it is well planned");
  assert.equal(h.goodTriangle(1.2, 1.3, 1.4), false);  // sides fine, total 3.9 m too short
  assert.match(h.triangleVerdict(1.2, 1.3, 1.4), /total is too short/);
  assert.match(h.triangleVerdict(3.2, 2, 2), /too long/);
  assert.match(h.triangleVerdict(0.9, 2, 2), /too short/);
  assert.equal(h.isTriangle(1, 1, 3), false);
  assert.throws(() => h.workTriangle(1, 1, 3), RangeError);
});

test("drawings are SVG images with no repeated attributes", () => {
  const all = [h.traditionalKitchen(123), h.fireplaces(4), h.kitchenUnits(500), h.workTriangle(1.8, 2.1, 2.4),
    ...[0, 1, 2, 3, 4].map(h.kitchenPlan)];
  for (const s of all) {
    assert.match(s, SVG);
    assert.doesNotMatch(s, /NaN|undefined|Infinity/);
    for (const tag of s.match(/<[a-z]+ [^>]*>/g)) {
      const names = [...tag.matchAll(/ ([a-z-]+)="/g)].map((m) => m[1]);
      assert.equal(new Set(names).size, names.length, tag);
    }
  }
  assert.equal(h.TRAD_PARTS.length, 6);
  assert.equal(h.UNIT_PARTS.length, 6);
  assert.equal(h.SHAPES.length, 5);
});
