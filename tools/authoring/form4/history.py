"""Form Four History Term One: lesson rows 1–7, 9–15; further-study rows excluded.
Original classroom sources are labelled invented, never presented as archive quotations.
"""
import json
import re
import sys
from itertools import combinations
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lessonlib as L
import banks_en as B
L.use_class('form-4', 'Form 4')
OUT = L.ROOT / 'history'
PATH = []
TIMELINES = {
 1: ['Rhineland remilitarisation in {1936}', 'Munich Agreement in September {1938}', 'German occupation of Czech lands in March {1939}', 'German invasion of Poland in September {1939}'],
 3: ['European war begins in September {1939}', 'Cameroon Youth League formed in {1940}', 'Cameroons trusteeship agreements approved in December {1946}', 'CDC begins operating in {1947}'],
 4: ['Free French rallying in August {1940}', 'USCC develops in {1944}', 'Douala labour conflict in September {1945}', 'ARCAM established in {1946}', 'UPC founded in {1948}'],
 6: ['European war begins in {1939}', 'French Cameroon rallies to Free France in {1940}', 'Brazzaville Conference opens in January {1944}', 'Second World War ends in {1945}'],
 11: ['Yalta Conference in February {1945}', 'Potsdam Conference in July–August {1945}', 'Iron Curtain speech in {1946}', 'Truman Doctrine announced in {1947}'],
 12: ['Truman Doctrine announced in {1947}', 'Marshall Plan begins operating in {1948}', 'NATO formed in {1949}', 'Warsaw Pact formed in {1955}'],
 13: ['Limited Test Ban Treaty in {1963}', 'SALT agreements in {1972}', 'Helsinki Final Act in {1975}', 'Soviet invasion of Afghanistan in {1979}'],
 15: ['JEUCAFRA established in {1938}', 'USCC develops in {1944}', 'UPC founded in {1948}', 'BDC founded in {1951}'],
}

def F(term, meaning, case, error, why):
    return dict(term=term, meaning=meaning, case=case, error=error, why=why)

def sentence(text):
    return text[:1].upper()+text[1:]

def qa(n, key, level, items, sources):
    return B.QA(f'y4-{n}-{key}', level, '{X.q}', items, sources)

def unit(n, title, goal, back, onward, overview, detail, method, facts, sources, prereq=()):
    assert len(facts) >= 4
    banks = [[], [], []]
    for i, f in enumerate(facts):
        others = [x for j, x in enumerate(facts) if i != j][:3]
        banks[0].append(dict(q='Which term or event fits this description: '+f['meaning']+'?', r=f['term'],
          w=[x['term'] for x in others], e=[x['term']+' concerns '+x['meaning']+'. Compare that with the description asked for.' for x in others], y=f['why']))
        banks[1].append(dict(q=f['case']+'\nWhich feature does this example illustrate?', r=f['term'],
          w=[x['term'] for x in others], e=['That identifies '+x['meaning']+'. The example instead concerns '+f['meaning']+'.' for x in others], y=f['why']))
        banks[2].append(dict(q='Invented classroom source for analysis, not an archive quotation: '+f['case']+'\nWhich claim does this text support? Treat it as a practice text; real historical proof requires authentic evidence.',
          r=sentence(f['meaning'])+'.', w=[sentence(x['meaning'])+'.' for x in others],
          e=['That claim concerns '+x['term']+'. This text instead gives evidence about '+f['term']+'; do not add the other claim.' for x in others],
          y='The words of the practice text support '+f['meaning']+'. '+f['why']))
    q0=qa(n,'identify',1,banks[0],sources)
    q1=qa(n,'case',1,banks[1],sources)
    q2=qa(n,'source',2,banks[2],sources)
    q3=B.MT(f'y4-{n}-connect',2,'Match each historical feature to the evidence or example that illustrates it.',[(f['term'],f['case']) for f in facts],sources,pick=3)
    if n in TIMELINES:
        bank=[dict(zip(['a','b','c'],events)) for events in combinations(TIMELINES[n],3)]
        q3=L.order(f'y4-{n}-sequence',2,'Put these dated events in chronological order, earliest first. Then use their sequence to distinguish an earlier condition from a later response.',
          ['{X.a}','{X.b}','{X.c}'],vars={'X':{'pick':bank}},sources=sources,review='authored')
    q4=B.SP(f'y4-{n}-assess',3,'Find the claim that misrepresents the history or the evidence.',
      [f['term']+': '+f['meaning']+'.' for f in facts],[(f['error'],f['why']) for f in facts],sources)
    for statement,f in zip(q4['pool']['right'],facts):
        statement['explain']='This is an accurate distinction: '+f['why']+' Look for a claim that reverses the event, relationship or limit.'
    note=re.sub(r'\{(\d+)\}',r'\1',overview)
    L.lesson('history','history',n,(f'y4-{n}',title),prereq,note,
      L.worked({},'Analyse this invented classroom source, not an archive quotation: '+facts[0]['case'],
        ['Identify the action, actor and setting stated in the text.',sentence(facts[0]['meaning'])+'.',facts[0]['why'],'This practice text helps test reasoning; authenticate and compare real sources before claiming historical proof.'],facts[0]['term']),
      [L.card(f'y4-{n}-c1','Distinguish the historical features before explaining their relationship.',[f['term']+': '+f['meaning']+'.' for f in facts],q0['id']),
       L.card(f'y4-{n}-c2','Connect a specific action or event to the historical feature it illustrates.',[f['case'] for f in facts],q1['id']),
       L.card(f'y4-{n}-c3','Check a claim against the sequence, setting and limits of the evidence.',[f['error']+' Correction: '+f['why'] for f in facts],q4['id'])],
      [q0,q1,q2,q3,q4],learn=L.learn([
       ('Your goal and connections','By the end, you should be able to '+goal+'. Builds on: '+back+'. Leads to: '+onward+'.'),
       ('Explain the history',overview),('Follow the evidence and examples',detail),('Reason and check',method)],
       key_words=[(f['term'],f['meaning']) for f in facts],
       mistake=(facts[0]['error'],facts[0]['term']+': '+facts[0]['meaning']+'.',facts[0]['why'])))
    PATH.append((n,title,goal,back,onward))

