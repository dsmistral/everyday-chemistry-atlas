# SURVEY.md — everyday-chem-survey working record

Dated per-chunk entries; append, never rewrite. Pattern IDs P1..P12 refer to the book's P-index (`everyday-chem-book/PROJECT.md` §3).

## Pattern census (firings per batch; a miss is a datum)

| Pattern | B01a | B01b | B02a | B02b | B03a | B03b | B04a | B04b | Total | Note |
|---------|------|------|------|------|------|------|------|------|-------|------|
| P1 Read the label (OTC sourcing) | 3/3 | 3/3 | 4/4 | 3/3 | 4/4 | 2/2 | 1/3 | 22 | 19/19 video corpus; +Thompson (BUY branch) in B04a — OpenStax will be the only non-firing source |
| P2 Separation train | 0/3 | 1/3 | 3/4 | 3/3 | 2/4 | 0/2 | 3/3 | 2/3 | 14 | separation is both curriculum (Thompson) and practice (distillation/filtration in most routes) |
| P3 Metathesis-precipitation | 0/3 | 1/3 | 0/4 | 0/3 | 1/4 | 0/2 | 0/3 | 1/3 | 3 | rare in the video corpus (2/19); carried by book canon (Dunn metathesis project) + the oxalate acid firing — honest split: field-light, curriculum-heavy |
| P4 Acid-base liberation | 2/3 | 1/3 | 1/4 | 0/3 | 3/4 | 0/2 | 0/3 | 2/3 | 9 | Dunn acid project; Golden Book gas/salt making |
| P5 Electricity as reagent | 0/3 | 0/3 | 2/4 | 0/3 | 1/4 | 0/2 | 1/3 | 1/3 | 5 | CuSO4 electrochemical; KClO3 cell; electrochemical H2SO4; Thompson electrolysis; Dunn batteries/electrochemicals |
| P6 Concentration ladder | 3/3 | 0/3 | 0/4 | 0/3 | 0/4 | 0/2 | 1/3 | 1/3 | 5 | B04a exemplar: azeotropic HNO3 (dilute -> 68% -> fuming); Dunn alcohol distillation |
| P7 Thermal decomposition | 0/3 | 0/3 | 0/4 | 0/3 | 0/4 | 2/2 | 1/3 | 1/3 | 4 | lime cycle (N18) + baking soda (N19) + copper nitrate -> HNO3 (N21) + Dunn lime project (N23) |
| P8 Redox smelting/displacement | 0/3 | 1/3 | 0/4 | 0/3 | 0/4 | 0/2 | 1/3 | 2/3 | 4 | sodium thermite; Thompson copper smelting; Dunn metals; Golden Book metals |
| P9 Instrumentless verification | 1/3 | 0/3 | 0/4 | 0/3 | 1/4 | 2/2 | 1/3 | 1/3 | 6 | faces: process control (N15), end-use (N18), mass loss (N19), flame/protein/sugar tests (N24), qual/quant curriculum (N20) |
| P10 Route economics | 1/3 | 1/3 | 3/4 | 2/3 | 4/4 | 0/2 | 3/3 | 1/3 | 15 | exemplars: CuSO4 3-way; N09+N15 cycle; urea-vs-ketazine; Leblanc-vs-Solvay (Dunn); recycling (N21) |
| P11 Apparatus improvisation | 2/3 | 1/3 | 1/4 | 1/3 | 0/4 | 2/2 | 0/3 | 2/3 | 9 | improvised kilns; oven as furnace; Dunn whole book; Golden Book apparatus-making; contrast: Thompson uses purchased gear |
| P12 Yield bookkeeping | 1/3 | 0/3 | 0/4 | 0/3 | 0/4 | 0/2 | 1/3 | 1/3 | 3 | HUNT RESOLVED: N21 states its own 60-80% yield (transcript-level); Dunn stoichiometry project carries book-canon bookkeeping |
| P13 In-situ redox generation | 1/3 | 0/3 | 1/4 | 0/3 | 1/4 | 0/2 | 0/3 | 0/3 | 3 | promoted REC-1; three faces: dissolved-gas, dissolved-ion, generated-unstable-acid |

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

### 2026-10-16 — Batch 03b (P7 hunt: calcination), sub-chunk commit

