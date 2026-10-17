// Vetted functions for Form 2 Maths content (Term 1: integers, powers, primes, HCF and LCM, roots, sequences,
// distances, the coordinate plane, algebraic expressions, equations and inequalities). Used together with maths.js
// (fmt, sup, …). Pure and deterministic, like every library the content may call.
import { fmt, sup } from "./maths.js";

const MINUS = "−";

// ---------------------------------------------------------------- integers and powers
/** An integer as it is written inside a calculation: negative numbers in brackets, "(−3)". */
export const br = (n) => (n < 0 ? `(${fmt(n)})` : fmt(n));
/** A power: pw(2, 3) → "2³", pw(-2, 3) → "(−2)³", pw("a", 5) → "a⁵". */
export const pw = (a, n) => (typeof a === "string" ? a : br(a)) + sup(n);
/** A power written out as a product: powExpand(-2, 3) → "(−2) × (−2) × (−2)". */
export const powExpand = (a, n) => Array.from({ length: n }, () => (typeof a === "string" ? a : br(a))).join(" × ");
/** The sign of a product or quotient of integers, in words. */
export const signWord = (n) => (n > 0 ? "positive" : n < 0 ? "negative" : "zero");
/** WRONG ON PURPOSE: −a² read as (−a)², or (−a)ⁿ always positive. */
export const powNoSign = (a, n) => Math.abs(a) ** n;

// ---------------------------------------------------------------- primes, factors, HCF and LCM
export function isPrime(n) {
  if (!Number.isInteger(n) || n < 2) return false;
  for (let d = 2; d * d <= n; d++) if (n % d === 0) return false;
  return true;
}
/** Prime factors in increasing order, with repeats: 60 → [2, 2, 3, 5]. */
export function primeFactors(n) {
  const out = [];
  let m = n;
  for (let d = 2; d * d <= m; d++) while (m % d === 0) { out.push(d); m /= d; }
  if (m > 1) out.push(m);
  return out;
}
/** 60 → "2 × 2 × 3 × 5". */
export const factorProduct = (n) => primeFactors(n).join(" × ");
/** 60 → "2² × 3 × 5" (index form). */
export function factorise(n) {
  const f = primeFactors(n), seen = [...new Set(f)];
  return seen.map((p) => { const k = f.filter((x) => x === p).length; return k > 1 ? `${p}${sup(k)}` : String(p); }).join(" × ");
}
/** The repeated divisions of the ladder method: 60 → ["60 ÷ 2 = 30", "30 ÷ 2 = 15", "15 ÷ 3 = 5", "5 ÷ 5 = 1"]. */
export function ladder(n) {
  let m = n;
  return primeFactors(n).map((p) => { const line = `${fmt(m)} ÷ ${p} = ${fmt(m / p)}`; m /= p; return line; });
}
export const numFactors = (n) => Array.from({ length: n }, (_, i) => i + 1).filter((d) => n % d === 0).length;
/** All factors of n, in order: 12 → "1, 2, 3, 4, 6, 12". */
export const factorsOf = (n) => Array.from({ length: n }, (_, i) => i + 1).filter((d) => n % d === 0).join(", ");
/** The first k multiples of n: multiplesOf(4, 5) → "4, 8, 12, 16, 20". */
export const multiplesOf = (n, k) => Array.from({ length: k }, (_, i) => fmt(n * (i + 1))).join(", ");
export function hcf(a, b) {
  let x = Math.abs(a), y = Math.abs(b);
  while (y) [x, y] = [y, x % y];
  return x;
}
export const lcm = (a, b) => (a / hcf(a, b)) * b;
export const hcf3 = (a, b, c) => hcf(hcf(a, b), c);
export const lcm3 = (a, b, c) => lcm(lcm(a, b), c);

export const isSquare = (n) => Number.isInteger(n) && n >= 0 && Number.isInteger(Math.round(Math.sqrt(n))) && Math.round(Math.sqrt(n)) ** 2 === n;
export const isCube = (n) => Number.isInteger(n) && Math.round(Math.cbrt(n)) ** 3 === n;

