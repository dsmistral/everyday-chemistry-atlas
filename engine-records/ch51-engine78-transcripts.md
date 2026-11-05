# Engine 78 — the transcripts (session 191, Ch 51 part 2 of 2)

*The five receipts frozen into `manuscript/vol8/ch51.md`'s Lab 51.2 verbatim. Digest lane: djb2 over the transcript text without the trailing newline (distinct from the sdbm convention of the Engines 66/77 receipts and all earlier digests); md5 over the receipt files as stored. The run history — four kernel defect classes caught by the probe pre-sheet, the harness-layer corrections at Pieces B/D/E — is printed in the transcript headers themselves and in the record's §3.*

## Piece A — the probe (engine78-a.txt, 1,821 B, md5 7fcbd98ef086c9b23550632396c2121a, djb2 d25c53b2)

```
ENGINE 78 PIECE A - REV-5: THE PROBE (E78-IL, the integer-lane engine; receipt run 2026-11-05; four honest defect classes caught by the probe before any sheet row ran - the sign convention [rev-1/2: the raw kernel carries product-side negatives; the claim verifier negates product columns], the K2 kernel defect [rev-2/3: cofactor minors on the unreduced element matrix are not square when the element count exceeds n-1; fixed on the rank basis], the K3 determinant defect [rev-3/4: the basis routine's row-gcd normalization reused inside the determinant, where row scaling scales the determinant; fixed: no normalization], the K4 determinant defect [rev-4/5: the fraction-free elimination multiplies every remaining row by the pivot, so the diagonal product over-counts the determinant by the product of the pivots - the Cannizzaro witness read 2:14:1:1; fixed with the Bareiss exact-division identity, every entry stays an exact minor of the original matrix]; two independent passes at rev-5, byte-identical, determinism PASS)
  A1 parse join SnCl2 -> Sn1 Cl2, mass 189610 my = 189.610 g/mol; W 189.610 MATCH -> PASS
  A2 half-up boundaries: 2.065 @2dp -> 2.07; 0.125 @2dp -> 0.13 -> PASS
  A3 cofactor kernel witness H2+O2->H2O: engine 2:1:2 (sides-aware, no anomaly); mass closure 2*2016+31998 = 36030 = 2*18015 my (0) -> PASS
  A4 the Cannizzaro witness 2 C6H5CHO + NaOH -> C6H5CH2OH + C6H5COONa: engine 2:1:1:1 (the K2+K3+K4 case, 4 elements over 4 species, rank basis, Bareiss minors); mass closure 2*106124+39997 = 252245 = 108140+144105 my (0) -> PASS
  INJ-A1 wrong-basis Cannizzaro claim 1:1:1:1: residual {"C":-7,"H":-6,"O":-1} -> CAUGHT; engine prints 2:1:1:1
  INJ-A2 uppercase-run formula SNCL2: refused (UNKNOWN ELEMENT: L) -> CAUGHT
PIECE A VERDICT: 4 PASS rows, 2 CAUGHT injections
E78-A djb2: d25c53b2
```

## Piece B — Sheet 1, the other doors' balances (engine78-b.txt, 1,523 B, md5 36a2cb20d22fbb654b54020c0dd4ddc8, djb2 eead09e4)

