# Computer Science Form 2, Batch S2-1: authored answers for review

Every answer fixed by a person, not computed. Part 1: the tables, conventions and rules that computed answers come from.
Part 2: every authored question template, with all its data (keys, statements, pairs, choices and feedback) and sources.
Regenerate with `npm run review:f2-computer-science`. Item IDs (TR-…) match `docs/teacher-review.md`.

## Part 1: rules the computed answers use (science2.js, maths.js)

- **Hexadecimal and binary**: 10 = A₁₆, 15 = F₁₆, 26 = 1A₁₆, 255 = FF₁₆; bytes as 8 bits (00001101 = 13).
- **ASCII**: A = 65, a = 97, 0 = 48, space = 32.
- **Storage (TR-T05 decision)**: 1 byte = 8 bits; 1 KB = 1024 bytes; 1 MB = 1024 KB; 1 GB = 1024 MB.

## Part 2: authored question templates

| # | Template | Lesson | Type, level | Sources |
|---|---|---|---|---|
| 1 | `s2-1-sort` | 1 | matching, 1 | hardware |
| 2 | `s2-1-both` | 1 | multiple choice, 1 | hardware |
| 3 | `s2-1-task` | 1 | multiple choice, 2 | hardware |
| 4 | `s2-1-spot` | 1 | spot the error, 3 | hardware |
| 5 | `s2-1-task-card` (card c1-3) | 1 | multiple choice, 1 | hardware |
| 6 | `s2-2-cpu` | 2 | multiple choice, 1 | hardware |
| 7 | `s2-2-ram` | 2 | multiple choice, 1 | hardware |
| 8 | `s2-2-store` | 2 | matching, 2 | hardware |
| 9 | `s2-2-spot` | 2 | spot the error, 3 | hardware |
| 10 | `s2-2-store-card` (card c2-3) | 2 | matching, 1 | hardware |
| 11 | `s2-4-what` | 4 | multiple choice, 1 | artificial-intelligence |
| 12 | `s2-4-learn` | 4 | multiple choice, 1 | artificial-intelligence |
| 13 | `s2-4-example` | 4 | matching, 2 | artificial-intelligence |
| 14 | `s2-4-spot` | 4 | spot the error, 3 | artificial-intelligence |
| 15 | `s2-4-example-card` (card c4-3) | 4 | matching, 1 | artificial-intelligence |
| 16 | `s2-5-use` | 5 | matching, 1 | artificial-intelligence |
| 17 | `s2-5-ethic` | 5 | matching, 1 | artificial-intelligence |
| 18 | `s2-5-rules` | 5 | multiple choice, 2 | artificial-intelligence |
| 19 | `s2-5-spot` | 5 | spot the error, 3 | artificial-intelligence |
| 20 | `s2-5-rules-card` (card c5-3) | 5 | multiple choice, 1 | artificial-intelligence |
| 21 | `s2-6-best` | 6 | multiple choice, 1 | artificial-intelligence |
| 22 | `s2-6-part` | 6 | matching, 1 | artificial-intelligence |
| 23 | `s2-6-check` | 6 | multiple choice, 2 | artificial-intelligence |
| 24 | `s2-6-spot` | 6 | spot the error, 3 | artificial-intelligence |
| 25 | `s2-6-check-card` (card c6-3) | 6 | multiple choice, 1 | artificial-intelligence |
| 26 | `s2-8-steps` | 8 | ordering, 1 | problem-solving |
| 27 | `s2-8-decompose` | 8 | multiple choice, 1 | problem-solving |
| 28 | `s2-8-algo` | 8 | ordering, 2 | problem-solving |
| 29 | `s2-8-spot` | 8 | spot the error, 3 | problem-solving |
| 30 | `s2-8-algo-card` (card c8-3) | 8 | ordering, 1 | problem-solving |
| 31 | `s2-9-symbol` | 9 | matching, 1 | problem-solving |
| 32 | `s2-11-job` | 11 | matching, 1 | system-software |
| 33 | `s2-11-kind` | 11 | matching, 1 | system-software |
| 34 | `s2-11-gui` | 11 | multiple choice, 2 | system-software |
| 35 | `s2-11-spot` | 11 | spot the error, 3 | system-software |
| 36 | `s2-11-gui-card` (card c11-3) | 11 | multiple choice, 1 | system-software |
| 37 | `s2-12-util` | 12 | matching, 1 | system-software |
| 38 | `s2-12-driver` | 12 | multiple choice, 1 | system-software |
| 39 | `s2-12-backup` | 12 | multiple choice, 2 | system-software |
| 40 | `s2-12-spot` | 12 | spot the error, 3 | system-software |
| 41 | `s2-12-backup-card` (card c12-3) | 12 | multiple choice, 1 | system-software |
| 42 | `s2-14-digits` | 14 | matching, 1 | number-systems |
| 43 | `s2-14-why` | 14 | multiple choice, 3 | number-systems |
| 44 | `s2-15-bits` | 15 | multiple choice, 1 | number-systems |

### `s2-1-sort` · Lesson 1 · matching, level 1

Prompt: Sort the devices: input or output?

Pairs (6 shown each time, sorted into groups):

- keyboard → **input**
- mouse → **input**
- scanner → **input**
- microphone → **input**
- webcam → **input**
- barcode reader → **input**
- monitor → **output**
- printer → **output**
- speakers → **output**
- projector → **output**
- headphones → **output**


Three generated variants:

> Sort the devices: input or output?

Groups: input · output
- projector → **output**
- microphone → **input**
- speakers → **output**
- barcode reader → **input**
- mouse → **input**
- webcam → **input**

Full working after a second miss:

> The right pairs are:  
> projector → output  
> microphone → input  
> speakers → output  
> barcode reader → input  
> mouse → input  
> webcam → input  

> Sort the devices: input or output?

Groups: input · output
- webcam → **input**
- scanner → **input**
- barcode reader → **input**
- monitor → **output**
- mouse → **input**
- headphones → **output**

Full working after a second miss:

> The right pairs are:  
> webcam → input  
> scanner → input  
> barcode reader → input  
> monitor → output  
> mouse → input  
> headphones → output  

> Sort the devices: input or output?

Groups: input · output
- keyboard → **input**
- barcode reader → **input**
- mouse → **input**
- scanner → **input**
- projector → **output**
- webcam → **input**

Full working after a second miss:

> The right pairs are:  
> keyboard → input  
> barcode reader → input  
> mouse → input  
> scanner → input  
> projector → output  
> webcam → input  

Sources: hardware (Computer hardware: input, output, processing and storage devices (standard ICT textbooks))

### `s2-1-both` · Lesson 1 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which device is both an input and an output device? | a touch screen | a keyboard · a printer · a speaker | A keyboard only inputs. · A printer only outputs. · A speaker only outputs. | A touch screen takes touches and shows images. |
| Which device is an input device? | a microphone | a projector · a monitor · headphones | A projector outputs images. · A monitor outputs images. · Headphones output sound. | A microphone sends sound into the computer. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which device is both an input and an output device?

- ◻️ a printer  
  _↳ feedback if chosen: A printer only outputs._
- ◻️ a keyboard  
  _↳ feedback if chosen: A keyboard only inputs._
- ✅ a touch screen
- ◻️ a speaker  
  _↳ feedback if chosen: A speaker only outputs._

Full working after a second miss:

> A touch screen takes touches and shows images.  
> So the answer is “a touch screen”.  

> Which device is both an input and an output device?

- ◻️ a keyboard  
  _↳ feedback if chosen: A keyboard only inputs._
- ◻️ a printer  
  _↳ feedback if chosen: A printer only outputs._
- ✅ a touch screen
- ◻️ a speaker  
  _↳ feedback if chosen: A speaker only outputs._

Full working after a second miss:

> A touch screen takes touches and shows images.  
> So the answer is “a touch screen”.  

> Which device is an input device?

- ◻️ a projector  
  _↳ feedback if chosen: A projector outputs images._
- ✅ a microphone
- ◻️ a monitor  
  _↳ feedback if chosen: A monitor outputs images._
- ◻️ headphones  
  _↳ feedback if chosen: Headphones output sound._

Full working after a second miss:

> A microphone sends sound into the computer.  
> So the answer is “a microphone”.  

Sources: hardware (Computer hardware: input, output, processing and storage devices (standard ICT textbooks))

### `s2-1-task` · Lesson 1 · multiple choice, level 2

Prompt: Which device is best for {X.q}?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| making a paper copy of a letter | a printer | a scanner · a microphone · a webcam | A scanner copies paper into the computer. · A microphone records sound. · A webcam records video. | A printer outputs on paper. |
| recording a voice message | a microphone | a speaker · a printer · a monitor | A speaker plays sound. · A printer prints. · A monitor shows images. | A microphone inputs sound. |
| reading prices at a shop checkout | a barcode reader | a projector · headphones · a mouse | A projector shows images. · Headphones play sound. · A mouse points. | A barcode reader inputs product codes. |
| a video call with a friend | a webcam | a printer · a scanner · a projector | A printer prints. · A scanner copies paper. · A projector shows big images. | A webcam inputs live video. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which device is best for a video call with a friend?

- ◻️ a projector  
  _↳ feedback if chosen: A projector shows big images._
- ◻️ a scanner  
  _↳ feedback if chosen: A scanner copies paper._
- ✅ a webcam
- ◻️ a printer  
  _↳ feedback if chosen: A printer prints._

Full working after a second miss:

> A webcam inputs live video.  
> So the answer is “a webcam”.  

> Which device is best for recording a voice message?

- ◻️ a printer  
  _↳ feedback if chosen: A printer prints._
- ✅ a microphone
- ◻️ a speaker  
  _↳ feedback if chosen: A speaker plays sound._
- ◻️ a monitor  
  _↳ feedback if chosen: A monitor shows images._

Full working after a second miss:

> A microphone inputs sound.  
> So the answer is “a microphone”.  

> Which device is best for reading prices at a shop checkout?

- ◻️ a projector  
  _↳ feedback if chosen: A projector shows images._
- ✅ a barcode reader
- ◻️ headphones  
  _↳ feedback if chosen: Headphones play sound._
- ◻️ a mouse  
  _↳ feedback if chosen: A mouse points._

Full working after a second miss:

> A barcode reader inputs product codes.  
> So the answer is “a barcode reader”.  

Sources: hardware (Computer hardware: input, output, processing and storage devices (standard ICT textbooks))

### `s2-1-spot` · Lesson 1 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ A keyboard is an input device.
- ✅ A monitor is an output device.
- ✅ A touch screen is both input and output.
- ✅ A scanner is an input device.
- ❌ A printer is an input device.  
  _↳ A printer gives results on paper: output._
- ❌ A microphone is an output device.  
  _↳ A microphone sends sound in: input._
- ❌ Speakers are input devices.  
  _↳ Speakers give out sound: output._


Three generated variants:

> Which statement is wrong?

- ◻️ A keyboard is an input device.
- ◻️ A monitor is an output device.
- ✅ A microphone is an output device.  
  _↳ explanation: A microphone sends sound in: input._
- ◻️ A touch screen is both input and output.

Full working after a second miss:

> The wrong statement is “A microphone is an output device.”.  
> A microphone sends sound in: input.  

> Which statement is wrong?

