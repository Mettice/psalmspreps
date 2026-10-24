# Chemistry Form 4, Form Four Chemistry: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f4-chemistry`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1

Rules the computed answers use are listed in the subject’s library tests; every authored answer is in Part 2.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `k4-1-frasch` | 1 | multiple choice, 1 | sulphur |
| 2 | `k4-1-ores` | 1 | matching, 2 | sulphur |
| 3 | `k4-1-pure` | 1 | multiple choice, 2 | sulphur |
| 4 | `k4-1-pure-card` (card c4k1-3) | 1 | multiple choice, 1 | sulphur |
| 5 | `k4-2-allo` | 2 | multiple choice, 1 | sulphur |
| 6 | `k4-2-match` | 2 | matching, 2 | sulphur |
| 7 | `k4-2-burn` | 2 | multiple choice, 2 | sulphur |
| 8 | `k4-2-why` | 2 | multiple choice, 3 | sulphur |
| 9 | `k4-2-burn-card` (card c4k2-3) | 2 | multiple choice, 1 | sulphur |
| 10 | `k4-3-prep` | 3 | multiple choice, 1 | sulphur |
| 11 | `k4-3-dry` | 3 | multiple choice, 2 | sulphur |
| 12 | `k4-3-dry-card` (card c4k3-3) | 3 | multiple choice, 1 | sulphur |
| 13 | `k4-4-chem` | 4 | multiple choice, 1 | sulphur |
| 14 | `k4-4-bleach` | 4 | multiple choice, 2 | sulphur |
| 15 | `k4-4-match` | 4 | matching, 3 | sulphur |
| 16 | `k4-4-bleach-card` (card c4k4-3) | 4 | multiple choice, 1 | sulphur |
| 17 | `k4-5-prep` | 5 | multiple choice, 1 | sulphur |
| 18 | `k4-6-chem` | 6 | multiple choice, 1 | sulphur |
| 19 | `k4-7-make` | 7 | multiple choice, 1 | sulphur |
| 20 | `k4-8-chem` | 8 | multiple choice, 1 | sulphur |
| 21 | `k4-9-uses` | 9 | multiple choice, 1 | sulphur |
| 22 | `k4-9-match` | 9 | matching, 2 | sulphur |
| 23 | `k4-9-match-card` (card c4k9-2) | 9 | matching, 1 | sulphur |

### `k4-1-frasch` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Where is sulphur found as the free element? | In underground deposits, often near volcanoes and oil fields | Only combined in sea water · Only in the air · Only in living plants | Sea water holds sulphates, which are combined sulphur, not the free element. · Air holds only traces of sulphur compounds, not the free element. · Plants hold sulphur in proteins, which is combined sulphur. | Free sulphur occurs in beds a few hundred metres down, and combined as sulphides and sulphates. |
| How many concentric pipes are used in the Frasch process? | Three | One · Two · Five | One pipe could not carry water down and sulphur up at the same time. · A third pipe is needed for the compressed air that lifts the froth. · Three are enough: water in, air in, froth out. | Superheated water goes down the outer pipe, hot compressed air down the inner one, and the froth rises up the middle one. |
| What is sent down the outer pipe in the Frasch process, and why? | Superheated water at about {170} °C, to melt the sulphur underground | Cold water, to cool the rock · Hot compressed air, to blow the sulphur up · Molten sulphur, to start the process | Cold water would not melt sulphur, which melts at about {115} °C. · The compressed air goes down the INNER pipe; the water goes down the outer one. · The sulphur is already in the ground; the water melts it there. | Sulphur melts at about {115} °C, so water above that temperature, kept liquid by pressure, melts it in place. |
| Why is hot compressed air forced down the inner pipe? | It froths the molten sulphur so that the lighter froth is pushed up the middle pipe | It burns the sulphur to sulphur dioxide · It cools the molten sulphur so it sets · It dissolves the sulphur in water | Burning would destroy the product; the air is there to lift it. · Hot air does not set the sulphur; the froth must stay molten to rise. · Sulphur is insoluble in water. | The froth of air and molten sulphur is less dense, so the pressure pushes it up the middle pipe. |
| Why is sulphur from the Frasch process very pure? | Only the sulphur melts and is pushed up; the rock and sand stay behind | It is purified later by distillation · It is washed with acid at the surface · It is crystallised from water | No further purification is needed; it comes up about {99} per cent pure. · No acid washing is used in the process. · Sulphur is insoluble in water, so it cannot be crystallised from it. | Melting separates the sulphur from the rock underground, so it arrives almost pure. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How many concentric pipes are used in the Frasch process?

- ◻️ Five  
  _↳ feedback if chosen: Three are enough: water in, air in, froth out._
- ◻️ Two  
  _↳ feedback if chosen: A third pipe is needed for the compressed air that lifts the froth._
- ✅ Three
- ◻️ One  
  _↳ feedback if chosen: One pipe could not carry water down and sulphur up at the same time._

Full working after a second miss:

> Superheated water goes down the outer pipe, hot compressed air down the inner one, and the froth rises up the middle one.  
> So the answer is Three.  

> How many concentric pipes are used in the Frasch process?

- ✅ Three
- ◻️ Five  
  _↳ feedback if chosen: Three are enough: water in, air in, froth out._
- ◻️ Two  
  _↳ feedback if chosen: A third pipe is needed for the compressed air that lifts the froth._
- ◻️ One  
  _↳ feedback if chosen: One pipe could not carry water down and sulphur up at the same time._

Full working after a second miss:

> Superheated water goes down the outer pipe, hot compressed air down the inner one, and the froth rises up the middle one.  
> So the answer is Three.  

> Why is sulphur from the Frasch process very pure?

- ◻️ It is crystallised from water  
  _↳ feedback if chosen: Sulphur is insoluble in water, so it cannot be crystallised from it._
- ◻️ It is washed with acid at the surface  
  _↳ feedback if chosen: No acid washing is used in the process._
- ◻️ It is purified later by distillation  
  _↳ feedback if chosen: No further purification is needed; it comes up about 99 per cent pure._
- ✅ Only the sulphur melts and is pushed up; the rock and sand stay behind

Full working after a second miss:

> Melting separates the sulphur from the rock underground, so it arrives almost pure.  
> So the answer is Only the sulphur melts and is pushed up; the rock and sand stay behind.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-1-ores` · Lesson 1 · matching, level 2

Prompt: Match each mineral to its formula.

Pairs (3 shown each time):

- Galena → **PbS**
- Zinc blende → **ZnS**
- Iron pyrites → **FeS₂**
- Gypsum → **CaSO₄**
- Barytes → **BaSO₄**


Three generated variants:

> Match each mineral to its formula.

Right-hand side (shuffled): ZnS · PbS · FeS₂
- Galena → **PbS**
- Zinc blende → **ZnS**
- Iron pyrites → **FeS₂**

Full working after a second miss:

> The right pairs are:  
> Galena → PbS  
> Zinc blende → ZnS  
> Iron pyrites → FeS₂  

> Match each mineral to its formula.

Right-hand side (shuffled): ZnS · FeS₂ · CaSO₄
- Zinc blende → **ZnS**
- Gypsum → **CaSO₄**
- Iron pyrites → **FeS₂**

Full working after a second miss:

> The right pairs are:  
> Zinc blende → ZnS  
> Gypsum → CaSO₄  
> Iron pyrites → FeS₂  

> Match each mineral to its formula.

Right-hand side (shuffled): CaSO₄ · PbS · ZnS
- Galena → **PbS**
- Gypsum → **CaSO₄**
- Zinc blende → **ZnS**

Full working after a second miss:

> The right pairs are:  
> Galena → PbS  
> Gypsum → CaSO₄  
> Zinc blende → ZnS  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-1-pure` · Lesson 1 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does the Frasch process give sulphur that needs no further purification? | Only the sulphur melts at that temperature, so the rock and sand are left behind underground | The sulphur is distilled as it rises · Acid is added to dissolve the impurities · The water washes all the impurities away | No distillation takes place; the separation happens by melting. · No acid is used in the Frasch process. · Sulphur is insoluble in water, and the impurities are not washed out by it. | Sulphur melts at about {115} °C but rock and sand do not, so only the sulphur is carried up. |
| Why is the Frasch process used instead of digging the sulphur out? | The beds lie under layers of loose, water-bearing rock that would collapse into a mine | Sulphur is too valuable to dig · Digging would set the sulphur on fire · The sulphur lies only a few metres down | Value is not the reason; the ground above the beds is. · Sulphur does not catch fire by itself when dug. · The beds lie a few HUNDRED metres down. | Pumping melted sulphur up through pipes avoids sinking a shaft through unsafe ground. |
| What happens to the molten sulphur when it reaches the surface? | It runs into large tanks and solidifies as it cools | It is burned at once to sulphur dioxide · It is dissolved in water for transport · It is distilled to separate the allotropes | Burning it would destroy the product; some is burned later, at the factory. · Sulphur is insoluble in water. · Allotropes are not separated by distillation; they are forms of the same element. | The froth is run into tanks, where the sulphur cools and sets as a solid ready for use. |
| Roughly how pure is the sulphur brought up by the Frasch process? | About {99} per cent pure | About {50} per cent pure · About {75} per cent pure · Less than {10} per cent pure | Half of the mass would be impurity, which melting underground avoids. · The purity is much higher than that. · That would be an ore, not the free element. | Because only the sulphur melts, almost nothing else comes up with it. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What happens to the molten sulphur when it reaches the surface?

- ◻️ It is dissolved in water for transport  
  _↳ feedback if chosen: Sulphur is insoluble in water._
- ✅ It runs into large tanks and solidifies as it cools
- ◻️ It is burned at once to sulphur dioxide  
  _↳ feedback if chosen: Burning it would destroy the product; some is burned later, at the factory._
- ◻️ It is distilled to separate the allotropes  
  _↳ feedback if chosen: Allotropes are not separated by distillation; they are forms of the same element._

Full working after a second miss:

> The froth is run into tanks, where the sulphur cools and sets as a solid ready for use.  
> So the answer is It runs into large tanks and solidifies as it cools.  

> What happens to the molten sulphur when it reaches the surface?

- ◻️ It is distilled to separate the allotropes  
  _↳ feedback if chosen: Allotropes are not separated by distillation; they are forms of the same element._
- ✅ It runs into large tanks and solidifies as it cools
- ◻️ It is dissolved in water for transport  
  _↳ feedback if chosen: Sulphur is insoluble in water._
- ◻️ It is burned at once to sulphur dioxide  
  _↳ feedback if chosen: Burning it would destroy the product; some is burned later, at the factory._

Full working after a second miss:

> The froth is run into tanks, where the sulphur cools and sets as a solid ready for use.  
> So the answer is It runs into large tanks and solidifies as it cools.  

> Why is the Frasch process used instead of digging the sulphur out?

- ◻️ Digging would set the sulphur on fire  
  _↳ feedback if chosen: Sulphur does not catch fire by itself when dug._
- ◻️ Sulphur is too valuable to dig  
  _↳ feedback if chosen: Value is not the reason; the ground above the beds is._
- ✅ The beds lie under layers of loose, water-bearing rock that would collapse into a mine
- ◻️ The sulphur lies only a few metres down  
  _↳ feedback if chosen: The beds lie a few HUNDRED metres down._

Full working after a second miss:

