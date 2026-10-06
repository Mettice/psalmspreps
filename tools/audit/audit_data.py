"""Audit judgements for the 9 non-Maths subjects (read by build_audit.py).

rows: (spine seq, class, question types, assets, note)
  class: C computed, F fact table, A authored, X paper-only, D deferred
  assets: comma-separated, d: drawn SVG, m: drawn SVG map, g: drawn by code. "(shared ...)" is ignored when
  counting unique assets.
These are judgement calls made from the lesson titles alone (2026-10-03), before any content exists.
"""

SUBJECTS = {}

# ------------------------------------------------------------------------------------------------ Biology
SUBJECTS["biology"] = dict(
    rows=[
        (1, "A", "MCQ MAT", "", ""),
        (2, "F", "TBL MCQ MAT", "", "one table of characteristics with examples"),
        (3, "F", "TBL MAT(sort)", "", "sort items: living vs non-living, plant vs animal"),
        (4, "A", "ORD MCQ", "", "steps of the scientific approach in order"),
        (5, "A", "MCQ", "", ""),
        (6, "X", "LBL MAT PAP", "d:lab equipment set", "hands-on; the app can quiz safety rules and equipment names"),
        (7, "A", "LBL MAT TPL", "d:microscope, d:hand lens", "total magnification = eyepiece × objective is computed"),
        (8, "X", "PAP TPL", "", "needs a microscope; magnification questions are computed"),
        (9, "A", "MCQ ORD", "", "discovery names and dates are P1 facts"),
        (13, "A", "LBL MAT", "d:plant cell, d:animal cell", ""),
        (14, "X", "PAP LBL", "d:plant cell (shared), d:animal cell (shared)", "needs a microscope"),
        (15, "F", "TBL MAT(sort)", "", "climatic vs edaphic factors"),
        (16, "A", "MCQ", "", ""),
        (17, "F", "TBL MAT", "", "predation, parasitism, mutualism, competition…"),
        (18, "X", "PAP MCQ", "", "field collection; app covers safety and preserving only"),
        (19, "A", "ORD MCQ TBL", "d:soil profile", "soil types (sand, clay, loam) as a small table"),
        (20, "A", "MCQ", "", ""),
        (21, "A", "MCQ", "", ""),
        (25, "A", "MCQ", "", ""),
        (26, "F", "TBL MAT LBL", "d:erosion types", "sheet, rill, gully, splash"),
        (27, "A", "MCQ MAT", "", ""),
        (28, "A", "MCQ MAT", "", "tools ↔ methods"),
        (29, "A", "MCQ MAT", "", ""),
        (30, "A", "MCQ", "", ""),
        (31, "A", "MCQ", "", "status changes over time: needs dated sources"),
        (32, "A", "MCQ MAT", "", "health safety: no doses, no self-treatment advice"),
        (33, "A", "ORD MCQ", "", "health safety: preparation in general terms only"),
        (37, "A", "MCQ MAT", "", "sensitive: see Risks"),
        (38, "A", "MCQ", "", "sensitive: see Risks"),
        (39, "A", "MCQ", "", "sensitive: see Risks"),
        (40, "F", "TBL MAT", "", "the sheet itself asks for a table (agent, spread, signs, prevention); sensitive"),
        (41, "A", "MCQ", "", "sensitive; must follow current national guidance"),
        (42, "F", "TBL MAT(sort)", "", "food → class → function (shared with Home Economics row 3)"),
        (43, "F", "TBL MAT", "", "deficiency ↔ disease"),
        (44, "A", "MCQ", "d:food plate", ""),
        (45, "C", "TPL MCQ", "g:food label", "per-portion values computed from a generated label"),
        (49, "F", "TBL MAT(sort)", "", "shared with Chemistry row 49"),
        (50, "F", "TBL MAT", "", "pollutant ↔ source ↔ effect (shared with Chemistry row 56)"),
        (51, "A", "ORD MCQ", "", ""),
        (52, "X", "PAP ORD", "d:filter layers", "hands-on; the order of the filter layers can be checked"),
        (53, "A", "MCQ MAT", "", ""),
        (54, "A", "MCQ MAT", "", ""),
        (55, "F", "TBL TPL MCQ", "g:food web", "authored who-eats-whom list; levels and 'what if X disappears' computed"),
        (56, "A", "MCQ", "", "Cameroon law: P1, needs the legal text"),
    ],
    summary=(
        "Mostly facts and classification. About a quarter of the rows fit a fact table (classify, match, sort) "
        "that one review covers. Only Lesson 45 (food labels) and the magnification and food-web parts are "
        "computed. Five practicals need equipment; the app can prepare for them but not replace them."
    ),
    offline="All rows can work offline. No audio needed. The practicals (rows 6, 8, 14, 18, 52) need a "
            "microscope, specimens or materials: the app gives the safety rules, the steps and a self-check, and "
            "marks them 'do with a teacher'.",
    gaps=(
        "- **Matching** and **sort into groups** (used by 17 rows).\n"
        "- **Labelling**: SVG with numbered pins; the pupil picks a name for each pin (works at 360px, no drag).\n"
        "- **Fact-table templates**: draw rows from an authored table, with distractors from other rows "
        "(an extension of the current `pool` mechanism).\n"
        "- **Generated food label** (HTML table, values computed) and **food-web graph** helpers (levels, "
        "what eats what, effect of removing one species).\n"
        "- **Paper-only / practical flow**: steps + self-check, not counted toward mastery.\n"
        "- **Sensitive-content gate** for rows 37–41 (see Risks): a decision, not only code."
    ),
    conventions=[
        "How many characteristics of living things are taught, and which mnemonic (MRS GREN or another).",
        "Wording and depth for reproductive health (rows 37–41): agree with the school's textbook.",
    ],
    reviewer="a Biology teacher; rows 32–33 and 37–41 also a health worker (school nurse or doctor).",
    risks=(
        "- **Sensitive topics (rows 37–41: puberty, menstruation, pregnancy, STIs, HIV).** Accuracy is P1 and "
        "tone matters. Decide whether these unlock only after a parent has previewed them.\n"
        "- **Medicinal plants (rows 32–33).** Never give doses or recipes that a child could try. Teach the idea, "
        "safety and conservation only.\n"
        "- **Changing facts (rows 31, 56).** Conservation status and laws change: each fact needs a dated source.\n"
        "- **Spine oddity, not a fix:** rows 34–36 sit in the 'Role of medicinal plants' chapter but assess "
        "'Understanding soil' (`assesses` field). This is as on the official sheet.\n"
        "- **Overlaps:** water sources and pollution (Chemistry), food classes (Home Economics). Write once, share."
    ),
)