- ◻️ A touch screen is both input and output.
- ◻️ A scanner is an input device.
- ✅ Speakers are input devices.  
  _↳ explanation: Speakers give out sound: output._
- ◻️ A keyboard is an input device.

Full working after a second miss:

> The wrong statement is “Speakers are input devices.”.  
> Speakers give out sound: output.  

> Which statement is wrong?

- ◻️ A touch screen is both input and output.
- ◻️ A keyboard is an input device.
- ✅ A microphone is an output device.  
  _↳ explanation: A microphone sends sound in: input._
- ◻️ A monitor is an output device.

Full working after a second miss:

> The wrong statement is “A microphone is an output device.”.  
> A microphone sends sound in: input.  

Sources: hardware (Computer hardware: input, output, processing and storage devices (standard ICT textbooks))

### `s2-1-task-card` · Lesson 1 · multiple choice, level 1

Prompt: Which device is best for {X.q}?

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| making a paper copy of a letter | a printer | a scanner · a microphone · a webcam | A scanner copies paper into the computer. · A microphone records sound. · A webcam records video. | A printer outputs on paper. |
| recording a voice message | a microphone | a speaker · a printer · a monitor | A speaker plays sound. · A printer prints. · A monitor shows images. | A microphone inputs sound. |
| reading prices at a shop checkout | a barcode reader | a projector · headphones · a mouse | A projector shows images. · Headphones play sound. · A mouse points. | A barcode reader inputs product codes. |
| a video call with a friend | a webcam | a printer · a scanner · a projector | A printer prints. · A scanner copies paper. · A projector shows big images. | A webcam inputs live video. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which device is best for a video call with a friend?

- ✅ a webcam
- ◻️ a scanner  
  _↳ feedback if chosen: A scanner copies paper._
- ◻️ a printer  
  _↳ feedback if chosen: A printer prints._
- ◻️ a projector  
  _↳ feedback if chosen: A projector shows big images._

Full working after a second miss:

> A webcam inputs live video.  
> So the answer is “a webcam”.  

> Which device is best for a video call with a friend?

- ◻️ a projector  
  _↳ feedback if chosen: A projector shows big images._
- ✅ a webcam
- ◻️ a printer  
  _↳ feedback if chosen: A printer prints._
- ◻️ a scanner  
  _↳ feedback if chosen: A scanner copies paper._

Full working after a second miss:

> A webcam inputs live video.  
> So the answer is “a webcam”.  

> Which device is best for recording a voice message?

- ✅ a microphone
- ◻️ a speaker  
  _↳ feedback if chosen: A speaker plays sound._
- ◻️ a printer  
  _↳ feedback if chosen: A printer prints._
- ◻️ a monitor  
  _↳ feedback if chosen: A monitor shows images._

Full working after a second miss:

> A microphone inputs sound.  
> So the answer is “a microphone”.  

Sources: hardware (Computer hardware: input, output, processing and storage devices (standard ICT textbooks))

### `s2-2-cpu` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Which part of the CPU does calculations and comparisons? | the arithmetic and logic unit (ALU) | the control unit · the monitor · the hard disk | The control unit directs. · The monitor is an output device. · The hard disk stores data. | The ALU does arithmetic and logic. |
| In what unit is the speed of a processor measured? | gigahertz (GHz) | gigabytes (GB) · kilograms (kg) · metres (m) | GB measures storage. · kg measures mass. · m measures length. | Clock speed is in GHz. |
| What does the control unit do? | fetches and decodes instructions and directs the other parts | stores files for ever · prints documents · shows images | That is storage. · That is a printer. · That is a monitor. | The control unit directs the computer. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What does the control unit do?

- ◻️ shows images  
  _↳ feedback if chosen: That is a monitor._
- ◻️ stores files for ever  
  _↳ feedback if chosen: That is storage._
- ✅ fetches and decodes instructions and directs the other parts
- ◻️ prints documents  
  _↳ feedback if chosen: That is a printer._

Full working after a second miss:

> The control unit directs the computer.  
> So the answer is “fetches and decodes instructions and directs the other parts”.  

> Which part of the CPU does calculations and comparisons?

- ◻️ the monitor  
  _↳ feedback if chosen: The monitor is an output device._
- ◻️ the control unit  
  _↳ feedback if chosen: The control unit directs._
- ◻️ the hard disk  
  _↳ feedback if chosen: The hard disk stores data._
- ✅ the arithmetic and logic unit (ALU)

Full working after a second miss:

> The ALU does arithmetic and logic.  
> So the answer is “the arithmetic and logic unit (ALU)”.  

> Which part of the CPU does calculations and comparisons?

- ◻️ the control unit  
  _↳ feedback if chosen: The control unit directs._
- ✅ the arithmetic and logic unit (ALU)
- ◻️ the hard disk  
  _↳ feedback if chosen: The hard disk stores data._
- ◻️ the monitor  
  _↳ feedback if chosen: The monitor is an output device._

Full working after a second miss:

> The ALU does arithmetic and logic.  
> So the answer is “the arithmetic and logic unit (ALU)”.  

Sources: hardware (Computer hardware: input, output, processing and storage devices (standard ICT textbooks))

### `s2-2-ram` · Lesson 2 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What happens to the contents of RAM when the power goes off? | They are lost. | They are printed. · They move to ROM. · Nothing happens. | Nothing is printed. · ROM is read only. · RAM is volatile. | RAM is volatile. |
| Which memory holds the start-up instructions? | ROM | RAM · a flash drive · the cloud | RAM is erased at power-off. · That is removable storage. · That is online storage. | ROM keeps them permanently. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Which memory holds the start-up instructions?

- ✅ ROM
- ◻️ a flash drive  
  _↳ feedback if chosen: That is removable storage._
- ◻️ RAM  
  _↳ feedback if chosen: RAM is erased at power-off._
- ◻️ the cloud  
  _↳ feedback if chosen: That is online storage._

Full working after a second miss:

> ROM keeps them permanently.  
> So the answer is “ROM”.  

> Which memory holds the start-up instructions?

- ◻️ a flash drive  
  _↳ feedback if chosen: That is removable storage._
- ◻️ the cloud  
  _↳ feedback if chosen: That is online storage._
- ✅ ROM
- ◻️ RAM  
  _↳ feedback if chosen: RAM is erased at power-off._

Full working after a second miss:

> ROM keeps them permanently.  
> So the answer is “ROM”.  

> Which memory holds the start-up instructions?

- ◻️ the cloud  
  _↳ feedback if chosen: That is online storage._
- ✅ ROM
- ◻️ RAM  
  _↳ feedback if chosen: RAM is erased at power-off._
- ◻️ a flash drive  
  _↳ feedback if chosen: That is removable storage._

Full working after a second miss:

> ROM keeps them permanently.  
> So the answer is “ROM”.  

Sources: hardware (Computer hardware: input, output, processing and storage devices (standard ICT textbooks))

### `s2-2-store` · Lesson 2 · matching, level 2

Prompt: Match each storage to its description.

Pairs (4 shown each time):

- RAM → **primary storage, loses data when power is off**
- ROM → **primary storage, keeps start-up instructions**
- hard disk drive (HDD) → **secondary storage with spinning disks**
- solid-state drive (SSD) → **secondary storage with no moving parts**
- USB flash drive → **small portable secondary storage**
- cloud storage → **storage on servers reached through the internet**


Three generated variants:

> Match each storage to its description.

Right-hand side (shuffled): small portable secondary storage · primary storage, keeps start-up instructions · storage on servers reached through the internet · secondary storage with spinning disks
- ROM → **primary storage, keeps start-up instructions**
- cloud storage → **storage on servers reached through the internet**
- USB flash drive → **small portable secondary storage**
- hard disk drive (HDD) → **secondary storage with spinning disks**

Full working after a second miss:

> The right pairs are:  
> ROM → primary storage, keeps start-up instructions  
> cloud storage → storage on servers reached through the internet  
> USB flash drive → small portable secondary storage  
> hard disk drive (HDD) → secondary storage with spinning disks  

> Match each storage to its description.

Right-hand side (shuffled): primary storage, keeps start-up instructions · primary storage, loses data when power is off · secondary storage with spinning disks · small portable secondary storage
- ROM → **primary storage, keeps start-up instructions**
- USB flash drive → **small portable secondary storage**
- hard disk drive (HDD) → **secondary storage with spinning disks**
- RAM → **primary storage, loses data when power is off**

Full working after a second miss:

> The right pairs are:  
> ROM → primary storage, keeps start-up instructions  
> USB flash drive → small portable secondary storage  
> hard disk drive (HDD) → secondary storage with spinning disks  
> RAM → primary storage, loses data when power is off  

> Match each storage to its description.

Right-hand side (shuffled): small portable secondary storage · secondary storage with spinning disks · storage on servers reached through the internet · primary storage, keeps start-up instructions
- cloud storage → **storage on servers reached through the internet**
- USB flash drive → **small portable secondary storage**
- ROM → **primary storage, keeps start-up instructions**
- hard disk drive (HDD) → **secondary storage with spinning disks**

Full working after a second miss:

> The right pairs are:  
> cloud storage → storage on servers reached through the internet  
> USB flash drive → small portable secondary storage  
> ROM → primary storage, keeps start-up instructions  
> hard disk drive (HDD) → secondary storage with spinning disks  

Sources: hardware (Computer hardware: input, output, processing and storage devices (standard ICT textbooks))

### `s2-2-spot` · Lesson 2 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ The CPU is the brain of the computer.
- ✅ RAM is volatile.
- ✅ An SSD has no moving parts.
- ✅ The ALU does calculations.
- ❌ RAM keeps data after the power goes off.  
  _↳ RAM loses its data: it is volatile._
- ❌ A USB flash drive is primary memory.  
  _↳ It is secondary storage._
- ❌ The monitor is a storage device.  
  _↳ A monitor is an output device._


Three generated variants:

> Which statement is wrong?

- ◻️ The CPU is the brain of the computer.
- ✅ The monitor is a storage device.  
  _↳ explanation: A monitor is an output device._
- ◻️ An SSD has no moving parts.
- ◻️ The ALU does calculations.

Full working after a second miss:

> The wrong statement is “The monitor is a storage device.”.  
> A monitor is an output device.  

> Which statement is wrong?

- ◻️ The ALU does calculations.
- ◻️ An SSD has no moving parts.
- ✅ The monitor is a storage device.  
  _↳ explanation: A monitor is an output device._
- ◻️ The CPU is the brain of the computer.

Full working after a second miss:

> The wrong statement is “The monitor is a storage device.”.  
> A monitor is an output device.  

> Which statement is wrong?

- ◻️ RAM is volatile.
- ◻️ The ALU does calculations.
- ◻️ The CPU is the brain of the computer.
- ✅ The monitor is a storage device.  
  _↳ explanation: A monitor is an output device._

Full working after a second miss:

> The wrong statement is “The monitor is a storage device.”.  
> A monitor is an output device.  

Sources: hardware (Computer hardware: input, output, processing and storage devices (standard ICT textbooks))

### `s2-2-store-card` · Lesson 2 · matching, level 1

Prompt: Match each storage to its description.

Pairs (4 shown each time):

