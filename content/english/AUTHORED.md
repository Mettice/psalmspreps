# English Form 1, Batch E1: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:english`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: word tables and rules (src/engine/lib/english.js)

**Irregular verbs (TR-E01)**: base → simple past → past participle

| Verb | Simple past | Past participle |
|---|---|---|
| be | was/were | been |
| become | became | become |
| begin | began | begun |
| break | broke | broken |
| bring | brought | brought |
| build | built | built |
| buy | bought | bought |
| catch | caught | caught |
| choose | chose | chosen |
| come | came | come |
| cost | cost | cost |
| cut | cut | cut |
| do | did | done |
| draw | drew | drawn |
| drink | drank | drunk |
| drive | drove | driven |
| eat | ate | eaten |
| fall | fell | fallen |
| feel | felt | felt |
| find | found | found |
| fly | flew | flown |
| forget | forgot | forgotten |
| get | got | got |
| give | gave | given |
| go | went | gone |
| grow | grew | grown |
| have | had | had |
| hear | heard | heard |
| keep | kept | kept |
| know | knew | known |
| leave | left | left |
| lend | lent | lent |
| lose | lost | lost |
| make | made | made |
| meet | met | met |
| pay | paid | paid |
| put | put | put |
| read | read | read |
| ride | rode | ridden |
| ring | rang | rung |
| run | ran | run |
| say | said | said |
| see | saw | seen |
| sell | sold | sold |
| send | sent | sent |
| sing | sang | sung |
| sit | sat | sat |
| sleep | slept | slept |
| speak | spoke | spoken |
| spend | spent | spent |
| stand | stood | stood |
| sweep | swept | swept |
| swim | swam | swum |
| take | took | taken |
| teach | taught | taught |
| tell | told | told |
| think | thought | thought |
| throw | threw | thrown |
| understand | understood | understood |
| wake | woke | woken |
| wear | wore | worn |
| win | won | won |
| write | wrote | written |

**Spelling rules (TR-E02, TR-E03)**, checked on known answers in `tests-js/english.test.js`:

- he/she/it form: add -es after s, sh, ch, x, z, o (washes, goes); consonant + y → -ies (carries); have → has.
- -ing: ie → ying (lying); drop a final e after a consonant (making), but see → seeing, be → being; double the last consonant (below).
- -ed: a final e adds -d (liked); consonant + y → -ied (carried); double the last consonant (below).
- Doubling: one-syllable verbs ending consonant + one vowel + consonant (not w, x, y): stop → stopped, run → running.
  Two-syllable verbs stressed on the last syllable: admit, begin, commit, control, forget, occur, permit, prefer, refer, regret, submit, upset.
  British English also doubles a final l after one vowel: travel → travelled, cancel → cancelled.
  Never doubled: visit, open, listen, happen, enter, answer, offer, order, wonder, remember, cover, suffer.

**a / an (TR-E04)**: by the first sound. “an” although a consonant letter: hour, honest, honour, heir. “a” although a vowel letter: university, uniform, unit, union, unique, user, useful, usual, utensil, European, one, once, ewe.

**Irregular plurals (TR-E05)**: child → children, man → men, woman → women, foot → feet, tooth → teeth, mouse → mice, person → people, knife → knives, wife → wives, leaf → leaves, loaf → loaves, life → lives, shelf → shelves, half → halves, sheep → sheep, fish → fish; -es after s, sh, ch, x, z and for tomato, potato, mango, hero, echo; consonant + y → -ies.

**Ordinal words (TR-E12)**: first, second, third, fifth, eighth, ninth, twelfth are special; -y → -ieth (twentieth); the rest add -th.

**Dates (TR-E16)**: dd/mm/yyyy (British order).

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `e1-reply` | 1 | multiple choice, 1 | introductions |
| 2 | `e1-greet` | 1 | fill the blank, 1 | introductions |
| 3 | `e1-build` | 1 | word order, 2 | introductions |
| 4 | `e1-dialogue` | 1 | ordering, 2 | introductions |
| 5 | `e1-spot` | 1 | spot the error, 3 | introductions |
| 6 | `c1-1-check` (card c1-1) | 1 | multiple choice, 1 | introductions |
| 7 | `c1-2-check` (card c1-2) | 1 | fill the blank, 1 | introductions |
| 8 | `e2-sort` | 2 | matching, 1 | daily-needs |
| 9 | `e2-capital` | 2 | multiple choice, 1 | spelling |
| 10 | `e2-spelling` | 2 | multiple choice, 1 | spelling |
| 11 | `e2-correct` | 2 | fill the blank, 2 | spelling |
| 12 | `e2-spot` | 2 | spot the error, 3 | spelling |
| 13 | `e3-spot` | 3 | spot the error, 3 | simple-present |
| 14 | `e5-account` | 5 | multiple choice, 2 | reading |
| 15 | `e5-irregular` | 5 | matching, 1 | irregular-verbs |
| 16 | `e6-spelling` | 6 | multiple choice, 2 | number-words |
| 17 | `c6-1-check` (card c6-1) | 6 | multiple choice, 1 | number-words |
| 18 | `e7-spot` | 7 | spot the error, 3 | present-continuous |
| 19 | `c9-1-check` (card c9-1) | 9 | matching, 1 | shopping-list |
| 20 | `c9-3-check` (card c9-3) | 9 | multiple choice, 1 | shopping-list |
| 21 | `e10-sort` | 10 | matching, 1 | countable |
| 22 | `e10-unit` | 10 | fill the blank, 2 | countable |
| 23 | `e10-spot` | 10 | spot the error, 3 | countable |
| 24 | `c10-3-check` (card c10-3) | 10 | fill the blank, 1 | countable |
| 25 | `e11-irregular` | 11 | matching, 1 | irregular-verbs |
| 26 | `e11-spot` | 11 | spot the error, 3 | simple-past |
| 27 | `e13-sort` | 13 | matching, 1 | transport |
| 28 | `e13-by` | 13 | fill the blank, 1 | transport |
| 29 | `e13-reply` | 13 | multiple choice, 1 | transport |
| 30 | `e13-build` | 13 | word order, 2 | transport |
| 31 | `e13-spot` | 13 | spot the error, 3 | transport |
| 32 | `e14-match` | 14 | matching, 1 | compounds |
| 33 | `e14-written` | 14 | multiple choice, 1 | compounds |
| 34 | `e14-class` | 14 | multiple choice, 1 | compounds |
| 35 | `e14-join` | 14 | fill the blank, 2 | compounds |
| 36 | `e14-convert` | 14 | fill the blank, 2 | compounds |
| 37 | `e14-spot` | 14 | spot the error, 3 | compounds |
| 38 | `e15-participle` | 15 | matching, 1 | irregular-verbs |
| 39 | `e15-spot` | 15 | spot the error, 3 | present-perfect |
| 40 | `c15-3-check` (card c15-3) | 15 | fill the blank, 1 | present-perfect |
| 41 | `c16-1-check` (card c16-1) | 16 | matching, 1 | forms |

### `e1-reply` · Lesson 1 · multiple choice, level 1

Prompt: Someone says: “{x.line}” What is the best reply?

Table `x` (one row is picked each time):

| line | right | w | why |
|---|---|---|---|
| Hello, my name is Enow. | Hello, Enow. My name is Mih. | Goodbye, Enow. · I am fine, thank you. · Yes, it is. | When someone tells you their name, greet them by name and give your own name. |
| Nice to meet you. | Nice to meet you too. | I am twelve years old. · Thank you, goodbye. · Yes, I am. | The polite reply to “Nice to meet you” is “Nice to meet you too.” |
| What is your name? | My name is Ndi. | I am from Wum. · I am fine. · Nice to meet you too. | “What is your name?” asks for a name: “My name is …”. |
| Where are you from? | I am from Buea. | My name is Ashu. · I am in Form One. · Good afternoon. | “Where are you from?” asks for a place: “I am from …”. |
| How are you? | I am fine, thank you. And you? | I am from Limbe. · My name is Ebai. · Nice to meet you too. | “How are you?” asks how you feel: “I am fine, thank you.” |
| This is my sister Manyi. | Hello, Manyi. Nice to meet you. | This is my sister too. · I am fine, thank you. · Goodbye, Manyi. | When someone is introduced to you, greet them by name and say “Nice to meet you.” |

Right answer: `{x.right}`; wrong choices: `{x.w[0]}`, `{x.w[1]}`, `{x.w[2]}`

- Feedback `off`: “That answer does not fit what was said. {x.why}”

Three generated variants:

> Someone says: “Hello, my name is Enow.” What is the best reply?

- ◻️ Goodbye, Enow.  
  _↳ feedback if chosen: That answer does not fit what was said. When someone tells you their name, greet them by name and give your own name._
- ✅ Hello, Enow. My name is Mih.
- ◻️ Yes, it is.  
  _↳ feedback if chosen: That answer does not fit what was said. When someone tells you their name, greet them by name and give your own name._
- ◻️ I am fine, thank you.  
  _↳ feedback if chosen: That answer does not fit what was said. When someone tells you their name, greet them by name and give your own name._

Full working after a second miss:

> “Hello, my name is Enow.” → “Hello, Enow. My name is Mih.”  
> When someone tells you their name, greet them by name and give your own name.  

> Someone says: “How are you?” What is the best reply?

- ◻️ I am from Limbe.  
  _↳ feedback if chosen: That answer does not fit what was said. “How are you?” asks how you feel: “I am fine, thank you.”_
- ✅ I am fine, thank you. And you?
- ◻️ Nice to meet you too.  
  _↳ feedback if chosen: That answer does not fit what was said. “How are you?” asks how you feel: “I am fine, thank you.”_
- ◻️ My name is Ebai.  
  _↳ feedback if chosen: That answer does not fit what was said. “How are you?” asks how you feel: “I am fine, thank you.”_

Full working after a second miss:

> “How are you?” → “I am fine, thank you. And you?”  
> “How are you?” asks how you feel: “I am fine, thank you.”  

> Someone says: “This is my sister Manyi.” What is the best reply?

- ✅ Hello, Manyi. Nice to meet you.
- ◻️ Goodbye, Manyi.  
  _↳ feedback if chosen: That answer does not fit what was said. When someone is introduced to you, greet them by name and say “Nice to meet you.”_
- ◻️ This is my sister too.  
  _↳ feedback if chosen: That answer does not fit what was said. When someone is introduced to you, greet them by name and say “Nice to meet you.”_
- ◻️ I am fine, thank you.  
  _↳ feedback if chosen: That answer does not fit what was said. When someone is introduced to you, greet them by name and say “Nice to meet you.”_

Full working after a second miss:

> “This is my sister Manyi.” → “Hello, Manyi. Nice to meet you.”  
> When someone is introduced to you, greet them by name and say “Nice to meet you.”  

Sources: introductions (Functional English for greetings and introductions, as in Cameroon Form 1 English course books)

### `e1-greet` · Lesson 1 · fill the blank, level 1

Prompt: Choose the greeting that fits.
Sentence: You meet your principal {t.when}. You say: “___, sir.”
Right answer: `t.g`

Table `t` (one row is picked each time):

| when | g |
|---|---|
| at seven o'clock in the morning | Good morning |
| at ten o'clock in the morning | Good morning |
| at two o'clock in the afternoon | Good afternoon |
| at four o'clock in the afternoon | Good afternoon |
| at eight o'clock in the evening | Good evening |

Choices: `Good morning`, `Good afternoon`, `Good evening`, `Good night`

- Feedback `morning`: “Good morning is for the morning, before midday.”
- Feedback `afternoon`: “Good afternoon is for the time after midday until about five or six o'clock.”
- Feedback `evening`: “Good evening is for the evening.”
- Feedback `night`: “Good night is said when leaving at night or before going to bed, not to greet someone.”

Three generated variants:

> Choose the greeting that fits.

Sentence: **You meet your principal at two o'clock in the afternoon. You say: “___, sir.”**
- ◻️ Good night  
  _↳ feedback if chosen: Good night is said when leaving at night or before going to bed, not to greet someone._
- ✅ Good afternoon
- ◻️ Good morning  
  _↳ feedback if chosen: Good morning is for the morning, before midday._

Full working after a second miss:

> The missing words are “Good afternoon”.  
> You meet your principal at two o'clock in the afternoon. You say: “Good afternoon, sir.”  

> Choose the greeting that fits.

