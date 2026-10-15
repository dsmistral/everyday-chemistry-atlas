# PROJECT.md — The Everyday-Chemistry Atlas (working record)

Working title: *The Everyday Chemist's Atlas: Rebuilding the Reagent World from Household Materials*.
Pipeline: `science-book-builder` skill. This file is the working master; the Knowledge topic is the working memory, the backup repo the byte-identical mirror. Extend, never rewrite.

## 1. Premise and scope decisions (user-set, 2026-10-15)

- **Premise ("the post-apocalyptic chemist")**: the reader has full access to advanced chemistry knowledge (books/PDFs) and the ordinary materials of the world around them, but NO advanced instruments and NO ready-made specialty chemicals. The book teaches chemistry step by step through experiments on everyday materials and materials synthesized from those; specialty chemicals are bought only when synthesis is genuinely impractical — and then only items of regular, unrestricted retail availability.
- **Audience**: intelligent adult autodidact (advanced-book reader without advanced lab). Not a kids' book.
- **Theory**: FULL track — equilibrium, thermodynamics, kinetics woven throughout, not appendices.
- **Hazard ceiling**: full home-lab (flammables, stronger acids) permitted WITH strict safety protocols; every experiment carries a hazard assessment. Deliberate exclusion (Phase 1, resolved): no step-by-step SYNTHESIS procedures for explosive/energetic materials — but energetic- and toxic-hazard KNOWLEDGE (recognition, avoidance, quenching, neutralization, incident response) is in scope and gets its own chapter (Vol III Ch 27). Everything else is standard educational home chemistry.
- **Size**: comprehensive atlas, many volumes, full reagent-synthesis network (the "tech tree" of chemicals is a first-class artifact of the book).
- **Charter**: the book is a distillation and assimilation of the existing everyday-chemistry literature (books, papers, YouTube channels, forums), unified by one voice, one theory track, one verified reagent network.

### Durable decisions log (dated; append, never rewrite)

- 2026-10-15, this paragraph the durable record: **Phase 1 gate outcome.** User approved the multi-volume atlas scope WITH adjustments to be specified (pending at session-1 close; authoring remains gated on receiving them). Sequencing decided: survey gather batches run BEFORE any chapter authoring (survey-first). User will create the private repo `everyday-chemistry-atlas` under `dsmistral` and install the Vibe GitHub app; the record/mirror push resumes as soon as the repo is detected.
- 2026-10-15, this paragraph the durable record: **Phase 1 gate PASSED.** User confirmed "none — proceed as mapped": the 5-volume / 34-chapter scope, canon, and exclusions stand as recorded, with no adjustments. Authoring is unblocked; survey-first sequencing governs (survey gather batches begin before any chapter authoring).
- 2026-10-15, this paragraph the durable record: **Energetics resolution.** User requested maximal energetic-materials knowledge, on the grounds that "not knowing is not a good defence" — recognition and handling knowledge for defensive purposes. Binding resolution: the book gains a dedicated hazard-recognition chapter (Vol III Ch 27: energetic & toxic hazards one may encounter or accidentally create — dangerous household combinations, oxidizer/organic incompatibilities, contaminated-consumer-product hazards — with recognition, avoidance, quenching, neutralization, and incident response) plus hazard notes woven through the oxidizer chapters (15, 17). Step-by-step synthesis procedures for explosive/energetic materials remain excluded from the manuscript; this line is binding on all sessions.

## 2. Canon Register (audit references + survey corpus)

**Audit canon (fixed 4):**
1. Robert Bruce Thompson, *Illustrated Guide to Home Chemistry Experiments: All Lab, No Lecture*, O'Reilly, 2008. — lab technique curriculum + OTC chemical sourcing. (Verified: O'Reilly catalog, Goodreads, archive.org entry.)
2. Kevin M. Dunn, *Caveman Chemistry*, Universal Publishers, 2003. — projects from raw materials (lime, soap, glass, metals, dyes); process-driven. (Metadata to re-verify at first survey batch.)
3. *The Golden Book of Chemistry Experiments*, 1960. — the classic model of ambitious home experimentation; historical benchmark. (Public-domain scans circulate; use as coverage benchmark only.)
4. OpenStax *Chemistry 2e* (free, open license) — the general-chemistry theory canon that the full theory track must cover. (Plus any standard text the user prefers.)

