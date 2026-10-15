# SURVEY.md — everyday-chem-survey working record

Dated per-chunk entries; append, never rewrite. Pattern IDs P1..P12 refer to the book's P-index (`everyday-chem-book/PROJECT.md` §3).

## Pattern census (firings per batch; a miss is a datum)

| Pattern | B01a | B01b | B02a | B02b | B03a | Total | Note |
|---------|------|------|------|------|------|-------|------|
| P1 Read the label (OTC sourcing) | 3/3 | 3/3 | 4/4 | 3/3 | 4/4 | 17 | 17/17 through batch 3a: load-bearing as designed |
| P2 Separation train | 0/3 | 1/3 | 3/4 | 3/3 | 2/4 | 9 | filter+sublime (iodine); solvent extraction (caffeine); steam distillation (limonene); crystallization everywhere |
| P3 Metathesis-precipitation | 0/3 | 1/3 | 0/4 | 0/3 | 1/4 | 2 | KClO3; NEW in B03a: oxalate HNO3 — precipitation drives ACID liberation (CAND-7) |
| P4 Acid-base liberation | 2/3 | 1/3 | 1/4 | 0/3 | 3/4 | 7 | hydrazine sulfate precipitation; HI displacement (N17) |
| P5 Electricity as reagent | 0/3 | 0/3 | 2/4 | 0/3 | 1/4 | 3 | CuSO4 electrochemical method; KClO3 cell; electrochemical H2SO4 (N15) |
| P6 Concentration ladder | 3/3 | 0/3 | 0/4 | 0/3 | 0/4 | 3 | all from B01a acid family |
| P7 Thermal decomposition | 0/3 | 0/3 | 0/4 | 0/3 | 0/4 | 0 | STILL 0/17 after batch 3a — batch 3b hunts calcination NOW |
| P8 Redox smelting/displacement | 0/3 | 1/3 | 0/4 | 0/3 | 0/4 | 1 | |
| P9 Instrumentless verification | 1/3 | 0/3 | 0/4 | 0/3 | 1/4 | 2 | under-counted generally; new face: observable process control (N15 cathode-H2 watch) |
| P10 Route economics | 1/3 | 1/3 | 3/4 | 2/3 | 4/4 | 11 | CuSO4 3-way exemplar; NEW: N09+N15 reversible cycle; urea-vs-ketazine hydrazine comparison |
| P11 Apparatus improvisation | 2/3 | 1/3 | 1/4 | 1/3 | 0/4 | 5 | chlorate cell; simple steam-distillation setup |
| P12 Yield bookkeeping | 1/3 | 0/3 | 0/4 | 0/3 | 0/4 | 1 | hunt MISSED in 3a (only wiki ~50% hydrazine-yield context); stays open |
| P13 In-situ redox generation | 1/3 | 0/3 | 1/4 | 0/3 | 1/4 | 3 | promoted from CAND-1 (REC-1); firings N01, N08, N17; third face in N17: generated-unstable-acid (HI displaced and oxidized in the same pot) |

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

### 2026-10-16 — Batch 02a (NurdRage: hydrazine, iodine, copper sulfate, electrolytic chlorate), sub-chunk commit

Papers gathered (register-first, URLs + evidence in `papers/batches/batch-02a.md`):
- **N07** Make Hydrazine Sulfate by the Hypochlorite-Ketazine Process, NurdRage (date unverified). Ammonia + MEK + bleach → hydrazine protected as ketazine during oxidation, then hydrolyzed + acidified to hydrazine sulfate. Moves: P1, P4, P10 + **CAND-5 fired** (protective-intermediate staging). Feeds Ch 19, 22. Misses: P3, P5, P7, P8.
- **N08** Make Iodine from an Alkali Metal Iodide, Hydrochloric Acid and Hydrogen Peroxide, NurdRage 2009-04-02. KI/NaI + HCl + 5 vol 3% H2O2 → I2 filtered, purified by sublimation/crystallization. Moves: P1, P2 + **CAND-1 fired in generalized form** (in-solution redox generation of the element). Feeds Ch 17. Misses: P3, P5, P7, P8.
- **N09** Make Copper Sulfate from Copper and Sulfuric Acid (3 Ways), NurdRage. Cu + H2SO4 needs an oxidant: H2O2 method, HNO3 method (NO2 hazard), electrochemical method (DC supply, Cu anode); electricity cheapest per gram. Moves: P1, P2, P5, P10 (the 3-way route-economics exemplar). Feeds Ch 18, 11. Misses: P3, P7.
- **N10** Make Potassium Chlorate by Electrolysis — The Basic Guide, NurdRage. Saturated KCl cell, carbon/Pt/MMO anode → KClO3 crystallized. Moves: P5, P1, P11, P2, P10. Feeds Ch 15, 11. Misses: P3, P7, P8. Note: r/NurdRage community corroboration shows NurdRage advising selective ethanol extraction of chlorate — a CAND-3-family selective-dissolution move (watch).

**Sub-chunk census:** P1 4/4, P2 3/4, P5 2/4, P10 3/4, P11 1/4, P4 1/4. P5 now exercised; P7 still zero.