// ---------------------------------------------------------------- sequences
/** The first k terms of the sequence that starts at a and adds d each time: "3, 7, 11, 15". */
export const seqTerms = (a, d, k) => Array.from({ length: k }, (_, i) => fmt(a + d * i)).join(", ");
/** The first k terms of the sequence that starts at a and multiplies by r each time: "2, 6, 18, 54". */
export const geoTerms = (a, r, k) => Array.from({ length: k }, (_, i) => fmt(a * r ** i)).join(", ");
/** The first k square numbers from 1² (squares), or cube numbers. */
export const squaresList = (k) => Array.from({ length: k }, (_, i) => fmt((i + 1) ** 2)).join(", ");
export const cubesList = (k) => Array.from({ length: k }, (_, i) => fmt((i + 1) ** 3)).join(", ");

// ---------------------------------------------------------------- distances
/** Three lengths make a triangle when each one is less than the sum of the other two. */
export const triangleOk = (a, b, c) => a < b + c && b < a + c && c < a + b;

// ---------------------------------------------------------------- the coordinate plane
/** A point's coordinates: pt(3, -2) → "(3, −2)". */
export const pt = (x, y) => `(${fmt(x)}, ${fmt(y)})`;

// ---------------------------------------------------------------- algebra
/** One term with its own sign: mono(-1, "x") → "−x", mono(3, "xy") → "3xy", mono(-5, "") → "−5". */
export function mono(c, v) {
  if (v === "") return fmt(c);
  if (c === 1) return v;
  if (c === -1) return MINUS + v;
  return fmt(c) + v;
}
/**
 * An expression from [coefficient, letters] pairs, zero terms left out:
 * poly([3, "x"], [-1, "y"], [5, ""]) → "3x − y + 5"; poly([0, "x"]) → "0".
 */
export function poly(...terms) {
  const kept = terms.filter(([c]) => c !== 0);
  if (!kept.length) return "0";
  return kept.map(([c, v], i) => {
    const t = mono(Math.abs(c), v);
    return i === 0 ? (c < 0 ? MINUS + t : t) : `${c < 0 ? ` ${MINUS} ` : " + "}${t}`;
  }).join("");
}
/** a(b + c) written out: bracket(3, [2, "x"], [5, ""]) → "3(2x + 5)"; a negative a keeps its sign: "−2(x − 4)". */
export const bracket = (a, ...terms) => `${a === 1 ? "" : a === -1 ? MINUS : fmt(a)}(${poly(...terms)})`;

// ---------------------------------------------------------------- inequalities
const OPS = { "<": (x, k) => x < k, ">": (x, k) => x > k, "≤": (x, k) => x <= k, "≥": (x, k) => x >= k };
export const ineq = (v, op, k) => `${v} ${op} ${fmt(k)}`;
export function holds(x, op, k) {
  if (!OPS[op]) throw new RangeError(`unknown inequality sign ${op}`);
  return OPS[op](x, k);
}
/** The sign turned round, as when both sides are multiplied or divided by a negative number. */
export const flipOp = (op) => ({ "<": ">", ">": "<", "≤": "≥", "≥": "≤" })[op];
/** The sign that includes or leaves out the end number: strictOp("≤") → "<". */
export const strictOp = (op) => ({ "<": "<", ">": ">", "≤": "<", "≥": ">" })[op];
export const looseOp = (op) => ({ "<": "≤", ">": "≥", "≤": "≤", "≥": "≥" })[op];
/** In words: "less than", "greater than or equal to", … */
export const opWords = (op) => ({ "<": "less than", ">": "greater than", "≤": "less than or equal to", "≥": "greater than or equal to" })[op];
/** The whole numbers from lo to hi that satisfy x op k, as a list ("−1, 0, 1, 2"), or "none". */
export function solutionsIn(lo, hi, op, k) {
  const out = [];
  for (let x = lo; x <= hi; x++) if (holds(x, op, k)) out.push(fmt(x));
  return out.length ? out.join(", ") : "none";
}

