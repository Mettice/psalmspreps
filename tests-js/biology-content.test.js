// Biology Batch B1 content tests (Term 1: Lessons 1–9, 13–21). Lesson numbers equal the rows; the practicals
// (6, 8, 14, 18) are kind "practical" on the sheet, so lessons are matched to the spine by place in the year.
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import * as homeeconomics from "../src/engine/lib/homeeconomics.js";
import * as history from "../src/engine/lib/history.js";
import * as biology from "../src/engine/lib/biology.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "biology", spine: "biology", prefix: "b", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology },
  batch: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21],
});
