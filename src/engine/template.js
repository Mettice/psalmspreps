// Turns a JSON question template + a seed into a concrete question, and checks responses.
// Correctness is always decided here, by code: the answer is computed from the template's
// expressions, never stored as free text from an author or a model.
//
// Template types
//   numeric     answer: expr, answer_kind: number | base | roman | text, unit?
//   mcq         correct: tmpl + distractors: [tmpl | {text?, misconception}]   (computed values)
//               or pool: {right: [stmt], wrong: [stmt]}, pick: {right, wrong}  (choose the true one)
//   spot_error  pool + pick (choose the false statement), or steps: [stmt] with exactly one false
//   ordering    items: [{text, key?}], order: asc | desc | as_written
//   cloze       text: tmpl with one ___ blank, answer: expr, accept?: [expr]
//               choices: [tmpl | {text, misconception}] → pick one (shown like mcq); no choices → typed,
//               checked against the accepted list (case- and space-insensitive), misconceptions: [{id, wrong: expr, explain}]
//   word_order  answer: tmpl (the sentence), accept?: [tmpl] (other correct orders of the same words)
//   matching    pool: [{left: tmpl, right: tmpl}], pick: n; with groups: true several lefts may share a right
//               (sort into groups)
// A stmt is {text: tmpl, truth: expr, explain?, misconception?}; the engine evaluates every truth.

import { evaluate, render, eq } from "./expr.js";
import { makeRng } from "./rng.js";

const LETTERS = "ABCDEFGHKLMNPRST";
const MAX_TRIES = 500;
const BLANK = "___";
const BAD = /NaN|undefined|\[object Object\]|Infinity/;

