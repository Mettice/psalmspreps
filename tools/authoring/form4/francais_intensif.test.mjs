import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { instantiate } from '../../../src/engine/template.js';
import { renderLearn } from '../../../src/engine/teach.js';
import { registrySubjects,libOf } from '../../classes.mjs';

const subject=registrySubjects().find((s)=>s.id==='f4-francais-intensif');
const lib=await libOf(subject);
const read=(p)=>JSON.parse(readFileSync(new URL(p,import.meta.url)));
const rows=read('../../../data/spine/form-4/francais-intensif.json').terms[0].lessons;
const files=rows.filter((r)=>r.kind==='lesson').map((r)=>read(`../../../content/form-4/francais-intensif/${r.seq}.json`));
const active=files.filter((l)=>l.status!=='deferred');
const tpl=(id)=>active.flatMap((l)=>l.questions).find((q)=>q.id===id);

test('all language rows have goals and earlier dependencies; prescribed literature remains explicitly pending',()=>{
  assert.equal(active.length,30);
  assert.equal(files.filter((l)=>l.status==='deferred').length,20);
  for(const r of rows.filter((r)=>r.kind==='lesson')){
    const l=files.find((f)=>f.lesson_no===r.seq);
    assert.equal(l.language,'fr');
    if(r.title.includes('littérature')){
      assert.equal(l.status,'deferred');
      assert.match(l.deferred_reason,/titre, auteur et édition/);
    }else{
      assert.equal(l.questions.length,5);
      const page=renderLearn(l,lib).pages[0];
      for(const s of ['À la fin','Acquis mobilisés :','Pour la suite :']) assert.ok(page.text.includes(s));
      for(const p of l.prerequisites) assert.ok(p<l.lesson_no&&active.some((x)=>x.lesson_no===p));
    }
  }
  assert.deepEqual(active.filter((l)=>l.paper_task).map((l)=>l.lesson_no),[9,17,23,30,34,51]);
});

test('conditional endings and compound-past auxiliaries match the actual displayed subjects',()=>{
  const pron=['je','tu','il','elle','nous','vous','ils','elles'],k=[0,1,2,2,3,4,5,5];
  const withPron=(p,s)=>p==='je'&&/^[aeiouéè]/.test(s)?'j’'+s:p+' '+s;
  const stem={aider:'aider',finir:'finir',être:'ser',avoir:'aur',aller:'ir',faire:'fer'};
  const seen=new Set();
  for(let seed=1;seed<=600;seed++){
    const c=instantiate(tpl('fi4-20-conjuguer'),seed,lib);
    const [v,p]=[...c.prompt.matchAll(/« ([^»]+) »/g)].map((m)=>m[1]);
    assert.equal(c.answer,withPron(p,stem[v]+['ais','ais','ait','ions','iez','aient'][k[pron.indexOf(p)]]));
    seen.add(v+':'+p);
    const q=instantiate(tpl('fi4-6-conjuguer'),seed,lib);
    const [verb,subject]=[...q.prompt.matchAll(/« ([^»]+) »/g)].map((m)=>m[1]);
    const pi=pron.indexOf(subject),moving=['arriver','partir'].includes(verb);
    const aux=(moving?['suis','es','est','sommes','êtes','sont']:['ai','as','a','avons','avez','ont'])[k[pi]];
    const pp={aider:'aidé',finir:'fini',arriver:'arrivé',partir:'parti'}[verb]+(moving&&[3,7].includes(pi)?'e':'')+(moving&&pi>=4?'s':'');
    assert.equal(q.answer,withPron(subject,aux+' '+pp));
  }
  assert.equal(seen.size,48);
});

test('avoir agreement follows the preceding object, not the feminine subject Bih',()=>{
  const forms={'la lettre':'écrite','les lettres':'écrites','le message':'lu','les messages':'lus','les affiches':'préparées','la fiche':'finie'};
  const seen=new Set();
  for(let seed=1;seed<=180;seed++){
    const q=instantiate(tpl('fi4-42-accorder'),seed,lib);
    const object=q.prompt.match(/« ([^»]+) que Bih/)[1];
    assert.equal(q.answer,forms[object]);
    assert.equal(new Set(q.options.map((o)=>o.text)).size,4);
    seen.add(object);
    const e=instantiate(tpl('fi4-13-accorder'),seed,lib);
    const v=e.prompt.match(/« ([^»]+) »/)[1];
    const feminine=e.prompt.includes('féminin'),plural=e.prompt.includes('pluriel');
    assert.equal(e.answer,{arriver:'arrivé',partir:'parti',aller:'allé',tomber:'tombé'}[v]+(feminine?'e':'')+(plural?'s':''));
  }
  assert.equal(seen.size,6);
});

test('traditional compound plurals preserve their structure and oral models make no audio claim',()=>{
  const plurals={'coffre-fort':'des coffres-forts','chou-fleur':'des choux-fleurs','pomme de terre':'des pommes de terre','tire-bouchon':'des tire-bouchons'};
  const seen=new Set();
  for(let seed=1;seed<=150;seed++){
    const q=instantiate(tpl('fi4-49-appliquer'),seed,lib);
    const word=Object.keys(plurals).find((w)=>q.prompt.includes(w));
    assert.equal(q.answer,plurals[word]);
    seen.add(word);
  }
  assert.equal(seen.size,4);
  for(const n of [4,8,19,39,41,43]){
    const text=renderLearn(active.find((l)=>l.lesson_no===n),lib).pages.map((p)=>p.text).join(' ');
    assert.match(text,/écrit|prépar/);
    assert.match(text,/ne .*(voix|écoute)|ne remplace|pas .*voix|pas .*son|réelle|réellement/);
  }
  const l=active.find((l)=>l.lesson_no===51);
  assert.match(renderLearn(l,lib).pages.find((p)=>p.figure).figure,/Illustration inventée/);
});
