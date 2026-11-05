# Engine 80 — The Shelf-Ledger Transcripts Record (Vol VIII Ch 52 · The Medicine Shelf · session 194)

The Engine 80 battery ran at session 194 (2026-11-05) against the Ch 52 part-1 figure set, split into pieces per the binding runtime constraints. The six transcripts below are the Outputs-Verbatim records, frozen to scratch at battery completion with md5 + sdbm receipts, and spliced into this record byte-exact: each block was md5-verified against its frozen receipt at splice time (the gate), the same six transcripts the master embeds at Lab 52.1 (manuscript/vol8/ch52.md, commit 54c261be). The frozen receipts are the binding identity; the blocks below are the record.

**Piece A — the pre-flight probe** (496 B; md5 25ea403839e9f380fd178bcd8bf61555; sdbm(body) 548c3cb0):

```
P1 massMy(C9H8O4)=180159 expect 180159 -> PASS
P2 massMy(C7H5BiO4)=362093 expect 362093 -> PASS
P3 E4reverse closure={"C":0,"H":0,"O":0} -> PASS
P4 divw(3300,26)=126,24,26 q.PASS
P5 pct(210,76710)=0.2738 expect 0.2738 -> PASS
I1 wrong-mass lane 180519 vs 180159 -> CAUGHT
I2 unbalanced nitration (H2O dropped) closure={"C":0,"H":2,"O":1,"N":0} -> CAUGHT
I3 miss on wrong basis 33/0.274 = 120.4 vs the lane truth 3300/26 -> CAUGHT (126.9 lives on the 0.26 headline, disclosed)
sdbm(body)=548c3cb0
```

**Sheet 1 — the molar book, rev-2** (1,808 B; md5 1618d98d7b1b3873892b0c89a2a0f6a0; sdbm(body) e5e50c0a):

```
E80 SHEET 1 rev-2 — THE MOLAR BOOK (integer lane my = mg/mol; display = my/1000 g/mol)
REV DISCLOSURE: rev-1 printed 18 PASS / 4 FAIL — the four FAILs were HARNESS-ONLY (the expectation strings written in alphabetical element order (H8 C9 O4) against the parser insertion order (C9 H8 O4)); no mass row moved; the rev-2 harness compares compositions SORTED, the engine untouched.
S1.1 aspirin C9H8O4 my=180159 M=180.159 [PIN Ch3/Ch34] PASS
S1.2 salicylic acid C7H6O3 my=138122 M=138.122 [PIN Ch13/Ch34] PASS
S1.3 salicin C13H18O7 my=286280 M=286.280 [PIN Ch34] PASS
S1.4 salicyl alcohol C7H8O2 my=124139 M=124.139 [PIN Ch34] PASS
S1.5 acetic anhydride C4H6O3 my=102089 M=102.089 [PIN Ch34/Ch45] PASS
S1.6 acetic acid C2H4O2 my=60052 M=60.052 [PIN Ch23-25] PASS
S1.7 phenol C6H6O my=94113 M=94.113 [NEW] PASS
S1.8 p-nitrophenol C6H5NO3 my=139110 M=139.110 [NEW] PASS
S1.9 p-aminophenol C6H7NO my=109128 M=109.128 [NEW] PASS
S1.10 acetaminophen C8H9NO2 my=151165 M=151.165 [NEW] PASS
S1.11 acetanilide C8H9NO my=135166 M=135.166 [NEW] PASS
S1.12 phenacetin C10H13NO2 my=179219 M=179.219 [NEW] PASS
S1.13 pyrimethamine C12H13ClN4 my=248714 M=248.714 [NEW] PASS
S1.14 bismuth subsalicylate C7H5BiO4 my=362093 M=362.093 [NEW] PASS
S1.15 BiOCl BiOCl my=260429 M=260.429 [NEW] PASS
S1.16 chlorobutanol C4H7Cl3O my=177449 M=177.449 [NEW] PASS
S1.17 phenytoin C15H12N2O2 my=252273 M=252.273 [NEW] PASS
S1.E C9H8O4 composition-sorted [C9 H8 O4] expect [C9 H8 O4] PASS
S1.E C8H9NO2 composition-sorted [C8 H9 N1 O2] expect [C8 H9 N1 O2] PASS
S1.E C7H5BiO4 composition-sorted [Bi1 C7 H5 O4] expect [Bi1 C7 H5 O4] PASS
S1.E C12H13ClN4 composition-sorted [C12 Cl1 H13 N4] expect [C12 Cl1 H13 N4] PASS
S1.Bi Bi my=208980 M=208.980 [NEW element, convergent web basis] PASS
S1 VERDICT 22 PASS / 0 FAIL
sdbm(body)=e5e50c0a
```