- RAM → **primary storage, loses data when power is off**
- ROM → **primary storage, keeps start-up instructions**
- hard disk drive (HDD) → **secondary storage with spinning disks**
- solid-state drive (SSD) → **secondary storage with no moving parts**
- USB flash drive → **small portable secondary storage**
- cloud storage → **storage on servers reached through the internet**


Three generated variants:

> Match each storage to its description.

Right-hand side (shuffled): primary storage, keeps start-up instructions · primary storage, loses data when power is off · storage on servers reached through the internet · secondary storage with no moving parts
- cloud storage → **storage on servers reached through the internet**
- solid-state drive (SSD) → **secondary storage with no moving parts**
- ROM → **primary storage, keeps start-up instructions**
- RAM → **primary storage, loses data when power is off**

Full working after a second miss:

> The right pairs are:  
> cloud storage → storage on servers reached through the internet  
> solid-state drive (SSD) → secondary storage with no moving parts  
> ROM → primary storage, keeps start-up instructions  
> RAM → primary storage, loses data when power is off  

> Match each storage to its description.

Right-hand side (shuffled): primary storage, keeps start-up instructions · secondary storage with no moving parts · storage on servers reached through the internet · secondary storage with spinning disks
- hard disk drive (HDD) → **secondary storage with spinning disks**
- solid-state drive (SSD) → **secondary storage with no moving parts**
- ROM → **primary storage, keeps start-up instructions**
- cloud storage → **storage on servers reached through the internet**

Full working after a second miss:

> The right pairs are:  
> hard disk drive (HDD) → secondary storage with spinning disks  
> solid-state drive (SSD) → secondary storage with no moving parts  
> ROM → primary storage, keeps start-up instructions  
> cloud storage → storage on servers reached through the internet  

> Match each storage to its description.

Right-hand side (shuffled): secondary storage with no moving parts · small portable secondary storage · storage on servers reached through the internet · primary storage, loses data when power is off
- RAM → **primary storage, loses data when power is off**
- USB flash drive → **small portable secondary storage**
- cloud storage → **storage on servers reached through the internet**
- solid-state drive (SSD) → **secondary storage with no moving parts**

Full working after a second miss:

> The right pairs are:  
> RAM → primary storage, loses data when power is off  
> USB flash drive → small portable secondary storage  
> cloud storage → storage on servers reached through the internet  
> solid-state drive (SSD) → secondary storage with no moving parts  

Sources: hardware (Computer hardware: input, output, processing and storage devices (standard ICT textbooks))

### `s2-4-what` · Lesson 4 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is artificial intelligence? | computer systems doing tasks that normally need human intelligence | a very fast keyboard · a type of printer · any machine with a battery | A keyboard is an input device. · A printer is an output device. · Batteries have nothing to do with it. | AI imitates intelligent tasks like seeing and understanding. |
| Which of these uses AI? | an app that translates spoken English into French | a simple calculator adding two numbers · a light switch · a pencil | A calculator follows fixed rules, not AI. · A switch is not AI. · A pencil is not a computer. | Understanding and translating speech needs AI. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is artificial intelligence?

- ◻️ any machine with a battery  
  _↳ feedback if chosen: Batteries have nothing to do with it._
- ◻️ a type of printer  
  _↳ feedback if chosen: A printer is an output device._
- ◻️ a very fast keyboard  
  _↳ feedback if chosen: A keyboard is an input device._
- ✅ computer systems doing tasks that normally need human intelligence

Full working after a second miss:

> AI imitates intelligent tasks like seeing and understanding.  
> So the answer is “computer systems doing tasks that normally need human intelligence”.  

> What is artificial intelligence?

- ◻️ a type of printer  
  _↳ feedback if chosen: A printer is an output device._
- ◻️ a very fast keyboard  
  _↳ feedback if chosen: A keyboard is an input device._
- ◻️ any machine with a battery  
  _↳ feedback if chosen: Batteries have nothing to do with it._
- ✅ computer systems doing tasks that normally need human intelligence

Full working after a second miss:

> AI imitates intelligent tasks like seeing and understanding.  
> So the answer is “computer systems doing tasks that normally need human intelligence”.  

> What is artificial intelligence?

- ◻️ any machine with a battery  
  _↳ feedback if chosen: Batteries have nothing to do with it._
- ◻️ a type of printer  
  _↳ feedback if chosen: A printer is an output device._
- ◻️ a very fast keyboard  
  _↳ feedback if chosen: A keyboard is an input device._
- ✅ computer systems doing tasks that normally need human intelligence

Full working after a second miss:

> AI imitates intelligent tasks like seeing and understanding.  
> So the answer is “computer systems doing tasks that normally need human intelligence”.  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-4-learn` · Lesson 4 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How does machine learning work? | The system learns patterns from lots of data. | A person types every possible answer. · It guesses with no data. · It copies the internet word for word. | It learns rules from data. · It needs data. · It learns patterns. | Data teaches the system patterns. |
| To teach an AI to recognise sick cassava leaves, what is needed? | many photos of healthy and sick leaves, labelled | one photo · a loud speaker · a fast car | One photo is not enough. · That does not help. · That does not help. | Many labelled examples train the system. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> How does machine learning work?

- ◻️ It guesses with no data.  
  _↳ feedback if chosen: It needs data._
- ◻️ A person types every possible answer.  
  _↳ feedback if chosen: It learns rules from data._
- ✅ The system learns patterns from lots of data.
- ◻️ It copies the internet word for word.  
  _↳ feedback if chosen: It learns patterns._

Full working after a second miss:

> Data teaches the system patterns.  
> So the answer is “The system learns patterns from lots of data.”.  

> How does machine learning work?

- ◻️ A person types every possible answer.  
  _↳ feedback if chosen: It learns rules from data._
- ◻️ It guesses with no data.  
  _↳ feedback if chosen: It needs data._
- ✅ The system learns patterns from lots of data.
- ◻️ It copies the internet word for word.  
  _↳ feedback if chosen: It learns patterns._

Full working after a second miss:

> Data teaches the system patterns.  
> So the answer is “The system learns patterns from lots of data.”.  

> How does machine learning work?

- ✅ The system learns patterns from lots of data.
- ◻️ It guesses with no data.  
  _↳ feedback if chosen: It needs data._
- ◻️ A person types every possible answer.  
  _↳ feedback if chosen: It learns rules from data._
- ◻️ It copies the internet word for word.  
  _↳ feedback if chosen: It learns patterns._

Full working after a second miss:

> Data teaches the system patterns.  
> So the answer is “The system learns patterns from lots of data.”.  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-4-example` · Lesson 4 · matching, level 2

Prompt: Match each AI application to what it does.

Pairs (4 shown each time):

- spam filter → **moves junk emails out of the inbox**
- face unlock → **recognises the owner's face**
- map app → **chooses the fastest route**
- chatbot → **answers questions in conversation**
- translation app → **changes text from one language to another**


Three generated variants:

> Match each AI application to what it does.

Right-hand side (shuffled): recognises the owner's face · answers questions in conversation · changes text from one language to another · chooses the fastest route
- translation app → **changes text from one language to another**
- face unlock → **recognises the owner's face**
- map app → **chooses the fastest route**
- chatbot → **answers questions in conversation**

Full working after a second miss:

> The right pairs are:  
> translation app → changes text from one language to another  
> face unlock → recognises the owner's face  
> map app → chooses the fastest route  
> chatbot → answers questions in conversation  

> Match each AI application to what it does.

Right-hand side (shuffled): answers questions in conversation · recognises the owner's face · chooses the fastest route · moves junk emails out of the inbox
- face unlock → **recognises the owner's face**
- map app → **chooses the fastest route**
- spam filter → **moves junk emails out of the inbox**
- chatbot → **answers questions in conversation**

Full working after a second miss:

> The right pairs are:  
> face unlock → recognises the owner's face  
> map app → chooses the fastest route  
> spam filter → moves junk emails out of the inbox  
> chatbot → answers questions in conversation  

> Match each AI application to what it does.

Right-hand side (shuffled): recognises the owner's face · chooses the fastest route · answers questions in conversation · moves junk emails out of the inbox
- spam filter → **moves junk emails out of the inbox**
- chatbot → **answers questions in conversation**
- face unlock → **recognises the owner's face**
- map app → **chooses the fastest route**

Full working after a second miss:

> The right pairs are:  
> spam filter → moves junk emails out of the inbox  
> chatbot → answers questions in conversation  
> face unlock → recognises the owner's face  
> map app → chooses the fastest route  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-4-spot` · Lesson 4 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ AI can recognise speech.
- ✅ Machine learning uses data.
- ✅ A spam filter can use AI.
- ✅ AI can make mistakes.
- ❌ AI never makes mistakes.  
  _↳ AI can make mistakes; its results should be checked._
- ❌ AI systems are not made by people.  
  _↳ People design and train AI systems._
- ❌ Machine learning needs no data.  
  _↳ It learns from data._


Three generated variants:

> Which statement is wrong?

- ◻️ A spam filter can use AI.
- ◻️ AI can recognise speech.
- ◻️ Machine learning uses data.
- ✅ AI systems are not made by people.  
  _↳ explanation: People design and train AI systems._

Full working after a second miss:

> The wrong statement is “AI systems are not made by people.”.  
> People design and train AI systems.  

> Which statement is wrong?

- ◻️ AI can recognise speech.
- ◻️ Machine learning uses data.
- ◻️ AI can make mistakes.
- ✅ Machine learning needs no data.  
  _↳ explanation: It learns from data._

Full working after a second miss:

> The wrong statement is “Machine learning needs no data.”.  
> It learns from data.  

> Which statement is wrong?

- ◻️ A spam filter can use AI.
- ✅ AI systems are not made by people.  
  _↳ explanation: People design and train AI systems._
- ◻️ AI can make mistakes.
- ◻️ AI can recognise speech.

Full working after a second miss:

> The wrong statement is “AI systems are not made by people.”.  
> People design and train AI systems.  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-4-example-card` · Lesson 4 · matching, level 1

Prompt: Match each AI application to what it does.

Pairs (4 shown each time):

- spam filter → **moves junk emails out of the inbox**
- face unlock → **recognises the owner's face**
- map app → **chooses the fastest route**
- chatbot → **answers questions in conversation**
- translation app → **changes text from one language to another**


Three generated variants:

> Match each AI application to what it does.

Right-hand side (shuffled): moves junk emails out of the inbox · changes text from one language to another · answers questions in conversation · chooses the fastest route
- translation app → **changes text from one language to another**
- spam filter → **moves junk emails out of the inbox**
- chatbot → **answers questions in conversation**
- map app → **chooses the fastest route**

Full working after a second miss:

> The right pairs are:  
> translation app → changes text from one language to another  
> spam filter → moves junk emails out of the inbox  
> chatbot → answers questions in conversation  
> map app → chooses the fastest route  

> Match each AI application to what it does.

Right-hand side (shuffled): recognises the owner's face · answers questions in conversation · chooses the fastest route · changes text from one language to another
- chatbot → **answers questions in conversation**
- translation app → **changes text from one language to another**
- face unlock → **recognises the owner's face**
- map app → **chooses the fastest route**

Full working after a second miss:

> The right pairs are:  
> chatbot → answers questions in conversation  
> translation app → changes text from one language to another  
> face unlock → recognises the owner's face  
> map app → chooses the fastest route  

