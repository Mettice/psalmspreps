// French helpers for templates: nouns with their gender, articles and possessives (with elision before a vowel or a
// silent h), subject pronouns, present-tense conjugation of the Form 1 verbs, numbers in words and alphabetical order.
// Used as {...maths, …, ...computerscience, ...french}. All names start with "fr" so they never clash with the
// English library (articles, plurals and numbers exist there too).
// Conventions to be checked by a French teacher (docs/teacher-review.md, TR-F*): traditional spelling of numbers
// (vingt et un, quatre-vingts); h aspiré nouns (le haricot, le hibou) take le/la, not l'.

// ---------------------------------------------------------------- nouns (authored, TR-F)
// [noun, gender "m" | "f", plural, starts with a vowel or a silent h (elision: l', mon amie)]
const NOUNS = [
  ["livre", "m", "livres"], ["cahier", "m", "cahiers"], ["stylo", "m", "stylos"], ["sac", "m", "sacs"], ["tableau", "m", "tableaux"], ["crayon", "m", "crayons"],
  ["table", "f", "tables"], ["chaise", "f", "chaises"], ["règle", "f", "règles"], ["maison", "f", "maisons"], ["porte", "f", "portes"], ["mangue", "f", "mangues"],
  ["école", "f", "écoles", true], ["amie", "f", "amies", true], ["orange", "f", "oranges", true], ["arbre", "m", "arbres", true], ["ami", "m", "amis", true],
  ["enfant", "m", "enfants", true], ["oiseau", "m", "oiseaux", true], ["homme", "m", "hommes", true], ["haricot", "m", "haricots"], ["hibou", "m", "hiboux"],
];
export const frNounCount = () => NOUNS.length;
export const frNoun = (i) => NOUNS[i][0];
export const frPlural = (i) => NOUNS[i][2];
export const frGender = (i) => (NOUNS[i][1] === "m" ? "masculin" : "féminin");
export const frVowel = (i) => !!NOUNS[i][3];
/** Definite article with its noun: le livre, la table, l'école, les livres. */
export function frDef(i, plural = false) {
  if (plural) return `les ${NOUNS[i][2]}`;
  return frVowel(i) ? `l’${NOUNS[i][0]}` : `${NOUNS[i][1] === "m" ? "le" : "la"} ${NOUNS[i][0]}`;
}
/** Indefinite article with its noun: un livre, une table, des livres. */
export const frIndef = (i, plural = false) => (plural ? `des ${NOUNS[i][2]}` : `${NOUNS[i][1] === "m" ? "un" : "une"} ${NOUNS[i][0]}`);
/** The article alone: "le", "la", "l’", "les", "un", "une", "des". */
export const frDefArticle = (i, plural = false) => (plural ? "les" : frVowel(i) ? "l’" : NOUNS[i][1] === "m" ? "le" : "la");
export const frIndefArticle = (i, plural = false) => (plural ? "des" : NOUNS[i][1] === "m" ? "un" : "une");

// ---------------------------------------------------------------- possessives
// person 0–5: je, tu, il/elle, nous, vous, ils/elles
const POSS = [["mon", "ma", "mes"], ["ton", "ta", "tes"], ["son", "sa", "ses"], ["notre", "notre", "nos"], ["votre", "votre", "vos"], ["leur", "leur", "leurs"]];
/** Possessive with its noun: mon livre, ma table, mon école (feminine before a vowel), mes livres. */
export function frPoss(person, i, plural = false) {
  const [m, f, pl] = POSS[person];
  if (plural) return `${pl} ${NOUNS[i][2]}`;
  return `${NOUNS[i][1] === "m" || frVowel(i) ? m : f} ${NOUNS[i][0]}`;
}
/** The possessive word alone. */
export const frPossWord = (person, i, plural = false) => frPoss(person, i, plural).split(" ")[0];
/** The owner in words, for prompts: "à moi", "à toi", "à lui ou à elle", … */
export const frOwner = (person) => ["à moi", "à toi", "à lui (ou à elle)", "à nous", "à vous", "à eux (ou à elles)"][person];

