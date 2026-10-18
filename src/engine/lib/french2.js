// Form 2 French helpers (French and Français intensif, Term 1): conjugation in the présent (with -ger and -cer verbs),
// passé composé, imparfait, passé simple, participe présent and gérondif; agreement of adjectives (-al, colours) and
// plurals of nouns in -al and -ail. Names start with "fr2" so they never clash with the Form 1 French library.
// The verb table is authored (docs/teacher-review.md, TR-Z01): a French teacher must check it.

const PRON = ["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"];
const PERSON = [0, 1, 2, 2, 3, 4, 5, 5];  // pronoun index 0–7 → person 0–5
export const fr2Pronoun = (p) => PRON[p];
const feminine = (p) => p === 3 || p === 7;
const plural = (p) => p >= 4;

// ---------------------------------------------------------------- the verb table (authored, TR-Z01)
// present: the six forms (je, tu, il, nous, vous, ils); pp: past participle; aux: "avoir" or "être";
// ps: passé simple stem type or the six forms. Regular -er and -ir (2nd group) verbs are built by rule.
const IRR = {
  être: { present: ["suis", "es", "est", "sommes", "êtes", "sont"], pp: "été", aux: "avoir", imp: "ét", ps: ["fus", "fus", "fut", "fûmes", "fûtes", "furent"], ppr: "étant" },
  avoir: { present: ["ai", "as", "a", "avons", "avez", "ont"], pp: "eu", aux: "avoir", ps: ["eus", "eus", "eut", "eûmes", "eûtes", "eurent"], ppr: "ayant" },
  aller: { present: ["vais", "vas", "va", "allons", "allez", "vont"], pp: "allé", aux: "être", ps: "er" },
  faire: { present: ["fais", "fais", "fait", "faisons", "faites", "font"], pp: "fait", aux: "avoir", ps: ["fis", "fis", "fit", "fîmes", "fîtes", "firent"] },
  dire: { present: ["dis", "dis", "dit", "disons", "dites", "disent"], pp: "dit", aux: "avoir", ps: ["dis", "dis", "dit", "dîmes", "dîtes", "dirent"] },
  lire: { present: ["lis", "lis", "lit", "lisons", "lisez", "lisent"], pp: "lu", aux: "avoir", ps: ["lus", "lus", "lut", "lûmes", "lûtes", "lurent"] },
  écrire: { present: ["écris", "écris", "écrit", "écrivons", "écrivez", "écrivent"], pp: "écrit", aux: "avoir", ps: ["écrivis", "écrivis", "écrivit", "écrivîmes", "écrivîtes", "écrivirent"] },
  prendre: { present: ["prends", "prends", "prend", "prenons", "prenez", "prennent"], pp: "pris", aux: "avoir", ps: ["pris", "pris", "prit", "prîmes", "prîtes", "prirent"] },
  voir: { present: ["vois", "vois", "voit", "voyons", "voyez", "voient"], pp: "vu", aux: "avoir", ps: ["vis", "vis", "vit", "vîmes", "vîtes", "virent"] },
  venir: { present: ["viens", "viens", "vient", "venons", "venez", "viennent"], pp: "venu", aux: "être", ps: ["vins", "vins", "vint", "vînmes", "vîntes", "vinrent"] },
  partir: { present: ["pars", "pars", "part", "partons", "partez", "partent"], pp: "parti", aux: "être", ps: ["partis", "partis", "partit", "partîmes", "partîtes", "partirent"] },
  sortir: { present: ["sors", "sors", "sort", "sortons", "sortez", "sortent"], pp: "sorti", aux: "être", ps: ["sortis", "sortis", "sortit", "sortîmes", "sortîtes", "sortirent"] },
  sentir: { present: ["sens", "sens", "sent", "sentons", "sentez", "sentent"], pp: "senti", aux: "avoir", ps: ["sentis", "sentis", "sentit", "sentîmes", "sentîtes", "sentirent"] },
  dormir: { present: ["dors", "dors", "dort", "dormons", "dormez", "dorment"], pp: "dormi", aux: "avoir", ps: ["dormis", "dormis", "dormit", "dormîmes", "dormîtes", "dormirent"] },
};
// Regular verbs used in the lessons; arriver, entrer, rentrer, tomber, rester and monter take être.
const ETRE_ER = new Set(["arriver", "entrer", "rentrer", "tomber", "rester", "monter"]);
const SECOND = new Set(["finir", "choisir", "grandir", "réussir", "remplir", "obéir", "nourrir", "guérir", "réfléchir", "salir"]);
const REG = ["parler", "jouer", "laver", "aider", "travailler", "désinfecter", "manger", "nager", "ranger", "partager", "commencer", "lancer", "avancer",
  "arriver", "entrer", "tomber", "rester", "appeler", "jeter", "acheter", "lever", "préférer", "espérer", "répéter"];
