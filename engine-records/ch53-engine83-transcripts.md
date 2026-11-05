# Engine 83 — the modular cross-check engine (E83-MC) — session 198, Vol VIII Ch 53

Fresh build, zero code shared with Engines 1-82. Design: every identity verified in three
independent lanes — the exact integer lane (masses in integer my-units, mg/mol; divisions
print integer witness triples [q, r, d]), modulo p1 = 65537, and modulo p2 = 1000003 — with
the modular residues required to be mutually consistent with the integer lane. No recursion
(the formula parser is an iterative character walk with an explicit group stack); no BigInt;
no floats in any value path (display-only centi formatting of exact integers excepted,
disclosed). Element table (my-units): H 1008, C 12011, O 15999, Na 22990, Ca 40078,
S 32065 (the 32.065 conventional weight, disclosed), Cl 35450. Diverges from E82's
rational-display round-half-up paradigm: E83's canonical display is truncation-with-witness,
the half-up printed as its comparison display only, never the engine's own rounding rule.

## The honest history, entire

Probe rev-2 PASS 5/5 (rev-1 harness defect: the census line swept the header into the
every-PASS check; value path clean). Molar book rev-1 22/22 PASS first run. Balance book
rev-1 7/7 PASS first run. Dose/economics rev-2 15/15 PASS + D12 by refusal (rev-1 8/15:
seven FAILs all harness-side — four percent rows missing their x100, D13 double-scaled,
the display helper at the wrong decimal place, and two expectation hand-slips the engine
had right: D9 hu 1539->1538, D10 hu 10000->9999 — the engine value path defect-free in
every run). Injections rev-1 4/4 CAUGHT. Determinism rev-3 PASS (rev-1: the X1 ternary
collapsed to an unconditional PASS — operator precedence; rev-2: byte-identity proven but
the compact mirror omitted the 10^dp scaling on four dose rows — harness mirror slip, the
main sheet standing 15/15 throughout; rev-3 mirror all-rows-PASS, digests equal both runs,
sdbm 820233240). Of record: src.txt's draft D2 row printed r=23815; the run is
authoritative, r=44615, q=2191 unchanged.

## Receipts

| File | md5 | Content |
|---|---|---|
| src.txt | b8613fd6944fdc9bcd32d66ce6fb532f | design source, written to disk before any run |
| tP1.txt | 984ab807c625c816d385a300a429e9ec | probe rev-1 (harness census defect) |
| tP2.txt | ce9d7f78584d0b9b1fa3028e1a6d37b9 | probe rev-2 PASS 5/5 |
| tM1.txt | 8ea2bab3f1c6325db2d48a07fea801a6 | molar book rev-1 22/22 |
| tB1.txt | b1227b9cbc3a95dbc3fb92413c585767 | balance book rev-1 7/7 |
| tD1.txt | 84243ca33d4a81bce8f3c9f2e04f3d44 | dose/economics rev-1 (gates caught 7 harness defects) |
| tD2.txt | e02253170074fafb93036447c136c8c0 | dose/economics rev-2 15/15 + D12 |
| tX1.txt | bb7792a00ef6a3266a1fa89353f4d3ca | injections rev-1 4/4 CAUGHT (+ the X1 precedence defect) |
| tX2.txt | c8eb965cb0bf9ea9dcd5477f01c33ad2 | determinism rev-2 (byte-identity proven, mirror slip) |
| tX3.txt | c54b2523ac1606966b1cd2f50e7be9df | determinism rev-3 PASS, mirror all-rows-PASS |

## The transcripts, Outputs Verbatim

### Probe rev-1 (the harness census defect, of record)
E83-MC PROBE rev-1
P1 parse Ca3(C6H5O7)2 -> {"Ca":3,"C":12,"H":10,"O":14} PASS
P2 massLane C6H8O7 = 192123 PASS
P3 mod-lane consistency P1/P2 PASS (r1=61049, r2=192123)
P4 mulmod edge PASS
P5 witness triple div(4500000,295735) = [15, 63975, 295735] PASS
PROBE FAIL

