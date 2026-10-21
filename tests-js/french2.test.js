// Form 2 French library (src/engine/lib/french2.js): checked on known answers from the conjugation tables.
import { test } from "node:test";
import assert from "node:assert/strict";
import * as f from "../src/engine/lib/french2.js";

const all = (fn, v) => [0, 1, 2, 4, 5, 6].map((p) => fn(v, p));

test("présent: regular, -ger, -cer, 2nd group and irregular verbs", () => {
  assert.deepEqual(all(f.fr2Present, "parler"), ["parle", "parles", "parle", "parlons", "parlez", "parlent"]);
  assert.equal(f.fr2Present("manger", 4), "mangeons");
  assert.equal(f.fr2Present("nager", 4), "nageons");
  assert.equal(f.fr2Present("commencer", 4), "commençons");
  assert.equal(f.fr2Present("lancer", 2), "lance");
  assert.deepEqual(all(f.fr2Present, "finir"), ["finis", "finis", "finit", "finissons", "finissez", "finissent"]);
  assert.deepEqual(all(f.fr2Present, "aller"), ["vais", "vas", "va", "allons", "allez", "vont"]);
  assert.equal(f.fr2Present("faire", 5), "faites");
  assert.throws(() => f.fr2Present("savoir", 0));
});

test("passé composé with avoir and être, agreement and elision", () => {
  assert.equal(f.fr2PasseCompose("manger", 0), "j’ai mangé");
  assert.equal(f.fr2PasseCompose("finir", 4), "nous avons fini");
  assert.equal(f.fr2PasseCompose("faire", 2), "il a fait");
  assert.equal(f.fr2PasseCompose("aller", 7), "elles sont allées");
  assert.equal(f.fr2PasseCompose("venir", 3), "elle est venue");
  assert.equal(f.fr2PasseCompose("arriver", 6), "ils sont arrivés");
  assert.equal(f.fr2PasseCompose("être", 0), "j’ai été");
  assert.equal(f.fr2Aux("tomber"), "être");
  assert.equal(f.fr2Aux("prendre"), "avoir");
});

test("imparfait from the nous-form of the présent", () => {
  assert.deepEqual(all(f.fr2Imparfait, "manger"), ["mangeais", "mangeais", "mangeait", "mangions", "mangiez", "mangeaient"]);
  assert.deepEqual(all(f.fr2Imparfait, "commencer"), ["commençais", "commençais", "commençait", "commencions", "commenciez", "commençaient"]);
  assert.equal(f.fr2Imparfait("finir", 2), "finissait");
  assert.equal(f.fr2Imparfait("être", 0), "étais");
  assert.equal(f.fr2Imparfait("faire", 6), "faisaient");
  assert.equal(f.fr2Imparfait("avoir", 4), "avions");
});

test("passé simple", () => {
  assert.deepEqual(all(f.fr2PasseSimple, "parler"), ["parlai", "parlas", "parla", "parlâmes", "parlâtes", "parlèrent"]);
  assert.equal(f.fr2PasseSimple("manger", 2), "mangea");
  assert.equal(f.fr2PasseSimple("manger", 6), "mangèrent");
  assert.equal(f.fr2PasseSimple("commencer", 2), "commença");
  assert.equal(f.fr2PasseSimple("commencer", 6), "commencèrent");
  assert.equal(f.fr2PasseSimple("finir", 6), "finirent");
  assert.equal(f.fr2PasseSimple("aller", 2), "alla");
  assert.equal(f.fr2PasseSimple("être", 6), "furent");
  assert.equal(f.fr2PasseSimple("venir", 2), "vint");
  assert.equal(f.fr2PasseSimple("faire", 2), "fit");
});

test("participe présent and gérondif", () => {
  assert.equal(f.fr2ParticipePresent("manger"), "mangeant");
  assert.equal(f.fr2ParticipePresent("commencer"), "commençant");
  assert.equal(f.fr2ParticipePresent("finir"), "finissant");
  assert.equal(f.fr2ParticipePresent("faire"), "faisant");
  assert.equal(f.fr2ParticipePresent("être"), "étant");
  assert.equal(f.fr2ParticipePresent("avoir"), "ayant");
  assert.equal(f.fr2Gerondif("lire"), "en lisant");
});

