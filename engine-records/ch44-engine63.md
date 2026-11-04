# Engine 63 record — the binary-limb mini-float engine (session 169, the Ch 44 Deuterium authoring)

## 1. Design spec

Engine 63, the binary-limb mini-float engine — fresh at session 169, sharing zero code with Engines 1–62. Every quantity a value m·2^e with the mantissa a 40-bit integer normalized to [2^40, 2^41) — one limb, held in a float64 lane (safe: 2^41 < 2^53, the limb an exact integer there). Multiplication splits each limb into 20-bit half-words and recombines the four exact partial products, renormalizing with round-half-up. Division a restoring 41-step binary long division with carry pre-reduction and round-to-nearest on the final bit. Addition aligns exponents by shifting the smaller operand with round-half-up. The engine series' first transcendental lane, built because the Rayleigh rows demand one: the logarithm an atanh series on the transformed z = (mm−1)/(mm+1) with ln2 bootstrapped from atanh(1/3), a range-reduced 22-term exponential, pow = exp(p·ln x). No BigInt, no recursion, no Math.random; the float64 lane carries witnesses only, never values.

Distinctness from Engines 1–62: the whole prior series is schoolbook string-integer digit arithmetic — Engines 1–62 span base-10 digit strings, exact rationals, and fixed-point scaling families (Engine 62, the immediate predecessor: exact rationals as digit-strings {n,d}, schoolbook sAdd/sSub/sMul, digit-by-digit sDivRem, round-half-up via next digit). Engine 63 is the series' first binary-limb engine and its first with a transcendental lane: the Rayleigh law's fractional exponents (S^k at k = −ln(1−f)/ln(...)-class rows) price a logarithm no digit-string engine in the series ever carried.

## 2. Honest run history

The kernel probe ran before any sheet row, and it caught four kernel defects before a single sheet row ran:

- (K1) the multiply dropped the half-word quotient scale — every product short by 2^40;
- (K2) the division lacked the A≥B carry pre-reduction (found by inspection at rev-1);
- (K3) an inverted add alignment shifted the LARGER operand right and zeroed it at exponent gaps > 41, collapsing every series to its tail (the ln2 = 0.00000000000 symptom);
- (K4) the logarithm fed the atanh series the mantissa ratio mm instead of the transform z = (mm−1)/(mm+1) — atanh(1.25) a divergent series, masked by a boot whose own z, one third, was accidentally correct, until the ln(10) probe row caught it.

All four fixed at kernel rev-3. Three harness defects after that, each caught by the sheets' own balance classes:

- (H1) Sheet 1 rev-1's witness tolerance compared at more digits than the printed precision — a spurious FAIL with all thirteen engine values numerically correct; the harness now compares at printed precision (Sheet 1 rev-2: 13/13);
- (H2) Sheet 2 rev-1's toDec printed a trailing decimal point at zero decimals — three string-format FAILs with identical values (Sheet 2 rev-2: 19/19);
- (H3) Sheet 3's S_eff inversion carried a sign slip the direct witness shared (it ran the same wrong algebra and could not see it); the E-recompute round-trip rows S1b/S2b caught it — the round-trip balance class earned (Sheet 3 rev-2: PASS).

The drafter's plan-value hand slips the machine corrected, printed in the transcripts and never laundered: 142.040 → 142.036 (Na₂SO₄); 0.55893 → 0.55915 (the Glauber water fraction); 59,505 → 59,509 A·h; 13,845 → 13,862.9 (the finale enrichment); 6,420.0 → 6,420.1 (1/R₀ at one decimal; the integer 6,420 the register's own arithmetic).

## 3. The gates

