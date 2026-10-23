# Physics Form 3, Form Three Physics: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f3-physics`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1

Rules the computed answers use are listed in the subject’s library tests; every authored answer is in Part 2.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `p3-1-si` | 1 | multiple choice, 1 | measurement |
| 2 | `p3-2-type` | 2 | multiple choice, 1 | forces |
| 3 | `p3-2-tool` | 2 | multiple choice, 1 | forces |
| 4 | `p3-2-dir` | 2 | multiple choice, 2 | forces |
| 5 | `p3-3-diff` | 3 | multiple choice, 1 | forces |
| 6 | `p3-3-safe` | 3 | multiple choice, 3 | forces |
| 7 | `p3-3-safe-card` (card c3p3-3) | 3 | multiple choice, 1 | forces |
| 8 | `p3-4-tool` | 4 | multiple choice, 1 | measurement |
| 9 | `p3-8-order` | 8 | ordering, 1 | density |
| 10 | `p3-9-ship` | 9 | multiple choice, 1 | density |
| 11 | `p3-9-choose` | 9 | multiple choice, 1 | density |
| 12 | `p3-10-app` | 10 | multiple choice, 1 | pressure |
| 13 | `p3-11-char` | 11 | multiple choice, 1 | pressure |
| 14 | `p3-12-demo` | 12 | multiple choice, 1 | pressure |
| 15 | `p3-12-why` | 12 | multiple choice, 2 | pressure |
| 16 | `p3-12-why-card` (card c3p12-3) | 12 | multiple choice, 1 | pressure |
| 17 | `p3-13-boil` | 13 | multiple choice, 1 | pressure |
| 18 | `p3-13-cooker` | 13 | multiple choice, 1 | pressure |
| 19 | `p3-13-health` | 13 | multiple choice, 2 | pressure |
| 20 | `p3-13-chain` | 13 | ordering, 3 | pressure |
| 21 | `p3-13-health-card` (card c3p13-3) | 13 | multiple choice, 1 | pressure |
| 22 | `p3-14-limit` | 14 | multiple choice, 3 | elasticity |
| 23 | `p3-14-limit-card` (card c3p14-3) | 14 | multiple choice, 1 | elasticity |
| 24 | `p3-15-use` | 15 | multiple choice, 1 | elasticity |
| 25 | `p3-15-shape` | 15 | multiple choice, 2 | elasticity |
| 26 | `p3-16-form` | 16 | multiple choice, 1 | energy |
| 27 | `p3-16-src` | 16 | multiple choice, 1 | energy |
| 28 | `p3-16-adv` | 16 | multiple choice, 2 | energy |
| 29 | `p3-16-change` | 16 | multiple choice, 3 | energy |
| 30 | `p3-16-adv-card` (card c3p16-3) | 16 | multiple choice, 1 | energy |
| 31 | `p3-17-trans` | 17 | multiple choice, 1 | energy |

### `p3-1-si` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is the SI unit of mass? | kilogram (kg) | gram (g) · newton (N) · litre (L) | The gram is a smaller unit; the SI base unit is the kilogram. · The newton is the unit of force (weight). · The litre measures volume. | Mass is measured in kilograms in SI. |
| What is the SI unit of temperature? | kelvin (K) | degree Celsius (°C) · joule (J) · degree Fahrenheit (°F) | °C is used every day, but the SI unit is the kelvin. · The joule is the unit of energy. · °F is not an SI unit. | The SI unit of temperature is the kelvin. |
| Which is a base quantity (not derived)? | time | speed · area · density | Speed = distance ÷ time: derived. · Area = length × length: derived. · Density = mass ÷ volume: derived. | Time is one of the base quantities; its unit is the second. |
| What is the SI unit of electric current? | ampere (A) | volt (V) · watt (W) · ohm (Ω) | The volt measures voltage. · The watt measures power. · The ohm measures resistance. | Current is a base quantity measured in amperes. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is a base quantity (not derived)?

- ◻️ area  
  _↳ feedback if chosen: Area = length × length: derived._
- ✅ time
- ◻️ density  
  _↳ feedback if chosen: Density = mass ÷ volume: derived._
- ◻️ speed  
  _↳ feedback if chosen: Speed = distance ÷ time: derived._

Full working after a second miss:

> Time is one of the base quantities; its unit is the second.  
> So the answer is time.  

> What is the SI unit of electric current?

- ◻️ volt (V)  
  _↳ feedback if chosen: The volt measures voltage._
- ✅ ampere (A)
- ◻️ ohm (Ω)  
  _↳ feedback if chosen: The ohm measures resistance._
- ◻️ watt (W)  
  _↳ feedback if chosen: The watt measures power._

Full working after a second miss:

> Current is a base quantity measured in amperes.  
> So the answer is ampere (A).  

> Which is a base quantity (not derived)?

- ◻️ area  
  _↳ feedback if chosen: Area = length × length: derived._
- ✅ time
- ◻️ density  
  _↳ feedback if chosen: Density = mass ÷ volume: derived._
- ◻️ speed  
  _↳ feedback if chosen: Speed = distance ÷ time: derived._

Full working after a second miss:

> Time is one of the base quantities; its unit is the second.  
> So the answer is time.  

Sources: measurement (Form 3 Physics syllabus, Term 1: physical quantities, SI units, prefixes, standard form; measurement of mass, volume, temperature and time)

### `p3-2-type` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which of these is a vector quantity? | force | mass · time · temperature | Mass has size only. · Time has size only. · Temperature has size only. | A force always acts in a direction. |
| Which of these is a scalar quantity? | speed | velocity · weight · displacement | Velocity is speed in a given direction. · Weight acts downwards: it has a direction. · Displacement is distance in a given direction. | Speed has size only. |
| Why is weight a vector quantity? | It has size and always acts downwards | It is measured in kilograms · It can be large or small · It is measured with a balance | Weight is measured in newtons. · Every quantity can be large or small: that does not make it a vector. · A balance measures mass. | Weight is a force towards the centre of the Earth. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which of these is a vector quantity?

- ◻️ temperature  
  _↳ feedback if chosen: Temperature has size only._
- ✅ force
- ◻️ time  
  _↳ feedback if chosen: Time has size only._
- ◻️ mass  
  _↳ feedback if chosen: Mass has size only._

Full working after a second miss:

> A force always acts in a direction.  
> So the answer is force.  

> Which of these is a vector quantity?

- ◻️ time  
  _↳ feedback if chosen: Time has size only._
- ✅ force
- ◻️ temperature  
  _↳ feedback if chosen: Temperature has size only._
- ◻️ mass  
  _↳ feedback if chosen: Mass has size only._

Full working after a second miss:

> A force always acts in a direction.  
> So the answer is force.  

> Which of these is a vector quantity?

- ◻️ temperature  
  _↳ feedback if chosen: Temperature has size only._
- ◻️ time  
  _↳ feedback if chosen: Time has size only._
- ✅ force
- ◻️ mass  
  _↳ feedback if chosen: Mass has size only._

Full working after a second miss:

> A force always acts in a direction.  
> So the answer is force.  

Sources: forces (Form 3 Physics syllabus, Term 1: scalar and vector quantities, measuring force, mass and weight, laboratory safety)

### `p3-2-tool` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which instrument measures force directly? | a newton meter (spring balance) | a beam balance · a metre rule · a measuring cylinder | A beam balance compares masses. · A metre rule measures length. · A measuring cylinder measures volume. | The spring stretches in proportion to the force. |
| What does a beam balance measure? | mass | weight in newtons · volume · density | It compares masses, so the answer does not change with g. · Volume needs a measuring cylinder. · Density needs mass and volume. | A beam balance compares an unknown mass with known masses. |
| A spring balance reads {30} N. What does it show? | a force of 30 N | a mass of 30 kg · a mass of 30 g · a volume of 30 cm³ | N is the unit of force, not mass. · N is the unit of force, not mass. · N is the unit of force. | A spring balance shows force in newtons. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which instrument measures force directly?

- ◻️ a metre rule  
  _↳ feedback if chosen: A metre rule measures length._
- ✅ a newton meter (spring balance)
- ◻️ a measuring cylinder  
  _↳ feedback if chosen: A measuring cylinder measures volume._
- ◻️ a beam balance  
  _↳ feedback if chosen: A beam balance compares masses._

Full working after a second miss:

> The spring stretches in proportion to the force.  
> So the answer is a newton meter (spring balance).  

> What does a beam balance measure?

- ✅ mass
- ◻️ weight in newtons  
  _↳ feedback if chosen: It compares masses, so the answer does not change with g._
- ◻️ volume  
  _↳ feedback if chosen: Volume needs a measuring cylinder._
- ◻️ density  
  _↳ feedback if chosen: Density needs mass and volume._

Full working after a second miss:

> A beam balance compares an unknown mass with known masses.  
> So the answer is mass.  

> A spring balance reads 30 N. What does it show?

- ◻️ a mass of 30 kg  
  _↳ feedback if chosen: N is the unit of force, not mass._
- ✅ a force of 30 N
- ◻️ a volume of 30 cm³  
  _↳ feedback if chosen: N is the unit of force._
- ◻️ a mass of 30 g  
  _↳ feedback if chosen: N is the unit of force, not mass._

Full working after a second miss:

> A spring balance shows force in newtons.  
> So the answer is a force of 30 N.  

Sources: forces (Form 3 Physics syllabus, Term 1: scalar and vector quantities, measuring force, mass and weight, laboratory safety)

### `p3-2-dir` · Lesson 2 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A {20} N force pulls a box east and a {35} N force pulls it west. What is the resultant? | 15 N west | 15 N east · 55 N west · 55 N east | The larger force is to the west, so the resultant points west. · Opposite directions: subtract. · Opposite directions: subtract, and the larger force decides the direction. | 35 − 20 = 15 N, in the direction of the larger force. |
| Two equal forces of {10} N pull a rope in opposite directions. What is the resultant? | 0 N | 20 N · 10 N · 5 N | They act in opposite directions: subtract. · Each force cancels the other. · Opposite equal forces cancel completely. | Equal and opposite forces are balanced: no resultant. |
| A {50} N push forward and {50} N friction act on a cart. The cart… | has no resultant force | has a resultant of 100 N · has a resultant of 50 N forward · has a resultant of 50 N backward | Friction acts in the opposite direction: subtract. · Friction cancels the push. · The push and friction are equal. | Equal and opposite forces balance. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Two equal forces of 10 N pull a rope in opposite directions. What is the resultant?

- ◻️ 20 N  
  _↳ feedback if chosen: They act in opposite directions: subtract._
- ◻️ 5 N  
  _↳ feedback if chosen: Opposite equal forces cancel completely._
