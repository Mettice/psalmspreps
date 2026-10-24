import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {instantiate} from '../../../src/engine/template.js';
import {renderLearn} from '../../../src/engine/teach.js';
import {registrySubjects,libOf} from '../../classes.mjs';
const subject=registrySubjects().find(s=>s.id==='f5-history');
const lib=await libOf(subject);
const read=n=>JSON.parse(readFileSync(new URL(`../../../content/form-5/history/${n}.json`,import.meta.url)));
const lessons=subject.lessons.map(read);
const text=n=>renderLearn(read(n),lib).pages.map(p=>p.text||'').join(' ');

test('History covers the teaching spine with earlier dependencies and measurable goals',()=>{
  const spine=JSON.parse(readFileSync(new URL('../../../data/spine/form-5/history.json',import.meta.url)));
  assert.deepEqual(subject.lessons,spine.terms[0].lessons.filter(r=>r.kind==='lesson').map(r=>r.seq));
  assert.equal(lessons.length,17);
  for(const l of lessons){
    assert.equal(l.subject,'history');assert.equal(l.class,'Form 5');assert.equal(l.questions.length,5);
    for(const p of l.prerequisites)assert.ok(p<l.lesson_no&&subject.lessons.includes(p));
    for(const label of ['By the end','Builds on:','Leads to:'])assert.ok(renderLearn(l,lib).pages[0].text.includes(label));
  }
});

const dates=[
 [/Gold Coast election/,1951,1,1],[/becomes prime minister/,1952,1,1],[/Further internal/,1954,1,1],[/Ghana becomes independent/,1957,3,6],
 [/Federal constitutional/,1954,1,1],[/Constitutional conference/,1958,1,1],[/Federal election/,1959,1,1],[/Nigeria becomes independent/,1960,10,1],
 [/Brazzaville/,1944,1,30],[/French Union/,1946,10,27],[/Loi-cadre/,1956,6,23],[/Guinea chooses/,1958,9,28],
 [/Congo becomes independent/,1960,6,30],[/Army mutiny/,1960,7,5],[/Katanga announces/,1960,7,11],[/establishes ONUC/,1960,7,14],
 [/Guinea-Bissau declares/,1973,9,24],[/Portugal’s April revolution/,1974,4,25],[/Portugal recognises/,1974,9,10],[/Mozambique becomes independent/,1975,6,25],
 [/Expansion of the US/,1920,1,1],[/US stock-market crash/,1929,10,1],[/US banking panics/,1930,11,1],[/Roosevelt’s banking holiday/,1933,3,1],
 [/Cameroon admitted/,1960,9,20],[/Cameroon among OAU/,1963,5,25],[/European Union established/,1993,11,1],[/African Union launched/,2002,7,9]
];
test('seven chronology exercises preserve independent event dates and within-month sequence',()=>{
  const templates=lessons.flatMap(l=>l.questions).filter(q=>q.type==='ordering');assert.equal(templates.length,7);
  for(const t of templates){
    const variants=new Set();
    for(let seed=1;seed<=160;seed++){
      const q=instantiate(t,seed,lib),ordered=q.correctOrder.map(i=>q.items[i]);variants.add(JSON.stringify(ordered));
      const keys=ordered.map(s=>{
        const r=dates.find(([pattern])=>pattern.test(s));assert.ok(r,s);
        assert.equal(Number(s.match(/(?:19|20)\d\d/)[0]),r[1],s);
        return r[1]*400+r[2]*31+r[3];
      });
      assert.deepEqual(keys,[...keys].sort((a,b)=>a-b),q.prompt);
    }
    assert.equal(variants.size,4,t.id);
  }
});

test('source tasks disclose invented provenance and offer distinct wrong-claim feedback',()=>{
  for(const l of lessons){
    const t=l.questions.find(q=>q.id.endsWith('-source')),seen=new Set();
    for(let seed=1;seed<=100;seed++){
      const q=instantiate(t,seed,lib);seen.add(q.prompt);
      assert.match(q.prompt,/^Invented classroom source/);assert.match(q.prompt,/not an archive quotation/);assert.match(q.prompt,/authentic evidence/);
      assert.equal(new Set(q.options.filter((o,i)=>i!==q.correctIndex).map(o=>o.explain)).size,3);
    }
    assert.equal(seen.size,4);
  }
});

test('constitutional status, recognition and membership distinctions survive rendering',()=>{
  assert.match(text(1),/6 March 1957/);assert.match(text(2),/1 October 1960/);
  assert.match(text(3),/did not grant immediate independence|not immediate independence/);
  assert.match(text(6),/declared independence in 1973.*recognition in 1974/);
  assert.match(text(13),/Democratic Republic of the Congo is not a CEMAC member/);
  assert.match(text(15),/not an EU member/);
  assert.match(text(16),/not a member of the League of Arab States/);
  assert.doesNotMatch(JSON.stringify(read(16).questions),/1975|1991/);
  assert.match(text(17),/Soviet Union began in 1964/);assert.match(text(17),/successor in 1992/);
});
