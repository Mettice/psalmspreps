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

// ================================================================ Term 2 (2026-10-21)
// ---------------------------------------------------------------- angles and parallel lines
// Two parallel lines cut by a transversal. Angle positions: 0 top-left, 1 top-right, 2 bottom-left, 3 bottom-right
// at the upper crossing; 4–7 the same at the lower crossing. With the transversal leaning right, positions 0, 3, 4, 7
// all have the same size a; 1, 2, 5, 6 are 180 − a.
export const angleAt = (a, pos) => ([0, 3, 4, 7].includes(pos) ? a : 180 - a);
/** The name of the pair of angles at positions p and q (p ≠ q). */
export function anglePair(p, q) {
  const [x, y] = [Math.min(p, q), Math.max(p, q)];
  if (x < 4 && y < 4 || x >= 4) {
    const a = x % 4, b = y % 4;
    return a + b === 3 ? "vertically opposite" : "on a straight line";
  }
  if (x % 4 === y % 4) return "corresponding";
  if ((x === 2 && y === 5) || (x === 3 && y === 4)) return "alternate";
  if ((x === 2 && y === 4) || (x === 3 && y === 5)) return "co-interior";
  return "alternate exterior";
}
/** Whether the pair is equal (true) or adds up to 180° (false). */
export const pairEqual = (p, q) => angleAt(100, p) === angleAt(100, q);
const LETTERS = ["p", "q", "r", "s", "t", "u", "v", "w"];
export const angleLetter = (pos) => LETTERS[pos];
/**
 * Parallel lines and a transversal with the angle at posA marked `a°` and the angle at posX marked `x`
 * (or every angle lettered when posA is −1). The label does not give the answer.
 */
export function parallelFig(a, posA, posX) {
  const Y = [55, 135], cx = [140, 98], dx = 0.53;  // the transversal goes up to the right
  let body = line(20, Y[0], 300, Y[0], ` stroke-width="1.5"`) + line(20, Y[1], 300, Y[1], ` stroke-width="1.5"`);
  body += `<path d="M262 ${Y[0] - 4} l6 4 l-6 4" />` + `<path d="M262 ${Y[1] - 4} l6 4 l-6 4" />`;  // parallel marks
  body += line(cx[1] - 60 * dx * 2.2, Y[1] + 60, cx[0] + 60 * dx * 2.2, Y[0] - 60, ` stroke-width="1.5"`);
  const spot = (pos) => {
    const k = pos < 4 ? 0 : 1, q = pos % 4, x = cx[k], y = Y[k];
    const offs = [[-22, -9], [26, -9], [-26, 18], [22, 18]][q];
    return [x + offs[0], y + offs[1]];
  };
  for (let pos = 0; pos < 8; pos++) {
    const [x, y] = spot(pos);
    const lab = pos === posA ? `${a}°` : pos === posX ? "x" : posA === -1 ? LETTERS[pos] : "";
    if (lab) body += text(x, y, lab, ` font-size="13" font-weight="${pos === posX ? 700 : 400}"`);
  }
  return svg(320, 190, "Two parallel lines cut by a transversal, with marked angles", body);
}
/** Two straight lines crossing, with one angle a° and the angle to find marked x (pos: 1 next to it, 2 opposite). */
export function crossFig(a, pos) {
  const c = [160, 80], rad = (d) => (d * Math.PI) / 180, L = 110;
  const t = Math.max(25, Math.min(155, a));  // drawn angle (the size is written, so the drawing need only be close)
  let body = line(c[0] - L, c[1], c[0] + L, c[1], ` stroke-width="1.5"`);
  body += line(c[0] - L * Math.cos(rad(t)), c[1] + L * 0.7 * Math.sin(rad(t)), c[0] + L * Math.cos(rad(t)), c[1] - L * 0.7 * Math.sin(rad(t)), ` stroke-width="1.5"`);
  const mid = (d, r = 30) => [c[0] + r * Math.cos(rad(d)), c[1] - r * Math.sin(rad(d)) + 4];
  const [ax, ay] = mid(t / 2), [nx, ny] = mid(t + (180 - t) / 2), [ox, oy] = mid(180 + t / 2);
  body += text(ax + 6, ay, `${a}°`, ` font-size="13"`);
  body += pos === 1 ? text(nx, ny, "x", ` font-size="13" font-weight="700"`) : text(ox - 4, oy + 4, "x", ` font-size="13" font-weight="700"`);
  return svg(320, 160, "Two straight lines crossing, with marked angles", body);
}

