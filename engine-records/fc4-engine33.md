# FC4 Engine 33 — the fixed-point rewrite engine (durable record, session 117 part 1)

## Design (the binding spec — rebuild from this alone)

Engine 33 is the FC4 "Pests and Weeds Without a Poison Shelf" authoring engine, built fresh and sharing zero code with Engines 1–32. Its architecture is the **fixed-point rewrite parser**: a lexical token tape (symbols, integers, parens, the hydrate dot handled at the segment split) reduced by **production rules applied to fixed point** — a rule fires at the leftmost position where its pattern matches, the tape is rewritten, and the loop repeats until no rule applies (fixed point) or an error state is reached. The three productions: **P1** `sym num -> atom` (subscript binding); **P2** bare `sym -> atom x 1`; **P3** an innermost all-atom paren group expands, scaled by its trailing multiplier (default 1). No recursion, no stack, no depth-map, no shunting-yard/RPN, no descent, no regex rewriting rounds, no bracket-depth coefficient maps (Engine 32's), no innermost-substitution (Engine 24's) — `rounds` is the maximum paren nesting depth reached. Rationals are `[n, d]` BigInt reduced by the **plain Euclidean gcd** (not Engine 32's continued-fraction reconstruction, not Stein's binary gcd).

**P18 name gate FIRST**: compose refuses to admit or price any name on the restricted list before any parsing — glyphosate, warfarin, paraquat, malathion, carbaryl, chlorpyrifos, metaldehyde, diquat, bromadiolone, 2,4-d (exact strings; the recognition-only fence as parser behavior; the chapter's prose tables carry no synthesis, no proportions, no pricing).

**Admission table, transcribed twice** (TABLE_A/TABLE_B asserted identical; checksum **2,055,320 myu**): 9 entries — B 108,100; C 120,110; Ca 400,780; Cl 354,530; H 10,080; K 390,980; Na 229,900; O 159,990; Si 280,850 (all in myu, 1 myu = 1e-4 g/mol). Pb, F, N (NH4Cl's), Mg etc. REFUSED at the table as gate rows. **Zero-sub** subscripts refused; **unclosed parens** refused with the input quoted; **stray decimals** refused mid-tape (`Na0.5Cl`), while **segment-leading decimals parse as rational hydrate coefficients** (`0.35H2O` — repair 4; the coefficient is applied before the tape is built, so the stray-decimal rule cannot fire at segment-leading position). **Mass integrality gate**: a composition whose total mass is non-integral in myu is refused NON-EXACT (`total mass 1172892.5000 myu`).

**Balances via Bareiss fraction-free elimination**: the species×element ledger matrix of the equation is ranked by exact integer elimination; a genuine single reaction must have **rank = species − 1** (one conservation subspace), otherwise RANK REFUSED. Sides are then compared atom-ledger to atom-ledger; equal ledgers print the raw myu total with `.` thousands separators (`3.385.730 EXACT`); a mismatch is CAUGHT with the oxygen ledger first (the book's master ledger atom), both masses, and the gap (`CAUGHT ATOMS O 4 vs 3, mass 1.018.280 vs 838.130 myu, gap 180.150 myu (18.015 g)`; the caught gap's g figure is gap/10,000).

**Displays**: g/mol at the book's **fixed 3 decimals** (304.450, never 304.45 — repairs 1/5); dose figures at 4 decimals (65.6922 mmol/L); heat in kJ at 3 decimals; every display a half-up rounding of an exact rational at the stated precision (session-104 convention). **Dimension lattice {M, L, T, Θ}** (the design checkpoint said {M,L,T}; the build corrected it — Θ needed for the heat rows' J/(g·K) class).

**Design corrections vs the checkpoint (recorded honestly, per the checkpoint's own note)**: (a) **Ca was admitted** — the checkpoint's table said {C,H,O,B,Si,Na,K,Cl}, but the hard-water scum equation (battery row B6: `2 C18H35NaO2 + CaCl2 -> Ca(C18H35O2)2 + 2 NaCl`, closing at 7.239.160 myu = 723.916 g) needs Ca; (b) dimensions corrected to {M,L,T,Θ}.

## Honest provenance (the compaction rebuild)

The original Engine 33 run-1 source and its verbatim battery output were **lost to a platform context compaction** at the session boundary (the two surviving tool-result dumps were census greps, not the engine run). Engine 33 was therefore **rebuilt from the durable design checkpoint** (fc4-design-notes.md §2–3) with the five preserved run-1 repairs applied, and the rebuild itself caught one further harness defect at its own run 2 (the whole-input multiplier parsed but never applied). The run-1 fail lines below are **transcribed from the preserved session diagnoses**, not verbatim; runs 2 and 3 are the rebuilt engine and their blocks are verbatim.

## Census summary (executed before any freeze; session-100 line)

- **N1 = sodium metaborate NaBO2 = 65.798 g/mol — NEW, grep-verified zero-hit on every page of the book**: "NaBO" (all forms) 0, "metaborate" 0, "65.798"/"65.79x" 0 — across local ch03–ch30 manuscripts + engine records + KNOWLEDGE.md + PROJECT.md; repo-only pages ch01, ch02, ch31–ch36 (fetched in full, grepped from the saved JSON); fc1–fc3 canvases. GitHub code search is not a valid instrument for this repo (unindexed markdown; returns 0 for the known-present "381.363"); direct fetch+grep is the only instrument.
- **Basis correction**: the book holds **B = 10.81** (not 10.811; held from Ch 3, admitted into Ch 24's table, confirmed by Ch 13's RA-6). Corrected hand values: B(OH)3 **61.831** (618,310 myu; NOT 61.832 — ALREADY OWNED, Ch 24's battery line 182 prints "B(OH)3 61.831"); NaBO2 **65.798** (657,980 myu; NOT 65.799); borax decahydrate **381.363** (NOT 381.367; owned Ch 2 RA-7 / Ch 3 / Ch 4 / Ch 13 / Ch 24).
- **"338.573"** (the KOH saponification closure, B1) unprinted anywhere = new arithmetic on owned species. **"diatomaceous"/"diatomite"** zero-hit = the NAME diatomaceous earth is a first print (recognition-only; DE is amorphous SiO2, mass owned by Ch 30).
- **Pins owner-verified on their own pages**: oleic 282.468, stearic 284.484, sodium oleate 304.450, sodium stearate 306.466, calcium stearate 607.030, potassium oleate 320.558, potassium stearate 322.574, KOH 56.105 [all Ch 23]; B(OH)4- 78.838, Na2B4O7 201.213 [Ch 24]; SiO2 60.083 [Ch 30]; CH3COOH 60.052 [Ch 4; first print Ch 2's review appendix]; NaOCl 74.442 [Ch 16]; NaCl 58.443 [Ch 16/25]; glycerol 92.094 [Ch 21/23]; NaOH 39.997 [Ch 14]; Na2CO3 105.988 [Ch 14]; H2O 18.015 [Ch 4]. FC4 admits zero new elements (Ca was already held-22).

## Engine source (verbatim — the executed Engine 33, run-3 form)

```
async function main() {
  // ===================== Engine 33: the fixed-point rewrite engine =====================
  // Fresh build for FC4 (session 117 part 1). Zero code shared with Engines 1-32: the parser is a
  // token tape reduced by production rules to FIXED POINT (no depth-map fold, no shunting-yard/RPN,
  // no regex rewriting rounds, no recursive descent, no frame stacks); rationals use the plain
  // Euclidean gcd (not Engine 32's continued-fraction reconstruction); balances are ranked by
  // Bareiss fraction-free elimination (rank must equal species-1). P18 restricted-name gate fires
  // first. Mass integrality gate in myu (1 myu = 1e-4 g/mol). Dimension lattice {M,L,T,Theta}.
  //
  // RUN HISTORY (honest):
  //   run 1 (pre-compaction original, verbatim lost to platform compaction): 49/54 — five fails,
  //     all harness/display-layer, diagnoses preserved: P8 "304.45"/P9 "607.03" (integral-search
  //     display stopped at dp=2 instead of the book's fixed 3 dp), D1 hand expectation 65.6915
  //     wrong (engine right at 65.6922), D2 hand expectation 80.8700 wrong (engine right at
  //     80.8656), R8 segment-leading 0.35 fired the stray-decimal rule instead of NON-EXACT.
  //   run 2 (rebuilt with repairs 1-5): 53/54 — S8 FAIL: the whole-input multiplier was parsed
  //     but never applied to the mass/count accumulation (got "C2H6O 46.069" for "2 C2H5OH").
  //   run 3 (this run): repair (6) — whole is applied in total and per-element accumulation.

  const TABLE_A: Record<string, bigint> = { B: 108100n, C: 120110n, Ca: 400780n, Cl: 354530n, H: 10080n, K: 390980n, Na: 229900n, O: 159990n, Si: 280850n };
  const TABLE_B: Record<string, bigint> = { B: 108100n, C: 120110n, Ca: 400780n, Cl: 354530n, H: 10080n, K: 390980n, Na: 229900n, O: 159990n, Si: 280850n };
  let tableTwice = true;
  for (const k of Object.keys(TABLE_A)) if (TABLE_A[k] !== TABLE_B[k]) tableTwice = false;
  const TABLE = TABLE_A;
  const ORDER = Object.keys(TABLE).sort(); // B, C, Ca, Cl, H, K, Na, O, Si
  let SUM = 0n;
  for (const k of ORDER) SUM += TABLE[k];
  const checksumOk = SUM === 2055320n;

  const NAME_GATE = ["glyphosate", "warfarin", "paraquat", "malathion", "carbaryl", "chlorpyrifos", "metaldehyde", "diquat", "bromadiolone", "2,4-d"];

  type Rat = [bigint, bigint];
  function gcd(a: bigint, b: bigint): bigint { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) { const t = a % b; a = b; b = t; } return a; }
  function rReduce(n: bigint, d: bigint): Rat { if (d < 0n) { n = -n; d = -d; } const g = gcd(n, d) || 1n; return [n / g, d / g]; }
  const rAdd = (x: Rat, y: Rat): Rat => rReduce(x[0] * y[1] + y[0] * x[1], x[1] * y[1]);
  const rMul = (x: Rat, y: Rat): Rat => rReduce(x[0] * y[0], x[1] * y[1]);
  const rSub = (x: Rat, y: Rat): Rat => rReduce(x[0] * y[1] - y[0] * x[1], x[1] * y[1]);
  function halfUp(n: bigint, d: bigint, dp: number): string {
    const neg = (n < 0n) !== (d < 0n);
    let a = n < 0n ? -n : n; const b = d < 0n ? -d : d;
    a = a * 10n ** BigInt(dp);
    const q = a / b, r = a % b;
    const qq = 2n * r >= b ? q + 1n : q;
    const s = qq.toString().padStart(dp + 1, "0");
    const body = dp === 0 ? s : s.slice(0, s.length - dp) + "." + s.slice(s.length - dp);
    return (neg && qq !== 0n ? "-" : "") + body;
  }
  function thou(n: bigint): string { const s = n.toString(); let out = ""; for (let i = 0; i < s.length; i++) { if (i > 0 && (s.length - i) % 3 === 0) out += "."; out += s[i]; } return out; }

  type Tok =
    | { t: "sym"; v: string }
    | { t: "num"; v: string }
    | { t: "op"; v: "(" | ")" }
    | { t: "atom"; sym: string; n: bigint };
  function lex(src: string): Tok[] | string {
    const toks: Tok[] = []; let i = 0;
    while (i < src.length) {
      const ch = src[i];
      if (ch >= "A" && ch <= "Z") {
        let sym = ch; i++;
        if (i < src.length && src[i] >= "a" && src[i] <= "z") { sym += src[i]; i++; }
        if (!(sym in TABLE)) return `TABLE REFUSES ${sym}`;
        toks.push({ t: "sym", v: sym }); continue;
      }
      if (ch >= "0" && ch <= "9") { let v = ""; while (i < src.length && src[i] >= "0" && src[i] <= "9") { v += src[i]; i++; } toks.push({ t: "num", v }); continue; }
      if (ch === "(" || ch === ")") { toks.push({ t: "op", v: ch }); i++; continue; }
      if (ch === ".") return `SYNTAX (stray decimal) refused: '${src}'`;
      return `BAD CHAR '${ch}' refused at position ${i}`;
    }
    return toks;
  }
  type Parsed = { counts: Record<string, bigint>; rounds: number };
  function rewrite(toks: Tok[], src: string): Parsed | string {
    let depth = 0, rounds = 0;
    for (const t of toks) { if (t.t === "op") { if (t.v === "(") { depth++; if (depth > rounds) rounds = depth; } else depth--; if (depth < 0) return `UNCLOSED PAREN refused: '${src}'`; } }
    if (depth !== 0) return `UNCLOSED PAREN refused: '${src}'`;
    const tape = toks.slice();
    for (;;) {
      let fired = false;
      for (let i = 0; i < tape.length; i++) {
        const t = tape[i];
        if (t.t === "sym") {
          const nxt = tape[i + 1];
          if (nxt && nxt.t === "num") tape.splice(i, 2, { t: "atom", sym: t.v, n: BigInt(nxt.v) }); // P1: sym num -> atom
          else tape.splice(i, 1, { t: "atom", sym: t.v, n: 1n });                                    // P2: bare sym -> atom x1
          fired = true; break;
        }
        if (t.t === "op" && t.v === "(") {                                                            // P3: innermost all-atom group expands
          let j = i + 1, allAtoms = true;
          while (j < tape.length && tape[j].t !== "op") { if (tape[j].t !== "atom") allAtoms = false; j++; }
          if (j < tape.length && (tape[j] as any).v === ")" && allAtoms) {
            let k = 1n, drop = 0;
            const after = tape[j + 1];
            if (after && after.t === "num") { k = BigInt(after.v); drop = 1; }
            const inner: Tok[] = tape.slice(i + 1, j).map((a) => ({ t: "atom", sym: (a as any).sym, n: (a as any).n * k }));
            tape.splice(i, j - i + 1 + drop, ...inner);
            fired = true; break;
          }
        }
      }
      if (!fired) break;
    }
    const counts: Record<string, bigint> = {};
    for (const t of tape) {
      if (t.t !== "atom") return `SYNTAX (unreduced tape) refused: '${src}'`;
      if (t.n === 0n) return `ZERO SUBSCRIPT refused: '${src}'`;
      counts[t.sym] = (counts[t.sym] ?? 0n) + t.n;
    }
    return { counts, rounds };
  }
  type Comp = { ok: true; counts: Record<string, Rat>; total: Rat; rounds: number } | { ok: false; msg: string };
  function compose(input: string): Comp {
    const t = input.trim();
    if (NAME_GATE.includes(t)) return { ok: false, msg: `P18 REFUSES: '${t}'` };
    if (t === "") return { ok: false, msg: "EMPTY refused" };
    let whole: Rat = [1n, 1n], body = t;
    const wm = body.match(/^([0-9]+) +(.+)$/);
    if (wm) { whole = [BigInt(wm[1]), 1n]; body = wm[2].trim(); }
    const merged: Record<string, Rat> = {};
    let total: Rat = [0n, 1n], rounds = 0;
    for (const seg of body.split("·")) {
      let coef: Rat = [1n, 1n], rest = seg;
      const cm = rest.match(/^(0|[1-9][0-9]*)(?:\.([0-9]+))?/); // repair (4): segment-leading decimals are rationals
      if (cm && cm[0].length > 0) {
        const frac = cm[2] ?? "";
        const den = 10n ** BigInt(frac.length);
        coef = [BigInt(cm[1]) * den + (frac ? BigInt(frac) : 0n), den];
        rest = rest.slice(cm[0].length);
      }
      if (rest === "") return { ok: false, msg: `EMPTY SEGMENT refused: '${t}'` };
      const toks = lex(rest);
      if (typeof toks === "string") return { ok: false, msg: toks };
      const pw = rewrite(toks, t);
      if (typeof pw === "string") return { ok: false, msg: pw };
      let mass: Rat = [0n, 1n];
      for (const s in pw.counts) mass = rAdd(mass, rMul([pw.counts[s], 1n], [TABLE[s], 1n]));
      total = rAdd(total, rMul(rMul(coef, mass), whole)); // repair (6): whole applied
      rounds = Math.max(rounds, pw.rounds);
      for (const s in pw.counts) merged[s] = rAdd(merged[s] ?? [0n, 1n], rMul(rMul([pw.counts[s], 1n], coef), whole));
    }
    if (total[1] !== 1n) return { ok: false, msg: `NON-EXACT refused: total mass ${halfUp(total[0], total[1], 4)} myu` };
    return { ok: true, counts: merged, total, rounds };
  }
  function canonical(counts: Record<string, Rat>): string {
    let out = "";
    for (const s of Object.keys(counts).filter(k => counts[k][0] !== 0n).sort()) {
      const [n, d] = counts[s];
      out += s + (d === 1n ? (n === 1n ? "" : n.toString()) : halfUp(n, d, 3));
    }
    return out;
  }
  function bareissRank(rowsIn: bigint[][]): number {
    const rows = rowsIn.map(r => r.slice());
    const n = rows.length, m = rows[0].length;
    let rank = 0, r = 0, prev = 1n;
    for (let c = 0; c < m && r < n; c++) {
      let piv = -1;
      for (let i = r; i < n; i++) if (rows[i][c] !== 0n) { piv = i; break; }
      if (piv === -1) continue;
      const tmp = rows[r]; rows[r] = rows[piv]; rows[piv] = tmp;
      for (let i = r + 1; i < n; i++) {
        for (let j = c + 1; j < m; j++) rows[i][j] = (rows[r][c] * rows[i][j] - rows[i][c] * rows[r][j]) / prev;
        rows[i][c] = 0n;
      }
      prev = rows[r][c]; r++; rank++;
    }
    return rank;
  }
  type Side = { counts: Record<string, Rat>; total: Rat; species: string[] } | string;
  function sideParse(side: string): Side {
    const counts: Record<string, Rat> = {};
    let total: Rat = [0n, 1n];
    const species: string[] = [];
    for (const term of side.split(" + ")) {
      const m = term.match(/^([0-9]+) +(.+)$/);
      let c: Rat = [1n, 1n], f = term.trim();
      if (m) { c = [BigInt(m[1]), 1n]; f = m[2].trim(); }
      const cp = compose(f);
      if (!cp.ok) return (cp as any).msg;
      total = rAdd(total, rMul(c, cp.total));
      if (!species.includes(f)) species.push(f);
      for (const s in cp.counts) counts[s] = rAdd(counts[s] ?? [0n, 1n], rMul(cp.counts[s], c));
    }
    return { counts, total, species };
  }
  function balance(input: string): string {
    const [lhs, rhs] = input.split(" -> ").map(s => s.trim());
    const L = sideParse(lhs), R = sideParse(rhs);
    if (typeof L === "string") return L as string;
    if (typeof R === "string") return R as string;
    const Ls = L as { counts: Record<string, Rat>; total: Rat; species: string[] };
    const Rs = R as { counts: Record<string, Rat>; total: Rat; species: string[] };
    const uniq = [...new Set([...Ls.species, ...Rs.species])];
    const elems = [...new Set(uniq.flatMap(f => Object.keys(compose(f)!.counts)))].sort();
    const mat = uniq.map(f => elems.map(e => { const c = compose(f)!.counts[e]; return c ? c[0] / c[1] : 0n; }));
    const rank = bareissRank(mat);
    if (rank !== uniq.length - 1) return `RANK REFUSED: rank ${rank} != ${uniq.length - 1} (species-1)`;
    let equal = true;
    for (const e of elems) {
      const l = Ls.counts[e] ?? [0n, 1n], r = Rs.counts[e] ?? [0n, 1n];
      if (rSub(l, r)[0] !== 0n) { equal = false; break; }
    }
    if (equal) return `${thou(Ls.total[0])} EXACT`;
    let atom = "O"; // the book's master ledger atom when oxygen mismatches
    const oL = Ls.counts["O"] ?? [0n, 1n], oR = Rs.counts["O"] ?? [0n, 1n];
    if (rSub(oL, oR)[0] === 0n) atom = elems.find(e => rSub(Ls.counts[e] ?? [0n, 1n], Rs.counts[e] ?? [0n, 1n])[0] !== 0n)!;
    const lo = (Ls.counts[atom] ?? [0n, 1n])[0] / (Ls.counts[atom] ?? [0n, 1n])[1];
    const ro = (Rs.counts[atom] ?? [0n, 1n])[0] / (Rs.counts[atom] ?? [0n, 1n])[1];
    const gap = rSub(Ls.total, Rs.total);
    const g = gap[0] < 0n ? -gap[0] : gap[0];
    return `CAUGHT ATOMS ${atom} ${lo} vs ${ro}, mass ${thou(Ls.total[0])} vs ${thou(Rs.total[0])} myu, gap ${thou(g)} myu (${halfUp(g, 10000n, 3)} g)`;
  }
  function dim(parts: [string, number][]): string {
    const e: Record<string, number> = { M: 0, L: 0, T: 0, "Θ": 0 };
    for (const [b, p] of parts) e[b] += p;
    return ["M", "L", "T", "Θ"].filter(k => e[k] !== 0).map(k => `${k}^${e[k]}`).join("·");
  }
  const gmol3 = (myu: bigint) => halfUp(myu, 10000n, 3); // repair (1)/(5): fixed 3-dp display
  const pin = (f: string) => gmol3((compose(f) as any).total[0]);
  const sForm = (f: string) => { const c = compose(f)!; return `${canonical(c.counts)} ${gmol3(c.total[0])} rounds=${c.rounds}`; };
  const kJ = (mj: bigint) => halfUp(mj, 1000000n, 3) + " kJ";

  // ---------------- the battery: 54 rows ----------------
  const B: [string, string, () => string, string][] = [
    ["T1", "admission table checksum Σmyu (9 elements, transcribed twice)", () => halfUp(SUM, 1000n, 3), "2055.320"],
    ["T2", "positional checksum Σ(i+1)·myu, alphabetical order", () => halfUp(ORDER.reduce((a, s, i) => a + BigInt(i + 1) * TABLE[s], 0n), 1000n, 3), "10781.930"],
    ["S1", "H2O", () => sForm("H2O"), "H2O 18.015 rounds=0"],
    ["S2", "NaOH", () => sForm("NaOH"), "HNaO 39.997 rounds=0"],
    ["S3", "KOH", () => sForm("KOH"), "HKO 56.105 rounds=0"],
    ["S4", "B(OH)3", () => sForm("B(OH)3"), "BH3O3 61.831 rounds=1"],
    ["S5", "SiO2", () => sForm("SiO2"), "O2Si 60.083 rounds=0"],
    ["S6", "Na2B4O7·10H2O", () => sForm("Na2B4O7·10H2O"), "B4H20Na2O17 381.363 rounds=0"],
    ["S7", "C18H33KO2", () => sForm("C18H33KO2"), "C18H33KO2 320.558 rounds=0"],
    ["S8", "2 C2H5OH — the whole-input multiplier (repair 6)", () => sForm("2 C2H5OH"), "C4H12O2 92.138 rounds=0"],
    ["R1", "the P18 gate fires first: glyphosate", () => (compose("glyphosate") as any).msg, "P18 REFUSES: 'glyphosate'"],
    ["R2", "the P18 gate, second name: warfarin", () => (compose("warfarin") as any).msg, "P18 REFUSES: 'warfarin'"],
    ["R3", "PbO — Pb honestly out of scope", () => (compose("PbO") as any).msg, "TABLE REFUSES Pb"],
    ["R4", "NaF — F honestly out of scope", () => (compose("NaF") as any).msg, "TABLE REFUSES F"],
    ["R5", "Na0Cl — the zero subscript", () => (compose("Na0Cl") as any).msg, "ZERO SUBSCRIPT refused: 'Na0Cl'"],
    ["R6", "'(NaOCl' — unclosed paren", () => (compose("(NaOCl") as any).msg, "UNCLOSED PAREN refused: '(NaOCl'"],
    ["R7", "Na0.5Cl — stray decimal mid-tape (the rule repair (4) narrowed)", () => (compose("Na0.5Cl") as any).msg, "SYNTAX (stray decimal) refused: 'Na0.5Cl'"],
    ["R8", "CaCl2·0.35H2O — segment-leading rational hydrate (repair 4)", () => (compose("CaCl2·0.35H2O") as any).msg, "NON-EXACT refused: total mass 1172892.5000 myu"],
    ["P1", "H2O pin (Ch 4)", () => pin("H2O"), "18.015"],
    ["P2", "NaOH pin (Ch 14)", () => pin("NaOH"), "39.997"],
    ["P3", "KOH pin (Ch 23)", () => pin("KOH"), "56.105"],
    ["P4", "NaOCl pin (Ch 16)", () => pin("NaOCl"), "74.442"],
    ["P5", "CH3COOH pin (Ch 4; first print Ch 2's review appendix)", () => pin("CH3COOH"), "60.052"],
    ["P6", "glycerol C3H8O3 pin (Ch 21/23)", () => pin("C3H8O3"), "92.094"],
    ["P7", "oleic acid C18H34O2 pin (Ch 23)", () => pin("C18H34O2"), "282.468"],
    ["P8", "sodium oleate C18H33NaO2 pin (Ch 23) — repair (1): fixed 3-dp display", () => pin("C18H33NaO2"), "304.450"],
    ["P9", "calcium stearate Ca(C18H35O2)2 pin (Ch 23) — repair (1)/(5)", () => pin("Ca(C18H35O2)2"), "607.030"],
    ["P10", "potassium oleate C18H33KO2 pin (Ch 23)", () => pin("C18H33KO2"), "320.558"],
    ["P11", "potassium stearate C18H35KO2 pin (Ch 23)", () => pin("C18H35KO2"), "322.574"],
    ["P12", "stearic acid C18H36O2 pin (Ch 23)", () => pin("C18H36O2"), "284.484"],
    ["P13", "sodium stearate C18H35NaO2 pin (Ch 23)", () => pin("C18H35NaO2"), "306.466"],
    ["P14", "Na2CO3 pin (Ch 14)", () => pin("Na2CO3"), "105.988"],
    ["P15", "Na2B4O7 pin (Ch 24)", () => pin("Na2B4O7"), "201.213"],
    ["P16", "B(OH)4 pin (Ch 24)", () => pin("B(OH)4"), "78.838"],
    ["P17", "NaCl pin (Ch 16/25)", () => pin("NaCl"), "58.443"],
    ["N1", "NaBO2 — sodium metaborate, the chapter's NEW composition (grep-verified zero-hit on every page)", () => pin("NaBO2"), "65.798"],
    ["B1", "the soft-soap cook :: C18H34O2 + KOH -> C18H33KO2 + H2O", () => balance("C18H34O2 + KOH -> C18H33KO2 + H2O"), "3.385.730 EXACT"],
    ["B2", "the stearate cook :: C18H36O2 + KOH -> C18H35KO2 + H2O", () => balance("C18H36O2 + KOH -> C18H35KO2 + H2O"), "3.405.890 EXACT"],
    ["B3", "the borax seam :: 4 B(OH)3 + 2 NaOH -> Na2B4O7 + 7 H2O", () => balance("4 B(OH)3 + 2 NaOH -> Na2B4O7 + 7 H2O"), "3.273.180 EXACT"],
    ["B4", "the metaborate seam :: B(OH)3 + NaOH -> NaBO2 + 2 H2O", () => balance("B(OH)3 + NaOH -> NaBO2 + 2 H2O"), "1.018.280 EXACT"],
    ["B5", "the decahydrate seam :: Na2B4O7 + 10 H2O -> Na2B4O7·10H2O", () => balance("Na2B4O7 + 10 H2O -> Na2B4O7·10H2O"), "3.813.630 EXACT"],
    ["B6", "the hard-water scum :: 2 C18H35NaO2 + CaCl2 -> Ca(C18H35O2)2 + 2 NaCl (Ca admitted for this row)", () => balance("2 C18H35NaO2 + CaCl2 -> Ca(C18H35O2)2 + 2 NaCl"), "7.239.160 EXACT"],
    ["E7", "the one-water-short must-fail :: B(OH)3 + NaOH -> NaBO2 + H2O", () => balance("B(OH)3 + NaOH -> NaBO2 + H2O"), "CAUGHT ATOMS O 4 vs 3, mass 1.018.280 vs 838.130 myu, gap 180.150 myu (18.015 g)"],
    ["H1", "boiling-water weeding: 1,000 g × 4.184 J/(g·K) × 80 K", () => kJ(1000n * 4184n * 80n), "334.720 kJ"],
    ["H2", "the 4.0 L kettle: 4 × 334,720 J", () => kJ(4n * 1000n * 4184n * 80n), "1338.880 kJ"],
    ["H3", "steam's latent row [recognition-only]: 1,000 g × 2,256 J/g", () => kJ(1000n * 2256000n), "2256.000 kJ"],
    ["D1", "the 2% soap spray: 20 g/L sodium oleate as C18H33NaO2 — repair (2): hand expectation corrected", () => halfUp(400000n, 6089n, 4) + " mmol/L", "65.6922 mmol/L"],
    ["D2", "the 5% bait band priced at 5 g per L of bait as B(OH)3 — repair (3)", () => halfUp(5000000n, 61831n, 4) + " mmol/L", "80.8656 mmol/L"],
    ["D3", "DE band coverage: the 250 g puffer at 50 m2", () => halfUp(250n, 50n, 3) + " g/m2", "5.000 g/m2"],
    ["D4", "vinegar 5% cut 1:1 with water", () => halfUp(5n, 2n, 3) + "%", "2.500%"],
    ["D5", "the 4.0 L kettle over a 2.0 m2 bed", () => halfUp(4n, 2n, 3) + " L/m2", "2.000 L/m2"],
    ["W1", "dim(DE coverage): g/m2", () => dim([["M", 1], ["L", -2]]), "M^1·L^-2"],
    ["W2", "dim(heat): J", () => dim([["M", 1], ["L", 2], ["T", -2]]), "M^1·L^2·T^-2"],
    ["W3", "dim(specific energy): kJ/kg", () => dim([["M", 1], ["L", 2], ["T", -2], ["M", -1]]), "L^2·T^-2"],
  ];
  const rows: string[] = [];
  let pass = 0;
  for (const [id, desc, fn, expect] of B) {
    let got = "THROW", ok = false;
    try { got = fn(); ok = true; } catch (e) { got = "THROW: " + String(e).slice(0, 80); }
    const verdict = ok && got === expect ? "PASS" : "FAIL";
    if (verdict === "PASS") pass++;
    rows.push(`${verdict} ${id} | ${desc} | got "${got}" | expect "${expect}"`);
  }
  const summary = `RUN 3 SUMMARY: ${pass}/54 PASS${pass === 54 ? " — CLEAN" : ""}`;
  return { rows: [...rows, summary], summary, checks: { tableTwice, checksumOk, rowCount: B.length } };
}
```

## Run-1 FAIL block (transcribed — see the provenance note; the verbatim output was lost to the platform context compaction at the session boundary; fail classes, got values and diagnoses as preserved in the session log)

```
FAIL P8 | sodium oleate pin | got "304.45" | expect "304.450"
FAIL P9 | calcium stearate pin | got "607.03" | expect "607.030"
FAIL D1 | the 2% soap spray | got "65.6922 mmol/L" | expect "65.6915 mmol/L"
FAIL D2 | the 5% bait band | got "80.8656 mmol/L" | expect "80.8700 mmol/L"
FAIL R8 | CaCl2·0.35H2O | got "SYNTAX (stray decimal)" | expect "NON-EXACT refused: total mass 1172892.5000 myu"
RUN 1 SUMMARY: 49/54 PASS
```

Diagnoses: P8/P9 — the display layer's expanding-scale integral search stopped at the smallest integral decimal scale (dp=2) instead of printing the book's fixed 3 decimals; the composition values were correct. D1/D2 — the HARNESS expectations were wrong hand values (20/304.450 × 1000 = 65.6922 at 4 dp; 5/61.831 × 1000 = 80.8656 at 4 dp); the engine was right. R8 — the stray-decimal rule fired at segment-leading position before the rational hydrate-coefficient path; the correct refusal is NON-EXACT (0.35 × 180,150 = 63,052.5 myu non-integral; total 1,172,892.5 myu).

## Run-2 FAIL block (verbatim — the single harness slip of the rebuild)

```
FAIL S8 | 2 C2H5OH — the whole-input multiplier | got "C2H6O 46.069 rounds=0" | expect "C4H12O2 92.138 rounds=0"
RUN 2 SUMMARY: 53/54 PASS
```

Diagnosis: the whole-input multiplier was parsed into `whole` but never applied to the mass and per-element accumulation — a harness-side wiring slip in the rebuilt compose; the parse itself was correct. Repair (6): `whole` multiplies both the segment mass and the merged counts.

## Run-3 battery block (frozen — the record block for the chapter's Lab FC4.1)

```
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
RUN 3 SUMMARY: 54/54 PASS — CLEAN
```

## Honest run history (runs 1–3)

Run 1 (the pre-compaction original) scored **49/54**: five fails, every one harness/display-layer — the two pin-display rows printed the smallest integral decimal scale instead of the book's fixed 3 decimals (P8 "304.45", P9 "607.03"); two hand-derived dose expectations were wrong at the fourth decimal (D1 65.6915 vs the true 20/304.450 × 1000 = 65.6922; D2 80.8700 vs the true 5/61.831 × 1000 = 80.8656) — the engine was right both times; and the stray-decimal rule fired on the segment-leading 0.35 of `CaCl2·0.35H2O` instead of the NON-EXACT integrality refusal. Zero engine-core defects at run 1: all composition, name-gate, table, zero-sub, balance, rank, pin, N1, heat, and dimension rows passed. **The run-1 verbatim output was lost to the platform context compaction at the session boundary; the transcribed block above is labeled as such** (the two surviving tool-result dumps were census greps, verified by grep before declaring the loss). The engine was rebuilt from the durable design checkpoint (fc4-design-notes.md) with the five repairs applied. Run 2 (the rebuild) scored **53/54**: the rebuilt battery's own S8 row caught the whole-input multiplier parsed but never applied to the mass/count accumulation — a fresh harness-side wiring slip, diagnosed and repaired (repair 6). Run 3, the repair: **54/54 PASS — CLEAN** — the frozen block above.

## Part-2 owed list (session 117 part 2, on the user's call)

- Chapter prose per the 6-lecture skeleton in fc4-design-notes.md §4 (L0 ant-trail pencil case; L1 the IPM ladder; L2 soap sprays; L3 boron baits + DE; L4 the weed toolbox; L5 the poison shelf you don't own — P18 recognition-only tables, first aid, the fence absolute). Labs FC4.1 (Engine 33 + the honest run history + the frozen run-3 block) / FC4.2 (dose ledgers). Exercises FC4.1–4.7. Safety 8 rows. Canon coverage. Forward flags (FC5, Ch 28, Ch 33, FC3 back). Chapter Ledger.
- Load the canvas skill; canvas everyday-chem-atlas-fc4; push manuscript/field-companion/fc4.md byte-verified against the canvas text.
- [convergent] web battery, every datum verified in-session before the page freezes: UC IPM ladder order; soap-spray mode of action on soft-bodied insects (membrane disruption); boric acid stomach-poison mode + the 5%-class bait band; DE desiccation mode, wet-ineffective; vinegar 5% contact-only, no root kill; boiling-water weeding; EPA signal words / first aid (Caution/Warning/Danger).
- Pin re-greps in the owners' own pages (session-112 binding line) for every pin row P1–P17 + the heat anchors 4.184 (Ch 7) and 2,256 J/g (Ch 7); N1 re-proved NEW at the review HEAD (fc4 itself excluded as the claiming chapter).
- Records close: map line 132 planned -> drafted; row 117 close + status flip IN PROGRESS -> DONE; KNOWLEDGE.md line 10 session-117 closed entry; standing bullet at line 279 flipped to [x] EXECUTED AND CLOSED + a session-118 bullet added (FC5 or FC4 review on the user's call); separate push runs for PROJECT.md and KNOWLEDGE.md, each byte-verified; scratch cleanup; terse final summary.
- Standing debts NOT this session: FC1/FC2/FC3 web editions.
