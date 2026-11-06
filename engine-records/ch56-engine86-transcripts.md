# Engine 86 — the exact-fraction engine (E86-XF) — session 201, Vol IX Ch 56

Fresh build, zero code shared with Engines 1-85. Design: every quantity an exact
(numerator, denominator) integer pair held under 2^52; integer cross-multiplication
arithmetic; iterative-Euclid reduction with the gcd recorded as the reduction witness;
cross-multiplication comparisons, never division; longDiv digit expansion at displayed
precision, round-half-up, the rounding choice disclosed in the probe. The PASS gate:
a claim passes iff the fraction expands to exactly that digit string — no rounding
tolerance anywhere, floats nowhere in the value path. The seventh verification
paradigm of the series (after E80's integer-lane ledger, E81's double-entry, E82's
round-half-up display engine, E83-MC's two-prime modular residues, E84-IR's
outward-rounded interval containment, and E85-DC's dimension chains), chosen for what
the J2 injection demonstrated live: an "exactly equals" claim that merely rounds true
is refused at cross-multiplication — 495/611 against 81/100 decided at 49500 vs 49491.

## The honest history, entire

Probe rev-1 PASS 4/4 first run. Karat book rev-1 5/5 first run. Stoichiometry book rev-1
7/7 first run. Ferrofluid book rev-2 10/10 (rev-1 disclosed in the frozen header — the
B3-7 expectation literal divided by the FULL-batch theoretical and expected the
HALF-batch figure; the engine expanded the computed quantity correctly, the harness row
was wrong: the hand-literal slip class, the engine value path defect-free in both runs).
Bismuth book rev-2 6/6 (rev-1 a file-assembly defect — a block-slice off-by-one leaked
this book's header line into the ferrofluid book's sink and left this book headerless;
the six rows byte-identical in both assemblies, recomputed and re-expanded in rev-2).
Calendar book rev-2 5/5 (rev-1 disclosed — the harness pinned ALL four ages to the
23 Oct 2026 reference, but the register computed the N381/N397 ages at their own
24 Oct 2026 gather dates (batches 33cl/33cq), so B5-4/B5-5 FAILed at 2667/1036 against
the register's 2668/1037: harness reference errors, the engine's iterative day-number
walk defect-free in both runs; rev-2 re-seats the references per the register's
per-member gather dates). Economics book rev-1 5/5 first run, replayed byte-identical
for determinism. Injections rev-1 4/4 CAUGHT.

## Receipts

| File | md5 | Content |
|---|---|---|
| src.txt | 522a95a0e308fa7b08cf003986fe4f85 | design source, written to disk before any run |
| tP0.txt | 293a5f626c84b8309a50b30229494d56 | probe rev-1 PASS 4/4 |
| tB1.txt | 3c9de51d60a4129168cfbf66b7ba0f7d | karat book rev-1 5/5 |
| tB2.txt | 139558cbf69ef09afb5bb0f28494293c | stoichiometry book rev-1 7/7 (the B2-1 derived datum) |
| tB3.txt | e6791f98ac80cd7f5ab3f9aa2fab59a6 | ferrofluid book rev-2 10/10 (rev-1 harness literal in the header of record) |
| tB4.txt | 54c38a07f1b5bd78b35b8e74e94ba9c2 | bismuth book rev-2 6/6 (rev-1 assembly defect in the header of record) |
| tB5.txt | 0388125e5352d5464817dab6406f0241 | calendar book rev-2 5/5 (rev-1 reference-date errors in the header of record) |
| tB6.txt | 148f43f396c3157eed6fe586dd6c9c1f | economics book rev-1 5/5 (the determinism replay's reference file) |
| tJ.txt | e9528d714b04b7ad9120ef42df1b4457 | injections rev-1 4/4 CAUGHT |

## The transcripts, Outputs Verbatim

### Probe rev-1
E86-P0: the exact-fraction engine — probe rev-1, 4 rows
E86-P0: longDiv = round-half-up of (n/d)*10^k at integer precision (the rounding choice disclosed here; the truncation read of P3 would print 0.0999 — the printed figure 0.1000 is the rounded read, both named)
E86-P0: P1 | frac 99/20 | gcd-witness 5 | expansion 4.95 | expected 4.95 | PASS | 495/100 reduced; identity 99x100 = 9900 vs 495x20 = 9900
E86-P0: P2 | frac 10891/20 | gcd-witness 1 | expansion 544.55 | expected 544.55 | PASS | 54455/100 reduced
E86-P0: P3 | frac 1390/13901 | gcd-witness 1 | expansion 0.1000 | expected 0.1000 | PASS | scaled I = 1000 (0.1000 the rounded read; the truncation read 0.0999 named)
E86-P0: P4 | frac 51/5 | gcd-witness 1 | expansion 10.2 | expected 10.2 | PASS | 1020/100 reduced
E86-P0: census: rows 4 | PASS 4 | FAIL 0
E86-P0: verdict: PROBE 4/4 CLEAN

### Karat book rev-1
E86-B1: rev-1, 5 rows (round-half-up longDiv at displayed precision)
E86-B1: B1-1 | frac 471/25 | gcd-witness 1 | expansion 18.84 | expected 18.84 | PASS | 24 x 78.5% the AuAl2 mass fraction — the '18 karat' read
E86-B1: B1-2 | frac 486/25 | gcd-witness 1 | expansion 19.44 | expected 19.44 | PASS | 24 x 81% — the N397 'about 19 karat' read
E86-B1: B1-3 | frac 3/4 | gcd-witness 1 | expansion 0.75 | expected 0.75 | PASS | 18K = 18/24
E86-B1: B1-4 | frac 1/1 | gcd-witness 1 | expansion 1.00 | expected 1.00 | PASS | 24K = 24/24
E86-B1: B1-5 | frac 19/24 | gcd-witness 1 | expansion 0.79 | expected 0.79 | PASS | 19K = 19/24 (the repeating case — expansion at 2 places)
E86-B1: census: rows 5 | PASS 5 | FAIL 0
E86-B1: verdict: BOOK CLEAN

### Stoichiometry book rev-1
E86-B2: rev-1, 7 rows (round-half-up longDiv at displayed precision)
E86-B2: B2-1 | frac 19697/25093 | gcd-witness 1 | expansion 78.5 | expected 78.5 | PASS | Au mass fraction in AuAl2 = 196.97/250.93 — THE DERIVED DATUM: the patent recipe's 78.5 IS the intermetallic stoichiometry
E86-B2: B2-2 | frac 5396/25093 | gcd-witness 1 | expansion 21.5 | expected 21.5 | PASS | Al mass fraction in AuAl2 = 53.96/250.93 (the complement)
E86-B2: B2-3 | frac 1/1 | gcd-witness 1 | expansion 1.00 | expected 1.00 | PASS | the 100-g AuAl2 split sums to 1 exactly
E86-B2: B2-4 | frac 209/180 | gcd-witness 1 | expansion 1.16 | expected 1.16 | PASS | the recipe-consistent Al charge: 4.95 x 19/81 = 1.16 (the digit-transposition arbiter: 1.16 NOT 1.61)
E86-B2: B2-5 | frac 495/611 | gcd-witness 1 | expansion 81 | expected 81 | PASS | 4.95/(4.95+1.16) = 81% the recipe-consistent read (6.11 denominator)
E86-B2: B2-6 | frac 495/656 | gcd-witness 1 | expansion 75 | expected 75 | PASS | 4.95/(4.95+1.61) = 75% the caption-figure read (6.56 denominator) — the tension printed honestly
E86-B2: B2-7 | frac 12375/164 | gcd-witness 1 | expansion 75.46 | expected 75.46 | PASS | the caption read at 2 places = 75.46 (the exact figure for the chapter's tension table)
E86-B2: census: rows 7 | PASS 7 | FAIL 0
E86-B2: verdict: BOOK CLEAN

### Ferrofluid book rev-2
E86-B3: rev-2, 10 rows (rev-1 disclosed: the B3-7 expectation literal divided by the FULL-batch theoretical and expected the HALF-batch figure — the engine expanded the computed quantity correctly at 2.68, the harness row was wrong; zero engine-value-path defects in either run)
E86-B3: B3-1 | frac 270/811 | gcd-witness 1 | expansion 0.3329 | expected 0.3329 | PASS | 54 g FeCl3 / 162.20 = 0.3329 mol Fe3+ (the N340 charge)
E86-B3: B3-2 | frac 1390/13901 | gcd-witness 1 | expansion 0.1000 | expected 0.1000 | PASS | 27.8 g FeSO4·7H2O / 278.02 = 0.1000 mol Fe2+ (the hydration-state pin at printed precision)
E86-B3: B3-3 | frac 375327/112729 | gcd-witness 1 | expansion 3.33 | expected 3.33 | PASS | the charge ratio (54/162.2)/(27.8/278.02) = 3.33 vs the ideal 2.00 — THE N340 FAILURE ARITHMETIC
E86-B3: B3-4 | frac 2/1 | gcd-witness 1 | expansion 2.00 | expected 2.00 | PASS | the ideal 2:1 as a fraction = 2.00 (the requirement lane)
E86-B3: B3-5 | frac 3218267/139010 | gcd-witness 1 | expansion 23.15 | expected 23.15 | PASS | theoretical Fe3O4: (27.8/278.02) x 231.53 = 23.15 g (Fe2+ limiting, full batch)
E86-B3: B3-6 | frac 3218267/278020 | gcd-witness 1 | expansion 11.58 | expected 11.58 | PASS | the half-batch theoretical 23.15/2 = 11.58 g (the N340 in-source 'around 11.6' floor)
E86-B3: B3-7 | frac 17237240/3218267 | gcd-witness 1 | expansion 5.36 | expected 5.36 | PASS | the N340 yield 0.62 / the HALF-BATCH theoretical 11.576 = 5.36% (rev-2: the rev-1 expectation literal divided by the full-batch 23.15 and expected the half-batch figure — the hand-literal slip class, caught by the expansion; the engine value path defect-free in both runs)
E86-B3: B3-8 | frac 3/2 | gcd-witness 1 | expansion 1.50 | expected 1.50 | PASS | the steel-wool factor 3/2 = 1.50 (Fe + 2Fe3+ -> 3Fe2+, the N381 1.5x claim EXACT)
E86-B3: B3-9 | frac 51/5 | gcd-witness 1 | expansion 10.2 | expected 10.2 | PASS | the kerosene carrier 12 x 85% = 10.2 g (the N381 85%-of-mass recipe)
E86-B3: B3-10 | frac 8/8 | gcd-witness 8 | expansion L=R | expected L=R | PASS | the atom balance 2Fe3+ + Fe2+ + 8OH- -> Fe3O4 + 4H2O: integer pairs Fe 3=3, O 8=(4+4)=8, H 8=(4x2)=8 — L=R
E86-B3: census: rows 10 | PASS 10 | FAIL 0
E86-B3: verdict: BOOK CLEAN

### Bismuth book rev-2
E86-B4: rev-2, 6 rows (the rev-1 file-assembly defect disclosed: the block-slice off-by-one leaked this book's header line into tB3.txt and left tB4.txt headerless — the six rows byte-identical in both files; this rev-2 reassembly from the per-book sinks, rows recomputed and re-expanded, all PASS)
E86-B4: B4-1 | frac 13013/25 | gcd-witness 1 | expansion 520.5 | expected 520.5 | PASS | 271.4 °C in °F: 271.4 x 9/5 + 32 = 520.5 (the published °F figure)
E86-B4: B4-2 | frac 2583/25 | gcd-witness 1 | expansion 103.32 | expected 103.32 | PASS | the solidification expansion: 100 cm3 melt x (1 + 3.32%) = 103.32 cm3 solid (the water-like lane)
E86-B4: B4-3 | frac 3483/163 | gcd-witness 1 | expansion 21.37 | expected 21.37 | PASS | the bismuth molar volume 208.98/9.78 = 21.37 cm3/mol
E86-B4: B4-4 | frac 50000/489 | gcd-witness 1 | expansion 102.25 | expected 102.25 | PASS | a 1000-g knife melt occupies 1000/9.78 = 102.25 cm3 as liquid
E86-B4: B4-5 | frac 17220/163 | gcd-witness 1 | expansion 105.64 | expected 105.64 | PASS | the same 1000-g melt solid: 1000/9.78 x 1.0332 = 105.64 cm3 (the cast swells — the knife-maker's datum)
E86-B4: B4-6 | frac 6463/5 | gcd-witness 1 | expansion 1292.6 | expected 1292.6 | PASS | the liquid window: bp 1564 − mp 271.4 = 1292.6 °C wide
E86-B4: census: rows 6 | PASS 6 | FAIL 0
E86-B4: verdict: BOOK CLEAN

### Calendar book rev-2
E86-B5: rev-2, 5 rows (rev-1 disclosed: the harness pinned ALL four ages to the 23 Oct 2026 reference — the register computed the N381/N397 ages at their own 24 Oct 2026 gather date (batches 33cl/33cq), so B5-4/B5-5 FAILed at 2667/1036 vs the register's 2668/1037; the engine's iterative day-number walk defect-free in both runs, the two FAILs harness reference errors; rev-2 re-seats the references per the register's per-member gather dates)
E86-B5: B5-1 | dayNum(b) − dayNum(a) = 262 | expected 262 | PASS | the N340->N381 promise chain: 16 Oct 2018 -> 5 Jul 2019
E86-B5: B5-2 | dayNum(b) − dayNum(a) = 2157 | expected 2157 | PASS | the N321 age at its 23 Oct 2026 gather: 26 Nov 2020 -> 23 Oct 2026
E86-B5: B5-3 | dayNum(b) − dayNum(a) = 2929 | expected 2929 | PASS | the N340 age at the 23 Oct 2026 reference: 16 Oct 2018 -> 23 Oct 2026
E86-B5: B5-4 | dayNum(b) − dayNum(a) = 2668 | expected 2668 | PASS | the N381 age at its own 24 Oct 2026 gather date: 5 Jul 2019 -> 24 Oct 2026
E86-B5: B5-5 | dayNum(b) − dayNum(a) = 1037 | expected 1037 | PASS | the N397 age at its own 24 Oct 2026 gather date: 22 Dec 2023 -> 24 Oct 2026
E86-B5: census: rows 5 | PASS 5 | FAIL 0
E86-B5: verdict: BOOK CLEAN

### Economics book rev-1
E86-B6: rev-1, 5 rows
E86-B6: B6-1 | frac 26/19 | gcd-witness 1 | expansion 1.3684 | expected 1.3684 | PASS | the N397 exchange pair: 7800/5700 = 1.3684 CAD per US
E86-B6: B6-2 | frac 57/1 | gcd-witness 1 | expansion 57.00 | expected 57.00 | PASS | the 100-g bar at $5,700: 5700/100 = 57.00 $/g
E86-B6: B6-3 | frac 25/2 | gcd-witness 1 | expansion 12.50 | expected 12.50 | PASS | the N381 etchant: 50/4 = 12.50 $/L (the circuit-board FeCl3)
E86-B6: B6-4 | frac 2/1 | gcd-witness 1 | expansion 2.00 | expected 2.00 | PASS | the N340 small-lot premium at the bulk floor: 1.00/0.50 = 2.00x
E86-B6: B6-5 | frac 5/2 | gcd-witness 1 | expansion 2.50 | expected 2.50 | PASS | the N340 small-lot premium at the bulk ceiling: 1.00/0.40 = 2.50x
E86-B6: census: rows 5 | PASS 5 | FAIL 0
E86-B6: verdict: BOOK CLEAN

### Injections rev-1
E86-J: rev-1, 4 injection rows (each REQUIRED to be caught; a row is caught when the engine REFUSES the false claim and prints the true expansion)
E86-J: J1 | the claim 4.95/(4.95+1.61) = 81% | frac 495/656 | expansion 75.46% | cross-mul vs 81/100: -1 (not equal) | CAUGHT — the caption figure refuses the 81% read; the true expansion 75.46%
E86-J: J2 | the claim 495/611 = 81/100 EXACTLY (rounds-to-pass at 0 places, 80.99->81) | cross-mul 49500 vs 49491 | not equal | CAUGHT — the exact-identity claim refused at cross-multiplication (49500 != 49491): the no-tolerance paradigm's own gate
E86-J: J3 | the claim 81/24 = 3.375 is a mass fraction | frac 27/8 | expansion 3.375 | vs 1/1: greater (refused — a mass fraction cannot exceed 1) | CAUGHT — the inverted karat conversion refused at cross-multiplication
E86-J: J4 | the claim 2Fe3+ + Fe2+ + 8OH- -> Fe3O4 + 8H2O is balanced | O: 8 vs 12 | H: 8 vs 16 | unbalanced | CAUGHT — the doubled water coefficient refused at integer atom counts (O 8 vs 12)
E86-J: census: rows 4 | CAUGHT 4 | MISSED 0
E86-J: verdict: INJECTION BOOK CLEAN — all four caught
