# Engine 68 — the source record (session 174)

*The honest entry first: the E68-ML source was not durably saved before the session's platform compaction, and is lost as exact text — the session-170 class, the second consecutive engine to lose it (Engine 67 first). Nothing below is presented as the recovered source; nothing is reconstructed. What survives is the design specification (detailed enough to rebuild the engine and re-derive every transcript), the seven verbatim transcripts with their djb2 digests (previous file), and the frozen battery they re-verified. The rebuild contract: a fresh engine built to this spec must reproduce the seven digests byte-for-byte; if it does, the spec was complete; if it does not, the gap is named and the transcripts remain the authority.*

## The design specification (E68-ML, as built)

**Units.** The lattice is milligrams: charges in mg (integers — 314000, 39250, 53000, 39000, 600, 77000), molar masses in mg/mol (integers on the held-22 element basis — N2H4 32046, NaOCl 74442, N2H6SO4 130118, C4H8O 72107, C8H16N2 140230, and so on per Sheet 1). Every operand is an integer; no decimal enters any chain.

**Factor products.** A mole quantity is `charge_mg × 1e? / molar_mg` — assembled as a factor product on the lattice, never a hand-computed decimal: the engine multiplies first, divides last, and the division is the print lane's job, not the operand's.

**Dual print lanes.** `divP`: the classic round-half-up on the exact rational `(num × 10^k) / den` with `(2*num*10^k + den) / (2*den)` floor arithmetic. `subP`: the subtraction lane — the same value derived as a difference of lattice quantities, then printed with the identical round-half-up. Both lanes print per row; a disagreement fails the row (`sub:true` is the cross-proof flag).

**Witness lane.** `f:` — a float64 computation from plain decimal formulas, typed independently of the lattice, printed at the row's granularity and compared.

**Balance gates.** Each balance row builds both sides as atom multisets (exact integer element counts) and as distributive mass sums (each species = its atom multiset × the held-22 element masses, each side = the sum over its species). `atoms:true` gates the multiset; `lhs==rhs` gates the mass. An injection that breaks either fails before arithmetic is trusted.

**Negative-lane refusal (E68-D1).** Any lane whose print input is negative is refused — the row reports the refusal rather than printing. Inherited from Engine 67's printK defect as a design rule, not a repair.

**Digest lane.** djb2 (h = 5381; h = h*33 + c, charCode, over the transcript text without trailing newline), printed unpadded hex.

**Guards.** 9.0e15 magnitude guard on every intermediate; iterative only (no recursion); no BigInt; probe-first — the seeded must-fail (P5, the chlorine seam) must CAUGHT before any frozen row runs.

**Harness spec.** The per-sheet spec strings are dot-separated (the rev-1 comma separator collided with the formula lists' own commas and crashed the run; the repair is part of the honest history, and the separator rule is now part of the spec).

## The transcript-to-digest table (the rebuild target)

s0 3382edd6 (5 rows) · s1 561f70f7 (16) · s2 53d079c6 (6) · s3 29c0107a (19) · s4 ccae8581 (8) · s5 61199678 (54, twice, byte-identical) · sR 6e8cd8f3 (10). Transcripts verbatim in `ch46-engine68-transcripts.md` and in the chapter master's Revision Appendix.

## The protocol lesson (promoted)

An engine's source is written to scratch disk at build time — before the battery runs. Session 174 saved the transcripts (e68-s*.txt) but not the source, and the compaction took the source and left the transcripts: the asymmetry is the defect. From Engine 69 on, the source file is a deliverable of the build step, named in the engine record, and its md5 is printed at build time.
