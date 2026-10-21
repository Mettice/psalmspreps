// Vetted functions for Form 2 Physics, Chemistry and Biology (Term 1): data and graphs, speed; atomic structure,
// electron shells, valency and chemical formulae, the periodic table; drawings of a flower and a bean seed.
// Used with maths.js, english.js, physics.js, chemistry.js and biology.js (bioArrangement for lettered parts).
// Tables marked "authored" are facts a teacher must check (docs/teacher-review.md, TR-Q, TR-J, TR-V).
import { fmt } from "./maths.js";
import { nameOf, ELEMENTS, parseFormula, kindOf, formula } from "./chemistry.js";
import { bioArrangement } from "./biology.js";

// ---------------------------------------------------------------- data
export const mean = (xs) => Number((xs.reduce((a, b) => a + b, 0) / xs.length).toFixed(2));
export const spread = (xs) => Math.max(...xs) - Math.min(...xs);
/** A list of readings as text: "12, 15, 11". */
export const readings = (xs) => xs.map(fmt).join(", ");

// ---------------------------------------------------------------- speed
export const kmhToMs = (v) => Number((v / 3.6).toFixed(2));
export const msToKmh = (v) => Number((v * 3.6).toFixed(2));

// ---------------------------------------------------------------- atoms (authored: mass number of the most common atom)
const MASS = { H: 1, He: 4, Li: 7, Be: 9, B: 11, C: 12, N: 14, O: 16, F: 19, Ne: 20, Na: 23, Mg: 24, Al: 27, Si: 28, P: 31, S: 32,
  Cl: 35, Ar: 40, K: 39, Ca: 40 };
const Z = Object.fromEntries(ELEMENTS.map((e) => [e.symbol, e.z]));
export const atomicNumber = (s) => Z[s];
export const massNumber = (s) => { if (!MASS[s]) throw new RangeError(`no mass number for ${s}`); return MASS[s]; };
export const neutrons = (s) => massNumber(s) - Z[s];
/** The first 20 elements' symbols, in order (for templates that pick one). */
export const firstTwenty = () => ELEMENTS.filter((e) => e.z <= 20).map((e) => e.symbol);
/** Electrons in each shell, 2, 8, 8, 2 (the Form 2 rule, for atomic numbers 1 to 20). */
export function shellList(z) {
  if (!Number.isInteger(z) || z < 1 || z > 20) throw new RangeError(`shells: atomic number ${z} is outside 1-20`);
  const out = [];
  let left = z;
  for (const cap of [2, 8, 8, 2]) { if (left <= 0) break; const n = Math.min(cap, left); out.push(n); left -= n; }
  return out;
}
export const shells = (z) => shellList(z).join(", ");
export const outerElectrons = (z) => { const s = shellList(z); return s[s.length - 1]; };
/** Group 1 to 8 (8 = the noble gases, also called group 0); helium is in group 8. Period = number of shells. */
export const groupOf = (z) => (z === 2 ? 8 : outerElectrons(z));
export const periodOf = (z) => shellList(z).length;
const FAMILY = { 1: "alkali metals", 2: "alkaline earth metals", 7: "halogens", 8: "noble gases" };
export const familyOf = (z) => FAMILY[groupOf(z)] || "none of these families";

// ---------------------------------------------------------------- valency and formulae (authored, TR-J)
// Positive parts (metals, hydrogen, ammonium) and negative parts (non-metals, radicals), each with its valency.
const POS = { H: [1, "hydrogen"], Li: [1, "lithium"], Na: [1, "sodium"], K: [1, "potassium"], Ag: [1, "silver"], NH4: [1, "ammonium"],
  Mg: [2, "magnesium"], Ca: [2, "calcium"], Zn: [2, "zinc"], Cu: [2, "copper"], Al: [3, "aluminium"] };
const NEG = { F: [1, "fluoride"], Cl: [1, "chloride"], I: [1, "iodide"], OH: [1, "hydroxide"], NO3: [1, "nitrate"], HCO3: [1, "hydrogencarbonate"],
  O: [2, "oxide"], S: [2, "sulfide"], SO4: [2, "sulfate"], CO3: [2, "carbonate"], N: [3, "nitride"], PO4: [3, "phosphate"] };
