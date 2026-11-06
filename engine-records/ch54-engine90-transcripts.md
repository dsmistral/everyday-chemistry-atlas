# Engine 90 (E90-RA) — the Ch 54 review battery, Outputs Verbatim (session 207)

The frozen transcripts, spliced from the md5-gated scratch files, never retyped. Receipts (wc -c / md5sum, bash):

```
tablecheck.txt  574 B   3b034436a97bcff654fb227fd6380f53
probe.txt       307 B   84a238f0af68f7648a76e371b509308a
tB1.txt         560 B   c24effc6ce9d5a3bc155f6084d362
tB2.txt         739 B   d2cacb7ca66d8f946ba39150f03613f3
tB3.txt        1161 B   c7e8a716da6b94d4545e07160f586239
tRH.txt        2078 B   2e5fa4e9fe8e046f1a9a6635a3c3f59a
tJ.txt          414 B   3d773a622bb4de1b1ae67feb6a9c3209
tB3r.txt (the determinism replay) 1161 B  c7e8a716da6b94d4545e07160f586239 — BYTE-IDENTICAL to tB3.txt (diff clean)
```

## The table self-check (rev-1, 13/13, first run — the fresh Rule 21 honored before any book ran)

```
ELEMENT-SELF-CHECK 5/5 (failures 0)
PASS benzaldehyde C7H6O T1-exact=106.12230 T2-printed=106.12
PASS acetone C3H6O T1-exact=58.07950 T2-printed=58.08
PASS DBA C17H14O T1-exact=234.29330 T2-printed=234.29
PASS KOH T1-exact=56.10570 T2-printed=56.11
PASS NaOH T1-exact=39.99717 T2-printed=40.00
PASS glucose C6H12O6 T1-exact=180.15660 T2-printed=180.16
PASS sodium citrate dihydrate T1-exact=294.10011 T2-printed=294.10
PASS citric acid C6H8O7 T1-exact=192.12400 T2-printed=192.12
MOLAR-MASS-CROSSCHECK 8/8 (failures 0)
TABLE SELF-CHECK 13/13 — dihydrate as H9O9 disclosed
```

## Probe (rev-1, 5/5, first run)

```
PASS P1 SPF3 blocks pct 1-1/3 (round) exact=66.6667 printed 66.67
PASS P2 benzaldehyde mol 32*1.044/106.12 (round) exact=0.314813
PASS P3 bz:ac regime ratio (round 2dp) exact=2.31155
PASS P4 KOH demand (500*190+100*256)/1000 exact exact=120.600
PASS P5 336/2^7 exact exact=2.6250
P0 PROBE OK rows=5 fails=0
```

## Molar book (rev-1: 8 PASS + 1 disclosed lane-FAIL — B1-6b is the RF-2 finding, not an engine defect)

```
PASS B1-1 benzaldehyde mol (round) exact=0.314813
PASS B1-2 acetone mol (round) exact=0.136191
PASS B1-3 acetone-limiting (2*ac < bz, exact cross-multiply) 2ac=0.272383 bz=0.314813
PASS B1-4 bz:ac regime (round 2dp) exact=2.31155
PASS B1-5 DBA theoretical g (round 2dp) exact=31.90830
PASS B1-6 yield pct unrounded lane (round 2dp) exact=69.8878
FAIL B1-6b yield pct rounded-mol lane (round 2dp) exact=69.8834
PASS B1-7 yield pct at integer (round) exact=69.89
PASS B1-8 mp overlap measured [109,111] vs lit [110,112] overlap=[110,111]
B1 MOLAR BOOK 8 fails=1
```

## Balance book (rev-1, 8/8, first run)

