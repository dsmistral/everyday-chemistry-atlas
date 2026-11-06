# Engine 88 — E88-PA — transcripts (session 203, Vol IX Ch 56 review)

Outputs Verbatim, spliced from the frozen scratch files, never retyped: tP.txt
(1,012 B, md5 7558ba9af0550556b085e257c03de725), tAB.txt (2,058 B, md5
93c4e39c735b1d3e16e5bb5971d2c8ce), tCD.txt (2,790 B, md5
2f82f84c641eb058de4fb4d07adae292), tEFG.txt (2,664 B, md5
d69340dddf44359d430398fad532bb75), tJ.txt (856 B, md5
5005d2da4c71b37065396ced0b5f9c9f). All five are the rev-3 re-runs — every book was
re-run under the enforced pmul contract after the rev-2 silent-zero defect was
caught and fixed; the rev-2 intermediates are disclosed in the engine record and
never reached a verdict table.

## tP.txt — the probe (rev-3)

R88-P: P1 | pmul 495x100 -> 49500 (table 1980+15840+31680=49500); pmul 100x495 -> 49500 (table 1980+15840+31680=49500); phalfUp(495,100,2) q=495 r=0 -> 4.95 | printed 4.95 | PASS | the gold charge, the doubling table the witness (rev-1 spec fed 49500 against scale 100 — a 100x slip, disclosed)
R88-P: P2 | pmul 12x85 -> 1020 (table 340+680=1020); phalfUp(1020,100,1) -> 10.2 | printed 10.2 | PASS | the carrier mass
R88-P: P3 | phalfUp(2780,27802,4) q=999 r=25802 -> 0.1000 (the truncation read would print 0.0999) | printed 0.1000 | PASS | the seventh-water hydration pin, the rounded read (rev-1 spec fed 2780000 — a 100x slip, disclosed)
R88-P: P4 | phalfUp(100000,978,2) q=10224 r=928 -> 102.25 | printed 102.25 | PASS | the 1000-g melt as liquid (rev-1 spec fed 1000000 — a 10x slip, disclosed)
R88-P: P0 census: rows 4 | PASS 4 | FAIL 0
R88-P: verdict: PROBE 4/4 CLEAN at rev-3 (rev-1 spec slips and the rev-2 engine silent-zero defect both disclosed; rev-3 re-run under the enforced pmul contract)

## tAB.txt — Books A+B, karat and the derived datum (rev-3 re-run)

R88-A1 | pmul 24x785 -> 18840 (table 6280+12560=18840); phalfUp(18840,1000,2) -> 18.84 | printed 18.84 | PASS | 24 x 78.5% the AuAl2 mass fraction — the '18 karat' read
R88-A2 | pmul 24x81 -> 1944 (table 648+1296=1944); phalfUp(1944,100,2) -> 19.44 | printed 19.44 | PASS | 24 x 81% — the N397 'about 19 karat' read
R88-A3 | phalfUp(18,24,2) -> 0.75 | printed 0.75 | PASS | 18K = 18/24
R88-A4 | phalfUp(24,24,2) -> 1.00 | printed 1.00 | PASS | 24K = 24/24
R88-A5 | phalfUp(19,24,2) -> 0.79 (the repeating case) | printed 0.79 | PASS | 19K = 19/24 at 2 places
R88-B1 | phalfUp(1969700,25093,1) -> 78.5 (percent) | printed 78.5 | PASS | Au mass fraction 196.97/250.93 — THE DERIVED DATUM: the patent's 78.5 IS the intermetallic stoichiometry
R88-B2 | pmul 2x2698 -> 5396 (the 53.96 complement, table 5396=5396); phalfUp(539600,25093,1) -> 21.5 (percent) | printed 21.5 | PASS | Al mass fraction 53.96/250.93, the complement
R88-B3 | phalfUp(2509300,25093,1) -> 100.0 (the two numerators sum to 100x the denominator) | printed 100.0 | PASS | 78.5 + 21.5 = 100 exactly — the split sums to the whole
R88-B4 | pmul 495x19 -> 9405 (table 495+990+7920=9405); phalfUp(9405,8100,2) -> 1.16 | printed 1.16 | PASS | the recipe-consistent Al charge 4.95 x 19/81 (the digit-transposition arbiter: 1.16 NOT 1.61)
R88-B5 | phalfUp(49500,611,0) -> 81 (percent at 0 places) | printed 81 | PASS | 4.95/(4.95+1.16) = 4.95/6.11 the recipe-consistent read
R88-B6 | phalfUp(49500,656,0) -> 75 (percent at 0 places) | printed 75 | PASS | 4.95/(4.95+1.61) = 4.95/6.56 the caption-figure read — the tension printed honestly
R88-B7 | phalfUp(49500,656,2) -> 75.46 (percent at 2 places; rev-1 spec fed 4950000 — a 100x slip, disclosed) | printed 75.46 | PASS | the caption read at 2 places — the chapter's tension-table figure
R88-A: census: rows 5 | PASS 5 | OBJECTION SUSTAINED 0
R88-B: census: rows 7 | PASS 7 | OBJECTION SUSTAINED 0
R88-AB: rev-3 re-run under the enforced pmul contract (rev-1 B7 scale slip + B2 note template token disclosed; all values defect-free)

