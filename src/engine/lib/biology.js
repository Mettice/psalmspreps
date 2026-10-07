// Biology helpers for templates: microscope magnification (computed), an authored table of cell discoveries, and
// drawings made by code with lettered parts (microscope, plant cell, animal cell, soil profile), so the letter a question
// asks about always matches the drawing. Used as {...maths, …, ...history, ...biology}.
// Conventions to be checked by a teacher (docs/teacher-review.md, TR-L*): total magnification = eyepiece × objective;
// sizes in micrometres (µm), 1 mm = 1000 µm.

// ---------------------------------------------------------------- magnification
/** Total magnification of a compound microscope: eyepiece × objective (×10 and ×40 give ×400). */
export const magnification = (eyepiece, objective) => eyepiece * objective;
/** Real size = image size ÷ magnification. */
export const realSize = (image, mag) => Number((image / mag).toPrecision(12));
/** Image size = real size × magnification. */
export const imageSize = (real, mag) => Number((real * mag).toPrecision(12));

// ---------------------------------------------------------------- cell discoveries (authored, TR-L)
const DISCOVERIES = [
  [1665, "Robert Hooke", "looked at thin slices of cork and named the little boxes he saw “cells”"],
  [1674, "Antonie van Leeuwenhoek", "made strong lenses and was the first to see living micro-organisms"],
  [1838, "Matthias Schleiden", "said that all plants are made of cells"],
  [1839, "Theodor Schwann", "said that all animals are made of cells"],
];
export const discoveryYear = (i) => DISCOVERIES[i][0];
export const discoverer = (i) => DISCOVERIES[i][1];
export const discoveryWhat = (i) => DISCOVERIES[i][2];

// ---------------------------------------------------------------- lettered parts
const FACT = [1, 1, 2, 6, 24, 120, 720, 5040, 40320];
/** The k-th arrangement of the first n letters A, B, C, … (0 ≤ k < n!). */
export function bioArrangement(k, n) {
  const letters = "ABCDEFGH".slice(0, n).split(""), out = [];
  let r = k % FACT[n];
  for (let i = n; i >= 1; i--) {
    out.push(letters.splice(Math.floor(r / FACT[i - 1]), 1)[0]);
    r %= FACT[i - 1];
  }
  return out;
}
/** The letter on part i of a drawing with n lettered parts, in arrangement k. */
export const bioLetter = (k, n, i) => bioArrangement(k, n)[i];

const r1 = (x) => Math.round(x * 10) / 10;
const svg = (w, h, label, body) =>
  `<svg class="fig" viewBox="0 0 ${w} ${h}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg" ` +
  `font-family="system-ui, sans-serif" font-size="11" fill="none" stroke="currentColor" stroke-width="1">${body}</svg>`;
const line = (x1, y1, x2, y2, extra = "") => `<line x1="${r1(x1)}" y1="${r1(y1)}" x2="${r1(x2)}" y2="${r1(y2)}"${extra}/>`;
const text = (x, y, s, extra = "") =>
  `<text x="${r1(x)}" y="${r1(y)}" fill="currentColor" stroke="none"${/text-anchor/.test(extra) ? "" : ` text-anchor="middle"`}${extra}>${s}</text>`;
const tag = (x, y, s) => `<circle cx="${r1(x)}" cy="${r1(y)}" r="10" style="fill: var(--card, #fff)"/>` + text(x, y + 4, s, ` font-weight="bold"`);
/** A label line from a point on the drawing to a lettered tag. */
const pointer = (px, py, tx, ty, s) => line(px, py, tx, ty, ` stroke-opacity="0.6"`) + `<circle cx="${r1(px)}" cy="${r1(py)}" r="2" fill="currentColor"/>` + tag(tx, ty, s);
const METAL = `style="fill: #8e949b"`, DARK = `style="fill: #4a4f55"`;

// A compound light microscope seen from the side, with eight lettered parts.
export const MICRO_PARTS = ["eyepiece", "objective lenses", "stage", "coarse focus knob", "fine focus knob", "mirror", "arm", "base"];
export const microPart = (i) => MICRO_PARTS[i];
export function microscope(k) {
  const L = bioArrangement(k, 8);
  let b = "";
  b += `<path d="M90 268 h150 l-10 -16 h-130 z" ${DARK}/>`;                                            // base
  b += `<path d="M200 252 v-60 q0 -70 -40 -110 l-14 12 q32 34 32 98 v60 z" ${METAL} stroke="currentColor"/>`; // arm
  b += `<rect x="96" y="176" width="110" height="10" ${DARK}/>` + `<rect x="104" y="170" width="26" height="4" ${METAL}/>`; // stage + clip
  b += `<rect x="118" y="44" width="26" height="78" transform="rotate(-20 131 83)" ${METAL} stroke="currentColor"/>`;   // body tube
  b += `<rect x="102" y="20" width="22" height="30" transform="rotate(-20 113 35)" ${DARK}/>`;                         // eyepiece
  b += `<rect x="128" y="124" width="36" height="12" rx="4" ${DARK}/>` + `<rect x="132" y="136" width="10" height="20" ${METAL} stroke="currentColor"/>` +
    `<rect x="148" y="136" width="10" height="14" ${METAL} stroke="currentColor"/>`;                                    // nosepiece + objectives
  b += `<circle cx="190" cy="150" r="13" ${DARK}/>` + `<circle cx="196" cy="206" r="8" ${DARK}/>`;                        // coarse, fine knobs
  b += `<ellipse cx="146" cy="226" rx="16" ry="6" transform="rotate(-20 146 226)" style="fill: #cfd6dc" stroke="currentColor"/>`; // mirror
  b += pointer(112, 30, 50, 30, L[0]) + pointer(140, 150, 70, 130, L[1]) + pointer(100, 181, 50, 186, L[2]) + pointer(200, 150, 268, 140, L[3]) +
    pointer(203, 206, 268, 200, L[4]) + pointer(134, 228, 60, 236, L[5]) + pointer(172, 90, 268, 84, L[6]) + pointer(236, 260, 288, 262, L[7]);
  return svg(310, 280, "A microscope with lettered parts", b);
}

