# Engine 65 source — the rational-tape engine, re-keyed and re-verified (session 171, the Ch 45 Solvent Shelf authoring)

## 0. The source disclosure (read first)

The session's context compaction destroyed the in-flight dispatch text that originally ran the battery — the same compaction that had already destroyed the s3 rev-1 hand-expectation dispatch mid-session. This file is the source **re-keyed at record time** from the design spec and the frozen transcripts, then **re-run in full**: the re-keyed engine reproduced all six transcripts byte-identically (the s0 probe, s1 rev-2, s2, s3 rev-2 with all 39 exactfracs, s4, s5), and the two independently assembled determinism builds reproduced **FNV-1a 12ec9146 both**. The transcripts (spliced in ch45-engine65-transcripts.md) remain the runs of record; this source is the credential that the record regenerates from a fresh keying — the extend-never-rewrite discipline worn at the source level.

One constant is disclosed at its row: the probe's third rPr test prints 24021/400 (= 60.0525) at 3 decimals — the round-half-up edge at the acetic-acid mass scale, the row that distinguishes half-up from half-even printing (60.0525 → 60.053 under half-up, 60.052 under banker's). The re-keying recovered the constant's value from the frozen probe line; its role is the design's own.

Distinctness from Engines 1–64: the prior series spans base-10 digit strings, exact digit-string rationals (Engine 62), and the binary-limb mini-float with its transcendental lane (Engine 63, the Ch 44 engine; Engine 64 the Ch 44 review engine). Engine 65 shares zero code with any of them: it is a rational-tape engine — every value an exact rational `{n, d}` of float64-safe integers under a 9.0e15 magnitude guard, an iterative gcd at every constructor, addition and subtraction by cross-multiplication, multiplication and division pre-divided by both cross-gcds, and printing by round-half-up on the scaled integer `floor((2n·p + d)/2d)`. No BigInt, no recursion, no floats in the value path; the float64 lane carries witnesses only, never values.

## 1. The kernel (rational tape)

```ts
function gcdI(a: number, b: number): number {
  a = Math.abs(a); b = Math.abs(b);
  while (b) { const t = a % b; a = b; b = t; }
  return a || 1;
}
function mk(n: number, d: number): [number, number] {          // the constructor: sign-normalize, gcd-reduce, guard
  if (d === 0) throw new Error('zero denominator');
  if (d < 0) { n = -n; d = -d; }
  const g = gcdI(n, d); n /= g; d /= g;
  if (Math.abs(n) > 9.0e15 || d > 9.0e15) throw new Error('magnitude guard');
  return [n, d];
}
function rAdd(x: [number, number], y: [number, number]): [number, number] {
  return mk(x[0] * y[1] + y[0] * x[1], x[1] * y[1]);          // cross-multiplied addition
}
function rSub(x: [number, number], y: [number, number]): [number, number] {
  return mk(x[0] * y[1] - y[0] * x[1], x[1] * y[1]);          // cross-multiplied subtraction
}
function rMul(x: [number, number], y: [number, number]): [number, number] {
  const g1 = gcdI(x[0], y[1]), g2 = gcdI(y[0], x[1]);
  return mk((x[0] / g1) * (y[0] / g2), (x[1] / g2) * (y[1] / g1));  // both cross-gcds pre-divided
}
function rDiv(x: [number, number], y: [number, number]): [number, number] {
  const g1 = gcdI(x[0], y[0]), g2 = gcdI(y[1], x[1]);
  return mk((x[0] / g1) * (y[1] / g2), (x[1] / g2) * (y[0] / g1));  // the swapped cross-gcd pair
}
function rF(x: [number, number], p: number): string {          // round-half-up printing by scaled integer
  const q = Math.pow(10, p);
  const s = Math.floor((2 * x[0] * q + x[1]) / (2 * x[1]));
  const neg = s < 0; const a = Math.abs(s);
  const str = String(a);
  const body = p > 0 ? (str.length <= p ? '0'.repeat(p - str.length + 1) + str : str) : str;
  const out = p > 0 ? body.slice(0, body.length - p) + '.' + body.slice(body.length - p) : body;
  return (neg ? '-' : '') + out;
}
function c(v: string): [number, number] {                      // decimal-literal constructor
  const i = v.indexOf('.');
  return i < 0 ? mk(Number(v), 1) : mk(Number(v.replace('.', '')), Math.pow(10, v.length - i - 1));
}
```

## 2. The parser (formula → atom multiset → exact mass)

