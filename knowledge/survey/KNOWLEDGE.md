---
name: everyday-chem-survey
description: "Survey track for the Everyday-Chemistry Atlas: register-first distillation of the home-chemistry corpus (NurdRage first, then other channels + books + forums). Chunk ledger, dated gather entries, pattern census, candidates, deferrals, resume protocol. Feeds the book; never edits it."
---

# Everyday-Chemistry Survey — record (sibling project of `everyday-chem-book`)

## Current state

Survey live since 2026-10-15 (book session 2). Batch 1 (NurdRage corpus, 6 papers, sub-chunks 1a + 1b) gathered register-first: acid family (sulfuric generation + distillation purification, nitric acid), sodium metal, potassium chlorate from bleach, luminol synthesis. 4 candidate patterns opened (CAND-1..4). Corpus skeleton + batch files live in the backup repo `dsmistral/everyday-chemistry-atlas` under `papers/`. Next: batch 2 (NurdRage continued: hydrazine from bleach, iodine from iodide, copper sulfate three ways; then first NileRed entries). The survey feeds the book; adoption decisions are user-approved; the survey never edits the manuscript.

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
- 2026-10-15: NurdRage electrolysis chlorate video + oxalate/bisulfate nitric-acid variants registered as follow-ups, not yet gathered.
