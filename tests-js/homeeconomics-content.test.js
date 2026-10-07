// Home Economics Batch H1 content tests (Term 1: Lessons 1–7, 10–17, 20–21; rows 8–9 and 18–19 are integration and remediation).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import * as homeeconomics from "../src/engine/lib/homeeconomics.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "home-economics", spine: "home-economics", prefix: "he",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics },
  batch: [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21],
});
