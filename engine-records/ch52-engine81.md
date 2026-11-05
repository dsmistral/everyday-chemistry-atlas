# Engine 81 — Chapter 52, Lab 52.2 — Design & Verdict

Session 195 (2026-11-05). **E81-DE, the double-entry engine.** Fresh build, zero code shared with Engines 1–80.

## The design contract

- **Double-entry value path:** every operation verified by its inverse lane — addition by subtraction both ways (s−b==a and s−a==b), multiplication by division both ways, subtraction by re-addition, and every division returning the witness triple (q, r) with q·d+r==n and 0≤r<d; a deFails counter accumulates any inverse-lane failure and must stay 0 across the whole battery.
- **The held element table (unchanged from Engine 80):** my = mg/mol ×10³ — H 1008, C 12011, N 14007, O 15999, Cl 35450, Na 22990, Bi 208980. No new elements needed for the caine shelf.
- **Parser:** iterative character walk, no recursion, no BigInt, no floats in the value path; handles "."-separated additive parts (the salt suffix ClH) and throws a hard gate on any unknown element or character.
- **The freezer:** md5 (RFC 1321) self-validated against the standard vectors before first use; sdbm per the declared convention; every piece frozen to scratch with bash md5sum receipts before the splice, the in-splice md5 gates run in the same pass as the record push.

## The battery and the honest history

| Piece | Rows | Revs | History |
|---|---|---|---|
| Probe | 5/5, 3 injections CAUGHT | rev-1 | clean first run; deFails=0 |
| Sheet 1 (molar book) | 13/13 + 1 injection CAUGHT | rev-1 | clean first run; all ten published gates pass within 0.01 g/mol |
| Sheet 2 (balance book) | 7/7 + 1 injection CAUGHT | rev-1 | clean first run; B1–B6 hold on counts and mass, B7 the classification row |
| Sheet 3 (dose/economics) | 5/5 + 1 injection CAUGHT | **rev-2** | run-1 carried three harness-side slips the engine exposed: the D1 unit label (g printed for an mg value), the D4 truncated approximation (~9.14 for 6500/700≈9.29), and a mis-armed injection (stated 200, the TRUE remainder, so it missed); rev-2 fixed the labels and re-armed the injection at the original mistaken hand value 100; the engine value path identical and defect-free in both revs (deFails=0); no check moved |
| Sheet 4 (determinism) | 23/23 MATCH | rev-1 | clean first run; every molar, balance, and dose lane recomputed through reversed iteration orders, two independent passes per row |

Six injections CAUGHT in total (probe 3, one per sheet), every one a harness slip against exact lanes; one injection mis-armed at Sheet 3 run-1, disclosed and re-armed at rev-2.

## Forensic notes

- **Chloroacetyl chloride, the two-convention datum:** the held table gives my=112937 (Cl 35.450); the 112.949 figure visible in the teaching-lab pages reflects an older chlorine standard weight. The published gate holds against the modern rounded 112.94 (|Δ|=3); both conventions named, neither smoothed.
- **Diethylamine hydrochloride, the no-gate row:** it appears in this battery as a balance-lane species only; its 109.597 is the table's own sum, printed with a witness but no published gate, stated as such in the transcript.
- **The 303,358 collision:** cocaine's my here is the same integer as Chapter 51's piperine-hydrolysis closure total (285343+18015) — the Chapter 34 E8 pin re-derived. Different molecules, different provenance; named in the chapter's Canon-Coverage Check and in both records' lineages.
- **The B2 bookkeeping disclosure:** lidocaine → MEGX + C2H4 balances formally and is printed as formal bookkeeping only; in vivo the ethyl is oxidized further (CYP1A2, to 2,6-xylidine), not set free as ethylene — the transcript states its own limit in-row.

## Verdict

**PASS.** The engine value path defect-free in every run (deFails=0 across both runs and all five pieces); every revision harness-side and disclosed; determinism 23/23; six injections CAUGHT; the two named arrows (B5, B6) verified as count-and-mass-consistent map entries and never transcribed. The source is preserved (ch52-engine81-src.md) — the Engine 80 full-loss event not repeated.