/** Every verb the lessons use: regular -er, 2nd-group -ir, and the irregular table. */
export const fr2Verbs = () => [...REG, ...SECOND, ...Object.keys(IRR)];
export const fr2Group = (v) => (IRR[v] ? 3 : SECOND.has(v) ? 2 : v.endsWith("er") ? 1 : 3);
const isKnown = (v) => !!IRR[v] || SECOND.has(v) || v.endsWith("er");

const ER = ["e", "es", "e", "ons", "ez", "ent"];
const IR = ["is", "is", "it", "issons", "issez", "issent"];
/** Present-tense form alone: fr2Present("manger", 4) = "mangeons", fr2Present("commencer", 4) = "commençons". */
export function fr2Present(v, p) {
  if (!isKnown(v)) throw new RangeError(`fr2Present: ${v}`);
  const k = PERSON[p];
  if (IRR[v]) return IRR[v].present[k];
  if (SECOND.has(v)) return v.slice(0, -2) + IR[k];
  let stem = v.slice(0, -2);
  if (k === 3 && v.endsWith("ger")) stem += "e";             // nous mangeons
  if (k === 3 && v.endsWith("cer")) stem = stem.slice(0, -1) + "ç";  // nous commençons
  if (SILENT.includes(k)) {                                   // before a silent ending (e, es, e, ent)
    if (DOUBLE.has(v)) stem += stem.slice(-1);                // j’appelle, je jette
    else if (GRAVE.has(v)) stem = stem.replace(/e([^e]*)$/, "è$1");   // j’achète, je lève
    else if (GRAVE_E.has(v)) stem = stem.replace(/é([^é]*)$/, "è$1"); // je préfère
  }
  return stem + ER[k];
}
const SILENT = [0, 1, 2, 5];
const DOUBLE = new Set(["appeler", "jeter", "rappeler", "épeler", "projeter"]);
const GRAVE = new Set(["acheter", "lever", "peser", "mener", "amener", "geler"]);
const GRAVE_E = new Set(["préférer", "espérer", "répéter", "céder"]);
/** The spelling change a -er verb makes in the présent, in words (for the working). */
export function fr2Change(v) {
  if (v.endsWith("ger")) return "on garde le e devant -ons : nous " + fr2Present(v, 4);
  if (v.endsWith("cer")) return "le c devient ç devant -ons : nous " + fr2Present(v, 4);
  if (DOUBLE.has(v)) return "la consonne double devant un e muet : " + fr2With(0, fr2Present(v, 0));
  if (GRAVE.has(v) || GRAVE_E.has(v)) return "le e prend un accent grave devant un e muet : " + fr2With(0, fr2Present(v, 0));
  return "pas de changement";
}
/** Wrong on purpose: the -er ending added to the bare stem, with no spelling change (for feedback only). */
export const fr2PlainPresent = (v, p) => v.slice(0, -2) + ER[PERSON[p]];
/** Wrong on purpose: the passé composé with the other auxiliary, or without agreement (for feedback only). */
export function fr2PcOtherAux(v, p) {
  const other = fr2Aux(v) === "être" ? "avoir" : "être";
  return withPronoun(p, `${fr2Present(other, p)} ${fr2Participle(v)}`);
}
export const fr2PcNoAgree = (v, p) => withPronoun(p, `${fr2Present(fr2Aux(v), p)} ${fr2Participle(v)}`);
/** Wrong on purpose: the infinitive in place of the participle ("j’ai manger"). */
export const fr2PcInfinitive = (v, p) => withPronoun(p, `${fr2Present(fr2Aux(v), p)} ${v}`);
/** Past participle: mangé, fini, fait … */
export function fr2Participle(v) {
  if (IRR[v]) return IRR[v].pp;
  if (SECOND.has(v)) return v.slice(0, -1);
  if (v.endsWith("er")) return v.slice(0, -2) + "é";
  throw new RangeError(`fr2Participle: ${v}`);
}
export const fr2Aux = (v) => (IRR[v] ? IRR[v].aux : ETRE_ER.has(v) ? "être" : "avoir");
/** Passé composé, with the pronoun and agreement after être: "elles sont allées", "j’ai mangé". */
export function fr2PasseCompose(v, p) {
  const aux = fr2Present(fr2Aux(v), p);
  let pp = fr2Participle(v);
  if (fr2Aux(v) === "être") pp += (feminine(p) ? "e" : "") + (plural(p) ? "s" : "");
  return withPronoun(p, `${aux} ${pp}`);
}
const IMP = ["ais", "ais", "ait", "ions", "iez", "aient"];
/** Imparfait form alone: stem of “nous” in the present + endings; mangeais / mangions, commençais / commencions. */
export function fr2Imparfait(v, p) {
  const k = PERSON[p];
  let stem = IRR[v]?.imp || fr2Present(v, 4).slice(0, -3);
  if (v.endsWith("ger") && !IRR[v]) stem = k === 3 || k === 4 ? stem.slice(0, -1) : stem;        // mange-ais, mang-ions
  if (v.endsWith("cer") && !IRR[v] && (k === 3 || k === 4)) stem = stem.slice(0, -1) + "c";      // commenç-ais, commenc-ions
  return stem + IMP[k];
}
const PS_ER = ["ai", "as", "a", "âmes", "âtes", "èrent"];
const PS_IR = ["is", "is", "it", "îmes", "îtes", "irent"];
/** Passé simple form alone: il mangea, ils mangèrent, il commença, elle finit, il fit. */
export function fr2PasseSimple(v, p) {
  const k = PERSON[p];
  if (IRR[v] && Array.isArray(IRR[v].ps)) return IRR[v].ps[k];
  if (SECOND.has(v)) return v.slice(0, -2) + PS_IR[k];
  let stem = v.slice(0, -2);
  const end = PS_ER[k];
  if (v.endsWith("ger") && /^[aâ]/.test(end)) stem += "e";       // mangea, mangeâmes
  if (v.endsWith("cer") && /^[aâ]/.test(end)) stem = stem.slice(0, -1) + "ç";       // commença
  return stem + end;
}
/** Participe présent: mangeant, commençant, finissant, étant, ayant, faisant. Gérondif: "en" + participe présent. */
export function fr2ParticipePresent(v) {
  if (IRR[v]?.ppr) return IRR[v].ppr;
  return fr2Present(v, 4).slice(0, -3) + "ant";
}
export const fr2Gerondif = (v) => `en ${fr2ParticipePresent(v)}`;
/** Pronoun + form with elision of je: "j’ai", "je mange". */
export function withPronoun(p, form) {
  return p === 0 && /^[aeiouyéèêh]/.test(form) ? `j’${form}` : `${PRON[p]} ${form}`;
}
export const fr2With = (p, form) => withPronoun(p, form);
/** The infinitive's ending: "-er", "-ir", "-re", "-oir". */
export const fr2Ending = (v) => (v.endsWith("oir") ? "-oir" : v.endsWith("er") ? "-er" : v.endsWith("ir") ? "-ir" : "-re");

