# Chemistry Form 2, Batch C2-1: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f2-chemistry`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: tables and rules the computed answers use (src/engine/lib/science2.js, chemistry.js)

- **Electron shells (TR-J01)**: 2, 8, 8, 2 for atomic numbers 1–20 (sodium 2, 8, 1, calcium 2, 8, 8, 2); group = outer electrons (helium in group 8), period = number of shells.
- **Mass numbers (TR-J02, authored)**: H 1, He 4, Li 7, Be 9, B 11, C 12, N 14, O 16, F 19, Ne 20, Na 23, Mg 24, Al 27, Si 28, P 31, S 32, Cl 35, Ar 40, K 39, Ca 40.
- **Valencies (TR-J03, authored)**: H 1, Li 1, Na 1, K 1, Ag 1, NH4 1, Mg 2, Ca 2, Zn 2, Cu 2, Al 3, F 1, Cl 1, I 1, OH 1, NO3 1, HCO3 1, O 2, S 2, SO4 2, CO3 2, N 3, PO4 3. Formulae swap the valencies and simplify (Al + SO4 → Al2(SO4)3; Mg + O → MgO; Ca + OH → Ca(OH)2; NH4 + SO4 → (NH4)2SO4).

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `k2-1-true` | 1 | multiple choice, 1 | atomic-structure |
| 2 | `k2-1-ratio` | 1 | multiple choice, 1 | atomic-structure |
| 3 | `k2-1-changed` | 1 | multiple choice, 2 | atomic-structure |
| 4 | `k2-1-spot` | 1 | spot the error, 3 | atomic-structure |
| 5 | `k2-1-changed-card` (card c1-3) | 1 | multiple choice, 1 | atomic-structure |
| 6 | `k2-2-particle` | 2 | matching, 1 | atomic-structure |
| 7 | `k2-2-mass` | 2 | multiple choice, 1 | atomic-structure |
| 8 | `k2-2-charge` | 2 | multiple choice, 2 | atomic-structure |
| 9 | `k2-2-spot` | 2 | spot the error, 3 | atomic-structure |
| 10 | `k2-4-isotope` | 4 | multiple choice, 3 | atomic-structure |
| 11 | `k2-6-latin` | 6 | multiple choice, 1 | symbols-valency |
| 12 | `k2-6-spot` | 6 | spot the error, 3 | symbols-valency |
| 13 | `k2-7-match` | 7 | matching, 1 | symbols-valency |
| 14 | `k2-7-ate` | 7 | multiple choice, 2 | symbols-valency |
| 15 | `k2-7-spot` | 7 | spot the error, 3 | symbols-valency |
| 16 | `k2-7-ate-card` (card c7-3) | 7 | multiple choice, 1 | symbols-valency |
| 17 | `k2-8-noble` | 8 | multiple choice, 2 | symbols-valency |
| 18 | `k2-8-noble-card` (card c8-3) | 8 | multiple choice, 1 | symbols-valency |
| 19 | `k2-11-radical` | 11 | multiple choice, 1 | symbols-valency |
| 20 | `k2-11-common` | 11 | multiple choice, 2 | symbols-valency |
| 21 | `k2-11-common-card` (card c11-3) | 11 | multiple choice, 1 | symbols-valency |
| 22 | `k2-13-purpose` | 13 | multiple choice, 1 | periodic-table |
| 23 | `k2-13-who` | 13 | matching, 1 | periodic-table |
| 24 | `k2-13-order` | 13 | multiple choice, 2 | periodic-table |
| 25 | `k2-13-spot` | 13 | spot the error, 3 | periodic-table |
| 26 | `k2-13-order-card` (card c13-3) | 13 | multiple choice, 1 | periodic-table |
| 27 | `k2-15-family` | 15 | matching, 1 | periodic-table |
| 28 | `k2-15-hydrogen` | 15 | multiple choice, 2 | periodic-table |
| 29 | `k2-15-hydrogen-card` (card c15-3) | 15 | multiple choice, 1 | periodic-table |
| 30 | `k2-16-alkali` | 16 | multiple choice, 1 | periodic-table |
| 31 | `k2-16-halogen` | 16 | matching, 1 | periodic-table |
| 32 | `k2-16-noble` | 16 | multiple choice, 2 | periodic-table |
| 33 | `k2-16-spot` | 16 | spot the error, 3 | periodic-table |
| 34 | `k2-16-noble-card` (card c16-3) | 16 | multiple choice, 1 | periodic-table |
| 35 | `k2-17-alkali` | 17 | ordering, 1 | periodic-table |
| 36 | `k2-17-halogen` | 17 | ordering, 1 | periodic-table |
| 37 | `k2-17-displace` | 17 | multiple choice, 2 | periodic-table |
| 38 | `k2-17-spot` | 17 | spot the error, 3 | periodic-table |
| 39 | `k2-17-displace-card` (card c17-3) | 17 | multiple choice, 1 | periodic-table |

### `k2-1-true` · Lesson 1 · multiple choice, level 1

Prompt: Which statement is part of Dalton's atomic theory?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ All matter is made of tiny particles called atoms.
- ✅ Atoms combine in simple whole-number ratios to form compounds.
- ✅ In a chemical reaction, atoms are rearranged.
- ✅ Atoms of different elements are different.
- ❌ Atoms are made of protons, neutrons and electrons.  
  _↳ That was discovered later; Dalton thought atoms could not be divided._
- ❌ Matter is a continuous substance with no particles.  
  _↳ Dalton said matter is made of atoms._
- ❌ New atoms are created in every reaction.  
  _↳ Dalton said atoms are not created or destroyed._


Three generated variants:

> Which statement is part of Dalton's atomic theory?

- ✅ Atoms of different elements are different.
- ◻️ Matter is a continuous substance with no particles.  
  _↳ feedback if chosen: Dalton said matter is made of atoms._
- ◻️ Atoms are made of protons, neutrons and electrons.  
  _↳ feedback if chosen: That was discovered later; Dalton thought atoms could not be divided._

Full working after a second miss:

> The true statement is “Atoms of different elements are different.”.  
> “Matter is a continuous substance with no particles.” is false: Dalton said matter is made of atoms.  
> “Atoms are made of protons, neutrons and electrons.” is false: That was discovered later; Dalton thought atoms could not be divided.  

> Which statement is part of Dalton's atomic theory?

- ◻️ New atoms are created in every reaction.  
  _↳ feedback if chosen: Dalton said atoms are not created or destroyed._
- ✅ Atoms of different elements are different.
- ◻️ Atoms are made of protons, neutrons and electrons.  
  _↳ feedback if chosen: That was discovered later; Dalton thought atoms could not be divided._

Full working after a second miss:

> The true statement is “Atoms of different elements are different.”.  
> “New atoms are created in every reaction.” is false: Dalton said atoms are not created or destroyed.  
> “Atoms are made of protons, neutrons and electrons.” is false: That was discovered later; Dalton thought atoms could not be divided.  

> Which statement is part of Dalton's atomic theory?

- ◻️ New atoms are created in every reaction.  
  _↳ feedback if chosen: Dalton said atoms are not created or destroyed._
- ✅ Atoms combine in simple whole-number ratios to form compounds.
- ◻️ Matter is a continuous substance with no particles.  
  _↳ feedback if chosen: Dalton said matter is made of atoms._

Full working after a second miss:

> The true statement is “Atoms combine in simple whole-number ratios to form compounds.”.  
> “New atoms are created in every reaction.” is false: Dalton said atoms are not created or destroyed.  
> “Matter is a continuous substance with no particles.” is false: Dalton said matter is made of atoms.  

Sources: atomic-structure (Dalton's atomic theory (1803-1808); protons, neutrons and electrons; Bohr's model with shells of 2, 8, 8 for the first 20 elements; atomic number, mass number, isotopes)

### `k2-1-ratio` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Water has two hydrogen atoms for every oxygen atom. Which idea of Dalton does this show? | Atoms combine in simple whole-number ratios. | Atoms can be divided. · Atoms are destroyed in reactions. · All atoms are the same. | Dalton said they cannot be divided. · Dalton said they are not destroyed. · Atoms of different elements differ. | Two to one is a simple whole-number ratio. |
| Who proposed the atomic theory in the early 1800s? | John Dalton | Isaac Newton · Dmitri Mendeleev · Charles Darwin | Newton worked on forces and motion. · Mendeleev made the periodic table later. · Darwin studied evolution. | John Dalton, an English chemist. |
| According to Dalton, what happens to atoms in a chemical reaction? | They are rearranged. | They are destroyed. · New atoms are made. · They turn into energy. | Dalton said atoms are not destroyed. · Dalton said atoms are not created. · That is not Dalton's idea. | Atoms are only rearranged. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> According to Dalton, what happens to atoms in a chemical reaction?

- ◻️ New atoms are made.  
  _↳ feedback if chosen: Dalton said atoms are not created._
- ◻️ They turn into energy.  
  _↳ feedback if chosen: That is not Dalton's idea._
- ◻️ They are destroyed.  
  _↳ feedback if chosen: Dalton said atoms are not destroyed._
- ✅ They are rearranged.

Full working after a second miss:

> Atoms are only rearranged.  
> So the answer is “They are rearranged.”.  

> According to Dalton, what happens to atoms in a chemical reaction?

- ◻️ They turn into energy.  
  _↳ feedback if chosen: That is not Dalton's idea._
- ◻️ New atoms are made.  
  _↳ feedback if chosen: Dalton said atoms are not created._
- ✅ They are rearranged.
- ◻️ They are destroyed.  
  _↳ feedback if chosen: Dalton said atoms are not destroyed._

Full working after a second miss:

> Atoms are only rearranged.  
> So the answer is “They are rearranged.”.  

> Water has two hydrogen atoms for every oxygen atom. Which idea of Dalton does this show?

- ◻️ All atoms are the same.  
  _↳ feedback if chosen: Atoms of different elements differ._
- ✅ Atoms combine in simple whole-number ratios.
- ◻️ Atoms can be divided.  
  _↳ feedback if chosen: Dalton said they cannot be divided._
- ◻️ Atoms are destroyed in reactions.  
  _↳ feedback if chosen: Dalton said they are not destroyed._

Full working after a second miss:

> Two to one is a simple whole-number ratio.  
> So the answer is “Atoms combine in simple whole-number ratios.”.  

