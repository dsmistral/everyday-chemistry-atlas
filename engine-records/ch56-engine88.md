# Engine 88 — E88-PA — design and verdict (session 203, Vol IX Ch 56 review)

**Engine 88** — the peasant-arithmetic engine, fresh, sharing zero code with Engines
1–87. Design: the native multiply, divide, and modulo operators are banned from the
value path entirely. Every multiplication runs through pmul (Russian-peasant doubling —
double one operand while halving the other, summing the rows where the halved operand
is odd, the doubling table kept as the witness); every division through pdiv (binary
shift-subtract long division — double the divisor up in [d,1] pairs, subtract back
down, + only, quotient and remainder); every printed figure through phalfUp (the
scaled division n·10^s/d with half-up decided by remainder inspection, 2r ≥ d, the
q·d + r = N witness enforced on every call). The calendar runs dual-lane (closed-form
leap-adjusted rata die against an iterative day-walk stepping month lengths with
leap Februaries), both lanes peasant. No floats, no rounding tolerance, no recursion,
no BigInt; all magnitudes under 2^53, the halved operand under 2^31. Verdict grammar
built for a review: PASS (the peasant lanes reproduce the printed figure), OBJECTION
SUSTAINED (the lanes agree on a figure the chapter does not print), REFUSED (an
injection). Deliberately distinct from Engine 87's dual-lane fixed point, 86's exact
rationals, 85's dimension chains, 84's interval containment, 83's modular residues,
82's display rounding, 81's double-entry, and 80's integer lanes — the ninth distinct
verification paradigm of the series, chosen because a review that questions the
chapter's arithmetic must itself run on an arithmetic nothing else in the series
shares: not even the operators.

The battery, split into pieces per the binding runtime constraints, each piece's
output frozen to scratch with md5 receipts before any splice, never retyped; the
design source written to disk before any run (src.txt rev-3, 2,942 B, md5
6d2d9aee2eea9ac221820501edf27cd7; the rev-2 source, 1,662 B, md5
d97eb14383a8bd6be33838b54a38ab46, preserved by history in the rev-3 file) — the
Engine 82 source-loss lesson, standing practice since E83.

The verdict: PASS WITH CORRECTIONS. Books A–F, 39 rows, 39 PASS — karat 5/5, the
derived datum and the digit-transposition arbiter 7/7, ferrofluid stoichiometry
10/10, bismuth 6/6, calendar 5/5 with both lanes agreeing on all five day numbers,
economics 6/6 replayed byte-identical for determinism. Book G, the review hunt,
5 rows: 3 PASS, 2 OBJECTION SUSTAINED — RF-1 (the °F gloss: 2,200 °F is 1,204.44 °C,
not "about 1,100 °C") and RF-2 (the karat gap is 0.60 karat, 2.50% of mass, not
"one karat"). The injections 4/4 REFUSED. The corrected figures and the canon
re-grep record live in the chapter's Revision Appendix.

The honest history, entire. Harness-side slips, all disclosed in the frozen receipts
themselves: the probe's rev-1 fed three out-of-scale specs (the engine value path
defect-free in both runs); Books A+B rev-1 held a 100× scale slip (B7) and a
note-template token (B2); Books C+D run 1 held two spec slips (C7's denominator
×1000 against ×100, D1's divisor 100 against 5). And one engine value-path defect —
the first of E88, caught by its own impossible output: rev-2's pmul halved whichever
operand it was handed; fed a first argument ≥ 2^31, the JavaScript bit-shift
operators silently coerced it to int32, flipped it negative, and ended the loop at
once — pmul returned 0, and the C7 row printed a confident 0.00 verdict against a
printed 5.36. The design contract (halved operand < 2^31) had existed from rev-1;
rev-2 stated it and never enforced it. rev-3 enforces it — auto-swap to the
smaller-magnitude operand, a loud throw when no operand qualifies, exactness guards
on the doubling side — and every book, probe through injections, was re-run under
rev-3; the defective intermediate never reached a verdict table. The engine that
audits arithmetic was itself audited by its own arithmetic: the review's standard
applied to the review's own tools.
