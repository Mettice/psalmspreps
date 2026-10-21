# French Form 1, Batch F1: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:french`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: tables and rules the computed answers use (src/engine/lib/french.js)

Everything the pupil reads in French lessons is in French, including the working the engine writes (`lang: "fr"`).

**Nouns (TR-F01)**: definite and indefinite article, plural, and the possessive “à moi”.

| Nom | Genre | Défini | Indéfini | Pluriel | À moi |
|---|---|---|---|---|---|
| livre | masculin | le livre | un livre | les livres | mon livre |
| cahier | masculin | le cahier | un cahier | les cahiers | mon cahier |
| stylo | masculin | le stylo | un stylo | les stylos | mon stylo |
| sac | masculin | le sac | un sac | les sacs | mon sac |
| tableau | masculin | le tableau | un tableau | les tableaux | mon tableau |
| crayon | masculin | le crayon | un crayon | les crayons | mon crayon |
| table | féminin | la table | une table | les tables | ma table |
| chaise | féminin | la chaise | une chaise | les chaises | ma chaise |
| règle | féminin | la règle | une règle | les règles | ma règle |
| maison | féminin | la maison | une maison | les maisons | ma maison |
| porte | féminin | la porte | une porte | les portes | ma porte |
| mangue | féminin | la mangue | une mangue | les mangues | ma mangue |
| école | féminin | l’école | une école | les écoles | mon école |
| amie | féminin | l’amie | une amie | les amies | mon amie |
| orange | féminin | l’orange | une orange | les oranges | mon orange |
| arbre | masculin | l’arbre | un arbre | les arbres | mon arbre |
| ami | masculin | l’ami | un ami | les amis | mon ami |
| enfant | masculin | l’enfant | un enfant | les enfants | mon enfant |
| oiseau | masculin | l’oiseau | un oiseau | les oiseaux | mon oiseau |
| homme | masculin | l’homme | un homme | les hommes | mon homme |
| haricot | masculin | le haricot | un haricot | les haricots | mon haricot |
| hibou | masculin | le hibou | un hibou | les hiboux | mon hibou |

- **Conjugation (TR-F02)**: avoir: j’ai, tu as, il a, nous avons, vous avez, ils ont; s’appeler: je m’appelle, tu t’appelles, il s’appelle, nous nous appelons, vous vous appelez, ils s’appellent; travailler: je travaille, tu travailles, il travaille, nous travaillons, vous travaillez, ils travaillent; laver: je lave, tu laves, il lave, nous lavons, vous lavez, ils lavent.
- **Numbers (TR-F03)**: traditional spelling taught; the 1990 spelling is also accepted when typed. 17 → dix-sept (1990 : dix-sept); 21 → vingt et un (1990 : vingt-et-un); 22 → vingt-deux (1990 : vingt-deux); 31 → trente et un (1990 : trente-et-un); 41 → quarante et un (1990 : quarante-et-un); 44 → quarante-quatre (1990 : quarante-quatre); 50 → cinquante (1990 : cinquante).
- **Alphabetical order (TR-F04)**: accents are ignored when ordering (école sorts with e).

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `f1-sort` | 1 | matching, 1 | alphabet |
| 2 | `f1-accent` | 1 | multiple choice, 2 | alphabet |
| 3 | `f1-spot` | 1 | spot the error, 3 | alphabet |
| 4 | `fc1-3-check` (card fc1-3) | 1 | multiple choice, 1 | alphabet |
| 5 | `f2-who` | 2 | multiple choice, 1 | lecture |
| 6 | `f2-family` | 2 | multiple choice, 1 | lecture |
| 7 | `f2-job` | 2 | multiple choice, 1 | lecture |
| 8 | `f2-true` | 2 | multiple choice, 2 | lecture |
| 9 | `f2-spot` | 2 | spot the error, 3 | lecture |
| 10 | `f3-answer` | 3 | matching, 1 | vocabulaire |
| 11 | `f3-rel` | 3 | matching, 1 | vocabulaire |
| 12 | `f3-who` | 3 | multiple choice, 2 | vocabulaire |
| 13 | `f3-spot` | 3 | spot the error, 3 | vocabulaire |
| 14 | `pilot-french-3-1` | 3 | multiple choice, 1 | vocabulaire |
| 15 | `pilot-french-3-2` | 3 | fill the blank, 2 | vocabulaire |
| 16 | `fc3-3-check` (card fc3-3) | 3 | multiple choice, 1 | vocabulaire |
| 17 | `fc4-3-check` (card fc4-3) | 4 | multiple choice, 1 | articles |
| 18 | `f5-spot` | 5 | spot the error, 3 | conjugaison |
| 19 | `fc5-3-check` (card fc5-3) | 5 | multiple choice, 1 | conjugaison |
| 20 | `f6-self` | 6 | multiple choice, 1 | oral |
| 21 | `f6-other` | 6 | multiple choice, 1 | oral |
| 22 | `f6-order` | 6 | word order, 2 | oral |
| 23 | `f6-spot` | 6 | spot the error, 3 | oral |
| 24 | `fc6-3-check` (card fc6-3) | 6 | multiple choice, 1 | oral |
| 25 | `f7-replace` | 7 | multiple choice, 1 | pronoms |
| 26 | `f7-sort` | 7 | matching, 1 | pronoms |
| 27 | `f7-person` | 7 | matching, 2 | pronoms |
| 28 | `f7-spot` | 7 | spot the error, 3 | pronoms |
| 29 | `fc7-3-check` (card fc7-3) | 7 | multiple choice, 1 | pronoms |
| 30 | `f8-spot` | 8 | spot the error, 3 | conjugaison |
| 31 | `fc8-3-check` (card fc8-3) | 8 | multiple choice, 1 | conjugaison |
| 32 | `f10-who` | 10 | multiple choice, 1 | lecture |
| 33 | `f10-when` | 10 | multiple choice, 1 | lecture |
| 34 | `f10-true` | 10 | multiple choice, 2 | lecture |
| 35 | `f10-word` | 10 | multiple choice, 3 | lecture |
| 36 | `fc10-3-check` (card fc10-3) | 10 | multiple choice, 1 | lecture |
| 37 | `f11-what` | 11 | multiple choice, 1 | lecture |
| 38 | `f11-true` | 11 | multiple choice, 1 | lecture |
| 39 | `f11-subject` | 11 | multiple choice, 2 | lecture |
| 40 | `f11-word` | 11 | multiple choice, 3 | lecture |
| 41 | `fc11-3-check` (card fc11-3) | 11 | multiple choice, 1 | lecture |
| 42 | `f12-place` | 12 | matching, 1 | vocabulaire |
| 43 | `f12-staff` | 12 | matching, 1 | vocabulaire |
| 44 | `f12-sort` | 12 | matching, 2 | vocabulaire |
| 45 | `f12-spot` | 12 | spot the error, 3 | vocabulaire |
| 46 | `fc12-3-check` (card fc12-3) | 12 | multiple choice, 1 | vocabulaire |
| 47 | `f13-phrase` | 13 | multiple choice, 1 | grammaire |
| 48 | `f13-sujet` | 13 | multiple choice, 1 | grammaire |
| 49 | `f13-verbe` | 13 | multiple choice, 1 | grammaire |
| 50 | `f13-order` | 13 | word order, 2 | grammaire |
| 51 | `f13-spot` | 13 | spot the error, 3 | grammaire |
| 52 | `f14-which` | 14 | multiple choice, 1 | ecriture |
| 53 | `f14-fault` | 14 | multiple choice, 2 | ecriture |
| 54 | `f14-type` | 14 | fill the blank, 3 | ecriture |
| 55 | `fc14-3-check` (card fc14-3) | 14 | multiple choice, 1 | ecriture |
| 56 | `f15-spot` | 15 | spot the error, 3 | possessifs |
| 57 | `fc15-3-check` (card fc15-3) | 15 | multiple choice, 1 | possessifs |

### `f1-sort` · Lesson 1 · matching, level 1

Prompt: Classe les lettres : voyelle ou consonne ?

Pairs (6 shown each time, sorted into groups):

- a → **voyelle**
- e → **voyelle**
- i → **voyelle**
- o → **voyelle**
- u → **voyelle**
- y → **voyelle**
- b → **consonne**
- d → **consonne**
- m → **consonne**
- r → **consonne**
- s → **consonne**
- t → **consonne**
- k → **consonne**
- p → **consonne**


Three generated variants:

> Classe les lettres : voyelle ou consonne ?

Groups: voyelle · consonne
- y → **voyelle**
- e → **voyelle**
- k → **consonne**
- s → **consonne**
- d → **consonne**
- m → **consonne**

Full working after a second miss:

> Les bonnes paires sont :  
> y → voyelle  
> e → voyelle  
> k → consonne  
> s → consonne  
> d → consonne  
> m → consonne  

> Classe les lettres : voyelle ou consonne ?

Groups: voyelle · consonne
- b → **consonne**
- k → **consonne**
- m → **consonne**
- r → **consonne**
- d → **consonne**
- o → **voyelle**

Full working after a second miss:

> Les bonnes paires sont :  
> b → consonne  
> k → consonne  
> m → consonne  
> r → consonne  
> d → consonne  
> o → voyelle  

> Classe les lettres : voyelle ou consonne ?

Groups: voyelle · consonne
- y → **voyelle**
- k → **consonne**
- b → **consonne**
- p → **consonne**
- m → **consonne**
- e → **voyelle**

Full working after a second miss:

> Les bonnes paires sont :  
> y → voyelle  
> k → consonne  
> b → consonne  
> p → consonne  
> m → consonne  
> e → voyelle  

Sources: alphabet (L’alphabet français, voyelles et consonnes, accents, ordre alphabétique (ordre calculé par le code, accents ignorés))

### `f1-accent` · Lesson 1 · multiple choice, level 2

Prompt: Comment s’appelle ce signe ? / {x.t}

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Le signe sur le e de « été » | l’accent aigu | Le signe sur le e de « été » : l’accent aigu. |
| Le signe sur le e de « mère » | l’accent grave | Le signe sur le e de « mère » : l’accent grave. |
| Le signe sur le e de « fenêtre » | l’accent circonflexe | Le signe sur le e de « fenêtre » : l’accent circonflexe. |
| Le signe sous le c de « garçon » | la cédille | Le signe sous le c de « garçon » : la cédille. |
| Le signe sur le i de « maïs » | le tréma | Le signe sur le i de « maïs » : le tréma. |

Right answer: `{x.a}`; wrong choices: `l’accent aigu`, `l’accent grave`, `l’accent circonflexe`, `la cédille`, `le tréma`

- Feedback `other`: “Ce n’est pas ce signe. Relis la liste des accents.”

Three generated variants:

> Comment s’appelle ce signe ?
> Le signe sous le c de « garçon »

- ◻️ l’accent aigu  
  _↳ feedback if chosen: Ce n’est pas ce signe. Relis la liste des accents._
- ◻️ le tréma  
  _↳ feedback if chosen: Ce n’est pas ce signe. Relis la liste des accents._
- ◻️ l’accent circonflexe  
  _↳ feedback if chosen: Ce n’est pas ce signe. Relis la liste des accents._
- ✅ la cédille

Full working after a second miss:

> Le signe sous le c de « garçon » : la cédille.  
> Réponse : la cédille.  

> Comment s’appelle ce signe ?
> Le signe sur le i de « maïs »

- ◻️ l’accent grave  
  _↳ feedback if chosen: Ce n’est pas ce signe. Relis la liste des accents._
- ◻️ l’accent aigu  
  _↳ feedback if chosen: Ce n’est pas ce signe. Relis la liste des accents._
- ✅ le tréma
- ◻️ l’accent circonflexe  
  _↳ feedback if chosen: Ce n’est pas ce signe. Relis la liste des accents._

Full working after a second miss:

> Le signe sur le i de « maïs » : le tréma.  
> Réponse : le tréma.  

> Comment s’appelle ce signe ?
> Le signe sur le i de « maïs »

- ◻️ la cédille  
  _↳ feedback if chosen: Ce n’est pas ce signe. Relis la liste des accents._
- ✅ le tréma
- ◻️ l’accent aigu  
  _↳ feedback if chosen: Ce n’est pas ce signe. Relis la liste des accents._
- ◻️ l’accent grave  
  _↳ feedback if chosen: Ce n’est pas ce signe. Relis la liste des accents._

Full working after a second miss:

> Le signe sur le i de « maïs » : le tréma.  
> Réponse : le tréma.  

Sources: alphabet (L’alphabet français, voyelles et consonnes, accents, ordre alphabétique (ordre calculé par le code, accents ignorés))

### `f1-spot` · Lesson 1 · spot the error, level 3

Prompt: Une phrase est fausse. Laquelle ?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ L’alphabet français a vingt-six lettres.
- ✅ Le y est une voyelle.
- ✅ Le ç porte une cédille.
- ✅ Dans l’ordre alphabétique, « arbre » vient avant « livre ».
- ❌ Le b est une voyelle.  
  _↳ Le b est une consonne._
- ❌ « école » vient après « maison » dans l’ordre alphabétique.  
  _↳ e vient avant m : « école » vient avant « maison »._
- ❌ Le « è » de « mère » porte un accent aigu.  
  _↳ C’est un accent grave._


Three generated variants:

> Une phrase est fausse. Laquelle ?

- ◻️ Dans l’ordre alphabétique, « arbre » vient avant « livre ».
- ◻️ L’alphabet français a vingt-six lettres.
- ◻️ Le ç porte une cédille.
- ✅ Le b est une voyelle.  
  _↳ explanation: Le b est une consonne._

Full working after a second miss:

> La phrase fausse est « Le b est une voyelle. ».  
> Le b est une consonne.  

> Une phrase est fausse. Laquelle ?

- ✅ « école » vient après « maison » dans l’ordre alphabétique.  
  _↳ explanation: e vient avant m : « école » vient avant « maison »._
- ◻️ L’alphabet français a vingt-six lettres.
- ◻️ Dans l’ordre alphabétique, « arbre » vient avant « livre ».
- ◻️ Le y est une voyelle.

Full working after a second miss:

> La phrase fausse est « « école » vient après « maison » dans l’ordre alphabétique. ».  
> e vient avant m : « école » vient avant « maison ».  

> Une phrase est fausse. Laquelle ?

- ✅ Le b est une voyelle.  
  _↳ explanation: Le b est une consonne._
- ◻️ Dans l’ordre alphabétique, « arbre » vient avant « livre ».
- ◻️ Le ç porte une cédille.
- ◻️ L’alphabet français a vingt-six lettres.

Full working after a second miss:

> La phrase fausse est « Le b est une voyelle. ».  
> Le b est une consonne.  

Sources: alphabet (L’alphabet français, voyelles et consonnes, accents, ordre alphabétique (ordre calculé par le code, accents ignorés))

### `fc1-3-check` · Lesson 1 · multiple choice, level 1

Prompt: Quel mot porte un accent aigu ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ été
- ✅ école
- ✅ café
- ✅ élève
- ❌ mère  
  _↳ è est un accent grave._
- ❌ fenêtre  
  _↳ ê est un accent circonflexe._
- ❌ garçon  
  _↳ ç est une cédille._
- ❌ maïs  
  _↳ ï est un tréma._


Three generated variants:

> Quel mot porte un accent aigu ?

- ◻️ garçon  
  _↳ feedback if chosen: ç est une cédille._
- ✅ été
- ◻️ mère  
  _↳ feedback if chosen: è est un accent grave._
- ◻️ maïs  
  _↳ feedback if chosen: ï est un tréma._

Full working after a second miss:

> La bonne réponse est « été ».  
> « garçon » est faux : ç est une cédille.  
> « mère » est faux : è est un accent grave.  
> « maïs » est faux : ï est un tréma.  

> Quel mot porte un accent aigu ?

- ◻️ garçon  
  _↳ feedback if chosen: ç est une cédille._
- ✅ élève
- ◻️ fenêtre  
  _↳ feedback if chosen: ê est un accent circonflexe._
- ◻️ mère  
  _↳ feedback if chosen: è est un accent grave._

Full working after a second miss:

> La bonne réponse est « élève ».  
> « garçon » est faux : ç est une cédille.  
> « fenêtre » est faux : ê est un accent circonflexe.  
> « mère » est faux : è est un accent grave.  

> Quel mot porte un accent aigu ?

- ◻️ maïs  
  _↳ feedback if chosen: ï est un tréma._
- ◻️ garçon  
  _↳ feedback if chosen: ç est une cédille._
- ◻️ mère  
  _↳ feedback if chosen: è est un accent grave._
- ✅ école

Full working after a second miss:

> La bonne réponse est « école ».  
> « maïs » est faux : ï est un tréma.  
> « garçon » est faux : ç est une cédille.  
> « mère » est faux : è est un accent grave.  

Sources: alphabet (L’alphabet français, voyelles et consonnes, accents, ordre alphabétique (ordre calculé par le code, accents ignorés))

### `f2-who` · Lesson 2 · multiple choice, level 1

Prompt: « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. » / {x.t}

Table `x` (one row is picked each time):

| t | a | why | q |
|---|---|---|---|
| Comment s’appelle le grand frère de Ngono ? | Paul | Comment s’appelle le grand frère de Ngono ? → Paul. | Comment s’appelle le grand frère de Ngono ? |
| Comment s’appelle la petite sœur de Ngono ? | Lisette | Comment s’appelle la petite sœur de Ngono ? → Lisette. | Comment s’appelle la petite sœur de Ngono ? |
| Comment s’appelle le père de Ngono ? | Monsieur Tchoua | Comment s’appelle le père de Ngono ? → Monsieur Tchoua. | Comment s’appelle le père de Ngono ? |
| Qui raconte l’histoire ? | Ngono | Qui raconte l’histoire ? → Ngono. | Qui raconte l’histoire ? |

Right answer: `{x.a}`; wrong choices: `Paul`, `Lisette`, `Monsieur Tchoua`, `Madame Tchoua`, `Ngono`

- Feedback `other`: “Relis la phrase du texte qui parle de cette personne.”

Three generated variants:

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Comment s’appelle le grand frère de Ngono ?

- ◻️ Monsieur Tchoua  
  _↳ feedback if chosen: Relis la phrase du texte qui parle de cette personne._
