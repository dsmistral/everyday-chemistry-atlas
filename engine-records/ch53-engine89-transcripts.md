# Engine 89 — E89-DS — the transcripts (session 206, Vol VIII Ch 53, the Phase-3 review)

Outputs Verbatim, frozen to scratch with md5 receipts (bash md5sum the freeze gate),
never retyped. Every defect disclosed in place.

## Receipts

| File | md5 | Bytes | Content |
|---|---|---|---|
| src.txt | e009da3bc3bfa8efb90473cc8ee00cfe | 5494 | design source, on disk before any run |
| out-probe.txt | 43884814bfb2443ee02cca8651360fc7 | 465 | probe rev-1, PASS 5/5 first run |
| out-molar.txt | 1d08b4caccc2d77bb1e56efc37b41c0e | 2032 | molar book rev-1, 22/22 first run, ET re-transcription MATCH |
| out-balance.txt | 09afeeb6c7afb381df68b0e846ea1668 | 751 | balance book rev-1, 7/7 first run |
| out-dose1.txt | 314ac3ef8100f7ca3f01dbec070ede62 | 862 | dose part 1 rev-1, 9/9 PASS, harness census defect (hardcoded 7/7) |
| out-dose1r2.txt | 3c9619686e6a4e8e8fba92dfc64ac674 | 1025 | dose part 1 rev-2, 9/9 PASS, census corrected, rows identical |
| out-dose2.txt | b52a3b3d60bf40245b84ec2b5818ba1e | 862 | dose part 2 rev-1, 6/6 PASS, the TH row-7 defect in the D10/D13 deep lanes (display gates unaffected) |
| out-dose2r2.txt | 7c52b7815eb5895fed13fc1ecbd32983 | 988 | dose part 2 rev-2, 6/6 PASS, lanes repaired, table self-check 200/200 |
| out-rhA.txt | acd985169ade2518abdc8851263bba60 | 914 | review-hunt part A rev-1 (RH1-RH4) |
| out-rhB.txt | d4373154c5404786dcf00087c1e2e2ec | 710 | review-hunt part B rev-2 — the RH5b gate FAIL that caught the carry-table defect (rev-1 crashed, nothing written) |
| out-rhB3.txt | 744921060c50fe5a1e8be9aca5788586 | 784 | review-hunt part B rev-3, 4/4 PASS + table self-check 200/200 |
| out-inj.txt | acc2a8f1a742c5a891dd1edcb7a20b9c | 556 | injections rev-1, 4/4 CAUGHT |
| out-det.txt | 65cd4143810fe71a82b34e431e691e8e | 2237 | determinism, byte-identical, sdbm 90944599 both runs |

The sdbm digests of record: probe -1199058022, molar 2027996228, balance 2102167596,
dose1r2 629222703, dose2 2115775469, rhA -1586291123, rhB3 -358110408, dose2r2
-1968511726, inj 211428428, det 90944599.

## Outputs Verbatim

### out-probe.txt (probe rev-1)
E89-DS PROBE rev-1 (session 206, the Ch 53 review; design source on disk before this run, 5494 B e009da3b)
P1 parse Ca3(C6H5O7)2 -> Ca3 C12 H10 O14 -> PASS
P2 add 192.123 + 18.015 = 210.138 | expected 210.138 -> PASS
P3 mul 13.35 x 28.3495 = 378.465825 | expected 378.465825 -> PASS
P4 div 450 / 29.5735 S=8 = 15.21632542 | trunc4 = 15.2163 | expected 15.2163 -> PASS
P5 disp 210.138 -> trunc 210.13 half-up 210.14 | expected 210.13 / 210.14 -> PASS
PROBE PASS 5/5