### 2026-10-16 — Batch 02b (NileRed first entries: extraction focus), sub-chunk commit

Papers gathered (register-first, URLs + evidence in `papers/batches/batch-02b.md`):
- **N11** Extracting Caffeine from Coffee — NileRed (circa 2016-12). Solvent extraction of caffeine from Folgers coffee; community route economics: tea easier to purify than coffee. Moves: P1, P2, P10. Feeds Ch 31, 5. Verification: metadata-verified (official channel video confirmed via Perfect Daily Grind + Chegg lab reference + official Facebook video); YouTube URL to pin at next pass (honest gap).
- **N12** Turning Plastic Gloves Into Hot Sauce — NileRed (2022-02-26). Artificial hot sauce from nitrile gloves + vanilla-derived ingredients; the genre's theatrical OTC-sourcing exemplar. Moves: P1, P10. Feeds Ch 32, 34 (motivation exemplar). Verification: metadata-verified (X post + reactor video credit + subreddit); chemistry details flagged for transcript-level fetch.
- **N13** How to Extract Limonene from Orange Peels — NileRed (2015). Steam distillation: peel oil co-distills with water vapor below 100 °C; immiscible oil separates. Moves: P1, P2, P11 + **CAND-6 fired** (carrier/steam distillation). Feeds Ch 5, 31. Corroborated by RSC class experiment (parallel procedure).

**Batch 2 census (a+b):** P1 7/7 (cumulative 13/13); P2 6/7; P10 5/7; P5 2/7; P7 remains 0/13 papers — batch 3 must include a calcination/thermal-decomposition source; P12 weak (1 firing) — prioritize a yield-focused source.

**Correction (2026-10-16, dated):** the batch-02b.md census line says "P7 zero across 14 papers" — the correct count is 13 papers (6 in batch 1 + 7 in batch 2). The committed batch file stays as-is (extend, never rewrite); this correction is authoritative.

**Promotion recommendation (pending user approval):** **REC-1: promote CAND-1 to the book P-index as P13 "In-situ redox generation"** (generalized: generate the reactive species in the pot from OTC reagents and oxidize/consume it in solution, never handling bulk material). Faces: dissolved-gas route (SO2 → H2SO4, N01) and dissolved-ion route (iodide → I2, N08). Fired across B01a + B02a (recurrence test passed).

### 2026-10-16 — Batch 03a (NurdRage round 3), sub-chunk commit

Papers gathered (register-first, URLs + evidence in `papers/batches/batch-03a.md`):
- **N14** Making Hydrazine Sulfate from Urea and Bleach, NurdRage (upload date unverified). Urea + hypochlorite under cold alkaline conditions with a gelatin viscolizer; H2SO4 precipitates the storable hydrazine sulfate. Corroborated: ScienceMadness Wiki + OrgSyn parallel. Moves: P1, P2, P4, P10. **CAND-5 honest miss** — the urea route needs no protective intermediate (route-specific-cost datum for Ch 19/22). Feeds Ch 19, 22, 34. Verification: content-verified.
- **N15** Make Sulfuric Acid (Copper Sulfate Electrochemical Method), NurdRage 2009-12-25. Inert-anode electrolysis of CuSO4: Cu plates out, H2SO4 builds in solution; current adjusted to minimize cathode H2; REVERSE of N09 — together a closed Cu/CuSO4/H2SO4 cycle. Moves: P1, P5, P9 (process-control face), P10. Feeds Ch 11, 14, 18, 34. Verification: content-verified (author mirror + WonderHowTo).
- **N16** Make Nitric Acid without Sulfuric Acid by Oxalate Precipitation, NurdRage 2024-07-13. 300 g calcium ammonium nitrate (fertilizer) + oxalic acid: Ca oxalate precipitates, leaving HNO3 in solution — an acid made by precipitation, no distillation, no H2SO4. Moves: P1, P2, P3, P4, P10 + **CAND-7 FIRED** (precipitation-driven acid liberation — the P3/P4 intersection). Community extension: the same trick on sulphates for H2SO4 (ScienceMadness thread — CAND-7 watch item). Feeds Ch 14, 8, 19, 34. Verification: content-verified (Patreon post date + two community corroborations).
- **N17** Make Iodine from Sulfuric acid and Alkali Metal Iodide, NurdRage 2009-03-28. Conc. H2SO4 displaces HI from KI/NaI and oxidizes it in the same pot; ice bath suppresses the H2S side pathway. Moves: P1, P4, P13 (third face: generated-unstable-acid, never isolated), P10 (one-reagent-two-roles vs N08). Kinetics datum for Ch 24: cold/hot as a pathway switch. Feeds Ch 17, 14, 24. Verification: content-verified (author mirror + WonderHowTo).

**Sub-chunk census:** P1 4/4 (17/17), P10 4/4 (11/17), P4 3/4 (7/17), P2 2/4 (9/17), P3 1/4 (2/17), P5 1/4 (3/17), P9 1/4 (2/17), P13 1/4 (3 firings). P7 still 0/17 (3b hunts it now); P12 0/4 (hunt continues).

