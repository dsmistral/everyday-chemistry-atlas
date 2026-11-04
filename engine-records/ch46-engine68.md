# Engine 68 — the milligram-lattice engine (E68-ML)

*Session 174 (2026-11-04), the Vol VII Ch 46 "Hydrazine" Phase-3 adversarial review unit. Fresh build, zero code shared with Engines 1–67. The review's charter: re-verify never re-author — the frozen battery's figures were the targets, every mismatch raised as a finding against the machine's chains, never a silent patch; every objection machine-verified before acceptance; the skeptic's own slips printed as faithfully as the drafter's.*

## 1. Design

**One sentence:** every quantity in the battery is an exact integer on a milligram lattice — charges in mg, molar masses in mg/mol — so no decimal ever enters an operand, and every printed figure is the lattice's own round-half-up.

- **The lattice lane:** exact integer mg units end to end; a product's operands are never hand-computed — a product is assembled from its factors on the lattice.
- **The print lanes (dual):** the direct division lane (divP) and the subtraction lane (subP), both round-half-up, cross-proven row by row (`sub:true`); at print precisions where the two lanes could disagree, the row fails rather than averages.
- **The witness lane:** an independent float64 path (`f:`) typed from plain formulas — sized to each row's printed granularity, agreement checked per row.
- **The balance gates:** atom-multiset equality (`atoms:true`) plus distributive mass lanes — each side of a balance summed from its species, each species from its atom multiset, both sides compared exactly (`lhs==rhs`).
- **The negative-lane refusal (E68-D1):** a lane that would print a negative value is a kernel defect, never a result — refused by design, the Engine-67 printK lesson inherited as a rule rather than a repair.
- **The digest lane:** djb2 over the transcript text, charCode lane, unpadded hex, text without trailing newline — distinct from Engine 67's sdbm, so the two engines' transcripts can never collide in the records.
- **Guards:** 9.0e15 magnitude guard on every intermediate; no recursion, no BigInt; probe-first (a seeded must-fail before any frozen row is trusted).
- **The harness spec separator:** dot (the rev-1 comma collision is run history, §3).

## 2. The battery (the frozen chapter battery re-verified)

- **s0 — the probe** (5 rows): 4 PASS + 1 CAUGHT — P5 the chlorine seam, the seeded digit slip caught at 74.43 against the frozen 74.44, the same seam Engine 67's probe caught; **djb2 3382edd6**.
- **s1 — Sheet 1, the molar book** (16 rows): 16/16 PASS, the S1-12 trailing-zero seam held at 140.23; **djb2 561f70f7**.
- **s2 — Sheet 2, the lineage's balances** (6 rows): 6/6 PASS — B1 214.492, B2 91.473, B3 68.507, B4 76.458, B5 176.260, B6 274.332, all atom-multiset-gated; **djb2 53d079c6**.
- **s3 — Sheet 3, the ledgers** (19 rows): 19/19 PASS on its first run — L01 0.5273, L02 1.3251, L03 0.6494, L04 1.0679, L05 76.04, L06 1.0127, L07 68.61, L08 0.2246, L09 42.60, L10 34.59, L11 30.81, L12 55.88, L13 36.56, L14 24.63, L15 21.53, L16 21226.7, L17 1.3099, L18 73.94, L19 1.54; **djb2 29c0107a**.
- **s4 — Sheet 4, fresh-keyed injections** (8 rows): 8/8 CAUGHT, no escapes — I01 the transposed chlorine (73.54), I02 the sulfur slip (130.108), I03 the wrong basis (42.88), I04 the halved condensation (104.153, atom gate), I05 the one-electron meter (10613.4), I06 the transposed chloramine (50.576), I07 the dropped NaCl (156.049, atom gate), I08 the over-counted azine (144.262); **djb2 ccae8581**.
- **s5 — Sheet 5, determinism**: the full 54-row battery built twice in-run — passOrCaught 54, byte-identical, **djb2 61199678 both passes**.
- **sR — the review sheet** (10 rows, the two-experts objections priced): 10/10 PASS — R01 39.38 g headroom, R02 57.40%, R03 1.4576 points/g (NaOCl basis), R04 1.1835 points/g (urea basis), R05 the urea ceiling by the exact chain 84.50, R06 by the rounded-mole product 84.50, R07 the L06 seam receipt (demand 76.0377, exact ratio 1.0127, rounded-demand hand division 1.0126), R08 the gelatin 1.54, R09 the meter 21226.7, R10 the conversion 1.3099; **djb2 6e8cd8f3**.

## 3. Honest run history

Nothing smoothed. **s5 rev-1 crashed:** the harness's spec separator was a comma, and the formula lists carry their own commas — the collision killed the run before a row printed; repaired to a dot separator, named in the s5 header. **sR rev-1 caught the drafter's own hand slip:** the frozen expectation R04 1.1834 was wrong — both print lanes and the float witness said 1.1835, the sensitivity dividing by the exact urea ceiling rather than its rounded print — repaired at rev-2 and named in the sheet's own header. And the review's one finding against the chapter itself: **RF-1**, a prose slip, not a battery row — Lecture 4's urea-basis ceiling printed "84.52 g," a figure no chain produces (both chains print 84.50, receipts R05/R06); corrected in the chapter's Revision Appendix per extend-never-rewrite, the body never edited. The battery itself: no frozen figure moved.

## 4. Source durability

The source was again not durably saved before the session's platform compaction — the session-170 class, twice running (Engine 67, then Engine 68). Disclosed per the standing discipline; nothing reconstructed as "the source." The durable record is this design specification, the seven verbatim transcripts (next file), and the djb2 digests. The protocol lesson promoted: an engine's source is written to scratch disk at build time, before the battery runs — the transcripts were saved, the source was not, and that asymmetry is the defect this entry exists to close.