// ---------------------------------------------------------------- adjectives and nouns (authored, TR-Z02)
// Masculine singular → [feminine singular, masculine plural, feminine plural]
const ADJ = {
  national: ["nationale", "nationaux", "nationales"], spécial: ["spéciale", "spéciaux", "spéciales"], principal: ["principale", "principaux", "principales"],
  général: ["générale", "généraux", "générales"], normal: ["normale", "normaux", "normales"], amical: ["amicale", "amicaux", "amicales"],
  final: ["finale", "finals", "finales"], banal: ["banale", "banals", "banales"], natal: ["natale", "natals", "natales"], naval: ["navale", "navals", "navales"],
  petit: ["petite", "petits", "petites"], grand: ["grande", "grands", "grandes"], propre: ["propre", "propres", "propres"], sale: ["sale", "sales", "sales"],
  beau: ["belle", "beaux", "belles"], nouveau: ["nouvelle", "nouveaux", "nouvelles"], vieux: ["vieille", "vieux", "vieilles"], malade: ["malade", "malades", "malades"],
  vert: ["verte", "verts", "vertes"], noir: ["noire", "noirs", "noires"], bleu: ["bleue", "bleus", "bleues"], blanc: ["blanche", "blancs", "blanches"],
  rouge: ["rouge", "rouges", "rouges"], jaune: ["jaune", "jaunes", "jaunes"], gris: ["grise", "gris", "grises"],
  // colour words that come from a noun stay invariable (TR-Z02; rose and mauve are exceptions that agree)
  orange: ["orange", "orange", "orange"], marron: ["marron", "marron", "marron"], kaki: ["kaki", "kaki", "kaki"], rose: ["rose", "roses", "roses"],
};
export const fr2AdjList = () => Object.keys(ADJ);
/** The adjective agreed with gender ("m"/"f") and number (true = plural). */
export function fr2Adj(a, g, pl) {
  if (!ADJ[a]) throw new RangeError(`fr2Adj: ${a}`);
  if (g === "m" && !pl) return a;
  return ADJ[a][g === "f" ? (pl ? 2 : 0) : 1];
}
/** Wrong on purpose: the pupil's usual rule, just add -e / -s (for feedback only). */
export const fr2AdjNaive = (a, g, pl) => a + (g === "f" ? "e" : "") + (pl ? "s" : "");
// Nouns in -al and -ail: most -al → -aux; bal, carnaval, festival, chacal, récital, régal → -als;
// most -ail → -ails; travail, corail, émail, soupirail, vitrail, bail, vantail → -aux.
const NOUN_PL = { cheval: "chevaux", journal: "journaux", animal: "animaux", hôpital: "hôpitaux", canal: "canaux", métal: "métaux", signal: "signaux", général: "généraux",
  bal: "bals", carnaval: "carnavals", festival: "festivals", chacal: "chacals", récital: "récitals", régal: "régals",
  détail: "détails", éventail: "éventails", rail: "rails", gouvernail: "gouvernails", épouvantail: "épouvantails",
  travail: "travaux", corail: "coraux", émail: "émaux", vitrail: "vitraux", bail: "baux", soupirail: "soupiraux" };
