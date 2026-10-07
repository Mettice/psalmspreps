// History Batch Y1 content tests (Lessons 1–10, Term 1). Numbered by place in the year: most rows are further study or guided work.
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import * as homeeconomics from "../src/engine/lib/homeeconomics.js";
import * as history from "../src/engine/lib/history.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "history", spine: "history", prefix: "hi", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history },
  batch: Array.from({ length: 10 }, (_, i) => i + 1),
});
