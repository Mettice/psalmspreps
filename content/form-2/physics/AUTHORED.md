# Physics Form 2, Batches P2-1, P2-2: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f2-physics`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: rules the computed answers use (src/engine/lib/science2.js, physics.js)

- **Speed**: v = d ÷ t; km/h ÷ 3.6 = m/s (20 m/s for 72 km/h). **Density**: mass ÷ volume, to 2 decimals. **Temperature**: T(K) = T(°C) + 273.
- **Data**: the mean of repeated readings; an anomalous reading is left out; graphs are drawn from the question's own numbers (lineGraph).

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `p2-1-kind` | 1 | matching, 1 | scientific-method |
| 2 | `p2-1-why` | 1 | multiple choice, 2 | scientific-method |
| 3 | `p2-1-c4` (card c1-4) | 1 | multiple choice, 1 | scientific-method |
| 4 | `p2-2-trend` | 2 | multiple choice, 1 | scientific-method |
| 5 | `p2-2-conclude` | 2 | multiple choice, 1 | scientific-method |
| 6 | `p2-3-var` | 3 | matching, 1 | scientific-method |
| 7 | `p2-3-improve` | 3 | multiple choice, 1 | scientific-method |
| 8 | `p2-3-spot` | 3 | spot the error, 3 | scientific-method |
| 9 | `p2-4-unit` | 4 | matching, 1 | measurement |
| 10 | `p2-4-tool` | 4 | matching, 1 | measurement |
| 11 | `p2-4-which` | 4 | multiple choice, 2 | measurement |
| 12 | `p2-5-measure` | 5 | multiple choice, 1 | speed |
| 13 | `p2-7-float` | 7 | multiple choice, 1 | measurement |
| 14 | `p2-8-sort` | 8 | matching, 1 | matter |
| 15 | `p2-8-same` | 8 | multiple choice, 1 | matter |
| 16 | `p2-8-life` | 8 | multiple choice, 2 | matter |
| 17 | `p2-8-spot` | 8 | spot the error, 3 | matter |
| 18 | `p2-9-props` | 9 | matching, 1 | matter |
| 19 | `p2-9-particles` | 9 | multiple choice, 1 | matter |
| 20 | `p2-9-compress` | 9 | multiple choice, 2 | matter |
| 21 | `p2-9-spot` | 9 | spot the error, 3 | matter |
| 22 | `p2-9-compress-card` (card c9-3) | 9 | multiple choice, 1 | matter |
| 23 | `p2-10-effect` | 10 | multiple choice, 1 | heat-electricity |
| 24 | `p2-11-sort` | 11 | matching, 1 | heat-electricity |
| 25 | `p2-11-thermal` | 11 | multiple choice, 1 | heat-electricity |
| 26 | `p2-11-safe` | 11 | multiple choice, 2 | heat-electricity |
| 27 | `p2-11-spot` | 11 | spot the error, 3 | heat-electricity |
| 28 | `p2-11-safe-card` (card c11-3) | 11 | multiple choice, 1 | heat-electricity |
| 29 | `p2-12-expand` | 12 | multiple choice, 1 | heat-electricity |
| 30 | `p2-12-reverse` | 12 | matching, 1 | heat-electricity |
| 31 | `p2-12-bimetal` | 12 | multiple choice, 2 | heat-electricity |
| 32 | `p2-12-spot` | 12 | spot the error, 3 | heat-electricity |
| 33 | `p2-12-bimetal-card` (card c12-3) | 12 | multiple choice, 1 | heat-electricity |
| 34 | `p2-13-effect` | 13 | matching, 1 | heat-electricity |
| 35 | `p2-13-fuse` | 13 | multiple choice, 1 | heat-electricity |
| 36 | `p2-13-energy` | 13 | multiple choice, 2 | energy-sources |
| 37 | `p2-13-spot` | 13 | spot the error, 3 | heat-electricity |
| 38 | `p2-13-energy-card` (card c13-3) | 13 | multiple choice, 1 | energy-sources |
| 39 | `p2-14-what` | 14 | multiple choice, 1 | heat-electricity |
| 40 | `p2-14-order` | 14 | ordering, 1 | heat-electricity |
| 41 | `p2-14-circuit` | 14 | multiple choice, 1 | heat-electricity |
| 42 | `p2-14-wax` | 14 | multiple choice, 2 | heat-electricity |
| 43 | `p2-14-spot` | 14 | spot the error, 3 | heat-electricity |
| 44 | `p2-15-sort` | 15 | matching, 1 | energy-sources |
| 45 | `p2-15-fossil` | 15 | multiple choice, 1 | energy-sources |
| 46 | `p2-15-problem` | 15 | multiple choice, 2 | energy-sources |
| 47 | `p2-15-spot` | 15 | spot the error, 3 | energy-sources |
| 48 | `p2-15-problem-card` (card c15-3) | 15 | multiple choice, 1 | energy-sources |
| 49 | `p2-16-kind` | 16 | multiple choice, 1 | energy-sources |
| 50 | `p2-16-match` | 16 | matching, 1 | energy-sources |
| 51 | `p2-16-use` | 16 | multiple choice, 2 | energy-sources |
| 52 | `p2-16-spot` | 16 | spot the error, 3 | energy-sources |
| 53 | `p2-16-use-card` (card c16-2) | 16 | multiple choice, 1 | energy-sources |
| 54 | `p2-17-why` | 17 | multiple choice, 1 | heat-electricity |
| 55 | `p2-17-part` | 17 | matching, 1 | heat-electricity |
| 56 | `p2-17-spot` | 17 | spot the error, 3 | heat-electricity |
| 57 | `p2-18-closed` | 18 | multiple choice, 1 | heat-electricity |
| 58 | `p2-18-spot` | 18 | spot the error, 3 | heat-electricity |
| 59 | `p2-19-lum` | 19 | multiple choice, 1 | light |
| 60 | `p2-19-nat` | 19 | multiple choice, 1 | light |
| 61 | `p2-19-led` | 19 | multiple choice, 2 | light |
| 62 | `p2-19-spot` | 19 | spot the error, 3 | light |
| 63 | `p2-19-led-card` (card c19-3) | 19 | multiple choice, 1 | light |
| 64 | `p2-20-rec` | 20 | multiple choice, 1 | light |
| 65 | `p2-20-mat` | 20 | multiple choice, 1 | light |
| 66 | `p2-20-shadow` | 20 | multiple choice, 2 | light |
| 67 | `p2-20-spot` | 20 | spot the error, 3 | light |
| 68 | `p2-20-shadow-card` (card c20-3) | 20 | multiple choice, 1 | light |
| 69 | `p2-21-beam` | 21 | multiple choice, 1 | light |
| 70 | `p2-21-kind` | 21 | multiple choice, 1 | light |
| 71 | `p2-21-spot` | 21 | spot the error, 3 | light |
| 72 | `p2-22-chain` | 22 | matching, 1 | energy-sources |
| 73 | `p2-22-form` | 22 | multiple choice, 1 | energy-sources |
| 74 | `p2-22-waste` | 22 | multiple choice, 2 | energy-sources |
| 75 | `p2-22-spot` | 22 | spot the error, 3 | energy-sources |
| 76 | `p2-22-waste-card` (card c22-3) | 22 | multiple choice, 1 | energy-sources |
| 77 | `p2-23-blood` | 23 | multiple choice, 2 | pressure-health |
| 78 | `p2-23-spot` | 23 | spot the error, 3 | pressure-health |
| 79 | `p2-23-blood-card` (card c23-3) | 23 | multiple choice, 1 | pressure-health |
| 80 | `p2-24-why` | 24 | multiple choice, 1 | pressure-health |
| 81 | `p2-24-safe` | 24 | spot the error, 3 | pressure-health |
| 82 | `p2-24-safe-card` (card c24-3) | 24 | spot the error, 1 | pressure-health |
| 83 | `p2-25-eye` | 25 | matching, 1 | light |
| 84 | `p2-25-defect` | 25 | multiple choice, 1 | light |
| 85 | `p2-25-spot` | 25 | spot the error, 3 | light |
| 86 | `p2-26-def` | 26 | multiple choice, 1 | radiation-climate |
| 87 | `p2-26-good` | 26 | multiple choice, 1 | radiation-climate |
| 88 | `p2-26-park` | 26 | multiple choice, 2 | radiation-climate |
| 89 | `p2-26-spot` | 26 | spot the error, 3 | radiation-climate |
| 90 | `p2-26-park-card` (card c26-3) | 26 | multiple choice, 1 | radiation-climate |
| 91 | `p2-27-kind` | 27 | multiple choice, 1 | radiation-climate |
| 92 | `p2-27-emit` | 27 | multiple choice, 1 | radiation-climate |
| 93 | `p2-27-effect` | 27 | multiple choice, 2 | radiation-climate |
| 94 | `p2-27-spot` | 27 | spot the error, 3 | radiation-climate |
| 95 | `p2-27-effect-card` (card c27-3) | 27 | multiple choice, 1 | radiation-climate |
| 96 | `p2-28-kind` | 28 | multiple choice, 1 | radiation-climate |
| 97 | `p2-28-protect` | 28 | multiple choice, 2 | radiation-climate |
| 98 | `p2-28-spot` | 28 | spot the error, 3 | radiation-climate |
| 99 | `p2-28-protect-card` (card c28-3) | 28 | multiple choice, 1 | radiation-climate |
| 100 | `p2-29-gas` | 29 | multiple choice, 1 | radiation-climate |
| 101 | `p2-29-good` | 29 | ordering, 1 | radiation-climate |
| 102 | `p2-29-human` | 29 | multiple choice, 2 | radiation-climate |
| 103 | `p2-29-spot` | 29 | spot the error, 3 | radiation-climate |
| 104 | `p2-29-human-card` (card c29-3) | 29 | multiple choice, 1 | radiation-climate |
| 105 | `p2-30-def` | 30 | multiple choice, 1 | radiation-climate |
| 106 | `p2-30-effect` | 30 | multiple choice, 1 | radiation-climate |
| 107 | `p2-30-solve` | 30 | multiple choice, 2 | radiation-climate |
| 108 | `p2-30-spot` | 30 | spot the error, 3 | radiation-climate |
| 109 | `p2-30-solve-card` (card c30-3) | 30 | multiple choice, 1 | radiation-climate |
| 110 | `p2-31-def` | 31 | multiple choice, 1 | radiation-climate |
| 111 | `p2-31-effect` | 31 | multiple choice, 1 | radiation-climate |
| 112 | `p2-31-adapt` | 31 | multiple choice, 2 | radiation-climate |
| 113 | `p2-31-spot` | 31 | spot the error, 3 | radiation-climate |
| 114 | `p2-31-adapt-card` (card c31-3) | 31 | multiple choice, 1 | radiation-climate |

### `p2-1-kind` · Lesson 1 · matching, level 1

Prompt: Sort the data: qualitative or quantitative?

Pairs (4 shown each time, sorted into groups):

- the liquid turned milky → **qualitative**
- a strong smell of gas → **qualitative**
- the leaf is dark green → **qualitative**
- the metal felt rough → **qualitative**
- a length of 15.2 cm → **quantitative**
- a temperature of 37 °C → **quantitative**
- a mass of 250 g → **quantitative**
- a time of 45 s → **quantitative**


Three generated variants:

> Sort the data: qualitative or quantitative?

Groups: qualitative · quantitative
- a strong smell of gas → **qualitative**
- the leaf is dark green → **qualitative**
- a length of 15.2 cm → **quantitative**
- a temperature of 37 °C → **quantitative**

Full working after a second miss:

> The right pairs are:  
> a strong smell of gas → qualitative  
> the leaf is dark green → qualitative  
> a length of 15.2 cm → quantitative  
> a temperature of 37 °C → quantitative  

> Sort the data: qualitative or quantitative?

Groups: qualitative · quantitative
- the liquid turned milky → **qualitative**
- a mass of 250 g → **quantitative**
- a time of 45 s → **quantitative**
- a strong smell of gas → **qualitative**

Full working after a second miss:

> The right pairs are:  
> the liquid turned milky → qualitative  
> a mass of 250 g → quantitative  
> a time of 45 s → quantitative  
> a strong smell of gas → qualitative  

> Sort the data: qualitative or quantitative?

Groups: qualitative · quantitative
- the metal felt rough → **qualitative**
- a mass of 250 g → **quantitative**
- the liquid turned milky → **qualitative**
- a temperature of 37 °C → **quantitative**

Full working after a second miss:

> The right pairs are:  
> the metal felt rough → qualitative  
> a mass of 250 g → quantitative  
> the liquid turned milky → qualitative  
> a temperature of 37 °C → quantitative  

Sources: scientific-method (The scientific method as taught in Cameroonian secondary physics: data, tables, graphs, fair tests, evaluation)

### `p2-1-why` · Lesson 1 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do scientists repeat a measurement several times? | To check it and make the result more reliable. | To make the numbers bigger. · Because the first reading is always wrong. · To use up time. | Repeating does not change the size of the result. · The first reading may be right; repeating checks it. · That is not a reason. | Repeats show mistakes and give a more reliable mean. |
| Why is data needed in an experiment? | It is the evidence for the conclusion. | It makes the report longer. · Teachers like numbers. · It replaces the method. | Length is not the reason. · That is not the reason. · The method is still needed. | A conclusion must be based on data. |
| What should you do with an anomalous reading? | Check it, repeat it, and leave it out of the mean. | Keep it and make the others match. · Change it to look right. · Use only that reading. | Never change good readings. · Never change data. · It is the odd one out. | An anomalous reading is checked and left out of the mean. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What should you do with an anomalous reading?

- ◻️ Keep it and make the others match.  
  _↳ feedback if chosen: Never change good readings._
- ◻️ Use only that reading.  
  _↳ feedback if chosen: It is the odd one out._
- ✅ Check it, repeat it, and leave it out of the mean.
- ◻️ Change it to look right.  
  _↳ feedback if chosen: Never change data._

Full working after a second miss:

> An anomalous reading is checked and left out of the mean.  
> So the answer is “Check it, repeat it, and leave it out of the mean.”.  

> Why do scientists repeat a measurement several times?

- ◻️ Because the first reading is always wrong.  
  _↳ feedback if chosen: The first reading may be right; repeating checks it._
- ✅ To check it and make the result more reliable.
- ◻️ To make the numbers bigger.  
  _↳ feedback if chosen: Repeating does not change the size of the result._
- ◻️ To use up time.  
  _↳ feedback if chosen: That is not a reason._

Full working after a second miss:

> Repeats show mistakes and give a more reliable mean.  
> So the answer is “To check it and make the result more reliable.”.  

> Why is data needed in an experiment?

- ✅ It is the evidence for the conclusion.
- ◻️ It makes the report longer.  
  _↳ feedback if chosen: Length is not the reason._
- ◻️ Teachers like numbers.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ It replaces the method.  
  _↳ feedback if chosen: The method is still needed._

Full working after a second miss:

> A conclusion must be based on data.  
> So the answer is “It is the evidence for the conclusion.”.  

Sources: scientific-method (The scientific method as taught in Cameroonian secondary physics: data, tables, graphs, fair tests, evaluation)

### `p2-1-c4` · Lesson 1 · multiple choice, level 1

Prompt: Which is the best column heading for {X.q}?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| times measured in seconds | Time (s) | Seconds · Time · s (Time) | Give the quantity, then the unit in brackets. · Add the unit in brackets: Time (s). · Quantity first, then the unit: Time (s). | Quantity, then the unit in brackets. |
| masses measured in grams | Mass (g) | Grams · Mass · g | Give the quantity, then the unit. · Add the unit: Mass (g). · Give the quantity too: Mass (g). | Quantity, then the unit in brackets. |
| temperatures in degrees Celsius | Temperature (°C) | °C · Temperature · Hotness (°C) | Give the quantity too. · Add the unit: Temperature (°C). · The quantity is temperature. | Quantity, then the unit in brackets. |
| lengths in centimetres | Length (cm) | cm · Length · Centimetres long | Give the quantity too. · Add the unit: Length (cm). · Quantity, then unit in brackets. | Quantity, then the unit in brackets. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is the best column heading for temperatures in degrees Celsius?

- ◻️ °C  
  _↳ feedback if chosen: Give the quantity too._
- ◻️ Hotness (°C)  
  _↳ feedback if chosen: The quantity is temperature._
- ✅ Temperature (°C)
- ◻️ Temperature  
  _↳ feedback if chosen: Add the unit: Temperature (°C)._

Full working after a second miss:

> Quantity, then the unit in brackets.  
> So the answer is “Temperature (°C)”.  

> Which is the best column heading for times measured in seconds?

- ◻️ s (Time)  
  _↳ feedback if chosen: Quantity first, then the unit: Time (s)._
- ◻️ Seconds  
  _↳ feedback if chosen: Give the quantity, then the unit in brackets._
- ◻️ Time  
  _↳ feedback if chosen: Add the unit in brackets: Time (s)._
- ✅ Time (s)

Full working after a second miss:

> Quantity, then the unit in brackets.  
> So the answer is “Time (s)”.  

> Which is the best column heading for times measured in seconds?

- ✅ Time (s)
- ◻️ Time  
  _↳ feedback if chosen: Add the unit in brackets: Time (s)._
- ◻️ s (Time)  
  _↳ feedback if chosen: Quantity first, then the unit: Time (s)._
- ◻️ Seconds  
  _↳ feedback if chosen: Give the quantity, then the unit in brackets._

Full working after a second miss:

> Quantity, then the unit in brackets.  
> So the answer is “Time (s)”.  

Sources: scientific-method (The scientific method as taught in Cameroonian secondary physics: data, tables, graphs, fair tests, evaluation)

### `p2-2-trend` · Lesson 2 · multiple choice, level 1

Prompt: {T[0]} What is the trend?

Table `T` (one row is picked each time):

| 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| The longer a pot of water is heated, the higher its temperature. | the temperature increases with time | the temperature decreases with time | the temperature stays the same | The temperature goes up as time goes on. |
| The further a torch is from a wall, the dimmer the light on the wall. | the brightness decreases with distance | the brightness increases with distance | the brightness stays the same | The light gets dimmer as the distance grows. |
| The more mass hung on a spring, the longer the spring. | the length increases with mass | the length decreases with mass | the length stays the same | The spring gets longer as the mass grows. |
| As a hot drink cools in a room, its temperature falls. | the temperature decreases with time | the temperature increases with time | the temperature stays the same | The temperature goes down as time goes on. |

Right answer: `{T[1]}`; wrong choices: `{T[2]}`, `{T[3]}`

- Feedback `w1`: “Read the description again: {T[4]}”
- Feedback `w2`: “Something changes: {T[4]}”

Three generated variants:

> The further a torch is from a wall, the dimmer the light on the wall. What is the trend?

- ◻️ the brightness increases with distance  
  _↳ feedback if chosen: Read the description again: The light gets dimmer as the distance grows._
- ◻️ the brightness stays the same  
  _↳ feedback if chosen: Something changes: The light gets dimmer as the distance grows._
- ✅ the brightness decreases with distance

Full working after a second miss:

> The light gets dimmer as the distance grows.  
> So the trend is: the brightness decreases with distance.  

> The more mass hung on a spring, the longer the spring. What is the trend?

- ✅ the length increases with mass
- ◻️ the length stays the same  
  _↳ feedback if chosen: Something changes: The spring gets longer as the mass grows._
- ◻️ the length decreases with mass  
  _↳ feedback if chosen: Read the description again: The spring gets longer as the mass grows._

Full working after a second miss:

> The spring gets longer as the mass grows.  
> So the trend is: the length increases with mass.  

> The further a torch is from a wall, the dimmer the light on the wall. What is the trend?

- ◻️ the brightness increases with distance  
  _↳ feedback if chosen: Read the description again: The light gets dimmer as the distance grows._
- ◻️ the brightness stays the same  
  _↳ feedback if chosen: Something changes: The light gets dimmer as the distance grows._
- ✅ the brightness decreases with distance

Full working after a second miss:

> The light gets dimmer as the distance grows.  
> So the trend is: the brightness decreases with distance.  

Sources: scientific-method (The scientific method as taught in Cameroonian secondary physics: data, tables, graphs, fair tests, evaluation)

### `p2-2-conclude` · Lesson 2 · multiple choice, level 1

Prompt: A pupil heated water and recorded that its temperature rose by the same amount every minute. Which conclusion is best?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ As the heating time increases, the temperature of the water increases steadily.
- ✅ The temperature of the water rose at a steady rate while it was heated.
- ❌ Water boils at every temperature.  
  _↳ The data do not show that._
- ❌ All liquids heat up at the same rate as water.  
  _↳ Only water was tested: the data cannot say that._
- ❌ The temperature went down while heating.  
  _↳ The data show it went up._
- ❌ Heating water is dangerous.  
  _↳ That does not answer the question from the data._


Three generated variants:

> A pupil heated water and recorded that its temperature rose by the same amount every minute. Which conclusion is best?

- ◻️ All liquids heat up at the same rate as water.  
  _↳ feedback if chosen: Only water was tested: the data cannot say that._
- ◻️ Heating water is dangerous.  
  _↳ feedback if chosen: That does not answer the question from the data._
- ✅ The temperature of the water rose at a steady rate while it was heated.

Full working after a second miss:

> The true statement is “The temperature of the water rose at a steady rate while it was heated.”.  
> “All liquids heat up at the same rate as water.” is false: Only water was tested: the data cannot say that.  
> “Heating water is dangerous.” is false: That does not answer the question from the data.  

> A pupil heated water and recorded that its temperature rose by the same amount every minute. Which conclusion is best?

- ◻️ The temperature went down while heating.  
  _↳ feedback if chosen: The data show it went up._
- ✅ As the heating time increases, the temperature of the water increases steadily.
- ◻️ Heating water is dangerous.  
  _↳ feedback if chosen: That does not answer the question from the data._

Full working after a second miss:

> The true statement is “As the heating time increases, the temperature of the water increases steadily.”.  
> “The temperature went down while heating.” is false: The data show it went up.  
> “Heating water is dangerous.” is false: That does not answer the question from the data.  

> A pupil heated water and recorded that its temperature rose by the same amount every minute. Which conclusion is best?

- ✅ The temperature of the water rose at a steady rate while it was heated.
- ◻️ Water boils at every temperature.  
  _↳ feedback if chosen: The data do not show that._
- ◻️ Heating water is dangerous.  
  _↳ feedback if chosen: That does not answer the question from the data._

Full working after a second miss:

> The true statement is “The temperature of the water rose at a steady rate while it was heated.”.  
> “Water boils at every temperature.” is false: The data do not show that.  
> “Heating water is dangerous.” is false: That does not answer the question from the data.  

Sources: scientific-method (The scientific method as taught in Cameroonian secondary physics: data, tables, graphs, fair tests, evaluation)

### `p2-3-var` · Lesson 3 · matching, level 1

Prompt: In an experiment on how the height of a ramp affects the time a ball takes to roll down it, sort the variables.

Pairs (4 shown each time, sorted into groups):

- the height of the ramp → **changed (independent)**
- the time taken → **measured (dependent)**
- the same ball each time → **kept the same (controlled)**
- the same length of ramp → **kept the same (controlled)**
- the same surface on the ramp → **kept the same (controlled)**


Three generated variants:

> In an experiment on how the height of a ramp affects the time a ball takes to roll down it, sort the variables.

Groups: changed (independent) · measured (dependent) · kept the same (controlled)
- the time taken → **measured (dependent)**
- the same ball each time → **kept the same (controlled)**
- the same length of ramp → **kept the same (controlled)**
- the height of the ramp → **changed (independent)**

Full working after a second miss:

> The right pairs are:  
> the time taken → measured (dependent)  
> the same ball each time → kept the same (controlled)  
> the same length of ramp → kept the same (controlled)  
> the height of the ramp → changed (independent)  

> In an experiment on how the height of a ramp affects the time a ball takes to roll down it, sort the variables.

Groups: changed (independent) · measured (dependent) · kept the same (controlled)
- the same surface on the ramp → **kept the same (controlled)**
- the height of the ramp → **changed (independent)**
- the same length of ramp → **kept the same (controlled)**
- the time taken → **measured (dependent)**

Full working after a second miss:

> The right pairs are:  
> the same surface on the ramp → kept the same (controlled)  
> the height of the ramp → changed (independent)  
> the same length of ramp → kept the same (controlled)  
> the time taken → measured (dependent)  

> In an experiment on how the height of a ramp affects the time a ball takes to roll down it, sort the variables.

Groups: changed (independent) · kept the same (controlled)
- the same surface on the ramp → **kept the same (controlled)**
- the same ball each time → **kept the same (controlled)**
- the same length of ramp → **kept the same (controlled)**
- the height of the ramp → **changed (independent)**

Full working after a second miss:

> The right pairs are:  
> the same surface on the ramp → kept the same (controlled)  
> the same ball each time → kept the same (controlled)  
> the same length of ramp → kept the same (controlled)  
> the height of the ramp → changed (independent)  

Sources: scientific-method (The scientific method as taught in Cameroonian secondary physics: data, tables, graphs, fair tests, evaluation)

### `p2-3-improve` · Lesson 3 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Ayuk times one swing of a pendulum with a stopwatch. What is the best way to improve his result? | Time 10 swings and divide by 10. | Time it once very fast. · Guess the time. · Use a ruler. | One quick reading has a large reaction-time error. · Guessing is not measuring. · A ruler measures length, not time. | Timing many swings makes the reaction-time error small compared with the total. |
| Bih's three readings are very different from each other. What should she do? | Repeat the measurement and check for mistakes. | Keep only the biggest. · Make up a new reading. · Stop the experiment. | Choosing the biggest is not fair. · Never make up data. · Find out why first. | Readings that disagree must be checked and repeated. |
| A pupil reads a measuring cylinder from above. What error can this cause? | a parallax error | a zero error · a reaction-time error · no error | A zero error is when an instrument does not start at zero. · Reaction time is about timing. · Reading at an angle gives a wrong value. | Reading at an angle gives a parallax error: read at eye level. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A pupil reads a measuring cylinder from above. What error can this cause?

- ◻️ a reaction-time error  
  _↳ feedback if chosen: Reaction time is about timing._
- ✅ a parallax error
- ◻️ no error  
  _↳ feedback if chosen: Reading at an angle gives a wrong value._
- ◻️ a zero error  
  _↳ feedback if chosen: A zero error is when an instrument does not start at zero._

Full working after a second miss:

> Reading at an angle gives a parallax error: read at eye level.  
> So the answer is “a parallax error”.  

> A pupil reads a measuring cylinder from above. What error can this cause?

- ✅ a parallax error
- ◻️ no error  
  _↳ feedback if chosen: Reading at an angle gives a wrong value._
- ◻️ a reaction-time error  
  _↳ feedback if chosen: Reaction time is about timing._
- ◻️ a zero error  
  _↳ feedback if chosen: A zero error is when an instrument does not start at zero._

Full working after a second miss:

> Reading at an angle gives a parallax error: read at eye level.  
> So the answer is “a parallax error”.  

> Ayuk times one swing of a pendulum with a stopwatch. What is the best way to improve his result?

- ◻️ Time it once very fast.  
  _↳ feedback if chosen: One quick reading has a large reaction-time error._
- ◻️ Guess the time.  
  _↳ feedback if chosen: Guessing is not measuring._
- ✅ Time 10 swings and divide by 10.
- ◻️ Use a ruler.  
  _↳ feedback if chosen: A ruler measures length, not time._

Full working after a second miss:

> Timing many swings makes the reaction-time error small compared with the total.  
> So the answer is “Time 10 swings and divide by 10.”.  

Sources: scientific-method (The scientific method as taught in Cameroonian secondary physics: data, tables, graphs, fair tests, evaluation)

### `p2-3-spot` · Lesson 3 · spot the error, level 3

Prompt: Which statement about a fair test is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Change only one variable at a time.
- ✅ Keep the controlled variables the same.
- ✅ Repeat readings and take the mean.
- ✅ Measure the dependent variable.
- ❌ Change two variables at once to save time.  
  _↳ Then you cannot tell which change caused the result._
- ❌ Use a different ball for each height of the ramp.  
  _↳ The ball must stay the same: it is a controlled variable._
- ❌ Leave out readings you do not like.  
  _↳ Only anomalous readings, after checking, may be left out._


Three generated variants:

> Which statement about a fair test is wrong?

- ✅ Use a different ball for each height of the ramp.  
  _↳ explanation: The ball must stay the same: it is a controlled variable._
- ◻️ Change only one variable at a time.
- ◻️ Keep the controlled variables the same.
- ◻️ Measure the dependent variable.

Full working after a second miss:

> The wrong statement is “Use a different ball for each height of the ramp.”.  
> The ball must stay the same: it is a controlled variable.  

> Which statement about a fair test is wrong?

- ◻️ Change only one variable at a time.
- ◻️ Repeat readings and take the mean.
- ✅ Use a different ball for each height of the ramp.  
  _↳ explanation: The ball must stay the same: it is a controlled variable._
- ◻️ Keep the controlled variables the same.

Full working after a second miss:

> The wrong statement is “Use a different ball for each height of the ramp.”.  
> The ball must stay the same: it is a controlled variable.  

> Which statement about a fair test is wrong?