Sources: atomic-structure (Dalton's atomic theory (1803-1808); protons, neutrons and electrons; Bohr's model with shells of 2, 8, 8 for the first 20 elements; atomic number, mass number, isotopes)

### `k2-1-changed` · Lesson 1 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which of Dalton's ideas is no longer accepted? | Atoms cannot be divided. | Matter is made of atoms. · Atoms join in whole-number ratios. · Atoms are rearranged in reactions. | That is still accepted. · That is still accepted. · That is still accepted. | Atoms are made of smaller particles. |
| What are atoms of one element with different masses called? | isotopes | compounds · molecules · ions | Compounds contain different elements. · Molecules are atoms joined together. · Ions are charged particles. | Isotopes have the same number of protons but different numbers of neutrons. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which of Dalton's ideas is no longer accepted?

- ✅ Atoms cannot be divided.
- ◻️ Atoms join in whole-number ratios.  
  _↳ feedback if chosen: That is still accepted._
- ◻️ Atoms are rearranged in reactions.  
  _↳ feedback if chosen: That is still accepted._
- ◻️ Matter is made of atoms.  
  _↳ feedback if chosen: That is still accepted._

Full working after a second miss:

> Atoms are made of smaller particles.  
> So the answer is “Atoms cannot be divided.”.  

> What are atoms of one element with different masses called?

- ◻️ ions  
  _↳ feedback if chosen: Ions are charged particles._
- ◻️ compounds  
  _↳ feedback if chosen: Compounds contain different elements._
- ◻️ molecules  
  _↳ feedback if chosen: Molecules are atoms joined together._
- ✅ isotopes

Full working after a second miss:

> Isotopes have the same number of protons but different numbers of neutrons.  
> So the answer is “isotopes”.  

> What are atoms of one element with different masses called?

- ◻️ compounds  
  _↳ feedback if chosen: Compounds contain different elements._
- ◻️ ions  
  _↳ feedback if chosen: Ions are charged particles._
- ✅ isotopes
- ◻️ molecules  
  _↳ feedback if chosen: Molecules are atoms joined together._

Full working after a second miss:

> Isotopes have the same number of protons but different numbers of neutrons.  
> So the answer is “isotopes”.  

Sources: atomic-structure (Dalton's atomic theory (1803-1808); protons, neutrons and electrons; Bohr's model with shells of 2, 8, 8 for the first 20 elements; atomic number, mass number, isotopes)

### `k2-1-spot` · Lesson 1 · spot the error, level 3

Prompt: Which statement does NOT agree with Dalton's theory?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Matter is made of atoms.
- ✅ Atoms of one element are identical.
- ✅ Atoms combine in whole-number ratios.
- ✅ Atoms are not destroyed in reactions.
- ❌ Half an atom of oxygen joins with one atom of hydrogen.  
  _↳ Dalton said atoms join in whole-number ratios; atoms cannot be split._
- ❌ Atoms disappear when wood burns.  
  _↳ Dalton said atoms are rearranged, not destroyed._
- ❌ Atoms of copper and gold are identical.  
  _↳ Atoms of different elements are different._


Three generated variants:

> Which statement does NOT agree with Dalton's theory?

- ◻️ Atoms combine in whole-number ratios.
- ✅ Atoms of copper and gold are identical.  
  _↳ explanation: Atoms of different elements are different._
- ◻️ Atoms of one element are identical.
- ◻️ Atoms are not destroyed in reactions.

Full working after a second miss:

> The wrong statement is “Atoms of copper and gold are identical.”.  
> Atoms of different elements are different.  

> Which statement does NOT agree with Dalton's theory?

- ◻️ Atoms of one element are identical.
- ◻️ Atoms are not destroyed in reactions.
- ✅ Atoms of copper and gold are identical.  
  _↳ explanation: Atoms of different elements are different._
- ◻️ Atoms combine in whole-number ratios.

Full working after a second miss:

> The wrong statement is “Atoms of copper and gold are identical.”.  
> Atoms of different elements are different.  

> Which statement does NOT agree with Dalton's theory?

- ◻️ Matter is made of atoms.
- ◻️ Atoms of one element are identical.
- ◻️ Atoms combine in whole-number ratios.
- ✅ Half an atom of oxygen joins with one atom of hydrogen.  
  _↳ explanation: Dalton said atoms join in whole-number ratios; atoms cannot be split._

Full working after a second miss:

> The wrong statement is “Half an atom of oxygen joins with one atom of hydrogen.”.  
> Dalton said atoms join in whole-number ratios; atoms cannot be split.  

Sources: atomic-structure (Dalton's atomic theory (1803-1808); protons, neutrons and electrons; Bohr's model with shells of 2, 8, 8 for the first 20 elements; atomic number, mass number, isotopes)

### `k2-1-changed-card` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which of Dalton's ideas is no longer accepted? | Atoms cannot be divided. | Matter is made of atoms. · Atoms join in whole-number ratios. · Atoms are rearranged in reactions. | That is still accepted. · That is still accepted. · That is still accepted. | Atoms are made of smaller particles. |
| What are atoms of one element with different masses called? | isotopes | compounds · molecules · ions | Compounds contain different elements. · Molecules are atoms joined together. · Ions are charged particles. | Isotopes have the same number of protons but different numbers of neutrons. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which of Dalton's ideas is no longer accepted?

- ◻️ Atoms join in whole-number ratios.  
  _↳ feedback if chosen: That is still accepted._
- ◻️ Matter is made of atoms.  
  _↳ feedback if chosen: That is still accepted._
- ✅ Atoms cannot be divided.
- ◻️ Atoms are rearranged in reactions.  
  _↳ feedback if chosen: That is still accepted._

Full working after a second miss:

> Atoms are made of smaller particles.  
> So the answer is “Atoms cannot be divided.”.  

> What are atoms of one element with different masses called?

- ◻️ compounds  
  _↳ feedback if chosen: Compounds contain different elements._
- ◻️ molecules  
  _↳ feedback if chosen: Molecules are atoms joined together._
- ✅ isotopes
- ◻️ ions  
  _↳ feedback if chosen: Ions are charged particles._

Full working after a second miss:

> Isotopes have the same number of protons but different numbers of neutrons.  
> So the answer is “isotopes”.  

> Which of Dalton's ideas is no longer accepted?

- ✅ Atoms cannot be divided.
- ◻️ Matter is made of atoms.  
  _↳ feedback if chosen: That is still accepted._
- ◻️ Atoms join in whole-number ratios.  
  _↳ feedback if chosen: That is still accepted._
- ◻️ Atoms are rearranged in reactions.  
  _↳ feedback if chosen: That is still accepted._

Full working after a second miss:

> Atoms are made of smaller particles.  
> So the answer is “Atoms cannot be divided.”.  

Sources: atomic-structure (Dalton's atomic theory (1803-1808); protons, neutrons and electrons; Bohr's model with shells of 2, 8, 8 for the first 20 elements; atomic number, mass number, isotopes)

### `k2-2-particle` · Lesson 2 · matching, level 1

Prompt: Match each particle to its charge.

Pairs (3 shown each time):

- proton → **positive (+1)**
- neutron → **no charge (0)**
- electron → **negative (−1)**


Three generated variants:

> Match each particle to its charge.

Right-hand side (shuffled): positive (+1) · no charge (0) · negative (−1)
- electron → **negative (−1)**
- proton → **positive (+1)**
- neutron → **no charge (0)**

Full working after a second miss:

> The right pairs are:  
> electron → negative (−1)  
> proton → positive (+1)  
> neutron → no charge (0)  

> Match each particle to its charge.

Right-hand side (shuffled): no charge (0) · positive (+1) · negative (−1)
- proton → **positive (+1)**
- electron → **negative (−1)**
- neutron → **no charge (0)**

Full working after a second miss:

> The right pairs are:  
> proton → positive (+1)  
> electron → negative (−1)  
> neutron → no charge (0)  

> Match each particle to its charge.

Right-hand side (shuffled): positive (+1) · negative (−1) · no charge (0)
- proton → **positive (+1)**
- neutron → **no charge (0)**
- electron → **negative (−1)**

Full working after a second miss:

> The right pairs are:  
> proton → positive (+1)  
> neutron → no charge (0)  
> electron → negative (−1)  

Sources: atomic-structure (Dalton's atomic theory (1803-1808); protons, neutrons and electrons; Bohr's model with shells of 2, 8, 8 for the first 20 elements; atomic number, mass number, isotopes)

### `k2-2-mass` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Where is almost all the mass of an atom? | in the nucleus | in the electrons · spread evenly through the atom · in the empty space | Electrons are very light. · It is concentrated in the nucleus. · Empty space has no mass. | Protons and neutrons, in the nucleus, carry the mass. |
| Which particle has the smallest mass? | the electron | the proton · the neutron · the nucleus | A proton is about 1840 times heavier. · A neutron is about as heavy as a proton. · The nucleus contains protons and neutrons. | An electron is about 1840 times lighter than a proton. |
| Which particles are in the nucleus? | protons and neutrons | electrons only · protons and electrons · neutrons and electrons | Electrons are outside the nucleus. · Electrons are outside the nucleus. · Electrons are outside the nucleus. | The nucleus has protons and neutrons. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Where is almost all the mass of an atom?

- ◻️ in the electrons  
  _↳ feedback if chosen: Electrons are very light._
- ◻️ spread evenly through the atom  
  _↳ feedback if chosen: It is concentrated in the nucleus._
- ✅ in the nucleus
- ◻️ in the empty space  
  _↳ feedback if chosen: Empty space has no mass._

Full working after a second miss:

> Protons and neutrons, in the nucleus, carry the mass.  
> So the answer is “in the nucleus”.  

> Which particle has the smallest mass?

- ✅ the electron
- ◻️ the proton  
  _↳ feedback if chosen: A proton is about 1840 times heavier._
- ◻️ the nucleus  
  _↳ feedback if chosen: The nucleus contains protons and neutrons._
- ◻️ the neutron  
  _↳ feedback if chosen: A neutron is about as heavy as a proton._

Full working after a second miss:

> An electron is about 1840 times lighter than a proton.  
> So the answer is “the electron”.  

> Which particle has the smallest mass?

- ◻️ the proton  
  _↳ feedback if chosen: A proton is about 1840 times heavier._
- ◻️ the nucleus  
  _↳ feedback if chosen: The nucleus contains protons and neutrons._
- ◻️ the neutron  
  _↳ feedback if chosen: A neutron is about as heavy as a proton._
- ✅ the electron