unit(1,'Causes of the Second World War',
 'distinguish underlying causes from the immediate European trigger and explain how aggression and failed restraint interacted',
 'Form Three’s imperial rivalry, the First World War and its settlement','Cameroon’s involvement in a war fought through imperial networks',
 'The Second World War had interacting causes. Nazi expansionism sought conquest and racial domination; explaining it does not endorse it. Resentment over the postwar settlement and the economic crisis helped destabilise politics, but did not make war inevitable. The League of Nations failed to check major aggression effectively. Appeasement sought to avoid another war through concessions; Munich did not stop Hitler. Germany invaded Poland on {1} September {1939}; Britain and France declared war on {3} September. This marks the conventional European outbreak, while war in Asia had earlier roots.',
 'Compare stages: Japanese expansion in Manchuria from {1931}, Italy’s invasion of Ethiopia in {1935}, German remilitarisation of the Rhineland in {1936}, and Munich in {1938}. German occupation of the Czech lands in March {1939} undermined further promises of restraint. The German-Soviet non-aggression pact in August {1939} reduced Hitler’s immediate fear of a two-front war; it did not create a permanent alliance. The Soviet Union also invaded Poland later that September. Different crises weakened the international order before the invasion that triggered the wider European war.',
 'Build an explanation rather than a list: identify a condition, explain how it enabled aggression, then connect it to a decision. Distinguish motives, failed responses and the trigger. Compare diplomatic promises with subsequent actions. A contemporary speech reveals its speaker’s position; it does not prove that every citizen agreed or that a promised peace occurred.',[
 F('expansionism','a policy seeking territorial conquest and domination','Nazi leaders pursued an empire in eastern Europe and used force against neighbouring states.','Nazi expansion was simply a peaceful request with no conquest aim.','Expansionist policy involved deliberate conquest; economic hardship alone did not force that choice.'),
 F('appeasement','concessions intended to avoid war with an aggressive power','At Munich in {1938}, concessions over the Sudetenland were accepted in the hope of avoiding war.','The Munich settlement permanently ended German expansion.','The later occupation of Czech lands and invasion of Poland show that Munich did not prevent further aggression.'),
 F('failure of collective security','the inability of international cooperation to restrain major aggression effectively','The League failed to prevent Italy’s conquest of Ethiopia despite the principle of collective restraint.','The League successfully prevented every invasion in the interwar period.','Its ineffective response to major aggression weakened confidence in collective security.'),
 F('economic instability','hardship that increased political tensions without making aggression inevitable','Depression damaged livelihoods and helped extremist parties exploit fear and resentment.','Every country experiencing depression necessarily chose aggressive war.','Economic crisis created pressures; political choices and different national circumstances still mattered.'),
 F('immediate European trigger','Germany’s invasion of Poland leading to British and French declarations of war','Germany attacked Poland on {1} September {1939}; Britain and France declared war on {3} September.','The invasion of Poland happened after Britain’s September declaration of war.','The invasion preceded those declarations; distinguish the immediate sequence from deeper causes.')],['war'])

unit(2,'Cameroonians in the Second World War: reasons and roles',
 'explain why colonial rule drew Cameroonians into the conflict and distinguish military, labour and material contributions',
 'the causes of war and the division of Cameroon under British and French mandates','wartime effects in each administered territory',
 'Cameroon was divided into British- and French-administered mandate territories, not an independent state making a single war declaration. Imperial administration drew people and resources into the conflict. Recruitment could involve pressure as well as personal motives such as pay, livelihood or opposition to fascism. Soldiers, carriers, drivers, producers and families had different experiences. French-administered Cameroon rallied to Free France in August {1940}; this must not be confused with the British-administered territory or with independence. Contributions included military service, transport, supplies and production.',
 'The conventional date of the Free French rallying is {27} August {1940}. Leclerc and associates secured control at Douala with local support and a change of authority, rather than a vote of every inhabitant. Ports and transport routes supported the Allied effort. Labour and agricultural output mattered alongside troops. British administration connected its Cameroons territory to the Nigerian wartime system. Avoid assigning every African campaign to every Cameroonian recruit: an individual’s unit and service record are needed for that claim.',
 'Separate reasons for involvement from roles performed. Colonial recruitment explains a route into service; carrying supplies describes a role. Ask who chose, who ordered and who bore costs. A military communiqué may reveal commanders’ aims while giving little about African workers or families. Compare it with service records and local accounts. Do not interpret administrative rallying as universal free consent.',[
 F('colonial mobilisation','administrative recruitment of people and resources through imperial rule','A mandate administration calls for labour and supplies for its wartime effort.','Cameroon acted as a single independent government in the war.','The territories were under different colonial administrations; mobilisation reflected those structures.'),
 F('Free French rallying','the shift of French-administered Cameroon to de Gaulle’s wartime movement','In August {1940}, Leclerc’s operation at Douala helped establish Free French authority.','The Douala operation made both administered Cameroons independent.','Rallying changed wartime allegiance in French-administered Cameroon, not the territory’s independence status.'),
 F('military contribution','service in armed units and their operational support','A Cameroonian recruit serves in a military unit with duties recorded in its service files.','Every African recruit served in exactly the same overseas battle.','Specific service must be established from a unit or individual record; origin alone does not identify a campaign.'),
 F('civilian and material contribution','work and supplies supporting operations beyond direct combat','Producers provide agricultural goods while transport workers move supplies through a port.','Only people firing weapons contributed to the war effort.','Production, transport and civilian work sustained military operations as well as creating burdens.')],['rally','africa'],[1])