> Match each AI application to what it does.

Right-hand side (shuffled): answers questions in conversation · moves junk emails out of the inbox · chooses the fastest route · recognises the owner's face
- map app → **chooses the fastest route**
- chatbot → **answers questions in conversation**
- face unlock → **recognises the owner's face**
- spam filter → **moves junk emails out of the inbox**

Full working after a second miss:

> The right pairs are:  
> map app → chooses the fastest route  
> chatbot → answers questions in conversation  
> face unlock → recognises the owner's face  
> spam filter → moves junk emails out of the inbox  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-5-use` · Lesson 5 · matching, level 1

Prompt: Match each area to an AI application.

Pairs (4 shown each time):

- health → **reading medical scans**
- agriculture → **spotting crop disease from photos**
- education → **a tutoring app**
- transport → **planning the fastest route**
- accessibility → **reading text aloud for blind people**


Three generated variants:

> Match each area to an AI application.

Right-hand side (shuffled): reading medical scans · reading text aloud for blind people · spotting crop disease from photos · a tutoring app
- education → **a tutoring app**
- accessibility → **reading text aloud for blind people**
- agriculture → **spotting crop disease from photos**
- health → **reading medical scans**

Full working after a second miss:

> The right pairs are:  
> education → a tutoring app  
> accessibility → reading text aloud for blind people  
> agriculture → spotting crop disease from photos  
> health → reading medical scans  

> Match each area to an AI application.

Right-hand side (shuffled): planning the fastest route · spotting crop disease from photos · reading text aloud for blind people · a tutoring app
- accessibility → **reading text aloud for blind people**
- transport → **planning the fastest route**
- education → **a tutoring app**
- agriculture → **spotting crop disease from photos**

Full working after a second miss:

> The right pairs are:  
> accessibility → reading text aloud for blind people  
> transport → planning the fastest route  
> education → a tutoring app  
> agriculture → spotting crop disease from photos  

> Match each area to an AI application.

Right-hand side (shuffled): planning the fastest route · reading text aloud for blind people · a tutoring app · reading medical scans
- health → **reading medical scans**
- accessibility → **reading text aloud for blind people**
- transport → **planning the fastest route**
- education → **a tutoring app**

Full working after a second miss:

> The right pairs are:  
> health → reading medical scans  
> accessibility → reading text aloud for blind people  
> transport → planning the fastest route  
> education → a tutoring app  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-5-ethic` · Lesson 5 · matching, level 1

Prompt: Match each ethical problem to an example.

Pairs (4 shown each time):

- bias → **a system that treats some groups unfairly**
- privacy → **personal data shared without permission**
- misinformation → **a fake video of a real person**
- over-reliance → **copying AI answers without thinking**


Three generated variants:

> Match each ethical problem to an example.

Right-hand side (shuffled): personal data shared without permission · a system that treats some groups unfairly · a fake video of a real person · copying AI answers without thinking
- over-reliance → **copying AI answers without thinking**
- bias → **a system that treats some groups unfairly**
- misinformation → **a fake video of a real person**
- privacy → **personal data shared without permission**

Full working after a second miss:

> The right pairs are:  
> over-reliance → copying AI answers without thinking  
> bias → a system that treats some groups unfairly  
> misinformation → a fake video of a real person  
> privacy → personal data shared without permission  

> Match each ethical problem to an example.

Right-hand side (shuffled): a fake video of a real person · personal data shared without permission · copying AI answers without thinking · a system that treats some groups unfairly
- over-reliance → **copying AI answers without thinking**
- bias → **a system that treats some groups unfairly**
- misinformation → **a fake video of a real person**
- privacy → **personal data shared without permission**

Full working after a second miss:

> The right pairs are:  
> over-reliance → copying AI answers without thinking  
> bias → a system that treats some groups unfairly  
> misinformation → a fake video of a real person  
> privacy → personal data shared without permission  

> Match each ethical problem to an example.

Right-hand side (shuffled): personal data shared without permission · a fake video of a real person · a system that treats some groups unfairly · copying AI answers without thinking
- bias → **a system that treats some groups unfairly**
- privacy → **personal data shared without permission**
- over-reliance → **copying AI answers without thinking**
- misinformation → **a fake video of a real person**

Full working after a second miss:

> The right pairs are:  
> bias → a system that treats some groups unfairly  
> privacy → personal data shared without permission  
> over-reliance → copying AI answers without thinking  
> misinformation → a fake video of a real person  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-5-rules` · Lesson 5 · multiple choice, level 2

Prompt: Which is responsible use of AI?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ checking AI answers with other sources
- ✅ saying honestly when you used AI
- ✅ keeping personal data private
- ✅ using AI to help you understand, then doing your own work
- ❌ sharing your friends' phone numbers with a chatbot  
  _↳ That breaks their privacy._
- ❌ handing in AI work as your own  
  _↳ That is dishonest._
- ❌ making a fake video to embarrass someone  
  _↳ That is harmful._


Three generated variants:

> Which is responsible use of AI?

- ◻️ sharing your friends' phone numbers with a chatbot  
  _↳ feedback if chosen: That breaks their privacy._
- ✅ checking AI answers with other sources
- ◻️ handing in AI work as your own  
  _↳ feedback if chosen: That is dishonest._

Full working after a second miss:

> The true statement is “checking AI answers with other sources”.  
> “sharing your friends' phone numbers with a chatbot” is false: That breaks their privacy.  
> “handing in AI work as your own” is false: That is dishonest.  

> Which is responsible use of AI?

- ✅ checking AI answers with other sources
- ◻️ sharing your friends' phone numbers with a chatbot  
  _↳ feedback if chosen: That breaks their privacy._
- ◻️ making a fake video to embarrass someone  
  _↳ feedback if chosen: That is harmful._

Full working after a second miss:

> The true statement is “checking AI answers with other sources”.  
> “sharing your friends' phone numbers with a chatbot” is false: That breaks their privacy.  
> “making a fake video to embarrass someone” is false: That is harmful.  

> Which is responsible use of AI?

- ◻️ making a fake video to embarrass someone  
  _↳ feedback if chosen: That is harmful._
- ◻️ sharing your friends' phone numbers with a chatbot  
  _↳ feedback if chosen: That breaks their privacy._
- ✅ saying honestly when you used AI

Full working after a second miss:

> The true statement is “saying honestly when you used AI”.  
> “making a fake video to embarrass someone” is false: That is harmful.  
> “sharing your friends' phone numbers with a chatbot” is false: That breaks their privacy.  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-5-spot` · Lesson 5 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ AI can help doctors read scans.
- ✅ Deepfakes are fake images or videos.
- ✅ AI can be biased.
- ✅ Personal data must be protected.
- ❌ AI answers are always correct, so there is no need to check them.  
  _↳ AI can be wrong: check with other sources._
- ❌ Bias means AI is always fair.  
  _↳ Bias means unfair treatment._
- ❌ It is fine to share passwords with a chatbot.  
  _↳ Never share passwords or personal data._


Three generated variants:

> Which statement is wrong?

- ✅ Bias means AI is always fair.  
  _↳ explanation: Bias means unfair treatment._
- ◻️ Personal data must be protected.
- ◻️ AI can be biased.
- ◻️ Deepfakes are fake images or videos.

Full working after a second miss:

> The wrong statement is “Bias means AI is always fair.”.  
> Bias means unfair treatment.  

> Which statement is wrong?

- ◻️ AI can be biased.
- ✅ Bias means AI is always fair.  
  _↳ explanation: Bias means unfair treatment._
- ◻️ Deepfakes are fake images or videos.
- ◻️ AI can help doctors read scans.

Full working after a second miss:

> The wrong statement is “Bias means AI is always fair.”.  
> Bias means unfair treatment.  

> Which statement is wrong?

- ◻️ AI can help doctors read scans.
- ✅ Bias means AI is always fair.  
  _↳ explanation: Bias means unfair treatment._
- ◻️ Deepfakes are fake images or videos.
- ◻️ AI can be biased.

Full working after a second miss:

> The wrong statement is “Bias means AI is always fair.”.  
> Bias means unfair treatment.  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-5-rules-card` · Lesson 5 · multiple choice, level 1

Prompt: Which is responsible use of AI?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ checking AI answers with other sources
- ✅ saying honestly when you used AI
- ✅ keeping personal data private
- ✅ using AI to help you understand, then doing your own work
- ❌ sharing your friends' phone numbers with a chatbot  
  _↳ That breaks their privacy._
- ❌ handing in AI work as your own  
  _↳ That is dishonest._
- ❌ making a fake video to embarrass someone  
  _↳ That is harmful._


Three generated variants:

> Which is responsible use of AI?

- ◻️ sharing your friends' phone numbers with a chatbot  
  _↳ feedback if chosen: That breaks their privacy._
- ✅ using AI to help you understand, then doing your own work
- ◻️ making a fake video to embarrass someone  
  _↳ feedback if chosen: That is harmful._

Full working after a second miss:

> The true statement is “using AI to help you understand, then doing your own work”.  
> “sharing your friends' phone numbers with a chatbot” is false: That breaks their privacy.  
> “making a fake video to embarrass someone” is false: That is harmful.  

> Which is responsible use of AI?

- ◻️ making a fake video to embarrass someone  
  _↳ feedback if chosen: That is harmful._
- ✅ using AI to help you understand, then doing your own work
- ◻️ handing in AI work as your own  
  _↳ feedback if chosen: That is dishonest._

Full working after a second miss:

> The true statement is “using AI to help you understand, then doing your own work”.  
> “making a fake video to embarrass someone” is false: That is harmful.  
> “handing in AI work as your own” is false: That is dishonest.  

> Which is responsible use of AI?

- ✅ checking AI answers with other sources
- ◻️ handing in AI work as your own  
  _↳ feedback if chosen: That is dishonest._
- ◻️ sharing your friends' phone numbers with a chatbot  
  _↳ feedback if chosen: That breaks their privacy._

Full working after a second miss:

> The true statement is “checking AI answers with other sources”.  
> “handing in AI work as your own” is false: That is dishonest.  
> “sharing your friends' phone numbers with a chatbot” is false: That breaks their privacy.  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-6-best` · Lesson 6 · multiple choice, level 1

Prompt: Which is the best prompt?

Shows 1 true and 2 false statement(s), drawn from:

- ✅ Explain photosynthesis to a Form Two pupil in five short sentences.
- ✅ Give me three quiz questions on the water cycle, with answers.
- ✅ Summarise this paragraph in two sentences for a younger child.
- ✅ List four safety rules for using electricity at home.
- ❌ Photosynthesis.  
  _↳ Too short: say what you want and for whom._
- ❌ Tell me everything.  
  _↳ Too vague: say what topic and how much._
- ❌ Do my homework.  
  _↳ Not specific, and it is dishonest: ask for explanations instead._
- ❌ Stuff about water?  
  _↳ Unclear: say exactly what you need._


Three generated variants:

> Which is the best prompt?

- ◻️ Do my homework.  
  _↳ feedback if chosen: Not specific, and it is dishonest: ask for explanations instead._
- ✅ Give me three quiz questions on the water cycle, with answers.
- ◻️ Tell me everything.  
  _↳ feedback if chosen: Too vague: say what topic and how much._

