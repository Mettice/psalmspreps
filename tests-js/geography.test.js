// Geography engine tests (written before content): time from longitude, map scale, grid references, drawings.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as g from "../src/engine/lib/geography.js";

const SVG = /^<svg [^>]*role="img"[\s\S]*<\/svg>$/;

test("latitude and longitude are written with N/S/E/W, latitude first", () => {
  assert.equal(g.lat(4), "4°N");
  assert.equal(g.lat(-12), "12°S");
  assert.equal(g.lat(0), "0°");
  assert.equal(g.lon(15), "15°E");
  assert.equal(g.lon(-30), "30°W");
  assert.equal(g.lon(180), "180°");
  assert.equal(g.latlon(4, 12), "4°N, 12°E");
  assert.equal(g.lonDiff(15, -30), 45);
  assert.equal(g.lonDiff(45, 15), 30);
  assert.equal(g.halfLat(23.5), "23½°N");
  assert.equal(g.halfLat(-66.5), "66½°S");
});

test("time: 15° = 1 hour, 1° = 4 minutes, east is ahead", () => {
  assert.equal(g.degreesPerHour(), 15);
  assert.equal(g.minutesPerDegree(), 4);
  assert.equal(g.timeForDegrees(45), 180);
  assert.equal(g.localTime(12 * 60, 0, 15), 13 * 60);   // noon at Greenwich → 1 p.m. at 15°E
  assert.equal(g.localTime(12 * 60, 0, -30), 10 * 60);  // → 10 a.m. at 30°W
  assert.equal(g.localTime(9 * 60, 15, 45), 11 * 60);
  assert.equal(g.clock(0), "12:00 midnight");
  assert.equal(g.clock(720), "12:00 noon");
  assert.equal(g.clock(860), "2:20 p.m.");
  assert.equal(g.clock(30), "12:30 a.m.");
  assert.equal(g.clock(750), "12:30 p.m.");
  assert.equal(g.clock(9 * 60 + 5), "9:05 a.m.");
  assert.equal(g.duration(140), "2 hours 20 minutes");
  assert.equal(g.duration(60), "1 hour");
  assert.equal(g.duration(4), "4 minutes");
  assert.equal(g.zone(45), "GMT+3");
  assert.equal(g.zone(-30), "GMT−2");
  assert.equal(g.zone(15), "GMT+1");   // Cameroon: West Africa Time
  assert.equal(g.zone(0), "GMT");
  assert.throws(() => g.zone(20), RangeError);
  assert.ok(g.sameDay(0) && g.sameDay(1439) && !g.sameDay(1440) && !g.sameDay(-1));
});

test("leap years (Form 1 rule, 2001–2099)", () => {
  assert.deepEqual([2024, 2027, 2028, 2100 - 1].map(g.daysInYear), [366, 365, 366, 365]);
  assert.throws(() => g.isLeap(2100), RangeError);
});

test("map scale: cm on the map ↔ km on the ground", () => {
  assert.equal(g.realKm(4, 50000), 2);
  assert.equal(g.realKm(3, 25000), 0.75);
  assert.equal(g.realKm(7, 100000), 7);
  assert.equal(g.mapCm(2, 50000), 4);
  assert.equal(g.ratio(50000), "1 : 50 000");
  assert.equal(g.ratio(5000), "1 : 5000");
});

test("grid references: eastings first, two digits each", () => {
  assert.equal(g.grid4(25, 34), "2534");
  assert.equal(g.grid4(5, 7), "0507");
  assert.equal(g.grid6(25, 3, 34, 7), "253347");
});

test("margin map: every arrangement uses A–E once, and letter ↔ part round-trips", () => {
  const seen = new Set();
  for (let k = 0; k < 120; k++) {
    const letters = g.marginParts.map((p) => g.marginLetter(k, p));
    assert.deepEqual([...letters].sort(), ["A", "B", "C", "D", "E"]);
    for (const p of g.marginParts) assert.equal(g.marginPart(k, g.marginLetter(k, p)), p);
    seen.add(letters.join(""));
  }
  assert.equal(seen.size, 120);
});

test("day and night: the half facing the Sun (left) is in daylight; the Earth turns anticlockwise", () => {
  assert.equal(g.dayOrNight(180), "day");
  assert.equal(g.dayOrNight(0), "night");
  assert.equal(g.dayOrNight(120), "day");
  assert.equal(g.dayOrNight(300), "night");
  assert.equal(g.sunriseOrSunset(100), "sunrise");  // top: turning towards the Sun
  assert.equal(g.sunriseOrSunset(260), "sunset");   // bottom: turning away
});

test("drawings are SVG images and refuse marks off the map", () => {
  for (const s of [
    g.gridMap(20, 30, [["school", 1.5, 2.5], ["well", 3.2, 4.7]]),
    g.graticule(-4, 8, 2, [["P", 0, 10], ["Q", 2, 14]]),
    g.marginMap(57), g.dayNight(135), g.parallels(),
  ]) {
    assert.match(s, SVG);
    assert.doesNotMatch(s, /NaN|undefined|Infinity/);
  }
  assert.throws(() => g.gridMap(20, 30, [["school", 5, 1]]), RangeError);
  assert.throws(() => g.graticule(0, 0, 2, [["P", 9, 1]]), RangeError);
  assert.equal(g.PARALLELS.length, 5);
});

test("tables: planets in order of distance; continents and oceans largest first", () => {
  const d = [0, 1, 2, 3, 4, 5, 6, 7].map(g.planetDistance);
  assert.deepEqual([...d].sort((a, b) => a - b), d);
  assert.equal(g.planetName(2), "Earth");
  const c = [0, 1, 2, 3, 4, 5, 6].map(g.continentArea), o = [0, 1, 2, 3, 4].map(g.oceanArea);
  assert.deepEqual([...c].sort((a, b) => b - a), c);
  assert.deepEqual([...o].sort((a, b) => b - a), o);
  assert.equal(g.continentName(1), "Africa");
});

test("drawings never repeat an attribute on one element (invalid SVG; HTML would keep only the first)", async () => {
  const physics = await import("../src/engine/lib/physics.js");
  for (const s of [g.gridMap(20, 30, [["school", 1.5, 2.5]]), g.graticule(-4, 8, 2, [["P", 0, 10]]), g.marginMap(3), g.dayNight(60), g.parallels(),
    physics.ruler(1, 4), physics.cylinder(40), physics.displacement(30, 44), physics.thermometer(25), physics.clinical(37.2)]) {
    for (const tag of s.match(/<[a-z]+ [^>]*>/g)) {
      const names = [...tag.matchAll(/ ([a-z-]+)="/g)].map((m) => m[1]);
      assert.equal(new Set(names).size, names.length, tag);
    }
  }
});
