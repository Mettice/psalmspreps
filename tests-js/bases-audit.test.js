// Audit (2026-10-19) of every question in the number-base lessons (Maths 8, 9, 10): 1000 variants of each template (and of its
// step-by-step form). Answers are recomputed from the words of the question with independent base arithmetic.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import * as lib from "../src/engine/lib/maths.js";
import { instantiate, check, scaffoldTemplate } from "../src/engine/template.js";

const SUBD = "₀₁₂₃₄₅₆₇₈₉";
const subOf = (c) => (c ? SUBD.indexOf(c) : null);
const toTen = (s, b) => [...String(s)].reduce((t, d) => { if (+d >= b) throw new Error(`digit ${d} in base ${b}`); return t * b + +d; }, 0);
const toB = (n, b) => { let s = ""; do { s = (n % b) + s; n = Math.floor(n / b); } while (n > 0); return s; };
const N = String.raw`(\d+)([₀-₉]?)`;
const RE = {
  tenToB: new RegExp(String.raw`^Convert (\d+) to base (\d)\.$`),
  bToTen: new RegExp(String.raw`^Convert ${N} to base ten\.$`),
  bToB: new RegExp(String.raw`^Convert ${N} to base (\d)\.$`),
  calc: new RegExp(String.raw`^In base (\d), calculate ${N} ([+−×]) ${N}`),
  units: new RegExp(String.raw`^In base (\d), you calculate ${N} × ${N}\. Which digit do you write in the units column\?$`),
  check: new RegExp(String.raw`^To check a product, you first change ${N} to base ten\. What is it\?$`),
};
const BROKEN = /NaN|undefined|\[object|\{[a-zA-Z]/;
const problems = new Map(), add = (k) => problems.set(k, (problems.get(k) || 0) + 1);
let variants = 0;


test("number bases (Maths 8-10): every answer recomputed independently, right typings accepted, hints never on a right answer", () => {
  for (const n of [8, 9, 10]) {
    const l = JSON.parse(readFileSync(new URL(`../content/maths/${n}.json`, import.meta.url), "utf8"));
    const tpls = [...l.teach.cards.map((c) => c.check).filter((c) => !c.ref), ...l.questions];
    for (const t of tpls) {
      for (const tt of t.scaffold ? [t, scaffoldTemplate(t)] : [t]) for (let seed = 0; seed < 1000; seed++) {
        const q = instantiate(tt, seed, lib); variants++;
        const p = q.prompt;
        let expect = null, m;
        if ((m = p.match(RE.tenToB))) expect = toB(+m[1], +m[2]);
        else if ((m = p.match(RE.bToTen))) expect = String(toTen(m[1], subOf(m[2])));
        else if ((m = p.match(RE.bToB))) expect = toB(toTen(m[1], subOf(m[2])), +m[3]);
        else if ((m = p.match(RE.calc))) {
          const b = +m[1], x = toTen(m[2], b), y = toTen(m[5], b);
          expect = toB(m[4] === "+" ? x + y : m[4] === "−" ? x - y : x * y, b);
        } else if ((m = p.match(RE.units))) expect = String((toTen(m[2], +m[1]) % +m[1]) * toTen(m[4], +m[1]) % +m[1]);
        else if ((m = p.match(RE.check))) expect = String(toTen(m[1], subOf(m[2])));
        else if (q.type === "numeric") add(`${t.id}: prompt not recognised by the checker`);

        if (expect !== null && q.type === "numeric") {
          if (q.answer.replace(/\s/g, "") !== expect) add(`${t.id}: "${p}" answer ${q.answer}, expected ${expect}`);
          for (const r of [expect, ` ${expect} `, ...(q.base ? [expect + q.base, `${expect} ${q.base}`] : [])])
            if (!check(q, r).correct) add(`${t.id}: typed "${r}" for ${p} marked wrong`);
          for (const mi of q.misconceptions) if (check(q, mi.value).correct) add(`${t.id}: hint ${mi.id} given for a right answer`);
        }
        if (q.type === "blanks") {
          m = p.match(RE.bToTen) || p.match(RE.check);
          const digits = [...m[1]].map(Number), b = subOf(m[2]);
          const want = [...digits.map((_, i) => b ** (digits.length - 1 - i)), toTen(m[1], b)];
          if (JSON.stringify(q.answerValues) !== JSON.stringify(want)) add(`${t.id} step by step: ${q.answer} expected ${want}`);
          if (!check(q, q.answers).correct) add(`${t.id} step by step: right boxes marked wrong`);
        }
        if (q.options) {
          const texts = q.options.map((o) => o.text);
          if (new Set(texts).size !== texts.length) add(`${t.id}: two options are the same`);
          if (q.correctIndex < 0) add(`${t.id}: no right option`);
        }
        const texts = [q.prompt, q.answer, ...(q.solution || []), ...(q.options || []).flatMap((o) => [o.text, o.explain || ""]), ...(q.misconceptions || []).map((x) => x.explain)];
        if (texts.some((x) => BROKEN.test(String(x)))) add(`${t.id}: broken text`);
      }
    }
  }
  assert.ok(variants >= 22000, `${variants} variants`);
  assert.deepEqual([...problems], []);
});