```
ENGINE 78 PIECE B - REV-2: SHEET 1, THE BALANCES (E78-IL; receipt run 2026-11-05; kernel = the rev-5 probe-cleared code, four defect classes fixed pre-sheet; claim lane negates product columns per the sign convention; rev-2 is a decorative-literal correction only: rev-1's B2 line typed HCl/NaCl as 36460/58442 where the engine table gives 36458/58440 - the computed closure value was exact 0 in both revisions, no figure changed; two independent passes, byte-identical, determinism PASS)
  B1 Cannizzaro 2 C6H5CHO + NaOH -> C6H5CH2OH + C6H5COONa: kernel 2:1:1:1, closure 2*106124+39997-108140-144105 = 0 -> PASS
  B2 the acid workup NaC7H5O2 + HCl -> C7H6O2 + NaCl: kernel 1:1:1:1 (5 elements over 4 species, rank basis), closure 144105+36458-122123-58440 = 0 -> PASS
  B3 Verley-Doebner C6H5CHO + C3H4O4 -> C9H8O2 + CO2 + H2O: kernel lane code -2 (rank 3 over 5 species, kernel dimension 2 - the engine REFUSES the unique-kernel print and says so; a second algebraic relation exists among these five species, disclosed); claim lane 1:1:1:1 residual {} clean; closure 106124+104061 = 210185 = 148161+44009+18015 (0) -> PASS
  B4 piperine hydrolysis C17H19NO3 + H2O -> C12H10O4 + C5H11N: kernel 1:1:1:1, closure 285343+18015 = 303358 = 218208+85150 (0; Ch 34 E8 pin re-derived) -> PASS
  INJ-B1 Verley-Doebner water-dropped 1:1:1:1:0: residual {"H":2,"O":1} -> CAUGHT
  INJ-B2 piperine hydrolysis over-watered 1:2:1:1: residual {"H":2,"O":1} -> CAUGHT
PIECE B VERDICT: 4 PASS rows, 2 CAUGHT injections
E78-B djb2: eead09e4
```

## Piece C — Sheet 2, the molar book (engine78-c.txt, 2,699 B, md5 59c8f1e9328f1a581271148852d7c70e, djb2 cc69f920)

```
ENGINE 78 PIECE C - REV-1: SHEET 2, THE MOLAR BOOK (E78-IL; receipt run 2026-11-05; integer lane my = mg/mol exact; float witness lane W over the same nominal table; every row printed at 3 dp where the lane is exact; two independent passes, byte-identical, determinism PASS)
  C1 benzaldehyde C6H5CHO: 106124 my = 106.124 g/mol; W 106.124 MATCH [printed at 3 dp: 106.124, not the ethyl acetate 106.121 of Ch 23-25/45 (the 106.12 collision, named)] -> PASS
  C2 benzyl alcohol C6H5CH2OH: 108140 my = 108.140 g/mol; W 108.140 MATCH [the Cannizzaro half] -> PASS
  C3 sodium benzoate NaC7H5O2: 144105 my = 144.105 g/mol; W 144.105 MATCH [Ch 31 pin 144.105 (part 1 printed 2 dp 144.11), re-proved] -> PASS
  C4 benzoic acid C7H6O2: 122123 my = 122.123 g/mol; W 122.123 MATCH [Ch 31 pin 122.123, re-proved] -> PASS
  C5 malonic acid C3H4O4: 104061 my = 104.061 g/mol; W 104.061 MATCH [the Verley-Doebner partner] -> PASS
  C6 cinnamic acid C9H8O2: 148161 my = 148.161 g/mol; W 148.161 MATCH [the product of the other door] -> PASS
  C7 pyridine C5H5N: 79102 my = 79.102 g/mol; W 79.102 MATCH [the solvent that is also a base] -> PASS
  C8 beta-alanine C3H7NO2: 89094 my = 89.094 g/mol; W 89.094 MATCH [the catalyst] -> PASS
  C9 piperine C17H19NO3: 285343 my = 285.343 g/mol; W 285.343 MATCH [Ch 34 pin 285.343, re-proved] -> PASS
  C10 piperic acid C12H10O4: 218208 my = 218.208 g/mol; W 218.208 MATCH [the hydrolysis half] -> PASS
  C11 piperidine C5H11N: 85150 my = 85.150 g/mol; W 85.150 MATCH [the other hydrolysis half] -> PASS
  C12 styrene C8H8: 104152 my = 104.152 g/mol; W 104.152 MATCH [Ch 50 collision: the exact formula/mass of cubane, named] -> PASS
  C13 water H2O: 18015 my = 18.015 g/mol; W 18.015 MATCH [the pivot of the book] -> PASS
  C14 carbon dioxide CO2: 44009 my = 44.009 g/mol; W 44.009 MATCH [Ch 20 pin 44.009, re-proved] -> PASS
  C15 sodium hydroxide NaOH: 39997 my = 39.997 g/mol; W 39.997 MATCH [Ch 8 pin 39.997, re-proved] -> PASS
  C16 hydrogen chloride HCl: 36458 my = 36.458 g/mol; W 36.458 MATCH [Ch 6 prints 36.46 at 2 dp; the lane reads 36.458, consistent] -> PASS
  C17 sodium chloride NaCl: 58440 my = 58.440 g/mol; W 58.440 MATCH [Ch 6 pin 58.44, re-proved] -> PASS
  C18 p-nitroaniline C6H6N2O2: 138126 my = 138.126 g/mol; W 138.126 MATCH [Ch 48 pin 138.126, re-proved] -> PASS
  C19 2-naphthol C10H8O: 144173 my = 144.173 g/mol; W 144.173 MATCH [Ch 48 pin 144.173, re-proved] -> PASS
  C20 para red C16H11N3O3: 293282 my = 293.282 g/mol; W 293.282 MATCH [Ch 48 pin 293.282 (S1-27), re-proved] -> PASS
  INJ-C1 benzaldehyde mis-pinned to the ester digit 106121: lane reads 106124 -> CAUGHT
PIECE C VERDICT: 20 PASS rows, 1 CAUGHT injections
E78-C djb2: cc69f920
```

