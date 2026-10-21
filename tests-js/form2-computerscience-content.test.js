// Form 2 Computer Science, Batches S2-1 and S2-2 content tests (Term 1: rows 1, 2, 4–6, 8, 9, 11, 12, 14–16, 18, 19; Term 2: rows 21, 22, 24, 26, 27, 29–34, 36–40; integration rows are not lessons).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import * as homeeconomics from "../src/engine/lib/homeeconomics.js";
import * as history from "../src/engine/lib/history.js";
import * as computerscience from "../src/engine/lib/computerscience.js";
import * as biology from "../src/engine/lib/biology.js";
import * as maths2 from "../src/engine/lib/maths2.js";
import * as science2 from "../src/engine/lib/science2.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "computer-science", dir: "form-2/computer-science", cls: "Form 2", spine: "form-2/computer-science", prefix: "s2-", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...maths2, ...science2 },
  batch: [1, 2, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16, 18, 19, 21, 22, 24, 26, 27, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40],
});
