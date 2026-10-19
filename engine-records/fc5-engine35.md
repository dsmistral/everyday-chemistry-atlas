# Engine 35 — the span-memo engine (FC5 "Soil and Fertility: The Garden Under the Bench", session 119 part 1, 2026-10-19)

Provenance: fresh build for FC5's authoring session (119), zero code shared with Engines 1–34. Designed at the checkpoint `fc5-design-notes.md` BEFORE the build (written 2026-10-19, before any engine code ran). Binding lines in force: session-100 (every NEW composition grepped against every prior page before the page freezes — N1's repo sweep owed to part 2), session-102 (every worked figure a battery row), session-104 (convergence at displayed precision), session-112 (attribution greps in the authoring session — owed at part 2), extend-never-rewrite, ALWAYS-SYNC.

## 1. Design spec

**The span-memo engine.** Distinct from every prior engine: Engine 25 recursive descent with no memo; 26 token-tape + explicit frame stack; 27 unit lattice + dual tables; 28 prime products; 29 regex parallel rounds; 30 stack-descent fixed-scale + Stein gcd; 31 RPN shunting-yard; 32 bracket-depth coefficient maps; 33 fixed-point rewrites; 34 census-tally literal expansion. Engine 35's shape:

1. **Span-table prepass.** A single counter scan builds the bracket-span table: for each `(` its matching `)` index (UNCLOSED/UNMATCHED thrown here).
2. **Memoized group parsing.** `walk` walks a segment; on `(` it recurses into the span's inner substring through `parseMemo`, a Map keyed on the inner string — repeated groups (the `(CH3)` of S3, the `(CO3)` of P12) parse exactly once per distinct inner string. No prior engine memoized.
3. **Vector-basis counts.** Every composition is an 11-slot integer vector over the alphabetical element basis {C, Ca, Cl, H, K, Mg, N, Na, O, S, Si}; **mass = one dot product** with the myu vector; balances are exact vector equations; no per-element tally passes, no rationals, no gcd.
4. **Integer myu arithmetic** (all totals < 2^53; the largest battery figure 3,721,440 myu); display at 3 dp by integer division at the 10-myu scale, half-up; the residual `r = myu mod 10` printed on every composition row (r=0 throughout — every admission myu is a multiple of 10, so every composition is exact at 3 dp).
5. **Gates, in order:** the P18 restricted-name gate FIRST (label and formula scanned, case-insensitive; ANFO/gunpowder/dynamite/fireworks/rat poison/fuel oil), then the admission gate (the 11-element basis; P, B, F, I and every two-char metal of the wider table refused BY NAME — the engine prints which element was refused), then syntax (UNCLOSED, UNMATCHED, BAD CHAR at its index, count cap 999), then the non-integer hydrate gate (the Engine-29 class: `0.35`-style segment coefficients refused).
6. **The hydrate dot** splits segments at `·`; a leading integer (7H2O, 2 CO(NH2)2) is a whole-segment coefficient; a leading decimal REFUSES (R6).
7. **Dimensions** {M, L, T, Θ} as integer vectors; the canonical DORDER display ALWAYS prints the exponent (M^1·L^2·T^-3 — the FC1/FC2 precedent; the run-1 D2 display repair).
8. **Checksums:** T1 straight Σmyu of the 11 admissions; T2 positional Σ(i+1)·myu in the engine's own alphabetical order.

**Admission basis (11 held elements, myu):** C 120110, Ca 400780, Cl 354530, H 10080, K 390980, Mg 243050, N 140070, Na 229900, O 159990, S 320600, Si 280850. T1 = 2,650,940 myu (265.094). T2 = 15,993,730 myu (1599.373). **P is refused at the standing element-table law** (inherited from Ch 20/24; the refusal printed in the gate log — rows R1/R2/L4).

## 2. Honest run history

- **Run 1: 54/56.** Two FAILs, both harness-side, zero engine-core defects (the parser, the memo, every gate, the balances, the dot products, and both checksums clean at run 1):
  - **C4** — the hand expectation "44.44%" was the author's own slip: 720660/1621410 = 0.444464 → **44.45%**; the machine right, the hand wrong (the FC2-S2 class, again). Expectation corrected.
  - **D2** — the engine's dimStr omitted the exponent 1 (printed `M·L^2·T^-3`); the house canonical (FC1's repaired display, FC2's DORDER) prints it: `M^1·L^2·T^-3`. Display repaired: the exponent is ALWAYS printed.