Full working after a second miss:

> The true statement is “Give me three quiz questions on the water cycle, with answers.”.  
> “Do my homework.” is false: Not specific, and it is dishonest: ask for explanations instead.  
> “Tell me everything.” is false: Too vague: say what topic and how much.  

> Which is the best prompt?

- ◻️ Photosynthesis.  
  _↳ feedback if chosen: Too short: say what you want and for whom._
- ✅ List four safety rules for using electricity at home.
- ◻️ Stuff about water?  
  _↳ feedback if chosen: Unclear: say exactly what you need._

Full working after a second miss:

> The true statement is “List four safety rules for using electricity at home.”.  
> “Photosynthesis.” is false: Too short: say what you want and for whom.  
> “Stuff about water?” is false: Unclear: say exactly what you need.  

> Which is the best prompt?

- ◻️ Stuff about water?  
  _↳ feedback if chosen: Unclear: say exactly what you need._
- ◻️ Photosynthesis.  
  _↳ feedback if chosen: Too short: say what you want and for whom._
- ✅ Give me three quiz questions on the water cycle, with answers.

Full working after a second miss:

> The true statement is “Give me three quiz questions on the water cycle, with answers.”.  
> “Stuff about water?” is false: Unclear: say exactly what you need.  
> “Photosynthesis.” is false: Too short: say what you want and for whom.  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-6-part` · Lesson 6 · matching, level 1

Prompt: Match each part of a good prompt to an example.

Pairs (4 shown each time):

- task → **Explain the causes of floods**
- context → **for a Form Two pupil in Douala**
- format → **in a table with two columns**
- limit → **in under 100 words**


Three generated variants:

> Match each part of a good prompt to an example.

Right-hand side (shuffled): for a Form Two pupil in Douala · in a table with two columns · Explain the causes of floods · in under 100 words
- format → **in a table with two columns**
- context → **for a Form Two pupil in Douala**
- limit → **in under 100 words**
- task → **Explain the causes of floods**

Full working after a second miss:

> The right pairs are:  
> format → in a table with two columns  
> context → for a Form Two pupil in Douala  
> limit → in under 100 words  
> task → Explain the causes of floods  

> Match each part of a good prompt to an example.

Right-hand side (shuffled): Explain the causes of floods · for a Form Two pupil in Douala · in under 100 words · in a table with two columns
- limit → **in under 100 words**
- task → **Explain the causes of floods**
- format → **in a table with two columns**
- context → **for a Form Two pupil in Douala**

Full working after a second miss:

> The right pairs are:  
> limit → in under 100 words  
> task → Explain the causes of floods  
> format → in a table with two columns  
> context → for a Form Two pupil in Douala  

> Match each part of a good prompt to an example.

Right-hand side (shuffled): Explain the causes of floods · in under 100 words · in a table with two columns · for a Form Two pupil in Douala
- task → **Explain the causes of floods**
- context → **for a Form Two pupil in Douala**
- limit → **in under 100 words**
- format → **in a table with two columns**

Full working after a second miss:

> The right pairs are:  
> task → Explain the causes of floods  
> context → for a Form Two pupil in Douala  
> limit → in under 100 words  
> format → in a table with two columns  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-6-check` · Lesson 6 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The AI's answer is too long and difficult. What should you do? | Ask again, adding “in simple words, in five sentences”. | Copy it anyway. · Give up. · Type the same prompt again unchanged. | You will not understand it. · Refining usually works. · The same prompt gives a similar answer. | Add details to refine the prompt. |
| Why must you check an AI response? | It may contain mistakes. | AI is never wrong. · Checking is cheating. · It is always too short. | AI can be wrong. · Checking is good practice. · Length is not the reason. | AI can give wrong information confidently. |
| What should you never put in a prompt? | your personal information, such as your address or passwords | the topic · the format you want · who the answer is for | The topic is needed. · The format helps. · Context helps. | Protect your privacy. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What should you never put in a prompt?

- ◻️ who the answer is for  
  _↳ feedback if chosen: Context helps._
- ◻️ the topic  
  _↳ feedback if chosen: The topic is needed._
- ◻️ the format you want  
  _↳ feedback if chosen: The format helps._
- ✅ your personal information, such as your address or passwords

Full working after a second miss:

> Protect your privacy.  
> So the answer is “your personal information, such as your address or passwords”.  

> What should you never put in a prompt?

- ◻️ the format you want  
  _↳ feedback if chosen: The format helps._
- ✅ your personal information, such as your address or passwords
- ◻️ the topic  
  _↳ feedback if chosen: The topic is needed._
- ◻️ who the answer is for  
  _↳ feedback if chosen: Context helps._

Full working after a second miss:

> Protect your privacy.  
> So the answer is “your personal information, such as your address or passwords”.  

> The AI's answer is too long and difficult. What should you do?

- ✅ Ask again, adding “in simple words, in five sentences”.
- ◻️ Type the same prompt again unchanged.  
  _↳ feedback if chosen: The same prompt gives a similar answer._
- ◻️ Copy it anyway.  
  _↳ feedback if chosen: You will not understand it._
- ◻️ Give up.  
  _↳ feedback if chosen: Refining usually works._

Full working after a second miss:

> Add details to refine the prompt.  
> So the answer is “Ask again, adding “in simple words, in five sentences”.”.  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-6-spot` · Lesson 6 · spot the error, level 3

Prompt: Which advice about prompts is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Be clear and specific.
- ✅ Say who the answer is for.
- ✅ Ask for a format.
- ✅ Check the response.
- ❌ Use one vague word as a prompt.  
  _↳ Vague prompts give poor answers._
- ❌ Include your password so the AI knows you.  
  _↳ Never share passwords._
- ❌ Never change your prompt.  
  _↳ Refining the prompt improves answers._


Three generated variants:

> Which advice about prompts is wrong?

- ✅ Never change your prompt.  
  _↳ explanation: Refining the prompt improves answers._
- ◻️ Check the response.
- ◻️ Be clear and specific.
- ◻️ Say who the answer is for.

Full working after a second miss:

> The wrong statement is “Never change your prompt.”.  
> Refining the prompt improves answers.  

> Which advice about prompts is wrong?

- ◻️ Be clear and specific.
- ◻️ Ask for a format.
- ◻️ Check the response.
- ✅ Include your password so the AI knows you.  
  _↳ explanation: Never share passwords._

Full working after a second miss:

> The wrong statement is “Include your password so the AI knows you.”.  
> Never share passwords.  

> Which advice about prompts is wrong?

- ◻️ Check the response.
- ◻️ Be clear and specific.
- ◻️ Ask for a format.
- ✅ Use one vague word as a prompt.  
  _↳ explanation: Vague prompts give poor answers._

Full working after a second miss:

> The wrong statement is “Use one vague word as a prompt.”.  
> Vague prompts give poor answers.  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-6-check-card` · Lesson 6 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| The AI's answer is too long and difficult. What should you do? | Ask again, adding “in simple words, in five sentences”. | Copy it anyway. · Give up. · Type the same prompt again unchanged. | You will not understand it. · Refining usually works. · The same prompt gives a similar answer. | Add details to refine the prompt. |
| Why must you check an AI response? | It may contain mistakes. | AI is never wrong. · Checking is cheating. · It is always too short. | AI can be wrong. · Checking is good practice. · Length is not the reason. | AI can give wrong information confidently. |
| What should you never put in a prompt? | your personal information, such as your address or passwords | the topic · the format you want · who the answer is for | The topic is needed. · The format helps. · Context helps. | Protect your privacy. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> The AI's answer is too long and difficult. What should you do?

- ◻️ Give up.  
  _↳ feedback if chosen: Refining usually works._
- ◻️ Copy it anyway.  
  _↳ feedback if chosen: You will not understand it._
- ◻️ Type the same prompt again unchanged.  
  _↳ feedback if chosen: The same prompt gives a similar answer._
- ✅ Ask again, adding “in simple words, in five sentences”.

Full working after a second miss:

> Add details to refine the prompt.  
> So the answer is “Ask again, adding “in simple words, in five sentences”.”.  

> What should you never put in a prompt?

- ◻️ the format you want  
  _↳ feedback if chosen: The format helps._
- ◻️ who the answer is for  
  _↳ feedback if chosen: Context helps._
- ✅ your personal information, such as your address or passwords
- ◻️ the topic  
  _↳ feedback if chosen: The topic is needed._

Full working after a second miss:

> Protect your privacy.  
> So the answer is “your personal information, such as your address or passwords”.  

> Why must you check an AI response?

- ◻️ It is always too short.  
  _↳ feedback if chosen: Length is not the reason._
- ◻️ AI is never wrong.  
  _↳ feedback if chosen: AI can be wrong._
- ✅ It may contain mistakes.
- ◻️ Checking is cheating.  
  _↳ feedback if chosen: Checking is good practice._

Full working after a second miss:

> AI can give wrong information confidently.  
> So the answer is “It may contain mistakes.”.  

Sources: artificial-intelligence (Introductory descriptions of artificial intelligence and machine learning (e.g. UNESCO guidance on AI in education, 2023); good practice for prompts)

### `s2-8-steps` · Lesson 8 · ordering, level 1

Prompt: Put the problem-solving steps in order.

Items in the right order:

1. Understand the problem
2. Plan a solution
3. Carry out the plan
4. Check the result


Three generated variants:

> Put the problem-solving steps in order.

Shown as: Carry out the plan · Plan a solution · Check the result · Understand the problem
Correct order: Understand the problem → Plan a solution → Carry out the plan → Check the result

Full working after a second miss:

> The correct order is: Understand the problem → Plan a solution → Carry out the plan → Check the result.  

> Put the problem-solving steps in order.

Shown as: Check the result · Carry out the plan · Understand the problem · Plan a solution
Correct order: Understand the problem → Plan a solution → Carry out the plan → Check the result

Full working after a second miss:

> The correct order is: Understand the problem → Plan a solution → Carry out the plan → Check the result.  

> Put the problem-solving steps in order.

Shown as: Check the result · Understand the problem · Carry out the plan · Plan a solution
Correct order: Understand the problem → Plan a solution → Carry out the plan → Check the result

Full working after a second miss:

> The correct order is: Understand the problem → Plan a solution → Carry out the plan → Check the result.  

Sources: problem-solving (Problem-solving steps (understand, plan, carry out, check), decomposition, algorithms, pseudocode and flowchart symbols, tracing)

### `s2-8-decompose` · Lesson 8 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is decomposition? | breaking a big problem into smaller parts | throwing a computer away · making a problem bigger · printing a document | That is not it. · That is the opposite. · That is not it. | Smaller parts are easier to solve. |
| In the problem “calculate the area of a rectangle”, what are the inputs? | the length and the width | the area · the printer · the colour of the rectangle | The area is the output. · That is a device. · Colour is not needed. | Inputs are the given data. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is decomposition?

- ◻️ throwing a computer away  
  _↳ feedback if chosen: That is not it._
- ◻️ making a problem bigger  
  _↳ feedback if chosen: That is the opposite._
- ✅ breaking a big problem into smaller parts
- ◻️ printing a document  
  _↳ feedback if chosen: That is not it._

Full working after a second miss:

> Smaller parts are easier to solve.  
> So the answer is “breaking a big problem into smaller parts”.  

> What is decomposition?

- ◻️ making a problem bigger  
  _↳ feedback if chosen: That is the opposite._
- ✅ breaking a big problem into smaller parts
- ◻️ printing a document  
  _↳ feedback if chosen: That is not it._
- ◻️ throwing a computer away  
  _↳ feedback if chosen: That is not it._

Full working after a second miss:

> Smaller parts are easier to solve.  
> So the answer is “breaking a big problem into smaller parts”.  

> In the problem “calculate the area of a rectangle”, what are the inputs?

- ◻️ the colour of the rectangle  
  _↳ feedback if chosen: Colour is not needed._
- ◻️ the printer  
  _↳ feedback if chosen: That is a device._
- ◻️ the area  
  _↳ feedback if chosen: The area is the output._
- ✅ the length and the width

Full working after a second miss:

> Inputs are the given data.  
> So the answer is “the length and the width”.  

Sources: problem-solving (Problem-solving steps (understand, plan, carry out, check), decomposition, algorithms, pseudocode and flowchart symbols, tracing)

### `s2-8-algo` · Lesson 8 · ordering, level 2

Prompt: Put the steps of an algorithm to make a cup of tea in order.

Items in the right order:

1. Boil the water
2. Put a tea bag in the cup
3. Pour the hot water into the cup
4. Wait, then remove the tea bag
5. Add sugar if wanted


Three generated variants:

> Put the steps of an algorithm to make a cup of tea in order.

Shown as: Add sugar if wanted · Pour the hot water into the cup · Put a tea bag in the cup · Wait, then remove the tea bag · Boil the water
Correct order: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted

Full working after a second miss:

> The correct order is: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted.  

> Put the steps of an algorithm to make a cup of tea in order.

Shown as: Wait, then remove the tea bag · Pour the hot water into the cup · Put a tea bag in the cup · Boil the water · Add sugar if wanted
Correct order: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted

Full working after a second miss:

> The correct order is: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted.  

> Put the steps of an algorithm to make a cup of tea in order.

Shown as: Add sugar if wanted · Wait, then remove the tea bag · Put a tea bag in the cup · Pour the hot water into the cup · Boil the water
Correct order: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted

Full working after a second miss:

> The correct order is: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted.  

Sources: problem-solving (Problem-solving steps (understand, plan, carry out, check), decomposition, algorithms, pseudocode and flowchart symbols, tracing)

### `s2-8-spot` · Lesson 8 · spot the error, level 3

Prompt: Which statement about algorithms is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ An algorithm has steps in order.
- ✅ Its steps must be clear.
- ✅ An algorithm must stop.
- ✅ A recipe is an everyday algorithm.
- ❌ An algorithm can go on for ever with no end.  
  _↳ An algorithm must stop._
- ❌ The order of the steps does not matter.  
  _↳ The order matters._
- ❌ Steps can be vague, like “do something nice”.  
  _↳ Steps must be precise._


Three generated variants:

> Which statement about algorithms is wrong?

- ◻️ An algorithm has steps in order.
- ◻️ Its steps must be clear.
- ✅ The order of the steps does not matter.  
  _↳ explanation: The order matters._
- ◻️ A recipe is an everyday algorithm.

Full working after a second miss:

> The wrong statement is “The order of the steps does not matter.”.  
> The order matters.  

> Which statement about algorithms is wrong?

- ◻️ An algorithm must stop.
- ✅ Steps can be vague, like “do something nice”.  
  _↳ explanation: Steps must be precise._
- ◻️ Its steps must be clear.
- ◻️ A recipe is an everyday algorithm.

Full working after a second miss:

> The wrong statement is “Steps can be vague, like “do something nice”.”.  
> Steps must be precise.  

> Which statement about algorithms is wrong?

- ◻️ A recipe is an everyday algorithm.
- ◻️ Its steps must be clear.
- ◻️ An algorithm has steps in order.
- ✅ An algorithm can go on for ever with no end.  
  _↳ explanation: An algorithm must stop._

Full working after a second miss:

> The wrong statement is “An algorithm can go on for ever with no end.”.  
> An algorithm must stop.  

Sources: problem-solving (Problem-solving steps (understand, plan, carry out, check), decomposition, algorithms, pseudocode and flowchart symbols, tracing)

### `s2-8-algo-card` · Lesson 8 · ordering, level 1

Prompt: Put the steps of an algorithm to make a cup of tea in order.

Items in the right order:

1. Boil the water
2. Put a tea bag in the cup
3. Pour the hot water into the cup
4. Wait, then remove the tea bag
5. Add sugar if wanted


Three generated variants:

> Put the steps of an algorithm to make a cup of tea in order.

Shown as: Pour the hot water into the cup · Add sugar if wanted · Wait, then remove the tea bag · Boil the water · Put a tea bag in the cup
Correct order: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted

Full working after a second miss:

> The correct order is: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted.  

> Put the steps of an algorithm to make a cup of tea in order.

Shown as: Pour the hot water into the cup · Wait, then remove the tea bag · Put a tea bag in the cup · Boil the water · Add sugar if wanted
Correct order: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted

Full working after a second miss:

> The correct order is: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted.  

> Put the steps of an algorithm to make a cup of tea in order.

Shown as: Boil the water · Pour the hot water into the cup · Add sugar if wanted · Wait, then remove the tea bag · Put a tea bag in the cup
Correct order: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted

Full working after a second miss:

> The correct order is: Boil the water → Put a tea bag in the cup → Pour the hot water into the cup → Wait, then remove the tea bag → Add sugar if wanted.  

Sources: problem-solving (Problem-solving steps (understand, plan, carry out, check), decomposition, algorithms, pseudocode and flowchart symbols, tracing)

### `s2-9-symbol` · Lesson 9 · matching, level 1

Prompt: Match each flowchart symbol to its meaning.

Pairs (4 shown each time):

- oval → **start or end**
- parallelogram → **input or output**
- rectangle → **a process (a calculation or action)**
- diamond → **a decision (a yes/no question)**
- arrow → **the direction of flow**


Three generated variants:

> Match each flowchart symbol to its meaning.

Right-hand side (shuffled): start or end · the direction of flow · a process (a calculation or action) · a decision (a yes/no question)
- arrow → **the direction of flow**
- diamond → **a decision (a yes/no question)**
- oval → **start or end**
- rectangle → **a process (a calculation or action)**

Full working after a second miss:

> The right pairs are:  
> arrow → the direction of flow  
> diamond → a decision (a yes/no question)  
> oval → start or end  
> rectangle → a process (a calculation or action)  

> Match each flowchart symbol to its meaning.

Right-hand side (shuffled): a decision (a yes/no question) · a process (a calculation or action) · input or output · start or end
- parallelogram → **input or output**
- diamond → **a decision (a yes/no question)**
- oval → **start or end**
- rectangle → **a process (a calculation or action)**

Full working after a second miss:

> The right pairs are:  
> parallelogram → input or output  
> diamond → a decision (a yes/no question)  
> oval → start or end  
> rectangle → a process (a calculation or action)  

> Match each flowchart symbol to its meaning.

Right-hand side (shuffled): a process (a calculation or action) · input or output · start or end · a decision (a yes/no question)
- parallelogram → **input or output**
- diamond → **a decision (a yes/no question)**
- oval → **start or end**
- rectangle → **a process (a calculation or action)**

Full working after a second miss:

> The right pairs are:  
> parallelogram → input or output  
> diamond → a decision (a yes/no question)  
> oval → start or end  
> rectangle → a process (a calculation or action)  

Sources: problem-solving (Problem-solving steps (understand, plan, carry out, check), decomposition, algorithms, pseudocode and flowchart symbols, tracing)

### `s2-11-job` · Lesson 11 · matching, level 1

Prompt: Match each function of the operating system to what it does.

Pairs (4 shown each time):

- managing memory → **decides which program uses which part of RAM**
- managing files → **creates, saves, copies and deletes files and folders**
- managing devices → **controls the printer, keyboard and screen**
- user interface → **lets the user give commands with icons, windows or text**
- security → **uses passwords and user accounts**
- managing processes → **shares the CPU between running programs**


Three generated variants:

> Match each function of the operating system to what it does.

Right-hand side (shuffled): controls the printer, keyboard and screen · creates, saves, copies and deletes files and folders · shares the CPU between running programs · uses passwords and user accounts
- managing files → **creates, saves, copies and deletes files and folders**
- security → **uses passwords and user accounts**
- managing processes → **shares the CPU between running programs**
- managing devices → **controls the printer, keyboard and screen**

Full working after a second miss:

> The right pairs are:  
> managing files → creates, saves, copies and deletes files and folders  
> security → uses passwords and user accounts  
> managing processes → shares the CPU between running programs  
> managing devices → controls the printer, keyboard and screen  

> Match each function of the operating system to what it does.

Right-hand side (shuffled): decides which program uses which part of RAM · lets the user give commands with icons, windows or text · controls the printer, keyboard and screen · creates, saves, copies and deletes files and folders
- user interface → **lets the user give commands with icons, windows or text**
- managing files → **creates, saves, copies and deletes files and folders**
- managing memory → **decides which program uses which part of RAM**
- managing devices → **controls the printer, keyboard and screen**

Full working after a second miss:

> The right pairs are:  
> user interface → lets the user give commands with icons, windows or text  
> managing files → creates, saves, copies and deletes files and folders  
> managing memory → decides which program uses which part of RAM  
> managing devices → controls the printer, keyboard and screen  

> Match each function of the operating system to what it does.

Right-hand side (shuffled): creates, saves, copies and deletes files and folders · controls the printer, keyboard and screen · decides which program uses which part of RAM · lets the user give commands with icons, windows or text
- managing devices → **controls the printer, keyboard and screen**
- user interface → **lets the user give commands with icons, windows or text**
- managing memory → **decides which program uses which part of RAM**
- managing files → **creates, saves, copies and deletes files and folders**

Full working after a second miss:

> The right pairs are:  
> managing devices → controls the printer, keyboard and screen  
> user interface → lets the user give commands with icons, windows or text  
> managing memory → decides which program uses which part of RAM  
> managing files → creates, saves, copies and deletes files and folders  

Sources: system-software (Operating systems, utility software and device drivers)

### `s2-11-kind` · Lesson 11 · matching, level 1

Prompt: Sort: operating system or application software?

Pairs (4 shown each time, sorted into groups):

- Windows → **operating system**
- Linux → **operating system**
- Android → **operating system**
- iOS → **operating system**
- a word processor → **application**
- a web browser → **application**
- a game → **application**
- a spreadsheet → **application**


Three generated variants:

> Sort: operating system or application software?

Groups: operating system · application
- a game → **application**
- a spreadsheet → **application**
- a word processor → **application**
- Windows → **operating system**

Full working after a second miss:

> The right pairs are:  
> a game → application  
> a spreadsheet → application  
> a word processor → application  
> Windows → operating system  

> Sort: operating system or application software?

Groups: operating system · application
- Linux → **operating system**
- iOS → **operating system**
- a web browser → **application**
- a spreadsheet → **application**

Full working after a second miss:

> The right pairs are:  
> Linux → operating system  
> iOS → operating system  
> a web browser → application  
> a spreadsheet → application  

