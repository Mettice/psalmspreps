import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { instantiate } from '../../../src/engine/template.js';
import { renderLearn } from '../../../src/engine/teach.js';
import { registrySubjects, libOf } from '../../classes.mjs';

const subject = registrySubjects().find((r) => r.id === 'f4-economics');
const lib = await libOf(subject);
const lessons = subject.lessons.map((n) => JSON.parse(readFileSync(new URL(`../../../content/form-4/economics/${n}.json`, import.meta.url))));
const numbers = (text) => (text.replace(/[\u00a0\u202f]/g, '').match(/\d+/g) || []).map(Number);

test('all Term One rows including guided cases and the practical have visible goals and connections', () => {
  const spine = JSON.parse(readFileSync(new URL('../../../data/spine/form-4/economics.json', import.meta.url)));
  assert.deepEqual(subject.lessons, spine.terms[0].lessons.map((r) => r.seq));
  for (const l of lessons) {
    const first = renderLearn(l, lib).pages[0];
    assert.equal(first.heading, 'Your goal and connections');
    for (const label of ['By the end', 'Builds on:', 'Leads to:']) assert.ok(first.text.includes(label), `${l.lesson_no}: ${label}`);
    for (const p of l.prerequisites) assert.ok(subject.lessons.includes(p) && p < l.lesson_no);
    assert.equal(l.questions.length, 5);
  }
});

// Read actual displayed data, independently of the generator's hidden variable names.
const expectedFromPrompt = {
  'n4-1-profit': ([sales, cost]) => sales - cost,
  'n4-2-share': ([total, first, second]) => total * first / (first + second),
  'n4-3-shares': ([shares, face]) => shares * face,
  'n4-4-dividend': ([pool, allShares, holding]) => pool / allShares * holding,
  'n4-6-issued': ([shares, face]) => shares * face,
  'n4-7-authorised': ([shares, face]) => shares * face,
  'n4-7-issued': ([shares, ceiling, face]) => shares * face,
  'n4-7-called': ([shares, call]) => shares * call,
  'n4-7-paid': ([callTotal, unpaid]) => callTotal - unpaid,
  'n4-7-uncalled': ([shares, face, call]) => shares * (face - call),
  'n4-8-votes': ([eligible, absent]) => eligible - absent,
  'n4-9-surplus': ([pool, member, allPurchases]) => member / allPurchases * pool,
  'n4-10-gap': ([cost, fees]) => cost - fees,
  'n4-11-budget': ([funds, tools, operating]) => funds - tools - operating,
  'n4-12-public-share': ([all, state]) => state / all * 100,
  'n4-13-private-share': ([original, sold]) => (original - sold) / original * 100,
  'n4-14-average-saving': ([qA, costA, qB, costB]) => costA / qA - costB / qB,
  'n4-15-average-rise': ([costA, qA, costB, qB]) => costB / qB - costA / qA,
  'n4-16-growth-rate': ([start, finish]) => (finish / start - 1) * 100,
  'n4-18-small-profit': ([jobs, fee, cost]) => jobs * fee - cost,
  'n4-19-transport': ([a, loads, b]) => b * loads - a * loads,
  'n4-20-site-cost': ([rentA, inA, outA, bTotal]) => bTotal - rentA - inA - outA,
};

test('numeric answers agree with the amounts and bases actually shown to the pupil', () => {
  const numeric = lessons.flatMap((l) => l.questions).filter((t) => t.type === 'numeric');
  assert.deepEqual(numeric.map((t) => t.id).sort(), Object.keys(expectedFromPrompt).sort());
  for (const t of numeric) {
    for (let seed = 1; seed <= 120; seed++) {
      const q = instantiate(t, seed, lib);
      const expected = expectedFromPrompt[t.id](numbers(q.prompt));
      assert.ok(Number.isFinite(expected), q.prompt);
      assert.ok(Math.abs(q.answerValue - expected) < 1e-7, `${t.id}: ${q.prompt} => ${q.answerValue}, expected ${expected}`);
      assert.ok(q.answerValue >= 0, t.id);
    }
  }
});

test('capital table reconciles issued/called/paid-up without double counting', () => {
  const practical = lessons.find((l) => l.lesson_no === 7);
  const figure = renderLearn(practical, lib).pages.find((p) => p.figure).figure;
  assert.match(figure, /CFA francs - classroom model/);
  assert.doesNotMatch(figure, /u2014/);
  const values = [...figure.matchAll(/text-anchor="end">([^<]+)<\/text>/g)].map((m) => numbers(m[1])[0]);
  assert.deepEqual(values, [80000, 50000, 30000, 28000, 20000, 2000]);
  const [ceiling, issued, called, paid, uncalled, arrears] = values;
  assert.ok(ceiling > issued);
  assert.equal(called + uncalled, issued);
  assert.equal(paid + arrears, called);
});

test('merger examples distinguish stages rather than treating every combination as horizontal', () => {
  const bank = lessons.find((l) => l.lesson_no === 17).questions.find((t) => t.id === 'n4-17-identify').vars.X.pick;
  const byAnswer = Object.fromEntries(bank.map((x) => [x.r, x.q]));
  assert.match(byAnswer['horizontal integration'], /Two fictional bakeries/);
  assert.match(byAnswer['backward vertical integration'], /flour supplier/);
  assert.match(byAnswer['forward vertical integration'], /retail outlets/);
  assert.match(byAnswer['conglomerate integration'], /unrelated furniture/);
});
