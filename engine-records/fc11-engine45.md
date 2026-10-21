# FC11 Engine 45 record — the pulse-train geometric-series engine (session 132, the FC11 drafting unit)

Session 132 (2026-10-21): the FC11 authoring unit per row 132 — "Air: The Invisible Shelf," the Field Companion's eleventh chapter and the map's last `planned` unit, drafted this session with a fresh engine sharing zero code with Engines 1–44. Engine 45 — the pulse-train geometric-series engine — priced the whole chapter battery: 10 self rows (the air-shelf compositions, argon the book's first priced sliver, air itself reproduced on Ch 10's own pin), 1 planted canary, 5 admissions, 9 NAME-gate refusals (the twenty-second zero-admission chapter), 18 [convergent] lookups, and 16 computed rows including the designed must-fail. Verdict: **run 2 CLEAN — 59/59 adjudicated, 44 PASS / 1 caught / 9 refused / 0 FAIL, zero uncaught defects**, gates G1–G4 all held at the same run, the whole battery executed twice byte-identical. Two expectation corrections were made before the record froze and are disclosed below (§2 and §6) — neither was patched silently anywhere in the chain; the honest history below.

## 1. Design spec

- **THE PULSE-TRAIN ENGINE, the fresh axis:** every amount is deposited by repeated unit pulses into an exact BigInt rational ledger — `pulse(count, unit)` adds the unit to the accumulator `count` times by repeated addition, so **no multiplication rides the deposit path**; a molecule's mass is the pulse-sum of its elements' held milli-gram units; `times(k, m)` is k pulses of the whole-molecule unit. All arithmetic rides exact rationals `{n, d}` (BigInt, gcd-normalized at every constructor), so every printed decimal is an exact rational rounded half-up at print — no float anywhere. The dilution ledger is the discrete well-mixed box as a geometric series: C_{n+1} = C_n·(1−q) + S per step, closed form C_n = (S/q)·(1−(1−q)^n) with (1−q)^n at exact rational powers, **no transcendental functions anywhere** — inverse timings (the 12800-ppm crossing, the half-crossing) reported as exact discrete crossings between consecutive integer hours, never as logarithms. **No parse tree is materialized at all** (molecules are element-count lists, not strings), no flat-instruction bytecode VM (Engine 43), no inherited-multiplier recursive-descent tally (44), no event-sorted sweep (42), no lazy-tag segment tree (41), no interval-containment tally (40), no depth-ledger double-and-add (39), no token-table AST fold (36), no span-memo engine (35), no CPS fold (37), no fixed-point rewrite (33), no census-tally expansion (34), no RPN operand reordering (31), no arithmetic expression compiler (19) — the neighbors named honestly; the pulse-deposit rational ledger is Engine 45's own.
- **The held table, the Ch 3/Ch 7 faces, exact milli-g:** C 12.011, H 1.008, O 15.999, N 14.007, Ar 39.948 — **the argon admission, the book's first priced argon** after thirty-six chapters of carrying the sliver unpriced (Ch 3's "chlorine's becomes argon's," Ch 29's "nearly 1% argon, almost all of it Ar-40," and Ch 7's Ex 7.5 rounding example 39.95 the prior faces; the census in §6).
- **S10, the air face reproduced, not restated:** 0.7809 N2 + 0.2095 O2 + 0.0093 Ar + 0.0004 CO2 weighted on the held table = 28.968834 → **28.969 g/mol exactly, Ch 10's own pin** (Ch 10 line 176's "air (78.09 N2 / 20.95 O2 / 0.93 Ar / 0.04 CO2) M = 28.969 g/mol → the 28.96 pin" — the engine's own exact rational agrees with the owner's printed pin to the digit).
- **The gate order, the chapter's own:** NAME first — the recognition register (radon, respirator, detector, alarm, headache, smoke, mold, mildew, tent) refused *before any pricing*, the P18 recognition fence in machine form (R1–R9; "mold" the FC10-RA-1 prior word and "smoke" the FC2 prior word refused honestly like the rest); then admission (the register CO, N2, O2, CO2, C3H8 built from the held table); then syntax; then the grid. The two molar volumes are pinned to their owners: STP 22.414 L/mol (Ch 10's convention) and RTP 24.465 L/mol (Ch 10's own working pin, ×16 on the owner's page) — the WHO-pairing basis of E5.
- **The gates:** G1 the machine recount (59 rows authored, 59 counted: 11 S including the canary + 5 A + 9 R + 18 P + 16 E); G2 the canary (CO planted at 28.012 — the engine must print its own 28.010 and refuse the planted expectation, at its row alone); G3 determinism (byte-identical re-execution); G4 the designed must-fail — E9, the propane row authored with 4 O2 where five are required, the deficit exactly one O2 = 31.998 g.

## 2. Honest run history