## tCD.txt — Books C+D, ferrofluid and bismuth (rev-3, run 2)

R88-C1 | phalfUp(540,1622,4) -> 0.3329 | printed 0.3329 | PASS | 54 g / 162.20 g/mol the FeCl3 moles
R88-C2 | phalfUp(2780,27802,4) -> 0.1000 | printed 0.1000 | PASS | 27.8 g / 278.02 g/mol the FeSO4·7H2O moles
R88-C3 | pmul 54x27802 -> 1501308; pmul 1622x278 -> 450916; phalfUp(1501308,450916,2) -> 3.33 | printed 3.33 | PASS | the Fe(III):Fe(II) charge ratio 0.3329/0.1000
R88-C4 | phalfUp(2,1,2) -> 2.00 | printed 2.00 | PASS | Fe3O4 needs the 2:1 Fe(III):Fe(II) lattice ratio
R88-C5 | pmul 278x23153 -> 6436534; phalfUp(6436534,278020,2) -> 23.15 | printed 23.15 | PASS | 0.1000 mol x 231.53 g/mol the FULL-batch Fe3O4 theoretical
R88-C6 | phalfUp(6436534,556040,2) -> 11.58 | printed 11.58 | PASS | the half-batch theoretical — denominator 556,040 = 278,020 x 2, the chapter's 11.58-g read
R88-C7 | n = pmul(pmul(62,556040)=34474480, 100) = 3447448000; d = pmul(6436534,100) = 643653400; phalfUp(3447448000,643653400,2) -> 5.36 | printed 5.36 | PASS | 0.62 g vs the half-batch 11.58-g theoretical = 5.36% the chapter's percent-of-theoretical (run-1 spec fed d x1000 and the impossible 0.00 verdict exposed the rev-2 engine silent-zero defect — disclosed; engine rev-3, value path now loud)
R88-C8 | phalfUp(3,2,2) -> 1.50 | printed 1.50 | PASS | the mole-ratio halving 3:2 the half-batch read
R88-C9 | pmul 12x85 -> 1020 (table 340+680=1020); phalfUp(1020,100,1) -> 10.2 | printed 10.2 | PASS | 12 g x 85% the chapter's expected yield
R88-C10 | atom balance: Fe pmul(2,1)=2, +1 -> 3 vs 3; O pmul(4,2)=8 vs 8; H pmul(4,2)=8 vs 8 — left Fe3O8H8 right Fe3O8H8 | printed Fe 3=3 O 8=8 H 8=8 L=R | PASS | the net-precipitation balance the chapter prints
R88-D1 | pmul 2714x9 -> 24426 (table 2714+21712=24426); pmul 24426x10 -> 244260 (table 48852+195408=244260); pdiv(244260,5) -> q 48852 r 0; +3200 -> 52052; phalfUp(52052,100,1) -> 520.5 | printed 520.5 | PASS | 271.4 C to F: x9/5+32 via peasant only (run-1 spec divided by 100 — a harness slip, disclosed)
R88-D2 | phalfUp(1033200,10000,2) -> 103.32 | printed 103.32 | PASS | 9.78 x 10.56 the theoretical density read
R88-D3 | phalfUp(20898,978,2) -> 21.37 | printed 21.37 | PASS | 208.98/9.78 the atom-volume datum
R88-D4 | phalfUp(100000,978,2) -> 102.25 | printed 102.25 | PASS | 1/9.78 = 102.25 cm3/g the unit read
R88-D5 | phalfUp(103320,978,2) -> 105.64 | printed 105.64 | PASS | the 105.64 read the chapter prints
R88-D6 | phalfUp(12926,10,1) -> 1292.6 | printed 1292.6 | PASS | 1564 - 271.4 = 1292.6 the liquid range
R88-C: census: rows 10 | PASS 10 | OBJECTION SUSTAINED 0
R88-D: census: rows 6 | PASS 6 | OBJECTION SUSTAINED 0
R88-CD: rev-3 run 2 under the enforced pmul contract (run-1 spec slips C7/D1 disclosed; the C7 0.00 exposed the rev-2 engine defect — the review's own engine held to the review's standard)

## tEFG.txt — Books E+F+G, calendar, economics, and the review hunt (rev-3)

