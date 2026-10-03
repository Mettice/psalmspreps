// Vetted functions that Maths content JSON may call from expressions.
// Everything here is pure and deterministic. Misconception helpers (marked "WRONG ON PURPOSE")
// reproduce a predictable pupil mistake so its answer can be recognised and explained.

const NBSP = " ";
const SUP = "⁰¹²³⁴⁵⁶⁷⁸⁹";
const SUB = "₀₁₂₃₄₅₆₇₈₉";

// ---------------------------------------------------------------- display
export function fmt(n) {
  if (typeof n !== "number") return String(n);
  if (!Number.isFinite(n)) return String(n);
  const neg = n < 0;
  const [int, frac] = String(Number(Math.abs(n).toFixed(9))).split(".");
  // House style (Dion, 2026-10-02): 4-digit numbers are not grouped (7750, 1948); 5+ digits are (12 500).
  const grouped = int.length > 4 ? int.replace(/\B(?=(\d{3})+(?!\d))/g, NBSP) : int;
  return (neg ? "−" : "") + grouped + (frac ? "." + frac : "");
}
export const sup = (n) => String(n).replace(/[0-9]/g, (d) => SUP[d]);
export const sub = (n) => String(n).replace(/[0-9]/g, (d) => SUB[d]);
export const str = (x) => String(x);
export const num = (s) => Number(s);
export const len = (x) => x.length;
export const reverse = (s) => String(s).split("").reverse().join("");
export const join = (list, sep) => list.join(sep);
export const upper = (s) => String(s).toUpperCase();

// ---------------------------------------------------------------- arithmetic
export const abs = Math.abs;
export const floor = Math.floor;
export const min = Math.min;
export const max = Math.max;
export const idiv = (a, b) => Math.floor(a / b);
export const round = (x, places = 0) => Number(x.toFixed(places));
export const isInt = (x) => Number.isInteger(x);
export const sum = (list) => list.reduce((a, b) => a + b, 0);
export const contains = (list, x) => list.includes(x);
export const distinct = (list) => new Set(list.map(String)).size === list.length;
export const inN = (x) => Number.isInteger(x) && x >= 0;
export const inNstar = (x) => Number.isInteger(x) && x >= 1;
export const plural = (k, one, many) => `${fmt(k)} ${k === 1 ? one : many}`;
export const pad = (n, width) => String(n).padStart(width, "0");
export const rep = (x, k) => Array.from({ length: k }, () => x);
/** Inclusive list a, a+1, ..., b. */
export const range = (a, b) => Array.from({ length: Math.max(0, b - a + 1) }, (_, i) => a + i);
/** Digit of a numeral string at position pos counted from the right (0 = units); 0 beyond its length. */
export const dig = (s, pos) => {
  s = String(s);
  return pos < s.length ? Number(s[s.length - 1 - pos]) : 0;
};

// ---------------------------------------------------------------- place value
const PLACES = ["units", "tens", "hundreds", "thousands", "ten thousands", "hundred thousands", "millions"];
export const placeName = (pos) => PLACES[pos];
export const numDigits = (n) => String(Math.abs(n)).length;
export const digitAt = (n, pos) => Math.floor(n / 10 ** pos) % 10;
export const placeValue = (n, pos) => digitAt(n, pos) * 10 ** pos;
/** Position (0 = units) of digit d in n, or -1. Only meaningful when d occurs once. */
export const posOf = (n, d) => {
  const s = String(n);
  const i = s.lastIndexOf(String(d));
  return i < 0 ? -1 : s.length - 1 - i;
};
export const countDigit = (n, d) => String(n).split(String(d)).length - 1;
/** Digits split into groups of `size`, from the right (correct for size 3) or from the left (a mistake). */
export function groupDigits(n, size, fromLeft = false) {
  const s = String(n), out = [];
  if (fromLeft) for (let i = 0; i < s.length; i += size) out.push(s.slice(i, i + size));
  else for (let i = s.length; i > 0; i -= size) out.unshift(s.slice(Math.max(0, i - size), i));
  return out.join(NBSP);
}
/** WRONG ON PURPOSE: forgets zero place holders, 40 307 -> 437. */
export const stripZeros = (n) => Number(String(n).replace(/0/g, "") || "0");

