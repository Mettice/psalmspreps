// Computer Science helpers for templates: patterns (number sequences and repeating shapes, computed), tracing short
// algorithms, an authored table of computer history, and drawings made by code (shape sequences, laboratory layouts).
// Used as {...maths, …, ...biology, ...computerscience}.
// Conventions to be checked by a teacher (docs/teacher-review.md, TR-S*): the generations of computers and their dates
// (textbooks differ); flowchart symbols.

// ---------------------------------------------------------------- number patterns
/** Term n (1-based) of the sequence start, start + step, start + 2·step, … */
export const nthTerm = (start, step, n) => start + step * (n - 1);
/** The first n terms as a list for display: "3, 7, 11, 15". */
export const firstTerms = (start, step, n) => Array.from({ length: n }, (_, i) => start + step * i).join(", ");
/** Term n of a doubling sequence: start, 2·start, 4·start, … */
export const nthDouble = (start, n) => start * 2 ** (n - 1);
export const firstDoubles = (start, n) => Array.from({ length: n }, (_, i) => start * 2 ** i).join(", ");

// ---------------------------------------------------------------- repeating shape patterns
const SHAPES = ["circle", "square", "triangle", "star"];
export const patternShape = (i) => SHAPES[i];
/** The shape at position n (1-based) of a repeating pattern given as a string of shape indexes, e.g. "012" or "0011". */
export const shapeAt = (pattern, n) => SHAPES[Number(String(pattern)[(n - 1) % String(pattern).length])];
export const patternLength = (pattern) => String(pattern).length;

const r1 = (x) => Math.round(x * 10) / 10;
const svg = (w, h, label, body) =>
  `<svg class="fig" viewBox="0 0 ${w} ${h}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg" ` +
  `font-family="system-ui, sans-serif" font-size="11" fill="none" stroke="currentColor" stroke-width="1">${body}</svg>`;
const text = (x, y, s, extra = "") =>
  `<text x="${r1(x)}" y="${r1(y)}" fill="currentColor" stroke="none"${/text-anchor/.test(extra) ? "" : ` text-anchor="middle"`}${extra}>${s}</text>`;
const FILL = ["#d0473b", "#3b7dd8", "#e0a526", "#3f9a3f"];
function drawShape(i, cx, cy, r) {
  const f = `style="fill: ${FILL[i]}" stroke="currentColor"`;
  if (i === 0) return `<circle cx="${r1(cx)}" cy="${r1(cy)}" r="${r}" ${f}/>`;
  if (i === 1) return `<rect x="${r1(cx - r)}" y="${r1(cy - r)}" width="${2 * r}" height="${2 * r}" ${f}/>`;
  if (i === 2) return `<path d="M${r1(cx)} ${r1(cy - r)} L${r1(cx + r)} ${r1(cy + r)} L${r1(cx - r)} ${r1(cy + r)} Z" ${f}/>`;
  const pts = Array.from({ length: 10 }, (_, k) => {
    const a = -Math.PI / 2 + (k * Math.PI) / 5, rr = k % 2 ? r * 0.45 : r;
    return `${r1(cx + rr * Math.cos(a))} ${r1(cy + rr * Math.sin(a))}`;
  });
  return `<path d="M${pts.join(" L")} Z" ${f}/>`;
}
/** The first `shown` shapes of a repeating pattern, then a box with a question mark. */
export function shapeSequence(pattern, shown) {
  const gap = 36, w = (shown + 1) * gap + 16;
  let b = "";
  for (let n = 1; n <= shown; n++) b += drawShape(Number(String(pattern)[(n - 1) % String(pattern).length]), 8 + n * gap - 10, 30, 12);
  const x = 8 + (shown + 1) * gap - 10;
  b += `<rect x="${r1(x - 14)}" y="16" width="28" height="28" rx="4" stroke-dasharray="4 3"/>` + text(x, 36, "?", ` font-size="16" font-weight="bold"`);
  return svg(w, 60, "A row of shapes that repeats, ending with a question mark", b);
}

