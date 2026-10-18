// Form 2 Home Economics, Batch H2-1 content tests (Term 1: rows 1–9 and 12–21; integration and remediation rows are not lessons).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import * as homeeconomics from "../src/engine/lib/homeeconomics.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "home-economics", dir: "form-2/home-economics", cls: "Form 2", spine: "form-2/home-economics", prefix: "h2-", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics },
  batch: [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
});