// ---------------------------------------------------------------- triangles
/** A triangle ABC with its angles written (a number, or "x"); shape is generic, sizes are written. */
export function triangleFig(A, B, C) {
  const P = [[40, 170], [280, 170], [150, 30]];
  let body = `<path d="M${P[0]} L${P[1]} L${P[2]} Z" stroke-width="1.5"/>`;
  body += text(28, 186, "A", ` font-weight="bold"`) + text(292, 186, "B", ` font-weight="bold"`) + text(150, 20, "C", ` font-weight="bold"`);
  const lab = (v) => (typeof v === "number" ? `${fmt(v)}°` : v);
  body += text(78, 162, lab(A), ` font-size="13"`) + text(240, 162, lab(B), ` font-size="13"`) + text(150, 62, lab(C), ` font-size="13"`);
  return svg(320, 195, "A triangle ABC with marked angles", body);
}
/** A right-angled triangle with legs a, b and hypotenuse c; each is a number or "?" / a letter. */
export function rightTriFig(a, b, c, unit = "cm") {
  const lab = (v) => (typeof v === "number" ? `${fmt(v)} ${unit}` : v);
  let body = `<path d="M40 160 L260 160 L40 40 Z" stroke-width="1.5"/>` + `<path d="M40 148 h12 v12" />`;
  body += text(150, 178, lab(a)) + text(32, 104, lab(b), ` text-anchor="end"`) + text(162, 92, lab(c), ` text-anchor="start"`);
  return svg(300, 190, "A right-angled triangle with marked sides", body);
}
/** Integral Pythagorean triples (legs, hypotenuse), as the syllabus asks. */
export const TRIPLES = [[3, 4, 5], [6, 8, 10], [5, 12, 13], [9, 12, 15], [8, 15, 17], [12, 16, 20], [7, 24, 25], [15, 20, 25], [10, 24, 26], [20, 21, 29], [9, 40, 41], [12, 35, 37]];
export const triple = (i) => TRIPLES[i % TRIPLES.length];
export const nTriples = () => TRIPLES.length;
export const isRightTriangle = (a, b, c) => { const s = [a, b, c].sort((x, y) => x - y); return s[0] ** 2 + s[1] ** 2 === s[2] ** 2; };

// ---------------------------------------------------------------- fractions (answers typed as a/b or as a mixed number)
const gcd = (a, b) => { a = Math.abs(a); b = Math.abs(b); while (b) [a, b] = [b, a % b]; return a || 1; };
/** a/b in lowest terms, "3/4", a whole number when the denominator is 1, "−1/2" for negatives. */
export function frac(n, d) {
  if (d === 0) throw new RangeError("frac: zero denominator");
  if (d < 0) { n = -n; d = -d; }
  const g = gcd(n, d), p = n / g, q = d / g;
  return q === 1 ? fmt(p) : `${p < 0 ? MINUS : ""}${Math.abs(p)}/${q}`;
}
export const fracRaw = (n, d) => `${n}/${d}`;  // as written, not simplified
/** "1 3/4" for 7/4; a proper fraction or a whole number as it is. */
export function mixed(n, d) {
  const g = gcd(n, d); n /= g; d /= g;
  if (d === 1 || Math.abs(n) < d) return frac(n, d);
  const w = Math.trunc(n / d), r = Math.abs(n % d);
  return `${fmt(w)} ${r}/${d}`;
}
export const fAddN = (a, b, c, d) => a * d + c * b;
export const fAddD = (a, b, c, d) => b * d;
export const fAdd = (a, b, c, d) => frac(a * d + c * b, b * d);
export const fSub = (a, b, c, d) => frac(a * d - c * b, b * d);
export const fMul = (a, b, c, d) => frac(a * c, b * d);
export const fDiv = (a, b, c, d) => frac(a * d, b * c);
export const lcmOf = (a, b) => (a / gcd(a, b)) * b;
/** Wrong on purpose: tops added and bottoms added (1/2 + 1/3 = 2/5). */
export const fAddWrong = (a, b, c, d) => frac(a + c, b + d);
/** Wrong on purpose: the first fraction divided by the second without turning it upside down. */
export const fDivWrong = (a, b, c, d) => frac(a * c, b * d);