Full working after a second miss:

> An electron is about 1840 times lighter than a proton.  
> So the answer is “the electron”.  

Sources: atomic-structure (Dalton's atomic theory (1803-1808); protons, neutrons and electrons; Bohr's model with shells of 2, 8, 8 for the first 20 elements; atomic number, mass number, isotopes)

### `k2-2-charge` · Lesson 2 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does an atom have no overall charge? | It has the same number of protons and electrons. | It has no protons. · Neutrons cancel the electrons. · Its electrons are positive. | Every atom has protons. · Neutrons have no charge. · Electrons are negative. | Equal + and − charges cancel. |
| What charge does the nucleus have? | positive | negative · none · it changes | Electrons are negative, but they are outside. · It contains positive protons. · It is always positive. | The nucleus has positive protons and neutral neutrons. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does an atom have no overall charge?

- ✅ It has the same number of protons and electrons.
- ◻️ It has no protons.  
  _↳ feedback if chosen: Every atom has protons._
- ◻️ Neutrons cancel the electrons.  
  _↳ feedback if chosen: Neutrons have no charge._
- ◻️ Its electrons are positive.  
  _↳ feedback if chosen: Electrons are negative._

Full working after a second miss:

> Equal + and − charges cancel.  
> So the answer is “It has the same number of protons and electrons.”.  

> What charge does the nucleus have?

- ◻️ none  
  _↳ feedback if chosen: It contains positive protons._
- ◻️ negative  
  _↳ feedback if chosen: Electrons are negative, but they are outside._
- ◻️ it changes  
  _↳ feedback if chosen: It is always positive._
- ✅ positive

Full working after a second miss:

> The nucleus has positive protons and neutral neutrons.  
> So the answer is “positive”.  

> What charge does the nucleus have?

- ◻️ none  
  _↳ feedback if chosen: It contains positive protons._
- ◻️ negative  
  _↳ feedback if chosen: Electrons are negative, but they are outside._
- ◻️ it changes  
  _↳ feedback if chosen: It is always positive._
- ✅ positive

Full working after a second miss:

> The nucleus has positive protons and neutral neutrons.  
> So the answer is “positive”.  

Sources: atomic-structure (Dalton's atomic theory (1803-1808); protons, neutrons and electrons; Bohr's model with shells of 2, 8, 8 for the first 20 elements; atomic number, mass number, isotopes)

### `k2-2-spot` · Lesson 2 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Protons are positive.
- ✅ Neutrons have no charge.
- ✅ Electrons move around the nucleus.
- ✅ An atom is neutral.
- ❌ Electrons are found in the nucleus.  
  _↳ Electrons move in shells around the nucleus._
- ❌ A neutron is negative.  
  _↳ A neutron has no charge._
- ❌ An electron is heavier than a proton.  
  _↳ An electron is about 1840 times lighter._


Three generated variants:

> Which statement is wrong?

- ◻️ Neutrons have no charge.
- ◻️ An atom is neutral.
- ◻️ Electrons move around the nucleus.
- ✅ An electron is heavier than a proton.  
  _↳ explanation: An electron is about 1840 times lighter._

Full working after a second miss:

> The wrong statement is “An electron is heavier than a proton.”.  
> An electron is about 1840 times lighter.  

> Which statement is wrong?

- ◻️ Neutrons have no charge.
- ◻️ An atom is neutral.
- ✅ An electron is heavier than a proton.  
  _↳ explanation: An electron is about 1840 times lighter._
- ◻️ Electrons move around the nucleus.

Full working after a second miss:

> The wrong statement is “An electron is heavier than a proton.”.  
> An electron is about 1840 times lighter.  

> Which statement is wrong?

- ◻️ Protons are positive.
- ✅ An electron is heavier than a proton.  
  _↳ explanation: An electron is about 1840 times lighter._
- ◻️ An atom is neutral.
- ◻️ Neutrons have no charge.

Full working after a second miss:

> The wrong statement is “An electron is heavier than a proton.”.  
> An electron is about 1840 times lighter.  

Sources: atomic-structure (Dalton's atomic theory (1803-1808); protons, neutrons and electrons; Bohr's model with shells of 2, 8, 8 for the first 20 elements; atomic number, mass number, isotopes)

### `k2-4-isotope` · Lesson 4 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Chlorine-35 and chlorine-37 are isotopes. What is different between their atoms? | the number of neutrons | the number of protons · the number of electrons · the element | Both are chlorine: same protons. · Both are neutral chlorine atoms: same electrons. · Both are chlorine. | Isotopes differ only in neutrons. |
| Which number tells you which element an atom is? | the atomic number | the mass number · the number of neutrons · the number of shells | Isotopes of one element have different mass numbers. · Neutrons can vary. · Many elements share the same number of shells. | The number of protons identifies the element. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Chlorine-35 and chlorine-37 are isotopes. What is different between their atoms?

- ◻️ the number of electrons  
  _↳ feedback if chosen: Both are neutral chlorine atoms: same electrons._
- ✅ the number of neutrons
- ◻️ the element  
  _↳ feedback if chosen: Both are chlorine._
- ◻️ the number of protons  
  _↳ feedback if chosen: Both are chlorine: same protons._

Full working after a second miss:

> Isotopes differ only in neutrons.  
> So the answer is “the number of neutrons”.  

> Chlorine-35 and chlorine-37 are isotopes. What is different between their atoms?

- ◻️ the number of protons  
  _↳ feedback if chosen: Both are chlorine: same protons._
- ◻️ the element  
  _↳ feedback if chosen: Both are chlorine._
- ✅ the number of neutrons
- ◻️ the number of electrons  
  _↳ feedback if chosen: Both are neutral chlorine atoms: same electrons._

Full working after a second miss:

> Isotopes differ only in neutrons.  
> So the answer is “the number of neutrons”.  

> Chlorine-35 and chlorine-37 are isotopes. What is different between their atoms?

- ◻️ the number of protons  
  _↳ feedback if chosen: Both are chlorine: same protons._
- ◻️ the element  
  _↳ feedback if chosen: Both are chlorine._
- ◻️ the number of electrons  
  _↳ feedback if chosen: Both are neutral chlorine atoms: same electrons._
- ✅ the number of neutrons

Full working after a second miss:

> Isotopes differ only in neutrons.  
> So the answer is “the number of neutrons”.  

Sources: atomic-structure (Dalton's atomic theory (1803-1808); protons, neutrons and electrons; Bohr's model with shells of 2, 8, 8 for the first 20 elements; atomic number, mass number, isotopes)

### `k2-6-latin` · Lesson 6 · multiple choice, level 1

Prompt: What is the symbol of {nameOf(s)}?

Table `X` (one row is picked each time):

| 0 | 1 |
|---|---|
| Na | So |
| Fe | Ir |
| Cu | Co |
| Ag | Si |
| Sn | Ti |
| Pb | Le |
| Au | Go |

Right answer: `{s}`; wrong choices: `{E}`, `{upper(s)}`

- Feedback `english`: “This symbol comes from the Latin name, {latinName(s)}, not the English name.”
- Feedback `caps`: “Only the first letter is a capital.”

Three generated variants:

> What is the symbol of lead?

- ✅ Pb
- ◻️ PB  
  _↳ feedback if chosen: Only the first letter is a capital._
- ◻️ Le  
  _↳ feedback if chosen: This symbol comes from the Latin name, plumbum, not the English name._

Full working after a second miss:

> lead comes from the Latin plumbum.  
> Its symbol is Pb.  

> What is the symbol of sodium?

- ◻️ NA  
  _↳ feedback if chosen: Only the first letter is a capital._
- ✅ Na
- ◻️ So  
  _↳ feedback if chosen: This symbol comes from the Latin name, natrium, not the English name._

Full working after a second miss:

> sodium comes from the Latin natrium.  
> Its symbol is Na.  

> What is the symbol of gold?

- ◻️ AU  
  _↳ feedback if chosen: Only the first letter is a capital._
- ✅ Au
- ◻️ Go  
  _↳ feedback if chosen: This symbol comes from the Latin name, aurum, not the English name._

Full working after a second miss:

> gold comes from the Latin aurum.  
> Its symbol is Au.  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-6-spot` · Lesson 6 · spot the error, level 3

Prompt: One symbol is written wrongly. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Ca for calcium
- ✅ Cl for chlorine
- ✅ Na for sodium
- ✅ Fe for iron
- ✅ Mg for magnesium
- ✅ K for potassium
- ❌ CA for calcium  
  _↳ Only the first letter is a capital: Ca._
- ❌ So for sodium  
  _↳ Sodium's symbol comes from Latin natrium: Na._
- ❌ Ir for iron  
  _↳ Iron's symbol comes from Latin ferrum: Fe._
- ❌ mg for magnesium  
  _↳ The first letter is a capital: Mg._


Three generated variants:

> One symbol is written wrongly. Which one?

- ◻️ K for potassium
- ◻️ Mg for magnesium
- ✅ CA for calcium  
  _↳ explanation: Only the first letter is a capital: Ca._
- ◻️ Na for sodium

Full working after a second miss:

> The wrong statement is “CA for calcium”.  
> Only the first letter is a capital: Ca.  

> One symbol is written wrongly. Which one?

- ◻️ Ca for calcium
- ✅ So for sodium  
  _↳ explanation: Sodium's symbol comes from Latin natrium: Na._
- ◻️ K for potassium
- ◻️ Mg for magnesium

Full working after a second miss:

> The wrong statement is “So for sodium”.  
> Sodium's symbol comes from Latin natrium: Na.  

> One symbol is written wrongly. Which one?

- ◻️ Ca for calcium
- ◻️ K for potassium
- ✅ So for sodium  
  _↳ explanation: Sodium's symbol comes from Latin natrium: Na._
- ◻️ Fe for iron

Full working after a second miss:

> The wrong statement is “So for sodium”.  
> Sodium's symbol comes from Latin natrium: Na.  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-7-match` · Lesson 7 · matching, level 1

Prompt: Match each radical to its formula.

Pairs (4 shown each time):

- hydroxide → **OH**
- nitrate → **NO₃**
- sulfate → **SO₄**
- carbonate → **CO₃**
- phosphate → **PO₄**
- ammonium → **NH₄**
- hydrogencarbonate → **HCO₃**


Three generated variants:

> Match each radical to its formula.

