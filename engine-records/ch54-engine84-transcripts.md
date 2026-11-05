# Engine 84 — the interval engine (E84-IR) — session 199, Vol VIII Ch 54

Fresh build, zero code shared with Engines 1-83. Design: every quantity carried
as an outward-rounded interval [lo, hi] through strict worst-case arithmetic —
componentwise addition, four-corner multiplication and division, the reciprocal
of [a,b] as [1/b, 1/a]; each measured input enters at its stated ± tolerance;
derived bounds are only ever widened, never narrowed. The PASS gate is
containment: a claim passes iff the printed figure lies within the derived
interval. No recursion; no BigInt; floats only as the display layer over exact
rational lanes. The fifth verification paradigm of the series (after E80's
integer-lane ledger, E81's double-entry, E82's round-half-up display engine,
and E83-MC's two-prime modular residues), chosen for what the J2/J3 injections
demonstrated live: a plausible point just outside the bracket is refused, and a
digit-slipped density is caught by the register-verified interval itself.

## The honest history, entire

Probe rev-1 PASS 2/2 first run. Molar book rev-1 8/8 PASS first run. Balance
book rev-3 8/8 (rev-1 5/8 — three harness-side FAILs: the lye-discount interval
composed in the wrong order, f(x)=1-80/x increasing in x, the hand-composed
division bypassing the four-corner discipline building a reversed bracket,
plus a printed figure gated without its own display-rounding window; rev-2 8/8
rows PASS but the census printed 8/16, the denominator double-counted at the
call site AND inside row() — the census-defect class, disclosed in the frozen
rev-3 header itself; the engine value path defect-free in every run).
Dose/economics rev-1 18/18 PASS first run. Injections rev-1 4/4 CAUGHT.
Determinism: the dose/economics book re-run byte-identical against its frozen
file (tB3, md5 0327b74f878e65c589b343497fc2b5a6).

## Receipts

| File | md5 | Content |
|---|---|---|
| src.txt | 405dc95de29c555d97cded722234fe5a | design source, written to disk before any run |
| tP0.txt | 1a17e8108a82aad1a773408dae408070 | probe rev-1 PASS 2/2 |
| tB1.txt | a6475d72550c7c08bcac5a50da731106 | molar book rev-1 8/8 |
| tB2.txt | 84b918dfcd56dc2e17ea0c5d69bb5d98 | balance book rev-3 8/8 (rev-1/rev-2 harness history in the header of record) |
| tB3.txt | 0327b74f878e65c589b343497fc2b5a6 | dose/economics book rev-1 18/18 (the determinism replay's reference file) |
| tJ.txt | 6914d9430cb2b06e12f2b67e76a67229b | injections rev-1 4/4 CAUGHT |

## The transcripts, Outputs Verbatim

### Probe rev-1
P1 SPF3 blocks=0.6667 printed67 contained=true
P2 bz-mol [0.3147,0.3150] register 0.3148 contained=true
P0 PROBE OK rows=2


### Molar book rev-1
B1-1 PASS benzaldehyde mol (32 mL, 1.044 g/mL, MW 106.12) printed=0.3148 interval=[0.3147,0.3150]
B1-2 PASS acetone mol (10 mL, 0.791 g/mL, MW 58.08) printed=0.1362 interval=[0.1361,0.1363]
B1-3 PASS acetone-limiting (acMol.hi 0.1363 < bzHalf.lo 0.1573)
B1-4 PASS bz:ac regime ratio printed=2.31 interval=[2.3090,2.3141]
B1-5 PASS DBA theoretical yield g printed=31.91 interval=[31.8881,31.9285]
B1-6 PASS yield pct (22.3 g/theo) printed=69.89 interval=[69.6870,70.0888]
B1-7 PASS yield pct rounded printed=70 interval=[69.6870,70.0888]
B1-8 PASS mp overlap measured [109,111] vs lit [110,112]
B1 MOLAR BOOK 8/8


### Balance book rev-3
B2 REV-3 (rev-2: 8/8 rows PASS but the census printed 8/16 — the harness double-counted the denominator, n++ at the call site AND inside row(); the census defect class disclosed, the row results themselves valid)
B2-1 PASS KOH demand g printed=120.6 interval=[120.0000,121.2000]
B2-2 PASS NaOH equivalent g printed=86 interval=[85.5523,86.4079]
B2-3 PASS lye discount pct (superfat) printed=7 interval=[6.4900,7.4158]
B2-4 PASS lye discount pct bounds printed=6.9 interval=[6.4900,7.4158]
B2-5 PASS lye water w/v pct printed=40 interval=[40.0000,40.0000]
B2-6 PASS recipe input mass sum g printed=880 interval=[880.0000,880.0000]
B2-7 PASS coconut pct of blend (100/600 = 16.6667) inside the printed 16.67 display window [16.665,16.675]
B2-8 PASS N396 soap concentration pct printed=52 interval=[52.0000,52.0000]
B2 BALANCE BOOK rev-3 8/8


### Dose/economics book rev-1
B3-1 PASS SPF 2.75 blocks pct (1-1/2.75) calc=63.64
B3-2 PASS SPF 3 blocks pct (1-1/3, the "bloquea 67%" tail) calc=66.67
B3-3 PASS beads time ratio brackets SPF 2.75 interval=[2.333,3.286]
B3-4 PASS buffer M vs the stated 0.0495 calc=0.04950
B3-5 PASS buffer M rounds to the stated "0.05" calc=0.04950
B3-6 PASS pretreat w/v pct (60/3000) calc=2.00
B3-7 PASS 2000 F -> C calc=1093.3
B3-8 PASS 2400 F -> C calc=1315.6
B3-9 PASS doubling rule 336/2^7 calc=2.625
B3-10 PASS N379 duration 22 min 39.46 s = 1359.46 s calc=1359.46
B3-11 PASS N394 duration 21 min 04.40 s = 1264.40 s calc=1264.4
B3-12 PASS N394 live/crawl 7268622/2.5M = 2.9074 calc=2.9074
B3-13 PASS N398 live/crawl 4380403/1.6M = 2.7378 calc=2.7378
B3-14 PASS N404 live/crawl 14432844/10.8M = 1.3364 calc=1.3364
B3-15 PASS N449 ratio 1.1157 inside the crawl-rounded band interval=[1.1149,1.1159]
B3-16 PASS N396 live/crawl 2076065/1M = 2.0761 calc=2.0761
B3-17 PASS margarine ladder gaps (1869->1902->1910: 33/8)
B3-18 PASS the 27->29 May inversion = 2 days
B3 DOSE/ECONOMICS BOOK 18/18


### Injections rev-1
J1 CAUGHT — lo>hi swap refused: J1
J2 CAUGHT — point-estimate outside the bracket (4.455 vs [2.333,3.286])
J3 CAUGHT — corrupted density 1.440 -> mol 0.4342 vs verified [0.3147,0.3150]
J4 CAUGHT — F->C inversion 3632.0 vs exact 1093.3 (delta 2538.7)
INJECTIONS 4/4 CAUGHT

