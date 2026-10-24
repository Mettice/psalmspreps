"""Français intensif Form Five Term One: language drafts; prescribed books pending teacher feedback."""
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import lessonlib as L
import banks_fr as B
L.use_class('form-5','Form 5')
OUT=L.ROOT/'francais-intensif'
SRC=['francais']
PATH=[]
def F(term,meaning,case,error,why): return dict(term=term,meaning=meaning,case=case,error=error,why=why)
def item(q,r,w,y):
    assert len(w)==3
    return dict(q=q,r=r,w=[a for a,b in w],e=[b for a,b in w],y=y)
def qa(n,key,level,bank,**kw): return B.QA(f'fi5-{n}-{key}',level,'{X.q}',bank,SRC,**kw)
def choose(n,rows,key='appliquer',level=2):
    return qa(n,key,level,[item(q,r,list(zip(w,e)),y) for q,r,w,e,y in rows])
def unit(n,title,goal,back,onward,note,model,method,facts,applied,prereq=(),paper=None,extra=None,figure=None,example=None):
    assert 4<=len(facts)<=6
    defs=[]; cases=[]
    for i,f in enumerate(facts):
        others=[x for j,x in enumerate(facts) if j!=i][:3]
        defs.append(item('Quel terme désigne '+f['meaning']+' ?',f['term'],[(x['term'],'Cela désigne '+x['meaning']+', plutôt que la notion demandée.') for x in others],f['why']))
        cases.append(item(f['case']+'\nQuelle notion convient ?',f['term'],[(x['term'],'Cela concerne '+x['meaning']+'. Compare cette définition avec le cas présenté.') for x in others],f['why']))
    q0=qa(n,'notions',1,defs); q1=qa(n,'cas',1,cases)
    q3=extra or B.MT(f'fi5-{n}-relier',2,'Relie chaque notion à son exemple.',[(f['term'],f['case']) for f in facts],SRC,pick=3)
    q4=B.SP(f'fi5-{n}-corriger',3,'Repère la formulation ou l’affirmation incorrecte.',[f['term']+' : '+f['meaning']+'.' for f in facts],[(f['error'],f['why']) for f in facts],SRC)
    for st,f in zip(q4['pool']['right'],facts): st['explain']='Cette distinction est correcte : '+f['why']+' Cherche plutôt une phrase qui contredit le sens ou la règle.'
    sections=[('Ton objectif et les liens','À la fin, tu pourras '+goal+'. Acquis mobilisés : '+back+'. Pour la suite : '+onward+'.'),('Comprendre la règle ou le sens',note),('Lire le modèle original',model),('Appliquer et vérifier',method)]
    if figure: sections[2]=(*sections[2],figure)
    L.lesson('francais-intensif','francais-intensif',n,(f'fi5-{n}',title),prereq,note,
      example or L.worked({},facts[0]['case']+' Explique le choix.',[facts[0]['meaning']+'.',facts[0]['why']],facts[0]['term']),
      [L.card(f'fi5-{n}-c1','Distingue les notions avant de choisir.',[f['term']+' : '+f['meaning']+'.' for f in facts],q0['id']),
       L.card(f'fi5-{n}-c2','Lis le contexte avant de nommer la notion.',[f['case'] for f in facts],q1['id']),
       L.card(f'fi5-{n}-c3','Corrige sans changer le sens voulu.',[f['error']+' Correction : '+f['why'] for f in facts],q4['id'])],
      [q0,q1,applied,q3,q4],paper=paper,lang='fr',learn=L.learn(sections,key_words=[(f['term'],f['meaning']) for f in facts],mistake=(facts[0]['error'],facts[0]['meaning']+'.',facts[0]['why'])))
    PATH.append((n,title,goal,back,onward))

def reuse(n,folder,subject,old,prefix,title,goal,back,onward,prereq):
    obj=json.loads((L.CONTENT/folder/subject/f'{old}.json').read_text(encoding='utf-8'))
    obj=json.loads(json.dumps(obj,ensure_ascii=False).replace(f'{prefix}-{old}',f'fi5-{n}'))
    def sources(x):
        if isinstance(x,dict):
            for k,v in x.items():
                if k=='sources':x[k]=SRC[:]
                else:sources(v)
        elif isinstance(x,list):
            for v in x:sources(v)
    sources(obj)
    obj.update(lesson_no=n,subject='francais-intensif',**{'class':'Form 5'},prerequisites=prereq)
    obj['skills'][0]['name']=title
    obj['learn']['sections'][0]['text']='À la fin, tu pourras '+goal+'. Acquis mobilisés : '+back+'. Pour la suite : '+onward+'.'
    L.write('francais-intensif',n,obj);PATH.append((n,title,goal,back,onward))

reuse(6,'form-4','francais-intensif',4,'fi4','Préparer une prise de parole dans une situation familiale fictive','développer une proposition respectueuse avec une raison et une reformulation','le sens contextuel, les raisons et les conséquences','l’écriture d’une scène et la cohérence des échanges',[1,2,3])
reuse(9,'form-4','french',1,'fr4','Lexique de la vie familiale et de l’intégration sociale','décrire une situation sociale avec des mots précis sans inférer la valeur d’une personne','la parole contextualisée et la formation des mots','comparaisons et lecture de situations familiales',[1,3,6,7])
reuse(11,'form-4','francais-intensif',45,'fi4','Le degré de l’adjectif : comparaisons irrégulières','choisir meilleur ou pire selon le nom et distinguer les degrés comparatifs','qualifications et lexique de la vie sociale','description appuyée et comparaison avec l’adverbe',[9])
reuse(13,'form-5','french',22,'fr5','Le subjonctif présent : formation et emploi','former le subjonctif étudié et distinguer une construction de souhait d’un simple constat','formes verbales et phrase complexe de la classe précédente','propositions et écrits développés',[3,7,11])
reuse(16,'form-5','french',15,'fr5','Les mots empruntés','distinguer origine attestée, sens actuel et intégration d’un emprunt','dérivation, composition et lexique social','traduction fidèle et homophones',[1,9,15])
reuse(17,'form-5','french',11,'fr5','Traduire de courts textes familiaux et communautaires','préserver sujet, destinataire et action accomplie dans une traduction','pronominalisation, formes composées et lexique social','comparaison des temps du récit',[7,9,13,16])
reuse(21,'form-5','french',6,'fr5','Voir, voire, voix et voie : sens et graphie','choisir une graphie en expliquant la construction et la paraphrase','classes de mots, emprunts et traduction','interprétation d’image et lettre formelle',[1,2,16,19])
reuse(23,'form-4','french',4,'fr4','Préparer l’interprétation d’une image de vie sociale','appuyer une description sur les indices visibles et distinguer une intention non montrée','dialogues et sens des mots','écriture d’une demande formelle',[6,15,21])
reuse(28,'form-4','french',17,'fr4','Lexique de la protection de l’environnement','choisir un terme environnemental et distinguer projet de protection et résultat observé','sources, description et formulation d’une demande','vocabulaire de santé et lecture critique',[16,23,24])
reuse(34,'form-4','french',21,'fr4','Lexique de la santé','distinguer métier, lieu de soins et vocabulaire de santé sans poser de diagnostic','lexique de l’environnement et précision du sens','lecture d’un passage et traduction de messages',[28,29,33])
reuse(38,'form-5','french',25,'fr5','Lire un passage sur l’eau et l’information','distinguer définition, analyse absente et projet de communication dans un passage','santé, environnement et lecture d’indices','image, lieu décrit et message traduit',[28,34,36])
reuse(39,'form-5','french',19,'fr5','Préparer l’interprétation d’images environnementales','décrire un indice et justifier une interprétation en signalant les informations absentes','lexique environnemental et lecture critique','description de lieu et écriture à partir d’image',[28,34,38])
reuse(41,'form-4','francais-intensif',32,'fi4','Imparfait et passé composé','former les temps et justifier un arrière-plan ou un événement accompli dans le modèle','participes, temps du récit et indices contextuels','description de lieu et récit développé',[7,19,38,39])

# Original definitions and applied banks below complement the explicit foundation adaptations.
def vocab(n,title,goal,back,onward,note,model,facts,gaps,prereq=()):
    bank=[]
    for text,term in gaps:
        target=next(f for f in facts if f['term']==term)
        other=[f for f in facts if f['term']!=term][:3]
        bank.append(item(text+'\nQuelle notion convient ?',term,[(f['term'],'Cela concerne '+f['meaning']+', plutôt que '+target['meaning']+'.') for f in other],target['why']))
    unit(n,title,goal,back,onward,note,model,'Lis le contexte, explique le trait de sens et vérifie une paraphrase. Réemploie ensuite le mot dans une phrase originale sans ajouter de conclusion absente.',facts,qa(n,'contexte',2,bank),prereq)

