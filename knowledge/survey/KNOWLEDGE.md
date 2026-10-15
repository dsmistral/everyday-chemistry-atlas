---
name: everyday-chem-survey
description: "Survey track for the Everyday-Chemistry Atlas: register-first distillation of the home-chemistry corpus (NurdRage first, then other channels + books + forums). Chunk ledger, dated gather entries, pattern census, candidates, deferrals, resume protocol. Feeds the book; never edits it."
---

# Everyday-Chemistry Survey — record (sibling project of `everyday-chem-book`)

## Current state

Survey live since 2026-10-15. Batches 1-3 (video/web corpus, 19 papers) + batch 4 (book canon, session 5) complete: 25 papers gathered register-first. Batch 4a: Thompson canon audit (anchors Vol I; the BUY branch; his forensic chapter = FINDING-A), NurdRage copper-nitrate recycling (**P12 hunt RESOLVED — the source states its own 60-80% yield; P7 third firing**), azeotropic-HNO3 (**P6 archetype**). Batch 4b: Dunn canon audit (28 projects verified; **Leblanc-vs-Solvay = the historical P10 exemplar**; gunpowder chapter = FINDING-B1 under the energetics binding line), Golden Book (ambition benchmark), OpenStax (theory-coverage check; **FINDING-B2 nuclear chemistry absent; FINDING-C atomic-structure/bonding has no home chapter**). Census (25 papers): P1 22/25, P10 15/25, P2 14/25, P12 3/25 (resolved), P7 4/25, P13 3 firings/3 faces. CAND-7 (precipitation-driven acid liberation) has one firing — not yet promotable. First ANALYSIS.md synthesis written. Honest gaps: transcript fetches deferred; several dates unverified; Dunn publisher imprint + Golden Book page-level TOC to pin. NEXT: the authoring-start proposal (user gate); the survey then continues opportunistically alongside authoring (CAND-7 watch, follow-ups). The survey feeds the book; adoption decisions are user-approved; the survey never edits the manuscript.

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
- 2026-10-15 (session 5): batch-4 honest gaps — N21 upload date unverified; N21 in-video yield confirmation flagged; N22 description-level only; Dunn publisher imprint to pin; Golden Book per-chapter page-level TOC to pin; CAND-7's H2SO4 face (ScienceMadness sulphates+oxalic-acid thread) unverified.
