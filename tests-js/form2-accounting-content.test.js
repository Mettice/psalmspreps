// Form 2 Accounting, Batches A2-1 and A2-2 content tests (Term 1: rows 1–8 and 10–12; Term 2: rows 13–18; row 9, remedial activities, is not a lesson).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as maths2 from "../src/engine/lib/maths2.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "accounting", dir: "form-2/accounting", cls: "Form 2", spine: "form-2/accounting", prefix: "a2-", numbering: "seq",
  lib: { ...maths, ...english, ...maths2 },
  batch: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18],
});