### out-molar.txt (molar book rev-1)
E89-DS MOLAR BOOK rev-1 (session 206)
ET re-transcription: H=1.008 C=12.011 O=15.999 Na=22.990 Ca=40.078 S=32.065 Cl=35.450 | digit-check vs the held table: MATCH
M1 C6H8O7: lane=192.123 trunc=192.12 half-up=192.12 | expected 192.12/192.12 -> PASS
M2 C6H8O7H2O: lane=210.138 trunc=210.13 half-up=210.14 | expected 210.13/210.14 -> PASS
M3 Na3C6H5O7: lane=258.069 trunc=258.06 half-up=258.07 | expected 258.06/258.07 -> PASS
M4 Na3C6H5O7H4O2: lane=294.099 trunc=294.09 half-up=294.10 | expected 294.09/294.10 -> PASS
M5 Ca3(C6H5O7)2: lane=498.432 trunc=498.43 half-up=498.43 | expected 498.43/498.43 -> PASS
M6 CaSO4H4O2: lane=172.169 trunc=172.16 half-up=172.17 | expected 172.16/172.17 -> PASS
M7 CaCl2: lane=110.978 trunc=110.97 half-up=110.98 | expected 110.97/110.98 -> PASS
M8 H2SO4: lane=98.077 trunc=98.07 half-up=98.08 | expected 98.07/98.08 -> PASS
M9 NaOH: lane=39.997 trunc=39.99 half-up=40.00 | expected 39.99/40.00 -> PASS
M10 NaCl: lane=58.440 trunc=58.44 half-up=58.44 | expected 58.44/58.44 -> PASS
M11 H2O: lane=18.015 trunc=18.01 half-up=18.02 | expected 18.01/18.02 -> PASS
M12 C6H10O5: lane=162.141 trunc=162.14 half-up=162.14 | expected 162.14/162.14 -> PASS
M13 C6H12O6: lane=180.156 trunc=180.15 half-up=180.16 | expected 180.15/180.16 -> PASS
M14 C8H8O3: lane=152.149 trunc=152.14 half-up=152.15 | expected 152.14/152.15 -> PASS
M15 C7H8O2: lane=124.139 trunc=124.13 half-up=124.14 | expected 124.13/124.14 -> PASS
M16 C2H2O3: lane=74.035 trunc=74.03 half-up=74.04 | expected 74.03/74.04 -> PASS
M17 C9H10O5: lane=198.174 trunc=198.17 half-up=198.17 | expected 198.17/198.17 -> PASS
M18 CO2: lane=44.009 trunc=44.00 half-up=44.01 | expected 44.00/44.01 -> PASS
M19 CH4O: lane=32.042 trunc=32.04 half-up=32.04 | expected 32.04/32.04 -> PASS
M20 CH2Cl2: lane=84.927 trunc=84.92 half-up=84.93 | expected 84.92/84.93 -> PASS
M21 C10H12O2: lane=164.204 trunc=164.20 half-up=164.20 | expected 164.20/164.20 -> PASS
M22 O2: lane=31.998 trunc=31.99 half-up=32.00 | expected 31.99/32.00 -> PASS
MOLAR BOOK 22/22 PASS

### out-balance.txt (balance book rev-1)
E89-DS BALANCE BOOK rev-1 (session 206)
B1 neutralization: counts C6 H11 Na3 O10 = C6 H11 Na3 O10 | mass-lane 312.114 = 312.114 -> PASS
B2 double displacement: counts C12 Ca3 Cl6 H10 Na6 O14 = C12 Ca3 Cl6 H10 Na6 O14 | mass-lane 849.072 = 849.072 -> PASS
B3 the liberation: counts C12 Ca3 H16 O26 S3 = C12 Ca3 H16 O26 S3 | mass-lane 792.663 = 792.663 -> PASS
B4 hydration: counts Ca1 H4 O6 S1 = Ca1 H4 O6 S1 | mass-lane 172.169 = 172.169 -> PASS
B5 starch hydrolysis: counts C6 H12 O6 = C6 H12 O6 | mass-lane 180.156 = 180.156 -> PASS
B6 guaiacol condensation: counts C9 H10 O5 = C9 H10 O5 | mass-lane 198.174 = 198.174 -> PASS
B7 oxidative decarboxylation: counts C18 H20 O12 = C18 H20 O12 | mass-lane 428.346 = 428.346 -> PASS
BALANCE BOOK 7/7 PASS