R88-E1 | closed-form dayNum(b) - dayNum(a) = 262; day-walk = 262 LANES AGREE | printed 262 | PASS | the N340->N381 promise chain: 16 Oct 2018 -> 5 Jul 2019
R88-E2 | closed-form dayNum(b) - dayNum(a) = 2157; day-walk = 2157 LANES AGREE | printed 2157 | PASS | the N321 age at its 23 Oct 2026 gather: 26 Nov 2020 -> 23 Oct 2026
R88-E3 | closed-form dayNum(b) - dayNum(a) = 2929; day-walk = 2929 LANES AGREE | printed 2929 | PASS | the N340 age at the 23 Oct 2026 reference: 16 Oct 2018 -> 23 Oct 2026
R88-E4 | closed-form dayNum(b) - dayNum(a) = 2668; day-walk = 2668 LANES AGREE | printed 2668 | PASS | the N381 age at its own 24 Oct 2026 gather date: 5 Jul 2019 -> 24 Oct 2026
R88-E5 | closed-form dayNum(b) - dayNum(a) = 1037; day-walk = 1037 LANES AGREE | printed 1037 | PASS | the N397 age at its own 24 Oct 2026 gather date: 22 Dec 2023 -> 24 Oct 2026
R88-E: census: rows 5 | PASS 5 | OBJECTION SUSTAINED 0
R88-E: both lanes peasant (pmul 365x(y-1), pdiv leap floors, walk via +1 only) — the dual-lane discipline as in E87
R88-F1 | 1.3684 | printed 1.3684 | PASS | the CAD-per-US exchange pair 7800/5700 at 4 places
R88-F2 | 57.00 | printed 57.00 | PASS | the gold bar $5700/100 g = $57.00 per gram
R88-F3 | 12.50 | printed 12.50 | PASS | the etchant $50 for 4 L = $12.50 per liter
R88-F4 | 2.00 | printed 2.00 | PASS | the small-lot premium floor 2.00x
R88-F5 | 2.50 | printed 2.50 | PASS | the small-lot premium ceiling 2.50x
R88-F6 | 2.5058 | printed 2.5058 | PASS | the N397 view ratio 32,825,735 / 13,100,000 at 4 places
R88-F: census: rows 6 | PASS 6 | OBJECTION SUSTAINED 0
R88-G1 | (2200-32)=2168; pmul 2168x5 -> 10840 (table 2168+8672=10840); phalfUp(10840,9,2) -> 1204.44 | printed "about 1,100 C" | OBJECTION SUSTAINED | RF-1: the °F gloss — (2200-32) x 5/9 = 1204.44 C, not "about 1,100 C"; the Safety Table's "1,100 C bench" inherits the gloss
R88-G2 | karat gap 19.44-18.84: phalfUp(60,100,2) -> 0.60; mass gap 81-78.5: phalfUp(250,100,2) -> 2.50 | printed "one karat apart" | OBJECTION SUSTAINED | RF-2: the exact gap is 0.60 karat (0.60) = 2.50% of mass; "one karat apart" follows only from the quoted round reads ("18" vs "about 19")
R88-G3 | phalfUp(3320,978,2) -> 3.39 | printed 3.39 | PASS | Ex 56.5: the swell figure 3.32% of the 9.78 g/cm3 melt
R88-G4 | phalfUp(100,24,2) -> 4.17 | printed 4.17 | PASS | Ex 56.2: the karat step 1/24 = 4.17% of mass — the very step that makes the RF-2 gap 0.60 karat, not one
R88-G5 | aqua regia HNO3 + 3HCl -> NOCl + Cl2 + 2H2O: H 4=4 N 1=1 O 3=3 Cl 3=3 L=R | printed H4/N1/O3/Cl3 balanced | PASS | the dissolution balance the chapter prints
R88-G: census: rows 5 | PASS 3 | OBJECTION SUSTAINED 2

## tJ.txt — the injections and the determinism replay (rev-3)

R88-J1 | injection: "2,200 °F converts to about 1,100 °C" | REFUSED | (2200-32) x 5/9 = 1204.44 °C — the gloss understates by ~104 °C (RF-1)
R88-J2 | injection: the caption's "exactly 1.61 g" of aluminum as the recipe-consistent charge | REFUSED | the recipe-consistent charge is 4.95 x 19/81 = 1.16 g — the digit transposition the chapter itself holds open
R88-J3 | injection: "0.62 g is 5.36% of the FULL-batch theoretical" | REFUSED | 0.62 / 23.15 = 2.68% vs the full batch; 5.36% holds only against the half-batch 11.58-g theoretical
R88-J4 | injection: the N397 age as 1,036 days | REFUSED | both lanes say 1037 — the one-day-short injection, the E86 rev-1 failure class replayed as a probe
R88-J: census: injections 4 | REFUSED 4 | SLIPPED 0
R88-REP: Book F replayed under the same engine: frozen 6 rows, replay 6 rows, byte-identical true
