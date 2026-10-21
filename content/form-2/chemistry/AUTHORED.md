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
| 40 | `k2-20-kind` | 20 | multiple choice, 1 | reactions-equations |
| 41 | `k2-20-sign` | 20 | multiple choice, 1 | reactions-equations |
| 42 | `k2-20-terms` | 20 | multiple choice, 2 | reactions-equations |
| 43 | `k2-20-spot` | 20 | spot the error, 3 | reactions-equations |
| 44 | `k2-20-terms-card` (card c20-3) | 20 | multiple choice, 1 | reactions-equations |
| 45 | `k2-21-type` | 21 | multiple choice, 1 | reactions-equations |
| 46 | `k2-21-burn` | 21 | multiple choice, 1 | reactions-equations |
| 47 | `k2-21-disp` | 21 | multiple choice, 2 | reactions-equations |
| 48 | `k2-21-spot` | 21 | spot the error, 3 | reactions-equations |
| 49 | `k2-21-disp-card` (card c21-3) | 21 | multiple choice, 1 | reactions-equations |
| 50 | `k2-22-read` | 22 | multiple choice, 1 | reactions-equations |
| 51 | `k2-22-name` | 22 | multiple choice, 2 | reactions-equations |
| 52 | `k2-22-spot` | 22 | spot the error, 3 | reactions-equations |
| 53 | `k2-22-name-card` (card c22-3) | 22 | multiple choice, 1 | reactions-equations |
| 54 | `k2-23-gas` | 23 | multiple choice, 1 | reactions-equations |
| 55 | `k2-23-state` | 23 | multiple choice, 2 | reactions-equations |
| 56 | `k2-23-state-card` (card c23-3) | 23 | multiple choice, 1 | reactions-equations |
| 57 | `k2-24-rule` | 24 | multiple choice, 1 | reactions-equations |
| 58 | `k2-26-open` | 26 | multiple choice, 3 | reactions-equations |
| 59 | `k2-26-open-card` (card c26-3) | 26 | multiple choice, 1 | reactions-equations |
| 60 | `k2-27-law` | 27 | multiple choice, 1 | reactions-equations |
| 61 | `k2-27-exp` | 27 | multiple choice, 2 | reactions-equations |
| 62 | `k2-27-exp-card` (card c27-2) | 27 | multiple choice, 1 | reactions-equations |
| 63 | `k2-29-parts` | 29 | multiple choice, 1 | air |
| 64 | `k2-29-copper` | 29 | multiple choice, 1 | air |
| 65 | `k2-30-active` | 30 | multiple choice, 1 | air |
| 66 | `k2-30-inactive` | 30 | multiple choice, 1 | air |
| 67 | `k2-30-use` | 30 | multiple choice, 2 | air |
| 68 | `k2-30-spot` | 30 | spot the error, 3 | air |
| 69 | `k2-30-use-card` (card c30-3) | 30 | multiple choice, 1 | air |
| 70 | `k2-31-why` | 31 | multiple choice, 1 | air |
| 71 | `k2-31-compound` | 31 | multiple choice, 1 | air |
| 72 | `k2-31-props` | 31 | multiple choice, 2 | air |
| 73 | `k2-31-spot` | 31 | spot the error, 3 | air |
| 74 | `k2-31-props-card` (card c31-2) | 31 | multiple choice, 1 | air |
| 75 | `k2-32-steps` | 32 | multiple choice, 1 | air |
| 76 | `k2-32-cool` | 32 | multiple choice, 1 | air |
| 77 | `k2-33-triangle` | 33 | multiple choice, 1 | burning-rusting |
| 78 | `k2-33-products` | 33 | multiple choice, 1 | burning-rusting |
| 79 | `k2-33-air` | 33 | multiple choice, 2 | burning-rusting |
| 80 | `k2-33-spot` | 33 | spot the error, 3 | burning-rusting |
| 81 | `k2-33-air-card` (card c33-3) | 33 | multiple choice, 1 | burning-rusting |
| 82 | `k2-34-wood` | 34 | multiple choice, 1 | burning-rusting |
| 83 | `k2-34-charcoal` | 34 | multiple choice, 1 | burning-rusting |
| 84 | `k2-34-safe` | 34 | multiple choice, 2 | burning-rusting |
| 85 | `k2-34-spot` | 34 | spot the error, 3 | burning-rusting |
| 86 | `k2-34-safe-card` (card c34-3) | 34 | multiple choice, 1 | burning-rusting |
| 87 | `k2-35-flame` | 35 | multiple choice, 1 | burning-rusting |
| 88 | `k2-35-spot` | 35 | spot the error, 3 | burning-rusting |
| 89 | `k2-36-def` | 36 | multiple choice, 1 | burning-rusting |
| 90 | `k2-36-need` | 36 | multiple choice, 1 | burning-rusting |
| 91 | `k2-36-fast` | 36 | multiple choice, 2 | burning-rusting |
| 92 | `k2-36-spot` | 36 | spot the error, 3 | burning-rusting |
| 93 | `k2-36-fast-card` (card c36-3) | 36 | multiple choice, 1 | burning-rusting |
| 94 | `k2-37-comp` | 37 | multiple choice, 1 | burning-rusting |
| 95 | `k2-37-flaky` | 37 | multiple choice, 2 | burning-rusting |
| 96 | `k2-37-ox` | 37 | multiple choice, 1 | burning-rusting |
| 97 | `k2-37-spot` | 37 | spot the error, 3 | burning-rusting |
| 98 | `k2-37-flaky-card` (card c37-2) | 37 | multiple choice, 1 | burning-rusting |
| 99 | `k2-38-bad` | 38 | multiple choice, 1 | burning-rusting |
| 100 | `k2-38-way` | 38 | multiple choice, 1 | burning-rusting |
| 101 | `k2-38-zinc` | 38 | multiple choice, 2 | burning-rusting |
| 102 | `k2-38-spot` | 38 | spot the error, 3 | burning-rusting |
| 103 | `k2-38-zinc-card` (card c38-3) | 38 | multiple choice, 1 | burning-rusting |
| 104 | `k2-40-part` | 40 | multiple choice, 1 | separation-purity |
| 105 | `k2-40-change` | 40 | multiple choice, 1 | separation-purity |
| 106 | `k2-40-spot` | 40 | spot the error, 3 | separation-purity |
| 107 | `k2-41-filter` | 41 | multiple choice, 1 | separation-purity |
| 108 | `k2-41-evap` | 41 | multiple choice, 1 | separation-purity |
| 109 | `k2-41-method` | 41 | multiple choice, 2 | separation-purity |
| 110 | `k2-41-method-card` (card c41-3) | 41 | multiple choice, 1 | separation-purity |
| 111 | `k2-42-simple` | 42 | multiple choice, 1 | separation-purity |
| 112 | `k2-42-parts` | 42 | multiple choice, 1 | separation-purity |
| 113 | `k2-42-spot` | 42 | spot the error, 3 | separation-purity |
| 114 | `k2-43-use` | 43 | multiple choice, 1 | separation-purity |
| 115 | `k2-43-setup` | 43 | multiple choice, 1 | separation-purity |
| 116 | `k2-44-points` | 44 | multiple choice, 1 | separation-purity |
| 117 | `k2-44-sub` | 44 | multiple choice, 1 | separation-purity |
| 118 | `k2-44-sep` | 44 | multiple choice, 2 | separation-purity |
| 119 | `k2-44-sep-card` (card c44-3) | 44 | multiple choice, 1 | separation-purity |
| 120 | `k2-45-pure` | 45 | multiple choice, 1 | separation-purity |
| 121 | `k2-45-imp` | 45 | multiple choice, 2 | separation-purity |
| 122 | `k2-45-spot` | 45 | multiple choice, 3 | separation-purity |
| 123 | `k2-45-imp-card` (card c45-2) | 45 | multiple choice, 1 | separation-purity |
| 124 | `k2-45-spot-card` (card c45-3) | 45 | multiple choice, 1 | separation-purity |

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

### `k2-20-kind` · Lesson 20 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Is cooking an egg a physical or a chemical change? | a chemical change | a physical change · neither · both at once | The cooked egg is a new substance; it cannot become raw again. · The egg does change. · A new substance is made, so it is chemical. | The cooked egg cannot be turned back: a new substance was made. |
| Is melting ice a physical or a chemical change? | a physical change | a chemical change · neither · a reaction | Water is still water; no new substance. · The state changes. · No new substance is made, so it is not a reaction. | Ice and water are the same substance in different states. |
| Is rusting of iron a physical or a chemical change? | a chemical change | a physical change · neither · a change of state | Rust is a new brown substance. · The iron does change. · Rust is a new substance, not iron in another state. | Rust is a new substance. |
| Is dissolving salt in water a physical or a chemical change? | a physical change | a chemical change · neither · a reaction | The salt can be got back by evaporating the water. · The salt does dissolve. · No new substance is made. | Evaporation gives the salt back, so no new substance was made. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is rusting of iron a physical or a chemical change?

- ◻️ a physical change  
  _↳ feedback if chosen: Rust is a new brown substance._
- ✅ a chemical change
- ◻️ a change of state  
  _↳ feedback if chosen: Rust is a new substance, not iron in another state._
- ◻️ neither  
  _↳ feedback if chosen: The iron does change._

Full working after a second miss:

> Rust is a new substance.  
> So the answer is “a chemical change”.  

> Is cooking an egg a physical or a chemical change?

- ◻️ neither  
  _↳ feedback if chosen: The egg does change._
- ✅ a chemical change
- ◻️ both at once  
  _↳ feedback if chosen: A new substance is made, so it is chemical._
- ◻️ a physical change  
  _↳ feedback if chosen: The cooked egg is a new substance; it cannot become raw again._

Full working after a second miss:

> The cooked egg cannot be turned back: a new substance was made.  
> So the answer is “a chemical change”.  

> Is melting ice a physical or a chemical change?

- ◻️ neither  
  _↳ feedback if chosen: The state changes._
- ◻️ a reaction  
  _↳ feedback if chosen: No new substance is made, so it is not a reaction._
- ◻️ a chemical change  
  _↳ feedback if chosen: Water is still water; no new substance._
- ✅ a physical change

Full working after a second miss:

> Ice and water are the same substance in different states.  
> So the answer is “a physical change”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-20-sign` · Lesson 20 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which observation shows that a chemical change has taken place? | Bubbles of a new gas are given off. | The solid changes shape. · The water gets colder in the fridge. · The sugar disappears into the tea. | A change of shape makes no new substance. · Cooling is physical. · Dissolving is physical. | A new gas is a new substance. |
| Which of these is a sign of a chemical reaction? | A change of colour | A change of size · A change of position · A change of shape | Size alone shows no new substance. · Moving does not make a new substance. · Shape alone shows no new substance. | A new colour often means a new substance. |
| When two clear solutions are mixed, a yellow solid appears. What is this solid called? | a precipitate | a solvent · a crystal of ice · a reactant | The solvent is the liquid that dissolves things. · It is not frozen water. · It is a product, not a reactant. | A solid formed in a solution is a precipitate. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which of these is a sign of a chemical reaction?

- ✅ A change of colour
- ◻️ A change of size  
  _↳ feedback if chosen: Size alone shows no new substance._
- ◻️ A change of shape  
  _↳ feedback if chosen: Shape alone shows no new substance._
- ◻️ A change of position  
  _↳ feedback if chosen: Moving does not make a new substance._

Full working after a second miss:

> A new colour often means a new substance.  
> So the answer is “A change of colour”.  

> Which observation shows that a chemical change has taken place?

- ◻️ The solid changes shape.  
  _↳ feedback if chosen: A change of shape makes no new substance._
- ◻️ The water gets colder in the fridge.  
  _↳ feedback if chosen: Cooling is physical._
- ✅ Bubbles of a new gas are given off.
- ◻️ The sugar disappears into the tea.  
  _↳ feedback if chosen: Dissolving is physical._

Full working after a second miss:

> A new gas is a new substance.  
> So the answer is “Bubbles of a new gas are given off.”.  

> Which of these is a sign of a chemical reaction?

- ◻️ A change of position  
  _↳ feedback if chosen: Moving does not make a new substance._
- ✅ A change of colour
- ◻️ A change of shape  
  _↳ feedback if chosen: Shape alone shows no new substance._
- ◻️ A change of size  
  _↳ feedback if chosen: Size alone shows no new substance._

Full working after a second miss:

> A new colour often means a new substance.  
> So the answer is “A change of colour”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-20-terms` · Lesson 20 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Charcoal burns in oxygen to form carbon dioxide. What are the reactants? | charcoal (carbon) and oxygen | carbon dioxide only · carbon dioxide and oxygen · ash and smoke | Carbon dioxide is the product. · Carbon dioxide is made; it is not a starting substance. · Those are not named in this reaction. | Reactants are the starting substances. |
| Magnesium burns in oxygen to form magnesium oxide. What is the product? | magnesium oxide | magnesium · oxygen · magnesium and oxygen | Magnesium is a reactant. · Oxygen is a reactant. · Those are the reactants. | The product is the new substance formed. |
| Which statement about a chemical change is true? | New substances are formed. | It is always easy to reverse. · No energy change happens. · The substances only change state. | Most chemical changes are hard to reverse. · Heat or light is usually given out or taken in. · A change of state is physical. | A chemical change always makes new substances. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which statement about a chemical change is true?

- ◻️ The substances only change state.  
  _↳ feedback if chosen: A change of state is physical._
- ◻️ It is always easy to reverse.  
  _↳ feedback if chosen: Most chemical changes are hard to reverse._
- ◻️ No energy change happens.  
  _↳ feedback if chosen: Heat or light is usually given out or taken in._
- ✅ New substances are formed.

Full working after a second miss:

> A chemical change always makes new substances.  
> So the answer is “New substances are formed.”.  

> Magnesium burns in oxygen to form magnesium oxide. What is the product?

- ◻️ magnesium  
  _↳ feedback if chosen: Magnesium is a reactant._
- ✅ magnesium oxide
- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen is a reactant._
- ◻️ magnesium and oxygen  
  _↳ feedback if chosen: Those are the reactants._

Full working after a second miss:

> The product is the new substance formed.  
> So the answer is “magnesium oxide”.  

> Which statement about a chemical change is true?

- ◻️ No energy change happens.  
  _↳ feedback if chosen: Heat or light is usually given out or taken in._
- ◻️ The substances only change state.  
  _↳ feedback if chosen: A change of state is physical._
- ◻️ It is always easy to reverse.  
  _↳ feedback if chosen: Most chemical changes are hard to reverse._
- ✅ New substances are formed.

Full working after a second miss:

> A chemical change always makes new substances.  
> So the answer is “New substances are formed.”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-20-spot` · Lesson 20 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Burning wood is a chemical change.
- ✅ Boiling water is a physical change.
- ✅ Souring of milk is a chemical change.
- ✅ Breaking a glass is a physical change.
- ❌ Melting candle wax is a chemical change.  
  _↳ Melting makes no new substance: it is physical (only the burning of the wick and wax is chemical)._
- ❌ Rusting is a physical change because the iron is still there.  
  _↳ Rust is a new substance, so rusting is chemical._
- ❌ Dissolving sugar is a chemical change.  
  _↳ The sugar can be got back by evaporation: physical._


Three generated variants:

> Which statement is wrong?

- ◻️ Burning wood is a chemical change.
- ◻️ Boiling water is a physical change.
- ◻️ Souring of milk is a chemical change.
- ✅ Dissolving sugar is a chemical change.  
  _↳ explanation: The sugar can be got back by evaporation: physical._

Full working after a second miss:

> The wrong statement is “Dissolving sugar is a chemical change.”.  
> The sugar can be got back by evaporation: physical.  

> Which statement is wrong?

- ◻️ Breaking a glass is a physical change.
- ◻️ Boiling water is a physical change.
- ◻️ Souring of milk is a chemical change.
- ✅ Rusting is a physical change because the iron is still there.  
  _↳ explanation: Rust is a new substance, so rusting is chemical._

Full working after a second miss:

> The wrong statement is “Rusting is a physical change because the iron is still there.”.  
> Rust is a new substance, so rusting is chemical.  

> Which statement is wrong?

- ◻️ Burning wood is a chemical change.
- ◻️ Boiling water is a physical change.
- ◻️ Souring of milk is a chemical change.
- ✅ Melting candle wax is a chemical change.  
  _↳ explanation: Melting makes no new substance: it is physical (only the burning of the wick and wax is chemical)._

Full working after a second miss:

> The wrong statement is “Melting candle wax is a chemical change.”.  
> Melting makes no new substance: it is physical (only the burning of the wick and wax is chemical).  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-20-terms-card` · Lesson 20 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Charcoal burns in oxygen to form carbon dioxide. What are the reactants? | charcoal (carbon) and oxygen | carbon dioxide only · carbon dioxide and oxygen · ash and smoke | Carbon dioxide is the product. · Carbon dioxide is made; it is not a starting substance. · Those are not named in this reaction. | Reactants are the starting substances. |
| Magnesium burns in oxygen to form magnesium oxide. What is the product? | magnesium oxide | magnesium · oxygen · magnesium and oxygen | Magnesium is a reactant. · Oxygen is a reactant. · Those are the reactants. | The product is the new substance formed. |
| Which statement about a chemical change is true? | New substances are formed. | It is always easy to reverse. · No energy change happens. · The substances only change state. | Most chemical changes are hard to reverse. · Heat or light is usually given out or taken in. · A change of state is physical. | A chemical change always makes new substances. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Charcoal burns in oxygen to form carbon dioxide. What are the reactants?

- ◻️ ash and smoke  
  _↳ feedback if chosen: Those are not named in this reaction._
- ◻️ carbon dioxide and oxygen  
  _↳ feedback if chosen: Carbon dioxide is made; it is not a starting substance._
- ✅ charcoal (carbon) and oxygen
- ◻️ carbon dioxide only  
  _↳ feedback if chosen: Carbon dioxide is the product._

Full working after a second miss:

> Reactants are the starting substances.  
> So the answer is “charcoal (carbon) and oxygen”.  

> Charcoal burns in oxygen to form carbon dioxide. What are the reactants?

- ◻️ ash and smoke  
  _↳ feedback if chosen: Those are not named in this reaction._
- ◻️ carbon dioxide only  
  _↳ feedback if chosen: Carbon dioxide is the product._
- ◻️ carbon dioxide and oxygen  
  _↳ feedback if chosen: Carbon dioxide is made; it is not a starting substance._
- ✅ charcoal (carbon) and oxygen

Full working after a second miss:

> Reactants are the starting substances.  
> So the answer is “charcoal (carbon) and oxygen”.  

> Magnesium burns in oxygen to form magnesium oxide. What is the product?

- ◻️ magnesium and oxygen  
  _↳ feedback if chosen: Those are the reactants._
- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen is a reactant._
- ◻️ magnesium  
  _↳ feedback if chosen: Magnesium is a reactant._
- ✅ magnesium oxide

Full working after a second miss:

> The product is the new substance formed.  
> So the answer is “magnesium oxide”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-21-type` · Lesson 21 · multiple choice, level 1

Prompt: What type of reaction is this? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| iron + sulphur → iron sulphide | combination | decomposition · neutralisation · displacement | Nothing breaks down; two substances join. · No acid or base is used. · No element is pushed out. | Two substances join to make one. |
| calcium carbonate → calcium oxide + carbon dioxide | decomposition | combination · neutralisation · combustion | One substance gives two, the opposite of combination. · No acid or base. · No oxygen is used. | One substance breaks into two. |
| sodium hydroxide + hydrochloric acid → sodium chloride + water | neutralisation | decomposition · combination · combustion | Two substances react, not one breaking down. · Two products are made, not one. · Nothing burns in oxygen. | Acid + base → salt + water. |
| methane + oxygen → carbon dioxide + water | combustion | decomposition · neutralisation · displacement | Methane reacts with oxygen; it does not just break down. · No acid or base. · No metal is pushed out. | Burning in oxygen is combustion. |
| zinc + copper sulphate → zinc sulphate + copper | displacement | combination · decomposition · neutralisation | Two products are made, not one. · Two substances react. · No acid or base. | Zinc pushes copper out of its compound. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What type of reaction is this? iron + sulphur → iron sulphide

- ◻️ neutralisation  
  _↳ feedback if chosen: No acid or base is used._
- ◻️ displacement  
  _↳ feedback if chosen: No element is pushed out._
- ◻️ decomposition  
  _↳ feedback if chosen: Nothing breaks down; two substances join._
- ✅ combination

Full working after a second miss:

> Two substances join to make one.  
> So the answer is “combination”.  

> What type of reaction is this? iron + sulphur → iron sulphide

- ◻️ displacement  
  _↳ feedback if chosen: No element is pushed out._
- ◻️ decomposition  
  _↳ feedback if chosen: Nothing breaks down; two substances join._
- ◻️ neutralisation  
  _↳ feedback if chosen: No acid or base is used._
- ✅ combination

Full working after a second miss:

> Two substances join to make one.  
> So the answer is “combination”.  

> What type of reaction is this? zinc + copper sulphate → zinc sulphate + copper

- ◻️ decomposition  
  _↳ feedback if chosen: Two substances react._
- ◻️ combination  
  _↳ feedback if chosen: Two products are made, not one._
- ✅ displacement
- ◻️ neutralisation  
  _↳ feedback if chosen: No acid or base._

Full working after a second miss:

> Zinc pushes copper out of its compound.  
> So the answer is “displacement”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-21-burn` · Lesson 21 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is given out when a substance burns? | heat and light | oxygen · only water · nothing | Oxygen is used up when things burn. · Water may form, but heat and light are always given out. · Burning gives out heat and light. | Combustion gives out heat and light. |
| What does an acid react with in neutralisation? | a base (alkali) | another acid · oxygen · a noble gas | Two acids do not neutralise each other. · That is combustion. · Noble gases do not react. | Acid + base → salt + water. |
| Which everyday process is a chemical reaction? | digesting food | drying clothes · melting shea butter · grinding pepper | Drying is evaporation: physical. · Melting is physical. · Grinding only makes small pieces. | Digestion breaks food into new substances. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which everyday process is a chemical reaction?

- ✅ digesting food
- ◻️ drying clothes  
  _↳ feedback if chosen: Drying is evaporation: physical._
- ◻️ melting shea butter  
  _↳ feedback if chosen: Melting is physical._
- ◻️ grinding pepper  
  _↳ feedback if chosen: Grinding only makes small pieces._

Full working after a second miss:

> Digestion breaks food into new substances.  
> So the answer is “digesting food”.  

> What is given out when a substance burns?

- ✅ heat and light
- ◻️ only water  
  _↳ feedback if chosen: Water may form, but heat and light are always given out._
- ◻️ nothing  
  _↳ feedback if chosen: Burning gives out heat and light._
- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen is used up when things burn._

Full working after a second miss:

> Combustion gives out heat and light.  
> So the answer is “heat and light”.  

> What does an acid react with in neutralisation?

- ✅ a base (alkali)
- ◻️ a noble gas  
  _↳ feedback if chosen: Noble gases do not react._