## Piece D — Sheet 3, the charge/yield ledger (engine78-d.txt, 2,504 B, md5 6fa59684abf2eae9919e89ae13b95946, djb2 abb3df74)

```
ENGINE 78 PIECE D - REV-2: SHEET 3, THE CHARGE/YIELD LEDGER (E78-IL; receipt run 2026-11-05; every figure re-derived from the register charges in the integer nmol lane (nmol = mg*10^9/my, exact floor); masses printed in 0.1 mg units as g at 4 dp; the register's own stated figures are printed as stated where they are register claims (the unequal-yield puzzle, the 87, the mp), never smoothed; rev-1/rev-2: four harness defects fixed - the D2 percent scale (divided by 1000 where a percent needs 100), the D4 yield-percent scale (x10 high), a mis-pinned D5 expected value (the plan's 3.5052 mmol was a bad 4-digit rounding; the lane reads 3.5046 mmol and the reconstruction identity replaces the pin), and one decorative mol literal (D3 malonic 0.240252 -> 0.240244); all lane figures (nmol, mg) were exact in both revisions; two independent passes at rev-2, byte-identical, determinism PASS)
  D1 Cannizzaro charge: benzaldehyde 20 mL x 1044 mg/mL = 20880 mg = 196750970 nmol (0.196751 mol); NaOH 15 g = 375028127 nmol (0.375028 mol) = 1.906 eq per aldehyde; the 2:1 demand = aldehyde/2 = 98375485 nmol exact (0.098375 mol); NaOH headroom = 3.812x the demand -> PASS
  D2 Cannizzaro yields: benzyl alcohol theoretical 98375485 nmol x 108140 = 10.6383 g; sodium benzoate theoretical 14.1763 g; register states 51% and 62% -> implied 5.4255 g and 8.7893 g (register-stated, the unequal-yield puzzle, printed as stated, no smoothing); bp 205-206 observed vs 205.3 literature (the window brackets it, delta 0.3-1.3 K) -> PASS
  D3 Verley-Doebner charge: benzaldehyde 10 mL = 10440 mg = 98375485 nmol (0.098375 mol) LIMITING; malonic acid 25 g = 240243703 nmol (0.240244 mol) = 2.442 eq; beta-alanine 2 g = 22448200 nmol (0.022448 mol) = 0.228 eq catalytic -> PASS
  D4 cinnamic yield: theoretical 98375485 nmol x 148161 = 14.5754 g; stated 12.6 g -> 86.44% vs the register's 87 (the register rounded up, delta 0.56 pt); mp observed 125 vs literature 132-133 -> 7-8 K low, the register's own deficit -> PASS
  D5 piperine: 1 g from 23 g pepper = 4.35% (the register's ~4; the typical range is 5-9, this run light, disclosed); 1 g = 3504554 nmol = 3.505 mmol (reconstruction |nmol x my - 10^12| < my: true) -> PASS
  INJ-D1 density digit-slip 0.844 g/mL: charge reads 16880 mg, not 20880 mg (guard: fed charge must equal density x volume exactly) -> CAUGHT
  INJ-D2 cinnamic theoretical digit-slip 14.75 g: lane reads 14.5754 g -> CAUGHT
PIECE D VERDICT: 5 PASS rows, 2 CAUGHT injections
E78-D djb2: abb3df74
```

