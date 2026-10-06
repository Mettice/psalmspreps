// Physics Batch P1 content tests (Lessons 1–19, Term 1).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "physics", spine: "physics", prefix: "p",
  lib: { ...maths, ...english, ...physics },
  batch: Array.from({ length: 19 }, (_, i) => i + 1),
});
