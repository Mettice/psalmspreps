import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { instantiate } from '../../../src/engine/template.js';
import { renderLearn } from '../../../src/engine/teach.js';
import { registrySubjects, libOf } from '../../classes.mjs';

const subject = registrySubjects().find((r) => r.id === 'f4-logic');
const lib = await libOf(subject);
const lessons = subject.lessons.map((n) => JSON.parse(readFileSync(new URL(`../../../content/form-4/logic/${n}.json`, import.meta.url))));
const template = (id) => lessons.flatMap((l) => l.questions).find((q) => q.id === id);

test('all teaching rows are present and their outcomes/connections render first', () => {
  const spine = JSON.parse(readFileSync(new URL('../../../data/spine/form-4/logic.json', import.meta.url)));
  assert.deepEqual(subject.lessons, spine.terms[0].lessons.filter((r) => r.kind === 'lesson').map((r) => r.seq));
  for (const l of lessons) {
    const first = renderLearn(l, lib).pages[0];
    assert.equal(first.heading, 'Your goal and connections');
    for (const label of ['By the end', 'Builds on:', 'Leads to:']) assert.ok(first.text.includes(label), `${l.lesson_no}: ${label}`);
    for (const p of l.prerequisites) assert.ok(subject.lessons.includes(p) && p < l.lesson_no);
  }
});

test('truth-table answers match independently enumerated conditional and OR cases', () => {
  const oracles = {
    'l4-8-truth': [[1, 1], [0, 1]],
    'l4-9-truth': [[0, 1], [1, 1]],
    'l4-9-exclusive': [[0, 1], [1, 0]],
  };
  for (const [id, table] of Object.entries(oracles)) {
    const seen = new Set();
    for (let seed = 1; seed <= 200; seed++) {
      const q = instantiate(template(id), seed, lib);
      const values = /P(?: has value| =)\s*(\d).*?Q(?: has value| =)?\s*(\d)/.exec(q.prompt);
      assert.ok(values, q.prompt);
      const [p, r] = values.slice(1).map(Number);
      seen.add(`${p}${r}`);
      assert.equal(q.answerValue, table[p][r], `${id}: ${p},${r}`);
    }
    assert.equal(seen.size, 4, `${id}: every truth-table row exercised`);
  }
});

test('distribution bank follows the accepted whole-class coverage table', () => {
  const t = template('l4-5-coverage');
  for (const x of t.vars.X.pick) {
    const statement = x.q.split(': ')[1];
    const expected = statement.startsWith('All ') ? 'Subject only'
      : statement.startsWith('No ') ? 'Both subject and predicate'
      : statement.includes(' are not ') ? 'Predicate only' : 'Neither term';
    assert.equal(x.r, expected, statement);
  }
});

test('diagram questions preserve the distinct empty/existence markings', () => {
  const diagrams = template('l4-6-read-diagram').vars.X.pick;
  assert.equal(diagrams.length, 4);
  for (const x of diagrams) {
    assert.match(x.svg, /^<svg/);
    if (x.r.startsWith('All ')) {
      assert.match(x.svg, /cx="120" cy="95" r="65" fill="#b4c9bf"/);
      assert.match(x.svg, /fill="white"/);
    } else if (x.r.startsWith('No ')) {
      assert.match(x.svg, /clip-path="url\(#subject\)".*cx="195".*fill="#b4c9bf"/);
    } else if (x.r.includes('not')) {
      assert.match(x.svg, /x="87".*>x<\/text>/);
    } else {
      assert.match(x.svg, /x="158".*>x<\/text>/);
    }
  }
});
