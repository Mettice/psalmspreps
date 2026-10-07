// Computer Science engine tests (written before content): patterns, tracing, history, drawings.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as c from "../src/engine/lib/computerscience.js";

test("number patterns", () => {
  assert.equal(c.firstTerms(3, 4, 4), "3, 7, 11, 15");
  assert.equal(c.nthTerm(3, 4, 5), 19);
  assert.equal(c.firstDoubles(3, 4), "3, 6, 12, 24");
  assert.equal(c.nthDouble(3, 5), 48);
});

test("repeating shapes: the n-th shape follows the pattern", () => {
  assert.equal(c.shapeAt("012", 1), "circle");
  assert.equal(c.shapeAt("012", 4), "circle");
  assert.equal(c.shapeAt("012", 6), "triangle");
  assert.equal(c.shapeAt("0011", 7), "square");
  assert.equal(c.patternLength("0011"), 4);
});

test("tracing algorithms", () => {
  assert.equal(c.traceAdd(5, 3, 4), 17);
  assert.equal(c.traceDouble(3, 3), 24);
  assert.equal(c.traceIf(12, 10, "big", "small"), "big");
  assert.equal(c.traceIf(10, 10, "big", "small"), "small");
});

test("history in date order; five generations", () => {
  const years = [0, 1, 2, 3, 4, 5, 6].map(c.historyYear);
  assert.deepEqual([...years].sort((a, b) => a - b), years);
  assert.equal(c.generationTech(2), "transistors");
});

test("drawings are SVG images with no repeated attributes", () => {
  for (const s of [c.shapeSequence("0123", 6), c.shapeSequence("01", 5), ...[0, 1, 2].map(c.labLayout)]) {
    assert.match(s, /^<svg [^>]*role="img"[\s\S]*<\/svg>$/);
    assert.doesNotMatch(s, /NaN|undefined|Infinity/);
    for (const tag of s.match(/<[a-z]+ [^>]*>/g)) {
      const names = [...tag.matchAll(/ ([a-z-]+)="/g)].map((m) => m[1]);
      assert.equal(new Set(names).size, names.length, tag);
    }
  }
});

test("subject libraries after English never reuse a function name (a later library would silently replace it)", async () => {
  const seen = {};
  for (const n of ["maths", "english", "physics", "chemistry", "geography", "homeeconomics", "history", "biology", "computerscience"]) {
    const m = await import(`../src/engine/lib/${n}.js`);
    for (const k of Object.keys(m)) (seen[k] = seen[k] || []).push(n);
  }
  const known = new Set(["plural", "sum"]);  // maths and english, since English E1 (English's versions are the ones English uses)
  const clashes = Object.entries(seen).filter(([k, v]) => v.length > 1 && !known.has(k));
  assert.deepEqual(clashes, []);
});