- ◻️ 10 N  
  _↳ feedback if chosen: Each force cancels the other._
- ✅ 0 N

Full working after a second miss:

> Equal and opposite forces are balanced: no resultant.  
> So the answer is 0 N.  

> Two equal forces of 10 N pull a rope in opposite directions. What is the resultant?

- ◻️ 10 N  
  _↳ feedback if chosen: Each force cancels the other._
- ◻️ 20 N  
  _↳ feedback if chosen: They act in opposite directions: subtract._
- ◻️ 5 N  
  _↳ feedback if chosen: Opposite equal forces cancel completely._
- ✅ 0 N

Full working after a second miss:

> Equal and opposite forces are balanced: no resultant.  
> So the answer is 0 N.  

> A 50 N push forward and 50 N friction act on a cart. The cart…

- ◻️ has a resultant of 50 N forward  
  _↳ feedback if chosen: Friction cancels the push._
- ◻️ has a resultant of 100 N  
  _↳ feedback if chosen: Friction acts in the opposite direction: subtract._
- ✅ has no resultant force
- ◻️ has a resultant of 50 N backward  
  _↳ feedback if chosen: The push and friction are equal._

Full working after a second miss:

> Equal and opposite forces balance.  
> So the answer is has no resultant force.  

Sources: forces (Form 3 Physics syllabus, Term 1: scalar and vector quantities, measuring force, mass and weight, laboratory safety)

### `p3-3-diff` · Lesson 3 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which statement about mass is true? | It is the same on the Earth and on the Moon | It is measured in newtons · It is smaller on the Moon · It is measured with a newton meter | Mass is measured in kilograms. · The amount of matter does not change. · A newton meter measures force (weight). | Mass is the amount of matter: it does not depend on place. |
| Which statement about weight is true? | It is a force measured in newtons | It is measured in kilograms · It is the same everywhere · It is a scalar | Kilograms measure mass. · Weight depends on g, which changes from place to place. · Weight has a direction (down): it is a vector. | Weight is the pull of gravity, a force. |
| An astronaut goes to the Moon. What happens? | Her weight decreases but her mass stays the same | Her mass decreases but her weight stays the same · Both decrease · Both stay the same | Mass does not change with place. · Mass does not change with place. · Weight changes because g is smaller on the Moon. | g is smaller on the Moon, so W = mg is smaller; m is unchanged. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> An astronaut goes to the Moon. What happens?

- ◻️ Both decrease  
  _↳ feedback if chosen: Mass does not change with place._
- ◻️ Both stay the same  
  _↳ feedback if chosen: Weight changes because g is smaller on the Moon._
- ✅ Her weight decreases but her mass stays the same
- ◻️ Her mass decreases but her weight stays the same  
  _↳ feedback if chosen: Mass does not change with place._

Full working after a second miss:

> g is smaller on the Moon, so W = mg is smaller; m is unchanged.  
> So the answer is Her weight decreases but her mass stays the same.  

> An astronaut goes to the Moon. What happens?

- ✅ Her weight decreases but her mass stays the same
- ◻️ Both decrease  
  _↳ feedback if chosen: Mass does not change with place._
- ◻️ Her mass decreases but her weight stays the same  
  _↳ feedback if chosen: Mass does not change with place._
- ◻️ Both stay the same  
  _↳ feedback if chosen: Weight changes because g is smaller on the Moon._

Full working after a second miss:

> g is smaller on the Moon, so W = mg is smaller; m is unchanged.  
> So the answer is Her weight decreases but her mass stays the same.  

> Which statement about mass is true?

- ◻️ It is measured in newtons  
  _↳ feedback if chosen: Mass is measured in kilograms._
- ✅ It is the same on the Earth and on the Moon
- ◻️ It is smaller on the Moon  
  _↳ feedback if chosen: The amount of matter does not change._
- ◻️ It is measured with a newton meter  
  _↳ feedback if chosen: A newton meter measures force (weight)._

Full working after a second miss:

> Mass is the amount of matter: it does not depend on place.  
> So the answer is It is the same on the Earth and on the Moon.  

Sources: forces (Form 3 Physics syllabus, Term 1: scalar and vector quantities, measuring force, mass and weight, laboratory safety)

### `p3-3-safe` · Lesson 3 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A thermometer breaks and mercury spills on the bench. What should you do first? | Tell the teacher at once and keep away from the mercury | Pick up the mercury with your fingers · Wipe it into the sink with water · Carry on with the experiment | Mercury is poisonous: never touch it. · Mercury must not go down the drain. · Spills must be reported straight away. | Report accidents immediately; some substances are dangerous. |
| Which is a safe practice in the laboratory? | Wearing goggles when heating liquids | Tasting a solution to identify it · Running between benches · Hanging a heavy load on a small spring balance | Never taste chemicals. · Running causes accidents. · Overloading damages the spring and the load may fall. | Goggles protect your eyes from splashes. |
| Why must you not overload a spring balance? | The spring can be stretched past its limit and be damaged | It makes the reading in kilograms · It changes the value of g · It makes the spring lighter | A spring balance reads newtons. · g depends on the planet, not on the balance. · Mass of the spring does not change. | Beyond its elastic limit a spring does not return to its shape. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is a safe practice in the laboratory?

- ✅ Wearing goggles when heating liquids
- ◻️ Running between benches  
  _↳ feedback if chosen: Running causes accidents._
- ◻️ Tasting a solution to identify it  
  _↳ feedback if chosen: Never taste chemicals._
- ◻️ Hanging a heavy load on a small spring balance  
  _↳ feedback if chosen: Overloading damages the spring and the load may fall._

Full working after a second miss:

> Goggles protect your eyes from splashes.  
> So the answer is Wearing goggles when heating liquids.  

> Which is a safe practice in the laboratory?

- ✅ Wearing goggles when heating liquids
- ◻️ Hanging a heavy load on a small spring balance  
  _↳ feedback if chosen: Overloading damages the spring and the load may fall._
- ◻️ Running between benches  
  _↳ feedback if chosen: Running causes accidents._
- ◻️ Tasting a solution to identify it  
  _↳ feedback if chosen: Never taste chemicals._

Full working after a second miss:

> Goggles protect your eyes from splashes.  
> So the answer is Wearing goggles when heating liquids.  

> Which is a safe practice in the laboratory?

- ◻️ Tasting a solution to identify it  
  _↳ feedback if chosen: Never taste chemicals._
- ✅ Wearing goggles when heating liquids
- ◻️ Running between benches  
  _↳ feedback if chosen: Running causes accidents._
- ◻️ Hanging a heavy load on a small spring balance  
  _↳ feedback if chosen: Overloading damages the spring and the load may fall._

Full working after a second miss:

> Goggles protect your eyes from splashes.  
> So the answer is Wearing goggles when heating liquids.  

Sources: forces (Form 3 Physics syllabus, Term 1: scalar and vector quantities, measuring force, mass and weight, laboratory safety)

### `p3-3-safe-card` · Lesson 3 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A thermometer breaks and mercury spills on the bench. What should you do first? | Tell the teacher at once and keep away from the mercury | Pick up the mercury with your fingers · Wipe it into the sink with water · Carry on with the experiment | Mercury is poisonous: never touch it. · Mercury must not go down the drain. · Spills must be reported straight away. | Report accidents immediately; some substances are dangerous. |
| Which is a safe practice in the laboratory? | Wearing goggles when heating liquids | Tasting a solution to identify it · Running between benches · Hanging a heavy load on a small spring balance | Never taste chemicals. · Running causes accidents. · Overloading damages the spring and the load may fall. | Goggles protect your eyes from splashes. |
| Why must you not overload a spring balance? | The spring can be stretched past its limit and be damaged | It makes the reading in kilograms · It changes the value of g · It makes the spring lighter | A spring balance reads newtons. · g depends on the planet, not on the balance. · Mass of the spring does not change. | Beyond its elastic limit a spring does not return to its shape. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why must you not overload a spring balance?

- ✅ The spring can be stretched past its limit and be damaged
- ◻️ It changes the value of g  
  _↳ feedback if chosen: g depends on the planet, not on the balance._
- ◻️ It makes the spring lighter  
  _↳ feedback if chosen: Mass of the spring does not change._
- ◻️ It makes the reading in kilograms  
  _↳ feedback if chosen: A spring balance reads newtons._

Full working after a second miss:

> Beyond its elastic limit a spring does not return to its shape.  
> So the answer is The spring can be stretched past its limit and be damaged.  

> Why must you not overload a spring balance?

- ✅ The spring can be stretched past its limit and be damaged
- ◻️ It makes the spring lighter  
  _↳ feedback if chosen: Mass of the spring does not change._
- ◻️ It makes the reading in kilograms  
  _↳ feedback if chosen: A spring balance reads newtons._
- ◻️ It changes the value of g  
  _↳ feedback if chosen: g depends on the planet, not on the balance._

Full working after a second miss:

> Beyond its elastic limit a spring does not return to its shape.  
> So the answer is The spring can be stretched past its limit and be damaged.  

> Why must you not overload a spring balance?

- ◻️ It makes the reading in kilograms  
  _↳ feedback if chosen: A spring balance reads newtons._
- ✅ The spring can be stretched past its limit and be damaged
- ◻️ It makes the spring lighter  
  _↳ feedback if chosen: Mass of the spring does not change._
- ◻️ It changes the value of g  
  _↳ feedback if chosen: g depends on the planet, not on the balance._

Full working after a second miss:

> Beyond its elastic limit a spring does not return to its shape.  
> So the answer is The spring can be stretched past its limit and be damaged.  

Sources: forces (Form 3 Physics syllabus, Term 1: scalar and vector quantities, measuring force, mass and weight, laboratory safety)

### `p3-4-tool` · Lesson 4 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Before weighing on an electronic balance, what should you do? | Check that it reads zero (tare it) | Put the object on it first · Shake it · Add a known mass | Zero the balance before adding the object. · Shaking gives false readings. · That would add to the reading. | A balance that does not start at zero gives a zero error. |
| Which instrument is used to measure mass in the laboratory? | a beam balance | a newton meter · a measuring cylinder · a vernier caliper | A newton meter measures force. · A measuring cylinder measures volume. · Calipers measure length. | Balances measure mass. |
| A balance reads {5} g with nothing on it. What is this called? | a zero error | the mass of the air · the tare · a parallax error | The balance should read {0} with nothing on it. · Taring is how you remove the error. · Parallax is about reading a scale from the side. | Subtract {5} g from every reading, or tare the balance. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which instrument is used to measure mass in the laboratory?

- ✅ a beam balance
- ◻️ a newton meter  
  _↳ feedback if chosen: A newton meter measures force._