- ◻️ Keep the controlled variables the same.
- ◻️ Measure the dependent variable.
- ◻️ Repeat readings and take the mean.
- ✅ Change two variables at once to save time.  
  _↳ explanation: Then you cannot tell which change caused the result._

Full working after a second miss:

> The wrong statement is “Change two variables at once to save time.”.  
> Then you cannot tell which change caused the result.  

Sources: scientific-method (The scientific method as taught in Cameroonian secondary physics: data, tables, graphs, fair tests, evaluation)

### `p2-4-unit` · Lesson 4 · matching, level 1

Prompt: Match each base quantity to its SI unit.

Pairs (4 shown each time):

- length → **metre (m)**
- mass → **kilogram (kg)**
- time → **second (s)**
- temperature → **kelvin (K)**
- electric current → **ampere (A)**


Three generated variants:

> Match each base quantity to its SI unit.

Right-hand side (shuffled): kelvin (K) · ampere (A) · kilogram (kg) · second (s)
- temperature → **kelvin (K)**
- mass → **kilogram (kg)**
- time → **second (s)**
- electric current → **ampere (A)**

Full working after a second miss:

> The right pairs are:  
> temperature → kelvin (K)  
> mass → kilogram (kg)  
> time → second (s)  
> electric current → ampere (A)  

> Match each base quantity to its SI unit.

Right-hand side (shuffled): kelvin (K) · ampere (A) · metre (m) · second (s)
- temperature → **kelvin (K)**
- length → **metre (m)**
- time → **second (s)**
- electric current → **ampere (A)**

Full working after a second miss:

> The right pairs are:  
> temperature → kelvin (K)  
> length → metre (m)  
> time → second (s)  
> electric current → ampere (A)  

> Match each base quantity to its SI unit.

Right-hand side (shuffled): kilogram (kg) · second (s) · kelvin (K) · metre (m)
- length → **metre (m)**
- mass → **kilogram (kg)**
- time → **second (s)**
- temperature → **kelvin (K)**

Full working after a second miss:

> The right pairs are:  
> length → metre (m)  
> mass → kilogram (kg)  
> time → second (s)  
> temperature → kelvin (K)  

Sources: measurement (SI base quantities and units (BIPM, The International System of Units); density = mass / volume; volume by displacement)

### `p2-4-tool` · Lesson 4 · matching, level 1

Prompt: Match each quantity to the instrument that measures it.

Pairs (4 shown each time):

- mass → **a balance**
- time → **a stopwatch**
- electric current → **an ammeter**
- temperature → **a thermometer**
- length → **a metre rule**
- volume of a liquid → **a measuring cylinder**


Three generated variants:

> Match each quantity to the instrument that measures it.

Right-hand side (shuffled): a thermometer · a balance · an ammeter · a metre rule
- electric current → **an ammeter**
- length → **a metre rule**
- temperature → **a thermometer**
- mass → **a balance**

Full working after a second miss:

> The right pairs are:  
> electric current → an ammeter  
> length → a metre rule  
> temperature → a thermometer  
> mass → a balance  

> Match each quantity to the instrument that measures it.

Right-hand side (shuffled): a balance · a stopwatch · an ammeter · a metre rule
- length → **a metre rule**
- mass → **a balance**
- electric current → **an ammeter**
- time → **a stopwatch**

Full working after a second miss:

> The right pairs are:  
> length → a metre rule  
> mass → a balance  
> electric current → an ammeter  
> time → a stopwatch  

> Match each quantity to the instrument that measures it.

Right-hand side (shuffled): a balance · a stopwatch · a metre rule · a measuring cylinder
- mass → **a balance**
- time → **a stopwatch**
- volume of a liquid → **a measuring cylinder**
- length → **a metre rule**

Full working after a second miss:

> The right pairs are:  
> mass → a balance  
> time → a stopwatch  
> volume of a liquid → a measuring cylinder  
> length → a metre rule  

Sources: measurement (SI base quantities and units (BIPM, The International System of Units); density = mass / volume; volume by displacement)

### `p2-4-which` · Lesson 4 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which of these is NOT a base quantity? | speed | length · mass · time | Length is a base quantity (metre). · Mass is a base quantity (kilogram). · Time is a base quantity (second). | Speed is derived: distance ÷ time. |
| Which unit is a derived unit? | m/s | kg · s · A | The kilogram is a base unit. · The second is a base unit. · The ampere is a base unit. | m/s comes from metres and seconds: it is derived. |
| What is the SI unit of mass? | the kilogram | the gram · the newton · the litre | The gram is smaller; the SI base unit is the kilogram. · The newton measures force. · The litre measures volume. | The SI unit of mass is the kilogram. |
| Which instrument measures electric current? | an ammeter | a thermometer · a balance · a stopwatch | A thermometer measures temperature. · A balance measures mass. · A stopwatch measures time. | An ammeter measures current in amperes. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which instrument measures electric current?

- ◻️ a balance  
  _↳ feedback if chosen: A balance measures mass._
- ✅ an ammeter
- ◻️ a thermometer  
  _↳ feedback if chosen: A thermometer measures temperature._
- ◻️ a stopwatch  
  _↳ feedback if chosen: A stopwatch measures time._

Full working after a second miss:

> An ammeter measures current in amperes.  
> So the answer is “an ammeter”.  

> Which of these is NOT a base quantity?

- ◻️ length  
  _↳ feedback if chosen: Length is a base quantity (metre)._
- ✅ speed
- ◻️ time  
  _↳ feedback if chosen: Time is a base quantity (second)._
- ◻️ mass  
  _↳ feedback if chosen: Mass is a base quantity (kilogram)._

Full working after a second miss:

> Speed is derived: distance ÷ time.  
> So the answer is “speed”.  

> Which instrument measures electric current?

- ◻️ a balance  
  _↳ feedback if chosen: A balance measures mass._
- ◻️ a stopwatch  
  _↳ feedback if chosen: A stopwatch measures time._
- ◻️ a thermometer  
  _↳ feedback if chosen: A thermometer measures temperature._
- ✅ an ammeter

Full working after a second miss:

> An ammeter measures current in amperes.  
> So the answer is “an ammeter”.  

Sources: measurement (SI base quantities and units (BIPM, The International System of Units); density = mass / volume; volume by displacement)

### `p2-5-measure` · Lesson 5 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which two instruments do you need to measure the speed of a runner? | a tape measure and a stopwatch | a balance and a thermometer · a ruler and a balance · an ammeter and a clock | Those measure mass and temperature. · A balance measures mass. · An ammeter measures current. | Speed needs a distance and a time. |
| What does a speedometer show? | the speed at each moment | the average speed of the whole trip · the distance only · the time only | Distance ÷ total time gives the average speed. · That is an odometer. · That is a clock. | A speedometer shows the speed at that moment. |
| What is the SI unit of speed? | metre per second (m/s) | kilometre (km) · second (s) · kilogram (kg) | That is a unit of length. · That is a unit of time. · That is a unit of mass. | Speed is distance per time: m/s. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which two instruments do you need to measure the speed of a runner?

- ✅ a tape measure and a stopwatch
- ◻️ a balance and a thermometer  
  _↳ feedback if chosen: Those measure mass and temperature._
- ◻️ an ammeter and a clock  
  _↳ feedback if chosen: An ammeter measures current._
- ◻️ a ruler and a balance  
  _↳ feedback if chosen: A balance measures mass._

Full working after a second miss:

> Speed needs a distance and a time.  
> So the answer is “a tape measure and a stopwatch”.  

> What is the SI unit of speed?

- ◻️ kilogram (kg)  
  _↳ feedback if chosen: That is a unit of mass._
- ✅ metre per second (m/s)
- ◻️ second (s)  
  _↳ feedback if chosen: That is a unit of time._
- ◻️ kilometre (km)  
  _↳ feedback if chosen: That is a unit of length._

Full working after a second miss:

> Speed is distance per time: m/s.  
> So the answer is “metre per second (m/s)”.  

> What does a speedometer show?

- ✅ the speed at each moment
- ◻️ the distance only  
  _↳ feedback if chosen: That is an odometer._
- ◻️ the time only  
  _↳ feedback if chosen: That is a clock._
- ◻️ the average speed of the whole trip  
  _↳ feedback if chosen: Distance ÷ total time gives the average speed._

Full working after a second miss:

> A speedometer shows the speed at that moment.  
> So the answer is “the speed at each moment”.  

Sources: speed (Speed = distance / time; average speed; 1 km/h = 1/3.6 m/s)

### `p2-7-float` · Lesson 7 · multiple choice, level 1

Prompt: {X[0]} has a density of {X[1]} g/cm³. In water it …

Table `X` (one row is picked each time):

| 0 | 1 |
|---|---|
| Cork | 0.25 |
| Dry wood | 0.6 |
| Ice | 0.92 |
| Palm oil | 0.91 |
| Iron | 7.9 |
| Aluminium | 2.7 |
| Glass | 2.5 |
| Copper | 8.9 |
| Stone | 2.6 |

Right answer: `{X[1] < 1 ? 'floats' : 'sinks'}`; wrong choices: `{X[1] < 1 ? 'sinks' : 'floats'}`

- Feedback `flip`: “Compare with water, {one} g/cm³: less dense floats, denser sinks.”

Three generated variants:

> Stone has a density of 2.6 g/cm³. In water it …

- ✅ sinks
- ◻️ floats  
  _↳ feedback if chosen: Compare with water, 1 g/cm³: less dense floats, denser sinks._

Full working after a second miss:

> Water has a density of 1 g/cm³.  
> 2.6 is more than 1, so it sinks.  

> Cork has a density of 0.25 g/cm³. In water it …

- ◻️ sinks  
  _↳ feedback if chosen: Compare with water, 1 g/cm³: less dense floats, denser sinks._
- ✅ floats

Full working after a second miss:

> Water has a density of 1 g/cm³.  
> 0.25 is less than 1, so it floats.  

> Iron has a density of 7.9 g/cm³. In water it …

- ◻️ floats  
  _↳ feedback if chosen: Compare with water, 1 g/cm³: less dense floats, denser sinks._
- ✅ sinks

Full working after a second miss:

> Water has a density of 1 g/cm³.  
> 7.9 is more than 1, so it sinks.  

Sources: measurement (SI base quantities and units (BIPM, The International System of Units); density = mass / volume; volume by displacement)

### `p2-8-sort` · Lesson 8 · matching, level 1

Prompt: Sort each substance by its state at room temperature.

Pairs (6 shown each time, sorted into groups):

- stone → **solid**
- salt → **solid**
- iron nail → **solid**
- ice cube → **solid**
- palm oil → **liquid**
- kerosene → **liquid**
- milk → **liquid**
- petrol → **liquid**
- air → **gas**
- oxygen → **gas**
- steam → **gas**
- cooking gas → **gas**


Three generated variants:

> Sort each substance by its state at room temperature.

Groups: solid · liquid · gas
- steam → **gas**
- petrol → **liquid**
- palm oil → **liquid**
- salt → **solid**
- iron nail → **solid**
- ice cube → **solid**

Full working after a second miss:

> The right pairs are:  
> steam → gas  
> petrol → liquid  
> palm oil → liquid  
> salt → solid  
> iron nail → solid  
> ice cube → solid  

> Sort each substance by its state at room temperature.

Groups: solid · liquid · gas
- steam → **gas**
- kerosene → **liquid**
- oxygen → **gas**
- stone → **solid**
- ice cube → **solid**
- petrol → **liquid**

Full working after a second miss:

> The right pairs are:  
> steam → gas  
> kerosene → liquid  
> oxygen → gas  
> stone → solid  
> ice cube → solid  
> petrol → liquid  

> Sort each substance by its state at room temperature.

Groups: solid · liquid · gas
- oxygen → **gas**
- ice cube → **solid**
- milk → **liquid**
- cooking gas → **gas**
- air → **gas**
- salt → **solid**

Full working after a second miss:

> The right pairs are:  
> oxygen → gas  
> ice cube → solid  
> milk → liquid  
> cooking gas → gas  
> air → gas  
> salt → solid  

Sources: matter (The particle model of matter and the changes of state (as in Form One, TR-P07))

### `p2-8-same` · Lesson 8 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is water in the solid state called? | ice | steam · vapour · rain | Steam is water as a gas. · Vapour is water as a gas. · Rain is liquid water. | Solid water is ice. |
| What is water in the gas state called? | steam (water vapour) | ice · dew · frost | Ice is solid. · Dew is liquid water. · Frost is solid ice. | Water as a gas is steam or water vapour. |
| Candle wax that melts becomes … | a liquid | a gas · a harder solid · nothing | Melting gives a liquid. · Melting makes it liquid. · The wax is still there. | Melting changes a solid into a liquid. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is water in the solid state called?

- ◻️ vapour  
  _↳ feedback if chosen: Vapour is water as a gas._
- ◻️ steam  
  _↳ feedback if chosen: Steam is water as a gas._
- ✅ ice
- ◻️ rain  
  _↳ feedback if chosen: Rain is liquid water._

Full working after a second miss:

> Solid water is ice.  
> So the answer is “ice”.  

> What is water in the gas state called?

- ✅ steam (water vapour)
- ◻️ frost  
  _↳ feedback if chosen: Frost is solid ice._
- ◻️ dew  
  _↳ feedback if chosen: Dew is liquid water._
- ◻️ ice  
  _↳ feedback if chosen: Ice is solid._

Full working after a second miss:

> Water as a gas is steam or water vapour.  
> So the answer is “steam (water vapour)”.  

> What is water in the gas state called?

- ◻️ ice  
  _↳ feedback if chosen: Ice is solid._
- ◻️ dew  
  _↳ feedback if chosen: Dew is liquid water._
- ◻️ frost  
  _↳ feedback if chosen: Frost is solid ice._
- ✅ steam (water vapour)

Full working after a second miss:

> Water as a gas is steam or water vapour.  
> So the answer is “steam (water vapour)”.  

Sources: matter (The particle model of matter and the changes of state (as in Form One, TR-P07))

### `p2-8-life` · Lesson 8 · multiple choice, level 2

Prompt: {X.q} Which change of state is this?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Wet clothes dry on a line. | evaporation | condensation · melting · freezing | Condensation turns gas into liquid. · Melting turns solid into liquid. · Freezing turns liquid into solid. | The water in the clothes becomes vapour. |
| Drops form on the outside of a cold bottle of water. | condensation | evaporation · melting · sublimation | Evaporation turns liquid into gas. · Nothing solid melts here. · Sublimation turns solid into gas. | Water vapour in the air cools and becomes liquid. |
| Shea butter becomes runny in the hot sun. | melting | freezing · condensation · boiling | Freezing is liquid → solid. · Condensation is gas → liquid. · Boiling is liquid → gas. | A solid becomes liquid: melting. |
| Naphthalene balls in a wardrobe get smaller without becoming liquid. | sublimation | melting · evaporation · freezing | Melting would make a liquid. · Evaporation starts from a liquid. · Freezing makes a solid. | Solid → gas directly is sublimation. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Naphthalene balls in a wardrobe get smaller without becoming liquid. Which change of state is this?

- ◻️ freezing  
  _↳ feedback if chosen: Freezing makes a solid._
- ◻️ melting  
  _↳ feedback if chosen: Melting would make a liquid._
- ✅ sublimation
- ◻️ evaporation  
  _↳ feedback if chosen: Evaporation starts from a liquid._

Full working after a second miss:

> Solid → gas directly is sublimation.  
> So the answer is “sublimation”.  

> Naphthalene balls in a wardrobe get smaller without becoming liquid. Which change of state is this?

- ◻️ freezing  
  _↳ feedback if chosen: Freezing makes a solid._
- ◻️ melting  
  _↳ feedback if chosen: Melting would make a liquid._
- ✅ sublimation
- ◻️ evaporation  
  _↳ feedback if chosen: Evaporation starts from a liquid._

Full working after a second miss:

> Solid → gas directly is sublimation.  
> So the answer is “sublimation”.  

> Shea butter becomes runny in the hot sun. Which change of state is this?

- ◻️ freezing  
  _↳ feedback if chosen: Freezing is liquid → solid._
- ◻️ condensation  
  _↳ feedback if chosen: Condensation is gas → liquid._
- ◻️ boiling  
  _↳ feedback if chosen: Boiling is liquid → gas._
- ✅ melting

Full working after a second miss:

> A solid becomes liquid: melting.  
> So the answer is “melting”.  

Sources: matter (The particle model of matter and the changes of state (as in Form One, TR-P07))

### `p2-8-spot` · Lesson 8 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Matter has mass and takes up space.
- ✅ Ice, water and steam are the same substance.
- ✅ Air is a gas.
- ✅ Melting changes a solid into a liquid.
- ❌ Steam is water in the solid state.  
  _↳ Steam is water as a gas; ice is the solid._
- ❌ Condensation changes a liquid into a gas.  
  _↳ Condensation changes a gas into a liquid._
- ❌ Air has no mass.  
  _↳ Air is matter: it has mass._


Three generated variants:

> Which statement is wrong?

- ◻️ Melting changes a solid into a liquid.
- ✅ Steam is water in the solid state.  
  _↳ explanation: Steam is water as a gas; ice is the solid._
- ◻️ Matter has mass and takes up space.
- ◻️ Ice, water and steam are the same substance.

Full working after a second miss:

> The wrong statement is “Steam is water in the solid state.”.  
> Steam is water as a gas; ice is the solid.  

> Which statement is wrong?

- ◻️ Air is a gas.
- ◻️ Melting changes a solid into a liquid.
- ✅ Steam is water in the solid state.  
  _↳ explanation: Steam is water as a gas; ice is the solid._
- ◻️ Ice, water and steam are the same substance.

Full working after a second miss:

> The wrong statement is “Steam is water in the solid state.”.  
> Steam is water as a gas; ice is the solid.  

> Which statement is wrong?

- ◻️ Air is a gas.
- ✅ Steam is water in the solid state.  
  _↳ explanation: Steam is water as a gas; ice is the solid._
- ◻️ Melting changes a solid into a liquid.
- ◻️ Matter has mass and takes up space.

Full working after a second miss:

> The wrong statement is “Steam is water in the solid state.”.  
> Steam is water as a gas; ice is the solid.  

Sources: matter (The particle model of matter and the changes of state (as in Form One, TR-P07))

### `p2-9-props` · Lesson 9 · matching, level 1

Prompt: Match each description to the state of matter.

Pairs (3 shown each time):

- fixed shape and fixed volume → **solid**
- fixed volume, takes the shape of its container → **liquid**
- no fixed shape and no fixed volume → **gas**
- particles only vibrate in fixed places → **solid**
- particles slide past one another → **liquid**
- particles far apart, moving fast → **gas**


Three generated variants:

> Match each description to the state of matter.

Right-hand side (shuffled): gas · solid · liquid
- fixed volume, takes the shape of its container → **liquid**
- fixed shape and fixed volume → **solid**
- particles far apart, moving fast → **gas**

Full working after a second miss:

> The right pairs are:  
> fixed volume, takes the shape of its container → liquid  
> fixed shape and fixed volume → solid  
> particles far apart, moving fast → gas  

> Match each description to the state of matter.

Right-hand side (shuffled): liquid · gas · solid
- no fixed shape and no fixed volume → **gas**
- fixed shape and fixed volume → **solid**
- fixed volume, takes the shape of its container → **liquid**

Full working after a second miss:

> The right pairs are:  
> no fixed shape and no fixed volume → gas  
> fixed shape and fixed volume → solid  
> fixed volume, takes the shape of its container → liquid  

> Match each description to the state of matter.

Right-hand side (shuffled): gas · solid · liquid
- particles slide past one another → **liquid**
- particles only vibrate in fixed places → **solid**
- no fixed shape and no fixed volume → **gas**

Full working after a second miss:

> The right pairs are:  
> particles slide past one another → liquid  
> particles only vibrate in fixed places → solid  
> no fixed shape and no fixed volume → gas  

Sources: matter (The particle model of matter and the changes of state (as in Form One, TR-P07))

### `p2-9-particles` · Lesson 9 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In which state are the particles furthest apart? | gas | solid · liquid · all the same | Solid particles are packed close. · Liquid particles are close. · They differ. | Gas particles are far apart. |
| In which state do the particles only vibrate? | solid | liquid · gas · none | Liquid particles slide. · Gas particles move fast everywhere. · Solid particles vibrate. | Solid particles vibrate in fixed places. |
| Why does a liquid flow? | Its particles can slide past one another. | Its particles are far apart. · It has no mass. · Its particles do not move. | That describes a gas. · Liquids have mass. · They move. | Sliding particles let a liquid flow. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does a liquid flow?

- ◻️ Its particles do not move.  
  _↳ feedback if chosen: They move._
- ✅ Its particles can slide past one another.
- ◻️ It has no mass.  
  _↳ feedback if chosen: Liquids have mass._
- ◻️ Its particles are far apart.  
  _↳ feedback if chosen: That describes a gas._

Full working after a second miss:

> Sliding particles let a liquid flow.  
> So the answer is “Its particles can slide past one another.”.  

> In which state do the particles only vibrate?

- ◻️ liquid  
  _↳ feedback if chosen: Liquid particles slide._
- ◻️ none  
  _↳ feedback if chosen: Solid particles vibrate._
- ◻️ gas  
  _↳ feedback if chosen: Gas particles move fast everywhere._
- ✅ solid

Full working after a second miss:

> Solid particles vibrate in fixed places.  
> So the answer is “solid”.  

> In which state do the particles only vibrate?

- ◻️ gas  
  _↳ feedback if chosen: Gas particles move fast everywhere._
- ◻️ liquid  
  _↳ feedback if chosen: Liquid particles slide._
- ◻️ none  
  _↳ feedback if chosen: Solid particles vibrate._
- ✅ solid

Full working after a second miss:

> Solid particles vibrate in fixed places.  
> So the answer is “solid”.  

Sources: matter (The particle model of matter and the changes of state (as in Form One, TR-P07))

### `p2-9-compress` · Lesson 9 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is it easy to pump air into a tyre? | Gas particles have spaces between them. | Air has no particles. · Air is a liquid. · Tyres pull air in. | Air is made of particles. · Air is a gas. · The pump pushes the air. | There is space between gas particles, so gas compresses. |
| The smell of fried plantains reaches the whole house. What does this show? | Gas particles move and spread out (diffusion). | Smells are solids. · Liquids flow. · Particles do not move. | Smells are gases. · This is about a gas. · It shows they do move. | Spreading of a gas is diffusion. |
| Why does a stone keep its shape? | Its particles are held in fixed places. | It is very heavy. · It is cold. · Its particles are far apart. | Weight does not fix shape. · Temperature is not the reason. · That describes a gas. | In a solid the particles stay in a fixed pattern. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does a stone keep its shape?

- ✅ Its particles are held in fixed places.
- ◻️ It is cold.  
  _↳ feedback if chosen: Temperature is not the reason._
- ◻️ Its particles are far apart.  
  _↳ feedback if chosen: That describes a gas._
- ◻️ It is very heavy.  
  _↳ feedback if chosen: Weight does not fix shape._

Full working after a second miss:

> In a solid the particles stay in a fixed pattern.  
> So the answer is “Its particles are held in fixed places.”.  

> Why is it easy to pump air into a tyre?

- ◻️ Air has no particles.  
  _↳ feedback if chosen: Air is made of particles._
- ✅ Gas particles have spaces between them.
- ◻️ Tyres pull air in.  
  _↳ feedback if chosen: The pump pushes the air._
- ◻️ Air is a liquid.  
  _↳ feedback if chosen: Air is a gas._

Full working after a second miss:

> There is space between gas particles, so gas compresses.  
> So the answer is “Gas particles have spaces between them.”.  

> Why is it easy to pump air into a tyre?

- ◻️ Air is a liquid.  
  _↳ feedback if chosen: Air is a gas._
- ◻️ Air has no particles.  
  _↳ feedback if chosen: Air is made of particles._
- ✅ Gas particles have spaces between them.
- ◻️ Tyres pull air in.  
  _↳ feedback if chosen: The pump pushes the air._

Full working after a second miss:

> There is space between gas particles, so gas compresses.  
> So the answer is “Gas particles have spaces between them.”.  

Sources: matter (The particle model of matter and the changes of state (as in Form One, TR-P07))

### `p2-9-spot` · Lesson 9 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A liquid takes the shape of its container.
- ✅ A gas fills its container.
- ✅ Solid particles vibrate.
- ✅ A gas is easy to compress.
- ❌ A liquid has no fixed volume.  
  _↳ A liquid has a fixed volume; only its shape changes._
- ❌ Solid particles move freely in all directions.  
  _↳ That describes a gas; solid particles only vibrate._
- ❌ A solid is easy to compress.  
  _↳ A solid cannot be compressed: its particles touch._


Three generated variants:

> Which statement is wrong?

- ◻️ A liquid takes the shape of its container.
- ✅ A liquid has no fixed volume.  
  _↳ explanation: A liquid has a fixed volume; only its shape changes._
- ◻️ A gas is easy to compress.
- ◻️ Solid particles vibrate.

Full working after a second miss:

> The wrong statement is “A liquid has no fixed volume.”.  
> A liquid has a fixed volume; only its shape changes.  

> Which statement is wrong?

- ◻️ A gas is easy to compress.
- ✅ A liquid has no fixed volume.  
  _↳ explanation: A liquid has a fixed volume; only its shape changes._
- ◻️ Solid particles vibrate.
- ◻️ A gas fills its container.

Full working after a second miss:

> The wrong statement is “A liquid has no fixed volume.”.  
> A liquid has a fixed volume; only its shape changes.  

> Which statement is wrong?

- ◻️ A gas fills its container.
- ◻️ A liquid takes the shape of its container.
- ◻️ A gas is easy to compress.
- ✅ A solid is easy to compress.  
  _↳ explanation: A solid cannot be compressed: its particles touch._

Full working after a second miss:

> The wrong statement is “A solid is easy to compress.”.  
> A solid cannot be compressed: its particles touch.  

Sources: matter (The particle model of matter and the changes of state (as in Form One, TR-P07))

### `p2-9-compress-card` · Lesson 9 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is it easy to pump air into a tyre? | Gas particles have spaces between them. | Air has no particles. · Air is a liquid. · Tyres pull air in. | Air is made of particles. · Air is a gas. · The pump pushes the air. | There is space between gas particles, so gas compresses. |
| The smell of fried plantains reaches the whole house. What does this show? | Gas particles move and spread out (diffusion). | Smells are solids. · Liquids flow. · Particles do not move. | Smells are gases. · This is about a gas. · It shows they do move. | Spreading of a gas is diffusion. |
| Why does a stone keep its shape? | Its particles are held in fixed places. | It is very heavy. · It is cold. · Its particles are far apart. | Weight does not fix shape. · Temperature is not the reason. · That describes a gas. | In a solid the particles stay in a fixed pattern. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does a stone keep its shape?

- ◻️ It is cold.  
  _↳ feedback if chosen: Temperature is not the reason._
- ◻️ Its particles are far apart.  
  _↳ feedback if chosen: That describes a gas._
- ◻️ It is very heavy.  
  _↳ feedback if chosen: Weight does not fix shape._
- ✅ Its particles are held in fixed places.

Full working after a second miss:

> In a solid the particles stay in a fixed pattern.  
> So the answer is “Its particles are held in fixed places.”.  

> The smell of fried plantains reaches the whole house. What does this show?

- ◻️ Particles do not move.  
  _↳ feedback if chosen: It shows they do move._
- ✅ Gas particles move and spread out (diffusion).
- ◻️ Liquids flow.  
  _↳ feedback if chosen: This is about a gas._
- ◻️ Smells are solids.  
  _↳ feedback if chosen: Smells are gases._

Full working after a second miss:

> Spreading of a gas is diffusion.  
> So the answer is “Gas particles move and spread out (diffusion).”.  

> The smell of fried plantains reaches the whole house. What does this show?

- ◻️ Liquids flow.  
  _↳ feedback if chosen: This is about a gas._
- ◻️ Smells are solids.  
  _↳ feedback if chosen: Smells are gases._
- ◻️ Particles do not move.  
  _↳ feedback if chosen: It shows they do move._
- ✅ Gas particles move and spread out (diffusion).

Full working after a second miss:

> Spreading of a gas is diffusion.  
> So the answer is “Gas particles move and spread out (diffusion).”.  

Sources: matter (The particle model of matter and the changes of state (as in Form One, TR-P07))

### `p2-10-effect` · Lesson 10 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do railway lines have small gaps between the rails? | Heat makes the rails expand. | To save metal. · To let water drain. · So trains are quieter. | It is not about saving metal. · The gaps are for expansion. · Gaps actually make noise. | In the heat the rails expand into the gaps instead of bending. |
| Why does the liquid in a thermometer rise when it is warmed? | The liquid expands. | The glass shrinks. · The liquid boils. · Air pushes it up. | The glass hardly changes. · It does not boil. · It rises because it expands. | Warmed liquid expands and moves up the tube. |
| What is the normal temperature of the human body? | about 37 °C | about 100 °C · about 0 °C · about 20 °C | That is boiling water. · That is freezing water. · That is a cool room. | Normal body temperature is about 37 °C. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does the liquid in a thermometer rise when it is warmed?

- ◻️ The glass shrinks.  
  _↳ feedback if chosen: The glass hardly changes._
- ◻️ The liquid boils.  
  _↳ feedback if chosen: It does not boil._
