# SURVEY.md — everyday-chem-survey working record

Dated per-chunk entries; append, never rewrite. Pattern IDs P1..P12 refer to the book's P-index (`everyday-chem-book/PROJECT.md` §3).

## Pattern census (firings per batch; a miss is a datum)

| Pattern | B01a | B01b | Total | Note |
|---------|------|------|-------|------|
| P1 Read the label (OTC sourcing) | 3/3 | 3/3 | 6 | load-bearing everywhere, as designed |
| P2 Separation train | 0/3 | 1/3 | 1 | filter/crystallize in KClO3 route |
| P3 Metathesis-precipitation | 0/3 | 1/3 | 1 | KClO3 from NaClO3 + KCl |
| P4 Acid-base liberation | 2/3 | 1/3 | 3 | SO2 liberation; hydrazine salt liberation; acid displacement distillation |
| P5 Electricity as reagent | 0/3 | 0/3 | 0 | honest: no electrolysis video gathered yet |
| P6 Concentration ladder | 3/3 | 0/3 | 3 | boil-off HCl/H2O; H2SO4 distillation; HNO3 distillation |
| P7 Thermal decomposition | 0/3 | 0/3 | 0 | honest: not yet exercised |
| P8 Redox smelting/displacement | 0/3 | 1/3 | 1 | NaOH + Mg → Na |
| P9 Instrumentless verification | 1/3 | 0/3 | 1 | purity-by-appearance in H2SO4 distillation |
| P10 Route economics | 1/3 | 1/3 | 2 | distill-vs-buy; luminol precursor network |
| P11 Apparatus improvisation | 2/3 | 1/3 | 3 | DIY heating mantle; all-glass requirement; oil-bath stirring setup |
| P12 Yield bookkeeping | 1/3 | 0/3 | 1 | stoichiometric H2SO4:KNO3 for max yield |

## Dated chunk entries

### 2026-10-15 — Batch 01a (NurdRage acid family), sub-chunk commit A

Papers gathered (register-first, URLs + evidence in `papers/batches/batch-01a.md`):
- **N01** Make Sulfuric acid (metabisulfite/oxidizer method), NurdRage 2009-06-28. Metabisulfite + muriatic HCl liberate SO2 in situ; H2O2 (or HNO3) oxidizes it in-solution; boiling off HCl/H2O concentrates. Moves: P1, P4, P6 + **CAND-1 fired**. Feeds Ch 14, 15. Misses: P3, P5, P7, P8.
- **N02** How to Purify Sulfuric Acid by Distillation, NurdRage (circa 2015-03). Distill drain-cleaner H2SO4 (~337 °C) to reagent grade; DIY heating mantle. Moves: P1, P2, P6, P9, P10, P11. Feeds Ch 5, 14. Misses: P3, P4, P5, P7, P8, P12.
- **N03** Make Nitric Acid — The Complete Guide, NurdRage 2009-06-03. Three routes / two approaches; purest: conc. H2SO4 + pure nitrate salt, stoichiometric, all-glass distillation. Moves: P4, P6, P12, P11, P1. Feeds Ch 14, 19. Misses: P3, P5, P7, P8.

Verification levels: N01 content-verified (author Instructables mirror + archive.org date); N02 metadata-verified + corroborated; N03 content-verified via author mirror (first-two-routes split flagged for transcript fetch). Zero-firing so far: P5, P7 (single-batch datum, not a verdict).

### 2026-10-15 — Batch 01b (NurdRage: sodium, chlorate, luminol), sub-chunk commit B

Papers gathered (register-first, URLs + evidence in `papers/batches/batch-01b.md`):
- **N04** Making Sodium Metal (thermite→dioxane approach; menthol/oil refinement), NurdRage (circa 2019-02). 2Mg + 2NaOH → 2MgO + 2Na + H2 below Na's boiling point, in mineral oil with menthol catalyst; Na isolated from MgO slag by phase separation/dioxane. Corroborated: Hackaday (2019-02-26), ScienceMadness wiki "Thermochemical dioxane approach" (named for NurdRage), Chemistry StackExchange recipe. Moves: P1, P8, P11 + **CAND-3 fired**. Feeds Ch 18, 13. Misses: P3, P5, P7.
- **N05** Make Potassium Chlorate from Bleach, NurdRage (date unverified). Boil NaOCl → 3NaClO → 2NaCl + NaClO3 (heat-driven disproportionation only); KCl (salt substitute) metathesis → KClO3 crystallizes. Corroborated: author Instructables mirror, ThoughtCo (attributes video to NurdRage), Home Scientist blog (equations). Moves: P1, P2, P3 + **CAND-2 fired**. Feeds Ch 15. Misses: P5 (electrolysis variant registered as follow-up), P7, P8, P12.
- **N06** Luminol Synthesis, NurdRage (date unverified). Multi-step organic route from domestically available chemicals: own-made 3-nitrophthalic acid, hydrazine from OTC hypochlorite+ammonia+gelatin (series predecessor), condensation in glycerin (high-boiler), dithionite reduction. Corroborated: author Instructables mirror, r/OrganicChemistry (hydrazine acetate step). Moves: P1, P4, P10 (full precursor-network chaining) + **CAND-4 fired**. Feeds Ch 22, 34, 24. Misses: P3, P5, P7, P8.

**Batch 1 census (a+b):** P1 6/6 (load-bearing, as designed); P4 3/6, P6 3/6, P11 3/6; P2, P3, P8, P9, P12 each 1; P10 2; **P5, P7 zero-firing across batch 1** — honest datum: no electrolysis or calcination video gathered yet; batch 2 deliberately tests P5 (electrolysis chlorate) and P7 (thermal decomposition candidates).

**Candidate patterns opened in B01b:**
- **CAND-2 Disproportionation upgrade.** Heat-driven self-redox converts a weak OTC oxidant into a stronger one (hypochlorite → chlorate). Fired: B01b N05. Watch: hypochlorite → chlorate via electrolysis (P5 alternative) and other disproportionation cascades.
- **CAND-3 Protective medium + selective dissolution/co-distillation.** Isolate a reactive product (molten Na) below its boiling point under a liquid barrier, then separate from slag by selective solvent. Fired: B01b N04.
- **CAND-4 High-boiling solvent at atmospheric pressure.** Reach dehydration/condensation temperatures without pressure apparatus by switching to a high-boiler (glycerin, glycols). Fired: B01b N06.

## Candidate patterns (recurrence test: promote on firing across >= 2 batches)

- **CAND-1 In-situ redox generation (dissolved-gas route).** Generate a reactive gas in the pot from OTC reagents and oxidize/consume it in solution rather than handling bulk gas. Fired: B01a N01. Watch: iodine-from-iodide videos (HCl + H2O2) in batch 2.
- (CAND-2..4 opened in B01b — see the B01b entry below.)

## Follow-ups register (registered, not yet gathered)

- NurdRage "Make Nitric Acid from Sodium Bisulfate and Sodium Nitrate" (2020-08-01) — route-economics comparison, no H2SO4 needed.
- NurdRage "Make Nitric Acid without Sulfuric Acid by Oxalate Precipitation" — Ca nitrate (fertilizer) + oxalic acid; P3 route to HNO3.
- NurdRage potassium chlorate from bleach by ELECTROLYSIS (r/NurdRage thread reference) — tests P5.
- NurdRage sodium original thermite video + improved-process response video (channel attribution to verify).
- NurdRage hydrazine from bleach+ammonia+gelatin; 3-nitrophthalic acid from phthalic anhydride (luminol precursors).
