// Physics helpers for templates: units and conversions, weight and density, and measuring instruments drawn
// as SVG from the question's own numbers (so the reading is computed, never typed). Used as {...maths, ...physics}.
// Conventions to be checked by a teacher (docs/teacher-review.md, TR-P*): g = 10 N/kg, T(K) = T(°C) + 273.

// ---------------------------------------------------------------- units
// Each unit is a power of ten of the quantity's base unit (metre, gram, litre, second-free).
const UNITS = {
  length: { km: 3, hm: 2, dam: 1, m: 0, dm: -1, cm: -2, mm: -3 },
  mass: { t: 6, kg: 3, hg: 2, dag: 1, g: 0, dg: -1, cg: -2, mg: -3 },
  capacity: { kL: 3, hL: 2, daL: 1, L: 0, dL: -1, cL: -2, mL: -3, "m³": 3, "dm³": 0, "cm³": -3 },
};
const TIME = { h: 3600, min: 60, s: 1 };

/** The quantity a unit measures: "length", "mass", "capacity", "time", or undefined. */
export function quantityOf(u) {
  for (const [q, table] of Object.entries(UNITS)) if (u in table) return q;
  return u in TIME ? "time" : undefined;
}

/** Exact decimal result of v × 10^k, without floating-point noise (2.5 × 1000 = 2500, 7 ÷ 1000 = 0.007). */
function shift(v, k) {
  const r = k >= 0 ? v * 10 ** k : v / 10 ** -k;
  return Number(r.toPrecision(12));
}

/** Converts v between two units of the same quantity: convertUnit(2.5, 'kg', 'g') = 2500; 1 L = 1000 cm³. */
export function convertUnit(v, from, to) {
  const q = quantityOf(from);
  if (!q || q !== quantityOf(to)) throw new RangeError(`cannot convert ${from} to ${to}`);
  if (q === "time") return Number(((v * TIME[from]) / TIME[to]).toPrecision(12));
  return shift(v, UNITS[q][from] - UNITS[q][to]);
}
/** How many `to` units make one `from` unit, e.g. factor('kg', 'g') = 1000. */
export const factor = (from, to) => convertUnit(1, from, to);

/** °C → K and K → °C, with the Form 1 rule T(K) = T(°C) + 273 (TR-P04). */
export const toKelvin = (c) => c + 273;
export const toCelsius = (k) => k - 273;

/** Weight in newtons: W = m × g, with m in kg and g = 10 N/kg unless given (TR-P03). */
export const weight = (m, g = 10) => Number((m * g).toPrecision(12));
/** Density = mass ÷ volume, rounded to 2 decimals for display. */
export const density = (m, v) => Number((m / v).toFixed(2));
/** Floats in water (density 1 g/cm³) when its density is less than 1. */
export const floatsInWater = (d) => d < 1;
/** Volume of a cuboid. */
export const cuboid = (l, w, h) => Number((l * w * h).toPrecision(12));

// ---------------------------------------------------------------- SVG instruments
// Each function returns an SVG string with role="img" and a label that does NOT give the reading.
// Colours come from the page (currentColor, CSS variables) so light and dark themes both work.
const r1 = (x) => Math.round(x * 10) / 10;
const svg = (w, h, label, body) =>
  `<svg class="fig" viewBox="0 0 ${w} ${h}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg" ` +
  `font-family="system-ui, sans-serif" font-size="11" fill="none" stroke="currentColor" stroke-width="1">${body}</svg>`;
const line = (x1, y1, x2, y2, extra = "") => `<line x1="${r1(x1)}" y1="${r1(y1)}" x2="${r1(x2)}" y2="${r1(y2)}"${extra}/>`;
// Centred unless `extra` sets its own text-anchor (an attribute written twice is invalid SVG, and HTML keeps the first).
const text = (x, y, s, extra = "") =>
  `<text x="${r1(x)}" y="${r1(y)}" fill="currentColor" stroke="none"${/text-anchor/.test(extra) ? "" : ` text-anchor="middle"`}${extra}>${s}</text>`;

/**
 * A ruler (0 to 8 cm by default) with millimetre marks, and an object lying on it from `start` to `end` (in cm, to the mm).
 * The reading is end − start: the object need not start at zero.
 */
export function ruler(start, end, length = 8) {
  if (start < 0 || end > length || end <= start) throw new RangeError(`ruler: object from ${start} to ${end} cm does not fit a ${length} cm ruler`);
  const x0 = 15, px = 20;  // 20 px per cm; 8 cm keeps the millimetre marks about 4 px apart on a 360 px screen
  const X = (cm) => x0 + cm * px;
  let ticks = "";
  for (let mm = 0; mm <= length * 10; mm++) {
    const h = mm % 10 === 0 ? 16 : mm % 5 === 0 ? 11 : 6;
    ticks += line(X(mm / 10), 46, X(mm / 10), 46 + h);
    if (mm % 10 === 0) ticks += text(X(mm / 10), 78, mm / 10);
  }
  const body = `<rect x="${x0 - 8}" y="46" width="${length * px + 16}" height="38" rx="3"/>` + ticks +
    `<rect x="${r1(X(start))}" y="18" width="${r1((end - start) * px)}" height="14" rx="3" style="fill: var(--fig-object, #c98b3a)" stroke="currentColor"/>` +
    line(X(start), 32, X(start), 46, ` stroke-dasharray="3 2"`) + line(X(end), 32, X(end), 46, ` stroke-dasharray="3 2"`) +
    text(x0 + length * px - 2, 96, "cm", ` text-anchor="end"`);
  return svg(length * px + 30, 100, "A ruler with an object lying on it", body);
}