// ---------------------------------------------------------------- rounding and significant figures
/** x rounded to the nearest `unit` (10, 100, 0.1 …). */
export const roundTo = (x, unit) => Number((Math.round(x / unit) * unit).toFixed(10));
/** x to k significant figures, as a number. */
export function sigFig(x, k) {
  if (x === 0) return 0;
  const e = Math.floor(Math.log10(Math.abs(x))), f = 10 ** (k - 1 - e);
  return Number((Math.round(x * f) / f).toFixed(Math.max(0, k - 1 - e)));
}
/** x to k significant figures, written with any zeros that count ("0.0500", "3.0"). */
export function sigFigStr(x, k) {
  const v = sigFig(x, k), e = Math.floor(Math.log10(Math.abs(v)));
  return fmt(v).includes(".") || k - 1 - e <= 0 ? v.toFixed(Math.max(0, k - 1 - e)) : v.toFixed(Math.max(0, k - 1 - e));
}
/** The number of significant figures of a decimal written as a string ("0.0305" → 3, "4500" → 2, "4.50" → 3). */
export function countSig(s) {
  s = String(s).replace("−", "").replace("-", "");
  if (s.includes(".")) return s.replace(".", "").replace(/^0+/, "").length;
  return s.replace(/^0+/, "").replace(/0+$/, "").length;
}
/** Decimals without floating-point noise: 0.1 + 0.2 = 0.3. */
export const dec = (x) => Number(x.toFixed(10));

// ---------------------------------------------------------------- real numbers and intervals
export const isPerfectSquare = (n) => Number.isInteger(n) && n >= 0 && Math.round(Math.sqrt(n)) ** 2 === n;
/** √n written with the root sign; its value when n is a perfect square. */
export const root = (n) => `√${n}`;
export const sqrtInt = (n) => Math.round(Math.sqrt(n));
/** An interval in the notation of the lesson (TR-N20): [a, b], (a, b), [a, b), (a, b], [a, +∞), (−∞, b] … */
// An infinite end is written null, or 'inf' / '-inf' in content (the expression language has no null).
const isInf = (v) => v === null || v === "inf" || v === "-inf";
export function interval(a, b, closedA, closedB) {
  const L = isInf(a) ? "(" : closedA ? "[" : "(", R = isInf(b) ? ")" : closedB ? "]" : ")";
  return `${L}${isInf(a) ? "−∞" : fmt(a)}, ${isInf(b) ? "+∞" : fmt(b)}${R}`;
}
/** The same set as an inequality in x: "−2 ≤ x < 5", "x ≥ 3". */
export function intervalIneq(a, b, closedA, closedB) {
  if (isInf(a)) return `x ${closedB ? "≤" : "<"} ${fmt(b)}`;
  if (isInf(b)) return `x ${closedA ? "≥" : ">"} ${fmt(a)}`;
  return `${fmt(a)} ${closedA ? "≤" : "<"} x ${closedB ? "≤" : "<"} ${fmt(b)}`;
}
export const inInterval = (x, a, b, closedA, closedB) =>
  (isInf(a) || (closedA ? x >= a : x > a)) && (isInf(b) || (closedB ? x <= b : x < b));
/** Whole numbers in a finite interval, listed. */
export function intsIn(a, b, closedA, closedB) {
  const out = [];
  for (let x = Math.ceil(a); x <= Math.floor(b); x++) if (inInterval(x, a, b, closedA, closedB)) out.push(x);
  return out;
}

// ---------------------------------------------------------------- money: percentages, interest, exchange
export const pctOf = (p, x) => dec((p * x) / 100);
export const pctChange = (from, to) => dec(((to - from) / from) * 100);
/** Simple interest I = P × R × T ÷ 100. */
export const simpleInterest = (P, R, T) => dec((P * R * T) / 100);
/** Amount after n years at r% compound interest (the syllabus stops at two years). */
export const compound = (P, r, n) => { let A = P; for (let i = 0; i < n; i++) A = dec(A + (A * r) / 100); return A; };