const RADICAL = new Set(["NH4", "OH", "NO3", "HCO3", "SO4", "CO3", "PO4"]);
export const valency = (x) => { const v = (POS[x] || NEG[x]); if (!v) throw new RangeError(`no valency for ${x}`); return v[0]; };
export const isRadical = (x) => RADICAL.has(x);
export const partName = (x) => { const v = (POS[x] || NEG[x]); if (!v) throw new RangeError(`unknown part ${x}`); return v[1]; };
export const positives = () => Object.keys(POS);
export const negatives = () => Object.keys(NEG);
export const radicals = () => [...RADICAL];
const gcd = (a, b) => (b ? gcd(b, a % b) : a);
const part = (x, n) => (n === 1 ? x : RADICAL.has(x) ? `(${x})${n}` : `${x}${n}`);
/** The formula from the valencies (swap and simplify): compoundFormula("Al", "SO4") → "Al2(SO4)3". Plain digits; show with formula(). */
export function compoundFormula(p, n) {
  const a = valency(p), b = valency(n), g = gcd(a, b);
  return part(p, b / g) + part(n, a / g);
}
/** The swapped numbers before simplifying, as a pupil writes them first: Mg O → Mg2O2. */
export const unsimplified = (p, n) => part(p, valency(n)) + part(n, valency(p));
export const needsSimplifying = (p, n) => gcd(valency(p), valency(n)) > 1;
/** The compound's name: compoundName("Na", "Cl") → "sodium chloride". */
export const compoundName = (p, n) => `${partName(p)} ${partName(n)}`;
/** The element names of a compound's parts, for explanations: elementOf("Cl") → "chlorine". */
export const elementOf = (x) => nameOf(x);

// ---------------------------------------------------------------- SVG
const r1 = (x) => Math.round(x * 10) / 10;
const svg = (w, h, label, body) =>
  `<svg class="fig" viewBox="0 0 ${w} ${h}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg" ` +
  `font-family="system-ui, sans-serif" font-size="11" fill="none" stroke="currentColor" stroke-width="1">${body}</svg>`;
const line = (x1, y1, x2, y2, extra = "") => `<line x1="${r1(x1)}" y1="${r1(y1)}" x2="${r1(x2)}" y2="${r1(y2)}"${extra}/>`;
const text = (x, y, s, extra = "") =>
  `<text x="${r1(x)}" y="${r1(y)}" fill="currentColor" stroke="none"${/text-anchor/.test(extra) ? "" : ` text-anchor="middle"`}${extra}>${s}</text>`;
const dot = (x, y, r = 3.5) => `<circle cx="${r1(x)}" cy="${r1(y)}" r="${r}" fill="currentColor"/>`;
const tag = (x, y, s) => `<circle cx="${r1(x)}" cy="${r1(y)}" r="10" style="fill: var(--card, #fff)"/>` + text(x, y + 4, s, ` font-weight="bold"`);
const pointer = (px, py, tx, ty, s) => line(px, py, tx, ty, ` stroke-opacity="0.6"`) + `<circle cx="${r1(px)}" cy="${r1(py)}" r="2" fill="currentColor"/>` + tag(tx, ty, s);

/** A line graph of readings: xs and ys are lists of the same length (ys ≥ 0); axes start at 0 with labelled ticks. */
export function lineGraph(xs, ys, xName, yName) {
  if (xs.length !== ys.length || xs.length < 2) throw new RangeError("lineGraph: needs two lists of the same length");
  const W = 250, H = 160, x0 = 46, y0 = 14, xMax = Math.max(...xs), yMax = Math.max(...ys);
  const niceY = [5, 10, 20, 25, 50, 100, 200, 500].find((s) => s * 5 >= yMax) || yMax / 5;
  const top = niceY * 5;
  const X = (x) => x0 + (x / xMax) * W, Y = (y) => y0 + H - (y / top) * H;
  let b = line(x0, y0, x0, y0 + H, ` stroke-width="1.5"`) + line(x0, y0 + H, x0 + W + 8, y0 + H, ` stroke-width="1.5"`);
  for (let i = 0; i <= 5; i++) b += line(x0 - 4, Y(i * niceY), x0 + W, Y(i * niceY), ` stroke-opacity="${i ? 0.2 : 1}"`) + text(x0 - 7, Y(i * niceY) + 4, fmt(i * niceY), ` font-size="10" text-anchor="end"`);
  for (const x of xs) b += line(X(x), y0 + H, X(x), y0 + H + 4) + text(X(x), y0 + H + 16, fmt(x), ` font-size="10"`);
  b += `<polyline points="${xs.map((x, i) => `${r1(X(x))},${r1(Y(ys[i]))}`).join(" ")}" stroke-width="2"/>` + xs.map((x, i) => dot(X(x), Y(ys[i]))).join("");
  b += text(x0 + W / 2, y0 + H + 32, xName, ` font-size="11"`) + text(12, y0 + H / 2, yName, ` font-size="11" transform="rotate(-90 12 ${r1(y0 + H / 2)})"`);
  return svg(x0 + W + 20, y0 + H + 40, "A line graph of measured values", b);
}