- ◻️ oxygen  
  _↳ feedback if chosen: That is combustion._
- ◻️ another acid  
  _↳ feedback if chosen: Two acids do not neutralise each other._

Full working after a second miss:

> Acid + base → salt + water.  
> So the answer is “a base (alkali)”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-21-disp` · Lesson 21 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Zinc is more reactive than copper. What happens when zinc is put in copper sulphate solution? | Copper is displaced and zinc sulphate forms. | Nothing happens. · Zinc is displaced. · Oxygen is given off. | Zinc is more reactive, so it does react. · The more reactive metal stays in the compound, not out of it. · No oxygen is made here. | The more reactive metal takes the place of the less reactive one. |
| Copper is less reactive than iron. Will copper displace iron from iron sulphate? | No | Yes · Only when cold · Only in the dark | A less reactive metal cannot push out a more reactive one. · Temperature does not change the order of reactivity. · Light does not matter. | Only a more reactive metal can displace another. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Zinc is more reactive than copper. What happens when zinc is put in copper sulphate solution?

- ✅ Copper is displaced and zinc sulphate forms.
- ◻️ Oxygen is given off.  
  _↳ feedback if chosen: No oxygen is made here._
- ◻️ Zinc is displaced.  
  _↳ feedback if chosen: The more reactive metal stays in the compound, not out of it._
- ◻️ Nothing happens.  
  _↳ feedback if chosen: Zinc is more reactive, so it does react._

Full working after a second miss:

> The more reactive metal takes the place of the less reactive one.  
> So the answer is “Copper is displaced and zinc sulphate forms.”.  

> Zinc is more reactive than copper. What happens when zinc is put in copper sulphate solution?

- ◻️ Oxygen is given off.  
  _↳ feedback if chosen: No oxygen is made here._
- ✅ Copper is displaced and zinc sulphate forms.
- ◻️ Nothing happens.  
  _↳ feedback if chosen: Zinc is more reactive, so it does react._
- ◻️ Zinc is displaced.  
  _↳ feedback if chosen: The more reactive metal stays in the compound, not out of it._

Full working after a second miss:

> The more reactive metal takes the place of the less reactive one.  
> So the answer is “Copper is displaced and zinc sulphate forms.”.  

> Zinc is more reactive than copper. What happens when zinc is put in copper sulphate solution?

- ◻️ Oxygen is given off.  
  _↳ feedback if chosen: No oxygen is made here._
- ✅ Copper is displaced and zinc sulphate forms.
- ◻️ Zinc is displaced.  
  _↳ feedback if chosen: The more reactive metal stays in the compound, not out of it._
- ◻️ Nothing happens.  
  _↳ feedback if chosen: Zinc is more reactive, so it does react._

Full working after a second miss:

> The more reactive metal takes the place of the less reactive one.  
> So the answer is “Copper is displaced and zinc sulphate forms.”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-21-spot` · Lesson 21 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Heating limestone is a decomposition reaction.
- ✅ Burning is a reaction with oxygen.
- ✅ Neutralisation gives a salt and water.
- ✅ Respiration is a chemical reaction.
- ❌ Combination: one substance breaks into two.  
  _↳ That is decomposition; combination joins substances._
- ❌ Copper displaces zinc from zinc sulphate.  
  _↳ Copper is less reactive than zinc, so it cannot._
- ❌ Photosynthesis is a physical change.  
  _↳ Photosynthesis makes glucose and oxygen: a chemical change._


Three generated variants:

> Which statement is wrong?

- ◻️ Heating limestone is a decomposition reaction.
- ◻️ Burning is a reaction with oxygen.
- ✅ Combination: one substance breaks into two.  
  _↳ explanation: That is decomposition; combination joins substances._
- ◻️ Neutralisation gives a salt and water.

Full working after a second miss:

> The wrong statement is “Combination: one substance breaks into two.”.  
> That is decomposition; combination joins substances.  

> Which statement is wrong?

- ◻️ Neutralisation gives a salt and water.
- ✅ Photosynthesis is a physical change.  
  _↳ explanation: Photosynthesis makes glucose and oxygen: a chemical change._
- ◻️ Respiration is a chemical reaction.
- ◻️ Burning is a reaction with oxygen.

Full working after a second miss:

> The wrong statement is “Photosynthesis is a physical change.”.  
> Photosynthesis makes glucose and oxygen: a chemical change.  

> Which statement is wrong?

- ✅ Combination: one substance breaks into two.  
  _↳ explanation: That is decomposition; combination joins substances._
- ◻️ Respiration is a chemical reaction.
- ◻️ Burning is a reaction with oxygen.
- ◻️ Heating limestone is a decomposition reaction.

Full working after a second miss:

> The wrong statement is “Combination: one substance breaks into two.”.  
> That is decomposition; combination joins substances.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-21-disp-card` · Lesson 21 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Zinc is more reactive than copper. What happens when zinc is put in copper sulphate solution? | Copper is displaced and zinc sulphate forms. | Nothing happens. · Zinc is displaced. · Oxygen is given off. | Zinc is more reactive, so it does react. · The more reactive metal stays in the compound, not out of it. · No oxygen is made here. | The more reactive metal takes the place of the less reactive one. |
| Copper is less reactive than iron. Will copper displace iron from iron sulphate? | No | Yes · Only when cold · Only in the dark | A less reactive metal cannot push out a more reactive one. · Temperature does not change the order of reactivity. · Light does not matter. | Only a more reactive metal can displace another. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Copper is less reactive than iron. Will copper displace iron from iron sulphate?

- ◻️ Only in the dark  
  _↳ feedback if chosen: Light does not matter._
- ◻️ Only when cold  
  _↳ feedback if chosen: Temperature does not change the order of reactivity._
- ◻️ Yes  
  _↳ feedback if chosen: A less reactive metal cannot push out a more reactive one._
- ✅ No

Full working after a second miss:

> Only a more reactive metal can displace another.  
> So the answer is “No”.  

> Zinc is more reactive than copper. What happens when zinc is put in copper sulphate solution?

- ◻️ Zinc is displaced.  
  _↳ feedback if chosen: The more reactive metal stays in the compound, not out of it._
- ◻️ Oxygen is given off.  
  _↳ feedback if chosen: No oxygen is made here._
- ◻️ Nothing happens.  
  _↳ feedback if chosen: Zinc is more reactive, so it does react._
- ✅ Copper is displaced and zinc sulphate forms.

Full working after a second miss:

> The more reactive metal takes the place of the less reactive one.  
> So the answer is “Copper is displaced and zinc sulphate forms.”.  

> Zinc is more reactive than copper. What happens when zinc is put in copper sulphate solution?

- ✅ Copper is displaced and zinc sulphate forms.
- ◻️ Nothing happens.  
  _↳ feedback if chosen: Zinc is more reactive, so it does react._
- ◻️ Zinc is displaced.  
  _↳ feedback if chosen: The more reactive metal stays in the compound, not out of it._
- ◻️ Oxygen is given off.  
  _↳ feedback if chosen: No oxygen is made here._

Full working after a second miss:

> The more reactive metal takes the place of the less reactive one.  
> So the answer is “Copper is displaced and zinc sulphate forms.”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-22-read` · Lesson 22 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In a word equation, what does the arrow (→) mean? | gives (forms) | equals exactly · and · is mixed with | It shows a change, not equal quantities. · That is what + means on the right. · The substances react; they are not just mixed. | The arrow means react to form. |
| In copper + oxygen → copper oxide, which side shows the reactants? | the left side | the right side · both sides · neither side | The right side shows the products. · Products are only on the right. · The reactants are written on the left. | Reactants are always on the left. |
| In hydrogen + oxygen → water, how many products are there? | one | two · three · none | Hydrogen and oxygen are reactants. · Count only the right side. · Water is a product. | Only water is on the right. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In hydrogen + oxygen → water, how many products are there?

- ◻️ two  
  _↳ feedback if chosen: Hydrogen and oxygen are reactants._
- ✅ one
- ◻️ three  
  _↳ feedback if chosen: Count only the right side._
- ◻️ none  
  _↳ feedback if chosen: Water is a product._

Full working after a second miss:

> Only water is on the right.  
> So the answer is “one”.  

> In a word equation, what does the arrow (→) mean?

- ◻️ and  
  _↳ feedback if chosen: That is what + means on the right._
- ◻️ is mixed with  
  _↳ feedback if chosen: The substances react; they are not just mixed._
- ◻️ equals exactly  
  _↳ feedback if chosen: It shows a change, not equal quantities._
- ✅ gives (forms)

Full working after a second miss:

> The arrow means react to form.  
> So the answer is “gives (forms)”.  

> In hydrogen + oxygen → water, how many products are there?

- ◻️ three  
  _↳ feedback if chosen: Count only the right side._
- ◻️ two  
  _↳ feedback if chosen: Hydrogen and oxygen are reactants._
- ✅ one
- ◻️ none  
  _↳ feedback if chosen: Water is a product._

Full working after a second miss:

> Only water is on the right.  
> So the answer is “one”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-22-name` · Lesson 22 · multiple choice, level 2

Prompt: Complete the word equation: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| magnesium + oxygen → ___ | magnesium oxide | magnesium oxygen · magnesium carbonate · oxygen magnesium | The non-metal part ends in -ide: oxide. · There is no carbon. · The metal is named first. | Metal + oxygen → metal oxide. |
| sodium + chlorine → ___ | sodium chloride | sodium chlorine · chlorine sodide · sodium chlorate | Chlorine becomes chloride. · The metal is named first and keeps its name. · Chlorate contains oxygen too. | Metal + chlorine → metal chloride. |
| zinc + hydrochloric acid → zinc chloride + ___ | hydrogen | oxygen · water · chlorine | No oxygen is in the reactants. · Metal + acid gives hydrogen, not water. · The chlorine is in the zinc chloride. | Metal + acid → salt + hydrogen. |
| carbon + oxygen → ___ | carbon dioxide | carbon oxygen · carbonate · water | Name the compound: carbon dioxide. · A carbonate has a metal too. · There is no hydrogen. | Carbon burns to carbon dioxide. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Complete the word equation: zinc + hydrochloric acid → zinc chloride + ___

- ◻️ oxygen  
  _↳ feedback if chosen: No oxygen is in the reactants._
- ✅ hydrogen
- ◻️ chlorine  
  _↳ feedback if chosen: The chlorine is in the zinc chloride._
- ◻️ water  
  _↳ feedback if chosen: Metal + acid gives hydrogen, not water._

Full working after a second miss:

> Metal + acid → salt + hydrogen.  
> So the answer is “hydrogen”.  

> Complete the word equation: magnesium + oxygen → ___

- ◻️ magnesium oxygen  
  _↳ feedback if chosen: The non-metal part ends in -ide: oxide._
- ✅ magnesium oxide
- ◻️ magnesium carbonate  
  _↳ feedback if chosen: There is no carbon._
- ◻️ oxygen magnesium  
  _↳ feedback if chosen: The metal is named first._

Full working after a second miss:

> Metal + oxygen → metal oxide.  
> So the answer is “magnesium oxide”.  

> Complete the word equation: zinc + hydrochloric acid → zinc chloride + ___

- ✅ hydrogen
- ◻️ chlorine  
  _↳ feedback if chosen: The chlorine is in the zinc chloride._
- ◻️ water  
  _↳ feedback if chosen: Metal + acid gives hydrogen, not water._
- ◻️ oxygen  
  _↳ feedback if chosen: No oxygen is in the reactants._

Full working after a second miss:

> Metal + acid → salt + hydrogen.  
> So the answer is “hydrogen”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-22-spot` · Lesson 22 · spot the error, level 3

Prompt: Which word equation is written wrongly?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ iron + sulphur → iron sulphide
- ✅ calcium + oxygen → calcium oxide
- ✅ methane + oxygen → carbon dioxide + water
- ✅ magnesium + hydrochloric acid → magnesium chloride + hydrogen
- ❌ magnesium oxide → magnesium + oxygen when magnesium burns  
  _↳ Magnesium and oxygen are the reactants: they go on the left._
- ❌ sodium + chlorine → sodium chlorine  
  _↳ The product is named sodium chloride._
- ❌ carbon + oxygen → carbon + oxygen  
  _↳ The product, carbon dioxide, must be on the right._


Three generated variants:

> Which word equation is written wrongly?

- ◻️ iron + sulphur → iron sulphide
- ◻️ magnesium + hydrochloric acid → magnesium chloride + hydrogen
- ✅ carbon + oxygen → carbon + oxygen  
  _↳ explanation: The product, carbon dioxide, must be on the right._
- ◻️ methane + oxygen → carbon dioxide + water

Full working after a second miss:

> The wrong statement is “carbon + oxygen → carbon + oxygen”.  
> The product, carbon dioxide, must be on the right.  

> Which word equation is written wrongly?

- ◻️ magnesium + hydrochloric acid → magnesium chloride + hydrogen
- ◻️ calcium + oxygen → calcium oxide
- ✅ sodium + chlorine → sodium chlorine  
  _↳ explanation: The product is named sodium chloride._
- ◻️ methane + oxygen → carbon dioxide + water

Full working after a second miss:

> The wrong statement is “sodium + chlorine → sodium chlorine”.  
> The product is named sodium chloride.  

> Which word equation is written wrongly?

- ◻️ calcium + oxygen → calcium oxide
- ◻️ magnesium + hydrochloric acid → magnesium chloride + hydrogen
- ◻️ methane + oxygen → carbon dioxide + water
- ✅ carbon + oxygen → carbon + oxygen  
  _↳ explanation: The product, carbon dioxide, must be on the right._

Full working after a second miss:

> The wrong statement is “carbon + oxygen → carbon + oxygen”.  
> The product, carbon dioxide, must be on the right.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-22-name-card` · Lesson 22 · multiple choice, level 1

Prompt: Complete the word equation: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| magnesium + oxygen → ___ | magnesium oxide | magnesium oxygen · magnesium carbonate · oxygen magnesium | The non-metal part ends in -ide: oxide. · There is no carbon. · The metal is named first. | Metal + oxygen → metal oxide. |
| sodium + chlorine → ___ | sodium chloride | sodium chlorine · chlorine sodide · sodium chlorate | Chlorine becomes chloride. · The metal is named first and keeps its name. · Chlorate contains oxygen too. | Metal + chlorine → metal chloride. |
| zinc + hydrochloric acid → zinc chloride + ___ | hydrogen | oxygen · water · chlorine | No oxygen is in the reactants. · Metal + acid gives hydrogen, not water. · The chlorine is in the zinc chloride. | Metal + acid → salt + hydrogen. |
| carbon + oxygen → ___ | carbon dioxide | carbon oxygen · carbonate · water | Name the compound: carbon dioxide. · A carbonate has a metal too. · There is no hydrogen. | Carbon burns to carbon dioxide. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Complete the word equation: carbon + oxygen → ___

- ✅ carbon dioxide
- ◻️ carbon oxygen  
  _↳ feedback if chosen: Name the compound: carbon dioxide._
- ◻️ carbonate  
  _↳ feedback if chosen: A carbonate has a metal too._
- ◻️ water  
  _↳ feedback if chosen: There is no hydrogen._

Full working after a second miss:

> Carbon burns to carbon dioxide.  
> So the answer is “carbon dioxide”.  

> Complete the word equation: sodium + chlorine → ___

- ◻️ chlorine sodide  
  _↳ feedback if chosen: The metal is named first and keeps its name._
- ◻️ sodium chlorate  
  _↳ feedback if chosen: Chlorate contains oxygen too._
- ✅ sodium chloride
- ◻️ sodium chlorine  
  _↳ feedback if chosen: Chlorine becomes chloride._

Full working after a second miss:

> Metal + chlorine → metal chloride.  
> So the answer is “sodium chloride”.  

> Complete the word equation: zinc + hydrochloric acid → zinc chloride + ___

- ✅ hydrogen
- ◻️ chlorine  
  _↳ feedback if chosen: The chlorine is in the zinc chloride._
- ◻️ oxygen  
  _↳ feedback if chosen: No oxygen is in the reactants._
- ◻️ water  
  _↳ feedback if chosen: Metal + acid gives hydrogen, not water._

Full working after a second miss:

> Metal + acid → salt + hydrogen.  
> So the answer is “hydrogen”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-23-gas` · Lesson 23 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the formula of oxygen gas? | O₂ | O · O₃ · OX | Oxygen gas is made of molecules of two atoms. · O₃ is ozone. · There is no element X. | Oxygen gas is diatomic: O₂. |
| What is the formula of hydrogen gas? | H₂ | H · H₂O · 2H | Hydrogen gas is made of molecules of two atoms. · H₂O is water. · 2H means two separate atoms. | Hydrogen gas is diatomic: H₂. |
| What is the formula of chlorine gas? | Cl₂ | Cl · CL · C₂ | Chlorine gas is diatomic. · The second letter of a symbol is small. · C is carbon. | Chlorine gas is Cl₂. |
| What is the formula of nitrogen gas? | N₂ | N · Ni · NO₂ | Nitrogen gas is diatomic. · Ni is nickel. · NO₂ is nitrogen dioxide. | Nitrogen gas is N₂. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the formula of oxygen gas?

- ◻️ O₃  
  _↳ feedback if chosen: O₃ is ozone._
- ✅ O₂
- ◻️ OX  
  _↳ feedback if chosen: There is no element X._
- ◻️ O  
  _↳ feedback if chosen: Oxygen gas is made of molecules of two atoms._

Full working after a second miss:

> Oxygen gas is diatomic: O₂.  
> So the answer is “O₂”.  

> What is the formula of chlorine gas?

- ◻️ CL  
  _↳ feedback if chosen: The second letter of a symbol is small._
- ✅ Cl₂
- ◻️ C₂  
  _↳ feedback if chosen: C is carbon._
- ◻️ Cl  
  _↳ feedback if chosen: Chlorine gas is diatomic._

Full working after a second miss:

> Chlorine gas is Cl₂.  
> So the answer is “Cl₂”.  

> What is the formula of nitrogen gas?

- ◻️ Ni  
  _↳ feedback if chosen: Ni is nickel._
- ◻️ N  
  _↳ feedback if chosen: Nitrogen gas is diatomic._
- ◻️ NO₂  
  _↳ feedback if chosen: NO₂ is nitrogen dioxide._
- ✅ N₂

Full working after a second miss:

> Nitrogen gas is N₂.  
> So the answer is “N₂”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-23-state` · Lesson 23 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does (aq) mean after a formula? | dissolved in water | a liquid · a gas · a solid | A pure liquid is (l). · A gas is (g). · A solid is (s). | aq is from aqua, water. |
| Which state symbol is used for water as a liquid? | (l) | (aq) · (s) · (w) | (aq) means dissolved in water. · (s) is a solid. · There is no symbol (w). | (l) means liquid. |
| Carbon dioxide is given off as bubbles. Which state symbol does it take? | (g) | (l) · (s) · (aq) | Bubbles are a gas. · Bubbles are a gas, not a solid. · The bubbles escape; they are not dissolved. | A gas takes (g). |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does (aq) mean after a formula?

- ◻️ a gas  
  _↳ feedback if chosen: A gas is (g)._
- ✅ dissolved in water
- ◻️ a liquid  
  _↳ feedback if chosen: A pure liquid is (l)._
- ◻️ a solid  
  _↳ feedback if chosen: A solid is (s)._

Full working after a second miss:

> aq is from aqua, water.  
> So the answer is “dissolved in water”.  

> Which state symbol is used for water as a liquid?

- ◻️ (aq)  
  _↳ feedback if chosen: (aq) means dissolved in water._
- ✅ (l)
- ◻️ (s)  
  _↳ feedback if chosen: (s) is a solid._
- ◻️ (w)  
  _↳ feedback if chosen: There is no symbol (w)._

Full working after a second miss:

> (l) means liquid.  
> So the answer is “(l)”.  

> Which state symbol is used for water as a liquid?

- ◻️ (aq)  
  _↳ feedback if chosen: (aq) means dissolved in water._
- ◻️ (w)  
  _↳ feedback if chosen: There is no symbol (w)._
- ◻️ (s)  
  _↳ feedback if chosen: (s) is a solid._
- ✅ (l)

Full working after a second miss:

> (l) means liquid.  
> So the answer is “(l)”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-23-state-card` · Lesson 23 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does (aq) mean after a formula? | dissolved in water | a liquid · a gas · a solid | A pure liquid is (l). · A gas is (g). · A solid is (s). | aq is from aqua, water. |
| Which state symbol is used for water as a liquid? | (l) | (aq) · (s) · (w) | (aq) means dissolved in water. · (s) is a solid. · There is no symbol (w). | (l) means liquid. |
| Carbon dioxide is given off as bubbles. Which state symbol does it take? | (g) | (l) · (s) · (aq) | Bubbles are a gas. · Bubbles are a gas, not a solid. · The bubbles escape; they are not dissolved. | A gas takes (g). |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does (aq) mean after a formula?

- ◻️ a gas  
  _↳ feedback if chosen: A gas is (g)._
- ◻️ a liquid  
  _↳ feedback if chosen: A pure liquid is (l)._
- ✅ dissolved in water
- ◻️ a solid  
  _↳ feedback if chosen: A solid is (s)._

Full working after a second miss:

> aq is from aqua, water.  
> So the answer is “dissolved in water”.  

> Carbon dioxide is given off as bubbles. Which state symbol does it take?

- ◻️ (aq)  
  _↳ feedback if chosen: The bubbles escape; they are not dissolved._
- ◻️ (l)  
  _↳ feedback if chosen: Bubbles are a gas._
- ✅ (g)
- ◻️ (s)  
  _↳ feedback if chosen: Bubbles are a gas, not a solid._

Full working after a second miss:

> A gas takes (g).  
> So the answer is “(g)”.  

> What does (aq) mean after a formula?

- ◻️ a liquid  
  _↳ feedback if chosen: A pure liquid is (l)._
- ◻️ a solid  
  _↳ feedback if chosen: A solid is (s)._
- ◻️ a gas  
  _↳ feedback if chosen: A gas is (g)._
- ✅ dissolved in water

Full working after a second miss:

> aq is from aqua, water.  
> So the answer is “dissolved in water”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-24-rule` · Lesson 24 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| To balance H₂ + O₂ → H₂O, what may you change? | the numbers in front of the formulae | the small numbers in the formulae · the symbols · the arrow | Changing H₂O to H₂O₂ makes a different substance. · The substances must stay the same. · The arrow is not a number. | Only coefficients are changed. |
| Why must an equation be balanced? | Atoms are not created or destroyed in a reaction. | To make it look tidy · Because products are heavier · Because gases have no mass | It shows a real rule of nature. · The total mass stays the same. · Gases do have mass. | The same atoms are only rearranged. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why must an equation be balanced?

- ◻️ Because products are heavier  
  _↳ feedback if chosen: The total mass stays the same._
- ◻️ To make it look tidy  
  _↳ feedback if chosen: It shows a real rule of nature._
- ◻️ Because gases have no mass  
  _↳ feedback if chosen: Gases do have mass._
- ✅ Atoms are not created or destroyed in a reaction.

Full working after a second miss:

> The same atoms are only rearranged.  
> So the answer is “Atoms are not created or destroyed in a reaction.”.  

> To balance H₂ + O₂ → H₂O, what may you change?

- ◻️ the symbols  
  _↳ feedback if chosen: The substances must stay the same._
- ◻️ the small numbers in the formulae  
  _↳ feedback if chosen: Changing H₂O to H₂O₂ makes a different substance._
- ✅ the numbers in front of the formulae
- ◻️ the arrow  
  _↳ feedback if chosen: The arrow is not a number._

Full working after a second miss:

> Only coefficients are changed.  
> So the answer is “the numbers in front of the formulae”.  

> To balance H₂ + O₂ → H₂O, what may you change?

- ◻️ the small numbers in the formulae  
  _↳ feedback if chosen: Changing H₂O to H₂O₂ makes a different substance._
- ◻️ the arrow  
  _↳ feedback if chosen: The arrow is not a number._
- ◻️ the symbols  
  _↳ feedback if chosen: The substances must stay the same._
- ✅ the numbers in front of the formulae

Full working after a second miss:

> Only coefficients are changed.  
> So the answer is “the numbers in front of the formulae”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-26-open` · Lesson 26 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Magnesium ribbon is burned in an open crucible. Why is the ash heavier than the magnesium? | Oxygen from the air has joined the magnesium. | Mass was created in the reaction. · The flame added mass. · Magnesium is lighter when hot. | Mass is never created. · Heat has no mass. · The ash was weighed cold. | Magnesium + oxygen → magnesium oxide: the oxygen adds mass. |
| A piece of wood is burned in the open. Why is the ash lighter than the wood? | Gases and smoke escaped into the air. | Mass was destroyed. · The ash is a different element. · Wood has no mass when dry. | Mass is never destroyed. · The ash is not lighter for that reason. · Wood has mass. | The products include gases that escaped. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A piece of wood is burned in the open. Why is the ash lighter than the wood?

- ◻️ Mass was destroyed.  
  _↳ feedback if chosen: Mass is never destroyed._
- ◻️ Wood has no mass when dry.  
  _↳ feedback if chosen: Wood has mass._
- ◻️ The ash is a different element.  
  _↳ feedback if chosen: The ash is not lighter for that reason._
- ✅ Gases and smoke escaped into the air.

Full working after a second miss:

> The products include gases that escaped.  
> So the answer is “Gases and smoke escaped into the air.”.  

> Magnesium ribbon is burned in an open crucible. Why is the ash heavier than the magnesium?

- ✅ Oxygen from the air has joined the magnesium.
- ◻️ The flame added mass.  
  _↳ feedback if chosen: Heat has no mass._
- ◻️ Magnesium is lighter when hot.  
  _↳ feedback if chosen: The ash was weighed cold._
- ◻️ Mass was created in the reaction.  
  _↳ feedback if chosen: Mass is never created._

Full working after a second miss:

> Magnesium + oxygen → magnesium oxide: the oxygen adds mass.  
> So the answer is “Oxygen from the air has joined the magnesium.”.  

> A piece of wood is burned in the open. Why is the ash lighter than the wood?

- ◻️ The ash is a different element.  
  _↳ feedback if chosen: The ash is not lighter for that reason._
- ◻️ Mass was destroyed.  
  _↳ feedback if chosen: Mass is never destroyed._
- ✅ Gases and smoke escaped into the air.
- ◻️ Wood has no mass when dry.  
  _↳ feedback if chosen: Wood has mass._

Full working after a second miss:

> The products include gases that escaped.  
> So the answer is “Gases and smoke escaped into the air.”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-26-open-card` · Lesson 26 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Magnesium ribbon is burned in an open crucible. Why is the ash heavier than the magnesium? | Oxygen from the air has joined the magnesium. | Mass was created in the reaction. · The flame added mass. · Magnesium is lighter when hot. | Mass is never created. · Heat has no mass. · The ash was weighed cold. | Magnesium + oxygen → magnesium oxide: the oxygen adds mass. |
| A piece of wood is burned in the open. Why is the ash lighter than the wood? | Gases and smoke escaped into the air. | Mass was destroyed. · The ash is a different element. · Wood has no mass when dry. | Mass is never destroyed. · The ash is not lighter for that reason. · Wood has mass. | The products include gases that escaped. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Magnesium ribbon is burned in an open crucible. Why is the ash heavier than the magnesium?

- ◻️ The flame added mass.  
  _↳ feedback if chosen: Heat has no mass._
- ◻️ Mass was created in the reaction.  
  _↳ feedback if chosen: Mass is never created._
- ◻️ Magnesium is lighter when hot.  
  _↳ feedback if chosen: The ash was weighed cold._
- ✅ Oxygen from the air has joined the magnesium.

Full working after a second miss:

> Magnesium + oxygen → magnesium oxide: the oxygen adds mass.  
> So the answer is “Oxygen from the air has joined the magnesium.”.  

> A piece of wood is burned in the open. Why is the ash lighter than the wood?

- ✅ Gases and smoke escaped into the air.
- ◻️ Wood has no mass when dry.  
  _↳ feedback if chosen: Wood has mass._
- ◻️ Mass was destroyed.  
  _↳ feedback if chosen: Mass is never destroyed._
- ◻️ The ash is a different element.  
  _↳ feedback if chosen: The ash is not lighter for that reason._

Full working after a second miss:

> The products include gases that escaped.  
> So the answer is “Gases and smoke escaped into the air.”.  

> A piece of wood is burned in the open. Why is the ash lighter than the wood?

- ✅ Gases and smoke escaped into the air.
- ◻️ Wood has no mass when dry.  
  _↳ feedback if chosen: Wood has mass._
- ◻️ Mass was destroyed.  
  _↳ feedback if chosen: Mass is never destroyed._
- ◻️ The ash is a different element.  
  _↳ feedback if chosen: The ash is not lighter for that reason._

Full working after a second miss:

> The products include gases that escaped.  
> So the answer is “Gases and smoke escaped into the air.”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-27-law` · Lesson 27 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does the law of conservation of mass say? | Matter is neither created nor destroyed in a chemical reaction. | Products are always heavier than reactants. · Gases have no mass. · Mass is lost as heat. | The total mass is equal. · Gases have mass. · Heat has no mass. | Total mass of reactants = total mass of products. |
| Which scientist stated the law of conservation of mass? | Antoine Lavoisier | John Dalton · Dmitri Mendeleev · Isaac Newton | Dalton gave the atomic theory. · Mendeleev made the periodic table. · Newton studied forces. | Lavoisier, the French chemist. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which scientist stated the law of conservation of mass?

- ✅ Antoine Lavoisier
- ◻️ Isaac Newton  
  _↳ feedback if chosen: Newton studied forces._
- ◻️ Dmitri Mendeleev  
  _↳ feedback if chosen: Mendeleev made the periodic table._
- ◻️ John Dalton  
  _↳ feedback if chosen: Dalton gave the atomic theory._

Full working after a second miss:

> Lavoisier, the French chemist.  
> So the answer is “Antoine Lavoisier”.  

> Which scientist stated the law of conservation of mass?

- ✅ Antoine Lavoisier
- ◻️ Dmitri Mendeleev  
  _↳ feedback if chosen: Mendeleev made the periodic table._
- ◻️ Isaac Newton  
  _↳ feedback if chosen: Newton studied forces._
- ◻️ John Dalton  
  _↳ feedback if chosen: Dalton gave the atomic theory._

Full working after a second miss:

> Lavoisier, the French chemist.  
> So the answer is “Antoine Lavoisier”.  

> What does the law of conservation of mass say?

- ◻️ Gases have no mass.  
  _↳ feedback if chosen: Gases have mass._
- ◻️ Products are always heavier than reactants.  
  _↳ feedback if chosen: The total mass is equal._
- ◻️ Mass is lost as heat.  
  _↳ feedback if chosen: Heat has no mass._
- ✅ Matter is neither created nor destroyed in a chemical reaction.

Full working after a second miss:

> Total mass of reactants = total mass of products.  
> So the answer is “Matter is neither created nor destroyed in a chemical reaction.”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-27-exp` · Lesson 27 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is the flask closed in the experiment on conservation of mass? | So that nothing can escape or enter. | To keep it warm · To stop the precipitate forming · To make it lighter | Temperature is not the reason. · The precipitate forms anyway. · A stopper does not make it lighter. | All the matter must stay inside to be weighed. |
| The closed flask weighed 150 g before mixing. What does it weigh after the yellow precipitate forms? | 150 g | more than 150 g · less than 150 g · 0 g | Nothing entered the flask. · Nothing escaped from the flask. · The flask still has its contents. | Mass is conserved. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is the flask closed in the experiment on conservation of mass?

- ◻️ To stop the precipitate forming  
  _↳ feedback if chosen: The precipitate forms anyway._
- ◻️ To make it lighter  
  _↳ feedback if chosen: A stopper does not make it lighter._
- ◻️ To keep it warm  
  _↳ feedback if chosen: Temperature is not the reason._
- ✅ So that nothing can escape or enter.

Full working after a second miss:

> All the matter must stay inside to be weighed.  
> So the answer is “So that nothing can escape or enter.”.  

> Why is the flask closed in the experiment on conservation of mass?

- ◻️ To make it lighter  
  _↳ feedback if chosen: A stopper does not make it lighter._
- ✅ So that nothing can escape or enter.
- ◻️ To keep it warm  
  _↳ feedback if chosen: Temperature is not the reason._
- ◻️ To stop the precipitate forming  
  _↳ feedback if chosen: The precipitate forms anyway._

Full working after a second miss:

> All the matter must stay inside to be weighed.  
> So the answer is “So that nothing can escape or enter.”.  

> The closed flask weighed 150 g before mixing. What does it weigh after the yellow precipitate forms?

- ◻️ less than 150 g  
  _↳ feedback if chosen: Nothing escaped from the flask._
- ✅ 150 g
- ◻️ more than 150 g  
  _↳ feedback if chosen: Nothing entered the flask._
- ◻️ 0 g  
  _↳ feedback if chosen: The flask still has its contents._

Full working after a second miss:

> Mass is conserved.  
> So the answer is “150 g”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-27-exp-card` · Lesson 27 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is the flask closed in the experiment on conservation of mass? | So that nothing can escape or enter. | To keep it warm · To stop the precipitate forming · To make it lighter | Temperature is not the reason. · The precipitate forms anyway. · A stopper does not make it lighter. | All the matter must stay inside to be weighed. |
| The closed flask weighed 150 g before mixing. What does it weigh after the yellow precipitate forms? | 150 g | more than 150 g · less than 150 g · 0 g | Nothing entered the flask. · Nothing escaped from the flask. · The flask still has its contents. | Mass is conserved. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is the flask closed in the experiment on conservation of mass?

- ◻️ To keep it warm  
  _↳ feedback if chosen: Temperature is not the reason._
- ◻️ To stop the precipitate forming  
  _↳ feedback if chosen: The precipitate forms anyway._
- ◻️ To make it lighter  
  _↳ feedback if chosen: A stopper does not make it lighter._
- ✅ So that nothing can escape or enter.

Full working after a second miss:

> All the matter must stay inside to be weighed.  
> So the answer is “So that nothing can escape or enter.”.  

> The closed flask weighed 150 g before mixing. What does it weigh after the yellow precipitate forms?

- ◻️ less than 150 g  
  _↳ feedback if chosen: Nothing escaped from the flask._
- ◻️ more than 150 g  
  _↳ feedback if chosen: Nothing entered the flask._
- ◻️ 0 g  
  _↳ feedback if chosen: The flask still has its contents._
- ✅ 150 g

Full working after a second miss:

> Mass is conserved.  
> So the answer is “150 g”.  

> Why is the flask closed in the experiment on conservation of mass?

- ◻️ To keep it warm  
  _↳ feedback if chosen: Temperature is not the reason._
- ✅ So that nothing can escape or enter.
- ◻️ To make it lighter  
  _↳ feedback if chosen: A stopper does not make it lighter._
- ◻️ To stop the precipitate forming  
  _↳ feedback if chosen: The precipitate forms anyway._

Full working after a second miss:

> All the matter must stay inside to be weighed.  
> So the answer is “So that nothing can escape or enter.”.  

Sources: reactions-equations (Physical and chemical changes; types of reaction (combination, decomposition, combustion, displacement, neutralisation); word and symbolic equations, state symbols; balancing by coefficients; the law of conservation of mass (Lavoisier) and the closed-flask experiment (lead nitrate + potassium iodide))

### `k2-29-parts` · Lesson 29 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which gas makes up the largest part of air? | nitrogen | oxygen · carbon dioxide · argon | Oxygen is only about 21%. · Carbon dioxide is a tiny part. · Argon is under 1%. | Nitrogen is about 78% of air. |
| About what percentage of air is oxygen? | 21% | 78% · 50% · 1% | 78% is nitrogen. · Oxygen is about one fifth, not half. · Argon is about 1%. | Oxygen is about 21% of air. |
| Which noble gas is found in air (about 0.9%)? | argon | chlorine · hydrogen · fluorine | Chlorine is not a noble gas. · Hydrogen is not a noble gas. · Fluorine is a halogen. | Argon is the main noble gas in air. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which gas makes up the largest part of air?

- ◻️ argon  
  _↳ feedback if chosen: Argon is under 1%._
- ◻️ carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide is a tiny part._
- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen is only about 21%._
- ✅ nitrogen

Full working after a second miss:

> Nitrogen is about 78% of air.  
> So the answer is “nitrogen”.  

> About what percentage of air is oxygen?

- ◻️ 1%  
  _↳ feedback if chosen: Argon is about 1%._
- ◻️ 78%  
  _↳ feedback if chosen: 78% is nitrogen._
- ✅ 21%
- ◻️ 50%  
  _↳ feedback if chosen: Oxygen is about one fifth, not half._

Full working after a second miss:

> Oxygen is about 21% of air.  
> So the answer is “21%”.  

> Which noble gas is found in air (about 0.9%)?

- ◻️ hydrogen  
  _↳ feedback if chosen: Hydrogen is not a noble gas._
- ✅ argon
- ◻️ fluorine  
  _↳ feedback if chosen: Fluorine is a halogen._
- ◻️ chlorine  
  _↳ feedback if chosen: Chlorine is not a noble gas._

Full working after a second miss:

> Argon is the main noble gas in air.  
> So the answer is “argon”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-29-copper` · Lesson 29 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In the experiment, what happens to the heated copper? | It turns black. | It melts. · It turns white. · Nothing happens. | The tube is not hot enough to melt copper. · Copper oxide is black. · It reacts with oxygen. | Copper(II) oxide is black. |
| Which gas is mainly left in the syringe at the end? | nitrogen | oxygen · carbon dioxide · hydrogen | The oxygen was used by the copper. · Carbon dioxide is a tiny part. · Air has almost no hydrogen. | Nitrogen does not react with copper. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which gas is mainly left in the syringe at the end?

- ✅ nitrogen
- ◻️ carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide is a tiny part._
- ◻️ hydrogen  
  _↳ feedback if chosen: Air has almost no hydrogen._
- ◻️ oxygen  
  _↳ feedback if chosen: The oxygen was used by the copper._

Full working after a second miss:

> Nitrogen does not react with copper.  
> So the answer is “nitrogen”.  

> Which gas is mainly left in the syringe at the end?

- ◻️ hydrogen  
  _↳ feedback if chosen: Air has almost no hydrogen._
- ✅ nitrogen
- ◻️ carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide is a tiny part._
- ◻️ oxygen  
  _↳ feedback if chosen: The oxygen was used by the copper._

Full working after a second miss:

> Nitrogen does not react with copper.  
> So the answer is “nitrogen”.  

> In the experiment, what happens to the heated copper?

- ◻️ It turns white.  
  _↳ feedback if chosen: Copper oxide is black._
- ◻️ Nothing happens.  
  _↳ feedback if chosen: It reacts with oxygen._
- ✅ It turns black.
- ◻️ It melts.  
  _↳ feedback if chosen: The tube is not hot enough to melt copper._

Full working after a second miss:

> Copper(II) oxide is black.  
> So the answer is “It turns black.”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-30-active` · Lesson 30 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which part of air is called the active part? | oxygen | nitrogen · argon · water vapour | Nitrogen is inactive. · Argon is a noble gas: it hardly reacts. · Water vapour is not the active part. | Oxygen takes part in burning, rusting and breathing. |
| Why are patients with breathing problems given oxygen? | Their cells need oxygen for respiration. | To cool them · To put out fires · To make them sleep | Oxygen is not used for cooling. · Oxygen helps burning. · Oxygen is not a sleeping gas. | Respiration needs oxygen. |
| Which gas, with acetylene, gives a very hot flame for welding? | oxygen | nitrogen · argon · carbon dioxide | Nitrogen does not support burning. · Argon does not support burning. · Carbon dioxide puts fires out. | The oxy-acetylene flame. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which gas, with acetylene, gives a very hot flame for welding?

- ◻️ argon  
  _↳ feedback if chosen: Argon does not support burning._
- ◻️ carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide puts fires out._
- ✅ oxygen
- ◻️ nitrogen  
  _↳ feedback if chosen: Nitrogen does not support burning._

Full working after a second miss:

> The oxy-acetylene flame.  
> So the answer is “oxygen”.  

> Which part of air is called the active part?

- ◻️ nitrogen  
  _↳ feedback if chosen: Nitrogen is inactive._
- ◻️ argon  
  _↳ feedback if chosen: Argon is a noble gas: it hardly reacts._
- ✅ oxygen
- ◻️ water vapour  
  _↳ feedback if chosen: Water vapour is not the active part._

Full working after a second miss:

> Oxygen takes part in burning, rusting and breathing.  
> So the answer is “oxygen”.  

> Why are patients with breathing problems given oxygen?

- ◻️ To make them sleep  
  _↳ feedback if chosen: Oxygen is not a sleeping gas._
- ✅ Their cells need oxygen for respiration.
- ◻️ To put out fires  
  _↳ feedback if chosen: Oxygen helps burning._
- ◻️ To cool them  
  _↳ feedback if chosen: Oxygen is not used for cooling._

Full working after a second miss:

> Respiration needs oxygen.  
> So the answer is “Their cells need oxygen for respiration.”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-30-inactive` · Lesson 30 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which part of air is called the inactive part? | nitrogen | oxygen · carbon dioxide · water vapour | Oxygen is the active part. · Carbon dioxide is a small part used by plants. · Water vapour varies. | Nitrogen does not react easily. |
| Why is nitrogen put in packets of groundnuts? | It does not react, so the food stays fresh. | It adds taste. · It makes the packet heavier. · It kills the groundnuts. | Nitrogen has no taste. · That is not the reason. · The groundnuts are already dried. | Without oxygen the oil does not go bad. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is nitrogen put in packets of groundnuts?

- ◻️ It kills the groundnuts.  
  _↳ feedback if chosen: The groundnuts are already dried._
- ✅ It does not react, so the food stays fresh.
- ◻️ It makes the packet heavier.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ It adds taste.  
  _↳ feedback if chosen: Nitrogen has no taste._

Full working after a second miss:

> Without oxygen the oil does not go bad.  
> So the answer is “It does not react, so the food stays fresh.”.  

> Which part of air is called the inactive part?

- ◻️ carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide is a small part used by plants._
- ◻️ water vapour  
  _↳ feedback if chosen: Water vapour varies._
- ✅ nitrogen
- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen is the active part._

Full working after a second miss:

> Nitrogen does not react easily.  
> So the answer is “nitrogen”.  

> Why is nitrogen put in packets of groundnuts?

- ✅ It does not react, so the food stays fresh.
- ◻️ It makes the packet heavier.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ It adds taste.  
  _↳ feedback if chosen: Nitrogen has no taste._
- ◻️ It kills the groundnuts.  
  _↳ feedback if chosen: The groundnuts are already dried._

Full working after a second miss:

> Without oxygen the oil does not go bad.  
> So the answer is “It does not react, so the food stays fresh.”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-30-use` · Lesson 30 · multiple choice, level 2

Prompt: Which gas is used {X.q}?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| to make fertilisers | nitrogen | argon · oxygen · neon | Argon does not react. · Fertilisers need nitrogen compounds. · Neon is used in signs. | Nitrogen → ammonia → fertilisers. |
| to fill electric light bulbs | argon | oxygen · hydrogen · chlorine | Oxygen would make the filament burn. · Hydrogen is flammable. · Chlorine is poisonous and reactive. | Argon does not react with the hot filament. |
| in some fire extinguishers | carbon dioxide | oxygen · hydrogen · methane | Oxygen helps fires burn. · Hydrogen burns. · Methane burns. | Carbon dioxide does not support burning. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which gas is used to fill electric light bulbs?

- ◻️ hydrogen  
  _↳ feedback if chosen: Hydrogen is flammable._
- ◻️ chlorine  
  _↳ feedback if chosen: Chlorine is poisonous and reactive._
- ✅ argon
- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen would make the filament burn._

Full working after a second miss:

> Argon does not react with the hot filament.  
> So the answer is “argon”.  

> Which gas is used to fill electric light bulbs?

- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen would make the filament burn._
- ◻️ hydrogen  
  _↳ feedback if chosen: Hydrogen is flammable._
- ◻️ chlorine  
  _↳ feedback if chosen: Chlorine is poisonous and reactive._
- ✅ argon

Full working after a second miss:

> Argon does not react with the hot filament.  
> So the answer is “argon”.  

> Which gas is used to make fertilisers?

- ◻️ argon  
  _↳ feedback if chosen: Argon does not react._
- ◻️ neon  
  _↳ feedback if chosen: Neon is used in signs._
- ✅ nitrogen
- ◻️ oxygen  
  _↳ feedback if chosen: Fertilisers need nitrogen compounds._

Full working after a second miss:

> Nitrogen → ammonia → fertilisers.  
> So the answer is “nitrogen”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-30-spot` · Lesson 30 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Oxygen is used by divers.
- ✅ Nitrogen is used to make ammonia.
- ✅ Argon is used in light bulbs.
- ✅ Plants use carbon dioxide in photosynthesis.
- ❌ Nitrogen is the active part of air.  
  _↳ Oxygen is the active part; nitrogen is inactive._
- ❌ Carbon dioxide is used to help fires burn.  
  _↳ Carbon dioxide puts fires out._
- ❌ Food packets are filled with oxygen to keep food fresh.  
  _↳ Oxygen spoils food; nitrogen is used._


Three generated variants:

> Which statement is wrong?

- ✅ Carbon dioxide is used to help fires burn.  
  _↳ explanation: Carbon dioxide puts fires out._
- ◻️ Oxygen is used by divers.
- ◻️ Plants use carbon dioxide in photosynthesis.
- ◻️ Nitrogen is used to make ammonia.

Full working after a second miss:

> The wrong statement is “Carbon dioxide is used to help fires burn.”.  
> Carbon dioxide puts fires out.  

> Which statement is wrong?

- ◻️ Nitrogen is used to make ammonia.
- ◻️ Plants use carbon dioxide in photosynthesis.
- ✅ Nitrogen is the active part of air.  
  _↳ explanation: Oxygen is the active part; nitrogen is inactive._
- ◻️ Argon is used in light bulbs.

Full working after a second miss:

> The wrong statement is “Nitrogen is the active part of air.”.  
> Oxygen is the active part; nitrogen is inactive.  

> Which statement is wrong?

- ✅ Food packets are filled with oxygen to keep food fresh.  
  _↳ explanation: Oxygen spoils food; nitrogen is used._
- ◻️ Argon is used in light bulbs.
- ◻️ Nitrogen is used to make ammonia.
- ◻️ Oxygen is used by divers.

Full working after a second miss:

> The wrong statement is “Food packets are filled with oxygen to keep food fresh.”.  
> Oxygen spoils food; nitrogen is used.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-30-use-card` · Lesson 30 · multiple choice, level 1

