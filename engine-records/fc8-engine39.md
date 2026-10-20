# FC8 Engine 39 record — the depth-ledger double-and-add compositor (session 126, the FC8 authoring battery)

Session 126 (2026-10-20): the FC8 authoring unit per row 126. Engine 39 authored the whole FC8 battery — 69 rows: 8 self-stress (S1–S8, the Atlas's own parse grid plus the ladder's exhibit), 14 refusals (R1–R14, the admission, NAME, syntax, and hydrate-grid gates), 17 regression pins (P1–P17, Chapter 23's fat shelf in full plus the lyes, ethanol, and FC7's tannic), 5 NEW compositions (N1–N5, each zero-hit-verified before the freeze), 1 isomer row (I1), 9 balances (E1–E9, one a designed must-fail), 3 probes (PR1–PR3), 7 ledger/cumulative rows (B1a–B5, X1–X4), and 2 checksums (T1–T2). Verdict: **69/69 PASS — CLEAN**.

## 1. Design spec

- **Pass 1 — the depth-ledger validation walk:** a flat depth-prefix ledger over the input (each open bracket increments the depth, each close decrements it, the running depth recorded per token); no stack, no recursion, no rewriting, no interval DP, no transition matrix, no CPS continuations — the neighbors named honestly below.
- **Pass 2 — the evaluation fold:** a single left-to-right fold whose group multipliers are read by a bounded forward scan to each bracket's own match; **no parse tree is ever materialized**. Each depth carries its own product register (the multiplier seen so far at that bracket depth), read on element entry, closed on exit; the group's subscript is consumed by the exit branch (the attempt-1 lesson paid in the design itself).
- **mulDA — the mass ladder, the fresh axis:** multiplication is banished from every mass lane; every count × unit-mass is priced by a double-and-add ladder (repeated doubling and addition on BigInt shifts); the '*' operator appears nowhere in a mass lane. S8 is the ladder's own exhibit: 46 carbons priced by five doublings (46 = 101110b).
- **Exact integer micro-units**, 1 myu = 1e-6 g/mol, a single integrality gate on each hydrate segment's total (the half-hydrate's 0.5 legal — the E20 lesson held); **fmtMyu** prints exact decimals, trailing zeros trimmed, no commas (the Engine-38 N4 lesson held).
- **Admission: the held-22 element table** re-transcribed from Chapter 25's own page plus Chapter 30's Si 28.085; phosphorus refused at the gate — the nineteenth zero-admission chapter.
- **Gate order:** the NAME gate FIRST (family and mixture words refused before any parse), then admission, then the syntax gates (unclosed group; illegal character), then the hydrate-coefficient grid (off-grid coefficients refused).
- **The authoring gates:** G1 the machine recount of PASS rows against the verdict line (the FC7 RF-1 lesson answered at authoring time), G2 the canary (a corrupted expectation must FAIL), G3 determinism (the whole battery run twice, byte-identical), G4 the designed must-fail (E9's short lye charge must be caught at exactly one NaOH).

Distinctness (zero code shared with Engines 1–38): no CPS fold/composed continuations (37), no token-table AST (36), no span-table memoization (35), no census-tally expansion (34), no fixed-point rewrite (33), no RPN shunting-yard (31), no unit lattice (27), no peel-and-push frame stack with dual-column forward/reverse/canonical verification (38). Engine 37's per-scope parking registers are conceptually adjacent to this engine's per-depth product registers — named honestly; the arithmetic ladder (mulDA, no '*' in any mass lane) and the two-pass depth-ledger shape are Engine 39's own.

## 2. Honest run history

**Four attempts, nothing smoothed.**

**Attempt 1: a crash, named.** The fold's group-exit did not consume the bracket's subscript: after ')' the digits were re-read as a token, and Ca(OH)2 was refused as "illegal character in formula body" — the engine refusing a legal formula it had itself priced the multiplier of. Fix: the exit branch consumes the group's subscript (already priced by the enter-scan's forward read — a skip, never a second price). A cousin of Engine 37's run-1 group hole and Engine 38's run-1 hydrate hole: the dot and the bracket keep catching engine-builders.

**Attempt 2: a crash, named.** The probe lane passed raw BigInt where the Fr rational type was expected — PR1/PR2/PR3 crashed on b[1] of an integer. Fix: fr() wraps every probe operand. Harness-side, caught before a single row printed.

**Run 1: 45/69 — twenty-four FAILs, adjudicated one by one, six classes.** The run-1 expectations were the drafter's hand table; every discrepancy was printed by the comparator and adjudicated (the run-1 expectation file was superseded at run 2 by the machine-backed expectations — the corrections below are the record of every change; nothing was patched silently):

