import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {instantiate} from '../../../src/engine/template.js';
import {renderLearn} from '../../../src/engine/teach.js';
import {registrySubjects,libOf} from '../../classes.mjs';
const subject=registrySubjects().find(s=>s.id==='f5-french');
const lib=await libOf(subject);
const read=n=>JSON.parse(readFileSync(new URL(`../../../content/form-5/french/${n}.json`,import.meta.url)));
const tpl=(n,id)=>read(n).questions.find(q=>q.id===id);
const pronouns=['je','tu','il','elle','nous','vous','ils','elles'],persons=[0,1,2,2,3,4,5,5];
const full=(p,form)=>p==='je'&&/^[aeiouéè]/.test(form)?'j’'+form:p+' '+form;
const tokens=q=>[...q.prompt.matchAll(/« ([^»]+) »/g)].map(m=>m[1]);

test('French covers parsed teaching rows and keeps the suspected integration classification visible for review',()=>{
  const spine=JSON.parse(readFileSync(new URL('../../../data/spine/form-5/french.json',import.meta.url)));
  assert.deepEqual(subject.lessons,spine.terms[0].lessons.filter(r=>r.kind==='lesson').map(r=>r.seq));
  assert.equal(subject.lessons.length,29);
  assert.deepEqual(subject.lessons.filter(n=>read(n).paper_task),[9,31]);
  for(const n of subject.lessons){
    const l=read(n);assert.equal(l.language,'fr');assert.equal(l.subject,'french');
    for(const p of l.prerequisites)assert.ok(p<n&&subject.lessons.includes(p));
    const pages=renderLearn(l,lib).pages;
    for(const label of ['À la fin','Acquis mobilisés :','Pour la suite :'])assert.ok(pages[0].text.includes(label));
    assert.doesNotMatch(pages.map(p=>p.text||'').join(' '),/Elle elle|Nous nous nous/);
  }
  const review=readFileSync(new URL('../../../content/form-5/french/TEACHER-REVIEW.md',import.meta.url),'utf8');
  assert.match(review,/ligne 3/);assert.match(review,/kind vaut integration/);
});

test('pronominal present preserves person, stem and elision across all taught forms',()=>{
  const forms={laver:['lave','laves','lave','lavons','lavez','lavent'],lever:['lève','lèves','lève','levons','levez','lèvent'],appeler:['appelle','appelles','appelle','appelons','appelez','appellent']};
  const seen=new Set();
  for(let seed=1;seed<=650;seed++){
    const q=instantiate(tpl(4,'fr5-4-formes'),seed,lib);
    const [verbPhrase,p]=tokens(q);const v=verbPhrase.includes('appeler')?'appeler':verbPhrase.split(' ')[1];
    const pi=pronouns.indexOf(p),k=persons[pi];assert.ok(pi>=0);
    let ref=['me','te','se','nous','vous','se'][k];
    ref=v==='appeler' && ['me','te','se'].includes(ref)?ref[0]+'’':ref+' ';
    assert.equal(q.answer,p+' '+ref+forms[v][k],q.prompt);
    assert.equal(new Set(q.options.map(o=>o.text)).size,4);
    seen.add(v+':'+p);
  }
  assert.equal(seen.size,24);
});

test('irregular present and past frames agree with separate reference paradigms',()=>{
  const present={aller:['vais','vas','va','allons','allez','vont'],faire:['fais','fais','fait','faisons','faites','font'],venir:['viens','viens','vient','venons','venez','viennent'],prendre:['prends','prends','prend','prenons','prenez','prennent'],être:['suis','es','est','sommes','êtes','sont'],avoir:['ai','as','a','avons','avez','ont']};
  const imp={aider:['aidais','aidais','aidait','aidions','aidiez','aidaient'],finir:['finissais','finissais','finissait','finissions','finissiez','finissaient'],voir:['voyais','voyais','voyait','voyions','voyiez','voyaient'],faire:['faisais','faisais','faisait','faisions','faisiez','faisaient']};
  const pp={aider:'aidé',finir:'fini',voir:'vu',faire:'fait'},aux=['avais','avais','avait','avions','aviez','avaient'];
  const seen=new Set();
  for(let seed=1;seed<=700;seed++){
    for(const [n,id] of [[10,'fr5-10-present'],[18,'fr5-18-formes']]){
      const q=instantiate(tpl(n,id),seed,lib);const [v,p]=tokens(q),k=persons[pronouns.indexOf(p)];
      const expected=n===10?full(p,present[v][k]):full(p,q.prompt.includes('plus-que-parfait')?aux[k]+' '+pp[v]:imp[v][k]);
      assert.equal(q.answer,expected,q.prompt);
      assert.equal(new Set(q.options.map(o=>o.text)).size,4);
      seen.add(n+':'+v+':'+p);
    }
  }
  assert.ok(seen.size>=70);
});

test('images vary visually and contextual quelque forms preserve agreement',()=>{
  const images=new Set(),forms=new Set();
  const model=renderLearn(read(19),lib).pages.find(p=>p.figure).figure;
  assert.match(model,/Scène environnementale inventée/);assert.doesNotMatch(model,/u00/);
  for(let seed=1;seed<=200;seed++){
    const img=instantiate(tpl(19,'fr5-19-image'),seed,lib);images.add(img.figure);
    assert.match(img.figure,/Dessin pédagogique inventé/);
    const q=instantiate(tpl(29,'fr5-29-appliquer'),seed,lib);
    const expected=q.prompt.includes('temps')?'quelque':q.prompt.includes('affiches')?'quelques':q.prompt.includes('les activités')?'quelles que':q.prompt.includes('l’activité')?'quelle que':q.prompt.includes('les projets')?'quels que':'quel que';
    assert.equal(q.answer,expected,q.prompt);forms.add(q.answer);
  }
  assert.equal(images.size,4);assert.equal(forms.size,6);
});
