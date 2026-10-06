# Physics Form 1, Batch P1: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:physics`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: conventions and rules the computed answers use (src/engine/lib/physics.js)

- **g = 10 N/kg on Earth (TR-P03)**; on the Moon about 1.6 N/kg. Weight = mass × g.
- **T(K) = T(°C) + 273 (TR-P04)**; 0 °C = 273 K; 100 °C = 373 K; a change of 1 °C is a change of 1 K.
- **Unit ladders (TR-P05)**: length km hm dam m dm cm mm; mass t (= 1000 kg) kg hg dag g dg cg mg; capacity kL hL daL L dL cL mL; 1 L = 1 dm³ = 1000 cm³; 1 m³ = 1000 L; 1 mL = 1 cm³; time 1 h = 60 min = 3600 s.
- **Density (TR-P06)**: density = mass ÷ volume, shown to 2 decimals; water 1 g/cm³; 1 g/cm³ = 1000 kg/m³; floats if less than 1 g/cm³.
- **Changes of state (TR-P07)**: melting, freezing, evaporation, condensation, sublimation (solid → gas), deposition (gas → solid); heat is taken in going solid → liquid → gas and given out the other way.
- **Drawings (TR-P08)**: rulers (0–15 cm, mm marks), measuring cylinders (marks every 2 mL, numbers every 10 mL, read at the bottom of the meniscus), thermometers (0–50 °C, marks every 1 °C) are drawn by code from the question's own numbers; tests check that each drawing shows exactly the reading.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `p1-branch` | 1 | matching, 1 | science |
| 2 | `p1-which` | 1 | multiple choice, 1 | science |
| 3 | `p1-true` | 1 | multiple choice, 2 | science |
| 4 | `p1-spot` | 1 | spot the error, 3 | science |
| 5 | `pc1-1-check` (card pc1-1) | 1 | multiple choice, 1 | science |
| 6 | `p2-match` | 2 | matching, 1 | scientists |
| 7 | `p2-who` | 2 | multiple choice, 1 | scientists |
| 8 | `p2-life` | 2 | multiple choice, 2 | scientists |
| 9 | `p2-order` | 2 | ordering, 2 | scientists |
| 10 | `p2-spot` | 2 | spot the error, 3 | scientists |
| 11 | `pc2-2-check` (card pc2-2) | 2 | multiple choice, 1 | scientists |
| 12 | `p3-match` | 3 | matching, 1 | physics-branches |
| 13 | `p3-which` | 3 | multiple choice, 1 | physics-branches |
| 14 | `p3-sort` | 3 | matching, 2 | physics-branches |
| 15 | `p3-spot` | 3 | spot the error, 3 | physics-branches |
| 16 | `pc3-1-check` (card pc3-1) | 3 | multiple choice, 1 | physics-branches |
| 17 | `p4-steps` | 4 | ordering, 1 | method |
| 18 | `p4-which` | 4 | multiple choice, 1 | method |
| 19 | `p4-fair` | 4 | multiple choice, 2 | method |
| 20 | `p4-spot` | 4 | spot the error, 3 | method |
| 21 | `pc4-3-check` (card pc4-3) | 4 | multiple choice, 1 | method |
| 22 | `p5-match` | 5 | matching, 1 | equipment |
| 23 | `p5-choose` | 5 | multiple choice, 1 | equipment |
| 24 | `p5-sort` | 5 | matching, 2 | equipment |
| 25 | `p5-spot` | 5 | spot the error, 3 | equipment |
| 26 | `pc5-3-check` (card pc5-3) | 5 | multiple choice, 1 | equipment |
| 27 | `p6-sort` | 6 | matching, 1 | safety |
| 28 | `p6-what` | 6 | multiple choice, 2 | safety |
| 29 | `p6-spot` | 6 | spot the error, 3 | safety |
| 30 | `pc6-2-check` (card pc6-2) | 6 | multiple choice, 1 | safety |
| 31 | `pc6-3-check` (card pc6-3) | 6 | multiple choice, 1 | safety |
| 32 | `p7-match` | 7 | matching, 1 | jobs |
| 33 | `p7-like` | 7 | multiple choice, 2 | jobs |
| 34 | `p7-spot` | 7 | spot the error, 3 | jobs |
| 35 | `pc7-2-check` (card pc7-2) | 7 | multiple choice, 1 | jobs |
| 36 | `pc7-3-check` (card pc7-3) | 7 | multiple choice, 1 | jobs |
| 37 | `p8-instrument` | 8 | multiple choice, 1 | measurement |
| 38 | `p8-eye` | 8 | multiple choice, 2 | measurement |
| 39 | `pc8-1-check` (card pc8-1) | 8 | multiple choice, 1 | measurement |
| 40 | `p9-sort` | 9 | matching, 1 | quantities |
| 41 | `p9-which` | 9 | multiple choice, 1 | quantities |
| 42 | `p9-unit` | 9 | multiple choice, 1 | quantities |
| 43 | `p9-why` | 9 | multiple choice, 2 | quantities |
| 44 | `p9-spot` | 9 | spot the error, 3 | quantities |
| 45 | `p10-si` | 10 | matching, 1 | si-units |
| 46 | `p10-symbol` | 10 | matching, 1 | si-units |
| 47 | `p10-trap` | 10 | multiple choice, 2 | si-units |
| 48 | `p11-sort` | 11 | matching, 1 | matter |
| 49 | `p11-prop` | 11 | multiple choice, 1 | matter |
| 50 | `p11-particles` | 11 | multiple choice, 2 | matter |
| 51 | `p11-why` | 11 | multiple choice, 2 | matter |
| 52 | `p11-spot` | 11 | spot the error, 3 | matter |
| 53 | `pc11-3-check` (card pc11-3) | 11 | multiple choice, 1 | matter |
| 54 | `p12-example` | 12 | multiple choice, 1 | matter |
| 55 | `p12-spot` | 12 | spot the error, 3 | matter |
| 56 | `p13-tool` | 13 | multiple choice, 1 | measurement |
| 57 | `pc14-1-check` (card pc14-1) | 14 | multiple choice, 1 | mass |
| 58 | `p15-diff` | 15 | matching, 1 | weight |
| 59 | `p15-spot` | 15 | spot the error, 3 | weight |
| 60 | `pc15-3-check` (card pc15-3) | 15 | multiple choice, 1 | weight |
| 61 | `p17-spot` | 17 | spot the error, 3 | density |
| 62 | `p18-spot` | 18 | spot the error, 3 | temperature |
| 63 | `pc18-3-check` (card pc18-3) | 18 | multiple choice, 1 | temperature |
| 64 | `p19-symbol` | 19 | matching, 1 | hazards |
| 65 | `p19-label-l1` | 19 | multiple choice, 1 | hazards |
| 66 | `p19-product` | 19 | multiple choice, 1 | hazards |
| 67 | `p19-what` | 19 | multiple choice, 2 | hazards |
| 68 | `p19-spot` | 19 | spot the error, 3 | hazards |

### `p1-branch` · Lesson 1 · matching, level 1

Prompt: Match each branch of science with what it studies.

Pairs (4 shown each time):

- Physics → **matter, energy, forces and motion**
- Chemistry → **substances and how they change**
- Biology → **living things**
- Geology → **rocks and the Earth's crust**
- Meteorology → **weather**
- Astronomy → **planets and stars**


Three generated variants:

> Match each branch of science with what it studies.

Right-hand side (shuffled): substances and how they change · rocks and the Earth's crust · matter, energy, forces and motion · planets and stars
- Physics → **matter, energy, forces and motion**
- Geology → **rocks and the Earth's crust**
- Chemistry → **substances and how they change**
- Astronomy → **planets and stars**

Full working after a second miss:

> The right pairs are:  
> Physics → matter, energy, forces and motion  
> Geology → rocks and the Earth's crust  
> Chemistry → substances and how they change  
> Astronomy → planets and stars  

> Match each branch of science with what it studies.

Right-hand side (shuffled): weather · rocks and the Earth's crust · living things · matter, energy, forces and motion
- Meteorology → **weather**
- Physics → **matter, energy, forces and motion**
- Geology → **rocks and the Earth's crust**
- Biology → **living things**

Full working after a second miss:

> The right pairs are:  
> Meteorology → weather  
> Physics → matter, energy, forces and motion  
> Geology → rocks and the Earth's crust  
> Biology → living things  

> Match each branch of science with what it studies.

Right-hand side (shuffled): matter, energy, forces and motion · planets and stars · weather · substances and how they change
- Chemistry → **substances and how they change**
- Meteorology → **weather**
- Physics → **matter, energy, forces and motion**
- Astronomy → **planets and stars**

Full working after a second miss:

> The right pairs are:  
> Chemistry → substances and how they change  
> Meteorology → weather  
> Physics → matter, energy, forces and motion  
> Astronomy → planets and stars  

Sources: science (What science is; branches of science (Form 1 course outline))

### `p1-which` · Lesson 1 · multiple choice, level 1

Prompt: A scientist studies {x.t}. Which branch of science is this?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| how plants make their food | Biology | Plants are living things: Biology. |
| how the heart pumps blood | Biology | The heart is part of a living body: Biology. |
| why iron rusts | Chemistry | Rusting changes iron into a new substance: Chemistry. |
| what table salt is made of | Chemistry | What substances are made of is Chemistry. |
| how fast a taxi moves | Physics | Motion and speed are part of Physics. |
| how sound travels through the air | Physics | Sound is a form of energy: Physics. |
| the rocks of Mount Cameroon | Geology | Rocks and the Earth's crust are studied in Geology. |
| the planets and the stars | Astronomy | Planets and stars are studied in Astronomy. |
| tomorrow's weather in Buea | Meteorology | Weather is studied in Meteorology. |

Right answer: `{x.a}`; wrong choices: `Physics`, `Chemistry`, `Biology`, `Geology`, `Astronomy`, `Meteorology`

- Feedback `other`: “Not this branch. Think: is it about energy and motion, substances, living things, rocks, weather or the sky?”

Three generated variants:

> A scientist studies tomorrow's weather in Buea. Which branch of science is this?

- ◻️ Biology  
  _↳ feedback if chosen: Not this branch. Think: is it about energy and motion, substances, living things, rocks, weather or the sky?_
- ✅ Meteorology
- ◻️ Astronomy  
  _↳ feedback if chosen: Not this branch. Think: is it about energy and motion, substances, living things, rocks, weather or the sky?_
- ◻️ Geology  
  _↳ feedback if chosen: Not this branch. Think: is it about energy and motion, substances, living things, rocks, weather or the sky?_

Full working after a second miss:

> Weather is studied in Meteorology.  
> Answer: Meteorology.  

> A scientist studies how the heart pumps blood. Which branch of science is this?

- ◻️ Physics  
  _↳ feedback if chosen: Not this branch. Think: is it about energy and motion, substances, living things, rocks, weather or the sky?_
- ◻️ Chemistry  
  _↳ feedback if chosen: Not this branch. Think: is it about energy and motion, substances, living things, rocks, weather or the sky?_
- ✅ Biology
- ◻️ Geology  
  _↳ feedback if chosen: Not this branch. Think: is it about energy and motion, substances, living things, rocks, weather or the sky?_

Full working after a second miss:

> The heart is part of a living body: Biology.  
> Answer: Biology.  

> A scientist studies what table salt is made of. Which branch of science is this?

- ✅ Chemistry
- ◻️ Physics  
  _↳ feedback if chosen: Not this branch. Think: is it about energy and motion, substances, living things, rocks, weather or the sky?_
- ◻️ Meteorology  
  _↳ feedback if chosen: Not this branch. Think: is it about energy and motion, substances, living things, rocks, weather or the sky?_
- ◻️ Biology  
  _↳ feedback if chosen: Not this branch. Think: is it about energy and motion, substances, living things, rocks, weather or the sky?_

Full working after a second miss:

> What substances are made of is Chemistry.  
> Answer: Chemistry.  

Sources: science (What science is; branches of science (Form 1 course outline))

### `p1-true` · Lesson 1 · multiple choice, level 2

Prompt: Which sentence is true?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Physics, Chemistry and Biology are the three main branches of science.
- ✅ Medicines, electricity and phones all came from science.
- ✅ A scientist tests an idea before saying it is true.
- ❌ Biology studies rocks and soil only.  
  _↳ Biology studies living things. Rocks are studied in Geology._
- ❌ Physics is the study of living things.  
  _↳ Physics studies matter and energy. Living things are Biology._
- ❌ Science cannot help farmers.  
  _↳ Science gives better seeds, fertilisers and ways to fight pests._
- ❌ Chemistry studies the weather.  
  _↳ Weather is Meteorology. Chemistry studies substances and how they change._


Three generated variants:

> Which sentence is true?

- ◻️ Biology studies rocks and soil only.  
  _↳ feedback if chosen: Biology studies living things. Rocks are studied in Geology._
- ◻️ Science cannot help farmers.  
  _↳ feedback if chosen: Science gives better seeds, fertilisers and ways to fight pests._
- ◻️ Chemistry studies the weather.  
  _↳ feedback if chosen: Weather is Meteorology. Chemistry studies substances and how they change._
- ✅ Medicines, electricity and phones all came from science.

Full working after a second miss:

> The true statement is “Medicines, electricity and phones all came from science.”.  
> “Biology studies rocks and soil only.” is false: Biology studies living things. Rocks are studied in Geology.  
> “Science cannot help farmers.” is false: Science gives better seeds, fertilisers and ways to fight pests.  
> “Chemistry studies the weather.” is false: Weather is Meteorology. Chemistry studies substances and how they change.  

> Which sentence is true?

- ◻️ Chemistry studies the weather.  
  _↳ feedback if chosen: Weather is Meteorology. Chemistry studies substances and how they change._
- ◻️ Biology studies rocks and soil only.  
  _↳ feedback if chosen: Biology studies living things. Rocks are studied in Geology._
- ◻️ Physics is the study of living things.  
  _↳ feedback if chosen: Physics studies matter and energy. Living things are Biology._
- ✅ A scientist tests an idea before saying it is true.

Full working after a second miss:

> The true statement is “A scientist tests an idea before saying it is true.”.  
> “Chemistry studies the weather.” is false: Weather is Meteorology. Chemistry studies substances and how they change.  
> “Biology studies rocks and soil only.” is false: Biology studies living things. Rocks are studied in Geology.  
> “Physics is the study of living things.” is false: Physics studies matter and energy. Living things are Biology.  

> Which sentence is true?

- ◻️ Science cannot help farmers.  
  _↳ feedback if chosen: Science gives better seeds, fertilisers and ways to fight pests._
- ✅ Physics, Chemistry and Biology are the three main branches of science.
- ◻️ Physics is the study of living things.  
  _↳ feedback if chosen: Physics studies matter and energy. Living things are Biology._
- ◻️ Biology studies rocks and soil only.  
  _↳ feedback if chosen: Biology studies living things. Rocks are studied in Geology._

Full working after a second miss:

> The true statement is “Physics, Chemistry and Biology are the three main branches of science.”.  
> “Science cannot help farmers.” is false: Science gives better seeds, fertilisers and ways to fight pests.  
> “Physics is the study of living things.” is false: Physics studies matter and energy. Living things are Biology.  
> “Biology studies rocks and soil only.” is false: Biology studies living things. Rocks are studied in Geology.  

Sources: science (What science is; branches of science (Form 1 course outline))

### `p1-spot` · Lesson 1 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Meteorology helps farmers know when the rains will come.
- ✅ Astronomy studies the Moon, the planets and the stars.
- ✅ Chemistry studies what substances are made of.
- ✅ Physics studies forces, motion, heat, light and sound.
- ❌ Geology studies the weather.  
  _↳ Geology studies rocks. The weather is studied in Meteorology._
- ❌ Biology studies how a lamp makes light.  
  _↳ Light is studied in Physics. Biology studies living things._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Chemistry studies what substances are made of.
- ◻️ Physics studies forces, motion, heat, light and sound.
- ◻️ Meteorology helps farmers know when the rains will come.
- ✅ Biology studies how a lamp makes light.  
  _↳ explanation: Light is studied in Physics. Biology studies living things._

Full working after a second miss:

> The wrong statement is “Biology studies how a lamp makes light.”.  
> Light is studied in Physics. Biology studies living things.  

> One sentence is wrong. Which one?

- ◻️ Physics studies forces, motion, heat, light and sound.
- ◻️ Chemistry studies what substances are made of.
- ✅ Biology studies how a lamp makes light.  
  _↳ explanation: Light is studied in Physics. Biology studies living things._
- ◻️ Astronomy studies the Moon, the planets and the stars.

Full working after a second miss:

> The wrong statement is “Biology studies how a lamp makes light.”.  
> Light is studied in Physics. Biology studies living things.  

> One sentence is wrong. Which one?

- ◻️ Chemistry studies what substances are made of.
- ◻️ Physics studies forces, motion, heat, light and sound.
- ◻️ Astronomy studies the Moon, the planets and the stars.
- ✅ Biology studies how a lamp makes light.  
  _↳ explanation: Light is studied in Physics. Biology studies living things._

Full working after a second miss:

> The wrong statement is “Biology studies how a lamp makes light.”.  
> Light is studied in Physics. Biology studies living things.  

Sources: science (What science is; branches of science (Form 1 course outline))

### `pc1-1-check` · Lesson 1 · multiple choice, level 1

Prompt: Which sentence describes science?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Science is knowledge we get by observing and testing our ideas.
- ❌ Science is a list of facts we must believe without checking.  
  _↳ Scientists check their ideas with observations and experiments._
- ❌ Science is only done by people in big laboratories.  
  _↳ Anyone who observes carefully and tests ideas is doing science, even at home or on a farm._
- ❌ Science is the same thing as magic.  
  _↳ Science explains things by observing and testing, not by magic._


Three generated variants:

> Which sentence describes science?

- ◻️ Science is only done by people in big laboratories.  
  _↳ feedback if chosen: Anyone who observes carefully and tests ideas is doing science, even at home or on a farm._
- ✅ Science is knowledge we get by observing and testing our ideas.
- ◻️ Science is a list of facts we must believe without checking.  
  _↳ feedback if chosen: Scientists check their ideas with observations and experiments._
- ◻️ Science is the same thing as magic.  
  _↳ feedback if chosen: Science explains things by observing and testing, not by magic._

Full working after a second miss:

> The true statement is “Science is knowledge we get by observing and testing our ideas.”.  
> “Science is only done by people in big laboratories.” is false: Anyone who observes carefully and tests ideas is doing science, even at home or on a farm.  
> “Science is a list of facts we must believe without checking.” is false: Scientists check their ideas with observations and experiments.  
> “Science is the same thing as magic.” is false: Science explains things by observing and testing, not by magic.  

> Which sentence describes science?

- ◻️ Science is the same thing as magic.  
  _↳ feedback if chosen: Science explains things by observing and testing, not by magic._
- ◻️ Science is a list of facts we must believe without checking.  
  _↳ feedback if chosen: Scientists check their ideas with observations and experiments._
- ◻️ Science is only done by people in big laboratories.  
  _↳ feedback if chosen: Anyone who observes carefully and tests ideas is doing science, even at home or on a farm._
- ✅ Science is knowledge we get by observing and testing our ideas.

Full working after a second miss:

> The true statement is “Science is knowledge we get by observing and testing our ideas.”.  
> “Science is the same thing as magic.” is false: Science explains things by observing and testing, not by magic.  
> “Science is a list of facts we must believe without checking.” is false: Scientists check their ideas with observations and experiments.  
> “Science is only done by people in big laboratories.” is false: Anyone who observes carefully and tests ideas is doing science, even at home or on a farm.  

> Which sentence describes science?

- ◻️ Science is a list of facts we must believe without checking.  
  _↳ feedback if chosen: Scientists check their ideas with observations and experiments._
- ✅ Science is knowledge we get by observing and testing our ideas.
- ◻️ Science is only done by people in big laboratories.  
  _↳ feedback if chosen: Anyone who observes carefully and tests ideas is doing science, even at home or on a farm._
- ◻️ Science is the same thing as magic.  
  _↳ feedback if chosen: Science explains things by observing and testing, not by magic._

Full working after a second miss:

> The true statement is “Science is knowledge we get by observing and testing our ideas.”.  
> “Science is a list of facts we must believe without checking.” is false: Scientists check their ideas with observations and experiments.  
> “Science is only done by people in big laboratories.” is false: Anyone who observes carefully and tests ideas is doing science, even at home or on a farm.  
> “Science is the same thing as magic.” is false: Science explains things by observing and testing, not by magic.  

Sources: science (What science is; branches of science (Form 1 course outline))

### `p2-match` · Lesson 2 · matching, level 1

Prompt: Match each scientist with the discovery.

Pairs (4 shown each time):

- Isaac Newton → **the laws of motion and gravity**
- Alexander Graham Bell → **the telephone**
- Michael Faraday → **how to make electricity with magnets (the dynamo)**
- Marie Curie → **radioactivity (with radium and polonium)**
- Alexander Fleming → **penicillin (the first antibiotic)**
- the Wright brothers → **the first powered aeroplane flight**
- Arthur Zang (Cameroon) → **the Cardiopad, a tablet that records heart tests**


Three generated variants:

> Match each scientist with the discovery.

Right-hand side (shuffled): the first powered aeroplane flight · radioactivity (with radium and polonium) · how to make electricity with magnets (the dynamo) · the Cardiopad, a tablet that records heart tests
- Arthur Zang (Cameroon) → **the Cardiopad, a tablet that records heart tests**
- the Wright brothers → **the first powered aeroplane flight**
- Marie Curie → **radioactivity (with radium and polonium)**
- Michael Faraday → **how to make electricity with magnets (the dynamo)**

Full working after a second miss:

> The right pairs are:  
> Arthur Zang (Cameroon) → the Cardiopad, a tablet that records heart tests  
> the Wright brothers → the first powered aeroplane flight  
> Marie Curie → radioactivity (with radium and polonium)  
> Michael Faraday → how to make electricity with magnets (the dynamo)  

> Match each scientist with the discovery.