```
PASS B2-1 KOH demand exact exact=120.600 (the printed interval [120.0,121.2] contains it)
PASS B2-2 NaOH equiv both lanes (round) 56.1-lane=85.9893 exact-mass-lane=85.9806 (the printed interval [85.55,86.41] contains both)
PASS B2-3 lye discount pct both lanes (round to integer) 56.1-lane=6.9652 exact-lane=6.9557
PASS B2-4 the printed interval [6.49,7.42] contains both exact lanes d1=6.9652 d2=6.9557
PASS B2-5 lye water w/v pct 80g/200mL exact exact=40.00
PASS B2-6 recipe input mass sum 500+100+80+200 (water at density-1 convention, disclosed) exact=880
PASS B2-7 coconut pct of blend inside the printed 16.67 display window exact=16.6667 (1/6)
PASS B2-8 N396 soap concentration 1300/2500 exact exact=52.00
B2 BALANCE BOOK 8 fails=0
```

## Dose/economics book (rev-3, 18/18; rev-1 syntax crash, rev-2 missing-qadd crash — both harness-side, disclosed, nothing written)

```
PASS B3-1 SPF 2.75 blocks pct (round 2dp) exact=63.6364
PASS B3-2 SPF 3 blocks pct (the bloquea-67 tail) exact=66.6667
PASS B3-3 beads bracket corners 23/7,23/9,21/7,21/9 (round 3dp) interval=[2.333,3.286]
PASS B3-4 buffer M (round 4dp) exact=0.049502
PASS B3-5 buffer M (round 2dp) exact=0.0495
PASS B3-6 pretreat w/v 60/3000 exact=2.000
PASS B3-7 2000F->C (2000-32)*5/9 (round 1dp) exact=1093.3333
PASS B3-8 2400F->C (round 1dp) exact=1315.5556
PASS B3-9 doubling rule 336/2^7 exact exact=2.6250
PASS B3-10 N379 duration 22:39.46 exact exact=1359.460
PASS B3-11 N394 duration 21:04.40 exact exact=1264.400
PASS B3-12 N394 live/crawl (round 4dp) exact=2.907449
PASS B3-13 N398 live/crawl (round 4dp, half-up boundary) exact=2.737752
PASS B3-14 N404 live/crawl (round 4dp) exact=1.336374
PASS B3-15 N449: printed 1.1157 NOT the 1.1M-exact composition (naive=1.1164); implied crawl base 1100682 inside the 1.1M display band register-held ratio, RH2 note
PASS B3-16 N396 live/crawl (round 4dp) exact=2.076065
PASS B3-17 margarine ladder gaps 1869->1902->1910 exact 33/8
PASS B3-18 the 27->29 May inversion = 2 days exact 2
B3 DOSE/ECONOMICS BOOK rev-3 18 fails=0
```

## Review hunt (rev-2; rev-1's RH6 harness formula slip disclosed in the header)

```
RH REV-2 (rev-1 RH6 FAIL: the harness gated the SHIFT against the RATIO — qdiv ratio 1.079914 x 100 = 107.99, not the shift; the value path clean, every individual figure in the row correct; the formula fixed, the row re-run)
SUSTAINED RH1 the printed 69.89 is the UNROUNDED-lane display (exact 69.8878 -> 69.89); the rounded-mol lane displays 69.88 — the lane must be named; robust at 70. RF-2.
NOTE RH2 the printed 1.1157 is register-held; composed from the printed 1.1M base it would display 1.1164; the implied crawl base is 1,100,682 — the 1.1M is its display band. No correction (both figures register-held); the appendix names the implied base.
NOTE RH3 DBA 234.29 holds on the IUPAC 12.0107 basis (exact 234.2933 -> 234.29); the 12.011 textbook basis displays 234.30 — the chapter's supplier/reference basis is the right one and is named in Sources; no correction.
NOTE RH4 KOH exact 56.1057 displays 56.1 (1dp, the Ex 54.1 lane) and 56.11 (2dp, the Sources lane) — both of record, both already named in the chapter; no correction.
SUSTAINED RH5 the chapter's own anchor is SPF 30 (the commercial rung it prints); 30/3 = 10 exactly and the transmission lane (1/3)/(1/30) = 10 exactly — the 'twenty-fold short' phrase (Lectures 2 and 5, Ex 54.2) does not follow from any stated figure; twenty-fold requires an SPF-60 bottle the chapter never names. RF-1: corrected of record to ten-fold.
CLEAN RH6 Ex 54.3 worked: 25/294.10=0.085005 12.2/192.12=0.063502 sum=0.148507 anhydrous 25/258.07=0.096873 the ~8 percent shift exact=7.9914 (the ~8 percent claim holds)
CLEAN RH7 Ex 54.2 worked: 1/2.75 = 0.36364 at 5dp round; the printed subtraction 1-0.36364 = 0.63636 checks exactly (100000-36364 = 63636); consistent with 63.64 at 2dp
CLEAN RH8 Ex 54.4: the printed 2.75 = 11/4 exactly, inside the four-corner bracket [2.333,3.286] (receipt tB3 B3-3)
CLEAN RH9 the chapter's molar sum 0.1485 mol: exact 0.148507 -> 0.1485 (round); and the molarity 0.0495/0.05 per tB3 B3-4/5
RH REVIEW HUNT rev-2 9 rows: 2 SUSTAINED (RF-1, RF-2), 3 NOTE (RH2-RH4), 4 CLEAN (RH6-RH9)
```

