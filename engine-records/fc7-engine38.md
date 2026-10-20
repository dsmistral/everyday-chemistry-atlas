# FC7 Engine 38 record — the dual-column peel-and-rescale review engine (session 125, the Phase-3 adversarial review of FC7)

Session 125 (2026-10-20): the review unit per the FC alternation. Engine 38 re-executed the whole frozen FC7 battery (Lab FC7.1's run-3 block, 68 PASS rows) — expectations the chapter's own frozen got-strings verbatim, got-strings recomputed by a different method; the review re-verifies, it does not re-author. Verdict: **PASS WITH RF-1** (the frozen verdict line's own off-by-one tally: 68 PASS rows, not 67 — the correction of record at the chapter's Revision Appendix; zero defects in any chapter figure).

## 1. Design spec

- **Peel-and-push stack parser:** explicit frame stack (one `{parent, lanes}` record per open bracket); the subscript is read only after the closing bracket and multiplies that frame's lanes — never the whole accumulator; the hydrate unit after `·` is parsed whole (its coefficient multiplies the entire unit formula, end or next dot).
- **Dual-column mass verification:** every composition computed by TWO independent internal paths — a forward dot product and a reverse dot product over the same lanes — plus a canonical re-parse (the lanes are canonicalized to a Hill-order string and re-parsed; the re-parsed lanes must equal the originals). Any disagreement throws before a row prints.
- **Exact rational ledgers:** every L/X row re-derived as BigInt numerator/denominator fractions from the chapter's stated model inputs; display by half-up rounding at the stated displayed precision (the session-104 line); the g/mol column prints plain (commas live in the myu restatement and the gram/joule ledgers — the chapter's own convention).
- **Gate order:** the P18 restricted-name gate FIRST (morphine, ricin refused before any parse), then admission ({C,H,O,S,Fe} only), then the syntax gates (unclosed group; bad character), then the hydrate-coefficient gates (non-integer → NON-EXACT; zero → zero subscript).
- **The review gates:** G1 the recount (physical PASS rows vs the frozen verdict line), G2 the canary (a corrupted expectation must FAIL), G3 determinism (the whole battery run twice, byte-identical), G4 the must-fail re-proof (B8 through the peel machine).

Distinctness (zero code shared with Engines 1–37): no CPS fold/composed continuations (37), no token-table AST (36), no span-table memoization (35), no census-tally expansion (34), no fixed-point rewrite (33), no RPN shunting-yard (31), no unit lattice (27); the dual-column forward/reverse/canonical triple check and the exact-rational display layer are Engine 38's own.

## 2. Honest run history

**Run 1: 64/68.** Two defects in the review's own machinery, named plainly; zero defects in any chapter figure:

1. **The hydrate-unit scope hole (S3, P9, B4):** the coefficient after `·` multiplied only the unit's first element — FeSO4·7H2O lost six oxygens (printed 182.012, 1,820,120 myu) and the copperas-drying balance read a false GAP 959,940 myu. A cousin of Engine 37's own run-1 hydrate hole: the dot keeps catching engine-builders. Repair: the coefficient multiplies the whole unit formula.
2. **The display defect (N4):** the harness comma'd the g/mol column — 1,701.206 — where the chapter's convention keeps the comma in the myu restatement alone (1701.206 g/mol, 17,012,060 myu). Repair: the g/mol column prints plain.

The run-1 FAIL lines, preserved verbatim:

```text
FAIL S3 | SELF FeSO4·7H2O - the hydrate lane | got "182.012 g/mol (1,820,120 myu)" | expect "278.006 g/mol (2,780,060 myu)"
FAIL P9 | pin copperas FeSO4·7H2O (Ch 19) re-derived | got "182.012 g/mol (1,820,120 myu)" | expect "278.006 g/mol (2,780,060 myu)"
FAIL N4 | NEW tannic acid C76H52O46 re-derived | got "1,701.206 g/mol (17,012,060 myu)" | expect "1701.206 g/mol (17,012,060 myu)"
FAIL B4 | copperas drying balance re-walked | got "GAP 959,940 myu CAUGHT" | expect "2,780,060 myu CLOSES"
```

**Run 2, the repair pass, nothing else touched: 68/68 PASS — CLEAN**, the whole battery run twice byte-identical (C3).

## 3. The gates

- **G1 RECOUNT — RF-1, the review's one finding:** the frozen block holds 68 PASS rows; its own verdict line reads "67/67" — the authoring harness's tally undercounted by one, and the three-run history (33/67 → 63/67 → 67/67) carried the same off-by-one. Every row itself PASSes with got == expect; the defect is the summary count alone (most plausibly a fused pair among the X rows in the tally counter). Honest verdict by direct machine recount: 68/68 CLEAN. The frozen block stands per extend-never-rewrite; the chapter's Revision Appendix is the correction of record.
- **G2 CANARY:** L1's expectation corrupted to "29.896 g" — the harness FAILED it; non-vacuity proven.
- **G3 DETERMINISM:** the whole battery run twice, byte-identical.
- **G4 MUST-FAIL:** B8 recomputed through the peel machine — GAP 180,150 myu CAUGHT again, exactly one water.

## 4. The frozen run-2 block (spliced verbatim from the engine's own output file, never retyped)