# ------------------------------------------------------------------------------------------------ Chemistry
SUBJECTS["chemistry"] = dict(
    rows=[
        (1, "A", "MCQ", "", ""),
        (2, "A", "MCQ MAT", "", ""),
        (3, "F", "TBL LBL MAT", "d:lab equipment set (shared with Biology, Physics)", ""),
        (4, "F", "TBL LBL MAT", "d:lab equipment set (shared)", ""),
        (5, "F", "TBL MAT LBL", "d:hazard symbols", "8–9 symbols, drawn by us (shared with Physics row 19)"),
        (6, "A", "MCQ SPOT", "", "'what is wrong in this picture/story?'"),
        (7, "C", "TPL", "g:measuring cylinder, g:balance", "unit conversions; reading the meniscus"),
        (8, "C", "TPL", "g:thermometer, g:stopwatch", "time units; °C reading"),
        (10, "F", "TBL MAT(sort)", "", "physical vs chemical change"),
        (11, "F", "TBL TPL MAT", "d:particle diagrams", "process name computed from start and end state"),
        (12, "A", "MCQ ORD", "", ""),
        (14, "F", "TBL MAT(sort)", "", ""),
        (15, "F", "TBL MAT", "", ""),
        (16, "F", "TBL ORD", "d:separation set-ups", "mixture → method; steps in order"),
        (17, "F", "TBL ORD LBL", "d:filtration and evaporation", ""),
        (18, "F", "TBL LBL", "d:separating funnel", ""),
        (19, "F", "TBL", "", ""),
        (20, "F", "TBL", "", "check depth for Form 1"),
        (21, "F", "TBL MAT", "", "element names ↔ symbols"),
        (22, "C", "TPL TBL", "", "atoms counted from a formula (H₂O → 2 H, 1 O)"),
        (23, "A", "MAT MCQ", "", ""),
        (25, "F", "TBL MAT(sort)", "", ""),
        (26, "F", "TBL MAT(sort)", "", ""),
        (27, "F", "TBL MAT(sort)", "", ""),
        (28, "F", "TBL MAT", "", ""),
        (30, "F", "TBL MAT(sort)", "", ""),
        (31, "F", "TBL MAT", "", "lemon → citric acid, etc."),
        (32, "F", "TBL MAT", "", ""),
        (33, "F", "TBL MAT", "", ""),
        (34, "C", "TPL TBL", "", "colour computed from (indicator, acidic/neutral/basic)"),
        (35, "X", "ORD PAP", "", "home practical (e.g. hibiscus); steps can be ordered"),
        (36, "C", "TPL", "g:pH colour scale", "pH → acidic/neutral/basic computed"),
        (37, "C", "TPL TBL", "", "word equations; salt name computed (hydrochloric → chloride…)"),
        (38, "F", "TBL MAT", "", ""),
        (40, "A", "MCQ", "", ""),
        (41, "F", "TBL MAT", "", ""),
        (42, "C", "TPL", "g:pie chart", "volumes from percentages"),
        (43, "A", "MCQ", "", ""),
        (44, "A", "MCQ", "", ""),
        (45, "F", "TBL MAT", "", ""),
        (46, "F", "TBL MAT", "", ""),
        (47, "A", "MCQ", "", ""),
        (49, "F", "TBL MAT(sort)", "", "shared with Biology row 49"),
        (50, "A", "ORD LBL", "d:water cycle", "shared with Geography row 20"),
        (51, "F", "TBL MAT", "", ""),
        (52, "A", "ORD MCQ", "", ""),
        (53, "A", "LBL ORD", "d:distillation apparatus", ""),
        (54, "A", "MCQ", "", ""),
        (55, "F", "TBL MAT", "", "anhydrous copper(II) sulfate, cobalt chloride paper"),
        (56, "F", "TBL MAT", "", "shared with Biology row 50"),
        (57, "F", "TBL MAT", "", "solute, solvent, solution"),
        (58, "C", "TPL", "", "concentration = mass ÷ volume, if in scope"),
        (59, "C", "TPL", "g:solubility table", "saturated or not; mass that crystallises"),
    ],
    summary=(
        "The most 'table-shaped' subject: separation methods, metals and non-metals, acids and bases, "
        "pollutants and tests are all naturally fact tables. Measurement, pH, word equations, air by volume "
        "and solubility can be computed. Little needs equipment."
    ),
    offline="All rows work offline. No audio. Row 35 (extracting an indicator) is a home practical; the app "
            "gives the steps and a self-check.",
    gaps=(
        "- **Matching**, **sort into groups**, **labelling**, **fact-table templates** (as Biology).\n"
        "- **Units library** beyond length: mass (mg, g, kg), volume (cm³, mL, L, dm³), time, temperature. "
        "`convert` in `src/engine/lib/maths.js` only handles metric length today.\n"
        "- **Instrument renderers** (code-drawn SVG with the reading computed): measuring cylinder with meniscus, "
        "balance, thermometer, stopwatch, pH colour scale, pie chart.\n"
        "- **Chemistry helpers**: count atoms in a simple formula; name a salt from acid + base; classify pH.\n"
        "- **Subscripts** in rendered text (H₂O): Unicode subscripts are enough, no MathML needed."
    ),
    conventions=[
        "Composition of air by volume: which rounded figures (78 / 21 / 1 or with 0.04 for CO₂).",
        "Hazard symbols: the current GHS diamonds or the older orange squares still found in some textbooks.",
        "Units for concentration and solubility: g/L or g/dm³; g per 100 g of water.",
    ],
    reviewer="a Chemistry teacher.",
    risks=(
        "- **Safety rows (5, 6)** are P1: a wrong hazard meaning could hurt someone.\n"
        "- **Scope:** some titles (gas-gas separation, solutions, solubility) may go beyond what Form 1 "
        "teaches in practice; the teacher should confirm depth before writing.\n"
        "- **Overlaps:** water and pollution (Biology), water cycle (Geography), lab equipment and hazard "
        "symbols (Physics), states of matter (Physics rows 11–12). Write once, share."
    ),
)