**Survey corpus (sibling project; to be gathered register-first with fresh verification, never from memory):**
- YouTube: NurdRage (amateur-accessible synthesis from OTC precursors — highest survey priority), NileRed/NileBlue, Cody's Lab, Extractions&Ire, Chemical Force, Explosions&Fire, Doug's Lab, Periodic Videos (theory support).
- Print/web: Thompson's Make: "Setting Up a Home Science Lab" series (OTC chemicals on the cheap), Texium "Essential Chemicals for the Organic Lab" (amateur-lab stocking philosophy), ScienceMadness forum threads, Golden Book, *Caveman Chemistry*, pre-1950 home-chem books (*The Boy Chemist*, *Chemical Magic*), Wikipedia/primary lit for reaction verification.
- Survey record: separate sibling Knowledge topic `everyday-chem-survey` + `papers/` corpus in the backup repo (CORPUS.md, STATE.md, README.md, patterns/, ANALYSIS.md) per `survey-track.md`. Survey feeds the book; adoption decisions are user-approved; the survey never edits the manuscript.

## 3. Master Pattern Index (P-index) — initial mining, v0

Load-bearing moves of everyday-chemistry problem-solving. Tag all methods with P-IDs; ◆ exercises diagnose against this index. Prune/promote at chapter reviews; survey batches add usage evidence.

- **P1: Read the label (OTC sourcing).** Shape: need a chemical, have a store. Move: identify consumer products whose active ingredient IS the needed chemical at useful purity/assay (vinegar→acetic acid; baking soda→NaHCO3; drain cleaner→NaOH/H2SO4; battery acid→~35% H2SO4; muriatic acid→HCl; bleach→NaOCl; peroxide→H2O2). When to use: always, before synthesizing. Fails: low assay, additives/surfactants, regional availability. Chapters: 2, all of Vol II.
- **P2: Separation train.** Shape: wanted substance locked in a mixture. Move: choose the cheapest separation that exploits the largest physical-property difference (settle/decant → filter → evaporate → crystallize/recrystallize → distill). Chapters: 4–6, everywhere.
- **P3: Metathesis-precipitation route.** Shape: want salt MX, have two soluble OTC salts. Move: pick reactants whose byproduct is insoluble (solubility rules) so the target separates itself: AX + MY → MX(aq) + AY↓. Chapters: 8, all Vol II metal salts.
- **P4: Acid–base liberation.** Shape: want a gas or free acid/base. Move: carbonate + acid → CO2↑; ammonium salt + base → NH3↑; acid + volatile acid salt → HCl↑. Chapters: 7, 9, 14, 19.
- **P5: Electricity as reagent.** Shape: need an oxidation/reduction no OTC reagent performs cheaply. Move: electrolysis with chosen electrodes (chlorate from brine; NaOH/H2/Cl2 from salt; metal deposition; CuCl2 cycle). Chapters: 11, 15, 18.
- **P6: Concentration ladder.** Shape: reagent available only dilute. Move: upgrade in steps chosen by stability (boil battery acid → ~70%; distill with a drying agent → concentrated; fractional freeze; azeotrope-breaking). Chapters: 5, 14, 20.
- **P7: Thermal decomposition.** Shape: want an oxide/carbonate/element; have a salt or mineral. Move: calcine/pyrolyze (NaHCO3→Na2CO3→Na2O; CaCO3→CaO; CuCO3/Cu(OH)2→CuO). Chapters: 6, 10, 13.
- **P8: Redox smelting/displacement.** Shape: want a metal. Move: reduce the oxide/ore with carbon or displace with a more active metal (thermite-class reductions only at demonstration scale under the safety charter). Chapters: 10, 18.
- **P9: Instrumentless verification.** Shape: is this the stuff I think it is? No spectrometer. Move: convergence of cheap orthogonal evidence — flame color, pH, precipitation behavior, melting point, density, characteristic reaction. Chapters: 12, everywhere as "verify before use".
- **P10: Route economics.** Shape: several syntheses reach the target. Move: score routes by (a) starting-material availability, (b) apparatus demand, (c) hazard, (d) yield & separability; prefer routes that produce easy-to-separate byproducts. This is the network's edge-cost function. Chapters: Reagent Network chapters (Vol II–V).
- **P11: Apparatus improvisation.** Shape: no proper glassware. Move: rebuild the instrument from kitchenware (double-boiler as water bath; kettle+tube still; steel-can furnace; syringe gas collector) with a stated accuracy penalty. Chapters: 1, 5, 11, 12.
- **P12: Yield bookkeeping.** Shape: did the synthesis work? Move: theoretical vs. actual yield, loss ledger per step (transfer → separation → purification), cumulative route yield across the network. Chapters: 3, 8, network appendix.

