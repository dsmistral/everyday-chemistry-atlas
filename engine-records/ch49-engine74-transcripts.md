# Engine 74 Transcripts — E74-SD, the string-decimal engine (session 180, 2026-11-05)

Vol VII Ch 49 "Photochromism and Cold" review unit. Fresh engine, zero code shared with Engines 1-73. Design: every quantity a sign, digit string, and decimal scale (value = sign x digits x 10^-sc); no BigInt, no Number in the value path; schoolbook string algorithms (addD/subD with borrow, mulD O(n.m) carry table, divHalfUp string long division with half-up on the (frac+1)-th digit); single-pass group-stack atom parser reading a closing bracket's trailing multiplier at the close; W1 float64 witness typed from independent decimal constants; held table in micro-y as digit strings (C 120110, H 10080, N 140070, O 159990, S 320600, Na 229900, Cl 354530, Mg 243050); P18 NAME gate first; digest CRC-32 (IEEE reflected poly 0xEDB88320), distinct from FNV-1a/j31/joat/sdbm/adler-32; the chains by the Fliegel-Van Flandern JDN with truncating integer division — a fresh civil-date method where E73 used days_from_civil.

Honest run history: rev-0 the integer-part accumulator kept leading zeros ("000600.560" for 60.056, four probe FAILs) and the seeded-fault row escaped because its gate compared a hard-coded string instead of the witness; rev-1 stripped the zeros and made the gate compare the truncation lane against the half-up witness dynamically — and the probe then caught two scale defects rev-0's garbled output had masked: the molar-book divisor 1000 instead of 10000 (the held table is 1e-4 g/mol; urea 600.560) and the render denominator over-scaled by 10^frac (9.995 -> 0.10); rev-2 both fixed, the probe clean and frozen. Battery authoring caught by the two-lane and register discipline, never laundered: the first s3 build's six mis-scaled row encodings (L20/L21/L22/L24/L25/L26) and sR's two S05 mis-encodings (1.85/10, then a spurious qnd /10 around a plain product) — engine core untouched, frozen at rev-2. The sheets below are the frozen clean battery, written as they were generated (scratch is not storage) and spliced byte-verbatim.

Manifest: s0 the probe (8 PASS + 1 CAUGHT, crc32 711fdf24); s1 the molar book re-derived (23/23, T1 exact 17178130 myu, crc32 ccd03c75); s2 the balances re-derived (11 PASS + 1 CAUGHT must-fail, T2 exact 12546100 myu, crc32 37ce3e1e); s3 the charge ledger re-derived (26/26 two-lane, crc32 f65fca26); s4 the fresh injections (8/8 CAUGHT, crc32 f0b36a0d); sR the register settlement (20/20 SETTLED, crc32 1899029e); s5 determinism (s4/sR byte-identical and disk-matching; G5 all six sheets recompute MATCH from disk; whole battery crc32 14515d26). Verdict: ZERO ARITHMETIC FINDINGS.

---

```text
=== E74-SD s0 — the probe, rev-2 battery (2026-11-05) ===
rev-0: integer-part accumulator kept leading zeros; the seeded-fault row compared a hard-coded string, not the witness — caught (4 FAIL, SF ESCAPED)
rev-1: leading zeros stripped, SF row compares the trunc lane against the half-up witness dynamically — but the probe then caught two masked scale defects (below)
PASS P1 string long-division half-up: 2/3 at 3 dp | got 0.667 | expect 0.667
PASS P2 exact tail: 1/8 at 6 dp terminates | got 0.125000 | expect 0.125000
PASS P3 repeating tail: 1/7 at 6 dp | got 0.142857 | expect 0.142857
PASS P4 carry chain on round-up: 9.995 at 2 dp | got 10.00 | expect 10.00
PASS P5 dp=0 no bare dot: 150.4 at 0 dp | got 150 | expect 150
PASS P6 the rev-2 regression row: urea at its Ch 20 pin (gMol divisor 10000, myu = 1e-4 g/mol) | got 60.056 | expect 60.056
PASS P6w W1 float witness agrees | got 60.056 | expect 60.056
PASS P7 renderV denominator 10^sc: 0.25 x 4 at 2 dp | got 1.00 | expect 1.00
CAUGHT SF | the seeded truncation lane: trunc 0.666 vs half-up witness 0.667 — the witness caught it, as designed
s0 SUMMARY: 8 PASS, 1 CAUGHT
s0 crc32: 711fdf24
```

