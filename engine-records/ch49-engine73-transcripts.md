# Engine 73 Transcripts — E73-LD, the long-division rational engine (session 179, 2026-11-05)

Vol VII Ch 49 "Photochromism and Cold" authoring unit. Fresh engine, zero code shared with Engines 1-72. Design: exact rationals as coprime BigInt pairs normalized by iterative binary GCD; guarded cross-multiplication comparisons (10^24 guard, refuse rather than approximate); digit-by-digit long-division render with exact half-up; no float in the value path; W1 float64 witness (typed from independent decimal constants); W2 fixed-scale integer render witness; two-pass table-driven atom parser (validate/tokenize, then frame-stack accumulation, no AST, no recursion); P18 NAME gate first; held table in micro-y (C 120110, H 10080, N 140070, O 159990, S 320600, Na 229900, Cl 354530, Mg 243050); digest Adler-32 (mod 65521), distinct from FNV-1a/j31/joat/sdbm; integer civil-date ordinals for the chains.

Honest run history: rev-0 the trailing group subscript read nowhere — (NH2)2 counted once, urea 44.033 vs 60.056, both lanes wrong together (W1 shares the parser; caught by the s1 urea row at the Ch 20 pin; lesson: claims catch formula defects); rev-1 the multiplier set after the frame merged — same 44.033, caught again; rev-2 the lookahead close — clean; rev-3 the constructor refused decimal literals (caught at L02's $0.25; three percent-scale rows and the mg-to-g scale fixed in the same pass); rev-4 the dp=0 render appended a bare "." on nonzero remainder (caught by S13 refusing "150."); rev-5 the G5 gate — digest domains differed by construction and endsWith("MATCH") admitted "MISMATCH" — fixed to same-domain recompute with strict equality. The sheets below are the frozen clean battery, written as they were generated (scratch is not storage) and spliced byte-verbatim.

Manifest: s0 the probe (5 PASS + 1 CAUGHT, adler32 04a8043c); s1 the molar book (22/22, T1 17178130 myu, adler32 ded3323c); s2 the balances (10 PASS + 1 CAUGHT must-fail, T2 12546100 myu, adler32 7703688d); s3 the charge ledger (26/26, adler32 1c638d84); s4 the injections (8/8 CAUGHT, adler32 7d7b5d59); sR the register settlement (20/20 SETTLED, adler32 9b55006c); s5 determinism (s4/sR byte-identical double execution; G5 all six sheets recompute MATCH from disk; whole battery adler32 9de4accb). Verdict: ZERO ARITHMETIC FINDINGS.

---

```text
=== E73-LD s0 — the probe, rev-2 battery (2026-11-05) ===
PASS P1 | long-division half-up: 2/3 at 3 dp | got 0.667 | expect 0.667
PASS P2 | exact tail: 1/8 terminates | got 0.125 | expect 0.125
PASS P3 | repeating tail at 6 dp | got 0.333333 | expect 0.333333
PASS P4 | the held table prices water at the book's own pin | got 18.015 | expect 18.015
PASS P5 | the rev-0/rev-1 defect row, now priced by the frame stack: urea at its Ch 20 pin | got 60.056 | expect 60.056
CAUGHT  SF | the seeded truncation lane: trunc 0.666 vs half-up witness 0.667 — the witness caught it, as designed
s0 SUMMARY: 5 PASS, 1 CAUGHT (the seeded fault among them)
s0 adler32: 04a8043c
```

```text
=== E73-LD s1 — the molar book, rev-2 battery (2026-11-05) ===
PASS C12H9N3O4   M = 259.221 g/mol  [W1 259.221]  DNBP, the photochrom — NEW, zero-hit at the 101-file corpus
PASS C12H11N     M = 169.227 g/mol  [W1 169.227]  2-benzylpyridine, the feed — NEW, zero-hit
PASS C5H5N       M = 79.102 g/mol  [W1 79.102]  pyridine, the parent ring — NEW, zero-hit
PASS CO(NH2)2    M = 60.056 g/mol  [W1 60.056]  urea — PIN, Ch 20's fixed-N bench (re-pinned Ch 46)
PASS NH4NO3      M = 80.043 g/mol  [W1 80.043]  ammonium nitrate — PIN, Ch 15 (Ch 20: the cold pack's salt)
PASS NH3         M = 17.031 g/mol  [W1 17.031]  ammonia — PIN, Ch 20
PASS HNO3        M = 63.012 g/mol  [W1 63.012]  nitric acid — PIN, Ch 15 (the strong-acid ladder)
PASS HNO2        M = 47.013 g/mol  [W1 47.013]  nitrous acid — PIN, Ch 20 (the nitrification waystation)
PASS NO          M = 30.006 g/mol  [W1 30.006]  nitric oxide — PIN, Ch 3 (Ch 20: never generated)
PASS NO2         M = 46.005 g/mol  [W1 46.005]  nitrogen dioxide — PIN, Ch 3 (Ch 20: never generated)
PASS N2O         M = 44.013 g/mol  [W1 44.013]  nitrous oxide — PIN, Ch 20 (recognition-only)
PASS NaNO3       M = 84.994 g/mol  [W1 84.994]  sodium nitrate — PIN, Ch 27 (Ch 31 names the owner)
PASS NH4Cl       M = 53.492 g/mol  [W1 53.492]  sal ammoniac — PIN, Ch 19 (Ch 20: the white bottle)
PASS MgSO4       M = 120.361 g/mol  [W1 120.361]  the drying agent — PIN, Ch 4 (Epsom 246.466)
PASS C4H10O      M = 74.123 g/mol  [W1 74.123]  diethyl ether — PIN, Ch 21 (the flammable shelf)
PASS NaOH        M = 39.997 g/mol  [W1 39.997]  lye — PIN, Ch 8
PASS Na2CO3      M = 105.988 g/mol  [W1 105.988]  soda ash — PIN, Ch 8
PASS Na2SO4      M = 142.036 g/mol  [W1 142.036]  the quench's salt — PIN, Ch 13/14 (Ch 15 names the owners)
PASS H2SO4       M = 98.072 g/mol  [W1 98.072]  sulfuric acid — PIN, Ch 6
PASS O2          M = 31.998 g/mol  [W1 31.998]  oxygen — PIN, Ch 10
PASS N2          M = 28.014 g/mol  [W1 28.014]  nitrogen — PIN, Ch 10
PASS CO2         M = 44.009 g/mol  [W1 44.009]  carbon dioxide — PIN, Ch 20
s1 SUMMARY: 22/22 PASS — CLEAN
s1 T1 composition checksum (sum of the 22 masses, myu): 17178130
s1 adler32: ded3323c
```

```text
=== E73-LD s2 — the balances, atom-multiset-gated (2026-11-05) ===
PASS E1 the nitration :: C12H11N + 2 HNO3 -> C12H9N3O4 + 2 H2O | 295.251 = 295.251 g/mol | atoms OK | charge 0=0 | the episode's genuine synthesis, priced
PASS E2 the alkaline door :: CO(NH2)2 + 2 NaOH -> Na2CO3 + 2 NH3 | 140.050 = 140.050 g/mol | atoms OK | charge 0=0 | the urea-to-ammonia ladder the episode climbs
PASS E3 hydrolysis :: CO(NH2)2 + H2O -> 2 NH3 + CO2 | 78.071 = 78.071 g/mol | atoms OK | charge 0=0 | the gentler corridor (FC5's B1, re-derived here)
PASS E4 the arc's first bond :: N2 + O2 -> 2 NO | 60.012 = 60.012 g/mol | atoms OK | charge 0=0 | recognition-only (Ch 20's never-generate line)
PASS E5 the brown gate :: 2 NO + O2 -> 2 NO2 | 92.010 = 92.010 g/mol | atoms OK | charge 0=0 | recognition-only
PASS E6 the absorption :: 2 NO2 + H2O -> HNO3 + HNO2 | 110.025 = 110.025 g/mol | atoms OK | charge 0=0 | recognition-only (the episode's mixed-acid claim)
PASS E7 the waystation decays :: 3 HNO2 -> HNO3 + 2 NO + H2O | 141.039 = 141.039 g/mol | atoms OK | charge 0=0 | recognition-only ('the latter slowly decomposing into the former')
PASS E8 the neutralization :: HNO3 + NH3 -> NH4NO3 | 80.043 = 80.043 g/mol | atoms OK | charge 0=0 | the purity-by-construction argument's own door
PASS E9 the thermal face :: NH4NO3 -> N2O + 2 H2O | 80.043 = 80.043 g/mol | atoms OK | charge 0=0 | recognition-only (Ch 20's E23, the AN safety lecture)
PASS E10 the quench :: H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O | 178.066 = 178.066 g/mol | atoms OK | charge 0=0 | the DNBP workup's neutralization door
CAUGHT M1 the must-fail :: NH4NO3 -> N2O + H2O | one water short by design | gap 18.015 g = exactly one H2O (18.015)
s2 SUMMARY: 10 PASS, 1 CAUGHT (the must-fail by design) — 10 balances + 1 must-fail, all adjudicated
s2 T2 mass checksum (sum of the 10 balance left-side masses, myu): 12546100
s2 adler32: 7703688d
```

```text
=== E73-LD s3 — the charge ledger, every printed figure two-lane (2026-11-05) ===
-- N368 (NileRed, the color-changing plastic) --
PASS L01 | the harvest: 2.05 g DNBP, theoretical UNSTATED — the honest gap | got REFUSED (no theoretical in the record — a yield is not computable) | expect REFUSED (no theoretical in the record — a yield is not computable)
PASS L02 | the make-vs-buy: $163 per 50 mg / $0.25 per 50 mg | got 652x | expect 652x
PASS L03 | the honest total settles: $10 at $0.25 per 50 mg -> | got 2.0 g — against the 2.05 g harvested (2.4%, inside 'I don't really have exact numbers') | expect 2.0 g — against the 2.05 g harvested (2.4%, inside 'I don't really have exact numbers')
-- N367 (Hyperspace Pirate, the pee fridge) --
PASS L04 | the urea charge: 75 g / 60.056 g/mol | got 1.249 mol | expect 1.249 mol
PASS L05 | the ammonia as stated: x 17.031 | got 21.27 g | expect 21.27 g
PASS L06 | the full-basis seam: E3 makes TWO NH3 per urea -> | got 42.54 g | expect 42.54 g
PASS L07 | the AN charge: 50 g / 80.043 g/mol | got 0.6247 mol | expect 0.6247 mol
PASS L08 | the endotherm: x Ch 26's +25.7 kJ/mol | got 16.05 kJ | expect 16.05 kJ
PASS L09 | the comma-drop settlement: 205,980 J = | got 205.98 kJ | expect 205.98 kJ
PASS L10 | the COP machine-side: 16.0539 / 205.98 | got 7.79% | expect 7.79%
PASS L11 | the production ledger: 1.85 g/kWh x 0.2 kW | got 0.37 g/h | expect 0.37 g/h
PASS L12 | x 24 h | got 8.88 g/day | expect 8.88 g/day
PASS L13 | the industrial comparison: 1.85 / 60 | got 3.08% | expect 3.08%
PASS L14 | the flyback: 75 x 125 (the 8-turn/1000-turn ratio) | got 9375 V | expect 9375 V
PASS L15 | the collection: 700 mL of 7500 mL | got 9.33% (~10x, the honest estimate) | expect 9.33% (~10x, the honest estimate)
PASS L16 | the tare: 71 g total - 2 g bag | got 69 g net | expect 69 g net
PASS L17 | the cold-pack charge: 50 g in 80 mL | got 625 g/L | expect 625 g/L
PASS L18 | the first batch: 3.2 g / 12 h | got 0.267 g/h (vs L11's 0.37 g/h ledger) | expect 0.267 g/h (vs L11's 0.37 g/h ledger)
-- N171 (DBX Labs, the arc-fixation economics) --
PASS L19 | the energy: 216 h x 225 W | got 48.6 kWh | expect 48.6 kWh
PASS L20 | the cost: x $0.10/kWh | got 4.86 | expect 4.86
PASS L21 | the per-gram: $4.86 / 24.75 g | got 0.196 $/g | expect 0.196 $/g
PASS L22 | the acid equivalent: 24.75 x 63.012 / 80.043 | got 19.48 g | expect 19.48 g
PASS L23 | the rate: 19.4835 / 48.6 kWh | got 0.40 g/kWh | expect 0.40 g/kWh
PASS L24 | the industrial gap: 60 / 0.4009 | got 149.7x | expect 149.7x
PASS L25 | the RFNA seam: 14.75 x 63.012 / 80.043 | got 11.61 g theoretical | expect 11.61 g theoretical
PASS L26 | at the RFNA density 1.50 g/mL -> | got 7.74 mL (vs the stated 10 mL — the FLAGGED tension: water co-distillation or a lower density probable) | expect 7.74 mL (vs the stated 10 mL — the FLAGGED tension: water co-distillation or a lower density probable)
s3 SUMMARY: 26 PASS, 0 FAIL — 26 rows, every printed figure two-lane
s3 adler32: 1c638d84
```

```text
=== E73-LD s4 — the injections, eight fresh-keyed corruptions (2026-11-05) ===
CAUGHT I1 | DNBP mass, digits transposed | engine got 259.221 | corrupted expect 259.212
CAUGHT I2 | urea mass, digits transposed | engine got 60.056 | corrupted expect 60.065
CAUGHT I3 | pyridine mass, digits transposed | engine got 79.102 | corrupted expect 79.012
CAUGHT I4 | the make-vs-buy ratio, digits transposed | engine got 652x | corrupted expect 625x
CAUGHT I5 | the endotherm, a dropped digit | engine got 16.05 kJ | corrupted expect 16.5 kJ
CAUGHT I6 | the energy ledger, scale slipped | engine got 48.6 kWh | corrupted expect 4.86 kWh
CAUGHT I7 | the arc-to-fridge chain, digits transposed | engine got 1254 d | corrupted expect 1245 d
CAUGHT I8 | the COP, a digit invented | engine got 7.79% | corrupted expect 7.97%
s4 SUMMARY: 8 CAUGHT, 0 escaped — 8/8 fresh-keyed corruptions refused
s4 adler32: 7d7b5d59
```

```text
=== E73-LD sR — the register settlement (2026-11-05) ===
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
SETTLED S11 | ~= 'roughly 20 cents' per gram | got 0.196 $/g | register 0.196 $/g
SETTLED S12 | ~= 'approximately 19.5 grams' of nitric acid | got 19.48 g | register 19.48 g
SETTLED S13 | the rate vs the industrial 60 g/kWh ('we are a little bit off') | got 0.40 g/kWh; 60 / 0.40 = 150x | register 0.40 g/kWh; 60 / 0.40 = 150x
SETTLED S14 | the RFNA theoretical cut vs the stated 10 mL — the FLAGGED tension standing, neither corrected | got 11.61 g / 1.50 = 7.74 mL | register 11.61 g / 1.50 = 7.74 mL
SETTLED S15 | the register's recorded tensions, printed as recorded — the episode's own basis not reconstructible, nothing adjudicated | got 2564 J/g stated vs 2571 machine-side (~0.3%); COP 7.85% stated vs 7.79% machine-side (~0.8%) | register 2564 J/g stated vs 2571 machine-side (~0.3%); COP 7.85% stated vs 7.79% machine-side (~0.8%)
SETTLED S16 | cyanotype Part 1 (Prussian Blue) -> Part 2 (the blueprint) | got 13 d | register 13 d
SETTLED S17 | Part 2 -> N368 (the color-changing plastic) | got 18 d | register 18 d
SETTLED S18 | N368 -> Part 3 (developing my own photos) | got 39 d | register 39 d
SETTLED S19 | Part 1 -> Part 3, the chain closing on itself EXACT | got 70 d = 70 d | register 70 d = 70 d
SETTLED S20 | N171 (the arc performer) -> N367 (the fridge performer) | got 1254 d | register 1254 d
sR SUMMARY: 20 SETTLED, 0 REFUSED — 20 rows, the register's recorded set re-settled by fresh arithmetic
sR adler32: 9b55006c
```

```text
=== E73-LD s5 — the determinism proof and the whole-battery digest (2026-11-05) ===
G3a s4 double execution: byte-identical
G3b sR double execution: byte-identical
G5 e73-s0.txt: recorded 04a8043c, recomputed 04a8043c MATCH
G5 e73-s1.txt: recorded ded3323c, recomputed ded3323c MATCH
G5 e73-s2.txt: recorded 7703688d, recomputed 7703688d MATCH
G5 e73-s3.txt: recorded 1c638d84, recomputed 1c638d84 MATCH
G5 e73-s4.txt: recorded 7d7b5d59, recomputed 7d7b5d59 MATCH
G5 e73-sR.txt: recorded 9b55006c, recomputed 9b55006c MATCH
G5 SUMMARY: all six sheets' recorded adler32 digests recompute MATCH from disk (same domain, digest line excluded) — the transcripts are the battery
WHOLE BATTERY: e73-s0.txt + e73-s1.txt + e73-s2.txt + e73-s3.txt + e73-s4.txt + e73-sR.txt — 11194 chars, 121 lines
WHOLE BATTERY adler32: 9de4accb
s5 adler32: b5115ef6
```
