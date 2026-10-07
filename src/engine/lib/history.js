// History helpers for templates: dates BC and AD (there is no year 0), centuries, years between two dates, a timeline
// drawn by code from the question's own years, and an authored table of early humans.
// Used as {...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics, ...history}.
// Conventions to be checked by a teacher (docs/teacher-review.md, TR-Y*): years are written "500 BC" and "AD 476";
// estimated dates are given with "about"; there is no year 0 (1 BC is followed by AD 1).
// Years are numbers: AD years positive, BC years negative (−500 = 500 BC).

/** A year as it is written: −500 → "500 BC", 476 → "AD 476". */
export function year(y) {
  if (!Number.isInteger(y) || y === 0) throw new RangeError(`year: ${y} is not a year (there is no year 0)`);
  return y < 0 ? `${-y} BC` : `AD ${y}`;
}
/** Years from one date to a later one. No year 0, so across BC/AD one year less than the plain difference. */
export function yearsBetween(a, b) {
  if (a === 0 || b === 0) throw new RangeError("there is no year 0");
  const [x, y] = a < b ? [a, b] : [b, a];
  return x < 0 && y > 0 ? y - x - 1 : y - x;
}
/** The wrong answer a pupil gets by forgetting that there is no year 0 (for feedback only). */
export const yearsBetweenWithZero = (a, b) => Math.abs(b - a);
/** The century a year is in: AD 1–100 is the 1st century, AD 1901–2000 the 20th; 500 BC is in the 5th century BC. */
export const centuryOf = (y) => Math.ceil(Math.abs(y) / 100);
const ORD = (n) => `${n}${n % 100 >= 11 && n % 100 <= 13 ? "th" : ["th", "st", "nd", "rd"][n % 10] || "th"}`;
/** The century in words: 1884 → "19th century AD", −500 → "5th century BC". */
export const century = (y) => `${ORD(centuryOf(y))} century ${y < 0 ? "BC" : "AD"}`;
/** The wrong century a pupil gets by reading the first two digits (1884 → 18th): for feedback only. */
export const centuryFirstDigits = (y) => `${ORD(Math.floor(Math.abs(y) / 100))} century ${y < 0 ? "BC" : "AD"}`;
/** First and last year of a century: AD 19th → 1801 to 1900. */
export const centuryStart = (n) => (n - 1) * 100 + 1;
export const centuryEnd = (n) => n * 100;
/** Which of two dates is earlier (BC dates are earlier the bigger their number). */
export const earlier = (a, b) => (a < b ? a : b);

// ---------------------------------------------------------------- early humans (authored, TR-Y)
// [name, about how many years ago it first appears, what the name means / is known for, where important fossils were found]
const HOMININS = [
  ["Sahelanthropus tchadensis (Toumaï)", 7000000, "one of the oldest known ancestors, found in Chad", "Chad"],
  ["Australopithecus (“Lucy”)", 3200000, "walked upright on two legs, with a small brain", "Ethiopia"],
  ["Homo habilis", 2400000, "“handy man”: made the first simple stone tools", "Tanzania (Olduvai Gorge)"],
  ["Homo erectus", 1900000, "“upright man”: used fire and travelled out of Africa", "Kenya"],
  ["Homo sapiens", 300000, "“wise man”: modern humans, like us", "Morocco and Ethiopia"],
];
export const homininName = (i) => HOMININS[i][0];
export const homininAgo = (i) => HOMININS[i][1];
export const homininNote = (i) => HOMININS[i][2];
export const homininPlace = (i) => HOMININS[i][3];
/** "about 2.4 million years ago", "about 300 000 years ago". */
export function ago(n) {
  if (n >= 1000000) return `about ${Number((n / 1000000).toFixed(1))} million years ago`;
  return `about ${String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " ")} years ago`;
}

// ---------------------------------------------------------------- timeline drawing
const r1 = (x) => Math.round(x * 10) / 10;
const svg = (w, h, label, body) =>
  `<svg class="fig" viewBox="0 0 ${w} ${h}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg" ` +
  `font-family="system-ui, sans-serif" font-size="11" fill="none" stroke="currentColor" stroke-width="1">${body}</svg>`;
const line = (x1, y1, x2, y2, extra = "") => `<line x1="${r1(x1)}" y1="${r1(y1)}" x2="${r1(x2)}" y2="${r1(y2)}"${extra}/>`;
const text = (x, y, s, extra = "") =>
  `<text x="${r1(x)}" y="${r1(y)}" fill="currentColor" stroke="none"${/text-anchor/.test(extra) ? "" : ` text-anchor="middle"`}${extra}>${s}</text>`;
/**
 * A timeline from `from` to `to` (years, BC negative) with a mark every `step` years, the BC/AD change shown,
 * and the events [[label, year], …] marked above the line. Labels only, never the years of the events.
 */
export function timeline(from, to, step, events) {
  const x0 = 20, x1 = 320, Y = 70;
  const X = (y) => x0 + ((x1 - x0) * (y - from)) / (to - from);
  let b = line(x0, Y, x1, Y, ` stroke-width="2"`) + `<path d="M${x1 - 8} ${Y - 5} L${x1} ${Y} L${x1 - 8} ${Y + 5}"/>`;
  for (let y = Math.ceil(from / step) * step; y <= to; y += step) {
    b += line(X(y), Y - 5, X(y), Y + 5);
    b += text(X(y), Y + 20, y === 0 ? "BC | AD" : y < 0 ? `${-y} BC` : `${y}`, ` font-size="10"`);
  }
  events.forEach(([label, y], i) => {
    const h = 22 + (i % 2) * 18;
    b += `<circle cx="${r1(X(y))}" cy="${Y}" r="4" style="fill: var(--fig-red, #d0473b)"/>` + line(X(y), Y - 4, X(y), Y - h) + text(X(y), Y - h - 4, label, ` font-weight="bold"`);
  });
  return svg(340, 104, "A timeline with lettered events", b);
}
