# The Everyday-Chemistry Atlas

Backup repo (self-sufficient resume point) for the book project **The Everyday Chemist's Atlas: Rebuilding the Reagent World from Household Materials** — a comprehensive home-chemistry experiment book built from everyday materials ("the post-apocalyptic chemist" premise), full theory track, strict safety charter.

## Cold start — reading order

1. `knowledge/KNOWLEDGE.md` — project topic entrypoint: current state + routing. **Read this first.**
2. `knowledge/PROJECT.md` — the working master record: scope decisions, durable decisions log, Canon Register, Master Pattern Index (P-index), Chapter Map, session log, Working Protocol, Conventions, Safety Charter.

## Repo map

- `knowledge/` — byte-identical mirror of the project's Personal Knowledge topic (the Knowledge base is the working master; this repo is the mirror). Every record edit is pushed in the same session it is written.
- `papers/` — survey-track corpus (sibling project `everyday-chem-survey`): `CORPUS.md` (registered sources, unverified until gathered), `STATE.md` (chunk ledger — source of truth for what is next), `README.md` (per-paper template + chunk protocol), `patterns/` (one dossier per P-ID + candidates), `ANALYSIS.md` (synthesis, written from dossiers). The survey feeds the book; it never edits the manuscript; adoptions are user-approved.
- `manuscript/` — chapter masters (one file per chapter), mirrored as chapters are drafted.

## Method

Built with the `science-book-builder` pipeline: lecture-style chapters (Lecture 0, one idea per lecture), every verifiable claim machine-verified, graded exercises with pattern-unknown diagnostics, adversarial two-experts review per chapter, quality gates before a chapter closes.