// ---------------------------------------------------------------- polygons
const POLY = { 3: "triangle", 4: "quadrilateral", 5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon", 9: "nonagon", 10: "decagon", 12: "dodecagon" };
export const polyName = (n) => POLY[n];
export const angleSum = (n) => (n - 2) * 180;
export const interiorRegular = (n) => dec(((n - 2) * 180) / n);
export const exteriorRegular = (n) => dec(360 / n);
/** A regular polygon with n sides (drawn), labelled with nothing that gives an answer away. */
export function regularFig(n) {
  const c = 90, r = 70, pts = Array.from({ length: n }, (_, i) => {
    const t = -Math.PI / 2 + (2 * Math.PI * i) / n;
    return `${r1(c + 30 + r * Math.cos(t))},${r1(c + r * Math.sin(t))}`;
  });
  return svg(240, 180, `A regular polygon with ${n} sides`, `<polygon points="${pts.join(" ")}" stroke-width="1.5"/>`);
}
/** A trapezium with parallel sides a (bottom) and b (top) and height h, written on the figure. */
export function trapeziumFig(a, b, h) {
  let body = `<path d="M30 150 L290 150 L220 50 L90 50 Z" stroke-width="1.5"/>` + line(90, 50, 90, 150, ` stroke-dasharray="4 3"`) + `<path d="M90 140 h10 v10"/>`;
  body += text(160, 168, `${fmt(a)} cm`) + text(155, 42, `${fmt(b)} cm`) + text(84, 104, `${fmt(h)} cm`, ` text-anchor="end"`);
  return svg(320, 180, "A trapezium with its parallel sides and height marked", body);
}
/** A parallelogram with base b and height h written on the figure. */
export function parallelogramFig(b, h) {
  let body = `<path d="M30 150 L230 150 L290 50 L90 50 Z" stroke-width="1.5"/>` + line(90, 50, 90, 150, ` stroke-dasharray="4 3"`) + `<path d="M90 140 h10 v10"/>`;
  body += text(130, 168, `${fmt(b)} cm`) + text(84, 104, `${fmt(h)} cm`, ` text-anchor="end"`);
  return svg(320, 180, "A parallelogram with its base and height marked", body);
}

// ---------------------------------------------------------------- symmetry
/** Reflection of (x, y) in the line x = k (vertical) or y = k (horizontal). */
export const reflectX = (x, k) => 2 * k - x;
/** Point symmetry (half turn) about (a, b): (x, y) → (2a − x, 2b − y). */
export const halfTurn = (v, c) => 2 * c - v;
/** Lines of symmetry of a regular polygon with n sides (n), of some common shapes (authored, TR-N21). */
const SYM_LINES = { square: 4, rectangle: 2, rhombus: 2, parallelogram: 0, "isosceles trapezium": 1, kite: 1, "equilateral triangle": 3, "isosceles triangle": 1, "scalene triangle": 0, circle: "infinitely many" };
export const symLines = (shape) => SYM_LINES[shape];
export const symShapes = () => Object.keys(SYM_LINES);
const POINT_SYM = { square: true, rectangle: true, rhombus: true, parallelogram: true, "isosceles trapezium": false, kite: false, "equilateral triangle": false, "isosceles triangle": false, "scalene triangle": false, circle: true };
export const hasPointSym = (shape) => POINT_SYM[shape];

// ---------------------------------------------------------------- circles
/** The relative position of two circles with radii r1, r2 and distance d between centres. */
export function circlesPos(r1_, r2, d) {
  const big = r1_ + r2, small = Math.abs(r1_ - r2);
  if (d === 0) return r1_ === r2 ? "the same circle" : "concentric";
  if (d > big) return "separate (outside each other)";
  if (d === big) return "touching externally";
  if (d > small) return "intersecting in two points";
  if (d === small) return "touching internally";
  return "one inside the other";
}
export const CIRCLE_POSITIONS = ["separate (outside each other)", "touching externally", "intersecting in two points", "touching internally", "one inside the other", "concentric"];
export const otherPositions = (p) => CIRCLE_POSITIONS.filter((x) => x !== p);
export const tA = (i) => triple(i)[0];
export const tB = (i) => triple(i)[1];
export const tC = (i) => triple(i)[2];
/** The whole number just below √n. */
export const sqrtFloor = (n) => Math.floor(Math.sqrt(n) + 1e-9);
/** The smallest of ℕ, ℤ, ℚ, ℝ a number belongs to (kind: "nat", "int", "rat", "irr"). */
export const smallestSet = (kind) => ({ nat: "ℕ", int: "ℤ", rat: "ℚ", irr: "ℝ" })[kind];
export const sqrt = (x) => Math.sqrt(x);
/** The pair named for a sentence: "corresponding angles", "angles on a straight line" … */
export const pairPhrase = (p, q) => (anglePair(p, q) === "on a straight line" ? "angles on a straight line" : `${anglePair(p, q)} angles`);
/** a/b is already in lowest terms. */
export const isLowest = (a, b) => gcd(a, b) === 1;
/** "a hexagon", "an octagon", "an isosceles triangle". */
export const aOrAn = (w) => `${/^[aeiou]/i.test(String(w)) ? "an" : "a"} ${w}`;

// ================================================================ Term 3 (2026-10-21): solids and statistics
// ---------------------------------------------------------------- right prisms and regular pyramids
/** A right prism whose base has n sides: n + 2 faces (n lateral), 3n edges, 2n vertices. */
export const prismFaces = (n) => n + 2;
export const prismEdges = (n) => 3 * n;
export const prismVertices = (n) => 2 * n;
/** A pyramid whose base has n sides: n + 1 faces (n triangles), 2n edges, n + 1 vertices. */
export const pyramidFaces = (n) => n + 1;
export const pyramidEdges = (n) => 2 * n;
export const pyramidVertices = (n) => n + 1;
const BASE_NAMES = { 3: "triangular", 5: "pentagonal", 6: "hexagonal", 8: "octagonal" };
/** The name of an n-sided base: "triangular", "square" (pyramid) or "rectangular" (prism), "pentagonal", "hexagonal". */
export const baseName = (n, solid) => (n === 4 ? (solid === "pyramid" ? "square" : "rectangular") : BASE_NAMES[n]);
/** Lateral area of a right prism = perimeter of the base × height. */
export const lateralArea = (perimeter, h) => dec(perimeter * h);
/** Total surface area = lateral area + 2 × base area. */
export const prismTotalArea = (perimeter, h, baseArea) => dec(perimeter * h + 2 * baseArea);
/** Volume of a right prism = base area × height. */
export const prismVolume = (baseArea, h) => dec(baseArea * h);
/** Surface area of a square-based pyramid: base² + 4 × ½ × base × slant height. */
export const sqPyramidArea = (b, slant) => dec(b * b + 2 * b * slant);

// ---------------------------------------------------------------- spheres (π = 3.14)
export const sphereArea = (r) => dec(4 * 3.14 * r * r);
export const sphereVolume = (r) => dec((4 * 3.14 * r * r * r) / 3);

// ---------------------------------------------------------------- statistics
export const sorted = (list) => [...list].sort((a, b) => a - b);
export const listStr = (list) => list.map(fmt).join(", ");
export const meanOf = (list) => dec(list.reduce((a, b) => a + b, 0) / list.length);
export function medianOf(list) {
  const s = sorted(list), n = s.length;
  return n % 2 ? s[(n - 1) / 2] : dec((s[n / 2 - 1] + s[n / 2]) / 2);
}
/** The single most frequent value, or "none" when two or more values tie for most frequent. */
export function modeOf(list) {
  const c = new Map();
  for (const x of list) c.set(x, (c.get(x) || 0) + 1);
  const top = Math.max(...c.values()), best = [...c].filter(([, k]) => k === top).map(([x]) => x);
  return best.length === 1 ? best[0] : "none";
}
export const rangeOf = (list) => Math.max(...list) - Math.min(...list);
/** Mean of a frequency table: Σ(x × f) ÷ Σf. */
export const freqMean = (xs, fs) => dec(xs.reduce((a, x, i) => a + x * fs[i], 0) / fs.reduce((a, f) => a + f, 0));
export const freqTotal = (fs) => fs.reduce((a, f) => a + f, 0);
export const freqSumXF = (xs, fs) => xs.reduce((a, x, i) => a + x * fs[i], 0);
/** The value with the highest frequency (the first if two tie). */
export const freqMode = (xs, fs) => xs[fs.indexOf(Math.max(...fs))];
/** True when one value alone has the highest frequency. */
export const freqModeUnique = (fs) => fs.filter((f) => f === Math.max(...fs)).length === 1;
/** Pie-chart angle of a part: frequency ÷ total × 360°. */
export const pieAngle = (f, total) => dec((f / total) * 360);
/** How many times each value occurs in the list, in the order of xs. */
export const countEach = (list, xs) => xs.map((x) => list.filter((y) => y === x).length);

// ---------------------------------------------------------------- figures
const PRISM_BASES = {
  3: [[40, 150], [170, 150], [110, 112]],
  4: [[40, 152], [170, 152], [210, 122], [80, 122]],
  5: [[60, 156], [150, 156], [182, 128], [105, 106], [28, 128]],
  6: [[70, 156], [150, 156], [190, 132], [150, 108], [70, 108], [30, 132]],
};
// Base edges (start vertex index) and vertical edges hidden from view, per base size.
const HIDDEN = { 3: { edges: [1, 2], verts: [2] }, 4: { edges: [2, 3], verts: [3] }, 5: { edges: [2, 3], verts: [3] }, 6: { edges: [3, 4], verts: [4] } };
/** A right prism with an n-sided base (3, 4, 5 or 6) in oblique view; hidden edges are dashed. */
export function prismFig(n) {
  const base = PRISM_BASES[n], top = base.map(([x, y]) => [x, y - 80]), hid = HIDDEN[n];
  let body = "";
  base.forEach(([x, y], i) => { const [x2, y2] = base[(i + 1) % n]; body += line(x, y, x2, y2, hid.edges.includes(i) ? ` stroke-dasharray="4 3"` : ` stroke-width="1.5"`); });
  top.forEach(([x, y], i) => { const [x2, y2] = top[(i + 1) % n]; body += line(x, y, x2, y2, ` stroke-width="1.5"`); });
  base.forEach(([x, y], i) => { body += line(x, y, top[i][0], top[i][1], hid.verts.includes(i) ? ` stroke-dasharray="4 3"` : ` stroke-width="1.5"`); });
  return svg(240, 175, `A right prism with a ${n}-sided base`, body);
}
/** A regular pyramid with an n-sided base (3, 4, 5 or 6), apex above the centre; hidden edges are dashed. */
export function pyramidFig(n) {
  const base = PRISM_BASES[n], hid = HIDDEN[n];
  const cx = base.reduce((a, p) => a + p[0], 0) / n, apex = [cx, 22];
  let body = "";
  base.forEach(([x, y], i) => { const [x2, y2] = base[(i + 1) % n]; body += line(x, y, x2, y2, hid.edges.includes(i) ? ` stroke-dasharray="4 3"` : ` stroke-width="1.5"`); });
  base.forEach(([x, y], i) => { body += line(x, y, apex[0], apex[1], hid.verts.includes(i) ? ` stroke-dasharray="4 3"` : ` stroke-width="1.5"`); });
  body += dot(apex[0], apex[1], 2.5);
  return svg(240, 175, `A pyramid with a ${n}-sided base`, body);
}
/** A sphere with its centre O and a radius of r cm marked. */
export function sphereFig(r) {
  const body = `<circle cx="110" cy="90" r="70" stroke-width="1.5"/><ellipse cx="110" cy="90" rx="70" ry="18" stroke-dasharray="4 3"/>` +
    dot(110, 90, 2.5) + text(104, 86, "O", ` text-anchor="end"`) + line(110, 90, 180, 90) + text(145, 84, `${fmt(r)} cm`);
  return svg(220, 180, "A sphere with its centre and a radius marked", body);
}
/** A bar chart of whole-number values (up to 6 bars) with a scale on the left. */
export function barChartFig(labels, values) {
  const n = labels.length, max = Math.max(...values), step = max <= 10 ? 2 : max <= 20 ? 5 : 10, top = Math.ceil(max / step) * step;
  const X0 = 40, Y0 = 160, H = 130, W = 270, bw = W / n;
  let body = line(X0, Y0, X0 + W, Y0) + line(X0, Y0, X0, Y0 - H - 5);
  for (let v = 0; v <= top; v += step) {
    const y = Y0 - (v / top) * H;
    body += line(X0 - 4, y, X0, y) + text(X0 - 6, y + 4, fmt(v), ` text-anchor="end"`) + (v ? line(X0, y, X0 + W, y, ` stroke-dasharray="2 4" stroke-width="0.5"`) : "");
  }
  labels.forEach((l, i) => {
    const h = (values[i] / top) * H, x = X0 + i * bw + bw * 0.2;
    body += `<rect x="${r1(x)}" y="${r1(Y0 - h)}" width="${r1(bw * 0.6)}" height="${r1(h)}" fill="currentColor" fill-opacity="0.25" stroke-width="1.2"/>` + text(x + bw * 0.3, Y0 + 14, l);
  });
  return svg(330, 180, "A bar chart", body);
}
/** A pie chart with labelled sectors (the angles are not written). */
export function pieFig(labels, values) {
  const total = values.reduce((a, b) => a + b, 0), cx = 130, cy = 105, R = 66;
  let a = -Math.PI / 2, body = `<circle cx="${cx}" cy="${cy}" r="${R}" stroke-width="1.5"/>`;
  labels.forEach((l, i) => {
    const t = (values[i] / total) * 2 * Math.PI, m = a + t / 2;
    body += line(cx, cy, cx + R * Math.cos(a), cy + R * Math.sin(a)) + text(cx + (R + 24) * Math.cos(m), cy + (R + 24) * Math.sin(m) + 4, l);
    a += t;
  });
  return svg(260, 210, "A pie chart", body);
}

// ---------------------------------------------------------------- Form 3 (2026-10-23): trigonometry, logarithms, matrices
const RAD = Math.PI / 180;
/** Trigonometric ratios of an angle in degrees, and the inverse ratios in degrees. */
export const sinD = (x) => Math.sin(x * RAD);
export const cosD = (x) => Math.cos(x * RAD);
export const tanD = (x) => Math.tan(x * RAD);
export const asinD = (r) => Math.asin(r) / RAD;
export const acosD = (r) => Math.acos(r) / RAD;
export const atanD = (r) => Math.atan(r) / RAD;
/** Logarithms: log10(1000) = 3; logb(2, 8) = 3 (exact for exact powers). */
export const log10 = (x) => Math.log10(x);
export const logb = (b, x) => { const v = Math.log(x) / Math.log(b), r = Math.round(v); return Math.abs(v - r) < 1e-9 ? r : v; };
/** 2 × 2 matrices as [[a, b], [c, d]]. */
export const det2 = (m) => m[0][0] * m[1][1] - m[0][1] * m[1][0];
export const matAdd = (p, q) => p.map((r, i) => r.map((v, j) => v + q[i][j]));
export const matSub = (p, q) => p.map((r, i) => r.map((v, j) => v - q[i][j]));
export const matScale = (k, p) => p.map((r) => r.map((v) => k * v));
export const matMul = (p, q) => p.map((r) => q[0].map((_, j) => r.reduce((s, v, k) => s + v * q[k][j], 0)));
export const matT = (p) => p[0].map((_, j) => p.map((r) => r[j]));
/** The adjoint (adjugate) of a 2 × 2 matrix: swap the leading diagonal, change the signs of the other. */
export const adj2 = (m) => [[m[1][1], -m[0][1]], [-m[1][0], m[0][0]]];
/** A matrix written on one line, rows separated by semicolons: "(2  3 ; 1  4)". */
export const matStr = (m) => `(${m.map((r) => r.map(fmt).join("  ")).join(" ; ")})`;
/**
 * Named matrices drawn with brackets: matFig([["A", [[2, 3], [1, 4]]], ["B", [[0, 1], [5, 2]]]]).
 * Any size up to 3 × 3; entries are written with fmt.
 */
export function matFig(named) {
  const cw = 34, rh = 22;
  let x = 10, body = "", h = 0;
  for (const [name, m] of named) {
    const rows = m.length, cols = m[0].length, H = rows * rh + 8, W = cols * cw;
    h = Math.max(h, H + 10);
    body += text(x + 12, 10 + H / 2 + 4, `${name} =`, ` text-anchor="middle"`);
    const bx = x + 30;
    body += `<path d="M${bx + 6} 10 q-6 ${H / 2} 0 ${H}" stroke-width="1.3"/><path d="M${bx + W + 6} 10 q6 ${H / 2} 0 ${H}" stroke-width="1.3"/>`;
    m.forEach((r, i) => r.forEach((v, j) => { body += text(bx + 6 + cw * j + cw / 2, 10 + 4 + rh * i + rh / 2 + 4, fmt(v)); }));
    x = bx + W + 30;
  }
  return svg(Math.max(x, 120), h + 10, `Matrices ${named.map(([n]) => n).join(" and ")}`, body);
}
/**
 * A right-angled triangle for trigonometry: the right angle at the bottom left, the marked angle θ at the bottom right.
 * base (adjacent), height (opposite), hyp: a number (with unit), a letter, or "" to leave the side blank.
 */
export function trigFig(base, height, hyp, angle = "θ", unit = "cm") {
  const lab = (v) => (typeof v === "number" ? `${fmt(v)} ${unit}` : v);
  // room on the left for a word label ("opposite") beside the vertical side
  let body = `<path d="M90 160 L310 160 L90 40 Z" stroke-width="1.5"/><path d="M90 148 h12 v12"/>`;
  body += `<path d="M278 160 A32 32 0 0 0 281.9 144.7"/>` + text(262, 154, typeof angle === "number" ? `${fmt(angle)}°` : angle);
  body += text(200, 178, lab(base)) + text(82, 104, lab(height), ` text-anchor="end"`) + text(212, 92, lab(hyp), ` text-anchor="start"`);
  return svg(340, 190, "A right-angled triangle with a marked angle", body);
}
/**
 * Thales (intercept theorem): triangle ABC (A at the top) cut by DE parallel to BC, D on AB and E on AC.
 * Each length is a number (cm), a letter, or "" to leave it unmarked: thalesFig(AD, DB, AE, EC, DE, BC).
 */
export function thalesFig(ad, db, ae, ec, de, bc, unit = "cm") {
  const lab = (v) => (typeof v === "number" ? `${fmt(v)} ${unit}` : v);
  const A = [170, 24], B = [40, 176], C = [300, 176], t = 0.45, D = [A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t], E = [A[0] + (C[0] - A[0]) * t, A[1] + (C[1] - A[1]) * t];
  let body = `<path d="M${A} L${B} L${C} Z" stroke-width="1.5"/>` + line(D[0], D[1], E[0], E[1], ` stroke-width="1.5"`);
  body += [["A", A, 0, -8], ["B", B, -10, 12], ["C", C, 10, 12], ["D", D, -12, 2], ["E", E, 12, 2]].map(([n, P, dx, dy]) => text(P[0] + dx, P[1] + dy, n, ` font-weight="bold"`)).join("");
  body += text((A[0] + D[0]) / 2 - 14, (A[1] + D[1]) / 2, lab(ad), ` text-anchor="end"`) + text((D[0] + B[0]) / 2 - 14, (D[1] + B[1]) / 2, lab(db), ` text-anchor="end"`);
  body += text((A[0] + E[0]) / 2 + 14, (A[1] + E[1]) / 2, lab(ae), ` text-anchor="start"`) + text((E[0] + C[0]) / 2 + 14, (E[1] + C[1]) / 2, lab(ec), ` text-anchor="start"`);
  body += text((D[0] + E[0]) / 2, D[1] - 6, lab(de)) + text(170, 192, lab(bc));
  return svg(340, 200, "Triangle ABC with DE parallel to BC", body);
}

// ---------------------------------------------------------------- Form 4 algebra and surds (2026-10-24)
/** The largest k with k² dividing n: √n = k√(n ÷ k²). */
export function surdOut(n) { let k = 1; for (let i = 2; i * i <= n; i++) if (n % (i * i) === 0) k = i; return k; }
/** What stays under the root: √12 → 3. */
export const surdIn = (n) => n / surdOut(n) ** 2;
/** √n in simplest form: 12 → "2√3", 9 → "3", 7 → "√7"; with a coefficient c: c√n simplified (c = 3, n = 8 → "6√2"). */
export function surd(n, c = 1) {
  const k = c * surdOut(n), m = surdIn(n);
  if (m === 1) return fmt(k);
  return `${k === 1 ? "" : k === -1 ? "−" : fmt(k)}√${m}`;
}
/** A product of two linear brackets: lin2(2, 3, 1, -4) → "(2x + 3)(x − 4)". */
export const lin2 = (a, b, c, d, v = "x") => `(${poly([a, v], [b, ""])})(${poly([c, v], [d, ""])})`;
/** ax² + bx + c, zero terms left out: quad(1, -5, 6) → "x² − 5x + 6". */
export const quad = (a, b, c, v = "x") => poly([a, `${v}²`], [b, v], [c, ""]);