### out-dose1.txt (dose part 1 rev-1, the census defect)
E89-DS DOSE/ECONOMICS BOOK rev-1 part 1 (session 206)
D1 450 mL in fl oz: lane=15.21632542 trunc=15.216 half-up=15.216 | expected 15.216/15.216 -> PASS
D2 theoretical citric (450 mL x 1.44 g/fl oz): lane=21.91150861 trunc=21.91 half-up=21.91 | expected 21.91/21.91 -> PASS
D3a crude/theoretical percent, 1 dp: lane=82.60499228 trunc=82.6 half-up=82.6 | expected 82.6/82.6 -> PASS
D3b crude/theoretical percent, 0 dp: lane=82.60499228 trunc=82 half-up=83 | expected 82/83 -> PASS
D4 DCM train volume vs charge (percent): lane=80.0000 trunc=80 half-up=80 | expected 80/80 -> PASS
D5a vanilla-sugar charge: 18 x 9 = 162 | expected 162 -> PASS
D5b methanol charge: 150+150+50 = 350 | expected 350 -> PASS
D6 methanol recovery (percent): lane=92.85714285 trunc=92.8 half-up=92.9 | expected 92.8/92.9 -> PASS
D7 N261 vanillin wt-percent: lane=0.92592592 trunc=0.92 half-up=0.93 | expected 0.92/0.93 -> PASS
DOSE BOOK part 1 7/7 PASS

### out-dose1r2.txt (dose part 1 rev-2)
E89-DS DOSE/ECONOMICS BOOK rev-2 part 1 (session 206; rev-1 census defect disclosed: hardcoded 7/7 over 9 PASS rows — the value path clean both runs)
D1 450 mL in fl oz: lane=15.21632542 trunc=15.216 half-up=15.216 | expected 15.216/15.216 -> PASS
D2 theoretical citric (450 mL x 1.44 g/fl oz): lane=21.91150861 trunc=21.91 half-up=21.91 | expected 21.91/21.91 -> PASS
D3a crude/theoretical percent, 1 dp: lane=82.60499228 trunc=82.6 half-up=82.6 | expected 82.6/82.6 -> PASS
D3b crude/theoretical percent, 0 dp: lane=82.60499228 trunc=82 half-up=83 | expected 82/83 -> PASS
D4 DCM train volume vs charge (percent): lane=80.0000 trunc=80 half-up=80 | expected 80/80 -> PASS
D5a vanilla-sugar charge: 18 x 9 = 162 | expected 162 -> PASS
D5b methanol charge: 150+150+50 = 350 | expected 350 -> PASS
D6 methanol recovery (percent): lane=92.85714285 trunc=92.8 half-up=92.9 | expected 92.8/92.9 -> PASS
D7 N261 vanillin wt-percent: lane=0.92592592 trunc=0.92 half-up=0.93 | expected 0.92/0.93 -> PASS
DOSE BOOK part 1 9/9 PASS

### out-dose2.txt (dose part 2 rev-1, the deep-lane defect disclosed)
E89-DS DOSE/ECONOMICS BOOK rev-1 part 2 (session 206)
D8a N260 yield vs brand range top (percent): lane=10.0000 trunc=10 half-up=10 | expected 10/10 -> PASS
D8b N260 yield vs brand range bottom (percent): lane=40.0000 trunc=40 half-up=40 | expected 40/40 -> PASS
D9 Madagascar peak multiple (600/39): lane=15.38461538 trunc=15.38 half-up=15.38 | expected 15.38/15.38 -> PASS
D10 FDA unit beans per liter: lane=99.99096999 trunc=99.99 half-up=99.99 | expected 99.99/99.99 -> PASS
D11 natural vanillin recovery (percent): lane=10.0000 trunc=10 half-up=10 | expected 10/10 -> PASS
D13 citric density of the premise (g/100 mL): lane=4.86584269 trunc=4.86 half-up=4.87 | expected 4.86/4.87 -> PASS
D12 the honest gap: 47 g starch, input mass unstated in-source -> recovery UNCOMPUTABLE; no row fabricated (PASS by refusal)
DOSE BOOK part 2 6/6 PASS (+D12 by refusal)

