"""Form Five Logic Term One, including screen-based guided work."""
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import lessonlib as L
import banks_en as B
from lessonlib import card,worked,learn,num,mcq
L.use_class("form-5","Form 5")
OUT=L.ROOT/"logic"
SRC=["logic"]
PATH=[]

def F(term,meaning,case,error,why): return dict(term=term,meaning=meaning,case=case,error=error,why=why)
def item(q,r,wrong,why):
    assert len(wrong)==3
    return dict(q=q,r=r,w=[x[0] for x in wrong],e=[x[1] for x in wrong],y=why)
def qa(n,key,level,items): return B.QA(f"l5-{n}-{key}",level,"{X.q}",items,SRC)
def choose(n,rows,level=2,key="apply"):
    return qa(n,key,level,[item(q,r,list(zip(w,e)),why) for q,r,w,e,why in rows])
def word_order(n,sentences): return B.WO(f"l5-{n}-build",2,sentences,SRC)

def unit(n,title,goal,back,next_use,note,case,method,facts,applied,prereq=(),paper=None,extra=None,example=None,figure=None):
    assert 4 <= len(facts) <= 6
    terms=[]; cases=[]
    for i,f in enumerate(facts):
        other=[x for j,x in enumerate(facts) if j!=i][:3]
        terms.append(item("Which term means "+f["meaning"]+"?",f["term"],[(x["term"],"That concerns "+x["meaning"]+", rather than "+f["meaning"]+".") for x in other],f["why"]))
        cases.append(item(f["case"]+"\nWhich description best fits the selected feature?",f["term"],[(x["term"],"That means "+x["meaning"]+". The selected feature instead illustrates "+f["meaning"]+".") for x in other],f["why"]))
    q0=qa(n,"terms",1,terms); q1=qa(n,"cases",1,cases)
    q3=extra or B.MT(f"l5-{n}-link",2,"Match each term to its example.",[(f["term"],f["case"]) for f in facts],SRC,pick=3)
    q4=B.SP(f"l5-{n}-repair",3,"Find the incorrect logical claim.",[f["term"]+": "+f["meaning"]+"." for f in facts],[(f["error"],f["why"]) for f in facts],SRC)
    for st,f in zip(q4["pool"]["right"],facts): st["explain"]="This is correct: "+f["meaning"]+". Look for a claim that conflicts with a rule or distinction taught in Learn."
    questions=[q0,q1,applied,q3,q4]
    cards=[card(f"l5-{n}-c1","Distinguish the ideas used in this lesson.",[f["term"]+": "+f["meaning"]+"." for f in facts],q0["id"]),
       card(f"l5-{n}-c2","Read the whole example before identifying its function.",[f["case"] for f in facts],q1["id"]),
       card(f"l5-{n}-c3","A correction must preserve scope, terms and assumptions.",[f["error"]+" Correction: "+f["why"] for f in facts],q4["id"])]
    L.lesson("logic","logic",n,(f"l5-{n}",title),prereq,note,
       example or worked({},facts[0]["case"]+" Explain the selected feature.",[facts[0]["meaning"].capitalize()+".",facts[0]["why"]],facts[0]["term"]),cards,questions,paper=paper,
       learn=learn([("Your goal and connections","By the end, you should be able to "+goal+". Builds on: "+back+". Leads to: "+next_use+"."),
         ("Understand the pattern",note),(("Read the original model",case,json.dumps(figure)) if figure else ("Read the original model",case)),("Apply and check",method)],
         key_words=[(f["term"],f["meaning"]) for f in facts],mistake=(facts[0]["error"],facts[0]["term"]+": "+facts[0]["meaning"]+".",facts[0]["why"])))
    PATH.append((n,title,goal,back,next_use))

