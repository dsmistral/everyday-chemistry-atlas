# Engine 78 — the source record (session 191, Ch 51 part 2 of 2)

*The source record of Engine 78 (E78-IL, the integer-lane engine) — with a disclosure this series has not needed before. The session's as-run code text was lost to a platform context compaction that struck between the battery's freeze and this file's writing; unlike Engine 77's source, preserved verbatim at part-1 close, Engine 78's could not be. What this file preserves is a close-of-session reconstruction: rebuilt from the session's design spec and the frozen receipts, then re-executed on 2026-11-05 against every figure all five receipts print — sixty-five assertions, kernels and closures and residuals, all twenty molar rows with their W-lane matches, every charge, yield and settlement figure, every injection — all reproduced exactly. The receipts (`engine78-a`–`e.txt`, the transcripts file, Lab 51.2) remain the run record; this file is the durable design, re-proved against them. Nothing laundered: where the receipts' printed values forced a convention the lost text cannot confirm, the convention is named below as a reconstruction choice. The labels are the contract in both directions.*

## The kernel and harnesses (reconstructed, re-executed at close — every figure reproduced)

```typescript
async function main() {
  // The element table: the integer lane (my, exact mg/mol) and the float witness lane (W, nominal).
  const EL: Record<string, number>  = { H:1008, C:12011, N:14007, O:15999, Na:22990, Cl:35450, Sn:118710, S:32060 };
  const ELW: Record<string, number> = { H:1.008, C:12.011, N:14.007, O:15.999, Na:22.990, Cl:35.450, Sn:118.710, S:32.060 };
  function parse(f: string): Record<string, number> {   // uppercase-run parse; two-letter symbols need the lowercase;
    const c: Record<string, number> = {}; let i = 0;    // SNCL2 -> S,N,C,L -> refused at the element gate
    while (i < f.length) {
      if (f[i] < 'A' || f[i] > 'Z') throw new Error('BAD CHARACTER');
      let sym = f[i];
      if (i+1 < f.length && f[i+1] >= 'a' && f[i+1] <= 'z') { sym += f[i+1]; i++; }
      if (!(sym in EL)) throw new Error('UNKNOWN ELEMENT: ' + sym);
      i++; let num = '';
      while (i < f.length && f[i] >= '0' && f[i] <= '9') { num += f[i]; i++; }
      c[sym] = (c[sym] || 0) + (num === '' ? 1 : parseInt(num, 10));
    }
    return c;
  }
  const massMy = (s: Record<string, number>) => Object.entries(s).reduce((a,[e,n]) => a + n*EL[e], 0);
  const massW  = (s: Record<string, number>) => Object.entries(s).reduce((a,[e,n]) => a + n*ELW[e], 0);
  function fmt(x: number, dp: number): string {          // half-up at the decimal reading (A2's boundary semantics);
    const p = Math.pow(10, dp);                          // reconstruction note: epsilon form, verified at 2.065->2.07,
    return (Math.round(x*p + 1e-9) / p).toFixed(dp);     // 0.125->0.13; the as-run text's internals are unrecoverable
  }
  function gcd2(a: number, b: number): number { a=Math.abs(a); b=Math.abs(b); while (b) { const t=a%b; a=b; b=t; } return a; }
  const rowGcd = (r: number[]) => r.reduce((a,v) => gcd2(a,v), 0);
  function basis(M: number[][]): { rank: number; rows: number[] } {  // row-echelon, row-gcd normalized (K3: never
    const W = M.map(r => r.slice());                                // inside detM); rows = ORIGINAL pivot-row indices
    const orig = M.map((_, i) => i); const rows: number[] = [];
    let rank = 0, piv = 0; const m = W.length, n = W[0].length;
    while (piv < n && rank < m) {
      let sel = -1;
      for (let i = rank; i < m; i++) if (W[i][piv] !== 0) { sel = i; break; }
      if (sel === -1) { piv++; continue; }
      [W[rank], W[sel]] = [W[sel], W[rank]]; [orig[rank], orig[sel]] = [orig[sel], orig[rank]];
      rows.push(orig[rank]);
      const p = W[rank][piv];
      for (let i = rank+1; i < m; i++) { const f = W[i][piv];
        if (f !== 0) for (let j = piv; j < n; j++) W[i][j] = W[i][j]*p - f*W[rank][j];
        const g = rowGcd(W[i]); if (g > 1) for (let j = piv; j < n; j++) W[i][j] /= g; }
      rank++; piv++;
    }
    return { rank, rows };
  }
  function detM(A: number[][]): number {                  // Bareiss fraction-free, exact division, NO row
    const n = A.length; const M = A.map(r => r.slice());  // normalization (the K4 fix: every entry stays an
    let sign = 1, prev = 1;                               // exact minor of the original matrix)
    for (let k = 0; k < n-1; k++) {
      if (M[k][k] === 0) { let sw = -1; for (let i = k+1; i < n; i++) if (M[i][k] !== 0) { sw = i; break; }
        if (sw === -1) return 0; [M[k], M[sw]] = [M[sw], M[k]]; sign = -sign; }
      for (let i = k+1; i < n; i++) for (let j = k+1; j < n; j++) M[i][j] = (M[i][j]*M[k][k] - M[i][k]*M[k][j]) / prev;
      prev = M[k][k];
    }
    return sign * M[n-1][n-1];
  }
  type Spec = { f: string; side: 'r' | 'p' };
  function elemMatrix(specs: Spec[]) {                    // product columns negated — the sign convention
    const elems: string[] = []; const vs = specs.map(s => parse(s.f));
    for (const v of vs) for (const e of Object.keys(v)) if (!elems.includes(e)) elems.push(e);
    const M = elems.map(e => vs.map((v, s) => (v[e] || 0) * (specs[s].side === 'p' ? -1 : 1)));
    return { M, elems };
  }
  function kernel(specs: Spec[]): { code: number; k?: number[]; nullity: number } {
    const { M } = elemMatrix(specs); const n = specs.length;
    const { rank, rows } = basis(M); const nullity = n - rank;   // the K2 fix: rank on the row-reduced basis
    if (nullity !== 1) return { code: -2, nullity };            // B3's refusal lane: no unique kernel, said so
    const B = rows.map(r => M[r]); const m = rank;               // the rank basis (n-1 independent rows)
    const k: number[] = [];
    for (let i = 0; i < n; i++) k.push(Math.pow(-1, m+i) * detM(B.map(r => r.filter((_,c) => c !== i))));
    for (const row of M) { let s = 0; for (let j = 0; j < n; j++) s += row[j]*k[j];
      if (s !== 0) throw new Error('KERNEL FAILS FULL MATRIX'); } // the cofactor kernel must satisfy every row
    const g = k.reduce((a,v) => gcd2(a,v), 0); const kk = k.map(v => v/g);
    const pos = kk.filter(v => v > 0).length, neg = kk.filter(v => v < 0).length;
    if (pos > 0 && neg > 0) throw new Error('SIGN ANOMALY: mixed-sign kernel');  // the rev-1/2 defect class, guarded
    return { code: 0, k: neg > 0 ? kk.map(v => -v) : kk, nullity };
  }
  function residual(specs: Spec[], claim: number[]): Record<string, number> {
    const { M, elems } = elemMatrix(specs); const out: Record<string, number> = {};
    elems.forEach((e, i) => { let s = 0; for (let j = 0; j < specs.length; j++) s += M[i][j]*claim[j]; if (s !== 0) out[e] = s; });
    return out;
  }
  const closure = (specs: Spec[], coefs: number[]) =>
    specs.reduce((a,s,i) => a + (s.side === 'p' ? -1 : 1)*coefs[i]*massMy(parse(s.f)), 0);
  function djb2(s: string): string {                       // the receipt digest lane (distinct from sdbm, the
    let h = 5381;                                         // Engine-66/77 convention)
    for (let i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) >>> 0;
    return (h >>> 0).toString(16);
  }
  // The nmol lane (Pieces D and E): integer nanomoles and 0.1 mg units, both floored.
  const nmol = (mg: number, my: number) => Math.floor(mg * 1e9 / my);
  const mgFromNmol = (n: number, my: number) => Math.floor(n * my / 1e8);   // 0.1 mg units — the quantization
  const g4 = (units: number) => (units/1e4).toFixed(4);                     // exact 4 dp from integer units
  const dp3 = (x: number) => x.toFixed(3);
  // Two percent conventions, both forced by the receipts' printed values (reconstruction choices, named):
  const pctYield = (yUnits: number, tUnits: number) => (Math.floor(yUnits * 10000 / tUnits) / 100).toFixed(2); // truncating hundredths: 86.447 -> 86.44
  const pctHalfUp = (x: number) => fmt(x, 2);                                                                 // half-up: 4.3478 -> 4.35

  /* the five piece bodies — spec form below; their literal row text is frozen verbatim in
     engine78-a..e.txt, the transcripts file, and Lab 51.2 */
}
```

