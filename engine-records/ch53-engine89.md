# Engine 89 — E89-DS — design and verdict (session 206, Vol VIII Ch 53, the Phase-3 review)

**Engine 89** — the decimal-string schoolbook engine, fresh, sharing zero code with
Engines 1–88 (E79 modular Gauss-Jordan GF; E80 integer-lane ledger; E81 double-entry;
E82 round-half-up display; E83 two-prime modular cross-check; E84 interval four-corner;
E85 the Ch 55 drafting engine; E86 exact fractions; E87 dual-lane fixed-point; E88
peasant arithmetic). Design: every quantity an exact decimal digit-string {digits, exp},
the value the digits times ten to the minus exponent; addition right-to-left with carry,
subtraction with borrow; multiplication as per-pair single-digit products from the
transcribed ten-by-ten times tables TL (low digit) and TH (high digit) — two hundred
literal entries, no arithmetic used to build them — with immediate column carry
propagation; division by compare-subtract long division, each quotient digit a
nine-step descent on schoolbook D x q over the bring-down digits of the padded dividend
(z = S + B.e − A.e scaling); truncation a digit slice, half-up the guard digit with a
schoolbook increment on the kept digits. No floats, no BigInt, no fractions, no modular
lane, no recursion anywhere in the value path; the battery sign-free (disclosed); the
element table independently re-transcribed from the standard values (H 1.008, C 12.011,
O 15.999, Na 22.990, Ca 40.078, S 32.065, Cl 35.450) and matched against the chapter's
held table. The tenth distinct verification paradigm in the series, chosen for the
review's own reason: a display audit that recomputes every printed figure from raw
digit strings cannot inherit any arithmetic habit from the drafting engine it audits.

The battery, split into pieces per the binding runtime constraints, each piece's output
frozen to scratch with md5 receipts before any splice, never retyped; the design source
written to disk (src.txt, md5 e009da3bc3bfa8efb90473cc8ee00cfe, 5,494 B) BEFORE any run.
The honest history, entire: probe rev-1 PASS 5/5 first run; molar book rev-1 22/22 first
run (ET re-transcription MATCH); balance book rev-1 7/7 first run; dose part 1 rev-1
9/9 PASS with a harness census defect (a hardcoded 7/7 printed over nine PASS rows — the
value path clean both runs; rev-2 identical rows, census corrected); dose part 2 rev-1
6/6 PASS whose deep lanes carried a transcription defect (below); review-hunt part A
rev-1 (RH1 objection SUSTAINED, RH2 displays robust, RH3 exact, RH4 floor note);
review-hunt part B rev-1 CRASHED (an undefined operand in the nested single-line RH6 lane
construction — TypeError, nothing written; rev-2 rebuilt the lane staged via the
balance-book species-list pattern); one defect caught at design review before any run
(the division scaling rule sign-flipped in the draft). The deepest catch: rev-2's RH5b
gate FAILED on an impossible lane (1.39999999 for 1,109,352/756,200), and the descent
found the freshly transcribed TH carry table's rows six and seven corrupted — 6x3
carrying 2 for 1, 7x4 carrying 3 for 2, 7x7 carrying 5 for 4 — three wrong entries in
two hundred; the dose part 2 rev-1 had carried the same row-seven defect silently in
two deep lanes beyond their display digits (D10's lane 99.99096999 for the true
99.99097093; D13's 4.86584269 for the true 4.86922413 — both display gates unaffected).
Both books re-run clean at rev-2/rev-3, the tables re-transcribed and self-checked
entry-by-entry against trivial literal single-digit arithmetic (200/200, a data-integrity
check outside the value path, disclosed), every display gate standing. The transcription,
never the algorithm, was the defect — and the gates caught it, which is the battery's own
best argument for its existence. Injections rev-1 4/4 CAUGHT (the Cl transposition, the
numerator splice, the display corruption, the decimal-point slip). Determinism PASS:
buildAll() (probe + the full dose book + the D12 refusal) run twice in-run, byte-identical,
sdbm 90944599 both runs.

Verdict: **PASS WITH CORRECTIONS — three findings, zero frozen-figure chemistry moved:**
RF-1 (Ex 53.1's truncation witness is 8 mg, the half-up excess 2 mg — the printed 3 mg
matches neither lane); RF-2 (Ex 53.3's denominator is the untruncated theoretical lane
21.91151 g, printed 21.91 — the displays robust, 82.6 / 83 under both lanes); RF-3 (the
Lecture 4 multiple 1.5/0.4 = 3.75 exact, gated of record); plus RH4 (the 15.38x
Madagascar multiple is a floor, premise ">$600/kg") and RH5 (the watch ratios: 2.6403
the half-up, truncation witness 2.6402; 1.4670 both displays, lane 1.46700872) as notes
of record. The corrections live in the chapter's Revision Appendix, extend-never-rewrite
honored.

The transcripts, Outputs Verbatim, and the receipts: ch53-engine89-transcripts.md. The
as-run source: ch53-engine89-src.md.