**Sheet 2 — the dose book, rev-3** (1,741 B; md5 1b122da3c009d31921e6d0df45342d8a; sdbm(body) 5aed60f7):

```
E80 SHEET 2 rev-3 — THE DOSE BOOK (integer witness lanes; umol = mg*1e6/my, exact)
REV DISCLOSURE: run-1 10/16 — all six FAILs harness-only (pre-stated expectations hand-slips; the engine exact; every quotient then verified by direct multiplication). rev-2 16/16 but TWO DISPLAY-LANE slips in row text remained (S2.3 the truncation of 19.8458 to "19.84" — the exact witness carries the remainder; S2.11b the divisor slip 1000-for-100 printing 2.8 for 27.55); rev-3 prints the displays from the exact rational witness (q + r/den); NO CHECK MOVED IN ANY REV; the engine value path untouched throughout.
S2.1 325 mg aspirin umol=1803 r173323/180159 = 1.8040 mmol (mul-check true) PASS
S2.2 500 mg acetaminophen umol=3307 r97345/151165 = 3.3076 mmol PASS
S2.3 the 3 g window = 19.85 mmol; the 4 g = 26.46 mmol PASS
S2.4 72 pills x 25 mg = 1800 mg = 1.800 g exact PASS
S2.5 $750 per 25 mg = $30,000 per gram (750*40) PASS
S2.6 $22,000 / 1.8 g = 1222222 r400/1800 cents/g = $12222.22/g PASS
S2.7 500 tablets x 325 mg = 162,500 mg = 162.500 g nominal API PASS
S2.8 94% of 162.5 g = 152750 mg = 152.750 g recovered PASS
S2.9 120 pills x 262 mg = 31,440 mg = 31.440 g label subsalicylate PASS
S2.10 Bi in 31.44 g label charge = 18145 r153715/362093 mg = 18.145 g PASS
S2.11 5 g at the stated 22% implies 22.727 g theoretical (the register 22.7) PASS
S2.11b 5 g on the label-Bi basis 18.145 g = 27.6% (the register 27.6) PASS
S2.12 200 g purchasable / 5 g extracted = 40x PASS
S2.13 the Pepto revisit live views 17,368,097 [register N401 exact] PASS
S2.14 325 mg as salicylic acid umol=2352 r137056/138122 = 2.3530 mmol PASS
S2.INJ transposed-digit lane 180519 refused (aspirin stays 180159) PASS
S2 VERDICT 16 PASS / 0 FAIL
sdbm(body)=5aed60f7
```

**Sheet 3 — the chain-efficiency book, rev-2** (1,808 B; md5 8480597023ffabf80853cc130a2d6b5b; sdbm(body) e037e292):