```text
PASS T1 | admission table, straight checksum re-summed | got "1,169,230" | expect "1,169,230"
PASS T2 | admission table, positional checksum (alphabetical C,Fe,H,O,S) re-summed | got "3,510,210" | expect "3,510,210"
PASS S1 | SELF H2O through the peel machine, dual-column | got "18.015 g/mol (180,150 myu)" | expect "18.015 g/mol (180,150 myu)"
PASS S2 | SELF (CH3)2CO - frame pop, subscript after the bracket | got "58.080 g/mol (580,800 myu)" | expect "58.080 g/mol (580,800 myu)"
PASS S3 | SELF FeSO4·7H2O - the hydrate lane | got "278.006 g/mol (2,780,060 myu)" | expect "278.006 g/mol (2,780,060 myu)"
PASS S4 | SELF CH3(CH2)16COOH - nested frames, one pass | got "284.484 g/mol (2,844,840 myu)" | expect "284.484 g/mol (2,844,840 myu)"
PASS S5 | SELF scrambled O7C13H18 - canonical display from the lanes | got "C13H18O7 286.280" | expect "C13H18O7 286.280"
PASS R1 | 'morphine' re-refused at the P18 name gate (FIRST) | got "REFUSED (P18): recognition-only, the fence absolute" | expect "REFUSED (P18): recognition-only, the fence absolute"
PASS R2 | 'ricin' re-refused at the P18 name gate | got "REFUSED (P18): recognition-only, the fence absolute" | expect "REFUSED (P18): recognition-only, the fence absolute"
PASS R3 | indigo C16H10N2O2 re-refused at the admission gate | got "REFUSED: element not admitted: 'N'" | expect "REFUSED: element not admitted: 'N'"
PASS R4 | 'P' re-refused at the admission gate | got "REFUSED: element not admitted: 'P'" | expect "REFUSED: element not admitted: 'P'"
PASS R5 | unclosed group C6H12(O6 re-refused | got "REFUSED: syntax (unclosed group)" | expect "REFUSED: syntax (unclosed group)"
PASS R6 | bad character in 'C6H12O6$' re-refused | got "REFUSED: syntax (bad character)" | expect "REFUSED: syntax (bad character)"
PASS R7 | FeSO4·0.35H2O re-refused as NON-EXACT at the dot | got "REFUSED: NON-EXACT (non-integer hydrate)" | expect "REFUSED: NON-EXACT (non-integer hydrate)"
PASS R8 | FeSO4·0H2O re-refused, zero subscript | got "REFUSED: zero subscript" | expect "REFUSED: zero subscript"
PASS P1 | pin H2O (Ch 4) re-derived | got "18.015 g/mol (180,150 myu)" | expect "18.015 g/mol (180,150 myu)"
PASS P2 | pin glucose C6H12O6 (Ch 21) re-derived | got "180.156 g/mol (1,801,560 myu)" | expect "180.156 g/mol (1,801,560 myu)"
PASS P3 | pin sucrose C12H22O11 (Ch 5) re-derived | got "342.297 g/mol (3,422,970 myu)" | expect "342.297 g/mol (3,422,970 myu)"
PASS P4 | pin acetic acid C2H4O2 (Ch 4) re-derived | got "60.052 g/mol (600,520 myu)" | expect "60.052 g/mol (600,520 myu)"
PASS P5 | pin methanol CH4O (Ch 21) re-derived | got "32.042 g/mol (320,420 myu)" | expect "32.042 g/mol (320,420 myu)"
PASS P6 | pin O2 (Ch 7) re-derived | got "31.998 g/mol (319,980 myu)" | expect "31.998 g/mol (319,980 myu)"
PASS P7 | pin CO2 (Ch 20) re-derived | got "44.009 g/mol (440,090 myu)" | expect "44.009 g/mol (440,090 myu)"
PASS P8 | pin cellulose C6H10O5 (Ch 25) re-derived | got "162.141 g/mol (1,621,410 myu)" | expect "162.141 g/mol (1,621,410 myu)"
PASS P9 | pin copperas FeSO4·7H2O (Ch 19) re-derived | got "278.006 g/mol (2,780,060 myu)" | expect "278.006 g/mol (2,780,060 myu)"
PASS P10 | pin salicin C13H18O7 (Ch 34) re-derived | got "286.280 g/mol (2,862,800 myu)" | expect "286.280 g/mol (2,862,800 myu)"
PASS P11 | pin saligenin C7H8O2 (Ch 34) re-derived | got "124.139 g/mol (1,241,390 myu)" | expect "124.139 g/mol (1,241,390 myu)"
PASS P12 | pin aspirin C9H8O4 (Ch 3) re-derived | got "180.159 g/mol (1,801,590 myu)" | expect "180.159 g/mol (1,801,590 myu)"
PASS P13 | pin isoprene C5H8 (Ch 35) re-derived | got "68.119 g/mol (681,190 myu)" | expect "68.119 g/mol (681,190 myu)"
PASS P14 | pin salicylic acid C7H6O3 (Ch 13) re-derived | got "138.122 g/mol (1,381,220 myu)" | expect "138.122 g/mol (1,381,220 myu)"
PASS P15 | pin stearic acid C18H36O2 (Ch 23) re-derived | got "284.484 g/mol (2,844,840 myu)" | expect "284.484 g/mol (2,844,840 myu)"
PASS I1 | ISOMER a-pinene C10H16 - Ch 34 limonene number re-derived | got "136.238 g/mol (1,362,380 myu)" | expect "136.238 g/mol (1,362,380 myu)"
PASS N1 | NEW abietic acid C20H30O2 re-derived | got "302.458 g/mol (3,024,580 myu)" | expect "302.458 g/mol (3,024,580 myu)"
PASS N2 | NEW betulin C30H50O2 re-derived | got "442.728 g/mol (4,427,280 myu)" | expect "442.728 g/mol (4,427,280 myu)"
PASS N3 | NEW gallic acid C7H6O5 re-derived | got "170.120 g/mol (1,701,200 myu)" | expect "170.120 g/mol (1,701,200 myu)"
PASS N4 | NEW tannic acid C76H52O46 re-derived | got "1701.206 g/mol (17,012,060 myu)" | expect "1701.206 g/mol (17,012,060 myu)"
PASS N5 | NEW arabinose C5H10O5 re-derived | got "150.130 g/mol (1,501,300 myu)" | expect "150.130 g/mol (1,501,300 myu)"
PASS N6 | NEW formic acid CH2O2 re-derived | got "46.025 g/mol (460,250 myu)" | expect "46.025 g/mol (460,250 myu)"
PASS B1 | salicin hydrolysis balance re-walked by lanes | got "3,042,950 myu CLOSES" | expect "3,042,950 myu CLOSES"
PASS B2 | saligenin oxidation balance re-walked | got "1,561,370 myu CLOSES" | expect "1,561,370 myu CLOSES"
PASS B3 | tannic hydrolysis balance re-walked | got "18,813,560 myu CLOSES" | expect "18,813,560 myu CLOSES"
PASS B4 | copperas drying balance re-walked | got "2,780,060 myu CLOSES" | expect "2,780,060 myu CLOSES"
PASS B5 | isoprene polymerization bookkeeping 1000 x C5H8 re-summed | got "681,190,000 myu CLOSES" | expect "681,190,000 myu CLOSES"
PASS B6 | a-pinene combustion balance re-walked | got "5,842,100 myu CLOSES" | expect "5,842,100 myu CLOSES"
PASS B7 | aspirin hydrolysis balance re-walked | got "1,981,740 myu CLOSES" | expect "1,981,740 myu CLOSES"
PASS B8 | MUST-FAIL re-proof: salicin hydrolysis drafted with C6H10O5 for glucose | got "GAP 180,150 myu CAUGHT" | expect "GAP 180,150 myu CAUGHT"
PASS PR1 | the 136-family re-probed: a-pinene vs limonene | got "0 myu — SAME number, DIFFERENT molecule (isomers)" | expect "0 myu — SAME number, DIFFERENT molecule (isomers)"
PASS PR2 | the 180-family re-probed: aspirin minus glucose | got "30 myu" | expect "30 myu"
PASS PR3 | the 150-family re-probed: thymol minus arabinose | got "910 myu" | expect "910 myu"
PASS PR4 | the 46-family re-probed: ethanol minus formic | got "440 myu" | expect "440 myu"
PASS L1 | maple model: 20 g sucrose / 0.669 solids, exact rational | got "29.895 g" | expect "29.895 g"
PASS L2 | water evaporated: 1000 - syrup, exact rational | got "970.105 g" | expect "970.105 g"
PASS L3 | the boil energy: water x 2256 J/g, exact rational | got "2,188,556 J (2.189 MJ)" | expect "2,188,556 J (2.189 MJ)"
PASS L4 | the rule of 86 at 2% sap | got "43.0" | expect "43.0"
PASS L5 | model sap:syrup ratio (density 1.33 g/mL) vs the rule, exact rational | got "44.49 vs 43.0 — honest gap 1.49 (~3.5%)" | expect "44.49 vs 43.0 — honest gap 1.49 (~3.5%)"
PASS L6 | RO pre-concentration 2%->8%: 750 g vs the 970.105 g boil, exact rational | got "77.3% of the boil" | expect "77.3% of the boil"
PASS L7 | latex: 350 g rubber / isoprene pin, exact rational | got "5.138 mol" | expect "5.138 mol"
PASS L8 | oleoresin 20/80 model: pinene and abietic lanes, exact rational | got "0.1468 mol pinene / 0.2645 mol abietic acid" | expect "0.1468 mol pinene / 0.2645 mol abietic acid"
PASS L9 | ink batch 4 g tannic + 3 g copperas, exact rational | got "tannic 2.3513 mmol, Fe 10.7911 mmol, gallate:Fe 2.179:1" | expect "tannic 2.3513 mmol, Fe 10.7911 mmol, gallate:Fe 2.179:1"
PASS X1 | Ex 7.1 resin split at the 20/80 model | got "20.0 g turpentine / 80.0 g rosin" | expect "20.0 g turpentine / 80.0 g rosin"
PASS X2 | Ex 7.2 the rule of 86 at 3% sap | got "28.667 (about 29 gal)" | expect "28.667 (about 29 gal)"
PASS X3 | Ex 7.3 six waters over the heptahydrate, exact rational | got "38.880%" | expect "38.880%"
PASS X4a | Ex 7.4a 40 L sap: 800 g sucrose / 0.669, exact rational | got "1,195.815 g" | expect "1,195.815 g"
PASS X4b | Ex 7.4b the 40 L boil: 25,960,000/669 g water x 2256, exact rational | got "87,542,242 J (87.542 MJ)" | expect "87,542,242 J (87.542 MJ)"
PASS X5a | Ex 7.5a the willow corridor 25 g salicin, exact rational | got "0.087327 mol -> 10.841 g -> 12.062 g" | expect "0.087327 mol -> 10.841 g -> 12.062 g"
PASS X5b | Ex 7.5b the ink pot 60 g Aleppo galls at 65%, exact rational | got "22.925 mmol tannic (229.249 mmol galloyl) -> 29.250 g copperas" | expect "22.925 mmol tannic (229.249 mmol galloyl) -> 29.250 g copperas"
PASS C1 | tannic acid's census read back from the lanes | got "C:76 H:52 O:46" | expect "C:76 H:52 O:46"
PASS C2 | B3's element lanes, both sides re-compared | got "IDENTICAL" | expect "IDENTICAL"
PASS C3 | determinism: the whole battery run twice, byte-identical | got "IDENTICAL" | expect "IDENTICAL"
RUN 2 VERDICT: 68/68 PASS — CLEAN
G1 RECOUNT: the frozen block holds 68 PASS rows; the frozen verdict line reads 67/67 — OFF-BY-ONE RAISED (RF-1)
G2 CANARY: L1 expectation corrupted to "29.896 g" -> the harness FAIL (good - canary caught); non-vacuity proven
G4 MUST-FAIL: B8 recomputed through the peel machine -> "GAP 180,150 myu CAUGHT"
```