unit(3,'Effects of the war on the Southern British Cameroons',
 'connect wartime economic disruption with postwar plantation change and stronger political demands without confusing their dates',
 'Cameroon’s colonial mobilisation and contributions','comparison with French-administered Cameroon and postwar nationalism',
 'War disrupted trade, drew on labour and changed plantation administration in the British Cameroons. German-owned properties were again taken under enemy-property control. Shortages and labour demands could burden households even where production provided employment. Wartime experience and new political networks encouraged demands for representation and improved conditions. These developments were uneven; the war neither granted immediate independence nor gave every household the same result. Postwar plantation reorganisation led to the Cameroon Development Corporation, operating from {1947}.',
 'Distinguish a wartime action from a later response. Enemy-property control during the conflict was not identical to the CDC’s postwar establishment. Plantation development created employment and infrastructure but continued disputes over land and working conditions, including Bakweri land concerns. The Cameroon Youth League formed in Lagos in {1940}, showing that political organisation already existed during the war. British administration remained linked to Nigeria. UN trusteeship in {1946} later added international scrutiny; it did not instantly remove British authority.',
 'Organise effects as political, economic and social, then show connections: plantation change affected labour, land and political claims. Explain both opportunities and burdens. Compare workers’ accounts with administrative reports. A later institution may be part of the postwar response without being created during the fighting. Avoid claiming uniform prosperity or a direct, automatic path from military service to independence.',[
 F('enemy-property control','wartime administration of German-owned assets by British authorities','German-owned plantations in the British Cameroons came under wartime enemy-property control.','All German plantations remained unaffected by the war.','War changed their administration; later plantation reorganisation must be placed after this intervention.'),
 F('postwar plantation reorganisation','the establishment of the CDC after the conflict to operate plantation assets','The CDC began operating in {1947} after reorganisation of former German plantations.','The CDC was created before the Second World War began.','Its postwar establishment followed wartime control, rather than preceding the conflict.'),
 F('political organisation','collective activity seeking a stronger voice and representation','The Cameroon Youth League formed in Lagos in {1940}, before the war had ended.','Political association began only after independence.','The league provides a wartime example; later demands built on earlier organising.'),
 F('uneven social effects','different experiences of employment pressures land and household burdens','Plantation employment and development coexisted with labour demands and Bakweri land grievances.','New plantation employment proves that every local community benefited equally.','Employment did not erase land disputes or demonstrate equal benefits for all communities.')],['southern','plantations','trust'],[2])

unit(4,'Effects of the war on French-administered Cameroon',
 'explain political openings and economic burdens and distinguish promised reform from continued colonial inequality',
 'wartime contributions and the Southern British Cameroons comparison','Brazzaville and the rise of pressure groups',
 'French-administered Cameroon’s Free French commitment brought recruitment, production demands and financial burdens. Scarcity and rising living costs could intensify workers’ grievances. Wartime mobilisation and discussion of reform helped expand political expectations, while colonial power and inequality continued. Trade-union activity developed during the later war years. In Douala in September {1945}, labour conflict and violent repression exposed the gulf between claims of freedom and the conditions experienced locally. Neither rallying nor victory brought immediate independence.',
 'The USCC emerged in {1944} as an important union federation. Workers sought pay and conditions, while networks helped some activists move into wider politics. Postwar changes included representation through ARCAM and UN trusteeship in {1946}, but these were limited institutions within continued French administration. The UPC was founded in {1948}, after the fighting ended. Treat these as connected stages, not one event. Estimates of casualties and responsibility in the Douala violence need careful comparison; this lesson does not invent a precise death toll.',
 'Explain a chain: mobilisation and scarcity → grievances → organisation and demands → reform or repression. Do not assume that one reform abolished all inequality. Separate workers’ immediate objectives from every later party programme. Identify whether a source is a union appeal, official report or later account; compare what each includes and omits.',[
 F('wartime economic burdens','production demands and scarcity affecting workers and households','Supplies were directed towards war while shortages and living costs burdened local households.','Supporting Free France removed every economic hardship.','The contribution to war could increase burdens; political allegiance did not ensure prosperity.'),
 F('trade-union organisation','collective worker action for pay rights and conditions','The USCC developed in {1944}; workers organised around employment grievances.','A trade union’s immediate purpose is always identical to every later party’s programme.','Labour demands and broader political aims could overlap, but the organisations and objectives must be distinguished.'),
 F('Douala conflict','the labour confrontation and violent repression of September {1945}','A later account describes wage grievances and repression in Douala after the war in Europe had ended.','The Douala confrontation demonstrates that every colonial conflict ended peacefully.','Violent repression contradicts that sweeping claim; detailed tolls require checked evidence.'),
 F('limited postwar political opening','new representation and scrutiny under continued French administration','ARCAM and trusteeship appeared in {1946}, while independence remained a later struggle.','ARCAM and trusteeship immediately made French Cameroon sovereign.','Political openings were not the same as sovereign independence or an end to French administration.')],['french','trust'],[2,3])

unit(5,'Africa’s participation in the Second World War',
 'explain varied reasons for involvement and classify military and civilian roles using named regional examples',
 'Cameroonian mobilisation and contrasting wartime effects','reform debates and the growth of African nationalism',
 'Africa’s participation was diverse. Colonial powers recruited troops and labour and demanded production; individuals could also seek wages, defend homes or oppose Axis rule. Some recruitment involved coercion. North and East Africa were battlefields, and Africans also fought outside the continent. Soldiers from West and East Africa served in the Burma campaign against Japan. African producers, transport workers and households supported armies with food, raw materials and work. Participation did not mean equal rights, identical motives or uniform support for imperial rule.',
 'Use distinct examples. Ethiopian resistance and Allied forces fought Italian occupation; North Africa saw major Allied-Axis campaigns. West African units served in Burma, alongside forces from other regions. Cameroon’s Free French contribution belonged to a particular imperial and territorial setting. Mining, farming, transport and provisioning supported operations beyond the battlefield. Overseas contact could broaden expectations, but veterans returned to differing conditions and political choices. Avoid turning a continental contribution into an unsupported biography of one recruit.',
 'For each example identify where, who and what role. Distinguish a reason for enlistment from a task performed. A photograph of an African soldier in Burma supports presence there; it does not by itself reveal willingness, pay or later nationalist beliefs. Compare recruitment records, personal accounts and production evidence. African agency and colonial pressure can both be part of the explanation.',[
 F('imperial recruitment','colonial authorities drawing people into their war effort','Officials recruit soldiers in a dependent territory for an imperial army.','Every recruit independently decided the colony’s foreign policy.','Colonial authority structured mobilisation; individual motives and pressures varied.'),
 F('African battlefields','fighting on the continent as part of the global conflict','Allied and Axis forces fought in North Africa, while Ethiopia resisted Italian domination.','No part of Africa experienced military campaigning.','African territory included major theatres of war as well as places supplying overseas operations.'),
 F('overseas military service','African troops serving in campaigns outside Africa','West African soldiers fought in Burma against Japanese forces.','All African soldiers remained on the African continent throughout the war.','The Burma example demonstrates overseas service without proving that every recruit went there.'),
 F('economic and logistical support','production and movement of goods sustaining the war','Farmers supply food and transport workers move military materials.','An army needs combatants but no supplies or civilian labour.','Operations depended on food, transport and materials as well as combat service.')],['africa','rally'],[2,3,4])