// ---------------------------------------------------------------- SVG
// Same drawing style as the other subjects: role="img", a label that does NOT give the answer, page colours.
const r1 = (x) => Math.round(x * 10) / 10;
const svg = (w, h, label, body) =>
  `<svg class="fig" viewBox="0 0 ${w} ${h}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg" ` +
  `font-family="system-ui, sans-serif" font-size="11" fill="none" stroke="currentColor" stroke-width="1">${body}</svg>`;
const line = (x1, y1, x2, y2, extra = "") => `<line x1="${r1(x1)}" y1="${r1(y1)}" x2="${r1(x2)}" y2="${r1(y2)}"${extra}/>`;
const text = (x, y, s, extra = "") =>
  `<text x="${r1(x)}" y="${r1(y)}" fill="currentColor" stroke="none"${/text-anchor/.test(extra) ? "" : ` text-anchor="middle"`}${extra}>${s}</text>`;
const dot = (x, y, r = 4) => `<circle cx="${r1(x)}" cy="${r1(y)}" r="${r}" fill="currentColor"/>`;

/**
 * A coordinate plane from −5 to 5 on both axes, with lettered points: points is a list of [letter, x, y].
 * The axes are labelled x and y and the origin O; every whole number is marked on both axes.
 */
export function coordPlane(points) {
  const N = 5, S = 26, c = 16 + N * S;
  const X = (x) => c + x * S, Y = (y) => c - y * S;
  let body = "";
  for (let i = -N; i <= N; i++) {
    body += line(X(i), Y(-N), X(i), Y(N), ` stroke-opacity="0.25"`) + line(X(-N), Y(i), X(N), Y(i), ` stroke-opacity="0.25"`);
    if (i !== 0) body += text(X(i), Y(0) + 13, fmt(i), ` font-size="9"`) + text(X(0) - 4, Y(i) + 3, fmt(i), ` font-size="9" text-anchor="end"`);
  }
  body += line(X(-N) - 8, Y(0), X(N) + 8, Y(0), ` stroke-width="1.5"`) + line(X(0), Y(-N) - 8, X(0), Y(N) + 8, ` stroke-width="1.5"`);
  body += text(X(N) + 10, Y(0) - 5, "x", ` font-style="italic"`) + text(X(0) + 9, Y(N) - 2, "y", ` font-style="italic"`) + text(X(0) - 7, Y(0) + 13, "O");
  for (const [name, x, y] of points) {
    if (Math.abs(x) > N || Math.abs(y) > N) throw new RangeError(`coordPlane: ${name} at ${x}, ${y} is off the grid`);
    body += dot(X(x), Y(y), 3.5) + text(X(x) + 7, Y(y) - 6, name, ` text-anchor="start" font-weight="bold" font-size="12"`);
  }
  return svg(2 * c + 6, 2 * c, "A coordinate plane with lettered points", body);
}

/** A number line of whole numbers from lo to hi (at most 16 marks) with lettered points: marks is a list of [letter, value]. */
export function numberLine(lo, hi, marks) {
  if (hi - lo > 16) throw new RangeError("numberLine: too many marks");
  const S = 300 / (hi - lo), x0 = 20, y = 34;
  const X = (v) => x0 + (v - lo) * S;
  let body = line(X(lo) - 10, y, X(hi) + 10, y, ` stroke-width="1.5"`);
  for (let v = lo; v <= hi; v++) body += line(X(v), y - 5, X(v), y + 5) + text(X(v), y + 19, fmt(v), ` font-size="10"`);
  for (const [name, v] of marks) {
    if (v < lo || v > hi) throw new RangeError(`numberLine: ${name} is off the line`);
    body += dot(X(v), y, 4) + text(X(v), y - 10, name, ` font-weight="bold" font-size="12"`);
  }
  return svg(340, 62, "A number line with lettered points", body);
}