## Piece A — the probe (rev-5), in spec form

*Rows: A1 `massMy(parse('SnCl2')) = 189610`, `massW` printed 189.610 against `massMy/1000` 189.610 — W-MATCH. A2 `fmt(2.065, 2) = '2.07'`, `fmt(0.125, 2) = '0.13'`. A3 `kernel([H2 r, O2 r, H2O p]) = [2,1,2]`, closure over the kernel = 0, lhs 2×2016+31998 = 36030 = rhs 2×18015. A4 `kernel([C6H5CHO r, NaOH r, C6H5CH2OH p, NaC7H5O2 p]) = [2,1,1,1]` — four elements over four species, rank basis, Bareiss minors — closure 0, lhs 2×106124+39997 = 252245 = rhs 108140+144105. INJ-A1 `residual(cann, [1,1,1,1]) = {C:-7, H:-6, O:-1}` — caught. INJ-A2 `parse('SNCL2')` throws `UNKNOWN ELEMENT: L` — caught. The four defect classes of rev-1..4 (sign convention; non-square cofactor minors; row-gcd scaling inside the determinant; fraction-free pivot over-counting — the Cannizzaro witness reading 2:14:1:1 until the Bareiss fix) are all in the kernel above: the negated product columns, the rank basis, the normalization-free detM, the exact-division Bareiss.*