- ◻️ a vernier caliper  
  _↳ feedback if chosen: Calipers measure length._
- ◻️ a measuring cylinder  
  _↳ feedback if chosen: A measuring cylinder measures volume._

Full working after a second miss:

> Balances measure mass.  
> So the answer is a beam balance.  

> Which instrument is used to measure mass in the laboratory?

- ◻️ a newton meter  
  _↳ feedback if chosen: A newton meter measures force._
- ✅ a beam balance
- ◻️ a vernier caliper  
  _↳ feedback if chosen: Calipers measure length._
- ◻️ a measuring cylinder  
  _↳ feedback if chosen: A measuring cylinder measures volume._

Full working after a second miss:

> Balances measure mass.  
> So the answer is a beam balance.  

> A balance reads 5 g with nothing on it. What is this called?

- ◻️ the mass of the air  
  _↳ feedback if chosen: The balance should read 0 with nothing on it._
- ✅ a zero error
- ◻️ the tare  
  _↳ feedback if chosen: Taring is how you remove the error._
- ◻️ a parallax error  
  _↳ feedback if chosen: Parallax is about reading a scale from the side._

Full working after a second miss:

> Subtract 5 g from every reading, or tare the balance.  
> So the answer is a zero error.  

Sources: measurement (Form 3 Physics syllabus, Term 1: physical quantities, SI units, prefixes, standard form; measurement of mass, volume, temperature and time)

### `p3-8-order` · Lesson 8 · ordering, level 1

Prompt: Put the steps for finding the density of a stone in order.

Items in the right order:

1. Find the mass of the dry stone on a balance.
2. Pour water into a measuring cylinder and read the volume.
3. Lower the stone in gently on a thread and read the new volume.
4. Subtract the readings to get the volume of the stone.
5. Divide the mass by the volume.


Three generated variants:

> Put the steps for finding the density of a stone in order.

Shown as: Lower the stone in gently on a thread and read the new volume. · Divide the mass by the volume. · Subtract the readings to get the volume of the stone. · Find the mass of the dry stone on a balance. · Pour water into a measuring cylinder and read the volume.
Correct order: Find the mass of the dry stone on a balance. → Pour water into a measuring cylinder and read the volume. → Lower the stone in gently on a thread and read the new volume. → Subtract the readings to get the volume of the stone. → Divide the mass by the volume.

Hint (draft): Weigh the stone while it is still dry.

Full working after a second miss:

> The correct order is: Find the mass of the dry stone on a balance. → Pour water into a measuring cylinder and read the volume. → Lower the stone in gently on a thread and read the new volume. → Subtract the readings to get the volume of the stone. → Divide the mass by the volume..  

> Put the steps for finding the density of a stone in order.

Shown as: Lower the stone in gently on a thread and read the new volume. · Subtract the readings to get the volume of the stone. · Divide the mass by the volume. · Find the mass of the dry stone on a balance. · Pour water into a measuring cylinder and read the volume.
Correct order: Find the mass of the dry stone on a balance. → Pour water into a measuring cylinder and read the volume. → Lower the stone in gently on a thread and read the new volume. → Subtract the readings to get the volume of the stone. → Divide the mass by the volume.

Hint (draft): Weigh the stone while it is still dry.

Full working after a second miss:

> The correct order is: Find the mass of the dry stone on a balance. → Pour water into a measuring cylinder and read the volume. → Lower the stone in gently on a thread and read the new volume. → Subtract the readings to get the volume of the stone. → Divide the mass by the volume..  

> Put the steps for finding the density of a stone in order.

Shown as: Find the mass of the dry stone on a balance. · Divide the mass by the volume. · Subtract the readings to get the volume of the stone. · Lower the stone in gently on a thread and read the new volume. · Pour water into a measuring cylinder and read the volume.
Correct order: Find the mass of the dry stone on a balance. → Pour water into a measuring cylinder and read the volume. → Lower the stone in gently on a thread and read the new volume. → Subtract the readings to get the volume of the stone. → Divide the mass by the volume.

Hint (draft): Weigh the stone while it is still dry.

Full working after a second miss:

> The correct order is: Find the mass of the dry stone on a balance. → Pour water into a measuring cylinder and read the volume. → Lower the stone in gently on a thread and read the new volume. → Subtract the readings to get the volume of the stone. → Divide the mass by the volume..  

Sources: density (Form 3 Physics syllabus, Term 1: density, its measurement for liquids, regular and irregular solids, and applications)

### `p3-9-ship` · Lesson 9 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does a large steel ship float when a steel nail sinks? | The hollow hull makes the ship's average density less than water's | Steel is less dense than water · The ship is lighter than the nail · Sea water has no density | Steel (7.9 g/cm³) is much denser than water. · The ship is far heavier than the nail. · Sea water is slightly denser than fresh water. | The air inside the hull lowers the average density. |
| Why does a hot-air balloon rise? | Hot air is less dense than the cold air around it | Hot air has no mass · The basket is lighter than air · Fire pushes the balloon up | Hot air still has mass, just less per cubic metre. · The basket is denser than air; the hot air carries it. · The flame heats the air; it does not push the balloon. | Less dense air rises through denser air. |
| After an oil spill, the oil spreads on top of the sea. Why? | Oil is less dense than sea water | Oil is denser than sea water · Oil is a gas · The wind pushes it up | Denser oil would sink. · Oil is a liquid. · It floats because of density, even on a calm day. | Less dense liquids float on denser ones. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> After an oil spill, the oil spreads on top of the sea. Why?

- ✅ Oil is less dense than sea water
- ◻️ Oil is a gas  
  _↳ feedback if chosen: Oil is a liquid._
- ◻️ The wind pushes it up  
  _↳ feedback if chosen: It floats because of density, even on a calm day._
- ◻️ Oil is denser than sea water  
  _↳ feedback if chosen: Denser oil would sink._

Full working after a second miss:

> Less dense liquids float on denser ones.  
> So the answer is Oil is less dense than sea water.  

> Why does a hot-air balloon rise?

- ◻️ The basket is lighter than air  
  _↳ feedback if chosen: The basket is denser than air; the hot air carries it._
- ✅ Hot air is less dense than the cold air around it
- ◻️ Hot air has no mass  
  _↳ feedback if chosen: Hot air still has mass, just less per cubic metre._
- ◻️ Fire pushes the balloon up  
  _↳ feedback if chosen: The flame heats the air; it does not push the balloon._

Full working after a second miss:

> Less dense air rises through denser air.  
> So the answer is Hot air is less dense than the cold air around it.  

> After an oil spill, the oil spreads on top of the sea. Why?

- ◻️ Oil is denser than sea water  
  _↳ feedback if chosen: Denser oil would sink._
- ◻️ Oil is a gas  
  _↳ feedback if chosen: Oil is a liquid._
- ◻️ The wind pushes it up  
  _↳ feedback if chosen: It floats because of density, even on a calm day._
- ✅ Oil is less dense than sea water

Full working after a second miss:

> Less dense liquids float on denser ones.  
> So the answer is Oil is less dense than sea water.  

Sources: density (Form 3 Physics syllabus, Term 1: density, its measurement for liquids, regular and irregular solids, and applications)

### `p3-9-choose` · Lesson 9 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is aluminium used to make aircraft bodies? | It is strong and has a low density | It is the densest metal · It is magnetic · It melts easily | A dense metal would make the aircraft too heavy. · Magnetism is not why it is chosen. · A low melting point would be a problem, not an advantage. | Strength with low density keeps the aircraft light. |
| Which material is best for a life jacket? | Foam of very low density | Iron · Concrete · Lead | Iron is very dense: it sinks. · Concrete sinks. · Lead is very dense: it sinks. | A low-density material floats and helps you float. |
| Fishermen in Limbe tie lead weights to their nets. Why lead? | Lead is very dense, so a small piece pulls the net down | Lead floats · Lead is light · Lead dissolves in water | Lead sinks: it is denser than water. · Lead is very dense. · Lead does not dissolve; it is chosen for its density. | High density: a small volume has a large mass. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Fishermen in Limbe tie lead weights to their nets. Why lead?

- ◻️ Lead dissolves in water  
  _↳ feedback if chosen: Lead does not dissolve; it is chosen for its density._
- ✅ Lead is very dense, so a small piece pulls the net down
- ◻️ Lead is light  
  _↳ feedback if chosen: Lead is very dense._
- ◻️ Lead floats  
  _↳ feedback if chosen: Lead sinks: it is denser than water._

Full working after a second miss:

> High density: a small volume has a large mass.  
> So the answer is Lead is very dense, so a small piece pulls the net down.  

> Why is aluminium used to make aircraft bodies?

- ◻️ It is the densest metal  
  _↳ feedback if chosen: A dense metal would make the aircraft too heavy._
- ✅ It is strong and has a low density
- ◻️ It is magnetic  
  _↳ feedback if chosen: Magnetism is not why it is chosen._
- ◻️ It melts easily  
  _↳ feedback if chosen: A low melting point would be a problem, not an advantage._

Full working after a second miss:

> Strength with low density keeps the aircraft light.  
> So the answer is It is strong and has a low density.  

> Which material is best for a life jacket?

- ✅ Foam of very low density
- ◻️ Lead  
  _↳ feedback if chosen: Lead is very dense: it sinks._
- ◻️ Iron  
  _↳ feedback if chosen: Iron is very dense: it sinks._
- ◻️ Concrete  
  _↳ feedback if chosen: Concrete sinks._

Full working after a second miss:

> A low-density material floats and helps you float.  
> So the answer is Foam of very low density.  

Sources: density (Form 3 Physics syllabus, Term 1: density, its measurement for liquids, regular and irregular solids, and applications)

### `p3-10-app` · Lesson 10 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is a kitchen knife sharpened? | A thin edge has a small area, so the pressure is large | A thin edge has a large area · Sharpening makes the knife heavier · Sharpening reduces the force needed to lift it | A thin edge has a small area. · Sharpening removes metal; it is lighter. · Lifting has nothing to do with cutting. | The same push over a smaller area gives a bigger pressure. |
| Why do heavy lorries have many wide tyres? | To spread the weight over a large area and reduce the pressure on the road | To increase the pressure on the road · To make the lorry go faster · To reduce the weight of the lorry | Large pressure would damage the road and sink into soft ground. · Tyre width is about pressure, not speed. · The weight stays the same. | A large area reduces the pressure. |
| Why are the foundations of a building made wide? | To reduce the pressure on the ground so the building does not sink | To increase the pressure on the ground · To make the walls stronger · To make the building lighter | High pressure would make the building sink. · Width of the foundation is about pressure on the soil. · The weight is not reduced. | A wide base spreads the weight over a large area. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why do heavy lorries have many wide tyres?

