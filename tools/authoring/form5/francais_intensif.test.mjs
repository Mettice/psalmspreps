import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {instantiate} from '../../../src/engine/template.js';
import {renderLearn} from '../../../src/engine/teach.js';
import {registrySubjects,libOf} from '../../classes.mjs';
const subject=registrySubjects().find(s=>s.id==='f5-francais-intensif');
const lib=await libOf(subject);
const read=n=>JSON.parse(readFileSync(new URL(`../../../content/form-5/francais-intensif/${n}.json`,import.meta.url)));
const tpl=(n,id)=>read(n).questions.find(q=>q.id===id);
const active=subject.lessons.filter(n=>read(n).status!=='deferred');
const pronouns=['je','tu','il','elle','nous','vous','ils','elles'],persons=[0,1,2,2,3,4,5,5];
const full=(p,form)=>p==='je'&&/^[aeiouéè]/.test(form)?'j’'+form:p+' '+form;
const tokens=q=>[...q.prompt.matchAll(/« ([^»]+) »/g)].map(m=>m[1]);

test('thirty language drafts and twenty prescribed-book deferrals account for the teaching spine',()=>{
  const spine=JSON.parse(readFileSync(new URL('../../../data/spine/form-5/francais-intensif.json',import.meta.url)));
  const rows=spine.terms[0].lessons.filter(r=>r.kind==='lesson');
  const deferred=rows.filter(r=>read(r.seq).status==='deferred');
  assert.equal(active.length,30);assert.equal(deferred.length,20);
  assert.deepEqual(active,rows.filter(r=>read(r.seq).status!=='deferred').map(r=>r.seq));
  for(const r of deferred){assert.match(r.title,/œuvres/);assert.match(read(r.seq).deferred_reason,/retour enseignant/);assert.ok(!read(r.seq).questions);}
  assert.deepEqual(active.filter(n=>read(n).paper_task),[15,24,43,51]);
  for(const n of active){
    const l=read(n);assert.equal(l.subject,'francais-intensif');assert.equal(l.class,'Form 5');assert.equal(l.language,'fr');
    for(const p of l.prerequisites)assert.ok(p<n&&active.includes(p));
    for(const page of renderLearn(l,lib).pages)if(page.figure)assert.doesNotMatch(page.figure,/u00/);
  }
});

test('gerunds and irregular noun plurals match independent lexical references',()=>{
  const participles={avoir:'ayant',être:'étant',faire:'faisant',finir:'finissant',parler:'parlant',manger:'mangeant'};
  const plurals={cheval:'chevaux',travail:'travaux',genou:'genoux',pneu:'pneus',festival:'festivals'};
  const seen=new Set();
  for(let seed=1;seed<=220;seed++){
    const g=instantiate(tpl(7,'fi5-7-former'),seed,lib),v=tokens(g)[0];
    assert.equal(g.answer,(g.prompt.includes('gérondif')?'en ':'')+participles[v],g.prompt);
    const p=instantiate(tpl(36,'fi5-36-pluriel'),seed,lib),noun=tokens(p)[0];
    assert.equal(p.answer,plurals[noun]);seen.add(noun);
  }
  assert.equal(seen.size,5);
});

test('simple and compound past forms preserve the requested person and structure',()=>{
  const ps={aider:['aidai','aidas','aida','aidâmes','aidâtes','aidèrent'],parler:['parlai','parlas','parla','parlâmes','parlâtes','parlèrent'],finir:['finis','finis','finit','finîmes','finîtes','finirent'],choisir:['choisis','choisis','choisit','choisîmes','choisîtes','choisirent']};
  const pp={aider:'aidé',parler:'parlé',finir:'fini',choisir:'choisi'},aux=['ai','as','a','avons','avez','ont'];
  const seen=new Set();
  for(let seed=1;seed<=650;seed++){
    const q=instantiate(tpl(19,'fi5-19-formes'),seed,lib),[v,p]=tokens(q),k=persons[pronouns.indexOf(p)];
    assert.equal(q.answer,full(p,q.prompt.includes('passé simple')?ps[v][k]:aux[k]+' '+pp[v]),q.prompt);
    assert.equal(new Set(q.options.map(o=>o.text)).size,4);
    seen.add(v+':'+p+':'+q.prompt.includes('passé simple'));
  }
  assert.ok(seen.size>=60);
});

test('future and conditional use independently checked stems and endings',()=>{
  const stems={aller:'ir',faire:'fer',venir:'viendr',avoir:'aur',choisir:'choisir',envoyer:'enverr'};
  const fut=['ai','as','a','ons','ez','ont'],cond=['ais','ais','ait','ions','iez','aient'];
  const seen=new Set();
  for(let seed=1;seed<=750;seed++){
    const q=instantiate(tpl(31,'fi5-31-formes'),seed,lib),[v,p]=tokens(q),k=persons[pronouns.indexOf(p)];
    const future=q.prompt.includes('futur simple');
    assert.equal(q.answer,full(p,stems[v]+(future?fut:cond)[k]),q.prompt);
    assert.equal(new Set(q.options.map(o=>o.text)).size,4);
    seen.add(v+':'+p+':'+future);
  }
  assert.ok(seen.size>=90);
});

test('writing figures are fictional and distinct; oral homophone grouping is qualified',()=>{
  const figures=[15,43,51].map(n=>renderLearn(read(n),lib).pages.find(p=>p.figure).figure);
  assert.equal(new Set(figures).size,3);
  assert.match(figures[0],/Support familial inventé/);assert.match(figures[1],/sans échelle/);assert.match(figures[2],/Dessin pédagogique inventé/);
  assert.match(JSON.stringify(read(2).learn),/c de donc peut s’entendre/);
  assert.match(JSON.stringify(read(45).learn),/ne prouve pas à lui seul plusieurs événements/);
});
