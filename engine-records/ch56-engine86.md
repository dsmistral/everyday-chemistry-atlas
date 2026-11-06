# Engine 86 — E86-XF — design and verdict (session 201, Vol IX Ch 56)

**Engine 86** — the exact-fraction engine, fresh, sharing zero code with Engines 1-85.
Design: every quantity an exact rational — a (numerator, denominator) integer pair, both
magnitudes held under 2^52, no BigInt anywhere; all arithmetic integer cross-multiplication;
every result passes through reduce(), an iterative-Euclid gcd that records the gcd value
as the reduction witness; all comparisons cross-multiplication (a/b against c/d decided
by a*d against c*b — never by division); printed figures reproduced by longDiv, the
digit-by-digit integer expansion of the fraction at the displayed precision, round-half-up,
the rounding choice disclosed in the probe itself. The PASS gate: a claim passes iff the
fraction expands to exactly that digit string — the first engine in the series with no
rounding tolerance at all; floats appear nowhere in the value path. Deliberately distinct
from Engine 85's dimension chains (E85-DC), Engine 84's outward-rounded interval
containment, Engine 83's two-prime modular residues, Engine 82's round-half-up display
engine, Engine 81's double-entry, and Engine 80's integer-lane ledger: the seventh
distinct verification paradigm of the series, chosen for what the J2 injection
demonstrated live — the claim 495/611 = 81/100 "exactly" (it rounds there) refused at
cross-multiplication 49500 vs 49491, a figure every tolerance-based gate in the series
would have passed — and the J1 injection offered the video's own caption arithmetic
(4.95/6.56 = 81%) and was refused at the same gate, the true expansion 75.46% printed
in the refusal.

The battery, split into pieces per the binding runtime constraints, each piece's output
frozen to scratch with md5 receipts before any splice, never retyped; the design source
written to disk (src.txt, md5 522a95a0e308fa7b08cf003986fe4f85) BEFORE any run — the
Engine 82 source-loss lesson, standing practice since E83. The honest history, entire:
probe rev-1 PASS 4/4 first run; karat book rev-1 5/5 first run; stoichiometry book rev-1
7/7 first run; ferrofluid book rev-2 10/10 (rev-1 disclosed in the frozen header — the
B3-7 expectation literal divided by the FULL-batch theoretical and expected the
HALF-batch figure, the engine expanding the computed quantity correctly, the harness row
wrong: the hand-literal slip class, the engine value path defect-free in both runs);
bismuth book rev-2 6/6 (rev-1 a file-assembly defect — a block-slice off-by-one leaked
this book's header line into the ferrofluid book's sink and left this book headerless;
the six rows byte-identical in both assemblies, recomputed and re-expanded); calendar
book rev-2 5/5 (rev-1 disclosed — the harness pinned ALL four ages to the 23 Oct 2026
reference, but the register computed the N381/N397 ages at their own 24 Oct 2026 gather
dates (batches 33cl/33cq), so B5-4/B5-5 FAILed at 2667/1036 against the register's
2668/1037: harness reference errors, the engine's iterative day-number walk defect-free
in both runs; rev-2 re-seats the references per the register's per-member gather dates);
economics book rev-1 5/5 first run; injections rev-1 4/4 CAUGHT; determinism proven by
the byte-identical replay of the economics book against its frozen file.

Verdict: **PASS**. The figures this chapter's prose prints are the battery's rows: the
karat book (24 x 78.5% = 18.84, the "18 karat" read; 24 x 81% = 19.44, the "about 19
karat" read; 18K = 0.750; 19K = 0.790; 24K = 1.000); the stoichiometry book (196.97/250.93
= 78.5 — the derived datum: the patent recipe IS the AuAl2 stoichiometry; 53.96/250.93 =
21.5 the complement; the split sums to 1 exactly; 4.95 x 19/81 = 1.16, the
digit-transposition arbiter; 4.95/6.11 = 81% the recipe read; 4.95/6.56 = 75% and at two
places 75.46% the caption read — the tension printed honestly); the ferrofluid book
(54/162.20 = 0.3329 mol Fe3+; 27.8/278.02 = 0.1000 mol Fe2+; the charge ratio 3.33 vs
the ideal 2.00 — the N340 failure arithmetic; the theoretical 23.15 g, half-batch
11.58 g, yield 5.36%; the steel-wool factor 3/2 = 1.50, the N381 1.5x claim exact; the
kerosene 12 x 85% = 10.2 g; the atom balance L=R at integer pairs Fe 3=3, O 8=8, H 8=8);
the bismuth book (271.4 °C = 520.5 °F; 100 cm3 melt -> 103.32 cm3 solid; 208.98/9.78 =
21.37 cm3/mol; the 1,000-g melt 102.25 -> 105.64 cm3 — the cast swells, the
knife-maker's datum; the liquid window 1564 − 271.4 = 1292.6 °C); the calendar book (the
N340->N381 promise chain 262 days; the ages 2157 / 2929 / 2668 / 1037 at the register's
per-member gather dates); the economics book (7800/5700 = 1.3684 CAD per US; 5700/100 =
57.00 $/g; 50/4 = 12.50 $/L; the small-lot premiums 2.00x and 2.50x); the injections (the
caption's 81% refused for the true 75.46%; the rounding-tolerance confusion refused at
49500 vs 49491 — the no-tolerance paradigm's own gate; the karat inversion refused at
greater than 1/1; the doubled water coefficient refused at O 8 vs 12 — all four caught).

The transcripts, Outputs Verbatim, and the receipts: ch56-engine86-transcripts.md.
The as-run design source: ch56-engine86-src.md.
