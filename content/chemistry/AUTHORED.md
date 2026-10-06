# Chemistry Form 1, Batch C1: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:chemistry`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: tables and rules the computed answers use (src/engine/lib/chemistry.js, physics.js)

**Elements (TR-K02)**: atomic number, symbol, name, kind.

| Z | Symbol | Name | Kind |
|---|---|---|---|
| 1 | H | hydrogen | non-metal |
| 2 | He | helium | non-metal |
| 3 | Li | lithium | metal |
| 4 | Be | beryllium | metal |
| 5 | B | boron | metalloid |
| 6 | C | carbon | non-metal |
| 7 | N | nitrogen | non-metal |
| 8 | O | oxygen | non-metal |
| 9 | F | fluorine | non-metal |
| 10 | Ne | neon | non-metal |
| 11 | Na | sodium | metal |
| 12 | Mg | magnesium | metal |
| 13 | Al | aluminium | metal |
| 14 | Si | silicon | metalloid |
| 15 | P | phosphorus | non-metal |
| 16 | S | sulfur | non-metal |
| 17 | Cl | chlorine | non-metal |
| 18 | Ar | argon | non-metal |
| 19 | K | potassium | metal |
| 20 | Ca | calcium | metal |
| 26 | Fe | iron | metal |
| 29 | Cu | copper | metal |
| 30 | Zn | zinc | metal |
| 47 | Ag | silver | metal |
| 50 | Sn | tin | metal |
| 53 | I | iodine | non-metal |
| 79 | Au | gold | metal |
| 80 | Hg | mercury | metal |
| 82 | Pb | lead | metal |

**Symbols from Latin (TR-K02)**: Na (natrium), K (kalium), Fe (ferrum), Cu (cuprum), Ag (argentum), Sn (stannum), Au (aurum), Hg (hydrargyrum), Pb (plumbum).

- **Formulas (TR-K03)**: the small number after a symbol counts the atoms of that symbol; no number means one; a bracket multiplies everything inside it (Ca(OH)₂: 1 Ca, 2 O, 2 H). Counted by `parseFormula()`, tested on known answers.
- **Measurement**: the unit conversions, °C → K (+ 273), the measuring cylinder and thermometer drawings are the same as in Physics (TR-P04, TR-P05, TR-P08).

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `ch1-branch` | 1 | matching, 1 | chemistry |
| 2 | `ch1-which` | 1 | multiple choice, 1 | chemistry |
| 3 | `ch1-true` | 1 | multiple choice, 2 | chemistry |
| 4 | `ch1-spot` | 1 | spot the error, 3 | chemistry |
| 5 | `chc1-1-check` (card chc1-1) | 1 | multiple choice, 1 | chemistry |
| 6 | `ch2-match` | 2 | matching, 1 | chemistry-life |
| 7 | `ch2-area` | 2 | multiple choice, 1 | chemistry-life |
| 8 | `ch2-sort` | 2 | matching, 2 | chemistry-life |
| 9 | `ch2-spot` | 2 | spot the error, 3 | chemistry-life |
| 10 | `chc2-3-check` (card chc2-3) | 2 | multiple choice, 1 | chemistry-life |
| 11 | `ch3-match` | 3 | matching, 1 | equipment-chem |
| 12 | `ch3-choose` | 3 | multiple choice, 1 | equipment-chem |
| 13 | `ch3-sort` | 3 | matching, 2 | equipment-chem |
| 14 | `ch3-spot` | 3 | spot the error, 3 | equipment-chem |
| 15 | `chc3-3-check` (card chc3-3) | 3 | multiple choice, 1 | equipment-chem |
| 16 | `ch4-match` | 4 | matching, 1 | equipment-chem |
| 17 | `ch4-choose` | 4 | multiple choice, 1 | equipment-chem |
| 18 | `ch4-sort` | 4 | matching, 2 | equipment-chem |
| 19 | `ch4-spot` | 4 | spot the error, 3 | equipment-chem |
| 20 | `chc4-3-check` (card chc4-3) | 4 | multiple choice, 1 | equipment-chem |
| 21 | `ch5-match` | 5 | matching, 1 | hazards-chem |
| 22 | `ch5-reagent` | 5 | multiple choice, 1 | hazards-chem |
| 23 | `ch5-act` | 5 | multiple choice, 2 | hazards-chem |
| 24 | `ch5-spot` | 5 | spot the error, 3 | hazards-chem |
| 25 | `chc5-3-check` (card chc5-3) | 5 | multiple choice, 1 | hazards-chem |
| 26 | `ch6-sort` | 6 | matching, 1 | safety-chem |
| 27 | `ch6-what` | 6 | multiple choice, 1 | safety-chem |
| 28 | `ch6-why` | 6 | multiple choice, 2 | safety-chem |
| 29 | `ch6-spot` | 6 | spot the error, 3 | safety-chem |
| 30 | `chc6-2-check` (card chc6-2) | 6 | multiple choice, 1 | safety-chem |
| 31 | `ch8-spot` | 8 | spot the error, 3 | measure-chem |
| 32 | `ch9-sort` | 9 | matching, 1 | changes |
| 33 | `ch9-which` | 9 | multiple choice, 1 | changes |
| 34 | `ch9-sign` | 9 | multiple choice, 1 | changes |
| 35 | `ch9-why` | 9 | multiple choice, 2 | changes |
| 36 | `ch9-spot` | 9 | spot the error, 3 | changes |
| 37 | `ch10-state` | 10 | multiple choice, 1 | states |
| 38 | `ch10-example` | 10 | multiple choice, 2 | states |
| 39 | `ch10-spot` | 10 | spot the error, 3 | states |
| 40 | `chc10-3-check` (card chc10-3) | 10 | multiple choice, 1 | states |
| 41 | `ch11-move` | 11 | multiple choice, 1 | kinetic |
| 42 | `ch11-heat` | 11 | multiple choice, 1 | kinetic |
| 43 | `ch11-diffusion` | 11 | multiple choice, 1 | kinetic |
| 44 | `ch11-faster` | 11 | multiple choice, 2 | kinetic |
| 45 | `ch11-spot` | 11 | spot the error, 3 | kinetic |
| 46 | `ch12-sort` | 12 | matching, 1 | mixtures |
| 47 | `ch12-which` | 12 | multiple choice, 1 | mixtures |
| 48 | `ch12-why` | 12 | multiple choice, 2 | mixtures |
| 49 | `ch12-spot` | 12 | spot the error, 3 | mixtures |
| 50 | `chc12-3-check` (card chc12-3) | 12 | multiple choice, 1 | mixtures |
| 51 | `ch13-type` | 13 | multiple choice, 1 | mixtures |
| 52 | `ch13-misc` | 13 | matching, 1 | mixtures |
| 53 | `ch13-solution` | 13 | matching, 2 | mixtures |
| 54 | `ch13-spot` | 13 | spot the error, 3 | mixtures |
| 55 | `chc13-3-check` (card chc13-3) | 13 | multiple choice, 1 | mixtures |
| 56 | `ch14-method` | 14 | multiple choice, 1 | separation |
| 57 | `ch14-match` | 14 | matching, 1 | separation |
| 58 | `ch14-steps` | 14 | ordering, 1 | separation |
| 59 | `ch14-why` | 14 | multiple choice, 2 | separation |
| 60 | `ch14-spot` | 14 | spot the error, 3 | separation |
| 61 | `ch15-method` | 15 | multiple choice, 1 | separation |
| 62 | `ch15-match` | 15 | matching, 1 | separation |
| 63 | `ch15-distil` | 15 | ordering, 2 | separation |
| 64 | `ch15-words` | 15 | multiple choice, 2 | separation |
| 65 | `ch15-spot` | 15 | spot the error, 3 | separation |
| 66 | `chc15-3-check` (card chc15-3) | 15 | multiple choice, 1 | separation |
| 67 | `ch16-method` | 16 | multiple choice, 1 | separation |
| 68 | `ch16-funnel` | 16 | ordering, 2 | separation |
| 69 | `ch16-spot` | 16 | spot the error, 3 | separation |
| 70 | `chc16-3-check` (card chc16-3) | 16 | multiple choice, 1 | separation |
| 71 | `ch17-which` | 17 | multiple choice, 1 | separation |
| 72 | `ch17-heat` | 17 | multiple choice, 1 | separation |
| 73 | `ch17-fish` | 17 | multiple choice, 2 | separation |
| 74 | `ch17-spot` | 17 | spot the error, 3 | separation |
| 75 | `chc17-3-check` (card chc17-3) | 17 | multiple choice, 1 | separation |
| 76 | `ch18-air` | 18 | multiple choice, 1 | separation |
| 77 | `ch18-method` | 18 | multiple choice, 1 | separation |
| 78 | `ch18-why` | 18 | multiple choice, 2 | separation |
| 79 | `ch18-spot` | 18 | spot the error, 3 | separation |
| 80 | `chc18-3-check` (card chc18-3) | 18 | multiple choice, 1 | separation |
| 81 | `ch19-match` | 19 | matching, 1 | elements |
| 82 | `ch19-symbol` | 19 | multiple choice, 1 | elements |
| 83 | `ch19-sort` | 19 | matching, 2 | elements |
| 84 | `ch19-name` | 19 | fill the blank, 2 | elements |
| 85 | `ch19-spot` | 19 | spot the error, 3 | elements |
| 86 | `chc19-1-check` (card chc19-1) | 19 | multiple choice, 1 | elements |
| 87 | `ch21-sort` | 21 | matching, 1 | compounds |
| 88 | `ch21-which` | 21 | multiple choice, 1 | compounds |
| 89 | `ch21-test` | 21 | multiple choice, 2 | compounds |
| 90 | `ch21-spot` | 21 | spot the error, 3 | compounds |
| 91 | `chc21-3-check` (card chc21-3) | 21 | multiple choice, 1 | compounds |

### `ch1-branch` · Lesson 1 · matching, level 1

Prompt: Match each branch of chemistry with what it studies.

Pairs (4 shown each time):

- Organic chemistry → **the compounds of carbon found in living things, fuels and plastics**
- Inorganic chemistry → **metals, salts and minerals**
- Analytical chemistry → **what a sample contains and how much of each substance**
- Biochemistry → **the chemical changes that happen inside living things**
- Physical chemistry → **energy changes and how fast reactions happen**


Three generated variants:

> Match each branch of chemistry with what it studies.

Right-hand side (shuffled): metals, salts and minerals · the compounds of carbon found in living things, fuels and plastics · what a sample contains and how much of each substance · energy changes and how fast reactions happen
- Analytical chemistry → **what a sample contains and how much of each substance**
- Inorganic chemistry → **metals, salts and minerals**
- Physical chemistry → **energy changes and how fast reactions happen**
- Organic chemistry → **the compounds of carbon found in living things, fuels and plastics**

Full working after a second miss:

> The right pairs are:  
> Analytical chemistry → what a sample contains and how much of each substance  
> Inorganic chemistry → metals, salts and minerals  
> Physical chemistry → energy changes and how fast reactions happen  
> Organic chemistry → the compounds of carbon found in living things, fuels and plastics  

> Match each branch of chemistry with what it studies.

Right-hand side (shuffled): what a sample contains and how much of each substance · the chemical changes that happen inside living things · the compounds of carbon found in living things, fuels and plastics · metals, salts and minerals
- Organic chemistry → **the compounds of carbon found in living things, fuels and plastics**
- Analytical chemistry → **what a sample contains and how much of each substance**
- Biochemistry → **the chemical changes that happen inside living things**
- Inorganic chemistry → **metals, salts and minerals**

Full working after a second miss:

> The right pairs are:  
> Organic chemistry → the compounds of carbon found in living things, fuels and plastics  
> Analytical chemistry → what a sample contains and how much of each substance  
> Biochemistry → the chemical changes that happen inside living things  
> Inorganic chemistry → metals, salts and minerals  

> Match each branch of chemistry with what it studies.

Right-hand side (shuffled): the chemical changes that happen inside living things · what a sample contains and how much of each substance · metals, salts and minerals · the compounds of carbon found in living things, fuels and plastics
- Biochemistry → **the chemical changes that happen inside living things**
- Organic chemistry → **the compounds of carbon found in living things, fuels and plastics**
- Inorganic chemistry → **metals, salts and minerals**
- Analytical chemistry → **what a sample contains and how much of each substance**

Full working after a second miss:

> The right pairs are:  
> Biochemistry → the chemical changes that happen inside living things  
> Organic chemistry → the compounds of carbon found in living things, fuels and plastics  
> Inorganic chemistry → metals, salts and minerals  
> Analytical chemistry → what a sample contains and how much of each substance  

Sources: chemistry (What chemistry is; branches of chemistry)

### `ch1-which` · Lesson 1 · multiple choice, level 1

