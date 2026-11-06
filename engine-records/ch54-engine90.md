# Engine 90 — E90-RA, the Exact-Rational Engine (session 207, the Ch 54 review)

Series paradigm 11. Zero code shared with any prior engine. Contract: every quantity is an exact reduced rational — a float64 integer pair (n, d) at full float64 integer range, reduced by iterative gcd, guarded at 2^51 denominator (and 2^60 at print-parse). Printed figures are gated as exact half-up roundings of the rational at the figure's own decimal count (the decimal count string-parsed from the manuscript's own printed figure, so the gate reads the page, not the plan). The engine never compares floats for truth; it compares rationals and rounds once, at print, half-up.

## Design

Rational ops: add/sub/mul/div by cross-multiply + gcd-reduce; pow by squaring with reduction each step; half-up rounding of a non-negative rational at k decimals = floor(200·n·10^k/d + 1)/(2·d)·10^-k — exact integer arithmetic throughout, the 2· trick shifting the 0.5 into the integer lane. Negative q prohibited at the rounding gate (no negative printed figure in the battery). Guard: reduce() refuses d ≥ 2^51 (qadd/qmul/qdiv/qpow all route through it); the print gate refuses parsed mantissas longer than 21 digits or denominators ≥ 2^60.

Constants: the five atomic masses in units of 10^-5 u — C 1201070, H 100800, O 1599940, Na 2298977, K 3909830 — each as exact rationals with denominator 10^5. Molar masses: benzaldehyde 106.12230, acetone 58.07950, DBA 234.29330, KOH 56.10570, NaOH 39.99717, glucose 180.15660, the glucose monohydrate (dihydrate seam disclosed at RH3) 294.10011, citric anhydrous 192.12400 — all built by the engine from the atom counts, never typed.

## The Rule-21 table self-check (13/13, first run, before any book)

The fresh Rule 21 (session 206's lesson: transcribed constant tables escape unit gates until a specific operand exercises the bad cell): the eight molar masses were self-checked entry-by-entry against trivial independent arithmetic — C7H6O = 7×12.0107+6×1.008+15.9994 = 106.1231 ≈ 106.12230 at the table's own 5 decimals — 13/13 PASS first run, zero transcription defects. The lesson held: no deep-lane surprise later.

## The battery (all receipts in the transcripts record)

- Table self-check: 13/13, first run.
- Probe (5 sanity identities): 5/5, first run.
- Molar book B1 (the chapter's printed figures vs the exact lanes): 8 PASS + 1 lane-FAIL — B1-6b, the 69.89 yield percent. Root cause: the manuscript lane is the UNROUNDED-mol lane (22.3 g / 31.90830 g = 69.8878 → 69.89); the rounded-mol lane displays 69.88. This is the RF-2 finding: a named-of-record lane, both displays within 0.01 of each other, robust at the honest 70. Not an engine defect; the gate did its job.
- Balance book B2 (the four stoichiometric balances, Cannizzaro and Claisen–Schmidt lanes): 8/8, first run.
- Dose/economics book B3 (SPF factors, per-unit costs, the crawl tally): 18/18 at rev-3. Honest run history: rev-1 crashed at parse (harness syntax), rev-2 crashed at a missing qadd — both harness-side, disclosed, nothing written, fixed and re-run clean. The value path never produced a wrong number.
- Review hunt RH (the 9 independent re-derivations): 2 SUSTAINED, 3 NOTE, 4 CLEAN, at rev-2 — rev-1's RH6 harness formula slip (107.99 vs the 7.99 shift-vs-ratio lane) disclosed and fixed. The SUSTAINEDs: RH1 (the SPF 30 anchor: 30/3 = 10 exactly, transmission (1/3)/(1/30) = 10 exactly) and RH2 (the N449 1.1157 register vs the naive 1.1M composition 1.1164 — the register holds; implied crawl base 1,100,682). The NOTEs: RH3 (DBA 234.29 correct on the IUPAC 12.0107 basis, 234.29330; the 12.011 textbook basis displays 234.30), RH4 (KOH 56.1/56.11 both displays of 56.10570, already named of record), and the tB1 RF-2 lane.
- Injections J (4 deliberate defects): 4/4 CAUGHT, first run — a 2^60-guard violation, an inverted ratio (0.43261 vs 2.31141), a truncated denominator (2.7377 vs 2.73767...), and a digit-slipped figure (106.21 vs the manuscript's 106.12 — the engine caught it at the string-parse gate). The gates work at the boundary conditions they exist for.
- Determinism: the B3 replay ran byte-identical (diff clean, md5 c7e8a716 both runs).

## Verdict

PASS WITH CORRECTIONS. RF-1: the chapter's 'twenty-fold short of the bottle' (3 occurrences: Lecture 2, Lecture 5, Ex 54.2) follows from no stated figure — the chapter's anchor is SPF 30, and 30/3 = 10 exactly, transmission (1/3)/(1/30) = 10 exactly — corrected of record to 'ten-fold'. RF-2: the 69.89 yield percent is the unrounded-mol lane display; the rounded-mol lane displays 69.88; lane named of record, robust at 70. RH2–RH4 notes stand as above. The Revision Appendix is appended to the master (commit 8f99c0c4).

## Canon re-grep

20 key literals zero-hit over the complete local web corpus (68 files, all chapters' reading editions) + local manuscripts + engine-records, excluding ch54 and its E84 records; controls pass (180.16 → Ch 34/53/54; Cannizzaro → Ch 51/54). Honest disclosure: GitHub search_code returned a false all-zero (0 hits for known-present literals — the index is dead for this repo; the control literals caught it). The local corpus is the coverage of record; the local manuscript mirror carries only volumes 6/8/9, with full content coverage via the complete local web corpus.

## Honest run history

B3 rev-1 syntax crash (harness), B3 rev-2 missing-qadd crash (harness), RH rev-1 the shift-vs-ratio formula slip (harness), the read-shape slip at the master push (a nested-extraction pattern that fails on this read_file's plain shape — no effect on the push, the master landed at 58,062 B exactly), and the search_code false all-zero (tool defect, caught by controls). Zero engine value-path defects across the entire battery.

## Receipts (bash wc -c / md5sum)

```
design source e90-design.md   2880 B  82e80c18cf7ab3e4b688de4eacdd0e57
tablecheck.txt                 574 B  3b034436a97bcff654fb227fd6380f53
probe.txt                      307 B  84a238f0af68f7648a76e371b509308a
tB1.txt                        560 B  c24effc6ce9d5a3bc155f6084d3629
tB2.txt                        739 B  d2cacb7ca66d8f946ba39150f03613f3
tB3.txt                       1161 B  c7e8a716da6b94d4545e07160f586239
tRH.txt                       2078 B  2e5fa4e9fe8e046f1a9a6635a3c3f59a
tJ.txt                         414 B  3d773a622bb4de1b1ae67feb6a9c3209
tB3r.txt (replay)             1161 B  c7e8a716da6b94d4545e07160f586239
appendix54.md (the Revision Appendix source)  6489 B  76e9cdfa275669b3f9a99590a7e5cd8e
master manuscript/vol8/ch54.md at HEAD       58062 B  29955581328415b3c18a7ceed8f82906
```
