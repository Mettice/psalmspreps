import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { instantiate } from '../../../src/engine/template.js';
import { renderLearn } from '../../../src/engine/teach.js';
import { registrySubjects, libOf } from '../../classes.mjs';

const subject = registrySubjects().find((s) => s.id === 'f4-history');
const lib = await libOf(subject);
const read = (p) => JSON.parse(readFileSync(new URL(p, import.meta.url)));
const lessons = subject.lessons.map((n) => read(`../../../content/form-4/history/${n}.json`));
const lesson = (n) => lessons.find((l) => l.lesson_no === n);
const textOf = (n) => renderLearn(lesson(n), lib).pages.map((p) => p.text).join(' ');

test('History covers every lesson row with goals and valid earlier dependencies', () => {
  const spine = read('../../../data/spine/form-4/history.json');
  assert.deepEqual(subject.lessons, spine.terms[0].lessons.filter((r) => r.kind === 'lesson').map((r) => r.seq));
  assert.equal(lessons.length, 14);
  for (const l of lessons) {
    assert.equal(l.questions.length, 5);
    const opening = renderLearn(l, lib).pages[0];
    for (const label of ['By the end', 'Builds on:', 'Leads to:']) assert.ok(opening.text.includes(label));
    for (const n of l.prerequisites) assert.ok(subject.lessons.includes(n) && n < l.lesson_no);
  }
});

// Check dates independently against event names in the pupil's actual displayed tiles.
const dates = [
  [/Rhineland/, 1936, 3], [/Munich/, 1938, 9], [/Czech lands/, 1939, 3], [/invasion of Poland/, 1939, 9],
  [/European war begins/, 1939, 9], [/Youth League/, 1940, 3], [/trusteeship agreements approved/, 1946, 12], [/CDC/, 1947, 1],
  [/Free French rallying|rallies to Free France/, 1940, 8], [/USCC/, 1944, 1], [/Douala labour conflict/, 1945, 9],
  [/ARCAM/, 1946, 1], [/UPC/, 1948, 4], [/Brazzaville/, 1944, 1], [/Second World War ends/, 1945, 9],
  [/Yalta/, 1945, 2], [/Potsdam/, 1945, 7], [/Iron Curtain/, 1946, 3], [/Truman Doctrine/, 1947, 3],
  [/Marshall Plan/, 1948, 1], [/NATO/, 1949, 4], [/Warsaw Pact/, 1955, 5], [/Limited Test Ban/, 1963, 8],
  [/SALT/, 1972, 5], [/Helsinki/, 1975, 8], [/Afghanistan/, 1979, 12], [/JEUCAFRA/, 1938, 1], [/BDC/, 1951, 1],
];
test('eight varied chronological exercises preserve the dated event sequence', () => {
  const templates = lessons.flatMap((l) => l.questions).filter((t) => t.type === 'ordering');
  assert.equal(templates.length, 8);
  for (const t of templates) {
    const variants = new Set();
    for (let seed = 1; seed <= 160; seed++) {
      const q = instantiate(t, seed, lib);
      const ordered = q.correctOrder.map((i) => q.items[i]);
      variants.add(JSON.stringify(ordered));
      const keys = ordered.map((item) => {
        const record = dates.find(([name]) => name.test(item));
        assert.ok(record, item);
        assert.equal(Number(item.match(/\b(19\d\d)\b/)[1]), record[1], item);
        return record[1] * 12 + record[2];
      });
      assert.deepEqual(keys, keys.slice().sort((a, b) => a - b), q.answer);
    }
    assert.ok(variants.size >= 4, t.id);
  }
});

test('source exercises disclose invented provenance and preserve the selected claim across variants', () => {
  for (const l of lessons) {
    const t = l.questions.find((q) => q.id.endsWith('-source'));
    const seen = new Set();
    for (let seed = 1; seed <= 80; seed++) {
      const q = instantiate(t, seed, lib);
      seen.add(q.prompt);
      assert.match(q.prompt, /^Invented classroom source/);
      assert.match(q.prompt, /not an archive quotation/);
      assert.match(q.prompt, /real historical proof requires authentic evidence/);
      assert.equal(q.options.length, 4);
      assert.equal(new Set(q.options.filter((o, i) => i !== q.correctIndex).map((o) => o.explain)).size, 3);
    }
    assert.ok(seen.size >= 4);
  }
  // These distinctions prevent serious historical misreadings of reform and supervision.
  assert.match(textOf(7), /rejected political development outside the French framework/);
  assert.match(textOf(14), /Britain and France continued to administer/);
  assert.match(textOf(14), /did not grant immediate independence/);
  assert.match(textOf(14), /did not guarantee an immediate remedy/);
  assert.match(textOf(13), /not the destruction of every weapon/);
});
