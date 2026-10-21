import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import * as physics from "../src/engine/lib/physics.js";
import * as chemistry from "../src/engine/lib/chemistry.js";
import * as geography from "../src/engine/lib/geography.js";
import * as homeeconomics from "../src/engine/lib/homeeconomics.js";
import * as history from "../src/engine/lib/history.js";
import * as biology from "../src/engine/lib/biology.js";
import * as computerscience from "../src/engine/lib/computerscience.js";
import * as french from "../src/engine/lib/french.js";
import * as french2 from "../src/engine/lib/french2.js";
import * as template from "../src/engine/template.js";
const { instantiate, check } = template;
import * as teach from "../src/engine/teach.js";

const lib = { ...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history, ...biology, ...computerscience, ...french, ...french2 };
const pilots = [["maths", 7], ["form-2/accounting", 1], ["physics", 16], ["chemistry", 8], ["biology", 13], ["history", 2], ["geography", 5], ["english", 13], ["french", 3], ["form-2/francais-intensif", 1], ["computer-science", 11], ["home-economics", 20]];
const load = (dir, n) => JSON.parse(readFileSync(new URL(`../content/${dir}/${n}.json`, import.meta.url), "utf8"));

for (const [dir, n] of pilots) {
  const lesson = load(dir, n);
  test(`${dir} ${n}: pilot stages render, accept their correct answers, reject wrong answers`, () => {
    const ids = new Set(lesson.questions.map((q) => q.id));
    assert.equal(lesson.activity.status, "draft");
    const sources = JSON.parse(readFileSync(new URL(`../content/${dir}/sources.json`, import.meta.url), "utf8"));
    for (const stage of lesson.activity.stages) {
      const tpl = stage.question;
      assert.ok(stage.title && !ids.has(tpl.id));
      ids.add(tpl.id);
      assert.ok(tpl.sources.every((s) => sources[s]?.ref));
      for (let seed = 1; seed <= 1000; seed++) {
        const q = instantiate(tpl, seed, lib, n);
        assert.equal(q.verified, true);
        assert.doesNotMatch([q.prompt, q.answer, ...q.solution].join(" "), /undefined|NaN|Infinity|\{[^}]*\}/);
        assert.ok(q.solution.length);
        const answer = q.options ? q.correctIndex : q.type === "blanks" ? q.answers : q.answer;
        assert.equal(check(q, answer).correct, true);
        if (q.options) assert.equal(check(q, (q.correctIndex + 1) % q.options.length).correct, false);
        else if (q.type === "blanks") assert.equal(check(q, q.answers.map(() => "-999")).correct, false);
        else assert.equal(check(q, "-999").correct, false);
        if (q.figure) assert.match(q.figure, /^<svg [\s\S]*<\/svg>$/);
      }
    }
    if (lesson.activity.reflection) {
      const p = teach.renderPaper({ paper_task: lesson.activity.reflection }, lib);
      assert.ok(p.prompt && p.model.length && p.checklist.length);
      assert.deepEqual(p.failedChecks, []);
    }
  });

  test(`${dir} ${n}: activity follows the worked example, completes and supports targeted review`, () => {
    let flow = teach.startTeach(lesson, 42);
    const stages = flow.steps.filter((s) => s.kind === "activity");
    assert.equal(flow.steps[flow.steps.findIndex((s) => s.kind === "worked_example") + 1].kind, "activity");
    assert.deepEqual(stages.map((s) => s.template), lesson.activity.stages.map((s) => s.question.id));
    while (!teach.isDone(flow)) {
      const step = flow.steps[flow.step];
      if ((step.kind === "card" || step.kind === "practice" || step.kind === "activity") && flow.phase === "check") {
        teach.itemQuestion(lesson, flow, lib);
        flow = teach.answerItem(flow, { correct: true }, 100);
      } else flow = teach.nextPhase(flow);
    }
    assert.equal(flow.log.filter((e) => e.kind === "activity").length, stages.length);
    flow = teach.startReview(lesson, stages.map((s) => s.template), 99);
    while (!teach.isDone(flow)) {
      if (flow.phase === "check") flow = teach.answerItem(flow, { correct: false }, 100);
      else flow = teach.nextPhase(flow);
    }
    assert.deepEqual(teach.needsReview(flow).map((s) => s.template), stages.map((s) => s.template));
  });
}

