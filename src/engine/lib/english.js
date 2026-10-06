// English word forms for templates. Rules plus authored exception tables; the tables are facts a teacher
// must check (docs/teacher-review.md, TR-E*), the rules are tested on known answers (tests-js/english.test.js).
// British spelling (travelled, cancelled), as in Cameroonian schools.

const VOWELS = "aeiou";
const isVowel = (c) => VOWELS.includes(c);

// ---------------------------------------------------------------- irregular verbs (authored, TR-E03)
// base: [simple past, past participle]. Only verbs used in Form 1 lessons; British forms first.
export const IRREGULAR = {
  be: ["was/were", "been"], become: ["became", "become"], begin: ["began", "begun"], break: ["broke", "broken"],
  bring: ["brought", "brought"], build: ["built", "built"], buy: ["bought", "bought"], catch: ["caught", "caught"],
  choose: ["chose", "chosen"], come: ["came", "come"], cost: ["cost", "cost"], cut: ["cut", "cut"], do: ["did", "done"],
  draw: ["drew", "drawn"], drink: ["drank", "drunk"], drive: ["drove", "driven"], eat: ["ate", "eaten"], fall: ["fell", "fallen"],
  feel: ["felt", "felt"], find: ["found", "found"], fly: ["flew", "flown"], forget: ["forgot", "forgotten"], get: ["got", "got"],
  give: ["gave", "given"], go: ["went", "gone"], grow: ["grew", "grown"], have: ["had", "had"], hear: ["heard", "heard"],
  keep: ["kept", "kept"], know: ["knew", "known"], leave: ["left", "left"], lend: ["lent", "lent"], lose: ["lost", "lost"],
  make: ["made", "made"], meet: ["met", "met"], pay: ["paid", "paid"], put: ["put", "put"], read: ["read", "read"],
  ride: ["rode", "ridden"], ring: ["rang", "rung"], run: ["ran", "run"], say: ["said", "said"], see: ["saw", "seen"],
  sell: ["sold", "sold"], send: ["sent", "sent"], sing: ["sang", "sung"], sit: ["sat", "sat"], sleep: ["slept", "slept"],
  speak: ["spoke", "spoken"], spend: ["spent", "spent"], stand: ["stood", "stood"], sweep: ["swept", "swept"], swim: ["swam", "swum"], take: ["took", "taken"],
  teach: ["taught", "taught"], tell: ["told", "told"], think: ["thought", "thought"], throw: ["threw", "thrown"],
  understand: ["understood", "understood"], wake: ["woke", "woken"], wear: ["wore", "worn"], win: ["won", "won"], write: ["wrote", "written"],
};
export const isIrregular = (v) => Object.prototype.hasOwnProperty.call(IRREGULAR, v);

// Two-syllable verbs stressed on the last syllable double the final consonant (British, TR-E04);
// British English also doubles a final -l after one vowel (travel → travelled).
const DOUBLE_LONG = new Set(["admit", "begin", "commit", "control", "forget", "occur", "permit", "prefer", "refer", "regret", "submit", "upset"]);
const NO_DOUBLE = new Set(["visit", "open", "listen", "happen", "enter", "answer", "offer", "order", "wonder", "remember", "cover", "suffer", "garden", "market"]);

/** True when a final consonant is doubled before -ed / -ing: stop → stopped, run → running, travel → travelled. */
export function doublesFinal(v) {
  if (DOUBLE_LONG.has(v)) return true;
  if (NO_DOUBLE.has(v) || v.length < 3) return false;
  const [a, b, c] = v.slice(-3);
  if (isVowel(c) || "wxy".includes(c) || !isVowel(b) || isVowel(a)) return false;
  const vowelGroups = (v.match(/[aeiou]+/g) || []).length;
  if (vowelGroups === 1) return true;            // one syllable, consonant-vowel-consonant
  return c === "l";                                // British: travel → travelled, cancel → cancelled
}

/** he/she/it form of the Simple Present: go → goes, carry → carries, wash → washes, have → has. */
export function thirdPerson(v) {
  if (v === "have") return "has";
  if (v === "be") return "is";
  if (/(s|sh|ch|x|z|o)$/.test(v)) return v + "es";
  if (/[^aeiou]y$/.test(v)) return v.slice(0, -1) + "ies";
  return v + "s";
}

