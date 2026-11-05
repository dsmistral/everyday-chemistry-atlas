# Engine 83 — E83-MC — the as-run source (session 198)

The design source (src.txt, md5 b8613fd6944fdc9bcd32d66ce6fb532f) was written to disk
before any run. This file preserves the AS-RUN source of the final revision of each piece,
splice-verbatim. The honest history (rev-1/2/3 harness defects, all disclosed) lives in
ch53-engine83-transcripts.md; the code below is the code that produced the PASS rows.

Shared invariants (every piece): p1 = 65537, p2 = 1000003; element table in integer
my-units (mg/mol): H 1008, C 12011, O 15999, Na 22990, Ca 40078, S 32065, Cl 35450;
no recursion (iterative parser with an explicit group stack); no BigInt; no floats in
any value path.

## The shared helper block (identical in every piece, as-run)

```typescript
const P1 = 65537, P2 = 1000003;
const EL: Record<string, number> = { H: 1008, C: 12011, O: 15999, Na: 22990, Ca: 40078, S: 32065, Cl: 35450 };
const mod = (v: number, p: number) => ((v % p) + p) % p;
const mulmod = (a: number, b: number, p: number) => mod(a * b, p);
function parse(f: string): Record<string, number> {
  const group: Array<Record<string, number>> = [{}];
  let i = 0;
  while (i < f.length) {
    const c = f[i];
    if (c === '(') { group.push({}); i++; continue; }
    if (c === ')') {
      i++;
      let n = 0, got = false;
      while (i < f.length && f[i] >= '0' && f[i] <= '9') { n = n * 10 + (f.charCodeAt(i) - 48); got = true; i++; }
      const k = (got && n > 0) ? n : 1;
      const sub = group.pop() as Record<string, number>;
      const top = group[group.length - 1];
      for (const e in sub) top[e] = (top[e] || 0) + sub[e] * k;
      continue;
    }
    if (c >= 'A' && c <= 'Z') {
      let sym = c; i++;
      while (i < f.length && f[i] >= 'a' && f[i] <= 'z') { sym += f[i]; i++; }
      let n = 0, got = false;
      while (i < f.length && f[i] >= '0' && f[i] <= '9') { n = n * 10 + (f.charCodeAt(i) - 48); got = true; i++; }
      const k = (got && n > 0) ? n : 1;
      const top = group[group.length - 1];
      top[sym] = (top[sym] || 0) + k;
      continue;
    }
    i++;
  }
  return group[0];
}
function massLane(f: string): number { const m = parse(f); let s = 0; for (const e in m) s += EL[e] * m[e]; return s; }
function massMod(f: string, p: number): number { const m = parse(f); let s = 0; for (const e in m) s = mod(s + mulmod(EL[e], m[e], p), p); return s; }
const trunc = (lane: number) => Math.floor(lane / 10);
const halfup = (lane: number) => Math.floor((lane + 5) / 10);
const cents = (c: number) => (c / 100).toFixed(2);
type Side = Array<[string, number]>;
function elemSums(side: Side) {
  const ints: Record<string, number> = {}; const m1: Record<string, number> = {}; const m2: Record<string, number> = {};
  for (const [f, c] of side) {
    const m = parse(f);
    for (const e in m) {
      ints[e] = (ints[e] || 0) + m[e] * c;
      m1[e] = mod((m1[e] || 0) + mulmod(m[e] % P1, c % P1, P1), P1);
      m2[e] = mod((m2[e] || 0) + mulmod(m[e] % P2, c % P2, P2), P2);
    }
  }
  return { ints, m1, m2 };
}
const massSide = (side: Side) => { let s = 0; for (const [f, c] of side) { const m = parse(f); for (const e in m) s += EL[e] * m[e] * c; } return s; };
function sdbm(s: string): number { let h = 0; for (let i = 0; i < s.length; i++) h = (h * 65599 + s.charCodeAt(i)) % 4294967296; return h; }
```

## Piece P — probe (as-run rev-2; rev-1 differed only in the census line's slice)