test("language activity UI: answer stages, write before the model, save self-checks and export them", () => {
  class Node {
    constructor(tag, text = "") { this.tag = tag; this.text = text; this.children = []; this.events = {}; this.attrs = {}; this.nodeType = 1; this.style = { setProperty() {} }; }
    append(...nodes) { this.children.push(...nodes); }
    replaceChildren(...nodes) { this.children = nodes; }
    setAttribute(k, v) { this.attrs[k] = v; }
    addEventListener(k, fn) { this.events[k] = fn; }
    focus() {}
    get textContent() { return this.text + this.children.map((c) => c.textContent).join(""); }
  }
  const app = readFileSync(new URL("../tools/prototype/app.js", import.meta.url), "utf8");
  const factory = new Function("env", `const { ENGINE, CONTENT, TITLES, LESSONS, SUBJECTS, CLASS_OF, CLASSES, BUILD, document, localStorage, window, setTimeout } = env;
    const addEventListener = () => {}; ${app}; return { state, openLesson, lesson, lessonResultsText };`);
  for (const [dir, subject, n] of [["english", "english", 13], ["french", "french", 3], ["form-2/francais-intensif", "f2-francais-intensif", 1]]) {
    const l = load(dir, n), root = new Node("root");
    let stored;
    const ui = factory({ ENGINE: { libs: { [subject]: lib }, template, teach }, CONTENT: { [subject]: { [n]: l } },
      TITLES: { [subject]: { [n]: "Pilot" } }, LESSONS: { [subject]: [n] }, SUBJECTS: { [subject]: "Language" },
      CLASS_OF: { [subject]: "form-1" }, CLASSES: { "form-1": "Form One" }, BUILD: "test",
      document: { getElementById: () => root, createElement: (tag) => new Node(tag), createElementNS: (_, tag) => new Node(tag), createTextNode: (s) => new Node("text", s), documentElement: {} },
      localStorage: { getItem: () => null, setItem: (_, value) => { stored = value; } }, window: { scrollTo() {} }, setTimeout() {} });
    const nodes = (node = root) => [node, ...node.children.flatMap((c) => nodes(c))];
    const click = (label) => {
      const b = nodes().find((x) => x.tag === "button" && x.textContent === label);
      assert.ok(b, `${subject}: missing button ${label}`);
      b.events.click();
    };
    ui.openLesson(subject, n);
    const current = ui.state.current[subject];
    const start = current.flow.steps.findIndex((s) => s.kind === "activity");
    ui.lesson({ ...current.flow, step: start, phase: "check" });
    for (const stage of l.activity.stages) {
      const q = teach.itemQuestion(l, current.flow, lib);
      assert.ok(root.textContent.includes(stage.title));
      click(q.answer);
      click(subject === "english" ? "Next" : "Suivant");
    }
    assert.equal(current.flow.steps[current.flow.step].kind, "activity_reflection");
    const model = l.activity.reflection.model[0];
    assert.ok(!root.textContent.includes(model), "model is hidden until the pupil has written");
    click(subject === "english" ? "I've written it" : "J’ai écrit");
    assert.ok(root.textContent.includes(model));
    const box = nodes().find((x) => x.tag === "input" && x.attrs.type === "checkbox");
    box.checked = true;
    box.events.change();
    assert.equal(JSON.parse(stored).current[subject].activityPaper.ticks[0], true);
    click(subject === "english" ? "Done" : "Terminé");
    assert.equal(current.flow.steps[current.flow.step].kind, "practice", "writing supplements ordinary practice");
    let flow = current.flow;
    while (!teach.isDone(flow)) flow = flow.phase === "check" ? teach.answerItem(flow, { correct: true }, 100) : teach.nextPhase(flow);
    ui.lesson(flow);
    const record = ui.state.lessons[`${subject}:${n}`];
    assert.equal(record.activityPaper.ticks[0], true);
    assert.equal(record.rows.filter((r) => r.phase === "activity").length, l.activity.stages.length);
    assert.match(ui.lessonResultsText(subject, n), /activity writing \(not marked; self-check by the pupil\): 1 of 3 ticked/);
  }
});