def writing(n,title,goal,back,onward,note,model,facts,prompt,prereq,figure=None):
    unit(n,title,goal,back,onward,note,'Extrait du modèle original : '+model[0],
      'Identifie le destinataire, le but et les indices disponibles. Organise les idées avant de rédiger. Vérifie chaque détail, distingue observation et ajout fictif annoncé, puis relis accords, reprises et temps.',facts,
      B.WO(f'fi5-{n}-construire',2,[f['case'] for f in facts],SRC),prereq,
      paper=dict(vars={},checks=[],prompt=prompt,model=model,checklist=[f['term']+' : '+f['meaning']+'.' for f in facts]+['Vérifier les accords, les reprises et la cohérence des temps.']),figure=figure)

unit(1,'Formation des mots : dérivation et composition','expliquer la formation d’un mot sans confondre affixe, base et mot composé',
 'classes de mots et familles de la classe précédente','homophones et lexique des relations sociales',
 'La dérivation forme un mot à partir d’une base et d’un affixe. Un préfixe se place devant la base ; un suffixe après elle et peut changer la classe du mot. La composition associe des éléments formant une unité lexicale, comme chou-fleur ou pomme de terre. Tout groupe de mots n’est pas automatiquement un composé, et une ressemblance ne suffit pas à établir une famille. Analyse structure et sens avant de généraliser une règle de formation.',
 'Modèles originaux : relire associe re- à lire ; rangement associe une base verbale à un suffixe nominal. Chou-fleur est un composé, tandis que cahier bleu est ici un groupe descriptif ordinaire. La présence d’un trait d’union aide parfois à repérer une structure, mais tous les composés n’en ont pas.',
 'Repère les éléments, précise leur rôle et compare le sens du mot obtenu. Vérifie sa classe dans une phrase. Ne remplace pas une analyse par le seul comptage des lettres ou des traits d’union.',[
 F('préfixation','l’ajout d’un affixe devant la base','Relire associe re- à lire.','Tout préfixe se place après la base.','Un préfixe précède la base.'),
 F('suffixation','l’ajout d’un affixe après la base','Rangement emploie un suffixe nominal.','Un suffixe ne peut jamais changer la classe d’un mot.','Des suffixes forment des noms à partir d’autres bases.'),
 F('composition','l’association d’éléments en une unité lexicale','Chou-fleur est un composé.','Tous les composés doivent avoir exactement le même sens que chaque élément isolé.','Le sens de l’ensemble doit être vérifié.'),
 F('analyse contextuelle','la vérification du sens et de la classe dans une phrase','Cahier bleu est ici un groupe descriptif ordinaire.','Tout groupe contenant un adjectif est automatiquement un nom composé.','La structure lexicale et le contexte doivent être examinés.')],choose(1,[
 ('Dans relire, quelle analyse est pertinente ?','Re- est placé avant la base lire.',['Re- est obligatoirement un suffixe final.','Lire est une marque de pluriel.','Le mot contient nécessairement deux noms complets.'],['Il précède la base.','Lire fournit la base verbale.','Ce modèle est dérivé.'],'Identifie position et rôle.'),
 ('Dans rangement, que fait le suffixe étudié ?','Il contribue à former un nom sur une base verbale.',['Il indique toujours un futur.','Il remplace toute la phrase par une ponctuation.','Il prouve qu’aucun lien de sens n’existe.'],['Ce n’est pas une terminaison de futur.','Le mot formé est lexical.','La dérivation entretient un lien à analyser.'],'La classe du mot obtenu compte.'),
 ('Pourquoi pomme de terre peut-il être un composé sans trait d’union ?','Une unité lexicale peut comprendre plusieurs éléments non reliés par des traits.',['Le trait est obligatoire dans tous les composés.','Terre doit toujours être conjugué.','Tous les groupes libres deviennent composés.'],['L’exemple montre une autre structure.','Terre est un nom ici.','L’unité lexicale doit être établie.'],'Le signe graphique n’est pas le seul critère.'),
 ('Quel contrôle évite une famille de mots inventée ?','Vérifier le lien de formation et de sens.',['Choisir seulement les mots de même longueur.','Compter uniquement les voyelles.','Ignorer le contexte de tous les mots.'],['La longueur ne prouve pas la parenté.','Le nombre de voyelles ne prouve pas la formation.','Le sens en contexte aide à analyser.'],'Une ressemblance seule ne suffit pas.')]))

unit(2,'Dont, donc et don : distinguer les emplois','choisir le mot à partir de son rôle et de son sens plutôt que d’une ressemblance sonore',
 'classes et formation des mots','cause, conséquence et reprise d’un complément',
 'Dont peut reprendre un complément construit avec de : le livre dont je parle. Donc peut marquer une conséquence ou une conclusion : la salle est occupée, donc nous attendons. Don est un nom désignant notamment ce qui est donné. Le regroupement orthographique ne signifie pas une prononciation identique dans tous les usages : le c de donc peut s’entendre. Cette leçon travaille la lecture et le sens, sans évaluer l’écoute ni fournir une règle absolue de prononciation.',
 'Modèles originaux : Voici le projet dont Bih parle. Le lieu est provisoire, donc il faut le vérifier. Le club reçoit un don de livres. Le relatif rattache une reprise à de ; le connecteur exprime un lien logique ; le nom désigne ce qui est donné.',
 'Cherche la construction et paraphrase : parler de, par conséquent ou chose donnée. Ne laisse pas le thème commun du passage supprimer ces différences. Un professeur pourra fournir les réalisations orales attendues.',[
 F('dont relatif','une reprise liée au complément en de dans le modèle','Le projet dont Bih parle reprend parler du projet.','Dont signifie toujours par conséquent.','La reprise d’un complément diffère du lien logique.'),
 F('donc connecteur','une marque de conséquence ou conclusion dans le modèle','Le lieu est provisoire, donc il faut vérifier.','Donc nomme le livre reçu en cadeau.','Le nom de la chose donnée est don.'),
 F('don nominal','ce qui est donné dans le sens étudié','Le club reçoit un don de livres.','Don remplace toujours le relatif de parler de.','Le nom désigne ici la chose donnée.'),
 F('contrôle syntaxique','la vérification du rôle dans la phrase','La paraphrase aide à choisir sans s’appuyer seulement sur le son.','Le c de donc est obligatoirement silencieux dans tous les usages.','La réalisation sonore peut varier ; le rôle écrit reste analysable.')],choose(2,[
 ('Le projet ___ elle parle est affiché.','dont',['donc','don','dans'],['Une conséquence ne reprend pas parler de.','Le nom ne fournit pas le relatif.','La préposition change la relation demandée.'],'Parler du projet appelle cette reprise.'),
 ('La salle est fermée ; ___ nous attendons.','donc',['dont','don','dans'],['Le relatif n’exprime pas ici la conséquence.','Un nom de cadeau ne relie pas les propositions.','Dans demanderait un autre complément.'],'Le connecteur porte le lien logique.'),
 ('Le club reçoit un ___ de livres.','don',['dont','donc','dans'],['Le relatif ne remplit pas ce nom après un.','Le connecteur n’est pas ce nom.','La préposition ne donne pas la chose reçue.'],'Le contexte demande le nom de ce qui est donné.'),
 ('Quelle démarche est correcte pour ce groupe de mots ?','Vérifier rôle et sens, sans promettre une homophonie universelle.',['Choisir au hasard si les sons semblent proches.','Toujours supprimer le c de donc à l’écrit.','Transformer chaque don en une conséquence.'],['La ressemblance ne décide pas de la graphie.','Le mot écrit conserve son c.','Don est un nom dans le sens étudié.'],'La construction guide le choix.')]),[1])

