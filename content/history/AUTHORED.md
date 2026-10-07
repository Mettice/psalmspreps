# History Form 1, Batch Y1: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:history`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: rules and the table the computed answers use (src/engine/lib/history.js)

- **Writing years (TR-Y01)**: 500 BC, 1 BC, AD 1, AD 476, AD 2026; there is no year 0 (1 BC is followed by AD 1).
- **Years between (TR-Y01)**: same era, subtract; across BC and AD, add and take away 1: AD 1884 → AD 1961: 77; 500 BC → 200 BC: 300; 50 BC → AD 50: 99; 1 BC → AD 1: 1.
- **Centuries (TR-Y01)**: AD 111 → 2nd century AD; AD 1884 → 19th century AD; AD 1900 → 19th century AD; AD 1901 → 20th century AD; AD 2026 → 21st century AD; 500 BC → 5th century BC; 501 BC → 6th century BC.

**Early humans (TR-Y03)**, oldest first (estimates; only the order and these rounded dates are used):

| Name | First appears | Known for | Important finds |
|---|---|---|---|
| Sahelanthropus tchadensis (Toumaï) | about 7 million years ago | one of the oldest known ancestors, found in Chad | Chad |
| Australopithecus (“Lucy”) | about 3.2 million years ago | walked upright on two legs, with a small brain | Ethiopia |
| Homo habilis | about 2.4 million years ago | “handy man”: made the first simple stone tools | Tanzania (Olduvai Gorge) |
| Homo erectus | about 1.9 million years ago | “upright man”: used fire and travelled out of Africa | Kenya |
| Homo sapiens | about 300 000 years ago | “wise man”: modern humans, like us | Morocco and Ethiopia |

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `hi1-source` | 1 | multiple choice, 1 | history-intro |
| 2 | `hi1-why` | 1 | multiple choice, 1 | history-intro |
| 3 | `hi1-sort` | 1 | matching, 2 | history-intro |
| 4 | `hi1-prehistory` | 1 | multiple choice, 2 | history-intro |
| 5 | `hi1-spot` | 1 | spot the error, 3 | history-intro |
| 6 | `hic1-1-check` (card hic1-1) | 1 | multiple choice, 1 | history-intro |
| 7 | `hi2-which` | 2 | multiple choice, 1 | relics |
| 8 | `hi2-use` | 2 | matching, 1 | relics |
| 9 | `hi2-material` | 2 | matching, 2 | relics |
| 10 | `hi2-care` | 2 | multiple choice, 2 | relics |
| 11 | `hi2-spot` | 2 | spot the error, 3 | relics |
| 12 | `hic2-3-check` (card hic2-3) | 2 | multiple choice, 1 | relics |
| 13 | `hi4-place` | 4 | multiple choice, 1 | early-humans |
| 14 | `hi4-fossil` | 4 | multiple choice, 1 | early-humans |
| 15 | `hi4-cradle` | 4 | multiple choice, 2 | early-humans |
| 16 | `hi4-water` | 4 | multiple choice, 2 | early-humans |
| 17 | `hi4-spot` | 4 | spot the error, 3 | early-humans |
| 18 | `hic4-3-check` (card hic4-3) | 4 | multiple choice, 1 | early-humans |
| 19 | `hi5-life` | 5 | multiple choice, 1 | early-humans |
| 20 | `hi5-tool` | 5 | multiple choice, 1 | early-humans |
| 21 | `hi5-fire` | 5 | multiple choice, 1 | early-humans |
| 22 | `hi5-sort` | 5 | matching, 2 | early-humans, stone-age |
| 23 | `hi5-spot` | 5 | spot the error, 3 | early-humans |
| 24 | `hi6-what` | 6 | multiple choice, 1 | creation-myths |
| 25 | `hi6-passed` | 6 | multiple choice, 1 | creation-myths |
| 26 | `hi6-sort` | 6 | matching, 2 | creation-myths |
| 27 | `hi6-respect` | 6 | multiple choice, 2 | creation-myths |
| 28 | `hi6-spot` | 6 | spot the error, 3 | creation-myths |
| 29 | `hic6-3-check` (card hic6-3) | 6 | multiple choice, 1 | creation-myths |
| 30 | `hi7-sort` | 7 | matching, 1 | stone-age |
| 31 | `hi7-new` | 7 | multiple choice, 1 | stone-age |
| 32 | `hi7-why` | 7 | multiple choice, 2 | stone-age |
| 33 | `hi7-when` | 7 | multiple choice, 2 | stone-age |
| 34 | `hi7-spot` | 7 | spot the error, 3 | stone-age |
| 35 | `hic7-3-check` (card hic7-3) | 7 | multiple choice, 1 | stone-age |
| 36 | `hi8-order` | 8 | ordering, 1 | early-humans |
| 37 | `hi8-name` | 8 | multiple choice, 1 | early-humans |
| 38 | `hi8-older` | 8 | multiple choice, 2 | early-humans |
| 39 | `hi8-when` | 8 | multiple choice, 2 | early-humans |
| 40 | `hi8-spot` | 8 | spot the error, 3 | early-humans |
| 41 | `hic8-3-check` (card hic8-3) | 8 | multiple choice, 1 | early-humans |
| 42 | `hi9-where` | 9 | multiple choice, 1 | cameroon-neolithic |
| 43 | `hi9-find` | 9 | multiple choice, 1 | cameroon-neolithic |
| 44 | `hi9-show` | 9 | multiple choice, 2 | cameroon-neolithic |
| 45 | `hi9-sort` | 9 | matching, 2 | cameroon-neolithic, stone-age |
| 46 | `hi9-spot` | 9 | spot the error, 3 | cameroon-neolithic |
| 47 | `hic9-3-check` (card hic9-3) | 9 | multiple choice, 1 | cameroon-neolithic |
| 48 | `hi10-where` | 10 | multiple choice, 1 | forest-peoples |
| 49 | `hi10-life` | 10 | multiple choice, 1 | forest-peoples |
| 50 | `hi10-name` | 10 | multiple choice, 2 | forest-peoples |
| 51 | `hi10-sort` | 10 | matching, 2 | forest-peoples |
| 52 | `hi10-spot` | 10 | spot the error, 3 | forest-peoples |
| 53 | `hic10-3-check` (card hic10-3) | 10 | multiple choice, 1 | forest-peoples |

### `hi1-source` · Lesson 1 · multiple choice, level 1