/** A bar chart: labels and values (≥ 0). */
export function barChart(labels, values, yName) {
  const n = labels.length, W = 260, H = 150, x0 = 46, y0 = 12, vMax = Math.max(...values);
  const step = [1, 2, 5, 10, 20, 25, 50, 100, 200, 500].find((s) => s * 5 >= vMax) || vMax / 5, top = step * 5;
  const bw = W / n, Y = (v) => y0 + H - (v / top) * H;
  let b = line(x0, y0, x0, y0 + H, ` stroke-width="1.5"`) + line(x0, y0 + H, x0 + W, y0 + H, ` stroke-width="1.5"`);
  for (let i = 0; i <= 5; i++) b += line(x0 - 4, Y(i * step), x0 + W, Y(i * step), ` stroke-opacity="${i ? 0.2 : 1}"`) + text(x0 - 7, Y(i * step) + 4, fmt(i * step), ` font-size="10" text-anchor="end"`);
  labels.forEach((l, i) => {
    b += `<rect x="${r1(x0 + i * bw + bw * 0.2)}" y="${r1(Y(values[i]))}" width="${r1(bw * 0.6)}" height="${r1(y0 + H - Y(values[i]))}" style="fill: var(--fig-liquid, #6aa9e9)" stroke="currentColor"/>`;
    b += text(x0 + i * bw + bw / 2, y0 + H + 15, l, ` font-size="10"`);
  });
  b += text(12, y0 + H / 2, yName, ` font-size="11" transform="rotate(-90 12 ${r1(y0 + H / 2)})"`);
  return svg(x0 + W + 12, y0 + H + 24, "A bar chart of measured values", b);
}

/** Bohr model of an atom (atomic number 1 to 20): the nucleus, then each shell with its electrons as dots. */
export function bohr(z) {
  const s = shellList(z), cx = 130, cy = 130;
  let b = `<circle cx="${cx}" cy="${cy}" r="18" style="fill: #f3c38b" stroke="currentColor"/>` + text(cx, cy + 4, "nucleus", ` font-size="8"`);
  s.forEach((n, i) => {
    const r = 34 + i * 26;
    b += `<circle cx="${cx}" cy="${cy}" r="${r}" stroke-opacity="0.6"/>`;
    for (let k = 0; k < n; k++) { const a = (2 * Math.PI * k) / n - Math.PI / 2; b += dot(cx + r * Math.cos(a), cy + r * Math.sin(a), 3.5); }
  });
  return svg(260, 260, "An atom drawn with its electron shells", b);
}

