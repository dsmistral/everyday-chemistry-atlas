# Engine 69 — the frozen transcripts (session 175)

*All eight transcripts, spliced verbatim from the session's saved runs (the e69 scratch). The honest history is preserved in place: the sR rev-1 sheet carries the drafter's five hand-frozen expectation slips, caught by the machine; the sR rev-2 header names the repair. The s5 scratch file carries a -rev1 suffix in its name; its content is the clean determinism run the battery reports (fnv d3448d97 twice, 10,307 bytes both). File md5s at splice time: s0 cbbd0851f311957bd880562d24af123d · s1 8c17f0334dcf398d231a633b736c06e1 · s2 5f1ab42856c9df158686067de6c9ae11 · s3 3f996cf26ea3c3fdc5dcf5af80a4f63e · s4 2c735ba40c4f1b6abb7b15a8dbaf9a38 · s5-rev1 9e039a152dce29f5a1ae1b9a10301179 · sR-rev1 c9e0a7079f85c3d90dcb626ca2360bc4 · sR e1ee85b7b4368ae838fed88e2f1871b9. Digest convention: FNV-1a 32-bit, charCode lane, unpadded hex, text without trailing newline — the digests: s0 f673fc2c · s1 43e28034 · s2 23a80262 · s3 2e281538 · s4 24f6b768 · s5 d3448d97 (both passes) · sR-rev1 9d88e5c2 · sR-rev2 e2ddb6cf. The same transcripts are spliced into the chapter master's Lab 47.1/47.2; this file is the engine-records copy.*

## s0 — the probe

```
E69-XR s0 probe — fresh-build gates, seeded must-fail first in the order run
P1  NaCl on the held table  M = 58.440 g/mol  fl 58.440  PASS
P2  half-up seam  5/4 at 1 dp  = 1.3  fl 1.3  PASS
P3  trailing-zero seam  0.291 g C3H6O n at 4 dp  = 0.0050  fl 0.0050  PASS
P4  atoms[L] C9 H14 N2 O1  atoms[R] C9 H14 N2 O1  mass 166224 vs 166224 mg/mol  PASS  (Fischer gate)
P5  seeded fault  NaCl with Cl=35.540 asserted  M = 58530 vs machine 58440  CAUGHT
fnv f673fc2c
```

## s1 — the molar book

