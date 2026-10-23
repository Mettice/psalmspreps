# Chemistry Form 3, Form Three Chemistry: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f3-chemistry`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1

Rules the computed answers use are listed in the subject’s library tests; every authored answer is in Part 2.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `k3-1-where` | 1 | multiple choice, 1 | atoms |
| 2 | `k3-1-model` | 1 | multiple choice, 3 | atoms |
| 3 | `k3-2-def` | 2 | multiple choice, 1 | atoms |
| 4 | `k3-2-ring` | 2 | multiple choice, 2 | atoms |
| 5 | `k3-2-brown` | 2 | multiple choice, 2 | atoms |
| 6 | `k3-2-order` | 2 | ordering, 3 | atoms |
| 7 | `k3-2-ring-card` (card c3k2-2) | 2 | multiple choice, 1 | atoms |
| 8 | `k3-2-brown-card` (card c3k2-3) | 2 | multiple choice, 1 | atoms |
| 9 | `k3-3-table` | 3 | multiple choice, 1 | atoms |
| 10 | `k3-3-charge` | 3 | multiple choice, 3 | atoms |
| 11 | `k3-5-def` | 5 | multiple choice, 1 | isotopes |
| 12 | `k3-5-real` | 5 | number, 1 | isotopes |
| 13 | `k3-5-prop` | 5 | multiple choice, 2 | isotopes |
| 14 | `k3-5-prop-card` (card c3k5-3) | 5 | multiple choice, 1 | isotopes |
| 15 | `k3-7-L` | 7 | multiple choice, 1 | mole |

### `k3-1-where` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Where are the protons in an atom? | in the nucleus | in the shells around the nucleus · spread evenly through the atom · outside the atom | Electrons are in the shells. · The nucleus is a tiny dense centre. · All particles of an atom are inside it. | Protons and neutrons make up the nucleus. |
| Which particle moves around the nucleus? | the electron | the proton · the neutron · the nucleus | Protons stay in the nucleus. · Neutrons stay in the nucleus. · The nucleus is the centre itself. | Electrons move in shells around the nucleus. |
| Why is an atom electrically neutral? | It has equal numbers of protons and electrons | It has no particles with charge · It has equal numbers of protons and neutrons · Its neutrons cancel the charges | Protons and electrons are charged. · Neutrons have no charge, so they do not balance anything. · Neutrons have no charge. | Each proton's + charge is balanced by an electron's − charge. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is an atom electrically neutral?

- ◻️ It has equal numbers of protons and neutrons  
  _↳ feedback if chosen: Neutrons have no charge, so they do not balance anything._
- ◻️ Its neutrons cancel the charges  
  _↳ feedback if chosen: Neutrons have no charge._
- ◻️ It has no particles with charge  
  _↳ feedback if chosen: Protons and electrons are charged._
- ✅ It has equal numbers of protons and electrons

Full working after a second miss:

> Each proton's + charge is balanced by an electron's − charge.  
> So the answer is It has equal numbers of protons and electrons.  

> Which particle moves around the nucleus?

- ◻️ the nucleus  
  _↳ feedback if chosen: The nucleus is the centre itself._
- ◻️ the proton  
  _↳ feedback if chosen: Protons stay in the nucleus._
- ◻️ the neutron  
  _↳ feedback if chosen: Neutrons stay in the nucleus._
- ✅ the electron

Full working after a second miss:

> Electrons move in shells around the nucleus.  
> So the answer is the electron.  

> Where are the protons in an atom?

- ◻️ in the shells around the nucleus  
  _↳ feedback if chosen: Electrons are in the shells._
- ◻️ outside the atom  
  _↳ feedback if chosen: All particles of an atom are inside it._
- ✅ in the nucleus
- ◻️ spread evenly through the atom  
  _↳ feedback if chosen: The nucleus is a tiny dense centre._

Full working after a second miss:

> Protons and neutrons make up the nucleus.  
> So the answer is in the nucleus.  

Sources: atoms (Form 3 Chemistry syllabus, Term 1: structure of the atom, diffusion and Brownian motion, subatomic particles, atomic and mass numbers)

### `k3-1-model` · Lesson 1 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Most of the mass of an atom is in… | the nucleus | the electrons · the empty space · the outer shell | Electrons are very light (about 1/1840 of a proton). · Space has no mass. · The outer shell holds only light electrons. | Protons and neutrons are much heavier than electrons. |
| Most of the volume of an atom is… | empty space around the nucleus | filled by the nucleus · filled with neutrons · filled with protons | The nucleus is tiny compared with the atom. · Neutrons are in the tiny nucleus. · Protons are in the tiny nucleus. | Electrons move in a large space around a tiny nucleus. |
| Which statement about the nucleus is correct? | It is positively charged | It is negatively charged · It has no charge · It contains the electrons | It holds protons (positive) and neutrons (none). · The protons give it a positive charge. · Electrons are outside it. | Protons give the nucleus its positive charge. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Most of the mass of an atom is in…

- ✅ the nucleus
- ◻️ the outer shell  
  _↳ feedback if chosen: The outer shell holds only light electrons._
- ◻️ the empty space  
  _↳ feedback if chosen: Space has no mass._
