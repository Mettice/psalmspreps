// Geography helpers for templates: local time from longitude, map scale, grid references, latitude and longitude,
// and maps drawn as SVG from the question's own numbers (so the answer is computed, never typed).
// Used as {...maths, ...english, ...physics, ...chemistry, ...geography}.
// Conventions to be checked by a teacher (docs/teacher-review.md, TR-G*): 15° of longitude = 1 hour, 1° = 4 minutes,
// places east of Greenwich are ahead; clock times in the 12-hour style ("2:20 p.m.", "12:00 noon"); Tropics at 23½°,
// Polar Circles at 66½°; a leap year is a year divisible by 4 (the Form 1 rule; years 2001–2099 only).

// ---------------------------------------------------------------- latitude and longitude
// Latitude: + north, − south. Longitude: + east, − west (degrees).
export const lat = (d) => (d === 0 ? "0°" : `${Math.abs(d)}°${d > 0 ? "N" : "S"}`);
export const lon = (d) => (d === 0 ? "0°" : Math.abs(d) === 180 ? "180°" : `${Math.abs(d)}°${d > 0 ? "E" : "W"}`);
/** A position as it is written: latitude first, then longitude ("4°N, 12°E"). */
export const latlon = (la, lo) => `${lat(la)}, ${lon(lo)}`;
/** Difference in longitude between two places (both sides of Greenwich: add; same side: subtract). */
export const lonDiff = (a, b) => Math.abs(a - b);

// ---------------------------------------------------------------- time
/** Minutes of time for a difference in longitude: 360° in 24 hours, so 15° = 1 hour and 1° = 4 minutes. */
const MPD = (24 * 60) / 360, DPH = 360 / 24;
export const minutesPerDegree = () => MPD;
export const degreesPerHour = () => DPH;
export const timeForDegrees = (d) => d * MPD;
const mod = (a, n) => ((a % n) + n) % n;
/** A clock time from minutes after midnight, 12-hour style: 0 → "12:00 midnight", 720 → "12:00 noon", 860 → "2:20 p.m.". */
export function clock(m) {
  m = mod(Math.round(m), 24 * 60);
  if (m === 0) return "12:00 midnight";
  if (m === 720) return "12:00 noon";
  const h = Math.floor(m / 60), mm = String(m % 60).padStart(2, "0");
  return `${h % 12 === 0 ? 12 : h % 12}:${mm} ${h < 12 ? "a.m." : "p.m."}`;
}
/** Hours and minutes from a number of minutes: 140 → "2 hours 20 minutes", 60 → "1 hour". */
export function duration(m) {
  const h = Math.floor(m / 60), r = m % 60;
  const hs = h ? `${h} hour${h === 1 ? "" : "s"}` : "", ms = r ? `${r} minute${r === 1 ? "" : "s"}` : "";
  return [hs, ms].filter(Boolean).join(" ") || "0 minutes";
}
/** Local time (minutes after midnight) at longitude `to` when it is `t` at longitude `from`: east is ahead. */
export const localTime = (t, from, to) => t + (to - from) * MPD;
/** True if the local time stays on the same day (no midnight crossed). */
export const sameDay = (m) => m >= 0 && m < 24 * 60;
/** The standard time zone of a meridian that is a multiple of 15°: 45 → "GMT+3", −30 → "GMT−2", 0 → "GMT". */
export function zone(d) {
  const h = d / DPH;
  if (!Number.isInteger(h)) throw new RangeError(`${d}° is not a standard meridian`);
  return h === 0 ? "GMT" : `GMT${h > 0 ? "+" : "−"}${Math.abs(h)}`;
}

/** Leap years by the Form 1 rule (divisible by 4), for 2001–2099 where it agrees with the full calendar rule. */
export function isLeap(y) {
  if (y < 2001 || y > 2099) throw new RangeError(`isLeap: use years 2001–2099 (got ${y})`);
  return y % 4 === 0;
}
export const daysInYear = (y) => (isLeap(y) ? 366 : 365);

// ---------------------------------------------------------------- map scale
/** Real distance in km for `cm` on a map with scale 1 : n. */
export const realKm = (cm, n) => Number(((cm * n) / 100000).toPrecision(12));
/** Map distance in cm for `km` on the ground with scale 1 : n. */
export const mapCm = (km, n) => Number(((km * 100000) / n).toPrecision(12));
/** The scale as a ratio, "1 : 50 000" (digits grouped from 5 digits up, as in maths fmt). */
export const ratio = (n) => `1 : ${n >= 10000 ? String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " ") : n}`;

