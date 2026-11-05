# Engine 73 Record — E73-LD "the long-division rational engine" (session 179, 2026-11-05)

Vol VII Ch 49 "Photochromism and Cold" — the authoring unit's fresh engine, zero code shared with Engines 1–72.

## Design

Every quantity an exact rational held as a coprime BigInt pair [num, den], normalized by an iterative binary GCD (shift-and-subtract on the odd parts; no subtraction-only loop, no factorization, no digit arrays — nothing carried from Engine 71's prime-exponent vectors or Engine 72's interval bounds except the problem set). Comparisons by guarded cross-multiplication under a 10²⁴ overflow guard that refuses the row rather than approximates. Every printed decimal rendered digit by digit by exact long division with half-up rounding decided on the true remainder — no float in the value path, no toFixed, no epsilon. Two independent witnesses flank every row: W1, a float64 plain-formula lane typed from independent decimal constants; W2, a fixed-scale integer render witness that computes the scaled integer directly and must print the same digits. The atom parser is two-pass and table-driven: pass one validates and tokenizes, pass two accumulates a frame stack with a lookahead close that reads its trailing group multiplier — no AST, no recursion. The P18 NAME gate runs first, refusing the restricted-name list before any formula is parsed. The held element table in micro-y units: C 120110, H 10080, N 140070, O 159990, S 320600, Na 229900, Cl 354530, Mg 243050 (Chapter 3's table at ten-thousandths). Digest Adler-32 (mod 65521), 32-bit hex — distinct from E69's FNV-1a, E70's j31, E71's joat, and E72's sdbm, none reused. Dates by an integer civil-date ordinal converter (days_from_civil) — exact day counts, no float, no library.

## Honest run history (all caught before any battery row was accepted)

- rev-0: the bracket-multiplier stack read the trailing group subscript nowhere — (NH₂)₂ counted once, urea priced 44.033 instead of 60.056; both lanes agreed because W1 shares the parser. Caught by the s1 urea row's claim check at the Chapter 20 pin. Lesson: claims catch formula defects; lane agreement catches only arithmetic-type defects.
- rev-1: first fix set the multiplier after the frame merged — the close never saw it; same 44.033, caught again by the same row.
- rev-2: the lookahead close — a close peeks for its trailing multiplier — clean; the probe's P5 row is the permanent regression test.
- rev-3: the rational constructor refused decimal literals outright (BigInt throws on "0.25") — caught at the make-vs-buy row's $0.25; the same fix pass corrected three percent-scale rows and the milligram-to-gram scale.
- rev-4: the render at zero decimal places with a nonzero remainder appended a bare decimal point ("150." for 150) — caught by the injection sheet refusing it.
- rev-5: the G5 digest gate doubly broken — recorded and recomputed digests over different domains by construction, and the summary's endsWith("MATCH") admitting "MISMATCH" (a summary line that lied while its rows said otherwise) — fixed to same-domain recompute with strict equality.

## Frozen battery (transcripts byte-verbatim in ch49-engine73-transcripts.md)

- s0 the probe: 5 PASS + 1 CAUGHT (the seeded truncation fault; the P5 row is the rev-0/rev-1 regression test). adler32 04a8043c.
- s1 the molar book: 22/22 — the three new admissions (DNBP 259.221, 2-benzylpyridine 169.227, pyridine 79.102) and nineteen cross-chapter pins. T1 composition checksum 17178130 μy. adler32 ded3323c.
- s2 the balances: 10 PASS + 1 CAUGHT must-fail (NH₄NO₃ → N₂O + H₂O caught at exactly one H₂O, 18.015 g). T2 mass checksum 12546100 μy. adler32 7703688d.
- s3 the charge ledger: 26/26 — the refused yield (L01), the 652× (L02), the urea full-basis seam (L05/L06 both printed), the endotherm chain (L07–L10), the production ledger (L11–L13), the flyback (L14), the arc economics (L19–L24), the RFNA tension (L26, unadjudicated). adler32 1c638d84.
- s4 the injections: 8/8 CAUGHT, zero escaped. adler32 7d7b5d59.
- sR the register settlement: 20/20 SETTLED — the ledgers, both numeric-garble resolutions, both economics tables, S14 the RFNA tension standing, S15 the recorded tensions printed as recorded, S16–S19 the cyanotype chains 13/18/39/70 d exact, S20 the arc-to-fridge chain 1254 d. adler32 9b55006c.
- s5 determinism: s4/sR double-executed byte-identical; G5 all six sheets' recorded adler32 recompute MATCH from disk (same domain, digest line excluded). Whole battery (all six sheets as spliced): adler32 9de4accb.

**Verdict: ZERO ARITHMETIC FINDINGS.** Every register figure re-derived by an engine sharing no code with any prior engine; every claims-check settled at its stated precision; both recorded tensions (2564-vs-2571 J/g; 7.85%-vs-7.79% COP) printed as recorded, neither adjudicated; the one refused row (L01) refused for the honest reason — no theoretical in the record.

## Freeze-gate census (101-file corpus)

The 48 chapter masters (ch01/ch02 local + fc3–fc11 fetched + ch03–ch48 local), the 11 Field Companion masters, and the 42 engine records — assembled and byte-verified this session. Twenty distinctive new literals: zero hits. The cross-chapter pins re-grepped at their owners (per-literal grep -oF, no pattern competition): urea 60.056 Ch 20 ×15 (re-pinned Ch 46); AN 80.043 Ch 15; NH₃ 17.031 Ch 20 ×13; HNO₃ 63.012 Ch 15; HNO₂ 47.013 Ch 20; NO 30.006 / NO₂ 46.005 Ch 3 (Ch 20's never-generate line standing); N₂O 44.013 Ch 20 (the book's 44.013 held against the register arithmetic's 44.012 — the seam disclosed in the chapter); NaNO₃ 84.994 Ch 27; NH₄Cl 53.492 Ch 19; MgSO₄ 120.361 Ch 4; ether 74.123 Ch 21; NaOH 39.997 / Na₂CO₃ 105.988 Ch 8; Na₂SO₄ 142.036 Ch 13/14; H₂SO₄ 98.072 Ch 6; O₂/N₂ Ch 10; CO₂ 44.009 Ch 20; +25.7 kJ/mol Ch 26 ×2 (the worked cold pack); "cold pack" Ch 20 ×20; "ammonium nitrate" Ch 20 ×10; "sal ammoniac" Ch 20 ×11; epoxy Ch 35 ×26; cyanotype Ch 32 ×15 (Ch 48 ×1); nitration Ch 15 ×4; "400 nm" Ch 32 ×4 (the adjacent photon-energy face, disclosed); endotherm Ch 7/20/26/45; refrigerant Ch 20 ×2. Word-form "photochrom" prior: ch48 line 45 ×1 ("photochromics neighbor episode"), disclosed in the chapter. Coincidental substrings named: "48.6" (Ch 26's work term + Ch 48's Exercise 48.6 + this ledger's kWh), "21.3" (Ch 20's 21.312), "9375" (Ch 39's 10.509375), the four-figure generics (16.1/3.08/7.85/1.85/652), "2564" (Ch 6, fc8), "2571" (ch19 ×1), "1254" (fc9, kaolin temps).

## Got-strings ledger (machine-swept, single-pass awk index(), no pattern competition)

100 unique double-quoted spans in the drafted master; 89 verified byte-verbatim in the survey register (batch-33cg, batch-31k, batch-33ch, and the wider register where older priors live); 11 internal spans, every one named: the frontmatter fields (name, type, title), the digit-coincidence literals quoted as census data ("1254" at fc9's kaolin temperatures — a book-corpus hit, not an episode quote), the rev-4 render example "150.", the rev-5 gate literal "MISMATCH," the internal phrase "closing on itself," and the three book-corpus census words ("photochromics neighbor episode" at ch48 line 45, "sal ammoniac" and "the cold pack's salt" at ch20). Zero punctuation-class exceptions: the drafting pass moved every trailing comma and period outside the quote marks before the freeze (the session-178 RF-2 lesson applied at authoring time), and the "~$0.20/g" annotation prefix was moved out of the episode quote it had been glued to — the register's quote begins at "really is pretty bad."

## Files

- manuscript/vol7/ch49.md — the master (73,663 B / 302 lines; the seven transcript blocks spliced byte-verbatim, verified by per-block grep -F).
- engine-records/ch49-engine73.md — this record.
- engine-records/ch49-engine73-transcripts.md — the six sheets byte-verbatim plus header.
- web/ch49-web.html — rendered from the full master, chunk-read past the 64-KB cap (the session-178 RF-4 lesson: never certify a render by its own digest — re-render from the full master and byte-compare).
- canvases/everyday-chem-atlas-v7-ch49/CANVAS.md — the canvas mirror.