### out-dose2r2.txt (dose part 2 rev-2, repaired)
E89-DS DOSE/ECONOMICS BOOK rev-2 part 2 (session 206; rev-1 TH row-7 defect disclosed: D10/D13 deep lanes repaired here, display gates unchanged)
TABLE SELF-CHECK: 200/200 -> PASS
D8a N260 yield vs brand range top (percent): lane=10.0000 trunc=10 half-up=10 | expected 10/10 -> PASS
D8b N260 yield vs brand range bottom (percent): lane=40.0000 trunc=40 half-up=40 | expected 40/40 -> PASS
D9 Madagascar peak multiple (600/39): lane=15.38461538 trunc=15.38 half-up=15.38 | expected 15.38/15.38 -> PASS
D10 FDA unit beans per liter: lane=99.99097093 trunc=99.99 half-up=99.99 | expected 99.99/99.99 -> PASS
D11 natural vanillin recovery (percent): lane=10.0000 trunc=10 half-up=10 | expected 10/10 -> PASS
D13 citric density of the premise (g/100 mL): lane=4.86922413 trunc=4.86 half-up=4.87 | expected 4.86/4.87 -> PASS
D12 the honest gap: 47 g starch, input mass unstated in-source -> recovery UNCOMPUTABLE; no row fabricated (PASS by refusal)
DOSE BOOK part 2 6/6 PASS (+D12 by refusal)

### out-rhA.txt (review-hunt part A)
E89-DS REVIEW-HUNT BOOK rev-1 part A (session 206; the skeptic objections, each machine-verified)
RH1 the Ex 53.1 witness: 210.138 - 210.13 = 0.008 (8 mg); 210.14 - 210.138 = 0.002 (2 mg); the printed "3 mg" matches NEITHER -> OBJECTION SUSTAINED (RF-1)
RH2 the Ex 53.3 attribution: lane A (the untruncated theoretical) = 82.60499228 -> 82.6/83; lane B (the printed theoretical 21.91) = 82.61068005 -> 82.6/83; both lanes display 82.6 (1 dp) and 83 (0 dp) -> DISPLAYS ROBUST; the prose attribution to the untruncated lane corrected of record (RF-2)
RH3 the ungated Lecture-4 figure: 1.5 / 0.4 = 3.75000000 -> 3.75/3.75 (the lane terminates: 3.75 exact) -> PASS — the figure stands, the gate now of record (RF-3)
RH4 the D9 floor note: the premise states the peak ">$600/kg"; 15.38x is the multiple of the 600 bound, a floor (>= 15.38x) -> NOTE of record, no display change
REVIEW-HUNT part A 3 verified + 1 note

### out-rhB.txt (review-hunt part B rev-2 — the FAIL that caught the table)
E89-DS REVIEW-HUNT BOOK rev-2 part B (session 206; rev-1 crash disclosed above)
RH5a the citric-head watch ratio: 7,656,810 / 2,900,000 = 2.64027931 -> trunc 2.6402 / half-up 2.6403 | the register display 2.6403 is the HALF-UP at 4 dp (the truncation witness 2.6402 printed beside it) -> PASS
RH5b the starch-head watch ratio: 1,109,352 / 756,200 = 1.39999999 -> trunc 1.3999 / half-up 1.4000 | both displays 1.4670 -> FAIL
RH6 the Ex 53.2 mass lane: 498.432 + 3x98.077 + 6x18.015 = 900.753 = 2x192.123 + 3x172.169 = 900.753 -> PASS
RH7 the Ex 53.4 product: 13.35 x 28.3495 = 378.465825 g; digits 378465825 + 0000 = 3,784,658,250,000 x 10^-10 g -> PASS (the printed figure exact)
REVIEW-HUNT part B INCOMPLETE

### out-rhB3.txt (review-hunt part B rev-3)
E89-DS REVIEW-HUNT BOOK part B rev-3 (session 206)
TABLE SELF-CHECK: 200/200 TL+TH entries re-derived and matched -> PASS (0 mismatches)
RH5a the citric-head watch ratio: 7,656,810 / 2,900,000 = 2.64027931 -> trunc 2.6402 / half-up 2.6403 | the register display 2.6403 is the HALF-UP at 4 dp (the truncation witness 2.6402 printed beside it) -> PASS
RH5b the starch-head watch ratio: 1,109,352 / 756,200 = 1.46700872 -> trunc 1.4670 / half-up 1.4670 | both displays 1.4670 -> PASS
RH6 the Ex 53.2 mass lane: 498.432 + 3x98.077 + 6x18.015 = 900.753 = 2x192.123 + 3x172.169 = 900.753 -> PASS
RH7 the Ex 53.4 product: 13.35 x 28.3495 = 378.465825 g; digits 378465825 + 0000 = 3,784,658,250,000 x 10^-10 g -> PASS (the printed figure exact)
REVIEW-HUNT part B 4/4 PASS + table check PASS