- ◻️ the electrons  
  _↳ feedback if chosen: Electrons are very light (about 1/1840 of a proton)._

Full working after a second miss:

> Protons and neutrons are much heavier than electrons.  
> So the answer is the nucleus.  

> Most of the mass of an atom is in…

- ◻️ the electrons  
  _↳ feedback if chosen: Electrons are very light (about 1/1840 of a proton)._
- ✅ the nucleus
- ◻️ the outer shell  
  _↳ feedback if chosen: The outer shell holds only light electrons._
- ◻️ the empty space  
  _↳ feedback if chosen: Space has no mass._

Full working after a second miss:

> Protons and neutrons are much heavier than electrons.  
> So the answer is the nucleus.  

> Which statement about the nucleus is correct?

- ◻️ It is negatively charged  
  _↳ feedback if chosen: It holds protons (positive) and neutrons (none)._
- ◻️ It contains the electrons  
  _↳ feedback if chosen: Electrons are outside it._
- ◻️ It has no charge  
  _↳ feedback if chosen: The protons give it a positive charge._
- ✅ It is positively charged

Full working after a second miss:

> Protons give the nucleus its positive charge.  
> So the answer is It is positively charged.  

Sources: atoms (Form 3 Chemistry syllabus, Term 1: structure of the atom, diffusion and Brownian motion, subatomic particles, atomic and mass numbers)

### `k3-2-def` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is diffusion? | The spreading of particles from high to low concentration | The melting of a solid · The movement of particles from low to high concentration · The dissolving of a gas in a liquid only | Melting is a change of state. · Particles spread from where there are many to where there are few. · Diffusion happens in gases and liquids generally. | Random motion spreads particles out evenly. |
| A crystal of potassium permanganate is dropped into still water. After some hours… | the purple colour spreads through all the water | the colour stays around the crystal · the water turns solid · the colour moves to the top only | The particles move and spread out. · Nothing freezes. · They spread in all directions. | The coloured particles diffuse until evenly spread. |
| Which shows diffusion? | The smell of perfume spreading across a room | Water freezing in a fridge · A stone sinking in water · Ice melting in the sun | That is freezing. · That is sinking (density). · That is melting. | Perfume particles spread through the air. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is diffusion?

- ◻️ The movement of particles from low to high concentration  
  _↳ feedback if chosen: Particles spread from where there are many to where there are few._
- ◻️ The melting of a solid  
  _↳ feedback if chosen: Melting is a change of state._
- ◻️ The dissolving of a gas in a liquid only  
  _↳ feedback if chosen: Diffusion happens in gases and liquids generally._
- ✅ The spreading of particles from high to low concentration

Full working after a second miss:

> Random motion spreads particles out evenly.  
> So the answer is The spreading of particles from high to low concentration.  

> What is diffusion?

- ◻️ The melting of a solid  
  _↳ feedback if chosen: Melting is a change of state._
- ◻️ The dissolving of a gas in a liquid only  
  _↳ feedback if chosen: Diffusion happens in gases and liquids generally._
- ◻️ The movement of particles from low to high concentration  
  _↳ feedback if chosen: Particles spread from where there are many to where there are few._
- ✅ The spreading of particles from high to low concentration

Full working after a second miss:

> Random motion spreads particles out evenly.  
> So the answer is The spreading of particles from high to low concentration.  

> What is diffusion?

- ◻️ The movement of particles from low to high concentration  
  _↳ feedback if chosen: Particles spread from where there are many to where there are few._
- ◻️ The melting of a solid  
  _↳ feedback if chosen: Melting is a change of state._
- ✅ The spreading of particles from high to low concentration
- ◻️ The dissolving of a gas in a liquid only  
  _↳ feedback if chosen: Diffusion happens in gases and liquids generally._

Full working after a second miss:

> Random motion spreads particles out evenly.  
> So the answer is The spreading of particles from high to low concentration.  

Sources: atoms (Form 3 Chemistry syllabus, Term 1: structure of the atom, diffusion and Brownian motion, subatomic particles, atomic and mass numbers)

### `k3-2-ring` · Lesson 2 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In the ammonia / hydrogen chloride tube experiment, why does the white ring form nearer the hydrogen chloride end? | Ammonia particles are lighter and diffuse faster | Hydrogen chloride is lighter · Ammonia was put in first · The ring always forms in the middle | Hydrogen chloride (36.5) is heavier than ammonia (17). · Both are put in at the same time. · Then the ring would be in the middle. | The faster gas travels further before they meet. |
| Which gas diffuses fastest? | hydrogen (the lightest gas) | carbon dioxide · chlorine · oxygen | Carbon dioxide is heavier. · Chlorine is very heavy. · Oxygen is heavier than hydrogen. | Lighter particles move faster. |
| How does temperature affect diffusion? | Diffusion is faster at higher temperature | Diffusion is slower at higher temperature · Temperature has no effect · Diffusion stops above 50 °C | Heat makes particles move faster. · Faster particles spread faster. · It does not stop. | Particles have more energy when hot. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How does temperature affect diffusion?

- ◻️ Temperature has no effect  
  _↳ feedback if chosen: Faster particles spread faster._