// ---------------------------------------------------------------- pronouns and conjugation
export const FR_PRONOUNS = ["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"];
export const frPronoun = (p) => FR_PRONOUNS[p];
// pronoun index 0–7 → grammatical person 0–5
const PERSON = [0, 1, 2, 2, 3, 4, 5, 5];
const IRREGULAR = {
  avoir: ["ai", "as", "a", "avons", "avez", "ont"],
  "s’appeler": ["m’appelle", "t’appelles", "s’appelle", "nous appelons", "vous appelez", "s’appellent"],
};
const ER = ["e", "es", "e", "ons", "ez", "ent"];
/** The verb form alone (with its reflexive pronoun): frForm('laver', 4) = "lavons". */
export function frForm(verb, p) {
  const k = PERSON[p];
  if (IRREGULAR[verb]) return IRREGULAR[verb][k];
  if (!verb.endsWith("er")) throw new RangeError(`frForm: ${verb} is not in the Form 1 table`);
  return verb.slice(0, -2) + ER[k];
}
/** Pronoun and verb, with elision: "j’ai", "je travaille", "je m’appelle", "nous lavons". */
export function frConj(verb, p) {
  const form = frForm(verb, p);
  return p === 0 && /^[aeiouyéèêh]/.test(form) ? `j’${form}` : `${FR_PRONOUNS[p]} ${form}`;
}
/** The usual pupil mistake for -er verbs: the ending -e everywhere (for feedback only). */
export const frWrongEnding = (verb, p) => (IRREGULAR[verb] ? frForm(verb, (PERSON[p] + 1) % 6) : `${verb.slice(0, -2)}e`);

// ---------------------------------------------------------------- numbers in words (traditional spelling, TR-F)
const UNITS = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"];
const TENS = { 2: "vingt", 3: "trente", 4: "quarante", 5: "cinquante", 6: "soixante" };
/** 0 to 100 in words: 21 → "vingt et un", 71 → "soixante et onze", 80 → "quatre-vingts", 91 → "quatre-vingt-onze". */
export function frNumber(n) {
  if (!Number.isInteger(n) || n < 0 || n > 100) throw new RangeError(`frNumber: ${n}`);
  if (n <= 16) return UNITS[n];
  if (n < 20) return `dix-${UNITS[n - 10]}`;
  if (n === 100) return "cent";
  if (n < 70) {
    const t = Math.floor(n / 10), u = n % 10;
    return u === 0 ? TENS[t] : u === 1 ? `${TENS[t]} et un` : `${TENS[t]}-${UNITS[u]}`;
  }
  if (n < 80) return n === 71 ? "soixante et onze" : `soixante-${frNumber(n - 60)}`;
  if (n === 80) return "quatre-vingts";
  return `quatre-vingt-${frNumber(n - 80)}`;
}
/** The same number in the 1990 spelling (hyphens everywhere): accepted as well when typed. */
export const frNumber1990 = (n) => frNumber(n).replace(/ et /g, "-et-").replace(/ /g, "-");

// ---------------------------------------------------------------- alphabet and alphabetical order
export const FR_VOWELS = ["a", "e", "i", "o", "u", "y"];
export const frIsVowel = (c) => FR_VOWELS.includes(String(c).toLowerCase());
export const frLetter = (k) => "abcdefghijklmnopqrstuvwxyz"[k];
/** Accents are ignored when ordering words alphabetically (école comes with the e). */
const plain = (w) => String(w).normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
/** Rank (0-based) of a word among the words of a list, in alphabetical order. */
export const frAlphaRank = (w, list) => [...list].sort((a, b) => plain(a).localeCompare(plain(b))).indexOf(w);

// ---------------------------------------------------------------- typical mistakes (for wrong options and feedback only)
/** Starts with h (silent or aspiré): l’homme but le haricot. */
export const frStartsH = (i) => NOUNS[i][0].startsWith("h");
/** "vingt-un" instead of "vingt et un". */
export const frNumberNoEt = (n) => frNumber(n).replace(" et ", "-");
/** "dix sept" instead of "dix-sept": hyphens left out. */
export const frNumberSpaces = (n) => frNumber(n).replace(/-/g, " ");
/** The ending of a regular -er verb for pronoun p: e, es, e, e, ons, ez, ent, ent. */
export const frEnding = (p) => ER[PERSON[p]];
/** "ma école" instead of "mon école". */
export const frPossWrongVowel = (person, i) => `${POSS[person][1]} ${NOUNS[i][0]}`;
/** Feminine noun? */
export const frFeminine = (i) => NOUNS[i][1] === "f";