Prompt: Which gas is used {X.q}?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| to make fertilisers | nitrogen | argon · oxygen · neon | Argon does not react. · Fertilisers need nitrogen compounds. · Neon is used in signs. | Nitrogen → ammonia → fertilisers. |
| to fill electric light bulbs | argon | oxygen · hydrogen · chlorine | Oxygen would make the filament burn. · Hydrogen is flammable. · Chlorine is poisonous and reactive. | Argon does not react with the hot filament. |
| in some fire extinguishers | carbon dioxide | oxygen · hydrogen · methane | Oxygen helps fires burn. · Hydrogen burns. · Methane burns. | Carbon dioxide does not support burning. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which gas is used to fill electric light bulbs?

- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen would make the filament burn._
- ✅ argon
- ◻️ hydrogen  
  _↳ feedback if chosen: Hydrogen is flammable._
- ◻️ chlorine  
  _↳ feedback if chosen: Chlorine is poisonous and reactive._

Full working after a second miss:

> Argon does not react with the hot filament.  
> So the answer is “argon”.  

> Which gas is used to fill electric light bulbs?

- ✅ argon
- ◻️ hydrogen  
  _↳ feedback if chosen: Hydrogen is flammable._
- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen would make the filament burn._
- ◻️ chlorine  
  _↳ feedback if chosen: Chlorine is poisonous and reactive._

Full working after a second miss:

> Argon does not react with the hot filament.  
> So the answer is “argon”.  

> Which gas is used in some fire extinguishers?

- ◻️ hydrogen  
  _↳ feedback if chosen: Hydrogen burns._
- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen helps fires burn._
- ✅ carbon dioxide
- ◻️ methane  
  _↳ feedback if chosen: Methane burns._

Full working after a second miss:

> Carbon dioxide does not support burning.  
> So the answer is “carbon dioxide”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-31-why` · Lesson 31 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Is air an element, a compound or a mixture? | a mixture | a compound · an element · a pure substance | A compound has a fixed formula; air has none. · Air contains several substances. · Air contains several gases. | Air is a mixture of gases. |
| Which observation shows that air is a mixture? | Its composition varies from place to place. | It is invisible. · It has mass. · It can be compressed. | Many pure gases are invisible. · All matter has mass. · All gases can be compressed. | A compound always has the same composition. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which observation shows that air is a mixture?

- ◻️ It can be compressed.  
  _↳ feedback if chosen: All gases can be compressed._
- ◻️ It has mass.  
  _↳ feedback if chosen: All matter has mass._
- ✅ Its composition varies from place to place.
- ◻️ It is invisible.  
  _↳ feedback if chosen: Many pure gases are invisible._

Full working after a second miss:

> A compound always has the same composition.  
> So the answer is “Its composition varies from place to place.”.  

> Is air an element, a compound or a mixture?

- ◻️ a pure substance  
  _↳ feedback if chosen: Air contains several gases._
- ✅ a mixture
- ◻️ an element  
  _↳ feedback if chosen: Air contains several substances._
- ◻️ a compound  
  _↳ feedback if chosen: A compound has a fixed formula; air has none._

Full working after a second miss:

> Air is a mixture of gases.  
> So the answer is “a mixture”.  

> Which observation shows that air is a mixture?

- ◻️ It can be compressed.  
  _↳ feedback if chosen: All gases can be compressed._
- ◻️ It has mass.  
  _↳ feedback if chosen: All matter has mass._
- ◻️ It is invisible.  
  _↳ feedback if chosen: Many pure gases are invisible._
- ✅ Its composition varies from place to place.

Full working after a second miss:

> A compound always has the same composition.  
> So the answer is “Its composition varies from place to place.”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-31-compound` · Lesson 31 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which of these is a compound? | water | air · sea water · soil | Air is a mixture of gases. · Sea water is salt mixed with water. · Soil is a mixture. | Water has a fixed formula, H₂O. |
| Which is true of a compound but not of air? | It has a fixed composition and a formula. | It contains oxygen. · It has mass. · It is a gas. | Air contains oxygen too. · Air has mass too. · Air is a gas too. | Air has no formula; its composition varies. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which of these is a compound?

- ◻️ air  
  _↳ feedback if chosen: Air is a mixture of gases._
- ◻️ sea water  
  _↳ feedback if chosen: Sea water is salt mixed with water._
- ✅ water
- ◻️ soil  
  _↳ feedback if chosen: Soil is a mixture._

Full working after a second miss:

> Water has a fixed formula, H₂O.  
> So the answer is “water”.  

> Which is true of a compound but not of air?

- ◻️ It is a gas.  
  _↳ feedback if chosen: Air is a gas too._
- ✅ It has a fixed composition and a formula.
- ◻️ It contains oxygen.  
  _↳ feedback if chosen: Air contains oxygen too._
- ◻️ It has mass.  
  _↳ feedback if chosen: Air has mass too._

Full working after a second miss:

> Air has no formula; its composition varies.  
> So the answer is “It has a fixed composition and a formula.”.  

> Which is true of a compound but not of air?

- ◻️ It is a gas.  
  _↳ feedback if chosen: Air is a gas too._
- ◻️ It has mass.  
  _↳ feedback if chosen: Air has mass too._
- ✅ It has a fixed composition and a formula.
- ◻️ It contains oxygen.  
  _↳ feedback if chosen: Air contains oxygen too._

Full working after a second miss:

> Air has no formula; its composition varies.  
> So the answer is “It has a fixed composition and a formula.”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-31-props` · Lesson 31 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Air can be made by mixing nitrogen and oxygen. What is observed? | No heat change and no new substance | A flame appears · A precipitate forms · The gases turn brown | No reaction happens. · Nothing reacts. · No new substance is made. | Mixing gases is a physical process. |
| How are the gases of air separated? | by fractional distillation of liquid air | by a chemical reaction only · by filtration · by chromatography | Air is a mixture, so physical methods work. · Filtration separates solids from liquids. · Chromatography separates dyes. | A physical method separates a mixture. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How are the gases of air separated?

- ◻️ by filtration  
  _↳ feedback if chosen: Filtration separates solids from liquids._
- ◻️ by chromatography  
  _↳ feedback if chosen: Chromatography separates dyes._
- ✅ by fractional distillation of liquid air
- ◻️ by a chemical reaction only  
  _↳ feedback if chosen: Air is a mixture, so physical methods work._

Full working after a second miss:

> A physical method separates a mixture.  
> So the answer is “by fractional distillation of liquid air”.  

> Air can be made by mixing nitrogen and oxygen. What is observed?

- ◻️ The gases turn brown  
  _↳ feedback if chosen: No new substance is made._
- ✅ No heat change and no new substance
- ◻️ A flame appears  
  _↳ feedback if chosen: No reaction happens._
- ◻️ A precipitate forms  
  _↳ feedback if chosen: Nothing reacts._

Full working after a second miss:

> Mixing gases is a physical process.  
> So the answer is “No heat change and no new substance”.  

> How are the gases of air separated?

- ◻️ by filtration  
  _↳ feedback if chosen: Filtration separates solids from liquids._
- ◻️ by a chemical reaction only  
  _↳ feedback if chosen: Air is a mixture, so physical methods work._
- ◻️ by chromatography  
  _↳ feedback if chosen: Chromatography separates dyes._
- ✅ by fractional distillation of liquid air

Full working after a second miss:

> A physical method separates a mixture.  
> So the answer is “by fractional distillation of liquid air”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-31-spot` · Lesson 31 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Air has no chemical formula.
- ✅ The parts of air can be separated physically.
- ✅ Water is a compound with a fixed composition.
- ✅ Oxygen in air keeps its own properties.
- ❌ Air is a compound because it always has the same composition.  
  _↳ Air's composition varies; it is a mixture._
- ❌ Liquid air boils at one fixed temperature.  
  _↳ It boils over a range: it is a mixture._
- ❌ Air can only be separated by a chemical reaction.  
  _↳ Air is separated by fractional distillation, a physical method._


Three generated variants:

> Which statement is wrong?

- ◻️ Oxygen in air keeps its own properties.
- ◻️ Water is a compound with a fixed composition.
- ✅ Air can only be separated by a chemical reaction.  
  _↳ explanation: Air is separated by fractional distillation, a physical method._
- ◻️ Air has no chemical formula.

Full working after a second miss:

> The wrong statement is “Air can only be separated by a chemical reaction.”.  
> Air is separated by fractional distillation, a physical method.  

> Which statement is wrong?

- ◻️ Water is a compound with a fixed composition.
- ◻️ Oxygen in air keeps its own properties.
- ◻️ The parts of air can be separated physically.
- ✅ Air can only be separated by a chemical reaction.  
  _↳ explanation: Air is separated by fractional distillation, a physical method._

Full working after a second miss:

> The wrong statement is “Air can only be separated by a chemical reaction.”.  
> Air is separated by fractional distillation, a physical method.  

> Which statement is wrong?

- ◻️ Oxygen in air keeps its own properties.
- ◻️ Air has no chemical formula.
- ✅ Liquid air boils at one fixed temperature.  
  _↳ explanation: It boils over a range: it is a mixture._
- ◻️ Water is a compound with a fixed composition.

Full working after a second miss:

> The wrong statement is “Liquid air boils at one fixed temperature.”.  
> It boils over a range: it is a mixture.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-31-props-card` · Lesson 31 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Air can be made by mixing nitrogen and oxygen. What is observed? | No heat change and no new substance | A flame appears · A precipitate forms · The gases turn brown | No reaction happens. · Nothing reacts. · No new substance is made. | Mixing gases is a physical process. |
| How are the gases of air separated? | by fractional distillation of liquid air | by a chemical reaction only · by filtration · by chromatography | Air is a mixture, so physical methods work. · Filtration separates solids from liquids. · Chromatography separates dyes. | A physical method separates a mixture. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How are the gases of air separated?

- ◻️ by a chemical reaction only  
  _↳ feedback if chosen: Air is a mixture, so physical methods work._
- ✅ by fractional distillation of liquid air
- ◻️ by chromatography  
  _↳ feedback if chosen: Chromatography separates dyes._
- ◻️ by filtration  
  _↳ feedback if chosen: Filtration separates solids from liquids._

Full working after a second miss:

> A physical method separates a mixture.  
> So the answer is “by fractional distillation of liquid air”.  

> How are the gases of air separated?

- ◻️ by filtration  
  _↳ feedback if chosen: Filtration separates solids from liquids._
- ◻️ by chromatography  
  _↳ feedback if chosen: Chromatography separates dyes._
- ✅ by fractional distillation of liquid air
- ◻️ by a chemical reaction only  
  _↳ feedback if chosen: Air is a mixture, so physical methods work._

Full working after a second miss:

> A physical method separates a mixture.  
> So the answer is “by fractional distillation of liquid air”.  

> Air can be made by mixing nitrogen and oxygen. What is observed?

- ✅ No heat change and no new substance
- ◻️ A flame appears  
  _↳ feedback if chosen: No reaction happens._
- ◻️ The gases turn brown  
  _↳ feedback if chosen: No new substance is made._
- ◻️ A precipitate forms  
  _↳ feedback if chosen: Nothing reacts._

Full working after a second miss:

> Mixing gases is a physical process.  
> So the answer is “No heat change and no new substance”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-32-steps` · Lesson 32 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are water vapour and carbon dioxide removed before air is cooled? | They would freeze and block the pipes. | They are poisonous. · They make the air too heavy. · They are needed later. | That is not the reason in the plant. · Their mass is not the problem. · They are removed, not used. | Ice and solid carbon dioxide would block the pipes. |
| What is the first step in separating air? | Filter out the dust. | Boil the air. · Burn the air. · Add water to the air. | Air is already a gas; it is cooled, not boiled. · Burning would use the oxygen. · Water must be removed. | Dust is removed first. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why are water vapour and carbon dioxide removed before air is cooled?

- ✅ They would freeze and block the pipes.
- ◻️ They make the air too heavy.  
  _↳ feedback if chosen: Their mass is not the problem._
- ◻️ They are needed later.  
  _↳ feedback if chosen: They are removed, not used._
- ◻️ They are poisonous.  
  _↳ feedback if chosen: That is not the reason in the plant._

Full working after a second miss:

> Ice and solid carbon dioxide would block the pipes.  
> So the answer is “They would freeze and block the pipes.”.  

> What is the first step in separating air?

- ◻️ Boil the air.  
  _↳ feedback if chosen: Air is already a gas; it is cooled, not boiled._
- ✅ Filter out the dust.
- ◻️ Burn the air.  
  _↳ feedback if chosen: Burning would use the oxygen._
- ◻️ Add water to the air.  
  _↳ feedback if chosen: Water must be removed._

Full working after a second miss:

> Dust is removed first.  
> So the answer is “Filter out the dust.”.  

> What is the first step in separating air?

- ◻️ Boil the air.  
  _↳ feedback if chosen: Air is already a gas; it is cooled, not boiled._
- ◻️ Burn the air.  
  _↳ feedback if chosen: Burning would use the oxygen._
- ◻️ Add water to the air.  
  _↳ feedback if chosen: Water must be removed._
- ✅ Filter out the dust.

Full working after a second miss:

> Dust is removed first.  
> So the answer is “Filter out the dust.”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-32-cool` · Lesson 32 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How is air turned into a liquid? | by compressing and cooling it | by heating it · by filtering it · by adding salt | Heating keeps it a gas. · Filtering only removes dust. · Salt has nothing to do with it. | Compressed and cooled to about −200 °C. |
| What is the name of the method used to separate liquid air? | fractional distillation | filtration · evaporation · chromatography | Filtration separates a solid from a liquid. · Evaporation leaves a solid behind. · Chromatography separates dyes. | Each gas boils off at its own boiling point. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the name of the method used to separate liquid air?

- ◻️ filtration  
  _↳ feedback if chosen: Filtration separates a solid from a liquid._
- ◻️ chromatography  
  _↳ feedback if chosen: Chromatography separates dyes._
- ✅ fractional distillation
- ◻️ evaporation  
  _↳ feedback if chosen: Evaporation leaves a solid behind._

Full working after a second miss:

> Each gas boils off at its own boiling point.  
> So the answer is “fractional distillation”.  

> What is the name of the method used to separate liquid air?

- ◻️ evaporation  
  _↳ feedback if chosen: Evaporation leaves a solid behind._
- ✅ fractional distillation
- ◻️ chromatography  
  _↳ feedback if chosen: Chromatography separates dyes._
- ◻️ filtration  
  _↳ feedback if chosen: Filtration separates a solid from a liquid._

Full working after a second miss:

> Each gas boils off at its own boiling point.  
> So the answer is “fractional distillation”.  

> How is air turned into a liquid?

- ◻️ by filtering it  
  _↳ feedback if chosen: Filtering only removes dust._
- ✅ by compressing and cooling it
- ◻️ by heating it  
  _↳ feedback if chosen: Heating keeps it a gas._
- ◻️ by adding salt  
  _↳ feedback if chosen: Salt has nothing to do with it._

Full working after a second miss:

> Compressed and cooled to about −200 °C.  
> So the answer is “by compressing and cooling it”.  

Sources: air (Composition of dry air by volume (N₂ 78%, O₂ 21%, Ar about 0.9%, CO₂ about 0.04%); the heated-copper gas-syringe experiment; uses of oxygen, nitrogen, argon and carbon dioxide; air as a mixture; fractional distillation of liquid air)

### `k2-33-triangle` · Lesson 33 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which three things are needed for burning? | fuel, oxygen and heat | fuel, water and heat · oxygen, nitrogen and fuel · heat, light and water | Water puts fires out. · Nitrogen does not support burning; heat is needed. · Fuel and oxygen are needed. | The fire triangle. |
| Sand is thrown on a small fire. Which side of the fire triangle is removed? | oxygen | fuel · heat · nitrogen | The fuel is still there under the sand. · Sand mainly cuts off the air. · Nitrogen is not part of the triangle. | Sand stops air reaching the fuel. |
| Water is poured on a burning log. How does this put out the fire? | It cools the fuel below its ignition temperature. | It adds oxygen. · It adds fuel. · It makes the wood lighter. | Water does not add oxygen. · Water is not a fuel. · Mass is not the reason. | Water removes heat. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Sand is thrown on a small fire. Which side of the fire triangle is removed?

- ◻️ nitrogen  
  _↳ feedback if chosen: Nitrogen is not part of the triangle._
- ◻️ heat  
  _↳ feedback if chosen: Sand mainly cuts off the air._
- ◻️ fuel  
  _↳ feedback if chosen: The fuel is still there under the sand._
- ✅ oxygen

Full working after a second miss:

> Sand stops air reaching the fuel.  
> So the answer is “oxygen”.  

> Which three things are needed for burning?

- ◻️ fuel, water and heat  
  _↳ feedback if chosen: Water puts fires out._
- ✅ fuel, oxygen and heat
- ◻️ oxygen, nitrogen and fuel  
  _↳ feedback if chosen: Nitrogen does not support burning; heat is needed._
- ◻️ heat, light and water  
  _↳ feedback if chosen: Fuel and oxygen are needed._

Full working after a second miss:

> The fire triangle.  
> So the answer is “fuel, oxygen and heat”.  

> Which three things are needed for burning?

- ◻️ fuel, water and heat  
  _↳ feedback if chosen: Water puts fires out._
- ✅ fuel, oxygen and heat
- ◻️ oxygen, nitrogen and fuel  
  _↳ feedback if chosen: Nitrogen does not support burning; heat is needed._
- ◻️ heat, light and water  
  _↳ feedback if chosen: Fuel and oxygen are needed._

Full working after a second miss:

> The fire triangle.  
> So the answer is “fuel, oxygen and heat”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-33-products` · Lesson 33 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What are the products when cooking gas burns in plenty of air? | carbon dioxide and water | oxygen and hydrogen · nitrogen and water · carbon and oxygen | Oxygen is used, not made. · Nitrogen is not formed. · Carbon is only formed with too little air. | Fuels with carbon and hydrogen give carbon dioxide and water. |
| Which elements does paper mainly contain? | carbon, hydrogen and oxygen | iron and oxygen · nitrogen only · sodium and chlorine | Paper is not a metal compound. · Paper is mostly cellulose. · That is common salt. | Paper is cellulose: C, H and O. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which elements does paper mainly contain?

- ✅ carbon, hydrogen and oxygen
- ◻️ iron and oxygen  
  _↳ feedback if chosen: Paper is not a metal compound._
- ◻️ sodium and chlorine  
  _↳ feedback if chosen: That is common salt._
- ◻️ nitrogen only  
  _↳ feedback if chosen: Paper is mostly cellulose._

Full working after a second miss:

> Paper is cellulose: C, H and O.  
> So the answer is “carbon, hydrogen and oxygen”.  

> What are the products when cooking gas burns in plenty of air?

- ◻️ carbon and oxygen  
  _↳ feedback if chosen: Carbon is only formed with too little air._
- ✅ carbon dioxide and water
- ◻️ oxygen and hydrogen  
  _↳ feedback if chosen: Oxygen is used, not made._
- ◻️ nitrogen and water  
  _↳ feedback if chosen: Nitrogen is not formed._

Full working after a second miss:

> Fuels with carbon and hydrogen give carbon dioxide and water.  
> So the answer is “carbon dioxide and water”.  

> Which elements does paper mainly contain?

- ◻️ sodium and chlorine  
  _↳ feedback if chosen: That is common salt._
- ◻️ nitrogen only  
  _↳ feedback if chosen: Paper is mostly cellulose._
- ✅ carbon, hydrogen and oxygen
- ◻️ iron and oxygen  
  _↳ feedback if chosen: Paper is not a metal compound._

Full working after a second miss:

> Paper is cellulose: C, H and O.  
> So the answer is “carbon, hydrogen and oxygen”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-33-air` · Lesson 33 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A gas cooker burns with a yellow, smoky flame. What does this show? | There is not enough air. | There is too much air. · The gas is water. · The flame is very clean. | Plenty of air gives a blue flame. · Cooking gas is a fuel. · Smoke shows unburnt carbon. | Too little air gives a yellow, sooty flame. |
| Why is it dangerous to burn charcoal in a closed room? | Poisonous carbon monoxide forms. | It makes too much oxygen. · It makes the room cold. · It makes nitrogen. | Burning uses oxygen. · Burning gives out heat. · Nitrogen is not formed. | With little air, carbon monoxide forms; it can kill. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A gas cooker burns with a yellow, smoky flame. What does this show?

- ◻️ The flame is very clean.  
  _↳ feedback if chosen: Smoke shows unburnt carbon._
- ✅ There is not enough air.
- ◻️ There is too much air.  
  _↳ feedback if chosen: Plenty of air gives a blue flame._
- ◻️ The gas is water.  
  _↳ feedback if chosen: Cooking gas is a fuel._

Full working after a second miss:

> Too little air gives a yellow, sooty flame.  
> So the answer is “There is not enough air.”.  

> Why is it dangerous to burn charcoal in a closed room?

- ✅ Poisonous carbon monoxide forms.
- ◻️ It makes too much oxygen.  
  _↳ feedback if chosen: Burning uses oxygen._
- ◻️ It makes the room cold.  
  _↳ feedback if chosen: Burning gives out heat._
- ◻️ It makes nitrogen.  
  _↳ feedback if chosen: Nitrogen is not formed._

Full working after a second miss:

> With little air, carbon monoxide forms; it can kill.  
> So the answer is “Poisonous carbon monoxide forms.”.  

> A gas cooker burns with a yellow, smoky flame. What does this show?

- ✅ There is not enough air.
- ◻️ The gas is water.  
  _↳ feedback if chosen: Cooking gas is a fuel._
- ◻️ There is too much air.  
  _↳ feedback if chosen: Plenty of air gives a blue flame._
- ◻️ The flame is very clean.  
  _↳ feedback if chosen: Smoke shows unburnt carbon._

Full working after a second miss:

> Too little air gives a yellow, sooty flame.  
> So the answer is “There is not enough air.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-33-spot` · Lesson 33 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Burning gives out heat and light.
- ✅ A blue flame shows there is enough air.
- ✅ Cooking gas burns to carbon dioxide and water.
- ✅ Removing the fuel stops a fire.
- ❌ A fire can burn without oxygen if it is hot enough.  
  _↳ Every fire needs oxygen._
