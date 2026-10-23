import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import * as maths from '../../../src/engine/lib/maths.js';
import * as english from '../../../src/engine/lib/english.js';
import * as french from '../../../src/engine/lib/french.js';
import * as french2 from '../../../src/engine/lib/french2.js';
import { instantiate } from '../../../src/engine/template.js';
import { renderLearn,cardCheckTemplate } from '../../../src/engine/teach.js';
const lib={...maths,...english,...french,...french2};
const read=(p)=>JSON.parse(readFileSync(new URL(p,import.meta.url)));
const rows=read('../../../data/spine/form-2/french.json').terms[2].lessons.filter((r)=>r.kind==='lesson').map((r)=>r.seq);
const lessons=rows.map((n)=>read(`../../../content/form-2/french/${n}.json`));
const template=(id)=>lessons.flatMap((l)=>l.questions).find((q)=>q.id===id);

test('all twelve rows meet the full format and have genuine content variants and explained wrong options',()=>{
  assert.deepEqual(rows,Array.from({length:12},(_,i)=>70+i));
  for(const l of lessons){
    assert.equal(l.questions.length,5);
    assert.equal(l.teach.cards.length,3);
    assert.equal(l.language,'fr');
    const opening=renderLearn(l,lib).pages[0];
    for(const label of ['À la fin','Acquis mobilisés :','Pour la suite :']) assert.ok(opening.text.includes(label));
    for(const p of l.prerequisites) assert.ok(p<l.lesson_no&&rows.includes(p));
    for(const t of [...l.questions,...l.teach.cards.map((c)=>cardCheckTemplate(l,c))]){
      const seen=new Set();
      for(let seed=1;seed<=160;seed++){
        const q=instantiate(t,seed,lib);
        seen.add(JSON.stringify([q.prompt,q.answer,q.options?.map((o)=>o.text).sort(),q.left?.slice().sort()]));
        assert.equal(t.lang,'fr');
        for(const [i,o] of (q.options||[]).entries()) if(i!==q.correctIndex) assert.ok(o.explain);
      }
      assert.ok(seen.size>=3,`${t.id}: ${seen.size}`);
    }
  }
  assert.deepEqual(lessons.filter((l)=>l.paper_task).map((l)=>l.lesson_no),[77,81]);
});

test('displayed present and imperfect forms match separate reference tables',()=>{
  const pron=['je','tu','il','elle','nous','vous','ils','elles'],person=[0,1,2,2,3,4,5,5];
  const forms={
    74:{parler:['parlais','parlais','parlait','parlions','parliez','parlaient'],envoyer:['envoyais','envoyais','envoyait','envoyions','envoyiez','envoyaient'],lire:['lisais','lisais','lisait','lisions','lisiez','lisaient'],écrire:['écrivais','écrivais','écrivait','écrivions','écriviez','écrivaient'],manger:['mangeais','mangeais','mangeait','mangions','mangiez','mangeaient'],être:['étais','étais','était','étions','étiez','étaient']},
    80:{parler:['parle','parles','parle','parlons','parlez','parlent'],envoyer:['envoie','envoies','envoie','envoyons','envoyez','envoient'],recevoir:['reçois','reçois','reçoit','recevons','recevez','reçoivent'],lire:['lis','lis','lit','lisons','lisez','lisent'],écrire:['écris','écris','écrit','écrivons','écrivez','écrivent'],faire:['fais','fais','fait','faisons','faites','font']},
  };
  for(const n of [74,80]){
    const seen=new Set();
    for(let seed=1;seed<=650;seed++){
      const q=instantiate(template(`fr2-${n}-conjuguer`),seed,lib);
      const [v,p]=[...q.prompt.matchAll(/« ([^»]+) »/g)].map((m)=>m[1]);
      const form=forms[n][v][person[pron.indexOf(p)]];
      assert.equal(q.answer,p==='je'&&/^[aeiouéè]/.test(form)?'j’'+form:p+' '+form);
      assert.equal(new Set(q.options.map((o)=>o.text)).size,4);
      seen.add(v+':'+p);
    }
    assert.equal(seen.size,48);
  }
});

test('pronoun agreement follows the subject and sound models separate vowel and consonant nasality',()=>{
  const third={parler:['parle','parlent'],lire:['lit','lisent'],écrire:['écrit','écrivent'],travailler:['travaille','travaillent']};
  for(let seed=1;seed<=150;seed++){
    const q=instantiate(template('fr2-72-accorder'),seed,lib);
    const v=Object.keys(third).find((v)=>q.prompt.includes('Verbe : '+v));
    const plural=q.prompt.includes('Plusieurs')||q.prompt.includes('Certains');
    assert.equal(q.answer,third[v][Number(plural)]);
  }
  const nasal=renderLearn(lessons.find((l)=>l.lesson_no===79),lib).pages.map((p)=>p.text).join(' ');
  assert.match(nasal,/consonne est elle aussi nasale/);
  assert.match(nasal,/pas une voyelle/);
  const rounded=renderLearn(lessons.find((l)=>l.lesson_no===75),lib).pages.map((p)=>p.text).join(' ');
  assert.match(rounded,/se rapprochent ou se confondent/);
  assert.match(rounded,/pas .*écoute réelle/);
});
