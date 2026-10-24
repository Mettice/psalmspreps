import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {instantiate} from '../../../src/engine/template.js';
import {renderLearn} from '../../../src/engine/teach.js';
import {registrySubjects,libOf} from '../../classes.mjs';
const subject=registrySubjects().find(s=>s.id==='l6-english'),lib=await libOf(subject);
const read=n=>JSON.parse(readFileSync(new URL(`../../../content/lower-sixth/english/${n}.json`,import.meta.url)));

test('Lower Sixth English accounts for teaching rows while excluding diagnostics and explicit review',()=>{
 const spine=JSON.parse(readFileSync(new URL('../../../data/spine/lower-sixth/english-language.json',import.meta.url)));
 const expected=spine.terms[0].lessons.filter(r=>r.kind==='lesson'&&!/diagnostic|^Reading Comprehension and Grammar Review$/i.test(r.title)).map(r=>r.seq);
 assert.deepEqual(subject.lessons,expected);assert.equal(expected.length,24);
 for(const n of expected){
  const l=read(n);assert.equal(l.class,'Lower Sixth');assert.equal(l.subject,'english-language');assert.equal(l.questions.length,5);
  assert.ok(!JSON.stringify(l).includes('e5-'));
  for(const p of l.prerequisites)assert.ok(p<n&&expected.includes(p));
  for(const label of ['By the end','Builds on:','Leads to:'])assert.ok(renderLearn(l,lib).pages[0].text.includes(label));
 }
});

test('Foundations explicitly extend earlier work rather than retaining the old class or opening',()=>{
 for(const n of [9,11,17,22,23]){
  const text=renderLearn(read(n),lib).pages.map(p=>p.text).join(' ');
  assert.match(text,/Lower Sixth extension/);
 }
});

test('Written vowel model independently maps selected symbols and discloses oral limits',()=>{
 const t=read(8).questions[2],seen=new Set();
 for(let seed=1;seed<=100;seed++){
  const q=instantiate(t,seed,lib);seen.add(q.prompt);
  const expected=/pair contrasts/.test(q.prompt)?'sheep / ship':/illustrates \/ʊ\//.test(q.prompt)?'put':/sofa/.test(q.prompt)?'/ə/':'bed';
  assert.equal(q.answer,expected,q.prompt);
 }
 assert.equal(seen.size,4);
 const text=renderLearn(read(8),lib).pages.map(p=>p.text).join(' ');
 assert.match(text,/not audio assessment/);assert.match(text,/varieties differ/);assert.match(text,/teacher.*listening/i);
});

test('Independent language expectations cover contextual word roles, scope and edited forms',()=>{
 const keys={
  10:[[/record the decision/,'Functioning as a verb after will'],[/Who|Without further context/,'Who she refers to'],[/seems a verb/,'It heads a predicate expressing a state']],
  12:[[/checked:/,'carefully'],[/under the bench/,'Expresses a location relationship through a prepositional phrase'],[/stated reason/,'because']],
  13:[[/may reduce/,'The trial could make queues shorter.'],[/Only registered/,'Borrowing the folders is restricted to registered members.'],[/delayed the meeting/,'The room’s unavailability caused Bih to postpone the meeting.']],
  14:[[/hour remained/,'An'],[/useful guide/,'a'],[/uncountable pattern/,'some information'],[/Bih read a report/,'The']],
  21:[[/pacific reason/,'Please give a specific reason.'],[/Choose the verb/,'advise'],[/Choose the noun/,'advice'],[/meaning receive/,'accept']],
  24:[[/list of requests/,'is'],[/independent clauses/,'Bih checked the note; Tabe waited.'],[/writer means Ngozi/,'Bih told Ngozi that Ngozi would lead.']],
  25:[[/explanation is/,'clearer'],[/irregular comparative/,'better'],[/displayed proposals/,'most useful'],[/cannot be inferred/,'B is the best text for every reader and purpose']]
 };
 for(const [n,rows] of Object.entries(keys)){
  const seen=new Set();
  for(let seed=1;seed<=100;seed++){
   const q=instantiate(read(n).questions[2],seed,lib),key=rows.find(([p])=>p.test(q.prompt));
   assert.ok(key,q.prompt);assert.equal(q.answer,key[1]);seen.add(q.prompt);
   assert.equal(new Set(q.options.filter(o=>o.text!==q.answer).map(o=>o.explain)).size,3);
  }
  assert.equal(seen.size,rows.length);
 }
});

test('Five writing rows have substantive original models and inspectable paper criteria',()=>{
 assert.deepEqual(subject.lessons.filter(n=>read(n).paper_task),[9,11,15,22,26]);
 for(const n of [9,11,15,22,26]){
  const p=read(n).paper_task;assert.ok(p.prompt.length>80);assert.ok(p.model.join(' ').split(/\s+/).length>=65);assert.ok(p.checklist.length>=4);
 }
 assert.match(renderLearn(read(18),lib).pages.map(p=>p.text).join(' '),/No prescribed play/);
});