unit(1,'Arguments and reasoning','distinguish an offered inference from description or explanation and assess its intended strength',
 'Form Four statements, conditions and logical form','identifying premises, conclusions and indicators',
 'An argument offers claims as reasons to accept another claim. It need not be a quarrel or a successful proof. Deductive reasoning aims at a conclusion that cannot be false if its premises are true. Inductive reasoning supports a conclusion with a degree of confidence instead. An explanation can give a cause for an event already accepted, rather than evidence that it occurred. Context determines the intended purpose. Evaluating the inference differs from checking whether its premises are actually true.',
 'Original fictional rule: every reading-club voter holds a badge. Bih is a reading-club voter. Therefore Bih holds a badge. The stated premises support that conclusion. Reversing the rule would not establish that every badge holder votes. By contrast, Bih arrived late because the path was blocked may explain an accepted arrival, depending on context.',
 'Identify the claim the speaker wants accepted and the offered reasons. Ask whether the intended support is necessary or probable. For an explanation, check whether the event is already accepted. Then test the support separately from checking real-world facts.',[
 F('argument','claims offered as support for a conclusion','The badge rule and Bih’s voting status are reasons for her badge status.','An argument must be an angry disagreement.','Reasons can be offered calmly.'),
 F('deductive aim','an intention that true premises guarantee the conclusion','The voter rule and Bih’s voter status entail her badge status.','Every deductive attempt is automatically valid.','An aim can fail; the actual inference must be checked.'),
 F('inductive aim','support for a conclusion without a necessity claim','Past club meetings suggest the next may also be busy.','A repeated observation guarantees every future outcome.','Such support can leave room for exceptions.'),
 F('explanation','an account of why an accepted event happened','The blocked path explains an arrival already accepted as late.','The word because always makes a passage a proof of its conclusion.','Because can introduce a cause explaining an accepted event.')],choose(1,[
 ('Every club voter holds a badge; Bih is a voter; so she holds a badge. What support is intended?','Deductive support.',['A report of a quarrel.','Only an unrelated description.','An assertion that badges cause every vote.'],['No quarrel is described.','The claims are offered as reasons.','The rule does not express that causal claim.'],'The conclusion is required if the stated premises hold.'),
 ('Several earlier meetings were busy, so the next will probably be busy. What is the intended strength?','Probable rather than guaranteed support.',['A guarantee excluding every exception.','No conclusion is offered.','A contradiction by definition.'],['The wording is probable.','A future claim is offered.','No exact negation is asserted.'],'Earlier observations support an expectation without necessity.'),
 ('We already know the door closed. The speaker says it closed because a gust pushed it. What is the stated purpose?','Explain the accepted closure.',['Prove an event no one yet accepts.','Define every door as a gust.','Give a conclusion indicator with no cause.'],['The event is explicitly accepted.','The words do not define doors.','A cause is offered.'],'The context supplies the explanatory purpose.'),
 ('All club voters have badges. Ayuk has a badge. Therefore Ayuk is a voter. What is the problem?','The premises leave open badge holders who are not voters.',['The conclusion follows merely because it is last.','The first premise says all badge holders vote.','No conclusion appears.'],['Position does not establish support.','That reverses the stated rule.','The final claim is a conclusion.'],'The converse is not supplied.')]))

contexts=[('club voters','badge holders','Bih'),('reading-room volunteers','registered helpers','Ayuk'),('school-library books','catalogued items','the blue volume'),('club gardens','cultivated areas','the courtyard garden')]
parts=[]
for s,p,name in contexts:
    passage=f'All {s} are {p}. {name} belongs to the {s} class. Therefore {name} belongs to the {p} class.'
    parts.append((passage+' Which is the conclusion?',f'{name} belongs to the {p} class.',[f'All {s} are {p}.',f'{name} belongs to the {s} class.','Therefore'],['That is the general premise.','That is the case premise.','That is an indicator, not the complete claim.'],'The conclusion is the claim these reasons are offered to support.'))
unit(2,'Parts of an argument','extract complete premises and conclusion while separating background and inference',
 'arguments and intended support','indicators and later analysis of a whole passage',
 'Premises are the offered reasons; a conclusion is the claim they support. The inference is the move from reasons to that claim, not another quoted person or a punctuation mark. Background may explain the setting without functioning as a reason. A conclusion can come first, last or in the middle. Reconstruct complete claims and preserve their qualifications. Calling something a premise does not establish that it is true.',
 'Original passage: At a club meeting, Bih argues that the notice needs correction. The room is still provisional, but the notice calls it confirmed. Therefore its venue statement misrepresents the arrangement. The meeting location is background; the mismatch is the reason; the notice judgement is the conclusion.',
 'Underline the target claim, bracket each offered reason and mark contextual material separately. Rewrite each relevant claim as a full sentence without changing its scope. Ask how the premises are meant to support the target.',[
 F('premise','a claim offered as a reason','The room remains provisional supplies a reason for correction.','Every premise is guaranteed true because it is named a premise.','A role in an argument does not establish factual truth.'),
 F('conclusion','the claim offered reasons are meant to support','The venue statement misrepresents the arrangement is the target judgement.','A conclusion must be the passage’s final words.','Its role, not position, identifies it.'),
 F('inference','the reasoning move from premises to conclusion','The mismatch supports the correction judgement.','The word therefore alone is the complete conclusion.','The conclusion is a claim; therefore signals the move.'),
 F('background','context not serving as an offered reason in the case','The meeting location sets the scene without supporting the correction.','Every detail in a passage must be a premise.','Some details provide context rather than support.')],choose(2,parts),[1])