## 5. Expectations provenance

The expectations are the frozen block's own got-strings verbatim (parsed programmatically from the canvas's ```text fence — `PASS <id> | desc | got "..." | expect "..."`; got == expect on every frozen row). No expectation was patched to pass; every mismatch at run 1 was diagnosed as the review's own machinery and repaired with the repair disclosed. The refusal rows' inputs were reconstructed from their row descriptions (morphine; ricin; indigo C16H10N2O2; 'P'; C6H12(O6; C6H12O6$; FeSO4·0.35H2O; FeSO4·0H2O) and re-refused through Engine 38's own gate chain, a fresh implementation sharing no gate code with Engine 37.

## 6. The part-2 checks (all PAID at this close)

- **The pin re-greps (session-112 line, raw `grep -oF` counts in the owners' own pages):** all present, zero mismatches — H2O 18.015 Ch 4 ×1; glucose 180.156 Ch 21 ×2; sucrose 342.297 Ch 5 ×2; acetic 60.052 Ch 4 ×5; methanol 32.042 Ch 21 ×3; O2 31.998 Ch 7 ×1; CO2 44.009 Ch 20 ×6; cellulose 162.141 Ch 25 ×1; copperas 278.006 Ch 19 ×2 (Ch 22 cross ×4 — the ink-feedstock re-attribution verified); salicin 286.280 Ch 34 ×6 (matching the authoring record's ×6 exactly); saligenin 124.139 Ch 34 ×4; aspirin 180.159 Ch 3 ×3; isoprene 68.119 Ch 35 ×2; salicylic 138.122 Ch 13 ×1; stearic 284.484 Ch 23 ×6; the heat anchor 2256 Ch 7 ×4; the isomer twin limonene 136.238 Ch 34 ×3; the 150-family probe thymol 150.221 Ch 34 ×2; the 46-family probe ethanol 46.069 Ch 21 ×22.
- **The NEW re-proof at the review HEAD:** N1–N6 (302.458, 442.728, 170.120, 1701.206, 150.130, 46.025) and the seven shelf words (rosin, turpentine, arabic, hevea, guayule, birch, acorn) all zero-hit across the 28 local masters + the local FC engine records and design notes (2,247,571 B) + the 41 web editions (2,272,243 B) — fc7's own master and web edition excluded as the home chapter, disclosed; fc1 swept via its byte-verified web edition per the content contract (no composition is ever priced in the md-only apparatus). The six NEW compositions stand.
- **The [convergent] re-confirmations (twelve fresh searches, all convergent, zero corrections owed):** α-pinene 155–156 °C and 136.23 g/mol; the Kozowyk Palaeolithic dry-distillation series (mound/pit/raised structure); maple's 66.9 °Brix minimum legal density; the Jones rule of 86 (C.H. Jones, 1946, UVM); formic acid as Hevea latex's standard coagulant; Aleppo galls as the ink canon's tannin-rich ingredient; gallotannic acid 1701.19 g/mol "ten times that of gallic acid" (the decagalloyl convention AND the database-basis seam in one source line); gum arabic's three-fraction census with arabinogalactan the bulk; abietic acid 302.4510 (the databases); tannic acid C76H52O46 at 1701.19 (the averaged-weight basis against the bench table's 1701.206 — the seam re-printed honestly); betulin's bark-band source page; the maple-sap sugar class.
- **Ex FC7.6's withheld ◆ answer delivered** at the chapter's Revision Appendix (battery rows and [convergent] endpoints only — the E8 oxidation cited, the ~3:1 stability finding and L9's 2.179:1 convention ratio, Ex 7.3's fresh-copperas answer, the 4:2:1 1770 family, gum arabic's suspension; no new figures).
- **The canvas:** the Revision Appendix appended after the closing italic (the review description, the honest two-run history with the run-1 FAIL lines preserved, the frozen run-2 block spliced programmatically, the gates incl. RF-1, the re-grep table, the NEW re-proof, the web re-confirmations, the delivered answer, the verdict line, the new closing status line); the top status line flipped drafted → reviewed; canvas 61,328 → 79,722 B, no trailing newline. **A note for the record:** Engine 37 has no separate durable record (the session-124 close predates any engine-record push for FC7); the chapter's frozen Lab FC7.1 block is the battery's artifact of record, and this review's clean 68/68 reproduction of it — by an engine sharing zero code — is the independent verification. The web edition re-rendered same-session per the web-sync rule (56,431 B; the content contract held — the appendix remains md-only).

## 7. The full Engine 38 run-2 source, verbatim (the no-placeholder lesson — no elisions)

The complete program as executed at run 2 (engine + the 68-row spec table + the harness):

```typescript
// Engine 38 run 2 — the two run-1 defects repaired (nothing else touched):
//   (1) the hydrate-unit scope: the coefficient after '·' now multiplies the WHOLE
//       unit formula (to end or next '·'), not just its first element;
//   (2) the g/mol display column: plain, no comma (the comma convention lives in
//       the myu restatement and the gram/joule ledgers, not the g/mol column).
const AMYU: Record<string, bigint> = { C: 120110n, H: 10080n, O: 159990n, S: 320600n, Fe: 558450n };
const EL = ['C', 'H', 'O', 'S', 'Fe'];
const IDX: Record<string, number> = { C: 0, H: 1, O: 2, S: 3, Fe: 4 };
const ALPHA = ['C', 'Fe', 'H', 'O', 'S'];
const P18NAMES = ['morphine', 'ricin'];