// A flower cut in half, eight lettered parts (authored names, TR-V).
export const FLOWER_PARTS = ["petal", "sepal", "anther", "filament", "stigma", "style", "ovary", "receptacle"];
export const flowerPart = (i) => FLOWER_PARTS[i];
export function flower(k) {
  const L = bioArrangement(k, 8);
  let b = `<path d="M160 250 v-70" stroke-width="5" style="stroke: #5b8c3a"/>`;                                                      // stalk
  b += `<path d="M126 186 q34 -26 68 0 q-10 14 -34 14 q-24 0 -34 -14 z" style="fill: #9ccc65" stroke="currentColor"/>`;              // receptacle
  b += `<path d="M126 186 q-34 -2 -48 -24 q30 -8 56 12 z" style="fill: #7cb342" stroke="currentColor"/>` +
    `<path d="M194 186 q34 -2 48 -24 q-30 -8 -56 12 z" style="fill: #7cb342" stroke="currentColor"/>`;                               // sepals
  b += `<path d="M132 176 q-60 -40 -52 -110 q46 24 64 96 z" style="fill: #f48fb1" stroke="currentColor"/>` +
    `<path d="M188 176 q60 -40 52 -110 q-46 24 -64 96 z" style="fill: #f48fb1" stroke="currentColor"/>`;                              // petals
  b += `<path d="M148 182 q-6 -20 4 -34 q8 -6 16 0 q10 14 4 34 z" style="fill: #ffe082" stroke="currentColor"/>`;                   // ovary
  b += line(160, 148, 160, 78, ` stroke-width="3"`) + `<ellipse cx="160" cy="72" rx="12" ry="6" style="fill: #c5e1a5" stroke="currentColor"/>`; // style + stigma
  for (const [x1, y1, x2, y2] of [[146, 176, 126, 104], [174, 176, 194, 104]]) {
    b += line(x1, y1, x2, y2, ` stroke-width="1.5"`) + `<ellipse cx="${x2}" cy="${y2 - 6}" rx="6" ry="10" style="fill: #ffb300" stroke="currentColor"/>`; // stamens
  }
  b += pointer(96, 100, 40, 70, L[0]) + pointer(84, 166, 36, 196, L[1]) + pointer(126, 92, 96, 30, L[2]) + pointer(134, 130, 60, 130, L[3]) +
    pointer(168, 72, 230, 30, L[4]) + pointer(160, 110, 280, 100, L[5]) + pointer(166, 166, 284, 150, L[6]) + pointer(178, 196, 270, 222, L[7]);
  return svg(320, 260, "A flower cut in half, with lettered parts", b);
}

// A bean seed opened, six lettered parts (authored names, TR-V).
export const SEED_PARTS = ["testa", "hilum", "micropyle", "cotyledon", "plumule", "radicle"];
export const seedPart = (i) => SEED_PARTS[i];
export function beanSeed(k) {
  const L = bioArrangement(k, 6);
  let b = `<path d="M70 120 q0 -70 90 -74 q90 -2 96 74 q4 66 -96 70 q-92 2 -90 -70 z" style="fill: #e8c9a1" stroke="currentColor" stroke-width="3"/>`; // testa
  b += `<path d="M84 120 q2 -58 78 -62 q78 0 82 62 q2 54 -82 58 q-80 2 -78 -58 z" style="fill: #f6e7c8" stroke="currentColor"/>`;                 // cotyledon
  b += `<ellipse cx="160" cy="44" rx="16" ry="5" style="fill: #6d4c41" stroke="currentColor"/>`;                                               // hilum
  b += `<circle cx="186" cy="48" r="2.5" fill="currentColor"/>`;                                                                                 // micropyle
  b += `<path d="M150 64 q-4 30 6 50" stroke-width="5" style="stroke: #c0a46c"/>` + `<path d="M156 112 q10 -6 18 -2 q-6 8 -18 6 z" style="fill: #9ccc65" stroke="currentColor"/>`; // radicle + plumule
  b += pointer(70, 150, 30, 180, L[0]) + pointer(150, 42, 110, 18, L[1]) + pointer(186, 48, 236, 20, L[2]) + pointer(210, 140, 280, 160, L[3]) +
    pointer(170, 110, 280, 100, L[4]) + pointer(150, 76, 40, 80, L[5]);
  return svg(310, 210, "A bean seed opened, with lettered parts", b);
}