unit(3,'Premise and conclusion indicators','interpret indicator expressions by their role in context rather than spotting words mechanically',
 'argument parts and complete claims','opposition and reconstruction of reasoning',
 'Because, given that and since can introduce premises; therefore, thus and so can introduce conclusions. These are clues, not guarantees. Since can mark elapsed time; so can intensify a description. Arguments may omit indicators entirely. Identify what is offered as support and what is meant to follow. Changing an indicator without checking its role can reverse the argument.',
 'Original examples: The venue needs checking because it remains provisional. Here because introduces a reason. The venue remains provisional; therefore the notice should not call it confirmed. Here therefore introduces a conclusion. Bih has waited since Monday uses since temporally, not as a premise indicator.',
 'Read the whole passage. Replace an apparent premise cue with given that and test the relation; replace a conclusion cue with it follows that. Treat those substitutions as meaning checks rather than automatic proofs of validity.',[
 F('premise cue','an expression introducing an offered reason','Because it remains provisional introduces the reason.','Because always introduces the conclusion being supported.','In this argumentative use it introduces the reason.'),
 F('conclusion cue','an expression introducing the claim meant to follow','Therefore the notice needs correction introduces the target.','Therefore proves an argument valid by its spelling.','An indicator marks intention rather than guaranteeing support.'),
 F('contextual interpretation','identifying an expression’s actual use','Since Monday marks time, not an offered reason.','Since always signals a premise whatever its use.','The temporal phrase is a counterexample.'),
 F('unmarked inference','reasoning expressed without an explicit indicator','The room is provisional. Calling it confirmed misleads readers.','A passage without therefore can never contain reasoning.','A support relation can be conveyed without an indicator.')],choose(3,[
 ('Correct the notice because the venue is provisional. What follows because?','The offered reason.',['A date expression.','The correction conclusion.','A guarantee of truth.'],['No time phrase follows it.','Correction is the supported proposal.','An indicator guarantees no truth.'],'Because introduces the premise here.'),
 ('The venue is provisional; thus the notice needs checking. What follows thus?','The intended conclusion.',['The entire set of premises.','A temporal starting point.','An unrelated adjective.'],['The reason precedes thus.','Thus does not name a starting day.','A complete claim follows it.'],'The checking claim is meant to follow.'),
 ('Bih has waited since Monday. What does since do?','Introduce a temporal starting point.',['Introduce an argumentative premise.','Guarantee a conclusion.','Negate every statement.'],['The phrase supplies time, not an offered reason.','There is no supported conclusion here.','Since is not a negation.'],'Read its temporal use.'),
 ('All voters have badges. Bih votes. Bih has a badge. No indicator appears. Which assessment is accurate?','The final claim can still be presented as following from the earlier claims.',['No reasoning is possible without therefore.','Every sentence is an isolated question.','The last claim must be a premise solely because it is last.'],['Indicators are optional clues.','These are assertions.','Position alone does not identify a role.'],'The support relation can be reconstructed.')]),[1,2])