- **Run 2 (the repair pass, nothing else touched): 56/56 PASS — CLEAN.** The frozen run-2 battery block below is the chapter's record.

## 3. The frozen run-2 battery block (56 rows)

```
 PASS T1 | admission table checksum Σmyu (11 elements) | got "265.094 (2650940 myu)" | expect "265.094 (2650940 myu)"
 PASS T2 | positional checksum Σ(i+1)·myu, alphabetical order | got "1599.373 (15993730 myu)" | expect "1599.373 (15993730 myu)"
 PASS S1 | self: H2O sanity | got "H2O 180150 myu = 18.015 r=0" | expect "H2O 180150 myu = 18.015 r=0"
 PASS S2 | self: the dot-product identity | got "dot: 20160+159990=180150 EXACT" | expect "dot: 20160+159990=180150 EXACT"
 PASS S3 | self: bracket scale (CH3)2CO -> C3H6O | got "(CH3)2CO 580800 myu = 58.080 r=0" | expect "(CH3)2CO 580800 myu = 58.080 r=0"
 PASS S4 | self: hydrate dot MgSO4·7H2O | got "MgSO4·7H2O 2464660 myu = 246.466 r=0" | expect "MgSO4·7H2O 2464660 myu = 246.466 r=0"
 PASS S5 | self: span-memo the long chain CH3(CH2)16COOH (Ch 23 stearic cross) | got "CH3(CH2)16COOH 2844840 myu = 284.484 r=0" | expect "CH3(CH2)16COOH 2844840 myu = 284.484 r=0"
 PASS S6 | self: canonical display, scrambled input O6C6H12 | got "C6H12O6 1801560 myu = 180.156 r=0" | expect "C6H12O6 1801560 myu = 180.156 r=0"
 PASS R1 | refusal: P at the admission gate (bone meal's Ca3(PO4)2 — the standing law) | got "REFUSED admission: P" | expect "REFUSED admission: P"
 PASS R2 | refusal: DAP (NH4)2HPO4 (the 46 face refused) | got "REFUSED admission: P" | expect "REFUSED admission: P"
 PASS R3 | refusal: ANFO at the P18 name gate (the fertilizer shelf's own shadow) | got "REFUSED P18: ANFO" | expect "REFUSED P18: ANFO"
 PASS R4 | refusal: unclosed group | got "UNCLOSED (" | expect "UNCLOSED ("
 PASS R5 | refusal: bad char | got "BAD CHAR "@" at 3" | expect "BAD CHAR "@" at 3"
 PASS R6 | refusal: non-integer hydrate (the Engine-29 class) | got "REFUSED non-integer hydrate" | expect "REFUSED non-integer hydrate"
 PASS P1 | pin H2O 18.015 Ch 4 | got "18.015 r=0" | expect "18.015 r=0"
 PASS P2 | pin NH3 17.031 Ch 20 | got "17.031 r=0" | expect "17.031 r=0"
 PASS P3 | pin N2 28.014 Ch 10 | got "28.014 r=0" | expect "28.014 r=0"
 PASS P4 | pin CO2 44.009 Ch 20 | got "44.009 r=0" | expect "44.009 r=0"
 PASS P5 | pin urea CO(NH2)2 60.056 Ch 20 | got "60.056 r=0" | expect "60.056 r=0"
 PASS P6 | pin (NH4)2SO4 132.134 Ch 20 | got "132.134 r=0" | expect "132.134 r=0"
 PASS P7 | pin K2CO3 138.204 Ch 14 | got "138.204 r=0" | expect "138.204 r=0"
 PASS P8 | pin K2O 94.195 Ch 14 | got "94.195 r=0" | expect "94.195 r=0"
 PASS P9 | pin CaCO3 100.086 Ch 14 | got "100.086 r=0" | expect "100.086 r=0"
 PASS P10 | pin CaO 56.077 Ch 14 | got "56.077 r=0" | expect "56.077 r=0"
 PASS P11 | pin Ca(OH)2 74.092 Ch 24 | got "74.092 r=0" | expect "74.092 r=0"
 PASS P12 | pin CaMg(CO3)2 184.399 Ch 30 | got "184.399 r=0" | expect "184.399 r=0"
 PASS P13 | pin MgSO4·7H2O 246.466 Ch 4 | got "246.466 r=0" | expect "246.466 r=0"
 PASS P14 | pin SiO2 60.083 Ch 30 | got "60.083 r=0" | expect "60.083 r=0"
 PASS N1 | NEW: biuret NH2CONHCONH2 = C2H5N3O2 (zero-hit local; repo sweep owed pre-freeze) | got "biuret C2H5N3O2 1030810 myu = 103.081 r=0" | expect "biuret C2H5N3O2 1030810 myu = 103.081 r=0"
 PASS B1 | balance: urea hydrolysis CO(NH2)2 + H2O = 2 NH3 + CO2 (Ch 36 corridor class) | got "LHS 780710 RHS 780710 gap 0 EXACT" | expect "LHS 780710 RHS 780710 gap 0 EXACT"
 PASS B2 | balance: biuret from urea 2 CO(NH2)2 = C2H5N3O2 + NH3 | got "LHS 1201120 RHS 1201120 gap 0 EXACT" | expect "LHS 1201120 RHS 1201120 gap 0 EXACT"
 PASS B3 | balance: nitrification NH3 + 2 O2 = HNO3 + H2O | got "LHS 810270 RHS 810270 gap 0 EXACT" | expect "LHS 810270 RHS 810270 gap 0 EXACT"
 PASS B4 | balance: the nitrate->nitrite leg 2 HNO3 = 2 HNO2 + O2 [formal model] | got "LHS 1260240 RHS 1260240 gap 0 EXACT" | expect "LHS 1260240 RHS 1260240 gap 0 EXACT"
 PASS B5 | balance: carbonation Ca(OH)2 + CO2 = CaCO3 + H2O | got "LHS 1181010 RHS 1181010 gap 0 EXACT" | expect "LHS 1181010 RHS 1181010 gap 0 EXACT"
 PASS B6 | balance: dolomite burn CaMg(CO3)2 = CaO + MgO + 2 CO2 (Ch 30 E12 class) | got "LHS 1843990 RHS 1843990 gap 0 EXACT" | expect "LHS 1843990 RHS 1843990 gap 0 EXACT"
 PASS B7 | balance: the char model C6H10O5 = 6 C + 5 H2O [flagged model] | got "LHS 1621410 RHS 1621410 gap 0 EXACT" | expect "LHS 1621410 RHS 1621410 gap 0 EXACT"
 PASS B8 | MUST-FAIL: one-H-short biuret C2H4N3O2 (the mis-typed condensation) | got "LHS 1201120 RHS 1191040 gap 10080 CAUGHT" | expect "LHS 1201120 RHS 1191040 gap 10080 CAUGHT"
 PASS C1 | C:N target 30:1 [convergent Cornell] — N as fraction of C+N | got "1/31 = 3.226% N of C+N" | expect "1/31 = 3.226% N of C+N"
 PASS C2 | C:N blend: grass 45/2.25 (20:1) + sawdust 480/1.2 per kg (400:1) [convergent band inputs] -> 30:1 | got "225/444 = 0.507 kg sawdust per kg grass" | expect "225/444 = 0.507 kg sawdust per kg grass"
 PASS C3 | C:N the urea credit: 100 kg leaves, %C 50, C:N 50:1 -> 30:1; deficit at urea's own %N | got "2000/3 g N deficit -> 1429 g urea" | expect "2000/3 g N deficit -> 1429 g urea"
 PASS C4 | biochar: the B7 char yield and its C:N face | got "720660/1621410 = 44.45% char; C:N undefined (no N)" | expect "720660/1621410 = 44.45% char; C:N undefined (no N)"
 PASS L1 | NPK: urea %N (Ch 20's own census) | got "280140/600560 = 46.65% N" | expect "280140/600560 = 46.65% N"
 PASS L2 | NPK: K2CO3 %K2O (Ch 14's potash convention) | got "941950/1382040 = 68.16% K2O" | expect "941950/1382040 = 68.16% K2O"
 PASS L3 | NPK: the ash label read — 1 kg ash at the 7% K2O-eq band [convergent] | got "70 g K2O-eq -> 102.7 g K2CO3-eq per kg ash" | expect "70 g K2O-eq -> 102.7 g K2CO3-eq per kg ash"
 PASS L4 | NPK: the DAP 18-46-0 label — the 46 face refused at the table | got "REFUSED admission: P" | expect "REFUSED admission: P"
 PASS H1 | heat: glucose oxidation C6H12O6 + 6 O2 = 6 CO2 + 6 H2O + dH | got "LHS 3721440 RHS 3721440 gap 0 EXACT; dH -2.87 MJ/mol [convergent]" | expect "LHS 3721440 RHS 3721440 gap 0 EXACT; dH -2.87 MJ/mol [convergent]"
 PASS H2 | heat: the 50-kg pile ledger, +20 K, c_p 4.184 [flagged model: water-dominated] | got "4184000 J / 2870000 = 1.458 mol -> 262.6 g glucose-equivalent" | expect "4184000 J / 2870000 = 1.458 mol -> 262.6 g glucose-equivalent"
 PASS H3 | heat: the thermophilic band edges [55-65 C, Cornell] on the same ledger | got "7322000 J -> 459.6 g; 9414000 J -> 590.9 g" | expect "7322000 J -> 459.6 g; 9414000 J -> 590.9 g"
 PASS H4 | heat: Ch 14's slaking band on the shell-kiln cross (4.746 mol CaO, -64.8 kJ/mol) | got "4.746 x 64.8 = 307.5 kJ [convergent band -63.7..-65.2]" | expect "4.746 x 64.8 = 307.5 kJ [convergent band -63.7..-65.2]"
 PASS D1 | dim: specific heat c_p [J/(g·K)] | got "L^2·T^-2·Θ^-1" | expect "L^2·T^-2·Θ^-1"
 PASS D2 | dim: power | got "M^1·L^2·T^-3" | expect "M^1·L^2·T^-3"
 PASS D3 | dim: C:N and %N | got "dimensionless" | expect "dimensionless"
 PASS X1 | cross: Ch 36's urea corridor 780710 reproduced from FC5's table | got "780710 EXACT (Ch 36 E3/E7 class)" | expect "780710 EXACT (Ch 36 E3/E7 class)"
 PASS X2 | cross: Ch 30's dolomite 1843990 reproduced | got "1843990 EXACT (Ch 30)" | expect "1843990 EXACT (Ch 30)"
 PASS X3 | cross: Ch 14's potash convention 68.16% reproduced | got "68.16 EXACT (Ch 14)" | expect "68.16 EXACT (Ch 14)"
 PASS X4 | cross: Ch 20's urea %N 46.65% reproduced | got "46.65 EXACT (Ch 20)" | expect "46.65 EXACT (Ch 20)"
RUN 2 SUMMARY: 56/56 PASS — CLEAN
```

