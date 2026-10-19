# Engine 36 — the token-table AST-fold engine (FC5 Phase-3 adversarial review, session 120 part 1, 2026-10-19)

Provenance: fresh build for FC5's review session (120), zero code shared with Engines 1–35. The review's contract fixed before any engine code ran (PROJECT row 120's open note): Engine 36 re-verifies, it does not re-author — expectations are the chapter's frozen run-5 corrected strings verbatim (§8 of fc5-engine35-record.md), and any mismatch would be a finding raised for part-2 adjudication, never silently patched. Binding lines in force: session-100 (N1's re-proof owed at part 2 at the review HEAD), session-102 (every worked figure a battery row), session-104 (convergence at displayed precision), session-112 (the pin re-greps owed at part 2), extend-never-rewrite, ALWAYS-SYNC.

## 1. Design spec

**The token-table AST-fold engine.** Distinct from every prior engine: 25 recursive descent with inline evaluation; 26 token tape + explicit frame stack; 27 unit lattice + dual tables; 28 prime products; 29 regex parallel rounds; 30 stack-descent fixed-scale + Stein gcd; 31 RPN shunting-yard; 32 bracket-depth coefficient maps + CF rationals; 33 fixed-point rewrites + Bareiss rank; 34 census-tally literal expansion + centi-scale; 35 span-table prepass + memoized groups + 11-slot vector dot product. Engine 36's shape:

1. **Ordered token-table matching.** One ordered table — two-char element symbols (Ca, Na, Mg, Si, Cl) before one-char (C, H, K, N, O, S) — matched with `startsWith` at the cursor; no TWO-list dispatch, no span prepass, no memo.
2. **Explicit AST.** The parser builds nodes (atom / group-with-multiplier / sequence) BEFORE any arithmetic; evaluation is a separate post-order tree fold. (Engine 25's recursive descent evaluated inline; no prior engine materialized an AST.)
3. **BigInt sparse-map evaluation.** Every composition is a `Map<element, BigInt>`; mass = BigInt accumulation over the map — no 11-slot vectors, no dot product, no Number arithmetic on any mass.
4. **Shift-and-divmod rendering.** Every derived figure (percentages, molar amounts, gram conversions) computed as an exact BigInt quotient with explicit half-up rounding at the chapter's displayed precision (session-104); no floating point anywhere.
5. **Gates, in order:** the P18 restricted-name gate FIRST (label and formula scanned, case-insensitive; ANFO refused on the fertilizer shelf's own shadow), then admission (P refused BY NAME — the standing Ch 20/24 law; the refused-element scan lives in the tokenizer itself), then syntax (UNCLOSED, UNMATCHED, BAD CHAR at its index, count cap 999), then the non-integer hydrate gate (the Engine-29 class).
6. **The dims layer** {M, L, T, Θ} as BigInt 4-vectors with the always-printed-exponent canonical display (the house law since FC1's DORDER repair).

**Admission basis (11 held elements, myu):** C 120110, Ca 400780, Cl 354530, H 10080, K 390980, Mg 243050, N 140070, Na 229900, O 159990, S 320600, Si 280850 — the values on record since Engine 35's admission table; the review does not re-derive them, it re-verifies everything computed FROM them. **P is refused at the standing element-table law** (rows R1/R2/L4); ANFO/ammonium-nitrate names refused at the P18 gate (row R3).

## 2. Honest run history

- **Run 1: 56/56 PASS — CLEAN.** The engine's first execution reproduced all 56 got strings of the chapter's frozen run-5 corrected record byte-for-byte. Zero engine-core defects; zero repairs needed. The block is §4, frozen.
- **Harness-side slips, disclosed (neither touched the engine or the battery):**
  - The first code execution completed the full battery (every row computed) but its return statement crashed on a reporting-line slip: `new TextEncoder` does not exist in the sandbox (the byte-count line of the harness's own return object). The engine, battery, and every row were untouched; the re-execution — identical code, the reporting line replaced by a manual UTF-8 counter — reproduced the same 56/56 output. Recorded as the harness slip it is.
  - The §8-extraction harness's own "self-consistency" flag tripped on the summary line (the row regex does not match `RUN 5 SUMMARY: …`); a check artifact of the comparison harness, not a battery finding. All 56 parsed rows had got = expect.

## 3. Integrity gates

- **G1 (determinism):** the battery executed twice in the same run — byte-identical both times.
- **G2 (canary, non-vacuity):** L1's expectation deliberately corrupted to "46.66% N" in a battery copy — the harness FAILED that row (55/56), proving the PASS comparison is not vacuous; restored, the row passes.
- **G3 (MUST-FAIL in battery):** the B8 one-H-short biuret CAUGHT at gap 10,080 myu (part of the battery itself).
- **G4 (cross-engine byte equality) — THE REVIEW'S HEADLINE CHECK:** Engine 36's run-1 block (57 lines) and Engine 35's frozen run-5 block are **byte-identical** after normalizing the summary tag only (`RUN 5` → `RUN 1`, same length); verified by direct machine comparison against the block extracted from fc5-engine35-record.md §8. Two engines sharing zero code, built on different architectures (span-memo vectors vs AST BigInt sparse maps), produce the same 57-line battery output to the byte.
- **Size reconciliation, recorded to prevent future confusion:** the run-5 block's "7,334 bytes" (session 119's §8 header) is the block's UTF-16 length; the same block is 7,364 UTF-8 bytes. Both conventions agree because the content agrees; the two session records now name their counting convention.

## 4. The frozen run-1 block (56 rows; 7,334 UTF-16 units = 7,364 UTF-8 bytes)

```
 PASS T1 | admission table checksum Σmyu (11 elements) | got "265.094 (2650940 myu)" | expect "265.094 (2650940 myu)"
 PASS T2 | positional checksum Σ(i+1)·myu, alphabetical order | got "1599.373 (15993730 myu)" | expect "1599.373 (15993730 myu)"
 PASS S1 | self: H2O sanity | got "H2O 180150 myu = 18.015 r=0" | expect "H2O 180150 myu = 18.015 r=0"
 PASS S2 | self: the dot-product identity | got "dot: 20160+159990=180150 EXACT" | expect "dot: 20160+159990=180150 EXACT"
 PASS S3 | self: bracket scale (CH3)2CO -> C3H6O | got "(CH3)2CO 580800 myu = 58.080 r=0" | expect "(CH3)2CO 580800 myu = 58.080 r=0"
 PASS S4 | self: hydrate dot MgSO4·7H2O | got "MgSO4·7H2O 2464660 myu = 246.466 r=0" | expect "MgSO4·7H2O 2464660 myu = 246.466 r=0"
 PASS S5 | self: span-memo the long chain CH3(CH2)16COOH (Ch 23 stearic cross) | got "CH3(CH2)16COOH 2844840 myu = 284.484 r=0" | expect "CH3(CH2)16COOH 2844840 myu = 284.484 r=0"
 PASS S6 | self: canonical display, scrambled input O6C6H12 | got "C6H12O6 1801560 myu = 180.156 r=0" | expect "C6H12O6 1801560 myu = 180.156 r=0"
 PASS R1 | refusal: P at the admission gate (bone meal's Ca3(PO4)2 — the standing law) | got "REFUSED admission: P" | expect "REFUSED admission: P"
 PASS R2 | refusal: DAP (NH4)2HPO4 (the 46 face refused) | got "REFUSED admission: P" | expect "REFUSED admission: P"
 PASS R3 | refusal: ANFO at the P18 name gate (the fertilizer shelf's own shadow) | got "REFUSED P18: ANFO" | expect "REFUSED P18: ANFO"
 PASS R4 | refusal: unclosed group | got "UNCLOSED (" | expect "UNCLOSED ("
 PASS R5 | refusal: bad char | got "BAD CHAR "@" at 3" | expect "BAD CHAR "@" at 3"
 PASS R6 | refusal: non-integer hydrate (the Engine-29 class) | got "REFUSED non-integer hydrate" | expect "REFUSED non-integer hydrate"
 PASS P1 | pin H2O 18.015 Ch 4 | got "18.015 r=0" | expect "18.015 r=0"
 PASS P2 | pin NH3 17.031 Ch 20 | got "17.031 r=0" | expect "17.031 r=0"
 PASS P3 | pin N2 28.014 Ch 10 | got "28.014 r=0" | expect "28.014 r=0"
 PASS P4 | pin CO2 44.009 Ch 20 | got "44.009 r=0" | expect "44.009 r=0"
 PASS P5 | pin urea CO(NH2)2 60.056 Ch 20 | got "60.056 r=0" | expect "60.056 r=0"
 PASS P6 | pin (NH4)2SO4 132.134 Ch 20 | got "132.134 r=0" | expect "132.134 r=0"
 PASS P7 | pin K2CO3 138.204 Ch 14 | got "138.204 r=0" | expect "138.204 r=0"
 PASS P8 | pin K2O 94.195 Ch 14 | got "94.195 r=0" | expect "94.195 r=0"
 PASS P9 | pin CaCO3 100.086 Ch 14 | got "100.086 r=0" | expect "100.086 r=0"
 PASS P10 | pin CaO 56.077 Ch 14 | got "56.077 r=0" | expect "56.077 r=0"
 PASS P11 | pin Ca(OH)2 74.092 Ch 24 | got "74.092 r=0" | expect "74.092 r=0"
 PASS P12 | pin CaMg(CO3)2 184.399 Ch 30 | got "184.399 r=0" | expect "184.399 r=0"
 PASS P13 | pin MgSO4·7H2O 246.466 Ch 4 | got "246.466 r=0" | expect "246.466 r=0"
 PASS P14 | pin SiO2 60.083 Ch 30 | got "60.083 r=0" | expect "60.083 r=0"
 PASS N1 | NEW: biuret NH2CONHCONH2 = C2H5N3O2 (zero-hit corpus-wide — local masters, canvases, and all nine repo-only pages swept this session) | got "biuret C2H5N3O2 1030810 myu = 103.081 r=0" | expect "biuret C2H5N3O2 1030810 myu = 103.081 r=0"
 PASS B1 | balance: urea hydrolysis CO(NH2)2 + H2O = 2 NH3 + CO2 (Ch 36 corridor class) | got "LHS 780710 RHS 780710 gap 0 EXACT" | expect "LHS 780710 RHS 780710 gap 0 EXACT"
 PASS B2 | balance: biuret from urea 2 CO(NH2)2 = C2H5N3O2 + NH3 | got "LHS 1201120 RHS 1201120 gap 0 EXACT" | expect "LHS 1201120 RHS 1201120 gap 0 EXACT"
 PASS B3 | balance: nitrification NH3 + 2 O2 = HNO3 + H2O | got "LHS 810270 RHS 810270 gap 0 EXACT" | expect "LHS 810270 RHS 810270 gap 0 EXACT"
 PASS B4 | balance: the nitrate->nitrite leg 2 HNO3 = 2 HNO2 + O2 [formal model] | got "LHS 1260240 RHS 1260240 gap 0 EXACT" | expect "LHS 1260240 RHS 1260240 gap 0 EXACT"
 PASS B5 | balance: carbonation Ca(OH)2 + CO2 = CaCO3 + H2O | got "LHS 1181010 RHS 1181010 gap 0 EXACT" | expect "LHS 1181010 RHS 1181010 gap 0 EXACT"
 PASS B6 | balance: dolomite burn CaMg(CO3)2 = CaO + MgO + 2 CO2 (Ch 30 E12 class) | got "LHS 1843990 RHS 1843990 gap 0 EXACT" | expect "LHS 1843990 RHS 1843990 gap 0 EXACT"
 PASS B7 | balance: the char model C6H10O5 = 6 C + 5 H2O [flagged model] | got "LHS 1621410 RHS 1621410 gap 0 EXACT" | expect "LHS 1621410 RHS 1621410 gap 0 EXACT"
 PASS B8 | MUST-FAIL: one-H-short biuret C2H4N3O2 (the mis-typed condensation) | got "LHS 1201120 RHS 1191040 gap 10080 CAUGHT" | expect "LHS 1201120 RHS 1191040 gap 10080 CAUGHT"
 PASS C1 | C:N target 30:1 [convergent Cornell] — N as fraction of C+N | got "1/31 = 3.226% N of C+N" | expect "1/31 = 3.226% N of C+N"
 PASS C2 | C:N blend: grass 45/2.4 (18.75:1) + sawdust 480/1.2 per kg (400:1) [convergent Cornell band inputs] -> 30:1 | got "270/444 = 0.608 kg sawdust per kg grass" | expect "270/444 = 0.608 kg sawdust per kg grass"
 PASS C3 | C:N the urea credit: 100 kg leaves, %C 50, %N 0.75 (66.7:1) -> 30:1; deficit at urea's own %N | got "2750/3 g N deficit -> 1965 g urea" | expect "2750/3 g N deficit -> 1965 g urea"
 PASS C4 | biochar: the B7 char yield and its C:N face | got "720660/1621410 = 44.45% char; C:N undefined (no N)" | expect "720660/1621410 = 44.45% char; C:N undefined (no N)"
 PASS L1 | NPK: urea %N (Ch 20's own census) | got "280140/600560 = 46.65% N" | expect "280140/600560 = 46.65% N"
 PASS L2 | NPK: K2CO3 %K2O (Ch 14's potash convention) | got "941950/1382040 = 68.16% K2O" | expect "941950/1382040 = 68.16% K2O"
 PASS L3 | NPK: the ash label read — 1 kg ash at the 6% K2O-eq band [convergent] | got "60 g K2O-eq -> 88.0 g K2CO3-eq per kg ash" | expect "60 g K2O-eq -> 88.0 g K2CO3-eq per kg ash"
 PASS L4 | NPK: the DAP 18-46-0 label — the 46 face refused at the table | got "REFUSED admission: P" | expect "REFUSED admission: P"
 PASS H1 | heat: glucose oxidation C6H12O6 + 6 O2 = 6 CO2 + 6 H2O + dH | got "LHS 3721440 RHS 3721440 gap 0 EXACT; dH -2.803 MJ/mol [convergent]" | expect "LHS 3721440 RHS 3721440 gap 0 EXACT; dH -2.803 MJ/mol [convergent]"
 PASS H2 | heat: the 50-kg pile ledger, +20 K, c_p 4.184 [flagged model: water-dominated] | got "4184000 J / 2803000 = 1.493 mol -> 268.9 g glucose-equivalent" | expect "4184000 J / 2803000 = 1.493 mol -> 268.9 g glucose-equivalent"
 PASS H3 | heat: the thermophilic band edges [55-65 C, Cornell] on the same ledger | got "7322000 J -> 470.6 g; 9414000 J -> 605.1 g" | expect "7322000 J -> 470.6 g; 9414000 J -> 605.1 g"
 PASS H4 | heat: Ch 14's slaking band on the shell-kiln cross (4.746 mol CaO, -64.8 kJ/mol) | got "4.746 x 64.8 = 307.5 kJ [convergent band -63.7..-65.2]" | expect "4.746 x 64.8 = 307.5 kJ [convergent band -63.7..-65.2]"
 PASS D1 | dim: specific heat c_p [J/(g·K)] | got "L^2·T^-2·Θ^-1" | expect "L^2·T^-2·Θ^-1"
 PASS D2 | dim: power | got "M^1·L^2·T^-3" | expect "M^1·L^2·T^-3"
 PASS D3 | dim: C:N and %N | got "dimensionless" | expect "dimensionless"
 PASS X1 | cross: Ch 36's urea corridor 780710 reproduced from FC5's table | got "780710 EXACT (Ch 36 E3/E7 class)" | expect "780710 EXACT (Ch 36 E3/E7 class)"
 PASS X2 | cross: Ch 30's dolomite 1843990 reproduced | got "1843990 EXACT (Ch 30)" | expect "1843990 EXACT (Ch 30)"
 PASS X3 | cross: Ch 14's potash convention 68.16% reproduced | got "68.16 EXACT (Ch 14)" | expect "68.16 EXACT (Ch 14)"
 PASS X4 | cross: Ch 20's urea %N 46.65% reproduced | got "46.65 EXACT (Ch 20)" | expect "46.65 EXACT (Ch 20)"
RUN 1 SUMMARY: 56/56 PASS — CLEAN
```

## 5. Expectations and inputs provenance

- The 56 expectations are the frozen run-5 corrected strings **verbatim** — the chapter's record (§8 of fc5-engine35-record.md), including the six web-corrected rows (C2, C3, L3, H1, H2, H3).
- The row names are the authoring battery's names verbatim — including N1's session-119 sweep parenthetical and S5's "span-memo" phrasing. The names label the authoring engine's techniques; Engine 36 re-verifies the values under them. (G4's byte-equality proves the names match too.)
- The authoring harness source was lost to the session-119 compaction (recorded there); row INPUTS were therefore reconstructed from the row names and got strings exactly as session 119 part 2 rebuilt them. The refusal-row inputs chosen to reproduce the frozen got strings: R4 `H2(O` (UNCLOSED), R5 `H2O@` (BAD CHAR "@" at 3), R6 `MgSO4·0.35H2O` (non-integer hydrate); R1/R2 the bone-meal/DAP formulas with their labels, L4 the DAP 18-46-0 label; R3 ammonium nitrate's formula under the ANFO label. The derived-row inputs re-derive the six corrected rows from their corrected inputs (grass 45%C/2.4%N; sawdust 480 g C / 1.2 g N per kg; leaves 50%C/0.75%N; ash 6% K2O-eq; ΔH −2.803 MJ/mol; c_p 4.184).
- **No expectation was patched to make a row pass.** Every mismatch would have been a finding raised for part-2 adjudication; none occurred.

## 6. The full run-1 source, verbatim (the session-119 lesson: no placeholder harnesses)

```typescript
// ===== ENGINE 36: the token-table AST-fold engine (fresh build, session 120) =====
const MYU36: Record<string, bigint> = {C:120110n,Ca:400780n,Cl:354530n,H:10080n,K:390980n,Mg:243050n,N:140070n,Na:229900n,O:159990n,S:320600n,Si:280850n};
const ADM36 = ["C","Ca","Cl","H","K","Mg","N","Na","O","S","Si"];
const REF1 = ["P","B","F","I"];
const REF2 = ["Fe","Cu","Ag","Al","Mn","Zn","Ba","Pb","Sn","Cr","Ni","Li","Br","Hg","Ti","Sb","Co","He","Ne","Ar"];
const P18_36 = ["ANFO","GUNPOWDER","BLACK POWDER","DYNAMITE","FIREWORKS","RAT POISON","FUEL OIL"];
class Gate extends Error { constructor(public kind: string, public text: string) { super(text); } }
const TOKTAB: Array<[string,string]> = [["Ca","el"],["Na","el"],["Mg","el"],["Si","el"],["Cl","el"],["C","el"],["H","el"],["K","el"],["N","el"],["O","el"],["S","el"],["(","("],[")",")"]];
type Tok = {t:string; k:string; i:number};
function tokenize36(s: string): Tok[] {
  const out: Tok[] = []; let i = 0;
  while (i < s.length) {
    const ch = s[i];
    if (ch === " ") { i++; continue; }
    if (ch >= "0" && ch <= "9") { let j = i; while (j < s.length && s[j] >= "0" && s[j] <= "9") j++; out.push({t: s.slice(i,j), k:"num", i}); i = j; continue; }
    let hit: Tok | null = null;
    for (const [sym,kind] of TOKTAB) { if (s.startsWith(sym,i)) { hit = {t:sym,k:kind,i}; break; } }
    if (!hit) {
      for (const e of REF2) if (s.startsWith(e,i)) throw new Gate("admission","REFUSED admission: "+e);
      if (REF1.includes(ch)) throw new Gate("admission","REFUSED admission: "+ch);
      throw new Gate("syntax",'BAD CHAR "'+ch+'" at '+i);
    }
    out.push(hit); i += hit.t.length;
  }
  return out;
}
type Node = {k:"atom"; el:string; n:bigint} | {k:"grp"; kid:Node; n:bigint} | {k:"seq"; kids:Node[]};
function readNum(toks: Tok[], p: number): [bigint, number] {
  if (p < toks.length && toks[p].k === "num") { const v = BigInt(toks[p].t); if (v > 999n) throw new Gate("syntax","REFUSED count cap"); return [v, p+1]; }
  return [1n, p];
}
function parseSeq(toks: Tok[], p: number): [Node[], number] {
  const kids: Node[] = [];
  while (p < toks.length && toks[p].k !== ")") {
    const t = toks[p];
    if (t.k === "el") { p++; const [n,p2] = readNum(toks,p); kids.push({k:"atom",el:t.t,n}); p = p2; continue; }
    if (t.k === "(") {
      p++; const [inner,p2] = parseSeq(toks,p);
      if (p2 >= toks.length) throw new Gate("syntax","UNCLOSED (");
      p = p2 + 1; const [n,p3] = readNum(toks,p);
      kids.push({k:"grp",kid:{k:"seq",kids:inner},n}); p = p3; continue;
    }
    throw new Gate("syntax","BAD CHAR at "+t.i);
  }
  return [kids, p];
}
function parseSegment(seg: string): Node {
  const m = seg.match(/^(\d+)(\.\d+)?/);
  let coef = 1n; let s = seg;
  if (m) {
    if (m[2]) throw new Gate("hydrate","REFUSED non-integer hydrate");
    coef = BigInt(m[1]); if (coef > 999n) throw new Gate("syntax","REFUSED count cap");
    s = seg.slice(m[1].length);
  }
  const toks = tokenize36(s);
  const [kids,p] = parseSeq(toks,0);
  if (p < toks.length) {
    const t = toks[p];
    if (t.k === ")") throw new Gate("syntax","UNMATCHED )");
    throw new Gate("syntax","BAD CHAR at "+t.i);
  }
  if (coef === 1n) return {k:"seq",kids};
  return {k:"grp",kid:{k:"seq",kids},n:coef};
}
function fold36(node: Node): Map<string,bigint> {
  if (node.k === "atom") { const m = new Map<string,bigint>(); m.set(node.el,node.n); return m; }
  if (node.k === "grp") { const m = fold36(node.kid); const out = new Map<string,bigint>(); m.forEach((v,k)=>out.set(k,v*node.n)); return out; }
  const out = new Map<string,bigint>();
  for (const kid of node.kids) { const m = fold36(kid); m.forEach((v,k)=>out.set(k,(out.get(k)||0n)+v)); }
  return out;
}
function mass36(m: Map<string,bigint>): bigint { let M = 0n; m.forEach((v,k)=>M += MYU36[k]*v); return M; }
function disp3(myu: bigint): string {
  const x = (myu + 5n) / 10n; const w = x / 1000n; let f = (x % 1000n).toString(); while (f.length < 3) f = "0"+f;
  return w.toString() + "." + f;
}
function canon36(m: Map<string,bigint>): string {
  let s = ""; for (const el of ADM36) { const v = m.get(el); if (v) s += el + (v > 1n ? v.toString() : ""); } return s;
}
function p1836(label: string, f: string): string | null {
  const u = (label + " " + f).toUpperCase();
  for (const n of P18_36) if (u.includes(n)) return "REFUSED P18: " + n;
  return null;
}
function mergeMap(dst: Map<string,bigint>, src: Map<string,bigint>) { src.forEach((v,k)=>dst.set(k,(dst.get(k)||0n)+v)); }
function compMap36(f: string, label: string): Map<string,bigint> {
  const g = p1836(label, f); if (g) throw new Gate("p18", g);
  const m = new Map<string,bigint>();
  for (const seg of f.split("·")) mergeMap(m, fold36(parseSegment(seg.trim())));
  return m;
}
function side36(str: string): {m: Map<string,bigint>; myu: bigint} {
  const m = new Map<string,bigint>();
  for (const t of str.split("+")) mergeMap(m, fold36(parseSegment(t.trim())));
  return {m, myu: mass36(m)};
}
function mapsEq(a: Map<string,bigint>, b: Map<string,bigint>): boolean {
  if (a.size !== b.size) return false;
  for (const [k,v] of a) { if (b.get(k) !== v) return false; } return true;
}
function bal36(l: string, r: string): string {
  const L = side36(l), R = side36(r);
  const d = L.myu - R.myu; const g = d < 0n ? -d : d;
  const ok = g === 0n && mapsEq(L.m, R.m);
  return "LHS " + L.myu + " RHS " + R.myu + " gap " + g + " " + (ok ? "EXACT" : "CAUGHT");
}
function composeRow(f: string, label = ""): string {
  const m = compMap36(f, label); const myu = mass36(m);
  const disp = label ? label + " " + canon36(m) : f;
  return disp + " " + myu + " myu = " + disp3(myu) + " r=" + (myu % 10n);
}
function canonRow(f: string): string {
  const m = compMap36(f, ""); const myu = mass36(m);
  return canon36(m) + " " + myu + " myu = " + disp3(myu) + " r=" + (myu % 10n);
}
function pinRow(f: string): string { const myu = mass36(compMap36(f, "")); return disp3(myu) + " r=" + (myu % 10n); }
function contribTrace(f: string): string {
  const m = compMap36(f, ""); const parts: string[] = []; let tot = 0n;
  for (const el of ADM36) { const v = m.get(el); if (v) { const c = v * MYU36[el]; parts.push(c.toString()); tot += c; } }
  const mm = mass36(m);
  return "dot: " + parts.join("+") + "=" + mm + (tot === mm ? " EXACT" : " MISMATCH");
}
function round36(a: bigint, b: bigint, dp: number): string {
  const sc = 10n ** BigInt(dp); const num = a * sc; const q = num / b; const r = num % b;
  let v = q; if (r * 2n >= b) v = q + 1n;
  const neg = v < 0n; const av = neg ? -v : v;
  const ip = av / sc, fp = av % sc;
  let fs = fp.toString(); while (fs.length < dp) fs = "0"+fs;
  return (neg ? "-" : "") + ip.toString() + (dp ? "." + fs : "");
}
const DIMNM = ["M","L","T","Θ"];
function dim36(exps: bigint[]): string {
  if (exps.every(e => e === 0n)) return "dimensionless";
  return exps.map((e,i) => e === 0n ? "" : DIMNM[i]+"^"+e).filter(s => s !== "").join("·");
}
const sub4 = (a: bigint[], b: bigint[]) => a.map((x,i) => x - b[i]);
const Q_PILE = 50000n * 20n * 4184n / 1000n;   // 4,184,000 J (50 kg x 20 K x 4.184)
const DH = 2803n * 1000n;                      // 2,803,000 J/mol (the corrected dHc)
const CPKG = 50000n * 4184n / 1000n;           // 209,200 J/K for the 50-kg pile
const GLU = 180156n;                           // glucose 180.156 g/mol, in myu
const UREA_M = mass36(compMap36("CO(NH2)2",""));
const UREA_N = 2n * 140070n;
const K2CO3_M = mass36(compMap36("K2CO3",""));
const K2O_M = mass36(compMap36("K2O",""));
const B7L = side36("C6H10O5");
type Row = {id:string; name:string; expect:string; run:()=>string};
const battery: Row[] = [
  {id:"T1",name:"admission table checksum Σmyu (11 elements)",expect:"265.094 (2650940 myu)",run:()=>{let S=0n;for(const e of ADM36)S+=MYU36[e];return disp3(S)+" ("+S+" myu)";}},
  {id:"T2",name:"positional checksum Σ(i+1)·myu, alphabetical order",expect:"1599.373 (15993730 myu)",run:()=>{let S=0n;for(let i=0;i<11;i++)S+=BigInt(i+1)*MYU36[ADM36[i]];return disp3(S)+" ("+S+" myu)";}},
  {id:"S1",name:"self: H2O sanity",expect:"H2O 180150 myu = 18.015 r=0",run:()=>composeRow("H2O")},
  {id:"S2",name:"self: the dot-product identity",expect:"dot: 20160+159990=180150 EXACT",run:()=>contribTrace("H2O")},
  {id:"S3",name:"self: bracket scale (CH3)2CO -> C3H6O",expect:"(CH3)2CO 580800 myu = 58.080 r=0",run:()=>composeRow("(CH3)2CO")},
  {id:"S4",name:"self: hydrate dot MgSO4·7H2O",expect:"MgSO4·7H2O 2464660 myu = 246.466 r=0",run:()=>composeRow("MgSO4·7H2O")},
  {id:"S5",name:"self: span-memo the long chain CH3(CH2)16COOH (Ch 23 stearic cross)",expect:"CH3(CH2)16COOH 2844840 myu = 284.484 r=0",run:()=>composeRow("CH3(CH2)16COOH")},
  {id:"S6",name:"self: canonical display, scrambled input O6C6H12",expect:"C6H12O6 1801560 myu = 180.156 r=0",run:()=>canonRow("O6C6H12")},
  {id:"R1",name:"refusal: P at the admission gate (bone meal's Ca3(PO4)2 — the standing law)",expect:"REFUSED admission: P",run:()=>composeRow("Ca3(PO4)2","bone meal")},
  {id:"R2",name:"refusal: DAP (NH4)2HPO4 (the 46 face refused)",expect:"REFUSED admission: P",run:()=>composeRow("(NH4)2HPO4","DAP")},
  {id:"R3",name:"refusal: ANFO at the P18 name gate (the fertilizer shelf's own shadow)",expect:"REFUSED P18: ANFO",run:()=>composeRow("NH4NO3","ANFO")},
  {id:"R4",name:"refusal: unclosed group",expect:"UNCLOSED (",run:()=>composeRow("H2(O")},
  {id:"R5",name:"refusal: bad char",expect:'BAD CHAR "@" at 3',run:()=>composeRow("H2O@")},
  {id:"R6",name:"refusal: non-integer hydrate (the Engine-29 class)",expect:"REFUSED non-integer hydrate",run:()=>composeRow("MgSO4·0.35H2O")},
  {id:"P1",name:"pin H2O 18.015 Ch 4",expect:"18.015 r=0",run:()=>pinRow("H2O")},
  {id:"P2",name:"pin NH3 17.031 Ch 20",expect:"17.031 r=0",run:()=>pinRow("NH3")},
  {id:"P3",name:"pin N2 28.014 Ch 10",expect:"28.014 r=0",run:()=>pinRow("N2")},
  {id:"P4",name:"pin CO2 44.009 Ch 20",expect:"44.009 r=0",run:()=>pinRow("CO2")},
  {id:"P5",name:"pin urea CO(NH2)2 60.056 Ch 20",expect:"60.056 r=0",run:()=>pinRow("CO(NH2)2")},
  {id:"P6",name:"pin (NH4)2SO4 132.134 Ch 20",expect:"132.134 r=0",run:()=>pinRow("(NH4)2SO4")},
  {id:"P7",name:"pin K2CO3 138.204 Ch 14",expect:"138.204 r=0",run:()=>pinRow("K2CO3")},
  {id:"P8",name:"pin K2O 94.195 Ch 14",expect:"94.195 r=0",run:()=>pinRow("K2O")},
  {id:"P9",name:"pin CaCO3 100.086 Ch 14",expect:"100.086 r=0",run:()=>pinRow("CaCO3")},
  {id:"P10",name:"pin CaO 56.077 Ch 14",expect:"56.077 r=0",run:()=>pinRow("CaO")},
  {id:"P11",name:"pin Ca(OH)2 74.092 Ch 24",expect:"74.092 r=0",run:()=>pinRow("Ca(OH)2")},
  {id:"P12",name:"pin CaMg(CO3)2 184.399 Ch 30",expect:"184.399 r=0",run:()=>pinRow("CaMg(CO3)2")},
  {id:"P13",name:"pin MgSO4·7H2O 246.466 Ch 4",expect:"246.466 r=0",run:()=>pinRow("MgSO4·7H2O")},
  {id:"P14",name:"pin SiO2 60.083 Ch 30",expect:"60.083 r=0",run:()=>pinRow("SiO2")},
  {id:"N1",name:"NEW: biuret NH2CONHCONH2 = C2H5N3O2 (zero-hit corpus-wide — local masters, canvases, and all nine repo-only pages swept this session)",expect:"biuret C2H5N3O2 1030810 myu = 103.081 r=0",run:()=>composeRow("NH2CONHCONH2","biuret")},
  {id:"B1",name:"balance: urea hydrolysis CO(NH2)2 + H2O = 2 NH3 + CO2 (Ch 36 corridor class)",expect:"LHS 780710 RHS 780710 gap 0 EXACT",run:()=>bal36("CO(NH2)2 + H2O","2 NH3 + CO2")},
  {id:"B2",name:"balance: biuret from urea 2 CO(NH2)2 = C2H5N3O2 + NH3",expect:"LHS 1201120 RHS 1201120 gap 0 EXACT",run:()=>bal36("2 CO(NH2)2","C2H5N3O2 + NH3")},
  {id:"B3",name:"balance: nitrification NH3 + 2 O2 = HNO3 + H2O",expect:"LHS 810270 RHS 810270 gap 0 EXACT",run:()=>bal36("NH3 + 2 O2","HNO3 + H2O")},
  {id:"B4",name:"balance: the nitrate->nitrite leg 2 HNO3 = 2 HNO2 + O2 [formal model]",expect:"LHS 1260240 RHS 1260240 gap 0 EXACT",run:()=>bal36("2 HNO3","2 HNO2 + O2")},
  {id:"B5",name:"balance: carbonation Ca(OH)2 + CO2 = CaCO3 + H2O",expect:"LHS 1181010 RHS 1181010 gap 0 EXACT",run:()=>bal36("Ca(OH)2 + CO2","CaCO3 + H2O")},
  {id:"B6",name:"balance: dolomite burn CaMg(CO3)2 = CaO + MgO + 2 CO2 (Ch 30 E12 class)",expect:"LHS 1843990 RHS 1843990 gap 0 EXACT",run:()=>bal36("CaMg(CO3)2","CaO + MgO + 2 CO2")},
  {id:"B7",name:"balance: the char model C6H10O5 = 6 C + 5 H2O [flagged model]",expect:"LHS 1621410 RHS 1621410 gap 0 EXACT",run:()=>bal36("C6H10O5","6 C + 5 H2O")},
  {id:"B8",name:"MUST-FAIL: one-H-short biuret C2H4N3O2 (the mis-typed condensation)",expect:"LHS 1201120 RHS 1191040 gap 10080 CAUGHT",run:()=>bal36("2 CO(NH2)2","C2H4N3O2 + NH3")},
  {id:"C1",name:"C:N target 30:1 [convergent Cornell] — N as fraction of C+N",expect:"1/31 = 3.226% N of C+N",run:()=>"1/31 = "+round36(100n,31n,3)+"% N of C+N"},
  {id:"C2",name:"C:N blend: grass 45/2.4 (18.75:1) + sawdust 480/1.2 per kg (400:1) [convergent Cornell band inputs] -> 30:1",expect:"270/444 = 0.608 kg sawdust per kg grass",
    run:()=>{ const den=(4800n-360n), num=(7200n-4500n); // (4500+4800x)=30(240+12x) in tenths -> 4440x=2700 -> descale /10
      return (num/10n)+"/"+(den/10n)+" = "+round36(num,den,3)+" kg sawdust per kg grass"; }},
  {id:"C3",name:"C:N the urea credit: 100 kg leaves, %C 50, %N 0.75 (66.7:1) -> 30:1; deficit at urea's own %N",expect:"2750/3 g N deficit -> 1965 g urea",
    run:()=>{ const dn=(50000n-30n*750n), dd=30n;      // deficit=(C/30 - N)=(50000-22500)/30=27500/30 -> descale -> 2750/3
      return (dn/10n)+"/"+(dd/10n)+" g N deficit -> "+round36(dn*UREA_M, dd*UREA_N, 0)+" g urea"; }},
  {id:"C4",name:"biochar: the B7 char yield and its C:N face",expect:"720660/1621410 = 44.45% char; C:N undefined (no N)",
    run:()=>{ const cC=B7L.m.get("C")!*MYU36["C"]; const noN=!B7L.m.has("N");
      return cC+"/"+B7L.myu+" = "+round36(cC*100n,B7L.myu,2)+"% char; C:N "+(noN?"undefined (no N)":"defined"); }},
  {id:"L1",name:"NPK: urea %N (Ch 20's own census)",expect:"280140/600560 = 46.65% N",run:()=>UREA_N+"/"+UREA_M+" = "+round36(UREA_N*100n,UREA_M,2)+"% N"},
  {id:"L2",name:"NPK: K2CO3 %K2O (Ch 14's potash convention)",expect:"941950/1382040 = 68.16% K2O",run:()=>K2O_M+"/"+K2CO3_M+" = "+round36(K2O_M*100n,K2CO3_M,2)+"% K2O"},
  {id:"L3",name:"NPK: the ash label read — 1 kg ash at the 6% K2O-eq band [convergent]",expect:"60 g K2O-eq -> 88.0 g K2CO3-eq per kg ash",
    run:()=>{ const k2o=1000n*6n/100n; return k2o+" g K2O-eq -> "+round36(k2o*K2CO3_M,K2O_M,1)+" g K2CO3-eq per kg ash"; }},
  {id:"L4",name:"NPK: the DAP 18-46-0 label — the 46 face refused at the table",expect:"REFUSED admission: P",run:()=>composeRow("(NH4)2HPO4","DAP 18-46-0")},
  {id:"H1",name:"heat: glucose oxidation C6H12O6 + 6 O2 = 6 CO2 + 6 H2O + dH",expect:"LHS 3721440 RHS 3721440 gap 0 EXACT; dH -2.803 MJ/mol [convergent]",run:()=>bal36("C6H12O6 + 6 O2","6 CO2 + 6 H2O")+"; dH -2.803 MJ/mol [convergent]"},
  {id:"H2",name:"heat: the 50-kg pile ledger, +20 K, c_p 4.184 [flagged model: water-dominated]",expect:"4184000 J / 2803000 = 1.493 mol -> 268.9 g glucose-equivalent",
    run:()=>Q_PILE+" J / "+DH+" = "+round36(Q_PILE,DH,3)+" mol -> "+round36(Q_PILE*GLU,DH*1000n,1)+" g glucose-equivalent"},
  {id:"H3",name:"heat: the thermophilic band edges [55-65 C, Cornell] on the same ledger",expect:"7322000 J -> 470.6 g; 9414000 J -> 605.1 g",
    run:()=>{ const q55=CPKG*35n, q65=CPKG*45n;
      return q55+" J -> "+round36(q55*GLU,DH*1000n,1)+" g; "+q65+" J -> "+round36(q65*GLU,DH*1000n,1)+" g"; }},
  {id:"H4",name:"heat: Ch 14's slaking band on the shell-kiln cross (4.746 mol CaO, -64.8 kJ/mol)",expect:"4.746 x 64.8 = 307.5 kJ [convergent band -63.7..-65.2]",
    run:()=>"4.746 x 64.8 = "+round36(4746n*648n,10000n,1)+" kJ [convergent band -63.7..-65.2]"},
  {id:"D1",name:"dim: specific heat c_p [J/(g·K)]",expect:"L^2·T^-2·Θ^-1",run:()=>dim36(sub4([1n,2n,-2n,0n],[1n,0n,0n,1n]))},
  {id:"D2",name:"dim: power",expect:"M^1·L^2·T^-3",run:()=>dim36(sub4([1n,2n,-2n,0n],[0n,0n,1n,0n]))},
  {id:"D3",name:"dim: C:N and %N",expect:"dimensionless",run:()=>dim36(sub4([0n,0n,0n,0n],[0n,0n,0n,0n]))},
  {id:"X1",name:"cross: Ch 36's urea corridor 780710 reproduced from FC5's table",expect:"780710 EXACT (Ch 36 E3/E7 class)",run:()=>side36("CO(NH2)2 + H2O").myu+" EXACT (Ch 36 E3/E7 class)"},
  {id:"X2",name:"cross: Ch 30's dolomite 1843990 reproduced",expect:"1843990 EXACT (Ch 30)",run:()=>side36("CaMg(CO3)2").myu+" EXACT (Ch 30)"},
  {id:"X3",name:"cross: Ch 14's potash convention 68.16% reproduced",expect:"68.16 EXACT (Ch 14)",run:()=>round36(K2O_M*100n,K2CO3_M,2)+" EXACT (Ch 14)"},
  {id:"X4",name:"cross: Ch 20's urea %N 46.65% reproduced",expect:"46.65 EXACT (Ch 20)",run:()=>round36(UREA_N*100n,UREA_M,2)+" EXACT (Ch 20)"}
];
function runBattery(bat: Row[], tag: string): string[] {
  const lines: string[] = []; let pass = 0; let fail = false;
  for (const r of bat) {
    let got: string;
    try { got = r.run(); } catch (e: any) { got = (e instanceof Gate) ? e.text : "ERROR: " + (e?.message ?? e); }
    const ok = got === r.expect;
    if (ok) pass++; else fail = true;
    lines.push(" " + (ok ? "PASS " : "FAIL ") + r.id + " | " + r.name + ' | got "' + got + '" | expect "' + r.expect + '"');
  }
  lines.push("RUN " + tag + " SUMMARY: " + pass + "/" + bat.length + " PASS" + (fail ? "" : " — CLEAN"));
  return lines;
}
```

## 7. Part-2 owed list (BEFORE the review closes)

1. **Pin re-greps (session-112 line)** re-verified in the owners' own pages against the counts on record: H2O 18.015 Ch 4 ×1; NH3 17.031 Ch 20 ×13; N2 28.014 Ch 10 ×4; CO2 44.009 Ch 20 ×6; urea 60.056 Ch 20 ×3; (NH4)2SO4 132.134 Ch 20 ×2; K2CO3 138.204 Ch 14 ×2; K2O 94.195 Ch 14 ×2; CaCO3 100.086 Ch 14 ×7; CaO 56.077 Ch 14 ×2; Ca(OH)2 74.092 Ch 24 ×5; CaMg(CO3)2 184.399 Ch 30 ×6; MgSO4·7H2O 246.466 Ch 4 ×3 (Ch 3 ×1 honest); SiO2 60.083 Ch 30 ×4; the heat anchors 4.184 Ch 7 ×10 and 2256 Ch 7 ×4.
2. **N1 re-proof at the review HEAD (session-100 line):** biuret (ci), "103.08", "103.081", C2H5N3O2 across the local masters and the repo-only pages (ch01, ch02, ch31–ch36, fc1–fc5) at the post-part-1 HEAD, fetch lengths checked against the directory listing; the reused-pin conversion protocol if any hit.
3. **The [convergent] battery re-confirmed at named sources:** Cornell 30:1 + 55–65 °C; the grass/leaves C:N inputs; urea's biuret quality limit (<0.5% China mandate, >1% seed/seedling/foliar, forms >132 °C); ash K2O ~6% typical; glucose ΔHc −2,803 kJ/mol; DAP 18-46-0 label class; slaking −63.7..−65.2 (Ch 14's own band).
4. **The canvas battery block vs the record:** confirm the chapter's Lab FC5.1 run-5 block matches fc5-engine35-record.md §8 byte-for-byte (the spliced record of session 119).
5. **Ex FC5.6's withheld ◆ answer delivered** at the Revision Appendix (battery rows and [convergent] endpoints only, no new figures).
6. **The Revision Appendix assembled and appended** after the chapter's closing italic; the status line drafted → reviewed; map FC5 drafted → reviewed; row 120 close; ALWAYS-SYNC.