FORMS=[('A','All S are P.'),('E','No S are P.'),('I','Some S are P.'),('O','Some S are not P.')]
relations=[('A and O','contradictory','They cannot share a truth value under the stated standard meanings.'),('E and I','contradictory','They cannot share a truth value under the stated standard meanings.'),('A and E, with S nonempty','contrary','They cannot both be true, but a mixed subject class makes both false.'),('I and O, with S nonempty','subcontrary','They cannot both be false, but a mixed subject class makes both true.')]
relationq=choose(4,[(f'Classify the relation: {pair}.',rel,[other for other in ['contradictory','contrary','subcontrary','unrelated'] if other!=rel],[{'contradictory':'Contradictories must always differ in truth value.','contrary':'Contraries cannot both be true but may both be false.','subcontrary':'Subcontraries cannot both be false but may both be true.','unrelated':'The specified forms have a taught opposition relation.'}[other] for other in ['contradictory','contrary','subcontrary','unrelated'] if other!=rel],why) for pair,rel,why in relations])
unit(4,'Opposition as immediate inference','identify opposition relations without changing the subject, predicate or existence assumptions',
 'argument parts and Form Four categorical forms','using the square to infer truth values',
 'Opposition compares categorical claims with the same subject S and predicate P. A says all S are P; E says no S are P; I says some S are P; O says some S are not P. Some means at least one. Under the standard set-based meanings, A/O and E/I are contradictory even when S is empty. For the full classroom square here, explicitly assume S exists. Then A/E are contrary and I/O subcontrary. Do not silently change terms or assume existence from an all-claim alone.',
 'Original model: S means club members and P means badge holders in one fixed fictional club. If members exist and some hold badges while others do not, A and E are false while I and O are true. If no members exist, the standard set-based A and E are both true; I and O are false. This second case shows why the full square needs an existence assumption.',
 'Write A/E/I/O in words, hold the terms fixed and state whether S is assumed nonempty. Distinguish cannot both be true from cannot both be false. The spine title is truncated; this draft teaches opposition as a mode of immediate inference, subject to teacher terminology review.',[
 F('fixed terms','the same subject and predicate meanings in a comparison','Compare club members and badge holders throughout.','Changing S into teachers leaves the same opposition pair.','Changing the class changes the compared claims.'),
 F('contradictory','a relation whose paired claims always differ in truth value','A and O are contradictories under the stated meanings.','A and O may both be false under these meanings.','O asserts exactly the counterexample that denies A.'),
 F('contrary with existence','the A/E relation when S is assumed nonempty','All members have badges and no members have badges cannot both be true if members exist.','A and E cannot both be true even if no S exist under the standard meanings.','With empty S both universals are true in the stated set-based interpretation.'),
 F('subcontrary with existence','the I/O relation when S is assumed nonempty','A mixed membership makes I and O both true.','I and O cannot both be true.','A mixed class supplies a witness for each.')],relationq,[1,2,3])

def square():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 280" role="img" aria-label="Square of opposition assuming S exists. A and E contrary; I and O subcontrary; diagonals contradictory; downward arrows show subalternation."><rect width="320" height="280" fill="#fff"/><g stroke="#28533d" fill="none" stroke-width="2"><path d="M55 70H265M55 210H265M55 80L265 200M265 80L55 200"/><path d="M40 85V192l-5 -8m5 8 5 -8M280 85V192l-5 -8m5 8 5 -8"/></g><g fill="#172d22" font-family="sans-serif" text-anchor="middle"><text x="160" y="20" font-size="16">Assume S exists</text><text x="55" y="47" font-size="22">A</text><text x="265" y="47" font-size="22">E</text><text x="160" y="63" font-size="14">contrary</text><rect x="84" y="126" width="152" height="26" fill="white"/><text x="160" y="144" font-size="15">contradictory</text><text x="55" y="240" font-size="22">I</text><text x="265" y="240" font-size="22">O</text><text x="160" y="230" font-size="14">subcontrary</text><text x="160" y="267" font-size="12">Down: A to I, E to O</text></g></svg>'''

# Counts in the two S regions determine truth, not a typed answer bank.
truthvars={'a':{'int':[0,4]},'b':{'int':[0,4]},'X':{'pick':[{'code':'A','text':'All S are P.'},{'code':'E','text':'No S are P.'},{'code':'I','text':'Some S are P.'},{'code':'O','text':'Some S are not P.'}]}}
def truthq(n,key='model',nonempty=False):
    return B.mcq(f'l5-{n}-{key}',2,'Invented complete model: {a} S are inside P and {b} S are outside P. There are no other S. Assess {X.code}: {X.text}',
      '{(X.code=="A" ? b==0 : X.code=="E" ? a==0 : X.code=="I" ? a>0 : b>0) ? "True in this model." : "False in this model."}',
      [('{(X.code=="A" ? b==0 : X.code=="E" ? a==0 : X.code=="I" ? a>0 : b>0) ? "False in this model." : "True in this model."}','reverse'),('Undetermined from these complete counts.','unknown'),('It has no truth value because some is an exact total.','some')],
      ['Some means at least one. A has no S outside P; E has no S inside P.','Here A is {b==0}, E is {a==0}, I is {a>0} and O is {b>0}.','The requested claim is {answer}'],vars=truthvars,where=['a+b>0'] if nonempty else [],
      misc=[('reverse','That reverses the result of checking the relevant region.'),('unknown','Both S regions and completeness are supplied, so this claim can be assessed.'),('some','Some asserts existence, not an exact total; the supplied counts still determine truth.')],sources=SRC)

