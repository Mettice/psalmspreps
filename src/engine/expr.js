// A small, safe expression language for content JSON. No eval, no access to globals:
// expressions can only read template variables and call functions from the given library.
//
//   numbers 12 3.5   strings 'abc' "abc"   arrays [1, 2]   member a.b   index a[0]
//   + - * / % ^(power)   == != < <= > >=   && || !   cond ? x : y   f(x, y)
//
// `+` concatenates when either side is a string. `==` compares numbers with a tiny tolerance.

const OPS = ["==", "!=", "<=", ">=", "&&", "||", "+", "-", "*", "/", "%", "^", "<", ">", "!", "?", ":", "(", ")", "[", "]", ",", "."];

function tokenize(src) {
  const toks = [];
  let i = 0;
  while (i < src.length) {
    const c = src[i];
    if (/\s/.test(c)) { i++; continue; }
    if (/[0-9]/.test(c) || (c === "." && /[0-9]/.test(src[i + 1] || ""))) {
      const m = /^[0-9]*\.?[0-9]+(?:e[+-]?[0-9]+)?|^[0-9]+/.exec(src.slice(i));
      toks.push({ t: "num", v: Number(m[0]) });
      i += m[0].length;
      continue;
    }
    if (c === "'" || c === '"') {
      let j = i + 1, s = "";
      while (j < src.length && src[j] !== c) {
        if (src[j] === "\\" && j + 1 < src.length) { s += src[j + 1]; j += 2; } else s += src[j++];
      }
      if (j >= src.length) throw new SyntaxError(`unterminated string in: ${src}`);
      toks.push({ t: "str", v: s });
      i = j + 1;
      continue;
    }
    if (/[A-Za-z_]/.test(c)) {
      const m = /^[A-Za-z_][A-Za-z0-9_]*/.exec(src.slice(i));
      const w = m[0];
      toks.push(w === "true" || w === "false" ? { t: "lit", v: w === "true" } : { t: "id", v: w });
      i += w.length;
      continue;
    }
    const op = OPS.find((o) => src.startsWith(o, i));
    if (!op) throw new SyntaxError(`unexpected '${c}' in: ${src}`);
    toks.push({ t: "op", v: op });
    i += op.length;
  }
  return toks;
}

const BINARY = { "||": 1, "&&": 2, "==": 3, "!=": 3, "<": 4, "<=": 4, ">": 4, ">=": 4, "+": 5, "-": 5, "*": 6, "/": 6, "%": 6, "^": 8 };

function parse(src) {
  const toks = tokenize(src);
  let p = 0;
  const peek = () => toks[p];
  const isOp = (v) => peek() && peek().t === "op" && peek().v === v;
  const expect = (v) => {
    if (!isOp(v)) throw new SyntaxError(`expected '${v}' in: ${src}`);
    p++;
  };

  function primary() {
    const tok = toks[p++];
    if (!tok) throw new SyntaxError(`unexpected end of: ${src}`);
    let node;
    if (tok.t === "num" || tok.t === "str" || tok.t === "lit") node = { k: "lit", v: tok.v };
    else if (tok.t === "id") {
      if (isOp("(")) {
        p++;
        const args = [];
        if (!isOp(")")) do { args.push(ternary()); } while (isOp(",") && ++p);
        expect(")");
        node = { k: "call", f: tok.v, args };
      } else node = { k: "var", v: tok.v };
    } else if (tok.v === "(") { node = ternary(); expect(")"); }
    else if (tok.v === "[") {
      const items = [];
      if (!isOp("]")) do { items.push(ternary()); } while (isOp(",") && ++p);
      expect("]");
      node = { k: "arr", items };
    } else if (tok.v === "-") node = { k: "neg", x: unary() };
    else if (tok.v === "!") node = { k: "not", x: unary() };
    else throw new SyntaxError(`unexpected '${tok.v}' in: ${src}`);
    for (;;) {  // postfix: .member and [index]
      if (isOp(".")) { p++; const m = toks[p++]; node = { k: "idx", x: node, i: { k: "lit", v: m.v } }; }
      else if (isOp("[")) { p++; const i = ternary(); expect("]"); node = { k: "idx", x: node, i }; }
      else return node;
    }
  }
  function unary() { return primary(); }
  function binary(minPrec) {
    let left = unary();
    for (;;) {
      const tok = peek();
      const prec = tok && tok.t === "op" ? BINARY[tok.v] : undefined;
      if (prec === undefined || prec < minPrec) return left;
      p++;
      const right = binary(tok.v === "^" ? prec : prec + 1);  // ^ is right-associative
      left = { k: "bin", op: tok.v, a: left, b: right };
    }
  }
  function ternary() {
    const cond = binary(1);
    if (!isOp("?")) return cond;
    p++;
    const yes = ternary();
    expect(":");
    return { k: "cond", c: cond, y: yes, n: ternary() };
  }
  const tree = ternary();
  if (p !== toks.length) throw new SyntaxError(`unexpected '${toks[p].v}' in: ${src}`);
  return tree;
}

