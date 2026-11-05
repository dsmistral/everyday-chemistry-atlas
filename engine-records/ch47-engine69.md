# Engine 69 — the exact-rational engine (E69-XR)

*Session 175 (2026-11-05), the Vol VII Ch 47 "The Amines and Odorants" authoring unit. Fresh build, zero code shared with Engines 1–68. The authoring charter: every claim machine-verified — the battery runs fresh before a figure is installed in the master; the machine's dual-lane values win every mismatch; honest history never laundered. And the durability lesson finally paid: the source was written to scratch disk at build time, before the battery ran — the first engine since the streak began (Engine 67, then Engine 68) whose source survives the session in full.*

## 1. Design

**One sentence:** every quantity is an exact rational [num, den] on an integer lattice — charges in micrograms, molar masses in mg/mol — and every printed decimal is the lattice's own long-division half-up, decided at the (k+1)-th generated digit.

- **The lattice lane:** charges in integer µg; molar masses in integer mg/mol on Chapter 3's held element table, plus the chapter's three convergent pins (Ni 58.693, Sn 118.710, Br 79.904 g/mol) and the aniline density pin 1.0217 g/mL. No decimal ever enters an operand.
- **The print lanes (dual):** DS — long division, half-up decided at the (k+1)-th generated digit; XR — the exact rational itself, gcd-reduced (iterative Euclid) and printed as the reduced fraction; FL — an independent float64 recomputation from a separate decimal table, sized to the row's printed granularity. The printed figure must agree with both witnesses or the row FAILS.
- **The balance gates:** atom-multiset equality plus distributive mass sums, both sides, both must agree (the mg/mol lane: e.g. the Fischer gate's 166224 vs 166224).
- **The verdict gates priced into the battery:** CONTAMINATED (> 100%) and the limiting-reagent correction are engine outputs, not hand notes.
- **The negative-lane refusal (E69-D1):** a lane that would print a negative value is refused by design.
- **The digest lane:** FNV-1a 32-bit (h = 2166136261; h ^= c; h = imul(h, 16777619)) over the transcript text, unpadded hex — distinct from Engine 68's djb2 and Engine 67's sdbm, so no engine's transcripts can collide in the records.
- **Guards:** 9.0e15 magnitude guard on every stored integer; iterative only — no recursion, no BigInt, no eval; probe-first (the seeded must-fail runs before any frozen row is trusted).

## 2. The battery

- **s0 — the probe** (5 rows): 4 PASS + 1 CAUGHT — P1 NaCl on the held table (M = 58.440), P2 the half-up seam (5/4 at 1 dp = 1.3), P3 the trailing-zero seam (0.0050), P4 the Fischer gate's atom multiset, P5 the seeded chlorine fault (Cl = 35.540 asserted; 58530 vs the machine's 58440); **fnv f673fc2c**.
- **s1 — the molar book** (30 rows): 30/30 PASS — ornithine 132.163, ornithine·HCl 168.621, putrescine 88.154, lysine 146.190, lysine·HCl 182.648, 5-aminopentanenitrile 98.149 … capsaicin 305.418 (Chapter 34's own pin, re-pinned here); **fnv 43e28034**.
- **s2 — the lineage's balances** (8 rows): 8/8 PASS — B1 the ornithine decarboxylation, B2 the lysine decarboxylation, B3 the nitrile hydrogenation, B4 the Fischer indole gate (C6H8N2 + C3H6O), B5 the diazotization, B6 the SnCl2 reduction, B7 the oxime condensation, B8 the amide condensation (capsaicin itself, 323433 vs 323433 mg/mol); **fnv 23a80262**.
- **s3 — the lineage ledgers** (33 rows): 33/33 PASS — L03 putrescine theoretical 0.6796 g, L09 cadaverine theoretical 1.9748 g (the HCl-form charge basis), L10 cadaverine yield 25.32%, L11 the ruled-out lysine free-base mis-basis 2.4673 g named as a refused lane, L33 the pair's 56.0× time economy; **fnv 2e281538**.
- **s4 — fresh-keyed injections** (8 rows): 8/8 CAUGHT, 0 escaped — I01 the transposed ornithine charge, I02 the free-base mis-basis, I03/I06/I08 broken atom gates, I04 the equivalents slip (8 g = 2.298 eq), I05 the > 100% CONTAMINATED verdict, I07 the wrong-basis oxime yield (vanillin is limiting; the vanillin-basis yield = 82.19%); **fnv 24f6b768**. Cosmetic, named: the summary counter prints "caught 9" for 8 rows — it counts the header's own word "CAUGHT"; the per-row verdicts are the authority.
- **s5 — determinism**: the full battery built twice in-run — byte-identical, **fnv d3448d97 both passes**, 10,307 bytes both.
- **sR — the literal-settlement sheet** (10 rows, rev-2): 10/10 PASS — R01 0.6796, R02 1.9748, R03 25.32%, R04 0.6065 (the register's 0.607 named as the double-round), R05 7.2974, R06 137.03%, R07 10.7671, R08 82.19%, R09 0.926, R10 92.86%; **fnv e2ddb6cf**.

## 3. Honest run history

Nothing smoothed. **sR rev-1 caught FIVE hand-frozen drafter expectation slips** — R01 0.6797→0.6796, R02 1.9750→1.9748, R05 7.2959→7.2974, R06 137.01→137.03, R07 10.7680→10.7671 — the machine's dual-lane values won on every one, the FL witness agreeing on all ten rows; corrected at rev-2 and named in the sheet's own header (rev-1 preserved verbatim below). The s4 counter cosmetic is named above. **The freeze-gate census caught the drafter's own prose:** the "three new convergent pins" were not new — Ni 58.693 is Chapter 12's pin, Sn 118.710 Chapter 11's, Br 79.904 admitted at Chapter 18, capsaicin 305.418 Chapter 34's own — re-pinned, not admitted; the master's status paragraph, Lecture 0, the Lab 47.1 purpose line, the Canon-Coverage Check, and the Sources element-basis bullet were all corrected to say so before the freeze. And the intro's "five performers' hands" was corrected to "one performer's channel" before the freeze — all nine episodes are NileRed's.

## 4. Source durability

The streak is broken. Engine 67's source was lost at the session-170-class compaction; Engine 68's was lost the same way a session later; the E68 record closed with the promoted protocol lesson — an engine's source is written to scratch disk at build time, before the battery runs. Engine 69 is the first to execute that lesson: the source was saved at build time (24,009 bytes, md5 433a602a9b19490a4cf73773f174c351) and is reproduced verbatim in the source record, the third file of this set. No reconstruction, no design-specification-as-source: the actual code, the whole code.