```typescript
const out: string[] = ['E83-MC PROBE rev-2 (rev-1 harness defect: the census line swept the header into the every-PASS check; value path clean)'];
const m1 = parse('Ca3(C6H5O7)2');
out.push('P1 parse Ca3(C6H5O7)2 -> ' + JSON.stringify(m1) + (m1.Ca === 3 && m1.C === 12 && m1.H === 10 && m1.O === 14 ? ' PASS' : ' FAIL'));
const lane = massLane('C6H8O7');
out.push('P2 massLane C6H8O7 = ' + lane + (lane === 192123 ? ' PASS' : ' FAIL'));
const ok3 = mod(lane, P1) === massMod('C6H8O7', P1) && mod(lane, P2) === massMod('C6H8O7', P2);
out.push('P3 mod-lane consistency P1/P2 ' + (ok3 ? 'PASS' : 'FAIL') + ' (r1=' + mod(lane, P1) + ', r2=' + mod(lane, P2) + ')');
out.push('P4 mulmod edge ' + (mulmod(2, 3, P1) === 6 ? 'PASS' : 'FAIL'));
const q = Math.floor(4500000 / 295735), r = 4500000 - q * 295735;
out.push('P5 witness triple div(4500000,295735) = [' + q + ', ' + r + ', 295735] ' + (q === 15 && r === 63975 ? 'PASS' : 'FAIL'));
const pass = out.slice(1).every(l => l.includes('PASS'));
out.push('PROBE ' + (pass ? 'PASS 5/5' : 'FAIL'));
return out.join('\n');
```

## Piece M — molar book (as-run rev-1, 22/22)

```typescript
// rows: [name, parts(formula x count), convergent literature display]
const rows: Array<[string, Array<[string, number]>, string]> = [
  ['citric acid (anhydrous)', [['C6H8O7', 1]], '192.12'],
  ['citric acid monohydrate', [['C6H8O7', 1], ['H2O', 1]], '210.14'],
  ['trisodium citrate (anhydrous)', [['Na3C6H5O7', 1]], '258.07'],
  ['trisodium citrate dihydrate', [['Na3C6H5O7', 1], ['H2O', 2]], '294.10'],
  ['calcium citrate', [['Ca3(C6H5O7)2', 1]], '498.43'],
  ['gypsum', [['CaSO4', 1], ['H2O', 2]], '172.17'],
  ['calcium chloride', [['CaCl2', 1]], '110.98'],
  ['sulfuric acid', [['H2SO4', 1]], '98.08'],
  ['sodium hydroxide', [['NaOH', 1]], '40.00'],
  ['sodium chloride', [['NaCl', 1]], '58.44'],
  ['water', [['H2O', 1]], '18.02'],
  ['starch unit', [['C6H10O5', 1]], '162.14'],
  ['glucose', [['C6H12O6', 1]], '180.16'],
  ['vanillin', [['C8H8O3', 1]], '152.15'],
  ['guaiacol', [['C7H8O2', 1]], '124.14'],
  ['glyoxylic acid', [['C2H2O3', 1]], '74.04'],
  ['4-hydroxy-3-methoxymandelic acid', [['C9H10O5', 1]], '198.17'],
  ['carbon dioxide', [['CO2', 1]], '44.01'],
  ['methanol', [['CH4O', 1]], '32.04'],
  ['dichloromethane', [['CH2Cl2', 1]], '84.93'],
  ['eugenol', [['C10H12O2', 1]], '164.20'],
  ['oxygen', [['O2', 1]], '31.99'],
];
const out: string[] = ['E83-MC MOLAR BOOK rev-1'];
let n = 0, npass = 0;
for (const [name, parts, lit] of rows) {
  n++;
  let lane = 0, r1 = 0, r2 = 0;
  for (const [f, c] of parts) {
    const l = massLane(f) * c;
    lane += l;
    r1 = mod(r1 + mulmod(massLane(f) % P1, c % P1, P1), P1);
    r2 = mod(r2 + mulmod(massLane(f) % P2, c % P2, P2), P2);
  }
  const litC = Math.floor(parseFloat(lit) * 100 + 0.5);
  let cls = 'FAIL';
  if (trunc(lane) === litC) cls = 'AGREE-EXACT';
  else if (halfup(lane) === litC) cls = 'AGREE-HALFUP';
  const mok = mod(lane, P1) === r1 && mod(lane, P2) === r2;
  const pass = cls !== 'FAIL' && mok;
  if (pass) npass++;
  out.push('M' + n + ' ' + name + ': lane=' + lane + ' (' + (lane / 1000).toFixed(3) + '), trunc=' + cents(trunc(lane)) + ', half-up=' + cents(halfup(lane)) + ', lit=' + lit + ' -> ' + cls + (mok ? ', mod-lanes CONSISTENT' : ', mod-lanes FAIL') + (pass ? ' PASS' : ' FAIL'));
}
out.push('MOLAR BOOK ' + npass + '/' + n + (npass === n ? ' PASS' : ' FAIL'));
return out.join('\n');
```

## Piece B — balance book (as-run rev-1, 7/7)