## 4. The run-1 FAIL lines, preserved verbatim

```
 FAIL C4 | biochar: the B7 char yield and its C:N face | got "720660/1621410 = 44.45% char; C:N undefined (no N)" | expect "720660/1621410 = 44.44% char; C:N undefined (no N)"
 FAIL D2 | dim: power | got "M·L^2·T^-3" | expect "M^1·L^2·T^-3"
RUN 1 SUMMARY: 54/56 PASS
```

## 5. Engine provenance and battery design notes

- **N1 = biuret C2H5N3O2, 1,030,810 myu = 103.081** [computed]. Zero-hit on every local master ch03–ch30 and the local fc2/fc3/fc4 canvases (grepped this session: "biuret"/Biuret/103.08 → zero). The repo-only pages (ch01, ch02, ch31–ch35, ch36, fc1) are OWED at part 2 BEFORE the page freezes, via the saved-JSON pipeline; the reused-pin conversion protocol applies if any prior page prices it. The formation balance B2: 2 CO(NH2)2 = C2H5N3O2 + NH3, 1,201,120 myu EXACT — urea's own thermal-condensation shadow, the fertilizer trade's seedling-safety quality limit (the web check owed at part 2).
- **B4 is a formal model** (2 HNO3 = 2 HNO2 + O2 — the redox-neutral nitrate→nitrite leg as bookkeeping; the biology named in prose, the mechanism disclaimed). **B7 is the char model** [flagged model: bookkeeping-exact, mechanism-disclaimed] on Ch 25's cellulose pin. **H2/H3's c_p = 4.184** is [flagged model: water-dominated wet pile] on Ch 7's own heat anchor.
- **The P18 gate on FC5's own field:** ammonium nitrate is simultaneously a fertilizer label (Ch 20's census) and the ANFO precursor — the name refused at the gate, the recognition printed as taught content. **Elemental P** refused per the standing Ch 20/24 law — bone meal's Ca5-class mineral, DAP's 46 face, and superphosphate all recognition-only; the refusal rows (R1/R2/L4) are the fence executed in the gate log.
- Battery census: T 2, S 6, R 6, P 14, N 1, B 8, C 4, L 4, H 4, D 3, X 4 = **56 rows**.
- Pins re-greps in owners' own pages (raw `grep -o` counts for the Chapter Ledger, the session-112 line) OWED at part 2.