```text
=== E74-SD s1 — the 22-species molar book re-derivation (2026-11-05) ===
claims = the frozen E73 values; engine re-derives from the held table; W1 cross per species
PASS DNBP C12H9N3O4 | got 259.221 | W1 259.221 | claim 259.221
PASS 2-benzylpyridine C12H11N | got 169.227 | W1 169.227 | claim 169.227
PASS pyridine C5H5N | got 79.102 | W1 79.102 | claim 79.102
PASS urea CO(NH2)2 | got 60.056 | W1 60.056 | claim 60.056
PASS ammonium nitrate NH4NO3 | got 80.043 | W1 80.043 | claim 80.043
PASS ammonia NH3 | got 17.031 | W1 17.031 | claim 17.031
PASS nitric acid HNO3 | got 63.012 | W1 63.012 | claim 63.012
PASS nitrous acid HNO2 | got 47.013 | W1 47.013 | claim 47.013
PASS nitric oxide NO | got 30.006 | W1 30.006 | claim 30.006
PASS nitrogen dioxide NO2 | got 46.005 | W1 46.005 | claim 46.005
PASS nitrous oxide N2O | got 44.013 | W1 44.013 | claim 44.013
PASS sodium nitrate NaNO3 | got 84.994 | W1 84.994 | claim 84.994
PASS ammonium chloride NH4Cl | got 53.492 | W1 53.492 | claim 53.492
PASS magnesium sulfate MgSO4 | got 120.361 | W1 120.361 | claim 120.361
PASS diethyl ether C4H10O | got 74.123 | W1 74.123 | claim 74.123
PASS sodium hydroxide NaOH | got 39.997 | W1 39.997 | claim 39.997
PASS sodium carbonate Na2CO3 | got 105.988 | W1 105.988 | claim 105.988
PASS sodium sulfate Na2SO4 | got 142.036 | W1 142.036 | claim 142.036
PASS sulfuric acid H2SO4 | got 98.072 | W1 98.072 | claim 98.072
PASS oxygen O2 | got 31.998 | W1 31.998 | claim 31.998
PASS nitrogen N2 | got 28.014 | W1 28.014 | claim 28.014
PASS carbon dioxide CO2 | got 44.009 | W1 44.009 | claim 44.009
PASS T1 checksum: sum of 22 masses in myu | got 17178130 | claim 17178130
s1 SUMMARY: 23 PASS, 0 FAIL (of 23 rows)
s1 crc32: ccd03c75
```

```text
=== E74-SD s2 — the ten balances re-derived vs the frozen masses (2026-11-05) ===
PASS E1 nitration: C12H11N + 2 HNO3 -> C12H9N3O4 + 2 H2O | L 295.251 = R 295.251 | claim 295.251 | W1 295.251/295.251
PASS E2 urea + 2 NaOH -> Na2CO3 + 2 NH3 | L 140.050 = R 140.050 | claim 140.050 | W1 140.050/140.050
PASS E3 urea + H2O -> 2 NH3 + CO2 | L 78.071 = R 78.071 | claim 78.071 | W1 78.071/78.071
PASS E4 N2 + O2 -> 2 NO | L 60.012 = R 60.012 | claim 60.012 | W1 60.012/60.012
PASS E5 2 NO + O2 -> 2 NO2 | L 92.010 = R 92.010 | claim 92.010 | W1 92.010/92.010
PASS E6 2 NO2 + H2O -> HNO3 + HNO2 | L 110.025 = R 110.025 | claim 110.025 | W1 110.025/110.025
PASS E7 3 HNO2 -> HNO3 + 2 NO + H2O | L 141.039 = R 141.039 | claim 141.039 | W1 141.039/141.039
PASS E8 HNO3 + NH3 -> NH4NO3 | L 80.043 = R 80.043 | claim 80.043 | W1 80.043/80.043
PASS E9 NH4NO3 -> N2O + 2 H2O | L 80.043 = R 80.043 | claim 80.043 | W1 80.043/80.043
PASS E10 H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O | L 178.066 = R 178.066 | claim 178.066 | W1 178.066/178.066
CAUGHT M1 | the unbalanced NH4NO3 -> N2O + H2O: L 80.043 vs R 62.028 | gap 18.015 g — exactly one water short, caught
PASS T2 checksum: sum of the ten balanced totals in myu | got 12546100 | claim 12546100
s2 SUMMARY: 11 PASS, 1 CAUGHT
s2 crc32: 37ce3e1e
```