unit(3,'Cause et conséquence dans la phrase','distinguer une raison, son résultat et le sens du connecteur',
 'relations de sens et connecteurs','prise de parole justifiée et récit cohérent',
 'La cause présente une raison ; la conséquence présente ce qui en résulte dans le cadre donné. Parce que et à cause de peuvent introduire une cause avec des constructions différentes. Donc ou si bien que peuvent introduire une conséquence. Changer la direction du lien peut changer le message. Un connecteur ne prouve pas à lui seul que la causalité est vraie : il exprime le lien que le texte présente. Les catégories et fonctions de groupes ou subordonnées sont à nommer selon leur construction.',
 'Modèle original : Le lieu n’est pas confirmé, donc le club attend avant d’imprimer. Le manque de confirmation est présenté comme cause ; l’attente comme conséquence. Le club attend parce que le lieu n’est pas confirmé conserve cette relation en changeant l’ordre. À cause de cette incertitude est un groupe, non la même structure qu’une proposition avec parce que.',
 'Repère les faits, pose pourquoi pour la cause et que se passe-t-il en conséquence pour le résultat. Compare les constructions avant de remplacer un connecteur. Ne transforme pas une succession temporelle en cause certaine sans appui.',[
 F('cause','la raison présentée dans la relation étudiée','Le lieu non confirmé explique l’attente.','La cause est toujours le dernier mot de la phrase.','Le rôle dépend du lien exprimé, pas de la position.'),
 F('conséquence','le résultat présenté comme suivant la raison','Le club attend avant d’imprimer.','La conséquence doit précéder tout événement dans le temps.','Elle est présentée comme issue de la cause.'),
 F('construction conjonctive','une proposition introduite ici par parce que','Parce que le lieu est provisoire contient son groupe verbal.','À cause de cette incertitude est exactement la même structure verbale.','Ce groupe nominal diffère d’une proposition.'),
 F('prudence causale','la distinction entre un lien présenté et une preuve suffisante','Un connecteur annonce la relation voulue sans la démontrer seul.','Écrire donc suffit à rendre toute causalité vraie.','Le lien doit aussi être justifié par le contexte.')],choose(3,[
 ('Le club attend parce que le lieu est provisoire. Quelle est la cause présentée ?','Le caractère provisoire du lieu.',['L’attente du club.','Le seul mot club.','La fin de la ponctuation.'],['L’attente est la conséquence présentée.','Le nom seul ne donne pas la raison.','Un signe n’est pas ici la cause.'],'La proposition introduite par parce que fournit la raison.'),
 ('Le lieu est provisoire, donc le club attend. Quelle est la conséquence ?','Le club attend.',['Le lieu est provisoire.','Tout lieu est confirmé.','Le mot lieu est un verbe.'],['C’est la raison présentée.','Cela contredit le cas.','Lieu est ici un nom.'],'Donc introduit le résultat présenté.'),
 ('Quel remplacement préserve la relation et une construction correcte ?','Le club attend à cause de cette incertitude.',['Le club attend parce que cette incertitude, sans verbe.','La cause est toujours tout résultat.','À cause de le lieu est provisoire, sans adaptation.'],['Parce que appelle ici une proposition avec verbe.','Les rôles ne sont pas identiques.','À cause de demande un groupe adapté.'],'Le groupe nominal conserve la raison avec sa propre construction.'),
 ('Le texte dit après, sans autre appui causal. Quelle prudence convient ?','La succession seule ne prouve pas que le premier fait cause le second.',['Toute succession prouve une cause unique.','Aucun lien temporel n’existe jamais.','Tous les connecteurs sont interchangeables.'],['Il faut un appui supplémentaire.','Après exprime bien un ordre temporel.','Ils expriment des relations différentes.'],'Ne renforce pas le texte sans preuve.')]),[1,2])

participle=B.mcq('fi5-7-former',2,'Forme {T.label} de « {v} ».','{T.key=="ger" ? fr2Gerondif(v) : fr2ParticipePresent(v)}',
 [('{T.key=="ger" ? fr2ParticipePresent(v) : fr2Gerondif(v)}','en'),('{v}','inf'),('{fr2Participle(v)}','passe')],
 ['Le gérondif ajoute en au participe présent dans les modèles étudiés.','La forme demandée est {answer}.'],vars={'T':{'pick':[{'key':'ger','label':'le gérondif'},{'key':'pp','label':'le participe présent'}]},'v':{'pick':['avoir','être','faire','finir','parler','manger']}},
 misc=[('en','Ce choix échange le participe présent seul et le gérondif introduit par en.'),('inf','Tu as conservé l’infinitif plutôt que la forme demandée.'),('passe','Le participe passé ne répond pas à cette forme en -ant.')],sources=SRC)
unit(7,'Gérondif et participe présent','former les modèles et relier le gérondif au sujet de l’action principale',
 'verbes, cause et phrase complexe','traduction et description des actions',
 'Le participe présent verbal est invariable dans les modèles étudiés : parlant, finissant, ayant, étant. Le gérondif associe en au participe présent et peut exprimer notamment une simultanéité, une manière ou un moyen. Son sujet est normalement celui de l’action principale dans la construction enseignée. Distingue le participe verbal d’un adjectif verbal qui peut s’accorder, et d’un participe passé. L’interprétation dépend de la phrase, pas du seul groupe de lettres -ant.',
 'Modèles calculés : {fr2ParticipePresent("finir")}, {fr2ParticipePresent("avoir")}, {fr2Gerondif("être")}. Dans Bih lit en prenant des notes, Bih accomplit les actions reliées. Dans les membres parlant au groupe, parlant reste verbal et ne reçoit pas le pluriel du nom dans ce modèle.',
 'Identifie la forme demandée et la construction. Pour le gérondif, ajoute en et vérifie qui accomplit l’action. Ne rattache pas une action à un sujet différent sans le dire dans une autre proposition.',[
 F('participe présent verbal','une forme en -ant invariable dans le modèle verbal','Les membres parlant au groupe gardent parlant sans s.','Le participe verbal prend toujours le pluriel du sujet.','Il est invariable dans cet emploi.'),
 F('gérondif','la construction en suivie du participe présent','En finissant emploie le marqueur en.','Finissant seul contient déjà le marqueur en.','Le gérondif du modèle exige en.'),
 F('sujet partagé','le sujet commun attendu dans le gérondif étudié','Bih lit en prenant des notes attribue les actions à Bih.','Le gérondif peut changer secrètement de sujet sans effet.','Le rattachement doit rester cohérent.'),
 F('forme particulière','un participe présent dont le modèle doit être appris','Avoir donne ayant et être donne étant.','Avoirant est le modèle étudié.','La forme particulière est ayant.')],participle,[3,6])

past=B.mcq('fi5-19-formes',2,'Conjugue « {v} » {T.label} avec « {fr2Pronoun(p)} », à la voix active.','{T.key=="ps" ? fr2With(p,fr2PasseSimple(v,p)) : fr2PasseCompose(v,p)}',
 [('{T.key=="ps" ? fr2PasseCompose(v,p) : fr2With(p,fr2PasseSimple(v,p))}','autre'),('{fr2With(p,fr2Imparfait(v,p))}','imp'),('{fr2With(p,v)}','inf')],
 ['Le passé simple est une forme simple ; le passé composé associe auxiliaire et participe.','La forme demandée est {answer}.'],vars={'T':{'pick':[{'key':'ps','label':'au passé simple'},{'key':'pc','label':'au passé composé'}]},'p':{'int':[0,7]},'v':{'pick':['aider','parler','finir','choisir']}},
 misc=[('autre','Cette forme échange le passé simple et le passé composé demandés.'),('imp','L’imparfait ne répond pas à ce temps demandé.'),('inf','L’infinitif ne fournit pas la forme passée personnelle.')],sources=SRC)
unit(19,'Passé simple et passé composé','former les temps étudiés et distinguer registre narratif et structure verbale',
 'participes, auxiliaires et traduction','homophones et comparaison avec l’imparfait',
 'Le passé simple est une forme simple surtout associée au récit écrit littéraire. Le passé composé associe un auxiliaire au présent et un participe passé ; il est fréquent dans les échanges et de nombreux récits. Les deux peuvent présenter des événements accomplis, selon le cadre et la perspective. Ne décide pas que toute action brève impose le passé simple. Les exercices demandent explicitement le temps ; les verbes variables emploient ici avoir sans complément direct antéposé.',
 'Modèles calculés : {fr2With(3,fr2PasseSimple("aider",3))} le groupe ; {fr2PasseCompose("aider",3)} le groupe. Compare {fr2With(4,fr2PasseSimple("finir",4))} et {fr2PasseCompose("finir",4)}. Le récit choisi et le registre guident l’écriture ; la présence d’un auxiliaire distingue les structures.',
 'Identifie temps, sujet et verbe. Conjugue la forme simple ou l’auxiliaire requis, puis vérifie le participe. Dans une production, conserve un cadre narratif cohérent au lieu de changer de temps sans raison.',[
 F('temps simple','une forme conjuguée sans auxiliaire dans le modèle','Elle aida est au passé simple.','Le passé simple contient toujours avoir au présent.','Aida est une forme simple.'),
 F('temps composé','un auxiliaire conjugué associé au participe','Elle a aidé emploie auxiliaire et participe.','Elle a aider fournit le passé composé correct.','L’infinitif est remplacé par le participe aidé.'),
 F('registre narratif','le contexte d’écriture contribuant au choix du temps','Le passé simple apparaît surtout dans un récit écrit littéraire.','Toute action brève exige toujours le passé simple.','Le registre et la perspective comptent aussi.'),
 F('cadre cohérent','une perspective verbale maintenue ou changée pour une raison','Le narrateur choisit un cadre et justifie ses changements.','Des temps choisis au hasard conservent toujours le même récit.','Les relations temporelles peuvent changer.')],past,[7,13,17])