- Kernel probe (Piece A rev-3): P1 D₂O 20.027, P2 ln2 0.69314718, P3 e 2.71828183, P4 10^0.9 7.94328235 (the Rayleigh S=10, f=0.1 enrichment row) — all PASS beside float64 witnesses; P5 injection (ρ(D₂O)/ρ(H₂O) = 1.1076 vs injected 1.2133, the adjacent-infobox-cell transcription slip) CAUGHT. Probe verdict PASS.
- Sheet 1 (Lab 44.1's molar book) rev-2: 13/13.
- Sheet 2 (the electrolyte switch ledger) rev-2: 19/19.
- Sheet 3 (the Rayleigh ledger) rev-2: B1–B8 balances, E1–E5 two-method closed-vs-8-stage agreement, S_eff 2.63/3.62 with round-trips 713.3/2,140.0 — PASS.
- Sheet 4 (injections and corrupted literal claims): 19/19 CAUGHT, including the two literal transcription guards 3.82 → 3.28 and 101.4 → 110.4.
- Sheet 5 (determinism): two fresh kernel instances built independently, byte-identical; all 30 canonical values present in the transcripts on disk.
- Sheet 6 (the test ledger): 8/8 — ST1 83.1%, ST2 81.3%, ST3 1.88%, ST4 8.16%, MT1 0.382, MT2 0.955, MT3 1.91, T1 435 days.

## 4. The frozen runblock (Engine 63's own output, spliced verbatim — never retyped)

```text
ENGINE 63 - PIECE A REV-3: KERNEL PROBE (binary-limb mini-float: value = m*2^e, m normalized to [2^40,2^41); 20-bit half-word partial-product mul; restoring 41-step binary division with carry; atanh-series ln with the (mm-1)/(mm+1) transform, ln2 bootstrapped from atanh(1/3); range-reduced exp; pow = exp(p ln x); no BigInt, no recursion, no Math.random; float64 witness lane beside every row)
run: probe rev-3 2026-11-04
rev-1/rev-2 honest run history: 4 kernel defects caught BEFORE any sheet row ran - (K1) mul dropped the half-word quotient scale (returned exponent x[1]+y[1], short by 2^40; every product wrong); (K2) div lacked the A>=B carry pre-reduction (found by inspection at rev-1); (K3) add_ alignment INVERTED - the larger operand was shifted right and zeroed at exponent gaps >41, collapsing every series to its tail (the LN2=0.00000000000 symptom); (K4) loge passed the mantissa ratio mm to the atanh series instead of the transformed z=(mm-1)/(mm+1) - atanh(1.25) is a divergent series, and the boot's ln2 was accidentally correct (its z IS 1/3), masking the defect until the ln(10) probe row. All fixed at rev-3.
P1 D2O = 2*2.014+15.999 = 20.027 (expected 20.027) | float witness 20.0270000
P2 ln2 = 0.69314718 | float witness 0.693147181
P3 e = exp(1) = 2.71828183 | float witness 2.71828183
P4 10^0.9 = 7.94328235 (the Rayleigh S=10, f=0.1 enrichment row) | float witness 7.94328235
P1-P4 verdicts: PASS PASS PASS PASS
P5 injection: rho(D2O)/rho(H2O) = 1.1076 vs injected 1.2133 (the adjacent-infobox-cell transcription slip) - CAUGHT (digit slip)
PROBE VERDICT: PASS (kernel rows clean on the mini-float lane; injection caught)
```

```text
ENGINE 63 - SHEET 1 REV-2: MOLAR BOOK C-ROWS (book-basis atomic masses; kernel rev-3, probe PASS; harness rev-2: the rev-1 witness tolerance ignored printed precision - C9 printed 0.00015576 at 8dp was scored against the full-precision float witness and FAILed spuriously; the harness now scores the engine string against the witness ROUNDED TO THE PRINTED PRECISION. A harness defect, not an engine defect; all 13 engine values in rev-1 were numerically correct.)
run: sheet 1 rev-2 2026-11-04
C1 D2O = 2*2.014+15.999 = 20.027 | float witness rounded to 3dp = 20.027 | PASS
C2 H2O = 2*1.008+15.999 (PIN 18.015) = 18.015 | float witness rounded to 3dp = 18.015 | PASS
C3 D/H mass ratio (the isotope admission) = 1.9980 | float witness rounded to 4dp = 1.9980 | PASS
C4 Na2SO4 = 2*22.98977+32.06+4*15.999 = 142.036 | float witness rounded to 3dp = 142.036 | PASS
   note: drafter plan value 142.040 was a hand slip; machine value 142.036 stands (recorded honestly).
C5 Na2SO4*10H2O (Glauber's salt) = 322.186 | float witness rounded to 3dp = 322.186 | PASS
C5b hydrate water fraction = 180.15/322.186 = 0.55915 | float witness rounded to 5dp = 0.55915 | PASS
   note: drafter plan value 0.55893 was a hand slip; machine value 0.55915 stands (recorded honestly).
C6 Na2CO3*10H2O = 105.988+10*18.015 = 286.138 | float witness rounded to 3dp = 286.138 | PASS
C7 Na2CO3 re-proof (PIN 105.99 Ch 14) = 105.988 | float witness rounded to 3dp = 105.988 | PASS
C8 rho(D2O)/rho(H2O) = 1.1056/0.9982 = 1.1076 | float witness rounded to 4dp = 1.1076 | PASS
C8b excess density percent = 10.76 | float witness rounded to 2dp = 10.76 | PASS
C9 1/6420 (book rounding of 155.76 ppm) = 0.00015576 | float witness rounded to 8dp = 0.00015576 | PASS
C9b 1/0.00015576 = 6420.1 | float witness rounded to 1dp = 6420.1 | PASS
C10 Ex 44.1: 6400 mL * 0.00015576 = 0.99686 | float witness rounded to 5dp = 0.99686 | PASS
SHEET 1 VERDICT: PASS (13/13 rows)
```

```text
ENGINE 63 - SHEET 2 REV-2: CAMPAIGN LEDGER D-ROWS (Rayleigh enrichment E = f^(1/S - 1) on exact rational exponents; kernel rev-3; harness rev-3 - the three rev-1 FAILs (D04a/D10b/D10c) were string-format artifacts: toDec printed a trailing decimal point at 0 decimals ('4691.') against the witness '4691'; values identical on both lanes. Fixed at rev-2.)
run: sheet 2 rev-2 2026-11-04
D01 1/R0 (D/H ratio of natural water) = 6420.1 | float witness rounded to 1dp = 6420.1 | PASS
   D01 integer form: 6420 (the register's 1-in-6420 arithmetic)
D03a Part-1 11x: E = (1/11)^(-0.9) = 11^0.9 = 8.65 | float witness rounded to 2dp = 8.65 | PASS
D03b Part-1 D/H after 11x: R = 155.76e-6 * E = 0.0013481 | float witness rounded to 7dp = 0.0013481 | PASS
D04a goal 12000x: E = 12000^0.9 = 4691 | float witness rounded to 0dp = 4691 | PASS
D04b goal D fraction = r/(1+r) = 0.4222 | float witness rounded to 4dp = 0.4222 | PASS
D05a Part-4 (110/3)^0.9 (S=10) = 25.58 | float witness rounded to 2dp = 25.58 | PASS
D05b Part-4 D percent (S=10) = 0.397 | float witness rounded to 3dp = 0.397 | PASS
D05c Part-4 (110/3)^(5/6) (S=6) = 20.12 | float witness rounded to 2dp = 20.12 | PASS
D05d Part-4 D percent (S=6) = 0.312 | float witness rounded to 3dp = 0.312 | PASS
D07a finale 40000^0.9 (S=10) = 13862.9 | float witness rounded to 1dp = 13862.9 | PASS
D07b finale D percent (S=10) = 68.35 | float witness rounded to 2dp = 68.35 | PASS
D07c finale 40000^(5/6) (S=6) = 6839.9 | float witness rounded to 1dp = 6839.9 | PASS
D07d finale D percent (S=6) = 51.58 | float witness rounded to 2dp = 51.58 | PASS
   note: drafter plan value E(S=10) = 13,845 was a hand slip; machine value 13862.9 stands (recorded honestly).
D08 hydrate trap: 175 mL * Part-1 R = 0.23591 | float witness rounded to 5dp = 0.23591 | PASS
   D08 rounds to 0.24 mL - the register's 'quarter of a milliliter' [computed consistency]
D10a moles in 20,000 g H2O (18.015 basis) = 1110.2 | float witness rounded to 1dp = 1110.2 | PASS
D10b charge = mol * 192,970 C (2F, PIN Ch 19) = 214232584 | float witness rounded to 0dp = 214232584 | PASS
D10c ampere-hours = charge/3600 = 59509 | float witness rounded to 0dp = 59509 | PASS
   note: drafter plan value 59,505 A*h was a hand slip; machine value 59509 stands (recorded honestly).
D10d energy at 5 V = charge*5/3.6e6 (kWh) = 297.5 | float witness rounded to 1dp = 297.5 | PASS
D10e days at 7 A = A*h/168 = 354.2 | float witness rounded to 1dp = 354.2 | PASS
SHEET 2 VERDICT: PASS (19/19 rows)
```

```text
ENGINE 63 - SHEET 3 REV-2: BALANCES + TWO-METHOD E-ROWS + S_EFF INVERSION (kernel rev-3, harness rev-3)
run: sheet 3 rev-2 2026-11-04
rev-1 honest history: the S_eff inversion was written over ln(1/f) with a subtraction - a sign slip that the direct witness row could not see because the witness formula shared the same algebra (engine and witness agreed on the WRONG value 0.62); the E-recompute round-trip rows caught it (S1b/S2b FAILed). Corrected: 1/S = 1 - ln(E)/ln(40000). The round-trip balance earned its keep.
B1 2 x 96,485 (faraday pair, PIN Ch 12/19) = 192970 | witness = 192970 | PASS
B2 charge/192,970 round-trip to mol = 1110.2 | witness = 1110.2 | PASS
B3 A*h x 3600 round-trip to charge = 214232584 | witness = 214232584 | PASS
B4 days x 168 round-trip to A*h = 59509 | witness = 59509 | PASS
B5 kWh x 3.6e6 / 5 round-trip to charge = 214232584 | witness = 214232584 | PASS
B6 322.186 - 180.15 round-trip to Na2SO4 = 142.036 | witness = 142.036 | PASS
B7 hydrate-trap volume / 175 round-trip to Part-1 R = 0.0013481 | witness = 0.0013481 | PASS
B8 6420 x (1/6420) round-trip to 1 = 1 | witness = 1 | PASS
E1 Part-1 11^0.9: closed = 8.6547 | 8-stage staged = 8.6547 | witness = 8.6547 | PASS
E2 goal 12000^0.9: closed = 4690.975 | 8-stage staged = 4690.975 | witness = 4690.975 | PASS
E3 Part-4 (110/3)^0.9: closed = 25.577 | 8-stage staged = 25.577 | witness = 25.577 | PASS
E4 finale 40000^0.9: closed = 13862.897 | 8-stage staged = 13862.897 | witness = 13862.897 | PASS
E5 finale 40000^(5/6): closed = 6839.904 | 8-stage staged = 6839.904 | witness = 6839.904 | PASS
S1 S_eff implied by register endpoint ~10% D = 2.63 | witness = 2.63 | PASS
S2 S_eff implied by register endpoint ~25% D = 3.62 | witness = 3.62 | PASS
S1b E recomputed from S1 = r/R0 at 10% endpoint = 713.3 | witness = 713.3 | PASS
S2b E recomputed from S2 = r/R0 at 25% endpoint = 2140.0 | witness = 2140.0 | PASS
SHEET 3 VERDICT: PASS (17/17 rows)
```

```text
ENGINE 63 - SHEET 4: INJECTION BATTERY (kernel rev-3, harness rev-3; each row injects an engineered digit slip into a computed value - or a corrupted literal against its sourced pin - and the harness must CATCH the mismatch)
run: sheet 4 2026-11-04
I1 density ratio (adjacent-infobox-cell class): true = 1.1076 | injected = 1.1560 | CAUGHT
I2 1/R0 (transposition class): true = 6420 | injected = 6240 | CAUGHT
I3 D2O molar mass (dropped-digit class): true = 20.027 | injected = 20.72 | CAUGHT
I4 Na2SO4 molar mass (plan-slip echo): true = 142.036 | injected = 142.360 | CAUGHT
I5 hydrate water fraction (transposition class): true = 0.55915 | injected = 0.55951 | CAUGHT
I6 Part-1 enrichment 11^0.9 (transposition class): true = 8.65 | injected = 8.56 | CAUGHT
I7 goal enrichment 12000^0.9 (transposition class): true = 4691 | injected = 4961 | CAUGHT
I8 finale enrichment 40000^0.9 (digit-swap class): true = 13862.9 | injected = 13682.9 | CAUGHT
I9 2F faraday pair (transposition class): true = 192970 | injected = 192790 | CAUGHT
I10 charge (last-pair swap class): true = 214232584 | injected = 214232548 | CAUGHT
I11 ampere-hours (transposition class): true = 59509 | injected = 59059 | CAUGHT
I12 kWh at 5 V (digit-swap class): true = 297.5 | injected = 279.5 | CAUGHT
I13 days at 7 A (digit-swap class): true = 354.2 | injected = 345.2 | CAUGHT
I14 Ex 44.1 tap-water D2O (deletion class): true = 0.99686 | injected = 0.96986 | CAUGHT
I15 hydrate-trap volume (digit-swap class): true = 0.23591 | injected = 0.23519 | CAUGHT
I16 S_eff at 10% endpoint (digit-swap class): true = 2.63 | injected = 2.36 | CAUGHT
I17 S_eff at 25% endpoint (digit-swap class): true = 3.62 | injected = 3.26 | CAUGHT
T1 D2O melting point pin (transcription guard): true = 3.82 | injected = 3.28 | CAUGHT
T2 D2O boiling point pin (transcription guard): true = 101.4 | injected = 110.4 | CAUGHT
SHEET 4 VERDICT: PASS (19/19 injections CAUGHT)
```

```text
ENGINE 63 - SHEET 5: DETERMINISM (two fresh kernel instances built independently in one run; canonical row set of 30 values computed by each; byte-for-byte compare; cross-run check that every value string appears in the sheet 1/2/3 transcripts on disk)
run: sheet 5 2026-11-04
instance A vs instance B byte-identical: YES
cross-run transcript check: ALL 30 VALUES PRESENT in s1/s2/s3
SHEET 5 VERDICT: PASS
```

```text
ENGINE 63 - SHEET 6: THE SINK-THRESHOLD, MELTING-POINT INTERPOLATION, AND ARC-SPAN ROWS (Lecture 4's own ledger; basis named per row; kernel rev-3, harness rev-3)
run: sheet 6 2026-11-04
ST1 sink threshold, household basis (rho 1.000) = 83.1 | witness = 83.1 | PASS
ST2 sink threshold, STP pair (rho 0.9982) = 81.3 | witness = 81.3 | PASS
ST3 pure D2O ice sinking margin vs H2O (STP pair) = 1.88 | witness = 1.88 | PASS
ST4 H2O ice floating margin (STP pair) = 8.16 | witness = 8.16 | PASS
MT1 mp shift at the spoken ~10% estimate = 0.382 | witness = 0.382 | PASS
MT2 mp shift at the ~25% evaporation-corrected estimate = 0.955 | witness = 0.955 | PASS
MT3 mp shift at the purchased-control ~50% suspicion = 1.91 | witness = 1.91 | PASS
T1 published arc span, first to last video (days, exact integer) = 435 | witness = 435 | PASS
SHEET 6 VERDICT: PASS (8/8 rows)
```


## 5. Expectations provenance

The expected values beside every row come from the register arc N135–N142 (batch-31b/31c-class survey entries, the eight-video deuterium campaign CXsuYYPIMfc through rddSZzmA6AI), the campaign's own spoken and printed figures, and the session's web battery — all convergent: D/H 155.76 ppm VSMOW = 1-in-6,420; D₂O mp 3.82 °C, bp 101.4 °C, ρ 1.1056 g/mL, maximum density at 11.2 °C, M 20.0276 g/mol (NIST; the book basis 20.027 the seam recorded); D₂O ice ρ 1.017 vs H₂O ice 0.9167; the electrolytic separation-factor band (Vemork 5–7, mild steel 8–10, SPE 6.3, α rising with current density — the register's "10×" the published best case); Girdler's dual-temperature 30/130 °C towers (Spevack 1943); Urey 1931, Nobel 1934; toxicity >20% body fluids, 25–50% lethal, the sweet taste. Watch-note recorded: the Gasmet page's mp printed as a −3.8 °C sign variant and ρ 1.1059 — variants named, never laundered.

## 6. The session-169 checks (all PAID at this close)

- The freeze-gate census at authoring HEAD over Chapters 1–43 and the field companions: the chapter's new literals zero-hit (155.76, 20.027, 2.014, 101.4, 1.1056, 0.9982, 0.9167, 1.017, 322.186, 59,509, and the ledger's own rows); the digit coincidences named, never hidden (3.82 — Chapter 29's radon half-life seam, with its Ch 15 substring echo inside 13.826; 3.62 — Chapter 4's drop datum, the collision class Chapter 40's census already names; 354.2 — Chapter 9's soda-water grams; 2.63 — a substring of Chapter 26's 2.636 L of oxygen; and the pure substring classes 81.3, 435, 83.1, 1.91, 0.312 riding inside longer numbers); the pins re-proved at their owners (18.015, 96,485, 192970 — Chapter 19 line 326's own comma-free print — 105.99, 120.361, 98.072, plus the two the census itself caught as pins rather than new values: Na₂SO₄ 142.036, Chapter 5's compound-table pin, the Glauber family Chapters 13/14 carry and Chapter 37 wears six-strong; and the natron 286.138, Chapter 14's crystal-box decahydrate).
- The fifteen got-strings verified verbatim at the survey register (batch-31b/31c + SURVEY.md) and in the chapter, at their counted occurrences.
- [speculative] exactly once in the chapter (its single Sources declaration); 0.917 nowhere in the chapter (the FC6 avoidance held — 0.9167 the printed ice density).
- The web render oracle-first: ch43-web.html reproduced byte-identically (70,757 B, md5 e5dec37622d980905d1bd85639dce632) from ch43-manuscript.md before ch44-web.html was rendered (72,776 B, md5 14a9284e03b01d480c18abe1a2463214, the drafted tail; the 12-row Safety Table present in both master and render — the session-168 staleness lesson worn).

## 7. The source disclosure (the session-108 lesson worn again)

The full Engine 63 source is NOT printed here, and no reconstruction is printed as verbatim: the engine ran in the run_typescript sandbox at the pre-compaction half of session 169, and the source was not durably saved to disk before the session's context compaction — the same lesson the web renderer's own provenance note records from session 108 ("first built session 108 (not durably saved then — the recorded lesson)"). What survives, all durably hashed: the design spec (§1), the kernel and harness defect history (§2), the gates and their verdicts (§3), and the transcripts spliced verbatim in §4, hashed below. The manuscript's own engine description (Ch 44's Lab 44.1 head) completes the reproducible record. Standing instruction recorded for the next engine: Engine 64 (the Ch 44 review engine, session 170) must save its full source to the session buffer BEFORE the battery runs.

