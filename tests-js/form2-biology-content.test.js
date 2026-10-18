// Form 2 Biology, Batch B2-1 content tests (Term 1: rows 1–9 and 13–21; integration, evaluation and remediation rows are not lessons). Numbered by place in the year (proposal G1).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as biology from "../src/engine/lib/biology.js";
import * as maths2 from "../src/engine/lib/maths2.js";
import * as science2 from "../src/engine/lib/science2.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "biology", dir: "form-2/biology", cls: "Form 2", spine: "form-2/biology", prefix: "b2-", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...biology, ...maths2, ...science2 },
  batch: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21],
});