def family_scene():
    return json.dumps('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 330" role="img" aria-label="Suite familiale inventée : révision, lecture à voix haute puis horaire proposé"><rect width="320" height="330" fill="#f1f3eb"/><g fill="#213d2e" font-family="sans-serif" font-size="16"><text x="160" y="25" text-anchor="middle">Support familial inventé</text><rect x="20" y="43" width="280" height="70" fill="white" stroke="#597864"/><path d="M40 65h45v30H40zM85 65h45v30H85" fill="#bbd4c0" stroke="#345"/><text x="205" y="85" text-anchor="middle">Révision</text><rect x="20" y="128" width="280" height="70" fill="white" stroke="#597864"/><path d="M45 147h70v30H45zM120 142q35 20 0 40" fill="none" stroke="#456"/><text x="215" y="155" text-anchor="middle">Lecture à</text><text x="215" y="180" text-anchor="middle">voix haute</text><rect x="20" y="213" width="280" height="92" fill="white" stroke="#597864"/><path d="M40 232h70v50H40zM48 245h55M48 260h55" fill="none" stroke="#456"/><text x="205" y="250" text-anchor="middle">Horaire</text><text x="205" y="277" text-anchor="middle">proposé</text></g></svg>''',ensure_ascii=False)

writing(15,'Écrire à partir d’images de vie familiale','développer une scène fictive en distinguant indices dessinés et ajouts narratifs annoncés',
 'prise de parole, relations et cadre du récit','traduction et récit développé',
 'Une image fournit des indices, pas toute l’histoire des personnages. Pour écrire, commence par relever ce qui est visible, puis choisis un scénario fictif compatible. Annonce que les noms, pensées et événements ajoutés appartiennent à ton invention. Organise situation, difficulté et réponse, avec des liens compréhensibles. Le support ne permet pas de juger une famille réelle. Les modèles sont des propositions originales ; d’autres scénarios cohérents peuvent convenir.',
 ['Les dessins montrent une révision, une lecture à voix haute et un horaire proposé. J’imagine Bih et son cousin dans une maison fictive. Pendant que Bih révise, son cousin prépare sa lecture. Leurs activités se gênent ; le dessin ne donne pas leurs pensées, donc cette difficulté appartient au scénario que je choisis.',
 'Bih demande calmement s’ils pourraient comparer leurs horaires. Le cousin explique sa propre contrainte. Ils proposent des moments différents et demandent à un adulte de les aider à vérifier le programme. Cette réponse conserve les indices sans prétendre que tout problème familial se résout de la même façon.',
 'Le récit se termine sur un essai du nouvel horaire. Sa réussite reste à observer. Les noms, le dialogue et la difficulté racontée sont des ajouts fictifs annoncés, et non des faits fournis entièrement par les dessins.'],[
 F('indice dessiné','un élément directement représenté par le support','Le dessin indique une révision et une lecture à voix haute.','Le support révèle toutes les pensées privées des personnages.','Il représente des activités, pas une connaissance de tous les états intérieurs.'),
 F('ajout fictif annoncé','un détail inventé explicitement pour construire le scénario','J’imagine Bih et son cousin dans cette maison fictive.','Tout nom inventé devient une identité documentaire.','L’ajout reste une invention annoncée.'),
 F('enchaînement narratif','des événements reliés de manière compréhensible','Les activités se gênent, alors les personnages discutent.','Un récit doit accumuler uniquement des objets sans relation.','L’écriture développe une suite cohérente.'),
 F('fin proportionnée','une clôture ne dépassant pas ce que le récit établit','Le programme sera essayé sans résultat garanti.','Un horaire proposé garantit toutes les réussites futures.','Proposition et résultat doivent rester distincts.')],
 'À partir des dessins, écris une scène familiale originale. Relève les indices puis annonce les ajouts fictifs : noms, dialogue et difficulté choisie. Organise un début, une réponse et une fin cohérente. Suis la longueur demandée par ton enseignant.',[6,9,11,13],figure=family_scene())

writing(24,'Écrire une lettre formelle','rédiger une demande claire à un destinataire officiel en justifiant le projet et ses limites',
 'interprétation d’image, discours adapté et traduction','communication environnementale et descriptions organisées',
 'Une lettre formelle adapte présentation, formules et ton à son destinataire. Expose le but tôt, développe les informations utiles et formule précisément la réponse attendue. Une demande ne doit pas présenter une autorisation comme déjà accordée. Les coordonnées et dates du modèle sont fictives ou à compléter selon la consigne. Les conventions de présentation et de longueur varient selon le cadre d’examen ; l’enseignant doit confirmer celles à appliquer.',
 ['Club de lecture, établissement fictif de Bamenda. Date : à compléter selon la consigne. À la personne responsable des activités. Objet : demande d’autorisation pour une rencontre de lecture. Madame, Monsieur, nous sollicitons l’autorisation d’organiser une rencontre consacrée à la lecture et au partage des tâches au sein du club.',
 'Nous souhaitons proposer un passage original suivi d’un échange respectueux. Le programme devra être encadré par un adulte désigné. Le lieu et l’horaire restent à confirmer ; nous n’annoncerons pas ces détails comme définitifs avant votre réponse.',
 'Pourriez-vous nous indiquer si le projet peut être examiné et quelles précisions vous sont nécessaires ? Nous vous remercions de votre attention. Veuillez agréer, Madame, Monsieur, l’expression de nos salutations respectueuses. Bih, pour le club fictif.'],[
 F('destinataire et objet','les repères précisant à qui et pourquoi la lettre est adressée','L’objet annonce une demande d’autorisation.','Une lettre formelle doit cacher sa demande.','Le destinataire doit comprendre le but.'),
 F('demande justifiée','une action sollicitée avec des informations pertinentes','La rencontre et son encadrement sont expliqués.','Une demande prouve que l’autorisation est accordée.','Solliciter et recevoir l’accord sont différents.'),
 F('statut des détails','l’indication honnête des informations provisoires','Le lieu et l’horaire restent à confirmer.','Un détail provisoire peut devenir certain par une formule polie.','La politesse ne remplace pas la confirmation.'),
 F('formules cohérentes','un appel et une clôture adaptés au cadre formel','Madame, Monsieur est repris dans la clôture du modèle.','Toute lettre officielle doit se terminer comme un message à un ami intime.','Le registre doit correspondre au destinataire.')],
 'Écris une lettre formelle à la personne responsable demandant une rencontre de lecture supervisée. Présente le projet, son intérêt, l’encadrement souhaité et les arrangements encore provisoires. Utilise des renseignements fictifs et les conventions données par ton enseignant.',[15,17,21,23])

adverbs=[('manière','la façon dont se déroule l’action','Elle explique calmement.','Calmement donne le nom du lieu.','Il précise ici la manière.'),('quantité ou intensité','un degré ou une quantité dans le modèle','Elle travaille beaucoup.','Beaucoup fournit toujours une mesure exacte.','Un degré ne donne pas nécessairement une quantité numérique.'),('lieu','une localisation dans le modèle','Le groupe attend ici.','Ici signifie obligatoirement demain.','Ici localise, tandis que demain situe dans le temps.'),('temps','un repère temporel dans le modèle','Le groupe revient demain.','Demain indique la manière de revenir.','Il situe le retour dans le temps.')]
advq=choose(29,[(case+' Quelle valeur a l’adverbe sélectionné ?',term,[t for t,m,c,e,y in adverbs if t!=term],[f'Cette catégorie concerne {m}, plutôt que la valeur du modèle.' for t,m,c,e,y in adverbs if t!=term],why) for term,meaning,case,error,why in adverbs])
unit(29,'Les adverbes : manière, quantité, lieu et temps','identifier la valeur d’un adverbe et conserver sa portée dans une reformulation',
 'comparaison, classes de mots et vocabulaire environnemental','temps du projet et précision des descriptions',
 'Un adverbe peut modifier un verbe, un adjectif, un autre adverbe ou une phrase selon sa construction. Calmement précise une manière ; beaucoup peut indiquer une quantité ou intensité ; ici un lieu ; demain un temps. Tous les adverbes ne finissent pas par -ment et une forme peut avoir plusieurs emplois selon le contexte. Une indication de degré n’est pas une mesure exacte. Distingue la catégorie du mot de la valeur qu’il prend dans la phrase.',
 'Modèles originaux : Le groupe explique calmement, travaille beaucoup, attend ici et revient demain. Les adverbes ne sont pas interchangeables : changer demain en ici remplace un repère de temps par un lieu. Un texte soigneusement relu montre soigneusement modifiant le participe plutôt que le nom texte directement.',
 'Repère le mot modifié, puis la relation : comment, à quel degré, où ou quand. Paraphrase et vérifie que la substitution ne change pas une localisation en date ni une intensité en total mesuré.',[F(*x) for x in adverbs],advq,[11,23,28])