- ✅ Paul
- ◻️ Ngono  
  _↳ feedback if chosen: Relis la phrase du texte qui parle de cette personne._
- ◻️ Lisette  
  _↳ feedback if chosen: Relis la phrase du texte qui parle de cette personne._

Full working after a second miss:

> Comment s’appelle le grand frère de Ngono ? → Paul.  
> Réponse : Paul.  

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Comment s’appelle le grand frère de Ngono ?

- ◻️ Lisette  
  _↳ feedback if chosen: Relis la phrase du texte qui parle de cette personne._
- ◻️ Ngono  
  _↳ feedback if chosen: Relis la phrase du texte qui parle de cette personne._
- ✅ Paul
- ◻️ Madame Tchoua  
  _↳ feedback if chosen: Relis la phrase du texte qui parle de cette personne._

Full working after a second miss:

> Comment s’appelle le grand frère de Ngono ? → Paul.  
> Réponse : Paul.  

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Comment s’appelle le père de Ngono ?

- ✅ Monsieur Tchoua
- ◻️ Ngono  
  _↳ feedback if chosen: Relis la phrase du texte qui parle de cette personne._
- ◻️ Lisette  
  _↳ feedback if chosen: Relis la phrase du texte qui parle de cette personne._
- ◻️ Paul  
  _↳ feedback if chosen: Relis la phrase du texte qui parle de cette personne._

Full working after a second miss:

> Comment s’appelle le père de Ngono ? → Monsieur Tchoua.  
> Réponse : Monsieur Tchoua.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f2-family` · Lesson 2 · multiple choice, level 1

Prompt: Qui fait partie de la famille nucléaire ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ le père
- ✅ la mère
- ✅ les enfants
- ❌ le grand-père  
  _↳ Les grands-parents font partie de la famille élargie._
- ❌ l’oncle  
  _↳ L’oncle fait partie de la famille élargie._
- ❌ la cousine  
  _↳ La cousine fait partie de la famille élargie._
- ❌ le voisin  
  _↳ Le voisin ne fait pas partie de la famille._


Three generated variants:

> Qui fait partie de la famille nucléaire ?

- ◻️ l’oncle  
  _↳ feedback if chosen: L’oncle fait partie de la famille élargie._
- ◻️ le grand-père  
  _↳ feedback if chosen: Les grands-parents font partie de la famille élargie._
- ✅ le père
- ◻️ le voisin  
  _↳ feedback if chosen: Le voisin ne fait pas partie de la famille._

Full working after a second miss:

> La bonne réponse est « le père ».  
> « l’oncle » est faux : L’oncle fait partie de la famille élargie.  
> « le grand-père » est faux : Les grands-parents font partie de la famille élargie.  
> « le voisin » est faux : Le voisin ne fait pas partie de la famille.  

> Qui fait partie de la famille nucléaire ?

- ◻️ le voisin  
  _↳ feedback if chosen: Le voisin ne fait pas partie de la famille._
- ✅ le père
- ◻️ la cousine  
  _↳ feedback if chosen: La cousine fait partie de la famille élargie._
- ◻️ l’oncle  
  _↳ feedback if chosen: L’oncle fait partie de la famille élargie._

Full working after a second miss:

> La bonne réponse est « le père ».  
> « le voisin » est faux : Le voisin ne fait pas partie de la famille.  
> « la cousine » est faux : La cousine fait partie de la famille élargie.  
> « l’oncle » est faux : L’oncle fait partie de la famille élargie.  

> Qui fait partie de la famille nucléaire ?

- ◻️ le voisin  
  _↳ feedback if chosen: Le voisin ne fait pas partie de la famille._
- ◻️ le grand-père  
  _↳ feedback if chosen: Les grands-parents font partie de la famille élargie._
- ◻️ la cousine  
  _↳ feedback if chosen: La cousine fait partie de la famille élargie._
- ✅ le père

Full working after a second miss:

> La bonne réponse est « le père ».  
> « le voisin » est faux : Le voisin ne fait pas partie de la famille.  
> « le grand-père » est faux : Les grands-parents font partie de la famille élargie.  
> « la cousine » est faux : La cousine fait partie de la famille élargie.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f2-job` · Lesson 2 · multiple choice, level 1

Prompt: « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. » / {x.t}

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Quel est le métier du père ? | enseignant | Quel est le métier du père ? → enseignant. |
| Quel est le métier de la mère ? | couturière | Quel est le métier de la mère ? → couturière. |

Right answer: `{x.a}`; wrong choices: `enseignant`, `couturière`, `cultivateur`, `médecin`, `commerçant`

- Feedback `other`: “Relis la phrase qui parle de cette personne.”

Three generated variants:

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Quel est le métier de la mère ?

- ◻️ commerçant  
  _↳ feedback if chosen: Relis la phrase qui parle de cette personne._
- ◻️ enseignant  
  _↳ feedback if chosen: Relis la phrase qui parle de cette personne._
- ✅ couturière

Full working after a second miss:

> Quel est le métier de la mère ? → couturière.  
> Réponse : couturière.  

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Quel est le métier de la mère ?

- ◻️ cultivateur  
  _↳ feedback if chosen: Relis la phrase qui parle de cette personne._
- ◻️ médecin  
  _↳ feedback if chosen: Relis la phrase qui parle de cette personne._
- ✅ couturière

Full working after a second miss:

> Quel est le métier de la mère ? → couturière.  
> Réponse : couturière.  

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Quel est le métier de la mère ?

- ◻️ médecin  
  _↳ feedback if chosen: Relis la phrase qui parle de cette personne._
- ◻️ commerçant  
  _↳ feedback if chosen: Relis la phrase qui parle de cette personne._
- ✅ couturière

Full working after a second miss:

> Quel est le métier de la mère ? → couturière.  
> Réponse : couturière.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f2-true` · Lesson 2 · multiple choice, level 2

Prompt: « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. » / Quelle phrase est vraie d’après le texte ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Ngono habite à Bafoussam.
- ✅ Ngono a une petite sœur.
- ✅ Le samedi, la famille va au marché.
- ❌ Ngono habite au village.  
  _↳ Ngono habite à Bafoussam ; ses grands-parents habitent au village._
- ❌ Ngono a douze ans.  
  _↳ Le texte dit : « J’ai onze ans »._
- ❌ La mère de Ngono est enseignante.  
  _↳ La mère est couturière ; c’est le père qui est enseignant._
- ❌ Ngono est l’aîné de la famille.  
  _↳ Ngono a un grand frère, Paul._


Three generated variants:

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Quelle phrase est vraie d’après le texte ?

- ◻️ La mère de Ngono est enseignante.  
  _↳ feedback if chosen: La mère est couturière ; c’est le père qui est enseignant._
- ✅ Ngono habite à Bafoussam.
- ◻️ Ngono habite au village.  
  _↳ feedback if chosen: Ngono habite à Bafoussam ; ses grands-parents habitent au village._
- ◻️ Ngono a douze ans.  
  _↳ feedback if chosen: Le texte dit : « J’ai onze ans »._

Full working after a second miss:

> La bonne réponse est « Ngono habite à Bafoussam. ».  
> « La mère de Ngono est enseignante. » est faux : La mère est couturière ; c’est le père qui est enseignant.  
> « Ngono habite au village. » est faux : Ngono habite à Bafoussam ; ses grands-parents habitent au village.  
> « Ngono a douze ans. » est faux : Le texte dit : « J’ai onze ans ».  

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Quelle phrase est vraie d’après le texte ?

- ◻️ La mère de Ngono est enseignante.  
  _↳ feedback if chosen: La mère est couturière ; c’est le père qui est enseignant._
- ◻️ Ngono est l’aîné de la famille.  
  _↳ feedback if chosen: Ngono a un grand frère, Paul._
- ✅ Ngono a une petite sœur.
- ◻️ Ngono a douze ans.  
  _↳ feedback if chosen: Le texte dit : « J’ai onze ans »._

Full working after a second miss:

> La bonne réponse est « Ngono a une petite sœur. ».  
> « La mère de Ngono est enseignante. » est faux : La mère est couturière ; c’est le père qui est enseignant.  
> « Ngono est l’aîné de la famille. » est faux : Ngono a un grand frère, Paul.  
> « Ngono a douze ans. » est faux : Le texte dit : « J’ai onze ans ».  

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Quelle phrase est vraie d’après le texte ?

- ◻️ Ngono est l’aîné de la famille.  
  _↳ feedback if chosen: Ngono a un grand frère, Paul._
- ◻️ La mère de Ngono est enseignante.  
  _↳ feedback if chosen: La mère est couturière ; c’est le père qui est enseignant._
- ◻️ Ngono a douze ans.  
  _↳ feedback if chosen: Le texte dit : « J’ai onze ans »._
- ✅ Ngono habite à Bafoussam.

Full working after a second miss:

> La bonne réponse est « Ngono habite à Bafoussam. ».  
> « Ngono est l’aîné de la famille. » est faux : Ngono a un grand frère, Paul.  
> « La mère de Ngono est enseignante. » est faux : La mère est couturière ; c’est le père qui est enseignant.  
> « Ngono a douze ans. » est faux : Le texte dit : « J’ai onze ans ».  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f2-spot` · Lesson 2 · spot the error, level 3

Prompt: « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. » / Une phrase est fausse d’après le texte. Laquelle ?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Paul est le grand frère de Ngono.
- ✅ Le père s’appelle Monsieur Tchoua.
- ✅ La famille mange ensemble le soir.
- ✅ Les grands-parents habitent au village.
- ❌ Lisette est la grande sœur de Ngono.  
  _↳ Lisette est la petite sœur._
- ❌ Le dimanche, la famille va au marché.  
  _↳ Le texte dit « le samedi »._
- ❌ Ngono habite à Douala.  
  _↳ Ngono habite à Bafoussam._


Three generated variants:

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Une phrase est fausse d’après le texte. Laquelle ?

- ◻️ La famille mange ensemble le soir.
- ✅ Le dimanche, la famille va au marché.  
  _↳ explanation: Le texte dit « le samedi »._
- ◻️ Les grands-parents habitent au village.
- ◻️ Le père s’appelle Monsieur Tchoua.

Full working after a second miss:

> La phrase fausse est « Le dimanche, la famille va au marché. ».  
> Le texte dit « le samedi ».  

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Une phrase est fausse d’après le texte. Laquelle ?

- ✅ Lisette est la grande sœur de Ngono.  
  _↳ explanation: Lisette est la petite sœur._
- ◻️ La famille mange ensemble le soir.
- ◻️ Le père s’appelle Monsieur Tchoua.
- ◻️ Paul est le grand frère de Ngono.

Full working after a second miss:

> La phrase fausse est « Lisette est la grande sœur de Ngono. ».  
> Lisette est la petite sœur.  

> « Je m’appelle Ngono. J’ai onze ans et j’habite à Bafoussam avec ma famille. Mon père, Monsieur Tchoua, est enseignant. Ma mère, Madame Tchoua, est couturière. J’ai un grand frère, Paul, et une petite sœur, Lisette. Le soir, nous mangeons ensemble et chacun raconte sa journée. Le samedi, nous allons au marché, puis nous rendons visite à nos grands-parents au village. »
> Une phrase est fausse d’après le texte. Laquelle ?

- ◻️ La famille mange ensemble le soir.
- ◻️ Le père s’appelle Monsieur Tchoua.
- ✅ Ngono habite à Douala.  
  _↳ explanation: Ngono habite à Bafoussam._
- ◻️ Paul est le grand frère de Ngono.

Full working after a second miss:

> La phrase fausse est « Ngono habite à Douala. ».  
> Ngono habite à Bafoussam.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f3-answer` · Lesson 3 · matching, level 1

Prompt: Relie chaque question à la bonne réponse.

Pairs (4 shown each time):

- Comment t’appelles-tu ? → **Je m’appelle Ngono.**
- Quel âge as-tu ? → **J’ai onze ans.**
- Où habites-tu ? → **J’habite à Bafoussam.**
- Comment vas-tu ? → **Je vais bien, merci.**
- En quelle classe es-tu ? → **Je suis en Form One.**


Three generated variants:

> Relie chaque question à la bonne réponse.

Right-hand side (shuffled): J’habite à Bafoussam. · Je vais bien, merci. · Je suis en Form One. · Je m’appelle Ngono.
- Comment t’appelles-tu ? → **Je m’appelle Ngono.**
- En quelle classe es-tu ? → **Je suis en Form One.**
- Où habites-tu ? → **J’habite à Bafoussam.**
- Comment vas-tu ? → **Je vais bien, merci.**

Full working after a second miss:

> Les bonnes paires sont :  
> Comment t’appelles-tu ? → Je m’appelle Ngono.  
> En quelle classe es-tu ? → Je suis en Form One.  
> Où habites-tu ? → J’habite à Bafoussam.  
> Comment vas-tu ? → Je vais bien, merci.  

> Relie chaque question à la bonne réponse.

Right-hand side (shuffled): Je suis en Form One. · Je m’appelle Ngono. · J’ai onze ans. · Je vais bien, merci.
- En quelle classe es-tu ? → **Je suis en Form One.**
- Comment vas-tu ? → **Je vais bien, merci.**
- Comment t’appelles-tu ? → **Je m’appelle Ngono.**
- Quel âge as-tu ? → **J’ai onze ans.**

Full working after a second miss:

> Les bonnes paires sont :  
> En quelle classe es-tu ? → Je suis en Form One.  
> Comment vas-tu ? → Je vais bien, merci.  
> Comment t’appelles-tu ? → Je m’appelle Ngono.  
> Quel âge as-tu ? → J’ai onze ans.  

> Relie chaque question à la bonne réponse.

Right-hand side (shuffled): J’ai onze ans. · Je m’appelle Ngono. · J’habite à Bafoussam. · Je suis en Form One.
- Quel âge as-tu ? → **J’ai onze ans.**
- Où habites-tu ? → **J’habite à Bafoussam.**
- Comment t’appelles-tu ? → **Je m’appelle Ngono.**
- En quelle classe es-tu ? → **Je suis en Form One.**

Full working after a second miss:

> Les bonnes paires sont :  
> Quel âge as-tu ? → J’ai onze ans.  
> Où habites-tu ? → J’habite à Bafoussam.  
> Comment t’appelles-tu ? → Je m’appelle Ngono.  
> En quelle classe es-tu ? → Je suis en Form One.  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `f3-rel` · Lesson 3 · matching, level 1

Prompt: Relie pour trouver le membre de la famille.

Pairs (4 shown each time):

- le père de mon père → **mon grand-père**
- la mère de ma mère → **ma grand-mère**
- le frère de mon père → **mon oncle**
- la sœur de ma mère → **ma tante**
- le fils de mon oncle → **mon cousin**
- la fille de ma tante → **ma cousine**


Three generated variants:

> Relie pour trouver le membre de la famille.

Right-hand side (shuffled): mon cousin · ma tante · ma grand-mère · mon oncle
- la sœur de ma mère → **ma tante**
- le fils de mon oncle → **mon cousin**
- la mère de ma mère → **ma grand-mère**
- le frère de mon père → **mon oncle**

Full working after a second miss:

> Les bonnes paires sont :  
> la sœur de ma mère → ma tante  
> le fils de mon oncle → mon cousin  
> la mère de ma mère → ma grand-mère  
> le frère de mon père → mon oncle  

> Relie pour trouver le membre de la famille.

Right-hand side (shuffled): ma grand-mère · ma cousine · ma tante · mon cousin
- la sœur de ma mère → **ma tante**
- la fille de ma tante → **ma cousine**
- le fils de mon oncle → **mon cousin**
- la mère de ma mère → **ma grand-mère**

Full working after a second miss:

> Les bonnes paires sont :  
> la sœur de ma mère → ma tante  
> la fille de ma tante → ma cousine  
> le fils de mon oncle → mon cousin  
> la mère de ma mère → ma grand-mère  

> Relie pour trouver le membre de la famille.

Right-hand side (shuffled): ma tante · mon oncle · mon cousin · ma cousine
- la fille de ma tante → **ma cousine**
- la sœur de ma mère → **ma tante**
- le frère de mon père → **mon oncle**
- le fils de mon oncle → **mon cousin**

Full working after a second miss:

> Les bonnes paires sont :  
> la fille de ma tante → ma cousine  
> la sœur de ma mère → ma tante  
> le frère de mon père → mon oncle  
> le fils de mon oncle → mon cousin  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `f3-who` · Lesson 3 · multiple choice, level 2

Prompt: {x.t}

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Qui est le père de mon père ? | mon grand-père | Qui est le père de mon père ? → mon grand-père. |
| Qui est la mère de ma mère ? | ma grand-mère | Qui est la mère de ma mère ? → ma grand-mère. |
| Qui est le frère de mon père ? | mon oncle | Qui est le frère de mon père ? → mon oncle. |
| Qui est la sœur de ma mère ? | ma tante | Qui est la sœur de ma mère ? → ma tante. |
| Qui est le fils de mon oncle ? | mon cousin | Qui est le fils de mon oncle ? → mon cousin. |
| Qui est la fille de ma tante ? | ma cousine | Qui est la fille de ma tante ? → ma cousine. |

Right answer: `{x.a}`; wrong choices: `mon grand-père`, `ma grand-mère`, `mon oncle`, `ma tante`, `mon cousin`, `ma cousine`

- Feedback `other`: “Ce n’est pas cette personne. Lis bien : père ou mère ? frère ou sœur ?”

Three generated variants:

> Qui est la fille de ma tante ?

- ◻️ ma grand-mère  
  _↳ feedback if chosen: Ce n’est pas cette personne. Lis bien : père ou mère ? frère ou sœur ?_
- ✅ ma cousine
- ◻️ mon grand-père  
  _↳ feedback if chosen: Ce n’est pas cette personne. Lis bien : père ou mère ? frère ou sœur ?_
- ◻️ mon oncle  
  _↳ feedback if chosen: Ce n’est pas cette personne. Lis bien : père ou mère ? frère ou sœur ?_

Full working after a second miss:

> Qui est la fille de ma tante ? → ma cousine.  
> Réponse : ma cousine.  

> Qui est la fille de ma tante ?

- ✅ ma cousine
- ◻️ mon oncle  
  _↳ feedback if chosen: Ce n’est pas cette personne. Lis bien : père ou mère ? frère ou sœur ?_
- ◻️ mon cousin  
  _↳ feedback if chosen: Ce n’est pas cette personne. Lis bien : père ou mère ? frère ou sœur ?_
- ◻️ ma grand-mère  
  _↳ feedback if chosen: Ce n’est pas cette personne. Lis bien : père ou mère ? frère ou sœur ?_

Full working after a second miss:

> Qui est la fille de ma tante ? → ma cousine.  
> Réponse : ma cousine.  

> Qui est la sœur de ma mère ?

- ◻️ ma cousine  
  _↳ feedback if chosen: Ce n’est pas cette personne. Lis bien : père ou mère ? frère ou sœur ?_
- ✅ ma tante
- ◻️ mon oncle  
  _↳ feedback if chosen: Ce n’est pas cette personne. Lis bien : père ou mère ? frère ou sœur ?_
- ◻️ mon grand-père  
  _↳ feedback if chosen: Ce n’est pas cette personne. Lis bien : père ou mère ? frère ou sœur ?_

Full working after a second miss:

> Qui est la sœur de ma mère ? → ma tante.  
> Réponse : ma tante.  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `f3-spot` · Lesson 3 · spot the error, level 3

Prompt: Une phrase est fausse. Laquelle ?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Le frère de ma mère est mon oncle.
- ✅ La mère de mon père est ma grand-mère.
- ✅ On dit « J’ai onze ans » pour donner son âge.
- ✅ La fille de mon oncle est ma cousine.
- ❌ On dit « Je suis onze ans » pour donner son âge.  
  _↳ On dit « J’ai onze ans » (avec le verbe avoir)._
- ❌ La sœur de mon père est ma cousine.  
  _↳ La sœur de mon père est ma tante._
- ❌ Le fils de ma tante est mon oncle.  
  _↳ Le fils de ma tante est mon cousin._


Three generated variants:

> Une phrase est fausse. Laquelle ?

- ◻️ La fille de mon oncle est ma cousine.
- ◻️ On dit « J’ai onze ans » pour donner son âge.
- ✅ La sœur de mon père est ma cousine.  
  _↳ explanation: La sœur de mon père est ma tante._
- ◻️ Le frère de ma mère est mon oncle.

Full working after a second miss:

> La phrase fausse est « La sœur de mon père est ma cousine. ».  
> La sœur de mon père est ma tante.  

> Une phrase est fausse. Laquelle ?

- ◻️ On dit « J’ai onze ans » pour donner son âge.
- ◻️ Le frère de ma mère est mon oncle.
- ✅ Le fils de ma tante est mon oncle.  
  _↳ explanation: Le fils de ma tante est mon cousin._
- ◻️ La mère de mon père est ma grand-mère.

Full working after a second miss:

> La phrase fausse est « Le fils de ma tante est mon oncle. ».  
> Le fils de ma tante est mon cousin.  

> Une phrase est fausse. Laquelle ?

- ◻️ On dit « J’ai onze ans » pour donner son âge.
- ◻️ Le frère de ma mère est mon oncle.
- ◻️ La fille de mon oncle est ma cousine.
- ✅ La sœur de mon père est ma cousine.  
  _↳ explanation: La sœur de mon père est ma tante._

Full working after a second miss:

> La phrase fausse est « La sœur de mon père est ma cousine. ».  
> La sœur de mon père est ma tante.  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `pilot-french-3-1` · Lesson 3 · multiple choice, level 1

Prompt: NGONO : Comment t’appelles-tu ? / BIH : Je m’appelle Bih. J’habite à Buea. / Quelle phrase donne le lieu où Bih habite ?

Right answer: `J’habite à Buea.`; wrong choices: `Je m’appelle Bih.`, `Comment t’appelles-tu ?`

- Feedback `activity-choice-0`: “« J’habite à … » indique le lieu où l’on habite.”
- Feedback `activity-choice-1`: “« J’habite à … » indique le lieu où l’on habite.”

Three generated variants:

> NGONO : Comment t’appelles-tu ?
> BIH : Je m’appelle Bih. J’habite à Buea.
> Quelle phrase donne le lieu où Bih habite ?

- ◻️ Je m’appelle Bih.  
  _↳ feedback if chosen: « J’habite à … » indique le lieu où l’on habite._
- ◻️ Comment t’appelles-tu ?  
  _↳ feedback if chosen: « J’habite à … » indique le lieu où l’on habite._
- ✅ J’habite à Buea.

Full working after a second miss:

> « J’habite à … » indique le lieu où l’on habite.  

> NGONO : Comment t’appelles-tu ?
> BIH : Je m’appelle Bih. J’habite à Buea.
> Quelle phrase donne le lieu où Bih habite ?

- ✅ J’habite à Buea.
- ◻️ Je m’appelle Bih.  
  _↳ feedback if chosen: « J’habite à … » indique le lieu où l’on habite._
- ◻️ Comment t’appelles-tu ?  
  _↳ feedback if chosen: « J’habite à … » indique le lieu où l’on habite._

Full working after a second miss:

> « J’habite à … » indique le lieu où l’on habite.  

> NGONO : Comment t’appelles-tu ?
> BIH : Je m’appelle Bih. J’habite à Buea.
> Quelle phrase donne le lieu où Bih habite ?

- ✅ J’habite à Buea.
- ◻️ Comment t’appelles-tu ?  
  _↳ feedback if chosen: « J’habite à … » indique le lieu où l’on habite._
- ◻️ Je m’appelle Bih.  
  _↳ feedback if chosen: « J’habite à … » indique le lieu où l’on habite._

Full working after a second miss:

> « J’habite à … » indique le lieu où l’on habite.  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `pilot-french-3-2` · Lesson 3 · fill the blank, level 2

Prompt: Pour dire mon nom : Je ___ Ngono.
Sentence: Pour dire mon nom : Je ___ Ngono.
Right answer: `'m’appelle'`

Choices: `m’appelle`, `habite`, `suis`

- Feedback `activity-choice-0`: “Pour donner son nom, on dit : Je m’appelle Ngono.”
- Feedback `activity-choice-1`: “Pour donner son nom, on dit : Je m’appelle Ngono.”
- Feedback `activity-choice-2`: “Pour donner son nom, on dit : Je m’appelle Ngono.”

Three generated variants:

> undefined

Sentence: **Pour dire mon nom : Je ___ Ngono.**
- ◻️ habite  
  _↳ feedback if chosen: Pour donner son nom, on dit : Je m’appelle Ngono._
- ✅ m’appelle
- ◻️ suis  
  _↳ feedback if chosen: Pour donner son nom, on dit : Je m’appelle Ngono._

Full working after a second miss:

> Pour donner son nom, on dit : Je m’appelle Ngono.  

> undefined

Sentence: **Pour dire mon nom : Je ___ Ngono.**
- ✅ m’appelle
- ◻️ suis  
  _↳ feedback if chosen: Pour donner son nom, on dit : Je m’appelle Ngono._
- ◻️ habite  
  _↳ feedback if chosen: Pour donner son nom, on dit : Je m’appelle Ngono._

Full working after a second miss:

> Pour donner son nom, on dit : Je m’appelle Ngono.  

> undefined

Sentence: **Pour dire mon nom : Je ___ Ngono.**
- ◻️ suis  
  _↳ feedback if chosen: Pour donner son nom, on dit : Je m’appelle Ngono._
- ◻️ habite  
  _↳ feedback if chosen: Pour donner son nom, on dit : Je m’appelle Ngono._
- ✅ m’appelle

Full working after a second miss:

> Pour donner son nom, on dit : Je m’appelle Ngono.  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `fc3-3-check` · Lesson 3 · multiple choice, level 1

Prompt: Quel est un rôle des enfants dans la famille ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ respecter leurs parents
- ✅ aider à la maison
- ✅ bien travailler à l’école
- ❌ payer la maison  
  _↳ Ce sont les parents qui s’en occupent._
- ❌ ne jamais aider  
  _↳ Les enfants aident à la maison._
- ❌ désobéir aux parents  
  _↳ Les enfants respectent leurs parents._
- ❌ refuser d’aller à l’école  
  _↳ Les enfants vont à l’école et travaillent bien._


Three generated variants:

> Quel est un rôle des enfants dans la famille ?

- ✅ aider à la maison
- ◻️ payer la maison  
  _↳ feedback if chosen: Ce sont les parents qui s’en occupent._
- ◻️ refuser d’aller à l’école  
  _↳ feedback if chosen: Les enfants vont à l’école et travaillent bien._
- ◻️ désobéir aux parents  
  _↳ feedback if chosen: Les enfants respectent leurs parents._

Full working after a second miss:

> La bonne réponse est « aider à la maison ».  
> « payer la maison » est faux : Ce sont les parents qui s’en occupent.  
> « refuser d’aller à l’école » est faux : Les enfants vont à l’école et travaillent bien.  
> « désobéir aux parents » est faux : Les enfants respectent leurs parents.  

> Quel est un rôle des enfants dans la famille ?

- ◻️ refuser d’aller à l’école  
  _↳ feedback if chosen: Les enfants vont à l’école et travaillent bien._
- ◻️ payer la maison  
  _↳ feedback if chosen: Ce sont les parents qui s’en occupent._
- ◻️ désobéir aux parents  
  _↳ feedback if chosen: Les enfants respectent leurs parents._
- ✅ respecter leurs parents

Full working after a second miss:

> La bonne réponse est « respecter leurs parents ».  
> « refuser d’aller à l’école » est faux : Les enfants vont à l’école et travaillent bien.  
> « payer la maison » est faux : Ce sont les parents qui s’en occupent.  
> « désobéir aux parents » est faux : Les enfants respectent leurs parents.  

> Quel est un rôle des enfants dans la famille ?

- ✅ bien travailler à l’école
- ◻️ refuser d’aller à l’école  
  _↳ feedback if chosen: Les enfants vont à l’école et travaillent bien._
- ◻️ désobéir aux parents  
  _↳ feedback if chosen: Les enfants respectent leurs parents._
- ◻️ payer la maison  
  _↳ feedback if chosen: Ce sont les parents qui s’en occupent._

Full working after a second miss:

> La bonne réponse est « bien travailler à l’école ».  
> « refuser d’aller à l’école » est faux : Les enfants vont à l’école et travaillent bien.  
> « désobéir aux parents » est faux : Les enfants respectent leurs parents.  
> « payer la maison » est faux : Ce sont les parents qui s’en occupent.  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `fc4-3-check` · Lesson 4 · multiple choice, level 1

Prompt: Laquelle est correcte ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ le haricot
- ❌ l’haricot  
  _↳ « haricot » commence par un h aspiré : on écrit le haricot._
- ❌ la haricot  
  _↳ « haricot » est masculin._
- ❌ les haricot  
  _↳ Au pluriel : les haricots._
- ❌ un haricots  
  _↳ Au singulier : un haricot._


Three generated variants:

> Laquelle est correcte ?

- ◻️ la haricot  
  _↳ feedback if chosen: « haricot » est masculin._
- ◻️ un haricots  
  _↳ feedback if chosen: Au singulier : un haricot._
- ◻️ les haricot  
  _↳ feedback if chosen: Au pluriel : les haricots._
- ✅ le haricot

Full working after a second miss:

> La bonne réponse est « le haricot ».  
> « la haricot » est faux : « haricot » est masculin.  
> « un haricots » est faux : Au singulier : un haricot.  
> « les haricot » est faux : Au pluriel : les haricots.  

> Laquelle est correcte ?

- ◻️ un haricots  
  _↳ feedback if chosen: Au singulier : un haricot._
- ◻️ la haricot  
  _↳ feedback if chosen: « haricot » est masculin._
- ✅ le haricot
- ◻️ l’haricot  
  _↳ feedback if chosen: « haricot » commence par un h aspiré : on écrit le haricot._

Full working after a second miss:

> La bonne réponse est « le haricot ».  
> « un haricots » est faux : Au singulier : un haricot.  
> « la haricot » est faux : « haricot » est masculin.  
> « l’haricot » est faux : « haricot » commence par un h aspiré : on écrit le haricot.  

> Laquelle est correcte ?

- ◻️ la haricot  
  _↳ feedback if chosen: « haricot » est masculin._
- ✅ le haricot
- ◻️ un haricots  
  _↳ feedback if chosen: Au singulier : un haricot._
- ◻️ les haricot  
  _↳ feedback if chosen: Au pluriel : les haricots._

Full working after a second miss:

> La bonne réponse est « le haricot ».  
> « la haricot » est faux : « haricot » est masculin.  
> « un haricots » est faux : Au singulier : un haricot.  
> « les haricot » est faux : Au pluriel : les haricots.  

Sources: articles (Articles définis et indéfinis ; élision ; h aspiré (le haricot, le hibou))

### `f5-spot` · Lesson 5 · spot the error, level 3

Prompt: Une phrase est fausse. Laquelle ?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Nous avons une maison.
- ✅ Elles s’appellent Lisette et Anne.
- ✅ Tu as un stylo bleu.
- ✅ Je m’appelle Paul.
- ❌ Nous nous appellons Paul et Eric.  
  _↳ Avec nous, un seul l : nous nous appelons._
- ❌ Ils a trois chèvres.  
  _↳ Avec ils : ils ont._
- ❌ Vous avons un ballon.  
  _↳ Avec vous : vous avez._


Three generated variants:

> Une phrase est fausse. Laquelle ?

- ◻️ Je m’appelle Paul.
- ◻️ Nous avons une maison.
- ✅ Ils a trois chèvres.  
  _↳ explanation: Avec ils : ils ont._
- ◻️ Tu as un stylo bleu.

Full working after a second miss:

> La phrase fausse est « Ils a trois chèvres. ».  
> Avec ils : ils ont.  

> Une phrase est fausse. Laquelle ?

- ◻️ Elles s’appellent Lisette et Anne.
- ◻️ Je m’appelle Paul.
- ◻️ Tu as un stylo bleu.
- ✅ Ils a trois chèvres.  
  _↳ explanation: Avec ils : ils ont._

Full working after a second miss:

> La phrase fausse est « Ils a trois chèvres. ».  
> Avec ils : ils ont.  

> Une phrase est fausse. Laquelle ?

- ◻️ Tu as un stylo bleu.
- ◻️ Nous avons une maison.
- ◻️ Elles s’appellent Lisette et Anne.
- ✅ Nous nous appellons Paul et Eric.  
  _↳ explanation: Avec nous, un seul l : nous nous appelons._

Full working after a second miss:

> La phrase fausse est « Nous nous appellons Paul et Eric. ».  
> Avec nous, un seul l : nous nous appelons.  

Sources: conjugaison (Présent de l’indicatif : avoir, s’appeler, verbes en -er (travailler, laver))

### `fc5-3-check` · Lesson 5 · multiple choice, level 1

Prompt: Laquelle est correcte ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ J’ai onze ans.
- ❌ Je ai onze ans.  
  _↳ Devant une voyelle, je devient j’._
- ❌ J’as onze ans.  
  _↳ Avec je : j’ai._
- ❌ Je suis onze ans.  
  _↳ Pour l’âge, on utilise avoir : j’ai._
- ❌ J’a onze ans.  
  _↳ Avec je : j’ai._


Three generated variants:

> Laquelle est correcte ?

- ✅ J’ai onze ans.
- ◻️ Je suis onze ans.  
  _↳ feedback if chosen: Pour l’âge, on utilise avoir : j’ai._
- ◻️ J’as onze ans.  
  _↳ feedback if chosen: Avec je : j’ai._
- ◻️ Je ai onze ans.  
  _↳ feedback if chosen: Devant une voyelle, je devient j’._

Full working after a second miss:

> La bonne réponse est « J’ai onze ans. ».  
> « Je suis onze ans. » est faux : Pour l’âge, on utilise avoir : j’ai.  
> « J’as onze ans. » est faux : Avec je : j’ai.  
> « Je ai onze ans. » est faux : Devant une voyelle, je devient j’.  

> Laquelle est correcte ?

- ✅ J’ai onze ans.
- ◻️ Je ai onze ans.  
  _↳ feedback if chosen: Devant une voyelle, je devient j’._
- ◻️ Je suis onze ans.  
  _↳ feedback if chosen: Pour l’âge, on utilise avoir : j’ai._
- ◻️ J’a onze ans.  
  _↳ feedback if chosen: Avec je : j’ai._

Full working after a second miss:

> La bonne réponse est « J’ai onze ans. ».  
> « Je ai onze ans. » est faux : Devant une voyelle, je devient j’.  
> « Je suis onze ans. » est faux : Pour l’âge, on utilise avoir : j’ai.  
> « J’a onze ans. » est faux : Avec je : j’ai.  

> Laquelle est correcte ?

- ✅ J’ai onze ans.
- ◻️ J’as onze ans.  
  _↳ feedback if chosen: Avec je : j’ai._
- ◻️ Je ai onze ans.  
  _↳ feedback if chosen: Devant une voyelle, je devient j’._
- ◻️ J’a onze ans.  
  _↳ feedback if chosen: Avec je : j’ai._

Full working after a second miss:

> La bonne réponse est « J’ai onze ans. ».  
> « J’as onze ans. » est faux : Avec je : j’ai.  
> « Je ai onze ans. » est faux : Devant une voyelle, je devient j’.  
> « J’a onze ans. » est faux : Avec je : j’ai.  

Sources: conjugaison (Présent de l’indicatif : avoir, s’appeler, verbes en -er (travailler, laver))

### `f6-self` · Lesson 6 · multiple choice, level 1

Prompt: Quelle phrase sert à se présenter ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Je m’appelle Ngono.
- ✅ J’ai onze ans.
- ✅ J’habite à Bafoussam.
- ❌ Voici mon ami Paul.  
  _↳ Cette phrase présente une autre personne._
- ❌ Comment t’appelles-tu ?  
  _↳ C’est une question, pas une présentation._
- ❌ Il s’appelle Eric.  
  _↳ Cette phrase parle d’une autre personne._
- ❌ Au revoir !  
  _↳ C’est pour partir, pas pour se présenter._


Three generated variants:

> Quelle phrase sert à se présenter ?

- ◻️ Voici mon ami Paul.  
  _↳ feedback if chosen: Cette phrase présente une autre personne._
- ✅ J’ai onze ans.
- ◻️ Au revoir !  
  _↳ feedback if chosen: C’est pour partir, pas pour se présenter._
- ◻️ Il s’appelle Eric.  
  _↳ feedback if chosen: Cette phrase parle d’une autre personne._

Full working after a second miss:

> La bonne réponse est « J’ai onze ans. ».  
> « Voici mon ami Paul. » est faux : Cette phrase présente une autre personne.  
> « Au revoir ! » est faux : C’est pour partir, pas pour se présenter.  
> « Il s’appelle Eric. » est faux : Cette phrase parle d’une autre personne.  

> Quelle phrase sert à se présenter ?

- ◻️ Comment t’appelles-tu ?  
  _↳ feedback if chosen: C’est une question, pas une présentation._
- ◻️ Voici mon ami Paul.  
  _↳ feedback if chosen: Cette phrase présente une autre personne._
- ◻️ Il s’appelle Eric.  
  _↳ feedback if chosen: Cette phrase parle d’une autre personne._
- ✅ J’habite à Bafoussam.

Full working after a second miss:

> La bonne réponse est « J’habite à Bafoussam. ».  
> « Comment t’appelles-tu ? » est faux : C’est une question, pas une présentation.  
> « Voici mon ami Paul. » est faux : Cette phrase présente une autre personne.  
> « Il s’appelle Eric. » est faux : Cette phrase parle d’une autre personne.  

> Quelle phrase sert à se présenter ?

- ◻️ Voici mon ami Paul.  
  _↳ feedback if chosen: Cette phrase présente une autre personne._
- ◻️ Il s’appelle Eric.  
  _↳ feedback if chosen: Cette phrase parle d’une autre personne._
- ◻️ Au revoir !  
  _↳ feedback if chosen: C’est pour partir, pas pour se présenter._
- ✅ J’habite à Bafoussam.

Full working after a second miss:

> La bonne réponse est « J’habite à Bafoussam. ».  
> « Voici mon ami Paul. » est faux : Cette phrase présente une autre personne.  
> « Il s’appelle Eric. » est faux : Cette phrase parle d’une autre personne.  
> « Au revoir ! » est faux : C’est pour partir, pas pour se présenter.  

Sources: oral (Se présenter et présenter quelqu’un ; politesse (tu / vous))

### `f6-other` · Lesson 6 · multiple choice, level 1

Prompt: Quelle phrase sert à présenter quelqu’un d’autre ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Voici mon ami Paul.
- ✅ Je te présente ma sœur Lisette.
- ✅ Il s’appelle Eric.
- ❌ Je m’appelle Ngono.  
  _↳ Là, tu te présentes toi-même._
- ❌ J’ai onze ans.  
  _↳ Là, tu parles de toi._
- ❌ Où habites-tu ?  
  _↳ C’est une question._
- ❌ Merci beaucoup.  
  _↳ C’est un remerciement._


Three generated variants:

> Quelle phrase sert à présenter quelqu’un d’autre ?

- ◻️ Où habites-tu ?  
  _↳ feedback if chosen: C’est une question._
- ✅ Je te présente ma sœur Lisette.
- ◻️ Je m’appelle Ngono.  
  _↳ feedback if chosen: Là, tu te présentes toi-même._
- ◻️ J’ai onze ans.  
  _↳ feedback if chosen: Là, tu parles de toi._

Full working after a second miss:

> La bonne réponse est « Je te présente ma sœur Lisette. ».  
> « Où habites-tu ? » est faux : C’est une question.  
> « Je m’appelle Ngono. » est faux : Là, tu te présentes toi-même.  
> « J’ai onze ans. » est faux : Là, tu parles de toi.  

> Quelle phrase sert à présenter quelqu’un d’autre ?

- ◻️ J’ai onze ans.  
  _↳ feedback if chosen: Là, tu parles de toi._
- ✅ Il s’appelle Eric.
- ◻️ Où habites-tu ?  
  _↳ feedback if chosen: C’est une question._
- ◻️ Merci beaucoup.  
  _↳ feedback if chosen: C’est un remerciement._

Full working after a second miss:

> La bonne réponse est « Il s’appelle Eric. ».  
> « J’ai onze ans. » est faux : Là, tu parles de toi.  
> « Où habites-tu ? » est faux : C’est une question.  
> « Merci beaucoup. » est faux : C’est un remerciement.  

> Quelle phrase sert à présenter quelqu’un d’autre ?

- ◻️ Je m’appelle Ngono.  
  _↳ feedback if chosen: Là, tu te présentes toi-même._
- ✅ Je te présente ma sœur Lisette.
- ◻️ Merci beaucoup.  
  _↳ feedback if chosen: C’est un remerciement._
- ◻️ J’ai onze ans.  
  _↳ feedback if chosen: Là, tu parles de toi._

Full working after a second miss:

> La bonne réponse est « Je te présente ma sœur Lisette. ».  
> « Je m’appelle Ngono. » est faux : Là, tu te présentes toi-même.  
> « Merci beaucoup. » est faux : C’est un remerciement.  
> « J’ai onze ans. » est faux : Là, tu parles de toi.  

Sources: oral (Se présenter et présenter quelqu’un ; politesse (tu / vous))

### `f6-order` · Lesson 6 · word order, level 2

Prompt: Remets les mots dans l’ordre pour faire une phrase.

`s`: Je m’appelle Ngono. · J’ai onze ans. · J’habite à Bafoussam. · Voici mon ami Paul. · Je te présente ma sœur Lisette. · Il s’appelle Eric.

Sentence(s): {s}


Three generated variants:

> Remets les mots dans l’ordre pour faire une phrase.

Tiles: ans · J’ai · onze (then “.”)
Answer: **J’ai onze ans.**

Full working after a second miss:

> La phrase est : J’ai onze ans.  

> Remets les mots dans l’ordre pour faire une phrase.

Tiles: ans · onze · J’ai (then “.”)
Answer: **J’ai onze ans.**

Full working after a second miss:

> La phrase est : J’ai onze ans.  

> Remets les mots dans l’ordre pour faire une phrase.

Tiles: Eric · Il · s’appelle (then “.”)
Answer: **Il s’appelle Eric.**

Full working after a second miss:

> La phrase est : Il s’appelle Eric.  

Sources: oral (Se présenter et présenter quelqu’un ; politesse (tu / vous))

### `f6-spot` · Lesson 6 · spot the error, level 3

Prompt: Une phrase n’est pas correcte. Laquelle ?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Bonjour Monsieur, je m’appelle Ewane.
- ✅ Je te présente mon cousin Joël.
- ✅ Voici ma sœur, elle a dix ans.
- ✅ J’habite à Kribi.
- ❌ Je suis onze ans.  
  _↳ Pour l’âge : J’ai onze ans._
- ❌ Je présente toi mon ami.  
  _↳ On dit : Je te présente mon ami._
- ❌ Moi s’appelle Ngono.  
  _↳ On dit : Je m’appelle Ngono._


Three generated variants:

> Une phrase n’est pas correcte. Laquelle ?

- ◻️ Je te présente mon cousin Joël.
- ◻️ Voici ma sœur, elle a dix ans.
- ◻️ Bonjour Monsieur, je m’appelle Ewane.
- ✅ Moi s’appelle Ngono.  
  _↳ explanation: On dit : Je m’appelle Ngono._

Full working after a second miss:

> La phrase fausse est « Moi s’appelle Ngono. ».  
> On dit : Je m’appelle Ngono.  

> Une phrase n’est pas correcte. Laquelle ?

- ✅ Moi s’appelle Ngono.  
  _↳ explanation: On dit : Je m’appelle Ngono._
- ◻️ Bonjour Monsieur, je m’appelle Ewane.
- ◻️ J’habite à Kribi.
- ◻️ Je te présente mon cousin Joël.

Full working after a second miss:

> La phrase fausse est « Moi s’appelle Ngono. ».  
> On dit : Je m’appelle Ngono.  

> Une phrase n’est pas correcte. Laquelle ?

- ✅ Je présente toi mon ami.  
  _↳ explanation: On dit : Je te présente mon ami._
- ◻️ Je te présente mon cousin Joël.
- ◻️ Bonjour Monsieur, je m’appelle Ewane.
- ◻️ J’habite à Kribi.

Full working after a second miss:

> La phrase fausse est « Je présente toi mon ami. ».  
> On dit : Je te présente mon ami.  

Sources: oral (Se présenter et présenter quelqu’un ; politesse (tu / vous))

### `fc6-3-check` · Lesson 6 · multiple choice, level 1

Prompt: Que dis-tu poliment à la directrice ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Bonjour Madame, je m’appelle Paul.
- ❌ Salut toi, c’est Paul !  
  _↳ À un adulte, on parle poliment : « Bonjour Madame »._
- ❌ Hé ! Moi c’est Paul.  
  _↳ Ce n’est pas poli avec un adulte._
- ❌ Tu vas bien, toi ?  
  _↳ À un adulte, on dit « vous »._
- ❌ Paul. Voilà.  
  _↳ On salue et on fait une phrase complète._


Three generated variants:

> Que dis-tu poliment à la directrice ?

- ✅ Bonjour Madame, je m’appelle Paul.
- ◻️ Salut toi, c’est Paul !  
  _↳ feedback if chosen: À un adulte, on parle poliment : « Bonjour Madame »._
- ◻️ Tu vas bien, toi ?  
  _↳ feedback if chosen: À un adulte, on dit « vous »._
- ◻️ Hé ! Moi c’est Paul.  
  _↳ feedback if chosen: Ce n’est pas poli avec un adulte._

Full working after a second miss:

> La bonne réponse est « Bonjour Madame, je m’appelle Paul. ».  
> « Salut toi, c’est Paul ! » est faux : À un adulte, on parle poliment : « Bonjour Madame ».  
> « Tu vas bien, toi ? » est faux : À un adulte, on dit « vous ».  
> « Hé ! Moi c’est Paul. » est faux : Ce n’est pas poli avec un adulte.  

> Que dis-tu poliment à la directrice ?

- ◻️ Tu vas bien, toi ?  
  _↳ feedback if chosen: À un adulte, on dit « vous »._
- ✅ Bonjour Madame, je m’appelle Paul.
- ◻️ Salut toi, c’est Paul !  
  _↳ feedback if chosen: À un adulte, on parle poliment : « Bonjour Madame »._
- ◻️ Hé ! Moi c’est Paul.  
  _↳ feedback if chosen: Ce n’est pas poli avec un adulte._

Full working after a second miss:

> La bonne réponse est « Bonjour Madame, je m’appelle Paul. ».  
> « Tu vas bien, toi ? » est faux : À un adulte, on dit « vous ».  
> « Salut toi, c’est Paul ! » est faux : À un adulte, on parle poliment : « Bonjour Madame ».  
> « Hé ! Moi c’est Paul. » est faux : Ce n’est pas poli avec un adulte.  

> Que dis-tu poliment à la directrice ?

- ✅ Bonjour Madame, je m’appelle Paul.
- ◻️ Paul. Voilà.  
  _↳ feedback if chosen: On salue et on fait une phrase complète._
- ◻️ Tu vas bien, toi ?  
  _↳ feedback if chosen: À un adulte, on dit « vous »._
- ◻️ Hé ! Moi c’est Paul.  
  _↳ feedback if chosen: Ce n’est pas poli avec un adulte._

Full working after a second miss:

> La bonne réponse est « Bonjour Madame, je m’appelle Paul. ».  
> « Paul. Voilà. » est faux : On salue et on fait une phrase complète.  
> « Tu vas bien, toi ? » est faux : À un adulte, on dit « vous ».  
> « Hé ! Moi c’est Paul. » est faux : Ce n’est pas poli avec un adulte.  

Sources: oral (Se présenter et présenter quelqu’un ; politesse (tu / vous))

### `f7-replace` · Lesson 7 · multiple choice, level 1

Prompt: Quel pronom remplace « {x.t} » ?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Paul | il | « Paul » se remplace par « il ». |
| Lisette | elle | « Lisette » se remplace par « elle ». |
| Paul et Lisette | ils | « Paul et Lisette » se remplace par « ils ». |
| ma mère et ma tante | elles | « ma mère et ma tante » se remplace par « elles ». |
| mon père et ma mère | ils | « mon père et ma mère » se remplace par « ils ». |
| toi et moi | nous | « toi et moi » se remplace par « nous ». |
| toi et ton frère | vous | « toi et ton frère » se remplace par « vous ». |
| le chien | il | « le chien » se remplace par « il ». |
| la voiture | elle | « la voiture » se remplace par « elle ». |
| les enfants | ils | « les enfants » se remplace par « ils ». |
| les filles | elles | « les filles » se remplace par « elles ». |
| Eric et moi | nous | « Eric et moi » se remplace par « nous ». |

Right answer: `{x.a}`; wrong choices: `il`, `elle`, `nous`, `vous`, `ils`, `elles`

- Feedback `other`: “Regarde : masculin ou féminin ? singulier ou pluriel ? Y a-t-il « moi » ou « toi » ?”

Three generated variants:

> Quel pronom remplace « la voiture » ?

- ◻️ vous  
  _↳ feedback if chosen: Regarde : masculin ou féminin ? singulier ou pluriel ? Y a-t-il « moi » ou « toi » ?_
- ◻️ il  
  _↳ feedback if chosen: Regarde : masculin ou féminin ? singulier ou pluriel ? Y a-t-il « moi » ou « toi » ?_
- ✅ elle
- ◻️ ils  
  _↳ feedback if chosen: Regarde : masculin ou féminin ? singulier ou pluriel ? Y a-t-il « moi » ou « toi » ?_

Full working after a second miss:

> « la voiture » se remplace par « elle ».  
> Réponse : elle.  

> Quel pronom remplace « Eric et moi » ?

- ✅ nous
- ◻️ ils  
  _↳ feedback if chosen: Regarde : masculin ou féminin ? singulier ou pluriel ? Y a-t-il « moi » ou « toi » ?_
- ◻️ il  
  _↳ feedback if chosen: Regarde : masculin ou féminin ? singulier ou pluriel ? Y a-t-il « moi » ou « toi » ?_
- ◻️ elle  
  _↳ feedback if chosen: Regarde : masculin ou féminin ? singulier ou pluriel ? Y a-t-il « moi » ou « toi » ?_

Full working after a second miss:

> « Eric et moi » se remplace par « nous ».  
> Réponse : nous.  

> Quel pronom remplace « toi et ton frère » ?

- ◻️ il  
  _↳ feedback if chosen: Regarde : masculin ou féminin ? singulier ou pluriel ? Y a-t-il « moi » ou « toi » ?_
- ✅ vous
- ◻️ elle  
  _↳ feedback if chosen: Regarde : masculin ou féminin ? singulier ou pluriel ? Y a-t-il « moi » ou « toi » ?_
- ◻️ elles  
  _↳ feedback if chosen: Regarde : masculin ou féminin ? singulier ou pluriel ? Y a-t-il « moi » ou « toi » ?_

Full working after a second miss:

> « toi et ton frère » se remplace par « vous ».  
> Réponse : vous.  

Sources: pronoms (Pronoms personnels sujets)

### `f7-sort` · Lesson 7 · matching, level 1

Prompt: Classe les pronoms : singulier ou pluriel ?

Pairs (6 shown each time, sorted into groups):

- je → **singulier**
- tu → **singulier**
- il → **singulier**
- elle → **singulier**
- nous → **pluriel**
- vous → **pluriel**
- ils → **pluriel**
- elles → **pluriel**


Three generated variants:

> Classe les pronoms : singulier ou pluriel ?

Groups: singulier · pluriel
- il → **singulier**
- tu → **singulier**
- elle → **singulier**
- elles → **pluriel**
- nous → **pluriel**
- je → **singulier**

Full working after a second miss:

> Les bonnes paires sont :  
> il → singulier  
> tu → singulier  
> elle → singulier  
> elles → pluriel  
> nous → pluriel  
> je → singulier  

> Classe les pronoms : singulier ou pluriel ?

Groups: singulier · pluriel
- il → **singulier**
- je → **singulier**
- vous → **pluriel**
- nous → **pluriel**
- tu → **singulier**
- ils → **pluriel**

Full working after a second miss:

> Les bonnes paires sont :  
> il → singulier  
> je → singulier  
> vous → pluriel  
> nous → pluriel  
> tu → singulier  
> ils → pluriel  

> Classe les pronoms : singulier ou pluriel ?

Groups: singulier · pluriel
- ils → **pluriel**
- elles → **pluriel**
- je → **singulier**
- vous → **pluriel**
- elle → **singulier**
- nous → **pluriel**

Full working after a second miss:

> Les bonnes paires sont :  
> ils → pluriel  
> elles → pluriel  
> je → singulier  
> vous → pluriel  
> elle → singulier  
> nous → pluriel  

Sources: pronoms (Pronoms personnels sujets)

### `f7-person` · Lesson 7 · matching, level 2

Prompt: Relie chaque pronom à sa personne.

Pairs (4 shown each time):

- je → **1re personne du singulier**
- tu → **2e personne du singulier**
- il → **3e personne du singulier**
- nous → **1re personne du pluriel**
- vous → **2e personne du pluriel**
- ils → **3e personne du pluriel**


Three generated variants:

> Relie chaque pronom à sa personne.

Right-hand side (shuffled): 3e personne du singulier · 1re personne du singulier · 2e personne du pluriel · 2e personne du singulier
- tu → **2e personne du singulier**
- vous → **2e personne du pluriel**
- je → **1re personne du singulier**
- il → **3e personne du singulier**

Full working after a second miss:

> Les bonnes paires sont :  
> tu → 2e personne du singulier  
> vous → 2e personne du pluriel  
> je → 1re personne du singulier  
> il → 3e personne du singulier  

> Relie chaque pronom à sa personne.

Right-hand side (shuffled): 3e personne du pluriel · 2e personne du pluriel · 3e personne du singulier · 1re personne du pluriel
- il → **3e personne du singulier**
- nous → **1re personne du pluriel**
- ils → **3e personne du pluriel**
- vous → **2e personne du pluriel**

Full working after a second miss:

> Les bonnes paires sont :  
> il → 3e personne du singulier  
> nous → 1re personne du pluriel  
> ils → 3e personne du pluriel  
> vous → 2e personne du pluriel  

> Relie chaque pronom à sa personne.

Right-hand side (shuffled): 2e personne du singulier · 1re personne du singulier · 3e personne du singulier · 2e personne du pluriel
- il → **3e personne du singulier**
- je → **1re personne du singulier**
- tu → **2e personne du singulier**
- vous → **2e personne du pluriel**

Full working after a second miss:

> Les bonnes paires sont :  
> il → 3e personne du singulier  
> je → 1re personne du singulier  
> tu → 2e personne du singulier  
> vous → 2e personne du pluriel  

Sources: pronoms (Pronoms personnels sujets)

### `f7-spot` · Lesson 7 · spot the error, level 3

Prompt: Une phrase est fausse. Laquelle ?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ « Paul et Lisette » se remplace par « ils ».
- ✅ « Les filles » se remplace par « elles ».
- ✅ « Toi et moi » se remplace par « nous ».
- ✅ « La voiture » se remplace par « elle ».
- ❌ « Mon père et ma mère » se remplace par « elles ».  
  _↳ Groupe mélangé : ils._
- ❌ « Toi et ton frère » se remplace par « nous ».  
  _↳ Sans « moi » : vous._
- ❌ « Le chien » se remplace par « elle ».  
  _↳ « chien » est masculin : il._


Three generated variants:

> Une phrase est fausse. Laquelle ?

- ◻️ « Toi et moi » se remplace par « nous ».
- ◻️ « Paul et Lisette » se remplace par « ils ».
- ✅ « Mon père et ma mère » se remplace par « elles ».  
  _↳ explanation: Groupe mélangé : ils._
- ◻️ « La voiture » se remplace par « elle ».

Full working after a second miss:

> La phrase fausse est « « Mon père et ma mère » se remplace par « elles ». ».  
> Groupe mélangé : ils.  

> Une phrase est fausse. Laquelle ?

- ✅ « Mon père et ma mère » se remplace par « elles ».  
  _↳ explanation: Groupe mélangé : ils._
- ◻️ « Toi et moi » se remplace par « nous ».
- ◻️ « La voiture » se remplace par « elle ».
- ◻️ « Les filles » se remplace par « elles ».

Full working after a second miss:

> La phrase fausse est « « Mon père et ma mère » se remplace par « elles ». ».  
> Groupe mélangé : ils.  

> Une phrase est fausse. Laquelle ?

- ✅ « Le chien » se remplace par « elle ».  
  _↳ explanation: « chien » est masculin : il._
- ◻️ « Les filles » se remplace par « elles ».
- ◻️ « La voiture » se remplace par « elle ».
- ◻️ « Toi et moi » se remplace par « nous ».

Full working after a second miss:

> La phrase fausse est « « Le chien » se remplace par « elle ». ».  
> « chien » est masculin : il.  

Sources: pronoms (Pronoms personnels sujets)

### `fc7-3-check` · Lesson 7 · multiple choice, level 1

Prompt: Quel pronom remplace « toi et moi » ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ nous
- ❌ vous  
  _↳ « Vous », c’est toi et une autre personne, sans moi._
- ❌ ils  
  _↳ « Ils » ne contient pas « moi »._
- ❌ je  
  _↳ « Je » est une seule personne._
- ❌ elles  
  _↳ « Elles » ne contient pas « moi »._


Three generated variants:

> Quel pronom remplace « toi et moi » ?

- ◻️ vous  
  _↳ feedback if chosen: « Vous », c’est toi et une autre personne, sans moi._
- ◻️ elles  
  _↳ feedback if chosen: « Elles » ne contient pas « moi »._
- ◻️ je  
  _↳ feedback if chosen: « Je » est une seule personne._
- ✅ nous

Full working after a second miss:

> La bonne réponse est « nous ».  
> « vous » est faux : « Vous », c’est toi et une autre personne, sans moi.  
> « elles » est faux : « Elles » ne contient pas « moi ».  
> « je » est faux : « Je » est une seule personne.  

> Quel pronom remplace « toi et moi » ?

- ◻️ je  
  _↳ feedback if chosen: « Je » est une seule personne._
- ◻️ ils  
  _↳ feedback if chosen: « Ils » ne contient pas « moi »._
- ✅ nous
- ◻️ vous  
  _↳ feedback if chosen: « Vous », c’est toi et une autre personne, sans moi._

Full working after a second miss:

> La bonne réponse est « nous ».  
> « je » est faux : « Je » est une seule personne.  
> « ils » est faux : « Ils » ne contient pas « moi ».  
> « vous » est faux : « Vous », c’est toi et une autre personne, sans moi.  

> Quel pronom remplace « toi et moi » ?

- ◻️ ils  
  _↳ feedback if chosen: « Ils » ne contient pas « moi »._
- ◻️ elles  
  _↳ feedback if chosen: « Elles » ne contient pas « moi »._
- ◻️ vous  
  _↳ feedback if chosen: « Vous », c’est toi et une autre personne, sans moi._
- ✅ nous

Full working after a second miss:

> La bonne réponse est « nous ».  
> « ils » est faux : « Ils » ne contient pas « moi ».  
> « elles » est faux : « Elles » ne contient pas « moi ».  
> « vous » est faux : « Vous », c’est toi et une autre personne, sans moi.  

Sources: pronoms (Pronoms personnels sujets)

### `f8-spot` · Lesson 8 · spot the error, level 3

Prompt: Une phrase est fausse. Laquelle ?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Je travaille le samedi.
- ✅ Vous lavez la voiture.
- ✅ Elles travaillent à l’hôpital.
- ✅ Tu laves tes mains.
- ❌ Nous lavont le linge.  
  _↳ Avec nous : nous lavons._
- ❌ Il travaillent bien.  
  _↳ Avec il : il travaille._
- ❌ Tu travaillez dur.  
  _↳ Avec tu : tu travailles._


Three generated variants:

> Une phrase est fausse. Laquelle ?

- ◻️ Elles travaillent à l’hôpital.
- ◻️ Vous lavez la voiture.
- ◻️ Tu laves tes mains.
- ✅ Il travaillent bien.  
  _↳ explanation: Avec il : il travaille._

Full working after a second miss:

> La phrase fausse est « Il travaillent bien. ».  
> Avec il : il travaille.  

> Une phrase est fausse. Laquelle ?

- ◻️ Je travaille le samedi.
- ✅ Tu travaillez dur.  
  _↳ explanation: Avec tu : tu travailles._
- ◻️ Vous lavez la voiture.
- ◻️ Tu laves tes mains.

Full working after a second miss:

> La phrase fausse est « Tu travaillez dur. ».  
> Avec tu : tu travailles.  

> Une phrase est fausse. Laquelle ?

- ◻️ Tu laves tes mains.
- ◻️ Vous lavez la voiture.
- ✅ Nous lavont le linge.  
  _↳ explanation: Avec nous : nous lavons._
- ◻️ Elles travaillent à l’hôpital.

Full working after a second miss:

> La phrase fausse est « Nous lavont le linge. ».  
> Avec nous : nous lavons.  

Sources: conjugaison (Présent de l’indicatif : avoir, s’appeler, verbes en -er (travailler, laver))

### `fc8-3-check` · Lesson 8 · multiple choice, level 1

Prompt: Laquelle est correcte ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Ils travaillent au champ.
- ✅ Tu laves ta chemise.
- ✅ Nous lavons les assiettes.
- ❌ Ils travaille au champ.  
  _↳ Avec ils : -ent._
- ❌ Tu lave ta chemise.  
  _↳ Avec tu : -es._
- ❌ Nous lavez les assiettes.  
  _↳ Avec nous : -ons._
- ❌ Vous travaillons bien.  
  _↳ Avec vous : -ez._


Three generated variants:

> Laquelle est correcte ?

- ◻️ Nous lavez les assiettes.  
  _↳ feedback if chosen: Avec nous : -ons._
- ✅ Ils travaillent au champ.
- ◻️ Vous travaillons bien.  
  _↳ feedback if chosen: Avec vous : -ez._
- ◻️ Tu lave ta chemise.  
  _↳ feedback if chosen: Avec tu : -es._

Full working after a second miss:

> La bonne réponse est « Ils travaillent au champ. ».  
> « Nous lavez les assiettes. » est faux : Avec nous : -ons.  
> « Vous travaillons bien. » est faux : Avec vous : -ez.  
> « Tu lave ta chemise. » est faux : Avec tu : -es.  

> Laquelle est correcte ?

- ◻️ Tu lave ta chemise.  
  _↳ feedback if chosen: Avec tu : -es._
- ◻️ Nous lavez les assiettes.  
  _↳ feedback if chosen: Avec nous : -ons._
- ✅ Tu laves ta chemise.
- ◻️ Vous travaillons bien.  
  _↳ feedback if chosen: Avec vous : -ez._

Full working after a second miss:

> La bonne réponse est « Tu laves ta chemise. ».  
> « Tu lave ta chemise. » est faux : Avec tu : -es.  
> « Nous lavez les assiettes. » est faux : Avec nous : -ons.  
> « Vous travaillons bien. » est faux : Avec vous : -ez.  

> Laquelle est correcte ?

- ✅ Tu laves ta chemise.
- ◻️ Nous lavez les assiettes.  
  _↳ feedback if chosen: Avec nous : -ons._
- ◻️ Vous travaillons bien.  
  _↳ feedback if chosen: Avec vous : -ez._
- ◻️ Ils travaille au champ.  
  _↳ feedback if chosen: Avec ils : -ent._

Full working after a second miss:

> La bonne réponse est « Tu laves ta chemise. ».  
> « Nous lavez les assiettes. » est faux : Avec nous : -ons.  
> « Vous travaillons bien. » est faux : Avec vous : -ez.  
> « Ils travaille au champ. » est faux : Avec ils : -ent.  

Sources: conjugaison (Présent de l’indicatif : avoir, s’appeler, verbes en -er (travailler, laver))

### `f10-who` · Lesson 10 · multiple choice, level 1

Prompt: « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. » / {x.t}

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Qui va au champ ? | le père et les enfants | Qui va au champ ? → le père et les enfants. |
| Qui balaie la cour ? | la mère et le petit frère | Qui balaie la cour ? → la mère et le petit frère. |
| Qui nettoie le marché ? | les voisins | Qui nettoie le marché ? → les voisins. |
| Qui raconte des contes ? | la grand-mère | Qui raconte des contes ? → la grand-mère. |

Right answer: `{x.a}`; wrong choices: `le père et les enfants`, `la mère et le petit frère`, `les voisins`, `la grand-mère`

- Feedback `other`: “Relis la phrase qui parle de cette activité.”

Three generated variants:

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Qui balaie la cour ?

- ✅ la mère et le petit frère
- ◻️ le père et les enfants  
  _↳ feedback if chosen: Relis la phrase qui parle de cette activité._
- ◻️ la grand-mère  
  _↳ feedback if chosen: Relis la phrase qui parle de cette activité._
- ◻️ les voisins  
  _↳ feedback if chosen: Relis la phrase qui parle de cette activité._

Full working after a second miss:

> Qui balaie la cour ? → la mère et le petit frère.  
> Réponse : la mère et le petit frère.  

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Qui raconte des contes ?

- ◻️ le père et les enfants  
  _↳ feedback if chosen: Relis la phrase qui parle de cette activité._
- ◻️ la mère et le petit frère  
  _↳ feedback if chosen: Relis la phrase qui parle de cette activité._
- ✅ la grand-mère
- ◻️ les voisins  
  _↳ feedback if chosen: Relis la phrase qui parle de cette activité._

Full working after a second miss:

> Qui raconte des contes ? → la grand-mère.  
> Réponse : la grand-mère.  

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Qui nettoie le marché ?

- ◻️ le père et les enfants  
  _↳ feedback if chosen: Relis la phrase qui parle de cette activité._
- ◻️ la grand-mère  
  _↳ feedback if chosen: Relis la phrase qui parle de cette activité._
- ◻️ la mère et le petit frère  
  _↳ feedback if chosen: Relis la phrase qui parle de cette activité._
- ✅ les voisins

Full working after a second miss:

> Qui nettoie le marché ? → les voisins.  
> Réponse : les voisins.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f10-when` · Lesson 10 · multiple choice, level 1