// ---------------------------------------------------------------- grid references
const p2 = (n) => String(n).padStart(2, "0");
/** 4-figure grid reference of the square whose bottom-left corner is easting e, northing n: eastings first. */
export const grid4 = (e, n) => `${p2(e)}${p2(n)}`;
/** 6-figure grid reference: easting, tenths across, northing, tenths up. */
export const grid6 = (e, te, n, tn) => `${p2(e)}${te}${p2(n)}${tn}`;

// ---------------------------------------------------------------- SVG
// Same drawing style as the Physics instruments: role="img", a label that does NOT give the answer, page colours.
const r1 = (x) => Math.round(x * 10) / 10;
const svg = (w, h, label, body) =>
  `<svg class="fig" viewBox="0 0 ${w} ${h}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg" ` +
  `font-family="system-ui, sans-serif" font-size="11" fill="none" stroke="currentColor" stroke-width="1">${body}</svg>`;
const line = (x1, y1, x2, y2, extra = "") => `<line x1="${r1(x1)}" y1="${r1(y1)}" x2="${r1(x2)}" y2="${r1(y2)}"${extra}/>`;
// Centred unless `extra` sets its own text-anchor (an attribute written twice is invalid SVG, and HTML keeps the first).
const text = (x, y, s, extra = "") =>
  `<text x="${r1(x)}" y="${r1(y)}" fill="currentColor" stroke="none"${/text-anchor/.test(extra) ? "" : ` text-anchor="middle"`}${extra}>${s}</text>`;
const dot = (x, y, r = 4) => `<circle cx="${r1(x)}" cy="${r1(y)}" r="${r}" fill="currentColor"/>`;

const PLACES = ["school", "church", "market", "well", "clinic", "mosque", "bridge", "farm"];
/** The names used on code-drawn grid maps (a function: templates can only call the library). */
export const gridPlaces = () => [...PLACES];

/**
 * A grid map: 5 × 5 squares, eastings e0 … e0+5 along the bottom, northings n0 … n0+5 up the side.
 * `marks` is a list of [name, x, y] with x, y in squares from the bottom-left corner (2.5 = middle of the third square).
 */
export function gridMap(e0, n0, marks) {
  const S = 56, x0 = 34, y0 = 12, N = 5;
  const X = (x) => x0 + x * S, Y = (y) => y0 + (N - y) * S;
  let body = `<rect x="${x0}" y="${y0}" width="${N * S}" height="${N * S}"/>`;
  for (let i = 0; i <= N; i++) {
    body += line(X(i), Y(0), X(i), Y(N), ` stroke-opacity="0.6"`) + line(X(0), Y(i), X(N), Y(i), ` stroke-opacity="0.6"`);
    body += text(X(i), Y(0) + 16, p2(e0 + i)) + text(x0 - 6, Y(i) + 4, p2(n0 + i), ` text-anchor="end"`);
  }
  for (const [name, x, y] of marks) {
    if (x <= 0 || x >= N || y <= 0 || y >= N) throw new RangeError(`gridMap: ${name} at ${x}, ${y} is off the map`);
    body += dot(X(x), Y(y)) + text(X(x), Y(y) - 7, name, ` font-size="10"`);
  }
  body += text(X(N / 2), Y(0) + 32, "eastings →", ` font-size="10"`);
  return svg(x0 + N * S + 12, y0 + N * S + 38, "A grid map with numbered grid lines", body);
}

/**
 * Lines of latitude and longitude around a place: parallels la0, la0+step, … (4 spaces) and meridians lo0, lo0+step, …
 * `points` is a list of [letter, latitude, longitude].
 */
export function graticule(la0, lo0, step, points) {
  const N = 4, S = 62, x0 = 52, y0 = 14;
  const X = (lo) => x0 + ((lo - lo0) / step) * S, Y = (la) => y0 + (N - (la - la0) / step) * S;
  let body = "";
  for (let i = 0; i <= N; i++) {
    const la = la0 + i * step, lo = lo0 + i * step;
    body += line(X(lo0), Y(la), X(lo0 + N * step), Y(la), la === 0 ? ` stroke-width="2"` : ` stroke-opacity="0.6"`);
    body += line(X(lo), Y(la0), X(lo), Y(la0 + N * step), lo === 0 ? ` stroke-width="2"` : ` stroke-opacity="0.6"`);
    body += text(x0 - 6, Y(la) + 4, lat(la), ` text-anchor="end"`) + text(X(lo), Y(la0) + 16, lon(lo));
  }
  for (const [name, la, lo] of points) {
    if (la < la0 || la > la0 + N * step || lo < lo0 || lo > lo0 + N * step) throw new RangeError(`graticule: ${name} is off the map`);
    body += dot(X(lo), Y(la)) + text(X(lo) + 7, Y(la) - 6, name, ` text-anchor="start" font-weight="bold"`);
  }
  return svg(x0 + N * S + 26, y0 + N * S + 24, "Lines of latitude and longitude with lettered places", body);
}

