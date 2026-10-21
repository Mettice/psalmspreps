// Form 2 Physics, Batch P2-1 content tests (Term 1, rows 1–15). Numbered by place in the year (proposal G1).
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as biology from "../src/engine/lib/biology.js";
import * as maths2 from "../src/engine/lib/maths2.js";
import * as science2 from "../src/engine/lib/science2.js";
import { subjectSuite } from "./subject-suite.js";

subjectSuite({
  subject: "physics", dir: "form-2/physics", cls: "Form 2", spine: "form-2/physics", prefix: "p2-", numbering: "seq",
  lib: { ...maths, ...english, ...physics, ...chemistry, ...biology, ...maths2, ...science2 },
  batch: Array.from({ length: 36 }, (_, i) => i + 1),
});