Right-hand side (shuffled): penicillin (the first antibiotic) · how to make electricity with magnets (the dynamo) · the telephone · the Cardiopad, a tablet that records heart tests
- Alexander Graham Bell → **the telephone**
- Michael Faraday → **how to make electricity with magnets (the dynamo)**
- Alexander Fleming → **penicillin (the first antibiotic)**
- Arthur Zang (Cameroon) → **the Cardiopad, a tablet that records heart tests**

Full working after a second miss:

> The right pairs are:  
> Alexander Graham Bell → the telephone  
> Michael Faraday → how to make electricity with magnets (the dynamo)  
> Alexander Fleming → penicillin (the first antibiotic)  
> Arthur Zang (Cameroon) → the Cardiopad, a tablet that records heart tests  

> Match each scientist with the discovery.

Right-hand side (shuffled): penicillin (the first antibiotic) · how to make electricity with magnets (the dynamo) · radioactivity (with radium and polonium) · the laws of motion and gravity
- Michael Faraday → **how to make electricity with magnets (the dynamo)**
- Marie Curie → **radioactivity (with radium and polonium)**
- Isaac Newton → **the laws of motion and gravity**
- Alexander Fleming → **penicillin (the first antibiotic)**

Full working after a second miss:

> The right pairs are:  
> Michael Faraday → how to make electricity with magnets (the dynamo)  
> Marie Curie → radioactivity (with radium and polonium)  
> Isaac Newton → the laws of motion and gravity  
> Alexander Fleming → penicillin (the first antibiotic)  