// A plant cell with six lettered parts, and an animal cell with three.
export const PLANT_PARTS = ["cell wall", "cell membrane", "cytoplasm", "nucleus", "vacuole", "chloroplast"];
export const plantPart = (i) => PLANT_PARTS[i];
export function plantCell(k) {
  const L = bioArrangement(k, 6);
  let b = `<rect x="70" y="30" width="180" height="150" rx="6" stroke-width="5" style="stroke: #6b8f3a"/>` + `<rect x="78" y="38" width="164" height="134" rx="4"/>`;
  b += `<rect x="78" y="38" width="164" height="134" rx="4" style="fill: #e6f1d6" stroke="none" opacity="0.6"/>`;
  b += `<rect x="112" y="66" width="98" height="78" rx="18" style="fill: var(--fig-liquid, #6aa9e9)" opacity="0.35" stroke="currentColor"/>`;  // vacuole
  b += `<circle cx="222" cy="68" r="15" style="fill: #b38bd1" stroke="currentColor"/>` + `<circle cx="222" cy="68" r="5" fill="currentColor"/>`;  // nucleus
  for (const [x, y] of [[92, 58], [96, 150], [226, 152], [182, 160], [92, 108]]) b += `<ellipse cx="${x}" cy="${y}" rx="9" ry="5" style="fill: #3f9a3f" stroke="currentColor"/>`;
  b += pointer(71, 30, 30, 22, L[0]) + pointer(78, 128, 30, 140, L[1]) + pointer(104, 132, 40, 196, L[2]) + pointer(230, 68, 290, 56, L[3]) +
    pointer(170, 100, 290, 110, L[4]) + pointer(230, 152, 290, 170, L[5]);
  return svg(320, 210, "A plant cell with lettered parts", b);
}
export const ANIMAL_PARTS = ["cell membrane", "cytoplasm", "nucleus"];
export const animalPart = (i) => ANIMAL_PARTS[i];
export function animalCell(k) {
  const L = bioArrangement(k, 3);
  let b = `<path d="M90 100 q10 -66 90 -62 q80 6 74 70 q-6 64 -86 60 q-84 -4 -78 -68 z" style="fill: #f6dccf" stroke="currentColor"/>`;
  b += `<circle cx="168" cy="104" r="20" style="fill: #b38bd1" stroke="currentColor"/>` + `<circle cx="168" cy="104" r="6" fill="currentColor"/>`;
  b += pointer(92, 92, 40, 70, L[0]) + pointer(130, 140, 70, 176, L[1]) + pointer(184, 96, 280, 70, L[2]);
  return svg(320, 200, "An animal cell with lettered parts", b);
}

// A soil profile: four layers, lettered by arrangement k.
export const SOIL_LAYERS = ["topsoil", "subsoil", "weathered rock (parent material)", "bedrock"];
export const soilLayer = (i) => SOIL_LAYERS[i];
export function soilProfile(k) {
  const L = bioArrangement(k, 4);
  const layer = [[20, 46, "#4b3621"], [66, 60, "#9a6b3f"], [126, 50, "#b9a58a"], [176, 44, "#7d7d7d"]];
  let b = `<path d="M60 20 q10 -14 20 0 M100 20 q8 -16 18 0 M150 20 q10 -12 18 0" style="stroke: #3f9a3f" stroke-width="2"/>`;
  layer.forEach(([y, h, c], i) => {
    b += `<rect x="40" y="${y}" width="200" height="${h}" style="fill: ${c}" stroke="currentColor"/>`;
    if (i === 2) for (let x = 56; x < 236; x += 30) b += `<path d="M${x} ${y + 14} l10 -6 l10 8 l-8 10 z" style="fill: #8f8a80" stroke="currentColor"/>`;
    b += tag(266, y + h / 2, L[i]);
  });
  return svg(300, 230, "A soil profile with lettered layers", b);
}
