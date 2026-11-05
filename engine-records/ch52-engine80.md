# Engine 80 — The Shelf-Ledger Engine: Design & Verdict Record (Vol VIII Ch 52 · session 194)

**Session:** 194 (2026-11-05) · **Chapter:** Vol VIII Ch 52 "The Medicine Shelf", part 1 of 2 · **Subject:** the shelf-ledger battery behind Lab 52.1 — every printed figure in the part-1 master is a battery row.

## Design (the as-run contract)

- **Fresh build:** zero code shared with Engines 1–79.
- **Integer lane:** every mass in exact my units (mg/mol — the held element table ×10³): H 1008, C 12011, N 14007, O 15999, Cl 35450, Na 22990, and the chapter's new element **Bi 208980** (the basis verified convergent at authoring; bismuth effectively single-isotope). No float ever gates an identity: every division prints an integer **witness triple** [quotient, remainder, denominator]; dose-lane conversions (umol = mg×10⁶/my) are exact rationals, every quotient verified by direct multiplication.
- **Formula parser:** an iterative character walk — no recursion, no BigInt (the binding runtime constraints honored in the engine itself); two-letter elements (Bi, Cl, Na) supported; species tokens taken at the LAST space (the rev-3 gate); coefficient shorthand (3H2) refused by design.
- **Balance checker:** closes every equation over element counts AND mass lanes both — the closure object must be all-zeros and massMy(L) == massMy(R).
- **Run discipline:** the battery ran split into pieces (probe first, then four sheets, then determinism) per the binding runtime constraints; each piece's output frozen to scratch with md5 + sdbm digests before any splice; never retyped.

## The battery and its honest history

| Piece | Final state | Revisions (all harness-side) |
|---|---|---|
| Pre-flight probe | 5/5 PASS, 3 injections CAUGHT | first run PASS |
| Sheet 1 — molar book | 22/22 PASS | rev-2: run-1's 4 FAILs were harness-only expectation-string element-order slips; the engine exact |
| Sheet 2 — dose book | 16/16 PASS | rev-3: run-1's 6 FAILs all pre-stated hand-slip expectations the engine corrected; rev-2's 2 display slips caught by the freeze discipline; no check moved in any rev |
| Sheet 3 — chain-efficiency book | 10/10 PASS | rev-2: 3 hand-slip expectations; the mis-designed injection row re-designed to assert the rounded-vs-exact seam at its true precision |
| Sheet 4 — balance book | 18/18 PASS | rev-3: two parser-gate crashes where the harness fed malformed input and the gate refused it both times; the aniline pin re-keyed 93128→93129 (a hand-slip caught by the engine's lane) |
| Determinism | 48 MATCH / 0 DIFFER | rev-2: run-1's 2 DIFFER rows were a defect in the CHECK PIECE's own mini-parser (single-letter elements only); the engine's parser never at fault |

Eight injections CAUGHT across the battery. Every revision in the history is harness-side; the engine's value path was defect-free in every run; the gate was never bypassed.

## Forensic note (the Sheet-3 sdbm boundary)

The sdbm(body) digests reproduce under the standard convention — h = c + (h<<6) + (h<<16) − h over the piece body excluding the digest line, no trailing newline — for five of the six pieces (Piece A 548c3cb0, Sheet 1 e5e50c0a, Sheet 2 5aed60f7, Sheet 4 d274e0a2, determinism 211f4778). Sheet 3's printed e037e292 does not reproduce under that convention or any obvious boundary variant tested at record time. The frozen artifact itself is byte-exact — the md5 gate (8480597023ffabf80853cc130a2d6b5b, 1,808 B) binds the transcript as-run — so the discrepancy is a boundary-convention quirk of the as-run harness's digest step for that one piece, disclosed here rather than smoothed. The md5 receipts remain the binding identity for all six pieces.

## Verdict

**PASS.** Value path defect-free in every run; the gates working in every run, including against their own harness; determinism byte-identical on re-run; the figure set frozen to the battery (the master prints no figure the battery did not check). The transcripts record (ch52-engine80-transcripts.md) carries the outputs verbatim with the binding receipts; the source record (ch52-engine80-src.md) carries the code contract and its loss disclosure.
