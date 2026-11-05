# Engine 74 Record — E74-SD "the string-decimal engine" — Session 180, Vol VII Ch 49 review (Photochromism and Cold)

**Session 180 (2026-11-05), repo dsmistral/everyday-chemistry-atlas, branch main.** Engine 74 is fresh this session and shares zero code with Engines 1–73. The chapter unit is the Phase-3 adversarial review of Vol VII Chapter 49 (drafted session 179); the re-verify-never-re-author rule governed throughout — every mismatch was to be raised as a finding, never silently patched (none was: the arithmetic produced zero mismatches; the findings raised are cross-reference-, record-, and attribution-level, receipted in the chapter's Revision Appendix).

## Design

E74-SD holds every quantity as a **sign, a digit string, and a decimal scale** — value = sign × digits × 10⁻ˢᶜ — with **no BigInt and no Number in the value path**: the schoolbook string algorithms carry every operation — **addD/subD** with explicit carry and borrow columns, **mulD** as an O(n·m) carry table, **divHalfUp** as digit-by-digit string long division generating frac+1 digits with half-up decided on the (frac+1)-th digit, and the render as a scaled-integer split (numerator padded by 10^frac, denominator 10^sc, quotient split at the decimal point — a representation sharing nothing with Engine 73's coprime BigInt rationals except the problem set). The atom parser is a **single-pass group stack that reads a closing bracket's trailing multiplier at the close** (not E73's two-pass table, not E71's character-walker). Gates: the **W1 float64 witness** typed from independent decimal constants (C 12.011, H 1.008, N 14.007, O 15.999, S 32.06, Na 22.99, Cl 35.453, Mg 24.305); the **held element table in micro-y units as digit strings** (C 120110, H 10080, N 140070, O 159990, S 320600, Na 229900, Cl 354530, Mg 243050 — 1 e-4 g/mol); the **P18 name gate first**; the date chains by a **fresh civil-date method — the Fliegel–Van Flandern JDN with truncating integer division** (where E73 used days_from_civil). The digest is **CRC-32, IEEE reflected polynomial 0xEDB88320** — distinct from E69's FNV-1a, E70's j31, E71's joat, E72's sdbm, and E73's Adler-32, none reused. Iterative only; no recursion.

## Honest run history (all defect classes caught before any battery row was accepted)

- **rev-0:** the integer-part accumulator kept leading zeros ("000600.560" for 60.056 — four probe FAILs) AND the seeded-fault row escaped because its gate compared a hard-coded string instead of the witness.
- **rev-1:** qInt leading zeros stripped; the SF row made to compare the truncation lane against the divHalfUp witness dynamically — and the probe then caught **two scale defects rev-0's garbled output had masked**: the molar-book divisor was 1000 instead of 10000 (the held table is 10⁻⁴ g/mol; urea priced at 600.560) and the render's denominator was over-scaled by 10^frac (9.995 rendered 0.10; 0.25 × 4 rendered 0.01).
- **rev-2:** both fixed; the probe clean and frozen (8 PASS + 1 CAUGHT).
- **Battery authoring (row encodings, not the engine), caught by the two-lane and register discipline, never laundered:** the first s3 build carried six mis-scaled row encodings (L20's $0.10 written as 10; L21's numerator pre-scaled ×1000; L22/L25/L26's 63.012 carried at scale 2 for scale 3; L24 double pre-scaled) and the sR build mis-encoded S05 twice (1.85/10; then a spurious division wrapped around a plain product) — every one caught by the W1 lane or the register row, the engine core untouched throughout (frozen at rev-2 from s0 on).

## The battery (all machine-settled; transcript verbatim in ch49-engine74-transcripts.md)

```text
s0  the probe battery                  8 PASS + 1 seeded CAUGHT                       crc32 711fdf24
s1  the molar book re-derived          23/23 (22 species + T1 exact 17178130 μy)       crc32 ccd03c75
s2  the balances re-derived            11 PASS + 1 CAUGHT must-fail (T2 exact 12546100) crc32 37ce3e1e
s3  the charge ledger re-derived       26/26, every printed figure two-lane             crc32 f65fca26
s4  the fresh-keyed injections          8 CAUGHT, 0 escaped                             crc32 f0b36a0d
sR  the register settlement            20/20 SETTLED (chains by the fresh FVF JDN)     crc32 1899029e
s5  determinism                        s4/sR byte-identical, disk-matching; G5 MATCH    crc32 ab883255
whole battery (six sheets as written)  crc32 14515d26
```

**Verdict: ZERO ARITHMETIC FINDINGS.** Every frozen Engine 73 value reproduced exactly by an engine sharing no code with it: the 22-species molar book row for row with the T1 checksum re-derived exactly at 17178130 μy; the ten balances mass-equal on both sides with the unbalanced must-fail caught at the same one-water gap of 18.015 g and T2 re-derived exactly at 12546100 μy; the 26-row charge ledger two-lane at every printed figure; the 20-row register settlement with all five chain dates EXACT (13/18/39/70 and the 1254-day arc-to-fridge torch pass) by the different civil-date algorithm; eight fresh injections, all caught.

## The census and the got-strings, re-verified

The freeze-gate census re-run at the **full 101-file mirror held locally — 110 files** (the 48 chapter masters, the 11 Field Companion masters, and the 42 engine records, plus the survey's transport duplicates; the chapter's own files excluded): **all distinctive new literals zero hits** — 259.221, 169.227, 79.102, C₁₂H₉N₃O₄, C₁₂H₁₁N, DNBP, dinitrobenzyl, benzylpyridine, pyridine, Birkeland, Eyde, refrigeration, photochromism, 205,980, 205980, 24.75, $163, 14.75, 600 nm, 216 h, 225 W, 44.012, 53.491, 149.7, 9.33. The word pins re-grepped case-insensitively at their owners, every count exactly as the Chapter Ledger records: urea 60.056 at Chapter 20 with the fifteen-hit re-pin at Chapter 46; ammonium nitrate 80.043 at Chapter 15; nitrous oxide 44.013 twice at Chapter 20; the +25.7 kJ endotherm twice at Chapter 26; "cold pack" twenty, "ammonium nitrate" ten, "sal ammoniac" eleven at Chapter 20; epoxy twenty-six at Chapter 35; cyanotype fifteen at Chapter 32 with Chapter 48's single neighbor hit; nitration four at Chapter 15; 400 nm four at Chapter 32; refrigerant two at Chapter 20; endotherm across Chapters 7, 20, 26, and 45. The digit coincidentals all land where the ledger names them ("48.6" at Chapter 26's work term and Chapter 48's Exercise 48.6, with Chapter 30's portlandite 48.6777 a third owner of the same digit string, verified coincidental and added to the coincidence roll here; "21.3" at Chapter 20's 21.312 among others; "9375" at Chapter 39's 10.509375; "2564" at Chapter 6 and fc8; "2571" once at Chapter 19; "1254" at fc9's kaolin temperatures).

The got-strings re-swept single-pass (field-split on the double quote, unique spans, index() against the register — no pattern competition): **99 unique quoted spans** — 89 byte-verbatim (87 in the three primary batches 33cg/31k/33ch; "MATCH" and "MISMATCH" in the wider register), **10 internal**, every one on the ledger's named list (the frontmatter's three fields; "1254"; "150."; "MISMATCH,"; "closing on itself," quoted once without the ledger's trailing comma; the three book-corpus census words, verified at Chapter 48 line 45 and twice at Chapter 20). The ledger's 100-span total and eleventh internal span do not reproduce — RF-2; every episode quote verifies at its source. The seven transcript blocks verified byte-contained in the master against the E73 sheets on disk. [speculative] verified spent exactly once at its declaration, its three other appearances all naming the spend.

## The findings (raised, never patched; full text in the chapter's Revision Appendix)

- **RF-1 (cross-references, internal consistency):** the confinement fence is "stated at Lecture 3" (abstract) and "stated at Lecture 3 and Lecture 5 and enforced at the Safety Table's row 3" (the closing labels paragraph) — but no lecture body states it (the words vessel/grind/confined appear only in the abstract and the Safety Table), and the fence's binding row is row 10, not row 3 (row 3 is the ammonium nitrate row carrying the specific never-heat instruction — the kernel the pointer presumably reached for). The binding line's rank — the twenty-first, after Chapter 48's twentieth — verifies.
- **RF-2 (record-internal):** the E73 got-strings ledger's counts (100 unique / 89 verbatim / 11 internal) do not reproduce; the fresh sweep gives 99 / 89 / 10 with the named internal list complete. No episode word differs anywhere.
- **RF-3 (attribution):** the Chapter Ledger's claim that "the register's arithmetic figure would print 44.012" for nitrous oxide is unreconstructible from the register as stored — the survey carries no 44.012 in any file. The book's side verifies everywhere: 44.013 is the held table's print (440130 μy), Chapter 20's pin, and the chapter's printed value with the seam disclosed.

## The web battery (oracle-first)

The renderer reconstructed from the session-179 render itself and **proven byte-identical against it before use** (the drafted master through the renderer = the repo's drafted page, 68,662 chars, byte-for-byte); the extended master then rendered with tailWord "reviewed" — 69,352 B, the +1-char tail seam ("drafted" → "reviewed") the only difference from the drafted page's 69,351 B. The Revision Appendix lives past the Canon-Coverage cut and remains in the .md master only, exactly as the opening banner states.

## Files

- `engine-records/ch49-engine74-transcripts.md` — the seven sheets verbatim, spliced from the session scratch files as they were generated (scratch is not storage: the sheets were on disk from the moment each froze).
- This record: `engine-records/ch49-engine74.md`.
- The chapter's Revision Appendix (in `manuscript/vol7/ch49.md`): the verdict, RF-1..RF-3, and the ◆ of Exercise 49.6 answered.

*Engine 74 record closed at session 180 (2026-11-05); the chapter it serves is Vol VII Ch 49, reviewed this session — PASS WITH FINDINGS RF-1..RF-3, none of them arithmetic.*
