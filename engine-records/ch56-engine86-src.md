# Engine 86 — E86-XF — the as-run design source (session 201)

The design source (src.txt, md5 522a95a0e308fa7b08cf003986fe4f85) was written to disk
BEFORE any run — the Engine 82 source-loss lesson, standing practice since E83. This file
preserves it splice-verbatim. The honest history (the ferrofluid book's rev-1 harness
literal, the bismuth book's rev-1 file-assembly defect, and the calendar book's rev-1
reference-date errors, all disclosed) lives in ch56-engine86-transcripts.md; the design
below is the design that produced the PASS rows.

# E86-XF — THE EXACT-FRACTION ENGINE (Ch 56, session 201)

THE SEVENTH VERIFICATION PARADIGM. Every quantity is an exact rational: a
(numerator, denominator) integer pair, |n| < 2^52 and 0 < d < 2^52 (double-safe,
no BigInt anywhere in the value path). All arithmetic (add, sub, mul, div) is
integer cross-multiplication; every result MUST pass through reduce(), an
iterative Euclid gcd with the gcd value recorded as the reduction witness; all
comparisons are cross-multiplication (a/b vs c/d decided by a*d vs c*b — never
by division). Printed figures are reproduced by longDiv(q, k): the digit-by-digit
integer expansion of the fraction to k decimals (n*10^k // d with the remainder
chain, all integers). PASS = the printed figure equals the longDiv expansion at
the displayed precision AND the reduction witness is recorded. Floats appear
NOWHERE in the value path: only in this file's design prose. Zero code shared
with Engines 1-85 (E85 chained dimensions; this engine chains nothing — every
row is an exact identity at full precision, the first engine in the series with
no rounding tolerance at all: a figure passes at 1/10000 only if the fraction
expands to exactly that digit string).

Decimal inputs enter as fromDecimal: "4.95" -> 495/100 exactly; "271.4" ->
2714/10 exactly. Atomic masses enter as fromDecimal at their published 2-decimal
precision (Au 196.97, Al 26.98, Fe 55.845->55845/1000, O 15.999->15999/1000,
Cl 35.45, S 32.06, H 1.008, FeCl3 162.20, FeSO4*7H2O 278.02, Fe3O4 231.53 —
the register's own machine-checked set, re-keyed fresh this session).

BOOKS (each a split piece <= 4 KB, scratch-file output, md5'd transcript):
- tP0 the probe: 4 rows (identity checks + one printed-figure reproduction).
- tB1 the karat ladder book: 24 x 78.5% = 18.84 (the "18 karat" read);
  24 x 81% = 19.44 (the "about 19 karat" read); 18K = 18/24 = 75%;
  24K = 24/24 = 100%; 19K = 19/24 = 79.17%.
- tB2 the AuAl2 stoichiometry book: 196.97/(196.97+2x26.98) = 196.97/250.93 =
  78.497...% -> the 78.5%/21.5% recipe AS THE INTERMETALLIC'S OWN MASS RATIO
  (the derived datum: the patent's "typical mixture" IS the AuAl2 stoichiometry,
  machine-derived here); the 100-g AuAl2 split 78.5/21.5; the N397 charge masses:
  4.95/(4.95+1.16) = 80.99...% -> the 81% recipe-consistent read; the caption
  figure 1.61: 4.95/(4.95+1.61) = 75.46...% (the digit-transposition tension,
  both expansions printed).
- tB3 the ferrofluid chemistry book: 54/162.20 = 0.3329 mol Fe3+;
  27.8/278.02 = 0.1000 mol Fe2+ EXACT; the ideal charge ratio 2:1 vs the actual
  0.3329/0.1000 = 3.329:1; 0.1000 mol x 231.53 = 23.1526 -> 23.15 g theoretical;
  the half-batch 23.1526/2 = 11.5763 -> 11.58 g; the yield 0.62/11.5763 = 5.356%
  -> 5.36%; the steel-wool factor 3Fe2+/2Fe3+ = 1.5 EXACT (Fe + 2Fe3+ -> 3Fe2+);
  the kerosene carrier 12 x 85% = 10.2 g EXACT; the atom balance witness
  2Fe3+ + Fe2+ + 8OH- -> Fe3O4 + 4H2O (integer atom pairs per side:
  Fe 3/3, O 8/8 (4 in Fe3O4 + 4 in 4H2O), H 8/8 — L = R at integers).
- tB4 the bismuth book: 271.4 + 273.15 = 544.55 K; 271.4 x 9/5 + 32 =
  520.52 -> the 520.5 F figure; the solidification expansion 100 x (1 + 332/10000)
  = 103.32 (the 3.32% lane); 208.98/9.78 = 21.37 cm^3 per mol (the molar-volume
  lane); the knife: a 1000-g bismuth melt -> 1000/9.78 = 102.25 cm^3 liquid ->
  105.65 cm^3 solid.
- tB5 the calendar book (the register's own dates re-derived at exact integers,
  iterative day numbers, no recursion): 16 Oct 2018 -> 5 Jul 2019 = 262 days
  (the N340->N381 promise chain); the gather-date ages at 23 Oct 2026:
  N321 26 Nov 2020 = 2157, N340 16 Oct 2018 = 2929, N381 5 Jul 2019 = 2668,
  N397 22 Dec 2023 = 1037.
- tB6 the economics book: 7800/5700 = 1.3684 CAD per US (the N397 pair);
  5700/100 = 57 $/g; the etchant 50/4 = 12.50 $/L; the N340 price datum
  1 $/mL small vs 0.40-0.50 $/mL bulk -> the 2.00-2.50x small-lot premium.
- tJ the injection book (4 must-fail rows, each REQUIRED to be caught):
  J1 the digit-transposition read served as fact: "4.95/(4.95+1.61) = 81%" —
  refused, the expansion is 75.46%;
  J2 an unreduced result accepted: 495/611 declared equal to 81/100 — refused,
  495x100 = 49500 vs 611x81 = 49491, cross-multiplication inequality;
  J3 the karat inversion: 81/24 = 3.375 served as a mass fraction — refused,
  > 1/1 at cross-multiplication;
  J4 the atom-balance slip: 2Fe3+ + Fe2+ + 8OH- -> Fe3O4 + 8H2O — refused,
  O: 8 vs 12 at integers.
Determinism: the tB6 replay must be byte-identical against its frozen transcript.
All pieces iterative, no recursion, exit 0; the census prints counted rows and
FAILs; any FAIL in a forward row or any UNCAUGHT injection = the book's verdict
FAIL, honestly printed.