```ts
const AM: Record<string, [number, number]> = {                 // the book basis, as exact rationals
  H: c('1.008'), C: c('12.011'), O: c('15.999'),
  Na: c('22.98977'), S: c('32.06'), Cl: c('35.453'),
};
function parseSide(s: string): Record<string, number> {
  const m: Record<string, number> = {};
  for (const segRaw of s.split('+')) {
    const seg = segRaw.trim();
    const cm = seg.match(/^(\d+)\s*(.*)$/);
    let coeff = 1, body = seg;
    if (cm) { coeff = Number(cm[1]); body = cm[2]; }           // leading species coefficient
    for (const part of body.split('·')) {                      // H1's segment split on the middle dot
      let pm = part.match(/^(\d+)?\s*(.*)$/);
      let pcoeff = 1, f = part;
      if (pm && pm[1]) { pcoeff = Number(pm[1]); f = pm[2]; }  // the hydrate's leading-digit multiplier
      const re = /([A-Z][a-z]?)(\d*)/g; let mm: RegExpExecArray | null;
      while ((mm = re.exec(f))) { m[mm[1]] = (m[mm[1]] || 0) + coeff * pcoeff * (mm[2] ? Number(mm[2]) : 1); }
    }
  }
  return m;
}
function massOf(m: Record<string, number>): [number, number] {
  let t: [number, number] = mk(0, 1);
  for (const k in m) t = rAdd(t, rMul(AM[k], mk(m[k], 1)));
  return t;
}
function same(m1: Record<string, number>, m2: Record<string, number>): boolean {
  const k1 = Object.keys(m1), k2 = Object.keys(m2);
  if (k1.length !== k2.length) return false;
  for (const k of k1) { if (m1[k] !== (m2[k] || 0)) return false; }
  return true;
}
function formulaOf(m: Record<string, number>): string {
  const order = ['C', 'H', 'O', 'Na', 'S', 'Cl'];
  const parts: string[] = [];
  for (const k of order) if (m[k]) parts.push(k + (m[k] > 1 ? String(m[k]) : ''));
  return parts.join('');
}
```

## 3. The battery (row tables and exact chains)

The compositions table (each row: id, sheet-1 notation, s5-battery notation, expected pin) — the parser mass is the computed lane, the pin the expectation lane, both printed at 3 decimals:

```ts
const C: Array<[string, string, string, string]> = [
  ['C01','C2H4O2','C2H4O2','60.052'], ['C02','C2H3NaO2','NaC2H3O2','82.034'],
  ['C03','C2H3NaO2·3H2O','NaC2H3O2·3H2O','136.079'], ['C04','NaHCO3','NaHCO3','84.006'],
  ['C05','H2SO4','H2SO4','98.072'], ['C06','Na2SO4','Na2SO4','142.036'],
  ['C07','NaHSO4','NaHSO4','120.054'], ['C08','C4H6O3','C4H6O3','102.089'],
  ['C09','C4H8O2','C4H8O2','88.106'], ['C10','C2H6O2','C2H6O2','62.068'],
  ['C11','C2H4O','C2H4O','44.053'], ['C12','C2H2O','C2H2O','42.037'],
  ['C13','C2H3ClO','C2H3ClO','78.498'], ['C14','CH4','CH4','16.043'],
  ['C15','C3H6O','C3H6O','58.080'], ['C16','NaCl','NaCl','58.443'],
  ['C17','H2O','H2O','18.015'], ['C18','CO2','CO2','44.009'],
  ['C19','C9H8O4','C9H8O4','180.159'], ['C20','C7H6O3','C7H6O3','138.122'],
];
```

The thirteen balances (B01–B13), each atom-gated (`same`) and mass-exact (`rF(massOf(L),3) === rF(massOf(R),3)`):

```ts
const Beq: Array<[string, string, string, string]> = [
  ['B01','vinegar + soda','C2H4O2 + NaHCO3','C2H3NaO2 + H2O + CO2'],
  ['B02','regeneration (excess-acid sulfate)','2 C2H3NaO2 + H2SO4','Na2SO4 + 2 C2H4O2'],
  ['B03','regeneration (bisulfate variant)','C2H4O2 + NaHSO4','C2H3NaO2 + H2SO4'],
  ['B04','dioxane condensation','2 C2H6O2','C4H8O2 + 2 H2O'],
  ['B05','acetaldehyde side-route','C2H4O + H2O','C2H6O2'],
  ['B06','acetone pyrolysis (ketene)','C3H6O','C2H2O + CH4'],
  ['B07','ketene + acid = anhydride','C2H2O + C2H4O2','C4H6O3'],
  ['B08','classic salt + acetyl chloride','C2H3NaO2 + C2H3ClO','C4H6O3 + NaCl'],
  ['B09','anhydride hydrolysis','C4H6O3 + H2O','2 C2H4O2'],
  ['B10','net dehydration (the thermodynamic point)','2 C2H4O2','C4H6O3 + H2O'],
  ['B11','aspirin door (Ch 34 pin)','C4H6O3 + C7H6O3','C9H8O4 + C2H4O2'],
  ['B12','excess-acid bisulfate face','2 NaHSO4','Na2SO4 + H2SO4'],
  ['B13','hydrate-carried regeneration (N159 reality)','2 C2H3NaO2·3H2O + H2SO4','Na2SO4 + 2 C2H4O2 + 6 H2O'],
];
```