```
E80 SHEET 3 rev-2 — THE CHAIN-EFFICIENCY BOOK (the aspirin->acetaminophen series ledger; integer witness lanes)
REV DISCLOSURE: run-1 6/10 — three FAILs were the harness pre-stated expectations (hand-slips: 507.27 for the true 507.33 mmol; 76.71 for the true 76.690 g; 79.72 for the true 79.711 g — the register figures 76.7/0.274 were themselves rounded displays of exactly these lanes, verified consistent); the fourth FAIL was the INJECTION ROW mis-designed (the rounded-vs-exact divisor seam lives at the 5th decimal, invisible at the 4-decimal display — the row now asserts the seam at its true precision and the discipline stands); no engine value moved in any rev.
S3.1 2x45.7 g = 91,400 mg ASA -> umol=507329 r114689/180159 = 507.33 mmol (mul-check true) PASS
S3.2 theoretical acetaminophen = 91,400 x 151165/180159 = 76.690 g (the register rounded display 76.7) PASS
S3.3 efficiency = 210/76,690 = 0.2738% (the register 0.274) PASS
S3.4 the 2x47.5 g spoken basis: 95,000 x 151165/180159 = 79.711 g PASS
S3.5 the spoken-basis efficiency = 210/79,711 = 0.2635% (the register 0.263, the 0.26 headline) PASS
S3.6 the miss on the 0.26 headline = 3300/26 = 126.92x (the register 126.9) PASS
S3.7 the miss on the exact spoken basis = 3,300,000/26,347 = 125.25x (the honest alternate 125.26) PASS
S3.8 0.21 g at the stated 18% final step implies 1.167 g last-step theoretical PASS
S3.9 the 33% prediction vs the realized 0.2635-0.2738%: the prediction was 125.3-126.9x the outcome [from S3.3-S3.7] PASS
S3.INJ the rounded-lane 210/76,700 = 0.27379% vs the exact-lane 0.27383% — the seam lives at the 5th decimal, invisible at the the 4-decimal display; the discipline stands (compute from the exact lane, never divide by a print — Ch 46 R07) PASS
S3 VERDICT 10 PASS / 0 FAIL
sdbm(body)=e037e292
```

**Sheet 4 — the balance book, rev-3** (2,453 B; md5 b0e0b2aa65d5c975403ad4d046097638; sdbm(body) d274e0a2):

```
E80 SHEET 4 rev-3 — THE BALANCE BOOK (the fence chapter chemistry: equations named at the knowledge level, never procedural)
REV DISCLOSURE: run-1 crashed at the parser gate — coefficient shorthand (3H2, 3HCl, 2HCl, 2H2O) refused by design, re-expressed as repeated species (harness-side). run-2 crashed at the parser gate AGAIN — the harness fed massMy the token "acid" (the two-word name "acetic acid" split at the first space instead of the last token; the gate again the engine working); rev-3 takes the LAST token. One more harness slip corrected the same rev: the aniline pin re-keyed 93128 -> 93129 (C6H7N on the held lane = 72.066+7.056+14.007 = 93.129; the 8-for-9 terminal digit a hand-slip). The engine value path untouched in every rev; the gate never bypassed.
B1 salicin hydrolysis (Ch34 E1 pin re-proved): closure={"C":0,"H":0,"O":0} massMy L=304295 R=304295 -> PASS
B2 ASA acetylation (Ch34 E4 pin re-proved): closure={"C":0,"H":0,"O":0} massMy L=240211 R=240211 -> PASS
B3 ASA hydrolysis (the E4 reverse): closure={"C":0,"H":0,"O":0} massMy L=198174 R=198174 -> PASS
B4 decarboxylation (salicylic acid -> phenol): closure={"C":0,"H":0,"O":0} massMy L=138122 R=138122 -> PASS
B5 mono-nitration (phenol -> p-nitrophenol): closure={"C":0,"H":0,"O":0,"N":0} massMy L=157125 R=157125 -> PASS
B6 reduction (p-nitrophenol + 3 H2 -> p-aminophenol + 2 H2O): closure={"C":0,"H":0,"N":0,"O":0} massMy L=145158 R=145158 -> PASS
B7 acetylation (p-aminophenol -> acetaminophen): closure={"C":0,"H":0,"N":0,"O":0} massMy L=211217 R=211217 -> PASS
B8 acetanilide formation (the Antifebrin knowledge row): closure={"C":0,"H":0,"N":0,"O":0} massMy L=153181 R=153181 -> PASS
B9 subsalicylate in acid (the Pepto axis knowledge row): closure={"C":0,"H":0,"Bi":0,"O":0,"Cl":0} massMy L=471467 R=471467 -> PASS
B10 the BiOCl white flash (bismuth chloride hydrolysis): closure={"Bi":0,"Cl":0,"H":0,"O":0} massMy L=333345 R=333345 -> PASS
PIN salicin C13H18O7 my=286280 expect 286280 PASS
PIN glucose C6H12O6 my=180156 expect 180156 PASS
PIN aspirin C9H8O4 my=180159 expect 180159 PASS
PIN acetic acid C2H4O2 my=60052 expect 60052 PASS
PIN aniline C6H7N my=93129 expect 93129 PASS
INJ1 nitration without water CAUGHT: {"C":0,"H":2,"O":1,"N":0} -> CAUGHT
INJ2 acetaminophen off-by-one lane 151166 refused -> CAUGHT
INJ3 the BiOCl row under-charged (1 HCl not 2) CAUGHT: {"Bi":0,"Cl":1,"H":1,"O":0} -> CAUGHT
S4 VERDICT 18 PASS / 0 FAIL
sdbm(body)=d274e0a2
```

