// Pupil state for one subject (decisions 2026-10-02):
//
//   coverage[lesson_no] = "not_taught" | "taught"        Has the class covered it? Every lesson starts
//                                                        not_taught; only the weekly teacher checklist
//                                                        changes it. (The app is the pupil's main teacher.)
//   mastery[skill_id]   = "unknown" | "shaky" | "solid"  Can the pupil do it? Starts unknown; set only
//                                                        by answers in Form 1 lessons.
//   readiness                                            Primary 6 readiness from Lesson 0. Never touches
//                                                        coverage or mastery.
//
// All functions are pure: they return a new state.

export const COVERAGE = ["not_taught", "taught"];
export const MASTERY = ["unknown", "shaky", "solid"];

/** A lesson's skills: its declared `skills`, or one implicit skill named after the lesson. */
export function skillsOf(lesson) {
  return lesson.skills ? lesson.skills.map((s) => s.id) : [`m${lesson.lesson_no}`];
}

/** The skill a template trains: its `skill`, or the lesson's only skill. */
export function skillOf(lesson, tpl) {
  if (tpl.skill) return tpl.skill;
  const skills = skillsOf(lesson);
  if (skills.length !== 1) throw new Error(`${tpl.id}: lesson ${lesson.lesson_no} has several skills; set "skill"`);
  return skills[0];
}

export function emptyState() {
  return { coverage: {}, coverageSource: {}, mastery: {}, readiness: null };
}

/**
 * Weekly "Which of these lessons did your teacher actually cover?"
 * answers: {lesson_no: true | false} for the lessons shown.
 */
export function applyChecklist(state, answers) {
  const coverage = { ...state.coverage }, coverageSource = { ...state.coverageSource };
  for (const [lesson, taught] of Object.entries(answers)) {
    coverage[lesson] = taught ? "taught" : "not_taught";
    coverageSource[lesson] = "checklist";
  }
  return { ...state, coverage, coverageSource };
}

/** Lesson 0 result (from scoreReadiness). Sets readiness and nothing else. */
export function applyReadiness(state, readiness, takenAt) {
  return { ...state, readiness: { ...readiness, takenAt } };
}

export const masteryOf = (state, skill) => state.mastery[skill] || "unknown";
export const coverageOf = (state, lesson) => state.coverage[lesson] || "not_taught";
