# Engine 88 — E88-PA — the as-run design source (session 203)

The design source (src.txt rev-3, 2,942 B, md5 6d2d9aee2eea9ac221820501edf27cd7) was
written to disk BEFORE any rev-3 run — the Engine 82 source-loss lesson, standing
practice since E83. The rev-2 source (1,662 B, md5 d97eb14383a8bd6be33838b54a38ab46)
was itself written before any rev-2 run; its pmul contract sentence was honest but
unenforced, and the rev-3 text below replaces it with the enforced contract and the
full defect history. This file preserves the rev-3 source splice-verbatim.

---

# E88-PA rev-3 — THE PEASANT-ARITHMETIC ENGINE (Ch 56 review, session 203)

THE NINTH VERIFICATION PARADIGM. The engine bans the native multiply, divide,
and modulo operators from the value path entirely. Every multiplication goes
through pmul (Russian-peasant doubling: double the one operand while halving
the other, summing the rows where the halved operand is odd — the doubling
table itself kept as the witness). Every division goes through pdiv (binary
shift-subtract long division: double the divisor up, subtract back down,
returning quotient and remainder). Every printed figure goes through phalfUp
(scaled pdiv with half-up decided by remainder inspection, 2r >= d). Only
+, -, <<, >> and & appear in value arithmetic; the comparison lanes are the
same peasant algorithms run on independent decompositions. No floats, no
rounding tolerance, no recursion, no BigInt; all magnitudes held under 2^53.

pmul CONTRACT (rev-3, enforced): the halved operand is the one of smaller
magnitude and MUST be < 2^31 (JS bit-shift operators coerce to int32; an
out-of-range operand flips negative and ends the loop at once). rev-2 stated
the contract but never enforced it. rev-3 auto-swaps to the smaller
magnitude, THROWS if that magnitude is >= 2^31, and throws rather than let
the doubling side exceed the 2^53 exact-integer range. A silent zero can no
longer occur: the engine fails loud or not at all.

ENGINE DEFECT HISTORY (honest, disclosed):
- rev-2 defect, caught in the first C+D run: phalfUp(3447448000, ...) made
  pmul halve 3,447,448,000 >= 2^31; the int32 coercion turned it negative,
  the loop exited at once, pmul returned 0 silently, and the row printed a
  confident 0.00 verdict. The design contract existed from rev-1 but was
  unenforced — the engine's first and only value-path defect.
- rev-3: contract enforced (auto-swap, loud throws, 2^53 guards). Every book
  re-run under rev-3; the defective intermediate result never reached a
  verdict table.
Harness-side slips, separately disclosed, engine defect-free in each case:
probe rev-1 (three spec-scale calls), A+B rev-1 (B7 100x scale slip, B2 note
template token), C+D run 1 (C7 denominator x1000 vs x100 — the slip whose
impossible 0.00 verdict exposed the rev-2 engine defect — and D1 divisor
100 vs 5).

Verdict grammar (a review engine): PASS — the peasant lanes reproduce the
printed figure; OBJECTION SUSTAINED — the peasant lanes agree on a figure
the chapter does not print; REFUSED — an injection. The calendar runs
dual-lane as in E87 (closed-form leap-adjusted rata die against iterative
day-walk), every multiplication and division in both lanes peasant. Review
asymmetry: the engine does not verify itself; it verifies the chapter — the
review's question is whether the chapter's printed figures follow from the
chapter's own printed constants under an arithmetic that shares no code
path with the engine that drafted them (E86-XF).