> Pumping melted sulphur up through pipes avoids sinking a shaft through unsafe ground.  
> So the answer is The beds lie under layers of loose, water-bearing rock that would collapse into a mine.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-1-pure-card` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does the Frasch process give sulphur that needs no further purification? | Only the sulphur melts at that temperature, so the rock and sand are left behind underground | The sulphur is distilled as it rises · Acid is added to dissolve the impurities · The water washes all the impurities away | No distillation takes place; the separation happens by melting. · No acid is used in the Frasch process. · Sulphur is insoluble in water, and the impurities are not washed out by it. | Sulphur melts at about {115} °C but rock and sand do not, so only the sulphur is carried up. |
| Why is the Frasch process used instead of digging the sulphur out? | The beds lie under layers of loose, water-bearing rock that would collapse into a mine | Sulphur is too valuable to dig · Digging would set the sulphur on fire · The sulphur lies only a few metres down | Value is not the reason; the ground above the beds is. · Sulphur does not catch fire by itself when dug. · The beds lie a few HUNDRED metres down. | Pumping melted sulphur up through pipes avoids sinking a shaft through unsafe ground. |
| What happens to the molten sulphur when it reaches the surface? | It runs into large tanks and solidifies as it cools | It is burned at once to sulphur dioxide · It is dissolved in water for transport · It is distilled to separate the allotropes | Burning it would destroy the product; some is burned later, at the factory. · Sulphur is insoluble in water. · Allotropes are not separated by distillation; they are forms of the same element. | The froth is run into tanks, where the sulphur cools and sets as a solid ready for use. |
| Roughly how pure is the sulphur brought up by the Frasch process? | About {99} per cent pure | About {50} per cent pure · About {75} per cent pure · Less than {10} per cent pure | Half of the mass would be impurity, which melting underground avoids. · The purity is much higher than that. · That would be an ore, not the free element. | Because only the sulphur melts, almost nothing else comes up with it. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does the Frasch process give sulphur that needs no further purification?

- ◻️ The water washes all the impurities away  
  _↳ feedback if chosen: Sulphur is insoluble in water, and the impurities are not washed out by it._
- ✅ Only the sulphur melts at that temperature, so the rock and sand are left behind underground
- ◻️ Acid is added to dissolve the impurities  
  _↳ feedback if chosen: No acid is used in the Frasch process._
- ◻️ The sulphur is distilled as it rises  
  _↳ feedback if chosen: No distillation takes place; the separation happens by melting._

Full working after a second miss:

> Sulphur melts at about 115 °C but rock and sand do not, so only the sulphur is carried up.  
> So the answer is Only the sulphur melts at that temperature, so the rock and sand are left behind underground.  

> Why does the Frasch process give sulphur that needs no further purification?

- ◻️ The sulphur is distilled as it rises  
  _↳ feedback if chosen: No distillation takes place; the separation happens by melting._
- ✅ Only the sulphur melts at that temperature, so the rock and sand are left behind underground
- ◻️ Acid is added to dissolve the impurities  
  _↳ feedback if chosen: No acid is used in the Frasch process._
- ◻️ The water washes all the impurities away  
  _↳ feedback if chosen: Sulphur is insoluble in water, and the impurities are not washed out by it._

Full working after a second miss:

> Sulphur melts at about 115 °C but rock and sand do not, so only the sulphur is carried up.  
> So the answer is Only the sulphur melts at that temperature, so the rock and sand are left behind underground.  

> Roughly how pure is the sulphur brought up by the Frasch process?

- ◻️ About 75 per cent pure  
  _↳ feedback if chosen: The purity is much higher than that._
- ✅ About 99 per cent pure
- ◻️ About 50 per cent pure  
  _↳ feedback if chosen: Half of the mass would be impurity, which melting underground avoids._
- ◻️ Less than 10 per cent pure  
  _↳ feedback if chosen: That would be an ore, not the free element._

Full working after a second miss:

> Because only the sulphur melts, almost nothing else comes up with it.  
> So the answer is About 99 per cent pure.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-2-allo` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What are allotropes? | Different forms of the same element in the same physical state | Different elements with the same properties · Compounds of one element with another · Atoms of one element with different numbers of neutrons | Allotropes are forms of ONE element, not different elements. · No other element is joined: an allotrope is still the pure element. · Those are isotopes, which differ in the nucleus, not in the arrangement of the atoms. | Rhombic and monoclinic sulphur are both pure solid sulphur, with the atoms packed differently. |
| Which allotrope of sulphur is stable below {96} °C? | Rhombic (alpha) sulphur | Monoclinic (beta) sulphur · Plastic sulphur · Both are equally stable | Monoclinic sulphur is the stable form between about {96} °C and the melting point. · Plastic sulphur is not stable at all: it slowly changes back to rhombic. · Only one form is stable at a given temperature. | Below the transition temperature of about {96} °C, rhombic sulphur is the stable form. |
| What shape are the crystals of monoclinic sulphur? | Long needle-shaped crystals | Octahedral crystals · Cubes · It has no crystals at all | Octahedral crystals are the rhombic form. · Neither allotrope of sulphur forms cubes. · Monoclinic sulphur does form crystals; it is plastic sulphur that has none. | Monoclinic sulphur grows as needles, while rhombic sulphur grows as octahedral crystals. |
| In which liquid does sulphur dissolve? | Carbon disulphide | Water · Dilute hydrochloric acid · Ethanol, very readily | Sulphur is insoluble in water. · Sulphur does not react with or dissolve in dilute acids. · Sulphur is only very slightly soluble in ethanol. | Sulphur is insoluble in water but dissolves well in carbon disulphide, which is how rhombic crystals are grown. |
| What is seen when sulphur burns in air? | A blue flame, giving a colourless gas with a choking smell | A bright white flame, giving a white solid · A yellow flame, giving a black solid · No reaction takes place | A bright white flame with a white solid is burning magnesium. · A black solid is not formed; the product is a gas. · Sulphur burns readily when heated in air. | Sulphur burns with a blue flame to give sulphur dioxide: S + {formula('O2')} → {formula('SO2')}. |
| How is plastic sulphur made? | By pouring boiling sulphur into cold water | By cooling molten sulphur very slowly · By dissolving sulphur in carbon disulphide and evaporating · By heating sulphur gently to just above its melting point | Slow cooling gives crystals, not the plastic form. · That method grows rhombic crystals. · Gentle melting gives a runny amber liquid, which sets back to a crystalline form. | Sudden cooling traps long chains of sulphur atoms, giving a brown rubbery solid that is not crystalline. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What are allotropes?

- ✅ Different forms of the same element in the same physical state
- ◻️ Compounds of one element with another  
  _↳ feedback if chosen: No other element is joined: an allotrope is still the pure element._
- ◻️ Different elements with the same properties  
  _↳ feedback if chosen: Allotropes are forms of ONE element, not different elements._
- ◻️ Atoms of one element with different numbers of neutrons  
  _↳ feedback if chosen: Those are isotopes, which differ in the nucleus, not in the arrangement of the atoms._

Full working after a second miss:

> Rhombic and monoclinic sulphur are both pure solid sulphur, with the atoms packed differently.  
> So the answer is Different forms of the same element in the same physical state.  

> How is plastic sulphur made?

- ✅ By pouring boiling sulphur into cold water
- ◻️ By heating sulphur gently to just above its melting point  
  _↳ feedback if chosen: Gentle melting gives a runny amber liquid, which sets back to a crystalline form._
- ◻️ By cooling molten sulphur very slowly  
  _↳ feedback if chosen: Slow cooling gives crystals, not the plastic form._
- ◻️ By dissolving sulphur in carbon disulphide and evaporating  
  _↳ feedback if chosen: That method grows rhombic crystals._

Full working after a second miss:

> Sudden cooling traps long chains of sulphur atoms, giving a brown rubbery solid that is not crystalline.  
> So the answer is By pouring boiling sulphur into cold water.  

> What are allotropes?

- ✅ Different forms of the same element in the same physical state
- ◻️ Atoms of one element with different numbers of neutrons  
  _↳ feedback if chosen: Those are isotopes, which differ in the nucleus, not in the arrangement of the atoms._
- ◻️ Different elements with the same properties  
  _↳ feedback if chosen: Allotropes are forms of ONE element, not different elements._
- ◻️ Compounds of one element with another  
  _↳ feedback if chosen: No other element is joined: an allotrope is still the pure element._

Full working after a second miss:

> Rhombic and monoclinic sulphur are both pure solid sulphur, with the atoms packed differently.  
> So the answer is Different forms of the same element in the same physical state.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-2-match` · Lesson 2 · matching, level 2

Prompt: Match each quantity to its value for sulphur.

Pairs (3 shown each time):

- Shape of rhombic crystals → **Octahedral**
- Shape of monoclinic crystals → **Needles**
- Density of rhombic sulphur → **2.07 g/cm³**
- Density of monoclinic sulphur → **1.98 g/cm³**
- Transition temperature → **About 96 °C**
- Melting point → **About 115 °C**


Three generated variants:

> Match each quantity to its value for sulphur.

Right-hand side (shuffled): 1.98 g/cm³ · About 96 °C · 2.07 g/cm³
- Density of rhombic sulphur → **2.07 g/cm³**
- Transition temperature → **About 96 °C**
- Density of monoclinic sulphur → **1.98 g/cm³**

Full working after a second miss:

> The right pairs are:  
> Density of rhombic sulphur → 2.07 g/cm³  
> Transition temperature → About 96 °C  
> Density of monoclinic sulphur → 1.98 g/cm³  

> Match each quantity to its value for sulphur.

Right-hand side (shuffled): 2.07 g/cm³ · 1.98 g/cm³ · About 115 °C
- Melting point → **About 115 °C**
- Density of rhombic sulphur → **2.07 g/cm³**
- Density of monoclinic sulphur → **1.98 g/cm³**

Full working after a second miss:

> The right pairs are:  
> Melting point → About 115 °C  
> Density of rhombic sulphur → 2.07 g/cm³  
> Density of monoclinic sulphur → 1.98 g/cm³  

> Match each quantity to its value for sulphur.

Right-hand side (shuffled): Octahedral · Needles · About 115 °C
- Shape of monoclinic crystals → **Needles**
- Shape of rhombic crystals → **Octahedral**
- Melting point → **About 115 °C**

Full working after a second miss:

> The right pairs are:  
> Shape of monoclinic crystals → Needles  
> Shape of rhombic crystals → Octahedral  
> Melting point → About 115 °C  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-2-burn` · Lesson 2 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Sulphur is heated in a deflagrating spoon and lowered into a gas jar of air. What is seen and formed? | A blue flame, forming sulphur dioxide, {formula('SO2')} | A yellow flame, forming sulphur trioxide, {formula('SO3')} · A white flame, forming a white solid · Nothing happens | {formula('SO3')} is made in the Contact process with a catalyst, not by burning sulphur in air. · The product is a gas, not a solid. · Heated sulphur burns in air with a clearly visible flame. | S + {formula('O2')} → {formula('SO2')}, with a blue flame and a choking smell. |
| Iron filings and sulphur are heated together. What is formed? | Iron(II) sulphide, {formula('FeS')}, a black solid | A mixture of iron and sulphur, unchanged · Iron(II) sulphate, {formula('FeSO4')} · Iron and sulphur dioxide | Heating makes them react; the product cannot be separated with a magnet. · No oxygen is present, so no sulphate can form. · No oxygen is present, so no {formula('SO2')} can form. | Fe + S → {formula('FeS')}: sulphur combines with many metals when heated. |
| What does sulphur do with dilute hydrochloric acid? | Nothing: sulphur does not react with dilute acids | It gives off hydrogen · It gives off hydrogen sulphide · It dissolves to give a yellow solution | Only metals above hydrogen give off hydrogen with a dilute acid. · That happens with a metal SULPHIDE, not with sulphur itself. · Sulphur is insoluble and unreactive towards dilute acids. | Sulphur reacts with hot concentrated acids, but not with dilute ones. |
| Why is a deflagrating spoon used to burn sulphur in a gas jar? | It holds the burning sulphur safely in the jar while the gas collects | It makes the sulphur burn more brightly · It stops the sulphur from melting · It dries the gas as it forms | The brightness depends on the sulphur and the air, not on the spoon. · The sulphur melts before it burns; the spoon holds the molten sulphur. · The spoon does not dry anything. | The long handle lets the burning sulphur be lowered into the jar and taken out safely. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Iron filings and sulphur are heated together. What is formed?