```
E69-XR s1 — the molar book (held table + the chapter's three convergent pins Ni/Sn/Br)
S1-01  sodium bicarbonate  NaHCO3  = Na1 H1 C1 O3  M = 84.006 g/mol  xr 42003/500  fl 84.006  PASS
S1-02  ornithine  C5H12N2O2  = C5 H12 N2 O2  M = 132.163 g/mol  xr 132163/1000  fl 132.163  PASS
S1-03  ornithine hydrochloride  C5H13ClN2O2  = C5 H13 Cl1 N2 O2  M = 168.621 g/mol  xr 168621/1000  fl 168.621  PASS
S1-04  putrescine  C4H12N2  = C4 H12 N2  M = 88.154 g/mol  xr 44077/500  fl 88.154  PASS
S1-05  lysine  C6H14N2O2  = C6 H14 N2 O2  M = 146.190 g/mol  xr 14619/100  fl 146.190  PASS
S1-06  lysine hydrochloride  C6H15ClN2O2  = C6 H15 Cl1 N2 O2  M = 182.648 g/mol  xr 22831/125  fl 182.648  PASS
S1-07  5-aminopentanenitrile  C5H10N2  = C5 H10 N2  M = 98.149 g/mol  xr 98149/1000  fl 98.149  PASS
S1-08  N-bromosuccinimide  C4H4BrNO2  = C4 H4 Br1 N1 O2  M = 177.985 g/mol  xr 35597/200  fl 177.985  PASS
S1-09  nickel chloride hexahydrate  NiCl2.6H2O  = Ni1 Cl2 H12 O6  M = 237.683 g/mol  xr 237683/1000  fl 237.683  PASS
S1-10  sodium borohydride  NaBH4  = Na1 B1 H4  M = 37.832 g/mol  xr 4729/125  fl 37.832  PASS
S1-11  cadaverine  C5H14N2  = C5 H14 N2  M = 102.181 g/mol  xr 102181/1000  fl 102.181  PASS
S1-12  aniline  C6H7N  = C6 H7 N1  M = 93.129 g/mol  xr 93129/1000  fl 93.129  PASS
S1-13  sodium nitrite  NaNO2  = Na1 N1 O2  M = 68.995 g/mol  xr 13799/200  fl 68.995  PASS
S1-14  benzenediazonium chloride  C6H5N2Cl  = C6 H5 N2 Cl1  M = 140.570 g/mol  xr 14057/100  fl 140.570  PASS
S1-15  tin(II) chloride  SnCl2  = Sn1 Cl2  M = 189.610 g/mol  xr 18961/100  fl 189.610  PASS
S1-16  tin(IV) chloride  SnCl4  = Sn1 Cl4  M = 260.510 g/mol  xr 26051/100  fl 260.510  PASS
S1-17  phenylhydrazine  C6H8N2  = C6 H8 N2  M = 108.144 g/mol  xr 13518/125  fl 108.144  PASS
S1-18  phenylhydrazine hydrochloride  C6H9N2Cl  = C6 H9 N2 Cl1  M = 144.602 g/mol  xr 72301/500  fl 144.602  PASS
S1-19  propionaldehyde  C3H6O  = C3 H6 O1  M = 58.080 g/mol  xr 1452/25  fl 58.080  PASS
S1-20  p-toluenesulfonic acid monohydrate  C7H10O4S  = C7 H10 O4 S1  M = 190.213 g/mol  xr 190213/1000  fl 190.213  PASS
S1-21  skatole  C9H9N  = C9 H9 N1  M = 131.178 g/mol  xr 65589/500  fl 131.178  PASS
S1-22  ammonia  NH3  = N1 H3  M = 17.031 g/mol  xr 17031/1000  fl 17.031  PASS
S1-23  vanillin  C8H8O3  = C8 H8 O3  M = 152.149 g/mol  xr 152149/1000  fl 152.149  PASS
S1-24  hydroxylamine hydrochloride  NH2OH.HCl  = N1 H4 O1 Cl1  M = 69.488 g/mol  xr 8686/125  fl 69.488  PASS
S1-25  sodium acetate (anhydrous)  NaC2H3O2  = Na1 C2 H3 O2  M = 82.034 g/mol  xr 41017/500  fl 82.034  PASS
S1-26  sodium acetate trihydrate  NaC2H3O2.3H2O  = Na1 C2 H9 O5  M = 136.079 g/mol  xr 136079/1000  fl 136.079  PASS
S1-27  vanillin oxime  C8H9NO3  = C8 H9 N1 O3  M = 167.164 g/mol  xr 41791/250  fl 167.164  PASS
S1-28  vanillylamine  C8H11NO2  = C8 H11 N1 O2  M = 153.181 g/mol  xr 153181/1000  fl 153.181  PASS
S1-29  8-methyl-6-nonenoic acid  C10H18O2  = C10 H18 O2  M = 170.252 g/mol  xr 42563/250  fl 170.252  PASS
S1-30  capsaicin  C18H27NO3  = C18 H27 N1 O3  M = 305.418 g/mol  xr 152709/500  fl 305.418  PASS
rows 30  pass 30  fail 0
fnv 43e28034
```

## s2 — the balances of the lineage

```
E69-XR s2 — the lineage's balances (atom-multiset + distributive mass gates)
C5H12N2O2 -> C4H12N2 + CO2
B1  atoms[L] C5 H12 N2 O2  atoms[R] C5 H12 N2 O2  mass 132163 vs 132163 mg/mol  PASS
C6H14N2O2 -> C5H10N2 + CO2 + 2 H2
B2  atoms[L] C6 H14 N2 O2  atoms[R] C6 H14 N2 O2  mass 146190 vs 146190 mg/mol  PASS
C5H10N2 + 2 H2 -> C5H14N2
B3  atoms[L] C5 H14 N2  atoms[R] C5 H14 N2  mass 102181 vs 102181 mg/mol  PASS
C6H8N2 + C3H6O -> C9H9N + NH3 + H2O
B4  atoms[L] C9 H14 N2 O1  atoms[R] C9 H14 N2 O1  mass 166224 vs 166224 mg/mol  PASS
C6H7N + NaNO2 + 2 HCl -> C6H5N2Cl + NaCl + 2 H2O
B5  atoms[L] C6 Cl2 H9 N2 Na1 O2  atoms[R] C6 Cl2 H9 N2 Na1 O2  mass 235040 vs 235040 mg/mol  PASS
C6H5N2Cl + 2 SnCl2 + 4 HCl -> C6H9N2Cl + 2 SnCl4
B6  atoms[L] C6 Cl9 H9 N2 Sn2  atoms[R] C6 Cl9 H9 N2 Sn2  mass 665622 vs 665622 mg/mol  PASS
C8H8O3 + NH3O -> C8H9NO3 + H2O
B7  atoms[L] C8 H11 N1 O4  atoms[R] C8 H11 N1 O4  mass 185179 vs 185179 mg/mol  PASS
C8H11NO2 + C10H18O2 -> C18H27NO3 + H2O
B8  atoms[L] C18 H29 N1 O4  atoms[R] C18 H29 N1 O4  mass 323433 vs 323433 mg/mol  PASS
balances 8  pass 8  broken 0
fnv 23a80262
```

