# FC6 Engine 48 record — the CRT modular-residue review engine (session 135, the FC6 Phase-3 adversarial review)

Session 135 (2026-10-21): the FC6 review unit per row 135 — "Heavy Work Without Explosives," the Field Companion's sixth chapter, drafted session 134 and reviewed this session by a fresh engine sharing zero code with Engines 1–47. Engine 48 — the CRT modular-residue engine — re-executed the frozen 53-row battery with the expectations loaded at runtime from the Engine 47 record's §4 fence, the got-strings verbatim, never retyped. Verdict: **run 2 CLEAN — 53/53 adjudicated, 42 PASS / 2 caught / 9 refused / 0 FAIL, zero findings raised**, gates G1–G4 all held at the same run, the whole battery executed twice byte-identical, 52 of 53 rows reproduced byte-identical with the one difference the E4 witness lane's disclosed carrying clause (below). The honest history — a fence-extraction defect caught by the pre-run probe before the engine's first execution, a representation-level throw at run 1, and a close-time scratch loss that took the frozen source and runblock files between this record's part-writes (disclosed at §2, §4, and §7, never smoothed) — follows.

## 1. Design spec

- **THE RESIDUE ENGINE, the fresh axis:** every positive rational is carried at rest as a pair of residue vectors — (numerator residues, denominator residues) — over a fixed basis of four coprime primes (1000003, 1000033, 1000037, 1000039, each verified prime at startup by deterministic Miller-Rabin, a startup gate outside the arithmetic path), and **the arithmetic path has no integers at all**: +, −, × are componentwise modular operations on the residue pairs; division is the reciprocal swap (no modular inverse is ever computed); equality is the modular cross-product test. Integers are reconstructed exactly only at print and compare, via Garner's mixed-radix scheme with the magnitude bound asserted (< the basis product), and every reconstruction is re-encoded to residues with a round-trip assert before the value is used. Every printed decimal is an exact rational labeled at print — no float anywhere. **No parse tree is materialized at all** (molecules are element-count lists, not strings), no Stern-Brocot paths (47), no prime-exponent lattices (46), no pulse trains (45), no inherited-multiplier descent (44), no bytecode VM (43), no event sweep (42), no segment tree (41), no interval containment (40), no depth ledger (39), no dual-column peel (38), no CPS (37), no token-table AST fold (36), no span-memo (35), no census tally (34), no fixed-point rewriting (33), no RPN reorder (31), no expression compiler (19) — the neighbors named honestly; the CRT residue pair is Engine 48's own.
- **The review contract:** the frozen 53-row battery loaded at runtime from the Engine 47 record's §4 fence — never retyped; the fence's own identity asserted before a single row ran (lines 73 / bytes 6003 / bytesum 435804) and the repo's engine-records/fc6-engine47.md size verified at HEAD 5d18b4e7; any mismatch a finding raised for adjudication, never silently patched. The one carried face, declared before the run (the E44 witness-lane precedent, printed in the engine's own header): the E4 witness lane's carrying clause names this engine's CRT face where the frozen line names Engine 47's Stern-Brocot path — the value, the ratio and the repeating decimal identical.
- **The held table, unchanged from the drafting engine:** C 12.011, H 1.008, O 15.999, Ca 40.078, Si 28.085 — the five faces the lime cycle and the stone actually need; **iron deliberately not held** (R9's refusal — Ch 19's bloomery owns the face).
- **The gate order:** NAME first — the recognition register (dynamite, black powder, gunpowder, TNT, nitroglycerin, detonator, blasting cap, ANFO) refused *before any formula parses* (R1–R8); then the held-table gate (R9: Fe2O3 — Fe not held); then admission (A1–A5: the five register molecules rebuilt and checked against their own S rows); then syntax; then the grid.

## 2. Honest run history

Nothing smoothed; every defect named at its own line.

**The pre-run probe — a fence-extraction defect caught before the engine's first execution.** The §4-fence slicer read the record with an off-by-one: the fence's opening line (three backticks plus the word text) is eight bytes, and the draft sliced at nine, beheading the E of ENGINE (the probe read bytes 6002 / bytesum 435735 for the asserted 6003 / 435804). Fixed at its line before run 1 — a loading defect, named here because a review engine that loads the wrong fence verifies nothing.