// The marginal information on a map, in the order of the letters before they are shuffled.
const MARGIN = ["title", "key", "scale", "north arrow", "grid numbers"];
export const marginParts = MARGIN;
/** The k-th arrangement (0 ≤ k < 120) of the letters A–E over the five parts. */
function arrangement(k) {
  const letters = ["A", "B", "C", "D", "E"], out = [];
  let r = k;
  for (let i = 5; i >= 1; i--) {
    const f = [1, 1, 2, 6, 24][i - 1];
    out.push(letters.splice(Math.floor(r / f), 1)[0]);
    r %= f;
  }
  return out;
}
/** The letter that points to a part of the map in arrangement k: marginLetter(0, 'title') = 'A'. */
export const marginLetter = (k, part) => arrangement(k)[MARGIN.indexOf(part)];
/** The part a letter points to in arrangement k. */
export const marginPart = (k, letter) => MARGIN[arrangement(k).indexOf(letter)];
/** A small sketch map with its marginal information, each part pointed to by a letter (arrangement k). */
export function marginMap(k) {
  const L = arrangement(k);
  const tag = (x, y, s) => `<circle cx="${x}" cy="${y}" r="9" style="fill: var(--card, #fff)"/>` + text(x, y + 4, s, ` font-weight="bold"`);
  let body = `<rect x="40" y="40" width="210" height="150"/>`;
  // map content: a river, a road and a few houses (not part of the question)
  body += `<path d="M40 150 C 90 130, 120 170, 170 140 S 230 100, 250 110" style="stroke: var(--fig-liquid, #6aa9e9)" stroke-width="3"/>`;
  body += `<path d="M60 40 L 110 190" stroke-dasharray="6 3"/>`;
  for (const [x, y] of [[150, 80], [165, 90], [190, 75], [120, 110]]) body += `<rect x="${x}" y="${y}" width="8" height="8" fill="currentColor"/>`;
  // title (top)
  body += text(145, 26, "NKONGSAMBA AREA", ` font-weight="bold" font-size="12"`) + tag(28, 22, L[0]);
  // key (right)
  body += `<rect x="262" y="40" width="70" height="78"/>` + text(297, 54, "Key", ` font-weight="bold"`) +
    line(270, 68, 290, 68, ` style="stroke: var(--fig-liquid, #6aa9e9)" stroke-width="3"`) + text(296, 72, "river", ` text-anchor="start" font-size="10"`) +
    line(270, 86, 290, 86, ` stroke-dasharray="6 3"`) + text(296, 90, "road", ` text-anchor="start" font-size="10"`) +
    `<rect x="276" y="99" width="8" height="8" fill="currentColor"/>` + text(296, 107, "house", ` text-anchor="start" font-size="10"`) + tag(345, 52, L[1]);
  // scale line (bottom)
  body += line(60, 214, 180, 214) + [0, 1, 2, 3].map((i) => line(60 + i * 40, 209, 60 + i * 40, 219)).join("") +
    text(60, 230, "0", ` font-size="10"`) + text(100, 230, "1", ` font-size="10"`) + text(140, 230, "2", ` font-size="10"`) + text(180, 230, "3 km", ` font-size="10"`) + tag(204, 214, L[2]);
  // north arrow (right, below the key)
  body += `<path d="M297 178 L297 140 M290 152 L297 140 L304 152"/>` + text(297, 192, "N", ` font-weight="bold"`) + tag(322, 150, L[3]);
  // grid numbers (along the frame)
  for (let i = 0; i <= 3; i++) body += text(40 + i * 70, 204, 30 + i, ` font-size="9"`) + line(40 + i * 70, 190, 40 + i * 70, 194);
  body += tag(22, 196, L[4]);
  return svg(360, 240, "A sketch map with lettered parts around it", body);
}

/**
 * The Earth seen from above the North Pole, with the Sun's rays from the left (so the left half is in daylight).
 * The Earth turns anticlockwise in this view (west to east). A town is marked at angle `a` (degrees, anticlockwise
 * from the right-hand side).
 */