```text
=== E74-SD s3 — the charge ledger re-derivation, every printed figure two-lane (2026-11-05) ===
claims = the frozen E73 s3 rows; inputs = the same stated figures; value lane = string-decimal, W1 = float64 witness
build history: the first s3 build had six mis-scaled row encodings (L20/L21/L22/L24/L25/L26) — caught by the W1 lane and the frozen claims, fixed same-session; engine core untouched (frozen at rev-2)
PASS L01 | the harvest: 2.05 g DNBP, theoretical UNSTATED — REFUSED stands (a yield needs a stated theoretical) | got REFUSED | W1 REFUSED | expect REFUSED
PASS L02 | the make-vs-buy: $163 per 50 mg / $0.25 per 50 mg | got 652x | W1 652x | expect 652x
PASS L03 | the honest total settles: $10 at $0.25 per 50 mg -> | got 2.0 g (vs 2.05 harvested, 2.4%) | W1 2.0 g (vs 2.05 harvested, 2.4%) | expect 2.0 g (vs 2.05 harvested, 2.4%)
PASS L04 | the urea charge: 75 g / 60.056 g/mol | got 1.249 mol | W1 1.249 mol | expect 1.249 mol
PASS L05 | the ammonia as stated: x 17.031 | got 21.27 g | W1 21.27 g | expect 21.27 g
PASS L06 | the full-basis seam: E3 makes TWO NH3 per urea -> | got 42.54 g | W1 42.54 g | expect 42.54 g
PASS L07 | the AN charge: 50 g / 80.043 g/mol | got 0.6247 mol | W1 0.6247 mol | expect 0.6247 mol
PASS L08 | the endotherm: x Ch 26's +25.7 kJ/mol | got 16.05 kJ | W1 16.05 kJ | expect 16.05 kJ
PASS L09 | the comma-drop settlement: 205,980 J = | got 205.98 kJ | W1 205.98 kJ | expect 205.98 kJ
PASS L10 | the COP machine-side: 16.0539 / 205.98 | got 7.79% | W1 7.79% | expect 7.79%
PASS L11 | the production ledger: 1.85 g/kWh x 0.2 kW | got 0.37 g/h | W1 0.37 g/h | expect 0.37 g/h
PASS L12 | x 24 h | got 8.88 g/day | W1 8.88 g/day | expect 8.88 g/day
PASS L13 | the industrial comparison: 1.85 / 60 | got 3.08% | W1 3.08% | expect 3.08%
PASS L14 | the flyback: 75 x 125 (the 8-turn/1000-turn ratio) | got 9375 V | W1 9375 V | expect 9375 V
PASS L15 | the collection: 700 mL of 7500 mL | got 9.33% (~10x, the honest estimate) | W1 9.33% (~10x, the honest estimate) | expect 9.33% (~10x, the honest estimate)
PASS L16 | the tare: 71 g total - 2 g bag | got 69 g net | W1 69 g net | expect 69 g net
PASS L17 | the cold-pack charge: 50 g in 80 mL | got 625 g/L | W1 625 g/L | expect 625 g/L
PASS L18 | the first batch: 3.2 g / 12 h | got 0.267 g/h (vs L11's 0.37 g/h ledger) | W1 0.267 g/h (vs L11's 0.37 g/h ledger) | expect 0.267 g/h (vs L11's 0.37 g/h ledger)
PASS L19 | the energy: 216 h x 225 W | got 48.6 kWh | W1 48.6 kWh | expect 48.6 kWh
PASS L20 | the cost: x $0.10/kWh | got $4.86 | W1 $4.86 | expect $4.86
PASS L21 | the per-gram: $4.86 / 24.75 g | got $0.196/g | W1 $0.196/g | expect $0.196/g
PASS L22 | the acid equivalent: 24.75 x 63.012 / 80.043 | got 19.48 g | W1 19.48 g | expect 19.48 g
PASS L23 | the rate: 19.4835 / 48.6 kWh | got 0.40 g/kWh | W1 0.40 g/kWh | expect 0.40 g/kWh
PASS L24 | the industrial gap: 60 / 0.4009 | got 149.7x | W1 149.7x | expect 149.7x
PASS L25 | the RFNA seam: 14.75 x 63.012 / 80.043 | got 11.61 g theoretical | W1 11.61 g theoretical | expect 11.61 g theoretical
PASS L26 | at the RFNA density 1.50 g/mL -> | got 7.74 mL (vs the stated 10 mL — the FLAGGED tension: water co-distillation or a lower density probable) | W1 7.74 mL (vs the stated 10 mL — the FLAGGED tension: water co-distillation or a lower density probable) | expect 7.74 mL (vs the stated 10 mL — the FLAGGED tension: water co-distillation or a lower density probable)
s3 SUMMARY: 26 PASS, 0 FAIL — 26 rows, every printed figure two-lane
s3 crc32: f65fca26
```