/**
 * A measuring cylinder holding `level` mL (read at the bottom of the curved surface, the meniscus).
 * Marks every `step` mL, numbers every `label` mL, up to `max` mL. `stone` draws a stone at the bottom.
 */
function cylinderBody(cx, level, max, step, label, stone, top = 16, bottom = 236) {
  const w = 46, x = cx - w / 2;
  const Y = (v) => bottom - ((bottom - top) * v) / max;
  let out = `<path d="M${x} ${top - 6} L${x} ${bottom} Q${x} ${bottom + 8} ${x + 8} ${bottom + 8} L${x + w - 8} ${bottom + 8} Q${x + w} ${bottom + 8} ${x + w} ${bottom} L${x + w} ${top - 6}"/>`;
  out += `<path d="M${x} ${r1(Y(level) - 4)} Q${cx} ${r1(Y(level) + 3)} ${x + w} ${r1(Y(level) - 4)} L${x + w} ${bottom} Q${x + w} ${bottom + 8} ${x + w - 8} ${bottom + 8} L${x + 8} ${bottom + 8} Q${x} ${bottom + 8} ${x} ${bottom} Z" style="fill: var(--fig-liquid, #6aa9e9)" stroke="none" opacity="0.55"/>`;
  out += `<path d="M${x} ${r1(Y(level) - 4)} Q${cx} ${r1(Y(level) + 3)} ${x + w} ${r1(Y(level) - 4)}" stroke-width="1.5"/>`;
  for (let v = step; v <= max; v += step) {
    const major = v % label === 0;
    out += line(x, Y(v), x + (major ? 14 : 8), Y(v));
    if (major) out += text(x - 9, Y(v) + 4, v, ` text-anchor="end"`);
  }
  if (stone) out += `<path d="M${cx - 12} ${bottom + 2} q4 -16 14 -14 q12 2 10 14 z" style="fill: var(--fig-object, #8a8178)" stroke="currentColor"/>`;
  return out;
}
export function cylinder(level, max = 100, step = 2, label = 10) {
  return svg(140, 262, "A measuring cylinder with liquid in it",
    cylinderBody(80, level, max, step, label, false) + text(80, 258, "mL"));
}
/** Two measuring cylinders: water alone, then the same water with a stone in it (volume by displacement). */
export function displacement(before, after, max = 100, step = 2, label = 10) {
  return svg(280, 276, "Two measuring cylinders: water before and after a stone is put in",
    cylinderBody(78, before, max, step, label, false) + cylinderBody(218, after, max, step, label, true) +
    text(78, 262, "before (mL)") + text(218, 262, "after (mL)"));
}

/**
 * A liquid-in-glass thermometer in °C reading `t`. The scale shows `from` to `from + span` with a mark every
 * `step` degrees and a number every `label` degrees. For a clinical thermometer use clinical(t).
 */
export function thermometer(t, from = 0, span = 50, step = 1, label = 10) {
  const x0 = 34, x1 = 318, Y = 34;
  const X = (c) => x0 + ((x1 - x0) * (c - from)) / span;
  let ticks = "";
  const n = Math.round(span / step);
  for (let i = 0; i <= n; i++) {
    const c = from + i * step, lab = Math.abs((c / label) - Math.round(c / label)) < 1e-9;
    ticks += line(X(c), Y + 10, X(c), Y + (lab ? 24 : 17));
    if (lab) ticks += text(X(c), Y + 38, Number(c.toFixed(1)));
  }
  const body = `<circle cx="18" cy="${Y}" r="10" style="fill: var(--fig-red, #d0473b)"/>` +
    `<rect x="26" y="${Y - 5}" width="${x1 - 20}" height="10" rx="5"/>` +
    `<rect x="26" y="${Y - 2.5}" width="${r1(X(t) - 26)}" height="5" style="fill: var(--fig-red, #d0473b)" stroke="none"/>` + ticks +
    text(x1, Y + 52, "°C", ` text-anchor="end"`);
  return svg(330, 92, "A thermometer", body);
}
/** A clinical thermometer: 35 °C to 42 °C, a mark every 0.1 °C, a number every degree. */
export const clinical = (t) => thermometer(t, 35, 7, 0.1, 1);

// ---------------------------------------------------------------- changes of state (TR-P07)
// Names used in Form 1: melting, freezing (solidification), evaporation (boiling when it happens throughout the
// liquid at the boiling point), condensation, sublimation (solid → gas) and deposition (gas → solid).
const PROCESS = {
  "solid>liquid": "melting", "liquid>solid": "freezing", "liquid>gas": "evaporation",
  "gas>liquid": "condensation", "solid>gas": "sublimation", "gas>solid": "deposition",
};
/** The name of the change from one state to another: processName('solid', 'liquid') = 'melting'. */
export function processName(from, to) {
  const p = PROCESS[`${from}>${to}`];
  if (!p) throw new RangeError(`no change of state from ${from} to ${to}`);
  return p;
}
const ORDER = { solid: 0, liquid: 1, gas: 2 };
/** Heat is taken in when particles move further apart (solid → liquid → gas) and given out the other way. */
export const heatFlow = (from, to) => (ORDER[to] > ORDER[from] ? "taken in" : "given out");

// ---------------------------------------------------------------- dates on product labels
/** A date as one number that sorts correctly: 2026-10-07 → 20261007. */
export const dateNum = (d, m, y) => y * 10000 + m * 100 + d;
/** True if the "use before" date (d2, m2, y2) is still after today (d1, m1, y1). */
export const stillGood = (d1, m1, y1, d2, m2, y2) => dateNum(d2, m2, y2) > dateNum(d1, m1, y1);