- ◻️ To increase the pressure on the road  
  _↳ feedback if chosen: Large pressure would damage the road and sink into soft ground._
- ◻️ To reduce the weight of the lorry  
  _↳ feedback if chosen: The weight stays the same._
- ✅ To spread the weight over a large area and reduce the pressure on the road
- ◻️ To make the lorry go faster  
  _↳ feedback if chosen: Tyre width is about pressure, not speed._

Full working after a second miss:

> A large area reduces the pressure.  
> So the answer is To spread the weight over a large area and reduce the pressure on the road.  

> Why is a kitchen knife sharpened?

- ◻️ Sharpening makes the knife heavier  
  _↳ feedback if chosen: Sharpening removes metal; it is lighter._
- ✅ A thin edge has a small area, so the pressure is large
- ◻️ A thin edge has a large area  
  _↳ feedback if chosen: A thin edge has a small area._
- ◻️ Sharpening reduces the force needed to lift it  
  _↳ feedback if chosen: Lifting has nothing to do with cutting._

Full working after a second miss:

> The same push over a smaller area gives a bigger pressure.  
> So the answer is A thin edge has a small area, so the pressure is large.  

> Why are the foundations of a building made wide?

- ✅ To reduce the pressure on the ground so the building does not sink
- ◻️ To increase the pressure on the ground  
  _↳ feedback if chosen: High pressure would make the building sink._
- ◻️ To make the building lighter  
  _↳ feedback if chosen: The weight is not reduced._
- ◻️ To make the walls stronger  
  _↳ feedback if chosen: Width of the foundation is about pressure on the soil._

Full working after a second miss:

> A wide base spreads the weight over a large area.  
> So the answer is To reduce the pressure on the ground so the building does not sink.  

Sources: pressure (Form 3 Physics syllabus, Term 1: pressure in solids, liquids and the atmosphere; the simple barometer; effects on boiling points and health)

### `p3-11-char` · Lesson 11 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A tin has three holes at different heights and is filled with water. Water squirts furthest from… | the lowest hole | the highest hole · the middle hole · all holes equally | Near the top the depth, and so the pressure, is small. · The lowest hole is deepest. · Pressure increases with depth, so the jets differ. | The deepest point has the greatest pressure. |
| Why is a dam built thicker at the bottom than at the top? | Water pressure increases with depth | Water is denser at the top · The top must hold more water · Pressure is greatest at the surface | The density is the same throughout. · The deeper water pushes harder. · Pressure is smallest at the surface. | The wall must resist the large pressure near the bottom. |
| At the same depth in a liquid, the pressure acts… | equally in all directions | only downwards · only sideways · only upwards | Liquid pressure also pushes sideways and upwards. · It also pushes down and up. · It also pushes down and sideways. | Liquid pressure at a point is the same in every direction. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A tin has three holes at different heights and is filled with water. Water squirts furthest from…

- ✅ the lowest hole
- ◻️ the highest hole  
  _↳ feedback if chosen: Near the top the depth, and so the pressure, is small._
- ◻️ all holes equally  
  _↳ feedback if chosen: Pressure increases with depth, so the jets differ._
- ◻️ the middle hole  
  _↳ feedback if chosen: The lowest hole is deepest._

Full working after a second miss:

> The deepest point has the greatest pressure.  
> So the answer is the lowest hole.  

> Why is a dam built thicker at the bottom than at the top?

- ◻️ The top must hold more water  
  _↳ feedback if chosen: The deeper water pushes harder._
- ◻️ Pressure is greatest at the surface  
  _↳ feedback if chosen: Pressure is smallest at the surface._
- ✅ Water pressure increases with depth
- ◻️ Water is denser at the top  
  _↳ feedback if chosen: The density is the same throughout._

Full working after a second miss:

> The wall must resist the large pressure near the bottom.  
> So the answer is Water pressure increases with depth.  

> A tin has three holes at different heights and is filled with water. Water squirts furthest from…

- ✅ the lowest hole
- ◻️ the highest hole  
  _↳ feedback if chosen: Near the top the depth, and so the pressure, is small._
- ◻️ the middle hole  
  _↳ feedback if chosen: The lowest hole is deepest._
- ◻️ all holes equally  
  _↳ feedback if chosen: Pressure increases with depth, so the jets differ._

Full working after a second miss:

> The deepest point has the greatest pressure.  
> So the answer is the lowest hole.  

Sources: pressure (Form 3 Physics syllabus, Term 1: pressure in solids, liquids and the atmosphere; the simple barometer; effects on boiling points and health)

### `p3-12-demo` · Lesson 12 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Steam fills a can, the lid is closed and the can is cooled. It collapses. Why? | The steam condenses, the pressure inside falls, and the air outside crushes the can | Cold water shrinks the metal · The steam pulls the walls in · The can becomes heavier | Cooling the metal this little does not crush it. · Steam does not pull; the outside air pushes. · Its weight barely changes. | Atmospheric pressure outside is much larger than the pressure left inside. |
| How does a drinking straw work? | You lower the pressure in the straw; atmospheric pressure pushes the drink up | Your mouth pulls the drink up by suction force · The drink is lighter than air · The straw squeezes the drink | Suction is not a force: the outside air does the pushing. · Drinks are much denser than air. · The straw does not squeeze anything. | Air pressure on the surface of the drink pushes it up the straw. |
| A card covers a full glass of water turned upside down, and the water does not fall. Why? | Atmospheric pressure on the card is greater than the water pressure on it | The card is glued by the water · Water has no weight · The glass is magnetic | Water does not glue strongly enough to hold the weight. · Water has weight. · Glass is not magnetic. | The air pushes up on the card with about {100000} Pa. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Steam fills a can, the lid is closed and the can is cooled. It collapses. Why?

- ✅ The steam condenses, the pressure inside falls, and the air outside crushes the can
- ◻️ Cold water shrinks the metal  
  _↳ feedback if chosen: Cooling the metal this little does not crush it._
- ◻️ The steam pulls the walls in  
  _↳ feedback if chosen: Steam does not pull; the outside air pushes._
- ◻️ The can becomes heavier  
  _↳ feedback if chosen: Its weight barely changes._

Full working after a second miss:

> Atmospheric pressure outside is much larger than the pressure left inside.  
> So the answer is The steam condenses, the pressure inside falls, and the air outside crushes the can.  

> How does a drinking straw work?

- ◻️ The straw squeezes the drink  
  _↳ feedback if chosen: The straw does not squeeze anything._
- ✅ You lower the pressure in the straw; atmospheric pressure pushes the drink up
- ◻️ Your mouth pulls the drink up by suction force  
  _↳ feedback if chosen: Suction is not a force: the outside air does the pushing._
- ◻️ The drink is lighter than air  
  _↳ feedback if chosen: Drinks are much denser than air._

Full working after a second miss:

> Air pressure on the surface of the drink pushes it up the straw.  
> So the answer is You lower the pressure in the straw; atmospheric pressure pushes the drink up.  

> A card covers a full glass of water turned upside down, and the water does not fall. Why?

- ◻️ The glass is magnetic  
  _↳ feedback if chosen: Glass is not magnetic._
- ◻️ The card is glued by the water  
  _↳ feedback if chosen: Water does not glue strongly enough to hold the weight._
- ◻️ Water has no weight  
  _↳ feedback if chosen: Water has weight._
- ✅ Atmospheric pressure on the card is greater than the water pressure on it

Full working after a second miss:

> The air pushes up on the card with about 100 000 Pa.  
> So the answer is Atmospheric pressure on the card is greater than the water pressure on it.  

Sources: pressure (Form 3 Physics syllabus, Term 1: pressure in solids, liquids and the atmosphere; the simple barometer; effects on boiling points and health)

### `p3-12-why` · Lesson 12 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is mercury used in a barometer rather than water? | Mercury is very dense, so the column is short (about 76 cm) | Mercury is cheaper than water · Water evaporates too fast to read · Mercury is lighter than water | Mercury is expensive. · The main reason is the height: water would need about 10 m. · Mercury is about 13.6 times denser than water. | p = ρgh: a large ρ gives a small h. |
| What is in the space above the mercury in a barometer tube? | A vacuum (almost nothing) | Air · Water vapour · Mercury gas at high pressure | Air would push the mercury down and spoil the reading. · No water is in the tube. · There is only a tiny amount of mercury vapour. | The tube was full of mercury before it was turned over; nothing replaced the mercury that fell. |
| If the barometer tube is tilted, what happens to the vertical height of the mercury column? | It stays the same | It increases · It decreases · It becomes zero | The mercury fills more of the tube, but the vertical height is fixed by air pressure. · Air pressure has not changed. · Air pressure still holds the mercury up. | Only the vertical height depends on the air pressure. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> If the barometer tube is tilted, what happens to the vertical height of the mercury column?

- ◻️ It increases  
  _↳ feedback if chosen: The mercury fills more of the tube, but the vertical height is fixed by air pressure._
- ◻️ It becomes zero  
  _↳ feedback if chosen: Air pressure still holds the mercury up._
- ✅ It stays the same
- ◻️ It decreases  
  _↳ feedback if chosen: Air pressure has not changed._

Full working after a second miss:

> Only the vertical height depends on the air pressure.  
> So the answer is It stays the same.  

> Why is mercury used in a barometer rather than water?

- ◻️ Mercury is lighter than water  
  _↳ feedback if chosen: Mercury is about 13.6 times denser than water._
- ◻️ Mercury is cheaper than water  
  _↳ feedback if chosen: Mercury is expensive._
- ◻️ Water evaporates too fast to read  
  _↳ feedback if chosen: The main reason is the height: water would need about 10 m._
- ✅ Mercury is very dense, so the column is short (about 76 cm)

Full working after a second miss:

> p = ρgh: a large ρ gives a small h.  
> So the answer is Mercury is very dense, so the column is short (about 76 cm).  

> Why is mercury used in a barometer rather than water?

- ◻️ Mercury is cheaper than water  
  _↳ feedback if chosen: Mercury is expensive._
- ◻️ Water evaporates too fast to read  
  _↳ feedback if chosen: The main reason is the height: water would need about 10 m._
- ◻️ Mercury is lighter than water  
  _↳ feedback if chosen: Mercury is about 13.6 times denser than water._
- ✅ Mercury is very dense, so the column is short (about 76 cm)

Full working after a second miss:

> p = ρgh: a large ρ gives a small h.  
> So the answer is Mercury is very dense, so the column is short (about 76 cm).  