// ---------------------------------------------------------------- column arithmetic mistakes (Primary 6)
const digitsOf = (n, len) => String(n).padStart(len, "0").split("").map(Number);
/** WRONG ON PURPOSE: adds each column but never carries, 478 + 256 -> 624. */
export function addNoCarry(a, b) {
  const L = Math.max(String(a).length, String(b).length);
  const x = digitsOf(a, L), y = digitsOf(b, L);
  return Number(x.map((d, i) => (d + y[i]) % 10).join(""));
}
/** WRONG ON PURPOSE: in every column takes the smaller digit from the bigger, 503 - 168 -> 465. */
export function subSmallFromLarge(a, b) {
  const L = Math.max(String(a).length, String(b).length);
  const x = digitsOf(a, L), y = digitsOf(b, L);
  return Number(x.map((d, i) => Math.abs(d - y[i])).join(""));
}
/** WRONG ON PURPOSE: long multiplication by a 2-digit number without the zero in the second line, 123 × 45 -> 123×5 + 123×4. */
export const mulNoShift = (a, b) => a * (b % 10) + a * Math.floor(b / 10);

// ---------------------------------------------------------------- numbers in words (British usage)
const ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
  "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
const TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
function below100(n) {
  if (n < 20) return ONES[n];
  return TENS[Math.floor(n / 10)] + (n % 10 ? "-" + ONES[n % 10] : "");
}
function below1000(n) {
  const h = Math.floor(n / 100), r = n % 100;
  if (!h) return below100(r);
  return `${ONES[h]} hundred` + (r ? ` and ${below100(r)}` : "");
}
/** 2 405 012 -> "two million four hundred and five thousand and twelve". Up to 999 999 999. */
export function words(n) {
  if (!Number.isInteger(n) || n < 0 || n > 999_999_999) throw new RangeError(`words(${n})`);
  if (n === 0) return "zero";
  const m = Math.floor(n / 1e6), t = Math.floor(n / 1e3) % 1000, r = n % 1000;
  const parts = [];
  if (m) parts.push(`${below1000(m)} million`);
  if (t) parts.push(`${below1000(t)} thousand`);
  if (r) parts.push(r < 100 && parts.length ? `and ${below100(r)}` : below1000(r));
  return parts.join(" ");
}

/** Inverse of words(), written independently so tests can cross-check the two. NaN if not understood. */
export function fromWords(s) {
  const small = Object.fromEntries(ONES.map((w, i) => [w, i]));
  TENS.forEach((w, i) => { if (w) small[w] = i * 10; });
  let total = 0, current = 0, seen = false;
  for (const w of String(s).toLowerCase().replace(/-/g, " ").split(/\s+/).filter(Boolean)) {
    if (w === "and") continue;
    if (w in small) { current += small[w]; seen = true; }
    else if (w === "hundred") current *= 100;
    else if (w === "thousand") { total += current * 1000; current = 0; }
    else if (w === "million") { total += current * 1e6; current = 0; }
    else return NaN;
  }
  return seen ? total + current : NaN;
}

// ---------------------------------------------------------------- ordinals
export function ordinal(n) {
  const t = n % 100;
  const s = t >= 11 && t <= 13 ? "th" : ({ 1: "st", 2: "nd", 3: "rd" }[n % 10] || "th");
  return `${n}${s}`;
}

// ---------------------------------------------------------------- Roman and Egyptian numerals
const ROMAN = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"],
  [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]];
const ROMAN_ADD = [[1000, "M"], [500, "D"], [100, "C"], [50, "L"], [10, "X"], [5, "V"], [1, "I"]];
const SYMBOL = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
function toRoman(n, table) {
  if (!Number.isInteger(n) || n < 1 || n > 3999) throw new RangeError(`roman(${n})`);
  let out = "";
  for (const [v, s] of table) while (n >= v) { out += s; n -= v; }
  return out;
}
export const roman = (n) => toRoman(n, ROMAN);
/** Value of a standard Roman numeral, or NaN if it is not written the standard way. */
export function fromRoman(s) {
  s = String(s).toUpperCase();
  if (!/^[IVXLCDM]+$/.test(s)) return NaN;
  let total = 0;
  for (let i = 0; i < s.length; i++) {
    const v = SYMBOL[s[i]], next = SYMBOL[s[i + 1]] || 0;
    total += v < next ? -v : v;
  }
  return total >= 1 && total <= 3999 && roman(total) === s ? total : NaN;
}
/** WRONG ON PURPOSE: no subtraction rule, 4 -> IIII, 90 -> LXXXX. */
export const romanAdditive = (n) => toRoman(n, ROMAN_ADD);
/** WRONG ON PURPOSE: adds every symbol, XL -> 60. */
export const romanAddAll = (s) => String(s).split("").reduce((a, c) => a + SYMBOL[c], 0);
export const hasSubtractive = (n) => /[49]/.test(String(n));

