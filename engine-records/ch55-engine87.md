# Engine 87 — E87-DL — design and verdict (session 202, Vol IX Ch 55 review)

**Engine 87** — the dual-lane fixed-point engine, fresh, sharing zero code with Engines
1-86. Design: every claim recomputed twice in scaled-integer arithmetic — lane 1 the
direct scaled division (n*10^s/d, all integers), lane 2 an independent witness: the
quotient-and-remainder reconstruction (q*d + r == n) for the divisions, a partial-sum
rearrangement for the sums, and for the calendar a closed-form leap-adjusted rata die
against an iterative day-walk stepping month lengths with leap Februaries; half-up
rounding decided by remainder inspection (2r >= d), never by float; no floats in the
value path, no rounding tolerance, no recursion, no BigInt. Verdict grammar built for
a review: PASS (both lanes reproduce the printed figure), OBJECTION SUSTAINED (both
lanes agree on a figure the chapter does not print), REFUSED (an injection the engine
will not accept). Deliberately distinct from Engine 86's exact rationals, 85's
dimension chains, 84's interval containment, 83's modular residues, 82's display
rounding, 81's double-entry, and 80's integer lanes — the eighth distinct verification
paradigm of the series, chosen because a review's question is not "does the engine's
arithmetic reproduce itself" but "does any honest lane reproduce the chapter's printed
figure," and the answer, three times, was no.

The battery, split into pieces per the binding runtime constraints, each piece's
output frozen to scratch with md5 receipts before any splice, never retyped; the
design source written to disk (src.txt, 1,933 B, md5 6fbdc7625a1ed6bd4cfac450fa57c446)
BEFORE any run — the Engine 82 source-loss lesson, standing practice since E83. The
honest history, entire, harness-side defects all, disclosed in the frozen receipts
themselves: Books A+B rev-1 held a dual-lane comparison bug (A1), an s=0 format bug,
and Book B's 10x scale slip — all three fixed in-session, clean at rev-2; the frozen
tAB census line miscounts its own rows (the verdict token's trailing parenthetical
invisible to the count filter — "PASS 2, SUSTAINED 0" printed against its own 3 PASS
and 2 SUSTAINED rows; the authoritative counts bash-counted from the frozen rows,
the E84 census-defect class in its fourth costume); Book E rev-1's E8 fed the raw
fraction against the printed percent (fixed at rev-2, x100 scale); the first
determinism replay printed not-identical on its own lane1 token — an .out carried
into a string-returning halfUp copy, a transcription slip in the replay harness
caught by the determinism gate itself — the corrected replay byte-identical. The
engine's value path was never the defect; the chapter's figures were.

The verdict of record: probe 4/4 PASS first run; Book A (the unit ladder) 10 rows,
10 PASS — every temperature conversion reproduces, both lanes; Book B (the expansion
chain) 5 rows, 3 PASS, 2 OBJECTION SUSTAINED — RF-1; Book C (the displacement chain)
8 rows, 2 PASS, 6 OBJECTION SUSTAINED — RF-2 and RF-3; Book D (the heat chain) 5
rows, 5 PASS; Book E (the economics ledger) 8 rows, 8 PASS; Book F (the calendar)
8 rows, 8 PASS — the 217 correction of record re-derived a third time by two new
lanes; injections 4/4 REFUSED; determinism proven by the byte-identical replay of
Book E against its frozen file.

The chapter verdict: PASS WITH CORRECTIONS. RF-1: the expansion-band figures
(692.93/704.75 L) follow from neither lane of the chapter's own constants —
692.82/704.63 at full precision, 692.88/704.69 on displayed intermediates; the
corrected band [692.82, 704.63] still contains the dewar table's 1:696, the
headline survives. RF-2: the closet oxygen 17.4% follows only the additive model
(17.45% at two decimals); the chapter's own printed formula — the displacement
convention, confirmed convergent against the confined-space calculator lineage
(Vo = 0.2095 x (Vr - Vg)) — gives 16.76%, the figure the chapter's own Ex 55.2
worked line computes before bridging "16.76 = 17.4"; corrected 16.8%. RF-3: the
threshold room 9,651.6 L follows no lane — the additive model gives 9,651.5 (0.1
off even under its own model), the displacement convention 10,344.5-10,345.5 L;
Exercise 55.4's arithmetic doubly wrong (20.9 x 693 printed 14,533.7 against the
true 14,483.7, and 14,533.7/1.4 printed 9,651.6 against the true 10,381.2);
corrected ~10.3 m3. Every safety conclusion robust under all models: the closet
deficient and invisible either way, every model's threshold room in
[9,651.5, 10,345.5] L. The corrections live in the chapter master's Revision
Appendix, extend-only, the body untouched; no register correction of record this
session — RF-1 through RF-3 are chapter corrections, the register's rows standing.