Sources: pressure (Form 3 Physics syllabus, Term 1: pressure in solids, liquids and the atmosphere; the simple barometer; effects on boiling points and health)

### `p3-12-why-card` · Lesson 12 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is mercury used in a barometer rather than water? | Mercury is very dense, so the column is short (about 76 cm) | Mercury is cheaper than water · Water evaporates too fast to read · Mercury is lighter than water | Mercury is expensive. · The main reason is the height: water would need about 10 m. · Mercury is about 13.6 times denser than water. | p = ρgh: a large ρ gives a small h. |
| What is in the space above the mercury in a barometer tube? | A vacuum (almost nothing) | Air · Water vapour · Mercury gas at high pressure | Air would push the mercury down and spoil the reading. · No water is in the tube. · There is only a tiny amount of mercury vapour. | The tube was full of mercury before it was turned over; nothing replaced the mercury that fell. |
| If the barometer tube is tilted, what happens to the vertical height of the mercury column? | It stays the same | It increases · It decreases · It becomes zero | The mercury fills more of the tube, but the vertical height is fixed by air pressure. · Air pressure has not changed. · Air pressure still holds the mercury up. | Only the vertical height depends on the air pressure. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is in the space above the mercury in a barometer tube?

- ◻️ Water vapour  
  _↳ feedback if chosen: No water is in the tube._
- ◻️ Air  
  _↳ feedback if chosen: Air would push the mercury down and spoil the reading._
- ◻️ Mercury gas at high pressure  
  _↳ feedback if chosen: There is only a tiny amount of mercury vapour._
- ✅ A vacuum (almost nothing)

Full working after a second miss:

> The tube was full of mercury before it was turned over; nothing replaced the mercury that fell.  
> So the answer is A vacuum (almost nothing).  

> If the barometer tube is tilted, what happens to the vertical height of the mercury column?

- ✅ It stays the same
- ◻️ It becomes zero  
  _↳ feedback if chosen: Air pressure still holds the mercury up._
- ◻️ It decreases  
  _↳ feedback if chosen: Air pressure has not changed._
- ◻️ It increases  
  _↳ feedback if chosen: The mercury fills more of the tube, but the vertical height is fixed by air pressure._

Full working after a second miss:

> Only the vertical height depends on the air pressure.  
> So the answer is It stays the same.  

> If the barometer tube is tilted, what happens to the vertical height of the mercury column?

- ◻️ It increases  
  _↳ feedback if chosen: The mercury fills more of the tube, but the vertical height is fixed by air pressure._
- ◻️ It decreases  
  _↳ feedback if chosen: Air pressure has not changed._
- ◻️ It becomes zero  
  _↳ feedback if chosen: Air pressure still holds the mercury up._
- ✅ It stays the same

Full working after a second miss:

> Only the vertical height depends on the air pressure.  
> So the answer is It stays the same.  

Sources: pressure (Form 3 Physics syllabus, Term 1: pressure in solids, liquids and the atmosphere; the simple barometer; effects on boiling points and health)

### `p3-13-boil` · Lesson 13 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How does the boiling point of water change as you climb a mountain? | It goes down | It goes up · It stays at 100 °C · Water cannot boil there | Higher up the pressure is lower, which lowers the boiling point. · 100 °C is the boiling point only at normal sea-level pressure. · It boils, but at a lower temperature. | Lower air pressure, lower boiling point. |
| Why does food take longer to cook at high altitude? | Water boils at a lower temperature there | Water boils at a higher temperature there · Fire burns hotter there · Food is heavier there | Lower pressure means a lower boiling point. · Less oxygen makes fires burn less well, not hotter. · The weight of food has nothing to do with cooking time. | Boiling water is cooler, so cooking is slower. |
| What happens to atmospheric pressure as altitude increases? | It decreases | It increases · It stays the same · It becomes zero at once | There is less air above you higher up. · There is less air above you higher up. · It falls gradually. | Less air above, less weight, lower pressure. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What happens to atmospheric pressure as altitude increases?

- ✅ It decreases
- ◻️ It stays the same  
  _↳ feedback if chosen: There is less air above you higher up._
- ◻️ It increases  
  _↳ feedback if chosen: There is less air above you higher up._
- ◻️ It becomes zero at once  
  _↳ feedback if chosen: It falls gradually._

Full working after a second miss:

> Less air above, less weight, lower pressure.  
> So the answer is It decreases.  

> Why does food take longer to cook at high altitude?

- ✅ Water boils at a lower temperature there
- ◻️ Fire burns hotter there  
  _↳ feedback if chosen: Less oxygen makes fires burn less well, not hotter._
- ◻️ Food is heavier there  
  _↳ feedback if chosen: The weight of food has nothing to do with cooking time._
- ◻️ Water boils at a higher temperature there  
  _↳ feedback if chosen: Lower pressure means a lower boiling point._

Full working after a second miss:

> Boiling water is cooler, so cooking is slower.  
> So the answer is Water boils at a lower temperature there.  

> Why does food take longer to cook at high altitude?

- ◻️ Food is heavier there  
  _↳ feedback if chosen: The weight of food has nothing to do with cooking time._
- ◻️ Water boils at a higher temperature there  
  _↳ feedback if chosen: Lower pressure means a lower boiling point._
- ✅ Water boils at a lower temperature there
- ◻️ Fire burns hotter there  
  _↳ feedback if chosen: Less oxygen makes fires burn less well, not hotter._

Full working after a second miss:

> Boiling water is cooler, so cooking is slower.  
> So the answer is Water boils at a lower temperature there.  

Sources: pressure (Form 3 Physics syllabus, Term 1: pressure in solids, liquids and the atmosphere; the simple barometer; effects on boiling points and health)

### `p3-13-cooker` · Lesson 13 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How does a pressure cooker cook food faster? | It raises the pressure, so water boils above 100 °C | It lowers the boiling point · It removes the air so food cooks in a vacuum · It makes the flame hotter | It raises the boiling point. · It traps steam, raising the pressure. · The flame is the same. | Hotter boiling water cooks food faster. |
| Why must a pressure cooker have a safety valve? | To let steam out if the pressure gets dangerously high | To let air in · To make the food taste better · To measure the temperature | The valve releases pressure, it does not let air in. · Taste has nothing to do with it. · It does not measure temperature. | Too much pressure could burst the cooker. |
| Water in a sealed pressure cooker boils at about… | 120 °C | 80 °C · 100 °C exactly · 0 °C | Higher pressure raises the boiling point above 100 °C. · 100 °C is the boiling point at normal pressure. · 0 °C is the freezing point. | The higher pressure raises the boiling point to about 120 °C. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why must a pressure cooker have a safety valve?

- ✅ To let steam out if the pressure gets dangerously high
- ◻️ To measure the temperature  
  _↳ feedback if chosen: It does not measure temperature._
- ◻️ To let air in  
  _↳ feedback if chosen: The valve releases pressure, it does not let air in._
- ◻️ To make the food taste better  
  _↳ feedback if chosen: Taste has nothing to do with it._

Full working after a second miss:

> Too much pressure could burst the cooker.  
> So the answer is To let steam out if the pressure gets dangerously high.  

> How does a pressure cooker cook food faster?

- ✅ It raises the pressure, so water boils above 100 °C
- ◻️ It removes the air so food cooks in a vacuum  
  _↳ feedback if chosen: It traps steam, raising the pressure._
- ◻️ It makes the flame hotter  
  _↳ feedback if chosen: The flame is the same._
- ◻️ It lowers the boiling point  
  _↳ feedback if chosen: It raises the boiling point._

Full working after a second miss:

> Hotter boiling water cooks food faster.  
> So the answer is It raises the pressure, so water boils above 100 °C.  

> Water in a sealed pressure cooker boils at about…

- ◻️ 100 °C exactly  
  _↳ feedback if chosen: 100 °C is the boiling point at normal pressure._
- ◻️ 0 °C  
  _↳ feedback if chosen: 0 °C is the freezing point._
- ◻️ 80 °C  
  _↳ feedback if chosen: Higher pressure raises the boiling point above 100 °C._
- ✅ 120 °C

Full working after a second miss:

> The higher pressure raises the boiling point to about 120 °C.  
> So the answer is 120 °C.  

Sources: pressure (Form 3 Physics syllabus, Term 1: pressure in solids, liquids and the atmosphere; the simple barometer; effects on boiling points and health)

### `p3-13-health` · Lesson 13 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do some climbers feel dizzy near the summit of a high mountain? | The low air pressure means less oxygen in each breath | The air contains more oxygen · Their blood becomes heavier · The sun is closer | There is less oxygen per breath. · Blood density does not change. · Distance to the sun is not the cause. | Altitude sickness comes from low pressure and less oxygen. |
| Why do your ears 'pop' when a plane takes off? | The outside pressure changes quickly and the pressure in the middle ear adjusts | The engine noise is too loud · The ears freeze · Oxygen fills the ears | Noise does not cause popping. · Cabins are warm. · It is about pressure, not oxygen. | Swallowing lets air in or out to balance the pressure on the eardrum. |
| Why are aircraft cabins pressurised? | At cruising height the air pressure is too low for people to breathe comfortably | To make the plane heavier · To keep the plane warm · To make the engines work | Pressurising does not add useful weight. · Heating is a separate system. · Engines take in outside air. | High up, the outside pressure is too low for healthy breathing. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why are aircraft cabins pressurised?

- ◻️ To keep the plane warm  
  _↳ feedback if chosen: Heating is a separate system._
- ◻️ To make the engines work  
  _↳ feedback if chosen: Engines take in outside air._
- ✅ At cruising height the air pressure is too low for people to breathe comfortably
- ◻️ To make the plane heavier  
  _↳ feedback if chosen: Pressurising does not add useful weight._

Full working after a second miss:

> High up, the outside pressure is too low for healthy breathing.  
> So the answer is At cruising height the air pressure is too low for people to breathe comfortably.  

> Why do some climbers feel dizzy near the summit of a high mountain?

- ✅ The low air pressure means less oxygen in each breath
- ◻️ The sun is closer  
  _↳ feedback if chosen: Distance to the sun is not the cause._
- ◻️ Their blood becomes heavier  
  _↳ feedback if chosen: Blood density does not change._
- ◻️ The air contains more oxygen  
  _↳ feedback if chosen: There is less oxygen per breath._

Full working after a second miss:

> Altitude sickness comes from low pressure and less oxygen.  
> So the answer is The low air pressure means less oxygen in each breath.  

> Why do some climbers feel dizzy near the summit of a high mountain?

- ✅ The low air pressure means less oxygen in each breath
- ◻️ The air contains more oxygen  
  _↳ feedback if chosen: There is less oxygen per breath._