Right-hand side (shuffled): CO₃ · NO₃ · OH · SO₄
- carbonate → **CO₃**
- hydroxide → **OH**
- nitrate → **NO₃**
- sulfate → **SO₄**

Full working after a second miss:

> The right pairs are:  
> carbonate → CO₃  
> hydroxide → OH  
> nitrate → NO₃  
> sulfate → SO₄  

> Match each radical to its formula.

Right-hand side (shuffled): NH₄ · CO₃ · SO₄ · NO₃
- carbonate → **CO₃**
- sulfate → **SO₄**
- nitrate → **NO₃**
- ammonium → **NH₄**

Full working after a second miss:

> The right pairs are:  
> carbonate → CO₃  
> sulfate → SO₄  
> nitrate → NO₃  
> ammonium → NH₄  

> Match each radical to its formula.

Right-hand side (shuffled): SO₄ · NO₃ · CO₃ · NH₄
- ammonium → **NH₄**
- sulfate → **SO₄**
- nitrate → **NO₃**
- carbonate → **CO₃**

Full working after a second miss:

> The right pairs are:  
> ammonium → NH₄  
> sulfate → SO₄  
> nitrate → NO₃  
> carbonate → CO₃  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-7-ate` · Lesson 7 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which radical is positive? | ammonium, NH₄ | nitrate, NO₃ · sulfate, SO₄ · hydroxide, OH | Nitrate is negative. · Sulfate is negative. · Hydroxide is negative. | Ammonium is the common positive radical. |
| What do the radicals sulfate, nitrate and carbonate all contain? | oxygen | hydrogen · chlorine · sodium | They have no hydrogen. · They have no chlorine. · They have no sodium. | Names ending in -ate contain oxygen. |
| Which formula needs brackets? | Ca(OH)₂ | NaOH · KNO₃ · CaCO₃ | One hydroxide: no brackets. · One nitrate: no brackets. · One carbonate: no brackets. | Two hydroxide radicals: (OH)₂. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which formula needs brackets?

- ✅ Ca(OH)₂
- ◻️ CaCO₃  
  _↳ feedback if chosen: One carbonate: no brackets._
- ◻️ NaOH  
  _↳ feedback if chosen: One hydroxide: no brackets._
- ◻️ KNO₃  
  _↳ feedback if chosen: One nitrate: no brackets._

Full working after a second miss:

> Two hydroxide radicals: (OH)₂.  
> So the answer is “Ca(OH)₂”.  

> Which formula needs brackets?

- ◻️ NaOH  
  _↳ feedback if chosen: One hydroxide: no brackets._
- ◻️ CaCO₃  
  _↳ feedback if chosen: One carbonate: no brackets._
- ◻️ KNO₃  
  _↳ feedback if chosen: One nitrate: no brackets._
- ✅ Ca(OH)₂

Full working after a second miss:

> Two hydroxide radicals: (OH)₂.  
> So the answer is “Ca(OH)₂”.  

> Which formula needs brackets?

- ✅ Ca(OH)₂
- ◻️ KNO₃  
  _↳ feedback if chosen: One nitrate: no brackets._
- ◻️ CaCO₃  
  _↳ feedback if chosen: One carbonate: no brackets._
- ◻️ NaOH  
  _↳ feedback if chosen: One hydroxide: no brackets._

Full working after a second miss:

> Two hydroxide radicals: (OH)₂.  
> So the answer is “Ca(OH)₂”.  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-7-spot` · Lesson 7 · spot the error, level 3

Prompt: One radical is written with the wrong formula. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ hydroxide: OH
- ✅ nitrate: NO₃
- ✅ sulfate: SO₄
- ✅ carbonate: CO₃
- ✅ ammonium: NH₄
- ✅ phosphate: PO₄
- ❌ sulfate: SO₃  
  _↳ Sulfate is SO₄._
- ❌ nitrate: NO₄  
  _↳ Nitrate is NO₃._
- ❌ carbonate: CO₄  
  _↳ Carbonate is CO₃._
- ❌ ammonium: NH₃  
  _↳ NH₃ is ammonia; the ammonium radical is NH₄._


Three generated variants:

> One radical is written with the wrong formula. Which one?

- ✅ nitrate: NO₄  
  _↳ explanation: Nitrate is NO₃._
- ◻️ ammonium: NH₄
- ◻️ carbonate: CO₃
- ◻️ sulfate: SO₄

Full working after a second miss:

> The wrong statement is “nitrate: NO₄”.  
> Nitrate is NO₃.  

> One radical is written with the wrong formula. Which one?

- ◻️ carbonate: CO₃
- ◻️ sulfate: SO₄
- ◻️ ammonium: NH₄
- ✅ ammonium: NH₃  
  _↳ explanation: NH₃ is ammonia; the ammonium radical is NH₄._

Full working after a second miss:

> The wrong statement is “ammonium: NH₃”.  
> NH₃ is ammonia; the ammonium radical is NH₄.  

> One radical is written with the wrong formula. Which one?

- ◻️ sulfate: SO₄
- ◻️ nitrate: NO₃
- ✅ carbonate: CO₄  
  _↳ explanation: Carbonate is CO₃._
- ◻️ ammonium: NH₄

Full working after a second miss:

> The wrong statement is “carbonate: CO₄”.  
> Carbonate is CO₃.  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-7-ate-card` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which radical is positive? | ammonium, NH₄ | nitrate, NO₃ · sulfate, SO₄ · hydroxide, OH | Nitrate is negative. · Sulfate is negative. · Hydroxide is negative. | Ammonium is the common positive radical. |
| What do the radicals sulfate, nitrate and carbonate all contain? | oxygen | hydrogen · chlorine · sodium | They have no hydrogen. · They have no chlorine. · They have no sodium. | Names ending in -ate contain oxygen. |
| Which formula needs brackets? | Ca(OH)₂ | NaOH · KNO₃ · CaCO₃ | One hydroxide: no brackets. · One nitrate: no brackets. · One carbonate: no brackets. | Two hydroxide radicals: (OH)₂. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What do the radicals sulfate, nitrate and carbonate all contain?

- ✅ oxygen
- ◻️ hydrogen  
  _↳ feedback if chosen: They have no hydrogen._
- ◻️ sodium  
  _↳ feedback if chosen: They have no sodium._
- ◻️ chlorine  
  _↳ feedback if chosen: They have no chlorine._

Full working after a second miss:

> Names ending in -ate contain oxygen.  
> So the answer is “oxygen”.  

> What do the radicals sulfate, nitrate and carbonate all contain?

- ◻️ sodium  
  _↳ feedback if chosen: They have no sodium._
- ◻️ chlorine  
  _↳ feedback if chosen: They have no chlorine._
- ✅ oxygen
- ◻️ hydrogen  
  _↳ feedback if chosen: They have no hydrogen._

Full working after a second miss:

> Names ending in -ate contain oxygen.  
> So the answer is “oxygen”.  

> Which radical is positive?

- ◻️ sulfate, SO₄  
  _↳ feedback if chosen: Sulfate is negative._
- ◻️ nitrate, NO₃  
  _↳ feedback if chosen: Nitrate is negative._
- ✅ ammonium, NH₄
- ◻️ hydroxide, OH  
  _↳ feedback if chosen: Hydroxide is negative._

Full working after a second miss:

> Ammonium is the common positive radical.  
> So the answer is “ammonium, NH₄”.  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-8-noble` · Lesson 8 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do noble gases hardly form compounds? | Their outer shell is full. | They are metals. · They have no electrons. · They are liquids. | They are non-metals. · They have electrons. · They are gases. | A full outer shell makes them stable: valency zero. |
| Iron(III) oxide: what does the (III) tell you? | Iron has valency 3 in this compound. | There are three oxygen atoms only. · Iron is in group 3. · It is the third oxide ever made. | It is about iron's valency. · Iron is not in group 3. · It shows the valency. | The Roman number gives the metal's valency. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Iron(III) oxide: what does the (III) tell you?

- ◻️ Iron is in group 3.  
  _↳ feedback if chosen: Iron is not in group 3._
- ◻️ There are three oxygen atoms only.  
  _↳ feedback if chosen: It is about iron's valency._
- ◻️ It is the third oxide ever made.  
  _↳ feedback if chosen: It shows the valency._
- ✅ Iron has valency 3 in this compound.

Full working after a second miss:

> The Roman number gives the metal's valency.  
> So the answer is “Iron has valency 3 in this compound.”.  

> Iron(III) oxide: what does the (III) tell you?

- ✅ Iron has valency 3 in this compound.
- ◻️ Iron is in group 3.  
  _↳ feedback if chosen: Iron is not in group 3._
- ◻️ It is the third oxide ever made.  
  _↳ feedback if chosen: It shows the valency._
- ◻️ There are three oxygen atoms only.  
  _↳ feedback if chosen: It is about iron's valency._

Full working after a second miss:

> The Roman number gives the metal's valency.  
> So the answer is “Iron has valency 3 in this compound.”.  

> Why do noble gases hardly form compounds?

- ◻️ They are liquids.  
  _↳ feedback if chosen: They are gases._
- ✅ Their outer shell is full.
- ◻️ They are metals.  
  _↳ feedback if chosen: They are non-metals._
- ◻️ They have no electrons.  
  _↳ feedback if chosen: They have electrons._

Full working after a second miss:

> A full outer shell makes them stable: valency zero.  
> So the answer is “Their outer shell is full.”.  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-8-noble-card` · Lesson 8 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do noble gases hardly form compounds? | Their outer shell is full. | They are metals. · They have no electrons. · They are liquids. | They are non-metals. · They have electrons. · They are gases. | A full outer shell makes them stable: valency zero. |
| Iron(III) oxide: what does the (III) tell you? | Iron has valency 3 in this compound. | There are three oxygen atoms only. · Iron is in group 3. · It is the third oxide ever made. | It is about iron's valency. · Iron is not in group 3. · It shows the valency. | The Roman number gives the metal's valency. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why do noble gases hardly form compounds?

- ◻️ They are liquids.  
  _↳ feedback if chosen: They are gases._
- ◻️ They are metals.  
  _↳ feedback if chosen: They are non-metals._
- ✅ Their outer shell is full.
- ◻️ They have no electrons.  
  _↳ feedback if chosen: They have electrons._

Full working after a second miss:

> A full outer shell makes them stable: valency zero.  
> So the answer is “Their outer shell is full.”.  

> Iron(III) oxide: what does the (III) tell you?

- ✅ Iron has valency 3 in this compound.
- ◻️ It is the third oxide ever made.  
  _↳ feedback if chosen: It shows the valency._
- ◻️ There are three oxygen atoms only.  
  _↳ feedback if chosen: It is about iron's valency._
- ◻️ Iron is in group 3.  
  _↳ feedback if chosen: Iron is not in group 3._

Full working after a second miss:

> The Roman number gives the metal's valency.  
> So the answer is “Iron has valency 3 in this compound.”.  

> Iron(III) oxide: what does the (III) tell you?

- ✅ Iron has valency 3 in this compound.
- ◻️ There are three oxygen atoms only.  
  _↳ feedback if chosen: It is about iron's valency._
- ◻️ It is the third oxide ever made.  
  _↳ feedback if chosen: It shows the valency._
- ◻️ Iron is in group 3.  
  _↳ feedback if chosen: Iron is not in group 3._

Full working after a second miss:

> The Roman number gives the metal's valency.  
> So the answer is “Iron has valency 3 in this compound.”.  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-11-radical` · Lesson 11 · multiple choice, level 1

