# Engine 75 Transcripts — E75-QS, the quarter-square engine (session 181, 2026-11-05)

Vol VII Ch 50 "Cubane" authoring unit — the P18 recognition chapter, the fence's own hardest case, mapped and never proceduralized. Fresh engine, zero code shared with Engines 1-74. Design: every quantity a sign, a base-100 little-endian limb array, and a decimal scale; every product in the entire value path — limb-convolution terms, digit carries, coefficient multiples — computed through the quarter-square identity (a+b)²−(a−b)² = 4ab against a precomputed square table SQ[0..400] built by odd-number accumulation, so the engine executes no multiplication operator anywhere, only additions, subtractions, table lookups, and halvings by two; schoolbook limb convolution in base 100; mulSmall for coefficients ≤ 99 only, guarded (the guard that fired at rev-0); pow10 by limb shifts; divmod by linear trial-digit limb long division that prepends each incoming dividend limb as a new low limb — a concatenation, never a multiply (the rev-0 lesson); half-up division decided at the target dp by the 2R ≥ D test on the true remainder; a 10¹⁸ limb guard that refuses rather than overflows; the P18 name gate first, admitting the restricted names only at recognition rank, plus the E75-D1 fence gate that refuses PROCEDURAL rows outright — the recognition chapter's own gate class; the held element table in micro-y units (C 120110, H 10080, N 140070, O 159990, S 320600, Na 229900, Cl 354530, Mg 243050, Br 799040, K 390980 — bromine and potassium admitted to the held table this session, the chapter's own element faces); the W1 float64 witness typed from independent decimal element weights, compared at the row's printed dp with a one-ulp boundary tolerance where float64 representation fails, the engine's decimal half-up authoritative; the digest PJW-ELF, 32-bit hex, distinct from E69's FNV-1a, E70's j31, E71's joat, E72's sdbm, E73's adler32, and E74's crc32, none reused; the chains by the month-table rank method — a cumulative-days table plus the leap rule, a third civil-date method where E73 used days_from_civil and E74 the Fliegel-Van Flandern JDN.

Honest run history: rev-0 the divmod base-shift used mulSmall(·,100) and the engine's own coefficient guard refused it ("mulSmall>99" — the engine catching its own primitive), fixed to a prepend-limb concat that multiplies nothing; rev-1 the W1 witness comparison compared the full-precision float to the dp-rounded print and failed nineteen s1 rows — a harness convention defect, fixed to compare at the row's printed dp; rev-2 the drafter's own hand-claim slips caught by the engine, the E73 lesson recurring in reverse — the engine caught the claims this time: the ketal divisor "seam" dissolved (101/128.171 = 0.7880, the register's own figure, no seam), the tribromoketal yield first claimed 45.85, the diacid first claimed 196.17 (true 192.17), the bromocyclopentadienone ketal first claimed 198.03 (true 203.04), the diacid moles first claimed 0.0561 (true 0.0572); rev-3 the T1/T2 checksums printed at the wrong scale (the g-sum instead of the myu-sum) and the percent-of primitive took its scale from the wrong end ("13178" at sc 1 = 1317.8, ten times the charge), and the same pass corrected the L07 hand claim to the engine's 45.84 (131.78/287.508892 = 45.8351% → half-up 45.84); rev-4 the W1 boundary case — 203.035 is not representable in float64, and Math.round's 203.03 disagreed with the engine's decimal half-up 203.04 — fixed to a one-ulp boundary tolerance at the printed dp with the engine's decimal lane authoritative, disclosed on the row; rev-5 the freeze-gate census caught the drafter's claim strings naming pins as new (ethylene glycol the Solvent Shelf's own pin at 62.068; Br₂ and HBr Chapter 43's pins at 159.808 and 80.912; dioxane named at the Chapter 45 owner's 88.106 print; toluene's mass never printed before, word priors only; the diacid's 192.170 colliding with FC3's PET repeat unit — same empirical formula C₁₀H₈O₄, a different molecule; methanol's mass pinned at Chapters 21/23; the L04/L05/L08 register-only claims under-naming what Chapter 43 already printed at 0.7880, 377.8, the 363→390 correction, 1.0323×) — claims corrected, battery re-run, the census's catches recorded never laundered. The sheets below are the frozen clean battery, written as they were generated (scratch is not storage) and spliced byte-verbatim.