/**
 * The solutions of x op k on a number line from k − 5 to k + 5: a filled circle when k is included (≤, ≥), an open
 * one when it is not (<, >), and a thick line with an arrow towards the solutions.
 */
export function ineqLine(op, k) {
  if (!OPS[op]) throw new RangeError(`unknown inequality sign ${op}`);
  const lo = k - 5, hi = k + 5, S = 28, x0 = 22, y = 30;
  const X = (v) => x0 + (v - lo) * S;
  let body = line(X(lo) - 10, y, X(hi) + 10, y);
  for (let v = lo; v <= hi; v++) body += line(X(v), y - 4, X(v), y + 4) + text(X(v), y + 18, fmt(v), ` font-size="10"`);
  const right = op === ">" || op === "≥", end = right ? X(hi) + 12 : X(lo) - 12;
  body += line(X(k), y, end, y, ` stroke-width="4"`);
  body += right ? `<path d="M${r1(end + 8)} ${y} l-10 -6 v12 z" fill="currentColor" stroke="none"/>` : `<path d="M${r1(end - 8)} ${y} l10 -6 v12 z" fill="currentColor" stroke="none"/>`;
  body += `<circle cx="${r1(X(k))}" cy="${y}" r="6" stroke-width="2"${op === "≤" || op === "≥" ? ` fill="currentColor"` : ` fill="#fff" style="fill: var(--card, #fff)"`}/>`;
  return svg(X(hi) + 32, 56, "A number line with a set of numbers shaded", body);
}

/**
 * Segment [AB] with its perpendicular bisector (Δ) through the midpoint M, and a point P on (Δ) joined to A and B.
 * `pa` is written on [PA]; [PB] is labelled with `pbLabel` (a number or "?").
 */
export function bisectorFig(pa, pbLabel) {
  const A = [50, 150], B = [250, 150], M = [150, 150], P = [150, 40];
  let body = line(A[0], A[1], B[0], B[1], ` stroke-width="2"`) + dot(A[0], A[1], 3) + dot(B[0], B[1], 3) + dot(M[0], M[1], 3);
  body += line(150, 18, 150, 185, ` stroke-dasharray="6 4"`) + text(160, 22, "(Δ)", ` text-anchor="start"`);
  body += `<path d="M150 140 h10 v10" stroke-width="1"/>`;
  body += line(P[0], P[1], A[0], A[1]) + line(P[0], P[1], B[0], B[1]) + dot(P[0], P[1], 3);
  body += line(95, 152, 95, 148) + line(97, 155, 97, 145) + line(205, 155, 205, 145) + line(203, 155, 203, 145);
  body += text(A[0] - 10, A[1] + 4, "A", ` font-weight="bold"`) + text(B[0] + 10, B[1] + 4, "B", ` font-weight="bold"`) +
    text(M[0] + 8, M[1] + 16, "M", ` font-weight="bold"`) + text(P[0] - 10, P[1] - 4, "P", ` font-weight="bold"`);
  body += text(88, 88, `${typeof pa === "number" ? fmt(pa) : pa} cm`, ` text-anchor="end"`) + text(212, 88, `${typeof pbLabel === "number" ? fmt(pbLabel) : pbLabel}${pbLabel === "?" ? "" : " cm"}`, ` text-anchor="start"`);
  return svg(300, 195, "A segment AB, its perpendicular bisector and a point P on it", body);
}

/** Segment [AB] with a point M on it; the two parts are labelled (a number, or "?"). */
export function segmentFig(am, mb) {
  const lab = (v) => (typeof v === "number" ? `${fmt(v)} cm` : v);
  let body = line(30, 40, 290, 40, ` stroke-width="2"`) + dot(30, 40, 3) + dot(290, 40, 3) + dot(160, 40, 3);
  body += text(30, 26, "A", ` font-weight="bold"`) + text(160, 26, "M", ` font-weight="bold"`) + text(290, 26, "B", ` font-weight="bold"`);
  body += text(95, 60, lab(am)) + text(225, 60, lab(mb));
  return svg(320, 70, "A segment AB with a point M on it", body);
}