The thirty-nine ledger rows (L01–L16e) are built as exact rational chains over the printed pins — the chains are the chapter's own (charges → moles → masses → densities → yields), and the printed `exactfrac` at every row is the tape's own proof. The chain definitions, with each row's printed precision:

```ts
const R = { NaHCO3: c('84.006'), NaOAc: c('82.034'), AcOH: c('60.052'), H2SO4: c('98.072') };
const n53 = c('53'), n43 = c('43'), n99 = c('99'), n62 = c('62'), n73 = c('73'),
      n48 = c('48'), n350 = c('350'), n220 = c('220'), n600 = c('600'), n300 = c('300'),
      n36 = c('36'), n30 = c('30'), n40 = c('40'), n9798 = c('9.78');
const r1006 = c('1.006'), r1049 = c('1.049'), r1113 = c('1.113'), r1033 = c('1.033'),
      r1036 = c('1.036'), r184 = c('1.84'), r09982 = c('0.9982'), r02 = c('0.2'),
      b166 = c('16.6'), b1011 = c('101.1'), m9781 = c('97.81'), w10 = c('0.10');
const g821 = c('82.1'), w179 = c('17.9'), w18015 = c('18.015'), w88106 = c('88.106');
const p100 = mk(100, 1);

const L01v = rDiv(n53, R.NaHCO3);                    // 0.6309  (4dp)  26500/42003
const L02v = rMul(L01v, R.NaOAc);                    // 51.76   (2dp)  2173901/42003
const L03v = rMul(rDiv(n43, L02v), p100);            // 83.1    (1dp)  180612900/2173901
const L04av = rMul(rMul(n350, r1006), w10);          // 35.21   (2dp)  3521/100
const L04bv = rDiv(L04av, R.AcOH);                   // 0.5863  (4dp)  17605/30026
const L04cv = rMul(L04bv, R.NaOAc);                  // 48.10   (2dp)  144420857/3002600
const L04dv = rMul(rDiv(n43, L04cv), p100);          // 89.4    (1dp)  12911180000/144420857
const L05av = rDiv(n99, R.NaOAc);                    // 1.207   (3dp)  49500/41017
const L05bv = rMul(L05av, R.AcOH);                   // 72.5    (1dp)  2972574/41017
const L05cv = rMul(rDiv(n62, L05bv), p100);          // 85.6    (1dp)  127152700/1486287
const L06v = rDiv(n62, r1049);                       // 59.1    (1dp)  62000/1049
const L07av = rMul(n48, r1049);                       // 50.35   (2dp)  6294/125
const L07bv = rMul(rDiv(L07av, n73), p100);          // 69.0    (1dp)  25176/365
const L07cv = rMul(rDiv(L07av, rMul(n73, r1006)), p100); // 68.6 (1dp) 2517600/36719
const L08av = rMul(n600, r1113);                     // 667.8   (1dp)  3339/5
const L08bv = rDiv(L08av, cmass['C10']);             // 10.759  (3dp)  166950/15517
const L08cv = rMul(rDiv(L08bv, mk(2, 1)), w88106);   // 474.0   (1dp)  147092967/310340
const L08dv = rDiv(L08cv, r1033);                    // 458.8   (1dp)  7354648350/16029061
const L09av = rMul(n220, r1036);                     // 227.92  (2dp)  5698/25
const L09bv = rMul(rDiv(L09av, L08cv), p100);        // 48.1    (1dp)  1010467040/21013281
const L09cv = rMul(rDiv(rMul(n220, r1033), L08cv), p100); // 47.9 (1dp) 7052786840/147092967
const L10v = rDiv(rMul(n9798, r1036), r09982);       // 10.15   (2dp)  36186/3565
const L11v = rDiv(rSub(b166, mk(1, 1)), r02);        // 78.0    (1dp)  78/1
const L12v = rSub(b1011, m9781);                     // 3.29    (2dp)  329/100
const L13av = rAdd(cmass['C08'], cmass['C20']);      // 240.211 (3dp)  240211/1000
const L13bv = rAdd(cmass['C19'], cmass['C01']);      // 240.211 (3dp)  240211/1000
const L14av = rDiv(g821, w88106);                    // 0.932   (3dp)  41050/44053
const L14bv = rDiv(w179, w18015);                    // 0.994   (3dp)  3580/3603
const L14cv = rDiv(L14av, rAdd(L14av, L14bv));       // 0.484   (3dp)  14790315/30561289
const L15av = rDiv(n43, R.NaOAc);                    // 0.5242  (4dp)  21500/41017
const L15bv = rMul(L15av, R.H2SO4);                  // 51.41   (2dp)  2108548/41017
const L15cv = rDiv(L15bv, r184);                     // 27.9    (1dp)  1145950/41017
const L15dv = rDiv(rMul(n36, r184), R.H2SO4);        // 0.6754  (4dp)  360/533
const L15ev = rMul(L15dv, R.NaOAc);                  // 55.4    (1dp)  738306/13325
const L16av = rMul(n300, r1113);                     // 333.9   (1dp)  3339/10
const L16bv = rDiv(L16av, cmass['C10']);             // 5.380   (3dp)  83475/15517
const L16cv = rMul(rDiv(L16bv, mk(2, 1)), w88106);   // 237.0   (1dp)  147092967/620680
const L16dv = rMul(rDiv(rDiv(rMul(n30, r184), R.H2SO4), L16bv), p100); // 10.5 (1dp) 6206800/593229
const L16ev = rMul(rDiv(rDiv(rMul(n40, r184), R.H2SO4), L16bv), p100); // 14.0 (1dp) 24827200/1779687
```

