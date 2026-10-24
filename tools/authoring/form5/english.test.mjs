import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { instantiate } from '../../../src/engine/template.js';
import { registrySubjects, libOf } from '../../classes.mjs';

const subject = registrySubjects().find(s => s.id === 'f5-english');
const lib = await libOf(subject);
const read = n => JSON.parse(readFileSync(new URL(`../../../content/form-5/english/${n}.json`, import.meta.url)));
const template = (n, id) => read(n).questions.find(q => q.id === id);

test('Form Five English accounts for teaching rows and preserves writing and oral limits', () => {
  const spine = JSON.parse(readFileSync(new URL('../../../data/spine/form-5/english-language.json', import.meta.url)));
  assert.deepEqual(subject.lessons, spine.terms[0].lessons.filter(r => r.kind === 'lesson').map(r => r.seq));
  for (const n of subject.lessons) {
    const l = read(n);
    for (const p of l.prerequisites) assert.ok(p < n && subject.lessons.includes(p));
  }
  for (const n of [6,7,10,13,15,16,20,26,27,32]) assert.ok(read(n).paper_task, `Missing writing task ${n}`);
  for (const n of [5,18,30]) assert.match(JSON.stringify(read(n).learn), /written script|written preparation/);
  assert.match(JSON.stringify(read(12).learn), /do not assess hearing/);
});

test('tense forms match independently specified complete groups', () => {
  const forms = { write:['writes','wrote','writing','written'], take:['takes','took','taking','taken'], choose:['chooses','chose','choosing','chosen'], speak:['speaks','spoke','speaking','spoken'] };
  const seen = new Set();
  for (let seed=1; seed<=400; seed++) {
    const q = instantiate(template(4,'e5-4-forms'),seed,lib);
    const [,target,subject,verb] = q.prompt.match(/form: (.*?), with (.*?) and (\w+)\./);
    const [sing,past,ing,pp] = forms[verb];
    const expected = target==='simple present' ? sing : target==='simple past' ? past : target==='present progressive' ? (subject==='Bih'?'is':subject==='I'?'am':'are')+' '+ing : (subject==='Bih'?'has':'have')+' '+pp;
    assert.equal(q.answer,expected,q.prompt);
    assert.equal(new Set(q.options.map(o=>o.text)).size,4,q.prompt);
    seen.add(target);
  }
  assert.equal(seen.size,4);
});

test('concord follows subject nucleus and coordination, not intervening plural nouns', () => {
  const seen = new Set();
  for (let seed=1; seed<=200; seed++) {
    const q = instantiate(template(31,'e5-31-concord'),seed,lib);
    const verb=q.prompt.match(/Verb: (\w+)/)[1];
    const singular=q.prompt.includes('The chair of') || q.prompt.includes('Each of');
    const expected=singular ? ({write:'writes',check:'checks',prepare:'prepares',organise:'organises'})[verb] : verb;
    assert.equal(q.answer,expected,q.prompt);
    assert.equal(new Set(q.options.map(o=>o.text)).size,4,q.prompt);
    seen.add(q.prompt.split(' ___')[0]);
  }
  assert.equal(seen.size,4);
});

test('reporting keeps the optional-backshift distinction and consonants preserve word pairs', () => {
  const pairs={'pin and bin':'/p/ and /b/','tie and die':'/t/ and /d/','fan and van':'/f/ and /v/','sip and zip':'/s/ and /z/'};
  let optional=false;
  for(let seed=1;seed<=100;seed++) {
    const q=instantiate(template(12,'e5-12-apply'),seed,lib);
    const words=q.prompt.match(/distinguishes (.*?)\?/)[1];
    assert.equal(q.answer,pairs[words]);
    const report=instantiate(template(21,'e5-21-apply'),seed,lib);
    if(report.prompt.includes('Which claim')) {
      assert.match(report.answer,/unnecessary.*still true or relevant/);
      optional=true;
    }
  }
  assert.ok(optional);
});