Prompt: What is the name of {formula(compoundFormula(p, n))}?

Table `X` (one row is picked each time):

| 0 | 1 | 2 |
|---|---|---|
| Na | CO3 | carbonide |
| Cu | SO4 | sulfide |
| K | NO3 | nitride |
| Na | OH | oxide |
| Ca | CO3 | carbide |
| NH4 | Cl | chlorate |
| Mg | SO4 | sulfite |
| NH4 | NO3 | nitrite |

Right answer: `{compoundName(p, n)}`; wrong choices: `{partName(p)} {W}`, `{partName(n)} {partName(p)}`

- Feedback `wrong`: “Use the name of the radical: {partName(n)}.”
- Feedback `order`: “The positive part's name comes first.”

Three generated variants:

> What is the name of NH₄NO₃?

- ◻️ nitrate ammonium  
  _↳ feedback if chosen: The positive part's name comes first._
- ✅ ammonium nitrate
- ◻️ ammonium nitrite  
  _↳ feedback if chosen: Use the name of the radical: nitrate._

Full working after a second miss:

> The positive part first: ammonium.  
> Then the radical: nitrate. So: ammonium nitrate.  

> What is the name of KNO₃?

- ◻️ potassium nitride  
  _↳ feedback if chosen: Use the name of the radical: nitrate._
- ◻️ nitrate potassium  
  _↳ feedback if chosen: The positive part's name comes first._
- ✅ potassium nitrate

Full working after a second miss:

> The positive part first: potassium.  
> Then the radical: nitrate. So: potassium nitrate.  

> What is the name of NH₄Cl?

- ◻️ chloride ammonium  
  _↳ feedback if chosen: The positive part's name comes first._
- ✅ ammonium chloride
- ◻️ ammonium chlorate  
  _↳ feedback if chosen: Use the name of the radical: chloride._

Full working after a second miss:

> The positive part first: ammonium.  
> Then the radical: chloride. So: ammonium chloride.  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-11-common` · Lesson 11 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the common name of H₂O? | water | hydrogen oxide only · ammonia · methane | We call it water. · Ammonia is NH₃. · Methane is CH₄. | H₂O is water. |
| What is the formula of ammonia? | NH₃ | NH₄ · N₂ · H₂O | NH₄ is the ammonium radical. · N₂ is nitrogen gas. · H₂O is water. | Ammonia is NH₃. |
| Which name contains oxygen? | calcium carbonate | calcium chloride · sodium sulfide · magnesium nitride | Chloride: no oxygen. · Sulfide: no oxygen. · Nitride: no oxygen. | -ate radicals contain oxygen. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which name contains oxygen?

- ◻️ magnesium nitride  
  _↳ feedback if chosen: Nitride: no oxygen._
- ◻️ sodium sulfide  
  _↳ feedback if chosen: Sulfide: no oxygen._
- ✅ calcium carbonate
- ◻️ calcium chloride  
  _↳ feedback if chosen: Chloride: no oxygen._

Full working after a second miss:

> -ate radicals contain oxygen.  
> So the answer is “calcium carbonate”.  

> Which name contains oxygen?

- ✅ calcium carbonate
- ◻️ sodium sulfide  
  _↳ feedback if chosen: Sulfide: no oxygen._
- ◻️ magnesium nitride  
  _↳ feedback if chosen: Nitride: no oxygen._
- ◻️ calcium chloride  
  _↳ feedback if chosen: Chloride: no oxygen._

Full working after a second miss:

> -ate radicals contain oxygen.  
> So the answer is “calcium carbonate”.  

> Which name contains oxygen?

- ◻️ calcium chloride  
  _↳ feedback if chosen: Chloride: no oxygen._
- ✅ calcium carbonate
- ◻️ sodium sulfide  
  _↳ feedback if chosen: Sulfide: no oxygen._
- ◻️ magnesium nitride  
  _↳ feedback if chosen: Nitride: no oxygen._

Full working after a second miss:

> -ate radicals contain oxygen.  
> So the answer is “calcium carbonate”.  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-11-common-card` · Lesson 11 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the common name of H₂O? | water | hydrogen oxide only · ammonia · methane | We call it water. · Ammonia is NH₃. · Methane is CH₄. | H₂O is water. |
| What is the formula of ammonia? | NH₃ | NH₄ · N₂ · H₂O | NH₄ is the ammonium radical. · N₂ is nitrogen gas. · H₂O is water. | Ammonia is NH₃. |
| Which name contains oxygen? | calcium carbonate | calcium chloride · sodium sulfide · magnesium nitride | Chloride: no oxygen. · Sulfide: no oxygen. · Nitride: no oxygen. | -ate radicals contain oxygen. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which name contains oxygen?

- ◻️ magnesium nitride  
  _↳ feedback if chosen: Nitride: no oxygen._
- ✅ calcium carbonate
- ◻️ sodium sulfide  
  _↳ feedback if chosen: Sulfide: no oxygen._
- ◻️ calcium chloride  
  _↳ feedback if chosen: Chloride: no oxygen._

Full working after a second miss:

> -ate radicals contain oxygen.  
> So the answer is “calcium carbonate”.  

> What is the formula of ammonia?

- ✅ NH₃
- ◻️ N₂  
  _↳ feedback if chosen: N₂ is nitrogen gas._
- ◻️ H₂O  
  _↳ feedback if chosen: H₂O is water._
- ◻️ NH₄  
  _↳ feedback if chosen: NH₄ is the ammonium radical._

Full working after a second miss:

> Ammonia is NH₃.  
> So the answer is “NH₃”.  

> What is the common name of H₂O?

- ◻️ methane  
  _↳ feedback if chosen: Methane is CH₄._
- ◻️ hydrogen oxide only  
  _↳ feedback if chosen: We call it water._
- ✅ water
- ◻️ ammonia  
  _↳ feedback if chosen: Ammonia is NH₃._

Full working after a second miss:

> H₂O is water.  
> So the answer is “water”.  

Sources: symbols-valency (Chemical symbols (IUPAC), valencies of common elements and radicals, writing formulae by swapping valencies, naming binary compounds (-ide) and compounds with radicals)

### `k2-13-purpose` · Lesson 13 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the main purpose of the periodic table? | to classify the elements and predict their properties | to list elements by colour · to show the price of elements · to name compounds | Colour is not the basis. · It has nothing to do with price. · That is not its main purpose. | It groups similar elements and allows predictions. |
| In the periodic table, where are elements with similar properties? | in the same column (group) | in random places · always next to hydrogen · in the same row only | They are placed by a rule. · That is not the rule. · Similar properties are in columns. | Similar elements share a group. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In the periodic table, where are elements with similar properties?

- ◻️ always next to hydrogen  
  _↳ feedback if chosen: That is not the rule._
- ◻️ in the same row only  
  _↳ feedback if chosen: Similar properties are in columns._
- ◻️ in random places  
  _↳ feedback if chosen: They are placed by a rule._
- ✅ in the same column (group)

Full working after a second miss:

> Similar elements share a group.  
> So the answer is “in the same column (group)”.  

> What is the main purpose of the periodic table?

- ✅ to classify the elements and predict their properties
- ◻️ to show the price of elements  
  _↳ feedback if chosen: It has nothing to do with price._
- ◻️ to list elements by colour  
  _↳ feedback if chosen: Colour is not the basis._
- ◻️ to name compounds  
  _↳ feedback if chosen: That is not its main purpose._

Full working after a second miss:

> It groups similar elements and allows predictions.  
> So the answer is “to classify the elements and predict their properties”.  

> In the periodic table, where are elements with similar properties?

- ◻️ always next to hydrogen  
  _↳ feedback if chosen: That is not the rule._
- ◻️ in the same row only  
  _↳ feedback if chosen: Similar properties are in columns._
- ◻️ in random places  
  _↳ feedback if chosen: They are placed by a rule._
- ✅ in the same column (group)

Full working after a second miss:

> Similar elements share a group.  
> So the answer is “in the same column (group)”.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-13-who` · Lesson 13 · matching, level 1

Prompt: Match each scientist to the work.

Pairs (3 shown each time):

- Döbereiner → **triads: groups of three similar elements**
- Newlands → **the law of octaves**
- Mendeleev → **a table by atomic mass with gaps for unknown elements**
- Moseley → **order by atomic number**


Three generated variants:

> Match each scientist to the work.

Right-hand side (shuffled): the law of octaves · a table by atomic mass with gaps for unknown elements · order by atomic number
- Moseley → **order by atomic number**
- Mendeleev → **a table by atomic mass with gaps for unknown elements**
- Newlands → **the law of octaves**

Full working after a second miss:

> The right pairs are:  
> Moseley → order by atomic number  
> Mendeleev → a table by atomic mass with gaps for unknown elements  
> Newlands → the law of octaves  

> Match each scientist to the work.

Right-hand side (shuffled): order by atomic number · triads: groups of three similar elements · a table by atomic mass with gaps for unknown elements
- Mendeleev → **a table by atomic mass with gaps for unknown elements**
- Moseley → **order by atomic number**
- Döbereiner → **triads: groups of three similar elements**

Full working after a second miss:

> The right pairs are:  
> Mendeleev → a table by atomic mass with gaps for unknown elements  
> Moseley → order by atomic number  
> Döbereiner → triads: groups of three similar elements  

> Match each scientist to the work.

Right-hand side (shuffled): triads: groups of three similar elements · a table by atomic mass with gaps for unknown elements · order by atomic number
- Moseley → **order by atomic number**
- Döbereiner → **triads: groups of three similar elements**
- Mendeleev → **a table by atomic mass with gaps for unknown elements**

Full working after a second miss:

> The right pairs are:  
> Moseley → order by atomic number  
> Döbereiner → triads: groups of three similar elements  
> Mendeleev → a table by atomic mass with gaps for unknown elements  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-13-order` · Lesson 13 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How are the elements arranged in the modern periodic table? | in order of atomic number | in order of atomic mass · in alphabetical order · in order of discovery | That was Mendeleev's order. · Names do not decide the order. · Dates do not decide the order. | Today's order is by atomic number. |
| Why did Mendeleev leave gaps in his table? | for elements not yet discovered | because he made mistakes · to make it look nicer · for compounds | The gaps were deliberate. · They had a scientific reason. · The table is for elements. | He predicted elements that were found later. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why did Mendeleev leave gaps in his table?