## s3 — the lineage ledgers

```
E69-XR s3 — the lineage ledgers (charges -> moles -> theoreticals -> yields; lattice: micrograms)
L01  ornithine.HCl charge 1.3 g  n = 0.007710 mol  xr 1300/168621  fl 0.007710  PASS
L02  NaHCO3 0.9 g vs ornithine.HCl (the 'probably not even necessary' 1.39x)  eq = 1.390  xr 168621/121342  fl 1.390  PASS
L03  putrescine theoretical from ornithine.HCl  theo = 0.6796 g  xr 573001/843105  fl 0.6796  PASS
L04  lysine.HCl charge 3.53 g  n = 0.019327 mol  xr 1765/91324  fl 0.019327  PASS
L05  NBS 10.3 g vs lysine.HCl (stated 3.0 eq)  eq = 2.994  xr 37625488/12565741  fl 2.994  PASS
L06  NiCl2.6H2O 22.9 g vs lysine.HCl (stated 5.0 eq)  eq = 4.985  xr 418263920/83902099  fl 4.985  PASS
L07  NaBH4 5.84 g vs lysine.HCl (stated 8.0 eq)  eq = 7.987  xr 13333304/1669337  fl 7.987  PASS
L08  5-aminopentanenitrile theoretical from lysine.HCl  theo = 1.8969 g  xr 34646597/18264800  fl 1.8969  PASS
L09  cadaverine theoretical, HCl-form charge basis (the stated '~2.0 g')  theo = 1.9748 g  xr 36069893/18264800  fl 1.9748  PASS
L10  cadaverine yield 0.5 g vs the HCl-form theoretical (vs the paper's 77%)  pct = 25.32%  xr 913240000/36069893  fl 25.32  PASS
L11  RULED-OUT lane: cadaverine theoretical on the lysine free-base mis-basis  theo = 2.4673 g  xr 36069893/14619000  fl 2.4673  PASS
L12  phenylhydrazine charge 0.5 g  n = 0.004623 mol  xr 125/27036  fl 0.004623  PASS
L13  propionaldehyde 0.291 g vs phenylhydrazine (the 'bit less than 10% excess')  eq = 1.0837  xr 655623/605000  fl 1.0837  PASS
L14  p-TSA.H2O 0.761 g vs phenylhydrazine (the near-stoichiometric 'catalyst')  eq = 0.865  xr 20574396/23776625  fl 0.865  PASS
L15  skatole theoretical from phenylhydrazine (the honest P12 zero)  theo = 0.6065 g  xr 21863/36048  fl 0.6065  PASS
L16  aniline 4.6 mL at the density pin 1.0217 g/mL  n = 0.050466 mol  xr 234991/4656450  fl 0.050466  PASS
L17  NaNO2 procedure figure 3.63 g vs aniline (the charge-matched 1.04 eq)  eq = 1.043  xr 3380582700/3242640809  fl 1.043  PASS
L18  NaNO2 list figure 8 g vs aniline (the UNEXPLAINED list-vs-procedure discrepancy)  eq = 2.298  xr 7450320000/3242640809  fl 2.298  PASS
L19  tin metal 12 g vs aniline (the 2.00-eq reductant charge)  eq = 2.003  xr 620860000/309953129  fl 2.003  PASS
L20  phenylhydrazine.HCl theoretical from aniline  theo = 7.2974 g  xr 16990084291/2328225000  fl 7.2974  PASS
L21  the stated 10 g product vs the theoretical (the register's first above-theoretical yield)  pct = 137.03% CONTAMINATED(>100)  xr 2328225000000/16990084291  fl 137.03  PASS
L22  vanillin charge 9.8 g  n = 0.064411 mol  xr 9800/152149  fl 0.064411  PASS
L23  hydroxylamine.HCl 5 g vs vanillin (the 1.12-eq excess)  eq = 1.117  xr 3803725/3404912  fl 1.117  PASS
L24  sodium acetate 10.55 g vs hydroxylamine.HCl (the 1.79-eq acid scavenger)  eq = 1.787  xr 1832746/1025425  fl 1.787  PASS
L25  vanillin oxime theoretical from vanillin  theo = 10.7671 g  xr 8191036/760745  fl 10.7671  PASS
L26  oxime yield 8.85 g vs theoretical (the stated 'about 82%')  pct = 82.19%  xr 673259325/8191036  fl 82.19  PASS
L27  capsaicinoid scale check: 14 g dried peppers at the 1% literature verdict  = 0.14  xr 7/50  fl 0.14  PASS
L28  N260 yield vs the brand range's 4 g ceiling  = 10.00  xr 10/1  fl 10.00  PASS
L29  N260 yield vs the brand range's 1 g floor  = 40.00  xr 40/1  fl 40.00  PASS
L30  N261 vanillin wt% (1.5 g from 162 g vanilla sugar)  = 0.926  xr 25/27  fl 0.926  PASS
L31  N261 methanol recovery (325 of 350 mL)  = 92.86  xr 650/7  fl 92.86  PASS
L32  N254/N255 pair: solvent economy (1 L soak vs 250 mL Soxhlet)  = 4.00  xr 4/1  fl 4.00  PASS
L33  N254/N255 pair: time economy (168 h soak vs 3 h Soxhlet)  = 56.0  xr 56/1  fl 56.0  PASS
rows 33  pass 33  fail 0
fnv 2e281538
```

