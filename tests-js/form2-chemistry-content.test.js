// Form 2 Chemistry, Batches C2-1 and C2-2 content tests (Term 1: rows 1–4, 6–11, 13–17; Term 2: rows 20–27, 29–38, 40–45; integration rows are not lessons). Numbered by place in the year (proposal G1).
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
  batch: [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 55, 56, 57, 58, 59],
});