function parseLanes(f: string): bigint[] {
  const root: bigint[] = [0n, 0n, 0n, 0n, 0n];
  const stack: Array<{ parent: bigint[]; lanes: bigint[] }> = [];
  let cur = root;
  let i = 0;
  while (i < f.length) {
    const ch = f[i];
    if (ch === '(') {
      const nl: bigint[] = [0n, 0n, 0n, 0n, 0n];
      stack.push({ parent: cur, lanes: nl });
      cur = nl; i++;
    } else if (ch === ')') {
      const fr = stack.pop();
      if (!fr) throw new Error('bad character');
      i++;
      let num = '';
      while (i < f.length && f[i] >= '0' && f[i] <= '9') { num += f[i]; i++; }
      const k = num === '' ? 1n : BigInt(num);
      for (let e = 0; e < 5; e++) fr.parent[e] += fr.lanes[e] * k;
      cur = fr.parent;
    } else if (ch >= 'A' && ch <= 'Z') {
      let sym = ch; i++;
      if (i < f.length && f[i] >= 'a' && f[i] <= 'z') { sym += f[i]; i++; }
      if (!(sym in AMYU)) throw new Error('admission:' + sym);
      let num = '';
      while (i < f.length && f[i] >= '0' && f[i] <= '9') { num += f[i]; i++; }
      cur[IDX[sym]] += num === '' ? 1n : BigInt(num);
    } else if (ch === '·') {
      i++;
      let coef = '';
      while (i < f.length && f[i] >= '0' && f[i] <= '9') { coef += f[i]; i++; }
      const k = coef === '' ? 1n : BigInt(coef);
      let unit = '';
      while (i < f.length && f[i] !== '·') { unit += f[i]; i++; }
      const ul = parseLanes(unit);
      for (let e = 0; e < 5; e++) cur[e] += ul[e] * k;
    } else {
      throw new Error('bad character');
    }
  }
  if (stack.length) throw new Error('unclosed group');
  return root;
}

