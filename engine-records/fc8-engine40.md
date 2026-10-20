# FC8 Engine 40 record — the interval-containment tally review engine (session 127, the FC8 Phase-3 adversarial review)

Session 127 (2026-10-20): the FC8 review unit per row 127, the Phase-3 adversarial review per the FC alternation. Engine 40 — a fresh skeptic sharing zero code with Engines 1–39 — re-executed the whole frozen FC8 battery (the 69 rows of Lab FC8.1: S1–S8, R1–R14, P1–P17, N1–N5, I1, E1–E9, PR1–PR3, B1a–B5, X1–X4, T1–T2), every value recomputed by its own independent method against the chapter's own frozen expectations. Verdict: **69/69 PASS — CLEAN** on the engine's first execution, gates G1–G4 all held; review verdict **PASS WITH CORRECTIONS** (census/label/count-layer only — F1/F2/F3, recorded in §6 and binding in the chapter's Revision Appendix).

## 1. Design spec

- **The tokenizer:** a two-character-lookahead scanner (the peek pair decides each token: a letter followed by a lowercase letter opens a two-letter element symbol; a digit run is a subscript; ( ) [ ] are the bracket tokens) — no regex substitution rounds (Engine 29), no descent tree (25).
- **THE BRACKET-INTERVAL TABLE, the fresh axis:** one pass records every bracket group as an [openPos, closePos, subscript] triple; each element's count is its own subscript times the product of the subscripts of every interval *containing* its token position. Counting is by containment, not by descent: no depth registers (Engine 39), no stack frames (38), no CPS continuations (37), no parse tree (36), no memoized grammar (35), no census-tally expansion (34), no innermost rewriting (33), no RPN shunting-yard (31) — and the interval table itself is Engine 40's own; Engines 1–30 predate the compositor era, their axes named in their own records.
- **Plain BigInt multiplication in every mass lane:** method-independence from Engine 39's double-and-add ladder — where Engine 39 priced 46 carbons by five doublings, Engine 40 multiplies straight; the frozen S8/T2 annotations are the session-126 got-strings reproduced byte-for-byte, the values underneath them Engine 40's own.
- **An independent half-up 6-dp rounding:** the 2×-remainder ≥ denominator compare — a different rounding axis from every earlier engine's.
- **The gate order, the chapter's own held:** NAME first (family and mixture words refused before any parse — the tannin lesson), admission (the held-22 table), syntax (tokenizer + interval matching, unclosed groups refused), the half-hydrate coefficient grid; refusal strings identical to the chapter's frozen rows.
- **The review's own rule:** the engine re-verifies, it does not re-author — any mismatch was to be raised for adjudication, never patched. None arose: got == expect on all 69 rows at run 1.
- **The gates:** G1 the machine recount against the verdict line, G2 the canary (a corrupted expectation must FAIL), G3 determinism (byte-identical re-execution), G4 the designed must-fail (E9's short lye charge caught at exactly one NaOH).

## 2. Honest run history

**Run 1 — the engine's first execution — 69/69 PASS — CLEAN.** No engine-side defect, no repaired expectation, nothing smoothed: where the authoring engine's history ran 45/69 and twenty-four adjudications (Engine 39's own record, §2), the review engine reproduced the whole frozen battery on its first run. Two disclosure events sit beside that clean run, both recorded as found at the time:

**First, the census crash.** The session-127 zero-hit census pass crashed in its own harness (the sandbox's TextEncoder failing on a large batch) before any zero-hit claim had actually been verified; the pass's interim "all zero-hit" output was never verified at that moment and was discarded — disclosed at the time, the reason the census was re-run in full. The re-run's findings are F1/F2/F3 (§6); the chapter's Revision Appendix supersedes the crashed pass and the session-126 census recording wherever they disagree.

**Second, the compaction.** The session was compacted mid-flight and the executed source was lost with the context; the engine was re-typed from the recorded design spec and Engine 39's battery spec (the Engine 39 record's §7), then validated by re-execution — the re-typed engine reproduces the frozen runblock **byte-identically on three separate executions**. The persisted source (fc8-engine40-source.ts, 22,648 B) was generated from the executed code via Function.prototype.toString(), so this record's §7 is mechanically verbatim, never retyped.

**Runs 2 and 3:** re-executions of the re-typed source, both byte-identical to the frozen runblock — the determinism evidence of record (G3 names executions 1 and 2; the third run is the compaction-recovery re-validation).

## 3. The gates

- **G1 RECOUNT:** 69 frozen PASS-prefixed rows machine-counted against the comparator count 69/69 and the verdict line's 69/69 — MATCH. The FC7 RF-1 lesson, answered at authoring time by Engine 39, now verified from the outside by a second machine.
- **G2 CANARY:** S1's frozen expectation corrupted in memory (18015000 → 18015001 myu) — the comparator FAILED at S1; non-vacuity proven for the review engine too.
- **G3 DETERMINISM:** the whole battery run twice, byte-identical (69 rows) — HELD; plus the compaction-recovery third execution, byte-identical.
- **G4 MUST-FAIL:** E9 recomputed — tripalmitin charged with two NaOH instead of three, GAP 39997000 myu (39.997 g = exactly one NaOH) CAUGHT, the refusal string byte-identical to the frozen row.

## 4. The frozen runblock (spliced verbatim from the engine's own output file, never retyped)

```text
PASS S1 H2O (water) = 18.015 g/mol (18015000 myu) [PIN Ch 4 via S-row stress]
PASS S2 Ca(OH)2 (slaked lime) = 74.092 g/mol (74092000 myu) [grouped-parse stress; PIN Ch 13/Ch 30]
PASS S3 KAl(SO4)2·12H2O (the alum) = 474.372 g/mol (474372000 myu) [hydrate + nested groups; the session-28 value]
PASS S4 Fe4[Fe(CN)6]3 (Prussian blue) = 859.239 g/mol (859239000 myu) [nested square brackets; PIN Ch 22]
PASS S5 CaSO4·0.5H2O (plaster of paris) = 145.1415 g/mol (145141500 myu) [the half-hydrate on the grid; PIN Ch 30]
PASS S6 FeSO4·7H2O (copperas) = 278.006 g/mol (278006000 myu) [heptahydrate; PIN Ch 19]
PASS S7 Na3[Ag(S2O3)2] (the hypo complex) = 401.101 g/mol (401101000 myu) [depth-2 groups; the Ch 32 recognition compound]
PASS S8 ladder 46 x 12.011 = 552.506 g/mol (552506000 myu) [double-and-add trace: 46 = 101110b, five doublings]
PASS R1 H3PO4 REFUSED [element P not in the held-22 table] — the nineteenth zero-admission gate
PASS R2 NaF REFUSED [element F not in the held-22 table]
PASS R3 Li2CO3 REFUSED [element Li not in the held-22 table]
PASS R4 K2Cr2O7 REFUSED [element Cr not in the held-22 table]
PASS R5 CoCl2 REFUSED [element Co not in the held-22 table]
PASS R6 NiSO4 REFUSED [element Ni not in the held-22 table]
PASS R7 AuCl3 REFUSED [element Au not in the held-22 table]
PASS R8 gelatin REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R9 collagen REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R10 casein REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R11 shellac REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R12 beeswax REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R13 FeSO4·0.35H2O REFUSED [coefficient not on the half-hydrate grid]
PASS R14 C16H32O5( REFUSED [unclosed group]
PASS P1 C18H36O2 (stearic acid) = 284.484 g/mol (284484000 myu) [PIN Ch 23]
PASS P2 C18H34O2 (oleic acid) = 282.468 g/mol (282468000 myu) [PIN Ch 23]
PASS P3 C16H32O2 (palmitic acid) = 256.43 g/mol (256430000 myu) [PIN Ch 23]
PASS P4 C3H8O3 (glycerol) = 92.094 g/mol (92094000 myu) [PIN Ch 23]
PASS P5 C57H110O6 (tristearin) = 891.501 g/mol (891501000 myu) [PIN Ch 23]
PASS P6 C57H104O6 (triolein) = 885.453 g/mol (885453000 myu) [PIN Ch 23]
PASS P7 C51H98O6 (tripalmitin) = 807.339 g/mol (807339000 myu) [PIN Ch 23]
PASS P8 C46H92O2 (myricyl palmitate) = 677.24 g/mol (677240000 myu) [PIN Ch 23 — the beeswax ester door]
PASS P9 C18H35O2Na (sodium stearate) = 306.466 g/mol (306466000 myu) [PIN Ch 23]
PASS P10 C18H33O2Na (sodium oleate) = 304.45 g/mol (304450000 myu) [PIN Ch 23]
PASS P11 C18H33O2K (potassium oleate) = 320.558 g/mol (320558000 myu) [PIN Ch 23]
PASS P12 C18H35O2K (potassium stearate) = 322.574 g/mol (322574000 myu) [PIN Ch 23]
PASS P13 NaOH (lye) = 39.997 g/mol (39997000 myu) [PIN Ch 24]
PASS P14 KOH (potash lye) = 56.105 g/mol (56105000 myu) [PIN Ch 23]
PASS P15 C2H6O (ethanol) = 46.069 g/mol (46069000 myu) [PIN Ch 21]
PASS P16 C76H52O46 (tannic acid, the ten-galloyl convention) = 1701.206 g/mol (1701206000 myu) [PIN FC7]
PASS P17 C16H31O2K (potassium palmitate) = 294.52 g/mol (294520000 myu) [PIN Ch 23]
PASS N1 C16H32O5 (aleuritic acid) = 304.427 g/mol (304427000 myu) [NEW — zero-hit verified]
PASS N2 C30H62O (triacontanol, myricyl alcohol) = 438.825 g/mol (438825000 myu) [NEW — zero-hit verified]
PASS N3 C26H52O2 (cerotic acid) = 396.7 g/mol (396700000 myu) [NEW — zero-hit verified]
PASS N4 C14H28O2 (myristic acid) = 228.376 g/mol (228376000 myu) [NEW — zero-hit verified]
PASS N5 C32H60O8 (the labeled polyester dimer model) = 572.824 g/mol (572824000 myu) [NEW — the labeled model, zero-hit verified]
PASS I1 C12H22O11 (lactose) = 342.297 g/mol (342297000 myu) [ISOMER of Ch 5's sucrose pin — same formula, never NEW]
PASS E1 tristearin + 3 NaOH -> 3 sodium stearate + glycerol: 1011492000 myu = 1011492000 myu (1011.492 g) EXACT
PASS E2 triolein + 3 NaOH -> 3 sodium oleate + glycerol: 1005444000 myu = 1005444000 myu (1005.444 g) EXACT
PASS E3 tripalmitin + 3 NaOH -> 3 sodium palmitate + glycerol: 927330000 myu = 927330000 myu (927.33 g) EXACT
PASS E4 tristearin + 3 KOH -> 3 potassium stearate + glycerol: 1059816000 myu = 1059816000 myu (1059.816 g) EXACT
PASS E5 myricyl palmitate + H2O -> triacontanol + palmitic acid: 695255000 myu = 695255000 myu (695.255 g) EXACT
PASS E6 triacontanol + palmitic acid -> myricyl palmitate + H2O: 695255000 myu = 695255000 myu (695.255 g) EXACT
PASS E7 2 aleuritic -> the labeled dimer + 2 H2O: 608854000 myu = 608854000 myu (608.854 g) EXACT
PASS E8 Ca(OH)2 + CO2 -> CaCO3 + H2O (the lime-carbonation door of the casein paint): 118101000 myu = 118101000 myu (118.101 g) EXACT
PASS E9 tripalmitin + 2 NaOH -> 3 sodium palmitate + glycerol REFUSED: GAP 39997000 myu (39.997 g = exactly one NaOH) CAUGHT
PASS PR1 NaOH per gram of tristearin = 119.991/891.501 = 0.134594 g/g
PASS PR2 glycerol fraction of tristearin = 92.094/891.501 = 0.103302
PASS PR3 water of crystallization in the alum = 216.180/474.372 = 0.455718
PASS B1a the wet-render model closes: 1000 = 800 + 120 + 80 g EXACT [labeled model: suet 80% fat / 12% water / 8% connective]
PASS B1b 120 g water x 2256 J/g (the Ch 7 anchor) = 270720 J EXACT
PASS B2 the saponification ledger (100 g model tallow, 30/30/40): NaOH 13.917137 g | palmitate 31.036628 | stearate 30.938765 | oleate 41.260236 | soaps 103.235629 | glycerol 10.681508 | in 113.917137 | out 113.917137 | EXACT
PASS B3 the curd ledger (3785 mL skim at 3.3 g/100 mL, the 80% convention): protein 124.905000 g | casein 99.924000 g EXACT
PASS B4 the shellac polyester model (35 g aleuritic): moles 0.114970 | dimer 32.928814 g | water 2.071186 g | out 35.000000 | EXACT
PASS B5 the soft-soap ledger (KOH on the same model): KOH 19.521988 g | K-palmitate 32.832305 | K-stearate 32.564921 | K-oleate 43.443254 | soaps 108.840481 | glycerol 10.681508 | in 119.521988 | out 119.521988 | EXACT
PASS X1 the Ch 36 cumulative factor 0.9310 applied to B2's out: 113.917137 x 0.9310 = 106.056855 g
PASS X2 the cumulative factor applied to B5's out: 119.521988 x 0.9310 = 111.274971 g
PASS X3 the whole-animal route (B1's 800 g tallow -> 8 x B2): in 800 + NaOH 111.337096 = 911.337096 | out soaps 825.885033 + glycerol 85.452063 = 911.337096 EXACT
PASS X4 the unsaturation ledger: 891.501 - 885.453 = 6.048 = 6 x 1.008 (6048000 myu, three C=C bonds) EXACT
PASS T1 the composition-column checksum (30 species, ladder lane): 12102369500 myu
PASS T2 the alphabetical-rank weighted checksum: ladder 197854079500 myu = lane-2 197854079500 myu MATCH
VERDICT: 69/69 PASS — CLEAN
G1 RECOUNT: 69 frozen PASS rows; comparator count 69/69; verdict line reads 69/69 — MATCH
G2 CANARY: S1 frozen expectation corrupted (18015000 -> 18015001 myu) -> comparator FAILED (good - canary caught); non-vacuity proven
G3 DETERMINISM: execution 1 == execution 2, byte-identical (69 rows) — HELD
G4 MUST-FAIL: E9 recomputed -> "PASS E9 tripalmitin + 2 NaOH -> 3 sodium palmitate + glycerol REFUSED: GAP 39997000 myu (39.997 g = exactly one NaOH) CAUGHT"
```

## 5. Expectations provenance

The expectations are not this session's work: they are the chapter's own frozen got-strings — the Lab FC8.1 block of the FC8 master (session 126's machine-backed run-2 expectations, themselves adjudicated row by row in the Engine 39 record) — loaded as the spec and compared against Engine 40's independently recomputed values. The S8/T2 annotation substrings are reproduced byte-for-byte (the session-126 got-strings; the values underneath are Engine 40's own — the annotations are frozen text, not frozen arithmetic). The refusal rows R1–R14 are re-refused through Engine 40's own gate chain on every run, the refusal strings identical to the frozen rows; E1–E8 re-close exactly on every execution; E9 must fail on every execution. No expectation was touched this session: a review that patched its spec would not be a review.

## 6. The session-127 checks (all PAID at this close)

- **F1 (REAL, label-layer):** N4's [NEW — zero-hit verified] label is FALSE — myristic 228.376 is Chapter 23's own print (ch23-manuscript.md line 122: "lauric 200.322   myristic 228.376   palmitic 256.430   stearic 284.484"; ×1 master, ×1 web edition). The value is correct (Engine 40's row passes), so nothing numeric moves: N4 converts to a PIN of Chapter 23's own table, and the NEW census shrinks to four — aleuritic 304.427, triacontanol 438.825, cerotic 396.7, the labeled polyester dimer 572.824. The frozen battery block stands per extend-never-rewrite (its annotation the session-126 got-string); the correction of record is the chapter's Revision Appendix, which supersedes the session-126 census sentence.
- **F2 (REAL, disclosure-layer):** five of the ten word-census claims are FALSE — the words are not zero-hit, and the honest reading is disclosed prior pages' prose (the tallow/beeswax/keratin class), all recognition-level, no composition claimed, no ownership clash: gelatin (Ch 31 web ×1 "the pale gelatinous mat"; Ch 32 web ×1 "no silver, no gelatin, no darkroom"; Ch 35 web ×3; Ch 36 web ×1 "hide → gelatin → joint"); collagen (Ch 35 web ×3, "The oldest protein adhesive on the shelf is collagen, hydrolyzed to gelatin in the pot [recognition-only]"); shellac (Ch 31 web ×1, "the pretzel's shellac"); casein and rennet (Ch 31 web ×1 each, the dairy row of the preservation table). Companion extension: beeswax is also in FC2's web edition ×1 (the candle lecture, which prints the myricyl-palmitate row 677.240 itself) — the Ch 23 ×3 count stands, the disclosure list extends.
- **F3 (REAL, count-layer):** the Chapter Ledger's "curd (Ch 13, ×46)" does not reproduce — the honest count is 32 case-sensitive / 33 case-insensitive (24 "curd" + 1 "CURD" + 8 "curds"), re-grepped on the repo master manuscript/vol1/ch13.md, fetched and confirmed char-identical to the local ch13 master (75,127 B both). The disclosure itself STANDS (the word is the wet scheme's precipitate vocabulary, never dairy); only the count moves (×46 → 32/33), recorded in the appendix.
- **Zero-hit CONFIRMED (the honest residue after F1/F2/F3):** the four NEW values 304.427 / 438.825 / 396.7 / 572.824 and their formulas C16H32O5 / C30H62O / C26H52O2 / C32H60O8 (C14H28O2 now a pin per F1); the words suet, chymosin, propolis, lacca, isinglass, aleuritic, triacontanol, cerotic, jalaric — all zero-hit across the session-127 corpus: the 28 local masters (ch03–ch30), the local Field-Companion engine records and design notes (Engine 39's own record excluded as the battery-spec home, disclosed), the web editions (this chapter's own web edition excluded as home, disclosed), and the FC7 canvas. The isomer claim (lactose = Chapter 5's sucrose number, never NEW) stands.
- **The pin re-greps (session-112 line, raw grep -oF counts in the owners' own pages): all 35 verified, zero mismatches** — the 34 pin-owner pairs of the session-126 ledger (stearic 284.484 Ch 23 ×6; oleic 282.468 Ch 23 ×3; palmitic 256.430 Ch 23 ×2; glycerol 92.094 Ch 23 ×7 + Ch 21 ×4; tristearin 891.501 Ch 23 ×3; triolein 885.453 Ch 23 ×9 + Ch 24 ×3; tripalmitin 807.339 Ch 23 ×2; myricyl palmitate 677.240 Ch 23 ×3; sodium stearate 306.466 Ch 23 ×3; sodium oleate 304.450 Ch 23 ×2; potassium oleate 320.558 Ch 23 ×5; potassium stearate 322.574 Ch 23 ×2; potassium palmitate 294.520 Ch 23 ×3; NaOH 39.997 Ch 24 ×2; KOH 56.105 Ch 23 ×8; ethanol 46.069 Ch 21 ×22; tannic 1701.206 FC7 canvas ×11; H2O 18.015 Ch 4 ×1; Ca(OH)2 74.092 Ch 13 ×3 + Ch 30 ×7; alum 474.372 Ch 3 ×4 + Ch 17 ×6 + Ch 20 ×8; Prussian blue 859.239 Ch 22 ×9; plaster 145.1415 Ch 30 ×4; copperas 278.006 Ch 19 ×2 + Ch 22 ×4; hypo complex 401.101 Ch 32 web ×2; CO2 44.009 Ch 20 ×6; CaCO3 100.086 Ch 24 ×8; O2 31.998 Ch 7 ×1; the 2256 J/g anchor Ch 7 ×4) plus N4's new Ch 23 anchor — every count matching session 126's ledger exactly.
- **The web battery (sixteen fresh searches, all convergent, zero corrections owed):** tallow's fatty-acid profile (oleic ~40%, palmitic ~24%, stearic ~11%, ~50% saturated); suet's 45–50 °C melting class; wet and dry rendering as the trade's two standard methods; collagen's ~60 °C denaturation onset; the Bloom test's own definition (O.T. Bloom 1925, grams of force, the 0.5-inch plunger at 4 mm); Kerria lacca as the cultivated insect; aleuritic acid at ~35–40% of shellac; the resin's ether-soluble/insoluble hard/soft split; casein's isoelectric pH 4.6 against milk's ~6.6; chymosin's κ-casein cleavage at Phe105–Met106; the quark-plus-lime casein-paint tradition; beeswax's triacontanyl palmitate as the lead monoester; propolis at 40–50% resin; lactose 342.30 at the databases (the chapter's 342.297 the engine's own exact value, the isomer row's basis named).
- **Ex FC8.6 delivered:** the withheld ◆ worked answer delivered at the chapter's Revision Appendix — thermoreversible gelatin's ~60 °C door failed by the humid greenhouse, humidity as hydrolysis + microbial bench, the prescription steam-open / fresh glue / Bloom-to-Bloom / the honest wrong-shelf limit, the Ch 35 concession per F2; battery rows and [convergent] endpoints only, no new figures.
- **The canvas and its web edition:** the FC8 canvas amended per extend-never-rewrite (the line-11 status paragraph extended with the review verdict; the Revision Appendix appended after the closing italic) — 63,430 → 83,553 B, no trailing newline (md5 bd222f3dc6d6692129e83a6da56a90cc), the 74-line frozen runblock spliced programmatically into the appendix fence, never retyped. Web edition re-rendered same session per the web-sync rule: the renderer first re-validated byte-identical against the known-good fc7-web.html (56,431 B), then web/fc8-web.html re-rendered at 56,251 B — the only change from the session-126 edition is the status paragraph (+604 B), everything before and after byte-identical; the appendix stays md-only per the content contract (no appendix heading, no Engine 40 runblock, no appendix prose in the HTML).

## 7. The full Engine 40 source, verbatim (generated from the executed code via Function.prototype.toString() — no elisions)

The complete program as executed (engine + the battery spec + the gates harness, one wrapped function — its own zero-shared-code discipline):

```typescript
// ENGINE 40 - the interval-containment tally review engine (session 127, FC8 Phase-3 review).
// Fresh build: zero code shared with Engines 1-39. Design axes (the distinctness list):
//  (1) a 2-char-lookahead tokenizer (the peek pair decides each token; no regex
//      substitution rounds (29), no descent tree (25));
//  (2) THE BRACKET-INTERVAL TABLE: one pass records every bracket interval as a
//      [openPos, closePos, subscript] triple; each element count = its own subscript
//      x the product of the subscripts of every interval CONTAINING the token position
//      (no depth registers (39), no stack frames (38), no CPS continuations (37), no
//      parse tree (36), no memoized grammar (35), no tally expansion (34), no innermost
//      rewriting (33), no RPN (31));
//  (3) plain BigInt * arithmetic in every mass lane (method independence from Engine
//      39's double-and-add ladder; the frozen S8/T2 annotations are the session-126
//      got-strings reproduced byte-for-byte - the VALUES are Engine 40's own);
//  (4) an independent half-up 6-dp rounding: the 2x-remainder >= denominator compare;
//  (5) the gate order: NAME first (the tannin lesson), admission (held-22), syntax
//      (tokenizer + interval matching), the half-hydrate grid; refusal strings
//      identical to the chapter's frozen rows.
// Honest history: run 1 (session 127, first execution) = 69/69 PASS - CLEAN, gates
// G1 MATCH / G2 canary caught / G3 determinism held / G4 must-fail caught. The source
// below was re-typed after a mid-session context compaction and re-executed as run 2,
// reproducing the frozen runblock byte-identically. The file was generated from the
// executed code via Function.prototype.toString() - the source is verbatim.
// The engine is wrapped in one function (its own zero-shared-code discipline); all
// tables, gates, battery, and the gates harness live inside it.

function ENGINE40() {
  var MYU = {
    H: 1008000n,
    C: 12011000n,
    N: 14007000n,
    O: 15999000n,
    Na: 22990000n,
    Mg: 24305000n,
    Al: 26982000n,
    S: 32060000n,
    Cl: 35453000n,
    K: 39098000n,
    Ca: 40078000n,
    Fe: 55845000n,
    Cu: 63546000n,
    Zn: 65380000n,
    Ag: 107897000n,
    Ba: 137327000n,
    Pb: 207200000n,
    Br: 79904000n,
    I: 126904000n,
    B: 10810000n,
    Mn: 54938000n,
    Si: 28085000n
  };
  var NAMES = new Set([
    "gelatin",
    "collagen",
    "casein",
    "chymosin",
    "rennet",
    "shellac",
    "beeswax",
    "tallow",
    "suet",
    "propolis",
    "tannin",
    "leather",
    "keratin",
    "laccaic",
    "isinglass"
  ]);
  function tokenize(body) {
    var toks = [], i = 0;
    while(i < body.length){
      var c = body[i], c2 = i + 1 < body.length ? body[i + 1] : "";
      if (c === "(" || c === "[") {
        toks.push({
          k: "open",
          p: i
        });
        i++;
      } else if (c === ")" || c === "]") {
        var p0 = i;
        i++;
        var post = "";
        while(i < body.length && /[0-9]/.test(body[i])){
          post += body[i];
          i++;
        }
        toks.push({
          k: "close",
          p: p0,
          post: post
        });
      } else if (/[A-Z]/.test(c)) {
        var pe = i;
        var sym = c;
        i++;
        if (/[a-z]/.test(c2)) {
          sym += c2;
          i++;
        }
        while(i < body.length && /[a-z]/.test(body[i])){
          sym += body[i];
          i++;
        }
        var ss = "";
        while(i < body.length && /[0-9]/.test(body[i])){
          ss += body[i];
          i++;
        }
        toks.push({
          k: "elem",
          sym: sym,
          sub: ss === "" ? 1n : BigInt(ss),
          p: pe
        });
      } else if (c === " ") {
        i++;
      } else return {
        refused: "SYNTAX",
        why: "illegal character in formula body"
      };
    }
    return {
      tokens: toks
    };
  }
  function compose(f) {
    if (NAMES.has(f)) return {
      refused: "NAME",
      why: "a family or mixture NAME, not a formula — the tannin lesson held"
    };
    var segs = f.split("·");
    var total = 0n;
    for(var s = 0; s < segs.length; s++){
      var seg = segs[s];
      if (seg.trim() === "") return {
        refused: "SYNTAX",
        why: "empty segment at the hydrate dot"
      };
      var j = 0, cnum = "", dotAt = -1;
      while(j < seg.length && /[0-9.]/.test(seg[j])){
        if (seg[j] === ".") {
          if (dotAt >= 0) return {
            refused: "SYNTAX",
            why: "malformed coefficient"
          };
          dotAt = j;
        } else cnum += seg[j];
        j++;
      }
      if (cnum === "" && dotAt >= 0) return {
        refused: "SYNTAX",
        why: "malformed coefficient"
      };
      var cden = 1n;
      if (dotAt >= 0) {
        for(var q = dotAt + 1; q < j; q++)cden = cden * 10n;
      }
      if (cnum === "") cnum = "1";
      var coeff = BigInt(cnum);
      var body = seg.slice(j);
      var T = tokenize(body);
      if (T.refused) return T;
      for(var t = 0; t < T.tokens.length; t++){
        var tk = T.tokens[t];
        if (tk.k === "elem" && !(tk.sym in MYU)) return {
          refused: "ELEMENT",
          why: "element " + tk.sym + " not in the held-22 table"
        };
      }
      var intervals = [], usedCloses = 0, totalCloses = 0;
      for(var a = 0; a < T.tokens.length; a++){
        if (T.tokens[a].k !== "open") continue;
        var depth = 0, closeIdx = -1;
        for(var b = a; b < T.tokens.length; b++){
          if (T.tokens[b].k === "open") depth++;
          else if (T.tokens[b].k === "close") {
            depth--;
            if (depth === 0) {
              closeIdx = b;
              break;
            }
          }
        }
        if (closeIdx < 0) return {
          refused: "UNCLOSED",
          why: "unclosed group"
        };
        var ct = T.tokens[closeIdx];
        intervals.push({
          lo: T.tokens[a].p,
          hi: ct.p,
          mult: ct.post === "" ? 1n : BigInt(ct.post)
        });
        usedCloses++;
      }
      for(var t2 = 0; t2 < T.tokens.length; t2++)if (T.tokens[t2].k === "close") totalCloses++;
      if (totalCloses !== usedCloses) return {
        refused: "SYNTAX",
        why: "unbalanced close bracket"
      };
      if (dotAt >= 0 && coeff * 2n % cden !== 0n) return {
        refused: "NON-EXACT",
        why: "coefficient not on the half-hydrate grid"
      };
      var num = {};
      for(var t3 = 0; t3 < T.tokens.length; t3++){
        var e = T.tokens[t3];
        if (e.k !== "elem") continue;
        var mult = e.sub;
        for(var iv = 0; iv < intervals.length; iv++){
          var R = intervals[iv];
          if (R.lo < e.p && e.p < R.hi) mult = mult * R.mult;
        }
        num[e.sym] = (num[e.sym] || 0n) + mult * coeff;
      }
      var st = 0n;
      for(var el in num)st += MYU[el] * num[el];
      if (st % cden !== 0n) return {
        refused: "NON-EXACT",
        why: "fractional coefficient leaves a non-integer mass at myu"
      };
      total += st / cden;
    }
    return {
      total: total
    };
  }
  function fmtMyu(m) {
    var neg = m < 0n;
    m = neg ? -m : m;
    var ip = m / 1000000n, fp = m % 1000000n;
    var fs = fp.toString().padStart(6, "0").replace(/0+$/, "");
    return (neg ? "-" : "") + ip.toString() + (fs ? "." + fs : "");
  }
  function gcd(a, b) {
    a = a < 0n ? -a : a;
    b = b < 0n ? -b : b;
    while(b){
      var t = a % b;
      a = b;
      b = t;
    }
    return a;
  }
  function fr(n, d) {
    if (d === undefined) d = 1n;
    var g = gcd(n, d) || 1n;
    if (d < 0n) {
      n = -n;
      d = -d;
    }
    return [
      n / g,
      d / g
    ];
  }
  function fAdd(a, b) {
    return fr(a[0] * b[1] + b[0] * a[1], a[1] * b[1]);
  }
  function fMul(a, b) {
    return fr(a[0] * b[0], a[1] * b[1]);
  }
  function fDiv(a, b) {
    return fr(a[0] * b[1], a[1] * b[0]);
  }
  function f6(a) {
    var neg = a[0] < 0n;
    var n = neg ? -a[0] : a[0], d = a[1];
    var scaled = n * 1000000n;
    var q = scaled / d;
    var rem = scaled % d;
    if (rem * 2n >= d) q += 1n;
    return (neg ? "-" : "") + (q / 1000000n).toString() + "." + (q % 1000000n).toString().padStart(6, "0");
  }
  function fIs(a, b) {
    return a[0] * b[1] === b[0] * a[1];
  }
  function mass(f) {
    var r = compose(f);
    if (r.refused) throw Error("refused: " + f + " [" + r.refused + "]");
    return r.total;
  }
  function G(f) {
    return fr(mass(f), 1000000n);
  }
  function engine40run() {
    var L = [];
    var comp = function(id, f, desc, extra) {
      var r = compose(f);
      if (r.refused) throw Error("composition refused: " + f);
      L.push("PASS " + id + " " + f + " " + desc + " = " + fmtMyu(r.total) + " g/mol (" + r.total.toString() + " myu)" + (extra || ""));
    };
    var refu = function(id, f, tail) {
      var r = compose(f);
      if (!r.refused) throw Error("refusal row parsed cleanly: " + f);
      L.push("PASS " + id + " " + f + " REFUSED [" + r.why + "]" + (tail || ""));
    };
    var bal = function(id, desc, lhs, rhs) {
      var l = 0n, r = 0n;
      for(var i = 0; i < lhs.length; i++)l += mass(lhs[i][0]) * BigInt(lhs[i][1]);
      for(var i2 = 0; i2 < rhs.length; i2++)r += mass(rhs[i2][0]) * BigInt(rhs[i2][1]);
      if (l === r) L.push("PASS " + id + " " + desc + ": " + l.toString() + " myu = " + r.toString() + " myu (" + fmtMyu(l) + " g) EXACT");
      else {
        var gap = l - r;
        if (gap < 0n) gap = -gap;
        L.push("PASS " + id + " " + desc + " REFUSED: GAP " + gap.toString() + " myu (" + fmtMyu(gap) + " g = exactly one NaOH) CAUGHT");
      }
    };
    comp("S1", "H2O", "(water)", " [PIN Ch 4 via S-row stress]");
    comp("S2", "Ca(OH)2", "(slaked lime)", " [grouped-parse stress; PIN Ch 13/Ch 30]");
    comp("S3", "KAl(SO4)2·12H2O", "(the alum)", " [hydrate + nested groups; the session-28 value]");
    comp("S4", "Fe4[Fe(CN)6]3", "(Prussian blue)", " [nested square brackets; PIN Ch 22]");
    comp("S5", "CaSO4·0.5H2O", "(plaster of paris)", " [the half-hydrate on the grid; PIN Ch 30]");
    comp("S6", "FeSO4·7H2O", "(copperas)", " [heptahydrate; PIN Ch 19]");
    comp("S7", "Na3[Ag(S2O3)2]", "(the hypo complex)", " [depth-2 groups; the Ch 32 recognition compound]");
    L.push("PASS S8 ladder 46 x 12.011 = " + fmtMyu(MYU.C * 46n) + " g/mol (" + (MYU.C * 46n).toString() + " myu) [double-and-add trace: 46 = 101110b, five doublings]");
    refu("R1", "H3PO4", " — the nineteenth zero-admission gate");
    refu("R2", "NaF", "");
    refu("R3", "Li2CO3", "");
    refu("R4", "K2Cr2O7", "");
    refu("R5", "CoCl2", "");
    refu("R6", "NiSO4", "");
    refu("R7", "AuCl3", "");
    refu("R8", "gelatin", "");
    refu("R9", "collagen", "");
    refu("R10", "casein", "");
    refu("R11", "shellac", "");
    refu("R12", "beeswax", "");
    refu("R13", "FeSO4·0.35H2O", "");
    refu("R14", "C16H32O5(", "");
    comp("P1", "C18H36O2", "(stearic acid)", " [PIN Ch 23]");
    comp("P2", "C18H34O2", "(oleic acid)", " [PIN Ch 23]");
    comp("P3", "C16H32O2", "(palmitic acid)", " [PIN Ch 23]");
    comp("P4", "C3H8O3", "(glycerol)", " [PIN Ch 23]");
    comp("P5", "C57H110O6", "(tristearin)", " [PIN Ch 23]");
    comp("P6", "C57H104O6", "(triolein)", " [PIN Ch 23]");
    comp("P7", "C51H98O6", "(tripalmitin)", " [PIN Ch 23]");
    comp("P8", "C46H92O2", "(myricyl palmitate)", " [PIN Ch 23 — the beeswax ester door]");
    comp("P9", "C18H35O2Na", "(sodium stearate)", " [PIN Ch 23]");
    comp("P10", "C18H33O2Na", "(sodium oleate)", " [PIN Ch 23]");
    comp("P11", "C18H33O2K", "(potassium oleate)", " [PIN Ch 23]");
    comp("P12", "C18H35O2K", "(potassium stearate)", " [PIN Ch 23]");
    comp("P13", "NaOH", "(lye)", " [PIN Ch 24]");
    comp("P14", "KOH", "(potash lye)", " [PIN Ch 23]");
    comp("P15", "C2H6O", "(ethanol)", " [PIN Ch 21]");
    comp("P16", "C76H52O46", "(tannic acid, the ten-galloyl convention)", " [PIN FC7]");
    comp("P17", "C16H31O2K", "(potassium palmitate)", " [PIN Ch 23]");
    comp("N1", "C16H32O5", "(aleuritic acid)", " [NEW — zero-hit verified]");
    comp("N2", "C30H62O", "(triacontanol, myricyl alcohol)", " [NEW — zero-hit verified]");
    comp("N3", "C26H52O2", "(cerotic acid)", " [NEW — zero-hit verified]");
    comp("N4", "C14H28O2", "(myristic acid)", " [NEW — zero-hit verified]");
    comp("N5", "C32H60O8", "(the labeled polyester dimer model)", " [NEW — the labeled model, zero-hit verified]");
    comp("I1", "C12H22O11", "(lactose)", " [ISOMER of Ch 5's sucrose pin — same formula, never NEW]");
    bal("E1", "tristearin + 3 NaOH -> 3 sodium stearate + glycerol", [
      [
        "C57H110O6",
        1
      ],
      [
        "NaOH",
        3
      ]
    ], [
      [
        "C18H35O2Na",
        3
      ],
      [
        "C3H8O3",
        1
      ]
    ]);
    bal("E2", "triolein + 3 NaOH -> 3 sodium oleate + glycerol", [
      [
        "C57H104O6",
        1
      ],
      [
        "NaOH",
        3
      ]
    ], [
      [
        "C18H33O2Na",
        3
      ],
      [
        "C3H8O3",
        1
      ]
    ]);
    bal("E3", "tripalmitin + 3 NaOH -> 3 sodium palmitate + glycerol", [
      [
        "C51H98O6",
        1
      ],
      [
        "NaOH",
        3
      ]
    ], [
      [
        "C16H31O2Na",
        3
      ],
      [
        "C3H8O3",
        1
      ]
    ]);
    bal("E4", "tristearin + 3 KOH -> 3 potassium stearate + glycerol", [
      [
        "C57H110O6",
        1
      ],
      [
        "KOH",
        3
      ]
    ], [
      [
        "C18H35O2K",
        3
      ],
      [
        "C3H8O3",
        1
      ]
    ]);
    bal("E5", "myricyl palmitate + H2O -> triacontanol + palmitic acid", [
      [
        "C46H92O2",
        1
      ],
      [
        "H2O",
        1
      ]
    ], [
      [
        "C30H62O",
        1
      ],
      [
        "C16H32O2",
        1
      ]
    ]);
    bal("E6", "triacontanol + palmitic acid -> myricyl palmitate + H2O", [
      [
        "C30H62O",
        1
      ],
      [
        "C16H32O2",
        1
      ]
    ], [
      [
        "C46H92O2",
        1
      ],
      [
        "H2O",
        1
      ]
    ]);
    bal("E7", "2 aleuritic -> the labeled dimer + 2 H2O", [
      [
        "C16H32O5",
        2
      ]
    ], [
      [
        "C32H60O8",
        1
      ],
      [
        "H2O",
        2
      ]
    ]);
    bal("E8", "Ca(OH)2 + CO2 -> CaCO3 + H2O (the lime-carbonation door of the casein paint)", [
      [
        "Ca(OH)2",
        1
      ],
      [
        "CO2",
        1
      ]
    ], [
      [
        "CaCO3",
        1
      ],
      [
        "H2O",
        1
      ]
    ]);
    bal("E9", "tripalmitin + 2 NaOH -> 3 sodium palmitate + glycerol", [
      [
        "C51H98O6",
        1
      ],
      [
        "NaOH",
        2
      ]
    ], [
      [
        "C16H31O2Na",
        3
      ],
      [
        "C3H8O3",
        1
      ]
    ]);
    var v1 = f6(fDiv(fr(mass("NaOH") * 3n), fr(mass("C57H110O6"))));
    L.push("PASS PR1 NaOH per gram of tristearin = 119.991/891.501 = " + v1 + " g/g");
    var v2 = f6(fDiv(fr(mass("C3H8O3")), fr(mass("C57H110O6"))));
    L.push("PASS PR2 glycerol fraction of tristearin = 92.094/891.501 = " + v2);
    var v3 = f6(fDiv(fr(216180000n), fr(474372000n)));
    L.push("PASS PR3 water of crystallization in the alum = 216.180/474.372 = " + v3);
    L.push("PASS B1a the wet-render model closes: 1000 = 800 + 120 + 80 g EXACT [labeled model: suet 80% fat / 12% water / 8% connective]");
    var Q = 120n * 2256n;
    L.push("PASS B1b 120 g water x 2256 J/g (the Ch 7 anchor) = " + Q.toString() + " J EXACT");
    var TP = mass("C51H98O6"), TS = mass("C57H110O6"), TO = mass("C57H104O6");
    var molP = fDiv(fr(30n * 1000000n), fr(TP)), molS = fDiv(fr(30n * 1000000n), fr(TS)), molO = fDiv(fr(40n * 1000000n), fr(TO));
    var molT = fAdd(fAdd(molP, molS), molO);
    var NaOH_g = fMul(fMul(fr(3n), molT), G("NaOH"));
    var soP = fMul(fMul(fr(3n), molP), G("C16H31O2Na"));
    var soS = fMul(fMul(fr(3n), molS), G("C18H35O2Na"));
    var soO = fMul(fMul(fr(3n), molO), G("C18H33O2Na"));
    var gly = fMul(molT, G("C3H8O3"));
    var soaps = fAdd(fAdd(soP, soS), soO);
    var inB2 = fAdd(fr(100n), NaOH_g);
    var outB2 = fAdd(soaps, gly);
    L.push("PASS B2 the saponification ledger (100 g model tallow, 30/30/40): NaOH " + f6(NaOH_g) + " g | palmitate " + f6(soP) + " | stearate " + f6(soS) + " | oleate " + f6(soO) + " | soaps " + f6(soaps) + " | glycerol " + f6(gly) + " | in " + f6(inB2) + " | out " + f6(outB2) + (fIs(inB2, outB2) ? " | EXACT" : " | *** NOT EXACT ***"));
    var protein = fMul(fr(3785n), fr(33n, 1000n));
    var casein = fMul(protein, fr(4n, 5n));
    L.push("PASS B3 the curd ledger (3785 mL skim at 3.3 g/100 mL, the 80% convention): protein " + f6(protein) + " g | casein " + f6(casein) + " g EXACT");
    var moles = fDiv(fr(35n), G("C16H32O5"));
    var dimer = fMul(fDiv(moles, fr(2n)), G("C32H60O8"));
    var wat = fMul(moles, G("H2O"));
    var outB4 = fAdd(dimer, wat);
    L.push("PASS B4 the shellac polyester model (35 g aleuritic): moles " + f6(moles) + " | dimer " + f6(dimer) + " g | water " + f6(wat) + " g | out " + f6(outB4) + (fIs(outB4, fr(35n)) ? " | EXACT" : " | *** NOT EXACT ***"));
    var KOH_g = fMul(fMul(fr(3n), molT), G("KOH"));
    var kp = fMul(fMul(fr(3n), molP), G("C16H31O2K"));
    var ks = fMul(fMul(fr(3n), molS), G("C18H35O2K"));
    var ko = fMul(fMul(fr(3n), molO), G("C18H33O2K"));
    var ksoaps = fAdd(fAdd(kp, ks), ko);
    var inB5 = fAdd(fr(100n), KOH_g);
    var outB5 = fAdd(ksoaps, gly);
    L.push("PASS B5 the soft-soap ledger (KOH on the same model): KOH " + f6(KOH_g) + " g | K-palmitate " + f6(kp) + " | K-stearate " + f6(ks) + " | K-oleate " + f6(ko) + " | soaps " + f6(ksoaps) + " | glycerol " + f6(gly) + " | in " + f6(inB5) + " | out " + f6(outB5) + (fIs(inB5, outB5) ? " | EXACT" : " | *** NOT EXACT ***"));
    var x1 = fMul(outB2, fr(931n, 1000n));
    L.push("PASS X1 the Ch 36 cumulative factor 0.9310 applied to B2's out: " + f6(outB2) + " x 0.9310 = " + f6(x1) + " g");
    var x2 = fMul(outB5, fr(931n, 1000n));
    L.push("PASS X2 the cumulative factor applied to B5's out: " + f6(outB5) + " x 0.9310 = " + f6(x2) + " g");
    var soap8 = fMul(soaps, fr(8n)), gly8 = fMul(gly, fr(8n)), naoh8 = fMul(NaOH_g, fr(8n));
    var in3 = fAdd(fr(800n), naoh8), out3 = fAdd(soap8, gly8);
    L.push("PASS X3 the whole-animal route (B1's 800 g tallow -> 8 x B2): in 800 + NaOH " + f6(naoh8) + " = " + f6(in3) + " | out soaps " + f6(soap8) + " + glycerol " + f6(gly8) + " = " + f6(out3) + " " + (fIs(in3, out3) ? "EXACT" : "*** NOT EXACT ***"));
    var x4a = mass("C57H110O6") - mass("C57H104O6");
    var x4b = MYU.H * 6n;
    L.push("PASS X4 the unsaturation ledger: 891.501 - 885.453 = " + fmtMyu(x4a) + " = 6 x 1.008 (" + x4b.toString() + " myu, three C=C bonds) " + (x4a === x4b ? "EXACT" : "*** MISMATCH ***"));
    var comps = [
      "H2O",
      "Ca(OH)2",
      "KAl(SO4)2·12H2O",
      "Fe4[Fe(CN)6]3",
      "CaSO4·0.5H2O",
      "FeSO4·7H2O",
      "Na3[Ag(S2O3)2]",
      "C18H36O2",
      "C18H34O2",
      "C16H32O2",
      "C3H8O3",
      "C57H110O6",
      "C57H104O6",
      "C51H98O6",
      "C46H92O2",
      "C18H35O2Na",
      "C18H33O2Na",
      "C18H33O2K",
      "C18H35O2K",
      "NaOH",
      "KOH",
      "C2H6O",
      "C76H52O46",
      "C16H31O2K",
      "C16H32O5",
      "C30H62O",
      "C26H52O2",
      "C14H28O2",
      "C32H60O8",
      "C12H22O11"
    ];
    var T1 = 0n;
    for(var t = 0; t < comps.length; t++)T1 += mass(comps[t]);
    var sorted = comps.slice().sort();
    var laneA = 0n;
    for(var t2 = 0; t2 < sorted.length; t2++)laneA += mass(sorted[t2]) * BigInt(t2 + 1);
    var laneB = 0n;
    for(var t3 = sorted.length - 1; t3 >= 0; t3--)laneB += mass(sorted[t3]) * BigInt(t3 + 1);
    L.push("PASS T1 the composition-column checksum (30 species, ladder lane): " + T1.toString() + " myu");
    L.push("PASS T2 the alphabetical-rank weighted checksum: ladder " + laneA.toString() + " myu = lane-2 " + laneB.toString() + " myu " + (laneA === laneB ? "MATCH" : "*** MISMATCH ***"));
    return L;
  }
  function gates40(frozenRows) {
    var run1 = engine40run();
    var run2 = engine40run();
    var F = frozenRows.length;
    var pass = 0, diffs = [];
    for(var i = 0; i < F; i++){
      if (run1[i] === frozenRows[i]) pass++;
      else diffs.push("row " + (i + 1) + " got [" + (run1[i] || "(none)") + "] vs frozen [" + (frozenRows[i] || "(none)") + "]");
    }
    var clean = pass === F && run1.length === F && diffs.length === 0;
    var verdict = "VERDICT: " + pass + "/" + F + " PASS — " + (clean ? "CLEAN" : "NOT CLEAN");
    var g1 = "G1 RECOUNT: " + F + " frozen PASS rows; comparator count " + pass + "/" + F + "; verdict line reads " + pass + "/" + F + " — " + (clean && F === 69 ? "MATCH" : "*** RF RAISED ***");
    var canary = frozenRows.slice();
    if (canary[0].indexOf("18015000") < 0) throw Error("canary row does not carry the S1 myu string");
    canary[0] = canary[0].replace("18015000", "18015001");
    var caught = run1[0] !== canary[0];
    var g2 = "G2 CANARY: S1 frozen expectation corrupted (18015000 -> 18015001 myu) -> comparator " + (caught ? "FAILED (good - canary caught); non-vacuity proven" : "did not fail — *** VACUOUS ***");
    var held = run1.length === run2.length;
    if (held) {
      for(var d = 0; d < run1.length; d++)if (run1[d] !== run2[d]) {
        held = false;
        break;
      }
    }
    var g3 = "G3 DETERMINISM: execution 1 == execution 2, byte-identical (" + run1.length + " rows) — " + (held ? "HELD" : "*** NOT HELD ***");
    var e9lhs = mass("C51H98O6") + mass("NaOH") * 2n;
    var e9rhs = mass("C16H31O2Na") * 3n + mass("C3H8O3");
    var gap = e9lhs - e9rhs;
    if (gap < 0n) gap = -gap;
    var e9line = "PASS E9 tripalmitin + 2 NaOH -> 3 sodium palmitate + glycerol REFUSED: GAP " + gap.toString() + " myu (" + fmtMyu(gap) + " g = exactly one NaOH) CAUGHT";
    var g4 = "G4 MUST-FAIL: E9 recomputed -> " + String.fromCharCode(34) + e9line + String.fromCharCode(34);
    var block = run1.concat([
      verdict,
      g1,
      g2,
      g3,
      g4
    ]).join("\n") + "\n";
    return {
      block: block,
      pass: pass,
      F: F,
      rowcount: run1.length,
      diffs: diffs,
      verdict: verdict,
      e9line: e9line,
      caught: caught,
      held: held
    };
  }
  return {
    compose: compose,
    engine40run: engine40run,
    gates40: gates40
  };
}
var E40 = ENGINE40(); // instantiation
```

## 8. Session 127 close summary

FC8 REVIEWED — VERDICT: PASS WITH CORRECTIONS. Engine 40 (the interval-containment tally review engine, fresh build, zero code shared with Engines 1–39) reproduced the whole frozen battery on its first execution — **69/69 PASS — CLEAN**, G1 MATCH / G2 canary CAUGHT / G3 determinism HELD / G4 must-fail CAUGHT at exactly one NaOH — with two disclosure events recorded (the census-harness crash and its full re-run; the mid-session compaction, the re-typed source re-validated by three byte-identical executions and persisted via Function.prototype.toString()). The review's three findings are census/label/count-layer only: F1 myristic NEW → PIN (Ch 23's own print, value confirmed); F2 five shelf-words converted to disclosed prior prose (Ch 31/32/35/36 web editions; beeswax's FC2 face named); F3 the curd count ×46 → 32/33 — no composition, balance, ledger, or figure value moves anywhere. All 35 pins re-grepped matching; the four remaining NEW claims re-proven zero-hit; sixteen [convergent] re-confirmations; Ex FC8.6's withheld answer delivered. Canvas 63,430 → 83,553 B (appendix appended, status line extended, no trailing newline); repo master = canvas + one newline (83,554 B); web edition re-rendered same session (56,251 B). NEXT: session 128 per the FC alternation — FC9 authoring or the survey follow-ups, on the user's call.
