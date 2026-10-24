import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {instantiate} from '../../../src/engine/template.js';
import {renderLearn} from '../../../src/engine/teach.js';
import {registrySubjects,libOf} from '../../classes.mjs';
const subject=registrySubjects().find(s=>s.id==='f5-economics');
const lib=await libOf(subject);
const read=n=>JSON.parse(readFileSync(new URL(`../../../content/form-5/economics/${n}.json`,import.meta.url)));
const lessons=subject.lessons.map(read);
const numbers=s=>(s.replace(/[\u00a0\u202f]/g,'').match(/[−-]?\d+(?:\.\d+)?/g)||[]).map(s=>Number(s.replace('−','-')));

test('Economics covers teaching and practical rows with explicit model limits',()=>{
  const spine=JSON.parse(readFileSync(new URL('../../../data/spine/form-5/economics.json',import.meta.url)));
  assert.deepEqual(subject.lessons,spine.terms[0].lessons.filter(r=>['lesson','practical','guided_work'].includes(r.kind)).map(r=>r.seq));
  for(const l of lessons) for(const p of l.prerequisites) assert.ok(p<l.lesson_no && subject.lessons.includes(p));
  assert.match(JSON.stringify(read(14).learn),/not a mechanical description or prediction/);
  assert.match(JSON.stringify(read(15).learn),/not.*regulation|not.*regulatory/);
  assert.match(JSON.stringify(read(17).learn),/current reserve|current parameter/);
});

const answers={
  'n5-3-stock':([currency,deposits])=>currency+deposits,
  'n5-4-power':([base,now,indexBase])=>indexBase/(now/base),
  'n5-5-basket':([notebooks,oldN,newN,folders,oldF,newF])=>notebooks*newN+folders*newF,
  'n5-6-rate':([old,now])=>(now/old-1)*100,
  'n5-10-transfer':([a,b])=>a+b,
  'n5-12-equity':([reserves,loans,securities,deposits])=>reserves+loans+securities-deposits,
  'n5-13-loan-entry':([loans,newLoan])=>loans+newLoan,
  'n5-14-total':([initial,percent,base])=>initial/(percent/base),
  'n5-15-rounds':([initial,percent])=>{
    let incoming=initial,total=0;
    for(let i=0;i<3;i++){total+=incoming;incoming*=1-percent/100;}
    return total;
  },
  'n5-19-balance':([tax,nonTax,spending])=>tax+nonTax-spending
};
test('all numerical answers use the data and reference bases actually displayed',()=>{
  const templates=lessons.flatMap(l=>l.questions).filter(q=>q.type==='numeric');
  assert.deepEqual(templates.map(t=>t.id).sort(),Object.keys(answers).sort());
  let deficit=false,surplus=false;
  for(const t of templates) for(let seed=1;seed<=200;seed++) {
    const q=instantiate(t,seed,lib);
    const expected=answers[t.id](numbers(q.prompt));
    assert.ok(Number.isFinite(expected),q.prompt);
    assert.ok(Math.abs(q.answerValue-expected)<1e-7,`${t.id}: ${q.prompt}: ${q.answerValue} != ${expected}`);
    if(t.id==='n5-19-balance'){deficit ||= expected<0;surplus ||= expected>0;}
  }
  assert.ok(deficit && surplus);
});

test('rendered basket, balance sheet and finite-round records reconcile independently',()=>{
  const table=n=>{
    const svg=renderLearn(read(n),lib).pages.find(p=>p.figure).figure;
    return [...svg.matchAll(/text-anchor="end">([^<]+)<\/text>/g)].map(m=>numbers(m[1])[0]);
  };
  const basket=table(5);
  assert.deepEqual(basket,[400,600,1000,500,650,1150]);
  assert.equal(basket[0]+basket[1],basket[2]);assert.equal(basket[3]+basket[4],basket[5]);
  const [reserves,loans,securities,assets,deposits,equity,right]=table(12);
  assert.equal(reserves+loans+securities,assets);assert.equal(deposits+equity,right);assert.equal(assets,right);
  const [a,heldA,b,heldB,c,total]=table(15);
  assert.equal(a-heldA,b);assert.equal(b-heldB,c);assert.equal(a+b+c,total);
  assert.ok(total<50000);
});

test('model deposit limit agrees with a long finite sequence while excluding initial funds from extra credit',()=>{
  const t=read(14).questions.find(q=>q.id==='n5-14-total');
  for(let seed=1;seed<=100;seed++) {
    const q=instantiate(t,seed,lib);const [initial,percent,base]=numbers(q.prompt);
    let incoming=initial,total=0;
    for(let step=0;step<400;step++){total+=incoming;incoming*=1-percent/base;}
    assert.ok(Math.abs(total-q.answerValue)<1e-6);
    assert.ok(total-initial<total);
  }
});