const EGYPT = [[1000, "lotus flower", "lotus flowers"], [100, "coil of rope", "coils of rope"],
  [10, "heel bone", "heel bones"], [1, "stroke", "strokes"]];
/** 3 205 -> "3 lotus flowers, 2 coils of rope and 5 strokes". Below 10 000. */
export function egyptianList(n) {
  const parts = EGYPT.map(([v, one, many]) => [Math.floor(n / v) % 10, one, many]).filter(([k]) => k)
    .map(([k, one, many]) => plural(k, one, many));
  return parts.length > 1 ? parts.slice(0, -1).join(", ") + " and " + parts[parts.length - 1] : parts[0];
}

// ---------------------------------------------------------------- number bases
const DIGITS = "0123456789";
export function toBase(n, b) {
  if (!Number.isInteger(n) || n < 0 || b < 2 || b > 10) throw new RangeError(`toBase(${n}, ${b})`);
  if (n === 0) return "0";
  let out = "";
  while (n > 0) { out = DIGITS[n % b] + out; n = Math.floor(n / b); }
  return out;
}
/** Value of a base-b numeral, or NaN if a digit is not allowed in base b. */
export function fromBase(s, b) {
  s = String(s);
  if (!/^[0-9]+$/.test(s)) return NaN;
  let v = 0;
  for (const c of s) {
    const d = Number(c);
    if (d >= b) return NaN;
    v = v * b + d;
  }
  return v;
}
export const isValidInBase = (s, b) => !Number.isNaN(fromBase(s, b));
/** WRONG ON PURPOSE: column arithmetic done in base ten (carrying or borrowing ten, not b). */
export const decAdd = (xs, ys) => String(Number(xs) + Number(ys));
export const decSub = (xs, ys) => String(Number(xs) - Number(ys));
export const decMul = (xs, ys) => String(Number(xs) * Number(ys));

// ---------------------------------------------------------------- full working (shown after a second miss)
// Each returns lines joined with "\n"; every number comes from the same functions as the answers.
const sb = (s, b) => `${s}${sub(b)}`;