# ------------------------------------------------------------------------------------------------ Physics
SUBJECTS["physics"] = dict(
    rows=[
        (1, "F", "TBL MAT", "", "branch ↔ what it studies"),
        (2, "F", "TBL MAT ORD", "", "scientist ↔ discovery ↔ date; dates are P1"),
        (3, "F", "TBL MAT", "", ""),
        (4, "A", "MCQ ORD", "", ""),
        (5, "F", "TBL LBL", "d:lab equipment set (shared with Biology, Chemistry)", ""),
        (6, "A", "MCQ", "", ""),
        (7, "A", "MCQ MAT", "", "low stakes; careers facts are P2"),
        (8, "C", "TPL TBL", "g:ruler, g:scales", "instrument ↔ quantity; readings computed"),
        (9, "F", "TBL MAT(sort)", "", ""),
        (10, "C", "TPL TBL", "", "quantity ↔ SI unit ↔ symbol; prefixes computed"),
        (11, "F", "TBL MAT", "d:particle diagrams (shared with Chemistry)", ""),
        (12, "F", "TBL TPL", "", "same process table as Chemistry row 11"),
        (13, "C", "TPL", "g:ruler", ""),
        (14, "C", "TPL", "g:beam balance", ""),
        (15, "C", "TPL TBL", "", "W = m × g"),
        (16, "C", "TPL", "g:measuring cylinder, g:cuboid", "displacement V₂ − V₁; l × w × h"),
        (17, "C", "TPL", "", "density = mass ÷ volume; float or sink in water"),
        (18, "C", "TPL", "g:thermometer", "°C ↔ K"),
        (19, "F", "TBL MAT LBL", "d:hazard symbols (shared with Chemistry)", ""),
        (20, "F", "TBL MAT(sort)", "", ""),
        (21, "F", "TBL MAT", "", "device → energy in → energy out"),
        (22, "A", "LBL MCQ", "d:solar home system", ""),
        (23, "F", "TBL MAT", "", ""),
        (24, "F", "TBL MAT", "", ""),
        (25, "F", "TBL MAT(sort)", "d:conduction convection radiation", ""),
        (26, "F", "TBL MAT(sort)", "d:force arrows", ""),
        (27, "F", "TBL MAT(sort)", "", ""),
        (28, "A", "MCQ MAT", "d:road signs", "road safety: P1"),
        (29, "A", "MCQ", "", ""),
        (30, "A", "LBL MCQ", "d:ear", ""),
        (31, "A", "MCQ", "", ""),
        (32, "C", "TPL", "g:clinical thermometer", "normal or not, from a range"),
        (33, "A", "MCQ", "d:posture figures", ""),
        (34, "A", "MCQ", "d:radiation symbol", "safety facts: P1"),
        (35, "A", "LBL ORD MCQ", "d:greenhouse effect", ""),
        (36, "A", "MCQ", "", "shared with Geography row 21, English row 86"),
        (37, "F", "TBL MAT LBL", "d:hand tools", "tool ↔ use"),
        (38, "A", "MCQ", "", ""),
        (39, "F", "TBL LBL PAP", "d:drawing instruments", "the sample drawing itself is paper-only"),
    ],
    summary=(
        "The measurement block (rows 8–18 and 32) is as computable as Maths: unit conversions, readings from "
        "code-drawn instruments, weight, volume by displacement, density, temperature. Energy, forces and "
        "motion are classification tables. The rest is short authored facts."
    ),
    offline="All rows work offline. No audio is needed (row 29, sound, can be taught without playing sounds).",
    gaps=(
        "- **Units library** (shared with Chemistry): length, mass, volume, time, temperature, SI prefixes.\n"
        "- **Instrument renderers**: ruler, beam balance, measuring cylinder, thermometer, clinical thermometer, "
        "with the reading computed and the scale drawn from the same numbers.\n"
        "- **Decimal answers with units**: numeric input that accepts '2.5', '2,5' (comma decimal is common in "
        "Cameroon) and checks the unit when asked.\n"
        "- **Matching**, **sort into groups**, **labelling**, **fact-table templates**."
    ),
    conventions=[
        "Value of g: 10 N/kg (usual at this level) or 9.8 N/kg.",
        "Kelvin conversion: K = °C + 273 or + 273.15.",
        "Normal body temperature range for row 32 (about 36.5–37.5 °C) and the fever threshold.",
    ],
    reviewer="a Physics teacher; row 34 (radiation safety) should be checked against an official source.",
    risks=(
        "- **Decimal comma.** Pupils may type 2,5 for 2.5. Decide one rule and test it.\n"
        "- **Road signs (row 28):** draw our own, following the signs used in Cameroon.\n"
        "- **Overlaps:** lab equipment, hazard symbols and states of matter (Chemistry); climate change "
        "(Geography, English); heat transfer (Home Economics row 32)."
    ),
)

# ------------------------------------------------------------------------------------------------ Computer science
SUBJECTS["computer-science"] = dict(
    rows=[
        (1, "A", "MCQ", "", ""),
        (2, "F", "TBL ORD MAT", "", "computer generations; order computed from dates; dates are P1"),
        (3, "F", "TBL MAT(sort)", "", ""),
        (4, "A", "MCQ", "", ""),
        (5, "A", "MCQ", "", "ethics answers are judgement (P2) unless they state a law"),
        (6, "A", "MCQ SPOT", "", "no AI offline: 'which prompt is clearer, what is missing'; live practice deferred"),
        (8, "A", "ORD MAT", "", ""),
        (9, "C", "TPL", "g:shape sequences", "next term computed from a generated rule"),
        (10, "A", "MCQ", "", ""),
        (11, "C", "TPL ORD", "", "trace a short algorithm; output computed"),
        (13, "F", "TBL MAT", "", ""),
        (14, "F", "TBL MAT(sort)", "", "data vs information"),
        (16, "F", "TBL LBL", "d:lab devices", ""),
        (17, "A", "LBL MCQ", "d:lab layouts", ""),
        (18, "A", "MCQ", "", ""),
        (20, "F", "TBL MAT", "d:PC types", ""),
        (21, "F", "TBL LBL", "d:computer parts", ""),
        (22, "X", "PAP TPL LBL", "d:keyboard", "mouse and keyboard need a computer; touch gestures can be drilled and checked in the app"),
        (24, "F", "TBL MAT", "", ""),
        (25, "F", "TBL MAT(sort)", "", ""),
        (26, "A", "MCQ", "", ""),
        (27, "A", "MCQ", "", "hands-on part needs an AI tool: deferred"),
        (29, "A", "MCQ", "", ""),
        (30, "A", "MCQ", "", ""),
        (31, "A", "MCQ", "", ""),
        (33, "A", "LBL MCQ", "d:block editor screen", ""),
        (34, "C", "TPL ORD", "", "pseudocode traced by code; blocks put in order"),
        (35, "D", "PAP", "", "needs a block editor (see Engine gaps)"),
        (37, "F", "TBL MAT(sort)", "", "input / output / storage"),
        (38, "F", "TBL LBL", "d:ports", ""),
        (39, "A", "ORD", "", ""),
        (40, "F", "TBL MAT(sort)", "", ""),
        (41, "F", "TBL MAT(sort)", "", ""),
        (43, "F", "TBL LBL", "d:window parts", ""),
        (44, "C", "TPL ORD", "g:folder tree", "path after move or copy computed on a simulated tree"),
        (46, "F", "TBL LBL", "d:word processor toolbar", ""),
        (47, "C", "TPL LBL", "g:spreadsheet grid", "formula results computed (SUM, AVERAGE, + − × ÷)"),
        (48, "F", "TBL LBL", "d:graphics toolbar", ""),
        (50, "A", "MCQ", "", ""),
        (51, "C", "TBL TPL", "", "browser vs search engine; URL parts computed"),
        (53, "A", "MCQ", "", "electrical and fire safety: P1"),
        (54, "A", "MCQ", "", ""),
    ],
    summary=(
        "Two halves. The thinking and tools rows (patterns, algorithms, pseudocode, folders, spreadsheets, URLs) "
        "can be computed, and they reuse the existing safe expression evaluator. The hardware and software rows "
        "are fact tables with many labelled pictures. AI and ethics rows are judgement, mostly P2. Real "
        "hands-on practice (keyboard, mouse, block programming, AI tools) needs a computer."
    ),
    offline="All rows can be taught offline. Deferred: row 35 (writing programs in a block editor). Partly "
            "deferred: rows 6 and 27 (using a real AI tool) and row 22 (mouse and keyboard on a real computer).",
    gaps=(
        "- **Mini interpreter** for pseudocode tracing: variables, assignment, IF, a counted loop, OUTPUT. "
        "It can reuse `src/engine/expr.js` (no eval).\n"
        "- **Sequence generator** for pattern recognition (number and shape rules).\n"
        "- **Spreadsheet evaluator**: cell references, ranges, SUM, AVERAGE, MIN, MAX on top of `expr.js`.\n"
        "- **Folder-tree simulator** (create, move, copy, rename, path) and **URL parser**.\n"
        "- **Touch-gesture drill** (tap, double tap, long press, drag), checked by the app itself.\n"
        "- **Block editor:** Blockly is roughly 700 KB minified, a third of the whole 2 MB budget. A tiny "
        "custom block editor (sequence, repeat, if; about 10 blocks) is possible but is real engine work. "
        "Decision for Dion: build small, or keep row 35 on paper.\n"
        "- **Labelling**, **matching**, **sort into groups**, **fact-table templates**."
    ),
    conventions=[
        "Computer generations: which dates and defining technologies the school uses (textbooks differ).",
    ],
    reviewer="a Computer Science teacher.",
    risks=(
        "- **AI rows (4–6, 26–27)** date quickly: keep them about ideas (what a prompt is, checking answers, "
        "privacy), not about named products.\n"
        "- **Ethics rows (29–31)** are judgement: write clear-cut scenarios so the key is not arguable."
    ),
)