Sources: scientists (Scientists and dates: encyclopaedia entries (Newton 1687, Faraday 1831, Bell 1876, Curie 1898, Wright brothers 1903, Fleming 1928); Arthur Zang's Cardiopad (about 2011))

### `p2-who` · Lesson 2 · multiple choice, level 1

Prompt: Who is known for {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| the laws of motion and gravity | Isaac Newton | Isaac Newton: the laws of motion and gravity. |
| the telephone | Alexander Graham Bell | Alexander Graham Bell: the telephone. |
| how to make electricity with magnets (the dynamo) | Michael Faraday | Michael Faraday: how to make electricity with magnets (the dynamo). |
| radioactivity (with radium and polonium) | Marie Curie | Marie Curie: radioactivity (with radium and polonium). |
| penicillin (the first antibiotic) | Alexander Fleming | Alexander Fleming: penicillin (the first antibiotic). |
| the first powered aeroplane flight | the Wright brothers | the Wright brothers: the first powered aeroplane flight. |
| the Cardiopad, a tablet that records heart tests | Arthur Zang (Cameroon) | Arthur Zang (Cameroon): the Cardiopad, a tablet that records heart tests. |

Right answer: `{x.a}`; wrong choices: `Isaac Newton`, `Alexander Graham Bell`, `Michael Faraday`, `Marie Curie`, `Alexander Fleming`, `the Wright brothers`, `Arthur Zang (Cameroon)`

- Feedback `other`: “That person is known for a different discovery.”

Three generated variants:

> Who is known for penicillin (the first antibiotic)?

- ◻️ Isaac Newton  
  _↳ feedback if chosen: That person is known for a different discovery._
- ✅ Alexander Fleming
- ◻️ Michael Faraday  
  _↳ feedback if chosen: That person is known for a different discovery._
- ◻️ Alexander Graham Bell  
  _↳ feedback if chosen: That person is known for a different discovery._

Full working after a second miss:

> Alexander Fleming: penicillin (the first antibiotic).  
> Answer: Alexander Fleming.  

> Who is known for how to make electricity with magnets (the dynamo)?

- ◻️ Marie Curie  
  _↳ feedback if chosen: That person is known for a different discovery._
- ◻️ Isaac Newton  
  _↳ feedback if chosen: That person is known for a different discovery._
- ✅ Michael Faraday
- ◻️ Arthur Zang (Cameroon)  
  _↳ feedback if chosen: That person is known for a different discovery._

Full working after a second miss:

> Michael Faraday: how to make electricity with magnets (the dynamo).  
> Answer: Michael Faraday.  

> Who is known for how to make electricity with magnets (the dynamo)?

- ◻️ Arthur Zang (Cameroon)  
  _↳ feedback if chosen: That person is known for a different discovery._
- ◻️ the Wright brothers  
  _↳ feedback if chosen: That person is known for a different discovery._
- ✅ Michael Faraday
- ◻️ Alexander Fleming  
  _↳ feedback if chosen: That person is known for a different discovery._

Full working after a second miss:

> Michael Faraday: how to make electricity with magnets (the dynamo).  
> Answer: Michael Faraday.  

Sources: scientists (Scientists and dates: encyclopaedia entries (Newton 1687, Faraday 1831, Bell 1876, Curie 1898, Wright brothers 1903, Fleming 1928); Arthur Zang's Cardiopad (about 2011))

### `p2-life` · Lesson 2 · multiple choice, level 2

Prompt: How does {x.t} help people today?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| the laws of motion and gravity | helps engineers design bridges, cars and rockets | the laws of motion and gravity helps engineers design bridges, cars and rockets. |
| the telephone | lets people talk to each other across long distances | the telephone lets people talk to each other across long distances. |
| how to make electricity with magnets (the dynamo) | led to the generators that give us electric power | how to make electricity with magnets (the dynamo) led to the generators that give us electric power. |
| radioactivity (with radium and polonium) | led to X-ray machines and cancer treatment | radioactivity (with radium and polonium) led to X-ray machines and cancer treatment. |
| penicillin (the first antibiotic) | cures many infections caused by bacteria | penicillin (the first antibiotic) cures many infections caused by bacteria. |
| the first powered aeroplane flight | made travel by air possible | the first powered aeroplane flight made travel by air possible. |
| the Cardiopad, a tablet that records heart tests | lets a heart test be sent to a doctor far away | the Cardiopad, a tablet that records heart tests lets a heart test be sent to a doctor far away. |

Right answer: `{x.a}`; wrong choices: `helps engineers design bridges, cars and rockets`, `lets people talk to each other across long distances`, `led to the generators that give us electric power`, `led to X-ray machines and cancer treatment`, `cures many infections caused by bacteria`, `made travel by air possible`, `lets a heart test be sent to a doctor far away`

- Feedback `other`: “That is what a different discovery does.”

Three generated variants:

> How does penicillin (the first antibiotic) help people today?

- ◻️ led to X-ray machines and cancer treatment  
  _↳ feedback if chosen: That is what a different discovery does._
- ✅ cures many infections caused by bacteria
- ◻️ led to the generators that give us electric power  
  _↳ feedback if chosen: That is what a different discovery does._
- ◻️ lets a heart test be sent to a doctor far away  
  _↳ feedback if chosen: That is what a different discovery does._

Full working after a second miss:

> penicillin (the first antibiotic) cures many infections caused by bacteria.  
> Answer: cures many infections caused by bacteria.  

> How does the first powered aeroplane flight help people today?

- ✅ made travel by air possible
- ◻️ lets people talk to each other across long distances  
  _↳ feedback if chosen: That is what a different discovery does._
- ◻️ helps engineers design bridges, cars and rockets  
  _↳ feedback if chosen: That is what a different discovery does._
- ◻️ led to the generators that give us electric power  
  _↳ feedback if chosen: That is what a different discovery does._

Full working after a second miss:

> the first powered aeroplane flight made travel by air possible.  
> Answer: made travel by air possible.  

> How does the laws of motion and gravity help people today?

- ◻️ led to X-ray machines and cancer treatment  
  _↳ feedback if chosen: That is what a different discovery does._
- ✅ helps engineers design bridges, cars and rockets
- ◻️ made travel by air possible  
  _↳ feedback if chosen: That is what a different discovery does._
- ◻️ led to the generators that give us electric power  
  _↳ feedback if chosen: That is what a different discovery does._

Full working after a second miss:

> the laws of motion and gravity helps engineers design bridges, cars and rockets.  
> Answer: helps engineers design bridges, cars and rockets.  

Sources: scientists (Scientists and dates: encyclopaedia entries (Newton 1687, Faraday 1831, Bell 1876, Curie 1898, Wright brothers 1903, Fleming 1928); Arthur Zang's Cardiopad (about 2011))

### `p2-order` · Lesson 2 · ordering, level 2

Prompt: Put these discoveries in order, from the oldest to the newest.

Items in the right order:

1. {['Isaac Newton: the laws of motion and gravity', 'Alexander Graham Bell: the telephone', 'Michael Faraday: how to make electricity with magnets (the dynamo)', 'Marie Curie: radioactivity (with radium and polonium)', 'Alexander Fleming: penicillin (the first antibiotic)', 'the Wright brothers: the first powered aeroplane flight'][k[0]]}
2. {['Isaac Newton: the laws of motion and gravity', 'Alexander Graham Bell: the telephone', 'Michael Faraday: how to make electricity with magnets (the dynamo)', 'Marie Curie: radioactivity (with radium and polonium)', 'Alexander Fleming: penicillin (the first antibiotic)', 'the Wright brothers: the first powered aeroplane flight'][k[1]]}
3. {['Isaac Newton: the laws of motion and gravity', 'Alexander Graham Bell: the telephone', 'Michael Faraday: how to make electricity with magnets (the dynamo)', 'Marie Curie: radioactivity (with radium and polonium)', 'Alexander Fleming: penicillin (the first antibiotic)', 'the Wright brothers: the first powered aeroplane flight'][k[2]]}
4. {['Isaac Newton: the laws of motion and gravity', 'Alexander Graham Bell: the telephone', 'Michael Faraday: how to make electricity with magnets (the dynamo)', 'Marie Curie: radioactivity (with radium and polonium)', 'Alexander Fleming: penicillin (the first antibiotic)', 'the Wright brothers: the first powered aeroplane flight'][k[3]]}


Three generated variants:

> Put these discoveries in order, from the oldest to the newest.

Shown as: Michael Faraday: how to make electricity with magnets (the dynamo) · Isaac Newton: the laws of motion and gravity · Alexander Fleming: penicillin (the first antibiotic) · the Wright brothers: the first powered aeroplane flight
Correct order: Isaac Newton: the laws of motion and gravity → Michael Faraday: how to make electricity with magnets (the dynamo) → the Wright brothers: the first powered aeroplane flight → Alexander Fleming: penicillin (the first antibiotic)

Full working after a second miss:

> The correct order is: Isaac Newton: the laws of motion and gravity → Michael Faraday: how to make electricity with magnets (the dynamo) → the Wright brothers: the first powered aeroplane flight → Alexander Fleming: penicillin (the first antibiotic).  

> Put these discoveries in order, from the oldest to the newest.

Shown as: Marie Curie: radioactivity (with radium and polonium) · Alexander Graham Bell: the telephone · the Wright brothers: the first powered aeroplane flight · Michael Faraday: how to make electricity with magnets (the dynamo)
Correct order: Michael Faraday: how to make electricity with magnets (the dynamo) → Alexander Graham Bell: the telephone → Marie Curie: radioactivity (with radium and polonium) → the Wright brothers: the first powered aeroplane flight

Full working after a second miss:

> The correct order is: Michael Faraday: how to make electricity with magnets (the dynamo) → Alexander Graham Bell: the telephone → Marie Curie: radioactivity (with radium and polonium) → the Wright brothers: the first powered aeroplane flight.  

> Put these discoveries in order, from the oldest to the newest.

Shown as: Alexander Fleming: penicillin (the first antibiotic) · Michael Faraday: how to make electricity with magnets (the dynamo) · the Wright brothers: the first powered aeroplane flight · Alexander Graham Bell: the telephone
Correct order: Michael Faraday: how to make electricity with magnets (the dynamo) → Alexander Graham Bell: the telephone → the Wright brothers: the first powered aeroplane flight → Alexander Fleming: penicillin (the first antibiotic)

Full working after a second miss:

> The correct order is: Michael Faraday: how to make electricity with magnets (the dynamo) → Alexander Graham Bell: the telephone → the Wright brothers: the first powered aeroplane flight → Alexander Fleming: penicillin (the first antibiotic).  

Sources: scientists (Scientists and dates: encyclopaedia entries (Newton 1687, Faraday 1831, Bell 1876, Curie 1898, Wright brothers 1903, Fleming 1928); Arthur Zang's Cardiopad (about 2011))

### `p2-spot` · Lesson 2 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Alexander Graham Bell made the telephone.
- ✅ Alexander Fleming discovered penicillin.
- ✅ Michael Faraday showed how to make electricity with magnets.
- ✅ Arthur Zang created the Cardiopad.
- ❌ Isaac Newton made the first aeroplane.  
  _↳ Newton described motion and gravity. The first powered flight was by the Wright brothers._
- ❌ Marie Curie made the telephone.  
  _↳ Marie Curie studied radioactivity. The telephone was made by Bell._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ Marie Curie made the telephone.  
  _↳ explanation: Marie Curie studied radioactivity. The telephone was made by Bell._
- ◻️ Arthur Zang created the Cardiopad.
- ◻️ Michael Faraday showed how to make electricity with magnets.
- ◻️ Alexander Graham Bell made the telephone.

Full working after a second miss:

> The wrong statement is “Marie Curie made the telephone.”.  
> Marie Curie studied radioactivity. The telephone was made by Bell.  

> One sentence is wrong. Which one?

- ◻️ Arthur Zang created the Cardiopad.
- ◻️ Alexander Fleming discovered penicillin.
- ✅ Isaac Newton made the first aeroplane.  
  _↳ explanation: Newton described motion and gravity. The first powered flight was by the Wright brothers._
- ◻️ Alexander Graham Bell made the telephone.

Full working after a second miss:

> The wrong statement is “Isaac Newton made the first aeroplane.”.  
> Newton described motion and gravity. The first powered flight was by the Wright brothers.  

> One sentence is wrong. Which one?

- ◻️ Alexander Fleming discovered penicillin.
- ✅ Marie Curie made the telephone.  
  _↳ explanation: Marie Curie studied radioactivity. The telephone was made by Bell._
- ◻️ Arthur Zang created the Cardiopad.
- ◻️ Alexander Graham Bell made the telephone.

Full working after a second miss:

> The wrong statement is “Marie Curie made the telephone.”.  
> Marie Curie studied radioactivity. The telephone was made by Bell.  

Sources: scientists (Scientists and dates: encyclopaedia entries (Newton 1687, Faraday 1831, Bell 1876, Curie 1898, Wright brothers 1903, Fleming 1928); Arthur Zang's Cardiopad (about 2011))

### `pc2-2-check` · Lesson 2 · multiple choice, level 1

Prompt: Which discovery lets people talk to each other across long distances?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ the telephone
- ❌ penicillin  
  _↳ Penicillin cures infections._
- ❌ the aeroplane  
  _↳ The aeroplane lets people travel by air._
- ❌ the laws of motion  
  _↳ The laws of motion help engineers design machines and vehicles._


Three generated variants:

> Which discovery lets people talk to each other across long distances?

- ✅ the telephone
- ◻️ the laws of motion  
  _↳ feedback if chosen: The laws of motion help engineers design machines and vehicles._
- ◻️ penicillin  
  _↳ feedback if chosen: Penicillin cures infections._
- ◻️ the aeroplane  
  _↳ feedback if chosen: The aeroplane lets people travel by air._

Full working after a second miss:

> The true statement is “the telephone”.  
> “the laws of motion” is false: The laws of motion help engineers design machines and vehicles.  
> “penicillin” is false: Penicillin cures infections.  
> “the aeroplane” is false: The aeroplane lets people travel by air.  

> Which discovery lets people talk to each other across long distances?

- ◻️ penicillin  
  _↳ feedback if chosen: Penicillin cures infections._
- ◻️ the aeroplane  
  _↳ feedback if chosen: The aeroplane lets people travel by air._
- ◻️ the laws of motion  
  _↳ feedback if chosen: The laws of motion help engineers design machines and vehicles._
- ✅ the telephone

Full working after a second miss:

> The true statement is “the telephone”.  
> “penicillin” is false: Penicillin cures infections.  
> “the aeroplane” is false: The aeroplane lets people travel by air.  
> “the laws of motion” is false: The laws of motion help engineers design machines and vehicles.  

> Which discovery lets people talk to each other across long distances?

- ✅ the telephone
- ◻️ penicillin  
  _↳ feedback if chosen: Penicillin cures infections._
- ◻️ the laws of motion  
  _↳ feedback if chosen: The laws of motion help engineers design machines and vehicles._
- ◻️ the aeroplane  
  _↳ feedback if chosen: The aeroplane lets people travel by air._

Full working after a second miss:

> The true statement is “the telephone”.  
> “penicillin” is false: Penicillin cures infections.  
> “the laws of motion” is false: The laws of motion help engineers design machines and vehicles.  
> “the aeroplane” is false: The aeroplane lets people travel by air.  

Sources: scientists (Scientists and dates: encyclopaedia entries (Newton 1687, Faraday 1831, Bell 1876, Curie 1898, Wright brothers 1903, Fleming 1928); Arthur Zang's Cardiopad (about 2011))

### `p3-match` · Lesson 3 · matching, level 1

Prompt: Match each branch of physics with what it studies.

Pairs (4 shown each time):

- Mechanics → **forces and motion**
- Heat → **temperature and how heat moves**
- Optics → **light, mirrors and lenses**
- Sound (acoustics) → **how sound is made and travels**
- Electricity and magnetism → **batteries, wires and magnets**


Three generated variants:

> Match each branch of physics with what it studies.

Right-hand side (shuffled): batteries, wires and magnets · light, mirrors and lenses · forces and motion · how sound is made and travels
- Optics → **light, mirrors and lenses**
- Mechanics → **forces and motion**
- Sound (acoustics) → **how sound is made and travels**
- Electricity and magnetism → **batteries, wires and magnets**

Full working after a second miss:

> The right pairs are:  
> Optics → light, mirrors and lenses  
> Mechanics → forces and motion  
> Sound (acoustics) → how sound is made and travels  
> Electricity and magnetism → batteries, wires and magnets  

> Match each branch of physics with what it studies.

Right-hand side (shuffled): forces and motion · temperature and how heat moves · light, mirrors and lenses · batteries, wires and magnets
- Optics → **light, mirrors and lenses**
- Heat → **temperature and how heat moves**
- Mechanics → **forces and motion**
- Electricity and magnetism → **batteries, wires and magnets**

Full working after a second miss:

> The right pairs are:  
> Optics → light, mirrors and lenses  
> Heat → temperature and how heat moves  
> Mechanics → forces and motion  
> Electricity and magnetism → batteries, wires and magnets  

> Match each branch of physics with what it studies.

Right-hand side (shuffled): batteries, wires and magnets · how sound is made and travels · temperature and how heat moves · light, mirrors and lenses
- Optics → **light, mirrors and lenses**
- Sound (acoustics) → **how sound is made and travels**
- Electricity and magnetism → **batteries, wires and magnets**
- Heat → **temperature and how heat moves**

Full working after a second miss:

> The right pairs are:  
> Optics → light, mirrors and lenses  
> Sound (acoustics) → how sound is made and travels  
> Electricity and magnetism → batteries, wires and magnets  
> Heat → temperature and how heat moves  

Sources: physics-branches (Branches of physics: mechanics, heat, optics, sound (acoustics), electricity and magnetism)

### `p3-which` · Lesson 3 · multiple choice, level 1

Prompt: Which branch of physics studies {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| how a bicycle moves and stops | Mechanics | Forces and motion: Mechanics. |
| why a metal spoon in hot tea gets hot | Heat | How heat moves: Heat (thermal physics). |
| how a mirror makes an image | Optics | Light and images: Optics. |
| why a drum makes a loud sound | Sound (acoustics) | Sound: acoustics. |
| how a torch battery lights a bulb | Electricity and magnetism | Batteries and bulbs: electricity. |
| how a compass needle points north | Electricity and magnetism | A compass is a magnet: magnetism. |
| how a lever helps lift a heavy stone | Mechanics | Forces and machines: Mechanics. |
| how light bends in a glass of water | Optics | Light: Optics. |

Right answer: `{x.a}`; wrong choices: `Mechanics`, `Heat`, `Optics`, `Sound (acoustics)`, `Electricity and magnetism`

- Feedback `other`: “Not this one. Is it about forces and motion, heat, light, sound, or electricity and magnets?”

Three generated variants:

> Which branch of physics studies how light bends in a glass of water?

- ✅ Optics
- ◻️ Sound (acoustics)  
  _↳ feedback if chosen: Not this one. Is it about forces and motion, heat, light, sound, or electricity and magnets?_
- ◻️ Mechanics  
  _↳ feedback if chosen: Not this one. Is it about forces and motion, heat, light, sound, or electricity and magnets?_
- ◻️ Heat  
  _↳ feedback if chosen: Not this one. Is it about forces and motion, heat, light, sound, or electricity and magnets?_

Full working after a second miss:

> Light: Optics.  
> Answer: Optics.  

> Which branch of physics studies how a bicycle moves and stops?

- ◻️ Sound (acoustics)  
  _↳ feedback if chosen: Not this one. Is it about forces and motion, heat, light, sound, or electricity and magnets?_
- ◻️ Heat  
  _↳ feedback if chosen: Not this one. Is it about forces and motion, heat, light, sound, or electricity and magnets?_
- ◻️ Electricity and magnetism  
  _↳ feedback if chosen: Not this one. Is it about forces and motion, heat, light, sound, or electricity and magnets?_
- ✅ Mechanics

Full working after a second miss:

> Forces and motion: Mechanics.  
> Answer: Mechanics.  

> Which branch of physics studies why a metal spoon in hot tea gets hot?

- ◻️ Mechanics  
  _↳ feedback if chosen: Not this one. Is it about forces and motion, heat, light, sound, or electricity and magnets?_
- ◻️ Optics  
  _↳ feedback if chosen: Not this one. Is it about forces and motion, heat, light, sound, or electricity and magnets?_
- ◻️ Electricity and magnetism  
  _↳ feedback if chosen: Not this one. Is it about forces and motion, heat, light, sound, or electricity and magnets?_
- ✅ Heat

Full working after a second miss:

> How heat moves: Heat (thermal physics).  
> Answer: Heat.  

Sources: physics-branches (Branches of physics: mechanics, heat, optics, sound (acoustics), electricity and magnetism)

### `p3-sort` · Lesson 3 · matching, level 2

Prompt: Which branch of science does each question belong to?

Pairs (5 shown each time, sorted into groups):

- Why does a ball roll down a slope? → **Physics**
- How does a bulb light up? → **Physics**
- Why do we hear thunder after lightning? → **Physics**
- What is soap made of? → **Chemistry**
- Why does iron rust? → **Chemistry**
- How does a goat digest grass? → **Biology**
- Why do maize leaves turn yellow? → **Biology**


Three generated variants:

> Which branch of science does each question belong to?

Groups: Physics · Chemistry · Biology
- How does a goat digest grass? → **Biology**
- How does a bulb light up? → **Physics**
- Why does a ball roll down a slope? → **Physics**
- What is soap made of? → **Chemistry**
- Why do we hear thunder after lightning? → **Physics**

Full working after a second miss:

> The right pairs are:  
> How does a goat digest grass? → Biology  
> How does a bulb light up? → Physics  
> Why does a ball roll down a slope? → Physics  
> What is soap made of? → Chemistry  
> Why do we hear thunder after lightning? → Physics  

> Which branch of science does each question belong to?

Groups: Physics · Chemistry · Biology
- Why does iron rust? → **Chemistry**
- Why does a ball roll down a slope? → **Physics**
- Why do maize leaves turn yellow? → **Biology**
- How does a goat digest grass? → **Biology**
- How does a bulb light up? → **Physics**

Full working after a second miss:

> The right pairs are:  
> Why does iron rust? → Chemistry  
> Why does a ball roll down a slope? → Physics  
> Why do maize leaves turn yellow? → Biology  
> How does a goat digest grass? → Biology  
> How does a bulb light up? → Physics  

> Which branch of science does each question belong to?

Groups: Physics · Chemistry · Biology
- Why do maize leaves turn yellow? → **Biology**
- Why does a ball roll down a slope? → **Physics**
- How does a bulb light up? → **Physics**
- Why does iron rust? → **Chemistry**
- How does a goat digest grass? → **Biology**

Full working after a second miss:

> The right pairs are:  
> Why do maize leaves turn yellow? → Biology  
> Why does a ball roll down a slope? → Physics  
> How does a bulb light up? → Physics  
> Why does iron rust? → Chemistry  
> How does a goat digest grass? → Biology  

Sources: physics-branches (Branches of physics: mechanics, heat, optics, sound (acoustics), electricity and magnetism)

### `p3-spot` · Lesson 3 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Optics studies light and mirrors.
- ✅ Mechanics studies forces and motion.
- ✅ A compass works because of magnetism.
- ✅ Physics studies matter and energy.
- ❌ Optics studies sound.  
  _↳ Optics studies light. Sound is acoustics._
- ❌ Mechanics studies light and colours.  
  _↳ Mechanics studies forces and motion. Light is optics._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ Mechanics studies light and colours.  
  _↳ explanation: Mechanics studies forces and motion. Light is optics._
- ◻️ Physics studies matter and energy.
- ◻️ A compass works because of magnetism.
- ◻️ Optics studies light and mirrors.

Full working after a second miss:

> The wrong statement is “Mechanics studies light and colours.”.  
> Mechanics studies forces and motion. Light is optics.  

> One sentence is wrong. Which one?

- ◻️ Physics studies matter and energy.
- ◻️ Optics studies light and mirrors.
- ◻️ A compass works because of magnetism.
- ✅ Mechanics studies light and colours.  
  _↳ explanation: Mechanics studies forces and motion. Light is optics._

Full working after a second miss:

> The wrong statement is “Mechanics studies light and colours.”.  
> Mechanics studies forces and motion. Light is optics.  

> One sentence is wrong. Which one?

- ◻️ Mechanics studies forces and motion.
- ◻️ Physics studies matter and energy.
- ✅ Optics studies sound.  
  _↳ explanation: Optics studies light. Sound is acoustics._
- ◻️ Optics studies light and mirrors.

Full working after a second miss:

> The wrong statement is “Optics studies sound.”.  
> Optics studies light. Sound is acoustics.  

Sources: physics-branches (Branches of physics: mechanics, heat, optics, sound (acoustics), electricity and magnetism)

### `pc3-1-check` · Lesson 3 · multiple choice, level 1

Prompt: Which question is a physics question?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Why does a ball roll down a slope?
- ✅ How does a bulb light up?
- ❌ How does a goat digest grass?  
  _↳ Digestion in an animal is Biology._
- ❌ What is soap made of?  
  _↳ What substances are made of is Chemistry._
- ❌ Why do maize leaves turn yellow?  
  _↳ Plant health is Biology._


Three generated variants:

> Which question is a physics question?

- ◻️ Why do maize leaves turn yellow?  
  _↳ feedback if chosen: Plant health is Biology._
- ◻️ What is soap made of?  
  _↳ feedback if chosen: What substances are made of is Chemistry._
- ◻️ How does a goat digest grass?  
  _↳ feedback if chosen: Digestion in an animal is Biology._
- ✅ Why does a ball roll down a slope?

Full working after a second miss:

> The true statement is “Why does a ball roll down a slope?”.  
> “Why do maize leaves turn yellow?” is false: Plant health is Biology.  
> “What is soap made of?” is false: What substances are made of is Chemistry.  
> “How does a goat digest grass?” is false: Digestion in an animal is Biology.  

> Which question is a physics question?

- ◻️ Why do maize leaves turn yellow?  
  _↳ feedback if chosen: Plant health is Biology._
- ◻️ How does a goat digest grass?  
  _↳ feedback if chosen: Digestion in an animal is Biology._
- ✅ Why does a ball roll down a slope?
- ◻️ What is soap made of?  
  _↳ feedback if chosen: What substances are made of is Chemistry._

Full working after a second miss:

> The true statement is “Why does a ball roll down a slope?”.  
> “Why do maize leaves turn yellow?” is false: Plant health is Biology.  
> “How does a goat digest grass?” is false: Digestion in an animal is Biology.  
> “What is soap made of?” is false: What substances are made of is Chemistry.  

> Which question is a physics question?

- ✅ Why does a ball roll down a slope?
- ◻️ How does a goat digest grass?  
  _↳ feedback if chosen: Digestion in an animal is Biology._
- ◻️ Why do maize leaves turn yellow?  
  _↳ feedback if chosen: Plant health is Biology._
- ◻️ What is soap made of?  
  _↳ feedback if chosen: What substances are made of is Chemistry._

Full working after a second miss:

> The true statement is “Why does a ball roll down a slope?”.  
> “How does a goat digest grass?” is false: Digestion in an animal is Biology.  
> “Why do maize leaves turn yellow?” is false: Plant health is Biology.  
> “What is soap made of?” is false: What substances are made of is Chemistry.  

Sources: physics-branches (Branches of physics: mechanics, heat, optics, sound (acoustics), electricity and magnetism)

### `p4-steps` · Lesson 4 · ordering, level 1

Prompt: Put the steps of the scientific method in order.

Items in the right order:

1. Observe something carefully
2. Ask a question about it
3. Suggest an answer to test (a hypothesis)
4. Test it with an experiment
5. Record and study the results
6. Draw a conclusion


Three generated variants:

> Put the steps of the scientific method in order.

Shown as: Record and study the results · Draw a conclusion · Suggest an answer to test (a hypothesis) · Ask a question about it · Observe something carefully · Test it with an experiment
Correct order: Observe something carefully → Ask a question about it → Suggest an answer to test (a hypothesis) → Test it with an experiment → Record and study the results → Draw a conclusion

Full working after a second miss:

> The correct order is: Observe something carefully → Ask a question about it → Suggest an answer to test (a hypothesis) → Test it with an experiment → Record and study the results → Draw a conclusion.  

> Put the steps of the scientific method in order.

Shown as: Ask a question about it · Test it with an experiment · Observe something carefully · Draw a conclusion · Record and study the results · Suggest an answer to test (a hypothesis)
Correct order: Observe something carefully → Ask a question about it → Suggest an answer to test (a hypothesis) → Test it with an experiment → Record and study the results → Draw a conclusion

Full working after a second miss:

> The correct order is: Observe something carefully → Ask a question about it → Suggest an answer to test (a hypothesis) → Test it with an experiment → Record and study the results → Draw a conclusion.  

> Put the steps of the scientific method in order.

Shown as: Suggest an answer to test (a hypothesis) · Test it with an experiment · Observe something carefully · Record and study the results · Draw a conclusion · Ask a question about it
Correct order: Observe something carefully → Ask a question about it → Suggest an answer to test (a hypothesis) → Test it with an experiment → Record and study the results → Draw a conclusion

Full working after a second miss:

> The correct order is: Observe something carefully → Ask a question about it → Suggest an answer to test (a hypothesis) → Test it with an experiment → Record and study the results → Draw a conclusion.  

Sources: method (The scientific method; fair tests)

### `p4-which` · Lesson 4 · multiple choice, level 1

Prompt: {x.t} / Which step is this?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Bih notices that water in a black pot gets hot faster than in a white pot. | Observe something carefully | This is the step “Observe something carefully”. |
| Bih asks: “Does the colour of a pot change how fast water heats up?” | Ask a question about it | This is the step “Ask a question about it”. |
| Bih thinks: “Black pots take in more heat from the sun.” | Suggest an answer to test (a hypothesis) | This is the step “Suggest an answer to test (a hypothesis)”. |
| Bih puts the same amount of water in a black pot and a white pot, side by side in the sun. | Test it with an experiment | This is the step “Test it with an experiment”. |
| Every ten minutes Bih reads the thermometer in each pot and writes the temperature in a table. | Record and study the results | This is the step “Record and study the results”. |
| Bih says: “The black pot heated faster, so colour does matter.” | Draw a conclusion | This is the step “Draw a conclusion”. |

Right answer: `{x.a}`; wrong choices: `Observe something carefully`, `Ask a question about it`, `Suggest an answer to test (a hypothesis)`, `Test it with an experiment`, `Record and study the results`, `Draw a conclusion`

- Feedback `other`: “Not quite. Is Bih looking, asking, guessing, testing, writing results, or deciding?”

Three generated variants:

> Bih puts the same amount of water in a black pot and a white pot, side by side in the sun.
> Which step is this?

- ◻️ Ask a question about it  
  _↳ feedback if chosen: Not quite. Is Bih looking, asking, guessing, testing, writing results, or deciding?_
- ✅ Test it with an experiment
- ◻️ Suggest an answer to test (a hypothesis)  
  _↳ feedback if chosen: Not quite. Is Bih looking, asking, guessing, testing, writing results, or deciding?_
- ◻️ Draw a conclusion  
  _↳ feedback if chosen: Not quite. Is Bih looking, asking, guessing, testing, writing results, or deciding?_

Full working after a second miss:

> This is the step “Test it with an experiment”.  
> Answer: Test it with an experiment.  

> Bih thinks: “Black pots take in more heat from the sun.”
> Which step is this?

- ✅ Suggest an answer to test (a hypothesis)
- ◻️ Test it with an experiment  
  _↳ feedback if chosen: Not quite. Is Bih looking, asking, guessing, testing, writing results, or deciding?_
- ◻️ Record and study the results  
  _↳ feedback if chosen: Not quite. Is Bih looking, asking, guessing, testing, writing results, or deciding?_
- ◻️ Observe something carefully  
  _↳ feedback if chosen: Not quite. Is Bih looking, asking, guessing, testing, writing results, or deciding?_

Full working after a second miss:

> This is the step “Suggest an answer to test (a hypothesis)”.  
> Answer: Suggest an answer to test (a hypothesis).  

> Bih puts the same amount of water in a black pot and a white pot, side by side in the sun.
> Which step is this?

- ✅ Test it with an experiment
- ◻️ Draw a conclusion  
  _↳ feedback if chosen: Not quite. Is Bih looking, asking, guessing, testing, writing results, or deciding?_
- ◻️ Observe something carefully  
  _↳ feedback if chosen: Not quite. Is Bih looking, asking, guessing, testing, writing results, or deciding?_
- ◻️ Record and study the results  
  _↳ feedback if chosen: Not quite. Is Bih looking, asking, guessing, testing, writing results, or deciding?_

Full working after a second miss:

> This is the step “Test it with an experiment”.  
> Answer: Test it with an experiment.  

Sources: method (The scientific method; fair tests)

### `p4-fair` · Lesson 4 · multiple choice, level 2

Prompt: Ndi wants to test whether plants grow taller with fertiliser. Which plan is a fair test?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Two plants of the same kind, the same pot, soil, water and sunlight; fertiliser for one plant only.
- ❌ One plant in the sun with fertiliser, one in the shade without.  
  _↳ Two things change (sun and fertiliser), so we cannot tell which one made the difference._
- ❌ Give both plants fertiliser and see which grows taller.  
  _↳ Nothing is compared: both get fertiliser._
- ❌ Ask friends whether fertiliser works.  
  _↳ A scientist tests the idea with an experiment, not by asking opinions._


Three generated variants:

> Ndi wants to test whether plants grow taller with fertiliser. Which plan is a fair test?

- ◻️ One plant in the sun with fertiliser, one in the shade without.  
  _↳ feedback if chosen: Two things change (sun and fertiliser), so we cannot tell which one made the difference._
- ✅ Two plants of the same kind, the same pot, soil, water and sunlight; fertiliser for one plant only.
- ◻️ Give both plants fertiliser and see which grows taller.  
  _↳ feedback if chosen: Nothing is compared: both get fertiliser._
- ◻️ Ask friends whether fertiliser works.  
  _↳ feedback if chosen: A scientist tests the idea with an experiment, not by asking opinions._

Full working after a second miss:

> The true statement is “Two plants of the same kind, the same pot, soil, water and sunlight; fertiliser for one plant only.”.  
> “One plant in the sun with fertiliser, one in the shade without.” is false: Two things change (sun and fertiliser), so we cannot tell which one made the difference.  
> “Give both plants fertiliser and see which grows taller.” is false: Nothing is compared: both get fertiliser.  
> “Ask friends whether fertiliser works.” is false: A scientist tests the idea with an experiment, not by asking opinions.  

> Ndi wants to test whether plants grow taller with fertiliser. Which plan is a fair test?

- ◻️ Give both plants fertiliser and see which grows taller.  
  _↳ feedback if chosen: Nothing is compared: both get fertiliser._
- ◻️ One plant in the sun with fertiliser, one in the shade without.  
  _↳ feedback if chosen: Two things change (sun and fertiliser), so we cannot tell which one made the difference._
- ✅ Two plants of the same kind, the same pot, soil, water and sunlight; fertiliser for one plant only.
- ◻️ Ask friends whether fertiliser works.  
  _↳ feedback if chosen: A scientist tests the idea with an experiment, not by asking opinions._

Full working after a second miss:

> The true statement is “Two plants of the same kind, the same pot, soil, water and sunlight; fertiliser for one plant only.”.  
> “Give both plants fertiliser and see which grows taller.” is false: Nothing is compared: both get fertiliser.  
> “One plant in the sun with fertiliser, one in the shade without.” is false: Two things change (sun and fertiliser), so we cannot tell which one made the difference.  
> “Ask friends whether fertiliser works.” is false: A scientist tests the idea with an experiment, not by asking opinions.  

> Ndi wants to test whether plants grow taller with fertiliser. Which plan is a fair test?

- ◻️ One plant in the sun with fertiliser, one in the shade without.  
  _↳ feedback if chosen: Two things change (sun and fertiliser), so we cannot tell which one made the difference._
- ✅ Two plants of the same kind, the same pot, soil, water and sunlight; fertiliser for one plant only.
- ◻️ Give both plants fertiliser and see which grows taller.  
  _↳ feedback if chosen: Nothing is compared: both get fertiliser._
- ◻️ Ask friends whether fertiliser works.  
  _↳ feedback if chosen: A scientist tests the idea with an experiment, not by asking opinions._

Full working after a second miss:

> The true statement is “Two plants of the same kind, the same pot, soil, water and sunlight; fertiliser for one plant only.”.  
> “One plant in the sun with fertiliser, one in the shade without.” is false: Two things change (sun and fertiliser), so we cannot tell which one made the difference.  
> “Give both plants fertiliser and see which grows taller.” is false: Nothing is compared: both get fertiliser.  
> “Ask friends whether fertiliser works.” is false: A scientist tests the idea with an experiment, not by asking opinions.  

Sources: method (The scientific method; fair tests)

### `p4-spot` · Lesson 4 · spot the error, level 3

Prompt: One sentence about how scientists work is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Scientists repeat experiments to check their results.
- ✅ A hypothesis is an answer that can be tested.
- ✅ Scientists record their measurements carefully.
- ✅ In a fair test only one thing is changed.
- ❌ If the results do not match the idea, a scientist should change the results.  
  _↳ Scientists must be honest: if the results disagree, they change the idea, not the results._
- ❌ A scientist draws a conclusion before doing the experiment.  
  _↳ The conclusion comes after testing and studying the results._


Three generated variants:

> One sentence about how scientists work is wrong. Which one?

- ◻️ In a fair test only one thing is changed.
- ✅ A scientist draws a conclusion before doing the experiment.  
  _↳ explanation: The conclusion comes after testing and studying the results._
- ◻️ A hypothesis is an answer that can be tested.
- ◻️ Scientists repeat experiments to check their results.

Full working after a second miss:

> The wrong statement is “A scientist draws a conclusion before doing the experiment.”.  
> The conclusion comes after testing and studying the results.  

> One sentence about how scientists work is wrong. Which one?

- ◻️ In a fair test only one thing is changed.
- ◻️ Scientists repeat experiments to check their results.
- ◻️ A hypothesis is an answer that can be tested.
- ✅ A scientist draws a conclusion before doing the experiment.  
  _↳ explanation: The conclusion comes after testing and studying the results._

Full working after a second miss:

> The wrong statement is “A scientist draws a conclusion before doing the experiment.”.  
> The conclusion comes after testing and studying the results.  

> One sentence about how scientists work is wrong. Which one?

- ◻️ In a fair test only one thing is changed.
- ◻️ A hypothesis is an answer that can be tested.
- ◻️ Scientists repeat experiments to check their results.
- ✅ If the results do not match the idea, a scientist should change the results.  
  _↳ explanation: Scientists must be honest: if the results disagree, they change the idea, not the results._

Full working after a second miss:

> The wrong statement is “If the results do not match the idea, a scientist should change the results.”.  
> Scientists must be honest: if the results disagree, they change the idea, not the results.  

Sources: method (The scientific method; fair tests)

### `pc4-3-check` · Lesson 4 · multiple choice, level 1

Prompt: In a fair test, how many things do you change at a time?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ only one
- ❌ two  
  _↳ If two things change, you cannot tell which one caused the result._
- ❌ all of them  
  _↳ Then you cannot tell what caused the result._
- ❌ none  
  _↳ If nothing changes, there is nothing to test._


Three generated variants:

> In a fair test, how many things do you change at a time?

- ✅ only one
- ◻️ two  
  _↳ feedback if chosen: If two things change, you cannot tell which one caused the result._
- ◻️ none  
  _↳ feedback if chosen: If nothing changes, there is nothing to test._
- ◻️ all of them  
  _↳ feedback if chosen: Then you cannot tell what caused the result._

Full working after a second miss:

> The true statement is “only one”.  
> “two” is false: If two things change, you cannot tell which one caused the result.  
> “none” is false: If nothing changes, there is nothing to test.  
> “all of them” is false: Then you cannot tell what caused the result.  

> In a fair test, how many things do you change at a time?

- ◻️ none  
  _↳ feedback if chosen: If nothing changes, there is nothing to test._
- ◻️ two  
  _↳ feedback if chosen: If two things change, you cannot tell which one caused the result._
- ◻️ all of them  
  _↳ feedback if chosen: Then you cannot tell what caused the result._
- ✅ only one

Full working after a second miss:

> The true statement is “only one”.  
> “none” is false: If nothing changes, there is nothing to test.  
> “two” is false: If two things change, you cannot tell which one caused the result.  
> “all of them” is false: Then you cannot tell what caused the result.  

> In a fair test, how many things do you change at a time?

- ✅ only one
- ◻️ all of them  
  _↳ feedback if chosen: Then you cannot tell what caused the result._
- ◻️ none  
  _↳ feedback if chosen: If nothing changes, there is nothing to test._
- ◻️ two  
  _↳ feedback if chosen: If two things change, you cannot tell which one caused the result._

Full working after a second miss:

> The true statement is “only one”.  
> “all of them” is false: Then you cannot tell what caused the result.  
> “none” is false: If nothing changes, there is nothing to test.  
> “two” is false: If two things change, you cannot tell which one caused the result.  

Sources: method (The scientific method; fair tests)

### `p5-match` · Lesson 5 · matching, level 1

Prompt: Match each instrument with what it measures.

Pairs (4 shown each time, sorted into groups):

- metre rule → **length**
- measuring tape → **length**
- beam balance → **mass**
- top-pan balance → **mass**
- measuring cylinder → **volume of a liquid**
- stopwatch → **time**
- thermometer → **temperature**
- spring balance (newton meter) → **weight (a force)**


Three generated variants:

> Match each instrument with what it measures.

Groups: mass · time · volume of a liquid · length
- measuring cylinder → **volume of a liquid**
- metre rule → **length**
- beam balance → **mass**
- stopwatch → **time**

Full working after a second miss:

> The right pairs are:  
> measuring cylinder → volume of a liquid  
> metre rule → length  
> beam balance → mass  
> stopwatch → time  

> Match each instrument with what it measures.

Groups: length · time · weight (a force)
- metre rule → **length**
- stopwatch → **time**
- measuring tape → **length**
- spring balance (newton meter) → **weight (a force)**

Full working after a second miss:

> The right pairs are:  
> metre rule → length  
> stopwatch → time  
> measuring tape → length  
> spring balance (newton meter) → weight (a force)  

> Match each instrument with what it measures.

Groups: time · volume of a liquid · mass · length
- stopwatch → **time**
- top-pan balance → **mass**
- measuring cylinder → **volume of a liquid**
- metre rule → **length**

Full working after a second miss:

> The right pairs are:  
> stopwatch → time  
> top-pan balance → mass  
> measuring cylinder → volume of a liquid  
> metre rule → length  

Sources: equipment (School physics laboratory equipment and what each measures)

### `p5-choose` · Lesson 5 · multiple choice, level 1

Prompt: Which instrument would you use to measure {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| the length of your desk | metre rule | To measure the length of your desk, use a metre rule. |
| the length of the school field | measuring tape | To measure the length of the school field, use a measuring tape. |
| the mass of a stone | beam balance | To measure the mass of a stone, use a beam balance. |
| the volume of some palm oil | measuring cylinder | To measure the volume of some palm oil, use a measuring cylinder. |
| how long a race takes | stopwatch | To measure how long a race takes, use a stopwatch. |
| how hot the water in a pot is | thermometer | To measure how hot the water in a pot is, use a thermometer. |
| the weight of a bag of rice | spring balance (newton meter) | To measure the weight of a bag of rice, use a spring balance (newton meter). |

Right answer: `{x.a}`; wrong choices: `metre rule`, `measuring tape`, `beam balance`, `top-pan balance`, `measuring cylinder`, `stopwatch`, `thermometer`, `spring balance (newton meter)`

- Feedback `other`: “That instrument measures something else. Ask: is it a length, a mass, a volume, a time, a temperature or a weight?”

Three generated variants:

> Which instrument would you use to measure the length of the school field?

- ◻️ top-pan balance  
  _↳ feedback if chosen: That instrument measures something else. Ask: is it a length, a mass, a volume, a time, a temperature or a weight?_
- ◻️ measuring cylinder  
  _↳ feedback if chosen: That instrument measures something else. Ask: is it a length, a mass, a volume, a time, a temperature or a weight?_
- ◻️ spring balance (newton meter)  
  _↳ feedback if chosen: That instrument measures something else. Ask: is it a length, a mass, a volume, a time, a temperature or a weight?_
- ✅ measuring tape

Full working after a second miss:

> To measure the length of the school field, use a measuring tape.  
> Answer: measuring tape.  

> Which instrument would you use to measure the weight of a bag of rice?

- ◻️ top-pan balance  
  _↳ feedback if chosen: That instrument measures something else. Ask: is it a length, a mass, a volume, a time, a temperature or a weight?_
- ◻️ measuring cylinder  
  _↳ feedback if chosen: That instrument measures something else. Ask: is it a length, a mass, a volume, a time, a temperature or a weight?_
- ◻️ stopwatch  
  _↳ feedback if chosen: That instrument measures something else. Ask: is it a length, a mass, a volume, a time, a temperature or a weight?_
- ✅ spring balance (newton meter)

Full working after a second miss:

> To measure the weight of a bag of rice, use a spring balance (newton meter).  
> Answer: spring balance (newton meter).  

> Which instrument would you use to measure the length of your desk?

- ◻️ top-pan balance  
  _↳ feedback if chosen: That instrument measures something else. Ask: is it a length, a mass, a volume, a time, a temperature or a weight?_
- ✅ metre rule
- ◻️ thermometer  
  _↳ feedback if chosen: That instrument measures something else. Ask: is it a length, a mass, a volume, a time, a temperature or a weight?_
- ◻️ spring balance (newton meter)  
  _↳ feedback if chosen: That instrument measures something else. Ask: is it a length, a mass, a volume, a time, a temperature or a weight?_

Full working after a second miss:

> To measure the length of your desk, use a metre rule.  
> Answer: metre rule.  

Sources: equipment (School physics laboratory equipment and what each measures)

### `p5-sort` · Lesson 5 · matching, level 2

Prompt: Does each piece of equipment measure something, or hold or heat things?

Pairs (5 shown each time, sorted into groups):

- stopwatch → **measures something**
- thermometer → **measures something**
- metre rule → **measures something**
- beam balance → **measures something**
- retort stand → **holds or heats**
- Bunsen burner → **holds or heats**
- beaker → **holds or heats**
- tripod stand → **holds or heats**


Three generated variants:

> Does each piece of equipment measure something, or hold or heat things?

Groups: measures something · holds or heats
- beaker → **holds or heats**
- thermometer → **measures something**
- stopwatch → **measures something**
- beam balance → **measures something**
- tripod stand → **holds or heats**

Full working after a second miss:

> The right pairs are:  
> beaker → holds or heats  
> thermometer → measures something  
> stopwatch → measures something  
> beam balance → measures something  
> tripod stand → holds or heats  

> Does each piece of equipment measure something, or hold or heat things?

Groups: measures something · holds or heats
- beam balance → **measures something**
- thermometer → **measures something**
- stopwatch → **measures something**
- Bunsen burner → **holds or heats**
- metre rule → **measures something**

Full working after a second miss:

> The right pairs are:  
> beam balance → measures something  
> thermometer → measures something  
> stopwatch → measures something  
> Bunsen burner → holds or heats  
> metre rule → measures something  

> Does each piece of equipment measure something, or hold or heat things?

Groups: measures something · holds or heats
- tripod stand → **holds or heats**
- stopwatch → **measures something**
- Bunsen burner → **holds or heats**
- metre rule → **measures something**
- thermometer → **measures something**

Full working after a second miss:

> The right pairs are:  
> tripod stand → holds or heats  
> stopwatch → measures something  
> Bunsen burner → holds or heats  
> metre rule → measures something  
> thermometer → measures something  

Sources: equipment (School physics laboratory equipment and what each measures)

### `p5-spot` · Lesson 5 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A stopwatch measures time.
- ✅ A measuring cylinder measures the volume of a liquid.
- ✅ A beam balance measures mass.
- ✅ A measuring tape is good for long lengths.
- ❌ A thermometer measures mass.  
  _↳ A thermometer measures temperature. Mass is measured with a balance._
- ❌ A spring balance measures temperature.  
  _↳ A spring balance measures weight, which is a force._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ A measuring cylinder measures the volume of a liquid.
- ◻️ A beam balance measures mass.
- ✅ A spring balance measures temperature.  
  _↳ explanation: A spring balance measures weight, which is a force._
- ◻️ A measuring tape is good for long lengths.

Full working after a second miss:

> The wrong statement is “A spring balance measures temperature.”.  
> A spring balance measures weight, which is a force.  

> One sentence is wrong. Which one?

- ✅ A thermometer measures mass.  
  _↳ explanation: A thermometer measures temperature. Mass is measured with a balance._
- ◻️ A measuring cylinder measures the volume of a liquid.
- ◻️ A beam balance measures mass.
- ◻️ A measuring tape is good for long lengths.

Full working after a second miss:

> The wrong statement is “A thermometer measures mass.”.  
> A thermometer measures temperature. Mass is measured with a balance.  

> One sentence is wrong. Which one?

- ◻️ A stopwatch measures time.
- ◻️ A measuring tape is good for long lengths.
- ✅ A spring balance measures temperature.  
  _↳ explanation: A spring balance measures weight, which is a force._
- ◻️ A measuring cylinder measures the volume of a liquid.

Full working after a second miss:

> The wrong statement is “A spring balance measures temperature.”.  
> A spring balance measures weight, which is a force.  

Sources: equipment (School physics laboratory equipment and what each measures)

### `pc5-3-check` · Lesson 5 · multiple choice, level 1

Prompt: Which piece of equipment is used to HOLD apparatus in place?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ retort stand and clamp
- ❌ stopwatch  
  _↳ A stopwatch measures time._
- ❌ thermometer  
  _↳ A thermometer measures temperature._
- ❌ measuring cylinder  
  _↳ A measuring cylinder measures the volume of a liquid._


Three generated variants:

> Which piece of equipment is used to HOLD apparatus in place?

- ◻️ thermometer  
  _↳ feedback if chosen: A thermometer measures temperature._
- ◻️ stopwatch  
  _↳ feedback if chosen: A stopwatch measures time._
- ✅ retort stand and clamp
- ◻️ measuring cylinder  
  _↳ feedback if chosen: A measuring cylinder measures the volume of a liquid._

Full working after a second miss:

> The true statement is “retort stand and clamp”.  
> “thermometer” is false: A thermometer measures temperature.  
> “stopwatch” is false: A stopwatch measures time.  
> “measuring cylinder” is false: A measuring cylinder measures the volume of a liquid.  

> Which piece of equipment is used to HOLD apparatus in place?

- ✅ retort stand and clamp
- ◻️ measuring cylinder  
  _↳ feedback if chosen: A measuring cylinder measures the volume of a liquid._
- ◻️ thermometer  
  _↳ feedback if chosen: A thermometer measures temperature._
- ◻️ stopwatch  
  _↳ feedback if chosen: A stopwatch measures time._

Full working after a second miss:

> The true statement is “retort stand and clamp”.  
> “measuring cylinder” is false: A measuring cylinder measures the volume of a liquid.  
> “thermometer” is false: A thermometer measures temperature.  
> “stopwatch” is false: A stopwatch measures time.  

> Which piece of equipment is used to HOLD apparatus in place?

- ◻️ measuring cylinder  
  _↳ feedback if chosen: A measuring cylinder measures the volume of a liquid._
- ◻️ thermometer  
  _↳ feedback if chosen: A thermometer measures temperature._
- ✅ retort stand and clamp
- ◻️ stopwatch  
  _↳ feedback if chosen: A stopwatch measures time._

Full working after a second miss:

> The true statement is “retort stand and clamp”.  
> “measuring cylinder” is false: A measuring cylinder measures the volume of a liquid.  
> “thermometer” is false: A thermometer measures temperature.  
> “stopwatch” is false: A stopwatch measures time.  

Sources: equipment (School physics laboratory equipment and what each measures)

### `p6-sort` · Lesson 6 · matching, level 1

Prompt: Is each action safe or not safe in the laboratory?

Pairs (6 shown each time, sorted into groups):

- Walk, never run, in the laboratory. → **safe**
- Follow the teacher's instructions. → **safe**
- Tell the teacher at once about any accident or breakage. → **safe**
- Tie back long hair near a flame. → **safe**
- Switch off electricity and gas after use. → **safe**
- Wash your hands after an experiment. → **safe**
- Keep your bag away from the bench and the floor path. → **safe**
- Eat or drink in the laboratory. → **not safe**
- Touch electric sockets with wet hands. → **not safe**
- Pick up broken glass with bare hands. → **not safe**
- Taste a substance to find out what it is. → **not safe**
- Touch apparatus that has just been heated. → **not safe**
- Point a heated test tube at a classmate. → **not safe**


Three generated variants:

> Is each action safe or not safe in the laboratory?

Groups: safe · not safe
- Tie back long hair near a flame. → **safe**
- Eat or drink in the laboratory. → **not safe**
- Walk, never run, in the laboratory. → **safe**
- Pick up broken glass with bare hands. → **not safe**
- Tell the teacher at once about any accident or breakage. → **safe**
- Taste a substance to find out what it is. → **not safe**

Full working after a second miss:

> The right pairs are:  
> Tie back long hair near a flame. → safe  
> Eat or drink in the laboratory. → not safe  
> Walk, never run, in the laboratory. → safe  
> Pick up broken glass with bare hands. → not safe  
> Tell the teacher at once about any accident or breakage. → safe  
> Taste a substance to find out what it is. → not safe  

> Is each action safe or not safe in the laboratory?

Groups: safe · not safe
- Tie back long hair near a flame. → **safe**
- Point a heated test tube at a classmate. → **not safe**
- Follow the teacher's instructions. → **safe**
- Wash your hands after an experiment. → **safe**
- Touch apparatus that has just been heated. → **not safe**
- Taste a substance to find out what it is. → **not safe**

Full working after a second miss:

> The right pairs are:  
> Tie back long hair near a flame. → safe  
> Point a heated test tube at a classmate. → not safe  
> Follow the teacher's instructions. → safe  
> Wash your hands after an experiment. → safe  
> Touch apparatus that has just been heated. → not safe  
> Taste a substance to find out what it is. → not safe  

> Is each action safe or not safe in the laboratory?

Groups: safe · not safe
- Point a heated test tube at a classmate. → **not safe**
- Tie back long hair near a flame. → **safe**
- Touch apparatus that has just been heated. → **not safe**
- Walk, never run, in the laboratory. → **safe**
- Tell the teacher at once about any accident or breakage. → **safe**
- Touch electric sockets with wet hands. → **not safe**

Full working after a second miss:

> The right pairs are:  
> Point a heated test tube at a classmate. → not safe  
> Tie back long hair near a flame. → safe  
> Touch apparatus that has just been heated. → not safe  
> Walk, never run, in the laboratory. → safe  
> Tell the teacher at once about any accident or breakage. → safe  
> Touch electric sockets with wet hands. → not safe  

Sources: safety (Laboratory safety rules (school practice))

### `p6-what` · Lesson 6 · multiple choice, level 2

Prompt: {x.t} What should you do?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| A beaker breaks on the floor. | Tell the teacher and do not touch the glass. | Safety first: the teacher must know, and no one should take a risk. |
| Your classmate burns a finger on a hot tripod. | Tell the teacher at once. | Safety first: the teacher must know, and no one should take a risk. |
| You smell gas in the laboratory. | Do not light anything and tell the teacher at once. | Safety first: the teacher must know, and no one should take a risk. |
| You do not understand an instruction. | Ask the teacher before you start. | Safety first: the teacher must know, and no one should take a risk. |

Right answer: `{x.a}`; wrong choices: `Tell the teacher and do not touch the glass.`, `Tell the teacher at once.`, `Do not light anything and tell the teacher at once.`, `Ask the teacher before you start.`, `Carry on with the experiment.`, `Hide it so you are not punished.`

- Feedback `other`: “Not the best choice here. Read what happened again.”

Three generated variants:

> You smell gas in the laboratory. What should you do?

- ✅ Do not light anything and tell the teacher at once.
- ◻️ Tell the teacher and do not touch the glass.  
  _↳ feedback if chosen: Not the best choice here. Read what happened again._
- ◻️ Carry on with the experiment.  
  _↳ feedback if chosen: Not the best choice here. Read what happened again._
- ◻️ Ask the teacher before you start.  
  _↳ feedback if chosen: Not the best choice here. Read what happened again._

Full working after a second miss:

> Safety first: the teacher must know, and no one should take a risk.  
> Answer: Do not light anything and tell the teacher at once..  

> You do not understand an instruction. What should you do?

- ◻️ Hide it so you are not punished.  
  _↳ feedback if chosen: Not the best choice here. Read what happened again._
- ◻️ Tell the teacher and do not touch the glass.  
  _↳ feedback if chosen: Not the best choice here. Read what happened again._
- ◻️ Tell the teacher at once.  
  _↳ feedback if chosen: Not the best choice here. Read what happened again._
- ✅ Ask the teacher before you start.

Full working after a second miss:

> Safety first: the teacher must know, and no one should take a risk.  
> Answer: Ask the teacher before you start..  

> You smell gas in the laboratory. What should you do?

- ✅ Do not light anything and tell the teacher at once.
- ◻️ Hide it so you are not punished.  
  _↳ feedback if chosen: Not the best choice here. Read what happened again._
- ◻️ Carry on with the experiment.  
  _↳ feedback if chosen: Not the best choice here. Read what happened again._
- ◻️ Tell the teacher and do not touch the glass.  
  _↳ feedback if chosen: Not the best choice here. Read what happened again._

Full working after a second miss:

> Safety first: the teacher must know, and no one should take a risk.  
> Answer: Do not light anything and tell the teacher at once..  

Sources: safety (Laboratory safety rules (school practice))

### `p6-spot` · Lesson 6 · spot the error, level 3

Prompt: One rule is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Wash your hands after an experiment.
- ✅ Keep your bag away from the floor path.
- ✅ Switch off the gas when you finish.
- ✅ Walk, never run, in the laboratory.
- ❌ You may taste a substance if it looks like sugar.  
  _↳ Never taste anything in a laboratory: it could be poisonous._
- ❌ Pick up broken glass quickly with your hands.  
  _↳ Never touch broken glass: tell the teacher._


Three generated variants:

> One rule is wrong. Which one?

- ◻️ Keep your bag away from the floor path.
- ✅ You may taste a substance if it looks like sugar.  
  _↳ explanation: Never taste anything in a laboratory: it could be poisonous._
- ◻️ Wash your hands after an experiment.
- ◻️ Switch off the gas when you finish.

Full working after a second miss:

> The wrong statement is “You may taste a substance if it looks like sugar.”.  
> Never taste anything in a laboratory: it could be poisonous.  

> One rule is wrong. Which one?

- ✅ You may taste a substance if it looks like sugar.  
  _↳ explanation: Never taste anything in a laboratory: it could be poisonous._
- ◻️ Keep your bag away from the floor path.
- ◻️ Walk, never run, in the laboratory.
- ◻️ Switch off the gas when you finish.

Full working after a second miss:

> The wrong statement is “You may taste a substance if it looks like sugar.”.  
> Never taste anything in a laboratory: it could be poisonous.  

> One rule is wrong. Which one?

- ✅ You may taste a substance if it looks like sugar.  
  _↳ explanation: Never taste anything in a laboratory: it could be poisonous._
- ◻️ Keep your bag away from the floor path.
- ◻️ Switch off the gas when you finish.
- ◻️ Walk, never run, in the laboratory.

Full working after a second miss:

> The wrong statement is “You may taste a substance if it looks like sugar.”.  
> Never taste anything in a laboratory: it could be poisonous.  

Sources: safety (Laboratory safety rules (school practice))

### `pc6-2-check` · Lesson 6 · multiple choice, level 1

Prompt: A test tube breaks on your bench. What do you do first?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Tell the teacher and do not touch the glass.
- ❌ Pick up the pieces with your fingers.  
  _↳ Broken glass cuts: never touch it with bare hands._
- ❌ Hide the pieces in your bag.  
  _↳ Always report a breakage so it can be cleaned up safely._
- ❌ Carry on with the experiment.  
  _↳ Stop and report it first._


Three generated variants:

> A test tube breaks on your bench. What do you do first?

- ✅ Tell the teacher and do not touch the glass.
- ◻️ Hide the pieces in your bag.  
  _↳ feedback if chosen: Always report a breakage so it can be cleaned up safely._
- ◻️ Pick up the pieces with your fingers.  
  _↳ feedback if chosen: Broken glass cuts: never touch it with bare hands._
- ◻️ Carry on with the experiment.  
  _↳ feedback if chosen: Stop and report it first._

Full working after a second miss:

> The true statement is “Tell the teacher and do not touch the glass.”.  
> “Hide the pieces in your bag.” is false: Always report a breakage so it can be cleaned up safely.  
> “Pick up the pieces with your fingers.” is false: Broken glass cuts: never touch it with bare hands.  
> “Carry on with the experiment.” is false: Stop and report it first.  

> A test tube breaks on your bench. What do you do first?

- ◻️ Pick up the pieces with your fingers.  
  _↳ feedback if chosen: Broken glass cuts: never touch it with bare hands._
- ◻️ Carry on with the experiment.  
  _↳ feedback if chosen: Stop and report it first._
- ◻️ Hide the pieces in your bag.  
  _↳ feedback if chosen: Always report a breakage so it can be cleaned up safely._
- ✅ Tell the teacher and do not touch the glass.

Full working after a second miss:

> The true statement is “Tell the teacher and do not touch the glass.”.  
> “Pick up the pieces with your fingers.” is false: Broken glass cuts: never touch it with bare hands.  
> “Carry on with the experiment.” is false: Stop and report it first.  
> “Hide the pieces in your bag.” is false: Always report a breakage so it can be cleaned up safely.  

> A test tube breaks on your bench. What do you do first?

- ◻️ Pick up the pieces with your fingers.  
  _↳ feedback if chosen: Broken glass cuts: never touch it with bare hands._
- ✅ Tell the teacher and do not touch the glass.
- ◻️ Hide the pieces in your bag.  
  _↳ feedback if chosen: Always report a breakage so it can be cleaned up safely._
- ◻️ Carry on with the experiment.  
  _↳ feedback if chosen: Stop and report it first._

Full working after a second miss:

> The true statement is “Tell the teacher and do not touch the glass.”.  
> “Pick up the pieces with your fingers.” is false: Broken glass cuts: never touch it with bare hands.  
> “Hide the pieces in your bag.” is false: Always report a breakage so it can be cleaned up safely.  
> “Carry on with the experiment.” is false: Stop and report it first.  

Sources: safety (Laboratory safety rules (school practice))

### `pc6-3-check` · Lesson 6 · multiple choice, level 1

Prompt: Which is the safe thing to do?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Dry your hands before you touch a switch.
- ❌ Touch the socket with wet hands to see if it works.  
  _↳ Water and electricity together can give a dangerous shock._
- ❌ Pick up the hot tripod quickly.  
  _↳ Heated apparatus can burn you: let it cool first._
- ❌ Pour water on a burning electric wire.  
  _↳ Water on electricity is dangerous: switch off and call the teacher._


Three generated variants:

> Which is the safe thing to do?

- ◻️ Pour water on a burning electric wire.  
  _↳ feedback if chosen: Water on electricity is dangerous: switch off and call the teacher._
- ✅ Dry your hands before you touch a switch.
- ◻️ Touch the socket with wet hands to see if it works.  
  _↳ feedback if chosen: Water and electricity together can give a dangerous shock._
- ◻️ Pick up the hot tripod quickly.  
  _↳ feedback if chosen: Heated apparatus can burn you: let it cool first._

Full working after a second miss:

> The true statement is “Dry your hands before you touch a switch.”.  
> “Pour water on a burning electric wire.” is false: Water on electricity is dangerous: switch off and call the teacher.  
> “Touch the socket with wet hands to see if it works.” is false: Water and electricity together can give a dangerous shock.  
> “Pick up the hot tripod quickly.” is false: Heated apparatus can burn you: let it cool first.  

> Which is the safe thing to do?

- ◻️ Pick up the hot tripod quickly.  
  _↳ feedback if chosen: Heated apparatus can burn you: let it cool first._
- ✅ Dry your hands before you touch a switch.
- ◻️ Pour water on a burning electric wire.  
  _↳ feedback if chosen: Water on electricity is dangerous: switch off and call the teacher._
- ◻️ Touch the socket with wet hands to see if it works.  
  _↳ feedback if chosen: Water and electricity together can give a dangerous shock._

Full working after a second miss:

> The true statement is “Dry your hands before you touch a switch.”.  
> “Pick up the hot tripod quickly.” is false: Heated apparatus can burn you: let it cool first.  
> “Pour water on a burning electric wire.” is false: Water on electricity is dangerous: switch off and call the teacher.  
> “Touch the socket with wet hands to see if it works.” is false: Water and electricity together can give a dangerous shock.  

> Which is the safe thing to do?

- ✅ Dry your hands before you touch a switch.
- ◻️ Pour water on a burning electric wire.  
  _↳ feedback if chosen: Water on electricity is dangerous: switch off and call the teacher._
- ◻️ Pick up the hot tripod quickly.  
  _↳ feedback if chosen: Heated apparatus can burn you: let it cool first._
- ◻️ Touch the socket with wet hands to see if it works.  
  _↳ feedback if chosen: Water and electricity together can give a dangerous shock._

Full working after a second miss:

> The true statement is “Dry your hands before you touch a switch.”.  
> “Pour water on a burning electric wire.” is false: Water on electricity is dangerous: switch off and call the teacher.  
> “Pick up the hot tripod quickly.” is false: Heated apparatus can burn you: let it cool first.  
> “Touch the socket with wet hands to see if it works.” is false: Water and electricity together can give a dangerous shock.  

Sources: safety (Laboratory safety rules (school practice))

### `p7-match` · Lesson 7 · matching, level 1

Prompt: Match each job with what the person does.

Pairs (4 shown each time):

- electrician → **installs and repairs electric wiring**
- doctor → **finds out what is wrong with sick people and treats them**
- pharmacist → **prepares and gives out medicines**
- civil engineer → **designs roads, bridges and buildings**
- laboratory technician → **prepares and looks after apparatus for experiments**
- meteorologist → **studies and forecasts the weather**
- pilot → **flies aeroplanes**
- radiographer → **takes X-ray pictures in a hospital**
- agricultural engineer → **designs machines and water systems for farms**


Three generated variants:

> Match each job with what the person does.

Right-hand side (shuffled): prepares and gives out medicines · installs and repairs electric wiring · designs roads, bridges and buildings · designs machines and water systems for farms
- pharmacist → **prepares and gives out medicines**
- electrician → **installs and repairs electric wiring**
- agricultural engineer → **designs machines and water systems for farms**
- civil engineer → **designs roads, bridges and buildings**

Full working after a second miss:

> The right pairs are:  
> pharmacist → prepares and gives out medicines  
> electrician → installs and repairs electric wiring  
> agricultural engineer → designs machines and water systems for farms  
> civil engineer → designs roads, bridges and buildings  

> Match each job with what the person does.

Right-hand side (shuffled): installs and repairs electric wiring · prepares and gives out medicines · designs machines and water systems for farms · finds out what is wrong with sick people and treats them
- electrician → **installs and repairs electric wiring**
- doctor → **finds out what is wrong with sick people and treats them**
- pharmacist → **prepares and gives out medicines**
- agricultural engineer → **designs machines and water systems for farms**

Full working after a second miss:

> The right pairs are:  
> electrician → installs and repairs electric wiring  
> doctor → finds out what is wrong with sick people and treats them  
> pharmacist → prepares and gives out medicines  
> agricultural engineer → designs machines and water systems for farms  

> Match each job with what the person does.

Right-hand side (shuffled): studies and forecasts the weather · finds out what is wrong with sick people and treats them · prepares and looks after apparatus for experiments · flies aeroplanes
- pilot → **flies aeroplanes**
- laboratory technician → **prepares and looks after apparatus for experiments**
- doctor → **finds out what is wrong with sick people and treats them**
- meteorologist → **studies and forecasts the weather**

Full working after a second miss:

> The right pairs are:  
> pilot → flies aeroplanes  
> laboratory technician → prepares and looks after apparatus for experiments  
> doctor → finds out what is wrong with sick people and treats them  
> meteorologist → studies and forecasts the weather  

Sources: jobs (Careers that use science)

### `p7-like` · Lesson 7 · multiple choice, level 2

Prompt: {x.t} Which job suits this pupil best?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Ndi likes fixing radios and wiring torches. | electrician | Ndi likes fixing radios and wiring torches. A good job to think about: electrician. |
| Ewane wants to build bridges over rivers. | civil engineer | Ewane wants to build bridges over rivers. A good job to think about: civil engineer. |
| Bih wants to help sick people get better. | doctor | Bih wants to help sick people get better. A good job to think about: doctor. |
| Ashu is curious about rain and storms. | meteorologist | Ashu is curious about rain and storms. A good job to think about: meteorologist. |
| Akwen dreams of flying aeroplanes. | pilot | Akwen dreams of flying aeroplanes. A good job to think about: pilot. |

Right answer: `{x.a}`; wrong choices: `electrician`, `doctor`, `pharmacist`, `civil engineer`, `laboratory technician`, `meteorologist`, `pilot`

- Feedback `other`: “That job is about something else. What does the pupil enjoy?”

Three generated variants:

> Akwen dreams of flying aeroplanes. Which job suits this pupil best?

- ◻️ electrician  
  _↳ feedback if chosen: That job is about something else. What does the pupil enjoy?_
- ◻️ civil engineer  
  _↳ feedback if chosen: That job is about something else. What does the pupil enjoy?_
- ◻️ doctor  
  _↳ feedback if chosen: That job is about something else. What does the pupil enjoy?_
- ✅ pilot

Full working after a second miss:

> Akwen dreams of flying aeroplanes. A good job to think about: pilot.  
> Answer: pilot.  

> Ewane wants to build bridges over rivers. Which job suits this pupil best?

- ◻️ laboratory technician  
  _↳ feedback if chosen: That job is about something else. What does the pupil enjoy?_
- ◻️ doctor  
  _↳ feedback if chosen: That job is about something else. What does the pupil enjoy?_
- ◻️ electrician  
  _↳ feedback if chosen: That job is about something else. What does the pupil enjoy?_
- ✅ civil engineer

Full working after a second miss:

> Ewane wants to build bridges over rivers. A good job to think about: civil engineer.  
> Answer: civil engineer.  

> Ewane wants to build bridges over rivers. Which job suits this pupil best?

- ◻️ doctor  
  _↳ feedback if chosen: That job is about something else. What does the pupil enjoy?_
- ✅ civil engineer
- ◻️ laboratory technician  
  _↳ feedback if chosen: That job is about something else. What does the pupil enjoy?_
- ◻️ pharmacist  
  _↳ feedback if chosen: That job is about something else. What does the pupil enjoy?_

Full working after a second miss:

> Ewane wants to build bridges over rivers. A good job to think about: civil engineer.  
> Answer: civil engineer.  

Sources: jobs (Careers that use science)

### `p7-spot` · Lesson 7 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A pharmacist prepares and gives out medicines.
- ✅ A civil engineer designs roads and bridges.
- ✅ A meteorologist forecasts the weather.
- ✅ An electrician repairs electric wiring.
- ❌ A pilot takes X-ray pictures.  
  _↳ A pilot flies aeroplanes. X-ray pictures are taken by a radiographer._
- ❌ A radiographer designs bridges.  
  _↳ A radiographer takes X-ray pictures. Bridges are designed by civil engineers._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ A pilot takes X-ray pictures.  
  _↳ explanation: A pilot flies aeroplanes. X-ray pictures are taken by a radiographer._
- ◻️ A meteorologist forecasts the weather.
- ◻️ A pharmacist prepares and gives out medicines.
- ◻️ An electrician repairs electric wiring.

Full working after a second miss:

> The wrong statement is “A pilot takes X-ray pictures.”.  
> A pilot flies aeroplanes. X-ray pictures are taken by a radiographer.  

> One sentence is wrong. Which one?

- ◻️ An electrician repairs electric wiring.
- ◻️ A meteorologist forecasts the weather.
- ◻️ A pharmacist prepares and gives out medicines.
- ✅ A radiographer designs bridges.  
  _↳ explanation: A radiographer takes X-ray pictures. Bridges are designed by civil engineers._

Full working after a second miss:

> The wrong statement is “A radiographer designs bridges.”.  
> A radiographer takes X-ray pictures. Bridges are designed by civil engineers.  

> One sentence is wrong. Which one?

- ◻️ An electrician repairs electric wiring.
- ◻️ A pharmacist prepares and gives out medicines.
- ✅ A pilot takes X-ray pictures.  
  _↳ explanation: A pilot flies aeroplanes. X-ray pictures are taken by a radiographer._
- ◻️ A meteorologist forecasts the weather.

Full working after a second miss:

> The wrong statement is “A pilot takes X-ray pictures.”.  
> A pilot flies aeroplanes. X-ray pictures are taken by a radiographer.  

Sources: jobs (Careers that use science)

### `pc7-2-check` · Lesson 7 · multiple choice, level 1

Prompt: Which job is about electric wiring?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ electrician
- ❌ pharmacist  
  _↳ A pharmacist prepares medicines._
- ❌ pilot  
  _↳ A pilot flies aeroplanes._
- ❌ meteorologist  
  _↳ A meteorologist forecasts the weather._


Three generated variants:

> Which job is about electric wiring?

- ◻️ meteorologist  
  _↳ feedback if chosen: A meteorologist forecasts the weather._
- ◻️ pharmacist  
  _↳ feedback if chosen: A pharmacist prepares medicines._
- ✅ electrician
- ◻️ pilot  
  _↳ feedback if chosen: A pilot flies aeroplanes._

Full working after a second miss:

> The true statement is “electrician”.  
> “meteorologist” is false: A meteorologist forecasts the weather.  
> “pharmacist” is false: A pharmacist prepares medicines.  
> “pilot” is false: A pilot flies aeroplanes.  

> Which job is about electric wiring?

- ◻️ pilot  
  _↳ feedback if chosen: A pilot flies aeroplanes._
- ◻️ meteorologist  
  _↳ feedback if chosen: A meteorologist forecasts the weather._
- ✅ electrician
- ◻️ pharmacist  
  _↳ feedback if chosen: A pharmacist prepares medicines._

Full working after a second miss:

> The true statement is “electrician”.  
> “pilot” is false: A pilot flies aeroplanes.  
> “meteorologist” is false: A meteorologist forecasts the weather.  
> “pharmacist” is false: A pharmacist prepares medicines.  

> Which job is about electric wiring?

- ◻️ pharmacist  
  _↳ feedback if chosen: A pharmacist prepares medicines._
- ✅ electrician
- ◻️ pilot  
  _↳ feedback if chosen: A pilot flies aeroplanes._
- ◻️ meteorologist  
  _↳ feedback if chosen: A meteorologist forecasts the weather._

Full working after a second miss:

> The true statement is “electrician”.  
> “pharmacist” is false: A pharmacist prepares medicines.  
> “pilot” is false: A pilot flies aeroplanes.  
> “meteorologist” is false: A meteorologist forecasts the weather.  

Sources: jobs (Careers that use science)

### `pc7-3-check` · Lesson 7 · multiple choice, level 1

Prompt: Which of these is a health job?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ radiographer
- ❌ pilot  
  _↳ A pilot flies aeroplanes._
- ❌ civil engineer  
  _↳ A civil engineer designs roads and bridges._
- ❌ meteorologist  
  _↳ A meteorologist studies the weather._


Three generated variants:

> Which of these is a health job?

- ◻️ meteorologist  
  _↳ feedback if chosen: A meteorologist studies the weather._
- ◻️ civil engineer  
  _↳ feedback if chosen: A civil engineer designs roads and bridges._
- ◻️ pilot  
  _↳ feedback if chosen: A pilot flies aeroplanes._
- ✅ radiographer

Full working after a second miss:

> The true statement is “radiographer”.  
> “meteorologist” is false: A meteorologist studies the weather.  
> “civil engineer” is false: A civil engineer designs roads and bridges.  
> “pilot” is false: A pilot flies aeroplanes.  

> Which of these is a health job?

- ✅ radiographer
- ◻️ pilot  
  _↳ feedback if chosen: A pilot flies aeroplanes._
- ◻️ meteorologist  
  _↳ feedback if chosen: A meteorologist studies the weather._
- ◻️ civil engineer  
  _↳ feedback if chosen: A civil engineer designs roads and bridges._

Full working after a second miss:

> The true statement is “radiographer”.  
> “pilot” is false: A pilot flies aeroplanes.  
> “meteorologist” is false: A meteorologist studies the weather.  
> “civil engineer” is false: A civil engineer designs roads and bridges.  

> Which of these is a health job?

- ◻️ pilot  
  _↳ feedback if chosen: A pilot flies aeroplanes._
- ◻️ meteorologist  
  _↳ feedback if chosen: A meteorologist studies the weather._
- ✅ radiographer
- ◻️ civil engineer  
  _↳ feedback if chosen: A civil engineer designs roads and bridges._

Full working after a second miss:

> The true statement is “radiographer”.  
> “pilot” is false: A pilot flies aeroplanes.  
> “meteorologist” is false: A meteorologist studies the weather.  
> “civil engineer” is false: A civil engineer designs roads and bridges.  

Sources: jobs (Careers that use science)

### `p8-instrument` · Lesson 8 · multiple choice, level 1

Prompt: Which instrument measures {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| length | a ruler or metre rule | Length is measured with a ruler or metre rule. |
| mass | a balance | Mass is measured with a balance. |
| the volume of a liquid | a measuring cylinder | The volume of a liquid is measured with a measuring cylinder. |
| time | a stopwatch | Time is measured with a stopwatch. |
| temperature | a thermometer | Temperature is measured with a thermometer. |

Right answer: `{x.a}`; wrong choices: `a ruler or metre rule`, `a balance`, `a measuring cylinder`, `a stopwatch`, `a thermometer`

- Feedback `other`: “That instrument measures a different quantity.”

Three generated variants:

> Which instrument measures length?

- ◻️ a thermometer  
  _↳ feedback if chosen: That instrument measures a different quantity._
- ◻️ a balance  
  _↳ feedback if chosen: That instrument measures a different quantity._
- ✅ a ruler or metre rule
- ◻️ a stopwatch  
  _↳ feedback if chosen: That instrument measures a different quantity._

Full working after a second miss:

> Length is measured with a ruler or metre rule.  
> Answer: a ruler or metre rule.  

> Which instrument measures length?

- ◻️ a stopwatch  
  _↳ feedback if chosen: That instrument measures a different quantity._
- ◻️ a thermometer  
  _↳ feedback if chosen: That instrument measures a different quantity._
- ◻️ a measuring cylinder  
  _↳ feedback if chosen: That instrument measures a different quantity._
- ✅ a ruler or metre rule

Full working after a second miss:

> Length is measured with a ruler or metre rule.  
> Answer: a ruler or metre rule.  

> Which instrument measures temperature?

- ◻️ a ruler or metre rule  
  _↳ feedback if chosen: That instrument measures a different quantity._
- ◻️ a balance  
  _↳ feedback if chosen: That instrument measures a different quantity._
- ◻️ a measuring cylinder  
  _↳ feedback if chosen: That instrument measures a different quantity._
- ✅ a thermometer

Full working after a second miss:

> Temperature is measured with a thermometer.  
> Answer: a thermometer.  

Sources: measurement (Measuring with instruments; reading a scale; parallax)

### `p8-eye` · Lesson 8 · multiple choice, level 2

Prompt: Where should your eye be when you read a scale?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Level with the mark, looking straight at the scale.
- ❌ Above the mark, looking down at a slant.  
  _↳ Looking at a slant gives a wrong reading (parallax error)._
- ❌ Far to one side of the scale.  
  _↳ From the side the mark seems to move: a wrong reading._
- ❌ Below the mark, looking up.  
  _↳ Looking up at a slant also gives a wrong reading._


Three generated variants:

> Where should your eye be when you read a scale?

- ✅ Level with the mark, looking straight at the scale.
- ◻️ Above the mark, looking down at a slant.  
  _↳ feedback if chosen: Looking at a slant gives a wrong reading (parallax error)._
- ◻️ Far to one side of the scale.  
  _↳ feedback if chosen: From the side the mark seems to move: a wrong reading._
- ◻️ Below the mark, looking up.  
  _↳ feedback if chosen: Looking up at a slant also gives a wrong reading._

Full working after a second miss:

> The true statement is “Level with the mark, looking straight at the scale.”.  
> “Above the mark, looking down at a slant.” is false: Looking at a slant gives a wrong reading (parallax error).  
> “Far to one side of the scale.” is false: From the side the mark seems to move: a wrong reading.  
> “Below the mark, looking up.” is false: Looking up at a slant also gives a wrong reading.  

> Where should your eye be when you read a scale?

- ◻️ Below the mark, looking up.  
  _↳ feedback if chosen: Looking up at a slant also gives a wrong reading._
- ◻️ Above the mark, looking down at a slant.  
  _↳ feedback if chosen: Looking at a slant gives a wrong reading (parallax error)._
- ◻️ Far to one side of the scale.  
  _↳ feedback if chosen: From the side the mark seems to move: a wrong reading._
- ✅ Level with the mark, looking straight at the scale.

Full working after a second miss:

> The true statement is “Level with the mark, looking straight at the scale.”.  
> “Below the mark, looking up.” is false: Looking up at a slant also gives a wrong reading.  
> “Above the mark, looking down at a slant.” is false: Looking at a slant gives a wrong reading (parallax error).  
> “Far to one side of the scale.” is false: From the side the mark seems to move: a wrong reading.  

> Where should your eye be when you read a scale?

- ◻️ Above the mark, looking down at a slant.  
  _↳ feedback if chosen: Looking at a slant gives a wrong reading (parallax error)._
- ◻️ Below the mark, looking up.  
  _↳ feedback if chosen: Looking up at a slant also gives a wrong reading._
- ◻️ Far to one side of the scale.  
  _↳ feedback if chosen: From the side the mark seems to move: a wrong reading._
- ✅ Level with the mark, looking straight at the scale.

Full working after a second miss:

> The true statement is “Level with the mark, looking straight at the scale.”.  
> “Above the mark, looking down at a slant.” is false: Looking at a slant gives a wrong reading (parallax error).  
> “Below the mark, looking up.” is false: Looking up at a slant also gives a wrong reading.  
> “Far to one side of the scale.” is false: From the side the mark seems to move: a wrong reading.  

Sources: measurement (Measuring with instruments; reading a scale; parallax)

### `pc8-1-check` · Lesson 8 · multiple choice, level 1

Prompt: Which is a complete measurement?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ {n} cm
- ❌ {n}  
  _↳ A measurement needs a unit as well as a number._
- ❌ centimetres  
  _↳ A unit alone is not a measurement: give the number too._
- ❌ very long  
  _↳ Words like “very long” are not a measurement: give a number and a unit._


Three generated variants:

> Which is a complete measurement?

- ◻️ centimetres  
  _↳ feedback if chosen: A unit alone is not a measurement: give the number too._
- ◻️ 52  
  _↳ feedback if chosen: A measurement needs a unit as well as a number._
- ✅ 52 cm
- ◻️ very long  
  _↳ feedback if chosen: Words like “very long” are not a measurement: give a number and a unit._

Full working after a second miss:

> The true statement is “52 cm”.  
> “centimetres” is false: A unit alone is not a measurement: give the number too.  
> “52” is false: A measurement needs a unit as well as a number.  
> “very long” is false: Words like “very long” are not a measurement: give a number and a unit.  

> Which is a complete measurement?

- ◻️ very long  
  _↳ feedback if chosen: Words like “very long” are not a measurement: give a number and a unit._
- ◻️ 81  
  _↳ feedback if chosen: A measurement needs a unit as well as a number._
- ✅ 81 cm
- ◻️ centimetres  
  _↳ feedback if chosen: A unit alone is not a measurement: give the number too._

Full working after a second miss:

> The true statement is “81 cm”.  
> “very long” is false: Words like “very long” are not a measurement: give a number and a unit.  
> “81” is false: A measurement needs a unit as well as a number.  
> “centimetres” is false: A unit alone is not a measurement: give the number too.  

> Which is a complete measurement?

- ◻️ very long  
  _↳ feedback if chosen: Words like “very long” are not a measurement: give a number and a unit._
- ✅ 95 cm
- ◻️ centimetres  
  _↳ feedback if chosen: A unit alone is not a measurement: give the number too._
- ◻️ 95  
  _↳ feedback if chosen: A measurement needs a unit as well as a number._

Full working after a second miss:

> The true statement is “95 cm”.  
> “very long” is false: Words like “very long” are not a measurement: give a number and a unit.  
> “centimetres” is false: A unit alone is not a measurement: give the number too.  
> “95” is false: A measurement needs a unit as well as a number.  

Sources: measurement (Measuring with instruments; reading a scale; parallax)

### `p9-sort` · Lesson 9 · matching, level 1

Prompt: Sort them: physical quantity or not?

Pairs (6 shown each time, sorted into groups):

- length → **physical quantity**
- mass → **physical quantity**
- time → **physical quantity**
- temperature → **physical quantity**
- volume → **physical quantity**
- speed → **physical quantity**
- area → **physical quantity**
- weight → **physical quantity**
- love → **not a physical quantity**
- kindness → **not a physical quantity**
- beauty → **not a physical quantity**
- honesty → **not a physical quantity**
- happiness → **not a physical quantity**
- fear → **not a physical quantity**
- anger → **not a physical quantity**
- courage → **not a physical quantity**


Three generated variants:

> Sort them: physical quantity or not?

Groups: physical quantity · not a physical quantity
- courage → **not a physical quantity**
- volume → **physical quantity**
- happiness → **not a physical quantity**
- temperature → **physical quantity**
- anger → **not a physical quantity**
- love → **not a physical quantity**

Full working after a second miss:

> The right pairs are:  
> courage → not a physical quantity  
> volume → physical quantity  
> happiness → not a physical quantity  
> temperature → physical quantity  
> anger → not a physical quantity  
> love → not a physical quantity  

> Sort them: physical quantity or not?

Groups: physical quantity · not a physical quantity
- love → **not a physical quantity**
- temperature → **physical quantity**
- mass → **physical quantity**
- anger → **not a physical quantity**
- area → **physical quantity**
- happiness → **not a physical quantity**

Full working after a second miss:

> The right pairs are:  
> love → not a physical quantity  
> temperature → physical quantity  
> mass → physical quantity  
> anger → not a physical quantity  
> area → physical quantity  
> happiness → not a physical quantity  

> Sort them: physical quantity or not?

Groups: physical quantity · not a physical quantity
- time → **physical quantity**
- length → **physical quantity**
- happiness → **not a physical quantity**
- mass → **physical quantity**
- courage → **not a physical quantity**
- honesty → **not a physical quantity**

Full working after a second miss:

> The right pairs are:  
> time → physical quantity  
> length → physical quantity  
> happiness → not a physical quantity  
> mass → physical quantity  
> courage → not a physical quantity  
> honesty → not a physical quantity  

Sources: quantities (Physical and non-physical quantities)

### `p9-which` · Lesson 9 · multiple choice, level 1

Prompt: Which of these is a physical quantity?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ length
- ✅ mass
- ✅ time
- ✅ temperature
- ✅ volume
- ✅ speed
- ✅ area
- ✅ weight
- ❌ love  
  _↳ Love cannot be measured with an instrument and has no unit._
- ❌ kindness  
  _↳ Kindness cannot be measured with an instrument and has no unit._
- ❌ beauty  
  _↳ Beauty cannot be measured with an instrument and has no unit._
- ❌ honesty  
  _↳ Honesty cannot be measured with an instrument and has no unit._
- ❌ happiness  
  _↳ Happiness cannot be measured with an instrument and has no unit._
- ❌ fear  
  _↳ Fear cannot be measured with an instrument and has no unit._
- ❌ anger  
  _↳ Anger cannot be measured with an instrument and has no unit._
- ❌ courage  
  _↳ Courage cannot be measured with an instrument and has no unit._


Three generated variants:

> Which of these is a physical quantity?

- ◻️ happiness  
  _↳ feedback if chosen: Happiness cannot be measured with an instrument and has no unit._
- ◻️ beauty  
  _↳ feedback if chosen: Beauty cannot be measured with an instrument and has no unit._
- ◻️ love  
  _↳ feedback if chosen: Love cannot be measured with an instrument and has no unit._
- ✅ speed

Full working after a second miss:

> The true statement is “speed”.  
> “happiness” is false: Happiness cannot be measured with an instrument and has no unit.  
> “beauty” is false: Beauty cannot be measured with an instrument and has no unit.  
> “love” is false: Love cannot be measured with an instrument and has no unit.  

> Which of these is a physical quantity?

- ◻️ anger  
  _↳ feedback if chosen: Anger cannot be measured with an instrument and has no unit._
- ◻️ beauty  
  _↳ feedback if chosen: Beauty cannot be measured with an instrument and has no unit._
- ✅ mass
- ◻️ kindness  
  _↳ feedback if chosen: Kindness cannot be measured with an instrument and has no unit._

Full working after a second miss:

> The true statement is “mass”.  
> “anger” is false: Anger cannot be measured with an instrument and has no unit.  
> “beauty” is false: Beauty cannot be measured with an instrument and has no unit.  
> “kindness” is false: Kindness cannot be measured with an instrument and has no unit.  

> Which of these is a physical quantity?

- ◻️ happiness  
  _↳ feedback if chosen: Happiness cannot be measured with an instrument and has no unit._
- ◻️ love  
  _↳ feedback if chosen: Love cannot be measured with an instrument and has no unit._
- ◻️ courage  
  _↳ feedback if chosen: Courage cannot be measured with an instrument and has no unit._
- ✅ weight

Full working after a second miss:

> The true statement is “weight”.  
> “happiness” is false: Happiness cannot be measured with an instrument and has no unit.  
> “love” is false: Love cannot be measured with an instrument and has no unit.  
> “courage” is false: Courage cannot be measured with an instrument and has no unit.  

Sources: quantities (Physical and non-physical quantities)

### `p9-unit` · Lesson 9 · multiple choice, level 1

Prompt: Which unit can be used to measure {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| length | metre (m) | length can be measured in metre (m). |
| mass | kilogram (kg) | mass can be measured in kilogram (kg). |
| time | second (s) | time can be measured in second (s). |
| volume of a liquid | litre (L) | volume of a liquid can be measured in litre (L). |
| temperature | degree Celsius (°C) | temperature can be measured in degree Celsius (°C). |

Right answer: `{x.a}`; wrong choices: `metre (m)`, `kilogram (kg)`, `second (s)`, `litre (L)`, `degree Celsius (°C)`

- Feedback `other`: “That unit is for a different quantity.”

Three generated variants:

> Which unit can be used to measure temperature?

- ◻️ kilogram (kg)  
  _↳ feedback if chosen: That unit is for a different quantity._
- ◻️ metre (m)  
  _↳ feedback if chosen: That unit is for a different quantity._
- ✅ degree Celsius (°C)
- ◻️ second (s)  
  _↳ feedback if chosen: That unit is for a different quantity._

Full working after a second miss:

> temperature can be measured in degree Celsius (°C).  
> Answer: degree Celsius (°C).  

> Which unit can be used to measure mass?

- ◻️ metre (m)  
  _↳ feedback if chosen: That unit is for a different quantity._
- ◻️ degree Celsius (°C)  
  _↳ feedback if chosen: That unit is for a different quantity._
- ✅ kilogram (kg)
- ◻️ second (s)  
  _↳ feedback if chosen: That unit is for a different quantity._

Full working after a second miss:

> mass can be measured in kilogram (kg).  
> Answer: kilogram (kg).  

> Which unit can be used to measure length?

- ✅ metre (m)
- ◻️ litre (L)  
  _↳ feedback if chosen: That unit is for a different quantity._
- ◻️ kilogram (kg)  
  _↳ feedback if chosen: That unit is for a different quantity._
- ◻️ second (s)  
  _↳ feedback if chosen: That unit is for a different quantity._

Full working after a second miss:

> length can be measured in metre (m).  
> Answer: metre (m).  

Sources: quantities (Physical and non-physical quantities)

### `p9-why` · Lesson 9 · multiple choice, level 2

Prompt: Why is kindness NOT a physical quantity?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ No instrument can measure it, and it has no unit.
- ❌ Because it is too small to see.  
  _↳ Small things can still be measured. Kindness has no instrument and no unit._
- ❌ Because it changes from day to day.  
  _↳ Temperature changes too, and it is a physical quantity. The reason is: no instrument, no unit._
- ❌ Because only scientists can measure it.  
  _↳ No one can measure it: there is no instrument and no unit._


Three generated variants:

> Why is kindness NOT a physical quantity?

- ◻️ Because it is too small to see.  
  _↳ feedback if chosen: Small things can still be measured. Kindness has no instrument and no unit._
- ✅ No instrument can measure it, and it has no unit.
- ◻️ Because only scientists can measure it.  
  _↳ feedback if chosen: No one can measure it: there is no instrument and no unit._
- ◻️ Because it changes from day to day.  
  _↳ feedback if chosen: Temperature changes too, and it is a physical quantity. The reason is: no instrument, no unit._

Full working after a second miss:

> The true statement is “No instrument can measure it, and it has no unit.”.  
> “Because it is too small to see.” is false: Small things can still be measured. Kindness has no instrument and no unit.  
> “Because only scientists can measure it.” is false: No one can measure it: there is no instrument and no unit.  
> “Because it changes from day to day.” is false: Temperature changes too, and it is a physical quantity. The reason is: no instrument, no unit.  

> Why is kindness NOT a physical quantity?

- ✅ No instrument can measure it, and it has no unit.
- ◻️ Because it is too small to see.  
  _↳ feedback if chosen: Small things can still be measured. Kindness has no instrument and no unit._
- ◻️ Because it changes from day to day.  
  _↳ feedback if chosen: Temperature changes too, and it is a physical quantity. The reason is: no instrument, no unit._
- ◻️ Because only scientists can measure it.  
  _↳ feedback if chosen: No one can measure it: there is no instrument and no unit._

Full working after a second miss:

> The true statement is “No instrument can measure it, and it has no unit.”.  
> “Because it is too small to see.” is false: Small things can still be measured. Kindness has no instrument and no unit.  
> “Because it changes from day to day.” is false: Temperature changes too, and it is a physical quantity. The reason is: no instrument, no unit.  
> “Because only scientists can measure it.” is false: No one can measure it: there is no instrument and no unit.  

> Why is kindness NOT a physical quantity?

- ◻️ Because only scientists can measure it.  
  _↳ feedback if chosen: No one can measure it: there is no instrument and no unit._
- ◻️ Because it changes from day to day.  
  _↳ feedback if chosen: Temperature changes too, and it is a physical quantity. The reason is: no instrument, no unit._
- ✅ No instrument can measure it, and it has no unit.
- ◻️ Because it is too small to see.  
  _↳ feedback if chosen: Small things can still be measured. Kindness has no instrument and no unit._

Full working after a second miss:

> The true statement is “No instrument can measure it, and it has no unit.”.  
> “Because only scientists can measure it.” is false: No one can measure it: there is no instrument and no unit.  
> “Because it changes from day to day.” is false: Temperature changes too, and it is a physical quantity. The reason is: no instrument, no unit.  
> “Because it is too small to see.” is false: Small things can still be measured. Kindness has no instrument and no unit.  

Sources: quantities (Physical and non-physical quantities)

### `p9-spot` · Lesson 9 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Mass is a physical quantity measured in kilograms.
- ✅ Time is a physical quantity measured in seconds.
- ✅ Beauty is not a physical quantity.
- ✅ Temperature can be measured with a thermometer.
- ❌ Happiness is a physical quantity measured in metres.  
  _↳ Happiness cannot be measured with an instrument and has no unit._
- ❌ Length is not a physical quantity.  
  _↳ Length is measured with a ruler, in metres: it is a physical quantity._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ Happiness is a physical quantity measured in metres.  
  _↳ explanation: Happiness cannot be measured with an instrument and has no unit._
- ◻️ Time is a physical quantity measured in seconds.
- ◻️ Mass is a physical quantity measured in kilograms.
- ◻️ Temperature can be measured with a thermometer.

Full working after a second miss:

> The wrong statement is “Happiness is a physical quantity measured in metres.”.  
> Happiness cannot be measured with an instrument and has no unit.  

> One sentence is wrong. Which one?

- ◻️ Temperature can be measured with a thermometer.
- ◻️ Mass is a physical quantity measured in kilograms.
- ✅ Happiness is a physical quantity measured in metres.  
  _↳ explanation: Happiness cannot be measured with an instrument and has no unit._
- ◻️ Beauty is not a physical quantity.

Full working after a second miss:

> The wrong statement is “Happiness is a physical quantity measured in metres.”.  
> Happiness cannot be measured with an instrument and has no unit.  

> One sentence is wrong. Which one?

- ◻️ Beauty is not a physical quantity.
- ◻️ Mass is a physical quantity measured in kilograms.
- ✅ Length is not a physical quantity.  
  _↳ explanation: Length is measured with a ruler, in metres: it is a physical quantity._
- ◻️ Time is a physical quantity measured in seconds.

Full working after a second miss:

> The wrong statement is “Length is not a physical quantity.”.  
> Length is measured with a ruler, in metres: it is a physical quantity.  

Sources: quantities (Physical and non-physical quantities)

### `p10-si` · Lesson 10 · matching, level 1

Prompt: Match each quantity with its SI unit.

Pairs (4 shown each time):

- length → **metre**
- mass → **kilogram**
- time → **second**
- temperature → **kelvin**
- electric current → **ampere**


Three generated variants:

> Match each quantity with its SI unit.

Right-hand side (shuffled): kelvin · second · kilogram · ampere
- mass → **kilogram**
- electric current → **ampere**
- temperature → **kelvin**
- time → **second**

Full working after a second miss:

> The right pairs are:  
> mass → kilogram  
> electric current → ampere  
> temperature → kelvin  
> time → second  

> Match each quantity with its SI unit.

Right-hand side (shuffled): metre · kilogram · kelvin · ampere
- electric current → **ampere**
- mass → **kilogram**
- length → **metre**
- temperature → **kelvin**

Full working after a second miss:

> The right pairs are:  
> electric current → ampere  
> mass → kilogram  
> length → metre  
> temperature → kelvin  

> Match each quantity with its SI unit.

Right-hand side (shuffled): kelvin · ampere · metre · second
- time → **second**
- temperature → **kelvin**
- length → **metre**
- electric current → **ampere**

Full working after a second miss:

> The right pairs are:  
> time → second  
> temperature → kelvin  
> length → metre  
> electric current → ampere  

Sources: si-units (SI base units and prefixes (BIPM, The International System of Units))

### `p10-symbol` · Lesson 10 · matching, level 1

Prompt: Match each unit with its symbol.

Pairs (4 shown each time):

- metre → **m**
- kilogram → **kg**
- second → **s**
- kelvin → **K**
- ampere → **A**
- gram → **g**
- litre → **L**


Three generated variants:

> Match each unit with its symbol.

Right-hand side (shuffled): m · s · g · K
- gram → **g**
- second → **s**
- kelvin → **K**
- metre → **m**

Full working after a second miss:

> The right pairs are:  
> gram → g  
> second → s  
> kelvin → K  
> metre → m  

> Match each unit with its symbol.

Right-hand side (shuffled): L · kg · s · A
- litre → **L**
- second → **s**
- ampere → **A**
- kilogram → **kg**

Full working after a second miss:

> The right pairs are:  
> litre → L  
> second → s  
> ampere → A  
> kilogram → kg  

> Match each unit with its symbol.

Right-hand side (shuffled): m · kg · g · A
- kilogram → **kg**
- gram → **g**
- ampere → **A**
- metre → **m**

Full working after a second miss:

> The right pairs are:  
> kilogram → kg  
> gram → g  
> ampere → A  
> metre → m  

Sources: si-units (SI base units and prefixes (BIPM, The International System of Units))

### `p10-trap` · Lesson 10 · multiple choice, level 2

Prompt: Which sentence is true?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ The SI unit of mass is the kilogram.
- ✅ The SI unit of temperature is the kelvin.
- ✅ The SI unit of time is the second.
- ✅ The SI unit of length is the metre.
- ❌ The SI unit of mass is the gram.  
  _↳ The SI unit of mass is the kilogram (kg). The gram is a smaller unit._
- ❌ The SI unit of time is the minute.  
  _↳ The SI unit of time is the second (s)._
- ❌ The SI unit of temperature is the degree Celsius.  
  _↳ °C is used every day, but the SI unit is the kelvin (K)._
- ❌ The SI unit of length is the centimetre.  
  _↳ The SI unit of length is the metre (m)._


Three generated variants:

> Which sentence is true?

- ◻️ The SI unit of mass is the gram.  
  _↳ feedback if chosen: The SI unit of mass is the kilogram (kg). The gram is a smaller unit._
- ✅ The SI unit of mass is the kilogram.
- ◻️ The SI unit of temperature is the degree Celsius.  
  _↳ feedback if chosen: °C is used every day, but the SI unit is the kelvin (K)._
- ◻️ The SI unit of time is the minute.  
  _↳ feedback if chosen: The SI unit of time is the second (s)._

Full working after a second miss:

> The true statement is “The SI unit of mass is the kilogram.”.  
> “The SI unit of mass is the gram.” is false: The SI unit of mass is the kilogram (kg). The gram is a smaller unit.  
> “The SI unit of temperature is the degree Celsius.” is false: °C is used every day, but the SI unit is the kelvin (K).  
> “The SI unit of time is the minute.” is false: The SI unit of time is the second (s).  

> Which sentence is true?

- ◻️ The SI unit of time is the minute.  
  _↳ feedback if chosen: The SI unit of time is the second (s)._
- ◻️ The SI unit of length is the centimetre.  
  _↳ feedback if chosen: The SI unit of length is the metre (m)._
- ◻️ The SI unit of mass is the gram.  
  _↳ feedback if chosen: The SI unit of mass is the kilogram (kg). The gram is a smaller unit._
- ✅ The SI unit of temperature is the kelvin.

Full working after a second miss:

> The true statement is “The SI unit of temperature is the kelvin.”.  
> “The SI unit of time is the minute.” is false: The SI unit of time is the second (s).  
> “The SI unit of length is the centimetre.” is false: The SI unit of length is the metre (m).  
> “The SI unit of mass is the gram.” is false: The SI unit of mass is the kilogram (kg). The gram is a smaller unit.  

> Which sentence is true?

- ◻️ The SI unit of length is the centimetre.  
  _↳ feedback if chosen: The SI unit of length is the metre (m)._
- ◻️ The SI unit of time is the minute.  
  _↳ feedback if chosen: The SI unit of time is the second (s)._
- ✅ The SI unit of length is the metre.
- ◻️ The SI unit of mass is the gram.  
  _↳ feedback if chosen: The SI unit of mass is the kilogram (kg). The gram is a smaller unit._

Full working after a second miss:

> The true statement is “The SI unit of length is the metre.”.  
> “The SI unit of length is the centimetre.” is false: The SI unit of length is the metre (m).  
> “The SI unit of time is the minute.” is false: The SI unit of time is the second (s).  
> “The SI unit of mass is the gram.” is false: The SI unit of mass is the kilogram (kg). The gram is a smaller unit.  

Sources: si-units (SI base units and prefixes (BIPM, The International System of Units))

### `p11-sort` · Lesson 11 · matching, level 1

Prompt: Sort each one: solid, liquid or gas?

Pairs (6 shown each time, sorted into groups):

- stone → **solid**
- ice → **solid**
- wood → **solid**
- an iron nail → **solid**
- chalk → **solid**
- water → **liquid**
- palm oil → **liquid**
- kerosene → **liquid**
- milk → **liquid**
- honey → **liquid**
- air → **gas**
- water vapour (steam) → **gas**
- oxygen → **gas**
- carbon dioxide → **gas**


Three generated variants:

> Sort each one: solid, liquid or gas?

Groups: solid · liquid · gas
- oxygen → **gas**
- honey → **liquid**
- milk → **liquid**
- palm oil → **liquid**
- an iron nail → **solid**
- ice → **solid**

Full working after a second miss:

> The right pairs are:  
> oxygen → gas  
> honey → liquid  
> milk → liquid  
> palm oil → liquid  
> an iron nail → solid  
> ice → solid  

> Sort each one: solid, liquid or gas?

Groups: solid · liquid · gas
- ice → **solid**
- water vapour (steam) → **gas**
- an iron nail → **solid**
- oxygen → **gas**
- water → **liquid**
- milk → **liquid**

Full working after a second miss:

> The right pairs are:  
> ice → solid  
> water vapour (steam) → gas  
> an iron nail → solid  
> oxygen → gas  
> water → liquid  
> milk → liquid  

> Sort each one: solid, liquid or gas?

Groups: solid · gas
- stone → **solid**
- water vapour (steam) → **gas**
- air → **gas**
- ice → **solid**
- carbon dioxide → **gas**
- chalk → **solid**

Full working after a second miss:

> The right pairs are:  
> stone → solid  
> water vapour (steam) → gas  
> air → gas  
> ice → solid  
> carbon dioxide → gas  
> chalk → solid  

Sources: matter (States of matter, particle model, changes of state)

### `p11-prop` · Lesson 11 · multiple choice, level 1

Prompt: Which state of matter {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| has a fixed shape and a fixed volume | solid | A solid has a fixed shape and a fixed volume. |
| takes the shape of its container but keeps its volume | liquid | A liquid takes the shape of its container but keeps its volume. |
| spreads out to fill any container | gas | A gas spreads out to fill any container. |
| can be squashed (compressed) easily | gas | A gas can be squashed (compressed) easily. |
| can be poured but not squashed | liquid | A liquid can be poured but not squashed. |

Right answer: `{x.a}`; wrong choices: `solid`, `liquid`, `gas`

- Feedback `other`: “Not this state. Think: does it keep its shape? Its volume?”

Three generated variants:

> Which state of matter takes the shape of its container but keeps its volume?

- ◻️ gas  
  _↳ feedback if chosen: Not this state. Think: does it keep its shape? Its volume?_
- ◻️ solid  
  _↳ feedback if chosen: Not this state. Think: does it keep its shape? Its volume?_
- ✅ liquid

Full working after a second miss:

> A liquid takes the shape of its container but keeps its volume.  
> Answer: liquid.  

> Which state of matter takes the shape of its container but keeps its volume?

- ◻️ gas  
  _↳ feedback if chosen: Not this state. Think: does it keep its shape? Its volume?_
- ◻️ solid  
  _↳ feedback if chosen: Not this state. Think: does it keep its shape? Its volume?_
- ✅ liquid

Full working after a second miss:

> A liquid takes the shape of its container but keeps its volume.  
> Answer: liquid.  

> Which state of matter spreads out to fill any container?

- ◻️ liquid  
  _↳ feedback if chosen: Not this state. Think: does it keep its shape? Its volume?_
- ◻️ solid  
  _↳ feedback if chosen: Not this state. Think: does it keep its shape? Its volume?_
- ✅ gas

Full working after a second miss:

> A gas spreads out to fill any container.  
> Answer: gas.  

Sources: matter (States of matter, particle model, changes of state)

### `p11-particles` · Lesson 11 · multiple choice, level 2

Prompt: In which state are the particles {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| very close together, in fixed places; they only vibrate | solid | In a solid, the particles are very close together, in fixed places; they only vibrate. |
| close together, but able to move past each other | liquid | In a liquid, the particles are close together, but able to move past each other. |
| far apart, moving fast in all directions | gas | In a gas, the particles are far apart, moving fast in all directions. |

Right answer: `{x.a}`; wrong choices: `solid`, `liquid`, `gas`

- Feedback `other`: “Think about how close the particles are and how they move.”

Three generated variants:

> In which state are the particles close together, but able to move past each other?

- ◻️ gas  
  _↳ feedback if chosen: Think about how close the particles are and how they move._
- ◻️ solid  
  _↳ feedback if chosen: Think about how close the particles are and how they move._
- ✅ liquid

Full working after a second miss:

> In a liquid, the particles are close together, but able to move past each other.  
> Answer: liquid.  

> In which state are the particles far apart, moving fast in all directions?

- ◻️ liquid  
  _↳ feedback if chosen: Think about how close the particles are and how they move._
- ✅ gas
- ◻️ solid  
  _↳ feedback if chosen: Think about how close the particles are and how they move._

Full working after a second miss:

> In a gas, the particles are far apart, moving fast in all directions.  
> Answer: gas.  

> In which state are the particles far apart, moving fast in all directions?

- ✅ gas
- ◻️ solid  
  _↳ feedback if chosen: Think about how close the particles are and how they move._
- ◻️ liquid  
  _↳ feedback if chosen: Think about how close the particles are and how they move._

Full working after a second miss:

> In a gas, the particles are far apart, moving fast in all directions.  
> Answer: gas.  

Sources: matter (States of matter, particle model, changes of state)

### `p11-why` · Lesson 11 · multiple choice, level 2

Prompt: Why can a gas be squashed (compressed) but a liquid cannot?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ The particles of a gas are far apart; those of a liquid are already close together.
- ❌ Gases are always hot.  
  _↳ Gases can be cold. It is about the space between the particles._
- ❌ Liquids are heavier than gases.  
  _↳ It is not about weight but about the space between the particles._
- ❌ Gases have no particles.  
  _↳ Gases are made of particles too, but they are far apart._


Three generated variants:

> Why can a gas be squashed (compressed) but a liquid cannot?

- ✅ The particles of a gas are far apart; those of a liquid are already close together.
- ◻️ Liquids are heavier than gases.  
  _↳ feedback if chosen: It is not about weight but about the space between the particles._
- ◻️ Gases are always hot.  
  _↳ feedback if chosen: Gases can be cold. It is about the space between the particles._
- ◻️ Gases have no particles.  
  _↳ feedback if chosen: Gases are made of particles too, but they are far apart._

Full working after a second miss:

> The true statement is “The particles of a gas are far apart; those of a liquid are already close together.”.  
> “Liquids are heavier than gases.” is false: It is not about weight but about the space between the particles.  
> “Gases are always hot.” is false: Gases can be cold. It is about the space between the particles.  
> “Gases have no particles.” is false: Gases are made of particles too, but they are far apart.  

> Why can a gas be squashed (compressed) but a liquid cannot?

- ◻️ Gases have no particles.  
  _↳ feedback if chosen: Gases are made of particles too, but they are far apart._
- ✅ The particles of a gas are far apart; those of a liquid are already close together.
- ◻️ Liquids are heavier than gases.  
  _↳ feedback if chosen: It is not about weight but about the space between the particles._
- ◻️ Gases are always hot.  
  _↳ feedback if chosen: Gases can be cold. It is about the space between the particles._

Full working after a second miss:

> The true statement is “The particles of a gas are far apart; those of a liquid are already close together.”.  
> “Gases have no particles.” is false: Gases are made of particles too, but they are far apart.  
> “Liquids are heavier than gases.” is false: It is not about weight but about the space between the particles.  
> “Gases are always hot.” is false: Gases can be cold. It is about the space between the particles.  

> Why can a gas be squashed (compressed) but a liquid cannot?

- ◻️ Liquids are heavier than gases.  
  _↳ feedback if chosen: It is not about weight but about the space between the particles._
- ◻️ Gases are always hot.  
  _↳ feedback if chosen: Gases can be cold. It is about the space between the particles._
- ✅ The particles of a gas are far apart; those of a liquid are already close together.
- ◻️ Gases have no particles.  
  _↳ feedback if chosen: Gases are made of particles too, but they are far apart._

Full working after a second miss:

> The true statement is “The particles of a gas are far apart; those of a liquid are already close together.”.  
> “Liquids are heavier than gases.” is false: It is not about weight but about the space between the particles.  
> “Gases are always hot.” is false: Gases can be cold. It is about the space between the particles.  
> “Gases have no particles.” is false: Gases are made of particles too, but they are far apart.  

Sources: matter (States of matter, particle model, changes of state)

### `p11-spot` · Lesson 11 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Palm oil takes the shape of the bottle it is in.
- ✅ Air spreads out to fill a room.
- ✅ A stone keeps its shape.
- ✅ Water, ice and steam are the same substance.
- ❌ A solid takes the shape of its container.  
  _↳ A solid keeps its own shape. It is a liquid that takes the shape of its container._
- ❌ The particles in a gas are very close together.  
  _↳ In a gas the particles are far apart._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ The particles in a gas are very close together.  
  _↳ explanation: In a gas the particles are far apart._
- ◻️ Palm oil takes the shape of the bottle it is in.
- ◻️ Water, ice and steam are the same substance.
- ◻️ Air spreads out to fill a room.

Full working after a second miss:

> The wrong statement is “The particles in a gas are very close together.”.  
> In a gas the particles are far apart.  

> One sentence is wrong. Which one?

- ✅ A solid takes the shape of its container.  
  _↳ explanation: A solid keeps its own shape. It is a liquid that takes the shape of its container._
- ◻️ A stone keeps its shape.
- ◻️ Water, ice and steam are the same substance.
- ◻️ Air spreads out to fill a room.

Full working after a second miss:

> The wrong statement is “A solid takes the shape of its container.”.  
> A solid keeps its own shape. It is a liquid that takes the shape of its container.  

> One sentence is wrong. Which one?

- ◻️ A stone keeps its shape.
- ◻️ Water, ice and steam are the same substance.
- ◻️ Palm oil takes the shape of the bottle it is in.
- ✅ A solid takes the shape of its container.  
  _↳ explanation: A solid keeps its own shape. It is a liquid that takes the shape of its container._

Full working after a second miss:

> The wrong statement is “A solid takes the shape of its container.”.  
> A solid keeps its own shape. It is a liquid that takes the shape of its container.  

Sources: matter (States of matter, particle model, changes of state)

### `pc11-3-check` · Lesson 11 · multiple choice, level 1

Prompt: In which state are the particles {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| very close together, in fixed places; they only vibrate | solid | In a solid, the particles are very close together, in fixed places; they only vibrate. |
| close together, but able to move past each other | liquid | In a liquid, the particles are close together, but able to move past each other. |
| far apart, moving fast in all directions | gas | In a gas, the particles are far apart, moving fast in all directions. |

Right answer: `{x.a}`; wrong choices: `solid`, `liquid`, `gas`

- Feedback `other`: “Think about how close the particles are and how they move.”

Three generated variants:

> In which state are the particles very close together, in fixed places; they only vibrate?

- ✅ solid
- ◻️ gas  
  _↳ feedback if chosen: Think about how close the particles are and how they move._
- ◻️ liquid  
  _↳ feedback if chosen: Think about how close the particles are and how they move._

Full working after a second miss:

> In a solid, the particles are very close together, in fixed places; they only vibrate.  
> Answer: solid.  

> In which state are the particles close together, but able to move past each other?

- ✅ liquid
- ◻️ gas  
  _↳ feedback if chosen: Think about how close the particles are and how they move._
- ◻️ solid  
  _↳ feedback if chosen: Think about how close the particles are and how they move._

Full working after a second miss:

> In a liquid, the particles are close together, but able to move past each other.  
> Answer: liquid.  

> In which state are the particles close together, but able to move past each other?

- ◻️ gas  
  _↳ feedback if chosen: Think about how close the particles are and how they move._
- ◻️ solid  
  _↳ feedback if chosen: Think about how close the particles are and how they move._
- ✅ liquid

Full working after a second miss:

> In a liquid, the particles are close together, but able to move past each other.  
> Answer: liquid.  

Sources: matter (States of matter, particle model, changes of state)

### `p12-example` · Lesson 12 · multiple choice, level 1

Prompt: {x.t} What is this change of state called?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| An ice cube in a cold drink gets smaller and smaller. | melting | An ice cube in a cold drink gets smaller and smaller. This is melting. |
| Water in a pot on the fire boils away. | evaporation | Water in a pot on the fire boils away. This is evaporation. |
| In the morning, there are drops of dew on the grass. | condensation | In the morning, there are drops of dew on the grass. This is condensation. |
| Palm oil turns solid on a cold morning in Bamenda. | freezing | Palm oil turns solid on a cold morning in Bamenda. This is freezing. |
| Mothballs (naphthalene) in a wardrobe get smaller without leaving any liquid. | sublimation | Mothballs (naphthalene) in a wardrobe get smaller without leaving any liquid. This is sublimation. |
| Water drops form on the outside of a cold bottle of water. | condensation | Water drops form on the outside of a cold bottle of water. This is condensation. |
| Wet clothes dry on the line. | evaporation | Wet clothes dry on the line. This is evaporation. |
| Hot candle wax becomes hard again. | freezing | Hot candle wax becomes hard again. This is freezing. |

Right answer: `{x.a}`; wrong choices: `melting`, `freezing`, `evaporation`, `condensation`, `sublimation`

- Feedback `other`: “Not this change. Which state does it start in, and which state does it end in?”

Three generated variants:

> Water in a pot on the fire boils away. What is this change of state called?

- ◻️ sublimation  
  _↳ feedback if chosen: Not this change. Which state does it start in, and which state does it end in?_
- ◻️ melting  
  _↳ feedback if chosen: Not this change. Which state does it start in, and which state does it end in?_
- ◻️ condensation  
  _↳ feedback if chosen: Not this change. Which state does it start in, and which state does it end in?_
- ✅ evaporation

Full working after a second miss:

> Water in a pot on the fire boils away. This is evaporation.  
> Answer: evaporation.  

> Wet clothes dry on the line. What is this change of state called?

- ◻️ melting  
  _↳ feedback if chosen: Not this change. Which state does it start in, and which state does it end in?_
- ◻️ freezing  
  _↳ feedback if chosen: Not this change. Which state does it start in, and which state does it end in?_
- ◻️ condensation  
  _↳ feedback if chosen: Not this change. Which state does it start in, and which state does it end in?_
- ✅ evaporation

Full working after a second miss:

> Wet clothes dry on the line. This is evaporation.  
> Answer: evaporation.  

> In the morning, there are drops of dew on the grass. What is this change of state called?

- ◻️ sublimation  
  _↳ feedback if chosen: Not this change. Which state does it start in, and which state does it end in?_
- ◻️ freezing  
  _↳ feedback if chosen: Not this change. Which state does it start in, and which state does it end in?_
- ✅ condensation
- ◻️ evaporation  
  _↳ feedback if chosen: Not this change. Which state does it start in, and which state does it end in?_

Full working after a second miss:

> In the morning, there are drops of dew on the grass. This is condensation.  
> Answer: condensation.  

Sources: matter (States of matter, particle model, changes of state)

### `p12-spot` · Lesson 12 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Melting changes a solid into a liquid.
- ✅ Condensation changes a gas into a liquid.
- ✅ Evaporation takes in heat.
- ✅ Dew forms by condensation.
- ❌ Freezing changes a gas into a solid.  
  _↳ Freezing changes a liquid into a solid. Gas → solid is deposition._
- ❌ Wet clothes dry by condensation.  
  _↳ Wet clothes dry by evaporation: liquid → gas._
- ❌ Melting gives out heat.  
  _↳ Melting takes in heat._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Dew forms by condensation.
- ✅ Wet clothes dry by condensation.  
  _↳ explanation: Wet clothes dry by evaporation: liquid → gas._
- ◻️ Evaporation takes in heat.
- ◻️ Melting changes a solid into a liquid.

Full working after a second miss:

> The wrong statement is “Wet clothes dry by condensation.”.  
> Wet clothes dry by evaporation: liquid → gas.  

> One sentence is wrong. Which one?

- ◻️ Evaporation takes in heat.
- ◻️ Condensation changes a gas into a liquid.
- ◻️ Melting changes a solid into a liquid.
- ✅ Melting gives out heat.  
  _↳ explanation: Melting takes in heat._

Full working after a second miss:

> The wrong statement is “Melting gives out heat.”.  
> Melting takes in heat.  

> One sentence is wrong. Which one?

- ◻️ Dew forms by condensation.
- ◻️ Melting changes a solid into a liquid.
- ◻️ Evaporation takes in heat.
- ✅ Freezing changes a gas into a solid.  
  _↳ explanation: Freezing changes a liquid into a solid. Gas → solid is deposition._

Full working after a second miss:

> The wrong statement is “Freezing changes a gas into a solid.”.  
> Freezing changes a liquid into a solid. Gas → solid is deposition.  

Sources: matter (States of matter, particle model, changes of state)

### `p13-tool` · Lesson 13 · multiple choice, level 1

Prompt: Which instrument is best to measure {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| the length of a pencil | ruler | For the length of a pencil, a ruler is best. |
| the length of the classroom | measuring tape | For the length of the classroom, a measuring tape is best. |
| the width of your desk | metre rule | For the width of your desk, a metre rule is best. |
| the length of the school football field | measuring tape | For the length of the school football field, a measuring tape is best. |

Right answer: `{x.a}`; wrong choices: `ruler`, `metre rule`, `measuring tape`, `balance`

- Feedback `other`: “That instrument is too short, too long, or measures something else.”

Three generated variants:

> Which instrument is best to measure the length of the school football field?

- ◻️ ruler  
  _↳ feedback if chosen: That instrument is too short, too long, or measures something else._
- ✅ measuring tape
- ◻️ metre rule  
  _↳ feedback if chosen: That instrument is too short, too long, or measures something else._
- ◻️ balance  
  _↳ feedback if chosen: That instrument is too short, too long, or measures something else._

Full working after a second miss:

> For the length of the school football field, a measuring tape is best.  
> Answer: measuring tape.  

> Which instrument is best to measure the width of your desk?

- ◻️ ruler  
  _↳ feedback if chosen: That instrument is too short, too long, or measures something else._
- ◻️ measuring tape  
  _↳ feedback if chosen: That instrument is too short, too long, or measures something else._
- ✅ metre rule
- ◻️ balance  
  _↳ feedback if chosen: That instrument is too short, too long, or measures something else._

Full working after a second miss:

> For the width of your desk, a metre rule is best.  
> Answer: metre rule.  

> Which instrument is best to measure the length of a pencil?

- ◻️ balance  
  _↳ feedback if chosen: That instrument is too short, too long, or measures something else._
- ◻️ metre rule  
  _↳ feedback if chosen: That instrument is too short, too long, or measures something else._
- ◻️ measuring tape  
  _↳ feedback if chosen: That instrument is too short, too long, or measures something else._
- ✅ ruler

Full working after a second miss:

> For the length of a pencil, a ruler is best.  
> Answer: ruler.  

Sources: measurement (Measuring with instruments; reading a scale; parallax)

### `pc14-1-check` · Lesson 14 · multiple choice, level 1

Prompt: What is mass?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ The quantity of matter in a body.
- ❌ How hot a body is.  
  _↳ That is temperature._
- ❌ The space a body takes up.  
  _↳ That is volume._
- ❌ The pull of the Earth on a body.  
  _↳ That is weight, a force._


Three generated variants:

> What is mass?

- ◻️ How hot a body is.  
  _↳ feedback if chosen: That is temperature._
- ◻️ The pull of the Earth on a body.  
  _↳ feedback if chosen: That is weight, a force._
- ✅ The quantity of matter in a body.
- ◻️ The space a body takes up.  
  _↳ feedback if chosen: That is volume._

Full working after a second miss:

> The true statement is “The quantity of matter in a body.”.  
> “How hot a body is.” is false: That is temperature.  
> “The pull of the Earth on a body.” is false: That is weight, a force.  
> “The space a body takes up.” is false: That is volume.  

> What is mass?

- ◻️ The space a body takes up.  
  _↳ feedback if chosen: That is volume._
- ◻️ The pull of the Earth on a body.  
  _↳ feedback if chosen: That is weight, a force._
- ◻️ How hot a body is.  
  _↳ feedback if chosen: That is temperature._
- ✅ The quantity of matter in a body.

Full working after a second miss:

> The true statement is “The quantity of matter in a body.”.  
> “The space a body takes up.” is false: That is volume.  
> “The pull of the Earth on a body.” is false: That is weight, a force.  
> “How hot a body is.” is false: That is temperature.  

> What is mass?

- ◻️ The pull of the Earth on a body.  
  _↳ feedback if chosen: That is weight, a force._
- ◻️ The space a body takes up.  
  _↳ feedback if chosen: That is volume._
- ✅ The quantity of matter in a body.
- ◻️ How hot a body is.  
  _↳ feedback if chosen: That is temperature._

Full working after a second miss:

> The true statement is “The quantity of matter in a body.”.  
> “The pull of the Earth on a body.” is false: That is weight, a force.  
> “The space a body takes up.” is false: That is volume.  
> “How hot a body is.” is false: That is temperature.  

Sources: mass (Mass: quantity of matter; balances)

### `p15-diff` · Lesson 15 · matching, level 1

Prompt: Does each sentence describe mass or weight?

Pairs (6 shown each time, sorted into groups):

- the quantity of matter in a body → **mass**
- measured in kilograms → **mass**
- measured with a beam balance → **mass**
- the same everywhere → **mass**
- a force: the pull of gravity → **weight**
- measured in newtons → **weight**
- measured with a spring balance → **weight**
- smaller on the Moon → **weight**


Three generated variants:

> Does each sentence describe mass or weight?

Groups: mass · weight
- measured in kilograms → **mass**
- smaller on the Moon → **weight**
- the quantity of matter in a body → **mass**
- a force: the pull of gravity → **weight**
- measured in newtons → **weight**
- the same everywhere → **mass**

Full working after a second miss:

> The right pairs are:  
> measured in kilograms → mass  
> smaller on the Moon → weight  
> the quantity of matter in a body → mass  
> a force: the pull of gravity → weight  
> measured in newtons → weight  
> the same everywhere → mass  

> Does each sentence describe mass or weight?

Groups: mass · weight
- the quantity of matter in a body → **mass**
- a force: the pull of gravity → **weight**
- measured in kilograms → **mass**
- measured with a beam balance → **mass**
- the same everywhere → **mass**
- measured in newtons → **weight**

Full working after a second miss:

> The right pairs are:  
> the quantity of matter in a body → mass  
> a force: the pull of gravity → weight  
> measured in kilograms → mass  
> measured with a beam balance → mass  
> the same everywhere → mass  
> measured in newtons → weight  

> Does each sentence describe mass or weight?

Groups: mass · weight
- smaller on the Moon → **weight**
- measured in kilograms → **mass**
- measured with a beam balance → **mass**
- a force: the pull of gravity → **weight**
- the quantity of matter in a body → **mass**
- measured with a spring balance → **weight**

Full working after a second miss:

> The right pairs are:  
> smaller on the Moon → weight  
> measured in kilograms → mass  
> measured with a beam balance → mass  
> a force: the pull of gravity → weight  
> the quantity of matter in a body → mass  
> measured with a spring balance → weight  

Sources: weight (Weight W = m × g with g = 10 N/kg on Earth; g on the Moon about 1.6 N/kg)

### `p15-spot` · Lesson 15 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Weight is measured in newtons.
- ✅ A spring balance measures weight.
- ✅ Mass is the same on the Moon as on Earth.
- ✅ Weight is a force.
- ❌ Weight is measured in kilograms.  
  _↳ Weight is a force, measured in newtons (N). Kilograms measure mass._
- ❌ Mass is smaller on the Moon.  
  _↳ Mass is the same everywhere. It is weight that is smaller on the Moon._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Mass is the same on the Moon as on Earth.
- ◻️ Weight is a force.
- ✅ Mass is smaller on the Moon.  
  _↳ explanation: Mass is the same everywhere. It is weight that is smaller on the Moon._
- ◻️ A spring balance measures weight.

Full working after a second miss:

> The wrong statement is “Mass is smaller on the Moon.”.  
> Mass is the same everywhere. It is weight that is smaller on the Moon.  

> One sentence is wrong. Which one?

- ◻️ Weight is measured in newtons.
- ◻️ Weight is a force.
- ✅ Mass is smaller on the Moon.  
  _↳ explanation: Mass is the same everywhere. It is weight that is smaller on the Moon._
- ◻️ A spring balance measures weight.

Full working after a second miss:

> The wrong statement is “Mass is smaller on the Moon.”.  
> Mass is the same everywhere. It is weight that is smaller on the Moon.  

> One sentence is wrong. Which one?

- ✅ Mass is smaller on the Moon.  
  _↳ explanation: Mass is the same everywhere. It is weight that is smaller on the Moon._
- ◻️ A spring balance measures weight.
- ◻️ Weight is a force.
- ◻️ Weight is measured in newtons.

Full working after a second miss:

> The wrong statement is “Mass is smaller on the Moon.”.  
> Mass is the same everywhere. It is weight that is smaller on the Moon.  

Sources: weight (Weight W = m × g with g = 10 N/kg on Earth; g on the Moon about 1.6 N/kg)

### `pc15-3-check` · Lesson 15 · multiple choice, level 1

Prompt: An astronaut goes from the Earth to the Moon. What happens?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Her weight gets smaller, but her mass stays the same.
- ❌ Her mass gets smaller, but her weight stays the same.  
  _↳ Mass is the matter in her body: it does not change. The Moon pulls less, so her weight changes._
- ❌ Both her mass and her weight stay the same.  
  _↳ The Moon pulls less than the Earth, so her weight is smaller._
- ❌ Her mass and weight both become zero.  
  _↳ The Moon still pulls on her, and her body still has matter._


Three generated variants:

> An astronaut goes from the Earth to the Moon. What happens?

- ◻️ Both her mass and her weight stay the same.  
  _↳ feedback if chosen: The Moon pulls less than the Earth, so her weight is smaller._
- ◻️ Her mass and weight both become zero.  
  _↳ feedback if chosen: The Moon still pulls on her, and her body still has matter._
- ◻️ Her mass gets smaller, but her weight stays the same.  
  _↳ feedback if chosen: Mass is the matter in her body: it does not change. The Moon pulls less, so her weight changes._
- ✅ Her weight gets smaller, but her mass stays the same.

Full working after a second miss:

> The true statement is “Her weight gets smaller, but her mass stays the same.”.  
> “Both her mass and her weight stay the same.” is false: The Moon pulls less than the Earth, so her weight is smaller.  
> “Her mass and weight both become zero.” is false: The Moon still pulls on her, and her body still has matter.  
> “Her mass gets smaller, but her weight stays the same.” is false: Mass is the matter in her body: it does not change. The Moon pulls less, so her weight changes.  

> An astronaut goes from the Earth to the Moon. What happens?

- ✅ Her weight gets smaller, but her mass stays the same.
- ◻️ Her mass and weight both become zero.  
  _↳ feedback if chosen: The Moon still pulls on her, and her body still has matter._
- ◻️ Her mass gets smaller, but her weight stays the same.  
  _↳ feedback if chosen: Mass is the matter in her body: it does not change. The Moon pulls less, so her weight changes._
- ◻️ Both her mass and her weight stay the same.  
  _↳ feedback if chosen: The Moon pulls less than the Earth, so her weight is smaller._

Full working after a second miss:

> The true statement is “Her weight gets smaller, but her mass stays the same.”.  
> “Her mass and weight both become zero.” is false: The Moon still pulls on her, and her body still has matter.  
> “Her mass gets smaller, but her weight stays the same.” is false: Mass is the matter in her body: it does not change. The Moon pulls less, so her weight changes.  
> “Both her mass and her weight stay the same.” is false: The Moon pulls less than the Earth, so her weight is smaller.  

> An astronaut goes from the Earth to the Moon. What happens?

- ◻️ Her mass and weight both become zero.  
  _↳ feedback if chosen: The Moon still pulls on her, and her body still has matter._
- ✅ Her weight gets smaller, but her mass stays the same.
- ◻️ Her mass gets smaller, but her weight stays the same.  
  _↳ feedback if chosen: Mass is the matter in her body: it does not change. The Moon pulls less, so her weight changes._
- ◻️ Both her mass and her weight stay the same.  
  _↳ feedback if chosen: The Moon pulls less than the Earth, so her weight is smaller._

Full working after a second miss:

> The true statement is “Her weight gets smaller, but her mass stays the same.”.  
> “Her mass and weight both become zero.” is false: The Moon still pulls on her, and her body still has matter.  
> “Her mass gets smaller, but her weight stays the same.” is false: Mass is the matter in her body: it does not change. The Moon pulls less, so her weight changes.  
> “Both her mass and her weight stay the same.” is false: The Moon pulls less than the Earth, so her weight is smaller.  

Sources: weight (Weight W = m × g with g = 10 N/kg on Earth; g on the Moon about 1.6 N/kg)

### `p17-spot` · Lesson 17 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Density = mass ÷ volume.
- ✅ Ice floats because it is less dense than water.
- ✅ 1 g/cm³ = 1000 kg/m³.
- ✅ A body denser than water sinks.
- ❌ A big log sinks because it is heavy.  
  _↳ Size does not decide: wood floats because its density is less than water's._
- ❌ Density = mass × volume.  
  _↳ Density = mass ÷ volume._
- ❌ Iron floats in water.  
  _↳ Iron (about 7.9 g/cm³) is denser than water: it sinks._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ 1 g/cm³ = 1000 kg/m³.
- ◻️ Ice floats because it is less dense than water.
- ◻️ A body denser than water sinks.
- ✅ A big log sinks because it is heavy.  
  _↳ explanation: Size does not decide: wood floats because its density is less than water's._

Full working after a second miss:

> The wrong statement is “A big log sinks because it is heavy.”.  
> Size does not decide: wood floats because its density is less than water's.  

> One sentence is wrong. Which one?

- ◻️ Ice floats because it is less dense than water.
- ◻️ 1 g/cm³ = 1000 kg/m³.
- ◻️ Density = mass ÷ volume.
- ✅ Density = mass × volume.  
  _↳ explanation: Density = mass ÷ volume._

Full working after a second miss:

> The wrong statement is “Density = mass × volume.”.  
> Density = mass ÷ volume.  

> One sentence is wrong. Which one?

- ◻️ A body denser than water sinks.
- ◻️ Density = mass ÷ volume.
- ◻️ Ice floats because it is less dense than water.
- ✅ Iron floats in water.  
  _↳ explanation: Iron (about 7.9 g/cm³) is denser than water: it sinks._

Full working after a second miss:

> The wrong statement is “Iron floats in water.”.  
> Iron (about 7.9 g/cm³) is denser than water: it sinks.  

Sources: density (Density = mass ÷ volume; water 1 g/cm³; approximate densities of ice, kerosene, iron)

### `p18-spot` · Lesson 18 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The SI unit of temperature is the kelvin.
- ✅ 0 °C = 273 K.
- ✅ Pure water boils at 100 °C at normal air pressure.
- ✅ The liquid in a thermometer rises when it gets warmer.
- ❌ To change °C into kelvin, subtract 273.  
  _↳ From °C to K, add 273: 0 °C = 273 K._
- ❌ Pure ice melts at 100 °C.  
  _↳ Pure ice melts at 0 °C._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ To change °C into kelvin, subtract 273.  
  _↳ explanation: From °C to K, add 273: 0 °C = 273 K._
- ◻️ The SI unit of temperature is the kelvin.
- ◻️ 0 °C = 273 K.
- ◻️ The liquid in a thermometer rises when it gets warmer.

Full working after a second miss:

> The wrong statement is “To change °C into kelvin, subtract 273.”.  
> From °C to K, add 273: 0 °C = 273 K.  

> One sentence is wrong. Which one?

- ✅ Pure ice melts at 100 °C.  
  _↳ explanation: Pure ice melts at 0 °C._
- ◻️ The SI unit of temperature is the kelvin.
- ◻️ Pure water boils at 100 °C at normal air pressure.
- ◻️ 0 °C = 273 K.

Full working after a second miss:

> The wrong statement is “Pure ice melts at 100 °C.”.  
> Pure ice melts at 0 °C.  

> One sentence is wrong. Which one?

- ◻️ The SI unit of temperature is the kelvin.
- ◻️ Pure water boils at 100 °C at normal air pressure.
- ✅ Pure ice melts at 100 °C.  
  _↳ explanation: Pure ice melts at 0 °C._
- ◻️ 0 °C = 273 K.

Full working after a second miss:

> The wrong statement is “Pure ice melts at 100 °C.”.  
> Pure ice melts at 0 °C.  

Sources: temperature (Temperature, kelvin and Celsius (T(K) = T(°C) + 273), fixed points)

### `pc18-3-check` · Lesson 18 · multiple choice, level 1

Prompt: At normal air pressure, pure water boils at:

Shows 1 true and 3 false statement(s), drawn from:

- ✅ 100 °C
- ❌ 0 °C  
  _↳ 0 °C is where pure ice melts._
- ❌ 37 °C  
  _↳ 37 °C is about normal body temperature._
- ❌ 273 °C  
  _↳ 273 is the number added to change °C into kelvin._


Three generated variants:

> At normal air pressure, pure water boils at:

- ◻️ 0 °C  
  _↳ feedback if chosen: 0 °C is where pure ice melts._
- ✅ 100 °C
- ◻️ 273 °C  
  _↳ feedback if chosen: 273 is the number added to change °C into kelvin._
- ◻️ 37 °C  
  _↳ feedback if chosen: 37 °C is about normal body temperature._

Full working after a second miss:

> The true statement is “100 °C”.  
> “0 °C” is false: 0 °C is where pure ice melts.  
> “273 °C” is false: 273 is the number added to change °C into kelvin.  
> “37 °C” is false: 37 °C is about normal body temperature.  

> At normal air pressure, pure water boils at:

- ◻️ 273 °C  
  _↳ feedback if chosen: 273 is the number added to change °C into kelvin._
- ◻️ 0 °C  
  _↳ feedback if chosen: 0 °C is where pure ice melts._
- ◻️ 37 °C  
  _↳ feedback if chosen: 37 °C is about normal body temperature._
- ✅ 100 °C

Full working after a second miss:

> The true statement is “100 °C”.  
> “273 °C” is false: 273 is the number added to change °C into kelvin.  
> “0 °C” is false: 0 °C is where pure ice melts.  
> “37 °C” is false: 37 °C is about normal body temperature.  

> At normal air pressure, pure water boils at:

- ✅ 100 °C
- ◻️ 37 °C  
  _↳ feedback if chosen: 37 °C is about normal body temperature._
- ◻️ 0 °C  
  _↳ feedback if chosen: 0 °C is where pure ice melts._
- ◻️ 273 °C  
  _↳ feedback if chosen: 273 is the number added to change °C into kelvin._

Full working after a second miss:

> The true statement is “100 °C”.  
> “37 °C” is false: 37 °C is about normal body temperature.  
> “0 °C” is false: 0 °C is where pure ice melts.  
> “273 °C” is false: 273 is the number added to change °C into kelvin.  

Sources: temperature (Temperature, kelvin and Celsius (T(K) = T(°C) + 273), fixed points)

### `p19-symbol` · Lesson 19 · matching, level 1

Prompt: Match each hazard symbol (described in words) with what it means.

Pairs (4 shown each time):

- a flame → **flammable: catches fire easily**
- a skull and crossbones → **toxic: poisonous**
- liquid dripping onto a hand and a metal bar → **corrosive: burns skin and eats metal**
- an exclamation mark → **harmful or irritant: can hurt skin, eyes or breathing**
- a gas bottle → **gas under pressure: can burst if heated**
- a dead tree and a dead fish → **dangerous for the environment**
- an exploding bomb → **explosive**


Three generated variants:

> Match each hazard symbol (described in words) with what it means.

Right-hand side (shuffled): corrosive: burns skin and eats metal · harmful or irritant: can hurt skin, eyes or breathing · toxic: poisonous · flammable: catches fire easily
- a flame → **flammable: catches fire easily**
- an exclamation mark → **harmful or irritant: can hurt skin, eyes or breathing**
- liquid dripping onto a hand and a metal bar → **corrosive: burns skin and eats metal**
- a skull and crossbones → **toxic: poisonous**

Full working after a second miss:

> The right pairs are:  
> a flame → flammable: catches fire easily  
> an exclamation mark → harmful or irritant: can hurt skin, eyes or breathing  
> liquid dripping onto a hand and a metal bar → corrosive: burns skin and eats metal  
> a skull and crossbones → toxic: poisonous  

> Match each hazard symbol (described in words) with what it means.

Right-hand side (shuffled): gas under pressure: can burst if heated · flammable: catches fire easily · dangerous for the environment · corrosive: burns skin and eats metal
- a flame → **flammable: catches fire easily**
- liquid dripping onto a hand and a metal bar → **corrosive: burns skin and eats metal**
- a gas bottle → **gas under pressure: can burst if heated**
- a dead tree and a dead fish → **dangerous for the environment**

Full working after a second miss:

> The right pairs are:  
> a flame → flammable: catches fire easily  
> liquid dripping onto a hand and a metal bar → corrosive: burns skin and eats metal  
> a gas bottle → gas under pressure: can burst if heated  
> a dead tree and a dead fish → dangerous for the environment  

> Match each hazard symbol (described in words) with what it means.

Right-hand side (shuffled): explosive · toxic: poisonous · corrosive: burns skin and eats metal · dangerous for the environment
- a skull and crossbones → **toxic: poisonous**
- liquid dripping onto a hand and a metal bar → **corrosive: burns skin and eats metal**
- a dead tree and a dead fish → **dangerous for the environment**
- an exploding bomb → **explosive**

Full working after a second miss:

> The right pairs are:  
> a skull and crossbones → toxic: poisonous  
> liquid dripping onto a hand and a metal bar → corrosive: burns skin and eats metal  
> a dead tree and a dead fish → dangerous for the environment  
> an exploding bomb → explosive  

Sources: hazards (Hazard pictograms (UN Globally Harmonized System), described in words; reading product labels)

### `p19-label-l1` · Lesson 19 · multiple choice, level 1

Prompt: A label says {x.t} What does this part of the label tell you?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| “Keep out of reach of children.” | a warning | “Keep out of reach of children.” tells a warning. |
| “Use before 03/2027.” | the expiry date | “Use before 03/2027.” tells the expiry date. |
| “Store in a cool, dry place.” | how to store it | “Store in a cool, dry place.” tells how to store it. |
| “Shake well before use.” | how to use it | “Shake well before use.” tells how to use it. |
| “Made by … , Douala, Cameroon.” | who made it | “Made by … , Douala, Cameroon.” tells who made it. |

Right answer: `{x.a}`; wrong choices: `a warning`, `the expiry date`, `how to store it`, `how to use it`, `who made it`

- Feedback `other`: “That is a different part of the label.”

Three generated variants:

> A label says “Keep out of reach of children.” What does this part of the label tell you?

- ◻️ who made it  
  _↳ feedback if chosen: That is a different part of the label._
- ◻️ how to use it  
  _↳ feedback if chosen: That is a different part of the label._
- ✅ a warning
- ◻️ how to store it  
  _↳ feedback if chosen: That is a different part of the label._

Full working after a second miss:

> “Keep out of reach of children.” tells a warning.  
> Answer: a warning.  

> A label says “Store in a cool, dry place.” What does this part of the label tell you?

- ◻️ a warning  
  _↳ feedback if chosen: That is a different part of the label._
- ✅ how to store it
- ◻️ who made it  
  _↳ feedback if chosen: That is a different part of the label._
- ◻️ the expiry date  
  _↳ feedback if chosen: That is a different part of the label._

Full working after a second miss:

> “Store in a cool, dry place.” tells how to store it.  
> Answer: how to store it.  

> A label says “Use before 03/2027.” What does this part of the label tell you?

- ◻️ how to store it  
  _↳ feedback if chosen: That is a different part of the label._
- ◻️ how to use it  
  _↳ feedback if chosen: That is a different part of the label._
- ✅ the expiry date
- ◻️ a warning  
  _↳ feedback if chosen: That is a different part of the label._

Full working after a second miss:

> “Use before 03/2027.” tells the expiry date.  
> Answer: the expiry date.  

Sources: hazards (Hazard pictograms (UN Globally Harmonized System), described in words; reading product labels)

### `p19-product` · Lesson 19 · multiple choice, level 1

Prompt: Which danger does {x.t} have?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| kerosene or petrol | flammable: catches fire easily | kerosene or petrol: flammable: catches fire easily. |
| rat poison | toxic: poisonous | rat poison: toxic: poisonous. |
| acid from a car battery | corrosive: burns skin and eats metal | acid from a car battery: corrosive: burns skin and eats metal. |
| a cooking-gas bottle | gas under pressure: can burst if heated | a cooking-gas bottle: gas under pressure: can burst if heated. |

Right answer: `{x.a}`; wrong choices: `flammable: catches fire easily`, `toxic: poisonous`, `corrosive: burns skin and eats metal`, `gas under pressure: can burst if heated`

- Feedback `other`: “That warning is for a different product.”

Three generated variants:

> Which danger does kerosene or petrol have?

- ◻️ gas under pressure: can burst if heated  
  _↳ feedback if chosen: That warning is for a different product._
- ◻️ corrosive: burns skin and eats metal  
  _↳ feedback if chosen: That warning is for a different product._
- ◻️ toxic: poisonous  
  _↳ feedback if chosen: That warning is for a different product._
- ✅ flammable: catches fire easily

Full working after a second miss:

> kerosene or petrol: flammable: catches fire easily.  
> Answer: flammable: catches fire easily.  

> Which danger does rat poison have?

- ✅ toxic: poisonous
- ◻️ gas under pressure: can burst if heated  
  _↳ feedback if chosen: That warning is for a different product._
- ◻️ flammable: catches fire easily  
  _↳ feedback if chosen: That warning is for a different product._
- ◻️ corrosive: burns skin and eats metal  
  _↳ feedback if chosen: That warning is for a different product._

Full working after a second miss:

> rat poison: toxic: poisonous.  
> Answer: toxic: poisonous.  

> Which danger does acid from a car battery have?

- ◻️ toxic: poisonous  
  _↳ feedback if chosen: That warning is for a different product._
- ✅ corrosive: burns skin and eats metal
- ◻️ gas under pressure: can burst if heated  
  _↳ feedback if chosen: That warning is for a different product._
- ◻️ flammable: catches fire easily  
  _↳ feedback if chosen: That warning is for a different product._

Full working after a second miss:

> acid from a car battery: corrosive: burns skin and eats metal.  
> Answer: corrosive: burns skin and eats metal.  

Sources: hazards (Hazard pictograms (UN Globally Harmonized System), described in words; reading product labels)

### `p19-what` · Lesson 19 · multiple choice, level 2

Prompt: {x.t} What should you do?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| You find kerosene in an old drink bottle in the kitchen. | Tell an adult so it can go into a labelled container, away from food and children. | You find kerosene in an old drink bottle in the kitchen. → Tell an adult so it can go into a labelled container, away from food and children. |
| A product has the skull and crossbones symbol. | Do not touch or taste it, and keep it away from children. | A product has the skull and crossbones symbol. → Do not touch or taste it, and keep it away from children. |
| Your little brother wants to play with a cooking-gas bottle. | Keep children away from the gas bottle and tell an adult: it can burst or leak. | Your little brother wants to play with a cooking-gas bottle. → Keep children away from the gas bottle and tell an adult: it can burst or leak. |

Right answer: `{x.a}`; wrong choices: `Tell an adult so it can go into a labelled container, away from food and children.`, `Do not touch or taste it, and keep it away from children.`, `Keep children away from the gas bottle and tell an adult: it can burst or leak.`, `Taste a little to find out what it is.`, `Nothing: it is not dangerous.`

- Feedback `other`: “Not the safe choice. Read the situation again.”

Three generated variants:

> Your little brother wants to play with a cooking-gas bottle. What should you do?

- ◻️ Tell an adult so it can go into a labelled container, away from food and children.  
  _↳ feedback if chosen: Not the safe choice. Read the situation again._
- ✅ Keep children away from the gas bottle and tell an adult: it can burst or leak.
- ◻️ Do not touch or taste it, and keep it away from children.  
  _↳ feedback if chosen: Not the safe choice. Read the situation again._
- ◻️ Taste a little to find out what it is.  
  _↳ feedback if chosen: Not the safe choice. Read the situation again._

Full working after a second miss:

> Your little brother wants to play with a cooking-gas bottle. → Keep children away from the gas bottle and tell an adult: it can burst or leak.  
> Answer: Keep children away from the gas bottle and tell an adult: it can burst or leak..  

> A product has the skull and crossbones symbol. What should you do?

- ◻️ Tell an adult so it can go into a labelled container, away from food and children.  
  _↳ feedback if chosen: Not the safe choice. Read the situation again._
- ✅ Do not touch or taste it, and keep it away from children.
- ◻️ Nothing: it is not dangerous.  
  _↳ feedback if chosen: Not the safe choice. Read the situation again._
- ◻️ Taste a little to find out what it is.  
  _↳ feedback if chosen: Not the safe choice. Read the situation again._

Full working after a second miss:

> A product has the skull and crossbones symbol. → Do not touch or taste it, and keep it away from children.  
> Answer: Do not touch or taste it, and keep it away from children..  

> Your little brother wants to play with a cooking-gas bottle. What should you do?

- ◻️ Do not touch or taste it, and keep it away from children.  
  _↳ feedback if chosen: Not the safe choice. Read the situation again._
- ✅ Keep children away from the gas bottle and tell an adult: it can burst or leak.
- ◻️ Taste a little to find out what it is.  
  _↳ feedback if chosen: Not the safe choice. Read the situation again._
- ◻️ Nothing: it is not dangerous.  
  _↳ feedback if chosen: Not the safe choice. Read the situation again._

Full working after a second miss:

> Your little brother wants to play with a cooking-gas bottle. → Keep children away from the gas bottle and tell an adult: it can burst or leak.  
> Answer: Keep children away from the gas bottle and tell an adult: it can burst or leak..  

Sources: hazards (Hazard pictograms (UN Globally Harmonized System), described in words; reading product labels)

### `p19-spot` · Lesson 19 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The flame symbol means the product catches fire easily.
- ✅ Rat poison is toxic.
- ✅ Read the label before using a product.
- ✅ Keep dangerous products away from children.
- ❌ It is fine to keep kerosene in a drink bottle.  
  _↳ Someone could drink it by mistake. Keep it in its own labelled container._
- ❌ A product is still good after its expiry date.  
  _↳ After the expiry date, do not use it._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Keep dangerous products away from children.
- ✅ A product is still good after its expiry date.  
  _↳ explanation: After the expiry date, do not use it._
- ◻️ The flame symbol means the product catches fire easily.
- ◻️ Rat poison is toxic.

Full working after a second miss:

> The wrong statement is “A product is still good after its expiry date.”.  
> After the expiry date, do not use it.  

> One sentence is wrong. Which one?

- ◻️ Read the label before using a product.
- ✅ It is fine to keep kerosene in a drink bottle.  
  _↳ explanation: Someone could drink it by mistake. Keep it in its own labelled container._
- ◻️ The flame symbol means the product catches fire easily.
- ◻️ Rat poison is toxic.

Full working after a second miss:

> The wrong statement is “It is fine to keep kerosene in a drink bottle.”.  
> Someone could drink it by mistake. Keep it in its own labelled container.  

> One sentence is wrong. Which one?

- ✅ A product is still good after its expiry date.  
  _↳ explanation: After the expiry date, do not use it._
- ◻️ The flame symbol means the product catches fire easily.
- ◻️ Keep dangerous products away from children.
- ◻️ Rat poison is toxic.

Full working after a second miss:

> The wrong statement is “A product is still good after its expiry date.”.  
> After the expiry date, do not use it.  

Sources: hazards (Hazard pictograms (UN Globally Harmonized System), described in words; reading product labels)

