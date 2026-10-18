# Geography Form 2, Batch G2-1: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f2-geography`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: formulae (computed by code)

- BR = births ÷ population × 1000; DR likewise; NI = BR − DR (‰), ÷ 10 for %; density = population ÷ area.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `g2-1-read` | 1 | multiple choice, 1 | world-population |
| 2 | `g2-1-factor` | 1 | multiple choice, 1 | world-population |
| 3 | `g2-1-where` | 1 | multiple choice, 2 | world-population |
| 4 | `g2-1-where-card` (card c1-3) | 1 | multiple choice, 1 | world-population |
| 5 | `g2-2-effect` | 2 | multiple choice, 1 | world-population |
| 6 | `g2-2-match` | 2 | matching, 1 | world-population |
| 7 | `g2-2-solve` | 2 | multiple choice, 2 | world-population |
| 8 | `g2-2-spot` | 2 | spot the error, 3 | world-population |
| 9 | `g2-2-solve-card` (card c2-3) | 2 | multiple choice, 1 | world-population |
| 10 | `g2-5-where` | 5 | matching, 1 | world-population |
| 11 | `g2-5-sparse` | 5 | multiple choice, 3 | world-population |
| 12 | `g2-5-sparse-card` (card c5-3) | 5 | multiple choice, 1 | world-population |
| 13 | `g2-6-sort` | 6 | matching, 1 | world-population |
| 14 | `g2-6-kind` | 6 | matching, 1 | world-population |
| 15 | `g2-6-case` | 6 | multiple choice, 2 | world-population |
| 16 | `g2-6-spot` | 6 | spot the error, 3 | world-population |
| 17 | `g2-6-case-card` (card c6-3) | 6 | multiple choice, 1 | world-population |
| 18 | `g2-7-most` | 7 | multiple choice, 1 | cameroon-regions |
| 19 | `g2-8-where` | 8 | multiple choice, 1 | equatorial-zone |
| 20 | `g2-8-climate` | 8 | multiple choice, 1 | equatorial-zone |
| 21 | `g2-8-resource` | 8 | matching, 2 | equatorial-zone |
| 22 | `g2-8-method` | 8 | multiple choice, 3 | equatorial-zone |
| 23 | `g2-8-resource-card` (card c8-3) | 8 | matching, 1 | equatorial-zone |
| 24 | `g2-9-problem` | 9 | multiple choice, 1 | equatorial-zone |
| 25 | `g2-9-match` | 9 | matching, 1 | equatorial-zone |
| 26 | `g2-9-solve` | 9 | multiple choice, 2 | equatorial-zone |
| 27 | `g2-9-spot` | 9 | spot the error, 3 | equatorial-zone |
| 28 | `g2-9-solve-card` (card c9-3) | 9 | multiple choice, 1 | equatorial-zone |
| 29 | `g2-10-cause` | 10 | matching, 1 | cameroon-regions |
| 30 | `g2-10-see` | 10 | multiple choice, 1 | cameroon-regions |
| 31 | `g2-10-solve` | 10 | multiple choice, 2 | cameroon-regions |
| 32 | `g2-10-spot` | 10 | spot the error, 3 | cameroon-regions |
| 33 | `g2-10-solve-card` (card c10-3) | 10 | multiple choice, 1 | cameroon-regions |

### `g2-1-read` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| About how many people lived in the world in 2022? | 8 billion | 1 billion · 3 billion · 80 million | That was around 1800. · That was in 1960. · That is far too few. | The world reached 8 billion in 2022. |
| When did the world reach about 1 billion people? | around 1800 | around 1960 · around 2011 · around the year 1000 | It was 3 billion in 1960. · It was 7 billion in 2011. · It was much less then. | About 1 billion around 1800. |
| Between 1960 and 1999 the world's population … | doubled from 3 to 6 billion | stayed the same · fell · grew by only a little | It grew a lot. · It grew. · It doubled. | 3 billion to 6 billion is doubling. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> About how many people lived in the world in 2022?

- ◻️ 1 billion  
  _↳ feedback if chosen: That was around 1800._
- ✅ 8 billion
- ◻️ 3 billion  
  _↳ feedback if chosen: That was in 1960._
- ◻️ 80 million  
  _↳ feedback if chosen: That is far too few._

Full working after a second miss:

> The world reached 8 billion in 2022.  
> So the answer is “8 billion”.  

> When did the world reach about 1 billion people?

- ◻️ around 2011  
  _↳ feedback if chosen: It was 7 billion in 2011._
- ✅ around 1800
- ◻️ around 1960  
  _↳ feedback if chosen: It was 3 billion in 1960._
- ◻️ around the year 1000  
  _↳ feedback if chosen: It was much less then._

Full working after a second miss:

> About 1 billion around 1800.  
> So the answer is “around 1800”.  

> When did the world reach about 1 billion people?

- ◻️ around 2011  
  _↳ feedback if chosen: It was 7 billion in 2011._
- ✅ around 1800
- ◻️ around 1960  
  _↳ feedback if chosen: It was 3 billion in 1960._
- ◻️ around the year 1000  
  _↳ feedback if chosen: It was much less then._

Full working after a second miss:

> About 1 billion around 1800.  
> So the answer is “around 1800”.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-1-factor` · Lesson 1 · multiple choice, level 1

Prompt: Which is a factor of the rapid growth of the world's population?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ better medicine and vaccination
- ✅ clean water and better hygiene
- ✅ more food from better farming
- ✅ high birth rates in developing countries
- ❌ more wars and famines  
  _↳ Wars and famines raise death rates and slow growth._
- ❌ fewer babies surviving  
  _↳ More babies survive today._
- ❌ shorter lives  
  _↳ People live longer today._


Three generated variants:

> Which is a factor of the rapid growth of the world's population?

- ◻️ fewer babies surviving  
  _↳ feedback if chosen: More babies survive today._
- ✅ high birth rates in developing countries
- ◻️ shorter lives  
  _↳ feedback if chosen: People live longer today._

Full working after a second miss:

> The true statement is “high birth rates in developing countries”.  
> “fewer babies surviving” is false: More babies survive today.  
> “shorter lives” is false: People live longer today.  

> Which is a factor of the rapid growth of the world's population?

- ◻️ more wars and famines  
  _↳ feedback if chosen: Wars and famines raise death rates and slow growth._
- ◻️ shorter lives  
  _↳ feedback if chosen: People live longer today._
- ✅ better medicine and vaccination

Full working after a second miss:

> The true statement is “better medicine and vaccination”.  
> “more wars and famines” is false: Wars and famines raise death rates and slow growth.  
> “shorter lives” is false: People live longer today.  

> Which is a factor of the rapid growth of the world's population?

- ◻️ more wars and famines  
  _↳ feedback if chosen: Wars and famines raise death rates and slow growth._
- ✅ high birth rates in developing countries
- ◻️ fewer babies surviving  
  _↳ feedback if chosen: More babies survive today._

Full working after a second miss:

> The true statement is “high birth rates in developing countries”.  
> “more wars and famines” is false: Wars and famines raise death rates and slow growth.  
> “fewer babies surviving” is false: More babies survive today.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-1-where` · Lesson 1 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Where is the population growing fastest today? | Africa | Europe · North America · Australia | Europe grows slowest. · Growth there is slow. · Growth there is slow. | Africa has the highest birth rates. |
| Why do falling death rates make a population grow? | More people survive while births stay high. | Fewer babies are born. · People move to other planets. · Births stop. | Births stay high. · That is not true. · Births continue. | Births minus deaths gets bigger. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why do falling death rates make a population grow?

- ◻️ Fewer babies are born.  
  _↳ feedback if chosen: Births stay high._
- ◻️ People move to other planets.  
  _↳ feedback if chosen: That is not true._
- ◻️ Births stop.  
  _↳ feedback if chosen: Births continue._
- ✅ More people survive while births stay high.

Full working after a second miss:

> Births minus deaths gets bigger.  
> So the answer is “More people survive while births stay high.”.  

> Where is the population growing fastest today?

- ✅ Africa
- ◻️ Europe  
  _↳ feedback if chosen: Europe grows slowest._
- ◻️ North America  
  _↳ feedback if chosen: Growth there is slow._