- ◻️ The sun is closer  
  _↳ feedback if chosen: Distance to the sun is not the cause._
- ◻️ Their blood becomes heavier  
  _↳ feedback if chosen: Blood density does not change._

Full working after a second miss:

> Altitude sickness comes from low pressure and less oxygen.  
> So the answer is The low air pressure means less oxygen in each breath.  

Sources: pressure (Form 3 Physics syllabus, Term 1: pressure in solids, liquids and the atmosphere; the simple barometer; effects on boiling points and health)

### `p3-13-chain` · Lesson 13 · ordering, level 3

Prompt: Put the explanation in order: why does rice cook slowly near the top of Mount Cameroon?

Items in the right order:

1. The climber is very high up.
2. There is less air above, so the air pressure is lower.
3. Water boils at a temperature below 100 °C.
4. The boiling water is not as hot, so the rice cooks more slowly.


Three generated variants:

> Put the explanation in order: why does rice cook slowly near the top of Mount Cameroon?

Shown as: There is less air above, so the air pressure is lower. · The climber is very high up. · Water boils at a temperature below 100 °C. · The boiling water is not as hot, so the rice cooks more slowly.
Correct order: The climber is very high up. → There is less air above, so the air pressure is lower. → Water boils at a temperature below 100 °C. → The boiling water is not as hot, so the rice cooks more slowly.

Hint (draft): Start from the height and end with the cooking.

Full working after a second miss:

> The correct order is: The climber is very high up. → There is less air above, so the air pressure is lower. → Water boils at a temperature below 100 °C. → The boiling water is not as hot, so the rice cooks more slowly..  

> Put the explanation in order: why does rice cook slowly near the top of Mount Cameroon?

Shown as: The boiling water is not as hot, so the rice cooks more slowly. · There is less air above, so the air pressure is lower. · The climber is very high up. · Water boils at a temperature below 100 °C.
Correct order: The climber is very high up. → There is less air above, so the air pressure is lower. → Water boils at a temperature below 100 °C. → The boiling water is not as hot, so the rice cooks more slowly.

Hint (draft): Start from the height and end with the cooking.

Full working after a second miss:

> The correct order is: The climber is very high up. → There is less air above, so the air pressure is lower. → Water boils at a temperature below 100 °C. → The boiling water is not as hot, so the rice cooks more slowly..  

> Put the explanation in order: why does rice cook slowly near the top of Mount Cameroon?

Shown as: The boiling water is not as hot, so the rice cooks more slowly. · The climber is very high up. · There is less air above, so the air pressure is lower. · Water boils at a temperature below 100 °C.
Correct order: The climber is very high up. → There is less air above, so the air pressure is lower. → Water boils at a temperature below 100 °C. → The boiling water is not as hot, so the rice cooks more slowly.

Hint (draft): Start from the height and end with the cooking.

Full working after a second miss:

> The correct order is: The climber is very high up. → There is less air above, so the air pressure is lower. → Water boils at a temperature below 100 °C. → The boiling water is not as hot, so the rice cooks more slowly..  

Sources: pressure (Form 3 Physics syllabus, Term 1: pressure in solids, liquids and the atmosphere; the simple barometer; effects on boiling points and health)

### `p3-13-health-card` · Lesson 13 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do some climbers feel dizzy near the summit of a high mountain? | The low air pressure means less oxygen in each breath | The air contains more oxygen · Their blood becomes heavier · The sun is closer | There is less oxygen per breath. · Blood density does not change. · Distance to the sun is not the cause. | Altitude sickness comes from low pressure and less oxygen. |
| Why do your ears 'pop' when a plane takes off? | The outside pressure changes quickly and the pressure in the middle ear adjusts | The engine noise is too loud · The ears freeze · Oxygen fills the ears | Noise does not cause popping. · Cabins are warm. · It is about pressure, not oxygen. | Swallowing lets air in or out to balance the pressure on the eardrum. |
| Why are aircraft cabins pressurised? | At cruising height the air pressure is too low for people to breathe comfortably | To make the plane heavier · To keep the plane warm · To make the engines work | Pressurising does not add useful weight. · Heating is a separate system. · Engines take in outside air. | High up, the outside pressure is too low for healthy breathing. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why are aircraft cabins pressurised?

- ◻️ To keep the plane warm  
  _↳ feedback if chosen: Heating is a separate system._
- ✅ At cruising height the air pressure is too low for people to breathe comfortably
- ◻️ To make the engines work  
  _↳ feedback if chosen: Engines take in outside air._
- ◻️ To make the plane heavier  
  _↳ feedback if chosen: Pressurising does not add useful weight._

Full working after a second miss:

> High up, the outside pressure is too low for healthy breathing.  
> So the answer is At cruising height the air pressure is too low for people to breathe comfortably.  

> Why are aircraft cabins pressurised?

- ◻️ To make the engines work  
  _↳ feedback if chosen: Engines take in outside air._
- ◻️ To keep the plane warm  
  _↳ feedback if chosen: Heating is a separate system._
- ◻️ To make the plane heavier  
  _↳ feedback if chosen: Pressurising does not add useful weight._
- ✅ At cruising height the air pressure is too low for people to breathe comfortably

Full working after a second miss:

> High up, the outside pressure is too low for healthy breathing.  
> So the answer is At cruising height the air pressure is too low for people to breathe comfortably.  

> Why are aircraft cabins pressurised?

- ✅ At cruising height the air pressure is too low for people to breathe comfortably
- ◻️ To keep the plane warm  
  _↳ feedback if chosen: Heating is a separate system._
- ◻️ To make the engines work  
  _↳ feedback if chosen: Engines take in outside air._
- ◻️ To make the plane heavier  
  _↳ feedback if chosen: Pressurising does not add useful weight._

Full working after a second miss:

> High up, the outside pressure is too low for healthy breathing.  
> So the answer is At cruising height the air pressure is too low for people to breathe comfortably.  

Sources: pressure (Form 3 Physics syllabus, Term 1: pressure in solids, liquids and the atmosphere; the simple barometer; effects on boiling points and health)

### `p3-14-limit` · Lesson 14 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A spring is loaded beyond its elastic limit, then the load is removed. What happens? | It stays longer than its original length | It returns exactly to its original length · It becomes shorter than before · Its extension doubles | Only within the elastic limit does it return. · It is permanently stretched, not shortened. · There is no such rule. | Beyond the elastic limit the deformation is permanent. |
| Which material is plastic rather than elastic? | modelling clay | a rubber band · a steel spring · a tennis ball | A rubber band springs back. · A steel spring springs back within its limit. · A tennis ball regains its shape. | Clay keeps the new shape. |
| Hooke's law says the extension is proportional to the load… | provided the elastic limit is not exceeded | for any load · only for rubber · only when the spring is horizontal | Beyond the limit the graph curves. · It applies to springs and wires too. · Direction does not matter. | The law holds only up to the limit of proportionality. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A spring is loaded beyond its elastic limit, then the load is removed. What happens?

- ◻️ It becomes shorter than before  
  _↳ feedback if chosen: It is permanently stretched, not shortened._
- ◻️ Its extension doubles  
  _↳ feedback if chosen: There is no such rule._
- ◻️ It returns exactly to its original length  
  _↳ feedback if chosen: Only within the elastic limit does it return._
- ✅ It stays longer than its original length

Full working after a second miss:

> Beyond the elastic limit the deformation is permanent.  
> So the answer is It stays longer than its original length.  

> A spring is loaded beyond its elastic limit, then the load is removed. What happens?

- ✅ It stays longer than its original length
- ◻️ It becomes shorter than before  
  _↳ feedback if chosen: It is permanently stretched, not shortened._
- ◻️ Its extension doubles  
  _↳ feedback if chosen: There is no such rule._
- ◻️ It returns exactly to its original length  
  _↳ feedback if chosen: Only within the elastic limit does it return._

Full working after a second miss:

> Beyond the elastic limit the deformation is permanent.  
> So the answer is It stays longer than its original length.  

> Hooke's law says the extension is proportional to the load…

- ◻️ only when the spring is horizontal  
  _↳ feedback if chosen: Direction does not matter._
- ✅ provided the elastic limit is not exceeded
- ◻️ only for rubber  
  _↳ feedback if chosen: It applies to springs and wires too._
- ◻️ for any load  
  _↳ feedback if chosen: Beyond the limit the graph curves._

Full working after a second miss:

> The law holds only up to the limit of proportionality.  
> So the answer is provided the elastic limit is not exceeded.  