Sentence: **You meet your principal at four o'clock in the afternoon. You say: “___, sir.”**
- ✅ Good afternoon
- ◻️ Good night  
  _↳ feedback if chosen: Good night is said when leaving at night or before going to bed, not to greet someone._
- ◻️ Good morning  
  _↳ feedback if chosen: Good morning is for the morning, before midday._

Full working after a second miss:

> The missing words are “Good afternoon”.  
> You meet your principal at four o'clock in the afternoon. You say: “Good afternoon, sir.”  

> Choose the greeting that fits.

Sentence: **You meet your principal at two o'clock in the afternoon. You say: “___, sir.”**
- ✅ Good afternoon
- ◻️ Good evening  
  _↳ feedback if chosen: Good evening is for the evening._
- ◻️ Good morning  
  _↳ feedback if chosen: Good morning is for the morning, before midday._

Full working after a second miss:

> The missing words are “Good afternoon”.  
> You meet your principal at two o'clock in the afternoon. You say: “Good afternoon, sir.”  

Sources: introductions (Functional English for greetings and introductions, as in Cameroon Form 1 English course books)

### `e1-build` · Lesson 1 · word order, level 2

Prompt: Tap the words in the right order.

Table `x` (one row is picked each time):

| a | alt |
|---|---|
| This is my friend Ayuk. | This is my friend Ayuk. |
| My name is Bih and I am from Kumbo. | I am from Kumbo and my name is Bih. |
| Mummy, meet my classmate Tabe. | Mummy, meet my classmate Tabe. |
| Nice to meet you too. | Nice to meet you too. |
| Where are you from, Ewane? | Where are you from, Ewane? |
| I am in Form One at this school. | I am in Form One at this school. |

Sentence(s): {x.a} (also accepted: {x.alt})


Three generated variants:

> Tap the words in the right order.

Tiles: and · Kumbo · My · am · from · Bih · name · is · I (then “.”)
Answer: **My name is Bih and I am from Kumbo.**

Full working after a second miss:

> The sentence is: My name is Bih and I am from Kumbo.  

> Tap the words in the right order.

Tiles: classmate · Tabe · Mummy, · my · meet (then “.”)
Answer: **Mummy, meet my classmate Tabe.**

Full working after a second miss:

> The sentence is: Mummy, meet my classmate Tabe.  

> Tap the words in the right order.

Tiles: from, · Where · Ewane · you · are (then “?”)
Answer: **Where are you from, Ewane?**

Full working after a second miss:

> The sentence is: Where are you from, Ewane?  

Sources: introductions (Functional English for greetings and introductions, as in Cameroon Form 1 English course books)

### `e1-dialogue` · Lesson 1 · ordering, level 2

Prompt: Put the conversation in order.

Items in the right order:

1. {names[0]}: Good morning. My name is {names[0]}.
2. {names[1]}: Good morning, {names[0]}. My name is {names[1]}.
3. {names[0]}: {names[1]}, this is my friend {names[2]}.
4. {names[1]}: Nice to meet you, {names[2]}.
5. {names[2]}: Nice to meet you too.


Three generated variants:

> Put the conversation in order.

Shown as: Bih: Nice to meet you, Ewane. · Bih: Good morning, Ayuk. My name is Bih. · Ayuk: Bih, this is my friend Ewane. · Ayuk: Good morning. My name is Ayuk. · Ewane: Nice to meet you too.
Correct order: Ayuk: Good morning. My name is Ayuk. → Bih: Good morning, Ayuk. My name is Bih. → Ayuk: Bih, this is my friend Ewane. → Bih: Nice to meet you, Ewane. → Ewane: Nice to meet you too.

Full working after a second miss:

> The correct order is: Ayuk: Good morning. My name is Ayuk. → Bih: Good morning, Ayuk. My name is Bih. → Ayuk: Bih, this is my friend Ewane. → Bih: Nice to meet you, Ewane. → Ewane: Nice to meet you too..  

> Put the conversation in order.

Shown as: Tabe: Nice to meet you, Ashu. · Tabe: Good morning, Ewane. My name is Tabe. · Ewane: Good morning. My name is Ewane. · Ewane: Tabe, this is my friend Ashu. · Ashu: Nice to meet you too.
Correct order: Ewane: Good morning. My name is Ewane. → Tabe: Good morning, Ewane. My name is Tabe. → Ewane: Tabe, this is my friend Ashu. → Tabe: Nice to meet you, Ashu. → Ashu: Nice to meet you too.

Full working after a second miss:

> The correct order is: Ewane: Good morning. My name is Ewane. → Tabe: Good morning, Ewane. My name is Tabe. → Ewane: Tabe, this is my friend Ashu. → Tabe: Nice to meet you, Ashu. → Ashu: Nice to meet you too..  

> Put the conversation in order.

Shown as: Ashu: Good morning, Ewane. My name is Ashu. · Ewane: Good morning. My name is Ewane. · Ndi: Nice to meet you too. · Ewane: Ashu, this is my friend Ndi. · Ashu: Nice to meet you, Ndi.
Correct order: Ewane: Good morning. My name is Ewane. → Ashu: Good morning, Ewane. My name is Ashu. → Ewane: Ashu, this is my friend Ndi. → Ashu: Nice to meet you, Ndi. → Ndi: Nice to meet you too.

Full working after a second miss:

> The correct order is: Ewane: Good morning. My name is Ewane. → Ashu: Good morning, Ewane. My name is Ashu. → Ewane: Ashu, this is my friend Ndi. → Ashu: Nice to meet you, Ndi. → Ndi: Nice to meet you too..  

Sources: introductions (Functional English for greetings and introductions, as in Cameroon Form 1 English course books)

### `e1-spot` · Lesson 1 · spot the error, level 3

Prompt: Each line is a question and its answer. One answer does not fit its question. Which one?

`n`: Enow · Mih · Ashu · Ebai

`f`: Tabe · Ndi · Manyi · Ewane

`t`: Buea · Kumbo · Mamfe · Limbe

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ “What is your name?” — “My name is {n}.”
- ✅ “Where are you from?” — “I am from {t}.”
- ✅ “How are you?” — “I am fine, thank you.”
- ✅ “Nice to meet you.” — “Nice to meet you too.”
- ✅ “This is my friend {f}.” — “Hello, {f}. Nice to meet you.”
- ❌ “What is your name?” — “I am from {t}.”  
  _↳ The question asks for a name. The answer should be “My name is …”._
- ❌ “How are you?” — “My name is {n}.”  
  _↳ “How are you?” asks how you feel. The answer should be “I am fine, thank you.”_
- ❌ “Where are you from?” — “I am fine, thank you.”  
  _↳ “Where are you from?” asks for a place. The answer should be “I am from …”._
- ❌ “Nice to meet you.” — “Yes, it is.”  
  _↳ The polite reply is “Nice to meet you too.”_


Three generated variants:

> Each line is a question and its answer. One answer does not fit its question. Which one?

- ◻️ “What is your name?” — “My name is Mih.”
- ✅ “How are you?” — “My name is Mih.”  
  _↳ explanation: “How are you?” asks how you feel. The answer should be “I am fine, thank you.”_
- ◻️ “Where are you from?” — “I am from Limbe.”
- ◻️ “How are you?” — “I am fine, thank you.”

Full working after a second miss:

> The wrong statement is ““How are you?” — “My name is Mih.””.  
> “How are you?” asks how you feel. The answer should be “I am fine, thank you.”  

> Each line is a question and its answer. One answer does not fit its question. Which one?

- ◻️ “Where are you from?” — “I am from Limbe.”
- ◻️ “What is your name?” — “My name is Ashu.”
- ✅ “What is your name?” — “I am from Limbe.”  
  _↳ explanation: The question asks for a name. The answer should be “My name is …”._
- ◻️ “This is my friend Manyi.” — “Hello, Manyi. Nice to meet you.”

Full working after a second miss:

> The wrong statement is ““What is your name?” — “I am from Limbe.””.  
> The question asks for a name. The answer should be “My name is …”.  

> Each line is a question and its answer. One answer does not fit its question. Which one?

- ◻️ “Nice to meet you.” — “Nice to meet you too.”
- ◻️ “Where are you from?” — “I am from Mamfe.”
- ✅ “Where are you from?” — “I am fine, thank you.”  
  _↳ explanation: “Where are you from?” asks for a place. The answer should be “I am from …”._
- ◻️ “This is my friend Tabe.” — “Hello, Tabe. Nice to meet you.”

Full working after a second miss:

> The wrong statement is ““Where are you from?” — “I am fine, thank you.””.  
> “Where are you from?” asks for a place. The answer should be “I am from …”.  

Sources: introductions (Functional English for greetings and introductions, as in Cameroon Form 1 English course books)

### `c1-1-check` · Lesson 1 · multiple choice, level 1

Prompt: Which is the best way to introduce yourself to a new classmate?

`n`: Enow · Mih · Ashu · Ebai · Manyi

`t`: Buea · Kumbo · Mamfe · Limbe · Wum

Shows 1 true and 3 false statement(s), drawn from:

- ✅ “Hello, my name is {n}. I am from {t}.”
- ❌ “My name {n}. From {t}.”  
  _↳ Use full sentences: “My name is …”, “I am from …”._
- ❌ “Goodbye. I am {n}.”  
  _↳ “Goodbye” is for leaving, not for meeting someone._
- ❌ “What is your name? Nice to meet you too.”  
  _↳ Give your own name first; “Nice to meet you too” is a reply._
- ❌ “Hey you! Where are you from?”  
  _↳ “Hey you!” is not polite. Greet and give your name first._


Three generated variants:

> Which is the best way to introduce yourself to a new classmate?

- ✅ “Hello, my name is Enow. I am from Limbe.”
- ◻️ “What is your name? Nice to meet you too.”  
  _↳ feedback if chosen: Give your own name first; “Nice to meet you too” is a reply._
- ◻️ “My name Enow. From Limbe.”  
  _↳ feedback if chosen: Use full sentences: “My name is …”, “I am from …”._
- ◻️ “Goodbye. I am Enow.”  
  _↳ feedback if chosen: “Goodbye” is for leaving, not for meeting someone._

Full working after a second miss:

> The true statement is ““Hello, my name is Enow. I am from Limbe.””.  
> ““What is your name? Nice to meet you too.”” is false: Give your own name first; “Nice to meet you too” is a reply.  
> ““My name Enow. From Limbe.”” is false: Use full sentences: “My name is …”, “I am from …”.  
> ““Goodbye. I am Enow.”” is false: “Goodbye” is for leaving, not for meeting someone.  

> Which is the best way to introduce yourself to a new classmate?

- ◻️ “Goodbye. I am Ashu.”  
  _↳ feedback if chosen: “Goodbye” is for leaving, not for meeting someone._
- ◻️ “What is your name? Nice to meet you too.”  
  _↳ feedback if chosen: Give your own name first; “Nice to meet you too” is a reply._
- ◻️ “My name Ashu. From Mamfe.”  
  _↳ feedback if chosen: Use full sentences: “My name is …”, “I am from …”._
- ✅ “Hello, my name is Ashu. I am from Mamfe.”

Full working after a second miss:

> The true statement is ““Hello, my name is Ashu. I am from Mamfe.””.  
> ““Goodbye. I am Ashu.”” is false: “Goodbye” is for leaving, not for meeting someone.  
> ““What is your name? Nice to meet you too.”” is false: Give your own name first; “Nice to meet you too” is a reply.  
> ““My name Ashu. From Mamfe.”” is false: Use full sentences: “My name is …”, “I am from …”.  

> Which is the best way to introduce yourself to a new classmate?

- ◻️ “Hey you! Where are you from?”  
  _↳ feedback if chosen: “Hey you!” is not polite. Greet and give your name first._
- ◻️ “What is your name? Nice to meet you too.”  
  _↳ feedback if chosen: Give your own name first; “Nice to meet you too” is a reply._
- ✅ “Hello, my name is Manyi. I am from Wum.”
- ◻️ “My name Manyi. From Wum.”  
  _↳ feedback if chosen: Use full sentences: “My name is …”, “I am from …”._

Full working after a second miss:

> The true statement is ““Hello, my name is Manyi. I am from Wum.””.  
> ““Hey you! Where are you from?”” is false: “Hey you!” is not polite. Greet and give your name first.  
> ““What is your name? Nice to meet you too.”” is false: Give your own name first; “Nice to meet you too” is a reply.  
> ““My name Manyi. From Wum.”” is false: Use full sentences: “My name is …”, “I am from …”.  