```text
=== E74-SD s4 — fresh injections, each must be caught (2026-11-05) ===
gate: the corrupted value must diverge from the frozen claim AND the honest value must equal the claim — anything else is an escape
CAUGHT I1 wrong-side COP: multiply where divide belongs (16.0539 x 205.98 as %) | honest 7.79 = claim; corrupted 330678.23 — caught
CAUGHT I2 swapped denominator: 205.98 / 16.0539 as % | honest 7.79 = claim; corrupted 1283.05 — caught
CAUGHT I3 dropped percent scale: 16.0539 / 205.98 left unscaled | honest 7.79 = claim; corrupted 0.0779 — caught
CAUGHT I4 off-by-one chain day: N171->N367 as 1253 d | honest 1254 = claim; corrupted 1253 — caught
CAUGHT I5 full-for-half basis swap: 42.54 g quoted where the stated figure is 21.27 g | honest 21.27 = claim; corrupted 42.54 — caught
CAUGHT I6 endotherm sign flip: -16.05 kJ for a +25.7 kJ/mol endotherm | honest 16.05 = claim; corrupted -16.05 — caught
CAUGHT I7 mL->L scale slip: the 7.74 mL figure rendered a thousandfold small | honest 7.74 = claim; corrupted 0.00774 — caught
CAUGHT I8 mass transposition: the 2.05 g harvest transposed to 20.5 g | honest 2.05 = claim; corrupted 20.5 — caught
s4 SUMMARY: 8 CAUGHT, 0 ESCAPED — 8 injections, zero escapes tolerated
s4 crc32: f0b36a0d
```