- ◻️ Diffusion is slower at higher temperature  
  _↳ feedback if chosen: Heat makes particles move faster._
- ◻️ Diffusion stops above 50 °C  
  _↳ feedback if chosen: It does not stop._
- ✅ Diffusion is faster at higher temperature

Full working after a second miss:

> Particles have more energy when hot.  
> So the answer is Diffusion is faster at higher temperature.  

> In the ammonia / hydrogen chloride tube experiment, why does the white ring form nearer the hydrogen chloride end?

- ◻️ The ring always forms in the middle  
  _↳ feedback if chosen: Then the ring would be in the middle._
- ◻️ Ammonia was put in first  
  _↳ feedback if chosen: Both are put in at the same time._
- ✅ Ammonia particles are lighter and diffuse faster
- ◻️ Hydrogen chloride is lighter  
  _↳ feedback if chosen: Hydrogen chloride (36.5) is heavier than ammonia (17)._

Full working after a second miss:

> The faster gas travels further before they meet.  
> So the answer is Ammonia particles are lighter and diffuse faster.  

> Which gas diffuses fastest?

- ✅ hydrogen (the lightest gas)
- ◻️ chlorine  
  _↳ feedback if chosen: Chlorine is very heavy._
- ◻️ carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide is heavier._
- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen is heavier than hydrogen._

Full working after a second miss:

> Lighter particles move faster.  
> So the answer is hydrogen (the lightest gas).  

Sources: atoms (Form 3 Chemistry syllabus, Term 1: structure of the atom, diffusion and Brownian motion, subatomic particles, atomic and mass numbers)

### `k3-2-brown` · Lesson 2 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is seen in Brownian motion? | Small particles such as smoke moving in a jerky, random way | Atoms seen directly under a microscope · Particles moving in straight lines only · Particles standing still | Atoms are far too small to see; we see the smoke specks they hit. · The motion is zig-zag. · They keep moving. | Invisible air particles knock the visible specks about. |
| What causes Brownian motion of pollen grains in water? | Water molecules hitting the grains unevenly | The grains are alive and swimming · Light pushing the grains · Magnetism | Dead pollen and dust move too. · Light is not the cause. · There is no magnet. | Uneven bombardment by moving water molecules. |
| Brownian motion is evidence that… | the particles of liquids and gases are always moving | solids do not contain particles · particles are larger than smoke specks · air has no mass | It says nothing about solids. · The particles are much smaller. · Air particles have mass; that is why they can push. | Only moving particles could keep jostling the specks. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Brownian motion is evidence that…

- ◻️ air has no mass  
  _↳ feedback if chosen: Air particles have mass; that is why they can push._
- ◻️ solids do not contain particles  
  _↳ feedback if chosen: It says nothing about solids._
- ✅ the particles of liquids and gases are always moving
- ◻️ particles are larger than smoke specks  
  _↳ feedback if chosen: The particles are much smaller._

Full working after a second miss:

> Only moving particles could keep jostling the specks.  
> So the answer is the particles of liquids and gases are always moving.  

> What is seen in Brownian motion?

- ◻️ Particles moving in straight lines only  
  _↳ feedback if chosen: The motion is zig-zag._
- ✅ Small particles such as smoke moving in a jerky, random way
- ◻️ Atoms seen directly under a microscope  
  _↳ feedback if chosen: Atoms are far too small to see; we see the smoke specks they hit._
- ◻️ Particles standing still  
  _↳ feedback if chosen: They keep moving._

Full working after a second miss:

> Invisible air particles knock the visible specks about.  
> So the answer is Small particles such as smoke moving in a jerky, random way.  

> Brownian motion is evidence that…

- ◻️ air has no mass  
  _↳ feedback if chosen: Air particles have mass; that is why they can push._
- ✅ the particles of liquids and gases are always moving
- ◻️ particles are larger than smoke specks  
  _↳ feedback if chosen: The particles are much smaller._
- ◻️ solids do not contain particles  
  _↳ feedback if chosen: It says nothing about solids._

Full working after a second miss:

> Only moving particles could keep jostling the specks.  
> So the answer is the particles of liquids and gases are always moving.  

Sources: atoms (Form 3 Chemistry syllabus, Term 1: structure of the atom, diffusion and Brownian motion, subatomic particles, atomic and mass numbers)

### `k3-2-order` · Lesson 2 · ordering, level 3

Prompt: Put the explanation of the white ring in the ammonia / hydrogen chloride tube in order.

Items in the right order:

1. Ammonia and hydrogen chloride particles move along the tube by diffusion.
2. Ammonia particles are lighter, so they move faster.
3. The two gases meet nearer the hydrogen chloride end.
4. They react to form a white ring of solid ammonium chloride.


Three generated variants:

> Put the explanation of the white ring in the ammonia / hydrogen chloride tube in order.

Shown as: Ammonia particles are lighter, so they move faster. · The two gases meet nearer the hydrogen chloride end. · They react to form a white ring of solid ammonium chloride. · Ammonia and hydrogen chloride particles move along the tube by diffusion.
Correct order: Ammonia and hydrogen chloride particles move along the tube by diffusion. → Ammonia particles are lighter, so they move faster. → The two gases meet nearer the hydrogen chloride end. → They react to form a white ring of solid ammonium chloride.

