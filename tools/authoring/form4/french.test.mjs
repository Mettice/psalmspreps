import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { instantiate } from '../../../src/engine/template.js';
import { renderLearn } from '../../../src/engine/teach.js';
import { registrySubjects, libOf } from '../../classes.mjs';

const subject=registrySubjects().find((s)=>s.id==='f4-french');
const lib=await libOf(subject);
const read=(p)=>JSON.parse(readFileSync(new URL(p,import.meta.url)));
const lessons=subject.lessons.map((n)=>read(`../../../content/form-4/french/${n}.json`));
const template=(id)=>lessons.flatMap((l)=>l.questions).find((q)=>q.id===id);
const pronouns=['je','tu','il','elle','nous','vous','ils','elles'];
const person=[0,1,2,2,3,4,5,5];
const full=(p,form)=>p==='je'&&/^[aeiouéè]/.test(form)?'j’'+form:p+' '+form;

test('French covers the thirty teaching rows, with translated goals, earlier dependencies and writing models',()=>{
  const spine=read('../../../data/spine/form-4/french.json');
  assert.deepEqual(subject.lessons,spine.terms[0].lessons.filter((r)=>r.kind==='lesson').map((r)=>r.seq));
  assert.equal(lessons.length,30);
  for(const l of lessons){
    assert.equal(l.language,'fr');
    assert.equal(l.questions.length,5);
    assert.equal(l.teach.cards.length,3);
    const first=renderLearn(l,lib).pages[0];
    assert.equal(first.heading,'Ton objectif et les liens');
    for(const s of ['À la fin','Acquis mobilisés :','Pour la suite :']) assert.ok(first.text.includes(s));
    for(const n of l.prerequisites) assert.ok(n<l.lesson_no&&subject.lessons.includes(n));
  }
  assert.deepEqual(lessons.filter((l)=>l.paper_task).map((l)=>l.lesson_no),[9,31]);
});

const simple={
  6:{parler:['parlai','parlas','parla','parlâmes','parlâtes','parlèrent'],aider:['aidai','aidas','aida','aidâmes','aidâtes','aidèrent'],finir:['finis','finis','finit','finîmes','finîtes','finirent'],choisir:['choisis','choisis','choisit','choisîmes','choisîtes','choisirent']},
  15:{aider:['aidais','aidais','aidait','aidions','aidiez','aidaient'],finir:['finissais','finissais','finissait','finissions','finissiez','finissaient'],manger:['mangeais','mangeais','mangeait','mangions','mangiez','mangeaient'],être:['étais','étais','était','étions','étiez','étaient']},
  22:{être:['sois','sois','soit','soyons','soyez','soient'],avoir:['aie','aies','ait','ayons','ayez','aient'],faire:['fasse','fasses','fasse','fassions','fassiez','fassent'],aller:['aille','ailles','aille','allions','alliez','aillent'],finir:['finisse','finisses','finisse','finissions','finissiez','finissent'],choisir:['choisisse','choisisses','choisisse','choisissions','choisissiez','choisissent']},
};
test('displayed tense and subject determine conjugation, including accents, elision and auxiliary agreement',()=>{
  for(const n of [6,10,15,22]){
    const seen=new Set();
    for(let seed=1;seed<=600;seed++){
      const q=instantiate(template(`fr4-${n}-conjuguer`),seed,lib);
      const tokens=[...q.prompt.matchAll(/« ([^»]+) »/g)].map((m)=>m[1]);
      const [v,p]=n===22?[tokens[2],tokens[1]]:tokens;
      const pi=pronouns.indexOf(p),k=person[pi];
      assert.ok(pi>=0,q.prompt);
      let expected;
      if(n===10){
        const moving=['arriver','partir'].includes(v);
        const aux=(moving?['suis','es','est','sommes','êtes','sont']:['ai','as','a','avons','avez','ont'])[k];
        const pp={aider:'aidé',finir:'fini',arriver:'arrivé',partir:'parti'}[v]+(moving&&[3,7].includes(pi)?'e':'')+(moving&&pi>=4?'s':'');
        expected=full(p,aux+' '+pp);
      }else{
        expected=full(p,simple[n][v][k]);
        if(n===22) expected=(/^[aeiouéè]/.test(expected)?'qu’':'que ')+expected;
      }
      assert.equal(q.answer,expected,q.prompt);
      assert.equal(new Set(q.options.map((o)=>o.text)).size,4);
      seen.add(v+':'+p);
    }
    assert.ok(seen.size>=24,`${n}: insufficient tense/person coverage`);
  }
});

test('imperatives, weather spelling and nominal subjects use the requested person',()=>{
  const imperative={parler:['parle','parlons','parlez'],finir:['finis','finissons','finissez'],être:['sois','soyons','soyez'],avoir:['aie','ayons','ayez']};
  const present={arriver:['arrive','arrivent'],finir:['finit','finissent'],travailler:['travaille','travaillent'],choisir:['choisit','choisissent']};
  const weather=new Set();
  for(let seed=1;seed<=160;seed++){
    const q=instantiate(template('fr4-29-conjuguer'),seed,lib);
    const [v,p]=[...q.prompt.matchAll(/« ([^»]+) »/g)].map((m)=>m[1]);
    assert.equal(q.answer,imperative[v][['tu','nous','vous'].indexOf(p)]);
    const a=instantiate(template('fr4-30-accord'),seed,lib);
    const verb=Object.keys(present).find((v)=>a.prompt.includes(v));
    const plural=a.prompt.includes('Les élèves du groupe')||a.prompt.includes('Bih et Ayuk');
    assert.equal(a.answer,present[verb][Number(plural)],a.prompt);
    const w=instantiate(template('fr4-18-forme'),seed,lib);
    const inf=w.prompt.match(/« ([^»]+) »/)[1];
    assert.equal(w.answer,{neiger:'il neige',venter:'il vente',tonner:'il tonne',geler:'il gèle'}[inf]);
    weather.add(inf);
  }
  assert.equal(weather.size,4);
});

test('liaison answers distinguish actual sound boundaries and images retain four real visual variants',()=>{
  const liaison={'les amis':'liaison [z]','un ami':'liaison [n]','un petit ami':'liaison [t]','et elle':'aucune liaison à cet endroit','les héros':'aucune liaison à cet endroit'};
  const seen=new Set(),images=new Set();
  for(let seed=1;seed<=150;seed++){
    const q=instantiate(template('fr4-12-liaison'),seed,lib);
    const group=q.prompt.match(/« ([^»]+) »/)[1];
    assert.equal(q.answer,liaison[group]);
    const wrong=q.options.filter((o)=>o.text!==q.answer);
    assert.equal(new Set(wrong.map((o)=>o.explain)).size,3);
    seen.add(group);
    const img=instantiate(template('fr4-4-image'),seed,lib);
    assert.match(img.figure,/Scène scolaire inventée/);
    assert.match(img.figure,/sans enregistrement sonore/);
    images.add(img.figure);
  }
  assert.equal(seen.size,5);
  assert.equal(images.size,4);
});