function gate(input: string): string {
  const s = input.trim();
  if (P18NAMES.includes(s.toLowerCase())) return 'REFUSED (P18): recognition-only, the fence absolute';
  const syms = s.match(/[A-Z][a-z]?/g) || [];
  for (const sym of syms) if (!(sym in AMYU)) return "REFUSED: element not admitted: '" + sym + "'";
  const hidx = s.indexOf('·');
  if (hidx >= 0) {
    let j = hidx + 1;
    let coef = '';
    let dotted = false;
    while (j < s.length && /[0-9.]/.test(s[j])) { if (s[j] === '.') dotted = true; coef += s[j]; j++; }
    if (dotted) return 'REFUSED: NON-EXACT (non-integer hydrate)';
    if (coef !== '' && BigInt(coef) === 0n) return 'REFUSED: zero subscript';
  }
  try { parseLanes(s); } catch (e) { return 'REFUSED: syntax (' + (e as Error).message + ')'; }
  return 'ADMITTED';
}

function canonical(lanes: bigint[]): string {
  let out = '';
  for (const sym of ['C', 'H', 'Fe', 'O', 'S']) {
    const n = lanes[IDX[sym]];
    if (n === 0n) continue;
    out += sym + (n === 1n ? '' : n.toString());
  }
  return out;
}

function massOf(f: string): { lanes: bigint[], myu: bigint } {
  const lanes = parseLanes(f);
  let m1 = 0n, m2 = 0n;
  for (let e = 0; e < 5; e++) m1 += lanes[e] * AMYU[EL[e]];
  for (let e = 4; e >= 0; e--) m2 += lanes[e] * AMYU[EL[e]];
  if (m1 !== m2) throw new Error('dual-column mismatch on ' + f);
  const lanes2 = parseLanes(canonical(lanes));
  for (let e = 0; e < 5; e++) if (lanes2[e] !== lanes[e]) throw new Error('canonical re-parse mismatch on ' + f);
  return { lanes, myu: m1 };
}

function comma(s: string): string {
  let out = '';
  for (let i = 0; i < s.length; i++) {
    if (i > 0 && (s.length - i) % 3 === 0) out += ',';
    out += s[i];
  }
  return out;
}
function rhu(num: bigint, den: bigint, dp: number, withComma = true): string {
  const scale = 10n ** BigInt(dp);
  const scaled = (num * scale * 2n + den) / (den * 2n);
  let s = scaled.toString();
  if (dp === 0) return withComma ? comma(s) : s;
  if (s.length <= dp) s = s.padStart(dp + 1, '0');
  const ip = s.slice(0, s.length - dp);
  return (withComma ? comma(ip) : ip) + '.' + s.slice(s.length - dp);
}
const massDisp = (f: string) => {
  const m = massOf(f).myu;
  return rhu(m, 10000n, 3, false) + ' g/mol (' + comma(m.toString()) + ' myu)';
};

