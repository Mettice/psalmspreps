// Computer Science Batch S1 content tests (Term 1: Lessons 1–6, 8–11, 13–14, 16–18; the other rows are integration activities).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import * as homeeconomics from "../src/engine/lib/homeeconomics.js";
import * as history from "../src/engine/lib/history.js";
import * as biology from "../src/engine/lib/biology.js";
import * as computerscience from "../src/engine/lib/computerscience.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "computer-science", spine: "computer-science", prefix: "cs",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience },
  batch: [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 16, 17, 18],
});