Sources: elasticity (Form 3 Physics syllabus, Term 1: elasticity, Hooke's law, elastic limit, force-extension graphs and applications)

### `p3-14-limit-card` · Lesson 14 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A spring is loaded beyond its elastic limit, then the load is removed. What happens? | It stays longer than its original length | It returns exactly to its original length · It becomes shorter than before · Its extension doubles | Only within the elastic limit does it return. · It is permanently stretched, not shortened. · There is no such rule. | Beyond the elastic limit the deformation is permanent. |
| Which material is plastic rather than elastic? | modelling clay | a rubber band · a steel spring · a tennis ball | A rubber band springs back. · A steel spring springs back within its limit. · A tennis ball regains its shape. | Clay keeps the new shape. |
| Hooke's law says the extension is proportional to the load… | provided the elastic limit is not exceeded | for any load · only for rubber · only when the spring is horizontal | Beyond the limit the graph curves. · It applies to springs and wires too. · Direction does not matter. | The law holds only up to the limit of proportionality. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Hooke's law says the extension is proportional to the load…

- ◻️ only when the spring is horizontal  
  _↳ feedback if chosen: Direction does not matter._
- ◻️ for any load  
  _↳ feedback if chosen: Beyond the limit the graph curves._
- ✅ provided the elastic limit is not exceeded
- ◻️ only for rubber  
  _↳ feedback if chosen: It applies to springs and wires too._

Full working after a second miss:

> The law holds only up to the limit of proportionality.  
> So the answer is provided the elastic limit is not exceeded.  

> Hooke's law says the extension is proportional to the load…

- ✅ provided the elastic limit is not exceeded
- ◻️ only when the spring is horizontal  
  _↳ feedback if chosen: Direction does not matter._
- ◻️ only for rubber  
  _↳ feedback if chosen: It applies to springs and wires too._
- ◻️ for any load  
  _↳ feedback if chosen: Beyond the limit the graph curves._

Full working after a second miss:

> The law holds only up to the limit of proportionality.  
> So the answer is provided the elastic limit is not exceeded.  

> Hooke's law says the extension is proportional to the load…

- ◻️ only when the spring is horizontal  
  _↳ feedback if chosen: Direction does not matter._
- ✅ provided the elastic limit is not exceeded
- ◻️ for any load  
  _↳ feedback if chosen: Beyond the limit the graph curves._
- ◻️ only for rubber  
  _↳ feedback if chosen: It applies to springs and wires too._

Full working after a second miss:

> The law holds only up to the limit of proportionality.  
> So the answer is provided the elastic limit is not exceeded.  

Sources: elasticity (Form 3 Physics syllabus, Term 1: elasticity, Hooke's law, elastic limit, force-extension graphs and applications)

### `p3-15-use` · Lesson 15 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which device uses a spring to measure force? | a spring balance (newton meter) | a beam balance · a thermometer · a measuring cylinder | A beam balance compares masses without a spring. · A thermometer measures temperature. · A measuring cylinder measures volume. | The extension of the spring shows the force. |
| Why do cars and motorbikes have springs in their suspension? | To absorb shocks from bumps in the road | To make the vehicle faster · To measure the speed · To make the vehicle heavier | Springs do not increase speed. · A speedometer measures speed. · That is not their purpose. | The springs stretch and compress, giving a smoother ride. |
| Which of these does NOT use an elastic material for its job? | a brick wall | a catapult · a trampoline · a mattress | A catapult stores energy in stretched rubber. · A trampoline bounces back. · A mattress springs back. | A wall must stay rigid; it does not use elasticity. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which of these does NOT use an elastic material for its job?

- ◻️ a trampoline  
  _↳ feedback if chosen: A trampoline bounces back._
- ◻️ a mattress  
  _↳ feedback if chosen: A mattress springs back._
- ◻️ a catapult  
  _↳ feedback if chosen: A catapult stores energy in stretched rubber._
- ✅ a brick wall

Full working after a second miss:

> A wall must stay rigid; it does not use elasticity.  
> So the answer is a brick wall.  

> Why do cars and motorbikes have springs in their suspension?

- ◻️ To make the vehicle faster  
  _↳ feedback if chosen: Springs do not increase speed._
- ◻️ To make the vehicle heavier  
  _↳ feedback if chosen: That is not their purpose._
- ✅ To absorb shocks from bumps in the road
- ◻️ To measure the speed  
  _↳ feedback if chosen: A speedometer measures speed._

Full working after a second miss:

> The springs stretch and compress, giving a smoother ride.  
> So the answer is To absorb shocks from bumps in the road.  

> Which device uses a spring to measure force?

- ◻️ a beam balance  
  _↳ feedback if chosen: A beam balance compares masses without a spring._
- ✅ a spring balance (newton meter)
- ◻️ a thermometer  
  _↳ feedback if chosen: A thermometer measures temperature._
- ◻️ a measuring cylinder  
  _↳ feedback if chosen: A measuring cylinder measures volume._

Full working after a second miss:

> The extension of the spring shows the force.  
> So the answer is a spring balance (newton meter).  

Sources: elasticity (Form 3 Physics syllabus, Term 1: elasticity, Hooke's law, elastic limit, force-extension graphs and applications)

### `p3-15-shape` · Lesson 15 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| On a load-extension graph for a spring, what does a straight line through the origin show? | Extension is proportional to load (Hooke's law) | The spring has broken · The load is constant · The spring is plastic | A broken spring gives no line. · The load changes along the axis. · A plastic material does not give a straight line through the origin. | Straight line through the origin: direct proportion. |
| After a certain load the graph starts to curve. This point is… | the limit of proportionality | the origin · the spring constant · the zero error | The origin is where the line starts. · The spring constant is the gradient. · A zero error is a wrong starting reading. | Beyond it, extension is no longer proportional to load. |
| Spring A has a steeper load-extension line than spring B. Which is stiffer? | A | B · They are equally stiff · It depends on their colour | B stretches more for the same load. · Different gradients mean different stiffness. · Colour does not matter. | A steeper line means more load for each centimetre: a larger k. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> On a load-extension graph for a spring, what does a straight line through the origin show?

- ◻️ The spring is plastic  
  _↳ feedback if chosen: A plastic material does not give a straight line through the origin._
- ◻️ The load is constant  
  _↳ feedback if chosen: The load changes along the axis._
- ◻️ The spring has broken  
  _↳ feedback if chosen: A broken spring gives no line._
- ✅ Extension is proportional to load (Hooke's law)

Full working after a second miss:

> Straight line through the origin: direct proportion.  
> So the answer is Extension is proportional to load (Hooke's law).  

> Spring A has a steeper load-extension line than spring B. Which is stiffer?

- ✅ A
- ◻️ It depends on their colour  
  _↳ feedback if chosen: Colour does not matter._
- ◻️ They are equally stiff  
  _↳ feedback if chosen: Different gradients mean different stiffness._
- ◻️ B  
  _↳ feedback if chosen: B stretches more for the same load._

Full working after a second miss:

> A steeper line means more load for each centimetre: a larger k.  
> So the answer is A.  

> On a load-extension graph for a spring, what does a straight line through the origin show?

- ◻️ The spring is plastic  
  _↳ feedback if chosen: A plastic material does not give a straight line through the origin._
- ✅ Extension is proportional to load (Hooke's law)
- ◻️ The spring has broken  
  _↳ feedback if chosen: A broken spring gives no line._
- ◻️ The load is constant  
  _↳ feedback if chosen: The load changes along the axis._

Full working after a second miss:

> Straight line through the origin: direct proportion.  
> So the answer is Extension is proportional to load (Hooke's law).  

Sources: elasticity (Form 3 Physics syllabus, Term 1: elasticity, Hooke's law, elastic limit, force-extension graphs and applications)

### `p3-16-form` · Lesson 16 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What form of energy does a stretched catapult rubber store? | elastic potential energy | kinetic energy · chemical energy · sound energy | It is not moving yet. · Chemical energy is stored in food and fuels. · It makes little sound. | Stretched or squeezed objects store elastic potential energy. |
| What form of energy is stored in a plate of rice and beans? | chemical energy | kinetic energy · nuclear energy · light energy | The food is not moving. · Nuclear energy is in the nucleus of atoms such as uranium. · Food does not shine. | Food stores chemical energy that the body releases. |
| A mango hanging high on a tree has… | gravitational potential energy | kinetic energy · electrical energy · sound energy | It is not moving. · It carries no current. · It makes no sound. | Its height gives it gravitational potential energy. |
| What is the SI unit of energy? | joule (J) | watt (W) · newton (N) · pascal (Pa) | The watt is the unit of power. · The newton is the unit of force. · The pascal is the unit of pressure. | Energy is measured in joules. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A mango hanging high on a tree has…

- ◻️ electrical energy  
  _↳ feedback if chosen: It carries no current._
- ◻️ sound energy  
  _↳ feedback if chosen: It makes no sound._
- ✅ gravitational potential energy
- ◻️ kinetic energy  
  _↳ feedback if chosen: It is not moving._

Full working after a second miss:

> Its height gives it gravitational potential energy.  
> So the answer is gravitational potential energy.  

> A mango hanging high on a tree has…

- ◻️ kinetic energy  
  _↳ feedback if chosen: It is not moving._
- ◻️ sound energy  
  _↳ feedback if chosen: It makes no sound._
- ◻️ electrical energy  
  _↳ feedback if chosen: It carries no current._
- ✅ gravitational potential energy

Full working after a second miss:

> Its height gives it gravitational potential energy.  
> So the answer is gravitational potential energy.  

> A mango hanging high on a tree has…

- ◻️ kinetic energy  
  _↳ feedback if chosen: It is not moving._
- ◻️ electrical energy  
  _↳ feedback if chosen: It carries no current._
- ◻️ sound energy  
  _↳ feedback if chosen: It makes no sound._
- ✅ gravitational potential energy

Full working after a second miss:

> Its height gives it gravitational potential energy.  
> So the answer is gravitational potential energy.  

Sources: energy (Form 3 Physics syllabus, Term 1: energy forms and sources (renewable and non-renewable), conservation of energy, transducers, energy flow diagrams, simple calculations)

### `p3-16-src` · Lesson 16 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which source of energy is renewable? | hydroelectricity from a dam | petrol · natural gas · coal | Petrol comes from crude oil, which will run out. · Natural gas is a fossil fuel. · Coal is a fossil fuel. | Rain refills the river behind the dam. |
| Which source of energy is non-renewable? | kerosene | solar energy · wind energy · firewood from replanted forests | The sun keeps shining. · Wind keeps blowing. · Replanted trees grow again. | Kerosene comes from petroleum, which forms over millions of years. |
| Why is wood called renewable only if trees are replanted? | Cutting trees faster than they grow uses up the forest | Wood is a fossil fuel · Wood never burns completely · Trees grow back in one day | Wood is biomass, not a fossil fuel. · Burning has nothing to do with it. · Trees take years to grow. | Biomass is renewable only when it is replaced. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is wood called renewable only if trees are replanted?

- ◻️ Trees grow back in one day  
  _↳ feedback if chosen: Trees take years to grow._
- ✅ Cutting trees faster than they grow uses up the forest
- ◻️ Wood is a fossil fuel  
  _↳ feedback if chosen: Wood is biomass, not a fossil fuel._
- ◻️ Wood never burns completely  
  _↳ feedback if chosen: Burning has nothing to do with it._

Full working after a second miss:

> Biomass is renewable only when it is replaced.  
> So the answer is Cutting trees faster than they grow uses up the forest.  

> Which source of energy is non-renewable?

- ✅ kerosene
- ◻️ solar energy  
  _↳ feedback if chosen: The sun keeps shining._
- ◻️ firewood from replanted forests  
  _↳ feedback if chosen: Replanted trees grow again._
- ◻️ wind energy  
  _↳ feedback if chosen: Wind keeps blowing._

Full working after a second miss:

> Kerosene comes from petroleum, which forms over millions of years.  
> So the answer is kerosene.  

> Why is wood called renewable only if trees are replanted?

- ◻️ Wood never burns completely  
  _↳ feedback if chosen: Burning has nothing to do with it._
- ◻️ Wood is a fossil fuel  
  _↳ feedback if chosen: Wood is biomass, not a fossil fuel._
- ✅ Cutting trees faster than they grow uses up the forest
- ◻️ Trees grow back in one day  
  _↳ feedback if chosen: Trees take years to grow._

Full working after a second miss:

> Biomass is renewable only when it is replaced.  
> So the answer is Cutting trees faster than they grow uses up the forest.  

Sources: energy (Form 3 Physics syllabus, Term 1: energy forms and sources (renewable and non-renewable), conservation of energy, transducers, energy flow diagrams, simple calculations)

### `p3-16-adv` · Lesson 16 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is one disadvantage of solar panels? | They produce little at night or on cloudy days | They release a lot of carbon dioxide · Sunlight will soon run out · They need petrol to work | They release no carbon dioxide when working. · The sun will shine for billions of years. · They need only sunlight. | Solar power depends on the weather and time of day. |
| What is one disadvantage of burning fossil fuels? | They release carbon dioxide and pollute the air | They are renewable · They cannot be burned · They give no heat | Fossil fuels are non-renewable. · They burn easily. · They give a lot of heat. | Carbon dioxide contributes to climate change. |
| What is one advantage of hydroelectricity for Cameroon? | It uses rivers that are renewed by rain and releases little pollution | It works without water · It can be built anywhere · It is non-renewable | It needs flowing water. · It needs a suitable river and valley. · It is renewable. | Rivers such as the Sanaga provide renewable energy. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is one advantage of hydroelectricity for Cameroon?

- ◻️ It can be built anywhere  
  _↳ feedback if chosen: It needs a suitable river and valley._
- ◻️ It works without water  
  _↳ feedback if chosen: It needs flowing water._
- ✅ It uses rivers that are renewed by rain and releases little pollution
- ◻️ It is non-renewable  
  _↳ feedback if chosen: It is renewable._

Full working after a second miss:

> Rivers such as the Sanaga provide renewable energy.  
> So the answer is It uses rivers that are renewed by rain and releases little pollution.  

> What is one disadvantage of solar panels?

- ◻️ Sunlight will soon run out  
  _↳ feedback if chosen: The sun will shine for billions of years._
- ◻️ They need petrol to work  
  _↳ feedback if chosen: They need only sunlight._
- ✅ They produce little at night or on cloudy days
- ◻️ They release a lot of carbon dioxide  
  _↳ feedback if chosen: They release no carbon dioxide when working._

Full working after a second miss:

> Solar power depends on the weather and time of day.  
> So the answer is They produce little at night or on cloudy days.  

> What is one disadvantage of burning fossil fuels?

- ◻️ They are renewable  
  _↳ feedback if chosen: Fossil fuels are non-renewable._
- ◻️ They cannot be burned  
  _↳ feedback if chosen: They burn easily._
- ◻️ They give no heat  
  _↳ feedback if chosen: They give a lot of heat._
- ✅ They release carbon dioxide and pollute the air

Full working after a second miss:

> Carbon dioxide contributes to climate change.  
> So the answer is They release carbon dioxide and pollute the air.  

Sources: energy (Form 3 Physics syllabus, Term 1: energy forms and sources (renewable and non-renewable), conservation of energy, transducers, energy flow diagrams, simple calculations)

### `p3-16-change` · Lesson 16 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A girl climbs to the top of a slide, then slides down. Which energy change happens as she slides? | gravitational potential energy → kinetic energy (and some heat) | kinetic energy → chemical energy · electrical energy → sound energy · chemical energy → nuclear energy | She is not storing energy chemically as she slides. · No electricity is involved. · No nuclear change happens. | She loses height and gains speed; friction makes some heat. |
| A battery-powered torch is switched on. What is the main energy change in the battery? | chemical → electrical | electrical → chemical · light → electrical · kinetic → chemical | That happens when charging. · That happens in a solar cell. · The battery is not moving. | Chemicals in the battery react to give electrical energy. |
| In a hydroelectric power station, what is the order of energy changes? | potential (stored water) → kinetic (falling water) → electrical | electrical → kinetic → potential · chemical → heat → electrical · nuclear → heat → electrical | That is backwards. · That describes a fuel-burning station. · That describes a nuclear station. | Water high behind the dam falls, turns turbines and generators. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In a hydroelectric power station, what is the order of energy changes?

- ◻️ nuclear → heat → electrical  
  _↳ feedback if chosen: That describes a nuclear station._
- ✅ potential (stored water) → kinetic (falling water) → electrical
- ◻️ chemical → heat → electrical  
  _↳ feedback if chosen: That describes a fuel-burning station._
- ◻️ electrical → kinetic → potential  
  _↳ feedback if chosen: That is backwards._

Full working after a second miss:

> Water high behind the dam falls, turns turbines and generators.  
> So the answer is potential (stored water) → kinetic (falling water) → electrical.  

> A battery-powered torch is switched on. What is the main energy change in the battery?

- ✅ chemical → electrical
- ◻️ kinetic → chemical  
  _↳ feedback if chosen: The battery is not moving._
- ◻️ electrical → chemical  
  _↳ feedback if chosen: That happens when charging._
- ◻️ light → electrical  
  _↳ feedback if chosen: That happens in a solar cell._

Full working after a second miss:

> Chemicals in the battery react to give electrical energy.  
> So the answer is chemical → electrical.  

> A girl climbs to the top of a slide, then slides down. Which energy change happens as she slides?

- ◻️ kinetic energy → chemical energy  
  _↳ feedback if chosen: She is not storing energy chemically as she slides._
- ✅ gravitational potential energy → kinetic energy (and some heat)
- ◻️ chemical energy → nuclear energy  
  _↳ feedback if chosen: No nuclear change happens._
- ◻️ electrical energy → sound energy  
  _↳ feedback if chosen: No electricity is involved._

Full working after a second miss:

> She loses height and gains speed; friction makes some heat.  
> So the answer is gravitational potential energy → kinetic energy (and some heat).  

Sources: energy (Form 3 Physics syllabus, Term 1: energy forms and sources (renewable and non-renewable), conservation of energy, transducers, energy flow diagrams, simple calculations)

### `p3-16-adv-card` · Lesson 16 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is one disadvantage of solar panels? | They produce little at night or on cloudy days | They release a lot of carbon dioxide · Sunlight will soon run out · They need petrol to work | They release no carbon dioxide when working. · The sun will shine for billions of years. · They need only sunlight. | Solar power depends on the weather and time of day. |
| What is one disadvantage of burning fossil fuels? | They release carbon dioxide and pollute the air | They are renewable · They cannot be burned · They give no heat | Fossil fuels are non-renewable. · They burn easily. · They give a lot of heat. | Carbon dioxide contributes to climate change. |
| What is one advantage of hydroelectricity for Cameroon? | It uses rivers that are renewed by rain and releases little pollution | It works without water · It can be built anywhere · It is non-renewable | It needs flowing water. · It needs a suitable river and valley. · It is renewable. | Rivers such as the Sanaga provide renewable energy. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is one disadvantage of burning fossil fuels?

- ◻️ They cannot be burned  
  _↳ feedback if chosen: They burn easily._
- ◻️ They give no heat  
  _↳ feedback if chosen: They give a lot of heat._
- ✅ They release carbon dioxide and pollute the air
- ◻️ They are renewable  
  _↳ feedback if chosen: Fossil fuels are non-renewable._

Full working after a second miss:

> Carbon dioxide contributes to climate change.  
> So the answer is They release carbon dioxide and pollute the air.  

> What is one disadvantage of burning fossil fuels?

- ◻️ They give no heat  
  _↳ feedback if chosen: They give a lot of heat._
- ✅ They release carbon dioxide and pollute the air
- ◻️ They cannot be burned  
  _↳ feedback if chosen: They burn easily._
- ◻️ They are renewable  
  _↳ feedback if chosen: Fossil fuels are non-renewable._

Full working after a second miss:

> Carbon dioxide contributes to climate change.  
> So the answer is They release carbon dioxide and pollute the air.  

> What is one advantage of hydroelectricity for Cameroon?

- ◻️ It can be built anywhere  
  _↳ feedback if chosen: It needs a suitable river and valley._
- ✅ It uses rivers that are renewed by rain and releases little pollution
- ◻️ It is non-renewable  
  _↳ feedback if chosen: It is renewable._
- ◻️ It works without water  
  _↳ feedback if chosen: It needs flowing water._

Full working after a second miss:

> Rivers such as the Sanaga provide renewable energy.  
> So the answer is It uses rivers that are renewed by rain and releases little pollution.  

Sources: energy (Form 3 Physics syllabus, Term 1: energy forms and sources (renewable and non-renewable), conservation of energy, transducers, energy flow diagrams, simple calculations)

### `p3-17-trans` · Lesson 17 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What energy change happens in a microphone? | sound → electrical | electrical → sound · light → electrical · kinetic → light | That is a loudspeaker. · That is a solar cell. · No light is produced. | A microphone turns sound waves into electrical signals. |
| What energy change happens in a solar cell? | light → electrical | electrical → light · chemical → electrical · heat → sound | That is a lamp. · That is a battery. · That is not what a solar cell does. | Sunlight falling on the cell produces electricity. |
| Which device changes electrical energy into kinetic energy? | an electric motor | a dynamo · a microphone · a solar cell | A dynamo does the opposite (kinetic → electrical). · A microphone gives electrical energy from sound. · A solar cell gives electrical energy from light. | A motor turns electricity into motion, as in a fan. |
| A bicycle dynamo lights a lamp. What is the energy change in the dynamo? | kinetic → electrical | electrical → kinetic · chemical → light · sound → electrical | That is a motor. · The dynamo uses motion, not chemicals. · That is a microphone. | The turning wheel drives the dynamo, which produces electricity. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What energy change happens in a solar cell?

- ◻️ chemical → electrical  
  _↳ feedback if chosen: That is a battery._
- ◻️ heat → sound  
  _↳ feedback if chosen: That is not what a solar cell does._
- ✅ light → electrical
- ◻️ electrical → light  
  _↳ feedback if chosen: That is a lamp._

Full working after a second miss:

> Sunlight falling on the cell produces electricity.  
> So the answer is light → electrical.  

> A bicycle dynamo lights a lamp. What is the energy change in the dynamo?

- ✅ kinetic → electrical
- ◻️ sound → electrical  
  _↳ feedback if chosen: That is a microphone._
- ◻️ electrical → kinetic  
  _↳ feedback if chosen: That is a motor._
- ◻️ chemical → light  
  _↳ feedback if chosen: The dynamo uses motion, not chemicals._

Full working after a second miss:

> The turning wheel drives the dynamo, which produces electricity.  
> So the answer is kinetic → electrical.  

> What energy change happens in a solar cell?

- ◻️ chemical → electrical  
  _↳ feedback if chosen: That is a battery._
- ◻️ electrical → light  
  _↳ feedback if chosen: That is a lamp._
- ◻️ heat → sound  
  _↳ feedback if chosen: That is not what a solar cell does._
- ✅ light → electrical

Full working after a second miss:

> Sunlight falling on the cell produces electricity.  
> So the answer is light → electrical.  

Sources: energy (Form 3 Physics syllabus, Term 1: energy forms and sources (renewable and non-renewable), conservation of energy, transducers, energy flow diagrams, simple calculations)