- ◻️ Australia  
  _↳ feedback if chosen: Growth there is slow._

Full working after a second miss:

> Africa has the highest birth rates.  
> So the answer is “Africa”.  

> Where is the population growing fastest today?

- ✅ Africa
- ◻️ Europe  
  _↳ feedback if chosen: Europe grows slowest._
- ◻️ Australia  
  _↳ feedback if chosen: Growth there is slow._
- ◻️ North America  
  _↳ feedback if chosen: Growth there is slow._

Full working after a second miss:

> Africa has the highest birth rates.  
> So the answer is “Africa”.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-1-where-card` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Where is the population growing fastest today? | Africa | Europe · North America · Australia | Europe grows slowest. · Growth there is slow. · Growth there is slow. | Africa has the highest birth rates. |
| Why do falling death rates make a population grow? | More people survive while births stay high. | Fewer babies are born. · People move to other planets. · Births stop. | Births stay high. · That is not true. · Births continue. | Births minus deaths gets bigger. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Where is the population growing fastest today?

- ◻️ Europe  
  _↳ feedback if chosen: Europe grows slowest._
- ✅ Africa
- ◻️ Australia  
  _↳ feedback if chosen: Growth there is slow._
- ◻️ North America  
  _↳ feedback if chosen: Growth there is slow._

Full working after a second miss:

> Africa has the highest birth rates.  
> So the answer is “Africa”.  

> Why do falling death rates make a population grow?

- ◻️ People move to other planets.  
  _↳ feedback if chosen: That is not true._
- ✅ More people survive while births stay high.
- ◻️ Fewer babies are born.  
  _↳ feedback if chosen: Births stay high._
- ◻️ Births stop.  
  _↳ feedback if chosen: Births continue._

Full working after a second miss:

> Births minus deaths gets bigger.  
> So the answer is “More people survive while births stay high.”.  

> Where is the population growing fastest today?

- ◻️ North America  
  _↳ feedback if chosen: Growth there is slow._
- ◻️ Europe  
  _↳ feedback if chosen: Europe grows slowest._
- ◻️ Australia  
  _↳ feedback if chosen: Growth there is slow._
- ✅ Africa

Full working after a second miss:

> Africa has the highest birth rates.  
> So the answer is “Africa”.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-2-effect` · Lesson 2 · multiple choice, level 1

Prompt: Which is an effect of rapid population growth on natural resources?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ forests cleared for farms
- ✅ soils losing their fertility
- ✅ water shortages
- ✅ wildlife losing its habitat
- ❌ more forest everywhere  
  _↳ More people usually means less forest._
- ❌ cleaner rivers  
  _↳ More waste often pollutes rivers._
- ❌ more wild animals  
  _↳ Habitats shrink, so wildlife declines._


Three generated variants:

> Which is an effect of rapid population growth on natural resources?

- ◻️ more wild animals  
  _↳ feedback if chosen: Habitats shrink, so wildlife declines._
- ◻️ cleaner rivers  
  _↳ feedback if chosen: More waste often pollutes rivers._
- ✅ forests cleared for farms

Full working after a second miss:

> The true statement is “forests cleared for farms”.  
> “more wild animals” is false: Habitats shrink, so wildlife declines.  
> “cleaner rivers” is false: More waste often pollutes rivers.  

> Which is an effect of rapid population growth on natural resources?

- ◻️ more forest everywhere  
  _↳ feedback if chosen: More people usually means less forest._
- ◻️ more wild animals  
  _↳ feedback if chosen: Habitats shrink, so wildlife declines._
- ✅ water shortages

Full working after a second miss:

> The true statement is “water shortages”.  
> “more forest everywhere” is false: More people usually means less forest.  
> “more wild animals” is false: Habitats shrink, so wildlife declines.  

> Which is an effect of rapid population growth on natural resources?

- ◻️ cleaner rivers  
  _↳ feedback if chosen: More waste often pollutes rivers._
- ✅ water shortages
- ◻️ more forest everywhere  
  _↳ feedback if chosen: More people usually means less forest._

Full working after a second miss:

> The true statement is “water shortages”.  
> “cleaner rivers” is false: More waste often pollutes rivers.  
> “more forest everywhere” is false: More people usually means less forest.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-2-match` · Lesson 2 · matching, level 1

Prompt: Match each resource to the pressure on it.

Pairs (4 shown each time):

- forest → **cut for farms and firewood**
- soil → **overcultivated and overgrazed**
- water → **shortages and pollution**
- wildlife → **hunting and loss of habitat**
- minerals → **used up faster**


Three generated variants:

> Match each resource to the pressure on it.

Right-hand side (shuffled): hunting and loss of habitat · cut for farms and firewood · overcultivated and overgrazed · shortages and pollution
- water → **shortages and pollution**
- forest → **cut for farms and firewood**
- soil → **overcultivated and overgrazed**
- wildlife → **hunting and loss of habitat**

Full working after a second miss:

> The right pairs are:  
> water → shortages and pollution  
> forest → cut for farms and firewood  
> soil → overcultivated and overgrazed  
> wildlife → hunting and loss of habitat  

> Match each resource to the pressure on it.

Right-hand side (shuffled): cut for farms and firewood · overcultivated and overgrazed · shortages and pollution · used up faster
- soil → **overcultivated and overgrazed**
- forest → **cut for farms and firewood**
- water → **shortages and pollution**
- minerals → **used up faster**

Full working after a second miss:

> The right pairs are:  
> soil → overcultivated and overgrazed  
> forest → cut for farms and firewood  
> water → shortages and pollution  
> minerals → used up faster  

> Match each resource to the pressure on it.

Right-hand side (shuffled): hunting and loss of habitat · used up faster · cut for farms and firewood · overcultivated and overgrazed
- wildlife → **hunting and loss of habitat**
- soil → **overcultivated and overgrazed**
- minerals → **used up faster**
- forest → **cut for farms and firewood**

Full working after a second miss:

> The right pairs are:  
> wildlife → hunting and loss of habitat  
> soil → overcultivated and overgrazed  
> minerals → used up faster  
> forest → cut for farms and firewood  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-2-solve` · Lesson 2 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which is a solution to the pressure on forests? | reforestation (planting trees) | cutting more trees · burning the bush · more logging roads | That worsens it. · That destroys forest. · That opens more forest to logging. | Replanting replaces lost trees. |
| What does sustainable use of resources mean? | using them so that future generations still have them | using them all up quickly · never using them at all · selling them abroad | That is the opposite. · Resources can be used carefully. · That is not the meaning. | Sustainable means it can go on. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is a solution to the pressure on forests?

- ◻️ burning the bush  
  _↳ feedback if chosen: That destroys forest._
- ✅ reforestation (planting trees)
- ◻️ more logging roads  
  _↳ feedback if chosen: That opens more forest to logging._
- ◻️ cutting more trees  
  _↳ feedback if chosen: That worsens it._

Full working after a second miss:

> Replanting replaces lost trees.  
> So the answer is “reforestation (planting trees)”.  

> Which is a solution to the pressure on forests?

- ◻️ burning the bush  
  _↳ feedback if chosen: That destroys forest._
- ◻️ cutting more trees  
  _↳ feedback if chosen: That worsens it._
- ✅ reforestation (planting trees)
- ◻️ more logging roads  
  _↳ feedback if chosen: That opens more forest to logging._

Full working after a second miss:

> Replanting replaces lost trees.  
> So the answer is “reforestation (planting trees)”.  

> Which is a solution to the pressure on forests?

- ◻️ more logging roads  
  _↳ feedback if chosen: That opens more forest to logging._
- ◻️ burning the bush  
  _↳ feedback if chosen: That destroys forest._
- ◻️ cutting more trees  
  _↳ feedback if chosen: That worsens it._
- ✅ reforestation (planting trees)

Full working after a second miss:

