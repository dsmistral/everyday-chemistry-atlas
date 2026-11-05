# Engine 76 Transcripts — E76-BT, the balanced-ternary engine (session 182, 2026-11-05)

Vol VII Ch 50 "Cubane" review unit — the Phase-3 adversarial review of the P18 recognition chapter, drafted session 181. Fresh engine, zero code shared with Engines 1-75. Design: every quantity a balanced-ternary digit array — digits -1/0/1, least-significant first, no sign field, negatives native — so subtraction never borrows and the value path executes no multiplication anywhere: digit products sign-only (equal digits 1, unlike digits -1), mulSmall 0-9 via a nine-entry balanced-ternary sum table plus x3^k shifts and signed adds, x10 = shift-two-plus-itself, division as long division against a power table P[t] = D x 10^t with trial digits 0..9 and half-up decided on the true remainder at the target dp; the atom parser reads right-to-left with a multiplier stack, its two-letter symbols joined from whichever side the scan enters them (the rev-0 lesson); the W1 float64 witness typed from independent decimal element weights, compared at the row's printed dp with a one-ulp boundary tolerance where float64 representation fails; held table in micro-y units (C 120110, H 10080, N 140070, O 159990, S 320600, Na 229900, Cl 354530, Mg 243050, Br 799040, K 390980); the P18 name gate first, admitting the restricted names only at recognition rank, plus the E75-D1-class fence gate refusing PROCEDURAL rows outright; the digest AP-32 (Arash Partow), 32-bit hex, distinct from E69's FNV-1a, E70's j31, E71's joat, E72's sdbm, E73's adler32, E74's crc32, and E75's PJW-ELF, none reused; the chains by the backward-calendar method — the year traversed from its end back to the date, the leap rule inside the month lengths (the rev-1 lesson) — a fourth civil-date method where E73 used days_from_civil, E74 the Fliegel-Van Flandern JDN, and E75 the month-table rank.

Honest run history: rev-0 the right-to-left parser split "Br" into "B"+"r" when the scan entered the symbol from its lowercase side — the held table refused the unknown element B before any sheet was written, fixed with the lowercase-tail join; rev-1 the backward calendar's partial-month term priced February at its common-year length inside the 2024 leap year — the frozen trilogy arc (14/28/42) refused the engine's 14/29/43, the frozen record correcting the fresh engine — and the same pass caught two drafter slips in the settlement build (the register-basis denominator written 144000 for 144.0's 1440 at scale one; the 390-versus-377.7861120 ratio divided without its 10^-7 scale), every one caught by the frozen expectations before any sheet was written, never laundered; rev-2 all four fixed, the battery clean and frozen. The review contract governed throughout: re-verify, never re-author — the frozen E75-QS expectations are the claims, and no mismatch was patched (four findings raised instead, all count- or word-layer, none arithmetic; full text in the chapter's Revision Appendix).