future=B.mcq('fi5-31-formes',2,'Conjugue « {v} » au {T.label} avec « {fr2Pronoun(p)} ».','{fr2With(p,T.key=="fut" ? fr2FuturSimple(v,p) : fr2Conditionnel(v,p))}',
 [('{fr2With(p,T.key=="fut" ? fr2Conditionnel(v,p) : fr2FuturSimple(v,p))}','autre'),('{fr2With(p,fr2Imparfait(v,p))}','imp'),('{fr2With(p,v)}','inf')],
 ['Les deux formes partagent le radical du futur mais pas les mêmes terminaisons.','La forme demandée est {answer}.'],vars={'T':{'pick':[{'key':'fut','label':'futur simple'},{'key':'cond','label':'conditionnel présent'}]},'p':{'int':[0,7]},'v':{'pick':['aller','faire','venir','avoir','choisir','envoyer']}},
 misc=[('autre','Ce choix échange futur et conditionnel.'),('imp','Cette forme emploie l’imparfait, non le temps demandé.'),('inf','L’infinitif ne porte pas la terminaison personnelle demandée.')],sources=SRC)
unit(31,'Conditionnel présent et futur simple','former les temps et distinguer projection, hypothèse et demande atténuée',
 'subjonctif, temps du récit et repères adverbiaux','lettre, projet et description cohérents',
 'Le futur simple emploie le radical du futur et ses terminaisons ; le conditionnel présent emploie le même radical avec les terminaisons de l’imparfait. Des radicaux sont particuliers : ir-, fer-, viendr-, aur-, enverr-. Le futur peut présenter une projection ; le conditionnel peut exprimer une hypothèse ou atténuer une demande selon le contexte. Aucune terminaison ne garantit qu’une prédiction se réalisera. Les exercices nomment la forme attendue ; un autre temps peut être grammatical dans une autre perspective.',
 'Modèles calculés : {fr2With(0,fr2FuturSimple("aller",0))} et {fr2With(0,fr2Conditionnel("aller",0))} ; {fr2With(4,fr2FuturSimple("envoyer",4))} et {fr2With(4,fr2Conditionnel("envoyer",4))}. Dans nous voudrions une précision, le conditionnel peut atténuer la demande. Le choix du sens se vérifie avec le reste de la phrase.',
 'Choisis le radical attesté, puis les terminaisons du temps et de la personne. Relis la perspective voulue. Ne confonds pas une projection future avec une information déjà vérifiée ni un conditionnel avec une absence totale de sens temporel.',[
 F('radical du futur','la base commune aux temps étudiés pour le même verbe','Aller utilise ir- dans le futur et le conditionnel étudiés.','Le futur de aller doit conserver aller comme radical sans changement.','Le radical particulier est ir-.'),
 F('terminaison du futur','la marque personnelle du futur simple','Je partirai porte ici -ai.','Je partirais et je partirai sont la même graphie.','Le s distingue les formes écrites.'),
 F('terminaison du conditionnel','les marques de l’imparfait ajoutées au radical du futur','Je partirais porte la terminaison du conditionnel.','Le conditionnel emploie toujours le radical de l’imparfait sans autre distinction.','La base est celle du futur dans ces modèles.'),
 F('valeur contextualisée','un sens interprété avec le cadre de la phrase','Une demande au conditionnel peut être atténuée.','Le futur prouve nécessairement la réalisation de toute prédiction.','La forme ne garantit pas l’événement.')],future,[13,17,28,29])

courwords=[('cour','un espace découvert près d’un bâtiment dans le modèle','La classe traverse la ___ de l’école.','cour'),('cours','un enseignement suivi sur une matière dans le modèle','Le ___ de français commence.','cours'),('court','un adjectif de faible longueur ou durée dans le modèle','Le message est bref : il est ___.','court'),('courre','la forme conservée dans l’expression chasse à courre','Le texte ancien emploie chasse à ___.','courre')]
unit(33,'Cour, cours, court et courre','choisir le mot selon le sens et la construction étudiés',
 'homophones, classes et vocabulaire des activités','lecture et description de lieux',
 'Cour désigne notamment un espace découvert près d’un bâtiment. Cours peut désigner un enseignement, un écoulement ou un déroulement selon le contexte. Court peut être adjectif de faible longueur ou durée ; il a d’autres emplois. Courre est conservé dans l’expression chasse à courre. La proximité sonore ne rend pas ces graphies interchangeables. Les exemples sélectionnent des sens précis sans prétendre définir tous les emplois des mots.',
 'Modèles originaux : Le cours de français se déroule près de la cour. Le message est court. Le texte mentionne l’expression ancienne chasse à courre sans donner de consignes de pratique. La classe et le sens attendus permettent le choix.',
 'Repère le rôle grammatical et remplace le mot par une paraphrase : espace, enseignement ou bref, lorsque le contexte le permet. Pour courre, reconnais l’expression attestée au lieu d’inventer une règle générale.',
 [F(t,m,s.replace('___',a),f'Tous les emplois de {t} peuvent être remplacés sans changement par une autre graphie du groupe.',f'{t} correspond ici à {m} ; le remplacement doit conserver ce sens.') for t,m,s,a in courwords],
 choose(33,[(s+' Choisis la graphie.',a,[tt for tt,mm,ss,aa in courwords if tt!=t],[f'{tt} correspond ici à {mm}, pas au sens demandé.' for tt,mm,ss,aa in courwords if tt!=t],'Le contexte demande '+t+'.') for t,m,s,a in courwords]),[2,21,31])

plural=B.mcq('fi5-36-pluriel',2,'Donne le pluriel nominal étudié de « {n} ».','{fr2NounPlural(n)}',
 [('{fr2NounNaive(n)}','regle'),('{n}','sing'),('{n+"es"}','es')],['Choisis le modèle attesté plutôt qu’une terminaison appliquée partout.','{fr2NounRule(n)}. Le pluriel est {answer}.'],vars={'n':{'pick':['cheval','travail','genou','pneu','festival']}},
 misc=[('regle','Cette généralisation ne correspond pas au pluriel attesté de ce nom.'),('sing','La forme donnée reste celle du singulier.'),('es','Ajouter -es mécaniquement n’est pas la graphie du modèle.')],sources=SRC)
unit(36,'Le pluriel des noms : cas particuliers','former les pluriels étudiés et reconnaître une exception sans généraliser à toute une finale',
 'accords nominaux et contexte','lecture, description et noms lexicalement pluriels',
 'Les finales donnent des modèles mais aussi des exceptions. Cheval donne chevaux, tandis que festival donne festivals. Travail donne travaux ; détail garde détails. Genou donne genoux, tandis que trou donne trous. Pneu donne pneus. Un modèle reconnu ne permet pas de transformer chaque mot d’apparence proche. Le pluriel nominal doit être vérifié avec le nom précis et la convention étudiée. Il ne se confond pas avec la conjugaison d’un verbe.',
 'Modèles calculés : {fr2NounPlural("cheval")}, {fr2NounPlural("festival")}, {fr2NounPlural("travail")}, {fr2NounPlural("genou")}, {fr2NounPlural("pneu")}. Compare {fr2NounPlural("détail")} et {fr2NounPlural("travail")} : la même finale singulière ne suffit pas à imposer une transformation unique.',
 'Identifie le nom, rappelle le modèle ou l’exception et écris le groupe avec son déterminant. Vérifie ensuite les accords autour du nom. N’invente pas une forme en -aux pour tout mot ni un x final pour tout pluriel.',[
 F('modèle en -al','le passage à -aux pour les noms étudiés comme cheval','Cheval donne {fr2NounPlural("cheval")}.','Cheval doit donner chevals dans ce modèle.','Le pluriel étudié est chevaux.'),
 F('exception en -al','le maintien de -s pour festival dans le modèle','Festival donne {fr2NounPlural("festival")}.','Tout nom en -al exige -aux sans exception.','Festival fournit une exception.'),
 F('cas en -ail','la distinction entre travail et détail dans les modèles','Travail donne travaux, détail donne détails.','Tous les noms en -ail suivent forcément travail.','Les noms précis doivent être distingués.'),
 F('cas en -ou ou -eu','le choix attesté entre x et s pour les noms étudiés','Genou donne genoux, pneu donne pneus.','Tous les noms de ces finales prennent le même x final.','Les modèles et exceptions diffèrent.')],plural,[1,11,34])

