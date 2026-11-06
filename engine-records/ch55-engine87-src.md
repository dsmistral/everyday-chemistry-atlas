# Engine 87 — E87-DL — the as-run design source (session 202)

The design source (src.txt, 1,933 B, md5 6fbdc7625a1ed6bd4cfac450fa57c446) was
written to disk BEFORE any run — the Engine 82 source-loss lesson, standing
practice since E83. This file preserves it splice-verbatim. The honest history
(Books A+B rev-1's three harness defects, the tAB census miscount with its
bash-counted correction, Book E rev-1's percent-scale slip, and the first replay's
transcription slip caught by the determinism gate, all disclosed) lives in
ch55-engine87-transcripts.md and ch55-engine87.md; the design below is the design
that produced the verdict rows.

# E87-DL — THE DUAL-LANE FIXED-POINT RECONSTRUCTION ENGINE (Ch 55 review, session 202)

THE EIGHTH VERIFICATION PARADIGM. Every constant is independently re-transcribed as a
scaled integer (fixed point; the per-row scale chosen so every intermediate stays
< 2^52, no BigInt anywhere); all arithmetic is integer arithmetic — the only division
is an exact integer division with quotient AND remainder both carried as witnesses;
rounding is half-up by remainder inspection at the displayed digit, never by float.
Every printed figure of the chapter under review is derived by TWO INDEPENDENT
LANES — different entry constants, or different operation orders, or a complementary
chain — and a row passes iff BOTH lanes agree at the displayed precision AND
reproduce the printed digit string. No tolerance, no float in the value path, zero
code shared with Engines 1-86.

THE REVIEW ASYMMETRY (this engine reviews a published chapter): a row carries the
chapter's printed figure as the claim. Verdicts: PASS (both lanes reproduce it),
OBJECTION SUSTAINED (both lanes reproduce a DIFFERENT figure — the printed one
fails), REFUTED (an objection row whose printed figure both lanes reproduce — the
objection dies). The transcript prints both lanes' witnesses on every row.

THE BOOKS: P probe; A the unit ladder (8 rows); B the expansion chain (5 rows,
the RF-1 candidate); C the displacement chain (7 rows, the RF-2/RF-3 candidates:
three mixing models, the printed-formula lane, the arithmetic-slip rows);
D the heat book (5 rows); E the economics book (8 rows); F the calendar book
(8 rows, integer day-walk vs closed-form leap-adjusted lane); J injections
(4 must-catch); R the replay (book E byte-identical against its frozen file).
Determinism: the E replay. All pieces iterative, exit 0; the census prints
counted rows; any SUSTAINED objection is printed honestly — this engine's job
is to find them, not to avoid them.