/** Repeated division of n by b, then the remainders read upwards. */
export function divSteps(n, b) {
  const out = [];
  let q = n;
  do { out.push(`${fmt(q)} ÷ ${b} = ${fmt(Math.floor(q / b))} r ${q % b}`); q = Math.floor(q / b); } while (q > 0);
  out.push(`Read the remainders from the bottom up: ${sb(toBase(n, b), b)}`);
  return out.join("\n");
}
/** "1 × 25 + 2 × 5 + 3 × 1 = 25 + 10 + 3 = 38" for a base-b numeral. */
export function placeSum(s, b) {
  s = String(s);
  const digits = [...s].map(Number), L = digits.length;
  const terms = digits.map((d, i) => `${d} × ${fmt(b ** (L - 1 - i))}`);
  const values = digits.map((d, i) => fmt(d * b ** (L - 1 - i)));
  return `${sb(s, b)} = ${terms.join(" + ")} = ${values.join(" + ")} = ${fmt(fromBase(s, b))}`;
}
/** Column addition in base b, right to left, with carries. */
export function columnAdd(xs, ys, b) {
  const L = Math.max(String(xs).length, String(ys).length), out = [];
  let carry = 0;
  for (let i = 0; i < L; i++) {
    const a = dig(xs, i), c = dig(ys, i), t = a + c + carry;
    out.push(`Column ${i + 1} from the right: ${a} + ${c}${carry ? ` + ${carry} (carried)` : ""} = ${t}` +
      (t >= b ? ` = ${b} + ${t - b}: write ${t - b}, carry 1` : `: write ${t}`));
    carry = t >= b ? 1 : 0;
  }
  if (carry) out.push("Write the last carry, 1.");
  out.push(`Answer: ${sb(toBase(fromBase(xs, b) + fromBase(ys, b), b), b)}`);
  return out.join("\n");
}
/** Column subtraction in base b, right to left, borrowing b. Requires xs ≥ ys. */
export function columnSub(xs, ys, b) {
  const L = String(xs).length, out = [];
  let borrow = 0;
  // Plain steps with no negative intermediates (TR-C31, Dion 2026-10-03).
  for (let i = 0; i < L; i++) {
    const d = dig(xs, i), c = dig(ys, i);
    const col = `Column ${i + 1} from the right: `;
    if (borrow && d === 0) {
      // Borrowing across a zero: the 0 has already lent 1, so it borrows b and gives back the 1.
      out.push(`${col}This 0 already lent 1 to the right and has nothing left, so it borrows from the next column. ` +
        `In base ${b}, borrowing gives ${b}. ${b} − 1 (what it lent) = ${b - 1}. Then ${b - 1} − ${c} = ${b - 1 - c}.`);
      borrow = 1;
    } else if (borrow) {
      const top = d - 1;  // ≥ 0 here
      if (top < c) {
        out.push(`${col}This ${d} lent 1 to the right: ${d} − 1 = ${top}. ${top} is less than ${c}, so it borrows from the next column. ` +
          `In base ${b}, borrowing gives ${b} more: ${top} + ${b} = ${top + b}. Then ${top + b} − ${c} = ${top + b - c}.`);
        borrow = 1;
      } else {
        out.push(`${col}This ${d} lent 1 to the right: ${d} − 1 = ${top}. Then ${top} − ${c} = ${top - c}.`);
        borrow = 0;
      }
    } else if (d < c) {
      out.push(`${col}${d} is less than ${c}, so it borrows from the next column. ` +
        `In base ${b}, borrowing gives ${b} more: ${d} + ${b} = ${d + b}. Then ${d + b} − ${c} = ${d + b - c}.`);
      borrow = 1;
    } else {
      out.push(`${col}${d} − ${c} = ${d - c}.`);
      borrow = 0;
    }
  }
  out.push(`Answer: ${sb(toBase(fromBase(xs, b) - fromBase(ys, b), b), b)}`);
  return out.join("\n");
}
/** Multiplying a base-b numeral by a one-digit number e, column by column with carries. */
export function columnMul(xs, e, b) {
  const L = String(xs).length, out = [];
  let carry = 0;
  for (let i = 0; i < L; i++) {
    const d = dig(xs, i), t = d * e + carry;
    out.push(`Column ${i + 1} from the right: ${e} × ${d}${carry ? ` + ${carry} (carried)` : ""} = ${t} = ${Math.floor(t / b)} × ${b} + ${t % b}: write ${t % b}, carry ${Math.floor(t / b)}`);
    carry = Math.floor(t / b);
  }
  if (carry) out.push(`Write the last carry, ${carry}.`);
  out.push(`Answer: ${sb(toBase(fromBase(xs, b) * e, b), b)}`);
  return out.join("\n");
}
/** "MCMXLVIII = M + CM + XL + VIII = 1000 + 900 + 40 + 8 = 1948" (place by place). */
export function romanWorking(n) {
  const parts = [1000, 100, 10, 1].map((p) => Math.floor(n / p) % 10 * p).filter(Boolean);
  if (parts.length === 1) return `${roman(n)} = ${fmt(n)}`;
  return `${roman(n)} = ${parts.map(roman).join(" + ")} = ${parts.map(fmt).join(" + ")} = ${fmt(n)}`;
}
/** Non-zero place values of n: "40 000 + 300 + 7". */
export const expanded = (n) => String(n).split("").map((d, i, a) => Number(d) * 10 ** (a.length - 1 - i)).filter(Boolean).map(fmt).join(" + ");

// ---------------------------------------------------------------- lengths
const UNITS = { km: 3, hm: 2, dam: 1, m: 0, dm: -1, cm: -2, mm: -3 };
export const unitExp = (u) => UNITS[u];
/** Exact conversion between metric length units. */
export function convert(v, from, to) {
  const d = UNITS[from] - UNITS[to];
  return d >= 0 ? v * 10 ** d : Number((v / 10 ** -d).toFixed(12));
}

// ---------------------------------------------------------------- lines in a plane
/** (X) r1 (Y) and (Z) r2 (X)  =>  relation between (Z) and (Y). r is "//" or "⊥". */
export function lineRule(r1, r2) {
  const perp = (r1 === "⊥") !== (r2 === "⊥");
  return perp ? "⊥" : "//";
}
