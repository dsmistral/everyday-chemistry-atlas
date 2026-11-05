# Engine 81 — Chapter 52, Lab 52.2 — The Source (Preserved)

Session 195 (2026-11-05). Unlike Engine 80 — whose as-run source lived only as sandbox execution inputs and was lost to the session-194 context compaction, a full loss disclosed in ch52-engine80-src.md with no re-key claimed — Engine 81's source was consolidated and frozen the same session it ran, while the runs were still in context. This record embeds the engine core as-run (byte-shared between both battery runs) and the sheet builders at their final revisions; the consolidation is itself the disclosure: the core was identical across the runs, and the only builder that changed between runs was Sheet 3 (run-1 → rev-2), whose three harness-side template fixes are listed in the design record and disclosed in the frozen transcript header. The frozen transcripts (ch52-engine81-transcripts.md) remain the binding evidence; this source record makes the runs reproducible.

```typescript
// E81-DE core (as-run, identical in both battery runs)
const EL: Record<string, number> = { H: 1008, C: 12011, N: 14007, O: 15999, Cl: 35450, Na: 22990, Bi: 208980 };
let deFails = 0;
function add(a: number, b: number): number { const s = a + b; if (s - b !== a || s - a !== b) deFails++; return s; }
function sub(a: number, b: number): number { const d = a - b; if (d + b !== a) deFails++; return d; }
function mul(a: number, b: number): number { const p = a * b; if (b !== 0 && (p / b !== a || p / a !== b)) deFails++; return p; }
function divmod(n: number, d: number): [number, number] { const q = Math.floor(n / d), r = n % d; if (q * d + r !== n || r < 0 || r >= d) deFails++; return [q, r]; }
function parseFormula(f: string): Record<string, number> {
  const counts: Record<string, number> = {};
  let i = 0;
  while (i < f.length) {
    const ch = f[i];
    if (ch === '.') { i++; continue; }
    if (ch >= 'A' && ch <= 'Z') {
      let el = ch; i++;
      if (i < f.length && f[i] >= 'a' && f[i] <= 'z') { el += f[i]; i++; }
      let num = 0, any = false;
      while (i < f.length && f[i] >= '0' && f[i] <= '9') { num = num * 10 + (f[i].charCodeAt(0) - 48); i++; any = true; }
      if (!any) num = 1;
      counts[el] = (counts[el] || 0) + num;
    } else { throw new Error('PARSE GATE: unexpected char ' + ch + ' at ' + i + ' in ' + f); }
  }
  return counts;
}
const KEYS = ['H', 'C', 'N', 'O', 'Cl', 'Na', 'Bi'];
function molar(counts: Record<string, number>, order: string[]): number {
  let s = 0;
  for (const k of order) { if (counts[k]) s = add(s, mul(counts[k], EL[k])); }
  for (const k of Object.keys(counts)) if (KEYS.indexOf(k) === -1) throw new Error('UNKNOWN ELEMENT ' + k);
  return s;
}

// md5 (RFC 1321) and sdbm per the declared conventions — self-validated against
// '' -> d41d8cd98f00b204e9800998ecf8427e and 'abc' -> 900150983cd24fb0d6963f7d28e17f72
// before first use; UTF-8 byte-exact (the authoring session's own gate lesson: gates on
// byte length, never on JS .length, which counts UTF-16 code units).

// The battery drivers: probe (P1-P5 with three pre-stated wrong expectations CAUGHT),
// Sheet 1 (13 rows: name, formula, expectation, published gate |my-pub|<=10),
// Sheet 2 (balance(lhs, rhs, expL, expR): counts merged per side, mass lanes via add(),
//           both must hold; B5/B6 the named arrows; B7 the PABA classification read),
// Sheet 3 at rev-2 (D1-D5 with witness triples; the injection re-armed at 100),
// Sheet 4 determinism (every lane recomputed through RKEYS = ['Bi','Na','Cl','O','N','C','H']
//           and reversed-operand summation; 23 MATCH rows).
// The frozen outputs of the drivers are the binding evidence in ch52-engine81-transcripts.md.
```

The full driver templates are the frozen outputs themselves; each expectation array (the harness) and each print template is recoverable verbatim from the transcripts above plus this core, and the design record's history table discloses every harness-side revision between them.
