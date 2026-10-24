import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { instantiate } from '../../../src/engine/template.js';
import { registrySubjects, libOf } from '../../classes.mjs';

const subject=registrySubjects().find(s=>s.id==='f5-logic');
const lib=await libOf(subject);
const read=n=>JSON.parse(readFileSync(new URL(`../../../content/form-5/logic/${n}.json`,import.meta.url)));
const tpl=(n,id)=>read(n).questions.find(q=>q.id===id);

test('Logic includes the screen-based guided work and orders dependencies',()=>{
  const spine=JSON.parse(readFileSync(new URL('../../../data/spine/form-5/logic.json',import.meta.url)));
  assert.deepEqual(subject.lessons,spine.terms[0].lessons.filter(r=>['lesson','guided_work'].includes(r.kind)).map(r=>r.seq));
  for(const n of subject.lessons) for(const p of read(n).prerequisites) assert.ok(p<n && subject.lessons.includes(p));
  for(const n of [4,5,6]) assert.match(JSON.stringify(read(n).learn),/exist|nonempty/);
});

test('counted models determine each form including mixed and empty classes',()=>{
  const seen=new Set();
  for(const n of [5,6]) for(let seed=1;seed<=600;seed++) {
    const q=instantiate(tpl(n,`l5-${n}-model`),seed,lib);
    const [,a,b,code]=q.prompt.match(/model: (\d+) S are inside P and (\d+) S are outside P\. There are no other S\. Assess ([AEIO])/);
    const objects=[...Array(+a).fill(true),...Array(+b).fill(false)];
    const value={A:objects.every(Boolean),E:objects.every(x=>!x),I:objects.some(Boolean),O:objects.some(x=>!x)}[code];
    assert.equal(q.answer,value?'True in this model.':'False in this model.',q.prompt);
    seen.add(code+':'+(objects.length===0?'empty':+a>0 && +b>0?'mixed':'uniform'));
  }
  for(const c of 'AEIO') {assert.ok(seen.has(c+':empty'));assert.ok(seen.has(c+':mixed'));}
});

function parseClaim(text) {
  const m=text.match(/(All|No|Some) (.+?) are (not )?(.+?)\.$/);
  assert.ok(m,text);
  return {quant:m[1],s:m[2],negative:!!m[3],p:m[4]};
}
function holds(claim,world) {
  function member(term,i) {
    if(term.startsWith('non-(') && term.endsWith(')')) return !member(term.slice(5,-1),i);
    assert.ok(Object.hasOwn(world,term),term);
    return world[term].has(i);
  }
  const S=[0,1,2].filter(i=>member(claim.s,i));
  const P=i=>claim.negative ? !member(claim.p,i) : member(claim.p,i);
  return claim.quant==='All'?S.every(P):claim.quant==='No'?S.every(i=>!P(i)):S.some(P);
}

test('converses, obverses and contrapositives are equivalent across exhaustive finite interpretations',()=>{
  for(const n of [7,8,9]) for(let seed=1;seed<=100;seed++) {
    const q=instantiate(tpl(n,`l5-${n}-apply`),seed,lib);
    const original=parseClaim(q.prompt),answer=parseClaim(q.answer);
    for(let mask=0;mask<64;mask++) {
      const world={
        [original.s]:new Set([0,1,2].filter(i=>mask & (1<<i))),
        [original.p]:new Set([0,1,2].filter(i=>mask & (1<<(i+3))))
      };
      assert.equal(holds(original,world),holds(answer,world),q.prompt+' => '+q.answer+' in '+mask);
    }
    assert.equal(new Set(q.options.map(o=>o.text)).size,4,q.prompt);
  }
});

test('the full square requires nonempty S and invalid converse has a counterexample',()=>{
  for(let mask=1;mask<64;mask++) {
    const S=new Set([0,1,2].filter(i=>mask & (1<<i)));
    const P=new Set([0,1,2].filter(i=>mask & (1<<(i+3))));
    const world={S,P};
    const A=holds(parseClaim('All S are P.'),world),E=holds(parseClaim('No S are P.'),world),I=holds(parseClaim('Some S are P.'),world),O=holds(parseClaim('Some S are not P.'),world);
    assert.notEqual(A,O);assert.notEqual(E,I);
    if(S.size) { assert.ok(!(A&&E));assert.ok(I||O);assert.ok(!A||I);assert.ok(!E||O); }
  }
  const world={S:new Set([0]),P:new Set([0,1])};
  assert.equal(holds(parseClaim('All S are P.'),world),true);
  assert.equal(holds(parseClaim('All P are S.'),world),false);
});
