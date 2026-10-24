"""Form Four Literature: edition-independent foundations; prescribed texts await teacher feedback."""
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import lessonlib as L
import banks_en as B
from lessonlib import card,worked,learn,num,mcq
L.use_class("form-4","Form 4")
OUT=L.ROOT/"literature"
SRC=["literary-foundations"]
PATH=[]

def F(term,meaning,case,error,why): return dict(term=term,meaning=meaning,case=case,error=error,why=why)
def item(q,r,wrong,why):
    assert len(wrong)==3
    return dict(q=q,r=r,w=[x[0] for x in wrong],e=[x[1] for x in wrong],y=why)
def qa(n,key,level,items): return B.QA(f"lit4-{n}-{key}",level,"{X.q}",items,SRC)
def choose(n,rows,level=2,key="apply"):
    return qa(n,key,level,[item(q,r,list(zip(w,e)),why) for q,r,w,e,why in rows])
def word_order(n,sentences): return B.WO(f"lit4-{n}-build",2,sentences,SRC)

def unit(n,title,goal,back,next_use,note,case,method,facts,applied,prereq=(),paper=None,extra=None,example=None):
    assert 4 <= len(facts) <= 6
    terms=[]; cases=[]
    for i,f in enumerate(facts):
        other=[x for j,x in enumerate(facts) if j!=i][:3]
        terms.append(item("Which term means "+f["meaning"]+"?",f["term"],[(x["term"],"That concerns "+x["meaning"]+", rather than "+f["meaning"]+".") for x in other],f["why"]))
        cases.append(item(f["case"]+"\nWhich description best fits the selected feature?",f["term"],[(x["term"],"That means "+x["meaning"]+". The selected feature instead illustrates "+f["meaning"]+".") for x in other],f["why"]))
    q0=qa(n,"terms",1,terms); q1=qa(n,"cases",1,cases)
    q3=extra or B.MT(f"lit4-{n}-link",2,"Match each term to its example.",[(f["term"],f["case"]) for f in facts],SRC,pick=3)
    q4=B.SP(f"lit4-{n}-repair",3,"Find the incorrect claim or language form.",[f["term"]+": "+f["meaning"]+"." for f in facts],[(f["error"],f["why"]) for f in facts],SRC)
    for st,f in zip(q4["pool"]["right"],facts): st["explain"]="This is correct: "+f["meaning"]+". Look for a claim that conflicts with a rule or distinction taught in Learn."
    questions=[q0,q1,applied,q3,q4]
    cards=[card(f"lit4-{n}-c1","Distinguish the ideas used in this lesson.",[f["term"]+": "+f["meaning"]+"." for f in facts],q0["id"]),
       card(f"lit4-{n}-c2","Read the whole example before identifying its function.",[f["case"] for f in facts],q1["id"]),
       card(f"lit4-{n}-c3","A correction must preserve the intended meaning and form.",[f["error"]+" Correction: "+f["why"] for f in facts],q4["id"])]
    L.lesson("literature","literature-in-english",n,(f"lit4-{n}",title),prereq,note,
       example or worked({},facts[0]["case"]+" Explain the selected feature.",[facts[0]["meaning"].capitalize()+".",facts[0]["why"]],facts[0]["term"]),cards,questions,paper=paper,
       learn=learn([("Your goal and connections","By the end, you should be able to "+goal+". Builds on: "+back+". Leads to: "+next_use+"."),
         ("Understand the pattern",note),("Read the original model",case),("Apply and check",method)],
         key_words=[(f["term"],f["meaning"]) for f in facts],mistake=(facts[0]["error"],facts[0]["term"]+": "+facts[0]["meaning"]+".",facts[0]["why"])))
    PATH.append((n,title,goal,back,next_use))