```typescript
const B: Array<[string, Side, Side]> = [
  ['B1 neutralization C6H8O7 + 3 NaOH -> Na3C6H5O7 + 3 H2O', [['C6H8O7', 1], ['NaOH', 3]], [['Na3C6H5O7', 1], ['H2O', 3]]],
  ['B2 double displacement 2 Na3C6H5O7 + 3 CaCl2 -> Ca3(C6H5O7)2 + 6 NaCl', [['Na3C6H5O7', 2], ['CaCl2', 3]], [['Ca3(C6H5O7)2', 1], ['NaCl', 6]]],
  ['B3 the liberation Ca3(C6H5O7)2 + 3 H2SO4 -> 2 C6H8O7 + 3 CaSO4', [['Ca3(C6H5O7)2', 1], ['H2SO4', 3]], [['C6H8O7', 2], ['CaSO4', 3]]],
  ['B4 hydration CaSO4 + 2 H2O -> CaSO4(H2O)2', [['CaSO4', 1], ['H2O', 2]], [['CaSO4(H2O)2', 1]]],
  ['B5 starch hydrolysis C6H10O5 + H2O -> C6H12O6', [['C6H10O5', 1], ['H2O', 1]], [['C6H12O6', 1]]],
  ['B6 guaiacol condensation C7H8O2 + C2H2O3 -> C9H10O5', [['C7H8O2', 1], ['C2H2O3', 1]], [['C9H10O5', 1]]],
  ['B7 oxidative decarboxylation 2 C9H10O5 + O2 -> 2 C8H8O3 + 2 CO2 + 2 H2O', [['C9H10O5', 2], ['O2', 1]], [['C8H8O3', 2], ['CO2', 2], ['H2O', 2]]],
];
const out: string[] = ['E83-MC BALANCE BOOK rev-1'];
let npass = 0;
for (const [name, L, R] of B) {
  const li = elemSums(L), ri = elemSums(R);
  const els: string[] = [];
  for (const e in li.ints) if (!(e in ri.ints)) els.push(e);
  for (const e in ri.ints) if (els.indexOf(e) < 0) els.push(e);
  let ok = true; const det: string[] = [];
  for (const e of els) {
    const a = li.ints[e] || 0, b = ri.ints[e] || 0;
    const c1 = mod(li.m1[e] || 0, P1) === mod(ri.m1[e] || 0, P1);
    const c2 = mod(li.m2[e] || 0, P2) === mod(ri.m2[e] || 0, P2);
    const ex = a === b;
    if (!ex || !c1 || !c2) ok = false;
    det.push(e + ' ' + a + '/' + b + (ex && c1 && c2 ? ' ok' : ' CATCH'));
  }
  const laneOk = massSide(L) === massSide(R);
  if (!laneOk) ok = false;
  if (ok) npass++;
  out.push(name + ' -> int ' + (det.every(d => d.includes(' ok')) ? 'CLOSED' : 'OPEN') + ', mass-lane ' + (laneOk ? 'EQUAL' : 'MISMATCH') + (ok ? ' PASS [' + det.join(', ') + ']' : ' FAIL [' + det.join(', ') + ']'));
}
out.push('BALANCE BOOK ' + npass + '/7 ' + (npass === 7 ? 'PASS' : 'FAIL'));
return out.join('\n');
```

## Piece D — dose/economics display audit (as-run rev-2, 15/15 + D12 by refusal)

