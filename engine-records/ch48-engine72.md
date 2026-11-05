# Engine 72 Record — E72-IV "the interval engine" — Session 178, Vol VII Ch 48 review (Indigo and Natural Dyes)

**Session 178 (2026-11-05), repo dsmistral/everyday-chemistry-atlas, branch main.** Engine 72 is fresh this session and shares zero code with Engines 1–71. The chapter unit is the Phase-3 adversarial review of Vol VII Chapter 48 (drafted session 177); the re-verify-never-re-author rule governed throughout — every mismatch was to be raised as a finding, never silently patched (none was: the arithmetic produced zero mismatches; the findings raised are prose-, record-, and edition-level, receipted in the chapter's Revision Appendix).

## Design

E72-IV holds every quantity as a **rigorous fixed-scale decimal interval [lo, hi]**: each bound an unreduced integer pair (n, s) meaning n/10^s, **outward-rounded at every operation** so the true value can only ever lie inside the interval — add and subtract on plain integer lanes under the **9.0e15 guard** (checked before every multiply; scales to 10^24), multiply by per-operand internal alignment (sa, sb) with products at scale sa+sb, divide by **adaptive-scale divA** (target t=9, stepping down, guard refusal). No gcd, no prime factorization, no digit-array rationals — a representation sharing nothing with Engine 71's prime-exponent vectors except the problem set. Gates: a **character-walking atom parser** (no stack, no recursion) feeding atom-multiset and mass-ledger equality; the carbonate equilibrium root by **integer bisection against the exact rational constant with guarded interval comparison** (no float enters the bracket; the pH log renders in the float witness inside the exact bracket, the same cage convention as E71); the date chains by a **fresh civil-date ordinal converter** (no date library, no reused E71 date code). The digest is **sdbm (32-bit, hex)** — distinct from E69's FNV-1a, E70's j31, and E71's joat, none reused. Iterative only; no recursion; no BigInt anywhere in the value path.

## Honest run history (all six defect classes caught before any battery row was accepted)

- **rev-0:** mul() pre-aligned BOTH operands to max scale before multiplying, inflating cross-scale products by 10^Δ — the L02 theoretical (25 g aldehyde → indigo) hit the GUARD refusal (165445114×262268000 ≈ 4.3e16) — fixed to per-operand internal alignment (sa, sb), products at scale sa+sb.
- **rev-1:** a tight(x,7) helper rescaled operands to an absolute scale and destroyed small-value operands' significant digits — caught by the L10/L15/L16 STRADDLE rows (the dye-bath equivalents, the stock-vat equivalents, the pretreatment mM); removed — plain guard-adaptive divA suffices; L03 recomposed as the direct-rational divA(mul(pt(2200,0),pt(151121,3)), mul(pt(25,0),pt(262268,3))).
- **rev-2 (row construction, not engine):** a s3b row slip pt(25,1) = 2.5 for 0.25 L on L27/L28/L31 (10× off) — caught by float-lane disagreement; fixed to pt(25,2).
- **rev-3:** the s4 gate's key-set condition (ks.length === new Set(ks).size — always false when the two sides share elements, so settled B1 printed MISMATCH) — fixed to a Set-based every-key check.
- **rev-4:** rootBracket compared the bound OBJECT .lo against 0 instead of .lo.n (always false → the bisection exhausted to the top; I05 printed pH 13.3010) — fixed to .lo.n.
- **rev-5:** the I04 formula multiplied the denominator instead of dividing (18018843.9) — the correct form gives 197.2140, matching the injection's intended wrong-answer.
- The P2 probe was invariant under the rev-0 mul fix by design (a scale-8 bracket operand).

The frozen battery below is the clean rev-final run. s0/s1/s2 were re-run under the FIXED core and verified byte-identical to the on-disk sheets (digests unchanged) — one core throughout, receipts in hand. Every sheet was executed twice, byte-identical.

## The battery (all machine-settled; transcript verbatim in ch48-engine72-transcripts.md)

```text
s0  the probe battery                 5 rows: 4 PASS + 1 seeded CAUGHT               sdbm 5f4e8467   535 B
s1  the molar book, Sheet 1          29 rows: 29 PASS 0 fail                          sdbm 1f4bb5b8  2817 B
s2  the balances, Sheet 2            9 rows:  9 PASS 0 fail (atom multiset + ledger)  sdbm 013fbd16  1578 B
s3  the charge ledger, Sheet 3       35 rows: 35 PASS 0 fail (two-lane + claims)      sdbm bd586dfa  2883 B
s4  the fresh-keyed injections        8 rows:  8 CAUGHT 0 escaped                     sdbm 12c4be8e  1073 B
sR  the register settlement          14 rows: 14 SETTLED 0 unsettled                  sdbm cba59d05  1322 B
s5  determinism                      every sheet run twice, byte-identical           (per-sheet digests equal)
whole battery (six sheets joined)    sdbm aa84c8b6 (cross-ref joat 6c427170)
```

s3 was generated as s3a (17 rows, sdbm cdeaea84) + s3b (18 rows, sdbm b74ac036) and frozen as the joined sheet (sdbm bd586dfa, 36 lines incl. the tail "s3 rows 35 pass 35 fail 0"); the split files are kept in the session scratch as intermediate receipts, superseded by the join.

**Verdict: ZERO ARITHMETIC FINDINGS.** Every frozen E71 value reproduced exactly by an engine sharing no code with it: all 29 molar rows, all 9 balances, all 35 charge-ledger rows, all 8 injections CAUGHT, all 14 settlements — and R09 byte-exact (the carbonate bracket x ∈ [0.0078583, 0.0078584] M → pH [11.8953, 11.8953]; w1 quadratic pH 11.8953), the promise chains R10–R14 at 135/54/131/110/241 days EXACT by the fresh civil-date ordinal converter (the 241-day chain N338→N366 included).

## The census and the got-strings, re-verified

The freeze-gate census re-run at a SUPERSET of session 177's sweep — 68 files (the 45 chapter masters of Chapters 3–47 plus the Field Companion's 23, vs session 177's 67): the 20 distinctive new literals → **zero hits**; the 18-value ledger sweep → **exactly the two named finds** ("7.87" the coincidental molar-mass substrings at Chapters 11/12/13/19/39; "0.5133" the Chapter 15 convergence); the dye-axis pins (262.268, 264.284, 174.096, 195.147) verified at Chapter 22 and nowhere else in the corpus (58.080/0.791/82.034 carry their multiple owners as E71 already recorded; fc7's indigo admission-gate refusal string and the "Fe 10.7911" coincidence confirmed as recorded).

