# Physics Form 2, Batch P2-1: authored answers for review

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