Prompt: « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. » / {x.t}

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Quand la famille va-t-elle au champ ? | le samedi matin | Quand la famille va-t-elle au champ ? → le samedi matin. |
| Quand les voisins font-ils l’investissement humain ? | l’après-midi | Quand les voisins font-ils l’investissement humain ? → l’après-midi. |
| Quand la grand-mère raconte-t-elle des contes ? | le soir | Quand la grand-mère raconte-t-elle des contes ? → le soir. |

Right answer: `{x.a}`; wrong choices: `le samedi matin`, `l’après-midi`, `le soir`

- Feedback `other`: “Relis le texte : matin, après-midi ou soir ?”

Three generated variants:

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Quand les voisins font-ils l’investissement humain ?

- ◻️ le samedi matin  
  _↳ feedback if chosen: Relis le texte : matin, après-midi ou soir ?_
- ◻️ le soir  
  _↳ feedback if chosen: Relis le texte : matin, après-midi ou soir ?_
- ✅ l’après-midi

Full working after a second miss:

> Quand les voisins font-ils l’investissement humain ? → l’après-midi.  
> Réponse : l’après-midi.  

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Quand les voisins font-ils l’investissement humain ?

- ◻️ le samedi matin  
  _↳ feedback if chosen: Relis le texte : matin, après-midi ou soir ?_
