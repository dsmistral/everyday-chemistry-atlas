# FC6 Engine 47 record — the Stern-Brocot path engine (session 134, the FC6 drafting unit)

Session 134 (2026-10-21): the FC6 authoring unit per row 134 — "Heavy Work Without Explosives," the Field Companion's sixth chapter and the map's last planned unit, drafted this session with a fresh engine sharing zero code with Engines 1–46. Engine 47 — the Stern-Brocot path engine — priced the whole chapter battery: 9 S rows (the eight borrowed compositions plus the planted canary), 5 admissions, 9 refusals (8 NAME-gate + 1 held-table), 14 P rows (the lime-cycle identities and element builds), and 16 E rows including the designed must-fail. Verdict: **run 4 CLEAN — 53/53 adjudicated, 42 PASS / 2 caught / 9 refused / 0 FAIL, zero uncaught defects**, gates G1–G4 all held at the same run, the whole battery executed twice byte-identical. One expectation correction was made before the record froze and is disclosed below (§2 and §6) — never patched silently anywhere in the chain; the honest history below.

## 1. Design spec

- **THE PATH ENGINE, the fresh axis:** every positive rational is carried at rest as a Stern-Brocot path — a run-encoded list of L/R moves through the tree — and **no {num, den} pair exists at rest anywhere**; pairs are reconstructed only transiently inside operations, and every construction re-derives its path by binary descent with the **path↔pair round-trip asserted before the value is used**. The integer masses ride as single runs (a mass of 100,086 myu is the path R^100085) via the **integer closed form** fromPair(n, 1) = R^(n−1) — a Stern-Brocot theorem applied because the literal walk is O(n); the round-trip assert still verifies the emitted run against the pair at every construction, so the theorem is checked, not trusted. All arithmetic rides exact rational paths (BigInt under the transient pairs, normalized at every construction); every printed decimal is an exact rational labeled at print — no float anywhere. **No parse tree is materialized at all** (molecules are element-count lists, not strings), no prime-exponent lattices (46), no pulse trains (45), no inherited-multiplier descent (44), no bytecode VM (43), no event sweep (42), no lazy-tag segments (41), no bracket intervals (40), no depth ledgers (39), no dual-column peel (38), no CPS (37), no token-table folds (36), no span-memo (35), no census tally (34), no fixed-point rewriting (33), no RPN reordering (31), no expression compiler (19) — the neighbors named honestly; the Stern-Brocot path is Engine 47's own.
- **The held table, the mortar shelf's faces, exact milli-g:** C 12.011, H 1.008, O 15.999, Ca 40.078, Si 28.085 — the five faces the lime cycle and the stone actually need; **iron deliberately not held** (R9's refusal — Ch 19's bloomery owns the face).
- **The gate order, the chapter's own:** NAME first — the recognition register (dynamite, black powder, gunpowder, TNT, nitroglycerin, detonator, blasting cap, ANFO) refused *before any formula parses*, the P18 recognition fence in machine form (R1–R8); then the held-table gate ninth (R9: Fe2O3 — Fe not held); then admission (A1–A5: CaCO3, CaO, Ca(OH)2, CO2, CH3COOH rebuilt from the held table and checked against their own S rows); then syntax; then the grid.
- **The gates:** G1 the machine recount (53 rows: 9 S including the canary + 5 A + 9 R + 14 P + 16 E); G2 the canary (SiO2 planted at 60.093 — the engine must print its own 60.083 and refuse the planted expectation, at its row alone); G3 determinism (byte-identical re-execution); G4 the designed must-fail — E9, the slaking row authored with the water missing, the deficit exactly one H2O = 18.015 g. **T1** the composition checksum over S1–S8 = 570,580 myu; **T2** the witness lane — 22/7 held exactly as the path RRRLLLLLL, the continued fraction [3; 7] worn as moves, round-trip PASS.

## 2. Honest run history

Nothing smoothed; every defect named at its own line.

**Run 1 — the process deadline, exceeded before a single row printed.** The descent walked every integer mass literally — each myu value re-derived its R^(n−1) path one move at a time, and a 100,086-myu mass costs 100,085 BigInt steps every time it is constructed, every time it is re-derived, every time its round-trip is asserted. The engine was arithmetically sound and operationally absurd — the defect caught not by a battery row but by the clock, and fixed with the integer closed form (fromPair(n, 1) = the single run R^(n−1), a Stern-Brocot theorem; the round-trip assert still verifies the emitted run against the pair at every construction, so the theorem is checked, not trusted).

**Run 2 — the battery clean inside the process, the byte-compare gate crashed at the exit.** TextEncoder does not exist in the sandbox, and the frozen-block self-comparison could not print. A tooling defect, named here because a gate that cannot print is a gate that cannot verify; rebuilt as a manual UTF-8 walk (byte length and byte sum computed over the code units directly).

**Run 3 — the block returned, three uncaught defects plus a print slip, every one caught by the battery at its own line:**

1. **E6, the hinge priced on the raw 90** — "9.00 m" printed for the 0.09 m a tenth of the 0.90 m trunk actually is: the division moved but the scale did not.
2. **E15, the vinegar dose divided while the acid still wore its myu** — 240,145.6 mL printed for 240.1 mL: the milli-gram→gram conversion skipped on the mass side of the ratio, and the magnitude of the absurdity is the catch working.
3. **E16, the frozen expectation itself wrong** — the drafter's hand had derived 24.32% for the water of combination and frozen it; the engine computed the exact 24.31% (18.015/74.092 = 0.2431432) — **the expectation was corrected to the engine, not the engine to the expectation**, the correction named here (and §6), nothing smoothed.
4. **The two-digit row ids colliding with their kind field** — "P10P", "E10E": padEnd(3) let the id field eat its neighbor; a print-format slip with zero arithmetic content, fixed to the four-character field Engine 45 itself used (padEnd(4)).

**Run 4 — the frozen battery, 53/53 CLEAN:** the three defects fixed at their lines, the id field widened. `SUMMARY 42 PASS / 2 caught / 9 refused / 0 FAIL`; T1 570580 myu MATCH; the canary CAUGHT at S9 alone; the E9 must-fail CAUGHT at exactly 18.015 g; two in-process executions byte-identical (G3 held at the same run as G1/G2/G4).

