import { test } from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import * as maths from '../../../src/engine/lib/maths.js';
import * as english from '../../../src/engine/lib/english.js';
import * as french from '../../../src/engine/lib/french.js';
import * as french2 from '../../../src/engine/lib/french2.js';
import {instantiate} from '../../../src/engine/template.js';
import {renderLearn,cardCheckTemplate} from '../../../src/engine/teach.js';
const lib={...maths,...english,...french,...french2};
const read=(p)=>JSON.parse(readFileSync(new URL(p,import.meta.url)));
const rows=read('../../../data/spine/form-2/francais-intensif.json').terms[2].lessons.filter((r)=>r.kind==='lesson').map((r)=>r.seq);
const lessons=rows.map((n)=>read(`../../../content/form-2/francais-intensif/${n}.json`));
const tpl=(id)=>lessons.flatMap((l)=>l.questions).find((q)=>q.id===id);

test('twenty-five complete lessons preserve goals, earlier dependencies, paper writing and genuine variants',()=>{
  assert.deepEqual(rows,Array.from({length:25},(_,i)=>104+i));
  for(const l of lessons){
    assert.equal(l.language,'fr');assert.equal(l.questions.length,5);assert.equal(l.teach.cards.length,3);
    const opening=renderLearn(l,lib).pages[0];
    for(const label of ['À la fin','Acquis mobilisés :','Pour la suite :']) assert.ok(opening.text.includes(label));
    for(const p of l.prerequisites) assert.ok(p<l.lesson_no&&rows.includes(p));
    for(const t of [...l.questions,...l.teach.cards.map((c)=>cardCheckTemplate(l,c))]){
      const seen=new Set();
      for(let seed=1;seed<=160;seed++){
        const q=instantiate(t,seed,lib);
        seen.add(JSON.stringify([q.prompt,q.answer,q.figure,q.options?.map((o)=>o.text).sort(),q.left?.slice().sort()]));
        assert.equal(t.lang,'fr');
        for(const [i,o] of (q.options||[]).entries()) if(i!==q.correctIndex) assert.ok(o.explain);
      }
      assert.ok(seen.size>=3,`${t.id}: ${seen.size}`);
    }
  }
  assert.deepEqual(lessons.filter((l)=>l.paper_task).map((l)=>l.lesson_no),[110,117,122,124,128]);
});

test('future and conditional use independent stems and the actual displayed person',()=>{
  const pron=['je','tu','il','elle','nous','vous','ils','elles'],person=[0,1,2,2,3,4,5,5];
  const stem={parler:'parler',finir:'finir',envoyer:'enverr',recevoir:'recevr',être:'ser',faire:'fer'};
  const seen=new Set();
  for(let seed=1;seed<=1100;seed++){
    const q=instantiate(tpl('fi2-105-conjuguer'),seed,lib);
    const [v,p]=[...q.prompt.matchAll(/« ([^»]+) »/g)].map((m)=>m[1]);
    const tense=q.prompt.includes('au futur simple,')?'future':'conditional';
    const form=stem[v]+(tense==='future'?['ai','as','a','ons','ez','ont']:['ais','ais','ait','ions','iez','aient'])[person[pron.indexOf(p)]];
    assert.equal(q.answer,p==='je'&&/^[aeiouéè]/.test(form)?'j’'+form:p+' '+form);
    assert.equal(new Set(q.options.map((o)=>o.text)).size,4);seen.add(v+':'+p+':'+tense);
  }
  assert.equal(seen.size,96);
});

test('past anterior uses past-simple auxiliaries, elision and subject agreement after être',()=>{
  const pron=['je','tu','il','elle','nous','vous','ils','elles'],person=[0,1,2,2,3,4,5,5];
  const seen=new Set();
  for(let seed=1;seed<=650;seed++){
    const q=instantiate(tpl('fi2-113-conjuguer'),seed,lib);
    const [v,p]=[...q.prompt.matchAll(/« ([^»]+) »/g)].map((m)=>m[1]);
    const pi=pron.indexOf(p),moving=['arriver','partir'].includes(v);
    const aux=(moving?['fus','fus','fut','fûmes','fûtes','furent']:['eus','eus','eut','eûmes','eûtes','eurent'])[person[pi]];
    const pp={finir:'fini',écrire:'écrit',arriver:'arrivé',partir:'parti'}[v]+(moving&&[3,7].includes(pi)?'e':'')+(moving&&pi>=4?'s':'');
    const phrase=aux+' '+pp;
    assert.equal(q.answer,p==='je'&&/^[aeiouéè]/.test(phrase)?'j’'+phrase:p+' '+phrase);
    seen.add(v+':'+p);
  }
  assert.equal(seen.size,32);
});

test('coordinated subjects preserve grammatical person and images supply four real visual scenarios',()=>{
  const persons={'Bih et Ayuk':2,'Bih et moi':0,'Ayuk et toi':1,'Toi et moi':0};
  const forms={lire:['lisons','lisez','lisent'],écrire:['écrivons','écrivez','écrivent'],parler:['parlons','parlez','parlent'],faire:['faisons','faites','font']};
  const images=new Set();
  for(let seed=1;seed<=180;seed++){
    const q=instantiate(tpl('fi2-112-accorder'),seed,lib);
    const s=Object.keys(persons).find((s)=>q.prompt.includes(s));
    const v=Object.keys(forms).find((v)=>q.prompt.includes('Verbe : '+v));
    assert.equal(q.answer,forms[v][persons[s]]);
    const i=instantiate(tpl('fi2-121-image'),seed,lib);
    assert.match(i.figure,/Scène de média inventée/);images.add(i.figure);
  }
  assert.equal(images.size,4);
  const sequence=renderLearn(lessons.find((l)=>l.lesson_no===124),lib).pages.find((p)=>p.figure).figure;
  assert.match(sequence,/de gauche à droite/);assert.match(sequence,/Préparer/);assert.match(sequence,/Vérifier/);assert.match(sequence,/Corriger/);
  for(const n of [111,127]) assert.match(renderLearn(lessons.find((l)=>l.lesson_no===n),lib).pages[2].text,/Récit original/);
});