unit(6,'The Brazzaville Conference: reasons and setting',
 'explain why French leaders convened the conference and distinguish its colonial reform agenda from an independence congress',
 'Africa’s wartime contributions and reform expectations','the recommendations and limits of Brazzaville',
 'The Brazzaville Conference met from {30} January to {8} February {1944}, before the war ended. De Gaulle opened it; René Pleven presided over its work. French officials wanted to reconsider imperial administration, recognise Africa’s wartime importance and strengthen France’s future position. Growing expectations and the need for reconstruction made reform urgent. It was primarily a conference of French colonial authorities, not an elected assembly of African peoples negotiating independence. Its framework sought a reformed relationship within French power.',
 'Brazzaville had served as a centre of Free France in equatorial Africa. Wartime dependence on African people and resources made the future of empire a pressing issue. Proposed reform also sought to preserve French influence, so gratitude and imperial interest must be examined together. Read the opening address as a statement of leadership aims; compare it with the recommendations to see what was proposed and excluded. The conference’s location in Africa did not make its participants representative of every African community.',
 'Ask why now, why here and who was represented. Distinguish reasons for convening from results. A statement recognising African contributions may support a reform agenda without promising national sovereignty. Do not transfer later independence dates backwards into a wartime conference. Explain how the desire to preserve empire could coexist with proposed improvements.',[
 F('wartime setting','a reform conference held before the Second World War ended','The conference opened in January {1944} while fighting continued.','Brazzaville was held only after the Second World War ended.','Its wartime timing helps explain both urgency and France’s dependence on its African base.'),
 F('recognition of African contribution','attention to the people and resources sustaining Free France','French leaders discussed the role African territories had played in continuing the war.','Africa had supplied no useful base or resources to Free France.','The importance of Africa formed part of the setting for reconsidering imperial policy.'),
 F('imperial reconstruction','an effort to reshape French rule while maintaining French influence','Officials considered reforms for the future relationship between France and its overseas territories.','Discussing reform necessarily meant agreeing to dissolve the empire immediately.','Reform within French power was distinct from a commitment to independence.'),
 F('limited representation','official deliberation without an elected African independence delegation','Colonial officials met to recommend policy rather than negotiate with representatives elected by all African peoples.','Meeting in Africa proves all Africans elected the conference delegates.','Location and representative authority are different; examine who actually attended and spoke.')],['brazzaville'],[4,5])

unit(7,'The Brazzaville Conference: recommendations and limits',
 'classify political social and labour recommendations and explain why reform did not amount to a promise of independence',
 'the reasons and official setting of Brazzaville','postwar nationalism and the trusteeship debate',
 'Brazzaville recommended wider representation, local assemblies, access to employment and improvements in education and social conditions. It proposed ending the indigénat system of exceptional administrative penalties and moving towards free labour. These were recommendations requiring later action, not proof of immediate universal enforcement. The conference rejected political development outside the French framework and did not promise independence. Its reform language nevertheless helped raise expectations that could be compared with continued inequality.',
 'Follow proposal and implementation separately. The conference called for labour change, but its labour recommendation allowed a transition rather than instantly ending all compulsion. The French law abolishing forced labour in overseas territories came in {1946}. Recommendations for representation did not automatically establish equal voting power everywhere. Brazzaville therefore combined reform proposals with an intention to maintain imperial unity. Later nationalist demands cannot be reduced to gratitude for a French promise of immediate sovereignty, because that promise was not made.',
 'Make a comparison: proposed change, limitation, later action. Check dates before claiming an effect. A statement about improving participation is different from a commitment to independent statehood. Recommendations can be historically important even when incomplete, delayed or used to preserve authority. Use later records to test implementation rather than assuming that the conference’s words transformed every locality.',[
 F('political recommendation','greater representation and local consultative or representative institutions','Officials recommended wider representation and local assemblies within the French framework.','A representation proposal automatically grants full national sovereignty.','Participation within an empire is different from independent control of a state.'),
 F('social recommendation','improvements in education access and social conditions','A conference recommendation seeks better education and wider access to employment.','Every social recommendation was already fully achieved when the conference opened.','A proposed improvement must be distinguished from its implementation and reach.'),
 F('labour reform','movement towards free labour and ending exceptional colonial constraints','The conference proposed labour changes, while abolition required subsequent measures.','Every form of compelled labour ended instantly at Brazzaville.','The recommendations and later abolition measures belong to different stages.'),
 F('imperial limit','the rejection of political evolution outside the French framework','The recommendations excluded independence despite proposing reforms to colonial administration.','Brazzaville guaranteed immediate independence for all French African territories.','The conference maintained the French framework; later independence was not its immediate grant.')],['brazzaville','reforms'],[6])

