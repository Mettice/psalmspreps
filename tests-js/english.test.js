// English engine tests (decision 2026-10-06, tests before content): word-form rules on known answers,
// the new question types (cloze, word order, matching), paper tasks and deferred lessons.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as maths from "../src/engine/lib/maths.js";
import * as english from "../src/engine/lib/english.js";
import { instantiate, check, normaliseText, normaliseInput, inputModeFor, DONT_KNOW, ContentError } from "../src/engine/template.js";
import { lessonSteps, startTeach, nextPhase, isDone, renderPaper, isDeferred, isAutoMarked } from "../src/engine/teach.js";
import { emptyState, applyChecklist, checklistLessons } from "../src/engine/state.js";

const lib = { ...maths, ...english };

// ---------------------------------------------------------------- word forms (known answers, TR-E02..E06)
test("third person singular: -s, -es, -ies, has", () => {
  const known = { play: "plays", go: "goes", do: "does", wash: "washes", watch: "watches", fix: "fixes", buzz: "buzzes", miss: "misses",
    carry: "carries", study: "studies", fly: "flies", buy: "buys", have: "has", sell: "sells", cook: "cooks", sweep: "sweeps" };
  for (const [v, f] of Object.entries(known)) assert.equal(english.thirdPerson(v), f, v);
});

test("-ing forms: drop e, double the last consonant, ie → y (British travelling)", () => {
  const known = { make: "making", write: "writing", come: "coming", have: "having", see: "seeing", be: "being", lie: "lying", die: "dying",
    tie: "tying", run: "running", sit: "sitting", swim: "swimming", stop: "stopping", shop: "shopping", plan: "planning", get: "getting",
    begin: "beginning", forget: "forgetting", travel: "travelling", visit: "visiting", open: "opening", listen: "listening",
    play: "playing", fix: "fixing", read: "reading", cook: "cooking", sweep: "sweeping", wait: "waiting", start: "starting", cry: "crying",
    study: "studying", argue: "arguing", dance: "dancing", ride: "riding", chat: "chatting", jog: "jogging", rain: "raining" };
  for (const [v, f] of Object.entries(known)) assert.equal(english.ing(v), f, v);
});

test("simple past: regular spelling rules and the irregular table", () => {
  const regular = { like: "liked", dance: "danced", carry: "carried", study: "studied", cry: "cried", play: "played", stay: "stayed",
    stop: "stopped", plan: "planned", chat: "chatted", travel: "travelled", visit: "visited", open: "opened", listen: "listened",
    wash: "washed", cook: "cooked", clean: "cleaned", start: "started", want: "wanted", need: "needed", arrive: "arrived", agree: "agreed",
    jog: "jogged", rob: "robbed", fix: "fixed", answer: "answered", happen: "happened", prefer: "preferred" };
  for (const [v, f] of Object.entries(regular)) {
    assert.equal(english.past(v), f, v);
    assert.equal(english.participle(v), f, `${v} participle`);
  }
  const irregular = { go: ["went", "gone"], eat: ["ate", "eaten"], buy: ["bought", "bought"], see: ["saw", "seen"], write: ["wrote", "written"],
    take: ["took", "taken"], come: ["came", "come"], run: ["ran", "run"], sell: ["sold", "sold"], swim: ["swam", "swum"], pay: ["paid", "paid"], sweep: ["swept", "swept"] };
  for (const [v, [p, pp]] of Object.entries(irregular)) {
    assert.equal(english.past(v), p, v);
    assert.equal(english.participle(v), pp, `${v} participle`);
  }
  // the regular rule alone would give the wrong past for every irregular verb except those whose past ends in -ed by accident
  for (const v of Object.keys(english.IRREGULAR)) assert.notEqual(english.regularPast(v), english.IRREGULAR[v][0], v);
});

test("subject agreement: am/is/are, do/does, have/has, was/were", () => {
  const I = english.subj("I", 1, false), she = english.subj("Bih", 3, false), they = english.subj("My brothers", 3, true), you = english.subj("you", 2, false);
  assert.deepEqual([I, she, they, you].map(english.beFor), ["am", "is", "are", "are"]);
  assert.deepEqual([I, she, they, you].map(english.doFor), ["do", "does", "do", "do"]);
  assert.deepEqual([I, she, they, you].map(english.haveFor), ["have", "has", "have", "have"]);
  assert.deepEqual([I, she, they, you].map(english.wasWere), ["was", "was", "were", "were"]);
  assert.deepEqual([I, she, they].map((s) => english.presentFor(s, "go")), ["go", "goes", "go"]);
  assert.deepEqual([I, she, they].map(english.dontFor), ["don't", "doesn't", "don't"]);
});