test("every verb in the table gives every form without error", () => {
  for (const v of f.fr2Verbs()) {
    for (let p = 0; p < 8; p++) {
      for (const fn of [f.fr2Present, f.fr2Imparfait, f.fr2PasseSimple, f.fr2PasseCompose]) assert.ok(fn(v, p).length >= 1 && !fn(v, p).includes("undefined"), `${v} ${p}`);
    }
    assert.ok(f.fr2ParticipePresent(v).endsWith("ant"), v);
  }
});

test("adjectives in -al, colours and nouns in -al / -ail", () => {
  assert.equal(f.fr2Adj("national", "m", true), "nationaux");
  assert.equal(f.fr2Adj("national", "f", true), "nationales");
  assert.equal(f.fr2Adj("final", "m", true), "finals");
  assert.equal(f.fr2Adj("blanc", "f", false), "blanche");
  assert.equal(f.fr2Adj("orange", "f", true), "orange");
  assert.equal(f.fr2Adj("rose", "f", true), "roses");
  assert.equal(f.fr2AdjNaive("national", "m", true), "nationals");
  assert.equal(f.fr2NounPlural("cheval"), "chevaux");
  assert.equal(f.fr2NounPlural("festival"), "festivals");
  assert.equal(f.fr2NounPlural("travail"), "travaux");
  assert.equal(f.fr2NounPlural("détail"), "détails");
  for (const n of f.fr2Nouns()) assert.notEqual(f.fr2NounNaive(n), f.fr2NounPlural(n), n);
});

test("-eler, -eter and -é-er verbs change before a silent ending", () => {
  assert.deepEqual(all(f.fr2Present, "appeler"), ["appelle", "appelles", "appelle", "appelons", "appelez", "appellent"]);
  assert.equal(f.fr2Present("jeter", 6), "jettent");
  assert.equal(f.fr2Present("acheter", 0), "achète");
  assert.equal(f.fr2Present("acheter", 4), "achetons");
  assert.equal(f.fr2Present("lever", 2), "lève");
  assert.equal(f.fr2Present("préférer", 1), "préfères");
  assert.equal(f.fr2Present("préférer", 5), "préférez");
  assert.equal(f.fr2With(0, f.fr2Present("appeler", 0)), "j’appelle");
  assert.equal(f.fr2Imparfait("appeler", 0), "appelais");
  assert.equal(f.fr2PlainPresent("manger", 4), "mangons");
  assert.equal(f.fr2Change("commencer"), "le c devient ç devant -ons : nous commençons");
});

test("wrong-on-purpose passé composé forms", () => {
  assert.equal(f.fr2PcOtherAux("aller", 0), "j’ai allé");
  assert.equal(f.fr2PcOtherAux("manger", 2), "il est mangé");
  assert.equal(f.fr2PcNoAgree("aller", 7), "elles sont allé");
  assert.equal(f.fr2PcInfinitive("manger", 0), "j’ai manger");
});

test("helpers for adjectives and -ir verbs", () => {
  assert.equal(f.fr2AlAux("final"), "finaux");
  assert.equal(f.fr2OtherGender("m"), "f");
  assert.equal(f.fr2GenderNumber("f", true), "féminin pluriel");
  assert.equal(f.fr2WrongGroup("choisir", 4), "choisons");
  assert.equal(f.fr2WrongGroup("sentir", 4), "sentissons");
  assert.equal(f.fr2Present("sentir", 4), "sentons");
  assert.equal(f.fr2Present("choisir", 4), "choisissons");
});

