// Form 2 History, Batches Y2-1, Y2-2 and Y2-3 content tests (Terms 1–3, rows 1–22; guided work and further study included).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import * as homeeconomics from "../src/engine/lib/homeeconomics.js";
import * as history from "../src/engine/lib/history.js";
import * as biology from "../src/engine/lib/biology.js";
import * as maths2 from "../src/engine/lib/maths2.js";
import * as science2 from "../src/engine/lib/science2.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "history", dir: "form-2/history", cls: "Form 2", spine: "form-2/history", prefix: "y2-", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...maths2, ...science2 },
  batch: Array.from({ length: 22 }, (_, i) => i + 1),
});
