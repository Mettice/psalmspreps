// Form 2 Chemistry, Batch C2-1 content tests (Term 1: rows 1–4, 6–11, 13–17; integration and review rows are not lessons). Numbered by place in the year (proposal G1).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as biology from "../src/engine/lib/biology.js";
import * as maths2 from "../src/engine/lib/maths2.js";
import * as science2 from "../src/engine/lib/science2.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "chemistry", dir: "form-2/chemistry", cls: "Form 2", spine: "form-2/chemistry", prefix: "k2-", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...biology, ...maths2, ...science2 },
  batch: [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17],
});