unit(2,'Plot, setting, character, theme and point of view',
 'support a claim about a story feature with a specific detail and distinguish interpretation from summary',
 'reading short passages and separating facts from inference in Form Three English',
 'analysing the prescribed novel once the class text and edition are confirmed',
 'Plot concerns what happens and how events are connected; setting places those events in a time, place and social situation. Characterisation develops a person through actions, speech, description or reported thought. A theme is an idea explored through the work, rather than merely a topic word or a list of events. Point of view concerns the perspective and access through which the story is told. A fictional narrator is not automatically its real author. Interpretations need evidence: describe a detail, explain what it suggests, and keep the conclusion within what the passage supports.',
 'Original invented story: At dusk in a fictional Bamenda reading club, Bih found a borrowed book under the table. She could quietly return it and avoid a difficult question. Instead, she told Ayuk where she had left it. He checked the register with her. The narrator reports their actions but gives no direct account of Ayuk’s thoughts. The choice and its consequence can support discussion of responsibility; the setting alone does not prove that interpretation.',
 'Ask what happened, where and when, how a person is presented, what idea the choices explore, and whose perspective is available. For an interpretation, name the detail before explaining its effect. A different reading may be reasonable if supported; do not turn an absent thought or future outcome into a fact.',[
 F('plot','the events of a story and the relationships connecting them','Bih finds the book, chooses to speak, and checks the register with Ayuk.','A plot is simply any place named in the story.','The actions and choices form the event pattern; the place is part of setting.'),
 F('setting','the time, place and relevant social circumstances of the story','Dusk in the fictional Bamenda club locates the scene.','A place name proves the whole theme without any action or language.','Setting can contribute to meaning, but an interpretation needs relevant evidence.'),
 F('characterisation','the presentation of a character through relevant details','Bih chooses to acknowledge where she left the book.','A single choice proves every trait of a person for all time.','The choice supports a limited interpretation of this scene, not a complete personality judgement.'),
 F('theme','an idea explored through the work and supported by its details','Responsibility may be explored through admission and checking together.','The word book alone states a developed theme.','A topic names a subject; a thematic claim explains an idea supported by the work.'),
 F('point of view','the perspective and access through which the story is narrated','The narrator shows actions without revealing Ayuk’s exact thoughts.','Every fictional narrator must be the real author speaking autobiographically.','Narrator and author are different roles; access must be established from the text.')],
 choose(2,[
 ('Original invented passage: Bih could hide a misplaced book, but instead reports it and helps check the record. Which claim has the strongest support?',
  'The choice can support an interpretation about taking responsibility.',
  ['Bih will never make any mistake again.','Every person in Bamenda always acts identically.','The real author personally lost this exact book.'],
  ['The future absolute goes beyond this choice.','One fictional action does not establish a fact about a population.','A fictional event is not proof of the author’s biography.'],'Link the choice to a proportionate thematic interpretation.'),
 ('Original invented passage: At dawn in a Buea classroom, Ayuk waits beside an empty noticeboard. Which detail most directly establishes setting?',
  'At dawn in a Buea classroom.',
  ['Ayuk must secretly be furious.','Every noticeboard represents betrayal.','The author must have been Ayuk.'],
  ['The passage does not report that thought.','No evidence establishes this symbolic meaning.','A named character does not identify the author.'],'Time and place are explicit; the other claims add unsupported meanings.'),
 ('Original invented passage: “I hid the unfinished notice in my bag. I could not tell what Amina thought.” Which point-of-view claim is supported?',
  'A participating first-person narrator reports a limit to their knowledge.',
  ['The narrator knows every character’s exact thoughts.','The writer and narrator must be the same real person.','The passage has no perspective because it uses I.'],
  ['The stated uncertainty contradicts unlimited access.','First-person fiction need not be autobiography.','I marks a perspective rather than removing it.'],'The voice participates and explicitly lacks access to another person’s thoughts.'),
 ('Original invented passage: Ngozi admits an error; the group corrects the notice before sharing it. Which response goes beyond event summary?',
  'The correction after admission suggests a link between honesty and collective repair.',
  ['Ngozi admits an error, then the group corrects a notice.','The word notice is the complete theme.','The scene proves every group always repairs every error.'],
  ['That retells the events without explaining their possible significance.','A topic word alone does not develop a thematic claim.','This universal conclusion exceeds one invented scene.'],'Analysis explains a relationship between evidence and meaning, while remaining open to supported alternatives.')]),
 example=worked({},'Original invented example: Bih admits misplacing a book and joins the search. Explain a possible thematic reading.',
 ['The relevant evidence is the admission followed by participation in repair.','These choices can suggest responsibility as an explored idea.','The wording can suggest keeps the conclusion tied to this short scene.'],
 'The admission and joint search can support a reading about responsibility; they do not prove Bih’s behaviour in every situation.'))