> Replanting replaces lost trees.  
> So the answer is “reforestation (planting trees)”.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-2-spot` · Lesson 2 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Rapid growth increases pressure on forests.
- ✅ Overgrazing can cause soil erosion.
- ✅ Reforestation helps replace lost trees.
- ✅ Family planning can slow population growth.
- ❌ Rapid population growth always makes soils more fertile.  
  _↳ Overuse usually makes soils less fertile._
- ❌ More people means less need for water.  
  _↳ More people need more water._
- ❌ Deforestation increases wildlife.  
  _↳ It destroys habitats and reduces wildlife._


Three generated variants:

> Which statement is wrong?

- ◻️ Rapid growth increases pressure on forests.
- ◻️ Family planning can slow population growth.
- ◻️ Overgrazing can cause soil erosion.
- ✅ Rapid population growth always makes soils more fertile.  
  _↳ explanation: Overuse usually makes soils less fertile._

Full working after a second miss:

> The wrong statement is “Rapid population growth always makes soils more fertile.”.  
> Overuse usually makes soils less fertile.  

> Which statement is wrong?

- ◻️ Family planning can slow population growth.
- ✅ More people means less need for water.  
  _↳ explanation: More people need more water._
- ◻️ Overgrazing can cause soil erosion.
- ◻️ Rapid growth increases pressure on forests.

Full working after a second miss:

> The wrong statement is “More people means less need for water.”.  
> More people need more water.  

> Which statement is wrong?

- ◻️ Rapid growth increases pressure on forests.
- ◻️ Family planning can slow population growth.
- ✅ More people means less need for water.  
  _↳ explanation: More people need more water._
- ◻️ Reforestation helps replace lost trees.

Full working after a second miss:

> The wrong statement is “More people means less need for water.”.  
> More people need more water.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-2-solve-card` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which is a solution to the pressure on forests? | reforestation (planting trees) | cutting more trees · burning the bush · more logging roads | That worsens it. · That destroys forest. · That opens more forest to logging. | Replanting replaces lost trees. |
| What does sustainable use of resources mean? | using them so that future generations still have them | using them all up quickly · never using them at all · selling them abroad | That is the opposite. · Resources can be used carefully. · That is not the meaning. | Sustainable means it can go on. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is a solution to the pressure on forests?

- ◻️ more logging roads  
  _↳ feedback if chosen: That opens more forest to logging._
- ◻️ burning the bush  
  _↳ feedback if chosen: That destroys forest._
- ◻️ cutting more trees  
  _↳ feedback if chosen: That worsens it._
- ✅ reforestation (planting trees)

Full working after a second miss:

> Replanting replaces lost trees.  
> So the answer is “reforestation (planting trees)”.  

> Which is a solution to the pressure on forests?

- ✅ reforestation (planting trees)
- ◻️ burning the bush  
  _↳ feedback if chosen: That destroys forest._
- ◻️ more logging roads  
  _↳ feedback if chosen: That opens more forest to logging._
- ◻️ cutting more trees  
  _↳ feedback if chosen: That worsens it._

Full working after a second miss:

> Replanting replaces lost trees.  
> So the answer is “reforestation (planting trees)”.  

> What does sustainable use of resources mean?

- ◻️ selling them abroad  
  _↳ feedback if chosen: That is not the meaning._
- ◻️ never using them at all  
  _↳ feedback if chosen: Resources can be used carefully._
- ✅ using them so that future generations still have them
- ◻️ using them all up quickly  
  _↳ feedback if chosen: That is the opposite._

Full working after a second miss:

> Sustainable means it can go on.  
> So the answer is “using them so that future generations still have them”.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-5-where` · Lesson 5 · matching, level 1

Prompt: Sort the areas: densely or sparsely populated?

Pairs (4 shown each time, sorted into groups):

- eastern China → **dense**
- Bangladesh → **dense**
- the Nile valley → **dense**
- Western Europe → **dense**
- the Sahara → **sparse**
- Greenland → **sparse**
- the Amazon forest → **sparse**
- Antarctica → **sparse**


Three generated variants:

> Sort the areas: densely or sparsely populated?

Groups: dense · sparse
- Western Europe → **dense**
- eastern China → **dense**
- the Sahara → **sparse**
- Antarctica → **sparse**

Full working after a second miss:

> The right pairs are:  
> Western Europe → dense  
> eastern China → dense  
> the Sahara → sparse  
> Antarctica → sparse  

> Sort the areas: densely or sparsely populated?

Groups: dense · sparse
- Greenland → **sparse**
- the Nile valley → **dense**
- Antarctica → **sparse**
- the Sahara → **sparse**

Full working after a second miss:

> The right pairs are:  
> Greenland → sparse  
> the Nile valley → dense  
> Antarctica → sparse  
> the Sahara → sparse  

> Sort the areas: densely or sparsely populated?

Groups: dense · sparse
- Greenland → **sparse**
- the Sahara → **sparse**
- the Nile valley → **dense**
- eastern China → **dense**

Full working after a second miss:

> The right pairs are:  
> Greenland → sparse  
> the Sahara → sparse  
> the Nile valley → dense  
> eastern China → dense  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-5-sparse` · Lesson 5 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does Antarctica have no permanent population? | It is far too cold and covered in ice. | It is too hot. · It has too many cities. · It is too crowded. | It is the coldest continent. · It has no cities. · It has no permanent people. | Extreme cold makes life very hard. |
| Which hemisphere holds most of the world's people? | the Northern Hemisphere | the Southern Hemisphere · both equally · neither | It holds far fewer. · Most live in the north. · Most live in the north. | Most land and most people are north of the equator. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does Antarctica have no permanent population?

- ◻️ It is too crowded.  
  _↳ feedback if chosen: It has no permanent people._
- ✅ It is far too cold and covered in ice.
- ◻️ It is too hot.  
  _↳ feedback if chosen: It is the coldest continent._
- ◻️ It has too many cities.  
  _↳ feedback if chosen: It has no cities._

Full working after a second miss:

> Extreme cold makes life very hard.  
> So the answer is “It is far too cold and covered in ice.”.  

> Which hemisphere holds most of the world's people?

- ◻️ neither  
  _↳ feedback if chosen: Most live in the north._
- ◻️ the Southern Hemisphere  
  _↳ feedback if chosen: It holds far fewer._
- ◻️ both equally  
  _↳ feedback if chosen: Most live in the north._
- ✅ the Northern Hemisphere

Full working after a second miss:

> Most land and most people are north of the equator.  
> So the answer is “the Northern Hemisphere”.  

> Which hemisphere holds most of the world's people?

- ◻️ the Southern Hemisphere  
  _↳ feedback if chosen: It holds far fewer._
- ◻️ both equally  
  _↳ feedback if chosen: Most live in the north._
- ✅ the Northern Hemisphere
- ◻️ neither  
  _↳ feedback if chosen: Most live in the north._

Full working after a second miss:

> Most land and most people are north of the equator.  
> So the answer is “the Northern Hemisphere”.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-5-sparse-card` · Lesson 5 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why does Antarctica have no permanent population? | It is far too cold and covered in ice. | It is too hot. · It has too many cities. · It is too crowded. | It is the coldest continent. · It has no cities. · It has no permanent people. | Extreme cold makes life very hard. |
| Which hemisphere holds most of the world's people? | the Northern Hemisphere | the Southern Hemisphere · both equally · neither | It holds far fewer. · Most live in the north. · Most live in the north. | Most land and most people are north of the equator. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which hemisphere holds most of the world's people?

- ✅ the Northern Hemisphere
- ◻️ both equally  
  _↳ feedback if chosen: Most live in the north._
- ◻️ the Southern Hemisphere  
  _↳ feedback if chosen: It holds far fewer._
- ◻️ neither  
  _↳ feedback if chosen: Most live in the north._

Full working after a second miss:

> Most land and most people are north of the equator.  
> So the answer is “the Northern Hemisphere”.  

> Which hemisphere holds most of the world's people?

- ◻️ neither  
  _↳ feedback if chosen: Most live in the north._
- ◻️ the Southern Hemisphere  
  _↳ feedback if chosen: It holds far fewer._
- ◻️ both equally  
  _↳ feedback if chosen: Most live in the north._
- ✅ the Northern Hemisphere

Full working after a second miss:

> Most land and most people are north of the equator.  
> So the answer is “the Northern Hemisphere”.  

> Why does Antarctica have no permanent population?

- ✅ It is far too cold and covered in ice.
- ◻️ It is too hot.  
  _↳ feedback if chosen: It is the coldest continent._
- ◻️ It has too many cities.  
  _↳ feedback if chosen: It has no cities._
- ◻️ It is too crowded.  
  _↳ feedback if chosen: It has no permanent people._

Full working after a second miss:

> Extreme cold makes life very hard.  
> So the answer is “It is far too cold and covered in ice.”.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-6-sort` · Lesson 6 · matching, level 1