Hint (draft): Start with the particles moving.

Full working after a second miss:

> The correct order is: Ammonia and hydrogen chloride particles move along the tube by diffusion. → Ammonia particles are lighter, so they move faster. → The two gases meet nearer the hydrogen chloride end. → They react to form a white ring of solid ammonium chloride..  

> Put the explanation of the white ring in the ammonia / hydrogen chloride tube in order.

Shown as: Ammonia and hydrogen chloride particles move along the tube by diffusion. · Ammonia particles are lighter, so they move faster. · They react to form a white ring of solid ammonium chloride. · The two gases meet nearer the hydrogen chloride end.
Correct order: Ammonia and hydrogen chloride particles move along the tube by diffusion. → Ammonia particles are lighter, so they move faster. → The two gases meet nearer the hydrogen chloride end. → They react to form a white ring of solid ammonium chloride.

Hint (draft): Start with the particles moving.

Full working after a second miss:

> The correct order is: Ammonia and hydrogen chloride particles move along the tube by diffusion. → Ammonia particles are lighter, so they move faster. → The two gases meet nearer the hydrogen chloride end. → They react to form a white ring of solid ammonium chloride..  

> Put the explanation of the white ring in the ammonia / hydrogen chloride tube in order.

Shown as: They react to form a white ring of solid ammonium chloride. · Ammonia and hydrogen chloride particles move along the tube by diffusion. · Ammonia particles are lighter, so they move faster. · The two gases meet nearer the hydrogen chloride end.
Correct order: Ammonia and hydrogen chloride particles move along the tube by diffusion. → Ammonia particles are lighter, so they move faster. → The two gases meet nearer the hydrogen chloride end. → They react to form a white ring of solid ammonium chloride.

Hint (draft): Start with the particles moving.

Full working after a second miss:

> The correct order is: Ammonia and hydrogen chloride particles move along the tube by diffusion. → Ammonia particles are lighter, so they move faster. → The two gases meet nearer the hydrogen chloride end. → They react to form a white ring of solid ammonium chloride..  

Sources: atoms (Form 3 Chemistry syllabus, Term 1: structure of the atom, diffusion and Brownian motion, subatomic particles, atomic and mass numbers)

### `k3-2-ring-card` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In the ammonia / hydrogen chloride tube experiment, why does the white ring form nearer the hydrogen chloride end? | Ammonia particles are lighter and diffuse faster | Hydrogen chloride is lighter · Ammonia was put in first · The ring always forms in the middle | Hydrogen chloride (36.5) is heavier than ammonia (17). · Both are put in at the same time. · Then the ring would be in the middle. | The faster gas travels further before they meet. |
| Which gas diffuses fastest? | hydrogen (the lightest gas) | carbon dioxide · chlorine · oxygen | Carbon dioxide is heavier. · Chlorine is very heavy. · Oxygen is heavier than hydrogen. | Lighter particles move faster. |
| How does temperature affect diffusion? | Diffusion is faster at higher temperature | Diffusion is slower at higher temperature · Temperature has no effect · Diffusion stops above 50 °C | Heat makes particles move faster. · Faster particles spread faster. · It does not stop. | Particles have more energy when hot. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In the ammonia / hydrogen chloride tube experiment, why does the white ring form nearer the hydrogen chloride end?

- ◻️ The ring always forms in the middle  
  _↳ feedback if chosen: Then the ring would be in the middle._
- ◻️ Ammonia was put in first  
  _↳ feedback if chosen: Both are put in at the same time._
- ◻️ Hydrogen chloride is lighter  
  _↳ feedback if chosen: Hydrogen chloride (36.5) is heavier than ammonia (17)._
- ✅ Ammonia particles are lighter and diffuse faster

Full working after a second miss:

> The faster gas travels further before they meet.  
> So the answer is Ammonia particles are lighter and diffuse faster.  

> In the ammonia / hydrogen chloride tube experiment, why does the white ring form nearer the hydrogen chloride end?

- ◻️ Hydrogen chloride is lighter  
  _↳ feedback if chosen: Hydrogen chloride (36.5) is heavier than ammonia (17)._
- ◻️ The ring always forms in the middle  
  _↳ feedback if chosen: Then the ring would be in the middle._
- ✅ Ammonia particles are lighter and diffuse faster
- ◻️ Ammonia was put in first  
  _↳ feedback if chosen: Both are put in at the same time._

Full working after a second miss:

> The faster gas travels further before they meet.  
> So the answer is Ammonia particles are lighter and diffuse faster.  

> How does temperature affect diffusion?

- ✅ Diffusion is faster at higher temperature
- ◻️ Diffusion stops above 50 °C  
  _↳ feedback if chosen: It does not stop._
- ◻️ Temperature has no effect  
  _↳ feedback if chosen: Faster particles spread faster._
- ◻️ Diffusion is slower at higher temperature  
  _↳ feedback if chosen: Heat makes particles move faster._

Full working after a second miss:

> Particles have more energy when hot.  
> So the answer is Diffusion is faster at higher temperature.  

