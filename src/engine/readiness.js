// Lesson 0: Primary 6 readiness check. Sets a readiness score and flags weak foundations.
// It never sets Form 1 mastery or coverage (decision 2026-10-02).

import { instantiate } from "./template.js";

function templateOf(lesson0, id) {
  const tpl = lesson0.questions.find((t) => t.id === id);
  if (!tpl) throw new Error(`readiness: no template ${id}`);
  return tpl;
}

/** lesson0: content/maths/0.json. Returns the questions in order. */
export function buildReadiness(lesson0, seed, lib) {
  return lesson0.readiness.items.map((item, i) => instantiate(templateOf(lesson0, item.template), seed + i, lib, 0));
}

/**
 * results: [{template, correct}]  ("I don't know" is recorded as correct: false)
 * Returns {right, asked, percent, areas: {area: {name, right, asked, weak}}, weak: [area]}.
 */
export function scoreReadiness(lesson0, results) {
  const spec = lesson0.readiness;
  const areas = Object.fromEntries(Object.entries(spec.areas).map(([id, name]) => [id, { name, right: 0, asked: 0, weak: false }]));
  for (const r of results) {
    const a = areas[templateOf(lesson0, r.template).area];
    a.asked += 1;
    a.right += r.correct ? 1 : 0;
  }
  for (const a of Object.values(areas)) a.weak = a.asked > 0 && a.right / a.asked < spec.weak_if_below;
  const right = results.filter((r) => r.correct).length;
  return {
    right, asked: results.length,
    percent: results.length ? Math.round((100 * right) / results.length) : 0,
    areas,
    weak: Object.entries(areas).filter(([, a]) => a.weak).map(([id]) => id),
  };
}