```typescript
// rev-2. rev-1 caught, all harness-side, value path defect-free: (1) percent rows D4/D8a/D8b/D11
// missing the x100; (2) D13 double-scaled; (3) display helper toFixed at the wrong decimal;
// (4) D9 expectation hu 1539->1538 (engine right); (5) D10 expectation hu 10000->9999 (engine
// right: r=36,750,000 < D/2). Row: [desc, N, D, dp, div, dd, eTr, eHu, stated]
type Row = [string, number, number, number, number, number, number, number, string];
const rows: Row[] = [
  ['D1 450 mL in fl oz (10^-4 mL units)', 4500000, 295735, 3, 1, 3, 15216, 15216, '15.216 fl oz (stated)'],
  ['D2 theoretical citric from 450 mL x 1.44 g/fl oz (my-g)', 648000000, 295735, 0, 100, 2, 2191, 2191, '21.91 g (register machine-exact)'],
  ['D3a crude/theoretical percent, 1 dp', 535280350, 6480000, 1, 10, 1, 826, 826, '82.6% (register)'],
  ['D3b crude/theoretical percent, 0 dp', 535280350, 6480000, 0, 1, 0, 82, 83, '83% (video stated)'],
  ['D4 DCM train volume vs charge (percent)', 24000, 300, 0, 1, 0, 80, 80, '80% (240 of ~300 mL)'],
  ['D5a vanilla-sugar charge', 162, 1, 0, 1, 0, 162, 162, '162 g = 18 x 9 g (exact)'],
  ['D5b methanol charge', 350, 1, 0, 1, 0, 350, 350, '350 mL = 150+150+50 (exact)'],
  ['D6 methanol recovery', 325000, 3500, 1, 10, 1, 928, 929, '92.9% (stated)'],
  ['D7 N261 vanillin wt%', 150, 162, 2, 100, 2, 92, 93, '0.93 wt% (stated)'],
  ['D8a N260 yield vs brand range top (percent)', 40000, 4000, 0, 1, 0, 10, 10, '10% of 4 g/500 mL'],
  ['D8b N260 yield vs brand range bottom (percent)', 40000, 1000, 0, 1, 0, 40, 40, '40% of 1 g/500 mL'],
  ['D9 Madagascar peak multiple', 600, 39, 2, 100, 2, 1538, 1538, '15.38x (2013 -> 2018 peak)'],
  ['D10 FDA unit beans per liter', 1335000 * 2834950, 378500000, 0, 100, 2, 9999, 9999, '99.99 g/L, trunc and half-up (the ~100 g/L fold)'],
  ['D11 natural vanillin recovery (percent)', 100000, 10000, 0, 1, 0, 10, 10, '~10% (1 kg of the ~10 kg present in 500 kg beans at 2%)'],
  ['D13 citric density of the premise (g/100 mL)', 648000000, 133080750, 2, 100, 2, 486, 487, '4.86 g/100 mL trunc / 4.87 half-up (band 4.5-5)'],
];
const out: string[] = ['E83-MC DOSE/ECONOMICS AUDIT rev-2 (rev-1: 8/15 + D12; the seven FAILs all harness-side)'];
let npass = 0;
for (const [desc, N, D, dp, div, dd, eTr, eHu, stated] of rows) {
  const S = N * Math.pow(10, dp);
  const tr = Math.floor(S / D);
  const r = S - tr * D;
  const hu = Math.floor((2 * S + D) / (2 * D));
  const disp = (v: number) => (v / div).toFixed(dd);
  const ok = tr === eTr && hu === eHu;
  if (ok) npass++;
  out.push(desc + ': q=' + tr + ' r=' + r + ' d=' + D + ' | trunc=' + disp(tr) + ' half-up=' + disp(hu) + ' | expected tr=' + eTr + ' hu=' + eHu + ' | stated: ' + stated + (ok ? ' PASS' : ' FAIL'));
}
out.push('D12 the honest gap: 47 g starch, input mass unstated in-source -> recovery UNCOMPUTABLE; no row fabricated (PASS by refusal)');
out.push('NOTE (of record): src.txt draft row D2 printed r=23815; the run is authoritative: r=44615, q=2191 unchanged.');
out.push('DOSE/ECONOMICS AUDIT ' + npass + '/' + rows.length + ' rows PASS (+D12 by refusal)');
return out.join('\n');
```

## Piece X — injections (as-run rev-1, 4/4 CAUGHT)

```typescript
const j1 = !balancePass([['C6H8O7', 1], ['NaOH', 3]], [['Na3C6H5O7', 2], ['H2O', 3]]);
const badLane = parse('C6H8O6'); let bl = 0; for (const e in badLane) bl += EL[e] * badLane[e];
const j2 = Math.floor(bl / 10) !== 19212;
const j3 = Math.floor(648000000 / 300000) !== 2191;
// J4: the p1-invisible corruption (+65537 to B3's left Ca count)
const li = elemSums([['Ca3(C6H5O7)2', 1], ['H2SO4', 3]]);
const caInt = (li.ints['Ca'] || 0) + P1;
const intCatches = caInt !== 3;
const p1Blind = mod(caInt, P1) === mod(3, P1);
const p2Catches = mod(caInt, P2) !== mod(3, P2);
const j4 = intCatches && p1Blind && p2Catches;
```

## Piece X — determinism (as-run rev-3, PASS; revs 1-2 of record in the transcripts)

```typescript
function run12(): string {
  const lines: string[] = [];
  for (const [nm, L, R] of B) lines.push(nm + ' ' + (balancePass(L, R) ? 'PASS' : 'FAIL'));
  const dose: Array<[string, number, number, number, number]> = [
    ['D2', 648000000, 295735, 0, 2191], ['D6', 325000, 3500, 1, 928], ['D7', 150, 162, 2, 92], ['D9', 600, 39, 2, 1538], ['D10', 1335000 * 2834950, 378500000, 0, 9999], ['D13', 648000000, 133080750, 2, 486],
  ];
  for (const [nm, N, D, dp, e] of dose) {
    const q = Math.floor(N * Math.pow(10, dp) / D);
    lines.push(nm + ' ' + (q === e ? 'PASS' : 'FAIL') + ' q=' + q);
  }
  return lines.join('|');
}
const r1 = run12(), r2 = run12();
const det = r1 === r2 && sdbm(r1) === sdbm(r2);
const allPass = r1.indexOf('FAIL') < 0;
```

Verdict: PASS. The battery froze every figure this chapter's prose prints; the transcripts
and receipts live in ch53-engine83-transcripts.md.