- ✅ The liquid expands.
- ◻️ Air pushes it up.  
  _↳ feedback if chosen: It rises because it expands._

Full working after a second miss:

> Warmed liquid expands and moves up the tube.  
> So the answer is “The liquid expands.”.  

> Why do railway lines have small gaps between the rails?

- ◻️ So trains are quieter.  
  _↳ feedback if chosen: Gaps actually make noise._
- ◻️ To let water drain.  
  _↳ feedback if chosen: The gaps are for expansion._
- ◻️ To save metal.  
  _↳ feedback if chosen: It is not about saving metal._
- ✅ Heat makes the rails expand.

Full working after a second miss:

> In the heat the rails expand into the gaps instead of bending.  
> So the answer is “Heat makes the rails expand.”.  

> Why do railway lines have small gaps between the rails?

- ◻️ So trains are quieter.  
  _↳ feedback if chosen: Gaps actually make noise._
- ◻️ To let water drain.  
  _↳ feedback if chosen: The gaps are for expansion._
- ✅ Heat makes the rails expand.
- ◻️ To save metal.  
  _↳ feedback if chosen: It is not about saving metal._

Full working after a second miss:

> In the heat the rails expand into the gaps instead of bending.  
> So the answer is “Heat makes the rails expand.”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-11-sort` · Lesson 11 · matching, level 1

Prompt: Sort the materials: conductor or insulator?

Pairs (6 shown each time, sorted into groups):

- copper → **conductor**
- aluminium → **conductor**
- iron → **conductor**
- silver → **conductor**
- steel spoon → **conductor**
- plastic → **insulator**
- wood → **insulator**
- rubber → **insulator**
- glass → **insulator**
- dry cloth → **insulator**
- air → **insulator**


Three generated variants:

> Sort the materials: conductor or insulator?

Groups: conductor · insulator
- iron → **conductor**
- steel spoon → **conductor**
- air → **insulator**
- glass → **insulator**
- rubber → **insulator**
- copper → **conductor**

Full working after a second miss:

> The right pairs are:  
> iron → conductor  
> steel spoon → conductor  
> air → insulator  
> glass → insulator  
> rubber → insulator  
> copper → conductor  

> Sort the materials: conductor or insulator?

Groups: conductor · insulator
- rubber → **insulator**
- iron → **conductor**
- glass → **insulator**
- copper → **conductor**
- air → **insulator**
- dry cloth → **insulator**

Full working after a second miss:

> The right pairs are:  
> rubber → insulator  
> iron → conductor  
> glass → insulator  
> copper → conductor  
> air → insulator  
> dry cloth → insulator  

> Sort the materials: conductor or insulator?

Groups: conductor · insulator
- aluminium → **conductor**
- rubber → **insulator**
- silver → **conductor**
- glass → **insulator**
- iron → **conductor**
- wood → **insulator**

Full working after a second miss:

> The right pairs are:  
> aluminium → conductor  
> rubber → insulator  
> silver → conductor  
> glass → insulator  
> iron → conductor  
> wood → insulator  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-11-thermal` · Lesson 11 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do pots have wooden or plastic handles? | Wood and plastic are thermal insulators. | They are cheaper than metal. · They conduct heat well. · They look nice. | Cost is not the reason given. · They do the opposite. · The reason is safety from heat. | Insulating handles stay cool. |
| Why do fish sellers keep fish in a cold box? | The box insulates the fish from the heat outside. | The box makes the fish heavier. · The box conducts heat in. · The box cooks the fish. | Weight is not the reason. · It does the opposite. · It keeps them cold. | An insulated box keeps heat out. |
| Which keeps a drink hot longest? | a vacuum flask | a metal cup · a glass bottle in the sun · an open bowl | Metal conducts heat away. · Glass loses heat and the sun is not insulation. · An open bowl loses heat quickly. | A vacuum flask is a good thermal insulator. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which keeps a drink hot longest?

- ◻️ a glass bottle in the sun  
  _↳ feedback if chosen: Glass loses heat and the sun is not insulation._
- ✅ a vacuum flask
- ◻️ a metal cup  
  _↳ feedback if chosen: Metal conducts heat away._
- ◻️ an open bowl  
  _↳ feedback if chosen: An open bowl loses heat quickly._

Full working after a second miss:

> A vacuum flask is a good thermal insulator.  
> So the answer is “a vacuum flask”.  

> Which keeps a drink hot longest?

- ◻️ a glass bottle in the sun  
  _↳ feedback if chosen: Glass loses heat and the sun is not insulation._
- ✅ a vacuum flask
- ◻️ an open bowl  
  _↳ feedback if chosen: An open bowl loses heat quickly._
- ◻️ a metal cup  
  _↳ feedback if chosen: Metal conducts heat away._

Full working after a second miss:

> A vacuum flask is a good thermal insulator.  
> So the answer is “a vacuum flask”.  

> Why do fish sellers keep fish in a cold box?

- ✅ The box insulates the fish from the heat outside.
- ◻️ The box makes the fish heavier.  
  _↳ feedback if chosen: Weight is not the reason._
- ◻️ The box cooks the fish.  
  _↳ feedback if chosen: It keeps them cold._
- ◻️ The box conducts heat in.  
  _↳ feedback if chosen: It does the opposite._

Full working after a second miss:

> An insulated box keeps heat out.  
> So the answer is “The box insulates the fish from the heat outside.”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-11-safe` · Lesson 11 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are electric wires covered with plastic? | Plastic is an electrical insulator and protects us from shocks. | Plastic makes the current faster. · Plastic is a conductor. · Plastic makes the wire heavier. | Plastic does not speed up current. · Plastic is an insulator. · Weight is not the reason. | The plastic insulates the wire. |
| Why must you not touch a switch with wet hands? | Water with salts conducts electricity. | Water is an insulator. · The switch will rust at once. · Wet hands are slippery only. | Tap water and sweat conduct. · That is not the danger. · The danger is an electric shock. | Wet hands can let current pass through the body. |
| What should an electrician wear? | rubber gloves and boots | metal gloves · wet clothes · a copper bracelet | Metal conducts. · Wet clothes conduct. · Copper conducts. | Rubber is an electrical insulator. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What should an electrician wear?

- ✅ rubber gloves and boots
- ◻️ wet clothes  
  _↳ feedback if chosen: Wet clothes conduct._
- ◻️ metal gloves  
  _↳ feedback if chosen: Metal conducts._
- ◻️ a copper bracelet  
  _↳ feedback if chosen: Copper conducts._

Full working after a second miss:

> Rubber is an electrical insulator.  
> So the answer is “rubber gloves and boots”.  

> Why must you not touch a switch with wet hands?

- ✅ Water with salts conducts electricity.
- ◻️ Water is an insulator.  
  _↳ feedback if chosen: Tap water and sweat conduct._
- ◻️ The switch will rust at once.  
  _↳ feedback if chosen: That is not the danger._
- ◻️ Wet hands are slippery only.  
  _↳ feedback if chosen: The danger is an electric shock._

Full working after a second miss:

> Wet hands can let current pass through the body.  
> So the answer is “Water with salts conducts electricity.”.  

> What should an electrician wear?

- ◻️ metal gloves  
  _↳ feedback if chosen: Metal conducts._
- ◻️ a copper bracelet  
  _↳ feedback if chosen: Copper conducts._
- ✅ rubber gloves and boots
- ◻️ wet clothes  
  _↳ feedback if chosen: Wet clothes conduct._

Full working after a second miss:

> Rubber is an electrical insulator.  
> So the answer is “rubber gloves and boots”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-11-spot` · Lesson 11 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Copper is a good conductor of electricity.
- ✅ Rubber is an electrical insulator.
- ✅ Air is a poor conductor of heat.
- ✅ Metals conduct heat well.
- ❌ Plastic is a good conductor of electricity.  
  _↳ Plastic is an insulator._
- ❌ Wood conducts heat better than iron.  
  _↳ Iron, a metal, conducts heat much better._
- ❌ Wet hands make it safe to touch switches.  
  _↳ Water conducts electricity: it is dangerous._


Three generated variants:

> Which statement is wrong?

- ◻️ Copper is a good conductor of electricity.
- ✅ Wood conducts heat better than iron.  
  _↳ explanation: Iron, a metal, conducts heat much better._
- ◻️ Air is a poor conductor of heat.
- ◻️ Metals conduct heat well.

Full working after a second miss:

> The wrong statement is “Wood conducts heat better than iron.”.  
> Iron, a metal, conducts heat much better.  

> Which statement is wrong?

- ✅ Wood conducts heat better than iron.  
  _↳ explanation: Iron, a metal, conducts heat much better._
- ◻️ Air is a poor conductor of heat.
- ◻️ Rubber is an electrical insulator.
- ◻️ Copper is a good conductor of electricity.

Full working after a second miss:

> The wrong statement is “Wood conducts heat better than iron.”.  
> Iron, a metal, conducts heat much better.  

> Which statement is wrong?

- ◻️ Air is a poor conductor of heat.
- ◻️ Metals conduct heat well.
- ✅ Plastic is a good conductor of electricity.  
  _↳ explanation: Plastic is an insulator._
- ◻️ Rubber is an electrical insulator.

Full working after a second miss:

> The wrong statement is “Plastic is a good conductor of electricity.”.  
> Plastic is an insulator.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-11-safe-card` · Lesson 11 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are electric wires covered with plastic? | Plastic is an electrical insulator and protects us from shocks. | Plastic makes the current faster. · Plastic is a conductor. · Plastic makes the wire heavier. | Plastic does not speed up current. · Plastic is an insulator. · Weight is not the reason. | The plastic insulates the wire. |
| Why must you not touch a switch with wet hands? | Water with salts conducts electricity. | Water is an insulator. · The switch will rust at once. · Wet hands are slippery only. | Tap water and sweat conduct. · That is not the danger. · The danger is an electric shock. | Wet hands can let current pass through the body. |
| What should an electrician wear? | rubber gloves and boots | metal gloves · wet clothes · a copper bracelet | Metal conducts. · Wet clothes conduct. · Copper conducts. | Rubber is an electrical insulator. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What should an electrician wear?

- ◻️ metal gloves  
  _↳ feedback if chosen: Metal conducts._
- ◻️ wet clothes  
  _↳ feedback if chosen: Wet clothes conduct._
- ◻️ a copper bracelet  
  _↳ feedback if chosen: Copper conducts._
- ✅ rubber gloves and boots

Full working after a second miss:

> Rubber is an electrical insulator.  
> So the answer is “rubber gloves and boots”.  

> Why are electric wires covered with plastic?

- ◻️ Plastic is a conductor.  
  _↳ feedback if chosen: Plastic is an insulator._
- ✅ Plastic is an electrical insulator and protects us from shocks.
- ◻️ Plastic makes the wire heavier.  
  _↳ feedback if chosen: Weight is not the reason._
- ◻️ Plastic makes the current faster.  
  _↳ feedback if chosen: Plastic does not speed up current._

Full working after a second miss:

> The plastic insulates the wire.  
> So the answer is “Plastic is an electrical insulator and protects us from shocks.”.  

> Why are electric wires covered with plastic?

- ◻️ Plastic is a conductor.  
  _↳ feedback if chosen: Plastic is an insulator._
- ◻️ Plastic makes the current faster.  
  _↳ feedback if chosen: Plastic does not speed up current._
- ✅ Plastic is an electrical insulator and protects us from shocks.
- ◻️ Plastic makes the wire heavier.  
  _↳ feedback if chosen: Weight is not the reason._

Full working after a second miss:

> The plastic insulates the wire.  
> So the answer is “Plastic is an electrical insulator and protects us from shocks.”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-12-expand` · Lesson 12 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A football left in the hot sun becomes harder. Why? | The air inside expands. | The leather shrinks only. · The air leaks out. · The ball gets heavier. | The main reason is the air expanding. · That would make it softer. · Its mass does not change. | Heated air expands and presses harder on the ball. |
| Why are gaps left in a long concrete bridge? | To let it expand in the heat without cracking. | To let rain fall through. · To save concrete. · For decoration. | The gaps are for expansion. · Saving material is not the reason. · They have a purpose. | Expansion gaps stop cracking. |
| Which expands the most when heated by the same amount? | a gas | a solid · a liquid · they all expand the same | Solids expand the least. · Liquids expand less than gases. · They expand differently. | Gases expand the most. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why are gaps left in a long concrete bridge?

- ◻️ To save concrete.  
  _↳ feedback if chosen: Saving material is not the reason._
- ✅ To let it expand in the heat without cracking.
- ◻️ To let rain fall through.  
  _↳ feedback if chosen: The gaps are for expansion._
- ◻️ For decoration.  
  _↳ feedback if chosen: They have a purpose._

Full working after a second miss:

> Expansion gaps stop cracking.  
> So the answer is “To let it expand in the heat without cracking.”.  

> Why are gaps left in a long concrete bridge?

- ✅ To let it expand in the heat without cracking.
- ◻️ To save concrete.  
  _↳ feedback if chosen: Saving material is not the reason._
- ◻️ To let rain fall through.  
  _↳ feedback if chosen: The gaps are for expansion._
- ◻️ For decoration.  
  _↳ feedback if chosen: They have a purpose._

Full working after a second miss:

> Expansion gaps stop cracking.  
> So the answer is “To let it expand in the heat without cracking.”.  

> Which expands the most when heated by the same amount?

- ◻️ a liquid  
  _↳ feedback if chosen: Liquids expand less than gases._
- ◻️ a solid  
  _↳ feedback if chosen: Solids expand the least._
- ✅ a gas
- ◻️ they all expand the same  
  _↳ feedback if chosen: They expand differently._

Full working after a second miss:

> Gases expand the most.  
> So the answer is “a gas”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-12-reverse` · Lesson 12 · matching, level 1

Prompt: Sort the changes: can they be reversed?

Pairs (4 shown each time, sorted into groups):

- melting ice → **reversible**
- melting candle wax → **reversible**
- a rail expanding in the sun → **reversible**
- boiling water → **reversible**
- burning paper → **not reversible**
- frying an egg → **not reversible**
- toasting bread → **not reversible**
- burning firewood → **not reversible**


Three generated variants:

> Sort the changes: can they be reversed?

Groups: reversible · not reversible
- boiling water → **reversible**
- burning paper → **not reversible**
- frying an egg → **not reversible**
- toasting bread → **not reversible**

Full working after a second miss:

> The right pairs are:  
> boiling water → reversible  
> burning paper → not reversible  
> frying an egg → not reversible  
> toasting bread → not reversible  

> Sort the changes: can they be reversed?

Groups: reversible · not reversible
- boiling water → **reversible**
- toasting bread → **not reversible**
- burning paper → **not reversible**
- burning firewood → **not reversible**

Full working after a second miss:

> The right pairs are:  
> boiling water → reversible  
> toasting bread → not reversible  
> burning paper → not reversible  
> burning firewood → not reversible  

> Sort the changes: can they be reversed?

Groups: reversible · not reversible
- toasting bread → **not reversible**
- burning firewood → **not reversible**
- melting ice → **reversible**
- burning paper → **not reversible**

Full working after a second miss:

> The right pairs are:  
> toasting bread → not reversible  
> burning firewood → not reversible  
> melting ice → reversible  
> burning paper → not reversible  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-12-bimetal` · Lesson 12 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does a bimetallic strip bend when heated? | Its two metals expand by different amounts. | It melts. · It loses mass. · Only one metal gets hot. | It does not melt. · Its mass does not change. · Both are heated. | Different expansion makes it bend. |
| Where is a bimetallic strip used? | in the thermostat of an electric iron | in a football · in a ruler · in a light bulb filament | A football has no thermostat. · A ruler measures length. · A filament is a thin wire that glows. | It switches the iron off when hot. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Where is a bimetallic strip used?

- ◻️ in a light bulb filament  
  _↳ feedback if chosen: A filament is a thin wire that glows._
- ✅ in the thermostat of an electric iron
- ◻️ in a ruler  
  _↳ feedback if chosen: A ruler measures length._
- ◻️ in a football  
  _↳ feedback if chosen: A football has no thermostat._

Full working after a second miss:

> It switches the iron off when hot.  
> So the answer is “in the thermostat of an electric iron”.  

> Where is a bimetallic strip used?

- ◻️ in a light bulb filament  
  _↳ feedback if chosen: A filament is a thin wire that glows._
- ✅ in the thermostat of an electric iron
- ◻️ in a football  
  _↳ feedback if chosen: A football has no thermostat._
- ◻️ in a ruler  
  _↳ feedback if chosen: A ruler measures length._

Full working after a second miss:

> It switches the iron off when hot.  
> So the answer is “in the thermostat of an electric iron”.  

> Where is a bimetallic strip used?

- ◻️ in a football  
  _↳ feedback if chosen: A football has no thermostat._
- ✅ in the thermostat of an electric iron
- ◻️ in a light bulb filament  
  _↳ feedback if chosen: A filament is a thin wire that glows._
- ◻️ in a ruler  
  _↳ feedback if chosen: A ruler measures length._

Full working after a second miss:

> It switches the iron off when hot.  
> So the answer is “in the thermostat of an electric iron”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-12-spot` · Lesson 12 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Heating makes most materials expand.
- ✅ Burning wood cannot be reversed.
- ✅ Gases expand more than solids.
- ✅ A bimetallic strip bends when heated.
- ❌ Heating makes solids contract.  
  _↳ Heating makes solids expand; cooling makes them contract._
- ❌ Burning paper is easy to reverse.  
  _↳ Burning cannot be reversed._
- ❌ Railways need no gaps because steel does not expand.  
  _↳ Steel expands in the heat: gaps are needed._


Three generated variants:

> Which statement is wrong?

- ◻️ Gases expand more than solids.
- ◻️ Heating makes most materials expand.
- ✅ Railways need no gaps because steel does not expand.  
  _↳ explanation: Steel expands in the heat: gaps are needed._
- ◻️ Burning wood cannot be reversed.

Full working after a second miss:

> The wrong statement is “Railways need no gaps because steel does not expand.”.  
> Steel expands in the heat: gaps are needed.  

> Which statement is wrong?

- ◻️ Burning wood cannot be reversed.
- ◻️ Gases expand more than solids.
- ✅ Heating makes solids contract.  
  _↳ explanation: Heating makes solids expand; cooling makes them contract._
- ◻️ Heating makes most materials expand.

Full working after a second miss:

> The wrong statement is “Heating makes solids contract.”.  
> Heating makes solids expand; cooling makes them contract.  

> Which statement is wrong?

- ✅ Railways need no gaps because steel does not expand.  
  _↳ explanation: Steel expands in the heat: gaps are needed._
- ◻️ A bimetallic strip bends when heated.
- ◻️ Gases expand more than solids.
- ◻️ Burning wood cannot be reversed.

Full working after a second miss:

> The wrong statement is “Railways need no gaps because steel does not expand.”.  
> Steel expands in the heat: gaps are needed.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-12-bimetal-card` · Lesson 12 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does a bimetallic strip bend when heated? | Its two metals expand by different amounts. | It melts. · It loses mass. · Only one metal gets hot. | It does not melt. · Its mass does not change. · Both are heated. | Different expansion makes it bend. |
| Where is a bimetallic strip used? | in the thermostat of an electric iron | in a football · in a ruler · in a light bulb filament | A football has no thermostat. · A ruler measures length. · A filament is a thin wire that glows. | It switches the iron off when hot. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does a bimetallic strip bend when heated?

- ✅ Its two metals expand by different amounts.
- ◻️ It melts.  
  _↳ feedback if chosen: It does not melt._
- ◻️ Only one metal gets hot.  
  _↳ feedback if chosen: Both are heated._
- ◻️ It loses mass.  
  _↳ feedback if chosen: Its mass does not change._

Full working after a second miss:

> Different expansion makes it bend.  
> So the answer is “Its two metals expand by different amounts.”.  

> Why does a bimetallic strip bend when heated?

- ✅ Its two metals expand by different amounts.
- ◻️ It loses mass.  
  _↳ feedback if chosen: Its mass does not change._
- ◻️ Only one metal gets hot.  
  _↳ feedback if chosen: Both are heated._
- ◻️ It melts.  
  _↳ feedback if chosen: It does not melt._

Full working after a second miss:

> Different expansion makes it bend.  
> So the answer is “Its two metals expand by different amounts.”.  

> Where is a bimetallic strip used?

- ◻️ in a ruler  
  _↳ feedback if chosen: A ruler measures length._
- ◻️ in a football  
  _↳ feedback if chosen: A football has no thermostat._
- ◻️ in a light bulb filament  
  _↳ feedback if chosen: A filament is a thin wire that glows._
- ✅ in the thermostat of an electric iron

Full working after a second miss:

> It switches the iron off when hot.  
> So the answer is “in the thermostat of an electric iron”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-13-effect` · Lesson 13 · matching, level 1

Prompt: Match each device to the effect of current it uses.

Pairs (4 shown each time, sorted into groups):

- an electric iron → **heating effect**
- a hot plate → **heating effect**
- a water heater → **heating effect**
- a light bulb → **lighting effect**
- a torch → **lighting effect**
- an electric bell → **magnetic effect**
- an electric motor in a fan → **magnetic effect**
- an electromagnet in a scrapyard crane → **magnetic effect**
- silver-plating a spoon → **chemical effect**
- charging a car battery → **chemical effect**


Three generated variants:

> Match each device to the effect of current it uses.

Groups: heating effect · lighting effect · magnetic effect · chemical effect
- a torch → **lighting effect**
- an electric bell → **magnetic effect**
- charging a car battery → **chemical effect**
- an electric iron → **heating effect**

Full working after a second miss:

> The right pairs are:  
> a torch → lighting effect  
> an electric bell → magnetic effect  
> charging a car battery → chemical effect  
> an electric iron → heating effect  

> Match each device to the effect of current it uses.

Groups: heating effect · magnetic effect · chemical effect
- an electromagnet in a scrapyard crane → **magnetic effect**
- silver-plating a spoon → **chemical effect**
- a water heater → **heating effect**
- an electric motor in a fan → **magnetic effect**

Full working after a second miss:

> The right pairs are:  
> an electromagnet in a scrapyard crane → magnetic effect  
> silver-plating a spoon → chemical effect  
> a water heater → heating effect  
> an electric motor in a fan → magnetic effect  

> Match each device to the effect of current it uses.

Groups: heating effect · lighting effect · magnetic effect
- a torch → **lighting effect**
- an electric iron → **heating effect**
- an electric bell → **magnetic effect**
- an electromagnet in a scrapyard crane → **magnetic effect**

Full working after a second miss:

> The right pairs are:  
> a torch → lighting effect  
> an electric iron → heating effect  
> an electric bell → magnetic effect  
> an electromagnet in a scrapyard crane → magnetic effect  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-13-fuse` · Lesson 13 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does a fuse do when the current is too big? | It melts and breaks the circuit. | It makes the current bigger. · It lights up. · It becomes a magnet. | It stops the current. · It is not a lamp. · It works by heating. | The thin wire melts and protects the circuit. |
| Which effect of current does a fuse use? | the heating effect | the magnetic effect · the chemical effect · the lighting effect | A fuse is not a magnet. · It does not break down liquids. · It does not give light. | Too much current heats the fuse wire until it melts. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which effect of current does a fuse use?

- ✅ the heating effect
- ◻️ the chemical effect  
  _↳ feedback if chosen: It does not break down liquids._
- ◻️ the lighting effect  
  _↳ feedback if chosen: It does not give light._
- ◻️ the magnetic effect  
  _↳ feedback if chosen: A fuse is not a magnet._

Full working after a second miss:

> Too much current heats the fuse wire until it melts.  
> So the answer is “the heating effect”.  

> Which effect of current does a fuse use?

- ◻️ the chemical effect  
  _↳ feedback if chosen: It does not break down liquids._
- ◻️ the lighting effect  
  _↳ feedback if chosen: It does not give light._
- ✅ the heating effect
- ◻️ the magnetic effect  
  _↳ feedback if chosen: A fuse is not a magnet._

Full working after a second miss:

> Too much current heats the fuse wire until it melts.  
> So the answer is “the heating effect”.  

> Which effect of current does a fuse use?

- ◻️ the chemical effect  
  _↳ feedback if chosen: It does not break down liquids._
- ✅ the heating effect
- ◻️ the lighting effect  
  _↳ feedback if chosen: It does not give light._
- ◻️ the magnetic effect  
  _↳ feedback if chosen: A fuse is not a magnet._

Full working after a second miss:

> Too much current heats the fuse wire until it melts.  
> So the answer is “the heating effect”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-13-energy` · Lesson 13 · multiple choice, level 2

Prompt: Which energy change happens in {X.q}?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| an electric fan | electrical → movement | electrical → light · heat → electrical · sound → electrical | A fan's main output is movement. · A fan uses electricity. · A fan uses electricity. | The motor turns the blades: movement. |
| a radio | electrical → sound | sound → electrical · electrical → heat only · light → electrical | A radio makes sound. · Its main output is sound. · It uses electrical energy. | The loudspeaker gives sound. |
| a light bulb | electrical → light (and heat) | light → electrical · electrical → movement · electrical → sound | It uses electricity. · It does not move. · It does not make sound. | A bulb gives light and some heat. |
| an electric iron | electrical → heat | heat → electrical · electrical → sound · electrical → movement | It uses electricity. · It does not make sound. · It does not move by itself. | An iron's plate gets hot. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which energy change happens in a radio?

- ◻️ electrical → heat only  
  _↳ feedback if chosen: Its main output is sound._
- ◻️ sound → electrical  
  _↳ feedback if chosen: A radio makes sound._
- ◻️ light → electrical  
  _↳ feedback if chosen: It uses electrical energy._
- ✅ electrical → sound

Full working after a second miss:

> The loudspeaker gives sound.  
> So the answer is “electrical → sound”.  

> Which energy change happens in an electric fan?

- ◻️ heat → electrical  
  _↳ feedback if chosen: A fan uses electricity._
- ✅ electrical → movement
- ◻️ sound → electrical  
  _↳ feedback if chosen: A fan uses electricity._
- ◻️ electrical → light  
  _↳ feedback if chosen: A fan's main output is movement._

Full working after a second miss:

> The motor turns the blades: movement.  
> So the answer is “electrical → movement”.  

> Which energy change happens in a radio?

- ◻️ light → electrical  
  _↳ feedback if chosen: It uses electrical energy._
- ◻️ sound → electrical  
  _↳ feedback if chosen: A radio makes sound._
- ✅ electrical → sound
- ◻️ electrical → heat only  
  _↳ feedback if chosen: Its main output is sound._

Full working after a second miss:

> The loudspeaker gives sound.  
> So the answer is “electrical → sound”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-13-spot` · Lesson 13 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ An electric iron uses the heating effect of current.
- ✅ An electric bell uses the magnetic effect.
- ✅ Electroplating uses the chemical effect.
- ✅ A fuse melts if the current is too big.
- ❌ A light bulb uses the chemical effect of current.  
  _↳ A bulb uses the lighting (and heating) effect._
- ❌ A fuse is a thick wire that never melts.  
  _↳ A fuse is a thin wire made to melt._
- ❌ An electric fan changes movement into electrical energy.  
  _↳ A fan changes electrical energy into movement._


Three generated variants:

> Which statement is wrong?

- ◻️ A fuse melts if the current is too big.
- ◻️ An electric bell uses the magnetic effect.
- ✅ An electric fan changes movement into electrical energy.  
  _↳ explanation: A fan changes electrical energy into movement._
- ◻️ An electric iron uses the heating effect of current.

Full working after a second miss:

> The wrong statement is “An electric fan changes movement into electrical energy.”.  
> A fan changes electrical energy into movement.  

> Which statement is wrong?

- ◻️ A fuse melts if the current is too big.
- ◻️ Electroplating uses the chemical effect.
- ◻️ An electric bell uses the magnetic effect.
- ✅ A light bulb uses the chemical effect of current.  
  _↳ explanation: A bulb uses the lighting (and heating) effect._

Full working after a second miss:

> The wrong statement is “A light bulb uses the chemical effect of current.”.  
> A bulb uses the lighting (and heating) effect.  

> Which statement is wrong?

- ✅ A light bulb uses the chemical effect of current.  
  _↳ explanation: A bulb uses the lighting (and heating) effect._
- ◻️ A fuse melts if the current is too big.
- ◻️ An electric bell uses the magnetic effect.
- ◻️ Electroplating uses the chemical effect.

Full working after a second miss:

> The wrong statement is “A light bulb uses the chemical effect of current.”.  
> A bulb uses the lighting (and heating) effect.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-13-energy-card` · Lesson 13 · multiple choice, level 1

Prompt: Which energy change happens in {X.q}?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| an electric fan | electrical → movement | electrical → light · heat → electrical · sound → electrical | A fan's main output is movement. · A fan uses electricity. · A fan uses electricity. | The motor turns the blades: movement. |
| a radio | electrical → sound | sound → electrical · electrical → heat only · light → electrical | A radio makes sound. · Its main output is sound. · It uses electrical energy. | The loudspeaker gives sound. |
| a light bulb | electrical → light (and heat) | light → electrical · electrical → movement · electrical → sound | It uses electricity. · It does not move. · It does not make sound. | A bulb gives light and some heat. |
| an electric iron | electrical → heat | heat → electrical · electrical → sound · electrical → movement | It uses electricity. · It does not make sound. · It does not move by itself. | An iron's plate gets hot. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which energy change happens in a light bulb?

- ✅ electrical → light (and heat)
- ◻️ electrical → movement  
  _↳ feedback if chosen: It does not move._
- ◻️ electrical → sound  
  _↳ feedback if chosen: It does not make sound._
- ◻️ light → electrical  
  _↳ feedback if chosen: It uses electricity._

Full working after a second miss:

> A bulb gives light and some heat.  
> So the answer is “electrical → light (and heat)”.  

> Which energy change happens in an electric iron?

- ◻️ electrical → movement  
  _↳ feedback if chosen: It does not move by itself._
- ◻️ electrical → sound  
  _↳ feedback if chosen: It does not make sound._
- ◻️ heat → electrical  
  _↳ feedback if chosen: It uses electricity._
- ✅ electrical → heat

Full working after a second miss:

> An iron's plate gets hot.  
> So the answer is “electrical → heat”.  

> Which energy change happens in a radio?

- ✅ electrical → sound
- ◻️ sound → electrical  
  _↳ feedback if chosen: A radio makes sound._
- ◻️ electrical → heat only  
  _↳ feedback if chosen: Its main output is sound._
- ◻️ light → electrical  
  _↳ feedback if chosen: It uses electrical energy._

Full working after a second miss:

> The loudspeaker gives sound.  
> So the answer is “electrical → sound”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-14-what` · Lesson 14 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is conduction? | heat passing through a material from particle to particle | a material moving to carry heat · heat travelling as light · a material losing its mass | That is convection. · That is radiation. · Conduction does not change mass. | Energy passes between particles; the material stays still. |
| Why do metals conduct heat well? | They have free electrons that carry energy. | They are heavy. · They are shiny. · They are cold. | Weight is not the reason. · Shine is not the reason. · Temperature is not the reason. | Free electrons carry energy quickly through a metal. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is conduction?

- ◻️ a material moving to carry heat  
  _↳ feedback if chosen: That is convection._
- ◻️ heat travelling as light  
  _↳ feedback if chosen: That is radiation._
- ✅ heat passing through a material from particle to particle
- ◻️ a material losing its mass  
  _↳ feedback if chosen: Conduction does not change mass._

Full working after a second miss:

> Energy passes between particles; the material stays still.  
> So the answer is “heat passing through a material from particle to particle”.  

> Why do metals conduct heat well?

- ✅ They have free electrons that carry energy.
- ◻️ They are heavy.  
  _↳ feedback if chosen: Weight is not the reason._
- ◻️ They are shiny.  
  _↳ feedback if chosen: Shine is not the reason._
- ◻️ They are cold.  
  _↳ feedback if chosen: Temperature is not the reason._

Full working after a second miss:

> Free electrons carry energy quickly through a metal.  
> So the answer is “They have free electrons that carry energy.”.  

> What is conduction?

- ◻️ a material losing its mass  
  _↳ feedback if chosen: Conduction does not change mass._
- ◻️ a material moving to carry heat  
  _↳ feedback if chosen: That is convection._
- ◻️ heat travelling as light  
  _↳ feedback if chosen: That is radiation._
- ✅ heat passing through a material from particle to particle

Full working after a second miss:

> Energy passes between particles; the material stays still.  
> So the answer is “heat passing through a material from particle to particle”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-14-order` · Lesson 14 · ordering, level 1

Prompt: Put these materials in order, best conductor of heat first.

Items in the right order:

1. copper
2. aluminium
3. iron
4. glass
5. wood


Three generated variants:

> Put these materials in order, best conductor of heat first.

Shown as: glass · iron · wood · aluminium · copper
Correct order: copper → aluminium → iron → glass → wood

Full working after a second miss:

> The correct order is: copper → aluminium → iron → glass → wood.  

> Put these materials in order, best conductor of heat first.

Shown as: aluminium · wood · iron · copper · glass
Correct order: copper → aluminium → iron → glass → wood

Full working after a second miss:

> The correct order is: copper → aluminium → iron → glass → wood.  

> Put these materials in order, best conductor of heat first.

Shown as: wood · copper · aluminium · iron · glass
Correct order: copper → aluminium → iron → glass → wood

Full working after a second miss:

> The correct order is: copper → aluminium → iron → glass → wood.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-14-circuit` · Lesson 14 · multiple choice, level 1