- ◻️ le soir  
  _↳ feedback if chosen: Relis le texte : matin, après-midi ou soir ?_
- ✅ l’après-midi

Full working after a second miss:

> Quand les voisins font-ils l’investissement humain ? → l’après-midi.  
> Réponse : l’après-midi.  

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Quand la grand-mère raconte-t-elle des contes ?

- ◻️ l’après-midi  
  _↳ feedback if chosen: Relis le texte : matin, après-midi ou soir ?_
- ◻️ le samedi matin  
  _↳ feedback if chosen: Relis le texte : matin, après-midi ou soir ?_
- ✅ le soir

Full working after a second miss:

> Quand la grand-mère raconte-t-elle des contes ? → le soir.  
> Réponse : le soir.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f10-true` · Lesson 10 · multiple choice, level 2

Prompt: « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. » / Quelle phrase est vraie d’après le texte ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ La famille se lève tôt le samedi.
- ✅ Les voisins curent les caniveaux.
- ✅ Le soir, tout le monde est content.
- ❌ La famille dort jusqu’à midi.  
  _↳ Le texte dit qu’elle se lève tôt._
- ❌ La mère va au champ.  
  _↳ La mère balaie la cour et lave le linge._
- ❌ Les voisins vont à la plage.  
  _↳ Ils nettoient le marché et les caniveaux._
- ❌ La grand-mère désherbe le maïs.  
  _↳ Elle raconte des contes le soir._


Three generated variants:

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Quelle phrase est vraie d’après le texte ?

- ◻️ La famille dort jusqu’à midi.  
  _↳ feedback if chosen: Le texte dit qu’elle se lève tôt._
- ◻️ La mère va au champ.  
  _↳ feedback if chosen: La mère balaie la cour et lave le linge._
- ◻️ La grand-mère désherbe le maïs.  
  _↳ feedback if chosen: Elle raconte des contes le soir._
- ✅ La famille se lève tôt le samedi.

Full working after a second miss:

> La bonne réponse est « La famille se lève tôt le samedi. ».  
> « La famille dort jusqu’à midi. » est faux : Le texte dit qu’elle se lève tôt.  
> « La mère va au champ. » est faux : La mère balaie la cour et lave le linge.  
> « La grand-mère désherbe le maïs. » est faux : Elle raconte des contes le soir.  

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Quelle phrase est vraie d’après le texte ?

- ◻️ La famille dort jusqu’à midi.  
  _↳ feedback if chosen: Le texte dit qu’elle se lève tôt._
- ◻️ La grand-mère désherbe le maïs.  
  _↳ feedback if chosen: Elle raconte des contes le soir._
- ✅ Le soir, tout le monde est content.
- ◻️ La mère va au champ.  
  _↳ feedback if chosen: La mère balaie la cour et lave le linge._

Full working after a second miss:

> La bonne réponse est « Le soir, tout le monde est content. ».  
> « La famille dort jusqu’à midi. » est faux : Le texte dit qu’elle se lève tôt.  
> « La grand-mère désherbe le maïs. » est faux : Elle raconte des contes le soir.  
> « La mère va au champ. » est faux : La mère balaie la cour et lave le linge.  

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Quelle phrase est vraie d’après le texte ?

- ✅ Le soir, tout le monde est content.
- ◻️ Les voisins vont à la plage.  
  _↳ feedback if chosen: Ils nettoient le marché et les caniveaux._
- ◻️ La mère va au champ.  
  _↳ feedback if chosen: La mère balaie la cour et lave le linge._
- ◻️ La grand-mère désherbe le maïs.  
  _↳ feedback if chosen: Elle raconte des contes le soir._

Full working after a second miss:

> La bonne réponse est « Le soir, tout le monde est content. ».  
> « Les voisins vont à la plage. » est faux : Ils nettoient le marché et les caniveaux.  
> « La mère va au champ. » est faux : La mère balaie la cour et lave le linge.  
> « La grand-mère désherbe le maïs. » est faux : Elle raconte des contes le soir.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f10-word` · Lesson 10 · multiple choice, level 3

Prompt: « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. » / Dans le texte, que veut dire « désherber » ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ enlever les mauvaises herbes
- ❌ planter du maïs  
  _↳ Planter, c’est mettre les graines en terre._
- ❌ arroser le champ  
  _↳ Arroser, c’est donner de l’eau._
- ❌ récolter le maïs  
  _↳ Récolter, c’est ramasser ce qui a poussé._
- ❌ brûler la brousse  
  _↳ Désherber, c’est enlever les mauvaises herbes._


Three generated variants:

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Dans le texte, que veut dire « désherber » ?

- ◻️ récolter le maïs  
  _↳ feedback if chosen: Récolter, c’est ramasser ce qui a poussé._
- ◻️ arroser le champ  
  _↳ feedback if chosen: Arroser, c’est donner de l’eau._
- ✅ enlever les mauvaises herbes
- ◻️ brûler la brousse  
  _↳ feedback if chosen: Désherber, c’est enlever les mauvaises herbes._

Full working after a second miss:

> La bonne réponse est « enlever les mauvaises herbes ».  
> « récolter le maïs » est faux : Récolter, c’est ramasser ce qui a poussé.  
> « arroser le champ » est faux : Arroser, c’est donner de l’eau.  
> « brûler la brousse » est faux : Désherber, c’est enlever les mauvaises herbes.  

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Dans le texte, que veut dire « désherber » ?

- ✅ enlever les mauvaises herbes
- ◻️ planter du maïs  
  _↳ feedback if chosen: Planter, c’est mettre les graines en terre._
- ◻️ arroser le champ  
  _↳ feedback if chosen: Arroser, c’est donner de l’eau._
- ◻️ brûler la brousse  
  _↳ feedback if chosen: Désherber, c’est enlever les mauvaises herbes._

Full working after a second miss:

> La bonne réponse est « enlever les mauvaises herbes ».  
> « planter du maïs » est faux : Planter, c’est mettre les graines en terre.  
> « arroser le champ » est faux : Arroser, c’est donner de l’eau.  
> « brûler la brousse » est faux : Désherber, c’est enlever les mauvaises herbes.  

> « Le samedi matin, toute la famille de Mbarga se lève tôt. Le père et les enfants vont au champ pour désherber le maïs. La mère et le petit frère balaient la cour et lavent le linge. L’après-midi, les voisins se réunissent pour l’investissement humain : ils nettoient le marché et curent les caniveaux du quartier. Le soir, tout le monde est fatigué mais content. La grand-mère raconte des contes aux enfants autour du feu. »
> Dans le texte, que veut dire « désherber » ?

- ◻️ brûler la brousse  
  _↳ feedback if chosen: Désherber, c’est enlever les mauvaises herbes._
- ◻️ arroser le champ  
  _↳ feedback if chosen: Arroser, c’est donner de l’eau._
- ◻️ récolter le maïs  
  _↳ feedback if chosen: Récolter, c’est ramasser ce qui a poussé._
- ✅ enlever les mauvaises herbes

Full working after a second miss:

> La bonne réponse est « enlever les mauvaises herbes ».  
> « brûler la brousse » est faux : Désherber, c’est enlever les mauvaises herbes.  
> « arroser le champ » est faux : Arroser, c’est donner de l’eau.  
> « récolter le maïs » est faux : Récolter, c’est ramasser ce qui a poussé.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `fc10-3-check` · Lesson 10 · multiple choice, level 1

Prompt: Que veut dire « investissement humain » ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ un travail fait ensemble pour le bien du quartier
- ❌ mettre de l’argent à la banque  
  _↳ Ici, c’est un travail fait ensemble, sans salaire._
- ❌ une fête au village  
  _↳ C’est un travail pour le quartier._
- ❌ un match de football  
  _↳ C’est un travail pour le quartier._
- ❌ un cours à l’école  
  _↳ C’est un travail pour le quartier._


Three generated variants:

> Que veut dire « investissement humain » ?

- ◻️ une fête au village  
  _↳ feedback if chosen: C’est un travail pour le quartier._
- ✅ un travail fait ensemble pour le bien du quartier
- ◻️ mettre de l’argent à la banque  
  _↳ feedback if chosen: Ici, c’est un travail fait ensemble, sans salaire._
- ◻️ un cours à l’école  
  _↳ feedback if chosen: C’est un travail pour le quartier._

Full working after a second miss:

> La bonne réponse est « un travail fait ensemble pour le bien du quartier ».  
> « une fête au village » est faux : C’est un travail pour le quartier.  
> « mettre de l’argent à la banque » est faux : Ici, c’est un travail fait ensemble, sans salaire.  
> « un cours à l’école » est faux : C’est un travail pour le quartier.  

> Que veut dire « investissement humain » ?

- ◻️ un cours à l’école  
  _↳ feedback if chosen: C’est un travail pour le quartier._
- ◻️ un match de football  
  _↳ feedback if chosen: C’est un travail pour le quartier._
- ✅ un travail fait ensemble pour le bien du quartier
- ◻️ mettre de l’argent à la banque  
  _↳ feedback if chosen: Ici, c’est un travail fait ensemble, sans salaire._

Full working after a second miss:

> La bonne réponse est « un travail fait ensemble pour le bien du quartier ».  
> « un cours à l’école » est faux : C’est un travail pour le quartier.  
> « un match de football » est faux : C’est un travail pour le quartier.  
> « mettre de l’argent à la banque » est faux : Ici, c’est un travail fait ensemble, sans salaire.  

> Que veut dire « investissement humain » ?

- ✅ un travail fait ensemble pour le bien du quartier
- ◻️ mettre de l’argent à la banque  
  _↳ feedback if chosen: Ici, c’est un travail fait ensemble, sans salaire._
- ◻️ un cours à l’école  
  _↳ feedback if chosen: C’est un travail pour le quartier._
- ◻️ une fête au village  
  _↳ feedback if chosen: C’est un travail pour le quartier._

Full working after a second miss:

> La bonne réponse est « un travail fait ensemble pour le bien du quartier ».  
> « mettre de l’argent à la banque » est faux : Ici, c’est un travail fait ensemble, sans salaire.  
> « un cours à l’école » est faux : C’est un travail pour le quartier.  
> « une fête au village » est faux : C’est un travail pour le quartier.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f11-what` · Lesson 11 · multiple choice, level 1

Prompt: « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. » / {x.t}

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Où va un élève malade ? | à l’infirmerie | Où va un élève malade ? → à l’infirmerie. |
| Où se rassemblent les élèves le lundi matin ? | dans la cour | Où se rassemblent les élèves le lundi matin ? → dans la cour. |
| Où se trouve le lycée ? | à l’entrée de la ville | Où se trouve le lycée ? → à l’entrée de la ville. |

Right answer: `{x.a}`; wrong choices: `à l’infirmerie`, `dans la cour`, `à l’entrée de la ville`, `au marché`

- Feedback `other`: “Relis la phrase qui parle de ce lieu.”

Three generated variants:

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Où se rassemblent les élèves le lundi matin ?

- ◻️ au marché  
  _↳ feedback if chosen: Relis la phrase qui parle de ce lieu._
- ◻️ à l’entrée de la ville  
  _↳ feedback if chosen: Relis la phrase qui parle de ce lieu._
- ◻️ à l’infirmerie  
  _↳ feedback if chosen: Relis la phrase qui parle de ce lieu._
- ✅ dans la cour

Full working after a second miss:

> Où se rassemblent les élèves le lundi matin ? → dans la cour.  
> Réponse : dans la cour.  

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Où se trouve le lycée ?

- ◻️ dans la cour  
  _↳ feedback if chosen: Relis la phrase qui parle de ce lieu._
- ◻️ à l’infirmerie  
  _↳ feedback if chosen: Relis la phrase qui parle de ce lieu._
- ◻️ au marché  
  _↳ feedback if chosen: Relis la phrase qui parle de ce lieu._
- ✅ à l’entrée de la ville

Full working after a second miss:

> Où se trouve le lycée ? → à l’entrée de la ville.  
> Réponse : à l’entrée de la ville.  

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Où se rassemblent les élèves le lundi matin ?

- ✅ dans la cour
- ◻️ à l’infirmerie  
  _↳ feedback if chosen: Relis la phrase qui parle de ce lieu._
- ◻️ au marché  
  _↳ feedback if chosen: Relis la phrase qui parle de ce lieu._
- ◻️ à l’entrée de la ville  
  _↳ feedback if chosen: Relis la phrase qui parle de ce lieu._

Full working after a second miss:

> Où se rassemblent les élèves le lundi matin ? → dans la cour.  
> Réponse : dans la cour.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f11-true` · Lesson 11 · multiple choice, level 1

Prompt: « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. » / Quelle phrase est vraie d’après le texte ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Le lever des couleurs a lieu le lundi matin.
- ✅ Ngono étudie l’anglais.
- ✅ À la récréation, des élèves jouent au football.
- ❌ Le lever des couleurs a lieu le vendredi soir.  
  _↳ Le texte dit « chaque lundi matin »._
- ❌ Ngono n’étudie pas les mathématiques.  
  _↳ Les mathématiques sont dans la liste._
- ❌ Les élèves malades rentrent à la maison seuls.  
  _↳ Ils vont à l’infirmerie._
- ❌ Le lycée est au milieu de la forêt.  
  _↳ Il est à l’entrée de la ville._


Three generated variants:

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Quelle phrase est vraie d’après le texte ?

- ◻️ Le lever des couleurs a lieu le vendredi soir.  
  _↳ feedback if chosen: Le texte dit « chaque lundi matin »._
- ◻️ Les élèves malades rentrent à la maison seuls.  
  _↳ feedback if chosen: Ils vont à l’infirmerie._
- ✅ À la récréation, des élèves jouent au football.
- ◻️ Ngono n’étudie pas les mathématiques.  
  _↳ feedback if chosen: Les mathématiques sont dans la liste._

Full working after a second miss:

> La bonne réponse est « À la récréation, des élèves jouent au football. ».  
> « Le lever des couleurs a lieu le vendredi soir. » est faux : Le texte dit « chaque lundi matin ».  
> « Les élèves malades rentrent à la maison seuls. » est faux : Ils vont à l’infirmerie.  
> « Ngono n’étudie pas les mathématiques. » est faux : Les mathématiques sont dans la liste.  

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Quelle phrase est vraie d’après le texte ?

- ◻️ Le lycée est au milieu de la forêt.  
  _↳ feedback if chosen: Il est à l’entrée de la ville._
- ✅ À la récréation, des élèves jouent au football.
- ◻️ Les élèves malades rentrent à la maison seuls.  
  _↳ feedback if chosen: Ils vont à l’infirmerie._
- ◻️ Le lever des couleurs a lieu le vendredi soir.  
  _↳ feedback if chosen: Le texte dit « chaque lundi matin »._

Full working after a second miss:

> La bonne réponse est « À la récréation, des élèves jouent au football. ».  
> « Le lycée est au milieu de la forêt. » est faux : Il est à l’entrée de la ville.  
> « Les élèves malades rentrent à la maison seuls. » est faux : Ils vont à l’infirmerie.  
> « Le lever des couleurs a lieu le vendredi soir. » est faux : Le texte dit « chaque lundi matin ».  

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Quelle phrase est vraie d’après le texte ?

- ◻️ Le lever des couleurs a lieu le vendredi soir.  
  _↳ feedback if chosen: Le texte dit « chaque lundi matin »._
- ◻️ Le lycée est au milieu de la forêt.  
  _↳ feedback if chosen: Il est à l’entrée de la ville._
- ◻️ Ngono n’étudie pas les mathématiques.  
  _↳ feedback if chosen: Les mathématiques sont dans la liste._
- ✅ À la récréation, des élèves jouent au football.

Full working after a second miss:

> La bonne réponse est « À la récréation, des élèves jouent au football. ».  
> « Le lever des couleurs a lieu le vendredi soir. » est faux : Le texte dit « chaque lundi matin ».  
> « Le lycée est au milieu de la forêt. » est faux : Il est à l’entrée de la ville.  
> « Ngono n’étudie pas les mathématiques. » est faux : Les mathématiques sont dans la liste.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f11-subject` · Lesson 11 · multiple choice, level 2

Prompt: « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. » / Quelle matière n’est pas dans la liste du texte ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ l’informatique
- ❌ le français  
  _↳ Le français est dans la liste._
- ❌ l’histoire  
  _↳ L’histoire est dans la liste._
- ❌ la géographie  
  _↳ La géographie est dans la liste._
- ❌ l’anglais  
  _↳ L’anglais est dans la liste._


Three generated variants:

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Quelle matière n’est pas dans la liste du texte ?

- ◻️ l’anglais  
  _↳ feedback if chosen: L’anglais est dans la liste._
- ◻️ l’histoire  
  _↳ feedback if chosen: L’histoire est dans la liste._
- ◻️ le français  
  _↳ feedback if chosen: Le français est dans la liste._
- ✅ l’informatique

Full working after a second miss:

> La bonne réponse est « l’informatique ».  
> « l’anglais » est faux : L’anglais est dans la liste.  
> « l’histoire » est faux : L’histoire est dans la liste.  
> « le français » est faux : Le français est dans la liste.  

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Quelle matière n’est pas dans la liste du texte ?

- ◻️ le français  
  _↳ feedback if chosen: Le français est dans la liste._
- ✅ l’informatique
- ◻️ l’anglais  
  _↳ feedback if chosen: L’anglais est dans la liste._
- ◻️ l’histoire  
  _↳ feedback if chosen: L’histoire est dans la liste._

Full working after a second miss:

> La bonne réponse est « l’informatique ».  
> « le français » est faux : Le français est dans la liste.  
> « l’anglais » est faux : L’anglais est dans la liste.  
> « l’histoire » est faux : L’histoire est dans la liste.  

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Quelle matière n’est pas dans la liste du texte ?

- ◻️ le français  
  _↳ feedback if chosen: Le français est dans la liste._
- ✅ l’informatique
- ◻️ la géographie  
  _↳ feedback if chosen: La géographie est dans la liste._
- ◻️ l’histoire  
  _↳ feedback if chosen: L’histoire est dans la liste._

Full working after a second miss:

> La bonne réponse est « l’informatique ».  
> « le français » est faux : Le français est dans la liste.  
> « la géographie » est faux : La géographie est dans la liste.  
> « l’histoire » est faux : L’histoire est dans la liste.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f11-word` · Lesson 11 · multiple choice, level 3

Prompt: « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. » / Dans le texte, que veut dire « veillent sur » ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ surveillent, font attention à
- ❌ dorment  
  _↳ Veiller sur quelqu’un, c’est le surveiller._
- ❌ oublient  
  _↳ C’est le contraire._
- ❌ vendent  
  _↳ Ce n’est pas le sens._
- ❌ chantent  
  _↳ Ce n’est pas le sens._


Three generated variants:

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Dans le texte, que veut dire « veillent sur » ?

- ✅ surveillent, font attention à
- ◻️ chantent  
  _↳ feedback if chosen: Ce n’est pas le sens._
- ◻️ oublient  
  _↳ feedback if chosen: C’est le contraire._
- ◻️ dorment  
  _↳ feedback if chosen: Veiller sur quelqu’un, c’est le surveiller._

Full working after a second miss:

> La bonne réponse est « surveillent, font attention à ».  
> « chantent » est faux : Ce n’est pas le sens.  
> « oublient » est faux : C’est le contraire.  
> « dorment » est faux : Veiller sur quelqu’un, c’est le surveiller.  

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Dans le texte, que veut dire « veillent sur » ?

- ◻️ oublient  
  _↳ feedback if chosen: C’est le contraire._
- ◻️ vendent  
  _↳ feedback if chosen: Ce n’est pas le sens._
- ✅ surveillent, font attention à
- ◻️ chantent  
  _↳ feedback if chosen: Ce n’est pas le sens._

Full working after a second miss:

> La bonne réponse est « surveillent, font attention à ».  
> « oublient » est faux : C’est le contraire.  
> « vendent » est faux : Ce n’est pas le sens.  
> « chantent » est faux : Ce n’est pas le sens.  

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Dans le texte, que veut dire « veillent sur » ?

- ◻️ chantent  
  _↳ feedback if chosen: Ce n’est pas le sens._
- ◻️ oublient  
  _↳ feedback if chosen: C’est le contraire._
- ◻️ dorment  
  _↳ feedback if chosen: Veiller sur quelqu’un, c’est le surveiller._
- ✅ surveillent, font attention à

Full working after a second miss:

> La bonne réponse est « surveillent, font attention à ».  
> « chantent » est faux : Ce n’est pas le sens.  
> « oublient » est faux : C’est le contraire.  
> « dorment » est faux : Veiller sur quelqu’un, c’est le surveiller.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `fc11-3-check` · Lesson 11 · multiple choice, level 1

Prompt: « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. » / Qui veille sur la discipline ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ le proviseur, le censeur et les surveillants
- ❌ les élèves seulement  
  _↳ Le texte nomme le proviseur, le censeur et les surveillants._
- ❌ les vendeuses de beignets  
  _↳ Elles vendent des beignets._
- ❌ l’infirmière  
  _↳ Elle soigne les malades._
- ❌ les parents  
  _↳ Le texte nomme le proviseur, le censeur et les surveillants._


Three generated variants:

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Qui veille sur la discipline ?

- ◻️ les élèves seulement  
  _↳ feedback if chosen: Le texte nomme le proviseur, le censeur et les surveillants._
- ◻️ les vendeuses de beignets  
  _↳ feedback if chosen: Elles vendent des beignets._
- ◻️ les parents  
  _↳ feedback if chosen: Le texte nomme le proviseur, le censeur et les surveillants._
- ✅ le proviseur, le censeur et les surveillants

Full working after a second miss:

> La bonne réponse est « le proviseur, le censeur et les surveillants ».  
> « les élèves seulement » est faux : Le texte nomme le proviseur, le censeur et les surveillants.  
> « les vendeuses de beignets » est faux : Elles vendent des beignets.  
> « les parents » est faux : Le texte nomme le proviseur, le censeur et les surveillants.  

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Qui veille sur la discipline ?

- ✅ le proviseur, le censeur et les surveillants
- ◻️ les élèves seulement  
  _↳ feedback if chosen: Le texte nomme le proviseur, le censeur et les surveillants._
- ◻️ les parents  
  _↳ feedback if chosen: Le texte nomme le proviseur, le censeur et les surveillants._
- ◻️ les vendeuses de beignets  
  _↳ feedback if chosen: Elles vendent des beignets._

Full working after a second miss:

> La bonne réponse est « le proviseur, le censeur et les surveillants ».  
> « les élèves seulement » est faux : Le texte nomme le proviseur, le censeur et les surveillants.  
> « les parents » est faux : Le texte nomme le proviseur, le censeur et les surveillants.  
> « les vendeuses de beignets » est faux : Elles vendent des beignets.  

> « Le lycée de Ngono se trouve à l’entrée de la ville. Chaque lundi matin, les élèves se rassemblent dans la cour pour le lever des couleurs. Ensuite, ils entrent en classe. En Form One, Ngono étudie le français, l’anglais, les mathématiques, l’histoire, la géographie et les sciences. À la récréation, les élèves jouent au football ou achètent des beignets. Quand un élève est malade, il va à l’infirmerie. Le proviseur, le censeur et les surveillants veillent sur le travail et la discipline. »
> Qui veille sur la discipline ?