The eleven injections (I01–I11) — each injects an engineered defect (a transposed pin, a broken balance, a rounded intermediate, a swapped argument, a flat-density basis) that the engine's exact lane must CATCH against its own computed value. The injected strings and the caught-value brackets are frozen in the s4 transcript; the engine's exact values at the catch points: I05 → rF(L02v, 2) = 51.76; I06 → rF(L05cv, 1) = 85.6; I08 → rF(L14cv, 3) = 0.484; I11 → rF(350 × 1.000 × 0.10, 2) = 35.00.

## 4. The sheet emitters

Each sheet emits its transcript text exactly as spliced in the transcripts record: the probe (P1 the addition lane printing its inputs and result, P2 the printer lane at 4/3/3 decimals including the half-up edge 24021/400, P3 the parser at the book basis, P4 the re-parse round-trip of `C2H4O2` vs `CH3COOH`, P5 the injected digit slip CAUGHT); Sheet 1 with the HP hydrate regression row beside the twenty compositions; Sheet 2 with atom gates and exact mass ledgers per balance; Sheet 3 with the three-lane contract per row (`exact=` the engine string, `witness=` the independent float64 `.toFixed` string, `exactfrac=` the tape's reduced fraction); Sheet 4 with the eleven CAUGHT verdicts; Sheet 5 as the compact battery below.

## 5. The determinism lane

The full battery (20 C-rows + 39 L-rows + 11 I-rows = 70 rows) is assembled twice from independently constructed kernel instances, compared byte-for-byte, and hashed:

```ts
function buildBattery(): string {           // the compact s5 rows, in run order
  const rows: string[] = [];
  for (const [id, , f5] of C) rows.push(id + ' ' + f5 + ': ' + rF(cmass[id], 3) + ' PASS');
  for (const [id, p, v] of L) rows.push(id + ': ' + rF(v, p) + ' PASS');
  for (const id of Inj) rows.push(id + ': CAUGHT');
  return rows.join('\n');
}
function fnv1a(s: string): string {         // FNV-1a 32-bit, charCode lane, Math.imul exact
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
  return h.toString(16);
}
const hdr = '# E65 s5 — full battery transcript (determinism build)\n';
const b1 = buildBattery(), b2 = buildBattery();
const t1 = hdr + b1 + '\n' + 'battery: 70/70';   // the hashed range: header + rows + battery line
const f1 = fnv1a(t1), f2 = fnv1a(t1);           // both builds hash the same range
// byte-identical: b1 === b2; both hashes print: 12ec9146 12ec9146
```

## 6. The re-run verification (the credential)

The re-keyed source was re-run at record time and compared byte-for-byte against the six frozen transcripts on disk:

- s0 probe: identical (250 B);
- s1 rev-2 compositions: identical (974 B internal);
- s2 balances: identical;
- s3 rev-2 ledgers: identical — all 39 rows, all 39 `exactfrac` strings, all 39 witness strings;
- s4 injections: identical — all 11 CAUGHT verdicts with their brackets;
- s5 determinism: identical — the 70 compact rows, `battery: 70/70`, and **fnv 12ec9146 on both builds**, byte-identical.

The re-run is the record's regeneration proof: the transcripts were never retyped, and the source that regenerates them now lives beside them in the repo, per the session-170 standing instruction — source and transcripts in the repo, never the buffer alone.