Sources: atoms (Form 3 Chemistry syllabus, Term 1: structure of the atom, diffusion and Brownian motion, subatomic particles, atomic and mass numbers)

### `k3-2-brown-card` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is seen in Brownian motion? | Small particles such as smoke moving in a jerky, random way | Atoms seen directly under a microscope · Particles moving in straight lines only · Particles standing still | Atoms are far too small to see; we see the smoke specks they hit. · The motion is zig-zag. · They keep moving. | Invisible air particles knock the visible specks about. |
| What causes Brownian motion of pollen grains in water? | Water molecules hitting the grains unevenly | The grains are alive and swimming · Light pushing the grains · Magnetism | Dead pollen and dust move too. · Light is not the cause. · There is no magnet. | Uneven bombardment by moving water molecules. |
| Brownian motion is evidence that… | the particles of liquids and gases are always moving | solids do not contain particles · particles are larger than smoke specks · air has no mass | It says nothing about solids. · The particles are much smaller. · Air particles have mass; that is why they can push. | Only moving particles could keep jostling the specks. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Brownian motion is evidence that…

- ✅ the particles of liquids and gases are always moving
- ◻️ particles are larger than smoke specks  
  _↳ feedback if chosen: The particles are much smaller._
- ◻️ air has no mass  
  _↳ feedback if chosen: Air particles have mass; that is why they can push._
- ◻️ solids do not contain particles  
  _↳ feedback if chosen: It says nothing about solids._

Full working after a second miss:

> Only moving particles could keep jostling the specks.  
> So the answer is the particles of liquids and gases are always moving.  

> What causes Brownian motion of pollen grains in water?

- ✅ Water molecules hitting the grains unevenly
- ◻️ Light pushing the grains  
  _↳ feedback if chosen: Light is not the cause._
- ◻️ Magnetism  
  _↳ feedback if chosen: There is no magnet._
- ◻️ The grains are alive and swimming  
  _↳ feedback if chosen: Dead pollen and dust move too._

Full working after a second miss:

> Uneven bombardment by moving water molecules.  
> So the answer is Water molecules hitting the grains unevenly.  

> What causes Brownian motion of pollen grains in water?

- ◻️ Magnetism  
  _↳ feedback if chosen: There is no magnet._
- ◻️ The grains are alive and swimming  
  _↳ feedback if chosen: Dead pollen and dust move too._
- ✅ Water molecules hitting the grains unevenly
- ◻️ Light pushing the grains  
  _↳ feedback if chosen: Light is not the cause._

Full working after a second miss:

> Uneven bombardment by moving water molecules.  
> So the answer is Water molecules hitting the grains unevenly.  

Sources: atoms (Form 3 Chemistry syllabus, Term 1: structure of the atom, diffusion and Brownian motion, subatomic particles, atomic and mass numbers)

### `k3-3-table` · Lesson 3 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the relative charge of a neutron? | 0 | +1 · −1 · +2 | +1 is the proton. · −1 is the electron. · No subatomic particle has +2. | Neutrons are neutral. |
| Which particle has a relative mass of about 1/1840? | the electron | the proton · the neutron · the nucleus | A proton has relative mass 1. · A neutron has relative mass 1. · The nucleus is the heaviest part. | Electrons are about 1840 times lighter than protons. |
| What is the relative charge of a proton? | +1 | −1 · 0 · +1840 | −1 is the electron. · 0 is the neutron. · 1840 compares masses, not charges. | Protons carry one positive charge each. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the relative charge of a proton?

- ◻️ 0  
  _↳ feedback if chosen: 0 is the neutron._
- ✅ +1
- ◻️ −1  
  _↳ feedback if chosen: −1 is the electron._
- ◻️ +1840  
  _↳ feedback if chosen: 1840 compares masses, not charges._

Full working after a second miss:

> Protons carry one positive charge each.  
> So the answer is +1.  

> Which particle has a relative mass of about 1/1840?

- ◻️ the nucleus  
  _↳ feedback if chosen: The nucleus is the heaviest part._
- ✅ the electron
- ◻️ the neutron  
  _↳ feedback if chosen: A neutron has relative mass 1._
- ◻️ the proton  
  _↳ feedback if chosen: A proton has relative mass 1._

Full working after a second miss:

> Electrons are about 1840 times lighter than protons.  
> So the answer is the electron.  

> Which particle has a relative mass of about 1/1840?

- ◻️ the proton  
  _↳ feedback if chosen: A proton has relative mass 1._
- ✅ the electron
- ◻️ the nucleus  
  _↳ feedback if chosen: The nucleus is the heaviest part._
- ◻️ the neutron  
  _↳ feedback if chosen: A neutron has relative mass 1._

Full working after a second miss:

> Electrons are about 1840 times lighter than protons.  
> So the answer is the electron.  

Sources: atoms (Form 3 Chemistry syllabus, Term 1: structure of the atom, diffusion and Brownian motion, subatomic particles, atomic and mass numbers)