export function eq(a, b) {
  if (typeof a === "number" && typeof b === "number") return Math.abs(a - b) <= 1e-9 * Math.max(1, Math.abs(a), Math.abs(b));
  if (Array.isArray(a) && Array.isArray(b)) return a.length === b.length && a.every((x, i) => eq(x, b[i]));
  return a === b;
}

function run(n, scope, lib) {
  switch (n.k) {
    case "lit": return n.v;
    case "var":
      if (!Object.prototype.hasOwnProperty.call(scope, n.v)) throw new ReferenceError(`unknown variable '${n.v}'`);
      return scope[n.v];
    case "arr": return n.items.map((x) => run(x, scope, lib));
    case "idx": {
      const x = run(n.x, scope, lib), i = run(n.i, scope, lib);
      if (x === null || x === undefined || !Object.prototype.hasOwnProperty.call(Object(x), i)) {
        if (i === "length" && (typeof x === "string" || Array.isArray(x))) return x.length;
        throw new ReferenceError(`no member '${i}'`);
      }
      return x[i];
    }
    case "call": {
      if (!Object.prototype.hasOwnProperty.call(lib, n.f)) throw new ReferenceError(`unknown function '${n.f}'`);
      return lib[n.f](...n.args.map((x) => run(x, scope, lib)));
    }
    case "neg": return -run(n.x, scope, lib);
    case "not": return !run(n.x, scope, lib);
    case "cond": return run(n.c, scope, lib) ? run(n.y, scope, lib) : run(n.n, scope, lib);
    case "bin": {
      if (n.op === "&&") return run(n.a, scope, lib) && run(n.b, scope, lib);
      if (n.op === "||") return run(n.a, scope, lib) || run(n.b, scope, lib);
      const a = run(n.a, scope, lib), b = run(n.b, scope, lib);
      switch (n.op) {
        case "+": return a + b;
        case "-": return a - b;
        case "*": return a * b;
        case "/": return a / b;
        case "%": return ((a % b) + b) % b;
        case "^": return a ** b;
        case "==": return eq(a, b);
        case "!=": return !eq(a, b);
        case "<": return a < b;
        case "<=": return a <= b;
        case ">": return a > b;
        case ">=": return a >= b;
      }
    }
  }
  throw new Error(`bad node ${n.k}`);
}

const cache = new Map();

export function evaluate(src, scope, lib) {
  if (typeof src !== "string") return src;
  let tree = cache.get(src);
  if (!tree) { tree = parse(src); cache.set(src, tree); }
  return run(tree, scope, lib);
}

// "Convert {n} to base {b}." -> each {expr} is evaluated. "{{" and "}}" are literal braces.
export function render(template, scope, lib, show = String) {
  if (typeof template !== "string") return template;
  let out = "", i = 0;
  while (i < template.length) {
    const c = template[i];
    if (c === "{" && template[i + 1] === "{") { out += "{"; i += 2; continue; }
    if (c === "}" && template[i + 1] === "}") { out += "}"; i += 2; continue; }
    if (c === "{") {
      let depth = 1, j = i + 1, quote = null;
      for (; j < template.length && depth; j++) {
        const d = template[j];
        if (quote) { if (d === quote) quote = null; continue; }
        if (d === "'" || d === '"') quote = d;
        else if (d === "{") depth++;
        else if (d === "}") depth--;
      }
      if (depth) throw new SyntaxError(`unclosed '{' in: ${template}`);
      out += show(evaluate(template.slice(i + 1, j - 1), scope, lib));
      i = j;
      continue;
    }
    out += c;
    i++;
  }
  return out;
}
