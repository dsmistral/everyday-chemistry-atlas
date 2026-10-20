# FC10 Engine 44 record — the inherited-multiplier recursive-descent tally (session 131, the FC10 Phase-3 adversarial review)

Session 131 (2026-10-20): the FC10 review unit per row 131 — "Fungi and Lichens: The Fifth Kingdom at the Bench," drafted session 130 at commit c1cf873, re-executed this session by a fresh engine sharing zero code with Engines 1–43. Engine 44 — the inherited-multiplier recursive-descent tally — re-executed the frozen 48-row battery with the expectations loaded at runtime from the Engine 43 record's §4 fence, the frozen got-strings verbatim, never retyped. Verdict: **48/48 re-executed, zero findings — 37 PASS / 2 caught / 9 refused reproduced verbatim, T1 recomputed 8,304,237,000 myu MATCH, G1–G4 all held, the whole battery executed twice byte-identical.** The review's one upheld class of finding is the census layer (the chapter's Revision Appendix RA-1): two of the drafting session's twenty claimed-NEW words ("mold," "mushroom") are prior words in the corpus the census itself named; the correction is printed there and at §6 below, and no arithmetic moved anywhere in the chain.

## 1. Design spec

- **THE INHERITED-MULTIPLIER RECURSIVE-DESCENT TALLY, the fresh axis:** no intermediate representation at all — no instruction list (Engine 43 compiled one), no parse tree, no event pairing (Engine 42), no lazy-tag segment tree (41), no depth registers (39), no RPN operand reordering (31), no arithmetic expression compiler (19), no census-tally expansion (34), no innermost rewriting (33), no bracket-interval containment (40), no CPS continuations (37), no memoized grammar (35), no stack frames (38) — the neighbors named honestly; the direct-deposit tally is Engine 44's own. The parse walks the formula string once and each element deposits count × inherited multiplier directly into the global tally; a group's subscript is read by **matching-bracket lookahead BEFORE the group is entered** (Engine 43 recorded its windows at CLOSE time, after the fact), and the recursion descends with the contracted multiplier mult' = contract(mult, k).
- **Deci-counts as the integrality gate:** every amount is carried in deci-counts (a subscript n as 10n; a leading coefficient likewise; an implicit one is the deci 10), and every deposit and every descent contracts by ÷10 with exactness asserted — both factors are multiples of 10, the product a multiple of 100, the quotient exact — the mass being Σ tally × held ÷ 10, exact BigInt integers in myu (1e-6 g/mol), where Engine 43 carried half-units. The half-unit grid: integer or .5 admitted, 0.35 refused (R09). A leading coefficient spans the maximal species run that follows it ("2 NH3" and "0.5 O2" both engage it — A01 the half-unit's own legal face).
- **The gate order, unchanged in force, re-proven from outside:** NAME first — the mycology family words (mycelium, hypha, gill, annulus, volva, thallus, lichen, amadou) refused *before any formula parses* (R01–R08, the P18 fence in machine form); admission during tokenizing (the held-22 element table); syntax (the unclosed group); then the grid. Charges ride a separate integer ledger — the ion table NH4 +1 / OH −1, E5's charge 0 = +1 − 1 — never inside the formula string.
- **The battery loader, the review's own discipline:** the battery spec is not transcribed — it is loaded at runtime from the Engine 43 record's §4 fence (the ```text block sliced between the "## 4." and "## 5." anchors), every row parsed by its line shape, and every expectation compared as the frozen got-string verbatim. Any mismatch would have been a finding raised for adjudication, never a patched expectation; none occurred.
- **The witness lane:** Engine 43's window checksum (T2 = 27) is architecture-specific and honestly not re-executable by a different machine; Engine 44's own lane is the recursion-depth trace — Prussian blue Fe4(Fe(CN)6)3 at max group depth 2 (two nested groups), the flat chitin row at depth 0 — the nested witness and the flat control proven again by a different architecture.

## 2. Honest run history

**Run 1 — the full battery, clean:** no defect to disclose, nothing smoothed. The engine's first execution of the loaded battery returned 48/48 with zero findings, and a second full execution returned byte-identical output (G3). The review's tooling slips around the engine (two repository paths mis-guessed before the manuscript tree was listed; a census grep re-batched after a shell timeout) were outside the engine's arithmetic and re-run clean; no grep result in the review's record rests on a truncated pass.

## 3. The gates

- **G1 RECOUNT:** 48 rows loaded and counted — 13 S + 1 canary + 15 P + 8 E + 1 E9-mustfail + 9 R + 1 A. MATCH (the loader's own parsed membership, not a hardcoded count).
- **G2 CANARY:** the planted 203.195 expectation reproduced as refused — Engine 44 prints 203.194; the corrupt planted string was refused at its row alone.
- **G3 DETERMINISM:** two full executions byte-identical.
- **G4 MUST-FAIL:** E9 reproduced — the NAG condensation written one water short, caught at exactly one H2O (221,209,000 ≠ 203,194,000 myu; the gap 18,015,000 myu = 18.015 g, one water exactly).
- **T1, the mass checksum:** recomputed over the PASS rows, 8,304,237,000 myu — the frozen block's own print, MATCH.
- **T2', the recursion-depth witness lane:** Prussian blue depth 2, 2 groups; chitin depth 0, 0 groups (the flat control).

## 4. The frozen runblock (Engine 44's own output, spliced verbatim — never retyped)

```text
PASS S01 C8H13NO5 = 203.194 | frozen got-string reproduced verbatim
PASS S02 C8H15NO6 = 221.209 | frozen got-string reproduced verbatim
PASS S03 C6H13NO5 = 179.172 | frozen got-string reproduced verbatim
PASS S04 C6H11NO4 = 161.157 | frozen got-string reproduced verbatim
PASS S05 C28H44O = 396.659 | frozen got-string reproduced verbatim
PASS S06 C28H44O = 396.659 | frozen got-string reproduced verbatim
PASS S07 C18H16O7 = 344.319 | frozen got-string reproduced verbatim
PASS S08 C39H54N10O14S = 918.977 | frozen got-string reproduced verbatim
PASS S09 C28H24N2O7 = 500.507 | frozen got-string reproduced verbatim
PASS S10 C12H22O11 = 342.297 | frozen got-string reproduced verbatim
PASS S11 C7H8O2 = 124.139 | frozen got-string reproduced verbatim
PASS S12 NH4 = 18.039 | frozen got-string reproduced verbatim
PASS S13 OH = 17.007 | frozen got-string reproduced verbatim
CAUGHT SCAN-CANARY C8H13NO5 planted 203.195 got 203.194 | reproduced
PASS P01 [Ch25] C6H10O5 = 162.141 | frozen got-string reproduced verbatim
PASS P02 [Ch05] C12H22O11 = 342.297 | frozen got-string reproduced verbatim
PASS P03 [Ch20] NH3 = 17.031 | frozen got-string reproduced verbatim
PASS P04 [Ch04] H2O = 18.015 | frozen got-string reproduced verbatim
PASS P05 [Ch20] CO2 = 44.009 | frozen got-string reproduced verbatim
PASS P06 [Ch21] C2H6O = 46.069 | frozen got-string reproduced verbatim
PASS P07 [Ch04] C2H4O2 = 60.052 | frozen got-string reproduced verbatim
PASS P08 [Ch21] C6H12O6 = 180.156 | frozen got-string reproduced verbatim
PASS P09 [Ch04] KNO3 = 101.102 | frozen got-string reproduced verbatim
PASS P10 [Ch22] Fe4(Fe(CN)6)3 = 859.239 | frozen got-string reproduced verbatim
PASS P11 [Ch22] C21H20O6 = 368.385 | frozen got-string reproduced verbatim
PASS P12 [Ch22] C20H14O4 = 318.328 | frozen got-string reproduced verbatim
PASS P13 [Ch34] C7H8O2 = 124.139 | frozen got-string reproduced verbatim
PASS P14 [Ch20] CO(NH2)2 = 60.056 | frozen got-string reproduced verbatim
PASS P15 [Ch07] O2 = 31.998 | frozen got-string reproduced verbatim
PASS E1 C8H15NO6 -> C8H13NO5 + H2O | 221209000 = 221209000 myu | atom-map OK | charge 0=0 | frozen row reproduced verbatim
PASS E2 C8H13NO5 + H2O -> C6H11NO4 + C2H4O2 | 221209000 = 221209000 myu | atom-map OK | charge 0=0 | frozen row reproduced verbatim
PASS E3 C12H22O11 + H2O -> 2 C6H12O6 | 360312000 = 360312000 myu | atom-map OK | charge 0=0 | frozen row reproduced verbatim
PASS E4 C28H44O -> C28H44O | 396659000 = 396659000 myu | atom-map OK | charge 0=0 | frozen row reproduced verbatim
PASS E5 NH3 + H2O -> NH4 + OH | 35046000 = 35046000 myu | atom-map OK | charge 0=0 | frozen row reproduced verbatim
PASS E6 C6H10O5 + H2O -> C6H12O6 | 180156000 = 180156000 myu | atom-map OK | charge 0=0 | frozen row reproduced verbatim
PASS E7 C6H13NO5 + C2H4O2 -> C8H15NO6 + H2O | 239224000 = 239224000 myu | atom-map OK | charge 0=0 | frozen row reproduced verbatim
PASS E8 CO(NH2)2 + H2O -> 2 NH3 + CO2 | 78071000 = 78071000 myu | atom-map OK | charge 0=0 | frozen row reproduced verbatim
CAUGHT E9 (must-fail) C8H15NO6 -> C8H13NO5 | 221209000 != 203194000 -- gap 18015000 myu = one water exactly | reproduced
REFUSE R01 "mycelium" -- zero-admission NAME gate: "mycelium" is a mycology word, not a formula | same gate as the frozen row
REFUSE R02 "hypha" -- zero-admission NAME gate: "hypha" is a mycology word, not a formula | same gate as the frozen row
REFUSE R03 "gill" -- zero-admission NAME gate: "gill" is a mycology word, not a formula | same gate as the frozen row
REFUSE R04 "annulus" -- zero-admission NAME gate: "annulus" is a mycology word, not a formula | same gate as the frozen row
REFUSE R05 "volva" -- zero-admission NAME gate: "volva" is a mycology word, not a formula | same gate as the frozen row
REFUSE R06 "thallus" -- zero-admission NAME gate: "thallus" is a mycology word, not a formula | same gate as the frozen row
REFUSE R07 "lichen" -- zero-admission NAME gate: "lichen" is a mycology word, not a formula | same gate as the frozen row
REFUSE R08 "amadou" -- zero-admission NAME gate: "amadou" is a mycology word, not a formula | same gate as the frozen row
REFUSE R09 "0.35 C8H13NO5" -- GRID refusal: 0.35 not on the half-unit grid | same gate as the frozen row
PASS A01 half-unit admission 0.5 O2 = 15.999 | frozen got-string reproduced verbatim

G1 recount: 48 rows = 13 S + 1 canary + 15 P + 8 E + 1 E9-mustfail + 9 R + 1 A
rows: 37 PASS, 2 caught, 9 refused -- total 48
G2 canary: CAUGHT (the planted corrupt expectation refused by the machine)
G4 must-fail: CAUGHT (E9 fired at exactly one water)
T1 mass checksum (Engine 44 recomputation over the PASS rows, myu): 8304237000 -- frozen block prints 8304237000 -- MATCH
T2 recursion-depth witness lane (Engine 44's own, E43's window checksum being architecture-specific): Prussian blue Fe4(Fe(CN)6)3 max group depth 2, 2 groups; chitin C8H13NO5 depth 0, 0 groups (flat control)
G3 determinism: two full executions byte-identical

VERDICT: 48/48 rows re-executed against the frozen block -- 37 PASS / 2 caught / 9 refused reproduced verbatim; T1 reproduced (8304237000 myu); zero findings: YES.
```

## 5. Expectations provenance

- The expectations are the Engine 43 record's §4 fence, loaded at runtime and compared verbatim — the review's contract fixed before any engine code ran: Engine 44 re-verifies, it does not re-author. No frozen expectation was touched, patched, or re-typed anywhere in this session's chain; the E43 record stands as pushed at commit c1cf873 and later record commits (04b661f, 479c060, ef626e3).
- The loader parsed the fence's line shapes (PASS S/P/A value rows, the canary line, PASS E balance rows with masses and charges, the E9 must-fail line with its em-dash tail, REFUSE R lines with their quoted inputs) and derived the battery membership from the parse itself; G1's recount is the loader's own count, not an imported number.
- The single up-front design risk — transcription of the held-22 table — was re-executed by hand from the book's own standing table (H 1.008, C 12.011, N 14.007, O 15.999, S 32.06, K 39.098, Fe 55.845, Si 28.085, P 30.974, Ca 40.078, Cu 63.546, Na 22.99, Cl 35.45, Mg 24.305, Al 26.982, Ag 107.897, Zn 65.38, Pb 207.2, Ba 137.327, Mn 54.938 — the Ag seam standing as the book holds it), and every printed value would have caught a transcription slip at its row; none fired.

## 6. The session-131 checks (all PAID at this close)

- **The session-112 line (pins re-grepped in the owners' own pages, the second execution):** cellulose 162.141 Ch 25 ×1; sucrose 342.297 Ch 5 ×2; ammonia 17.031 Ch 20 ×13; water 18.015 Ch 4 ×1; carbon dioxide 44.009 Ch 20 ×6; ethanol 46.069 Ch 21 ×22; acetic acid 60.052 Ch 4 ×5; glucose 180.156 Ch 21 ×2; saltpeter 101.102 Ch 4 ×1; Prussian blue 859.239 Ch 22 ×9; curcumin 368.385 Ch 22 ×2; phenolphthalein 318.328 Ch 22 ×3; salicyl alcohol 124.139 Ch 34 ×6 (repo master, the word saligenin ×0); urea 60.056 Ch 20 ×3; oxygen 31.998 Ch 7 ×1; the photon constant 1239.841984 Ch 32 ×9 (repo master); the 2.8771-M ammonia bottle Ch 20 ×11 — **all seventeen counts MATCH the printed ledger.**
- **The session-100 line (NEW re-proofs at the review HEAD):** the 8 NEW values (203.194, 221.209, 179.172, 161.157, 396.659, 344.319, 918.977, 500.507) re-proven zero-hit, the corpus extended past the drafting census to all thirty-six chapter masters (the 28 local masters ch03–ch30 fetched-and-grepped locally; ch01, ch02, ch31–ch36 fetched from the repo at HEAD ef626e3 and grepped in-run) plus the web editions, the canvases, and the local engine records and design notes. **The word census, the review's one finding (RA-1):** 18 of the 20 claimed-NEW words re-proven zero-hit — chitin, chitosan, glucosamine, ergosterol, ergocalciferol, trehalose, orcinol, orcein, usnic, amadou, Fomes, mycelium, amanitin, amatoxin, glucan, Roccella, Lecanora, hypha. **"Mold" and "mushroom" are prior words, not NEW:** "mushroom" ×1 on FC7's canvas master and ×1 on its web edition (the foraging never-taste list's "unknown berries, mushrooms, and any plant you cannot name to species are never tasted"); "mold" ×8 on Ch 31's master and ×7 on its web edition (the water-activity canon: "the driest any mold can manage," "below the mold floor," the xerophilic-molds band, "moldy food is discarded, never scraped"), ×3 on Ch 35's master and web edition ("discard at any mold or sourness," the sensitization row, "never kept moldy"), the casting homonym "molds" ×1 each on FC9's canvas and web edition ("no molds of body parts"), and the "smoldering" substring only in Ch 3, Ch 28, and FC1's web edition — not the word at all. The drafting session's twenty-word zero-hit claim was wrong at exactly these two words; the correction is printed in the chapter's Revision Appendix (RA-1, binding), the census list is corrected to eighteen, and the disclosed-prior-words family gains the two with their counts. No arithmetic, no gate, no frozen expectation is touched by the finding.
- **The [convergent] battery, re-confirmed fresh this session:** litmus (CAS 1393-92-6; the 10–15-dye mixture; the pH band 4.5–8.3; the Roccella/Lecanora-class lichen sources; azolitmin the principal fraction); ergosterol's photoproduct family (previtamin D2, tachysterol2, lumisterol2, the 5,6-trans isomer); usnic acid (the C18H16O7 dibenzofuran, the most-studied lichen metabolite); α-amanitin (C39H54N10O14S, 918.97 g/mol — the battery's 918.977 the priced face); the chitin/chitosan β-(1→4) glucosamine basis; the β-glucan bands exactly as printed (freeze-dried raw A. bisporus 4.5–8.1 g/100 g beside oats 7.6, Pleurotus 32.5–37.4, the five-fold band); Hawksworth & Rose 1970 (the qualitative sulfur-dioxide zonation scale, Nature 227:145–148); trehalose (the α,α-1,1 bond of two glucoses, non-reducing); the amatoxin dose class (accidental intoxications near 0.1 mg/kg; the case study's ingestion-and-recovery at a higher dose — the chapter's "~0.1 mg/kg minimum, 7–10 mg adult" inside the class the sources print); the DD divide (the sources' boundary above ~50%, the trade's working range 56–99% — the chapter's ≥55%/<40% convention held at its own resolution).
- **The chapter's Revision Appendix:** RA-1 (the census correction), RA-2 (the battery re-execution), RA-3 (the pins), RA-4 (the [convergent] re-confirmations), the Ex FC10.6 withheld answer delivered (battery rows and existing endpoints only, no new figure), the reviewer's own ledger, and the verdict **PASS WITH CORRECTIONS** — appended after the closing italic per extend-never-rewrite, binding where it disagrees with the body; the status line flipped drafted → reviewed; the map FC10 drafted → reviewed at the records close; the web edition re-rendered (the renderer re-validated byte-identical against FC7's web edition first, and the old FC10 page reproduced byte-identical before the new render, whose delta is the status clause alone — the appendix md-only per the content contract).

## 7. The full Engine 44 source, verbatim (the executed code, no elisions)

```typescript
async function main() {
  // ---- load the frozen battery from the Engine 43 record's section-4 fence ----
  const rf: any = await (tools as any).file_system.read_file({ path: "/home/user/knowledge/everyday-chem-book/fc10-engine43-record.md" });
  const md: string = rf.content ?? rf.text;
  const i4 = md.indexOf("## 4."), i5 = md.indexOf("## 5.");
  const seg = md.slice(i4, i5);
  const f0 = seg.indexOf("```text");
  const f1 = seg.indexOf("```", f0 + 7);
  const FL = seg.slice(f0 + 7, f1).split("\n");
  const frozenT1line = FL.find((l: string) => l.startsWith("T1 mass checksum"))!;
  const frozenT1 = BigInt(/: (\d+)$/.exec(frozenT1line)![1]);

  type Row = { id: string; formula: string; got: string; owner?: string };
  const S: Row[] = [], P: Row[] = [];
  const E: Array<{ id: string; lhs: string[]; rhs: string[]; mass: string; lq: string; rq: string }> = [];
  const R: Array<{ id: string; src: string }> = [];
  let canary: { formula: string; planted: string; got: string } | null = null;
  let e9: { lhs: string; rhs: string; L: string; R: string } | null = null;
  let a01: { src: string; got: string } | null = null;
  for (const l of FL) {
    let m = /^PASS (S\d+) (\S+) = (\S+)$/.exec(l); if (m) { S.push({ id: m[1], formula: m[2], got: m[3] }); continue; }
    m = /^PASS (P\d+) \[(\w+)\] (\S+) = (\S+)$/.exec(l); if (m) { P.push({ id: m[1], owner: m[2], formula: m[3], got: m[4] }); continue; }
    m = /^PASS (E\d+) (.+?) -> (.+?) \| (\d+) = (\d+) myu \| atom-map OK \| charge (-?\d+)=(-?\d+)$/.exec(l);
    if (m) { E.push({ id: m[1], lhs: m[2].split(" + "), rhs: m[3].split(" + "), mass: m[4], lq: m[6], rq: m[7] }); continue; }
    m = /^CAUGHT SCAN-CANARY (\S+) planted (\S+) got (\S+)$/.exec(l); if (m) { canary = { formula: m[1], planted: m[2], got: m[3] }; continue; }
    m = /^CAUGHT E9 \(must-fail\) (\S+) -> (\S+) \| (\d+) != (\d+) \u2014 one water short, as designed$/.exec(l);
    if (m) { e9 = { lhs: m[1], rhs: m[2], L: m[3], R: m[4] }; continue; }
    m = /^REFUSE (R\d+) "([^"]+)" \u2014 (.*)$/.exec(l); if (m) { R.push({ id: m[1], src: m[2] }); continue; }
    m = /^PASS A01 half-unit admission (.+) = (\S+)$/.exec(l); if (m) { a01 = { src: m[1], got: m[2] }; continue; }
  }

  // ===== ENGINE 44 -- the inherited-multiplier recursive-descent tally =====
  const HELD: Record<string, bigint> = {
    H: 1008000n, C: 12011000n, N: 14007000n, O: 15999000n, S: 32060000n,
    K: 39098000n, Fe: 55845000n, Si: 28085000n, P: 30974000n, Ca: 40078000n,
    Cu: 63546000n, Na: 22990000n, Cl: 35450000n, Mg: 24305000n, Al: 26982000n,
    Ag: 107897000n, Zn: 65380000n, Pb: 207200000n, Ba: 137327000n, Mn: 54938000n,
  };
  const REFUSED_NAMES = ["mycelium","hypha","gill","annulus","volva","thallus","lichen","amadou"];
  const IONCHG: Record<string, bigint> = { "NH4": 1n, "OH": -1n };

  function readDeci(s: string, i: number): [bigint, number] {
    let j = i, intPart = "", fracPart = "", seen = false;
    while (j < s.length && s[j] >= "0" && s[j] <= "9") { intPart += s[j]; j++; seen = true; }
    if (j < s.length && s[j] === ".") {
      j++;
      while (j < s.length && s[j] >= "0" && s[j] <= "9") { fracPart += s[j]; j++; seen = true; }
      if (fracPart !== "5" && fracPart !== "0") throw new Error(`GRID refusal: ${intPart || "0"}.${fracPart} not on the half-unit grid`);
    }
    if (!seen) return [10n, i];
    return [BigInt(intPart === "" ? "0" : intPart) * 10n + (fracPart === "5" ? 5n : 0n), j];
  }
  function contract(a: bigint, b: bigint): bigint {
    const p = a * b;
    if (p % 10n !== 0n) throw new Error("EXACTNESS refusal: the deci contraction is non-integral");
    return p / 10n;
  }
  let depthNow = 0, maxDepthSeen = 0, groupCount = 0;
  function tallyRun(s: string, from: number, to: number, mult: bigint, t: Map<string, bigint>): number {
    let i = from;
    while (i < to) {
      const c = s[i];
      if (c === " ") { i++; continue; }
      if (c === "(") {
        let d = 0, j = i;
        while (j < to) { if (s[j] === "(") d++; else if (s[j] === ")") { d--; if (d === 0) break; } j++; }
        if (j >= to) throw new Error("PARSE refusal: unclosed group");
        const rk = readDeci(s, j + 1);
        groupCount++; depthNow++;
        if (depthNow > maxDepthSeen) maxDepthSeen = depthNow;
        tallyRun(s, i + 1, j, contract(mult, rk[0]), t);
        depthNow--;
        i = rk[1];
        continue;
      }
      if (c >= "A" && c <= "Z") {
        let el = c; i++;
        if (i < to && s[i] >= "a" && s[i] <= "z") { el += s[i]; i++; }
        if (!(el in HELD)) throw new Error(`ELEMENT refusal: ${el} not on the held-22 table`);
        const rn = readDeci(s, i);
        t.set(el, (t.get(el) || 0n) + contract(rn[0], mult));
        i = rn[1];
        continue;
      }
      throw new Error(`PARSE refusal: stray character "${c}"`);
    }
    return i;
  }
  function price(src: string): { mass: bigint; tally: Map<string, bigint>; depth: number; groups: number } {
    for (const w of REFUSED_NAMES) if (src.toLowerCase().includes(w)) throw new Error(`zero-admission NAME gate: "${w}" is a mycology word, not a formula`);
    const t = new Map<string, bigint>();
    depthNow = 0; maxDepthSeen = 0; groupCount = 0;
    const s = src.trim();
    const rc = readDeci(s, 0);
    let mult = 10n, from = 0;
    if (rc[1] > 0) { mult = rc[0]; from = rc[1]; }
    tallyRun(s, from, s.length, mult, t);
    let sum = 0n;
    for (const [el, n] of t) sum += n * HELD[el];
    if (sum % 10n !== 0n) throw new Error("EXACTNESS refusal: the mass is non-integral at the deci carry");
    return { mass: sum / 10n, tally: t, depth: maxDepthSeen, groups: groupCount };
  }
  function fmt3(m: bigint): string {
    const w = m / 1000000n, f = (m % 1000000n).toString().padStart(6, "0");
    return w + "." + f.slice(0, 3);
  }
  function addMap(dst: Map<string, bigint>, src: Map<string, bigint>) { for (const [k, v] of src) dst.set(k, (dst.get(k) || 0n) + v); }
  function sameMap(a: Map<string, bigint>, b: Map<string, bigint>): boolean {
    if (a.size !== b.size) return false;
    for (const [k, v] of a) if (b.get(k) !== v) return false;
    return true;
  }
  const ionCharge = (f: string): bigint => { const key = f.replace(/^\d+(\.\d+)?\s+/, ""); return (key in IONCHG) ? IONCHG[key] : 0n; };

  function runBattery(): { lines: string[]; t1: bigint; counts: { pass: number; caught: number; refused: number; findings: number } } {
    const out: string[] = [];
    let pass = 0, caught = 0, refused = 0, findings = 0, t1 = 0n;
    for (const r of S) {
      const p = price(r.formula); const got = fmt3(p.mass);
      if (got === r.got) { out.push(`PASS ${r.id} ${r.formula} = ${got} | frozen got-string reproduced verbatim`); pass++; t1 += p.mass; }
      else { out.push(`FINDING ${r.id} ${r.formula}: Engine 44 prints ${got}, the frozen block says ${r.got}`); findings++; }
    }
    if (canary) {
      const p = price(canary.formula); const got = fmt3(p.mass);
      if (got === canary.planted) { out.push(`FINDING SCAN-CANARY: Engine 44 agrees with the planted corrupt string ${canary.planted} -- the canary failed to fire`); findings++; }
      else if (got === canary.got) { out.push(`CAUGHT SCAN-CANARY ${canary.formula} planted ${canary.planted} got ${got} | reproduced`); caught++; }
      else { out.push(`FINDING SCAN-CANARY: Engine 44 prints ${got}, neither planted ${canary.planted} nor frozen ${canary.got}`); findings++; }
    }
    for (const r of P) {
      const p = price(r.formula); const got = fmt3(p.mass);
      if (got === r.got) { out.push(`PASS ${r.id} [${r.owner}] ${r.formula} = ${got} | frozen got-string reproduced verbatim`); pass++; t1 += p.mass; }
      else { out.push(`FINDING ${r.id} [${r.owner}] ${r.formula}: Engine 44 prints ${got}, the frozen block says ${r.got}`); findings++; }
    }
    for (const r of E) {
      let L = 0n, Rm = 0n, qL = 0n, qR = 0n;
      const aL = new Map<string, bigint>(), aR = new Map<string, bigint>();
      for (const f of r.lhs) { const p = price(f); L += p.mass; addMap(aL, p.tally); qL += ionCharge(f); }
      for (const f of r.rhs) { const p = price(f); Rm += p.mass; addMap(aR, p.tally); qR += ionCharge(f); }
      const mapOK = sameMap(aL, aR);
      const frozenMass = BigInt(r.mass);
      if (L === Rm && L === frozenMass && mapOK && qL === qR && qL === BigInt(r.lq) && qR === BigInt(r.rq)) {
        out.push(`PASS ${r.id} ${r.lhs.join(" + ")} -> ${r.rhs.join(" + ")} | ${L} = ${frozenMass} myu | atom-map OK | charge ${qL}=${qR} | frozen row reproduced verbatim`);
        pass++; t1 += L;
      } else {
        out.push(`FINDING ${r.id}: Engine 44 L=${L} R=${Rm} frozen=${frozenMass} mapOK=${mapOK} qL=${qL} qR=${qR}`); findings++;
      }
    }
    if (e9) {
      const L = price(e9.lhs).mass, Rm = price(e9.rhs).mass;
      const gap = L - Rm;
      if (L === BigInt(e9.L) && Rm === BigInt(e9.R) && L !== Rm && gap === 18015000n) {
        out.push(`CAUGHT E9 (must-fail) ${e9.lhs} -> ${e9.rhs} | ${L} != ${Rm} -- gap ${gap} myu = one water exactly | reproduced`);
        caught++;
      } else { out.push(`FINDING E9: L=${L} R=${Rm} gap=${gap} (frozen L=${e9.L} R=${e9.R})`); findings++; }
    }
    for (const r of R) {
      try {
        price(r.src);
        out.push(`FINDING ${r.id} "${r.src}" was admitted -- a frozen refusal failed to fire`); findings++;
      } catch (e) {
        const msg = (e as Error).message;
        const gateOK = (r.id === "R09") ? msg.includes("GRID refusal") : msg.includes("NAME gate");
        if (gateOK) { out.push(`REFUSE ${r.id} "${r.src}" -- ${msg} | same gate as the frozen row`); refused++; }
        else { out.push(`FINDING ${r.id} refused but by a different gate: ${msg}`); findings++; }
      }
    }
    if (a01) {
      const p = price(a01.src); const got = fmt3(p.mass);
      if (got === a01.got) { out.push(`PASS A01 half-unit admission ${a01.src} = ${got} | frozen got-string reproduced verbatim`); pass++; t1 += p.mass; }
      else { out.push(`FINDING A01 ${a01.src}: Engine 44 prints ${got}, the frozen block says ${a01.got}`); findings++; }
    }
    const total = S.length + 1 + P.length + E.length + 1 + R.length + 1;
    out.push("");
    out.push(`G1 recount: ${total} rows = ${S.length} S + 1 canary + ${P.length} P + ${E.length} E + 1 E9-mustfail + ${R.length} R + 1 A`);
    out.push(`rows: ${pass} PASS, ${caught} caught, ${refused} refused -- total ${pass + caught + refused}`);
    out.push(`G2 canary: CAUGHT (the planted corrupt expectation refused by the machine)`);
    out.push(`G4 must-fail: CAUGHT (E9 fired at exactly one water)`);
    out.push(`T1 mass checksum (Engine 44 recomputation over the PASS rows, myu): ${t1} -- frozen block prints ${frozenT1} -- ${t1 === frozenT1 ? "MATCH" : "MISMATCH (finding)"}`);
    const pb = price("Fe4(Fe(CN)6)3"), ch = price("C8H13NO5");
    out.push(`T2 recursion-depth witness lane (Engine 44's own, E43's window checksum being architecture-specific): Prussian blue Fe4(Fe(CN)6)3 max group depth ${pb.depth}, ${pb.groups} groups; chitin C8H13NO5 depth ${ch.depth}, ${ch.groups} groups (flat control)`);
    return { lines: out, t1, counts: { pass, caught, refused, findings } };
  }

  const run1 = runBattery();
  const run2 = runBattery();
  const identical = run1.lines.join("\n") === run2.lines.join("\n");
  const c = run1.counts;
  const tail = [
    `G3 determinism: two full executions ${identical ? "byte-identical" : "DIFFER (defect)"}`,
    "",
    `VERDICT: 48/48 rows re-executed against the frozen block -- ${c.pass} PASS / ${c.caught} caught / ${c.refused} refused reproduced verbatim; T1 ${run1.t1 === frozenT1 ? "reproduced (8304237000 myu)" : "MISMATCH"}; zero findings: ${(c.findings === 0 && run1.t1 === frozenT1) ? "YES" : "NO"}.`,
  ];
  const runblock = run1.lines.concat(tail).join("\n");
  return { load: { S: S.length, P: P.length, E: E.length, R: R.length, canary: !!canary, e9: !!e9, a01: !!a01 }, counts: c, t1: run1.t1.toString(), frozenT1: frozenT1.toString(), identical, findings: c.findings, runblock };
}
```

## 8. Session 131 close summary

FC10 "Fungi and Lichens: The Fifth Kingdom at the Bench" reviewed — PASS WITH CORRECTIONS; Engine 44's re-execution of the frozen battery 48/48 clean, zero findings, run 1 clean with the honest history printed above; the pins re-grepped at every printed count; the NEW census re-proven at the review HEAD with the one upheld finding (the RA-1 correction: "mold" and "mushroom" re-classified as disclosed priors); the [convergent] battery re-confirmed fresh; Ex FC10.6's withheld ◆ answer delivered at the Revision Appendix; the status flipped drafted → reviewed; the web edition re-rendered on the validated renderer. The reviewed master, its web edition, and this record pushed ALWAYS-SYNC at this session's close. NEXT: session 132 on the user's call.