### `k3-3-charge` · Lesson 3 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| An atom loses two electrons. What is the charge of the ion? | 2+ | 2− · 0 · 1+ | Losing negative electrons leaves extra positive charge. · It now has more protons than electrons. · It lost two, not one. | Two more protons than electrons: 2+. |
| An ion has 17 protons and 18 electrons. What is its charge? | 1− | 1+ · 0 · 35− | It has more electrons than protons. · The numbers are not equal. · Charge = protons − electrons = −1. | One extra electron: 1−. |
| An ion has 12 protons and 10 electrons. What is its charge? | 2+ | 2− · 22+ · 0 | It has fewer electrons than protons. · Charge is the difference, not the sum. · The numbers are not equal. | 12 − 10 = 2 more protons: 2+. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> An ion has 12 protons and 10 electrons. What is its charge?

- ◻️ 2−  
  _↳ feedback if chosen: It has fewer electrons than protons._
- ✅ 2+
- ◻️ 22+  
  _↳ feedback if chosen: Charge is the difference, not the sum._
- ◻️ 0  
  _↳ feedback if chosen: The numbers are not equal._

Full working after a second miss:

> 12 − 10 = 2 more protons: 2+.  
> So the answer is 2+.  

> An ion has 12 protons and 10 electrons. What is its charge?

- ✅ 2+
- ◻️ 22+  
  _↳ feedback if chosen: Charge is the difference, not the sum._
- ◻️ 2−  
  _↳ feedback if chosen: It has fewer electrons than protons._
- ◻️ 0  
  _↳ feedback if chosen: The numbers are not equal._

Full working after a second miss:

> 12 − 10 = 2 more protons: 2+.  
> So the answer is 2+.  

> An ion has 17 protons and 18 electrons. What is its charge?

- ◻️ 0  
  _↳ feedback if chosen: The numbers are not equal._
- ◻️ 35−  
  _↳ feedback if chosen: Charge = protons − electrons = −1._
- ◻️ 1+  
  _↳ feedback if chosen: It has more electrons than protons._
- ✅ 1−

Full working after a second miss:

> One extra electron: 1−.  
> So the answer is 1−.  

Sources: atoms (Form 3 Chemistry syllabus, Term 1: structure of the atom, diffusion and Brownian motion, subatomic particles, atomic and mass numbers)

### `k3-5-def` · Lesson 5 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What are isotopes? | Atoms of the same element with different numbers of neutrons | Atoms of different elements with the same mass number · Atoms with different numbers of protons · Atoms with different numbers of electrons only | Different elements have different numbers of protons. · Changing the protons changes the element. · That describes ions. | Same Z, different A. |
| ¹²₆C and ¹⁴₆C are isotopes. How do they differ? | ¹⁴C has two more neutrons | ¹⁴C has two more protons · ¹⁴C has two more electrons · They are different elements | Both have 6 protons. · Both neutral atoms have 6 electrons. · Both are carbon (Z = 6). | Mass numbers differ by 2, protons are equal, so neutrons differ by 2. |
| Which pair are isotopes? | ³⁵₁₇Cl and ³⁷₁₇Cl | ⁴⁰₁₈Ar and ⁴⁰₂₀Ca · ²³₁₁Na and ²⁴₁₂Mg · ¹⁶₈O and ¹⁴₇N | Same mass number but different elements (different Z). · Different elements. · Different elements. | Same atomic number (17), different mass numbers. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> ¹²₆C and ¹⁴₆C are isotopes. How do they differ?

- ◻️ ¹⁴C has two more electrons  
  _↳ feedback if chosen: Both neutral atoms have 6 electrons._
- ◻️ They are different elements  
  _↳ feedback if chosen: Both are carbon (Z = 6)._
- ✅ ¹⁴C has two more neutrons
- ◻️ ¹⁴C has two more protons  
  _↳ feedback if chosen: Both have 6 protons._

Full working after a second miss:

> Mass numbers differ by 2, protons are equal, so neutrons differ by 2.  
> So the answer is ¹⁴C has two more neutrons.  

> Which pair are isotopes?

- ◻️ ¹⁶₈O and ¹⁴₇N  
  _↳ feedback if chosen: Different elements._
- ◻️ ⁴⁰₁₈Ar and ⁴⁰₂₀Ca  
  _↳ feedback if chosen: Same mass number but different elements (different Z)._
- ◻️ ²³₁₁Na and ²⁴₁₂Mg  
  _↳ feedback if chosen: Different elements._
- ✅ ³⁵₁₇Cl and ³⁷₁₇Cl

Full working after a second miss:

> Same atomic number (17), different mass numbers.  
> So the answer is ³⁵₁₇Cl and ³⁷₁₇Cl.  

> What are isotopes?

- ◻️ Atoms with different numbers of electrons only  
  _↳ feedback if chosen: That describes ions._
- ✅ Atoms of the same element with different numbers of neutrons
- ◻️ Atoms with different numbers of protons  
  _↳ feedback if chosen: Changing the protons changes the element._
- ◻️ Atoms of different elements with the same mass number  
  _↳ feedback if chosen: Different elements have different numbers of protons._

Full working after a second miss:

> Same Z, different A.  
> So the answer is Atoms of the same element with different numbers of neutrons.  

Sources: isotopes (Form 3 Chemistry syllabus, Term 1: isotopy and calculation of relative atomic mass)

