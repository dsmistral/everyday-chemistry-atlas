# Engine 67 — the continued-fraction convergent engine (E67-CF)

*Session 173 (2026-11-04), the Vol VII Ch 46 "Hydrazine" authoring unit. Fresh build, zero code shared with Engines 1–66. The chapter's whole battery — the molar book, the balances, the lineage ledgers, the injection battery, the determinism proof — was computed by this engine and frozen into the master verbatim; this record, the transcripts file (`ch46-engine67-transcripts.md`), and the source/design record (`ch46-engine67-src.md`) are the durable record.*

## 1. Design

**One sentence:** every value in the battery is an exact rational held as its canonical continued-fraction expansion, reconstructed through the convergent lattice and certified row by row by the determinant identity — the CF IS the arithmetic.

- **The value lane:** exact rationals as canonical CF expansions (integer part, then partial quotients), convergent-lattice reconstruction computed iteratively (no recursion, no BigInt, no floats in the value path); the reconstruction's own **determinant identity pᵢqᵢ₋₁ − pᵢ₋₁qᵢ = (−1)^(i−1)** checked at every step as the machine witness (detW), plus a **CF roundtrip witness** (rt): expand → reconstruct → re-expand must reproduce the canonical expansion byte-identically.
- **The print lane:** round-half-up printing with a CF-native floor (the floor computed on the lattice, not by float truncation), at each row's stated precision.
- **The witness lane:** an independent float64 path (f:) from the original charges — sized to each row's printed granularity, agreement checked to the digit shown.
- **The balance gate:** atom-multiset equality plus exact rational mass equality on both sides (B-rows print `lhs==rhs`).
- **The digest lane:** sdbm over the transcript text, charCode lane, unpadded hex, text WITHOUT trailing newline (the Engine-66 convention, inherited).
- **Guards:** 9.0e15 magnitude guard on every intermediate; negative print lanes refused by design (D2 — see the run history); split pieces, no recursion, no BigInt, per the sandbox-runtime constraints.

## 2. The battery (frozen into the chapter verbatim)

- **s0 probe** (5 rows): N₂H₄ 32.046; the B1 balance 214.492; the yield fraction 0.2246; the −21.2 kJ couple; and the P5 must-fail (74.43 vs the frozen 74.44) — first run **4 PASS + 1 CAUGHT**, sdbm 6f01148c.
- **s1 + s2 — the molar book and the balances** (22 rows): sixteen species on the held-22 basis (N₂H₄ 32.046, NH₃ 17.031, NH₂Cl 51.476, CH₄N₂O 60.056, NaOCl 74.44, NaOH 39.997, NaCl 58.443, Na₂CO₃ 105.988, H₂SO₄ 98.072, N₂H₆SO₄ 130.118, C₄H₈O 72.107, C₈H₁₆N₂ 140.230, K₂CO₃ 138.204, CH₃ClN₂O 94.501, KCl 74.551, H₂O 18.015) and six balances (B1 214.492, B2 91.473, B3 68.507, B4 76.458, B5 176.260, B6 274.332). Rev-1: 20/22 — two dispatch slips engine-caught (S1-12: a JS numeric literal cannot hold the trailing zero, frozen printed "140.23"; B6: the hand-summed frozen 386.875 was never the sum — the true balanced mass is 274.332, atom-gated). Rev-2: **22/22**, sdbm 3301847f.
- **s3 + s4 — the lineage ledgers and the injection battery** (19 + 8 rows): the publication's ledger as computed (NaOCl 0.5273 mol limiting; NaOH 1.3251; urea 0.6494, 23% excess; MEK 1.0679; azine demand 76.04 g; ratio 1.0127; theoretical sulfate 68.61 g; stated 0.2246 mol = 42.60% NaOCl-basis / 34.59% urea-basis; NaCl 30.81 g; Na₂CO₃ 55.88 g; H₂SO₄ 36.56% excess; hydrazine fraction 24.63%; N fraction 21.53%; the meter 21226.7 J; the exposure conversion 1.3099; azine theoretical 73.94 g; gelatin 1.54%). Rev-1: 17/19 + 6 CAUGHT — two hand-frozen slips (L06 1.0126 → **1.0127**; L13 36.55 → **36.56**, the float witness right both times), one real kernel defect (L13's percent multiply mis-parenthesized into a negative, where printK rendered the malformed "-99.-63" — **D2: the negative lane is now refused by design**), and two omitted injections (I04/I07, a harness slip named on its rows). Rev-2: **19/19 + 8/8 CAUGHT**, sdbm 9a68a344.
- **s5 — determinism**: the full 54-row battery built twice in one run, byte-identical, **sdbm c98d820d both times**.

## 3. Honest run history

Nothing smoothed: the probe's own must-fail fired on the first run; rev-1's failures are printed in the transcripts file with their repairs named; the one kernel defect (the printK negative lane) was caught by the battery itself, fixed by refusal, and disclosed here; the drafter's hand slips (B6's 386.875; L06's 1.0126; L13's 36.55) were all overruled by the machine and the frozen values repaired BEFORE the master froze — the frozen battery is rev-2/s5, and the rev-1 transcripts are preserved as the record of how it got there.

## 4. Source durability

The source was NOT durably saved before the session's platform compaction and is lost as exact text — the session-170 class, disclosed per the honest-history rule; nothing reconstructed, nothing laundered. The design specification (sufficient to re-key a fresh engine) and the loss disclosure are in `ch46-engine67-src.md`; the transcripts and their digests are the verification anchors; the Phase-3 review's fresh engine (session 174) re-derives every row independently per the standing protocol.

*Engine 67 record — session 173, 2026-11-04. The labels are the contract in both directions.*