## 4. Chapter Map (draft, master plan) — one chapter = one session

Status key: `planned` → `in-progress` → `drafted` → `reviewed` → `published`.

**Vol I — Foundations of the Home Lab**
1. The Lab in a Ruined World — safety charter, kitchen glassware, heat sources, the notebook — `planned`
2. Reading the World as a Chemical Inventory — labels, grades, the OTC map — `planned`
3. Water and Solutions — concentration, molarity, solubility — `planned`
4. Separation Train I: Mechanical and Evaporative — filter, decant, evaporate, crystallize — `planned`
5. Separation Train II: Distillation — build a still; vapor pressure, mixtures, azeotropes — `planned`
6. Heat, Fire, and Fuels — combustion, thermochemistry, calorimetry — `planned`
7. The Household pH World — acids and bases; Arrhenius→Brønsted, equilibrium — `planned`
8. Salts and the Precipitation Network — metathesis, Ksp, solubility rules — `planned`
9. Gases — generation, collection, recognition; gas laws — `planned`
10. Redox and Metals — activity series, displacement, corrosion — `planned`
11. Electrochemistry — electrolysis, cells, Nernst — `planned`
12. Analysis Without Instruments — the wet qualitative scheme — `planned`

**Vol II — The Reagent Network (core synthesis atlas)**
13. Alkalis and Carbonates (NaOH, KOH, soda ash, lime) — `planned`
14. The Mineral Acids (HCl, H2SO4, HNO3 from OTC) — `planned`
15. Oxidizers of the Household (peroxide, hypochlorite, permanganate, chlorate via electrolysis) — `planned`
16. Sulfur and Its Compounds — `planned`
17. The Halogens and Their Salts — `planned`
18. Metals and Their Compounds (Cu, Fe, Zn, Al, Mg, Sn, Pb, Ag) — `planned`
19. Nitrogen and Ammonia (ammonia, nitrates, the N cycle at the bench) — `planned`
20. The Alcohol Family and Organic Solvents — `planned`
21. Indicators, Dyes, and Pigments — `planned`
22. Fats, Soaps, and Esters — `planned`

**Vol III — Theory Deepened at the Bench**
23. Equilibrium at the Kitchen Bench (buffers, Ksp in action) — `planned`
24. Kinetics You Can Watch (clock reactions, temperature, catalysis) — `planned`
25. Thermochemistry and Calorimetry — `planned`
26. Electroanalysis (conductivity, plating, electro-titration) — `planned`
27. Hazard Recognition and Neutralization — energetic & toxic hazards met or accidentally made: dangerous household combinations, oxidizer/organic incompatibilities; avoidance, quenching, neutralization, incident response — `planned`

**Vol IV — Projects: Rebuilding Useful Things**
28. Glass, Ceramics, and Lime — materials chemistry — `planned`
29. Food Chemistry (fermentation, preservation) — `planned`
30. Light-Sensitive Chemistry (cyanotype, silver halides) — `planned`
31. Cleaning-Product Chemistry (surfactants, chelation) — `planned`
32. Plant and Medicinal Extractions — `planned`
33. Adhesives, Polymers, and Plastics — `planned`

**Vol V — The Reagent Network Graph (capstone)**
34. The Tech Tree — the full dependency graph of syntheses, route economics, and the "what can I build from a supermarket + hardware store" map — `planned`

## 5. Progress Report

### Session log
| # | Date | Session | State | Outcome |
|---|------|---------|-------|---------|
| 1 | 2026-10-15 | Bootstrap | DONE | Topic + PROJECT.md created; P-index v0 (12 patterns); chapter map (34 ch/5 vols after energetics resolution); canon register; backup repo BLOCKED (user creating `everyday-chemistry-atlas`); Phase 1 gate PASSED (scope approved as mapped, no adjustments); survey-first sequencing decided; energetics resolved as Vol III Ch 27 hazard-recognition chapter, synthesis procedures excluded |
| 2 | 2026-10-15 | Repo mirror bootstrap + Survey batch 1 (NurdRage corpus) | DONE | Mirror live at dsmistral/everyday-chemistry-atlas (cold-start README, record mirrors, papers/ skeleton, 3 commits); sibling topic `everyday-chem-survey` created (KNOWLEDGE.md + SURVEY.md); batch 1 gathered register-first: 6 NurdRage papers (acid family, sodium, chlorate, luminol), all metadata/content-verified with honest gaps flagged; census: P1 6/6, P5/P7 zero-firing (batch 2 tests both); candidates CAND-1..4 opened, none promotable yet (need >= 2 batches) |