// ---------------------------------------------------------------- Form 2 Computer Science: hexadecimal, characters, storage
const HEX = "0123456789ABCDEF";
/** n in base 16, capital letters: toHex(255) → "FF". */
export function toHex(n) {
  if (!Number.isInteger(n) || n < 0) throw new RangeError(`toHex(${n})`);
  let s = "";
  do { s = HEX[n % 16] + s; n = Math.floor(n / 16); } while (n > 0);
  return s;
}
export function fromHex(s) {
  let v = 0;
  for (const c of String(s).toUpperCase()) { const d = HEX.indexOf(c); if (d < 0) return NaN; v = v * 16 + d; }
  return v;
}
/** The value of one hexadecimal digit: hexValue("B") → 11. */
export const hexValue = (c) => HEX.indexOf(String(c).toUpperCase());
/** An 8-bit binary pattern: bits8(5) → "00000101". */
export function bits8(n) {
  if (!Number.isInteger(n) || n < 0 || n > 255) throw new RangeError(`bits8(${n})`);
  return n.toString(2).padStart(8, "0");
}
/** ASCII code of a character, and the character of a code (printable ASCII only, 32 to 126). */
export function asciiOf(c) {
  const n = String(c).charCodeAt(0);
  if (String(c).length !== 1 || n < 32 || n > 126) throw new RangeError(`asciiOf(${c})`);
  return n;
}
export function charOf(n) {
  if (!Number.isInteger(n) || n < 32 || n > 126) throw new RangeError(`charOf(${n})`);
  return String.fromCharCode(n);
}
// Storage units (authored, TR-T05: the school convention of 1 KB = 1024 bytes). 1 byte = 8 bits.
const STORE = { bit: 1 / 8, byte: 1, KB: 1024, MB: 1024 ** 2, GB: 1024 ** 3, TB: 1024 ** 4 };
export const storageUnits = () => Object.keys(STORE);
/** Converts between storage units: storageConvert(2, "KB", "byte") → 2048. */
export function storageConvert(v, from, to) {
  if (!(from in STORE) || !(to in STORE)) throw new RangeError(`storageConvert: ${from} → ${to}`);
  return Number(((v * STORE[from]) / STORE[to]).toPrecision(12));
}
/** How many `to` units in one `from` unit: storageFactor("MB", "KB") → 1024. */
export const storageFactor = (from, to) => storageConvert(1, from, to);

// ================================================================ Physics Term 2 (2026-10-21)
const dec2 = (x) => Number(x.toFixed(6));
/** Energy in joules: power (W) × time (s). */
export const energyJ = (P, t) => dec2(P * t);
/** Energy in kilowatt-hours: power (W) ÷ 1000 × hours. */
export const kWh = (P, h) => dec2((P / 1000) * h);
/** Cost of electricity: energy in kWh × price per kWh. */
export const elecCost = (P, h, price) => dec2((P / 1000) * h * price);
/** Electrical power P = V × I. */
export const powerVI = (V, I) => dec2(V * I);
/** Height of the shadow of an object of height h at distance d1 from a point source, on a screen at distance d2. */
export const shadowHeight = (h, d1, d2) => dec2((h * d2) / d1);
/** Power of a lens in dioptres from its focal length in centimetres (P = 100 ÷ f). */
export const lensPower = (fcm) => dec2(100 / fcm);
/** Pressure = force ÷ area (N/m² = Pa). */
export const pressure = (F, A) => dec2(F / A);
/** Pressure in a liquid: density (kg/m³) × g × depth (m), with g = 10 N/kg. */
export const liquidPressure = (rho, h, g = 10) => dec2(rho * g * h);
/** Pulse rate in beats per minute from beats counted in some seconds. */
export const pulseRate = (beats, seconds) => dec2((beats * 60) / seconds);
/** Light travel time in seconds over a distance in kilometres (c ≈ 300 000 km/s). */
export const lightTime = (km) => dec2(km / 300000);
/** A point source, an opaque object of height h at d1 and a screen at d2, with the shadow (heights written, not to scale). */
export function shadowFig(h, d1, d2) {
  const S = 260 / d2, x0 = 20, y0 = 90, X1 = x0 + d1 * S, X2 = x0 + d2 * S, H1 = 28, H2 = (H1 * d2) / d1;
  const r = (v) => Math.round(v * 10) / 10;
  let body = `<circle cx="${x0}" cy="${y0}" r="5" fill="currentColor"/>`;
  body += `<line x1="${r(X1)}" y1="${r(y0 - H1)}" x2="${r(X1)}" y2="${r(y0 + H1)}" stroke-width="4"/>`;
  body += `<line x1="${r(X2)}" y1="${r(y0 - H2 - 8)}" x2="${r(X2)}" y2="${r(y0 + H2 + 8)}" stroke-width="1.5"/>`;
  body += `<line x1="${x0}" y1="${y0}" x2="${r(X2)}" y2="${r(y0 - H2)}" stroke-dasharray="4 3"/><line x1="${x0}" y1="${y0}" x2="${r(X2)}" y2="${r(y0 + H2)}" stroke-dasharray="4 3"/>`;
  body += `<line x1="${r(X2 + 4)}" y1="${r(y0 - H2)}" x2="${r(X2 + 4)}" y2="${r(y0 + H2)}" stroke-width="5" stroke-opacity="0.45"/>`;
  body += `<text x="${x0}" y="${y0 + 22}" fill="currentColor" stroke="none" text-anchor="middle" font-size="11">source</text>`;
  body += `<text x="${r(X1)}" y="${r(y0 + H1 + 16)}" fill="currentColor" stroke="none" text-anchor="middle" font-size="11">object ${h} cm</text>`;
  body += `<text x="${r(X2 - 6)}" y="18" fill="currentColor" stroke="none" text-anchor="end" font-size="11">screen</text>`;
  body += `<text x="${r((x0 + X1) / 2)}" y="178" fill="currentColor" stroke="none" text-anchor="middle" font-size="11">${d1} cm</text>`;
  body += `<text x="${r((x0 + X2) / 2)}" y="194" fill="currentColor" stroke="none" text-anchor="middle" font-size="11">${d2} cm from the source</text>`;
  return `<svg class="fig" viewBox="0 0 300 200" role="img" aria-label="A point source, an object and its shadow on a screen" xmlns="http://www.w3.org/2000/svg" ` +
    `font-family="system-ui, sans-serif" fill="none" stroke="currentColor" stroke-width="1">${body}</svg>`;
}

