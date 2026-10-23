// Additional reviewer checks for Codex-authored subjects. Does not change the shared suite.
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { registrySubjects, libOf } from '../../classes.mjs';
import { instantiate } from '../../../src/engine/template.js';
import { cardCheckTemplate } from '../../../src/engine/teach.js';

const requested = process.argv.slice(2);
const subjects = registrySubjects().filter((r) => requested.includes(r.id));
assert.equal(subjects.length, requested.length, 'Unknown subject id');
let count = 0;
for (const r of subjects) {
  const lib = await libOf(r);
  for (const n of r.lessons) {
    const l = JSON.parse(readFileSync(new URL(`../../../content/${r.dir}/${n}.json`, import.meta.url), 'utf8'));
    if (l.status === 'deferred') continue;
    assert.ok(l.learn?.sections?.length, `${r.id}:${n}: Learn is required`);
    assert.ok(l.questions.length >= 4 && l.questions.length <= 6, `${r.id}:${n}: require 4–6 questions`);
    for (const tpl of [...l.questions, ...l.teach.cards.map((c) => cardCheckTemplate(l, c))]) {
      const seen = new Set();
      for (let seed = 1; seed <= 160; seed++) {
        const q = instantiate(tpl, seed, lib, n);
        // Ignore option/tile order: a shuffled fixed question is not a new content variant.
        seen.add(JSON.stringify([q.prompt, q.sentence, q.parts, q.answer, q.figure,
          q.options?.map((o) => o.text).sort(), q.left?.slice().sort()]));
        for (const [i, o] of (q.options || []).entries()) {
          if (i !== q.correctIndex) assert.ok(o.explain, `${tpl.id}: no feedback for ${o.text}`);
        }
        if (r.lang === 'fr') assert.equal(tpl.lang, 'fr', tpl.id);
      }
      assert.ok(seen.size >= 3, `${tpl.id}: only ${seen.size} content variants`);
    }
    count++;
  }
}
console.log(`${count} lessons meet the extra content-variation, Learn and feedback checks.`);