- ✅ le proviseur, le censeur et les surveillants
- ◻️ les parents  
  _↳ feedback if chosen: Le texte nomme le proviseur, le censeur et les surveillants._
- ◻️ les élèves seulement  
  _↳ feedback if chosen: Le texte nomme le proviseur, le censeur et les surveillants._
- ◻️ les vendeuses de beignets  
  _↳ feedback if chosen: Elles vendent des beignets._

Full working after a second miss:

> La bonne réponse est « le proviseur, le censeur et les surveillants ».  
> « les parents » est faux : Le texte nomme le proviseur, le censeur et les surveillants.  
> « les élèves seulement » est faux : Le texte nomme le proviseur, le censeur et les surveillants.  
> « les vendeuses de beignets » est faux : Elles vendent des beignets.  

Sources: lecture (Textes de lecture originaux écrits pour l’application (famille, activités, école))

### `f12-place` · Lesson 12 · matching, level 1

Prompt: Relie chaque lieu à sa définition.

Pairs (4 shown each time):

- le provisorat → **le bureau du proviseur**
- l’infirmerie → **la salle où l’on soigne les malades**
- la bibliothèque → **la salle où l’on lit et emprunte des livres**
- le laboratoire → **la salle des expériences de sciences**
- la cour → **l’espace de la récréation et du lever des couleurs**
- la salle de classe → **la salle où ont lieu les cours**
- le terrain de sport → **l’endroit où l’on fait du sport**


Three generated variants:

> Relie chaque lieu à sa définition.

Right-hand side (shuffled): le bureau du proviseur · la salle où l’on soigne les malades · la salle où l’on lit et emprunte des livres · la salle où ont lieu les cours
- l’infirmerie → **la salle où l’on soigne les malades**
- la bibliothèque → **la salle où l’on lit et emprunte des livres**
- la salle de classe → **la salle où ont lieu les cours**
- le provisorat → **le bureau du proviseur**

Full working after a second miss:

> Les bonnes paires sont :  
> l’infirmerie → la salle où l’on soigne les malades  
> la bibliothèque → la salle où l’on lit et emprunte des livres  
> la salle de classe → la salle où ont lieu les cours  
> le provisorat → le bureau du proviseur  

> Relie chaque lieu à sa définition.

Right-hand side (shuffled): la salle des expériences de sciences · l’espace de la récréation et du lever des couleurs · la salle où ont lieu les cours · la salle où l’on lit et emprunte des livres
- la bibliothèque → **la salle où l’on lit et emprunte des livres**
- le laboratoire → **la salle des expériences de sciences**
- la cour → **l’espace de la récréation et du lever des couleurs**
- la salle de classe → **la salle où ont lieu les cours**

Full working after a second miss:

> Les bonnes paires sont :  
> la bibliothèque → la salle où l’on lit et emprunte des livres  
> le laboratoire → la salle des expériences de sciences  
> la cour → l’espace de la récréation et du lever des couleurs  
> la salle de classe → la salle où ont lieu les cours  

> Relie chaque lieu à sa définition.

Right-hand side (shuffled): la salle où l’on soigne les malades · la salle des expériences de sciences · la salle où ont lieu les cours · la salle où l’on lit et emprunte des livres
- le laboratoire → **la salle des expériences de sciences**
- la salle de classe → **la salle où ont lieu les cours**
- la bibliothèque → **la salle où l’on lit et emprunte des livres**
- l’infirmerie → **la salle où l’on soigne les malades**

Full working after a second miss:

> Les bonnes paires sont :  
> le laboratoire → la salle des expériences de sciences  
> la salle de classe → la salle où ont lieu les cours  
> la bibliothèque → la salle où l’on lit et emprunte des livres  
> l’infirmerie → la salle où l’on soigne les malades  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `f12-staff` · Lesson 12 · matching, level 1

Prompt: Relie chaque personne à son rôle.

Pairs (4 shown each time):

- le proviseur → **dirige le lycée**
- le censeur → **organise les cours et les études**
- le surveillant général → **s’occupe de la discipline**
- l’intendant → **s’occupe de l’argent et du matériel**
- le professeur → **enseigne une matière**
- l’infirmière → **soigne les élèves malades**


Three generated variants:

> Relie chaque personne à son rôle.

Right-hand side (shuffled): s’occupe de la discipline · soigne les élèves malades · dirige le lycée · organise les cours et les études
- l’infirmière → **soigne les élèves malades**
- le surveillant général → **s’occupe de la discipline**
- le proviseur → **dirige le lycée**
- le censeur → **organise les cours et les études**

Full working after a second miss:

> Les bonnes paires sont :  
> l’infirmière → soigne les élèves malades  
> le surveillant général → s’occupe de la discipline  
> le proviseur → dirige le lycée  
> le censeur → organise les cours et les études  

> Relie chaque personne à son rôle.

Right-hand side (shuffled): s’occupe de l’argent et du matériel · enseigne une matière · dirige le lycée · soigne les élèves malades
- le professeur → **enseigne une matière**
- l’infirmière → **soigne les élèves malades**
- l’intendant → **s’occupe de l’argent et du matériel**
- le proviseur → **dirige le lycée**

Full working after a second miss:

> Les bonnes paires sont :  
> le professeur → enseigne une matière  
> l’infirmière → soigne les élèves malades  
> l’intendant → s’occupe de l’argent et du matériel  
> le proviseur → dirige le lycée  

> Relie chaque personne à son rôle.

Right-hand side (shuffled): soigne les élèves malades · enseigne une matière · dirige le lycée · organise les cours et les études
- le proviseur → **dirige le lycée**
- le censeur → **organise les cours et les études**
- le professeur → **enseigne une matière**
- l’infirmière → **soigne les élèves malades**

Full working after a second miss:

> Les bonnes paires sont :  
> le proviseur → dirige le lycée  
> le censeur → organise les cours et les études  
> le professeur → enseigne une matière  
> l’infirmière → soigne les élèves malades  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `f12-sort` · Lesson 12 · matching, level 2

Prompt: Classe les mots : lieu, personne ou matière ?

Pairs (6 shown each time, sorted into groups):

- l’infirmerie → **lieu**
- la bibliothèque → **lieu**
- le laboratoire → **lieu**
- le proviseur → **personne**
- le censeur → **personne**
- l’intendant → **personne**
- la géographie → **matière**
- la chimie → **matière**
- l’anglais → **matière**


Three generated variants:

> Classe les mots : lieu, personne ou matière ?

Groups: lieu · personne · matière
- le laboratoire → **lieu**
- l’infirmerie → **lieu**
- l’anglais → **matière**
- la géographie → **matière**
- la bibliothèque → **lieu**
- le proviseur → **personne**

Full working after a second miss:

> Les bonnes paires sont :  
> le laboratoire → lieu  
> l’infirmerie → lieu  
> l’anglais → matière  
> la géographie → matière  
> la bibliothèque → lieu  
> le proviseur → personne  

> Classe les mots : lieu, personne ou matière ?

Groups: lieu · personne · matière
- le proviseur → **personne**
- l’anglais → **matière**
- l’infirmerie → **lieu**
- l’intendant → **personne**
- la géographie → **matière**
- la bibliothèque → **lieu**

Full working after a second miss:

> Les bonnes paires sont :  
> le proviseur → personne  
> l’anglais → matière  
> l’infirmerie → lieu  
> l’intendant → personne  
> la géographie → matière  
> la bibliothèque → lieu  

> Classe les mots : lieu, personne ou matière ?

Groups: lieu · personne · matière
- le laboratoire → **lieu**
- le proviseur → **personne**
- l’infirmerie → **lieu**
- le censeur → **personne**
- la chimie → **matière**
- l’intendant → **personne**

Full working after a second miss:

> Les bonnes paires sont :  
> le laboratoire → lieu  
> le proviseur → personne  
> l’infirmerie → lieu  
> le censeur → personne  
> la chimie → matière  
> l’intendant → personne  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `f12-spot` · Lesson 12 · spot the error, level 3

Prompt: Une phrase est fausse. Laquelle ?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Le proviseur dirige le lycée.
- ✅ On soigne les élèves malades à l’infirmerie.
- ✅ La chimie est une matière.
- ✅ On emprunte des livres à la bibliothèque.
- ❌ L’intendant enseigne les mathématiques.  
  _↳ L’intendant s’occupe de l’argent et du matériel._
- ❌ Le laboratoire est la salle du proviseur.  
  _↳ Le bureau du proviseur est le provisorat._
- ❌ La récréation est une matière.  
  _↳ La récréation est une pause._


Three generated variants:

> Une phrase est fausse. Laquelle ?

- ✅ La récréation est une matière.  
  _↳ explanation: La récréation est une pause._
- ◻️ La chimie est une matière.
- ◻️ On soigne les élèves malades à l’infirmerie.
- ◻️ Le proviseur dirige le lycée.

Full working after a second miss:

> La phrase fausse est « La récréation est une matière. ».  
> La récréation est une pause.  

> Une phrase est fausse. Laquelle ?

- ◻️ On emprunte des livres à la bibliothèque.
- ◻️ On soigne les élèves malades à l’infirmerie.
- ◻️ La chimie est une matière.
- ✅ La récréation est une matière.  
  _↳ explanation: La récréation est une pause._

Full working after a second miss:

> La phrase fausse est « La récréation est une matière. ».  
> La récréation est une pause.  

> Une phrase est fausse. Laquelle ?

- ◻️ On soigne les élèves malades à l’infirmerie.
- ◻️ On emprunte des livres à la bibliothèque.
- ◻️ Le proviseur dirige le lycée.
- ✅ L’intendant enseigne les mathématiques.  
  _↳ explanation: L’intendant s’occupe de l’argent et du matériel._

Full working after a second miss:

> La phrase fausse est « L’intendant enseigne les mathématiques. ».  
> L’intendant s’occupe de l’argent et du matériel.  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `fc12-3-check` · Lesson 12 · multiple choice, level 1

Prompt: Lequel est une matière scolaire ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ la géographie
- ✅ la chimie
- ✅ l’anglais
- ✅ l’histoire
- ❌ la récréation  
  _↳ C’est une pause, pas une matière._
- ❌ l’infirmerie  
  _↳ C’est un lieu._
- ❌ le censeur  
  _↳ C’est une personne._
- ❌ la cour  
  _↳ C’est un lieu._


Three generated variants:

> Lequel est une matière scolaire ?

- ◻️ l’infirmerie  
  _↳ feedback if chosen: C’est un lieu._
- ◻️ la cour  
  _↳ feedback if chosen: C’est un lieu._
- ◻️ la récréation  
  _↳ feedback if chosen: C’est une pause, pas une matière._
- ✅ la géographie

Full working after a second miss:

> La bonne réponse est « la géographie ».  
> « l’infirmerie » est faux : C’est un lieu.  
> « la cour » est faux : C’est un lieu.  
> « la récréation » est faux : C’est une pause, pas une matière.  

> Lequel est une matière scolaire ?

- ◻️ la cour  
  _↳ feedback if chosen: C’est un lieu._
- ◻️ le censeur  
  _↳ feedback if chosen: C’est une personne._
- ◻️ la récréation  
  _↳ feedback if chosen: C’est une pause, pas une matière._
- ✅ l’anglais

Full working after a second miss:

> La bonne réponse est « l’anglais ».  
> « la cour » est faux : C’est un lieu.  
> « le censeur » est faux : C’est une personne.  
> « la récréation » est faux : C’est une pause, pas une matière.  

> Lequel est une matière scolaire ?

- ◻️ l’infirmerie  
  _↳ feedback if chosen: C’est un lieu._
- ✅ la géographie
- ◻️ la cour  
  _↳ feedback if chosen: C’est un lieu._
- ◻️ la récréation  
  _↳ feedback if chosen: C’est une pause, pas une matière._

Full working after a second miss:

> La bonne réponse est « la géographie ».  
> « l’infirmerie » est faux : C’est un lieu.  
> « la cour » est faux : C’est un lieu.  
> « la récréation » est faux : C’est une pause, pas une matière.  

Sources: vocabulaire (Vocabulaire de la famille, des présentations et de l’école (lycée camerounais : provisorat, censeur, surveillant général, intendant))

### `f13-phrase` · Lesson 13 · multiple choice, level 1

Prompt: Laquelle est une phrase correcte ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Le chien garde la maison.
- ✅ Paul mange une mangue.
- ✅ Nous préparons le repas.
- ❌ le chien la maison  
  _↳ Il n’y a pas de verbe, pas de majuscule et pas de point._
- ❌ Mange une Paul mangue.  
  _↳ Les mots ne sont pas dans l’ordre._
- ❌ nous préparons le repas  
  _↳ Il manque la majuscule et le point._
- ❌ Lisette un livre.  
  _↳ Il manque le verbe._


Three generated variants:

> Laquelle est une phrase correcte ?

- ◻️ le chien la maison  
  _↳ feedback if chosen: Il n’y a pas de verbe, pas de majuscule et pas de point._
- ◻️ Lisette un livre.  
  _↳ feedback if chosen: Il manque le verbe._
- ✅ Le chien garde la maison.
- ◻️ Mange une Paul mangue.  
  _↳ feedback if chosen: Les mots ne sont pas dans l’ordre._

Full working after a second miss:

> La bonne réponse est « Le chien garde la maison. ».  
> « le chien la maison » est faux : Il n’y a pas de verbe, pas de majuscule et pas de point.  
> « Lisette un livre. » est faux : Il manque le verbe.  
> « Mange une Paul mangue. » est faux : Les mots ne sont pas dans l’ordre.  

> Laquelle est une phrase correcte ?

- ✅ Nous préparons le repas.
- ◻️ le chien la maison  
  _↳ feedback if chosen: Il n’y a pas de verbe, pas de majuscule et pas de point._
- ◻️ nous préparons le repas  
  _↳ feedback if chosen: Il manque la majuscule et le point._
- ◻️ Lisette un livre.  
  _↳ feedback if chosen: Il manque le verbe._

Full working after a second miss:

> La bonne réponse est « Nous préparons le repas. ».  
> « le chien la maison » est faux : Il n’y a pas de verbe, pas de majuscule et pas de point.  
> « nous préparons le repas » est faux : Il manque la majuscule et le point.  
> « Lisette un livre. » est faux : Il manque le verbe.  

> Laquelle est une phrase correcte ?

- ◻️ Lisette un livre.  
  _↳ feedback if chosen: Il manque le verbe._
- ◻️ Mange une Paul mangue.  
  _↳ feedback if chosen: Les mots ne sont pas dans l’ordre._
- ✅ Paul mange une mangue.
- ◻️ le chien la maison  
  _↳ feedback if chosen: Il n’y a pas de verbe, pas de majuscule et pas de point._

Full working after a second miss:

> La bonne réponse est « Paul mange une mangue. ».  
> « Lisette un livre. » est faux : Il manque le verbe.  
> « Mange une Paul mangue. » est faux : Les mots ne sont pas dans l’ordre.  
> « le chien la maison » est faux : Il n’y a pas de verbe, pas de majuscule et pas de point.  

Sources: grammaire (La phrase simple : majuscule, point, sujet, verbe, complément)

### `f13-sujet` · Lesson 13 · multiple choice, level 1

Prompt: Quel est le sujet de la phrase « {x.p} » ?

Table `x` (one row is picked each time):

| p | s | v | c |
|---|---|---|---|
| Paul mange une mangue. | Paul | mange | une mangue |
| Ma mère lave le linge. | Ma mère | lave | le linge |
| Les élèves chantent l’hymne national. | Les élèves | chantent | l’hymne national |
| Le chien garde la maison. | Le chien | garde | la maison |
| Lisette lit un livre. | Lisette | lit | un livre |
| Nous préparons le repas. | Nous | préparons | le repas |
| Le professeur corrige les cahiers. | Le professeur | corrige | les cahiers |

Right answer: `{x.s}`; wrong choices: `{x.v}`, `{x.c}`

- Feedback `verbe`: “C’est le verbe (l’action).”
- Feedback `comp`: “C’est le complément. Demande : Qui est-ce qui {x.v} ?”

Three generated variants:

> Quel est le sujet de la phrase « Ma mère lave le linge. » ?

- ◻️ lave  
  _↳ feedback if chosen: C’est le verbe (l’action)._
- ✅ Ma mère
- ◻️ le linge  
  _↳ feedback if chosen: C’est le complément. Demande : Qui est-ce qui lave ?_

Full working after a second miss:

> Qui est-ce qui lave ? Ma mère.  
> Le sujet est « Ma mère ».  

> Quel est le sujet de la phrase « Lisette lit un livre. » ?

- ◻️ un livre  
  _↳ feedback if chosen: C’est le complément. Demande : Qui est-ce qui lit ?_
- ✅ Lisette
- ◻️ lit  
  _↳ feedback if chosen: C’est le verbe (l’action)._

Full working after a second miss:

> Qui est-ce qui lit ? Lisette.  
> Le sujet est « Lisette ».  

> Quel est le sujet de la phrase « Les élèves chantent l’hymne national. » ?

- ◻️ chantent  
  _↳ feedback if chosen: C’est le verbe (l’action)._
- ◻️ l’hymne national  
  _↳ feedback if chosen: C’est le complément. Demande : Qui est-ce qui chantent ?_
- ✅ Les élèves

Full working after a second miss:

> Qui est-ce qui chantent ? Les élèves.  
> Le sujet est « Les élèves ».  

Sources: grammaire (La phrase simple : majuscule, point, sujet, verbe, complément)

### `f13-verbe` · Lesson 13 · multiple choice, level 1

Prompt: Quel est le verbe de la phrase « {x.p} » ?

Table `x` (one row is picked each time):

| p | s | v | c |
|---|---|---|---|
| Paul mange une mangue. | Paul | mange | une mangue |
| Ma mère lave le linge. | Ma mère | lave | le linge |
| Les élèves chantent l’hymne national. | Les élèves | chantent | l’hymne national |
| Le chien garde la maison. | Le chien | garde | la maison |
| Lisette lit un livre. | Lisette | lit | un livre |
| Nous préparons le repas. | Nous | préparons | le repas |
| Le professeur corrige les cahiers. | Le professeur | corrige | les cahiers |