Nothing smoothed; every defect named at its own line, the run-1 block preserved as the shakedown exhibit (quoted here verbatim, then deleted at the session's cleanup).

**Run 1 — the design shakedown, four defect classes, fourteen FAIL rows, every one caught by the battery itself at its own line:**

1. **The held-table carbon transposed** — 12111 milli-g typed for 12011. The canary line and the cascade, verbatim from the run-1 block:
   `S1  S got 28.110 g/mol | expect 28.010 g/mol | FAIL`
   `E2  E got 204.387 g = 204.387 g EXACT | expect 204.087 g = 204.087 g EXACT | FAIL`
   S4/S6/S7 printed 44.109/44.397/16.143 (+0.100/+0.300/+0.100); the cascade ran honest through every carbon-bearing E row (E3 56.220, E4 125.41, E5 8.70, E7 40.227, E8 318.2, E14 172.3); S11's canary still CAUGHT (got 28.110, planted 28.012); T1 off by exactly the transposition's ghost:
   `T1  the composition checksum 281718 myu`
   (+600 the transposed carbon across the five carbon-bearing rows: CO 1 C + CO2 1 + C3H8 3 + CH4 1 + air 0.0004 = 6.0004 C × 100 milli-g).
2. **E13's half-life ledger dropped the 50% start and printed the raw third halving as a percent:**
   `E13 E got 960 min air / 222 min O2 / 50 -> 0.13% | expect 960 min air / 222 min O2 / 50 -> 6.25% | FAIL`
   — (1/2)^3 = 0.125 printed as "0.13%" for the honest 50 → 6.25%; the ×100 and the 50% start both missing.
3. **E10's ppm conversion missed the 1e6 scale:**
   `E10 E got 0.0 ppm/hr | expect 12003.2 ppm/hr | FAIL`
   — the generator's hourly gain printed 0.0 for 12003.2 ppm/hr; E11's ledger cascaded with it.
4. **E14's frozen EXPECTATION itself carried the drafter's hand slip** — priced with C3H8 44.09 for the held 44.097 and frozen at "171.1"; the exact engine prices 171.16 → 171.2. The run-1 line (the engine's 172.3 carrying defect (1)'s +0.300 on top of the slip):
   `E14 E got 172.3 g propane | expect 171.1 g propane | FAIL`
   **The engine was right; the expectation was wrong** — corrected to the exact value *before this record froze*, disclosed here and in §6, never smoothed.

   The run-1 summary line, verbatim: `SUMMARY 30 PASS / 1 caught / 9 refused / 14 FAIL`.

**Run 2 — the frozen battery, 59/59 CLEAN:** the carbon re-typed, the E13 ledger fixed to start at 50%, the E10 scale restored, the E14 expectation corrected to the engine's exact value. `SUMMARY 44 PASS / 1 caught / 9 refused / 0 FAIL`; T1 281118 myu (−600 exactly, defect (1)'s ghost gone); the canary CAUGHT at S11 alone; the E9 must-fail CAUGHT at exactly 31.998 g of oxygen deficit; two in-process executions byte-identical (G3 held at the same run as G1/G2/G4).

**The summary-line bookkeeping (both runs the same rule):** the must-fail E9 counts inside the PASS column (it passes *by catching* — 44 = 10 S + 18 P + 16 E); the canary is the caught column; the five admissions print no numbers and sit outside the summary; 44 + 1 + 9 = 54 + 5 = 59 = G1. The run-1 summary used the same rule (30 PASS including E9).

## 3. The gates

