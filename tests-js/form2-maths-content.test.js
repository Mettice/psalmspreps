// Form 2 Maths, Batch M2-1 content tests (Term 1, rows 1–24 of the Form 2 sheet). Numbered by place in the year
// (proposal G1, approved by Dion 2026-10-17); row 1 is the diagnostic test, deferred.
import * as maths from "../src/engine/lib/maths.js";
import * as maths2 from "../src/engine/lib/maths2.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "mathematics", dir: "form-2/maths", cls: "Form 2", spine: "form-2/mathematics", prefix: "m2-", numbering: "seq",
  lib: { ...maths, ...maths2 },
  batch: Array.from({ length: 24 }, (_, i) => i + 1),
});