## Injections (rev-1, 4/4 CAUGHT, first run)

```
CAUGHT J1 — the integer guard refused the 2^60 product: E90: integer guard
CAUGHT J2 — the inverted regime ratio 0.43261 refused against the printed 2.31 (round gate)
CAUGHT J3 — the truncated 2.7377 refused (the true round is 2.7378; the round gate knows its convention)
CAUGHT J4 — the digit-slipped benzaldehyde (106.21) gives 0.314547 and is refused against the printed 0.3148
J0 INJECTIONS 4/4 CAUGHT
```

## Determinism (the B3 replay, byte-identical)

```
PASS B3-1 SPF 2.75 blocks pct (round 2dp) exact=63.6364
PASS B3-2 SPF 3 blocks pct (the bloquea-67 tail) exact=66.6667
PASS B3-3 beads bracket corners 23/7,23/9,21/7,21/9 (round 3dp) interval=[2.333,3.286]
PASS B3-4 buffer M (round 4dp) exact=0.049502
PASS B3-5 buffer M (round 2dp) exact=0.0495
PASS B3-6 pretreat w/v 60/3000 exact=2.000
PASS B3-7 2000F->C (2000-32)*5/9 (round 1dp) exact=1093.3333
PASS B3-8 2400F->C (round 1dp) exact=1315.5556
PASS B3-9 doubling rule 336/2^7 exact exact=2.6250
PASS B3-10 N379 duration 22:39.46 exact exact=1359.460
PASS B3-11 N394 duration 21:04.40 exact exact=1264.400
PASS B3-12 N394 live/crawl (round 4dp) exact=2.907449
PASS B3-13 N398 live/crawl (round 4dp, half-up boundary) exact=2.737752
PASS B3-14 N404 live/crawl (round 4dp) exact=1.336374
PASS B3-15 N449: printed 1.1157 NOT the 1.1M-exact composition (naive=1.1164); implied crawl base 1100682 inside the 1.1M display band register-held ratio, RH2 note
PASS B3-16 N396 live/crawl (round 4dp) exact=2.076065
PASS B3-17 margarine ladder gaps 1869->1902->1910 exact 33/8
PASS B3-18 the 27->29 May inversion = 2 days exact 2
B3 DOSE/ECONOMICS BOOK rev-3 18 fails=0
```

Battery totals: table self-check 13/13 + probe 5/5 + molar 8+1 + balance 8/8 + dose/economics 18/18 + review hunt 9 + injections 4/4 CAUGHT; determinism byte-identical. Zero engine value-path defects; four harness-side slips disclosed and repaired (B3 rev-1/rev-2, RH rev-1, and the read-shape slip at the master push, no effect).