**Run 1 — threw at E12's own line: NON-INTEGER AT INT PRINT.** E12's kinetic row prices ½ × 1000 × 25, and the value arrives carried as the residue pair 25000/2 — the CRT never reduces, reduction being impossible in residues — while intStr had equated "integer value" with "denominator residues = 1," a representation-level confusion the battery caught exactly where authored. Fixed at intStr's line: the divisibility test (num % den = 0), the value exact, the carrier untouched.

**Run 2 — the frozen battery, 53/53 CLEAN (42 PASS / 2 caught / 9 refused / 0 FAIL):** G1 recount MATCH 53/53; the canary re-caught at S9 alone (60.093 planted, 60.083 re-printed); G3 two in-process executions byte-identical; the E9 must-fail re-caught at exactly 18.015 g — the deficit proven equal to S5 itself; T1 recomputed 570,580 myu MATCH; SUMMARY and VERDICT byte-identical to the frozen block. **52 of 53 rows reproduced byte-identical; the one difference is the E4 witness lane's disclosed carrying clause** — Engine 48's CRT residue pair (Garner reconstruct 220 and 70 exact, gcd 10, re-encode round-trip PASS) where the frozen line names Engine 47's SB path RRRLLLLLL — value 22/7, ratio and repeating decimal (3.142857..., period 6) identical, the E44 witness-lane precedent declared before the run, printed in the engine's own header, and adjudicated here rather than smoothed.

**THE CLOSE-TIME LOSS, disclosed at its own line — the frozen files wiped between this record's part-writes.** A platform filesystem reset struck mid-close: the scratch layer (/home/user/.fc6-e48-source.ts — the frozen engine source; /home/user/.fc6-e48-runblock.txt — the frozen runblock; the session's fetched-masters census directory) was wiped between this record's first and later part-writes, while the reviewed canvas, the re-rendered web page, and the knowledge folder survived untouched. The loss was caught by the assembly's own byte-checks — the splices could not be made from files that no longer existed — and nothing was reconstructed silently: the §4 block below is a disclosed reconstruction (82 of its 85 lines byte-exact, the three reconstructed header lines named), and §7 records the source as lost, claiming nothing about the lines that died unread. The run's own verified identity is recorded here as history: **the frozen runblock file measured 85 lines / 7,232 bytes / bytesum 545,130 (the file 7,233 with its trailing newline), and the frozen source measured 601 lines / 33,471 bytes / bytesum 2,492,407 — both verified at the run and re-verified at this close before the wipe.** A future loader asserts the reconstruction's own stats, printed in §4.

## 3. The gates

- **G1 RECOUNT:** 53 rows authored, 53 counted — 9 S (8 + the canary) + 5 A + 9 R + 14 P + 16 E. MATCH.
- **G2 CANARY:** S9 — SiO2 planted at 60.093 — RE-CAUGHT at its row alone; the engine printed its own 60.083 and refused the planted expectation.
- **G3 DETERMINISM:** two full in-process executions of the battery, byte-identical.
- **G4 MUST-FAIL:** E9 — the slaking row authored with the water missing — RE-CAUGHT, the deficit exactly one H2O = 18.015 g (the deficit equals S5 itself — the closure charge the battery was designed to catch).
- **T1, the composition checksum:** 570,580 myu over the S1–S8 rows — recomputed in residues, reconstructed exact, MATCH.
- **T2, this engine's own witness lane:** 22/7 = 220/70 carried as the CRT residue pair over the four-prime basis — Garner reconstruct 220 and 70 exact (each < the basis product, the bound asserted), gcd 10, the fraction 22/7, re-encode round-trip PASS, long division 3.142857... repeating, period 6 — a repeating decimal carried by a machine whose arithmetic path has no integers at all.

## 4. The runblock — RECONSTRUCTED after the close-time loss, disclosed at every line