unit(5,'Squares of opposition','use opposition and subalternation while distinguishing false from undetermined',
 'categorical meanings and opposition relations','guided square problems and eduction',
 'With S assumed nonempty, A implies I and E implies O: these downward inferences are subalternation. Falsity travels upward from I to A and O to E. A false universal does not determine its contrary, and a true particular does not establish its corresponding universal. Undetermined means the supplied information permits either truth value; it does not mean false. If S can be empty, use the standard meanings directly and retain only the contradictory diagonals without extra existence information.',
 'Original model: if some club members have badges, I is true. That alone leaves A undetermined: all members might have badges, or some might not. If A is true and members exist, I is true. In a complete counted model, inspect both regions: {2} members inside P and {1} outside P make A false, E false, I true and O true.',
 'State the existence convention, identify the given form and truth value, then use only a licensed direction. Test an uncertain case by describing alternatives. Counts supplied as a complete model can settle more than a single square premise.',[
 F('subalternation','downward truth inference with S explicitly nonempty','A true plus existing S gives I true.','A true guarantees I true without any existence condition.','An empty subject is the counterexample under standard meanings.'),
 F('upward falsity','inference from a false particular to its false universal','I false implies A false when S exists.','A false always makes I false.','A mixed subject makes A false but I true.'),
 F('undetermined','either truth value remains possible from the given information','I true alone leaves A open.','Undetermined is just another word for false.','Incomplete information differs from a false claim.'),
 F('empty subject check','testing whether an existence assumption is available','Empty S gives A and E true, I and O false under the stated meanings.','A universal statement automatically provides an existing member.','Universals do not alone assert existence in this convention.')],truthq(5),[4],figure=square())

unit(6,'Guided work: checking a square-of-opposition record','construct a complete counted model and use it to detect an unjustified square inference',
 'square relations and existence conditions','conversion, obversion and checking transformations',
 'Work with an invented finite class on paper or on this screen. Separate S members inside P from S members outside P and state that these counts cover all S. Record A, E, I and O by their definitions before consulting the square. A mixed class supplies useful counterexamples to false upward inferences. An empty class tests whether existence was silently assumed. These are logical models, not a survey of actual pupils.',
 'Original record: {3} S are P and {2} S are not P; no other S exist. I and O are true because each region contains members. A and E are false because each has a counterexample. A pupil’s claim that I true forces A true fails in this same model. Next change the outside count to {0}: now A is true, while the remaining inside count keeps I true.',
 'Prepare columns for inside/outside counts and the truth of A/E/I/O. Try a mixed, all-inside, all-outside and empty model. Compare a proposed inference with each record; a true premise and false conclusion gives a counterexample.',[
 F('complete record','counts covering every S in the invented model','The model states there are no other S.','Unreported S can be added while still calling the supplied model complete.','Completeness fixes the whole subject class.'),
 F('mixed model','existing S both inside and outside P','Positive counts in both regions make I and O true.','A mixed model makes A true.','An outside member refutes A.'),
 F('counterexample model','a model with a true premise and false proposed conclusion','I true with A false refutes an unrestricted I-to-A inference.','A false premise and true conclusion alone refute validity.','Invalidity needs premises true and conclusion false.'),
 F('recorded assumption','an explicit condition governing a model’s use','Mark whether S exists before applying the full square.','An existence condition may be omitted without affecting every inference.','Some square directions depend on existence.')],truthq(6),[4,5],figure=square(),example=worked({},'Test I true therefore A true using {3} S inside P and {2} outside P.',
 ['The inside count {3} makes I true.','The outside count {2} supplies a counterexample to A.','So the premise is true and conclusion false in this complete model.'],'The inference fails.'))

