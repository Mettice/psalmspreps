// Form 2 English, Batches E2-1, E2-2 and E2-3 content tests (Terms 1–3, rows 1–104 of the Form 2 sheet). Numbered by place in the year
// (proposal G1, approved by Dion 2026-10-17). Speech work is deferred (needs audio); writing lessons are paper tasks.
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "english-language", dir: "form-2/english", cls: "Form 2", spine: "form-2/english-language", prefix: "e2-", numbering: "seq",
  lib: { ...maths, ...english },
  batch: Array.from({ length: 104 }, (_, i) => i + 1),
});
