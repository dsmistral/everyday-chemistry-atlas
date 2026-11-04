# Engine 67 — source record and design specification

> **DISCLOSURE — the lost-source class (the session-170 precedent, disclosed, never laundered).** Engine 67 was built and run in the session-173 sandbox in split pieces (the s0 probe; s1+s2 rev-2; s3+s4 rev-2; the s5 determinism run). The session underwent a platform context compaction at the final-records phase, and the exact source text — held only in the run bodies — was lost before it could be saved to the durable record. The transcripts and their digests WERE saved at run time (`ch46-engine67-transcripts.md`) and are the verification anchors. Nothing below is a reconstruction of the lost text; it is the design specification as recorded in the project record, sufficient to re-key a fresh engine. The Phase-3 review's fresh engine (session 174) re-derives every row independently per the standing protocol, exactly as Engines 62/64/66 did for their chapters.

## 1. The kernel (as designed and run)

- **Rationals as canonical CF expansions.** Every exact rational is expanded once into its canonical continued fraction [a₀; a₁, a₂, …]: the integer part, then the partial quotients produced by the Euclidean steps. Values are built CF-first (the chapter's charges as exact integer ratios), never parsed from decimals.
- **Convergent-lattice reconstruction.** The p/q reconstruction is a single iterative pass (p_i = a_i·p_{i−1} + p_{i−2}, q_i = a_i·q_{i−1} + q_{i−2}), with the **determinant identity pᵢqᵢ₋₁ − pᵢ₋₁qᵢ = (−1)^(i−1)** asserted at EVERY step as the machine witness (detW in the transcripts). A failed determinant at any step fails the row.
- **The roundtrip witness (rt).** expand → reconstruct → re-expand must reproduce the canonical expansion exactly; a divergent re-expansion fails the row (rt in the transcripts).
- **Arithmetic on the lattice.** The four operations are performed on the reconstructed integer pairs (schoolbook, exact), each result re-canonicalized through its own CF expansion and re-witnessed — the CF is not a serialization of the rational, it is the rational's own certificate.
- **Printing.** round-half-up at the row's stated precision, with the floor taken on the lattice (CF-native), never via float truncation; **D2 — the negative lane is refused by design**: the rev-1 L13 defect (a mis-parenthesized percent multiply producing a negative, rendered by the draft printK as the malformed "-99.-63") is closed by making every negative result an error, not a print.
- **The float64 witness lane (f:).** an independent path from the ORIGINAL charges, sized to each row's printed granularity; agreement checked to the digit shown. It caught both hand slips (L06, L13) with the exact lane.
- **Guards.** 9.0e15 magnitude guard on every intermediate; atom-multiset gate on every balance (atoms:); split pieces; no recursion; no BigInt — the sandbox-runtime constraints in force since the Engines 59–66 lessons.

## 2. The harness (as designed and run)

- **s0 probe** — five rows pinned before any sheet ran: the chapter's central mass (32.046), the B1 balance equality, the yield fraction at 4 decimals, the Ch 20 couple print (21.2 kJ), and one injected must-fail (74.43 vs frozen 74.44) required CAUGHT before the engine was trusted.
- **Sheets 1–2** — the molar book (16 species on the held-22 element basis, each composition expanded, computed, and double-witnessed) and the balances (6 rows, atom-multiset + exact rational equality on both sides).
- **Sheets 3–4** — the lineage ledgers (19 rows, the publication's recipe computed from its own charges) and the injection battery (8 must-fail rows: wrong-table, wrong-basis, transposition, atom-gate, scale, and copy errors — all required CAUGHT).
- **Sheet 5** — determinism: the full 54-row battery built twice in one run and compared byte-identically (sdbm c98d820d both times).

## 3. Digest convention (inherited from Engine 66, stated for the record)

sdbm: h = 65536 + Σ (c + (h << 6) + (h << 16) − h), charCode lane, printed as UNPADDED hex, computed over the transcript text WITHOUT the trailing newline. Durable anchors: probe 6f01148c; s1+s2 rev-2 3301847f; s3+s4 rev-2 9a68a344; s5 c98d820d (twice, byte-identical).

*Source record — session 173, 2026-11-04. The loss is disclosed; the transcripts are the contract; the review's fresh engine is the re-derivation of record.*