conversion=[]
for s,p,name in contexts:
    for code in ['E','I']:
        start=f'No {s} are {p}.' if code=='E' else f'Some {s} are {p}.'
        result=f'No {p} are {s}.' if code=='E' else f'Some {p} are {s}.'
        conversion.append((f'Give the simple converse of this claim under the stated standard meanings: {start}',result,
          [f'All {p} are {s}.',f'Some {p} are not {s}.',f'All {s} are {p}.'],
          ['That introduces a universal affirmative not supplied by this converse.','That changes to a negative particular rather than preserving the taught converse.','That does not perform the required switch and changes the stated form.'],
          'E and I preserve truth when their complete subject and predicate terms are exchanged.'))
unit(7,'Eduction and simple conversion','transform a categorical claim by a licensed operation and reject an unsupported converse',
 'opposition, complete terms and counterexample models','obversion and chains of immediate inference',
 'Eduction here means deriving a categorical claim from a single categorical premise by transforming terms or quality. Simple conversion exchanges the complete subject and predicate. It preserves truth for E and I under the stated standard meanings. A does not convert simply: all voters may hold badges without every badge holder voting. With an explicit existing subject, A supports conversion by limitation to some P are S. O does not generally convert. Distinguish a truth-preserving equivalence from a weaker consequence requiring existence.',
 'Original model: No club voters are unregistered persons converts to No unregistered persons are club voters. Some volunteers are readers converts to Some readers are volunteers. All voters are badge holders does not give All badge holders are voters. If at least one voter exists, it does give Some badge holders are voters.',
 'Mark complete S and P, exchange them and keep the original quantity and quality for simple conversion. Check whether the original form permits it. For a limited A consequence, state the existence premise and avoid claiming full equivalence.',[
 F('simple conversion','exchange of complete subject and predicate terms','No S are P becomes No P are S.','Conversion means changing only the predicate to non-P.','That describes part of obversion, not switching terms.'),
 F('E and I equivalence','truth preservation for the two simply convertible forms','Some S are P is equivalent to Some P are S.','Every categorical form converts simply.','A and O have counterexamples.'),
 F('invalid universal converse','an unsupported reversal of an A statement','All voters have badges does not imply all badge holders vote.','All S are P always means All P are S.','P can contain additional members outside S.'),
 F('conversion by limitation','a particular converted consequence of A when S exists','All S are P plus existing S implies Some P are S.','The universal alone proves an existing witness in the stated convention.','An existence premise is needed.')],choose(7,conversion),[4,5,6])

def categorical(code,s,p):
    return {'A':f'All {s} are {p}.','E':f'No {s} are {p}.','I':f'Some {s} are {p}.','O':f'Some {s} are not {p}.'}[code]
obversions=[]
for s,p,name in contexts:
    for code,target in [('A','E'),('E','A'),('I','O'),('O','I')]:
        start=categorical(code,s,p); result=categorical(target,s,'non-('+p+')')
        obversions.append((f'Obvert this claim. Here non-({p}) means every item outside the {p} class in the fixed universe. {start}',result,
          [categorical(code,s,'non-('+p+')'),categorical(target,s,p),categorical(target,p,'non-('+s+')')],
          ['The predicate is complemented but quality is not changed.','Quality changes but the predicate complement is missing.','That swaps terms instead of retaining the original subject.'],
          'Retain subject and quantity, change affirmative/negative quality and complement the whole predicate.'))
unit(8,'Obversion','obvert each categorical form by changing quality and complementing the whole predicate',
 'categorical forms, conversion and fixed terms','complex eduction without changing a claim’s scope',
 'Obversion retains the subject and quantity, changes affirmative to negative or negative to affirmative, and replaces the complete predicate by its complement. The complement contains exactly what is outside that class within a fixed universe. Under the standard set-based meanings used here, all the categorical forms are equivalent to their obverses. Complement is not merely an everyday opposite: non-red does not mean only blue. Double complementation restores the original class.',
 'Original models: All S are P becomes No S are non-P. No S are P becomes All S are non-P. Some S are P becomes Some S are not non-P. Some S are not P becomes Some S are non-P. For club members and badge holders, non-(badge holders) means all items outside the badge-holder class within the stated universe.',
 'Keep S fixed. Circle the original quality and change it, retain all or some scope, then complement the entire P term. Check that you have not merely negated the whole sentence. Use the fixed-universe meaning of non-P, not a narrow everyday opposite.',[
 F('retained subject','the unchanged subject term in an obverse','S stays the subject when All S are P is obverted.','Obversion requires exchanging S and P.','The subject remains fixed; conversion exchanges terms.'),
 F('changed quality','the affirmative/negative switch in obversion','A becomes E while I becomes O.','Complementing P alone completes obversion.','Quality must also change.'),
 F('term complement','everything outside a class in the fixed universe','Non-red includes all non-red items, not just blue ones.','The complement of red is exactly blue in every universe.','Many things can be neither red nor blue.'),
 F('retained quantity','preservation of universal or particular scope','Some remains some in the obverse.','Obverting a universal alone creates a particular witness.','Changing quality and predicate does not add existence.')],choose(8,obversions),[7])