The block below is not the frozen file (lost, §2): it is the session's reconstruction, assembled after the wipe from pieces every one of which is named. **Byte-exact, read verbatim this session before the loss:** the header lines 1–20 and 23 (the engine's own architecture and review-contract lines) and the tail lines 60–85 (P13–P14, the E rows, the gates, T1, T2, SUMMARY, VERDICT). **Byte-exact by the run's own verified claim, re-verified against the record:** the 35 battery rows S1–P12, carried from the Engine 47 record's §4 fence lines 13–47 — run 2 reproduced those rows byte-identically (52/53 row-identity), and the overlap rows (S9, P13, P14, E9, E16, G1, G2, T1, SUMMARY, VERDICT) were diffed against that fence at this close, identical. **Reconstructed — the wording the reviewer's, the content the engine's own disclosed sentences:** header lines 21–22 (completing the E4 carrying-face clause the engine's source header carries verbatim) and line 24 (the any-mismatch review-contract clause, likewise from the source header). The reconstruction stands 23 bytes short of the lost file — the shortfall lives in the unknown true wording of line 24 — and its own identity, the numbers a future loader asserts: **85 lines / 7,209 bytes / bytesum 543,402.**

```text
ENGINE 48 - the CRT modular-residue engine (fresh build, zero code shared with Engines 1-47)
  architecture: every positive rational carried at rest as a pair of residue vectors
  (numerator residues, denominator residues) over a fixed basis of four coprime primes
  (1000003, 1000033, 1000037, 1000039 - each verified prime at startup by deterministic Miller-Rabin);
  the arithmetic path has no integers at all: +, -, x and / are componentwise modular
  operations on the residue pairs (division the reciprocal swap, no inverse ever computed);
  equality is the modular cross-product test; integers are reconstructed exactly only at
  print and compare, via Garner's mixed-radix scheme with the magnitude bound asserted
  (< the basis product), every reconstruction re-encoded to residues with a round-trip
  assert before the value is used; the gate order NAME -> held-table -> admission ->
  syntax -> grid. No Stern-Brocot paths (47), no prime-exponent lattices (46), no pulse
  trains (45), no inherited-multiplier descent (44), no bytecode VM (43), no event sweep
  (42), no segment tree (41), no interval containment (40), no depth ledger (39), no
  dual-column peel (38), no CPS fold (37), no token-table AST fold (36), no span-memo
  (35), no census tally (34), no fixed-point rewriting (33), no RPN reorder (31), no
  expression compiler (19).
  review contract: the frozen 53-row battery loaded at runtime from the Engine 47
  record's section-4 fence - lines 73 bytes 6003 bytesum 435804 verified at load -
  the expectations the frozen got-strings verbatim, never retyped; the one carried face:
  the E4 witness lane's carrying clause names this engine's CRT face (the frozen line
  names Engine 47's Stern-Brocot face - the value, the ratio and the repeating
  decimal identical, the E44 witness-lane precedent);
  source of record: .fc6-e48-source.ts, read at runtime - bytes 33471 bytesum 2492407
  any mismatch a finding raised for adjudication, never silently patched
S1  S got 100.086 g/mol (CaCO3 - Ch 14's lime pin) | expect 100.086 g/mol | PASS
S2  S got 56.077 g/mol (CaO - Ch 14's pin) | expect 56.077 g/mol | PASS
S3  S got 74.092 g/mol (Ca(OH)2 - Ch 14's and Ch 24's pin) | expect 74.092 g/mol | PASS
S4  S got 44.009 g/mol (CO2 - Ch 20's pin) | expect 44.009 g/mol | PASS
S5  S got 18.015 g/mol (H2O - Ch 4's pin) | expect 18.015 g/mol | PASS
S6  S got 60.083 g/mol (SiO2 - Ch 30's pin) | expect 60.083 g/mol | PASS
S7  S got 60.052 g/mol (CH3COOH - Ch 4's pin) | expect 60.052 g/mol | PASS
S8  S got 158.166 g/mol (Ca(C2H3O2)2 - Ch 21's pin) | expect 158.166 g/mol | PASS
S9  S got 60.083 g/mol | expect 60.093 g/mol | CAUGHT (the canary: 60.093 planted, 60.083 re-printed)
A1  A ADMIT (held table - CaCO3 rebuilt 100.086 g/mol = S1) | PASS
A2  A ADMIT (held table - CaO rebuilt 56.077 g/mol = S2) | PASS
A3  A ADMIT (held table - Ca(OH)2 rebuilt 74.092 g/mol = S3) | PASS
A4  A ADMIT (held table - CO2 rebuilt 44.009 g/mol = S4) | PASS
A5  A ADMIT (held table - CH3COOH rebuilt 60.052 g/mol = S7) | PASS
R1  R REFUSED (NAME gate - recognition register: dynamite)
R2  R REFUSED (NAME gate - recognition register: black powder)
R3  R REFUSED (NAME gate - recognition register: gunpowder)
R4  R REFUSED (NAME gate - recognition register: TNT)
R5  R REFUSED (NAME gate - recognition register: nitroglycerin)
R6  R REFUSED (NAME gate - recognition register: detonator)
R7  R REFUSED (NAME gate - recognition register: blasting cap)
R8  R REFUSED (NAME gate - recognition register: ANFO)
R9  R REFUSED (held table - Fe not held; Ch 19's bloomery owns the face)
P1  P got 56.077 + 44.009 = 100.086 (calcination, Ch 14's E2 face) | expect 100.086 | PASS
P2  P got 56.077 + 18.015 = 74.092 (slaking, Ch 14's E6 face) | expect 74.092 | PASS
P3  P got 74.092 + 44.009 = 118.101 = 100.086 + 18.015 (carbonation closes both ways) | expect 118.101 both ways | PASS
P4  P got 74.092 = 56.077 + 18.015 (dehydroxylation, the 512 degC rung - Ch 14's pin) | expect 74.092 | PASS
P5  P got 28.085 + 31.998 = 60.083 (Si + O2 = SiO2, Ch 30's face) | expect 60.083 | PASS
P6  P got 80.156 + 31.998 = 112.154 (2Ca + O2 = 2CaO) | expect 112.154 | PASS
P7  P got 100.086 + 120.104 = 220.190 = 158.166 + 18.015 + 44.009 (the vinegar quench closes both ways) | expect 220.190 both ways | PASS
P8  P got 40.078 + 15.999 = 56.077 (element build: CaO) | expect 56.077 | PASS
P9  P got 40.078 + 31.998 + 2.016 = 74.092 (element build: Ca(OH)2) | expect 74.092 | PASS
P10 P got 40.078 + 12.011 + 47.997 = 100.086 (element build: CaCO3) | expect 100.086 | PASS
P11 P got 40.078 + 48.044 + 6.048 + 63.996 = 158.166 (element build: Ca(C2H3O2)2) | expect 158.166 | PASS
P12 P got 12.011 + 31.998 = 44.009 (C + O2 = CO2) | expect 44.009 | PASS
P13 P got 4.032 + 31.998 = 36.030 (2H2 + O2 = 2H2O; 2 x 18.015) | expect 36.030 | PASS
P14 P got 24.022 + 4.032 + 31.998 = 60.052 (element build: CH3COOH) | expect 60.052 | PASS
E1  E got MA = 200/50 = 4.000 (lever: 2.00 m effort arm, 0.50 m load arm) | expect MA = 4.000 | PASS
E2  E got 300 / 4.000 = 75.0 N | expect 75.0 N | PASS
E3  E got 2000 / 4 segments = 500.0 N | expect 500.0 N | PASS
E4  E got MA = 220/70 = 22/7 held as the CRT residue pair (Garner reconstruct exact, gcd 10); decimal 3.142857... repeating | expect MA = 22/7 (the repeating decimal held exactly, no decimal point) | PASS
E5  E got F = W x 0.30/3.00 = 0.100 W (push at 3.00 m, weight at 0.30 m) | expect 0.100 W | PASS
E6  E got notch 0.90/3 = 0.30 m; hinge 0.09 m (10% of 0.90 m) | expect 0.30 m + 0.09 m | PASS
E7  E got 0.45% x 2.000 m = 9.0 mm (the quartz inversion step) | expect 9.0 mm | PASS
E8  E got 573 - 20 = 553 K (delta T to the inversion) | expect 553 K | PASS
E9  E got deficit 18.015 g (one H2O missing) | expect deficit 18.015 g | CAUGHT (must-fail: slaking authored with the water missing)
E10 E got expansion 83/917 = 9.051% (ice 0.917 g/mL; 1000/917 = 1.091) | expect 9.051% | PASS
E11 E got overflow 1000 x 83/917 = 90.51 mL | expect 90.51 mL | PASS
E12 E got KE = 1/2 x 1000 kg x (5 m/s)^2 = 12500 J | expect 12500 J | PASS
E13 E got 178 kJ/mol / 100.086 g/mol = 1.778 kJ/g | expect 1.778 kJ/g | PASS
E14 E got gain 25.994/74.092 = 35.08% (Ca(OH)2 -> CaCO3) | expect 35.08% | PASS
E15 E got dose 10.006 g CaCO3 needs 12.007 g CH3COOH = 240.1 mL of 5% w/v vinegar | expect 240.1 mL | PASS
E16 E got water of combination 18.015/74.092 = 24.31% | expect 24.31% | PASS
G1  G1 recount 53 rows (9 S + 5 A + 9 R + 14 P + 16 E) MATCH
G2  G2 canary re-caught at S9 alone (60.093 planted, 60.083 re-printed) HELD
G3  G3 determinism: HELD - the second in-process execution byte-identical
G4  G4 must-fail re-caught at exactly 18.015 g (one H2O; the deficit equals S5 itself) HELD
T1  T1 composition checksum 570580 myu (the exact S1-S8 sum) MATCH
T2  T2 22/7 = 220/70 carried as the CRT residue pair over the four-prime basis; Garner reconstruct 220 and 70 exact (each < the basis product, the bound asserted); gcd 10; 22/7; re-encode round-trip PASS; long division 3.142857... repeating, period 6 - a repeating decimal carried by a machine whose arithmetic path has no integers
SUMMARY  42 PASS / 2 caught / 9 refused / 0 FAIL
VERDICT  53/53 adjudicated, zero uncaught defects: CLEAN
```

## 5. Expectations provenance

- The got-strings were **loaded at runtime from the Engine 47 record's §4 fence** — the frozen run-4 block, itself spliced verbatim from Engine 47's own output at the session-134 close — with the fence identity asserted before a single row ran (73 lines / 6003 bytes / bytesum 435804) and the repo record's size verified at HEAD 5d18b4e7. No expectation was retyped by hand at this review: the review's whole point is that the frozen strings, not the reviewer's memory of them, are the contract. Every got-string in the §4 block is run 2's own output — the 35 S/A/R/P rows carried via the Engine 47 record's fence (run 2's byte-identical reproduction, re-verified at this close), the rest read verbatim this session before the loss.
- The battery's membership (frozen at session 134, unchanged here): S1–S8 the chapter's borrowed compositions (CaCO3, CaO, Ca(OH)2, CO2, H2O, SiO2, CH3COOH, Ca(C2H3O2)2 — all prior pins, no NEW mass faces); S9 the canary; A1–A5 the admissions (the five register molecules rebuilt and checked against their own S rows); R1–R8 the NAME-gate refusals (the explosive register, priced never); R9 the held-table refusal (Fe2O3 — Ch 19's face); P1–P14 the lime-cycle identities and element builds; E1–E16 the computed grid including the designed must-fail.
- **The E4 carrying clause, adjudicated not smoothed:** the frozen expectation matched verbatim ("MA = 22/7 (the repeating decimal held exactly, no decimal point)"); the got-string's carrying clause names this engine's CRT face ("held as the CRT residue pair (Garner reconstruct exact, gcd 10)") where the frozen got-line named Engine 47's SB path RRRLLLLLL — value 22/7, ratio and repeating decimal identical, the E44 witness-lane precedent declared before the run, printed in the engine's own header, adjudicated here rather than smoothed. The row counts PASS in both engines; the difference is disclosed, never reconciled away.

## 6. The session-135 checks (all PAID at this review close)

- **RA-1, the census re-proof (FC10's binding line — the NEW re-grepped at the review HEAD):** corpus = 110 files at HEAD 5d18b4e7 — the 28 local masters + the 10 fetched repo-only masters (ch01, ch02, ch31–ch36, fc1, fc2 — each byte-verified at its repo size) + the 5 FC canvas masters (fc7–fc11) + the 20 local records (19 engine/design records + the renderer record) + the 46 web editions + the index — FC6's own homes excluded. **21 NEW words zero-hit** (case-insensitive, word-bounded, a single alternation pass, Māori and Maori both carried, the wedge and undermin- stems included): fire-setting, fire-felling, felling, wedge, pulley, block and tackle, mechanical advantage, frost wedging, ice wedging, freeze-thaw, dunting, Diodorus, Hannibal, Selmecbánya, Nobel, waka, Māori, undermining, vinegar quench, TNT, blasting cap. **7 NEW values zero-hit in their claimed forms:** 0.917 g/mL (ice), 207 MPa (confined ice), 178 kJ/mol (calcination), 1627 (Selmecbánya), 1867 (dynamite), 0.45% (the quartz inversion's linear step — the bare digits ride inside 60 corpus hits, every one a digit-collision: 0.457 V the Cu|Ag pin, 0.4504 g glucose, 30.45×, 280.452, 0.45 g K banana, 0.45 M among them), −22 °C (the frost-wedging maximum — the bare digits ride inside −22.9, −2231, −2219.9, −22.85, −229.2). **The 512 °C PRIOR re-verified:** Ch 14 ×3 + FC9's canvas ×6 — the session-134 census catch stands. The index's new FC6 row carries no NEW word.
- **RA-3, the pins re-grepped (the session-112 line, fresh counts at the review HEAD, matching the session-134 ledger exactly):** CaCO3 100.086 Ch 14 ×7 + Ch 30 ×5; CaO 56.077 Ch 14 ×2 + Ch 30 ×9; Ca(OH)2 74.092 Ch 14 ×6 + Ch 24 ×5 + Ch 30 ×7; CO2 44.009 Ch 20 ×6; H2O 18.015 Ch 4 ×1; SiO2 60.083 Ch 30 ×4; CH3COOH 60.052 Ch 4 ×5; Ca(C2H3O2)2 158.166 Ch 21 ×2 + Ch 23 ×1 + Ch 31 ×1 + Ch 33 ×2; Ca 40.078 Ch 3 ×1; Si 28.085 Ch 14 ×3 + Ch 30 ×5; O2 31.998 Ch 10 ×4 + Ch 7 ×1; the quartz door 573 °C Ch 30 ×11 (×7 with unit); the dehydroxylation rung 512 °C Ch 14 ×3 + FC9's canvas ×6. **The session-133 typography line:** every pin also grepped in its owner's web edition — the web counts lower exactly where the pin lives in md-only apparatus (the Canon-Coverage, ledger, and review sections the web pages cut by contract), disclosed rather than reconciled.
- **RA-4, the [convergent] battery re-confirmed at fresh named sources:** the fire-setting canon — Hérault's Copper-Age workings (the evidence class), Diodorus Siculus ~60 BC (rock heated by fire and struck with iron), Pliny NH Book XXXIII (the vinegar quench), Livy's Hannibal record with the modern laboratory verification; **Selmecbánya (Banská Štiavnica) 1627** — black powder's first mining use; **Nobel's dynamite 1867** (the kieselguhr patent record); the quartz inversion **573 °C** and the dunting hygiene (the dunt literature); the freeze canon — **−3 to −8 °C** the active band verbatim, **207 MPa at −22 °C** confined verbatim, the **>91% saturation** damage threshold and the 9% frost-damage construction figure; ice at **0.917 g/mL**; the Māori fire-felling canon (the burn-notched waka method, the IAWF source); the hand-felling ratios verbatim (the notch no deeper than one-third of the trunk's diameter, the hinge about 10% of it); the demolition canon (the wrecking ball 450–5,400 kg of iron, heyday 1940s–50s, abandoned for control not force; high-reach excavators to 67 m by 2017, the record successor to 90 m); the lime cycle's datums (carbonation's **40–80% RH** window verbatim; calcination above roughly **840 °C** and **178 kJ/mol** verbatim). **One transparency note, no finding:** the chapter's ≤50 °C/h dunting hygiene is the conservative end of the practitioner schedules (a ~42–93 °C/h spread across the sources) — carried as the binding line for the next review, the chapter's own number unchanged.
- **Ex FC6.6's withheld ◆ answer delivered** at the canvas's Revision Appendix per the FC alternation: the recognition-only levels, the history-versus-instruction distinction, the NAME gate as the P18 fence in machine form — FC6 battery rows only, no new figures.
- **The record-layer confirmation:** session 134's disclosed correction (the session-133 close texts' "all drafted and reviewed" wording had overlooked the map's own FC6 line) stands confirmed; the map's FC6 line, moved to `drafted` at session 134, moves to `reviewed` at this close — the Field Companion's chapters all drafted and reviewed.
- **The standing errata (Ch 10 Ex 10.5; the Ag 107.897 seam) were NOT touched by this review** and remain standing for their next touches.

## 7. The Engine 48 source — lost at the close, disclosed at its line

The executed source cannot be spliced: the same close-time wipe that took the runblock (§2) took the frozen source file (.fc6-e48-source.ts), and no copy had been pushed before the reset. Its verified identity is recorded as history: **601 lines / 33,471 bytes / bytesum 2,492,407** — asserted by the engine at run 2 (the source of record read at runtime, its stats printed in the block's own header line) and re-verified at this close before the wipe. What the record holds instead, every piece read this session before the loss and named at its line: the engine's own header comment (the design and review contract, carried at §1); the §4 block (the engine's own console output, reconstructed as disclosed above); the deterministic Miller-Rabin startup gate (BigInt, the small-prime base 2–37, a startup gate outside the arithmetic path); the basis construction (the candidates 1000003, 1000033, 1000037, 1000039, 1000081, 1000099, MR-filtered, K = 4 asserted with a construction throw); the manual UTF-8 byteLen/byteSum walk (the session-134 house convention — TextEncoder absent in the sandbox); the runtime verification lines (the fence identity asserted before any row ran, the repo record's size checked at HEAD via the GitHub listing, the source of record read at runtime, the runblock written by the engine itself at run 2, the block self-stats printed); the intStr divisibility fix of run 1 (num % den = 0 — the value exact, the carrier untouched); and the final return object (basis, repoRecordOk, fenceStats, sourceStats, g3Held, counts, rowByteIdentical, rowDiffs, gateCompare, summaryMatch, verdictMatch, blockStats, block). The loss is total for the middle four hundred-odd lines — the residue core, the molecule parser, the NAME gate, the battery rows, and the print layer — and this record claims nothing about them beyond what §1's design spec and §4's block attest. The session's verified claims stand as recorded; the source's verbatim text does not ride with this record.

## 8. Session 135 close summary

FC6 "Heavy Work Without Explosives" reviewed — the Phase-3 adversarial review **PASS, zero findings**: Engine 48 (the CRT modular-residue engine, fresh, zero code shared with Engines 1–47) re-executed the frozen 53-row battery with the expectations loaded at runtime from the Engine 47 record's §4 fence — run 2 CLEAN, 42 PASS / 2 caught / 9 refused / 0 FAIL, G1–G4 held at the same run, T1 570,580 myu MATCH, T2 this engine's own residue witness lane, the honest history printed above (the pre-run probe's fence off-by-one, run 1's E12 representation throw), the E4 carrying clause disclosed and adjudicated, 52/53 rows byte-identical. The census re-proven at the review HEAD (FC10's RA-1 line, the 110-file corpus), the pins re-grepped in their owners' own pages with the session-133 typography line paid, the [convergent] battery re-confirmed at fresh named sources with one transparency note carried forward as the next review's binding line, and Ex FC6.6's withheld ◆ answer delivered at the appendix. **The close-time loss, named here rather than buried:** a platform filesystem reset wiped the scratch layer between this record's part-writes — the frozen source and runblock files lost, the §4 block reconstructed with 82 of 85 lines byte-exact and the three reconstructed header lines named, the source recorded as lost at §7 with its verified identity held as history; the record claims nothing the surviving bytes cannot attest. The reviewed chapter master, its re-rendered web edition (the renderer re-validated byte-identical on the fc11 pair first; the status clause the only pre-canon change), and this record pushed ALWAYS-SYNC at this session's close. NEXT: session 136 — the Field Companion volume close, the survey follow-ups, or another map extension, on the user's call.