Prompt: A material is placed in a circuit with a cell and a bulb. {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The bulb lights. What does this show? | The material conducts electricity. | The material is an insulator. · The cell is flat. · The bulb is broken. | Insulators stop the current. · A flat cell would not light the bulb. · A broken bulb would not light. | The circuit is closed through a conductor. |
| Which of these would light the bulb? | an iron nail | a plastic ruler · a rubber band · a dry stick | Plastic is an insulator. · Rubber is an insulator. · Dry wood is an insulator. | Metals conduct electricity. |
| The bulb stays off with a glass rod. What does this show? | Glass is an electrical insulator. | Glass conducts well. · The current is too big. · The bulb is too bright. | The bulb would light. · There is no current. · It is off. | No current flows through an insulator. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A material is placed in a circuit with a cell and a bulb. Which of these would light the bulb?

- ◻️ a dry stick  
  _↳ feedback if chosen: Dry wood is an insulator._
- ◻️ a rubber band  
  _↳ feedback if chosen: Rubber is an insulator._
- ✅ an iron nail
- ◻️ a plastic ruler  
  _↳ feedback if chosen: Plastic is an insulator._

Full working after a second miss:

> Metals conduct electricity.  
> So the answer is “an iron nail”.  

> A material is placed in a circuit with a cell and a bulb. The bulb lights. What does this show?

- ◻️ The bulb is broken.  
  _↳ feedback if chosen: A broken bulb would not light._
- ◻️ The cell is flat.  
  _↳ feedback if chosen: A flat cell would not light the bulb._
- ◻️ The material is an insulator.  
  _↳ feedback if chosen: Insulators stop the current._
- ✅ The material conducts electricity.

Full working after a second miss:

> The circuit is closed through a conductor.  
> So the answer is “The material conducts electricity.”.  

> A material is placed in a circuit with a cell and a bulb. The bulb lights. What does this show?

- ◻️ The material is an insulator.  
  _↳ feedback if chosen: Insulators stop the current._
- ◻️ The bulb is broken.  
  _↳ feedback if chosen: A broken bulb would not light._
- ✅ The material conducts electricity.
- ◻️ The cell is flat.  
  _↳ feedback if chosen: A flat cell would not light the bulb._

Full working after a second miss:

> The circuit is closed through a conductor.  
> So the answer is “The material conducts electricity.”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-14-wax` · Lesson 14 · multiple choice, level 2

Prompt: Drops of wax are stuck along rods of different materials, and one end of each rod is heated. {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| On which rod does the wax melt furthest first? | copper | glass · wood · iron | Glass is a poor conductor. · Wood is an insulator. · Iron conducts, but less well than copper. | Copper is the best conductor of the four. |
| What must be kept the same for a fair test? | the length and thickness of the rods and the heat given | nothing · only the colour of the rods · the material of the rods | A fair test keeps other variables the same. · Colour does not matter here. · The material is what we change. | Only the material should change. |
| On which rod does the wax hardly melt? | glass | copper · aluminium · iron | Copper conducts best. · Aluminium conducts well. · Iron is a metal and conducts. | Glass is a poor conductor of heat. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Drops of wax are stuck along rods of different materials, and one end of each rod is heated. On which rod does the wax melt furthest first?

- ◻️ wood  
  _↳ feedback if chosen: Wood is an insulator._
- ◻️ glass  
  _↳ feedback if chosen: Glass is a poor conductor._
- ✅ copper
- ◻️ iron  
  _↳ feedback if chosen: Iron conducts, but less well than copper._

Full working after a second miss:

> Copper is the best conductor of the four.  
> So the answer is “copper”.  

> Drops of wax are stuck along rods of different materials, and one end of each rod is heated. On which rod does the wax melt furthest first?

- ◻️ glass  
  _↳ feedback if chosen: Glass is a poor conductor._
- ◻️ iron  
  _↳ feedback if chosen: Iron conducts, but less well than copper._
- ✅ copper
- ◻️ wood  
  _↳ feedback if chosen: Wood is an insulator._

Full working after a second miss:

> Copper is the best conductor of the four.  
> So the answer is “copper”.  

> Drops of wax are stuck along rods of different materials, and one end of each rod is heated. On which rod does the wax melt furthest first?

- ✅ copper
- ◻️ glass  
  _↳ feedback if chosen: Glass is a poor conductor._
- ◻️ wood  
  _↳ feedback if chosen: Wood is an insulator._
- ◻️ iron  
  _↳ feedback if chosen: Iron conducts, but less well than copper._

Full working after a second miss:

> Copper is the best conductor of the four.  
> So the answer is “copper”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-14-spot` · Lesson 14 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Copper conducts heat better than iron.
- ✅ Current needs a closed circuit.
- ✅ Wood is a poor conductor of heat.
- ✅ In conduction the material does not move.
- ❌ In conduction the hot material flows to the cold place.  
  _↳ That is convection; in conduction the material stays still._
- ❌ Glass conducts heat better than copper.  
  _↳ Copper is a far better conductor._
- ❌ A bulb lights in an open circuit.  
  _↳ Current flows only in a closed circuit._


Three generated variants:

> Which statement is wrong?

- ◻️ Wood is a poor conductor of heat.
- ◻️ In conduction the material does not move.
- ✅ Glass conducts heat better than copper.  
  _↳ explanation: Copper is a far better conductor._
- ◻️ Current needs a closed circuit.

Full working after a second miss:

> The wrong statement is “Glass conducts heat better than copper.”.  
> Copper is a far better conductor.  

> Which statement is wrong?

- ◻️ Copper conducts heat better than iron.
- ◻️ Current needs a closed circuit.
- ◻️ Wood is a poor conductor of heat.
- ✅ A bulb lights in an open circuit.  
  _↳ explanation: Current flows only in a closed circuit._

Full working after a second miss:

> The wrong statement is “A bulb lights in an open circuit.”.  
> Current flows only in a closed circuit.  

> Which statement is wrong?

- ◻️ In conduction the material does not move.
- ◻️ Copper conducts heat better than iron.
- ◻️ Wood is a poor conductor of heat.
- ✅ In conduction the hot material flows to the cold place.  
  _↳ explanation: That is convection; in conduction the material stays still._

Full working after a second miss:

> The wrong statement is “In conduction the hot material flows to the cold place.”.  
> That is convection; in conduction the material stays still.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-15-sort` · Lesson 15 · matching, level 1

Prompt: Sort the energy sources: renewable or non-renewable?

Pairs (4 shown each time, sorted into groups):

- coal → **non-renewable**
- crude oil (petrol, kerosene) → **non-renewable**
- natural gas (cooking gas) → **non-renewable**
- uranium (nuclear fuel) → **non-renewable**
- sunlight → **renewable**
- wind → **renewable**
- flowing water in a dam → **renewable**
- firewood from new trees → **renewable**


Three generated variants:

> Sort the energy sources: renewable or non-renewable?

Groups: non-renewable · renewable
- firewood from new trees → **renewable**
- sunlight → **renewable**
- crude oil (petrol, kerosene) → **non-renewable**
- coal → **non-renewable**

Full working after a second miss:

> The right pairs are:  
> firewood from new trees → renewable  
> sunlight → renewable  
> crude oil (petrol, kerosene) → non-renewable  
> coal → non-renewable  

> Sort the energy sources: renewable or non-renewable?

Groups: non-renewable · renewable
- uranium (nuclear fuel) → **non-renewable**
- natural gas (cooking gas) → **non-renewable**
- flowing water in a dam → **renewable**
- firewood from new trees → **renewable**

Full working after a second miss:

> The right pairs are:  
> uranium (nuclear fuel) → non-renewable  
> natural gas (cooking gas) → non-renewable  
> flowing water in a dam → renewable  
> firewood from new trees → renewable  

> Sort the energy sources: renewable or non-renewable?

Groups: non-renewable · renewable
- coal → **non-renewable**
- sunlight → **renewable**
- wind → **renewable**
- crude oil (petrol, kerosene) → **non-renewable**

Full working after a second miss:

> The right pairs are:  
> coal → non-renewable  
> sunlight → renewable  
> wind → renewable  
> crude oil (petrol, kerosene) → non-renewable  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-15-fossil` · Lesson 15 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which of these is a fossil fuel? | coal | sunlight · wind · uranium | Sunlight is renewable. · Wind is renewable. · Uranium is a nuclear fuel, not a fossil fuel. | Coal formed from ancient plants. |
| Where does kerosene come from? | crude oil | coal · uranium · wind | Kerosene is refined from crude oil. · Uranium is a nuclear fuel. · Wind is not a fuel. | Kerosene is made from crude oil. |
| How did fossil fuels form? | from dead plants and animals over millions of years | from rain last year · from sunlight in one day · from rocks melting quickly | It took millions of years. · It took millions of years. · They come from living things. | They formed slowly from buried remains of living things. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which of these is a fossil fuel?

- ◻️ sunlight  
  _↳ feedback if chosen: Sunlight is renewable._
- ◻️ uranium  
  _↳ feedback if chosen: Uranium is a nuclear fuel, not a fossil fuel._
- ◻️ wind  
  _↳ feedback if chosen: Wind is renewable._
- ✅ coal

Full working after a second miss:

> Coal formed from ancient plants.  
> So the answer is “coal”.  

> Where does kerosene come from?

- ✅ crude oil
- ◻️ uranium  
  _↳ feedback if chosen: Uranium is a nuclear fuel._
- ◻️ coal  
  _↳ feedback if chosen: Kerosene is refined from crude oil._
- ◻️ wind  
  _↳ feedback if chosen: Wind is not a fuel._

Full working after a second miss:

> Kerosene is made from crude oil.  
> So the answer is “crude oil”.  

> Which of these is a fossil fuel?

- ◻️ sunlight  
  _↳ feedback if chosen: Sunlight is renewable._
- ◻️ uranium  
  _↳ feedback if chosen: Uranium is a nuclear fuel, not a fossil fuel._
- ✅ coal
- ◻️ wind  
  _↳ feedback if chosen: Wind is renewable._

Full working after a second miss:

> Coal formed from ancient plants.  
> So the answer is “coal”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-15-problem` · Lesson 15 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are fossil fuels called non-renewable? | They will run out: they form far more slowly than we use them. | They are cheap. · They do not burn. · They come from the sun every day. | Price is not the reason. · They do burn. · That describes solar energy. | We use them much faster than they form. |
| Which is a problem of burning fossil fuels? | It pollutes the air with smoke and carbon dioxide. | It makes the air cleaner. · It makes more fuel. · It cools the Earth. | It makes the air dirtier. · It uses fuel up. · Carbon dioxide warms the Earth. | Burning releases smoke and carbon dioxide. |
| Which source of electricity in Cameroon is renewable? | the hydroelectric dams at Edéa and Song Loulou | a diesel generator · a thermal power station burning oil · a coal fire | Diesel comes from crude oil. · Oil is non-renewable. · Coal is non-renewable. | Flowing water does not run out. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is a problem of burning fossil fuels?

- ◻️ It makes more fuel.  
  _↳ feedback if chosen: It uses fuel up._
- ◻️ It cools the Earth.  
  _↳ feedback if chosen: Carbon dioxide warms the Earth._
- ◻️ It makes the air cleaner.  
  _↳ feedback if chosen: It makes the air dirtier._
- ✅ It pollutes the air with smoke and carbon dioxide.

Full working after a second miss:

> Burning releases smoke and carbon dioxide.  
> So the answer is “It pollutes the air with smoke and carbon dioxide.”.  

> Which source of electricity in Cameroon is renewable?

- ◻️ a diesel generator  
  _↳ feedback if chosen: Diesel comes from crude oil._
- ◻️ a coal fire  
  _↳ feedback if chosen: Coal is non-renewable._
- ✅ the hydroelectric dams at Edéa and Song Loulou
- ◻️ a thermal power station burning oil  
  _↳ feedback if chosen: Oil is non-renewable._

Full working after a second miss:

> Flowing water does not run out.  
> So the answer is “the hydroelectric dams at Edéa and Song Loulou”.  

> Which is a problem of burning fossil fuels?

- ✅ It pollutes the air with smoke and carbon dioxide.
- ◻️ It cools the Earth.  
  _↳ feedback if chosen: Carbon dioxide warms the Earth._
- ◻️ It makes the air cleaner.  
  _↳ feedback if chosen: It makes the air dirtier._
- ◻️ It makes more fuel.  
  _↳ feedback if chosen: It uses fuel up._

Full working after a second miss:

> Burning releases smoke and carbon dioxide.  
> So the answer is “It pollutes the air with smoke and carbon dioxide.”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-15-spot` · Lesson 15 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Coal is a fossil fuel.
- ✅ Crude oil will run out one day.
- ✅ Cooking gas is natural gas.
- ✅ Burning petrol produces carbon dioxide.
- ❌ Wind is a non-renewable energy source.  
  _↳ Wind does not run out: it is renewable._
- ❌ Fossil fuels form in a few days.  
  _↳ They took millions of years to form._
- ❌ Burning coal makes the air cleaner.  
  _↳ It pollutes the air._


Three generated variants:

> Which statement is wrong?

- ◻️ Burning petrol produces carbon dioxide.
- ◻️ Crude oil will run out one day.
- ✅ Burning coal makes the air cleaner.  
  _↳ explanation: It pollutes the air._
- ◻️ Cooking gas is natural gas.

Full working after a second miss:

> The wrong statement is “Burning coal makes the air cleaner.”.  
> It pollutes the air.  

> Which statement is wrong?

- ◻️ Coal is a fossil fuel.
- ◻️ Burning petrol produces carbon dioxide.
- ◻️ Crude oil will run out one day.
- ✅ Burning coal makes the air cleaner.  
  _↳ explanation: It pollutes the air._

Full working after a second miss:

> The wrong statement is “Burning coal makes the air cleaner.”.  
> It pollutes the air.  

> Which statement is wrong?

- ◻️ Crude oil will run out one day.
- ✅ Wind is a non-renewable energy source.  
  _↳ explanation: Wind does not run out: it is renewable._
- ◻️ Cooking gas is natural gas.
- ◻️ Coal is a fossil fuel.

Full working after a second miss:

> The wrong statement is “Wind is a non-renewable energy source.”.  
> Wind does not run out: it is renewable.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-15-problem-card` · Lesson 15 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are fossil fuels called non-renewable? | They will run out: they form far more slowly than we use them. | They are cheap. · They do not burn. · They come from the sun every day. | Price is not the reason. · They do burn. · That describes solar energy. | We use them much faster than they form. |
| Which is a problem of burning fossil fuels? | It pollutes the air with smoke and carbon dioxide. | It makes the air cleaner. · It makes more fuel. · It cools the Earth. | It makes the air dirtier. · It uses fuel up. · Carbon dioxide warms the Earth. | Burning releases smoke and carbon dioxide. |
| Which source of electricity in Cameroon is renewable? | the hydroelectric dams at Edéa and Song Loulou | a diesel generator · a thermal power station burning oil · a coal fire | Diesel comes from crude oil. · Oil is non-renewable. · Coal is non-renewable. | Flowing water does not run out. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which source of electricity in Cameroon is renewable?

- ◻️ a diesel generator  
  _↳ feedback if chosen: Diesel comes from crude oil._
- ◻️ a thermal power station burning oil  
  _↳ feedback if chosen: Oil is non-renewable._
- ✅ the hydroelectric dams at Edéa and Song Loulou
- ◻️ a coal fire  
  _↳ feedback if chosen: Coal is non-renewable._

Full working after a second miss:

> Flowing water does not run out.  
> So the answer is “the hydroelectric dams at Edéa and Song Loulou”.  

> Which is a problem of burning fossil fuels?

- ◻️ It cools the Earth.  
  _↳ feedback if chosen: Carbon dioxide warms the Earth._
- ◻️ It makes more fuel.  
  _↳ feedback if chosen: It uses fuel up._
- ◻️ It makes the air cleaner.  
  _↳ feedback if chosen: It makes the air dirtier._
- ✅ It pollutes the air with smoke and carbon dioxide.

Full working after a second miss:

> Burning releases smoke and carbon dioxide.  
> So the answer is “It pollutes the air with smoke and carbon dioxide.”.  

> Which source of electricity in Cameroon is renewable?

- ◻️ a coal fire  
  _↳ feedback if chosen: Coal is non-renewable._
- ✅ the hydroelectric dams at Edéa and Song Loulou
- ◻️ a thermal power station burning oil  
  _↳ feedback if chosen: Oil is non-renewable._
- ◻️ a diesel generator  
  _↳ feedback if chosen: Diesel comes from crude oil._

Full working after a second miss:

> Flowing water does not run out.  
> So the answer is “the hydroelectric dams at Edéa and Song Loulou”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-16-kind` · Lesson 16 · multiple choice, level 1

Prompt: Is {X.q} a renewable energy source?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| solar energy | yes, it is renewable | no, it will run out soon · no, it is a fossil fuel · it is not an energy source | The sun shines every day. · Fossil fuels are petrol, coal and gas. · Sunlight is an energy source. | The sun is renewed every day. |
| petrol | no, it is non-renewable | yes, it is renewable · yes, it is biomass · it is not an energy source | It took millions of years to form. · Biomass is plant or animal matter. · Petrol is an energy source. | Petrol comes from petroleum, which will run out. |
| wind | yes, it is renewable | no, it will run out · no, it is a fossil fuel · it is not an energy source | Wind never runs out. · Wind is moving air. · Windmills use wind energy. | Wind is renewed by the sun heating the air. |
| coal | no, it is non-renewable | yes, it is renewable · yes, it is solar · it is not an energy source | Coal took millions of years to form. · Coal is a fossil fuel. · Coal burns to give heat. | Coal is a fossil fuel. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is petrol a renewable energy source?

- ◻️ yes, it is biomass  
  _↳ feedback if chosen: Biomass is plant or animal matter._
- ✅ no, it is non-renewable
- ◻️ yes, it is renewable  
  _↳ feedback if chosen: It took millions of years to form._
- ◻️ it is not an energy source  
  _↳ feedback if chosen: Petrol is an energy source._

Full working after a second miss:

> Petrol comes from petroleum, which will run out.  
> So the answer is “no, it is non-renewable”.  

> Is solar energy a renewable energy source?

- ◻️ no, it will run out soon  
  _↳ feedback if chosen: The sun shines every day._
- ✅ yes, it is renewable
- ◻️ it is not an energy source  
  _↳ feedback if chosen: Sunlight is an energy source._
- ◻️ no, it is a fossil fuel  
  _↳ feedback if chosen: Fossil fuels are petrol, coal and gas._

Full working after a second miss:

> The sun is renewed every day.  
> So the answer is “yes, it is renewable”.  

> Is coal a renewable energy source?

- ◻️ yes, it is renewable  
  _↳ feedback if chosen: Coal took millions of years to form._
- ◻️ it is not an energy source  
  _↳ feedback if chosen: Coal burns to give heat._
- ✅ no, it is non-renewable
- ◻️ yes, it is solar  
  _↳ feedback if chosen: Coal is a fossil fuel._

Full working after a second miss:

> Coal is a fossil fuel.  
> So the answer is “no, it is non-renewable”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-16-match` · Lesson 16 · matching, level 1

Prompt: Match each source to a use.

Pairs (4 shown each time):

- flowing water in a dam → **electricity for towns**
- sunlight on a panel → **charging a phone in a village**
- wind → **turning a windmill to pump water**
- animal dung → **biogas for cooking**
- the heat of the Earth → **geothermal power**


Three generated variants:

> Match each source to a use.

Right-hand side (shuffled): geothermal power · turning a windmill to pump water · electricity for towns · charging a phone in a village
- the heat of the Earth → **geothermal power**
- flowing water in a dam → **electricity for towns**
- sunlight on a panel → **charging a phone in a village**
- wind → **turning a windmill to pump water**

Full working after a second miss:

> The right pairs are:  
> the heat of the Earth → geothermal power  
> flowing water in a dam → electricity for towns  
> sunlight on a panel → charging a phone in a village  
> wind → turning a windmill to pump water  

> Match each source to a use.

Right-hand side (shuffled): electricity for towns · turning a windmill to pump water · charging a phone in a village · biogas for cooking
- animal dung → **biogas for cooking**
- flowing water in a dam → **electricity for towns**
- sunlight on a panel → **charging a phone in a village**
- wind → **turning a windmill to pump water**

Full working after a second miss:

> The right pairs are:  
> animal dung → biogas for cooking  
> flowing water in a dam → electricity for towns  
> sunlight on a panel → charging a phone in a village  
> wind → turning a windmill to pump water  

> Match each source to a use.

Right-hand side (shuffled): charging a phone in a village · geothermal power · electricity for towns · turning a windmill to pump water
- the heat of the Earth → **geothermal power**
- flowing water in a dam → **electricity for towns**
- wind → **turning a windmill to pump water**
- sunlight on a panel → **charging a phone in a village**

Full working after a second miss:

> The right pairs are:  
> the heat of the Earth → geothermal power  
> flowing water in a dam → electricity for towns  
> wind → turning a windmill to pump water  
> sunlight on a panel → charging a phone in a village  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-16-use` · Lesson 16 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are renewable sources better for the environment? | they do not run out and pollute less | they are always free · they work only at night · they need no equipment | Equipment like panels costs money. · Solar works by day. · They need panels, dams or turbines. | They are renewed and cleaner. |
| Where does much of Cameroon's electricity come from? | hydroelectric dams | coal mines · nuclear power stations · windmills only | Cameroon has little coal power. · Cameroon has no nuclear power station. · Windmills are rare. | Dams such as Song Loulou and Edéa produce much of it. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why are renewable sources better for the environment?

- ◻️ they need no equipment  
  _↳ feedback if chosen: They need panels, dams or turbines._
- ◻️ they work only at night  
  _↳ feedback if chosen: Solar works by day._
- ◻️ they are always free  
  _↳ feedback if chosen: Equipment like panels costs money._
- ✅ they do not run out and pollute less

Full working after a second miss:

> They are renewed and cleaner.  
> So the answer is “they do not run out and pollute less”.  

> Why are renewable sources better for the environment?

- ◻️ they are always free  
  _↳ feedback if chosen: Equipment like panels costs money._
- ◻️ they work only at night  
  _↳ feedback if chosen: Solar works by day._
- ◻️ they need no equipment  
  _↳ feedback if chosen: They need panels, dams or turbines._
- ✅ they do not run out and pollute less

Full working after a second miss:

> They are renewed and cleaner.  
> So the answer is “they do not run out and pollute less”.  

> Why are renewable sources better for the environment?

- ◻️ they are always free  
  _↳ feedback if chosen: Equipment like panels costs money._
- ◻️ they need no equipment  
  _↳ feedback if chosen: They need panels, dams or turbines._
- ◻️ they work only at night  
  _↳ feedback if chosen: Solar works by day._
- ✅ they do not run out and pollute less

Full working after a second miss:

> They are renewed and cleaner.  
> So the answer is “they do not run out and pollute less”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-16-spot` · Lesson 16 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The sun is a renewable source.
- ✅ Biogas can be made from dung.
- ✅ Coal is non-renewable.
- ✅ A dam turns flowing water into electricity.
- ❌ Petrol will never run out.  
  _↳ It is non-renewable and will run out._
- ❌ Wind energy is a fossil fuel.  
  _↳ Wind is renewable; fossil fuels are petrol, coal and gas._
- ❌ Solar panels work best in the dark.  
  _↳ They need sunlight._


Three generated variants:

> Which statement is wrong?

- ◻️ Biogas can be made from dung.
- ✅ Petrol will never run out.  
  _↳ explanation: It is non-renewable and will run out._
- ◻️ The sun is a renewable source.
- ◻️ Coal is non-renewable.

Full working after a second miss:

> The wrong statement is “Petrol will never run out.”.  
> It is non-renewable and will run out.  

> Which statement is wrong?

- ◻️ A dam turns flowing water into electricity.
- ✅ Wind energy is a fossil fuel.  
  _↳ explanation: Wind is renewable; fossil fuels are petrol, coal and gas._
- ◻️ Biogas can be made from dung.
- ◻️ The sun is a renewable source.

Full working after a second miss:

> The wrong statement is “Wind energy is a fossil fuel.”.  
> Wind is renewable; fossil fuels are petrol, coal and gas.  

> Which statement is wrong?

- ✅ Petrol will never run out.  
  _↳ explanation: It is non-renewable and will run out._
- ◻️ A dam turns flowing water into electricity.
- ◻️ Biogas can be made from dung.
- ◻️ Coal is non-renewable.

Full working after a second miss:

> The wrong statement is “Petrol will never run out.”.  
> It is non-renewable and will run out.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-16-use-card` · Lesson 16 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why are renewable sources better for the environment? | they do not run out and pollute less | they are always free · they work only at night · they need no equipment | Equipment like panels costs money. · Solar works by day. · They need panels, dams or turbines. | They are renewed and cleaner. |
| Where does much of Cameroon's electricity come from? | hydroelectric dams | coal mines · nuclear power stations · windmills only | Cameroon has little coal power. · Cameroon has no nuclear power station. · Windmills are rare. | Dams such as Song Loulou and Edéa produce much of it. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why are renewable sources better for the environment?

- ✅ they do not run out and pollute less
- ◻️ they work only at night  
  _↳ feedback if chosen: Solar works by day._
- ◻️ they need no equipment  
  _↳ feedback if chosen: They need panels, dams or turbines._
- ◻️ they are always free  
  _↳ feedback if chosen: Equipment like panels costs money._

Full working after a second miss:

> They are renewed and cleaner.  
> So the answer is “they do not run out and pollute less”.  

> Where does much of Cameroon's electricity come from?

- ✅ hydroelectric dams
- ◻️ windmills only  
  _↳ feedback if chosen: Windmills are rare._
- ◻️ nuclear power stations  
  _↳ feedback if chosen: Cameroon has no nuclear power station._
- ◻️ coal mines  
  _↳ feedback if chosen: Cameroon has little coal power._

Full working after a second miss:

> Dams such as Song Loulou and Edéa produce much of it.  
> So the answer is “hydroelectric dams”.  

> Why are renewable sources better for the environment?

- ✅ they do not run out and pollute less
- ◻️ they need no equipment  
  _↳ feedback if chosen: They need panels, dams or turbines._
- ◻️ they are always free  
  _↳ feedback if chosen: Equipment like panels costs money._
- ◻️ they work only at night  
  _↳ feedback if chosen: Solar works by day._

Full working after a second miss:

> They are renewed and cleaner.  
> So the answer is “they do not run out and pollute less”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-17-why` · Lesson 17 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is the plate of a solar water heater painted black? | black surfaces absorb heat radiation best | black is cheaper · black reflects sunlight · black keeps water cold | The reason is physics, not price. · Shiny or white surfaces reflect. · The aim is to heat the water. | Dark surfaces absorb best. |
| Why is the hot-water tank insulated? | to stop the heat escaping | to make it heavier · to let sunlight in · to cool the water | Weight is not the reason. · The tank does not collect sunlight. · The aim is to keep it hot. | Insulation reduces heat loss. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is the hot-water tank insulated?

- ◻️ to cool the water  
  _↳ feedback if chosen: The aim is to keep it hot._
- ◻️ to let sunlight in  
  _↳ feedback if chosen: The tank does not collect sunlight._
- ◻️ to make it heavier  
  _↳ feedback if chosen: Weight is not the reason._
- ✅ to stop the heat escaping

Full working after a second miss:

> Insulation reduces heat loss.  
> So the answer is “to stop the heat escaping”.  

> Why is the hot-water tank insulated?

- ◻️ to cool the water  
  _↳ feedback if chosen: The aim is to keep it hot._
- ◻️ to let sunlight in  
  _↳ feedback if chosen: The tank does not collect sunlight._
- ◻️ to make it heavier  
  _↳ feedback if chosen: Weight is not the reason._
- ✅ to stop the heat escaping

Full working after a second miss:

> Insulation reduces heat loss.  
> So the answer is “to stop the heat escaping”.  

> Why is the hot-water tank insulated?

- ◻️ to let sunlight in  
  _↳ feedback if chosen: The tank does not collect sunlight._
- ◻️ to cool the water  
  _↳ feedback if chosen: The aim is to keep it hot._
- ✅ to stop the heat escaping
- ◻️ to make it heavier  
  _↳ feedback if chosen: Weight is not the reason._

Full working after a second miss:

> Insulation reduces heat loss.  
> So the answer is “to stop the heat escaping”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-17-part` · Lesson 17 · matching, level 1

Prompt: Match each part of a solar water heater to its job.

Pairs (4 shown each time):

- the black plate → **absorbs sunlight**
- the glass cover → **lets light in and keeps heat inside**
- the pipes → **carry water over the hot plate**
- the insulated tank → **stores hot water without losing heat**


Three generated variants:

> Match each part of a solar water heater to its job.

Right-hand side (shuffled): carry water over the hot plate · lets light in and keeps heat inside · stores hot water without losing heat · absorbs sunlight
- the glass cover → **lets light in and keeps heat inside**
- the black plate → **absorbs sunlight**
- the pipes → **carry water over the hot plate**
- the insulated tank → **stores hot water without losing heat**

Full working after a second miss:

> The right pairs are:  
> the glass cover → lets light in and keeps heat inside  
> the black plate → absorbs sunlight  
> the pipes → carry water over the hot plate  
> the insulated tank → stores hot water without losing heat  

> Match each part of a solar water heater to its job.

Right-hand side (shuffled): stores hot water without losing heat · lets light in and keeps heat inside · absorbs sunlight · carry water over the hot plate
- the glass cover → **lets light in and keeps heat inside**
- the insulated tank → **stores hot water without losing heat**
- the black plate → **absorbs sunlight**
- the pipes → **carry water over the hot plate**

Full working after a second miss:

> The right pairs are:  
> the glass cover → lets light in and keeps heat inside  
> the insulated tank → stores hot water without losing heat  
> the black plate → absorbs sunlight  
> the pipes → carry water over the hot plate  

> Match each part of a solar water heater to its job.

Right-hand side (shuffled): carry water over the hot plate · absorbs sunlight · lets light in and keeps heat inside · stores hot water without losing heat
- the insulated tank → **stores hot water without losing heat**
- the black plate → **absorbs sunlight**
- the pipes → **carry water over the hot plate**
- the glass cover → **lets light in and keeps heat inside**

Full working after a second miss:

> The right pairs are:  
> the insulated tank → stores hot water without losing heat  
> the black plate → absorbs sunlight  
> the pipes → carry water over the hot plate  
> the glass cover → lets light in and keeps heat inside  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-17-spot` · Lesson 17 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Black surfaces absorb heat radiation well.
- ✅ The glass cover keeps heat inside.
- ✅ Energy = power × time.
- ✅ Hot water rises into the tank.
- ❌ Shiny white plates absorb sunlight best.  
  _↳ Shiny or white surfaces reflect it; black absorbs._
- ❌ The tank should be thin metal with no insulation.  
  _↳ Insulation keeps the water hot._
- ❌ A solar water heater needs petrol.  
  _↳ It uses the sun's energy._


Three generated variants:

> Which statement is wrong?

- ◻️ Black surfaces absorb heat radiation well.
- ✅ The tank should be thin metal with no insulation.  
  _↳ explanation: Insulation keeps the water hot._
- ◻️ Hot water rises into the tank.
- ◻️ Energy = power × time.

Full working after a second miss:

> The wrong statement is “The tank should be thin metal with no insulation.”.  
> Insulation keeps the water hot.  

> Which statement is wrong?

- ◻️ Hot water rises into the tank.
- ✅ Shiny white plates absorb sunlight best.  
  _↳ explanation: Shiny or white surfaces reflect it; black absorbs._
- ◻️ Black surfaces absorb heat radiation well.
- ◻️ The glass cover keeps heat inside.

Full working after a second miss:

> The wrong statement is “Shiny white plates absorb sunlight best.”.  
> Shiny or white surfaces reflect it; black absorbs.  

> Which statement is wrong?

- ◻️ Black surfaces absorb heat radiation well.
- ◻️ The glass cover keeps heat inside.
- ◻️ Hot water rises into the tank.
- ✅ The tank should be thin metal with no insulation.  
  _↳ explanation: Insulation keeps the water hot._

Full working after a second miss:

> The wrong statement is “The tank should be thin metal with no insulation.”.  
> Insulation keeps the water hot.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-18-closed` · Lesson 18 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| When does a bulb in a simple circuit light up? | when the circuit is closed (complete) | when the switch is open · when a wire is cut · when there is no cell | An open switch breaks the circuit. · A cut wire breaks the circuit. · A source is needed. | Current needs a complete path. |
| What does a fuse do? | it melts and cuts the current if the current is too large | it makes the current larger · it stores electricity · it measures the voltage | It does the opposite. · A battery stores energy. · A voltmeter measures voltage. | It protects against too much current. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> When does a bulb in a simple circuit light up?

- ✅ when the circuit is closed (complete)
- ◻️ when there is no cell  
  _↳ feedback if chosen: A source is needed._
- ◻️ when a wire is cut  
  _↳ feedback if chosen: A cut wire breaks the circuit._
- ◻️ when the switch is open  
  _↳ feedback if chosen: An open switch breaks the circuit._

Full working after a second miss:

> Current needs a complete path.  
> So the answer is “when the circuit is closed (complete)”.  

> When does a bulb in a simple circuit light up?

- ✅ when the circuit is closed (complete)
- ◻️ when there is no cell  
  _↳ feedback if chosen: A source is needed._
- ◻️ when a wire is cut  
  _↳ feedback if chosen: A cut wire breaks the circuit._
- ◻️ when the switch is open  
  _↳ feedback if chosen: An open switch breaks the circuit._

Full working after a second miss:

> Current needs a complete path.  
> So the answer is “when the circuit is closed (complete)”.  

> What does a fuse do?

- ◻️ it measures the voltage  
  _↳ feedback if chosen: A voltmeter measures voltage._
- ◻️ it makes the current larger  
  _↳ feedback if chosen: It does the opposite._
- ✅ it melts and cuts the current if the current is too large
- ◻️ it stores electricity  
  _↳ feedback if chosen: A battery stores energy._

Full working after a second miss:

> It protects against too much current.  
> So the answer is “it melts and cuts the current if the current is too large”.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-18-spot` · Lesson 18 · spot the error, level 3

Prompt: Which safety rule is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Do not touch switches with wet hands.
- ✅ Do not overload sockets.
- ✅ Call an electrician to repair wiring.
- ✅ A fuse protects the circuit.
- ❌ Replace a fuse with a nail if it melts.  
  _↳ A nail does not melt: it removes the protection._
- ❌ Push a metal object into a socket to test it.  
  _↳ That can kill: never do it._
- ❌ Use a wet cloth to clean a lamp that is switched on.  
  _↳ Switch off and use a dry cloth._


Three generated variants:

> Which safety rule is wrong?

- ◻️ A fuse protects the circuit.
- ◻️ Call an electrician to repair wiring.
- ✅ Push a metal object into a socket to test it.  
  _↳ explanation: That can kill: never do it._
- ◻️ Do not touch switches with wet hands.

Full working after a second miss:

> The wrong statement is “Push a metal object into a socket to test it.”.  
> That can kill: never do it.  

> Which safety rule is wrong?

- ◻️ Call an electrician to repair wiring.
- ◻️ A fuse protects the circuit.
- ✅ Replace a fuse with a nail if it melts.  
  _↳ explanation: A nail does not melt: it removes the protection._
- ◻️ Do not touch switches with wet hands.

Full working after a second miss:

> The wrong statement is “Replace a fuse with a nail if it melts.”.  
> A nail does not melt: it removes the protection.  

> Which safety rule is wrong?

- ◻️ Do not overload sockets.
- ✅ Replace a fuse with a nail if it melts.  
  _↳ explanation: A nail does not melt: it removes the protection._
- ◻️ Call an electrician to repair wiring.
- ◻️ Do not touch switches with wet hands.

Full working after a second miss:

> The wrong statement is “Replace a fuse with a nail if it melts.”.  
> A nail does not melt: it removes the protection.  

Sources: heat-electricity (Temperature scales, expansion, conductors and insulators, effects of electric current (heating, lighting, magnetic, chemical), conduction)

### `p2-19-lum` · Lesson 19 · multiple choice, level 1

Prompt: Is {X.q} luminous or non-luminous?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| the moon | non-luminous | luminous · artificial · a star | It reflects sunlight. · It is natural, and not a source. · The moon is a satellite. | The moon reflects the sun's light. |
| a candle flame | luminous | non-luminous · natural · a mirror | The flame makes its own light. · A candle is man-made. · It is a flame. | A flame gives its own light. |
| a mirror | non-luminous | luminous · natural source · a star | It only reflects light. · It gives no light of its own. · It is not a star. | A mirror reflects light. |
| a firefly | luminous | non-luminous · artificial · a planet | It makes its own light. · It is a living insect. · It is an insect. | Fireflies make their own light. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is a mirror luminous or non-luminous?

- ◻️ a star  
  _↳ feedback if chosen: It is not a star._
- ◻️ natural source  
  _↳ feedback if chosen: It gives no light of its own._
- ✅ non-luminous
- ◻️ luminous  
  _↳ feedback if chosen: It only reflects light._

Full working after a second miss:

> A mirror reflects light.  
> So the answer is “non-luminous”.  

> Is a firefly luminous or non-luminous?

- ✅ luminous
- ◻️ non-luminous  
  _↳ feedback if chosen: It makes its own light._
- ◻️ a planet  
  _↳ feedback if chosen: It is an insect._
- ◻️ artificial  
  _↳ feedback if chosen: It is a living insect._

Full working after a second miss:

> Fireflies make their own light.  
> So the answer is “luminous”.  

> Is a firefly luminous or non-luminous?

- ◻️ a planet  
  _↳ feedback if chosen: It is an insect._
- ◻️ non-luminous  
  _↳ feedback if chosen: It makes its own light._
- ◻️ artificial  
  _↳ feedback if chosen: It is a living insect._
- ✅ luminous

Full working after a second miss:

> Fireflies make their own light.  
> So the answer is “luminous”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-19-nat` · Lesson 19 · multiple choice, level 1

Prompt: Is {X.q} a natural or an artificial source of light?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| lightning | natural | artificial · non-luminous · a receiver | Nobody makes lightning. · Lightning gives light. · It gives light. | Lightning is natural. |
| a torch | artificial | natural · non-luminous · a receiver | People make torches. · A torch gives light. · It gives light. | A torch is man-made. |
| the sun | natural | artificial · non-luminous · a receiver | Nobody made the sun. · The sun gives light. · It gives light. | The sun is natural. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is lightning a natural or an artificial source of light?

- ◻️ non-luminous  
  _↳ feedback if chosen: Lightning gives light._
- ✅ natural
- ◻️ artificial  
  _↳ feedback if chosen: Nobody makes lightning._
- ◻️ a receiver  
  _↳ feedback if chosen: It gives light._

Full working after a second miss:

> Lightning is natural.  
> So the answer is “natural”.  

> Is lightning a natural or an artificial source of light?

- ◻️ a receiver  
  _↳ feedback if chosen: It gives light._
- ◻️ non-luminous  
  _↳ feedback if chosen: Lightning gives light._
- ◻️ artificial  
  _↳ feedback if chosen: Nobody makes lightning._
- ✅ natural

Full working after a second miss:

> Lightning is natural.  
> So the answer is “natural”.  

> Is the sun a natural or an artificial source of light?

- ◻️ a receiver  
  _↳ feedback if chosen: It gives light._
- ◻️ artificial  
  _↳ feedback if chosen: Nobody made the sun._
- ✅ natural
- ◻️ non-luminous  
  _↳ feedback if chosen: The sun gives light._

Full working after a second miss:

> The sun is natural.  
> So the answer is “natural”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-19-led` · Lesson 19 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is an LED bulb better than a filament bulb? | it gives the same light with less electricity and little heat | it gives more heat · it uses more electricity · it needs petrol | It gives less heat. · It uses less. · It uses electricity. | LEDs waste less energy as heat. |
| Why can we see a book in a lit room? | it reflects light into our eyes | it makes its own light · our eyes send light to it · it is an LED | A book is non-luminous. · Light comes into our eyes. · It is not a lamp. | Non-luminous objects are seen by reflected light. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is an LED bulb better than a filament bulb?

- ◻️ it uses more electricity  
  _↳ feedback if chosen: It uses less._
- ✅ it gives the same light with less electricity and little heat
- ◻️ it gives more heat  
  _↳ feedback if chosen: It gives less heat._
- ◻️ it needs petrol  
  _↳ feedback if chosen: It uses electricity._

Full working after a second miss:

> LEDs waste less energy as heat.  
> So the answer is “it gives the same light with less electricity and little heat”.  

> Why can we see a book in a lit room?

- ◻️ it is an LED  
  _↳ feedback if chosen: It is not a lamp._
- ✅ it reflects light into our eyes
- ◻️ it makes its own light  
  _↳ feedback if chosen: A book is non-luminous._
- ◻️ our eyes send light to it  
  _↳ feedback if chosen: Light comes into our eyes._

Full working after a second miss:

> Non-luminous objects are seen by reflected light.  
> So the answer is “it reflects light into our eyes”.  

> Why is an LED bulb better than a filament bulb?

- ◻️ it uses more electricity  
  _↳ feedback if chosen: It uses less._
- ◻️ it needs petrol  
  _↳ feedback if chosen: It uses electricity._
- ✅ it gives the same light with less electricity and little heat
- ◻️ it gives more heat  
  _↳ feedback if chosen: It gives less heat._

Full working after a second miss:

> LEDs waste less energy as heat.  
> So the answer is “it gives the same light with less electricity and little heat”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-19-spot` · Lesson 19 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The sun is luminous.
- ✅ A torch is artificial.
- ✅ The moon reflects sunlight.
- ✅ LEDs save electricity.
- ❌ The moon makes its own light.  
  _↳ The moon reflects the sun's light._
- ❌ A mirror is a source of light.  
  _↳ A mirror only reflects light._
- ❌ Lightning is an artificial source.  
  _↳ Lightning is natural._


Three generated variants:

> Which statement is wrong?

- ◻️ LEDs save electricity.
- ◻️ A torch is artificial.
- ◻️ The moon reflects sunlight.
- ✅ A mirror is a source of light.  
  _↳ explanation: A mirror only reflects light._

Full working after a second miss:

> The wrong statement is “A mirror is a source of light.”.  
> A mirror only reflects light.  

> Which statement is wrong?

- ◻️ The sun is luminous.
- ✅ Lightning is an artificial source.  
  _↳ explanation: Lightning is natural._
- ◻️ A torch is artificial.
- ◻️ The moon reflects sunlight.

Full working after a second miss:

> The wrong statement is “Lightning is an artificial source.”.  
> Lightning is natural.  

> Which statement is wrong?

- ◻️ The moon reflects sunlight.
- ◻️ LEDs save electricity.
- ◻️ The sun is luminous.
- ✅ The moon makes its own light.  
  _↳ explanation: The moon reflects the sun's light._

Full working after a second miss:

> The wrong statement is “The moon makes its own light.”.  
> The moon reflects the sun's light.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-19-led-card` · Lesson 19 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is an LED bulb better than a filament bulb? | it gives the same light with less electricity and little heat | it gives more heat · it uses more electricity · it needs petrol | It gives less heat. · It uses less. · It uses electricity. | LEDs waste less energy as heat. |
| Why can we see a book in a lit room? | it reflects light into our eyes | it makes its own light · our eyes send light to it · it is an LED | A book is non-luminous. · Light comes into our eyes. · It is not a lamp. | Non-luminous objects are seen by reflected light. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why can we see a book in a lit room?

- ◻️ our eyes send light to it  
  _↳ feedback if chosen: Light comes into our eyes._
- ◻️ it makes its own light  
  _↳ feedback if chosen: A book is non-luminous._
- ◻️ it is an LED  
  _↳ feedback if chosen: It is not a lamp._
- ✅ it reflects light into our eyes

Full working after a second miss:

> Non-luminous objects are seen by reflected light.  
> So the answer is “it reflects light into our eyes”.  

> Why can we see a book in a lit room?

- ◻️ it makes its own light  
  _↳ feedback if chosen: A book is non-luminous._
- ✅ it reflects light into our eyes
- ◻️ our eyes send light to it  
  _↳ feedback if chosen: Light comes into our eyes._
- ◻️ it is an LED  
  _↳ feedback if chosen: It is not a lamp._

Full working after a second miss:

> Non-luminous objects are seen by reflected light.  
> So the answer is “it reflects light into our eyes”.  

> Why can we see a book in a lit room?

- ✅ it reflects light into our eyes
- ◻️ it is an LED  
  _↳ feedback if chosen: It is not a lamp._
- ◻️ it makes its own light  
  _↳ feedback if chosen: A book is non-luminous._
- ◻️ our eyes send light to it  
  _↳ feedback if chosen: Light comes into our eyes._

Full working after a second miss:

> Non-luminous objects are seen by reflected light.  
> So the answer is “it reflects light into our eyes”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-20-rec` · Lesson 20 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which of these is a light receiver? | a solar cell | a candle · a torch · the sun | A candle is a source. · A torch is a source. · The sun is a source. | A solar cell receives light and makes electricity. |
| Which of these is a light receiver? | the eye | a lamp · a fire · a star | A lamp is a source. · A fire is a source. · A star is a source. | The eye detects light. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which of these is a light receiver?

- ◻️ the sun  
  _↳ feedback if chosen: The sun is a source._
- ◻️ a candle  
  _↳ feedback if chosen: A candle is a source._
- ✅ a solar cell
- ◻️ a torch  
  _↳ feedback if chosen: A torch is a source._

Full working after a second miss:

> A solar cell receives light and makes electricity.  
> So the answer is “a solar cell”.  

> Which of these is a light receiver?

- ✅ a solar cell
- ◻️ the sun  
  _↳ feedback if chosen: The sun is a source._
- ◻️ a torch  
  _↳ feedback if chosen: A torch is a source._
- ◻️ a candle  
  _↳ feedback if chosen: A candle is a source._

Full working after a second miss:

> A solar cell receives light and makes electricity.  
> So the answer is “a solar cell”.  

> Which of these is a light receiver?

- ◻️ a fire  
  _↳ feedback if chosen: A fire is a source._
- ◻️ a lamp  
  _↳ feedback if chosen: A lamp is a source._
- ✅ the eye
- ◻️ a star  
  _↳ feedback if chosen: A star is a source._

Full working after a second miss:

> The eye detects light.  
> So the answer is “the eye”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-20-mat` · Lesson 20 · multiple choice, level 1

Prompt: Is {X.q} transparent, translucent or opaque?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| frosted glass | translucent | transparent · opaque · luminous | We cannot see clearly through it. · Some light passes. · It gives no light. | Some light passes, but not clearly. |
| clean water | transparent | translucent · opaque · luminous | We see clearly through it. · Light passes. · It gives no light. | We see clearly through clean water. |
| a metal sheet | opaque | transparent · translucent · luminous | No light passes. · No light passes. · It gives no light. | Metal stops light. |
| tracing paper | translucent | transparent · opaque · luminous | We cannot see clearly through it. · Some light passes. · It gives no light. | Tracing paper lets some light through. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is frosted glass transparent, translucent or opaque?

- ✅ translucent
- ◻️ luminous  
  _↳ feedback if chosen: It gives no light._
- ◻️ transparent  
  _↳ feedback if chosen: We cannot see clearly through it._
- ◻️ opaque  
  _↳ feedback if chosen: Some light passes._

Full working after a second miss:

> Some light passes, but not clearly.  
> So the answer is “translucent”.  

> Is clean water transparent, translucent or opaque?

- ◻️ luminous  
  _↳ feedback if chosen: It gives no light._
- ✅ transparent
- ◻️ translucent  
  _↳ feedback if chosen: We see clearly through it._
- ◻️ opaque  
  _↳ feedback if chosen: Light passes._

Full working after a second miss:

> We see clearly through clean water.  
> So the answer is “transparent”.  

> Is frosted glass transparent, translucent or opaque?

- ◻️ luminous  
  _↳ feedback if chosen: It gives no light._
- ◻️ transparent  
  _↳ feedback if chosen: We cannot see clearly through it._
- ◻️ opaque  
  _↳ feedback if chosen: Some light passes._
- ✅ translucent

Full working after a second miss:

> Some light passes, but not clearly.  
> So the answer is “translucent”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-20-shadow` · Lesson 20 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which object makes the darkest shadow? | a wooden board | a clear glass · a sheet of tracing paper · clean air | Light passes through clear glass. · Some light passes. · Air is transparent. | Opaque objects make dark shadows. |
| Why are bathroom windows often made of frosted glass? | they let light in but people cannot see in clearly | they stop all light · they are transparent · they make light | They let light in. · Clear glass is transparent. · Glass is not a source. | Translucent glass gives light and privacy. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why are bathroom windows often made of frosted glass?

- ◻️ they make light  
  _↳ feedback if chosen: Glass is not a source._
- ✅ they let light in but people cannot see in clearly
- ◻️ they are transparent  
  _↳ feedback if chosen: Clear glass is transparent._
- ◻️ they stop all light  
  _↳ feedback if chosen: They let light in._

Full working after a second miss:

> Translucent glass gives light and privacy.  
> So the answer is “they let light in but people cannot see in clearly”.  

> Which object makes the darkest shadow?

- ◻️ a sheet of tracing paper  
  _↳ feedback if chosen: Some light passes._
- ◻️ clean air  
  _↳ feedback if chosen: Air is transparent._
- ◻️ a clear glass  
  _↳ feedback if chosen: Light passes through clear glass._
- ✅ a wooden board

Full working after a second miss:

> Opaque objects make dark shadows.  
> So the answer is “a wooden board”.  

> Which object makes the darkest shadow?

- ◻️ a sheet of tracing paper  
  _↳ feedback if chosen: Some light passes._
- ◻️ clean air  
  _↳ feedback if chosen: Air is transparent._
- ✅ a wooden board
- ◻️ a clear glass  
  _↳ feedback if chosen: Light passes through clear glass._

Full working after a second miss:

> Opaque objects make dark shadows.  
> So the answer is “a wooden board”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-20-spot` · Lesson 20 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The eye is a light receiver.
- ✅ Clear glass is transparent.
- ✅ Wood is opaque.
- ✅ Opaque objects make shadows.
- ❌ Frosted glass is opaque.  
  _↳ It lets some light through: translucent._
- ❌ A candle is a light receiver.  
  _↳ A candle is a source._
- ❌ Transparent objects make dark shadows.  
  _↳ Light passes through them._


Three generated variants:

> Which statement is wrong?

- ✅ Transparent objects make dark shadows.  
  _↳ explanation: Light passes through them._
- ◻️ Opaque objects make shadows.
- ◻️ Wood is opaque.
- ◻️ The eye is a light receiver.

Full working after a second miss:

> The wrong statement is “Transparent objects make dark shadows.”.  
> Light passes through them.  

> Which statement is wrong?

- ◻️ Opaque objects make shadows.
- ◻️ Clear glass is transparent.
- ✅ Transparent objects make dark shadows.  
  _↳ explanation: Light passes through them._
- ◻️ Wood is opaque.

Full working after a second miss:

> The wrong statement is “Transparent objects make dark shadows.”.  
> Light passes through them.  

> Which statement is wrong?

- ◻️ The eye is a light receiver.
- ◻️ Clear glass is transparent.
- ✅ Frosted glass is opaque.  
  _↳ explanation: It lets some light through: translucent._
- ◻️ Wood is opaque.

Full working after a second miss:

> The wrong statement is “Frosted glass is opaque.”.  
> It lets some light through: translucent.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-20-shadow-card` · Lesson 20 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which object makes the darkest shadow? | a wooden board | a clear glass · a sheet of tracing paper · clean air | Light passes through clear glass. · Some light passes. · Air is transparent. | Opaque objects make dark shadows. |
| Why are bathroom windows often made of frosted glass? | they let light in but people cannot see in clearly | they stop all light · they are transparent · they make light | They let light in. · Clear glass is transparent. · Glass is not a source. | Translucent glass gives light and privacy. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why are bathroom windows often made of frosted glass?

- ◻️ they make light  
  _↳ feedback if chosen: Glass is not a source._
- ◻️ they stop all light  
  _↳ feedback if chosen: They let light in._
- ◻️ they are transparent  
  _↳ feedback if chosen: Clear glass is transparent._
- ✅ they let light in but people cannot see in clearly

Full working after a second miss:

> Translucent glass gives light and privacy.  
> So the answer is “they let light in but people cannot see in clearly”.  

> Why are bathroom windows often made of frosted glass?

- ◻️ they make light  
  _↳ feedback if chosen: Glass is not a source._
- ✅ they let light in but people cannot see in clearly
- ◻️ they stop all light  
  _↳ feedback if chosen: They let light in._
- ◻️ they are transparent  
  _↳ feedback if chosen: Clear glass is transparent._

Full working after a second miss:

> Translucent glass gives light and privacy.  
> So the answer is “they let light in but people cannot see in clearly”.  

> Which object makes the darkest shadow?

- ✅ a wooden board
- ◻️ a clear glass  
  _↳ feedback if chosen: Light passes through clear glass._
- ◻️ a sheet of tracing paper  
  _↳ feedback if chosen: Some light passes._
- ◻️ clean air  
  _↳ feedback if chosen: Air is transparent._

Full working after a second miss:

> Opaque objects make dark shadows.  
> So the answer is “a wooden board”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-21-beam` · Lesson 21 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do opaque objects make shadows? | light travels in straight lines and cannot bend round them | light is absorbed by the air · the object gives out darkness · light travels in curves | Air lets light through. · Darkness is the absence of light. · Light travels in straight lines. | Rectilinear propagation. |
| What is a ray of light? | the straight path that light follows, drawn with an arrow | a kind of shadow · a dark area · a light bulb | A shadow is where light does not reach. · That is a shadow. · That is a source. | Rays are drawn as straight lines with arrows. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is a ray of light?

- ✅ the straight path that light follows, drawn with an arrow
- ◻️ a kind of shadow  
  _↳ feedback if chosen: A shadow is where light does not reach._
- ◻️ a dark area  
  _↳ feedback if chosen: That is a shadow._
- ◻️ a light bulb  
  _↳ feedback if chosen: That is a source._

Full working after a second miss:

> Rays are drawn as straight lines with arrows.  
> So the answer is “the straight path that light follows, drawn with an arrow”.  

> Why do opaque objects make shadows?

- ◻️ light travels in curves  
  _↳ feedback if chosen: Light travels in straight lines._
- ◻️ the object gives out darkness  
  _↳ feedback if chosen: Darkness is the absence of light._
- ✅ light travels in straight lines and cannot bend round them
- ◻️ light is absorbed by the air  
  _↳ feedback if chosen: Air lets light through._

Full working after a second miss:

> Rectilinear propagation.  
> So the answer is “light travels in straight lines and cannot bend round them”.  

> Why do opaque objects make shadows?

- ✅ light travels in straight lines and cannot bend round them
- ◻️ light travels in curves  
  _↳ feedback if chosen: Light travels in straight lines._
- ◻️ light is absorbed by the air  
  _↳ feedback if chosen: Air lets light through._
- ◻️ the object gives out darkness  
  _↳ feedback if chosen: Darkness is the absence of light._

Full working after a second miss:

> Rectilinear propagation.  
> So the answer is “light travels in straight lines and cannot bend round them”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-21-kind` · Lesson 21 · multiple choice, level 1

Prompt: What kind of beam is this? {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Light spreading out from a candle flame | divergent | parallel · convergent · opaque | The rays spread out. · The rays do not meet. · Opaque is about materials. | Spreading rays make a divergent beam. |
| Sunlight reaching the Earth | parallel | divergent · convergent · translucent | The sun is very far: its rays are almost parallel. · The rays do not meet. · Translucent is about materials. | Distant sources give parallel beams. |
| Light coming together after a magnifying glass | convergent | parallel · divergent · opaque | The rays meet. · The rays come together. · Opaque is about materials. | Rays coming together make a convergent beam. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What kind of beam is this? Light coming together after a magnifying glass

- ◻️ opaque  
  _↳ feedback if chosen: Opaque is about materials._
- ◻️ divergent  
  _↳ feedback if chosen: The rays come together._
- ◻️ parallel  
  _↳ feedback if chosen: The rays meet._
- ✅ convergent

Full working after a second miss:

> Rays coming together make a convergent beam.  
> So the answer is “convergent”.  

> What kind of beam is this? Light coming together after a magnifying glass

- ◻️ parallel  
  _↳ feedback if chosen: The rays meet._
- ◻️ opaque  
  _↳ feedback if chosen: Opaque is about materials._
- ◻️ divergent  
  _↳ feedback if chosen: The rays come together._
- ✅ convergent

Full working after a second miss:

> Rays coming together make a convergent beam.  
> So the answer is “convergent”.  

> What kind of beam is this? Sunlight reaching the Earth

- ◻️ translucent  
  _↳ feedback if chosen: Translucent is about materials._
- ◻️ divergent  
  _↳ feedback if chosen: The sun is very far: its rays are almost parallel._
- ◻️ convergent  
  _↳ feedback if chosen: The rays do not meet._
- ✅ parallel

Full working after a second miss:

> Distant sources give parallel beams.  
> So the answer is “parallel”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-21-spot` · Lesson 21 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Light travels in straight lines.
- ✅ Sunlight reaching the Earth forms a parallel beam.
- ✅ A large source gives an umbra and a penumbra.
- ✅ Opaque objects make shadows.
- ❌ A shadow is light coming out of the object.  
  _↳ A shadow is a region light cannot reach._
- ❌ With a point source, the shadow is smaller than the object.  
  _↳ It is bigger when the screen is farther than the object._
- ❌ Light bends round opaque objects to fill the shadow.  
  _↳ Light travels in straight lines._


Three generated variants:

> Which statement is wrong?

- ◻️ Light travels in straight lines.
- ✅ With a point source, the shadow is smaller than the object.  
  _↳ explanation: It is bigger when the screen is farther than the object._
- ◻️ Opaque objects make shadows.
- ◻️ A large source gives an umbra and a penumbra.

Full working after a second miss:

> The wrong statement is “With a point source, the shadow is smaller than the object.”.  
> It is bigger when the screen is farther than the object.  

> Which statement is wrong?

- ✅ A shadow is light coming out of the object.  
  _↳ explanation: A shadow is a region light cannot reach._
- ◻️ Sunlight reaching the Earth forms a parallel beam.
- ◻️ Light travels in straight lines.
- ◻️ Opaque objects make shadows.

Full working after a second miss:

> The wrong statement is “A shadow is light coming out of the object.”.  
> A shadow is a region light cannot reach.  

> Which statement is wrong?

- ✅ A shadow is light coming out of the object.  
  _↳ explanation: A shadow is a region light cannot reach._
- ◻️ Opaque objects make shadows.
- ◻️ A large source gives an umbra and a penumbra.
- ◻️ Sunlight reaching the Earth forms a parallel beam.

Full working after a second miss:

> The wrong statement is “A shadow is light coming out of the object.”.  
> A shadow is a region light cannot reach.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-22-chain` · Lesson 22 · matching, level 1

Prompt: Match each device to its energy change.

Pairs (4 shown each time):

- a torch → **chemical energy (battery) → electrical energy → light (and heat)**
- a hydroelectric dam → **kinetic energy of water → electrical energy**
- a person climbing stairs → **chemical energy (food) → kinetic energy → potential energy**
- a solar panel → **light energy → electrical energy**
- a radio → **electrical energy → sound energy**


Three generated variants:

> Match each device to its energy change.

Right-hand side (shuffled): chemical energy (battery) → electrical energy → light (and heat) · kinetic energy of water → electrical energy · electrical energy → sound energy · chemical energy (food) → kinetic energy → potential energy
- a person climbing stairs → **chemical energy (food) → kinetic energy → potential energy**
- a torch → **chemical energy (battery) → electrical energy → light (and heat)**
- a radio → **electrical energy → sound energy**
- a hydroelectric dam → **kinetic energy of water → electrical energy**

Full working after a second miss:

> The right pairs are:  
> a person climbing stairs → chemical energy (food) → kinetic energy → potential energy  
> a torch → chemical energy (battery) → electrical energy → light (and heat)  
> a radio → electrical energy → sound energy  
> a hydroelectric dam → kinetic energy of water → electrical energy  

> Match each device to its energy change.

Right-hand side (shuffled): chemical energy (battery) → electrical energy → light (and heat) · kinetic energy of water → electrical energy · electrical energy → sound energy · chemical energy (food) → kinetic energy → potential energy
- a radio → **electrical energy → sound energy**
- a person climbing stairs → **chemical energy (food) → kinetic energy → potential energy**
- a torch → **chemical energy (battery) → electrical energy → light (and heat)**
- a hydroelectric dam → **kinetic energy of water → electrical energy**

Full working after a second miss:

> The right pairs are:  
> a radio → electrical energy → sound energy  
> a person climbing stairs → chemical energy (food) → kinetic energy → potential energy  
> a torch → chemical energy (battery) → electrical energy → light (and heat)  
> a hydroelectric dam → kinetic energy of water → electrical energy  

> Match each device to its energy change.

Right-hand side (shuffled): chemical energy (food) → kinetic energy → potential energy · chemical energy (battery) → electrical energy → light (and heat) · light energy → electrical energy · kinetic energy of water → electrical energy
- a torch → **chemical energy (battery) → electrical energy → light (and heat)**
- a person climbing stairs → **chemical energy (food) → kinetic energy → potential energy**
- a solar panel → **light energy → electrical energy**
- a hydroelectric dam → **kinetic energy of water → electrical energy**

Full working after a second miss:

> The right pairs are:  
> a torch → chemical energy (battery) → electrical energy → light (and heat)  
> a person climbing stairs → chemical energy (food) → kinetic energy → potential energy  
> a solar panel → light energy → electrical energy  
> a hydroelectric dam → kinetic energy of water → electrical energy  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-22-form` · Lesson 22 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What form of energy is stored in a battery? | chemical energy | sound energy · light energy · kinetic energy | Sound is produced, not stored. · Light is produced, not stored. · Kinetic energy is movement. | Batteries store chemical energy. |
| What form of energy does a moving car have? | kinetic energy | potential energy · nuclear energy · light energy | Potential energy is stored by height. · That is in atoms. · Light is from lamps. | Moving things have kinetic energy. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What form of energy is stored in a battery?

- ✅ chemical energy
- ◻️ light energy  
  _↳ feedback if chosen: Light is produced, not stored._
- ◻️ kinetic energy  
  _↳ feedback if chosen: Kinetic energy is movement._
- ◻️ sound energy  
  _↳ feedback if chosen: Sound is produced, not stored._

Full working after a second miss:

> Batteries store chemical energy.  
> So the answer is “chemical energy”.  

> What form of energy is stored in a battery?

- ◻️ light energy  
  _↳ feedback if chosen: Light is produced, not stored._
- ◻️ sound energy  
  _↳ feedback if chosen: Sound is produced, not stored._
- ✅ chemical energy
- ◻️ kinetic energy  
  _↳ feedback if chosen: Kinetic energy is movement._

Full working after a second miss:

> Batteries store chemical energy.  
> So the answer is “chemical energy”.  

> What form of energy does a moving car have?

- ◻️ potential energy  
  _↳ feedback if chosen: Potential energy is stored by height._
- ◻️ nuclear energy  
  _↳ feedback if chosen: That is in atoms._
- ◻️ light energy  
  _↳ feedback if chosen: Light is from lamps._
- ✅ kinetic energy

Full working after a second miss:

> Moving things have kinetic energy.  
> So the answer is “kinetic energy”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-22-waste` · Lesson 22 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does an electric iron get hot? | it changes electrical energy into heat on purpose | it creates new energy · it changes heat into electricity · it stores potential energy | Energy is not created. · It is the opposite. · It does not store height energy. | Electrical → heat. |
| Which is the correct chain for a hydroelectric dam? | potential energy of water → kinetic energy → electrical energy | electrical → kinetic → potential · light → electrical · chemical → sound | That is backwards. · That is a solar panel. · That does not fit a dam. | Falling water turns turbines. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does an electric iron get hot?

- ✅ it changes electrical energy into heat on purpose
- ◻️ it creates new energy  
  _↳ feedback if chosen: Energy is not created._
- ◻️ it changes heat into electricity  
  _↳ feedback if chosen: It is the opposite._
- ◻️ it stores potential energy  
  _↳ feedback if chosen: It does not store height energy._

Full working after a second miss:

> Electrical → heat.  
> So the answer is “it changes electrical energy into heat on purpose”.  

> Which is the correct chain for a hydroelectric dam?

- ◻️ light → electrical  
  _↳ feedback if chosen: That is a solar panel._
- ◻️ electrical → kinetic → potential  
  _↳ feedback if chosen: That is backwards._
- ✅ potential energy of water → kinetic energy → electrical energy
- ◻️ chemical → sound  
  _↳ feedback if chosen: That does not fit a dam._

Full working after a second miss:

> Falling water turns turbines.  
> So the answer is “potential energy of water → kinetic energy → electrical energy”.  

> Which is the correct chain for a hydroelectric dam?

- ◻️ chemical → sound  
  _↳ feedback if chosen: That does not fit a dam._
- ◻️ electrical → kinetic → potential  
  _↳ feedback if chosen: That is backwards._
- ◻️ light → electrical  
  _↳ feedback if chosen: That is a solar panel._
- ✅ potential energy of water → kinetic energy → electrical energy

Full working after a second miss:

> Falling water turns turbines.  
> So the answer is “potential energy of water → kinetic energy → electrical energy”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-22-spot` · Lesson 22 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Energy changes from one form to another.
- ✅ Food stores chemical energy.
- ✅ A solar panel changes light into electricity.
- ✅ Some energy is wasted as heat.
- ❌ A torch creates new energy from nothing.  
  _↳ Energy is not created: the battery's chemical energy changes form._
- ❌ A radio changes sound into electricity.  
  _↳ A radio changes electrical energy into sound._
- ❌ Energy can be destroyed completely.  
  _↳ Energy is conserved; it only changes form._


Three generated variants:

> Which statement is wrong?

- ◻️ Energy changes from one form to another.
- ◻️ A solar panel changes light into electricity.
- ✅ A radio changes sound into electricity.  
  _↳ explanation: A radio changes electrical energy into sound._
- ◻️ Some energy is wasted as heat.

Full working after a second miss:

> The wrong statement is “A radio changes sound into electricity.”.  
> A radio changes electrical energy into sound.  

> Which statement is wrong?

- ◻️ A solar panel changes light into electricity.
- ✅ A torch creates new energy from nothing.  
  _↳ explanation: Energy is not created: the battery's chemical energy changes form._
- ◻️ Energy changes from one form to another.
- ◻️ Some energy is wasted as heat.

Full working after a second miss:

> The wrong statement is “A torch creates new energy from nothing.”.  
> Energy is not created: the battery's chemical energy changes form.  

> Which statement is wrong?

- ◻️ A solar panel changes light into electricity.
- ◻️ Food stores chemical energy.
- ✅ Energy can be destroyed completely.  
  _↳ explanation: Energy is conserved; it only changes form._
- ◻️ Energy changes from one form to another.

Full working after a second miss:

> The wrong statement is “Energy can be destroyed completely.”.  
> Energy is conserved; it only changes form.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-22-waste-card` · Lesson 22 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does an electric iron get hot? | it changes electrical energy into heat on purpose | it creates new energy · it changes heat into electricity · it stores potential energy | Energy is not created. · It is the opposite. · It does not store height energy. | Electrical → heat. |
| Which is the correct chain for a hydroelectric dam? | potential energy of water → kinetic energy → electrical energy | electrical → kinetic → potential · light → electrical · chemical → sound | That is backwards. · That is a solar panel. · That does not fit a dam. | Falling water turns turbines. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does an electric iron get hot?

- ◻️ it stores potential energy  
  _↳ feedback if chosen: It does not store height energy._
- ✅ it changes electrical energy into heat on purpose
- ◻️ it changes heat into electricity  
  _↳ feedback if chosen: It is the opposite._
- ◻️ it creates new energy  
  _↳ feedback if chosen: Energy is not created._

Full working after a second miss:

> Electrical → heat.  
> So the answer is “it changes electrical energy into heat on purpose”.  

> Which is the correct chain for a hydroelectric dam?

- ✅ potential energy of water → kinetic energy → electrical energy
- ◻️ chemical → sound  
  _↳ feedback if chosen: That does not fit a dam._
- ◻️ electrical → kinetic → potential  
  _↳ feedback if chosen: That is backwards._
- ◻️ light → electrical  
  _↳ feedback if chosen: That is a solar panel._

Full working after a second miss:

> Falling water turns turbines.  
> So the answer is “potential energy of water → kinetic energy → electrical energy”.  

> Why does an electric iron get hot?

- ◻️ it changes heat into electricity  
  _↳ feedback if chosen: It is the opposite._
- ◻️ it creates new energy  
  _↳ feedback if chosen: Energy is not created._
- ◻️ it stores potential energy  
  _↳ feedback if chosen: It does not store height energy._
- ✅ it changes electrical energy into heat on purpose

Full working after a second miss:

> Electrical → heat.  
> So the answer is “it changes electrical energy into heat on purpose”.  

Sources: energy-sources (Renewable and non-renewable energy sources; fossil fuels; hydroelectric power in Cameroon (Edéa and Song Loulou dams))

### `p2-23-blood` · Lesson 23 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In a blood pressure of 120/80 mmHg, what does 120 show? | the pressure when the heart contracts (systolic) | the pressure when the heart relaxes · the pulse rate · the body temperature | That is the lower number, 80. · The pulse is counted separately. · Temperature is in °C. | The higher number is systolic. |
| Which habit helps to prevent high blood pressure? | eating less salt and exercising regularly | eating a lot of salt · smoking · never exercising | Salt raises blood pressure. · Smoking raises the risk. · Exercise helps. | Less salt and more exercise lower the risk. |
| What instrument measures blood pressure? | a sphygmomanometer | a thermometer · a barometer only for weather · a ruler | It measures temperature. · A barometer measures air pressure. · A ruler measures length. | The doctor uses a sphygmomanometer. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In a blood pressure of 120/80 mmHg, what does 120 show?

- ◻️ the pressure when the heart relaxes  
  _↳ feedback if chosen: That is the lower number, 80._
- ◻️ the pulse rate  
  _↳ feedback if chosen: The pulse is counted separately._
- ◻️ the body temperature  
  _↳ feedback if chosen: Temperature is in °C._
- ✅ the pressure when the heart contracts (systolic)

Full working after a second miss:

> The higher number is systolic.  
> So the answer is “the pressure when the heart contracts (systolic)”.  

> In a blood pressure of 120/80 mmHg, what does 120 show?

- ◻️ the pressure when the heart relaxes  
  _↳ feedback if chosen: That is the lower number, 80._
- ✅ the pressure when the heart contracts (systolic)
- ◻️ the body temperature  
  _↳ feedback if chosen: Temperature is in °C._
- ◻️ the pulse rate  
  _↳ feedback if chosen: The pulse is counted separately._

Full working after a second miss:

> The higher number is systolic.  
> So the answer is “the pressure when the heart contracts (systolic)”.  

> Which habit helps to prevent high blood pressure?

- ✅ eating less salt and exercising regularly
- ◻️ eating a lot of salt  
  _↳ feedback if chosen: Salt raises blood pressure._
- ◻️ never exercising  
  _↳ feedback if chosen: Exercise helps._
- ◻️ smoking  
  _↳ feedback if chosen: Smoking raises the risk._

Full working after a second miss:

> Less salt and more exercise lower the risk.  
> So the answer is “eating less salt and exercising regularly”.  

Sources: pressure-health (Pressure = force/area, pressure in liquids p = ρgh, blood pressure (systolic/diastolic, mmHg), pulse rate, exercise and health (220 − age as a common guide only))

### `p2-23-spot` · Lesson 23 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Pressure = force ÷ area.
- ✅ Pressure in a liquid increases with depth.
- ✅ Blood pressure is caused by the pumping of the heart.
- ✅ Too much salt can raise blood pressure.
- ❌ Pressure in a liquid is the same at every depth.  
  _↳ It increases with depth._
- ❌ High blood pressure is always harmless.  
  _↳ It is dangerous for the heart and brain._
- ❌ Blood pressure is measured in kilograms.  
  _↳ It is measured in mmHg._


Three generated variants:

> Which statement is wrong?

- ◻️ Blood pressure is caused by the pumping of the heart.
- ◻️ Pressure = force ÷ area.
- ✅ High blood pressure is always harmless.  
  _↳ explanation: It is dangerous for the heart and brain._
- ◻️ Too much salt can raise blood pressure.

Full working after a second miss:

> The wrong statement is “High blood pressure is always harmless.”.  
> It is dangerous for the heart and brain.  

> Which statement is wrong?

- ◻️ Pressure = force ÷ area.
- ◻️ Too much salt can raise blood pressure.
- ◻️ Pressure in a liquid increases with depth.
- ✅ Pressure in a liquid is the same at every depth.  
  _↳ explanation: It increases with depth._

Full working after a second miss:

> The wrong statement is “Pressure in a liquid is the same at every depth.”.  
> It increases with depth.  

> Which statement is wrong?

- ◻️ Pressure in a liquid increases with depth.
- ✅ High blood pressure is always harmless.  
  _↳ explanation: It is dangerous for the heart and brain._
- ◻️ Too much salt can raise blood pressure.
- ◻️ Pressure = force ÷ area.

Full working after a second miss:

> The wrong statement is “High blood pressure is always harmless.”.  
> It is dangerous for the heart and brain.  

Sources: pressure-health (Pressure = force/area, pressure in liquids p = ρgh, blood pressure (systolic/diastolic, mmHg), pulse rate, exercise and health (220 − age as a common guide only))

### `p2-23-blood-card` · Lesson 23 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| In a blood pressure of 120/80 mmHg, what does 120 show? | the pressure when the heart contracts (systolic) | the pressure when the heart relaxes · the pulse rate · the body temperature | That is the lower number, 80. · The pulse is counted separately. · Temperature is in °C. | The higher number is systolic. |
| Which habit helps to prevent high blood pressure? | eating less salt and exercising regularly | eating a lot of salt · smoking · never exercising | Salt raises blood pressure. · Smoking raises the risk. · Exercise helps. | Less salt and more exercise lower the risk. |
| What instrument measures blood pressure? | a sphygmomanometer | a thermometer · a barometer only for weather · a ruler | It measures temperature. · A barometer measures air pressure. · A ruler measures length. | The doctor uses a sphygmomanometer. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In a blood pressure of 120/80 mmHg, what does 120 show?

- ◻️ the body temperature  
  _↳ feedback if chosen: Temperature is in °C._
- ✅ the pressure when the heart contracts (systolic)
- ◻️ the pulse rate  
  _↳ feedback if chosen: The pulse is counted separately._
- ◻️ the pressure when the heart relaxes  
  _↳ feedback if chosen: That is the lower number, 80._

Full working after a second miss:

> The higher number is systolic.  
> So the answer is “the pressure when the heart contracts (systolic)”.  

> What instrument measures blood pressure?

- ◻️ a thermometer  
  _↳ feedback if chosen: It measures temperature._
- ◻️ a barometer only for weather  
  _↳ feedback if chosen: A barometer measures air pressure._
- ◻️ a ruler  
  _↳ feedback if chosen: A ruler measures length._
- ✅ a sphygmomanometer

Full working after a second miss:

> The doctor uses a sphygmomanometer.  
> So the answer is “a sphygmomanometer”.  

> What instrument measures blood pressure?

- ✅ a sphygmomanometer
- ◻️ a thermometer  
  _↳ feedback if chosen: It measures temperature._
- ◻️ a ruler  
  _↳ feedback if chosen: A ruler measures length._
- ◻️ a barometer only for weather  
  _↳ feedback if chosen: A barometer measures air pressure._

Full working after a second miss:

> The doctor uses a sphygmomanometer.  
> So the answer is “a sphygmomanometer”.  

Sources: pressure-health (Pressure = force/area, pressure in liquids p = ρgh, blood pressure (systolic/diastolic, mmHg), pulse rate, exercise and health (220 − age as a common guide only))

### `p2-24-why` · Lesson 24 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does the heart beat faster during exercise? | the muscles need more oxygen and energy | the heart is tired · the blood becomes cold · the lungs stop working | It beats faster, not slower. · Body temperature rises. · We breathe faster. | More oxygen is carried to the muscles. |
| What is a benefit of regular exercise? | a stronger heart and lower blood pressure | higher blood pressure · weaker muscles · worse sleep | Exercise lowers it. · Exercise strengthens muscles. · Exercise improves sleep. | Exercise keeps the heart healthy. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is a benefit of regular exercise?

- ◻️ worse sleep  
  _↳ feedback if chosen: Exercise improves sleep._
- ◻️ higher blood pressure  
  _↳ feedback if chosen: Exercise lowers it._
- ◻️ weaker muscles  
  _↳ feedback if chosen: Exercise strengthens muscles._
- ✅ a stronger heart and lower blood pressure

Full working after a second miss:

> Exercise keeps the heart healthy.  
> So the answer is “a stronger heart and lower blood pressure”.  

> What is a benefit of regular exercise?

- ✅ a stronger heart and lower blood pressure
- ◻️ worse sleep  
  _↳ feedback if chosen: Exercise improves sleep._
- ◻️ higher blood pressure  
  _↳ feedback if chosen: Exercise lowers it._
- ◻️ weaker muscles  
  _↳ feedback if chosen: Exercise strengthens muscles._

Full working after a second miss:

> Exercise keeps the heart healthy.  
> So the answer is “a stronger heart and lower blood pressure”.  

> Why does the heart beat faster during exercise?

- ◻️ the lungs stop working  
  _↳ feedback if chosen: We breathe faster._
- ◻️ the blood becomes cold  
  _↳ feedback if chosen: Body temperature rises._
- ◻️ the heart is tired  
  _↳ feedback if chosen: It beats faster, not slower._
- ✅ the muscles need more oxygen and energy

Full working after a second miss:

> More oxygen is carried to the muscles.  
> So the answer is “the muscles need more oxygen and energy”.  

Sources: pressure-health (Pressure = force/area, pressure in liquids p = ρgh, blood pressure (systolic/diastolic, mmHg), pulse rate, exercise and health (220 − age as a common guide only))

### `p2-24-safe` · Lesson 24 · spot the error, level 3

Prompt: Which advice is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Warm up before running.
- ✅ Drink water during long exercise.
- ✅ Rest after hard training.
- ✅ Stretch after exercise.
- ❌ Run as hard as possible without warming up.  
  _↳ Cold muscles tear easily: warm up first._
- ❌ Never drink water during sport.  
  _↳ Drink water to replace sweat._
- ❌ Train every day without any rest.  
  _↳ Muscles need rest to recover._


Three generated variants:

> Which advice is wrong?

- ◻️ Rest after hard training.
- ✅ Run as hard as possible without warming up.  
  _↳ explanation: Cold muscles tear easily: warm up first._
- ◻️ Stretch after exercise.
- ◻️ Drink water during long exercise.

Full working after a second miss:

> The wrong statement is “Run as hard as possible without warming up.”.  
> Cold muscles tear easily: warm up first.  

> Which advice is wrong?

- ◻️ Stretch after exercise.
- ◻️ Drink water during long exercise.
- ✅ Train every day without any rest.  
  _↳ explanation: Muscles need rest to recover._
- ◻️ Warm up before running.

Full working after a second miss:

> The wrong statement is “Train every day without any rest.”.  
> Muscles need rest to recover.  

> Which advice is wrong?

- ◻️ Drink water during long exercise.
- ◻️ Stretch after exercise.
- ◻️ Warm up before running.
- ✅ Run as hard as possible without warming up.  
  _↳ explanation: Cold muscles tear easily: warm up first._

Full working after a second miss:

> The wrong statement is “Run as hard as possible without warming up.”.  
> Cold muscles tear easily: warm up first.  

Sources: pressure-health (Pressure = force/area, pressure in liquids p = ρgh, blood pressure (systolic/diastolic, mmHg), pulse rate, exercise and health (220 − age as a common guide only))

### `p2-24-safe-card` · Lesson 24 · spot the error, level 1

Prompt: Which advice is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Warm up before running.
- ✅ Drink water during long exercise.
- ✅ Rest after hard training.
- ✅ Stretch after exercise.
- ❌ Run as hard as possible without warming up.  
  _↳ Cold muscles tear easily: warm up first._
- ❌ Never drink water during sport.  
  _↳ Drink water to replace sweat._
- ❌ Train every day without any rest.  
  _↳ Muscles need rest to recover._


Three generated variants:

> Which advice is wrong?

- ✅ Never drink water during sport.  
  _↳ explanation: Drink water to replace sweat._
- ◻️ Drink water during long exercise.
- ◻️ Stretch after exercise.
- ◻️ Rest after hard training.

Full working after a second miss:

> The wrong statement is “Never drink water during sport.”.  
> Drink water to replace sweat.  

> Which advice is wrong?

- ✅ Run as hard as possible without warming up.  
  _↳ explanation: Cold muscles tear easily: warm up first._
- ◻️ Stretch after exercise.
- ◻️ Warm up before running.
- ◻️ Drink water during long exercise.

Full working after a second miss:

> The wrong statement is “Run as hard as possible without warming up.”.  
> Cold muscles tear easily: warm up first.  

> Which advice is wrong?

- ◻️ Warm up before running.
- ✅ Run as hard as possible without warming up.  
  _↳ explanation: Cold muscles tear easily: warm up first._
- ◻️ Stretch after exercise.
- ◻️ Rest after hard training.

Full working after a second miss:

> The wrong statement is “Run as hard as possible without warming up.”.  
> Cold muscles tear easily: warm up first.  

Sources: pressure-health (Pressure = force/area, pressure in liquids p = ρgh, blood pressure (systolic/diastolic, mmHg), pulse rate, exercise and health (220 − age as a common guide only))

### `p2-25-eye` · Lesson 25 · matching, level 1

Prompt: Match each part of the eye to its job.

Pairs (4 shown each time):

- the lens → **focuses light on the retina**
- the retina → **receives the image**
- the optic nerve → **carries signals to the brain**
- the pupil → **the hole that lets light in**
- the iris → **controls the size of the pupil**


Three generated variants:

> Match each part of the eye to its job.

Right-hand side (shuffled): focuses light on the retina · receives the image · the hole that lets light in · controls the size of the pupil
- the iris → **controls the size of the pupil**
- the lens → **focuses light on the retina**
- the retina → **receives the image**
- the pupil → **the hole that lets light in**

Full working after a second miss:

> The right pairs are:  
> the iris → controls the size of the pupil  
> the lens → focuses light on the retina  
> the retina → receives the image  
> the pupil → the hole that lets light in  

> Match each part of the eye to its job.

Right-hand side (shuffled): controls the size of the pupil · focuses light on the retina · carries signals to the brain · the hole that lets light in
- the iris → **controls the size of the pupil**
- the lens → **focuses light on the retina**
- the pupil → **the hole that lets light in**
- the optic nerve → **carries signals to the brain**

Full working after a second miss:

> The right pairs are:  
> the iris → controls the size of the pupil  
> the lens → focuses light on the retina  
> the pupil → the hole that lets light in  
> the optic nerve → carries signals to the brain  

> Match each part of the eye to its job.

Right-hand side (shuffled): controls the size of the pupil · carries signals to the brain · focuses light on the retina · the hole that lets light in
- the iris → **controls the size of the pupil**
- the pupil → **the hole that lets light in**
- the lens → **focuses light on the retina**
- the optic nerve → **carries signals to the brain**

Full working after a second miss:

> The right pairs are:  
> the iris → controls the size of the pupil  
> the pupil → the hole that lets light in  
> the lens → focuses light on the retina  
> the optic nerve → carries signals to the brain  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-25-defect` · Lesson 25 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| A pupil sees near things clearly but cannot read the board from the back of the class. What defect has he? | short sight (myopia) | long sight (hypermetropia) · colour blindness · no defect | Long sight blurs near things. · That is about colours. · He cannot see far. | Far objects are blurred: short sight. |
| Which lens corrects short sight? | a diverging (concave) lens | a converging (convex) lens · a flat glass · a mirror | That corrects long sight. · It does not change the rays. · A mirror is not worn as glasses. | A diverging lens moves the image back onto the retina. |
| Which lens corrects long sight? | a converging (convex) lens | a diverging (concave) lens · a flat glass · a prism | That corrects short sight. · It does not change the rays. · A prism is not worn as glasses. | A converging lens brings the image forward onto the retina. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which lens corrects short sight?

- ◻️ a flat glass  
  _↳ feedback if chosen: It does not change the rays._
- ◻️ a converging (convex) lens  
  _↳ feedback if chosen: That corrects long sight._
- ✅ a diverging (concave) lens
- ◻️ a mirror  
  _↳ feedback if chosen: A mirror is not worn as glasses._

Full working after a second miss:

> A diverging lens moves the image back onto the retina.  
> So the answer is “a diverging (concave) lens”.  

> A pupil sees near things clearly but cannot read the board from the back of the class. What defect has he?

- ◻️ long sight (hypermetropia)  
  _↳ feedback if chosen: Long sight blurs near things._
- ◻️ no defect  
  _↳ feedback if chosen: He cannot see far._
- ◻️ colour blindness  
  _↳ feedback if chosen: That is about colours._
- ✅ short sight (myopia)

Full working after a second miss:

> Far objects are blurred: short sight.  
> So the answer is “short sight (myopia)”.  

> Which lens corrects short sight?

- ◻️ a flat glass  
  _↳ feedback if chosen: It does not change the rays._
- ◻️ a mirror  
  _↳ feedback if chosen: A mirror is not worn as glasses._
- ◻️ a converging (convex) lens  
  _↳ feedback if chosen: That corrects long sight._
- ✅ a diverging (concave) lens

Full working after a second miss:

> A diverging lens moves the image back onto the retina.  
> So the answer is “a diverging (concave) lens”.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-25-spot` · Lesson 25 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The retina receives the image.
- ✅ Short sight is corrected with a diverging lens.
- ✅ A converging lens is thicker in the middle.
- ✅ The optic nerve carries signals to the brain.
- ❌ Long sight is corrected with a diverging lens.  
  _↳ Long sight needs a converging lens._
- ❌ The image of a short-sighted eye forms behind the retina.  
  _↳ It forms in front of the retina._
- ❌ A diverging lens brings rays together.  
  _↳ A diverging lens spreads rays out._


Three generated variants:

> Which statement is wrong?

- ◻️ The retina receives the image.
- ◻️ A converging lens is thicker in the middle.
- ◻️ The optic nerve carries signals to the brain.
- ✅ Long sight is corrected with a diverging lens.  
  _↳ explanation: Long sight needs a converging lens._

Full working after a second miss:

> The wrong statement is “Long sight is corrected with a diverging lens.”.  
> Long sight needs a converging lens.  

> Which statement is wrong?

- ◻️ A converging lens is thicker in the middle.
- ✅ A diverging lens brings rays together.  
  _↳ explanation: A diverging lens spreads rays out._
- ◻️ The retina receives the image.
- ◻️ Short sight is corrected with a diverging lens.

Full working after a second miss:

> The wrong statement is “A diverging lens brings rays together.”.  
> A diverging lens spreads rays out.  

> Which statement is wrong?

- ◻️ The optic nerve carries signals to the brain.
- ◻️ Short sight is corrected with a diverging lens.
- ✅ The image of a short-sighted eye forms behind the retina.  
  _↳ explanation: It forms in front of the retina._
- ◻️ A converging lens is thicker in the middle.

Full working after a second miss:

> The wrong statement is “The image of a short-sighted eye forms behind the retina.”.  
> It forms in front of the retina.  

Sources: light (Sources and receivers of light, transparent/translucent/opaque, rays and beams, shadows (size by similar triangles), the eye, lenses, short and long sight, lens power P = 100/f(cm))

### `p2-26-def` · Lesson 26 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does sustainable management mean? | using resources so that they remain for future generations | using everything now · never using any resource · selling all the forests | That leaves nothing for the future. · We need resources to live. · That destroys the forests. | Use, but keep enough for the future. |
| Which practice is sustainable? | replanting trees after cutting | bush fires · overfishing · dumping waste in rivers | They destroy plants and soil. · Fish disappear. · It pollutes water. | Reforestation keeps the forest. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does sustainable management mean?

- ◻️ selling all the forests  
  _↳ feedback if chosen: That destroys the forests._
- ✅ using resources so that they remain for future generations
- ◻️ using everything now  
  _↳ feedback if chosen: That leaves nothing for the future._
- ◻️ never using any resource  
  _↳ feedback if chosen: We need resources to live._

Full working after a second miss:

> Use, but keep enough for the future.  
> So the answer is “using resources so that they remain for future generations”.  

> Which practice is sustainable?

- ✅ replanting trees after cutting
- ◻️ overfishing  
  _↳ feedback if chosen: Fish disappear._
- ◻️ dumping waste in rivers  
  _↳ feedback if chosen: It pollutes water._
- ◻️ bush fires  
  _↳ feedback if chosen: They destroy plants and soil._

Full working after a second miss:

> Reforestation keeps the forest.  
> So the answer is “replanting trees after cutting”.  

> Which practice is sustainable?

- ◻️ overfishing  
  _↳ feedback if chosen: Fish disappear._
- ◻️ dumping waste in rivers  
  _↳ feedback if chosen: It pollutes water._
- ◻️ bush fires  
  _↳ feedback if chosen: They destroy plants and soil._
- ✅ replanting trees after cutting

Full working after a second miss:

> Reforestation keeps the forest.  
> So the answer is “replanting trees after cutting”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-26-good` · Lesson 26 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which action saves energy? | switching off lights you do not need | leaving the fridge open · using filament bulbs everywhere · running a generator all day | That wastes electricity. · LEDs use less energy. · That wastes fuel. | Switch off what you do not use. |
| Which action protects rivers? | treating waste water before it reaches the river | washing cars in the river · throwing plastic in the river · pouring oil in the river | Soap and oil pollute the river. · Plastic pollutes the river. · Oil pollutes the river. | Clean water keeps fish and people healthy. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which action saves energy?

- ◻️ using filament bulbs everywhere  
  _↳ feedback if chosen: LEDs use less energy._
- ◻️ leaving the fridge open  
  _↳ feedback if chosen: That wastes electricity._
- ◻️ running a generator all day  
  _↳ feedback if chosen: That wastes fuel._
- ✅ switching off lights you do not need

Full working after a second miss:

> Switch off what you do not use.  
> So the answer is “switching off lights you do not need”.  

> Which action saves energy?

- ◻️ running a generator all day  
  _↳ feedback if chosen: That wastes fuel._
- ◻️ using filament bulbs everywhere  
  _↳ feedback if chosen: LEDs use less energy._
- ✅ switching off lights you do not need
- ◻️ leaving the fridge open  
  _↳ feedback if chosen: That wastes electricity._

Full working after a second miss:

> Switch off what you do not use.  
> So the answer is “switching off lights you do not need”.  

> Which action saves energy?

- ✅ switching off lights you do not need
- ◻️ leaving the fridge open  
  _↳ feedback if chosen: That wastes electricity._
- ◻️ running a generator all day  
  _↳ feedback if chosen: That wastes fuel._
- ◻️ using filament bulbs everywhere  
  _↳ feedback if chosen: LEDs use less energy._

Full working after a second miss:

> Switch off what you do not use.  
> So the answer is “switching off lights you do not need”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-26-park` · Lesson 26 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does Cameroon create national parks such as Korup and Dja? | to protect forests and wild animals | to cut timber faster · to build factories · to hunt more animals | Parks protect the forest. · Parks are protected areas. · Hunting is controlled in parks. | Parks protect biodiversity. |
| What is overfishing? | catching fish faster than they can reproduce | catching fish with a licence · keeping fish in ponds · eating fish once a week | A licence controls fishing. · That is fish farming. · That is a diet, not fishing. | Overfishing empties rivers and seas. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is overfishing?

- ◻️ eating fish once a week  
  _↳ feedback if chosen: That is a diet, not fishing._
- ✅ catching fish faster than they can reproduce
- ◻️ catching fish with a licence  
  _↳ feedback if chosen: A licence controls fishing._
- ◻️ keeping fish in ponds  
  _↳ feedback if chosen: That is fish farming._

Full working after a second miss:

> Overfishing empties rivers and seas.  
> So the answer is “catching fish faster than they can reproduce”.  

> What is overfishing?

- ◻️ keeping fish in ponds  
  _↳ feedback if chosen: That is fish farming._
- ◻️ eating fish once a week  
  _↳ feedback if chosen: That is a diet, not fishing._
- ◻️ catching fish with a licence  
  _↳ feedback if chosen: A licence controls fishing._
- ✅ catching fish faster than they can reproduce

Full working after a second miss:

> Overfishing empties rivers and seas.  
> So the answer is “catching fish faster than they can reproduce”.  

> Why does Cameroon create national parks such as Korup and Dja?

- ◻️ to hunt more animals  
  _↳ feedback if chosen: Hunting is controlled in parks._
- ✅ to protect forests and wild animals
- ◻️ to cut timber faster  
  _↳ feedback if chosen: Parks protect the forest._
- ◻️ to build factories  
  _↳ feedback if chosen: Parks are protected areas._

Full working after a second miss:

> Parks protect biodiversity.  
> So the answer is “to protect forests and wild animals”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-26-spot` · Lesson 26 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Reforestation helps forests.
- ✅ Recycling reduces waste.
- ✅ National parks protect wildlife.
- ✅ Saving water is sustainable.
- ❌ Bush fires make the soil richer for ever.  
  _↳ They destroy plants, animals and soil._
- ❌ Sustainable means using everything now.  
  _↳ It means keeping resources for the future._
- ❌ Overfishing protects fish.  
  _↳ It empties rivers and seas._


Three generated variants:

> Which statement is wrong?

- ◻️ Saving water is sustainable.
- ✅ Overfishing protects fish.  
  _↳ explanation: It empties rivers and seas._
- ◻️ National parks protect wildlife.
- ◻️ Reforestation helps forests.

Full working after a second miss:

> The wrong statement is “Overfishing protects fish.”.  
> It empties rivers and seas.  

> Which statement is wrong?

- ◻️ Recycling reduces waste.
- ◻️ National parks protect wildlife.
- ✅ Sustainable means using everything now.  
  _↳ explanation: It means keeping resources for the future._
- ◻️ Saving water is sustainable.

Full working after a second miss:

> The wrong statement is “Sustainable means using everything now.”.  
> It means keeping resources for the future.  

> Which statement is wrong?

- ◻️ Reforestation helps forests.
- ✅ Overfishing protects fish.  
  _↳ explanation: It empties rivers and seas._
- ◻️ National parks protect wildlife.
- ◻️ Saving water is sustainable.

Full working after a second miss:

> The wrong statement is “Overfishing protects fish.”.  
> It empties rivers and seas.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-26-park-card` · Lesson 26 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does Cameroon create national parks such as Korup and Dja? | to protect forests and wild animals | to cut timber faster · to build factories · to hunt more animals | Parks protect the forest. · Parks are protected areas. · Hunting is controlled in parks. | Parks protect biodiversity. |
| What is overfishing? | catching fish faster than they can reproduce | catching fish with a licence · keeping fish in ponds · eating fish once a week | A licence controls fishing. · That is fish farming. · That is a diet, not fishing. | Overfishing empties rivers and seas. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does Cameroon create national parks such as Korup and Dja?

- ◻️ to cut timber faster  
  _↳ feedback if chosen: Parks protect the forest._
- ◻️ to build factories  
  _↳ feedback if chosen: Parks are protected areas._
- ✅ to protect forests and wild animals
- ◻️ to hunt more animals  
  _↳ feedback if chosen: Hunting is controlled in parks._

Full working after a second miss:

> Parks protect biodiversity.  
> So the answer is “to protect forests and wild animals”.  

> Why does Cameroon create national parks such as Korup and Dja?

- ◻️ to build factories  
  _↳ feedback if chosen: Parks are protected areas._
- ✅ to protect forests and wild animals
- ◻️ to hunt more animals  
  _↳ feedback if chosen: Hunting is controlled in parks._
- ◻️ to cut timber faster  
  _↳ feedback if chosen: Parks protect the forest._

Full working after a second miss:

> Parks protect biodiversity.  
> So the answer is “to protect forests and wild animals”.  

> What is overfishing?

- ✅ catching fish faster than they can reproduce
- ◻️ keeping fish in ponds  
  _↳ feedback if chosen: That is fish farming._
- ◻️ eating fish once a week  
  _↳ feedback if chosen: That is a diet, not fishing._
- ◻️ catching fish with a licence  
  _↳ feedback if chosen: A licence controls fishing._

Full working after a second miss:

> Overfishing empties rivers and seas.  
> So the answer is “catching fish faster than they can reproduce”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-27-kind` · Lesson 27 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which radiation do we feel as heat? | infrared | ultraviolet · radio waves · X-rays | UV causes sunburn but we do not feel it as heat. · We do not feel radio waves. · X-rays are used in hospitals. | Infrared is heat radiation. |
| Which radiation causes sunburn? | ultraviolet (UV) | infrared · radio waves · visible light only | Infrared warms us. · Radio waves carry broadcasts. · UV is invisible. | UV burns the skin. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which radiation causes sunburn?

- ✅ ultraviolet (UV)
- ◻️ infrared  
  _↳ feedback if chosen: Infrared warms us._
- ◻️ radio waves  
  _↳ feedback if chosen: Radio waves carry broadcasts._
- ◻️ visible light only  
  _↳ feedback if chosen: UV is invisible._

Full working after a second miss:

> UV burns the skin.  
> So the answer is “ultraviolet (UV)”.  

> Which radiation causes sunburn?

- ◻️ radio waves  
  _↳ feedback if chosen: Radio waves carry broadcasts._
- ✅ ultraviolet (UV)
- ◻️ visible light only  
  _↳ feedback if chosen: UV is invisible._
- ◻️ infrared  
  _↳ feedback if chosen: Infrared warms us._

Full working after a second miss:

> UV burns the skin.  
> So the answer is “ultraviolet (UV)”.  

> Which radiation do we feel as heat?

- ◻️ X-rays  
  _↳ feedback if chosen: X-rays are used in hospitals._
- ✅ infrared
- ◻️ ultraviolet  
  _↳ feedback if chosen: UV causes sunburn but we do not feel it as heat._
- ◻️ radio waves  
  _↳ feedback if chosen: We do not feel radio waves._

Full working after a second miss:

> Infrared is heat radiation.  
> So the answer is “infrared”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-27-emit` · Lesson 27 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What gas does burning wood or petrol emit? | carbon dioxide | oxygen · nitrogen only · pure water only | Burning uses up oxygen. · Nitrogen is not the main product. · Water vapour is not the only product. | Burning releases carbon dioxide. |
| What damages the ozone layer? | CFC gases from old fridges and some sprays | water vapour from rivers · oxygen from plants · sound from radios | Water vapour is not the problem. · Plants give oxygen. · Sound is not a gas. | CFCs break down ozone. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What gas does burning wood or petrol emit?

- ◻️ oxygen  
  _↳ feedback if chosen: Burning uses up oxygen._
- ◻️ pure water only  
  _↳ feedback if chosen: Water vapour is not the only product._
- ✅ carbon dioxide
- ◻️ nitrogen only  
  _↳ feedback if chosen: Nitrogen is not the main product._

Full working after a second miss:

> Burning releases carbon dioxide.  
> So the answer is “carbon dioxide”.  

> What gas does burning wood or petrol emit?

- ✅ carbon dioxide
- ◻️ oxygen  
  _↳ feedback if chosen: Burning uses up oxygen._
- ◻️ nitrogen only  
  _↳ feedback if chosen: Nitrogen is not the main product._
- ◻️ pure water only  
  _↳ feedback if chosen: Water vapour is not the only product._

Full working after a second miss:

> Burning releases carbon dioxide.  
> So the answer is “carbon dioxide”.  

> What damages the ozone layer?

- ◻️ sound from radios  
  _↳ feedback if chosen: Sound is not a gas._
- ◻️ oxygen from plants  
  _↳ feedback if chosen: Plants give oxygen._
- ✅ CFC gases from old fridges and some sprays
- ◻️ water vapour from rivers  
  _↳ feedback if chosen: Water vapour is not the problem._

Full working after a second miss:

> CFCs break down ozone.  
> So the answer is “CFC gases from old fridges and some sprays”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-27-effect` · Lesson 27 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is carbon monoxide from a closed room with a charcoal stove dangerous? | it is a poisonous gas that can kill | it makes the room cold · it is healthy · it cleans the air | It is a poison. · It is a poison. · It pollutes. | Never use a charcoal stove in a closed room. |
| How can we reduce emissions? | maintain engines and stop bush fires | burn more rubbish · use older vehicles · cut more trees | That adds smoke. · Old engines pollute more. · Trees absorb carbon dioxide. | Cleaner engines and fewer fires mean less smoke. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is carbon monoxide from a closed room with a charcoal stove dangerous?

- ✅ it is a poisonous gas that can kill
- ◻️ it makes the room cold  
  _↳ feedback if chosen: It is a poison._
- ◻️ it is healthy  
  _↳ feedback if chosen: It is a poison._
- ◻️ it cleans the air  
  _↳ feedback if chosen: It pollutes._

Full working after a second miss:

> Never use a charcoal stove in a closed room.  
> So the answer is “it is a poisonous gas that can kill”.  

> How can we reduce emissions?

- ◻️ cut more trees  
  _↳ feedback if chosen: Trees absorb carbon dioxide._
- ✅ maintain engines and stop bush fires
- ◻️ burn more rubbish  
  _↳ feedback if chosen: That adds smoke._
- ◻️ use older vehicles  
  _↳ feedback if chosen: Old engines pollute more._

Full working after a second miss:

> Cleaner engines and fewer fires mean less smoke.  
> So the answer is “maintain engines and stop bush fires”.  

> How can we reduce emissions?

- ◻️ cut more trees  
  _↳ feedback if chosen: Trees absorb carbon dioxide._
- ◻️ use older vehicles  
  _↳ feedback if chosen: Old engines pollute more._
- ◻️ burn more rubbish  
  _↳ feedback if chosen: That adds smoke._
- ✅ maintain engines and stop bush fires

Full working after a second miss:

> Cleaner engines and fewer fires mean less smoke.  
> So the answer is “maintain engines and stop bush fires”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-27-spot` · Lesson 27 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Infrared radiation is felt as heat.
- ✅ Burning fuel emits carbon dioxide.
- ✅ CFCs damage the ozone layer.
- ✅ Bush fires pollute the air.
- ❌ Carbon monoxide is a harmless gas.  
  _↳ It is poisonous._
- ❌ Planting trees increases emissions.  
  _↳ Trees absorb carbon dioxide._
- ❌ UV radiation cannot harm the skin.  
  _↳ UV causes sunburn._


Three generated variants:

> Which statement is wrong?

- ◻️ Infrared radiation is felt as heat.
- ◻️ CFCs damage the ozone layer.
- ◻️ Burning fuel emits carbon dioxide.
- ✅ UV radiation cannot harm the skin.  
  _↳ explanation: UV causes sunburn._

Full working after a second miss:

> The wrong statement is “UV radiation cannot harm the skin.”.  
> UV causes sunburn.  

> Which statement is wrong?

- ◻️ Burning fuel emits carbon dioxide.
- ◻️ Bush fires pollute the air.
- ◻️ Infrared radiation is felt as heat.
- ✅ Carbon monoxide is a harmless gas.  
  _↳ explanation: It is poisonous._

Full working after a second miss:

> The wrong statement is “Carbon monoxide is a harmless gas.”.  
> It is poisonous.  

> Which statement is wrong?

- ✅ Planting trees increases emissions.  
  _↳ explanation: Trees absorb carbon dioxide._
- ◻️ CFCs damage the ozone layer.
- ◻️ Infrared radiation is felt as heat.
- ◻️ Bush fires pollute the air.

Full working after a second miss:

> The wrong statement is “Planting trees increases emissions.”.  
> Trees absorb carbon dioxide.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-27-effect-card` · Lesson 27 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is carbon monoxide from a closed room with a charcoal stove dangerous? | it is a poisonous gas that can kill | it makes the room cold · it is healthy · it cleans the air | It is a poison. · It is a poison. · It pollutes. | Never use a charcoal stove in a closed room. |
| How can we reduce emissions? | maintain engines and stop bush fires | burn more rubbish · use older vehicles · cut more trees | That adds smoke. · Old engines pollute more. · Trees absorb carbon dioxide. | Cleaner engines and fewer fires mean less smoke. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How can we reduce emissions?

- ◻️ cut more trees  
  _↳ feedback if chosen: Trees absorb carbon dioxide._
- ◻️ use older vehicles  
  _↳ feedback if chosen: Old engines pollute more._
- ✅ maintain engines and stop bush fires
- ◻️ burn more rubbish  
  _↳ feedback if chosen: That adds smoke._

Full working after a second miss:

> Cleaner engines and fewer fires mean less smoke.  
> So the answer is “maintain engines and stop bush fires”.  

> How can we reduce emissions?

- ◻️ use older vehicles  
  _↳ feedback if chosen: Old engines pollute more._
- ◻️ burn more rubbish  
  _↳ feedback if chosen: That adds smoke._
- ✅ maintain engines and stop bush fires
- ◻️ cut more trees  
  _↳ feedback if chosen: Trees absorb carbon dioxide._

Full working after a second miss:

> Cleaner engines and fewer fires mean less smoke.  
> So the answer is “maintain engines and stop bush fires”.  

> How can we reduce emissions?

- ◻️ cut more trees  
  _↳ feedback if chosen: Trees absorb carbon dioxide._
- ◻️ use older vehicles  
  _↳ feedback if chosen: Old engines pollute more._
- ✅ maintain engines and stop bush fires
- ◻️ burn more rubbish  
  _↳ feedback if chosen: That adds smoke._

Full working after a second miss:

> Cleaner engines and fewer fires mean less smoke.  
> So the answer is “maintain engines and stop bush fires”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-28-kind` · Lesson 28 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which radiation from the sun can we see? | visible light | ultraviolet · infrared · radio waves | UV is invisible. · We feel infrared as heat. · Radio waves are invisible. | Only visible light is seen. |
| What does sunlight help plants to do? | make food by photosynthesis | breathe out carbon dioxide only · stop growing · absorb UV to cool down | Photosynthesis takes in carbon dioxide. · Light helps them grow. · That is not the use. | Plants use light to make food. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which radiation from the sun can we see?

- ✅ visible light
- ◻️ ultraviolet  
  _↳ feedback if chosen: UV is invisible._
- ◻️ infrared  
  _↳ feedback if chosen: We feel infrared as heat._
- ◻️ radio waves  
  _↳ feedback if chosen: Radio waves are invisible._

Full working after a second miss:

> Only visible light is seen.  
> So the answer is “visible light”.  

> Which radiation from the sun can we see?

- ✅ visible light
- ◻️ radio waves  
  _↳ feedback if chosen: Radio waves are invisible._
- ◻️ ultraviolet  
  _↳ feedback if chosen: UV is invisible._
- ◻️ infrared  
  _↳ feedback if chosen: We feel infrared as heat._

Full working after a second miss:

> Only visible light is seen.  
> So the answer is “visible light”.  

> Which radiation from the sun can we see?

- ◻️ radio waves  
  _↳ feedback if chosen: Radio waves are invisible._
- ◻️ infrared  
  _↳ feedback if chosen: We feel infrared as heat._
- ◻️ ultraviolet  
  _↳ feedback if chosen: UV is invisible._
- ✅ visible light

Full working after a second miss:

> Only visible light is seen.  
> So the answer is “visible light”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-28-protect` · Lesson 28 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What protects the Earth from most of the sun's UV? | the ozone layer | the clouds only · the oceans · the moon | Clouds help a little but not most. · Oceans do not absorb UV for us. · The moon does not shield us. | Ozone high in the atmosphere absorbs UV. |
| Which is good protection against too much sun? | a hat and clothes that cover the skin | looking straight at the sun · staying in the midday sun for hours · removing sunglasses | That damages the eyes. · That is the most dangerous time. · Sunglasses help. | Cover up and avoid midday sun. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is good protection against too much sun?

- ✅ a hat and clothes that cover the skin
- ◻️ removing sunglasses  
  _↳ feedback if chosen: Sunglasses help._
- ◻️ looking straight at the sun  
  _↳ feedback if chosen: That damages the eyes._
- ◻️ staying in the midday sun for hours  
  _↳ feedback if chosen: That is the most dangerous time._

Full working after a second miss:

> Cover up and avoid midday sun.  
> So the answer is “a hat and clothes that cover the skin”.  

> Which is good protection against too much sun?

- ◻️ staying in the midday sun for hours  
  _↳ feedback if chosen: That is the most dangerous time._
- ◻️ removing sunglasses  
  _↳ feedback if chosen: Sunglasses help._
- ◻️ looking straight at the sun  
  _↳ feedback if chosen: That damages the eyes._
- ✅ a hat and clothes that cover the skin

Full working after a second miss:

> Cover up and avoid midday sun.  
> So the answer is “a hat and clothes that cover the skin”.  

> What protects the Earth from most of the sun's UV?

- ◻️ the moon  
  _↳ feedback if chosen: The moon does not shield us._
- ◻️ the clouds only  
  _↳ feedback if chosen: Clouds help a little but not most._
- ◻️ the oceans  
  _↳ feedback if chosen: Oceans do not absorb UV for us._
- ✅ the ozone layer

Full working after a second miss:

> Ozone high in the atmosphere absorbs UV.  
> So the answer is “the ozone layer”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-28-spot` · Lesson 28 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Sunlight takes about eight minutes to reach the Earth.
- ✅ UV can cause sunburn.
- ✅ The ozone layer absorbs UV.
- ✅ Plants need sunlight.
- ❌ It is safe to look straight at the sun.  
  _↳ It can damage the eyes._
- ❌ Sunlight reaches the Earth instantly.  
  _↳ It takes about eight minutes._
- ❌ Infrared radiation is cold.  
  _↳ Infrared is heat radiation._


Three generated variants:

> Which statement is wrong?

- ◻️ Plants need sunlight.
- ◻️ Sunlight takes about eight minutes to reach the Earth.
- ✅ It is safe to look straight at the sun.  
  _↳ explanation: It can damage the eyes._
- ◻️ The ozone layer absorbs UV.

Full working after a second miss:

> The wrong statement is “It is safe to look straight at the sun.”.  
> It can damage the eyes.  

> Which statement is wrong?

- ✅ It is safe to look straight at the sun.  
  _↳ explanation: It can damage the eyes._
- ◻️ Plants need sunlight.
- ◻️ Sunlight takes about eight minutes to reach the Earth.
- ◻️ The ozone layer absorbs UV.

Full working after a second miss:

> The wrong statement is “It is safe to look straight at the sun.”.  
> It can damage the eyes.  

> Which statement is wrong?

- ✅ It is safe to look straight at the sun.  
  _↳ explanation: It can damage the eyes._
- ◻️ Plants need sunlight.
- ◻️ Sunlight takes about eight minutes to reach the Earth.
- ◻️ The ozone layer absorbs UV.

Full working after a second miss:

> The wrong statement is “It is safe to look straight at the sun.”.  
> It can damage the eyes.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-28-protect-card` · Lesson 28 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What protects the Earth from most of the sun's UV? | the ozone layer | the clouds only · the oceans · the moon | Clouds help a little but not most. · Oceans do not absorb UV for us. · The moon does not shield us. | Ozone high in the atmosphere absorbs UV. |
| Which is good protection against too much sun? | a hat and clothes that cover the skin | looking straight at the sun · staying in the midday sun for hours · removing sunglasses | That damages the eyes. · That is the most dangerous time. · Sunglasses help. | Cover up and avoid midday sun. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What protects the Earth from most of the sun's UV?

- ✅ the ozone layer
- ◻️ the moon  
  _↳ feedback if chosen: The moon does not shield us._
- ◻️ the clouds only  
  _↳ feedback if chosen: Clouds help a little but not most._
- ◻️ the oceans  
  _↳ feedback if chosen: Oceans do not absorb UV for us._

Full working after a second miss:

> Ozone high in the atmosphere absorbs UV.  
> So the answer is “the ozone layer”.  

> Which is good protection against too much sun?

- ◻️ looking straight at the sun  
  _↳ feedback if chosen: That damages the eyes._
- ✅ a hat and clothes that cover the skin
- ◻️ staying in the midday sun for hours  
  _↳ feedback if chosen: That is the most dangerous time._
- ◻️ removing sunglasses  
  _↳ feedback if chosen: Sunglasses help._

Full working after a second miss:

> Cover up and avoid midday sun.  
> So the answer is “a hat and clothes that cover the skin”.  

> Which is good protection against too much sun?

- ◻️ staying in the midday sun for hours  
  _↳ feedback if chosen: That is the most dangerous time._
- ✅ a hat and clothes that cover the skin
- ◻️ removing sunglasses  
  _↳ feedback if chosen: Sunglasses help._
- ◻️ looking straight at the sun  
  _↳ feedback if chosen: That damages the eyes._

Full working after a second miss:

> Cover up and avoid midday sun.  
> So the answer is “a hat and clothes that cover the skin”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-29-gas` · Lesson 29 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which is a greenhouse gas? | carbon dioxide | oxygen · nitrogen · argon | Oxygen does not trap much heat. · Nitrogen does not trap much heat. · Argon does not trap heat. | Carbon dioxide traps infrared radiation. |
| Which is a greenhouse gas made by rotting rubbish? | methane | oxygen · hydrogen · helium | Rotting uses oxygen. · Hydrogen is not the main gas. · Helium is not produced. | Rotting waste gives methane. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is a greenhouse gas made by rotting rubbish?

- ◻️ oxygen  
  _↳ feedback if chosen: Rotting uses oxygen._
- ◻️ helium  
  _↳ feedback if chosen: Helium is not produced._
- ✅ methane
- ◻️ hydrogen  
  _↳ feedback if chosen: Hydrogen is not the main gas._

Full working after a second miss:

> Rotting waste gives methane.  
> So the answer is “methane”.  

> Which is a greenhouse gas made by rotting rubbish?

- ◻️ oxygen  
  _↳ feedback if chosen: Rotting uses oxygen._
- ◻️ helium  
  _↳ feedback if chosen: Helium is not produced._
- ◻️ hydrogen  
  _↳ feedback if chosen: Hydrogen is not the main gas._
- ✅ methane

Full working after a second miss:

> Rotting waste gives methane.  
> So the answer is “methane”.  

> Which is a greenhouse gas?

- ◻️ oxygen  
  _↳ feedback if chosen: Oxygen does not trap much heat._
- ✅ carbon dioxide
- ◻️ nitrogen  
  _↳ feedback if chosen: Nitrogen does not trap much heat._
- ◻️ argon  
  _↳ feedback if chosen: Argon does not trap heat._

Full working after a second miss:

> Carbon dioxide traps infrared radiation.  
> So the answer is “carbon dioxide”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-29-good` · Lesson 29 · ordering, level 1

Prompt: Put the steps of the greenhouse effect in order.

Items in the right order:

1. Sunlight passes through the atmosphere.
2. The ground absorbs it and gets warm.
3. The warm ground gives out infrared radiation.
4. Greenhouse gases absorb part of this radiation.
5. The air near the ground stays warm.


Three generated variants:

> Put the steps of the greenhouse effect in order.

Shown as: The air near the ground stays warm. · The ground absorbs it and gets warm. · Sunlight passes through the atmosphere. · Greenhouse gases absorb part of this radiation. · The warm ground gives out infrared radiation.
Correct order: Sunlight passes through the atmosphere. → The ground absorbs it and gets warm. → The warm ground gives out infrared radiation. → Greenhouse gases absorb part of this radiation. → The air near the ground stays warm.

Full working after a second miss:

> The correct order is: Sunlight passes through the atmosphere. → The ground absorbs it and gets warm. → The warm ground gives out infrared radiation. → Greenhouse gases absorb part of this radiation. → The air near the ground stays warm..  

> Put the steps of the greenhouse effect in order.

Shown as: The warm ground gives out infrared radiation. · Greenhouse gases absorb part of this radiation. · Sunlight passes through the atmosphere. · The air near the ground stays warm. · The ground absorbs it and gets warm.
Correct order: Sunlight passes through the atmosphere. → The ground absorbs it and gets warm. → The warm ground gives out infrared radiation. → Greenhouse gases absorb part of this radiation. → The air near the ground stays warm.

Full working after a second miss:

> The correct order is: Sunlight passes through the atmosphere. → The ground absorbs it and gets warm. → The warm ground gives out infrared radiation. → Greenhouse gases absorb part of this radiation. → The air near the ground stays warm..  

> Put the steps of the greenhouse effect in order.

Shown as: The warm ground gives out infrared radiation. · Sunlight passes through the atmosphere. · The ground absorbs it and gets warm. · The air near the ground stays warm. · Greenhouse gases absorb part of this radiation.
Correct order: Sunlight passes through the atmosphere. → The ground absorbs it and gets warm. → The warm ground gives out infrared radiation. → Greenhouse gases absorb part of this radiation. → The air near the ground stays warm.

Full working after a second miss:

> The correct order is: Sunlight passes through the atmosphere. → The ground absorbs it and gets warm. → The warm ground gives out infrared radiation. → Greenhouse gases absorb part of this radiation. → The air near the ground stays warm..  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-29-human` · Lesson 29 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which human activity increases the greenhouse effect? | burning fuel and forests | planting trees · using solar energy · walking to school | Trees absorb carbon dioxide. · Solar energy emits no carbon dioxide. · Walking burns no fuel. | Burning adds carbon dioxide. |
| What would happen without any greenhouse effect? | the Earth would be too cold for life | the Earth would be hotter · nothing would change · there would be more rain | It would be colder. · It would be much colder. · The main effect is cold. | Greenhouse gases keep us warm. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which human activity increases the greenhouse effect?

- ◻️ planting trees  
  _↳ feedback if chosen: Trees absorb carbon dioxide._
- ◻️ walking to school  
  _↳ feedback if chosen: Walking burns no fuel._
- ✅ burning fuel and forests
- ◻️ using solar energy  
  _↳ feedback if chosen: Solar energy emits no carbon dioxide._

Full working after a second miss:

> Burning adds carbon dioxide.  
> So the answer is “burning fuel and forests”.  

> What would happen without any greenhouse effect?

- ◻️ the Earth would be hotter  
  _↳ feedback if chosen: It would be colder._
- ✅ the Earth would be too cold for life
- ◻️ nothing would change  
  _↳ feedback if chosen: It would be much colder._
- ◻️ there would be more rain  
  _↳ feedback if chosen: The main effect is cold._

Full working after a second miss:

> Greenhouse gases keep us warm.  
> So the answer is “the Earth would be too cold for life”.  

> What would happen without any greenhouse effect?

- ✅ the Earth would be too cold for life
- ◻️ there would be more rain  
  _↳ feedback if chosen: The main effect is cold._
- ◻️ the Earth would be hotter  
  _↳ feedback if chosen: It would be colder._
- ◻️ nothing would change  
  _↳ feedback if chosen: It would be much colder._

Full working after a second miss:

> Greenhouse gases keep us warm.  
> So the answer is “the Earth would be too cold for life”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-29-spot` · Lesson 29 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Carbon dioxide is a greenhouse gas.
- ✅ The ground gives out infrared radiation.
- ✅ Without the greenhouse effect the Earth would be very cold.
- ✅ Burning forests adds carbon dioxide.
- ❌ Planting trees increases the greenhouse effect.  
  _↳ Trees absorb carbon dioxide._
- ❌ Oxygen is the main greenhouse gas.  
  _↳ Carbon dioxide, methane and water vapour are._
- ❌ The greenhouse effect is always harmful.  
  _↳ The natural effect keeps life possible._


Three generated variants:

> Which statement is wrong?

- ◻️ Burning forests adds carbon dioxide.
- ◻️ Without the greenhouse effect the Earth would be very cold.
- ◻️ Carbon dioxide is a greenhouse gas.
- ✅ The greenhouse effect is always harmful.  
  _↳ explanation: The natural effect keeps life possible._

Full working after a second miss:

> The wrong statement is “The greenhouse effect is always harmful.”.  
> The natural effect keeps life possible.  

> Which statement is wrong?

- ◻️ The ground gives out infrared radiation.
- ◻️ Carbon dioxide is a greenhouse gas.
- ◻️ Burning forests adds carbon dioxide.
- ✅ Oxygen is the main greenhouse gas.  
  _↳ explanation: Carbon dioxide, methane and water vapour are._

Full working after a second miss:

> The wrong statement is “Oxygen is the main greenhouse gas.”.  
> Carbon dioxide, methane and water vapour are.  

> Which statement is wrong?

- ◻️ Without the greenhouse effect the Earth would be very cold.
- ✅ The greenhouse effect is always harmful.  
  _↳ explanation: The natural effect keeps life possible._
- ◻️ The ground gives out infrared radiation.
- ◻️ Burning forests adds carbon dioxide.

Full working after a second miss:

> The wrong statement is “The greenhouse effect is always harmful.”.  
> The natural effect keeps life possible.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-29-human-card` · Lesson 29 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which human activity increases the greenhouse effect? | burning fuel and forests | planting trees · using solar energy · walking to school | Trees absorb carbon dioxide. · Solar energy emits no carbon dioxide. · Walking burns no fuel. | Burning adds carbon dioxide. |
| What would happen without any greenhouse effect? | the Earth would be too cold for life | the Earth would be hotter · nothing would change · there would be more rain | It would be colder. · It would be much colder. · The main effect is cold. | Greenhouse gases keep us warm. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What would happen without any greenhouse effect?

- ◻️ the Earth would be hotter  
  _↳ feedback if chosen: It would be colder._
- ◻️ nothing would change  
  _↳ feedback if chosen: It would be much colder._
- ✅ the Earth would be too cold for life
- ◻️ there would be more rain  
  _↳ feedback if chosen: The main effect is cold._

Full working after a second miss:

> Greenhouse gases keep us warm.  
> So the answer is “the Earth would be too cold for life”.  

> Which human activity increases the greenhouse effect?

- ◻️ planting trees  
  _↳ feedback if chosen: Trees absorb carbon dioxide._
- ◻️ walking to school  
  _↳ feedback if chosen: Walking burns no fuel._
- ✅ burning fuel and forests
- ◻️ using solar energy  
  _↳ feedback if chosen: Solar energy emits no carbon dioxide._

Full working after a second miss:

> Burning adds carbon dioxide.  
> So the answer is “burning fuel and forests”.  

> Which human activity increases the greenhouse effect?

- ◻️ walking to school  
  _↳ feedback if chosen: Walking burns no fuel._
- ◻️ planting trees  
  _↳ feedback if chosen: Trees absorb carbon dioxide._
- ◻️ using solar energy  
  _↳ feedback if chosen: Solar energy emits no carbon dioxide._
- ✅ burning fuel and forests

Full working after a second miss:

> Burning adds carbon dioxide.  
> So the answer is “burning fuel and forests”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-30-def` · Lesson 30 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is global warming? | the slow rise of the Earth's average temperature | a hot day · the dry season · a volcano erupting | One hot day is weather. · That is a normal season. · That is a natural event. | It is a long-term rise in temperature. |
| What is the main cause of global warming? | extra greenhouse gases from human activities | the moon · too many rivers · earthquakes | The moon does not warm the Earth. · Rivers do not cause it. · Earthquakes do not cause it. | Burning fuel and forests add greenhouse gases. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the main cause of global warming?

- ◻️ the moon  
  _↳ feedback if chosen: The moon does not warm the Earth._
- ◻️ too many rivers  
  _↳ feedback if chosen: Rivers do not cause it._
- ◻️ earthquakes  
  _↳ feedback if chosen: Earthquakes do not cause it._
- ✅ extra greenhouse gases from human activities

Full working after a second miss:

> Burning fuel and forests add greenhouse gases.  
> So the answer is “extra greenhouse gases from human activities”.  

> What is global warming?

- ◻️ a hot day  
  _↳ feedback if chosen: One hot day is weather._
- ◻️ the dry season  
  _↳ feedback if chosen: That is a normal season._
- ✅ the slow rise of the Earth's average temperature
- ◻️ a volcano erupting  
  _↳ feedback if chosen: That is a natural event._

Full working after a second miss:

> It is a long-term rise in temperature.  
> So the answer is “the slow rise of the Earth's average temperature”.  

> What is global warming?

- ◻️ the dry season  
  _↳ feedback if chosen: That is a normal season._
- ✅ the slow rise of the Earth's average temperature
- ◻️ a hot day  
  _↳ feedback if chosen: One hot day is weather._
- ◻️ a volcano erupting  
  _↳ feedback if chosen: That is a natural event._

Full working after a second miss:

> It is a long-term rise in temperature.  
> So the answer is “the slow rise of the Earth's average temperature”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-30-effect` · Lesson 30 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do sea levels rise with global warming? | ice melts and warm water takes more space | it rains only on the sea · rivers flow backwards · fish drink less water | Rain falls everywhere. · That does not happen. · That is not a cause. | Melting ice adds water. |
| Which is a consequence of global warming? | longer droughts | colder winters everywhere · more ice on mountains · fewer floods everywhere | The average temperature rises. · Ice melts. · Heavy rains and floods increase in some places. | Dry areas get drier. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why do sea levels rise with global warming?

- ✅ ice melts and warm water takes more space
- ◻️ rivers flow backwards  
  _↳ feedback if chosen: That does not happen._
- ◻️ it rains only on the sea  
  _↳ feedback if chosen: Rain falls everywhere._
- ◻️ fish drink less water  
  _↳ feedback if chosen: That is not a cause._

Full working after a second miss:

> Melting ice adds water.  
> So the answer is “ice melts and warm water takes more space”.  

> Which is a consequence of global warming?

- ✅ longer droughts
- ◻️ colder winters everywhere  
  _↳ feedback if chosen: The average temperature rises._
- ◻️ more ice on mountains  
  _↳ feedback if chosen: Ice melts._
- ◻️ fewer floods everywhere  
  _↳ feedback if chosen: Heavy rains and floods increase in some places._

Full working after a second miss:

> Dry areas get drier.  
> So the answer is “longer droughts”.  

> Why do sea levels rise with global warming?

- ◻️ fish drink less water  
  _↳ feedback if chosen: That is not a cause._
- ✅ ice melts and warm water takes more space
- ◻️ rivers flow backwards  
  _↳ feedback if chosen: That does not happen._
- ◻️ it rains only on the sea  
  _↳ feedback if chosen: Rain falls everywhere._

Full working after a second miss:

> Melting ice adds water.  
> So the answer is “ice melts and warm water takes more space”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-30-solve` · Lesson 30 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which action helps to fight global warming? | using solar energy instead of a diesel generator | burning more rubbish · cutting forests · leaving engines running | That adds greenhouse gases. · That removes trees. · That burns fuel for nothing. | Solar energy emits no carbon dioxide. |
| Why does planting trees help? | trees absorb carbon dioxide | trees produce carbon dioxide only · trees make the Earth hotter · trees stop the rain | They take it in during photosynthesis. · They cool the land. · They help the water cycle. | Trees store carbon. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which action helps to fight global warming?

- ◻️ leaving engines running  
  _↳ feedback if chosen: That burns fuel for nothing._
- ◻️ cutting forests  
  _↳ feedback if chosen: That removes trees._
- ✅ using solar energy instead of a diesel generator
- ◻️ burning more rubbish  
  _↳ feedback if chosen: That adds greenhouse gases._

Full working after a second miss:

> Solar energy emits no carbon dioxide.  
> So the answer is “using solar energy instead of a diesel generator”.  

> Why does planting trees help?

- ◻️ trees stop the rain  
  _↳ feedback if chosen: They help the water cycle._
- ◻️ trees make the Earth hotter  
  _↳ feedback if chosen: They cool the land._
- ◻️ trees produce carbon dioxide only  
  _↳ feedback if chosen: They take it in during photosynthesis._
- ✅ trees absorb carbon dioxide

Full working after a second miss:

> Trees store carbon.  
> So the answer is “trees absorb carbon dioxide”.  

> Why does planting trees help?

- ✅ trees absorb carbon dioxide
- ◻️ trees produce carbon dioxide only  
  _↳ feedback if chosen: They take it in during photosynthesis._
- ◻️ trees make the Earth hotter  
  _↳ feedback if chosen: They cool the land._
- ◻️ trees stop the rain  
  _↳ feedback if chosen: They help the water cycle._

Full working after a second miss:

> Trees store carbon.  
> So the answer is “trees absorb carbon dioxide”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-30-spot` · Lesson 30 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Global warming raises sea levels.
- ✅ Planting trees helps.
- ✅ Burning fuel adds greenhouse gases.
- ✅ Droughts may become longer.
- ❌ Global warming makes the Earth colder.  
  _↳ It raises the average temperature._
- ❌ Cutting forests stops global warming.  
  _↳ It adds carbon dioxide._
- ❌ Global warming has no effect on Cameroon.  
  _↳ Droughts and floods affect Cameroon._


Three generated variants:

> Which statement is wrong?

- ◻️ Droughts may become longer.
- ✅ Global warming has no effect on Cameroon.  
  _↳ explanation: Droughts and floods affect Cameroon._
- ◻️ Burning fuel adds greenhouse gases.
- ◻️ Planting trees helps.

Full working after a second miss:

> The wrong statement is “Global warming has no effect on Cameroon.”.  
> Droughts and floods affect Cameroon.  

> Which statement is wrong?

- ◻️ Burning fuel adds greenhouse gases.
- ✅ Global warming makes the Earth colder.  
  _↳ explanation: It raises the average temperature._
- ◻️ Global warming raises sea levels.
- ◻️ Droughts may become longer.

Full working after a second miss:

> The wrong statement is “Global warming makes the Earth colder.”.  
> It raises the average temperature.  

> Which statement is wrong?

- ✅ Global warming has no effect on Cameroon.  
  _↳ explanation: Droughts and floods affect Cameroon._
- ◻️ Planting trees helps.
- ◻️ Burning fuel adds greenhouse gases.
- ◻️ Droughts may become longer.

Full working after a second miss:

> The wrong statement is “Global warming has no effect on Cameroon.”.  
> Droughts and floods affect Cameroon.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-30-solve-card` · Lesson 30 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which action helps to fight global warming? | using solar energy instead of a diesel generator | burning more rubbish · cutting forests · leaving engines running | That adds greenhouse gases. · That removes trees. · That burns fuel for nothing. | Solar energy emits no carbon dioxide. |
| Why does planting trees help? | trees absorb carbon dioxide | trees produce carbon dioxide only · trees make the Earth hotter · trees stop the rain | They take it in during photosynthesis. · They cool the land. · They help the water cycle. | Trees store carbon. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which action helps to fight global warming?

- ◻️ burning more rubbish  
  _↳ feedback if chosen: That adds greenhouse gases._
- ◻️ cutting forests  
  _↳ feedback if chosen: That removes trees._
- ✅ using solar energy instead of a diesel generator
- ◻️ leaving engines running  
  _↳ feedback if chosen: That burns fuel for nothing._

Full working after a second miss:

> Solar energy emits no carbon dioxide.  
> So the answer is “using solar energy instead of a diesel generator”.  

> Which action helps to fight global warming?

- ◻️ cutting forests  
  _↳ feedback if chosen: That removes trees._
- ◻️ burning more rubbish  
  _↳ feedback if chosen: That adds greenhouse gases._
- ◻️ leaving engines running  
  _↳ feedback if chosen: That burns fuel for nothing._
- ✅ using solar energy instead of a diesel generator

Full working after a second miss:

> Solar energy emits no carbon dioxide.  
> So the answer is “using solar energy instead of a diesel generator”.  

> Which action helps to fight global warming?

- ◻️ leaving engines running  
  _↳ feedback if chosen: That burns fuel for nothing._
- ◻️ burning more rubbish  
  _↳ feedback if chosen: That adds greenhouse gases._
- ◻️ cutting forests  
  _↳ feedback if chosen: That removes trees._
- ✅ using solar energy instead of a diesel generator

Full working after a second miss:

> Solar energy emits no carbon dioxide.  
> So the answer is “using solar energy instead of a diesel generator”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-31-def` · Lesson 31 · multiple choice, level 1

Prompt: Is this weather or climate? “{X.q}”

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| It rained heavily in Buea this morning. | weather | climate · climate change · pollution | One morning is weather. · One morning is not a long-term change. · It is about rain, not pollution. | One day's conditions are weather. |
| The north of Cameroon has a long dry season every year. | climate | weather · a storm · pollution | It is a pattern over many years. · It is a yearly pattern. · It is not pollution. | A pattern over many years is climate. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is this weather or climate? “It rained heavily in Buea this morning.”

- ✅ weather
- ◻️ pollution  
  _↳ feedback if chosen: It is about rain, not pollution._
- ◻️ climate change  
  _↳ feedback if chosen: One morning is not a long-term change._
- ◻️ climate  
  _↳ feedback if chosen: One morning is weather._

Full working after a second miss:

> One day's conditions are weather.  
> So the answer is “weather”.  

> Is this weather or climate? “It rained heavily in Buea this morning.”

- ✅ weather
- ◻️ pollution  
  _↳ feedback if chosen: It is about rain, not pollution._
- ◻️ climate change  
  _↳ feedback if chosen: One morning is not a long-term change._
- ◻️ climate  
  _↳ feedback if chosen: One morning is weather._

Full working after a second miss:

> One day's conditions are weather.  
> So the answer is “weather”.  

> Is this weather or climate? “It rained heavily in Buea this morning.”

- ◻️ climate  
  _↳ feedback if chosen: One morning is weather._
- ✅ weather
- ◻️ pollution  
  _↳ feedback if chosen: It is about rain, not pollution._
- ◻️ climate change  
  _↳ feedback if chosen: One morning is not a long-term change._

Full working after a second miss:

> One day's conditions are weather.  
> So the answer is “weather”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-31-effect` · Lesson 31 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How does climate change affect farmers? | they do not know when the rains will come to plant | they always get bigger harvests · nothing changes for them · they stop needing water | Harvests often fall. · Rains change. · Crops still need water. | Unpredictable rains disturb planting. |
| Why can food prices rise with climate change? | harvests fall, so there is less food | there is too much food · markets close every day · people stop eating | Less food is produced. · Markets still open. · That is not the reason. | Less supply → higher prices. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why can food prices rise with climate change?

- ◻️ there is too much food  
  _↳ feedback if chosen: Less food is produced._
- ◻️ markets close every day  
  _↳ feedback if chosen: Markets still open._
- ◻️ people stop eating  
  _↳ feedback if chosen: That is not the reason._
- ✅ harvests fall, so there is less food

Full working after a second miss:

> Less supply → higher prices.  
> So the answer is “harvests fall, so there is less food”.  

> How does climate change affect farmers?

- ◻️ nothing changes for them  
  _↳ feedback if chosen: Rains change._
- ✅ they do not know when the rains will come to plant
- ◻️ they stop needing water  
  _↳ feedback if chosen: Crops still need water._
- ◻️ they always get bigger harvests  
  _↳ feedback if chosen: Harvests often fall._

Full working after a second miss:

> Unpredictable rains disturb planting.  
> So the answer is “they do not know when the rains will come to plant”.  

> How does climate change affect farmers?

- ◻️ nothing changes for them  
  _↳ feedback if chosen: Rains change._
- ◻️ they stop needing water  
  _↳ feedback if chosen: Crops still need water._
- ✅ they do not know when the rains will come to plant
- ◻️ they always get bigger harvests  
  _↳ feedback if chosen: Harvests often fall._

Full working after a second miss:

> Unpredictable rains disturb planting.  
> So the answer is “they do not know when the rains will come to plant”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-31-adapt` · Lesson 31 · multiple choice, level 2

Prompt: Is this adaptation or mitigation? “{X.q}”

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Storing rain water for the dry season | adaptation | mitigation · pollution · weather | It does not reduce greenhouse gases; it helps us live with the change. · It is not pollution. · It is an action. | Adapting to scarce water. |
| Using solar energy instead of diesel | mitigation | adaptation · pollution · weather | It reduces greenhouse gases. · It reduces pollution. · It is an action. | It reduces the cause. |
| Planting drought-resistant crops | adaptation | mitigation · pollution · weather | It helps farmers live with droughts. · It is not pollution. · It is an action. | Adapting to droughts. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is this adaptation or mitigation? “Storing rain water for the dry season”

- ◻️ mitigation  
  _↳ feedback if chosen: It does not reduce greenhouse gases; it helps us live with the change._
- ✅ adaptation
- ◻️ weather  
  _↳ feedback if chosen: It is an action._
- ◻️ pollution  
  _↳ feedback if chosen: It is not pollution._

Full working after a second miss:

> Adapting to scarce water.  
> So the answer is “adaptation”.  

> Is this adaptation or mitigation? “Storing rain water for the dry season”

- ◻️ weather  
  _↳ feedback if chosen: It is an action._
- ✅ adaptation
- ◻️ pollution  
  _↳ feedback if chosen: It is not pollution._
- ◻️ mitigation  
  _↳ feedback if chosen: It does not reduce greenhouse gases; it helps us live with the change._

Full working after a second miss:

> Adapting to scarce water.  
> So the answer is “adaptation”.  

> Is this adaptation or mitigation? “Using solar energy instead of diesel”

- ◻️ weather  
  _↳ feedback if chosen: It is an action._
- ✅ mitigation
- ◻️ pollution  
  _↳ feedback if chosen: It reduces pollution._
- ◻️ adaptation  
  _↳ feedback if chosen: It reduces greenhouse gases._

Full working after a second miss:

> It reduces the cause.  
> So the answer is “mitigation”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-31-spot` · Lesson 31 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Climate is the pattern of weather over many years.
- ✅ Storing rain water is adaptation.
- ✅ Using renewable energy is mitigation.
- ✅ Climate change can bring floods.
- ❌ One rainy day proves climate change.  
  _↳ One day is weather._
- ❌ Climate change only affects rich countries.  
  _↳ Cameroon's farmers feel it too._
- ❌ Adaptation means increasing greenhouse gases.  
  _↳ Adaptation means living with the change._


Three generated variants:

> Which statement is wrong?

- ✅ One rainy day proves climate change.  
  _↳ explanation: One day is weather._
- ◻️ Using renewable energy is mitigation.
- ◻️ Climate is the pattern of weather over many years.
- ◻️ Storing rain water is adaptation.

Full working after a second miss:

> The wrong statement is “One rainy day proves climate change.”.  
> One day is weather.  

> Which statement is wrong?

- ✅ Adaptation means increasing greenhouse gases.  
  _↳ explanation: Adaptation means living with the change._
- ◻️ Storing rain water is adaptation.
- ◻️ Climate is the pattern of weather over many years.
- ◻️ Using renewable energy is mitigation.

Full working after a second miss:

> The wrong statement is “Adaptation means increasing greenhouse gases.”.  
> Adaptation means living with the change.  

> Which statement is wrong?

- ✅ Climate change only affects rich countries.  
  _↳ explanation: Cameroon's farmers feel it too._
- ◻️ Storing rain water is adaptation.
- ◻️ Climate change can bring floods.
- ◻️ Using renewable energy is mitigation.

Full working after a second miss:

> The wrong statement is “Climate change only affects rich countries.”.  
> Cameroon's farmers feel it too.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

### `p2-31-adapt-card` · Lesson 31 · multiple choice, level 1

Prompt: Is this adaptation or mitigation? “{X.q}”

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Storing rain water for the dry season | adaptation | mitigation · pollution · weather | It does not reduce greenhouse gases; it helps us live with the change. · It is not pollution. · It is an action. | Adapting to scarce water. |
| Using solar energy instead of diesel | mitigation | adaptation · pollution · weather | It reduces greenhouse gases. · It reduces pollution. · It is an action. | It reduces the cause. |
| Planting drought-resistant crops | adaptation | mitigation · pollution · weather | It helps farmers live with droughts. · It is not pollution. · It is an action. | Adapting to droughts. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Is this adaptation or mitigation? “Planting drought-resistant crops”

- ✅ adaptation
- ◻️ pollution  
  _↳ feedback if chosen: It is not pollution._
- ◻️ mitigation  
  _↳ feedback if chosen: It helps farmers live with droughts._
- ◻️ weather  
  _↳ feedback if chosen: It is an action._

Full working after a second miss:

> Adapting to droughts.  
> So the answer is “adaptation”.  

> Is this adaptation or mitigation? “Planting drought-resistant crops”

- ◻️ mitigation  
  _↳ feedback if chosen: It helps farmers live with droughts._
- ◻️ weather  
  _↳ feedback if chosen: It is an action._
- ◻️ pollution  
  _↳ feedback if chosen: It is not pollution._
- ✅ adaptation

Full working after a second miss:

> Adapting to droughts.  
> So the answer is “adaptation”.  

> Is this adaptation or mitigation? “Using solar energy instead of diesel”

- ◻️ weather  
  _↳ feedback if chosen: It is an action._
- ◻️ pollution  
  _↳ feedback if chosen: It reduces pollution._
- ✅ mitigation
- ◻️ adaptation  
  _↳ feedback if chosen: It reduces greenhouse gases._

Full working after a second miss:

> It reduces the cause.  
> So the answer is “mitigation”.  

Sources: radiation-climate (Kinds of radiation, emissions, the sun's radiation and the ozone layer, the greenhouse effect, global warming, climate change, adaptation and mitigation, sustainable management (national parks Korup, Waza, Dja))