unit(19,'Dramatic elements and conventions',
 'interpret a short script by separating spoken words, performance instructions and audience knowledge',
 'story features, point of view and evidence in the earlier foundation lesson',
 'reading the prescribed play with the teacher-confirmed edition and scene divisions',
 'Drama can communicate through dialogue, action, pauses and instructions for performance. Stage directions specify features such as movement or delivery; they are not necessarily spoken by a character. An aside is conventionally not heard by specified other characters. A soliloquy gives access to private thought, often when a character speaks as if alone; actual staging can vary. Dramatic irony arises when the audience knows a relevant fact that a character does not, making words or actions carry an additional meaning. Identify what each participant can know before explaining an effect.',
 'Original invented script: [Bih puts an unsigned notice in a folder. Ayuk enters.] AYUK: “The notice has already been approved.” BIH [aside; Ayuk does not hear]: “The signature is still missing.” The audience has seen and heard a gap in Ayuk’s knowledge. This can create concern about his confidence. The script does not prove why the signature is absent or what the group will decide. This is written preparation; the screen does not assess acting or listening.',
 'Separate dialogue from directions. Map what the audience knows, what a character knows and which instruction establishes that difference. Explain the possible effect with a detail. Do not treat every long speech as a soliloquy or assume that a character’s belief is the play’s confirmed truth.',[
 F('dialogue','words spoken by characters in the dramatic exchange','AYUK: The notice has already been approved is a spoken line in the invented script.','Every spoken belief must be a confirmed fact of the play.','A character can be mistaken; compare the line with other evidence.'),
 F('stage direction','a written instruction guiding performance or stage action','Ayuk enters tells a performer about movement.','Every stage direction must be recited as the character’s dialogue.','The instruction guides action and need not be spoken.'),
 F('aside','a speech conventionally unheard by specified other characters','The instruction explicitly says Ayuk does not hear Bih’s short comment.','An aside automatically makes every character know the secret.','The stated convention keeps the information from Ayuk in this model.'),
 F('soliloquy','a speech presenting private thought, often as if a character were alone','An invented character speaks their private uncertainty as if alone.','Every speech to a group is automatically a soliloquy because it is long.','Private thought and dramatic convention matter; length alone does not decide.'),
 F('dramatic irony','an important difference between audience and character knowledge','The audience knows about the missing signature while Ayuk confidently assumes approval.','Dramatic irony requires the audience and character to know exactly the same facts.','The significant gap in knowledge creates the additional meaning.')],
 choose(19,[
 ('Original invented script: [Amina slips the only key into her bag and exits. Bih enters.] BIH: “The key is safely on the hook.” What creates dramatic irony?',
  'The audience saw the key moved, while Bih speaks from incomplete knowledge.',
  ['Bih knows everything the audience has seen.','The stage direction is an instruction for the audience to take a real key.','The script proves Amina’s whole motive and future.'],
  ['Bih’s claim conflicts with what the audience saw.','The direction describes fictional stage action.','The action alone does not establish all motives or outcomes.'],'Explain the relevant difference in knowledge.'),
 ('Original invented script: BIH [aside; Ayuk cannot hear]: “I have not checked the date.” AYUK: “Then we agree it is accurate.” Which interpretation respects the convention?',
  'The audience receives Bih’s uncertainty without Ayuk receiving that aside.',
  ['Ayuk must have heard the aside because the audience did.','The aside guarantees the date is wrong.','The instruction erases every possible performance choice in every play.'],
  ['Audience access and character access differ here by explicit instruction.','Unverified does not mean proven false.','This model specifies a local convention, not every staging of every play.'],'Separate access to information from proof of its truth.'),
 ('Original invented script: [Alone, Amina speaks her private doubt.] AMINA: “Should I admit the unfinished work?” Which feature best fits this written model?',
  'A soliloquy exposing private deliberation.',
  ['An ordinary conversation addressed to a group of classmates.','A stage direction spoken instead of every word in the speech.','Proof that all real performances must place no other actor anywhere on stage.'],
  ['The model says alone and gives private deliberation.','The bracketed instruction and spoken words have separate roles.','Production choices vary; this is the convention specified for this example.'],'The instruction and reflective question support the classification.'),
 ('Original invented script: [Pause. Bih looks at the unsigned page.] AYUK: “Why have you stopped?” Which claim is best supported?',
  'The pause and gaze can draw attention to the page before the question.',
  ['Bih’s exact thoughts and a later confession are already given.','Pause is necessarily a word Bih must pronounce.','The audience has been told the signature was deliberately forged.'],
  ['The direction does not state those thoughts or future action.','The direction controls performance rather than requiring that spoken word.','No forgery or intention is stated.'],'A performance instruction supports a possible effect without revealing every motive.')]),
 prereq=[2],example=worked({},'In the original Learn script, explain why Ayuk’s confidence can create dramatic irony.',
 ['The audience receives the information that the signature is missing.','The instruction says Ayuk does not hear the aside.','His confident approval claim therefore has an additional meaning for the audience.'],
 'The gap between audience knowledge and Ayuk’s belief can create concern; the missing signature’s cause remains unknown.'))

(OUT/'sources.json').write_text(json.dumps({'literary-foundations':{
 'ref':'Original invented prose and scripts; OpenStax textual-analysis teaching; RSC and Folger discussion of dramatic convention and audience knowledge',
 'urls':['https://openstax.org/books/writing-guide/pages/16-5-writing-process-thinking-critically-about-text',
 'https://openstax.org/books/writing-guide/pages/4-3-glance-at-genre-conflict-detail-and-revelation',
 'https://www.rsc.org.uk/learn/young-people/homework-help',
 'https://cdn2.rsc.org.uk/sitefinity/education-pdfs/teacher-packs/bitd-pack.pdf?sfvrsn=52d6a121_4',
 'https://www.folger.edu/explore/shakespeares-works/hamlet/further-reading/'],
 'checked':'Official educational pages and indexed passages consulted 2026-10-24. All pupil passages and scripts are newly authored and explicitly invented; no prescribed-text quotation or analysis is supplied. Soliloquy staging is treated as variable, not an absolute rule. Teacher review must confirm terminology and classroom depth.'}},ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
lines=['# Literature in English — Form Four, Term One foundations','','| Row | Topic | By the end | Builds on | Leads to |','|---|---|---|---|---|']
lines += [f'| {n} | {title} | {goal} | {back} | {next_use} |' for n,title,goal,back,next_use in PATH]
lines += ['', 'Row 1 is diagnostic and excluded. Rows 3–18 and 20–38 await teacher feedback on prescribed texts and editions, as Dion requested. These foundations do not replace the novel or play study.']
(OUT/'LEARNING-PATH.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