Sources: introductions (Functional English for greetings and introductions, as in Cameroon Form 1 English course books)

### `c1-2-check` · Lesson 1 · fill the blank, level 1

Prompt: Choose the words that fit.
Sentence: Mummy, ___ my {y} {x}.
Right answer: `'this is'`

`x`: Mih · Ewane · Ndip · Akwen

`y`: friend · cousin · classmate · brother

Choices: `he is`, `it is`, `there is`

- Feedback `pronoun`: “To introduce someone, we say “This is …”, not “He is …”.”
- Feedback `it`: ““It” is for things, not people. Say “This is …”.”
- Feedback `there`: ““There is” tells that something exists. To introduce someone, say “This is …”.”

Three generated variants:

> Choose the words that fit.

Sentence: **Mummy, ___ my brother Ndip.**
- ✅ this is
- ◻️ he is  
  _↳ feedback if chosen: To introduce someone, we say “This is …”, not “He is …”._
- ◻️ it is  
  _↳ feedback if chosen: “It” is for things, not people. Say “This is …”._

Full working after a second miss:

> The missing words are “this is”.  
> Mummy, this is my brother Ndip.  

> Choose the words that fit.

Sentence: **Mummy, ___ my cousin Ewane.**
- ◻️ there is  
  _↳ feedback if chosen: “There is” tells that something exists. To introduce someone, say “This is …”._
- ◻️ he is  
  _↳ feedback if chosen: To introduce someone, we say “This is …”, not “He is …”._
- ✅ this is

Full working after a second miss:

> The missing words are “this is”.  
> Mummy, this is my cousin Ewane.  

> Choose the words that fit.

Sentence: **Mummy, ___ my classmate Ndip.**
- ✅ this is
- ◻️ he is  
  _↳ feedback if chosen: To introduce someone, we say “This is …”, not “He is …”._
- ◻️ it is  
  _↳ feedback if chosen: “It” is for things, not people. Say “This is …”._

Full working after a second miss:

> The missing words are “this is”.  
> Mummy, this is my classmate Ndip.  

Sources: introductions (Functional English for greetings and introductions, as in Cameroon Form 1 English course books)

### `e2-sort` · Lesson 2 · matching, level 1

Prompt: Sort each word into its group.

Pairs (6 shown each time, sorted into groups):

- rice → **food**
- beans → **food**
- plantains → **food**
- bread → **food**
- fish → **food**
- shirt → **clothing**
- uniform → **clothing**
- sandals → **clothing**
- dress → **clothing**
- trousers → **clothing**
- soap → **keeping clean**
- toothbrush → **keeping clean**
- toothpaste → **keeping clean**
- sponge → **keeping clean**


Three generated variants:

> Sort each word into its group.

Groups: food · clothing · keeping clean
- toothpaste → **keeping clean**
- fish → **food**
- toothbrush → **keeping clean**
- dress → **clothing**
- soap → **keeping clean**
- sponge → **keeping clean**

Full working after a second miss:

> The right pairs are:  
> toothpaste → keeping clean  
> fish → food  
> toothbrush → keeping clean  
> dress → clothing  
> soap → keeping clean  
> sponge → keeping clean  

> Sort each word into its group.

Groups: food · clothing · keeping clean
- sandals → **clothing**
- rice → **food**
- plantains → **food**
- toothbrush → **keeping clean**
- sponge → **keeping clean**
- beans → **food**

Full working after a second miss:

> The right pairs are:  
> sandals → clothing  
> rice → food  
> plantains → food  
> toothbrush → keeping clean  
> sponge → keeping clean  
> beans → food  

> Sort each word into its group.

Groups: food · clothing · keeping clean
- plantains → **food**
- dress → **clothing**
- toothbrush → **keeping clean**
- uniform → **clothing**
- toothpaste → **keeping clean**
- trousers → **clothing**

Full working after a second miss:

> The right pairs are:  
> plantains → food  
> dress → clothing  
> toothbrush → keeping clean  
> uniform → clothing  
> toothpaste → keeping clean  
> trousers → clothing  

Sources: daily-needs (Everyday vocabulary: food, clothing, keeping clean (Form 1 syllabus theme “Satisfying basic daily needs”))

### `e2-capital` · Lesson 2 · multiple choice, level 1

Prompt: Which word in this sentence needs a capital letter? / “{k == 'n' ? lowerAll(n) : n} bought {it} in {k == 't' ? lowerAll(t) : t} on {k == 'd' ? lowerAll(d) : d}.”

`n`: Ayuk · Bih · Ndi · Ewane · Manyi

`t`: Bamenda · Buea · Kumba · Limbe · Mamfe

`d`: Monday · Tuesday · Friday · Saturday

`it`: rice · soap · plantains · salt · bread

`k`: n · t · d

Right answer: `{k == 'n' ? lowerAll(n) : k == 't' ? lowerAll(t) : lowerAll(d)}`; wrong choices: `{it}`, `bought`, `on`

- Feedback `common`: ““{it}” is an ordinary word, not a name: no capital letter.”
- Feedback `verb`: ““bought” is an ordinary word in the middle of the sentence: no capital letter.”
- Feedback `small`: ““on” is a small ordinary word: no capital letter.”

Three generated variants:

> Which word in this sentence needs a capital letter?
> “manyi bought plantains in Bamenda on Tuesday.”

- ◻️ plantains  
  _↳ feedback if chosen: “plantains” is an ordinary word, not a name: no capital letter._
- ◻️ bought  
  _↳ feedback if chosen: “bought” is an ordinary word in the middle of the sentence: no capital letter._
- ✅ manyi
- ◻️ on  
  _↳ feedback if chosen: “on” is a small ordinary word: no capital letter._

Full working after a second miss:

> “manyi” is the name of a person, so it needs a capital letter: Manyi.  
> Manyi bought plantains in Bamenda on Tuesday.  

> Which word in this sentence needs a capital letter?
> “Ayuk bought rice in limbe on Monday.”

- ◻️ bought  
  _↳ feedback if chosen: “bought” is an ordinary word in the middle of the sentence: no capital letter._
- ◻️ on  
  _↳ feedback if chosen: “on” is a small ordinary word: no capital letter._
- ◻️ rice  
  _↳ feedback if chosen: “rice” is an ordinary word, not a name: no capital letter._
- ✅ limbe

Full working after a second miss:

> “limbe” is the name of a town, so it needs a capital letter: Limbe.  
> Ayuk bought rice in Limbe on Monday.  

> Which word in this sentence needs a capital letter?
> “ewane bought plantains in Buea on Saturday.”

- ◻️ plantains  
  _↳ feedback if chosen: “plantains” is an ordinary word, not a name: no capital letter._
- ✅ ewane
- ◻️ on  
  _↳ feedback if chosen: “on” is a small ordinary word: no capital letter._
- ◻️ bought  
  _↳ feedback if chosen: “bought” is an ordinary word in the middle of the sentence: no capital letter._

Full working after a second miss:

> “ewane” is the name of a person, so it needs a capital letter: Ewane.  
> Ewane bought plantains in Buea on Saturday.  