- ◻️ Iron(II) sulphate, FeSO₄  
  _↳ feedback if chosen: No oxygen is present, so no sulphate can form._
- ◻️ Iron and sulphur dioxide  
  _↳ feedback if chosen: No oxygen is present, so no SO₂ can form._
- ◻️ A mixture of iron and sulphur, unchanged  
  _↳ feedback if chosen: Heating makes them react; the product cannot be separated with a magnet._
- ✅ Iron(II) sulphide, FeS, a black solid

Full working after a second miss:

> Fe + S → FeS: sulphur combines with many metals when heated.  
> So the answer is Iron(II) sulphide, FeS, a black solid.  

> What does sulphur do with dilute hydrochloric acid?

- ✅ Nothing: sulphur does not react with dilute acids
- ◻️ It dissolves to give a yellow solution  
  _↳ feedback if chosen: Sulphur is insoluble and unreactive towards dilute acids._
- ◻️ It gives off hydrogen  
  _↳ feedback if chosen: Only metals above hydrogen give off hydrogen with a dilute acid._
- ◻️ It gives off hydrogen sulphide  
  _↳ feedback if chosen: That happens with a metal SULPHIDE, not with sulphur itself._

Full working after a second miss:

> Sulphur reacts with hot concentrated acids, but not with dilute ones.  
> So the answer is Nothing: sulphur does not react with dilute acids.  

> What does sulphur do with dilute hydrochloric acid?

- ◻️ It dissolves to give a yellow solution  
  _↳ feedback if chosen: Sulphur is insoluble and unreactive towards dilute acids._
- ✅ Nothing: sulphur does not react with dilute acids
- ◻️ It gives off hydrogen  
  _↳ feedback if chosen: Only metals above hydrogen give off hydrogen with a dilute acid._
- ◻️ It gives off hydrogen sulphide  
  _↳ feedback if chosen: That happens with a metal SULPHIDE, not with sulphur itself._

Full working after a second miss:

> Sulphur reacts with hot concentrated acids, but not with dilute ones.  
> So the answer is Nothing: sulphur does not react with dilute acids.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-2-why` · Lesson 2 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Rhombic and monoclinic sulphur are both pure sulphur, yet their densities and crystal shapes differ. Why? | The same atoms are packed in a different arrangement in each crystal | They contain different numbers of neutrons · One of them contains a little oxygen · They are different elements | Different numbers of neutrons give isotopes, which have the same crystal forms. · Both allotropes are pure sulphur; neither contains oxygen. · Allotropes are forms of ONE element, not different elements. | Both are rings of {8} sulphur atoms, but the rings are stacked differently. |
| Monoclinic sulphur is left at room temperature for several weeks. What happens? | It slowly changes into rhombic sulphur, the stable form below {96} °C | It stays monoclinic for ever · It changes into plastic sulphur · It melts | Below the transition temperature the monoclinic form is not stable. · Plastic sulphur comes from pouring boiling sulphur into cold water. · Sulphur melts at about {115} °C, far above room temperature. | An allotrope changes into whichever form is stable at that temperature, though slowly. |
| How are crystals of rhombic sulphur grown in the laboratory? | By dissolving sulphur in carbon disulphide and letting the liquid evaporate slowly | By dissolving sulphur in hot water and cooling it · By pouring boiling sulphur into cold water · By heating sulphur until it glows | Sulphur is insoluble in water, so no solution can be made. · That gives plastic sulphur, which has no crystals. · Heating alone does not grow crystals. | As the solvent evaporates below {96} °C, octahedral rhombic crystals are left. |
| Why does plastic sulphur slowly harden and turn yellow again? | The long chains of atoms slowly rearrange into stable rhombic crystals | It takes in oxygen from the air · It loses water · It reacts with the carbon dioxide in air | No oxygen is taken in; the element stays pure sulphur. · There is no water in plastic sulphur to lose. · Sulphur does not react with carbon dioxide. | Plastic sulphur is unstable, so its atoms return to the arrangement of the stable rhombic form. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How are crystals of rhombic sulphur grown in the laboratory?

- ◻️ By pouring boiling sulphur into cold water  
  _↳ feedback if chosen: That gives plastic sulphur, which has no crystals._
- ◻️ By dissolving sulphur in hot water and cooling it  
  _↳ feedback if chosen: Sulphur is insoluble in water, so no solution can be made._
- ◻️ By heating sulphur until it glows  
  _↳ feedback if chosen: Heating alone does not grow crystals._
- ✅ By dissolving sulphur in carbon disulphide and letting the liquid evaporate slowly

Full working after a second miss:

> As the solvent evaporates below 96 °C, octahedral rhombic crystals are left.  
> So the answer is By dissolving sulphur in carbon disulphide and letting the liquid evaporate slowly.  

> Monoclinic sulphur is left at room temperature for several weeks. What happens?

- ◻️ It stays monoclinic for ever  
  _↳ feedback if chosen: Below the transition temperature the monoclinic form is not stable._
- ◻️ It melts  
  _↳ feedback if chosen: Sulphur melts at about 115 °C, far above room temperature._
- ◻️ It changes into plastic sulphur  
  _↳ feedback if chosen: Plastic sulphur comes from pouring boiling sulphur into cold water._
- ✅ It slowly changes into rhombic sulphur, the stable form below 96 °C

Full working after a second miss:

> An allotrope changes into whichever form is stable at that temperature, though slowly.  
> So the answer is It slowly changes into rhombic sulphur, the stable form below 96 °C.  

> Monoclinic sulphur is left at room temperature for several weeks. What happens?

- ◻️ It stays monoclinic for ever  
  _↳ feedback if chosen: Below the transition temperature the monoclinic form is not stable._
- ◻️ It melts  
  _↳ feedback if chosen: Sulphur melts at about 115 °C, far above room temperature._
- ◻️ It changes into plastic sulphur  
  _↳ feedback if chosen: Plastic sulphur comes from pouring boiling sulphur into cold water._
- ✅ It slowly changes into rhombic sulphur, the stable form below 96 °C

Full working after a second miss:

> An allotrope changes into whichever form is stable at that temperature, though slowly.  
> So the answer is It slowly changes into rhombic sulphur, the stable form below 96 °C.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-2-burn-card` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Sulphur is heated in a deflagrating spoon and lowered into a gas jar of air. What is seen and formed? | A blue flame, forming sulphur dioxide, {formula('SO2')} | A yellow flame, forming sulphur trioxide, {formula('SO3')} · A white flame, forming a white solid · Nothing happens | {formula('SO3')} is made in the Contact process with a catalyst, not by burning sulphur in air. · The product is a gas, not a solid. · Heated sulphur burns in air with a clearly visible flame. | S + {formula('O2')} → {formula('SO2')}, with a blue flame and a choking smell. |
| Iron filings and sulphur are heated together. What is formed? | Iron(II) sulphide, {formula('FeS')}, a black solid | A mixture of iron and sulphur, unchanged · Iron(II) sulphate, {formula('FeSO4')} · Iron and sulphur dioxide | Heating makes them react; the product cannot be separated with a magnet. · No oxygen is present, so no sulphate can form. · No oxygen is present, so no {formula('SO2')} can form. | Fe + S → {formula('FeS')}: sulphur combines with many metals when heated. |
| What does sulphur do with dilute hydrochloric acid? | Nothing: sulphur does not react with dilute acids | It gives off hydrogen · It gives off hydrogen sulphide · It dissolves to give a yellow solution | Only metals above hydrogen give off hydrogen with a dilute acid. · That happens with a metal SULPHIDE, not with sulphur itself. · Sulphur is insoluble and unreactive towards dilute acids. | Sulphur reacts with hot concentrated acids, but not with dilute ones. |
| Why is a deflagrating spoon used to burn sulphur in a gas jar? | It holds the burning sulphur safely in the jar while the gas collects | It makes the sulphur burn more brightly · It stops the sulphur from melting · It dries the gas as it forms | The brightness depends on the sulphur and the air, not on the spoon. · The sulphur melts before it burns; the spoon holds the molten sulphur. · The spoon does not dry anything. | The long handle lets the burning sulphur be lowered into the jar and taken out safely. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does sulphur do with dilute hydrochloric acid?

- ◻️ It gives off hydrogen sulphide  
  _↳ feedback if chosen: That happens with a metal SULPHIDE, not with sulphur itself._
- ✅ Nothing: sulphur does not react with dilute acids
- ◻️ It dissolves to give a yellow solution  
  _↳ feedback if chosen: Sulphur is insoluble and unreactive towards dilute acids._
- ◻️ It gives off hydrogen  
  _↳ feedback if chosen: Only metals above hydrogen give off hydrogen with a dilute acid._

Full working after a second miss:

> Sulphur reacts with hot concentrated acids, but not with dilute ones.  
> So the answer is Nothing: sulphur does not react with dilute acids.  

> What does sulphur do with dilute hydrochloric acid?

- ◻️ It gives off hydrogen sulphide  
  _↳ feedback if chosen: That happens with a metal SULPHIDE, not with sulphur itself._
- ◻️ It gives off hydrogen  
  _↳ feedback if chosen: Only metals above hydrogen give off hydrogen with a dilute acid._
- ✅ Nothing: sulphur does not react with dilute acids
- ◻️ It dissolves to give a yellow solution  
  _↳ feedback if chosen: Sulphur is insoluble and unreactive towards dilute acids._

Full working after a second miss:

> Sulphur reacts with hot concentrated acids, but not with dilute ones.  
> So the answer is Nothing: sulphur does not react with dilute acids.  

> Sulphur is heated in a deflagrating spoon and lowered into a gas jar of air. What is seen and formed?

- ✅ A blue flame, forming sulphur dioxide, SO₂
- ◻️ A white flame, forming a white solid  
  _↳ feedback if chosen: The product is a gas, not a solid._
- ◻️ A yellow flame, forming sulphur trioxide, SO₃  
  _↳ feedback if chosen: SO₃ is made in the Contact process with a catalyst, not by burning sulphur in air._
- ◻️ Nothing happens  
  _↳ feedback if chosen: Heated sulphur burns in air with a clearly visible flame._

Full working after a second miss:

> S + O₂ → SO₂, with a blue flame and a choking smell.  
> So the answer is A blue flame, forming sulphur dioxide, SO₂.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-3-prep` · Lesson 3 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which reagents are used to prepare sulphur dioxide in the laboratory? | Sodium sulphite and dilute hydrochloric acid | Sodium sulphate and dilute hydrochloric acid · Sodium sulphide and dilute hydrochloric acid · Sodium carbonate and dilute hydrochloric acid | A sulphate does not give off {formula('SO2')} with a dilute acid; a sulphite does. · A sulphide gives hydrogen sulphide, {formula('H2S')}, not {formula('SO2')}. · A carbonate gives carbon dioxide. | {formula('Na2SO3')} + {2}{formula('HCl')} → {2}{formula('NaCl')} + {formula('H2O')} + {formula('SO2')}. |
| How is sulphur dioxide collected? | By downward delivery, because it is denser than air | By downward displacement of water · Over water · By upward delivery, because it is less dense than air | {formula('SO2')} is very soluble in water, so it cannot be collected over or through water. · It would dissolve in the water. · Its relative molecular mass is {64}, well above the average for air, so it is denser. | A dense, very soluble gas is collected by downward delivery into a dry gas jar. |
| Which drying agent is used for sulphur dioxide? | Concentrated sulphuric acid | Quicklime, {formula('CaO')} · Sodium hydroxide pellets · Water | Quicklime is basic and would react with the acidic gas. · Sodium hydroxide is a base and would absorb the gas. · Water dissolves the gas instead of drying it. | An acidic gas is dried with concentrated sulphuric acid, which does not react with it. |
| What is the smell and colour of sulphur dioxide? | Colourless, with a sharp choking smell | Brown, with a choking smell · Colourless, with a smell of rotten eggs · Yellow and odourless | Brown is the colour of nitrogen dioxide. · Rotten eggs is the smell of hydrogen sulphide. · Sulphur dioxide is colourless and certainly not odourless. | {formula('SO2')} is a colourless, poisonous gas with a sharp choking smell. |
| Why must sulphur dioxide be prepared in a fume cupboard? | It is poisonous and irritates the eyes and lungs | It catches fire easily · It explodes on contact with air · It is only a nuisance because of its colour | Sulphur dioxide does not burn; it is itself a product of burning. · It does not explode in air. · The gas is colourless; the danger is that it is poisonous. | Breathing it in damages the lungs, so it must be used where the fumes can be drawn away. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How is sulphur dioxide collected?

- ◻️ By downward displacement of water  
  _↳ feedback if chosen: SO₂ is very soluble in water, so it cannot be collected over or through water._
- ✅ By downward delivery, because it is denser than air
- ◻️ By upward delivery, because it is less dense than air  
  _↳ feedback if chosen: Its relative molecular mass is 64, well above the average for air, so it is denser._
- ◻️ Over water  
  _↳ feedback if chosen: It would dissolve in the water._

Full working after a second miss:

> A dense, very soluble gas is collected by downward delivery into a dry gas jar.  
> So the answer is By downward delivery, because it is denser than air.  

> Which reagents are used to prepare sulphur dioxide in the laboratory?

- ✅ Sodium sulphite and dilute hydrochloric acid
- ◻️ Sodium carbonate and dilute hydrochloric acid  
  _↳ feedback if chosen: A carbonate gives carbon dioxide._
- ◻️ Sodium sulphide and dilute hydrochloric acid  
  _↳ feedback if chosen: A sulphide gives hydrogen sulphide, H₂S, not SO₂._
- ◻️ Sodium sulphate and dilute hydrochloric acid  
  _↳ feedback if chosen: A sulphate does not give off SO₂ with a dilute acid; a sulphite does._

Full working after a second miss:

> Na₂SO₃ + 2HCl → 2NaCl + H₂O + SO₂.  
> So the answer is Sodium sulphite and dilute hydrochloric acid.  

> Why must sulphur dioxide be prepared in a fume cupboard?

- ✅ It is poisonous and irritates the eyes and lungs
- ◻️ It catches fire easily  
  _↳ feedback if chosen: Sulphur dioxide does not burn; it is itself a product of burning._
- ◻️ It is only a nuisance because of its colour  
  _↳ feedback if chosen: The gas is colourless; the danger is that it is poisonous._
- ◻️ It explodes on contact with air  
  _↳ feedback if chosen: It does not explode in air._

Full working after a second miss:

> Breathing it in damages the lungs, so it must be used where the fumes can be drawn away.  
> So the answer is It is poisonous and irritates the eyes and lungs.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-3-dry` · Lesson 3 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is quicklime, {formula('CaO')}, not used to dry sulphur dioxide? | Quicklime is basic and reacts with the acidic gas | Quicklime is not a drying agent at all · Quicklime would make the gas wetter · Quicklime dissolves the gas in water | Quicklime IS a drying agent; it is used for ammonia. The problem here is that it reacts. · A drying agent removes water; quicklime does not add any. · Quicklime reacts with the gas; it does not dissolve it in water. | An acidic gas must be dried with an acidic drying agent, such as concentrated sulphuric acid. |
| Which drying agent is used for ammonia, and why? | Quicklime, because ammonia is alkaline and would react with an acidic drying agent | Concentrated sulphuric acid, because it dries every gas · Water, because ammonia dissolves in it · No drying agent can be used with ammonia | Concentrated sulphuric acid reacts with ammonia to give ammonium sulphate. · Water dissolves ammonia instead of drying it. · Quicklime dries it well. | A drying agent must not react with the gas: a basic gas needs a basic drying agent. |
| A gas is passed through a wash bottle of concentrated sulphuric acid. What is this for? | To remove water vapour from the gas | To cool the gas · To make the gas more soluble · To change the gas into an acid | Cooling is not the purpose, and the acid does not cool the gas. · Drying does not change how soluble the gas is. · The acid does not react with a gas it is used to dry. | Concentrated sulphuric acid takes up water strongly, which is why it is a drying agent. |
| Why must the gas jar be dry when sulphur dioxide is collected? | The gas is very soluble, so any water in the jar would dissolve some of it | Water would make the gas explode · A wet jar would crack · Water would turn the gas brown | Sulphur dioxide does not explode with water; it dissolves. · The jar does not crack; the problem is loss of the gas. · Sulphur dioxide stays colourless in water; it forms sulphurous acid. | {formula('SO2')} is very soluble in water, so a wet jar would hold less gas. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which drying agent is used for ammonia, and why?

- ✅ Quicklime, because ammonia is alkaline and would react with an acidic drying agent
- ◻️ Concentrated sulphuric acid, because it dries every gas  
  _↳ feedback if chosen: Concentrated sulphuric acid reacts with ammonia to give ammonium sulphate._
- ◻️ Water, because ammonia dissolves in it  
  _↳ feedback if chosen: Water dissolves ammonia instead of drying it._
- ◻️ No drying agent can be used with ammonia  
  _↳ feedback if chosen: Quicklime dries it well._

Full working after a second miss:

> A drying agent must not react with the gas: a basic gas needs a basic drying agent.  
> So the answer is Quicklime, because ammonia is alkaline and would react with an acidic drying agent.  

> Which drying agent is used for ammonia, and why?

- ◻️ No drying agent can be used with ammonia  
  _↳ feedback if chosen: Quicklime dries it well._
- ✅ Quicklime, because ammonia is alkaline and would react with an acidic drying agent
- ◻️ Concentrated sulphuric acid, because it dries every gas  
  _↳ feedback if chosen: Concentrated sulphuric acid reacts with ammonia to give ammonium sulphate._
- ◻️ Water, because ammonia dissolves in it  
  _↳ feedback if chosen: Water dissolves ammonia instead of drying it._

Full working after a second miss:

> A drying agent must not react with the gas: a basic gas needs a basic drying agent.  
> So the answer is Quicklime, because ammonia is alkaline and would react with an acidic drying agent.  

> Why is quicklime, CaO, not used to dry sulphur dioxide?

- ◻️ Quicklime would make the gas wetter  
  _↳ feedback if chosen: A drying agent removes water; quicklime does not add any._
- ✅ Quicklime is basic and reacts with the acidic gas
- ◻️ Quicklime is not a drying agent at all  
  _↳ feedback if chosen: Quicklime IS a drying agent; it is used for ammonia. The problem here is that it reacts._
- ◻️ Quicklime dissolves the gas in water  
  _↳ feedback if chosen: Quicklime reacts with the gas; it does not dissolve it in water._

Full working after a second miss:

> An acidic gas must be dried with an acidic drying agent, such as concentrated sulphuric acid.  
> So the answer is Quicklime is basic and reacts with the acidic gas.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-3-dry-card` · Lesson 3 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is quicklime, {formula('CaO')}, not used to dry sulphur dioxide? | Quicklime is basic and reacts with the acidic gas | Quicklime is not a drying agent at all · Quicklime would make the gas wetter · Quicklime dissolves the gas in water | Quicklime IS a drying agent; it is used for ammonia. The problem here is that it reacts. · A drying agent removes water; quicklime does not add any. · Quicklime reacts with the gas; it does not dissolve it in water. | An acidic gas must be dried with an acidic drying agent, such as concentrated sulphuric acid. |
| Which drying agent is used for ammonia, and why? | Quicklime, because ammonia is alkaline and would react with an acidic drying agent | Concentrated sulphuric acid, because it dries every gas · Water, because ammonia dissolves in it · No drying agent can be used with ammonia | Concentrated sulphuric acid reacts with ammonia to give ammonium sulphate. · Water dissolves ammonia instead of drying it. · Quicklime dries it well. | A drying agent must not react with the gas: a basic gas needs a basic drying agent. |
| A gas is passed through a wash bottle of concentrated sulphuric acid. What is this for? | To remove water vapour from the gas | To cool the gas · To make the gas more soluble · To change the gas into an acid | Cooling is not the purpose, and the acid does not cool the gas. · Drying does not change how soluble the gas is. · The acid does not react with a gas it is used to dry. | Concentrated sulphuric acid takes up water strongly, which is why it is a drying agent. |
| Why must the gas jar be dry when sulphur dioxide is collected? | The gas is very soluble, so any water in the jar would dissolve some of it | Water would make the gas explode · A wet jar would crack · Water would turn the gas brown | Sulphur dioxide does not explode with water; it dissolves. · The jar does not crack; the problem is loss of the gas. · Sulphur dioxide stays colourless in water; it forms sulphurous acid. | {formula('SO2')} is very soluble in water, so a wet jar would hold less gas. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why must the gas jar be dry when sulphur dioxide is collected?

- ✅ The gas is very soluble, so any water in the jar would dissolve some of it
- ◻️ A wet jar would crack  
  _↳ feedback if chosen: The jar does not crack; the problem is loss of the gas._
- ◻️ Water would make the gas explode  
  _↳ feedback if chosen: Sulphur dioxide does not explode with water; it dissolves._
- ◻️ Water would turn the gas brown  
  _↳ feedback if chosen: Sulphur dioxide stays colourless in water; it forms sulphurous acid._

Full working after a second miss:

> SO₂ is very soluble in water, so a wet jar would hold less gas.  
> So the answer is The gas is very soluble, so any water in the jar would dissolve some of it.  

> Why must the gas jar be dry when sulphur dioxide is collected?

- ◻️ Water would make the gas explode  
  _↳ feedback if chosen: Sulphur dioxide does not explode with water; it dissolves._
- ◻️ A wet jar would crack  
  _↳ feedback if chosen: The jar does not crack; the problem is loss of the gas._
- ◻️ Water would turn the gas brown  
  _↳ feedback if chosen: Sulphur dioxide stays colourless in water; it forms sulphurous acid._
- ✅ The gas is very soluble, so any water in the jar would dissolve some of it

Full working after a second miss:

> SO₂ is very soluble in water, so a wet jar would hold less gas.  
> So the answer is The gas is very soluble, so any water in the jar would dissolve some of it.  

> Why must the gas jar be dry when sulphur dioxide is collected?

- ◻️ Water would make the gas explode  
  _↳ feedback if chosen: Sulphur dioxide does not explode with water; it dissolves._
- ✅ The gas is very soluble, so any water in the jar would dissolve some of it
- ◻️ A wet jar would crack  
  _↳ feedback if chosen: The jar does not crack; the problem is loss of the gas._
- ◻️ Water would turn the gas brown  
  _↳ feedback if chosen: Sulphur dioxide stays colourless in water; it forms sulphurous acid._

Full working after a second miss:

> SO₂ is very soluble in water, so a wet jar would hold less gas.  
> So the answer is The gas is very soluble, so any water in the jar would dissolve some of it.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-4-chem` · Lesson 4 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does sulphur dioxide form when it dissolves in water? | Sulphurous acid, {formula('H2SO3')} | Sulphuric acid, {formula('H2SO4')} · Hydrogen sulphide, {formula('H2S')} · A neutral solution | Sulphuric acid comes from sulphur TRIoxide dissolving in water. · Hydrogen sulphide is a different compound, made from a sulphide and an acid. · The solution turns blue litmus red, so it is acidic. | {formula('SO2')} + {formula('H2O')} → {formula('H2SO3')}: an acidic oxide gives an acid. |
| What happens when sulphur dioxide is bubbled into acidified potassium manganate(VII) solution? | The purple colour disappears, because the {formula('SO2')} reduces it | The solution turns a deeper purple · The solution turns brown · Nothing happens | Reduction removes the purple colour; it does not deepen it. · Brown is what happens with bromine water, not with manganate(VII). · The colour change is clear and is used as a test. | {formula('SO2')} is a reducing agent: it is itself oxidised to a sulphate while the purple ion is reduced. |
| Why is the bleaching by sulphur dioxide called temporary? | The colour slowly returns as air oxidises the bleached material | The bleaching only works in the dark · The material is destroyed rather than bleached · It only works on cotton | Light is not what undoes it; oxygen from the air is. · The material is not destroyed; its colour is removed and then returns. · It works on wool, silk, straw and paper as well. | {formula('SO2')} bleaches by reduction, and oxygen in the air slowly reverses the change. |
| How does bleaching by sulphur dioxide differ from bleaching by chlorine? | Sulphur dioxide bleaches by reduction; chlorine bleaches by oxidation | Both bleach by oxidation · Both bleach by reduction · Sulphur dioxide bleaches by oxidation and chlorine by reduction | Chlorine bleaches by oxidation, but sulphur dioxide does not. · Chlorine is an oxidising bleach, not a reducing one. · It is the other way round. | That is why the bleaching by {formula('SO2')} is temporary and that by chlorine is permanent. |
| Sulphur dioxide is bubbled through hydrogen sulphide. What is seen? | A yellow deposit of sulphur forms | A white precipitate forms · The mixture turns blue · No change is seen | No white precipitate is formed in this reaction. · No blue colour appears. · A pale yellow solid appears clearly. | {formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}: here {formula('SO2')} acts as the oxidising agent. |
| Which gas is mainly responsible for acid rain from burning coal? | Sulphur dioxide | Carbon dioxide · Nitrogen · Oxygen | Carbon dioxide makes rain only very slightly acidic; it is not the main cause of acid rain. · Nitrogen in the air is unreactive and does not itself cause acid rain. · Oxygen is neutral. | {formula('SO2')} from the sulphur in coal dissolves in rain and is oxidised to sulphuric acid. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How does bleaching by sulphur dioxide differ from bleaching by chlorine?

- ◻️ Both bleach by oxidation  
  _↳ feedback if chosen: Chlorine bleaches by oxidation, but sulphur dioxide does not._
- ✅ Sulphur dioxide bleaches by reduction; chlorine bleaches by oxidation
- ◻️ Both bleach by reduction  
  _↳ feedback if chosen: Chlorine is an oxidising bleach, not a reducing one._
- ◻️ Sulphur dioxide bleaches by oxidation and chlorine by reduction  
  _↳ feedback if chosen: It is the other way round._

Full working after a second miss:

> That is why the bleaching by SO₂ is temporary and that by chlorine is permanent.  
> So the answer is Sulphur dioxide bleaches by reduction; chlorine bleaches by oxidation.  

> Sulphur dioxide is bubbled through hydrogen sulphide. What is seen?

- ◻️ A white precipitate forms  
  _↳ feedback if chosen: No white precipitate is formed in this reaction._
- ◻️ The mixture turns blue  
  _↳ feedback if chosen: No blue colour appears._
- ◻️ No change is seen  
  _↳ feedback if chosen: A pale yellow solid appears clearly._
- ✅ A yellow deposit of sulphur forms

Full working after a second miss:

> SO₂ + 2H₂S → 3S + 2H₂O: here SO₂ acts as the oxidising agent.  
> So the answer is A yellow deposit of sulphur forms.  

> Which gas is mainly responsible for acid rain from burning coal?

- ◻️ Carbon dioxide  
  _↳ feedback if chosen: Carbon dioxide makes rain only very slightly acidic; it is not the main cause of acid rain._
- ✅ Sulphur dioxide
- ◻️ Oxygen  
  _↳ feedback if chosen: Oxygen is neutral._
- ◻️ Nitrogen  
  _↳ feedback if chosen: Nitrogen in the air is unreactive and does not itself cause acid rain._

Full working after a second miss:

> SO₂ from the sulphur in coal dissolves in rain and is oxidised to sulphuric acid.  
> So the answer is Sulphur dioxide.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-4-bleach` · Lesson 4 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A red flower is held in moist sulphur dioxide and loses its colour. It is then left in the air for some days. What happens? | The colour slowly returns, because the bleaching by {formula('SO2')} is temporary | The flower stays white for ever · The flower turns black · The colour returns at once | Permanent bleaching is what chlorine does, by oxidation. · Blackening is what concentrated sulphuric acid does to sugar, by dehydration. · The change back takes days, because oxidation by air is slow. | {formula('SO2')} bleaches by reduction, and oxygen in the air slowly reverses it. |
| Why must the material be moist for sulphur dioxide to bleach it? | The gas must dissolve in the water to act on the colouring matter | Water is what does the bleaching · Dry material would catch fire · The water washes the colour away | Water alone does not remove the colour of a flower. · Nothing catches fire in this test. · Washing is not the effect: the colour is removed chemically, and later returns. | Moisture lets the gas form sulphurous acid at the surface, and that is the reducing agent. |
| Which bleach is used for cotton cloth, and why not sulphur dioxide? | Chlorine or a chlorine compound, because its bleaching is permanent | Sulphur dioxide, because it is cheaper · Neither: cotton cannot be bleached · Sulphur dioxide, because it is permanent | Cheapness does not help if the colour returns. · Cotton is bleached in large amounts in industry. · Bleaching by {formula('SO2')} is temporary, not permanent. | Chlorine bleaches by oxidation, which the air cannot reverse; sulphur dioxide bleaches by reduction. |
| Why is sulphur dioxide still used to bleach straw, wool and paper? | Chlorine would attack and weaken those materials, while sulphur dioxide does not | It is the only bleach that works on them · It makes them stronger · Its bleaching lasts longer than chlorine's | Other bleaches exist, but they damage these materials. · Bleaching does not strengthen a material. · Its bleaching lasts a shorter time, not longer. | A gentle reducing bleach is chosen where an oxidising bleach would damage the fibres. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is sulphur dioxide still used to bleach straw, wool and paper?

- ◻️ It makes them stronger  
  _↳ feedback if chosen: Bleaching does not strengthen a material._
- ◻️ It is the only bleach that works on them  
  _↳ feedback if chosen: Other bleaches exist, but they damage these materials._
- ✅ Chlorine would attack and weaken those materials, while sulphur dioxide does not
- ◻️ Its bleaching lasts longer than chlorine's  
  _↳ feedback if chosen: Its bleaching lasts a shorter time, not longer._

Full working after a second miss:

> A gentle reducing bleach is chosen where an oxidising bleach would damage the fibres.  
> So the answer is Chlorine would attack and weaken those materials, while sulphur dioxide does not.  

> A red flower is held in moist sulphur dioxide and loses its colour. It is then left in the air for some days. What happens?

- ◻️ The colour returns at once  
  _↳ feedback if chosen: The change back takes days, because oxidation by air is slow._
- ✅ The colour slowly returns, because the bleaching by SO₂ is temporary
- ◻️ The flower turns black  
  _↳ feedback if chosen: Blackening is what concentrated sulphuric acid does to sugar, by dehydration._
- ◻️ The flower stays white for ever  
  _↳ feedback if chosen: Permanent bleaching is what chlorine does, by oxidation._

Full working after a second miss:

> SO₂ bleaches by reduction, and oxygen in the air slowly reverses it.  
> So the answer is The colour slowly returns, because the bleaching by SO₂ is temporary.  

> Which bleach is used for cotton cloth, and why not sulphur dioxide?

- ✅ Chlorine or a chlorine compound, because its bleaching is permanent
- ◻️ Sulphur dioxide, because it is cheaper  
  _↳ feedback if chosen: Cheapness does not help if the colour returns._
- ◻️ Neither: cotton cannot be bleached  
  _↳ feedback if chosen: Cotton is bleached in large amounts in industry._
- ◻️ Sulphur dioxide, because it is permanent  
  _↳ feedback if chosen: Bleaching by SO₂ is temporary, not permanent._

Full working after a second miss:

> Chlorine bleaches by oxidation, which the air cannot reverse; sulphur dioxide bleaches by reduction.  
> So the answer is Chlorine or a chlorine compound, because its bleaching is permanent.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-4-match` · Lesson 4 · matching, level 3

Prompt: Match each observation to what is formed or seen.

Pairs (3 shown each time):

- SO₂ dissolved in water → **Sulphurous acid, H₂SO₃**
- SO₂ passed into sodium hydroxide solution → **Sodium sulphite, Na₂SO₃**
- SO₂ bubbled into acidified manganate(VII) → **The purple colour disappears**
- SO₂ bubbled into acidified dichromate(VI) → **Orange changes to green**
- SO₂ mixed with H₂S → **A yellow deposit of sulphur**


Three generated variants:

> Match each observation to what is formed or seen.

Right-hand side (shuffled): Sulphurous acid, H₂SO₃ · Orange changes to green · The purple colour disappears
- SO₂ bubbled into acidified dichromate(VI) → **Orange changes to green**
- SO₂ dissolved in water → **Sulphurous acid, H₂SO₃**
- SO₂ bubbled into acidified manganate(VII) → **The purple colour disappears**

Full working after a second miss:

> The right pairs are:  
> SO₂ bubbled into acidified dichromate(VI) → Orange changes to green  
> SO₂ dissolved in water → Sulphurous acid, H₂SO₃  
> SO₂ bubbled into acidified manganate(VII) → The purple colour disappears  