- ✅ for elements not yet discovered
- ◻️ to make it look nicer  
  _↳ feedback if chosen: They had a scientific reason._
- ◻️ because he made mistakes  
  _↳ feedback if chosen: The gaps were deliberate._
- ◻️ for compounds  
  _↳ feedback if chosen: The table is for elements._

Full working after a second miss:

> He predicted elements that were found later.  
> So the answer is “for elements not yet discovered”.  

> How are the elements arranged in the modern periodic table?

- ◻️ in alphabetical order  
  _↳ feedback if chosen: Names do not decide the order._
- ◻️ in order of atomic mass  
  _↳ feedback if chosen: That was Mendeleev's order._
- ◻️ in order of discovery  
  _↳ feedback if chosen: Dates do not decide the order._
- ✅ in order of atomic number

Full working after a second miss:

> Today's order is by atomic number.  
> So the answer is “in order of atomic number”.  

> Why did Mendeleev leave gaps in his table?

- ✅ for elements not yet discovered
- ◻️ because he made mistakes  
  _↳ feedback if chosen: The gaps were deliberate._
- ◻️ for compounds  
  _↳ feedback if chosen: The table is for elements._
- ◻️ to make it look nicer  
  _↳ feedback if chosen: They had a scientific reason._

Full working after a second miss:

> He predicted elements that were found later.  
> So the answer is “for elements not yet discovered”.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-13-spot` · Lesson 13 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Mendeleev left gaps for undiscovered elements.
- ✅ The modern table is in order of atomic number.
- ✅ Similar elements are in the same group.
- ✅ Mendeleev predicted properties of unknown elements.
- ❌ Mendeleev arranged elements in alphabetical order.  
  _↳ He arranged them by atomic mass and properties._
- ❌ The modern table is in order of atomic mass.  
  _↳ The modern table uses atomic number._
- ❌ The periodic table was made to show the prices of metals.  
  _↳ It classifies elements and predicts properties._


Three generated variants:

> Which statement is wrong?

- ◻️ Similar elements are in the same group.
- ✅ The modern table is in order of atomic mass.  
  _↳ explanation: The modern table uses atomic number._
- ◻️ Mendeleev predicted properties of unknown elements.
- ◻️ Mendeleev left gaps for undiscovered elements.

Full working after a second miss:

> The wrong statement is “The modern table is in order of atomic mass.”.  
> The modern table uses atomic number.  

> Which statement is wrong?

- ✅ The periodic table was made to show the prices of metals.  
  _↳ explanation: It classifies elements and predicts properties._
- ◻️ Similar elements are in the same group.
- ◻️ Mendeleev predicted properties of unknown elements.
- ◻️ The modern table is in order of atomic number.

Full working after a second miss:

> The wrong statement is “The periodic table was made to show the prices of metals.”.  
> It classifies elements and predicts properties.  

> Which statement is wrong?

- ✅ The modern table is in order of atomic mass.  
  _↳ explanation: The modern table uses atomic number._
- ◻️ The modern table is in order of atomic number.
- ◻️ Mendeleev left gaps for undiscovered elements.
- ◻️ Similar elements are in the same group.

Full working after a second miss:

> The wrong statement is “The modern table is in order of atomic mass.”.  
> The modern table uses atomic number.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-13-order-card` · Lesson 13 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How are the elements arranged in the modern periodic table? | in order of atomic number | in order of atomic mass · in alphabetical order · in order of discovery | That was Mendeleev's order. · Names do not decide the order. · Dates do not decide the order. | Today's order is by atomic number. |
| Why did Mendeleev leave gaps in his table? | for elements not yet discovered | because he made mistakes · to make it look nicer · for compounds | The gaps were deliberate. · They had a scientific reason. · The table is for elements. | He predicted elements that were found later. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How are the elements arranged in the modern periodic table?

- ◻️ in order of atomic mass  
  _↳ feedback if chosen: That was Mendeleev's order._
- ◻️ in order of discovery  
  _↳ feedback if chosen: Dates do not decide the order._
- ✅ in order of atomic number
- ◻️ in alphabetical order  
  _↳ feedback if chosen: Names do not decide the order._

Full working after a second miss:

> Today's order is by atomic number.  
> So the answer is “in order of atomic number”.  

> Why did Mendeleev leave gaps in his table?

- ◻️ to make it look nicer  
  _↳ feedback if chosen: They had a scientific reason._
- ◻️ because he made mistakes  
  _↳ feedback if chosen: The gaps were deliberate._
- ✅ for elements not yet discovered
- ◻️ for compounds  
  _↳ feedback if chosen: The table is for elements._

Full working after a second miss:

> He predicted elements that were found later.  
> So the answer is “for elements not yet discovered”.  

> Why did Mendeleev leave gaps in his table?

- ◻️ to make it look nicer  
  _↳ feedback if chosen: They had a scientific reason._
- ◻️ because he made mistakes  
  _↳ feedback if chosen: The gaps were deliberate._
- ◻️ for compounds  
  _↳ feedback if chosen: The table is for elements._
- ✅ for elements not yet discovered

Full working after a second miss:

> He predicted elements that were found later.  
> So the answer is “for elements not yet discovered”.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-15-family` · Lesson 15 · matching, level 1

Prompt: Sort the elements into their families.

Pairs (6 shown each time, sorted into groups):

- lithium → **alkali metals**
- sodium → **alkali metals**
- potassium → **alkali metals**
- magnesium → **alkaline earth metals**
- calcium → **alkaline earth metals**
- beryllium → **alkaline earth metals**
- fluorine → **halogens**
- chlorine → **halogens**
- iodine → **halogens**
- helium → **noble gases**
- neon → **noble gases**
- argon → **noble gases**


Three generated variants:

> Sort the elements into their families.

Groups: alkali metals · alkaline earth metals · halogens · noble gases
- potassium → **alkali metals**
- chlorine → **halogens**
- calcium → **alkaline earth metals**
- fluorine → **halogens**
- helium → **noble gases**
- lithium → **alkali metals**

Full working after a second miss:

> The right pairs are:  
> potassium → alkali metals  
> chlorine → halogens  
> calcium → alkaline earth metals  
> fluorine → halogens  
> helium → noble gases  
> lithium → alkali metals  

> Sort the elements into their families.

Groups: alkali metals · alkaline earth metals · halogens · noble gases
- fluorine → **halogens**
- calcium → **alkaline earth metals**
- chlorine → **halogens**
- sodium → **alkali metals**
- argon → **noble gases**
- iodine → **halogens**

Full working after a second miss:

> The right pairs are:  
> fluorine → halogens  
> calcium → alkaline earth metals  
> chlorine → halogens  
> sodium → alkali metals  
> argon → noble gases  
> iodine → halogens  

> Sort the elements into their families.

Groups: alkali metals · alkaline earth metals · halogens · noble gases
- argon → **noble gases**
- lithium → **alkali metals**
- sodium → **alkali metals**
- beryllium → **alkaline earth metals**
- fluorine → **halogens**
- helium → **noble gases**

Full working after a second miss:

> The right pairs are:  
> argon → noble gases  
> lithium → alkali metals  
> sodium → alkali metals  
> beryllium → alkaline earth metals  
> fluorine → halogens  
> helium → noble gases  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-15-hydrogen` · Lesson 15 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is hydrogen not an alkali metal although it is in group 1? | It is a non-metal gas. | It has two outer electrons. · It is a liquid. · It is a noble gas. | It has one electron. · It is a gas. · It reacts, unlike noble gases. | Hydrogen is a non-metal. |
| What do the members of one family have in common? | the same number of outer electrons | the same mass · the same number of shells · the same colour | Their masses differ. · That would be a period. · Colour is not the rule. | Same outer electrons, similar reactions. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What do the members of one family have in common?

- ◻️ the same number of shells  
  _↳ feedback if chosen: That would be a period._
- ◻️ the same mass  
  _↳ feedback if chosen: Their masses differ._
- ✅ the same number of outer electrons
- ◻️ the same colour  
  _↳ feedback if chosen: Colour is not the rule._

Full working after a second miss:

> Same outer electrons, similar reactions.  
> So the answer is “the same number of outer electrons”.  

> Why is hydrogen not an alkali metal although it is in group 1?

- ✅ It is a non-metal gas.
- ◻️ It has two outer electrons.  
  _↳ feedback if chosen: It has one electron._
- ◻️ It is a noble gas.  
  _↳ feedback if chosen: It reacts, unlike noble gases._
- ◻️ It is a liquid.  
  _↳ feedback if chosen: It is a gas._

Full working after a second miss:

> Hydrogen is a non-metal.  
> So the answer is “It is a non-metal gas.”.  

> What do the members of one family have in common?

- ✅ the same number of outer electrons
- ◻️ the same colour  
  _↳ feedback if chosen: Colour is not the rule._
- ◻️ the same number of shells  
  _↳ feedback if chosen: That would be a period._
- ◻️ the same mass  
  _↳ feedback if chosen: Their masses differ._

Full working after a second miss:

> Same outer electrons, similar reactions.  
> So the answer is “the same number of outer electrons”.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-15-hydrogen-card` · Lesson 15 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is hydrogen not an alkali metal although it is in group 1? | It is a non-metal gas. | It has two outer electrons. · It is a liquid. · It is a noble gas. | It has one electron. · It is a gas. · It reacts, unlike noble gases. | Hydrogen is a non-metal. |
| What do the members of one family have in common? | the same number of outer electrons | the same mass · the same number of shells · the same colour | Their masses differ. · That would be a period. · Colour is not the rule. | Same outer electrons, similar reactions. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What do the members of one family have in common?

- ✅ the same number of outer electrons
- ◻️ the same colour  
  _↳ feedback if chosen: Colour is not the rule._
- ◻️ the same number of shells  
  _↳ feedback if chosen: That would be a period._
- ◻️ the same mass  
  _↳ feedback if chosen: Their masses differ._

Full working after a second miss:

> Same outer electrons, similar reactions.  
> So the answer is “the same number of outer electrons”.  

> What do the members of one family have in common?

- ◻️ the same number of shells  
  _↳ feedback if chosen: That would be a period._
- ◻️ the same mass  
  _↳ feedback if chosen: Their masses differ._
- ✅ the same number of outer electrons
- ◻️ the same colour  
  _↳ feedback if chosen: Colour is not the rule._

Full working after a second miss:

> Same outer electrons, similar reactions.  
> So the answer is “the same number of outer electrons”.  

> Why is hydrogen not an alkali metal although it is in group 1?

- ◻️ It has two outer electrons.  
  _↳ feedback if chosen: It has one electron._
- ◻️ It is a liquid.  
  _↳ feedback if chosen: It is a gas._
- ✅ It is a non-metal gas.
- ◻️ It is a noble gas.  
  _↳ feedback if chosen: It reacts, unlike noble gases._

Full working after a second miss:

> Hydrogen is a non-metal.  
> So the answer is “It is a non-metal gas.”.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-16-alkali` · Lesson 16 · multiple choice, level 1

Prompt: Which statement about the alkali metals is true?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ They are soft enough to cut with a knife.
- ✅ They react with water to give hydrogen.
- ✅ They are kept under oil.
- ✅ They form alkaline solutions with water.
- ❌ They are hard and do not react with water.  
  _↳ Alkali metals are soft and react with water._
- ❌ They are kept in water.  
  _↳ They react with water, so they are kept under oil._
- ❌ They are coloured gases.  
  _↳ That describes the halogens._


Three generated variants:

> Which statement about the alkali metals is true?

- ◻️ They are coloured gases.  
  _↳ feedback if chosen: That describes the halogens._
- ✅ They are soft enough to cut with a knife.
- ◻️ They are kept in water.  
  _↳ feedback if chosen: They react with water, so they are kept under oil._

Full working after a second miss:

> The true statement is “They are soft enough to cut with a knife.”.  
> “They are coloured gases.” is false: That describes the halogens.  
> “They are kept in water.” is false: They react with water, so they are kept under oil.  

> Which statement about the alkali metals is true?

- ◻️ They are kept in water.  
  _↳ feedback if chosen: They react with water, so they are kept under oil._
- ◻️ They are coloured gases.  
  _↳ feedback if chosen: That describes the halogens._
- ✅ They are kept under oil.

Full working after a second miss:

> The true statement is “They are kept under oil.”.  
> “They are kept in water.” is false: They react with water, so they are kept under oil.  
> “They are coloured gases.” is false: That describes the halogens.  

> Which statement about the alkali metals is true?

- ◻️ They are hard and do not react with water.  
  _↳ feedback if chosen: Alkali metals are soft and react with water._
- ✅ They are kept under oil.
- ◻️ They are kept in water.  
  _↳ feedback if chosen: They react with water, so they are kept under oil._

Full working after a second miss:

> The true statement is “They are kept under oil.”.  
> “They are hard and do not react with water.” is false: Alkali metals are soft and react with water.  
> “They are kept in water.” is false: They react with water, so they are kept under oil.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-16-halogen` · Lesson 16 · matching, level 1

Prompt: Match each element to a property or use.

Pairs (4 shown each time):

- chlorine → **green-yellow gas that kills germs in water**
- iodine → **dark solid used as an antiseptic**
- helium → **light gas used to fill balloons**
- neon → **glows in advertising signs**
- argon → **fills light bulbs**
- sodium → **soft metal kept under oil**


Three generated variants:

> Match each element to a property or use.

Right-hand side (shuffled): glows in advertising signs · green-yellow gas that kills germs in water · fills light bulbs · light gas used to fill balloons
- helium → **light gas used to fill balloons**
- chlorine → **green-yellow gas that kills germs in water**
- argon → **fills light bulbs**
- neon → **glows in advertising signs**

Full working after a second miss:

> The right pairs are:  
> helium → light gas used to fill balloons  
> chlorine → green-yellow gas that kills germs in water  
> argon → fills light bulbs  
> neon → glows in advertising signs  

> Match each element to a property or use.

Right-hand side (shuffled): light gas used to fill balloons · glows in advertising signs · green-yellow gas that kills germs in water · soft metal kept under oil
- sodium → **soft metal kept under oil**
- helium → **light gas used to fill balloons**
- chlorine → **green-yellow gas that kills germs in water**
- neon → **glows in advertising signs**

Full working after a second miss:

> The right pairs are:  
> sodium → soft metal kept under oil  
> helium → light gas used to fill balloons  
> chlorine → green-yellow gas that kills germs in water  
> neon → glows in advertising signs  

> Match each element to a property or use.

Right-hand side (shuffled): glows in advertising signs · soft metal kept under oil · fills light bulbs · green-yellow gas that kills germs in water
- neon → **glows in advertising signs**
- chlorine → **green-yellow gas that kills germs in water**
- sodium → **soft metal kept under oil**
- argon → **fills light bulbs**

Full working after a second miss:

> The right pairs are:  
> neon → glows in advertising signs  
> chlorine → green-yellow gas that kills germs in water  
> sodium → soft metal kept under oil  
> argon → fills light bulbs  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-16-noble` · Lesson 16 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are noble gases used in light bulbs and signs? | They are very unreactive. | They burn easily. · They are coloured solids. · They react with metals. | They do not burn. · They are colourless gases. · They hardly react. | They do not react with the hot filament. |
| Why is chlorine added to drinking water? | It kills germs. | It adds colour. · It makes the water sweet. · It makes the water heavier. | Only a little is added, with no colour. · It does not sweeten. · That is not the reason. | Chlorine kills germs. |
| Which family reacts with water to give an alkaline solution and hydrogen? | the alkali metals | the noble gases · the halogens · the alkaline earth metals only | They do not react. · Halogens are non-metals. · Group 2 reacts more slowly; group 1 is the family named for it. | Group 1 metals are named for the alkalis they make. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which family reacts with water to give an alkaline solution and hydrogen?

- ◻️ the alkaline earth metals only  
  _↳ feedback if chosen: Group 2 reacts more slowly; group 1 is the family named for it._
- ✅ the alkali metals
- ◻️ the noble gases  
  _↳ feedback if chosen: They do not react._
- ◻️ the halogens  
  _↳ feedback if chosen: Halogens are non-metals._

Full working after a second miss:

> Group 1 metals are named for the alkalis they make.  
> So the answer is “the alkali metals”.  

> Why are noble gases used in light bulbs and signs?

- ◻️ They burn easily.  
  _↳ feedback if chosen: They do not burn._
- ◻️ They react with metals.  
  _↳ feedback if chosen: They hardly react._
- ✅ They are very unreactive.
- ◻️ They are coloured solids.  
  _↳ feedback if chosen: They are colourless gases._

Full working after a second miss:

> They do not react with the hot filament.  
> So the answer is “They are very unreactive.”.  

> Why is chlorine added to drinking water?

- ◻️ It makes the water heavier.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ It makes the water sweet.  
  _↳ feedback if chosen: It does not sweeten._
- ✅ It kills germs.
- ◻️ It adds colour.  
  _↳ feedback if chosen: Only a little is added, with no colour._

Full working after a second miss:

> Chlorine kills germs.  
> So the answer is “It kills germs.”.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-16-spot` · Lesson 16 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Chlorine is a halogen.
- ✅ Neon is used in advertising signs.
- ✅ Sodium is kept under oil.
- ✅ Halogen molecules have two atoms.
- ❌ Noble gases react violently with water.  
  _↳ Noble gases are very unreactive._
- ❌ Iodine is a green-yellow gas.  
  _↳ Chlorine is green-yellow; iodine is a dark solid._
- ❌ Alkali metals are too hard to cut.  
  _↳ They are soft enough to cut with a knife._


Three generated variants:

> Which statement is wrong?

- ◻️ Halogen molecules have two atoms.
- ✅ Alkali metals are too hard to cut.  
  _↳ explanation: They are soft enough to cut with a knife._
- ◻️ Neon is used in advertising signs.
- ◻️ Chlorine is a halogen.

Full working after a second miss:

> The wrong statement is “Alkali metals are too hard to cut.”.  
> They are soft enough to cut with a knife.  

> Which statement is wrong?

- ◻️ Chlorine is a halogen.
- ◻️ Neon is used in advertising signs.
- ✅ Noble gases react violently with water.  
  _↳ explanation: Noble gases are very unreactive._
- ◻️ Halogen molecules have two atoms.

Full working after a second miss:

> The wrong statement is “Noble gases react violently with water.”.  
> Noble gases are very unreactive.  

> Which statement is wrong?

- ◻️ Chlorine is a halogen.
- ◻️ Halogen molecules have two atoms.
- ✅ Noble gases react violently with water.  
  _↳ explanation: Noble gases are very unreactive._
- ◻️ Sodium is kept under oil.

Full working after a second miss:

> The wrong statement is “Noble gases react violently with water.”.  
> Noble gases are very unreactive.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-16-noble-card` · Lesson 16 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are noble gases used in light bulbs and signs? | They are very unreactive. | They burn easily. · They are coloured solids. · They react with metals. | They do not burn. · They are colourless gases. · They hardly react. | They do not react with the hot filament. |
| Why is chlorine added to drinking water? | It kills germs. | It adds colour. · It makes the water sweet. · It makes the water heavier. | Only a little is added, with no colour. · It does not sweeten. · That is not the reason. | Chlorine kills germs. |
| Which family reacts with water to give an alkaline solution and hydrogen? | the alkali metals | the noble gases · the halogens · the alkaline earth metals only | They do not react. · Halogens are non-metals. · Group 2 reacts more slowly; group 1 is the family named for it. | Group 1 metals are named for the alkalis they make. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which family reacts with water to give an alkaline solution and hydrogen?

- ◻️ the noble gases  
  _↳ feedback if chosen: They do not react._
