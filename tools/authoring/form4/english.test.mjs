import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { instantiate } from '../../../src/engine/template.js';
import { renderLearn } from '../../../src/engine/teach.js';
import { registrySubjects, libOf } from '../../classes.mjs';

const subject = registrySubjects().find((s) => s.id === 'f4-english');
const lib = await libOf(subject);
const read = (path) => JSON.parse(readFileSync(new URL(path, import.meta.url)));
const lessons = subject.lessons.map((n) => read(`../../../content/form-4/english/${n}.json`));
const lesson = (n) => lessons.find((l) => l.lesson_no === n);

test('English covers the teaching spine with goals, valid dependencies and seven original writing tasks', () => {
  const spine = read('../../../data/spine/form-4/english-language.json');
  assert.deepEqual(subject.lessons, spine.terms[0].lessons.filter((r) => r.kind === 'lesson').map((r) => r.seq));
  assert.deepEqual(lessons.filter((l) => l.paper_task).map((l) => l.lesson_no), [5, 8, 13, 22, 25, 28, 32]);
  for (const l of lessons) {
    const opening = renderLearn(l, lib).pages[0];
    for (const label of ['By the end', 'Builds on:', 'Leads to:']) assert.ok(opening.text.includes(label));
    for (const n of l.prerequisites) assert.ok(subject.lessons.includes(n) && n < l.lesson_no);
    assert.equal(l.questions.length, 5);
    if (l.paper_task) {
      assert.ok(l.paper_task.model.join(' ').split(/\s+/).length >= 25);
      assert.ok(l.paper_task.checklist.length >= 3);
    }
  }
});

test('displayed base verbs produce independently checked past and participle forms', () => {
  for (const [n, id, expected] of [
    [4, 'e4-4-verb', { buy: 'bought', choose: 'chose', make: 'made', take: 'took' }],
    [29, 'e4-29-participle', { take: 'taken', choose: 'chosen', write: 'written', see: 'seen' }],
  ]) {
    const seen = new Set();
    const t = lesson(n).questions.find((q) => q.id === id);
    for (let seed = 1; seed <= 120; seed++) {
      const q = instantiate(t, seed, lib);
      const verb = q.prompt.match(/Base verb: (\w+)/)[1];
      seen.add(verb);
      assert.equal(q.answer, expected[verb], q.prompt);
      assert.equal(q.options.length, 4);
    }
    assert.deepEqual([...seen].sort(), Object.keys(expected).sort());
  }
});

test('dental and user-confirmed affricate model words are classified correctly', () => {
  for (const [n, groups] of [[7, { '/θ/': ['think', 'thin', 'thank', 'thing'], '/ð/': ['this', 'that', 'these', 'those'] }],
    [19, { '/tʃ/': ['chair', 'cheap', 'chalk', 'choose'], '/dʒ/': ['judge', 'jam', 'joy', 'join'] }]]) {
    const t = lesson(n).questions.find((q) => q.id === `e4-${n}-sound`);
    const seen = new Set();
    for (let seed = 1; seed <= 160; seed++) {
      const q = instantiate(t, seed, lib);
      const word = q.prompt.match(/model for (\w+)/)[1];
      seen.add(word);
      assert.ok(groups[q.answer]?.includes(word), `${word}: ${q.answer}`);
      const feedback = q.options.filter((o, i) => i !== q.correctIndex).map((o) => o.explain);
      assert.equal(new Set(feedback).size, 3);
    }
    assert.equal(seen.size, 8);
    assert.match(renderLearn(lesson(n), lib).pages.map((p) => p.text).join(' '), /printed choices cannot assess your pronunciation/);
  }
});

// Parse the displayed phrase independently of the engine's words() helper.
const small = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'];
const tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'];
function phraseValue(s) {
  let total = 0, group = 0;
  for (const word of s.toLowerCase().replace(/-/g, ' ').split(/\s+/)) {
    if (small.includes(word)) group += small.indexOf(word);
    else if (tens.includes(word)) group += (tens.indexOf(word) + 2) * 10;
    else if (word === 'hundred') group *= 100;
    else if (word === 'thousand') { total += group * 1000; group = 0; }
    else assert.equal(word, 'and', `Unexpected number word ${word}`);
  }
  return total + group;
}
test('number phrases and fictional money-script balance preserve the stated amounts', () => {
  const t = lesson(26).questions.find((q) => q.id === 'e4-26-amount');
  for (let seed = 1; seed <= 200; seed++) {
    const q = instantiate(t, seed, lib);
    assert.equal(q.answerValue, phraseValue(q.prompt.match(/figures: (.*?) CFA francs/)[1]));
  }
  const money = lesson(27).questions.find((q) => q.id === 'e4-27-apply');
  let checked = false;
  for (let seed = 1; seed <= 60; seed++) {
    const q = instantiate(money, seed, lib);
    if (!q.prompt.includes('What amount remains')) continue;
    checked = true;
    const values = [...q.prompt.replace(/[\u00a0\u202f]/g, '').matchAll(/\d+/g)].map((m) => Number(m[0]));
    assert.equal(Number(q.answer.replace(/\D/g, '')), values[0] - values[1]);
    assert.equal(values[3], values[0] - values[1]);
  }
  assert.ok(checked);
});