/** Typed words: case-insensitive, outer and repeated spaces ignored, curly quotes read as straight ones. */
export function normaliseText(s) {
  return String(s).replace(/[‘’ʼ`]/g, "'").replace(/[“”]/g, '"')
    .replace(/[\s  ]+/g, " ").trim().toLowerCase();
}

function hash(s) {
  let h = 2166136261;
  for (const c of s) h = Math.imul(h ^ c.charCodeAt(0), 16777619);
  return h >>> 0;
}

export class ContentError extends Error {}

function show(lib) {
  return (v) => (typeof v === "number" ? lib.fmt(v) : Array.isArray(v) ? v.join(", ") : String(v));
}

function renderDeep(x, scope, lib) {
  if (typeof x === "string") return render(x, scope, lib, show(lib));
  if (Array.isArray(x)) return x.map((y) => renderDeep(y, scope, lib));
  if (x && typeof x === "object") return Object.fromEntries(Object.entries(x).map(([k, v]) => [k, renderDeep(v, scope, lib)]));
  return x;
}

function sampleVar(spec, scope, rng, lib) {
  if (spec === null || typeof spec !== "object" || Array.isArray(spec)) return spec;
  if ("int" in spec) {
    const [lo, hi] = spec.int.map((e) => evaluate(e, scope, lib));
    const step = spec.step || 1;
    return lo + step * rng.int(0, Math.floor((hi - lo) / step));
  }
  if ("pick" in spec) return renderDeep(rng.pick(spec.pick), scope, lib);
  if ("sample" in spec) return rng.sample(evaluate(spec.sample[0], scope, lib), evaluate(spec.sample[1], scope, lib));
  if ("letters" in spec) return rng.sample(LETTERS.split(""), spec.letters);
  if ("expr" in spec) return evaluate(spec.expr, scope, lib);
  throw new ContentError(`unknown variable spec ${JSON.stringify(spec)}`);
}

export function sampleScope(vars, where, rng, lib) {
  const conds = where ? [].concat(where) : [];
  for (let t = 0; t < MAX_TRIES; t++) {
    const scope = {};
    for (const [name, spec] of Object.entries(vars || {})) scope[name] = sampleVar(spec, scope, rng, lib);
    if (conds.every((c) => evaluate(c, scope, lib))) return scope;
  }
  throw new ContentError(`could not satisfy 'where' after ${MAX_TRIES} tries: ${conds.join(" && ")}`);
}

// ---------------------------------------------------------------- answer normalisation
export function parseNumber(s) {
  let t = String(s).replace(/[\s  ]/g, "").replace(/−/g, "-");
  if (/^-?\d{1,3}(,\d{3})+$/.test(t)) t = t.replace(/,/g, "");  // 1,500 = thousands separator
  else t = t.replace(",", ".");                                   // 2,5 = decimal comma
  return /^-?(\d+\.?\d*|\.\d+)$/.test(t) ? Number(t) : NaN;
}

const SUBSCRIPTS = /[₀₁₂₃₄₅₆₇₈₉]/g;

export function normalize(value, kind) {
  if (kind === "number") return typeof value === "number" ? value : parseNumber(value);
  const s = String(value).replace(/[\s  ]/g, "");
  if (kind === "base") return s.replace(SUBSCRIPTS, "").replace(/^0+(?=\d)/, "");
  if (kind === "roman") return s.toUpperCase();
  return String(value).trim().replace(/\s+/g, " ").toLowerCase();
}

const same = (a, b, kind) => {
  const x = normalize(a, kind), y = normalize(b, kind);
  return kind === "number" ? !Number.isNaN(x) && eq(x, y) : x === y;
};

// ---------------------------------------------------------------- statements
function stmt(s, scope, lib) {
  const text = render(s.text, scope, lib, show(lib));
  const truth = evaluate(s.truth, scope, lib);
  if (typeof truth !== "boolean") throw new ContentError(`truth of "${text}" is not true/false`);
  return { text, truth, misconception: s.misconception, explain: s.explain && render(s.explain, scope, lib, show(lib)) };
}

function fromPool(tpl, scope, rng, lib, wantTrue) {
  const right = tpl.pool.right.map((s) => stmt(s, scope, lib));
  const wrong = tpl.pool.wrong.map((s) => stmt(s, scope, lib));
  for (const s of right) if (!s.truth) throw new ContentError(`${tpl.id}: "${s.text}" is listed as right but evaluates false`);
  for (const s of wrong) if (s.truth) throw new ContentError(`${tpl.id}: "${s.text}" is listed as wrong but evaluates true`);
  const chosen = rng.shuffle([...rng.sample(right, tpl.pick.right), ...rng.sample(wrong, tpl.pick.wrong)]);
  if (new Set(chosen.map((s) => s.text)).size !== chosen.length) return null;  // two identical statements: resample
  const answers = chosen.map((s, i) => (s.truth === wantTrue ? i : -1)).filter((i) => i >= 0);
  if (answers.length !== 1) throw new ContentError(`${tpl.id}: pick must give exactly one ${wantTrue ? "true" : "false"} statement`);
  return { options: chosen.map(({ text, misconception, explain }) => ({ text, misconception, explain })), correctIndex: answers[0] };
}

// ---------------------------------------------------------------- full working
/**
 * The correct answer with full working, shown after a second miss (decision 2026-10-03).
 * Numeric and computed-mcq templates write it in `solution` (templates, may use {answer});
 * statement, spot-the-error and ordering questions build it from their own data.
 */
function solutionOf(tpl, scope, q, R) {
  const quote = (t) => `“${t}”`;
  if (tpl.solution) return tpl.solution.flatMap((t) => R(t, { ...scope, answer: q.answer }).split("\n"));
  if (q.type === "mcq" && tpl.pool) {
    return [`The true statement is ${quote(q.answer)}.`,
      ...q.options.filter((o, i) => i !== q.correctIndex && o.explain).map((o) => `${quote(o.text)} is false: ${o.explain}`)];
  }
  if (q.type === "spot_error") {
    const wrong = q.options[q.correctIndex];
    return [`The wrong ${tpl.pool ? "statement" : "line"} is ${quote(wrong.text)}.`, ...(wrong.explain ? [wrong.explain] : [])];
  }
  if (q.type === "ordering") return [`The correct order is: ${q.answer}.`];
  if (q.type === "cloze") return [`The missing word${/\s/.test(q.answer) ? "s are" : " is"} ${quote(q.answer)}.`, q.full];
  if (q.type === "word_order") return [`The sentence is: ${q.answer}`];
  if (q.type === "matching") return ["The right pairs are:", ...q.left.map((l, i) => `${l} → ${q.right[q.correctMatch[i]]}`)];
  return undefined;  // numeric / computed mcq without a written solution (tests require one in Form 1 lessons)
}

// ---------------------------------------------------------------- instantiate
export function instantiate(tpl, seed, lib, lesson = null) {
  const rng = makeRng(hash(tpl.id) ^ seed);
  const R = (t, scope) => render(t, scope, lib, show(lib));
  const withSolution = (q, scope) => {
    const solution = solutionOf(tpl, scope, q, R);
    if (solution) q.solution = solution;
    return q;
  };
  const miscById = Object.fromEntries((tpl.misconceptions || []).map((m) => [m.id, m]));
  const explainOf = (id, scope) => (id && miscById[id] ? R(miscById[id].explain, scope) : undefined);

  for (let t = 0; t < MAX_TRIES; t++) {
    const scope = sampleScope(tpl.vars, tpl.where, rng, lib);
    const q = { id: tpl.id, lesson, seed, type: tpl.type, level: tpl.level, prompt: R(tpl.prompt, scope) };
    if (tpl.hint) q.hint = R(tpl.hint, scope);

    if (tpl.type === "numeric") {
      const kind = tpl.answer_kind || "number";
      const value = evaluate(tpl.answer, scope, lib);
      if (kind === "number" && (typeof value !== "number" || !Number.isFinite(value))) throw new ContentError(`${tpl.id}: answer is ${value}`);
      Object.assign(q, { answerKind: kind, answerValue: value, answer: show(lib)(value), unit: tpl.unit && R(tpl.unit, scope) });
      q.misconceptions = (tpl.misconceptions || []).flatMap((m) => {
        if (m.when && !evaluate(m.when, scope, lib)) return [];
        const v = evaluate(m.wrong, scope, lib);
        if (v === undefined || (typeof v === "number" && !Number.isFinite(v)) || same(v, value, kind)) return [];
        return [{ id: m.id, value: show(lib)(v), explain: R(m.explain, scope) }];
      });
      q.verified = tpl.verify ? evaluate(tpl.verify, { ...scope, answer: value }, lib) === true : true;
      return withSolution(q, scope);
    }

    if (tpl.type === "mcq" && tpl.correct !== undefined) {
      const correct = R(tpl.correct, scope);
      const seen = new Set([correct]);
      const pool = [];
      for (const d of tpl.distractors) {
        if (d.when && !evaluate(d.when, scope, lib)) continue;
        const text = typeof d === "string" ? R(d, scope)
          : d.text !== undefined ? R(d.text, scope) : show(lib)(evaluate(miscById[d.misconception].wrong, scope, lib));
        if (seen.has(text) || text.includes("NaN") || text.includes("undefined")) continue;
        seen.add(text);
        pool.push({ text, misconception: d.misconception, explain: explainOf(d.misconception, scope) });
      }
      const need = (tpl.show || 4) - 1;
      if (pool.length < Math.min(need, tpl.min_distractors ?? need)) continue;  // resample: not enough distinct options
      const options = rng.shuffle([{ text: correct }, ...rng.sample(pool, need)]);
      Object.assign(q, { options, correctIndex: options.findIndex((o) => o.text === correct), answer: correct });
      q.verified = tpl.verify ? evaluate(tpl.verify, { ...scope, answer: correct }, lib) === true : true;
      return withSolution(q, scope);
    }

    if (tpl.type === "mcq" || (tpl.type === "spot_error" && tpl.pool)) {
      const picked = fromPool(tpl, scope, rng, lib, tpl.type === "mcq");
      if (!picked) continue;
      Object.assign(q, picked);
      q.answer = q.options[q.correctIndex].text;
      q.verified = true;
      return withSolution(q, scope);
    }

    if (tpl.type === "spot_error") {
      const steps = tpl.steps.map((s) => stmt(s, scope, lib));
      const wrong = steps.map((s, i) => (s.truth ? -1 : i)).filter((i) => i >= 0);
      if (wrong.length !== 1) throw new ContentError(`${tpl.id}: ${wrong.length} false steps (need exactly 1)`);
      Object.assign(q, { options: steps.map(({ text, misconception, explain }) => ({ text, misconception, explain })),
        correctIndex: wrong[0], answer: steps[wrong[0]].text, ordered: true });
      q.verified = true;
      return withSolution(q, scope);
    }

    if (tpl.type === "ordering") {
      const items = tpl.items.map((it) => ({ text: R(it.text, scope), key: it.key === undefined ? undefined : evaluate(it.key, scope, lib) }));
      let correct = items.map((_, i) => i);
      if (tpl.order === "asc" || tpl.order === "desc") {
        const keys = items.map((i) => i.key);
        if (new Set(keys).size !== keys.length) continue;  // ties make the order ambiguous: resample
        correct.sort((a, b) => (tpl.order === "asc" ? keys[a] - keys[b] : keys[b] - keys[a]));
      }
      let display;
      do { display = rng.shuffle(items.map((_, i) => i)); } while (display.every((d, i) => d === correct[i]));
      Object.assign(q, {
        items: display.map((i) => items[i].text),
        correctOrder: correct.map((c) => display.indexOf(c)),  // display positions in the right order
        answer: correct.map((c) => items[c].text).join(" → "),
      });
      q.verified = true;
      return withSolution(q, scope);
    }

    if (tpl.type === "cloze") {
      const text = R(tpl.text, scope);
      if (text.split(BLANK).length !== 2) throw new ContentError(`${tpl.id}: the text needs exactly one ${BLANK} blank: ${text}`);
      const answer = String(evaluate(tpl.answer, scope, lib));
      const accept = [answer, ...(tpl.accept || []).flatMap((a) => [].concat(evaluate(a, scope, lib))).map(String)];  // an expr may give a list
      Object.assign(q, { sentence: text, answer, full: text.replace(BLANK, answer) });
      if (tpl.choices) {
        const seen = new Set([normaliseText(answer)]);
        const pool = [];
        for (const d of tpl.choices) {
          if (d.when && !evaluate(d.when, scope, lib)) continue;
          const t = typeof d === "string" ? R(d, scope) : R(d.text, scope);
          if (seen.has(normaliseText(t)) || BAD.test(t)) continue;
          seen.add(normaliseText(t));
          pool.push({ text: t, misconception: d.misconception, explain: explainOf(d.misconception, scope) });
        }
        const need = (tpl.show || 3) - 1;
        if (pool.length < need) continue;  // resample: not enough distinct choices
        const options = rng.shuffle([{ text: answer }, ...rng.sample(pool, need)]);
        Object.assign(q, { mode: "choose", options, correctIndex: options.findIndex((o) => o.text === answer) });
      } else {
        q.mode = "type";
        q.accept = [...new Set(accept.map(normaliseText))];
        q.misconceptions = (tpl.misconceptions || []).flatMap((m) => {
          if (m.when && !evaluate(m.when, scope, lib)) return [];
          return [].concat(m.wrong).flatMap((w) => [].concat(evaluate(w, scope, lib))).map(String)  // wrong: expr or [expr]
            .filter((v) => v && !q.accept.includes(normaliseText(v)))
            .map((v) => ({ id: m.id, value: v, explain: R(m.explain, scope) }));
        });
      }
      q.verified = (!BAD.test(answer) && answer.trim() !== "") && (tpl.verify ? evaluate(tpl.verify, { ...scope, answer }, lib) === true : true);
      return withSolution(q, scope);
    }

    if (tpl.type === "word_order") {
      // The final . ? or ! is not a tile: it stays at the end, so any correct order of the words is accepted.
      const answer = R(tpl.answer, scope);
      const end = /[.?!]$/.exec(answer)?.[0] || "";
      const body = (s) => s.replace(/\s*[.?!]$/, "");
      const words = body(answer).split(/\s+/).filter(Boolean);
      if (words.length < 3) throw new ContentError(`${tpl.id}: a word-order sentence needs at least 3 words: ${answer}`);
      const accept = [answer, ...(tpl.accept || []).map((a) => R(a, scope))].map(body);
      const bag = (s) => s.split(/\s+/).filter(Boolean).map(normaliseText).sort().join(" ");
      for (const a of accept) if (bag(a) !== bag(body(answer))) throw new ContentError(`${tpl.id}: "${a}" does not use the same words as "${answer}"`);
      const inOrder = (d) => accept.some((a) => normaliseText(d.map((i) => words[i]).join(" ")) === normaliseText(a));
      let display = rng.shuffle(words.map((_, i) => i));
      for (let k = 0; inOrder(display); k++) {
        if (k > 50) throw new ContentError(`${tpl.id}: cannot shuffle "${answer}" out of order`);
        display = rng.shuffle(words.map((_, i) => i));
      }
      Object.assign(q, {
        items: display.map((i) => words[i]),
        correctOrder: words.map((_, w) => display.indexOf(w)),
        accept: accept.map(normaliseText),
        end,
        answer,
      });
      q.verified = !BAD.test(answer);
      return withSolution(q, scope);
    }

    if (tpl.type === "matching") {
      const pairs = rng.sample(tpl.pool, tpl.pick || tpl.pool.length).map((p) => ({ left: R(p.left, scope), right: R(p.right, scope) }));
      const lefts = pairs.map((p) => p.left), rights = pairs.map((p) => p.right);
      if (new Set(lefts).size !== lefts.length) continue;                     // resample: two identical left items
      if (!tpl.groups && new Set(rights).size !== rights.length) continue;    // resample: two identical answers
      const shownRights = [...new Set(rights)];
      if (tpl.groups && tpl.group_order) shownRights.sort((a, b) => tpl.group_order.indexOf(a) - tpl.group_order.indexOf(b));
      let right = tpl.groups && tpl.group_order ? shownRights : rng.shuffle(shownRights);
      if (!tpl.groups && right.length > 1) while (right.every((r, i) => r === rights[i])) right = rng.shuffle(shownRights);
      if (tpl.groups && right.length < 2) continue;                          // resample: every item in one group
      Object.assign(q, { left: lefts, right, correctMatch: rights.map((r) => right.indexOf(r)), groups: !!tpl.groups });
      q.answer = lefts.map((l, i) => `${l} → ${rights[i]}`).join("; ");
      q.verified = ![...lefts, ...right].some((t) => BAD.test(t));
      return withSolution(q, scope);
    }
    throw new ContentError(`${tpl.id}: unknown type ${tpl.type}`);
  }
  throw new ContentError(`${tpl.id}: could not build enough distinct options`);
}

// ---------------------------------------------------------------- typed input
/**
 * Cleans what the pupil typed before checking: spaces, non-breaking and thin spaces always go;
 * commas also go when the answer is a whole number ("9,038,766" → "9038766").
 */
export function normaliseInput(text, q) {
  if (q.type === "cloze") return String(text).replace(/[\s  ]+/g, " ").trim();  // words keep their spaces
  const s = String(text).replace(/[\s   ]/g, "");
  return q.answerKind === "number" && Number.isInteger(q.answerValue) ? s.replace(/,/g, "") : s;
}

/** Keyboard to show: the number pad for whole numbers and base numerals, decimal pad otherwise. */
export function inputModeFor(q) {
  if (q.type === "cloze") return "text";
  if (q.answerKind === "base" || (q.answerKind === "number" && Number.isInteger(q.answerValue))) return "numeric";
  return q.answerKind === "number" ? "decimal" : "text";
}

// ---------------------------------------------------------------- checking
/** The pupil pressed "I don't know". Incorrect for mastery; no misconception feedback. */
export const DONT_KNOW = Object.freeze({ dontKnow: true });

/** response: string for numeric, option index for mcq/spot_error, display-index array for ordering, or DONT_KNOW. */
export function check(q, response) {
  if (response === DONT_KNOW) {
    return { correct: false, dontKnow: true, misconception: null, show: q.hint ? ["hint", "worked_example"] : ["worked_example"] };
  }
  if (q.type === "numeric") {
    if (same(response, q.answerValue, q.answerKind)) return { correct: true };
    const m = q.misconceptions.find((x) => same(response, x.value, q.answerKind));
    return { correct: false, misconception: m ? { id: m.id, explain: m.explain } : null };
  }
  if (q.type === "mcq" || q.type === "spot_error") {
    if (response === q.correctIndex) return { correct: true };
    const o = q.options[response];
    return { correct: false, misconception: o && (o.misconception || o.explain) ? { id: o.misconception || null, explain: o.explain } : null };
  }
  if (q.type === "ordering") return { correct: Array.isArray(response) && response.every((r, i) => r === q.correctOrder[i]) && response.length === q.correctOrder.length };
  if (q.type === "cloze") {
    if (q.mode === "choose") {
      if (response === q.correctIndex) return { correct: true };
      const o = q.options[response];
      return { correct: false, misconception: o && (o.misconception || o.explain) ? { id: o.misconception || null, explain: o.explain } : null };
    }
    const typed = normaliseText(response);
    if (q.accept.includes(typed)) return { correct: true };
    const m = q.misconceptions.find((x) => normaliseText(x.value) === typed);
    return { correct: false, misconception: m ? { id: m.id, explain: m.explain } : null };
  }
  if (q.type === "word_order") {
    // response: display indices in the order tapped. Any accepted order of the same words is right.
    const ok = Array.isArray(response) && response.length === q.items.length && new Set(response).size === response.length;
    return { correct: ok && q.accept.includes(normaliseText(response.map((i) => q.items[i]).join(" "))) };
  }
  if (q.type === "matching") {
    // response: for each left item, the index of the right item chosen. All must be right; wrong ones are listed.
    const wrong = q.left.map((_, i) => i).filter((i) => !Array.isArray(response) || q.right[response[i]] !== q.right[q.correctMatch[i]]);
    return wrong.length ? { correct: false, wrongPairs: wrong } : { correct: true };
  }
  throw new Error(`unknown type ${q.type}`);
}

// ---------------------------------------------------------------- worked examples
/** Renders a worked example from fixed `vars`: every number is computed by code. */
export function renderWorked(we, lib) {
  const scope = sampleScope(we.vars, null, makeRng(1), lib);
  const R = (t) => render(t, scope, lib, show(lib));
  const failed = (we.checks || []).filter((c) => evaluate(c, scope, lib) !== true);
  return { problem: R(we.problem), steps: we.steps.map(R), answer: R(we.answer), failedChecks: failed };
}