# ------------------------------------------------------------------------------------------------ English language
_EN = {
    1: ("A", "MCQ ORD PAP", "", "choose the right reply; put a dialogue in order; speaking itself is paper/aloud"),
    2: ("F", "TBL CLZ", "", "spelling rules as cloze"),
    3: ("C", "TPL CLZ", "", "-s/-es/-ies and do/does forms computed from sentence frames"),
    4: ("D", "MCQ", "", "speech work: needs audio"),
    5: ("C", "TPL MCQ", "g:timetable", "questions on a generated timetable; irregular verbs from a table"),
    6: ("C", "TPL", "", "number words (reuse words() from Maths)"),
    7: ("C", "TPL CLZ", "", "-ing spelling rules computed"),
    8: ("D", "MCQ", "", "speech work: needs audio"),
    9: ("X", "PAP TPL", "", "the cost of a list within a budget can be computed"),
    10: ("F", "TBL MAT(sort)", "", ""),
    11: ("C", "TPL CLZ", "", "-ed rules + irregular verb table"),
    12: ("D", "MCQ", "", "speech work: needs audio"),
    13: ("A", "MCQ PAP", "", ""),
    14: ("F", "TBL MAT", "", "compounds and conversion from a word table"),
    15: ("C", "TPL CLZ", "", "past participles from the verb table"),
    16: ("A", "CLZ LBL", "g:form", "fill in a form; fields checked"),
    17: ("A", "ORD PAP", "", "stages in order; the description is paper-only"),
    18: ("D", "MCQ", "", "speech work: needs audio"),
    19: ("C", "TPL CLZ", "", "adverb position and 'will' from sentence frames"),
    20: ("D", "MCQ", "", "speech work: needs audio"),
    21: ("A", "MCQ", "", "needs an original passage"),
    22: ("X", "LBL PAP", "d:letter layout", "letter parts labelled; the letter is paper-only"),
    23: ("F", "TBL MAT", "", ""),
    24: ("A", "MCQ CLZ", "", ""),
    25: ("F", "TPL CLZ", "", "a/an needs an exceptions list (an hour, a uniform)"),
    26: ("A", "MCQ", "", "needs short passages"),
    27: ("C", "TPL LBL", "g:room scene", "positions in a generated scene; preposition computed"),
    28: ("X", "PAP", "", ""),
    29: ("A", "MCQ", "", "needs an original dialogue and poem"),
    30: ("F", "TBL MAT", "", ""),
    31: ("C", "TPL CLZ", "", "same verb table as rows 11 and 15"),
    32: ("D", "MCQ", "", "speech work: needs audio"),
    33: ("X", "PAP", "", ""),
    34: ("X", "PAP", "", ""),
    35: ("A", "MCQ CLZ", "", ""),
    36: ("X", "PAP", "", ""),
    37: ("C", "TPL CLZ", "", "-er/-est, more/most, irregular table"),
    38: ("X", "PAP", "", ""),
    39: ("A", "CLZ MCQ", "", ""),
    41: ("D", "MCQ", "", "listening: needs audio"),
    42: ("F", "TBL MAT", "", ""),
    43: ("C", "TPL CLZ", "", ""),
    44: ("A", "MCQ", "", "needs an original passage (facts shared with Biology row 44)"),
    45: ("A", "MCQ PAP", "", ""),
    46: ("F", "TBL MAT", "", ""),
    47: ("C", "TPL CLZ", "", "statement → imperative from frames"),
    48: ("D", "MCQ", "", "listening: needs audio"),
    49: ("X", "PAP", "", ""),
    50: ("F", "TBL MAT", "", ""),
    51: ("F", "TBL MAT(sort) TPL", "", "capital letters checked by code"),
    52: ("A", "CLZ", "", ""),
    53: ("A", "MCQ ORD PAP", "", "doctor dialogue"),
    54: ("F", "TBL MAT", "", ""),
    55: ("F", "TBL MAT(sort)", "", ""),
    56: ("F", "TBL TPL MAT", "", "affix meanings from a table; the new word built by code"),
    57: ("D", "MCQ", "", "listening: needs audio"),
    58: ("C", "TPL CLZ", "", "plural rules + irregular table"),
    59: ("C", "TPL CLZ", "", "tag computed from the sentence frame"),
    61: ("A", "MCQ", "", "needs an original passage"),
    62: ("F", "TBL MAT", "", ""),
    63: ("A", "CLZ SPOT", "", ""),
    64: ("X", "PAP", "", ""),
    65: ("D", "MCQ PAP", "", "listening: needs audio"),
    66: ("F", "TBL MAT", "", ""),
    67: ("A", "CLZ MCQ", "", ""),
    68: ("X", "PAP", "", ""),
    69: ("A", "MCQ", "", "needs an original article"),
    70: ("F", "TBL MAT", "", ""),
    71: ("F", "TBL", "", "syllable splits authored per word; code cannot syllabify reliably"),
    72: ("D", "MCQ", "", "speech work: needs audio"),
    73: ("X", "PAP MCQ", "", ""),
    74: ("C", "TPL ORD", "", "alphabetical order and guide words computed"),
    75: ("C", "TPL CLZ", "", "first and second conditional from frames"),
    76: ("A", "MCQ", "", "needs original texts"),
    77: ("A", "MCQ", "", "needs an original text"),
    78: ("F", "TBL MAT", "", "the /ə/ sound part needs audio"),
    79: ("A", "CLZ MCQ", "", ""),
    81: ("X", "PAP", "", ""),
    82: ("F", "TBL MAT", "", ""),
    83: ("D", "MCQ", "", "speech work: needs audio"),
    84: ("A", "CLZ MCQ", "", ""),
    85: ("A", "MCQ", "d:hazard scenes", "pictures and texts"),
    86: ("F", "TBL MAT", "", ""),
    87: ("F", "TBL MAT(sort)", "", ""),
    88: ("X", "PAP", "", ""),
    89: ("A", "MCQ", "", "needs an original text"),
    90: ("A", "CLZ MCQ", "", ""),
    91: ("A", "MAT(sort) MCQ", "", "simple, compound, complex"),
    92: ("X", "PAP", "", ""),
    93: ("X", "PAP", "", ""),
    94: ("C", "TPL CLZ", "", "reuses row 59"),
    95: ("C", "TPL CLZ", "", "contraction table"),
    96: ("C", "TPL PAP", "g:street grid", "directions on a generated street grid checked by code; writing them is paper-only"),
    97: ("D", "MCQ", "", "listening: needs audio"),
    98: ("F", "TBL MAT", "", ""),
    99: ("X", "PAP", "", ""),
    100: ("X", "PAP", "", ""),
    101: ("A", "MCQ", "", "needs an original text"),
    102: ("X", "PAP", "", ""),
    103: ("X", "PAP MAT(sort)", "", "sorting dos and don'ts is checkable"),
    104: ("X", "PAP", "", ""),
}
SUBJECTS["english-language"] = dict(
    rows=[(k, *v) for k, v in sorted(_EN.items())],
    summary=(
        "Grammar is the computable part: tenses, plurals, comparatives, question tags, contractions and "
        "conditionals follow rules plus exception tables, so code can build and check them from sentence "
        "frames. Vocabulary is fact tables. Reading needs original passages (the biggest authoring and P1 "
        "load). Writing and speaking cannot be checked by code. Speech work and listening need audio."
    ),
    offline=(
        "**Deferred (audio): 13 rows.** Speech work: 4, 8, 12, 18, 20, 32, 72, 83 (and the /ə/ part of 78). "
        "Listening: 41, 48, 57, 65, 97. Minimal-pair audio at speech quality is roughly 60–120 KB per lesson, "
        "so about 1–1.5 MB for all of them: most of the 2 MB budget. Options: a separate optional 'audio pack' "
        "downloaded once over Wi-Fi, or a grown-up reads the words aloud from a printed list. Decision for Dion.\n\n"
        "**Paper-only: writing and open speaking** (rows marked X). The app shows the task, a model answer and "
        "a checklist; the pupil ticks it off; it does not count toward mastery."
    ),
    gaps=(
        "- **Cloze** (typed word in a gap) with an accepted-answers list and normalisation: case, spaces, "
        "curly vs straight apostrophes (don’t / don't).\n"
        "- **English morphology library**: 3rd person -s, -ing, -ed, plurals, comparatives, contractions, "
        "question tags, a/an; plus authored tables of irregular verbs, plurals and a/an exceptions.\n"
        "- **Sentence frames**: authored sentences with slots (subject, verb, object, polarity) that code "
        "inflects, so the answer is computed.\n"
        "- **Reading passage** item type: one passage, several questions, scroll-friendly at 360px.\n"
        "- **Generated scenes**: room scene for prepositions (row 27), street grid for directions (row 96), "
        "timetable (row 5), form (row 16).\n"
        "- **Paper-only flow** with model answer and checklist.\n"
        "- **Audio playback** (deferred; see above).\n"
        "- **Matching**, **sort into groups**, **fact-table templates**."
    ),
    conventions=[
        "British spelling throughout (colour, centre), and whether both learnt/learned, dreamt/dreamed are accepted.",
        "Question tag for 'I am': aren't I.",
        "a/an by sound, with an authored exceptions list (an hour, a uniform, a European).",
    ],
    reviewer="an English teacher. Reading passages also need a check for level (Form 1) and local relevance.",
    risks=(
        "- **Reading passages must be original.** Textbook passages are copyrighted; poems must be original "
        "or public domain. This is the largest authoring job in any subject (about 12 passages).\n"
        "- **Comprehension keys are P1:** a wrong key teaches the pupil to read wrongly.\n"
        "- **Writing quality cannot be checked offline.** Paper-only tasks need a grown-up to look at them "
        "now and then; the parent summary should list them.\n"
        "- **Overlaps:** health and diet (Biology), climate change (Physics, Geography), numbers (Maths)."
    ),
)

