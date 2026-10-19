# web/renderer-record.md — the session-108 line-block renderer, rebuilt and recorded (session 121, 2026-10-19)

**What this records.** The book's md→HTML reading-edition renderer — first built session 108, **not durably saved then** (the recorded lesson, the reason all five FC web editions stood as debts) — was rebuilt in session 121 from the recorded spec + the `web/ch01-web.html` template, **validated byte-identical before any FC render**, used to render the five Field-Companion web editions, and this time **saved durably and pushed**: `web/renderer.ts` (9,854 B, the full validated source with the CSS embedded verbatim) + this record. The session-108 debt class is closed.

## §1 Validation (the claim of record)

- **Pre-compaction pass (this session):** the rebuilt renderer reproduced **all 36 chapter web files byte-identically** from their masters (ch01/ch02 fetched pairs; ch03–ch30 local masters; ch31–ch36 repo masters) before any FC page was rendered.
- **Post-compaction re-validation:** the session's context compaction lost the working code; the renderer was re-authored from the recorded spec and **re-validated 6/6 byte-identical** on representative pairs covering every path the corpus exercises — ch01 (nested + loose lists, code spans, h1–h3), ch02, ch04/ch22/ch28 (nested lists), ch20 (thead tables, long fences) — 47,209 / 39,690 / 53,476 / 78,842 / 64,543 / 49,892 bytes, string equality, no normalization.
- **The FC renders (the deliverable):** web/fc1-web.html 50,563 B; fc2 45,114; fc3 46,614; fc4 51,067; fc5 44,994 — pushed at commit 3210a0c, every repo blob size-verified against the local renders; the 36 chapter pages untouched; index.html 6,295 → 6,807 B (banner + intro line + the Field Companion section).
- **CSS byte count, honestly:** the embedded CSS slice (ch01-web.html, `indexOf('<style>')+7` to `indexOf('</style>')`) measures **1,619 B by the session-121 manual UTF-8 counter**; the session-108 record printed 1,618. A one-byte counting discrepancy, recorded here as found; **non-load-bearing** — the CSS is spliced verbatim from the ground-truth file, so the rendered bytes are identical either way.

## §2 The algorithm (as validated)

**Inline pipeline, order load-bearing:** `esc` (& < > " → entities) → code (`` `x` `` → `<code>x</code>`) → link (`[t](u)` → `<a href="u">t</a>`) → strong (`\*\*([^*]+?)\*\*`) → em (`(?<!\w)\*([^*\s](?:[^*]*[^*\s])?)\*(?!\w)` — the opening star not after a word char, content star-free with no leading/trailing space, the closing star not before a word char).

**Block layer:** frontmatter stripped (opening `---` pair; the title read via `/^title:\s*"(.*)"$/m` and used verbatim as `<title>`); **the content-contract cut at the first `/^## [Cc]anon/ line** — Canon-Coverage and everything after it (Forward Flags, Back Flags, Chapter Ledger, Revision Appendix) stay md-only; trailing pops (blanks → one `---` → blanks — the pre-canon `---` is consumed here so the page tail can own its `<hr>`); `---` → `<hr>`; headings `/^#{1,6}\s/` → h1–h4 capped `Math.min(len,4)` with inline applied; fences → `<pre><code>` + esc(lines).join('\n') + `</code></pre>` (trailing spaces **preserved**); blockquotes (§5); tables (§3); lists (§4); paragraphs = consecutive plain lines, each `.trim()`'d, joined with a single space, wrapped `<p>…</p>`.

**Page template:** `<!doctype html>` … `<style>` + CSS + `</style>` … `<main id="content">` + banner paragraph + blocks + **tail-owned** `<hr>` + the no-print contract banner + close. Blocks are concatenated with no blank lines; every block emits its own trailing newline.

## §3 Tables (the session-108 ground truth, reproduced)

Rows match `/^\s*\|/` (leading whitespace allowed — the "whitespace-prefixed table rows" quirk). Cells: strip the leading `|` and a trailing `|\s*$`, split on `|`, trim each. If `rows[1]` is all cells `/^-+$/` → `<thead><tr><th>…</th></tr></thead>` from rows[0], tbody = the rest; **else no thead, tbody = all rows** (the thead-less separator-less case — supported, unexercised by both the 36 chapters and the five FCs, whose tables all carry separator rows). Rows render one per line: `<tr><td>a</td><td>b</td></tr>`, tbody/`</table>` on their own lines.

## §4 Lists (the session-108 reverse-engineered quirks, reproduced faithfully)

- Tag from the first item's marker (`/^\s*\d+\.\s/` → ol, `/^\s*[-*]\s/` → ul); **a blank line does NOT close a list** (loose lists — item, blank, item render as one `<ul>`; verified against ch03's ground truth).
- An indented item opens a sub-list **with the PARENT's tag** (`<ol>` under an `ol` even when the sub-markers are `-` — ch01's ground truth).
- Return from a sub-list emits **`</tag></li>\n<li><li>content</li>`** — the double-`<li>` artifact of the original session-108 renderer, reproduced byte-for-byte, never "fixed" (fixing it would break byte-equality with the 36 shipped pages).
- A block ending inside a sub-list closes `</subtag></li>` then `</tag>`.

## §5 Session-121 conventions (no session-108 ground truth — decisions, flagged as such)

- **Blockquote:** `/^> /` lines, the `> ` stripped, consecutive quote lines joined with a single space, **inline applied**, wrapped `<blockquote>…</blockquote>`. The FC masters carry the corpus's only two blockquotes (fc1 md lines 83 and 247); no chapter exercises the path, so the format is a session-121 decision recorded here, not a validated equality.
- **The FC banner:** `The Everyday Chemist's Atlas — The Field Companion · FC{n} ({subtitle — the part of the frontmatter title after "— "}). HTML reading edition, generated 2026-10-19 from the manuscript master. The Canon-Coverage record and the review apparatus (forward flags, back flags, chapter ledger, revision appendix) remain in the .md master.` Chapter banners keep the session-108 form (`Vol {N} · Chapter {n} ({volume name})` with the page's own generation date).

## §6 Tooling notes (binding for future renders)

- The FC render sources: fc1 fetched from the repo master (69,337 B, byte-verified against the listing); fc2–fc5 from the local canvases, each verified at **repo blob size − 1** (the canvases lack the trailing newline — harmless: the split/trim layer is insensitive to it, and the page tail supplies the final newline).
- The FC census held: no nested lists, no links, no code spans in the FC bodies (fc1's inline backticks all sit after the canon cut), no separator-less tables — the renders exercise only validated paths plus fc1's two blockquotes (§5).
- GitHub `search_code` remains unindexed for this repo; `get_file_contents` returns a stub at `r[0].text` and the full text at `r[1].resource.text` (the session-120 tooling note, binding).

## §7 Where everything lives

Local master copies: this folder's `web/` (renderer.ts, renderer-record.md, fc1–fc5-web.html, the extended index.html, all 36 chapter pages). Repo mirror: `web/` in dsmistral/everyday-chemistry-atlas (same filenames, pushed session 121). The .md masters remain the master of record; the HTML is a derived layer. Per the web-sync rule, any future md-master update owes a re-render + push of its web file in the same session.
