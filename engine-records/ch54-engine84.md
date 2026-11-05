# Engine 84 — E84-IR — design and verdict (session 199, Vol VIII Ch 54)

**Engine 84** — the interval engine, fresh, sharing zero code with Engines 1–83.
Design: every quantity carried as an outward-rounded interval [lo, hi] through
strict worst-case arithmetic — interval addition componentwise, multiplication
and division by the four-corner min/max rule, the reciprocal of [a,b] as [1/b,
1/a], each measured input entering at its stated ± tolerance, derived bounds
only ever widened, never narrowed. The PASS gate is containment: a claim passes
iff the printed figure lies within the derived interval; a FAIL names its row.
No recursion; no BigInt; floats permitted only as the display layer over exact
rational lanes. Deliberately distinct from Engine 83's modular residues, Engine
82's round-half-up display engine, Engine 81's double-entry, and Engine 80's
integer-lane ledger: the fifth distinct verification paradigm in the series,
chosen so a plausible-but-wrong point estimate (the J2 injection: 4.455 just
outside [2.333, 3.286]) is refused by the bracket rather than waved through on
authority, and a digit-slipped input (the J3 density 1.440) is caught by the
register-verified interval [0.3147, 0.3150] itself.

The battery, split into pieces per the binding runtime constraints, each
piece's output frozen to scratch with md5 receipts before any splice, never
retyped; the design source written to disk (src.txt, md5
405dc95de29c555d97cded722234fe5a) BEFORE any run — the Engine 82 source-loss
lesson, standing practice since E83. The honest history, entire: probe rev-1
PASS 2/2 first run; molar book rev-1 8/8 PASS first run; balance book rev-3 8/8
(rev-1 5/8 — three harness-side FAILs: the lye-discount interval composed in
the wrong order, f(x)=1−80/x increasing in x, the hand-composed division
bypassing the four-corner discipline building a reversed bracket, plus a
printed figure gated without its display-rounding window; rev-2 8/8 rows PASS
but the census printed 8/16, the denominator double-counted at the call site
and inside row() — the census-defect class, disclosed in the frozen header
itself; the engine's value path defect-free in every run); dose/economics
rev-1 18/18 PASS first run, the battery's largest single book; injections rev-1
4/4 CAUGHT; determinism proven by the byte-identical replay of the
dose/economics book against its frozen file.

Verdict: **PASS**. The figures this chapter's prose prints are the battery's
rows: the molar book (the sunscreen axis — benzaldehyde 0.3148 mol at [0.3147,
0.3150], acetone 0.1362 mol at [0.1361, 0.1363] limiting, the 2.31 regime,
the 31.91 g theoretical at [31.8881, 31.9285], the 22.3 g at 69.89 → 70
percent, the 109–111 mp inside the 110–112 literature band); the balance book
(the soap axis — the SAP-derived KOH demand 120.6 g at [120.0, 121.2], the
NaOH equivalent 86.0 g at [85.55, 86.41], the 80-g charge's ~7 percent lye
discount at [6.49, 7.42] — the E84-derived datum the episode never computed —
the 40.00 percent w/v lye water, the 880 g recipe sum, the 16.67 coconut
display window, the 52 percent liquid concentration); and the dose/economics
book (the SPF ladder 63.64 / 66.67 percent at 2.75 / 3, the 11/4 beads bracket
[2.333, 3.286] containing 2.75, the buffer 0.04950 M on the dihydrate/anhydrous
basis rounding to the stated 0.05, the 2.00 percent pretreat, the furnace
ladder 1093.3 / 1315.6 °C, the doubling rule 336/2^7 = 2.625, the duration pins
1359.46 / 1264.40 s, the five watch ratios 2.9074 / 2.7378 / 1.3364 / 1.1157 /
2.0761, the history-ladder gaps 33/8, and the 27→29 May inversion = 2 days).

The transcripts, Outputs Verbatim, and the receipts:
ch54-engine84-transcripts.md. The as-run design source: ch54-engine84-src.md.