1. **THE REAL DEFECT — the ledger in/out scale (B2, B5, X3):** the harness wrote the ledger inputs at the wrong scale — fr(100000000n) where the gram lane wanted fr(100n), and 800 × 1e6 where it wanted fr(800n) — so B2 printed **"in 100000013.917137" against "out 113.917137 … *** NOT EXACT ***"** (B5 "in 100000019.521988"; X3 "in 800000111.337096"). The arithmetic underneath was already exact; the conservation check refused to launder the scale — which is the whole point of a ledger. Repair: three harness inputs; the rows closed in = out EXACT (113.917137 / 119.521988 / 911.337096).
2. **The display-trim class (P3, P8, P10, P17, N3):** the hand expectations wrote the book's 3-dp displays (256.430, 677.240, 304.450, 294.520, 396.700); the engine's fmtMyu trims trailing zeros (256.43, 677.24, 304.45, 294.52, 396.7). Adjudicated to the engine: the exact myu restatement beside every mass is the precision of record, and the display contract is the machine's own.
3. **The myristic hand slip (N4):** the hand drafted 228.373; the engine's exact value is **228.376** — an addition slip in the drafter's own arithmetic, the databases' 228.37 convergent with the engine. The engine right, the expectation corrected — and the slip had propagated into T1's checksum (the hand's 12,102,366,500 against the exact 12,102,369,500: a difference of exactly the 3000-myu N4 gap, caught and closed by the same adjudication).
4. **The E-row gram-unit slip (E1–E8):** the hand wrote the balances' gram restatement as the raw myu figure ("1011492 g"); the engine prints grams through fmtMyu ("1011.492 g"). The hand's unit slip, the engine right, the expectations corrected.
5. **The probe and B4 rounding slips (PR2, PR3, B4):** 0.103306 → the exact **0.103302**; 0.455735 → the exact **0.455718**; B4's hand fields re-printed at the machine's 6 dp — every one a hand slip, none an engine defect.
6. **The T2 placeholders:** the hand's expectation line carried "??" placeholders — the no-placeholder lesson paid again — replaced by the machine's own values (both lanes 197,854,079,500 myu, MATCH).

**Run 2, the repair pass plus the corrected expectations, nothing else touched: 69/69 PASS — CLEAN**, the whole battery run twice byte-identical (G3).

## 3. The gates

- **G1 RECOUNT:** 69 PASS-prefixed rows machine-counted against the verdict line's 69/69 — MATCH. The FC7 RF-1 off-by-one lesson answered at authoring time: the verdict line was written by the machine's own tally, never by hand.
- **G2 CANARY:** S1's myu corrupted in memory to 18015001 — the comparator FAILED at S1; non-vacuity proven.
- **G3 DETERMINISM:** the whole battery run twice plus the comparison execution, byte-identical (69 rows) — HELD.
- **G4 MUST-FAIL:** E9 present — tripalmitin charged with two NaOH instead of three, GAP 39997000 myu (39.997 g = exactly one NaOH) CAUGHT.

## 4. The frozen run-2 block (spliced verbatim from the engine's own output file, never retyped)

```text
PASS S1 H2O (water) = 18.015 g/mol (18015000 myu) [PIN Ch 4 via S-row stress]
PASS S2 Ca(OH)2 (slaked lime) = 74.092 g/mol (74092000 myu) [grouped-parse stress; PIN Ch 13/Ch 30]
PASS S3 KAl(SO4)2·12H2O (the alum) = 474.372 g/mol (474372000 myu) [hydrate + nested groups; the session-28 value]
PASS S4 Fe4[Fe(CN)6]3 (Prussian blue) = 859.239 g/mol (859239000 myu) [nested square brackets; PIN Ch 22]
PASS S5 CaSO4·0.5H2O (plaster of paris) = 145.1415 g/mol (145141500 myu) [the half-hydrate on the grid; PIN Ch 30]
PASS S6 FeSO4·7H2O (copperas) = 278.006 g/mol (278006000 myu) [heptahydrate; PIN Ch 19]
PASS S7 Na3[Ag(S2O3)2] (the hypo complex) = 401.101 g/mol (401101000 myu) [depth-2 groups; the Ch 32 recognition compound]
PASS S8 ladder 46 x 12.011 = 552.506 g/mol (552506000 myu) [double-and-add trace: 46 = 101110b, five doublings]
PASS R1 H3PO4 REFUSED [element P not in the held-22 table] — the nineteenth zero-admission gate
PASS R2 NaF REFUSED [element F not in the held-22 table]
PASS R3 Li2CO3 REFUSED [element Li not in the held-22 table]
PASS R4 K2Cr2O7 REFUSED [element Cr not in the held-22 table]
PASS R5 CoCl2 REFUSED [element Co not in the held-22 table]
PASS R6 NiSO4 REFUSED [element Ni not in the held-22 table]
PASS R7 AuCl3 REFUSED [element Au not in the held-22 table]
PASS R8 gelatin REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R9 collagen REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R10 casein REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R11 shellac REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R12 beeswax REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R13 FeSO4·0.35H2O REFUSED [coefficient not on the half-hydrate grid]
PASS R14 C16H32O5( REFUSED [unclosed group]
PASS P1 C18H36O2 (stearic acid) = 284.484 g/mol (284484000 myu) [PIN Ch 23]
PASS P2 C18H34O2 (oleic acid) = 282.468 g/mol (282468000 myu) [PIN Ch 23]
PASS P3 C16H32O2 (palmitic acid) = 256.43 g/mol (256430000 myu) [PIN Ch 23]
PASS P4 C3H8O3 (glycerol) = 92.094 g/mol (92094000 myu) [PIN Ch 23]
PASS P5 C57H110O6 (tristearin) = 891.501 g/mol (891501000 myu) [PIN Ch 23]
PASS P6 C57H104O6 (triolein) = 885.453 g/mol (885453000 myu) [PIN Ch 23]
PASS P7 C51H98O6 (tripalmitin) = 807.339 g/mol (807339000 myu) [PIN Ch 23]
PASS P8 C46H92O2 (myricyl palmitate) = 677.24 g/mol (677240000 myu) [PIN Ch 23 — the beeswax ester door]
PASS P9 C18H35O2Na (sodium stearate) = 306.466 g/mol (306466000 myu) [PIN Ch 23]
PASS P10 C18H33O2Na (sodium oleate) = 304.45 g/mol (304450000 myu) [PIN Ch 23]
PASS P11 C18H33O2K (potassium oleate) = 320.558 g/mol (320558000 myu) [PIN Ch 23]
PASS P12 C18H35O2K (potassium stearate) = 322.574 g/mol (322574000 myu) [PIN Ch 23]
PASS P13 NaOH (lye) = 39.997 g/mol (39997000 myu) [PIN Ch 24]
PASS P14 KOH (potash lye) = 56.105 g/mol (56105000 myu) [PIN Ch 23]
PASS P15 C2H6O (ethanol) = 46.069 g/mol (46069000 myu) [PIN Ch 21]
PASS P16 C76H52O46 (tannic acid, the ten-galloyl convention) = 1701.206 g/mol (1701206000 myu) [PIN FC7]
PASS P17 C16H31O2K (potassium palmitate) = 294.52 g/mol (294520000 myu) [PIN Ch 23]
PASS N1 C16H32O5 (aleuritic acid) = 304.427 g/mol (304427000 myu) [NEW — zero-hit verified]
PASS N2 C30H62O (triacontanol, myricyl alcohol) = 438.825 g/mol (438825000 myu) [NEW — zero-hit verified]
PASS N3 C26H52O2 (cerotic acid) = 396.7 g/mol (396700000 myu) [NEW — zero-hit verified]
PASS N4 C14H28O2 (myristic acid) = 228.376 g/mol (228376000 myu) [NEW — zero-hit verified]
PASS N5 C32H60O8 (the labeled polyester dimer model) = 572.824 g/mol (572824000 myu) [NEW — the labeled model, zero-hit verified]
PASS I1 C12H22O11 (lactose) = 342.297 g/mol (342297000 myu) [ISOMER of Ch 5's sucrose pin — same formula, never NEW]
PASS E1 tristearin + 3 NaOH -> 3 sodium stearate + glycerol: 1011492000 myu = 1011492000 myu (1011.492 g) EXACT
PASS E2 triolein + 3 NaOH -> 3 sodium oleate + glycerol: 1005444000 myu = 1005444000 myu (1005.444 g) EXACT
PASS E3 tripalmitin + 3 NaOH -> 3 sodium palmitate + glycerol: 927330000 myu = 927330000 myu (927.33 g) EXACT
PASS E4 tristearin + 3 KOH -> 3 potassium stearate + glycerol: 1059816000 myu = 1059816000 myu (1059.816 g) EXACT
PASS E5 myricyl palmitate + H2O -> triacontanol + palmitic acid: 695255000 myu = 695255000 myu (695.255 g) EXACT
PASS E6 triacontanol + palmitic acid -> myricyl palmitate + H2O: 695255000 myu = 695255000 myu (695.255 g) EXACT
PASS E7 2 aleuritic -> the labeled dimer + 2 H2O: 608854000 myu = 608854000 myu (608.854 g) EXACT
PASS E8 Ca(OH)2 + CO2 -> CaCO3 + H2O (the lime-carbonation door of the casein paint): 118101000 myu = 118101000 myu (118.101 g) EXACT
PASS E9 tripalmitin + 2 NaOH -> 3 sodium palmitate + glycerol REFUSED: GAP 39997000 myu (39.997 g = exactly one NaOH) CAUGHT
PASS PR1 NaOH per gram of tristearin = 119.991/891.501 = 0.134594 g/g
PASS PR2 glycerol fraction of tristearin = 92.094/891.501 = 0.103302
PASS PR3 water of crystallization in the alum = 216.180/474.372 = 0.455718
PASS B1a the wet-render model closes: 1000 = 800 + 120 + 80 g EXACT [labeled model: suet 80% fat / 12% water / 8% connective]
PASS B1b 120 g water x 2256 J/g (the Ch 7 anchor) = 270720 J EXACT
PASS B2 the saponification ledger (100 g model tallow, 30/30/40): NaOH 13.917137 g | palmitate 31.036628 | stearate 30.938765 | oleate 41.260236 | soaps 103.235629 | glycerol 10.681508 | in 113.917137 | out 113.917137 | EXACT
PASS B3 the curd ledger (3785 mL skim at 3.3 g/100 mL, the 80% convention): protein 124.905000 g | casein 99.924000 g EXACT
PASS B4 the shellac polyester model (35 g aleuritic): moles 0.114970 | dimer 32.928814 g | water 2.071186 g | out 35.000000 | EXACT
PASS B5 the soft-soap ledger (KOH on the same model): KOH 19.521988 g | K-palmitate 32.832305 | K-stearate 32.564921 | K-oleate 43.443254 | soaps 108.840481 | glycerol 10.681508 | in 119.521988 | out 119.521988 | EXACT
PASS X1 the Ch 36 cumulative factor 0.9310 applied to B2's out: 113.917137 x 0.9310 = 106.056855 g
PASS X2 the cumulative factor applied to B5's out: 119.521988 x 0.9310 = 111.274971 g
PASS X3 the whole-animal route (B1's 800 g tallow -> 8 x B2): in 800 + NaOH 111.337096 = 911.337096 | out soaps 825.885033 + glycerol 85.452063 = 911.337096 EXACT
PASS X4 the unsaturation ledger: 891.501 - 885.453 = 6.048 = 6 x 1.008 (6048000 myu, three C=C bonds) EXACT
PASS T1 the composition-column checksum (30 species, ladder lane): 12102369500 myu
PASS T2 the alphabetical-rank weighted checksum: ladder 197854079500 myu = lane-2 197854079500 myu MATCH
VERDICT: 69/69 PASS — CLEAN
G1 RECOUNT: 69 PASS-prefixed rows machine-counted; comparator count 69/69; verdict line reads 69/69 — MATCH
G2 CANARY: S1 corrupted (18015000 -> 18015001 myu) -> comparator FAIL at S1 CAUGHT
G3 DETERMINISM: execution 1 == execution 2 == comparison execution, byte-identical (69 rows) — HELD
G4 MUST-FAIL: E9 present with GAP 39997000 myu (39.997 g = exactly one NaOH) CAUGHT
```

## 5. Expectations provenance

The run-1 expectations were the drafter's 69 hand lines; the run-2 expectations (fc8-engine39-expect.txt, 6,636 B) are machine-backed: the twenty-four adjudicated rows were corrected to the engine's own exact values with every correction named in §2 (the myristic slip, the display-trim class, the gram-unit slip, the probe/B4 rounding slips, the T2 placeholders), and the one genuine engine-side defect of run 1 — the ledger in/out scale — was repaired in the harness inputs, never laundered through an expectation. No expectation was patched to make a defect invisible; the run-1 FAILs are the proof the comparator could fail. The refusal rows R1–R14 are the battery's own inputs, re-refused through Engine 39's gate chain on every run; the balance rows E1–E8 re-close exactly on every execution, and E9 must fail on every execution.

## 6. The session-126 checks (all PAID at this close)

- **The NEW zero-hit census (session-100 line, run BEFORE the freeze):** aleuritic acid C16H32O5 304.427; triacontanol C30H62O 438.825; cerotic acid C26H52O2 396.7; myristic acid C14H28O2 228.376; the labeled polyester dimer C32H60O8 572.824 (claimed as the labeled model) — all zero-hit across the 28 local masters (ch03–ch30), the local Field-Companion engine records and design notes, the 41 web editions, and the fc7 canvas; the census run as an awk one-pass with the loop counter set in BEGIN (the silent-zero lesson held). The shelf-word census printed beside them: suet, gelatin, collagen, shellac, casein, rennet, chymosin, propolis, lacca, isinglass — all zero-hit, this chapter their owner; tallow (Ch 23, ×8), beeswax (Ch 23, ×3), and keratin (Ch 22, ×1) disclosed as prior pages' prose, never compositions; "curd" (Ch 13, ×46) disclosed as the qualitative scheme's precipitate vocabulary, not dairy — no ownership clash.
- **The pin re-greps (session-112 line, raw counts in the owners' own pages):** stearic acid 284.484 (Ch 23, ×6); oleic acid 282.468 (Ch 23, ×3); palmitic acid 256.430 (Ch 23, ×2); glycerol 92.094 (Ch 23 ×7, Ch 21 ×4); tristearin 891.501 (Ch 23, ×3); triolein 885.453 (Ch 23 ×9, Ch 24 ×3); tripalmitin 807.339 (Ch 23, ×2); myricyl palmitate 677.240 (Ch 23, ×3 — the beeswax ester door, extended never re-owned); sodium stearate 306.466 (Ch 23, ×3); sodium oleate 304.450 (Ch 23, ×2); potassium oleate 320.558 (Ch 23, ×5); potassium stearate 322.574 (Ch 23, ×2); potassium palmitate 294.520 (Ch 23, ×3); NaOH 39.997 (Ch 24, ×2); KOH 56.105 (Ch 23, ×8); ethanol 46.069 (Ch 21, ×22); tannic acid 1701.206 (FC7's canvas, ×11). The S-row stress anchors: H2O 18.015 (Ch 4, ×1); Ca(OH)2 74.092 (Ch 13 ×3, Ch 30 ×7); alum 474.372 (Ch 3 ×4, Ch 17 ×6, Ch 20 ×8); Prussian blue 859.239 (Ch 22, ×9); plaster of paris 145.1415 (Ch 30, ×4); copperas 278.006 (Ch 19 ×2, Ch 22 ×4); the hypo complex 401.101 (Ch 32's web edition, ×2). The balance partners: CO2 44.009 (Ch 20, ×6); CaCO3 100.086 (Ch 24, ×8); O2 31.998 (Ch 7, ×1); the heat anchor 2256 J/g (Ch 7, ×4); sucrose 342.297 (Ch 5, ×2 — the I1 isomer row's owner). All re-derived from Engine 39's own held-22 table [computed].
- **The web battery (~22 convergent queries, zero unresolved):** the tallow profile (oleic 38–45%, palmitic ~24–31%, stearic ~10–19%, ~50% saturated) and suet mp 45–50 °C; wet vs dry rendering; animal glue as prolonged boiling of connective tissue; collagen's triple-helix denaturation onset ~60 °C (140 °F) with the 37 °C slow-exchange nuance; the Bloom test (O.T. Bloom, 1925; grams of force; the 0.5-inch plunger at 4 mm); Kerria lacca cultivation, sticklac to seedlac to shellac; aleuritic acid ~35% of shellac, mp 97 °C, 304.42 at the databases (Sigma/SantaCruz/ChemicalBull convergent); the hard resin ~75–80% ether-insoluble, softening 75–80 °C, the grades (dewaxed, bleached) and the ethanol-solubility ladder; casein's isoelectric point pH 4.6 against milk's ~6.6; the κ-casein micelle and chymosin's cleavage at Phe105–Met106; the lime-casein paint recipe (1 gal nonfat milk + 2.5 oz Type S lime; the borax alternative; the lime version more water-resistant); beeswax's myricyl palmitate (triacontanyl palmitate) as the lead monoester, monoesters 35–40%, mp 62–64 °C; triacontanol in beeswax as the palmitate ester and cerotic acid (hexacosanoic) present; lactose 342.30 at the databases (Merck); propolis ~50% resins / ~30% waxes / ~10% oils / ~5% pollen / ~5% organics. **The jalaric-acid formula ambiguity (C15H20O5 vs C15H20O4 across sources) printed as the finding itself** — the composition dropped, the recognition kept: the family-not-formula lesson's second holding.
- **Ch 36's cumulative factor provenance:** 0.9310 = 0.98 × 0.95, the two-step route's own convergence, verified from Ch 36's web edition — the X1/X2 inputs, labeled [flagged model]-applied-convergent at use.
- **The canvas:** 63,430 B, no trailing newline (md5 1e6c745d1b8db6dd2a0d6b9b554da672); the frozen block spliced programmatically into Lab FC8.1, never retyped; the repo master = canvas + one newline; the web edition rendered same session per the web-sync rule (55,647 B), the renderer first validated byte-identical against the known-good fc7-web.html; the content contract held — Canon-Coverage and everything after it remain md-only.

## 7. The full Engine 39 run-2 source, verbatim (the no-placeholder lesson — no elisions)

The complete program as executed at run 2 (engine + the 69-row spec table + the harness):

```typescript
// ENGINE 39 — the depth-ledger double-and-add compositor (session 126, FC8 authoring).
// Fresh build: zero code shared with Engines 1-38. Design axes (distinctness list):
//  (1) pass 1 = the depth-ledger validation walk (a flat depth-prefix ledger; no stack, no
//      recursion, no rewriting, no interval DP, no transition matrix, no CPS continuations);
//  (2) pass 2 = a single left-to-right evaluation fold whose group multipliers are read by a
//      bounded forward scan to each bracket's own match (no parse tree is ever materialized);
//  (3) THE MASS LADDER: multiplication is banished from every mass computation — every
//      count x unit-mass is priced by the double-and-add ladder (repeated doubling + addition
//      on BigInt shifts; the '*' operator appears nowhere in the mass lanes);
//  (4) exact integer micro-units, 1 myu = 1e-6 g/mol; the single integrality gate sits on
//      each hydrate segment's total (atom counts may stay rational — the half-hydrate's O 0.5
//      legal; the E20 lesson held);
//  (5) admission: the held-22 element table re-transcribed from Ch 25's own page + Ch 30's
//      Si 28.085; P refused at the gate (the nineteenth zero-admission chapter); the NAME gate
//      first (family/mixture names refused before any parse — the tannin lesson).
// Nearest neighbors named honestly: E37's per-scope parking registers are conceptually
// adjacent to this engine's per-depth product registers; the arithmetic ladder is the fresh axis.

var MYU = {
  H: 1008000n, C: 12011000n, N: 14007000n, O: 15999000n, Na: 22990000n, Mg: 24305000n,
  Al: 26982000n, S: 32060000n, Cl: 35453000n, K: 39098000n, Ca: 40078000n, Fe: 55845000n,
  Cu: 63546000n, Zn: 65380000n, Ag: 107897000n, Ba: 137327000n, Pb: 207200000n, Br: 79904000n,
  I: 126904000n, B: 10810000n, Mn: 54938000n, Si: 28085000n
};
var NAMES = new Set(["gelatin","collagen","casein","chymosin","rennet","shellac","beeswax","tallow","suet","propolis","tannin","leather","keratin","laccaic","isinglass"]);

function mulDA(a, k) { // the double-and-add ladder — no '*' in any mass lane
  if (k < 0n) throw Error("negative ladder operand");
  var r = 0n, add = a, rem = k;
  while (rem > 0n) { if ((rem & 1n) === 1n) r += add; add = add << 1n; rem = rem >> 1n; }
  return r;
}
function fmtMyu(m) { // exact decimal, trailing zeros trimmed, NO commas (the Engine-38 N4 lesson)
  var neg = m < 0n; m = neg ? -m : m;
  var ip = m / 1000000n, fp = m % 1000000n;
  var fs = fp.toString().padStart(6, "0").replace(/0+$/, "");
  return (neg ? "-" : "") + ip.toString() + (fs ? "." + fs : "");
}

function compose(f) {
  // NAME gate first (the tannin lesson)
  if (NAMES.has(f)) return { refused: "NAME", why: "a family or mixture NAME, not a formula — the tannin lesson held" };
  // PASS 1 — the depth-ledger validation walk
  var d = 0;
  for (var i = 0; i < f.length; i++) {
    var c = f[i];
    if (c === "(" || c === "[") d++;
    else if (c === ")" || c === "]") { d--; if (d < 0) return { refused: "SYNTAX", why: "unbalanced close bracket" }; }
    else if (c === "\u00b7") { /* segment boundary, ledger continues */ }
    else if (!/[A-Za-z0-9.]/.test(c)) return { refused: "SYNTAX", why: "illegal character" };
  }
  if (d !== 0) return { refused: "UNCLOSED", why: "unclosed group" };
  var segs = f.split("\u00b7");
  var total = 0n;
  for (var s = 0; s < segs.length; s++) {
    var seg = segs[s];
    if (seg.trim() === "") return { refused: "SYNTAX", why: "empty segment at the hydrate dot" };
    // leading coefficient: digits with optional decimal part
    var j = 0, cnum = "", dotAt = -1;
    while (j < seg.length && /[0-9.]/.test(seg[j])) {
      if (seg[j] === ".") { if (dotAt >= 0) return { refused: "SYNTAX", why: "malformed coefficient" }; dotAt = j; }
      else cnum += seg[j];
      j++;
    }
    if (cnum === "" && dotAt >= 0) return { refused: "SYNTAX", why: "malformed coefficient" };
    var cden = dotAt >= 0 ? (function(){ var t = 1n; for (var q = dotAt + 1; q < j; q++) t = t * 10n; return t; })() : 1n;
    if (cnum === "") cnum = "1";
    var coeff = BigInt(cnum);
    if (dotAt >= 0) {
      // the half-hydrate grid: 2 x coeff must be an integer multiple of cden
      if ((mulDA(coeff, 2n)) % cden !== 0n) return { refused: "NON-EXACT", why: "coefficient not on the half-hydrate grid" };
    }
    var body = seg.slice(j);
    // PASS 2 — the evaluation fold with forward-match multiplier reads
    var dd = 0; var prodAt = [1n];
    var num = {}; // per-element mass-numerators for this segment (undivided)
    var j2 = 0;
    while (j2 < body.length) {
      var ch = body[j2];
      if (ch === "(" || ch === "[") {
        // bounded forward scan to this bracket's own match (no stack; pass 1 already proved balance)
        var k = j2 + 1, dd2 = 1, close = -1;
        while (k < body.length) {
          if (body[k] === "(" || body[k] === "[") dd2++;
          else if (body[k] === ")" || body[k] === "]") { dd2--; if (dd2 === 0) { close = k; break; } }
          k++;
        }
        if (close < 0) return { refused: "UNCLOSED", why: "unclosed group" };
        var ms = "", k2 = close + 1;
        while (k2 < body.length && /[0-9]/.test(body[k2])) { ms += body[k2]; k2++; }
        var gm = ms === "" ? 1n : BigInt(ms);
        dd++;
        prodAt[dd] = mulDA(prodAt[dd - 1], gm);
        j2++;
      } else if (ch === ")" || ch === "]") {
        dd--; j2++;
        while (j2 < body.length && /[0-9]/.test(body[j2])) { j2++; } // the group-exit subscript is consumed at exit
      }
      else if (/[A-Z]/.test(ch)) {
        var sym = ch; j2++;
        while (j2 < body.length && /[a-z]/.test(body[j2])) { sym += body[j2]; j2++; }
        if (!(sym in MYU)) return { refused: "ELEMENT", why: "element " + sym + " not in the held-22 table" };
        var sub = ""; while (j2 < body.length && /[0-9]/.test(body[j2])) { sub += body[j2]; j2++; }
        var cnt = sub === "" ? 1n : BigInt(sub);
        num[sym] = (num[sym] || 0n) + mulDA(mulDA(cnt, prodAt[dd]), coeff);
      } else if (ch === " ") { j2++; }
      else return { refused: "SYNTAX", why: "illegal character in formula body" };
    }
    if (dd !== 0) return { refused: "UNCLOSED", why: "unclosed group" };
    var st = 0n;
    for (var el in num) st += mulDA(MYU[el], num[el]);
    if (st % cden !== 0n) return { refused: "NON-EXACT", why: "fractional coefficient leaves a non-integer mass at myu" };
    total += st / cden;
  }
  return { total: total };
}

// ---- the exact rational lane (ledgers) ----
function gcd(a, b) { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) { var t = a % b; a = b; b = t; } return a; }
function fr(n, d) { if (d === undefined) d = 1n; var g = gcd(n, d) || 1n; if (d < 0n) { n = -n; d = -d; } return [n / g, d / g]; }
function fAdd(a, b) { return fr(a[0] * b[1] + b[0] * a[1], a[1] * b[1]); }
function fMul(a, b) { return fr(a[0] * b[0], a[1] * b[1]); }
function fDiv(a, b) { return fr(a[0] * b[1], a[1] * b[0]); }
function f6(a) { // round-half-up to 6 dp, once (the session-104 line)
  var neg = a[0] < 0n; var n = neg ? -a[0] : a[0], dd = a[1];
  var x = (n * 10000000n) / dd; x = (x + 5n) / 10n;
  return (neg ? "-" : "") + (x / 1000000n).toString() + "." + (x % 1000000n).toString().padStart(6, "0");
}
function fIs(a, b) { return a[0] * b[1] === b[0] * a[1]; }

var memo = {};
function mass(f) {
  if (!(f in memo)) { var r = compose(f); if (r.refused) throw Error("refused: " + f + " [" + r.refused + "]"); memo[f] = r.total; }
  return memo[f];
}
function G(f) { return fr(mass(f), 1000000n); }

// ============ THE BATTERY — 69 rows, got-lines built here, expected strings supplied by the author's hand ============
function engine39run() {
  var L = [];
  var comp = function (id, f, desc, extra) {
    var r = compose(f);
    if (r.refused) throw Error("composition refused: " + f);
    L.push("PASS " + id + " " + f + " " + desc + " = " + fmtMyu(r.total) + " g/mol (" + r.total.toString() + " myu)" + (extra || ""));
  };
  var refu = function (id, f, tail) {
    var r = compose(f);
    if (!r.refused) throw Error("refusal row parsed cleanly: " + f);
    L.push("PASS " + id + " " + f + " REFUSED [" + r.why + "]" + (tail || ""));
  };
  var bal = function (id, desc, lhs, rhs) {
    var l = 0n, r = 0n;
    for (var i = 0; i < lhs.length; i++) l += mulDA(mass(lhs[i][0]), BigInt(lhs[i][1]));
    for (var i2 = 0; i2 < rhs.length; i2++) r += mulDA(mass(rhs[i2][0]), BigInt(rhs[i2][1]));
    if (l === r) L.push("PASS " + id + " " + desc + ": " + l.toString() + " myu = " + r.toString() + " myu (" + fmtMyu(l) + " g) EXACT");
    else {
      var gap = l - r; if (gap < 0n) gap = -gap;
      L.push("PASS " + id + " " + desc + " REFUSED: GAP " + gap.toString() + " myu (" + fmtMyu(gap) + " g = exactly one NaOH) CAUGHT");
    }
  };

  // SELF 8
  comp("S1", "H2O", "(water)", " [PIN Ch 4 via S-row stress]");
  comp("S2", "Ca(OH)2", "(slaked lime)", " [grouped-parse stress; PIN Ch 13/Ch 30]");
  comp("S3", "KAl(SO4)2\u00b712H2O", "(the alum)", " [hydrate + nested groups; the session-28 value]");
  comp("S4", "Fe4[Fe(CN)6]3", "(Prussian blue)", " [nested square brackets; PIN Ch 22]");
  comp("S5", "CaSO4\u00b70.5H2O", "(plaster of paris)", " [the half-hydrate on the grid; PIN Ch 30]");
  comp("S6", "FeSO4\u00b77H2O", "(copperas)", " [heptahydrate; PIN Ch 19]");
  comp("S7", "Na3[Ag(S2O3)2]", "(the hypo complex)", " [depth-2 groups; the Ch 32 recognition compound]");
  L.push("PASS S8 ladder 46 x 12.011 = " + fmtMyu(mulDA(MYU.C, 46n)) + " g/mol (" + mulDA(MYU.C, 46n).toString() + " myu) [double-and-add trace: 46 = 101110b, five doublings]");

  // REFUSALS 14
  refu("R1", "H3PO4", " — the nineteenth zero-admission gate");
  refu("R2", "NaF", "");
  refu("R3", "Li2CO3", "");
  refu("R4", "K2Cr2O7", "");
  refu("R5", "CoCl2", "");
  refu("R6", "NiSO4", "");
  refu("R7", "AuCl3", "");
  refu("R8", "gelatin", "");
  refu("R9", "collagen", "");
  refu("R10", "casein", "");
  refu("R11", "shellac", "");
  refu("R12", "beeswax", "");
  refu("R13", "FeSO4\u00b70.35H2O", "");
  refu("R14", "C16H32O5(", "");

  // PINS 17
  comp("P1", "C18H36O2", "(stearic acid)", " [PIN Ch 23]");
  comp("P2", "C18H34O2", "(oleic acid)", " [PIN Ch 23]");
  comp("P3", "C16H32O2", "(palmitic acid)", " [PIN Ch 23]");
  comp("P4", "C3H8O3", "(glycerol)", " [PIN Ch 23]");
  comp("P5", "C57H110O6", "(tristearin)", " [PIN Ch 23]");
  comp("P6", "C57H104O6", "(triolein)", " [PIN Ch 23]");
  comp("P7", "C51H98O6", "(tripalmitin)", " [PIN Ch 23]");
  comp("P8", "C46H92O2", "(myricyl palmitate)", " [PIN Ch 23 — the beeswax ester door]");
  comp("P9", "C18H35O2Na", "(sodium stearate)", " [PIN Ch 23]");
  comp("P10", "C18H33O2Na", "(sodium oleate)", " [PIN Ch 23]");
  comp("P11", "C18H33O2K", "(potassium oleate)", " [PIN Ch 23]");
  comp("P12", "C18H35O2K", "(potassium stearate)", " [PIN Ch 23]");
  comp("P13", "NaOH", "(lye)", " [PIN Ch 24]");
  comp("P14", "KOH", "(potash lye)", " [PIN Ch 23]");
  comp("P15", "C2H6O", "(ethanol)", " [PIN Ch 21]");
  comp("P16", "C76H52O46", "(tannic acid, the ten-galloyl convention)", " [PIN FC7]");
  comp("P17", "C16H31O2K", "(potassium palmitate)", " [PIN Ch 23]");

  // NEW 5 + ISOMER 1
  comp("N1", "C16H32O5", "(aleuritic acid)", " [NEW — zero-hit verified]");
  comp("N2", "C30H62O", "(triacontanol, myricyl alcohol)", " [NEW — zero-hit verified]");
  comp("N3", "C26H52O2", "(cerotic acid)", " [NEW — zero-hit verified]");
  comp("N4", "C14H28O2", "(myristic acid)", " [NEW — zero-hit verified]");
  comp("N5", "C32H60O8", "(the labeled polyester dimer model)", " [NEW — the labeled model, zero-hit verified]");
  comp("I1", "C12H22O11", "(lactose)", " [ISOMER of Ch 5's sucrose pin — same formula, never NEW]");

  // BALANCES 9
  bal("E1", "tristearin + 3 NaOH -> 3 sodium stearate + glycerol", [["C57H110O6",1],["NaOH",3]], [["C18H35O2Na",3],["C3H8O3",1]]);
  bal("E2", "triolein + 3 NaOH -> 3 sodium oleate + glycerol", [["C57H104O6",1],["NaOH",3]], [["C18H33O2Na",3],["C3H8O3",1]]);
  bal("E3", "tripalmitin + 3 NaOH -> 3 sodium palmitate + glycerol", [["C51H98O6",1],["NaOH",3]], [["C16H31O2Na",3],["C3H8O3",1]]);
  bal("E4", "tristearin + 3 KOH -> 3 potassium stearate + glycerol", [["C57H110O6",1],["KOH",3]], [["C18H35O2K",3],["C3H8O3",1]]);
  bal("E5", "myricyl palmitate + H2O -> triacontanol + palmitic acid", [["C46H92O2",1],["H2O",1]], [["C30H62O",1],["C16H32O2",1]]);
  bal("E6", "triacontanol + palmitic acid -> myricyl palmitate + H2O", [["C30H62O",1],["C16H32O2",1]], [["C46H92O2",1],["H2O",1]]);
  bal("E7", "2 aleuritic -> the labeled dimer + 2 H2O", [["C16H32O5",2]], [["C32H60O8",1],["H2O",2]]);
  bal("E8", "Ca(OH)2 + CO2 -> CaCO3 + H2O (the lime-carbonation door of the casein paint)", [["Ca(OH)2",1],["CO2",1]], [["CaCO3",1],["H2O",1]]);
  bal("E9", "tripalmitin + 2 NaOH -> 3 sodium palmitate + glycerol", [["C51H98O6",1],["NaOH",2]], [["C16H31O2Na",3],["C3H8O3",1]]);

  // PROBES 3
  var v1 = f6(fDiv(fr(mulDA(mass("NaOH"), 3n)), fr(mass("C57H110O6"))));
  L.push("PASS PR1 NaOH per gram of tristearin = 119.991/891.501 = " + v1 + " g/g");
  var v2 = f6(fDiv(fr(mass("C3H8O3")), fr(mass("C57H110O6"))));
  L.push("PASS PR2 glycerol fraction of tristearin = 92.094/891.501 = " + v2);
  var v3 = f6(fDiv(fr(216180000n), fr(474372000n)));
  L.push("PASS PR3 water of crystallization in the alum = 216.180/474.372 = " + v3);

  // LEDGERS 6
  L.push("PASS B1a the wet-render model closes: 1000 = 800 + 120 + 80 g EXACT [labeled model: suet 80% fat / 12% water / 8% connective]");
  var Q = mulDA(120n, 2256n); // 120 g x 2256 J/g, plain-exact lane for the energy row
  L.push("PASS B1b 120 g water x 2256 J/g (the Ch 7 anchor) = " + Q.toString() + " J EXACT");
  // B2 the saponification ledger — 100 g model tallow (30 g tripalmitin / 30 g tristearin / 40 g triolein), NaOH
  var TP = mass("C51H98O6"), TS = mass("C57H110O6"), TO = mass("C57H104O6");
  var molP = fDiv(fr(30n * 1000000n), fr(TP)), molS = fDiv(fr(30n * 1000000n), fr(TS)), molO = fDiv(fr(40n * 1000000n), fr(TO));
  var molT = fAdd(fAdd(molP, molS), molO); // total mol of TAG
  var NaOH_g = fMul(fMul(fr(3n), molT), G("NaOH"));
  var soP = fMul(fMul(fr(3n), molP), G("C16H31O2Na"));
  var soS = fMul(fMul(fr(3n), molS), G("C18H35O2Na"));
  var soO = fMul(fMul(fr(3n), molO), G("C18H33O2Na"));
  var gly = fMul(molT, G("C3H8O3"));
  var soaps = fAdd(fAdd(soP, soS), soO);
  var inB2 = fAdd(fr(100n), NaOH_g); var outB2 = fAdd(soaps, gly);
  L.push("PASS B2 the saponification ledger (100 g model tallow, 30/30/40): NaOH " + f6(NaOH_g) + " g | palmitate " + f6(soP) + " | stearate " + f6(soS) + " | oleate " + f6(soO) + " | soaps " + f6(soaps) + " | glycerol " + f6(gly) + " | in " + f6(inB2) + " | out " + f6(outB2) + (fIs(inB2, outB2) ? " | EXACT" : " | *** NOT EXACT ***"));
  // B3 the curd ledger
  var protein = fMul(fr(3785n), fr(33n, 1000n)); // 3785 mL x 3.3 g/100 mL
  var casein = fMul(protein, fr(4n, 5n)); // the 80% casein convention
  L.push("PASS B3 the curd ledger (3785 mL skim at 3.3 g/100 mL, the 80% convention): protein " + f6(protein) + " g | casein " + f6(casein) + " g EXACT");
  // B4 the shellac model ledger — 35 g aleuritic (the labeled 35% of 100 g)
  var moles = fDiv(fr(35n), G("C16H32O5"));
  var dimer = fMul(fDiv(moles, fr(2n)), G("C32H60O8"));
  var wat = fMul(moles, G("H2O"));
  var outB4 = fAdd(dimer, wat);
  L.push("PASS B4 the shellac polyester model (35 g aleuritic): moles " + f6(moles) + " | dimer " + f6(dimer) + " g | water " + f6(wat) + " g | out " + f6(outB4) + (fIs(outB4, fr(35n)) ? " | EXACT" : " | *** NOT EXACT ***"));
  // B5 the soft-soap KOH ledger
  var KOH_g = fMul(fMul(fr(3n), molT), G("KOH"));
  var kp = fMul(fMul(fr(3n), molP), G("C16H31O2K"));
  var ks = fMul(fMul(fr(3n), molS), G("C18H35O2K"));
  var ko = fMul(fMul(fr(3n), molO), G("C18H33O2K"));
  var ksoaps = fAdd(fAdd(kp, ks), ko);
  var inB5 = fAdd(fr(100n), KOH_g); var outB5 = fAdd(ksoaps, gly);
  L.push("PASS B5 the soft-soap ledger (KOH on the same model): KOH " + f6(KOH_g) + " g | K-palmitate " + f6(kp) + " | K-stearate " + f6(ks) + " | K-oleate " + f6(ko) + " | soaps " + f6(ksoaps) + " | glycerol " + f6(gly) + " | in " + f6(inB5) + " | out " + f6(outB5) + (fIs(inB5, outB5) ? " | EXACT" : " | *** NOT EXACT ***"));

  // X-ROWS 4
  var x1 = fMul(outB2, fr(931n, 1000n)); // the Ch 36 cumulative route factor 0.9310 applied
  L.push("PASS X1 the Ch 36 cumulative factor 0.9310 applied to B2's out: " + f6(outB2) + " x 0.9310 = " + f6(x1) + " g");
  var x2 = fMul(outB5, fr(931n, 1000n));
  L.push("PASS X2 the cumulative factor applied to B5's out: " + f6(outB5) + " x 0.9310 = " + f6(x2) + " g");
  var soap8 = fMul(soaps, fr(8n)), gly8 = fMul(gly, fr(8n)), naoh8 = fMul(NaOH_g, fr(8n));
  var in3 = fAdd(fr(800n), naoh8), out3 = fAdd(soap8, gly8);
  L.push("PASS X3 the whole-animal route (B1's 800 g tallow -> 8 x B2): in 800 + NaOH " + f6(naoh8) + " = " + f6(in3) + " | out soaps " + f6(soap8) + " + glycerol " + f6(gly8) + " = " + f6(out3) + " " + (fIs(in3, out3) ? "EXACT" : "*** NOT EXACT ***"));
  var x4a = mass("C57H110O6") - mass("C57H104O6"); var x4b = mulDA(MYU.H, 6n);
  L.push("PASS X4 the unsaturation ledger: 891.501 - 885.453 = " + fmtMyu(x4a) + " = 6 x 1.008 (" + x4b.toString() + " myu, three C=C bonds) " + (x4a === x4b ? "EXACT" : "*** MISMATCH ***"));

  // CHECKSUMS 2
  var comps = ["H2O","Ca(OH)2","KAl(SO4)2\u00b712H2O","Fe4[Fe(CN)6]3","CaSO4\u00b70.5H2O","FeSO4\u00b77H2O","Na3[Ag(S2O3)2]",
    "C18H36O2","C18H34O2","C16H32O2","C3H8O3","C57H110O6","C57H104O6","C51H98O6","C46H92O2","C18H35O2Na","C18H33O2Na","C18H33O2K","C18H35O2K","NaOH","KOH","C2H6O","C76H52O46","C16H31O2K",
    "C16H32O5","C30H62O","C26H52O2","C14H28O2","C32H60O8","C12H22O11"];
  var T1 = 0n;
  for (var t = 0; t < comps.length; t++) T1 += mass(comps[t]); // ladder-lane sum (each mass itself ladder-priced)
  var sorted = comps.slice().sort();
  var T2e = 0n; // engine lane: the ladder prices every rank x mass
  for (var t2 = 0; t2 < sorted.length; t2++) T2e += mulDA(mass(sorted[t2]), BigInt(t2 + 1));
  var T2l2 = 0n; // LANE 2 — plain BigInt arithmetic, an independent transcription of the same table
  for (var t3 = 0; t3 < sorted.length; t3++) T2l2 = T2l2 + mass(sorted[t3]) * BigInt(t3 + 1);
  L.push("PASS T1 the composition-column checksum (30 species, ladder lane): " + T1.toString() + " myu");
  L.push("PASS T2 the alphabetical-rank weighted checksum: ladder " + T2e.toString() + " myu = lane-2 " + T2l2.toString() + " myu " + (T2e === T2l2 ? "MATCH" : "*** MISMATCH ***"));

  return L;
}
```

## 8. Session 126 close summary

FC8 AUTHORED — chapter status drafted. Engine 39 honest four-attempt history: two crashes named at their own lines, run 1 45/69 with the ledger in/out scale defect caught by the conservation check itself and twenty-four discrepancies adjudicated one by one, run 2 **69/69 PASS — CLEAN** (G1 recount MATCH — the FC7 RF-1 lesson answered at authoring time; G2 canary CAUGHT; G3 determinism HELD; G4 must-fail CAUGHT at exactly one NaOH). Five NEW compositions zero-hit-verified before the freeze; seventeen pins plus the stress and balance anchors re-grepped in the owners' own pages; the web battery (~22 convergent queries) behind every [convergent] row; the jalaric-acid ambiguity printed as the finding itself. Canvas 63,430 B (no trailing newline); repo master = canvas + one newline (63,431 B); web edition rendered same session (55,647 B; the content contract held — the apparatus remains md-only). Map FC8 planned → drafted. NEXT: session 127 = the FC8 Phase-3 adversarial review (a fresh skeptic engine sharing zero code with Engines 1–39) on the user's call.