# ------------------------------------------------------------------------------------------------ French
_FR = {
    1: ("C", "TPL ORD", "", "alphabetical order computed; letter names need audio (deferred part)"),
    2: ("A", "MCQ", "", "needs an original text, in French"),
    3: ("F", "TBL MAT", "", ""),
    4: ("F", "TBL TPL CLZ", "", "article from gender + number; needs a noun list with genders"),
    5: ("C", "TPL CLZ", "", "conjugation computed (s'appeler: double l)"),
    6: ("X", "PAP MCQ", "", "oral; choosing the right phrase is checkable"),
    7: ("C", "TPL CLZ", "", ""),
    8: ("C", "TPL CLZ", "", ""),
    9: ("C", "TPL", "", "numbers 1–50 in words"),
    10: ("A", "MCQ", "", "needs an original text"),
    11: ("A", "MCQ", "", "needs an original text"),
    12: ("F", "TBL MAT", "", ""),
    13: ("A", "MCQ MAT", "", ""),
    14: ("C", "CLZ", "", "exact copy, accents checked"),
    15: ("C", "TPL CLZ", "", "mon/ton/son before a vowel (mon amie) computed"),
    17: ("A", "MCQ", "d:scene (sick person)", "picture interpretation as MCQ; oral part paper/aloud"),
    18: ("C", "TPL ORD", "", "next day, the day after, months in order computed"),
    19: ("C", "TPL CLZ", "", "ce/cet/cette/ces; needs an h aspiré list"),
    20: ("A", "MCQ", "", "needs an original text"),
    21: ("C", "TPL CLZ", "", "-yer verbs: both paie/paye-type forms where allowed"),
    22: ("A", "CLZ", "", "homophones as cloze; sounds /u/ /y/ need audio (deferred part)"),
    23: ("A", "MCQ", "", "needs an original text"),
    24: ("F", "TBL MAT", "", ""),
    25: ("C", "TPL CLZ", "", "agreement rules + exception table"),
    26: ("C", "TPL CLZ", "", "impératif présent"),
    27: ("A", "MCQ", "", "needs an original text"),
    28: ("F", "TBL MAT", "", ""),
    29: ("C", "TPL CLZ", "", ""),
    30: ("C", "CLZ", "", "exact copy, accents checked"),
    31: ("C", "TPL", "", "numbers 51–100 in words"),
    33: ("C", "TPL CLZ", "", "ne … pas with elision (n')"),
    34: ("F", "TBL MAT", "", ""),
    35: ("C", "TPL CLZ", "", "nous mangeons, nous commençons"),
    36: ("A", "MCQ", "", "rules extract must be original"),
    37: ("D", "MCQ", "", "sounds: needs audio (spelling part can be written)"),
    38: ("A", "MCQ", "d:flag and coat of arms", "anthem: see Risks"),
    39: ("F", "TBL MAT", "", ""),
    40: ("A", "MAT MCQ", "", "groupe nominal / groupe verbal"),
    41: ("D", "PAP", "", "singing the anthem: with a grown-up"),
    42: ("C", "TPL CLZ", "", "rules + exception table"),
    43: ("C", "TPL CLZ", "", ""),
    44: ("C", "TPL CLZ", "", "capital letter rule (un Camerounais / il est camerounais)"),
    45: ("A", "MCQ", "", "needs an original text"),
    46: ("C", "TPL CLZ", "", "le/la/l'/les substitution from frames"),
    47: ("A", "CLZ LBL", "g:form", "form filling; fields checked"),
    49: ("C", "TPL CLZ", "", "aller + infinitive"),
    50: ("A", "MCQ", "", "needs an original text"),
    51: ("F", "TBL MAT", "", ""),
    52: ("C", "TPL CLZ", "", "gender and plural rules + exception lists"),
    53: ("A", "MCQ", "d:market scene", "picture interpretation"),
    54: ("C", "TPL CLZ", "", "est-ce que / inversion with -t-"),
    55: ("C", "TPL CLZ", "", "j'achète; payer: two forms"),
    56: ("F", "TBL MAT", "", ""),
    57: ("A", "MCQ", "", "needs an original text"),
    58: ("D", "MCQ", "", "sounds: needs audio"),
    59: ("C", "TPL CLZ", "", "à/en/au/aux + country computed from a gender table"),
    60: ("A", "MCQ", "", "needs an original text"),
    61: ("X", "PAP", "", ""),
    62: ("C", "TPL CLZ", "", "du/de la/de l'/des; de after a negative"),
    63: ("C", "TPL CLZ", "", ""),
    65: ("F", "TBL MAT", "", ""),
    66: ("A", "MCQ", "", "needs an original text"),
    67: ("C", "TPL CLZ", "", ""),
    68: ("C", "TPL CLZ", "", "rules + exception list"),
    69: ("A", "MCQ", "d:ICT scene", "picture interpretation"),
    70: ("C", "TPL CLZ", "", ""),
    71: ("D", "MCQ", "", "sounds: needs audio"),
    72: ("C", "TPL CLZ", "", "celui/celle/ceux/celles"),
    73: ("A", "MCQ", "", "needs an original text"),
    74: ("F", "TBL MAT", "", ""),
    75: ("F", "TBL LBL", "d:computer parts (shared with Computer Science)", ""),
    76: ("A", "ORD MCQ", "", "instructions put in order"),
    77: ("A", "CLZ", "", ""),
    78: ("C", "TPL CLZ", "", "le mien / la mienne …"),
    79: ("F", "TBL MAT", "", ""),
}
SUBJECTS["french"] = dict(
    rows=[(k, *v) for k, v in sorted(_FR.items())],
    summary=(
        "The most computable language subject. Almost half the rows (33 of 75) are conjugation, numbers in words and "
        "grammar agreement (articles, possessives, demonstratives, gender and plural, partitives), which "
        "rules plus exception lists can generate and check. Reading needs original French texts. All lesson "
        "text, feedback and hints must be in French (brief constraint)."
    ),
    offline=(
        "**Deferred (audio): rows 37, 58, 71** (sounds), plus the sound parts of rows 1 and 22. Row 41 "
        "(singing the anthem) is with a grown-up. Same audio-budget problem as English.\n\n"
        "**Paper-only:** rows 6 and 61 (speaking and writing)."
    ),
    gaps=(
        "- **French conjugation library**: present (regular -er, -cer/-ger, -yer, -eler, e→è), imperative, "
        "futur proche; authored tables for avoir, être, faire, prendre, devoir, pouvoir, vouloir, vendre, lire, "
        "écrire, suivre.\n"
        "- **French numbers in words** (1–100), with the chosen spelling convention.\n"
        "- **Agreement helpers**: articles, partitives, possessives, demonstratives, feminine and plural of "
        "nouns and adjectives, elision (l', n', cet), country prepositions; from a noun list with genders.\n"
        "- **Cloze with French normalisation**: apostrophes ’ vs ', and an accent policy (strict for "
        "orthographe and copying rows; lenient elsewhere, with a 'watch the accent' note).\n"
        "- **French UI strings**: feedback, hints, buttons ('Je ne sais pas') in French for French lessons.\n"
        "- **Reading passage** type, **paper-only flow**, **audio** (deferred), **matching**, **fact tables**."
    ),
    conventions=[
        "Numbers in words: traditional hyphens (vingt et un) or the 1990 rules (vingt-et-un); accept both?",
        "-yer verbs (payer, balayer): accept both je paie and je paye.",
        "Nationality capitals: noun capitalised (un Camerounais), adjective not (il est camerounais).",
        "Accents in typed answers: strict or lenient, per question type.",
        "The h aspiré list used for ce/cet and elision.",
    ],
    reviewer="a French teacher (FLE / bilingual-system French). Not the same person as for English.",
    risks=(
        "- **Language constraint:** French content in French. Every note, card, hint and feedback line needs a "
        "French reviewer, so P1 review cannot be shared with other subjects.\n"
        "- **National anthem (rows 38, 41):** do not ship the lyrics in the app; the pupil learns them from "
        "school or a grown-up. Teach the emblems instead.\n"
        "- **Reading texts must be original** (about 15 short texts).\n"
        "- **Typing accents on a phone** is slow for a Form 1 pupil: consider an accent bar (é è ê à ç ù) "
        "above the keyboard in cloze questions."
    ),
)

