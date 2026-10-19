# FC3 Engine 32 — the depth-map fold review engine (durable record, session 116 part 1)

## Design (the binding spec — rebuild from this alone)

Engine 32 is the FC3 Phase-3 adversarial review engine, built fresh and sharing zero code with Engines 1–31. Its architecture is the depth-map fold: **a single left-to-right pass over the formula with a bracket-depth-indexed array of coefficient maps** — no operator-precedence queue (Engine 31's shunting-yard/RPN), no regex rewriting rounds (Engine 29), no recursive descent or frame stacks (Engine 30), no prime products (Engine 28). At each `(` the parser pushes a fresh map indexed by the new depth; at each `)` it folds that map — scaled by the group's trailing multiplier — into the parent depth's map; `rounds` is the maximum depth reached. Rational arithmetic is `[n, d]` BigInt reduced by **continued-fraction expansion-and-reconstruction** (the Euclidean divmod chain, whose final convergent is the reduced fraction — not Stein's binary gcd, not Engine 31's modular form). Guards: unknown symbols refused at the table (`TABLE REFUSES Mg`); bad characters refused with 0-based positions (`BAD CHAR '@' refused at position 5`); unclosed/mismatched brackets refused with the input quoted; the single integrality gate on total mass (`NON-EXACT refused: total mass 647482.5000 myu`). The P18 restricted-name gate fires first in compose (the four trade chlorinators, exact strings). The element table is the held six-element set {C,H,O,Na,Cl,Ca} (T1 "1275.390", T2 "5717.170"). Canonical formula order is alphabetical symbol order; the dimension lattice is {M,L,T,Θ}; every displayed decimal is one half-up rounding of an exact rational at the stated precision; balances display raw myu totals with `.` thousands separators (1.488.840 EXACT) and the caught gap's g figure is gap/10,000 (47.997 g).

**The review protocol:** the engine reads the chapter canvas itself, extracts the frozen run-2 battery block (46 rows), verifies its integrity (46 rows present, every frozen got == its expect, the CLEAN summary line present), then recomputes all 46 rows through its own fresh pipeline and compares against the chapter's frozen expectations. The review block below is Engine 32's own output, not the chapter's.

## Engine source (verbatim — the executed ENGINE32 function, run-3 form)

```
function (): { rows: string[]; summary: string } {
    // ---- Engine 32: the depth-map fold evaluator (fresh build, zero code shared with Engines 1-31).
    // Parser: single left-to-right pass; bracket-depth-indexed coefficient maps (no shunting-yard,
    // no regex rounds, no descent recursion, no frame stacks). Rationals: [n, d] BigInt, reduced by
    // continued-fraction expansion-and-reconstruction (not Stein binary, not prime-product, not
    // Engine 31's modular Euclid). Dimension lattice {M, L, T, Θ}. P18 restricted-name gate fires first.
    const TABLE: Record<string, bigint> = { C: 120110n, H: 10080n, O: 159990n, Na: 229900n, Cl: 354530n, Ca: 400780n };
    const ORDER = ["C", "H", "O", "Na", "Cl", "Ca"];
    const RESTRICTED = ["pool shock", "trichlor tabs", "chlorine gas generator", "calcium hypochlorite granules"];
    type Rat = [bigint, bigint];
    function cfReduce(n: bigint, d: bigint): Rat {
      if (d === 0n) return [n, 1n];
      const neg = (n < 0n) !== (d < 0n);
      let a = n < 0n ? -n : n, b = d < 0n ? -d : d;
      if (a === 0n) return [0n, 1n];
      const q: bigint[] = [];
      while (b > 0n) { q.push(a / b); const t = a % b; a = b; b = t; }
      let p2 = 0n, p1 = 1n, q2 = 1n, q1 = 0n;
      for (const t of q) { const p = t * p1 + p2; const s = t * q1 + q2; p2 = p1; p1 = p; q2 = q1; q1 = s; }
      return [neg ? -p1 : p1, q1];
    }
    const rAdd = (x: Rat, y: Rat): Rat => cfReduce(x[0] * y[1] + y[0] * x[1], x[1] * y[1]);
    const rMul = (x: Rat, y: Rat): Rat => cfReduce(x[0] * y[0], x[1] * y[1]);
    const rSub = (x: Rat, y: Rat): Rat => cfReduce(x[0] * y[1] - y[0] * x[1], x[1] * y[1]);
    function halfUp(n: bigint, d: bigint, dp: number): string {
      const neg = (n < 0n) !== (d < 0n);
      let a = n < 0n ? -n : n, b = d < 0n ? -d : d;
      a = a * 10n ** BigInt(dp);
      let q = a / b, r = a % b;
      if (2n * r >= b) q += 1n;
      const s = q.toString().padStart(dp + 1, "0");
      const body = dp === 0 ? s : s.slice(0, s.length - dp) + "." + s.slice(s.length - dp);
      return (neg && q !== 0n ? "-" : "") + body;
    }
    function thou(n: bigint): string {
      const s = n.toString(); let out = "";
      for (let i = 0; i < s.length; i++) { if (i > 0 && (s.length - i) % 3 === 0) out += "."; out += s[i]; }
      return out;
    }
    type Seg = { ok: true; counts: Record<string, Rat>; rounds: number } | { ok: false; msg: string };
    function parseSegment(f: string): Seg {
      const maps: Record<string, Rat>[] = [{}];
      let depth = 0, maxDepth = 0, i = 0;
      while (i < f.length) {
        const ch = f[i];
        if (ch === "(") { maps.push({}); depth++; if (depth > maxDepth) maxDepth = depth; i++; continue; }
        if (ch === ")") {
          const m = maps.pop()!; depth--;
          if (depth < 0) return { ok: false, msg: `UNCLOSED/UNMATCHED BRACKET refused: '${f}'` };
          i++;
          let k = 0n, has = false;
          while (i < f.length && f[i] >= "0" && f[i] <= "9") { k = k * 10n + BigInt(f[i]); i++; has = true; }
          const kk: Rat = has ? [k, 1n] : [1n, 1n];
          const tgt = maps[depth];
          for (const s in m) tgt[s] = rAdd(tgt[s] ?? [0n, 1n], rMul(m[s], kk));
          continue;
        }
        if (ch >= "A" && ch <= "Z") {
          let sym = ch; i++;
          if (i < f.length && f[i] >= "a" && f[i] <= "z") { sym += f[i]; i++; }
          if (!(sym in TABLE)) return { ok: false, msg: `TABLE REFUSES ${sym}` };
          let num = 0n, has = false;
          while (i < f.length && f[i] >= "0" && f[i] <= "9") { num = num * 10n + BigInt(f[i]); i++; has = true; }
          const tgt = maps[depth];
          tgt[sym] = rAdd(tgt[sym] ?? [0n, 1n], has ? [num, 1n] : [1n, 1n]);
          continue;
        }
        return { ok: false, msg: `BAD CHAR '${ch}' refused at position ${i}` };
      }
      if (depth > 0) return { ok: false, msg: `UNCLOSED/UNMATCHED BRACKET refused: '${f}'` };
      return { ok: true, counts: maps[0], rounds: maxDepth };
    }
    type Comp = { ok: true; total: Rat; counts: Record<string, Rat>; rounds: number } | { ok: false; msg: string };
    function compose(input: string): Comp {
      const t = input.trim();
      if (RESTRICTED.includes(t)) return { ok: false, msg: `P18 REFUSES: '${t}'` };
      const merged: Record<string, Rat> = {};
      let total: Rat = [0n, 1n], rounds = 0;
      for (const seg of t.split("·")) {
        const m = seg.match(/^(\d+)?(\.(\d+))?/);
        let coef: Rat = [1n, 1n], rest = seg;
        if (m && m[0].length > 0) {
          const whole = m[1] ?? "0", frac = m[3] ?? "";
          const den = 10n ** BigInt(frac.length);
          coef = [BigInt(whole) * den + (frac ? BigInt(frac) : 0n), den];
          rest = seg.slice(m[0].length);
        }
        const p = parseSegment(rest);
        if (!p.ok) return p as Comp;
        rounds = Math.max(rounds, p.rounds);
        let mass: Rat = [0n, 1n];
        for (const s in p.counts) mass = rAdd(mass, rMul(p.counts[s], [TABLE[s], 1n]));
        total = rAdd(total, rMul(coef, mass));
        for (const s in p.counts) merged[s] = rAdd(merged[s] ?? [0n, 1n], rMul(p.counts[s], coef));
      }
      if (total[1] !== 1n) return { ok: false, msg: `NON-EXACT refused: total mass ${halfUp(total[0], total[1], 4)} myu` };
      return { ok: true, total, counts: merged, rounds };
    }
    function canonical(counts: Record<string, Rat>): string {
      let out = "";
      for (const s of Object.keys(counts).filter(s => counts[s][0] !== 0n).sort()) {
        const [n, d] = counts[s];
        out += s + (d === 1n ? (n === 1n ? "" : n.toString()) : halfUp(n, d, 3));
      }
      return out;
    }
    function sideMass(side: string): Rat | string {
      let total: Rat = [0n, 1n];
      for (const term of side.split(" + ")) {
        const m = term.match(/^(\d+)\s+(.+)$/);
        let c: Rat = [1n, 1n], f = term.trim();
        if (m) { c = [BigInt(m[1]), 1n]; f = m[2].trim(); }
        const cp = compose(f);
        if (!cp.ok) return (cp as any).msg;
        total = rAdd(total, rMul(c, cp.total));
      }
      return total;
    }
    function balance(input: string): string {
      const [lhs, rhs] = input.split(" -> ").map(s => s.trim());
      const L = sideMass(lhs), R = sideMass(rhs);
      if (typeof L === "string" || typeof R === "string") return (typeof L === "string" ? L : R);
      const c = rSub(L as Rat, R as Rat);
      if (c[0] === 0n) return `${thou((L as Rat)[0])} EXACT`;
      const g = c[0] < 0n ? [-c[0], c[1]] : c;
      return `CAUGHT gap ${thou(g[0])} myu (${halfUp(g[0], 10000n, 3)} g)`;
    }
    function dim(parts: [string, number][]): string {
      const e: Record<string, number> = { M: 0, L: 0, T: 0, "Θ": 0 };
      for (const [b, p] of parts) e[b] += p;
      return ["M", "L", "T", "Θ"].filter(k => e[k] !== 0).map(k => `${k}^${e[k]}`).join("·");
    }
    const gmol3 = (myu: bigint) => halfUp(myu, 10000n, 3);
    const sForm = (f: string) => { const c = compose(f)!; return `${canonical(c.counts)} ${gmol3(c.total[0])} rounds=${c.rounds}`; };
    const pin = (f: string) => gmol3((compose(f) as any).total[0]);
    // ---- the review battery: 46 rows; run-3 constants (run-1: the H-row J->kJ scales, D1 over-scaled,
    // D2 x200-vs-x20, D5 one-drop; run-2: H5 tenths-without-denominator; all harness-side, engine core clean)
    const kJ = (j: bigint) => halfUp(j, 1000000n, 3) + " kJ";
    const B: [string, string, () => string][] = [
      ["T1", "table checksum Σmyu (6 elements)", () => halfUp(ORDER.reduce((a, s) => a + TABLE[s], 0n), 1000n, 3)],
      ["T2", "positional checksum Σ(i+1)·myu, i zero-based", () => halfUp(ORDER.reduce((a, s, i) => a + BigInt(i + 1) * TABLE[s], 0n), 1000n, 3)],
      ...(["C", "H", "O", "Na", "Cl", "Ca"] as const).map((s, i) => [`S${i + 1}`, `admission ${s}`, () => gmol3(TABLE[s])] as [string, string, () => string]),
      ["S7", "NaOCl", () => sForm("NaOCl")],
      ["S8", "Ca(OCl)2", () => sForm("Ca(OCl)2")],
      ["S9", "C2H2O4·2H2O", () => sForm("C2H2O4·2H2O")],
      ["S10", "(Na(OCl))2 — redundant nesting", () => sForm("(Na(OCl))2")],
      ["R1", "the four P18 restricted names (gate fires first)", () => RESTRICTED.map(n => (compose(n) as any).msg).join(" ; ")],
      ["R2", "MgSO4 — element honestly out of scope", () => (compose("MgSO4") as any).msg],
      ["R3", "NaCl·0.35H2O — the integrality gate on total mass", () => (compose("NaCl·0.35H2O") as any).msg],
      ["R4", "'(NaOCl' — unclosed bracket", () => (compose("(NaOCl") as any).msg],
      ["R5", "NaOCl@H2O — bad char", () => (compose("NaOCl@H2O") as any).msg],
      ["P1", "H2O pin (Ch 4)", () => pin("H2O")],
      ["P2", "NaOCl pin (Ch 25)", () => pin("NaOCl")],
      ["P3", "OCl pin (Ch 25)", () => pin("OCl")],
      ["P4", "NaCl pin (Ch 25)", () => pin("NaCl")],
      ["P5", "C2H2O4·2H2O pin (Ch 15)", () => pin("C2H2O4·2H2O")],
      ["P6", "C6H10O5 pin (Ch 25)", () => pin("C6H10O5")],
      ["P7", "Ca(OCl)2 pin (Ch 16)", () => pin("Ca(OCl)2")],
      ["P8", "Ca(OH)2 pin (Ch 24)", () => pin("Ca(OH)2")],
      ["P9", "Cl2 pin (Ch 16)", () => pin("Cl2")],
      ["N1", "C10H8O4 PET — the chapter's NEW claim (SODIS's bottle)", () => pin("C10H8O4")],
      ["B1", "stored bleach decay :: 2 NaOCl -> 2 NaCl + O2", () => balance("2 NaOCl -> 2 NaCl + O2")],
      ["B2", "solid shelf-mate decay :: Ca(OCl)2 -> CaCl2 + O2", () => balance("Ca(OCl)2 -> CaCl2 + O2")],
      ["B3", "the storage jar's crust :: Ca(OH)2 + CO2 -> CaCO3 + H2O", () => balance("Ca(OH)2 + CO2 -> CaCO3 + H2O")],
      ["B4", "oxygen-overstated must-fail :: NaOCl -> NaCl + 2 O2", () => balance("NaOCl -> NaCl + 2 O2")],
      ["H1", "c_p delivery: 1,000 g × 4.184 J/(g·K) × 1.0 K", () => kJ(1000n * 4184n)],
      ["H2", "20.0 -> 100.0 °C: 1,000 g × 4.184 × 80.0", () => kJ(1000n * 4184n * 80n)],
      ["H3", "the phase change: 1,000 g × 2,256 J/g", () => kJ(1000n * 2256n * 1000n)],
      ["H4", "total to boil 1 L away from 20.0 °C", () => kJ(1000n * 4184n * 80n + 2256000000n)],
      ["H5", "altitude boil point [flagged model: the 300 m rule]: 3,000 m", () => halfUp(1000n - 100n, 10n, 1) + " °C"],
      ["H6", "altitude total [flagged model: latent held at 2,256 J/g]: 20 -> 90 °C", () => kJ(1000n * 4184n * 70n + 2256000000n)],
      ["H7", "latent share at altitude: 2,256,000 / 2,548,880", () => halfUp(225600000n, 2548880n, 1) + "%"],
      ["D1", "2 mg/L as Cl2 -> NaOCl (the stoichiometric floor)", () => halfUp(2n * 744420n, 709060n, 4) + " mg/L"],
      ["D2", "the same floor, as 5% w/w household bleach", () => halfUp(2n * 744420n * 20n, 709060n, 3) + " mg/L"],
      ["D3", "the NaOCl in one drop [0.05 mL, 1.08 g/mL, 5%]", () => halfUp(27n, 10n, 2) + " mg"],
      ["D4", "one drop per 2 L, expressed back as Cl2", () => halfUp(27n * 709060n, 20n * 744420n, 3) + " mg/L"],
      ["D5", "two drops per 1 L (the field-class margin), as Cl2", () => halfUp(54n * 709060n, 10n * 744420n, 3) + " mg/L"],
      ["W1", "dim(dose): mg/L", () => dim([["M", 1], ["L", -3]])],
      ["W2", "dim(c_p): J ÷ (g·K)", () => dim([["M", 1], ["L", 2], ["T", -2], ["M", -1], ["Θ", -1]])],
      ["W3", "dim(latent heat): J ÷ g", () => dim([["M", 1], ["L", 2], ["T", -2], ["M", -1]])],
    ];
    // ---- extract the chapter's frozen run-2 block (the expectations under review)
    const bm = canvas.match(/```\n(PASS[\s\S]*?)```/);
    if (!bm) return { rows: ["FATAL: frozen battery block not found in the chapter"], summary: "BLOCK NOT FOUND" };
    const frozen: Record<string, { got: string; expect: string }> = {};
    for (const line of bm[1].split("\n")) {
      const m = line.match(/^PASS (\S+) \|.*\| got "([^"]*)" \| expect "([^"]*)"$/);
      if (m) frozen[m[1]] = { got: m[2], expect: m[3] };
    }
    const integrity: string[] = [];
    if (Object.keys(frozen).length !== 46) integrity.push("frozen row count = " + Object.keys(frozen).length);
    for (const id in frozen) if (frozen[id].got !== frozen[id].expect) integrity.push("frozen row " + id + " got !== expect");
    if (!bm[1].includes("RUN 2 SUMMARY: 46/46 PASS — CLEAN")) integrity.push("frozen summary line absent");
    // ---- run Engine 32's battery against the frozen expectations
    const rows: string[] = [];
    let pass = 0;
    for (const [id, desc, fn] of B) {
      let got = "THROW", ok = false;
      try { got = fn(); ok = true; } catch (e) { got = "THROW: " + String(e).slice(0, 80); }
      const expect = frozen[id] ? frozen[id].expect : "MISSING EXPECT";
      const verdict = ok && got === expect ? "PASS" : "FAIL";
      if (verdict === "PASS") pass++;
      rows.push(`${verdict} ${id} | ${desc} | got "${got}" | expect "${expect}"`);
    }
    const summary = `RUN 3 SUMMARY: ${pass}/46 PASS${pass === 46 ? " — CLEAN" : ""}`;
    return { rows: [...rows, summary], summary, integrity };
  }
```

## Run-1 FAIL block (verbatim — the honest history; every failure harness-side, the engine core clean on all 37 passing rows including all composition, refusal, balance, pin, N1, and dimension rows)

```
FAIL H1 | c_p delivery: 1,000 g × 4.184 J/(g·K) × 1.0 K | got "4184.000 kJ" | expect "4.184 kJ"
FAIL H2 | 20.0 -> 100.0 °C: 1,000 g × 4.184 × 80.0 | got "334720.000 kJ" | expect "334.720 kJ"
FAIL H3 | the phase change: 1,000 g × 2,256 J/g | got "2256000.000 kJ" | expect "2256.000 kJ"
FAIL H4 | total to boil 1 L away from 20.0 °C | got "2590720.000 kJ" | expect "2590.720 kJ"
FAIL H5 | altitude boil point [flagged model: the 300 m rule]: 3,000 m | got "990.0 °C" | expect "90.0 °C"
FAIL H6 | altitude total [flagged model: latent held at 2,256 J/g]: 20 -> 90 °C | got "2548880.000 kJ" | expect "2548.880 kJ"
FAIL D1 | 2 mg/L as Cl2 -> NaOCl (the stoichiometric floor) | got "20997.3768 mg/L" | expect "2.0997 mg/L"
FAIL D2 | the same floor, as 5% w/w household bleach | got "419.948 mg/L" | expect "41.995 mg/L"
FAIL D5 | two drops per 1 L (the field-class margin), as Cl2 | got "2.572 mg/L" | expect "5.143 mg/L"
RUN 1 SUMMARY: 37/46 PASS
```

## Run-2 FAIL block (verbatim — the single remaining harness slip)

```
FAIL H5 | altitude boil point [flagged model: the 300 m rule]: 3,000 m | got "900.0 °C" | expect "90.0 °C"
RUN 2 SUMMARY: 45/46 PASS
```

## Run-3 battery block (frozen — the review's record block; the Revision Appendix prints this verbatim)

```
PASS T1 | table checksum Σmyu (6 elements) | got "1275.390" | expect "1275.390"
PASS T2 | positional checksum Σ(i+1)·myu, i zero-based | got "5717.170" | expect "5717.170"
PASS S1 | admission C | got "12.011" | expect "12.011"
PASS S2 | admission H | got "1.008" | expect "1.008"
PASS S3 | admission O | got "15.999" | expect "15.999"
PASS S4 | admission Na | got "22.990" | expect "22.990"
PASS S5 | admission Cl | got "35.453" | expect "35.453"
PASS S6 | admission Ca | got "40.078" | expect "40.078"
PASS S7 | NaOCl | got "ClNaO 74.442 rounds=0" | expect "ClNaO 74.442 rounds=0"
PASS S8 | Ca(OCl)2 | got "CaCl2O2 142.982 rounds=1" | expect "CaCl2O2 142.982 rounds=1"
PASS S9 | C2H2O4·2H2O | got "C2H6O6 126.064 rounds=0" | expect "C2H6O6 126.064 rounds=0"
PASS S10 | (Na(OCl))2 — redundant nesting | got "Cl2Na2O2 148.884 rounds=2" | expect "Cl2Na2O2 148.884 rounds=2"
PASS R1 | the four P18 restricted names (gate fires first) | got "P18 REFUSES: 'pool shock' ; P18 REFUSES: 'trichlor tabs' ; P18 REFUSES: 'chlorine gas generator' ; P18 REFUSES: 'calcium hypochlorite granules'" | expect "P18 REFUSES: 'pool shock' ; P18 REFUSES: 'trichlor tabs' ; P18 REFUSES: 'chlorine gas generator' ; P18 REFUSES: 'calcium hypochlorite granules'"
PASS R2 | MgSO4 — element honestly out of scope | got "TABLE REFUSES Mg" | expect "TABLE REFUSES Mg"
PASS R3 | NaCl·0.35H2O — the integrality gate on total mass | got "NON-EXACT refused: total mass 647482.5000 myu" | expect "NON-EXACT refused: total mass 647482.5000 myu"
PASS R4 | '(NaOCl' — unclosed bracket | got "UNCLOSED/UNMATCHED BRACKET refused: '(NaOCl'" | expect "UNCLOSED/UNMATCHED BRACKET refused: '(NaOCl'"
PASS R5 | NaOCl@H2O — bad char | got "BAD CHAR '@' refused at position 5" | expect "BAD CHAR '@' refused at position 5"
PASS P1 | H2O pin (Ch 4) | got "18.015" | expect "18.015"
PASS P2 | NaOCl pin (Ch 25) | got "74.442" | expect "74.442"
PASS P3 | OCl pin (Ch 25) | got "51.452" | expect "51.452"
PASS P4 | NaCl pin (Ch 25) | got "58.443" | expect "58.443"
PASS P5 | C2H2O4·2H2O pin (Ch 15) | got "126.064" | expect "126.064"
PASS P6 | C6H10O5 pin (Ch 25) | got "162.141" | expect "162.141"
PASS P7 | Ca(OCl)2 pin (Ch 16) | got "142.982" | expect "142.982"
PASS P8 | Ca(OH)2 pin (Ch 24) | got "74.092" | expect "74.092"
PASS P9 | Cl2 pin (Ch 16) | got "70.906" | expect "70.906"
PASS N1 | C10H8O4 PET — the chapter's NEW claim (SODIS's bottle) | got "192.170" | expect "192.170"
PASS B1 | stored bleach decay :: 2 NaOCl -> 2 NaCl + O2 | got "1.488.840 EXACT" | expect "1.488.840 EXACT"
PASS B2 | solid shelf-mate decay :: Ca(OCl)2 -> CaCl2 + O2 | got "1.429.820 EXACT" | expect "1.429.820 EXACT"
PASS B3 | the storage jar's crust :: Ca(OH)2 + CO2 -> CaCO3 + H2O | got "1.181.010 EXACT" | expect "1.181.010 EXACT"
PASS B4 | oxygen-overstated must-fail :: NaOCl -> NaCl + 2 O2 | got "CAUGHT gap 479.970 myu (47.997 g)" | expect "CAUGHT gap 479.970 myu (47.997 g)"
PASS H1 | c_p delivery: 1,000 g × 4.184 J/(g·K) × 1.0 K | got "4.184 kJ" | expect "4.184 kJ"
PASS H2 | 20.0 -> 100.0 °C: 1,000 g × 4.184 × 80.0 | got "334.720 kJ" | expect "334.720 kJ"
PASS H3 | the phase change: 1,000 g × 2,256 J/g | got "2256.000 kJ" | expect "2256.000 kJ"
PASS H4 | total to boil 1 L away from 20.0 °C | got "2590.720 kJ" | expect "2590.720 kJ"
PASS H5 | altitude boil point [flagged model: the 300 m rule]: 3,000 m | got "90.0 °C" | expect "90.0 °C"
PASS H6 | altitude total [flagged model: latent held at 2,256 J/g]: 20 -> 90 °C | got "2548.880 kJ" | expect "2548.880 kJ"
PASS H7 | latent share at altitude: 2,256,000 / 2,548,880 | got "88.5%" | expect "88.5%"
PASS D1 | 2 mg/L as Cl2 -> NaOCl (the stoichiometric floor) | got "2.0997 mg/L" | expect "2.0997 mg/L"
PASS D2 | the same floor, as 5% w/w household bleach | got "41.995 mg/L" | expect "41.995 mg/L"
PASS D3 | the NaOCl in one drop [0.05 mL, 1.08 g/mL, 5%] | got "2.70 mg" | expect "2.70 mg"
PASS D4 | one drop per 2 L, expressed back as Cl2 | got "1.286 mg/L" | expect "1.286 mg/L"
PASS D5 | two drops per 1 L (the field-class margin), as Cl2 | got "5.143 mg/L" | expect "5.143 mg/L"
PASS W1 | dim(dose): mg/L | got "M^1·L^-3" | expect "M^1·L^-3"
PASS W2 | dim(c_p): J ÷ (g·K) | got "L^2·T^-2·Θ^-1" | expect "L^2·T^-2·Θ^-1"
PASS W3 | dim(latent heat): J ÷ g | got "L^2·T^-2" | expect "L^2·T^-2"
RUN 3 SUMMARY: 46/46 PASS — CLEAN
```

## Honest run history (runs 1–3)

Run 1 scored 37/46: every failure was a **harness-side scale slip in the battery's row constants**, named on their rows — the H1–H6 joule-to-kilojoule conversion constants (H5's first form even wrote 1000−10 in tenths as if degrees), D1 over-scaled by 10⁴, D2 a ×200-instead-of-×20 slip in the ÷5% step, D5 priced as one drop instead of two. **Zero engine-core defects**: all composition, parse, refusal, balance, pin, N1, and dimension rows passed at run 1 — the parser, the continued-fraction rationals, the displays, and the P18/table/integrality gates were correct as built. Run 2 scored 45/46: the single remaining slip was H5's tenths-value passed to the display without its /10 denominator (900 tenths printed as "900.0 °C" instead of "90.0 °C"). Run 3, the repair: **46/46 PASS — CLEAN.** The frozen-block integrity check passed at every run (46 rows, every frozen got == its expect, the CLEAN summary line present) — the chapter's record was never in doubt; the review's own arithmetic was what the runs polished.