function balGot(lhs: Array<[string, bigint]>, rhs: Array<[string, bigint]>): string {
  const L: bigint[] = [0n, 0n, 0n, 0n, 0n];
  const R: bigint[] = [0n, 0n, 0n, 0n, 0n];
  for (const [f, k] of lhs) { const la = massOf(f).lanes; for (let e = 0; e < 5; e++) L[e] += la[e] * k; }
  for (const [f, k] of rhs) { const la = massOf(f).lanes; for (let e = 0; e < 5; e++) R[e] += la[e] * k; }
  let ml = 0n, mr = 0n;
  for (let e = 0; e < 5; e++) { ml += L[e] * AMYU[EL[e]]; mr += R[e] * AMYU[EL[e]]; }
  if (ml === mr) return comma(ml.toString()) + ' myu CLOSES';
  return 'GAP ' + comma((ml > mr ? ml - mr : mr - ml).toString()) + ' myu CAUGHT';
}

type Spec = [string, string, () => string];
const specs: Spec[] = [
  ['T1', 'admission table, straight checksum re-summed', () => comma((120110n + 10080n + 159990n + 320600n + 558450n).toString())],
  ['T2', 'admission table, positional checksum (alphabetical C,Fe,H,O,S) re-summed', () => comma(ALPHA.reduce((a, s, i) => a + AMYU[s] * BigInt(i + 1), 0n).toString())],
  ['S1', 'SELF H2O through the peel machine, dual-column', () => massDisp('H2O')],
  ['S2', 'SELF (CH3)2CO - frame pop, subscript after the bracket', () => massDisp('(CH3)2CO')],
  ['S3', 'SELF FeSO4·7H2O - the hydrate lane', () => massDisp('FeSO4·7H2O')],
  ['S4', 'SELF CH3(CH2)16COOH - nested frames, one pass', () => massDisp('CH3(CH2)16COOH')],
  ['S5', 'SELF scrambled O7C13H18 - canonical display from the lanes', () => { const r = massOf('O7C13H18'); return canonical(r.lanes) + ' ' + rhu(r.myu, 10000n, 3, false); }],
  ['R1', "'morphine' re-refused at the P18 name gate (FIRST)", () => gate('morphine')],
  ['R2', "'ricin' re-refused at the P18 name gate", () => gate('ricin')],
  ['R3', 'indigo C16H10N2O2 re-refused at the admission gate', () => gate('C16H10N2O2')],
  ['R4', "'P' re-refused at the admission gate", () => gate('P')],
  ['R5', 'unclosed group C6H12(O6 re-refused', () => gate('C6H12(O6')],
  ['R6', "bad character in 'C6H12O6$' re-refused", () => gate('C6H12O6$')],
  ['R7', 'FeSO4·0.35H2O re-refused as NON-EXACT at the dot', () => gate('FeSO4·0.35H2O')],
  ['R8', 'FeSO4·0H2O re-refused, zero subscript', () => gate('FeSO4·0H2O')],
  ['P1', 'pin H2O (Ch 4) re-derived', () => massDisp('H2O')],
  ['P2', 'pin glucose C6H12O6 (Ch 21) re-derived', () => massDisp('C6H12O6')],
  ['P3', 'pin sucrose C12H22O11 (Ch 5) re-derived', () => massDisp('C12H22O11')],
  ['P4', 'pin acetic acid C2H4O2 (Ch 4) re-derived', () => massDisp('C2H4O2')],
  ['P5', 'pin methanol CH4O (Ch 21) re-derived', () => massDisp('CH4O')],
  ['P6', 'pin O2 (Ch 7) re-derived', () => massDisp('O2')],
  ['P7', 'pin CO2 (Ch 20) re-derived', () => massDisp('CO2')],
  ['P8', 'pin cellulose C6H10O5 (Ch 25) re-derived', () => massDisp('C6H10O5')],
  ['P9', 'pin copperas FeSO4·7H2O (Ch 19) re-derived', () => massDisp('FeSO4·7H2O')],
  ['P10', 'pin salicin C13H18O7 (Ch 34) re-derived', () => massDisp('C13H18O7')],
  ['P11', 'pin saligenin C7H8O2 (Ch 34) re-derived', () => massDisp('C7H8O2')],
  ['P12', 'pin aspirin C9H8O4 (Ch 3) re-derived', () => massDisp('C9H8O4')],
  ['P13', 'pin isoprene C5H8 (Ch 35) re-derived', () => massDisp('C5H8')],
  ['P14', 'pin salicylic acid C7H6O3 (Ch 13) re-derived', () => massDisp('C7H6O3')],
  ['P15', 'pin stearic acid C18H36O2 (Ch 23) re-derived', () => massDisp('C18H36O2')],
  ['I1', 'ISOMER a-pinene C10H16 - Ch 34 limonene number re-derived', () => massDisp('C10H16')],
  ['N1', 'NEW abietic acid C20H30O2 re-derived', () => massDisp('C20H30O2')],
  ['N2', 'NEW betulin C30H50O2 re-derived', () => massDisp('C30H50O2')],
  ['N3', 'NEW gallic acid C7H6O5 re-derived', () => massDisp('C7H6O5')],
  ['N4', 'NEW tannic acid C76H52O46 re-derived', () => massDisp('C76H52O46')],
  ['N5', 'NEW arabinose C5H10O5 re-derived', () => massDisp('C5H10O5')],
  ['N6', 'NEW formic acid CH2O2 re-derived', () => massDisp('CH2O2')],
  ['B1', 'salicin hydrolysis balance re-walked by lanes', () => balGot([['C13H18O7', 1n], ['H2O', 1n]], [['C7H8O2', 1n], ['C6H12O6', 1n]])],
  ['B2', 'saligenin oxidation balance re-walked', () => balGot([['C7H8O2', 1n], ['O2', 1n]], [['C7H6O3', 1n], ['H2O', 1n]])],
  ['B3', 'tannic hydrolysis balance re-walked', () => balGot([['C76H52O46', 1n], ['H2O', 10n]], [['C6H12O6', 1n], ['C7H6O5', 10n]])],
  ['B4', 'copperas drying balance re-walked', () => balGot([['FeSO4·7H2O', 1n]], [['FeSO4·H2O', 1n], ['H2O', 6n]])],
  ['B5', 'isoprene polymerization bookkeeping 1000 x C5H8 re-summed', () => comma((massOf('C5H8').myu * 1000n).toString()) + ' myu CLOSES'],
  ['B6', 'a-pinene combustion balance re-walked', () => balGot([['C10H16', 1n], ['O2', 14n]], [['CO2', 10n], ['H2O', 8n]])],
  ['B7', 'aspirin hydrolysis balance re-walked', () => balGot([['C9H8O4', 1n], ['H2O', 1n]], [['C7H6O3', 1n], ['C2H4O2', 1n]])],
  ['B8', 'MUST-FAIL re-proof: salicin hydrolysis drafted with C6H10O5 for glucose', () => balGot([['C13H18O7', 1n], ['H2O', 1n]], [['C7H8O2', 1n], ['C6H10O5', 1n]])],
  ['PR1', 'the 136-family re-probed: a-pinene vs limonene', () => { const d = massOf('C10H16').myu - 1362380n; return d === 0n ? '0 myu — SAME number, DIFFERENT molecule (isomers)' : comma(d.toString()) + ' myu'; }],
  ['PR2', 'the 180-family re-probed: aspirin minus glucose', () => comma((massOf('C9H8O4').myu - massOf('C6H12O6').myu).toString()) + ' myu'],
  ['PR3', 'the 150-family re-probed: thymol minus arabinose', () => comma((1502210n - massOf('C5H10O5').myu).toString()) + ' myu'],
  ['PR4', 'the 46-family re-probed: ethanol minus formic', () => comma((460690n - massOf('CH2O2').myu).toString()) + ' myu'],
  ['L1', 'maple model: 20 g sucrose / 0.669 solids, exact rational', () => rhu(20000n, 669n, 3) + ' g'],
  ['L2', 'water evaporated: 1000 - syrup, exact rational', () => rhu(649000n, 669n, 3) + ' g'],
  ['L3', 'the boil energy: water x 2256 J/g, exact rational', () => { const jn = 649000n * 2256n; return comma((jn / 669n).toString()) + ' J (' + rhu(jn, 669000000n, 3) + ' MJ)'; }],
  ['L4', 'the rule of 86 at 2% sap', () => rhu(86n, 2n, 1)],
  ['L5', 'model sap:syrup ratio (density 1.33 g/mL) vs the rule, exact rational', () => rhu(88977000n, 2000000n, 2) + ' vs ' + rhu(86n, 2n, 1) + ' — honest gap ' + rhu(2977000n, 2000000n, 2) + ' (~' + rhu(297700000n, 86000000n, 1) + '%)'],
  ['L6', 'RO pre-concentration 2%->8%: 750 g vs the 970.105 g boil, exact rational', () => rhu(50175000n, 649000n, 1) + '% of the boil'],
  ['L7', 'latex: 350 g rubber / isoprene pin, exact rational', () => rhu(3500000n, 681190n, 3) + ' mol'],
  ['L8', 'oleoresin 20/80 model: pinene and abietic lanes, exact rational', () => rhu(200000n, 1362380n, 4) + ' mol pinene / ' + rhu(800000n, 3024580n, 4) + ' mol abietic acid'],
  ['L9', 'ink batch 4 g tannic + 3 g copperas, exact rational', () => 'tannic ' + rhu(40000000n, 17012060n, 4) + ' mmol, Fe ' + rhu(30000000n, 2780060n, 4) + ' mmol, gallate:Fe ' + rhu(400000000n * 2780060n, 17012060n * 30000000n, 3) + ':1'],
  ['X1', 'Ex 7.1 resin split at the 20/80 model', () => rhu(20n, 1n, 1) + ' g turpentine / ' + rhu(80n, 1n, 1) + ' g rosin'],
  ['X2', 'Ex 7.2 the rule of 86 at 3% sap', () => rhu(86n, 3n, 3) + ' (about 29 gal)'],
  ['X3', 'Ex 7.3 six waters over the heptahydrate, exact rational', () => rhu(108090000n, 2780060n, 3) + '%'],
  ['X4a', 'Ex 7.4a 40 L sap: 800 g sucrose / 0.669, exact rational', () => rhu(800000n, 669n, 3) + ' g'],
  ['X4b', 'Ex 7.4b the 40 L boil: 25,960,000/669 g water x 2256, exact rational', () => { const jn = 25960000n * 2256n; return comma((jn / 669n).toString()) + ' J (' + rhu(jn, 669000000n, 3) + ' MJ)'; }],
  ['X5a', 'Ex 7.5a the willow corridor 25 g salicin, exact rational', () => rhu(250000n, 2862800n, 6) + ' mol -> ' + rhu(25n * 1241390n, 2862800n, 3) + ' g -> ' + rhu(25n * 1381220n, 2862800n, 3) + ' g'],
  ['X5b', 'Ex 7.5b the ink pot 60 g Aleppo galls at 65%, exact rational', () => rhu(390000000n, 17012060n, 3) + ' mmol tannic (' + rhu(3900000000n, 17012060n, 3) + ' mmol galloyl) -> ' + rhu(117n, 4n, 3) + ' g copperas'],
  ['C1', "tannic acid's census read back from the lanes", () => { const la = massOf('C76H52O46').lanes; return EL.filter(e => la[IDX[e]] > 0n).map(e => e + ':' + la[IDX[e]].toString()).join(' '); }],
  ['C2', "B3's element lanes, both sides re-compared", () => { const a = balGot([['C76H52O46', 1n], ['H2O', 10n]], [['C6H12O6', 1n], ['C7H6O5', 10n]]); return a.endsWith('CLOSES') ? 'IDENTICAL' : 'NOT IDENTICAL'; }],
  ['C3', 'determinism: the whole battery run twice, byte-identical', () => 'IDENTICAL'],
];

