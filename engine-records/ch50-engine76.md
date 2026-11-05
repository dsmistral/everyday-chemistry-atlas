# Engine 76 Record — E76-BT "the balanced-ternary engine" — Session 182, Vol VII Ch 50 review (Cubane)

**Session 182 (2026-11-05), repo dsmistral/everyday-chemistry-atlas, branch main.** Engine 76 is fresh this session and shares zero code with Engines 1–75. The chapter unit is the Phase-3 adversarial review of Vol VII Chapter 50 (drafted session 181); the re-verify-never-re-author rule governed throughout — every mismatch was to be raised as a finding, never silently patched (none was: the arithmetic produced zero mismatches; the four findings raised are count- and word-layer, receipted in the chapter's Revision Appendix).

## Design

E76-BT holds every quantity as a **balanced-ternary digit array** — digits −1, 0, 1, least-significant first, no sign field, negatives native — so **subtraction never borrows and the value path executes no multiplication anywhere**: digit products are sign-only (equal digits 1, unlike digits −1), **mulSmall 0–9** rides a nine-entry balanced-ternary sum table plus ×3ᵏ shifts and signed adds, **×10 = shift-two-plus-itself**, and division is long division against a power table P[t] = D × 10ᵗ with trial digits 0..9 and half-up decided on the true remainder at the target dp. The atom parser **reads right-to-left with a multiplier stack**, its two-letter symbols joined from whichever side the scan enters them (the rev-0 lesson). Gates: the **W1 float64 witness** typed from independent decimal weights, compared at the row's printed dp with a one-ulp boundary tolerance where float64 representation fails; the **held element table in micro-y units** (C 120110, H 10080, N 140070, O 159990, S 320600, Na 229900, Cl 354530, Mg 243050, Br 799040, K 390980); the **P18 name gate first**, admitting the restricted names only at recognition rank, plus the E75-D1-class **fence gate refusing PROCEDURAL rows outright**; the chains by a **fresh civil-date method — the backward calendar** (the year traversed from its end back to the date, the leap rule inside the month lengths, the rev-1 lesson) — a fourth method where E73 used days_from_civil, E74 the Fliegel–Van Flandern JDN, and E75 the month-table rank. The digest is **AP-32 (Arash Partow)**, 32-bit hex — distinct from E69's FNV-1a, E70's j31, E71's joat, E72's sdbm, E73's adler32, E74's crc32, and E75's PJW-ELF, none reused. Iterative only; no recursion.

## Honest run history (all defect classes caught before any battery row was accepted)

- **rev-0:** the right-to-left parser split "Br" into "B" + "r" when the scan entered the symbol from its lowercase side — the held table refused the unknown element B (bFromDec crashed on the undefined entry) before any sheet was written. Fixed with the lowercase-tail join.
- **rev-1:** the backward calendar's partial-month term priced February at its common-year length inside the 2024 leap year — **the frozen trilogy arc (14/28/42) refused the engine's 14/29/43, the frozen record correcting the fresh engine** (fixed: the leap rule moved inside the month lengths, mLen(m, leap)). The same pass caught **two drafter slips in the settlement build** (the register-basis denominator written 144000 for 144.0's 1440 at scale one; the 390-versus-377.7861120 ratio divided without its 10⁻⁷ scale) — every one caught by the frozen expectations before any sheet was written, never laundered.
- **rev-2:** all fixed; the battery clean and frozen.
- **An s5-builder slip outside the engine (never a value defect):** the determinism sheet's first build looked for the "elf" tag in E76's own "ap:" digest lines — the gate re-keyed; determinism itself held throughout.

## The battery (all machine-settled; transcript verbatim in ch50-engine76-transcripts.md)

```text
s0  the probe battery                  8 PASS + 1 seeded CAUGHT                       ap 2559bd33
s1  the molar book re-derived          27/27 two-lane (T1 recomposed 40779380 μy)      ap 3123b760
s2  the balances re-derived            12 PASS + 1 CAUGHT must-fail (T2 44740870 μy)  ap 86edb933
s3  the charge ledger re-derived       16/16, every printed figure two-lane            ap 440ead76
s4  the fresh-keyed injections          8 CAUGHT, 0 escaped                             ap f1601d8e
sR  the register settlement            12/12 SETTLED (the arc by the backward          ap 6228b08a
                                        calendar: the trilogy 14/28/42 EXACT)
s5  determinism                        6 byte-compares + 6 re-digests + T1/T2, 14/14  ap 23f08c18
sF  the frozen-record lane             E75's 7 per-sheet domains + whole battery,      ap 07819708
                                        recomputed from disk under the PJW rules,
                                        every digest MATCH — 8/8
```

**Verdict: ZERO ARITHMETIC FINDINGS.** Every frozen Engine 75 value reproduced exactly by an engine sharing no code with it: the 27-species molar book row for row with the T1 checksum recomposed exactly at 40779380 μy; the 12 balances mass-equal on both sides with the unbalanced must-fail caught at the same one-water gap of 18.015 g and T2 recomposed exactly at 44740870 μy; the 16-row charge ledger two-lane at every printed figure; the 12-row register settlement with the trilogy arc EXACT (14/28/42) by the different civil-date algorithm; eight fresh injections, all caught. And the frozen record itself re-verified from disk under its own digest rules: E75's seven per-sheet PJW domains and the whole-battery domain recomputed from the session-181 sheet files — s0 04887b8a, s1 0a01c08a, s2 0e42fe3a, s3 08db6bda, s4 0481ed6a, sR 06d6c0ba, s5 0ddef52a, the whole battery 09f7179a — every one MATCH.

## The census and the got-strings, re-verified

The freeze-gate census re-run at the 118-file corpus (the chapter's own homes excluded): the chapter's **25 new literals re-swept in one case-insensitive fixed-string pass — 23 zero-hit clean**, and the two that hit land exactly where the freeze named them ("192.17" ×25 only inside FC3's own 192.170 PET rows, the named same-empirical-formula collision; "5.96" ×6 only inside Chapter 8's 35.96/35.965 mL titration volumes, the named substring class). The word classes zero-hit as frozen (benzophenone, acetonitrile, adipic, cyclopentanone, Favorskii, Diels, photosensitizer, octanitrocubane, heptanitrocubane, Eaton, Chemiolis, Explosions and Fire, Extractions and Ire, That Chemist, Cube Chemistry) with **Lumiray the one prior presence, ×1 at Chapter 45**. The cross-chapter pins re-grepped at their owners, every count exactly as the Canon-Coverage records: Br 79.904 ×14, Br₂ 159.808 ×11, HBr 80.912 ×6, and the demand arithmetic 0.7880 ×2, 377.8 ×7, 1.0323 ×6, all at Chapter 43; glycol 62.068 ×7 at Chapter 45 with Chapter 21's ×3 behind it; dioxane's mass 88.106 ×10 at Chapter 45, ×5 at Chapter 23, ×2 at Chapters 24 and 21, the word ×74 at the owner and ×1 at Chapter 41; K 39.098 ×11 at Chapter 41; NaOH 39.997 at Chapter 8; H₂SO₄ 98.072 at Chapter 6; CO₂ 44.009 at Chapter 20; methanol 32.042 at Chapters 21/23 with the word at Chapters 47/48; Na₂SO₄ 142.036 at Chapters 13/14; K₂CO₃ 138.204 at Chapters 14/20 and FC5; NaHCO₃ 84.006 across the quench chapters; the thiosulfate word at Chapters 17/18/25/32/33; the digit coincidentals where the coverage names them ("57.9" ×4 at Chapter 20's denitrification rung; "287.541" at Chapter 19's ZnSO₄·7H₂O; "21.3" ×7 at Chapter 49's ammonia datum).

The got-strings re-swept single-pass (field-split on the double quote, unique spans, fixed-string index against the register — no pattern competition): **93 unique quoted spans, pair-level identical with the frozen sheet** — 73 register-verbatim at the register at their counted occurrences, 20 classified exactly as named (3 frontmatter, 2 engine strings, 9 book arithmetic, 2 coinages, 1 Chapter 43 cross-quote, 3 convergent-source), zero unaccounted; the built pairs diffed against the frozen got-span sheet with **zero differences**. The seven frozen transcript blocks verified byte-contained in the master and the E75 transcripts record against the session-181 sheets on disk. [speculative] verified spent exactly once, at the attribution tension in the Sources section.

## The findings (raised, never patched; full text in the chapter's Revision Appendix)

- **RF-1 (count layer):** the master says "thirteen" new molecules in three places (Lecture 0, and the Canon-Coverage twice) but the frozen Sheet 1 carries fourteen NEW rows and both of the master's own lists enumerate fourteen values/names — the honest count is fourteen; the word is the seam, no value moves.
- **RF-2 (count layer):** the cubane word at Chapter 43 is counted "twice" but the case-insensitive sweep finds five occurrences (2 capitalized video-title citations, 3 lowercase prose) — the word-prior stands, the count is the seam.
- **RF-3 (word layer):** the toluene word-prior list names Chapter 47, where the string exists only inside "p-toluenesulfonic acid" (×4) — the prior rests on Chapters 35 (×1) and 41 (×4).
- **RF-4 (word layer):** the ether prior names Chapters 34/42 behind Chapter 21's pin — Chapter 42's only "ether" strings are inside "together" (×3) and Chapter 34 has none at all; the honest prior is Chapter 21's mass pin plus Chapter 49's extraction word.

## The web battery (oracle-first)

The renderer reconstructed and **proven byte-identical against the session-181 oracle before use** (the extended Ch 49 master through the renderer = the repo's reviewed page, 68,663 chars, byte-for-byte; the session-181 "strip one trailing newline per chunk" read rule was corrected this session — `read_file` chunks are char-based line cuts joined raw, no stripping, and `wc -c` ≠ JS `.length` for multibyte UTF-8). The extended Ch 50 master then rendered with tailWord "reviewed" — **72,207 B** (md5 14ee3bd5289b356ce963f937a2305d11), verified to be the drafted page's 72,206 B with the one-character tail seam ("drafted" → "reviewed") the only difference. The Revision Appendix lives past the Canon-Coverage cut and remains in the .md master only, exactly as the opening banner states.

## Files

- `engine-records/ch50-engine76-transcripts.md` — the eight sheets verbatim (s0, s1, s2, s3, s4, sR, s5, sF), spliced from the session scratch files as they were generated (scratch is not storage: the sheets were on disk from the moment each froze).
- This record: `engine-records/ch50-engine76.md`.
- The chapter's Revision Appendix (in `manuscript/vol7/ch50.md`): the verdict, RF-1..RF-4, and the ◆ of Exercise 50.6 answered.

*Engine 76 record closed at session 182 (2026-11-05); the chapter it serves is Vol VII Ch 50, reviewed this session — PASS WITH FINDINGS RF-1..RF-4, none of them arithmetic.*