unit(9,'African nationalism: meaning and forms',
 'distinguish demands for collective self-government from a limited reform and explain how nationalism differed from Pan-Africanism',
 'colonial rule, wartime change and the limits of Brazzaville','the internal and external factors strengthening nationalist movements',
 'In this course, African nationalism means movements and ideas asserting a people’s right to determine its political future, especially to end colonial domination. A campaign could begin with demands for rights or representation and later seek independence; the stages were not identical everywhere. A nation is not simply one ethnic group, and nationalist movements could unite people across language or regional differences. Pan-Africanism promoted solidarity among Africans and people of African descent across territorial boundaries. Nationalism and Pan-Africanism could reinforce one another without being interchangeable.',
 'A petition for fair pay addresses an immediate grievance. A demand that inhabitants control the territory’s government raises the wider issue of self-government. A Pan-African meeting connects struggles across territories and the diaspora. Methods included petitions, associations, newspapers, unions, elections and, in some settings, armed struggle. No method alone defines every nationalist movement. Leaders disagreed over aims and tactics, and claims to represent a nation must be examined alongside the experiences of workers, women, rural communities and minorities.',
 'Identify the political objective rather than labelling every protest nationalist automatically. Ask who should govern, whose rights are claimed and how broadly support is organised. Distinguish solidarity across Africa from one territory’s constitutional objective. Explain a movement’s programme without treating all its assertions as established facts or assuming that national unity eliminated internal disagreement.',[
 F('self-determination','a people’s claim to decide its political future','An association demands that inhabitants determine the territory’s future government.','Self-determination means permanent rule without the inhabitants’ wishes.','The concept concerns political choice by the people, not their exclusion from deciding.'),
 F('nationalist mobilisation','organisation around collective political rights and self-government','People from several language groups campaign together for control of their territory’s government.','A nationalist coalition must consist of only one ethnic group.','A territorial movement can organise across ethnic and regional differences.'),
 F('Pan-African solidarity','cooperation among Africans and the diaspora across territorial boundaries','Delegates from different territories coordinate opposition to colonial domination.','Pan-Africanism concerns only one village’s private arrangements.','Its scope crosses territorial boundaries, even when participants also pursue local national goals.'),
 F('limited reform demand','a request for a particular improvement without necessarily demanding independent rule','A workers’ petition asks for a pay rise without stating a constitutional objective.','Every request for improved pay explicitly demands independence.','A wage demand may connect to nationalism but does not by itself specify independent statehood.')],['nationalism','trust'],[5,7])

unit(10,'Factors promoting African nationalism',
 'classify internal and external influences and explain how a grievance became organised pressure for political change',
 'the meaning of nationalism and Pan-African solidarity','Cameroonian pressure groups and party formation',
 'Nationalism grew through interacting internal and external influences. Colonial land, labour, tax and racial inequalities produced grievances. Education, newspapers, religious and welfare associations, unions and towns helped people exchange ideas and organise. The war brought burdens and new experiences and weakened claims of European invincibility. Pan-African networks and examples of Asian independence encouraged activists; UN principles offered language and forums for claims. None automatically produced independence: organisation, popular support, political choices and the authorities’ responses mattered.',
 'At Manchester in {1945}, the Pan-African Congress brought together activists calling for an end to colonial domination. India’s independence in {1947} supplied a powerful external example, not a law instantly freeing Africa. In Cameroon, workers’ organisation linked employment grievances with wider political networks. Wartime service could expose contradictions between fighting for freedom and experiencing colonial inequality. A factor’s classification depends on the question: overseas congresses are external influences, while local organising turns ideas into action.',
 'Explain the mechanism: a grievance supplies an issue; communication spreads it; an organisation sustains demands; an external example strengthens expectations. Avoid simply listing factors without links. Not all educated people or veterans held the same views. Superpower rhetoric about colonialism was selective and tied to strategic interests, rather than a guarantee of African freedom.',[
 F('internal grievance','a local colonial inequality or burden encouraging opposition','Residents oppose unfair land loss and unequal treatment under colonial administration.','Local land grievances were events occurring only in distant foreign capitals.','These grievances arise within the society experiencing colonial rule.'),
 F('organising network','institutions and communication linking people around political demands','Workers use a union and newspapers to share grievances and coordinate a campaign.','A grievance automatically creates a durable organisation without communication.','Networks help convert dissatisfaction into sustained collective action.'),
 F('international solidarity','cross-border contacts strengthening anticolonial arguments and cooperation','The Manchester Congress of {1945} connected African and diaspora activists.','The Manchester Congress was a meeting confined to one Cameroonian plantation.','Its international setting and participants made it a source of wider solidarity.'),
 F('external independence example','another country’s achievement encouraging expectations without determining the local outcome','India’s independence in {1947} encouraged anticolonial hopes in Africa.','Indian independence legally granted every African territory immediate independence.','An example can inspire activists without changing another territory’s legal status automatically.')],['nationalism','asia','french'],[9])

unit(11,'Origins of the Cold War',
 'explain how the wartime alliance gave way to rivalry and distinguish ideological disagreement from postwar security disputes',
 'the Second World War and the changing international setting of African nationalism','the Cold War’s policies, alliances and conflicts',
 'The Cold War was a prolonged rivalry centred on the United States and Soviet Union, involving power, ideology, security and competing political-economic systems. Their wartime alliance against Nazi Germany did not remove earlier distrust. After {1945}, disputes over Germany, Eastern Europe and reconstruction intensified suspicion. The United States feared expanding communist influence; Soviet leaders sought security and imposed influence over neighbouring states. These explanations must be assessed critically rather than accepted as complete justifications. Rivalry developed through a sequence, not one universally agreed starting incident.',
 'Yalta and Potsdam in {1945} concerned the postwar settlement. Differences over elections, occupation zones, reparations and influence in Eastern Europe helped undermine cooperation. Churchill’s Iron Curtain speech in {1946} expressed a Western interpretation of the division; it did not create every division by itself. American and Soviet accounts often presented their own actions as defensive and the other side’s as aggressive. Compare those claims with decisions and effects. Germany’s occupation and later division became a central arena of tension.',
 'Distinguish a background disagreement from an action escalating it. Explain how one side’s security measure could be read as a threat by the other, while still examining coercion and responsibility. Do not describe all countries as passive objects: smaller states and anticolonial movements pursued aims of their own. Cold does not mean that no armed conflicts or deaths occurred.',[
 F('ideological rivalry','competition involving opposing political and economic systems','American and Soviet leaders promoted contrasting visions of political power and economic organisation.','The former allies had identical political systems and no ideological differences.','Shared opposition to Nazi Germany did not eliminate their different systems or aims.'),
 F('postwar security dispute','conflict over influence borders and political control after the common enemy’s defeat','Disagreement over Eastern European governments intensified mistrust after {1945}.','Every dispute concerned only sporting competition.','Control and security in postwar Europe were central political issues.'),
 F('breakdown of the wartime alliance','the weakening of cooperation once the common war effort ended','Former allies increasingly disagreed over Germany’s future and reconstruction.','The alliance against Hitler guaranteed permanent agreement after the war.','A common enemy had supported cooperation without settling later conflicting interests.'),
 F('competing interpretations','different explanations of responsibility requiring comparison with evidence','Each government describes its policy as defensive while criticising its rival’s intentions.','An official’s claim that a policy is defensive proves every effect was harmless.','Official claims reveal standpoint; actions, effects and other sources must also be examined.')],['cold-origins','cold-documents'],[1,10])