placefigure=json.dumps('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 250" role="img" aria-label="Plan de cour scolaire inventé sans échelle"><rect width="320" height="250" fill="#eef1e7"/><g font-family="sans-serif" font-size="15" fill="#213c2d"><text x="160" y="23" text-anchor="middle">Cour inventée - sans échelle</text><rect x="85" y="42" width="150" height="55" fill="#d6c7a7" stroke="#567"/><text x="160" y="74" text-anchor="middle">Salle de lecture</text><rect x="25" y="130" width="70" height="52" fill="#78a686"/><text x="60" y="120" text-anchor="middle">Bac</text><circle cx="255" cy="152" r="29" fill="#70a76a"/><text x="255" y="199" text-anchor="middle">Arbre</text><path d="M130 222h60" stroke="#355" stroke-width="3"/><text x="160" y="242" text-anchor="middle">Entrée</text></g></svg>''',ensure_ascii=False)
writing(43,'Décrire un lieu lié au module','organiser une description spatiale fondée sur un plan fictif et distinguer une impression',
 'images, accords et temps du récit','écrits développés et description d’un projet environnemental',
 'Une description de lieu suit un point de vue et un ordre spatial. Des repères comme à gauche, au fond et près de aident à situer les éléments. Ils doivent conserver le point d’observation choisi. Distingue l’objet visible d’une impression personnelle. Le plan inventé ne fournit ni mesures, ni fréquentation réelle, ni preuve de sécurité. Une description claire sélectionne des détails utiles au lieu d’accumuler des adjectifs ou de transformer une impression en fait mesuré.',
 ['Depuis l’entrée située en bas du plan fictif, la salle de lecture apparaît au fond. Un bac se trouve à gauche et un arbre à droite. Ces repères suivent le point de vue adopté ; ils ne donnent pas les distances réelles.',
 'J’imagine une cour accueillante parce que ses éléments offrent un cadre simple à décrire. Cette impression appartient à mon texte, non à une mesure du plan. Rien n’indique combien de personnes fréquentent la cour ni comment elle est utilisée chaque jour.',
 'La description garde donc un parcours stable : entrée, fond puis côtés. Elle distingue les éléments représentés des impressions ajoutées et ne transforme pas le dessin en relevé documentaire.'],[
 F('point d’observation','le repère depuis lequel les positions sont décrites','La description commence depuis l’entrée en bas du dessin.','Gauche et droite gardent le même sens malgré tout changement de point de vue.','Le repère choisi influence ces positions.'),
 F('ordre spatial','une progression cohérente entre positions','Le texte décrit l’entrée, le fond puis les côtés.','Une description doit changer de repère à chaque mot sans le signaler.','La progression doit rester lisible.'),
 F('élément représenté','un détail effectivement donné par le plan','Le bac est à gauche depuis le point de vue annoncé.','Le dessin mesure la fréquentation quotidienne.','Aucun relevé de fréquentation n’est fourni.'),
 F('impression annoncée','une interprétation personnelle distinguée d’un fait fourni','J’imagine une cour accueillante annonce une impression.','Toute impression est automatiquement une mesure certaine.','Le lecteur doit reconnaître son statut.')],
 'Décris la cour du plan inventé depuis l’entrée. Organise les positions et les détails, puis ajoute une impression explicitement personnelle. N’invente pas de mesures ou de fréquentation comme si elles étaient documentées.',[23,36,39,41],figure=placefigure)

plurals=[('Les funérailles ___ annoncées.','{fr2Present("être",6)}',['{fr2Present("être",2)}','être','étant'],['Le sujet nominal est pluriel dans ce modèle.','L’infinitif ne porte pas la personne.','Le participe ne fournit pas le présent fini.'],'Le verbe s’accorde au pluriel.'),
 ('Choisis le déterminant du nom lexicalement pluriel : ___ fiançailles.','Les',['Le','La','Un'],['Le déterminant singulier masculin ne convient pas.','Le déterminant singulier ne convient pas.','Le déterminant singulier ne convient pas au nom pluriel.'],'La forme nominale est plurielle dans ce sens.'),
 ('Complète l’adjectif : des ténèbres ___.','profondes',['profond','profonde','profonds'],['Il manque genre et nombre.','Il manque le pluriel.','Le nom est féminin dans le modèle.'],'Le groupe demande le féminin pluriel.'),
 ('Le mot fiançailles est pluriel dans ce sens. Que prouve ce pluriel lexical ?','La forme du nom, pas à lui seul plusieurs événements distincts.',['Que chaque récit parle de plusieurs couples obligatoirement.','Que tout adjectif doit rester singulier.','Que le nom est un verbe conjugué.'],['Le pluriel lexical ne fournit pas ce comptage.','L’accord se fait au pluriel dans le modèle.','Il s’agit d’un nom.'],'Distingue forme lexicale et nombre d’événements.')]
unit(45,'Les noms normalement employés au pluriel','accorder les groupes étudiés sans déduire un comptage du seul pluriel lexical',
 'pluriels nominaux et descriptions','homophones et écriture précise',
 'Certains noms sont normalement employés au pluriel dans les sens courants retenus : fiançailles, funérailles, ténèbres. Leur déterminant, les adjectifs et le verbe suivent l’accord du groupe nominal. Le pluriel lexical ne prouve pas à lui seul plusieurs événements séparés : des fiançailles peut désigner un événement dans le récit. Les emplois rares, littéraires ou d’autres sens demandent une vérification particulière. N’invente pas un singulier ordinaire en supprimant simplement le s.',
 'Modèles originaux : Les funérailles {fr2Present("être",6)} annoncées. Des fiançailles discrètes sont évoquées. Des ténèbres profondes entourent le lieu du récit. Le sens du passage reste nécessaire pour savoir de quoi il parle ; la forme plurielle n’établit pas toute l’histoire des personnes.',
 'Repère le nom et son sens, conserve sa forme attestée puis accorde le groupe. Distingue cet emploi lexical d’un pluriel obtenu simplement en comptant plusieurs objets. Vérifie les formes rares avant de les employer.',[
 F('pluriel lexical','une forme plurielle normalement retenue pour le sens du nom','Fiançailles est pluriel dans le sens étudié.','Il suffit de retirer le s pour obtenir un singulier courant de tout nom.','Certains emplois lexicaux n’ont pas ce singulier ordinaire.'),
 F('accord du déterminant','la forme du déterminant adaptée au groupe pluriel','Les accompagne funérailles.','La funérailles forme le groupe courant étudié.','Le déterminant doit correspondre au pluriel.'),
 F('accord de l’adjectif','les marques adaptées au genre et nombre du groupe','Ténèbres profondes garde le féminin pluriel.','Ténèbres profonde respecte le nombre du modèle.','Il manque la marque de pluriel.'),
 F('limite du comptage','l’absence de total événementiel fourni par le seul pluriel lexical','Fiançailles ne prouve pas plusieurs couples.','Toute terminaison plurielle prouve plusieurs événements indépendants.','La forme lexicale ne donne pas seule ce comptage.')],choose(45,plurals),[9,36,43])

couwords=[('cou','la partie du corps reliant tête et tronc dans le modèle','Le foulard entoure le ___.','cou'),('coût','la dépense ou valeur nécessaire dans le contexte','Le texte compare le ___ du matériel.','coût'),('coup','le geste ponctuel évoqué dans coup de crayon','Elle ajoute un ___ de crayon.','coup'),('coup','le mot conservé dans la locution après coup','Après ___, elle relit son texte.','coup')]
unit(46,'Cou, coût et coup','choisir une graphie selon un sens ou une locution reconnue',
 'homophones et analyse du contexte','traduction et relecture d’un texte développé',
 'Cou est un nom anatomique ; coût désigne une dépense dans les contextes étudiés ; coup peut désigner un geste ponctuel et entre dans de nombreuses locutions. Après coup signifie après l’événement dans le modèle. La proximité sonore ne supprime ni le sens ni la graphie. Cherche la construction entière au lieu de remplacer un mot par un autre uniquement parce qu’il se prononce de manière proche.',
 'Modèles originaux : Le foulard entoure le cou. Le club compare le coût du matériel sans fournir de prix réel. Bih ajoute un coup de crayon puis, après coup, relit son texte. Les contextes distinguent anatomie, dépense, geste et locution.',
 'Identifie le sens demandé et vérifie une paraphrase. Pour une locution, conserve la forme attestée du groupe entier. N’invente pas un montant lorsque le texte n’en donne pas.',[
 F('cou','le nom anatomique de la région entre tête et tronc','Le foulard entoure le cou.','Coût nomme cette région du corps.','Cou porte ici le sens anatomique.'),
 F('coût','la dépense évoquée dans le modèle','Le coût du matériel reste à comparer.','Cou fournit la graphie de la dépense.','Le sens de dépense demande coût.'),
 F('coup de crayon','la locution nommant le geste du modèle','Un coup de crayon ajoute une marque au dessin.','Coup doit toujours désigner une dépense financière.','Ses sens dépendent de la construction.'),
 F('après coup','la locution signifiant après l’événement dans le modèle','Après coup, elle relit son texte.','Après coût signifie après l’événement dans cette locution.','La locution conserve coup.')],choose(46,[(s+' Choisis la graphie.',a,[w for w in ['cou','coût','coup','cours'] if w!=a],[{'cou':'Cou désigne la région du corps.','coût':'Coût nomme une dépense dans le modèle.','coup':'Coup désigne le geste ou la locution étudiés.','cours':'Cours concerne un enseignement ou un déroulement selon le contexte, pas ce sens.'}[w] for w in ['cou','coût','coup','cours'] if w!=a],'Le sens de la phrase demande '+a+'.') for t,m,s,a in couwords]),[21,33,45])