/** -ing form: make → making, run → running, lie → lying, see → seeing, travel → travelling. */
export function ing(v) {
  if (v === "be") return "being";
  if (/ie$/.test(v)) return v.slice(0, -2) + "ying";
  if (/[^aeiouy]e$/.test(v) || v.endsWith("ue")) return v.slice(0, -1) + "ing";
  if (doublesFinal(v)) return v + v.slice(-1) + "ing";
  return v + "ing";
}

/** Regular simple past by the spelling rules, ignoring the irregular table: like → liked, carry → carried, stop → stopped. */
export function regularPast(v) {
  if (v.endsWith("e")) return v + "d";
  if (/[^aeiou]y$/.test(v)) return v.slice(0, -1) + "ied";
  if (doublesFinal(v)) return v + v.slice(-1) + "ed";
  return v + "ed";
}

/** Simple past: the irregular table first, then the rules. "be" gives "was/were"; use wasWere() for one form. */
export const past = (v) => (isIrregular(v) ? IRREGULAR[v][0] : regularPast(v));
/** Past participle (for the Present Perfect). */
export const participle = (v) => (isIrregular(v) ? IRREGULAR[v][1] : regularPast(v));

// ---------------------------------------------------------------- subjects and auxiliaries
// A subject is {text, person: 1|2|3, plural: bool}. Built in templates with subj(text, person, plural).
export const subj = (text, person, plural) => ({ text, person, plural });
const isThirdSingular = (s) => s.person === 3 && !s.plural;

/** Simple Present affirmative verb form for a subject. */
export const presentFor = (s, v) => (v === "be" ? beFor(s) : isThirdSingular(s) ? thirdPerson(v) : v);
/** am / is / are. */
export const beFor = (s) => (s.person === 1 && !s.plural ? "am" : isThirdSingular(s) ? "is" : "are");
/** was / were. */
export const wasWere = (s) => ((s.person === 1 || s.person === 3) && !s.plural ? "was" : "were");
/** do / does. */
export const doFor = (s) => (isThirdSingular(s) ? "does" : "do");
/** have / has. */
export const haveFor = (s) => (isThirdSingular(s) ? "has" : "have");
/** don't / doesn't. */
export const dontFor = (s) => (isThirdSingular(s) ? "doesn't" : "don't");

/** Capital first letter (for questions and sentence starts). */
export const cap = (s) => (s ? s[0].toUpperCase() + s.slice(1) : s);
/** Lower-case first letter, except "I" and proper nouns (passed as keep = true). */
export const low = (s, keep = false) => (keep || /^I\b/.test(s) ? s : s[0].toLowerCase() + s.slice(1));

// ---------------------------------------------------------------- articles and nouns
// a/an goes by the first SOUND (TR-E05). Words that start with a vowel letter but a consonant sound, and the reverse:
const AN_EXCEPT = new Set(["hour", "hours", "honest", "honour", "heir"]);
const A_EXCEPT = new Set(["university", "uniform", "unit", "union", "unique", "user", "useful", "usual", "utensil", "european", "one", "once", "ewe"]);
/** "a" or "an" for the word that follows (by its first word). */
export function article(word) {
  const w = String(word).toLowerCase().split(/[\s-]/)[0];
  if (AN_EXCEPT.has(w)) return "an";
  if (A_EXCEPT.has(w)) return "a";
  return isVowel(w[0]) ? "an" : "a";
}
export const withArticle = (word) => `${article(word)} ${word}`;

// Irregular plurals (authored, TR-E06).
export const IRREGULAR_PLURAL = { child: "children", man: "men", woman: "women", foot: "feet", tooth: "teeth", mouse: "mice",
  person: "people", knife: "knives", wife: "wives", leaf: "leaves", loaf: "loaves", life: "lives", shelf: "shelves", half: "halves", sheep: "sheep", fish: "fish" };