export const fr2Nouns = () => Object.keys(NOUN_PL);
export const fr2NounPlural = (n) => { if (!NOUN_PL[n]) throw new RangeError(`fr2NounPlural: ${n}`); return NOUN_PL[n]; };
/** Wrong on purpose: always -aux (or always -s), for feedback only. */
export const fr2NounNaive = (n) => (NOUN_PL[n].endsWith("aux") ? `${n}s` : n.replace(/(al|ail)$/, "aux"));
/** Wrong on purpose: an adjective in -al always given -aux ("finaux" for final), for feedback only. */
export const fr2AlAux = (a) => a.replace(/al$/, "aux");
/** The other gender: "m" ↔ "f". */
export const fr2OtherGender = (g) => (g === "m" ? "f" : "m");
/** "masculin singulier", "féminin pluriel" … */
export const fr2GenderNumber = (g, pl) => `${g === "m" ? "masculin" : "féminin"} ${pl ? "pluriel" : "singulier"}`;
/** Wrong on purpose: an -ir verb conjugated in the other group (nous choisons, nous sentissons), for feedback only. */
export function fr2WrongGroup(v, p) {
  const k = PERSON[p];
  if (SECOND.has(v)) return v.slice(0, -2) + ["s", "s", "t", "ons", "ez", "ent"][k];
  if (v.endsWith("ir")) return v.slice(0, -2) + IR[k];
  throw new RangeError(`fr2WrongGroup: ${v}`);
}