def translation(n,title,goal,back,onward,model,rows,prereq):
    unit(n,title,goal,back,onward,
      'Traduire demande de conserver le sens, les personnes, les relations et le temps dans une construction naturelle. On ne remplace pas simplement chaque mot anglais par le premier mot français rencontré. Repère qui fait quoi, à qui et quand. Une traduction peut avoir plusieurs formulations justes ; les choix proposés testent ici des contrastes explicitement définis. Les courts textes sources anglais sont nécessaires à l’exercice, tandis que les consignes et les explications restent en français.',model,
      'Lis la source, repère les informations essentielles et rédige une proposition en français. Vérifie ensuite personne, temps et sens. N’ajoute pas un traitement, une identité ou un événement absent. Compare la fidélité du message plutôt que l’identité absolue des mots.',[
      F('fidélité','la conservation des informations et relations du texte source','Une traduction garde qui aide qui dans le modèle.','Traduire autorise à inventer les faits qui plaisent.','Les informations ajoutées sans source changent le message.'),
      F('personne grammaticale','le sujet ou destinataire à conserver dans la traduction','We ne devient pas automatiquement elle.','Chaque pronom anglais peut être remplacé par un sujet français au hasard.','Les référents font partie du sens à préserver.'),
      F('temps et aspect','la manière de situer et présenter l’action à conserver selon le contexte','Un événement accompli n’est pas remplacé sans raison par une habitude actuelle.','Le temps du verbe n’a aucune incidence sur le message.','La situation temporelle contribue à l’information.'),
      F('formulation naturelle','une construction française correcte plutôt qu’un calque mécanique','Une phrase est reformulée avec l’ordre attendu en français.','Une traduction fidèle doit toujours copier chaque ordre de mots anglais.','Les langues peuvent organiser différemment un même sens.')],
      choose(n,rows,key='traduire'),prereq)

def eco_scene(kind):
    shapes=[
      '<rect x="220" y="80" width="55" height="75" fill="#6e9f7b"/><text x="247" y="70" text-anchor="middle">Bac</text><path d="M80 145l45 -5 5 20 -45 5z" fill="white" stroke="#444"/><text x="100" y="190" text-anchor="middle">Papier au sol</text>',
      '<path d="M55 80h100v25h-50v45H80v-70" fill="#a4b7c7" stroke="#334"/><path d="M95 165q-15 20 0 20t0 -20" fill="#387ca1"/><text x="225" y="110" text-anchor="middle">Goutte</text>',
      '<path d="M120 140h80l-10 40h-60z" fill="#b37b50"/><path d="M160 140V70M160 100q-45 0 -40 -30 35 0 40 30M160 120q45 0 40 -30 -35 0 -40 30" fill="#5c9d62" stroke="#35673c"/><text x="160" y="205" text-anchor="middle">Plante en pot</text>',
      '<rect x="65" y="70" width="190" height="110" fill="#fff" stroke="#345"/><text x="160" y="110" text-anchor="middle">Gardons la cour</text><text x="160" y="140" text-anchor="middle">propre</text>'
    ]
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 235" role="img" aria-label="Scène environnementale inventée pour décrire des indices"><rect width="320" height="235" fill="#f1f3eb"/><g font-family="sans-serif" font-size="16" fill="#213c2d"><text x="160" y="28" text-anchor="middle">Dessin pédagogique inventé</text>'+shapes[kind]+'</g></svg>'

translation(49,'Traduire un court message d’environnement ou de santé','préserver action, personne, modalité et limite d’un message source',
 'formes composées, conditionnel et vocabulaire contextualisé','choix des homophones et écrits sur image',
 'Modèles originaux : “We have read the poster.” → {cap(fr2PasseCompose("lire",4))} l’affiche. “She would help the group.” → {cap(fr2With(3,fr2Conditionnel("aider",3)))} le groupe. La traduction conserve l’accompli ou l’hypothèse au lieu d’inventer un résultat sanitaire. Le contexte de santé n’autorise pas l’ajout d’un diagnostic.',[
 ('Traduis : “We have read the poster.”','{cap(fr2PasseCompose("lire",4))} l’affiche.',['{cap(fr2With(4,fr2Present("lire",4)))} l’affiche.','{cap(fr2PasseCompose("écrire",4))} l’affiche.','{cap(fr2PasseCompose("lire",3))} l’affiche.'],['Le modèle demande un accompli, non cette habitude présente.','Read ne signifie pas write.','We est pluriel et renvoie à nous.'],'Préserve personne, action et accompli.'),
 ('Traduis : “She would help the group.” Le contexte est hypothétique.','{cap(fr2With(3,fr2Conditionnel("aider",3)))} le groupe.',['{cap(fr2With(3,fr2FuturSimple("aider",3)))} le groupe.','{cap(fr2With(6,fr2Conditionnel("aider",6)))} le groupe.','{cap(fr2With(3,fr2Conditionnel("aider",3)))} un autre lieu sans rapport.'],['Le futur change la perspective hypothétique demandée.','She est singulier dans ce contexte.','Le complément source est le groupe.'],'Le conditionnel garde la modalité du contexte.'),
 ('Traduis : “They are here.” Le contexte précise un groupe féminin.','Elles {fr2Present("être",7)} ici.',['Elle {fr2Present("être",3)} ici.','Elles {fr2Present("être",7)} ailleurs.','Elles {fr2Imparfait("être",7)} ici.'],['Le groupe est pluriel.','Here signifie ici.','La source donne ici un présent.'],'Conserve genre contextuel, nombre, lieu et temps.'),
 ('Traduis le sens de “The text explains a word, not a diagnosis.”','Le texte explique un mot, pas un diagnostic.',['Le texte établit chaque diagnostic du quartier.','Le texte prescrit un traitement.','Le texte fournit les résultats d’une analyse absente.'],['La portée est volontairement limitée.','Aucune prescription n’est donnée.','Les résultats ne figurent pas dans la source.'],'Ne transforme pas un message de langue en preuve médicale.')],[13,17,31,34,41,46])

ourows=[('Tu proposes une lecture ___ une discussion ?','ou',['où','au','houx'],['La phrase offre une alternative, pas un lieu.','Au ne relie pas ces deux choix.','Houx nomme une plante et ne convient pas à cette relation.'],'Ou peut être remplacé ici par ou bien.'),
 ('___ se trouve la salle ?','Où',['Ou','Au','Houx'],['La question demande un lieu, pas une alternative.','Au ne forme pas cette question.','Le nom de plante n’est pas le mot interrogatif demandé.'],'Où interroge sur le lieu.'),
 ('Voici la cour ___ le groupe se réunit.','où',['ou','au','houx'],['La phrase reprend un lieu plutôt que deux choix.','Cette forme ne construit pas la relative demandée.','Le nom de plante ne reprend pas cour ici.'],'Où reprend le lieu antécédent.'),
 ('Le jour ___ le club arrive est indiqué.','où',['ou','au','houx'],['Il ne s’agit pas d’une alternative entre jours.','Cette préposition ne forme pas la reprise temporelle.','Le nom ne fournit pas le relatif temporel.'],'Où peut reprendre un repère de temps dans ce modèle.')]
unit(50,'Ou et où : alternative et repère','choisir l’accent selon une alternative ou une reprise de lieu ou de temps',
 'reprises, contexte et traduction','relecture d’un texte produit à partir d’image',
 'Ou sans accent exprime ici une alternative et peut être remplacé par ou bien. Où avec accent peut demander un lieu ou reprendre un antécédent de lieu ; il peut aussi reprendre un repère temporel comme le jour où. Le son seul ne décide donc pas de la graphie. La substitution est un contrôle de sens, pas une obligation de changer tous les mots du texte. Observe la construction entière avant de choisir.',
 'Modèles originaux : Une lecture ou une discussion ? Où se trouve la salle ? Voici la cour où le groupe se réunit. Le jour où il arrive est indiqué. Les derniers exemples ont des antécédents différents, mais ne présentent pas une alternative.',
 'Essaie ou bien si un choix est proposé. Sinon, repère la question ou l’antécédent spatial ou temporel. Relis pour éviter de convertir une date ou un lieu en alternative.',[
 F('alternative','un choix ou une disjonction exprimés dans le modèle','Une lecture ou une discussion propose des possibilités.','Ou sans accent est toujours une question de lieu.','Il relie ici des choix.'),
 F('interrogation de lieu','une demande de localisation','Où se trouve la salle demande un lieu.','L’accent ne change jamais le rôle du mot dans ces exemples.','Ou et où ont des constructions distinctes.'),
 F('reprise de lieu','une relative rattachée à un antécédent spatial','La cour où le groupe se réunit reprend cour.','La relative donne nécessairement deux choix à sélectionner.','Elle précise ici un lieu.'),
 F('reprise de temps','une relative rattachée à un repère temporel','Le jour où il arrive reprend jour.','Où ne peut jamais reprendre un repère temporel.','Le modèle le jour où fournit cet emploi.')],choose(50,ourows),[21,33,46,49])