export function dayNight(a) {
  const cx = 210, cy = 132, R = 80, rad = (a * Math.PI) / 180;
  const tx = cx + R * Math.cos(rad), ty = cy - R * Math.sin(rad);
  let body = "";
  for (const y of [72, 102, 132, 162, 192]) body += line(14, y, 86, y) + `<path d="M80 ${y - 4} L86 ${y} L80 ${y + 4}"/>`;
  body += text(48, 52, "Sun’s rays", ` font-size="10"`);
  body += `<path d="M${cx} ${cy - R} A ${R} ${R} 0 0 0 ${cx} ${cy + R} Z" style="fill: #f2d16b" stroke="none" opacity="0.7"/>`;
  body += `<path d="M${cx} ${cy - R} A ${R} ${R} 0 0 1 ${cx} ${cy + R} Z" style="fill: #3b4a6b" stroke="none" opacity="0.75"/>`;
  body += `<circle cx="${cx}" cy="${cy}" r="${R}"/>` + dot(cx, cy, 3) + text(cx + 12, cy + 4, "N", ` font-size="10" text-anchor="start"`);
  body += `<path d="M${cx + 58} ${cy - R - 8} A ${R + 14} ${R + 14} 0 0 0 ${cx - 58} ${cy - R - 8}"/>` +
    `<path d="M${cx - 50} ${cy - R - 14} L${cx - 58} ${cy - R - 8} L${cx - 49} ${cy - R - 2}"/>`;
  body += `<circle cx="${r1(tx)}" cy="${r1(ty)}" r="6" style="fill: var(--fig-red, #d0473b)" stroke="currentColor"/>` +
    text(cx + (R + 22) * Math.cos(rad), cy - (R + 22) * Math.sin(rad) + 4, "T", ` font-weight="bold"`);
  return svg(320, 248, "The Earth seen from above the North Pole, lit by the Sun, with a town marked T", body);
}
/** Day or night at the town in dayNight(a): day on the side facing the Sun (the left half). */
export const dayOrNight = (a) => (Math.cos((a * Math.PI) / 180) < 0 ? "day" : "night");
/** The Earth turns anticlockwise in the drawing: a town at the top (≈ 90°) is moving into daylight, at the bottom out of it. */
export const sunriseOrSunset = (a) => (Math.sin((a * Math.PI) / 180) > 0 ? "sunrise" : "sunset");

// The parallels on a globe, from the top: [name, latitude] (TR-G convention 23½° and 66½°).
export const PARALLELS = [
  ["Arctic Circle", 66.5], ["Tropic of Cancer", 23.5], ["Equator", 0], ["Tropic of Capricorn", -23.5], ["Antarctic Circle", -66.5],
];
export const parallelName = (i) => PARALLELS[i][0];
export const parallelLat = (i) => PARALLELS[i][1];
const half = (d) => (Number.isInteger(d) ? `${Math.abs(d)}` : `${Math.floor(Math.abs(d))}½`);
/** A latitude with the ½ sign: halfLat(23.5) = "23½°N". */
export const halfLat = (d) => (d === 0 ? "0°" : `${half(d)}°${d > 0 ? "N" : "S"}`);
/** A globe with the five main parallels, lettered A–E from the top. */
export function parallels() {
  const cx = 150, cy = 120, R = 100;
  let body = `<circle cx="${cx}" cy="${cy}" r="${R}"/>` + line(cx, cy - R - 10, cx, cy + R + 10, ` stroke-dasharray="4 3"`) +
    text(cx, cy - R - 14, "North Pole", ` font-size="10"`) + text(cx, cy + R + 22, "South Pole", ` font-size="10"`);
  PARALLELS.forEach(([, d], i) => {
    const y = cy - R * Math.sin((d * Math.PI) / 180), w = R * Math.cos((d * Math.PI) / 180);
    body += line(cx - w, y, cx + w, y, d === 0 ? ` stroke-width="2"` : "") + text(cx + w + 14, y + 4, "ABCDE"[i], ` font-weight="bold"`);
  });
  return svg(300, 250, "A globe with five lettered lines of latitude", body);
}

// ---------------------------------------------------------------- authored tables (TR-G items)
// Planets in order from the Sun, with the average distance in millions of km (rounded).
const PLANETS = [["Mercury", 58], ["Venus", 108], ["Earth", 150], ["Mars", 228], ["Jupiter", 778], ["Saturn", 1430], ["Uranus", 2870], ["Neptune", 4500]];
export const planetName = (i) => PLANETS[i][0];
export const planetDistance = (i) => PLANETS[i][1];
// Continents and oceans, largest first, with the area in millions of km² (rounded; sources differ slightly).
const CONTINENTS = [["Asia", 44.6], ["Africa", 30.4], ["North America", 24.7], ["South America", 17.8], ["Antarctica", 14.2], ["Europe", 10.2], ["Australia", 8.6]];
const OCEANS = [["Pacific Ocean", 165.2], ["Atlantic Ocean", 106.5], ["Indian Ocean", 73.4], ["Southern Ocean", 20.3], ["Arctic Ocean", 14.1]];
export const continentName = (i) => CONTINENTS[i][0];
export const continentArea = (i) => CONTINENTS[i][1];
export const oceanName = (i) => OCEANS[i][0];
export const oceanArea = (i) => OCEANS[i][1];
