import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { instantiate, check } from '../../../src/engine/template.js';
import { renderLearn } from '../../../src/engine/teach.js';
import { registrySubjects, libOf } from '../../classes.mjs';

const subject=registrySubjects().find((s)=>s.id==='f4-geography');
const lib=await libOf(subject);
const read=(p)=>JSON.parse(readFileSync(new URL(p,import.meta.url)));
const lessons=subject.lessons.map((n)=>read(`../../../content/form-4/geography/${n}.json`));
const template=(id)=>lessons.flatMap((l)=>l.questions).find((t)=>t.id===id);
const numbers=(s)=>(s.replace(/[\u00a0\u202f]/g,'').match(/\d+(?:\.\d+)?/g)||[]).map(Number);

test('all nineteen Geography rows have goals, earlier dependencies and the full lesson format',()=>{
  const spine=read('../../../data/spine/form-4/geography-ok.json');
  assert.deepEqual(subject.lessons,spine.terms[0].lessons.filter((r)=>r.kind==='lesson').map((r)=>r.seq));
  assert.equal(lessons.length,19);
  for(const l of lessons){
    assert.equal(l.questions.length,5);
    assert.equal(l.teach.cards.length,3);
    const first=renderLearn(l,lib).pages[0];
    for(const label of ['By the end','Builds on:','Leads to:']) assert.ok(first.text.includes(label));
    for(const n of l.prerequisites) assert.ok(subject.lessons.includes(n)&&n<l.lesson_no);
  }
});

const oracle={
  'g4-1-air':([whole,mineral,organic,water])=>whole-mineral-organic-water,
  'g4-2-clay':([whole,sand,silt])=>whole-sand-silt,
  'g4-4-loss':([bare,covered])=>bare-covered,
  'g4-7-transfer':([input,percent])=>input*percent/100,
  'g4-10-water-store':([start,rain,use,drain])=>start+rain-use-drain,
  'g4-15-relative-height':([high,low])=>high-low,
  'g4-17-rain-contrast':([coast,north])=>coast-north,
};
test('numeric answers agree with displayed measurements and conditional wrong answers remain wrong',()=>{
  for(const [id,expected] of Object.entries(oracle)){
    for(let seed=1;seed<=180;seed++){
      const q=instantiate(template(id),seed,lib);
      assert.ok(Math.abs(q.answerValue-expected(numbers(q.prompt)))<1e-8,q.prompt);
      assert.ok(q.answerValue>=0,id);
      for(const m of q.misconceptions) assert.equal(check(q,String(m.value)).correct,false,`${id}: ${m.value}`);
    }
  }
});

test('rainfall totals use the twelve visible bars and their drawn heights match their labels',()=>{
  for(const n of [8,9,11,12,13]){
    const seen=new Set();
    for(let seed=1;seed<=80;seed++){
      const q=instantiate(template(`g4-${n}-rain-total`),seed,lib);
      const bars=[...q.figure.matchAll(/width="16" height="([\d.]+)" fill="#448d98"\/><text[^>]*>(\d+)<\/text>/g)];
      assert.equal(bars.length,12);
      const values=bars.map((b)=>Number(b[2]));
      assert.equal(q.answerValue,values.reduce((a,b)=>a+b,0));
      for(const b of bars) assert.ok(Math.abs(Number(b[1])-Number(b[2])*0.44)<1e-7);
      assert.match(q.figure,/model data, not a town record/);
      seen.add(values.join(','));
    }
    assert.equal(seen.size,4);
  }
});

test('erosion choice is the steepest exposed plot actually shown, with four distinct map scenarios',()=>{
  const seen=new Set();
  for(let seed=1;seed<=120;seed++){
    const q=instantiate(template('g4-5-map-decision'),seed,lib);
    const plots=[...q.figure.matchAll(/Plot ([A-D])<\/text><text[^>]*>Slope: (\d+)°<\/text><text[^>]*>Cover: (\w+)<\/text>/g)];
    assert.equal(plots.length,4);
    const exposed=plots.filter((p)=>p[3]==='bare').sort((a,b)=>Number(b[2])-Number(a[2]));
    assert.equal(q.answer.match(/^Plot ([A-D])/)[1],exposed[0][1]);
    assert.equal(q.options.length,4);
    seen.add(plots.map((p)=>p.slice(1).join(':')).join('|'));
  }
  assert.equal(seen.size,4);
});

test('diagram and coordinate answers preserve soil layers, grid conventions and river connections',()=>{
  const profile=renderLearn(lessons.find((l)=>l.lesson_no===3),lib).pages.find((p)=>p.figure).figure;
  assert.match(profile,/O, A, B, C, R from surface downward/);
  assert.match(profile,/E may occur/);
  const systems={Sanaga:'Atlantic Ocean',Benue:'Niger → Atlantic',Dja:'Congo → Atlantic',Logone:'Lake Chad basin'};
  for(let seed=1;seed<=120;seed++){
    const q=instantiate(template('g4-16-basin-map'),seed,lib);
    const river=q.prompt.match(/the (Sanaga|Benue|Dja|Logone) system/)[1];
    assert.equal(q.answer,systems[river]);
    assert.match(q.figure,/Schematic, not a river course map/);
    const p=instantiate(template('g4-14-coordinate'),seed,lib);
    const coords=p.answer.match(/(\d+)°N, (\d+)°E/);
    assert.ok(coords,p.answer);
    assert.ok([4,6,8].includes(Number(coords[1])));
    assert.ok([10,12,14].includes(Number(coords[2])));
    const grid=instantiate(template('g4-6-habitat-grid'),seed,lib);
    const x=Number(grid.figure.match(/<circle cx="([\d.]+)"/)[1]);
    const y=Number(grid.figure.match(/<circle[^>]*cy="([\d.]+)"/)[1]);
    const e=20+Math.floor((x-34)/56), north=60+Math.floor(5-(y-12)/56);
    assert.equal(grid.answer,String(e)+String(north));
  }
});