## Candidate patterns (recurrence test: promote on firing across >= 2 batches)

- **CAND-1 In-situ redox generation.** Generate the reactive species in the pot from OTC reagents and oxidize/consume it in solution, never handling bulk material. Fired: B01a N01 (dissolved-gas: SO2 → H2SO4), B02a N08 (dissolved-ion: iodide → I2). **PROMOTED: user approved REC-1 on 2026-10-16 → book P13.**
- **CAND-2 Disproportionation upgrade.** Heat-driven self-redex converts a weak OTC oxidant into a stronger one (hypochlorite → chlorate). Fired: B01b N05. Watch: further cascades (chlorate → perchlorate references).
- **CAND-3 Protective medium + selective dissolution.** Isolate a reactive product under a liquid barrier, then separate from slag by selective solvent. Fired: B01b N04. Watch: r/NurdRage ethanol-extraction-of-chlorate advice (community corroboration, not yet a registered paper).
- **CAND-4 High-boiling solvent at atmospheric pressure.** Fired: B01b N06. Watch: Ch 22 sources (soap/ester syntheses).
- **CAND-5 Protective-intermediate staging.** Temporarily mask a reactive species as a stable intermediate to survive harsh reaction conditions, then unmask it. Fired: B02a N07 (hydrazine as ketazine during hypochlorite oxidation). Honest miss: B03a N14 — the urea route needs NO protective intermediate; protection is a route-specific cost (route-economics datum for Ch 19/22).
- **CAND-6 Carrier (steam) distillation.** Co-distill a high-boiling immiscible liquid with water at ~100 °C to isolate it without pressure/vacuum gear. Fired: B02b N13. Watch: other essential-oil/Ch 31 sources.
- **CAND-7 Precipitation-driven acid liberation.** Make a strong acid from its OTC salt by metathesis with an acid whose metal-salt byproduct is INSOLUBLE — the precipitation pulls the proton transfer, leaving the free acid in solution; filter off the precipitate. The P3/P4 intersection: acid without distillation or a stronger-acid precursor. Fired: B03a N16 (calcium ammonium nitrate + oxalic acid -> HNO3). Watch: sulphates + oxalic acid for H2SO4 (ScienceMadness thread https://www.sciencemadness.org/whisper/viewthread.php?tid=160390).

## Follow-ups register (registered, not yet gathered)

- NurdRage "Make Nitric Acid from Sodium Bisulfate and Sodium Nitrate" (2020-08-01, https://www.youtube.com/watch?v=CqzrTxshOXM) — route-economics comparison, no H2SO4 needed.
- NurdRage "Make Nitric Acid without Sulfuric Acid by Oxalate Precipitation" (https://www.youtube.com/watch?v=1x8oXCBjHFY) — GATHERED: N16 (batch 3a); CAND-7 fired.
- NurdRage "Making Hydrazine Sulfate from Urea and Bleach" (https://www.youtube.com/watch?v=PCovDr4FVNQ) — GATHERED: N14 (batch 3a); CAND-5 honest miss recorded.
- NurdRage "Make Iodine from Sulfuric acid and Alkali Metal Iodide" (2009-03-28, https://www.youtube.com/watch?v=2F_kPXbi2D8) — GATHERED: N17 (batch 3a); P13 third face.
- NurdRage "make sulfuric acid electrochemically" (copper sulfate electrochemical method, WonderHowTo reference) — network chaining: CuSO4 → H2SO4 regeneration.
- NurdRage sodium original thermite video + improved-process response video (channel attribution to verify).
- NurdRage "Making 3-Nitrophthalic Acid" (https://www.youtube.com/watch?v=ridu6XIDb4I, attribution to verify) — luminol precursor, first-class paper.
- Pin YouTube URL for NileRed caffeine-from-coffee video (N11); transcript-level fetch for N12 (gloves→hot sauce chemistry).
- **P7 hunt (zero firings after 17 papers):** batch 3b gathers NOW — Primitive Technology lime cycle (verified) + SkillCult secondary + baking-soda calcination (ThoughtCo/Scientific American). Cody's Lab lime video did not surface in fresh searches; optional corroboration at a later pass.
- NurdRage "Azeotropic and Fuming Nitric Acid Concentration and Purification" (Patreon, https://www.patreon.com/NurdRage/posts/azeotropic-and-43344027) — P6 face + likely concentration/yield numbers: a P12-hunt target.
- ScienceMadness thread "making sulphuric acid from sulphates and oxalic acid" (https://www.sciencemadness.org/whisper/viewthread.php?tid=160390) — possible CAND-7 second face (H2SO4); gather as a paper if it holds up.
- NileRed hydrazine-from-urea video (https://www.youtube.com/watch?v=0yvbJ8tE2y8) — urea-route variant by the second priority channel (noted in ScienceMadness Wiki); gather at the next NileRed pass.
- **P12 hunt:** register a yield-focused source (gold-refining-forum-style stoichiometry threads or a NurdRage "revisited" video with yield numbers).