Prompt: What kind of source is this: {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| a story about the founding of the village, told by an elder | an oral source | An oral source: a story about the founding of the village, told by an elder. |
| a song a griot sings about a past king | an oral source | An oral source: a song a griot sings about a past king. |
| a proverb passed down from grandparents | an oral source | An oral source: a proverb passed down from grandparents. |
| an old letter written by a missionary | a written source | A written source: an old letter written by a missionary. |
| a newspaper from 1960 | a written source | A written source: a newspaper from 1960. |
| a school register from the colonial period | a written source | A written source: a school register from the colonial period. |
| a clay pot dug up by archaeologists | a material source | A material source: a clay pot dug up by archaeologists. |
| an old stone axe | a material source | A material source: an old stone axe. |
| the ruins of an old palace | a material source | A material source: the ruins of an old palace. |

Right answer: `{x.a}`; wrong choices: `an oral source`, `a written source`, `a material source`

- Feedback `other`: “Not that kind. Is it spoken, written, or an object?”

Three generated variants:

> What kind of source is this: a proverb passed down from grandparents?

- ✅ an oral source
- ◻️ a written source  
  _↳ feedback if chosen: Not that kind. Is it spoken, written, or an object?_
- ◻️ a material source  
  _↳ feedback if chosen: Not that kind. Is it spoken, written, or an object?_

Full working after a second miss:

> An oral source: a proverb passed down from grandparents.  
> Answer: an oral source.  

> What kind of source is this: a story about the founding of the village, told by an elder?

- ✅ an oral source
- ◻️ a written source  
  _↳ feedback if chosen: Not that kind. Is it spoken, written, or an object?_
- ◻️ a material source  
  _↳ feedback if chosen: Not that kind. Is it spoken, written, or an object?_

Full working after a second miss:

> An oral source: a story about the founding of the village, told by an elder.  
> Answer: an oral source.  

> What kind of source is this: a story about the founding of the village, told by an elder?

- ✅ an oral source
- ◻️ a written source  
  _↳ feedback if chosen: Not that kind. Is it spoken, written, or an object?_
- ◻️ a material source  
  _↳ feedback if chosen: Not that kind. Is it spoken, written, or an object?_

Full working after a second miss:

> An oral source: a story about the founding of the village, told by an elder.  
> Answer: an oral source.  

Sources: history-intro (What history is; oral, written and material sources; prehistory)

### `hi1-why` · Lesson 1 · multiple choice, level 1

Prompt: Which is a good reason to study history?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ to understand how our community came to be
- ✅ to learn from the mistakes of the past
- ✅ to keep our heritage alive
- ✅ to respect other peoples
- ❌ to know exactly what will happen tomorrow  
  _↳ History studies the past; it cannot tell the future exactly._
- ❌ to forget the past  
  _↳ History helps us remember the past._
- ❌ only to pass examinations  
  _↳ History is useful in life, not only for examinations._
- ❌ to learn how to repair cars  
  _↳ That is mechanics._


Three generated variants:

> Which is a good reason to study history?

- ◻️ only to pass examinations  
  _↳ feedback if chosen: History is useful in life, not only for examinations._
- ✅ to learn from the mistakes of the past
- ◻️ to learn how to repair cars  
  _↳ feedback if chosen: That is mechanics._
- ◻️ to forget the past  
  _↳ feedback if chosen: History helps us remember the past._

Full working after a second miss:

> The true statement is “to learn from the mistakes of the past”.  
> “only to pass examinations” is false: History is useful in life, not only for examinations.  
> “to learn how to repair cars” is false: That is mechanics.  
> “to forget the past” is false: History helps us remember the past.  

> Which is a good reason to study history?

- ◻️ to know exactly what will happen tomorrow  
  _↳ feedback if chosen: History studies the past; it cannot tell the future exactly._
- ◻️ to learn how to repair cars  
  _↳ feedback if chosen: That is mechanics._
- ✅ to understand how our community came to be
- ◻️ only to pass examinations  
  _↳ feedback if chosen: History is useful in life, not only for examinations._

Full working after a second miss:

> The true statement is “to understand how our community came to be”.  
> “to know exactly what will happen tomorrow” is false: History studies the past; it cannot tell the future exactly.  
> “to learn how to repair cars” is false: That is mechanics.  
> “only to pass examinations” is false: History is useful in life, not only for examinations.  

> Which is a good reason to study history?

- ✅ to respect other peoples
- ◻️ to know exactly what will happen tomorrow  
  _↳ feedback if chosen: History studies the past; it cannot tell the future exactly._
- ◻️ to learn how to repair cars  
  _↳ feedback if chosen: That is mechanics._
- ◻️ to forget the past  
  _↳ feedback if chosen: History helps us remember the past._

Full working after a second miss:

> The true statement is “to respect other peoples”.  
> “to know exactly what will happen tomorrow” is false: History studies the past; it cannot tell the future exactly.  
> “to learn how to repair cars” is false: That is mechanics.  
> “to forget the past” is false: History helps us remember the past.  

Sources: history-intro (What history is; oral, written and material sources; prehistory)

### `hi1-sort` · Lesson 1 · matching, level 2

Prompt: Sort these sources: oral, written or material?

Pairs (6 shown each time, sorted into groups):

- a story told by an elder → **oral**
- a griot’s song → **oral**
- a proverb → **oral**
- an old letter → **written**
- a newspaper → **written**
- a stone inscription with writing → **written**
- a stone axe → **material**
- a clay pot → **material**
- old coins → **material**


Three generated variants:

> Sort these sources: oral, written or material?

Groups: oral · written · material
- a stone axe → **material**
- a stone inscription with writing → **written**
- a newspaper → **written**
- a proverb → **oral**
- old coins → **material**
- a griot’s song → **oral**

Full working after a second miss:

> The right pairs are:  
> a stone axe → material  
> a stone inscription with writing → written  
> a newspaper → written  
> a proverb → oral  
> old coins → material  
> a griot’s song → oral  

> Sort these sources: oral, written or material?

Groups: oral · written · material
- a newspaper → **written**
- a clay pot → **material**
- a griot’s song → **oral**
- old coins → **material**
- a story told by an elder → **oral**
- an old letter → **written**

Full working after a second miss:

> The right pairs are:  
> a newspaper → written  
> a clay pot → material  
> a griot’s song → oral  
> old coins → material  
> a story told by an elder → oral  
> an old letter → written  

> Sort these sources: oral, written or material?

Groups: oral · written · material
- a proverb → **oral**
- a stone axe → **material**
- a clay pot → **material**
- a stone inscription with writing → **written**
- an old letter → **written**
- a story told by an elder → **oral**

Full working after a second miss:

> The right pairs are:  
> a proverb → oral  
> a stone axe → material  
> a clay pot → material  
> a stone inscription with writing → written  
> an old letter → written  
> a story told by an elder → oral  

Sources: history-intro (What history is; oral, written and material sources; prehistory)

### `hi1-prehistory` · Lesson 1 · multiple choice, level 2

Prompt: Why do we learn about prehistory mainly from material sources?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ People had not yet invented writing.
- ❌ Nobody lived in prehistoric times.  
  _↳ People lived then; they simply did not write._
- ❌ Oral sources are always false.  
  _↳ Oral sources are useful, but memories do not reach back that far._
- ❌ Material sources are the easiest to read.  
  _↳ The reason is that there was no writing._
- ❌ Historians do not like books.  
  _↳ Books did not exist then: there was no writing._


Three generated variants:

> Why do we learn about prehistory mainly from material sources?

- ✅ People had not yet invented writing.
- ◻️ Material sources are the easiest to read.  
  _↳ feedback if chosen: The reason is that there was no writing._
- ◻️ Nobody lived in prehistoric times.  
  _↳ feedback if chosen: People lived then; they simply did not write._
- ◻️ Historians do not like books.  
  _↳ feedback if chosen: Books did not exist then: there was no writing._

Full working after a second miss:

> The true statement is “People had not yet invented writing.”.  
> “Material sources are the easiest to read.” is false: The reason is that there was no writing.  
> “Nobody lived in prehistoric times.” is false: People lived then; they simply did not write.  
> “Historians do not like books.” is false: Books did not exist then: there was no writing.  

> Why do we learn about prehistory mainly from material sources?

- ◻️ Nobody lived in prehistoric times.  
  _↳ feedback if chosen: People lived then; they simply did not write._
- ◻️ Material sources are the easiest to read.  
  _↳ feedback if chosen: The reason is that there was no writing._
- ✅ People had not yet invented writing.
- ◻️ Historians do not like books.  
  _↳ feedback if chosen: Books did not exist then: there was no writing._

Full working after a second miss:

> The true statement is “People had not yet invented writing.”.  
> “Nobody lived in prehistoric times.” is false: People lived then; they simply did not write.  
> “Material sources are the easiest to read.” is false: The reason is that there was no writing.  
> “Historians do not like books.” is false: Books did not exist then: there was no writing.  

> Why do we learn about prehistory mainly from material sources?

- ◻️ Nobody lived in prehistoric times.  
  _↳ feedback if chosen: People lived then; they simply did not write._
- ◻️ Material sources are the easiest to read.  
  _↳ feedback if chosen: The reason is that there was no writing._
- ◻️ Oral sources are always false.  
  _↳ feedback if chosen: Oral sources are useful, but memories do not reach back that far._
- ✅ People had not yet invented writing.

Full working after a second miss:

> The true statement is “People had not yet invented writing.”.  
> “Nobody lived in prehistoric times.” is false: People lived then; they simply did not write.  
> “Material sources are the easiest to read.” is false: The reason is that there was no writing.  
> “Oral sources are always false.” is false: Oral sources are useful, but memories do not reach back that far.  

Sources: history-intro (What history is; oral, written and material sources; prehistory)

### `hi1-spot` · Lesson 1 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ History studies the past using evidence.
- ✅ A griot’s song is an oral source.
- ✅ Archaeologists dig up material sources.
- ✅ Prehistory is the time before writing.
- ❌ A newspaper is a material source.  
  _↳ A newspaper is a written source._
- ❌ Oral sources are written down in books.  
  _↳ Oral sources are passed on by word of mouth._
- ❌ History is the study of the future.  
  _↳ History is the study of the past._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Prehistory is the time before writing.
- ◻️ A griot’s song is an oral source.
- ◻️ History studies the past using evidence.
- ✅ History is the study of the future.  
  _↳ explanation: History is the study of the past._

Full working after a second miss:

> The wrong statement is “History is the study of the future.”.  
> History is the study of the past.  

> One sentence is wrong. Which one?

- ◻️ History studies the past using evidence.
- ◻️ Archaeologists dig up material sources.
- ✅ A newspaper is a material source.  
  _↳ explanation: A newspaper is a written source._
- ◻️ Prehistory is the time before writing.

Full working after a second miss:

> The wrong statement is “A newspaper is a material source.”.  
> A newspaper is a written source.  

> One sentence is wrong. Which one?

- ✅ History is the study of the future.  
  _↳ explanation: History is the study of the past._
- ◻️ A griot’s song is an oral source.
- ◻️ Archaeologists dig up material sources.
- ◻️ Prehistory is the time before writing.

Full working after a second miss:

> The wrong statement is “History is the study of the future.”.  
> History is the study of the past.  

Sources: history-intro (What history is; oral, written and material sources; prehistory)

### `hic1-1-check` · Lesson 1 · multiple choice, level 1

Prompt: What is history?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ the study of the past, based on evidence
- ❌ the study of the stars  
  _↳ That is astronomy._
- ❌ the study of plants  
  _↳ That is botany, part of Biology._
- ❌ guessing about the future  
  _↳ History studies the past._
- ❌ the study of numbers  
  _↳ That is Mathematics._


Three generated variants:

> What is history?

- ◻️ the study of numbers  
  _↳ feedback if chosen: That is Mathematics._
- ✅ the study of the past, based on evidence
- ◻️ the study of plants  
  _↳ feedback if chosen: That is botany, part of Biology._
- ◻️ guessing about the future  
  _↳ feedback if chosen: History studies the past._

Full working after a second miss:

> The true statement is “the study of the past, based on evidence”.  
> “the study of numbers” is false: That is Mathematics.  
> “the study of plants” is false: That is botany, part of Biology.  
> “guessing about the future” is false: History studies the past.  

> What is history?

- ◻️ the study of the stars  
  _↳ feedback if chosen: That is astronomy._
- ◻️ the study of numbers  
  _↳ feedback if chosen: That is Mathematics._
- ◻️ the study of plants  
  _↳ feedback if chosen: That is botany, part of Biology._
- ✅ the study of the past, based on evidence

Full working after a second miss:

> The true statement is “the study of the past, based on evidence”.  
> “the study of the stars” is false: That is astronomy.  
> “the study of numbers” is false: That is Mathematics.  
> “the study of plants” is false: That is botany, part of Biology.  

> What is history?

- ◻️ the study of the stars  
  _↳ feedback if chosen: That is astronomy._
- ✅ the study of the past, based on evidence
- ◻️ the study of plants  
  _↳ feedback if chosen: That is botany, part of Biology._
- ◻️ the study of numbers  
  _↳ feedback if chosen: That is Mathematics._

Full working after a second miss:

> The true statement is “the study of the past, based on evidence”.  
> “the study of the stars” is false: That is astronomy.  
> “the study of plants” is false: That is botany, part of Biology.  
> “the study of numbers” is false: That is Mathematics.  

Sources: history-intro (What history is; oral, written and material sources; prehistory)

### `hi2-which` · Lesson 2 · multiple choice, level 1

Prompt: Which of these is a historical relic?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ an old iron hoe
- ✅ a clay pot from a past generation
- ✅ an old cowrie-shell necklace
- ✅ a stone axe
- ❌ a new plastic bucket  
  _↳ It is new: it does not come from the past._
- ❌ a mobile phone bought this year  
  _↳ It is new._
- ❌ a song on the radio today  
  _↳ A relic is an object from the past._
- ❌ this morning’s bread  
  _↳ A relic is an object that has survived from the past._


Three generated variants:

> Which of these is a historical relic?

- ✅ an old iron hoe
- ◻️ a mobile phone bought this year  
  _↳ feedback if chosen: It is new._
- ◻️ this morning’s bread  
  _↳ feedback if chosen: A relic is an object that has survived from the past._
- ◻️ a new plastic bucket  
  _↳ feedback if chosen: It is new: it does not come from the past._

Full working after a second miss:

> The true statement is “an old iron hoe”.  
> “a mobile phone bought this year” is false: It is new.  
> “this morning’s bread” is false: A relic is an object that has survived from the past.  
> “a new plastic bucket” is false: It is new: it does not come from the past.  

> Which of these is a historical relic?

- ✅ an old cowrie-shell necklace
- ◻️ a song on the radio today  
  _↳ feedback if chosen: A relic is an object from the past._
- ◻️ this morning’s bread  
  _↳ feedback if chosen: A relic is an object that has survived from the past._
- ◻️ a mobile phone bought this year  
  _↳ feedback if chosen: It is new._

Full working after a second miss:

> The true statement is “an old cowrie-shell necklace”.  
> “a song on the radio today” is false: A relic is an object from the past.  
> “this morning’s bread” is false: A relic is an object that has survived from the past.  
> “a mobile phone bought this year” is false: It is new.  

> Which of these is a historical relic?

- ◻️ a song on the radio today  
  _↳ feedback if chosen: A relic is an object from the past._
- ◻️ a mobile phone bought this year  
  _↳ feedback if chosen: It is new._
- ✅ an old iron hoe
- ◻️ a new plastic bucket  
  _↳ feedback if chosen: It is new: it does not come from the past._

Full working after a second miss:

> The true statement is “an old iron hoe”.  
> “a song on the radio today” is false: A relic is an object from the past.  
> “a mobile phone bought this year” is false: It is new.  
> “a new plastic bucket” is false: It is new: it does not come from the past.  

Sources: relics (Historical relics: collecting, labelling, caring for and classifying them)

### `hi2-use` · Lesson 2 · matching, level 1

Prompt: Classify these relics by their use.

Pairs (6 shown each time, sorted into groups):

- an iron hoe → **farming**
- a cutlass → **farming**
- a wooden digging stick → **farming**
- a clay cooking pot → **cooking**
- a grinding stone → **cooking**
- a wooden mortar → **cooking**
- a spear → **hunting or war**
- a bow and arrows → **hunting or war**
- a shield → **hunting or war**


Three generated variants:

> Classify these relics by their use.

Groups: farming · cooking · hunting or war
- a shield → **hunting or war**
- a grinding stone → **cooking**
- a wooden mortar → **cooking**
- a bow and arrows → **hunting or war**
- a wooden digging stick → **farming**
- a clay cooking pot → **cooking**

Full working after a second miss:

> The right pairs are:  
> a shield → hunting or war  
> a grinding stone → cooking  
> a wooden mortar → cooking  
> a bow and arrows → hunting or war  
> a wooden digging stick → farming  
> a clay cooking pot → cooking  

> Classify these relics by their use.

Groups: farming · cooking · hunting or war
- a cutlass → **farming**
- a clay cooking pot → **cooking**
- a bow and arrows → **hunting or war**
- a shield → **hunting or war**
- an iron hoe → **farming**
- a wooden digging stick → **farming**

Full working after a second miss:

> The right pairs are:  
> a cutlass → farming  
> a clay cooking pot → cooking  
> a bow and arrows → hunting or war  
> a shield → hunting or war  
> an iron hoe → farming  
> a wooden digging stick → farming  

> Classify these relics by their use.

Groups: farming · cooking · hunting or war
- an iron hoe → **farming**
- a grinding stone → **cooking**
- a wooden mortar → **cooking**
- a spear → **hunting or war**
- a cutlass → **farming**
- a shield → **hunting or war**

Full working after a second miss:

> The right pairs are:  
> an iron hoe → farming  
> a grinding stone → cooking  
> a wooden mortar → cooking  
> a spear → hunting or war  
> a cutlass → farming  
> a shield → hunting or war  

Sources: relics (Historical relics: collecting, labelling, caring for and classifying them)

### `hi2-material` · Lesson 2 · matching, level 2

Prompt: Classify these relics by material.

Pairs (5 shown each time, sorted into groups):

- a grinding stone → **stone**
- a stone axe → **stone**
- a clay pot → **clay**
- a clay pipe → **clay**
- an iron hoe → **metal**
- a bronze bell → **metal**


Three generated variants:

> Classify these relics by material.

Groups: stone · clay · metal
- a clay pot → **clay**
- a bronze bell → **metal**
- a stone axe → **stone**
- a clay pipe → **clay**
- a grinding stone → **stone**

Full working after a second miss:

> The right pairs are:  
> a clay pot → clay  
> a bronze bell → metal  
> a stone axe → stone  
> a clay pipe → clay  
> a grinding stone → stone  

> Classify these relics by material.

Groups: stone · clay · metal
- a clay pipe → **clay**
- a clay pot → **clay**
- a bronze bell → **metal**
- a stone axe → **stone**
- an iron hoe → **metal**

Full working after a second miss:

> The right pairs are:  
> a clay pipe → clay  
> a clay pot → clay  
> a bronze bell → metal  
> a stone axe → stone  
> an iron hoe → metal  

> Classify these relics by material.

Groups: stone · clay · metal
- a bronze bell → **metal**
- a clay pot → **clay**
- an iron hoe → **metal**
- a stone axe → **stone**
- a grinding stone → **stone**

Full working after a second miss:

> The right pairs are:  
> a bronze bell → metal  
> a clay pot → clay  
> an iron hoe → metal  
> a stone axe → stone  
> a grinding stone → stone  

Sources: relics (Historical relics: collecting, labelling, caring for and classifying them)

### `hi2-care` · Lesson 2 · multiple choice, level 2

Prompt: How should you look after a relic?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Handle it carefully and keep it in a safe place.
- ✅ Write a label saying where and when it was found.
- ❌ Scrub it hard to make it look new.  
  _↳ Scrubbing can damage it._
- ❌ Sell it to a visitor.  
  _↳ Selling relics loses our heritage._
- ❌ Break it to see what is inside.  
  _↳ Breaking it destroys the evidence._
- ❌ Paint it a bright colour.  
  _↳ Paint hides the original surface._


Three generated variants:

> How should you look after a relic?

- ◻️ Break it to see what is inside.  
  _↳ feedback if chosen: Breaking it destroys the evidence._
- ◻️ Sell it to a visitor.  
  _↳ feedback if chosen: Selling relics loses our heritage._
- ✅ Handle it carefully and keep it in a safe place.
- ◻️ Scrub it hard to make it look new.  
  _↳ feedback if chosen: Scrubbing can damage it._

Full working after a second miss:

> The true statement is “Handle it carefully and keep it in a safe place.”.  
> “Break it to see what is inside.” is false: Breaking it destroys the evidence.  
> “Sell it to a visitor.” is false: Selling relics loses our heritage.  
> “Scrub it hard to make it look new.” is false: Scrubbing can damage it.  

> How should you look after a relic?

- ✅ Handle it carefully and keep it in a safe place.
- ◻️ Paint it a bright colour.  
  _↳ feedback if chosen: Paint hides the original surface._
- ◻️ Sell it to a visitor.  
  _↳ feedback if chosen: Selling relics loses our heritage._
- ◻️ Break it to see what is inside.  
  _↳ feedback if chosen: Breaking it destroys the evidence._

Full working after a second miss:

> The true statement is “Handle it carefully and keep it in a safe place.”.  
> “Paint it a bright colour.” is false: Paint hides the original surface.  
> “Sell it to a visitor.” is false: Selling relics loses our heritage.  
> “Break it to see what is inside.” is false: Breaking it destroys the evidence.  

> How should you look after a relic?

- ◻️ Sell it to a visitor.  
  _↳ feedback if chosen: Selling relics loses our heritage._
- ◻️ Scrub it hard to make it look new.  
  _↳ feedback if chosen: Scrubbing can damage it._
- ◻️ Break it to see what is inside.  
  _↳ feedback if chosen: Breaking it destroys the evidence._
- ✅ Handle it carefully and keep it in a safe place.

Full working after a second miss:

> The true statement is “Handle it carefully and keep it in a safe place.”.  
> “Sell it to a visitor.” is false: Selling relics loses our heritage.  
> “Scrub it hard to make it look new.” is false: Scrubbing can damage it.  
> “Break it to see what is inside.” is false: Breaking it destroys the evidence.  

Sources: relics (Historical relics: collecting, labelling, caring for and classifying them)

### `hi2-spot` · Lesson 2 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A relic is an object that has survived from the past.
- ✅ Museums keep relics safe.
- ✅ Relics can be classified by their use.
- ✅ A label tells where a relic was found.
- ❌ A new plastic chair is a historical relic.  
  _↳ It is new: a relic comes from the past._
- ❌ Relics should be cleaned with strong soap and a brush.  
  _↳ That can damage them: handle carefully._
- ❌ Selling relics protects our heritage.  
  _↳ Selling relics loses them from our heritage._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Museums keep relics safe.
- ◻️ A label tells where a relic was found.
- ◻️ Relics can be classified by their use.
- ✅ A new plastic chair is a historical relic.  
  _↳ explanation: It is new: a relic comes from the past._

Full working after a second miss:

> The wrong statement is “A new plastic chair is a historical relic.”.  
> It is new: a relic comes from the past.  

> One sentence is wrong. Which one?

- ◻️ A label tells where a relic was found.
- ✅ A new plastic chair is a historical relic.  
  _↳ explanation: It is new: a relic comes from the past._
- ◻️ Museums keep relics safe.
- ◻️ Relics can be classified by their use.

Full working after a second miss:

> The wrong statement is “A new plastic chair is a historical relic.”.  
> It is new: a relic comes from the past.  

> One sentence is wrong. Which one?

- ◻️ Museums keep relics safe.
- ◻️ A relic is an object that has survived from the past.
- ✅ Selling relics protects our heritage.  
  _↳ explanation: Selling relics loses them from our heritage._
- ◻️ A label tells where a relic was found.

Full working after a second miss:

> The wrong statement is “Selling relics protects our heritage.”.  
> Selling relics loses them from our heritage.  

Sources: relics (Historical relics: collecting, labelling, caring for and classifying them)

### `hic2-3-check` · Lesson 2 · multiple choice, level 1

Prompt: What should a relic’s label say?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ what it is, where and when it was found, and who gave it
- ❌ only its price  
  _↳ A relic’s value is its history, not only its price._
- ❌ nothing: labels are not needed  
  _↳ Without a label, its story is lost._
- ❌ the name of the person who will buy it  
  _↳ Relics should not be sold._
- ❌ a made-up story  
  _↳ A label must tell the truth about the relic._


Three generated variants:

> What should a relic’s label say?

- ✅ what it is, where and when it was found, and who gave it
- ◻️ the name of the person who will buy it  
  _↳ feedback if chosen: Relics should not be sold._
- ◻️ nothing: labels are not needed  
  _↳ feedback if chosen: Without a label, its story is lost._
- ◻️ only its price  
  _↳ feedback if chosen: A relic’s value is its history, not only its price._

Full working after a second miss:

> The true statement is “what it is, where and when it was found, and who gave it”.  
> “the name of the person who will buy it” is false: Relics should not be sold.  
> “nothing: labels are not needed” is false: Without a label, its story is lost.  
> “only its price” is false: A relic’s value is its history, not only its price.  

> What should a relic’s label say?

- ✅ what it is, where and when it was found, and who gave it
- ◻️ the name of the person who will buy it  
  _↳ feedback if chosen: Relics should not be sold._
- ◻️ nothing: labels are not needed  
  _↳ feedback if chosen: Without a label, its story is lost._
- ◻️ only its price  
  _↳ feedback if chosen: A relic’s value is its history, not only its price._

Full working after a second miss:

> The true statement is “what it is, where and when it was found, and who gave it”.  
> “the name of the person who will buy it” is false: Relics should not be sold.  
> “nothing: labels are not needed” is false: Without a label, its story is lost.  
> “only its price” is false: A relic’s value is its history, not only its price.  

> What should a relic’s label say?

- ◻️ nothing: labels are not needed  
  _↳ feedback if chosen: Without a label, its story is lost._
- ◻️ only its price  
  _↳ feedback if chosen: A relic’s value is its history, not only its price._
- ✅ what it is, where and when it was found, and who gave it
- ◻️ the name of the person who will buy it  
  _↳ feedback if chosen: Relics should not be sold._

Full working after a second miss:

> The true statement is “what it is, where and when it was found, and who gave it”.  
> “nothing: labels are not needed” is false: Without a label, its story is lost.  
> “only its price” is false: A relic’s value is its history, not only its price.  
> “the name of the person who will buy it” is false: Relics should not be sold.  

Sources: relics (Historical relics: collecting, labelling, caring for and classifying them)

### `hi4-place` · Lesson 4 · multiple choice, level 1

Prompt: In which country: {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| Toumaï (Sahelanthropus) was found here | Chad | Chad: Toumaï (Sahelanthropus) was found here. |
| “Lucy” (Australopithecus) was found here | Ethiopia | Ethiopia: “Lucy” (Australopithecus) was found here. |
| Olduvai Gorge, famous for Homo habilis, is here | Tanzania | Tanzania: Olduvai Gorge, famous for Homo habilis, is here. |
| the “Turkana Boy” (Homo erectus) was found here | Kenya | Kenya: the “Turkana Boy” (Homo erectus) was found here. |
| the Sterkfontein caves are here | South Africa | South Africa: the Sterkfontein caves are here. |

Right answer: `{x.a}`; wrong choices: `Chad`, `Ethiopia`, `Tanzania`, `Kenya`, `South Africa`

- Feedback `other`: “Not that country. Read the list of finds again.”

Three generated variants:

> In which country: “Lucy” (Australopithecus) was found here?

- ✅ Ethiopia
- ◻️ Chad  
  _↳ feedback if chosen: Not that country. Read the list of finds again._
- ◻️ Tanzania  
  _↳ feedback if chosen: Not that country. Read the list of finds again._
- ◻️ South Africa  
  _↳ feedback if chosen: Not that country. Read the list of finds again._

Full working after a second miss:

> Ethiopia: “Lucy” (Australopithecus) was found here.  
> Answer: Ethiopia.  

> In which country: Toumaï (Sahelanthropus) was found here?

- ✅ Chad
- ◻️ South Africa  
  _↳ feedback if chosen: Not that country. Read the list of finds again._
- ◻️ Ethiopia  
  _↳ feedback if chosen: Not that country. Read the list of finds again._
- ◻️ Tanzania  
  _↳ feedback if chosen: Not that country. Read the list of finds again._

Full working after a second miss:

> Chad: Toumaï (Sahelanthropus) was found here.  
> Answer: Chad.  

> In which country: “Lucy” (Australopithecus) was found here?

- ✅ Ethiopia
- ◻️ Chad  
  _↳ feedback if chosen: Not that country. Read the list of finds again._
- ◻️ South Africa  
  _↳ feedback if chosen: Not that country. Read the list of finds again._
- ◻️ Tanzania  
  _↳ feedback if chosen: Not that country. Read the list of finds again._

Full working after a second miss:

> Ethiopia: “Lucy” (Australopithecus) was found here.  
> Answer: Ethiopia.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi4-fossil` · Lesson 4 · multiple choice, level 1

Prompt: What is a fossil?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ the remains of a very old living thing, often turned to stone
- ❌ a new kind of stone tool  
  _↳ A tool is made by people; a fossil is a remain of a living thing._
- ❌ a story about the first people  
  _↳ That is a myth or oral tradition._
- ❌ a kind of cave painting  
  _↳ A painting is made by people; a fossil is a remain._
- ❌ a modern skeleton in a hospital  
  _↳ Fossils are very, very old._


Three generated variants:

> What is a fossil?

- ◻️ a new kind of stone tool  
  _↳ feedback if chosen: A tool is made by people; a fossil is a remain of a living thing._
- ◻️ a kind of cave painting  
  _↳ feedback if chosen: A painting is made by people; a fossil is a remain._
- ◻️ a story about the first people  
  _↳ feedback if chosen: That is a myth or oral tradition._
- ✅ the remains of a very old living thing, often turned to stone

Full working after a second miss:

> The true statement is “the remains of a very old living thing, often turned to stone”.  
> “a new kind of stone tool” is false: A tool is made by people; a fossil is a remain of a living thing.  
> “a kind of cave painting” is false: A painting is made by people; a fossil is a remain.  
> “a story about the first people” is false: That is a myth or oral tradition.  

> What is a fossil?

- ✅ the remains of a very old living thing, often turned to stone
- ◻️ a story about the first people  
  _↳ feedback if chosen: That is a myth or oral tradition._
- ◻️ a modern skeleton in a hospital  
  _↳ feedback if chosen: Fossils are very, very old._
- ◻️ a kind of cave painting  
  _↳ feedback if chosen: A painting is made by people; a fossil is a remain._

Full working after a second miss:

> The true statement is “the remains of a very old living thing, often turned to stone”.  
> “a story about the first people” is false: That is a myth or oral tradition.  
> “a modern skeleton in a hospital” is false: Fossils are very, very old.  
> “a kind of cave painting” is false: A painting is made by people; a fossil is a remain.  

> What is a fossil?

- ◻️ a new kind of stone tool  
  _↳ feedback if chosen: A tool is made by people; a fossil is a remain of a living thing._
- ◻️ a kind of cave painting  
  _↳ feedback if chosen: A painting is made by people; a fossil is a remain._
- ◻️ a modern skeleton in a hospital  
  _↳ feedback if chosen: Fossils are very, very old._
- ✅ the remains of a very old living thing, often turned to stone

Full working after a second miss:

> The true statement is “the remains of a very old living thing, often turned to stone”.  
> “a new kind of stone tool” is false: A tool is made by people; a fossil is a remain of a living thing.  
> “a kind of cave painting” is false: A painting is made by people; a fossil is a remain.  
> “a modern skeleton in a hospital” is false: Fossils are very, very old.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi4-cradle` · Lesson 4 · multiple choice, level 2

Prompt: Why is Africa called the cradle of humankind?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ The oldest fossils of human ancestors have been found there.
- ❌ It is the largest continent.  
  _↳ Asia is larger. The reason is the oldest fossils._
- ❌ It has the most people today.  
  _↳ Asia has the most people. The reason is the oldest fossils._
- ❌ It is the hottest continent.  
  _↳ The reason is the oldest fossils of human ancestors._
- ❌ All animals came from Africa.  
  _↳ The phrase is about human ancestors._


Three generated variants:

> Why is Africa called the cradle of humankind?

- ◻️ It is the hottest continent.  
  _↳ feedback if chosen: The reason is the oldest fossils of human ancestors._
- ◻️ It has the most people today.  
  _↳ feedback if chosen: Asia has the most people. The reason is the oldest fossils._
- ✅ The oldest fossils of human ancestors have been found there.
- ◻️ All animals came from Africa.  
  _↳ feedback if chosen: The phrase is about human ancestors._

Full working after a second miss:

> The true statement is “The oldest fossils of human ancestors have been found there.”.  
> “It is the hottest continent.” is false: The reason is the oldest fossils of human ancestors.  
> “It has the most people today.” is false: Asia has the most people. The reason is the oldest fossils.  
> “All animals came from Africa.” is false: The phrase is about human ancestors.  

> Why is Africa called the cradle of humankind?

- ✅ The oldest fossils of human ancestors have been found there.
- ◻️ It is the largest continent.  
  _↳ feedback if chosen: Asia is larger. The reason is the oldest fossils._
- ◻️ All animals came from Africa.  
  _↳ feedback if chosen: The phrase is about human ancestors._
- ◻️ It has the most people today.  
  _↳ feedback if chosen: Asia has the most people. The reason is the oldest fossils._

Full working after a second miss:

> The true statement is “The oldest fossils of human ancestors have been found there.”.  
> “It is the largest continent.” is false: Asia is larger. The reason is the oldest fossils.  
> “All animals came from Africa.” is false: The phrase is about human ancestors.  
> “It has the most people today.” is false: Asia has the most people. The reason is the oldest fossils.  

> Why is Africa called the cradle of humankind?

- ◻️ It is the hottest continent.  
  _↳ feedback if chosen: The reason is the oldest fossils of human ancestors._
- ✅ The oldest fossils of human ancestors have been found there.
- ◻️ It is the largest continent.  
  _↳ feedback if chosen: Asia is larger. The reason is the oldest fossils._
- ◻️ All animals came from Africa.  
  _↳ feedback if chosen: The phrase is about human ancestors._

Full working after a second miss:

> The true statement is “The oldest fossils of human ancestors have been found there.”.  
> “It is the hottest continent.” is false: The reason is the oldest fossils of human ancestors.  
> “It is the largest continent.” is false: Asia is larger. The reason is the oldest fossils.  
> “All animals came from Africa.” is false: The phrase is about human ancestors.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi4-water` · Lesson 4 · multiple choice, level 2

Prompt: Why did early humans settle near rivers and lakes?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ for drinking water and food from animals and plants
- ❌ to swim for fun  
  _↳ They needed water and food to survive._
- ❌ to travel by motor boat  
  _↳ Motor boats did not exist._
- ❌ because rivers were warm in winter  
  _↳ The reasons were water and food._
- ❌ to build bridges  
  _↳ Bridges came much later._


Three generated variants:

> Why did early humans settle near rivers and lakes?

- ◻️ to swim for fun  
  _↳ feedback if chosen: They needed water and food to survive._
- ◻️ to build bridges  
  _↳ feedback if chosen: Bridges came much later._
- ✅ for drinking water and food from animals and plants
- ◻️ to travel by motor boat  
  _↳ feedback if chosen: Motor boats did not exist._

Full working after a second miss:

> The true statement is “for drinking water and food from animals and plants”.  
> “to swim for fun” is false: They needed water and food to survive.  
> “to build bridges” is false: Bridges came much later.  
> “to travel by motor boat” is false: Motor boats did not exist.  

> Why did early humans settle near rivers and lakes?

- ◻️ to build bridges  
  _↳ feedback if chosen: Bridges came much later._
- ◻️ to travel by motor boat  
  _↳ feedback if chosen: Motor boats did not exist._
- ✅ for drinking water and food from animals and plants
- ◻️ because rivers were warm in winter  
  _↳ feedback if chosen: The reasons were water and food._

Full working after a second miss:

> The true statement is “for drinking water and food from animals and plants”.  
> “to build bridges” is false: Bridges came much later.  
> “to travel by motor boat” is false: Motor boats did not exist.  
> “because rivers were warm in winter” is false: The reasons were water and food.  

> Why did early humans settle near rivers and lakes?

- ✅ for drinking water and food from animals and plants
- ◻️ because rivers were warm in winter  
  _↳ feedback if chosen: The reasons were water and food._
- ◻️ to build bridges  
  _↳ feedback if chosen: Bridges came much later._
- ◻️ to travel by motor boat  
  _↳ feedback if chosen: Motor boats did not exist._

Full working after a second miss:

> The true statement is “for drinking water and food from animals and plants”.  
> “because rivers were warm in winter” is false: The reasons were water and food.  
> “to build bridges” is false: Bridges came much later.  
> “to travel by motor boat” is false: Motor boats did not exist.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi4-spot` · Lesson 4 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ “Lucy” was found in Ethiopia.
- ✅ Toumaï was found in Chad.
- ✅ Fossil dates are estimates.
- ✅ Early humans used caves for shelter.
- ❌ The oldest human fossils were found in Europe.  
  _↳ They were found in Africa._
- ❌ Early humans lived far from water.  
  _↳ They lived near water._
- ❌ Lucy lived about 300 years ago.  
  _↳ Lucy lived about 3.2 million years ago._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Toumaï was found in Chad.
- ✅ Lucy lived about 300 years ago.  
  _↳ explanation: Lucy lived about 3.2 million years ago._
- ◻️ Early humans used caves for shelter.
- ◻️ Fossil dates are estimates.

Full working after a second miss:

> The wrong statement is “Lucy lived about 300 years ago.”.  
> Lucy lived about 3.2 million years ago.  

> One sentence is wrong. Which one?

- ✅ Lucy lived about 300 years ago.  
  _↳ explanation: Lucy lived about 3.2 million years ago._
- ◻️ Early humans used caves for shelter.
- ◻️ Fossil dates are estimates.
- ◻️ Toumaï was found in Chad.

Full working after a second miss:

> The wrong statement is “Lucy lived about 300 years ago.”.  
> Lucy lived about 3.2 million years ago.  

> One sentence is wrong. Which one?

- ◻️ Fossil dates are estimates.
- ◻️ Toumaï was found in Chad.
- ◻️ “Lucy” was found in Ethiopia.
- ✅ Early humans lived far from water.  
  _↳ explanation: They lived near water._

Full working after a second miss:

> The wrong statement is “Early humans lived far from water.”.  
> They lived near water.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hic4-3-check` · Lesson 4 · multiple choice, level 1

Prompt: Where did early humans often live?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ near rivers and lakes
- ✅ in caves and rock shelters
- ✅ in the savanna, where there were animals to hunt
- ❌ in big cities  
  _↳ Cities came much later._
- ❌ in houses of cement  
  _↳ Cement was not known._
- ❌ on the tops of high, bare mountains  
  _↳ They needed water and food nearby._
- ❌ in the middle of deserts far from water  
  _↳ They needed water every day._


Three generated variants:

> Where did early humans often live?

- ◻️ on the tops of high, bare mountains  
  _↳ feedback if chosen: They needed water and food nearby._
- ◻️ in houses of cement  
  _↳ feedback if chosen: Cement was not known._
- ✅ in the savanna, where there were animals to hunt
- ◻️ in big cities  
  _↳ feedback if chosen: Cities came much later._

Full working after a second miss:

> The true statement is “in the savanna, where there were animals to hunt”.  
> “on the tops of high, bare mountains” is false: They needed water and food nearby.  
> “in houses of cement” is false: Cement was not known.  
> “in big cities” is false: Cities came much later.  

> Where did early humans often live?

- ✅ near rivers and lakes
- ◻️ on the tops of high, bare mountains  
  _↳ feedback if chosen: They needed water and food nearby._
- ◻️ in big cities  
  _↳ feedback if chosen: Cities came much later._
- ◻️ in houses of cement  
  _↳ feedback if chosen: Cement was not known._

Full working after a second miss:

> The true statement is “near rivers and lakes”.  
> “on the tops of high, bare mountains” is false: They needed water and food nearby.  
> “in big cities” is false: Cities came much later.  
> “in houses of cement” is false: Cement was not known.  

> Where did early humans often live?

- ◻️ in houses of cement  
  _↳ feedback if chosen: Cement was not known._
- ◻️ in the middle of deserts far from water  
  _↳ feedback if chosen: They needed water every day._
- ◻️ in big cities  
  _↳ feedback if chosen: Cities came much later._
- ✅ near rivers and lakes

Full working after a second miss:

> The true statement is “near rivers and lakes”.  
> “in houses of cement” is false: Cement was not known.  
> “in the middle of deserts far from water” is false: They needed water every day.  
> “in big cities” is false: Cities came much later.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi5-life` · Lesson 5 · multiple choice, level 1

Prompt: How did early humans get their food?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ by hunting, fishing and gathering wild plants
- ❌ by farming large fields of maize  
  _↳ Farming came later, in the New Stone Age._
- ❌ by buying food in markets  
  _↳ There were no markets or money._
- ❌ by keeping cattle in big ranches  
  _↳ Herding came later._
- ❌ from shops in towns  
  _↳ There were no towns or shops._


Three generated variants:

> How did early humans get their food?

- ◻️ from shops in towns  
  _↳ feedback if chosen: There were no towns or shops._
- ✅ by hunting, fishing and gathering wild plants
- ◻️ by keeping cattle in big ranches  
  _↳ feedback if chosen: Herding came later._
- ◻️ by farming large fields of maize  
  _↳ feedback if chosen: Farming came later, in the New Stone Age._

Full working after a second miss:

> The true statement is “by hunting, fishing and gathering wild plants”.  
> “from shops in towns” is false: There were no towns or shops.  
> “by keeping cattle in big ranches” is false: Herding came later.  
> “by farming large fields of maize” is false: Farming came later, in the New Stone Age.  

> How did early humans get their food?

- ◻️ from shops in towns  
  _↳ feedback if chosen: There were no towns or shops._
- ◻️ by farming large fields of maize  
  _↳ feedback if chosen: Farming came later, in the New Stone Age._
- ✅ by hunting, fishing and gathering wild plants
- ◻️ by keeping cattle in big ranches  
  _↳ feedback if chosen: Herding came later._

Full working after a second miss:

> The true statement is “by hunting, fishing and gathering wild plants”.  
> “from shops in towns” is false: There were no towns or shops.  
> “by farming large fields of maize” is false: Farming came later, in the New Stone Age.  
> “by keeping cattle in big ranches” is false: Herding came later.  

> How did early humans get their food?

- ◻️ by buying food in markets  
  _↳ feedback if chosen: There were no markets or money._
- ◻️ from shops in towns  
  _↳ feedback if chosen: There were no towns or shops._
- ◻️ by keeping cattle in big ranches  
  _↳ feedback if chosen: Herding came later._
- ✅ by hunting, fishing and gathering wild plants

Full working after a second miss:

> The true statement is “by hunting, fishing and gathering wild plants”.  
> “by buying food in markets” is false: There were no markets or money.  
> “from shops in towns” is false: There were no towns or shops.  
> “by keeping cattle in big ranches” is false: Herding came later.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi5-tool` · Lesson 5 · multiple choice, level 1

Prompt: What were early humans’ tools made of?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ stone, bone and wood
- ❌ iron and steel  
  _↳ Iron came much later._
- ❌ plastic  
  _↳ Plastic is a modern material._
- ❌ gold and silver  
  _↳ They used stone, bone and wood._
- ❌ glass  
  _↳ They used stone, bone and wood._


Three generated variants:

> What were early humans’ tools made of?

- ✅ stone, bone and wood
- ◻️ glass  
  _↳ feedback if chosen: They used stone, bone and wood._
- ◻️ iron and steel  
  _↳ feedback if chosen: Iron came much later._
- ◻️ gold and silver  
  _↳ feedback if chosen: They used stone, bone and wood._

Full working after a second miss:

> The true statement is “stone, bone and wood”.  
> “glass” is false: They used stone, bone and wood.  
> “iron and steel” is false: Iron came much later.  
> “gold and silver” is false: They used stone, bone and wood.  

> What were early humans’ tools made of?

- ◻️ glass  
  _↳ feedback if chosen: They used stone, bone and wood._
- ◻️ plastic  
  _↳ feedback if chosen: Plastic is a modern material._
- ✅ stone, bone and wood
- ◻️ iron and steel  
  _↳ feedback if chosen: Iron came much later._

Full working after a second miss:

> The true statement is “stone, bone and wood”.  
> “glass” is false: They used stone, bone and wood.  
> “plastic” is false: Plastic is a modern material.  
> “iron and steel” is false: Iron came much later.  

> What were early humans’ tools made of?

- ◻️ iron and steel  
  _↳ feedback if chosen: Iron came much later._
- ◻️ gold and silver  
  _↳ feedback if chosen: They used stone, bone and wood._
- ◻️ glass  
  _↳ feedback if chosen: They used stone, bone and wood._
- ✅ stone, bone and wood

Full working after a second miss:

> The true statement is “stone, bone and wood”.  
> “iron and steel” is false: Iron came much later.  
> “gold and silver” is false: They used stone, bone and wood.  
> “glass” is false: They used stone, bone and wood.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi5-fire` · Lesson 5 · multiple choice, level 1

Prompt: Which was a use of fire for early humans?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ cooking food
- ✅ keeping warm at night
- ✅ keeping wild animals away
- ✅ giving light in the dark
- ❌ charging phones  
  _↳ There was no electricity._
- ❌ melting iron in factories  
  _↳ That came much later._
- ❌ driving machines  
  _↳ There were no machines._
- ❌ boiling water in kettles  
  _↳ There were no metal kettles._


Three generated variants:

> Which was a use of fire for early humans?

- ✅ keeping wild animals away
- ◻️ charging phones  
  _↳ feedback if chosen: There was no electricity._
- ◻️ melting iron in factories  
  _↳ feedback if chosen: That came much later._
- ◻️ driving machines  
  _↳ feedback if chosen: There were no machines._

Full working after a second miss:

> The true statement is “keeping wild animals away”.  
> “charging phones” is false: There was no electricity.  
> “melting iron in factories” is false: That came much later.  
> “driving machines” is false: There were no machines.  

> Which was a use of fire for early humans?

- ◻️ boiling water in kettles  
  _↳ feedback if chosen: There were no metal kettles._
- ✅ giving light in the dark
- ◻️ charging phones  
  _↳ feedback if chosen: There was no electricity._
- ◻️ melting iron in factories  
  _↳ feedback if chosen: That came much later._

Full working after a second miss:

> The true statement is “giving light in the dark”.  
> “boiling water in kettles” is false: There were no metal kettles.  
> “charging phones” is false: There was no electricity.  
> “melting iron in factories” is false: That came much later.  

> Which was a use of fire for early humans?

- ◻️ boiling water in kettles  
  _↳ feedback if chosen: There were no metal kettles._
- ◻️ melting iron in factories  
  _↳ feedback if chosen: That came much later._
- ◻️ charging phones  
  _↳ feedback if chosen: There was no electricity._
- ✅ cooking food

Full working after a second miss:

> The true statement is “cooking food”.  
> “boiling water in kettles” is false: There were no metal kettles.  
> “melting iron in factories” is false: That came much later.  
> “charging phones” is false: There was no electricity.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi5-sort` · Lesson 5 · matching, level 2

Prompt: Sort these: true of early humans (Old Stone Age), or only later?

Pairs (6 shown each time, sorted into groups):

- hunting and gathering → **early humans**
- moving from place to place → **early humans**
- stone hand axes → **early humans**
- using fire → **early humans**
- wearing animal skins → **early humans**
- farming crops → **only later**
- living in permanent villages → **only later**
- making pottery → **only later**
- iron tools → **only later**
- keeping goats and cattle → **only later**


Three generated variants:

> Sort these: true of early humans (Old Stone Age), or only later?

Groups: early humans · only later
- farming crops → **only later**
- hunting and gathering → **early humans**
- making pottery → **only later**
- keeping goats and cattle → **only later**
- wearing animal skins → **early humans**
- using fire → **early humans**

Full working after a second miss:

> The right pairs are:  
> farming crops → only later  
> hunting and gathering → early humans  
> making pottery → only later  
> keeping goats and cattle → only later  
> wearing animal skins → early humans  
> using fire → early humans  

> Sort these: true of early humans (Old Stone Age), or only later?

Groups: early humans · only later
- stone hand axes → **early humans**
- living in permanent villages → **only later**
- keeping goats and cattle → **only later**
- farming crops → **only later**
- wearing animal skins → **early humans**
- iron tools → **only later**

Full working after a second miss:

> The right pairs are:  
> stone hand axes → early humans  
> living in permanent villages → only later  
> keeping goats and cattle → only later  
> farming crops → only later  
> wearing animal skins → early humans  
> iron tools → only later  

> Sort these: true of early humans (Old Stone Age), or only later?

Groups: early humans · only later
- stone hand axes → **early humans**
- iron tools → **only later**
- living in permanent villages → **only later**
- keeping goats and cattle → **only later**
- using fire → **early humans**
- making pottery → **only later**

Full working after a second miss:

> The right pairs are:  
> stone hand axes → early humans  
> iron tools → only later  
> living in permanent villages → only later  
> keeping goats and cattle → only later  
> using fire → early humans  
> making pottery → only later  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates); stone-age (Old and New Stone Age (Palaeolithic and Neolithic); the Neolithic revolution)

### `hi5-spot` · Lesson 5 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Early humans were nomads.
- ✅ Early humans lived in small groups.
- ✅ Fire helped early humans cook their food.
- ✅ Early humans painted on rock walls.
- ❌ Early humans grew maize and cassava on farms.  
  _↳ Farming came later, in the New Stone Age._
- ❌ Early humans used iron tools.  
  _↳ They used stone, bone and wood._
- ❌ Early humans lived in large towns.  
  _↳ They lived in small, moving groups._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Early humans were nomads.
- ✅ Early humans grew maize and cassava on farms.  
  _↳ explanation: Farming came later, in the New Stone Age._
- ◻️ Early humans lived in small groups.
- ◻️ Early humans painted on rock walls.

Full working after a second miss:

> The wrong statement is “Early humans grew maize and cassava on farms.”.  
> Farming came later, in the New Stone Age.  

> One sentence is wrong. Which one?

- ✅ Early humans lived in large towns.  
  _↳ explanation: They lived in small, moving groups._
- ◻️ Early humans painted on rock walls.
- ◻️ Fire helped early humans cook their food.
- ◻️ Early humans were nomads.

Full working after a second miss:

> The wrong statement is “Early humans lived in large towns.”.  
> They lived in small, moving groups.  

> One sentence is wrong. Which one?

- ◻️ Early humans were nomads.
- ◻️ Early humans painted on rock walls.
- ✅ Early humans lived in large towns.  
  _↳ explanation: They lived in small, moving groups._
- ◻️ Fire helped early humans cook their food.

Full working after a second miss:

> The wrong statement is “Early humans lived in large towns.”.  
> They lived in small, moving groups.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi6-what` · Lesson 6 · multiple choice, level 1

Prompt: What is a creation myth?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ a traditional story that explains how the world or the first people began
- ❌ a newspaper report  
  _↳ That is a written source about recent events._
- ❌ a fossil  
  _↳ A fossil is a remain of a living thing._
- ❌ a modern science experiment  
  _↳ A myth is a traditional story._
- ❌ a map of a village  
  _↳ A myth is a story._


Three generated variants:

> What is a creation myth?

- ✅ a traditional story that explains how the world or the first people began
- ◻️ a newspaper report  
  _↳ feedback if chosen: That is a written source about recent events._
- ◻️ a map of a village  
  _↳ feedback if chosen: A myth is a story._
- ◻️ a modern science experiment  
  _↳ feedback if chosen: A myth is a traditional story._

Full working after a second miss:

> The true statement is “a traditional story that explains how the world or the first people began”.  
> “a newspaper report” is false: That is a written source about recent events.  
> “a map of a village” is false: A myth is a story.  
> “a modern science experiment” is false: A myth is a traditional story.  

> What is a creation myth?

- ✅ a traditional story that explains how the world or the first people began
- ◻️ a newspaper report  
  _↳ feedback if chosen: That is a written source about recent events._
- ◻️ a fossil  
  _↳ feedback if chosen: A fossil is a remain of a living thing._
- ◻️ a modern science experiment  
  _↳ feedback if chosen: A myth is a traditional story._

Full working after a second miss:

> The true statement is “a traditional story that explains how the world or the first people began”.  
> “a newspaper report” is false: That is a written source about recent events.  
> “a fossil” is false: A fossil is a remain of a living thing.  
> “a modern science experiment” is false: A myth is a traditional story.  

> What is a creation myth?

- ◻️ a map of a village  
  _↳ feedback if chosen: A myth is a story._
- ◻️ a fossil  
  _↳ feedback if chosen: A fossil is a remain of a living thing._
- ◻️ a newspaper report  
  _↳ feedback if chosen: That is a written source about recent events._
- ✅ a traditional story that explains how the world or the first people began

Full working after a second miss:

> The true statement is “a traditional story that explains how the world or the first people began”.  
> “a map of a village” is false: A myth is a story.  
> “a fossil” is false: A fossil is a remain of a living thing.  
> “a newspaper report” is false: That is a written source about recent events.  

Sources: creation-myths (Myths of creation as oral sources (described neutrally))

### `hi6-passed` · Lesson 6 · multiple choice, level 1

Prompt: How are most creation myths passed on?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ orally: told by elders, storytellers and griots
- ❌ by text message  
  _↳ They are very old: they are passed on by word of mouth._
- ❌ only in school textbooks  
  _↳ Most are told by word of mouth._
- ❌ on radio only  
  _↳ They are much older than radio._
- ❌ by carving them on stone only  
  _↳ Most are told by word of mouth._


Three generated variants:

> How are most creation myths passed on?

- ✅ orally: told by elders, storytellers and griots
- ◻️ by text message  
  _↳ feedback if chosen: They are very old: they are passed on by word of mouth._
- ◻️ only in school textbooks  
  _↳ feedback if chosen: Most are told by word of mouth._
- ◻️ on radio only  
  _↳ feedback if chosen: They are much older than radio._

Full working after a second miss:

> The true statement is “orally: told by elders, storytellers and griots”.  
> “by text message” is false: They are very old: they are passed on by word of mouth.  
> “only in school textbooks” is false: Most are told by word of mouth.  
> “on radio only” is false: They are much older than radio.  

> How are most creation myths passed on?

- ◻️ on radio only  
  _↳ feedback if chosen: They are much older than radio._
- ◻️ by text message  
  _↳ feedback if chosen: They are very old: they are passed on by word of mouth._
- ◻️ only in school textbooks  
  _↳ feedback if chosen: Most are told by word of mouth._
- ✅ orally: told by elders, storytellers and griots

Full working after a second miss:

> The true statement is “orally: told by elders, storytellers and griots”.  
> “on radio only” is false: They are much older than radio.  
> “by text message” is false: They are very old: they are passed on by word of mouth.  
> “only in school textbooks” is false: Most are told by word of mouth.  

> How are most creation myths passed on?

- ◻️ only in school textbooks  
  _↳ feedback if chosen: Most are told by word of mouth._
- ◻️ by carving them on stone only  
  _↳ feedback if chosen: Most are told by word of mouth._
- ◻️ on radio only  
  _↳ feedback if chosen: They are much older than radio._
- ✅ orally: told by elders, storytellers and griots

Full working after a second miss:

> The true statement is “orally: told by elders, storytellers and griots”.  
> “only in school textbooks” is false: Most are told by word of mouth.  
> “by carving them on stone only” is false: Most are told by word of mouth.  
> “on radio only” is false: They are much older than radio.  

Sources: creation-myths (Myths of creation as oral sources (described neutrally))

### `hi6-sort` · Lesson 6 · matching, level 2

Prompt: Sort these sources: a story passed on by people, or material evidence?

Pairs (6 shown each time, sorted into groups):

- an elder’s story about the first ancestor → **story passed on by people**
- a song about how the river was made → **story passed on by people**
- a griot’s tale about the founding of the clan → **story passed on by people**
- a fossil bone → **material evidence**
- a stone tool dug up from the ground → **material evidence**
- the remains of an old fireplace → **material evidence**


Three generated variants:

> Sort these sources: a story passed on by people, or material evidence?

Groups: story passed on by people · material evidence
- a fossil bone → **material evidence**
- a song about how the river was made → **story passed on by people**
- a griot’s tale about the founding of the clan → **story passed on by people**
- an elder’s story about the first ancestor → **story passed on by people**
- a stone tool dug up from the ground → **material evidence**
- the remains of an old fireplace → **material evidence**

Full working after a second miss:

> The right pairs are:  
> a fossil bone → material evidence  
> a song about how the river was made → story passed on by people  
> a griot’s tale about the founding of the clan → story passed on by people  
> an elder’s story about the first ancestor → story passed on by people  
> a stone tool dug up from the ground → material evidence  
> the remains of an old fireplace → material evidence  

> Sort these sources: a story passed on by people, or material evidence?

Groups: story passed on by people · material evidence
- an elder’s story about the first ancestor → **story passed on by people**
- a stone tool dug up from the ground → **material evidence**
- a griot’s tale about the founding of the clan → **story passed on by people**
- a fossil bone → **material evidence**
- the remains of an old fireplace → **material evidence**
- a song about how the river was made → **story passed on by people**

Full working after a second miss:

> The right pairs are:  
> an elder’s story about the first ancestor → story passed on by people  
> a stone tool dug up from the ground → material evidence  
> a griot’s tale about the founding of the clan → story passed on by people  
> a fossil bone → material evidence  
> the remains of an old fireplace → material evidence  
> a song about how the river was made → story passed on by people  

> Sort these sources: a story passed on by people, or material evidence?

Groups: story passed on by people · material evidence
- a griot’s tale about the founding of the clan → **story passed on by people**
- a song about how the river was made → **story passed on by people**
- a fossil bone → **material evidence**
- the remains of an old fireplace → **material evidence**
- an elder’s story about the first ancestor → **story passed on by people**
- a stone tool dug up from the ground → **material evidence**

Full working after a second miss:

> The right pairs are:  
> a griot’s tale about the founding of the clan → story passed on by people  
> a song about how the river was made → story passed on by people  
> a fossil bone → material evidence  
> the remains of an old fireplace → material evidence  
> an elder’s story about the first ancestor → story passed on by people  
> a stone tool dug up from the ground → material evidence  

Sources: creation-myths (Myths of creation as oral sources (described neutrally))

### `hi6-respect` · Lesson 6 · multiple choice, level 2

Prompt: Your friend’s family tells a creation story different from yours. What is the best thing to do?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ listen with respect and learn about it
- ❌ laugh at the story  
  _↳ We respect other people’s beliefs._
- ❌ tell your friend the story is stupid  
  _↳ We respect other people’s beliefs._
- ❌ refuse to talk to your friend  
  _↳ Different beliefs are not a reason to reject a friend._
- ❌ tell the teacher your friend is wrong  
  _↳ Myths tell beliefs; we listen with respect._


Three generated variants:

> Your friend’s family tells a creation story different from yours. What is the best thing to do?

- ◻️ laugh at the story  
  _↳ feedback if chosen: We respect other people’s beliefs._
- ◻️ refuse to talk to your friend  
  _↳ feedback if chosen: Different beliefs are not a reason to reject a friend._
- ◻️ tell your friend the story is stupid  
  _↳ feedback if chosen: We respect other people’s beliefs._
- ✅ listen with respect and learn about it

Full working after a second miss:

> The true statement is “listen with respect and learn about it”.  
> “laugh at the story” is false: We respect other people’s beliefs.  
> “refuse to talk to your friend” is false: Different beliefs are not a reason to reject a friend.  
> “tell your friend the story is stupid” is false: We respect other people’s beliefs.  

> Your friend’s family tells a creation story different from yours. What is the best thing to do?

- ◻️ laugh at the story  
  _↳ feedback if chosen: We respect other people’s beliefs._
- ◻️ tell the teacher your friend is wrong  
  _↳ feedback if chosen: Myths tell beliefs; we listen with respect._
- ✅ listen with respect and learn about it
- ◻️ refuse to talk to your friend  
  _↳ feedback if chosen: Different beliefs are not a reason to reject a friend._

Full working after a second miss:

> The true statement is “listen with respect and learn about it”.  
> “laugh at the story” is false: We respect other people’s beliefs.  
> “tell the teacher your friend is wrong” is false: Myths tell beliefs; we listen with respect.  
> “refuse to talk to your friend” is false: Different beliefs are not a reason to reject a friend.  

> Your friend’s family tells a creation story different from yours. What is the best thing to do?

- ◻️ tell your friend the story is stupid  
  _↳ feedback if chosen: We respect other people’s beliefs._
- ◻️ tell the teacher your friend is wrong  
  _↳ feedback if chosen: Myths tell beliefs; we listen with respect._
- ✅ listen with respect and learn about it
- ◻️ refuse to talk to your friend  
  _↳ feedback if chosen: Different beliefs are not a reason to reject a friend._

Full working after a second miss:

> The true statement is “listen with respect and learn about it”.  
> “tell your friend the story is stupid” is false: We respect other people’s beliefs.  
> “tell the teacher your friend is wrong” is false: Myths tell beliefs; we listen with respect.  
> “refuse to talk to your friend” is false: Different beliefs are not a reason to reject a friend.  

Sources: creation-myths (Myths of creation as oral sources (described neutrally))

### `hi6-spot` · Lesson 6 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A myth explains how something began.
- ✅ Many myths are passed on orally.
- ✅ Historians study myths to learn about beliefs.
- ✅ Almost every people has creation stories.
- ❌ Only one people in the world has a creation story.  
  _↳ Almost every people has creation stories._
- ❌ Historians study fossils by listening to songs.  
  _↳ Fossils are material evidence; songs are oral sources._
- ❌ Myths are always written in newspapers.  
  _↳ Myths are usually passed on orally._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Many myths are passed on orally.
- ✅ Only one people in the world has a creation story.  
  _↳ explanation: Almost every people has creation stories._
- ◻️ A myth explains how something began.
- ◻️ Historians study myths to learn about beliefs.

Full working after a second miss:

> The wrong statement is “Only one people in the world has a creation story.”.  
> Almost every people has creation stories.  

> One sentence is wrong. Which one?

- ✅ Myths are always written in newspapers.  
  _↳ explanation: Myths are usually passed on orally._
- ◻️ Many myths are passed on orally.
- ◻️ A myth explains how something began.
- ◻️ Historians study myths to learn about beliefs.

Full working after a second miss:

> The wrong statement is “Myths are always written in newspapers.”.  
> Myths are usually passed on orally.  

> One sentence is wrong. Which one?

- ◻️ Historians study myths to learn about beliefs.
- ✅ Historians study fossils by listening to songs.  
  _↳ explanation: Fossils are material evidence; songs are oral sources._
- ◻️ Many myths are passed on orally.
- ◻️ Almost every people has creation stories.

Full working after a second miss:

> The wrong statement is “Historians study fossils by listening to songs.”.  
> Fossils are material evidence; songs are oral sources.  

Sources: creation-myths (Myths of creation as oral sources (described neutrally))

### `hic6-3-check` · Lesson 6 · multiple choice, level 1

Prompt: Why do historians study creation myths?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ to learn what a people believed and valued
- ❌ to make fun of other people’s beliefs  
  _↳ We respect everyone’s beliefs._
- ❌ to find the exact date the world began  
  _↳ Myths tell beliefs, not exact dates._
- ❌ because myths are written in old books only  
  _↳ Most myths are passed on orally._
- ❌ to stop people telling stories  
  _↳ Historians want the stories kept and recorded._


Three generated variants:

> Why do historians study creation myths?

- ◻️ to make fun of other people’s beliefs  
  _↳ feedback if chosen: We respect everyone’s beliefs._
- ◻️ to find the exact date the world began  
  _↳ feedback if chosen: Myths tell beliefs, not exact dates._
- ◻️ because myths are written in old books only  
  _↳ feedback if chosen: Most myths are passed on orally._
- ✅ to learn what a people believed and valued

Full working after a second miss:

> The true statement is “to learn what a people believed and valued”.  
> “to make fun of other people’s beliefs” is false: We respect everyone’s beliefs.  
> “to find the exact date the world began” is false: Myths tell beliefs, not exact dates.  
> “because myths are written in old books only” is false: Most myths are passed on orally.  

> Why do historians study creation myths?

- ◻️ to stop people telling stories  
  _↳ feedback if chosen: Historians want the stories kept and recorded._
- ◻️ to find the exact date the world began  
  _↳ feedback if chosen: Myths tell beliefs, not exact dates._
- ◻️ because myths are written in old books only  
  _↳ feedback if chosen: Most myths are passed on orally._
- ✅ to learn what a people believed and valued

Full working after a second miss:

> The true statement is “to learn what a people believed and valued”.  
> “to stop people telling stories” is false: Historians want the stories kept and recorded.  
> “to find the exact date the world began” is false: Myths tell beliefs, not exact dates.  
> “because myths are written in old books only” is false: Most myths are passed on orally.  

> Why do historians study creation myths?

- ✅ to learn what a people believed and valued
- ◻️ to make fun of other people’s beliefs  
  _↳ feedback if chosen: We respect everyone’s beliefs._
- ◻️ to stop people telling stories  
  _↳ feedback if chosen: Historians want the stories kept and recorded._
- ◻️ because myths are written in old books only  
  _↳ feedback if chosen: Most myths are passed on orally._

Full working after a second miss:

> The true statement is “to learn what a people believed and valued”.  
> “to make fun of other people’s beliefs” is false: We respect everyone’s beliefs.  
> “to stop people telling stories” is false: Historians want the stories kept and recorded.  
> “because myths are written in old books only” is false: Most myths are passed on orally.  

Sources: creation-myths (Myths of creation as oral sources (described neutrally))

### `hi7-sort` · Lesson 7 · matching, level 1

Prompt: Sort these: Old Stone Age or New Stone Age?

Pairs (6 shown each time, sorted into groups):

- hunting and gathering → **Old Stone Age**
- moving from place to place → **Old Stone Age**
- chipped stone tools → **Old Stone Age**
- living in caves and camps → **Old Stone Age**
- farming crops → **New Stone Age**
- keeping goats and cattle → **New Stone Age**
- permanent villages → **New Stone Age**
- polished stone tools → **New Stone Age**
- pottery → **New Stone Age**


Three generated variants:

> Sort these: Old Stone Age or New Stone Age?

Groups: Old Stone Age · New Stone Age
- pottery → **New Stone Age**
- farming crops → **New Stone Age**
- polished stone tools → **New Stone Age**
- moving from place to place → **Old Stone Age**
- keeping goats and cattle → **New Stone Age**
- chipped stone tools → **Old Stone Age**

Full working after a second miss:

> The right pairs are:  
> pottery → New Stone Age  
> farming crops → New Stone Age  
> polished stone tools → New Stone Age  
> moving from place to place → Old Stone Age  
> keeping goats and cattle → New Stone Age  
> chipped stone tools → Old Stone Age  

> Sort these: Old Stone Age or New Stone Age?

Groups: Old Stone Age · New Stone Age
- hunting and gathering → **Old Stone Age**
- moving from place to place → **Old Stone Age**
- pottery → **New Stone Age**
- chipped stone tools → **Old Stone Age**
- living in caves and camps → **Old Stone Age**
- farming crops → **New Stone Age**

Full working after a second miss:

> The right pairs are:  
> hunting and gathering → Old Stone Age  
> moving from place to place → Old Stone Age  
> pottery → New Stone Age  
> chipped stone tools → Old Stone Age  
> living in caves and camps → Old Stone Age  
> farming crops → New Stone Age  

> Sort these: Old Stone Age or New Stone Age?

Groups: Old Stone Age · New Stone Age
- polished stone tools → **New Stone Age**
- pottery → **New Stone Age**
- living in caves and camps → **Old Stone Age**
- permanent villages → **New Stone Age**
- hunting and gathering → **Old Stone Age**
- chipped stone tools → **Old Stone Age**

Full working after a second miss:

> The right pairs are:  
> polished stone tools → New Stone Age  
> pottery → New Stone Age  
> living in caves and camps → Old Stone Age  
> permanent villages → New Stone Age  
> hunting and gathering → Old Stone Age  
> chipped stone tools → Old Stone Age  

Sources: stone-age (Old and New Stone Age (Palaeolithic and Neolithic); the Neolithic revolution)

### `hi7-new` · Lesson 7 · multiple choice, level 1

Prompt: Which was new in the Neolithic (New Stone Age)?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ pottery
- ✅ polished stone axes
- ✅ growing crops
- ✅ keeping animals
- ❌ using fire  
  _↳ Fire was used long before, in the Old Stone Age._
- ❌ hunting  
  _↳ People hunted long before._
- ❌ iron tools  
  _↳ Iron came later, in the Iron Age._
- ❌ gathering wild fruits  
  _↳ That is older._


Three generated variants:

> Which was new in the Neolithic (New Stone Age)?

- ◻️ hunting  
  _↳ feedback if chosen: People hunted long before._
- ◻️ iron tools  
  _↳ feedback if chosen: Iron came later, in the Iron Age._
- ◻️ using fire  
  _↳ feedback if chosen: Fire was used long before, in the Old Stone Age._
- ✅ keeping animals

Full working after a second miss:

> The true statement is “keeping animals”.  
> “hunting” is false: People hunted long before.  
> “iron tools” is false: Iron came later, in the Iron Age.  
> “using fire” is false: Fire was used long before, in the Old Stone Age.  

> Which was new in the Neolithic (New Stone Age)?

- ◻️ using fire  
  _↳ feedback if chosen: Fire was used long before, in the Old Stone Age._
- ◻️ hunting  
  _↳ feedback if chosen: People hunted long before._
- ✅ keeping animals
- ◻️ iron tools  
  _↳ feedback if chosen: Iron came later, in the Iron Age._

Full working after a second miss:

> The true statement is “keeping animals”.  
> “using fire” is false: Fire was used long before, in the Old Stone Age.  
> “hunting” is false: People hunted long before.  
> “iron tools” is false: Iron came later, in the Iron Age.  

> Which was new in the Neolithic (New Stone Age)?

- ◻️ hunting  
  _↳ feedback if chosen: People hunted long before._
- ◻️ gathering wild fruits  
  _↳ feedback if chosen: That is older._
- ◻️ using fire  
  _↳ feedback if chosen: Fire was used long before, in the Old Stone Age._
- ✅ pottery

Full working after a second miss:

> The true statement is “pottery”.  
> “hunting” is false: People hunted long before.  
> “gathering wild fruits” is false: That is older.  
> “using fire” is false: Fire was used long before, in the Old Stone Age.  

Sources: stone-age (Old and New Stone Age (Palaeolithic and Neolithic); the Neolithic revolution)

### `hi7-why` · Lesson 7 · multiple choice, level 2

Prompt: Why could Neolithic people live in permanent villages?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Farming and herding gave them food in one place.
- ❌ They had cars to fetch food.  
  _↳ There were no cars._
- ❌ Wild animals came to their houses every day.  
  _↳ They grew crops and kept animals._
- ❌ They stopped eating.  
  _↳ They grew their food._
- ❌ They bought food from shops.  
  _↳ There were no shops._


Three generated variants:

> Why could Neolithic people live in permanent villages?

- ✅ Farming and herding gave them food in one place.
- ◻️ Wild animals came to their houses every day.  
  _↳ feedback if chosen: They grew crops and kept animals._
- ◻️ They bought food from shops.  
  _↳ feedback if chosen: There were no shops._
- ◻️ They had cars to fetch food.  
  _↳ feedback if chosen: There were no cars._

Full working after a second miss:

> The true statement is “Farming and herding gave them food in one place.”.  
> “Wild animals came to their houses every day.” is false: They grew crops and kept animals.  
> “They bought food from shops.” is false: There were no shops.  
> “They had cars to fetch food.” is false: There were no cars.  

> Why could Neolithic people live in permanent villages?

- ◻️ They had cars to fetch food.  
  _↳ feedback if chosen: There were no cars._
- ◻️ Wild animals came to their houses every day.  
  _↳ feedback if chosen: They grew crops and kept animals._
- ◻️ They stopped eating.  
  _↳ feedback if chosen: They grew their food._
- ✅ Farming and herding gave them food in one place.

Full working after a second miss:

> The true statement is “Farming and herding gave them food in one place.”.  
> “They had cars to fetch food.” is false: There were no cars.  
> “Wild animals came to their houses every day.” is false: They grew crops and kept animals.  
> “They stopped eating.” is false: They grew their food.  

> Why could Neolithic people live in permanent villages?

- ✅ Farming and herding gave them food in one place.
- ◻️ They stopped eating.  
  _↳ feedback if chosen: They grew their food._
- ◻️ Wild animals came to their houses every day.  
  _↳ feedback if chosen: They grew crops and kept animals._
- ◻️ They bought food from shops.  
  _↳ feedback if chosen: There were no shops._

Full working after a second miss:

> The true statement is “Farming and herding gave them food in one place.”.  
> “They stopped eating.” is false: They grew their food.  
> “Wild animals came to their houses every day.” is false: They grew crops and kept animals.  
> “They bought food from shops.” is false: There were no shops.  

Sources: stone-age (Old and New Stone Age (Palaeolithic and Neolithic); the Neolithic revolution)

### `hi7-when` · Lesson 7 · multiple choice, level 2

Prompt: When did this begin: {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| the first crops and domesticated animals | the New Stone Age (Neolithic) | The New Stone Age (Neolithic): the first crops and domesticated animals. |
| hand axes made by chipping stone | the Old Stone Age (Palaeolithic) | The Old Stone Age (Palaeolithic): hand axes made by chipping stone. |
| clay pots for storing grain | the New Stone Age (Neolithic) | The New Stone Age (Neolithic): clay pots for storing grain. |
| the first use of fire | the Old Stone Age (Palaeolithic) | The Old Stone Age (Palaeolithic): the first use of fire. |
| the first permanent farming villages | the New Stone Age (Neolithic) | The New Stone Age (Neolithic): the first permanent farming villages. |

Right answer: `{x.a}`; wrong choices: `the Old Stone Age (Palaeolithic)`, `the New Stone Age (Neolithic)`

- Feedback `other`: “Think: hunting and moving (Old), or farming and villages (New)?”

Three generated variants:

> When did this begin: the first crops and domesticated animals?

- ✅ the New Stone Age (Neolithic)
- ◻️ the Old Stone Age (Palaeolithic)  
  _↳ feedback if chosen: Think: hunting and moving (Old), or farming and villages (New)?_

Full working after a second miss:

> The New Stone Age (Neolithic): the first crops and domesticated animals.  
> Answer: the New Stone Age (Neolithic).  

> When did this begin: the first use of fire?

- ✅ the Old Stone Age (Palaeolithic)
- ◻️ the New Stone Age (Neolithic)  
  _↳ feedback if chosen: Think: hunting and moving (Old), or farming and villages (New)?_

Full working after a second miss:

> The Old Stone Age (Palaeolithic): the first use of fire.  
> Answer: the Old Stone Age (Palaeolithic).  

> When did this begin: the first use of fire?

- ◻️ the New Stone Age (Neolithic)  
  _↳ feedback if chosen: Think: hunting and moving (Old), or farming and villages (New)?_
- ✅ the Old Stone Age (Palaeolithic)

Full working after a second miss:

> The Old Stone Age (Palaeolithic): the first use of fire.  
> Answer: the Old Stone Age (Palaeolithic).  

Sources: stone-age (Old and New Stone Age (Palaeolithic and Neolithic); the Neolithic revolution)

### `hi7-spot` · Lesson 7 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Neolithic people made pottery.
- ✅ Neolithic people kept goats and cattle.
- ✅ The Neolithic began about 10 000 years ago.
- ✅ Farming led to permanent villages.
- ❌ Neolithic people only hunted and never farmed.  
  _↳ Farming is what makes the Neolithic new._
- ❌ Neolithic people made iron tools.  
  _↳ Iron came later._
- ❌ Farming made food scarcer.  
  _↳ Farming gave more food._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ Neolithic people only hunted and never farmed.  
  _↳ explanation: Farming is what makes the Neolithic new._
- ◻️ The Neolithic began about 10 000 years ago.
- ◻️ Neolithic people made pottery.
- ◻️ Neolithic people kept goats and cattle.

Full working after a second miss:

> The wrong statement is “Neolithic people only hunted and never farmed.”.  
> Farming is what makes the Neolithic new.  

> One sentence is wrong. Which one?

- ◻️ Neolithic people made pottery.
- ◻️ The Neolithic began about 10 000 years ago.
- ✅ Neolithic people made iron tools.  
  _↳ explanation: Iron came later._
- ◻️ Neolithic people kept goats and cattle.

Full working after a second miss:

> The wrong statement is “Neolithic people made iron tools.”.  
> Iron came later.  

> One sentence is wrong. Which one?

- ◻️ The Neolithic began about 10 000 years ago.
- ✅ Neolithic people only hunted and never farmed.  
  _↳ explanation: Farming is what makes the Neolithic new._
- ◻️ Neolithic people made pottery.
- ◻️ Neolithic people kept goats and cattle.

Full working after a second miss:

> The wrong statement is “Neolithic people only hunted and never farmed.”.  
> Farming is what makes the Neolithic new.  

Sources: stone-age (Old and New Stone Age (Palaeolithic and Neolithic); the Neolithic revolution)

### `hic7-3-check` · Lesson 7 · multiple choice, level 1

Prompt: What was a result of farming in the New Stone Age?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ more food and more people
- ✅ permanent villages
- ✅ trade between villages
- ❌ fewer people  
  _↳ More food meant more people._
- ❌ everyone moved from place to place  
  _↳ Farmers stayed in one place._
- ❌ the end of all tools  
  _↳ Tools improved: polished axes and hoes._
- ❌ people stopped cooking  
  _↳ Pottery made cooking and storage easier._


Three generated variants:

> What was a result of farming in the New Stone Age?

- ✅ permanent villages
- ◻️ fewer people  
  _↳ feedback if chosen: More food meant more people._
- ◻️ people stopped cooking  
  _↳ feedback if chosen: Pottery made cooking and storage easier._
- ◻️ everyone moved from place to place  
  _↳ feedback if chosen: Farmers stayed in one place._

Full working after a second miss:

> The true statement is “permanent villages”.  
> “fewer people” is false: More food meant more people.  
> “people stopped cooking” is false: Pottery made cooking and storage easier.  
> “everyone moved from place to place” is false: Farmers stayed in one place.  

> What was a result of farming in the New Stone Age?

- ◻️ the end of all tools  
  _↳ feedback if chosen: Tools improved: polished axes and hoes._
- ✅ trade between villages
- ◻️ fewer people  
  _↳ feedback if chosen: More food meant more people._
- ◻️ people stopped cooking  
  _↳ feedback if chosen: Pottery made cooking and storage easier._

Full working after a second miss:

> The true statement is “trade between villages”.  
> “the end of all tools” is false: Tools improved: polished axes and hoes.  
> “fewer people” is false: More food meant more people.  
> “people stopped cooking” is false: Pottery made cooking and storage easier.  

> What was a result of farming in the New Stone Age?

- ◻️ fewer people  
  _↳ feedback if chosen: More food meant more people._
- ◻️ everyone moved from place to place  
  _↳ feedback if chosen: Farmers stayed in one place._
- ◻️ the end of all tools  
  _↳ feedback if chosen: Tools improved: polished axes and hoes._
- ✅ permanent villages

Full working after a second miss:

> The true statement is “permanent villages”.  
> “fewer people” is false: More food meant more people.  
> “everyone moved from place to place” is false: Farmers stayed in one place.  
> “the end of all tools” is false: Tools improved: polished axes and hoes.  

Sources: stone-age (Old and New Stone Age (Palaeolithic and Neolithic); the Neolithic revolution)

### `hi8-order` · Lesson 8 · ordering, level 1

Prompt: Put these in order, oldest first.

Items in the right order:

1. {homininName(s[0])}
2. {homininName(s[1])}
3. {homininName(s[2])}


Three generated variants:

> Put these in order, oldest first.

Shown as: Homo erectus · Australopithecus (“Lucy”) · Homo habilis
Correct order: Australopithecus (“Lucy”) → Homo habilis → Homo erectus

Full working after a second miss:

> The correct order is: Australopithecus (“Lucy”) → Homo habilis → Homo erectus.  

> Put these in order, oldest first.

Shown as: Homo sapiens · Homo habilis · Australopithecus (“Lucy”)
Correct order: Australopithecus (“Lucy”) → Homo habilis → Homo sapiens

Full working after a second miss:

> The correct order is: Australopithecus (“Lucy”) → Homo habilis → Homo sapiens.  

> Put these in order, oldest first.

Shown as: Sahelanthropus tchadensis (Toumaï) · Homo erectus · Australopithecus (“Lucy”)
Correct order: Sahelanthropus tchadensis (Toumaï) → Australopithecus (“Lucy”) → Homo erectus

Full working after a second miss:

> The correct order is: Sahelanthropus tchadensis (Toumaï) → Australopithecus (“Lucy”) → Homo erectus.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi8-name` · Lesson 8 · multiple choice, level 1

Prompt: Which is {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| “handy man”, the first maker of simple stone tools | Homo habilis | Homo habilis: “handy man”, the first maker of simple stone tools. |
| “upright man”, who used fire | Homo erectus | Homo erectus: “upright man”, who used fire. |
| “wise man”: modern humans | Homo sapiens | Homo sapiens: “wise man”: modern humans. |

Right answer: `{x.a}`; wrong choices: `Homo habilis`, `Homo erectus`, `Homo sapiens`, `Australopithecus (“Lucy”)`

- Feedback `other`: “Not that one. Read what each name means.”

Three generated variants:

> Which is “upright man”, who used fire?

- ◻️ Homo habilis  
  _↳ feedback if chosen: Not that one. Read what each name means._
- ◻️ Homo sapiens  
  _↳ feedback if chosen: Not that one. Read what each name means._
- ✅ Homo erectus

Full working after a second miss:

> Homo erectus: “upright man”, who used fire.  
> Answer: Homo erectus.  

> Which is “upright man”, who used fire?

- ✅ Homo erectus
- ◻️ Homo habilis  
  _↳ feedback if chosen: Not that one. Read what each name means._
- ◻️ Australopithecus (“Lucy”)  
  _↳ feedback if chosen: Not that one. Read what each name means._

Full working after a second miss:

> Homo erectus: “upright man”, who used fire.  
> Answer: Homo erectus.  

> Which is “handy man”, the first maker of simple stone tools?

- ◻️ Australopithecus (“Lucy”)  
  _↳ feedback if chosen: Not that one. Read what each name means._
- ✅ Homo habilis
- ◻️ Homo sapiens  
  _↳ feedback if chosen: Not that one. Read what each name means._

Full working after a second miss:

> Homo habilis: “handy man”, the first maker of simple stone tools.  
> Answer: Homo habilis.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi8-older` · Lesson 8 · multiple choice, level 2

Prompt: Which appeared earlier: {homininName(a)} or {homininName(b)}?

Right answer: `{homininName(min(a, b))}`; wrong choices: `{homininName(max(a, b))}`

- Feedback `later`: “That one appeared later. Compare how many years ago each lived.”

Three generated variants:

> Which appeared earlier: Australopithecus (“Lucy”) or Homo habilis?

- ✅ Australopithecus (“Lucy”)
- ◻️ Homo habilis  
  _↳ feedback if chosen: That one appeared later. Compare how many years ago each lived._

Full working after a second miss:

> Australopithecus (“Lucy”): about 3.2 million years ago. Homo habilis: about 2.4 million years ago.  
> Earlier: Australopithecus (“Lucy”).  

> Which appeared earlier: Homo sapiens or Homo erectus?

- ✅ Homo erectus
- ◻️ Homo sapiens  
  _↳ feedback if chosen: That one appeared later. Compare how many years ago each lived._

Full working after a second miss:

> Homo erectus: about 1.9 million years ago. Homo sapiens: about 300 000 years ago.  
> Earlier: Homo erectus.  

> Which appeared earlier: Australopithecus (“Lucy”) or Homo erectus?

- ✅ Australopithecus (“Lucy”)
- ◻️ Homo erectus  
  _↳ feedback if chosen: That one appeared later. Compare how many years ago each lived._

Full working after a second miss:

> Australopithecus (“Lucy”): about 3.2 million years ago. Homo erectus: about 1.9 million years ago.  
> Earlier: Australopithecus (“Lucy”).  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi8-when` · Lesson 8 · multiple choice, level 2

Prompt: About when did {homininName(i)} first appear?

Right answer: `{ago(homininAgo(i))}`; wrong choices: `{ago(homininAgo(0))}`, `{ago(homininAgo(1))}`, `{ago(homininAgo(2))}`, `{ago(homininAgo(3))}`, `{ago(homininAgo(4))}`

- Feedback `other`: “That date belongs to a different ancestor. Oldest first: Toumaï, Lucy, Homo habilis, Homo erectus, Homo sapiens.”

Three generated variants:

> About when did Homo habilis first appear?

- ◻️ about 300 000 years ago  
  _↳ feedback if chosen: That date belongs to a different ancestor. Oldest first: Toumaï, Lucy, Homo habilis, Homo erectus, Homo sapiens._
- ◻️ about 1.9 million years ago  
  _↳ feedback if chosen: That date belongs to a different ancestor. Oldest first: Toumaï, Lucy, Homo habilis, Homo erectus, Homo sapiens._
- ◻️ about 7 million years ago  
  _↳ feedback if chosen: That date belongs to a different ancestor. Oldest first: Toumaï, Lucy, Homo habilis, Homo erectus, Homo sapiens._
- ✅ about 2.4 million years ago

Full working after a second miss:

> Homo habilis: about 2.4 million years ago.  

> About when did Homo habilis first appear?

- ◻️ about 1.9 million years ago  
  _↳ feedback if chosen: That date belongs to a different ancestor. Oldest first: Toumaï, Lucy, Homo habilis, Homo erectus, Homo sapiens._
- ◻️ about 7 million years ago  
  _↳ feedback if chosen: That date belongs to a different ancestor. Oldest first: Toumaï, Lucy, Homo habilis, Homo erectus, Homo sapiens._
- ◻️ about 3.2 million years ago  
  _↳ feedback if chosen: That date belongs to a different ancestor. Oldest first: Toumaï, Lucy, Homo habilis, Homo erectus, Homo sapiens._
- ✅ about 2.4 million years ago

Full working after a second miss:

> Homo habilis: about 2.4 million years ago.  

> About when did Homo habilis first appear?

- ◻️ about 1.9 million years ago  
  _↳ feedback if chosen: That date belongs to a different ancestor. Oldest first: Toumaï, Lucy, Homo habilis, Homo erectus, Homo sapiens._
- ◻️ about 3.2 million years ago  
  _↳ feedback if chosen: That date belongs to a different ancestor. Oldest first: Toumaï, Lucy, Homo habilis, Homo erectus, Homo sapiens._
- ✅ about 2.4 million years ago
- ◻️ about 7 million years ago  
  _↳ feedback if chosen: That date belongs to a different ancestor. Oldest first: Toumaï, Lucy, Homo habilis, Homo erectus, Homo sapiens._

Full working after a second miss:

> Homo habilis: about 2.4 million years ago.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi8-spot` · Lesson 8 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Homo sapiens means “wise man”.
- ✅ Homo habilis made simple stone tools.
- ✅ Homo erectus used fire.
- ✅ Australopithecus walked upright.
- ❌ Homo sapiens lived before Australopithecus.  
  _↳ Australopithecus is much older._
- ❌ The human brain became smaller during humanisation.  
  _↳ It became bigger._
- ❌ Homo erectus means “handy man”.  
  _↳ Homo erectus means “upright man”; Homo habilis is “handy man”._


Three generated variants:

> One sentence is wrong. Which one?

- ✅ Homo erectus means “handy man”.  
  _↳ explanation: Homo erectus means “upright man”; Homo habilis is “handy man”._
- ◻️ Homo erectus used fire.
- ◻️ Australopithecus walked upright.
- ◻️ Homo sapiens means “wise man”.

Full working after a second miss:

> The wrong statement is “Homo erectus means “handy man”.”.  
> Homo erectus means “upright man”; Homo habilis is “handy man”.  

> One sentence is wrong. Which one?

- ✅ Homo sapiens lived before Australopithecus.  
  _↳ explanation: Australopithecus is much older._
- ◻️ Homo sapiens means “wise man”.
- ◻️ Australopithecus walked upright.
- ◻️ Homo erectus used fire.

Full working after a second miss:

> The wrong statement is “Homo sapiens lived before Australopithecus.”.  
> Australopithecus is much older.  

> One sentence is wrong. Which one?

- ◻️ Homo erectus used fire.
- ◻️ Homo habilis made simple stone tools.
- ◻️ Australopithecus walked upright.
- ✅ Homo sapiens lived before Australopithecus.  
  _↳ explanation: Australopithecus is much older._

Full working after a second miss:

> The wrong statement is “Homo sapiens lived before Australopithecus.”.  
> Australopithecus is much older.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hic8-3-check` · Lesson 8 · multiple choice, level 1

Prompt: Which change happened during humanisation?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ walking upright on two legs
- ✅ a bigger brain
- ✅ making better tools
- ✅ using fire
- ❌ growing wings  
  _↳ Humans never grew wings._
- ❌ losing the hands  
  _↳ The hands became more useful._
- ❌ the brain becoming smaller  
  _↳ The brain became bigger._
- ❌ learning to drive  
  _↳ Cars came only recently._


Three generated variants:

> Which change happened during humanisation?

- ◻️ the brain becoming smaller  
  _↳ feedback if chosen: The brain became bigger._
- ◻️ growing wings  
  _↳ feedback if chosen: Humans never grew wings._
- ◻️ losing the hands  
  _↳ feedback if chosen: The hands became more useful._
- ✅ making better tools

Full working after a second miss:

> The true statement is “making better tools”.  
> “the brain becoming smaller” is false: The brain became bigger.  
> “growing wings” is false: Humans never grew wings.  
> “losing the hands” is false: The hands became more useful.  

> Which change happened during humanisation?

- ◻️ losing the hands  
  _↳ feedback if chosen: The hands became more useful._
- ◻️ learning to drive  
  _↳ feedback if chosen: Cars came only recently._
- ✅ making better tools
- ◻️ growing wings  
  _↳ feedback if chosen: Humans never grew wings._

Full working after a second miss:

> The true statement is “making better tools”.  
> “losing the hands” is false: The hands became more useful.  
> “learning to drive” is false: Cars came only recently.  
> “growing wings” is false: Humans never grew wings.  

> Which change happened during humanisation?

- ✅ making better tools
- ◻️ losing the hands  
  _↳ feedback if chosen: The hands became more useful._
- ◻️ growing wings  
  _↳ feedback if chosen: Humans never grew wings._
- ◻️ the brain becoming smaller  
  _↳ feedback if chosen: The brain became bigger._

Full working after a second miss:

> The true statement is “making better tools”.  
> “losing the hands” is false: The hands became more useful.  
> “growing wings” is false: Humans never grew wings.  
> “the brain becoming smaller” is false: The brain became bigger.  

Sources: early-humans (Fossil finds in Africa (Toumaï, Lucy, Olduvai, Turkana, Sterkfontein, Jebel Irhoud) and the way of life of early humans; all dates are estimates)

### `hi9-where` · Lesson 9 · multiple choice, level 1

Prompt: Which site is {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| a rock shelter near Bamenda, used by people for many thousands of years | Shum Laka | Shum Laka: a rock shelter near Bamenda, used by people for many thousands of years. |
| an old village site near Yaoundé with pottery and oil-palm nuts | Obobogo | Obobogo: an old village site near Yaoundé with pottery and oil-palm nuts. |

Right answer: `{x.a}`; wrong choices: `Shum Laka`, `Obobogo`

- Feedback `other`: “Shum Laka is near Bamenda; Obobogo is near Yaoundé.”

Three generated variants:

> Which site is an old village site near Yaoundé with pottery and oil-palm nuts?

- ✅ Obobogo
- ◻️ Shum Laka  
  _↳ feedback if chosen: Shum Laka is near Bamenda; Obobogo is near Yaoundé._

Full working after a second miss:

> Obobogo: an old village site near Yaoundé with pottery and oil-palm nuts.  
> Answer: Obobogo.  

> Which site is a rock shelter near Bamenda, used by people for many thousands of years?

- ✅ Shum Laka
- ◻️ Obobogo  
  _↳ feedback if chosen: Shum Laka is near Bamenda; Obobogo is near Yaoundé._

Full working after a second miss:

> Shum Laka: a rock shelter near Bamenda, used by people for many thousands of years.  
> Answer: Shum Laka.  

> Which site is an old village site near Yaoundé with pottery and oil-palm nuts?

- ✅ Obobogo
- ◻️ Shum Laka  
  _↳ feedback if chosen: Shum Laka is near Bamenda; Obobogo is near Yaoundé._

Full working after a second miss:

> Obobogo: an old village site near Yaoundé with pottery and oil-palm nuts.  
> Answer: Obobogo.  

Sources: cameroon-neolithic (Neolithic archaeology in Cameroon: Shum Laka (near Bamenda), Obobogo (near Yaoundé))

### `hi9-find` · Lesson 9 · multiple choice, level 1

Prompt: Which of these was found at Neolithic sites in Cameroon?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ pottery
- ✅ polished stone axes
- ✅ oil-palm nuts
- ✅ stone tools
- ❌ iron trains  
  _↳ Trains are modern._
- ❌ plastic bottles  
  _↳ Plastic is modern._
- ❌ coins of the Central African franc  
  _↳ That money is modern._
- ❌ printed books  
  _↳ Printing is modern._


Three generated variants:

> Which of these was found at Neolithic sites in Cameroon?

- ◻️ iron trains  
  _↳ feedback if chosen: Trains are modern._
- ◻️ coins of the Central African franc  
  _↳ feedback if chosen: That money is modern._
- ◻️ printed books  
  _↳ feedback if chosen: Printing is modern._
- ✅ oil-palm nuts

Full working after a second miss:

> The true statement is “oil-palm nuts”.  
> “iron trains” is false: Trains are modern.  
> “coins of the Central African franc” is false: That money is modern.  
> “printed books” is false: Printing is modern.  

> Which of these was found at Neolithic sites in Cameroon?

- ◻️ coins of the Central African franc  
  _↳ feedback if chosen: That money is modern._
- ◻️ printed books  
  _↳ feedback if chosen: Printing is modern._
- ✅ stone tools
- ◻️ iron trains  
  _↳ feedback if chosen: Trains are modern._

Full working after a second miss:

> The true statement is “stone tools”.  
> “coins of the Central African franc” is false: That money is modern.  
> “printed books” is false: Printing is modern.  
> “iron trains” is false: Trains are modern.  

> Which of these was found at Neolithic sites in Cameroon?

- ✅ pottery
- ◻️ plastic bottles  
  _↳ feedback if chosen: Plastic is modern._
- ◻️ coins of the Central African franc  
  _↳ feedback if chosen: That money is modern._
- ◻️ iron trains  
  _↳ feedback if chosen: Trains are modern._

Full working after a second miss:

> The true statement is “pottery”.  
> “plastic bottles” is false: Plastic is modern.  
> “coins of the Central African franc” is false: That money is modern.  
> “iron trains” is false: Trains are modern.  

Sources: cameroon-neolithic (Neolithic archaeology in Cameroon: Shum Laka (near Bamenda), Obobogo (near Yaoundé))

### `hi9-show` · Lesson 9 · multiple choice, level 2

Prompt: What do the pots and polished axes found in Cameroon show?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ that Neolithic people lived there, cooking and storing food in pots and clearing land with axes
- ❌ that nobody lived in Cameroon long ago  
  _↳ The finds show that people lived there._
- ❌ that people used electricity  
  _↳ There was no electricity._
- ❌ that people bought pots in shops  
  _↳ They made the pots themselves._
- ❌ that the people had cars  
  _↳ There were no cars._


Three generated variants:

> What do the pots and polished axes found in Cameroon show?

- ◻️ that people bought pots in shops  
  _↳ feedback if chosen: They made the pots themselves._
- ◻️ that the people had cars  
  _↳ feedback if chosen: There were no cars._
- ✅ that Neolithic people lived there, cooking and storing food in pots and clearing land with axes
- ◻️ that people used electricity  
  _↳ feedback if chosen: There was no electricity._

Full working after a second miss:

> The true statement is “that Neolithic people lived there, cooking and storing food in pots and clearing land with axes”.  
> “that people bought pots in shops” is false: They made the pots themselves.  
> “that the people had cars” is false: There were no cars.  
> “that people used electricity” is false: There was no electricity.  

> What do the pots and polished axes found in Cameroon show?

- ◻️ that people used electricity  
  _↳ feedback if chosen: There was no electricity._
- ✅ that Neolithic people lived there, cooking and storing food in pots and clearing land with axes
- ◻️ that nobody lived in Cameroon long ago  
  _↳ feedback if chosen: The finds show that people lived there._
- ◻️ that the people had cars  
  _↳ feedback if chosen: There were no cars._

Full working after a second miss:

> The true statement is “that Neolithic people lived there, cooking and storing food in pots and clearing land with axes”.  
> “that people used electricity” is false: There was no electricity.  
> “that nobody lived in Cameroon long ago” is false: The finds show that people lived there.  
> “that the people had cars” is false: There were no cars.  

> What do the pots and polished axes found in Cameroon show?

- ◻️ that the people had cars  
  _↳ feedback if chosen: There were no cars._
- ◻️ that people bought pots in shops  
  _↳ feedback if chosen: They made the pots themselves._
- ◻️ that nobody lived in Cameroon long ago  
  _↳ feedback if chosen: The finds show that people lived there._
- ✅ that Neolithic people lived there, cooking and storing food in pots and clearing land with axes

Full working after a second miss:

> The true statement is “that Neolithic people lived there, cooking and storing food in pots and clearing land with axes”.  
> “that the people had cars” is false: There were no cars.  
> “that people bought pots in shops” is false: They made the pots themselves.  
> “that nobody lived in Cameroon long ago” is false: The finds show that people lived there.  

Sources: cameroon-neolithic (Neolithic archaeology in Cameroon: Shum Laka (near Bamenda), Obobogo (near Yaoundé))

### `hi9-sort` · Lesson 9 · matching, level 2

Prompt: Sort these: evidence of Neolithic life, or modern objects?

Pairs (6 shown each time, sorted into groups):

- broken clay pots → **Neolithic evidence**
- polished stone axes → **Neolithic evidence**
- old oil-palm nuts → **Neolithic evidence**
- stone hoes → **Neolithic evidence**
- a metal cooking pot from the market → **modern**
- a plastic bucket → **modern**
- a bicycle → **modern**
- a radio → **modern**


Three generated variants:

> Sort these: evidence of Neolithic life, or modern objects?

Groups: Neolithic evidence · modern
- polished stone axes → **Neolithic evidence**
- broken clay pots → **Neolithic evidence**
- a metal cooking pot from the market → **modern**
- stone hoes → **Neolithic evidence**
- a radio → **modern**
- a bicycle → **modern**

Full working after a second miss:

> The right pairs are:  
> polished stone axes → Neolithic evidence  
> broken clay pots → Neolithic evidence  
> a metal cooking pot from the market → modern  
> stone hoes → Neolithic evidence  
> a radio → modern  
> a bicycle → modern  

> Sort these: evidence of Neolithic life, or modern objects?

Groups: Neolithic evidence · modern
- stone hoes → **Neolithic evidence**
- a radio → **modern**
- old oil-palm nuts → **Neolithic evidence**
- a plastic bucket → **modern**
- polished stone axes → **Neolithic evidence**
- a metal cooking pot from the market → **modern**

Full working after a second miss:

> The right pairs are:  
> stone hoes → Neolithic evidence  
> a radio → modern  
> old oil-palm nuts → Neolithic evidence  
> a plastic bucket → modern  
> polished stone axes → Neolithic evidence  
> a metal cooking pot from the market → modern  

> Sort these: evidence of Neolithic life, or modern objects?

Groups: Neolithic evidence · modern
- a metal cooking pot from the market → **modern**
- a radio → **modern**
- a plastic bucket → **modern**
- a bicycle → **modern**
- polished stone axes → **Neolithic evidence**
- stone hoes → **Neolithic evidence**

Full working after a second miss:

> The right pairs are:  
> a metal cooking pot from the market → modern  
> a radio → modern  
> a plastic bucket → modern  
> a bicycle → modern  
> polished stone axes → Neolithic evidence  
> stone hoes → Neolithic evidence  

Sources: cameroon-neolithic (Neolithic archaeology in Cameroon: Shum Laka (near Bamenda), Obobogo (near Yaoundé)); stone-age (Old and New Stone Age (Palaeolithic and Neolithic); the Neolithic revolution)

### `hi9-spot` · Lesson 9 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Shum Laka is near Bamenda.
- ✅ Obobogo is near Yaoundé.
- ✅ Pottery has been found at Neolithic sites in Cameroon.
- ✅ Dates of old sites are estimates.
- ❌ Shum Laka is near Maroua.  
  _↳ Shum Laka is in the North-West region, near Bamenda._
- ❌ No one lived in Cameroon before the colonial period.  
  _↳ Archaeology shows people lived there for thousands of years._
- ❌ Obobogo is famous for its iron railway.  
  _↳ Obobogo is an old village site with pottery and stone axes._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ Pottery has been found at Neolithic sites in Cameroon.
- ◻️ Dates of old sites are estimates.
- ◻️ Obobogo is near Yaoundé.
- ✅ Obobogo is famous for its iron railway.  
  _↳ explanation: Obobogo is an old village site with pottery and stone axes._

Full working after a second miss:

> The wrong statement is “Obobogo is famous for its iron railway.”.  
> Obobogo is an old village site with pottery and stone axes.  

> One sentence is wrong. Which one?

- ◻️ Pottery has been found at Neolithic sites in Cameroon.
- ◻️ Dates of old sites are estimates.
- ◻️ Obobogo is near Yaoundé.
- ✅ Obobogo is famous for its iron railway.  
  _↳ explanation: Obobogo is an old village site with pottery and stone axes._

Full working after a second miss:

> The wrong statement is “Obobogo is famous for its iron railway.”.  
> Obobogo is an old village site with pottery and stone axes.  

> One sentence is wrong. Which one?

- ◻️ Pottery has been found at Neolithic sites in Cameroon.
- ✅ Obobogo is famous for its iron railway.  
  _↳ explanation: Obobogo is an old village site with pottery and stone axes._
- ◻️ Shum Laka is near Bamenda.
- ◻️ Dates of old sites are estimates.

Full working after a second miss:

> The wrong statement is “Obobogo is famous for its iron railway.”.  
> Obobogo is an old village site with pottery and stone axes.  

Sources: cameroon-neolithic (Neolithic archaeology in Cameroon: Shum Laka (near Bamenda), Obobogo (near Yaoundé))

### `hic9-3-check` · Lesson 9 · multiple choice, level 1

Prompt: Who studies old sites such as Shum Laka by digging carefully?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ archaeologists
- ❌ farmers  
  _↳ Farmers grow crops; archaeologists study old sites._
- ❌ doctors  
  _↳ Doctors treat patients._
- ❌ drivers  
  _↳ Drivers drive vehicles._
- ❌ tailors  
  _↳ Tailors make clothes._


Three generated variants:

> Who studies old sites such as Shum Laka by digging carefully?

- ◻️ tailors  
  _↳ feedback if chosen: Tailors make clothes._
- ◻️ doctors  
  _↳ feedback if chosen: Doctors treat patients._
- ✅ archaeologists
- ◻️ drivers  
  _↳ feedback if chosen: Drivers drive vehicles._

Full working after a second miss:

> The true statement is “archaeologists”.  
> “tailors” is false: Tailors make clothes.  
> “doctors” is false: Doctors treat patients.  
> “drivers” is false: Drivers drive vehicles.  

> Who studies old sites such as Shum Laka by digging carefully?

- ◻️ tailors  
  _↳ feedback if chosen: Tailors make clothes._
- ◻️ drivers  
  _↳ feedback if chosen: Drivers drive vehicles._
- ◻️ farmers  
  _↳ feedback if chosen: Farmers grow crops; archaeologists study old sites._
- ✅ archaeologists

Full working after a second miss:

> The true statement is “archaeologists”.  
> “tailors” is false: Tailors make clothes.  
> “drivers” is false: Drivers drive vehicles.  
> “farmers” is false: Farmers grow crops; archaeologists study old sites.  

> Who studies old sites such as Shum Laka by digging carefully?

- ◻️ drivers  
  _↳ feedback if chosen: Drivers drive vehicles._
- ◻️ tailors  
  _↳ feedback if chosen: Tailors make clothes._
- ✅ archaeologists
- ◻️ doctors  
  _↳ feedback if chosen: Doctors treat patients._

Full working after a second miss:

> The true statement is “archaeologists”.  
> “drivers” is false: Drivers drive vehicles.  
> “tailors” is false: Tailors make clothes.  
> “doctors” is false: Doctors treat patients.  

Sources: cameroon-neolithic (Neolithic archaeology in Cameroon: Shum Laka (near Bamenda), Obobogo (near Yaoundé))

### `hi10-where` · Lesson 10 · multiple choice, level 1

Prompt: Which forest people is this: {x.t}?

Table `x` (one row is picked each time):

| t | a | why |
|---|---|---|
| the largest group, living in the East and South regions | the Baka | The Baka: the largest group, living in the East and South regions. |
| living in the South region, near the coast (also called Bakola) | the Bagyeli | The Bagyeli: living in the South region, near the coast (also called Bakola). |
| living in the Centre region | the Bedzang | The Bedzang: living in the Centre region. |

Right answer: `{x.a}`; wrong choices: `the Baka`, `the Bagyeli`, `the Bedzang`

- Feedback `other`: “Not that people. Read where each group lives.”

Three generated variants:

> Which forest people is this: the largest group, living in the East and South regions?

- ◻️ the Bagyeli  
  _↳ feedback if chosen: Not that people. Read where each group lives._
- ◻️ the Bedzang  
  _↳ feedback if chosen: Not that people. Read where each group lives._
- ✅ the Baka

Full working after a second miss:

> The Baka: the largest group, living in the East and South regions.  
> Answer: the Baka.  

> Which forest people is this: living in the South region, near the coast (also called Bakola)?

- ◻️ the Bedzang  
  _↳ feedback if chosen: Not that people. Read where each group lives._
- ◻️ the Baka  
  _↳ feedback if chosen: Not that people. Read where each group lives._
- ✅ the Bagyeli

Full working after a second miss:

> The Bagyeli: living in the South region, near the coast (also called Bakola).  
> Answer: the Bagyeli.  

> Which forest people is this: the largest group, living in the East and South regions?

- ◻️ the Bagyeli  
  _↳ feedback if chosen: Not that people. Read where each group lives._
- ◻️ the Bedzang  
  _↳ feedback if chosen: Not that people. Read where each group lives._
- ✅ the Baka

Full working after a second miss:

> The Baka: the largest group, living in the East and South regions.  
> Answer: the Baka.  

Sources: forest-peoples (Cameroon's forest peoples: Baka, Bagyeli (Bakola), Bedzang; way of life and challenges)

### `hi10-life` · Lesson 10 · multiple choice, level 1

Prompt: Which is part of the traditional way of life of the forest peoples?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ gathering honey and wild yams
- ✅ hunting and fishing
- ✅ knowing forest medicines
- ✅ living in forest camps of leaf-covered huts
- ❌ working in factories  
  _↳ Their traditional life was in the forest._
- ❌ herding camels  
  _↳ Camels live in deserts, not rainforests._
- ❌ fishing at sea in big ships  
  _↳ They lived in the forest._
- ❌ growing wheat on large farms  
  _↳ Wheat is not a rainforest crop._


Three generated variants:

> Which is part of the traditional way of life of the forest peoples?

- ◻️ fishing at sea in big ships  
  _↳ feedback if chosen: They lived in the forest._
- ✅ gathering honey and wild yams
- ◻️ growing wheat on large farms  
  _↳ feedback if chosen: Wheat is not a rainforest crop._
- ◻️ herding camels  
  _↳ feedback if chosen: Camels live in deserts, not rainforests._

Full working after a second miss:

> The true statement is “gathering honey and wild yams”.  
> “fishing at sea in big ships” is false: They lived in the forest.  
> “growing wheat on large farms” is false: Wheat is not a rainforest crop.  
> “herding camels” is false: Camels live in deserts, not rainforests.  

> Which is part of the traditional way of life of the forest peoples?

- ✅ hunting and fishing
- ◻️ working in factories  
  _↳ feedback if chosen: Their traditional life was in the forest._
- ◻️ fishing at sea in big ships  
  _↳ feedback if chosen: They lived in the forest._
- ◻️ herding camels  
  _↳ feedback if chosen: Camels live in deserts, not rainforests._

Full working after a second miss:

> The true statement is “hunting and fishing”.  
> “working in factories” is false: Their traditional life was in the forest.  
> “fishing at sea in big ships” is false: They lived in the forest.  
> “herding camels” is false: Camels live in deserts, not rainforests.  

> Which is part of the traditional way of life of the forest peoples?

- ✅ gathering honey and wild yams
- ◻️ growing wheat on large farms  
  _↳ feedback if chosen: Wheat is not a rainforest crop._
- ◻️ herding camels  
  _↳ feedback if chosen: Camels live in deserts, not rainforests._
- ◻️ working in factories  
  _↳ feedback if chosen: Their traditional life was in the forest._

Full working after a second miss:

> The true statement is “gathering honey and wild yams”.  
> “growing wheat on large farms” is false: Wheat is not a rainforest crop.  
> “herding camels” is false: Camels live in deserts, not rainforests.  
> “working in factories” is false: Their traditional life was in the forest.  

Sources: forest-peoples (Cameroon's forest peoples: Baka, Bagyeli (Bakola), Bedzang; way of life and challenges)

### `hi10-name` · Lesson 10 · multiple choice, level 2

Prompt: What is the most respectful way to speak about the forest peoples?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ call each people by its own name, such as Baka or Bagyeli
- ❌ make jokes about their height  
  _↳ Jokes about people’s bodies are disrespectful._
- ❌ say they have no history  
  _↳ They have a long history in the forest._
- ❌ call them all by one word they may not like  
  _↳ Many prefer their own names._
- ❌ avoid learning about them  
  _↳ Learning about other peoples builds respect._


Three generated variants:

> What is the most respectful way to speak about the forest peoples?

- ◻️ avoid learning about them  
  _↳ feedback if chosen: Learning about other peoples builds respect._
- ◻️ make jokes about their height  
  _↳ feedback if chosen: Jokes about people’s bodies are disrespectful._
- ✅ call each people by its own name, such as Baka or Bagyeli
- ◻️ say they have no history  
  _↳ feedback if chosen: They have a long history in the forest._

Full working after a second miss:

> The true statement is “call each people by its own name, such as Baka or Bagyeli”.  
> “avoid learning about them” is false: Learning about other peoples builds respect.  
> “make jokes about their height” is false: Jokes about people’s bodies are disrespectful.  
> “say they have no history” is false: They have a long history in the forest.  

> What is the most respectful way to speak about the forest peoples?

- ◻️ make jokes about their height  
  _↳ feedback if chosen: Jokes about people’s bodies are disrespectful._
- ◻️ say they have no history  
  _↳ feedback if chosen: They have a long history in the forest._
- ◻️ avoid learning about them  
  _↳ feedback if chosen: Learning about other peoples builds respect._
- ✅ call each people by its own name, such as Baka or Bagyeli

Full working after a second miss:

> The true statement is “call each people by its own name, such as Baka or Bagyeli”.  
> “make jokes about their height” is false: Jokes about people’s bodies are disrespectful.  
> “say they have no history” is false: They have a long history in the forest.  
> “avoid learning about them” is false: Learning about other peoples builds respect.  

> What is the most respectful way to speak about the forest peoples?

- ◻️ call them all by one word they may not like  
  _↳ feedback if chosen: Many prefer their own names._
- ◻️ make jokes about their height  
  _↳ feedback if chosen: Jokes about people’s bodies are disrespectful._
- ✅ call each people by its own name, such as Baka or Bagyeli
- ◻️ say they have no history  
  _↳ feedback if chosen: They have a long history in the forest._

Full working after a second miss:

> The true statement is “call each people by its own name, such as Baka or Bagyeli”.  
> “call them all by one word they may not like” is false: Many prefer their own names.  
> “make jokes about their height” is false: Jokes about people’s bodies are disrespectful.  
> “say they have no history” is false: They have a long history in the forest.  

Sources: forest-peoples (Cameroon's forest peoples: Baka, Bagyeli (Bakola), Bedzang; way of life and challenges)

### `hi10-sort` · Lesson 10 · matching, level 2

Prompt: Sort these: traditional forest life, or a change of today?

Pairs (6 shown each time, sorted into groups):

- gathering honey → **traditional**
- hunting with nets → **traditional**
- moving between forest camps → **traditional**
- using forest medicines → **traditional**
- living in villages beside roads → **change of today**
- children going to school → **change of today**
- loss of forest from logging → **change of today**
- farming and trading with neighbours → **change of today**


Three generated variants:

> Sort these: traditional forest life, or a change of today?

Groups: traditional · change of today
- children going to school → **change of today**
- using forest medicines → **traditional**
- loss of forest from logging → **change of today**
- gathering honey → **traditional**
- living in villages beside roads → **change of today**
- moving between forest camps → **traditional**

Full working after a second miss:

> The right pairs are:  
> children going to school → change of today  
> using forest medicines → traditional  
> loss of forest from logging → change of today  
> gathering honey → traditional  
> living in villages beside roads → change of today  
> moving between forest camps → traditional  

> Sort these: traditional forest life, or a change of today?

Groups: traditional · change of today
- children going to school → **change of today**
- living in villages beside roads → **change of today**
- loss of forest from logging → **change of today**
- hunting with nets → **traditional**
- using forest medicines → **traditional**
- farming and trading with neighbours → **change of today**

Full working after a second miss:

> The right pairs are:  
> children going to school → change of today  
> living in villages beside roads → change of today  
> loss of forest from logging → change of today  
> hunting with nets → traditional  
> using forest medicines → traditional  
> farming and trading with neighbours → change of today  

> Sort these: traditional forest life, or a change of today?

Groups: traditional · change of today
- moving between forest camps → **traditional**
- loss of forest from logging → **change of today**
- gathering honey → **traditional**
- farming and trading with neighbours → **change of today**
- hunting with nets → **traditional**
- using forest medicines → **traditional**

Full working after a second miss:

> The right pairs are:  
> moving between forest camps → traditional  
> loss of forest from logging → change of today  
> gathering honey → traditional  
> farming and trading with neighbours → change of today  
> hunting with nets → traditional  
> using forest medicines → traditional  

Sources: forest-peoples (Cameroon's forest peoples: Baka, Bagyeli (Bakola), Bedzang; way of life and challenges)

### `hi10-spot` · Lesson 10 · spot the error, level 3

Prompt: One sentence is wrong. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The Baka live in the East and South regions.
- ✅ The forest peoples know many forest medicines.
- ✅ Loss of forest is a problem for the forest peoples.
- ✅ The Bagyeli are also called Bakola.
- ❌ The forest peoples have no history.  
  _↳ They have lived in the forest for a very long time._
- ❌ The Baka live mainly in the Far North desert.  
  _↳ They live in the rainforest of the East and South._
- ❌ The forest peoples have never had any knowledge of plants.  
  _↳ They have deep knowledge of forest plants._


Three generated variants:

> One sentence is wrong. Which one?

- ◻️ The Baka live in the East and South regions.
- ◻️ The forest peoples know many forest medicines.
- ◻️ Loss of forest is a problem for the forest peoples.
- ✅ The forest peoples have no history.  
  _↳ explanation: They have lived in the forest for a very long time._

Full working after a second miss:

> The wrong statement is “The forest peoples have no history.”.  
> They have lived in the forest for a very long time.  

> One sentence is wrong. Which one?

- ◻️ Loss of forest is a problem for the forest peoples.
- ◻️ The forest peoples know many forest medicines.
- ◻️ The Baka live in the East and South regions.
- ✅ The Baka live mainly in the Far North desert.  
  _↳ explanation: They live in the rainforest of the East and South._

Full working after a second miss:

> The wrong statement is “The Baka live mainly in the Far North desert.”.  
> They live in the rainforest of the East and South.  

> One sentence is wrong. Which one?

- ✅ The forest peoples have no history.  
  _↳ explanation: They have lived in the forest for a very long time._
- ◻️ Loss of forest is a problem for the forest peoples.
- ◻️ The Baka live in the East and South regions.
- ◻️ The Bagyeli are also called Bakola.

Full working after a second miss:

> The wrong statement is “The forest peoples have no history.”.  
> They have lived in the forest for a very long time.  

Sources: forest-peoples (Cameroon's forest peoples: Baka, Bagyeli (Bakola), Bedzang; way of life and challenges)

### `hic10-3-check` · Lesson 10 · multiple choice, level 1

Prompt: Which is a challenge facing forest peoples today?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ the loss of the forest
- ✅ rights over their land
- ✅ access to schools and health care
- ❌ too much snow  
  _↳ Cameroon’s rainforest has no snow._
- ❌ too many trains in the forest  
  _↳ That is not a challenge they face._
- ❌ having too much forest  
  _↳ The problem is losing forest._
- ❌ living in the desert  
  _↳ They live in the rainforest._


Three generated variants:

> Which is a challenge facing forest peoples today?

- ◻️ too much snow  
  _↳ feedback if chosen: Cameroon’s rainforest has no snow._
- ✅ the loss of the forest
- ◻️ too many trains in the forest  
  _↳ feedback if chosen: That is not a challenge they face._
- ◻️ having too much forest  
  _↳ feedback if chosen: The problem is losing forest._

Full working after a second miss:

> The true statement is “the loss of the forest”.  
> “too much snow” is false: Cameroon’s rainforest has no snow.  
> “too many trains in the forest” is false: That is not a challenge they face.  
> “having too much forest” is false: The problem is losing forest.  

> Which is a challenge facing forest peoples today?

- ◻️ having too much forest  
  _↳ feedback if chosen: The problem is losing forest._
- ◻️ too many trains in the forest  
  _↳ feedback if chosen: That is not a challenge they face._
- ✅ access to schools and health care
- ◻️ too much snow  
  _↳ feedback if chosen: Cameroon’s rainforest has no snow._

Full working after a second miss:

> The true statement is “access to schools and health care”.  
> “having too much forest” is false: The problem is losing forest.  
> “too many trains in the forest” is false: That is not a challenge they face.  
> “too much snow” is false: Cameroon’s rainforest has no snow.  

> Which is a challenge facing forest peoples today?

- ◻️ living in the desert  
  _↳ feedback if chosen: They live in the rainforest._
- ◻️ too much snow  
  _↳ feedback if chosen: Cameroon’s rainforest has no snow._
- ◻️ too many trains in the forest  
  _↳ feedback if chosen: That is not a challenge they face._
- ✅ rights over their land

Full working after a second miss:

> The true statement is “rights over their land”.  
> “living in the desert” is false: They live in the rainforest.  
> “too much snow” is false: Cameroon’s rainforest has no snow.  
> “too many trains in the forest” is false: That is not a challenge they face.  

Sources: forest-peoples (Cameroon's forest peoples: Baka, Bagyeli (Bakola), Bedzang; way of life and challenges)

