// Content tests for every subject in content/classes.json (Form 3 on, 2026-10-23): the same rules as every subject
// (tests-js/subject-suite.js), run on the lesson files present. A subject with no lesson yet is skipped.
// Nothing to edit here when lessons are added: put the files in content/<class>/<subject>/ and run npm test.
import { registrySubjects, libOf } from "../tools/classes.mjs";
import { subjectSuite } from "./subject-suite.js";

for (const r of registrySubjects().filter((x) => x.lessons.length)) {
  subjectSuite({ subject: r.lessonSubject, spine: r.spine, lib: await libOf(r), batch: r.lessons, prefix: r.ids, numbering: "seq", dir: r.dir, cls: r.clsLabel });
}