Sources: spelling (Cambridge Dictionary / Oxford Learner's Dictionaries for the spelling of each word; capital-letter conventions)

### `e2-spelling` · Lesson 2 · multiple choice, level 1

Prompt: Which word is spelt correctly?

Table `w` (one row is picked each time):

| right | w |
|---|---|
| Wednesday | Wensday · Wednesay · Wenesday |
| February | Febuary · Febraury · Februery |
| vegetables | vegitables · vegetabels · vejetables |
| necessary | neccessary · necessery · nesessary |
| blanket | blankit · blancket · blankett |
| soap | sope · soop · saop |
| bucket | bukket · buckit · buket |
| mattress | matress · mattres · matres |
| toothpaste | toothpast · tothpaste · toothpaist |
| tomatoes | tomatos · tomattoes · tommatoes |
| sandals | sandles · sandels · sandalls |
| clothes | clotes · cloths · clothse |

Right answer: `{w.right}`; wrong choices: `{w.w[0]}`, `{w.w[1]}`, `{w.w[2]}`

- Feedback `letters`: “Not quite. Say the word slowly and look at each letter again.”

Three generated variants:

> Which word is spelt correctly?

- ✅ bucket
- ◻️ bukket  
  _↳ feedback if chosen: Not quite. Say the word slowly and look at each letter again._
- ◻️ buckit  
  _↳ feedback if chosen: Not quite. Say the word slowly and look at each letter again._
- ◻️ buket  
  _↳ feedback if chosen: Not quite. Say the word slowly and look at each letter again._

Full working after a second miss:

> The correct spelling is “bucket”.  

> Which word is spelt correctly?

- ◻️ Februery  
  _↳ feedback if chosen: Not quite. Say the word slowly and look at each letter again._
- ✅ February
- ◻️ Febuary  
  _↳ feedback if chosen: Not quite. Say the word slowly and look at each letter again._
- ◻️ Febraury  
  _↳ feedback if chosen: Not quite. Say the word slowly and look at each letter again._

Full working after a second miss:

> The correct spelling is “February”.  

> Which word is spelt correctly?

- ◻️ tomattoes  
  _↳ feedback if chosen: Not quite. Say the word slowly and look at each letter again._
- ◻️ tommatoes  
  _↳ feedback if chosen: Not quite. Say the word slowly and look at each letter again._
- ✅ tomatoes
- ◻️ tomatos  
  _↳ feedback if chosen: Not quite. Say the word slowly and look at each letter again._

Full working after a second miss:

> The correct spelling is “tomatoes”.  

Sources: spelling (Cambridge Dictionary / Oxford Learner's Dictionaries for the spelling of each word; capital-letter conventions)

### `e2-correct` · Lesson 2 · fill the blank, level 2

Prompt: The word in brackets is misspelt. Write it correctly.
Sentence: {x.frame} ({x.wrong})
Right answer: `x.right`

Table `x` (one row is picked each time):

| frame | wrong | right |
|---|---|---|
| We buy fresh ___ at the market every Saturday. | vejetables | vegetables |
| Mother washed all our school ___ on Sunday. | clotes | clothes |
| I wash my hands with ___ and water. | sope | soap |
| Kumbo is cold at night, so we sleep under a thick ___. | blankit | blanket |
| Bih fetched a ___ of water from the tap. | buckit | bucket |
| My birthday is in ___. | Febuary | February |
| We have Sports on ___ afternoon. | Wensday | Wednesday |
| Squeeze a little ___ onto your toothbrush. | toothpast | toothpaste |

- Feedback `copied` (typed `x.wrong`): “That is the misspelt word. Look at each letter again.”

Three generated variants:

> The word in brackets is misspelt. Write it correctly.

Sentence: **My birthday is in ___. (Febuary)**
Typed answer accepted (case and extra spaces ignored): **february**
- Typed **Febuary** (copied) → “That is the misspelt word. Look at each letter again.”

Full working after a second miss:

> The missing word is “February”.  
> My birthday is in February. (Febuary)  

> The word in brackets is misspelt. Write it correctly.

Sentence: **Squeeze a little ___ onto your toothbrush. (toothpast)**
Typed answer accepted (case and extra spaces ignored): **toothpaste**
- Typed **toothpast** (copied) → “That is the misspelt word. Look at each letter again.”

Full working after a second miss:

> The missing word is “toothpaste”.  
> Squeeze a little toothpaste onto your toothbrush. (toothpast)  

> The word in brackets is misspelt. Write it correctly.

Sentence: **Squeeze a little ___ onto your toothbrush. (toothpast)**
Typed answer accepted (case and extra spaces ignored): **toothpaste**
- Typed **toothpast** (copied) → “That is the misspelt word. Look at each letter again.”

Full working after a second miss:

> The missing word is “toothpaste”.  
> Squeeze a little toothpaste onto your toothbrush. (toothpast)  

Sources: spelling (Cambridge Dictionary / Oxford Learner's Dictionaries for the spelling of each word; capital-letter conventions)

### `e2-spot` · Lesson 2 · spot the error, level 3

Prompt: One sentence has a mistake in capital letters or spelling. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Bih goes to the market on Saturday.
- ✅ I need soap and a toothbrush.
- ✅ Our school uniform is blue and white.
- ✅ Ayuk lives in Bamenda with his grandmother.
- ✅ We eat rice and beans on Sundays.
- ❌ Ewane lives in limbe.  
  _↳ Limbe is the name of a town: it needs a capital L._
- ❌ Every morning i make my bed.  
  _↳ The word I is always a capital letter._
- ❌ We buy bred at the bakery.  
  _↳ The correct spelling is bread._
- ❌ My birthday is in febuary.  
  _↳ Months take a capital letter, and the spelling is February._
- ❌ my brother likes plantains.  
  _↳ A sentence starts with a capital letter: My._


Three generated variants:

> One sentence has a mistake in capital letters or spelling. Which one?

- ◻️ Ayuk lives in Bamenda with his grandmother.
- ◻️ We eat rice and beans on Sundays.
- ◻️ Bih goes to the market on Saturday.
- ✅ my brother likes plantains.  
  _↳ explanation: A sentence starts with a capital letter: My._

Full working after a second miss:

> The wrong statement is “my brother likes plantains.”.  
> A sentence starts with a capital letter: My.  

> One sentence has a mistake in capital letters or spelling. Which one?

- ◻️ We eat rice and beans on Sundays.
- ◻️ Ayuk lives in Bamenda with his grandmother.
- ✅ My birthday is in febuary.  
  _↳ explanation: Months take a capital letter, and the spelling is February._
- ◻️ Bih goes to the market on Saturday.

Full working after a second miss:

> The wrong statement is “My birthday is in febuary.”.  
> Months take a capital letter, and the spelling is February.  

> One sentence has a mistake in capital letters or spelling. Which one?

- ◻️ We eat rice and beans on Sundays.
- ◻️ I need soap and a toothbrush.
- ◻️ Ayuk lives in Bamenda with his grandmother.
- ✅ Every morning i make my bed.  
  _↳ explanation: The word I is always a capital letter._

Full working after a second miss:

> The wrong statement is “Every morning i make my bed.”.  
> The word I is always a capital letter.  

Sources: spelling (Cambridge Dictionary / Oxford Learner's Dictionaries for the spelling of each word; capital-letter conventions)

### `e3-spot` · Lesson 3 · spot the error, level 3

Prompt: One sentence has a mistake. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Ayuk washes his uniform on Saturdays.
- ✅ Do you like puff-puff?
- ✅ My sisters don't drink coffee.
- ✅ Does Tabe carry water every morning?
- ✅ We go to church on Sundays.
- ✅ Mih studies in the evening.
- ❌ Bih don't like fish.  
  _↳ Bih is one person (she): Bih doesn't like fish._
- ❌ Does Ndi plays football?  
  _↳ After does, the verb has no -s: Does Ndi play football?_
- ❌ My father go to the farm every day.  
  _↳ My father is he: My father goes to the farm every day._
- ❌ They doesn't eat meat.  
  _↳ They takes don't: They don't eat meat._
- ❌ She carrys water from the stream.  
  _↳ Carry → carries (consonant + y becomes -ies)._


Three generated variants:

> One sentence has a mistake. Which one?

- ◻️ We go to church on Sundays.
- ✅ Bih don't like fish.  
  _↳ explanation: Bih is one person (she): Bih doesn't like fish._
- ◻️ Mih studies in the evening.
- ◻️ Does Tabe carry water every morning?

Full working after a second miss:

> The wrong statement is “Bih don't like fish.”.  
> Bih is one person (she): Bih doesn't like fish.  

> One sentence has a mistake. Which one?

- ◻️ Ayuk washes his uniform on Saturdays.
- ◻️ Mih studies in the evening.
- ◻️ We go to church on Sundays.
- ✅ My father go to the farm every day.  
  _↳ explanation: My father is he: My father goes to the farm every day._

Full working after a second miss:

> The wrong statement is “My father go to the farm every day.”.  
> My father is he: My father goes to the farm every day.  

> One sentence has a mistake. Which one?

- ◻️ Mih studies in the evening.
- ◻️ Ayuk washes his uniform on Saturdays.
- ◻️ We go to church on Sundays.
- ✅ My father go to the farm every day.  
  _↳ explanation: My father is he: My father goes to the farm every day._

Full working after a second miss:

> The wrong statement is “My father go to the farm every day.”.  
> My father is he: My father goes to the farm every day.  

Sources: simple-present (Cambridge English Grammar Today: present simple (affirmative, negative, questions))

### `e5-account` · Lesson 5 · multiple choice, level 2

Prompt: {text} / Which sentence is true, from the account?

Shows 1 true and 3 false statement(s), drawn from:

- ✅ The pupils cleaned the school compound on Saturday.
- ✅ Tabe and Bih carried the rubbish to the pit.
- ✅ The Principal gave everyone bread and a drink.
- ✅ The pupils went home at noon.
- ❌ The pupils came at ten o'clock.  
  _↳ They came at eight o'clock. Ten o'clock was the time of the bread and drink._
- ❌ Only the boys cut the grass.  
  _↳ The account says “some pupils” cut the grass._
- ❌ The pupils cleaned the market.  
  _↳ They cleaned the school compound._
- ❌ The pupils went home on Sunday.  
  _↳ They went home at noon on Saturday._
- ❌ The pupils were sad at the end.  
  _↳ They went home “tired but happy”._


Three generated variants:

> Last Saturday, the Form One pupils cleaned the school compound. They came at eight o'clock. Some pupils cut the grass, others swept the classrooms, and Tabe and Bih carried the rubbish to the pit. At ten o'clock, the Principal gave everyone bread and a drink. The pupils went home at noon, tired but happy.
> Which sentence is true, from the account?

- ◻️ The pupils came at ten o'clock.  
  _↳ feedback if chosen: They came at eight o'clock. Ten o'clock was the time of the bread and drink._
- ◻️ Only the boys cut the grass.  
  _↳ feedback if chosen: The account says “some pupils” cut the grass._
- ◻️ The pupils went home on Sunday.  
  _↳ feedback if chosen: They went home at noon on Saturday._
- ✅ Tabe and Bih carried the rubbish to the pit.

Full working after a second miss:

> The true statement is “Tabe and Bih carried the rubbish to the pit.”.  
> “The pupils came at ten o'clock.” is false: They came at eight o'clock. Ten o'clock was the time of the bread and drink.  
> “Only the boys cut the grass.” is false: The account says “some pupils” cut the grass.  
> “The pupils went home on Sunday.” is false: They went home at noon on Saturday.  

> Last Saturday, the Form One pupils cleaned the school compound. They came at eight o'clock. Some pupils cut the grass, others swept the classrooms, and Tabe and Bih carried the rubbish to the pit. At ten o'clock, the Principal gave everyone bread and a drink. The pupils went home at noon, tired but happy.
> Which sentence is true, from the account?

- ◻️ Only the boys cut the grass.  
  _↳ feedback if chosen: The account says “some pupils” cut the grass._
- ◻️ The pupils cleaned the market.  
  _↳ feedback if chosen: They cleaned the school compound._
- ◻️ The pupils came at ten o'clock.  
  _↳ feedback if chosen: They came at eight o'clock. Ten o'clock was the time of the bread and drink._
- ✅ Tabe and Bih carried the rubbish to the pit.

Full working after a second miss:

> The true statement is “Tabe and Bih carried the rubbish to the pit.”.  
> “Only the boys cut the grass.” is false: The account says “some pupils” cut the grass.  
> “The pupils cleaned the market.” is false: They cleaned the school compound.  
> “The pupils came at ten o'clock.” is false: They came at eight o'clock. Ten o'clock was the time of the bread and drink.  

> Last Saturday, the Form One pupils cleaned the school compound. They came at eight o'clock. Some pupils cut the grass, others swept the classrooms, and Tabe and Bih carried the rubbish to the pit. At ten o'clock, the Principal gave everyone bread and a drink. The pupils went home at noon, tired but happy.
> Which sentence is true, from the account?

- ◻️ The pupils cleaned the market.  
  _↳ feedback if chosen: They cleaned the school compound._
- ✅ The pupils cleaned the school compound on Saturday.
- ◻️ Only the boys cut the grass.  
  _↳ feedback if chosen: The account says “some pupils” cut the grass._
- ◻️ The pupils were sad at the end.  
  _↳ feedback if chosen: They went home “tired but happy”._

Full working after a second miss:

> The true statement is “The pupils cleaned the school compound on Saturday.”.  
> “The pupils cleaned the market.” is false: They cleaned the school compound.  
> “Only the boys cut the grass.” is false: The account says “some pupils” cut the grass.  
> “The pupils were sad at the end.” is false: They went home “tired but happy”.  

Sources: reading (Original texts written for this app (timetable, notices, account); no copied passages)

### `e5-irregular` · Lesson 5 · matching, level 1

Prompt: Match each verb with its past form.

Pairs (4 shown each time):

- go → **went**
- come → **came**
- take → **took**
- eat → **ate**
- bring → **brought**
- see → **saw**
- give → **gave**
- buy → **bought**
- write → **wrote**
- sit → **sat**
- run → **ran**
- sing → **sang**
- drink → **drank**
- wake → **woke**
- meet → **met**
- teach → **taught**
- sell → **sold**
- tell → **told**
- cut → **cut**


Three generated variants:

> Match each verb with its past form.

Right-hand side (shuffled): sat · woke · met · sold
- meet → **met**
- sell → **sold**
- sit → **sat**
- wake → **woke**

Full working after a second miss:

> The right pairs are:  
> meet → met  
> sell → sold  
> sit → sat  
> wake → woke  

> Match each verb with its past form.

Right-hand side (shuffled): ate · gave · woke · brought
- eat → **ate**
- bring → **brought**
- wake → **woke**
- give → **gave**

Full working after a second miss:

> The right pairs are:  
> eat → ate  
> bring → brought  
> wake → woke  
> give → gave  

> Match each verb with its past form.

Right-hand side (shuffled): brought · came · took · saw
- come → **came**
- take → **took**
- see → **saw**
- bring → **brought**

Full working after a second miss:

> The right pairs are:  
> come → came  
> take → took  
> see → saw  
> bring → brought  

Sources: irregular-verbs (Oxford Learner's Dictionaries: list of irregular verbs (British forms))

### `e6-spelling` · Lesson 6 · multiple choice, level 2

Prompt: Which number word is spelt correctly?

Table `x` (one row is picked each time):

| right | w |
|---|---|
| forty | fourty · fortey · forthy |
| nineteen | ninteen · nineteenn · ninetteen |
| ninety | ninty · ninetie · nintey |
| twelfth | twelveth · twelth · twelvth |
| eighth | eightth · eigth · eighthe |
| ninth | nineth · nienth · ninthe |
| fourteen | forteen · fourtenn · fourtheen |
| eighteen | eightteen · eigteen · eighteenn |
| thousand | thousend · tousand · thowsand |
| hundred | hundered · hunderd · hundread |

Right answer: `{x.right}`; wrong choices: `{x.w[0]}`, `{x.w[1]}`, `{x.w[2]}`

- Feedback `letters`: “Not quite. Say the word slowly and check each letter.”

Three generated variants:

> Which number word is spelt correctly?

- ✅ ninth
- ◻️ nienth  
  _↳ feedback if chosen: Not quite. Say the word slowly and check each letter._
- ◻️ ninthe  
  _↳ feedback if chosen: Not quite. Say the word slowly and check each letter._
- ◻️ nineth  
  _↳ feedback if chosen: Not quite. Say the word slowly and check each letter._

Full working after a second miss:

> The correct spelling is “ninth”.  

> Which number word is spelt correctly?

- ✅ fourteen
- ◻️ fourtenn  
  _↳ feedback if chosen: Not quite. Say the word slowly and check each letter._
- ◻️ fourtheen  
  _↳ feedback if chosen: Not quite. Say the word slowly and check each letter._
- ◻️ forteen  
  _↳ feedback if chosen: Not quite. Say the word slowly and check each letter._

Full working after a second miss:

> The correct spelling is “fourteen”.  

> Which number word is spelt correctly?

- ✅ fourteen
- ◻️ fourtheen  
  _↳ feedback if chosen: Not quite. Say the word slowly and check each letter._
- ◻️ forteen  
  _↳ feedback if chosen: Not quite. Say the word slowly and check each letter._
- ◻️ fourtenn  
  _↳ feedback if chosen: Not quite. Say the word slowly and check each letter._

Full working after a second miss:

> The correct spelling is “fourteen”.  

Sources: number-words (British number words, as in Maths TR-A06 (and after hundred, hyphens 21–99); ordinal words)

### `c6-1-check` · Lesson 6 · multiple choice, level 1

Prompt: Which is {x.n} in words?

Table `x` (one row is picked each time):

| n | w |
|---|---|
| 40 | fourty · forthy |
| 19 | ninteen · nineteenn |
| 90 | ninty · ninetty |
| 14 | forteen · fourtheen |
| 18 | eightteen · eigteen |
| 80 | eigthy · eightty |
| 12 | twelf · twelv |
| 15 | fiveteen · fivteen |
| 50 | fivety · fiffty |

Right answer: `{words(x.n)}`; wrong choices: `{x.w[0]}`, `{x.w[1]}`

- Feedback `letters`: “Not quite. Check the tricky letters: four → forty, nine → ninety.”

Three generated variants:

> Which is 14 in words?

- ✅ fourteen
- ◻️ forteen  
  _↳ feedback if chosen: Not quite. Check the tricky letters: four → forty, nine → ninety._
- ◻️ fourtheen  
  _↳ feedback if chosen: Not quite. Check the tricky letters: four → forty, nine → ninety._

Full working after a second miss:

> 14 is written “fourteen”.  

> Which is 50 in words?

- ◻️ fiffty  
  _↳ feedback if chosen: Not quite. Check the tricky letters: four → forty, nine → ninety._
- ✅ fifty
- ◻️ fivety  
  _↳ feedback if chosen: Not quite. Check the tricky letters: four → forty, nine → ninety._

Full working after a second miss:

> 50 is written “fifty”.  

> Which is 90 in words?

- ◻️ ninty  
  _↳ feedback if chosen: Not quite. Check the tricky letters: four → forty, nine → ninety._
- ✅ ninety
- ◻️ ninetty  
  _↳ feedback if chosen: Not quite. Check the tricky letters: four → forty, nine → ninety._

Full working after a second miss:

> 90 is written “ninety”.  

Sources: number-words (British number words, as in Maths TR-A06 (and after hundred, hyphens 21–99); ordinal words)

### `e7-spot` · Lesson 7 · spot the error, level 3

Prompt: One sentence has a mistake. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Look! The children are running to the field.
- ✅ I am writing a letter to my uncle in Douala.
- ✅ Is Ayuk sleeping now?
- ✅ We aren't watching television at the moment.
- ✅ Mih is sitting under the mango tree.
- ❌ Bih is cook achu now.  
  _↳ After is, use the -ing form: Bih is cooking achu now._
- ❌ They is playing football.  
  _↳ They takes are: They are playing football._
- ❌ I am siting on the bench.  
  _↳ Sit → sitting: double the t after one short vowel._
- ❌ Ewane is writeing a letter.  
  _↳ Write → writing: drop the final e._
- ❌ Are you listen to me?  
  _↳ After are you, use the -ing form: Are you listening to me?_


Three generated variants:

> One sentence has a mistake. Which one?

- ◻️ Look! The children are running to the field.
- ◻️ I am writing a letter to my uncle in Douala.
- ✅ They is playing football.  
  _↳ explanation: They takes are: They are playing football._
- ◻️ Is Ayuk sleeping now?

Full working after a second miss:

> The wrong statement is “They is playing football.”.  
> They takes are: They are playing football.  

> One sentence has a mistake. Which one?

- ✅ I am siting on the bench.  
  _↳ explanation: Sit → sitting: double the t after one short vowel._
- ◻️ We aren't watching television at the moment.
- ◻️ I am writing a letter to my uncle in Douala.
- ◻️ Is Ayuk sleeping now?

Full working after a second miss:

> The wrong statement is “I am siting on the bench.”.  
> Sit → sitting: double the t after one short vowel.  

> One sentence has a mistake. Which one?

- ◻️ We aren't watching television at the moment.
- ◻️ I am writing a letter to my uncle in Douala.
- ✅ Bih is cook achu now.  
  _↳ explanation: After is, use the -ing form: Bih is cooking achu now._
- ◻️ Mih is sitting under the mango tree.

Full working after a second miss:

> The wrong statement is “Bih is cook achu now.”.  
> After is, use the -ing form: Bih is cooking achu now.  

Sources: present-continuous (Cambridge English Grammar Today: present continuous)

### `c9-1-check` · Lesson 9 · matching, level 1

Prompt: Sort each item: is it a need or a want?

Pairs (4 shown each time, sorted into groups):

- rice → **need**
- soap → **need**
- salt → **need**
- cooking oil → **need**
- exercise books → **need**
- toothpaste → **need**
- beans → **need**
- kerosene for the lamp → **need**
- sweets → **want**
- chewing gum → **want**
- a toy car → **want**
- a new phone → **want**
- soft drinks → **want**
- a video game → **want**


Three generated variants:

> Sort each item: is it a need or a want?

Groups: need · want
- soft drinks → **want**
- exercise books → **need**
- soap → **need**
- a new phone → **want**

Full working after a second miss:

> The right pairs are:  
> soft drinks → want  
> exercise books → need  
> soap → need  
> a new phone → want  

> Sort each item: is it a need or a want?

Groups: need · want
- cooking oil → **need**
- chewing gum → **want**
- sweets → **want**
- a toy car → **want**

Full working after a second miss:

> The right pairs are:  
> cooking oil → need  
> chewing gum → want  
> sweets → want  
> a toy car → want  

> Sort each item: is it a need or a want?

Groups: need · want
- beans → **need**
- sweets → **want**
- soap → **need**
- a toy car → **want**

Full working after a second miss:

> The right pairs are:  
> beans → need  
> sweets → want  
> soap → need  
> a toy car → want  

Sources: shopping-list (Writing a shopping list: needs and wants, priorities; prices are invented examples)

### `c9-3-check` · Lesson 9 · multiple choice, level 1

Prompt: Which line is written the right way for a shopping list?

`p`: 150 · 200 · 250

Shows 1 true and 3 false statement(s), drawn from:

- ✅ Salt, 1 packet — {p} FCFA
- ❌ salt  
  _↳ Give the quantity and the price too._
- ❌ I will buy some salt because we need it for the soup.  
  _↳ A list has short lines, not full sentences._
- ❌ Salt and soap and rice and oil  
  _↳ Write one item on each line._


Three generated variants:

> Which line is written the right way for a shopping list?

- ◻️ salt  
  _↳ feedback if chosen: Give the quantity and the price too._
- ✅ Salt, 1 packet — 250 FCFA
- ◻️ I will buy some salt because we need it for the soup.  
  _↳ feedback if chosen: A list has short lines, not full sentences._
- ◻️ Salt and soap and rice and oil  
  _↳ feedback if chosen: Write one item on each line._

Full working after a second miss:

> The true statement is “Salt, 1 packet — 250 FCFA”.  
> “salt” is false: Give the quantity and the price too.  
> “I will buy some salt because we need it for the soup.” is false: A list has short lines, not full sentences.  
> “Salt and soap and rice and oil” is false: Write one item on each line.  

> Which line is written the right way for a shopping list?

- ◻️ I will buy some salt because we need it for the soup.  
  _↳ feedback if chosen: A list has short lines, not full sentences._
- ◻️ salt  
  _↳ feedback if chosen: Give the quantity and the price too._
- ✅ Salt, 1 packet — 250 FCFA
- ◻️ Salt and soap and rice and oil  
  _↳ feedback if chosen: Write one item on each line._

Full working after a second miss:

> The true statement is “Salt, 1 packet — 250 FCFA”.  
> “I will buy some salt because we need it for the soup.” is false: A list has short lines, not full sentences.  
> “salt” is false: Give the quantity and the price too.  
> “Salt and soap and rice and oil” is false: Write one item on each line.  

> Which line is written the right way for a shopping list?

- ◻️ I will buy some salt because we need it for the soup.  
  _↳ feedback if chosen: A list has short lines, not full sentences._
- ✅ Salt, 1 packet — 200 FCFA
- ◻️ salt  
  _↳ feedback if chosen: Give the quantity and the price too._
- ◻️ Salt and soap and rice and oil  
  _↳ feedback if chosen: Write one item on each line._

Full working after a second miss:

> The true statement is “Salt, 1 packet — 200 FCFA”.  
> “I will buy some salt because we need it for the soup.” is false: A list has short lines, not full sentences.  
> “salt” is false: Give the quantity and the price too.  
> “Salt and soap and rice and oil” is false: Write one item on each line.  

Sources: shopping-list (Writing a shopping list: needs and wants, priorities; prices are invented examples)

### `e10-sort` · Lesson 10 · matching, level 1

Prompt: Sort the nouns: countable or uncountable?

Pairs (6 shown each time, sorted into groups):

- orange → **countable**
- egg → **countable**
- bucket → **countable**
- mango → **countable**
- plantain → **countable**
- pencil → **countable**
- chair → **countable**
- goat → **countable**
- bag → **countable**
- tomato → **countable**
- banana → **countable**
- bottle → **countable**
- rice → **uncountable**
- water → **uncountable**
- salt → **uncountable**
- oil → **uncountable**
- sugar → **uncountable**
- sand → **uncountable**
- money → **uncountable**
- bread → **uncountable**
- milk → **uncountable**
- flour → **uncountable**
- garri → **uncountable**
- advice → **uncountable**


Three generated variants:

> Sort the nouns: countable or uncountable?

Groups: countable · uncountable
- oil → **uncountable**
- rice → **uncountable**
- mango → **countable**
- egg → **countable**
- plantain → **countable**
- orange → **countable**

Full working after a second miss:

> The right pairs are:  
> oil → uncountable  
> rice → uncountable  
> mango → countable  
> egg → countable  
> plantain → countable  
> orange → countable  

> Sort the nouns: countable or uncountable?

Groups: countable · uncountable
- flour → **uncountable**
- egg → **countable**
- rice → **uncountable**
- mango → **countable**
- bottle → **countable**
- tomato → **countable**

Full working after a second miss:

> The right pairs are:  
> flour → uncountable  
> egg → countable  
> rice → uncountable  
> mango → countable  
> bottle → countable  
> tomato → countable  

> Sort the nouns: countable or uncountable?

Groups: countable · uncountable
- pencil → **countable**
- milk → **uncountable**
- plantain → **countable**
- rice → **uncountable**
- garri → **uncountable**
- advice → **uncountable**

Full working after a second miss:

> The right pairs are:  
> pencil → countable  
> milk → uncountable  
> plantain → countable  
> rice → uncountable  
> garri → uncountable  
> advice → uncountable  

Sources: countable (Cambridge English Grammar Today: nouns, countable and uncountable; much/many, a little/a few)

### `e10-unit` · Lesson 10 · fill the blank, level 2

Prompt: Write the missing word.
Sentence: Mother asked me to buy {words(k)} ___ of {x.n}.
Right answer: `plural(x.u)`

Table `x` (one row is picked each time):

| n | u | w |
|---|---|---|
| bread | loaf | bottle · bar |
| soap | bar | loaf · bottle |
| oil | bottle | loaf · bar |
| water | bucket | loaf · bar |
| salt | packet | loaf · bottle |
| rice | bag | loaf · bar |

- Feedback `singular` (typed `x.u`): “There are {words(k)} of them: use the plural, {plural(x.u)}.”

Three generated variants:

> Write the missing word.

Sentence: **Mother asked me to buy three ___ of rice.**
Typed answer accepted (case and extra spaces ignored): **bags**
- Typed **bag** (singular) → “There are three of them: use the plural, bags.”

Full working after a second miss:

> rice is counted in bags: one bag, three bags.  
> Mother asked me to buy three bags of rice.  

> Write the missing word.

Sentence: **Mother asked me to buy two ___ of oil.**
Typed answer accepted (case and extra spaces ignored): **bottles**
- Typed **bottle** (singular) → “There are two of them: use the plural, bottles.”

Full working after a second miss:

> oil is counted in bottles: one bottle, two bottles.  
> Mother asked me to buy two bottles of oil.  

> Write the missing word.

Sentence: **Mother asked me to buy two ___ of bread.**
Typed answer accepted (case and extra spaces ignored): **loaves**
- Typed **loaf** (singular) → “There are two of them: use the plural, loaves.”

Full working after a second miss:

> bread is counted in loaves: one loaf, two loaves.  
> Mother asked me to buy two loaves of bread.  

Sources: countable (Cambridge English Grammar Today: nouns, countable and uncountable; much/many, a little/a few)

### `e10-spot` · Lesson 10 · spot the error, level 3

Prompt: One sentence has a mistake. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ We need some rice and two bottles of oil.
- ✅ How many eggs are in the basket?
- ✅ Bih gave me some good advice.
- ✅ There is a little sugar in the tin.
- ✅ Ayuk bought three loaves of bread.
- ❌ Tabe bought three breads at the bakery.  
  _↳ Bread is uncountable: three loaves of bread._
- ❌ How much oranges do you want?  
  _↳ Oranges can be counted: How many oranges?_
- ❌ My uncle gave me an advice.  
  _↳ Advice is uncountable: some advice._
- ❌ We need many water for the garden.  
  _↳ Water is uncountable: a lot of water (or much water)._


Three generated variants:

> One sentence has a mistake. Which one?

- ✅ Tabe bought three breads at the bakery.  
  _↳ explanation: Bread is uncountable: three loaves of bread._
- ◻️ We need some rice and two bottles of oil.
- ◻️ Ayuk bought three loaves of bread.
- ◻️ There is a little sugar in the tin.

Full working after a second miss:

> The wrong statement is “Tabe bought three breads at the bakery.”.  
> Bread is uncountable: three loaves of bread.  

> One sentence has a mistake. Which one?

- ✅ Tabe bought three breads at the bakery.  
  _↳ explanation: Bread is uncountable: three loaves of bread._
- ◻️ How many eggs are in the basket?
- ◻️ Ayuk bought three loaves of bread.
- ◻️ Bih gave me some good advice.

Full working after a second miss:

> The wrong statement is “Tabe bought three breads at the bakery.”.  
> Bread is uncountable: three loaves of bread.  

> One sentence has a mistake. Which one?

- ✅ Tabe bought three breads at the bakery.  
  _↳ explanation: Bread is uncountable: three loaves of bread._
- ◻️ We need some rice and two bottles of oil.
- ◻️ Bih gave me some good advice.
- ◻️ How many eggs are in the basket?

Full working after a second miss:

> The wrong statement is “Tabe bought three breads at the bakery.”.  
> Bread is uncountable: three loaves of bread.  

Sources: countable (Cambridge English Grammar Today: nouns, countable and uncountable; much/many, a little/a few)

### `c10-3-check` · Lesson 10 · fill the blank, level 1

Prompt: Choose the word that fits.
Sentence: Please buy a ___ of {x.n}.
Right answer: `x.u`

Table `x` (one row is picked each time):

| n | u | w |
|---|---|---|
| bread | loaf | bottle · bar |
| soap | bar | loaf · bottle |
| oil | bottle | loaf · bar |
| water | bucket | loaf · bar |
| salt | packet | loaf · bottle |
| rice | bag | loaf · bar |

Choices: `{x.w[0]}`, `{x.w[1]}`

- Feedback `unit`: “We do not say that. Think of how {x.n} is sold at the market.”

Three generated variants:

> Choose the word that fits.

Sentence: **Please buy a ___ of oil.**
- ◻️ loaf  
  _↳ feedback if chosen: We do not say that. Think of how oil is sold at the market._
- ◻️ bar  
  _↳ feedback if chosen: We do not say that. Think of how oil is sold at the market._
- ✅ bottle

Full working after a second miss:

> The missing word is “bottle”.  
> Please buy a bottle of oil.  

> Choose the word that fits.

Sentence: **Please buy a ___ of soap.**
- ◻️ bottle  
  _↳ feedback if chosen: We do not say that. Think of how soap is sold at the market._
- ◻️ loaf  
  _↳ feedback if chosen: We do not say that. Think of how soap is sold at the market._
- ✅ bar

Full working after a second miss:

> The missing word is “bar”.  
> Please buy a bar of soap.  

> Choose the word that fits.

Sentence: **Please buy a ___ of rice.**
- ◻️ bar  
  _↳ feedback if chosen: We do not say that. Think of how rice is sold at the market._
- ◻️ loaf  
  _↳ feedback if chosen: We do not say that. Think of how rice is sold at the market._
- ✅ bag

Full working after a second miss:

> The missing word is “bag”.  
> Please buy a bag of rice.  

Sources: countable (Cambridge English Grammar Today: nouns, countable and uncountable; much/many, a little/a few)

### `e11-irregular` · Lesson 11 · matching, level 1

Prompt: Match each verb with its past form.

Pairs (4 shown each time):

- go → **went**
- eat → **ate**
- buy → **bought**
- see → **saw**
- take → **took**
- write → **wrote**
- come → **came**
- drink → **drank**
- sell → **sold**
- meet → **met**
- swim → **swam**
- bring → **brought**
- think → **thought**
- speak → **spoke**
- sleep → **slept**
- pay → **paid**


Three generated variants:

> Match each verb with its past form.

Right-hand side (shuffled): drank · went · took · spoke
- speak → **spoke**
- go → **went**
- take → **took**
- drink → **drank**

Full working after a second miss:

> The right pairs are:  
> speak → spoke  
> go → went  
> take → took  
> drink → drank  

> Match each verb with its past form.

Right-hand side (shuffled): met · swam · ate · brought
- bring → **brought**
- meet → **met**
- eat → **ate**
- swim → **swam**

Full working after a second miss:

> The right pairs are:  
> bring → brought  
> meet → met  
> eat → ate  
> swim → swam  

> Match each verb with its past form.

Right-hand side (shuffled): met · sold · slept · paid
- pay → **paid**
- sell → **sold**
- sleep → **slept**
- meet → **met**

Full working after a second miss:

> The right pairs are:  
> pay → paid  
> sell → sold  
> sleep → slept  
> meet → met  

Sources: irregular-verbs (Oxford Learner's Dictionaries: list of irregular verbs (British forms))

### `e11-spot` · Lesson 11 · spot the error, level 3

Prompt: One sentence has a mistake. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Last Saturday, Ndi travelled to Douala.
- ✅ Did you eat eru yesterday?
- ✅ We didn't go to school on Monday.
- ✅ Ashu bought plantains at the market.
- ✅ The rain stopped at noon.
- ❌ Yesterday Ebai goed to the farm.  
  _↳ Go is irregular: Yesterday Ebai went to the farm._
- ❌ Did Tabe saw the snake?  
  _↳ After did, use the verb as it is: Did Tabe see the snake?_
- ❌ I didn't went to church.  
  _↳ After didn't, use the verb as it is: I didn't go to church._
- ❌ Mih carryed the bucket.  
  _↳ Carry → carried (consonant + y becomes -ied)._
- ❌ Last week we visit our uncle.  
  _↳ Last week is in the past: we visited our uncle._


Three generated variants:

> One sentence has a mistake. Which one?

- ✅ I didn't went to church.  
  _↳ explanation: After didn't, use the verb as it is: I didn't go to church._
- ◻️ Last Saturday, Ndi travelled to Douala.
- ◻️ Did you eat eru yesterday?
- ◻️ We didn't go to school on Monday.

Full working after a second miss:

> The wrong statement is “I didn't went to church.”.  
> After didn't, use the verb as it is: I didn't go to church.  

> One sentence has a mistake. Which one?

- ◻️ Last Saturday, Ndi travelled to Douala.
- ✅ Yesterday Ebai goed to the farm.  
  _↳ explanation: Go is irregular: Yesterday Ebai went to the farm._
- ◻️ The rain stopped at noon.
- ◻️ Did you eat eru yesterday?

Full working after a second miss:

> The wrong statement is “Yesterday Ebai goed to the farm.”.  
> Go is irregular: Yesterday Ebai went to the farm.  

> One sentence has a mistake. Which one?

- ◻️ The rain stopped at noon.
- ✅ Did Tabe saw the snake?  
  _↳ explanation: After did, use the verb as it is: Did Tabe see the snake?_
- ◻️ Did you eat eru yesterday?
- ◻️ We didn't go to school on Monday.

Full working after a second miss:

> The wrong statement is “Did Tabe saw the snake?”.  
> After did, use the verb as it is: Did Tabe see the snake?  

Sources: simple-past (Cambridge English Grammar Today: past simple)

### `e13-sort` · Lesson 13 · matching, level 1

Prompt: How does each one travel? Sort them.

Pairs (6 shown each time, sorted into groups):

- taxi → **road**
- bus → **road**
- motorbike → **road**
- lorry → **road**
- bicycle → **road**
- car → **road**
- canoe → **water**
- boat → **water**
- ship → **water**
- ferry → **water**
- train → **rail**
- plane → **air**
- helicopter → **air**


Three generated variants:

> How does each one travel? Sort them.

Groups: road · water
- bicycle → **road**
- canoe → **water**
- motorbike → **road**
- boat → **water**
- lorry → **road**
- ferry → **water**

Full working after a second miss:

> The right pairs are:  
> bicycle → road  
> canoe → water  
> motorbike → road  
> boat → water  
> lorry → road  
> ferry → water  

> How does each one travel? Sort them.

Groups: road · water · air
- bicycle → **road**
- motorbike → **road**
- car → **road**
- helicopter → **air**
- bus → **road**
- ship → **water**

Full working after a second miss:

> The right pairs are:  
> bicycle → road  
> motorbike → road  
> car → road  
> helicopter → air  
> bus → road  
> ship → water  

> How does each one travel? Sort them.

Groups: road · water · air
- ship → **water**
- helicopter → **air**
- motorbike → **road**
- canoe → **water**
- bicycle → **road**
- ferry → **water**

Full working after a second miss:

> The right pairs are:  
> ship → water  
> helicopter → air  
> motorbike → road  
> canoe → water  
> bicycle → road  
> ferry → water  

Sources: transport (by + transport, on foot (Cambridge English Grammar Today: by))

### `e13-by` · Lesson 13 · fill the blank, level 1

Prompt: Choose the word that fits.
Sentence: {n} goes to school ___ {t.w}.
Right answer: `t.p`

Table `t` (one row is picked each time):

| w | p |
|---|---|
| taxi | by |
| bus | by |
| motorbike | by |
| train | by |
| bicycle | by |
| canoe | by |
| foot | on |

`n`: Ayuk · Bih · Ndi · Ewane · Manyi

Choices: `by`, `on`, `with`

- Feedback `by`: “We say “on foot”, not “by foot”.”
- Feedback `on`: “With a means of transport we say “by”: by {t.w}.”
- Feedback `with`: “We do not say “with {t.w}”. Use by + the means of transport (but: on foot).”

Three generated variants:

> Choose the word that fits.

Sentence: **Ewane goes to school ___ foot.**
- ◻️ by  
  _↳ feedback if chosen: We say “on foot”, not “by foot”._
- ◻️ with  
  _↳ feedback if chosen: We do not say “with foot”. Use by + the means of transport (but: on foot)._
- ✅ on

Full working after a second miss:

> The missing word is “on”.  
> Ewane goes to school on foot.  

> Choose the word that fits.

Sentence: **Bih goes to school ___ train.**
- ◻️ with  
  _↳ feedback if chosen: We do not say “with train”. Use by + the means of transport (but: on foot)._
- ◻️ on  
  _↳ feedback if chosen: With a means of transport we say “by”: by train._
- ✅ by

Full working after a second miss:

> The missing word is “by”.  
> Bih goes to school by train.  

> Choose the word that fits.

Sentence: **Ewane goes to school ___ motorbike.**
- ◻️ with  
  _↳ feedback if chosen: We do not say “with motorbike”. Use by + the means of transport (but: on foot)._
- ◻️ on  
  _↳ feedback if chosen: With a means of transport we say “by”: by motorbike._
- ✅ by

Full working after a second miss:

> The missing word is “by”.  
> Ewane goes to school by motorbike.  

Sources: transport (by + transport, on foot (Cambridge English Grammar Today: by))

### `e13-reply` · Lesson 13 · multiple choice, level 1

Prompt: Someone asks: “{x.q}” What is the best answer?

`t`: bus · taxi · motorbike · train

`town`: Buea · Limbe · Kumba · Bamenda · Mamfe · Douala · Yaoundé

Table `x` (one row is picked each time):

| q | r | w | why |
|---|---|---|---|
| How do you go to school? | I go to school by {t}. | I go to school at seven o'clock. · My school is in {town}. · Yes, I do. | “How” asks about the means of transport. |
| How long does the journey take? | It takes about one hour. | I travel by {t}. · It costs five hundred francs. · It is in {town}. | “How long” asks about time. |
| How much is the fare to {town}? | It is one thousand francs. | It takes about one hour. · I go by {t}. · It is very fast. | “How much” asks about money (the fare). |
| Where does this bus go? | It goes to {town}. | It goes by road. · It takes two hours. · Yes, it does. | “Where” asks about a place. |

Right answer: `{x.r}`; wrong choices: `{x.w[0]}`, `{x.w[1]}`, `{x.w[2]}`

- Feedback `off`: “That answer does not fit the question. {x.why}”

Three generated variants:

> Someone asks: “Where does this bus go?” What is the best answer?

- ◻️ Yes, it does.  
  _↳ feedback if chosen: That answer does not fit the question. “Where” asks about a place._
- ◻️ It takes two hours.  
  _↳ feedback if chosen: That answer does not fit the question. “Where” asks about a place._
- ◻️ It goes by road.  
  _↳ feedback if chosen: That answer does not fit the question. “Where” asks about a place._
- ✅ It goes to Mamfe.

Full working after a second miss:

> “Where” asks about a place.  
> “Where does this bus go?” → “It goes to Mamfe.”  

> Someone asks: “How long does the journey take?” What is the best answer?

- ◻️ I travel by motorbike.  
  _↳ feedback if chosen: That answer does not fit the question. “How long” asks about time._
- ◻️ It costs five hundred francs.  
  _↳ feedback if chosen: That answer does not fit the question. “How long” asks about time._
- ✅ It takes about one hour.
- ◻️ It is in Limbe.  
  _↳ feedback if chosen: That answer does not fit the question. “How long” asks about time._

Full working after a second miss:

> “How long” asks about time.  
> “How long does the journey take?” → “It takes about one hour.”  

> Someone asks: “How do you go to school?” What is the best answer?

- ◻️ Yes, I do.  
  _↳ feedback if chosen: That answer does not fit the question. “How” asks about the means of transport._
- ◻️ My school is in Limbe.  
  _↳ feedback if chosen: That answer does not fit the question. “How” asks about the means of transport._
- ◻️ I go to school at seven o'clock.  
  _↳ feedback if chosen: That answer does not fit the question. “How” asks about the means of transport._
- ✅ I go to school by bus.

Full working after a second miss:

> “How” asks about the means of transport.  
> “How do you go to school?” → “I go to school by bus.”  

Sources: transport (by + transport, on foot (Cambridge English Grammar Today: by))

### `e13-build` · Lesson 13 · word order, level 2

Prompt: Tap the words in the right order.

`x`: I go to school on foot. · We travelled to Bamenda by bus. · How do you travel to Limbe? · My father rides a motorbike to work. · Ships carry goods to the port of Douala. · How long does the journey take?

Sentence(s): {x}


Three generated variants:

> Tap the words in the right order.

Tiles: journey · the · take · long · does · How (then “?”)
Answer: **How long does the journey take?**

Full working after a second miss:

> The sentence is: How long does the journey take?  

> Tap the words in the right order.

Tiles: go · I · on · foot · to · school (then “.”)
Answer: **I go to school on foot.**

Full working after a second miss:

> The sentence is: I go to school on foot.  

> Tap the words in the right order.

Tiles: do · How · to · you · Limbe · travel (then “?”)
Answer: **How do you travel to Limbe?**

Full working after a second miss:

> The sentence is: How do you travel to Limbe?  

Sources: transport (by + transport, on foot (Cambridge English Grammar Today: by))

### `e13-spot` · Lesson 13 · spot the error, level 3

Prompt: One sentence has a mistake. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ We travelled to Buea by bus.
- ✅ My brother rides a motorbike to work.
- ✅ Ships carry goods to the port of Douala.
- ✅ I walk to school every day.
- ✅ Always wear a seat belt in a car.
- ❌ I go to school by foot.  
  _↳ We say “on foot”: I go to school on foot._
- ❌ We travelled to Limbe on taxi.  
  _↳ With a means of transport we say “by”: by taxi._
- ❌ A canoe travels by road.  
  _↳ A canoe travels by water._
- ❌ We went to Douala by the train.  
  _↳ After by, no the: by train._


Three generated variants:

> One sentence has a mistake. Which one?

- ✅ A canoe travels by road.  
  _↳ explanation: A canoe travels by water._
- ◻️ Ships carry goods to the port of Douala.
- ◻️ My brother rides a motorbike to work.
- ◻️ I walk to school every day.

Full working after a second miss:

> The wrong statement is “A canoe travels by road.”.  
> A canoe travels by water.  

> One sentence has a mistake. Which one?

- ✅ We travelled to Limbe on taxi.  
  _↳ explanation: With a means of transport we say “by”: by taxi._
- ◻️ My brother rides a motorbike to work.
- ◻️ We travelled to Buea by bus.
- ◻️ I walk to school every day.

Full working after a second miss:

> The wrong statement is “We travelled to Limbe on taxi.”.  
> With a means of transport we say “by”: by taxi.  

> One sentence has a mistake. Which one?

- ◻️ My brother rides a motorbike to work.
- ◻️ We travelled to Buea by bus.
- ◻️ I walk to school every day.
- ✅ I go to school by foot.  
  _↳ explanation: We say “on foot”: I go to school on foot._

Full working after a second miss:

> The wrong statement is “I go to school by foot.”.  
> We say “on foot”: I go to school on foot.  

Sources: transport (by + transport, on foot (Cambridge English Grammar Today: by))

### `e14-match` · Lesson 14 · matching, level 1

Prompt: Match the two halves of each compound word.

Pairs (4 shown each time):

- air → **port**
- class → **room**
- black → **board**
- round → **about**
- motor → **bike**


Three generated variants:

> Match the two halves of each compound word.

Right-hand side (shuffled): room · about · port · bike
- air → **port**
- round → **about**
- class → **room**
- motor → **bike**

Full working after a second miss:

> The right pairs are:  
> air → port  
> round → about  
> class → room  
> motor → bike  

> Match the two halves of each compound word.

Right-hand side (shuffled): about · port · board · room
- black → **board**
- class → **room**
- round → **about**
- air → **port**

Full working after a second miss:

> The right pairs are:  
> black → board  
> class → room  
> round → about  
> air → port  

> Match the two halves of each compound word.

Right-hand side (shuffled): room · bike · port · board
- air → **port**
- motor → **bike**
- black → **board**
- class → **room**

Full working after a second miss:

> The right pairs are:  
> air → port  
> motor → bike  
> black → board  
> class → room  

Sources: compounds (Cambridge Dictionary for the written form of each compound; word formation: conversion and compounding)

### `e14-written` · Lesson 14 · multiple choice, level 1

Prompt: Which is written correctly?

Table `x` (one row is picked each time):

| a | b | f |
|---|---|---|
| foot | ball | football |
| air | port | airport |
| rail | way | railway |
| motor | bike | motorbike |
| class | room | classroom |
| tooth | brush | toothbrush |
| black | board | blackboard |
| round | about | roundabout |
| foot | path | footpath |
| bus | stop | bus stop |
| car | park | car park |
| road | sign | road sign |
| taxi | driver | taxi driver |
| traffic | light | traffic light |

Right answer: `{x.f}`; wrong choices: `{x.a}{x.b}`, `{x.a} {x.b}`, `{x.a}-{x.b}`

- Feedback `form`: “This compound is written {x.f == x.a + x.b ? 'as one word' : 'as two words'}.”

Three generated variants:

> Which is written correctly?

- ◻️ class room  
  _↳ feedback if chosen: This compound is written as one word._
- ◻️ class-room  
  _↳ feedback if chosen: This compound is written as one word._
- ✅ classroom

Full working after a second miss:

> class + room is written as one word: classroom.  

> Which is written correctly?

- ✅ bus stop
- ◻️ busstop  
  _↳ feedback if chosen: This compound is written as two words._
- ◻️ bus-stop  
  _↳ feedback if chosen: This compound is written as two words._

Full working after a second miss:

> bus + stop is written as two words: bus stop.  

> Which is written correctly?

- ◻️ foot ball  
  _↳ feedback if chosen: This compound is written as one word._
- ◻️ foot-ball  
  _↳ feedback if chosen: This compound is written as one word._
- ✅ football

Full working after a second miss:

> foot + ball is written as one word: football.  

Sources: compounds (Cambridge Dictionary for the written form of each compound; word formation: conversion and compounding)

### `e14-class` · Lesson 14 · multiple choice, level 1

Prompt: In the sentence “{x.s}”, the word “{x.w}” is a:

Table `x` (one row is picked each time):

| s | w | c |
|---|---|---|
| Please water the flowers. | water | verb |
| Bring me a cup of water. | water | noun |
| We walk to school. | walk | verb |
| It is a long walk to school. | walk | noun |
| Text me when you arrive. | text | verb |
| I got a text from Bih. | text | noun |
| Ayuk can ride a motorbike. | ride | verb |
| The ride to Buea was bumpy. | ride | noun |
| Park the car under the tree. | park | verb |
| The children play in the park. | park | noun |
| My uncle will phone us tonight. | phone | verb |
| Mother's phone is ringing. | phone | noun |
| I want a cold drink. | drink | noun |
| We ate fish and plantains. | fish | noun |

Right answer: `{x.c}`; wrong choices: `noun`, `verb`

- Feedback `noun`: “Here “{x.w}” is an action: who does it? It is a verb.”
- Feedback `verb`: “Here “{x.w}” names a thing: it can take a, the or some. It is a noun.”

Three generated variants:

> In the sentence “It is a long walk to school.”, the word “walk” is a:

- ◻️ verb  
  _↳ feedback if chosen: Here “walk” names a thing: it can take a, the or some. It is a noun._
- ✅ noun

Full working after a second miss:

> In “It is a long walk to school.”, “walk” names a thing: it is a noun.  

> In the sentence “Park the car under the tree.”, the word “park” is a:

- ✅ verb
- ◻️ noun  
  _↳ feedback if chosen: Here “park” is an action: who does it? It is a verb._

Full working after a second miss:

> In “Park the car under the tree.”, “park” is an action: it is a verb.  

> In the sentence “Text me when you arrive.”, the word “text” is a:

- ✅ verb
- ◻️ noun  
  _↳ feedback if chosen: Here “text” is an action: who does it? It is a verb._

Full working after a second miss:

> In “Text me when you arrive.”, “text” is an action: it is a verb.  

Sources: compounds (Cambridge Dictionary for the written form of each compound; word formation: conversion and compounding)

### `e14-join` · Lesson 14 · fill the blank, level 2

Prompt: Join the two words to make a compound word.
Sentence: {x.a} + {x.b} → ___
Right answer: `x.f`

Table `x` (one row is picked each time):

| a | b | f |
|---|---|---|
| foot | ball | football |
| air | port | airport |
| rail | way | railway |
| motor | bike | motorbike |
| class | room | classroom |
| tooth | brush | toothbrush |
| black | board | blackboard |
| round | about | roundabout |
| foot | path | footpath |
| bus | stop | bus stop |
| car | park | car park |
| road | sign | road sign |
| taxi | driver | taxi driver |
| traffic | light | traffic light |

- Feedback `form` (typed `x.a + x.b` or `x.a + ' ' + x.b` or `x.a + '-' + x.b`): “Right words, but this compound is written {x.f == x.a + x.b ? 'as one word' : 'as two words'}.”

Three generated variants:

> Join the two words to make a compound word.

Sentence: **round + about → ___**
Typed answer accepted (case and extra spaces ignored): **roundabout**
- Typed **round about** (form) → “Right words, but this compound is written as one word.”
- Typed **round-about** (form) → “Right words, but this compound is written as one word.”

Full working after a second miss:

> The missing word is “roundabout”.  
> round + about → roundabout  

> Join the two words to make a compound word.

Sentence: **round + about → ___**
Typed answer accepted (case and extra spaces ignored): **roundabout**
- Typed **round about** (form) → “Right words, but this compound is written as one word.”
- Typed **round-about** (form) → “Right words, but this compound is written as one word.”

Full working after a second miss:

> The missing word is “roundabout”.  
> round + about → roundabout  

> Join the two words to make a compound word.

Sentence: **motor + bike → ___**
Typed answer accepted (case and extra spaces ignored): **motorbike**
- Typed **motor bike** (form) → “Right words, but this compound is written as one word.”
- Typed **motor-bike** (form) → “Right words, but this compound is written as one word.”

Full working after a second miss:

> The missing word is “motorbike”.  
> motor + bike → motorbike  

Sources: compounds (Cambridge Dictionary for the written form of each compound; word formation: conversion and compounding)

### `e14-convert` · Lesson 14 · fill the blank, level 2

Prompt: The first sentence uses a verb. Use the same word as a noun in the second sentence.
Sentence: {x.v} → {x.n}
Right answer: `x.w`

Table `x` (one row is picked each time):

| v | n | w |
|---|---|---|
| We walk to school. | It is a long ___ to school. | walk |
| Text me tonight. | Bih sent me a ___. | text |
| Can you ride a bicycle? | The ___ to Kumba took two hours. | ride |
| Let us drink some water. | I would like a cold ___. | drink |
| Please phone your mother. | My ___ is in my bag. | phone |
| Park the car here. | We played football in the ___. | park |

- Feedback `changed` (typed `x.w + 's'` or `x.w + 'ing'`): “In conversion the spelling does not change: the noun is “{x.w}”.”

Three generated variants:

> The first sentence uses a verb. Use the same word as a noun in the second sentence.

Sentence: **Please phone your mother. → My ___ is in my bag.**
Typed answer accepted (case and extra spaces ignored): **phone**
- Typed **phones** (changed) → “In conversion the spelling does not change: the noun is “phone”.”
- Typed **phoneing** (changed) → “In conversion the spelling does not change: the noun is “phone”.”

Full working after a second miss:

> The missing word is “phone”.  
> Please phone your mother. → My phone is in my bag.  

> The first sentence uses a verb. Use the same word as a noun in the second sentence.

Sentence: **Park the car here. → We played football in the ___.**
Typed answer accepted (case and extra spaces ignored): **park**
- Typed **parks** (changed) → “In conversion the spelling does not change: the noun is “park”.”
- Typed **parking** (changed) → “In conversion the spelling does not change: the noun is “park”.”

Full working after a second miss:

> The missing word is “park”.  
> Park the car here. → We played football in the park.  

> The first sentence uses a verb. Use the same word as a noun in the second sentence.

Sentence: **Park the car here. → We played football in the ___.**
Typed answer accepted (case and extra spaces ignored): **park**
- Typed **parks** (changed) → “In conversion the spelling does not change: the noun is “park”.”
- Typed **parking** (changed) → “In conversion the spelling does not change: the noun is “park”.”

Full working after a second miss:

> The missing word is “park”.  
> Park the car here. → We played football in the park.  

Sources: compounds (Cambridge Dictionary for the written form of each compound; word formation: conversion and compounding)

### `e14-spot` · Lesson 14 · spot the error, level 3

Prompt: One sentence has a compound word written wrongly. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Wear your seat belt in the taxi.
- ✅ The football match starts after lunch.
- ✅ We waited at the bus stop for an hour.
- ✅ The plane landed at the airport.
- ✅ Turn left at the roundabout.
- ❌ We waited at the busstop.  
  _↳ Bus stop is written as two words._
- ❌ The plane landed at the air port.  
  _↳ Airport is written as one word._
- ❌ Ayuk rides a motor bike to school.  
  _↳ Motorbike is written as one word._
- ❌ The taxidriver stopped at the market.  
  _↳ Taxi driver is written as two words._


Three generated variants:

> One sentence has a compound word written wrongly. Which one?

- ◻️ The football match starts after lunch.
- ◻️ Turn left at the roundabout.
- ◻️ The plane landed at the airport.
- ✅ The plane landed at the air port.  
  _↳ explanation: Airport is written as one word._

Full working after a second miss:

> The wrong statement is “The plane landed at the air port.”.  
> Airport is written as one word.  

> One sentence has a compound word written wrongly. Which one?

- ◻️ The football match starts after lunch.
- ◻️ Wear your seat belt in the taxi.
- ✅ We waited at the busstop.  
  _↳ explanation: Bus stop is written as two words._
- ◻️ The plane landed at the airport.

Full working after a second miss:

> The wrong statement is “We waited at the busstop.”.  
> Bus stop is written as two words.  

> One sentence has a compound word written wrongly. Which one?

- ✅ The plane landed at the air port.  
  _↳ explanation: Airport is written as one word._
- ◻️ Wear your seat belt in the taxi.
- ◻️ The football match starts after lunch.
- ◻️ We waited at the bus stop for an hour.

Full working after a second miss:

> The wrong statement is “The plane landed at the air port.”.  
> Airport is written as one word.  

Sources: compounds (Cambridge Dictionary for the written form of each compound; word formation: conversion and compounding)

### `e15-participle` · Lesson 15 · matching, level 1

Prompt: Match each verb with its past participle.

Pairs (4 shown each time):

- go → **gone**
- eat → **eaten**
- see → **seen**
- write → **written**
- take → **taken**
- break → **broken**
- drink → **drunk**
- forget → **forgotten**
- speak → **spoken**
- give → **given**
- sing → **sung**
- swim → **swum**
- do → **done**
- buy → **bought**


Three generated variants:

> Match each verb with its past participle.

Right-hand side (shuffled): forgotten · gone · given · eaten
- forget → **forgotten**
- eat → **eaten**
- go → **gone**
- give → **given**

Full working after a second miss:

> The right pairs are:  
> forget → forgotten  
> eat → eaten  
> go → gone  
> give → given  

> Match each verb with its past participle.

Right-hand side (shuffled): gone · bought · sung · swum
- go → **gone**
- sing → **sung**
- swim → **swum**
- buy → **bought**

Full working after a second miss:

> The right pairs are:  
> go → gone  
> sing → sung  
> swim → swum  
> buy → bought  

> Match each verb with its past participle.

Right-hand side (shuffled): bought · sung · forgotten · seen
- see → **seen**
- forget → **forgotten**
- buy → **bought**
- sing → **sung**

Full working after a second miss:

> The right pairs are:  
> see → seen  
> forget → forgotten  
> buy → bought  
> sing → sung  

Sources: irregular-verbs (Oxford Learner's Dictionaries: list of irregular verbs (British forms))

### `e15-spot` · Lesson 15 · spot the error, level 3

Prompt: One sentence has a mistake. Which one?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ I have never seen snow.
- ✅ Has Ewane finished his homework yet?
- ✅ They have already eaten.
- ✅ Ndi has lost her pencil.
- ✅ We saw the new teacher yesterday.
- ❌ Bih has went to the market.  
  _↳ After has, use the past participle: Bih has gone to the market._
- ❌ I have seen him yesterday.  
  _↳ Yesterday is a finished time: I saw him yesterday._
- ❌ They has finished their work.  
  _↳ They takes have: They have finished their work._
- ❌ Have you ever eat koki?  
  _↳ Use the past participle: Have you ever eaten koki?_
- ❌ He have taken my book.  
  _↳ He takes has: He has taken my book._


Three generated variants:

> One sentence has a mistake. Which one?

- ◻️ They have already eaten.
- ✅ They has finished their work.  
  _↳ explanation: They takes have: They have finished their work._
- ◻️ Ndi has lost her pencil.
- ◻️ We saw the new teacher yesterday.

Full working after a second miss:

> The wrong statement is “They has finished their work.”.  
> They takes have: They have finished their work.  

> One sentence has a mistake. Which one?

- ✅ He have taken my book.  
  _↳ explanation: He takes has: He has taken my book._
- ◻️ They have already eaten.
- ◻️ We saw the new teacher yesterday.
- ◻️ Has Ewane finished his homework yet?

Full working after a second miss:

> The wrong statement is “He have taken my book.”.  
> He takes has: He has taken my book.  

> One sentence has a mistake. Which one?

- ✅ Bih has went to the market.  
  _↳ explanation: After has, use the past participle: Bih has gone to the market._
- ◻️ Has Ewane finished his homework yet?
- ◻️ We saw the new teacher yesterday.
- ◻️ Ndi has lost her pencil.

Full working after a second miss:

> The wrong statement is “Bih has went to the market.”.  
> After has, use the past participle: Bih has gone to the market.  

Sources: present-perfect (Cambridge English Grammar Today: present perfect; ever, never, already, yet)

### `c15-3-check` · Lesson 15 · fill the blank, level 1

Prompt: Choose the word that fits.
Sentence: {x.t}
Right answer: `x.a`

Table `x` (one row is picked each time):

| t | a | w |
|---|---|---|
| I have ___ seen the sea. I would like to see it one day. | never | ever · yet |
| Bih has ___ finished her homework, so she can play now. | already | ever · yet |
| Ndi hasn't finished her homework ___. | yet | already · ever |
| Have you ___ been to Yaoundé in your life? | ever | yet · just |

Choices: `{x.w[0]}`, `{x.w[1]}`

- Feedback `adv`: “Not here. Ever: in questions; never: not at any time; already: done sooner than expected; yet: at the end of questions and negatives.”

Three generated variants:

> Choose the word that fits.

Sentence: **I have ___ seen the sea. I would like to see it one day.**
- ◻️ yet  
  _↳ feedback if chosen: Not here. Ever: in questions; never: not at any time; already: done sooner than expected; yet: at the end of questions and negatives._
- ◻️ ever  
  _↳ feedback if chosen: Not here. Ever: in questions; never: not at any time; already: done sooner than expected; yet: at the end of questions and negatives._
- ✅ never

Full working after a second miss:

> The missing word is “never”.  
> I have never seen the sea. I would like to see it one day.  

> Choose the word that fits.

Sentence: **Have you ___ been to Yaoundé in your life?**
- ◻️ just  
  _↳ feedback if chosen: Not here. Ever: in questions; never: not at any time; already: done sooner than expected; yet: at the end of questions and negatives._
- ◻️ yet  
  _↳ feedback if chosen: Not here. Ever: in questions; never: not at any time; already: done sooner than expected; yet: at the end of questions and negatives._
- ✅ ever

Full working after a second miss:

> The missing word is “ever”.  
> Have you ever been to Yaoundé in your life?  

> Choose the word that fits.

Sentence: **I have ___ seen the sea. I would like to see it one day.**
- ◻️ yet  
  _↳ feedback if chosen: Not here. Ever: in questions; never: not at any time; already: done sooner than expected; yet: at the end of questions and negatives._
- ✅ never
- ◻️ ever  
  _↳ feedback if chosen: Not here. Ever: in questions; never: not at any time; already: done sooner than expected; yet: at the end of questions and negatives._

Full working after a second miss:

> The missing word is “never”.  
> I have never seen the sea. I would like to see it one day.  

Sources: present-perfect (Cambridge English Grammar Today: present perfect; ever, never, already, yet)

### `c16-1-check` · Lesson 16 · matching, level 1

Prompt: Manyi Ebai, from Mamfe, is in Form One. Match each label on her form with what she writes.

Pairs (4 shown each time):

- Surname (in BLOCK LETTERS) → **EBAI**
- First name → **Manyi**
- Date of birth → **14/05/2014**
- Place of birth → **Mamfe**
- Class → **Form One**


Three generated variants:

> Manyi Ebai, from Mamfe, is in Form One. Match each label on her form with what she writes.

Right-hand side (shuffled): Form One · 14/05/2014 · Manyi · Mamfe
- Class → **Form One**
- Place of birth → **Mamfe**
- First name → **Manyi**
- Date of birth → **14/05/2014**

Full working after a second miss:

> The right pairs are:  
> Class → Form One  
> Place of birth → Mamfe  
> First name → Manyi  
> Date of birth → 14/05/2014  

> Manyi Ebai, from Mamfe, is in Form One. Match each label on her form with what she writes.

Right-hand side (shuffled): 14/05/2014 · Manyi · Mamfe · Form One
- Date of birth → **14/05/2014**
- Class → **Form One**
- First name → **Manyi**
- Place of birth → **Mamfe**

Full working after a second miss:

> The right pairs are:  
> Date of birth → 14/05/2014  
> Class → Form One  
> First name → Manyi  
> Place of birth → Mamfe  

> Manyi Ebai, from Mamfe, is in Form One. Match each label on her form with what she writes.

Right-hand side (shuffled): Manyi · EBAI · Form One · Mamfe
- First name → **Manyi**
- Place of birth → **Mamfe**
- Class → **Form One**
- Surname (in BLOCK LETTERS) → **EBAI**

Full working after a second miss:

> The right pairs are:  
> First name → Manyi  
> Place of birth → Mamfe  
> Class → Form One  
> Surname (in BLOCK LETTERS) → EBAI  

Sources: forms (Filling in forms: British date order dd/mm/yyyy, BLOCK LETTERS; writing invitations)

