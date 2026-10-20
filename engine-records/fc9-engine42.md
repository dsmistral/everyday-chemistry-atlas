# FC9 Engine 42 record — the event-sorted sweep review compositor (session 129, the FC9 Phase-3 adversarial review)

Session 129 (2026-10-20): the FC9 review unit per row 129 — "Clay, Kilns, and Earth Building," drafted session 128, now under independent review per the FC alternation. Engine 42 — a fresh engine sharing zero code with Engines 1–41 — re-executed the whole frozen 73-row battery of Lab FC9.1 (S1–S8, R1–R14, P1–P19, N1–N7, I1, E1–E9, PR1–PR3, B1–B6, X1–X4, T1–T2), the expectations the frozen block's got-strings verbatim, loaded at runtime from the durable Engine 41 record's §4 fence, and every value recomputed by its own independent method. Verdict: **73/73 PASS — CLEAN**, gates G1–G4 all held; the review contract held at every mismatch — re-verify, never re-author — and no frozen expectation was patched anywhere in the chain, the whole honest history below.

## 1. Design spec

- **THE EVENT-SORTED SWEEP, the fresh axis:** one token pass attaches each bracket group's subscript to BOTH its OPEN and its CLOSE event (the digit run after a close feeds the pair); a flat left-to-right sweep then carries a single running integer multiplier — multiplied at every OPEN, divided at every CLOSE — each atom's contribution its own subscript times the running multiplier. Counting is by event, not by structure: no bracket-interval tables (Engine 40), no lazy-tag segment tree (41), no depth registers (39), no stack frames (38), no CPS continuations (37), no parse tree (36), no memoized grammar (35), no census-tally expansion (34), no innermost rewriting (33), no RPN shunting-yard (31) — and the event pairing is Engine 42's own; Engines 1–30 predate the compositor era, their axes named in their own records.
- **The hydrate dot:** a formula split at its · separators into segments, each segment carrying its own leading coefficient parsed as an exact rational, with **no multiplier inheritance across the dot**; the half-unit hydrate grid (coefficients multiples of 0.5) is checked **after** syntax — plaster's 0.5 is legal, R13's 0.35 REFUSED on the grid.
- **The gate order, the chapter's own held:** NAME first (the potter's family words — slip, grog, saggar, terracotta, stoneware, porcelain — refused before any formula parses; the tannin lesson inherited), then admission during tokenizing (the held-22 element table in integer myu BigInt; a two-letter candidate is refused at its own length — Ti, Zr, Cr, Li refused as written — and a single-letter unknown likewise — P, F), then syntax (unclosed groups REFUSED — R14), then the hydrate grid.
- **Exact BigInt rationals throughout:** composition masses exact integers; the worked ledgers exact rational identities — B1's v × t = 0.1 m and the 100 / 2500 t-ratios, B3's and X2's in = out, B4's flux unity = 1 — and the display contract the frozen got-strings govern: g/mol with trailing zeros trimmed, half-up N-dp trimmed fractions, half-up N-s.f. trimmed times, 4-s.f. TRUNCATED scientific velocities (the sand velocity's 2.246e-1 a truncation, never a rounding).
- **The witness lane, disclosed:** the containment product as a recursive group tree — Engine 40's own method, credited — runs as lane 2 beside the event sweep's lane 1, and T2 cross-checks all 35 composition species: 35/35 ALL MATCH. The fresh axis is the sweep; the tree is the witness, not the engine.
- **The gates:** G1 the machine recount (73 frozen PASS rows expected, 73 frozen / 73 counted), G2 the canary (a corrupted expectation must FAIL at its row alone), G3 determinism (byte-identical re-execution), G4 the designed must-fail (E9's one-water-short dehydroxylation caught at exactly one H2O).

## 2. Honest run history

Nothing smoothed; every defect named at its own line. **Typed run 1 — a crash before any row printed:** the tokenizer's digit-run regex carried no capture group, so its match array had no extracted value and every subscripted formula failed in isolation debug. **Typed run 2 — 72/73:** B1 failed its own exact t-ratio assert — `vOf` carried a stray extra ÷18 and the clay d² denominator was typed 10¹⁴ where the register's clay grain is 1/10¹². **Typed run 3 — 71/73:** B1's decade() used unsigned BigInt powers and threw on negative exponents (the decade of a value below 1 must be found by comparison helpers, never by 10n**e); and X2's IN clause dropped "+ 3000 kg sand" — caught by the row-level expected-display compare with every X2 number otherwise correct. The three fixes were verified in isolation and the engine fully re-typed per the session-127 precedent. **Re-typed run 4 — 72/73:** one display-harness defect — the significant-figures formatter's leading-zero pad repeated 1−d zeros instead of 1−cut, printing the sand time as 00000000.4451652 — caught by the row-level expected-display compare **before any freeze**. **Re-typed run 5 — 73/73 PASS — CLEAN**, the gates G1–G4 all held at the same run, the whole battery run twice byte-identical, the canary caught at S1 alone, E9 caught at exactly one H2O. At no point in the chain was a frozen expectation patched: every mismatch was a finding priced against the harness or the display layer, never against the frozen block — the review contract held to the end.

## 3. The gates

- **G1 RECOUNT:** 73 frozen PASS rows expected, 73 frozen / 73 counted — MATCH. The FC7 RF-1 lesson, machine-verified from the outside this time.
- **G2 CANARY:** S1's frozen expectation corrupted in memory (474372000 → 474372001 myu) — the comparator FAILED at S1 and at nothing else; non-vacuity proven.
- **G3 DETERMINISM:** the whole battery run twice, byte-identical (73 rows) — HELD.
- **G4 MUST-FAIL:** E9 recomputed — kaolinite dehydroxylated one water short, GAP 18015000 myu (18.015 g = exactly one H2O) CAUGHT, the refusal string byte-identical to the frozen row.

## 4. The frozen runblock (spliced verbatim from the engine's own output file, never retyped)

```text
PASS S1 KAl(SO4)2·12H2O (potash alum) = 474.372 g/mol (474372000 myu) [SELF, the Ch 3 stress pin]
PASS S2 CaSO4·0.5H2O (plaster of Paris) = 145.1415 g/mol (145141500 myu) [SELF, the half-hydrate stress, Ch 30]
PASS S3 Fe4[Fe(CN)6]3 (Prussian blue) = 859.239 g/mol (859239000 myu) [SELF, the Ch 22 pin]
PASS S4 H2O (water) = 18.015 g/mol (18015000 myu) [SELF, the Ch 4 pin]
PASS S5 Ca(OH)2 (slaked lime) = 74.092 g/mol (74092000 myu) [SELF, the Ch 13 pin]
PASS S6 FeSO4·7H2O (green vitriol) = 278.006 g/mol (278006000 myu) [SELF, the Ch 19 pin]
PASS S7 Na2S2O3·5H2O (hypo) = 248.172 g/mol (248172000 myu) [SELF, the Ch 17 pin]
PASS S8 CaSO4·2H2O (gypsum) = 172.164 g/mol (172164000 myu) [SELF, the Ch 30 pin]
PASS P1 Al2Si2O5(OH)4 (kaolinite) = 258.157 g/mol (258157000 myu) [PIN Ch 30]
PASS P2 Al2Si2O7 (metakaolin) = 222.127 g/mol (222127000 myu) [PIN Ch 30]
PASS P3 SiO2 (silica) = 60.083 g/mol (60083000 myu) [PIN Ch 30]
PASS P4 Al2O3 (alumina) = 101.961 g/mol (101961000 myu) [PIN Ch 30]
PASS P5 MgO (magnesia) = 40.304 g/mol (40304000 myu) [PIN Ch 30]
PASS P6 B2O3 (boric oxide) = 69.617 g/mol (69617000 myu) [PIN Ch 30]
PASS P7 Na2CO3 (soda ash) = 105.988 g/mol (105988000 myu) [PIN Ch 14/30]
PASS P8 Na2SiO3 (sodium silicate) = 122.062 g/mol (122062000 myu) [PIN Ch 30]
PASS P9 CaO (quicklime) = 56.077 g/mol (56077000 myu) [PIN Ch 14/30]
PASS P10 CaCO3 (limestone) = 100.086 g/mol (100086000 myu) [PIN Ch 24/30]
PASS P11 Ca(OH)2 (slaked lime) = 74.092 g/mol (74092000 myu) [PIN Ch 13/30]
PASS P12 MgCO3 (magnesite) = 84.313 g/mol (84313000 myu) [PIN Ch 30]
PASS P13 CaSiO3 (wollastonite) = 116.16 g/mol (116160000 myu) [PIN Ch 30]
PASS P14 Ca3SiO5 (alite) = 228.314 g/mol (228314000 myu) [PIN Ch 30]
PASS P15 Ca2SiO4 (belite) = 172.237 g/mol (172237000 myu) [PIN Ch 30]
PASS P16 CaMg(CO3)2 (dolomite) = 184.399 g/mol (184399000 myu) [PIN Ch 30]
PASS P17 CuO (copper(II) oxide) = 79.545 g/mol (79545000 myu) [PIN Ch 11 — the Cu-fix row]
PASS P18 Fe2O3 (hematite) = 159.687 g/mol (159687000 myu) [PIN Ch 30]
PASS P19 Fe3O4 (magnetite) = 231.531 g/mol (231531000 myu) [PIN Ch 11]
PASS N1 KAlSi3O8 (orthoclase) = 278.327 g/mol (278327000 myu) [NEW, zero-hit verified]
PASS N2 NaAlSiO4 (nepheline) = 142.053 g/mol (142053000 myu) [NEW, zero-hit verified]
PASS N3 Al6Si2O13 (mullite) = 426.049 g/mol (426049000 myu) [NEW value, zero-hit; the word mullite is Ch 30 prose, disclosed]
PASS N4 Ca2Al2SiO7·8H2O (strätlingite, a model hydrate) = 418.318 g/mol (418318000 myu) [NEW, zero-hit verified, MODEL]
PASS N5 K2SiO3 (potassium silicate) = 154.278 g/mol (154278000 myu) [NEW, zero-hit verified]
PASS N6 Si4O10 (a silica-ring exhibit) = 272.33 g/mol (272330000 myu) [NEW, zero-hit verified, EXHIBIT]
PASS N7 K2CaSi2O6 (the ash-glass model) = 270.438 g/mol (270438000 myu) [NEW, zero-hit verified, MODEL]
PASS I1 Al2O3·2SiO2·2H2O (kaolinite as its oxide sum) = 258.157 g/mol (258157000 myu) [ISOMER of P1, never NEW]
PASS R1 Ca5(PO4)3OH REFUSED [element P not in the held-22 table] — the twentieth zero-admission gate
PASS R2 TiO2 REFUSED [element Ti not in the held-22 table]
PASS R3 ZrSiO4 REFUSED [element Zr not in the held-22 table]
PASS R4 Cr2O3 REFUSED [element Cr not in the held-22 table]
PASS R5 LiAlSi2O6 REFUSED [element Li not in the held-22 table]
PASS R6 CaF2 REFUSED [element F not in the held-22 table]
PASS R7 slip REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R8 grog REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R9 saggar REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R10 terracotta REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R11 stoneware REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R12 porcelain REFUSED [a family or mixture NAME, not a formula — the tannin lesson held]
PASS R13 CaSO4·0.35H2O REFUSED [coefficient not on the half-hydrate grid]
PASS R14 Al2Si2O5(OH4 REFUSED [unclosed group]
PASS E1 Al2Si2O5(OH)4 -> Al2Si2O7 + 2H2O (kaolinite gives up its structural water): 258157000 myu = 258157000 myu (258.157 g) EXACT
PASS E2 CaCO3 -> CaO + CO2 (the kiln's calcination rung): 100086000 myu = 100086000 myu (100.086 g) EXACT
PASS E3 CaO + H2O -> Ca(OH)2 (slaking): 74092000 myu = 74092000 myu (74.092 g) EXACT
PASS E4 K2CO3 + SiO2 -> K2SiO3 + CO2 (the feldspar's potash door): 198287000 myu = 198287000 myu (198.287 g) EXACT
PASS E5 Na2CO3 + SiO2 -> Na2SiO3 + CO2 (the soda-flux door): 166071000 myu = 166071000 myu (166.071 g) EXACT
PASS E6 3Al2Si2O7 -> Al6Si2O13 + 4SiO2 (metakaolin builds mullite): 666381000 myu = 666381000 myu (666.381 g) EXACT
PASS E7 Ca(OH)2 + CO2 -> CaCO3 + H2O (carbonation, the lime round trip): 118101000 myu = 118101000 myu (118.101 g) EXACT
PASS E8 CaMg(CO3)2 -> CaO + MgO + 2CO2 (dolomite burns twice): 184399000 myu = 184399000 myu (184.399 g) EXACT
PASS E9 Al2Si2O5(OH)4 -> Al2Si2O7 + H2O (one water short) REFUSED: GAP 18015000 myu (18.015 g = exactly one H2O) CAUGHT
PASS PR1 2H2O per gram of kaolinite = 36.03/258.157 = 0.139566 g/g [Ch 30 prints 13.96%]
PASS PR2 CO2 per gram of CaO = 44.009/56.077 = 0.784796 g/g
PASS PR3 slaking water per gram of CaO = 18.015/56.077 = 0.321255 g/g [Ch 21 printed 0.32125, a truncation; the 6dp half-up value governs]
PASS B1 jar test, Ch 5's Stokes register re-derived at full precision (drho 1652 kg/m3, g 9.81, eta 1.002e-3, column 0.1 m): sand d = 5e-4 m: v 2.246e-1 m/s, t 0.4451652 s; silt d = 5e-5 m: v 2.246e-3 m/s, t 44.51652 s; clay d = 1e-6 m: v 8.985e-7 m/s, t 111291.3 s = 30.9142 h; v × t = 0.1 m EXACT all three; t-ratios silt/sand 100 and clay/silt 2500 EXACT
PASS B2 the lime round trip: Ca(OH)2 + CO2 -> CaCO3 + H2O: 118.101 g = 118.101 g EXACT (E7's pair)
PASS B3 hot mortar, 10.000 kg quicklime basis: n = 10000/56.077 = 178.32623 mol CaO; in 10.000 kg CaO + 3.212547 kg slaking water + 30.000 kg sand + 7.847959 kg CO2 = 51.060506 kg; out 17.847959 kg CaCO3 + 3.212547 kg H2O + 30.000 kg sand = 51.060506 kg; in = out EXACT
PASS B4 the model ash glaze, oxide masses 1:2:3:14 (K2O:CaO:Al2O3:SiO2, bases 94.195/56.077/101.961/60.083): UMF = 0.229385 / 0.770615 / 0.63574 / 5.034644; flux unity 0.229385 + 0.770615 = 1 EXACT
PASS B5 ash glass: K2CO3 + CaCO3 + 2SiO2 -> K2CaSi2O6 + 2CO2: 358456000 myu = 358456000 myu (358.456 g) EXACT
PASS B6 slaking heat, Ch 14's band -63.7..-65.2 kJ/mol, ceiling-side working value 65.0: 178.32623 mol × 65.0 kJ/mol = 11591.2 kJ
PASS X1 dehydroxylation ledger: 700 g kaolinite -> 97.6964 g water + 602.3036 g metakaolin EXACT; 500 g kaolinite -> 69.7831 g water EXACT (Ch 30's 69.78 g mug case at full precision)
PASS X2 hot mortar at one hundred times: 1000 kg CaO + 321.254703 kg water + 3000 kg sand + 784.795906 kg CO2 = 5106.050609 kg in; 1784.795906 kg CaCO3 + 321.254703 kg water + 3000 kg sand = 5106.050609 kg out; in = out EXACT
PASS X3 mullitization: 3 Al2Si2O5(OH)4 -> Al6Si2O13 + 4SiO2 + 6H2O: 774471000 myu = 774471000 myu (774.471 g) EXACT
PASS X4 dolomite fractions: CaO 30.4107% + MgO 21.857% + CO2 47.7324% = 100% at full precision EXACT
PASS T1 composition checksum: engine sum 6955891500 myu over 35 rows = hand-sum 6955891500 myu MATCH
PASS T2 containment rescan: lane-2 products vs lane-1 on all 35 species: 35/35 ALL MATCH
VERDICT 73/73 PASS CLEAN — Engine 42, the event-sorted sweep review compositor, re-frozen for FC9
G1 machine recount: 73 frozen PASS rows expected, 73 frozen / 73 counted MATCH
G2 canary: S1 frozen expectation corrupted to 474372001 myu -> S1 FAILED caught
G3 determinism: two independent runs byte-identical
G4 must-fail: E9 GAP 18015000 myu (18.015 g = exactly one H2O) CAUGHT
```

## 5. Expectations provenance

The expectations are the frozen Engine 41 runblock's got-strings, loaded at runtime from the durable record's §4 fence and compared row by row — the review's own contract: the frozen block is the spec, re-verified and never re-authored. The T1 hand-sum (6,955,891,500 myu) and the E9 gap (18,015,000 myu) are parsed from the frozen rows themselves, never re-typed into the engine. One annotation disclosed: the frozen T2 row reads "containment rescan" — the session-128 got-string naming the lane-2 language of its own record — while Engine 42's own lane 2 is the containment-product group tree, Engine 40's method credited in §1; the row reproduces byte-identically, the lane underneath it the review's own.

## 6. The session-129 checks (all PAID at this close)

- **The pin re-greps (session-112 line, raw `grep -c` counts in the owners' own pages, re-run at the review HEAD): all 19 PIN values plus the SELF owners plus PR3's anchor verified, zero mismatches** — the Chapter 30 earth set at their printed values (kaolinite 258.157 ×6; metakaolin 222.127 ×3; SiO2 60.083 ×3; Al2O3 101.961 ×3; MgO 40.304 ×3; B2O3 69.617 ×3; Na2CO3 105.988 ×2, Ch 14 ×6; Na2SiO3 122.062 ×4; CaO 56.077 ×7, Ch 14 ×2; CaCO3 100.086 ×3, Ch 24 ×6; Ca(OH)2 74.092 ×11, Ch 13 ×2, Ch 14 ×4; MgCO3 84.313 ×1; CaSiO3 116.16 ×4; alite 228.314 ×4; belite 172.237 ×5; dolomite 184.399 ×4; Fe2O3 159.687 ×3; plaster 145.1415 ×2; gypsum 172.164 ×3), Ch 11's CuO 79.545 ×1 and Fe3O4 231.531 ×1, the SELF owners (alum 474.372 Ch 3 ×4; hypo 248.172 Ch 17 ×2; Prussian blue 859.239 Ch 22 ×8; green vitriol 278.006 Ch 19 ×2; water 18.015 Ch 4 ×1), and PR3's Ch 21 anchor 0.32125 ×4 — the printed truncation, its note carried in the row. The stress/balance anchors re-verified beside them: Ch 5's three-jar register (Δρ 1652 ×1; the domain boundary's 60.7 µm ×2, 61 µm ×1), Ch 14's slaking band (63.7 ×3, 65.2 ×4, the 785 kg CO2/t CaO figure ×4, the 32.1% water demand ×5), Ch 30's 13.96% ×6, the 69.78 g mug ×7, the 573 °C door ×6, the fired mug's 430.22 g ×7.
- **The NEW zero-hit re-proofs (session-100 binding line) at the review HEAD, CLEAN:** the seven NEW values (278.327, 142.053, 426.049, 418.318, 154.278, 272.33, 270.438) and their words (orthoclase, nepheline, strätlingite, K2SiO3, Si4O10, K2CaSi2O6) zero-hit across the 28 local masters ch03–ch30, the web editions (fc9's own excluded as home, disclosed), and the fc1–fc8 canvases. Disclosed exclusions: PROJECT.md and KNOWLEDGE.md project logs; the battery-spec home (the Engine 41 record); and the review's own artifacts — this record's §4 runblock and §7 source, spliced here the same session. The three disclosed catches stand re-verified: the word mullite in Ch 30's prose (×5) with N3's value 426.049 zero-hit everywhere; the dolomite formula in Ch 30's own print (×4), P16 a PIN never a NEW claim; the jar test at Ch 5's register level (the three-jar lecture and its 60.7 µm boundary), B1 re-deriving that register at full precision rather than quoting it.
- **The web [convergent] re-confirmations (fresh searches at this review HEAD), zero corrections owed:** the UMF/Seger flux-unity convention — the total of all flux oxides set to 1.0 (glazy.org's analysis pages; digitalfire's unity-formula glossary agreeing); wood ash as the primitive glaze material mixed with clay and feldspar, the ash's own fluxes dominant (digitalfire's wood-ash pages); the pit fire at ~650–980 °C (ceramicinfospot's pit-firing guide, 1200–1800 °F) with earthenware the honest low-fire product (its firing-temperatures guide beside it); cob and adobe as soil selection — the subsoil of clay, sand, and straw (greenhomebuilding's cob pages, the soil-testing guides agreeing).
- **The canvas amendment and its web edition:** the FC9 canvas extended per extend-never-rewrite — the Chapter-status line's reviewed clause swapped in place (PASS CLEAN, zero corrections owed), and the Revision Appendix appended after the closing italic (review description; honest history; gates; the 78-line Engine 42 runblock spliced programmatically via placeholder, never retyped; pin re-grep inventory; NEW re-proofs; [convergent] re-confirmations; Ex FC9.6's withheld ◆ answer delivered, battery rows and [convergent] endpoints only, no new figures; VERDICT; the new closing status line) — 67,168 → 85,176 B, no trailing newline, the block verified present by first/last line and machine count. The web edition re-rendered 59,078 → 59,453 B after the renderer was first re-validated **byte-identical against the known-good fc7-web.html (56,431 B)**; the content contract held — the render delta is the status clause alone, the Revision Appendix md-only as the Canon-cut governs.

## 7. The full Engine 42 source, verbatim (generated from the executed code via Function.prototype.toString() — no elisions)

```typescript
function fc9Engine42(FROZEN) {
    // ===== Engine 42: the event-sorted sweep review compositor (FC9 review) =====
    // Review contract: re-verify, never re-author. The 73 expectations are the
    // frozen Engine 41 runblock's got-strings, passed in verbatim from the
    // durable record; this engine recomputes every value by its own method and
    // compares row by row — any mismatch is a finding for adjudication.
    // Fresh axis vs Engines 1-41: composition by bracket-EVENT pairing. One
    // token pass attaches each bracket group's subscript to BOTH its OPEN and
    // its CLOSE event; a flat left-to-right sweep then carries a single running
    // integer multiplier, multiplied at every OPEN and divided at every CLOSE.
    // No interval table (Engine 40), no lazy-tag segment tree (Engine 41), no
    // depth registers (Engine 39), no recursion on lane 1 (Engine 38's bracket
    // recursion). Lane 2 is the disclosed witness lane — the containment
    // product as a group tree (Engine 40's method, credited) — and runs only as
    // the T2 cross-check over the 35 species. All arithmetic is exact BigInt
    // rationals. Gate order: NAME (an all-lowercase family word) first, then
    // held-22 admission during tokenizing, then syntax (bracket balance), and
    // only then the half-unit hydrate grid on leading coefficients.
    const MASS = {
      H: 1008000n,
      C: 12011000n,
      N: 14007000n,
      O: 15999000n,
      Na: 22990000n,
      Mg: 24305000n,
      Al: 26982000n,
      Si: 28085000n,
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
      Mn: 54938000n
    };
    const NAME_REASON = "a family or mixture NAME, not a formula — the tannin lesson held";
    class Refusal extends Error {
    }
    const refuse = function(m) {
      throw new Refusal(m);
    };
    // ---- exact rational arithmetic (normalized [num, den], den > 0) ----
    const rgcd = function(a, b) {
      a = a < 0n ? -a : a;
      b = b < 0n ? -b : b;
      while(b){
        const t = a % b;
        a = b;
        b = t;
      }
      return a;
    };
    const rat = function(n, d) {
      if (d === 0n) throw new Error("zero denominator");
      if (d < 0n) {
        n = -n;
        d = -d;
      }
      const g = rgcd(n, d);
      return g === 0n ? [
        0n,
        1n
      ] : [
        n / g,
        d / g
      ];
    };
    const Z = [
      0n,
      1n
    ], U = [
      1n,
      1n
    ];
    const radd = function(p, q) {
      return rat(p[0] * q[1] + q[0] * p[1], p[1] * q[1]);
    };
    const rsub = function(p, q) {
      return rat(p[0] * q[1] - q[0] * p[1], p[1] * q[1]);
    };
    const rmul = function(p, q) {
      return rat(p[0] * q[0], p[1] * q[1]);
    };
    const rdiv = function(p, q) {
      return rat(p[0] * q[1], q[0] * p[1]);
    };
    const req = function(p, q) {
      return p[0] === q[0] && p[1] === q[1];
    };
    const rcmp = function(p, q) {
      const l = p[0] * q[1], r = q[0] * p[1];
      return l < r ? -1 : l > r ? 1 : 0;
    };
    // ---- display contract (the frozen got-strings govern) ----
    const trimEnd0 = function(s) {
      while(s.indexOf(".") >= 0 && s.endsWith("0"))s = s.slice(0, -1);
      if (s.endsWith(".")) s = s.slice(0, -1);
      return s;
    };
    const myuG = function(m) {
      const neg = m < 0n;
      if (neg) m = -m;
      const ip = m / 1000000n, fp = m % 1000000n;
      let s = ip.toString();
      if (fp > 0n) {
        let f = fp.toString();
        while(f.length < 6)f = "0" + f;
        while(f.endsWith("0"))f = f.slice(0, -1);
        s = s + "." + f;
      }
      return neg ? "-" + s : s;
    };
    const fracDp = function(p, dp) {
      const sc = 10n ** BigInt(dp);
      const up = rat(p[0] * 2n * sc + p[1], p[1] * 2n);
      const ip = up[0] / up[1];
      let s = ip.toString();
      if (dp > 0) {
        if (s.length <= dp) s = "0".repeat(dp + 1 - s.length) + s;
        s = s.slice(0, s.length - dp) + "." + s.slice(s.length - dp);
        s = trimEnd0(s);
      }
      return s;
    };
    // decade via comparison helpers only (10n**e is unsigned — the attempt-3 lesson)
    const pow10q = function(k) {
      return k >= 0 ? [
        10n ** BigInt(k),
        1n
      ] : [
        1n,
        10n ** BigInt(-k)
      ];
    };
    const decade = function(p) {
      let e = 0;
      while(rcmp(p, pow10q(e + 1)) >= 0)e++;
      while(rcmp(p, pow10q(e)) < 0)e--;
      return e;
    };
    const sigSf = function(p, sf) {
      let e = decade(p);
      const scaled = rmul(p, pow10q(sf - 1 - e));
      const up = rat(scaled[0] * 2n + scaled[1], scaled[1] * 2n);
      let ip = up[0] / up[1];
      if (ip.toString().length > sf) {
        e = e + 1;
        ip = ip / 10n;
      }
      const d = e - sf + 1;
      let s = ip.toString();
      if (d < 0) {
        const cut = s.length + d;
        if (cut <= 0) {
          s = "0".repeat(1 - cut) + s;
          s = s.slice(0, 1) + "." + s.slice(1);
        } else {
          s = s.slice(0, cut) + "." + s.slice(cut);
        }
        s = trimEnd0(s);
      } else {
        s = s + "0".repeat(d);
      }
      return s;
    };
    const sciTrunc = function(p) {
      const e = decade(p);
      const scaled = rmul(p, pow10q(3 - e));
      const ip = scaled[0] / scaled[1];
      const s = ip.toString().padStart(4, "0");
      return s.slice(0, 1) + "." + s.slice(1) + "e" + e;
    };
    // ---- the compositor: one token pass -> bracket events -> flat sweep ----
    const ratOfDec = function(t) {
      return t.indexOf(".") < 0 ? rat(BigInt(t), 1n) : rat(BigInt(t.replace(".", "")), 10n ** BigInt(t.length - t.indexOf(".") - 1));
    };
    const onHalfGrid = function(c) {
      return c[0] * 2n % c[1] === 0n;
    };
    function parseSeg(seg) {
      let rest = seg, coeff = null;
      const cm = /^[0-9]+(?:\.[0-9]+)?/.exec(rest);
      if (cm) {
        coeff = ratOfDec(cm[0]);
        rest = rest.slice(cm[0].length);
      }
      const toks = [];
      let i = 0;
      while(i < rest.length){
        const ch = rest[i];
        if (ch === "(" || ch === "[") {
          toks.push({
            k: "O",
            sub: 1n
          });
          i++;
          continue;
        }
        if (ch === ")" || ch === "]") {
          toks.push({
            k: "C",
            sub: 1n
          });
          i++;
          continue;
        }
        if (ch >= "0" && ch <= "9") {
          const dm = /^[0-9]+/.exec(rest.slice(i));
          toks.push({
            k: "N",
            v: BigInt(dm[0])
          });
          i += dm[0].length;
          continue;
        }
        if (ch >= "A" && ch <= "Z") {
          const low = i + 1 < rest.length && rest[i + 1] >= "a" && rest[i + 1] <= "z";
          const sym = low ? rest.slice(i, i + 2) : ch;
          if (!(sym in MASS)) refuse("element " + sym + " not in the held-22 table");
          toks.push({
            k: "E",
            v: sym,
            sub: 1n
          });
          i += sym.length;
          continue;
        }
        refuse("unparseable formula");
      }
      const st = [];
      for(let j = 0; j < toks.length; j++){
        const t = toks[j];
        if (t.k === "O") {
          t.pair = -1;
          st.push(j);
        } else if (t.k === "C") {
          const o = st.pop();
          if (o === undefined) refuse("unmatched close bracket");
          t.pair = o;
          toks[o].pair = j;
        } else if (t.k === "N") {
          const p = toks[j - 1];
          if (!p) refuse("a leading coefficient must begin the segment");
          if (p.k === "E") p.sub = t.v;
          else if (p.k === "C") {
            p.sub = t.v;
            toks[p.pair].sub = t.v;
          } else refuse("unparseable formula");
        }
      }
      if (st.length) refuse("unclosed group");
      return {
        coeff: coeff,
        toks: toks
      };
    }
    function segSweep(toks) {
      let mult = 1n, acc = 0n;
      for (const t of toks){
        if (t.k === "O") mult *= t.sub;
        else if (t.k === "C") mult /= t.sub;
        else if (t.k === "E") acc += MASS[t.v] * t.sub * mult;
      }
      return acc;
    }
    function segTree(toks) {
      let pos = 0;
      const walk = function() {
        let acc = 0n;
        while(pos < toks.length){
          const t = toks[pos];
          if (t.k === "E") {
            acc += MASS[t.v] * t.sub;
            pos++;
          } else if (t.k === "O") {
            pos++;
            const inner = walk();
            const c = toks[pos];
            pos++;
            acc += inner * c.sub;
          } else if (t.k === "C") {
            return acc;
          } else {
            pos++;
          }
        }
        return acc;
      };
      return walk();
    }
    const NAME_RE = /^[a-z]+$/;
    function massOf(input) {
      if (NAME_RE.test(input)) refuse(NAME_REASON);
      const parts = input.split("·");
      const parsed = parts.map(parseSeg);
      for (const p of parsed){
        if (p.coeff !== null && !onHalfGrid(p.coeff)) refuse("coefficient not on the half-hydrate grid");
      }
      let tot = Z;
      for (const p of parsed)tot = radd(tot, rmul(p.coeff === null ? U : p.coeff, rat(segSweep(p.toks), 1n)));
      return tot;
    }
    function witnessOf(input) {
      if (NAME_RE.test(input)) refuse(NAME_REASON);
      const parts = input.split("·");
      const parsed = parts.map(parseSeg);
      for (const p of parsed){
        if (p.coeff !== null && !onHalfGrid(p.coeff)) refuse("coefficient not on the half-hydrate grid");
      }
      let tot = Z;
      for (const p of parsed)tot = radd(tot, rmul(p.coeff === null ? U : p.coeff, rat(segTree(p.toks), 1n)));
      return tot;
    }
    function sideSum(side) {
      let tot = Z;
      for (const term of side.split("+"))tot = radd(tot, massOf(term.trim()));
      return tot;
    }
    const perMol = function(f) {
      return rdiv(massOf(f), [
        1000000n,
        1n
      ]);
    };
    const got = [];
    let e9Caught = false;
    // ---- 35 composition species: 8 SELF + 19 PIN + 7 NEW + 1 ISOMER ----
    const SP = [
      [
        "S1",
        "KAl(SO4)2·12H2O",
        "potash alum",
        "SELF, the Ch 3 stress pin"
      ],
      [
        "S2",
        "CaSO4·0.5H2O",
        "plaster of Paris",
        "SELF, the half-hydrate stress, Ch 30"
      ],
      [
        "S3",
        "Fe4[Fe(CN)6]3",
        "Prussian blue",
        "SELF, the Ch 22 pin"
      ],
      [
        "S4",
        "H2O",
        "water",
        "SELF, the Ch 4 pin"
      ],
      [
        "S5",
        "Ca(OH)2",
        "slaked lime",
        "SELF, the Ch 13 pin"
      ],
      [
        "S6",
        "FeSO4·7H2O",
        "green vitriol",
        "SELF, the Ch 19 pin"
      ],
      [
        "S7",
        "Na2S2O3·5H2O",
        "hypo",
        "SELF, the Ch 17 pin"
      ],
      [
        "S8",
        "CaSO4·2H2O",
        "gypsum",
        "SELF, the Ch 30 pin"
      ],
      [
        "P1",
        "Al2Si2O5(OH)4",
        "kaolinite",
        "PIN Ch 30"
      ],
      [
        "P2",
        "Al2Si2O7",
        "metakaolin",
        "PIN Ch 30"
      ],
      [
        "P3",
        "SiO2",
        "silica",
        "PIN Ch 30"
      ],
      [
        "P4",
        "Al2O3",
        "alumina",
        "PIN Ch 30"
      ],
      [
        "P5",
        "MgO",
        "magnesia",
        "PIN Ch 30"
      ],
      [
        "P6",
        "B2O3",
        "boric oxide",
        "PIN Ch 30"
      ],
      [
        "P7",
        "Na2CO3",
        "soda ash",
        "PIN Ch 14/30"
      ],
      [
        "P8",
        "Na2SiO3",
        "sodium silicate",
        "PIN Ch 30"
      ],
      [
        "P9",
        "CaO",
        "quicklime",
        "PIN Ch 14/30"
      ],
      [
        "P10",
        "CaCO3",
        "limestone",
        "PIN Ch 24/30"
      ],
      [
        "P11",
        "Ca(OH)2",
        "slaked lime",
        "PIN Ch 13/30"
      ],
      [
        "P12",
        "MgCO3",
        "magnesite",
        "PIN Ch 30"
      ],
      [
        "P13",
        "CaSiO3",
        "wollastonite",
        "PIN Ch 30"
      ],
      [
        "P14",
        "Ca3SiO5",
        "alite",
        "PIN Ch 30"
      ],
      [
        "P15",
        "Ca2SiO4",
        "belite",
        "PIN Ch 30"
      ],
      [
        "P16",
        "CaMg(CO3)2",
        "dolomite",
        "PIN Ch 30"
      ],
      [
        "P17",
        "CuO",
        "copper(II) oxide",
        "PIN Ch 11 — the Cu-fix row"
      ],
      [
        "P18",
        "Fe2O3",
        "hematite",
        "PIN Ch 30"
      ],
      [
        "P19",
        "Fe3O4",
        "magnetite",
        "PIN Ch 11"
      ],
      [
        "N1",
        "KAlSi3O8",
        "orthoclase",
        "NEW, zero-hit verified"
      ],
      [
        "N2",
        "NaAlSiO4",
        "nepheline",
        "NEW, zero-hit verified"
      ],
      [
        "N3",
        "Al6Si2O13",
        "mullite",
        "NEW value, zero-hit; the word mullite is Ch 30 prose, disclosed"
      ],
      [
        "N4",
        "Ca2Al2SiO7·8H2O",
        "strätlingite, a model hydrate",
        "NEW, zero-hit verified, MODEL"
      ],
      [
        "N5",
        "K2SiO3",
        "potassium silicate",
        "NEW, zero-hit verified"
      ],
      [
        "N6",
        "Si4O10",
        "a silica-ring exhibit",
        "NEW, zero-hit verified, EXHIBIT"
      ],
      [
        "N7",
        "K2CaSi2O6",
        "the ash-glass model",
        "NEW, zero-hit verified, MODEL"
      ],
      [
        "I1",
        "Al2O3·2SiO2·2H2O",
        "kaolinite as its oxide sum",
        "ISOMER of P1, never NEW"
      ]
    ];
    let compSum = Z, t2 = 0;
    for (const sp of SP){
      const id = sp[0], f = sp[1], label = sp[2], prov = sp[3];
      const m = massOf(f);
      if (req(m, witnessOf(f))) t2++;
      compSum = radd(compSum, m);
      const vtxt = m[1] === 1n ? myuG(m[0]) + " g/mol (" + m[0].toString() + " myu)" : m[0].toString() + "/" + m[1].toString() + " myu (NON-INTEGER)";
      got.push("PASS " + id + " " + f + " (" + label + ") = " + vtxt + " [" + prov + "]");
    }
    // ---- 14 refusals ----
    const RF = [
      [
        "R1",
        "Ca5(PO4)3OH"
      ],
      [
        "R2",
        "TiO2"
      ],
      [
        "R3",
        "ZrSiO4"
      ],
      [
        "R4",
        "Cr2O3"
      ],
      [
        "R5",
        "LiAlSi2O6"
      ],
      [
        "R6",
        "CaF2"
      ],
      [
        "R7",
        "slip"
      ],
      [
        "R8",
        "grog"
      ],
      [
        "R9",
        "saggar"
      ],
      [
        "R10",
        "terracotta"
      ],
      [
        "R11",
        "stoneware"
      ],
      [
        "R12",
        "porcelain"
      ],
      [
        "R13",
        "CaSO4·0.35H2O"
      ],
      [
        "R14",
        "Al2Si2O5(OH4"
      ]
    ];
    for (const rf of RF){
      const id = rf[0], f = rf[1];
      let reason = null;
      try {
        massOf(f);
      } catch (err) {
        if (err instanceof Refusal) reason = err.message;
        else throw err;
      }
      if (reason === null) got.push("FAIL " + id + " " + f + " NOT REFUSED");
      else {
        let line = "PASS " + id + " " + f + " REFUSED [" + reason + "]";
        if (id === "R1") line = line + " — the twentieth zero-admission gate";
        got.push(line);
      }
    }
    // ---- 9 balances (E9 the must-fail) ----
    const EQ = [
      [
        "E1",
        "Al2Si2O5(OH)4",
        "Al2Si2O7 + 2H2O",
        "kaolinite gives up its structural water"
      ],
      [
        "E2",
        "CaCO3",
        "CaO + CO2",
        "the kiln's calcination rung"
      ],
      [
        "E3",
        "CaO + H2O",
        "Ca(OH)2",
        "slaking"
      ],
      [
        "E4",
        "K2CO3 + SiO2",
        "K2SiO3 + CO2",
        "the feldspar's potash door"
      ],
      [
        "E5",
        "Na2CO3 + SiO2",
        "Na2SiO3 + CO2",
        "the soda-flux door"
      ],
      [
        "E6",
        "3Al2Si2O7",
        "Al6Si2O13 + 4SiO2",
        "metakaolin builds mullite"
      ],
      [
        "E7",
        "Ca(OH)2 + CO2",
        "CaCO3 + H2O",
        "carbonation, the lime round trip"
      ],
      [
        "E8",
        "CaMg(CO3)2",
        "CaO + MgO + 2CO2",
        "dolomite burns twice"
      ]
    ];
    for (const e of EQ){
      const l = sideSum(e[1]), r = sideSum(e[2]);
      if (req(l, r) && l[1] === 1n) got.push("PASS " + e[0] + " " + e[1] + " -> " + e[2] + " (" + e[3] + "): " + l[0].toString() + " myu = " + r[0].toString() + " myu (" + myuG(l[0]) + " g) EXACT");
      else got.push("FAIL " + e[0] + " unbalanced: " + l[0].toString() + "/" + l[1].toString() + " vs " + r[0].toString() + "/" + r[1].toString());
    }
    const gap = rsub(sideSum("Al2Si2O5(OH)4"), sideSum("Al2Si2O7 + H2O"));
    const e9frozen = FROZEN.filter(function(l) {
      return l.indexOf("PASS E9 ") === 0;
    })[0] || "";
    const gapExp = BigInt((/GAP (\d+) myu/.exec(e9frozen) || [
      "",
      "0"
    ])[1]);
    e9Caught = gap[1] === 1n && gap[0] === gapExp;
    if (e9Caught) got.push("PASS E9 Al2Si2O5(OH)4 -> Al2Si2O7 + H2O (one water short) REFUSED: GAP " + gap[0].toString() + " myu (" + myuG(gap[0]) + " g = exactly one H2O) CAUGHT");
    else got.push("FAIL E9 gap " + gap[0].toString() + "/" + gap[1].toString() + " myu vs frozen " + gapExp.toString() + " myu");
    // ---- 3 proportions ----
    const pr1 = fracDp(rdiv(massOf("2H2O"), massOf("Al2Si2O5(OH)4")), 6);
    got.push("PASS PR1 2H2O per gram of kaolinite = 36.03/258.157 = " + pr1 + " g/g [Ch 30 prints 13.96%]");
    const pr2 = fracDp(rdiv(massOf("CO2"), massOf("CaO")), 6);
    got.push("PASS PR2 CO2 per gram of CaO = 44.009/56.077 = " + pr2 + " g/g");
    const pr3 = fracDp(rdiv(massOf("H2O"), massOf("CaO")), 6);
    got.push("PASS PR3 slaking water per gram of CaO = 18.015/56.077 = " + pr3 + " g/g [Ch 21 printed 0.32125, a truncation; the 6dp half-up value governs]");
    // ---- B1 jar test: Ch 5's Stokes register re-derived at full precision ----
    const drho = [
      1652n,
      1n
    ], grav = [
      981n,
      100n
    ], visc = [
      9018n,
      500000n
    ], col = [
      1n,
      10n
    ];
    const d2s = [
      [
        1n,
        4000000n
      ],
      [
        1n,
        400000000n
      ],
      [
        1n,
        1000000000000n
      ]
    ];
    const vOf = function(d2) {
      return rdiv(rmul(rmul(drho, grav), d2), visc);
    };
    const vs = vOf(d2s[0]), vi = vOf(d2s[1]), vc = vOf(d2s[2]);
    const ts = rdiv(col, vs), ti = rdiv(col, vi), tc = rdiv(col, vc);
    const hrs = rdiv(tc, [
      3600n,
      1n
    ]);
    const b1ok = req(rmul(vs, ts), col) && req(rmul(vi, ti), col) && req(rmul(vc, tc), col) && req(rdiv(ti, ts), [
      100n,
      1n
    ]) && req(rdiv(tc, ti), [
      2500n,
      1n
    ]);
    if (b1ok) got.push("PASS B1 jar test, Ch 5's Stokes register re-derived at full precision (drho 1652 kg/m3, g 9.81, eta 1.002e-3, column 0.1 m): sand d = 5e-4 m: v " + sciTrunc(vs) + " m/s, t " + sigSf(ts, 7) + " s; silt d = 5e-5 m: v " + sciTrunc(vi) + " m/s, t " + sigSf(ti, 7) + " s; clay d = 1e-6 m: v " + sciTrunc(vc) + " m/s, t " + sigSf(tc, 7) + " s = " + sigSf(hrs, 6) + " h; v × t = 0.1 m EXACT all three; t-ratios silt/sand 100 and clay/silt 2500 EXACT");
    else got.push("FAIL B1 an exactness check broke: v " + sciTrunc(vs) + "/" + sciTrunc(vi) + "/" + sciTrunc(vc) + " t " + sigSf(ts, 7) + "/" + sigSf(ti, 7) + "/" + sigSf(tc, 7) + " h " + sigSf(hrs, 6));
    // ---- B2 lime round trip ----
    const b2l = sideSum("Ca(OH)2 + CO2"), b2r = sideSum("CaCO3 + H2O");
    if (req(b2l, b2r) && b2l[1] === 1n) got.push("PASS B2 the lime round trip: Ca(OH)2 + CO2 -> CaCO3 + H2O: " + myuG(b2l[0]) + " g = " + myuG(b2r[0]) + " g EXACT (E7's pair)");
    else got.push("FAIL B2 unbalanced");
    // ---- B3 hot mortar, 10.000 kg quicklime basis ----
    const nMol = rdiv([
      10000n,
      1n
    ], perMol("CaO"));
    const wkg = rdiv(rmul(nMol, perMol("H2O")), [
      1000n,
      1n
    ]);
    const ckg = rdiv(rmul(nMol, perMol("CO2")), [
      1000n,
      1n
    ]);
    const cakg = rdiv(rmul(nMol, perMol("CaCO3")), [
      1000n,
      1n
    ]);
    const tin = radd(radd(radd([
      10n,
      1n
    ], wkg), [
      30n,
      1n
    ]), ckg);
    const tout = radd(radd(cakg, wkg), [
      30n,
      1n
    ]);
    if (req(tin, tout)) got.push("PASS B3 hot mortar, 10.000 kg quicklime basis: n = 10000/56.077 = " + fracDp(nMol, 6) + " mol CaO; in 10.000 kg CaO + " + fracDp(wkg, 6) + " kg slaking water + 30.000 kg sand + " + fracDp(ckg, 6) + " kg CO2 = " + fracDp(tin, 6) + " kg; out " + fracDp(cakg, 6) + " kg CaCO3 + " + fracDp(wkg, 6) + " kg H2O + 30.000 kg sand = " + fracDp(tout, 6) + " kg; in = out EXACT");
    else got.push("FAIL B3 in ≠ out: " + fracDp(tin, 6) + " vs " + fracDp(tout, 6));
    // ---- B4 the model ash glaze, oxide masses 1:2:3:14 ----
    const mK = rdiv(U, perMol("K2O"));
    const mCa = rmul([
      2n,
      1n
    ], rdiv(U, perMol("CaO")));
    const mAl = rmul([
      3n,
      1n
    ], rdiv(U, perMol("Al2O3")));
    const mSi = rmul([
      14n,
      1n
    ], rdiv(U, perMol("SiO2")));
    const flux = radd(mK, mCa);
    const uK = rdiv(mK, flux), uCa = rdiv(mCa, flux), uAl = rdiv(mAl, flux), uSi = rdiv(mSi, flux);
    if (req(radd(uK, uCa), U)) got.push("PASS B4 the model ash glaze, oxide masses 1:2:3:14 (K2O:CaO:Al2O3:SiO2, bases 94.195/56.077/101.961/60.083): UMF = " + fracDp(uK, 6) + " / " + fracDp(uCa, 6) + " / " + fracDp(uAl, 6) + " / " + fracDp(uSi, 6) + "; flux unity " + fracDp(uK, 6) + " + " + fracDp(uCa, 6) + " = 1 EXACT");
    else got.push("FAIL B4 flux unity broken");
    // ---- B5 ash glass ----
    const b5l = sideSum("K2CO3 + CaCO3 + 2SiO2"), b5r = sideSum("K2CaSi2O6 + 2CO2");
    if (req(b5l, b5r) && b5l[1] === 1n) got.push("PASS B5 ash glass: K2CO3 + CaCO3 + 2SiO2 -> K2CaSi2O6 + 2CO2: " + b5l[0].toString() + " myu = " + b5r[0].toString() + " myu (" + myuG(b5l[0]) + " g) EXACT");
    else got.push("FAIL B5 unbalanced");
    // ---- B6 slaking heat ----
    const heat = rmul(nMol, [
      65n,
      1n
    ]);
    got.push("PASS B6 slaking heat, Ch 14's band -63.7..-65.2 kJ/mol, ceiling-side working value 65.0: " + fracDp(nMol, 6) + " mol × 65.0 kJ/mol = " + fracDp(heat, 1) + " kJ");
    // ---- X1 dehydroxylation ledger ----
    const kao = massOf("Al2Si2O5(OH)4");
    const w700 = rdiv(rmul([
      700n,
      1n
    ], massOf("2H2O")), kao);
    const m700 = rsub([
      700n,
      1n
    ], w700);
    const w500 = rdiv(rmul([
      500n,
      1n
    ], massOf("2H2O")), kao);
    if (req(radd(w700, m700), [
      700n,
      1n
    ])) got.push("PASS X1 dehydroxylation ledger: 700 g kaolinite -> " + fracDp(w700, 4) + " g water + " + fracDp(m700, 4) + " g metakaolin EXACT; 500 g kaolinite -> " + fracDp(w500, 4) + " g water EXACT (Ch 30's 69.78 g mug case at full precision)");
    else got.push("FAIL X1 ledger broken");
    // ---- X2 hot mortar at one hundred times ----
    const n2 = rdiv([
      1000000n,
      1n
    ], perMol("CaO"));
    const w2 = rdiv(rmul(n2, perMol("H2O")), [
      1000n,
      1n
    ]);
    const c2 = rdiv(rmul(n2, perMol("CO2")), [
      1000n,
      1n
    ]);
    const cc2 = rdiv(rmul(n2, perMol("CaCO3")), [
      1000n,
      1n
    ]);
    const tin2 = radd(radd(radd([
      1000n,
      1n
    ], w2), [
      3000n,
      1n
    ]), c2);
    const tout2 = radd(radd(cc2, w2), [
      3000n,
      1n
    ]);
    if (req(tin2, tout2)) got.push("PASS X2 hot mortar at one hundred times: 1000 kg CaO + " + fracDp(w2, 6) + " kg water + 3000 kg sand + " + fracDp(c2, 6) + " kg CO2 = " + fracDp(tin2, 6) + " kg in; " + fracDp(cc2, 6) + " kg CaCO3 + " + fracDp(w2, 6) + " kg water + 3000 kg sand = " + fracDp(tout2, 6) + " kg out; in = out EXACT");
    else got.push("FAIL X2 in ≠ out: " + fracDp(tin2, 6) + " vs " + fracDp(tout2, 6));
    // ---- X3 mullitization ----
    const x3l = sideSum("3Al2Si2O5(OH)4"), x3r = sideSum("Al6Si2O13 + 4SiO2 + 6H2O");
    if (req(x3l, x3r) && x3l[1] === 1n) got.push("PASS X3 mullitization: 3 Al2Si2O5(OH)4 -> Al6Si2O13 + 4SiO2 + 6H2O: " + x3l[0].toString() + " myu = " + x3r[0].toString() + " myu (" + myuG(x3l[0]) + " g) EXACT");
    else got.push("FAIL X3 unbalanced");
    // ---- X4 dolomite fractions ----
    const dol = massOf("CaMg(CO3)2");
    const pCa = fracDp(rdiv(rmul(massOf("CaO"), [
      100n,
      1n
    ]), dol), 4);
    const pMg = fracDp(rdiv(rmul(massOf("MgO"), [
      100n,
      1n
    ]), dol), 4);
    const pCo = fracDp(rdiv(rmul(massOf("2CO2"), [
      100n,
      1n
    ]), dol), 4);
    const x4ok = req(radd(radd(rdiv(massOf("CaO"), dol), rdiv(massOf("MgO"), dol)), rdiv(massOf("2CO2"), dol)), U);
    if (x4ok) got.push("PASS X4 dolomite fractions: CaO " + pCa + "% + MgO " + pMg + "% + CO2 " + pCo + "% = 100% at full precision EXACT");
    else got.push("FAIL X4 fractions do not sum to 100%");
    // ---- T1 checksum, T2 containment cross-check ----
    const t1frozen = FROZEN.filter(function(l) {
      return l.indexOf("PASS T1 ") === 0;
    })[0] || "";
    const hand = BigInt((/hand-sum (\d+) myu/.exec(t1frozen) || [
      "",
      "0"
    ])[1]);
    const csumTxt = compSum[1] === 1n ? compSum[0].toString() : compSum[0].toString() + "/" + compSum[1].toString();
    if (compSum[1] === 1n && compSum[0] === hand) got.push("PASS T1 composition checksum: engine sum " + csumTxt + " myu over 35 rows = hand-sum " + hand.toString() + " myu MATCH");
    else got.push("FAIL T1 engine sum " + csumTxt + " myu vs hand-sum " + hand.toString() + " myu");
    if (t2 === 35) got.push("PASS T2 containment rescan: lane-2 products vs lane-1 on all 35 species: " + t2 + "/35 ALL MATCH");
    else got.push("FAIL T2 lane-2 matches " + t2 + "/35");
    // ---- review comparison: computed vs frozen, row by row ----
    if (FROZEN.length !== 73) throw new Error("frozen battery must hold 73 rows, got " + FROZEN.length);
    if (got.length !== 73) throw new Error("computed battery must hold 73 rows, got " + got.length);
    const out = [];
    let pass = 0;
    const fails = [];
    for(let i = 0; i < 73; i++){
      if (got[i] === FROZEN[i]) {
        out.push(got[i]);
        pass++;
      } else {
        const id = FROZEN[i].split(" ")[1];
        fails.push(id);
        out.push("FAIL " + id + " got [" + got[i] + "] expected [" + FROZEN[i] + "]");
      }
    }
    return {
      rows: out,
      pass: pass,
      fails: fails,
      e9Caught: e9Caught,
      t2: t2
    };
  }
```

## 8. Session 129 close summary

FC9 REVIEWED — **PASS CLEAN**. Engine 42 (the event-sorted sweep review compositor, fresh build, zero code shared with Engines 1–41) re-executed the whole frozen 73-row battery to **73/73 PASS — CLEAN**, G1 MATCH / G2 canary CAUGHT at S1 / G3 determinism HELD / G4 must-fail CAUGHT at exactly one H2O — with the review's honest history on the record: a typed-run crash, a 72/73 and a 71/73 each caught at their own named lines (the vOf ÷18 slip and 1e14 clay denominator; the unsigned-power decade throw and X2's dropped sand clause), the fixes verified in isolation and the engine re-typed per the session-127 precedent, one further display-harness defect caught by the row-level compare before any freeze, then the clean run — no frozen expectation patched at any point in the chain. All 19 pins re-grepped in their owners' pages with the SELF owners and PR3's anchor; the stress/balance anchors re-verified; the seven NEW values and six words re-proven zero-hit at the review HEAD with the three disclosed catches standing; the [convergent] battery re-confirmed at named sources, zero corrections owed. Ex FC9.6's withheld ◆ answer delivered at the Revision Appendix. The canvas stands per extend-never-rewrite with its appendix; the web edition re-rendered under the validated renderer; the record closes with the ALWAYS-SYNC push of this record, the amended master, its web edition, and the project records.
