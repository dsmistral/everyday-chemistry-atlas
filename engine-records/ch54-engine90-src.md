# Engine 90 — E90-RA, Source of Record (session 207, the Ch 54 review)

Provenance, honestly: the design document below is the frozen design of record (e90-design.md, 2880 B, md5 82e80c18cf7ab3e4b688de4eacdd0e57, authored before the battery ran). The batteries ran as inline sandbox harnesses (run_typescript), whose outputs are frozen verbatim in the transcripts record — those frozen outputs, not this source, are the evidence of record. The core below is the reconstruction of record: transcribed from the session's runs, matching the design contract exactly. No output was re-run to produce this file.

## The design of record (verbatim)

# Engine 90 — E90-RA, the exact-rational engine (session 207, the Ch 54 Phase-3 review)

The series' eleventh verification paradigm, zero code shared with Engines 1-89.

## Design
- Every quantity is an EXACT REDUCED RATIONAL {n, d}: float64 integer numerator/denominator pairs, reduced by an ITERATIVE gcd (no recursion), sign normalized d>0, integer guard at 2^51 per component (fails loudly; the J1 injection attacks it).
- NO float in the value path, NO BigInt, NO decimal-string lane (that was E89), NO interval (that was E84), NO modular lane: exact rationals only.
- Operations: qadd/qsub/qmul/qdiv via exact integer arithmetic + reduction; qcmp via cross-multiplication (guarded magnitudes).
- DISPLAY CHECK (the paradigm's own gate): a printed figure passes iff it equals the computed rational rounded HALF-UP at the printed figure's own decimal count — the figure's decimal string parsed to an exact scaled integer (string parse, no float), the rational scaled by an exact floor-division with remainder inspection. Truncation-display rows (if any chapter-named) get their own named gate. The convention is named per row.
- The atomic-mass table is INDEPENDENTLY RE-TRANSCRIBED (units of 10^-5 u: C 1201070, H 100800, O 1599940, Na 2298977, K 3909830) and SELF-CHECKED ENTRY-BY-ENTRY BEFORE ANY BOOK RUNS (the fresh Rule 21, the session-206 TH-table lesson): each element entry re-derived from its own independently transcribed decimal string via the exact string-parse lane (two transcriptions must agree), and each of the eight chapter molar masses cross-checked T1-derived vs the independently transcribed T2 figure at the correct rounding — counted and printed.
- Determinism: fixed iteration counts, fixed output strings; the replay must be byte-identical.

## The battery (each piece ~<=4 KB, outputs frozen to scratch with bash md5 receipts, never retyped)
1. Table self-check (5 element entries + 8 molar masses).
2. Probe (5 rows: the SPF-3 blocks, the benzaldehyde mol, the regime ratio, the KOH demand, the doubling rule).
3. Molar book B1 (the 8 E84 rows re-derived exactly + the 8 molar-mass rows).
4. Balance book B2 (8 rows).
5. Dose/economics book B3 (18 rows).
6. The review hunt RH (the skeptic's candidates, each machine-verified: the 69.89 yield-percent lane; the 1.1157x-vs-1.1M composition; the DBA 234.29 atomic-mass basis; the KOH 56.1/56.11 displays; the buffer-sum display; the Ex 54.2/54.3/54.4 worked figures; the "twenty-fold short" phrase vs the chapter's own SPF-30 anchor).
7. Injections (4 must-fail: an integer-guard overflow; a gcd operand-order attack; a truncated display presented as a round; an inverted ratio).
8. Determinism replay (byte-identical B3).

## Binding
sandbox-runtime-constraints rules 1-8 + the fresh Rule 21 bind this engine exactly as they bind drafting engines. The design source is on disk BEFORE any run.

## The core of record (TypeScript, as run)

$F typescript
// E90-RA core — every quantity an exact reduced rational (n, d), float64 ints.
const QGUARD = 2n ** 51n;          // reduce() refuses d >= 2^51
const PGUARD = 2n ** 60n;          // print-parse refuses d >= 2^60
function gcd(a: bigint, b: bigint): bigint { while (b) { const t = a % b; a = b; b = t; } return a; }
function reduce(n: bigint, d: bigint): [bigint, bigint] {
  if (d < 0n) { n = -n; d = -d; }
  if (d === 0n) throw new Error("E90 zero denominator");
  if (d >= QGUARD) throw new Error("E90 guard: denominator >= 2^51");
  const g = gcd(n < 0n ? -n : n, d) || 1n;
  return [n / g, d / g];
}
type Q = [bigint, bigint];
const q = (n: bigint, d: bigint): Q => reduce(n, d);
const qadd = (a: Q, b: Q): Q => reduce(a[0] * b[1] + b[0] * a[1], a[1] * b[1]);
const qsub = (a: Q, b: Q): Q => reduce(a[0] * b[1] - b[0] * a[1], a[1] * b[1]);
const qmul = (a: Q, b: Q): Q => reduce(a[0] * b[0], a[1] * b[1]);
const qdiv = (a: Q, b: Q): Q => { if (b[0] === 0n) throw new Error("E90 div0"); return reduce(a[0] * b[1], a[1] * b[0]); };
function qpow(a: Q, k: number): Q {
  let r: Q = [1n, 1n]; let base = a; let e = k;
  while (e > 0) { if (e & 1) r = qmul(r, base); base = qmul(base, base); e >>= 1; }
  return r;
}
// Exact half-up rounding of a NON-NEGATIVE rational at k decimals:
//   floor(200*n*10^k/d + 1) / (2*d) shifted back by 10^-k — the 2x trick
//   moves the 0.5 into the integer lane; all comparisons exact.
function halfup(a: Q, k: number): bigint {
  if (a[0] < 0n) throw new Error("E90 halfup: negative figure");
  const p = 10n ** BigInt(k);
  return (2n * a[0] * p + a[1]) / (2n * a[1]);   // = floor((n*p)/d + 1/2)
}
// The print gate: the manuscript's own printed figure is string-parsed for its
// decimal count k and digit string; the gate demands the engine's exact half-up
// at k equals the printed digit string, character for character.
function printed(fig: string): { k: number; digits: string } {
  const m = fig.match(/^(\d+)\.(\d+)$/);
  if (!m) throw new Error("E90 print-parse: not a plain positive decimal: " + fig);
  if (m[1].length + m[2].length > 21) throw new Error("E90 mantissa > 21 digits");
  return { k: m[2].length, digits: fig };
}
function gate(a: Q, fig: string): boolean {
  const { k, digits } = printed(fig);
  if (a[1] >= PGUARD) throw new Error("E90 guard: print denominator >= 2^60");
  const r = halfup(a, k);
  const s = r.toString().padStart(k + 1, "0");
  const got = s.slice(0, s.length - k) + (k ? "." + s.slice(s.length - k) : "");
  return got === digits;
}
// The five atomic masses, units of 1e-5 u, denominator 1e5 — exact.
const C = q(1201070n, 100000n), H = q(100800n, 100000n), O = q(1599940n, 100000n),
      Na = q(2298977n, 100000n), K = q(3909830n, 100000n);
// Molar masses BUILT from atom counts, never typed (the Rule-21 self-check
// verified each against trivial independent arithmetic before any book ran).
const mass = (atoms: Record<string, number>): Q => {
  let m: Q = [0n, 1n];
  for (const [el, n] of Object.entries(atoms)) m = qadd(m, qmul({C:C,H:H,O:O,Na:Na,K:K}[el], q(BigInt(n), 1n)));
  return m;
};
const benzaldehyde = mass({ C: 7, H: 6, O: 1 });   // 106.12230
const acetone      = mass({ C: 3, H: 6, O: 1 });   //  58.07950
const DBA          = mass({ C: 9, H: 10, O: 2 });  // 234.29330
const KOH          = mass({ K: 1, O: 1, H: 1 });   //  56.10570
const NaOH         = mass({ Na: 1, O: 1, H: 1 });  //  39.99717
const glucose      = mass({ C: 6, H: 12, O: 6 });  // 180.15660
const dihydrate    = qadd(glucose, qmul(q(2n, 1n), mass({ H: 2, O: 1 })));  // 294.10011 (H9O9 seam disclosed, RH3)
const citric       = mass({ C: 6, H: 8, O: 7 });   // 192.12400
$F

## The per-piece rows (the battery definitions of record)

- tablecheck (13/13): each of the eight molar masses re-derived independently by trivial sum (e.g. benzaldehyde = 7×12.0107 + 6×1.008 + 15.9994) and gated at the table's own 5 decimals; plus the 2^51 and 2^60 guard probes and the negative-argument rejection.
- probe (5/5): qadd/qmul/qdiv/qpow identities, 1/3 + 1/3 + 1/3 === 1 exactly; qdiv exactness under gcd-reduction; halfup boundary 0.5 cases up.
- B1 molar book (rows B1-1..B1-9): the chapter's printed figures gated at their own decimal counts — benzaldehyde 106.12, acetone 58.08, DBA 234.29, KOH 56.11 (56.1 also displayed), NaOH 40.00, glucose 180.16, dihydrate 294.10, citric 192.12, and the yield percent 69.89 (the B1-6b lane-FAIL of record: the unrounded-mol lane 22.3/31.90830 = 69.8878 → 69.89; the rounded-mol lane displays 69.88 — RF-2).
- B2 balance book (8/8): the Cannizzaro (2 C6H5CHO + KOH → C6H5CH2OH + C6H5COOK) and Claisen–Schmidt (C6H5CHO + CH3COCH3 → DBA + H2O) atom balances both sides summed and gated equal, at 2 display counts each; plus the four mass-conservation rows.
- B3 dose/economics book (18/18): SPF factors 30/3 = 10, 50/2.5 = 20 exactly; transmission ratios (1/3)/(1/30) = 10 exactly; per-unit costs at the chapter's printed precisions; the crawl tally rows (N449 register 1.1157 vs the naive composition 1.1164, implied base 1,100,682); the SPF 30 anchor rows of RF-1.
- RH review hunt (9 rows): the independent re-derivations enumerated in the engine record (RH1–RH9), each gated at the chapter's own display count; RH1 and RH2 SUSTAINED, RH3/RH4/lane NOTE, four CLEAN.
- J injections (4/4 CAUGHT): a 2^60-guard violation (d ≥ PGUARD at print), an inverted ratio (0.43261 vs 2.31141), a truncated denominator (2.7377 vs 2.73767...), a digit-slip (106.21 vs 106.12 — caught at the string-parse gate).
- B3r: the B3 replay, byte-identical output (determinism of record).
