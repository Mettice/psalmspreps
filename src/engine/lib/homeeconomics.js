// Home Economics helpers for templates: the kitchen work triangle (computed), and kitchen drawings made by code with
// lettered parts, so the letter the question asks about always matches the drawing.
// Used as {...maths, ...english, ...physics, ...chemistry, ...geography, ...homeeconomics}.
// Conventions to be checked by a teacher (docs/teacher-review.md, TR-H*): work-triangle sides 1.2 m to 2.7 m each,
// total 4 m to 7.9 m (a common kitchen-design guideline).

// ---------------------------------------------------------------- lettered parts
const FACT = [1, 1, 2, 6, 24, 120, 720];
/** The k-th arrangement (0 ≤ k < n!) of the first n letters of A, B, C, … */
export function arrangement(k, n) {
  const letters = "ABCDEFGH".slice(0, n).split(""), out = [];
  let r = k % FACT[n];
  for (let i = n; i >= 1; i--) {
    out.push(letters.splice(Math.floor(r / FACT[i - 1]), 1)[0]);
    r %= FACT[i - 1];
  }
  return out;
}
/** The letter on part `i` (0-based) of a drawing with n lettered parts, in arrangement k. */
export const letterOf = (k, n, i) => arrangement(k, n)[i];

// ---------------------------------------------------------------- work triangle (TR-H convention)
export const SIDE_MIN = 1.2, SIDE_MAX = 2.7, TOTAL_MIN = 4, TOTAL_MAX = 7.9;
export const sideMin = () => SIDE_MIN;
export const sideMax = () => SIDE_MAX;
export const totalMin = () => TOTAL_MIN;
export const totalMax = () => TOTAL_MAX;
const r2 = (x) => Number(x.toFixed(2));
/** Total length of the work triangle (sink–cooker, cooker–fridge, fridge–sink), in metres. */
export const triangleTotal = (a, b, c) => r2(a + b + c);
/** Can three lengths make a triangle at all? Each side shorter than the other two together. */
export const isTriangle = (a, b, c) => a + b > c && b + c > a && a + c > b;
/** Is the work triangle well planned? Every side 1.2–2.7 m and the total 4–7.9 m. */
export const goodTriangle = (a, b, c) =>
  [a, b, c].every((s) => s >= SIDE_MIN && s <= SIDE_MAX) && triangleTotal(a, b, c) >= TOTAL_MIN && triangleTotal(a, b, c) <= TOTAL_MAX;
/** Why a triangle is or is not well planned, in words. */
export function triangleVerdict(a, b, c) {
  const sides = [a, b, c];
  if (sides.some((s) => s > SIDE_MAX)) return "a side is too long: too much walking";
  if (sides.some((s) => s < SIDE_MIN)) return "a side is too short: the work centres are crowded";
  const t = triangleTotal(a, b, c);
  if (t > TOTAL_MAX) return "the total is too long: too much walking";
  if (t < TOTAL_MIN) return "the total is too short: the work centres are crowded";
  return "it is well planned";
}

// ---------------------------------------------------------------- SVG
const r1 = (x) => Math.round(x * 10) / 10;
const svg = (w, h, label, body) =>
  `<svg class="fig" viewBox="0 0 ${w} ${h}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg" ` +
  `font-family="system-ui, sans-serif" font-size="11" fill="none" stroke="currentColor" stroke-width="1">${body}</svg>`;
const line = (x1, y1, x2, y2, extra = "") => `<line x1="${r1(x1)}" y1="${r1(y1)}" x2="${r1(x2)}" y2="${r1(y2)}"${extra}/>`;
const text = (x, y, s, extra = "") =>
  `<text x="${r1(x)}" y="${r1(y)}" fill="currentColor" stroke="none"${/text-anchor/.test(extra) ? "" : ` text-anchor="middle"`}${extra}>${s}</text>`;
const tag = (x, y, s) => `<circle cx="${r1(x)}" cy="${r1(y)}" r="10" style="fill: var(--card, #fff)"/>` + text(x, y + 4, s, ` font-weight="bold"`);
const rect = (x, y, w, h, extra = "") => `<rect x="${r1(x)}" y="${r1(y)}" width="${r1(w)}" height="${r1(h)}"${extra}/>`;
const WOOD = `style="fill: var(--fig-object, #c98b3a)"`, FIRE = `style="fill: var(--fig-red, #d0473b)"`, WATER = `style="fill: var(--fig-liquid, #6aa9e9)"`;
const GREY = `style="fill: #9a958c"`;