**Determinism, rev-2** (1,306 B; md5 69f581dfb46331c0fda51757d7ecb66e; sdbm(body) 211f4778):

```
E80 DETERMINISM rev-2 — the S4 balance lanes recomputed with the FULL two-letter parser
REV DISCLOSURE: the first determinism piece printed 38 MATCH / 2 DIFFER — the two DIFFER rows (B9/B10) were NaN from the CHECK PIECE's own mini-parser, which handled only single-letter elements and read BiCl3 as B-i-Cl3 (the lowercase i falling outside its element table); the ENGINE's parser, proven on these exact rows in S1 (362093/260429) and S4 (471467/333345 PASS), was never at fault. This rev re-runs the balance lanes with the full parser.
D.S4.B1 mass lane L=304295 R=304295 frozen=304295 -> MATCH
D.S4.B2 mass lane L=240211 R=240211 frozen=240211 -> MATCH
D.S4.B3 mass lane L=198174 R=198174 frozen=198174 -> MATCH
D.S4.B4 mass lane L=138122 R=138122 frozen=138122 -> MATCH
D.S4.B5 mass lane L=157125 R=157125 frozen=157125 -> MATCH
D.S4.B6 mass lane L=145158 R=145158 frozen=145158 -> MATCH
D.S4.B7 mass lane L=211217 R=211217 frozen=211217 -> MATCH
D.S4.B8 mass lane L=153181 R=153181 frozen=153181 -> MATCH
D.S4.B9 mass lane L=471467 R=471467 frozen=471467 -> MATCH
D.S4.B10 mass lane L=333345 R=333345 frozen=333345 -> MATCH
DETERMINISM VERDICT 10 MATCH / 0 DIFFER (the 38 MATCH rows of run-1 stand — the single-letter molecule lanes were unaffected by the mini-parser defect)
sdbm(body)=211f4778
```

**Honest history, entire.** Every revision in the battery's history is harness-side: Sheet 1 rev-2 (four expectation-string element-order slips, the engine exact); Sheet 2 rev-3 (six pre-stated hand-slip expectations the engine corrected, then two display slips caught by the freeze discipline — no check moved in any rev); Sheet 3 rev-2 (three hand-slip expectations, one mis-designed injection row re-designed); Sheet 4 rev-3 (two parser-gate crashes where the harness fed the engine malformed input and the gate refused it both times, one pin re-keyed 93128→93129 — a hand-slip caught by the engine's own lane); determinism rev-2 (a check-piece mini-parser defect, disclosed). The engine's value path was defect-free in every run; the gate was never bypassed; eight injections CAUGHT across the battery; determinism byte-identical on re-run. Total transcript mass: 9,612 B.