// ================================================================ Chemistry Term 2 (2026-10-21)
// Balanced equations (authored, TR-J10); every one is checked by atom counting in the tests.
// Each: [words, reactants [[coefficient, formula]], products [[coefficient, formula]]].
const EQ = [
  ["magnesium + oxygen → magnesium oxide", [[2, "Mg"], [1, "O2"]], [[2, "MgO"]]],
  ["carbon + oxygen → carbon dioxide", [[1, "C"], [1, "O2"]], [[1, "CO2"]]],
  ["hydrogen + oxygen → water", [[2, "H2"], [1, "O2"]], [[2, "H2O"]]],
  ["sodium + oxygen → sodium oxide", [[4, "Na"], [1, "O2"]], [[2, "Na2O"]]],
  ["calcium + oxygen → calcium oxide", [[2, "Ca"], [1, "O2"]], [[2, "CaO"]]],
  ["sulphur + oxygen → sulphur dioxide", [[1, "S"], [1, "O2"]], [[1, "SO2"]]],
  ["iron + oxygen → iron(III) oxide", [[4, "Fe"], [3, "O2"]], [[2, "Fe2O3"]]],
  ["aluminium + oxygen → aluminium oxide", [[4, "Al"], [3, "O2"]], [[2, "Al2O3"]]],
  ["copper + oxygen → copper(II) oxide", [[2, "Cu"], [1, "O2"]], [[2, "CuO"]]],
  ["iron + sulphur → iron(II) sulphide", [[1, "Fe"], [1, "S"]], [[1, "FeS"]]],
  ["nitrogen + hydrogen → ammonia", [[1, "N2"], [3, "H2"]], [[2, "NH3"]]],
  ["hydrogen + chlorine → hydrogen chloride", [[1, "H2"], [1, "Cl2"]], [[2, "HCl"]]],
  ["zinc + hydrochloric acid → zinc chloride + hydrogen", [[1, "Zn"], [2, "HCl"]], [[1, "ZnCl2"], [1, "H2"]]],
  ["magnesium + hydrochloric acid → magnesium chloride + hydrogen", [[1, "Mg"], [2, "HCl"]], [[1, "MgCl2"], [1, "H2"]]],
  ["calcium carbonate → calcium oxide + carbon dioxide", [[1, "CaCO3"]], [[1, "CaO"], [1, "CO2"]]],
  ["methane + oxygen → carbon dioxide + water", [[1, "CH4"], [2, "O2"]], [[1, "CO2"], [2, "H2O"]]],
  ["sodium hydroxide + hydrochloric acid → sodium chloride + water", [[1, "NaOH"], [1, "HCl"]], [[1, "NaCl"], [1, "H2O"]]],
  ["potassium chlorate → potassium chloride + oxygen", [[2, "KClO3"]], [[2, "KCl"], [3, "O2"]]],
  ["hydrogen peroxide → water + oxygen", [[2, "H2O2"]], [[2, "H2O"], [1, "O2"]]],
  ["calcium oxide + water → calcium hydroxide", [[1, "CaO"], [1, "H2O"]], [[1, "Ca(OH)2"]]],
];
export const nEquations = () => EQ.length;
/** Indices of the equations that only form a binary compound from elements (Term 2, row 24). */
export const binaryEquations = () => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
export const otherEquations = () => [12, 13, 14, 15, 16, 17, 18, 19];
export const eqWords = (i) => EQ[i][0];
const side = (terms, coefs) => terms.map(([c, f], k) => `${(coefs ? coefs[k] : c) === 1 ? "" : coefs ? coefs[k] : c}${formula(f)}`).join(" + ");
/** "2Mg + O₂ → 2MgO" (balanced), or with the given coefficients (to make wrong options). */
export const eqStr = (i) => `${side(EQ[i][1])} → ${side(EQ[i][2])}`;
/** The unbalanced skeleton: every coefficient 1. */
export const eqSkeleton = (i) => `${side(EQ[i][1], EQ[i][1].map(() => 1))} → ${side(EQ[i][2], EQ[i][2].map(() => 1))}`;
/** The balanced equation with the coefficient of term k (counting reactants then products) shown as ___. */
export function eqBlank(i, k) {
  const all = [...EQ[i][1], ...EQ[i][2]], n = EQ[i][1].length;
  const one = (t, j) => (j === k ? `___${formula(t[1])}` : `${t[0] === 1 ? "" : t[0]}${formula(t[1])}`);
  return `${all.slice(0, n).map(one).join(" + ")} → ${all.slice(n).map((t, j) => one(t, j + n)).join(" + ")}`;
}
export const eqCoef = (i, k) => [...EQ[i][1], ...EQ[i][2]][k][0];
export const eqTerms = (i) => EQ[i][1].length + EQ[i][2].length;
/** The term whose coefficient is not 1 (the most useful blank); the first if all are 1. */
export const eqKeyTerm = (i) => Math.max(0, [...EQ[i][1], ...EQ[i][2]].findIndex((t) => t[0] !== 1));
/** The equation with the coefficient of term k changed by d (a wrong option). */
export function eqWrong(i, k, d) {
  const all = [...EQ[i][1], ...EQ[i][2]].map((t) => t[0]);
  all[k] = Math.max(1, all[k] + d);
  const n = EQ[i][1].length;
  return `${side(EQ[i][1], all.slice(0, n))} → ${side(EQ[i][2], all.slice(n))}`;
}
/** Number of atoms of an element on one side (0 reactants, 1 products) of the balanced equation. */
export const eqAtoms = (i, s, symbol) => EQ[i][1 + s].reduce((t, [c, f]) => t + c * (parseFormula(f)[symbol] || 0), 0);
export const eqElements = (i) => [...new Set(EQ[i][1].flatMap(([, f]) => Object.keys(parseFormula(f))))];
export const eqBalanced = (i) => eqElements(i).every((e) => eqAtoms(i, 0, e) === eqAtoms(i, 1, e));
/** Burning an element in oxygen: a metal gives a basic oxide, a non-metal an acidic oxide. */
export const oxideType = (symbol) => (kindOf(symbol) === "metal" ? "basic" : "acidic");
/** Rf value of a chromatography spot: distance moved by the spot ÷ distance moved by the solvent. */
export const rf = (spot, solvent) => Number((spot / solvent).toFixed(2));
/** The state of a substance at temperature T (°C) from its melting and boiling points. */
export const stateAt = (T, mp, bp) => (T < mp ? "solid" : T < bp ? "liquid" : "gas");
/** The k-th element in the equation (wrapping round), so a question can pick one with an integer. */
export const eqElement = (i, k) => eqElements(i)[k % eqElements(i).length];
/** The usual slip when counting atoms: the small numbers counted but the big numbers in front forgotten. */
export const eqAtomsNoCoef = (i, s, symbol) => EQ[i][1 + s].reduce((t, [, f]) => t + (parseFormula(f)[symbol] || 0), 0);
/** The formula of term k (reactants then products). */
export const eqTermFormula = (i, k) => [...EQ[i][1], ...EQ[i][2]][k][1];