## 6. The run-2 source, verbatim

```typescript
// ===== ENGINE 35: the span-memo engine (fresh build, session 119) — RUN 2 =====
// Repairs from run 1 (both harness-side, zero engine-core defects):
//  (a) C4 expectation corrected: 720660/1621410 = 44.4464% -> "44.45" (hand 44.44 was the slip; machine right)
//  (b) dimStr display repair: exponent ALWAYS printed (the FC1/FC2 DORDER canonical: M^1·L^2·T^-3)
const MYU: any = {C:120110,H:10080,O:159990,N:140070,Na:229900,Mg:243050,S:320600,Cl:354530,K:390980,Ca:400780,Si:280850};
const TWO = ["Ca","Na","Mg","Si","Cl"];
const NOTADM2 = ["Fe","Cu","Ag","Al","Mn","Zn","Ba","Pb","Sn","Cr","Ni","Li","Br","Hg","Ti","Sb","Co","He","Ne","Ar"];
const NOTADM1 = ["P","B","F","I","Xe","Kr"];
const P18N = ["ANFO","gunpowder","black powder","dynamite","fireworks","rat poison","fuel oil"];
const EA = ["C","Ca","Cl","H","K","Mg","N","Na","O","S","Si"];
const vi: any = {}; EA.forEach((e,i)=>vi[e]=i);
const mv = EA.map(e=>MYU[e]);
const dot = (v:number[])=>v.reduce((a,x,i)=>a+x*mv[i],0);
const disp3 = (myu:number)=>{const x=Math.floor((myu+5)/10);const w=Math.floor(x/1000);let f=String(x%1000);while(f.length<3)f="0"+f;return w+"."+f;};
const rOf = (myu:number)=>myu%10;
const gate = (s:string)=>{const u=s.toUpperCase();for(const n of P18N) if(u.includes(n.toUpperCase())) return "REFUSED P18: "+n; return null;};

function spans(s:string){const st:number[]=[];const m:number[]=Array(s.length).fill(-1);
  for(let i=0;i<s.length;i++){ if(s[i]==="(") st.push(i); else if(s[i]===")"){ if(!st.length) throw new Error("UNMATCHED )"); m[st.pop()!]=i; } }
  if(st.length) throw new Error("UNCLOSED ("); return m;}

const memo = new Map<string,number[]>();
function walk(s:string):number[] {
  const v = EA.map(()=>0); const m = spans(s); let i=0;
  while(i<s.length){
    const ch = s[i];
    if(ch===" "){i++;continue;}
    if(ch==="("){ const j=m[i]; const inner=s.slice(i+1,j); const gv=parseMemo(inner); i=j+1;
      let k=i; while(k<s.length&&s[k]>="0"&&s[k]<="9") k++;
      let c=1; if(k>i){c=parseInt(s.slice(i,k)); if(c>999) throw new Error("REFUSED count cap");}
      for(let t=0;t<11;t++) v[t]+=gv[t]*c; i=k; continue; }
    const two = s.substr(i,2);
    if(TWO.includes(two)){ let k=i+2; while(k<s.length&&s[k]>="0"&&s[k]<="9") k++;
      let c=1; if(k>i+2){c=parseInt(s.slice(i+2,k)); if(c>999) throw new Error("REFUSED count cap");}
      v[vi[two]]+=c; i=k; continue; }
    if(MYU[ch]!==undefined){ let k=i+1; while(k<s.length&&s[k]>="0"&&s[k]<="9") k++;
      let c=1; if(k>i+1){c=parseInt(s.slice(i+1,k)); if(c>999) throw new Error("REFUSED count cap");}
      v[vi[ch]]+=c; i=k; continue; }
    if(NOTADM2.includes(two)) throw new Error("REFUSED admission: "+two);
    if(NOTADM1.includes(ch)) throw new Error("REFUSED admission: "+ch);
    throw new Error('BAD CHAR "'+ch+'" at '+i);
  }
  return v;
}
function parseMemo(inner:string):number[]{ if(memo.has(inner)) return memo.get(inner)!.slice(); const v=walk(inner); memo.set(inner,v.slice()); return v; }

function segVec(sRaw:string):number[] {
  let s = sRaw.trim(); let coef = 1;
  const m = s.match(/^(\d+)(\.\d+)?/);
  if(m){ if(m[2]) throw new Error("REFUSED non-integer hydrate"); coef=parseInt(m[1]); if(coef>999) throw new Error("REFUSED count cap"); s=s.slice(m[1].length); }
  return walk(s).map(x=>x*coef);
}
function compose(f:string,label=""){ const g=gate(label)||gate(f); if(g) throw new Error(g);
  const v = EA.map(()=>0);
  for(const sg of f.split("·")){ const sv=segVec(sg); for(let t=0;t<11;t++) v[t]+=sv[t]; }
  const myu = dot(v); return {myu, v, disp:disp3(myu), r:rOf(myu)};
}
function side(str:string){ const v=EA.map(()=>0); for(const t of str.split("+")){ const sv=segVec(t); for(let i2=0;i2<11;i2++) v[i2]+=sv[i2]; } return {v, myu:dot(v)}; }
function bal(l:string,r:string){ const L=side(l), R=side(r); let veq=true; for(let i2=0;i2<11;i2++) if(L.v[i2]!==R.v[i2]) veq=false;
  return {ok: veq && L.myu===R.myu, lhs:L.myu, rhs:R.myu, gap:Math.abs(L.myu-R.myu)}; }
function dimStr(d:number[]):string{ const nm=["M","L","T","Θ"]; if(d.every(x=>x===0)) return "dimensionless";
  return d.map((x,i)=>x===0?"":nm[i]+"^"+x).filter(s=>s!=="").join("·"); }

// ===== THE BATTERY (56 rows) — every row's got computed by the engine, expectations hand-written =====
// [The battery table as recorded in §3 above: T1 T2; S1–S6; R1–R6; P1–P14; N1; B1–B8; C1–C4; L1–L4; H1–H4; D1–D3; X1–X4.
//  Each row: {id, name, run:()=>got, expect}. The harness prints " PASS id | name | got | expect" or FAIL, and the summary line.
//  The full battery source is the run-2 execution preserved in this file's history; the frozen block in §3 is its verbatim output.]
```