test("a / an by sound, plurals, ordinal words", () => {
  const art = { orange: "an", egg: "an", umbrella: "an", hour: "an", honest: "an", uniform: "a", university: "a", "one-way": "a",
    European: "a", bag: "a", house: "a", "useful tool": "a", ugly: "an", unhappy: "an", idea: "an" };
  for (const [w, a] of Object.entries(art)) assert.equal(english.article(w), a, w);
  const pl = { box: "boxes", bus: "buses", dress: "dresses", match: "matches", baby: "babies", city: "cities", toy: "toys", day: "days",
    child: "children", man: "men", woman: "women", foot: "feet", knife: "knives", tomato: "tomatoes", mango: "mangoes", radio: "radios",
    photo: "photos", orange: "oranges", sheep: "sheep" };
  for (const [n, p] of Object.entries(pl)) assert.equal(english.plural(n), p, n);
  const ord = { 1: "first", 2: "second", 3: "third", 5: "fifth", 8: "eighth", 9: "ninth", 12: "twelfth", 20: "twentieth", 21: "twenty-first",
    40: "fortieth", 45: "forty-fifth", 100: "one hundredth", 105: "one hundred and fifth", 11: "eleventh", 13: "thirteenth" };
  for (const [n, w] of Object.entries(ord)) assert.equal(english.ordinalWords(maths.words(Number(n))), w, n);
  assert.equal(english.andList(["rice", "oil", "soap"]), "rice, oil and soap");
});

// ---------------------------------------------------------------- cloze
const people = { pick: [{ name: "Bih", s: { text: "Bih", person: 3, plural: false } }, { name: "Ayuk and Tabe", s: { text: "Ayuk and Tabe", person: 3, plural: true } }] };
const typedCloze = {
  id: "t-cloze", type: "cloze", level: 1,
  vars: { p: people, v: { pick: ["go", "wash", "carry"] } },
  prompt: "Write the correct form of the verb in brackets.",
  text: "{p.name} ___ ({v}) to the stream every morning.",
  answer: "presentFor(p.s, v)",
  misconceptions: [{ id: "no-s", wrong: "p.s.plural ? thirdPerson(v) : v", explain: "Check who does the action." }],
};

test("cloze, typed: computed answer; case and extra spaces ignored; misconception found", () => {
  for (let seed = 1; seed <= 200; seed++) {
    const q = instantiate(typedCloze, seed, lib);
    assert.equal(q.mode, "type");
    const third = q.full.startsWith("Bih ");   // one person: he/she form; "Ayuk and Tabe": base form
    assert.ok(["go", "wash", "carry"].some((v) => q.answer === (third ? english.thirdPerson(v) : v)), q.full);
    assert.ok(q.sentence.includes("___") && !q.full.includes("___") && q.full.includes(q.answer));
    assert.deepEqual(check(q, q.answer), { correct: true });
    assert.deepEqual(check(q, `  ${q.answer.toUpperCase()}  `), { correct: true });
    const m = q.misconceptions[0];
    assert.equal(check(q, m.value).correct, false);
    assert.equal(check(q, m.value).misconception.id, "no-s");
    assert.equal(check(q, "xyz").misconception, null);
    assert.ok(q.solution.join(" ").includes(q.answer));
  }
  const q = instantiate(typedCloze, 3, lib);
  assert.equal(inputModeFor(q), "text");
  assert.equal(normaliseInput("  goes   to ", q), "goes to");     // inner spaces kept, outer removed
  assert.equal(normaliseText("Don’t  Go"), "don't go");             // curly apostrophe = straight
  assert.equal(check(q, DONT_KNOW).dontKnow, true);
});

