// The subjects of content/classes.json (Form 3 on, 2026-10-23), for the build, the tests and the review files.
// A subject's lessons are the numbered JSON files present in its folder: adding a lesson needs no list to edit.
import { readFileSync, readdirSync, existsSync } from "node:fs";

const ROOT = new URL("../", import.meta.url);

/** [{id, cls, className, clsLabel, dir, spine, name, lessonSubject, ids, libs, lang, lessons}] */
export function registrySubjects() {
  const reg = JSON.parse(readFileSync(new URL("content/classes.json", ROOT), "utf8"));
  return Object.entries(reg).filter(([c]) => !c.startsWith("_")).flatMap(([c, k]) => Object.entries(k.subjects).map(([d, s]) => {
    const folder = new URL(`content/${c}/${d}/`, ROOT);
    const lessons = existsSync(folder) ? readdirSync(folder).filter((f) => /^\d+\.json$/.test(f)).map((f) => Number(f.slice(0, -5))).sort((a, b) => a - b) : [];
    return { id: `${k.prefix}-${d}`, cls: c, className: k.name, clsLabel: k.cls, dir: `${c}/${d}`, spine: `${c}/${s.spine}`, name: s.name,
      lessonSubject: s.lesson_subject, ids: s.ids, libs: s.libs, lang: s.lang || "en", lessons };
  }));
}

/** The engine library object a subject's templates use: its modules merged in order. */
export async function libOf(subject) {
  const mods = await Promise.all(subject.libs.map((m) => import(new URL(`src/engine/lib/${m}.js`, ROOT))));
  return Object.assign({}, ...mods);
}
