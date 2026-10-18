// Form 2 Geography, Batch G2-1 content tests (Term 1, rows 1–10; practicals and further study included).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import * as biology from "../src/engine/lib/biology.js";
import * as maths2 from "../src/engine/lib/maths2.js";
import * as science2 from "../src/engine/lib/science2.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "geography", dir: "form-2/geography", cls: "Form 2", spine: "form-2/geography", prefix: "g2-", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...geography, ...biology, ...maths2, ...science2 },
  batch: Array.from({ length: 10 }, (_, i) => i + 1),
});