> Sort: operating system or application software?

Groups: operating system · application
- a web browser → **application**
- a spreadsheet → **application**
- a game → **application**
- iOS → **operating system**

Full working after a second miss:

> The right pairs are:  
> a web browser → application  
> a spreadsheet → application  
> a game → application  
> iOS → operating system  

Sources: system-software (Operating systems, utility software and device drivers)

### `s2-11-gui` · Lesson 11 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does GUI stand for? | graphical user interface | general unit of information · great unknown internet · graphic upload index | That is not it. · That is not it. · That is not it. | Windows, icons, menus, pointer. |
| In which interface do you type commands? | a command-line interface (CLI) | a graphical user interface · a touch screen menu · an icon | A GUI uses icons and windows. · That is a GUI. · An icon is clicked, not typed. | A CLI takes typed commands. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In which interface do you type commands?

- ◻️ a touch screen menu  
  _↳ feedback if chosen: That is a GUI._
- ◻️ a graphical user interface  
  _↳ feedback if chosen: A GUI uses icons and windows._
- ✅ a command-line interface (CLI)
- ◻️ an icon  
  _↳ feedback if chosen: An icon is clicked, not typed._

Full working after a second miss:

> A CLI takes typed commands.  
> So the answer is “a command-line interface (CLI)”.  

> What does GUI stand for?

- ◻️ graphic upload index  
  _↳ feedback if chosen: That is not it._
- ✅ graphical user interface
- ◻️ general unit of information  
  _↳ feedback if chosen: That is not it._
- ◻️ great unknown internet  
  _↳ feedback if chosen: That is not it._

Full working after a second miss:

> Windows, icons, menus, pointer.  
> So the answer is “graphical user interface”.  

> What does GUI stand for?

- ◻️ great unknown internet  
  _↳ feedback if chosen: That is not it._
- ◻️ graphic upload index  
  _↳ feedback if chosen: That is not it._
- ◻️ general unit of information  
  _↳ feedback if chosen: That is not it._
- ✅ graphical user interface

Full working after a second miss:

> Windows, icons, menus, pointer.  
> So the answer is “graphical user interface”.  

Sources: system-software (Operating systems, utility software and device drivers)

### `s2-11-spot` · Lesson 11 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Windows is an operating system.
- ✅ The OS manages memory.
- ✅ A GUI uses icons and windows.
- ✅ Android runs on phones.
- ❌ A web browser is an operating system.  
  _↳ A browser is application software._
- ❌ The OS starts only after you open a game.  
  _↳ The OS starts when the computer is switched on._
- ❌ A CLI uses icons and a mouse only.  
  _↳ A CLI uses typed commands._


Three generated variants:

> Which statement is wrong?

- ◻️ The OS manages memory.
- ◻️ A GUI uses icons and windows.
- ◻️ Windows is an operating system.
- ✅ The OS starts only after you open a game.  
  _↳ explanation: The OS starts when the computer is switched on._

Full working after a second miss:

> The wrong statement is “The OS starts only after you open a game.”.  
> The OS starts when the computer is switched on.  

> Which statement is wrong?

- ◻️ Windows is an operating system.
- ◻️ Android runs on phones.
- ✅ The OS starts only after you open a game.  
  _↳ explanation: The OS starts when the computer is switched on._
- ◻️ A GUI uses icons and windows.

Full working after a second miss:

> The wrong statement is “The OS starts only after you open a game.”.  
> The OS starts when the computer is switched on.  

> Which statement is wrong?

- ◻️ Windows is an operating system.
- ✅ A CLI uses icons and a mouse only.  
  _↳ explanation: A CLI uses typed commands._
- ◻️ The OS manages memory.
- ◻️ Android runs on phones.

Full working after a second miss:

> The wrong statement is “A CLI uses icons and a mouse only.”.  
> A CLI uses typed commands.  

Sources: system-software (Operating systems, utility software and device drivers)

### `s2-11-gui-card` · Lesson 11 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What does GUI stand for? | graphical user interface | general unit of information · great unknown internet · graphic upload index | That is not it. · That is not it. · That is not it. | Windows, icons, menus, pointer. |
| In which interface do you type commands? | a command-line interface (CLI) | a graphical user interface · a touch screen menu · an icon | A GUI uses icons and windows. · That is a GUI. · An icon is clicked, not typed. | A CLI takes typed commands. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> In which interface do you type commands?

- ◻️ a graphical user interface  
  _↳ feedback if chosen: A GUI uses icons and windows._
- ✅ a command-line interface (CLI)
- ◻️ a touch screen menu  
  _↳ feedback if chosen: That is a GUI._
- ◻️ an icon  
  _↳ feedback if chosen: An icon is clicked, not typed._

Full working after a second miss:

> A CLI takes typed commands.  
> So the answer is “a command-line interface (CLI)”.  

> What does GUI stand for?

- ◻️ graphic upload index  
  _↳ feedback if chosen: That is not it._
- ◻️ great unknown internet  
  _↳ feedback if chosen: That is not it._
- ◻️ general unit of information  
  _↳ feedback if chosen: That is not it._
- ✅ graphical user interface

Full working after a second miss:

> Windows, icons, menus, pointer.  
> So the answer is “graphical user interface”.  

> In which interface do you type commands?

- ◻️ a graphical user interface  
  _↳ feedback if chosen: A GUI uses icons and windows._
- ◻️ an icon  
  _↳ feedback if chosen: An icon is clicked, not typed._
- ✅ a command-line interface (CLI)
- ◻️ a touch screen menu  
  _↳ feedback if chosen: That is a GUI._

Full working after a second miss:

> A CLI takes typed commands.  
> So the answer is “a command-line interface (CLI)”.  

Sources: system-software (Operating systems, utility software and device drivers)

### `s2-12-util` · Lesson 12 · matching, level 1

Prompt: Match each utility to what it does.

Pairs (4 shown each time):

- antivirus → **finds and removes malware**
- backup software → **makes copies of files to restore after a loss**
- disk clean-up → **deletes unneeded temporary files**
- file compression → **makes files smaller (zip)**
- disk defragmenter → **rearranges files on a hard disk so they load faster**
- firewall → **blocks unwanted network connections**


Three generated variants:

> Match each utility to what it does.

Right-hand side (shuffled): makes copies of files to restore after a loss · blocks unwanted network connections · finds and removes malware · makes files smaller (zip)
- file compression → **makes files smaller (zip)**
- firewall → **blocks unwanted network connections**
- antivirus → **finds and removes malware**
- backup software → **makes copies of files to restore after a loss**

Full working after a second miss:

> The right pairs are:  
> file compression → makes files smaller (zip)  
> firewall → blocks unwanted network connections  
> antivirus → finds and removes malware  
> backup software → makes copies of files to restore after a loss  

> Match each utility to what it does.

Right-hand side (shuffled): deletes unneeded temporary files · rearranges files on a hard disk so they load faster · makes copies of files to restore after a loss · makes files smaller (zip)
- file compression → **makes files smaller (zip)**
- backup software → **makes copies of files to restore after a loss**
- disk defragmenter → **rearranges files on a hard disk so they load faster**
- disk clean-up → **deletes unneeded temporary files**

Full working after a second miss:

> The right pairs are:  
> file compression → makes files smaller (zip)  
> backup software → makes copies of files to restore after a loss  
> disk defragmenter → rearranges files on a hard disk so they load faster  
> disk clean-up → deletes unneeded temporary files  

> Match each utility to what it does.

Right-hand side (shuffled): rearranges files on a hard disk so they load faster · makes files smaller (zip) · makes copies of files to restore after a loss · finds and removes malware
- file compression → **makes files smaller (zip)**
- backup software → **makes copies of files to restore after a loss**
- disk defragmenter → **rearranges files on a hard disk so they load faster**
- antivirus → **finds and removes malware**

Full working after a second miss:

> The right pairs are:  
> file compression → makes files smaller (zip)  
> backup software → makes copies of files to restore after a loss  
> disk defragmenter → rearranges files on a hard disk so they load faster  
> antivirus → finds and removes malware  

Sources: system-software (Operating systems, utility software and device drivers)

### `s2-12-driver` · Lesson 12 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| What is a device driver? | a program that lets the OS communicate with a hardware device | a person who drives a computer · a type of keyboard · an antivirus | It is software. · A keyboard is hardware. · Antivirus removes malware. | Drivers connect the OS and hardware. |
| A new scanner is plugged in but does not work. What is most likely missing? | its device driver | a bigger monitor · a new mouse · more paper | The monitor is not the problem. · The mouse is not the problem. · Scanners do not use paper. | Without its driver, the OS cannot use the device. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> A new scanner is plugged in but does not work. What is most likely missing?

- ◻️ more paper  
  _↳ feedback if chosen: Scanners do not use paper._
- ◻️ a new mouse  
  _↳ feedback if chosen: The mouse is not the problem._
- ✅ its device driver
- ◻️ a bigger monitor  
  _↳ feedback if chosen: The monitor is not the problem._

Full working after a second miss:

> Without its driver, the OS cannot use the device.  
> So the answer is “its device driver”.  

> A new scanner is plugged in but does not work. What is most likely missing?

- ◻️ a new mouse  
  _↳ feedback if chosen: The mouse is not the problem._
- ◻️ a bigger monitor  
  _↳ feedback if chosen: The monitor is not the problem._
- ✅ its device driver
- ◻️ more paper  
  _↳ feedback if chosen: Scanners do not use paper._

Full working after a second miss:

> Without its driver, the OS cannot use the device.  
> So the answer is “its device driver”.  

> What is a device driver?

- ◻️ an antivirus  
  _↳ feedback if chosen: Antivirus removes malware._
- ✅ a program that lets the OS communicate with a hardware device
- ◻️ a person who drives a computer  
  _↳ feedback if chosen: It is software._
- ◻️ a type of keyboard  
  _↳ feedback if chosen: A keyboard is hardware._

Full working after a second miss:

> Drivers connect the OS and hardware.  
> So the answer is “a program that lets the OS communicate with a hardware device”.  

Sources: system-software (Operating systems, utility software and device drivers)

### `s2-12-backup` · Lesson 12 · multiple choice, level 2

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why should you back up your files? | so they can be restored if lost or damaged | to make the computer slower · to delete them · to print them | That is not the aim. · Backup keeps copies. · Backup does not print. | A backup copy protects against loss. |
| Which utility makes a file smaller to send by email? | file compression (zip) | antivirus · disk defragmenter · device driver | Antivirus removes malware. · It rearranges files on a disk. · A driver controls hardware. | Compression reduces file size. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why should you back up your files?

- ◻️ to delete them  
  _↳ feedback if chosen: Backup keeps copies._
- ✅ so they can be restored if lost or damaged
- ◻️ to make the computer slower  
  _↳ feedback if chosen: That is not the aim._
- ◻️ to print them  
  _↳ feedback if chosen: Backup does not print._

Full working after a second miss:

> A backup copy protects against loss.  
> So the answer is “so they can be restored if lost or damaged”.  

> Which utility makes a file smaller to send by email?

- ◻️ disk defragmenter  
  _↳ feedback if chosen: It rearranges files on a disk._
- ✅ file compression (zip)
- ◻️ device driver  
  _↳ feedback if chosen: A driver controls hardware._