Papers gathered (register-first, URLs + evidence in `papers/batches/batch-03b.md`):
- **N18** Lime — Primitive Technology 2018-03-06 (official video https://www.youtube.com/watch?v=Ek3aeUhHaFY pinned from the author's blog); secondary: SkillCult 2016-01-22 (video attribution RESOLVED this session: SkillCult blog + Instructables + video are one "The Pet" kiln project). Shells/limestone calcined above ~840 C -> CaO; slaked to putty; re-carbonation hardens mortar — the FULL lime cycle, plus the dead-lime over-burn failure datum. Moves: P1 (nature face), **P7 archetype** (calcination + the reversible cycle), P11 (improvised kilns), P9 (end-use verification). Feeds Ch 6, 10, 13, 28, 24. Verification: content-verified.
- **N19** Sodium carbonate from baking soda (kitchen-scale P7) — ThoughtCo + Scientific American "Vanishing Baking Soda" (https://www.scientificamerican.com/article/vanishing-baking-soda/). NaHCO3 -> Na2CO3 + CO2 + H2O in a kitchen oven; two temperature programs (low-and-slow ~1 h vs 400 F/15 min) land on the same product; before/after mass loss = the verification. Moves: P1, **P7 kitchen face**, P11 (oven as furnace), P9 (mass-loss face, single-source — flag). No verified-attribution YouTube video for this procedure: web sources registered instead (honest gap). Feeds Ch 13, 6, 12, 10. Verification: content-verified (two-source convergent).

**Batch 3 census (a+b, 6 papers):** P1 6/6 (19/19); **P7 2/6 — FIRES at last** (2/19; archetype N18, kitchen face N19); P10 4/6 (11/19); P4 3/6 (7/19); P9 3/6 (4/19); P2 2/6 (9/19); P5 1/6 (3/19); P3 1/6 (2/19 — CAND-7); P11 2/6 (7/19); P13 1/6 (3 firings, three faces); P6 3/19, P8 1/19; **P12 0/6 — hunt missed again; stays open** into the book-canon batches with sharper targets.

### 2026-10-15 — Batch 04a (book canon I: Thompson audit + P12 hunt), sub-chunk commit

Clock note: sandbox clock reads 2026-10-15 UTC; session-log chronology follows session numbers (see PROJECT.md row 5). Papers gathered (register-first, URLs + evidence in `papers/batches/batch-04a.md`):
- **N20** Thompson, *Illustrated Guide to Home Chemistry Experiments* (O'Reilly 2008, ISBN 9780596514921) — the modern home-lab technique curriculum: 17 hands-on chapters verified from the publisher TOC. Moves: P1 (BUY-branch sourcing), P2, P5 (electrolytic H2/O2), P8 (copper smelting from self-made ore), P9 (qual/quant analysis curriculum), P10. Canon audit table written: anchors our Vol I Ch 1-12 nearly one-to-one; Vol II reagent network beyond his coverage (his model is BUY, ours MAKE) — the Atlas's differentiator. FINDING-A: his Forensic Chemistry chapter is beyond our map (optional Ch 12 section, user gate). Feeds Ch 1-12, 30. Verification: content-verified.
- **N21** NurdRage "Make Nitric Acid by Thermal Decomposition of Copper Nitrate" (circa 2020-11) — recycle copper nitrate waste to nitric acid by thermal decomposition (exploits residual hydration; basic copper nitrate + HNO3 form directly, then NO2 absorption). Moves: **P7 (third firing — first in the video corpus)**, **P12 — HUNT RESOLVED: the source states its own yield (60-80%, transcript-level, flagged)**, P10 (acid AND copper recovered), P2. Feeds Ch 14, 19, 34, 6. Verification: content-verified (YouTube + filmot transcript + reddit thread).
- **N22** NurdRage "Nitric Acid Concentration and Purification (Azeotropic and Fuming)" — dilute HNO3 -> ~68% azeotrope by fractional distillation -> fuming via drying agents. Moves: **P6 archetype**, P2, P10 (concentrate-vs-make). Feeds Ch 14, 5, 19. Verification: metadata + description-level (procedure from the video description; transcript fetch flagged).

**Sub-chunk census:** P10 3/3 (14/25), P2 3/3 (14/25), P6 1/3 (4/25), P7 1/3 (3/25), P12 1/3 (2/25), P1 1/3 (22/25), P5 1/3 (4/25), P8 1/3 (2/25), P9 1/3 (5/25). P3, P4, P11, P13 zero (P11 miss is a canon contrast datum: Thompson uses proper purchased gear).

**Correction (2026-10-15, dated):** the batch-04a intermediate census (the committed batch-04a.md census line and the B04a-only table state) mis-stated two running totals: P1 was written as 22 at 22 papers (correct intermediate: 20/22) and P2 as 14 (correct: 12/22). The committed batch file stays as-is (extend, never rewrite); the consolidated B04b table above is authoritative: P1 22/25, P2 14/25.

### 2026-10-15 — Batch 04b (book canon II: Dunn + Golden Book + OpenStax), sub-chunk commit

Papers gathered (register-first, URLs + evidence in `papers/batches/batch-04b.md`):
- **N23** Dunn, *Caveman Chemistry* (2003, ISBN 1-58112-566-6) — metadata re-verified (canon-register flag RESOLVED); complete 28-project list verified from the author's site + two mirrors. The book is our P-index in book form: make everything from nature with improvised apparatus. Moves: P1 (nature face), P2, P3 (Adam metathesis), P4, P5 (Volta/Dow), P6 (alcohol distillation), P7 (Vitruvius lime — book-canon corroboration of N18), P8 (Vulcan metals), P10 (**Leblanc vs Solvay — the historical route-economics exemplar**), P11, P12 (al-Razi stoichiometry). FINDING-B1: Dunn Ch 17 (Gunpowder) — energetics binding line applies: history/hazard context to Ch 27 only, no procedures. Feeds Ch 13, 18-22, 28-33. Verification: content-verified.
- **N24** Brent, *The Golden Book of Chemistry Experiments* (1960, Western Publishing) — contents-page + topic list verified from scans/mirrors; benchmark-only per charter. Moves: P1, P2, P4, P8 (metals), P9 (flame test + protein/sugar tests), P11 ("Making Apparatus for Experiments"). Feeds Ch 1-3, 7-12, 18, 20-22, 29-33 (ambition model + density benchmark). Verification: content-verified (per-chapter page TOC to pin at next pass).
- **N25** OpenStax *Chemistry 2e* (2019, CC BY-NC-SA) — the theory canon; 21 chapters verified. Honest zero-firing datum: theory canon, not field practice — its role is the theory-coverage check. **FINDING-B2:** nuclear chemistry (OpenStax ch 21) absent from our 34-chapter map -> propose a Ch 27 hazard/detection section or explicit exclusion (user gate). **FINDING-C:** atomic structure/electronic structure/bonding (OpenStax ch 2, 6-8) have no dedicated home chapter -> propose weaving into Ch 2/3/7 or one new Vol I chapter (user gate).

**Session-5 census (batch 4a+b: N20-N25; corpus now 25 papers):** P1 22/25 (OpenStax the only miss, by design), P10 15/25, P2 14/25, P4 9/25, P11 9/25, P9 6/25, P5 5/25, P6 5/25, P7 4/25, P8 4/25, P13 3/25 (three faces), P12 3/25 (HUNT RESOLVED), P3 3/25 (field-light, curriculum-heavy — honest split). First ANALYSIS.md synthesis written this session (papers/ANALYSIS.md).

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
- **P7 hunt: RESOLVED in batch 3b** — N18 (Primitive Technology lime cycle + SkillCult) + N19 (baking-soda calcination) both fire P7. Cody's Lab lime video did not surface in fresh searches; optional corroboration at a later pass.
- NurdRage "Azeotropic and Fuming Nitric Acid Concentration and Purification" (https://www.youtube.com/watch?v=88gbfCnrV8o) — GATHERED: N22 (batch 4a); P6 archetype.
- NurdRage "Efficiently Recover Nitric Acid and Copper Metal From Copper Nitrate Wastes" (https://www.youtube.com/watch?v=l8uQWibpRYk, X post 2020-11-22) — sibling video of N21; gather at next NurdRage pass.
- ScienceMadness thread "making sulphuric acid from sulphates and oxalic acid" (https://www.sciencemadness.org/whisper/viewthread.php?tid=160390) — possible CAND-7 second face (H2SO4); gather as a paper if it holds up.
- NileRed hydrazine-from-urea video (https://www.youtube.com/watch?v=0yvbJ8tE2y8) — urea-route variant by the second priority channel (noted in ScienceMadness Wiki); gather at the next NileRed pass.
- **P12 hunt: RESOLVED in batch 4a** — N21 states its own yield (60-80%); Dunn's Stoichiometry project (N23, batch 4b) adds book-canon yield bookkeeping.
