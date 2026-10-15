---
name: everyday-chem-survey
description: "Survey track for the Everyday-Chemistry Atlas: register-first distillation of the home-chemistry corpus (NurdRage first, then other channels + books + forums). Chunk ledger, dated gather entries, pattern census, candidates, deferrals, resume protocol. Feeds the book; never edits it."
---

# Everyday-Chemistry Survey — record (sibling project of `everyday-chem-book`)

## Current state

Survey live since 2026-10-15. Batches 1-3 complete (19 papers): batch 1 NurdRage core (acid family, sodium, chlorate, luminol); batch 2 NurdRage round 2 + first NileRed entries; batch 3 (2026-10-16) NurdRage round 3 (urea-hydrazine route, electrochemical H2SO4, oxalate-precipitation HNO3, iodine-from-H2SO4) + the P7 hunt (Primitive Technology lime cycle + SkillCult; baking-soda calcination via ThoughtCo/Scientific American). **P7 FIRES: 2/19** (lime-cycle archetype N18 + kitchen face N19). **CAND-7 opened: precipitation-driven acid liberation** (N16 — the P3/P4 intersection; watch: sulphates+oxalic-acid H2SO4 extension, ScienceMadness thread). CAND-5 honest miss in N14 (urea hydrazine needs no protective intermediate). P13 (promoted REC-1) now has 3 firings and a third face (generated-unstable-acid). P12 still weak (1/19) — hunt continues with sharper targets (NurdRage azeotropic-HNO3 Patreon post, Thompson yield tables, refining forums). Honest gaps: N14 upload date, N15 product-concentration and N17 purification details unverified (mirror-text level); transcript-level fetches deferred. Next: book-canon batches (Thompson / Dunn / Golden Book audit tables + OpenStax coverage check), then the authoring-start proposal. The survey feeds the book; adoption decisions are user-approved; the survey never edits the manuscript.

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
- 2026-10-15: NurdRage electrolysis chlorate video + oxalate/bisulfate nitric-acid variants registered as follow-ups — RESOLVED 2026-10-16: gathered as N10, N16 (and the bisulfate variant still open as a follow-up).
- 2026-10-16: Batch-3 honest gaps — N14 upload date unverified; N15 product-concentration step and N17 purification details not in mirror text (transcript fetch flagged); oxalic-acid OTC availability unverified; N19 has no verified-attribution YouTube video (web sources registered instead). Transcript-level fetches for batch-3 papers deferred.
- 2026-10-16: P12 yield hunt missed across batches 2-3 (1/19); sharper targets registered (NurdRage azeotropic-HNO3 Patreon post; Thompson yield tables; refining-forum stoichiometry threads).
- 2026-10-16: Cody's Lab lime video did not surface in fresh searches; Primitive Technology + SkillCult verified instead; optional Cody's Lab corroboration at a later pass.
