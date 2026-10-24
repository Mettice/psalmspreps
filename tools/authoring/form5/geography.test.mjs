import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {instantiate} from '../../../src/engine/template.js';
import {renderLearn} from '../../../src/engine/teach.js';
import {registrySubjects,libOf} from '../../classes.mjs';
const subject=registrySubjects().find(s=>s.id==='f5-geography');
const lib=await libOf(subject);
const read=n=>JSON.parse(readFileSync(new URL(`../../../content/form-5/geography/${n}.json`,import.meta.url)));
const applied=n=>read(n).questions[3];

test('Geography covers all teaching and map practical rows with connected goals',()=>{
 const spine=JSON.parse(readFileSync(new URL('../../../data/spine/form-5/geography-ok.json',import.meta.url)));
 assert.deepEqual(subject.lessons,spine.terms[0].lessons.filter(r=>['lesson','practical'].includes(r.kind)).map(r=>r.seq));
 assert.equal(subject.lessons.length,23);assert.ok(!subject.lessons.includes(13));
 for(const n of subject.lessons){
  const l=read(n);assert.equal(l.subject,'geography');assert.equal(l.class,'Form 5');assert.equal(l.questions.length,5);
  for(const p of l.prerequisites)assert.ok(p<n&&subject.lessons.includes(p));
  const goal=renderLearn(l,lib).pages[0].text;
  for(const label of ['By the end','Builds on:','Leads to:'])assert.ok(goal.includes(label));
 }
});

test('Weber task independently compares all listed vertices and states its limited scope',()=>{
 const t=applied(5),seen=new Set();
 for(let seed=1;seed<=500;seed++){
  const q=instantiate(t,seed,lib),[a,b,p,d]=[...q.prompt.matchAll(/\b\d+\b/g)].map(m=>Number(m[0]));
  const costs=[[(b+p)*d,'Site A'],[(a+p)*d,'Site B'],[(a+b)*d,'Site M']].sort((a,b)=>a[0]-b[0]);
  assert.equal(q.answer,costs[0][1]);assert.ok(costs[0][0]<costs[1][0]);
  assert.equal(new Set(q.options.map(o=>o.text)).size,4);assert.match(q.figure,/Only A, B, M are candidates/);
  seen.add(q.answer);
 }
 assert.equal(seen.size,3);
});

test('Land-use map chooses exactly the plot satisfying every visible criterion',()=>{
 const seen=new Set();
 for(let seed=1;seed<=100;seed++){
  const q=instantiate(applied(7),seed,lib);
  const plots=[...q.figure.matchAll(/Plot ([A-D])<\/text>.*?Land: ([^<]+)<\/text>.*?Flood: (yes|no)<\/text>.*?Road: (yes|no)<\/text>/g)];
  assert.equal(plots.length,4);const eligible=plots.filter(m=>m[2]==='available'&&m[3]==='no'&&m[4]==='yes');
  assert.equal(eligible.length,1);assert.equal(q.answer,'Plot '+eligible[0][1]);seen.add(q.answer);
  assert.equal(new Set(q.options.filter(o=>o.text!==q.answer).map(o=>o.explain)).size,3);
 }
 assert.equal(seen.size,4);
});

test('Network maps reject closures before independently comparing route distances',()=>{
 const seen=new Set(),closures=new Set();
 for(let seed=1;seed<=160;seed++){
  const q=instantiate(applied(21),seed,lib),get=k=>Number(q.figure.match(new RegExp(k+': (\\d+) km'))[1]);
  const block=q.figure.match(/Closed link: (none|AB|CD)/)[1],routes=[];
  if(block!=='AB')routes.push([get('AB')+get('BD'),'A–B–D']);
  if(block!=='CD')routes.push([get('AC')+get('CD'),'A–C–D']);
  routes.sort((a,b)=>a[0]-b[0]);assert.equal(q.answer,routes[0][1]);
  if(routes.length===2)assert.ok(routes[0][0]<routes[1][0]);
  assert.ok(!/[{}]|NaN|undefined/.test(q.figure));seen.add(q.figure);closures.add(block);
 }
 assert.equal(seen.size,6);assert.equal(closures.size,3);
});

test('Transport and trade arithmetic independently preserves units and measures',()=>{
 for(const n of [9,10,11,22,24]){
  const seen=new Set();
  for(let seed=1;seed<=100;seed++){
   const q=instantiate(applied(n),seed,lib),v=[...q.prompt.replace(/[\u00a0\u202f]/g,'').matchAll(/\b\d+\b/g)].map(m=>Number(m[0]));
   const expected=n===9?v[0]/v[1]*60:n===10?v[0]*v[1]:n===11?v[0]-v[1]:n===22?v[0]+v[1]:v[0]/v[1]*100;
   assert.equal(Number(q.answer),expected,q.prompt);seen.add(q.prompt);
  }
  assert.ok(seen.size>=3);
 }
});