### Standing to-do
- [ ] NEXT UNIT: survey batch 2 — sub-chunk 2a: NurdRage hydrazine from bleach; iodine from iodide + HCl + H2O2 (CAND-1 recurrence test); copper sulfate three ways; chlorate by electrolysis (P5 test). Sub-chunk 2b: first NileRed entries. Then propose the authoring-start gate (after corpus priority-1 coverage: NurdRage core + Thompson/Dunn/Golden Book audit tables).
- [ ] Canon-coverage audit tables: Thompson vs Dunn vs Golden Book vs OpenStax, per chapter, before Vol I authoring.
- [ ] Survey deferrals (see everyday-chem-survey): transcript-level fetches; N05/N06 video dates; sequel-video channel attributions; follow-ups register (oxalate + bisulfate nitric-acid variants, sodium thermite originals, luminol precursors as first-class papers).
- [ ] Reagent-network data model for Ch. 33 (nodes=chemicals, edges=syntheses, edge costs per P10) — design during Vol II.

### Quality checklist (per chapter, from the skill's gates)
- [ ] Every problem solved ≥2 ways, each via a named P-ID.
- [ ] Lecture 0 (pencil-and-paper phenomenon before notation); one idea per lecture.
- [ ] Computational Lab EXECUTED in-session, outputs shown (labs here: stoichiometry/yield calculators, titration curve simulators, network-graph verifiers, solubility/Ksp calculators — computed, since bench chemistry itself can't run in-sandbox; bench procedures get rigorous sanity-check calculations instead).
- [ ] Graded exercises ●○○/●●○/●●● with hints + worked answers; ≥1 ◆ pattern-unknown per chapter; ◐ explorations.
- [ ] Safety assessment per experiment: hazards, PPE, quench/disposal route — non-optional gate.
- [ ] Canon-audit coverage check for the chapter's topics.
- [ ] Adversarial two-experts review (prover vs skeptic), objections machine-verified; verdict in session log.

### Verification-level adaptation for experimental chemistry (binding convention)
Claims about bench procedures are ranked: (1) **computed** — mass/mole/energy/eq calculations executed and shown; (2) **convergent** — consistent across ≥2 canon sources (name them); (3) **single-source** — cited, flagged as needing bench confirmation; (4) **speculative** — labeled as such, never presented as verified. No unverified claim may read as verified. Where the canon corpus (books/channels) has actually demonstrated a procedure, cite the source and its observed outcome as evidence.

## 6. Working Protocol

- Session open: read this file + KNOWLEDGE.md current state; mark session-log row IN PROGRESS; pick next unit from the Chapter Map.
- Session close: update chapter status, session log, KNOWLEDGE.md current-state paragraph; push record edits to the backup repo in the same session (records and pushes are one unit).
- Chapter canvases: one canvas per chapter under `/home/user/canvases/`; load `canvas` skill for format before authoring.
- Published chapters are never rewritten; corrections extend + revision appendix.
- Decisions: a decision exists only when recorded here as a dated paragraph marked "this paragraph the durable record".

## 7. Conventions (summary; full versions in the skill's `conventions.md`)

Feynman rule (intuition before formalism; "how you could have found this" commentary); discovery cycle (Encounter→Experiment→Conjecture→Struggle→Explain→Generalize); simplest-case-first worked to the end; pay-for-it density discipline; labs as demonstrations; same summit (never sand off difficulty). Plus the chemistry verification-level ladder in §5 above.

## 8. Safety Charter (binding)

Every experiment: hazard table (chemical, physical, environmental), minimum PPE, failure modes, quench procedure, disposal route, "do not scale up" notes. Restricted experiments list: no explosive/energetic materials synthesis (scope exclusion, pending user confirmation); no high-pressure or sealed-vessel procedures; fume-generating steps outdoors or with improvised ventilation. The charter is restated in full in Ch. 1 and enforced by the adversarial reviewer.

## 9. Backup repo

GitHub mirror of this record (and, as chapters are drafted, the manuscript masters): `everyday-chemistry-atlas`. Cold-start README: reading order = project KNOWLEDGE.md → PROJECT.md. Every record edit is pushed in the same session it is written.
