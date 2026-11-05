# Engine 82 — Chapter 52, the Phase-3 Adversarial Review — Design & Verdict

Session 196 (2026-11-05). **E82-RD, the rational-display engine.** Fresh build, zero code shared with Engines 1–81, run as the skeptic under the two-experts protocol: the prover's chapter (both parts, Engines 80/81 frozen figures) audited by an engine built to distrust displays.

## The design contract

- **Exact rational lanes:** every quantity carried as an [n, d] pair of safe integers, pre-reduced to stay under 2^53; no float ever gates an identity. Round-half-up at dp digits: rhu(n, d, dp) computed from (2·n·10^dp + d) div 2d — exact integer arithmetic; the truncation detector trc(n, d, dp) = (n·10^dp) div d, the floor of the exact lane at the printed precision.
- **The display audit dc(printed, n/d):** PASS if the printed digits equal rhu; **TRUNC** if they equal trc but not rhu — the print floored its exact lane, the error class this review actually found; FAIL otherwise. Every dose/economics display in the chapter audited at its own printed precision.
- **The element table independently re-transcribed:** my = mg/mol ×10³ — H 1008, C 12011, N 14007, O 15999, Cl 35450, Na 22990, Bi 208980; every molar mass of both parts recomputed, every balance of both engines recomputed on element counts and mass lanes; iterative walks only, no recursion, no BigInt, no floats in the value path.
- **The freezer:** every piece frozen to scratch with bash md5sum receipts before the splice (the receipts in ch52-engine82-transcripts.md), never retyped.

## The battery and the honest history

| Piece | Rows | Revs | History |
|---|---|---|---|
| Probe | 7/7, 3 injections CAUGHT | rev-1 | clean first run; the audit semantics proven on 1/8, 1/3, 2/3 and the 9.28/9.29 seam itself |
| Sheet A (molar book) | 32/32 MATCH + 1 injection CAUGHT | rev-1 | clean first run; both parts' every mass recomputed exact; the salt identity re-proved |
| Sheet B (display audit) | 20 PASS / 1 TRUNC / 7 FAIL + 3 fixed-lane rows | rev-1 | five of the seven FAILs harness-side lane slips (a 10× numerator, two missing ×100 percent factors, two more 10× numerators), fixed in Sheet D; the TRUNC and two FAILs the real findings RA-2, RA-1, RA-3 |
| Sheet C (balance book) | 15/16 PASS + 1 injection CAUGHT | rev-1 | two harness-side slips: the reduction's right side encoded H₂O₂ for 2 H₂O (C.6 FAIL), and C.10 built on a wrong-but-coincidence-balanced equation (its PASS was on the wrong lane — Lmass 349344, not the standard BiCl3 + H₂O → BiOCl + 2 HCl, whose true lane is 333345 both sides, D.7) |
| Sheet D (rev-2) | the fixed lanes; the suspect lanes at full witness precision; determinism 13/13 MATCH; 2 injections CAUGHT | rev-2 | the last two harness slips surfaced here: the 22.727 theoretical lane slipping a second time in a row (50,000/22 then 5,000/22, the true lane 500/22), and a 10⁴-short factor in the spoken-basis efficiency lane |
| Sheet D2 (rev-3) | the two remaining lanes fixed | rev-3 | D2.1 the true 500/22 lane PASS; D2.2 the exact spoken-basis efficiency 26,345.13 (witness 26,345×14,360,675 + 1,917,125 = 378,333,900,000 — the S3.7 printed divisor 26,347 wrong by +2); D2.3 the miss 125.26 |

Eight distinct harness lanes slipped across the three runs — one of them (the 22.727 lane) twice in a row — every slip harness-side, every slip disclosed in the frozen transcripts, the engine value path defect-free in every run (the probe, the twenty clean Sheet-B rows, and the 13/13 determinism pass prove the lanes); five injections CAUGHT across the battery.

## The findings (the verdict's content)

- **RA-1 — the exact-basis miss printed 125.25×; the true value is 125.26×.** S3.7's divisor 26,347 matches no exact lane in either battery; the true spoken-basis efficiency is 26,345.13 (witness above), and the miss it gives is 33t/21,000 with t = 95,000×151,165/180,159: value 125 r 984,900,000/3,783,339,000 (witness 125×3,783,339,000 + 984,900,000 = 473,902,275,000) = **125.26** — the very figure E80's sheet printed as "the honest alternate". Lecture 2's "125.25× on the exact basis" inherited the wrong divisor; S3.9's "125.3–126.9×" and the 126.9× headline stand.
- **RA-2 — the patch-load display truncated: 9.28 for 9.29.** The exact lane 6,500/700 = 9 r 200 → 9.2857; the two-decimal round-half-up display is **9.29**, and the Engine 81 transcript's own rev-2 note already said ~9.29 — the master text (§6.5 D4, Exercise 52.7) contradicted its own transcript. Both displays read 9.29 by the appendix; the witness triples unchanged.
- **RA-3 — the Daraprim percent annotated.** (750 − 13.50)/13.50 = 5,455.6% → **5,456** whole-percent; the printed "5,500 percent" stays as the sources' rounded display [convergent], the exact arithmetic named beside it — the honest-reporting tag was correct, and the annotation is the correction.

The corrections live in the master's Revision Appendix (extend-never-rewrite); zero frozen-figure chemistry moved; three displays corrected.

## Forensic notes

- **The 303,358 collision re-verified at its owner:** cocaine's my = Ch 51's piperine-hydrolysis closure total (285,343 + 18,015), re-grepped at Ch 51's own pages and the E78 records — the Canon-Coverage Check's claim exact.
- **The coverage sweeps re-run:** the eleven-word keyword sweep (Löfgren, Karolinska, Koller, MEGX, PABA, procaine, Novocaine, benzocaine, Lidoderm, chloroacetyl chloride, diethylamine) zero-hit outside ch52's own files; the integer-literal sweep zero-hit outside except the named collision; the fence audit re-read — the two lidocaine arrows remain named map entries, no conditions, quantities-as-instructions, or workup steps anywhere in either part.
- **The canvas drift, disclosed:** the ch52 canvas was found 1 byte drifted from the part-2 master (77,968 vs 77,969 B) at this session's re-materialization; re-materialized byte-exact against the reviewed master (83,442 B) — the drift never touched the repo, only the rendering.
- **The split, disclosed:** this review session split at the context boundary per the split-on-trouble amendment — part 1 (this session) = battery + Revision Appendix + records + close; part 2 (next session) = the reviewed web edition, oracle-first re-render with the banner `drafted`→`reviewed`, and the map flip `drafted`→`reviewed` at that close.
- **The source, honestly:** the as-run literal was lost to the session-196 context compaction — the Engine 80 event repeated, one session later in the pipeline; ch52-engine82-src.md carries a reconstruction keyed to the frozen transcripts and corrects the appendix's "as-run code preserved" line, which was written before the split.

## Verdict

**PASS WITH CORRECTIONS** — three findings (RA-1, RA-2, RA-3), zero frozen-figure chemistry moved; 32/32 molar rows and 16/16 balances re-verified exact; every dose/economics display passes its exact-lane audit except the three named; determinism 13/13; five injections CAUGHT; the honest harness history disclosed in full. The chapter's chemistry stands; three displays were corrected; the witness discipline that caught them is the battery's own argument for itself.