/** Plural of a countable noun: box → boxes, baby → babies, child → children, radio → radios, tomato → tomatoes. */
export function plural(n) {
  if (Object.prototype.hasOwnProperty.call(IRREGULAR_PLURAL, n)) return IRREGULAR_PLURAL[n];
  if (/(s|sh|ch|x|z)$/.test(n) || ["tomato", "potato", "mango", "hero", "echo"].includes(n)) return n + "es";
  if (/[^aeiou]y$/.test(n)) return n.slice(0, -1) + "ies";
  return n + "s";
}
/** "1 orange", "3 oranges". */
export const countNoun = (k, n) => `${k} ${k === 1 ? n : plural(n)}`;

// ---------------------------------------------------------------- number words
const ORD_SPECIAL = { one: "first", two: "second", three: "third", five: "fifth", eight: "eighth", nine: "ninth", twelve: "twelfth" };
/** Ordinal in words from cardinal words: "twenty-one" → "twenty-first", "forty" → "fortieth", "a hundred" style not used. */
export function ordinalWords(cardinalWords) {
  const m = /^(.*?)([a-z]+)$/.exec(cardinalWords);
  const [, head, last] = m;
  if (ORD_SPECIAL[last]) return head + ORD_SPECIAL[last];
  if (last.endsWith("y")) return head + last.slice(0, -1) + "ieth";
  return head + last + "th";
}

// ---------------------------------------------------------------- text helpers for templates
/** Joins words with single spaces and fixes spaces before punctuation. */
export const sentence = (...parts) => parts.filter((p) => p !== "" && p != null).join(" ").replace(/\s+([.,?!])/g, "$1");
/** The words of a sentence for word-order questions (punctuation stays on its word). */
export const tokens = (s) => String(s).split(/\s+/).filter(Boolean);
/** Removes the first capital (for "the sentence starts with a capital letter" checks). */
export const lowerAll = (s) => String(s).toLowerCase();
/** Sum of a list of numbers (shopping lists). */
export const sum = (xs) => xs.reduce((a, b) => a + b, 0);
/** Picks the field `key` from every object in a list. */
export const pluck = (xs, key) => xs.map((x) => x[key]);
/** Comma list with "and": ["rice", "oil", "soap"] → "rice, oil and soap". */
export const andList = (xs) => (xs.length < 2 ? xs.join("") : `${xs.slice(0, -1).join(", ")} and ${xs[xs.length - 1]}`);

// ---------------------------------------------------------------- helpers for number words, prices, dates, timetables
/** Replaces the first `a` in s with `b` ("one hundred" → "a hundred"). */
export const replaceFirst = (s, a, b) => String(s).replace(a, b);
/** Number words with the hyphens taken out ("twenty-one" → "twenty one"): a common slip. */
export const noHyphen = (s) => String(s).replace(/-/g, " ");
/** s with every `part` removed ("one hundred and five" without " and" → "one hundred five"). */
export const without = (s, part) => String(s).split(part).join("");
/** Ways a pupil may type a whole number: 1500, 1 500, 1,500 (all accepted, decision TR-C33). */
export function numberVariants(n) {
  const plain = String(n), grouped = plain.replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  return [...new Set([plain, grouped, grouped.replace(/ /g, ",")])];
}
const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
export const monthName = (m) => MONTHS[m - 1];
const pad2 = (n) => String(n).padStart(2, "0");
/** British order day/month/year: 7, 3, 2014 → "07/03/2014". */
export const ddmmyyyy = (d, m, y) => `${pad2(d)}/${pad2(m)}/${y}`;
/** American order month/day/year (a distractor). */
export const mmddyyyy = (d, m, y) => `${pad2(m)}/${pad2(d)}/${y}`;
/** Year first (a distractor). */
export const yyyymmdd = (d, m, y) => `${y}/${pad2(m)}/${pad2(d)}`;
/** A one-day timetable, one line per lesson: "7:30  Mathematics". */
export const timetable = (times, subjects) => times.map((t, i) => `${t}  ${subjects[i]}`).join("\n");
/** Lines joined for display (shopping lists, forms). */
export const lines = (xs) => xs.join("\n");
/** BLOCK LETTERS for forms: "Ebai" → "EBAI". */
export const upperAll = (s) => String(s).toUpperCase();
