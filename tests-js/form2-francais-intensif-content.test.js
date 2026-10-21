// Form 2 Français intensif, Batches FI2-1 and FI2-2 content tests (Term 1, rows 1–25 and 27–51; Term 2, rows 53–76 and 78–102; integration rows 26, 52, 77 and 103 are not
// lessons). Same rules as every subject, plus: every template is marked lang "fr".
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
import * as french2 from "../src/engine/lib/french2.js";
import { subjectSuite } from "./subject-suite.js";

const BATCH = [...Array.from({ length: 25 }, (_, i) => i + 1), ...Array.from({ length: 25 }, (_, i) => i + 27), ...Array.from({ length: 24 }, (_, i) => i + 53), ...Array.from({ length: 25 }, (_, i) => i + 78)];
subjectSuite({
  subject: "francais-intensif", dir: "form-2/francais-intensif", cls: "Form 2", spine: "form-2/francais-intensif", prefix: "fi2-", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...french, ...french2 },
  batch: BATCH,
});

test("form 2 français intensif: every template is marked lang fr", () => {
  for (const n of BATCH) {
    const l = JSON.parse(readFileSync(new URL(`../content/form-2/francais-intensif/${n}.json`, import.meta.url), "utf8"));
    assert.equal(l.language, "fr");
    for (const t of [...l.questions, ...l.teach.cards.filter((c) => !c.check.ref).map((c) => c.check)]) assert.equal(t.lang, "fr", t.id);
  }
});