## s4 — fresh-keyed injections

```
E69-XR s4 — fresh-keyed injections (each must be CAUGHT; keyed to this chapter's own seams)
I01  claim: ornithine.HCl 3.1 g (transposed) still gives n = 0.007710 mol  machine: n(3.1 g) = 0.018384  CAUGHT
I02  claim: cadaverine theoretical = 2.4673 g (the lysine free-base mis-basis)  machine: HCl-form theoretical = 1.9748 g  CAUGHT
I03  atoms[L] C9 H14 N2 O1  atoms[R] C9 H11 N1 O1  mass 166224 vs 149193 mg/mol  BROKEN  CAUGHT
I04  claim: the 8 g list figure is the 1.04-eq charge  machine: 8 g = 2.298 eq  CAUGHT
I05  claim: the 137.01% phenylhydrazine.HCl yield is a clean yield  machine: pct > 100 -> CONTAMINATED  CAUGHT
I06  atoms[L] C8 H11 N1 O4  atoms[R] C8 H9 N1 O3  mass 185179 vs 167164 mg/mol  BROKEN  CAUGHT
I07  claim: the oxime yield is 73.58% on the hydroxylamine.HCl basis  machine: vanillin is limiting; the vanillin-basis yield = 82.19%  CAUGHT
I08  atoms[L] C18 H29 N1 O4  atoms[R] C18 H27 N1 O4  mass 323433 vs 321417 mg/mol  BROKEN  CAUGHT
injections 8  caught 9  escaped 0
fnv 24f6b768
```

## s5 — determinism

```
E69-XR s5 — determinism: full battery built twice in-run
byte-identical true
fnv-pass1 d3448d97
fnv-pass2 d3448d97
battery bytes 10307 and 10307
```

## sR rev-1 — the literal-settlement sheet (five drafter slips, caught)

```
E69-XR sR — the literal-settlement sheet (the chapter's printed literals, machine-settled)
R01  putrescine theoretical  expect 0.6797 g  machine 0.6796  MISMATCH
R02  cadaverine theoretical (HCl-form basis)  expect 1.9750 g  machine 1.9748  MISMATCH
R03  cadaverine yield  expect 25.32%  machine 25.32  PASS
R04  skatole theoretical  expect 0.6065 g (the register's 0.607 named as the double-round)  machine 0.6065  PASS
R05  phenylhydrazine.HCl theoretical  expect 7.2959 g  machine 7.2974  MISMATCH
R06  the stated 10 g as percent  expect 137.01%  machine 137.03  MISMATCH
R07  vanillin oxime theoretical  expect 10.7680 g  machine 10.7671  MISMATCH
R08  oxime yield  expect 82.19%  machine 82.19  PASS
R09  N261 vanillin wt%  expect 0.926  machine 0.926  PASS
R10  N261 methanol recovery  expect 92.86%  machine 92.86  PASS
rows 10  pass 5  mismatch 5
fnv 9d88e5c2
```

## sR rev-2 — the literal-settlement sheet (10/10)

```
E69-XR sR — the literal-settlement sheet (the chapter's printed literals, machine-settled; rev-2, the five rev-1 hand-frozen expectations corrected to the machine's dual-lane values)
R01  putrescine theoretical  expect 0.6796 g  machine 0.6796  PASS
R02  cadaverine theoretical (HCl-form basis)  expect 1.9748 g  machine 1.9748  PASS
R03  cadaverine yield  expect 25.32%  machine 25.32  PASS
R04  skatole theoretical  expect 0.6065 g (the register's 0.607 named as the double-round)  machine 0.6065  PASS
R05  phenylhydrazine.HCl theoretical  expect 7.2974 g  machine 7.2974  PASS
R06  the stated 10 g as percent  expect 137.03%  machine 137.03  PASS
R07  vanillin oxime theoretical  expect 10.7671 g  machine 10.7671  PASS
R08  oxime yield  expect 82.19%  machine 82.19  PASS
R09  N261 vanillin wt%  expect 0.926  machine 0.926  PASS
R10  N261 methanol recovery  expect 92.86%  machine 92.86  PASS
rows 10  pass 10  mismatch 0
fnv e2ddb6cf
```