The got-strings gate re-verified with a full accounting that supersedes E71's (whose count was internally inconsistent — see RF-3): **104 quoted-span instances** in the chapter's prose (frontmatter and the six text fences excluded), **90 unique strings**; **91 instances (77 unique) byte-verbatim** at the register batches; **10 punctuation-class exceptions** (every episode word verbatim; only quote-internal trailing punctuation differs — the four episode titles' trailing commas, "a nice and crispy red powder.", "a pathetic 0.9 grams.", "about 51,", "isn't the best," [the register: "isn't the best."], the kit sentence's "pre-reduced," [the register closes at "pre-reduced"], "as far as I know... has ever been proven." [the register closes at "proven"]); **2 internal non-episode quotes** ("joat," the E71 digest name; "quickly," a one-word quote whose word is register-verbatim at "quickly clear up"); and **1 no-episode-source span** ("8 months" — RF-1). Both of session 177's in-place quote-prefix fixes verify verbatim (the diazonium sentence ends "...it'll start to degrade if the temperature rises too much."; the kit quote carries the literal "..."). The direct grep -oFf pass showed pattern-competition artifacts (64 first-pass hits); the authoritative check is the single-pass awk index() sweep over all four batches — the recorded method note.

## The findings (raised, never patched; full text in the chapter's Revision Appendix)

- **RF-1 (provenance, narrowed on re-verification):** the "8 months" is register-ANNOTATION voice (batch 33cf prints "THE 8-MONTH DELIVERY CHAIN EXACT" four times, all survey gather-annotations), never episode voice (N366: "a previous video"); the EXACT belongs to the 241 days, the month rendering is a rounded conversion (≈7.9 thirty-day months); the review's interim "no register source at all" was an incomplete grep, corrected honestly. The chapter's Ex 48.5(b) already teaches the distinction.
- **RF-2 (minor):** the 10 punctuation-class spans above — no episode word differs anywhere. (The interim count of 8 was a miscount of the review's own 10-item list.)
- **RF-3 (minor, record-internal):** E71's freeze-gate paragraph says "all forty-nine quoted spans" while its per-batch counts sum to 56 and its span list was never recorded; the session-178 accounting supersedes.
- **RF-4 (the oracle catch, FIXED this session):** the session-177 web edition was not a faithful render of the master — its safety table ends at row 2 (rows 3–10 and the disposal note missing); the render's master read was cut at the same sandbox ~64-KB seam as the e760c8f2 truncated push, and because the cut precedes the Canon-Coverage heading (byte 65,762), the renderer's content-contract cut never fired. The session-177 receipt "web edition unaffected" was wrong. Machine facts: repo page 67,383 chars / 68,143 B (j31 60f0ea7c, fnv cda7f949 — both matching session 177's records; joat 95aab0c0, sdbm 1847eb7c); the faithful render of the drafted master 70,435 chars / 71,220 B, first 67,168 chars byte-identical, the divergence exactly the missing rows. Fixed by this session's re-render from the extended master (tailWord "reviewed"), pushed at this session's chapter push. Lesson recorded: never certify a render by its own digest — re-render from the full master and byte-compare.

## The web battery (oracle-first)

The repo's web/ch48-web.html fetched fresh (blob 3a19231e488a05165f758b6cdbec463e16433ada at HEAD 43ee31b0), its j31/fnv digests verified against session 177's records before any comparison; the renderer ported verbatim from the repo's own web/renderer.ts (with the session-176 tailWord adaptation), validated by the 67,168-char byte-identical prefix; the faithful-render finding (RF-4) and the fix receipted above.

## Files

- `engine-records/ch48-engine72-transcripts.md` — the six sheets verbatim, spliced from the session scratch files as they were generated (scratch is not storage: the sheets were on disk from the moment each froze).
- This record: `engine-records/ch48-engine72.md`.
- The chapter's Revision Appendix (in `manuscript/vol7/ch48.md`): the verdict, RF-1..RF-4, and the ◆ of Exercise 48.6 answered.

*Engine 72 record closed at session 178 (2026-11-05); the chapter it serves is Vol VII Ch 48, reviewed this session — PASS WITH FINDINGS RF-1..RF-4, none of them arithmetic.*