- ◻️ the alkaline earth metals only  
  _↳ feedback if chosen: Group 2 reacts more slowly; group 1 is the family named for it._
- ◻️ the halogens  
  _↳ feedback if chosen: Halogens are non-metals._
- ✅ the alkali metals

Full working after a second miss:

> Group 1 metals are named for the alkalis they make.  
> So the answer is “the alkali metals”.  

> Why are noble gases used in light bulbs and signs?

- ◻️ They burn easily.  
  _↳ feedback if chosen: They do not burn._
- ◻️ They react with metals.  
  _↳ feedback if chosen: They hardly react._
- ◻️ They are coloured solids.  
  _↳ feedback if chosen: They are colourless gases._
- ✅ They are very unreactive.

Full working after a second miss:

> They do not react with the hot filament.  
> So the answer is “They are very unreactive.”.  

> Which family reacts with water to give an alkaline solution and hydrogen?

- ◻️ the noble gases  
  _↳ feedback if chosen: They do not react._
- ✅ the alkali metals
- ◻️ the alkaline earth metals only  
  _↳ feedback if chosen: Group 2 reacts more slowly; group 1 is the family named for it._
- ◻️ the halogens  
  _↳ feedback if chosen: Halogens are non-metals._

Full working after a second miss:

> Group 1 metals are named for the alkalis they make.  
> So the answer is “the alkali metals”.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-17-alkali` · Lesson 17 · ordering, level 1

Prompt: Put the alkali metals in order of reactivity, MOST reactive first.

Items in the right order:

1. potassium
2. sodium
3. lithium


Three generated variants:

> Put the alkali metals in order of reactivity, MOST reactive first.

Shown as: lithium · potassium · sodium
Correct order: potassium → sodium → lithium

Full working after a second miss:

> The correct order is: potassium → sodium → lithium.  

> Put the alkali metals in order of reactivity, MOST reactive first.

Shown as: potassium · lithium · sodium
Correct order: potassium → sodium → lithium

Full working after a second miss:

> The correct order is: potassium → sodium → lithium.  

> Put the alkali metals in order of reactivity, MOST reactive first.

Shown as: potassium · lithium · sodium
Correct order: potassium → sodium → lithium

Full working after a second miss:

> The correct order is: potassium → sodium → lithium.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-17-halogen` · Lesson 17 · ordering, level 1

Prompt: Put the halogens in order of reactivity, MOST reactive first.

Items in the right order:

1. fluorine
2. chlorine
3. bromine
4. iodine


Three generated variants:

> Put the halogens in order of reactivity, MOST reactive first.

Shown as: iodine · chlorine · bromine · fluorine
Correct order: fluorine → chlorine → bromine → iodine

Full working after a second miss:

> The correct order is: fluorine → chlorine → bromine → iodine.  

> Put the halogens in order of reactivity, MOST reactive first.

Shown as: bromine · iodine · fluorine · chlorine
Correct order: fluorine → chlorine → bromine → iodine

Full working after a second miss:

> The correct order is: fluorine → chlorine → bromine → iodine.  

> Put the halogens in order of reactivity, MOST reactive first.

Shown as: iodine · chlorine · fluorine · bromine
Correct order: fluorine → chlorine → bromine → iodine

Full working after a second miss:

> The correct order is: fluorine → chlorine → bromine → iodine.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-17-displace` · Lesson 17 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Chlorine is bubbled into potassium iodide solution. What happens? | Iodine is pushed out, because chlorine is more reactive. | Nothing, because iodine is more reactive. · Chlorine is pushed out. · Potassium becomes a gas. | Chlorine is more reactive than iodine. · Chlorine displaces iodine, not the reverse. · Potassium stays in the compound. | A more reactive halogen displaces a less reactive one. |
| Why is potassium more reactive than sodium? | Its outer electron is further from the nucleus, so it is lost more easily. | It has fewer shells. · It is a halogen. · It has a full outer shell. | It has more shells. · It is an alkali metal. · It has one outer electron. | Further from the nucleus, the electron is held less tightly. |
| Why do noble gases not react? | Their outer shell is full. | They are too heavy. · They are metals. · They have no electrons. | Mass is not the reason. · They are non-metals. · They have electrons. | A full outer shell is stable. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is potassium more reactive than sodium?

- ◻️ It is a halogen.  
  _↳ feedback if chosen: It is an alkali metal._
- ◻️ It has fewer shells.  
  _↳ feedback if chosen: It has more shells._
- ✅ Its outer electron is further from the nucleus, so it is lost more easily.
- ◻️ It has a full outer shell.  
  _↳ feedback if chosen: It has one outer electron._

Full working after a second miss:

> Further from the nucleus, the electron is held less tightly.  
> So the answer is “Its outer electron is further from the nucleus, so it is lost more easily.”.  

> Chlorine is bubbled into potassium iodide solution. What happens?

- ◻️ Chlorine is pushed out.  
  _↳ feedback if chosen: Chlorine displaces iodine, not the reverse._
- ◻️ Potassium becomes a gas.  
  _↳ feedback if chosen: Potassium stays in the compound._
- ◻️ Nothing, because iodine is more reactive.  
  _↳ feedback if chosen: Chlorine is more reactive than iodine._
- ✅ Iodine is pushed out, because chlorine is more reactive.

Full working after a second miss:

> A more reactive halogen displaces a less reactive one.  
> So the answer is “Iodine is pushed out, because chlorine is more reactive.”.  

> Why do noble gases not react?

- ◻️ They are too heavy.  
  _↳ feedback if chosen: Mass is not the reason._
- ✅ Their outer shell is full.
- ◻️ They are metals.  
  _↳ feedback if chosen: They are non-metals._
- ◻️ They have no electrons.  
  _↳ feedback if chosen: They have electrons._

Full working after a second miss:

> A full outer shell is stable.  
> So the answer is “Their outer shell is full.”.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-17-spot` · Lesson 17 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Potassium is more reactive than lithium.
- ✅ Fluorine is more reactive than iodine.
- ✅ Chlorine displaces iodine from potassium iodide.
- ✅ Noble gases are unreactive.
- ❌ Lithium is more reactive than potassium.  
  _↳ Alkali metals get more reactive down the group: potassium is more reactive._
- ❌ Iodine is the most reactive halogen.  
  _↳ Fluorine is the most reactive; iodine the least of the four._
- ❌ Iodine displaces chlorine from potassium chloride.  
  _↳ Iodine is less reactive, so it cannot displace chlorine._


Three generated variants:

> Which statement is wrong?

- ✅ Iodine displaces chlorine from potassium chloride.  
  _↳ explanation: Iodine is less reactive, so it cannot displace chlorine._
- ◻️ Chlorine displaces iodine from potassium iodide.
- ◻️ Potassium is more reactive than lithium.
- ◻️ Noble gases are unreactive.

Full working after a second miss:

> The wrong statement is “Iodine displaces chlorine from potassium chloride.”.  
> Iodine is less reactive, so it cannot displace chlorine.  

> Which statement is wrong?

- ✅ Lithium is more reactive than potassium.  
  _↳ explanation: Alkali metals get more reactive down the group: potassium is more reactive._
- ◻️ Chlorine displaces iodine from potassium iodide.
- ◻️ Fluorine is more reactive than iodine.
- ◻️ Noble gases are unreactive.

Full working after a second miss:

> The wrong statement is “Lithium is more reactive than potassium.”.  
> Alkali metals get more reactive down the group: potassium is more reactive.  

> Which statement is wrong?

- ✅ Lithium is more reactive than potassium.  
  _↳ explanation: Alkali metals get more reactive down the group: potassium is more reactive._
- ◻️ Potassium is more reactive than lithium.
- ◻️ Fluorine is more reactive than iodine.
- ◻️ Noble gases are unreactive.

Full working after a second miss:

> The wrong statement is “Lithium is more reactive than potassium.”.  
> Alkali metals get more reactive down the group: potassium is more reactive.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

### `k2-17-displace-card` · Lesson 17 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Chlorine is bubbled into potassium iodide solution. What happens? | Iodine is pushed out, because chlorine is more reactive. | Nothing, because iodine is more reactive. · Chlorine is pushed out. · Potassium becomes a gas. | Chlorine is more reactive than iodine. · Chlorine displaces iodine, not the reverse. · Potassium stays in the compound. | A more reactive halogen displaces a less reactive one. |
| Why is potassium more reactive than sodium? | Its outer electron is further from the nucleus, so it is lost more easily. | It has fewer shells. · It is a halogen. · It has a full outer shell. | It has more shells. · It is an alkali metal. · It has one outer electron. | Further from the nucleus, the electron is held less tightly. |
| Why do noble gases not react? | Their outer shell is full. | They are too heavy. · They are metals. · They have no electrons. | Mass is not the reason. · They are non-metals. · They have electrons. | A full outer shell is stable. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is potassium more reactive than sodium?

- ◻️ It has fewer shells.  
  _↳ feedback if chosen: It has more shells._
- ◻️ It has a full outer shell.  
  _↳ feedback if chosen: It has one outer electron._
- ◻️ It is a halogen.  
  _↳ feedback if chosen: It is an alkali metal._
- ✅ Its outer electron is further from the nucleus, so it is lost more easily.

Full working after a second miss:

> Further from the nucleus, the electron is held less tightly.  
> So the answer is “Its outer electron is further from the nucleus, so it is lost more easily.”.  

> Why do noble gases not react?

- ◻️ They are too heavy.  
  _↳ feedback if chosen: Mass is not the reason._
- ✅ Their outer shell is full.
- ◻️ They are metals.  
  _↳ feedback if chosen: They are non-metals._
- ◻️ They have no electrons.  
  _↳ feedback if chosen: They have electrons._

Full working after a second miss:

> A full outer shell is stable.  
> So the answer is “Their outer shell is full.”.  

> Why do noble gases not react?

- ◻️ They have no electrons.  
  _↳ feedback if chosen: They have electrons._
- ✅ Their outer shell is full.
- ◻️ They are metals.  
  _↳ feedback if chosen: They are non-metals._
- ◻️ They are too heavy.  
  _↳ feedback if chosen: Mass is not the reason._

Full working after a second miss:

> A full outer shell is stable.  
> So the answer is “Their outer shell is full.”.  

Sources: periodic-table (History of the periodic table (Döbereiner 1829, Newlands 1864, Mendeleev 1869, Moseley 1913); groups and periods; the families alkali metals, alkaline earth metals, halogens, noble gases; trends in reactivity)