test("plurals in -ou, -au, -eau, -eu and their rules", () => {
  assert.equal(f.fr2NounPlural("bijou"), "bijoux");
  assert.equal(f.fr2NounPlural("trou"), "trous");
  assert.equal(f.fr2NounPlural("bateau"), "bateaux");
  assert.equal(f.fr2NounPlural("pneu"), "pneus");
  assert.equal(f.fr2NounNaive("bijou"), "bijous");
  assert.equal(f.fr2NounNaive("trou"), "troux");
  assert.equal(f.fr2NounNaive("cheval"), "chevals");
  assert.equal(f.fr2NounNaive("festival"), "festivaux");
  assert.match(f.fr2NounRule("genou"), /sept noms en -ou/);
  for (const n of f.fr2Nouns()) assert.notEqual(f.fr2NounNaive(n), f.fr2NounPlural(n), n);
});

test("intensif helpers: naive forms, tenses, adverbs", () => {
  assert.equal(f.fr2ImparfaitNaive("manger", 0), "mangais");
  assert.equal(f.fr2ImparfaitNaive("finir", 2), "finait");
  assert.equal(f.fr2PsWrongGroup("parler", 2), "parlit");
  assert.equal(f.fr2PsWrongGroup("finir", 2), "fina");
  assert.equal(f.fr2PprNaive("commencer"), "commencant");
  assert.equal(f.fr2Form("manger", 4, "imparfait"), "nous mangions");
  assert.equal(f.fr2Form("aller", 3, "passé composé"), "elle est allée");
  assert.equal(f.fr2Form("faire", 6, "passé simple"), "ils firent");
  assert.equal(f.fr2Form("avoir", 0, "présent"), "j’ai");
  assert.ok(f.fr2Ambiguous("finir", 0) && !f.fr2Ambiguous("manger", 2));
  assert.equal(f.fr2Adverb("doux"), "doucement");
  assert.equal(f.fr2Adverb("prudent"), "prudemment");
  assert.equal(f.fr2AdvNaive("lent"), "lentment");
  assert.equal(f.fr2AdvRule("bruyant"), "-ant devient -amment");
  assert.equal(f.fr2AdvRule("lent"), "on ajoute -ment au féminin de l’adjectif");
  assert.equal(f.fr2AdvRule("patient"), "-ent devient -emment");
  for (const a of f.fr2AdvList().filter((a) => !a.endsWith("e"))) assert.notEqual(f.fr2AdvNaive(a), f.fr2Adverb(a), a);
});


test("Term 2 tenses: futur simple, conditionnel, futur proche, plus-que-parfait, impératif, subjonctif", () => {
  assert.equal(f.fr2FuturSimple("appeler", 0), "appellerai");
  assert.equal(f.fr2FuturSimple("acheter", 6), "achèteront");
  assert.equal(f.fr2FuturSimple("voir", 4), "verrons");
  assert.equal(f.fr2FuturSimple("envoyer", 2), "enverra");
  assert.equal(f.fr2Conditionnel("être", 0), "serais");
  assert.equal(f.fr2Conditionnel("finir", 6), "finiraient");
  assert.equal(f.fr2FuturProche("finir", 6), "ils vont finir");
  assert.equal(f.fr2PlusQueParfait("aller", 7), "elles étaient allées");
  assert.equal(f.fr2PlusQueParfait("manger", 0), "j’avais mangé");
  assert.deepEqual([0, 1, 2].map((k) => f.fr2Imperatif("manger", k)), ["mange", "mangeons", "mangez"]);
  assert.deepEqual([0, 1, 2].map((k) => f.fr2Imperatif("finir", k)), ["finis", "finissons", "finissez"]);
  assert.equal(f.fr2Imperatif("aller", 0), "va");
  assert.equal(f.fr2Que(0, f.fr2Subjonctif("avoir", 0)), "que j’aie");
  assert.equal(f.fr2Que(2, f.fr2Subjonctif("finir", 2)), "qu’il finisse");
  assert.equal(f.fr2Subjonctif("prendre", 4), "prenions");
  assert.equal(f.fr2Subjonctif("faire", 6), "fassent");
  assert.equal(f.fr2Present("recevoir", 6), "reçoivent");
});
