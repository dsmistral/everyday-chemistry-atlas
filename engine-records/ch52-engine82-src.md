# Engine 82 — Chapter 52, the Phase-3 Review — The Source (Reconstruction; the as-run literal lost)

Session 196 (2026-11-05). The honest status first: **the as-run source text was lost.** E82-RD ran in five sandbox pieces whose code lived only as run_typescript execution inputs; the session split at the context boundary (the split-on-trouble amendment) after the battery and the Revision Appendix landed but before this record set was authored, and the compaction took the run blocks with it — the Engine 80 event repeated, this time one session later in the pipeline. The Revision Appendix's "the as-run code preserved" line was written before the split, in the honest expectation that the runs were still consolidatable in-context; **this record corrects that line.** No claim of byte-identity with the as-run text is made, and none should be inferred from the code below.

What IS exact: the frozen transcripts (ch52-engine82-transcripts.md) print every row the engine touched — every input lane, every printed value, every witness triple, every injection and its caught value — and the design contract (ch52-engine82.md) fixes the semantics. The reconstruction below is keyed row-by-row to those transcripts: it is a faithful re-expression of the value path the transcripts evidence, not a recovered artifact. The distinction is the record's whole point.

```typescript
// E82-RD core (RECONSTRUCTION, keyed to the frozen transcripts — not the as-run literal)
// Exact rational lanes [n, d] of safe integers (< 2^53, pre-reduced); no floats, no
// recursion, no BigInt in the value path. The probe's own rows fix the semantics:
//   rhu(1/8, 2) = 13 ; rhu(1/3, 4) = 3333 ; rhu(2/3, 4) = 6667 ; trc(2/3, 4) = 6666
function pow10(dp: number): number { let p = 1; for (let i = 0; i < dp; i++) p *= 10; return p; }
function rhuInt(n: number, d: number, dp: number): number {  // round-half-up of n/d at dp, integer lane
  const p = pow10(dp);
  return Math.floor((2 * n * p + d) / (2 * d));               // exact: (n·10^dp)/d + 1/2 rounded down
}
function trcInt(n: number, d: number, dp: number): number {  // the truncation detector: floor at dp
  const p = pow10(dp);
  return Math.floor((n * p) / d);
}
function digits(v: number, dp: number): string {             // integer lane -> printed decimal
  const p = pow10(dp), w = Math.floor(v / p), f = v % p;
  return dp === 0 ? String(w) : w + '.' + String(f).padStart(dp, '0');
}
function dc(printed: string, n: number, d: number, dp: number): string {
  const r = digits(rhuInt(n, d, dp), dp), t = digits(trcInt(n, d, dp), dp);
  if (printed === r) return 'PASS';
  if (printed === t) return 'TRUNC';                         // the print floored its exact lane
  return 'FAIL';
}
// The element table independently re-transcribed (my = mg/mol x 10^3):
const EL: Record<string, number> = { H: 1008, C: 12011, N: 14007, O: 15999, Cl: 35450, Na: 22990, Bi: 208980 };
// molar(formula) and balance(lhs, rhs): iterative character walks, element counts merged
// per side, mass lanes summed exactly — the same contract as Engines 80/81, re-keyed here
// against Sheet A (32/32) and Sheet C (16 balances, counts + mass both).
// The battery drivers (probe, Sheets A-D2) are recoverable verbatim from the frozen
// transcripts: each row's inputs, printed values, and witness triples appear there in full.
```

The engine's reproducibility rests on the transcripts, not on this text: any implementation of the contract above that reproduces the frozen outputs row-for-row is the engine; anything else is not. The loss is real, the recovery standard is stated, and the next engine's source will be consolidated to disk the same session it runs — the lesson of Engine 80, now twice learned, made procedural.