# ------------------------------------------------------------------------------------------------ Geography
SUBJECTS["geography"] = dict(
    rows=[
        (1, "F", "TBL MAT", "", ""),
        (2, "F", "TBL ORD", "d:solar system", "planet order computed from a distance table"),
        (3, "F", "TBL LBL TPL", "m:world", "named parallels; continents and oceans ordered by area (computed)"),
        (4, "C", "LBL TPL", "g:sample map", "marginal information labelled; distances from the scale computed"),
        (5, "C", "TPL", "g:grid map", "grid references computed"),
        (6, "C", "TPL", "g:graticule", "latitude and longitude read and computed"),
        (7, "A", "MCQ LBL", "d:rotation and revolution", ""),
        (8, "C", "TPL", "", "15° per hour, 4 minutes per degree; east is ahead"),
        (9, "C", "TPL", "", "same library as row 8; basis of time zones"),
        (10, "F", "TBL MAT", "", ""),
        (11, "A", "MCQ LBL", "m:Cameroon natural regions", "climate figures are P1"),
        (12, "A", "MCQ LBL", "m:Cameroon natural regions (shared)", ""),
        (13, "C", "TPL", "g:climograph", "generated data (computed answers) or a named station's data (P1)"),
        (14, "F", "TBL MAT", "", "cause ↔ consequence ↔ solution"),
        (15, "X", "PAP", "", "field visit around the school"),
        (16, "X", "PAP MAT(sort)", "", "collecting is hands-on; sorting waste is checkable (shared with Home Economics)"),
        (17, "F", "TBL ORD LBL", "d:atmosphere layers", "layer order from altitudes; composition shared with Chemistry"),
        (18, "A", "LBL MCQ", "d:pressure belts and winds", ""),
        (19, "F", "TBL MAT", "d:cloud types", ""),
        (20, "A", "ORD MCQ", "", "rain formation in order (shared with Chemistry row 50)"),
        (21, "A", "MCQ", "", "shared with Physics row 36"),
        (22, "F", "TBL LBL ORD", "d:earth layers", ""),
        (23, "F", "TBL MAT LBL", "d:plate boundaries", ""),
        (24, "A", "LBL MCQ", "d:volcano", ""),
        (25, "A", "ORD MCQ", "", "safety steps: P1"),
    ],
    summary=(
        "Small (25 rows) and unusually computable for a humanities subject: map skills (scale, grid "
        "references, latitude and longitude), local time and the climograph are Maths-like. The cost is in "
        "drawings: two maps and about eight diagrams."
    ),
    offline="All rows work offline. No audio. Row 15 (visit around the school) and the collecting in row 16 "
            "are paper-only field work.",
    gaps=(
        "- **Geography library**: local time from longitude (and the reverse), latitude/longitude formatting "
        "(°N/S/E/W), 4- and 6-figure grid references, map scale (cm on map → km).\n"
        "- **Code-drawn maps**: a grid map and a graticule drawn from the question's own numbers, so the "
        "answer is computed; a sample map with marginal information.\n"
        "- **Climograph renderer** (rainfall bars + temperature line) and helpers: range, total, wettest month.\n"
        "- **Drawn SVG maps** (world, Cameroon natural regions), simplified to stay small.\n"
        "- **Labelling**, **matching**, **sort into groups**, **fact-table templates**."
    ),
    conventions=[
        "Tropics and polar circles: 23.5° / 66.5° or 23°26′ / 66°34′.",
        "Climograph: the rule for a 'wet' or 'dry' month (a rainfall threshold, or P = 2T).",
        "Time: GMT or UTC in wording; Cameroon is UTC+1 (West Africa Time).",
    ],
    reviewer="a Geography teacher. The Cameroon map also needs a check of the region boundaries.",
    risks=(
        "- **Map accuracy:** the Cameroon natural-regions map is P1 and the most likely to be wrong if drawn by "
        "hand; trace it from a public-domain source and note the source.\n"
        "- **Real station data** for climographs needs a source; generated data avoids that but should still "
        "look like a real Cameroonian place.\n"
        "- **Overlaps:** atmosphere and water cycle (Chemistry), climate change (Physics, English), waste "
        "(Home Economics)."
    ),
)

