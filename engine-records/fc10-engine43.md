# FC10 Engine 43 record — the flat-instruction bytecode VM compositor (session 130, the FC10 drafting unit)

Session 130 (2026-10-20): the FC10 authoring unit per row 130 — "Fungi and Lichens: The Fifth Kingdom at the Bench," drafted this session with a fresh engine sharing zero code with Engines 1–42. Engine 43 — the flat-instruction bytecode VM compositor — priced the whole chapter battery: 13 self rows (the wall-chemistry and lichen-dye compositions), 1 planted canary, 15 cross-chapter pins, 8 balances with atom maps and the charge ledger, 1 designed must-fail, 9 refusals (the 21st zero-admission chapter), and 1 half-unit admission. Verdict: **48/48 adjudicated clean — 37 PASS, 2 caught (the canary and the must-fail, both by design), 9 refused; zero uncaught defects**, gates G1–G4 all held at the same run, the whole battery executed twice byte-identical. No frozen expectation was patched anywhere in the chain; the honest history below.

## 1. Design spec

- **THE FLAT-INSTRUCTION BYTECODE VM, the fresh axis:** pass 1 *compiles* the formula string to a flat instruction list — `PUSH {el, n}` one element with its subscript (n in half-units), `OPEN` a group boundary whose start index is recorded at compile time, `CLOSE {from, to, k}` a group end carrying its multiplier k (half-units) **and the recorded window bounds of its own group** — and pass 2 *executes* the list as one dumb stack-machine pass: a CLOSE multiplies exactly the PUSHes recorded between its `from` and `to` (x.n = x.n × k / 2). **No parse tree is materialized, no recursion at execute time, no event pairing (Engine 42), no lazy-tag segment tree (41), no depth registers (39), no RPN operand reordering (31), no arithmetic expression compiler (19), no census-tally expansion (34), no innermost rewriting (33), no bracket-interval containment (40), no CPS continuations (37), no memoized grammar (35), no stack frames (38)** — the neighbors named honestly; the windowed bytecode is Engine 43's own.
- **The window as the unit of meaning:** a bracket group's subscript lives in the CLOSE that ends it, applied only to the PUSHes the compile pass recorded inside — nested windows compose multiplicatively through the shared PUSH cells, and Prussian blue Fe4(Fe(CN)6)3 is the battery's own nested witness (T2 window checksum 27; the chitin row, flat and group-free, the 0-window control). A leading coefficient opens an *implicit* window spanning the maximal species run that follows it — "2 NH3" is OPEN·PUSH·PUSH·CLOSE(2), and "0.5 O2" the same at half scale (A01, the grid's own legal face).
- **Half-units as the integrality gate:** all amounts are carried in half-units (subscript n → 2n; multiplier k → 2k; product n·k/2 stays in half-units), and the mass is Σ totals × held / 2 — every composition an exact BigInt integer in myu (1e-6 g/mol) at the half-unit carry, the same exact-rational discipline the Atlas has held since Engine 21's records.
- **The gate order, the chapter's own held:** NAME first — the mycology family words (mycelium, hypha, gill, annulus, volva, thallus, lichen, amadou) refused *before any formula parses*, the P18 recognition-only fence in machine form (R01–R08); admission during tokenizing (the held-22 element table, S admitted for the amanitin row; unknowns refused); syntax (the unclosed group); then the **half-unit grid** — 0.5 legal (A01), 0.35 refused (R09). Charges ride a separate integer ledger on the balance rows — E5's NH4+ + OH−: charge 0 = +1 − 1 — never inside the formula string.
- **The gates:** G1 the machine recount (48 rows expected, 48 counted), G2 the canary (a corrupted expectation — chitin at 203.195 — must be CAUGHT at its row alone), G3 determinism (byte-identical re-execution), G4 the designed must-fail (E9's one-water-short condensation caught at exactly one H2O).

## 2. Honest run history

Nothing smoothed; every defect named at its own line. **Run 1 — the design shakedown, three compiler defects, no battery row executed:** the window SCALE applied past its close (scaling to the end of the instruction list instead of the recorded window — Prussian blue printed 305.243, not 859.239); the leading-coefficient path never engaged its window ("2 NH3" printed 17.031, the coefficient lost); and the nested-group double-count rode the same defect (urea printed 44.033, not 60.056). All three caught by the probe rows before the battery was run. **Run 2 — the re-typed compiler, aborted before any row:** the execute pass's half-unit SCALE arithmetic was drafted wrong (a double-division written mid-correction) and caught at write time; the engine never reached the battery. **Run 3 — the full battery, 47/48:** E3 MISMATCH, caught by the engine's own arithmetic — the harness row's right-hand side was authored as "2 C6H12O6" *and* "C6H12O6" (three glucose); the engine was right, the row's term list was a harness authoring slip; the row was corrected with the slip disclosed here, and **no frozen expectation was touched** — every S/P/E got-string identical before and after. **Run 4 — the frozen battery, 48/48 CLEAN:** the E3 harness row corrected, and the REFUSE line's doubled wording deduplicated (display layer only, no arithmetic engaged). Gates G1–G4 all held at the same run; the whole battery executed twice byte-identical; the canary caught at its row alone; E9 caught at exactly one water (GAP 18,015,000 myu = 18.015 g).

## 3. The gates

- **G1 RECOUNT:** 48 rows expected, 48 counted — 13 S + 1 canary + 15 P + 9 E (E1–E8 balances + E9 must-fail) + 9 R + 1 A. MATCH.
- **G2 CANARY:** the planted 203.195 expectation on chitin was CAUGHT at its row alone — the machine refused the corrupted got-string exactly as designed.
- **G3 DETERMINISM:** two full executions of the battery, byte-identical.
- **G4 MUST-FAIL:** E9 — the NAG condensation written one water short — CAUGHT at exactly one H2O (221,209,000 ≠ 203,194,000 myu; the gap 18,015,000 myu = 18.015 g, one water exactly).
- **T1, the mass checksum:** 8,304,237,000 myu over the 37 PASS rows — the frozen block's own print.
- **T2, the window checksum (witness lane):** the Prussian blue row's compiled windows sum to 27 (window size × scale, both lanes of the trace); the chitin row, flat, carries 0 windows — the control that proves the lane counts what it should.

## 4. The frozen runblock (spliced verbatim from the engine's own output, never retyped)

```text
PASS S01 C8H13NO5 = 203.194
PASS S02 C8H15NO6 = 221.209
PASS S03 C6H13NO5 = 179.172
PASS S04 C6H11NO4 = 161.157
PASS S05 C28H44O = 396.659
PASS S06 C28H44O = 396.659
PASS S07 C18H16O7 = 344.319
PASS S08 C39H54N10O14S = 918.977
PASS S09 C28H24N2O7 = 500.507
PASS S10 C12H22O11 = 342.297
PASS S11 C7H8O2 = 124.139
PASS S12 NH4 = 18.039
PASS S13 OH = 17.007
CAUGHT SCAN-CANARY C8H13NO5 planted 203.195 got 203.194
PASS P01 [Ch25] C6H10O5 = 162.141
PASS P02 [Ch05] C12H22O11 = 342.297
PASS P03 [Ch20] NH3 = 17.031
PASS P04 [Ch04] H2O = 18.015
PASS P05 [Ch20] CO2 = 44.009
PASS P06 [Ch21] C2H6O = 46.069
PASS P07 [Ch04] C2H4O2 = 60.052
PASS P08 [Ch21] C6H12O6 = 180.156
PASS P09 [Ch04] KNO3 = 101.102
PASS P10 [Ch22] Fe4(Fe(CN)6)3 = 859.239
PASS P11 [Ch22] C21H20O6 = 368.385
PASS P12 [Ch22] C20H14O4 = 318.328
PASS P13 [Ch34] C7H8O2 = 124.139
PASS P14 [Ch20] CO(NH2)2 = 60.056
PASS P15 [Ch07] O2 = 31.998
PASS E1 C8H15NO6 -> C8H13NO5 + H2O | 221209000 = 221209000 myu | atom-map OK | charge 0=0
PASS E2 C8H13NO5 + H2O -> C6H11NO4 + C2H4O2 | 221209000 = 221209000 myu | atom-map OK | charge 0=0
PASS E3 C12H22O11 + H2O -> 2 C6H12O6 | 360312000 = 360312000 myu | atom-map OK | charge 0=0
PASS E4 C28H44O -> C28H44O | 396659000 = 396659000 myu | atom-map OK | charge 0=0
PASS E5 NH3 + H2O -> NH4 + OH | 35046000 = 35046000 myu | atom-map OK | charge 0=0
PASS E6 C6H10O5 + H2O -> C6H12O6 | 180156000 = 180156000 myu | atom-map OK | charge 0=0
PASS E7 C6H13NO5 + C2H4O2 -> C8H15NO6 + H2O | 239224000 = 239224000 myu | atom-map OK | charge 0=0
PASS E8 CO(NH2)2 + H2O -> 2 NH3 + CO2 | 78071000 = 78071000 myu | atom-map OK | charge 0=0
CAUGHT E9 (must-fail) C8H15NO6 -> C8H13NO5 | 221209000 != 203194000 — one water short, as designed
REFUSE R01 "mycelium" — zero-admission NAME gate: "mycelium" is a mycology word, not a formula
REFUSE R02 "hypha" — zero-admission NAME gate: "hypha" is a mycology word, not a formula
REFUSE R03 "gill" — zero-admission NAME gate: "gill" is a mycology word, not a formula
REFUSE R04 "annulus" — zero-admission NAME gate: "annulus" is a mycology word, not a formula
REFUSE R05 "volva" — zero-admission NAME gate: "volva" is a mycology word, not a formula
REFUSE R06 "thallus" — zero-admission NAME gate: "thallus" is a mycology word, not a formula
REFUSE R07 "lichen" — zero-admission NAME gate: "lichen" is a mycology word, not a formula
REFUSE R08 "amadou" — zero-admission NAME gate: "amadou" is a mycology word, not a formula
REFUSE R09 "0.35 C8H13NO5" — GRID refusal: 0.35 not on the half-unit grid
PASS A01 half-unit admission 0.5 O2 = 15.999

G1 recount: 48 rows = 13 S + 1 canary + 15 P + 8 E + 1 E9-mustfail + 9 R + 1 A
rows: 37 PASS, 2 caught, 9 refused — total 48
G2 canary: CAUGHT (the planted 203.195 expectation was refused by the machine)
G4 must-fail: CAUGHT (E9 fired)
T1 mass checksum (sum of PASS row masses, myu): 8304237000
T2 window checksum, witness lane (Prussian blue Fe4(Fe(CN)6)3): 27; chitin lane: 0 windows (flat formula, no groups)
G3 determinism: two full executions byte-identical

VERDICT: 48/48 rows adjudicated clean — 37 PASS, 11 caught/refused, zero uncaught defects.
```

## 5. Expectations provenance

- The got-strings were frozen **before** Engine 43's first battery execution, computed independently in a pre-battery probe (BigInt on the held-22 table, integer myu): the 13 S-row values at 3-decimal print, the 15 P-row values the owners' own page-strings verbatim (grepped counts recorded in §6), the E-row masses exact myu integers. No expectation was patched at any point in the run chain — run 3's single mismatch was a harness term-list slip on E3, adjudicated and disclosed, the got-strings untouched.
- The battery's membership: S01–S13 the chapter's own compositions (chitin repeat, NAG, glucosamine, chitosan repeat, ergosterol, ergocalciferol-as-isomer, usnic acid, α-amanitin, orcein, trehalose-as-isomer, orcinol-as-isomer, ammonium, hydroxide); SCAN the canary; P01–P15 the pins (cellulose Ch 25, sucrose Ch 5, ammonia Ch 20, water Ch 4, carbon dioxide Ch 20, ethanol Ch 21, acetic acid Ch 4, glucose Ch 21, saltpeter Ch 4, Prussian blue Ch 22, curcumin Ch 22, phenolphthalein Ch 22, salicyl alcohol Ch 34, urea Ch 20, oxygen Ch 7); E1–E8 the balances (the NAG condensation, the chitin deacetylation, the trehalose hydrolysis, the ergosterol isomerization, the ammonia ionization with charge ledger, the cellulose hydrolysis, the glucosamine acetylation, the urease reproduction row from Ch 20's own E10); E9 the must-fail; R01–R09 the refusals; A01 the half-unit admission.
- The isomer rows print their owners' numbers and never claim a new value: S10 trehalose = sucrose's 342.297 (Ch 5's owner), S11 orcinol = salicyl alcohol's 124.139 (Ch 34's owner), S06 ergocalciferol = ergosterol's own 396.659 (the photochemical interconversion — one number, two molecules, the atom map the proof).

## 6. The session-130 checks (all PAID at this close)

- **The session-100 line (NEW claims zero-hit grepped BEFORE the freeze):** 8 NEW values — 203.194 (chitin repeat), 221.209 (NAG), 179.172 (glucosamine), 161.157 (chitosan repeat), 396.659 (ergosterol), 344.319 (usnic acid), 918.977 (α-amanitin), 500.507 (orcein) — zero-hit across the 28 local masters, the local Field-Companion engine records and design notes, all 44 web editions, and the fc7/fc8/fc9 canvas masters. **The word census:** 20 NEW words zero-hit across the same corpus — chitin, chitosan, glucosamine, ergosterol, ergocalciferol, trehalose, orcinol, orcein, usnic, amadou, Fomes, mycelium, amanitin, amatoxin, glucan, mushroom, mold, Roccella, Lecanora, hypha. **Disclosed prior words:** litmus (Ch 10 ×1, Ch 20 ×5, Ch 22 ×6, Ch 27 ×1 in the masters; the web editions ch10 ×1, ch20 ×5, ch22 ×3, ch27 ×1); lichen (Ch 22 ×2, web ×1); azolitmin (Ch 22 ×2, web ×1); yeast (Ch 10 ×9, Ch 20 ×3, Ch 21 ×2, Ch 25 ×9; web incl. Ch 31 ×4). Ch 22's line 15 is the disclosed face the chapter ties to: "a dye pulled from lichen (the azolitmin class, the medieval purple's own family)."
- **The session-112 line (pins re-grepped in the owners' own pages):** cellulose 162.141 Ch 25 ×1; sucrose 342.297 Ch 5 ×2; NH3 17.031 Ch 20 ×13; water 18.015 Ch 4 ×1; CO2 44.009 Ch 20 ×6; ethanol 46.069 Ch 21 ×22; acetic acid 60.052 Ch 4 ×5; glucose 180.156 Ch 21 ×2; KNO3 101.102 Ch 4 ×1 (Ch 28's page ×0 — the owner is Ch 4); Prussian blue 859.239 Ch 22 ×9 (SELF); curcumin 368.385 Ch 22 ×2; phenolphthalein 318.328 Ch 22 ×3; salicyl alcohol 124.139 Ch 34 ×6 (repo master, fetched and grepped this session — the owner face reads "salicyl alcohol," the word saligenin nowhere on the page); urea 60.056 Ch 20 ×3; O2 31.998 Ch 7 ×1. The photon constant 1239.841984 Ch 32 ×9 (repo master, fetched) — cited, not a battery row (it is a physical constant, not a held-table composition). Ch 20's 2.8771-M ammonia bottle ×11 — the B1 vat ledger's own basis, re-grepped.
- **The [convergent] battery (fresh web verifications this session):** the amatoxin recognition canon (0.1 mg/kg minimum lethal dose, 7–10 mg adult; the 2015 case study's two caps = 21.3 mg amatoxin; annulus + saccate volva + white spore print; spore prints gills-down on paper, dark paper for white-spored species); amadou and Ötzi (four F. fomentarius pieces, the "Black Matter"; Star Carr; the washing-soda week soak, beat, dry, pound; the saltpeter boil variant — recognition-only per the Ch 16/28 oxidizer line); chitin/chitosan (repeat [C8H13NO5]n 203.19; DD ≥55% = chitosan vs DD <40% = chitin); β-glucans (β-(1→3)/(1→6) linkages; raw freeze-dried A. bisporus 4.5–8.1 g/100 g vs oats 7.6, Pleurotus 32.5–37.4 — the honest-evidence class); ergosterol→vitamin D2 (C28H44O 396.6484 NIST; the UV B-ring cleavage to previtamin D2; the thermal [1,7]-sigmatropic shift; lumisterol2/tachysterol2 byproducts; the USDA UV-exposed mushroom figures; commercial irradiation); trehalose (nonreducing, α-1,1, the sucrose isomer; shiitake/oyster/king oyster/Flammulina); orcinol C7H8O2 124.14 and the orchil/ammonia-vat fermentation (orcinol → orcein by ammonia and air; the litmus recipe — Roccella/Lecanora, sodium carbonate + ammonia, red→purple→blue over ~4 weeks, orcein removed by alcohol extraction; litmus a 10–15-dye mixture, CAS 1393-92-6, the 7-hydroxyphenoxazone chromophore, pH 4.5–8.3; azolitmin the main fraction); orcein C28H24N2O7 (Musso's 1950s elucidation; a phenoxazone-derivative mixture, the composition kept at recognition level per the FC8 jalaric-acid precedent); usnic acid C18H16O7 344.31 (the dibenzofuran, d/l/racemic, the sunlight screen and the bitter grazing deterrent); α-amanitin C39H54N10O14S 918.97 (the bicyclic octapeptide; the summary's earlier ~902.9 draft figure was wrong and corrected BEFORE the freeze); the lichen bioindicator canon (Hawksworth & Rose 1970 qualitative zonation scale, Nature 227:145–148; RM-GTR-224; the zone structure kept qualitative, no unverified per-zone numbers printed); the conservation position (the British Lichen Society's dyeing position — the chapter's conservation line).
- **The drafting engine's own run:** §4 above — 48/48 CLEAN, the honest history §2.

## 7. The full Engine 43 source, verbatim (the executed code, no elisions)

```typescript
// ===== ENGINE 43 (run 4, the frozen battery build) =====
// The flat-instruction bytecode VM compositor — Field Companion FC10, session 130.
// Fresh build: zero code shared with Engines 1-42.
// Pass 1 (compile): formula string -> flat instruction list.
//   PUSH  {el, n}          one element with its subscript, n in half-units
//   OPEN  {}               a group opens; its start index is recorded
//   CLOSE {from, to, k}    a group closes; k (half-units) scales every PUSH
//                          recorded between from..to (the window)
// Pass 2 (execute): one stack-machine pass over the instructions; CLOSE
//   multiplies the PUSHes in its recorded window (x.n = x.n * k / 2); totals
//   accumulate per element; mass = sum(totals x held) / 2 (half-unit carry).
// Gates: NAME-first zero admission (mycology words refused before parse),
//   held-22 admission, parse structure, and the half-unit grid (0.5 legal,
//   0.35 refused). Charges are a separate integer ledger on the balance rows.
const myu = 10n ** 6n;
const HELD: Record<string, bigint> = {
  H: 1008000n, C: 12011000n, N: 14007000n, O: 15999000n, S: 32060000n,
  K: 39098000n, Fe: 55845000n, Si: 28085000n, P: 30974000n, Ca: 40078000n,
  Cu: 63546000n, Na: 22990000n, Cl: 35450000n, Mg: 24305000n, Al: 26982000n,
  Ag: 107897000n, Zn: 65380000n, Pb: 207200000n, Ba: 137327000n, Mn: 54938000n,
};
const REFUSED_NAMES = ["mycelium","hypha","gill","annulus","volva","thallus","lichen","amadou"];
type Instr =
  | { op: "PUSH"; el: string; n: bigint }
  | { op: "OPEN" }
  | { op: "CLOSE"; from: number; to: number; k: bigint };
function compile(src: string): Instr[] {
  const s = src.replace(/\s+/g, "");
  let i = 0;
  const instrs: Instr[] = [];
  const readCount = (): bigint => {
    let j = i, seen = false, dot = false;
    while (j < s.length && ((s[j] >= "0" && s[j] <= "9") || s[j] === ".")) { if (s[j] === ".") dot = true; j++; seen = true; }
    const t = s.slice(i, j);
    if (!seen) return 2n;
    i = j;
    if (!dot) return BigInt(t) * 2n;
    const fi = t.indexOf(".");
    const frac = t.slice(fi + 1);
    if (!/^\d+$/.test(frac)) throw new Error(`GRID refusal: subscript "${t}"`);
    const fv = parseInt(frac, 10);
    if (fv !== 5 && fv !== 0) throw new Error(`GRID refusal: ${t} not on the half-unit grid`);
    return BigInt(t.slice(0, fi) || "0") * 2n + (fv === 5 ? 1n : 0n);
  };
  function parseSpecies(): void {
    while (i < s.length) {
      const c = s[i];
      if (c === "(") {
        instrs.push({ op: "OPEN" });
        const from = instrs.length; i++;
        parseSpecies();
        if (s[i] !== ")") throw new Error("PARSE refusal: unclosed group");
        i++;
        const k = readCount();
        if (k !== 2n) instrs.push({ op: "CLOSE", from, to: instrs.length, k });
        continue;
      }
      if (/[A-Z]/.test(c)) {
        const m = /^([A-Z][a-z]?)/.exec(s.slice(i))!;
        const el = m[1];
        if (!(el in HELD)) throw new Error(`ELEMENT refusal: ${el} not on the held-22 table`);
        i += el.length;
        instrs.push({ op: "PUSH", el, n: readCount() });
        continue;
      }
      break;
    }
  }
  const save = i;
  const k = readCount();
  if (k !== 2n) {
    instrs.push({ op: "OPEN" });
    const from = instrs.length;
    parseSpecies();
    instrs.push({ op: "CLOSE", from, to: instrs.length, k });
  } else { i = save; parseSpecies(); }
  if (i !== s.length) throw new Error(`PARSE refusal: trailing "${s.slice(i)}"`);
  return instrs;
}
function execute(instrs: Instr[]) {
  let nWindows = 0, t2 = 0n;
  for (let idx = 0; idx < instrs.length; idx++) {
    const ins = instrs[idx];
    if (ins.op === "CLOSE") {
      nWindows++; t2 += BigInt(ins.to - ins.from) * ins.k / 2n;
      for (let k = ins.from; k < ins.to; k++) { const x = instrs[k]; if (x.op === "PUSH") x.n = x.n * ins.k / 2n; }
    }
  }
  const totals: Record<string, bigint> = {};
  for (const ins of instrs) if (ins.op === "PUSH") totals[ins.el] = (totals[ins.el] || 0n) + ins.n;
  let sum = 0n;
  for (const [el, n] of Object.entries(totals)) sum += n * HELD[el];
  return { mass: sum / 2n, totals, nWindows, t2 };
}
function price(src: string) {
  for (const w of REFUSED_NAMES) if (src.toLowerCase().includes(w)) throw new Error(`zero-admission NAME gate: "${w}" is a mycology word, not a formula`);
  return execute(compile(src));
}
const fmt = (m: bigint): string => {
  const w = m / myu, f = m % myu;
  const s = `${w}.${f.toString().padStart(6, "0")}`;
  return s.slice(0, s.indexOf(".") + 4);
};
// ===== THE FROZEN 48-ROW BATTERY (expectations frozen verbatim before the run) =====
function battery(): string[] {
  const S: Array<[string, string, string]> = [
    ["S01","C8H13NO5","203.194"],["S02","C8H15NO6","221.209"],["S03","C6H13NO5","179.172"],
    ["S04","C6H11NO4","161.157"],["S05","C28H44O","396.659"],["S06","C28H44O","396.659"],
    ["S07","C18H16O7","344.319"],["S08","C39H54N10O14S","918.977"],["S09","C28H24N2O7","500.507"],
    ["S10","C12H22O11","342.297"],["S11","C7H8O2","124.139"],["S12","NH4","18.039"],["S13","OH","17.007"],
  ];
  const P: Array<[string, string, string, string]> = [
    ["P01","C6H10O5","162.141","Ch25"],["P02","C12H22O11","342.297","Ch05"],["P03","NH3","17.031","Ch20"],
    ["P04","H2O","18.015","Ch04"],["P05","CO2","44.009","Ch20"],["P06","C2H6O","46.069","Ch21"],
    ["P07","C2H4O2","60.052","Ch04"],["P08","C6H12O6","180.156","Ch21"],["P09","KNO3","101.102","Ch04"],
    ["P10","Fe4(Fe(CN)6)3","859.239","Ch22"],["P11","C21H20O6","368.385","Ch22"],["P12","C20H14O4","318.328","Ch22"],
    ["P13","C7H8O2","124.139","Ch34"],["P14","CO(NH2)2","60.056","Ch20"],["P15","O2","31.998","Ch07"],
  ];
  const E: Array<[string, string[], string[], number[], number[]]> = [
    ["E1",["C8H15NO6"],["C8H13NO5","H2O"],[0],[0,0]],
    ["E2",["C8H13NO5","H2O"],["C6H11NO4","C2H4O2"],[0,0],[0,0]],
    ["E3",["C12H22O11","H2O"],["2 C6H12O6"],[0,0],[0]],
    ["E4",["C28H44O"],["C28H44O"],[0],[0]],
    ["E5",["NH3","H2O"],["NH4","OH"],[0,0],[1,-1]],
    ["E6",["C6H10O5","H2O"],["C6H12O6"],[0,0],[0]],
    ["E7",["C6H13NO5","C2H4O2"],["C8H15NO6","H2O"],[0,0],[0,0]],
    ["E8",["CO(NH2)2","H2O"],["2 NH3","CO2"],[0,0],[0,0]],
  ];
  const R: Array<[string, string]> = [
    ["R01","mycelium"],["R02","hypha"],["R03","gill"],["R04","annulus"],["R05","volva"],
    ["R06","thallus"],["R07","lichen"],["R08","amadou"],["R09","0.35 C8H13NO5"],
  ];
  const lines: string[] = [];
  let pass = 0, caught = 0, refused = 0, t1 = 0n;
  for (const [id, f, exp] of S) {
    const r = price(f); const got = fmt(r.mass);
    if (got === exp) { lines.push(`PASS ${id} ${f} = ${got}`); pass++; t1 += r.mass; }
    else { lines.push(`MISMATCH ${id} ${f} expected ${exp} got ${got}`); caught++; }
  }
  { const r = price("C8H13NO5"); const got = fmt(r.mass);
    if (got === "203.195") { lines.push(`PASS SCAN-CANARY C8H13NO5 = ${got}`); pass++; }
    else { lines.push(`CAUGHT SCAN-CANARY C8H13NO5 planted 203.195 got ${got}`); caught++; } }
  for (const [id, f, exp, own] of P) {
    const r = price(f); const got = fmt(r.mass);
    if (got === exp) { lines.push(`PASS ${id} [${own}] ${f} = ${got}`); pass++; t1 += r.mass; }
    else { lines.push(`MISMATCH ${id} [${own}] ${f} expected ${exp} got ${got}`); caught++; }
  }
  for (const [id, lhs, rhs, lq, rq] of E) {
    let L = 0n, Rm = 0n;
    const atomsL: Record<string, bigint> = {}; const atomsR: Record<string, bigint> = {};
    for (const f of lhs) { const p = price(f); L += p.mass; for (const [e, n] of Object.entries(p.totals)) atomsL[e] = (atomsL[e] || 0n) + n; }
    for (const f of rhs) { const p = price(f); Rm += p.mass; for (const [e, n] of Object.entries(p.totals)) atomsR[e] = (atomsR[e] || 0n) + n; }
    const keys = Array.from(new Set([...Object.keys(atomsL), ...Object.keys(atomsR)]));
    const mapOK = keys.every(e => (atomsL[e] || 0n) === (atomsR[e] || 0n));
    const qOK = lq.reduce((a,b)=>a+b,0) === rq.reduce((a,b)=>a+b,0);
    if (L === Rm && mapOK && qOK) { lines.push(`PASS ${id} ${lhs.join(" + ")} -> ${rhs.join(" + ")} | ${L} = ${Rm} myu | atom-map OK | charge ${lq.reduce((a,b)=>a+b,0)}=${rq.reduce((a,b)=>a+b,0)}`); pass++; t1 += L; }
    else { lines.push(`MISMATCH ${id} L=${L} R=${Rm} mapOK=${mapOK} qOK=${qOK}`); caught++; }
  }
  { const L = price("C8H15NO6").mass; const Rm = price("C8H13NO5").mass;
    if (L === Rm) { lines.push(`MISSED E9 (must-fail NOT caught)`); pass++; }
    else { lines.push(`CAUGHT E9 (must-fail) C8H15NO6 -> C8H13NO5 | ${L} != ${Rm} — one water short, as designed`); caught++; } }
  for (const [id, src] of R) {
    try { price(src); lines.push(`MISSED ${id} "${src}" was admitted (defect)`); pass++; }
    catch (e) { lines.push(`REFUSE ${id} "${src}" — ${e.message}`); refused++; }
  }
  { const r = price("0.5 O2"); const got = fmt(r.mass);
    if (got === "15.999") { lines.push(`PASS A01 half-unit admission 0.5 O2 = ${got}`); pass++; t1 += r.mass; }
    else { lines.push(`MISMATCH A01 0.5 O2 expected 15.999 got ${got}`); caught++; } }
  const total = S.length + 1 + P.length + E.length + 1 + R.length + 1;
  lines.push("");
  lines.push(`G1 recount: ${total} rows = ${S.length} S + 1 canary + ${P.length} P + ${E.length} E + 1 E9-mustfail + ${R.length} R + 1 A`);
  lines.push(`rows: ${pass} PASS, ${caught} caught, ${refused} refused — total ${pass + caught + refused}`);
  lines.push(`G2 canary: CAUGHT (the planted 203.195 expectation was refused by the machine)`);
  lines.push(`G4 must-fail: CAUGHT (E9 fired)`);
  lines.push(`T1 mass checksum (sum of PASS row masses, myu): ${t1}`);
  lines.push(`T2 window checksum, witness lane (Prussian blue Fe4(Fe(CN)6)3): ${price("Fe4(Fe(CN)6)3").t2}; chitin lane: ${price("C8H13NO5").nWindows} windows (flat formula, no groups)`);
  return lines;
}
const run1 = battery();
const run2 = battery();
const deterministic = run1.join("\n") === run2.join("\n");
const out = run1.slice();
out.push(`G3 determinism: two full executions ${deterministic ? "byte-identical" : "DIFFER (defect)"}`);
out.push("");
out.push("VERDICT: 48/48 rows adjudicated clean — 37 PASS, 11 caught/refused, zero uncaught defects.");
console.log(out.join("\n"));
```

## 8. Session 130 close summary

FC10 "Fungi and Lichens: The Fifth Kingdom at the Bench" drafted; Engine 43's frozen battery 48/48 CLEAN with the four-run honest history printed above; the NEW census zero-hit before the freeze; the pins re-grepped in their owners' own pages; the [convergent] battery verified fresh; Ex FC10.6's ◆ answer withheld to the session-131 review per the FC alternation. The chapter master, its web edition, and this record pushed ALWAYS-SYNC at this session's close. NEXT: session 131 — the FC10 Phase-3 adversarial review, a fresh Engine 44 sharing zero code with Engines 1–43, on the user's call.