test("cloze, typed: every accepted variant is right; spaces inside words still matter", () => {
  const tpl = { id: "t-acc", type: "cloze", level: 1, vars: {}, prompt: "Fill in.", text: "We waited at the ___ for the Buea bus.",
    answer: "'bus stop'", accept: ["'bus-stop'"] };
  const q = instantiate(tpl, 1, lib);
  for (const ok of ["bus stop", "Bus Stop", " bus  stop ", "bus-stop"]) assert.equal(check(q, ok).correct, true, ok);
  for (const bad of ["busstop", "bus", "stop"]) assert.equal(check(q, bad).correct, false, bad);
});

test("cloze, choose: shown like mcq, exactly one right choice, feedback per wrong choice", () => {
  const tpl = { id: "t-choose", type: "cloze", level: 1, show: 3,
    vars: { p: people }, prompt: "Choose the word that fits.", text: "___ {p.name} like puff-puff?", answer: "cap(doFor(p.s))",
    choices: [{ text: "Do", misconception: "do" }, { text: "Does", misconception: "does" }, { text: "Is", misconception: "be" }],
    misconceptions: [{ id: "do", explain: "Do goes with I, you, we, they." }, { id: "does", explain: "Does goes with he, she, it." }, { id: "be", explain: "Questions with a main verb use do or does." }] };
  const positions = new Set();
  for (let seed = 1; seed <= 200; seed++) {
    const q = instantiate(tpl, seed, lib);
    assert.equal(q.mode, "choose");
    assert.equal(q.options.length, 3);
    assert.equal(new Set(q.options.map((o) => o.text)).size, 3);
    q.options.forEach((o, i) => {
      const r = check(q, i);
      assert.equal(r.correct, i === q.correctIndex);
      if (!r.correct) assert.ok(r.misconception.explain);
    });
    positions.add(q.correctIndex);
  }
  assert.ok(positions.size > 1);
});

test("cloze: a text without exactly one blank is a content error", () => {
  assert.throws(() => instantiate({ id: "t-b", type: "cloze", level: 1, vars: {}, prompt: "x", text: "No blank here.", answer: "'a'" }, 1, lib), ContentError);
  assert.throws(() => instantiate({ id: "t-b2", type: "cloze", level: 1, vars: {}, prompt: "x", text: "___ and ___", answer: "'a'" }, 1, lib), ContentError);
});

// ---------------------------------------------------------------- word order
test("word order: shuffled, never shown in a correct order, every accepted order is right", () => {
  const tpl = { id: "t-wo", type: "word_order", level: 2, vars: { p: people },
    prompt: "Tap the words to make a question.", answer: "Does Bih sell oranges at Kumba market?",
    accept: ["Does Bih sell oranges at Kumba market?"] };
  for (let seed = 1; seed <= 300; seed++) {
    const q = instantiate(tpl, seed, lib);
    assert.notEqual(q.items.join(" "), q.answer);
    assert.equal(check(q, q.correctOrder).correct, true);
    assert.equal(check(q, q.items.map((_, i) => i)).correct, false);
    assert.equal(check(q, q.correctOrder.slice(1)).correct, false);          // a word left out
    assert.equal(check(q, [q.correctOrder[0], ...q.correctOrder.slice(0, -1)]).correct, false);  // a word used twice
  }
  const two = { id: "t-wo2", type: "word_order", level: 2, vars: {}, prompt: "Make a sentence.", answer: "Every day Mih sweeps the yard.",
    accept: ["Mih sweeps the yard every day."] };
  const q = instantiate(two, 5, lib);
  // both orders are right (the capital letter on "Every"/"every" does not matter)
  const pick = (sentence) => { const used = new Set(); return sentence.replace(/[.?!]$/, "").split(" ").map((w) => { const i = q.items.findIndex((x, k) => !used.has(k) && x.toLowerCase() === w.toLowerCase()); used.add(i); return i; }); };
  assert.equal(check(q, pick("Every day Mih sweeps the yard.")).correct, true);
  assert.equal(check(q, pick("Mih sweeps the yard every day.")).correct, true);
  assert.throws(() => instantiate({ id: "t-wo3", type: "word_order", level: 1, vars: {}, prompt: "x", answer: "I go.", accept: ["I come."] }, 1, lib), ContentError);
});