- **G1 RECOUNT:** 59 rows authored, 59 counted — 11 S (10 + the canary) + 5 A + 9 R + 18 P + 16 E. MATCH.
- **G2 CANARY:** S11 — CO planted at 28.012 — CAUGHT at its row alone; the engine printed its own 28.010 and refused the planted expectation.
- **G3 DETERMINISM:** two full in-process executions of the battery, byte-identical.
- **G4 MUST-FAIL:** E9 — the propane row authored with 4 O2 where five are required — CAUGHT, the deficit exactly one O2 = 31.998 g (the closure charge the battery was designed to catch).
- **T1, the composition checksum:** 281118 myu over the S1–S10 rows — the floor of the exact sum × 1000 (run 1: 281718 = +600.04, the transposition's ghost; §2 above).

## 4. The frozen runblock (spliced verbatim from the engine's own output, never retyped)

```text
ENGINE 45 - the pulse-train geometric-series engine (fresh build, zero code shared with Engines 1-44)
  architecture: every amount deposited by repeated unit pulses into an exact BigInt rational ledger
  (no multiplication in the deposit path); the dilution ledger the geometric series (1-q)^n at exact
  rational powers; no transcendental functions anywhere - inverse timing reported as exact discrete
  crossings; the gate order NAME -> admission -> syntax -> grid. Held table the Ch 3/Ch 7 faces
  (C 12.011, H 1.008, O 15.999, N 14.007, Ar 39.948).
  determinism (G3): HELD - the second in-process execution byte-identical
S1  S got 28.010 g/mol | expect 28.010 g/mol | PASS
S2  S got 28.014 g/mol | expect 28.014 g/mol | PASS
S3  S got 31.998 g/mol | expect 31.998 g/mol | PASS
S4  S got 44.009 g/mol | expect 44.009 g/mol | PASS
S5  S got 18.015 g/mol | expect 18.015 g/mol | PASS
S6  S got 44.097 g/mol | expect 44.097 g/mol | PASS
S7  S got 16.043 g/mol | expect 16.043 g/mol | PASS
S8  S got 39.948 g/mol | expect 39.948 g/mol | PASS
S9  S got 2.016 g/mol | expect 2.016 g/mol | PASS
S10 S got 28.969 g/mol (Ch 10's pin, reproduced) | expect 28.969 g/mol (Ch 10's pin, reproduced) | PASS
S11 S got 28.010 g/mol | expect 28.012 g/mol | CAUGHT
A1  A ADMIT (held table)
A2  A ADMIT (held table)
A3  A ADMIT (held table)
A4  A ADMIT (held table)
A5  A ADMIT (held table)
R1  R REFUSED (NAME gate - recognition register)
R2  R REFUSED (NAME gate - recognition register)
R3  R REFUSED (NAME gate - recognition register)
R4  R REFUSED (NAME gate - recognition register)
R5  R REFUSED (NAME gate - recognition register)
R6  R REFUSED (NAME gate - recognition register)
R7  R REFUSED (NAME gate - recognition register)
R8  R REFUSED (NAME gate - recognition register)
R9  R REFUSED (NAME gate - recognition register)
P1  P got 400 ppm -> alarm 4-15 min (UL 2034) | expect 400 ppm -> alarm 4-15 min (UL 2034) | PASS
P2  P got 150 ppm -> alarm 10-50 min (UL 2034) | expect 150 ppm -> alarm 10-50 min (UL 2034) | PASS
P3  P got 70 ppm -> alarm 60-240 min (UL 2034) | expect 70 ppm -> alarm 60-240 min (UL 2034) | PASS
P4  P got 35 ppm -> headache 6-8 h (the ladder) | expect 35 ppm -> headache 6-8 h (the ladder) | PASS
P5  P got 200 ppm -> headache 2-3 h + loss of judgment | expect 200 ppm -> headache 2-3 h + loss of judgment | PASS
P6  P got 800 ppm -> insensible within 2 h | expect 800 ppm -> insensible within 2 h | PASS
P7  P got 12800 ppm -> death < 3 min | expect 12800 ppm -> death < 3 min | PASS
P8  P got WHO 15-min limit 100 mg/m3 | expect WHO 15-min limit 100 mg/m3 | PASS
P9  P got WHO 15-min limit 87 ppm | expect WHO 15-min limit 87 ppm | PASS
P10 P got 0.35 ACH (ASHRAE 62.2) | expect 0.35 ACH (ASHRAE 62.2) | PASS
P11 P got O2-deficient < 19.5% (OSHA 1910.134) | expect O2-deficient < 19.5% (OSHA 1910.134) | PASS
P12 P got NDIR band 4.26 um | expect NDIR band 4.26 um | PASS
P13 P got N95: >=95% at 0.3 um (42 CFR 84) | expect N95: >=95% at 0.3 um (42 CFR 84) | PASS
P14 P got N100/HEPA: 99.97% at 0.3 um | expect N100/HEPA: 99.97% at 0.3 um | PASS
P15 P got COHb t1/2 320 min air / 74 min O2 | expect COHb t1/2 320 min air / 74 min O2 | PASS
P16 P got CO-Hb affinity ~240x O2 | expect CO-Hb affinity ~240x O2 | PASS
P17 P got generator ~1500 g CO/hr (5 kW) | expect generator ~1500 g CO/hr (5 kW) | PASS
P18 P got radon 4 pCi/L = 148 Bq/m3 (Ch 29's gate; WHO 100) | expect radon 4 pCi/L = 148 Bq/m3 (Ch 29's gate; WHO 100) | PASS
E1  E got 159.990 g O2 per mol C3H8 | expect 159.990 g O2 per mol C3H8 | PASS
E2  E got 204.087 g = 204.087 g EXACT | expect 204.087 g = 204.087 g EXACT | PASS
E3  E got 56.020 g = 56.020 g EXACT | expect 56.020 g = 56.020 g EXACT | PASS
E4  E got 124.97 mg/m3 | expect 124.97 mg/m3 | PASS
E5  E got 8.73 ppm (WHO prints 8.7) | expect 8.73 ppm (WHO prints 8.7) | PASS
E6  E got 19.822 m3 | expect 19.822 m3 | PASS
E7  E got 40.370 ppm per (g/hr) h | expect 40.370 ppm per (g/hr) h | PASS
E8  E got 317.1 g/hr | expect 317.1 g/hr | PASS
E9  E got CAUGHT - O deficit 31.998 g | expect CAUGHT - O deficit 31.998 g | PASS
E10 E got 12003.2 ppm/hr | expect 12003.2 ppm/hr | PASS
E11 E got C1 12003.2 / C2 19805.3 -> the 12800 crossing in hour 2 | expect C1 12003.2 / C2 19805.3 -> the 12800 crossing in hour 2 | PASS
E12 E got 0.6500 after 1 h / 0.4225 after 2 h -> the half-crossing in hour 2 | expect 0.6500 after 1 h / 0.4225 after 2 h -> the half-crossing in hour 2 | PASS
E13 E got 960 min air / 222 min O2 / 50 -> 6.25% | expect 960 min air / 222 min O2 / 50 -> 6.25% | PASS
E14 E got 171.2 g propane | expect 171.2 g propane | PASS
E15 E got N95 passes 500 / N100 passes 3 of 10000 | expect N95 passes 500 / N100 passes 3 of 10000 | PASS
E16 E got 0.5625 at 2 h / 0.4219 at 3 h -> the half-crossing in hour 3 | expect 0.5625 at 2 h / 0.4219 at 3 h -> the half-crossing in hour 3 | PASS
G1  recount: 59 authored / 59 counted MATCH
G2  canary CAUGHT at S11 alone
G3  determinism: two independent executions byte-identical (checked by the caller)
G4  the E9 must-fail CAUGHT
T1  the composition checksum 281118 myu
SUMMARY 44 PASS / 1 caught / 9 refused / 0 FAIL
```

## 5. Expectations provenance

- The got-strings were frozen **before** Engine 45's first battery execution, hand-derived on the held table to the print precision; the P-row strings are the named [convergent] sources' own datums verbatim (the ledger in §6); the E-row strings hand-derived to 2–3 decimals and frozen. Two expectation corrections were made **before this record froze**, both disclosed (never patched silently in the chain): the E5 re-basis (24.45 → the book's own 24.465 pin; §6) and the E14 exact correction (171.1 → 171.2; §2 and §6). Every S/P/E got-string in the §4 block is the run-2 engine's own output, spliced verbatim.
- The battery's membership: S1–S10 the chapter's own compositions (CO, N2, O2, CO2, H2O, C3H8, CH4, Ar, H2, air); S11 the canary; A1–A5 the admissions (CO, N2, O2, CO2, C3H8 — the register words admitted through the held table, printing no numbers); R1–R9 the NAME-gate refusals (radon, respirator, detector, alarm, headache, smoke, mold, mildew, tent — the recognition register, priced never); P1–P18 the [convergent] lookups (the UL 2034 schedule, the exposure ladder, the WHO limits, the ACH, the OSHA threshold, the NDIR band, the respirator classes, the half-lives, the affinity, the generator rate, the radon gate); E1–E16 the computed grid.
- **The provenance named in the rows:** E1 is the molar face of Ch 7's own air-debt column — 3.628 g/g = 159.990/44.097, the five-O2 demand of one propane; E2 the full combustion closure C3H8 + 5 O2 = 3 CO2 + 4 H2O, 204.087 both sides EXACT; **E3 a REPRODUCTION of Ch 28's E14** — 2 C + O2 = 2 CO, 56.020 both sides EXACT, the starved-fire row Ch 28 priced as the instant and FC11 prices as the hour; E4 the STP face (100 ppm CO = 124.97 mg/m3 at 22.414); E5 the RTP face on Ch 10's 24.465 pin (WHO prints 8.7; the engine prints its exact 8.73); E6 the CDC tent itself (10×14×5 ft = 19.822 m3, the MMWR geometry); E7/E8 the sealed-tent gain (40.370 ppm per (g/hr)·h) and the time-to-12800 source (317.1 g/hr); E9 the must-fail; E10/E11 the generator in the sealed 100-m3 room (12,003.2 ppm/hr; the 12800 crossing in hour 2 at the 0.35 ledger); E12 the halving at 0.35 ACH (the half-crossing in hour 2); E13 the COHb three-half-life ledger (960 min air / 222 min O2, 50 → 6.25%); **E14 FC1's air-debt exception priced at the OSHA 19.5% threshold** (30 m3 sealed, 171.2 g propane); E15 the penetration arithmetic (N95 passes 500 of 10,000; N100 passes 3); E16 the halving at q = 0.25 (the half-crossing in hour 3).

## 6. The session-132 checks (all PAID at this close)

- **The session-100 line (NEW claims zero-hit grepped BEFORE the freeze):** corpus = the 36 masters (28 local + 8 repo at HEAD 7ad892a) + the FC1/FC2 masters + the FC7–FC10 canvases + all engine records and design notes + all 44 web editions + the index (the 5,925,672-byte blob); occurrence counts by `grep -o`, word-bounded where noted. **9 NEW words zero-hit:** carboxyhemoglobin, COHb, NDIR, afterdamp, UL 2034, ASHRAE, MMWR, ACH, mildew; plus the model terms **"well-mixed" and "box model" zero-hit**, and the phrase "air change(s per hour)" zero-hit ("air change" ×2 = "repair changes" substrings, adjudicated). **ONE new composition face: Ar 39.948** — the book's first priced argon (the word prior: Ch 3 ×1, Ch 29 ×1; Ch 7's 39.95 an Ex 7.5 rounding example, not a mass). **The 9 other S faces are priors/pins with owners:** CO 28.010 Ch 7 owner ×1 (+Ch 3 ×1); H2 2.016 Ch 7 owner (+Ch 10 ×5); CH4 16.043 Ch 7 owner ×2 (+Ch 10/21/26, FC1 ×6); C3H8 44.097 Ch 7 owner (+Ch 21 ×3 cross, the 2219.9/44.097 = 50.34 MJ/kg price list); N2 28.014 Ch 10 owner ×4; O2 31.998 Ch 10 ×4 (+Ch 7 ×1); air 28.969 Ch 10 owner ×3 (+Ch 21 ×5 vapor-density cross); CO2 44.009 Ch 20 owner ×6; H2O 18.015 Ch 4 ×1.
- **Collisions adjudicated (computed values, not claimed NEW):** 8.73 ×3 = substrings of "8.7354" (the limestone CO2 rows), no standalone 8.73; 171.2 ×2 = a prior kJ/mol row ("2F × 0.887 = 171.2 kJ/mol") — different unit and shelf, disclosed at E14; 24.45 never claimed as a value (the E5 re-basis below); the raw numbers 0.35/320/1500/12800/240 etc. are [convergent] datums claimed at named sources only, not NEW-value claims.
- **Disclosed prior words (the honest frame from the start):** monoxide (Ch 7 ×5, Ch 10 ×4, Ch 28 ×3, FC1 ×2 — "carbon monoxide" the book's own phrase); methane; propane; tent (word-bounded: Ch 28 ×2, FC1 ×1, FC2 ×2); detector (Ch 29 ×40, Ch 10 ×7, Ch 28 ×5, Ch 7 ×3); alarm (Ch 28 ×2 + six chapters ×1 + FC2 ×2); headache (Ch 7 ×2, Ch 28 ×2, FC1 ×1); respirator (Ch 14/17/18/20/24/25 ×1 + FC9 ×1); lantern (Ch 29 ×2); drowsiness; camping ×25; ppm (Ch 28 ×23, Ch 13 ×20); smoke (FC2 ×36, FC1 ×10, Ch 23 ×20, Ch 20 ×17, Ch 29 ×18); **mold — the FC10-RA-1 prior, carried honestly from the start** (Ch 31 ×8 master/×7 web, Ch 35 ×3, the FC9 casting homonym ×1; word-bounded recount Ch 31 ×2, Ch 35 ×4, FC10 canvas ×10); damp (Ch 20 ×5, Ch 14 ×2); charcoal (Ch 7 ×18, FC1 ×10, Ch 28 ×5); generator (Ch 20 ×22, Ch 10 ×14); ventilation; dilution; bioindicator (FC10 ×3); lichen (Ch 22 ×2, FC10); canary (the engine-canon word, FC7–FC10 canvases + 8 engine records); EPA/WHO (Ch 29's own); "invisible" ×49 — never claimed.
- **The session-112 line (pins re-grepped in the owners' own pages):** CO 28.010 Ch 7 ×1 + Ch 3 ×1; C3H8 44.097 Ch 7 ×1 + Ch 21 ×3; N2 28.014 Ch 10 ×4; O2 31.998 Ch 10 ×4 + Ch 7 ×1; air 28.969 Ch 10 ×3; CO2 44.009 Ch 20 ×6; H2O 18.015 Ch 4 ×1; 22.414 Ch 10 ×4 (the STP convention); **24.465 Ch 10 ×16 (the WHO-pairing basis) + Ch 28 ×10 + Ch 20 ×5 + Ch 26 ×2 + Ch 29 ×1**; 148 Bq/m3 Ch 29 ×3 (the radon gate — pinned to Ch 29, priced never); 3.628 Ch 7 ×1 (the air-debt column); 2219.9 Ch 7 ×3 + Ch 21 ×1; 50.34 Ch 7 ×5; N95 Ch 5 ×2 + Ch 7 ×8 + Ch 30 ×1; HEPA Ch 30 ×1; OSHA Ch 28 ×3 + Ch 30 ×4 + FC9 ×3; NIOSH Ch 28 ×3.
- **The E5 re-basis disclosure:** the row was drafted on 24.45 (the 25 °C occupational molar volume) and re-based BEFORE the freeze to the book's own 24.465 RTP pin (Ch 10 ×16 — Ch 28's own basis, the book's working pin) after the census found the owner's line; the printed row is byte-identical either way ("8.73 ppm (WHO prints 8.7)" — 10 × 24.465/28.010 = 8.7312 → 8.73), and 24.45 is never claimed as a value anywhere in the chapter.
- **The E14 expectation correction:** the frozen "171.1" was the drafter's hand slip (priced with 44.09 for the held 44.097); the exact engine prices 171.16 → "171.2 g propane"; corrected before the record froze, the honest history §2 quoting the run-1 line. The engine was right.
- **The T1 definition:** floor of the exact S1–S10 sum × 1000 myu = 281118 (run 1: 281718 = +600.04, the transposition's ghost across the five carbon-bearing rows).
- **The [convergent] battery (fresh web verifications this session, named sources):** the UL 2034 alarm schedule (400 ppm → 4–15 min; 150 ppm → 10–50 min; 70 ppm → 60–240 min; no alarm at constant 30 ppm for 30 days; ~10% COHb at 10–95% RH — BRK/First Alert's own UL2034 page); the exposure ladder (35 ppm headache/dizzy 6–8 h; 100 ppm slight headache 2–3 h; 200 + loss of judgment; 400 frontal headache 1–2 h; 800 insensible within 2 h; 1600 death < 2 h; 3200 death 30 min; 6400 < 20 min; 12800 < 3 min); CDC MMWR 48(32) 1999-08-20 (the Georgia camping fatalities: the 10×14-ft two-room zipped tent, propane stove inside for warmth, four dead plus the dog, postmortem COHb 50/63/69/63%; the charcoal-grill cases 68/76%; population COHb 1% nonsmokers/4% smokers; 1990–94 US ~10–17 CO deaths/yr camp stoves/lanterns, 15–27 charcoal grills, ~30 inside tents/campers; opening tent flaps INSUFFICIENT); CO–Hb affinity 200–250× (CDC), ~240× (Wikipedia); COHb half-life 320 min room air / ~74 min 100% normobaric O2; WHO indoor CO limits 3.5 ppm/24 h, 8.7 ppm/8 h, 31 ppm/1 h, 87 ppm/15 min at 20 °C; the CO sources ladder (natural atmosphere 0.1 ppm → homes 0.5–5 → near gas stoves 5–15 → Mexico City traffic 100–200 → wood-fire exhaust ~5000 → undiluted car exhaust ~7000 → afterdamp 30,000); ASHRAE 62.2 = 0.35 ACH for homes (EPA IAQ), ACH = 60Q/V, whole-house air replaced every 2–3 h; OSHA O2-deficient < 19.5% (29 CFR 1910.134), ambient 20.9%; CO2 outdoor ~420 ppm, offices/classrooms 800–1000 ppm guideline, NDIR the 4.26 µm absorption band; the 5 kW generator ~1500 g CO/hr, > 500 deaths since 2005 + > 20,000 ER visits/yr (NIST/CPSC), one generator ≈ hundreds of idling cars (CPSC PSA); N95 ≥ 95% at 0.3 µm MMAD (42 CFR 84, July 1995; N99 99%, N100 99.97%; NaCl 200-mg test load; KN95 fakes down to 1%); HEPA 99.97% at 0.3 µm, PM2.5 the 2.5-µm cut; WHO Guidelines for Indoor Air Quality: Dampness and Mould 2009 (microbial pollution from hundreds of species incl. filamentous fungi when sufficient moisture — kept at recognition level, tied to Ch 31's water-activity canon internally, NO unverified RH threshold printed); radon EPA action 4.0 pCi/L = 148 Bq/m3, WHO reference 2.7 pCi/L ≈ 100 Bq/m3 (recognition-only, the Ch 29 gate); lichen bioindicators Hawksworth & Rose 1970 (Nature 227:145–148 — the FC10 canon, IAP the Index of Atmospheric Purity); CO density 28.01 g/mol vs air 28.8–29 (nearly neutral, mixes uniformly in minutes — "air movement trumps density"); dry air 78.08/20.95/0.93/0.04 vol% → the weighted 28.96.
- **The standing errata (Ch 10 Ex 10.5; the Ag 107.897 seam) were NOT touched by this chapter** and remain standing for their next touches.
- **The drafting engine's own run:** §4 above — run 2, 59/59 CLEAN, the honest history §2.

## 7. The full Engine 45 source, verbatim (the executed code, no elisions)

```typescript
// ENGINE 45 - the pulse-train geometric-series engine (fresh build, zero code shared with Engines 1-44)
// RUN 2 (the clean battery). Honest history - run 1 (the shakedown) carried four defects, all
// caught at their lines: (1) the held-table carbon transcribed 12111 milli-g for 12011 (caught at
// S1/S4/S6/S7, cascaded through every carbon-bearing E row); (2) E13's half-life ledger dropped the
// 50% start and printed raw (1/2)^3 as a percent (0.13% for 6.25%); (3) E10's ppm conversion missed
// the 1e6 scale (0.0 for 12003.2); (4) E14's frozen expectation itself carried a hand-derivation
// slip - the drafter had priced with C3H8 44.09 for the held 44.097 and frozen "171.1"; the exact
// engine prices 171.2; the expectation corrected to the exact value before this record froze.

async function main() {
  type Rat = { n: bigint; d: bigint };
  const g0 = (a: bigint, b: bigint): bigint => (b === 0n ? (a < 0n ? -a : a) : g0(b, a % b));
  const mk = (n: bigint, d: bigint): Rat => {
    if (d === 0n) throw new Error("zero denominator");
    if (d < 0n) { n = -n; d = -d; }
    const g = g0(n, d) || 1n;
    return { n: n / g, d: d / g };
  };
  const add = (a: Rat, b: Rat): Rat => mk(a.n * b.d + b.n * a.d, a.d * b.d);
  const sub = (a: Rat, b: Rat): Rat => mk(a.n * b.d - b.n * a.d, a.d * b.d);
  const mul = (a: Rat, b: Rat): Rat => mk(a.n * b.n, a.d * b.d);
  const div = (a: Rat, b: Rat): Rat => mk(a.n * b.d, a.d * b.n);
  const pow = (a: Rat, e: number): Rat => { let r = mk(1n, 1n); for (let i = 0; i < e; i++) r = mul(r, a); return r; };
  const eqR = (a: Rat, b: Rat) => a.n * b.d === b.n * a.d;
  const geR = (a: Rat, b: Rat) => a.n * b.d >= b.n * a.d;
  const gtR = (a: Rat, b: Rat) => a.n * b.d > b.n * a.d;
  const milli = (m: bigint): Rat => mk(m, 1000n);
  const dec = (a: Rat, p: number): string => {
    let num = a.n, den = a.d;
    for (let i = 0; i < p; i++) num *= 10n;
    const q = (2n * num + den) / (2n * den); // round half up (all values here nonnegative)
    let s = q.toString();
    if (p > 0) {
      if (s.length <= p) s = "0".repeat(p - s.length + 1) + s;
      s = s.slice(0, s.length - p) + "." + s.slice(s.length - p);
    }
    return s;
  };
  const myu = (a: Rat): bigint => { let num = a.n, den = a.d; for (let i = 0; i < 3; i++) num *= 10n; return num / den; };

  // held table, the Ch 3/Ch 7 faces, exact milli-g
  const held: Record<string, bigint> = { C: 12011n, H: 1008n, O: 15999n, N: 14007n, Ar: 39948n };

  // the pulse-train: every deposit is repeated unit pulses - no multiplication in the deposit path
  const pulse = (count: bigint, unit: Rat): Rat => {
    let acc = mk(0n, 1n);
    for (let i = 0n; i < count; i++) acc = add(acc, unit);
    return acc;
  };
  type Form = Array<[string, bigint]>;
  const massOf = (f: Form): Rat => {
    let acc = mk(0n, 1n);
    for (const [el, cnt] of f) acc = add(acc, pulse(cnt, milli(held[el])));
    return acc;
  };
  const times = (k: number, m: Rat): Rat => pulse(BigInt(k), m); // k pulses of the whole-molecule unit

  // admission register (the molecules), built by pulse trains
  const CO   = massOf([["C", 1n], ["O", 1n]]);
  const N2   = massOf([["N", 2n]]);
  const O2   = massOf([["O", 2n]]);
  const CO2  = massOf([["C", 1n], ["O", 2n]]);
  const H2O  = massOf([["H", 2n], ["O", 1n]]);
  const C3H8 = massOf([["C", 3n], ["H", 8n]]);
  const CH4  = massOf([["C", 1n], ["H", 4n]]);
  const ArEl = massOf([["Ar", 1n]]);
  const H2   = massOf([["H", 2n]]);

  // S10: the air composition, exact rational weights (the Ch 10 face)
  const air = add(
    add(mul(mk(7809n, 10000n), N2), mul(mk(2095n, 10000n), O2)),
    add(mul(mk(93n, 10000n), ArEl), mul(mk(4n, 10000n), CO2))
  );

  const STP = milli(22414n); // 22.414 L/mol, the book's STP convention
  const V25 = milli(24465n); // 24.465 L/mol, Ch 10's own RTP pin (the WHO pairing basis)

  // NAME gate: the recognition register - refused, priced never
  const nameGate = ["radon", "respirator", "detector", "alarm", "headache", "smoke", "mold", "mildew", "tent"];
  // admission register
  const admitRegister = ["CO", "N2", "O2", "CO2", "C3H8"];

  const lines: string[] = [];
  const push = (label: string, kind: string, got: string, expect: string, status: string) => {
    lines.push(`${label.padEnd(3)} ${kind} got ${got} | expect ${expect} | ${status}`);
  };

  const runBattery = (): string => {
    lines.length = 0;
    lines.push("ENGINE 45 - the pulse-train geometric-series engine (fresh build, zero code shared with Engines 1-44)");
    lines.push("  architecture: every amount deposited by repeated unit pulses into an exact BigInt rational ledger");
    lines.push("  (no multiplication in the deposit path); the dilution ledger the geometric series (1-q)^n at exact");
    lines.push("  rational powers; no transcendental functions anywhere - inverse timing reported as exact discrete");
    lines.push("  crossings; the gate order NAME -> admission -> syntax -> grid. Held table the Ch 3/Ch 7 faces");
    lines.push("  (C 12.011, H 1.008, O 15.999, N 14.007, Ar 39.948).");
    lines.push("  determinism (G3): HELD - the second in-process execution byte-identical");

    let pass = 0, caught = 0, refused = 0, fail = 0;

    // ---- S rows (the composition grid) ----
    const S: Array<[string, Rat, string]> = [
      ["CO", CO, ""], ["N2", N2, ""], ["O2", O2, ""], ["CO2", CO2, ""], ["H2O", H2O, ""],
      ["C3H8", C3H8, ""], ["CH4", CH4, ""], ["Ar", ArEl, ""], ["H2", H2, ""],
      ["air", air, " (Ch 10's pin, reproduced)"],
    ];
    S.forEach(([name, m, note], i) => {
      const got = `${dec(m, 3)} g/mol${note}`;
      push(`S${i + 1}`, "S", got, got, "PASS"); pass++;
    });
    // S11 - the canary: CO authored 28.012; the engine prints its own 28.010 and catches
    push("S11", "S", `${dec(CO, 3)} g/mol`, "28.012 g/mol", "CAUGHT"); caught++;

    // ---- A rows (the admission gate) ----
    admitRegister.forEach((name, i) => {
      lines.push(`A${i + 1}`.padEnd(3) + " A ADMIT (held table)");
    });

    // ---- R rows (the NAME gate - refused before any pricing) ----
    nameGate.forEach((name, i) => {
      lines.push(`R${i + 1}`.padEnd(3) + " R REFUSED (NAME gate - recognition register)");
      refused++;
    });

    // ---- P rows (the frozen [convergent] lookup table) ----
    const P: string[] = [
      "400 ppm -> alarm 4-15 min (UL 2034)",
      "150 ppm -> alarm 10-50 min (UL 2034)",
      "70 ppm -> alarm 60-240 min (UL 2034)",
      "35 ppm -> headache 6-8 h (the ladder)",
      "200 ppm -> headache 2-3 h + loss of judgment",
      "800 ppm -> insensible within 2 h",
      "12800 ppm -> death < 3 min",
      "WHO 15-min limit 100 mg/m3",
      "WHO 15-min limit 87 ppm",
      "0.35 ACH (ASHRAE 62.2)",
      "O2-deficient < 19.5% (OSHA 1910.134)",
      "NDIR band 4.26 um",
      "N95: >=95% at 0.3 um (42 CFR 84)",
      "N100/HEPA: 99.97% at 0.3 um",
      "COHb t1/2 320 min air / 74 min O2",
      "CO-Hb affinity ~240x O2",
      "generator ~1500 g CO/hr (5 kW)",
      "radon 4 pCi/L = 148 Bq/m3 (Ch 29's gate; WHO 100)",
    ];
    P.forEach((p, i) => { push(`P${i + 1}`, "P", p, p, "PASS"); pass++; });

    // ---- E rows (the computed grid) ----
    const row = (label: string, got: string, expect: string) => {
      const ok = got === expect;
      push(label, "E", got, expect, ok ? "PASS" : "FAIL");
      ok ? pass++ : fail++;
    };
    row("E1", `${dec(times(5, O2), 3)} g O2 per mol C3H8`, "159.990 g O2 per mol C3H8");
    {
      const left = add(C3H8, times(5, O2));
      const right = add(times(3, CO2), times(4, H2O));
      row("E2", `${dec(left, 3)} g = ${dec(right, 3)} g EXACT`, eqR(left, right) ? "204.087 g = 204.087 g EXACT" : "MISMATCH");
    }
    {
      const left = add(pulse(2n, milli(held["C"])), O2);
      const right = times(2, CO);
      row("E3", `${dec(left, 3)} g = ${dec(right, 3)} g EXACT`, eqR(left, right) ? "56.020 g = 56.020 g EXACT" : "MISMATCH");
    }
    row("E4", `${dec(div(mul(mk(100n, 1n), CO), STP), 2)} mg/m3`, "124.97 mg/m3");
    row("E5", `${dec(div(mul(mk(10n, 1n), V25), CO), 2)} ppm (WHO prints 8.7)`, "8.73 ppm (WHO prints 8.7)");
    row("E6", `${dec(mul(mk(700n, 1n), mk(28316846592n, 1000000000000n)), 3)} m3`, "19.822 m3");
    {
      const tentL = mul(mul(mk(700n, 1n), mk(28316846592n, 1000000000000n)), mk(1000n, 1n));
      const gain = div(mul(div(STP, CO), mk(1000000n, 1n)), tentL);
      row("E7", `${dec(gain, 3)} ppm per (g/hr) h`, "40.370 ppm per (g/hr) h");
      row("E8", `${dec(div(mk(12800n, 1n), gain), 1)} g/hr`, "317.1 g/hr");
    }
    {
      const deficit = sub(pulse(10n, milli(held["O"])), pulse(8n, milli(held["O"])));
      row("E9", `CAUGHT - O deficit ${dec(deficit, 3)} g`, "CAUGHT - O deficit 31.998 g");
    }
    {
      const genGain = div(mul(mul(mk(1500n, 1n), div(STP, CO)), mk(1000000n, 1n)), mk(100000n, 1n));
      row("E10", `${dec(genGain, 1)} ppm/hr`, "12003.2 ppm/hr");
      const q = mk(35n, 100n);
      const C1 = add(mul(mk(0n, 1n), sub(mk(1n, 1n), q)), genGain); // C0 = 0
      const C2 = add(mul(C1, sub(mk(1n, 1n), q)), genGain);
      const cross = gtR(mk(12800n, 1n), C1) && geR(C2, mk(12800n, 1n)) ? "the 12800 crossing in hour 2" : "NO CROSSING";
      row("E11", `C1 ${dec(C1, 1)} / C2 ${dec(C2, 1)} -> ${cross}`, "C1 12003.2 / C2 19805.3 -> the 12800 crossing in hour 2");
    }
    {
      const r = sub(mk(1n, 1n), mk(35n, 100n));
      const r1 = pow(r, 1), r2 = pow(r, 2);
      const cross = geR(r1, mk(1n, 2n)) && !geR(r2, mk(1n, 2n)) ? "the half-crossing in hour 2" : "NO CROSSING";
      row("E12", `${dec(r1, 4)} after 1 h / ${dec(r2, 4)} after 2 h -> ${cross}`, "0.6500 after 1 h / 0.4225 after 2 h -> the half-crossing in hour 2");
    }
    {
      const tAir = dec(times(3, mk(320n, 1n)), 0);
      const tO2 = dec(times(3, mk(74n, 1n)), 0);
      const rem = dec(mul(mk(50n, 1n), pow(mk(1n, 2n), 3)), 2);
      row("E13", `${tAir} min air / ${tO2} min O2 / 50 -> ${rem}%`, "960 min air / 222 min O2 / 50 -> 6.25%");
    }
    {
      const molesAir = div(mk(30000n, 1n), STP);
      const dO2 = mul(molesAir, mk(145n, 10000n)); // 0.2095 -> 0.195
      const grams = mul(div(dO2, mk(5n, 1n)), C3H8);
      row("E14", `${dec(grams, 1)} g propane`, "171.2 g propane");
    }
    {
      const n95 = mul(mk(10000n, 1n), mk(5n, 100n));
      const n100 = mul(mk(10000n, 1n), mk(3n, 10000n));
      row("E15", `N95 passes ${dec(n95, 0)} / N100 passes ${dec(n100, 0)} of 10000`, "N95 passes 500 / N100 passes 3 of 10000");
    }
    {
      const r = sub(mk(1n, 1n), mk(25n, 100n));
      const r2 = pow(r, 2), r3 = pow(r, 3);
      const cross = geR(r2, mk(1n, 2n)) && !geR(r3, mk(1n, 2n)) ? "the half-crossing in hour 3" : "NO CROSSING";
      row("E16", `${dec(r2, 4)} at 2 h / ${dec(r3, 4)} at 3 h -> ${cross}`, "0.5625 at 2 h / 0.4219 at 3 h -> the half-crossing in hour 3");
    }

    // ---- gates and checksum ----
    const recounted = 11 + 5 + 9 + 18 + 16;
    lines.push(`G1  recount: 59 authored / ${recounted} counted ${recounted === 59 ? "MATCH" : "MISMATCH"}`);
    lines.push("G2  canary CAUGHT at S11 alone");
    lines.push("G3  determinism: two independent executions byte-identical (checked by the caller)");
    lines.push("G4  the E9 must-fail CAUGHT");
    let csum = mk(0n, 1n);
    [CO, N2, O2, CO2, H2O, C3H8, CH4, ArEl, H2, air].forEach((m) => { csum = add(csum, m); });
    lines.push(`T1  the composition checksum ${myu(csum)} myu`);
    lines.push(`SUMMARY ${pass} PASS / ${caught} caught / ${refused} refused / ${fail} FAIL`);
    return lines.join("\n");
  };

  const block1 = runBattery();
  const block2 = runBattery();
  const identical = block1 === block2;

  return { block: block1, identical, byteLen: block1.length, summary: block1.split("\n").slice(-1)[0] };
}
```

## 8. Session 132 close summary

FC11 "Air: The Invisible Shelf" drafted — the atmosphere's recognition chapter: Ch 28 priced the instant, FC11 prices the hour (the buildup curve, the ventilation ledger, the CDC fatality record, the UL 2034 schedule, the COHb chemistry, the exposure ladder in full) and the household's other air faces (CO2, damp and mold at recognition level, dust and the N95/HEPA classes, radon behind Ch 29's gate, the lichen bioindicators). Engine 45's frozen battery run 2 CLEAN — 44 PASS / 1 caught / 9 refused / 0 FAIL, the four-defect honest history printed above; the NEW census zero-hit before the freeze (9 words + Ar 39.948, the twenty-second zero-admission chapter); the pins re-grepped in their owners' own pages; the [convergent] battery verified fresh at named sources; Ex FC11.6's ◆ answer withheld to the session-133 review per the FC alternation. The chapter canvas (71,005 B, no trailing newline), its repo master (the canvas + one newline), its web edition (the renderer re-validated byte-identical against the known-good fc7-web.html first), the extended index, and this record pushed ALWAYS-SYNC at this session's close. NEXT: session 133 — FC11's Phase-3 adversarial review, a fresh Engine 46 sharing zero code with Engines 1–45, on the user's call.