- ◻️ antivirus  
  _↳ feedback if chosen: Antivirus removes malware._

Full working after a second miss:

> Compression reduces file size.  
> So the answer is “file compression (zip)”.  

> Why should you back up your files?

- ◻️ to print them  
  _↳ feedback if chosen: Backup does not print._
- ◻️ to delete them  
  _↳ feedback if chosen: Backup keeps copies._
- ◻️ to make the computer slower  
  _↳ feedback if chosen: That is not the aim._
- ✅ so they can be restored if lost or damaged

Full working after a second miss:

> A backup copy protects against loss.  
> So the answer is “so they can be restored if lost or damaged”.  

Sources: system-software (Operating systems, utility software and device drivers)

### `s2-12-spot` · Lesson 12 · spot the error, level 3

Prompt: Which statement is wrong?

Shows 3 correct and 1 wrong statement(s), drawn from:

- ✅ Antivirus removes malware.
- ✅ A driver lets the OS use a device.
- ✅ Backups protect against data loss.
- ✅ Compression makes files smaller.
- ❌ An antivirus never needs updating.  
  _↳ It must be updated to catch new malware._
- ❌ A device driver is a hardware part.  
  _↳ A driver is software._
- ❌ Disk clean-up adds unneeded files.  
  _↳ It removes unneeded files._


Three generated variants:

> Which statement is wrong?

- ◻️ Compression makes files smaller.
- ◻️ A driver lets the OS use a device.
- ✅ An antivirus never needs updating.  
  _↳ explanation: It must be updated to catch new malware._
- ◻️ Backups protect against data loss.

Full working after a second miss:

> The wrong statement is “An antivirus never needs updating.”.  
> It must be updated to catch new malware.  

> Which statement is wrong?

- ✅ Disk clean-up adds unneeded files.  
  _↳ explanation: It removes unneeded files._
- ◻️ Antivirus removes malware.
- ◻️ Compression makes files smaller.
- ◻️ Backups protect against data loss.

Full working after a second miss:

> The wrong statement is “Disk clean-up adds unneeded files.”.  
> It removes unneeded files.  

> Which statement is wrong?

- ◻️ Backups protect against data loss.
- ◻️ Compression makes files smaller.
- ◻️ Antivirus removes malware.
- ✅ A device driver is a hardware part.  
  _↳ explanation: A driver is software._

Full working after a second miss:

> The wrong statement is “A device driver is a hardware part.”.  
> A driver is software.  

Sources: system-software (Operating systems, utility software and device drivers)

### `s2-12-backup-card` · Lesson 12 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why should you back up your files? | so they can be restored if lost or damaged | to make the computer slower · to delete them · to print them | That is not the aim. · Backup keeps copies. · Backup does not print. | A backup copy protects against loss. |
| Which utility makes a file smaller to send by email? | file compression (zip) | antivirus · disk defragmenter · device driver | Antivirus removes malware. · It rearranges files on a disk. · A driver controls hardware. | Compression reduces file size. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why should you back up your files?

- ◻️ to print them  
  _↳ feedback if chosen: Backup does not print._
- ✅ so they can be restored if lost or damaged
- ◻️ to make the computer slower  
  _↳ feedback if chosen: That is not the aim._
- ◻️ to delete them  
  _↳ feedback if chosen: Backup keeps copies._

Full working after a second miss:

> A backup copy protects against loss.  
> So the answer is “so they can be restored if lost or damaged”.  

> Why should you back up your files?

- ◻️ to print them  
  _↳ feedback if chosen: Backup does not print._
- ◻️ to make the computer slower  
  _↳ feedback if chosen: That is not the aim._
- ◻️ to delete them  
  _↳ feedback if chosen: Backup keeps copies._
- ✅ so they can be restored if lost or damaged

Full working after a second miss:

> A backup copy protects against loss.  
> So the answer is “so they can be restored if lost or damaged”.  

> Why should you back up your files?

- ◻️ to delete them  
  _↳ feedback if chosen: Backup keeps copies._
- ✅ so they can be restored if lost or damaged
- ◻️ to make the computer slower  
  _↳ feedback if chosen: That is not the aim._
- ◻️ to print them  
  _↳ feedback if chosen: Backup does not print._

Full working after a second miss:

> A backup copy protects against loss.  
> So the answer is “so they can be restored if lost or damaged”.  

Sources: system-software (Operating systems, utility software and device drivers)

### `s2-14-digits` · Lesson 14 · matching, level 1

Prompt: Match each number system to its digits.

Pairs (4 shown each time):

- binary (base 2) → **0 and 1**
- octal (base 8) → **0 to 7**
- decimal (base 10) → **0 to 9**
- hexadecimal (base 16) → **0 to 9 and A to F**


Three generated variants:

> Match each number system to its digits.

Right-hand side (shuffled): 0 to 9 · 0 to 7 · 0 and 1 · 0 to 9 and A to F
- hexadecimal (base 16) → **0 to 9 and A to F**
- binary (base 2) → **0 and 1**
- decimal (base 10) → **0 to 9**
- octal (base 8) → **0 to 7**

Full working after a second miss:

> The right pairs are:  
> hexadecimal (base 16) → 0 to 9 and A to F  
> binary (base 2) → 0 and 1  
> decimal (base 10) → 0 to 9  
> octal (base 8) → 0 to 7  

> Match each number system to its digits.

Right-hand side (shuffled): 0 to 9 and A to F · 0 to 7 · 0 to 9 · 0 and 1
- decimal (base 10) → **0 to 9**
- octal (base 8) → **0 to 7**
- binary (base 2) → **0 and 1**
- hexadecimal (base 16) → **0 to 9 and A to F**

Full working after a second miss:

> The right pairs are:  
> decimal (base 10) → 0 to 9  
> octal (base 8) → 0 to 7  
> binary (base 2) → 0 and 1  
> hexadecimal (base 16) → 0 to 9 and A to F  

> Match each number system to its digits.

Right-hand side (shuffled): 0 to 9 and A to F · 0 to 7 · 0 and 1 · 0 to 9
- binary (base 2) → **0 and 1**
- hexadecimal (base 16) → **0 to 9 and A to F**
- decimal (base 10) → **0 to 9**
- octal (base 8) → **0 to 7**

Full working after a second miss:

> The right pairs are:  
> binary (base 2) → 0 and 1  
> hexadecimal (base 16) → 0 to 9 and A to F  
> decimal (base 10) → 0 to 9  
> octal (base 8) → 0 to 7  

Sources: number-systems (Binary, octal, decimal and hexadecimal; bits and bytes; ASCII (A = 65, a = 97, 0 = 48, space = 32) and Unicode)

### `s2-14-why` · Lesson 14 · multiple choice, level 3

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| Why do computers use binary? | Their circuits have two states, on and off. | Binary numbers are shorter. · Ten is too big for a computer. · Programmers like the number two. | Binary numbers are longer. · That is not the reason. · That is not the reason. | Two states fit the two digits 0 and 1. |
| Which number system is often used for colours on web pages? | hexadecimal | Roman numerals · binary only · decimal only | Roman numerals are not used. · Colours are written in hex, e.g. #FF0000. · Colours are written in hex. | Colours are written like #FF0000. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> Why do computers use binary?

- ◻️ Binary numbers are shorter.  
  _↳ feedback if chosen: Binary numbers are longer._
- ◻️ Ten is too big for a computer.  
  _↳ feedback if chosen: That is not the reason._
- ◻️ Programmers like the number two.  
  _↳ feedback if chosen: That is not the reason._
- ✅ Their circuits have two states, on and off.

Full working after a second miss:

> Two states fit the two digits 0 and 1.  
> So the answer is “Their circuits have two states, on and off.”.  

> Which number system is often used for colours on web pages?

- ◻️ decimal only  
  _↳ feedback if chosen: Colours are written in hex._
- ✅ hexadecimal
- ◻️ Roman numerals  
  _↳ feedback if chosen: Roman numerals are not used._
- ◻️ binary only  
  _↳ feedback if chosen: Colours are written in hex, e.g. #FF0000._

Full working after a second miss:

> Colours are written like #FF0000.  
> So the answer is “hexadecimal”.  

> Which number system is often used for colours on web pages?

- ◻️ decimal only  
  _↳ feedback if chosen: Colours are written in hex._
- ✅ hexadecimal
- ◻️ binary only  
  _↳ feedback if chosen: Colours are written in hex, e.g. #FF0000._
- ◻️ Roman numerals  
  _↳ feedback if chosen: Roman numerals are not used._

Full working after a second miss:

> Colours are written like #FF0000.  
> So the answer is “hexadecimal”.  

Sources: number-systems (Binary, octal, decimal and hexadecimal; bits and bytes; ASCII (A = 65, a = 97, 0 = 48, space = 32) and Unicode)

### `s2-15-bits` · Lesson 15 · multiple choice, level 1

Prompt: {X.q}

Table `X` (one row is picked each time):

| q | r | w | e | y |
|---|---|---|---|---|
| How many bits are in a byte? | 8 | 2 · 10 · 1024 | That is too few. · A byte is 8 bits. · That is the bytes in a kilobyte. | 1 byte = 8 bits. |
| What is a bit? | a binary digit, 0 or 1 | a group of 8 bytes · a letter · a decimal number | That is backwards. · A letter needs a byte or more. · A bit is binary. | Bit = binary digit. |
| What is the largest number one byte can store? | 255 | 256 · 8 · 100 | There are 256 values, from 0 to 255. · That is the number of bits. · It is 255. | 11111111₂ = 255. |

Right answer: `{X.r}`; wrong choices: `{X.w[0]}`, `{X.w[1]}`, `{X.w[2]}`

- Feedback `w0`: “{X.e[0]}”
- Feedback `w1`: “{X.e[1]}”
- Feedback `w2`: “{X.e[2]}”

Three generated variants:

> What is the largest number one byte can store?

- ◻️ 8  
  _↳ feedback if chosen: That is the number of bits._
- ✅ 255
- ◻️ 100  
  _↳ feedback if chosen: It is 255._
- ◻️ 256  
  _↳ feedback if chosen: There are 256 values, from 0 to 255._

Full working after a second miss:

> 11111111₂ = 255.  
> So the answer is “255”.  

> What is a bit?

- ◻️ a group of 8 bytes  
  _↳ feedback if chosen: That is backwards._
- ✅ a binary digit, 0 or 1
- ◻️ a letter  
  _↳ feedback if chosen: A letter needs a byte or more._
- ◻️ a decimal number  
  _↳ feedback if chosen: A bit is binary._

Full working after a second miss:

> Bit = binary digit.  
> So the answer is “a binary digit, 0 or 1”.  

> What is the largest number one byte can store?

- ◻️ 8  
  _↳ feedback if chosen: That is the number of bits._
- ✅ 255
- ◻️ 100  
  _↳ feedback if chosen: It is 255._
- ◻️ 256  
  _↳ feedback if chosen: There are 256 values, from 0 to 255._

Full working after a second miss:

> 11111111₂ = 255.  
> So the answer is “255”.  

Sources: number-systems (Binary, octal, decimal and hexadecimal; bits and bytes; ASCII (A = 65, a = 97, 0 = 48, space = 32) and Unicode)

