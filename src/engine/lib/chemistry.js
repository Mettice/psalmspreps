// Chemistry helpers for templates: elements and their symbols, and chemical formulas (parse, count atoms, display
// with subscripts). Used as {...maths, ...english, ...physics, ...chemistry}.
// The element table is authored (TR-K02): names in British school spelling (aluminium, sulfur).

// ---------------------------------------------------------------- elements (authored)
// [atomic number, symbol, name, kind]. kind: "metal" | "non-metal" | "metalloid".
const TABLE = [
  [1, "H", "hydrogen", "non-metal"], [2, "He", "helium", "non-metal"], [3, "Li", "lithium", "metal"], [4, "Be", "beryllium", "metal"],
  [5, "B", "boron", "metalloid"], [6, "C", "carbon", "non-metal"], [7, "N", "nitrogen", "non-metal"], [8, "O", "oxygen", "non-metal"],
  [9, "F", "fluorine", "non-metal"], [10, "Ne", "neon", "non-metal"], [11, "Na", "sodium", "metal"], [12, "Mg", "magnesium", "metal"],
  [13, "Al", "aluminium", "metal"], [14, "Si", "silicon", "metalloid"], [15, "P", "phosphorus", "non-metal"], [16, "S", "sulfur", "non-metal"],
  [17, "Cl", "chlorine", "non-metal"], [18, "Ar", "argon", "non-metal"], [19, "K", "potassium", "metal"], [20, "Ca", "calcium", "metal"],
  [26, "Fe", "iron", "metal"], [29, "Cu", "copper", "metal"], [30, "Zn", "zinc", "metal"], [47, "Ag", "silver", "metal"],
  [50, "Sn", "tin", "metal"], [53, "I", "iodine", "non-metal"], [79, "Au", "gold", "metal"], [80, "Hg", "mercury", "metal"], [82, "Pb", "lead", "metal"],
];
export const ELEMENTS = TABLE.map(([z, symbol, name, kind]) => ({ z, symbol, name, kind }));
const BY_SYMBOL = Object.fromEntries(ELEMENTS.map((e) => [e.symbol, e]));
const BY_NAME = Object.fromEntries(ELEMENTS.map((e) => [e.name, e]));
/** Symbols whose letters do not come from the English name (they come from Latin), TR-K02. */
export const LATIN = { Na: "natrium", K: "kalium", Fe: "ferrum", Cu: "cuprum", Ag: "argentum", Sn: "stannum", Au: "aurum", Hg: "hydrargyrum", Pb: "plumbum" };

export const symbolOf = (name) => { const e = BY_NAME[name]; if (!e) throw new RangeError(`unknown element ${name}`); return e.symbol; };
export const nameOf = (symbol) => { const e = BY_SYMBOL[symbol]; if (!e) throw new RangeError(`unknown symbol ${symbol}`); return e.name; };
export const kindOf = (symbol) => BY_SYMBOL[symbol].kind;
export const isSymbol = (s) => Object.prototype.hasOwnProperty.call(BY_SYMBOL, s);

// ---------------------------------------------------------------- formulas
/**
 * Parses a formula such as "H2O", "CaCO3", "Ca(OH)2" or "C6H12O6" into {symbol: count}, in order of first appearance.
 * Throws on anything that is not a valid formula made of known symbols.
 */
export function parseFormula(f) {
  let i = 0;
  const num = () => { const m = /^\d+/.exec(f.slice(i)); if (!m) return 1; i += m[0].length; return Number(m[0]); };
  function group() {
    const out = new Map();
    while (i < f.length && f[i] !== ")") {
      let part;
      if (f[i] === "(") {
        i++;
        part = group();
        if (f[i] !== ")") throw new SyntaxError(`missing ) in ${f}`);
        i++;
      } else {
        const m = /^[A-Z][a-z]?/.exec(f.slice(i));
        if (!m || !isSymbol(m[0])) throw new SyntaxError(`unknown symbol at "${f.slice(i)}" in ${f}`);
        i += m[0].length;
        part = new Map([[m[0], 1]]);
      }
      const k = num();
      for (const [s, c] of part) out.set(s, (out.get(s) || 0) + c * k);
    }
    return out;
  }
  const out = group();
  if (i !== f.length || !out.size) throw new SyntaxError(`bad formula ${f}`);
  return Object.fromEntries(out);
}
/** Number of atoms of one element in a formula: atomCount('H2SO4', 'O') = 4. */
export const atomCount = (f, symbol) => parseFormula(f)[symbol] || 0;
/** Total atoms in one unit of the formula: totalAtoms('H2SO4') = 7. */
export const totalAtoms = (f) => Object.values(parseFormula(f)).reduce((a, b) => a + b, 0);
/** How many different elements: elementCount('CaCO3') = 3. */
export const elementCount = (f) => Object.keys(parseFormula(f)).length;
/** The symbols in order: symbolsIn('CaCO3') = ['Ca', 'C', 'O']. */
export const symbolsIn = (f) => Object.keys(parseFormula(f));
/** The element names joined for a sentence: "hydrogen, sulfur and oxygen". */
export function elementNames(f) {
  const n = symbolsIn(f).map(nameOf);
  return n.length < 2 ? n.join("") : `${n.slice(0, -1).join(", ")} and ${n[n.length - 1]}`;
}
const SUBS = "₀₁₂₃₄₅₆₇₈₉";
/** A formula for display with subscript numbers: "H2SO4" → "H₂SO₄". */
export const formula = (f) => String(f).replace(/\d/g, (d) => SUBS[d]);
/** One line per element: "H: 2, S: 1, O: 4". */
export const atomList = (f) => Object.entries(parseFormula(f)).map(([s, c]) => `${s}: ${c}`).join(", ");
/** The Latin name behind a symbol, for the symbols that do not match the English name: latinName('Fe') = 'ferrum'. */
export const latinName = (symbol) => { if (!LATIN[symbol]) throw new RangeError(`${symbol} is not from a Latin name`); return LATIN[symbol]; };
