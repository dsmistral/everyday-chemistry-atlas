# FC4 Engine 34 — the census-tally expansion review engine (durable record, session 118 part 1)

The Field Companion FC4's Phase-3 adversarial review, part 1: the review engine, its honest run history, and its frozen clean battery. Engine 34 recomputes all 54 rows of the chapter's frozen run-3 block (Lab FC4.1) from scratch and compares against the frozen got and expect values, plus three integrity gates over the frozen block itself.

## Design (the binding spec — rebuild from this alone)

- **A review engine, not a drafter's engine.** The engine reads the chapter canvas (`/home/user/canvases/everyday-chem-atlas-fc4/CANVAS.md`), extracts the frozen run-3 battery block (the canvas's single fenced code block), and recomputes every row from its own independent spec, comparing recomputed got against the frozen got and the frozen expect.
- **The element table is DERIVED, not transcribed — the adversarial census.** The nine-element admission table {B, C, Ca, Cl, H, K, Na, O, Si} is backed out of the chapter's own pinned compositions: a four-pin boot system (H2O 180,150 + NaOH 399,970 + Na2CO3 1,059,880 + CH3COOH 600,520 myu; four equations, four unknowns H, O, Na, C, eliminated by substitution — C from 2C + 2(2H+O) = 600,520; then Na from NaOH, H from equating the two Na expressions, O from H2O), then one-equation extractions (K from KOH 561,050; Cl from NaCl 584,430; B from B(OH)3 618,310; Si from SiO2 600,830; Ca from calcium stearate 6,070,300 = Ca + 2(18C+35H+2O)). Eleven cross-checks against further pins: NaOCl 744,420; B(OH)4 788,380; Na2B4O7 2,012,130; glycerol C3H8O3 920,940; oleic 2,824,680; stearic 2,844,840; sodium oleate 3,044,500; sodium stearate 3,064,660; potassium oleate 3,205,580; potassium stearate 3,225,740; and NaBO2 657,980 — the NEW row's own value cross-checked in the census. Derived: H 10,080; O 159,990; Na 229,900; C 120,110; K 390,980; Cl 354,530; B 108,100; Si 280,850; Ca 400,780 (myu = 10⁻⁴ g/mol). The checksums T1/T2 are recomputed from the derived table (Σmyu = 2,055,320 → "2055.320"; Σ(i+1)·myu alphabetical = 10,781,930 → "10781.930").
- **Parsing by literal bracket expansion + a single tally pass.** The innermost bracket pair is found by scan and replaced by its content repeated by its trailing multiplier; the loop repeats until no bracket remains; then one left-to-right pass pairs symbols with their subscript digit runs. `rounds` (the S-row metric) = the maximum bracket nesting depth of the original segment. No recursion into formulas, no stacks, no depth-indexed coefficient maps, no production-rule rewriting, no shunting-yard, no regex rounds over the tape (coefficients and digit runs are read by anchored prefixes).
- **Arithmetic: integer centi-scale fixed-point.** u4 = myu×10⁴; whole-input and segment coefficients parsed as integer hundredths (0.35 → 35); mass accumulates as Σ segMass·segCoeffH·wholeMultH; the integrality gate is massU4 % 10⁴ (R8's CaCl₂·0.35H₂O refuses NON-EXACT at 11,728,925,000 u4 = 1,172,892.5000 myu). NO rationals, NO BigInt, NO gcd anywhere.
- **Gates, in firing order.** The P18 restricted-name gate first (the ten trade names of the chapter's recognition table, refused as exact strings); then the table refusal (longest-symbol match, two-letter candidate before one-letter, the two-letter candidate named on refusal — "TABLE REFUSES Pb", "TABLE REFUSES F"); the zero subscript; the unclosed paren; the stray decimal (a '.' in the tally region, including one directly after a digit run — the R7/R8 boundary: a decimal directly after a symbol's digits is a stray mid-tape, a decimal at a segment head is a legal hydrate coefficient); the mass integrality gate.
- **Displays.** g/mol at exactly 3 decimals (u4 → g/mol: divide by 10⁸); dose figures at per-row precision (4 decimals for D1/D2, 3 for D3/D4/D5); heat in kJ at 3 decimals; balance closures in myu with European dot separators + " EXACT" (e.g. "3.385.730 EXACT"); the must-fail catch prints the oxygen ledger — the book's master atom per Engine 33's recorded design — with euro-formatted masses and the gap in g; checksums displayed as Σmyu/1000 at 3 decimals; dimensions over {M, L, T, Θ} in that order, zero exponents omitted, every exponent printed ("M^1·L^-2").
- **Roundings**: half-up at the stated precision, integer arithmetic throughout (roundDiv = floor(n·10^dp/d), +1 when the doubled remainder reaches d).
- **The integrity gates (the review layer over the frozen block).** G1: the frozen block has 54 PASS rows and the summary "RUN 3 SUMMARY: 54/54 PASS — CLEAN", every frozen got == expect. G2: the canvas's frozen block ≡ the durable record fc4-engine33-record.md's run-3 block, line for line. G3: the census's eleven cross-checks all OK.

## Provenance

Fresh build, zero code shared with Engines 1–33, written independently this session. The design family is distinct from every recorded prior engine description: no unit-lattice (27), no prime-product (28), no run-history splicing (29), no stack-descent fixed-scale (30), no RPN shunting-yard integer-lattice (31), no depth-map fold with continued-fraction rationals (32), no fixed-point token-tape rewrite with Bareiss rank (33); and none of the main volume's drafter engines (recursive-descent, hand-coded atom-map, and the rest) — no code of any prior engine was read or reused at build time.

## Census and gates (verbatim, run 2)

```
CENSUS H = 10080 myu (derived)
CENSUS O = 159990 myu (derived)
CENSUS Na = 229900 myu (derived)
CENSUS C = 120110 myu (derived)
CENSUS K = 390980 myu (derived)
CENSUS Cl = 354530 myu (derived)
CENSUS B = 108100 myu (derived)
CENSUS Si = 280850 myu (derived)
CENSUS Ca = 400780 myu (derived)
CENSUS X NaOCl 744420 == 744420 (P4) OK
CENSUS X B(OH)4 788380 == 788380 (P16) OK
CENSUS X Na2B4O7 2012130 == 2012130 (P15) OK
CENSUS X glycerol C3H8O3 920940 == 920940 (P6) OK
CENSUS X oleic C18H34O2 2824680 == 2824680 (P7) OK
CENSUS X stearic C18H36O2 2844840 == 2844840 (P12) OK
CENSUS X sodium oleate 3044500 == 3044500 (P8) OK
CENSUS X sodium stearate 3064660 == 3064660 (P13) OK
CENSUS X potassium oleate 3205580 == 3205580 (P10) OK
CENSUS X potassium stearate 3225740 == 3225740 (P11) OK
CENSUS X NaBO2 (N1) 657980 == 657980 (N1) OK
G1 PASS | frozen block: 54 rows, summary CLEAN | rows=54
G2 PASS | canvas frozen block == durable record run-3 block | record lines=55
G3 PASS | census: 9 elements derived, 11 cross-checks OK
```

## Engine source (verbatim — the executed Engine 34, run-2 form)

```typescript
// ===== Engine 34 run 2 (post-repair) — census-tally expansion review engine =====
function fmtScaled(q: number, dp: number): string {
  if (dp === 0) return String(q);
  let s = String(q);
  if (s.length <= dp) s = "0".repeat(dp - s.length + 1) + s;
  return s.slice(0, s.length - dp) + "." + s.slice(s.length - dp);
}
function roundDiv(n: number, d: number, dp: number): string {
  const a = n * Math.pow(10, dp);
  let q = Math.floor(a / d); const r = a % d;
  if (2 * r >= d) q += 1;
  return fmtScaled(q, dp);
}
function euro(n: number): string {
  const s = String(n); let out = ""; const L = s.length;
  for (let i = 0; i < L; i++) { out += s[i]; if ((L - i - 1) % 3 === 0 && i < L - 1) out += "."; }
  return out;
}
const censusLog: string[] = [];
function deriveTable(): Record<string, number> {
  const pH2O = 180150, pNaOH = 399970, pNa2CO3 = 1059880, pCH3COOH = 600520;
  const pKOH = 561050, pNaCl = 584430, pBOH3 = 618310, pSiO2 = 600830, pCaSt = 6070300;
  const C = (pCH3COOH - 2 * pH2O) / 2;
  const H = (219820 - (1059880 - C - 3 * 180150) / 2) / 2;
  const O = pH2O - 2 * H;
  const Na = 219820 + H;
  const K = pKOH - O - H;
  const Cl = pNaCl - Na;
  const B = pBOH3 - 3 * (O + H);
  const Si = pSiO2 - 2 * O;
  const Ca = pCaSt - 2 * (18 * C + 35 * H + 2 * O);
  const T: Record<string, number> = { B, C, Ca, Cl, H, K, Na, O, Si };
  for (const k of ["H","O","Na","C","K","Cl","B","Si","Ca"]) censusLog.push("CENSUS " + k + " = " + T[k] + " myu (derived)");
  const xs: [string, number, string][] = [
    ["NaOCl", Na + O + Cl, "744420 (P4)"], ["B(OH)4", B + 4 * (O + H), "788380 (P16)"],
    ["Na2B4O7", 2 * Na + 4 * B + 7 * O, "2012130 (P15)"], ["glycerol C3H8O3", 3 * C + 8 * H + 3 * O, "920940 (P6)"],
    ["oleic C18H34O2", 18 * C + 34 * H + 2 * O, "2824680 (P7)"], ["stearic C18H36O2", 18 * C + 36 * H + 2 * O, "2844840 (P12)"],
    ["sodium oleate", 18 * C + 33 * H + Na + 2 * O, "3044500 (P8)"], ["sodium stearate", 18 * C + 35 * H + Na + 2 * O, "3064660 (P13)"],
    ["potassium oleate", 18 * C + 33 * H + K + 2 * O, "3205580 (P10)"], ["potassium stearate", 18 * C + 35 * H + K + 2 * O, "3225740 (P11)"],
    ["NaBO2 (N1)", Na + B + 2 * O, "657980 (N1)"],
  ];
  for (const [nm, v, lbl] of xs) {
    const want = parseInt(lbl); const ok = v === want;
    censusLog.push("CENSUS X " + nm + " " + v + (ok ? " == " : " != ") + lbl + (ok ? " OK" : " MISMATCH"));
    if (!ok) throw new Error("census cross-check failed: " + nm);
  }
  return T;
}
const TRADE = ["glyphosate","2,4-D","paraquat","diquat","malathion","chlorpyrifos","carbaryl","metaldehyde","warfarin","bromadiolone"];
class Refusal extends Error {}
function nestingDepth(s: string): number {
  let d = 0, max = 0;
  for (const ch of s) { if (ch === "(") { d++; if (d > max) max = d; } else if (ch === ")") d--; }
  return max;
}
function tallyStr(s: string, T: Record<string, number>): { counts: Record<string, number>; mass: number } {
  const counts: Record<string, number> = {}; let mass = 0;
  let i = 0;
  while (i < s.length) {
    const c = s[i];
    if (c === ".") throw new Refusal("SYNTAX (stray decimal)");
    let sym = "";
    if (i + 1 < s.length && /[A-Z]/.test(c) && /[a-z]/.test(s[i + 1])) {
      const two = s.slice(i, i + 2);
      if (T[two] !== undefined) sym = two;
    }
    if (!sym && T[c] !== undefined) sym = c;
    if (!sym) {
      const cand = (i + 1 < s.length && /[a-z]/.test(s[i + 1])) ? s.slice(i, i + 2) : c;
      throw new Refusal("TABLE REFUSES " + cand);
    }
    i += sym.length;
    let j = i; while (j < s.length && /[0-9]/.test(s[j])) j++;
    if (j < s.length && s[j] === "." && j > i) throw new Refusal("SYNTAX (stray decimal)");
    const sub = j > i ? parseInt(s.slice(i, j)) : 1;
    if (sub === 0) throw new Refusal("ZERO SUBSCRIPT");
    counts[sym] = (counts[sym] || 0) + sub;
    mass += T[sym] * sub;
    i = j;
  }
  return { counts, mass };
}
function expand(s: string): string {
  let t = s;
  while (t.includes("(")) {
    let expanded = false;
    for (let p = 0; p < t.length && !expanded; p++) {
      if (t[p] !== "(") continue;
      let q = -1, sn = 0;
      for (let r = p; r < t.length; r++) { if (t[r] === "(") sn++; else if (t[r] === ")") { sn--; if (sn === 0) { q = r; break; } } }
      if (q < 0) throw new Refusal("UNCLOSED PAREN");
      if (t.slice(p + 1, q).includes("(")) continue;
      let m = q + 1; while (m < t.length && /[0-9]/.test(t[m])) m++;
      const k = m > q + 1 ? parseInt(t.slice(q + 1, m)) : 1;
      if (k === 0) throw new Refusal("ZERO SUBSCRIPT");
      t = t.slice(0, p) + t.slice(p + 1, q).repeat(k) + t.slice(m);
      expanded = true;
    }
    if (!expanded) {
      const i2 = t.indexOf("("); let sn = 0, found = false;
      for (let r = i2; r < t.length; r++) { if (t[r] === "(") sn++; else if (t[r] === ")") { sn--; if (sn === 0) { found = true; break; } } }
      if (!found) throw new Refusal("UNCLOSED PAREN");
      throw new Error("expansion stalled: " + t);
    }
  }
  return t;
}
function compose(input: string, T: Record<string, number>): { kind: "ok"; hill: string; massU4: number; depth: number; disp: string } | { kind: "refused"; msg: string } {
  const raw = input.trim();
  if (TRADE.includes(raw)) return { kind: "refused", msg: "P18 REFUSES: '" + raw + "'" };
  let wholeH = 100, rest = raw;
  const mw = /^(\d+(?:\.\d{1,2})?)\s+(.+)$/.exec(rest);
  if (mw) { const [a, b] = mw[1].split("."); wholeH = parseInt(a) * 100 + (b ? parseInt(b.padEnd(2, "0")) : 0); rest = mw[2].trim(); }
  const segs = rest.split("·");
  let massU4 = 0, depth = 0;
  const cntU4: Record<string, number> = {};
  for (const segRaw of segs) {
    let seg = segRaw.trim(); let segH = 100;
    const ms = /^(\d+(?:\.\d{1,2})?)(?=[A-Za-z(])/.exec(seg);
    if (ms) { const [a, b] = ms[1].split("."); segH = parseInt(a) * 100 + (b ? parseInt(b.padEnd(2, "0")) : 0); seg = seg.slice(ms[1].length); }
    let counts: Record<string, number>, smass: number;
    try {
      const ex = expand(seg);
      depth = Math.max(depth, nestingDepth(seg));
      const r = tallyStr(ex, T); counts = r.counts; smass = r.mass;
    } catch (e) {
      if (e instanceof Refusal) {
        const m = e.message;
        const msg = (m === "UNCLOSED PAREN" || m === "SYNTAX (stray decimal)" || m === "ZERO SUBSCRIPT")
          ? m + " refused: '" + raw + "'" : m;
        return { kind: "refused", msg };
      }
      throw e;
    }
    massU4 += smass * segH * wholeH;
    for (const el in counts) cntU4[el] = (cntU4[el] || 0) + counts[el] * segH * wholeH;
  }
  if (massU4 % 10000 !== 0) return { kind: "refused", msg: "NON-EXACT refused: total mass " + roundDiv(massU4, 10000, 4) + " myu" };
  const ints: Record<string, number> = {};
  for (const el in cntU4) { if (cntU4[el] % 10000 !== 0) throw new Error("non-integer count " + el); ints[el] = cntU4[el] / 10000; }
  const keys = Object.keys(ints).sort();
  const order = ints["C"] !== undefined ? ["C", "H", ...keys.filter(k => k !== "C" && k !== "H")] : keys;
  let hill = "";
  for (const k of order) hill += k + (ints[k] > 1 ? String(ints[k]) : "");
  return { kind: "ok", hill, massU4, depth, disp: roundDiv(massU4, 100000000, 3) };
}
function eqSides(eq: string, T: Record<string, number>) {
  const sides = eq.split("->");
  const out: { atoms: Record<string, number>; massU4: number }[] = [];
  for (const sd of sides) {
    const atoms: Record<string, number> = {}; let massU4 = 0;
    for (const termRaw of sd.split("+")) {
      const term = termRaw.trim();
      const mt = /^(\d+)\s+(.+)$/.exec(term);
      const coeff = mt ? parseInt(mt[1]) : 1;
      const spec = mt ? mt[2] : term;
      const segs = spec.split("·"); const cnts: Record<string, number> = {}; let smy = 0;
      for (const sg of segs) {
        let s2 = sg.trim(); let sc = 1;
        const ms = /^(\d+)(?=[A-Za-z(])/.exec(s2);
        if (ms) { sc = parseInt(ms[1]); s2 = s2.slice(ms[1].length); }
        const rr = tallyStr(expand(s2), T);
        for (const k in rr.counts) cnts[k] = (cnts[k] || 0) + rr.counts[k] * sc;
        smy += rr.mass * sc;
      }
      for (const k in cnts) atoms[k] = (atoms[k] || 0) + cnts[k] * coeff;
      massU4 += smy * 10000 * coeff;
    }
    out.push({ atoms, massU4 });
  }
  return out;
}
async function main() {
  const T = deriveTable();
  const rr = await tools.file_system.read_file({ path: "/home/user/canvases/everyday-chem-atlas-fc4/CANVAS.md" });
  const canvas = typeof rr === "string" ? rr : (rr as any).content;
  const open = canvas.indexOf("```\n");
  const close = canvas.indexOf("```", open + 4);
  const block = canvas.substring(open + 4, close);
  const blockLines = block.split("\n").filter(l => l.length > 0);
  const gates: string[] = [];
  const rows = blockLines.filter(l => l.startsWith("PASS "));
  const summ = blockLines.find(l => l.startsWith("RUN 3 SUMMARY"));
  gates.push("G1 " + (rows.length === 54 && summ === "RUN 3 SUMMARY: 54/54 PASS — CLEAN" ? "PASS" : "FAIL") + " | frozen block: 54 rows, summary CLEAN | rows=" + rows.length);
  const rec = await tools.file_system.read_file({ path: "/home/user/knowledge/everyday-chem-book/fc4-engine33-record.md" });
  const record = typeof rec === "string" ? rec : (rec as any).content;
  const ri = record.indexOf("## Run-3 battery block");
  const rblock = record.substring(ri);
  const rLines = rblock.split("\n").filter(l => l.startsWith("PASS ") || l.startsWith("RUN 3 SUMMARY"));
  const same = rLines.length === blockLines.length && rLines.every((l, i) => l === blockLines[i]);
  gates.push("G2 " + (same ? "PASS" : "FAIL") + " | canvas frozen block == durable record run-3 block | record lines=" + rLines.length);
  const chk = censusLog.filter(l => l.startsWith("CENSUS X")).every(l => l.endsWith("OK"));
  gates.push("G3 " + (chk ? "PASS" : "FAIL") + " | census: 9 elements derived, 11 cross-checks OK");
  const frozen = rows.map(l => { const m = /^PASS (\S+) \| (.+) \| got "(.*)" \| expect "(.*)"$/.exec(l); return { id: m![1], desc: m![2], got: m![3], expect: m![4] }; });
  const SPEC: Record<string, any> = {
    T1: { k: "t1" }, T2: { k: "t2" },
    S1: { k: "comp", f: "H2O" }, S2: { k: "comp", f: "NaOH" }, S3: { k: "comp", f: "KOH" },
    S4: { k: "comp", f: "B(OH)3" }, S5: { k: "comp", f: "SiO2" }, S6: { k: "comp", f: "Na2B4O7·10H2O" },
    S7: { k: "comp", f: "C18H33KO2" }, S8: { k: "comp", f: "2 C2H5OH" },
    R1: { k: "ref", f: "glyphosate" }, R2: { k: "ref", f: "warfarin" }, R3: { k: "ref", f: "PbO" },
    R4: { k: "ref", f: "NaF" }, R5: { k: "ref", f: "Na0Cl" }, R6: { k: "ref", f: "(NaOCl" },
    R7: { k: "ref", f: "Na0.5Cl" }, R8: { k: "ref", f: "CaCl2·0.35H2O" },
    P1: { k: "pin", f: "H2O" }, P2: { k: "pin", f: "NaOH" }, P3: { k: "pin", f: "KOH" },
    P4: { k: "pin", f: "NaOCl" }, P5: { k: "pin", f: "CH3COOH" }, P6: { k: "pin", f: "C3H8O3" },
    P7: { k: "pin", f: "C18H34O2" }, P8: { k: "pin", f: "C18H33NaO2" }, P9: { k: "pin", f: "Ca(C18H35O2)2" },
    P10: { k: "pin", f: "C18H33KO2" }, P11: { k: "pin", f: "C18H35KO2" }, P12: { k: "pin", f: "C18H36O2" },
    P13: { k: "pin", f: "C18H35NaO2" }, P14: { k: "pin", f: "Na2CO3" }, P15: { k: "pin", f: "Na2B4O7" },
    P16: { k: "pin", f: "B(OH)4" }, P17: { k: "pin", f: "NaCl" }, N1: { k: "pin", f: "NaBO2" },
    B1: { k: "bal", eq: "C18H34O2 + KOH -> C18H33KO2 + H2O" },
    B2: { k: "bal", eq: "C18H36O2 + KOH -> C18H35KO2 + H2O" },
    B3: { k: "bal", eq: "4 B(OH)3 + 2 NaOH -> Na2B4O7 + 7 H2O" },
    B4: { k: "bal", eq: "B(OH)3 + NaOH -> NaBO2 + 2 H2O" },
    B5: { k: "bal", eq: "Na2B4O7 + 10 H2O -> Na2B4O7·10H2O" },
    B6: { k: "bal", eq: "2 C18H35NaO2 + CaCl2 -> Ca(C18H35O2)2 + 2 NaCl" },
    E7: { k: "bal", eq: "B(OH)3 + NaOH -> NaBO2 + H2O", mustFail: true },
    H1: { k: "kJ", J: (1000 * 4184 * 80) / 1000 }, H2: { k: "kJ", J: 4 * 334720 }, H3: { k: "kJ", J: 1000 * 2256 },
    D1: { k: "dose", n: 2000000, d: 30445, dp: 4, unit: " mmol/L" }, D2: { k: "dose", n: 5000000, d: 61831, dp: 4, unit: " mmol/L" },
    D3: { k: "dose", n: 250, d: 50, dp: 3, unit: " g/m2" }, D4: { k: "dose", n: 5, d: 2, dp: 3, unit: "%" }, D5: { k: "dose", n: 4, d: 2, dp: 3, unit: " L/m2" },
    W1: { k: "dim", v: { M: 1, L: -2 } }, W2: { k: "dim", v: { M: 1, L: 2, T: -2 } }, W3: { k: "dim", v: { L: 2, T: -2 } },
  };
  const recompute = (id: string): string => {
    const s = SPEC[id];
    if (!s) throw new Error("no spec for " + id);
    if (s.k === "t1") { let sum = 0; for (const k in T) sum += T[k]; return roundDiv(sum, 1000, 3); }
    if (s.k === "t2") { const ks = Object.keys(T).sort(); let sum = 0; ks.forEach((k, i) => sum += (i + 1) * T[k]); return roundDiv(sum, 1000, 3); }
    if (s.k === "kJ") return roundDiv(s.J, 1000, 3) + " kJ";
    if (s.k === "dose") return roundDiv(s.n, s.d, s.dp) + s.unit;
    if (s.k === "dim") { const order = ["M", "L", "T", "Θ"]; const parts: string[] = []; for (const b of order) { const v = s.v[b] || 0; if (v !== 0) parts.push(b + "^" + v); } return parts.join("·"); }
    if (s.k === "bal") {
      const [L, R] = eqSides(s.eq, T);
      const massLmyu = L.massU4 / 10000, massRmyu = R.massU4 / 10000;
      const els = [...new Set([...Object.keys(L.atoms), ...Object.keys(R.atoms)])].sort();
      const diffs = els.filter(e => (L.atoms[e] || 0) !== (R.atoms[e] || 0));
      if (s.mustFail) {
        if ((L.atoms["O"] || 0) === (R.atoms["O"] || 0)) throw new Error("must-fail: oxygen ledger matches");
        const gap = massLmyu - massRmyu;
        return "CAUGHT ATOMS O " + L.atoms["O"] + " vs " + R.atoms["O"] + ", mass " + euro(massLmyu) + " vs " + euro(massRmyu) + " myu, gap " + euro(gap) + " myu (" + roundDiv(gap, 10000, 3) + " g)";
      }
      if (diffs.length !== 0 || massLmyu !== massRmyu) throw new Error("balance row does not close: " + id + " diffs=" + diffs.join(","));
      return euro(massLmyu) + " EXACT";
    }
    const r = compose(s.f, T);
    if (s.k === "comp") { if (r.kind !== "ok") throw new Error("S row refused: " + id); return r.hill + " " + r.disp + " rounds=" + r.depth; }
    if (s.k === "ref") { if (r.kind !== "refused") throw new Error("R row not refused: " + id); return r.msg; }
    if (s.k === "pin") { if (r.kind !== "ok") throw new Error("P row refused: " + id); return r.disp; }
    throw new Error("unknown kind " + s.k);
  };
  const out: string[] = [...censusLog, ...gates];
  let pass = 0;
  for (const f of frozen) {
    let got2 = ""; let ok = false;
    try { got2 = recompute(f.id); ok = got2 === f.got && f.got === f.expect; }
    catch (e) { got2 = "ENGINE ERROR: " + (e as Error).message; }
    if (ok) pass++;
    out.push((ok ? "PASS " : "FAIL ") + f.id + " | " + f.desc + ' | got "' + got2 + '" | expect "' + f.expect + '"');
  }
  out.push("RUN 2 SUMMARY: " + pass + "/54 PASS" + (pass === 54 ? " — CLEAN" : ""));
  return out.join("\n");
}
```

## Run-1 FAIL block (verbatim — the five harness slips, named)

Run 1 scored 10/54. The ten passes were the ten refusal rows (R1–R8) and both checksums (T1, T2) — the engine core (census, parser, gates, arithmetic) was clean from the first run. G1/G2 passed at run 1; G3 FAILed on a harness-side filter bug. The 44 fails, verbatim (the S/P/N rows' mass displays printed myu instead of g/mol — slip (2); the B/E/H/D/W rows crashed at a shared compose() call on rows that carry no formula — slip (3)):

```
G3 FAIL | census: 9 elements derived, 11 cross-checks OK
FAIL S1 | H2O | got "H2O 180150.000 rounds=0" | expect "H2O 18.015 rounds=0"
FAIL S2 | NaOH | got "HNaO 399970.000 rounds=0" | expect "HNaO 39.997 rounds=0"
FAIL S3 | KOH | got "HKO 561050.000 rounds=0" | expect "HKO 56.105 rounds=0"
FAIL S4 | B(OH)3 | got "BH3O3 618310.000 rounds=1" | expect "BH3O3 61.831 rounds=1"
FAIL S5 | SiO2 | got "O2Si 600830.000 rounds=0" | expect "O2Si 60.083 rounds=0"
FAIL S6 | Na2B4O7·10H2O | got "B4H20Na2O17 3813630.000 rounds=0" | expect "B4H20Na2O17 381.363 rounds=0"
FAIL S7 | C18H33KO2 | got "C18H33KO2 3205580.000 rounds=0" | expect "C18H33KO2 320.558 rounds=0"
FAIL S8 | 2 C2H5OH — the whole-input multiplier (repair 6) | got "C4H12O2 921380.000 rounds=0" | expect "C4H12O2 92.138 rounds=0"
FAIL P1 | H2O pin (Ch 4) | got "180150.000" | expect "18.015"
FAIL P2 | NaOH pin (Ch 14) | got "399970.000" | expect "39.997"
FAIL P3 | KOH pin (Ch 23) | got "561050.000" | expect "56.105"
FAIL P4 | NaOCl pin (Ch 16) | got "744420.000" | expect "74.442"
FAIL P5 | CH3COOH pin (Ch 4; first print Ch 2's review appendix) | got "600520.000" | expect "60.052"
FAIL P6 | glycerol C3H8O3 pin (Ch 21/23) | got "920940.000" | expect "92.094"
FAIL P7 | oleic acid C18H34O2 pin (Ch 23) | got "2824680.000" | expect "282.468"
FAIL P8 | sodium oleate C18H33NaO2 pin (Ch 23) — repair (1): fixed 3-dp display | got "3044500.000" | expect "304.450"
FAIL P9 | calcium stearate Ca(C18H35O2)2 pin (Ch 23) — repair (1)/(5) | got "6070300.000" | expect "607.030"
FAIL P10 | potassium oleate C18H33KO2 pin (Ch 23) | got "3205580.000" | expect "320.558"
FAIL P11 | potassium stearate C18H35KO2 pin (Ch 23) | got "3225740.000" | expect "322.574"
FAIL P12 | stearic acid C18H36O2 pin (Ch 23) | got "2844840.000" | expect "284.484"
FAIL P13 | sodium stearate C18H35NaO2 pin (Ch 23) | got "3064660.000" | expect "306.466"
FAIL P14 | Na2CO3 pin (Ch 14) | got "1059880.000" | expect "105.988"
FAIL P15 | Na2B4O7 pin (Ch 24) | got "2012130.000" | expect "201.213"
FAIL P16 | B(OH)4 pin (Ch 24) | got "788380.000" | expect "78.838"
FAIL P17 | NaCl pin (Ch 16/25) | got "584430.000" | expect "58.443"
FAIL N1 | NaBO2 — sodium metaborate, the chapter's NEW composition (grep-verified zero-hit on every page) | got "657980.000" | expect "65.798"
FAIL B1 | the soft-soap cook :: C18H34O2 + KOH -> C18H33KO2 + H2O | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "3.385.730 EXACT"
FAIL B2 | the stearate cook :: C18H36O2 + KOH -> C18H35KO2 + H2O | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "3.405.890 EXACT"
FAIL B3 | the borax seam :: 4 B(OH)3 + 2 NaOH -> Na2B4O7 + 7 H2O | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "3.273.180 EXACT"
FAIL B4 | the metaborate seam :: B(OH)3 + NaOH -> NaBO2 + 2 H2O | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "1.018.280 EXACT"
FAIL B5 | the decahydrate seam :: Na2B4O7 + 10 H2O -> Na2B4O7·10H2O | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "3.813.630 EXACT"
FAIL B6 | the hard-water scum :: 2 C18H35NaO2 + CaCl2 -> Ca(C18H35O2)2 + 2 NaCl (Ca admitted for this row) | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "7.239.160 EXACT"
FAIL E7 | the one-water-short must-fail :: B(OH)3 + NaOH -> NaBO2 + H2O | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "CAUGHT ATOMS O 4 vs 3, mass 1.018.280 vs 838.130 myu, gap 180.150 myu (18.015 g)"
FAIL H1 | boiling-water weeding: 1,000 g × 4.184 J/(g·K) × 80 K | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "334.720 kJ"
FAIL H2 | the 4.0 L kettle: 4 × 334,720 J | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "1338.880 kJ"
FAIL H3 | steam's latent row [recognition-only]: 1,000 g × 2,256 J/g | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "2256.000 kJ"
FAIL D1 | the 2% soap spray: 20 g/L sodium oleate as C18H33NaO2 — repair (2): hand expectation corrected | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "65.6922 mmol/L"
FAIL D2 | the 5% bait band priced at 5 g per L of bait as B(OH)3 — repair (3) | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "80.8656 mmol/L"
FAIL D3 | DE band coverage: the 250 g puffer at 50 m2 | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "5.000 g/m2"
FAIL D4 | vinegar 5% cut 1:1 with water | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "2.500%"
FAIL D5 | the 4.0 L kettle over a 2.0 m2 bed | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "2.000 L/m2"
FAIL W1 | dim(DE coverage): g/m2 | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "M^1·L^-2"
FAIL W2 | dim(heat): J | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "M^1·L^2·T^-2"
FAIL W3 | dim(specific energy): kJ/kg | got "ENGINE ERROR: Cannot read properties of undefined (reading 'trim')" | expect "L^2·T^-2"
RUN 1 SUMMARY: 10/54 PASS
```

The five harness slips, named: (1) G3's cross-check filter tested the census's derived-element lines as well as its cross-check lines; (2) the S/P/N mass display divided u4 by 10⁴ (printing myu) instead of 10⁸ (g/mol) — a display-layer slip, every underlying mass already exact; (3) compose() was invoked for B/E/H/D/W rows whose specs carry no formula, crashing on undefined; (4) E7's catch format — the frozen block prints the oxygen ledger per Engine 33's recorded master-atom design (the reviewer notes H also differs, 4 vs 2; the recorded format carries O only, by design) with euro-formatted masses; (5) the dose rows' decimal precision is per-row (D1/D2 at 4, D3/D4/D5 at 3), not uniform. Zero engine-core defects at run 1.

## Run-2 battery block (frozen — the review's record)

```
CENSUS H = 10080 myu (derived)
CENSUS O = 159990 myu (derived)
CENSUS Na = 229900 myu (derived)
CENSUS C = 120110 myu (derived)
CENSUS K = 390980 myu (derived)
CENSUS Cl = 354530 myu (derived)
CENSUS B = 108100 myu (derived)
CENSUS Si = 280850 myu (derived)
CENSUS Ca = 400780 myu (derived)
CENSUS X NaOCl 744420 == 744420 (P4) OK
CENSUS X B(OH)4 788380 == 788380 (P16) OK
CENSUS X Na2B4O7 2012130 == 2012130 (P15) OK
CENSUS X glycerol C3H8O3 920940 == 920940 (P6) OK
CENSUS X oleic C18H34O2 2824680 == 2824680 (P7) OK
CENSUS X stearic C18H36O2 2844840 == 2844840 (P12) OK
CENSUS X sodium oleate 3044500 == 3044500 (P8) OK
CENSUS X sodium stearate 3064660 == 3064660 (P13) OK
CENSUS X potassium oleate 3205580 == 3205580 (P10) OK
CENSUS X potassium stearate 3225740 == 3225740 (P11) OK
CENSUS X NaBO2 (N1) 657980 == 657980 (N1) OK
G1 PASS | frozen block: 54 rows, summary CLEAN | rows=54
G2 PASS | canvas frozen block == durable record run-3 block | record lines=55
G3 PASS | census: 9 elements derived, 11 cross-checks OK
PASS T1 | admission table checksum Σmyu (9 elements, transcribed twice) | got "2055.320" | expect "2055.320"
PASS T2 | positional checksum Σ(i+1)·myu, alphabetical order | got "10781.930" | expect "10781.930"
PASS S1 | H2O | got "H2O 18.015 rounds=0" | expect "H2O 18.015 rounds=0"
PASS S2 | NaOH | got "HNaO 39.997 rounds=0" | expect "HNaO 39.997 rounds=0"
PASS S3 | KOH | got "HKO 56.105 rounds=0" | expect "HKO 56.105 rounds=0"
PASS S4 | B(OH)3 | got "BH3O3 61.831 rounds=1" | expect "BH3O3 61.831 rounds=1"
PASS S5 | SiO2 | got "O2Si 60.083 rounds=0" | expect "O2Si 60.083 rounds=0"
PASS S6 | Na2B4O7·10H2O | got "B4H20Na2O17 381.363 rounds=0" | expect "B4H20Na2O17 381.363 rounds=0"
PASS S7 | C18H33KO2 | got "C18H33KO2 320.558 rounds=0" | expect "C18H33KO2 320.558 rounds=0"
PASS S8 | 2 C2H5OH — the whole-input multiplier (repair 6) | got "C4H12O2 92.138 rounds=0" | expect "C4H12O2 92.138 rounds=0"
PASS R1 | the P18 gate fires first: glyphosate | got "P18 REFUSES: 'glyphosate'" | expect "P18 REFUSES: 'glyphosate'"
PASS R2 | the P18 gate, second name: warfarin | got "P18 REFUSES: 'warfarin'" | expect "P18 REFUSES: 'warfarin'"
PASS R3 | PbO — Pb honestly out of scope | got "TABLE REFUSES Pb" | expect "TABLE REFUSES Pb"
PASS R4 | NaF — F honestly out of scope | got "TABLE REFUSES F" | expect "TABLE REFUSES F"
PASS R5 | Na0Cl — the zero subscript | got "ZERO SUBSCRIPT refused: 'Na0Cl'" | expect "ZERO SUBSCRIPT refused: 'Na0Cl'"
PASS R6 | '(NaOCl' — unclosed paren | got "UNCLOSED PAREN refused: '(NaOCl'" | expect "UNCLOSED PAREN refused: '(NaOCl'"
PASS R7 | Na0.5Cl — stray decimal mid-tape (the rule repair (4) narrowed) | got "SYNTAX (stray decimal) refused: 'Na0.5Cl'" | expect "SYNTAX (stray decimal) refused: 'Na0.5Cl'"
PASS R8 | CaCl2·0.35H2O — segment-leading rational hydrate (repair 4) | got "NON-EXACT refused: total mass 1172892.5000 myu" | expect "NON-EXACT refused: total mass 1172892.5000 myu"
PASS P1 | H2O pin (Ch 4) | got "18.015" | expect "18.015"
PASS P2 | NaOH pin (Ch 14) | got "39.997" | expect "39.997"
PASS P3 | KOH pin (Ch 23) | got "56.105" | expect "56.105"
PASS P4 | NaOCl pin (Ch 16) | got "74.442" | expect "74.442"
PASS P5 | CH3COOH pin (Ch 4; first print Ch 2's review appendix) | got "60.052" | expect "60.052"
PASS P6 | glycerol C3H8O3 pin (Ch 21/23) | got "92.094" | expect "92.094"
PASS P7 | oleic acid C18H34O2 pin (Ch 23) | got "282.468" | expect "282.468"
PASS P8 | sodium oleate C18H33NaO2 pin (Ch 23) — repair (1): fixed 3-dp display | got "304.450" | expect "304.450"
PASS P9 | calcium stearate Ca(C18H35O2)2 pin (Ch 23) — repair (1)/(5) | got "607.030" | expect "607.030"
PASS P10 | potassium oleate C18H33KO2 pin (Ch 23) | got "320.558" | expect "320.558"
PASS P11 | potassium stearate C18H35KO2 pin (Ch 23) | got "322.574" | expect "322.574"
PASS P12 | stearic acid C18H36O2 pin (Ch 23) | got "284.484" | expect "284.484"
PASS P13 | sodium stearate C18H35NaO2 pin (Ch 23) | got "306.466" | expect "306.466"
PASS P14 | Na2CO3 pin (Ch 14) | got "105.988" | expect "105.988"
PASS P15 | Na2B4O7 pin (Ch 24) | got "201.213" | expect "201.213"
PASS P16 | B(OH)4 pin (Ch 24) | got "78.838" | expect "78.838"
PASS P17 | NaCl pin (Ch 16/25) | got "58.443" | expect "58.443"
PASS N1 | NaBO2 — sodium metaborate, the chapter's NEW composition (grep-verified zero-hit on every page) | got "65.798" | expect "65.798"
PASS B1 | the soft-soap cook :: C18H34O2 + KOH -> C18H33KO2 + H2O | got "3.385.730 EXACT" | expect "3.385.730 EXACT"
PASS B2 | the stearate cook :: C18H36O2 + KOH -> C18H35KO2 + H2O | got "3.405.890 EXACT" | expect "3.405.890 EXACT"
PASS B3 | the borax seam :: 4 B(OH)3 + 2 NaOH -> Na2B4O7 + 7 H2O | got "3.273.180 EXACT" | expect "3.273.180 EXACT"
PASS B4 | the metaborate seam :: B(OH)3 + NaOH -> NaBO2 + 2 H2O | got "1.018.280 EXACT" | expect "1.018.280 EXACT"
PASS B5 | the decahydrate seam :: Na2B4O7 + 10 H2O -> Na2B4O7·10H2O | got "3.813.630 EXACT" | expect "3.813.630 EXACT"
PASS B6 | the hard-water scum :: 2 C18H35NaO2 + CaCl2 -> Ca(C18H35O2)2 + 2 NaCl (Ca admitted for this row) | got "7.239.160 EXACT" | expect "7.239.160 EXACT"
PASS E7 | the one-water-short must-fail :: B(OH)3 + NaOH -> NaBO2 + H2O | got "CAUGHT ATOMS O 4 vs 3, mass 1.018.280 vs 838.130 myu, gap 180.150 myu (18.015 g)" | expect "CAUGHT ATOMS O 4 vs 3, mass 1.018.280 vs 838.130 myu, gap 180.150 myu (18.015 g)"
PASS H1 | boiling-water weeding: 1,000 g × 4.184 J/(g·K) × 80 K | got "334.720 kJ" | expect "334.720 kJ"
PASS H2 | the 4.0 L kettle: 4 × 334,720 J | got "1338.880 kJ" | expect "1338.880 kJ"
PASS H3 | steam's latent row [recognition-only]: 1,000 g × 2,256 J/g | got "2256.000 kJ" | expect "2256.000 kJ"
PASS D1 | the 2% soap spray: 20 g/L sodium oleate as C18H33NaO2 — repair (2): hand expectation corrected | got "65.6922 mmol/L" | expect "65.6922 mmol/L"
PASS D2 | the 5% bait band priced at 5 g per L of bait as B(OH)3 — repair (3) | got "80.8656 mmol/L" | expect "80.8656 mmol/L"
PASS D3 | DE band coverage: the 250 g puffer at 50 m2 | got "5.000 g/m2" | expect "5.000 g/m2"
PASS D4 | vinegar 5% cut 1:1 with water | got "2.500%" | expect "2.500%"
PASS D5 | the 4.0 L kettle over a 2.0 m2 bed | got "2.000 L/m2" | expect "2.000 L/m2"
PASS W1 | dim(DE coverage): g/m2 | got "M^1·L^-2" | expect "M^1·L^-2"
PASS W2 | dim(heat): J | got "M^1·L^2·T^-2" | expect "M^1·L^2·T^-2"
PASS W3 | dim(specific energy): kJ/kg | got "L^2·T^-2" | expect "L^2·T^-2"
RUN 2 SUMMARY: 54/54 PASS — CLEAN
```

## Honest run history (runs 1–2)

Run 1: 10/54 — the census clean (nine elements derived from the chapter's own pins, eleven cross-checks OK), G1/G2 PASS, all ten refusal rows and both checksums PASS as built; forty-four fails, every one of them harness-side, the five slips named above (the G3 filter; the u4→g/mol display divisor; compose() on formula-less rows; E7's oxygen-ledger format; the dose rows' per-row precision). Zero engine-core defects at run 1. Run 2, the repair: **54/54 PASS — CLEAN**, with G1/G2/G3 PASS. The frozen run-2 block above is the review's record of part 1.

## Review findings raised at part 1 (for part-2 adjudication)

- **OBJ-1 (RA candidate, machine-check done, web check owed).** Lecture 3's availability note reads "sodium metaborate is the trade's product ... made industrially by drying borax." The alkali route closes on this chapter's own shelf: Na₂B₄O₇ + 2 NaOH → 4 NaBO₂ + H₂O — LHS 2,012,130 + 2×399,970 = 2,812,070 myu; RHS 4×657,980 + 180,150 = 2,812,070 myu — **2.812.070 EXACT** on the derived table (Engine 34's census arithmetic, checked by hand against the closure; drying borax decahydrate yields the lower hydrates/anhydride of borax, not the metaborate). Part 2 owes the web check of the industrial route and the adjudication: a Revision-Appendix correction-of-record if the drying claim stands wrong, a note if the literature supports a drying route.
- **OBJ-2 (grep owed).** The Ledger's first-print claim for B1's closure figure — "the KOH saponification closure 338.573 is unprinted anywhere before this page" — was asserted at authoring but NOT grep-verified (unlike N1). Part 2 owes the corpus sweep for "338.573" (local ch03–ch30 + the repo-only pages), the same pipeline as N1.
- **Integrity observation (bookkeeping, part 2 resolves).** The canvas at review reads 56,784 B (no trailing newline; platform byteLen and bash wc agree) while the repo master fc4.md is 56,786 B; the session-117 close recorded canvas 56,785 (trailing newline) + 1 = 56,786. The local canvas's trailing newline appears to have been trimmed after the close push; the repo master stands as the byte-verified artifact of record. Part 2's Revision-Appendix push re-establishes byte-verified equality and records the exact relation.
- **E7's hydrogen ledger (a note, not a correction).** The one-water-short must-fail differs in two elements (O 4 vs 3 AND H 4 vs 2); Engine 33's recorded design prints the oxygen ledger only (the book's master atom), and the frozen row carries O only — consistent, recorded here so the reviewer's observation is not lost.

## Part-2 owed list (session 118 part 2, on the user's call)

1. The anchor re-greps per the session-112 binding line — the 17 pins and their owners' pages (raw `grep -o` occurrence counts against the Chapter Ledger's recorded counts: H₂O 18.015 Ch 4 ×1; NaOH 39.997 Ch 14 ×5; KOH 56.105 Ch 23 ×8; NaOCl 74.442 Ch 16 ×3; CH₃COOH 60.052 Ch 4 ×5; glycerol 92.094 Ch 21 ×4 + Ch 23 ×7; oleic 282.468 Ch 23 ×3; sodium oleate 304.450 Ch 23 ×2; calcium stearate 607.030 Ch 23 ×3; potassium oleate 320.558 Ch 23 ×5; potassium stearate 322.574 Ch 23 ×2; stearic 284.484 Ch 23 ×6; sodium stearate 306.466 Ch 23 ×3; Na₂CO₃ 105.988 Ch 14 ×8; Na₂B₄O₇ 201.213 Ch 24 ×1; B(OH)₄ 78.838 Ch 24 ×1; NaCl 58.443 Ch 16 ×4 + Ch 25 ×2); the composition anchors (B(OH)₃ 61.831 Ch 24 ×1; SiO₂ 60.083 Ch 30 ×4; the decahydrate 381.363 Ch 24 ×6 + Ch 13 ×3 + Ch 4 ×1 + Ch 3 ×1); the two heat anchors (4.184 Ch 7 ×10; 2256 Ch 7 ×4). Every mismatch inspected line by line.
2. N1 re-proven NEW at the review HEAD — NaBO, "metaborate", 65.798, and the 65.79 prefix across the local ch03–ch30 masters, the local fc2/fc3 canvases (byte-identical to their repo masters), and the repo-only pages (ch01, ch02, ch31–ch36, fc1) via the saved-JSON pipeline; FC4's own page and this session's artifacts excluded as claim artifacts.
3. OBJ-2's grep: "338.573" across the same corpus (the B1 first-print claim).
4. The [convergent] web battery re-confirmed at named sources (UC IPM's pesticides-last; insecticidal soap's membrane mode; boric acid's stomach-poison mode + the 5%/5.4% bait band; DE's desiccation + wet-ineffectiveness; vinegar's contact-only limits; the boiling pour; EPA signal words + the label's first-aid statement) + OBJ-1's sodium-metaborate-route check.
5. Ex FC4.6's withheld ◆ answer, machine-verified — battery rows and canon labels only, no new figures — delivered in the Revision Appendix.
6. The Revision Appendix assembled and appended per extend-never-rewrite: the review description, Engine 34's honest two-run history, the frozen run-2 block spliced verbatim, the anchor table, the N1 re-proof + the 338.573 grep, the web checks, OBJ-1's adjudication, the Ex FC4.6 answer, the verdict line; the chapter's status line extended drafted → reviewed; the canvas and repo master pushed byte-verified (the trailing-byte relation recorded).
7. The map flip (FC4 drafted → reviewed); row 118 closed DONE; the Standing to-do session-118 bullet closed and the session-119 bullet added; PROJECT.md and KNOWLEDGE.md pushed ALWAYS-SYNC; scratch cleaned.