writing(51,'Écrire à partir d’une image environnementale','développer un texte distinguant observation, interprétation et proposition',
 'lecture d’image, description, traduction et révision','écriture indépendante reliée aux preuves disponibles',
 'Une image peut lancer un texte descriptif ou explicatif, mais ne fournit pas toutes les causes ni les résultats. Organise les indices avant de proposer une action. Sépare je vois, cela peut évoquer et le groupe pourrait : observation, interprétation et proposition n’ont pas le même statut. Un projet doit rester annoncé comme tel. Le dessin inventé n’est ni une enquête réelle ni une autorisation de manipuler des déchets. Les ajouts narratifs doivent être signalés comme fictifs.',
 ['Le dessin pédagogique représente un papier au sol près d’un bac. Je peux décrire leur position, mais je ne connais pas l’auteur du geste ni le volume de déchets d’une ville. Ces limites empêchent de transformer la scène en accusation ou en bilan.',
 'La proximité du papier et du bac peut évoquer la propreté d’un lieu partagé. Dans un scénario fictif, notre club pourrait préparer une affiche rappelant où déposer les papiers ordinaires selon les consignes de l’établissement. Cette idée serait à discuter avec l’adulte responsable ; elle ne constitue pas un résultat déjà observé.',
 'Un texte fidèle à l’image distingue ainsi ce qui est montré, ce qui est interprété et ce qui est proposé. Il peut inviter à une réflexion sans prétendre prouver que toute difficulté a disparu.'],[
 F('observation délimitée','un relevé de ce que l’image représente réellement','Un papier est au sol près du bac.','Le dessin nomme tous les responsables de déchets.','Aucune identité n’est donnée.'),
 F('interprétation appuyée','un sens proposé à partir d’un indice','La proximité peut évoquer la propreté du lieu.','Une lecture possible devient automatiquement une mesure nationale.','Interpréter ne fournit pas cette mesure.'),
 F('proposition annoncée','une action envisagée plutôt que déjà accomplie','Le club pourrait préparer une affiche à discuter.','Pourrait signifie que le résultat est déjà prouvé.','La modalité marque une possibilité ou proposition.'),
 F('texte organisé','une progression reliant observation, sens et projet','Le texte décrit, interprète puis propose.','L’organisation exige de confondre tous les statuts des idées.','La clarté repose sur leurs relations et distinctions.')],
 'À partir de l’image inventée, écris un texte organisé : décris les indices, propose une interprétation et développe une idée de communication à discuter. Distingue les ajouts fictifs, les informations inconnues et les résultats encore non observés.',[15,24,28,39,43,45,49,50],figure=json.dumps(eco_scene(0),ensure_ascii=False))

OUT.mkdir(parents=True,exist_ok=True)
spine=json.loads((L.CONTENT.parent/'data/spine/form-5/francais-intensif.json').read_text(encoding='utf-8'))
DEFERRED=[]
for row in spine['terms'][0]['lessons']:
    if row['kind']=='lesson' and 'littérature' in row['title'].lower():
        n=row['seq'];DEFERRED.append(n)
        L.write('francais-intensif',n,dict(subject='francais-intensif',**{'class':'Form 5'},lesson_no=n,language='fr',status='deferred',sheet_title=row['title'],
          deferred_reason='Œuvres au programme : titre, auteur et édition en attente de retour enseignant, conformément à la demande de Dion. Aucune lecture suivie de remplacement inventée.'))
urls=json.loads((L.CONTENT/'form-5/french/sources.json').read_text(encoding='utf-8'))['francais']['urls']+[
 'https://vitrinelinguistique.oqlf.gouv.qc.ca/22915/la-grammaire/le-verbe/modes/distinction-entre-le-participe-present-et-ladjectif-participe',
 'https://vitrinelinguistique.oqlf.gouv.qc.ca/24712/la-syntaxe/constructions-syntaxiques-boiteuses/logique-syntaxique-sujet-sous-entendu-du-participe-present',
 'https://vitrinelinguistique.oqlf.gouv.qc.ca/22057/lorthographe/homophones-lexicaux/les-homophones-cour-cours-court-et-courre',
 'https://www.dictionnaire-academie.fr/article/A9F1882',
 'https://dictionnaire.lerobert.com/guide/pluriel-des-noms-communs',
 'https://www.larousse.fr/dictionnaires/francais/donc/26425']
(OUT/'sources.json').write_text(json.dumps({'francais':{
 'ref':'Supports et traductions originaux ; adaptations explicites de fondations Form Four et French Form Five ; OQLF, dictionnaires d’éditeurs, Portail linguistique et références thématiques conservées',
 'urls':list(dict.fromkeys(urls)),
 'checked':'Nouvelles références consultées le 2026-10-24, y compris passages indexés. Treize leçons de fondation sont adaptées avec identifiants, sujet, objectifs et dépendances propres : Form Four FI 4/45/32 ; Form Four French 1/4/17/21 ; Form Five French 22/15/11/6/25/19. Les autres banques appliquées et modèles sont nouveaux. Gérondif, temps, pluriels et accords variables utilisent les fonctions existantes. Don/dont et donc ne sont pas déclarés homophones universels : la réalisation du c est explicitement contextualisée. Aucun extrait d’œuvre prescrite ni substitution d’auteur. Les dessins sont inventés, les cadres de santé ne diagnostiquent personne.'}},ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
lines=['# Français intensif, Form Five — objectifs et liens','','Chaque ouverture présente un objectif, les acquis et la suite. Les prérequis relient uniquement les ressources actives.','','| Ligne | Sujet | À la fin | Acquis mobilisés | Pour la suite |','|---|---|---|---|---|']
lines += [f'| {n} | {title} | {goal} | {back} | {onward} |' for n,title,goal,back,onward in sorted(PATH)]
lines += ['','Trente brouillons de langue actifs. Vingt lectures suivies prescrites restent en attente de retour enseignant : '+', '.join(map(str,DEFERRED))+'. Intégrations 26/27/53 exclues.','','But commun : comprendre et préserver le sens, expliquer un choix grammatical, puis produire un texte organisé lié à un support et à un destinataire. L’oral reste une préparation écrite ; les œuvres prescrites ne sont pas remplacées par des fictions.']
(OUT/'LEARNING-PATH.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(OUT/'TEACHER-REVIEW.md').write_text('''# Français intensif, Form Five — retour enseignant

- TR-francais-intensif-1 : Vingt lectures suivies attendent titres, auteurs et éditions. Dion demande de conserver ce choix comme retour enseignant ; aucune œuvre ni analyse de remplacement n’est inventée. Les lignes différées sont énumérées dans LEARNING-PATH et ne comptent pas parmi les trente brouillons actifs.
- TR-francais-intensif-2 : Valider profondeur, rythme et adaptation au niveau intensif. Treize fondations sont explicitement adaptées de ressources proches ; confirmer les approfondissements nécessaires et les traductions alternatives acceptables.
- TR-francais-intensif-3 : Confirmer terminologie, conventions d’examen, longueur et présentation des textes sur image, de la lettre formelle et de la description. Les quatre productions 15/24/43/51 et leurs modèles illustrent la tâche ; leur qualité n’est pas notée automatiquement.
- TR-francais-intensif-4 : Les prises de parole et interprétations d’image 6/23/39 préparent l’écrit. Fournir échange réel, voix et écoute séparément. Images de famille, cour et environnement inventées ; distinguer les indices visibles des ajouts narratifs.
- TR-francais-intensif-5 : Vérifier le regroupement dont/donc/don : le c de donc peut se prononcer, donc pas de promesse d’homophonie universelle. Valider les usages contextuels de cour/cours/court/courre, cou/coût/coup et ou/où.
- TR-francais-intensif-6 : Les noms normalement pluriels sont limités aux sens courants étudiés ; ne pas transformer un pluriel lexical en nombre d’événements. Confirmer les exceptions rares/littéraires et les pluriels nominaux retenus.
- TR-francais-intensif-7 : Valider les conventions de gérondif, comparaison, concordance et temps narratifs. Les modèles n’imposent pas une règle absolue de registre ou de réalisation de toute prédiction.
- TR-francais-intensif-8 : Les lectures et traductions de santé distinguent vocabulaire, preuve et information absente. Aucun diagnostic, traitement, information privée, résultat d’analyse ou relevé réel n’est fourni. Les vérifications techniques ne valent pas approbation enseignante ni mesure d’apprentissage.
''',encoding='utf-8')
assert len(PATH)==30 and len(DEFERRED)==20
assert {n for n,*_ in PATH}|set(DEFERRED)=={r['seq'] for r in spine['terms'][0]['lessons'] if r['kind']=='lesson'}