- ❌ Water on a fire adds oxygen and makes it burn faster.  
  _↳ Water cools the fire and puts it out._
- ❌ A yellow smoky flame burns more cleanly than a blue one.  
  _↳ The yellow flame has soot and carbon monoxide._


Three generated variants:

> Which statement is wrong?

- ◻️ Removing the fuel stops a fire.
- ✅ Water on a fire adds oxygen and makes it burn faster.  
  _↳ explanation: Water cools the fire and puts it out._
- ◻️ Cooking gas burns to carbon dioxide and water.
- ◻️ A blue flame shows there is enough air.

Full working after a second miss:

> The wrong statement is “Water on a fire adds oxygen and makes it burn faster.”.  
> Water cools the fire and puts it out.  

> Which statement is wrong?

- ◻️ Removing the fuel stops a fire.
- ◻️ A blue flame shows there is enough air.
- ✅ A fire can burn without oxygen if it is hot enough.  
  _↳ explanation: Every fire needs oxygen._
- ◻️ Cooking gas burns to carbon dioxide and water.

Full working after a second miss:

> The wrong statement is “A fire can burn without oxygen if it is hot enough.”.  
> Every fire needs oxygen.  

> Which statement is wrong?

- ◻️ Removing the fuel stops a fire.
- ◻️ A blue flame shows there is enough air.
- ◻️ Cooking gas burns to carbon dioxide and water.
- ✅ A yellow smoky flame burns more cleanly than a blue one.  
  _↳ explanation: The yellow flame has soot and carbon monoxide._

Full working after a second miss:

> The wrong statement is “A yellow smoky flame burns more cleanly than a blue one.”.  
> The yellow flame has soot and carbon monoxide.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-33-air-card` · Lesson 33 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A gas cooker burns with a yellow, smoky flame. What does this show? | There is not enough air. | There is too much air. · The gas is water. · The flame is very clean. | Plenty of air gives a blue flame. · Cooking gas is a fuel. · Smoke shows unburnt carbon. | Too little air gives a yellow, sooty flame. |
| Why is it dangerous to burn charcoal in a closed room? | Poisonous carbon monoxide forms. | It makes too much oxygen. · It makes the room cold. · It makes nitrogen. | Burning uses oxygen. · Burning gives out heat. · Nitrogen is not formed. | With little air, carbon monoxide forms; it can kill. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is it dangerous to burn charcoal in a closed room?

- ◻️ It makes the room cold.  
  _↳ feedback if chosen: Burning gives out heat._
- ◻️ It makes too much oxygen.  
  _↳ feedback if chosen: Burning uses oxygen._
- ✅ Poisonous carbon monoxide forms.
- ◻️ It makes nitrogen.  
  _↳ feedback if chosen: Nitrogen is not formed._

Full working after a second miss:

> With little air, carbon monoxide forms; it can kill.  
> So the answer is “Poisonous carbon monoxide forms.”.  

> A gas cooker burns with a yellow, smoky flame. What does this show?

- ✅ There is not enough air.
- ◻️ The gas is water.  
  _↳ feedback if chosen: Cooking gas is a fuel._
- ◻️ The flame is very clean.  
  _↳ feedback if chosen: Smoke shows unburnt carbon._
- ◻️ There is too much air.  
  _↳ feedback if chosen: Plenty of air gives a blue flame._

Full working after a second miss:

> Too little air gives a yellow, sooty flame.  
> So the answer is “There is not enough air.”.  

> Why is it dangerous to burn charcoal in a closed room?

- ◻️ It makes nitrogen.  
  _↳ feedback if chosen: Nitrogen is not formed._
- ✅ Poisonous carbon monoxide forms.
- ◻️ It makes the room cold.  
  _↳ feedback if chosen: Burning gives out heat._
- ◻️ It makes too much oxygen.  
  _↳ feedback if chosen: Burning uses oxygen._

Full working after a second miss:

> With little air, carbon monoxide forms; it can kill.  
> So the answer is “Poisonous carbon monoxide forms.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-34-wood` · Lesson 34 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the ash left after wood burns? | the mineral part that does not burn | unburnt carbon · water · pure oxygen | That is soot or smoke. · Water leaves as vapour. · Oxygen is used up. | Ash is the mineral part of the wood. |
| What does black smoke from a wood fire show? | The burning is not complete. | The fire has too much air. · The wood is iron. · The fire is out. | Plenty of air gives little smoke. · Wood is not a metal. · Smoke comes from a burning fire. | Smoke is unburnt carbon. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does black smoke from a wood fire show?

- ◻️ The fire is out.  
  _↳ feedback if chosen: Smoke comes from a burning fire._
- ◻️ The wood is iron.  
  _↳ feedback if chosen: Wood is not a metal._
- ✅ The burning is not complete.
- ◻️ The fire has too much air.  
  _↳ feedback if chosen: Plenty of air gives little smoke._

Full working after a second miss:

> Smoke is unburnt carbon.  
> So the answer is “The burning is not complete.”.  

> What does black smoke from a wood fire show?

- ✅ The burning is not complete.
- ◻️ The fire has too much air.  
  _↳ feedback if chosen: Plenty of air gives little smoke._
- ◻️ The fire is out.  
  _↳ feedback if chosen: Smoke comes from a burning fire._
- ◻️ The wood is iron.  
  _↳ feedback if chosen: Wood is not a metal._

Full working after a second miss:

> Smoke is unburnt carbon.  
> So the answer is “The burning is not complete.”.  

> What is the ash left after wood burns?

- ◻️ pure oxygen  
  _↳ feedback if chosen: Oxygen is used up._
- ◻️ unburnt carbon  
  _↳ feedback if chosen: That is soot or smoke._
- ◻️ water  
  _↳ feedback if chosen: Water leaves as vapour._
- ✅ the mineral part that does not burn

Full working after a second miss:

> Ash is the mineral part of the wood.  
> So the answer is “the mineral part that does not burn”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-34-charcoal` · Lesson 34 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How is charcoal made from wood? | by heating wood with very little air | by burning wood in plenty of air · by soaking wood in water · by drying wood in the sun | Plenty of air turns the wood to ash. · Water does not make charcoal. · Sun-dried wood is still wood. | Little air: the gases leave and carbon stays. |
| Charcoal is nearly pure which element? | carbon | oxygen · iron · sulphur | The oxygen leaves in the gases. · Wood contains no iron to speak of. · Wood has very little sulphur. | Charcoal is carbon. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Charcoal is nearly pure which element?

- ◻️ sulphur  
  _↳ feedback if chosen: Wood has very little sulphur._
- ◻️ iron  
  _↳ feedback if chosen: Wood contains no iron to speak of._
- ◻️ oxygen  
  _↳ feedback if chosen: The oxygen leaves in the gases._
- ✅ carbon

Full working after a second miss:

> Charcoal is carbon.  
> So the answer is “carbon”.  

> How is charcoal made from wood?

- ◻️ by soaking wood in water  
  _↳ feedback if chosen: Water does not make charcoal._
- ◻️ by burning wood in plenty of air  
  _↳ feedback if chosen: Plenty of air turns the wood to ash._
- ✅ by heating wood with very little air
- ◻️ by drying wood in the sun  
  _↳ feedback if chosen: Sun-dried wood is still wood._

Full working after a second miss:

> Little air: the gases leave and carbon stays.  
> So the answer is “by heating wood with very little air”.  

> How is charcoal made from wood?

- ✅ by heating wood with very little air
- ◻️ by burning wood in plenty of air  
  _↳ feedback if chosen: Plenty of air turns the wood to ash._
- ◻️ by soaking wood in water  
  _↳ feedback if chosen: Water does not make charcoal._
- ◻️ by drying wood in the sun  
  _↳ feedback if chosen: Sun-dried wood is still wood._

Full working after a second miss:

> Little air: the gases leave and carbon stays.  
> So the answer is “by heating wood with very little air”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-34-safe` · Lesson 34 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are nylon clothes dangerous near an open fire? | They melt and stick to the skin. | They cannot burn at all. · They give out oxygen. · They are too heavy. | Nylon does burn and melt. · Cloth does not give out oxygen. · Weight is not the danger. | Melting synthetic cloth causes deep burns. |
| A girl's dress catches fire. What should she do? | Stop, drop and roll. | Run to get water. · Fan the flames. · Stand still and wait. | Running gives the flames more air. · Fanning adds air. · The flames keep burning. | Rolling cuts off the oxygen. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A girl's dress catches fire. What should she do?

- ✅ Stop, drop and roll.
- ◻️ Fan the flames.  
  _↳ feedback if chosen: Fanning adds air._
- ◻️ Stand still and wait.  
  _↳ feedback if chosen: The flames keep burning._
- ◻️ Run to get water.  
  _↳ feedback if chosen: Running gives the flames more air._

Full working after a second miss:

> Rolling cuts off the oxygen.  
> So the answer is “Stop, drop and roll.”.  

> A girl's dress catches fire. What should she do?

- ✅ Stop, drop and roll.
- ◻️ Fan the flames.  
  _↳ feedback if chosen: Fanning adds air._
- ◻️ Run to get water.  
  _↳ feedback if chosen: Running gives the flames more air._
- ◻️ Stand still and wait.  
  _↳ feedback if chosen: The flames keep burning._

Full working after a second miss:

> Rolling cuts off the oxygen.  
> So the answer is “Stop, drop and roll.”.  

> Why are nylon clothes dangerous near an open fire?

- ◻️ They cannot burn at all.  
  _↳ feedback if chosen: Nylon does burn and melt._
- ◻️ They give out oxygen.  
  _↳ feedback if chosen: Cloth does not give out oxygen._
- ✅ They melt and stick to the skin.
- ◻️ They are too heavy.  
  _↳ feedback if chosen: Weight is not the danger._

Full working after a second miss:

> Melting synthetic cloth causes deep burns.  
> So the answer is “They melt and stick to the skin.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-34-spot` · Lesson 34 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Wood burns to carbon dioxide and water.
- ✅ Charcoal is made by heating wood with little air.
- ✅ Cotton burns and leaves a soft ash.
- ✅ Rolling on the ground smothers burning clothes.
- ❌ Smoke shows that wood is burning completely.  
  _↳ Smoke is unburnt carbon: the burning is incomplete._
- ❌ Running helps to put out burning clothes.  
  _↳ Running brings more air to the flames._
- ❌ Ash is the carbon of the wood.  
  _↳ The carbon burns away; ash is the mineral part._


Three generated variants:

> Which statement is wrong?

- ◻️ Charcoal is made by heating wood with little air.
- ◻️ Rolling on the ground smothers burning clothes.
- ◻️ Wood burns to carbon dioxide and water.
- ✅ Running helps to put out burning clothes.  
  _↳ explanation: Running brings more air to the flames._

Full working after a second miss:

> The wrong statement is “Running helps to put out burning clothes.”.  
> Running brings more air to the flames.  

> Which statement is wrong?

- ✅ Smoke shows that wood is burning completely.  
  _↳ explanation: Smoke is unburnt carbon: the burning is incomplete._
- ◻️ Cotton burns and leaves a soft ash.
- ◻️ Charcoal is made by heating wood with little air.
- ◻️ Wood burns to carbon dioxide and water.

Full working after a second miss:

> The wrong statement is “Smoke shows that wood is burning completely.”.  
> Smoke is unburnt carbon: the burning is incomplete.  

> Which statement is wrong?

- ◻️ Cotton burns and leaves a soft ash.
- ◻️ Charcoal is made by heating wood with little air.
- ✅ Ash is the carbon of the wood.  
  _↳ explanation: The carbon burns away; ash is the mineral part._
- ◻️ Rolling on the ground smothers burning clothes.

Full working after a second miss:

> The wrong statement is “Ash is the carbon of the wood.”.  
> The carbon burns away; ash is the mineral part.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-34-safe-card` · Lesson 34 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are nylon clothes dangerous near an open fire? | They melt and stick to the skin. | They cannot burn at all. · They give out oxygen. · They are too heavy. | Nylon does burn and melt. · Cloth does not give out oxygen. · Weight is not the danger. | Melting synthetic cloth causes deep burns. |
| A girl's dress catches fire. What should she do? | Stop, drop and roll. | Run to get water. · Fan the flames. · Stand still and wait. | Running gives the flames more air. · Fanning adds air. · The flames keep burning. | Rolling cuts off the oxygen. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A girl's dress catches fire. What should she do?

- ✅ Stop, drop and roll.
- ◻️ Run to get water.  
  _↳ feedback if chosen: Running gives the flames more air._
- ◻️ Fan the flames.  
  _↳ feedback if chosen: Fanning adds air._
- ◻️ Stand still and wait.  
  _↳ feedback if chosen: The flames keep burning._

Full working after a second miss:

> Rolling cuts off the oxygen.  
> So the answer is “Stop, drop and roll.”.  

> A girl's dress catches fire. What should she do?

- ✅ Stop, drop and roll.
- ◻️ Fan the flames.  
  _↳ feedback if chosen: Fanning adds air._
- ◻️ Stand still and wait.  
  _↳ feedback if chosen: The flames keep burning._
- ◻️ Run to get water.  
  _↳ feedback if chosen: Running gives the flames more air._

Full working after a second miss:

> Rolling cuts off the oxygen.  
> So the answer is “Stop, drop and roll.”.  

> Why are nylon clothes dangerous near an open fire?

- ◻️ They cannot burn at all.  
  _↳ feedback if chosen: Nylon does burn and melt._
- ✅ They melt and stick to the skin.
- ◻️ They are too heavy.  
  _↳ feedback if chosen: Weight is not the danger._
- ◻️ They give out oxygen.  
  _↳ feedback if chosen: Cloth does not give out oxygen._

Full working after a second miss:

> Melting synthetic cloth causes deep burns.  
> So the answer is “They melt and stick to the skin.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-35-flame` · Lesson 35 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which element burns with a dazzling white flame? | magnesium | sulphur · copper · carbon | Sulphur burns with a blue flame. · Copper turns black but does not flame. · Carbon glows red. | Magnesium gives a very bright white flame. |
| Which element burns with a blue flame and a choking smell? | sulphur | magnesium · sodium · iron | Magnesium gives a white flame. · Sodium gives a yellow flame. · Iron gives sparks. | Sulphur dioxide has a choking smell. |
| What is formed when carbon burns in plenty of oxygen? | carbon dioxide | carbonate · carbon monoxide only · water | A carbonate also contains a metal. · Carbon monoxide forms only with too little oxygen. · There is no hydrogen. | Carbon + oxygen → carbon dioxide. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is formed when carbon burns in plenty of oxygen?

- ◻️ carbonate  
  _↳ feedback if chosen: A carbonate also contains a metal._
- ◻️ water  
  _↳ feedback if chosen: There is no hydrogen._
- ◻️ carbon monoxide only  
  _↳ feedback if chosen: Carbon monoxide forms only with too little oxygen._
- ✅ carbon dioxide

Full working after a second miss:

> Carbon + oxygen → carbon dioxide.  
> So the answer is “carbon dioxide”.  

> Which element burns with a dazzling white flame?

- ◻️ sulphur  
  _↳ feedback if chosen: Sulphur burns with a blue flame._
- ◻️ copper  
  _↳ feedback if chosen: Copper turns black but does not flame._
- ◻️ carbon  
  _↳ feedback if chosen: Carbon glows red._
- ✅ magnesium

Full working after a second miss:

> Magnesium gives a very bright white flame.  
> So the answer is “magnesium”.  

> Which element burns with a blue flame and a choking smell?

- ✅ sulphur
- ◻️ sodium  
  _↳ feedback if chosen: Sodium gives a yellow flame._
- ◻️ iron  
  _↳ feedback if chosen: Iron gives sparks._
- ◻️ magnesium  
  _↳ feedback if chosen: Magnesium gives a white flame._

Full working after a second miss:

> Sulphur dioxide has a choking smell.  
> So the answer is “sulphur”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-35-spot` · Lesson 35 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Magnesium oxide is a basic oxide.
- ✅ Sulphur dioxide is an acidic oxide.
- ✅ Copper turns black when heated in air.
- ✅ Calcium burns with a brick-red flame.
- ❌ Carbon dioxide dissolves in water to give an alkali.  
  _↳ Carbon dioxide is acidic: it gives a weak acid._
- ❌ Sodium oxide turns blue litmus red.  
  _↳ Sodium oxide is basic: it turns red litmus blue._
- ❌ Non-metals burn to form basic oxides.  
  _↳ Non-metal oxides are acidic._


Three generated variants:

> Which statement is wrong?

- ◻️ Magnesium oxide is a basic oxide.
- ◻️ Copper turns black when heated in air.
- ✅ Sodium oxide turns blue litmus red.  
  _↳ explanation: Sodium oxide is basic: it turns red litmus blue._
- ◻️ Calcium burns with a brick-red flame.

Full working after a second miss:

> The wrong statement is “Sodium oxide turns blue litmus red.”.  
> Sodium oxide is basic: it turns red litmus blue.  

> Which statement is wrong?

- ✅ Sodium oxide turns blue litmus red.  
  _↳ explanation: Sodium oxide is basic: it turns red litmus blue._
- ◻️ Magnesium oxide is a basic oxide.
- ◻️ Sulphur dioxide is an acidic oxide.
- ◻️ Copper turns black when heated in air.

Full working after a second miss:

> The wrong statement is “Sodium oxide turns blue litmus red.”.  
> Sodium oxide is basic: it turns red litmus blue.  

> Which statement is wrong?

- ◻️ Magnesium oxide is a basic oxide.
- ◻️ Sulphur dioxide is an acidic oxide.
- ✅ Sodium oxide turns blue litmus red.  
  _↳ explanation: Sodium oxide is basic: it turns red litmus blue._
- ◻️ Copper turns black when heated in air.

Full working after a second miss:

> The wrong statement is “Sodium oxide turns blue litmus red.”.  
> Sodium oxide is basic: it turns red litmus blue.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-36-def` · Lesson 36 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which metal rusts? | iron | gold · copper · aluminium | Gold does not react with air. · Copper corrodes green but does not rust. · Aluminium corrodes but does not rust. | Only iron and steel rust. |
| What colour is rust? | reddish-brown | green · white · black | Green is corroded copper. · White is the colour of aluminium or zinc oxide. · Black is copper oxide or iron oxide formed by heating. | Rust is reddish-brown. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What colour is rust?

- ✅ reddish-brown
- ◻️ black  
  _↳ feedback if chosen: Black is copper oxide or iron oxide formed by heating._
- ◻️ green  
  _↳ feedback if chosen: Green is corroded copper._
- ◻️ white  
  _↳ feedback if chosen: White is the colour of aluminium or zinc oxide._

Full working after a second miss:

> Rust is reddish-brown.  
> So the answer is “reddish-brown”.  

> What colour is rust?

- ◻️ green  
  _↳ feedback if chosen: Green is corroded copper._
- ◻️ black  
  _↳ feedback if chosen: Black is copper oxide or iron oxide formed by heating._
- ✅ reddish-brown
- ◻️ white  
  _↳ feedback if chosen: White is the colour of aluminium or zinc oxide._

Full working after a second miss:

> Rust is reddish-brown.  
> So the answer is “reddish-brown”.  

> What colour is rust?

- ◻️ green  
  _↳ feedback if chosen: Green is corroded copper._
- ◻️ white  
  _↳ feedback if chosen: White is the colour of aluminium or zinc oxide._
- ✅ reddish-brown
- ◻️ black  
  _↳ feedback if chosen: Black is copper oxide or iron oxide formed by heating._

Full working after a second miss:

> Rust is reddish-brown.  
> So the answer is “reddish-brown”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-36-need` · Lesson 36 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which two things are needed for iron to rust? | oxygen and water | nitrogen and water · oxygen and heat · salt and sunlight | Nitrogen does not cause rusting. · Heat is not needed. · Salt speeds it up but is not needed. | Both air (oxygen) and water. |
| A nail is kept in a dry tube with calcium chloride. Does it rust? | No, there is no water. | Yes, quickly. · Yes, because air is present. · No, there is no nitrogen. | Calcium chloride takes up the water. · Air alone is not enough. · Nitrogen is not needed. | Rusting needs water too. |
| Why is the water boiled in the rusting experiment? | to remove the dissolved air | to kill germs · to add oxygen · to make it salty | Germs do not matter here. · Boiling drives oxygen out. · Boiling does not add salt. | Then the nail has water but no oxygen. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is the water boiled in the rusting experiment?

- ◻️ to add oxygen  
  _↳ feedback if chosen: Boiling drives oxygen out._
- ◻️ to make it salty  
  _↳ feedback if chosen: Boiling does not add salt._
- ◻️ to kill germs  
  _↳ feedback if chosen: Germs do not matter here._
- ✅ to remove the dissolved air

Full working after a second miss:

> Then the nail has water but no oxygen.  
> So the answer is “to remove the dissolved air”.  

> A nail is kept in a dry tube with calcium chloride. Does it rust?

- ✅ No, there is no water.
- ◻️ Yes, because air is present.  
  _↳ feedback if chosen: Air alone is not enough._
- ◻️ No, there is no nitrogen.  
  _↳ feedback if chosen: Nitrogen is not needed._
- ◻️ Yes, quickly.  
  _↳ feedback if chosen: Calcium chloride takes up the water._

Full working after a second miss:

> Rusting needs water too.  
> So the answer is “No, there is no water.”.  

> Why is the water boiled in the rusting experiment?

- ✅ to remove the dissolved air
- ◻️ to add oxygen  
  _↳ feedback if chosen: Boiling drives oxygen out._
- ◻️ to make it salty  
  _↳ feedback if chosen: Boiling does not add salt._
- ◻️ to kill germs  
  _↳ feedback if chosen: Germs do not matter here._

Full working after a second miss:

> Then the nail has water but no oxygen.  
> So the answer is “to remove the dissolved air”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-36-fast` · Lesson 36 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do iron roofs in Limbe rust faster than those in Garoua? | The sea air is wet and salty. | It is colder in Limbe. · There is less oxygen in Limbe. · Limbe has more nitrogen. | Cold slows reactions. · Air everywhere has about the same oxygen. · Nitrogen does not cause rusting. | Water and salt speed up rusting. |
| Which makes rusting faster? | salt water | oil · paint · dry air | Oil keeps air and water out. · Paint protects iron. · Dry air has no water. | Salt speeds up rusting. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which makes rusting faster?

- ◻️ paint  
  _↳ feedback if chosen: Paint protects iron._
- ✅ salt water
- ◻️ oil  
  _↳ feedback if chosen: Oil keeps air and water out._
- ◻️ dry air  
  _↳ feedback if chosen: Dry air has no water._

Full working after a second miss:

> Salt speeds up rusting.  
> So the answer is “salt water”.  

> Which makes rusting faster?

- ◻️ oil  
  _↳ feedback if chosen: Oil keeps air and water out._
- ◻️ paint  
  _↳ feedback if chosen: Paint protects iron._
- ✅ salt water
- ◻️ dry air  
  _↳ feedback if chosen: Dry air has no water._

Full working after a second miss:

> Salt speeds up rusting.  
> So the answer is “salt water”.  

> Why do iron roofs in Limbe rust faster than those in Garoua?

- ✅ The sea air is wet and salty.
- ◻️ It is colder in Limbe.  
  _↳ feedback if chosen: Cold slows reactions._
- ◻️ Limbe has more nitrogen.  
  _↳ feedback if chosen: Nitrogen does not cause rusting._
- ◻️ There is less oxygen in Limbe.  
  _↳ feedback if chosen: Air everywhere has about the same oxygen._

Full working after a second miss:

> Water and salt speed up rusting.  
> So the answer is “The sea air is wet and salty.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-36-spot` · Lesson 36 · spot the error, level 3

