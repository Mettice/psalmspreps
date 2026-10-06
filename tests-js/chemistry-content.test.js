// Chemistry Batch C1 content tests (Lessons 1–21, Term 1).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "chemistry", spine: "chemistry", prefix: "ch",
  lib: { ...maths, ...english, ...physics, ...chemistry },
  batch: Array.from({ length: 21 }, (_, i) => i + 1),
});