# ------------------------------------------------------------------------------------------------ History
SUBJECTS["history"] = dict(
    rows=[
        (1, "A", "MCQ", "", ""),
        (2, "X", "PAP MAT(sort)", "", "collecting relics; sorting sources (oral, written, material) is checkable"),
        (3, "C", "TPL PAP", "", "BC/AD and century arithmetic computed (no year 0); the local enquiry is paper-only"),
        (4, "A", "MCQ LBL", "m:Africa", "fossil dates are P1 (estimates differ by source)"),
        (5, "A", "MCQ", "", ""),
        (6, "A", "MCQ PAP", "", "sensitive (beliefs): see Risks"),
        (7, "F", "TBL MAT(sort)", "", "Old vs New Stone Age"),
        (8, "F", "TBL ORD", "", "order of species computed from dates; dates are P1"),
        (9, "A", "MCQ", "", "Cameroonian sites (e.g. Shum Laka): P1"),
        (10, "A", "MCQ", "", "sensitive naming: see Risks"),
        (11, "A", "MCQ LBL", "d:social pyramid", ""),
        (12, "A", "MCQ", "", ""),
        (13, "X", "PAP", "", "enquiry in the pupil's own region"),
        (14, "F", "TBL MAT", "", "shared with Maths Lesson 1 (Egyptian numerals)"),
        (15, "F", "TBL MAT", "", "gods and their roles"),
        (16, "A", "ORD MCQ", "", ""),
        (17, "A", "MCQ LBL", "m:Nile valley", ""),
        (18, "A", "MCQ", "", ""),
        (19, "A", "MCQ LBL", "m:Ancient Greece", ""),
        (20, "F", "TBL MAT", "", "person ↔ contribution; Olympic games"),
        (21, "A", "MCQ", "", ""),
        (22, "F", "TBL MAT", "", "inventions"),
        (23, "F", "TBL MAT", "", "shared with Maths Lessons 1 and 3 (Hindu-Arabic numerals, zero)"),
        (24, "A", "MCQ", "", "sensitive (religion): see Risks"),
        (25, "A", "MCQ ORD", "m:Africa (shared)", ""),
        (26, "A", "MCQ", "", "sensitive (religion)"),
        (27, "A", "MCQ ORD", "m:Africa (shared)", ""),
        (28, "F", "TBL MAT", "", "sensitive (religion)"),
    ],
    summary=(
        "Almost all authored facts. Only dating (BC/AD, centuries) is computed, and a single authored "
        "timeline table could drive ordering questions across all lessons. Nine 'further study' and four "
        "'guided work' rows are on the sheet; most can be short authored lessons, and the local enquiries "
        "are paper-only. Several rows touch religion and identity."
    ),
    offline="All rows work offline. No audio. Rows 2, 3 (enquiry part) and 13 are local enquiries, paper-only.",
    gaps=(
        "- **Dates library**: BC/AD arithmetic with no year 0, year → century, ordering mixed BC/AD dates.\n"
        "- **Timeline**: one authored table of dated events; ordering and 'which came first' questions "
        "computed from it across the whole subject.\n"
        "- **Drawn maps** (Africa, Nile valley, Ancient Greece), simplified.\n"
        "- **Matching**, **sort into groups**, **fact-table templates**, **paper-only flow**."
    ),
    conventions=[
        "BC/AD or BCE/CE in wording (and 'about' for estimated dates).",
        "One source per estimated date (fossils, Neolithic sites), recorded in sources.json.",
    ],
    reviewer="a History teacher; rows 6, 10 and 24–28 ideally also a second reader for neutrality.",
    risks=(
        "- **Religion (rows 6, 24–28):** describe beliefs neutrally ('Christians believe…'); questions must "
        "test facts about history, not belief.\n"
        "- **Row 10 'The pygmies in Cameroon':** the sheet's word is considered offensive by some; use the "
        "peoples' own names (Baka, Bagyeli, Bakola, Bedzang) and keep the sheet title only as a reference. "
        "Needs a teacher's decision.\n"
        "- **Estimated dates** differ between sources; a wrong 'exact' date is a P1 error. Prefer 'about' and "
        "ranges.\n"
        "- **Overlaps:** Egyptian and Indian numerals (Maths Lessons 1 and 3): reuse the reviewed wording "
        "(TR-D01)."
    ),
)