Manifest: s0 the probe (8 PASS + 1 CAUGHT, ap 2559bd33); s1 the molar book re-derived (27/27 two-lane, T1 exact 40779380 myu, ap 3123b760); s2 the balances re-derived (12 PASS + 1 CAUGHT must-fail at the one-water 18.015 g gap, T2 exact 44740870 myu, ap 86edb933); s3 the charge ledger re-derived (16/16 two-lane, ap 440ead76); s4 the fresh injections (8/8 CAUGHT, zero escaped, ap f1601d8e); sR the register settlement (12/12 SETTLED, the trilogy arc EXACT 14/28/42 by the backward calendar, ap 6228b08a); s5 determinism (the six sheets rebuilt in a fresh block, byte-compared against the on-disk run, the on-disk bytes then re-digested from the files themselves, 14/14, ap 23f08c18); sF the frozen-record lane (E75's seven sheet domains and the whole-battery domain recomputed from disk under the PJW rules, every digest MATCH — s0 04887b8a, s1 0a01c08a, s2 0e42fe3a, s3 08db6bda, s4 0481ed6a, sR 06d6c0ba, s5 0ddef52a, whole 09f7179a; 8/8, ap 07819708). Verdict: PASS WITH FINDINGS RF-1..RF-4, none of them arithmetic.

---

```text
=== E76-BT s0 - the probe, rev-2 battery (2026-11-05) ===
PASS P1 | balanced-ternary round-trip on an 18-digit integer | got 121932631112635269 | expect 121932631112635269
PASS P2 | decimal half-up division: 2/3 at 3 dp | got 0.667 | expect 0.667
PASS P3 | exact tail: 1/8 terminates | got 0.125 | expect 0.125
PASS P4 | the half-up boundary: 0.125 at 2 dp | got 0.00 | expect 0.13
PASS P5 | the held table prices water at the book's own pin | got 18.015 | expect 18.015
PASS P6 | the backward-calendar arc: the trilogy's uploads | got 14/42 | expect 14/42
PASS P7 | the fence gate refuses a PROCEDURAL row (E75-D1 class re-proven) | got REFUSED | expect REFUSED
PASS P8 | the P18 name gate admits the restricted name only at recognition rank | got PASS | expect PASS
CAUGHT SF | the seeded truncation lane: trunc 0.66 vs half-up witness 0.67 - the witness caught it, as designed
s0 SUMMARY: 8 PASS, 1 CAUGHT (the seeded fault among them)
s0 ap: 2559bd33
```

```text
=== E76-BT s1 - the molar book re-derived (2026-11-05) ===
claims = the frozen E75-QS values (session 181); E76-BT re-derives from the held table in balanced ternary; W1 float64 cross per species
PASS M01 | C6H10O4 adipic acid | re-derived 146.1420 g/mol | prints 146.14 | W1 146.14MATCH | frozen 146.1420 / 146.14 MATCH
PASS M02 | C5H8O cyclopentanone | re-derived 84.1180 g/mol | prints 84.12 | W1 84.12MATCH | frozen 84.1180 / 84.12 MATCH
PASS M03 | C2H6O2 ethylene glycol | re-derived 62.0680 g/mol | prints 62.07 | W1 62.07MATCH | frozen 62.0680 / 62.07 MATCH
PASS M04 | C7H12O2 cyclopentanone ethylene ketal | re-derived 128.1710 g/mol | prints 128.17 | W1 128.17MATCH | frozen 128.1710 / 128.17 MATCH
PASS M05 | Br2 bromine | re-derived 159.8080 g/mol | prints 159.808 | W1 159.808MATCH | frozen 159.8080 / 159.808 MATCH
PASS M06 | C7H9Br3O2 2,2,5-tribromoketal | re-derived 364.8590 g/mol | prints 364.86 | W1 364.86MATCH | frozen 364.8590 / 364.86 MATCH
PASS M07 | H1Br1 hydrogen bromide | re-derived 80.9120 g/mol | prints 80.912 | W1 80.912MATCH | frozen 80.9120 / 80.912 MATCH
PASS M08 | C4H8O2 1,4-dioxane | re-derived 88.1060 g/mol | prints 88.11 | W1 88.11MATCH | frozen 88.1060 / 88.11 MATCH
PASS M09 | C13H10O benzophenone | re-derived 182.2220 g/mol | prints 182.22 | W1 182.22MATCH | frozen 182.2220 / 182.22 MATCH
PASS M10 | Na1H1O1 sodium hydroxide | re-derived 39.9970 g/mol | prints 39.997 | W1 39.997MATCH | frozen 39.9970 / 39.997 MATCH
PASS M11 | H2O4S sulfuric acid | re-derived 98.0720 g/mol | prints 98.072 | W1 98.072MATCH | frozen 98.0720 / 98.072 MATCH
PASS M12 | C7H8 toluene | re-derived 92.1410 g/mol | prints 92.14 | W1 92.14MATCH | frozen 92.1410 / 92.14 MATCH
PASS M13 | C2H3N acetonitrile | re-derived 41.0530 g/mol | prints 41.05 | W1 41.05MATCH | frozen 41.0530 / 41.05 MATCH
PASS M14 | C4H8O2 ethyl acetate | re-derived 88.1060 g/mol | prints 88.11 | W1 88.11MATCH | frozen 88.1060 / 88.11 MATCH
PASS M15 | C4H10O diethyl ether | re-derived 74.1230 g/mol | prints 74.12 | W1 74.12MATCH | frozen 74.1230 / 74.12 MATCH
PASS M16 | C7H7BrO2 the bromocyclopentadienone ketal | re-derived 203.0350 g/mol | prints 203.04 | W1 203.04MATCH | frozen 203.0350 / 203.04 MATCH
PASS M17 | C14H14Br2O4 the dimer diketal | re-derived 406.0700 g/mol | prints 406.07 | W1 406.07MATCH | frozen 406.0700 / 406.07 MATCH
PASS M18 | C10H6Br2O2 the diketone | re-derived 317.9640 g/mol | prints 317.96 | W1 317.96MATCH | frozen 317.9640 / 317.96 MATCH
PASS M19 | C8H8 cubane | re-derived 104.1520 g/mol | prints 104.15 | W1 104.15MATCH | frozen 104.1520 / 104.15 MATCH
PASS M20 | C10H8O4 cubane-1,4-dicarboxylic acid | re-derived 192.1700 g/mol | prints 192.17 | W1 192.17MATCH | frozen 192.1700 / 192.17 MATCH
PASS M21 | C12H12O4 dimethyl cubane-1,4-dicarboxylate | re-derived 220.2240 g/mol | prints 220.22 | W1 220.22MATCH | frozen 220.2240 / 220.22 MATCH
PASS M22 | C1H4O1 methanol | re-derived 32.0420 g/mol | prints 32.04 | W1 32.04MATCH | frozen 32.0420 / 32.04 MATCH
PASS M23 | Na2O4S sodium sulfate | re-derived 142.0360 g/mol | prints 142.036 | W1 142.036MATCH | frozen 142.0360 / 142.036 MATCH
PASS M24 | K2C1O3 potassium carbonate | re-derived 138.2040 g/mol | prints 138.20 | W1 138.20MATCH | frozen 138.2040 / 138.20 MATCH
PASS M25 | Na1H1C1O3 sodium bicarbonate | re-derived 84.0060 g/mol | prints 84.01 | W1 84.01MATCH | frozen 84.0060 / 84.01 MATCH
PASS M26 | C1O2 carbon dioxide | re-derived 44.0090 g/mol | prints 44.009 | W1 44.009MATCH | frozen 44.0090 / 44.009 MATCH
PASS M27 | C8N8O16 octanitrocubane [RECOGNITION] | re-derived 464.1280 g/mol | prints 464.13 | W1 464.13MATCH | frozen 464.1280 / 464.13 MATCH
s1 SUMMARY: 27/27 MATCH two-lane (re-derived = frozen; W1 agreement at the printed dp, boundary tolerance one ulp)
T1 composition checksum: 40779380 myu (frozen 40779380 MATCH)
s1 ap: 3123b760
```

```text
=== E76-BT s2 - the balances re-derived, atom-multiset + mass-ledger gated (2026-11-05) ===
claims = the frozen E75-QS values; the must-fail re-seeded fresh
PASS B01 | C6H10O4 -> C5H8O + C1O2 + H2O1 | atoms C6 H10 O4 = C6 H10 O4 | mass 146 = 146 | myu 1461420 = 1461420 | frozen 146 = 146 MATCH
PASS B02 | C5H8O + C2H6O2 -> C7H12O2 + H2O1 | atoms C7 H14 O3 = C7 H14 O3 | mass 146 = 146 | myu 1461860 = 1461860 | frozen 146 = 146 MATCH
PASS B03 | C7H12O2 + 3 Br2 -> C7H9Br3O2 + 3 H1Br1 | atoms Br6 C7 H12 O2 = Br6 C7 H12 O2 | mass 608 = 608 | myu 6075950 = 6075950 | frozen 608 = 608 MATCH
PASS B04 | 2 C7H9Br3O2 + 4 O1H1 -> C14H14Br2O4 + 4 Br1 + 4 H2O1 | atoms Br6 C14 H22 O8 = Br6 C14 H22 O8 | mass 798 = 798 | myu 7977460 = 7977460 | frozen 798 = 798 MATCH
PASS B05 | C14H14Br2O4 + 2 H2O1 -> C10H6Br2O2 + 2 C2H6O2 | atoms Br2 C14 H18 O6 = Br2 C14 H18 O6 | mass 442 = 442 | myu 4421000 = 4421000 | frozen 442 = 442 MATCH
PASS B06 | C10H6Br2O2 -> C10H6Br2O2 | atoms Br2 C10 H6 O2 = Br2 C10 H6 O2 | mass 318 = 318 | myu 3179640 = 3179640 | frozen 318 = 318 MATCH
PASS B07 | C10H6Br2O2 + 4 Na1H1O1 -> Na2C10H6O4 + 2 Na1Br1 + 2 H2O1 | atoms Br2 C10 H10 Na4 O6 = Br2 C10 H10 Na4 O6 | mass 478 = 478 | myu 4779520 = 4779520 | frozen 478 = 478 MATCH
PASS B08 | Na2C10H6O4 + 2 H1Cl1 -> C10H8O4 + 2 Na1Cl1 | atoms C10 Cl2 H8 Na2 O4 = C10 Cl2 H8 Na2 O4 | mass 309 = 309 | myu 3090560 = 3090560 | frozen 309 = 309 MATCH
PASS B09 | C10H8O4 + 2 C1H4O1 -> C12H12O4 + 2 H2O1 | atoms C12 H16 O6 = C12 H16 O6 | mass 256 = 256 | myu 2562540 = 2562540 | frozen 256 = 256 MATCH
PASS B10 | C8H8 + 10 O2 -> 8 C1O2 + 4 H2O1 | atoms C8 H8 O20 = C8 H8 O20 | mass 424 = 424 | myu 4241320 = 4241320 | frozen 424 = 424 MATCH
PASS B11 | H1Br1 + Na1H1C1O3 -> Na1Br1 + C1O2 + H2O1 | atoms Br1 C1 H2 Na1 O3 = Br1 C1 H2 Na1 O3 | mass 165 = 165 | myu 1649180 = 1649180 | frozen 165 = 165 MATCH
PASS B12 | Br2 + 2 S2O3 -> 2 Br1 + S4O6 | atoms Br2 O6 S4 = Br2 O6 S4 | mass 384 = 384 | myu 3840420 = 3840420 | frozen 384 = 384 MATCH
CAUGHT MF | the seeded B02 seed, water dropped | mass gap 18.015 g = 180150 myu | the atom gate caught it (C7 H14 O3 vs C7 H12 O2), as designed
s2 SUMMARY: 12/12 balances PASS atom + mass gates, 1 CAUGHT must-fail
T2 product-mass checksum: 44740870 myu (frozen 44740870 MATCH)
s2 ap: 86edb933
```

```text
=== E76-BT s3 - the charge ledger re-derived, two-lane (2026-11-05) ===
claims = the frozen E75-QS values; E76-BT re-derives every printed figure by balanced ternary
PASS L01 | adipic acid charge 250 g at 146.142 | got 1.7107 | frozen 1.7107 MATCH | claim: register 1.7107 mol
PASS L02 | cyclopentanone theoretical, machine basis 1.7107 x 84.118 | got 143.90 | frozen 143.90 MATCH | claim: register basis 144.0 at 84.16 - both printed, never averaged
PASS L03 | the 104.8 g harvest, machine basis | got 72.83 | frozen 72.83 MATCH | claim: register basis 72.78%, stated 73% - both round to it
PASS L04 | ketal moles, machine basis 101/128.171 | got 0.7880 | frozen 0.7880 MATCH | claim: the register's own 0.7880, priced at Ch 43's demand row
PASS L05 | Br2 demand, machine basis 3 x 0.7880 x 159.808 | got 377.8 | frozen 377.8 MATCH | claim: Ch 43 pin 377.8; 390 g on hand
PASS L06 | tribromoketal theoretical, machine basis 0.7880 x 364.859 | got 287.5 | frozen 287.5 MATCH | claim: register 287.5
PASS L07 | the 131.78 g tribromoketal, machine basis | got 45.84 | frozen 45.84 MATCH | claim: the register's own 45.8% basis - all round to the stated 46
PASS L08 | the bromine self-correction 390 - 363 | got 27 | frozen 27 MATCH | claim: exact; priced at Ch 43, the register's first cross-episode yield correction
PASS L09 | benzophenone charge 5.96 g | got 0.0327 | frozen 0.0327 MATCH | claim: substoichiometric by design per the 2023 OBC paper
PASS L10 | the pseudo-Favorskii NaOH charge 85 g | got 2.1252 | frozen 2.1252 MATCH | claim: the four-equivalent demand the mechanism lecture names
PASS L11 | the ~11 g diacid at its rank | got 0.0572 | frozen 0.0572 MATCH | claim: from an approx, the rank printed with it
PASS L12 | the strain face 695 kJ/mol over 12 C-C bonds | got 57.9 | frozen 57.9 MATCH | claim: convergent 695, zero-hit as a datum
PASS L13 | the density face 104.152 g/mol at 1.29 g/cm3 | got 80.7 | frozen 80.7 MATCH | claim: convergent 1.29, the densest hydrocarbon
PASS L14 | the octanitrocubane fence face C8N8O16 | got 464.13 | frozen 464.13 MATCH | claim: recognition-only, the P18 gate owns the row
PASS L15 | the trilogy's arc by the backward calendar | got 14 / 28 / 42 | frozen 14 / 28 / 42 MATCH | claim: 2024-01-13 / 01-27 / 02-24 EXACT
PASS L16 | the parent cube C8H8 | got 104.15 | frozen 104.15 MATCH | claim: the parent the register's episodes never claim
s3 SUMMARY: 16/16 rows PASS two-lane (re-derived = frozen)
s3 ap: 440ead76
```

```text
=== E76-BT s4 - eight fresh-keyed injections, every one must be CAUGHT (2026-11-05) ===
CAUGHT J01 | transposed molar mass 128.711 for the ketal
CAUGHT J02 | the scale fault: the tribromoketal at 3648.59 g/mol
CAUGHT J03 | the broken atom gate: B12 with only one thiosulfate
CAUGHT J04 | the wrong-way mass gate: B05 returning three glycols
CAUGHT J05 | the truncation lane: 131.78/287.508892 truncated to 45.83
CAUGHT J06 | the equivalents slip: Br2 demand computed at two equivalents
CAUGHT J07 | the off-by-one chain: the trilogy's arc claimed 15 / 29 / 43
CAUGHT J08 | the fence gate: a PROCEDURAL row must be refused
s4 SUMMARY: 8/8 CAUGHT, 0 escaped
s4 ap: f1601d8e
```

```text
=== E76-BT sR - the register settlement re-settled (2026-11-05) ===
SETTLED R01 | N154's 104.8 g / stated 73% | re-settled both bases: machine 72.83% at 84.118, register 72.78% at 84.16 - both round to the stated 73 | frozen MATCH
SETTLED R02 | N155's 131.78 g / stated 46% | re-settled: machine 45.84% at 131.78/287.5, the register's own 45.8% basis - all round to the stated 46 | frozen MATCH
SETTLED R03 | the 390 g bromine on hand vs the 377.8 g stoichiometric | re-settled: 1.0323x, Ch 43's own printed digit - a 3.2% excess the episode never claims as one | frozen MATCH
SETTLED R04 | the 27-g cross-episode correction | re-settled exact: 390 - 363 = 27, priced at Ch 43 - the register's first in-source yield correction | frozen MATCH
SETTLED R05 | N156's 21.3 g diketone / stated 41% vs literature 93% | re-settled as recorded, NOT independently checkable - the Diels-Alder adduct mass unseen, the register's own flag stands | frozen MATCH
SETTLED R06 | the ~11 g brown diacid | re-settled at its rank: an approx, 0.0572 mol machine-side from it, the rank printed with it | frozen MATCH
SETTLED R07 | the 5.96 g benzophenone photosensitizer charge | re-settled: 0.0327 mol, substoichiometric by design per the 2023 OBC paper | frozen MATCH
SETTLED R08 | the 85 g NaOH pseudo-Favorskii charge | re-settled: 2.1252 mol, the four-equivalent demand the mechanism lecture names | frozen MATCH
SETTLED R09 | the trilogy's upload arc 2024-01-13 / 01-27 / 02-24 | re-settled EXACT: 14 / 28 / 42 days by the backward calendar | frozen MATCH
SETTLED R10 | the production datums: 9 h distillation, 9 h filtrations x2, 25 GB, the two-week stir | re-settled as recorded - production datums, no arithmetic owed | frozen MATCH
SETTLED R11 | the 155 C crude melt test | re-settled as recorded - the instrumentless identity argument; no convergent literature mp pinned for the diketone, the comparison refused honestly | frozen MATCH
SETTLED R12 | the octanitrocubane forward question at the Part II comments | re-settled at the fence: recognition-only forever, the P18 gate owns the row, no answer owed | frozen MATCH
sR SUMMARY: 12/12 SETTLED
sR ap: 6228b08a
```

```text
=== E76-BT s5 - determinism: a fresh rebuild, byte-compared against the frozen run (2026-11-05) ===
method = the same engine re-executed in a fresh block, every sheet rebuilt and byte-compared against the on-disk run, then the on-disk bytes re-digested
PASS D-s0 | rebuilt sheet byte-identical to the on-disk run | MATCH
PASS D-s1 | rebuilt sheet byte-identical to the on-disk run | MATCH
PASS D-s2 | rebuilt sheet byte-identical to the on-disk run | MATCH
PASS D-s3 | rebuilt sheet byte-identical to the on-disk run | MATCH
PASS D-s4 | rebuilt sheet byte-identical to the on-disk run | MATCH
PASS D-sR | rebuilt sheet byte-identical to the on-disk run | MATCH
PASS D-s0r | on-disk bytes re-digested from the file itself | 2559bd33 MATCH
PASS D-s1r | on-disk bytes re-digested from the file itself | 3123b760 MATCH
PASS D-s2r | on-disk bytes re-digested from the file itself | 86edb933 MATCH
PASS D-s3r | on-disk bytes re-digested from the file itself | 440ead76 MATCH
PASS D-s4r | on-disk bytes re-digested from the file itself | f1601d8e MATCH
PASS D-sRr | on-disk bytes re-digested from the file itself | 6228b08a MATCH
PASS D-T1 | T1 re-printed from the fresh rebuild | 40779380 myu (frozen 40779380 MATCH)
PASS D-T2 | T2 re-printed from the fresh rebuild | 44740870 myu (frozen 44740870 MATCH)
s5 SUMMARY: 14/14 determinism PASS (6 byte-compare, 6 re-digest, T1 + T2 re-printed)
s5 ap: 23f08c18
```

```text
=== E76-BT sF - the frozen E75-QS record re-verified from disk (2026-11-05) ===
method = PJW recomputed over each frozen sheet from disk, the final elf digest line stripped from the domain (the newline before it kept); the whole-battery digest over the raw concatenation of s0,s1,s2,s3,s4,sR, elf lines included
PASS F-s0 | frozen sheet re-read from disk, digest line stripped | PJW 04887b8a (file line 04887b8a, frozen 04887b8a) MATCH
PASS F-s1 | frozen sheet re-read from disk, digest line stripped | PJW 0a01c08a (file line 0a01c08a, frozen 0a01c08a) MATCH
PASS F-s2 | frozen sheet re-read from disk, digest line stripped | PJW 0e42fe3a (file line 0e42fe3a, frozen 0e42fe3a) MATCH
PASS F-s3 | frozen sheet re-read from disk, digest line stripped | PJW 08db6bda (file line 08db6bda, frozen 08db6bda) MATCH
PASS F-s4 | frozen sheet re-read from disk, digest line stripped | PJW 0481ed6a (file line 0481ed6a, frozen 0481ed6a) MATCH
PASS F-sR | frozen sheet re-read from disk, digest line stripped | PJW 06d6c0ba (file line 06d6c0ba, frozen 06d6c0ba) MATCH
PASS F-s5 | frozen sheet re-read from disk, digest line stripped | PJW 0ddef52a (file line 0ddef52a, frozen 0ddef52a) MATCH
PASS F-W | whole-battery domain: raw concat of s0+s1+s2+s3+s4+sR, elf lines included | PJW 09f7179a (frozen 09f7179a) MATCH
sF SUMMARY: 8/8 frozen-record re-verification PASS (seven per-sheet domains + the whole-battery domain)
sF ap: 07819708
```