### out-inj.txt (injections)
E89-DS INJECTIONS rev-1 (session 206; the corrected TH tables of rev-3)
J1 Cl 35.450 -> 35.540 transposition: CaCl2 lane=111.158 displays 111.15/111.16 | expected 110.97/110.98 -> CAUGHT
J2 D10 numerator splice 378.465825 -> 378.654825: lane=100.04090488 displays 100.04/100.04 | expected 99.99/99.99 -> CAUGHT
J3 M2 half-up expectation corrupted 210.14 -> 210.15: engine half-up=210.14 | corrupted expectation 210.15 -> CAUGHT
J4 D1 divisor point-slip 29.5735 -> 2.95735: lane=152.16325426 trunc3=152.163 | expected 15.216 -> CAUGHT
INJECTIONS 4/4 CAUGHT

### out-det.txt (determinism)
E89-DS DETERMINISM (session 206; buildAll() = probe 5 rows + dose 15 rows + D12 refusal, run twice in-run, corrected self-checked tables)
TABLE SELF-CHECK: 200/200 -> PASS
P1 parse Ca3(C6H5O7)2 -> Ca3 C12 H10 O14 | expected Ca3 C12 H10 O14 -> PASS
P2 add 192.123 + 18.015 = 210.138 | expected 210.138 -> PASS
P3 mul 13.35 x 28.3495 = 378.465825 | expected 378.465825 -> PASS
P4 div 450 / 29.5735 S=8 = 15.21632542 | trunc4 = 15.2163 | expected 15.2163 -> PASS
P5 disp 210.138 -> trunc 210.13 half-up 210.14 | expected 210.13/210.14 -> PASS
D1 450 mL in fl oz: lane=15.21632542 trunc=15.216 half-up=15.216 | expected 15.216/15.216 -> PASS
D2 theoretical citric (450 mL x 1.44 g/fl oz): lane=21.91150861 trunc=21.91 half-up=21.91 | expected 21.91/21.91 -> PASS
D3a crude/theoretical percent, 1 dp: lane=82.60499228 trunc=82.6 half-up=82.6 | expected 82.6/82.6 -> PASS
D3b crude/theoretical percent, 0 dp: lane=82.60499228 trunc=82 half-up=83 | expected 82/83 -> PASS
D4 DCM train volume vs charge (percent): lane=80.0000 trunc=80 half-up=80 | expected 80/80 -> PASS
D5a vanilla-sugar charge: 18 x 9 = 162 | expected 162 -> PASS
D5b methanol charge: 150+150+50 = 350 | expected 350 -> PASS
D6 methanol recovery (percent): lane=92.85714285 trunc=92.8 half-up=92.9 | expected 92.8/92.9 -> PASS
D7 N261 vanillin wt-percent: lane=0.92592592 trunc=0.92 half-up=0.93 | expected 0.92/0.93 -> PASS
D8a N260 yield vs brand range top (percent): lane=10.0000 trunc=10 half-up=10 | expected 10/10 -> PASS
D8b N260 yield vs brand range bottom (percent): lane=40.0000 trunc=40 half-up=40 | expected 40/40 -> PASS
D9 Madagascar peak multiple (600/39): lane=15.38461538 trunc=15.38 half-up=15.38 | expected 15.38/15.38 -> PASS
D10 FDA unit beans per liter: lane=99.99097093 trunc=99.99 half-up=99.99 | expected 99.99/99.99 -> PASS
D11 natural vanillin recovery (percent): lane=10.0000 trunc=10 half-up=10 | expected 10/10 -> PASS
D13 citric density of the premise (g/100 mL): lane=4.86922413 trunc=4.86 half-up=4.87 | expected 4.86/4.87 -> PASS
D12 the honest gap: 47 g starch, input mass unstated in-source -> recovery UNCOMPUTABLE; no row fabricated (PASS by refusal)
RUN1 vs RUN2: byte-identical=true | sdbm1=90944599 sdbm2=90944599 -> DETERMINISM PASS
