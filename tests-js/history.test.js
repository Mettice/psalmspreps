// History engine tests (written before content): BC/AD dates with no year 0, centuries, early humans, the timeline.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as h from "../src/engine/lib/history.js";

test("years are written 500 BC and AD 476; there is no year 0", () => {
  assert.equal(h.year(-500), "500 BC");
  assert.equal(h.year(476), "AD 476");
  assert.throws(() => h.year(0), RangeError);
});

test("years between dates: no year 0 across BC and AD", () => {
  assert.equal(h.yearsBetween(1884, 1961), 77);
  assert.equal(h.yearsBetween(-500, -200), 300);
  assert.equal(h.yearsBetween(-1, 1), 1);          // 1 BC to AD 1 is one year
  assert.equal(h.yearsBetween(-50, 50), 99);
  assert.equal(h.yearsBetween(50, -50), 99);
  assert.equal(h.yearsBetweenWithZero(-50, 50), 100);
});

test("centuries", () => {
  assert.equal(h.century(1884), "19th century AD");
  assert.equal(h.century(1900), "19th century AD");
  assert.equal(h.century(1901), "20th century AD");
  assert.equal(h.century(2026), "21st century AD");
  assert.equal(h.century(-500), "5th century BC");
  assert.equal(h.century(-501), "6th century BC");
  assert.equal(h.century(111), "2nd century AD");
  assert.equal(h.century(1150), "12th century AD");
  assert.equal(h.centuryFirstDigits(1884), "18th century AD");
  assert.equal(h.centuryStart(19), 1801);
  assert.equal(h.centuryEnd(19), 1900);
  assert.equal(h.earlier(-300, -100), -300);
});

test("early humans: in order, oldest first; written with 'about'", () => {
  const ago = [0, 1, 2, 3, 4].map(h.homininAgo);
  assert.deepEqual([...ago].sort((a, b) => b - a), ago);
  assert.equal(h.ago(2400000), "about 2.4 million years ago");
  assert.equal(h.ago(300000), "about 300 000 years ago");
  assert.equal(h.ago(7000000), "about 7 million years ago");
});

test("timeline: an SVG with no repeated attributes and no event years written on it", () => {
  const s = h.timeline(-400, 400, 100, [["A", -250], ["B", 150]]);
  assert.match(s, /^<svg [^>]*role="img"[\s\S]*<\/svg>$/);
  assert.doesNotMatch(s, /NaN|undefined|250|150/);
  for (const tag of s.match(/<[a-z]+ [^>]*>/g)) {
    const names = [...tag.matchAll(/ ([a-z-]+)="/g)].map((m) => m[1]);
    assert.equal(new Set(names).size, names.length, tag);
  }
});