unit(12,'The Cold War: causes and manifestations',
 'connect containment, aid, alliances, arms competition and proxy conflicts to the rivalry without treating every local war as wholly foreign-made',
 'the breakdown of the wartime alliance','détente and attempts to manage superpower competition',
 'The Cold War appeared in policy, alliances, propaganda, economic competition, arms races and conflicts involving other countries. The Truman Doctrine in {1947} expressed American support against communist pressure; the Marshall Plan operated from {1948} to aid European recovery and support Western stability. Soviet leaders opposed American influence and consolidated their own bloc. NATO formed in {1949}; the Warsaw Pact followed in {1955}. The Berlin blockade and airlift of {1948}–{1949} showed confrontation over access without a direct general war between the superpowers.',
 'Nuclear competition increased risks and encouraged deterrence: a state sought to prevent attack by threatening unacceptable costs. This was a strategy, not proof that weapons made everyone safe. The Korean War of {1950}–{1953} illustrates a conflict with local roots and major outside intervention. Propaganda promoted each bloc’s claims. Economic assistance could serve both recovery and strategic aims; it must not be reduced to one motive without evidence. Not every African government or nationalist movement simply followed orders from a superpower.',
 'For each manifestation state what happened and how it expressed rivalry. Separate alliance from aid, propaganda from military action and local objectives from outside intervention. The word cold refers to the absence of a full-scale direct US-Soviet war, not an absence of fighting elsewhere. Compare a policy’s announced purpose with its recipients, conditions and consequences.',[
 F('containment and aid','policy using support and resources to limit perceived communist expansion','The United States pairs assistance with the aim of resisting communist influence.','All economic aid was unrelated to political strategy.','Aid could address recovery while also serving strategic objectives.'),
 F('military blocs','formal security alliances grouping states around rival powers','NATO formed in {1949}; the Warsaw Pact formed in {1955}.','The Warsaw Pact was founded before NATO.','Check the sequence: NATO preceded the Warsaw Pact.'),
 F('Berlin confrontation','the blockade and airlift illustrating tension over access to the Western sectors','During {1948}–{1949}, an airlift supplied West Berlin amid the Soviet blockade of surface access.','The airlift was a programme for supplying a distant African plantation.','It responded to the Berlin access crisis in occupied Germany.'),
 F('conflict with outside intervention','a war combining local struggles and major external military involvement','In Korea, local division interacted with US-led UN and Chinese intervention within the wider rivalry.','Calling a war a Cold War conflict proves local causes and decisions did not exist.','Outside involvement and local origins can both be part of an explanation.')],['cold-policies','cold-origins'],[11])

unit(13,'Détente: meaning and manifestations',
 'recognise negotiated reductions in tension and distinguish arms limitation from disarmament or the end of the Cold War',
 'Cold War rivalry, alliances and nuclear risk','assessing agreements and the continued choices of states during decolonisation',
 'Détente means an easing of international tension through negotiation and practical accommodation. In Cold War study it commonly refers to improved US-Soviet relations, especially in the late {1960}s and {1970}s. Fear of nuclear escalation, the costs of competition and strategic calculations encouraged talks. Détente did not erase ideological differences, alliances or conflicts elsewhere. Arms limitation controlled specified weapons or systems; it was not the destruction of every weapon. A temporary easing must be distinguished from a permanent settlement.',
 'The Limited Test Ban Treaty of {1963} was an earlier step towards controlling nuclear danger; it did not ban all underground testing. SALT agreements in {1972} included the ABM Treaty and an interim limit on specified strategic offensive weapons. The Helsinki Final Act in {1975} addressed European security, cooperation and human rights. Meetings, exchanges and agreements offered channels for managing rivalry. Continued intervention and renewed tension, notably around the Soviet invasion of Afghanistan in {1979}, show the limits of accommodation.',
 'Ask what an agreement actually covers: testing, launchers, defensive systems or diplomatic principles. Compare obligations with implementation and later events. A photograph of leaders meeting proves contact, not complete agreement. Do not confuse the date of signing with ratification or enforcement. Explain both what changed and which rivalries continued.',[
 F('détente','an easing of tension through negotiation while rivalry can continue','Rival governments hold talks and agree measures to reduce the danger of confrontation.','Détente means every political disagreement and conflict has ended permanently.','Accommodation can reduce tension without eliminating the underlying rivalry.'),
 F('arms limitation','restrictions on specified weapons or systems rather than total abolition','SALT in {1972} placed agreed limits on particular strategic systems.','A limit on specified systems means all weapons everywhere were destroyed.','Scope matters: partial limits are different from universal disarmament.'),
 F('Helsinki cooperation','European security and cooperation commitments associated with the {1975} Final Act','States agree principles concerning security, cooperation and human rights at Helsinki.','The Helsinki Final Act was the agreement founding NATO in {1949}.','Helsinki belonged to a later effort at cooperation, not NATO’s founding.'),
 F('limits of accommodation','continued rivalry and renewed crises despite improved relations','Renewed confrontation after Afghanistan in {1979} exposes the fragility of improved relations.','One summit guaranteed that no later crisis could occur.','Later crises demonstrate that negotiated easing was conditional and reversible.')],['detente','helsinki'],[12])

