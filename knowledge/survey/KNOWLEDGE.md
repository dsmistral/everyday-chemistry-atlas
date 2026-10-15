---
name: everyday-chem-survey
description: "Survey track for the Everyday-Chemistry Atlas: register-first distillation of the home-chemistry corpus (NurdRage first, then other channels + books + forums). Chunk ledger, dated gather entries, pattern census, candidates, deferrals, resume protocol. Feeds the book; never edits it."
---

# Everyday-Chemistry Survey — record (sibling project of `everyday-chem-book`)

## Current state

Survey live since 2026-10-15. Batches 1-4 complete (25 papers: video/web corpus + book canon). Session 6 (batch 5, 6 papers N26-N31): **CAND-7 second firing — oxalate H2SO4 (N28, new NurdRage video "Make SULFURIC acid from WEAK oxalic acid with the SUN", + Keras's independent CuSO4 replication with quantities) → recurrence test PASSED → REC-2 APPROVED same session: CAND-7 is now book P14 "Precipitation-driven acid liberation"**; Cu-nitrate waste recovery (N26 — the video corpus's first explicit A/B route comparison, vs N21's thermal route); bisulfate HNO3 (N27 — no sulfuric-acid precursor); Texium make-or-buy classification (N29 — the Tech Tree's cost function); Thompson Make: "Chemicals on the Cheap" (N30 — pottery-supply sourcing + the CuCO3 metathesis hub); Extractions&Ire channel audit (N31 — in-scope/excluded split; energetic fraction excluded by the binding line). **Corrections (authoritative): N14 is NileRed's video (2016-02-18), not NurdRage's; follow-up 0yvbJ8tE2y8 is ChemEx LK (minor channel), de-prioritized.** Census (31 papers): P1 28/31, P10 21/31, P2 17/31, P4 13/31, P3 5/31, P6 6/31, P11 9/31, P9 6/31, P5 5/31, P7 4/31, P8 4/31, P12 3/31, P13 3 firings. Per the session-6 authoring gate, more survey batches run before chapter authoring. NEXT: survey batch 6 — candidates: pre-1950 home-chem books (*The Boy Chemist*, *Chemical Magic*), Cody's Lab first entry, NurdRage urea-route hydrazine video (UB7vwIFCnR0), Extractions&Ire individual in-scope videos, Thompson Make: Parts I-II. The survey feeds the book; adoption decisions are user-approved; the survey never edits the manuscript.

## Routing

- `SURVEY.md` — the working survey record: dated per-chunk entries (extend, never rewrite), pattern census (firings/misses per P-ID), candidate patterns with recurrence-test evidence, follow-ups register, deferral ledger. **Read this first on every survey session open.**
- Repo: `dsmistral/everyday-chemistry-atlas` — `papers/` corpus: `CORPUS.md` (register), `STATE.md` (chunk ledger — source of truth for what is next), `batches/` (gather files), `patterns/candidates/` (CAND- files), `ANALYSIS.md` (synthesis from dossiers). Mirrors of this topic: `knowledge/survey/`.
- Method: `survey-track.md` in the science-book-builder skill. Gather = fresh verification (never from memory), faithful summary, decisive moves tagged with book P-IDs, candidates AND honest misses logged, verification level recorded per paper.

## Resume protocol

1. Read `SURVEY.md`, then repo `papers/STATE.md` for the NEXT chunk.
2. Verify each source register-first (fresh web search; record URLs + verification evidence).
3. Write `papers/batches/batch-NNx.md` per sub-chunk (~3 papers), one push commit per sub-chunk, mirroring `SURVEY.md` + `knowledge/survey/` in the same commit.
4. Update the dated entry in `SURVEY.md` + push; append, never rewrite.

## Deferral ledger (dated, upgradeable)

- 2026-10-15: Transcript-level fetches deferred for all batch-1 papers (content-verified via author mirrors + corroborations). Upgrade when a candidate pattern needs teaching-grade detail.
- 2026-10-15: Video dates unverified for N05 (potassium chlorate) and N06 (luminol); channel attribution of the "3-Nitrophthalic Acid" and "improved sodium" videos to verify at next pass.
- 2026-10-15: NurdRage electrolysis chlorate video + oxalate/bisulfate nitric-acid variants registered as follow-ups — RESOLVED: gathered as N10, N16 (the bisulfate variant still open as a follow-up).
- 2026-10-16: Batch-3 honest gaps — N14 upload date unverified; N15 product-concentration step and N17 purification details not in mirror text (transcript fetch flagged); oxalic-acid OTC availability unverified; N19 has no verified-attribution YouTube video (web sources registered instead). Transcript-level fetches for batch-3 papers deferred.
- 2026-10-16: P12 yield hunt missed across batches 2-3 — RESOLVED (session 5, batch 4a): N21 states its own 60-80% yield (transcript-level datum, in-video confirmation flagged); Dunn's stoichiometry project (N23) adds book-canon bookkeeping.
- 2026-10-16: Cody's Lab lime video did not surface in fresh searches; Primitive Technology + SkillCult verified instead; optional Cody's Lab corroboration at a later pass.
- 2026-10-15 (session 5): clock note — the sandbox clock reads 2026-10-15 UTC while session-3/4 records carry 2026-10-16 dating from their time context; session-log chronology follows session numbers (noted in PROJECT.md row 5).
- 2026-10-15 (session 5): batch-4 honest gaps — N21 upload date unverified; N21 in-video yield confirmation flagged; N22 description-level only; Dunn publisher imprint to pin; Golden Book per-chapter page-level TOC to pin; CAND-7's H2SO4 face (ScienceMadness sulphates+oxalic-acid thread) unverified — **RESOLVED (session 6): gathered inside N28; CAND-7 second firing verified; promoted to book P14 (REC-2 approved)**.
- 2026-10-15 (session 6): batch-5 honest gaps — N26 copper-metal recovery step method not evidenced at description level (transcript fetch flagged); N27 wet-vs-dry variant details description-level; N28 "with the SUN" element unverified (transcript fetch flagged; Keras's ~8 M figure is a theoretical ceiling, not a measured yield); N30 Make: article date unpinned (series circa 2009); N31 Extractions&Ire audit is archive-listing level (individual video gathers deferred as follow-ups); **N14 attribution corrected to NileRed (2016-02-18) — the batch-03a NurdRage attribution was wrong; chemistry datum unchanged**; follow-up 0yvbJ8tE2y8 identified as ChemEx LK (minor channel, de-prioritized); NurdRage urea-route hydrazine video UB7vwIFCnR0 unverified.
