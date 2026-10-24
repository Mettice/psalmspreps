"""Record teacher-feedback deferrals and audit Codex's explicitly assigned batches.

Run from any directory. Does not author lessons, edit spines or change assignments.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
reg=json.loads((ROOT/'content/classes.json').read_text(encoding='utf-8'))
subjects=['english','french','francais-intensif','history','geography','economics','logic']
scopes=[(c,d,1) for c in ['form-3','form-4'] for d in subjects]
scopes += [('form-4','literature',1),('form-2','french',3),('form-2','francais-intensif',3)]
scopes += [('form-5',d,1) for d in subjects]
scopes += [('lower-sixth','english',1)]
pending={
 ('form-3','french'):{18:'Libellé « L’imparfait présent » ambigu : retour enseignant attendu, conformément à la consigne de Dion de laisser cette ligne en attente.'},
 ('form-3','francais-intensif'):{
  **{n:'Lecture d’une œuvre prescrite : retour enseignant attendu sur titre, auteur et édition/extraits avant rédaction.' for n in [3,5,9,14,19,23,24,30,31,35,39,41,42,46,48,49]},
  **{n:'Le titre mêle verbes pronominaux et voix active/passive : clarification enseignante attendue ; aucun remplacement inventé.' for n in [40,45]}},
 ('form-4','literature'):{n:'Awaiting teacher feedback on the prescribed text, author and edition/scene divisions. Dion requested that these rows remain pending; no replacement analysis is invented.' for n in [*range(3,19),*range(20,39)]},
}

for (cls,subject),entries in pending.items():
    spec=reg[cls]['subjects'][subject]
    for n,reason in entries.items():
        path=ROOT/f'content/{cls}/{subject}/{n}.json'
        if path.exists() and json.loads(path.read_text(encoding='utf-8')).get('status')!='deferred':
            continue  # A later teacher-informed lesson takes precedence.
        spine=json.loads((ROOT/f"data/spine/{cls}/{spec['spine']}.json").read_text(encoding='utf-8'))
        row=next(r for r in spine['terms'][0]['lessons'] if r['seq']==n)
        data={'subject':spec['lesson_subject'],'class':reg[cls]['cls'],'lesson_no':n,
              'language':spec.get('lang','en'),'status':'deferred','sheet_title':row['title'],
              'deferred_reason':reason}
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(data,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')

report=['# Codex completed batches — coverage and teacher feedback','','Audit date: 2026-10-24. Scope: Form Three, Form Four and Form Five Term One assigned language/humanities/economics/logic subjects, Form Four Literature, the two Form Two Term Three language quality batches, and completed Lower Sixth English. Other authorised Lower/Upper Sixth subjects remain outside this completed-batch audit and are not claimed complete.','','A draft is technically checked content awaiting teacher review, not a claim of classroom approval. A deferred row is explicitly awaiting teacher feedback and is not counted as written. Diagnostic/integration/revision activities are excluded under AUTHORING.md. Lower Sixth English row 16 is the standalone comprehension/grammar review; rows 10/12 teach named word-class foundations despite their review wording. Form Five French row 3 is classified integration despite a vocabulary title; teacher/integrator feedback is requested before reclassification.','','| Class / batch | Subject | Draft lessons and guided practicals | Awaiting teacher feedback | Unaccounted rows |','|---|---|---:|---:|---:|']
totals={'draft':0,'deferred':0}
details=[]
for cls,subject,term in scopes:
    if cls=='form-2':
        spine_name=subject
    else:
        spine_name=reg[cls]['subjects'][subject]['spine']
    spine=json.loads((ROOT/f'data/spine/{cls}/{spine_name}.json').read_text(encoding='utf-8'))
    rows=next(t for t in spine['terms'] if t['term']==term)['lessons']
    counts={'draft':0,'deferred':0};missing=[]
    for row in rows:
        if (cls,subject,row['seq'])==('lower-sixth','english',16):
            details.append('- lower-sixth english row 16: standalone comprehension/grammar review excluded despite its lesson classification.')
            continue
        if row['kind'] not in (['lesson','practical','guided_work'] if cls=='form-5' else ['lesson','practical']):
            continue
        if 'diagnostic' in row['title'].lower():
            details.append(f"- {cls} {subject} row {row['seq']}: diagnostic excluded even though the parser labels it lesson.")
            continue
        path=ROOT/f"content/{cls}/{subject}/{row['seq']}.json"
        if not path.exists():
            missing.append(row['seq']);continue
        obj=json.loads(path.read_text(encoding='utf-8'))
        if obj.get('status')=='deferred':
            counts['deferred']+=1
            details.append(f"- {cls} {subject} row {row['seq']}: {obj['deferred_reason']}")
        else:
            assert obj.get('learn',{}).get('sections'),str(path)+': missing Learn'
            assert 4<=len(obj.get('questions',[]))<=6,str(path)+': require 4–6 questions'
            counts['draft']+=1
    assert not missing,f'{cls} {subject}: unaccounted rows {missing}'
    for key in counts:totals[key]+=counts[key]
    report.append(f"| {cls}, Term {term} | {subject} | {counts['draft']} | {counts['deferred']} | {len(missing)} |")
report += ['',f"Total: {totals['draft']} drafts (including guided practicals), {totals['deferred']} rows awaiting teacher feedback, no unaccounted assigned teaching rows.",'',
 '## Feedback to collect from teachers','',
 '- Confirm prescribed titles, authors and editions for Form Three / Four / Five Français intensif. The relevant rows remain deferred.',
 '- Clarify Form Five French row 3 classification and Geography row 4 mixed title. Review the dated income/industry distinction, simplified Weber candidate model, historical case choices and institutional status notes in the subject teacher-review files.',
 '- Confirm the Form Four Literature books and edition. Its spine names The Crown of Thorns and Macbeth, but the author/edition and chapter/scene alignment still need teacher confirmation. Only the independent foundations in rows 2 and 19 are drafted.',
 '- Clarify Form Three French row 18 and Français intensif rows 40/45. Dion explicitly requested that ambiguous rows stay pending.',
 '- Review each subject’s TEACHER-REVIEW.md for terminology, depth, local facts, exam conventions and real oral/writing practice. No teacher-feedback item is automatically marked approved.',
 '', '## Row dispositions','',*details,'',
 'User direction on 2026-10-24: keep these unresolved choices for teacher feedback. Do not replace prescribed works, guess ambiguous titles or treat a deferral as a completed lesson.']
(ROOT/'docs/CODEX-CONTENT-STATUS.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print(f"{totals['draft']} drafts; {totals['deferred']} teacher-feedback deferrals; no unaccounted rows.")