## Piece E — Sheet 4, the worked answers and settlement rows (engine78-e.txt, 1,953 B, md5 04ae5c4e70ee661c32c7df6702eae0f8, djb2 c98f755b)

```
ENGINE 78 PIECE E - REV-2: SHEET 4, WORKED ANSWERS AND SETTLEMENT ROWS (E78-IL; receipt run 2026-11-05; the same integer nmol lane as Sheet 3; X2 is the settlement of part 1's Lab 51.1 L14 seam, computed both ways from the episode's own charges; rev-2 is a narrative correction only: rev-1's X2 parenthetical claimed the lane read 5.4926 g by a hand estimate - the lane's own printed figure was and is 5.4924 g, identical to Ch 48's settled row, the settlement is exact; no lane figure changed; two independent passes at rev-2, byte-identical, determinism PASS)
  X1 half-scale NaOH demand: 10 mL benzaldehyde = 98375485 nmol -> 2:1 demand 49187742 nmol -> NaOH 49187742 nmol x 39997 = 1.9673 g (the register's 1.967 g) -> PASS
  X2 the L14 settlement, both ways: the episode's own charges - p-nitroaniline 5 g = 36198832 nmol -> amine-limited para red 10.6164 g (part 1's L14 printed this way as 10.62 g, the wrong basis); 2-naphthol 2.7 g = 18727500 nmol -> naphthol-limited para red 5.4924 g; the smaller governs: NAPHTHOL limiting (part 1's L14 said diazonium limiting - corrected of record; this lane's fresh re-derivation reads 5.4924 g, identical to Ch 48's settled row, the settlement is exact) -> PASS
  X3 cinnamic round-trip: 0.87 x 14.5754 g = 12.6805 g vs the stated 12.6 g (the register's 87 was its own rounding; the lane reads 86.44%, the register rounded up, disclosed) -> PASS
  X4 the disproportionation symmetry: both Cannizzaro products take the same mol count = aldehyde/2 = 98375485 nmol (benzyl alcohol and sodium benzoate rise together, the defining symmetry of the disproportionation; 2 x 98375485 = 196750970 = the aldehyde charge nmol, exact) -> PASS
  INJ-E1 naphthol digit-slip 0.018278 mol: reads 5.3606 g, not the lane's 5.4924 g -> CAUGHT
  INJ-E2 51% of the wrong base (benzoate 14.1763 g): reads 7.2299 g, not the benzyl base's 5.4255 g -> CAUGHT
PIECE E VERDICT: 4 PASS rows, 2 CAUGHT injections
E78-E djb2: c98f755b
```

*Battery digest: djb2 f9ee439, computed over the five transcripts concatenated in A–E order, newline-separated — each transcript taken as its own digest convention takes it (the receipt text above its own trailing `E78-X djb2:` line, without trailing newline). Receipt files: 1,821 / 1,523 / 2,699 / 2,504 / 1,953 B, md5 7fcbd98ef086c9b23550632396c2121a / 36a2cb20d22fbb654b54020c0dd4ddc8 / 59c8f1e9328f1a581271148852d7c70e / 6fa59684abf2eae9919e89ae13b95946 / 04ae5c4e70ee661c32c7df6702eae0f8.*