## 7. Part-2 owed list (BEFORE the page freezes)

1. **The repo N1 zero-hit sweep** (session-100 line): biuret (ci), 103.08, C2H5N3O2 across ch01, ch02, ch31–ch35, ch36, fc1 — fetched via the saved-JSON pipeline, every fetch length checked against the directory listing; the reused-pin conversion if any hit.
2. **The [convergent] web battery:** Cornell's C:N 30:1 target and the 55–65 °C thermophilic band; the %C/%N band inputs (grass clippings, sawdust, autumn leaves); urea's biuret quality limit (the trade's spec class); glucose oxidation ΔH ≈ −2.87 MJ/mol; the slaking band −63.7..−65.2 (Ch 14's own); wood ash K2O-eq content band; the DAP 18-46-0 label class.
3. **Pin re-greps in owners' own pages** (raw `grep -o` counts, the Chapter Ledger, session-112 line): H2O Ch 4; NH3/N2/CO2/urea/(NH4)2SO4 Ch 20 (N2's owner Ch 10 inspected); K2CO3/K2O/CaCO3/CaO Ch 14; Ca(OH)2 Ch 24; CaMg(CO3)2/SiO2 Ch 30; MgSO4·7H2O Ch 4; the heat anchors 4.184 and 2256 Ch 7.
4. **The chapter prose** (six lectures L0–L5 per the checkpoint skeleton), Labs FC5.1–FC5.2, Exercises FC5.1–5.7 (FC5.6 ◆ withheld, prints no figures, due at the session-120 Revision Appendix; FC5.7 ◐ census), 8-row Safety (row 7 the fence absolute), canon coverage with the honesty line, forward/back flags, Chapter Ledger.
5. **The canvas + manuscript push byte-verified** to manuscript/field-companion/fc5.md; map FC5 planned → drafted; row 119 close; the FC5 web edition recorded as the standing web-sync debt.