// ---------------------------------------------------------------- tracing algorithms
/** Start with a, then add b to it n times: the value at the end. */
export const traceAdd = (a, b, n) => a + b * n;
/** Start with a, then double it n times. */
export const traceDouble = (a, n) => a * 2 ** n;
/** IF x > limit THEN output "big" ELSE output "small". */
export const traceIf = (x, limit, yes, no) => (x > limit ? yes : no);

// ---------------------------------------------------------------- computer history (authored, TR-S)
// [about which year, the step]
const HISTORY = [
  [-2500, "the abacus is used for counting"], [1642, "Blaise Pascal builds a mechanical adding machine (the Pascaline)"],
  [1837, "Charles Babbage designs the Analytical Engine"], [1843, "Ada Lovelace writes the first computer program"],
  [1946, "ENIAC, an early electronic computer, is switched on"], [1981, "personal computers spread into offices and homes"],
  [2007, "smartphones with touch screens spread"],
];
export const historyYear = (i) => HISTORY[i][0];
export const historyStep = (i) => HISTORY[i][1];
// Generations: [number, technology, about when]
const GENERATIONS = [
  [1, "vacuum tubes", "about 1940 to 1956"], [2, "transistors", "about 1956 to 1963"], [3, "integrated circuits (chips)", "about 1964 to 1971"],
  [4, "microprocessors", "from about 1971"], [5, "artificial intelligence", "today and the future"],
];
export const generationTech = (g) => GENERATIONS[g - 1][1];
export const generationWhen = (g) => GENERATIONS[g - 1][2];

// ---------------------------------------------------------------- computer laboratory layouts
export const LAYOUTS = ["rows", "U-shape (along the walls)", "clusters (groups)"];
export const layoutName = (i) => LAYOUTS[i];
/** A computer laboratory seen from above: the board at the top, desks with screens in the given layout. */
export function labLayout(type) {
  const x0 = 20, y0 = 20, W = 260, H = 180;
  const desk = (x, y, rot = 0) => `<g transform="translate(${x} ${y}) rotate(${rot})"><rect x="-14" y="-9" width="28" height="18" style="fill: #c9c3b8" stroke="currentColor"/>` +
    `<rect x="-8" y="-7" width="16" height="4" style="fill: #3b7dd8"/></g>`;
  let b = `<rect x="${x0}" y="${y0}" width="${W}" height="${H}" stroke-width="3"/>` + `<rect x="${x0 + 80}" y="${y0 + 4}" width="100" height="6" fill="currentColor"/>` +
    text(x0 + 130, y0 + 24, "board", ` font-size="10"`) + `<rect x="${x0 + W - 50}" y="${y0 + H - 2}" width="34" height="4" style="fill: var(--card, #fff)" stroke="none"/>` +
    text(x0 + W - 33, y0 + H + 14, "door", ` font-size="10"`);
  if (type === 0) for (let r = 0; r < 3; r++) for (let c = 0; c < 5; c++) b += desk(x0 + 40 + c * 45, y0 + 70 + r * 40);
  if (type === 1) {
    for (let c = 0; c < 5; c++) b += desk(x0 + 50 + c * 40, y0 + H - 20, 180);
    for (let r = 0; r < 3; r++) b += desk(x0 + 20, y0 + 50 + r * 35, 90) + desk(x0 + W - 20, y0 + 50 + r * 35, -90);
  }
  if (type === 2) for (const [cx, cy] of [[90, 78], [200, 78], [145, 138]]) b += desk(x0 + cx - 18, y0 + cy - 12) + desk(x0 + cx + 18, y0 + cy - 12) + desk(x0 + cx - 18, y0 + cy + 12, 180) + desk(x0 + cx + 18, y0 + cy + 12, 180);
  return svg(300, 222, "A computer laboratory seen from above, showing how the desks are arranged", b);
}