### Probe rev-2
E83-MC PROBE rev-2 (rev-1 harness defect: the census line swept the header into the every-PASS check; value path clean)
P1 parse Ca3(C6H5O7)2 -> {"Ca":3,"C":12,"H":10,"O":14} PASS
P2 massLane C6H8O7 = 192123 PASS
P3 mod-lane consistency P1/P2 PASS (r1=61049, r2=192123)
P4 mulmod edge PASS
P5 witness triple div(4500000,295735) = [15, 63975, 295735] PASS
PROBE PASS 5/5

### Molar book rev-1
E83-MC MOLAR BOOK rev-1
M1 citric acid (anhydrous): lane=192123 (192.123), trunc=192.12, half-up=192.12, lit=192.12 -> AGREE-EXACT, mod-lanes CONSISTENT PASS
M2 citric acid monohydrate: lane=210138 (210.138), trunc=210.13, half-up=210.14, lit=210.14 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M3 trisodium citrate (anhydrous): lane=258069 (258.069), trunc=258.06, half-up=258.07, lit=258.07 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M4 trisodium citrate dihydrate: lane=294099 (294.099), trunc=294.09, half-up=294.10, lit=294.10 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M5 calcium citrate: lane=498432 (498.432), trunc=498.43, half-up=498.43, lit=498.43 -> AGREE-EXACT, mod-lanes CONSISTENT PASS
M6 gypsum: lane=172169 (172.169), trunc=172.16, half-up=172.17, lit=172.17 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M7 calcium chloride: lane=110978 (110.978), trunc=110.97, half-up=110.98, lit=110.98 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M8 sulfuric acid: lane=98077 (98.077), trunc=98.07, half-up=98.08, lit=98.08 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M9 sodium hydroxide: lane=39997 (39.997), trunc=39.99, half-up=40.00, lit=40.00 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M10 sodium chloride: lane=58440 (58.440), trunc=58.44, half-up=58.44, lit=58.44 -> AGREE-EXACT, mod-lanes CONSISTENT PASS
M11 water: lane=18015 (18.015), trunc=18.01, half-up=18.02, lit=18.02 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M12 starch unit: lane=162141 (162.141), trunc=162.14, half-up=162.14, lit=162.14 -> AGREE-EXACT, mod-lanes CONSISTENT PASS
M13 glucose: lane=180156 (180.156), trunc=180.15, half-up=180.16, lit=180.16 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M14 vanillin: lane=152149 (152.149), trunc=152.14, half-up=152.15, lit=152.15 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M15 guaiacol: lane=124139 (124.139), trunc=124.13, half-up=124.14, lit=124.14 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M16 glyoxylic acid: lane=74035 (74.035), trunc=74.03, half-up=74.04, lit=74.04 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M17 4-hydroxy-3-methoxymandelic acid: lane=198174 (198.174), trunc=198.17, half-up=198.17, lit=198.17 -> AGREE-EXACT, mod-lanes CONSISTENT PASS
M18 carbon dioxide: lane=44009 (44.009), trunc=44.00, half-up=44.01, lit=44.01 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M19 methanol: lane=32042 (32.042), trunc=32.04, half-up=32.04, lit=32.04 -> AGREE-EXACT, mod-lanes CONSISTENT PASS
M20 dichloromethane: lane=84927 (84.927), trunc=84.92, half-up=84.93, lit=84.93 -> AGREE-HALFUP, mod-lanes CONSISTENT PASS
M21 eugenol: lane=164204 (164.204), trunc=164.20, half-up=164.20, lit=164.20 -> AGREE-EXACT, mod-lanes CONSISTENT PASS
M22 oxygen: lane=31998 (31.998), trunc=31.99, half-up=32.00, lit=31.99 -> AGREE-EXACT, mod-lanes CONSISTENT PASS
MOLAR BOOK 22/22 PASS