# ------------------------------------------------------------------------------------------------ Home economics
SUBJECTS["home-economics"] = dict(
    rows=[
        (1, "F", "TBL MAT", "", "term ↔ definition"),
        (2, "A", "MCQ", "", ""),
        (3, "F", "TBL MAT(sort)", "", "shared with Biology row 42"),
        (4, "F", "TBL MAT", "", ""),
        (5, "F", "TBL MAT", "", ""),
        (6, "A", "LBL", "d:traditional kitchen", ""),
        (7, "F", "TBL MAT", "d:fireplaces", "three-stone, improved stoves …"),
        (10, "A", "LBL", "d:fireplaces (shared)", ""),
        (11, "F", "TBL MAT(sort)", "", ""),
        (12, "A", "MCQ", "", ""),
        (13, "A", "MCQ", "d:work triangle", "work-triangle lengths could be computed"),
        (14, "F", "TBL LBL", "d:kitchen plans", "L, U, galley, island, single-wall"),
        (15, "F", "LBL", "d:kitchen units", ""),
        (16, "F", "TBL MAT(sort)", "", "base, wall, tall units"),
        (17, "A", "MCQ", "", ""),
        (20, "A", "MCQ", "", ""),
        (21, "A", "MCQ", "", ""),
        (22, "F", "TBL MAT", "d:small equipment", ""),
        (23, "A", "LBL", "d:small equipment (shared)", ""),
        (24, "A", "MCQ", "", ""),
        (25, "A", "MCQ", "", ""),
        (26, "F", "TBL MAT", "d:large equipment", ""),
        (27, "A", "MCQ", "", ""),
        (28, "A", "MCQ", "", ""),
        (31, "F", "TBL MAT", "d:labour-saving equipment", ""),
        (32, "F", "TBL MAT", "", "device ↔ principle (shared with Physics row 25)"),
        (33, "A", "MCQ", "", ""),
        (34, "A", "MCQ", "", ""),
        (35, "F", "TBL MAT(sort)", "", ""),
        (36, "F", "TBL MAT", "", ""),
        (37, "A", "MCQ", "", ""),
        (38, "A", "MCQ ORD", "", "first aid: P1 safety (see Risks)"),
        (39, "F", "TBL MAT LBL", "d:first-aid kit", "P1 safety"),
        (42, "F", "TBL MAT(sort)", "", "waste sorting (shared with Geography row 16)"),
        (43, "F", "TBL MAT(sort)", "", ""),
        (44, "F", "TBL MAT(sort)", "", ""),
        (45, "F", "TBL LBL", "g:stitch patterns", "stitches drawn by code; doing them is cloth work"),
        (46, "F", "TBL LBL", "g:stitch patterns (shared)", ""),
        (47, "F", "TBL MAT(sort)", "", "natural vs synthetic fibres"),
        (50, "F", "TBL LBL", "d:embroidery designs", ""),
        (51, "F", "TBL LBL", "d:embroidery designs (shared)", ""),
        (52, "F", "TBL LBL MAT", "d:care-label symbols", "draw our own symbols"),
        (53, "F", "TBL MAT LBL", "d:embroidery tools", ""),
        (54, "A", "MCQ", "", ""),
        (55, "F", "TBL MAT", "", ""),
        (56, "F", "TBL MAT", "d:irons", ""),
        (57, "A", "ORD MCQ TBL", "", "iron temperature by fabric is a table (shared with rows 47, 52)"),
    ],
    summary=(
        "Nothing is computed, but most rows are naming, sorting and labelling, so fact tables cover them well. "
        "It is the most picture-heavy subject: kitchens, equipment, stitches, care symbols. 'Care of …' and "
        "'points to consider when choosing …' rows are short authored lists."
    ),
    offline="All rows work offline. No audio. Stitching and ironing are practical skills: the app can name "
            "and recognise them, not teach the hand skill.",
    gaps=(
        "- **Labelling** at scale (about 13 drawn diagrams).\n"
        "- **Stitch renderer**: running, back, satin, zigzag, buttonhole stitches drawn by code (small, and "
        "shows each stitch step by step).\n"
        "- **Matching**, **sort into groups**, **fact-table templates**.\n"
        "- **Picture choices in MCQ** (options that are images, not words): also useful in Biology and Physics."
    ),
    conventions=[
        "Kitchen work triangle: the recommended total length, if taught.",
        "Ironing temperatures by fabric (cool / warm / hot dots) as on care labels.",
    ],
    reviewer="a Home Economics teacher; rows 38–39 (first aid) also a first-aid trainer or health worker.",
    risks=(
        "- **First aid (rows 38–39) is the highest-stakes content in this audit.** Common home remedies for "
        "burns (oil, toothpaste, raw egg) are harmful; the app must say 'cool under clean running water' "
        "and 'get an adult'. Check against current Red Cross guidance.\n"
        "- **Care-label symbols** are a registered trademark in some countries: draw our own, close to the "
        "standard shapes, for teaching only.\n"
        "- **Spine oddity, not a fix:** rows 40–41 sit under 'First aid' but assess 'Labour-saving equipment', "
        "as on the sheet.\n"
        "- **Overlaps:** food classes (Biology), heat transfer (Physics), waste (Geography)."
    ),
)

SUMMARY_TAIL = """**Reading the P1 ranking.** English and French look light per row only because 33 English rows and 6 French rows are paper-only or deferred, and those count little or nothing for now. In absolute terms they are the two heaviest subjects. Across all 9 subjects the estimate is roughly 2,100 P1 items, against 24 for Maths Lessons 0–16: most of the new work is facts that a person must check, not answers code can compute.

## Engine gaps across subjects

| Gap | What it is | Needed by | Size of work |
|---|---|---|---|
| Matching, sort into groups | Pair items, or sort them into 2–4 groups; tap-tap at 360px, no drag | all 9 | small |
| Fact-table templates | Questions drawn from an authored table; distractors from other rows (extends `pool`) | all 9 | small–medium |
| Labelling | SVG with numbered pins; pick a name for each pin | all 9 | medium |
| Cloze | Typed word in a gap; accepted answers; case, apostrophe and accent policy | English, French, some sciences | small |
| Paper-only flow | Task, model answer, checklist; not counted toward mastery; listed for a grown-up | 8 | small (needs a Phase 3 spec decision) |
| Units library | Mass, volume, time, temperature, SI prefixes (today `convert` is length only) | Chemistry, Physics | small |
| Instrument renderers | Code-drawn ruler, balance, cylinder, thermometers, pH scale, pie chart, with computed readings | Chemistry, Physics, Biology | medium |
| Geography library | Local time, latitude/longitude, grid references, scale; code-drawn grid map and climograph | Geography | medium |
| Dates library + timeline | BC/AD without year 0, centuries, ordering from an authored date table | History | small |
| English morphology | -s, -ing, -ed, plurals, comparatives, contractions, question tags, a/an + exception tables | English | medium |
| French morphology | Conjugation, agreement, elision, numbers in words + exception tables; French UI strings | French | medium–large |
| Reading passage type | One passage, several questions | English, French | small (the passages are the big job) |
| Mini interpreter, spreadsheet, folder tree, URL parser | Reuse `expr.js` | Computer Science | medium |
| Picture options in MCQ | Choices that are images | Home Economics, Biology, Physics | small |
| Audio | Playback of recorded sounds | English (13 rows), French (3 rows + parts) | small code, large size: deferred |
| Block editor | Drag-free block programming | Computer Science (1 row) | large: deferred or paper |

## Shared assets and content (write once)

- Lab equipment set: Biology 6, Chemistry 3–4, Physics 5.
- Hazard symbols: Chemistry 5, Physics 19.
- Particle diagrams and change-of-state table: Chemistry 11, Physics 11–12.
- Water sources, pollution, water cycle: Biology 49–50, Chemistry 49–50 and 56, Geography 20.
- Food classes: Biology 42, Home Economics 3.
- Climate change: Physics 36, Geography 21, English 86.
- Waste sorting: Geography 16, Home Economics 42–43.
- Egyptian and Hindu-Arabic numerals: History 14 and 23, Maths Lessons 1 and 3.
- Computer parts: Computer Science 21, French 75.

## Decisions needed (for Dion)

1. **Audio:** an optional audio pack downloaded once, or speech and listening rows done with a grown-up from a printed list? (English 13 rows, French 3+.)
2. **Paper-only work** (writing, speaking, practicals, field work): shown in the app with a model answer and checklist and listed in the parent summary, but not counted toward mastery?
3. **Sensitive content** (Biology 37–41; History 6, 10, 24–28): parent preview before it unlocks?
4. **Block programming** (Computer Science 35): build a tiny block editor, or keep it on paper?
5. **Order of subjects:** the rankings suggest Physics and Chemistry next (computable measurement block, fact tables, low asset cost), then Geography (computable, but maps). English and French have the largest computed grammar share but also the heaviest authoring (original reading texts) and the audio question. This is a judgement, not a measured result.

Nothing here changes content: no lesson has been written for these subjects. Still in force: no new content until the Lesson 3 test results come back.
"""