Manifest: s0 the probe (8 PASS + 1 CAUGHT, the seeded truncation fault and the fence gate pair both exercised, elf 04887b8a); s1 the molar book (27/27 two-lane, T1 exact 40779380 myu, elf 0a01c08a); s2 the balances (12 PASS + 1 CAUGHT must-fail, T2 exact 44740870 myu, elf 0e42fe3a); s3 the charge ledger (16/16 two-lane, claims lane included, elf 08db6bda); s4 the fresh injections (8/8 CAUGHT, zero escaped, elf 0481ed6a); sR the register settlement (12/12 SETTLED, the chains by the month-table rank, elf 06d6c0ba); s5 determinism (the full battery double-executed byte-identical; G5 all six sheets' recorded elf digests recompute MATCH from disk; whole battery elf 09f7179a). Verdict: the frozen battery is the clean authoring run — every defect class caught before any row was accepted, nothing laundered; the Phase-3 adversarial review is the next session's unit.

---

```text
=== E75-QS s0 - the probe, rev-5 battery (2026-11-05) ===
PASS P1 | quarter-square division half-up: 2/3 at 3 dp | got 0.667 | expect 0.667
PASS P2 | exact tail: 1/8 terminates | got 0.125 | expect 0.125
PASS P3 | the quarter-square identity on a 18-digit product | got 121932631112635269 | expect 121932631112635269
PASS P4 | the half-up boundary: 0.125 at 2 dp | got 0.13 | expect 0.13
PASS P5 | the held table prices water at the book's own pin | got 18.015 | expect 18.015
PASS P6 | the month-table rank: the trilogy's arc | got 14/42 | expect 14/42
PASS P7 | the fence gate refuses a PROCEDURAL row (E75-D1) | got REFUSED | expect REFUSED
PASS P8 | the P18 name gate admits the restricted name only at recognition rank | got PASS | expect PASS
CAUGHT SF | the seeded truncation lane: trunc 0.66 vs half-up witness 0.67 - the witness caught it, as designed
s0 SUMMARY: 8 PASS, 1 CAUGHT (the seeded fault among them)
s0 elf: 04887b8a
```

```text
=== E75-QS s1 - the molar book (2026-11-05) ===
PASS M01 | C6H10O4 adipic acid | 146.1420 g/mol | prints 146.14 | W1 146.142 MATCH | NEW (146.142; zero-hit)
PASS M02 | C5H8O cyclopentanone | 84.1180 g/mol | prints 84.12 | W1 84.118 MATCH | NEW molecule; book basis 84.12 vs register basis 84.16 - both printed, never averaged
PASS M03 | C2H6O2 ethylene glycol | 62.0680 g/mol | prints 62.07 | W1 62.068 MATCH | Ch 45 pin 62.068 (the solvent shelf's dioxane feed), Ch 21 behind it
PASS M04 | C7H12O2 cyclopentanone ethylene ketal | 128.1710 g/mol | prints 128.17 | W1 128.171 MATCH | NEW (register 128.17; the ketal WORD at Ch 43's demand row)
PASS M05 | Br2 bromine | 159.8080 g/mol | prints 159.808 | W1 159.808 MATCH | Ch 43 pin 159.808 (x11, the bromine chapter), the element Br 79.904 at Ch 43/Ch 18
PASS M06 | C7H9Br3O2 2,2,5-tribromoketal | 364.8590 g/mol | prints 364.86 | W1 364.859 MATCH | NEW (register 364.86)
PASS M07 | H1Br1 hydrogen bromide | 80.9120 g/mol | prints 80.912 | W1 80.91199999999999 MATCH | Ch 43 pin 80.912 (x6), Ch 18 behind it
PASS M08 | C4H8O2 1,4-dioxane | 88.1060 g/mol | prints 88.11 | W1 88.106 MATCH | Ch 45 pin 88.106 printed at 2 dp here; the isomer face at Ch 21/23/24
PASS M09 | C13H10O benzophenone | 182.2220 g/mol | prints 182.22 | W1 182.222 MATCH | NEW (zero-hit word and mass)
PASS M10 | Na1H1O1 sodium hydroxide | 39.9970 g/mol | prints 39.997 | W1 39.997 MATCH | Ch 8 pin 39.997
PASS M11 | H2O4S sulfuric acid | 98.0720 g/mol | prints 98.072 | W1 98.072 MATCH | Ch 6 pin 98.072
PASS M12 | C7H8 toluene | 92.1410 g/mol | prints 92.14 | W1 92.14099999999999 MATCH | NEW mass (word priors Ch 35/41/47, the mass never printed before)
PASS M13 | C2H3N acetonitrile | 41.0530 g/mol | prints 41.05 | W1 41.053 MATCH | NEW (zero-hit)
PASS M14 | C4H8O2 ethyl acetate | 88.1060 g/mol | prints 88.11 | W1 88.106 MATCH | the dioxane isomer note; the isomer class at Ch 21/23/24
PASS M15 | C4H10O diethyl ether | 74.1230 g/mol | prints 74.12 | W1 74.12299999999999 MATCH | Ch 21 pin 74.123
PASS M16 | C7H7BrO2 the bromocyclopentadienone ketal | 203.0350 g/mol | prints 203.04 | W1 203.03499999999997 MATCH | NEW (203.035; zero-hit)
PASS M17 | C14H14Br2O4 the dimer diketal | 406.0700 g/mol | prints 406.07 | W1 406.06999999999994 MATCH | NEW (406.07; zero-hit)
PASS M18 | C10H6Br2O2 the diketone | 317.9640 g/mol | prints 317.96 | W1 317.964 MATCH | NEW (317.964; zero-hit)
PASS M19 | C8H8 cubane | 104.1520 g/mol | prints 104.15 | W1 104.15199999999999 MATCH | NEW molecule (104.152; the WORD at Ch 43, the neighbor-episode precedent), convergent 104.15
PASS M20 | C10H8O4 cubane-1,4-dicarboxylic acid | 192.1700 g/mol | prints 192.17 | W1 192.17 MATCH | NEW molecule; 192.170 = FC3's PET repeat-unit pin, same formula C10H8O4 - the named collision
PASS M21 | C12H12O4 dimethyl cubane-1,4-dicarboxylate | 220.2240 g/mol | prints 220.22 | W1 220.22400000000002 MATCH | NEW (220.224; zero-hit)
PASS M22 | C1H4O1 methanol | 32.0420 g/mol | prints 32.04 | W1 32.042 MATCH | Ch 21/23 pin 32.042, the word at Ch 47
PASS M23 | Na2O4S sodium sulfate | 142.0360 g/mol | prints 142.036 | W1 142.036 MATCH | Ch 13/14 pin 142.036
PASS M24 | K2C1O3 potassium carbonate | 138.2040 g/mol | prints 138.20 | W1 138.204 MATCH | pin 138.204 at Ch 14/Ch 20 + FC5
PASS M25 | Na1H1C1O3 sodium bicarbonate | 84.0060 g/mol | prints 84.01 | W1 84.006 MATCH | pin 84.006, the salt shelf's constant
PASS M26 | C1O2 carbon dioxide | 44.0090 g/mol | prints 44.009 | W1 44.009 MATCH | Ch 20 pin 44.009
PASS M27 | C8N8O16 octanitrocubane [RECOGNITION] | 464.1280 g/mol | prints 464.13 | W1 464.12800000000004 MATCH | NEW recognition-only (464.128; the fence row, zero-hit)
s1 SUMMARY: 27/27 MATCH two-lane (W1 agreement at the printed dp, boundary tolerance one ulp)
T1 composition checksum: 40779380 myu
s1 elf: 0a01c08a
```

```text
=== E75-QS s2 - the balances, atom-multiset + mass-ledger gated (2026-11-05) ===
PASS B01 | C6H10O4 -> C5H8O + C1O2 + H2O1 | atoms C6 H10 O4 = C6 H10 O4 | mass 146 = 146 myu | the catalytic decarboxylation, Ba(OH)2 above the arrow, recognition
PASS B02 | C5H8O + C2H6O2 -> C7H12O2 + H2O1 | atoms C7 H14 O3 = C7 H14 O3 | mass 146 = 146 myu | the ketal protection, the protect-before-bromination fence
PASS B03 | C7H12O2 + 3 Br2 -> C7H9Br3O2 + 3 H1Br1 | atoms Br6 C7 H12 O2 = Br6 C7 H12 O2 | mass 608 = 608 myu | the tribromination, three equivalents - the demand Ch 43 priced
PASS B04 | 2 C7H9Br3O2 + 4 O1H1 -> C14H14Br2O4 + 4 Br1 + 4 H2O1 | atoms Br6 C14 H22 O8 = Br6 C14 H22 O8 | mass 798 = 798 myu | the double dehydrohalogenation + spontaneous Diels-Alder dimerization
PASS B05 | C14H14Br2O4 + 2 H2O1 -> C10H6Br2O2 + 2 C2H6O2 | atoms Br2 C14 H18 O6 = Br2 C14 H18 O6 | mass 442 = 442 myu | the deketalization, the 20-25 C window row
PASS B06 | C10H6Br2O2 -> C10H6Br2O2 | atoms Br2 C10 H6 O2 = Br2 C10 H6 O2 | mass 318 = 318 myu | the photochemical [2+2] cycloaddition - an isomerization, the gate proves nothing is lost
PASS B07 | C10H6Br2O2 + 4 Na1H1O1 -> Na2C10H6O4 + 2 Na1Br1 + 2 H2O1 | atoms Br2 C10 H10 Na4 O6 = Br2 C10 H10 Na4 O6 | mass 478 = 478 myu | the double pseudo-Favorskii, ring contraction x2
PASS B08 | Na2C10H6O4 + 2 H1Cl1 -> C10H8O4 + 2 Na1Cl1 | atoms C10 Cl2 H8 Na2 O4 = C10 Cl2 H8 Na2 O4 | mass 309 = 309 myu | the acidification, the target designed to drop out
PASS B09 | C10H8O4 + 2 C1H4O1 -> C12H12O4 + 2 H2O1 | atoms C12 H16 O6 = C12 H16 O6 | mass 256 = 256 myu | the methyl ester, the unseen step priced at the ester
PASS B10 | C8H8 + 10 O2 -> 8 C1O2 + 4 H2O1 | atoms C8 H8 O20 = C8 H8 O20 | mass 424 = 424 myu | the strain face: the cube's combustion
PASS B11 | H1Br1 + Na1H1C1O3 -> Na1Br1 + C1O2 + H2O1 | atoms Br1 C1 H2 Na1 O3 = Br1 C1 H2 Na1 O3 | mass 165 = 165 myu | the workup's neutralization pair
PASS B12 | Br2 + 2 S2O3 -> 2 Br1 + S4O6 | atoms Br2 O6 S4 = Br2 O6 S4 | mass 384 = 384 myu | the thiosulfate wash, ionic redox at recognition - the reagent pinned at Ch 17/25's iodine faces
CAUGHT MF | the seeded B02 seed, water dropped | mass gap 18 myu = 18.015 g | the atom gate caught it, as designed
s2 SUMMARY: 12/12 balances PASS atom + mass gates, 1 CAUGHT must-fail
T2 product-mass checksum: 44740870 myu
s2 elf: 0e42fe3a
```

```text
=== E75-QS s3 - the charge ledger, two-lane + claims (2026-11-05) ===
PASS L01 | adipic acid charge 250 g at 146.142 | got 1.7107 | expect 1.7107 | claim: register 1.7107 mol
PASS L02 | cyclopentanone theoretical, machine basis 1.7107 x 84.118 | got 143.90 | expect 143.90 | claim: register basis 144.0 at 84.16 - both printed, never averaged
PASS L03 | the 104.8 g harvest, machine basis | got 72.83 | expect 72.83 | claim: register basis 72.78%, stated 73% - both round to it
PASS L04 | ketal moles, machine basis 101/128.171 | got 0.7880 | expect 0.7880 | claim: the register's own 0.7880, priced at Ch 43's demand row - the divisor rounds agree, no seam
PASS L05 | Br2 demand, machine basis 3 x 0.7880 x 159.808 | got 377.8 | expect 377.8 | claim: Ch 43 pin 377.8 (the gather-side check printed there); 390 g on hand
PASS L06 | tribromoketal theoretical, machine basis 0.7880 x 364.859 | got 287.5 | expect 287.5 | claim: register 287.5
PASS L07 | the 131.78 g tribromoketal, machine basis | got 45.84 | expect 45.84 | claim: the register's own 45.8% basis rounds the same way - all round to the stated 46
PASS L08 | the bromine self-correction 390 - 363 | got 27 | expect 27 | claim: exact; priced at Ch 43, the register's first cross-episode yield correction
PASS L09 | benzophenone charge 5.96 g | got 0.0327 | expect 0.0327 | claim: substoichiometric by design per the 2023 OBC paper
PASS L10 | the pseudo-Favorskii NaOH charge 85 g | got 2.1252 | expect 2.1252 | claim: the four-equivalent demand the mechanism lecture names
PASS L11 | the ~11 g diacid at its rank | got 0.0572 | expect 0.0572 | claim: from an approx, the rank printed with it - the adduct mass unseen upstream
PASS L12 | the strain face 695 kJ/mol over 12 C-C bonds | got 57.9 | expect 57.9 | claim: convergent 695, zero-hit as a datum (the bare 695s are substrings)
PASS L13 | the density face 104.152 g/mol at 1.29 g/cm3 | got 80.7 | expect 80.7 | claim: convergent 1.29, the densest hydrocarbon
PASS L14 | the octanitrocubane fence face C8N8O16 | got 464.13 | expect 464.13 | claim: recognition-only, the P18 gate owns the row
PASS L15 | the trilogy's arc by the month-table rank | got 14 / 28 / 42 | expect 14 / 28 / 42 | claim: 2024-01-13 / 01-27 / 02-24 EXACT
PASS L16 | the parent cube C8H8 | got 104.15 | expect 104.15 | claim: the parent the register's episodes never claim
s3 SUMMARY: 16/16 rows PASS two-lane
s3 elf: 08db6bda
```

```text
=== E75-QS s4 - eight fresh-keyed injections, every one must be CAUGHT (2026-11-05) ===
CAUGHT I01 | transposed molar mass 84.811 for cyclopentanone
CAUGHT I02 | the scale fault: adipic acid at 1461.42 g/mol
CAUGHT I03 | the broken atom gate: B03 with only 2 Br2
CAUGHT I04 | the over-100 yield: 131.78 g against a 115-g theoretical
CAUGHT I05 | the truncation lane: 0.125 truncated to 0.12
CAUGHT I06 | the half-mass slip: Br2 demand at half the ketal charge
CAUGHT I07 | the off-by-one chain: the trilogy's arc claimed 43 days
CAUGHT I08 | the fence gate: a PROCEDURAL row must be refused (E75-D1)
s4 SUMMARY: 8/8 CAUGHT, 0 escaped
s4 elf: 0481ed6a
```

```text
=== E75-QS sR - the register settlement (2026-11-05) ===
SETTLED R01 | N154's 104.8 g / stated 73% | SETTLED both bases: machine 72.83% at 84.118, register 72.78% at 84.16 - both round to the stated 73
SETTLED R02 | N155's 131.78 g / stated 46% | SETTLED: machine 45.84% at 131.78/287.5, the register's own 45.8% basis - all round to the stated 46
SETTLED R03 | the 390 g bromine on hand vs the 377.8 g stoichiometric | SETTLED: 1.0323x, Ch 43's own printed digit - a 3.2% excess the episode never claims as one
SETTLED R04 | the 27-g cross-episode correction | SETTLED exact: 390 - 363 = 27, priced at Ch 43 - the register's first in-source yield correction
SETTLED R05 | N156's 21.3 g diketone / stated 41% vs literature 93% | SETTLED as recorded, NOT independently checkable - the Diels-Alder adduct mass unseen, the register's own flag stands
SETTLED R06 | the ~11 g brown diacid | SETTLED at its rank: an approx, 0.0572 mol machine-side from it, the rank printed with it
SETTLED R07 | the 5.96 g benzophenone photosensitizer charge | SETTLED: 0.0327 mol, substoichiometric by design per the 2023 OBC paper
SETTLED R08 | the 85 g NaOH pseudo-Favorskii charge | SETTLED: 2.1252 mol, the four-equivalent demand the mechanism lecture names
SETTLED R09 | the trilogy's upload arc 2024-01-13 / 01-27 / 02-24 | SETTLED EXACT: 14 / 28 / 42 days by the month-table rank
SETTLED R10 | the production datums: 9 h distillation, 9 h filtrations x2, 25 GB, the two-week stir | SETTLED as recorded - production datums, no arithmetic owed
SETTLED R11 | the 155 C crude melt test | SETTLED as recorded - the instrumentless identity argument; no convergent literature mp pinned for the diketone, the comparison refused honestly
SETTLED R12 | the octanitrocubane forward question at the Part II comments | SETTLED at the fence: recognition-only forever, the P18 gate owns the row, no answer owed
sR SUMMARY: 12/12 SETTLED
sR elf: 06d6c0ba
```

```text
=== E75-QS s5 - determinism + the G5 disk gate (2026-11-05) ===
D1 | the full battery double-executed in-run: byte-identical
G5 | s0: recorded 04887b8a recomputed 04887b8a MATCH
G5 | s1: recorded 0a01c08a recomputed 0a01c08a MATCH
G5 | s2: recorded 0e42fe3a recomputed 0e42fe3a MATCH
G5 | s3: recorded 08db6bda recomputed 08db6bda MATCH
G5 | s4: recorded 0481ed6a recomputed 0481ed6a MATCH
G5 | sR: recorded 06d6c0ba recomputed 06d6c0ba MATCH
s5 SUMMARY: 10/10 - double-run byte-identical + all six sheets' recorded elf digests recompute MATCH from disk, same domain (the digest line excluded), strict equality
s5 elf: 0ddef52a
```