Right answer: `{x.v}`; wrong choices: `{x.s}`, `{x.c}`

- Feedback `sujet`: “C’est le sujet (qui fait l’action).”
- Feedback `comp`: “C’est le complément. Le verbe dit l’action.”

Three generated variants:

> Quel est le verbe de la phrase « Le professeur corrige les cahiers. » ?

- ◻️ les cahiers  
  _↳ feedback if chosen: C’est le complément. Le verbe dit l’action._
- ✅ corrige
- ◻️ Le professeur  
  _↳ feedback if chosen: C’est le sujet (qui fait l’action)._

Full working after a second miss:

> L’action de la phrase : corrige.  
> Le verbe est « corrige ».  

> Quel est le verbe de la phrase « Lisette lit un livre. » ?

- ◻️ Lisette  
  _↳ feedback if chosen: C’est le sujet (qui fait l’action)._
- ◻️ un livre  
  _↳ feedback if chosen: C’est le complément. Le verbe dit l’action._
- ✅ lit

Full working after a second miss:

> L’action de la phrase : lit.  
> Le verbe est « lit ».  

> Quel est le verbe de la phrase « Le chien garde la maison. » ?

- ◻️ la maison  
  _↳ feedback if chosen: C’est le complément. Le verbe dit l’action._
- ◻️ Le chien  
  _↳ feedback if chosen: C’est le sujet (qui fait l’action)._
- ✅ garde

Full working after a second miss:

> L’action de la phrase : garde.  
> Le verbe est « garde ».  

Sources: grammaire (La phrase simple : majuscule, point, sujet, verbe, complément)

### `f13-order` · Lesson 13 · word order, level 2

Prompt: Remets les mots dans l’ordre pour faire une phrase.

Table `x` (one row is picked each time):

| p | s | v | c |
|---|---|---|---|
| Paul mange une mangue. | Paul | mange | une mangue |
| Ma mère lave le linge. | Ma mère | lave | le linge |
| Les élèves chantent l’hymne national. | Les élèves | chantent | l’hymne national |
| Le chien garde la maison. | Le chien | garde | la maison |
| Lisette lit un livre. | Lisette | lit | un livre |
| Nous préparons le repas. | Nous | préparons | le repas |
| Le professeur corrige les cahiers. | Le professeur | corrige | les cahiers |

Sentence(s): {x.p}


Three generated variants:

> Remets les mots dans l’ordre pour faire une phrase.

Tiles: Paul · mangue · mange · une (then “.”)
Answer: **Paul mange une mangue.**

Full working after a second miss:

> La phrase est : Paul mange une mangue.  

> Remets les mots dans l’ordre pour faire une phrase.

Tiles: une · Paul · mangue · mange (then “.”)
Answer: **Paul mange une mangue.**

Full working after a second miss:

> La phrase est : Paul mange une mangue.  

> Remets les mots dans l’ordre pour faire une phrase.

Tiles: maison · chien · garde · la · Le (then “.”)
Answer: **Le chien garde la maison.**

Full working after a second miss:

> La phrase est : Le chien garde la maison.  

Sources: grammaire (La phrase simple : majuscule, point, sujet, verbe, complément)

### `f13-spot` · Lesson 13 · spot the error, level 3

Prompt: Une phrase est fausse. Laquelle ?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Une phrase commence par une majuscule.
- ✅ La phrase simple a un seul verbe conjugué.
- ✅ Le sujet fait l’action.
- ✅ Le complément complète le verbe.
- ❌ Le sujet est toujours le dernier mot de la phrase.  
  _↳ Le sujet est souvent au début : on le trouve avec « Qui est-ce qui … ? »._
- ❌ Une phrase n’a pas besoin de point.  
  _↳ Une phrase se termine par un point._
- ❌ Le verbe est la personne qui fait l’action.  
  _↳ Le verbe est l’action ; le sujet fait l’action._


Three generated variants:

> Une phrase est fausse. Laquelle ?

- ✅ Une phrase n’a pas besoin de point.  
  _↳ explanation: Une phrase se termine par un point._
- ◻️ Le sujet fait l’action.
- ◻️ La phrase simple a un seul verbe conjugué.
- ◻️ Le complément complète le verbe.

Full working after a second miss:

> La phrase fausse est « Une phrase n’a pas besoin de point. ».  
> Une phrase se termine par un point.  

> Une phrase est fausse. Laquelle ?

- ◻️ Une phrase commence par une majuscule.
- ✅ Le sujet est toujours le dernier mot de la phrase.  
  _↳ explanation: Le sujet est souvent au début : on le trouve avec « Qui est-ce qui … ? »._
- ◻️ Le sujet fait l’action.
- ◻️ La phrase simple a un seul verbe conjugué.

Full working after a second miss:

> La phrase fausse est « Le sujet est toujours le dernier mot de la phrase. ».  
> Le sujet est souvent au début : on le trouve avec « Qui est-ce qui … ? ».  

> Une phrase est fausse. Laquelle ?

- ◻️ Le sujet fait l’action.
- ◻️ Une phrase commence par une majuscule.
- ◻️ La phrase simple a un seul verbe conjugué.
- ✅ Le sujet est toujours le dernier mot de la phrase.  
  _↳ explanation: Le sujet est souvent au début : on le trouve avec « Qui est-ce qui … ? »._

Full working after a second miss:

> La phrase fausse est « Le sujet est toujours le dernier mot de la phrase. ».  
> Le sujet est souvent au début : on le trouve avec « Qui est-ce qui … ? ».  

Sources: grammaire (La phrase simple : majuscule, point, sujet, verbe, complément)

### `f14-which` · Lesson 14 · multiple choice, level 1

Prompt: Quel mot est bien copié ? Modèle : « {x.w} »

Table `x` (one row is picked each time):

| w | a | b |
|---|---|---|
| élève | eleve | élêve |
| fenêtre | fenetre | fenétre |
| garçon | garcon | garçone |
| école | ecole | écolle |
| forêt | foret | forèt |
| mère | mere | mére |
| hôpital | hopital | hôpitale |
| maïs | mais | maîs |
| frère | frere | frére |
| téléphone | telephone | téléfone |

Right answer: `{x.w}`; wrong choices: `{x.a}`, `{x.b}`

- Feedback `accent`: “Il manque un accent ou un signe : compare avec « {x.w} ».”
- Feedback `autre`: “Une lettre ou un accent n’est pas comme le modèle « {x.w} ».”

Three generated variants:

> Quel mot est bien copié ? Modèle : « téléphone »

- ✅ téléphone
- ◻️ telephone  
  _↳ feedback if chosen: Il manque un accent ou un signe : compare avec « téléphone »._
- ◻️ téléfone  
  _↳ feedback if chosen: Une lettre ou un accent n’est pas comme le modèle « téléphone »._

Full working after a second miss:

> Compare lettre par lettre avec le modèle.  
> Le mot bien copié est « téléphone ».  

> Quel mot est bien copié ? Modèle : « frère »

- ✅ frère
- ◻️ frere  
  _↳ feedback if chosen: Il manque un accent ou un signe : compare avec « frère »._
- ◻️ frére  
  _↳ feedback if chosen: Une lettre ou un accent n’est pas comme le modèle « frère »._

Full working after a second miss:

> Compare lettre par lettre avec le modèle.  
> Le mot bien copié est « frère ».  

> Quel mot est bien copié ? Modèle : « maïs »

- ◻️ mais  
  _↳ feedback if chosen: Il manque un accent ou un signe : compare avec « maïs »._
- ◻️ maîs  
  _↳ feedback if chosen: Une lettre ou un accent n’est pas comme le modèle « maïs »._
- ✅ maïs

Full working after a second miss:

> Compare lettre par lettre avec le modèle.  
> Le mot bien copié est « maïs ».  

Sources: ecriture (Copier des mots sans faute (accents, cédille, tréma))

### `f14-fault` · Lesson 14 · multiple choice, level 2

Prompt: Quel mot contient une faute de copie ? Modèle : « {x.w} »

Table `x` (one row is picked each time):

| w | a | b |
|---|---|---|
| élève | eleve | élêve |
| fenêtre | fenetre | fenétre |
| garçon | garcon | garçone |
| école | ecole | écolle |
| forêt | foret | forèt |
| mère | mere | mére |
| hôpital | hopital | hôpitale |
| maïs | mais | maîs |
| frère | frere | frére |
| téléphone | telephone | téléfone |

Right answer: `{x.a}`; wrong choices: `{x.w}`

- Feedback `bon`: “Ce mot est exactement comme le modèle.”

Three generated variants:

> Quel mot contient une faute de copie ? Modèle : « mère »

- ✅ mere
- ◻️ mère  
  _↳ feedback if chosen: Ce mot est exactement comme le modèle._

Full working after a second miss:

> « mere » n’est pas comme le modèle « mère ».  
> La faute est dans « mere ».  

> Quel mot contient une faute de copie ? Modèle : « maïs »

- ◻️ maïs  
  _↳ feedback if chosen: Ce mot est exactement comme le modèle._
- ✅ mais

Full working after a second miss:

> « mais » n’est pas comme le modèle « maïs ».  
> La faute est dans « mais ».  

> Quel mot contient une faute de copie ? Modèle : « école »

- ✅ ecole
- ◻️ école  
  _↳ feedback if chosen: Ce mot est exactement comme le modèle._

Full working after a second miss:

> « ecole » n’est pas comme le modèle « école ».  
> La faute est dans « ecole ».  

Sources: ecriture (Copier des mots sans faute (accents, cédille, tréma))

### `f14-type` · Lesson 14 · fill the blank, level 3

Prompt: Recopie le mot exactement, avec ses accents.
Sentence: Recopie le mot « {x.w} » : ___
Right answer: `x.w`

Table `x` (one row is picked each time):

| w | a | b |
|---|---|---|
| élève | eleve | élêve |
| fenêtre | fenetre | fenétre |
| garçon | garcon | garçone |
| école | ecole | écolle |
| forêt | foret | forèt |
| mère | mere | mére |
| hôpital | hopital | hôpitale |
| maïs | mais | maîs |
| frère | frere | frére |
| téléphone | telephone | téléfone |

- Feedback `accent` (typed `x.a`): “Il manque un accent ou un signe : « {x.w} ».”

Three generated variants:

> Recopie le mot exactement, avec ses accents.

Sentence: **Recopie le mot « fenêtre » : ___**
Typed answer accepted (case and extra spaces ignored): **fenêtre**
- Typed **fenetre** (accent) → “Il manque un accent ou un signe : « fenêtre ».”

Full working after a second miss:

> Regarde chaque lettre et chaque accent.  
> On écrit : fenêtre.  

> Recopie le mot exactement, avec ses accents.

Sentence: **Recopie le mot « frère » : ___**
Typed answer accepted (case and extra spaces ignored): **frère**
- Typed **frere** (accent) → “Il manque un accent ou un signe : « frère ».”

Full working after a second miss:

> Regarde chaque lettre et chaque accent.  
> On écrit : frère.  

> Recopie le mot exactement, avec ses accents.

Sentence: **Recopie le mot « frère » : ___**
Typed answer accepted (case and extra spaces ignored): **frère**
- Typed **frere** (accent) → “Il manque un accent ou un signe : « frère ».”

Full working after a second miss:

> Regarde chaque lettre et chaque accent.  
> On écrit : frère.  

Sources: ecriture (Copier des mots sans faute (accents, cédille, tréma))

### `fc14-3-check` · Lesson 14 · multiple choice, level 1

Prompt: Quel mot est bien copié ? Modèle : « garçon »

Shows 1 true and 3 false statement(s), drawn from:

- ✅ garçon
- ❌ garcon  
  _↳ Il manque la cédille sous le c._
- ❌ garçone  
  _↳ Il y a un e en trop._
- ❌ garcçon  
  _↳ Il y a une lettre en trop._
- ❌ gaçron  
  _↳ Les lettres ne sont pas dans l’ordre._


Three generated variants:

> Quel mot est bien copié ? Modèle : « garçon »

- ◻️ gaçron  
  _↳ feedback if chosen: Les lettres ne sont pas dans l’ordre._
- ✅ garçon
- ◻️ garçone  
  _↳ feedback if chosen: Il y a un e en trop._
- ◻️ garcon  
  _↳ feedback if chosen: Il manque la cédille sous le c._

Full working after a second miss:

> La bonne réponse est « garçon ».  
> « gaçron » est faux : Les lettres ne sont pas dans l’ordre.  
> « garçone » est faux : Il y a un e en trop.  
> « garcon » est faux : Il manque la cédille sous le c.  

> Quel mot est bien copié ? Modèle : « garçon »

- ✅ garçon
- ◻️ gaçron  
  _↳ feedback if chosen: Les lettres ne sont pas dans l’ordre._
- ◻️ garcçon  
  _↳ feedback if chosen: Il y a une lettre en trop._
- ◻️ garcon  
  _↳ feedback if chosen: Il manque la cédille sous le c._

Full working after a second miss:

> La bonne réponse est « garçon ».  
> « gaçron » est faux : Les lettres ne sont pas dans l’ordre.  
> « garcçon » est faux : Il y a une lettre en trop.  
> « garcon » est faux : Il manque la cédille sous le c.  

> Quel mot est bien copié ? Modèle : « garçon »

- ◻️ gaçron  
  _↳ feedback if chosen: Les lettres ne sont pas dans l’ordre._
- ◻️ garçone  
  _↳ feedback if chosen: Il y a un e en trop._
- ✅ garçon
- ◻️ garcon  
  _↳ feedback if chosen: Il manque la cédille sous le c._

Full working after a second miss:

> La bonne réponse est « garçon ».  
> « gaçron » est faux : Les lettres ne sont pas dans l’ordre.  
> « garçone » est faux : Il y a un e en trop.  
> « garcon » est faux : Il manque la cédille sous le c.  

Sources: ecriture (Copier des mots sans faute (accents, cédille, tréma))

### `f15-spot` · Lesson 15 · spot the error, level 3

Prompt: Une phrase est fausse. Laquelle ?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Lisette aime son père.
- ✅ Nous lavons notre voiture.
- ✅ Les enfants rangent leurs cahiers.
- ✅ Mon amie habite à Buea.
- ❌ Paul aime son mère.  
  _↳ « mère » est féminin et commence par une consonne : sa mère._
- ❌ Vous oubliez votre cahiers.  
  _↳ Au pluriel : vos cahiers._
- ❌ Elle cherche ma amie.  
  _↳ Devant une voyelle : mon amie._


Three generated variants:

> Une phrase est fausse. Laquelle ?

- ◻️ Les enfants rangent leurs cahiers.
- ◻️ Nous lavons notre voiture.
- ◻️ Mon amie habite à Buea.
- ✅ Vous oubliez votre cahiers.  
  _↳ explanation: Au pluriel : vos cahiers._

Full working after a second miss:

> La phrase fausse est « Vous oubliez votre cahiers. ».  
> Au pluriel : vos cahiers.  

> Une phrase est fausse. Laquelle ?

- ◻️ Lisette aime son père.
- ◻️ Nous lavons notre voiture.
- ✅ Paul aime son mère.  
  _↳ explanation: « mère » est féminin et commence par une consonne : sa mère._
- ◻️ Les enfants rangent leurs cahiers.

Full working after a second miss:

> La phrase fausse est « Paul aime son mère. ».  
> « mère » est féminin et commence par une consonne : sa mère.  

> Une phrase est fausse. Laquelle ?

- ◻️ Lisette aime son père.
- ◻️ Nous lavons notre voiture.
- ◻️ Mon amie habite à Buea.
- ✅ Elle cherche ma amie.  
  _↳ explanation: Devant une voyelle : mon amie._

Full working after a second miss:

> La phrase fausse est « Elle cherche ma amie. ».  
> Devant une voyelle : mon amie.  

Sources: possessifs (Adjectifs possessifs ; mon/ton/son devant un nom féminin commençant par une voyelle)

### `fc15-3-check` · Lesson 15 · multiple choice, level 1

Prompt: Laquelle est correcte ?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ mon école
- ✅ ton amie
- ✅ son orange
- ❌ ma école  
  _↳ Devant une voyelle : mon école._
- ❌ ta amie  
  _↳ Devant une voyelle : ton amie._
- ❌ sa orange  
  _↳ Devant une voyelle : son orange._
- ❌ mes école  
  _↳ Au singulier : mon école._


Three generated variants:

> Laquelle est correcte ?

- ◻️ ma école  
  _↳ feedback if chosen: Devant une voyelle : mon école._
- ◻️ sa orange  
  _↳ feedback if chosen: Devant une voyelle : son orange._
- ✅ ton amie
- ◻️ ta amie  
  _↳ feedback if chosen: Devant une voyelle : ton amie._

Full working after a second miss:

> La bonne réponse est « ton amie ».  
> « ma école » est faux : Devant une voyelle : mon école.  
> « sa orange » est faux : Devant une voyelle : son orange.  
> « ta amie » est faux : Devant une voyelle : ton amie.  

> Laquelle est correcte ?

- ◻️ ma école  
  _↳ feedback if chosen: Devant une voyelle : mon école._
- ◻️ mes école  
  _↳ feedback if chosen: Au singulier : mon école._
- ✅ ton amie
- ◻️ ta amie  
  _↳ feedback if chosen: Devant une voyelle : ton amie._

Full working after a second miss:

> La bonne réponse est « ton amie ».  
> « ma école » est faux : Devant une voyelle : mon école.  
> « mes école » est faux : Au singulier : mon école.  
> « ta amie » est faux : Devant une voyelle : ton amie.  

> Laquelle est correcte ?

- ✅ son orange
- ◻️ ta amie  
  _↳ feedback if chosen: Devant une voyelle : ton amie._
- ◻️ mes école  
  _↳ feedback if chosen: Au singulier : mon école._
- ◻️ ma école  
  _↳ feedback if chosen: Devant une voyelle : mon école._

Full working after a second miss:

> La bonne réponse est « son orange ».  
> « ta amie » est faux : Devant une voyelle : ton amie.  
> « mes école » est faux : Au singulier : mon école.  
> « ma école » est faux : Devant une voyelle : mon école.  

Sources: possessifs (Adjectifs possessifs ; mon/ton/son devant un nom féminin commençant par une voyelle)