chains=[]
for s,p,name in contexts:
    for code in ['A','O']:
        target=categorical(code,'non-('+p+')','non-('+s+')')
        chains.append((f'Under standard set-based meanings, give the truth-equivalent contrapositive: {categorical(code,s,p)}',target,
          [categorical(code,p,s),categorical(code,'non-('+s+')','non-('+p+')'),categorical('E' if code=='A' else 'I','non-('+p+')','non-('+s+')')],
          ['This swaps terms but omits both complements.','This complements but does not exchange the terms.','That changes the required quantity/quality form.'],
          'For A and O, exchange the terms and complement each; preserve the categorical form.'))
unit(9,'Complex modes of eduction','justify a chain of licensed transformations and distinguish contraposition from a converse',
 'simple conversion, obversion and existence conditions','analysing complete passages without changing their claims',
 'A complex transformation can combine simpler truth-preserving steps. For A, obvert to E, convert that E, then obvert again: All S are P becomes All non-P are non-S. The analogous chain works for O through an I intermediate. This is contraposition. Under the standard meanings, A and O are equivalent to their contrapositives; E and I are not generally equivalent to theirs. Do not assume every operation is licensed merely because the final wording looks familiar.',
 'Original A chain: All S are P; No S are non-P; No non-P are S; All non-P are non-S. Original O chain: Some S are not P; Some S are non-P; Some non-P are S; Some non-P are not non-S. Each middle conversion is licensed because its form is E or I. Non-(non-S) denotes S in the fixed universe.',
 'Write every intermediate line and name its operation. Check the form before conversion and preserve the complement’s entire term. A failed intermediate equivalence cannot be rescued by labelling the whole chain complex. Ask the teacher which additional historical eduction names the examination requires.',[
 F('licensed chain','successive transformations each justified for its form','The A chain converts an E intermediate.','Any sequence of operations preserves truth automatically.','Each step needs an applicable rule.'),
 F('contraposition','exchange of terms with both complemented','All S are P becomes All non-P are non-S.','Contraposition merely exchanges S and P.','That gives the converse and omits complements.'),
 F('A and O restriction','the general equivalence scope for contraposition here','A and O preserve truth under the stated contraposition.','E and I always preserve truth under the same operation.','Those forms have counterexamples under standard meanings.'),
 F('double complement','return to the original class after complementing twice','Non-(non-S) denotes S in the fixed universe.','Non-(non-S) always denotes a smaller arbitrary class.','Taking the outside twice restores the class.')],choose(9,chains),[7,8])

analysisrows=[]
for s,p,name in contexts:
    analysisrows.append((f'At an imaginary club discussion, a speaker says: We should not infer that {name} belongs to the {s} class merely from membership in the predicate class. Our actual rule is only that all {s} are {p}. Knowing that {name} is among {p} does not exclude other kinds of {p}. What is the speaker’s central conclusion?',
      f'Membership of {p} alone does not establish that {name} belongs to {s}.',
      [f'All {p} are {s}.',f'{name} definitely cannot belong to {s}.','Every detail about the discussion is an offered logical premise.'],
      ['That is the very reversed rule being rejected.','Failure to establish membership does not establish non-membership.','Setting details need not support the target claim.'],
      'The passage rejects an inference while leaving the actual membership open.'))