// A traditional kitchen seen from the front, with six lettered parts.
export const TRAD_PARTS = ["three-stone fireplace", "smoke rack", "firewood store", "water pot", "shelf for utensils", "mortar and pestle"];
export const tradPart = (i) => TRAD_PARTS[i];
export function traditionalKitchen(k) {
  const L = arrangement(k, 6);
  let b = `<path d="M30 90 L170 22 L310 90"/>` + rect(42, 90, 256, 150);
  for (let x = 50; x < 300; x += 18) b += line(x, 90 - (x < 170 ? (x - 30) * 0.48 : (310 - x) * 0.48) + 4, x - 8, 92, ` stroke-opacity="0.4"`);
  // fireplace: three stones, a pot, flames (centre floor)
  b += `<path d="M150 228 q10 -30 20 -6 q8 -26 18 6 z" ${FIRE}/>` +
    [[146, 230], [170, 233], [194, 230]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="10" ry="7" ${GREY}/>`).join("") +
    `<path d="M150 214 q20 14 40 0 l-2 -20 h-36 z" style="fill: #555" stroke="currentColor"/>`;
  // smoke rack above the fire
  b += rect(124, 134, 92, 6, WOOD) + [130, 150, 170, 190, 210].map((x) => line(x, 140, x, 152, ` stroke-dasharray="2 2"`)).join("") +
    line(124, 137, 108, 96) + line(216, 137, 232, 96);
  // firewood store (right floor)
  b += [0, 1, 2, 3, 4].map((i) => `<rect x="${238 + (i % 3) * 16}" y="${232 - 9 * Math.floor(i / 3) - 9}" width="16" height="8" rx="3" ${WOOD}/>`).join("");
  // water pot (left floor)
  b += `<path d="M64 238 q-14 -26 6 -36 v-6 h16 v6 q20 10 6 36 z" style="fill: #b26b3d" stroke="currentColor"/>`;
  // shelf with plates (left wall)
  b += rect(52, 150, 56, 5, WOOD) + `<ellipse cx="68" cy="146" rx="10" ry="4" ${WATER}/><ellipse cx="92" cy="146" rx="10" ry="4" ${WATER}/>`;
  // mortar and pestle (right, behind the firewood)
  b += `<path d="M262 196 h22 l-4 26 h-14 z" ${WOOD}/>` + line(276, 196, 290, 150, ` stroke-width="4"`);
  // letters
  b += tag(172, 176, L[0]) + tag(240, 140, L[1]) + tag(232, 206, L[2]) + tag(72, 178, L[3]) + tag(80, 128, L[4]) + tag(300, 170, L[5]);
  return svg(330, 250, "A traditional kitchen with lettered parts", b);
}

// Three kinds of fireplace side by side; arrangement k decides the order, labelled A, B, C from the left.
export const FIRE_TYPES = ["three-stone fireplace", "improved (mud) stove", "charcoal stove"];
export const fireType = (i) => FIRE_TYPES[i];
/** The letter under fireplace type i in fireplaces(k). */
export const fireLetter = (k, i) => "ABC"[arrangement(k, 3).indexOf("ABC"[i])];
export const fireAt = (k, letter) => FIRE_TYPES["ABC".indexOf(arrangement(k, 3)["ABC".indexOf(letter)])];
function fireplace(type, x) {
  const flame = (cx, y) => `<path d="M${cx - 10} ${y} q5 -20 10 -6 q5 -18 10 6 z" ${FIRE}/>`;
  const pot = (cx, y) => `<path d="M${cx - 22} ${y} q22 18 44 0 l-3 -22 h-38 z" style="fill: #555" stroke="currentColor"/>`;
  if (type === 0) return flame(x, 128) + [[x - 22, 130], [x, 134], [x + 22, 130]].map(([a, c]) => `<ellipse cx="${a}" cy="${c}" rx="11" ry="8" ${GREY}/>`).join("") + pot(x, 110);
  if (type === 1) return `<path d="M${x - 36} 136 v-34 q36 -14 72 0 v34 z" style="fill: #b26b3d" stroke="currentColor"/>` +
    `<path d="M${x - 12} 136 v-14 q12 -10 24 0 v14 z" style="fill: #3a2a20"/>` + flame(x, 134) + pot(x, 98);
  return `<path d="M${x - 26} 124 h52 l-6 -28 h-40 z" style="fill: #7a7f86" stroke="currentColor"/>` +
    [-20, 0, 20].map((d) => `<circle cx="${x + d / 1.6}" cy="104" r="4" style="fill: #222"/>`).join("") +
    `<circle cx="${x}" cy="108" r="4" ${FIRE}/>` + line(x - 20, 124, x - 26, 140, ` stroke-width="3"`) + line(x + 20, 124, x + 26, 140, ` stroke-width="3"`) + pot(x, 94);
}
export function fireplaces(k) {
  const order = arrangement(k, 3).map((l) => "ABC".indexOf(l));  // order[pos] = type shown at that position
  let b = line(10, 140, 330, 140, ` stroke-opacity="0.5"`);
  order.forEach((t, pos) => { b += fireplace(t, 60 + pos * 110) + tag(60 + pos * 110, 160, "ABC"[pos]); });
  return svg(340, 176, "Three kinds of fireplace, lettered A, B and C", b);
}

// Kitchen shapes seen from above: counters (grey) along the walls, the door in the bottom wall.
export const SHAPES = ["one-wall (single-line)", "galley (corridor)", "L-shaped", "U-shaped", "island"];
export const shapeName = (i) => SHAPES[i];
export function kitchenPlan(type) {
  const x0 = 40, y0 = 20, W = 220, H = 170, d = 28;
  let b = `<path d="M${x0} ${y0} h${W} v${H} h-${W / 2 - 20} m-40 0 h-${W / 2 - 20} z" stroke-width="4"/>` +
    `<path d="M${x0 + W / 2 - 20} ${y0 + H} a40 40 0 0 1 40 -40" stroke-dasharray="3 3"/>` + text(x0 + W / 2, y0 + H + 16, "door", ` font-size="10"`);
  const c = (x, y, w, h) => rect(x, y, w, h, ` ${GREY}`);
  if (type === 0) b += c(x0, y0, W, d);
  if (type === 1) b += c(x0, y0, d, H - 40) + c(x0 + W - d, y0, d, H - 40);
  if (type === 2) b += c(x0, y0, W, d) + c(x0, y0, d, H - 40);
  if (type === 3) b += c(x0, y0, W, d) + c(x0, y0, d, H - 40) + c(x0 + W - d, y0, d, H - 40);
  if (type === 4) b += c(x0, y0, W, d) + c(x0 + 60, y0 + 76, 100, 40);
  return svg(300, 212, "A kitchen seen from above, with the counters shaded", b);
}

// The front of a modern kitchen with six lettered parts.
export const UNIT_PARTS = ["wall unit", "base unit", "tall unit", "worktop", "sink", "cooker"];
export const unitPart = (i) => UNIT_PARTS[i];
export function kitchenUnits(k) {
  const L = arrangement(k, 6);
  const door = (x, y, w, h) => rect(x, y, w, h) + line(x + w - 8, y + h / 2 - 8, x + w - 8, y + h / 2 + 8, ` stroke-width="2"`);
  let b = line(10, 236, 330, 236, ` stroke-opacity="0.5"`);
  b += door(20, 30, 60, 70) + door(80, 30, 60, 70) + door(200, 30, 60, 70);   // wall units
  b += door(20, 170, 60, 66) + door(80, 170, 60, 66) + door(200, 170, 60, 66); // base units
  b += rect(140, 170, 60, 66) + rect(150, 196, 40, 30) + [152, 172].map((x) => `<ellipse cx="${x + 8}" cy="158" rx="9" ry="3"/>`).join(""); // cooker
  b += rect(14, 162, 252, 8, ` ${WOOD}`);                                       // worktop
  b += `<path d="M216 162 q24 10 48 0" ${WATER}/>` + `<path d="M240 162 v-18 h10"/>`; // sink + tap
  b += door(272, 30, 50, 206);                                                  // tall unit
  b += tag(110, 64, L[0]) + tag(50, 204, L[1]) + tag(297, 120, L[2]) + tag(100, 150, L[3]) + tag(240, 132, L[4]) + tag(170, 210, L[5]);
  return svg(340, 248, "The front of a modern kitchen with lettered parts", b);
}

// The work triangle drawn from its three sides (sink–cooker a, cooker–fridge b, fridge–sink c), lengths in metres.
export function workTriangle(a, b, c) {
  if (!isTriangle(a, b, c)) throw new RangeError(`workTriangle: ${a}, ${b}, ${c} is not a triangle`);
  // S at the origin, C along the x axis, F from the law of cosines
  const fx = (a * a + c * c - b * b) / (2 * a), fy = Math.sqrt(Math.max(0, c * c - fx * fx));
  const xs = [0, a, fx], ys = [0, 0, fy];
  const minX = Math.min(...xs), maxX = Math.max(...xs), maxY = Math.max(...ys);
  const s = Math.min(220 / (maxX - minX), 140 / Math.max(maxY, 0.5));
  const P = (x, y) => [50 + (x - minX) * s, 186 - y * s];
  const [S, C, F] = [P(0, 0), P(a, 0), P(fx, fy)];
  const G = [(S[0] + C[0] + F[0]) / 3, (S[1] + C[1] + F[1]) / 3];
  // each length sits just outside the middle of its side, away from the centre of the triangle
  const label = (p, q, len) => {
    const mx = (p[0] + q[0]) / 2, my = (p[1] + q[1]) / 2, dx = mx - G[0], dy = my - G[1], d = Math.hypot(dx, dy) || 1;
    return text(mx + (dx / d) * 18, my + (dy / d) * 18 + 4, `${len} m`, ` font-size="10"`);
  };
  let body = `<path d="M${r1(S[0])} ${r1(S[1])} L${r1(C[0])} ${r1(C[1])} L${r1(F[0])} ${r1(F[1])} Z" stroke-dasharray="5 3"/>`;
  for (const [p, name, fill] of [[S, "sink", WATER], [C, "cooker", FIRE], [F, "fridge", GREY]]) {
    body += `<rect x="${r1(p[0] - 9)}" y="${r1(p[1] - 9)}" width="18" height="18" ${fill} stroke="currentColor"/>` + text(p[0], p[1] + (p === F ? -14 : 24), name, ` font-size="10"`);
  }
  body += label(S, C, a) + label(C, F, b) + label(F, S, c);
  return svg(320, 220, "A kitchen work triangle joining the sink, the cooker and the fridge", body);
}