Transcript hashes (md5, verified at this close):

- lab63-s0-probe.txt 1,650 B a60db60428e0c6bd14b6baa2d86c8f85
- lab63-s1.txt 1,929 B 842721d4b8493c363b280292c7202022
- lab63-s2.txt 2,496 B a7689564419d1bc212bce52fb67d726e
- lab63-s3.txt 1,937 B ab8f19de6065ae0ed62bd1b82dc08bac
- lab63-s4.txt 1,923 B 79c40cb2c1a05b58233a7749d93be854
- lab63-s5.txt 406 B 706e34fd48d462ae5a470df0cea8fca2
- lab63-s6.txt 864 B 07fb993113e4b5e251ff54c2483768c7

## 8. Session 169 close summary

VERDICT: the Ch 44 authoring battery PASSES at final runs — probe rev-3 PASS (P1–P4 clean beside float64 witnesses, the P5 injection CAUGHT), Sheets 1–6 all PASS at their final revisions (13/13; 19/19; the Rayleigh PASS with H3's round-trip class earned; 19/19 injections CAUGHT; determinism byte-identical across two fresh instances; 8/8), the freeze-gate census PAID with its two pin findings (142.036, 286.138) attributed at their owners rather than laundered as new, the got-strings 15/15 verbatim at the register, and the web oracle byte-identical before the new render. The chapter's honest negatives — the campaign's own (the extraction that did not concentrate) and the engine's own (K1–K4, H1–H3, the plan slips) — are printed, never laundered. Engine 63 is retired at this close; the Ch 44 Phase-3 adversarial review (session 170) builds fresh Engine 64, zero code shared with Engines 1–63.