### `k3-5-real` · Lesson 5 · number, level 1

Prompt: {X.n}: {X.a}. Calculate the relative atomic mass of {X.n} to {1} decimal place.
Right answer: `roundTo(X.v, 0.1)`

Table `X` (one row is picked each time):

| n | a | s | v |
|---|---|---|---|
| Chlorine | 75% ³⁵Cl and 25% ³⁷Cl | (35 × 75 + 37 × 25) ÷ 100 = 35.5 | 35.5 |
| Copper | 69% ⁶³Cu and 31% ⁶⁵Cu | (63 × 69 + 65 × 31) ÷ 100 = 63.62 | 63.62 |
| Boron | 20% ¹⁰B and 80% ¹¹B | (10 × 20 + 11 × 80) ÷ 100 = 10.8 | 10.8 |
| Neon | 90% ²⁰Ne and 10% ²²Ne | (20 × 90 + 22 × 10) ÷ 100 = 20.2 | 20.2 |
| Bromine | 50% ⁷⁹Br and 50% ⁸¹Br | (79 × 50 + 81 × 50) ÷ 100 = 80 | 80 |


Three generated variants:

> Boron: 20% ¹⁰B and 80% ¹¹B. Calculate the relative atomic mass of Boron to 1 decimal place.

Answer: **10.8**

Full working after a second miss:

> (10 × 20 + 11 × 80) ÷ 100 = 10.8  
> ≈ 10.8.  

> Boron: 20% ¹⁰B and 80% ¹¹B. Calculate the relative atomic mass of Boron to 1 decimal place.

Answer: **10.8**

Full working after a second miss:

> (10 × 20 + 11 × 80) ÷ 100 = 10.8  
> ≈ 10.8.  

> Neon: 90% ²⁰Ne and 10% ²²Ne. Calculate the relative atomic mass of Neon to 1 decimal place.

Answer: **20.2**

Full working after a second miss:

> (20 × 90 + 22 × 10) ÷ 100 = 20.2  
> ≈ 20.2.  

Sources: isotopes (Form 3 Chemistry syllabus, Term 1: isotopy and calculation of relative atomic mass)

### `k3-5-prop` · Lesson 5 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do ³⁵Cl and ³⁷Cl have the same chemical properties? | They have the same number of electrons | They have the same mass number · They have the same number of neutrons · They are different elements | Their mass numbers differ. · Their neutrons differ. · Both are chlorine. | Chemical reactions involve electrons, which are the same. |
| Which property differs between two isotopes of the same element? | their mass | their number of protons · their chemical reactions · their atomic number | Protons are the same. · Reactions are the same. · The atomic number is the same. | Different numbers of neutrons give different masses. |
| Why is the RAM of chlorine 35.5 and not a whole number? | It is an average of isotopes of mass 35 and 37 | A chlorine atom has half a neutron · It has 35.5 protons · It was measured wrongly | Particles are not split. · Chlorine has 17 protons. · It is an exact average. | The weighted average of 35 (75%) and 37 (25%) is 35.5. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why do ³⁵Cl and ³⁷Cl have the same chemical properties?

- ◻️ They are different elements  
  _↳ feedback if chosen: Both are chlorine._
- ◻️ They have the same mass number  
  _↳ feedback if chosen: Their mass numbers differ._
- ◻️ They have the same number of neutrons  
  _↳ feedback if chosen: Their neutrons differ._
- ✅ They have the same number of electrons

Full working after a second miss:

> Chemical reactions involve electrons, which are the same.  
> So the answer is They have the same number of electrons.  

> Why do ³⁵Cl and ³⁷Cl have the same chemical properties?

- ◻️ They have the same number of neutrons  
  _↳ feedback if chosen: Their neutrons differ._
- ◻️ They are different elements  
  _↳ feedback if chosen: Both are chlorine._
- ◻️ They have the same mass number  
  _↳ feedback if chosen: Their mass numbers differ._
- ✅ They have the same number of electrons

Full working after a second miss:

> Chemical reactions involve electrons, which are the same.  
> So the answer is They have the same number of electrons.  

> Why is the RAM of chlorine 35.5 and not a whole number?

- ✅ It is an average of isotopes of mass 35 and 37
- ◻️ It has 35.5 protons  
  _↳ feedback if chosen: Chlorine has 17 protons._
- ◻️ It was measured wrongly  
  _↳ feedback if chosen: It is an exact average._
- ◻️ A chlorine atom has half a neutron  
  _↳ feedback if chosen: Particles are not split._

Full working after a second miss:

> The weighted average of 35 (75%) and 37 (25%) is 35.5.  
> So the answer is It is an average of isotopes of mass 35 and 37.  

Sources: isotopes (Form 3 Chemistry syllabus, Term 1: isotopy and calculation of relative atomic mass)