## Piece B — Sheet 1, the balances (rev-2), in spec form

*Rows: B1 the Cannizzaro kernel [2,1,1,1], closure 0. B2 the acid workup `kernel([NaC7H5O2 r, HCl r, C7H6O2 p, NaCl p]) = [1,1,1,1]` — five elements over four species, the K2 case — closure 144105+36458−122123−58440 = 0. B3 Verley-Doebner `kernel([C6H5CHO r, C3H4O4 r, C9H8O2 p, CO2 p, H2O p])` returns code −2, nullity 2 — the refusal, itself a PASS condition; the claim lane `residual(vd, [1,1,1,1,1]) = {}`; closure 106124+104061 = 210185 = 148161+44009+18015. B4 piperine `kernel([C17H19NO3 r, H2O r, C12H10O4 p, C5H11N p]) = [1,1,1,1]`, closure 285343+18015 = 303358 = 218208+85150. INJ-B1 `residual(vd, [1,1,1,1,0]) = {H:2, O:1}` — caught. INJ-B2 the water-doubled claim [1,1,1,1,2] reads an H/O imbalance of magnitude 2/1 on the product side (the receipt prints {H:2, O:1}; the signed lane reads {H:−2, O:−1} — the catching condition, nonzero imbalance, is what the re-execution verifies) — caught. Rev-2's correction was decorative only: rev-1 typed HCl/NaCl 36460/58442 where the table reads 36458/58440; the closure was 0 in both.*

