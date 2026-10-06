// Geography Batch G1 content tests (Lessons 1–10, Term 1). Numbered by place in the year: PW1–PW3 are Lessons 4, 5–6 and 9.
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "geography", spine: "geography", prefix: "g", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography },
  batch: Array.from({ length: 10 }, (_, i) => i + 1),
});