unit(14,'Cameroon under UN trusteeship: agreement and administration',
 'explain why mandate territories entered trusteeship and distinguish the administering authority from UN supervision and petitions',
 'mandate administration, postwar reform and international institutions','pressure groups using local organisation and international scrutiny',
 'After the League of Nations period, UN trusteeship provided an international framework for administering and supervising designated territories. It aimed at political, economic, social and educational advancement and progress towards self-government or independence according to circumstances and the people’s wishes. The General Assembly approved separate agreements for the British- and French-administered Cameroons on {13} December {1946}. Britain and France continued to administer their respective territories under agreed obligations. The UN did not become the ordinary local government and did not grant immediate independence through approval alone.',
 'The process involved proposed terms, agreement by the states directly concerned and approval by the appropriate UN organ. For these non-strategic Cameroons agreements, approval lay with the General Assembly. Under its authority the Trusteeship Council considered reports, examined petitions in consultation with administrators and arranged agreed periodic visits. British Cameroons remained administered in connection with Nigeria; French Cameroon remained under French authority. Petitions and visiting missions offered routes for inhabitants’ claims, but scrutiny did not guarantee an immediate remedy or a predetermined constitutional outcome.',
 'Separate objective, agreement, administrator and supervision. A petition is a request or complaint, not itself a binding judgment. An annual report presents the administering authority’s account; compare it with petitions and visiting-mission evidence. Use the plural Cameroons when discussing the separate arrangements rather than assuming a single unified administration. Later outcomes require their own chronology and evidence.',[
 F('trusteeship objective','advancement and progress towards self-government or independence under an agreed international framework','The agreement sets goals for inhabitants’ advancement and future political development.','Trusteeship’s stated objective was permanent exclusion from all self-government.','The framework explicitly envisaged political advancement; actual progress still needs assessment.'),
 F('administering authority','the state conducting territorial administration under the agreement','Britain and France continued to administer their respective Cameroons territories.','UN approval replaced all local officials with a UN national government.','International supervision differed from day-to-day British or French administration.'),
 F('General Assembly approval','the UN authorisation of these non-strategic trusteeship agreements','The General Assembly approved the Cameroons agreements on {13} December {1946}.','The agreements were approved only by a private trading company.','Approval belonged to the appropriate UN organ, not a commercial firm.'),
 F('international supervision','scrutiny through reports petitions and agreed visits','The Trusteeship Council examines administrative reports alongside petitions and visiting evidence.','Every petition automatically grants the precise constitutional outcome requested.','Petitions offered a channel for claims but were not self-executing decisions.')],['trust','trust-charter'],[3,4,9])

unit(15,'Pressure groups and political parties in French Cameroon',
 'explain how labour and political networks developed and distinguish an organisation’s immediate demands from a party’s programme',
 'wartime grievances, nationalist mobilisation and trusteeship channels','later study of party rivalry, independence and reunification',
 'Pressure groups sought to influence policy around particular interests; political parties organised broader programmes and competed for political authority or representation. In French Cameroon, labour grievances, unequal rights, educated activists, urban networks and postwar openings encouraged organisation. The colonial-sponsored JEUCAFRA, established in {1938}, opposed a return to German rule but also became a space where some Cameroonians developed political experience. It must not be treated as if it already had the later UPC’s programme. Unions and associations helped activists build networks while pursuing their own immediate objectives.',
 'The USCC developed in {1944} around workers’ rights and conditions. The UPC, founded in {1948}, pressed for independence and reunification; Ruben Um Nyobè became a leading figure. Later party competition included Aujoulat’s BDC, founded in {1951}, whose approach differed from the UPC’s. Representation and international petitioning gave activists additional arenas, while colonial authorities also used surveillance, restriction and repression. These organisations were neither identical nor supported by every inhabitant. Detailed later conflict belongs to subsequent study, not an invented peaceful transition.',
 'For each organisation record setting, immediate aims, methods and relationship with colonial authority. Trace connections between unions and parties without saying they were the same body. Compare programmes with practice and distinguish an organisation’s claim to represent people from evidence of support. Do not infer that all political change came from foreign leaders or that every reform-minded association demanded immediate independence.',[
 F('JEUCAFRA','an initially colonial-sponsored political association opposing German return and providing political experience','In the late {1930}s JEUCAFRA combined pro-French aims with a forum for some Cameroonian claims.','JEUCAFRA and the later UPC had identical origins and programmes.','Colonial sponsorship and its initial pro-French stance differed from the later UPC’s independence programme.'),
 F('USCC','a union federation concerned with workers’ rights and conditions','Workers organise within the USCC around wages and employment conditions from {1944}.','Every union demand was already the complete programme of a later political party.','Labour organisation could develop political networks while retaining specific employment objectives.'),
 F('UPC','the party founded in {1948} advocating independence and reunification','The UPC links the end of French domination with reunification of the divided Cameroons.','The UPC was founded before the First World War.','Its foundation belongs to the post-Second World War period.'),
 F('party competition','different organised programmes competing for representation and political influence','The BDC founded in {1951} offered a different political approach from the UPC.','All parties in French Cameroon had a single agreed programme and leader.','Different organisations competed and disagreed; party plurality does not imply identical aims.')],['french','parties','trust'],[4,9,10,14])