> Match each observation to what is formed or seen.

Right-hand side (shuffled): A yellow deposit of sulphur · Sodium sulphite, Na₂SO₃ · Orange changes to green
- SO₂ passed into sodium hydroxide solution → **Sodium sulphite, Na₂SO₃**
- SO₂ mixed with H₂S → **A yellow deposit of sulphur**
- SO₂ bubbled into acidified dichromate(VI) → **Orange changes to green**

Full working after a second miss:

> The right pairs are:  
> SO₂ passed into sodium hydroxide solution → Sodium sulphite, Na₂SO₃  
> SO₂ mixed with H₂S → A yellow deposit of sulphur  
> SO₂ bubbled into acidified dichromate(VI) → Orange changes to green  

> Match each observation to what is formed or seen.

Right-hand side (shuffled): Orange changes to green · The purple colour disappears · Sulphurous acid, H₂SO₃
- SO₂ dissolved in water → **Sulphurous acid, H₂SO₃**
- SO₂ bubbled into acidified dichromate(VI) → **Orange changes to green**
- SO₂ bubbled into acidified manganate(VII) → **The purple colour disappears**

Full working after a second miss:

> The right pairs are:  
> SO₂ dissolved in water → Sulphurous acid, H₂SO₃  
> SO₂ bubbled into acidified dichromate(VI) → Orange changes to green  
> SO₂ bubbled into acidified manganate(VII) → The purple colour disappears  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-4-bleach-card` · Lesson 4 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A red flower is held in moist sulphur dioxide and loses its colour. It is then left in the air for some days. What happens? | The colour slowly returns, because the bleaching by {formula('SO2')} is temporary | The flower stays white for ever · The flower turns black · The colour returns at once | Permanent bleaching is what chlorine does, by oxidation. · Blackening is what concentrated sulphuric acid does to sugar, by dehydration. · The change back takes days, because oxidation by air is slow. | {formula('SO2')} bleaches by reduction, and oxygen in the air slowly reverses it. |
| Why must the material be moist for sulphur dioxide to bleach it? | The gas must dissolve in the water to act on the colouring matter | Water is what does the bleaching · Dry material would catch fire · The water washes the colour away | Water alone does not remove the colour of a flower. · Nothing catches fire in this test. · Washing is not the effect: the colour is removed chemically, and later returns. | Moisture lets the gas form sulphurous acid at the surface, and that is the reducing agent. |
| Which bleach is used for cotton cloth, and why not sulphur dioxide? | Chlorine or a chlorine compound, because its bleaching is permanent | Sulphur dioxide, because it is cheaper · Neither: cotton cannot be bleached · Sulphur dioxide, because it is permanent | Cheapness does not help if the colour returns. · Cotton is bleached in large amounts in industry. · Bleaching by {formula('SO2')} is temporary, not permanent. | Chlorine bleaches by oxidation, which the air cannot reverse; sulphur dioxide bleaches by reduction. |
| Why is sulphur dioxide still used to bleach straw, wool and paper? | Chlorine would attack and weaken those materials, while sulphur dioxide does not | It is the only bleach that works on them · It makes them stronger · Its bleaching lasts longer than chlorine's | Other bleaches exist, but they damage these materials. · Bleaching does not strengthen a material. · Its bleaching lasts a shorter time, not longer. | A gentle reducing bleach is chosen where an oxidising bleach would damage the fibres. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which bleach is used for cotton cloth, and why not sulphur dioxide?

- ◻️ Neither: cotton cannot be bleached  
  _↳ feedback if chosen: Cotton is bleached in large amounts in industry._
- ◻️ Sulphur dioxide, because it is cheaper  
  _↳ feedback if chosen: Cheapness does not help if the colour returns._
- ✅ Chlorine or a chlorine compound, because its bleaching is permanent
- ◻️ Sulphur dioxide, because it is permanent  
  _↳ feedback if chosen: Bleaching by SO₂ is temporary, not permanent._

Full working after a second miss:

> Chlorine bleaches by oxidation, which the air cannot reverse; sulphur dioxide bleaches by reduction.  
> So the answer is Chlorine or a chlorine compound, because its bleaching is permanent.  

> Why must the material be moist for sulphur dioxide to bleach it?

- ◻️ Water is what does the bleaching  
  _↳ feedback if chosen: Water alone does not remove the colour of a flower._
- ◻️ Dry material would catch fire  
  _↳ feedback if chosen: Nothing catches fire in this test._
- ✅ The gas must dissolve in the water to act on the colouring matter
- ◻️ The water washes the colour away  
  _↳ feedback if chosen: Washing is not the effect: the colour is removed chemically, and later returns._

Full working after a second miss:

> Moisture lets the gas form sulphurous acid at the surface, and that is the reducing agent.  
> So the answer is The gas must dissolve in the water to act on the colouring matter.  

> A red flower is held in moist sulphur dioxide and loses its colour. It is then left in the air for some days. What happens?

- ◻️ The flower stays white for ever  
  _↳ feedback if chosen: Permanent bleaching is what chlorine does, by oxidation._
- ✅ The colour slowly returns, because the bleaching by SO₂ is temporary
- ◻️ The colour returns at once  
  _↳ feedback if chosen: The change back takes days, because oxidation by air is slow._
- ◻️ The flower turns black  
  _↳ feedback if chosen: Blackening is what concentrated sulphuric acid does to sugar, by dehydration._

Full working after a second miss:

> SO₂ bleaches by reduction, and oxygen in the air slowly reverses it.  
> So the answer is The colour slowly returns, because the bleaching by SO₂ is temporary.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-5-prep` · Lesson 5 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which reagents are used to prepare hydrogen sulphide in the laboratory? | Iron(II) sulphide and dilute hydrochloric acid | Iron(II) sulphate and dilute hydrochloric acid · Iron filings and dilute hydrochloric acid · Iron(II) sulphide and concentrated nitric acid | A sulphate gives no {formula('H2S')} with a dilute acid; a sulphide does. · Iron with a dilute acid gives hydrogen, not hydrogen sulphide. · Concentrated nitric acid is an oxidising acid; it would oxidise the sulphide to sulphur. | {formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}. |
| What does hydrogen sulphide smell like? | Rotten eggs | A sharp choking smell · Sweet and pleasant · It has no smell | The sharp choking smell is sulphur dioxide. · The smell is strongly unpleasant. · Even a trace can be smelt, which is one way it is noticed. | {formula('H2S')} is a colourless, poisonous gas that smells of rotten eggs. |
| How is hydrogen sulphide collected? | By downward delivery, because it is denser than air | By upward delivery · Over water in an open trough · It cannot be collected | Its relative molecular mass is {34}, above the average for air, so it sinks. · It is fairly soluble in water, so some would be lost. · It is collected in the ordinary way, in a fume cupboard. | A gas denser than air and soluble in water is collected by downward delivery. |
| Why is hydrogen sulphide dangerous to work with? | It is very poisonous, and it dulls the sense of smell so that it may not be noticed | It explodes in contact with air · It is only unpleasant, not harmful · It burns the skin on contact | It burns in air, but it does not explode on contact. · It is seriously poisonous and has killed people. · The danger is from breathing it in, not from skin contact. | After a short time the smell can no longer be noticed, so the gas must always be used in a fume cupboard. |
| How does hydrogen sulphide behave in water? | It dissolves fairly well, giving a weakly acidic solution | It is insoluble · It dissolves to give an alkaline solution · It reacts violently with water | It is fairly soluble: a few volumes dissolve in one volume of water. · The solution turns blue litmus red, so it is acidic. · There is no violent reaction; it simply dissolves. | The solution is a weak acid, sometimes called hydrosulphuric acid. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How is hydrogen sulphide collected?

- ◻️ Over water in an open trough  
  _↳ feedback if chosen: It is fairly soluble in water, so some would be lost._
- ✅ By downward delivery, because it is denser than air
- ◻️ By upward delivery  
  _↳ feedback if chosen: Its relative molecular mass is 34, above the average for air, so it sinks._
- ◻️ It cannot be collected  
  _↳ feedback if chosen: It is collected in the ordinary way, in a fume cupboard._

Full working after a second miss:

> A gas denser than air and soluble in water is collected by downward delivery.  
> So the answer is By downward delivery, because it is denser than air.  

> Why is hydrogen sulphide dangerous to work with?

- ◻️ It is only unpleasant, not harmful  
  _↳ feedback if chosen: It is seriously poisonous and has killed people._
- ◻️ It burns the skin on contact  
  _↳ feedback if chosen: The danger is from breathing it in, not from skin contact._
- ◻️ It explodes in contact with air  
  _↳ feedback if chosen: It burns in air, but it does not explode on contact._
- ✅ It is very poisonous, and it dulls the sense of smell so that it may not be noticed

Full working after a second miss:

> After a short time the smell can no longer be noticed, so the gas must always be used in a fume cupboard.  
> So the answer is It is very poisonous, and it dulls the sense of smell so that it may not be noticed.  

> What does hydrogen sulphide smell like?

- ✅ Rotten eggs
- ◻️ It has no smell  
  _↳ feedback if chosen: Even a trace can be smelt, which is one way it is noticed._
- ◻️ Sweet and pleasant  
  _↳ feedback if chosen: The smell is strongly unpleasant._
- ◻️ A sharp choking smell  
  _↳ feedback if chosen: The sharp choking smell is sulphur dioxide._

Full working after a second miss:

> H₂S is a colourless, poisonous gas that smells of rotten eggs.  
> So the answer is Rotten eggs.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-6-chem` · Lesson 6 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Hydrogen sulphide burns in plenty of air. What is formed? | Sulphur dioxide and water | Sulphur and water only · Hydrogen and sulphur · Sulphur trioxide and hydrogen | Sulphur and water are formed when the air supply is LIMITED. · Burning joins the gas with oxygen; it does not split it into its elements. · {formula('SO3')} is not formed by simple burning, and the hydrogen is oxidised to water. | {2}{formula('H2S')} + {3}{formula('O2')} → {2}{formula('SO2')} + {2}{formula('H2O')}, with a blue flame. |
| Hydrogen sulphide burns in a limited supply of air. What is seen? | A yellow deposit of sulphur forms | A white solid forms · The flame goes out at once · A brown gas is given off | No white solid is formed in this reaction. · It still burns; the limited air changes the product, not whether it burns. · A brown gas is nitrogen dioxide, which is not formed here. | {2}{formula('H2S')} + {formula('O2')} → {2}S + {2}{formula('H2O')}: with too little oxygen the sulphur is not oxidised. |
| Why is hydrogen sulphide described as a reducing agent? | It gives up its hydrogen or its electrons, and is itself oxidised to sulphur | It adds oxygen to other substances · It is an acid in water · It is denser than air | Adding oxygen is what an OXIDISING agent does. · Being an acid is a separate property; it has nothing to do with reduction. · Density has nothing to do with being a reducing agent. | With most oxidising agents, {formula('H2S')} is oxidised and a pale yellow deposit of sulphur appears. |
| Hydrogen sulphide is passed into lead(II) nitrate solution. What is seen? | A black precipitate of lead(II) sulphide | A white precipitate · A yellow solution · No change | Lead(II) sulphide is black, not white. · A precipitate forms rather than a coloured solution. · The change is clear and is used as a test for the gas. | {formula('Pb(NO3)2')} + {formula('H2S')} → {formula('PbS')} + {2}{formula('HNO3')}: lead sulphide is black. |
| Which test paper shows that a gas is hydrogen sulphide? | Filter paper moistened with lead(II) ethanoate, which turns black | Damp red litmus paper, which turns blue · Starch iodide paper, which turns blue · Filter paper moistened with limewater, which turns milky | {formula('H2S')} is acidic, so it turns BLUE litmus red, and that is not a specific test. · Starch iodide paper is used for chlorine and other oxidising gases. · Limewater is the test for carbon dioxide. | Lead(II) ethanoate paper turning black shows the black lead sulphide. |
| Hydrogen sulphide is bubbled into a solution of sulphur dioxide. What is seen, and which gas is oxidised? | A yellow deposit of sulphur; the hydrogen sulphide is oxidised | A yellow deposit; the sulphur dioxide is oxidised · A white precipitate; neither is oxidised · No change; the two gases do not react | {formula('SO2')} is the oxidising agent here, so it is REDUCED, not oxidised. · A yellow solid, not a white one, is formed, and a redox reaction does take place. · The two react readily and the sulphur formed is easy to see. | {formula('SO2')} + {2}{formula('H2S')} → {3}S + {2}{formula('H2O')}: {formula('H2S')} loses hydrogen, so it is oxidised. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Hydrogen sulphide is passed into lead(II) nitrate solution. What is seen?

- ◻️ A yellow solution  
  _↳ feedback if chosen: A precipitate forms rather than a coloured solution._
- ✅ A black precipitate of lead(II) sulphide
- ◻️ A white precipitate  
  _↳ feedback if chosen: Lead(II) sulphide is black, not white._
- ◻️ No change  
  _↳ feedback if chosen: The change is clear and is used as a test for the gas._

Full working after a second miss:

> Pb(NO₃)₂ + H₂S → PbS + 2HNO₃: lead sulphide is black.  
> So the answer is A black precipitate of lead(II) sulphide.  

> Hydrogen sulphide burns in plenty of air. What is formed?

- ◻️ Sulphur trioxide and hydrogen  
  _↳ feedback if chosen: SO₃ is not formed by simple burning, and the hydrogen is oxidised to water._
- ◻️ Hydrogen and sulphur  
  _↳ feedback if chosen: Burning joins the gas with oxygen; it does not split it into its elements._
- ✅ Sulphur dioxide and water
- ◻️ Sulphur and water only  
  _↳ feedback if chosen: Sulphur and water are formed when the air supply is LIMITED._

Full working after a second miss:

> 2H₂S + 3O₂ → 2SO₂ + 2H₂O, with a blue flame.  
> So the answer is Sulphur dioxide and water.  

> Which test paper shows that a gas is hydrogen sulphide?

- ✅ Filter paper moistened with lead(II) ethanoate, which turns black
- ◻️ Starch iodide paper, which turns blue  
  _↳ feedback if chosen: Starch iodide paper is used for chlorine and other oxidising gases._
- ◻️ Damp red litmus paper, which turns blue  
  _↳ feedback if chosen: H₂S is acidic, so it turns BLUE litmus red, and that is not a specific test._
- ◻️ Filter paper moistened with limewater, which turns milky  
  _↳ feedback if chosen: Limewater is the test for carbon dioxide._

Full working after a second miss:

> Lead(II) ethanoate paper turning black shows the black lead sulphide.  
> So the answer is Filter paper moistened with lead(II) ethanoate, which turns black.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-7-make` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How is iron(II) sulphide prepared in the laboratory? | By heating a mixture of iron filings and sulphur | By adding iron filings to dilute sulphuric acid · By burning iron in air · By adding iron filings to water containing sulphur | Iron with dilute sulphuric acid gives iron(II) sulphate and hydrogen. · Burning iron in air gives an oxide, not a sulphide. · Sulphur is insoluble in water, and no reaction takes place in the cold. | Fe + S → {formula('FeS')}: once started, the mixture glows and keeps reacting by itself. |
| What is seen when a mixture of iron filings and sulphur is heated strongly? | The mixture glows red and keeps reacting without more heating | The mixture melts and runs like a liquid · A brown gas is given off · Nothing happens until acid is added | The product is a solid that does not melt at that temperature. · No brown gas is formed; the product is a black solid. · The reaction starts with heat alone. | The reaction gives out heat, so it continues on its own once it has started. |
| How can iron(II) sulphide be told from a mixture of iron and sulphur? | A magnet picks iron out of the mixture but not out of the compound | The compound is yellow and the mixture is black · Both behave in exactly the same way · Only the compound can be seen with a hand lens | It is the other way round in colour terms: the compound is black and the mixture shows yellow specks. · A compound has properties of its own, different from those of its elements. · Both can be seen; the difference is in their properties. | In a mixture the elements keep their own properties, so the iron is still magnetic. |
| What happens when dilute hydrochloric acid is added to iron(II) sulphide? | Hydrogen sulphide is given off | Hydrogen is given off · Sulphur dioxide is given off · Nothing happens | Hydrogen comes from a metal with an acid, not from a sulphide. · Sulphur dioxide comes from a sulphite with an acid. · The reaction is the standard way of making {formula('H2S')}. | {formula('FeS')} + {2}{formula('HCl')} → {formula('FeCl2')} + {formula('H2S')}. |
| Which statement about sodium sulphide is correct? | It is soluble in water and its solution is alkaline | It is insoluble in water · Its solution is strongly acidic · It is a yellow gas | Sodium compounds are generally soluble, and sodium sulphide is no exception. · The solution of a salt of a strong base and a weak acid is alkaline, not acidic. · It is a solid, not a gas. | {formula('Na2S')} dissolves and its solution is alkaline because the sulphide ion reacts with water. |
| Why is iron(II) sulphide used, rather than sodium sulphide, to make hydrogen sulphide in the laboratory? | It is a solid that reacts steadily with dilute acid, so the flow of gas is easy to control | Sodium sulphide gives a different gas · Iron(II) sulphide is the only sulphide that exists · Sodium sulphide does not react with acids | Both give hydrogen sulphide with an acid. · Many metal sulphides exist, such as {formula('Na2S')}, {formula('ZnS')} and {formula('PbS')}. · Sodium sulphide does react, and very readily. | Lumps of {formula('FeS')} react at a steady rate, while the very soluble {formula('Na2S')} would react too fast. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is seen when a mixture of iron filings and sulphur is heated strongly?

- ◻️ The mixture melts and runs like a liquid  
  _↳ feedback if chosen: The product is a solid that does not melt at that temperature._
- ✅ The mixture glows red and keeps reacting without more heating
- ◻️ A brown gas is given off  
  _↳ feedback if chosen: No brown gas is formed; the product is a black solid._
- ◻️ Nothing happens until acid is added  
  _↳ feedback if chosen: The reaction starts with heat alone._

Full working after a second miss:

> The reaction gives out heat, so it continues on its own once it has started.  
> So the answer is The mixture glows red and keeps reacting without more heating.  

> Why is iron(II) sulphide used, rather than sodium sulphide, to make hydrogen sulphide in the laboratory?

- ✅ It is a solid that reacts steadily with dilute acid, so the flow of gas is easy to control
- ◻️ Sodium sulphide does not react with acids  
  _↳ feedback if chosen: Sodium sulphide does react, and very readily._
- ◻️ Iron(II) sulphide is the only sulphide that exists  
  _↳ feedback if chosen: Many metal sulphides exist, such as Na₂S, ZnS and PbS._
- ◻️ Sodium sulphide gives a different gas  
  _↳ feedback if chosen: Both give hydrogen sulphide with an acid._

Full working after a second miss:

> Lumps of FeS react at a steady rate, while the very soluble Na₂S would react too fast.  
> So the answer is It is a solid that reacts steadily with dilute acid, so the flow of gas is easy to control.  

> What is seen when a mixture of iron filings and sulphur is heated strongly?

- ◻️ Nothing happens until acid is added  
  _↳ feedback if chosen: The reaction starts with heat alone._
- ✅ The mixture glows red and keeps reacting without more heating
- ◻️ The mixture melts and runs like a liquid  
  _↳ feedback if chosen: The product is a solid that does not melt at that temperature._
- ◻️ A brown gas is given off  
  _↳ feedback if chosen: No brown gas is formed; the product is a black solid._

Full working after a second miss:

> The reaction gives out heat, so it continues on its own once it has started.  
> So the answer is The mixture glows red and keeps reacting without more heating.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-8-chem` · Lesson 8 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Dilute sulphuric acid is added to zinc. What is seen? | Bubbles of hydrogen, which pop with a lighted splint | Bubbles of sulphur dioxide · A yellow deposit of sulphur · No reaction | Sulphur dioxide comes from the CONCENTRATED acid with copper, not from the dilute acid with zinc. · Sulphur is not formed with the dilute acid. · Zinc is above hydrogen in the reactivity series, so it does react. | Zn + {formula('H2SO4')} → {formula('ZnSO4')} + {formula('H2')}: the dilute acid behaves as an ordinary acid. |
| Dilute sulphuric acid is added to sodium carbonate. What gas is given off? | Carbon dioxide | Hydrogen · Sulphur dioxide · Hydrogen sulphide | Hydrogen comes from a metal with an acid, not from a carbonate. · Sulphur dioxide comes from a sulphite, not from a carbonate. · Hydrogen sulphide comes from a sulphide. | {formula('Na2CO3')} + {formula('H2SO4')} → {formula('Na2SO4')} + {formula('H2O')} + {formula('CO2')}. |
| Concentrated sulphuric acid is poured onto sugar. What is seen? | The sugar turns black and a spongy mass of carbon rises out of the beaker | The sugar dissolves to give a clear solution · The sugar turns bright yellow · Nothing happens until the mixture is heated | The sugar is not simply dissolved; it is chemically changed. · The colour is black, from the carbon left behind. · The change starts at once, and heat is given out. | The acid removes hydrogen and oxygen from the sugar as water, leaving carbon: it is a dehydrating agent. |
| Copper is warmed with concentrated sulphuric acid. What gas is given off? | Sulphur dioxide | Hydrogen · Hydrogen sulphide · Oxygen | Copper is below hydrogen in the reactivity series, so it cannot displace hydrogen. · Hydrogen sulphide comes from a sulphide with a dilute acid. · No oxygen is given off in this reaction. | Cu + {2}{formula('H2SO4')} → {formula('CuSO4')} + {formula('SO2')} + {2}{formula('H2O')}: here the acid is an oxidising agent. |
| Concentrated sulphuric acid is warmed with sodium chloride. What is given off, and why? | Hydrogen chloride, because the acid is less volatile and displaces the more volatile acid | Chlorine, because the acid is an oxidising agent · Hydrogen, because sodium is a reactive metal · Nothing: the two do not react | Chlorine needs a stronger oxidising agent, such as manganese(IV) oxide with concentrated hydrochloric acid. · The sodium is already combined as a salt, so it cannot displace hydrogen. · The reaction is the standard preparation of hydrogen chloride. | {formula('NaCl')} + {formula('H2SO4')} → {formula('NaHSO4')} + {formula('HCl')}: a less volatile acid drives out a more volatile one. |
| Why must concentrated sulphuric acid be added to water, and never water to the acid? | Mixing gives out a great deal of heat, and water poured onto the acid can boil and spit acid out | The acid would become too weak · Water would react chemically with the acid to give hydrogen · The order makes no difference | Diluting always lowers the concentration; that is not the danger. · No hydrogen is given off; the danger is heat. · The order matters a great deal for safety. | Adding acid slowly to a large volume of water lets the heat spread out safely. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Copper is warmed with concentrated sulphuric acid. What gas is given off?

- ◻️ Hydrogen sulphide  
  _↳ feedback if chosen: Hydrogen sulphide comes from a sulphide with a dilute acid._
- ◻️ Hydrogen  
  _↳ feedback if chosen: Copper is below hydrogen in the reactivity series, so it cannot displace hydrogen._
- ✅ Sulphur dioxide
- ◻️ Oxygen  
  _↳ feedback if chosen: No oxygen is given off in this reaction._

Full working after a second miss:

> Cu + 2H₂SO₄ → CuSO₄ + SO₂ + 2H₂O: here the acid is an oxidising agent.  
> So the answer is Sulphur dioxide.  

> Concentrated sulphuric acid is poured onto sugar. What is seen?

- ◻️ Nothing happens until the mixture is heated  
  _↳ feedback if chosen: The change starts at once, and heat is given out._
- ✅ The sugar turns black and a spongy mass of carbon rises out of the beaker
- ◻️ The sugar dissolves to give a clear solution  
  _↳ feedback if chosen: The sugar is not simply dissolved; it is chemically changed._
- ◻️ The sugar turns bright yellow  
  _↳ feedback if chosen: The colour is black, from the carbon left behind._

Full working after a second miss:

> The acid removes hydrogen and oxygen from the sugar as water, leaving carbon: it is a dehydrating agent.  
> So the answer is The sugar turns black and a spongy mass of carbon rises out of the beaker.  

> Concentrated sulphuric acid is warmed with sodium chloride. What is given off, and why?

- ◻️ Hydrogen, because sodium is a reactive metal  
  _↳ feedback if chosen: The sodium is already combined as a salt, so it cannot displace hydrogen._
- ◻️ Chlorine, because the acid is an oxidising agent  
  _↳ feedback if chosen: Chlorine needs a stronger oxidising agent, such as manganese(IV) oxide with concentrated hydrochloric acid._
- ✅ Hydrogen chloride, because the acid is less volatile and displaces the more volatile acid
- ◻️ Nothing: the two do not react  
  _↳ feedback if chosen: The reaction is the standard preparation of hydrogen chloride._

Full working after a second miss:

> NaCl + H₂SO₄ → NaHSO₄ + HCl: a less volatile acid drives out a more volatile one.  
> So the answer is Hydrogen chloride, because the acid is less volatile and displaces the more volatile acid.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-9-uses` · Lesson 9 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the largest single use of sulphur? | Making sulphuric acid | Making matches · Vulcanising rubber · Making fungicides | Matches use only a small amount of sulphur. · Vulcanising is important but uses far less sulphur than the acid industry. · Fungicides use a small amount compared with the acid industry. | Most mined sulphur is burned to {formula('SO2')} and turned into sulphuric acid by the Contact process. |
| Why is sulphur added to rubber? | To vulcanise it, making it harder and more elastic | To make it burn more easily · To colour it yellow · To make it dissolve in water | Rubber is not treated with sulphur in order to burn it. · Vulcanised rubber is not yellow; the change is in its strength, not its colour. · Rubber does not dissolve in water either before or after. | Sulphur links the rubber chains together, so the rubber keeps its shape and wears better in tyres. |
| Which use depends on sulphur dioxide being a preservative? | Treating dried fruit and fruit juice so that they keep | Filling a car battery · Making fertiliser · Vulcanising rubber | A car battery uses sulphuric ACID, not the gas as a preservative. · Fertiliser is made with sulphuric acid, not with the gas as a preservative. · Vulcanising uses the element sulphur. | {formula('SO2')} kills bacteria and moulds, so it is used in small amounts to preserve food and drink. |
| Which of these is made using sulphuric acid? | Ammonium sulphate fertiliser | Common salt from sea water · Limestone for building · Charcoal from wood | Salt is obtained by evaporating sea water; no acid is needed. · Limestone is quarried, not made with acid. · Charcoal is made by heating wood out of contact with air. | Ammonia is neutralised with sulphuric acid to give {formula('(NH4)2SO4')}, a widely used fertiliser. |
| Why is sulphuric acid used in a car battery? | It is the electrolyte that lets the battery give a current | It stops the battery from rusting · It cools the battery · It cleans the metal plates | Rusting is not what the acid is there to prevent. · Cooling is not its purpose; batteries are cooled by air. · The acid does not act as a cleaner; it carries the current as ions. | A lead-acid battery uses dilute sulphuric acid as its electrolyte. |
| Which use of sulphur depends on its killing fungi? | Dusting crops to control mildew and other fungal diseases | Making gunpowder · Making matches · Making sulphuric acid | Gunpowder uses sulphur because it burns, not because it kills fungi. · Matches use sulphur because it catches fire easily. · Making the acid depends on burning the sulphur. | Sulphur dust and lime-sulphur sprays are used as fungicides on crops. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which use depends on sulphur dioxide being a preservative?

- ◻️ Filling a car battery  
  _↳ feedback if chosen: A car battery uses sulphuric ACID, not the gas as a preservative._
- ✅ Treating dried fruit and fruit juice so that they keep
- ◻️ Making fertiliser  
  _↳ feedback if chosen: Fertiliser is made with sulphuric acid, not with the gas as a preservative._
- ◻️ Vulcanising rubber  
  _↳ feedback if chosen: Vulcanising uses the element sulphur._

Full working after a second miss:

> SO₂ kills bacteria and moulds, so it is used in small amounts to preserve food and drink.  
> So the answer is Treating dried fruit and fruit juice so that they keep.  

> Which use depends on sulphur dioxide being a preservative?

- ◻️ Making fertiliser  
  _↳ feedback if chosen: Fertiliser is made with sulphuric acid, not with the gas as a preservative._
- ◻️ Filling a car battery  
  _↳ feedback if chosen: A car battery uses sulphuric ACID, not the gas as a preservative._
- ◻️ Vulcanising rubber  
  _↳ feedback if chosen: Vulcanising uses the element sulphur._
- ✅ Treating dried fruit and fruit juice so that they keep

Full working after a second miss:

> SO₂ kills bacteria and moulds, so it is used in small amounts to preserve food and drink.  
> So the answer is Treating dried fruit and fruit juice so that they keep.  

> Which use of sulphur depends on its killing fungi?

- ✅ Dusting crops to control mildew and other fungal diseases
- ◻️ Making matches  
  _↳ feedback if chosen: Matches use sulphur because it catches fire easily._
- ◻️ Making gunpowder  
  _↳ feedback if chosen: Gunpowder uses sulphur because it burns, not because it kills fungi._
- ◻️ Making sulphuric acid  
  _↳ feedback if chosen: Making the acid depends on burning the sulphur._

Full working after a second miss:

> Sulphur dust and lime-sulphur sprays are used as fungicides on crops.  
> So the answer is Dusting crops to control mildew and other fungal diseases.  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-9-match` · Lesson 9 · matching, level 2

Prompt: Match each substance to a use.

Pairs (3 shown each time):

- Sulphur → **Vulcanising rubber**
- Sulphur dioxide → **Preserving dried fruit**
- Sulphuric acid → **The electrolyte of a car battery**
- Ammonium sulphate → **A nitrogen fertiliser**
- Lime-sulphur spray → **Controlling fungal disease on crops**


Three generated variants:

> Match each substance to a use.

Right-hand side (shuffled): The electrolyte of a car battery · Controlling fungal disease on crops · A nitrogen fertiliser
- Lime-sulphur spray → **Controlling fungal disease on crops**
- Sulphuric acid → **The electrolyte of a car battery**
- Ammonium sulphate → **A nitrogen fertiliser**

Full working after a second miss:

> The right pairs are:  
> Lime-sulphur spray → Controlling fungal disease on crops  
> Sulphuric acid → The electrolyte of a car battery  
> Ammonium sulphate → A nitrogen fertiliser  

> Match each substance to a use.

Right-hand side (shuffled): A nitrogen fertiliser · Vulcanising rubber · The electrolyte of a car battery
- Sulphuric acid → **The electrolyte of a car battery**
- Ammonium sulphate → **A nitrogen fertiliser**
- Sulphur → **Vulcanising rubber**

Full working after a second miss:

> The right pairs are:  
> Sulphuric acid → The electrolyte of a car battery  
> Ammonium sulphate → A nitrogen fertiliser  
> Sulphur → Vulcanising rubber  

> Match each substance to a use.

Right-hand side (shuffled): A nitrogen fertiliser · The electrolyte of a car battery · Vulcanising rubber
- Ammonium sulphate → **A nitrogen fertiliser**
- Sulphur → **Vulcanising rubber**
- Sulphuric acid → **The electrolyte of a car battery**

Full working after a second miss:

> The right pairs are:  
> Ammonium sulphate → A nitrogen fertiliser  
> Sulphur → Vulcanising rubber  
> Sulphuric acid → The electrolyte of a car battery  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

### `k4-9-match-card` · Lesson 9 · matching, level 1

Prompt: Match each substance to a use.

Pairs (3 shown each time):

- Sulphur → **Vulcanising rubber**
- Sulphur dioxide → **Preserving dried fruit**
- Sulphuric acid → **The electrolyte of a car battery**
- Ammonium sulphate → **A nitrogen fertiliser**
- Lime-sulphur spray → **Controlling fungal disease on crops**


Three generated variants:

> Match each substance to a use.

Right-hand side (shuffled): Preserving dried fruit · A nitrogen fertiliser · Vulcanising rubber
- Sulphur dioxide → **Preserving dried fruit**
- Sulphur → **Vulcanising rubber**
- Ammonium sulphate → **A nitrogen fertiliser**

Full working after a second miss:

> The right pairs are:  
> Sulphur dioxide → Preserving dried fruit  
> Sulphur → Vulcanising rubber  
> Ammonium sulphate → A nitrogen fertiliser  

> Match each substance to a use.

Right-hand side (shuffled): A nitrogen fertiliser · Controlling fungal disease on crops · Vulcanising rubber
- Sulphur → **Vulcanising rubber**
- Lime-sulphur spray → **Controlling fungal disease on crops**
- Ammonium sulphate → **A nitrogen fertiliser**

Full working after a second miss:

> The right pairs are:  
> Sulphur → Vulcanising rubber  
> Lime-sulphur spray → Controlling fungal disease on crops  
> Ammonium sulphate → A nitrogen fertiliser  

> Match each substance to a use.

Right-hand side (shuffled): Vulcanising rubber · Preserving dried fruit · The electrolyte of a car battery
- Sulphur dioxide → **Preserving dried fruit**
- Sulphuric acid → **The electrolyte of a car battery**
- Sulphur → **Vulcanising rubber**

Full working after a second miss:

> The right pairs are:  
> Sulphur dioxide → Preserving dried fruit  
> Sulphuric acid → The electrolyte of a car battery  
> Sulphur → Vulcanising rubber  

Sources: sulphur (Form 4 Chemistry syllabus, Term 1, Chemistry of Sulphur: occurrence and the Frasch process; properties and allotropes; preparation and properties of SO2 and H2S; sulphides of sodium and iron; properties of sulphuric acid; uses)