Prompt: Which statement about the rusting experiment is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A nail in tap water open to the air rusts.
- ✅ A nail in boiled water under oil does not rust.
- ✅ A nail in dry air does not rust.
- ✅ Rusting needs both oxygen and water.
- ❌ A nail in boiled water under oil rusts because water is present.  
  _↳ There is no oxygen, so it does not rust._
- ❌ A nail in dry air rusts because oxygen is present.  
  _↳ There is no water, so it does not rust._
- ❌ Oil on the water speeds up rusting.  
  _↳ The oil keeps air out._


Three generated variants:

> Which statement about the rusting experiment is wrong?

- ◻️ A nail in dry air does not rust.
- ◻️ Rusting needs both oxygen and water.
- ✅ Oil on the water speeds up rusting.  
  _↳ explanation: The oil keeps air out._
- ◻️ A nail in boiled water under oil does not rust.

Full working after a second miss:

> The wrong statement is “Oil on the water speeds up rusting.”.  
> The oil keeps air out.  

> Which statement about the rusting experiment is wrong?

- ◻️ A nail in tap water open to the air rusts.
- ◻️ A nail in boiled water under oil does not rust.
- ✅ Oil on the water speeds up rusting.  
  _↳ explanation: The oil keeps air out._
- ◻️ Rusting needs both oxygen and water.

Full working after a second miss:

> The wrong statement is “Oil on the water speeds up rusting.”.  
> The oil keeps air out.  

> Which statement about the rusting experiment is wrong?

- ✅ A nail in dry air rusts because oxygen is present.  
  _↳ explanation: There is no water, so it does not rust._
- ◻️ A nail in dry air does not rust.
- ◻️ A nail in boiled water under oil does not rust.
- ◻️ A nail in tap water open to the air rusts.

Full working after a second miss:

> The wrong statement is “A nail in dry air rusts because oxygen is present.”.  
> There is no water, so it does not rust.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-36-fast-card` · Lesson 36 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do iron roofs in Limbe rust faster than those in Garoua? | The sea air is wet and salty. | It is colder in Limbe. · There is less oxygen in Limbe. · Limbe has more nitrogen. | Cold slows reactions. · Air everywhere has about the same oxygen. · Nitrogen does not cause rusting. | Water and salt speed up rusting. |
| Which makes rusting faster? | salt water | oil · paint · dry air | Oil keeps air and water out. · Paint protects iron. · Dry air has no water. | Salt speeds up rusting. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why do iron roofs in Limbe rust faster than those in Garoua?

- ◻️ There is less oxygen in Limbe.  
  _↳ feedback if chosen: Air everywhere has about the same oxygen._
- ✅ The sea air is wet and salty.
- ◻️ It is colder in Limbe.  
  _↳ feedback if chosen: Cold slows reactions._
- ◻️ Limbe has more nitrogen.  
  _↳ feedback if chosen: Nitrogen does not cause rusting._

Full working after a second miss:

> Water and salt speed up rusting.  
> So the answer is “The sea air is wet and salty.”.  

> Which makes rusting faster?

- ◻️ dry air  
  _↳ feedback if chosen: Dry air has no water._
- ◻️ paint  
  _↳ feedback if chosen: Paint protects iron._
- ✅ salt water
- ◻️ oil  
  _↳ feedback if chosen: Oil keeps air and water out._

Full working after a second miss:

> Salt speeds up rusting.  
> So the answer is “salt water”.  

> Why do iron roofs in Limbe rust faster than those in Garoua?

- ◻️ It is colder in Limbe.  
  _↳ feedback if chosen: Cold slows reactions._
- ✅ The sea air is wet and salty.
- ◻️ Limbe has more nitrogen.  
  _↳ feedback if chosen: Nitrogen does not cause rusting._
- ◻️ There is less oxygen in Limbe.  
  _↳ feedback if chosen: Air everywhere has about the same oxygen._

Full working after a second miss:

> Water and salt speed up rusting.  
> So the answer is “The sea air is wet and salty.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-37-comp` · Lesson 37 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the chemical name of rust? | hydrated iron(III) oxide | iron sulphide · copper oxide · iron chloride | There is no sulphur in rust. · Rust is from iron, not copper. · There is no chlorine in rust. | Rust is Fe₂O₃·xH₂O. |
| Which formula is used for rust? | Fe₂O₃·xH₂O | FeS · CuO · Fe | FeS is iron sulphide. · CuO is copper oxide. · Fe is iron itself. | Hydrated iron(III) oxide. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the chemical name of rust?

- ◻️ iron chloride  
  _↳ feedback if chosen: There is no chlorine in rust._
- ✅ hydrated iron(III) oxide
- ◻️ iron sulphide  
  _↳ feedback if chosen: There is no sulphur in rust._
- ◻️ copper oxide  
  _↳ feedback if chosen: Rust is from iron, not copper._

Full working after a second miss:

> Rust is Fe₂O₃·xH₂O.  
> So the answer is “hydrated iron(III) oxide”.  

> Which formula is used for rust?

- ◻️ FeS  
  _↳ feedback if chosen: FeS is iron sulphide._
- ✅ Fe₂O₃·xH₂O
- ◻️ CuO  
  _↳ feedback if chosen: CuO is copper oxide._
- ◻️ Fe  
  _↳ feedback if chosen: Fe is iron itself._

Full working after a second miss:

> Hydrated iron(III) oxide.  
> So the answer is “Fe₂O₃·xH₂O”.  

> Which formula is used for rust?

- ◻️ CuO  
  _↳ feedback if chosen: CuO is copper oxide._
- ✅ Fe₂O₃·xH₂O
- ◻️ FeS  
  _↳ feedback if chosen: FeS is iron sulphide._
- ◻️ Fe  
  _↳ feedback if chosen: Fe is iron itself._

Full working after a second miss:

> Hydrated iron(III) oxide.  
> So the answer is “Fe₂O₃·xH₂O”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-37-flaky` · Lesson 37 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does rusting not stop once a thin layer of rust forms? | Rust is flaky and falls off, exposing fresh iron. | Rust gives out oxygen. · Rust is a catalyst. · Rust is a gas. | Rust does not give out oxygen. · That is not the reason. · Rust is a solid. | Rust does not protect the iron beneath. |
| Why does aluminium not keep corroding like iron? | Its oxide layer sticks and protects it. | It does not react with oxygen at all. · It is heavier than iron. · It is a non-metal. | Aluminium does react, forming a thin oxide. · Weight is not the reason. · Aluminium is a metal. | The aluminium oxide layer does not flake off. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does rusting not stop once a thin layer of rust forms?

- ◻️ Rust is a gas.  
  _↳ feedback if chosen: Rust is a solid._
- ✅ Rust is flaky and falls off, exposing fresh iron.
- ◻️ Rust is a catalyst.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ Rust gives out oxygen.  
  _↳ feedback if chosen: Rust does not give out oxygen._

Full working after a second miss:

> Rust does not protect the iron beneath.  
> So the answer is “Rust is flaky and falls off, exposing fresh iron.”.  

> Why does rusting not stop once a thin layer of rust forms?

- ◻️ Rust gives out oxygen.  
  _↳ feedback if chosen: Rust does not give out oxygen._
- ✅ Rust is flaky and falls off, exposing fresh iron.
- ◻️ Rust is a catalyst.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ Rust is a gas.  
  _↳ feedback if chosen: Rust is a solid._

Full working after a second miss:

> Rust does not protect the iron beneath.  
> So the answer is “Rust is flaky and falls off, exposing fresh iron.”.  

> Why does aluminium not keep corroding like iron?

- ✅ Its oxide layer sticks and protects it.
- ◻️ It does not react with oxygen at all.  
  _↳ feedback if chosen: Aluminium does react, forming a thin oxide._
- ◻️ It is heavier than iron.  
  _↳ feedback if chosen: Weight is not the reason._
- ◻️ It is a non-metal.  
  _↳ feedback if chosen: Aluminium is a metal._

Full working after a second miss:

> The aluminium oxide layer does not flake off.  
> So the answer is “Its oxide layer sticks and protects it.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-37-ox` · Lesson 37 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| When iron rusts, what does it gain? | oxygen | hydrogen · nitrogen · carbon | Rust contains no extra hydrogen gas. · Nitrogen does not react. · There is no carbon in rust. | Gaining oxygen is oxidation. |
| Is rusting a fast or a slow reaction? | slow | fast, like an explosion · it takes a second · it never happens | Explosions are fast reactions. · Rusting takes days to months. · Iron does rust in air and water. | Rusting takes weeks or months. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> When iron rusts, what does it gain?

- ✅ oxygen
- ◻️ nitrogen  
  _↳ feedback if chosen: Nitrogen does not react._
- ◻️ hydrogen  
  _↳ feedback if chosen: Rust contains no extra hydrogen gas._
- ◻️ carbon  
  _↳ feedback if chosen: There is no carbon in rust._

Full working after a second miss:

> Gaining oxygen is oxidation.  
> So the answer is “oxygen”.  

> When iron rusts, what does it gain?

- ◻️ nitrogen  
  _↳ feedback if chosen: Nitrogen does not react._
- ◻️ carbon  
  _↳ feedback if chosen: There is no carbon in rust._
- ◻️ hydrogen  
  _↳ feedback if chosen: Rust contains no extra hydrogen gas._
- ✅ oxygen

Full working after a second miss:

> Gaining oxygen is oxidation.  
> So the answer is “oxygen”.  

> When iron rusts, what does it gain?

- ◻️ hydrogen  
  _↳ feedback if chosen: Rust contains no extra hydrogen gas._
- ◻️ carbon  
  _↳ feedback if chosen: There is no carbon in rust._
- ◻️ nitrogen  
  _↳ feedback if chosen: Nitrogen does not react._
- ✅ oxygen

Full working after a second miss:

> Gaining oxygen is oxidation.  
> So the answer is “oxygen”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-37-spot` · Lesson 37 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Rust is hydrated iron(III) oxide.
- ✅ Rusting is a slow chemical change.
- ✅ Rust is flaky and falls off.
- ✅ Bicycle chains can rust.
- ❌ Rust protects the iron underneath.  
  _↳ Rust flakes off, so the iron keeps rusting._
- ❌ Rusting is a physical change.  
  _↳ Rust is a new substance._
- ❌ Iron loses oxygen when it rusts.  
  _↳ Iron gains oxygen: it is oxidised._


Three generated variants:

> Which statement is wrong?

- ◻️ Rusting is a slow chemical change.
- ◻️ Bicycle chains can rust.
- ✅ Rust protects the iron underneath.  
  _↳ explanation: Rust flakes off, so the iron keeps rusting._
- ◻️ Rust is hydrated iron(III) oxide.

Full working after a second miss:

> The wrong statement is “Rust protects the iron underneath.”.  
> Rust flakes off, so the iron keeps rusting.  

> Which statement is wrong?

- ◻️ Rust is hydrated iron(III) oxide.
- ✅ Iron loses oxygen when it rusts.  
  _↳ explanation: Iron gains oxygen: it is oxidised._
- ◻️ Rust is flaky and falls off.
- ◻️ Rusting is a slow chemical change.

Full working after a second miss:

> The wrong statement is “Iron loses oxygen when it rusts.”.  
> Iron gains oxygen: it is oxidised.  

> Which statement is wrong?

- ◻️ Rusting is a slow chemical change.
- ✅ Rust protects the iron underneath.  
  _↳ explanation: Rust flakes off, so the iron keeps rusting._
- ◻️ Rust is flaky and falls off.
- ◻️ Rust is hydrated iron(III) oxide.

Full working after a second miss:

> The wrong statement is “Rust protects the iron underneath.”.  
> Rust flakes off, so the iron keeps rusting.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-37-flaky-card` · Lesson 37 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does rusting not stop once a thin layer of rust forms? | Rust is flaky and falls off, exposing fresh iron. | Rust gives out oxygen. · Rust is a catalyst. · Rust is a gas. | Rust does not give out oxygen. · That is not the reason. · Rust is a solid. | Rust does not protect the iron beneath. |
| Why does aluminium not keep corroding like iron? | Its oxide layer sticks and protects it. | It does not react with oxygen at all. · It is heavier than iron. · It is a non-metal. | Aluminium does react, forming a thin oxide. · Weight is not the reason. · Aluminium is a metal. | The aluminium oxide layer does not flake off. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does aluminium not keep corroding like iron?

- ✅ Its oxide layer sticks and protects it.
- ◻️ It is a non-metal.  
  _↳ feedback if chosen: Aluminium is a metal._
- ◻️ It does not react with oxygen at all.  
  _↳ feedback if chosen: Aluminium does react, forming a thin oxide._
- ◻️ It is heavier than iron.  
  _↳ feedback if chosen: Weight is not the reason._

Full working after a second miss:

> The aluminium oxide layer does not flake off.  
> So the answer is “Its oxide layer sticks and protects it.”.  

> Why does rusting not stop once a thin layer of rust forms?

- ◻️ Rust gives out oxygen.  
  _↳ feedback if chosen: Rust does not give out oxygen._
- ◻️ Rust is a catalyst.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ Rust is a gas.  
  _↳ feedback if chosen: Rust is a solid._
- ✅ Rust is flaky and falls off, exposing fresh iron.

Full working after a second miss:

> Rust does not protect the iron beneath.  
> So the answer is “Rust is flaky and falls off, exposing fresh iron.”.  

> Why does rusting not stop once a thin layer of rust forms?

- ◻️ Rust gives out oxygen.  
  _↳ feedback if chosen: Rust does not give out oxygen._
- ◻️ Rust is a gas.  
  _↳ feedback if chosen: Rust is a solid._
- ✅ Rust is flaky and falls off, exposing fresh iron.
- ◻️ Rust is a catalyst.  
  _↳ feedback if chosen: That is not the reason._

Full working after a second miss:

> Rust does not protect the iron beneath.  
> So the answer is “Rust is flaky and falls off, exposing fresh iron.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-38-bad` · Lesson 38 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which is a disadvantage of rusting? | It weakens bridges and cars. | It makes iron stronger. · It makes iron shine. · It stops iron from conducting heat. | Rust weakens iron. · Rust is dull and brown. · That is not the main problem. | Rust eats the iron away. |
| Why should a cut from a rusty nail be treated quickly? | It can cause tetanus. | Rust is sweet. · Rust makes blood blue. · Rust is magnetic. | That is not true. · That is not true. · That is not the danger. | Tetanus germs live in soil and on dirty, rusty objects. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why should a cut from a rusty nail be treated quickly?

- ◻️ Rust is sweet.  
  _↳ feedback if chosen: That is not true._
- ◻️ Rust is magnetic.  
  _↳ feedback if chosen: That is not the danger._
- ◻️ Rust makes blood blue.  
  _↳ feedback if chosen: That is not true._
- ✅ It can cause tetanus.

Full working after a second miss:

> Tetanus germs live in soil and on dirty, rusty objects.  
> So the answer is “It can cause tetanus.”.  

> Why should a cut from a rusty nail be treated quickly?

- ◻️ Rust is magnetic.  
  _↳ feedback if chosen: That is not the danger._
- ◻️ Rust is sweet.  
  _↳ feedback if chosen: That is not true._
- ✅ It can cause tetanus.
- ◻️ Rust makes blood blue.  
  _↳ feedback if chosen: That is not true._

Full working after a second miss:

> Tetanus germs live in soil and on dirty, rusty objects.  
> So the answer is “It can cause tetanus.”.  

> Why should a cut from a rusty nail be treated quickly?

- ✅ It can cause tetanus.
- ◻️ Rust makes blood blue.  
  _↳ feedback if chosen: That is not true._
- ◻️ Rust is magnetic.  
  _↳ feedback if chosen: That is not the danger._
- ◻️ Rust is sweet.  
  _↳ feedback if chosen: That is not true._

Full working after a second miss:

> Tetanus germs live in soil and on dirty, rusty objects.  
> So the answer is “It can cause tetanus.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-38-way` · Lesson 38 · multiple choice, level 1

Prompt: Which is the best way to protect {X.q} from rusting?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| a bicycle chain | oiling or greasing | painting · plastic coating · tin plating | Paint would crack as the chain moves. · Plastic would wear off a moving chain. · Plating a chain is costly; oil is used. | Oil keeps out air and water and lets it move. |
| an iron gate | painting | oiling · tin plating · keeping it in water | Oil would be wiped off and collect dust. · Too costly for a gate. · Water causes rusting. | Paint keeps out air and water. |
| a food can | tin plating | greasing · painting the inside · galvanising the inside | Grease would spoil the food. · Paint could poison the food. · Zinc can react with acidic foods. | Tin is not poisonous and does not react with the food. |
| a roofing sheet | galvanising (coating with zinc) | oiling · chromium plating · plastic coating | Rain would wash oil off. · Chromium is too costly for roofs. · Plastic would be damaged by the sun. | Zinc protects the iron even when scratched. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is the best way to protect a food can from rusting?

- ◻️ greasing  
  _↳ feedback if chosen: Grease would spoil the food._
- ✅ tin plating
- ◻️ painting the inside  
  _↳ feedback if chosen: Paint could poison the food._
- ◻️ galvanising the inside  
  _↳ feedback if chosen: Zinc can react with acidic foods._

Full working after a second miss:

> Tin is not poisonous and does not react with the food.  
> So the answer is “tin plating”.  

> Which is the best way to protect a roofing sheet from rusting?

- ◻️ oiling  
  _↳ feedback if chosen: Rain would wash oil off._
- ◻️ plastic coating  
  _↳ feedback if chosen: Plastic would be damaged by the sun._
- ✅ galvanising (coating with zinc)
- ◻️ chromium plating  
  _↳ feedback if chosen: Chromium is too costly for roofs._

Full working after a second miss:

> Zinc protects the iron even when scratched.  
> So the answer is “galvanising (coating with zinc)”.  

> Which is the best way to protect a food can from rusting?

- ◻️ painting the inside  
  _↳ feedback if chosen: Paint could poison the food._
- ◻️ greasing  
  _↳ feedback if chosen: Grease would spoil the food._
- ✅ tin plating
- ◻️ galvanising the inside  
  _↳ feedback if chosen: Zinc can react with acidic foods._

Full working after a second miss:

> Tin is not poisonous and does not react with the food.  
> So the answer is “tin plating”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-38-zinc` · Lesson 38 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does a galvanised sheet not rust even when scratched? | Zinc is more reactive, so it corrodes instead of the iron. | Zinc is a non-metal. · Zinc is less reactive than iron. · Zinc absorbs water. | Zinc is a metal. · Zinc is more reactive than iron. · That is not the reason. | Sacrificial protection by the more reactive zinc. |
| Blocks of magnesium are fixed to the iron hull of a ship. Why? | Magnesium corrodes instead of the iron. | To make the ship heavier · To make the ship float · To paint the ship | Weight is not the reason. · Blocks do not make it float. · They are not paint. | Magnesium is more reactive than iron: sacrificial protection. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does a galvanised sheet not rust even when scratched?

- ◻️ Zinc is a non-metal.  
  _↳ feedback if chosen: Zinc is a metal._
- ◻️ Zinc is less reactive than iron.  
  _↳ feedback if chosen: Zinc is more reactive than iron._
- ◻️ Zinc absorbs water.  
  _↳ feedback if chosen: That is not the reason._
- ✅ Zinc is more reactive, so it corrodes instead of the iron.

Full working after a second miss:

> Sacrificial protection by the more reactive zinc.  
> So the answer is “Zinc is more reactive, so it corrodes instead of the iron.”.  

> Blocks of magnesium are fixed to the iron hull of a ship. Why?

- ◻️ To paint the ship  
  _↳ feedback if chosen: They are not paint._
- ◻️ To make the ship heavier  
  _↳ feedback if chosen: Weight is not the reason._
- ◻️ To make the ship float  
  _↳ feedback if chosen: Blocks do not make it float._
- ✅ Magnesium corrodes instead of the iron.

Full working after a second miss:

> Magnesium is more reactive than iron: sacrificial protection.  
> So the answer is “Magnesium corrodes instead of the iron.”.  

> Blocks of magnesium are fixed to the iron hull of a ship. Why?

- ✅ Magnesium corrodes instead of the iron.
- ◻️ To make the ship float  
  _↳ feedback if chosen: Blocks do not make it float._
- ◻️ To make the ship heavier  
  _↳ feedback if chosen: Weight is not the reason._
- ◻️ To paint the ship  
  _↳ feedback if chosen: They are not paint._

Full working after a second miss:

> Magnesium is more reactive than iron: sacrificial protection.  
> So the answer is “Magnesium corrodes instead of the iron.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-38-spot` · Lesson 38 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Galvanising is coating iron with zinc.
- ✅ Food cans are plated with tin.
- ✅ Greasing protects moving parts.
- ✅ Paint keeps out air and water.
- ❌ Copper blocks protect a ship's hull by corroding instead of the iron.  
  _↳ Copper is less reactive than iron; zinc or magnesium is used._
- ❌ Keeping iron tools in a wet place prevents rusting.  
  _↳ Water causes rusting._
- ❌ Painting is the best protection for a bicycle chain.  
  _↳ Paint cracks on a moving chain; oil it._


Three generated variants:

> Which statement is wrong?

- ✅ Copper blocks protect a ship's hull by corroding instead of the iron.  
  _↳ explanation: Copper is less reactive than iron; zinc or magnesium is used._
- ◻️ Greasing protects moving parts.
- ◻️ Paint keeps out air and water.
- ◻️ Food cans are plated with tin.

Full working after a second miss:

> The wrong statement is “Copper blocks protect a ship's hull by corroding instead of the iron.”.  
> Copper is less reactive than iron; zinc or magnesium is used.  

> Which statement is wrong?

- ◻️ Galvanising is coating iron with zinc.
- ◻️ Greasing protects moving parts.
- ✅ Painting is the best protection for a bicycle chain.  
  _↳ explanation: Paint cracks on a moving chain; oil it._
- ◻️ Paint keeps out air and water.

Full working after a second miss:

> The wrong statement is “Painting is the best protection for a bicycle chain.”.  
> Paint cracks on a moving chain; oil it.  

> Which statement is wrong?

- ◻️ Paint keeps out air and water.
- ◻️ Galvanising is coating iron with zinc.
- ✅ Copper blocks protect a ship's hull by corroding instead of the iron.  
  _↳ explanation: Copper is less reactive than iron; zinc or magnesium is used._
- ◻️ Greasing protects moving parts.

Full working after a second miss:

> The wrong statement is “Copper blocks protect a ship's hull by corroding instead of the iron.”.  
> Copper is less reactive than iron; zinc or magnesium is used.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-38-zinc-card` · Lesson 38 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does a galvanised sheet not rust even when scratched? | Zinc is more reactive, so it corrodes instead of the iron. | Zinc is a non-metal. · Zinc is less reactive than iron. · Zinc absorbs water. | Zinc is a metal. · Zinc is more reactive than iron. · That is not the reason. | Sacrificial protection by the more reactive zinc. |
| Blocks of magnesium are fixed to the iron hull of a ship. Why? | Magnesium corrodes instead of the iron. | To make the ship heavier · To make the ship float · To paint the ship | Weight is not the reason. · Blocks do not make it float. · They are not paint. | Magnesium is more reactive than iron: sacrificial protection. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does a galvanised sheet not rust even when scratched?

- ◻️ Zinc absorbs water.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ Zinc is a non-metal.  
  _↳ feedback if chosen: Zinc is a metal._
- ✅ Zinc is more reactive, so it corrodes instead of the iron.
- ◻️ Zinc is less reactive than iron.  
  _↳ feedback if chosen: Zinc is more reactive than iron._

Full working after a second miss:

> Sacrificial protection by the more reactive zinc.  
> So the answer is “Zinc is more reactive, so it corrodes instead of the iron.”.  

> Blocks of magnesium are fixed to the iron hull of a ship. Why?

- ✅ Magnesium corrodes instead of the iron.
- ◻️ To paint the ship  
  _↳ feedback if chosen: They are not paint._
- ◻️ To make the ship heavier  
  _↳ feedback if chosen: Weight is not the reason._
- ◻️ To make the ship float  
  _↳ feedback if chosen: Blocks do not make it float._

Full working after a second miss:

> Magnesium is more reactive than iron: sacrificial protection.  
> So the answer is “Magnesium corrodes instead of the iron.”.  

> Why does a galvanised sheet not rust even when scratched?

- ◻️ Zinc is a non-metal.  
  _↳ feedback if chosen: Zinc is a metal._
- ◻️ Zinc absorbs water.  
  _↳ feedback if chosen: That is not the reason._
- ✅ Zinc is more reactive, so it corrodes instead of the iron.
- ◻️ Zinc is less reactive than iron.  
  _↳ feedback if chosen: Zinc is more reactive than iron._

Full working after a second miss:

> Sacrificial protection by the more reactive zinc.  
> So the answer is “Zinc is more reactive, so it corrodes instead of the iron.”.  

Sources: burning-rusting (Combustion and the fire triangle; complete and incomplete burning (carbon monoxide); burning of paper, cooking gas, wood and cloth; burning of metals and non-metals, basic and acidic oxides; rusting (conditions, the three-tube experiment, Fe₂O₃·xH₂O) and its prevention (painting, oiling, galvanising, tin and chromium plating, sacrificial protection))

### `k2-40-part` · Lesson 40 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In which state are the particles far apart and moving fast? | gas | solid · liquid · all three | In a solid they only vibrate. · In a liquid they are close together. · Only in a gas are they far apart. | Gas particles are far apart. |
| Which state has a fixed volume but no fixed shape? | liquid | solid · gas · none | A solid has a fixed shape. · A gas has no fixed volume. · A liquid has a fixed volume. | A liquid takes the shape of its container. |
| Which state can be compressed easily? | gas | solid · liquid · none | Solid particles are already close. · Liquid particles are already close. · Gases can be compressed. | Gas particles have spaces between them. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which state can be compressed easily?

- ◻️ solid  
  _↳ feedback if chosen: Solid particles are already close._
- ✅ gas
- ◻️ none  
  _↳ feedback if chosen: Gases can be compressed._
- ◻️ liquid  
  _↳ feedback if chosen: Liquid particles are already close._

Full working after a second miss:

> Gas particles have spaces between them.  
> So the answer is “gas”.  

> Which state can be compressed easily?

- ◻️ solid  
  _↳ feedback if chosen: Solid particles are already close._
- ◻️ liquid  
  _↳ feedback if chosen: Liquid particles are already close._
- ✅ gas
- ◻️ none  
  _↳ feedback if chosen: Gases can be compressed._

Full working after a second miss:

> Gas particles have spaces between them.  
> So the answer is “gas”.  

> In which state are the particles far apart and moving fast?

- ◻️ all three  
  _↳ feedback if chosen: Only in a gas are they far apart._
- ◻️ liquid  
  _↳ feedback if chosen: In a liquid they are close together._
- ✅ gas
- ◻️ solid  
  _↳ feedback if chosen: In a solid they only vibrate._

Full working after a second miss:

> Gas particles are far apart.  
> So the answer is “gas”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-40-change` · Lesson 40 · multiple choice, level 1

Prompt: What is this change of state called? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Water vapour turns to drops on a cold bottle. | condensation | evaporation · melting · sublimation | Evaporation is liquid to gas. · Melting is solid to liquid. · Sublimation is solid to gas. | Gas to liquid is condensation. |
| A camphor ball gets smaller without melting. | sublimation | melting · freezing · condensation | No liquid forms. · Freezing is liquid to solid. · Condensation is gas to liquid. | Solid straight to gas. |
| Palm oil turns solid in the cold harmattan mornings. | freezing (solidification) | melting · boiling · sublimation | Melting is solid to liquid. · Boiling is liquid to gas. · Sublimation is solid to gas. | Liquid to solid. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is this change of state called? Palm oil turns solid in the cold harmattan mornings.

- ✅ freezing (solidification)
- ◻️ boiling  
  _↳ feedback if chosen: Boiling is liquid to gas._
- ◻️ sublimation  
  _↳ feedback if chosen: Sublimation is solid to gas._
- ◻️ melting  
  _↳ feedback if chosen: Melting is solid to liquid._

Full working after a second miss:

> Liquid to solid.  
> So the answer is “freezing (solidification)”.  

> What is this change of state called? Palm oil turns solid in the cold harmattan mornings.

- ◻️ melting  
  _↳ feedback if chosen: Melting is solid to liquid._
- ◻️ boiling  
  _↳ feedback if chosen: Boiling is liquid to gas._
- ◻️ sublimation  
  _↳ feedback if chosen: Sublimation is solid to gas._
- ✅ freezing (solidification)

Full working after a second miss:

> Liquid to solid.  
> So the answer is “freezing (solidification)”.  

> What is this change of state called? Palm oil turns solid in the cold harmattan mornings.

- ◻️ sublimation  
  _↳ feedback if chosen: Sublimation is solid to gas._
- ◻️ boiling  
  _↳ feedback if chosen: Boiling is liquid to gas._
- ✅ freezing (solidification)
- ◻️ melting  
  _↳ feedback if chosen: Melting is solid to liquid._

Full working after a second miss:

> Liquid to solid.  
> So the answer is “freezing (solidification)”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-40-spot` · Lesson 40 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Solid particles vibrate in fixed positions.
- ✅ A liquid takes the shape of its container.
- ✅ Condensation is gas → liquid.
- ✅ A gas fills its container.
- ❌ Water at {50} °C is a gas because it is warm.  
  _↳ {50} °C is below the boiling point ({100} °C): water is liquid._
- ❌ Evaporation is solid → liquid.  
  _↳ That is melting; evaporation is liquid → gas._
- ❌ Gas particles are close together in a regular pattern.  
  _↳ That describes a solid._


Three generated variants:

> Which statement is wrong?

- ✅ Gas particles are close together in a regular pattern.  
  _↳ explanation: That describes a solid._
- ◻️ A liquid takes the shape of its container.
- ◻️ Condensation is gas → liquid.
- ◻️ Solid particles vibrate in fixed positions.

Full working after a second miss:

> The wrong statement is “Gas particles are close together in a regular pattern.”.  
> That describes a solid.  

> Which statement is wrong?

- ◻️ Solid particles vibrate in fixed positions.
- ◻️ Condensation is gas → liquid.
- ✅ Water at 50 °C is a gas because it is warm.  
  _↳ explanation: 50 °C is below the boiling point (100 °C): water is liquid._
- ◻️ A liquid takes the shape of its container.

Full working after a second miss:

> The wrong statement is “Water at 50 °C is a gas because it is warm.”.  
> 50 °C is below the boiling point (100 °C): water is liquid.  

> Which statement is wrong?

- ◻️ Condensation is gas → liquid.
- ◻️ A gas fills its container.
- ✅ Water at 50 °C is a gas because it is warm.  
  _↳ explanation: 50 °C is below the boiling point (100 °C): water is liquid._
- ◻️ Solid particles vibrate in fixed positions.

Full working after a second miss:

> The wrong statement is “Water at 50 °C is a gas because it is warm.”.  
> 50 °C is below the boiling point (100 °C): water is liquid.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-41-filter` · Lesson 41 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Sand and water are filtered. What is the sand on the filter paper called? | the residue | the filtrate · the solvent · the solution | The filtrate is the liquid that passes through. · The solvent is the dissolving liquid. · A solution has a dissolved solid. | The solid left behind is the residue. |
| What is the liquid that passes through the filter paper called? | the filtrate | the residue · the precipitate · the crystal | The residue stays on the paper. · A precipitate is a solid. · Crystals are solid. | The filtrate passes through. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the liquid that passes through the filter paper called?

- ◻️ the residue  
  _↳ feedback if chosen: The residue stays on the paper._
- ✅ the filtrate
- ◻️ the precipitate  
  _↳ feedback if chosen: A precipitate is a solid._
- ◻️ the crystal  
  _↳ feedback if chosen: Crystals are solid._

Full working after a second miss:

> The filtrate passes through.  
> So the answer is “the filtrate”.  

> Sand and water are filtered. What is the sand on the filter paper called?

- ✅ the residue
- ◻️ the solvent  
  _↳ feedback if chosen: The solvent is the dissolving liquid._
- ◻️ the filtrate  
  _↳ feedback if chosen: The filtrate is the liquid that passes through._
- ◻️ the solution  
  _↳ feedback if chosen: A solution has a dissolved solid._

Full working after a second miss:

> The solid left behind is the residue.  
> So the answer is “the residue”.  

> What is the liquid that passes through the filter paper called?

- ✅ the filtrate
- ◻️ the crystal  
  _↳ feedback if chosen: Crystals are solid._
- ◻️ the residue  
  _↳ feedback if chosen: The residue stays on the paper._
- ◻️ the precipitate  
  _↳ feedback if chosen: A precipitate is a solid._

Full working after a second miss:

> The filtrate passes through.  
> So the answer is “the filtrate”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-41-evap` · Lesson 41 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How is salt obtained from salt water? | by evaporation | by filtration · with a magnet · by sieving | Dissolved salt passes through filter paper. · Salt is not magnetic. · Dissolved salt passes through a sieve. | Evaporate the water; the salt is left. |
| Which method gives large, well-shaped crystals of copper sulphate? | crystallisation | evaporation to dryness · filtration · decanting | Heating to dryness gives a powder. · Filtration removes insoluble solids. · Decanting pours off a liquid. | Cool a saturated solution slowly. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How is salt obtained from salt water?

- ◻️ by filtration  
  _↳ feedback if chosen: Dissolved salt passes through filter paper._
- ✅ by evaporation
- ◻️ by sieving  
  _↳ feedback if chosen: Dissolved salt passes through a sieve._
- ◻️ with a magnet  
  _↳ feedback if chosen: Salt is not magnetic._

Full working after a second miss:

> Evaporate the water; the salt is left.  
> So the answer is “by evaporation”.  

> How is salt obtained from salt water?

- ◻️ by sieving  
  _↳ feedback if chosen: Dissolved salt passes through a sieve._
- ✅ by evaporation
- ◻️ with a magnet  
  _↳ feedback if chosen: Salt is not magnetic._
- ◻️ by filtration  
  _↳ feedback if chosen: Dissolved salt passes through filter paper._

Full working after a second miss:

> Evaporate the water; the salt is left.  
> So the answer is “by evaporation”.  

> How is salt obtained from salt water?

- ◻️ by sieving  
  _↳ feedback if chosen: Dissolved salt passes through a sieve._
- ◻️ by filtration  
  _↳ feedback if chosen: Dissolved salt passes through filter paper._
- ✅ by evaporation
- ◻️ with a magnet  
  _↳ feedback if chosen: Salt is not magnetic._

Full working after a second miss:

> Evaporate the water; the salt is left.  
> So the answer is “by evaporation”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-41-method` · Lesson 41 · multiple choice, level 2

Prompt: Which method separates {X.q}?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| iron filings from sulphur powder | a magnet | filtration · evaporation · a separating funnel | Both are insoluble solids. · Neither is dissolved. · That is for two liquids. | Iron is magnetic; sulphur is not. |
| palm oil from water | a separating funnel | filtration · a magnet · sieving | Both liquids pass through filter paper. · Neither is magnetic. · Both liquids pass through a sieve. | Oil and water do not mix: run off the lower layer. |
| chaff from rice grains | winnowing | evaporation · filtration · crystallisation | Nothing is dissolved. · There is no liquid. · There is no solution. | The wind blows away the light chaff. |
| small stones from beans | hand picking | evaporation · a separating funnel · crystallisation | Nothing is dissolved. · There are no liquids. · There is no solution. | Large pieces can be picked out. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which method separates palm oil from water?

- ◻️ filtration  
  _↳ feedback if chosen: Both liquids pass through filter paper._
- ✅ a separating funnel
- ◻️ a magnet  
  _↳ feedback if chosen: Neither is magnetic._
- ◻️ sieving  
  _↳ feedback if chosen: Both liquids pass through a sieve._

Full working after a second miss:

> Oil and water do not mix: run off the lower layer.  
> So the answer is “a separating funnel”.  

> Which method separates palm oil from water?

- ◻️ sieving  
  _↳ feedback if chosen: Both liquids pass through a sieve._
- ✅ a separating funnel
- ◻️ filtration  
  _↳ feedback if chosen: Both liquids pass through filter paper._
- ◻️ a magnet  
  _↳ feedback if chosen: Neither is magnetic._

Full working after a second miss:

> Oil and water do not mix: run off the lower layer.  
> So the answer is “a separating funnel”.  

> Which method separates iron filings from sulphur powder?

- ◻️ evaporation  
  _↳ feedback if chosen: Neither is dissolved._
- ✅ a magnet
- ◻️ a separating funnel  
  _↳ feedback if chosen: That is for two liquids._
- ◻️ filtration  
  _↳ feedback if chosen: Both are insoluble solids._

Full working after a second miss:

> Iron is magnetic; sulphur is not.  
> So the answer is “a magnet”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-41-method-card` · Lesson 41 · multiple choice, level 1

Prompt: Which method separates {X.q}?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| iron filings from sulphur powder | a magnet | filtration · evaporation · a separating funnel | Both are insoluble solids. · Neither is dissolved. · That is for two liquids. | Iron is magnetic; sulphur is not. |
| palm oil from water | a separating funnel | filtration · a magnet · sieving | Both liquids pass through filter paper. · Neither is magnetic. · Both liquids pass through a sieve. | Oil and water do not mix: run off the lower layer. |
| chaff from rice grains | winnowing | evaporation · filtration · crystallisation | Nothing is dissolved. · There is no liquid. · There is no solution. | The wind blows away the light chaff. |
| small stones from beans | hand picking | evaporation · a separating funnel · crystallisation | Nothing is dissolved. · There are no liquids. · There is no solution. | Large pieces can be picked out. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which method separates chaff from rice grains?

- ◻️ evaporation  
  _↳ feedback if chosen: Nothing is dissolved._
- ✅ winnowing
- ◻️ crystallisation  
  _↳ feedback if chosen: There is no solution._
- ◻️ filtration  
  _↳ feedback if chosen: There is no liquid._

Full working after a second miss:

> The wind blows away the light chaff.  
> So the answer is “winnowing”.  

> Which method separates iron filings from sulphur powder?

- ◻️ evaporation  
  _↳ feedback if chosen: Neither is dissolved._
- ◻️ filtration  
  _↳ feedback if chosen: Both are insoluble solids._
- ✅ a magnet
- ◻️ a separating funnel  
  _↳ feedback if chosen: That is for two liquids._

Full working after a second miss:

> Iron is magnetic; sulphur is not.  
> So the answer is “a magnet”.  

> Which method separates small stones from beans?

- ◻️ a separating funnel  
  _↳ feedback if chosen: There are no liquids._
- ◻️ crystallisation  
  _↳ feedback if chosen: There is no solution._
- ✅ hand picking
- ◻️ evaporation  
  _↳ feedback if chosen: Nothing is dissolved._

Full working after a second miss:

> Large pieces can be picked out.  
> So the answer is “hand picking”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-42-simple` · Lesson 42 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which method gives pure water from salt water? | simple distillation | filtration · evaporation · decanting | Salt passes through filter paper. · Evaporation loses the water. · Decanting does not remove dissolved salt. | Boil, then condense the steam. |
| In simple distillation of salt water, where is the salt at the end? | in the flask | in the receiver · in the condenser · in the air | Only the water reaches the receiver. · Only vapour passes through. · Salt does not evaporate. | The salt stays behind. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In simple distillation of salt water, where is the salt at the end?

- ◻️ in the air  
  _↳ feedback if chosen: Salt does not evaporate._
- ◻️ in the condenser  
  _↳ feedback if chosen: Only vapour passes through._
- ✅ in the flask
- ◻️ in the receiver  
  _↳ feedback if chosen: Only the water reaches the receiver._

Full working after a second miss:

> The salt stays behind.  
> So the answer is “in the flask”.  

> In simple distillation of salt water, where is the salt at the end?

- ◻️ in the air  
  _↳ feedback if chosen: Salt does not evaporate._
- ◻️ in the condenser  
  _↳ feedback if chosen: Only vapour passes through._
- ◻️ in the receiver  
  _↳ feedback if chosen: Only the water reaches the receiver._
- ✅ in the flask

Full working after a second miss:

> The salt stays behind.  
> So the answer is “in the flask”.  

> Which method gives pure water from salt water?

- ◻️ decanting  
  _↳ feedback if chosen: Decanting does not remove dissolved salt._
- ◻️ filtration  
  _↳ feedback if chosen: Salt passes through filter paper._
- ◻️ evaporation  
  _↳ feedback if chosen: Evaporation loses the water._
- ✅ simple distillation

Full working after a second miss:

> Boil, then condense the steam.  
> So the answer is “simple distillation”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-42-parts` · Lesson 42 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the liquid collected in distillation called? | the distillate | the residue · the filtrate · the solute | The residue stays in the flask or filter. · The filtrate comes from filtering. · The solute is the dissolved solid. | The condensed liquid is the distillate. |
| Where does the cold water enter the condenser? | at the bottom | at the top · in the flask · in the receiver | Entering at the bottom fills the jacket completely. · The flask holds the solution. · The receiver collects the distillate. | In at the bottom, out at the top. |
| Where should the thermometer bulb be in distillation? | at the side arm of the flask | in the liquid at the bottom · in the receiver · in the cooling water | It must read the vapour temperature. · The receiver is cold. · That only shows the cooling water. | It reads the temperature of the vapour leaving. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the liquid collected in distillation called?

- ◻️ the solute  
  _↳ feedback if chosen: The solute is the dissolved solid._
- ◻️ the filtrate  
  _↳ feedback if chosen: The filtrate comes from filtering._
- ✅ the distillate
- ◻️ the residue  
  _↳ feedback if chosen: The residue stays in the flask or filter._

Full working after a second miss:

> The condensed liquid is the distillate.  
> So the answer is “the distillate”.  

> What is the liquid collected in distillation called?

- ✅ the distillate
- ◻️ the residue  
  _↳ feedback if chosen: The residue stays in the flask or filter._
- ◻️ the solute  
  _↳ feedback if chosen: The solute is the dissolved solid._
- ◻️ the filtrate  
  _↳ feedback if chosen: The filtrate comes from filtering._

Full working after a second miss:

> The condensed liquid is the distillate.  
> So the answer is “the distillate”.  

> Where should the thermometer bulb be in distillation?

- ◻️ in the cooling water  
  _↳ feedback if chosen: That only shows the cooling water._
- ✅ at the side arm of the flask
- ◻️ in the receiver  
  _↳ feedback if chosen: The receiver is cold._
- ◻️ in the liquid at the bottom  
  _↳ feedback if chosen: It must read the vapour temperature._

Full working after a second miss:

> It reads the temperature of the vapour leaving.  
> So the answer is “at the side arm of the flask”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-42-spot` · Lesson 42 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Distilled water is made by simple distillation.
- ✅ Crude oil is separated by fractional distillation.
- ✅ The distillate is collected in the receiver.
- ✅ The liquid with the lower boiling point distils first.
- ❌ Cold water enters the condenser at the top.  
  _↳ It enters at the bottom so the jacket fills._
- ❌ Filtration gives pure water from salt water.  
  _↳ The dissolved salt passes through the filter._
- ❌ The thermometer bulb is put in the boiling liquid.  
  _↳ It is placed at the side arm to read the vapour temperature._


Three generated variants:

> Which statement is wrong?

- ✅ Filtration gives pure water from salt water.  
  _↳ explanation: The dissolved salt passes through the filter._
- ◻️ Crude oil is separated by fractional distillation.
- ◻️ Distilled water is made by simple distillation.
- ◻️ The distillate is collected in the receiver.

Full working after a second miss:

> The wrong statement is “Filtration gives pure water from salt water.”.  
> The dissolved salt passes through the filter.  

> Which statement is wrong?

- ✅ The thermometer bulb is put in the boiling liquid.  
  _↳ explanation: It is placed at the side arm to read the vapour temperature._
- ◻️ Crude oil is separated by fractional distillation.
- ◻️ Distilled water is made by simple distillation.
- ◻️ The liquid with the lower boiling point distils first.

Full working after a second miss:

> The wrong statement is “The thermometer bulb is put in the boiling liquid.”.  
> It is placed at the side arm to read the vapour temperature.  

> Which statement is wrong?

- ◻️ Distilled water is made by simple distillation.
- ✅ The thermometer bulb is put in the boiling liquid.  
  _↳ explanation: It is placed at the side arm to read the vapour temperature._
- ◻️ The distillate is collected in the receiver.
- ◻️ The liquid with the lower boiling point distils first.

Full working after a second miss:

> The wrong statement is “The thermometer bulb is put in the boiling liquid.”.  
> It is placed at the side arm to read the vapour temperature.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-43-use` · Lesson 43 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which mixture is best separated by chromatography? | the dyes in black ink | sand and water · iron and sulphur · oil and water | Use filtration. · Use a magnet. · Use a separating funnel. | Chromatography separates dissolved dyes. |
| In paper chromatography, which dye moves furthest? | the most soluble one | the least soluble one · the heaviest one · the darkest one | It stays nearer the start. · Mass is not what decides. · Colour is not what decides. | The solvent carries the most soluble dye furthest. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which mixture is best separated by chromatography?

- ◻️ sand and water  
  _↳ feedback if chosen: Use filtration._
- ◻️ oil and water  
  _↳ feedback if chosen: Use a separating funnel._
- ✅ the dyes in black ink
- ◻️ iron and sulphur  
  _↳ feedback if chosen: Use a magnet._

Full working after a second miss:

> Chromatography separates dissolved dyes.  
> So the answer is “the dyes in black ink”.  

> In paper chromatography, which dye moves furthest?

- ◻️ the heaviest one  
  _↳ feedback if chosen: Mass is not what decides._
- ✅ the most soluble one
- ◻️ the darkest one  
  _↳ feedback if chosen: Colour is not what decides._
- ◻️ the least soluble one  
  _↳ feedback if chosen: It stays nearer the start._

Full working after a second miss:

> The solvent carries the most soluble dye furthest.  
> So the answer is “the most soluble one”.  

> Which mixture is best separated by chromatography?

- ◻️ oil and water  
  _↳ feedback if chosen: Use a separating funnel._
- ✅ the dyes in black ink
- ◻️ iron and sulphur  
  _↳ feedback if chosen: Use a magnet._
- ◻️ sand and water  
  _↳ feedback if chosen: Use filtration._

Full working after a second miss:

> Chromatography separates dissolved dyes.  
> So the answer is “the dyes in black ink”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-43-setup` · Lesson 43 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is the start line drawn in pencil? | Pencil does not dissolve in the solvent. | Pencil is cheaper. · Pencil is darker. · Ink is not allowed in school. | Cost is not the reason. · Darkness is not the reason. · That is not the reason. | Ink would run and mix with the dyes. |
| Why must the spot be above the level of the solvent? | Otherwise the dyes would dissolve into the solvent. | To keep it dry for ever · So that it moves faster · To make it darker | The solvent must reach it by rising. · That is not why. · That is not why. | The dyes must be carried up, not washed away. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why must the spot be above the level of the solvent?

- ◻️ To keep it dry for ever  
  _↳ feedback if chosen: The solvent must reach it by rising._
- ◻️ So that it moves faster  
  _↳ feedback if chosen: That is not why._
- ◻️ To make it darker  
  _↳ feedback if chosen: That is not why._
- ✅ Otherwise the dyes would dissolve into the solvent.

Full working after a second miss:

> The dyes must be carried up, not washed away.  
> So the answer is “Otherwise the dyes would dissolve into the solvent.”.  

> Why must the spot be above the level of the solvent?

- ✅ Otherwise the dyes would dissolve into the solvent.
- ◻️ To make it darker  
  _↳ feedback if chosen: That is not why._
- ◻️ To keep it dry for ever  
  _↳ feedback if chosen: The solvent must reach it by rising._
- ◻️ So that it moves faster  
  _↳ feedback if chosen: That is not why._

Full working after a second miss:

> The dyes must be carried up, not washed away.  
> So the answer is “Otherwise the dyes would dissolve into the solvent.”.  

> Why must the spot be above the level of the solvent?

- ✅ Otherwise the dyes would dissolve into the solvent.
- ◻️ To make it darker  
  _↳ feedback if chosen: That is not why._
- ◻️ To keep it dry for ever  
  _↳ feedback if chosen: The solvent must reach it by rising._
- ◻️ So that it moves faster  
  _↳ feedback if chosen: That is not why._

Full working after a second miss:

> The dyes must be carried up, not washed away.  
> So the answer is “Otherwise the dyes would dissolve into the solvent.”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-44-points` · Lesson 44 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the melting point of a substance? | the temperature at which the solid turns to liquid | the temperature at which the liquid turns to gas · the temperature at which a gas turns to liquid · the highest temperature it can reach | That is the boiling point. · That is condensation. · That is not a definition. | Solid → liquid. |
| At what temperature does pure water boil at sea level? | 100 °C | 0 °C · 37 °C · 78 °C | 0 °C is its melting point. · 37 °C is body temperature. · 78 °C is the boiling point of ethanol. | Pure water boils at 100 °C. |
| Why does water boil below 100 °C on top of Mount Cameroon? | The air pressure is lower. | It is hotter there. · The water is salty. · There is more oxygen. | It is colder there. · Salt would raise the boiling point. · There is less air, not more oxygen. | Lower pressure, lower boiling point. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the melting point of a substance?

- ✅ the temperature at which the solid turns to liquid
- ◻️ the temperature at which a gas turns to liquid  
  _↳ feedback if chosen: That is condensation._
- ◻️ the temperature at which the liquid turns to gas  
  _↳ feedback if chosen: That is the boiling point._
- ◻️ the highest temperature it can reach  
  _↳ feedback if chosen: That is not a definition._

Full working after a second miss:

> Solid → liquid.  
> So the answer is “the temperature at which the solid turns to liquid”.  

> At what temperature does pure water boil at sea level?

- ✅ 100 °C
- ◻️ 78 °C  
  _↳ feedback if chosen: 78 °C is the boiling point of ethanol._
- ◻️ 37 °C  
  _↳ feedback if chosen: 37 °C is body temperature._
- ◻️ 0 °C  
  _↳ feedback if chosen: 0 °C is its melting point._

Full working after a second miss:

> Pure water boils at 100 °C.  
> So the answer is “100 °C”.  

> Why does water boil below 100 °C on top of Mount Cameroon?

- ◻️ It is hotter there.  
  _↳ feedback if chosen: It is colder there._
- ✅ The air pressure is lower.
- ◻️ The water is salty.  
  _↳ feedback if chosen: Salt would raise the boiling point._
- ◻️ There is more oxygen.  
  _↳ feedback if chosen: There is less air, not more oxygen._

Full working after a second miss:

> Lower pressure, lower boiling point.  
> So the answer is “The air pressure is lower.”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-44-sub` · Lesson 44 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which substance sublimes when heated? | iodine | common salt · sand · sugar | Salt melts at a high temperature. · Sand does not sublime. · Sugar melts and burns. | Iodine turns straight to a purple vapour. |
| What is sublimation? | a solid turning directly into a gas | a liquid turning into a gas · a gas turning into a liquid · a solid turning into a liquid | That is evaporation or boiling. · That is condensation. · That is melting. | No liquid is formed. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is sublimation?

- ◻️ a liquid turning into a gas  
  _↳ feedback if chosen: That is evaporation or boiling._
- ◻️ a solid turning into a liquid  
  _↳ feedback if chosen: That is melting._
- ◻️ a gas turning into a liquid  
  _↳ feedback if chosen: That is condensation._
- ✅ a solid turning directly into a gas

Full working after a second miss:

> No liquid is formed.  
> So the answer is “a solid turning directly into a gas”.  

> Which substance sublimes when heated?

- ◻️ sugar  
  _↳ feedback if chosen: Sugar melts and burns._
- ◻️ sand  
  _↳ feedback if chosen: Sand does not sublime._
- ◻️ common salt  
  _↳ feedback if chosen: Salt melts at a high temperature._
- ✅ iodine

Full working after a second miss:

> Iodine turns straight to a purple vapour.  
> So the answer is “iodine”.  

> What is sublimation?

- ◻️ a solid turning into a liquid  
  _↳ feedback if chosen: That is melting._
- ◻️ a liquid turning into a gas  
  _↳ feedback if chosen: That is evaporation or boiling._
- ✅ a solid turning directly into a gas
- ◻️ a gas turning into a liquid  
  _↳ feedback if chosen: That is condensation._

Full working after a second miss:

> No liquid is formed.  
> So the answer is “a solid turning directly into a gas”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-44-sep` · Lesson 44 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How is ammonium chloride separated from salt? | by sublimation | by filtration · by a magnet · by distillation | Both dissolve in water. · Neither is magnetic. · Neither is a liquid. | Ammonium chloride sublimes; salt does not. |
| When a mixture of iodine and sand is heated under a cold funnel, where does the iodine collect? | on the cold funnel | at the bottom with the sand · in the air only · in the flame | The iodine leaves the sand as vapour. · The vapour turns back to solid on the cold surface. · It does not collect in the flame. | The vapour sublimes back to solid on cooling. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> When a mixture of iodine and sand is heated under a cold funnel, where does the iodine collect?

- ✅ on the cold funnel
- ◻️ at the bottom with the sand  
  _↳ feedback if chosen: The iodine leaves the sand as vapour._
- ◻️ in the air only  
  _↳ feedback if chosen: The vapour turns back to solid on the cold surface._
- ◻️ in the flame  
  _↳ feedback if chosen: It does not collect in the flame._

Full working after a second miss:

> The vapour sublimes back to solid on cooling.  
> So the answer is “on the cold funnel”.  

> When a mixture of iodine and sand is heated under a cold funnel, where does the iodine collect?

- ✅ on the cold funnel
- ◻️ at the bottom with the sand  
  _↳ feedback if chosen: The iodine leaves the sand as vapour._
- ◻️ in the air only  
  _↳ feedback if chosen: The vapour turns back to solid on the cold surface._
- ◻️ in the flame  
  _↳ feedback if chosen: It does not collect in the flame._

Full working after a second miss:

> The vapour sublimes back to solid on cooling.  
> So the answer is “on the cold funnel”.  

> When a mixture of iodine and sand is heated under a cold funnel, where does the iodine collect?

- ✅ on the cold funnel
- ◻️ in the air only  
  _↳ feedback if chosen: The vapour turns back to solid on the cold surface._
- ◻️ in the flame  
  _↳ feedback if chosen: It does not collect in the flame._
- ◻️ at the bottom with the sand  
  _↳ feedback if chosen: The iodine leaves the sand as vapour._

Full working after a second miss:

> The vapour sublimes back to solid on cooling.  
> So the answer is “on the cold funnel”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-44-sep-card` · Lesson 44 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How is ammonium chloride separated from salt? | by sublimation | by filtration · by a magnet · by distillation | Both dissolve in water. · Neither is magnetic. · Neither is a liquid. | Ammonium chloride sublimes; salt does not. |
| When a mixture of iodine and sand is heated under a cold funnel, where does the iodine collect? | on the cold funnel | at the bottom with the sand · in the air only · in the flame | The iodine leaves the sand as vapour. · The vapour turns back to solid on the cold surface. · It does not collect in the flame. | The vapour sublimes back to solid on cooling. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How is ammonium chloride separated from salt?

- ✅ by sublimation
- ◻️ by filtration  
  _↳ feedback if chosen: Both dissolve in water._
- ◻️ by distillation  
  _↳ feedback if chosen: Neither is a liquid._
- ◻️ by a magnet  
  _↳ feedback if chosen: Neither is magnetic._

Full working after a second miss:

> Ammonium chloride sublimes; salt does not.  
> So the answer is “by sublimation”.  

> How is ammonium chloride separated from salt?

- ✅ by sublimation
- ◻️ by a magnet  
  _↳ feedback if chosen: Neither is magnetic._
- ◻️ by distillation  
  _↳ feedback if chosen: Neither is a liquid._
- ◻️ by filtration  
  _↳ feedback if chosen: Both dissolve in water._

Full working after a second miss:

> Ammonium chloride sublimes; salt does not.  
> So the answer is “by sublimation”.  

> When a mixture of iodine and sand is heated under a cold funnel, where does the iodine collect?

- ◻️ in the air only  
  _↳ feedback if chosen: The vapour turns back to solid on the cold surface._
- ✅ on the cold funnel
- ◻️ in the flame  
  _↳ feedback if chosen: It does not collect in the flame._
- ◻️ at the bottom with the sand  
  _↳ feedback if chosen: The iodine leaves the sand as vapour._

Full working after a second miss:

> The vapour sublimes back to solid on cooling.  
> So the answer is “on the cold funnel”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-45-pure` · Lesson 45 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How does a pure solid melt? | at one sharp, fixed temperature | over a wide range of temperatures · at any temperature · only in sunlight | That shows an impure solid. · It has a fixed melting point. · Light does not decide it. | A sharp melting point shows purity. |
| A liquid boils at exactly 100 °C at sea level. What is it likely to be? | pure water | salt water · sugar solution · palm oil | Salt water boils above 100 °C. · A sugar solution boils above 100 °C. · Palm oil does not boil at 100 °C. | Pure water boils at 100 °C. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A liquid boils at exactly 100 °C at sea level. What is it likely to be?

- ◻️ palm oil  
  _↳ feedback if chosen: Palm oil does not boil at 100 °C._
- ◻️ salt water  
  _↳ feedback if chosen: Salt water boils above 100 °C._
- ◻️ sugar solution  
  _↳ feedback if chosen: A sugar solution boils above 100 °C._
- ✅ pure water

Full working after a second miss:

> Pure water boils at 100 °C.  
> So the answer is “pure water”.  

> How does a pure solid melt?

- ◻️ only in sunlight  
  _↳ feedback if chosen: Light does not decide it._
- ✅ at one sharp, fixed temperature
- ◻️ over a wide range of temperatures  
  _↳ feedback if chosen: That shows an impure solid._
- ◻️ at any temperature  
  _↳ feedback if chosen: It has a fixed melting point._

Full working after a second miss:

> A sharp melting point shows purity.  
> So the answer is “at one sharp, fixed temperature”.  

> A liquid boils at exactly 100 °C at sea level. What is it likely to be?

- ◻️ palm oil  
  _↳ feedback if chosen: Palm oil does not boil at 100 °C._
- ◻️ salt water  
  _↳ feedback if chosen: Salt water boils above 100 °C._
- ◻️ sugar solution  
  _↳ feedback if chosen: A sugar solution boils above 100 °C._
- ✅ pure water

Full working after a second miss:

> Pure water boils at 100 °C.  
> So the answer is “pure water”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-45-imp` · Lesson 45 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What happens to the boiling point of water when salt is dissolved in it? | It rises above 100 °C. | It falls below 100 °C. · It stays at 100 °C. · The water cannot boil. | Impurities raise the boiling point. · Impurities change it. · Salt water does boil. | Dissolved impurities raise the boiling point. |
| A solid melts slowly between 75 °C and 79 °C. Its true melting point is 80 °C. What does this show? | It is impure. | It is pure. · It is a gas. · It is a liquid. | A pure solid melts sharply at 80 °C. · It is a solid that melts. · It is a solid before it melts. | Impurities lower the melting point and give a range. |
| Why is salt put on icy roads in cold countries? | It lowers the freezing point, so the ice melts. | It raises the freezing point. · It makes the road dry by magic. · It adds heat. | Salt lowers the freezing point. · That is not science. · Salt does not give out heat here. | Impurities lower the freezing point. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What happens to the boiling point of water when salt is dissolved in it?

- ✅ It rises above 100 °C.
- ◻️ It stays at 100 °C.  
  _↳ feedback if chosen: Impurities change it._
- ◻️ It falls below 100 °C.  
  _↳ feedback if chosen: Impurities raise the boiling point._
- ◻️ The water cannot boil.  
  _↳ feedback if chosen: Salt water does boil._

Full working after a second miss:

> Dissolved impurities raise the boiling point.  
> So the answer is “It rises above 100 °C.”.  

> A solid melts slowly between 75 °C and 79 °C. Its true melting point is 80 °C. What does this show?

- ✅ It is impure.
- ◻️ It is a gas.  
  _↳ feedback if chosen: It is a solid that melts._
- ◻️ It is pure.  
  _↳ feedback if chosen: A pure solid melts sharply at 80 °C._
- ◻️ It is a liquid.  
  _↳ feedback if chosen: It is a solid before it melts._

Full working after a second miss:

> Impurities lower the melting point and give a range.  
> So the answer is “It is impure.”.  

> What happens to the boiling point of water when salt is dissolved in it?

- ◻️ The water cannot boil.  
  _↳ feedback if chosen: Salt water does boil._
- ◻️ It falls below 100 °C.  
  _↳ feedback if chosen: Impurities raise the boiling point._
- ◻️ It stays at 100 °C.  
  _↳ feedback if chosen: Impurities change it._
- ✅ It rises above 100 °C.

Full working after a second miss:

> Dissolved impurities raise the boiling point.  
> So the answer is “It rises above 100 °C.”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-45-spot` · Lesson 45 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A food colour gives three spots on a chromatogram. What does this show? | It is a mixture of at least three dyes. | It is a pure dye. · It is a gas. · The paper is dirty. | A pure dye gives one spot. · It is a dye solution. · That is not the likely reason. | Each spot is a different substance. |
| A sample gives one spot in chromatography and melts sharply at its known melting point. What can you say? | It is very likely pure. | It is a mixture. · It is impure. · It is a solution. | A mixture gives several spots and a range. · Both tests show purity. · It melts as a solid. | Both purity tests agree. |
| Why must medicines be pure? | Impurities can be harmful to the body. | Pure substances are cheaper. · Impurities make them taste sweet. · Pure substances are always liquids. | Purification costs more. · That is not the reason. · Many pure medicines are solids. | Impure medicines can poison or fail to work. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why must medicines be pure?

- ◻️ Impurities make them taste sweet.  
  _↳ feedback if chosen: That is not the reason._
- ✅ Impurities can be harmful to the body.
- ◻️ Pure substances are cheaper.  
  _↳ feedback if chosen: Purification costs more._
- ◻️ Pure substances are always liquids.  
  _↳ feedback if chosen: Many pure medicines are solids._

Full working after a second miss:

> Impure medicines can poison or fail to work.  
> So the answer is “Impurities can be harmful to the body.”.  

> A food colour gives three spots on a chromatogram. What does this show?

- ◻️ The paper is dirty.  
  _↳ feedback if chosen: That is not the likely reason._
- ✅ It is a mixture of at least three dyes.
- ◻️ It is a gas.  
  _↳ feedback if chosen: It is a dye solution._
- ◻️ It is a pure dye.  
  _↳ feedback if chosen: A pure dye gives one spot._

Full working after a second miss:

> Each spot is a different substance.  
> So the answer is “It is a mixture of at least three dyes.”.  

> A sample gives one spot in chromatography and melts sharply at its known melting point. What can you say?

- ✅ It is very likely pure.
- ◻️ It is a mixture.  
  _↳ feedback if chosen: A mixture gives several spots and a range._
- ◻️ It is a solution.  
  _↳ feedback if chosen: It melts as a solid._
- ◻️ It is impure.  
  _↳ feedback if chosen: Both tests show purity._

Full working after a second miss:

> Both purity tests agree.  
> So the answer is “It is very likely pure.”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-45-imp-card` · Lesson 45 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What happens to the boiling point of water when salt is dissolved in it? | It rises above 100 °C. | It falls below 100 °C. · It stays at 100 °C. · The water cannot boil. | Impurities raise the boiling point. · Impurities change it. · Salt water does boil. | Dissolved impurities raise the boiling point. |
| A solid melts slowly between 75 °C and 79 °C. Its true melting point is 80 °C. What does this show? | It is impure. | It is pure. · It is a gas. · It is a liquid. | A pure solid melts sharply at 80 °C. · It is a solid that melts. · It is a solid before it melts. | Impurities lower the melting point and give a range. |
| Why is salt put on icy roads in cold countries? | It lowers the freezing point, so the ice melts. | It raises the freezing point. · It makes the road dry by magic. · It adds heat. | Salt lowers the freezing point. · That is not science. · Salt does not give out heat here. | Impurities lower the freezing point. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What happens to the boiling point of water when salt is dissolved in it?

- ◻️ It stays at 100 °C.  
  _↳ feedback if chosen: Impurities change it._
- ✅ It rises above 100 °C.
- ◻️ The water cannot boil.  
  _↳ feedback if chosen: Salt water does boil._
- ◻️ It falls below 100 °C.  
  _↳ feedback if chosen: Impurities raise the boiling point._

Full working after a second miss:

> Dissolved impurities raise the boiling point.  
> So the answer is “It rises above 100 °C.”.  

> Why is salt put on icy roads in cold countries?

- ◻️ It adds heat.  
  _↳ feedback if chosen: Salt does not give out heat here._
- ◻️ It raises the freezing point.  
  _↳ feedback if chosen: Salt lowers the freezing point._
- ◻️ It makes the road dry by magic.  
  _↳ feedback if chosen: That is not science._
- ✅ It lowers the freezing point, so the ice melts.

Full working after a second miss:

> Impurities lower the freezing point.  
> So the answer is “It lowers the freezing point, so the ice melts.”.  

> A solid melts slowly between 75 °C and 79 °C. Its true melting point is 80 °C. What does this show?

- ◻️ It is a gas.  
  _↳ feedback if chosen: It is a solid that melts._
- ✅ It is impure.
- ◻️ It is pure.  
  _↳ feedback if chosen: A pure solid melts sharply at 80 °C._
- ◻️ It is a liquid.  
  _↳ feedback if chosen: It is a solid before it melts._

Full working after a second miss:

> Impurities lower the melting point and give a range.  
> So the answer is “It is impure.”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

### `k2-45-spot-card` · Lesson 45 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A food colour gives three spots on a chromatogram. What does this show? | It is a mixture of at least three dyes. | It is a pure dye. · It is a gas. · The paper is dirty. | A pure dye gives one spot. · It is a dye solution. · That is not the likely reason. | Each spot is a different substance. |
| A sample gives one spot in chromatography and melts sharply at its known melting point. What can you say? | It is very likely pure. | It is a mixture. · It is impure. · It is a solution. | A mixture gives several spots and a range. · Both tests show purity. · It melts as a solid. | Both purity tests agree. |
| Why must medicines be pure? | Impurities can be harmful to the body. | Pure substances are cheaper. · Impurities make them taste sweet. · Pure substances are always liquids. | Purification costs more. · That is not the reason. · Many pure medicines are solids. | Impure medicines can poison or fail to work. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A food colour gives three spots on a chromatogram. What does this show?

- ✅ It is a mixture of at least three dyes.
- ◻️ It is a gas.  
  _↳ feedback if chosen: It is a dye solution._
- ◻️ It is a pure dye.  
  _↳ feedback if chosen: A pure dye gives one spot._
- ◻️ The paper is dirty.  
  _↳ feedback if chosen: That is not the likely reason._

Full working after a second miss:

> Each spot is a different substance.  
> So the answer is “It is a mixture of at least three dyes.”.  

> A sample gives one spot in chromatography and melts sharply at its known melting point. What can you say?

- ✅ It is very likely pure.
- ◻️ It is a mixture.  
  _↳ feedback if chosen: A mixture gives several spots and a range._
- ◻️ It is a solution.  
  _↳ feedback if chosen: It melts as a solid._
- ◻️ It is impure.  
  _↳ feedback if chosen: Both tests show purity._

Full working after a second miss:

> Both purity tests agree.  
> So the answer is “It is very likely pure.”.  

> A food colour gives three spots on a chromatogram. What does this show?

- ◻️ It is a pure dye.  
  _↳ feedback if chosen: A pure dye gives one spot._
- ◻️ It is a gas.  
  _↳ feedback if chosen: It is a dye solution._
- ✅ It is a mixture of at least three dyes.
- ◻️ The paper is dirty.  
  _↳ feedback if chosen: That is not the likely reason._

Full working after a second miss:

> Each spot is a different substance.  
> So the answer is “It is a mixture of at least three dyes.”.  

Sources: separation-purity (States of matter and changes of state; separation by picking, sieving, decanting, filtration, evaporation, crystallisation, magnet, separating funnel, winnowing, simple and fractional distillation, paper and column chromatography, sublimation; melting and boiling points; criteria for purity)