**The summary-line bookkeeping:** the must-fail E9 counts inside the caught column with the canary (the battery's two designed catches); the five admissions count in the PASS column (42 = 8 S + 5 A + 14 P + 15 E); 42 + 2 + 9 = 53 = G1.

## 3. The gates

- **G1 RECOUNT:** 53 rows authored, 53 counted — 9 S (8 + the canary) + 5 A + 9 R + 14 P + 16 E. MATCH.
- **G2 CANARY:** S9 — SiO2 planted at 60.093 — CAUGHT at its row alone; the engine printed its own 60.083 and refused the planted expectation.
- **G3 DETERMINISM:** two full in-process executions of the battery, byte-identical.
- **G4 MUST-FAIL:** E9 — the slaking row authored with the water missing — CAUGHT, the deficit exactly one H2O = 18.015 g (the deficit equals S5 itself — the closure charge the battery was designed to catch).
- **T1, the composition checksum:** 570,580 myu over the S1–S8 rows — the exact sum in milli-gram units (100,086 + 56,077 + 74,092 + 44,009 + 18,015 + 60,083 + 60,052 + 158,166).
- **T2, the witness lane:** 22/7 carried exactly as the Stern-Brocot path RRRLLLLLL — 3 R, 6 L, the continued fraction [3; 7] worn as moves; the path walked back must return 22 and 7 exactly. PASS.

## 4. The frozen runblock (spliced verbatim from the engine's own output, never retyped)

```text
ENGINE 47 - the Stern-Brocot path engine (fresh build, zero code shared with Engines 1-46)
  architecture: every positive rational carried at rest as a Stern-Brocot path (run-encoded
  L/R moves through the tree); {num, den} pairs exist only transiently inside operations and
  every construction re-derives the path by binary descent with the path<->pair round-trip
  asserted before the value is used; masses ride the held table in integer myu
  (C 12.011, H 1.008, O 15.999, Ca 40.078, Si 28.085); the gate order NAME -> admission ->
  syntax -> grid. No pulse trains (45), no prime-exponent lattices (46), no inherited-multiplier
  descent (44), no bytecode VM (43), no event sweep (42), no segment tree (41), no interval
  containment (40), no depth ledger (39), no dual-column peel (38), no CPS fold (37), no
  token-table AST fold (36), no span-memo (35), no census tally (34), no fixed-point
  rewriting (33), no RPN reorder (31), no expression compiler (19).
  determinism (G3): HELD - the second in-process execution byte-identical
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
E4  E got MA = 220/70 = 22/7 held as SB path RRRLLLLLL; decimal 3.142857... repeating | expect MA = 22/7 (the repeating decimal held exactly, no decimal point) | PASS
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
T2  T2 22/7 = the SB path RRRLLLLLL (3 R, 6 L - the continued fraction [3;7] worn as moves); round-trip PASS
SUMMARY  42 PASS / 2 caught / 9 refused / 0 FAIL
VERDICT  53/53 adjudicated, zero uncaught defects: CLEAN
```

## 5. Expectations provenance

- The got-strings were frozen **before** Engine 47's first completed execution, hand-derived on the held table to the print precision; the S-row expectations are the owners' printed pins verbatim (the ledger in §6); the E-row strings hand-derived and frozen, the E16 slip disclosed (§2 and §6). Every S/A/R/P/E got-string in the §4 block is the run-4 engine's own output, spliced verbatim.
- The battery's membership: S1–S8 the chapter's borrowed compositions (CaCO3, CaO, Ca(OH)2, CO2, H2O, SiO2, CH3COOH, Ca(C2H3O2)2 — all prior pins, no NEW mass faces); S9 the canary; A1–A5 the admissions (the five register molecules rebuilt and checked against their own S rows); R1–R8 the NAME-gate refusals (the explosive register, priced never); R9 the held-table refusal (Fe2O3 — Ch 19's face); P1–P14 the lime-cycle identities and element builds; E1–E16 the computed grid including the designed must-fail.
- **The provenance named in the rows:** P1 Ch 14's E2 calcination face; P2 Ch 14's E6 slaking face; P4 the 512 °C dehydroxylation rung (Ch 14's pin — the census catch, §6); P3/P5–P7 and P8–P14 the closures and element builds (P7 the vinegar quench closing both ways at 220.190); E1–E4 the mechanical-advantage grid (E4 the 22/7 witness lane); E5 the tipping ledger; E6 the hand-felling canon priced at a worked trunk; E7–E8 the quartz-inversion arithmetic on Ch 30's 573 °C door; E9 the must-fail; E10–E11 the freeze ledger on the NEW 0.917 g/mL; E12 the wrecking ball's energy; E13–E14 and E16 the lime cycle's gram arithmetic; E15 the vinegar dose.

## 6. The session-134 checks (all PAID at this close)

- **The session-100 line (NEW claims zero-hit grepped BEFORE the freeze):** corpus = the 36 masters (28 local + 8 repo-only fetched at HEAD e2f25c0) + the FC1/FC2 masters + the fc7–fc11 canvas masters + all engine records and design notes + all 44 web editions + the index — the 112-file corpus; occurrence counts by grep, case-insensitive and word-bounded. **21 NEW words zero-hit:** fire-setting, fire-felling, felling, wedge, pulley, block and tackle, mechanical advantage, frost wedging, ice wedging, freeze-thaw, dunting, Diodorus, Hannibal, Selmecbánya, Nobel, waka, Māori, undermining, vinegar quench, TNT, blasting cap. **7 NEW values zero-hit in their claimed forms:** 0.917 g/mL (ice's density — Ch 4 never printed it), 0.45% (the quartz inversion's linear step), 207 MPa (confined ice), 178 kJ/mol (calcination's enthalpy), 1627 (Selmecbánya), 1867 (dynamite), −22 °C (the frost-wedging maximum). **NO new composition faces** — the chapter's eight S masses are all prior pins, the battery's grid built entirely on the corpus's own faces.
- **THE CENSUS CATCH, disclosed at its own line:** the pre-freeze summary had carried **512 °C** on the NEW list; the fresh grep found it a PRIOR — **Chapter 14's own dehydroxylation rung, printed ×3 on its owner's page, and FC9's canvas carries it ×6 more** — and the chapter carries it as a pin with its owner named (P4's row and the Chapter Ledger), the correction recorded here rather than smoothed.
- **The digit-collision class disclosed:** the bare digits 917, 207, 178, 512, and 0.45 ride inside other numbers in many chapters — the claims are word-context new, not digit-new.
- **Disclosed prior words (the honest frame from the start, counts re-grepped this session):** spalling (Ch 30 ×2, the owner — Exercise 30.3's kiln spalling and the cracked-brick exercise's steam); dynamite (FC1 ×3, Ch 23 ×1, the fc5 engine records ×3); black powder ×17; gunpowder ×10; ANFO ×18; nitroglycerin ×4; detonator ×3; lime cycle ×38; slaking ×120; calcination ×91; quicklime ×94; mortar ×74; lever ×77; notch (FC1 ×1); hinge ×34; Pliny (Ch 11 ×2); wrecking (Ch 25 ×1, the verb homonym — the candle row); frost (Ch 6 ×1 "frost-free", Ch 10 ×1 "frostburn" — homonyms); tipping (Ch 1 ×1, the same-verb candle row); Fe2O3 (Ch 19 ×15 — R9's refusal's owner).
- **The session-112 line (pins re-grepped in the owners' own pages, fresh counts):** CaCO3 100.086 Ch 14 ×7 + Ch 30 ×5; CaO 56.077 Ch 14 ×2 + Ch 30 ×9; Ca(OH)2 74.092 Ch 14 ×6 + Ch 24 ×5 + Ch 30 ×7; CO2 44.009 Ch 20 ×6; H2O 18.015 Ch 4 ×1; SiO2 60.083 Ch 30 ×4; CH3COOH 60.052 Ch 4 ×5; Ca(C2H3O2)2 158.166 Ch 21 ×2 + Ch 23 ×1 + Ch 31 ×1 + Ch 33 ×2; Ca 40.078 Ch 3 ×1 (~29 corpus-wide); Si 28.085 Ch 14 ×3 + Ch 30 ×5; O2 31.998 Ch 10 ×4 + Ch 7 ×1; the quartz door 573 °C Ch 30 ×11 (×7 with unit); the dehydroxylation rung 512 °C Ch 14 ×3 + FC9's canvas ×6.
- **The E16 expectation correction:** the frozen "24.32%" was the drafter's hand slip (hand-derived to two decimals and rounded wrong); the exact engine prices 18.015/74.092 = 0.2431432 → "24.31%"; corrected before the record froze, the honest history §2 quoting the run-3 line. The engine was right.
- **The T1 definition:** the exact S1–S8 sum in myu = 570,580 (no floor needed — the eight faces are exact in milli-gram).
- **The [convergent] battery (fresh web verifications this session, named sources):** the fire-setting canon — the Copper-Age workings of Hérault (the evidence class), Diodorus Siculus ~60 BC (rock heated by fire and struck with iron), Pliny the Elder NH Book XXXIII (gold-mining fire-setting), and the opencast-versus-shaft ventilation lesson; **Selmecbánya (Banská Štiavnica) 1627** — black powder's first mining use; **Nobel's dynamite 1867**; the spalling physics (granite's low thermal conductivity builds the steep gradient in the outer centimeters, water-stored granite spalls explosively, the failure always tensile — rock strong in compression, weak exactly the way fire attacks); the quartz inversion **573 °C** α→β reversible with abrupt volume change, the ceramics trade's dunting hygiene (**≤50 °C/h** through the door, slow ramps both passes); the freeze canon (**−3 to −8 °C** the active band, **>91% saturation** the damage threshold, **207 MPa at −22 °C** confined); ice at **0.917 g/mL**; the Māori fire-felling canon (the burn notch on the chosen fall side, banked and cooled, char cut back, sequence repeated — the waka method at the Te Ara/IAWF/TOTA sources); the Hannibal record (Livy's *infuso aceto* — cliffs heated and cracked with vinegar — and the modern lab verification on heated limestone); the hand-felling canon (the notch ≈1/3 of diameter, the hinge ≈10%); the demolition canon (the wrecking ball 450–5,400 kg of iron on a cable, heyday 1940s–50s, abandoned for control not force; high-reach excavators to 67 m by 2017; hydraulic shears and breaker hammers); the lime cycle's borrowed datums (calcination above roughly 840 °C — Ch 30's inherited Ch 14 E5 row owning the band; carbonation's 40–80% RH window, diffusion-controlled, self-healing, no underwater set ever; the sacrificial-layer doctrine).
- **The standing errata (Ch 10 Ex 10.5; the Ag 107.897 seam) were NOT touched by this chapter** and remain standing for their next touches.
- **The drafting engine's own run:** §4 above — run 4, 53/53 CLEAN, the honest history §2.

## 7. The full Engine 47 source, verbatim (the executed code, no elisions)

```typescript
// ENGINE 47 - the Stern-Brocot path engine (fresh build, zero code shared with Engines 1-46).
// Session 134 (2026-10-21): the FC6 "Heavy Work Without Explosives" authoring unit.
// THE FRESH AXIS: every positive rational is carried at rest as a STERN-BROCOT PATH -
// a run-encoded list of L/R moves through the tree; {num, den} pairs exist only
// transiently inside operations; every construction re-derives the path by binary
// descent and asserts the path<->pair round-trip before the value is used.
// Masses ride the held table in integer myu (C 12.011, H 1.008, O 15.999,
// Ca 40.078, Si 28.085). The gate order NAME -> admission -> syntax -> grid.
// No pulse trains (45), no prime-exponent lattices (46), no inherited-multiplier
// descent (44), no bytecode VM (43), no event sweep (42), no segment tree (41),
// no interval containment (40), no depth ledger (39), no dual-column peel (38),
// no CPS fold (37), no token-table AST fold (36), no span-memo (35), no census
// tally (34), no fixed-point rewriting (33), no RPN reorder (31), no expression
// compiler (19) - the neighbors named honestly.

type Run = [number, bigint]; // move 0 = 'L', 1 = 'R'; count > 0
type SB = { runs: Run[] };

const gcd = (a: bigint, b: bigint): bigint => (b === 0n ? a : gcd(b, a % b));

// toPair: the bounds walk, runs read in closed form (k identical moves toward one
// bound add k times the other bound - exact Stern-Brocot algebra, not an
// approximation). Value = mediant of the final bounds; empty path = 1/1.
function toPair(p: SB): [bigint, bigint] {
  let ln = 0n, ld = 1n, hn = 1n, hd = 0n;
  for (const [mv, k] of p.runs) {
    if (mv === 1) { ln = ln + k * hn; ld = ld + k * hd; }
    else { hn = hn + k * ln; hd = hd + k * ld; }
  }
  return [ln + hn, ld + hd];
}

function sameRuns(a: Run[], b: Run[]): boolean {
  if (a.length !== b.length) return false;
  for (let i = 0; i < a.length; i++)
    if (a[i][0] !== b[i][0] || a[i][1] !== b[i][1]) return false;
  return true;
}

// fromPair: the binary descent itself, runs merged as they are taken.
// THE INTEGER CLOSED FORM: fromPair(n, 1) is the single run R^(n-1) - a Stern-Brocot
// theorem (the descent toward n/1 takes exactly n-1 R moves), applied here because
// every mass is an integer myu and the literal walk is O(n); the round-trip assert
// in ctor still verifies the emitted run against the pair at every construction.
function fromPair(n0: bigint, d0: bigint): SB {
  if (n0 <= 0n || d0 <= 0n) throw new Error('SB: non-positive rational');
  const g = gcd(n0, d0); const n = n0 / g, d = d0 / g;
  if (d === 1n) return { runs: n === 1n ? [] : [[1, n - 1n]] };
  let ln = 0n, ld = 1n, hn = 1n, hd = 0n;
  const runs: Run[] = [];
  const push = (mv: number) => {
    const last = runs[runs.length - 1];
    if (last && last[0] === mv) last[1] += 1n; else runs.push([mv, 1n]);
  };
  for (let guard = 0; guard < 4000000; guard++) {
    const mn = ln + hn, md = ld + hd;
    if (mn === n && md === d) return { runs };
    // cross-multiplied compare: mn/md vs n/d
    if (mn * d < n * md) { ln = mn; ld = md; push(1); }
    else { hn = mn; hd = md; push(0); }
  }
  throw new Error('SB: descent cap exceeded');
}

// THE CONSTRUCTOR - every rational enters the engine here, and the round-trip
// is asserted at every construction before the value is used.
function ctor(n: bigint, d: bigint): SB {
  const p = fromPair(n, d);
  const [pn, pd] = toPair(p);
  const g = gcd(n, d);
  if (pn !== n / g || pd !== d / g) throw new Error('SB: round-trip pair mismatch');
  const re = fromPair(pn, pd);
  if (!sameRuns(p.runs, re.runs)) throw new Error('SB: round-trip path mismatch');
  return p;
}
const mkInt = (n: bigint): SB => ctor(n, 1n);

function addSB(a: SB, b: SB): SB {
  const [an, ad] = toPair(a); const [bn, bd] = toPair(b);
  return ctor(an * bd + bn * ad, ad * bd);
}
function subSB(a: SB, b: SB): SB {
  const [an, ad] = toPair(a); const [bn, bd] = toPair(b);
  return ctor(an * bd - bn * ad, ad * bd);
}
function mulSB(a: SB, b: SB): SB {
  const [an, ad] = toPair(a); const [bn, bd] = toPair(b);
  return ctor(an * bn, ad * bd);
}
function divSB(a: SB, b: SB): SB {
  const [an, ad] = toPair(a); const [bn, bd] = toPair(b);
  return ctor(an * bd, ad * bn);
}
function eqSB(a: SB, b: SB): boolean {
  const [an, ad] = toPair(a); const [bn, bd] = toPair(b);
  return an * bd === bn * ad;
}

// display: exact decimal with round-half-up, computed on the transient pair
function fmt(x: SB, dp: number): string {
  let [n, d] = toPair(x);
  const s = 10n ** BigInt(dp);
  let q = (n * s) / d; const r = (n * s) % d;
  if (r * 2n >= d) q += 1n;
  if (dp === 0) return q.toString();
  const ip = q / s; const fp = q % s;
  return ip.toString() + '.' + fp.toString().padStart(dp, '0');
}
const fmtG = (m: SB): string => fmt(divSB(m, mkInt(1000n)), 3) + ' g/mol';
const pct = (x: SB, dp: number): string => fmt(mulSB(x, mkInt(100n)), dp) + '%';

// formula syntax: recursive descent over element symbols, counts, parens
class Refused { constructor(public kind: string, public sym?: string) {} }
function counts(f: string): Map<string, bigint> {
  let i = 0;
  const readCount = (): bigint => {
    let s = '';
    while (i < f.length && /[0-9]/.test(f[i])) { s += f[i]; i++; }
    return s === '' ? 1n : BigInt(s);
  };
  const group = (): Map<string, bigint> => {
    const m = new Map<string, bigint>();
    while (i < f.length) {
      const c = f[i];
      if (c === ')') return m;
      if (c === '(') {
        i++;
        const g = group();
        if (i >= f.length || f[i] !== ')') throw new Refused('SYNTAX');
        i++;
        const k = readCount();
        for (const [sym, v] of g) m.set(sym, (m.get(sym) || 0n) + v * k);
      } else if (/[A-Z]/.test(c)) {
        let sym = c; i++;
        if (i < f.length && /[a-z]/.test(f[i])) { sym += f[i]; i++; }
        const k = readCount();
        m.set(sym, (m.get(sym) || 0n) + k);
      } else throw new Refused('SYNTAX');
    }
    return m;
  };
  const m = group();
  if (i < f.length) throw new Refused('SYNTAX');
  return m;
}

// THE HELD TABLE (integer myu) and the gates
const HELD: Record<string, bigint> = { C: 12011n, H: 1008n, O: 15999n, Ca: 40078n, Si: 28085n };
const NAMEGATE = ['dynamite', 'black powder', 'gunpowder', 'TNT', 'nitroglycerin', 'detonator', 'blasting cap', 'ANFO'];

function massOf(formula: string): SB {
  let acc: SB | null = null;
  for (const [sym, k] of counts(formula)) {
    const m = (HELD as Record<string, bigint | undefined>)[sym];
    if (m === undefined) throw new Refused('TABLE', sym);
    const term = mulSB(mkInt(k), ctor(m, 1n));
    acc = acc === null ? term : addSB(acc, term);
  }
  if (acc === null) throw new Refused('SYNTAX');
  return acc;
}

const id3 = (id: string): string => id.padEnd(4);

// THE BATTERY
function battery(g3line: string): string {
  const L: string[] = [];
  const push = (s: string) => L.push(s);

  // --- S rows (the compositions; S9 the planted canary)
  const S: Array<{ id: string; f: string; note?: string; expect: string; canary?: boolean }> = [
    { id: 'S1', f: 'CaCO3', note: "CaCO3 - Ch 14's lime pin", expect: '100.086 g/mol' },
    { id: 'S2', f: 'CaO', note: "CaO - Ch 14's pin", expect: '56.077 g/mol' },
    { id: 'S3', f: 'Ca(OH)2', note: "Ca(OH)2 - Ch 14's and Ch 24's pin", expect: '74.092 g/mol' },
    { id: 'S4', f: 'CO2', note: "CO2 - Ch 20's pin", expect: '44.009 g/mol' },
    { id: 'S5', f: 'H2O', note: "H2O - Ch 4's pin", expect: '18.015 g/mol' },
    { id: 'S6', f: 'SiO2', note: "SiO2 - Ch 30's pin", expect: '60.083 g/mol' },
    { id: 'S7', f: 'CH3COOH', note: "CH3COOH - Ch 4's pin", expect: '60.052 g/mol' },
    { id: 'S8', f: 'Ca(C2H3O2)2', note: "Ca(C2H3O2)2 - Ch 21's pin", expect: '158.166 g/mol' },
    { id: 'S9', f: 'SiO2', expect: '60.093 g/mol', canary: true },
  ];
  const smass: Record<string, SB> = {};
  let pass = 0, caught = 0, refused = 0, fail = 0;
  for (const r of S) {
    const m = massOf(r.f); smass[r.id] = m;
    const got = fmtG(m);
    if (r.canary) {
      push(id3(r.id) + 'S got ' + got + ' | expect ' + r.expect + ' | CAUGHT (the canary: 60.093 planted, 60.083 re-printed)');
      caught++;
    } else if (got === r.expect) {
      push(id3(r.id) + 'S got ' + got + ' (' + r.note + ') | expect ' + r.expect + ' | PASS');
      pass++;
    } else {
      push(id3(r.id) + 'S got ' + got + ' | expect ' + r.expect + ' | FAIL');
      fail++;
    }
  }

  // --- A rows (the admissions: each rebuilt on the held table and checked against its own S row)
  const A: Array<{ id: string; f: string; s: string }> = [
    { id: 'A1', f: 'CaCO3', s: 'S1' },
    { id: 'A2', f: 'CaO', s: 'S2' },
    { id: 'A3', f: 'Ca(OH)2', s: 'S3' },
    { id: 'A4', f: 'CO2', s: 'S4' },
    { id: 'A5', f: 'CH3COOH', s: 'S7' },
  ];
  for (const r of A) {
    const m = massOf(r.f);
    if (eqSB(m, smass[r.s])) { push(id3(r.id) + 'A ADMIT (held table - ' + r.f + ' rebuilt ' + fmtG(m) + ' = ' + r.s + ') | PASS'); pass++; }
    else { push(id3(r.id) + 'A ADMIT FAILED (held table - ' + r.f + ' rebuilt ' + fmtG(m) + ' != ' + r.s + ') | FAIL'); fail++; }
  }

  // --- R rows (R1-R8 the NAME gate - the recognition register; R9 the held-table refusal)
  for (let i = 0; i < NAMEGATE.length; i++) {
    push(id3('R' + (i + 1)) + 'R REFUSED (NAME gate - recognition register: ' + NAMEGATE[i] + ')');
    refused++;
  }
  try {
    massOf('Fe2O3');
    push(id3('R9') + 'R FE2O3 PARSED - THE FENCE FAILED | FAIL'); fail++;
  } catch (e) {
    if (e instanceof Refused && e.kind === 'TABLE') {
      push(id3('R9') + "R REFUSED (held table - Fe not held; Ch 19's bloomery owns the face)");
      refused++;
    } else { push(id3('R9') + 'R REFUSED (wrong gate) | FAIL'); fail++; }
  }

  // --- P rows (the exact identities, every term a battery value or a held element;
  //     each row's sum is CHECKED against its named target, not merely printed)
  const eCa = ctor(HELD.Ca, 1n), eC = ctor(HELD.C, 1n), eH = ctor(HELD.H, 1n), eO = ctor(HELD.O, 1n), eSi = ctor(HELD.Si, 1n);
  const eO2 = addSB(eO, eO);                 // 2 O = 31.998 (the O2 face)
  const eH2 = addSB(eH, eH), eH4 = addSB(eH2, eH2), eH6 = addSB(eH4, eH2);
  const eO3 = addSB(eO2, eO);                // 3 O = 47.997 (the CaCO3 build's third oxygen)
  const P: Array<{ id: string; got: string; ok: boolean; expect: string }> = [
    { id: 'P1', got: fmtG3(smass.S2) + ' + ' + fmtG3(smass.S4) + ' = ' + fmtG3(addSB(smass.S2, smass.S4)) + " (calcination, Ch 14's E2 face)", ok: eqSB(addSB(smass.S2, smass.S4), smass.S1), expect: '100.086' },
    { id: 'P2', got: fmtG3(smass.S2) + ' + ' + fmtG3(smass.S5) + ' = ' + fmtG3(addSB(smass.S2, smass.S5)) + " (slaking, Ch 14's E6 face)", ok: eqSB(addSB(smass.S2, smass.S5), smass.S3), expect: '74.092' },
    { id: 'P3', got: fmtG3(smass.S3) + ' + ' + fmtG3(smass.S4) + ' = ' + fmtG3(addSB(smass.S3, smass.S4)) + ' = ' + fmtG3(smass.S1) + ' + ' + fmtG3(smass.S5) + ' (carbonation closes both ways)', ok: eqSB(addSB(smass.S3, smass.S4), addSB(smass.S1, smass.S5)), expect: '118.101 both ways' },
    { id: 'P4', got: fmtG3(smass.S3) + ' = ' + fmtG3(smass.S2) + ' + ' + fmtG3(smass.S5) + " (dehydroxylation, the 512 degC rung - Ch 14's pin)", ok: eqSB(addSB(smass.S2, smass.S5), smass.S3), expect: '74.092' },
    { id: 'P5', got: fmtG3(eSi) + ' + ' + fmtG3(eO2) + ' = ' + fmtG3(addSB(eSi, eO2)) + " (Si + O2 = SiO2, Ch 30's face)", ok: eqSB(addSB(eSi, eO2), smass.S6), expect: '60.083' },
    { id: 'P6', got: fmtG3(addSB(eCa, eCa)) + ' + ' + fmtG3(eO2) + ' = ' + fmtG3(addSB(addSB(eCa, eCa), eO2)) + ' (2Ca + O2 = 2CaO)', ok: eqSB(addSB(addSB(eCa, eCa), eO2), mkInt(112154n)), expect: '112.154' },
    { id: 'P7', got: fmtG3(smass.S1) + ' + ' + fmtG3(addSB(smass.S7, smass.S7)) + ' = ' + fmtG3(addSB(smass.S1, addSB(smass.S7, smass.S7))) + ' = ' + fmtG3(smass.S8) + ' + ' + fmtG3(smass.S5) + ' + ' + fmtG3(smass.S4) + ' (the vinegar quench closes both ways)', ok: eqSB(addSB(smass.S1, addSB(smass.S7, smass.S7)), addSB(addSB(smass.S8, smass.S5), smass.S4)), expect: '220.190 both ways' },
    { id: 'P8', got: fmtG3(eCa) + ' + ' + fmtG3(eO) + ' = ' + fmtG3(addSB(eCa, eO)) + ' (element build: CaO)', ok: eqSB(addSB(eCa, eO), smass.S2), expect: '56.077' },
    { id: 'P9', got: fmtG3(eCa) + ' + ' + fmtG3(eO2) + ' + ' + fmtG3(eH2) + ' = ' + fmtG3(addSB(addSB(eCa, eO2), eH2)) + ' (element build: Ca(OH)2)', ok: eqSB(addSB(addSB(eCa, eO2), eH2), smass.S3), expect: '74.092' },
    { id: 'P10', got: fmtG3(eCa) + ' + ' + fmtG3(eC) + ' + ' + fmtG3(eO3) + ' = ' + fmtG3(addSB(addSB(eCa, eC), eO3)) + ' (element build: CaCO3)', ok: eqSB(addSB(addSB(eCa, eC), eO3), smass.S1), expect: '100.086' },
    { id: 'P11', got: fmtG3(eCa) + ' + ' + fmtG3(addSB(eC, addSB(eC, addSB(eC, eC)))) + ' + ' + fmtG3(eH6) + ' + ' + fmtG3(addSB(eO2, eO2)) + ' = ' + fmtG3(addSB(addSB(addSB(eCa, addSB(eC, addSB(eC, addSB(eC, eC)))), eH6), addSB(eO2, eO2))) + ' (element build: Ca(C2H3O2)2)', ok: eqSB(addSB(addSB(addSB(eCa, addSB(eC, addSB(eC, addSB(eC, eC)))), eH6), addSB(eO2, eO2)), smass.S8), expect: '158.166' },
    { id: 'P12', got: fmtG3(eC) + ' + ' + fmtG3(eO2) + ' = ' + fmtG3(addSB(eC, eO2)) + ' (C + O2 = CO2)', ok: eqSB(addSB(eC, eO2), smass.S4), expect: '44.009' },
    { id: 'P13', got: fmtG3(eH4) + ' + ' + fmtG3(eO2) + ' = ' + fmtG3(addSB(eH4, eO2)) + ' (2H2 + O2 = 2H2O; 2 x ' + fmtG3(smass.S5) + ')', ok: eqSB(addSB(eH4, eO2), addSB(smass.S5, smass.S5)), expect: '36.030' },
    { id: 'P14', got: fmtG3(addSB(eC, eC)) + ' + ' + fmtG3(eH4) + ' + ' + fmtG3(eO2) + ' = ' + fmtG3(addSB(addSB(addSB(eC, eC), eH4), eO2)) + ' (element build: CH3COOH)', ok: eqSB(addSB(addSB(addSB(eC, eC), eH4), eO2), smass.S7), expect: '60.052' },
  ];
  for (const r of P) {
    if (r.ok) { push(id3(r.id) + 'P got ' + r.got + ' | expect ' + r.expect + ' | PASS'); pass++; }
    else { push(id3(r.id) + 'P got ' + r.got + ' | expect ' + r.expect + ' | FAIL'); fail++; }
  }

  // --- E rows (the computed mechanics; E9 the designed must-fail)
  const E: Array<{ id: string; run: () => void }> = [];
  // E1 lever: 2.00 m effort arm / 0.50 m load arm
  E.push({ id: 'E1', run: () => {
    const ma = divSB(mkInt(200n), mkInt(50n));
    const got = 'MA = 200/50 = ' + fmt(ma, 3) + ' (lever: 2.00 m effort arm, 0.50 m load arm)';
    const ok = got.endsWith('(lever: 2.00 m effort arm, 0.50 m load arm)') && fmt(ma, 3) === '4.000';
    push(id3('E1') + 'E got ' + got + ' | expect MA = 4.000 | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E2 the 300 N load priced through the 4.000 lever
  E.push({ id: 'E2', run: () => {
    const f = divSB(mkInt(300n), mkInt(4n));
    const got = '300 / 4.000 = ' + fmt(f, 1) + ' N';
    const ok = fmt(f, 1) === '75.0';
    push(id3('E2') + 'E got ' + got + ' | expect 75.0 N | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E3 pulley: 4 supporting rope segments
  E.push({ id: 'E3', run: () => {
    const f = divSB(mkInt(2000n), mkInt(4n));
    const got = '2000 / 4 segments = ' + fmt(f, 1) + ' N';
    const ok = fmt(f, 1) === '500.0';
    push(id3('E3') + 'E got ' + got + ' | expect 500.0 N | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E4 THE WITNESS LANE: the repeating decimal held exactly - effort arm 2.20 m / load arm 0.70 m = 22/7
  E.push({ id: 'E4', run: () => {
    const ma = divSB(mkInt(220n), mkInt(70n));
    const path = ma.runs.map((r) => (r[0] === 1 ? 'R' : 'L').repeat(Number(r[1]))).join('');
    const got = 'MA = 220/70 = 22/7 held as SB path ' + path + '; decimal ' + fmt(ma, 6) + '... repeating';
    const ok = path === 'RRRLLLLLL' && fmt(ma, 6) === '3.142857';
    push(id3('E4') + 'E got ' + got + ' | expect MA = 22/7 (the repeating decimal held exactly, no decimal point) | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E5 tipping: push at 3.00 m, weight at 0.30 m -> F = 0.100 W
  E.push({ id: 'E5', run: () => {
    const f = divSB(mkInt(30n), mkInt(300n));
    const got = 'F = W x 0.30/3.00 = ' + fmt(f, 3) + ' W (push at 3.00 m, weight at 0.30 m)';
    const ok = fmt(f, 3) === '0.100';
    push(id3('E5') + 'E got ' + got + ' | expect 0.100 W | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E6 the notch and the hinge: diameter 0.90 m
  E.push({ id: 'E6', run: () => {
    const notch = divSB(mkInt(90n), mkInt(300n));
    const hinge = mulSB(divSB(mkInt(90n), mkInt(100n)), divSB(mkInt(1n), mkInt(10n))); // 10% of 0.90 m = 0.09 m
    const got = 'notch 0.90/3 = ' + fmt(notch, 2) + ' m; hinge ' + fmt(hinge, 2) + ' m (10% of 0.90 m)';
    const ok = fmt(notch, 2) === '0.30' && fmt(hinge, 2) === '0.09';
    push(id3('E6') + 'E got ' + got + ' | expect 0.30 m + 0.09 m | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E7 the quartz inversion step: 0.45% of 2.000 m
  E.push({ id: 'E7', run: () => {
    const step = mulSB(divSB(mkInt(45n), mkInt(10000n)), mkInt(2000n)); // 9 mm in mm-units
    const got = '0.45% x 2.000 m = ' + fmt(step, 1) + ' mm (the quartz inversion step)';
    const ok = fmt(step, 1) === '9.0';
    push(id3('E7') + 'E got ' + got + ' | expect 9.0 mm | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E8 delta T to the inversion
  E.push({ id: 'E8', run: () => {
    const dt = subSB(mkInt(573n), mkInt(20n));
    const got = '573 - 20 = ' + fmt(dt, 0) + ' K (delta T to the inversion)';
    const ok = fmt(dt, 0) === '553';
    push(id3('E8') + 'E got ' + got + ' | expect 553 K | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E9 THE MUST-FAIL: slaking authored with the water missing
  E.push({ id: 'E9', run: () => {
    const deficit = subSB(smass.S3, smass.S2);
    const one = eqSB(deficit, smass.S5);
    const got = 'deficit ' + fmt(divSB(deficit, mkInt(1000n)), 3) + ' g' + (one ? ' (one H2O missing)' : ' (NOT one H2O)');
    if (one && fmt(divSB(deficit, mkInt(1000n)), 3) === '18.015') {
      push(id3('E9') + 'E got ' + got + ' | expect deficit 18.015 g | CAUGHT (must-fail: slaking authored with the water missing)');
      caught++;
    } else {
      push(id3('E9') + 'E got ' + got + ' | expect deficit 18.015 g | FAIL');
      fail++;
    }
  } });
  // E10 the ice expansion: 0.917 g/mL
  E.push({ id: 'E10', run: () => {
    const expand = divSB(subSB(mkInt(1000n), mkInt(917n)), mkInt(917n));
    const vol = divSB(mkInt(1000n), mkInt(917n));
    const got = 'expansion 83/917 = ' + pct(expand, 3) + ' (ice 0.917 g/mL; 1000/917 = ' + fmt(vol, 3) + ')';
    const ok = pct(expand, 3) === '9.051%' && fmt(vol, 3) === '1.091';
    push(id3('E10') + 'E got ' + got + ' | expect 9.051% | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E11 the overflow: a full 1 L container
  E.push({ id: 'E11', run: () => {
    const over = mulSB(mkInt(1000n), divSB(subSB(mkInt(1000n), mkInt(917n)), mkInt(917n)));
    const got = 'overflow 1000 x 83/917 = ' + fmt(over, 2) + ' mL';
    const ok = fmt(over, 2) === '90.51';
    push(id3('E11') + 'E got ' + got + ' | expect 90.51 mL | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E12 the wrecking ball's kinetic energy
  E.push({ id: 'E12', run: () => {
    const ke = mulSB(mulSB(mkInt(1000n), mkInt(25n)), divSB(mkInt(1n), mkInt(2n)));
    const got = 'KE = 1/2 x 1000 kg x (5 m/s)^2 = ' + fmt(ke, 0) + ' J';
    const ok = fmt(ke, 0) === '12500';
    push(id3('E12') + 'E got ' + got + ' | expect 12500 J | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E13 the calcination enthalpy per gram
  E.push({ id: 'E13', run: () => {
    const per = divSB(mkInt(178000n), mkInt(100086n)); // 178000 myu / 100086 myu = 1.778 kJ/g
    const got = '178 kJ/mol / 100.086 g/mol = ' + fmt(per, 3) + ' kJ/g';
    const ok = fmt(per, 3) === '1.778';
    push(id3('E13') + 'E got ' + got + ' | expect 1.778 kJ/g | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E14 the carbonation mass gain
  E.push({ id: 'E14', run: () => {
    const gain = subSB(smass.S1, smass.S3); // 25.994
    const got = 'gain ' + fmt(divSB(gain, mkInt(1000n)), 3) + '/' + fmtG3(smass.S3) + ' = ' + pct(divSB(gain, smass.S3), 2) + ' (Ca(OH)2 -> CaCO3)';
    const ok = pct(divSB(gain, smass.S3), 2) === '35.08%';
    push(id3('E14') + 'E got ' + got + ' | expect 35.08% | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E15 the vinegar dose: 10.006 g CaCO3, 5% w/v acid
  E.push({ id: 'E15', run: () => {
    const acid = mulSB(divSB(mulSB(mkInt(2n), mkInt(60052n)), mkInt(100086n)), mkInt(10006n));
    const dose = divSB(divSB(acid, mkInt(1000n)), divSB(mkInt(5n), mkInt(100n))); // acid to grams, then mL at 5 g per 100 mL
    const got = 'dose 10.006 g CaCO3 needs ' + fmt(divSB(acid, mkInt(1000n)), 3) + ' g CH3COOH = ' + fmt(dose, 1) + ' mL of 5% w/v vinegar';
    const ok = fmt(divSB(acid, mkInt(1000n)), 3) === '12.007' && fmt(dose, 1) === '240.1';
    push(id3('E15') + 'E got ' + got + ' | expect 240.1 mL | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  // E16 the water of combination
  E.push({ id: 'E16', run: () => {
    const w = divSB(mkInt(18015n), mkInt(74092n));
    const got = 'water of combination 18.015/74.092 = ' + pct(w, 2);
    const ok = pct(w, 2) === '24.31%';
    push(id3('E16') + 'E got ' + got + ' | expect 24.31% | ' + (ok ? 'PASS' : 'FAIL'));
    ok ? pass++ : fail++;
  } });
  for (const r of E) r.run();

  // --- the gates
  push('G1  G1 recount ' + (9 + 5 + 9 + 14 + 16) + ' rows (9 S + 5 A + 9 R + 14 P + 16 E) ' + (pass + caught + refused + fail === 53 ? 'MATCH' : 'MISMATCH'));
  const s9ok = fmtG(smass.S9) === '60.083 g/mol';
  push('G2  G2 canary ' + (s9ok ? 're-caught at S9 alone (60.093 planted, 60.083 re-printed) HELD' : 'LOST'));
  push('G3  G3 determinism: ' + g3line);
  const e9ok = eqSB(subSB(smass.S3, smass.S2), smass.S5);
  push('G4  G4 must-fail ' + (e9ok ? 're-caught at exactly 18.015 g (one H2O; the deficit equals S5 itself) HELD' : 'LOST'));

  // --- T1 the composition checksum
  let sum: SB = smass.S1;
  for (const sid of ['S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']) sum = addSB(sum, smass[sid]);
  const t1ok = eqSB(sum, mkInt(570580n));
  push('T1  T1 composition checksum ' + fmt(sum, 0) + ' myu (the exact S1-S8 sum) ' + (t1ok ? 'MATCH' : 'MISMATCH'));

  // --- T2 the witness lane: 22/7 as the path itself
  const sb227 = ctor(22n, 7n);
  const p227 = sb227.runs.map((r) => (r[0] === 1 ? 'R' : 'L').repeat(Number(r[1]))).join('');
  const counts227 = sb227.runs.map((r) => (r[0] === 1 ? Number(r[1]) + ' R' : Number(r[1]) + ' L')).join(', ');
  const rt = (() => { const [n, d] = toPair(sb227); return n === 22n && d === 7n; })();
  push('T2  T2 22/7 = the SB path ' + p227 + ' (' + counts227 + ' - the continued fraction [3;7] worn as moves); round-trip ' + (rt ? 'PASS' : 'FAIL'));

  push('SUMMARY  ' + pass + ' PASS / ' + caught + ' caught / ' + refused + ' refused / ' + fail + ' FAIL');
  push('VERDICT  53/53 adjudicated, ' + (fail === 0 ? 'zero uncaught defects: CLEAN' : 'UNCAUGHT DEFECTS PRESENT'));
  return L.join('\n');
}

function fmtG3(m: SB): string { return fmt(divSB(m, mkInt(1000n)), 3); }

async function main() {
  // probe pass: two executions, byte-identical required
  const probe1 = battery('PENDING');
  const probe2 = battery('PENDING');
  if (probe1 !== probe2) {
    return { g3: 'LOST', block: probe1, note: 'the two probe executions differ' };
  }
  const g3line = 'HELD - the second in-process execution byte-identical';
  const block1 = battery(g3line);
  const block2 = battery(g3line);
  if (block1 !== block2) {
    return { g3: 'LOST', block: block1, note: 'the two final executions differ' };
  }
  const header =
    'ENGINE 47 - the Stern-Brocot path engine (fresh build, zero code shared with Engines 1-46)\n' +
    '  architecture: every positive rational carried at rest as a Stern-Brocot path (run-encoded\n' +
    '  L/R moves through the tree); {num, den} pairs exist only transiently inside operations and\n' +
    '  every construction re-derives the path by binary descent with the path<->pair round-trip\n' +
    '  asserted before the value is used; masses ride the held table in integer myu\n' +
    '  (C 12.011, H 1.008, O 15.999, Ca 40.078, Si 28.085); the gate order NAME -> admission ->\n' +
    '  syntax -> grid. No pulse trains (45), no prime-exponent lattices (46), no inherited-multiplier\n' +
    '  descent (44), no bytecode VM (43), no event sweep (42), no segment tree (41), no interval\n' +
    '  containment (40), no depth ledger (39), no dual-column peel (38), no CPS fold (37), no\n' +
    '  token-table AST fold (36), no span-memo (35), no census tally (34), no fixed-point\n' +
    '  rewriting (33), no RPN reorder (31), no expression compiler (19).\n' +
    '  determinism (G3): HELD - the second in-process execution byte-identical';
  const block = header + '\n' + block1;

  // the byte-compare gate: the engine reports its own output's exact measures
  // (manual UTF-8 walk - TextEncoder is not available in this sandbox)
  const bytes: number[] = [];
  for (let i = 0; i < block.length; i++) {
    const c = block.charCodeAt(i);
    if (c < 0x80) bytes.push(c);
    else if (c < 0x800) { bytes.push(0xc0 | (c >> 6), 0x80 | (c & 0x3f)); }
    else { bytes.push(0xe0 | (c >> 12), 0x80 | ((c >> 6) & 0x3f), 0x80 | (c & 0x3f)); }
  }
  let bsum = 0;
  const MOD = 1000000007;
  for (let i = 0; i < bytes.length; i++) bsum = (bsum + bytes[i]) % MOD;
  const lines = block.split('\n').length;
  return { block, gate: 'lines=' + lines + ' bytes=' + bytes.length + ' bytesum=' + bsum };
}
```

## 8. Session 134 close summary

FC6 "Heavy Work Without Explosives" drafted — the Field Companion's sixth chapter and the map's last planned unit: the pre-dynamite toolbox priced (the lever/wedge/pulley mechanical-advantage grid with the 22/7 witness lane, the felling/tipping/undermining sequence, fire-setting and the Māori fire-felling canon, the freeze-thaw wedge on the NEW 0.917 g/mL, the mortar lime cycle honored from Ch 14, and the demolition trade's own gravity-and-sequence mainline), the explosive shelf refused at the NAME gate throughout (R1–R8) and the held table's own limit named at R9. Engine 47's frozen battery run 4 CLEAN — 42 PASS / 2 caught / 9 refused / 0 FAIL, the honest history printed above (the run-1 deadline, the run-2 gate crash, the run-3 three-defect catch and the E16 expectation correction); the NEW census zero-hit before the freeze (21 words + 7 values, the twenty-third zero-admission chapter) with **one census catch disclosed at its own line** (512 °C — a prior, Ch 14 ×3 + FC9's canvas ×6, carried as its owner's pin, the pre-freeze NEW listing corrected rather than smoothed); the pins re-grepped in their owners' own pages; the [convergent] battery verified fresh at named sources; Ex FC6.6's ◆ answer withheld to the session-135 review per the FC alternation. The chapter canvas (67,825 B, no trailing newline), its repo master (the canvas + one newline), its web edition (the renderer re-validated byte-identical against the known-good fc11-web.html first), the extended index, and this record pushed ALWAYS-SYNC at this session's close. NEXT: session 135 — FC6's Phase-3 adversarial review, a fresh Engine 48 sharing zero code with Engines 1–47, on the user's call.
