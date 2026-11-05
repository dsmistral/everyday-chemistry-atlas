# Engine 84 — E84-IR — the as-run design source (session 199)

The design source (src.txt, md5 405dc95de29c555d97cded722234fe5a) was written
to disk BEFORE any run — the Engine 82 source-loss lesson, standing practice
since E83. This file preserves it splice-verbatim. The honest history (the
balance book's rev-1/rev-2 harness defects, disclosed) lives in
ch54-engine84-transcripts.md; the design below is the design that produced
the PASS rows.

E84-IR — THE INTERVAL ENGINE (Vol VIII Ch 54, session 199)
THE FIFTH VERIFICATION PARADIGM: every quantity carried as an outward-rounded
interval [lo, hi] through strict worst-case arithmetic; a claim PASSES iff the
printed figure lies within the derived interval. Zero code shared with Engines
1-83 (E83-MC was modular residues; E84-IR is interval containment).
DESIGN (written to disk BEFORE any run, the E82/E83 lesson):
- interval = [lo, hi] pair; add = componentwise; sub = add with swapped operand;
  mul = the four-corner min/max over products; scale = mul by a point; div by a
  positive interval = four-corner; reciprocal of [a,b] = [1/b, 1/a].
- OUTWARD ROUNDING: each measured input gets its stated +- tolerance; derived
  bounds are only ever widened, never narrowed (no center-point tricks).
- PASS GATE: printed in [lo,hi]. FAIL names the row. No exceptions.
- BOOKS: B1 molar (the sunscreen axis: benzaldehyde/acetone/DBA, the 31.91-g
  theoretical, the 69.9% yield, the mp band); B2 balance (the soap axis: SAP
  190/256 mg-KOH/g, the 120.6-g KOH -> 86.0-g NaOH, the 80-g charge -> the 7%
  lye discount, the 40% w/v lye water); B3 dose/economics (SPF ladder 1-1/n,
  the 11/4 = 2.75 beads ratio, the buffer (25/294.10+12.2/192.12)/3 = 0.0495,
  the 60/3000 = 2.00% pretreat, the F->C ladder 2000/2400, the N396 336/2^7
  = 2.625 and 1300/2500 = 52%, the durations 22:39.46 s and 21:04.40 s, the
  stale ratios 2.9074/2.7378/1.3364/1.1157/2.0761).
- INJECTIONS J1-J4 MUST FAIL (be caught): J1 lo>hi swap; J2 a point used where
  the bracket is required (containment must still fail honestly when the claim
  is outside); J3 corrupted density 1.440 (digit slip) must violate the
  register-verified mol interval; J4 the F->C inversion (multiply-then-add) must
  disagree with the exact lane by more than any tolerance.
- DETERMINISM: the full battery re-run must be byte-identical (md5).
- PIECES: p0 probe, b1, b2, b3, j (injections), d (determinism). Scratch files
  under /home/user/e84/, transcripts md5-recorded, spliced programmatically.