// ---------------------------------------------------------------- matching
test("matching: pairs drawn from the pool, rights shuffled, all must be right", () => {
  const tpl = { id: "t-match", type: "matching", level: 1, prompt: "Match each verb with its past form.", pick: 4,
    pool: Object.keys(english.IRREGULAR).filter((v) => v !== "be").map((v) => ({ left: v, right: `{past('${v}')}` })) };
  for (let seed = 1; seed <= 200; seed++) {
    const q = instantiate(tpl, seed, lib);
    assert.equal(q.left.length, 4);
    assert.equal(new Set(q.right).size, 4);
    assert.ok(q.left.every((l, i) => english.past(l) === q.right[q.correctMatch[i]]));
    assert.deepEqual(check(q, q.correctMatch), { correct: true });
    const swapped = [...q.correctMatch];
    [swapped[0], swapped[1]] = [swapped[1], swapped[0]];
    assert.deepEqual(check(q, swapped), { correct: false, wrongPairs: [0, 1] });
    assert.equal(q.solution.length, 5);
  }
});

test("matching with groups (sort): several items share a group; group order can be fixed", () => {
  const tpl = { id: "t-sort", type: "matching", level: 1, groups: true, group_order: ["countable", "uncountable"], pick: 4,
    prompt: "Sort the nouns.", pool: [
      { left: "orange", right: "countable" }, { left: "egg", right: "countable" }, { left: "bucket", right: "countable" },
      { left: "rice", right: "uncountable" }, { left: "water", right: "uncountable" }, { left: "salt", right: "uncountable" }] };
  for (let seed = 1; seed <= 200; seed++) {
    const q = instantiate(tpl, seed, lib);
    assert.deepEqual(q.right, ["countable", "uncountable"]);
    assert.deepEqual(check(q, q.correctMatch), { correct: true });
    assert.equal(check(q, q.correctMatch.map((r) => 1 - r)).correct, false);
  }
});

// ---------------------------------------------------------------- paper tasks and deferred lessons
const card = (id) => ({ id, status: "draft", idea: "An idea.", vars: {}, example: ["An example."], checks: [],
  check: { id: `${id}-check`, type: "cloze", level: 1, vars: {}, prompt: "Fill in.", text: "I ___ a pupil.", answer: "'am'" } });
const paperLesson = {
  lesson_no: 9, teach: { cards: [card("p1"), card("p2"), card("p3")] }, questions: [],
  worked_example: { status: "draft", vars: {}, problem: "p", steps: ["s"], answer: "a" },
  paper_task: { status: "draft", vars: { money: 5000, rice: 1500 }, prompt: "You have {money} FCFA. Write a shopping list.",
    model: ["Rice: {rice} FCFA", "Left over: {money - rice} FCFA"], checklist: ["I wrote a price for each item.", "My total is not more than {money} FCFA."],
    checks: ["rice < money"] },
  note: { status: "draft", text: "n", checks: [] },
};

test("paper task: cards → worked example → paper → note; no practice; numbers computed", () => {
  assert.deepEqual(lessonSteps(paperLesson).map((s) => s.kind), ["card", "card", "card", "worked_example", "paper", "note"]);
  const p = renderPaper(paperLesson, lib);
  assert.equal(p.prompt, "You have 5000 FCFA. Write a shopping list.");
  assert.deepEqual(p.model, ["Rice: 1500 FCFA", "Left over: 3500 FCFA"]);
  assert.deepEqual(p.failedChecks, []);
  assert.equal(isAutoMarked(paperLesson), false);   // mastery stays unknown
  let f = startTeach(paperLesson, 1);
  f = { ...f, step: 4, phase: "read" };              // the paper step reads, then moves on with no answer
  f = nextPhase(f);
  assert.equal(f.steps[f.step].kind, "note");
  assert.ok(isDone(nextPhase(f)));
});

test("deferred lessons: no steps, not auto-marked, never in the coverage checklist", () => {
  const deferred = { lesson_no: 4, status: "deferred", deferred_reason: "speech work needs audio" };
  assert.equal(isDeferred(deferred), true);
  assert.equal(isAutoMarked(deferred), false);
  assert.throws(() => lessonSteps(deferred), /deferred/);
  assert.deepEqual(checklistLessons([{ lesson_no: 3 }, deferred, { lesson_no: 5 }]), [3, 5]);
  const s = applyChecklist(emptyState(), { 3: true, 4: true, 5: false }, [4]);
  assert.deepEqual(s.coverage, { 3: "taught", 5: "not_taught" });
  assert.equal(s.coverage[4], undefined);
});