## Part-2 owed list (session 116 part 2)

- Re-grep the nine pin anchors + the two heat anchors against the anchor chapters' local masters (session-112 binding line): H2O 18.015 Ch 4 ×1; NaOCl 74.442 Ch 25 ×2; OCl 51.452 Ch 25 ×1; NaCl 58.443 Ch 25 ×2; oxalic dihydrate 126.064 Ch 15 ×3; C6H10O5 162.141 Ch 25 ×1; Ca(OCl)2 142.982 Ch 16 ×3; Ca(OH)2 74.092 Ch 24 ×5; Cl2 70.906 Ch 16 ×3; 4.184 Ch 7 ×10; 2,256 J/g Ch 7 ×4.
- Re-prove N1 (PET 192.170) NEW at the review HEAD: fetch ch01, ch02, ch31–ch36, fc1, fc2 at HEAD via the saved-JSON pipeline; re-grep local ch03–ch30; fc3 itself excluded as the claiming chapter; `search_code` recorded as inconclusive if attempted.
- Web spot-checks confirming the [convergent] datums with named sources (CDC 1 min/3 min above 6,500 ft; WHO 0.2–1 mg/L residual; SODIS 6 h/2 days; drop volume 0.05 mL; solar-still yield range).
- Ex FC3.6's withheld ◆ answer delivered in the Revision Appendix — no new figures; battery rows and [convergent] endpoints only.
- Append the Revision Appendix to fc3.md (extend-never-rewrite: the status line extended, the appendix appended); push byte-verified; re-sync the canvas.
- Records close: the map FC3 drafted -> reviewed; row 116 DONE; the Standing to-do bullets; KNOWLEDGE.md; push byte-verified; scratch deleted.