Prompt: Sort the factors: does each attract or repel people?

Pairs (4 shown each time, sorted into groups):

- flat, fertile river valleys → **attracts people**
- a mild climate with enough rain → **attracts people**
- mines and industries → **attracts people**
- good roads and ports → **attracts people**
- very cold climate → **repels people**
- hot desert with little water → **repels people**
- steep, high mountains → **repels people**
- areas with tsetse flies and disease → **repels people**


Three generated variants:

> Sort the factors: does each attract or repel people?

Groups: attracts people · repels people
- hot desert with little water → **repels people**
- a mild climate with enough rain → **attracts people**
- areas with tsetse flies and disease → **repels people**
- steep, high mountains → **repels people**

Full working after a second miss:

> The right pairs are:  
> hot desert with little water → repels people  
> a mild climate with enough rain → attracts people  
> areas with tsetse flies and disease → repels people  
> steep, high mountains → repels people  

> Sort the factors: does each attract or repel people?

Groups: attracts people · repels people
- a mild climate with enough rain → **attracts people**
- flat, fertile river valleys → **attracts people**
- good roads and ports → **attracts people**
- very cold climate → **repels people**

Full working after a second miss:

> The right pairs are:  
> a mild climate with enough rain → attracts people  
> flat, fertile river valleys → attracts people  
> good roads and ports → attracts people  
> very cold climate → repels people  

> Sort the factors: does each attract or repel people?

Groups: attracts people · repels people
- steep, high mountains → **repels people**
- good roads and ports → **attracts people**
- very cold climate → **repels people**
- flat, fertile river valleys → **attracts people**

Full working after a second miss:

> The right pairs are:  
> steep, high mountains → repels people  
> good roads and ports → attracts people  
> very cold climate → repels people  
> flat, fertile river valleys → attracts people  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-6-kind` · Lesson 6 · matching, level 1

Prompt: Sort the factors: physical or human?

Pairs (4 shown each time, sorted into groups):

- relief → **physical**
- climate → **physical**
- soils → **physical**
- water supply → **physical**
- industries → **human**
- roads and ports → **human**
- government policy → **human**
- schools and hospitals → **human**


Three generated variants:

> Sort the factors: physical or human?

Groups: physical · human
- soils → **physical**
- relief → **physical**
- water supply → **physical**
- schools and hospitals → **human**

Full working after a second miss:

> The right pairs are:  
> soils → physical  
> relief → physical  
> water supply → physical  
> schools and hospitals → human  

> Sort the factors: physical or human?

Groups: physical · human
- government policy → **human**
- soils → **physical**
- water supply → **physical**
- relief → **physical**

Full working after a second miss:

> The right pairs are:  
> government policy → human  
> soils → physical  
> water supply → physical  
> relief → physical  

> Sort the factors: physical or human?

Groups: physical · human
- schools and hospitals → **human**
- relief → **physical**
- soils → **physical**
- industries → **human**

Full working after a second miss:

> The right pairs are:  
> schools and hospitals → human  
> relief → physical  
> soils → physical  
> industries → human  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-6-case` · Lesson 6 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is Douala densely populated? | Its port and industries give many jobs. | It is very cold. · It is a desert. · It has steep mountains. | Douala is hot and humid. · It is not a desert. · It is on a coastal plain. | Economic activity attracts people. |
| Why is much of the East Region of Cameroon sparsely populated? | It is covered by dense equatorial forest with few roads. | It is a cold desert. · It is full of factories. · It has the biggest port. | It is hot and wet. · It has few industries. · The port is Douala. | Dense forest and poor communications repel people. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is Douala densely populated?

- ✅ Its port and industries give many jobs.
- ◻️ It has steep mountains.  
  _↳ feedback if chosen: It is on a coastal plain._
- ◻️ It is a desert.  
  _↳ feedback if chosen: It is not a desert._
- ◻️ It is very cold.  
  _↳ feedback if chosen: Douala is hot and humid._

Full working after a second miss:

> Economic activity attracts people.  
> So the answer is “Its port and industries give many jobs.”.  

> Why is Douala densely populated?

- ✅ Its port and industries give many jobs.
- ◻️ It has steep mountains.  
  _↳ feedback if chosen: It is on a coastal plain._
- ◻️ It is very cold.  
  _↳ feedback if chosen: Douala is hot and humid._
- ◻️ It is a desert.  
  _↳ feedback if chosen: It is not a desert._

Full working after a second miss:

> Economic activity attracts people.  
> So the answer is “Its port and industries give many jobs.”.  

> Why is much of the East Region of Cameroon sparsely populated?

- ◻️ It is a cold desert.  
  _↳ feedback if chosen: It is hot and wet._
- ◻️ It has the biggest port.  
  _↳ feedback if chosen: The port is Douala._
- ✅ It is covered by dense equatorial forest with few roads.
- ◻️ It is full of factories.  
  _↳ feedback if chosen: It has few industries._

Full working after a second miss:

> Dense forest and poor communications repel people.  
> So the answer is “It is covered by dense equatorial forest with few roads.”.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-6-spot` · Lesson 6 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Fertile soils attract farmers.
- ✅ Industries attract workers.
- ✅ Very dry deserts repel people.
- ✅ Wars push people away.
- ❌ Steep high mountains attract dense populations.  
  _↳ They usually repel people._
- ❌ Tsetse flies attract settlers.  
  _↳ Tsetse flies and disease repel people._
- ❌ Good roads repel people.  
  _↳ Good roads attract people._


Three generated variants:

> Which statement is wrong?

- ◻️ Fertile soils attract farmers.
- ◻️ Wars push people away.
- ◻️ Industries attract workers.
- ✅ Tsetse flies attract settlers.  
  _↳ explanation: Tsetse flies and disease repel people._

Full working after a second miss:

> The wrong statement is “Tsetse flies attract settlers.”.  
> Tsetse flies and disease repel people.  

> Which statement is wrong?

- ✅ Steep high mountains attract dense populations.  
  _↳ explanation: They usually repel people._
- ◻️ Industries attract workers.
- ◻️ Wars push people away.
- ◻️ Very dry deserts repel people.

Full working after a second miss:

> The wrong statement is “Steep high mountains attract dense populations.”.  
> They usually repel people.  

> Which statement is wrong?

- ✅ Steep high mountains attract dense populations.  
  _↳ explanation: They usually repel people._
- ◻️ Wars push people away.
- ◻️ Very dry deserts repel people.
- ◻️ Industries attract workers.

Full working after a second miss:

> The wrong statement is “Steep high mountains attract dense populations.”.  
> They usually repel people.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-6-case-card` · Lesson 6 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why is Douala densely populated? | Its port and industries give many jobs. | It is very cold. · It is a desert. · It has steep mountains. | Douala is hot and humid. · It is not a desert. · It is on a coastal plain. | Economic activity attracts people. |
| Why is much of the East Region of Cameroon sparsely populated? | It is covered by dense equatorial forest with few roads. | It is a cold desert. · It is full of factories. · It has the biggest port. | It is hot and wet. · It has few industries. · The port is Douala. | Dense forest and poor communications repel people. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why is Douala densely populated?

- ◻️ It has steep mountains.  
  _↳ feedback if chosen: It is on a coastal plain._
- ✅ Its port and industries give many jobs.
- ◻️ It is very cold.  
  _↳ feedback if chosen: Douala is hot and humid._
- ◻️ It is a desert.  
  _↳ feedback if chosen: It is not a desert._

Full working after a second miss:

> Economic activity attracts people.  
> So the answer is “Its port and industries give many jobs.”.  

> Why is much of the East Region of Cameroon sparsely populated?

- ◻️ It has the biggest port.  
  _↳ feedback if chosen: The port is Douala._
- ◻️ It is a cold desert.  
  _↳ feedback if chosen: It is hot and wet._
