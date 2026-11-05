# Engine 71 (E71-PE, the prime-exponent engine) — Session 177 transcripts, Vol VII Ch 48

Engine 71: E71-PE "the prime-exponent engine" — fresh this session, zero code shared with Engines 1–70. Every quantity is a signed rational held as prime-exponent vectors (numerator and denominator maps prime→exponent); multiply and divide are exponent arithmetic; add expands to integers under the 9.0e15 guard and re-factors by trial division; rendering is a digit-by-digit half-up lane; witnesses are an independent float64 plain-formula lane plus a prime-product re-expansion bijection check; gates are fresh atom-multiset parsers; the digest is Jenkins one-at-a-time ("joat", 32-bit, hex). Iterative only, no recursion, no BigInt, guards at 9.0e15.

**Honest run history (all defects caught before any battery row was accepted):** rev-0 defect: factorize's bump() used `get(p) as number` on absent keys (NaN exponents, every value 1/1) — caught by the s0 probe's P1 FAIL on the first run. rev-1 defect: norm() conflated a numerator cancelled to 1 with zero (ratI(1) returned the zero value, so every count-1 atom dropped: NaOH computed 0.000, "NO3" lost its N, "H2O" its O) — caught by s0 P1/P3/P4 FAILs and 17 s1 FAILs on the second run; fixed by having norm preserve the sign (zero enters only via the explicit constructors). rev-2 defect: the joat digest deviated from canonical Jenkins one-at-a-time (the mixing step was `h = h<<10` instead of `h += h<<10`, a weaker mixer) — caught by the suspicious s0/s1 digest collision (both "74d7207" for different texts) before the battery was frozen; fixed to the canonical form, all digests recomputed. rev-3 defects (row construction, not engine): the two-argument ratI misuse (ratI(25,10) = 25, so N338's 2.5 g read as 25 g — L18 ten-fold), the mmol-scale slips on the carmine rows, and a mol-vs-mmol division on the stock-NaOH equivalents row (both lanes agreeing on the wrong formula — the lesson named: lane agreement catches arithmetic-type defects, claims catch formula defects) — caught by eight s3 FAILs, fixed. rev-4 defect: the register-basis rows used ratF(46636,1000) = 46.636 for 466.36 — caught by the remaining two s3 FAILs, fixed. rev-5 defect: the carbonate bracket's comparison algebra dropped the denominator b from the right-hand constant (a·s²/q instead of a·s²/b), so the exact bracket landed at x ≈ 3e-6 instead of 7.9e-3 — caught by the sR R09 settlement refusing (UNSETTLED against the float witness, the two-lane discipline working as designed); fixed to the exact rational constant K = a·s²/b with guarded cross-multiplication. The frozen battery below is the clean rev-6 run, every sheet executed twice, byte-identical (s5).

```text
=== E71-PE s0 — the probe battery (2026-11-05) ===
P1 add 1/3+1/6 = 1/2^1 expand 1/2 expect 1/2 PASS
P2 add 2/7+3/5 = 31^1/5^1*7^1 expand 31/35 expect 31/35 PASS
P3 (2/3)*(9/4)/(3/2) = 1/1 expand 1/1 expect 1 PASS
P4 render half-up 2.345@2=2.35 0.0625@3=0.063 2.344@2=2.34 21.69333@2=21.69 expect 2.35/0.063/2.34/21.69 PASS
P5 SEEDED truncating render on 2.345@2 -> 0.02 vs half-up witness 2.35 CAUGHT
s0 rows 5 pass 4 caught 1 fail 0
```

```text
=== E71-PE s1 — the molar book, Sheet 1 (2026-11-05) ===
S1-01 C16H10N2O2 computed 262.268 expect 262.268 w1 262.268 bij ok indigo [PIN Ch22] PASS
S1-02 C16H12N2O2 computed 264.284 expect 264.284 w1 264.284 bij ok leuco-indigo [PIN Ch22] PASS
S1-03 C7H5NO3 computed 151.121 expect 151.121 w1 151.121 bij ok 2-nitrobenzaldehyde [NEW] PASS
S1-04 C3H6O computed 58.080 expect 58.080 w1 58.080 bij ok acetone [PIN Ch21] PASS
S1-05 NaOH computed 39.997 expect 39.997 w1 39.997 bij ok sodium hydroxide [PIN Ch08] PASS
S1-06 NaC2H3O2 computed 82.034 expect 82.034 w1 82.034 bij ok sodium acetate [PIN Ch21] PASS
S1-07 C8H5NO2 computed 147.133 expect 147.133 w1 147.133 bij ok isatin [NEW] PASS
S1-08 C6H7N computed 93.129 expect 93.129 w1 93.129 bij ok aniline [PIN Ch47] PASS
S1-09 C16H10N2O8S2 computed 422.382 expect 422.382 w1 422.382 bij ok indigo disulfonic acid [NEW] PASS
S1-10 C16H8N2Na2O8S2 computed 466.346 expect 466.346 w1 466.346 bij ok indigo carmine [NEW; register basis 466.36 seam named] PASS
S1-11 C16H10N2Na2O8S2 computed 468.362 expect 468.362 w1 468.362 bij ok reduced indigo carmine [NEW] PASS
S1-12 Na2S2O4 computed 174.096 expect 174.096 w1 174.096 bij ok sodium dithionite [PIN Ch22] PASS
S1-13 Na2SO3 computed 126.037 expect 126.037 w1 126.037 bij ok sodium sulfite [PIN Ch17] PASS
S1-14 Na2SO4 computed 142.036 expect 142.036 w1 142.036 bij ok sodium sulfate [PIN Ch05] PASS
S1-15 Na2S computed 78.040 expect 78.040 w1 78.040 bij ok sodium sulfide [PIN Ch13] PASS
S1-16 S8 computed 256.480 expect 256.480 w1 256.480 bij ok sulfur, S8 basis [PIN Ch17] PASS
S1-17 H2SO4 computed 98.072 expect 98.072 w1 98.072 bij ok sulfuric acid [PIN Ch06] PASS
S1-18 NaCl computed 58.440 expect 58.440 w1 58.440 bij ok sodium chloride [PIN Ch03] PASS
S1-19 HCl computed 36.458 expect 36.458 w1 36.458 bij ok hydrogen chloride [PIN Ch04] PASS
S1-20 C6H12O6 computed 180.156 expect 180.156 w1 180.156 bij ok glucose [PIN Ch10] PASS
S1-21 C6H11NaO7 computed 218.137 expect 218.137 w1 218.137 bij ok sodium gluconate [NEW; gluconate ion 195.147 PIN Ch22] PASS
S1-22 H2O2 computed 34.014 expect 34.014 w1 34.014 bij ok hydrogen peroxide [PIN Ch04] PASS
S1-23 Na2CO3 computed 105.988 expect 105.988 w1 105.988 bij ok sodium carbonate [PIN Ch08] PASS
S1-24 H2O computed 18.015 expect 18.015 w1 18.015 bij ok water [PIN Ch03] PASS
S1-25 C6H6N2O2 computed 138.126 expect 138.126 w1 138.126 bij ok p-nitroaniline [NEW] PASS
S1-26 C10H8O computed 144.173 expect 144.173 w1 144.173 bij ok 2-naphthol [NEW] PASS
S1-27 C16H11N3O3 computed 293.282 expect 293.282 w1 293.282 bij ok para red [NEW] PASS
S1-28 O2 computed 31.998 expect 31.998 w1 31.998 bij ok oxygen [PIN Ch07] PASS
S1-29 NaNO2 computed 68.995 expect 68.995 w1 68.995 bij ok sodium nitrite [PIN Ch20] PASS
s1 rows 29 pass 29 fail 0
```

```text
=== E71-PE s2 — the balances, Sheet 2 (2026-11-05) ===
B1 atoms L=R mass L 498.396 vs R 498.396 EQUAL charge 0 OK PASS 2 C7H5NO3 + 2 C3H6O + 2 NaOH -> C16H10N2O2 + 2 NaC2H3O2 + 4 H2O [the Baeyer-Drewsen indigo synthesis, the aldol condensation class]
B2 atoms L=R mass L 264.284 vs R 264.284 EQUAL charge 0 OK PASS C16H10N2O2 + H2 -> C16H12N2O2 [the vat reduction, the hydrogen account]
B3 atoms L=R mass L 286.088 vs R 286.088 EQUAL charge 0 OK PASS Na2S2O4 + O2 + 2 NaOH -> Na2SO3 + Na2SO4 + H2O [the dithionite oxygen scan, the pretreatment rationale]
B4 atoms L=R mass L 336.162 vs R 336.162 EQUAL charge 0 OK PASS 3 S + 6 NaOH -> 2 Na2S + Na2SO3 + 3 H2O [the episode own sulfur fix, the disproportionation to sulfide]
B5 atoms L=R mass L 458.412 vs R 458.412 EQUAL charge 0 OK PASS C16H10N2O2 + 2 H2SO4 -> C16H10N2O8S2 + 2 H2O [the sulfonation to the disulfonic acid]
B6 atoms L=R mass L 539.262 vs R 539.262 EQUAL charge 0 OK PASS C16H10N2O8S2 + 2 NaCl -> C16H8N2Na2O8S2 + 2 HCl [the salt-out, the disodium salt]
B7 atoms L=R mass L 686.499 vs R 686.499 EQUAL charge 0 OK PASS C16H8N2Na2O8S2 + C6H12O6 + NaOH -> C16H10N2Na2O8S2 + C6H11NaO7 [the glucose reduction, the stoplight reductant]
B8 atoms L=R mass L 500.360 vs R 500.360 EQUAL charge 0 OK PASS C16H10N2Na2O8S2 + O2 -> C16H8N2Na2O8S2 + H2O2 [the air re-oxidation, the reversible half of the stoplight]
B9 atoms L=R mass L 424.210 vs R 424.210 EQUAL charge 0 OK PASS C6H6N2O2 + NaNO2 + 2 HCl + C10H8O -> C16H11N3O3 + NaCl + 2 H2O + HCl [the azo coupling comparator, the net-catalytic HCl]
s2 rows 9 pass 9 fail 0
```

```text
=== E71-PE s3 — the charge ledger, Sheet 3 (2026-11-05) ===
L01 25 g 2-nitrobenzaldehyde -> mol r4 0.1654 fl 0.1654 claims [0.1654@4 vs 0.1654] PASS
L02 theoretical indigo (half the aldehyde) -> g r4 21.6935 fl 21.6935 claims [21.69@2 vs 21.69] PASS
L03 N369 yield 11 g -> % r4 50.7063 fl 50.7063 claims [50.7@1 vs 50.7; 51@0 vs 51] PASS
L04 5 g NaOH -> mol (sub-stoichiometric, named) r5 0.12501 fl 0.12501 PASS
L05 NaOH equivalents vs aldehyde (demand 1:1) r4 0.7557 fl 0.7557 PASS
L06 acetone 250 mL x 0.791 g/mL -> mol r4 3.4048 fl 3.4048 PASS
L07 acetone equivalents vs aldehyde r4 20.5814 fl 20.5814 PASS
L08 dye bath: 0.2 g indigo -> mmol r4 0.7626 fl 0.7626 PASS
L09 dye bath: 0.3 g dithionite -> mmol r4 1.7232 fl 1.7232 PASS
L10 dye bath dithionite equivalents (episode practice) r4 2.2597 fl 2.2597 PASS
L11 dye bath NaOH 0.8 g / 40 mL -> M r4 0.5000 fl 0.5000 PASS
L12 vat demand at 1:1 (Ch22 B4 convention) -> g dithionite for 0.2 g indigo r4 0.1328 fl 0.1328 PASS
L13 stock vat: 5 g indigo -> mmol r4 19.0645 fl 19.0645 PASS
L14 stock vat: 6 g dithionite -> mmol r4 34.4637 fl 34.4637 PASS
L15 stock vat dithionite equivalents r4 1.8077 fl 1.8077 PASS
L16 stock vat NaOH equivalents (6 g) r4 7.8686 fl 7.8686 claims [7.87@2 vs 7.87] PASS
L17 pretreatment 1 g dithionite / 5 L -> mM r4 1.1488 fl 1.1488 PASS
L18 N338: 2.5 g indigo -> mmol r4 9.5322 fl 9.5322 claims [9.53@2 vs 9.53] PASS
L19 theoretical carmine (disodium salt, held basis) -> g r4 4.4453 fl 4.4453 claims [4.445@3 vs 4.445] PASS
L20 theoretical carmine, register machine basis 466.36 -> g (the seam: 4.4453 vs 4.4455 at 4dp, same at the register 3dp) r4 4.4455 fl 4.4455 PASS
L21 N338 yield 2.8 g -> % r4 62.9876 fl 62.9876 claims [62.99@2 vs 62.99; 63@0 vs 63] PASS
L22 water wash: 1 g/100 mL x 10 mL -> g (the episode own arithmetic) r3 0.100 fl 0.100 claims [0.1@1 vs 0.1] PASS
L23 salt-out: 30 g NaCl -> mol r4 0.5133 fl 0.5133 PASS
L24 edible recovery 0.9 g of 2.8 g -> % r4 32.1429 fl 32.1429 PASS
L25 IPA shortfall: ideal 3:1 vs used 1:1 -> x r2 3.00 fl 3.00 PASS
L26 sulfonation H2SO4 demand (2 eq) -> g pure acid (30 mL conc = large excess, basis unstated) r4 1.8697 fl 1.8697 PASS
L27 N366 glucose 3 g / 250 mL -> M r4 0.0666 fl 0.0666 PASS
L28 N366 NaOH 5 g / 250 mL -> M (formal pH 13.70, the float-log convention named) r4 0.5000 fl 0.5000 PASS
L29 indigo carmine ~20 mg / 100 mL -> mM (held basis 466.346) r4 0.4289 fl 0.4289 PASS
L30 indigo carmine, register basis 466.36 -> mM (the seam: same at 4dp) r4 0.4289 fl 0.4289 PASS
L31 carbonate 8 g / 250 mL -> M r4 0.3019 fl 0.3019 claims [0.30@2 vs 0.30] PASS
L32 N385 p-nitroaniline 5 g -> mol r5 0.03620 fl 0.03620 PASS
L33 N385 2-naphthol 2.7 g -> mol (the limiting reagent at 1:1) r6 0.018728 fl 0.018728 PASS
L34 theoretical para red (naphthol basis) -> g (yield: P12 honest zero) r4 5.4924 fl 5.4924 PASS
L35 diazonium dilution 5 mL -> 25 mL -> x r2 5.00 fl 5.00 PASS
s3 rows 35 pass 35 fail 0
```

```text
=== E71-PE s4 — the fresh-keyed injections (2026-11-05) ===
I01 transposed charge: 0.2 g indigo priced with the dithionite molar (174.096) -> got 1.1488 vs settled 0.7626 CAUGHT
I02 mis-basis: N338 theoretical computed with indigo molar (262.268) instead of carmine (466.346) -> got 2.5000 vs settled 4.4453 CAUGHT
I03 dropped water: B1 without the 4 H2O (atom gate) -> got atoms MISMATCH mass L 498.396 vs R 426.336 vs settled atoms L=R mass equal (B1 settled) CAUGHT
I04 wrong-basis yield: inverted 21.69/11 (theoretical over actual) -> got 197.2140 vs settled 50.7063 CAUGHT
I05 pH wrong-base: carbonate root with C = 0.0755 mol (moles not molarity) -> got 11.59..11.59 vs settled 11.90 (settled bracket) CAUGHT
I06 dropped HCl: B6 without the 2 HCl on the right (atom gate) -> got atoms MISMATCH vs settled atoms L=R (B6 settled) CAUGHT
I07 uncondensed coupling: B9 with HCl net-negative (catalyst not recovered) -> got atoms MISMATCH vs settled atoms L=R (B9 settled) CAUGHT
I08 dropped condensation: theoretical indigo at 1:1 aldehyde (not 2:1) -> got 43.39 vs settled 21.69 CAUGHT
s4 rows 8 caught 8 escaped 0
```

```text
=== E71-PE sR — the register settlement (2026-11-05) ===
R01 N369 aldehyde mol (register 0.1654) L01 0.1654 SETTLED
R02 N369 theoretical indigo (register 21.69) L02 21.6935 SETTLED
R03 N369 yield (register 50.7; episode about 51) L03 50.7063 SETTLED
R04 N338 indigo mmol (register 9.53) L18 9.5322 SETTLED
R05 N338 theoretical carmine (register 4.445 at 4 sig figs; basis seam named) L19 4.4453 SETTLED
R06 N338 yield (register 62.99; episode 63) L21 62.9876 SETTLED
R07 N338 wash arithmetic (episode: about 0.1 grams) L22 0.100 exact SETTLED
R08 N366 carbonate M (register machine-side 0.30) L31 0.3019 SETTLED
R09 N366 carbonate pH (register ~11.9; the in-video 8-9 wrong by ~4; the pinned correction closer-to-11 supported) bracket x in [0.0078583, 0.0078584] M -> pH in [11.8953, 11.8953]; w1 quadratic pH 11.8953 SETTLED
R10 the 135-day chain N385 (2017-10-15) -> N369 (2018-02-27) 135 days SETTLED
R11 the 54-day chain N369 (2018-02-27) -> N338 (2018-04-22) 54 days SETTLED
R12 the axis chain N338 (2018-04-22) -> N365 (2018-08-31) 131 days SETTLED
R13 the axis chain N365 (2018-08-31) -> N366 (2018-12-19) 110 days SETTLED
R14 the 8-month register claim N338 -> N366 (241 days) 241 days = the 8-month chain EXACT SETTLED
sR rows 14 settled 14 unsettled 0
```