SOURCES={
 'war':dict(ref='Primary records and museum research on aggression, appeasement and the European outbreak',urls=[
  'https://www.nationalarchives.gov.uk/education/resources/chamberlain-and-hitler/',
  'https://encyclopedia.ushmm.org/content/en/article/world-war-ii-in-europe',
  'https://encyclopedia.ushmm.org/content/en/article/neville-chamberlain',
  'https://api.parliament.uk/historic-hansard/commons/1939/apr/03/european-situation-1',
  'https://www.iwm.org.uk/sites/default/files/Transforming_IWM_London_Phase_2.pdf']),
 'rally':dict(ref='Contemporary telegrams reproduced by the Charles de Gaulle Foundation and official military chronology',urls=[
  'https://www.charles-de-gaulle.org/blog/2020/09/24/chronologie-des-ralliements-des-territoires-de-lempire-a-la-france-libre/',
  'https://www.cheminsdememoire.gouv.fr/fr/1940-08-27-ralliement-du-cameroun-la-france-libre']),
 'africa':dict(ref='National Army Museum collection and research on African military service and supporting roles',urls=[
  'https://www.nam.ac.uk/whats-on/fighting-empire-britains-colonial-african-armies-1939-45',
  'https://www.nam.ac.uk/whats-on/west-african-soldiers-burma',
  'https://collection.nam.ac.uk/detail.php?acc=1996-08-382--26']),
 'southern':dict(ref='Original archival scholarship: Why Do We Need the White Man’s God?, chapter on wartime Southern Cameroons; teacher to check local political chronology',urls=[
  'https://eprints.soas.ac.uk/29549/1/10731705.pdf',
  'https://www.sumerianz.com/pdf-files/sjss3%288%2999-106.pdf']),
 'plantations':dict(ref='CDC institutional history and original research on plantation ownership and labour',urls=[
  'https://cdc-cameroon.net/new2014/about-cdc/',
  'https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers15-04/010063762.pdf',
  'https://www.persee.fr/doc/polaf_0244-7827_1986_num_22_1_3815']),
 'french':dict(ref='Original commission research, archival witness account and research on railway labour organisation',urls=[
  'https://www.vie-publique.fr/files/rapport/pdf/297054_0.pdf',
  'https://www.vie-publique.fr/files/rapports/fichiers_joints/297054_Volume_2.pdf',
  'https://mongobeti.arts.uwa.edu.au/issues/pnpa55_58/pnpa55_58_02.html',
  'https://www.tandfonline.com/doi/full/10.1080/0023656X.2025.2511702']),
 'brazzaville':dict(ref='Opening address, contemporary ministry recommendations and scholarly conference review',urls=[
  'https://www.charles-de-gaulle.org/lhomme/dossiers-thematiques/france-libre-lempire-colonial-francais/document-discours-douverture-conference-de-brazzaville/',
  'https://www.cvce.eu/content/publication/2015/10/23/37d49e93-13d5-4c31-ac33-31f550ad87f9/publishable_fr.pdf',
  'https://www.persee.fr/doc/outre_0300-9513_1991_num_78_292_2913_t1_0416_0000_2',
  'https://histoire-geo.ac-noumea.nc/IMG/pdf/sujetbacremplas07.pdf']),
 'reforms':dict(ref='French law abolishing forced labour, distinct from earlier conference recommendations',urls=[
  'https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000874642']),
 'nationalism':dict(ref='UNESCO African history scholarship, organiser’s congress account and archive-holding museum interpretation',urls=[
  'https://www.unesco.org/en/articles/first-world-war-and-its-consequences-africa-0',
  'https://openstax.marxists.info/archive/padmore/1947/pan-african-congress/index.htm',
  'https://phm.org.uk/blogposts/africa-speaks-in-manchester-pan-africanism-manchester-and-a-collection-gem/',
  'https://scholarworks.lib.csusb.edu/history-in-the-making/vol10/iss1/6/']),
 'asia':dict(ref='Official diplomatic history of decolonisation and Indian independence',urls=[
  'https://history.state.gov/milestones/1945-1952/asia-and-africa']),
 'cold-origins':dict(ref='US official interpretation, archival chronology and NATO institutional history; compare perspectives',urls=[
  'https://history.state.gov/milestones/1945-1952/foreword',
  'https://2001-2009.state.gov/r/pa/ho/pubs/fs/85895.htm',
  'https://www.trumanlibrary.gov/library/online-collections/ideological-foundations-of-cold-war',
  'https://www.nato.int/en/about-us/nato-history/a-short-history-of-nato']),
 'cold-documents':dict(ref='Archival collections of policy papers and speeches',urls=[
  'https://www.trumanlibrary.gov/library/online-collections/truman-doctrine']),
 'cold-policies':dict(ref='Contemporary policy and alliance chronology; aid and strategic objectives',urls=[
  'https://history.state.gov/milestones/1945-1952/marshall-plan',
  'https://www.nato.int/archives/1st5years/appendices/1.htm',
  'https://www.diplomaticrooms.state.gov/timelines/containment-and-cold-war/']),
 'detente':dict(ref='Arms control agreements and contemporary negotiation statement; official retrospective',urls=[
  'https://1997-2001.state.gov/global/arms/treaties/salt1.html',
  'https://www.presidency.ucsb.edu/documents/message-ambassador-gerard-c-smith-the-opening-the-strategic-arms-limitation-talks-helsinki',
  'https://history.state.gov/milestones/1969-1976/detente']),
 'helsinki':dict(ref='OSCE deposit of the Helsinki Final Act',urls=['https://www.osce.org/helsinki-final-act']),
 'trust':dict(ref='UN agreement records for separate British and French Cameroons',urls=[
  'https://research.un.org/en/docs/tc/britishcameroons',
  'https://research.un.org/en/docs/tc/frenchcameroons',
  'https://digitallibrary.un.org/record/3995996',
  'https://digitallibrary.un.org/record/860253/files/1122966-EN.pdf']),
 'trust-charter':dict(ref='UN Charter: objectives, agreement, approval, reporting, petitions and visits',urls=[
  'https://main.un.org/securitycouncil/en/content/working-methods-un-charter',
  'https://www.un.org/en/about-us/un-charter/chapter-13']),
 'parties':dict(ref='Original research on JEUCAFRA and political organisation, plus commission findings',urls=[
  'https://www.persee.fr/doc/acths_1764-7355_2012_act_134_8_2181',
  'https://journals.openedition.org/cea/pdf/533',
  'https://www.vie-publique.fr/files/rapports/fichiers_joints/297054_Volume_2.pdf'])
}
for value in SOURCES.values():
    value['checked']='Consulted 2026-10-23, including indexed research excerpts. All exercise sources are explicitly invented classroom texts, not historical quotations. Direct English commission PDF was too large for the web reader; indexed passages and French versions were consulted. CVCE scan has poor OCR. Exact regional chronology, interpretation and examination depth require teacher review.'
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'sources.json').write_text(json.dumps(SOURCES,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
lines=['# Form Four History — learning path','','Every opening Learn screen states a measurable goal, earlier knowledge and next use. Prerequisite lesson numbers are also stored in JSON.','','| Row | Topic | By the end | Builds on | Leads to |','|---|---|---|---|---|']
lines += [f'| {n} | {title} | {goal} | {back} | {onward} |' for n,title,goal,back,onward in PATH]
lines += ['', 'Teaching rows 1–7 and 9–15 are included. Rows 8 (Algerian FLN) and 16 (UPC further study) are classified further_study and are outside the assigned lesson rows; brief UPC context still appears in row 15. The later chapter-numbering warning at row 40 does not alter this Term One sequence.', '', 'Destination: explain how wartime mobilisation, reform limits, international rivalry and new forums connected to organised demands for political change. Distinguish cause from trigger, proposal from implementation, and source claim from corroborated history.']
(OUT/'LEARNING-PATH.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
