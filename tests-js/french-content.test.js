// French Batch F1 content tests (Lessons 1–15, first half of Term 1). Same rules as every subject, plus: every
// template is marked lang: "fr" so the working the engine writes is in French too.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import * as homeeconomics from "../src/engine/lib/homeeconomics.js";
import * as history from "../src/engine/lib/history.js";
import * as biology from "../src/engine/lib/biology.js";
import * as computerscience from "../src/engine/lib/computerscience.js";
import * as french from "../src/engine/lib/french.js";
import { subjectSuite } from "./subject-suite.js";

const BATCH = Array.from({ length: 15 }, (_, i) => i + 1);
subjectSuite({
  subject: "french", spine: "french", prefix: "f",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...french },
  batch: BATCH,
});

test("french: every template is marked lang fr", () => {
  for (const n of BATCH) {
    const l = JSON.parse(readFileSync(new URL(`../content/french/${n}.json`, import.meta.url), "utf8"));
    assert.equal(l.language, "fr");
    for (const t of [...l.questions, ...l.teach.cards.filter((c) => !c.check.ref).map((c) => c.check)]) assert.equal(t.lang, "fr", t.id);
  }
});