```text
=== E74-SD sR — the register settlement re-derivation (2026-11-05) ===
fresh civil-date method: Fliegel-Van Flandern JDN (truncating integer division) — a code path distinct from E73's days_from_civil; register = the frozen sR rows
build history: two successive S05 mis-encodings (1.85/10, then a spurious qnd /10 denominator around a plain product) — both caught by the register row, fixed same-session; engine core untouched (frozen at rev-2)
SETTLED S01 | the urea ledger: 75 g = 1.249 mol (batch 33cg, machine-checked at gather) | got 1.249 mol | register 1.249 mol
SETTLED S02 | the ammonia as stated ~= the in-source 21.3 g — EXACT at the stated basis | got 21.27 g | register 21.27 g
SETTLED S03 | the AN charge = 0.6247 mol | got 0.6247 mol | register 0.6247 mol
SETTLED S04 | x Ch 26's +25.7 kJ/mol ~= the in-source 'about 16.1' — EXACT | got 16.05 kJ | register 16.05 kJ
SETTLED S05 | the '37 G per hour' decimal-drop machine-resolved | got 0.37 g/h, x 24 = 8.88 g/day | register 0.37 g/h, x 24 = 8.88 g/day
SETTLED S06 | the industrial comparison — 'just over 3%' EXACT | got 3.08% | register 3.08%
SETTLED S07 | the flyback peak ~= 'about 9400 V' — the stated figure the honest round-up | got 9375 V | register 9375 V
SETTLED S08 | the Sigma economics, 50 mg for 50 mg | got 652x | register 652x
SETTLED S09 | the N367 stale-crawl ratio (watch 185,968 over crawl 60.6K) | got 3.0688x | register 3.0688x
SETTLED S10 | the N171 energy ledger | got 48.6 kWh, x $0.10 = $4.86 | register 48.6 kWh, x $0.10 = $4.86
SETTLED S11 | ~= 'roughly 20 cents' per gram | got $0.196/g | register $0.196/g
SETTLED S12 | ~= 'approximately 19.5 grams' of nitric acid | got 19.48 g | register 19.48 g
SETTLED S13 | the rate vs the industrial 60 g/kWh ('we are a little bit off') | got 0.40 g/kWh; 60 / 0.40 = 150x | register 0.40 g/kWh; 60 / 0.40 = 150x
SETTLED S14 | the RFNA theoretical cut vs the stated 10 mL — the FLAGGED tension standing, neither corrected | got 11.61 g / 1.50 = 7.74 mL | register 11.61 g / 1.50 = 7.74 mL
SETTLED S15 | the register's recorded tensions, printed as recorded — the episode's own basis not reconstructible, nothing adjudicated | got 2564 J/g stated vs 2571 machine-side (~0.3%); COP 7.85% stated vs 7.79% machine-side (~0.8%) | register 2564 J/g stated vs 2571 machine-side (~0.3%); COP 7.85% stated vs 7.79% machine-side (~0.8%)
SETTLED S16 | cyanotype Part 1 (Prussian Blue) -> Part 2 (the blueprint) [2018-05-28 -> 2018-06-10] | got 13 d | register 13 d
SETTLED S17 | Part 2 -> N368 (the color-changing plastic) [2018-06-10 -> 2018-06-28] | got 18 d | register 18 d
SETTLED S18 | N368 -> Part 3 (developing my own photos) [2018-06-28 -> 2018-08-06] | got 39 d | register 39 d
SETTLED S19 | Part 1 -> Part 3, the chain closing on itself EXACT [2018-05-28 -> 2018-08-06] | got 70 d = 70 d | register 70 d = 70 d
SETTLED S20 | N171 (the arc performer) -> N367 (the fridge performer) [2020-08-02 -> 2024-01-08] | got 1254 d | register 1254 d
sR SUMMARY: 20 SETTLED, 0 REFUSED — 20 rows, the register's recorded set re-settled by fresh arithmetic and a fresh civil-date method
sR crc32: 1899029e
```

```text
=== E74-SD s5 — determinism and digest verification (2026-11-05) ===
PASS D1 s4 double-execution byte-identical | two in-process executions, 1240 chars
PASS D2 sR double-execution byte-identical | two in-process executions, 3124 chars
PASS D3 s4 re-execution matches the frozen transcript on disk | builder output vs disk, byte-for-byte
PASS D4 sR re-execution matches the frozen transcript on disk | builder output vs disk, byte-for-byte
PASS G5 e74-s0.txt | recorded 711fdf24 | recomputed 711fdf24 (same domain, digest line excluded, strict equality)
PASS G5 e74-s1.txt | recorded ccd03c75 | recomputed ccd03c75 (same domain, digest line excluded, strict equality)
PASS G5 e74-s2.txt | recorded 37ce3e1e | recomputed 37ce3e1e (same domain, digest line excluded, strict equality)
PASS G5 e74-s3.txt | recorded f65fca26 | recomputed f65fca26 (same domain, digest line excluded, strict equality)
PASS G5 e74-s4.txt | recorded f0b36a0d | recomputed f0b36a0d (same domain, digest line excluded, strict equality)
PASS G5 e74-sR.txt | recorded 1899029e | recomputed 1899029e (same domain, digest line excluded, strict equality)
WHOLE BATTERY crc32 (six sheets concatenated, as written): 14515d26
s5 SUMMARY: 10 PASS, 0 FAIL
s5 crc32: ab883255
```
