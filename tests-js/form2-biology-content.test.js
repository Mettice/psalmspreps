// Form 2 Biology, Batches B2-1 and B2-2 content tests (Term 1: rows 1–9 and 13–21; Term 2: rows 25–33 and 37–46; integration, evaluation and remediation rows are not lessons). Numbered by place in the year (proposal G1).
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
  batch: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 25, 26, 27, 28, 29, 30, 31, 32, 33, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
});
