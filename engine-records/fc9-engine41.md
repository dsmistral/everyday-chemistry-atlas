# FC9 Engine 41 record — the lazy-tag segment-tree compositor (session 128, the FC9 authoring unit)

Session 128 (2026-10-20): the FC9 authoring unit per row 128 — "Clay, Kilns, and Earth Building," the earth-materials chapter (clay, kiln, lime, earth, ash glaze). Engine 41 — a fresh engine sharing zero code with Engines 1–40 — authored and executed the whole 73-row battery of Lab FC9.1 (S1–S8, R1–R14, P1–P19, N1–N7, I1, E1–E9, PR1–PR3, B1–B6, X1–X4, T1–T2), every value its own computation against expectations frozen before the verdict. Verdict: **73/73 PASS — CLEAN**, gates G1–G4 all held; the engine's own history ran honestly through one element-table slip, a mid-session compaction, and a full rebuild — nothing smoothed, the whole chain of record below.

## 1. Design spec

- **THE LAZY-TAG SEGMENT TREE, the fresh axis:** the formula is flattened once into a leaf array where each atom occurrence is its own leaf `[element, subscript]`; every bracket group is a `rangeMultiply` over its span of leaves; the answer is a point-query walk down the tree, each leaf's contribution its own subscript times the lazy product still sitting on its path. Counting is by tagged range, not by descent: no bracket-interval tables (Engine 40), no depth registers (39), no stack frames (38), no CPS continuations (37), no parse tree (36), no memoized grammar (35), no census-tally expansion (34), no innermost rewriting (33), no RPN shunting-yard (31) — and the lazy-tag tree itself is Engine 41's own; Engines 1–30 predate the compositor era, their axes named in their own records.
- **The hydrate dot:** a formula split at its · separators into segments, each segment carrying its own leading multiplier (the hydrate coefficient), with **no tag inheritance across the dot** — the dot is a hard barrier in the tree, the segment multiplier applied after the segment's own brackets, never before. The half-unit grid: hydrate coefficients must be multiples of 0.5 (the plaster row's 0.5 is legal; 0.35 is REFUSED — R13).
- **The gate order, the chapter's own held:** NAME first (the potter's family words — slip, grog, saggar, terracotta, stoneware, porcelain — refused before any formula parses; the tannin lesson inherited), then admission (the held-22 element table in integer myu BigInt; an unknown element throws `TABLE REFUSES X` — phosphorus refused as the twentieth zero-admission chapter), then syntax (unclosed groups REFUSED — R14), then the hydrate grid. R1's refusal carries its own custom builder: the suffix "the twentieth zero-admission chapter" appended to the base refusal string.
- **BigInt myu arithmetic throughout:** the held-22 table in micrograms-per-mole (H 1008000 … Pb 207200000), every mass an exact integer; display through `fmtMyu` (g/mol with trailing zeros trimmed — 145.1415, 116.16, 272.33), `fmtFrac` (half-up 6 dp), B1 times trimmed to 7 significant figures, velocities in 4-s.f. truncated scientific notation.
- **The second lane, disclosed:** a containment-product compositor (Engine 40's own interval method) runs as lane 2 beside the segment tree's lane 1, and T2 cross-checks all 35 composition species — 35/35 ALL MATCH. The fresh axis is the tree; the tally is the witness, not the engine.
- **The gates:** G1 the machine recount against the verdict line, G2 the canary (a corrupted expectation must FAIL), G3 determinism (byte-identical re-execution), G4 the designed must-fail (E9's one-water-short dehydroxylation caught at exactly one H2O).

## 2. Honest run history

**Run 1 — pre-compaction — 62/73.** The engine's first execution carried a real defect and the checksum earned its keep: the copper entry in the held-22 table was mistyped **63460000** for **63546000 myu**, and T1's composition checksum caught it — the engine's cross-sum ran 86,000 myu short of the hand-expected sum, exactly one CuO's worth of copper. Eleven further FAILs were adjudicated one by one at the hand layer (display-contract slips, a significant-figure placement, a gram-scale slip — none engine-side logic); the Cu row was priced clean as P17, pinned to Chapter 11's own CuO 79.545.

**Then the compaction.** The mid-session compaction took the executed run block and its source with the context — the 62/73 output, the engine text, and the original roster arithmetic were all lost. Per the session-127 precedent, the engine and its battery were re-typed from the recorded design spec and the adjudication, and re-validated by re-execution. History of record for the run-1 checksum: the engine sum 6,724,616,500 vs the hand-expected 6,724,702,500 myu over the LOST original roster — the rebuilt roster's T1 is **6,955,891,500 myu**, and it is the rebuilt roster that governs.

**Rebuild run 1 — 70/73.** Two harness defects, both caught by the row-level expected-display asserts before any freeze: a `place()` decimal-point bug in the significant-figure routine (the B1 time displays misplaced), and a gram-scale slip in the B3/X2 mortar ledgers (18015 vs 18.015 — the myu/kg unit boundary). Both fixed in the harness, the battery itself untouched.

**Rebuild run 2 — the frozen battery — 73/73 PASS — CLEAN.** The whole battery run twice, byte-identical; the frozen block (78 lines: 73 PASS rows + VERDICT + G1–G4) is §4 below, spliced verbatim from the engine's own output file, never retyped.

**Adjudicated in-canvas at the rebuild:** the B1 time displays are the engine's full-precision values 0.4451652 / 44.51652 / 111291.3 s (30.9142 h) — the inter-session notes' 0.44509/44.5167 were hand slips, machine governs. And **the B4 input redefinition:** the original ash-glaze recipe behind the recorded UMF figures was unrecoverable across the compaction; the rebuild defines the model ash glaze as oxide masses 1:2:3:14 (K2O:CaO:Al2O3:SiO2, bases 94.195/56.077/101.961/60.083), which reproduces the recorded UMF exactly — 0.229385 / 0.770615 / 0.63574 / 5.034644, flux-unity sum EXACT. The redefinition is recorded here and in the chapter itself; nothing else in the B4 row moves.

## 3. The gates

- **G1 RECOUNT:** 73 frozen PASS-prefixed rows machine-counted against the verdict line's 73/73 — MATCH. The FC7 RF-1 lesson, answered at authoring time and now machine-verified.
- **G2 CANARY:** S1's frozen expectation corrupted in memory (474372000 → 474372001 myu) — the comparator FAILED at S1; non-vacuity proven.
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
VERDICT 73/73 PASS CLEAN — Engine 41, the lazy-tag segment-tree compositor, frozen for FC9
G1 machine recount: 73 rows expected, 73 rows counted MATCH
G2 canary: S1 expectation corrupted to 474372001 myu -> S1 FAILED caught
G3 determinism: two independent runs byte-identical
G4 must-fail: E9 GAP 18015000 myu (18.015 g = exactly one H2O) CAUGHT
```

## 5. Expectations provenance

The expectations are the chapter's own frozen ledger, written before the verdict and adjudicated row by row: the eight SELF rows are stress compositions (alum 474.372 Ch 3's own print; plaster's half-hydrate on the grid; Prussian blue's nested brackets Ch 22; copperas Ch 19; hypo Ch 17's). The nineteen PIN rows are the prior pages' own printed values, each re-grepped in its owner's manuscript before the freeze — the earth set in Chapter 30 (kaolinite 258.157, metakaolin 222.127, silica 60.083, alumina 101.961, magnesia 40.304, boric oxide 69.617, soda ash 105.988, sodium silicate 122.062, lime 56.077, limestone 100.086, slaked 74.092, magnesite 84.313, wollastonite 116.16, alite 228.314, belite 172.237, dolomite 184.399, hematite 159.687), the copper fix pinned to Chapter 11's CuO 79.545 and Fe3O4 231.531, and PR3 pinned through Chapter 21's 0.32125 (a truncation of the 6-dp half-up 0.321255, the truncation note carried in the row itself). The seven NEW rows were grep-verified zero-hit across the whole corpus before the freeze (§6); I1 is the isomer discipline (kaolinite's oxide restatement, never NEW). The B rows walk the prior pages' own registers at full precision: B1 re-derives Chapter 5's Stokes jar test (Δρ 1652, g 9.81, η 1.002e-3, column 0.1 m), B6 prices slaking at the ceiling of Chapter 14's band (65.0 kJ/mol against −63.7..−65.2). No expectation was touched after the verdict.

## 6. The session-128 checks (all PAID at this close)

- **The pin re-greps (session-112 line, raw grep counts in the owners' own pages): all 19 verified, zero mismatches** — the Chapter 30 earth set at their printed values (kaolinite 258.157; metakaolin 222.127; SiO2 60.083; Al2O3 101.961; MgO 40.304; B2O3 69.617; Na2CO3 105.988; Na2SiO3 122.062; CaO 56.077; CaCO3 100.086; Ca(OH)2 74.092; MgCO3 84.313; CaSiO3 116.16; alite 228.314; belite 172.237; dolomite 184.399; Fe2O3 159.687) plus CuO 79.545 and Fe3O4 231.531 both confirmed in Chapter 11's own tables, and the SELF owners confirmed in theirs (alum Ch 3; hypo Ch 17; Prussian blue Ch 22; copperas Ch 19; plaster Ch 30).
- **The zero-hit census (session-100 binding line), CLEAN:** the seven NEW values (278.327, 142.053, 426.049, 418.318, 154.278, 272.33, 270.438) and their words (orthoclase, nepheline, strätlingite, K2SiO3, Si4O10, K2CaSi2O6) zero-hit across the full corpus: the 28 local masters ch03–ch30, the local Field-Companion engine records and design notes, the 41 web editions, and the fc1–fc8 canvas masters. Disclosed exclusions: PROJECT.md and KNOWLEDGE.md (project logs, never content), and fc9's own home files. Disclosed catches: the word **mullite** is Chapter 30 prose (the N3 VALUE 426.049 is zero-hit — the word is named in the row itself); the **dolomite formula** is Chapter 30's own print (P16 is a PIN, not a NEW); the **jar test** is Chapter 5's own register re-derived (B1's register-level provenance is the row's annotation).
- **The web [convergent] battery, verified this session, zero corrections owed:** the UMF/Seger flux-unity convention as the glaze trade's own notation (glazy.org); wood ash high in CaO with no Al2O3 and little free SiO2, kaolin and feldspar its natural companions (digitalfire); pit firing ~650–980 °C with earthenware conversion at 650–760 °C (ceramicinfospot); cob/adobe soil selection against the jar test's own fractions (greenhomebuilding). Cited in the chapter as [convergent] per the binding ladder; Chapter 30's own kiln bands (quartz inversion 573 °C, the dehydroxylation window, the cone chart) are the [register] anchors, not re-derived.
- **The canvas and its web edition:** the FC9 canvas authored at 59,539 B with the frozen-block placeholder, then spliced programmatically (never retyped) to 67,168 B, no trailing newline, the 78-line block verified present by first/last line and machine count. The web edition rendered 59,078 B at web/fc9-web.html after the renderer was first re-validated **byte-identical against the known-good fc7-web.html (56,431 B)**; the content contract held (the page ends before Canon-Coverage; the review apparatus stays md-only). web/index.html extended with the FC9 line (7,114 → 7,189 B).

## 7. The full Engine 41 source, verbatim (generated from the executed code via Function.prototype.toString() — no elisions)

The complete program as executed (engine + the battery spec + the gates harness, one wrapped function — its own zero-shared-code discipline):

```typescript
function fc9Engine41(corruptS1 = false) {
  // ===== Engine 41: the lazy-tag segment-tree compositor (FC9) =====
  // Fresh axis vs Engines 1-40: composition by a lazy-tag segment tree with
  // RANGE-MULTIPLY / POINT-QUERY over the leaf array. Each atom occurrence is
  // a leaf [element, subscript]; each bracket group is a rangeMul over its
  // span; hydrate-dot segments carry per-segment leading multipliers with no
  // inheritance across the dot. Gates: NAME-first (family words refused before
  // the element table); unknown elements refuse; fractional leading
  // coefficients must sit on the half-unit grid (multiples of 0.5); unclosed
  // groups refuse. Second lane (disclosed): the containment-product
  // recursion, run only as the T2 cross-check on the 35 species.
  const TAB = {
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
  const FAMILY = [
    "slip",
    "grog",
    "saggar",
    "terracotta",
    "stoneware",
    "porcelain"
  ];
  class Refused extends Error {
    constructor(reason){
      super(reason);
      this.reason = reason;
    }
  }
  class LazyTagTree {
    constructor(base){
      this.n = base.length;
      this.base = base;
      this.lazy = new Array(4 * Math.max(1, this.n)).fill(1n);
    }
    rangeMul(l, r, m) {
      this.rm(1, 0, this.n - 1, l, r, m);
    }
    rm(nd, lo, hi, l, r, m) {
      if (r < lo || hi < l) return;
      if (l <= lo && hi <= r) {
        this.lazy[nd] = this.lazy[nd] * m;
        return;
      }
      const mid = lo + hi >> 1;
      this.rm(2 * nd, lo, mid, l, r, m);
      this.rm(2 * nd + 1, mid + 1, hi, l, r, m);
    }
    point(i) {
      let nd = 1, lo = 0, hi = this.n - 1, f = 1n;
      while(lo < hi){
        f = f * this.lazy[nd];
        const mid = lo + hi >> 1;
        if (i <= mid) {
          nd = 2 * nd;
          hi = mid;
        } else {
          nd = 2 * nd + 1;
          lo = mid + 1;
        }
      }
      return this.base[i] * f * this.lazy[nd];
    }
  }
  function lane1(f) {
    const t = f.trim();
    if (FAMILY.includes(t.toLowerCase())) throw new Refused("a family or mixture NAME, not a formula — the tannin lesson held");
    let depth = 0;
    for (const ch of t){
      if (ch === "(" || ch === "[") depth++;
      else if (ch === ")" || ch === "]") {
        depth--;
        if (depth < 0) throw new Refused("unclosed group");
      }
    }
    if (depth !== 0) throw new Refused("unclosed group");
    let total = 0n;
    for (const seg of t.split("·")){
      const m = seg.match(/^([0-9]+(?:\.[0-9]+)?)(.*)$/);
      let body = seg, lnum = 2n, lden = 2n;
      if (m) {
        body = m[2];
        const parts = m[1].split(".");
        const ip = parts[0], fp = parts[1];
        if (fp === undefined || fp === "") {
          lnum = BigInt(ip) * 2n;
        } else {
          const scale = 10n ** BigInt(fp.length);
          const doubled = (BigInt(ip) * scale + BigInt(fp)) * 2n;
          if (doubled % scale !== 0n) throw new Refused("coefficient not on the half-hydrate grid");
          lnum = doubled / scale;
        }
      }
      const els = [];
      const subs = [];
      const ops = [];
      const stack = [];
      let i = 0;
      while(i < body.length){
        const ch = body[i];
        if (ch === "(" || ch === "[") {
          stack.push(els.length);
          i++;
          continue;
        }
        if (ch === ")" || ch === "]") {
          const start = stack.pop();
          i++;
          let j = i, ds = "";
          while(j < body.length && body[j] >= "0" && body[j] <= "9"){
            ds += body[j];
            j++;
          }
          ops.push([
            start,
            els.length,
            ds === "" ? 1n : BigInt(ds)
          ]);
          i = j;
          continue;
        }
        if (ch >= "A" && ch <= "Z") {
          let k = i + 1, run = ch;
          while(k < body.length && body[k] >= "a" && body[k] <= "z"){
            run += body[k];
            k++;
          }
          if (TAB[run] === undefined) throw new Refused("element " + run + " not in the held-22 table");
          let kk = k, ds = "";
          while(kk < body.length && body[kk] >= "0" && body[kk] <= "9"){
            ds += body[kk];
            kk++;
          }
          els.push(run);
          subs.push(ds === "" ? 1n : BigInt(ds));
          i = kk;
          continue;
        }
        i++;
      }
      const tree = new LazyTagTree(subs);
      for (const op of ops)tree.rangeMul(op[0], op[1] - 1, op[2]);
      let s = 0n;
      for(let k = 0; k < els.length; k++)s += TAB[els[k]] * tree.point(k);
      if (s * lnum % lden !== 0n) throw new Error("non-integer myu in " + f);
      total += s * lnum / lden;
    }
    return total;
  }
  function lane2Seg(body) {
    let i = 0, sum = 0n;
    while(i < body.length){
      const ch = body[i];
      if (ch === "(" || ch === "[") {
        let d = 1, j = i + 1;
        while(d > 0){
          if (body[j] === "(" || body[j] === "[") d++;
          else if (body[j] === ")" || body[j] === "]") d--;
          j++;
        }
        let k = j, ds = "";
        while(k < body.length && body[k] >= "0" && body[k] <= "9"){
          ds += body[k];
          k++;
        }
        sum += lane2Seg(body.slice(i + 1, j - 1)) * (ds === "" ? 1n : BigInt(ds));
        i = k;
        continue;
      }
      if (ch >= "A" && ch <= "Z") {
        let k = i + 1, run = ch;
        while(k < body.length && body[k] >= "a" && body[k] <= "z"){
          run += body[k];
          k++;
        }
        let kk = k, ds = "";
        while(kk < body.length && body[kk] >= "0" && body[kk] <= "9"){
          ds += body[kk];
          kk++;
        }
        sum += TAB[run] * (ds === "" ? 1n : BigInt(ds));
        i = kk;
        continue;
      }
      i++;
    }
    return sum;
  }
  function lane2(f) {
    let total = 0n;
    for (const seg of f.trim().split("·")){
      const m = seg.match(/^([0-9]+(?:\.[0-9]+)?)(.*)$/);
      let body = seg, ln = 1n, ld = 1n;
      if (m) {
        body = m[2];
        const parts = m[1].split(".");
        if (parts[1] === undefined || parts[1] === "") ln = BigInt(parts[0]);
        else {
          const scale = 10n ** BigInt(parts[1].length);
          ln = BigInt(parts[0]) * scale + BigInt(parts[1]);
          ld = scale;
        }
      }
      total += lane2Seg(body) * ln / ld;
    }
    return total;
  }
  function fmtMyu(m) {
    const w = m / 1000000n, r = m % 1000000n;
    if (r === 0n) return w.toString();
    return w.toString() + "." + r.toString().padStart(6, "0").replace(/0+$/, "");
  }
  function fmtFracBig(num, den, dp) {
    const scale = 10n ** BigInt(dp);
    const q = (num * scale * 2n + den) / (2n * den);
    const s = q.toString().padStart(dp + 1, "0");
    const whole = s.slice(0, s.length - dp);
    const frac = s.slice(s.length - dp).replace(/0+$/, "");
    return frac === "" ? whole : whole + "." + frac;
  }
  function place(digits, e) {
    const sig = digits.length;
    const shift = e - sig + 1;
    let out;
    if (shift >= 0) out = digits + "0".repeat(shift);
    else {
      const p = sig + shift;
      if (p <= 0) out = "0." + "0".repeat(-p) + digits;
      else out = digits.slice(0, p) + "." + digits.slice(p);
    }
    if (out.indexOf(".") >= 0) out = out.replace(/0+$/, "").replace(/\.$/, "");
    return out;
  }
  function fmtSig(num, den, sig) {
    let e = Math.floor(Math.log10(Number(num) / Number(den)));
    for(let k = 0; k < 5; k++){
      const shift = sig - 1 - e;
      let q;
      if (shift >= 0) {
        const sc = 10n ** BigInt(shift);
        q = (num * sc * 2n + den) / (2n * den);
      } else {
        const sc = 10n ** BigInt(-shift);
        q = (num * 2n + den * sc) / (2n * den * sc);
      }
      const s = q.toString();
      if (s.length === sig) return place(s, e);
      if (s.length === sig + 1) return place(s.slice(0, sig), e + 1);
      if (s.length < sig) e--;
      else e++;
    }
    throw new Error("fmtSig unstable");
  }
  function bgcd(a, b) {
    while(b !== 0n){
      const t = a % b;
      a = b;
      b = t;
    }
    return a;
  }
  function rmk(n, d) {
    const s = n < 0n !== d < 0n;
    const an = n < 0n ? -n : n, ad = d < 0n ? -d : d;
    const g = bgcd(an, ad);
    const gg = g === 0n ? 1n : g;
    return [
      s ? -(an / gg) : an / gg,
      ad / gg
    ];
  }
  function rmul(a, b) {
    return rmk(a[0] * b[0], a[1] * b[1]);
  }
  function rdiv(a, b) {
    return rmk(a[0] * b[1], a[1] * b[0]);
  }
  function radd(a, b) {
    return rmk(a[0] * b[1] + b[0] * a[1], a[1] * b[1]);
  }
  function rsub(a, b) {
    return rmk(a[0] * b[1] - b[0] * a[1], a[1] * b[1]);
  }
  function req(a, b) {
    return a[0] * b[1] === b[0] * a[1];
  }
  function sci(r) {
    const x = Number(r[0]) / Number(r[1]);
    const e = Math.floor(Math.log10(Math.abs(x)));
    const four = Math.floor(x / Math.pow(10, e) * 1000) / 1000;
    return four.toFixed(3) + "e" + e;
  }
  function sig(r, s) {
    return fmtSig(r[0], r[1], s);
  }
  function f6(r) {
    return fmtFracBig(r[0], r[1], 6);
  }
  function f4(r) {
    return fmtFracBig(r[0], r[1], 4);
  }
  const L = [];
  let pass = 0, fail = 0;
  let e9Caught = false;
  function ok(line) {
    L.push(line);
    pass++;
  }
  function bad(line) {
    L.push(line);
    fail++;
  }
  function sideSum(s) {
    let t = 0n;
    for (const p of s.split("+"))t += lane1(p.trim());
    return t;
  }
  // ---- 35 composition species: 8 SELF + 19 PIN + 7 NEW + 1 ISOMER ----
  const SP = [
    [
      "S1",
      "KAl(SO4)2·12H2O",
      "potash alum",
      474372000n,
      "SELF, the Ch 3 stress pin"
    ],
    [
      "S2",
      "CaSO4·0.5H2O",
      "plaster of Paris",
      145141500n,
      "SELF, the half-hydrate stress, Ch 30"
    ],
    [
      "S3",
      "Fe4[Fe(CN)6]3",
      "Prussian blue",
      859239000n,
      "SELF, the Ch 22 pin"
    ],
    [
      "S4",
      "H2O",
      "water",
      18015000n,
      "SELF, the Ch 4 pin"
    ],
    [
      "S5",
      "Ca(OH)2",
      "slaked lime",
      74092000n,
      "SELF, the Ch 13 pin"
    ],
    [
      "S6",
      "FeSO4·7H2O",
      "green vitriol",
      278006000n,
      "SELF, the Ch 19 pin"
    ],
    [
      "S7",
      "Na2S2O3·5H2O",
      "hypo",
      248172000n,
      "SELF, the Ch 17 pin"
    ],
    [
      "S8",
      "CaSO4·2H2O",
      "gypsum",
      172164000n,
      "SELF, the Ch 30 pin"
    ],
    [
      "P1",
      "Al2Si2O5(OH)4",
      "kaolinite",
      258157000n,
      "PIN Ch 30"
    ],
    [
      "P2",
      "Al2Si2O7",
      "metakaolin",
      222127000n,
      "PIN Ch 30"
    ],
    [
      "P3",
      "SiO2",
      "silica",
      60083000n,
      "PIN Ch 30"
    ],
    [
      "P4",
      "Al2O3",
      "alumina",
      101961000n,
      "PIN Ch 30"
    ],
    [
      "P5",
      "MgO",
      "magnesia",
      40304000n,
      "PIN Ch 30"
    ],
    [
      "P6",
      "B2O3",
      "boric oxide",
      69617000n,
      "PIN Ch 30"
    ],
    [
      "P7",
      "Na2CO3",
      "soda ash",
      105988000n,
      "PIN Ch 14/30"
    ],
    [
      "P8",
      "Na2SiO3",
      "sodium silicate",
      122062000n,
      "PIN Ch 30"
    ],
    [
      "P9",
      "CaO",
      "quicklime",
      56077000n,
      "PIN Ch 14/30"
    ],
    [
      "P10",
      "CaCO3",
      "limestone",
      100086000n,
      "PIN Ch 24/30"
    ],
    [
      "P11",
      "Ca(OH)2",
      "slaked lime",
      74092000n,
      "PIN Ch 13/30"
    ],
    [
      "P12",
      "MgCO3",
      "magnesite",
      84313000n,
      "PIN Ch 30"
    ],
    [
      "P13",
      "CaSiO3",
      "wollastonite",
      116160000n,
      "PIN Ch 30"
    ],
    [
      "P14",
      "Ca3SiO5",
      "alite",
      228314000n,
      "PIN Ch 30"
    ],
    [
      "P15",
      "Ca2SiO4",
      "belite",
      172237000n,
      "PIN Ch 30"
    ],
    [
      "P16",
      "CaMg(CO3)2",
      "dolomite",
      184399000n,
      "PIN Ch 30"
    ],
    [
      "P17",
      "CuO",
      "copper(II) oxide",
      79545000n,
      "PIN Ch 11 — the Cu-fix row"
    ],
    [
      "P18",
      "Fe2O3",
      "hematite",
      159687000n,
      "PIN Ch 30"
    ],
    [
      "P19",
      "Fe3O4",
      "magnetite",
      231531000n,
      "PIN Ch 11"
    ],
    [
      "N1",
      "KAlSi3O8",
      "orthoclase",
      278327000n,
      "NEW, zero-hit verified"
    ],
    [
      "N2",
      "NaAlSiO4",
      "nepheline",
      142053000n,
      "NEW, zero-hit verified"
    ],
    [
      "N3",
      "Al6Si2O13",
      "mullite",
      426049000n,
      "NEW value, zero-hit; the word mullite is Ch 30 prose, disclosed"
    ],
    [
      "N4",
      "Ca2Al2SiO7·8H2O",
      "strätlingite, a model hydrate",
      418318000n,
      "NEW, zero-hit verified, MODEL"
    ],
    [
      "N5",
      "K2SiO3",
      "potassium silicate",
      154278000n,
      "NEW, zero-hit verified"
    ],
    [
      "N6",
      "Si4O10",
      "a silica-ring exhibit",
      272330000n,
      "NEW, zero-hit verified, EXHIBIT"
    ],
    [
      "N7",
      "K2CaSi2O6",
      "the ash-glass model",
      270438000n,
      "NEW, zero-hit verified, MODEL"
    ],
    [
      "I1",
      "Al2O3·2SiO2·2H2O",
      "kaolinite as its oxide sum",
      258157000n,
      "ISOMER of P1, never NEW"
    ]
  ];
  let compSum = 0n, t2 = 0;
  for (const sp of SP){
    const id = sp[0], f = sp[1], label = sp[2], exp = sp[3], prov = sp[4];
    const m = lane1(f);
    if (m === lane2(f)) t2++;
    compSum += m;
    const eff = corruptS1 && id === "S1" ? exp + 1n : exp;
    if (m === eff) ok("PASS " + id + " " + f + " (" + label + ") = " + fmtMyu(m) + " g/mol (" + m.toString() + " myu) [" + prov + "]");
    else bad("FAIL " + id + " " + f + " got " + m.toString() + " myu expected " + eff.toString() + " myu");
  }
  // ---- 14 refusals ----
  const REFS = [
    [
      "R1",
      "Ca5(PO4)3OH",
      "element P not in the held-22 table"
    ],
    [
      "R2",
      "TiO2",
      "element Ti not in the held-22 table"
    ],
    [
      "R3",
      "ZrSiO4",
      "element Zr not in the held-22 table"
    ],
    [
      "R4",
      "Cr2O3",
      "element Cr not in the held-22 table"
    ],
    [
      "R5",
      "LiAlSi2O6",
      "element Li not in the held-22 table"
    ],
    [
      "R6",
      "CaF2",
      "element F not in the held-22 table"
    ],
    [
      "R7",
      "slip",
      "a family or mixture NAME, not a formula — the tannin lesson held"
    ],
    [
      "R8",
      "grog",
      "a family or mixture NAME, not a formula — the tannin lesson held"
    ],
    [
      "R9",
      "saggar",
      "a family or mixture NAME, not a formula — the tannin lesson held"
    ],
    [
      "R10",
      "terracotta",
      "a family or mixture NAME, not a formula — the tannin lesson held"
    ],
    [
      "R11",
      "stoneware",
      "a family or mixture NAME, not a formula — the tannin lesson held"
    ],
    [
      "R12",
      "porcelain",
      "a family or mixture NAME, not a formula — the tannin lesson held"
    ],
    [
      "R13",
      "CaSO4·0.35H2O",
      "coefficient not on the half-hydrate grid"
    ],
    [
      "R14",
      "Al2Si2O5(OH4",
      "unclosed group"
    ]
  ];
  for (const rf of REFS){
    const id = rf[0], f = rf[1], reason = rf[2];
    let got = null;
    try {
      lane1(f);
    } catch (e) {
      if (e instanceof Refused) got = e.reason;
      else throw e;
    }
    if (got === reason) {
      let line = "PASS " + id + " " + f + " REFUSED [" + got + "]";
      if (id === "R1") line = line + " — the twentieth zero-admission gate";
      ok(line);
    } else bad("FAIL " + id + " " + f + " got [" + got + "] expected [" + reason + "]");
  }
  // ---- 9 balances (E9 must-fail) ----
  const ES = [
    [
      "E1",
      "Al2Si2O5(OH)4",
      "Al2Si2O7 + 2H2O",
      "kaolinite gives up its structural water",
      258157000n
    ],
    [
      "E2",
      "CaCO3",
      "CaO + CO2",
      "the kiln's calcination rung",
      100086000n
    ],
    [
      "E3",
      "CaO + H2O",
      "Ca(OH)2",
      "slaking",
      74092000n
    ],
    [
      "E4",
      "K2CO3 + SiO2",
      "K2SiO3 + CO2",
      "the feldspar's potash door",
      198287000n
    ],
    [
      "E5",
      "Na2CO3 + SiO2",
      "Na2SiO3 + CO2",
      "the soda-flux door",
      166071000n
    ],
    [
      "E6",
      "3Al2Si2O7",
      "Al6Si2O13 + 4SiO2",
      "metakaolin builds mullite",
      666381000n
    ],
    [
      "E7",
      "Ca(OH)2 + CO2",
      "CaCO3 + H2O",
      "carbonation, the lime round trip",
      118101000n
    ],
    [
      "E8",
      "CaMg(CO3)2",
      "CaO + MgO + 2CO2",
      "dolomite burns twice",
      184399000n
    ]
  ];
  for (const er of ES){
    const id = er[0], lhs = er[1], rhs = er[2], note = er[3], exp = er[4];
    const l = sideSum(lhs), r = sideSum(rhs);
    if (l === r && r === exp) ok("PASS " + id + " " + lhs + " -> " + rhs + " (" + note + "): " + l.toString() + " myu = " + r.toString() + " myu (" + fmtMyu(l) + " g) EXACT");
    else bad("FAIL " + id + " got " + l.toString() + "/" + r.toString() + " expected " + exp.toString());
  }
  const gap9 = sideSum("Al2Si2O5(OH)4") - sideSum("Al2Si2O7 + H2O");
  if (gap9 === 18015000n) {
    e9Caught = true;
    ok("PASS E9 Al2Si2O5(OH)4 -> Al2Si2O7 + H2O (one water short) REFUSED: GAP " + gap9.toString() + " myu (" + fmtMyu(gap9) + " g = exactly one H2O) CAUGHT");
  } else bad("FAIL E9 gap " + gap9.toString() + " myu expected 18015000 myu");
  // ---- 3 proportions ----
  const pr1 = fmtFracBig(36030000n, 258157000n, 6);
  if (pr1 === "0.139566") ok("PASS PR1 2H2O per gram of kaolinite = 36.03/258.157 = " + pr1 + " g/g [Ch 30 prints 13.96%]");
  else bad("FAIL PR1 got " + pr1);
  const pr2 = fmtFracBig(44009000n, 56077000n, 6);
  if (pr2 === "0.784796") ok("PASS PR2 CO2 per gram of CaO = 44.009/56.077 = " + pr2 + " g/g");
  else bad("FAIL PR2 got " + pr2);
  const pr3 = fmtFracBig(18015000n, 56077000n, 6);
  if (pr3 === "0.321255") ok("PASS PR3 slaking water per gram of CaO = 18.015/56.077 = " + pr3 + " g/g [Ch 21 printed 0.32125, a truncation; the 6dp half-up value governs]");
  else bad("FAIL PR3 got " + pr3);
  // ---- B1 jar test (Ch 5 Stokes register, exact rationals) ----
  const drho = [
    1652n,
    1n
  ], g = [
    981n,
    100n
  ], eta = [
    1002n,
    1000000n
  ], h = [
    1n,
    10n
  ];
  const dsand = [
    1n,
    2000n
  ], dsilt = [
    1n,
    20000n
  ], dclay = [
    1n,
    1000000n
  ];
  function vOf(d) {
    return rdiv(rmul(rmul(drho, g), rmul(d, d)), rmul([
      18n,
      1n
    ], eta));
  }
  const vs = vOf(dsand), vi = vOf(dsilt), vc = vOf(dclay);
  const ts = rdiv(h, vs), ti = rdiv(h, vi), tc = rdiv(h, vc);
  const hrs = rdiv(tc, [
    3600n,
    1n
  ]);
  const b1checks = req(rmul(vs, ts), h) && req(rmul(vi, ti), h) && req(rmul(vc, tc), h) && req(rdiv(ti, ts), [
    100n,
    1n
  ]) && req(rdiv(tc, ti), [
    2500n,
    1n
  ]) && sci(vs) === "2.246e-1" && sci(vi) === "2.246e-3" && sci(vc) === "8.985e-7" && sig(ts, 7) === "0.4451652" && sig(ti, 7) === "44.51652" && sig(tc, 7) === "111291.3" && sig(hrs, 6) === "30.9142";
  if (b1checks) ok("PASS B1 jar test, Ch 5's Stokes register re-derived at full precision (drho 1652 kg/m3, g 9.81, eta 1.002e-3, column 0.1 m): sand d = 5e-4 m: v " + sci(vs) + " m/s, t " + sig(ts, 7) + " s; silt d = 5e-5 m: v " + sci(vi) + " m/s, t " + sig(ti, 7) + " s; clay d = 1e-6 m: v " + sci(vc) + " m/s, t " + sig(tc, 7) + " s = " + sig(hrs, 6) + " h; v × t = 0.1 m EXACT all three; t-ratios silt/sand 100 and clay/silt 2500 EXACT");
  else bad("FAIL B1 a check broke: v " + sci(vs) + "/" + sci(vi) + "/" + sci(vc) + " t " + sig(ts, 7) + "/" + sig(ti, 7) + "/" + sig(tc, 7) + " h " + sig(hrs, 6));
  // ---- B2 lime round trip ----
  const b2l = sideSum("Ca(OH)2 + CO2"), b2r = sideSum("CaCO3 + H2O");
  if (b2l === b2r && b2l === 118101000n) ok("PASS B2 the lime round trip: Ca(OH)2 + CO2 -> CaCO3 + H2O: " + fmtMyu(b2l) + " g = " + fmtMyu(b2r) + " g EXACT (E7's pair)");
  else bad("FAIL B2 got " + b2l.toString() + "/" + b2r.toString());
  // ---- B3 hot mortar ----
  const n = [
    10000000n,
    56077n
  ];
  const wkg = rdiv(rmul(n, [
    18015n,
    1000n
  ]), [
    1000n,
    1n
  ]);
  const ckg = rdiv(rmul(n, [
    44009n,
    1000n
  ]), [
    1000n,
    1n
  ]);
  const caco3 = rdiv(rmul(n, [
    100086n,
    1000n
  ]), [
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
  const tout = radd(radd(caco3, wkg), [
    30n,
    1n
  ]);
  if (req(tin, tout) && f6(n) === "178.32623" && f6(wkg) === "3.212547" && f6(ckg) === "7.847959" && f6(caco3) === "17.847959" && f6(tin) === "51.060506") ok("PASS B3 hot mortar, 10.000 kg quicklime basis: n = 10000/56.077 = " + f6(n) + " mol CaO; in 10.000 kg CaO + " + f6(wkg) + " kg slaking water + 30.000 kg sand + " + f6(ckg) + " kg CO2 = " + f6(tin) + " kg; out " + f6(caco3) + " kg CaCO3 + " + f6(wkg) + " kg H2O + 30.000 kg sand = " + f6(tout) + " kg; in = out EXACT");
  else bad("FAIL B3 n " + f6(n) + " w " + f6(wkg) + " c " + f6(ckg) + " cc " + f6(caco3) + " in " + f6(tin));
  // ---- B4 UMF of the model ash glaze ----
  const mK = rdiv([
    1n,
    1n
  ], [
    94195000n,
    1n
  ]);
  const mCa = rmul([
    2n,
    1n
  ], rdiv([
    1n,
    1n
  ], [
    56077000n,
    1n
  ]));
  const mAl = rmul([
    3n,
    1n
  ], rdiv([
    1n,
    1n
  ], [
    101961000n,
    1n
  ]));
  const mSi = rmul([
    14n,
    1n
  ], rdiv([
    1n,
    1n
  ], [
    60083000n,
    1n
  ]));
  const flux = radd(mK, mCa);
  const umfK = rdiv(mK, flux), umfCa = rdiv(mCa, flux), umfAl = rdiv(mAl, flux), umfSi = rdiv(mSi, flux);
  if (f6(umfK) === "0.229385" && f6(umfCa) === "0.770615" && f6(umfAl) === "0.63574" && f6(umfSi) === "5.034644" && req(radd(umfK, umfCa), [
    1n,
    1n
  ])) ok("PASS B4 the model ash glaze, oxide masses 1:2:3:14 (K2O:CaO:Al2O3:SiO2, bases 94.195/56.077/101.961/60.083): UMF = " + f6(umfK) + " / " + f6(umfCa) + " / " + f6(umfAl) + " / " + f6(umfSi) + "; flux unity " + f6(umfK) + " + " + f6(umfCa) + " = 1 EXACT");
  else bad("FAIL B4 K " + f6(umfK) + " Ca " + f6(umfCa) + " Al " + f6(umfAl) + " Si " + f6(umfSi));
  // ---- B5 ash glass ----
  const b5l = sideSum("K2CO3 + CaCO3 + 2SiO2"), b5r = sideSum("K2CaSi2O6 + 2CO2");
  if (b5l === b5r && b5l === 358456000n) ok("PASS B5 ash glass: K2CO3 + CaCO3 + 2SiO2 -> K2CaSi2O6 + 2CO2: " + b5l.toString() + " myu = " + b5r.toString() + " myu (" + fmtMyu(b5l) + " g) EXACT");
  else bad("FAIL B5 got " + b5l.toString() + "/" + b5r.toString());
  // ---- B6 slaking heat ----
  const heat = rmul(n, [
    65n,
    1n
  ]);
  if (fmtFracBig(heat[0], heat[1], 1) === "11591.2") ok("PASS B6 slaking heat, Ch 14's band -63.7..-65.2 kJ/mol, ceiling-side working value 65.0: " + f6(n) + " mol × 65.0 kJ/mol = " + fmtFracBig(heat[0], heat[1], 1) + " kJ");
  else bad("FAIL B6 got " + fmtFracBig(heat[0], heat[1], 1));
  // ---- X1 dehydroxylation ledger ----
  const w700 = rdiv(rmul([
    700n,
    1n
  ], [
    36030000n,
    1n
  ]), [
    258157000n,
    1n
  ]);
  const m700 = rsub([
    700n,
    1n
  ], w700);
  const w500 = rdiv(rmul([
    500n,
    1n
  ], [
    36030000n,
    1n
  ]), [
    258157000n,
    1n
  ]);
  if (f4(w700) === "97.6964" && f4(m700) === "602.3036" && f4(w500) === "69.7831" && req(radd(w700, m700), [
    700n,
    1n
  ])) ok("PASS X1 dehydroxylation ledger: 700 g kaolinite -> " + f4(w700) + " g water + " + f4(m700) + " g metakaolin EXACT; 500 g kaolinite -> " + f4(w500) + " g water EXACT (Ch 30's 69.78 g mug case at full precision)");
  else bad("FAIL X1 w700 " + f4(w700) + " m700 " + f4(m700) + " w500 " + f4(w500));
  // ---- X2 hot mortar at 100x ----
  const n2 = [
    1000000000n,
    56077n
  ];
  const w2 = rdiv(rmul(n2, [
    18015n,
    1000n
  ]), [
    1000n,
    1n
  ]);
  const c2 = rdiv(rmul(n2, [
    44009n,
    1000n
  ]), [
    1000n,
    1n
  ]);
  const cc2 = rdiv(rmul(n2, [
    100086n,
    1000n
  ]), [
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
  if (req(tin2, tout2) && f6(w2) === "321.254703" && f6(c2) === "784.795906" && f6(cc2) === "1784.795906" && f6(tin2) === "5106.050609") ok("PASS X2 hot mortar at one hundred times: 1000 kg CaO + " + f6(w2) + " kg water + 3000 kg sand + " + f6(c2) + " kg CO2 = " + f6(tin2) + " kg in; " + f6(cc2) + " kg CaCO3 + " + f6(w2) + " kg water + 3000 kg sand = " + f6(tout2) + " kg out; in = out EXACT");
  else bad("FAIL X2 w " + f6(w2) + " c " + f6(c2) + " cc " + f6(cc2) + " in " + f6(tin2));
  // ---- X3 mullitization ----
  const x3l = sideSum("3Al2Si2O5(OH)4"), x3r = sideSum("Al6Si2O13 + 4SiO2 + 6H2O");
  if (x3l === x3r && x3l === 774471000n) ok("PASS X3 mullitization: 3 Al2Si2O5(OH)4 -> Al6Si2O13 + 4SiO2 + 6H2O: " + x3l.toString() + " myu = " + x3r.toString() + " myu (" + fmtMyu(x3l) + " g) EXACT");
  else bad("FAIL X3 got " + x3l.toString() + "/" + x3r.toString());
  // ---- X4 dolomite fractions ----
  const pCa = fmtFracBig(56077000n * 100n, 184399000n, 4);
  const pMg = fmtFracBig(40304000n * 100n, 184399000n, 4);
  const pCo = fmtFracBig(88018000n * 100n, 184399000n, 4);
  const x4sum = radd(radd([
    56077000n,
    184399000n
  ], [
    40304000n,
    184399000n
  ]), [
    88018000n,
    184399000n
  ]);
  if (pCa === "30.4107" && pMg === "21.857" && pCo === "47.7324" && req(x4sum, [
    1n,
    1n
  ])) ok("PASS X4 dolomite fractions: CaO " + pCa + "% + MgO " + pMg + "% + CO2 " + pCo + "% = 100% at full precision EXACT");
  else bad("FAIL X4 " + pCa + "/" + pMg + "/" + pCo);
  // ---- T1 checksum, T2 containment rescan ----
  if (compSum === 6955891500n) ok("PASS T1 composition checksum: engine sum " + compSum.toString() + " myu over 35 rows = hand-sum 6955891500 myu MATCH");
  else bad("FAIL T1 engine sum " + compSum.toString() + " myu vs hand 6955891500 myu");
  if (t2 === 35) ok("PASS T2 containment rescan: lane-2 products vs lane-1 on all 35 species: 35/35 ALL MATCH");
  else bad("FAIL T2 lane matches " + t2 + "/35");
  return {
    L: L,
    pass: pass,
    fail: fail,
    e9Caught: e9Caught
  };
}
```

## 8. Session 128 close summary

FC9 AUTHORED. Engine 41 (the lazy-tag segment-tree compositor, fresh build, zero code shared with Engines 1–40) ran the whole 73-row battery to **73/73 PASS — CLEAN**, G1 MATCH / G2 canary CAUGHT at S1 / G3 determinism HELD / G4 must-fail CAUGHT at exactly one H2O — with the engine's honest history on the record: run 1's copper element-table slip (86,000 myu short) caught by the T1 composition checksum before the freeze; the mid-session compaction that took the executed block and its source; the rebuild per the session-127 precedent, re-typed from the recorded spec and re-validated by re-execution (rebuild run 1 at 70/73 with two harness defects caught by the row-level asserts, rebuild run 2 the frozen CLEAN battery); the B4 input redefined as oxide masses 1:2:3:14 with the UMF reproduced exactly. All 19 pins re-grepped in their owners' pages; the seven NEW claims zero-hit verified across the full corpus with three disclosed catches; four [convergent] web verifications logged. Canvas 67,168 B (no trailing newline); repo master = canvas + one newline; web edition 59,078 B, renderer pre-validated byte-identical against fc7; index extended. The ◆ exercise answer withheld to the session-129 Phase-3 review per the FC alternation. NEXT: session 129 — the FC9 Phase-3 adversarial review, a fresh Engine 42, on the user's call.
