// Biology engine tests (written before content): magnification and the lettered drawings.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as b from "../src/engine/lib/biology.js";

test("magnification = eyepiece × objective; real size = image size ÷ magnification", () => {
  assert.equal(b.magnification(10, 40), 400);
  assert.equal(b.magnification(10, 4), 40);
  assert.equal(b.realSize(20, 400), 0.05);
  assert.equal(b.imageSize(0.05, 400), 20);
});

test("cell discoveries in date order", () => {
  const years = [0, 1, 2, 3].map(b.discoveryYear);
  assert.deepEqual([...years].sort((x, y) => x - y), years);
  assert.equal(b.discoverer(0), "Robert Hooke");
});

test("arrangements: each letter once, all n! different (n = 3, 4, 6, 8)", () => {
  for (const n of [3, 4, 6]) {
    const total = [1, 1, 2, 6, 24, 120, 720][n], seen = new Set();
    for (let k = 0; k < total; k++) {
      const a = b.bioArrangement(k, n);
      assert.deepEqual([...a].sort(), "ABCDEFGH".slice(0, n).split(""));
      seen.add(a.join(""));
    }
    assert.equal(seen.size, total);
  }
  assert.deepEqual([...b.bioArrangement(40319, 8)].sort().join(""), "ABCDEFGH");
});

test("drawings are SVG images with no repeated attributes", () => {
  for (const s of [b.microscope(12345), b.plantCell(500), b.animalCell(4), b.soilProfile(17)]) {
    assert.match(s, /^<svg [^>]*role="img"[\s\S]*<\/svg>$/);
    assert.doesNotMatch(s, /NaN|undefined|Infinity/);
    for (const tag of s.match(/<[a-z]+ [^>]*>/g)) {
      const names = [...tag.matchAll(/ ([a-z-]+)="/g)].map((m) => m[1]);
      assert.equal(new Set(names).size, names.length, tag);
    }
  }
});