### Balance book rev-1
E83-MC BALANCE BOOK rev-1
B1 neutralization C6H8O7 + 3 NaOH -> Na3C6H5O7 + 3 H2O -> int CLOSED, mass-lane EQUAL PASS [Na 3/3 ok, C 6/6 ok, H 11/11 ok, O 10/10 ok]
B2 double displacement 2 Na3C6H5O7 + 3 CaCl2 -> Ca3(C6H5O7)2 + 6 NaCl -> int CLOSED, mass-lane EQUAL PASS [Ca 3/3 ok, C 12/12 ok, H 10/10 ok, O 14/14 ok, Na 6/6 ok, Cl 6/6 ok]
B3 the liberation Ca3(C6H5O7)2 + 3 H2SO4 -> 2 C6H8O7 + 3 CaSO4 -> int CLOSED, mass-lane EQUAL PASS [C 12/12 ok, H 16/16 ok, O 26/26 ok, Ca 3/3 ok, S 3/3 ok]
B4 hydration CaSO4 + 2 H2O -> CaSO4(H2O)2 -> int CLOSED, mass-lane EQUAL PASS [Ca 1/1 ok, S 1/1 ok, O 6/6 ok, H 4/4 ok]
B5 starch hydrolysis C6H10O5 + H2O -> C6H12O6 -> int CLOSED, mass-lane EQUAL PASS [C 6/6 ok, H 12/12 ok, O 6/6 ok]
B6 guaiacol condensation C7H8O2 + C2H2O3 -> C9H10O5 -> int CLOSED, mass-lane EQUAL PASS [C 9/9 ok, H 10/10 ok, O 5/5 ok]
B7 oxidative decarboxylation 2 C9H10O5 + O2 -> 2 C8H8O3 + 2 CO2 + 2 H2O -> int CLOSED, mass-lane EQUAL PASS [C 18/18 ok, H 20/20 ok, O 12/12 ok]
BALANCE BOOK 7/7 PASS
### Dose/economics rev-1 (the gates firing)
E83-MC DOSE/ECONOMICS AUDIT rev-1
D1 450 mL in fl oz (10^-4 mL units): q=15216 r=96240 d=295735 | trunc=15.216 half-up=15.216 | expected tr=15216 hu=15216 | stated: 15.216 fl oz (stated) PASS
D2 theoretical citric from 450 mL x 1.44 g/fl oz (my-g): q=2191 r=44615 d=295735 | trunc=22 half-up=22 | expected tr=2191 hu=2191 | stated: 21.91 g (register machine-exact) PASS
D3a crude/theoretical percent, 1 dp: q=826 r=323500 d=6480000 | trunc=8.3 half-up=8.3 | expected tr=826 hu=826 | stated: 82.6% (register) PASS
D3b crude/theoretical percent, 0 dp: q=82 r=3920350 d=6480000 | trunc=82 half-up=83 | expected tr=82 hu=83 | stated: 83% (video stated) PASS
D4 DCM train volume vs charge: q=0 r=240 d=300 | trunc=0 half-up=1 | expected tr=80 hu=80 | stated: 80% (240 of ~300 mL) FAIL
D5a vanilla-sugar charge: q=162 r=0 d=1 | trunc=162 half-up=162 | expected tr=162 hu=162 | stated: 162 g = 18 x 9 g (exact) PASS
D5b methanol charge: q=350 r=0 d=1 | trunc=350 half-up=350 | expected tr=350 hu=350 | stated: 350 mL = 150+150+50 (exact) PASS
D6 methanol recovery: q=928 r=2000 d=3500 | trunc=9.3 half-up=9.3 | expected tr=928 hu=929 | stated: 92.9% (stated) PASS
D7 N261 vanillin wt%: q=92 r=96 d=162 | trunc=0.01 half-up=0.01 | expected tr=92 hu=93 | stated: 0.93 wt% (stated) PASS
D8a N260 yield vs brand range top: q=0 r=400 d=4000 | trunc=0 half-up=0 | expected tr=10 hu=10 | stated: 10% of 4 g/500 mL FAIL
D8b N260 yield vs brand range bottom: q=0 r=400 d=1000 | trunc=0 half-up=0 | expected tr=40 hu=40 | stated: 40% of 1 g/500 mL FAIL
D9 Madagascar peak multiple: q=1538 r=18 d=39 | trunc=0.15 half-up=0.15 | expected tr=1538 hu=1539 | stated: 15.38x (2013 -> 2018 peak) FAIL
D10 FDA unit beans per liter: q=9999 r=36750000 d=378500000 | trunc=100 half-up=100 | expected tr=9999 hu=10000 | stated: 99.99 g/L trunc / 100.00 half-up FAIL
D11 natural vanillin recovery: q=0 r=1000 d=10000 | trunc=0 half-up=0 | expected tr=10 hu=10 | stated: ~10% (1 kg of the ~10 kg present in 500 kg beans at 2%) FAIL
D13 citric density of the premise: q=48692 r=32121000 d=133080750 | trunc=4.87 half-up=4.87 | expected tr=486 hu=487 | stated: 4.86 g/100 mL trunc / 4.87 half-up (band 4.5-5) FAIL
D12 the honest gap: 47 g starch, input mass unstated in-source -> recovery UNCOMPUTABLE; no row fabricated (PASS by refusal)
NOTE: src.txt draft row D2 printed r=23815; the run is authoritative: r=44615, q=2191 unchanged — corrected of record.
DOSE/ECONOMICS AUDIT 8/15 rows PASS (+D12 by refusal)
### Dose/economics rev-2
E83-MC DOSE/ECONOMICS AUDIT rev-2 (rev-1: 8/15 + D12; the seven FAILs all harness-side — four percent rows missing x100, D13 double-scaled, the display helper, and two expectation hand-slips the engine had right; value path defect-free)
D1 450 mL in fl oz (10^-4 mL units): q=15216 r=96240 d=295735 | trunc=15216.000 half-up=15216.000 | expected tr=15216 hu=15216 | stated: 15.216 fl oz (stated) PASS
D2 theoretical citric from 450 mL x 1.44 g/fl oz (my-g): q=2191 r=44615 d=295735 | trunc=21.91 half-up=21.91 | expected tr=2191 hu=2191 | stated: 21.91 g (register machine-exact) PASS
D3a crude/theoretical percent, 1 dp: q=826 r=323500 d=6480000 | trunc=82.6 half-up=82.6 | expected tr=826 hu=826 | stated: 82.6% (register) PASS
D3b crude/theoretical percent, 0 dp: q=82 r=3920350 d=6480000 | trunc=82 half-up=83 | expected tr=82 hu=83 | stated: 83% (video stated) PASS
D4 DCM train volume vs charge (percent): q=80 r=0 d=300 | trunc=80 half-up=80 | expected tr=80 hu=80 | stated: 80% (240 of ~300 mL) PASS
D5a vanilla-sugar charge: q=162 r=0 d=1 | trunc=162 half-up=162 | expected tr=162 hu=162 | stated: 162 g = 18 x 9 g (exact) PASS
D5b methanol charge: q=350 r=0 d=1 | trunc=350 half-up=350 | expected tr=350 hu=350 | stated: 350 mL = 150+150+50 (exact) PASS
D6 methanol recovery: q=928 r=2000 d=3500 | trunc=92.8 half-up=92.9 | expected tr=928 hu=929 | stated: 92.9% (stated) PASS
D7 N261 vanillin wt%: q=92 r=96 d=162 | trunc=0.92 half-up=0.93 | expected tr=92 hu=93 | stated: 0.93 wt% (stated) PASS
D8a N260 yield vs brand range top (percent): q=10 r=0 d=4000 | trunc=10 half-up=10 | expected tr=10 hu=10 | stated: 10% of 4 g/500 mL PASS
D8b N260 yield vs brand range bottom (percent): q=40 r=0 d=1000 | trunc=40 half-up=40 | expected tr=40 hu=40 | stated: 40% of 1 g/500 mL PASS
D9 Madagascar peak multiple: q=1538 r=18 d=39 | trunc=15.38 half-up=15.38 | expected tr=1538 hu=1538 | stated: 15.38x (2013 -> 2018 peak) PASS
D10 FDA unit beans per liter: q=9999 r=36750000 d=378500000 | trunc=99.99 half-up=99.99 | expected tr=9999 hu=9999 | stated: 99.99 g/L, trunc and half-up (the ~100 g/L fold) PASS
D11 natural vanillin recovery (percent): q=10 r=0 d=10000 | trunc=10 half-up=10 | expected tr=10 hu=10 | stated: ~10% (1 kg of the ~10 kg present in 500 kg beans at 2%) PASS
D13 citric density of the premise (g/100 mL): q=486 r=122755500 d=133080750 | trunc=4.86 half-up=4.87 | expected tr=486 hu=487 | stated: 4.86 g/100 mL trunc / 4.87 half-up (band 4.5-5) PASS
D12 the honest gap: 47 g starch, input mass unstated in-source -> recovery UNCOMPUTABLE; no row fabricated (PASS by refusal)
NOTE (of record): src.txt draft row D2 printed r=23815; the run is authoritative: r=44615, q=2191 unchanged.
DOSE/ECONOMICS AUDIT 15/15 rows PASS (+D12 by refusal)
### Injections rev-1 (with the X1 precedence defect, of record)
E83-MC DETERMINISM + INJECTIONS rev-1
PASS
X2 injections (each must be CAUGHT):
J1 B1 product count corrupted 1->2: CAUGHT (element sums fail)
J2 citric formula C6H8O6: lane=176124 vs 192123: CAUGHT (molar gate)
J3 fl-oz factor 295735->300000: q=2160 vs 2191: CAUGHT (witness gate)
J4 the p1-invisible corruption (+65537 to the Ca count): integer lane CATCHES, mod-p1 BLIND (residue unchanged — the single-prime design would miss it), mod-p2 CATCHES -> CAUGHT (two-prime design justified)
INJECTIONS 4/4 CAUGHT
### Determinism rev-2 (of record)
E83-MC DETERMINISM rev-2 (rev-1 harness defect: the X1 ternary collapsed to an unconditional PASS — precedence; injections rev-1 4/4 CAUGHT stand)
X1 determinism: run1 sdbm=2405803796, run2 sdbm=2405803796, strings byte-identical=true, digests equal=true -> PASS
X1 run1=B1 PASS|B2 PASS|B3 PASS|B4 PASS|B5 PASS|B6 PASS|B7 PASS|D2 PASS q=2191|D6 FAIL q=92|D7 FAIL q=0|D9 FAIL q=15|D10 PASS q=9999|D13 FAIL q=4
### Determinism rev-3
E83-MC DETERMINISM rev-3 (rev-2: byte-identity proven but the compact mirror omitted the 10^dp scaling on four dose rows — harness mirror slip, main sheet tD2 stands 15/15; rev-1: the precedence ternary; injections rev-1 4/4 CAUGHT stand)
X1 determinism: run1 sdbm=820233240, run2 sdbm=820233240, strings byte-identical=true, digests equal=true -> PASS
X1 mirror all-rows-PASS=true | run1=B1 PASS|B2 PASS|B3 PASS|B4 PASS|B5 PASS|B6 PASS|B7 PASS|D2 PASS q=2191|D6 PASS q=928|D7 PASS q=92|D9 PASS q=1538|D10 PASS q=9999|D13 PASS q=486