Prompt: Which branch of chemistry studies {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| the compounds of carbon found in living things, fuels and plastics | Organic chemistry | Organic chemistry studies the compounds of carbon found in living things, fuels and plastics. |
| metals, salts and minerals | Inorganic chemistry | Inorganic chemistry studies metals, salts and minerals. |
| what a sample contains and how much of each substance | Analytical chemistry | Analytical chemistry studies what a sample contains and how much of each substance. |
| the chemical changes that happen inside living things | Biochemistry | Biochemistry studies the chemical changes that happen inside living things. |
| energy changes and how fast reactions happen | Physical chemistry | Physical chemistry studies energy changes and how fast reactions happen. |

Right answer: `{x.a}`; wrong choices: `Organic chemistry`, `Inorganic chemistry`, `Analytical chemistry`, `Biochemistry`, `Physical chemistry`

- Feedback `other`: “Not this branch. Read what each branch studies again.”

Three generated variants:

> Which branch of chemistry studies the chemical changes that happen inside living things?

- ◻️ Organic chemistry  
  _↳ feedback if chosen: Not this branch. Read what each branch studies again._
- ✅ Biochemistry
- ◻️ Analytical chemistry  
  _↳ feedback if chosen: Not this branch. Read what each branch studies again._
- ◻️ Physical chemistry  
  _↳ feedback if chosen: Not this branch. Read what each branch studies again._

Full working after a second miss:

> Biochemistry studies the chemical changes that happen inside living things.  
> Answer: Biochemistry.  

> Which branch of chemistry studies the compounds of carbon found in living things, fuels and plastics?

- ✅ Organic chemistry
- ◻️ Analytical chemistry  
  _↳ feedback if chosen: Not this branch. Read what each branch studies again._
- ◻️ Biochemistry  
  _↳ feedback if chosen: Not this branch. Read what each branch studies again._
- ◻️ Inorganic chemistry  
  _↳ feedback if chosen: Not this branch. Read what each branch studies again._

Full working after a second miss:

> Organic chemistry studies the compounds of carbon found in living things, fuels and plastics.  
> Answer: Organic chemistry.  

> Which branch of chemistry studies metals, salts and minerals?

- ✅ Inorganic chemistry
- ◻️ Analytical chemistry  
  _↳ feedback if chosen: Not this branch. Read what each branch studies again._
- ◻️ Physical chemistry  
  _↳ feedback if chosen: Not this branch. Read what each branch studies again._
- ◻️ Organic chemistry  
  _↳ feedback if chosen: Not this branch. Read what each branch studies again._

Full working after a second miss:

> Inorganic chemistry studies metals, salts and minerals.  
> Answer: Inorganic chemistry.  

Sources: chemistry (What chemistry is; branches of chemistry)

### `ch1-true` · Lesson 1 · multiple choice, level 2

Prompt: Which sentence is true?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Chemistry studies what substances are made of and how they change.
- ✅ Burning firewood is a change that chemistry studies.
- ✅ A chemist records results honestly.
- ❌ Chemistry only studies dangerous substances.  
  _↳ Chemistry studies all matter: water, food, soap, air, medicines._
- ❌ Chemistry is the study of living things.  
  _↳ Living things are Biology; chemistry studies substances and their changes._
- ❌ A chemist changes results that look wrong.  
  _↳ Results are recorded as they are, even when they are surprising._


Three generated variants:

> Which sentence is true?

- ◻️ A chemist changes results that look wrong.  
  _↳ feedback if chosen: Results are recorded as they are, even when they are surprising._
- ✅ Chemistry studies what substances are made of and how they change.
- ◻️ Chemistry is the study of living things.  
  _↳ feedback if chosen: Living things are Biology; chemistry studies substances and their changes._
- ◻️ Chemistry only studies dangerous substances.  
  _↳ feedback if chosen: Chemistry studies all matter: water, food, soap, air, medicines._

Full working after a second miss:

> The true statement is “Chemistry studies what substances are made of and how they change.”.  
> “A chemist changes results that look wrong.” is false: Results are recorded as they are, even when they are surprising.  
> “Chemistry is the study of living things.” is false: Living things are Biology; chemistry studies substances and their changes.  
> “Chemistry only studies dangerous substances.” is false: Chemistry studies all matter: water, food, soap, air, medicines.  

> Which sentence is true?

- ◻️ A chemist changes results that look wrong.  
  _↳ feedback if chosen: Results are recorded as they are, even when they are surprising._
- ◻️ Chemistry only studies dangerous substances.  
  _↳ feedback if chosen: Chemistry studies all matter: water, food, soap, air, medicines._
- ◻️ Chemistry is the study of living things.  
  _↳ feedback if chosen: Living things are Biology; chemistry studies substances and their changes._
- ✅ Chemistry studies what substances are made of and how they change.

Full working after a second miss:

> The true statement is “Chemistry studies what substances are made of and how they change.”.  
> “A chemist changes results that look wrong.” is false: Results are recorded as they are, even when they are surprising.  
> “Chemistry only studies dangerous substances.” is false: Chemistry studies all matter: water, food, soap, air, medicines.  
> “Chemistry is the study of living things.” is false: Living things are Biology; chemistry studies substances and their changes.  

> Which sentence is true?

- ◻️ A chemist changes results that look wrong.  
  _↳ feedback if chosen: Results are recorded as they are, even when they are surprising._
- ◻️ Chemistry only studies dangerous substances.  
  _↳ feedback if chosen: Chemistry studies all matter: water, food, soap, air, medicines._
- ✅ Chemistry studies what substances are made of and how they change.
- ◻️ Chemistry is the study of living things.  
  _↳ feedback if chosen: Living things are Biology; chemistry studies substances and their changes._

Full working after a second miss:

> The true statement is “Chemistry studies what substances are made of and how they change.”.  
> “A chemist changes results that look wrong.” is false: Results are recorded as they are, even when they are surprising.  
> “Chemistry only studies dangerous substances.” is false: Chemistry studies all matter: water, food, soap, air, medicines.  
> “Chemistry is the study of living things.” is false: Living things are Biology; chemistry studies substances and their changes.  

Sources: chemistry (What chemistry is; branches of chemistry)

### `ch1-spot` · Lesson 1 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Organic chemistry studies compounds of carbon.
- ✅ Analytical chemistry finds out what a sample contains.
- ✅ Biochemistry studies chemical changes in living things.
- ✅ Inorganic chemistry studies metals and salts.
- ❌ Physical chemistry studies plants and animals.  
  _↳ Physical chemistry studies energy changes and how fast reactions go._
- ❌ Organic chemistry studies only metals.  
  _↳ Organic chemistry studies compounds of carbon. Metals are inorganic chemistry._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Analytical chemistry finds out what a sample contains.
- ◻️ Organic chemistry studies compounds of carbon.
- ◻️ Biochemistry studies chemical changes in living things.
- ✅ Organic chemistry studies only metals.  
  _↳ explanation: Organic chemistry studies compounds of carbon. Metals are inorganic chemistry._

Full working after a second miss:

> The wrong statement is “Organic chemistry studies only metals.”.  
> Organic chemistry studies compounds of carbon. Metals are inorganic chemistry.  

> One sentence is wrong. Which one?

- ✅ Physical chemistry studies plants and animals.  
  _↳ explanation: Physical chemistry studies energy changes and how fast reactions go._
- ◻️ Analytical chemistry finds out what a sample contains.
- ◻️ Biochemistry studies chemical changes in living things.
- ◻️ Inorganic chemistry studies metals and salts.

Full working after a second miss:

> The wrong statement is “Physical chemistry studies plants and animals.”.  
> Physical chemistry studies energy changes and how fast reactions go.  

> One sentence is wrong. Which one?

- ◻️ Inorganic chemistry studies metals and salts.
- ◻️ Biochemistry studies chemical changes in living things.
- ◻️ Analytical chemistry finds out what a sample contains.
- ✅ Organic chemistry studies only metals.  
  _↳ explanation: Organic chemistry studies compounds of carbon. Metals are inorganic chemistry._

Full working after a second miss:

> The wrong statement is “Organic chemistry studies only metals.”.  
> Organic chemistry studies compounds of carbon. Metals are inorganic chemistry.  

Sources: chemistry (What chemistry is; branches of chemistry)

### `chc1-1-check` · Lesson 1 · multiple choice, level 1

Prompt: Which question is a chemistry question?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ What is table salt made of?
- ✅ Why does iron rust?
- ❌ How fast does a taxi move?  
  _↳ Speed and motion are Physics._
- ❌ How does a goat digest grass?  
  _↳ Digestion in an animal is Biology._
- ❌ What will the weather be tomorrow?  
  _↳ Weather is Meteorology._


Three generated variants:

> Which question is a chemistry question?

- ◻️ What will the weather be tomorrow?  
  _↳ feedback if chosen: Weather is Meteorology._
- ◻️ How fast does a taxi move?  
  _↳ feedback if chosen: Speed and motion are Physics._
- ◻️ How does a goat digest grass?  
  _↳ feedback if chosen: Digestion in an animal is Biology._
- ✅ Why does iron rust?

Full working after a second miss:

> The true statement is “Why does iron rust?”.  
> “What will the weather be tomorrow?” is false: Weather is Meteorology.  
> “How fast does a taxi move?” is false: Speed and motion are Physics.  
> “How does a goat digest grass?” is false: Digestion in an animal is Biology.  

> Which question is a chemistry question?

- ◻️ What will the weather be tomorrow?  
  _↳ feedback if chosen: Weather is Meteorology._
- ◻️ How fast does a taxi move?  
  _↳ feedback if chosen: Speed and motion are Physics._
- ◻️ How does a goat digest grass?  
  _↳ feedback if chosen: Digestion in an animal is Biology._
- ✅ Why does iron rust?

Full working after a second miss:

> The true statement is “Why does iron rust?”.  
> “What will the weather be tomorrow?” is false: Weather is Meteorology.  
> “How fast does a taxi move?” is false: Speed and motion are Physics.  
> “How does a goat digest grass?” is false: Digestion in an animal is Biology.  

> Which question is a chemistry question?

- ◻️ How does a goat digest grass?  
  _↳ feedback if chosen: Digestion in an animal is Biology._
- ◻️ How fast does a taxi move?  
  _↳ feedback if chosen: Speed and motion are Physics._
- ✅ Why does iron rust?
- ◻️ What will the weather be tomorrow?  
  _↳ feedback if chosen: Weather is Meteorology._

Full working after a second miss:

> The true statement is “Why does iron rust?”.  
> “How does a goat digest grass?” is false: Digestion in an animal is Biology.  
> “How fast does a taxi move?” is false: Speed and motion are Physics.  
> “What will the weather be tomorrow?” is false: Weather is Meteorology.  

Sources: chemistry (What chemistry is; branches of chemistry)

### `ch2-match` · Lesson 2 · matching, level 1

Prompt: Match each product of chemistry with how it helps us.

Pairs (4 shown each time):

- medicines such as paracetamol → **health**
- fertilisers for maize and cocoa farms → **farming**
- soap and detergents → **cleaning and hygiene**
- chlorine to make water safe to drink → **clean water**
- cement for building houses → **building**
- petrol and kerosene → **fuels and energy**
- salt and vinegar to keep food from going bad → **keeping food**
- plastics for buckets and pipes → **household goods**


Three generated variants:

> Match each product of chemistry with how it helps us.

Right-hand side (shuffled): cleaning and hygiene · farming · keeping food · fuels and energy
- fertilisers for maize and cocoa farms → **farming**
- petrol and kerosene → **fuels and energy**
- soap and detergents → **cleaning and hygiene**
- salt and vinegar to keep food from going bad → **keeping food**

Full working after a second miss:

> The right pairs are:  
> fertilisers for maize and cocoa farms → farming  
> petrol and kerosene → fuels and energy  
> soap and detergents → cleaning and hygiene  
> salt and vinegar to keep food from going bad → keeping food  

> Match each product of chemistry with how it helps us.

Right-hand side (shuffled): health · fuels and energy · keeping food · farming
- medicines such as paracetamol → **health**
- fertilisers for maize and cocoa farms → **farming**
- salt and vinegar to keep food from going bad → **keeping food**
- petrol and kerosene → **fuels and energy**

Full working after a second miss:

> The right pairs are:  
> medicines such as paracetamol → health  
> fertilisers for maize and cocoa farms → farming  
> salt and vinegar to keep food from going bad → keeping food  
> petrol and kerosene → fuels and energy  

> Match each product of chemistry with how it helps us.

Right-hand side (shuffled): farming · cleaning and hygiene · building · fuels and energy
- fertilisers for maize and cocoa farms → **farming**
- petrol and kerosene → **fuels and energy**
- soap and detergents → **cleaning and hygiene**
- cement for building houses → **building**

Full working after a second miss:

> The right pairs are:  
> fertilisers for maize and cocoa farms → farming  
> petrol and kerosene → fuels and energy  
> soap and detergents → cleaning and hygiene  
> cement for building houses → building  

Sources: chemistry-life (Uses of chemistry in daily life (health, farming, cleaning, water, building, fuels, food))

### `ch2-area` · Lesson 2 · multiple choice, level 1

Prompt: In which area of life does chemistry give us {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| medicines such as paracetamol | health | medicines such as paracetamol: health. |
| fertilisers for maize and cocoa farms | farming | fertilisers for maize and cocoa farms: farming. |
| soap and detergents | cleaning and hygiene | soap and detergents: cleaning and hygiene. |
| chlorine to make water safe to drink | clean water | chlorine to make water safe to drink: clean water. |
| cement for building houses | building | cement for building houses: building. |
| petrol and kerosene | fuels and energy | petrol and kerosene: fuels and energy. |
| salt and vinegar to keep food from going bad | keeping food | salt and vinegar to keep food from going bad: keeping food. |
| plastics for buckets and pipes | household goods | plastics for buckets and pipes: household goods. |

Right answer: `{x.a}`; wrong choices: `health`, `farming`, `cleaning and hygiene`, `clean water`, `building`, `fuels and energy`, `keeping food`, `household goods`

- Feedback `other`: “That is a different area. Think about what the product is used for.”

Three generated variants:

> In which area of life does chemistry give us cement for building houses?

- ◻️ cleaning and hygiene  
  _↳ feedback if chosen: That is a different area. Think about what the product is used for._
- ✅ building
- ◻️ fuels and energy  
  _↳ feedback if chosen: That is a different area. Think about what the product is used for._
- ◻️ keeping food  
  _↳ feedback if chosen: That is a different area. Think about what the product is used for._

Full working after a second miss:

> cement for building houses: building.  
> Answer: building.  

> In which area of life does chemistry give us chlorine to make water safe to drink?

- ◻️ keeping food  
  _↳ feedback if chosen: That is a different area. Think about what the product is used for._
- ◻️ farming  
  _↳ feedback if chosen: That is a different area. Think about what the product is used for._
- ◻️ cleaning and hygiene  
  _↳ feedback if chosen: That is a different area. Think about what the product is used for._
- ✅ clean water

Full working after a second miss:

> chlorine to make water safe to drink: clean water.  
> Answer: clean water.  

> In which area of life does chemistry give us plastics for buckets and pipes?

- ◻️ cleaning and hygiene  
  _↳ feedback if chosen: That is a different area. Think about what the product is used for._
- ◻️ building  
  _↳ feedback if chosen: That is a different area. Think about what the product is used for._
- ◻️ keeping food  
  _↳ feedback if chosen: That is a different area. Think about what the product is used for._
- ✅ household goods

Full working after a second miss:

> plastics for buckets and pipes: household goods.  
> Answer: household goods.  

Sources: chemistry-life (Uses of chemistry in daily life (health, farming, cleaning, water, building, fuels, food))

### `ch2-sort` · Lesson 2 · matching, level 2

Prompt: Does each use of chemicals help or harm?

Pairs (6 shown each time, sorted into groups):

- washing clothes with detergent → **helps people**
- treating malaria with medicine → **helps people**
- preserving fish with salt → **helps people**
- killing germs in water with chlorine → **helps people**
- burning plastic waste in the open → **harms people or nature**
- pouring engine oil into a stream → **harms people or nature**
- spraying too much pesticide near a river → **harms people or nature**
- storing kerosene in a drink bottle → **harms people or nature**


Three generated variants:

> Does each use of chemicals help or harm?

Groups: helps people · harms people or nature
- washing clothes with detergent → **helps people**
- treating malaria with medicine → **helps people**
- killing germs in water with chlorine → **helps people**
- spraying too much pesticide near a river → **harms people or nature**
- storing kerosene in a drink bottle → **harms people or nature**
- preserving fish with salt → **helps people**

Full working after a second miss:

> The right pairs are:  
> washing clothes with detergent → helps people  
> treating malaria with medicine → helps people  
> killing germs in water with chlorine → helps people  
> spraying too much pesticide near a river → harms people or nature  
> storing kerosene in a drink bottle → harms people or nature  
> preserving fish with salt → helps people  

> Does each use of chemicals help or harm?

Groups: helps people · harms people or nature
- preserving fish with salt → **helps people**
- killing germs in water with chlorine → **helps people**
- storing kerosene in a drink bottle → **harms people or nature**
- pouring engine oil into a stream → **harms people or nature**
- washing clothes with detergent → **helps people**
- treating malaria with medicine → **helps people**

Full working after a second miss:

> The right pairs are:  
> preserving fish with salt → helps people  
> killing germs in water with chlorine → helps people  
> storing kerosene in a drink bottle → harms people or nature  
> pouring engine oil into a stream → harms people or nature  
> washing clothes with detergent → helps people  
> treating malaria with medicine → helps people  

> Does each use of chemicals help or harm?

Groups: helps people · harms people or nature
- spraying too much pesticide near a river → **harms people or nature**
- washing clothes with detergent → **helps people**
- treating malaria with medicine → **helps people**
- storing kerosene in a drink bottle → **harms people or nature**
- preserving fish with salt → **helps people**
- pouring engine oil into a stream → **harms people or nature**

Full working after a second miss:

> The right pairs are:  
> spraying too much pesticide near a river → harms people or nature  
> washing clothes with detergent → helps people  
> treating malaria with medicine → helps people  
> storing kerosene in a drink bottle → harms people or nature  
> preserving fish with salt → helps people  
> pouring engine oil into a stream → harms people or nature  

Sources: chemistry-life (Uses of chemistry in daily life (health, farming, cleaning, water, building, fuels, food))

### `ch2-spot` · Lesson 2 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Fertilisers help crops grow.
- ✅ Chlorine helps make water safe to drink.
- ✅ Cement is made by chemical industries.
- ✅ Burning plastic in the open pollutes the air.
- ❌ Soap is made without any chemistry.  
  _↳ Soap is made by a chemical reaction between fats or oils and an alkali._
- ❌ Chemicals can never harm people.  
  _↳ Some chemicals are poisonous or polluting when misused._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Chlorine helps make water safe to drink.
- ✅ Chemicals can never harm people.  
  _↳ explanation: Some chemicals are poisonous or polluting when misused._
- ◻️ Fertilisers help crops grow.
- ◻️ Cement is made by chemical industries.

Full working after a second miss:

> The wrong statement is “Chemicals can never harm people.”.  
> Some chemicals are poisonous or polluting when misused.  

> One sentence is wrong. Which one?

- ◻️ Fertilisers help crops grow.
- ◻️ Cement is made by chemical industries.
- ✅ Chemicals can never harm people.  
  _↳ explanation: Some chemicals are poisonous or polluting when misused._
- ◻️ Burning plastic in the open pollutes the air.

Full working after a second miss:

> The wrong statement is “Chemicals can never harm people.”.  
> Some chemicals are poisonous or polluting when misused.  

> One sentence is wrong. Which one?

- ◻️ Burning plastic in the open pollutes the air.
- ◻️ Fertilisers help crops grow.
- ✅ Chemicals can never harm people.  
  _↳ explanation: Some chemicals are poisonous or polluting when misused._
- ◻️ Cement is made by chemical industries.

Full working after a second miss:

> The wrong statement is “Chemicals can never harm people.”.  
> Some chemicals are poisonous or polluting when misused.  

Sources: chemistry-life (Uses of chemistry in daily life (health, farming, cleaning, water, building, fuels, food))

### `chc2-3-check` · Lesson 2 · multiple choice, level 1

Prompt: Which is a harmful use of chemicals?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Pouring used engine oil into a stream.
- ❌ Washing hands with soap.  
  _↳ Soap removes dirt and germs: a good use._
- ❌ Putting chlorine in drinking water.  
  _↳ Chlorine kills germs in water: a good use._
- ❌ Using fertiliser on a maize farm.  
  _↳ Used correctly, fertiliser helps crops grow._


Three generated variants:

> Which is a harmful use of chemicals?

- ◻️ Using fertiliser on a maize farm.  
  _↳ feedback if chosen: Used correctly, fertiliser helps crops grow._
- ◻️ Putting chlorine in drinking water.  
  _↳ feedback if chosen: Chlorine kills germs in water: a good use._
- ✅ Pouring used engine oil into a stream.
- ◻️ Washing hands with soap.  
  _↳ feedback if chosen: Soap removes dirt and germs: a good use._

Full working after a second miss:

> The true statement is “Pouring used engine oil into a stream.”.  
> “Using fertiliser on a maize farm.” is false: Used correctly, fertiliser helps crops grow.  
> “Putting chlorine in drinking water.” is false: Chlorine kills germs in water: a good use.  
> “Washing hands with soap.” is false: Soap removes dirt and germs: a good use.  

> Which is a harmful use of chemicals?

- ✅ Pouring used engine oil into a stream.
- ◻️ Using fertiliser on a maize farm.  
  _↳ feedback if chosen: Used correctly, fertiliser helps crops grow._
- ◻️ Washing hands with soap.  
  _↳ feedback if chosen: Soap removes dirt and germs: a good use._
- ◻️ Putting chlorine in drinking water.  
  _↳ feedback if chosen: Chlorine kills germs in water: a good use._

Full working after a second miss:

> The true statement is “Pouring used engine oil into a stream.”.  
> “Using fertiliser on a maize farm.” is false: Used correctly, fertiliser helps crops grow.  
> “Washing hands with soap.” is false: Soap removes dirt and germs: a good use.  
> “Putting chlorine in drinking water.” is false: Chlorine kills germs in water: a good use.  

> Which is a harmful use of chemicals?

- ◻️ Washing hands with soap.  
  _↳ feedback if chosen: Soap removes dirt and germs: a good use._
- ◻️ Putting chlorine in drinking water.  
  _↳ feedback if chosen: Chlorine kills germs in water: a good use._
- ✅ Pouring used engine oil into a stream.
- ◻️ Using fertiliser on a maize farm.  
  _↳ feedback if chosen: Used correctly, fertiliser helps crops grow._

Full working after a second miss:

> The true statement is “Pouring used engine oil into a stream.”.  
> “Washing hands with soap.” is false: Soap removes dirt and germs: a good use.  
> “Putting chlorine in drinking water.” is false: Chlorine kills germs in water: a good use.  
> “Using fertiliser on a maize farm.” is false: Used correctly, fertiliser helps crops grow.  

Sources: chemistry-life (Uses of chemistry in daily life (health, farming, cleaning, water, building, fuels, food))

### `ch3-match` · Lesson 3 · matching, level 1

Prompt: Match each piece of equipment with its job.

Pairs (4 shown each time):

- test tube → **holds small amounts of substances for reactions**
- beaker → **holds and heats liquids**
- conical flask → **holds liquids that are swirled or titrated**
- measuring cylinder → **measures the volume of a liquid**
- burette → **lets out an exact volume of liquid, drop by drop**
- pipette → **transfers an exact, fixed volume of liquid**
- dropper → **adds a liquid a few drops at a time**
- gas jar → **collects a gas**
- watch glass → **holds a small amount of a solid or evaporates a few drops**


Three generated variants:

> Match each piece of equipment with its job.

Right-hand side (shuffled): transfers an exact, fixed volume of liquid · holds small amounts of substances for reactions · lets out an exact volume of liquid, drop by drop · measures the volume of a liquid
- measuring cylinder → **measures the volume of a liquid**
- test tube → **holds small amounts of substances for reactions**
- burette → **lets out an exact volume of liquid, drop by drop**
- pipette → **transfers an exact, fixed volume of liquid**

Full working after a second miss:

> The right pairs are:  
> measuring cylinder → measures the volume of a liquid  
> test tube → holds small amounts of substances for reactions  
> burette → lets out an exact volume of liquid, drop by drop  
> pipette → transfers an exact, fixed volume of liquid  

> Match each piece of equipment with its job.

Right-hand side (shuffled): holds a small amount of a solid or evaporates a few drops · holds small amounts of substances for reactions · measures the volume of a liquid · holds and heats liquids
- measuring cylinder → **measures the volume of a liquid**
- test tube → **holds small amounts of substances for reactions**
- watch glass → **holds a small amount of a solid or evaporates a few drops**
- beaker → **holds and heats liquids**

Full working after a second miss:

> The right pairs are:  
> measuring cylinder → measures the volume of a liquid  
> test tube → holds small amounts of substances for reactions  
> watch glass → holds a small amount of a solid or evaporates a few drops  
> beaker → holds and heats liquids  

> Match each piece of equipment with its job.

Right-hand side (shuffled): collects a gas · holds small amounts of substances for reactions · holds liquids that are swirled or titrated · lets out an exact volume of liquid, drop by drop
- test tube → **holds small amounts of substances for reactions**
- gas jar → **collects a gas**
- conical flask → **holds liquids that are swirled or titrated**
- burette → **lets out an exact volume of liquid, drop by drop**

Full working after a second miss:

> The right pairs are:  
> test tube → holds small amounts of substances for reactions  
> gas jar → collects a gas  
> conical flask → holds liquids that are swirled or titrated  
> burette → lets out an exact volume of liquid, drop by drop  

Sources: equipment-chem (School chemistry laboratory apparatus and its uses)

### `ch3-choose` · Lesson 3 · multiple choice, level 1

Prompt: Which equipment would you use to {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| collect a gas | gas jar | To collect a gas, use a gas jar. |
| let out an exact volume drop by drop | burette | To let out an exact volume drop by drop, use a burette. |
| transfer exactly 25 cm³ of a solution | pipette | To transfer exactly 25 cm³ of a solution, use a pipette. |
| measure about 40 cm³ of water | measuring cylinder | To measure about 40 cm³ of water, use a measuring cylinder. |
| mix two solutions to see if they react | test tube | To mix two solutions to see if they react, use a test tube. |

Right answer: `{x.a}`; wrong choices: `test tube`, `beaker`, `conical flask`, `measuring cylinder`, `burette`, `pipette`, `dropper`, `gas jar`, `watch glass`

- Feedback `other`: “That equipment has a different job.”

Three generated variants:

> Which equipment would you use to transfer exactly 25 cm³ of a solution?

- ◻️ test tube  
  _↳ feedback if chosen: That equipment has a different job._
- ✅ pipette
- ◻️ conical flask  
  _↳ feedback if chosen: That equipment has a different job._
- ◻️ beaker  
  _↳ feedback if chosen: That equipment has a different job._

Full working after a second miss:

> To transfer exactly 25 cm³ of a solution, use a pipette.  
> Answer: pipette.  

> Which equipment would you use to measure about 40 cm³ of water?

- ◻️ test tube  
  _↳ feedback if chosen: That equipment has a different job._
- ◻️ conical flask  
  _↳ feedback if chosen: That equipment has a different job._
- ◻️ beaker  
  _↳ feedback if chosen: That equipment has a different job._
- ✅ measuring cylinder

Full working after a second miss:

> To measure about 40 cm³ of water, use a measuring cylinder.  
> Answer: measuring cylinder.  

> Which equipment would you use to measure about 40 cm³ of water?

- ◻️ conical flask  
  _↳ feedback if chosen: That equipment has a different job._
- ◻️ pipette  
  _↳ feedback if chosen: That equipment has a different job._
- ◻️ test tube  
  _↳ feedback if chosen: That equipment has a different job._
- ✅ measuring cylinder

Full working after a second miss:

> To measure about 40 cm³ of water, use a measuring cylinder.  
> Answer: measuring cylinder.  

Sources: equipment-chem (School chemistry laboratory apparatus and its uses)

### `ch3-sort` · Lesson 3 · matching, level 2

Prompt: Sort the equipment: does it measure a volume, or only hold substances?

Pairs (5 shown each time, sorted into groups):

- measuring cylinder → **measures a volume**
- burette → **measures a volume**
- pipette → **measures a volume**
- test tube → **holds substances**
- gas jar → **holds substances**
- watch glass → **holds substances**
- conical flask → **holds substances**


Three generated variants:

> Sort the equipment: does it measure a volume, or only hold substances?

Groups: measures a volume · holds substances
- gas jar → **holds substances**
- measuring cylinder → **measures a volume**
- burette → **measures a volume**
- test tube → **holds substances**
- watch glass → **holds substances**

Full working after a second miss:

> The right pairs are:  
> gas jar → holds substances  
> measuring cylinder → measures a volume  
> burette → measures a volume  
> test tube → holds substances  
> watch glass → holds substances  

> Sort the equipment: does it measure a volume, or only hold substances?

Groups: measures a volume · holds substances
- watch glass → **holds substances**
- conical flask → **holds substances**
- test tube → **holds substances**
- gas jar → **holds substances**
- burette → **measures a volume**

Full working after a second miss:

> The right pairs are:  
> watch glass → holds substances  
> conical flask → holds substances  
> test tube → holds substances  
> gas jar → holds substances  
> burette → measures a volume  

> Sort the equipment: does it measure a volume, or only hold substances?

Groups: measures a volume · holds substances
- conical flask → **holds substances**
- burette → **measures a volume**
- measuring cylinder → **measures a volume**
- pipette → **measures a volume**
- gas jar → **holds substances**

Full working after a second miss:

> The right pairs are:  
> conical flask → holds substances  
> burette → measures a volume  
> measuring cylinder → measures a volume  
> pipette → measures a volume  
> gas jar → holds substances  

Sources: equipment-chem (School chemistry laboratory apparatus and its uses)

### `ch3-spot` · Lesson 3 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A gas jar is used to collect a gas.
- ✅ A burette lets out a liquid drop by drop.
- ✅ A pipette transfers an exact volume of liquid.
- ✅ A test tube holds small amounts for reactions.
- ❌ A measuring cylinder is used to heat liquids.  
  _↳ Never heat a measuring cylinder: use a beaker or a test tube._
- ❌ A dropper measures a large volume exactly.  
  _↳ A dropper adds a few drops; exact volumes need a pipette or burette._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ A measuring cylinder is used to heat liquids.  
  _↳ explanation: Never heat a measuring cylinder: use a beaker or a test tube._
- ◻️ A gas jar is used to collect a gas.
- ◻️ A pipette transfers an exact volume of liquid.
- ◻️ A burette lets out a liquid drop by drop.

Full working after a second miss:

> The wrong statement is “A measuring cylinder is used to heat liquids.”.  
> Never heat a measuring cylinder: use a beaker or a test tube.  

> One sentence is wrong. Which one?

- ◻️ A burette lets out a liquid drop by drop.
- ◻️ A gas jar is used to collect a gas.
- ✅ A measuring cylinder is used to heat liquids.  
  _↳ explanation: Never heat a measuring cylinder: use a beaker or a test tube._
- ◻️ A pipette transfers an exact volume of liquid.

Full working after a second miss:

> The wrong statement is “A measuring cylinder is used to heat liquids.”.  
> Never heat a measuring cylinder: use a beaker or a test tube.  

> One sentence is wrong. Which one?

- ◻️ A burette lets out a liquid drop by drop.
- ◻️ A test tube holds small amounts for reactions.
- ◻️ A gas jar is used to collect a gas.
- ✅ A measuring cylinder is used to heat liquids.  
  _↳ explanation: Never heat a measuring cylinder: use a beaker or a test tube._

Full working after a second miss:

> The wrong statement is “A measuring cylinder is used to heat liquids.”.  
> Never heat a measuring cylinder: use a beaker or a test tube.  

Sources: equipment-chem (School chemistry laboratory apparatus and its uses)

### `chc3-3-check` · Lesson 3 · multiple choice, level 1

Prompt: Which of these should NOT be heated?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ a measuring cylinder
- ❌ a beaker  
  _↳ Beakers can be heated, on a tripod and gauze._
- ❌ a test tube  
  _↳ Test tubes can be heated, held with a test-tube holder._
- ❌ an evaporating dish  
  _↳ Evaporating dishes are made to be heated._


Three generated variants:

> Which of these should NOT be heated?

- ◻️ a test tube  
  _↳ feedback if chosen: Test tubes can be heated, held with a test-tube holder._
- ◻️ an evaporating dish  
  _↳ feedback if chosen: Evaporating dishes are made to be heated._
- ◻️ a beaker  
  _↳ feedback if chosen: Beakers can be heated, on a tripod and gauze._
- ✅ a measuring cylinder

Full working after a second miss:

> The true statement is “a measuring cylinder”.  
> “a test tube” is false: Test tubes can be heated, held with a test-tube holder.  
> “an evaporating dish” is false: Evaporating dishes are made to be heated.  
> “a beaker” is false: Beakers can be heated, on a tripod and gauze.  

> Which of these should NOT be heated?

- ◻️ a beaker  
  _↳ feedback if chosen: Beakers can be heated, on a tripod and gauze._
- ◻️ a test tube  
  _↳ feedback if chosen: Test tubes can be heated, held with a test-tube holder._
- ✅ a measuring cylinder
- ◻️ an evaporating dish  
  _↳ feedback if chosen: Evaporating dishes are made to be heated._

Full working after a second miss:

> The true statement is “a measuring cylinder”.  
> “a beaker” is false: Beakers can be heated, on a tripod and gauze.  
> “a test tube” is false: Test tubes can be heated, held with a test-tube holder.  
> “an evaporating dish” is false: Evaporating dishes are made to be heated.  

> Which of these should NOT be heated?

- ◻️ a test tube  
  _↳ feedback if chosen: Test tubes can be heated, held with a test-tube holder._
- ✅ a measuring cylinder
- ◻️ a beaker  
  _↳ feedback if chosen: Beakers can be heated, on a tripod and gauze._
- ◻️ an evaporating dish  
  _↳ feedback if chosen: Evaporating dishes are made to be heated._

Full working after a second miss:

> The true statement is “a measuring cylinder”.  
> “a test tube” is false: Test tubes can be heated, held with a test-tube holder.  
> “a beaker” is false: Beakers can be heated, on a tripod and gauze.  
> “an evaporating dish” is false: Evaporating dishes are made to be heated.  

Sources: equipment-chem (School chemistry laboratory apparatus and its uses)

### `ch4-match` · Lesson 4 · matching, level 1

Prompt: Match each piece of equipment with its job.

Pairs (4 shown each time):

- Bunsen burner → **heats things with a gas flame**
- tripod stand → **holds a beaker or dish over a flame**
- wire gauze → **spreads the heat under a beaker**
- test-tube holder → **holds a hot test tube**
- test-tube rack → **holds test tubes upright**
- funnel and filter paper → **separates a solid from a liquid**
- evaporating dish → **holds a solution while the water evaporates**
- crucible and tongs → **heats a solid very strongly; tongs lift it**
- mortar and pestle → **grinds solids into powder**
- spatula → **picks up small amounts of a powder**
- retort stand and clamp → **holds apparatus in place**


Three generated variants:

> Match each piece of equipment with its job.

Right-hand side (shuffled): holds a beaker or dish over a flame · heats things with a gas flame · grinds solids into powder · holds a hot test tube
- test-tube holder → **holds a hot test tube**
- Bunsen burner → **heats things with a gas flame**
- mortar and pestle → **grinds solids into powder**
- tripod stand → **holds a beaker or dish over a flame**

Full working after a second miss:

> The right pairs are:  
> test-tube holder → holds a hot test tube  
> Bunsen burner → heats things with a gas flame  
> mortar and pestle → grinds solids into powder  
> tripod stand → holds a beaker or dish over a flame  

> Match each piece of equipment with its job.

Right-hand side (shuffled): holds a solution while the water evaporates · picks up small amounts of a powder · holds a beaker or dish over a flame · heats a solid very strongly; tongs lift it
- crucible and tongs → **heats a solid very strongly; tongs lift it**
- evaporating dish → **holds a solution while the water evaporates**
- spatula → **picks up small amounts of a powder**
- tripod stand → **holds a beaker or dish over a flame**

Full working after a second miss:

> The right pairs are:  
> crucible and tongs → heats a solid very strongly; tongs lift it  
> evaporating dish → holds a solution while the water evaporates  
> spatula → picks up small amounts of a powder  
> tripod stand → holds a beaker or dish over a flame  

> Match each piece of equipment with its job.

Right-hand side (shuffled): heats a solid very strongly; tongs lift it · separates a solid from a liquid · holds apparatus in place · holds a solution while the water evaporates
- evaporating dish → **holds a solution while the water evaporates**
- crucible and tongs → **heats a solid very strongly; tongs lift it**
- retort stand and clamp → **holds apparatus in place**
- funnel and filter paper → **separates a solid from a liquid**

Full working after a second miss:

> The right pairs are:  
> evaporating dish → holds a solution while the water evaporates  
> crucible and tongs → heats a solid very strongly; tongs lift it  
> retort stand and clamp → holds apparatus in place  
> funnel and filter paper → separates a solid from a liquid  

Sources: equipment-chem (School chemistry laboratory apparatus and its uses)

### `ch4-choose` · Lesson 4 · multiple choice, level 1

Prompt: Which equipment would you use to {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| hold a hot test tube | test-tube holder | To hold a hot test tube, use a test-tube holder. |
| grind crystals into powder | mortar and pestle | To grind crystals into powder, use a mortar and pestle. |
| spread the heat under a beaker | wire gauze | To spread the heat under a beaker, use a wire gauze. |
| heat a solid very strongly | crucible and tongs | To heat a solid very strongly, use a crucible and tongs. |
| hold a thermometer in place over a beaker | retort stand and clamp | To hold a thermometer in place over a beaker, use a retort stand and clamp. |

Right answer: `{x.a}`; wrong choices: `Bunsen burner`, `tripod stand`, `wire gauze`, `test-tube holder`, `test-tube rack`, `funnel and filter paper`, `evaporating dish`, `crucible and tongs`, `mortar and pestle`, `spatula`, `retort stand and clamp`

- Feedback `other`: “That equipment has a different job.”

Three generated variants:

> Which equipment would you use to hold a thermometer in place over a beaker?

- ◻️ wire gauze  
  _↳ feedback if chosen: That equipment has a different job._
- ◻️ funnel and filter paper  
  _↳ feedback if chosen: That equipment has a different job._
- ✅ retort stand and clamp
- ◻️ crucible and tongs  
  _↳ feedback if chosen: That equipment has a different job._

Full working after a second miss:

> To hold a thermometer in place over a beaker, use a retort stand and clamp.  
> Answer: retort stand and clamp.  

> Which equipment would you use to spread the heat under a beaker?

- ◻️ mortar and pestle  
  _↳ feedback if chosen: That equipment has a different job._
- ✅ wire gauze
- ◻️ retort stand and clamp  
  _↳ feedback if chosen: That equipment has a different job._
- ◻️ test-tube rack  
  _↳ feedback if chosen: That equipment has a different job._

Full working after a second miss:

> To spread the heat under a beaker, use a wire gauze.  
> Answer: wire gauze.  

> Which equipment would you use to spread the heat under a beaker?

- ◻️ evaporating dish  
  _↳ feedback if chosen: That equipment has a different job._
- ◻️ funnel and filter paper  
  _↳ feedback if chosen: That equipment has a different job._
- ◻️ retort stand and clamp  
  _↳ feedback if chosen: That equipment has a different job._
- ✅ wire gauze

Full working after a second miss:

> To spread the heat under a beaker, use a wire gauze.  
> Answer: wire gauze.  

Sources: equipment-chem (School chemistry laboratory apparatus and its uses)

### `ch4-sort` · Lesson 4 · matching, level 2

Prompt: Sort the equipment by its main job.

Pairs (6 shown each time, sorted into groups):

- Bunsen burner → **heating**
- crucible → **heating**
- test-tube holder → **holding**
- retort stand and clamp → **holding**
- test-tube rack → **holding**
- funnel and filter paper → **separating or preparing**
- evaporating dish → **separating or preparing**
- mortar and pestle → **separating or preparing**


Three generated variants:

> Sort the equipment by its main job.

Groups: heating · holding · separating or preparing
- funnel and filter paper → **separating or preparing**
- evaporating dish → **separating or preparing**
- retort stand and clamp → **holding**
- mortar and pestle → **separating or preparing**
- Bunsen burner → **heating**
- crucible → **heating**

Full working after a second miss:

> The right pairs are:  
> funnel and filter paper → separating or preparing  
> evaporating dish → separating or preparing  
> retort stand and clamp → holding  
> mortar and pestle → separating or preparing  
> Bunsen burner → heating  
> crucible → heating  

> Sort the equipment by its main job.

Groups: heating · holding · separating or preparing
- mortar and pestle → **separating or preparing**
- evaporating dish → **separating or preparing**
- test-tube rack → **holding**
- retort stand and clamp → **holding**
- crucible → **heating**
- funnel and filter paper → **separating or preparing**

Full working after a second miss:

> The right pairs are:  
> mortar and pestle → separating or preparing  
> evaporating dish → separating or preparing  
> test-tube rack → holding  
> retort stand and clamp → holding  
> crucible → heating  
> funnel and filter paper → separating or preparing  

> Sort the equipment by its main job.

Groups: heating · holding · separating or preparing
- funnel and filter paper → **separating or preparing**
- Bunsen burner → **heating**
- test-tube holder → **holding**
- evaporating dish → **separating or preparing**
- crucible → **heating**
- test-tube rack → **holding**

Full working after a second miss:

> The right pairs are:  
> funnel and filter paper → separating or preparing  
> Bunsen burner → heating  
> test-tube holder → holding  
> evaporating dish → separating or preparing  
> crucible → heating  
> test-tube rack → holding  

Sources: equipment-chem (School chemistry laboratory apparatus and its uses)

### `ch4-spot` · Lesson 4 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A wire gauze spreads the heat under a beaker.
- ✅ Tongs are used to lift a hot crucible.
- ✅ A test-tube holder holds a hot test tube.
- ✅ A mortar and pestle grinds solids.
- ❌ A yellow Bunsen flame is the hottest.  
  _↳ The blue flame is hotter; the yellow flame is cooler and sooty._
- ❌ A spatula is used to heat liquids.  
  _↳ A spatula picks up small amounts of a powder._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ A test-tube holder holds a hot test tube.
- ◻️ A wire gauze spreads the heat under a beaker.
- ◻️ A mortar and pestle grinds solids.
- ✅ A yellow Bunsen flame is the hottest.  
  _↳ explanation: The blue flame is hotter; the yellow flame is cooler and sooty._

Full working after a second miss:

> The wrong statement is “A yellow Bunsen flame is the hottest.”.  
> The blue flame is hotter; the yellow flame is cooler and sooty.  

> One sentence is wrong. Which one?

- ◻️ A test-tube holder holds a hot test tube.
- ✅ A spatula is used to heat liquids.  
  _↳ explanation: A spatula picks up small amounts of a powder._
- ◻️ Tongs are used to lift a hot crucible.
- ◻️ A wire gauze spreads the heat under a beaker.

Full working after a second miss:

> The wrong statement is “A spatula is used to heat liquids.”.  
> A spatula picks up small amounts of a powder.  

> One sentence is wrong. Which one?

- ◻️ A test-tube holder holds a hot test tube.
- ◻️ A wire gauze spreads the heat under a beaker.
- ✅ A yellow Bunsen flame is the hottest.  
  _↳ explanation: The blue flame is hotter; the yellow flame is cooler and sooty._
- ◻️ Tongs are used to lift a hot crucible.

Full working after a second miss:

> The wrong statement is “A yellow Bunsen flame is the hottest.”.  
> The blue flame is hotter; the yellow flame is cooler and sooty.  

Sources: equipment-chem (School chemistry laboratory apparatus and its uses)

### `chc4-3-check` · Lesson 4 · multiple choice, level 1

Prompt: Which equipment separates sand from water?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ funnel and filter paper
- ❌ Bunsen burner  
  _↳ A Bunsen burner heats things._
- ❌ mortar and pestle  
  _↳ A mortar and pestle grinds solids._
- ❌ test-tube rack  
  _↳ A rack holds test tubes upright._


Three generated variants:

> Which equipment separates sand from water?

- ◻️ mortar and pestle  
  _↳ feedback if chosen: A mortar and pestle grinds solids._
- ✅ funnel and filter paper
- ◻️ test-tube rack  
  _↳ feedback if chosen: A rack holds test tubes upright._
- ◻️ Bunsen burner  
  _↳ feedback if chosen: A Bunsen burner heats things._

Full working after a second miss:

> The true statement is “funnel and filter paper”.  
> “mortar and pestle” is false: A mortar and pestle grinds solids.  
> “test-tube rack” is false: A rack holds test tubes upright.  
> “Bunsen burner” is false: A Bunsen burner heats things.  

> Which equipment separates sand from water?

- ◻️ mortar and pestle  
  _↳ feedback if chosen: A mortar and pestle grinds solids._
- ◻️ Bunsen burner  
  _↳ feedback if chosen: A Bunsen burner heats things._
- ◻️ test-tube rack  
  _↳ feedback if chosen: A rack holds test tubes upright._
- ✅ funnel and filter paper

Full working after a second miss:

> The true statement is “funnel and filter paper”.  
> “mortar and pestle” is false: A mortar and pestle grinds solids.  
> “Bunsen burner” is false: A Bunsen burner heats things.  
> “test-tube rack” is false: A rack holds test tubes upright.  

> Which equipment separates sand from water?

- ◻️ mortar and pestle  
  _↳ feedback if chosen: A mortar and pestle grinds solids._
- ◻️ test-tube rack  
  _↳ feedback if chosen: A rack holds test tubes upright._
- ◻️ Bunsen burner  
  _↳ feedback if chosen: A Bunsen burner heats things._
- ✅ funnel and filter paper

Full working after a second miss:

> The true statement is “funnel and filter paper”.  
> “mortar and pestle” is false: A mortar and pestle grinds solids.  
> “test-tube rack” is false: A rack holds test tubes upright.  
> “Bunsen burner” is false: A Bunsen burner heats things.  

Sources: equipment-chem (School chemistry laboratory apparatus and its uses)

### `ch5-match` · Lesson 5 · matching, level 1

Prompt: Match each hazard symbol (described in words) with its meaning.

Pairs (4 shown each time):

- a flame → **flammable: catches fire easily**
- a skull and crossbones → **toxic: poisonous**
- liquid dripping onto a hand and a metal bar → **corrosive: destroys skin and metal**
- a flame over a circle → **oxidising: makes other things burn more fiercely**
- an exclamation mark → **harmful or irritant**
- an exploding bomb → **explosive**
- a dead tree and a dead fish → **dangerous for the environment**


Three generated variants:

> Match each hazard symbol (described in words) with its meaning.

Right-hand side (shuffled): explosive · corrosive: destroys skin and metal · flammable: catches fire easily · toxic: poisonous
- a skull and crossbones → **toxic: poisonous**
- a flame → **flammable: catches fire easily**
- liquid dripping onto a hand and a metal bar → **corrosive: destroys skin and metal**
- an exploding bomb → **explosive**

Full working after a second miss:

> The right pairs are:  
> a skull and crossbones → toxic: poisonous  
> a flame → flammable: catches fire easily  
> liquid dripping onto a hand and a metal bar → corrosive: destroys skin and metal  
> an exploding bomb → explosive  

> Match each hazard symbol (described in words) with its meaning.

Right-hand side (shuffled): dangerous for the environment · oxidising: makes other things burn more fiercely · flammable: catches fire easily · explosive
- a dead tree and a dead fish → **dangerous for the environment**
- an exploding bomb → **explosive**
- a flame → **flammable: catches fire easily**
- a flame over a circle → **oxidising: makes other things burn more fiercely**

Full working after a second miss:

> The right pairs are:  
> a dead tree and a dead fish → dangerous for the environment  
> an exploding bomb → explosive  
> a flame → flammable: catches fire easily  
> a flame over a circle → oxidising: makes other things burn more fiercely  

> Match each hazard symbol (described in words) with its meaning.

Right-hand side (shuffled): toxic: poisonous · explosive · harmful or irritant · corrosive: destroys skin and metal
- a skull and crossbones → **toxic: poisonous**
- liquid dripping onto a hand and a metal bar → **corrosive: destroys skin and metal**
- an exploding bomb → **explosive**
- an exclamation mark → **harmful or irritant**

Full working after a second miss:

> The right pairs are:  
> a skull and crossbones → toxic: poisonous  
> liquid dripping onto a hand and a metal bar → corrosive: destroys skin and metal  
> an exploding bomb → explosive  
> an exclamation mark → harmful or irritant  

Sources: hazards-chem (Hazard pictograms (UN Globally Harmonized System), described in words; typical hazards of common reagents)

### `ch5-reagent` · Lesson 5 · multiple choice, level 1

Prompt: Which hazard symbol would you expect on a bottle of {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| concentrated sulfuric acid | corrosive: destroys skin and metal | A bottle of concentrated sulfuric acid carries the symbol for “corrosive: destroys skin and metal”. |
| sodium hydroxide | corrosive: destroys skin and metal | A bottle of sodium hydroxide carries the symbol for “corrosive: destroys skin and metal”. |
| ethanol (methylated spirit) | flammable: catches fire easily | A bottle of ethanol (methylated spirit) carries the symbol for “flammable: catches fire easily”. |
| kerosene | flammable: catches fire easily | A bottle of kerosene carries the symbol for “flammable: catches fire easily”. |
| mercury | toxic: poisonous | A bottle of mercury carries the symbol for “toxic: poisonous”. |
| potassium manganate(VII) (permanganate) | oxidising: makes other things burn more fiercely | A bottle of potassium manganate(VII) (permanganate) carries the symbol for “oxidising: makes other things burn more fiercely”. |

Right answer: `{x.a}`; wrong choices: `flammable: catches fire easily`, `toxic: poisonous`, `corrosive: destroys skin and metal`, `oxidising: makes other things burn more fiercely`, `harmful or irritant`, `explosive`, `dangerous for the environment`

- Feedback `other`: “That symbol warns of a different danger.”

Three generated variants:

> Which hazard symbol would you expect on a bottle of kerosene?

- ✅ flammable: catches fire easily
- ◻️ explosive  
  _↳ feedback if chosen: That symbol warns of a different danger._
- ◻️ oxidising: makes other things burn more fiercely  
  _↳ feedback if chosen: That symbol warns of a different danger._
- ◻️ toxic: poisonous  
  _↳ feedback if chosen: That symbol warns of a different danger._

Full working after a second miss:

> A bottle of kerosene carries the symbol for “flammable: catches fire easily”.  
> Answer: flammable: catches fire easily.  

> Which hazard symbol would you expect on a bottle of potassium manganate(VII) (permanganate)?

- ◻️ toxic: poisonous  
  _↳ feedback if chosen: That symbol warns of a different danger._
- ◻️ dangerous for the environment  
  _↳ feedback if chosen: That symbol warns of a different danger._
- ✅ oxidising: makes other things burn more fiercely
- ◻️ flammable: catches fire easily  
  _↳ feedback if chosen: That symbol warns of a different danger._

Full working after a second miss:

> A bottle of potassium manganate(VII) (permanganate) carries the symbol for “oxidising: makes other things burn more fiercely”.  
> Answer: oxidising: makes other things burn more fiercely.  

> Which hazard symbol would you expect on a bottle of kerosene?

- ◻️ harmful or irritant  
  _↳ feedback if chosen: That symbol warns of a different danger._
- ✅ flammable: catches fire easily
- ◻️ explosive  
  _↳ feedback if chosen: That symbol warns of a different danger._
- ◻️ oxidising: makes other things burn more fiercely  
  _↳ feedback if chosen: That symbol warns of a different danger._

Full working after a second miss:

> A bottle of kerosene carries the symbol for “flammable: catches fire easily”.  
> Answer: flammable: catches fire easily.  

Sources: hazards-chem (Hazard pictograms (UN Globally Harmonized System), described in words; typical hazards of common reagents)

### `ch5-act` · Lesson 5 · multiple choice, level 2

Prompt: {x.t} What should you do?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| The bottle shows a flame. | Keep it away from flames and sparks. | The bottle shows a flame. So: Keep it away from flames and sparks. |
| The bottle shows liquid dripping onto a hand. | Wear gloves and goggles, and wash off any splash with lots of water. | The bottle shows liquid dripping onto a hand. So: Wear gloves and goggles, and wash off any splash with lots of water. |
| The bottle shows a skull and crossbones. | Do not touch, taste or breathe it; use it only as the teacher says. | The bottle shows a skull and crossbones. So: Do not touch, taste or breathe it; use it only as the teacher says. |
| The bottle shows a dead tree and a dead fish. | Never pour it down the drain or onto the ground. | The bottle shows a dead tree and a dead fish. So: Never pour it down the drain or onto the ground. |

Right answer: `{x.a}`; wrong choices: `Keep it away from flames and sparks.`, `Wear gloves and goggles, and wash off any splash with lots of water.`, `Do not touch, taste or breathe it; use it only as the teacher says.`, `Never pour it down the drain or onto the ground.`

- Feedback `other`: “That advice is for a different symbol.”

Three generated variants:

> The bottle shows a dead tree and a dead fish. What should you do?

- ◻️ Keep it away from flames and sparks.  
  _↳ feedback if chosen: That advice is for a different symbol._
- ◻️ Wear gloves and goggles, and wash off any splash with lots of water.  
  _↳ feedback if chosen: That advice is for a different symbol._
- ◻️ Do not touch, taste or breathe it; use it only as the teacher says.  
  _↳ feedback if chosen: That advice is for a different symbol._
- ✅ Never pour it down the drain or onto the ground.

Full working after a second miss:

> The bottle shows a dead tree and a dead fish. So: Never pour it down the drain or onto the ground.  
> Answer: Never pour it down the drain or onto the ground..  

> The bottle shows a dead tree and a dead fish. What should you do?

- ◻️ Wear gloves and goggles, and wash off any splash with lots of water.  
  _↳ feedback if chosen: That advice is for a different symbol._
- ◻️ Do not touch, taste or breathe it; use it only as the teacher says.  
  _↳ feedback if chosen: That advice is for a different symbol._
- ✅ Never pour it down the drain or onto the ground.
- ◻️ Keep it away from flames and sparks.  
  _↳ feedback if chosen: That advice is for a different symbol._

Full working after a second miss:

> The bottle shows a dead tree and a dead fish. So: Never pour it down the drain or onto the ground.  
> Answer: Never pour it down the drain or onto the ground..  

> The bottle shows liquid dripping onto a hand. What should you do?

- ✅ Wear gloves and goggles, and wash off any splash with lots of water.
- ◻️ Keep it away from flames and sparks.  
  _↳ feedback if chosen: That advice is for a different symbol._
- ◻️ Do not touch, taste or breathe it; use it only as the teacher says.  
  _↳ feedback if chosen: That advice is for a different symbol._
- ◻️ Never pour it down the drain or onto the ground.  
  _↳ feedback if chosen: That advice is for a different symbol._

Full working after a second miss:

> The bottle shows liquid dripping onto a hand. So: Wear gloves and goggles, and wash off any splash with lots of water.  
> Answer: Wear gloves and goggles, and wash off any splash with lots of water..  

Sources: hazards-chem (Hazard pictograms (UN Globally Harmonized System), described in words; typical hazards of common reagents)

### `ch5-spot` · Lesson 5 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Concentrated sulfuric acid is corrosive.
- ✅ Ethanol is flammable.
- ✅ Mercury is toxic.
- ✅ A flame over a circle means oxidising.
- ❌ The skull and crossbones means flammable.  
  _↳ The skull and crossbones means toxic (poisonous). A flame means flammable._
- ❌ A corrosive liquid is safe on skin.  
  _↳ Corrosive substances destroy skin: wash any splash with lots of water and tell the teacher._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ A flame over a circle means oxidising.
- ✅ A corrosive liquid is safe on skin.  
  _↳ explanation: Corrosive substances destroy skin: wash any splash with lots of water and tell the teacher._
- ◻️ Concentrated sulfuric acid is corrosive.
- ◻️ Mercury is toxic.

Full working after a second miss:

> The wrong statement is “A corrosive liquid is safe on skin.”.  
> Corrosive substances destroy skin: wash any splash with lots of water and tell the teacher.  

> One sentence is wrong. Which one?

- ✅ The skull and crossbones means flammable.  
  _↳ explanation: The skull and crossbones means toxic (poisonous). A flame means flammable._
- ◻️ A flame over a circle means oxidising.
- ◻️ Ethanol is flammable.
- ◻️ Mercury is toxic.

Full working after a second miss:

> The wrong statement is “The skull and crossbones means flammable.”.  
> The skull and crossbones means toxic (poisonous). A flame means flammable.  

> One sentence is wrong. Which one?

- ◻️ Concentrated sulfuric acid is corrosive.
- ◻️ Mercury is toxic.
- ◻️ Ethanol is flammable.
- ✅ A corrosive liquid is safe on skin.  
  _↳ explanation: Corrosive substances destroy skin: wash any splash with lots of water and tell the teacher._

Full working after a second miss:

> The wrong statement is “A corrosive liquid is safe on skin.”.  
> Corrosive substances destroy skin: wash any splash with lots of water and tell the teacher.  

Sources: hazards-chem (Hazard pictograms (UN Globally Harmonized System), described in words; typical hazards of common reagents)

### `chc5-3-check` · Lesson 5 · multiple choice, level 1

Prompt: What should you do before opening a reagent bottle?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Read the label and the hazard symbols.
- ❌ Smell it to find out what it is.  
  _↳ Never smell chemicals directly: some give off harmful gases._
- ❌ Taste a little.  
  _↳ Never taste anything in a laboratory._
- ❌ Shake it hard.  
  _↳ Shaking can spill or splash: read the label first._


Three generated variants:

> What should you do before opening a reagent bottle?

- ◻️ Shake it hard.  
  _↳ feedback if chosen: Shaking can spill or splash: read the label first._
- ✅ Read the label and the hazard symbols.
- ◻️ Smell it to find out what it is.  
  _↳ feedback if chosen: Never smell chemicals directly: some give off harmful gases._
- ◻️ Taste a little.  
  _↳ feedback if chosen: Never taste anything in a laboratory._

Full working after a second miss:

> The true statement is “Read the label and the hazard symbols.”.  
> “Shake it hard.” is false: Shaking can spill or splash: read the label first.  
> “Smell it to find out what it is.” is false: Never smell chemicals directly: some give off harmful gases.  
> “Taste a little.” is false: Never taste anything in a laboratory.  

> What should you do before opening a reagent bottle?

- ◻️ Shake it hard.  
  _↳ feedback if chosen: Shaking can spill or splash: read the label first._
- ◻️ Smell it to find out what it is.  
  _↳ feedback if chosen: Never smell chemicals directly: some give off harmful gases._
- ◻️ Taste a little.  
  _↳ feedback if chosen: Never taste anything in a laboratory._
- ✅ Read the label and the hazard symbols.

Full working after a second miss:

> The true statement is “Read the label and the hazard symbols.”.  
> “Shake it hard.” is false: Shaking can spill or splash: read the label first.  
> “Smell it to find out what it is.” is false: Never smell chemicals directly: some give off harmful gases.  
> “Taste a little.” is false: Never taste anything in a laboratory.  

> What should you do before opening a reagent bottle?

- ✅ Read the label and the hazard symbols.
- ◻️ Smell it to find out what it is.  
  _↳ feedback if chosen: Never smell chemicals directly: some give off harmful gases._
- ◻️ Shake it hard.  
  _↳ feedback if chosen: Shaking can spill or splash: read the label first._
- ◻️ Taste a little.  
  _↳ feedback if chosen: Never taste anything in a laboratory._

Full working after a second miss:

> The true statement is “Read the label and the hazard symbols.”.  
> “Smell it to find out what it is.” is false: Never smell chemicals directly: some give off harmful gases.  
> “Shake it hard.” is false: Shaking can spill or splash: read the label first.  
> “Taste a little.” is false: Never taste anything in a laboratory.  

Sources: hazards-chem (Hazard pictograms (UN Globally Harmonized System), described in words; typical hazards of common reagents)

### `ch6-sort` · Lesson 6 · matching, level 1

Prompt: Is each action safe or not safe in the chemistry laboratory?

Pairs (6 shown each time, sorted into groups):

- Wear safety goggles when heating or using acids. → **safe**
- Waft a smell towards your nose with your hand. → **safe**
- Add acid to water, slowly, not water to acid. → **safe**
- Point a heated test tube away from people. → **safe**
- Label every container you fill. → **safe**
- Wash your hands after the practical. → **safe**
- Taste a chemical to identify it. → **not safe**
- Smell a gas by putting your nose over the test tube. → **not safe**
- Pour unused chemicals back into the stock bottle. → **not safe**
- Eat your lunch at the laboratory bench. → **not safe**
- Heat a test tube pointing at your neighbour. → **not safe**
- Pour water into concentrated acid. → **not safe**


Three generated variants:

> Is each action safe or not safe in the chemistry laboratory?

Groups: safe · not safe
- Smell a gas by putting your nose over the test tube. → **not safe**
- Eat your lunch at the laboratory bench. → **not safe**
- Pour unused chemicals back into the stock bottle. → **not safe**
- Wash your hands after the practical. → **safe**
- Pour water into concentrated acid. → **not safe**
- Taste a chemical to identify it. → **not safe**

Full working after a second miss:

> The right pairs are:  
> Smell a gas by putting your nose over the test tube. → not safe  
> Eat your lunch at the laboratory bench. → not safe  
> Pour unused chemicals back into the stock bottle. → not safe  
> Wash your hands after the practical. → safe  
> Pour water into concentrated acid. → not safe  
> Taste a chemical to identify it. → not safe  

> Is each action safe or not safe in the chemistry laboratory?

Groups: safe · not safe
- Wear safety goggles when heating or using acids. → **safe**
- Pour unused chemicals back into the stock bottle. → **not safe**
- Point a heated test tube away from people. → **safe**
- Smell a gas by putting your nose over the test tube. → **not safe**
- Taste a chemical to identify it. → **not safe**
- Waft a smell towards your nose with your hand. → **safe**

Full working after a second miss:

> The right pairs are:  
> Wear safety goggles when heating or using acids. → safe  
> Pour unused chemicals back into the stock bottle. → not safe  
> Point a heated test tube away from people. → safe  
> Smell a gas by putting your nose over the test tube. → not safe  
> Taste a chemical to identify it. → not safe  
> Waft a smell towards your nose with your hand. → safe  

> Is each action safe or not safe in the chemistry laboratory?

Groups: safe · not safe
- Add acid to water, slowly, not water to acid. → **safe**
- Wash your hands after the practical. → **safe**
- Point a heated test tube away from people. → **safe**
- Pour water into concentrated acid. → **not safe**
- Wear safety goggles when heating or using acids. → **safe**
- Label every container you fill. → **safe**

Full working after a second miss:

> The right pairs are:  
> Add acid to water, slowly, not water to acid. → safe  
> Wash your hands after the practical. → safe  
> Point a heated test tube away from people. → safe  
> Pour water into concentrated acid. → not safe  
> Wear safety goggles when heating or using acids. → safe  
> Label every container you fill. → safe  

Sources: safety-chem (Chemistry laboratory safety rules (school practice))

### `ch6-what` · Lesson 6 · multiple choice, level 1

Prompt: What should you do if {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| acid splashes on your hand | Wash it with plenty of running water and tell the teacher. | If acid splashes on your hand: Wash it with plenty of running water and tell the teacher. |
| a chemical splashes into your eye | Rinse the eye with clean water for a long time and get help at once. | If a chemical splashes into your eye: Rinse the eye with clean water for a long time and get help at once. |
| you smell gas from the Bunsen burner tap | Turn off the gas, open windows and tell the teacher. | If you smell gas from the Bunsen burner tap: Turn off the gas, open windows and tell the teacher. |
| your classmate's test tube starts to spit while heating | Move away and tell your classmate to point it away and stop heating. | If your classmate's test tube starts to spit while heating: Move away and tell your classmate to point it away and stop heating. |

Right answer: `{x.a}`; wrong choices: `Wash it with plenty of running water and tell the teacher.`, `Rinse the eye with clean water for a long time and get help at once.`, `Turn off the gas, open windows and tell the teacher.`, `Move away and tell your classmate to point it away and stop heating.`

- Feedback `other`: “That is the right action for a different accident.”

Three generated variants:

> What should you do if your classmate's test tube starts to spit while heating?

- ◻️ Turn off the gas, open windows and tell the teacher.  
  _↳ feedback if chosen: That is the right action for a different accident._
- ◻️ Wash it with plenty of running water and tell the teacher.  
  _↳ feedback if chosen: That is the right action for a different accident._
- ◻️ Rinse the eye with clean water for a long time and get help at once.  
  _↳ feedback if chosen: That is the right action for a different accident._
- ✅ Move away and tell your classmate to point it away and stop heating.

Full working after a second miss:

> If your classmate's test tube starts to spit while heating: Move away and tell your classmate to point it away and stop heating.  
> Answer: Move away and tell your classmate to point it away and stop heating..  

> What should you do if acid splashes on your hand?

- ◻️ Move away and tell your classmate to point it away and stop heating.  
  _↳ feedback if chosen: That is the right action for a different accident._
- ◻️ Rinse the eye with clean water for a long time and get help at once.  
  _↳ feedback if chosen: That is the right action for a different accident._
- ✅ Wash it with plenty of running water and tell the teacher.
- ◻️ Turn off the gas, open windows and tell the teacher.  
  _↳ feedback if chosen: That is the right action for a different accident._

Full working after a second miss:

> If acid splashes on your hand: Wash it with plenty of running water and tell the teacher.  
> Answer: Wash it with plenty of running water and tell the teacher..  

> What should you do if a chemical splashes into your eye?

- ◻️ Wash it with plenty of running water and tell the teacher.  
  _↳ feedback if chosen: That is the right action for a different accident._
- ◻️ Turn off the gas, open windows and tell the teacher.  
  _↳ feedback if chosen: That is the right action for a different accident._
- ✅ Rinse the eye with clean water for a long time and get help at once.
- ◻️ Move away and tell your classmate to point it away and stop heating.  
  _↳ feedback if chosen: That is the right action for a different accident._

Full working after a second miss:

> If a chemical splashes into your eye: Rinse the eye with clean water for a long time and get help at once.  
> Answer: Rinse the eye with clean water for a long time and get help at once..  

Sources: safety-chem (Chemistry laboratory safety rules (school practice))

### `ch6-why` · Lesson 6 · multiple choice, level 2

Prompt: Why must we never pour unused chemicals back into the stock bottle?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ It could spoil (contaminate) the whole bottle for everyone.
- ❌ Because it wastes time.  
  _↳ The danger is contaminating the whole stock bottle._
- ❌ Because the bottle is too small.  
  _↳ The real reason: the chemical may be dirty or mixed and spoil the stock._
- ❌ Because the teacher wants to count them.  
  _↳ The reason is safety and purity: it could contaminate the stock._


Three generated variants:

> Why must we never pour unused chemicals back into the stock bottle?

- ◻️ Because it wastes time.  
  _↳ feedback if chosen: The danger is contaminating the whole stock bottle._
- ◻️ Because the bottle is too small.  
  _↳ feedback if chosen: The real reason: the chemical may be dirty or mixed and spoil the stock._
- ✅ It could spoil (contaminate) the whole bottle for everyone.
- ◻️ Because the teacher wants to count them.  
  _↳ feedback if chosen: The reason is safety and purity: it could contaminate the stock._

Full working after a second miss:

> The true statement is “It could spoil (contaminate) the whole bottle for everyone.”.  
> “Because it wastes time.” is false: The danger is contaminating the whole stock bottle.  
> “Because the bottle is too small.” is false: The real reason: the chemical may be dirty or mixed and spoil the stock.  
> “Because the teacher wants to count them.” is false: The reason is safety and purity: it could contaminate the stock.  

> Why must we never pour unused chemicals back into the stock bottle?

- ◻️ Because it wastes time.  
  _↳ feedback if chosen: The danger is contaminating the whole stock bottle._
- ◻️ Because the teacher wants to count them.  
  _↳ feedback if chosen: The reason is safety and purity: it could contaminate the stock._
- ◻️ Because the bottle is too small.  
  _↳ feedback if chosen: The real reason: the chemical may be dirty or mixed and spoil the stock._
- ✅ It could spoil (contaminate) the whole bottle for everyone.

Full working after a second miss:

> The true statement is “It could spoil (contaminate) the whole bottle for everyone.”.  
> “Because it wastes time.” is false: The danger is contaminating the whole stock bottle.  
> “Because the teacher wants to count them.” is false: The reason is safety and purity: it could contaminate the stock.  
> “Because the bottle is too small.” is false: The real reason: the chemical may be dirty or mixed and spoil the stock.  

> Why must we never pour unused chemicals back into the stock bottle?

- ◻️ Because it wastes time.  
  _↳ feedback if chosen: The danger is contaminating the whole stock bottle._
- ◻️ Because the teacher wants to count them.  
  _↳ feedback if chosen: The reason is safety and purity: it could contaminate the stock._
- ◻️ Because the bottle is too small.  
  _↳ feedback if chosen: The real reason: the chemical may be dirty or mixed and spoil the stock._
- ✅ It could spoil (contaminate) the whole bottle for everyone.

Full working after a second miss:

> The true statement is “It could spoil (contaminate) the whole bottle for everyone.”.  
> “Because it wastes time.” is false: The danger is contaminating the whole stock bottle.  
> “Because the teacher wants to count them.” is false: The reason is safety and purity: it could contaminate the stock.  
> “Because the bottle is too small.” is false: The real reason: the chemical may be dirty or mixed and spoil the stock.  

Sources: safety-chem (Chemistry laboratory safety rules (school practice))

### `ch6-spot` · Lesson 6 · spot the error, level 3

Prompt: One rule is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Wear safety goggles when heating.
- ✅ Label every container you fill.
- ✅ Wash your hands after a practical.
- ✅ Waft a gas towards your nose to smell it.
- ❌ Add water to concentrated acid.  
  _↳ Always add acid to water, slowly._
- ❌ You may keep a chemical in an empty drink bottle if you label it.  
  _↳ Never use drink bottles: someone may drink from it._


Three generated variants:

> One rule is wrong. Which one?

- ◻️ Wear safety goggles when heating.
- ✅ You may keep a chemical in an empty drink bottle if you label it.  
  _↳ explanation: Never use drink bottles: someone may drink from it._
- ◻️ Label every container you fill.
- ◻️ Wash your hands after a practical.

Full working after a second miss:

> The wrong statement is “You may keep a chemical in an empty drink bottle if you label it.”.  
> Never use drink bottles: someone may drink from it.  

> One rule is wrong. Which one?

- ◻️ Waft a gas towards your nose to smell it.
- ◻️ Label every container you fill.
- ✅ You may keep a chemical in an empty drink bottle if you label it.  
  _↳ explanation: Never use drink bottles: someone may drink from it._
- ◻️ Wear safety goggles when heating.

Full working after a second miss:

> The wrong statement is “You may keep a chemical in an empty drink bottle if you label it.”.  
> Never use drink bottles: someone may drink from it.  

> One rule is wrong. Which one?

- ✅ You may keep a chemical in an empty drink bottle if you label it.  
  _↳ explanation: Never use drink bottles: someone may drink from it._
- ◻️ Label every container you fill.
- ◻️ Wear safety goggles when heating.
- ◻️ Waft a gas towards your nose to smell it.

Full working after a second miss:

> The wrong statement is “You may keep a chemical in an empty drink bottle if you label it.”.  
> Never use drink bottles: someone may drink from it.  

Sources: safety-chem (Chemistry laboratory safety rules (school practice))

### `chc6-2-check` · Lesson 6 · multiple choice, level 1

Prompt: How should you dilute an acid?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Add the acid slowly to the water.
- ❌ Add water quickly to the acid.  
  _↳ Water added to concentrated acid can make it boil and spit._
- ❌ Mix them in a drink bottle.  
  _↳ Never use drink bottles for chemicals._
- ❌ Heat the acid first.  
  _↳ Heating the acid makes it more dangerous._


Three generated variants:

> How should you dilute an acid?

- ◻️ Heat the acid first.  
  _↳ feedback if chosen: Heating the acid makes it more dangerous._
- ◻️ Add water quickly to the acid.  
  _↳ feedback if chosen: Water added to concentrated acid can make it boil and spit._
- ✅ Add the acid slowly to the water.
- ◻️ Mix them in a drink bottle.  
  _↳ feedback if chosen: Never use drink bottles for chemicals._

Full working after a second miss:

> The true statement is “Add the acid slowly to the water.”.  
> “Heat the acid first.” is false: Heating the acid makes it more dangerous.  
> “Add water quickly to the acid.” is false: Water added to concentrated acid can make it boil and spit.  
> “Mix them in a drink bottle.” is false: Never use drink bottles for chemicals.  

> How should you dilute an acid?

- ✅ Add the acid slowly to the water.
- ◻️ Heat the acid first.  
  _↳ feedback if chosen: Heating the acid makes it more dangerous._
- ◻️ Add water quickly to the acid.  
  _↳ feedback if chosen: Water added to concentrated acid can make it boil and spit._
- ◻️ Mix them in a drink bottle.  
  _↳ feedback if chosen: Never use drink bottles for chemicals._

Full working after a second miss:

> The true statement is “Add the acid slowly to the water.”.  
> “Heat the acid first.” is false: Heating the acid makes it more dangerous.  
> “Add water quickly to the acid.” is false: Water added to concentrated acid can make it boil and spit.  
> “Mix them in a drink bottle.” is false: Never use drink bottles for chemicals.  

> How should you dilute an acid?

- ◻️ Add water quickly to the acid.  
  _↳ feedback if chosen: Water added to concentrated acid can make it boil and spit._
- ◻️ Mix them in a drink bottle.  
  _↳ feedback if chosen: Never use drink bottles for chemicals._
- ✅ Add the acid slowly to the water.
- ◻️ Heat the acid first.  
  _↳ feedback if chosen: Heating the acid makes it more dangerous._

Full working after a second miss:

> The true statement is “Add the acid slowly to the water.”.  
> “Add water quickly to the acid.” is false: Water added to concentrated acid can make it boil and spit.  
> “Mix them in a drink bottle.” is false: Never use drink bottles for chemicals.  
> “Heat the acid first.” is false: Heating the acid makes it more dangerous.  

Sources: safety-chem (Chemistry laboratory safety rules (school practice))

### `ch8-spot` · Lesson 8 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ One minute is 60 seconds.
- ✅ A thermometer bulb should not touch the bottom of the beaker.
- ✅ 0 °C is 273 K.
- ✅ Time taken = finishing time − starting time.
- ❌ One minute is 100 seconds.  
  _↳ One minute is 60 seconds._
- ❌ Read the thermometer as soon as you put it in.  
  _↳ Wait until the reading stops changing._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ One minute is 60 seconds.
- ◻️ A thermometer bulb should not touch the bottom of the beaker.
- ✅ One minute is 100 seconds.  
  _↳ explanation: One minute is 60 seconds._
- ◻️ 0 °C is 273 K.

Full working after a second miss:

> The wrong statement is “One minute is 100 seconds.”.  
> One minute is 60 seconds.  

> One sentence is wrong. Which one?

- ✅ Read the thermometer as soon as you put it in.  
  _↳ explanation: Wait until the reading stops changing._
- ◻️ Time taken = finishing time − starting time.
- ◻️ A thermometer bulb should not touch the bottom of the beaker.
- ◻️ One minute is 60 seconds.

Full working after a second miss:

> The wrong statement is “Read the thermometer as soon as you put it in.”.  
> Wait until the reading stops changing.  

> One sentence is wrong. Which one?

- ◻️ A thermometer bulb should not touch the bottom of the beaker.
- ◻️ One minute is 60 seconds.
- ✅ One minute is 100 seconds.  
  _↳ explanation: One minute is 60 seconds._
- ◻️ Time taken = finishing time − starting time.

Full working after a second miss:

> The wrong statement is “One minute is 100 seconds.”.  
> One minute is 60 seconds.  

Sources: measure-chem (Measuring mass, volume, time and temperature; conversions computed by convertUnit())

### `ch9-sort` · Lesson 9 · matching, level 1

Prompt: Sort each change: physical or chemical?

Pairs (6 shown each time, sorted into groups):

- ice melting → **physical change**
- sugar dissolving in tea → **physical change**
- water boiling → **physical change**
- cutting paper → **physical change**
- breaking a glass → **physical change**
- palm oil turning solid in the cold → **physical change**
- grinding maize into flour → **physical change**
- firewood burning → **chemical change**
- an iron roof rusting → **chemical change**
- cooking an egg → **chemical change**
- palm wine turning sour → **chemical change**
- milk going sour → **chemical change**
- bread dough rising with yeast → **chemical change**
- a match burning → **chemical change**


Three generated variants:

> Sort each change: physical or chemical?

Groups: physical change · chemical change
- cutting paper → **physical change**
- milk going sour → **chemical change**
- palm oil turning solid in the cold → **physical change**
- breaking a glass → **physical change**
- water boiling → **physical change**
- an iron roof rusting → **chemical change**

Full working after a second miss:

> The right pairs are:  
> cutting paper → physical change  
> milk going sour → chemical change  
> palm oil turning solid in the cold → physical change  
> breaking a glass → physical change  
> water boiling → physical change  
> an iron roof rusting → chemical change  

> Sort each change: physical or chemical?

Groups: physical change · chemical change
- grinding maize into flour → **physical change**
- cooking an egg → **chemical change**
- ice melting → **physical change**
- sugar dissolving in tea → **physical change**
- water boiling → **physical change**
- palm wine turning sour → **chemical change**

Full working after a second miss:

> The right pairs are:  
> grinding maize into flour → physical change  
> cooking an egg → chemical change  
> ice melting → physical change  
> sugar dissolving in tea → physical change  
> water boiling → physical change  
> palm wine turning sour → chemical change  

> Sort each change: physical or chemical?

Groups: physical change · chemical change
- bread dough rising with yeast → **chemical change**
- milk going sour → **chemical change**
- breaking a glass → **physical change**
- sugar dissolving in tea → **physical change**
- water boiling → **physical change**
- an iron roof rusting → **chemical change**

Full working after a second miss:

> The right pairs are:  
> bread dough rising with yeast → chemical change  
> milk going sour → chemical change  
> breaking a glass → physical change  
> sugar dissolving in tea → physical change  
> water boiling → physical change  
> an iron roof rusting → chemical change  

Sources: changes (Physical and chemical changes; signs of a chemical change)

### `ch9-which` · Lesson 9 · multiple choice, level 1

Prompt: Which of these is a chemical change?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ firewood burning
- ✅ an iron roof rusting
- ✅ cooking an egg
- ✅ palm wine turning sour
- ✅ milk going sour
- ✅ bread dough rising with yeast
- ✅ a match burning
- ❌ ice melting  
  _↳ Ice melting makes no new substance: it is a physical change._
- ❌ sugar dissolving in tea  
  _↳ Sugar dissolving in tea makes no new substance: it is a physical change._
- ❌ water boiling  
  _↳ Water boiling makes no new substance: it is a physical change._
- ❌ cutting paper  
  _↳ Cutting paper makes no new substance: it is a physical change._
- ❌ breaking a glass  
  _↳ Breaking a glass makes no new substance: it is a physical change._
- ❌ palm oil turning solid in the cold  
  _↳ Palm oil turning solid in the cold makes no new substance: it is a physical change._
- ❌ grinding maize into flour  
  _↳ Grinding maize into flour makes no new substance: it is a physical change._


Three generated variants:

> Which of these is a chemical change?

- ✅ milk going sour
- ◻️ sugar dissolving in tea  
  _↳ feedback if chosen: Sugar dissolving in tea makes no new substance: it is a physical change._
- ◻️ grinding maize into flour  
  _↳ feedback if chosen: Grinding maize into flour makes no new substance: it is a physical change._
- ◻️ cutting paper  
  _↳ feedback if chosen: Cutting paper makes no new substance: it is a physical change._

Full working after a second miss:

> The true statement is “milk going sour”.  
> “sugar dissolving in tea” is false: Sugar dissolving in tea makes no new substance: it is a physical change.  
> “grinding maize into flour” is false: Grinding maize into flour makes no new substance: it is a physical change.  
> “cutting paper” is false: Cutting paper makes no new substance: it is a physical change.  

> Which of these is a chemical change?

- ◻️ water boiling  
  _↳ feedback if chosen: Water boiling makes no new substance: it is a physical change._
- ✅ palm wine turning sour
- ◻️ sugar dissolving in tea  
  _↳ feedback if chosen: Sugar dissolving in tea makes no new substance: it is a physical change._
- ◻️ ice melting  
  _↳ feedback if chosen: Ice melting makes no new substance: it is a physical change._

Full working after a second miss:

> The true statement is “palm wine turning sour”.  
> “water boiling” is false: Water boiling makes no new substance: it is a physical change.  
> “sugar dissolving in tea” is false: Sugar dissolving in tea makes no new substance: it is a physical change.  
> “ice melting” is false: Ice melting makes no new substance: it is a physical change.  

> Which of these is a chemical change?

- ◻️ breaking a glass  
  _↳ feedback if chosen: Breaking a glass makes no new substance: it is a physical change._
- ◻️ palm oil turning solid in the cold  
  _↳ feedback if chosen: Palm oil turning solid in the cold makes no new substance: it is a physical change._
- ✅ cooking an egg
- ◻️ sugar dissolving in tea  
  _↳ feedback if chosen: Sugar dissolving in tea makes no new substance: it is a physical change._

Full working after a second miss:

> The true statement is “cooking an egg”.  
> “breaking a glass” is false: Breaking a glass makes no new substance: it is a physical change.  
> “palm oil turning solid in the cold” is false: Palm oil turning solid in the cold makes no new substance: it is a physical change.  
> “sugar dissolving in tea” is false: Sugar dissolving in tea makes no new substance: it is a physical change.  

Sources: changes (Physical and chemical changes; signs of a chemical change)

### `ch9-sign` · Lesson 9 · multiple choice, level 1

Prompt: {x.t} Which sign of a chemical change is this?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Bubbles of gas appear when chalk is put in vinegar. | a gas is given off | Bubbles of gas appear when chalk is put in vinegar. The sign is: a gas is given off. |
| A shiny iron nail turns orange-brown. | the colour changes | A shiny iron nail turns orange-brown. The sign is: the colour changes. |
| Burning kerosene gives out heat and light. | heat or light is given out | Burning kerosene gives out heat and light. The sign is: heat or light is given out. |
| Two clear liquids are mixed and a cloudy white solid appears. | a new solid appears | Two clear liquids are mixed and a cloudy white solid appears. The sign is: a new solid appears. |

Right answer: `{x.a}`; wrong choices: `a gas is given off`, `the colour changes`, `heat or light is given out`, `a new solid appears`

- Feedback `other`: “Look again at what you can see happening.”

Three generated variants:

> Two clear liquids are mixed and a cloudy white solid appears. Which sign of a chemical change is this?

- ◻️ a gas is given off  
  _↳ feedback if chosen: Look again at what you can see happening._
- ◻️ the colour changes  
  _↳ feedback if chosen: Look again at what you can see happening._
- ◻️ heat or light is given out  
  _↳ feedback if chosen: Look again at what you can see happening._
- ✅ a new solid appears

Full working after a second miss:

> Two clear liquids are mixed and a cloudy white solid appears. The sign is: a new solid appears.  
> Answer: a new solid appears.  

> Burning kerosene gives out heat and light. Which sign of a chemical change is this?

- ◻️ the colour changes  
  _↳ feedback if chosen: Look again at what you can see happening._
- ◻️ a gas is given off  
  _↳ feedback if chosen: Look again at what you can see happening._
- ✅ heat or light is given out
- ◻️ a new solid appears  
  _↳ feedback if chosen: Look again at what you can see happening._

Full working after a second miss:

> Burning kerosene gives out heat and light. The sign is: heat or light is given out.  
> Answer: heat or light is given out.  

> Two clear liquids are mixed and a cloudy white solid appears. Which sign of a chemical change is this?

- ✅ a new solid appears
- ◻️ a gas is given off  
  _↳ feedback if chosen: Look again at what you can see happening._
- ◻️ heat or light is given out  
  _↳ feedback if chosen: Look again at what you can see happening._
- ◻️ the colour changes  
  _↳ feedback if chosen: Look again at what you can see happening._

Full working after a second miss:

> Two clear liquids are mixed and a cloudy white solid appears. The sign is: a new solid appears.  
> Answer: a new solid appears.  

Sources: changes (Physical and chemical changes; signs of a chemical change)

### `ch9-why` · Lesson 9 · multiple choice, level 2

Prompt: Water boils and gives bubbles. Why is boiling a physical change?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ The bubbles are steam, which is still water: no new substance is made.
- ❌ Because it needs heat.  
  _↳ Many chemical changes also need heat. What matters is whether a new substance forms._
- ❌ Because bubbles always mean a physical change.  
  _↳ Bubbles can come from chemical changes too (chalk in vinegar)._
- ❌ Because water is a liquid.  
  _↳ The state does not decide; ask whether a new substance forms._


Three generated variants:

> Water boils and gives bubbles. Why is boiling a physical change?

- ◻️ Because bubbles always mean a physical change.  
  _↳ feedback if chosen: Bubbles can come from chemical changes too (chalk in vinegar)._
- ◻️ Because it needs heat.  
  _↳ feedback if chosen: Many chemical changes also need heat. What matters is whether a new substance forms._
- ◻️ Because water is a liquid.  
  _↳ feedback if chosen: The state does not decide; ask whether a new substance forms._
- ✅ The bubbles are steam, which is still water: no new substance is made.

Full working after a second miss:

> The true statement is “The bubbles are steam, which is still water: no new substance is made.”.  
> “Because bubbles always mean a physical change.” is false: Bubbles can come from chemical changes too (chalk in vinegar).  
> “Because it needs heat.” is false: Many chemical changes also need heat. What matters is whether a new substance forms.  
> “Because water is a liquid.” is false: The state does not decide; ask whether a new substance forms.  

> Water boils and gives bubbles. Why is boiling a physical change?

- ◻️ Because bubbles always mean a physical change.  
  _↳ feedback if chosen: Bubbles can come from chemical changes too (chalk in vinegar)._
- ◻️ Because water is a liquid.  
  _↳ feedback if chosen: The state does not decide; ask whether a new substance forms._
- ◻️ Because it needs heat.  
  _↳ feedback if chosen: Many chemical changes also need heat. What matters is whether a new substance forms._
- ✅ The bubbles are steam, which is still water: no new substance is made.

Full working after a second miss:

> The true statement is “The bubbles are steam, which is still water: no new substance is made.”.  
> “Because bubbles always mean a physical change.” is false: Bubbles can come from chemical changes too (chalk in vinegar).  
> “Because water is a liquid.” is false: The state does not decide; ask whether a new substance forms.  
> “Because it needs heat.” is false: Many chemical changes also need heat. What matters is whether a new substance forms.  

> Water boils and gives bubbles. Why is boiling a physical change?

- ◻️ Because bubbles always mean a physical change.  
  _↳ feedback if chosen: Bubbles can come from chemical changes too (chalk in vinegar)._
- ✅ The bubbles are steam, which is still water: no new substance is made.
- ◻️ Because water is a liquid.  
  _↳ feedback if chosen: The state does not decide; ask whether a new substance forms._
- ◻️ Because it needs heat.  
  _↳ feedback if chosen: Many chemical changes also need heat. What matters is whether a new substance forms._

Full working after a second miss:

> The true statement is “The bubbles are steam, which is still water: no new substance is made.”.  
> “Because bubbles always mean a physical change.” is false: Bubbles can come from chemical changes too (chalk in vinegar).  
> “Because water is a liquid.” is false: The state does not decide; ask whether a new substance forms.  
> “Because it needs heat.” is false: Many chemical changes also need heat. What matters is whether a new substance forms.  

Sources: changes (Physical and chemical changes; signs of a chemical change)

### `ch9-spot` · Lesson 9 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Rusting is a chemical change.
- ✅ Dissolving sugar is a physical change.
- ✅ Burning firewood makes new substances.
- ✅ Melting ice can be reversed by freezing.
- ❌ Cooking an egg is a physical change.  
  _↳ Cooking makes new substances that do not change back: a chemical change._
- ❌ Grinding maize into flour is a chemical change.  
  _↳ Flour is still maize in small pieces: a physical change._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Burning firewood makes new substances.
- ◻️ Dissolving sugar is a physical change.
- ◻️ Rusting is a chemical change.
- ✅ Cooking an egg is a physical change.  
  _↳ explanation: Cooking makes new substances that do not change back: a chemical change._

Full working after a second miss:

> The wrong statement is “Cooking an egg is a physical change.”.  
> Cooking makes new substances that do not change back: a chemical change.  

> One sentence is wrong. Which one?

- ◻️ Burning firewood makes new substances.
- ◻️ Dissolving sugar is a physical change.
- ◻️ Melting ice can be reversed by freezing.
- ✅ Grinding maize into flour is a chemical change.  
  _↳ explanation: Flour is still maize in small pieces: a physical change._

Full working after a second miss:

> The wrong statement is “Grinding maize into flour is a chemical change.”.  
> Flour is still maize in small pieces: a physical change.  

> One sentence is wrong. Which one?

- ◻️ Burning firewood makes new substances.
- ◻️ Rusting is a chemical change.
- ✅ Cooking an egg is a physical change.  
  _↳ explanation: Cooking makes new substances that do not change back: a chemical change._
- ◻️ Melting ice can be reversed by freezing.

Full working after a second miss:

> The wrong statement is “Cooking an egg is a physical change.”.  
> Cooking makes new substances that do not change back: a chemical change.  

Sources: changes (Physical and chemical changes; signs of a chemical change)

### `ch10-state` · Lesson 10 · multiple choice, level 1

Prompt: Which state of matter {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| keeps its own shape | solid | A solid keeps its own shape. |
| takes the shape of its container but keeps its volume | liquid | A liquid takes the shape of its container but keeps its volume. |
| spreads to fill the whole container | gas | A gas spreads to fill the whole container. |

Right answer: `{x.a}`; wrong choices: `solid`, `liquid`, `gas`

- Feedback `other`: “Think: does it keep its shape? its volume?”

Three generated variants:

> Which state of matter takes the shape of its container but keeps its volume?

- ◻️ solid  
  _↳ feedback if chosen: Think: does it keep its shape? its volume?_
- ◻️ gas  
  _↳ feedback if chosen: Think: does it keep its shape? its volume?_
- ✅ liquid

Full working after a second miss:

> A liquid takes the shape of its container but keeps its volume.  
> Answer: liquid.  

> Which state of matter keeps its own shape?

- ✅ solid
- ◻️ liquid  
  _↳ feedback if chosen: Think: does it keep its shape? its volume?_
- ◻️ gas  
  _↳ feedback if chosen: Think: does it keep its shape? its volume?_

Full working after a second miss:

> A solid keeps its own shape.  
> Answer: solid.  

> Which state of matter takes the shape of its container but keeps its volume?

- ◻️ gas  
  _↳ feedback if chosen: Think: does it keep its shape? its volume?_
- ✅ liquid
- ◻️ solid  
  _↳ feedback if chosen: Think: does it keep its shape? its volume?_

Full working after a second miss:

> A liquid takes the shape of its container but keeps its volume.  
> Answer: liquid.  

Sources: states (States of matter, changes of state, fixed melting and boiling points)

### `ch10-example` · Lesson 10 · multiple choice, level 2

Prompt: {x.t} What change of state is this?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Iodine crystals warmed in a beaker give a purple gas, with no liquid. | sublimation | Iodine crystals warmed in a beaker give a purple gas, with no liquid. This is sublimation. |
| Candle wax becomes liquid near the flame. | melting | Candle wax becomes liquid near the flame. This is melting. |
| A mirror in the bathroom becomes covered with water drops. | condensation | A mirror in the bathroom becomes covered with water drops. This is condensation. |
| A puddle disappears in the afternoon sun. | evaporation | A puddle disappears in the afternoon sun. This is evaporation. |
| Hot lead poured into a mould becomes hard. | freezing | Hot lead poured into a mould becomes hard. This is freezing. |

Right answer: `{x.a}`; wrong choices: `melting`, `freezing`, `evaporation`, `condensation`, `sublimation`

- Feedback `other`: “Which state does it start in, and which does it end in?”

Three generated variants:

> A puddle disappears in the afternoon sun. What change of state is this?

- ◻️ freezing  
  _↳ feedback if chosen: Which state does it start in, and which does it end in?_
- ◻️ condensation  
  _↳ feedback if chosen: Which state does it start in, and which does it end in?_
- ✅ evaporation
- ◻️ sublimation  
  _↳ feedback if chosen: Which state does it start in, and which does it end in?_

Full working after a second miss:

> A puddle disappears in the afternoon sun. This is evaporation.  
> Answer: evaporation.  

> A puddle disappears in the afternoon sun. What change of state is this?

- ✅ evaporation
- ◻️ melting  
  _↳ feedback if chosen: Which state does it start in, and which does it end in?_
- ◻️ sublimation  
  _↳ feedback if chosen: Which state does it start in, and which does it end in?_
- ◻️ condensation  
  _↳ feedback if chosen: Which state does it start in, and which does it end in?_

Full working after a second miss:

> A puddle disappears in the afternoon sun. This is evaporation.  
> Answer: evaporation.  

> Candle wax becomes liquid near the flame. What change of state is this?

- ◻️ condensation  
  _↳ feedback if chosen: Which state does it start in, and which does it end in?_
- ◻️ sublimation  
  _↳ feedback if chosen: Which state does it start in, and which does it end in?_
- ✅ melting
- ◻️ freezing  
  _↳ feedback if chosen: Which state does it start in, and which does it end in?_

Full working after a second miss:

> Candle wax becomes liquid near the flame. This is melting.  
> Answer: melting.  

Sources: states (States of matter, changes of state, fixed melting and boiling points)

### `ch10-spot` · Lesson 10 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Melting is a physical change.
- ✅ Iodine can sublime.
- ✅ A pure substance has a fixed boiling point.
- ✅ Condensation turns a gas into a liquid.
- ❌ Salt water boils at exactly 100 °C.  
  _↳ Salt water is impure: it boils above 100 °C._
- ❌ Boiling makes a new substance.  
  _↳ Steam is still water: boiling is a physical change._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ Boiling makes a new substance.  
  _↳ explanation: Steam is still water: boiling is a physical change._
- ◻️ Iodine can sublime.
- ◻️ Condensation turns a gas into a liquid.
- ◻️ A pure substance has a fixed boiling point.

Full working after a second miss:

> The wrong statement is “Boiling makes a new substance.”.  
> Steam is still water: boiling is a physical change.  

> One sentence is wrong. Which one?

- ◻️ Iodine can sublime.
- ✅ Boiling makes a new substance.  
  _↳ explanation: Steam is still water: boiling is a physical change._
- ◻️ Melting is a physical change.
- ◻️ Condensation turns a gas into a liquid.

Full working after a second miss:

> The wrong statement is “Boiling makes a new substance.”.  
> Steam is still water: boiling is a physical change.  

> One sentence is wrong. Which one?

- ◻️ Melting is a physical change.
- ◻️ Condensation turns a gas into a liquid.
- ✅ Salt water boils at exactly 100 °C.  
  _↳ explanation: Salt water is impure: it boils above 100 °C._
- ◻️ Iodine can sublime.

Full working after a second miss:

> The wrong statement is “Salt water boils at exactly 100 °C.”.  
> Salt water is impure: it boils above 100 °C.  

Sources: states (States of matter, changes of state, fixed melting and boiling points)

### `chc10-3-check` · Lesson 10 · multiple choice, level 1

Prompt: How can we tell that a sample of water is pure?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ It boils at exactly 100 °C at normal pressure.
- ❌ It looks clear.  
  _↳ Salt water also looks clear._
- ❌ It has no smell.  
  _↳ Many impure liquids have no smell._
- ❌ It is cold.  
  _↳ Temperature does not show purity; the boiling point does._


Three generated variants:

> How can we tell that a sample of water is pure?

- ◻️ It has no smell.  
  _↳ feedback if chosen: Many impure liquids have no smell._
- ◻️ It is cold.  
  _↳ feedback if chosen: Temperature does not show purity; the boiling point does._
- ✅ It boils at exactly 100 °C at normal pressure.
- ◻️ It looks clear.  
  _↳ feedback if chosen: Salt water also looks clear._

Full working after a second miss:

> The true statement is “It boils at exactly 100 °C at normal pressure.”.  
> “It has no smell.” is false: Many impure liquids have no smell.  
> “It is cold.” is false: Temperature does not show purity; the boiling point does.  
> “It looks clear.” is false: Salt water also looks clear.  

> How can we tell that a sample of water is pure?

- ◻️ It has no smell.  
  _↳ feedback if chosen: Many impure liquids have no smell._
- ✅ It boils at exactly 100 °C at normal pressure.
- ◻️ It looks clear.  
  _↳ feedback if chosen: Salt water also looks clear._
- ◻️ It is cold.  
  _↳ feedback if chosen: Temperature does not show purity; the boiling point does._

Full working after a second miss:

> The true statement is “It boils at exactly 100 °C at normal pressure.”.  
> “It has no smell.” is false: Many impure liquids have no smell.  
> “It looks clear.” is false: Salt water also looks clear.  
> “It is cold.” is false: Temperature does not show purity; the boiling point does.  

> How can we tell that a sample of water is pure?

- ◻️ It is cold.  
  _↳ feedback if chosen: Temperature does not show purity; the boiling point does._
- ◻️ It looks clear.  
  _↳ feedback if chosen: Salt water also looks clear._
- ◻️ It has no smell.  
  _↳ feedback if chosen: Many impure liquids have no smell._
- ✅ It boils at exactly 100 °C at normal pressure.

Full working after a second miss:

> The true statement is “It boils at exactly 100 °C at normal pressure.”.  
> “It is cold.” is false: Temperature does not show purity; the boiling point does.  
> “It looks clear.” is false: Salt water also looks clear.  
> “It has no smell.” is false: Many impure liquids have no smell.  

Sources: states (States of matter, changes of state, fixed melting and boiling points)

### `ch11-move` · Lesson 11 · multiple choice, level 1

Prompt: In which state do the particles {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| vibrate in fixed places | solid | In a solid the particles vibrate in fixed places. |
| slide past each other | liquid | In a liquid the particles slide past each other. |
| move fast in all directions | gas | In a gas the particles move fast in all directions. |

Right answer: `{x.a}`; wrong choices: `solid`, `liquid`, `gas`

- Feedback `other`: “Think about how freely the particles can move.”

Three generated variants:

> In which state do the particles move fast in all directions?

- ◻️ solid  
  _↳ feedback if chosen: Think about how freely the particles can move._
- ✅ gas
- ◻️ liquid  
  _↳ feedback if chosen: Think about how freely the particles can move._

Full working after a second miss:

> In a gas the particles move fast in all directions.  
> Answer: gas.  

> In which state do the particles slide past each other?

- ◻️ gas  
  _↳ feedback if chosen: Think about how freely the particles can move._
- ✅ liquid
- ◻️ solid  
  _↳ feedback if chosen: Think about how freely the particles can move._

Full working after a second miss:

> In a liquid the particles slide past each other.  
> Answer: liquid.  

> In which state do the particles move fast in all directions?

- ◻️ solid  
  _↳ feedback if chosen: Think about how freely the particles can move._
- ◻️ liquid  
  _↳ feedback if chosen: Think about how freely the particles can move._
- ✅ gas

Full working after a second miss:

> In a gas the particles move fast in all directions.  
> Answer: gas.  

Sources: kinetic (Simple kinetic theory of matter; diffusion)

### `ch11-heat` · Lesson 11 · multiple choice, level 1

Prompt: What happens to the particles of a substance when it is heated?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ They gain energy and move faster.
- ❌ They get bigger.  
  _↳ The particles do not grow; they move faster._
- ❌ They stop moving.  
  _↳ Cooling slows them down; heating speeds them up._
- ❌ They change into new particles.  
  _↳ Heating alone does not make new particles in a change of state._


Three generated variants:

> What happens to the particles of a substance when it is heated?

- ◻️ They get bigger.  
  _↳ feedback if chosen: The particles do not grow; they move faster._
- ◻️ They stop moving.  
  _↳ feedback if chosen: Cooling slows them down; heating speeds them up._
- ✅ They gain energy and move faster.
- ◻️ They change into new particles.  
  _↳ feedback if chosen: Heating alone does not make new particles in a change of state._

Full working after a second miss:

> The true statement is “They gain energy and move faster.”.  
> “They get bigger.” is false: The particles do not grow; they move faster.  
> “They stop moving.” is false: Cooling slows them down; heating speeds them up.  
> “They change into new particles.” is false: Heating alone does not make new particles in a change of state.  

> What happens to the particles of a substance when it is heated?

- ◻️ They change into new particles.  
  _↳ feedback if chosen: Heating alone does not make new particles in a change of state._
- ◻️ They get bigger.  
  _↳ feedback if chosen: The particles do not grow; they move faster._
- ✅ They gain energy and move faster.
- ◻️ They stop moving.  
  _↳ feedback if chosen: Cooling slows them down; heating speeds them up._

Full working after a second miss:

> The true statement is “They gain energy and move faster.”.  
> “They change into new particles.” is false: Heating alone does not make new particles in a change of state.  
> “They get bigger.” is false: The particles do not grow; they move faster.  
> “They stop moving.” is false: Cooling slows them down; heating speeds them up.  

> What happens to the particles of a substance when it is heated?

- ◻️ They get bigger.  
  _↳ feedback if chosen: The particles do not grow; they move faster._
- ◻️ They change into new particles.  
  _↳ feedback if chosen: Heating alone does not make new particles in a change of state._
- ◻️ They stop moving.  
  _↳ feedback if chosen: Cooling slows them down; heating speeds them up._
- ✅ They gain energy and move faster.

Full working after a second miss:

> The true statement is “They gain energy and move faster.”.  
> “They get bigger.” is false: The particles do not grow; they move faster.  
> “They change into new particles.” is false: Heating alone does not make new particles in a change of state.  
> “They stop moving.” is false: Cooling slows them down; heating speeds them up.  

Sources: kinetic (Simple kinetic theory of matter; diffusion)

### `ch11-diffusion` · Lesson 11 · multiple choice, level 1

Prompt: {x.t} Which of these explains it?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| The smell of ndolé cooking fills the house. | diffusion | The smell of ndolé cooking fills the house. This is diffusion. |
| A purple crystal slowly colours still water. | diffusion | A purple crystal slowly colours still water. This is diffusion. |
| Water in a pot turns to steam. | boiling | Water in a pot turns to steam. This is boiling. |
| Ice cubes in a drink turn to water. | melting | Ice cubes in a drink turn to water. This is melting. |

Right answer: `{x.a}`; wrong choices: `diffusion`, `boiling`, `melting`, `condensation`

- Feedback `other`: “Is something spreading out, or changing state?”

Three generated variants:

> Water in a pot turns to steam. Which of these explains it?

- ◻️ condensation  
  _↳ feedback if chosen: Is something spreading out, or changing state?_
- ◻️ melting  
  _↳ feedback if chosen: Is something spreading out, or changing state?_
- ◻️ diffusion  
  _↳ feedback if chosen: Is something spreading out, or changing state?_
- ✅ boiling

Full working after a second miss:

> Water in a pot turns to steam. This is boiling.  
> Answer: boiling.  

> A purple crystal slowly colours still water. Which of these explains it?

- ◻️ melting  
  _↳ feedback if chosen: Is something spreading out, or changing state?_
- ◻️ boiling  
  _↳ feedback if chosen: Is something spreading out, or changing state?_
- ✅ diffusion
- ◻️ condensation  
  _↳ feedback if chosen: Is something spreading out, or changing state?_

Full working after a second miss:

> A purple crystal slowly colours still water. This is diffusion.  
> Answer: diffusion.  

> Water in a pot turns to steam. Which of these explains it?

- ◻️ melting  
  _↳ feedback if chosen: Is something spreading out, or changing state?_
- ✅ boiling
- ◻️ condensation  
  _↳ feedback if chosen: Is something spreading out, or changing state?_
- ◻️ diffusion  
  _↳ feedback if chosen: Is something spreading out, or changing state?_

Full working after a second miss:

> Water in a pot turns to steam. This is boiling.  
> Answer: boiling.  

Sources: kinetic (Simple kinetic theory of matter; diffusion)

### `ch11-faster` · Lesson 11 · multiple choice, level 2

Prompt: In which case does diffusion happen fastest?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ a smell spreading through warm air
- ❌ a smell spreading through cold air  
  _↳ Diffusion is faster when it is warm: the particles move faster._
- ❌ ink spreading through cold water  
  _↳ Diffusion is much faster in gases than in liquids._
- ❌ a solid spreading into another solid  
  _↳ In solids the particles only vibrate: diffusion is extremely slow._


Three generated variants:

> In which case does diffusion happen fastest?

- ◻️ a solid spreading into another solid  
  _↳ feedback if chosen: In solids the particles only vibrate: diffusion is extremely slow._
- ◻️ ink spreading through cold water  
  _↳ feedback if chosen: Diffusion is much faster in gases than in liquids._
- ✅ a smell spreading through warm air
- ◻️ a smell spreading through cold air  
  _↳ feedback if chosen: Diffusion is faster when it is warm: the particles move faster._

Full working after a second miss:

> The true statement is “a smell spreading through warm air”.  
> “a solid spreading into another solid” is false: In solids the particles only vibrate: diffusion is extremely slow.  
> “ink spreading through cold water” is false: Diffusion is much faster in gases than in liquids.  
> “a smell spreading through cold air” is false: Diffusion is faster when it is warm: the particles move faster.  

> In which case does diffusion happen fastest?

- ✅ a smell spreading through warm air
- ◻️ a solid spreading into another solid  
  _↳ feedback if chosen: In solids the particles only vibrate: diffusion is extremely slow._
- ◻️ ink spreading through cold water  
  _↳ feedback if chosen: Diffusion is much faster in gases than in liquids._
- ◻️ a smell spreading through cold air  
  _↳ feedback if chosen: Diffusion is faster when it is warm: the particles move faster._

Full working after a second miss:

> The true statement is “a smell spreading through warm air”.  
> “a solid spreading into another solid” is false: In solids the particles only vibrate: diffusion is extremely slow.  
> “ink spreading through cold water” is false: Diffusion is much faster in gases than in liquids.  
> “a smell spreading through cold air” is false: Diffusion is faster when it is warm: the particles move faster.  

> In which case does diffusion happen fastest?

- ◻️ a solid spreading into another solid  
  _↳ feedback if chosen: In solids the particles only vibrate: diffusion is extremely slow._
- ◻️ ink spreading through cold water  
  _↳ feedback if chosen: Diffusion is much faster in gases than in liquids._
- ◻️ a smell spreading through cold air  
  _↳ feedback if chosen: Diffusion is faster when it is warm: the particles move faster._
- ✅ a smell spreading through warm air

Full working after a second miss:

> The true statement is “a smell spreading through warm air”.  
> “a solid spreading into another solid” is false: In solids the particles only vibrate: diffusion is extremely slow.  
> “ink spreading through cold water” is false: Diffusion is much faster in gases than in liquids.  
> “a smell spreading through cold air” is false: Diffusion is faster when it is warm: the particles move faster.  

Sources: kinetic (Simple kinetic theory of matter; diffusion)

### `ch11-spot` · Lesson 11 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Particles in a gas move fast in all directions.
- ✅ Heating makes particles move faster.
- ✅ Diffusion is faster in gases than in liquids.
- ✅ All matter is made of tiny particles.
- ❌ Particles in a solid do not move at all.  
  _↳ They vibrate in fixed places._
- ❌ When ice melts, its particles get bigger.  
  _↳ The particles move more; they do not get bigger._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Particles in a gas move fast in all directions.
- ✅ When ice melts, its particles get bigger.  
  _↳ explanation: The particles move more; they do not get bigger._
- ◻️ All matter is made of tiny particles.
- ◻️ Heating makes particles move faster.

Full working after a second miss:

> The wrong statement is “When ice melts, its particles get bigger.”.  
> The particles move more; they do not get bigger.  

> One sentence is wrong. Which one?

- ✅ Particles in a solid do not move at all.  
  _↳ explanation: They vibrate in fixed places._
- ◻️ Heating makes particles move faster.
- ◻️ Diffusion is faster in gases than in liquids.
- ◻️ All matter is made of tiny particles.

Full working after a second miss:

> The wrong statement is “Particles in a solid do not move at all.”.  
> They vibrate in fixed places.  

> One sentence is wrong. Which one?

- ◻️ Particles in a gas move fast in all directions.
- ◻️ All matter is made of tiny particles.
- ✅ Particles in a solid do not move at all.  
  _↳ explanation: They vibrate in fixed places._
- ◻️ Heating makes particles move faster.

Full working after a second miss:

> The wrong statement is “Particles in a solid do not move at all.”.  
> They vibrate in fixed places.  

Sources: kinetic (Simple kinetic theory of matter; diffusion)

### `ch12-sort` · Lesson 12 · matching, level 1

Prompt: Sort them: pure substance or mixture?

Pairs (6 shown each time, sorted into groups):

- distilled water → **pure substance**
- table salt (sodium chloride) → **pure substance**
- sugar → **pure substance**
- oxygen → **pure substance**
- iron → **pure substance**
- gold → **pure substance**
- carbon dioxide → **pure substance**
- air → **mixture**
- sea water → **mixture**
- soil → **mixture**
- tap water → **mixture**
- palm wine → **mixture**
- concrete → **mixture**
- milk → **mixture**
- a soft drink → **mixture**


Three generated variants:

> Sort them: pure substance or mixture?

Groups: pure substance · mixture
- oxygen → **pure substance**
- milk → **mixture**
- iron → **pure substance**
- concrete → **mixture**
- air → **mixture**
- table salt (sodium chloride) → **pure substance**

Full working after a second miss:

> The right pairs are:  
> oxygen → pure substance  
> milk → mixture  
> iron → pure substance  
> concrete → mixture  
> air → mixture  
> table salt (sodium chloride) → pure substance  

> Sort them: pure substance or mixture?

Groups: pure substance · mixture
- concrete → **mixture**
- a soft drink → **mixture**
- iron → **pure substance**
- palm wine → **mixture**
- table salt (sodium chloride) → **pure substance**
- oxygen → **pure substance**

Full working after a second miss:

> The right pairs are:  
> concrete → mixture  
> a soft drink → mixture  
> iron → pure substance  
> palm wine → mixture  
> table salt (sodium chloride) → pure substance  
> oxygen → pure substance  

> Sort them: pure substance or mixture?

Groups: pure substance · mixture
- distilled water → **pure substance**
- iron → **pure substance**
- milk → **mixture**
- a soft drink → **mixture**
- table salt (sodium chloride) → **pure substance**
- soil → **mixture**

Full working after a second miss:

> The right pairs are:  
> distilled water → pure substance  
> iron → pure substance  
> milk → mixture  
> a soft drink → mixture  
> table salt (sodium chloride) → pure substance  
> soil → mixture  

Sources: mixtures (Pure substances and mixtures; types of mixtures; solutions and suspensions)

### `ch12-which` · Lesson 12 · multiple choice, level 1

Prompt: Which of these is a mixture?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ air
- ✅ sea water
- ✅ soil
- ✅ tap water
- ✅ palm wine
- ✅ concrete
- ✅ milk
- ✅ a soft drink
- ❌ distilled water  
  _↳ Distilled water is one kind of matter only: a pure substance._
- ❌ table salt (sodium chloride)  
  _↳ Table salt (sodium chloride) is one kind of matter only: a pure substance._
- ❌ sugar  
  _↳ Sugar is one kind of matter only: a pure substance._
- ❌ oxygen  
  _↳ Oxygen is one kind of matter only: a pure substance._
- ❌ iron  
  _↳ Iron is one kind of matter only: a pure substance._
- ❌ gold  
  _↳ Gold is one kind of matter only: a pure substance._
- ❌ carbon dioxide  
  _↳ Carbon dioxide is one kind of matter only: a pure substance._


Three generated variants:

> Which of these is a mixture?

- ◻️ sugar  
  _↳ feedback if chosen: Sugar is one kind of matter only: a pure substance._
- ✅ air
- ◻️ gold  
  _↳ feedback if chosen: Gold is one kind of matter only: a pure substance._
- ◻️ carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide is one kind of matter only: a pure substance._

Full working after a second miss:

> The true statement is “air”.  
> “sugar” is false: Sugar is one kind of matter only: a pure substance.  
> “gold” is false: Gold is one kind of matter only: a pure substance.  
> “carbon dioxide” is false: Carbon dioxide is one kind of matter only: a pure substance.  

> Which of these is a mixture?

- ◻️ distilled water  
  _↳ feedback if chosen: Distilled water is one kind of matter only: a pure substance._
- ◻️ table salt (sodium chloride)  
  _↳ feedback if chosen: Table salt (sodium chloride) is one kind of matter only: a pure substance._
- ◻️ sugar  
  _↳ feedback if chosen: Sugar is one kind of matter only: a pure substance._
- ✅ soil

Full working after a second miss:

> The true statement is “soil”.  
> “distilled water” is false: Distilled water is one kind of matter only: a pure substance.  
> “table salt (sodium chloride)” is false: Table salt (sodium chloride) is one kind of matter only: a pure substance.  
> “sugar” is false: Sugar is one kind of matter only: a pure substance.  

> Which of these is a mixture?

- ◻️ gold  
  _↳ feedback if chosen: Gold is one kind of matter only: a pure substance._
- ◻️ table salt (sodium chloride)  
  _↳ feedback if chosen: Table salt (sodium chloride) is one kind of matter only: a pure substance._
- ◻️ distilled water  
  _↳ feedback if chosen: Distilled water is one kind of matter only: a pure substance._
- ✅ palm wine

Full working after a second miss:

> The true statement is “palm wine”.  
> “gold” is false: Gold is one kind of matter only: a pure substance.  
> “table salt (sodium chloride)” is false: Table salt (sodium chloride) is one kind of matter only: a pure substance.  
> “distilled water” is false: Distilled water is one kind of matter only: a pure substance.  

Sources: mixtures (Pure substances and mixtures; types of mixtures; solutions and suspensions)

### `ch12-why` · Lesson 12 · multiple choice, level 2

Prompt: Why is air a mixture and not a pure substance?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ It contains several gases (nitrogen, oxygen, carbon dioxide…) that are not chemically joined.
- ❌ Because we cannot see it.  
  _↳ We cannot see oxygen either, and oxygen is pure._
- ❌ Because it is a gas.  
  _↳ Oxygen is a gas and it is pure._
- ❌ Because it is everywhere.  
  _↳ That does not decide; air is several gases mixed together._


Three generated variants:

> Why is air a mixture and not a pure substance?

- ✅ It contains several gases (nitrogen, oxygen, carbon dioxide…) that are not chemically joined.
- ◻️ Because it is a gas.  
  _↳ feedback if chosen: Oxygen is a gas and it is pure._
- ◻️ Because it is everywhere.  
  _↳ feedback if chosen: That does not decide; air is several gases mixed together._
- ◻️ Because we cannot see it.  
  _↳ feedback if chosen: We cannot see oxygen either, and oxygen is pure._

Full working after a second miss:

> The true statement is “It contains several gases (nitrogen, oxygen, carbon dioxide…) that are not chemically joined.”.  
> “Because it is a gas.” is false: Oxygen is a gas and it is pure.  
> “Because it is everywhere.” is false: That does not decide; air is several gases mixed together.  
> “Because we cannot see it.” is false: We cannot see oxygen either, and oxygen is pure.  

> Why is air a mixture and not a pure substance?

- ✅ It contains several gases (nitrogen, oxygen, carbon dioxide…) that are not chemically joined.
- ◻️ Because we cannot see it.  
  _↳ feedback if chosen: We cannot see oxygen either, and oxygen is pure._
- ◻️ Because it is everywhere.  
  _↳ feedback if chosen: That does not decide; air is several gases mixed together._
- ◻️ Because it is a gas.  
  _↳ feedback if chosen: Oxygen is a gas and it is pure._

Full working after a second miss:

> The true statement is “It contains several gases (nitrogen, oxygen, carbon dioxide…) that are not chemically joined.”.  
> “Because we cannot see it.” is false: We cannot see oxygen either, and oxygen is pure.  
> “Because it is everywhere.” is false: That does not decide; air is several gases mixed together.  
> “Because it is a gas.” is false: Oxygen is a gas and it is pure.  

> Why is air a mixture and not a pure substance?

- ◻️ Because it is a gas.  
  _↳ feedback if chosen: Oxygen is a gas and it is pure._
- ✅ It contains several gases (nitrogen, oxygen, carbon dioxide…) that are not chemically joined.
- ◻️ Because it is everywhere.  
  _↳ feedback if chosen: That does not decide; air is several gases mixed together._
- ◻️ Because we cannot see it.  
  _↳ feedback if chosen: We cannot see oxygen either, and oxygen is pure._

Full working after a second miss:

> The true statement is “It contains several gases (nitrogen, oxygen, carbon dioxide…) that are not chemically joined.”.  
> “Because it is a gas.” is false: Oxygen is a gas and it is pure.  
> “Because it is everywhere.” is false: That does not decide; air is several gases mixed together.  
> “Because we cannot see it.” is false: We cannot see oxygen either, and oxygen is pure.  

Sources: mixtures (Pure substances and mixtures; types of mixtures; solutions and suspensions)

### `ch12-spot` · Lesson 12 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Sea water is a mixture.
- ✅ Oxygen is a pure substance.
- ✅ The parts of a mixture can be separated by physical methods.
- ✅ Distilled water is pure.
- ❌ Tap water is a pure substance.  
  _↳ Tap water contains dissolved substances: it is a mixture._
- ❌ A mixture has a fixed boiling point.  
  _↳ Mixtures boil over a range of temperatures._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ The parts of a mixture can be separated by physical methods.
- ◻️ Distilled water is pure.
- ◻️ Oxygen is a pure substance.
- ✅ Tap water is a pure substance.  
  _↳ explanation: Tap water contains dissolved substances: it is a mixture._

Full working after a second miss:

> The wrong statement is “Tap water is a pure substance.”.  
> Tap water contains dissolved substances: it is a mixture.  

> One sentence is wrong. Which one?

- ◻️ Oxygen is a pure substance.
- ◻️ The parts of a mixture can be separated by physical methods.
- ◻️ Sea water is a mixture.
- ✅ A mixture has a fixed boiling point.  
  _↳ explanation: Mixtures boil over a range of temperatures._

Full working after a second miss:

> The wrong statement is “A mixture has a fixed boiling point.”.  
> Mixtures boil over a range of temperatures.  

> One sentence is wrong. Which one?

- ◻️ The parts of a mixture can be separated by physical methods.
- ◻️ Sea water is a mixture.
- ✅ A mixture has a fixed boiling point.  
  _↳ explanation: Mixtures boil over a range of temperatures._
- ◻️ Distilled water is pure.

Full working after a second miss:

> The wrong statement is “A mixture has a fixed boiling point.”.  
> Mixtures boil over a range of temperatures.  

Sources: mixtures (Pure substances and mixtures; types of mixtures; solutions and suspensions)

### `chc12-3-check` · Lesson 12 · multiple choice, level 1

Prompt: Which sentence is about a mixture?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Its parts can be present in any amounts.
- ❌ It has a fixed boiling point.  
  _↳ That is a pure substance._
- ❌ It is made of only one kind of matter.  
  _↳ That is a pure substance._
- ❌ It can only be split by a chemical reaction.  
  _↳ Mixtures can be separated by physical methods._


Three generated variants:

> Which sentence is about a mixture?

- ◻️ It can only be split by a chemical reaction.  
  _↳ feedback if chosen: Mixtures can be separated by physical methods._
- ◻️ It is made of only one kind of matter.  
  _↳ feedback if chosen: That is a pure substance._
- ◻️ It has a fixed boiling point.  
  _↳ feedback if chosen: That is a pure substance._
- ✅ Its parts can be present in any amounts.

Full working after a second miss:

> The true statement is “Its parts can be present in any amounts.”.  
> “It can only be split by a chemical reaction.” is false: Mixtures can be separated by physical methods.  
> “It is made of only one kind of matter.” is false: That is a pure substance.  
> “It has a fixed boiling point.” is false: That is a pure substance.  

> Which sentence is about a mixture?

- ◻️ It is made of only one kind of matter.  
  _↳ feedback if chosen: That is a pure substance._
- ◻️ It can only be split by a chemical reaction.  
  _↳ feedback if chosen: Mixtures can be separated by physical methods._
- ✅ Its parts can be present in any amounts.
- ◻️ It has a fixed boiling point.  
  _↳ feedback if chosen: That is a pure substance._

Full working after a second miss:

> The true statement is “Its parts can be present in any amounts.”.  
> “It is made of only one kind of matter.” is false: That is a pure substance.  
> “It can only be split by a chemical reaction.” is false: Mixtures can be separated by physical methods.  
> “It has a fixed boiling point.” is false: That is a pure substance.  

> Which sentence is about a mixture?

- ◻️ It is made of only one kind of matter.  
  _↳ feedback if chosen: That is a pure substance._
- ◻️ It has a fixed boiling point.  
  _↳ feedback if chosen: That is a pure substance._
- ◻️ It can only be split by a chemical reaction.  
  _↳ feedback if chosen: Mixtures can be separated by physical methods._
- ✅ Its parts can be present in any amounts.

Full working after a second miss:

> The true statement is “Its parts can be present in any amounts.”.  
> “It is made of only one kind of matter.” is false: That is a pure substance.  
> “It has a fixed boiling point.” is false: That is a pure substance.  
> “It can only be split by a chemical reaction.” is false: Mixtures can be separated by physical methods.  

Sources: mixtures (Pure substances and mixtures; types of mixtures; solutions and suspensions)

### `ch13-type` · Lesson 13 · multiple choice, level 1

Prompt: What type of mixture is {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| sand and salt | solid and solid | sand and salt: a mixture of solid and solid. |
| garri mixed with small stones | solid and solid | garri mixed with small stones: a mixture of solid and solid. |
| muddy water | solid and liquid | muddy water: a mixture of solid and liquid. |
| salt water | solid and liquid | salt water: a mixture of solid and liquid. |
| palm oil and water | liquid and liquid | palm oil and water: a mixture of liquid and liquid. |
| ethanol and water | liquid and liquid | ethanol and water: a mixture of liquid and liquid. |
| a soft drink (carbon dioxide in water) | gas and liquid | a soft drink (carbon dioxide in water): a mixture of gas and liquid. |
| air | gas and gas | air: a mixture of gas and gas. |
| smoke (soot in air) | solid and gas | smoke (soot in air): a mixture of solid and gas. |

Right answer: `{x.a}`; wrong choices: `solid and solid`, `solid and liquid`, `liquid and liquid`, `gas and liquid`, `gas and gas`, `solid and gas`

- Feedback `other`: “Think about the state of each part.”

Three generated variants:

> What type of mixture is ethanol and water?

- ✅ liquid and liquid
- ◻️ solid and gas  
  _↳ feedback if chosen: Think about the state of each part._
- ◻️ solid and liquid  
  _↳ feedback if chosen: Think about the state of each part._
- ◻️ gas and gas  
  _↳ feedback if chosen: Think about the state of each part._

Full working after a second miss:

> ethanol and water: a mixture of liquid and liquid.  
> Answer: liquid and liquid.  

> What type of mixture is smoke (soot in air)?

- ◻️ gas and gas  
  _↳ feedback if chosen: Think about the state of each part._
- ✅ solid and gas
- ◻️ solid and solid  
  _↳ feedback if chosen: Think about the state of each part._
- ◻️ solid and liquid  
  _↳ feedback if chosen: Think about the state of each part._

Full working after a second miss:

> smoke (soot in air): a mixture of solid and gas.  
> Answer: solid and gas.  

> What type of mixture is ethanol and water?

- ✅ liquid and liquid
- ◻️ gas and gas  
  _↳ feedback if chosen: Think about the state of each part._
- ◻️ solid and gas  
  _↳ feedback if chosen: Think about the state of each part._
- ◻️ solid and solid  
  _↳ feedback if chosen: Think about the state of each part._

Full working after a second miss:

> ethanol and water: a mixture of liquid and liquid.  
> Answer: liquid and liquid.  

Sources: mixtures (Pure substances and mixtures; types of mixtures; solutions and suspensions)

### `ch13-misc` · Lesson 13 · matching, level 1

Prompt: Do these liquids mix with water, or form layers?

Pairs (4 shown each time, sorted into groups):

- ethanol and water → **miscible (they mix)**
- vinegar and water → **miscible (they mix)**
- milk and water → **miscible (they mix)**
- palm oil and water → **immiscible (two layers)**
- kerosene and water → **immiscible (two layers)**
- petrol and water → **immiscible (two layers)**


Three generated variants:

> Do these liquids mix with water, or form layers?

Groups: miscible (they mix) · immiscible (two layers)
- ethanol and water → **miscible (they mix)**
- petrol and water → **immiscible (two layers)**
- vinegar and water → **miscible (they mix)**
- kerosene and water → **immiscible (two layers)**

Full working after a second miss:

> The right pairs are:  
> ethanol and water → miscible (they mix)  
> petrol and water → immiscible (two layers)  
> vinegar and water → miscible (they mix)  
> kerosene and water → immiscible (two layers)  

> Do these liquids mix with water, or form layers?

Groups: miscible (they mix) · immiscible (two layers)
- vinegar and water → **miscible (they mix)**
- palm oil and water → **immiscible (two layers)**
- milk and water → **miscible (they mix)**
- kerosene and water → **immiscible (two layers)**

Full working after a second miss:

> The right pairs are:  
> vinegar and water → miscible (they mix)  
> palm oil and water → immiscible (two layers)  
> milk and water → miscible (they mix)  
> kerosene and water → immiscible (two layers)  

> Do these liquids mix with water, or form layers?

Groups: miscible (they mix) · immiscible (two layers)
- milk and water → **miscible (they mix)**
- vinegar and water → **miscible (they mix)**
- ethanol and water → **miscible (they mix)**
- kerosene and water → **immiscible (two layers)**

Full working after a second miss:

> The right pairs are:  
> milk and water → miscible (they mix)  
> vinegar and water → miscible (they mix)  
> ethanol and water → miscible (they mix)  
> kerosene and water → immiscible (two layers)  

Sources: mixtures (Pure substances and mixtures; types of mixtures; solutions and suspensions)

### `ch13-solution` · Lesson 13 · matching, level 2

Prompt: Solution (dissolves completely) or suspension (pieces settle)?

Pairs (5 shown each time, sorted into groups):

- salt in water → **solution**
- sugar in tea → **solution**
- copper(II) sulfate in water → **solution**
- muddy water → **suspension**
- chalk dust in water → **suspension**
- sand in water → **suspension**


Three generated variants:

> Solution (dissolves completely) or suspension (pieces settle)?

Groups: solution · suspension
- sand in water → **suspension**
- sugar in tea → **solution**
- muddy water → **suspension**
- salt in water → **solution**
- chalk dust in water → **suspension**

Full working after a second miss:

> The right pairs are:  
> sand in water → suspension  
> sugar in tea → solution  
> muddy water → suspension  
> salt in water → solution  
> chalk dust in water → suspension  

> Solution (dissolves completely) or suspension (pieces settle)?

Groups: solution · suspension
- muddy water → **suspension**
- chalk dust in water → **suspension**
- sand in water → **suspension**
- copper(II) sulfate in water → **solution**
- sugar in tea → **solution**

Full working after a second miss:

> The right pairs are:  
> muddy water → suspension  
> chalk dust in water → suspension  
> sand in water → suspension  
> copper(II) sulfate in water → solution  
> sugar in tea → solution  

> Solution (dissolves completely) or suspension (pieces settle)?

Groups: solution · suspension
- sugar in tea → **solution**
- sand in water → **suspension**
- muddy water → **suspension**
- chalk dust in water → **suspension**
- copper(II) sulfate in water → **solution**

Full working after a second miss:

> The right pairs are:  
> sugar in tea → solution  
> sand in water → suspension  
> muddy water → suspension  
> chalk dust in water → suspension  
> copper(II) sulfate in water → solution  

Sources: mixtures (Pure substances and mixtures; types of mixtures; solutions and suspensions)

### `ch13-spot` · Lesson 13 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Air is a gas–gas mixture.
- ✅ Palm oil and water are immiscible.
- ✅ In salt water, salt is the solute.
- ✅ A soft drink contains a dissolved gas.
- ❌ Muddy water is a solution.  
  _↳ The mud does not dissolve and settles: it is a suspension._
- ❌ Ethanol and water form two layers.  
  _↳ Ethanol and water are miscible: they mix completely._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ Muddy water is a solution.  
  _↳ explanation: The mud does not dissolve and settles: it is a suspension._
- ◻️ Air is a gas–gas mixture.
- ◻️ Palm oil and water are immiscible.
- ◻️ A soft drink contains a dissolved gas.

Full working after a second miss:

> The wrong statement is “Muddy water is a solution.”.  
> The mud does not dissolve and settles: it is a suspension.  

> One sentence is wrong. Which one?

- ◻️ A soft drink contains a dissolved gas.
- ✅ Ethanol and water form two layers.  
  _↳ explanation: Ethanol and water are miscible: they mix completely._
- ◻️ Air is a gas–gas mixture.
- ◻️ Palm oil and water are immiscible.

Full working after a second miss:

> The wrong statement is “Ethanol and water form two layers.”.  
> Ethanol and water are miscible: they mix completely.  

> One sentence is wrong. Which one?

- ✅ Ethanol and water form two layers.  
  _↳ explanation: Ethanol and water are miscible: they mix completely._
- ◻️ In salt water, salt is the solute.
- ◻️ Palm oil and water are immiscible.
- ◻️ Air is a gas–gas mixture.

Full working after a second miss:

> The wrong statement is “Ethanol and water form two layers.”.  
> Ethanol and water are miscible: they mix completely.  

Sources: mixtures (Pure substances and mixtures; types of mixtures; solutions and suspensions)

### `chc13-3-check` · Lesson 13 · multiple choice, level 1

Prompt: In salt water, which is the solvent?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ water
- ❌ salt  
  _↳ The salt is the solute: it dissolves._
- ❌ the cup  
  _↳ The solvent is the liquid that does the dissolving._
- ❌ the air  
  _↳ Air is not part of the solution._


Three generated variants:

> In salt water, which is the solvent?

- ✅ water
- ◻️ the cup  
  _↳ feedback if chosen: The solvent is the liquid that does the dissolving._
- ◻️ the air  
  _↳ feedback if chosen: Air is not part of the solution._
- ◻️ salt  
  _↳ feedback if chosen: The salt is the solute: it dissolves._

Full working after a second miss:

> The true statement is “water”.  
> “the cup” is false: The solvent is the liquid that does the dissolving.  
> “the air” is false: Air is not part of the solution.  
> “salt” is false: The salt is the solute: it dissolves.  

> In salt water, which is the solvent?

- ✅ water
- ◻️ salt  
  _↳ feedback if chosen: The salt is the solute: it dissolves._
- ◻️ the cup  
  _↳ feedback if chosen: The solvent is the liquid that does the dissolving._
- ◻️ the air  
  _↳ feedback if chosen: Air is not part of the solution._

Full working after a second miss:

> The true statement is “water”.  
> “salt” is false: The salt is the solute: it dissolves.  
> “the cup” is false: The solvent is the liquid that does the dissolving.  
> “the air” is false: Air is not part of the solution.  

> In salt water, which is the solvent?

- ◻️ the cup  
  _↳ feedback if chosen: The solvent is the liquid that does the dissolving._
- ◻️ salt  
  _↳ feedback if chosen: The salt is the solute: it dissolves._
- ✅ water
- ◻️ the air  
  _↳ feedback if chosen: Air is not part of the solution._

Full working after a second miss:

> The true statement is “water”.  
> “the cup” is false: The solvent is the liquid that does the dissolving.  
> “salt” is false: The salt is the solute: it dissolves.  
> “the air” is false: Air is not part of the solution.  

Sources: mixtures (Pure substances and mixtures; types of mixtures; solutions and suspensions)

### `ch14-method` · Lesson 14 · multiple choice, level 1

Prompt: Which method would you use to separate {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| stones from rice | hand-picking | To separate stones from rice, use hand-picking. |
| fine garri from lumps | sieving | To separate fine garri from lumps, use sieving. |
| iron filings from sand | magnetic separation | To separate iron filings from sand, use magnetic separation. |
| chaff from rice grains | winnowing | To separate chaff from rice grains, use winnowing. |
| iodine from sand | sublimation | To separate iodine from sand, use sublimation. |
| salt from sand | dissolving, filtering and evaporating | To separate salt from sand, use dissolving, filtering and evaporating. |

Right answer: `{x.a}`; wrong choices: `hand-picking`, `sieving`, `magnetic separation`, `winnowing`, `sublimation`, `dissolving, filtering and evaporating`

- Feedback `other`: “That method uses a different difference between the solids.”

Three generated variants:

> Which method would you use to separate salt from sand?

- ◻️ hand-picking  
  _↳ feedback if chosen: That method uses a different difference between the solids._
- ✅ dissolving, filtering and evaporating
- ◻️ sublimation  
  _↳ feedback if chosen: That method uses a different difference between the solids._
- ◻️ magnetic separation  
  _↳ feedback if chosen: That method uses a different difference between the solids._

Full working after a second miss:

> To separate salt from sand, use dissolving, filtering and evaporating.  
> Answer: dissolving, filtering and evaporating.  

> Which method would you use to separate iodine from sand?

- ◻️ magnetic separation  
  _↳ feedback if chosen: That method uses a different difference between the solids._
- ◻️ dissolving, filtering and evaporating  
  _↳ feedback if chosen: That method uses a different difference between the solids._
- ✅ sublimation
- ◻️ hand-picking  
  _↳ feedback if chosen: That method uses a different difference between the solids._

Full working after a second miss:

> To separate iodine from sand, use sublimation.  
> Answer: sublimation.  

> Which method would you use to separate chaff from rice grains?

- ✅ winnowing
- ◻️ hand-picking  
  _↳ feedback if chosen: That method uses a different difference between the solids._
- ◻️ magnetic separation  
  _↳ feedback if chosen: That method uses a different difference between the solids._
- ◻️ sublimation  
  _↳ feedback if chosen: That method uses a different difference between the solids._

Full working after a second miss:

> To separate chaff from rice grains, use winnowing.  
> Answer: winnowing.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch14-match` · Lesson 14 · matching, level 1

Prompt: Match each method with how it works.

Pairs (4 shown each time):

- hand-picking → **pick out the unwanted pieces by hand**
- sieving → **shake through a sieve: small pieces fall through, big ones stay**
- magnetic separation → **a magnet pulls out the iron**
- winnowing → **the wind blows away the light chaff**
- sublimation → **heat: one solid turns into a gas and is collected when it cools**
- dissolving, filtering and evaporating → **dissolve one solid, filter out the other, evaporate the water**


Three generated variants:

> Match each method with how it works.

Right-hand side (shuffled): a magnet pulls out the iron · shake through a sieve: small pieces fall through, big ones stay · pick out the unwanted pieces by hand · the wind blows away the light chaff
- sieving → **shake through a sieve: small pieces fall through, big ones stay**
- magnetic separation → **a magnet pulls out the iron**
- winnowing → **the wind blows away the light chaff**
- hand-picking → **pick out the unwanted pieces by hand**

Full working after a second miss:

> The right pairs are:  
> sieving → shake through a sieve: small pieces fall through, big ones stay  
> magnetic separation → a magnet pulls out the iron  
> winnowing → the wind blows away the light chaff  
> hand-picking → pick out the unwanted pieces by hand  

> Match each method with how it works.

Right-hand side (shuffled): heat: one solid turns into a gas and is collected when it cools · a magnet pulls out the iron · shake through a sieve: small pieces fall through, big ones stay · dissolve one solid, filter out the other, evaporate the water
- sublimation → **heat: one solid turns into a gas and is collected when it cools**
- sieving → **shake through a sieve: small pieces fall through, big ones stay**
- dissolving, filtering and evaporating → **dissolve one solid, filter out the other, evaporate the water**
- magnetic separation → **a magnet pulls out the iron**

Full working after a second miss:

> The right pairs are:  
> sublimation → heat: one solid turns into a gas and is collected when it cools  
> sieving → shake through a sieve: small pieces fall through, big ones stay  
> dissolving, filtering and evaporating → dissolve one solid, filter out the other, evaporate the water  
> magnetic separation → a magnet pulls out the iron  

> Match each method with how it works.

Right-hand side (shuffled): a magnet pulls out the iron · the wind blows away the light chaff · dissolve one solid, filter out the other, evaporate the water · heat: one solid turns into a gas and is collected when it cools
- sublimation → **heat: one solid turns into a gas and is collected when it cools**
- magnetic separation → **a magnet pulls out the iron**
- dissolving, filtering and evaporating → **dissolve one solid, filter out the other, evaporate the water**
- winnowing → **the wind blows away the light chaff**

Full working after a second miss:

> The right pairs are:  
> sublimation → heat: one solid turns into a gas and is collected when it cools  
> magnetic separation → a magnet pulls out the iron  
> dissolving, filtering and evaporating → dissolve one solid, filter out the other, evaporate the water  
> winnowing → the wind blows away the light chaff  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch14-steps` · Lesson 14 · ordering, level 1

Prompt: Put the steps in order to get salt from a mixture of salt and sand.

Items in the right order:

1. Add water and stir until the salt dissolves.
2. Filter the mixture.
3. Collect the salt water (filtrate) in an evaporating dish.
4. Heat until the water evaporates and salt is left.


Three generated variants:

> Put the steps in order to get salt from a mixture of salt and sand.

Shown as: Filter the mixture. · Heat until the water evaporates and salt is left. · Collect the salt water (filtrate) in an evaporating dish. · Add water and stir until the salt dissolves.
Correct order: Add water and stir until the salt dissolves. → Filter the mixture. → Collect the salt water (filtrate) in an evaporating dish. → Heat until the water evaporates and salt is left.

Full working after a second miss:

> The correct order is: Add water and stir until the salt dissolves. → Filter the mixture. → Collect the salt water (filtrate) in an evaporating dish. → Heat until the water evaporates and salt is left..  

> Put the steps in order to get salt from a mixture of salt and sand.

Shown as: Filter the mixture. · Collect the salt water (filtrate) in an evaporating dish. · Heat until the water evaporates and salt is left. · Add water and stir until the salt dissolves.
Correct order: Add water and stir until the salt dissolves. → Filter the mixture. → Collect the salt water (filtrate) in an evaporating dish. → Heat until the water evaporates and salt is left.

Full working after a second miss:

> The correct order is: Add water and stir until the salt dissolves. → Filter the mixture. → Collect the salt water (filtrate) in an evaporating dish. → Heat until the water evaporates and salt is left..  

> Put the steps in order to get salt from a mixture of salt and sand.

Shown as: Collect the salt water (filtrate) in an evaporating dish. · Filter the mixture. · Add water and stir until the salt dissolves. · Heat until the water evaporates and salt is left.
Correct order: Add water and stir until the salt dissolves. → Filter the mixture. → Collect the salt water (filtrate) in an evaporating dish. → Heat until the water evaporates and salt is left.

Full working after a second miss:

> The correct order is: Add water and stir until the salt dissolves. → Filter the mixture. → Collect the salt water (filtrate) in an evaporating dish. → Heat until the water evaporates and salt is left..  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch14-why` · Lesson 14 · multiple choice, level 2

Prompt: Why can a magnet separate iron filings from sand?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Iron is attracted by a magnet; sand is not.
- ❌ Iron is heavier than sand.  
  _↳ Weight is not used here; magnetism is._
- ❌ Iron dissolves in water.  
  _↳ Iron does not dissolve in water._
- ❌ Sand is attracted by a magnet.  
  _↳ Sand is not attracted; iron is._


Three generated variants:

> Why can a magnet separate iron filings from sand?

- ◻️ Iron dissolves in water.  
  _↳ feedback if chosen: Iron does not dissolve in water._
- ◻️ Sand is attracted by a magnet.  
  _↳ feedback if chosen: Sand is not attracted; iron is._
- ✅ Iron is attracted by a magnet; sand is not.
- ◻️ Iron is heavier than sand.  
  _↳ feedback if chosen: Weight is not used here; magnetism is._

Full working after a second miss:

> The true statement is “Iron is attracted by a magnet; sand is not.”.  
> “Iron dissolves in water.” is false: Iron does not dissolve in water.  
> “Sand is attracted by a magnet.” is false: Sand is not attracted; iron is.  
> “Iron is heavier than sand.” is false: Weight is not used here; magnetism is.  

> Why can a magnet separate iron filings from sand?

- ◻️ Iron is heavier than sand.  
  _↳ feedback if chosen: Weight is not used here; magnetism is._
- ◻️ Iron dissolves in water.  
  _↳ feedback if chosen: Iron does not dissolve in water._
- ◻️ Sand is attracted by a magnet.  
  _↳ feedback if chosen: Sand is not attracted; iron is._
- ✅ Iron is attracted by a magnet; sand is not.

Full working after a second miss:

> The true statement is “Iron is attracted by a magnet; sand is not.”.  
> “Iron is heavier than sand.” is false: Weight is not used here; magnetism is.  
> “Iron dissolves in water.” is false: Iron does not dissolve in water.  
> “Sand is attracted by a magnet.” is false: Sand is not attracted; iron is.  

> Why can a magnet separate iron filings from sand?

- ◻️ Iron is heavier than sand.  
  _↳ feedback if chosen: Weight is not used here; magnetism is._
- ✅ Iron is attracted by a magnet; sand is not.
- ◻️ Sand is attracted by a magnet.  
  _↳ feedback if chosen: Sand is not attracted; iron is._
- ◻️ Iron dissolves in water.  
  _↳ feedback if chosen: Iron does not dissolve in water._

Full working after a second miss:

> The true statement is “Iron is attracted by a magnet; sand is not.”.  
> “Iron is heavier than sand.” is false: Weight is not used here; magnetism is.  
> “Sand is attracted by a magnet.” is false: Sand is not attracted; iron is.  
> “Iron dissolves in water.” is false: Iron does not dissolve in water.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch14-spot` · Lesson 14 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Winnowing removes the light chaff from grain.
- ✅ Sieving separates pieces of different sizes.
- ✅ Iodine can be separated from sand by sublimation.
- ✅ Hand-picking removes stones from beans.
- ❌ A magnet separates salt from sand.  
  _↳ Neither salt nor sand is magnetic: dissolve, filter and evaporate._
- ❌ Sieving separates salt from sugar.  
  _↳ Their grains are the same size; sieving cannot separate them._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Hand-picking removes stones from beans.
- ✅ Sieving separates salt from sugar.  
  _↳ explanation: Their grains are the same size; sieving cannot separate them._
- ◻️ Winnowing removes the light chaff from grain.
- ◻️ Iodine can be separated from sand by sublimation.

Full working after a second miss:

> The wrong statement is “Sieving separates salt from sugar.”.  
> Their grains are the same size; sieving cannot separate them.  

> One sentence is wrong. Which one?

- ◻️ Winnowing removes the light chaff from grain.
- ◻️ Iodine can be separated from sand by sublimation.
- ◻️ Hand-picking removes stones from beans.
- ✅ Sieving separates salt from sugar.  
  _↳ explanation: Their grains are the same size; sieving cannot separate them._

Full working after a second miss:

> The wrong statement is “Sieving separates salt from sugar.”.  
> Their grains are the same size; sieving cannot separate them.  

> One sentence is wrong. Which one?

- ✅ A magnet separates salt from sand.  
  _↳ explanation: Neither salt nor sand is magnetic: dissolve, filter and evaporate._
- ◻️ Winnowing removes the light chaff from grain.
- ◻️ Sieving separates pieces of different sizes.
- ◻️ Iodine can be separated from sand by sublimation.

Full working after a second miss:

> The wrong statement is “A magnet separates salt from sand.”.  
> Neither salt nor sand is magnetic: dissolve, filter and evaporate.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch15-method` · Lesson 15 · multiple choice, level 1

Prompt: Which method would you use to get {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| water from settled sand in a bucket | decantation | To separate water from settled sand in a bucket, use decantation. |
| sand from muddy water | filtration | To separate sand from muddy water, use filtration. |
| salt from salt water | evaporation | To separate salt from salt water, use evaporation. |
| copper(II) sulfate crystals from its solution | crystallisation | To separate copper(II) sulfate crystals from its solution, use crystallisation. |
| pure water from salt water | simple distillation | To separate pure water from salt water, use simple distillation. |

Right answer: `{x.a}`; wrong choices: `decantation`, `filtration`, `evaporation`, `crystallisation`, `simple distillation`

- Feedback `other`: “That method gives a different product. Do you want to keep the solid, the liquid, or both?”

Three generated variants:

> Which method would you use to get copper(II) sulfate crystals from its solution?

- ◻️ evaporation  
  _↳ feedback if chosen: That method gives a different product. Do you want to keep the solid, the liquid, or both?_
- ✅ crystallisation
- ◻️ simple distillation  
  _↳ feedback if chosen: That method gives a different product. Do you want to keep the solid, the liquid, or both?_
- ◻️ decantation  
  _↳ feedback if chosen: That method gives a different product. Do you want to keep the solid, the liquid, or both?_

Full working after a second miss:

> To separate copper(II) sulfate crystals from its solution, use crystallisation.  
> Answer: crystallisation.  

> Which method would you use to get sand from muddy water?

- ✅ filtration
- ◻️ decantation  
  _↳ feedback if chosen: That method gives a different product. Do you want to keep the solid, the liquid, or both?_
- ◻️ crystallisation  
  _↳ feedback if chosen: That method gives a different product. Do you want to keep the solid, the liquid, or both?_
- ◻️ evaporation  
  _↳ feedback if chosen: That method gives a different product. Do you want to keep the solid, the liquid, or both?_

Full working after a second miss:

> To separate sand from muddy water, use filtration.  
> Answer: filtration.  

> Which method would you use to get pure water from salt water?

- ◻️ evaporation  
  _↳ feedback if chosen: That method gives a different product. Do you want to keep the solid, the liquid, or both?_
- ◻️ decantation  
  _↳ feedback if chosen: That method gives a different product. Do you want to keep the solid, the liquid, or both?_
- ◻️ filtration  
  _↳ feedback if chosen: That method gives a different product. Do you want to keep the solid, the liquid, or both?_
- ✅ simple distillation

Full working after a second miss:

> To separate pure water from salt water, use simple distillation.  
> Answer: simple distillation.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch15-match` · Lesson 15 · matching, level 1

Prompt: Match each method with how it works.

Pairs (4 shown each time):

- decantation → **let the solid settle, then pour off the liquid**
- filtration → **pass through filter paper: the solid stays (residue), the liquid passes (filtrate)**
- evaporation → **heat to drive off the liquid and keep the dissolved solid**
- crystallisation → **heat to make a hot, strong solution, then let it cool to form crystals**
- simple distillation → **boil the liquid and cool the vapour to collect the pure liquid**


Three generated variants:

> Match each method with how it works.

Right-hand side (shuffled): let the solid settle, then pour off the liquid · boil the liquid and cool the vapour to collect the pure liquid · heat to make a hot, strong solution, then let it cool to form crystals · heat to drive off the liquid and keep the dissolved solid
- decantation → **let the solid settle, then pour off the liquid**
- simple distillation → **boil the liquid and cool the vapour to collect the pure liquid**
- evaporation → **heat to drive off the liquid and keep the dissolved solid**
- crystallisation → **heat to make a hot, strong solution, then let it cool to form crystals**

Full working after a second miss:

> The right pairs are:  
> decantation → let the solid settle, then pour off the liquid  
> simple distillation → boil the liquid and cool the vapour to collect the pure liquid  
> evaporation → heat to drive off the liquid and keep the dissolved solid  
> crystallisation → heat to make a hot, strong solution, then let it cool to form crystals  

> Match each method with how it works.

Right-hand side (shuffled): boil the liquid and cool the vapour to collect the pure liquid · pass through filter paper: the solid stays (residue), the liquid passes (filtrate) · heat to drive off the liquid and keep the dissolved solid · heat to make a hot, strong solution, then let it cool to form crystals
- filtration → **pass through filter paper: the solid stays (residue), the liquid passes (filtrate)**
- simple distillation → **boil the liquid and cool the vapour to collect the pure liquid**
- evaporation → **heat to drive off the liquid and keep the dissolved solid**
- crystallisation → **heat to make a hot, strong solution, then let it cool to form crystals**

Full working after a second miss:

> The right pairs are:  
> filtration → pass through filter paper: the solid stays (residue), the liquid passes (filtrate)  
> simple distillation → boil the liquid and cool the vapour to collect the pure liquid  
> evaporation → heat to drive off the liquid and keep the dissolved solid  
> crystallisation → heat to make a hot, strong solution, then let it cool to form crystals  

> Match each method with how it works.

Right-hand side (shuffled): boil the liquid and cool the vapour to collect the pure liquid · heat to drive off the liquid and keep the dissolved solid · pass through filter paper: the solid stays (residue), the liquid passes (filtrate) · heat to make a hot, strong solution, then let it cool to form crystals
- crystallisation → **heat to make a hot, strong solution, then let it cool to form crystals**
- simple distillation → **boil the liquid and cool the vapour to collect the pure liquid**
- evaporation → **heat to drive off the liquid and keep the dissolved solid**
- filtration → **pass through filter paper: the solid stays (residue), the liquid passes (filtrate)**

Full working after a second miss:

> The right pairs are:  
> crystallisation → heat to make a hot, strong solution, then let it cool to form crystals  
> simple distillation → boil the liquid and cool the vapour to collect the pure liquid  
> evaporation → heat to drive off the liquid and keep the dissolved solid  
> filtration → pass through filter paper: the solid stays (residue), the liquid passes (filtrate)  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch15-distil` · Lesson 15 · ordering, level 2

Prompt: Put the steps of simple distillation of salt water in order.

Items in the right order:

1. Heat the salt water in a flask until it boils.
2. Steam rises into the condenser.
3. Cold water around the condenser cools the steam into liquid water.
4. Pure water (the distillate) drips into a beaker; the salt stays in the flask.


Three generated variants:

> Put the steps of simple distillation of salt water in order.

Shown as: Heat the salt water in a flask until it boils. · Pure water (the distillate) drips into a beaker; the salt stays in the flask. · Steam rises into the condenser. · Cold water around the condenser cools the steam into liquid water.
Correct order: Heat the salt water in a flask until it boils. → Steam rises into the condenser. → Cold water around the condenser cools the steam into liquid water. → Pure water (the distillate) drips into a beaker; the salt stays in the flask.

Full working after a second miss:

> The correct order is: Heat the salt water in a flask until it boils. → Steam rises into the condenser. → Cold water around the condenser cools the steam into liquid water. → Pure water (the distillate) drips into a beaker; the salt stays in the flask..  

> Put the steps of simple distillation of salt water in order.

Shown as: Steam rises into the condenser. · Heat the salt water in a flask until it boils. · Pure water (the distillate) drips into a beaker; the salt stays in the flask. · Cold water around the condenser cools the steam into liquid water.
Correct order: Heat the salt water in a flask until it boils. → Steam rises into the condenser. → Cold water around the condenser cools the steam into liquid water. → Pure water (the distillate) drips into a beaker; the salt stays in the flask.

Full working after a second miss:

> The correct order is: Heat the salt water in a flask until it boils. → Steam rises into the condenser. → Cold water around the condenser cools the steam into liquid water. → Pure water (the distillate) drips into a beaker; the salt stays in the flask..  

> Put the steps of simple distillation of salt water in order.

Shown as: Cold water around the condenser cools the steam into liquid water. · Pure water (the distillate) drips into a beaker; the salt stays in the flask. · Heat the salt water in a flask until it boils. · Steam rises into the condenser.
Correct order: Heat the salt water in a flask until it boils. → Steam rises into the condenser. → Cold water around the condenser cools the steam into liquid water. → Pure water (the distillate) drips into a beaker; the salt stays in the flask.

Full working after a second miss:

> The correct order is: Heat the salt water in a flask until it boils. → Steam rises into the condenser. → Cold water around the condenser cools the steam into liquid water. → Pure water (the distillate) drips into a beaker; the salt stays in the flask..  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch15-words` · Lesson 15 · multiple choice, level 2

Prompt: After filtering muddy water, which sentence is right?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ The mud on the paper is the residue; the clear water is the filtrate.
- ❌ The mud is the filtrate.  
  _↳ The filtrate is the liquid that passes through._
- ❌ The clear water is the residue.  
  _↳ The residue is the solid left on the paper._
- ❌ Both are distillates.  
  _↳ Distillate is the liquid collected in distillation._


Three generated variants:

> After filtering muddy water, which sentence is right?

- ◻️ The mud is the filtrate.  
  _↳ feedback if chosen: The filtrate is the liquid that passes through._
- ◻️ Both are distillates.  
  _↳ feedback if chosen: Distillate is the liquid collected in distillation._
- ✅ The mud on the paper is the residue; the clear water is the filtrate.
- ◻️ The clear water is the residue.  
  _↳ feedback if chosen: The residue is the solid left on the paper._

Full working after a second miss:

> The true statement is “The mud on the paper is the residue; the clear water is the filtrate.”.  
> “The mud is the filtrate.” is false: The filtrate is the liquid that passes through.  
> “Both are distillates.” is false: Distillate is the liquid collected in distillation.  
> “The clear water is the residue.” is false: The residue is the solid left on the paper.  

> After filtering muddy water, which sentence is right?

- ◻️ Both are distillates.  
  _↳ feedback if chosen: Distillate is the liquid collected in distillation._
- ◻️ The clear water is the residue.  
  _↳ feedback if chosen: The residue is the solid left on the paper._
- ✅ The mud on the paper is the residue; the clear water is the filtrate.
- ◻️ The mud is the filtrate.  
  _↳ feedback if chosen: The filtrate is the liquid that passes through._

Full working after a second miss:

> The true statement is “The mud on the paper is the residue; the clear water is the filtrate.”.  
> “Both are distillates.” is false: Distillate is the liquid collected in distillation.  
> “The clear water is the residue.” is false: The residue is the solid left on the paper.  
> “The mud is the filtrate.” is false: The filtrate is the liquid that passes through.  

> After filtering muddy water, which sentence is right?

- ◻️ The mud is the filtrate.  
  _↳ feedback if chosen: The filtrate is the liquid that passes through._
- ✅ The mud on the paper is the residue; the clear water is the filtrate.
- ◻️ The clear water is the residue.  
  _↳ feedback if chosen: The residue is the solid left on the paper._
- ◻️ Both are distillates.  
  _↳ feedback if chosen: Distillate is the liquid collected in distillation._

Full working after a second miss:

> The true statement is “The mud on the paper is the residue; the clear water is the filtrate.”.  
> “The mud is the filtrate.” is false: The filtrate is the liquid that passes through.  
> “The clear water is the residue.” is false: The residue is the solid left on the paper.  
> “Both are distillates.” is false: Distillate is the liquid collected in distillation.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch15-spot` · Lesson 15 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Filtration separates sand from water.
- ✅ Distillation can give pure water from salt water.
- ✅ Crystallisation gives copper(II) sulfate crystals.
- ✅ Decantation pours off a liquid above a settled solid.
- ❌ Filtration separates salt from salt water.  
  _↳ Dissolved salt passes through the filter paper: use evaporation._
- ❌ Evaporation lets you keep the water.  
  _↳ Evaporation loses the water into the air: use distillation to keep it._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Filtration separates sand from water.
- ◻️ Crystallisation gives copper(II) sulfate crystals.
- ◻️ Distillation can give pure water from salt water.
- ✅ Evaporation lets you keep the water.  
  _↳ explanation: Evaporation loses the water into the air: use distillation to keep it._

Full working after a second miss:

> The wrong statement is “Evaporation lets you keep the water.”.  
> Evaporation loses the water into the air: use distillation to keep it.  

> One sentence is wrong. Which one?

- ◻️ Crystallisation gives copper(II) sulfate crystals.
- ◻️ Filtration separates sand from water.
- ◻️ Decantation pours off a liquid above a settled solid.
- ✅ Filtration separates salt from salt water.  
  _↳ explanation: Dissolved salt passes through the filter paper: use evaporation._

Full working after a second miss:

> The wrong statement is “Filtration separates salt from salt water.”.  
> Dissolved salt passes through the filter paper: use evaporation.  

> One sentence is wrong. Which one?

- ✅ Filtration separates salt from salt water.  
  _↳ explanation: Dissolved salt passes through the filter paper: use evaporation._
- ◻️ Distillation can give pure water from salt water.
- ◻️ Decantation pours off a liquid above a settled solid.
- ◻️ Filtration separates sand from water.

Full working after a second miss:

> The wrong statement is “Filtration separates salt from salt water.”.  
> Dissolved salt passes through the filter paper: use evaporation.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `chc15-3-check` · Lesson 15 · multiple choice, level 1

Prompt: In filtration, what is the filtrate?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ the liquid that passes through the filter paper
- ❌ the solid left on the filter paper  
  _↳ That is the residue._
- ❌ the filter paper itself  
  _↳ The filtrate is the liquid that passes through._
- ❌ the steam from the liquid  
  _↳ Steam comes from distillation or evaporation, not filtration._


Three generated variants:

> In filtration, what is the filtrate?

- ✅ the liquid that passes through the filter paper
- ◻️ the steam from the liquid  
  _↳ feedback if chosen: Steam comes from distillation or evaporation, not filtration._
- ◻️ the filter paper itself  
  _↳ feedback if chosen: The filtrate is the liquid that passes through._
- ◻️ the solid left on the filter paper  
  _↳ feedback if chosen: That is the residue._

Full working after a second miss:

> The true statement is “the liquid that passes through the filter paper”.  
> “the steam from the liquid” is false: Steam comes from distillation or evaporation, not filtration.  
> “the filter paper itself” is false: The filtrate is the liquid that passes through.  
> “the solid left on the filter paper” is false: That is the residue.  

> In filtration, what is the filtrate?

- ◻️ the steam from the liquid  
  _↳ feedback if chosen: Steam comes from distillation or evaporation, not filtration._
- ✅ the liquid that passes through the filter paper
- ◻️ the solid left on the filter paper  
  _↳ feedback if chosen: That is the residue._
- ◻️ the filter paper itself  
  _↳ feedback if chosen: The filtrate is the liquid that passes through._

Full working after a second miss:

> The true statement is “the liquid that passes through the filter paper”.  
> “the steam from the liquid” is false: Steam comes from distillation or evaporation, not filtration.  
> “the solid left on the filter paper” is false: That is the residue.  
> “the filter paper itself” is false: The filtrate is the liquid that passes through.  

> In filtration, what is the filtrate?

- ◻️ the filter paper itself  
  _↳ feedback if chosen: The filtrate is the liquid that passes through._
- ✅ the liquid that passes through the filter paper
- ◻️ the solid left on the filter paper  
  _↳ feedback if chosen: That is the residue._
- ◻️ the steam from the liquid  
  _↳ feedback if chosen: Steam comes from distillation or evaporation, not filtration._

Full working after a second miss:

> The true statement is “the liquid that passes through the filter paper”.  
> “the filter paper itself” is false: The filtrate is the liquid that passes through.  
> “the solid left on the filter paper” is false: That is the residue.  
> “the steam from the liquid” is false: Steam comes from distillation or evaporation, not filtration.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch16-method` · Lesson 16 · multiple choice, level 1

Prompt: Which method separates {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| palm oil and water | separating funnel | palm oil and water: separating funnel. |
| kerosene and water | separating funnel | kerosene and water: separating funnel. |
| ethanol and water | fractional distillation | ethanol and water: fractional distillation. |
| petrol and kerosene from crude oil | fractional distillation | petrol and kerosene from crude oil: fractional distillation. |

Right answer: `{x.a}`; wrong choices: `separating funnel`, `fractional distillation`, `filtration`, `sieving`

- Feedback `other`: “Ask: do the liquids form layers (separating funnel) or mix completely (fractional distillation)?”

Three generated variants:

> Which method separates petrol and kerosene from crude oil?

- ✅ fractional distillation
- ◻️ filtration  
  _↳ feedback if chosen: Ask: do the liquids form layers (separating funnel) or mix completely (fractional distillation)?_
- ◻️ separating funnel  
  _↳ feedback if chosen: Ask: do the liquids form layers (separating funnel) or mix completely (fractional distillation)?_
- ◻️ sieving  
  _↳ feedback if chosen: Ask: do the liquids form layers (separating funnel) or mix completely (fractional distillation)?_

Full working after a second miss:

> petrol and kerosene from crude oil: fractional distillation.  
> Answer: fractional distillation.  

> Which method separates petrol and kerosene from crude oil?

- ◻️ filtration  
  _↳ feedback if chosen: Ask: do the liquids form layers (separating funnel) or mix completely (fractional distillation)?_
- ◻️ separating funnel  
  _↳ feedback if chosen: Ask: do the liquids form layers (separating funnel) or mix completely (fractional distillation)?_
- ✅ fractional distillation
- ◻️ sieving  
  _↳ feedback if chosen: Ask: do the liquids form layers (separating funnel) or mix completely (fractional distillation)?_

Full working after a second miss:

> petrol and kerosene from crude oil: fractional distillation.  
> Answer: fractional distillation.  

> Which method separates ethanol and water?

- ✅ fractional distillation
- ◻️ filtration  
  _↳ feedback if chosen: Ask: do the liquids form layers (separating funnel) or mix completely (fractional distillation)?_
- ◻️ sieving  
  _↳ feedback if chosen: Ask: do the liquids form layers (separating funnel) or mix completely (fractional distillation)?_
- ◻️ separating funnel  
  _↳ feedback if chosen: Ask: do the liquids form layers (separating funnel) or mix completely (fractional distillation)?_

Full working after a second miss:

> ethanol and water: fractional distillation.  
> Answer: fractional distillation.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch16-funnel` · Lesson 16 · ordering, level 2

Prompt: Put the steps for using a separating funnel in order.

Items in the right order:

1. Pour the mixture into the separating funnel.
2. Wait until two layers form.
3. Open the tap and run off the bottom layer into a beaker.
4. Close the tap when the top layer reaches it.
5. Pour the top layer out into another beaker.


Three generated variants:

> Put the steps for using a separating funnel in order.

Shown as: Open the tap and run off the bottom layer into a beaker. · Pour the top layer out into another beaker. · Pour the mixture into the separating funnel. · Close the tap when the top layer reaches it. · Wait until two layers form.
Correct order: Pour the mixture into the separating funnel. → Wait until two layers form. → Open the tap and run off the bottom layer into a beaker. → Close the tap when the top layer reaches it. → Pour the top layer out into another beaker.

Full working after a second miss:

> The correct order is: Pour the mixture into the separating funnel. → Wait until two layers form. → Open the tap and run off the bottom layer into a beaker. → Close the tap when the top layer reaches it. → Pour the top layer out into another beaker..  

> Put the steps for using a separating funnel in order.

Shown as: Pour the top layer out into another beaker. · Pour the mixture into the separating funnel. · Close the tap when the top layer reaches it. · Wait until two layers form. · Open the tap and run off the bottom layer into a beaker.
Correct order: Pour the mixture into the separating funnel. → Wait until two layers form. → Open the tap and run off the bottom layer into a beaker. → Close the tap when the top layer reaches it. → Pour the top layer out into another beaker.

Full working after a second miss:

> The correct order is: Pour the mixture into the separating funnel. → Wait until two layers form. → Open the tap and run off the bottom layer into a beaker. → Close the tap when the top layer reaches it. → Pour the top layer out into another beaker..  

> Put the steps for using a separating funnel in order.

Shown as: Close the tap when the top layer reaches it. · Pour the top layer out into another beaker. · Pour the mixture into the separating funnel. · Open the tap and run off the bottom layer into a beaker. · Wait until two layers form.
Correct order: Pour the mixture into the separating funnel. → Wait until two layers form. → Open the tap and run off the bottom layer into a beaker. → Close the tap when the top layer reaches it. → Pour the top layer out into another beaker.

Full working after a second miss:

> The correct order is: Pour the mixture into the separating funnel. → Wait until two layers form. → Open the tap and run off the bottom layer into a beaker. → Close the tap when the top layer reaches it. → Pour the top layer out into another beaker..  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch16-spot` · Lesson 16 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Palm oil and water can be separated with a separating funnel.
- ✅ Ethanol boils at a lower temperature than water.
- ✅ Crude oil is separated by fractional distillation.
- ✅ Miscible liquids mix completely.
- ❌ Ethanol and water are separated with a separating funnel.  
  _↳ They mix completely: use fractional distillation._
- ❌ In fractional distillation the liquid with the higher boiling point comes over first.  
  _↳ The lower boiling point comes over first._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Miscible liquids mix completely.
- ◻️ Palm oil and water can be separated with a separating funnel.
- ◻️ Ethanol boils at a lower temperature than water.
- ✅ In fractional distillation the liquid with the higher boiling point comes over first.  
  _↳ explanation: The lower boiling point comes over first._

Full working after a second miss:

> The wrong statement is “In fractional distillation the liquid with the higher boiling point comes over first.”.  
> The lower boiling point comes over first.  

> One sentence is wrong. Which one?

- ◻️ Miscible liquids mix completely.
- ✅ In fractional distillation the liquid with the higher boiling point comes over first.  
  _↳ explanation: The lower boiling point comes over first._
- ◻️ Crude oil is separated by fractional distillation.
- ◻️ Ethanol boils at a lower temperature than water.

Full working after a second miss:

> The wrong statement is “In fractional distillation the liquid with the higher boiling point comes over first.”.  
> The lower boiling point comes over first.  

> One sentence is wrong. Which one?

- ✅ In fractional distillation the liquid with the higher boiling point comes over first.  
  _↳ explanation: The lower boiling point comes over first._
- ◻️ Palm oil and water can be separated with a separating funnel.
- ◻️ Ethanol boils at a lower temperature than water.
- ◻️ Miscible liquids mix completely.

Full working after a second miss:

> The wrong statement is “In fractional distillation the liquid with the higher boiling point comes over first.”.  
> The lower boiling point comes over first.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `chc16-3-check` · Lesson 16 · multiple choice, level 1

Prompt: Which method separates ethanol from water?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ fractional distillation
- ❌ a separating funnel  
  _↳ Ethanol and water mix completely: they do not form layers._
- ❌ filtration  
  _↳ Filtration removes undissolved solids._
- ❌ magnetic separation  
  _↳ A magnet only attracts iron and some metals._


Three generated variants:

> Which method separates ethanol from water?

- ◻️ filtration  
  _↳ feedback if chosen: Filtration removes undissolved solids._
- ◻️ a separating funnel  
  _↳ feedback if chosen: Ethanol and water mix completely: they do not form layers._
- ◻️ magnetic separation  
  _↳ feedback if chosen: A magnet only attracts iron and some metals._
- ✅ fractional distillation

Full working after a second miss:

> The true statement is “fractional distillation”.  
> “filtration” is false: Filtration removes undissolved solids.  
> “a separating funnel” is false: Ethanol and water mix completely: they do not form layers.  
> “magnetic separation” is false: A magnet only attracts iron and some metals.  

> Which method separates ethanol from water?

- ◻️ a separating funnel  
  _↳ feedback if chosen: Ethanol and water mix completely: they do not form layers._
- ◻️ magnetic separation  
  _↳ feedback if chosen: A magnet only attracts iron and some metals._
- ✅ fractional distillation
- ◻️ filtration  
  _↳ feedback if chosen: Filtration removes undissolved solids._

Full working after a second miss:

> The true statement is “fractional distillation”.  
> “a separating funnel” is false: Ethanol and water mix completely: they do not form layers.  
> “magnetic separation” is false: A magnet only attracts iron and some metals.  
> “filtration” is false: Filtration removes undissolved solids.  

> Which method separates ethanol from water?

- ◻️ magnetic separation  
  _↳ feedback if chosen: A magnet only attracts iron and some metals._
- ✅ fractional distillation
- ◻️ filtration  
  _↳ feedback if chosen: Filtration removes undissolved solids._
- ◻️ a separating funnel  
  _↳ feedback if chosen: Ethanol and water mix completely: they do not form layers._

Full working after a second miss:

> The true statement is “fractional distillation”.  
> “magnetic separation” is false: A magnet only attracts iron and some metals.  
> “filtration” is false: Filtration removes undissolved solids.  
> “a separating funnel” is false: Ethanol and water mix completely: they do not form layers.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch17-which` · Lesson 17 · multiple choice, level 1

Prompt: Which of these is a mixture of a gas dissolved in a liquid?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ a soft drink
- ✅ river water with oxygen in it
- ❌ sand and salt  
  _↳ That is solid–solid._
- ❌ palm oil and water  
  _↳ That is liquid–liquid._
- ❌ air  
  _↳ That is gas–gas._


Three generated variants:

> Which of these is a mixture of a gas dissolved in a liquid?

- ◻️ sand and salt  
  _↳ feedback if chosen: That is solid–solid._
- ✅ a soft drink
- ◻️ air  
  _↳ feedback if chosen: That is gas–gas._
- ◻️ palm oil and water  
  _↳ feedback if chosen: That is liquid–liquid._

Full working after a second miss:

> The true statement is “a soft drink”.  
> “sand and salt” is false: That is solid–solid.  
> “air” is false: That is gas–gas.  
> “palm oil and water” is false: That is liquid–liquid.  

> Which of these is a mixture of a gas dissolved in a liquid?

- ✅ river water with oxygen in it
- ◻️ palm oil and water  
  _↳ feedback if chosen: That is liquid–liquid._
- ◻️ air  
  _↳ feedback if chosen: That is gas–gas._
- ◻️ sand and salt  
  _↳ feedback if chosen: That is solid–solid._

Full working after a second miss:

> The true statement is “river water with oxygen in it”.  
> “palm oil and water” is false: That is liquid–liquid.  
> “air” is false: That is gas–gas.  
> “sand and salt” is false: That is solid–solid.  

> Which of these is a mixture of a gas dissolved in a liquid?

- ◻️ palm oil and water  
  _↳ feedback if chosen: That is liquid–liquid._
- ◻️ air  
  _↳ feedback if chosen: That is gas–gas._
- ◻️ sand and salt  
  _↳ feedback if chosen: That is solid–solid._
- ✅ river water with oxygen in it

Full working after a second miss:

> The true statement is “river water with oxygen in it”.  
> “palm oil and water” is false: That is liquid–liquid.  
> “air” is false: That is gas–gas.  
> “sand and salt” is false: That is solid–solid.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch17-heat` · Lesson 17 · multiple choice, level 1

Prompt: How can you remove the dissolved gas from a glass of soft drink?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Warm it gently and stir it.
- ❌ Put it in the fridge.  
  _↳ Cold liquid holds more gas, not less._
- ❌ Add more sugar.  
  _↳ Sugar does not remove the gas._
- ❌ Filter it.  
  _↳ A filter cannot hold back a dissolved gas._


Three generated variants:

> How can you remove the dissolved gas from a glass of soft drink?

- ◻️ Add more sugar.  
  _↳ feedback if chosen: Sugar does not remove the gas._
- ✅ Warm it gently and stir it.
- ◻️ Filter it.  
  _↳ feedback if chosen: A filter cannot hold back a dissolved gas._
- ◻️ Put it in the fridge.  
  _↳ feedback if chosen: Cold liquid holds more gas, not less._

Full working after a second miss:

> The true statement is “Warm it gently and stir it.”.  
> “Add more sugar.” is false: Sugar does not remove the gas.  
> “Filter it.” is false: A filter cannot hold back a dissolved gas.  
> “Put it in the fridge.” is false: Cold liquid holds more gas, not less.  

> How can you remove the dissolved gas from a glass of soft drink?

- ◻️ Put it in the fridge.  
  _↳ feedback if chosen: Cold liquid holds more gas, not less._
- ◻️ Add more sugar.  
  _↳ feedback if chosen: Sugar does not remove the gas._
- ✅ Warm it gently and stir it.
- ◻️ Filter it.  
  _↳ feedback if chosen: A filter cannot hold back a dissolved gas._

Full working after a second miss:

> The true statement is “Warm it gently and stir it.”.  
> “Put it in the fridge.” is false: Cold liquid holds more gas, not less.  
> “Add more sugar.” is false: Sugar does not remove the gas.  
> “Filter it.” is false: A filter cannot hold back a dissolved gas.  

> How can you remove the dissolved gas from a glass of soft drink?

- ◻️ Put it in the fridge.  
  _↳ feedback if chosen: Cold liquid holds more gas, not less._
- ◻️ Add more sugar.  
  _↳ feedback if chosen: Sugar does not remove the gas._
- ✅ Warm it gently and stir it.
- ◻️ Filter it.  
  _↳ feedback if chosen: A filter cannot hold back a dissolved gas._

Full working after a second miss:

> The true statement is “Warm it gently and stir it.”.  
> “Put it in the fridge.” is false: Cold liquid holds more gas, not less.  
> “Add more sugar.” is false: Sugar does not remove the gas.  
> “Filter it.” is false: A filter cannot hold back a dissolved gas.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch17-fish` · Lesson 17 · multiple choice, level 2

Prompt: In the dry season, a fish pond becomes very warm. Why can this harm the fish?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Warm water holds less dissolved oxygen, so the fish have less to breathe.
- ❌ Warm water has more oxygen, which is poisonous.  
  _↳ Warm water holds less oxygen, not more._
- ❌ The fish get sunburnt.  
  _↳ The main problem is less dissolved oxygen._
- ❌ Warm water turns into carbon dioxide.  
  _↳ Water does not turn into carbon dioxide._


Three generated variants:

> In the dry season, a fish pond becomes very warm. Why can this harm the fish?

- ◻️ Warm water turns into carbon dioxide.  
  _↳ feedback if chosen: Water does not turn into carbon dioxide._
- ◻️ Warm water has more oxygen, which is poisonous.  
  _↳ feedback if chosen: Warm water holds less oxygen, not more._
- ✅ Warm water holds less dissolved oxygen, so the fish have less to breathe.
- ◻️ The fish get sunburnt.  
  _↳ feedback if chosen: The main problem is less dissolved oxygen._

Full working after a second miss:

> The true statement is “Warm water holds less dissolved oxygen, so the fish have less to breathe.”.  
> “Warm water turns into carbon dioxide.” is false: Water does not turn into carbon dioxide.  
> “Warm water has more oxygen, which is poisonous.” is false: Warm water holds less oxygen, not more.  
> “The fish get sunburnt.” is false: The main problem is less dissolved oxygen.  

> In the dry season, a fish pond becomes very warm. Why can this harm the fish?

- ◻️ The fish get sunburnt.  
  _↳ feedback if chosen: The main problem is less dissolved oxygen._
- ◻️ Warm water has more oxygen, which is poisonous.  
  _↳ feedback if chosen: Warm water holds less oxygen, not more._
- ✅ Warm water holds less dissolved oxygen, so the fish have less to breathe.
- ◻️ Warm water turns into carbon dioxide.  
  _↳ feedback if chosen: Water does not turn into carbon dioxide._

Full working after a second miss:

> The true statement is “Warm water holds less dissolved oxygen, so the fish have less to breathe.”.  
> “The fish get sunburnt.” is false: The main problem is less dissolved oxygen.  
> “Warm water has more oxygen, which is poisonous.” is false: Warm water holds less oxygen, not more.  
> “Warm water turns into carbon dioxide.” is false: Water does not turn into carbon dioxide.  

> In the dry season, a fish pond becomes very warm. Why can this harm the fish?

- ◻️ Warm water turns into carbon dioxide.  
  _↳ feedback if chosen: Water does not turn into carbon dioxide._
- ✅ Warm water holds less dissolved oxygen, so the fish have less to breathe.
- ◻️ Warm water has more oxygen, which is poisonous.  
  _↳ feedback if chosen: Warm water holds less oxygen, not more._
- ◻️ The fish get sunburnt.  
  _↳ feedback if chosen: The main problem is less dissolved oxygen._

Full working after a second miss:

> The true statement is “Warm water holds less dissolved oxygen, so the fish have less to breathe.”.  
> “Warm water turns into carbon dioxide.” is false: Water does not turn into carbon dioxide.  
> “Warm water has more oxygen, which is poisonous.” is false: Warm water holds less oxygen, not more.  
> “The fish get sunburnt.” is false: The main problem is less dissolved oxygen.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch17-spot` · Lesson 17 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Opening a soft drink lowers the pressure.
- ✅ Fish breathe oxygen dissolved in water.
- ✅ A dissolved gas can be collected over water.
- ✅ Warm water holds less dissolved gas than cold water.
- ❌ Cold water holds less dissolved gas than warm water.  
  _↳ It is the other way round: cold water holds more gas._
- ❌ Filtering removes dissolved gas from a drink.  
  _↳ A filter cannot stop a dissolved gas._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Opening a soft drink lowers the pressure.
- ✅ Cold water holds less dissolved gas than warm water.  
  _↳ explanation: It is the other way round: cold water holds more gas._
- ◻️ A dissolved gas can be collected over water.
- ◻️ Fish breathe oxygen dissolved in water.

Full working after a second miss:

> The wrong statement is “Cold water holds less dissolved gas than warm water.”.  
> It is the other way round: cold water holds more gas.  

> One sentence is wrong. Which one?

- ✅ Cold water holds less dissolved gas than warm water.  
  _↳ explanation: It is the other way round: cold water holds more gas._
- ◻️ Fish breathe oxygen dissolved in water.
- ◻️ Opening a soft drink lowers the pressure.
- ◻️ Warm water holds less dissolved gas than cold water.

Full working after a second miss:

> The wrong statement is “Cold water holds less dissolved gas than warm water.”.  
> It is the other way round: cold water holds more gas.  

> One sentence is wrong. Which one?

- ◻️ Opening a soft drink lowers the pressure.
- ◻️ Fish breathe oxygen dissolved in water.
- ◻️ A dissolved gas can be collected over water.
- ✅ Cold water holds less dissolved gas than warm water.  
  _↳ explanation: It is the other way round: cold water holds more gas._

Full working after a second miss:

> The wrong statement is “Cold water holds less dissolved gas than warm water.”.  
> It is the other way round: cold water holds more gas.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `chc17-3-check` · Lesson 17 · multiple choice, level 1

Prompt: Why does a soft drink fizz when the bottle is opened?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ The pressure drops, so the dissolved carbon dioxide comes out.
- ❌ The drink starts to boil.  
  _↳ It does not boil; the dissolved gas escapes._
- ❌ Air rushes into the drink.  
  _↳ The bubbles are carbon dioxide coming out of the drink._
- ❌ The sugar turns into gas.  
  _↳ The gas was already dissolved: it is carbon dioxide._


Three generated variants:

> Why does a soft drink fizz when the bottle is opened?

- ◻️ Air rushes into the drink.  
  _↳ feedback if chosen: The bubbles are carbon dioxide coming out of the drink._
- ◻️ The sugar turns into gas.  
  _↳ feedback if chosen: The gas was already dissolved: it is carbon dioxide._
- ✅ The pressure drops, so the dissolved carbon dioxide comes out.
- ◻️ The drink starts to boil.  
  _↳ feedback if chosen: It does not boil; the dissolved gas escapes._

Full working after a second miss:

> The true statement is “The pressure drops, so the dissolved carbon dioxide comes out.”.  
> “Air rushes into the drink.” is false: The bubbles are carbon dioxide coming out of the drink.  
> “The sugar turns into gas.” is false: The gas was already dissolved: it is carbon dioxide.  
> “The drink starts to boil.” is false: It does not boil; the dissolved gas escapes.  

> Why does a soft drink fizz when the bottle is opened?

- ✅ The pressure drops, so the dissolved carbon dioxide comes out.
- ◻️ The drink starts to boil.  
  _↳ feedback if chosen: It does not boil; the dissolved gas escapes._
- ◻️ The sugar turns into gas.  
  _↳ feedback if chosen: The gas was already dissolved: it is carbon dioxide._
- ◻️ Air rushes into the drink.  
  _↳ feedback if chosen: The bubbles are carbon dioxide coming out of the drink._

Full working after a second miss:

> The true statement is “The pressure drops, so the dissolved carbon dioxide comes out.”.  
> “The drink starts to boil.” is false: It does not boil; the dissolved gas escapes.  
> “The sugar turns into gas.” is false: The gas was already dissolved: it is carbon dioxide.  
> “Air rushes into the drink.” is false: The bubbles are carbon dioxide coming out of the drink.  

> Why does a soft drink fizz when the bottle is opened?

- ◻️ The drink starts to boil.  
  _↳ feedback if chosen: It does not boil; the dissolved gas escapes._
- ◻️ The sugar turns into gas.  
  _↳ feedback if chosen: The gas was already dissolved: it is carbon dioxide._
- ◻️ Air rushes into the drink.  
  _↳ feedback if chosen: The bubbles are carbon dioxide coming out of the drink._
- ✅ The pressure drops, so the dissolved carbon dioxide comes out.

Full working after a second miss:

> The true statement is “The pressure drops, so the dissolved carbon dioxide comes out.”.  
> “The drink starts to boil.” is false: It does not boil; the dissolved gas escapes.  
> “The sugar turns into gas.” is false: The gas was already dissolved: it is carbon dioxide.  
> “Air rushes into the drink.” is false: The bubbles are carbon dioxide coming out of the drink.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch18-air` · Lesson 18 · multiple choice, level 1

Prompt: Which gas makes up the largest part of the air?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ nitrogen
- ❌ oxygen  
  _↳ Oxygen is about 21 %; nitrogen is about 78 %._
- ❌ carbon dioxide  
  _↳ Carbon dioxide is only a tiny part of the air._
- ❌ argon  
  _↳ Argon is almost 1 % of the air._


Three generated variants:

> Which gas makes up the largest part of the air?

- ✅ nitrogen
- ◻️ argon  
  _↳ feedback if chosen: Argon is almost 1 % of the air._
- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen is about 21 %; nitrogen is about 78 %._
- ◻️ carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide is only a tiny part of the air._

Full working after a second miss:

> The true statement is “nitrogen”.  
> “argon” is false: Argon is almost 1 % of the air.  
> “oxygen” is false: Oxygen is about 21 %; nitrogen is about 78 %.  
> “carbon dioxide” is false: Carbon dioxide is only a tiny part of the air.  

> Which gas makes up the largest part of the air?

- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen is about 21 %; nitrogen is about 78 %._
- ◻️ carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide is only a tiny part of the air._
- ◻️ argon  
  _↳ feedback if chosen: Argon is almost 1 % of the air._
- ✅ nitrogen

Full working after a second miss:

> The true statement is “nitrogen”.  
> “oxygen” is false: Oxygen is about 21 %; nitrogen is about 78 %.  
> “carbon dioxide” is false: Carbon dioxide is only a tiny part of the air.  
> “argon” is false: Argon is almost 1 % of the air.  

> Which gas makes up the largest part of the air?

- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen is about 21 %; nitrogen is about 78 %._
- ◻️ argon  
  _↳ feedback if chosen: Argon is almost 1 % of the air._
- ✅ nitrogen
- ◻️ carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide is only a tiny part of the air._

Full working after a second miss:

> The true statement is “nitrogen”.  
> “oxygen” is false: Oxygen is about 21 %; nitrogen is about 78 %.  
> “argon” is false: Argon is almost 1 % of the air.  
> “carbon dioxide” is false: Carbon dioxide is only a tiny part of the air.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch18-method` · Lesson 18 · multiple choice, level 1

Prompt: Which method would you use to {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| get pure oxygen and nitrogen from air in a factory | fractional distillation of liquid air | To get pure oxygen and nitrogen from air in a factory: fractional distillation of liquid air. |
| remove carbon dioxide from a sample of air | absorption in sodium hydroxide solution | To remove carbon dioxide from a sample of air: absorption in sodium hydroxide solution. |

Right answer: `{x.a}`; wrong choices: `fractional distillation of liquid air`, `absorption in sodium hydroxide solution`, `filtration`, `a separating funnel`

- Feedback `other`: “Think: is it many gases separated by boiling point, or one gas taken out by a liquid?”

Three generated variants:

> Which method would you use to get pure oxygen and nitrogen from air in a factory?

- ◻️ a separating funnel  
  _↳ feedback if chosen: Think: is it many gases separated by boiling point, or one gas taken out by a liquid?_
- ✅ fractional distillation of liquid air
- ◻️ absorption in sodium hydroxide solution  
  _↳ feedback if chosen: Think: is it many gases separated by boiling point, or one gas taken out by a liquid?_

Full working after a second miss:

> To get pure oxygen and nitrogen from air in a factory: fractional distillation of liquid air.  
> Answer: fractional distillation of liquid air.  

> Which method would you use to get pure oxygen and nitrogen from air in a factory?

- ◻️ a separating funnel  
  _↳ feedback if chosen: Think: is it many gases separated by boiling point, or one gas taken out by a liquid?_
- ✅ fractional distillation of liquid air
- ◻️ filtration  
  _↳ feedback if chosen: Think: is it many gases separated by boiling point, or one gas taken out by a liquid?_

Full working after a second miss:

> To get pure oxygen and nitrogen from air in a factory: fractional distillation of liquid air.  
> Answer: fractional distillation of liquid air.  

> Which method would you use to get pure oxygen and nitrogen from air in a factory?

- ◻️ absorption in sodium hydroxide solution  
  _↳ feedback if chosen: Think: is it many gases separated by boiling point, or one gas taken out by a liquid?_
- ✅ fractional distillation of liquid air
- ◻️ a separating funnel  
  _↳ feedback if chosen: Think: is it many gases separated by boiling point, or one gas taken out by a liquid?_

Full working after a second miss:

> To get pure oxygen and nitrogen from air in a factory: fractional distillation of liquid air.  
> Answer: fractional distillation of liquid air.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch18-why` · Lesson 18 · multiple choice, level 2

Prompt: Why does fractional distillation of liquid air work?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Each gas in the air has a different boiling point.
- ❌ Each gas has a different colour.  
  _↳ The gases are colourless; boiling points are used._
- ❌ Oxygen is magnetic.  
  _↳ That is not how fractional distillation works._
- ❌ Nitrogen dissolves in water.  
  _↳ Fractional distillation uses boiling points._


Three generated variants:

> Why does fractional distillation of liquid air work?

- ◻️ Oxygen is magnetic.  
  _↳ feedback if chosen: That is not how fractional distillation works._
- ◻️ Each gas has a different colour.  
  _↳ feedback if chosen: The gases are colourless; boiling points are used._
- ◻️ Nitrogen dissolves in water.  
  _↳ feedback if chosen: Fractional distillation uses boiling points._
- ✅ Each gas in the air has a different boiling point.

Full working after a second miss:

> The true statement is “Each gas in the air has a different boiling point.”.  
> “Oxygen is magnetic.” is false: That is not how fractional distillation works.  
> “Each gas has a different colour.” is false: The gases are colourless; boiling points are used.  
> “Nitrogen dissolves in water.” is false: Fractional distillation uses boiling points.  

> Why does fractional distillation of liquid air work?

- ◻️ Oxygen is magnetic.  
  _↳ feedback if chosen: That is not how fractional distillation works._
- ◻️ Nitrogen dissolves in water.  
  _↳ feedback if chosen: Fractional distillation uses boiling points._
- ◻️ Each gas has a different colour.  
  _↳ feedback if chosen: The gases are colourless; boiling points are used._
- ✅ Each gas in the air has a different boiling point.

Full working after a second miss:

> The true statement is “Each gas in the air has a different boiling point.”.  
> “Oxygen is magnetic.” is false: That is not how fractional distillation works.  
> “Nitrogen dissolves in water.” is false: Fractional distillation uses boiling points.  
> “Each gas has a different colour.” is false: The gases are colourless; boiling points are used.  

> Why does fractional distillation of liquid air work?

- ◻️ Oxygen is magnetic.  
  _↳ feedback if chosen: That is not how fractional distillation works._
- ◻️ Each gas has a different colour.  
  _↳ feedback if chosen: The gases are colourless; boiling points are used._
- ◻️ Nitrogen dissolves in water.  
  _↳ feedback if chosen: Fractional distillation uses boiling points._
- ✅ Each gas in the air has a different boiling point.

Full working after a second miss:

> The true statement is “Each gas in the air has a different boiling point.”.  
> “Oxygen is magnetic.” is false: That is not how fractional distillation works.  
> “Each gas has a different colour.” is false: The gases are colourless; boiling points are used.  
> “Nitrogen dissolves in water.” is false: Fractional distillation uses boiling points.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch18-spot` · Lesson 18 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Air is a mixture of gases.
- ✅ Sodium hydroxide solution absorbs carbon dioxide.
- ✅ Oxygen for hospitals comes from liquid air.
- ✅ Nitrogen is the largest part of the air.
- ❌ Air is a pure substance.  
  _↳ Air contains several gases that are not joined: it is a mixture._
- ❌ Oxygen makes up most of the air.  
  _↳ Nitrogen (about 78 %) makes up most of the air._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Air is a mixture of gases.
- ◻️ Sodium hydroxide solution absorbs carbon dioxide.
- ◻️ Nitrogen is the largest part of the air.
- ✅ Oxygen makes up most of the air.  
  _↳ explanation: Nitrogen (about 78 %) makes up most of the air._

Full working after a second miss:

> The wrong statement is “Oxygen makes up most of the air.”.  
> Nitrogen (about 78 %) makes up most of the air.  

> One sentence is wrong. Which one?

- ◻️ Oxygen for hospitals comes from liquid air.
- ◻️ Air is a mixture of gases.
- ✅ Air is a pure substance.  
  _↳ explanation: Air contains several gases that are not joined: it is a mixture._
- ◻️ Nitrogen is the largest part of the air.

Full working after a second miss:

> The wrong statement is “Air is a pure substance.”.  
> Air contains several gases that are not joined: it is a mixture.  

> One sentence is wrong. Which one?

- ◻️ Sodium hydroxide solution absorbs carbon dioxide.
- ◻️ Oxygen for hospitals comes from liquid air.
- ◻️ Nitrogen is the largest part of the air.
- ✅ Air is a pure substance.  
  _↳ explanation: Air contains several gases that are not joined: it is a mixture._

Full working after a second miss:

> The wrong statement is “Air is a pure substance.”.  
> Air contains several gases that are not joined: it is a mixture.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `chc18-3-check` · Lesson 18 · multiple choice, level 1

Prompt: Which liquid absorbs carbon dioxide from air?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ sodium hydroxide solution
- ❌ pure water only  
  _↳ Water dissolves only a little carbon dioxide._
- ❌ kerosene  
  _↳ Kerosene is not used to absorb carbon dioxide._
- ❌ palm oil  
  _↳ Palm oil does not absorb carbon dioxide._


Three generated variants:

> Which liquid absorbs carbon dioxide from air?

- ◻️ kerosene  
  _↳ feedback if chosen: Kerosene is not used to absorb carbon dioxide._
- ◻️ pure water only  
  _↳ feedback if chosen: Water dissolves only a little carbon dioxide._
- ◻️ palm oil  
  _↳ feedback if chosen: Palm oil does not absorb carbon dioxide._
- ✅ sodium hydroxide solution

Full working after a second miss:

> The true statement is “sodium hydroxide solution”.  
> “kerosene” is false: Kerosene is not used to absorb carbon dioxide.  
> “pure water only” is false: Water dissolves only a little carbon dioxide.  
> “palm oil” is false: Palm oil does not absorb carbon dioxide.  

> Which liquid absorbs carbon dioxide from air?

- ✅ sodium hydroxide solution
- ◻️ kerosene  
  _↳ feedback if chosen: Kerosene is not used to absorb carbon dioxide._
- ◻️ pure water only  
  _↳ feedback if chosen: Water dissolves only a little carbon dioxide._
- ◻️ palm oil  
  _↳ feedback if chosen: Palm oil does not absorb carbon dioxide._

Full working after a second miss:

> The true statement is “sodium hydroxide solution”.  
> “kerosene” is false: Kerosene is not used to absorb carbon dioxide.  
> “pure water only” is false: Water dissolves only a little carbon dioxide.  
> “palm oil” is false: Palm oil does not absorb carbon dioxide.  

> Which liquid absorbs carbon dioxide from air?

- ◻️ pure water only  
  _↳ feedback if chosen: Water dissolves only a little carbon dioxide._
- ◻️ palm oil  
  _↳ feedback if chosen: Palm oil does not absorb carbon dioxide._
- ◻️ kerosene  
  _↳ feedback if chosen: Kerosene is not used to absorb carbon dioxide._
- ✅ sodium hydroxide solution

Full working after a second miss:

> The true statement is “sodium hydroxide solution”.  
> “pure water only” is false: Water dissolves only a little carbon dioxide.  
> “palm oil” is false: Palm oil does not absorb carbon dioxide.  
> “kerosene” is false: Kerosene is not used to absorb carbon dioxide.  

Sources: separation (Separation methods (hand-picking, sieving, magnet, winnowing, sublimation, decantation, filtration, evaporation, crystallisation, distillation, separating funnel, fractional distillation, absorption); composition of air)

### `ch19-match` · Lesson 19 · matching, level 1

Prompt: Match each element with its symbol.

Pairs (4 shown each time):

- hydrogen → **H**
- helium → **He**
- carbon → **C**
- nitrogen → **N**
- oxygen → **O**
- sodium → **Na**
- magnesium → **Mg**
- aluminium → **Al**
- sulfur → **S**
- chlorine → **Cl**
- potassium → **K**
- calcium → **Ca**
- iron → **Fe**
- copper → **Cu**
- zinc → **Zn**
- silver → **Ag**
- gold → **Au**
- lead → **Pb**


Three generated variants:

> Match each element with its symbol.

Right-hand side (shuffled): Ca · Na · Cu · Fe
- copper → **Cu**
- sodium → **Na**
- calcium → **Ca**
- iron → **Fe**

Full working after a second miss:

> The right pairs are:  
> copper → Cu  
> sodium → Na  
> calcium → Ca  
> iron → Fe  

> Match each element with its symbol.

Right-hand side (shuffled): Ag · Fe · Cu · Na
- silver → **Ag**
- iron → **Fe**
- sodium → **Na**
- copper → **Cu**

Full working after a second miss:

> The right pairs are:  
> silver → Ag  
> iron → Fe  
> sodium → Na  
> copper → Cu  

> Match each element with its symbol.

Right-hand side (shuffled): K · Au · Cu · C
- copper → **Cu**
- carbon → **C**
- gold → **Au**
- potassium → **K**

Full working after a second miss:

> The right pairs are:  
> copper → Cu  
> carbon → C  
> gold → Au  
> potassium → K  

Sources: elements (Elements and symbols (IUPAC); British spellings aluminium and sulfur; Latin origins of Na, K, Fe, Cu, Ag, Sn, Au, Hg, Pb)

### `ch19-symbol` · Lesson 19 · multiple choice, level 1

Prompt: What is the symbol for {nameOf(s)}?

`s`: H · He · C · N · O · Na · Mg · Al · S · Cl · K · Ca · Fe · Cu · Zn · Ag · Au · Pb

Right answer: `{s}`; wrong choices: `{upper(s)}`, `{lowerAll(s)}`, `{upper(lowerAll(nameOf(s))[0])}{lowerAll(nameOf(s))[1]}`, `{upper(lowerAll(nameOf(s))[0])}`

- Feedback `case`: “A symbol starts with a capital letter; a second letter is always small.”
- Feedback `first-two`: “Not always the first two letters: some symbols come from Latin names or use another letter.”
- Feedback `first`: “Several elements start with the same letter, so many symbols need a second letter.”

Three generated variants:

> What is the symbol for copper?

- ◻️ cu  
  _↳ feedback if chosen: A symbol starts with a capital letter; a second letter is always small._
- ✅ Cu
- ◻️ CU  
  _↳ feedback if chosen: A symbol starts with a capital letter; a second letter is always small._

Full working after a second miss:

> copper: Cu.  

> What is the symbol for copper?

- ✅ Cu
- ◻️ Co  
  _↳ feedback if chosen: Not always the first two letters: some symbols come from Latin names or use another letter._
- ◻️ C  
  _↳ feedback if chosen: Several elements start with the same letter, so many symbols need a second letter._

Full working after a second miss:

> copper: Cu.  

> What is the symbol for hydrogen?

- ◻️ h  
  _↳ feedback if chosen: A symbol starts with a capital letter; a second letter is always small._
- ◻️ Hy  
  _↳ feedback if chosen: Not always the first two letters: some symbols come from Latin names or use another letter._
- ✅ H

Full working after a second miss:

> hydrogen: H.  

Sources: elements (Elements and symbols (IUPAC); British spellings aluminium and sulfur; Latin origins of Na, K, Fe, Cu, Ag, Sn, Au, Hg, Pb)

### `ch19-sort` · Lesson 19 · matching, level 2

Prompt: Sort the elements: metal or non-metal?

Pairs (6 shown each time, sorted into groups):

- sodium → **metal**
- magnesium → **metal**
- aluminium → **metal**
- potassium → **metal**
- calcium → **metal**
- iron → **metal**
- copper → **metal**
- zinc → **metal**
- hydrogen → **non-metal**
- carbon → **non-metal**
- nitrogen → **non-metal**
- oxygen → **non-metal**
- sulfur → **non-metal**
- chlorine → **non-metal**


Three generated variants:

> Sort the elements: metal or non-metal?

Groups: metal · non-metal
- iron → **metal**
- hydrogen → **non-metal**
- carbon → **non-metal**
- zinc → **metal**
- sulfur → **non-metal**
- chlorine → **non-metal**

Full working after a second miss:

> The right pairs are:  
> iron → metal  
> hydrogen → non-metal  
> carbon → non-metal  
> zinc → metal  
> sulfur → non-metal  
> chlorine → non-metal  

> Sort the elements: metal or non-metal?

Groups: metal · non-metal
- iron → **metal**
- hydrogen → **non-metal**
- potassium → **metal**
- magnesium → **metal**
- aluminium → **metal**
- carbon → **non-metal**

Full working after a second miss:

> The right pairs are:  
> iron → metal  
> hydrogen → non-metal  
> potassium → metal  
> magnesium → metal  
> aluminium → metal  
> carbon → non-metal  

> Sort the elements: metal or non-metal?

Groups: metal · non-metal
- copper → **metal**
- carbon → **non-metal**
- zinc → **metal**
- hydrogen → **non-metal**
- calcium → **metal**
- sodium → **metal**

Full working after a second miss:

> The right pairs are:  
> copper → metal  
> carbon → non-metal  
> zinc → metal  
> hydrogen → non-metal  
> calcium → metal  
> sodium → metal  

Sources: elements (Elements and symbols (IUPAC); British spellings aluminium and sulfur; Latin origins of Na, K, Fe, Cu, Ag, Sn, Au, Hg, Pb)

### `ch19-name` · Lesson 19 · fill the blank, level 2

Prompt: Write the name of the element.
Sentence: {s} is the symbol for ___.
Right answer: `nameOf(s)`

`s`: H · He · C · N · O · Na · Mg · Al · S · Cl · K · Ca · Fe · Cu · Zn · Ag · Au · Pb

- Feedback `sulphur` (typed `'sulphur'`): “This course spells it sulfur.”
- Feedback `aluminum` (typed `'aluminum'`): “In British English: aluminium.”

Three generated variants:

> Write the name of the element.

Sentence: **Cl is the symbol for ___.**
Typed answer accepted (case and extra spaces ignored): **chlorine**

Full working after a second miss:

> The missing word is “chlorine”.  
> Cl is the symbol for chlorine.  

> Write the name of the element.

Sentence: **S is the symbol for ___.**
Typed answer accepted (case and extra spaces ignored): **sulfur**
- Typed **sulphur** (sulphur) → “This course spells it sulfur.”

Full working after a second miss:

> The missing word is “sulfur”.  
> S is the symbol for sulfur.  

> Write the name of the element.

Sentence: **Zn is the symbol for ___.**
Typed answer accepted (case and extra spaces ignored): **zinc**

Full working after a second miss:

> The missing word is “zinc”.  
> Zn is the symbol for zinc.  

Sources: elements (Elements and symbols (IUPAC); British spellings aluminium and sulfur; Latin origins of Na, K, Fe, Cu, Ag, Sn, Au, Hg, Pb)

### `ch19-spot` · Lesson 19 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The symbol for sodium is Na.
- ✅ The symbol for iron is Fe.
- ✅ An element contains one kind of atom only.
- ✅ The symbol for gold is Au.
- ❌ The symbol for potassium is P.  
  _↳ Potassium is K (from kalium); P is phosphorus._
- ❌ Water is an element.  
  _↳ Water is a compound of hydrogen and oxygen._
- ❌ The symbol for chlorine is CL.  
  _↳ The second letter is always small: Cl._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ The symbol for chlorine is CL.  
  _↳ explanation: The second letter is always small: Cl._
- ◻️ An element contains one kind of atom only.
- ◻️ The symbol for iron is Fe.
- ◻️ The symbol for sodium is Na.

Full working after a second miss:

> The wrong statement is “The symbol for chlorine is CL.”.  
> The second letter is always small: Cl.  

> One sentence is wrong. Which one?

- ◻️ An element contains one kind of atom only.
- ◻️ The symbol for sodium is Na.
- ✅ The symbol for potassium is P.  
  _↳ explanation: Potassium is K (from kalium); P is phosphorus._
- ◻️ The symbol for gold is Au.

Full working after a second miss:

> The wrong statement is “The symbol for potassium is P.”.  
> Potassium is K (from kalium); P is phosphorus.  

> One sentence is wrong. Which one?

- ◻️ The symbol for sodium is Na.
- ◻️ The symbol for iron is Fe.
- ✅ The symbol for chlorine is CL.  
  _↳ explanation: The second letter is always small: Cl._
- ◻️ The symbol for gold is Au.

Full working after a second miss:

> The wrong statement is “The symbol for chlorine is CL.”.  
> The second letter is always small: Cl.  

Sources: elements (Elements and symbols (IUPAC); British spellings aluminium and sulfur; Latin origins of Na, K, Fe, Cu, Ag, Sn, Au, Hg, Pb)

### `chc19-1-check` · Lesson 19 · multiple choice, level 1

Prompt: Which of these is an element?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ iron
- ✅ oxygen
- ✅ gold
- ❌ water  
  _↳ Water is a compound of hydrogen and oxygen._
- ❌ table salt  
  _↳ Salt is a compound of sodium and chlorine._
- ❌ air  
  _↳ Air is a mixture of gases._
- ❌ sugar  
  _↳ Sugar is a compound._


Three generated variants:

> Which of these is an element?

- ✅ iron
- ◻️ water  
  _↳ feedback if chosen: Water is a compound of hydrogen and oxygen._
- ◻️ air  
  _↳ feedback if chosen: Air is a mixture of gases._
- ◻️ table salt  
  _↳ feedback if chosen: Salt is a compound of sodium and chlorine._

Full working after a second miss:

> The true statement is “iron”.  
> “water” is false: Water is a compound of hydrogen and oxygen.  
> “air” is false: Air is a mixture of gases.  
> “table salt” is false: Salt is a compound of sodium and chlorine.  

> Which of these is an element?

- ◻️ table salt  
  _↳ feedback if chosen: Salt is a compound of sodium and chlorine._
- ◻️ water  
  _↳ feedback if chosen: Water is a compound of hydrogen and oxygen._
- ◻️ sugar  
  _↳ feedback if chosen: Sugar is a compound._
- ✅ oxygen

Full working after a second miss:

> The true statement is “oxygen”.  
> “table salt” is false: Salt is a compound of sodium and chlorine.  
> “water” is false: Water is a compound of hydrogen and oxygen.  
> “sugar” is false: Sugar is a compound.  

> Which of these is an element?

- ✅ gold
- ◻️ water  
  _↳ feedback if chosen: Water is a compound of hydrogen and oxygen._
- ◻️ sugar  
  _↳ feedback if chosen: Sugar is a compound._
- ◻️ table salt  
  _↳ feedback if chosen: Salt is a compound of sodium and chlorine._

Full working after a second miss:

> The true statement is “gold”.  
> “water” is false: Water is a compound of hydrogen and oxygen.  
> “sugar” is false: Sugar is a compound.  
> “table salt” is false: Salt is a compound of sodium and chlorine.  

Sources: elements (Elements and symbols (IUPAC); British spellings aluminium and sulfur; Latin origins of Na, K, Fe, Cu, Ag, Sn, Au, Hg, Pb)

### `ch21-sort` · Lesson 21 · matching, level 1

Prompt: Does each sentence describe a mixture or a compound?

Pairs (6 shown each time, sorted into groups):

- its parts can be in any amounts → **mixture**
- its parts keep their own properties → **mixture**
- it can be separated by physical methods → **mixture**
- it melts or boils over a range of temperatures → **mixture**
- its elements are in a fixed ratio → **compound**
- it has new properties, unlike its elements → **compound**
- it can only be split by a chemical reaction → **compound**
- it has a fixed melting and boiling point → **compound**


Three generated variants:

> Does each sentence describe a mixture or a compound?

Groups: mixture · compound
- its parts keep their own properties → **mixture**
- its elements are in a fixed ratio → **compound**
- it has a fixed melting and boiling point → **compound**
- it can only be split by a chemical reaction → **compound**
- its parts can be in any amounts → **mixture**
- it melts or boils over a range of temperatures → **mixture**

Full working after a second miss:

> The right pairs are:  
> its parts keep their own properties → mixture  
> its elements are in a fixed ratio → compound  
> it has a fixed melting and boiling point → compound  
> it can only be split by a chemical reaction → compound  
> its parts can be in any amounts → mixture  
> it melts or boils over a range of temperatures → mixture  

> Does each sentence describe a mixture or a compound?

Groups: mixture · compound
- its elements are in a fixed ratio → **compound**
- it has a fixed melting and boiling point → **compound**
- it melts or boils over a range of temperatures → **mixture**
- its parts keep their own properties → **mixture**
- it can be separated by physical methods → **mixture**
- it can only be split by a chemical reaction → **compound**

Full working after a second miss:

> The right pairs are:  
> its elements are in a fixed ratio → compound  
> it has a fixed melting and boiling point → compound  
> it melts or boils over a range of temperatures → mixture  
> its parts keep their own properties → mixture  
> it can be separated by physical methods → mixture  
> it can only be split by a chemical reaction → compound  

> Does each sentence describe a mixture or a compound?

Groups: mixture · compound
- its parts can be in any amounts → **mixture**
- its parts keep their own properties → **mixture**
- it melts or boils over a range of temperatures → **mixture**
- its elements are in a fixed ratio → **compound**
- it can only be split by a chemical reaction → **compound**
- it has a fixed melting and boiling point → **compound**

Full working after a second miss:

> The right pairs are:  
> its parts can be in any amounts → mixture  
> its parts keep their own properties → mixture  
> it melts or boils over a range of temperatures → mixture  
> its elements are in a fixed ratio → compound  
> it can only be split by a chemical reaction → compound  
> it has a fixed melting and boiling point → compound  

Sources: compounds (Compounds, formulas and atom counts (computed by parseFormula()); mixtures and compounds compared)

### `ch21-which` · Lesson 21 · multiple choice, level 1

Prompt: Is {x.t} a mixture or a compound?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| iron filings and sulfur stirred together | a mixture | iron filings and sulfur stirred together: a mixture. |
| iron sulfide made by heating iron and sulfur | a compound | iron sulfide made by heating iron and sulfur: a compound. |
| salt water | a mixture | salt water: a mixture. |
| water (H₂O) | a compound | water (H₂O): a compound. |
| air | a mixture | air: a mixture. |
| carbon dioxide (CO₂) | a compound | carbon dioxide (CO₂): a compound. |

Right answer: `{x.a}`; wrong choices: `a mixture`, `a compound`

- Feedback `other`: “Ask: are the parts chemically joined in a fixed ratio?”

Three generated variants:

> Is carbon dioxide (CO₂) a mixture or a compound?

- ✅ a compound
- ◻️ a mixture  
  _↳ feedback if chosen: Ask: are the parts chemically joined in a fixed ratio?_

Full working after a second miss:

> carbon dioxide (CO₂): a compound.  
> Answer: a compound.  

> Is water (H₂O) a mixture or a compound?

- ✅ a compound
- ◻️ a mixture  
  _↳ feedback if chosen: Ask: are the parts chemically joined in a fixed ratio?_

Full working after a second miss:

> water (H₂O): a compound.  
> Answer: a compound.  

> Is iron sulfide made by heating iron and sulfur a mixture or a compound?

- ◻️ a mixture  
  _↳ feedback if chosen: Ask: are the parts chemically joined in a fixed ratio?_
- ✅ a compound

Full working after a second miss:

> iron sulfide made by heating iron and sulfur: a compound.  
> Answer: a compound.  

Sources: compounds (Compounds, formulas and atom counts (computed by parseFormula()); mixtures and compounds compared)

### `ch21-test` · Lesson 21 · multiple choice, level 2

Prompt: Iron and sulfur have been heated together. How can you show that a compound has formed?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ A magnet no longer pulls out the iron.
- ❌ The mixture is still yellow and grey.  
  _↳ Those are the old properties: a compound has new ones._
- ❌ You can still pick out the sulfur.  
  _↳ If you can, it is still a mixture._
- ❌ It weighs the same.  
  _↳ Weighing does not show whether the elements have joined._


Three generated variants:

> Iron and sulfur have been heated together. How can you show that a compound has formed?

- ◻️ You can still pick out the sulfur.  
  _↳ feedback if chosen: If you can, it is still a mixture._
- ✅ A magnet no longer pulls out the iron.
- ◻️ It weighs the same.  
  _↳ feedback if chosen: Weighing does not show whether the elements have joined._
- ◻️ The mixture is still yellow and grey.  
  _↳ feedback if chosen: Those are the old properties: a compound has new ones._

Full working after a second miss:

> The true statement is “A magnet no longer pulls out the iron.”.  
> “You can still pick out the sulfur.” is false: If you can, it is still a mixture.  
> “It weighs the same.” is false: Weighing does not show whether the elements have joined.  
> “The mixture is still yellow and grey.” is false: Those are the old properties: a compound has new ones.  

> Iron and sulfur have been heated together. How can you show that a compound has formed?

- ◻️ The mixture is still yellow and grey.  
  _↳ feedback if chosen: Those are the old properties: a compound has new ones._
- ◻️ You can still pick out the sulfur.  
  _↳ feedback if chosen: If you can, it is still a mixture._
- ✅ A magnet no longer pulls out the iron.
- ◻️ It weighs the same.  
  _↳ feedback if chosen: Weighing does not show whether the elements have joined._

Full working after a second miss:

> The true statement is “A magnet no longer pulls out the iron.”.  
> “The mixture is still yellow and grey.” is false: Those are the old properties: a compound has new ones.  
> “You can still pick out the sulfur.” is false: If you can, it is still a mixture.  
> “It weighs the same.” is false: Weighing does not show whether the elements have joined.  

> Iron and sulfur have been heated together. How can you show that a compound has formed?

- ◻️ The mixture is still yellow and grey.  
  _↳ feedback if chosen: Those are the old properties: a compound has new ones._
- ◻️ It weighs the same.  
  _↳ feedback if chosen: Weighing does not show whether the elements have joined._
- ✅ A magnet no longer pulls out the iron.
- ◻️ You can still pick out the sulfur.  
  _↳ feedback if chosen: If you can, it is still a mixture._

Full working after a second miss:

> The true statement is “A magnet no longer pulls out the iron.”.  
> “The mixture is still yellow and grey.” is false: Those are the old properties: a compound has new ones.  
> “It weighs the same.” is false: Weighing does not show whether the elements have joined.  
> “You can still pick out the sulfur.” is false: If you can, it is still a mixture.  

Sources: compounds (Compounds, formulas and atom counts (computed by parseFormula()); mixtures and compounds compared)

### `ch21-spot` · Lesson 21 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A compound has a fixed composition.
- ✅ A mixture can be separated by physical methods.
- ✅ Forming a compound often gives out heat.
- ✅ Air is a mixture.
- ❌ Water can be separated into hydrogen and oxygen by filtering.  
  _↳ Water is a compound: only a chemical reaction splits it._
- ❌ In a compound, each element keeps its own properties.  
  _↳ A compound has new properties; each part keeps its properties only in a mixture._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ Water can be separated into hydrogen and oxygen by filtering.  
  _↳ explanation: Water is a compound: only a chemical reaction splits it._
- ◻️ A compound has a fixed composition.
- ◻️ A mixture can be separated by physical methods.
- ◻️ Air is a mixture.

Full working after a second miss:

> The wrong statement is “Water can be separated into hydrogen and oxygen by filtering.”.  
> Water is a compound: only a chemical reaction splits it.  

> One sentence is wrong. Which one?

- ◻️ Air is a mixture.
- ◻️ A compound has a fixed composition.
- ◻️ Forming a compound often gives out heat.
- ✅ Water can be separated into hydrogen and oxygen by filtering.  
  _↳ explanation: Water is a compound: only a chemical reaction splits it._

Full working after a second miss:

> The wrong statement is “Water can be separated into hydrogen and oxygen by filtering.”.  
> Water is a compound: only a chemical reaction splits it.  

> One sentence is wrong. Which one?

- ◻️ Forming a compound often gives out heat.
- ◻️ A mixture can be separated by physical methods.
- ◻️ A compound has a fixed composition.
- ✅ In a compound, each element keeps its own properties.  
  _↳ explanation: A compound has new properties; each part keeps its properties only in a mixture._

Full working after a second miss:

> The wrong statement is “In a compound, each element keeps its own properties.”.  
> A compound has new properties; each part keeps its properties only in a mixture.  

Sources: compounds (Compounds, formulas and atom counts (computed by parseFormula()); mixtures and compounds compared)

### `chc21-3-check` · Lesson 21 · multiple choice, level 1

Prompt: Which is true of a compound?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Its elements are always in the same fixed ratio.
- ❌ Its parts can be in any amounts.  
  _↳ That is a mixture._
- ❌ It can be separated with a magnet or a filter.  
  _↳ That is a mixture._
- ❌ Each part keeps its own properties.  
  _↳ That is a mixture._


Three generated variants:

> Which is true of a compound?

- ✅ Its elements are always in the same fixed ratio.
- ◻️ Its parts can be in any amounts.  
  _↳ feedback if chosen: That is a mixture._
- ◻️ Each part keeps its own properties.  
  _↳ feedback if chosen: That is a mixture._
- ◻️ It can be separated with a magnet or a filter.  
  _↳ feedback if chosen: That is a mixture._

Full working after a second miss:

> The true statement is “Its elements are always in the same fixed ratio.”.  
> “Its parts can be in any amounts.” is false: That is a mixture.  
> “Each part keeps its own properties.” is false: That is a mixture.  
> “It can be separated with a magnet or a filter.” is false: That is a mixture.  

> Which is true of a compound?

- ◻️ Each part keeps its own properties.  
  _↳ feedback if chosen: That is a mixture._
- ◻️ It can be separated with a magnet or a filter.  
  _↳ feedback if chosen: That is a mixture._
- ✅ Its elements are always in the same fixed ratio.
- ◻️ Its parts can be in any amounts.  
  _↳ feedback if chosen: That is a mixture._

Full working after a second miss:

> The true statement is “Its elements are always in the same fixed ratio.”.  
> “Each part keeps its own properties.” is false: That is a mixture.  
> “It can be separated with a magnet or a filter.” is false: That is a mixture.  
> “Its parts can be in any amounts.” is false: That is a mixture.  

> Which is true of a compound?

- ◻️ It can be separated with a magnet or a filter.  
  _↳ feedback if chosen: That is a mixture._
- ◻️ Each part keeps its own properties.  
  _↳ feedback if chosen: That is a mixture._
- ◻️ Its parts can be in any amounts.  
  _↳ feedback if chosen: That is a mixture._
- ✅ Its elements are always in the same fixed ratio.

Full working after a second miss:

> The true statement is “Its elements are always in the same fixed ratio.”.  
> “It can be separated with a magnet or a filter.” is false: That is a mixture.  
> “Each part keeps its own properties.” is false: That is a mixture.  
> “Its parts can be in any amounts.” is false: That is a mixture.  

Sources: compounds (Compounds, formulas and atom counts (computed by parseFormula()); mixtures and compounds compared)