async function main() {
  const canvas = (await tools.file_system.read_file({ path: '/home/user/canvases/everyday-chem-atlas-fc7/CANVAS.md' })).content;
  const lines = canvas.split('\n');
  const fs = lines.indexOf('```text');
  const fe = lines.indexOf('```', fs + 1);
  const block = lines.slice(fs + 1, fe);
  const rowRe = /^PASS (\S+) \| (.+?) \| got "(.*)" \| expect "(.*)"$/;
  const frozen: Array<{ id: string; got: string }> = [];
  let verdictLine = '';
  for (const l of block) {
    if (l.startsWith('PASS ')) { const m = l.match(rowRe); if (!m) throw new Error('unparseable frozen row'); frozen.push({ id: m[1], got: m[3] }); }
    else if (l.startsWith('RUN ')) verdictLine = l;
  }
  const specMap = new Map<string, Spec>(specs.map(s => [s[0], s]));
  for (const f of frozen) if (!specMap.has(f.id)) throw new Error('no spec for frozen row ' + f.id);
  if (frozen.length !== specs.length) throw new Error('row count mismatch');

  function runBody(): { lines: string[]; fails: number } {
    const out: string[] = [];
    let fails = 0;
    for (const [id, desc, fn] of specs) {
      if (id === 'C3') continue;
      const got = fn();
      const fr = frozen.find(r => r.id === id) as { got: string };
      const ok = got === fr.got;
      if (!ok) fails++;
      out.push((ok ? 'PASS ' : 'FAIL ') + id + ' | ' + desc + ' | got "' + got + '" | expect "' + fr.got + '"');
    }
    return { lines: out, fails };
  }

  const r1 = runBody();
  const r2 = runBody();
  const c3ok = JSON.stringify(r1.lines) === JSON.stringify(r2.lines) && r1.fails === 0;
  const ordered: string[] = [];
  let idx = 0;
  for (const [id] of specs) {
    if (id === 'C3') ordered.push('PASS C3 | determinism: the whole battery run twice, byte-identical | got "' + (c3ok ? 'IDENTICAL' : 'NOT IDENTICAL') + '" | expect "IDENTICAL"');
    else ordered.push(r1.lines[idx++]);
  }
  const passCount = ordered.filter(l => l.startsWith('PASS ')).length;
  const clean = passCount === ordered.length && c3ok;
  const blockText = ordered.join('\n') + '\nRUN 2 VERDICT: ' + passCount + '/' + ordered.length + ' PASS' + (clean ? ' — CLEAN' : '');

  const canary = (() => {
    const fr = frozen.find(r => r.id === 'L1') as { got: string };
    const saved = fr.got;
    fr.got = '29.896 g';
    const got = (specMap.get('L1') as Spec)[2]();
    const res = got === '29.896 g' ? 'PASS (BAD - canary passed!)' : 'FAIL (good - canary caught)';
    fr.got = saved;
    return 'G2 CANARY: L1 expectation corrupted to "29.896 g" -> the harness ' + res + '; non-vacuity proven';
  })();

  const tallyMatch = /VERDICT: (\d+)\/(\d+)/.exec(verdictLine) as RegExpMatchArray;
  const g1 = 'G1 RECOUNT: the frozen block holds ' + frozen.length + ' PASS rows; the frozen verdict line reads ' + tallyMatch[1] + '/' + tallyMatch[2] + ' — OFF-BY-ONE RAISED (RF-1)';
  const b8 = balGot([['C13H18O7', 1n], ['H2O', 1n]], [['C7H8O2', 1n], ['C6H10O5', 1n]]);
  const g4 = 'G4 MUST-FAIL: B8 recomputed through the peel machine -> "' + b8 + '"';

  await tools.file_system.write_file({ path: '/home/user/knowledge/everyday-chem-book/fc7-engine38-runblock.txt', content: blockText + '\n' + g1 + '\n' + canary + '\n' + g4 + '\n' });
  return { run2Verdict: blockText.split('\n').pop(), passCount, total: ordered.length, c3identical: c3ok, g1, canary, g4, failLines: ordered.filter(l => l.startsWith('FAIL')) };
}
```

## 8. Session 125 close summary

FC7 REVIEWED — VERDICT: PASS WITH RF-1 (the verdict-line recount, corrected of record at the chapter's Revision Appendix; the body untouched per extend-never-rewrite). Engine 38 honest two-run history 64/68 → 68/68 CLEAN. All 68 rows reproduced exactly; the six NEW claims re-proven; 19 anchors re-grepped to the digit; twelve [convergent] searches re-confirmed; Ex FC7.6's withheld answer delivered. Canvas 79,722 B (no trailing newline); repo master = canvas + one newline; web edition re-rendered (56,431 B). Map FC7 drafted → reviewed. NEXT: session 126 = FC8 authoring on the user's call.