### `k3-5-prop-card` · Lesson 5 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do ³⁵Cl and ³⁷Cl have the same chemical properties? | They have the same number of electrons | They have the same mass number · They have the same number of neutrons · They are different elements | Their mass numbers differ. · Their neutrons differ. · Both are chlorine. | Chemical reactions involve electrons, which are the same. |
| Which property differs between two isotopes of the same element? | their mass | their number of protons · their chemical reactions · their atomic number | Protons are the same. · Reactions are the same. · The atomic number is the same. | Different numbers of neutrons give different masses. |
| Why is the RAM of chlorine 35.5 and not a whole number? | It is an average of isotopes of mass 35 and 37 | A chlorine atom has half a neutron · It has 35.5 protons · It was measured wrongly | Particles are not split. · Chlorine has 17 protons. · It is an exact average. | The weighted average of 35 (75%) and 37 (25%) is 35.5. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is the RAM of chlorine 35.5 and not a whole number?

- ◻️ It was measured wrongly  
  _↳ feedback if chosen: It is an exact average._
- ◻️ It has 35.5 protons  
  _↳ feedback if chosen: Chlorine has 17 protons._
- ✅ It is an average of isotopes of mass 35 and 37
- ◻️ A chlorine atom has half a neutron  
  _↳ feedback if chosen: Particles are not split._

Full working after a second miss:

> The weighted average of 35 (75%) and 37 (25%) is 35.5.  
> So the answer is It is an average of isotopes of mass 35 and 37.  

> Why is the RAM of chlorine 35.5 and not a whole number?

- ◻️ It has 35.5 protons  
  _↳ feedback if chosen: Chlorine has 17 protons._
- ◻️ It was measured wrongly  
  _↳ feedback if chosen: It is an exact average._
- ✅ It is an average of isotopes of mass 35 and 37
- ◻️ A chlorine atom has half a neutron  
  _↳ feedback if chosen: Particles are not split._

Full working after a second miss:

> The weighted average of 35 (75%) and 37 (25%) is 35.5.  
> So the answer is It is an average of isotopes of mass 35 and 37.  

> Which property differs between two isotopes of the same element?

- ✅ their mass
- ◻️ their number of protons  
  _↳ feedback if chosen: Protons are the same._
- ◻️ their atomic number  
  _↳ feedback if chosen: The atomic number is the same._
- ◻️ their chemical reactions  
  _↳ feedback if chosen: Reactions are the same._

Full working after a second miss:

> Different numbers of neutrons give different masses.  
> So the answer is their mass.  

Sources: isotopes (Form 3 Chemistry syllabus, Term 1: isotopy and calculation of relative atomic mass)

### `k3-7-L` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the Avogadro constant? | 6.02 × 10²³ particles per mole | 6.02 × 10²³ grams · 12 g of carbon · 1840 | It is a number of particles, not a mass. · 12 g of carbon is one mole; it contains 6.02 × 10²³ atoms. · 1840 compares the masses of a proton and an electron. | The number of particles in one mole. |
| Which contains 6.02 × 10²³ atoms? | 24 g of magnesium (Mg = 24) | 1 g of magnesium · 12 g of magnesium · 6.02 g of magnesium | 1 g is 1/24 mol. · 12 g is 0.5 mol. · The number 6.02 is not a mass. | 24 g of magnesium is 1 mol. |
| 12 g of carbon and 32 g of sulphur (C = 12, S = 32). Which has more atoms? | They have the same number | The sulphur · The carbon · It cannot be told | 32 g of S is only 1 mol. · 12 g of C is only 1 mol. · Both are 1 mol, so the numbers can be compared. | 1 mol of each: 6.02 × 10²³ atoms. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> 12 g of carbon and 32 g of sulphur (C = 12, S = 32). Which has more atoms?

- ◻️ The sulphur  
  _↳ feedback if chosen: 32 g of S is only 1 mol._
- ✅ They have the same number
- ◻️ The carbon  
  _↳ feedback if chosen: 12 g of C is only 1 mol._
- ◻️ It cannot be told  
  _↳ feedback if chosen: Both are 1 mol, so the numbers can be compared._

Full working after a second miss:

> 1 mol of each: 6.02 × 10²³ atoms.  
> So the answer is They have the same number.  

> What is the Avogadro constant?

- ◻️ 1840  
  _↳ feedback if chosen: 1840 compares the masses of a proton and an electron._
- ◻️ 12 g of carbon  
  _↳ feedback if chosen: 12 g of carbon is one mole; it contains 6.02 × 10²³ atoms._
- ✅ 6.02 × 10²³ particles per mole
- ◻️ 6.02 × 10²³ grams  
  _↳ feedback if chosen: It is a number of particles, not a mass._

Full working after a second miss:

> The number of particles in one mole.  
> So the answer is 6.02 × 10²³ particles per mole.  

> 12 g of carbon and 32 g of sulphur (C = 12, S = 32). Which has more atoms?

- ✅ They have the same number
- ◻️ It cannot be told  
  _↳ feedback if chosen: Both are 1 mol, so the numbers can be compared._
- ◻️ The sulphur  
  _↳ feedback if chosen: 32 g of S is only 1 mol._
- ◻️ The carbon  
  _↳ feedback if chosen: 12 g of C is only 1 mol._

Full working after a second miss:

> 1 mol of each: 6.02 × 10²³ atoms.  
> So the answer is They have the same number.  

Sources: mole (Form 3 Chemistry syllabus, Term 1: RAM of an element, the mole of atoms and the Avogadro constant)