unit(10,'Identifying argument parts in a passage','reconstruct a qualified conclusion and its supporting reason without adding a stronger claim',
 'argument roles, indicators and transformation limits','later assessment of syllogisms and argumentative prose',
 'A whole passage can mix background, a quoted view, a reason and a qualified conclusion. Identify whose claim each sentence expresses. Preserve terms such as may, not established and only: dropping them can strengthen or reverse the conclusion. Rejecting a proposed proof does not prove its opposite. Reconstruct the offered support before judging whether it succeeds. An argument map should show the role of each relevant claim rather than merely copying the passage in order.',
 'Original passage: During a fictional discussion, Manka says that a badge alone does not prove someone is a voter. The rule says every voter has a badge, but other people may also have one. She does not claim that no badge holder votes. Reconstruction: the rule permits badges beyond voters; therefore badge possession alone does not establish voter status. The discussion setting is background.',
 'Mark the central qualified claim, list the relevant reasons and keep contextual or quoted material distinct. Paraphrase faithfully, then test support. State whether the conclusion rejects an inference, asserts a fact or recommends an action.',[
 F('qualified target','a conclusion preserved with its actual limits','Badge possession alone does not prove voter status.','The conclusion says no badge holder can ever vote.','That changes lack of proof into a universal exclusion.'),
 F('supporting distinction','the reason separating the rule from its converse','The badge class may include non-voters.','A possible extra badge holder proves every badge holder is a non-voter.','A possibility defeating an inference does not prove that opposite universal.'),
 F('view attribution','identification of whose claim is being presented','Manka rejects the inference in the fictional discussion.','Every quoted view must be endorsed by the writer.','A passage can report a view to question it.'),
 F('faithful reconstruction','restatement preserving roles and scope','List the reason before the limited conclusion without changing either.','Reordering an argument permits inventing stronger premises.','Reconstruction clarifies existing support rather than fabricating it.')],choose(10,analysisrows),[1,2,3,7,8,9])

OUT.mkdir(parents=True,exist_ok=True)
(OUT/'sources.json').write_text(json.dumps({'logic':{
 'ref':'Original fictional argument banks and independently constructed finite-class models; OpenStax argument analysis; Stanford Encyclopedia square/existence discussion; Knachel and Sander-Staudt logical-equivalence chapter',
 'urls':['https://openstax.org/books/introduction-philosophy/pages/5-3-arguments','https://plato.stanford.edu/entries/square/','https://mlpp.pressbooks.pub/msander/chapter/chapter-8-operations-for-logical-equivalencies-conversion-obversion-and-contra-position/'],
 'checked':'Consulted 2026-10-24. Existence conventions are explicit: standard set-based meanings throughout, full square relations only with nonempty S. Finite-class models and transformation exercises are independently constructed, not copied textbook examples. A search-result LibreTexts passage contains inconsistent labels for contraposition; those labels are not followed. Teacher must confirm the truncated row 4 title, local eduction terminology and the examination convention.'}},ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
lines=['# Form Five Logic — learning path','','Each opening states a measurable goal and its connections.','','| Row | Topic | By the end | Builds on | Leads to |','|---|---|---|---|---|']
lines += [f'| {n} | {title} | {goal} | {back} | {next_use} |' for n,title,goal,back,next_use in sorted(PATH)]
lines += ['','Rows 1–10 include nine teaching rows and guided work 6, which is possible on screen. No diagnostic is listed.','','Overall destination: reconstruct an argument faithfully and test immediate inferences without changing terms, scope or existence assumptions.']
(OUT/'LEARNING-PATH.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(OUT/'TEACHER-REVIEW.md').write_text('''# Form Five Logic — teacher review

- TR-logic-1: Confirm the truncated row 4 title, Opposition as a Mood of Immediate. This draft teaches opposition as a mode of immediate inference within its supplied chapter, without changing the spine.
- TR-logic-2: Confirm examination conventions for existential import. The resources explicitly use standard set-based A/E/I/O meanings; the full square is used only with existing S. They do not merge this with all historical readings discussed by the reference.
- TR-logic-3: Confirm local eduction names and expected complex modes. Drafts cover E/I conversion, A conversion by limitation with existence, obversion, and A/O contraposition through licensed chains. Additional historical terms require teacher direction.
- TR-logic-4: All institutional rules, people and class models are fictional. Guided work 6 is a finite-class recording exercise, not an actual pupil survey. Check pace and the transition from letters to ordinary prose.
- TR-logic-5: Verify accepted alternative reconstructions, diagram conventions and the distinction between failing to establish a claim and proving its negation. Technical checks do not constitute teacher approval or classroom outcome evidence.
''',encoding='utf-8')
assert len(PATH)==10 and {n for n,*_ in PATH}==set(range(1,11))