- ◻️ It is full of factories.  
  _↳ feedback if chosen: It has few industries._
- ✅ It is covered by dense equatorial forest with few roads.

Full working after a second miss:

> Dense forest and poor communications repel people.  
> So the answer is “It is covered by dense equatorial forest with few roads.”.  

> Why is Douala densely populated?

- ✅ Its port and industries give many jobs.
- ◻️ It is very cold.  
  _↳ feedback if chosen: Douala is hot and humid._
- ◻️ It has steep mountains.  
  _↳ feedback if chosen: It is on a coastal plain._
- ◻️ It is a desert.  
  _↳ feedback if chosen: It is not a desert._

Full working after a second miss:

> Economic activity attracts people.  
> So the answer is “Its port and industries give many jobs.”.  

Sources: world-population (UN World Population Prospects (world population milestones: 1 billion about 1800 … 8 billion on 15 November 2022); geography textbooks on population distribution and its factors)

### `g2-7-most` · Lesson 7 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which region is among the most densely populated? | West | East · South · Adamawa | The East is the least dense. · The South is sparsely populated. · Adamawa is sparsely populated. | The West has a small area and many people. |
| Which region has the largest area? | East | West · Littoral · North-West | The West is small. · The Littoral is small. · The North-West is small. | The East is the largest region. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which region is among the most densely populated?

- ◻️ East  
  _↳ feedback if chosen: The East is the least dense._
- ◻️ South  
  _↳ feedback if chosen: The South is sparsely populated._
- ✅ West
- ◻️ Adamawa  
  _↳ feedback if chosen: Adamawa is sparsely populated._

Full working after a second miss:

> The West has a small area and many people.  
> So the answer is “West”.  

> Which region has the largest area?

- ◻️ Littoral  
  _↳ feedback if chosen: The Littoral is small._
- ◻️ West  
  _↳ feedback if chosen: The West is small._
- ✅ East
- ◻️ North-West  
  _↳ feedback if chosen: The North-West is small._

Full working after a second miss:

> The East is the largest region.  
> So the answer is “East”.  

> Which region is among the most densely populated?

- ◻️ East  
  _↳ feedback if chosen: The East is the least dense._
- ✅ West
- ◻️ South  
  _↳ feedback if chosen: The South is sparsely populated._
- ◻️ Adamawa  
  _↳ feedback if chosen: Adamawa is sparsely populated._

Full working after a second miss:

> The West has a small area and many people.  
> So the answer is “West”.  