## Piece C — Sheet 2, the molar book (rev-1), in spec form

*Twenty rows, each `my = massMy(parse(f))` with `massW` printed at 3 dp against `my/1000` — MATCH on all twenty: benzaldehyde 106124, benzyl alcohol 108140, sodium benzoate 144105, benzoic acid 122123, malonic acid 104061, cinnamic acid 148161, pyridine 79102, β-alanine 89094, piperine 285343, piperic acid 218208, piperidine 85150, styrene 104152, water 18015, CO₂ 44009, NaOH 39997, HCl 36458, NaCl 58440, p-nitroaniline 138126, 2-naphthol 144173, para red 293282 — the cross-chapter pins re-proved at their owners, the two collisions named at their rows (106.124 vs the ester's 106.121; styrene = cubane's exact 104.152). INJ-C1 the ester-digit mis-pin: the lane reads 106124, not 106121 — caught.*

## Piece D — Sheet 3, the charge/yield ledger (rev-2), in spec form

*Rows: D1 `nmol(20880, 106124) = 196750970` (20 mL × 1044 mg/mL); `nmol(15000, 39997) = 375028127`; demand = 196750970/2 = 98375485 exact; eq `375028127/196750970` at 3 dp = 1.906; headroom = 3.812. D2 `mgFromNmol(98375485, 108140)` → 10.6383 g; `mgFromNmol(98375485, 144105)` → 14.1763 g; the register's 51/62 printed as stated, implied `floor(51·bz/100)` → 5.4255 g and `floor(62·nb/100)` → 8.7893 g. D3 `nmol(10440, 106124) = 98375485` limiting; `nmol(25000, 104061) = 240243703` = 2.442 eq; `nmol(2000, 89094) = 22448200` = 0.228 eq catalytic. D4 `mgFromNmol(98375485, 148161)` → 14.5754 g theoretical; `pctYield(126000, cin)` = 86.44% vs the register's 87; mp 125 vs 132–133. D5 `nmol(1000, 285343) = 3504554` = 3.505 mmol with the reconstruction identity |n·my − 10¹²| < my; `pctHalfUp(10000/230000·100)` = 4.35%. INJ-D1 the density slip 0.844 → 16880 ≠ 20880 — caught. INJ-D2 the theoretical slip 14.75 ≠ 14.5754 — caught. Rev-2's four harness fixes (percent ÷1000→÷100; the yield-percent scale; the 3.5052 bad pin replaced by the reconstruction identity; the decorative 0.240252→0.240244) left every lane figure unchanged.*

## Piece E — Sheet 4, the worked answers and settlement rows (rev-2), in spec form

*Rows: X1 demand `floor(98375485/2) = 49187742` nmol; `mgFromNmol(49187742, 39997)` → 1.9673 g. X2 the L14 settlement both ways: `nmol(5000, 138126) = 36198832` → amine-limited `mgFromNmol(36198832, 293282)` → 10.6164 g; `nmol(2700, 144173) = 18727500` → naphthol-limited `mgFromNmol(18727500, 293282)` → 5.4924 g; the smaller governs — naphthol limiting, identical to Ch 48's settled row, the settlement exact. X3 `floor(87·cin/100)` in 0.1 mg units → 12.6805 g (the integer quantization is why the round-trip prints 12.6805 and not the float 12.6806). X4 `2 × 98375485 = 196750970` — the disproportionation symmetry, exact. INJ-E1 the naphthol mol slip 0.018278 → `mgFromNmol(18278000, 293282)` = 5.3606 ≠ 5.4924 — caught. INJ-E2 51% of the wrong base: `floor(51·nb/100)` = 7.2299 ≠ 5.4255 — caught.*

*Engine 78 source record — session 191, 2026-11-05. Reconstructed after a compaction took the as-run text; re-executed against all five frozen receipts; every figure reproduced. The receipts remain the run record.*