Sources: cameroon-regions (Areas of Cameroon's ten regions (km²) and rounded population estimates; deforestation in Cameroon; protected areas Dja, Lobéké, Korup)

### `g2-8-where` · Lesson 8 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which of these areas is in the equatorial zone? | the Congo basin | the Sahara · Greenland · the Mediterranean coast | That is a hot desert. · That is a cold land. · That has a Mediterranean climate. | The Congo basin lies on the equator. |
| About how far from the equator does the equatorial zone extend? | about 5° to 10° north and south | about 40° north and south · only at the poles · about 23° north only | That is too far. · The poles are cold. · It is on both sides of the equator. | It lies close to the equator. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which of these areas is in the equatorial zone?

- ◻️ the Mediterranean coast  
  _↳ feedback if chosen: That has a Mediterranean climate._
- ◻️ the Sahara  
  _↳ feedback if chosen: That is a hot desert._
- ◻️ Greenland  
  _↳ feedback if chosen: That is a cold land._
- ✅ the Congo basin

Full working after a second miss:

> The Congo basin lies on the equator.  
> So the answer is “the Congo basin”.  

> Which of these areas is in the equatorial zone?

- ◻️ the Sahara  
  _↳ feedback if chosen: That is a hot desert._
- ◻️ the Mediterranean coast  
  _↳ feedback if chosen: That has a Mediterranean climate._
- ✅ the Congo basin
- ◻️ Greenland  
  _↳ feedback if chosen: That is a cold land._

Full working after a second miss:

> The Congo basin lies on the equator.  
> So the answer is “the Congo basin”.  

> Which of these areas is in the equatorial zone?

- ◻️ the Mediterranean coast  
  _↳ feedback if chosen: That has a Mediterranean climate._
- ◻️ the Sahara  
  _↳ feedback if chosen: That is a hot desert._
- ◻️ Greenland  
  _↳ feedback if chosen: That is a cold land._
- ✅ the Congo basin

Full working after a second miss:

> The Congo basin lies on the equator.  
> So the answer is “the Congo basin”.  

Sources: equatorial-zone (The equatorial climate and the exploitation of the equatorial forest (as in Cameroonian Form 2 geography))

### `g2-8-climate` · Lesson 8 · multiple choice, level 1

Prompt: Which is a feature of the equatorial climate?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ hot all year
- ✅ heavy rain all year
- ✅ a small annual range of temperature
- ✅ high humidity
- ❌ a long dry season with no rain  
  _↳ Rain falls all year._
- ❌ a large annual range of temperature  
  _↳ The range is very small, 2–3 °C._
- ❌ snow in the cool season  
  _↳ It is hot all year._


Three generated variants:

> Which is a feature of the equatorial climate?

- ✅ a small annual range of temperature
- ◻️ a long dry season with no rain  
  _↳ feedback if chosen: Rain falls all year._
- ◻️ snow in the cool season  
  _↳ feedback if chosen: It is hot all year._

Full working after a second miss:

> The true statement is “a small annual range of temperature”.  
> “a long dry season with no rain” is false: Rain falls all year.  
> “snow in the cool season” is false: It is hot all year.  

> Which is a feature of the equatorial climate?

- ✅ a small annual range of temperature
- ◻️ snow in the cool season  
  _↳ feedback if chosen: It is hot all year._
- ◻️ a large annual range of temperature  
  _↳ feedback if chosen: The range is very small, 2–3 °C._

Full working after a second miss:

> The true statement is “a small annual range of temperature”.  
> “snow in the cool season” is false: It is hot all year.  
> “a large annual range of temperature” is false: The range is very small, 2–3 °C.  

> Which is a feature of the equatorial climate?

- ◻️ a long dry season with no rain  
  _↳ feedback if chosen: Rain falls all year._
- ◻️ a large annual range of temperature  
  _↳ feedback if chosen: The range is very small, 2–3 °C._
- ✅ heavy rain all year

Full working after a second miss:

> The true statement is “heavy rain all year”.  
> “a long dry season with no rain” is false: Rain falls all year.  
> “a large annual range of temperature” is false: The range is very small, 2–3 °C.  

Sources: equatorial-zone (The equatorial climate and the exploitation of the equatorial forest (as in Cameroonian Form 2 geography))

### `g2-8-resource` · Lesson 8 · matching, level 2

Prompt: Match each resource to its type.

Pairs (4 shown each time, sorted into groups):

- mahogany → **timber**
- ebony → **timber**
- cocoa → **cash crop**
- rubber → **cash crop**
- cassava → **food crop**
- plantain → **food crop**
- crude oil → **mineral**


Three generated variants:

> Match each resource to its type.

Groups: timber · cash crop · food crop · mineral
- rubber → **cash crop**
- ebony → **timber**
- crude oil → **mineral**
- cassava → **food crop**

Full working after a second miss:

> The right pairs are:  
> rubber → cash crop  
> ebony → timber  
> crude oil → mineral  
> cassava → food crop  

> Match each resource to its type.

Groups: cash crop · food crop
- plantain → **food crop**
- cocoa → **cash crop**
- rubber → **cash crop**
- cassava → **food crop**

Full working after a second miss:

> The right pairs are:  
> plantain → food crop  
> cocoa → cash crop  
> rubber → cash crop  
> cassava → food crop  

> Match each resource to its type.

Groups: timber · food crop · mineral
- crude oil → **mineral**
- ebony → **timber**
- plantain → **food crop**
- mahogany → **timber**

Full working after a second miss:

> The right pairs are:  
> crude oil → mineral  
> ebony → timber  
> plantain → food crop  
> mahogany → timber  

Sources: equatorial-zone (The equatorial climate and the exploitation of the equatorial forest (as in Cameroonian Form 2 geography))

### `g2-8-method` · Lesson 8 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is shifting cultivation? | clearing a plot, farming it for a few years, then moving to a new plot | farming one plot for ever · growing crops in glass houses · fishing at sea | That is permanent farming. · That is not it. · That is fishing. | The old plot is left to recover. |
| Which method of exploitation produces timber? | lumbering | fishing · plantation agriculture · mining | Fishing produces fish. · Plantations produce crops. · Mining produces minerals. | Lumbering is cutting trees for timber. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which method of exploitation produces timber?

- ◻️ plantation agriculture  
  _↳ feedback if chosen: Plantations produce crops._
- ◻️ mining  
  _↳ feedback if chosen: Mining produces minerals._
- ◻️ fishing  
  _↳ feedback if chosen: Fishing produces fish._
- ✅ lumbering

Full working after a second miss:

> Lumbering is cutting trees for timber.  
> So the answer is “lumbering”.  

> Which method of exploitation produces timber?

- ◻️ mining  
  _↳ feedback if chosen: Mining produces minerals._
- ✅ lumbering
- ◻️ fishing  
  _↳ feedback if chosen: Fishing produces fish._
- ◻️ plantation agriculture  
  _↳ feedback if chosen: Plantations produce crops._

Full working after a second miss:

> Lumbering is cutting trees for timber.  
> So the answer is “lumbering”.  

> Which method of exploitation produces timber?

- ◻️ mining  
  _↳ feedback if chosen: Mining produces minerals._
- ✅ lumbering
- ◻️ fishing  
  _↳ feedback if chosen: Fishing produces fish._
- ◻️ plantation agriculture  
  _↳ feedback if chosen: Plantations produce crops._

Full working after a second miss:

> Lumbering is cutting trees for timber.  
> So the answer is “lumbering”.  

Sources: equatorial-zone (The equatorial climate and the exploitation of the equatorial forest (as in Cameroonian Form 2 geography))

### `g2-8-resource-card` · Lesson 8 · matching, level 1

Prompt: Match each resource to its type.

Pairs (4 shown each time, sorted into groups):

- mahogany → **timber**
- ebony → **timber**
- cocoa → **cash crop**
- rubber → **cash crop**
- cassava → **food crop**
- plantain → **food crop**
- crude oil → **mineral**


Three generated variants:

> Match each resource to its type.

Groups: timber · cash crop · food crop
- ebony → **timber**
- mahogany → **timber**
- plantain → **food crop**
- cocoa → **cash crop**

Full working after a second miss:

> The right pairs are:  
> ebony → timber  
> mahogany → timber  
> plantain → food crop  
> cocoa → cash crop  

> Match each resource to its type.

Groups: timber · cash crop · food crop · mineral
- mahogany → **timber**
- plantain → **food crop**
- cocoa → **cash crop**
- crude oil → **mineral**

Full working after a second miss:

> The right pairs are:  
> mahogany → timber  
> plantain → food crop  
> cocoa → cash crop  
> crude oil → mineral  

> Match each resource to its type.

Groups: timber · food crop
- ebony → **timber**
- cassava → **food crop**
- plantain → **food crop**
- mahogany → **timber**

Full working after a second miss:

> The right pairs are:  
> ebony → timber  
> cassava → food crop  
> plantain → food crop  
> mahogany → timber  

Sources: equatorial-zone (The equatorial climate and the exploitation of the equatorial forest (as in Cameroonian Form 2 geography))

### `g2-9-problem` · Lesson 9 · multiple choice, level 1

Prompt: Which is a problem faced by people in the equatorial zone?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ leaching of soils by heavy rain
- ✅ dense forest that is hard to clear
- ✅ roads that become muddy in the rains
- ✅ diseases such as malaria
- ❌ very little rain all year  
  _↳ It rains heavily all year._
- ❌ snow blocking the roads  
  _↳ It never snows; it is hot._
- ❌ too few trees  
  _↳ The problem is dense forest, though deforestation is growing._


Three generated variants:

> Which is a problem faced by people in the equatorial zone?

- ✅ diseases such as malaria
- ◻️ very little rain all year  
  _↳ feedback if chosen: It rains heavily all year._
- ◻️ snow blocking the roads  
  _↳ feedback if chosen: It never snows; it is hot._

Full working after a second miss:

> The true statement is “diseases such as malaria”.  
> “very little rain all year” is false: It rains heavily all year.  
> “snow blocking the roads” is false: It never snows; it is hot.  

> Which is a problem faced by people in the equatorial zone?

- ◻️ very little rain all year  
  _↳ feedback if chosen: It rains heavily all year._
- ✅ leaching of soils by heavy rain
- ◻️ snow blocking the roads  
  _↳ feedback if chosen: It never snows; it is hot._

Full working after a second miss:

> The true statement is “leaching of soils by heavy rain”.  
> “very little rain all year” is false: It rains heavily all year.  
> “snow blocking the roads” is false: It never snows; it is hot.  

> Which is a problem faced by people in the equatorial zone?

- ◻️ too few trees  
  _↳ feedback if chosen: The problem is dense forest, though deforestation is growing._
- ◻️ snow blocking the roads  
  _↳ feedback if chosen: It never snows; it is hot._
- ✅ roads that become muddy in the rains

Full working after a second miss:

> The true statement is “roads that become muddy in the rains”.  
> “too few trees” is false: The problem is dense forest, though deforestation is growing.  
> “snow blocking the roads” is false: It never snows; it is hot.  

Sources: equatorial-zone (The equatorial climate and the exploitation of the equatorial forest (as in Cameroonian Form 2 geography))

### `g2-9-match` · Lesson 9 · matching, level 1

Prompt: Match each problem to a solution.

Pairs (4 shown each time):

- muddy, poor roads → **build and maintain roads and bridges**
- leached, poor soils → **use fertilisers and crop rotation**
- deforestation → **replant trees and protect national parks**
- malaria → **use mosquito nets and clear stagnant water**
- crops rotting quickly → **process and preserve crops quickly**


Three generated variants:

> Match each problem to a solution.

Right-hand side (shuffled): replant trees and protect national parks · use fertilisers and crop rotation · process and preserve crops quickly · use mosquito nets and clear stagnant water
- malaria → **use mosquito nets and clear stagnant water**
- deforestation → **replant trees and protect national parks**
- leached, poor soils → **use fertilisers and crop rotation**
- crops rotting quickly → **process and preserve crops quickly**

Full working after a second miss:

> The right pairs are:  
> malaria → use mosquito nets and clear stagnant water  
> deforestation → replant trees and protect national parks  
> leached, poor soils → use fertilisers and crop rotation  
> crops rotting quickly → process and preserve crops quickly  

> Match each problem to a solution.

Right-hand side (shuffled): replant trees and protect national parks · build and maintain roads and bridges · process and preserve crops quickly · use mosquito nets and clear stagnant water
- malaria → **use mosquito nets and clear stagnant water**
- deforestation → **replant trees and protect national parks**
- muddy, poor roads → **build and maintain roads and bridges**
- crops rotting quickly → **process and preserve crops quickly**

Full working after a second miss:

> The right pairs are:  
> malaria → use mosquito nets and clear stagnant water  
> deforestation → replant trees and protect national parks  
> muddy, poor roads → build and maintain roads and bridges  
> crops rotting quickly → process and preserve crops quickly  

> Match each problem to a solution.

Right-hand side (shuffled): use mosquito nets and clear stagnant water · process and preserve crops quickly · use fertilisers and crop rotation · build and maintain roads and bridges
- crops rotting quickly → **process and preserve crops quickly**
- malaria → **use mosquito nets and clear stagnant water**
- leached, poor soils → **use fertilisers and crop rotation**
- muddy, poor roads → **build and maintain roads and bridges**

Full working after a second miss:

> The right pairs are:  
> crops rotting quickly → process and preserve crops quickly  
> malaria → use mosquito nets and clear stagnant water  
> leached, poor soils → use fertilisers and crop rotation  
> muddy, poor roads → build and maintain roads and bridges  

Sources: equatorial-zone (The equatorial climate and the exploitation of the equatorial forest (as in Cameroonian Form 2 geography))

### `g2-9-solve` · Lesson 9 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is leaching? | rain water washing nutrients down out of the soil | wind blowing sand · the soil getting hotter · trees growing faster | That is wind erosion. · That is not it. · That is not it. | Heavy rain carries nutrients down beyond the roots. |
| Why does food rot quickly in the equatorial zone? | The high heat and humidity help moulds and bacteria grow. | It is too cold. · There is no rain. · The air is dry. | It is hot. · It rains a lot. · The air is humid. | Warm, damp conditions speed up decay. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does food rot quickly in the equatorial zone?

- ◻️ It is too cold.  
  _↳ feedback if chosen: It is hot._
- ◻️ The air is dry.  
  _↳ feedback if chosen: The air is humid._
- ◻️ There is no rain.  
  _↳ feedback if chosen: It rains a lot._
- ✅ The high heat and humidity help moulds and bacteria grow.

Full working after a second miss:

> Warm, damp conditions speed up decay.  
> So the answer is “The high heat and humidity help moulds and bacteria grow.”.  

> What is leaching?

- ✅ rain water washing nutrients down out of the soil
- ◻️ the soil getting hotter  
  _↳ feedback if chosen: That is not it._
- ◻️ wind blowing sand  
  _↳ feedback if chosen: That is wind erosion._
- ◻️ trees growing faster  
  _↳ feedback if chosen: That is not it._

Full working after a second miss:

> Heavy rain carries nutrients down beyond the roots.  
> So the answer is “rain water washing nutrients down out of the soil”.  

> Why does food rot quickly in the equatorial zone?

- ◻️ There is no rain.  
  _↳ feedback if chosen: It rains a lot._
- ◻️ It is too cold.  
  _↳ feedback if chosen: It is hot._
- ◻️ The air is dry.  
  _↳ feedback if chosen: The air is humid._
- ✅ The high heat and humidity help moulds and bacteria grow.

Full working after a second miss:

> Warm, damp conditions speed up decay.  
> So the answer is “The high heat and humidity help moulds and bacteria grow.”.  

Sources: equatorial-zone (The equatorial climate and the exploitation of the equatorial forest (as in Cameroonian Form 2 geography))

### `g2-9-spot` · Lesson 9 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Heavy rain causes leaching.
- ✅ Tsetse flies spread sleeping sickness.
- ✅ Replanting trees helps after logging.
- ✅ Roads become muddy in the rains.
- ❌ Cleared equatorial soils stay fertile for ever.  
  _↳ They become poor after a few years because of leaching._
- ❌ Malaria is spread by tsetse flies.  
  _↳ Malaria is spread by mosquitoes._
- ❌ The equatorial zone is cold and dry.  
  _↳ It is hot and wet._


Three generated variants:

> Which statement is wrong?

- ◻️ Tsetse flies spread sleeping sickness.
- ◻️ Replanting trees helps after logging.
- ✅ Cleared equatorial soils stay fertile for ever.  
  _↳ explanation: They become poor after a few years because of leaching._
- ◻️ Roads become muddy in the rains.

Full working after a second miss:

> The wrong statement is “Cleared equatorial soils stay fertile for ever.”.  
> They become poor after a few years because of leaching.  

> Which statement is wrong?

- ◻️ Roads become muddy in the rains.
- ✅ Cleared equatorial soils stay fertile for ever.  
  _↳ explanation: They become poor after a few years because of leaching._
- ◻️ Tsetse flies spread sleeping sickness.
- ◻️ Replanting trees helps after logging.

Full working after a second miss:

> The wrong statement is “Cleared equatorial soils stay fertile for ever.”.  
> They become poor after a few years because of leaching.  

> Which statement is wrong?

- ◻️ Tsetse flies spread sleeping sickness.
- ◻️ Replanting trees helps after logging.
- ✅ Malaria is spread by tsetse flies.  
  _↳ explanation: Malaria is spread by mosquitoes._
- ◻️ Heavy rain causes leaching.

Full working after a second miss:

> The wrong statement is “Malaria is spread by tsetse flies.”.  
> Malaria is spread by mosquitoes.  

Sources: equatorial-zone (The equatorial climate and the exploitation of the equatorial forest (as in Cameroonian Form 2 geography))

### `g2-9-solve-card` · Lesson 9 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is leaching? | rain water washing nutrients down out of the soil | wind blowing sand · the soil getting hotter · trees growing faster | That is wind erosion. · That is not it. · That is not it. | Heavy rain carries nutrients down beyond the roots. |
| Why does food rot quickly in the equatorial zone? | The high heat and humidity help moulds and bacteria grow. | It is too cold. · There is no rain. · The air is dry. | It is hot. · It rains a lot. · The air is humid. | Warm, damp conditions speed up decay. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why does food rot quickly in the equatorial zone?

- ✅ The high heat and humidity help moulds and bacteria grow.
- ◻️ The air is dry.  
  _↳ feedback if chosen: The air is humid._
- ◻️ It is too cold.  
  _↳ feedback if chosen: It is hot._
- ◻️ There is no rain.  
  _↳ feedback if chosen: It rains a lot._

Full working after a second miss:

> Warm, damp conditions speed up decay.  
> So the answer is “The high heat and humidity help moulds and bacteria grow.”.  

> Why does food rot quickly in the equatorial zone?

- ◻️ It is too cold.  
  _↳ feedback if chosen: It is hot._
- ◻️ The air is dry.  
  _↳ feedback if chosen: The air is humid._
- ◻️ There is no rain.  
  _↳ feedback if chosen: It rains a lot._
- ✅ The high heat and humidity help moulds and bacteria grow.

Full working after a second miss:

> Warm, damp conditions speed up decay.  
> So the answer is “The high heat and humidity help moulds and bacteria grow.”.  

> What is leaching?

- ◻️ the soil getting hotter  
  _↳ feedback if chosen: That is not it._
- ✅ rain water washing nutrients down out of the soil
- ◻️ wind blowing sand  
  _↳ feedback if chosen: That is wind erosion._
- ◻️ trees growing faster  
  _↳ feedback if chosen: That is not it._

Full working after a second miss:

> Heavy rain carries nutrients down beyond the roots.  
> So the answer is “rain water washing nutrients down out of the soil”.  

Sources: equatorial-zone (The equatorial climate and the exploitation of the equatorial forest (as in Cameroonian Form 2 geography))

### `g2-10-cause` · Lesson 10 · matching, level 1

Prompt: Sort: cause or consequence of deforestation?

Pairs (4 shown each time, sorted into groups):

- logging for timber → **cause**
- clearing land for farms → **cause**
- cutting firewood → **cause**
- mining → **cause**
- soil erosion → **consequence**
- loss of wildlife → **consequence**
- rivers silting up → **consequence**
- climate change → **consequence**


Three generated variants:

> Sort: cause or consequence of deforestation?

Groups: cause · consequence
- climate change → **consequence**
- clearing land for farms → **cause**
- soil erosion → **consequence**
- logging for timber → **cause**

Full working after a second miss:

> The right pairs are:  
> climate change → consequence  
> clearing land for farms → cause  
> soil erosion → consequence  
> logging for timber → cause  

> Sort: cause or consequence of deforestation?

Groups: cause · consequence
- logging for timber → **cause**
- soil erosion → **consequence**
- loss of wildlife → **consequence**
- climate change → **consequence**

Full working after a second miss:

> The right pairs are:  
> logging for timber → cause  
> soil erosion → consequence  
> loss of wildlife → consequence  
> climate change → consequence  

> Sort: cause or consequence of deforestation?

Groups: cause · consequence
- clearing land for farms → **cause**
- rivers silting up → **consequence**
- logging for timber → **cause**
- mining → **cause**

Full working after a second miss:

> The right pairs are:  
> clearing land for farms → cause  
> rivers silting up → consequence  
> logging for timber → cause  
> mining → cause  

Sources: cameroon-regions (Areas of Cameroon's ten regions (km²) and rounded population estimates; deforestation in Cameroon; protected areas Dja, Lobéké, Korup)

### `g2-10-see` · Lesson 10 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which is a sign (manifestation) of deforestation? | timber lorries and shrinking forest | more large trees · more gorillas · clearer rivers | There are fewer. · Wildlife declines. · Rivers silt up. | These show forest being removed. |
| Why does deforestation contribute to climate change? | Trees store carbon; when they are cut and burned, carbon dioxide is released. | Trees make the Earth colder at night only. · Cutting trees makes rain heavier everywhere. · Forests have nothing to do with climate. | That is not the reason. · It often reduces rain locally. · Forests strongly affect climate. | Lost forests release carbon dioxide. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is a sign (manifestation) of deforestation?

- ◻️ more large trees  
  _↳ feedback if chosen: There are fewer._
- ◻️ more gorillas  
  _↳ feedback if chosen: Wildlife declines._
- ✅ timber lorries and shrinking forest
- ◻️ clearer rivers  
  _↳ feedback if chosen: Rivers silt up._

Full working after a second miss:

> These show forest being removed.  
> So the answer is “timber lorries and shrinking forest”.  

> Why does deforestation contribute to climate change?

- ◻️ Forests have nothing to do with climate.  
  _↳ feedback if chosen: Forests strongly affect climate._
- ◻️ Trees make the Earth colder at night only.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ Cutting trees makes rain heavier everywhere.  
  _↳ feedback if chosen: It often reduces rain locally._
- ✅ Trees store carbon; when they are cut and burned, carbon dioxide is released.

Full working after a second miss:

> Lost forests release carbon dioxide.  
> So the answer is “Trees store carbon; when they are cut and burned, carbon dioxide is released.”.  

> Why does deforestation contribute to climate change?

- ◻️ Cutting trees makes rain heavier everywhere.  
  _↳ feedback if chosen: It often reduces rain locally._
- ◻️ Trees make the Earth colder at night only.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ Forests have nothing to do with climate.  
  _↳ feedback if chosen: Forests strongly affect climate._
- ✅ Trees store carbon; when they are cut and burned, carbon dioxide is released.

Full working after a second miss:

> Lost forests release carbon dioxide.  
> So the answer is “Trees store carbon; when they are cut and burned, carbon dioxide is released.”.  

Sources: cameroon-regions (Areas of Cameroon's ten regions (km²) and rounded population estimates; deforestation in Cameroon; protected areas Dja, Lobéké, Korup)

### `g2-10-solve` · Lesson 10 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which is a protected area in Cameroon? | the Dja reserve | Douala port · the Sahara · Lake Chad's dry bed | That is a port. · That is not in Cameroon. · That is not a forest reserve. | Dja, Lobéké and Korup protect forests. |
| How do improved stoves help the forest? | They use less firewood. | They burn more wood. · They plant trees. · They stop logging companies. | They use less. · Stoves do not plant trees. · They do not affect logging. | Less fuelwood means fewer trees cut. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which is a protected area in Cameroon?

- ◻️ the Sahara  
  _↳ feedback if chosen: That is not in Cameroon._
- ✅ the Dja reserve
- ◻️ Lake Chad's dry bed  
  _↳ feedback if chosen: That is not a forest reserve._
- ◻️ Douala port  
  _↳ feedback if chosen: That is a port._

Full working after a second miss:

> Dja, Lobéké and Korup protect forests.  
> So the answer is “the Dja reserve”.  

> Which is a protected area in Cameroon?

- ✅ the Dja reserve
- ◻️ Douala port  
  _↳ feedback if chosen: That is a port._
- ◻️ the Sahara  
  _↳ feedback if chosen: That is not in Cameroon._
- ◻️ Lake Chad's dry bed  
  _↳ feedback if chosen: That is not a forest reserve._

Full working after a second miss:

> Dja, Lobéké and Korup protect forests.  
> So the answer is “the Dja reserve”.  

> Which is a protected area in Cameroon?

- ✅ the Dja reserve
- ◻️ Douala port  
  _↳ feedback if chosen: That is a port._
- ◻️ Lake Chad's dry bed  
  _↳ feedback if chosen: That is not a forest reserve._
- ◻️ the Sahara  
  _↳ feedback if chosen: That is not in Cameroon._

Full working after a second miss:

> Dja, Lobéké and Korup protect forests.  
> So the answer is “the Dja reserve”.  

Sources: cameroon-regions (Areas of Cameroon's ten regions (km²) and rounded population estimates; deforestation in Cameroon; protected areas Dja, Lobéké, Korup)

### `g2-10-spot` · Lesson 10 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Logging causes deforestation.
- ✅ Reforestation helps the forest recover.
- ✅ Deforestation threatens gorillas.
- ✅ Bush fires destroy forest.
- ❌ Deforestation reduces soil erosion.  
  _↳ Deforestation increases soil erosion._
- ❌ National parks speed up deforestation.  
  _↳ Parks protect the forest._
- ❌ Cutting trees increases biodiversity.  
  _↳ It reduces biodiversity._


Three generated variants:

> Which statement is wrong?

- ◻️ Deforestation threatens gorillas.
- ◻️ Logging causes deforestation.
- ◻️ Reforestation helps the forest recover.
- ✅ Cutting trees increases biodiversity.  
  _↳ explanation: It reduces biodiversity._

Full working after a second miss:

> The wrong statement is “Cutting trees increases biodiversity.”.  
> It reduces biodiversity.  

> Which statement is wrong?

- ◻️ Deforestation threatens gorillas.
- ◻️ Reforestation helps the forest recover.
- ✅ Cutting trees increases biodiversity.  
  _↳ explanation: It reduces biodiversity._
- ◻️ Bush fires destroy forest.

Full working after a second miss:

> The wrong statement is “Cutting trees increases biodiversity.”.  
> It reduces biodiversity.  

> Which statement is wrong?

- ◻️ Logging causes deforestation.
- ✅ Cutting trees increases biodiversity.  
  _↳ explanation: It reduces biodiversity._
- ◻️ Reforestation helps the forest recover.
- ◻️ Bush fires destroy forest.

Full working after a second miss:

> The wrong statement is “Cutting trees increases biodiversity.”.  
> It reduces biodiversity.  

Sources: cameroon-regions (Areas of Cameroon's ten regions (km²) and rounded population estimates; deforestation in Cameroon; protected areas Dja, Lobéké, Korup)

### `g2-10-solve-card` · Lesson 10 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which is a protected area in Cameroon? | the Dja reserve | Douala port · the Sahara · Lake Chad's dry bed | That is a port. · That is not in Cameroon. · That is not a forest reserve. | Dja, Lobéké and Korup protect forests. |
| How do improved stoves help the forest? | They use less firewood. | They burn more wood. · They plant trees. · They stop logging companies. | They use less. · Stoves do not plant trees. · They do not affect logging. | Less fuelwood means fewer trees cut. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How do improved stoves help the forest?

- ◻️ They plant trees.  
  _↳ feedback if chosen: Stoves do not plant trees._
- ◻️ They burn more wood.  
  _↳ feedback if chosen: They use less._
- ◻️ They stop logging companies.  
  _↳ feedback if chosen: They do not affect logging._
- ✅ They use less firewood.

Full working after a second miss:

> Less fuelwood means fewer trees cut.  
> So the answer is “They use less firewood.”.  

> Which is a protected area in Cameroon?

- ◻️ Douala port  
  _↳ feedback if chosen: That is a port._
- ✅ the Dja reserve
- ◻️ the Sahara  
  _↳ feedback if chosen: That is not in Cameroon._
- ◻️ Lake Chad's dry bed  
  _↳ feedback if chosen: That is not a forest reserve._

Full working after a second miss:

> Dja, Lobéké and Korup protect forests.  
> So the answer is “the Dja reserve”.  

> How do improved stoves help the forest?

- ◻️ They stop logging companies.  
  _↳ feedback if chosen: They do not affect logging._
- ◻️ They plant trees.  
  _↳ feedback if chosen: Stoves do not plant trees._
- ✅ They use less firewood.
- ◻️ They burn more wood.  
  _↳ feedback if chosen: They use less._

Full working after a second miss:

> Less fuelwood means fewer trees cut.  
> So the answer is “They use less firewood.”.  

Sources: cameroon-regions (Areas of Cameroon's ten regions (km²) and rounded population estimates; deforestation in Cameroon; protected areas Dja, Lobéké, Korup)

