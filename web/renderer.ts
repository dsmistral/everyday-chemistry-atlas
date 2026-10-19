// web/renderer.ts — the Everyday Chemist's Atlas line-block md->HTML renderer.
// PROVENANCE: first built session 108 (not durably saved then — the recorded lesson);
// rebuilt session 121 (2026-10-19) from the recorded spec + the web/ch01-web.html template
// and VALIDATED byte-identical against the repo web files BEFORE any FC render:
//   36/36 chapters byte-identical in the session-121 pre-compaction pass
//   (ch01/ch02 fetched pairs; ch03-ch30 local masters; ch31-ch36 repo masters),
//   then re-validated 6/6 byte-identical post-compaction on representative pairs
//   (ch01, ch02, ch04, ch20, ch22, ch28 — covering nested + loose lists, thead tables,
//   fences, code spans, headings; 47,209/39,690/53,476/78,842/64,543/49,892 bytes).
// Used session 121 to render web/fc1-web.html..fc5-web.html (commit 3210a0c).
// CONTENT CONTRACT: every page ends BEFORE the first /^## [Cc]anon/ line — Canon-Coverage
// and everything after it (Forward Flags, Back Flags, Chapter Ledger, Revision Appendix)
// remain md-only. The algorithm spec, the reverse-engineered session-108 quirks, and the
// session-121 conventions are documented in web/renderer-record.md.
// Runnable in the Vibe run_typescript sandbox (tools.file_system for I/O); no imports.

// The page CSS, embedded VERBATIM: the slice of web/ch01-web.html between
// indexOf("<style>")+7 and indexOf("</style>") (session-121 manual UTF-8 count:
// 1619 bytes; the session-108 record printed 1,618 — a one-byte counting
// discrepancy, non-load-bearing: the splice is verbatim, rendered bytes unaffected).
const CSS = "\n  :root { font-family: Georgia, 'Times New Roman', serif; color: #1a1a1a; }\n  body { max-width: 46rem; margin: 0 auto; padding: 1.5rem 1.2rem 4rem; line-height: 1.55; background: #fff; }\n  h1 { font-size: 1.9rem; margin: 2.2rem 0 0.8rem; }\n  h2 { font-size: 1.45rem; margin: 2rem 0 0.6rem; border-bottom: 1px solid #ddd; padding-bottom: 0.25rem; }\n  h3 { font-size: 1.2rem; margin: 1.6rem 0 0.5rem; }\n  h4 { font-size: 1.05rem; margin: 1.3rem 0 0.4rem; }\n  pre, code { font-family: 'Courier New', Courier, monospace; }\n  code { background: #f2f2f2; padding: 0.05em 0.3em; border-radius: 3px; font-size: 0.92em; }\n  pre { white-space: pre; tab-size: 4; break-inside: avoid; page-break-inside: avoid; overflow-x: auto; border: 1px solid #ddd; background: #fafafa; padding: 0.7rem 0.9rem; font-size: 0.85rem; line-height: 1.35; }\n  blockquote { border-left: 3px solid #888; margin: 1rem 0; padding: 0.2rem 1rem; color: #333; }\n  table { border-collapse: collapse; margin: 1rem 0; break-inside: avoid; page-break-inside: avoid; }\n  th, td { border: 1px solid #bbb; padding: 0.35rem 0.6rem; text-align: left; }\n  th { background: #f0f0f0; }\n  hr { border: 0; border-top: 1px solid #ccc; margin: 2rem 0; }\n  .banner { background: #eef6ff; border: 1px solid #bcd6f0; border-radius: 6px; padding: 0.8rem 1rem; font-size: 0.9rem; font-family: system-ui, sans-serif; margin-bottom: 1.5rem; }\n  @page { size: A4; margin: 16mm 15mm; }\n  @media print { body { max-width: none; padding: 0; font-size: 10.5pt; } .no-print { display: none; } pre { font-size: 8.8pt; } h1, h2, h3, h4 { break-after: avoid; page-break-after: avoid; } }\n";

function byteLen(s: string): number {
  let n = 0;
  for (let i = 0; i < s.length; i++) {
    const c = s.charCodeAt(i);
    if (c < 0x80) n += 1;
    else if (c < 0x800) n += 2;
    else if (c >= 0xd800 && c <= 0xdbff) { n += 4; i++; }
    else n += 3;
  }
  return n;
}

// Inline pipeline — ORDER IS LOAD-BEARING: escape, then code, then link, then strong, then em.
const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
function inline(s: string): string {
  s = esc(s);
  s = s.replace(/`([^`]*)`/g, (m, c) => '<code>' + c + '</code>');
  s = s.replace(/\[([^\]]*)\]\(([^)]*)\)/g, (m, t, u) => '<a href="' + u + '">' + t + '</a>');
  s = s.replace(/\*\*([^*]+?)\*\*/g, (m, c) => '<strong>' + c + '</strong>');
  s = s.replace(/(?<!\w)\*([^*\s](?:[^*]*[^*\s])?)\*(?!\w)/g, (m, c) => '<em>' + c + '</em>');
  return s;
}

const isItem = (l: string) => /^\s*\d+\.\s/.test(l) || /^\s*[-*]\s/.test(l);

function blocks(md: string): string {
  let lines = md.split('\n');
  // frontmatter strip (title lives between the opening --- pair)
  if (lines[0].trim() === '---') {
    let j = 1; while (j < lines.length && lines[j].trim() !== '---') j++;
    lines = lines.slice(j + 1);
  }
  // the content-contract cut: everything from the first Canon-Coverage heading is dropped
  const ci = lines.findIndex((l: string) => /^## [Cc]anon/.test(l));
  if (ci >= 0) lines = lines.slice(0, ci);
  // trailing pops: blanks, then ONE hr (the pre-canon ---), then blanks
  while (lines.length && !lines[lines.length - 1].trim()) lines.pop();
  if (lines.length && lines[lines.length - 1].trim() === '---') lines.pop();
  while (lines.length && !lines[lines.length - 1].trim()) lines.pop();
  const out: string[] = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }
    if (/^```/.test(line)) {
      const buf: string[] = []; i++;
      while (i < lines.length && !/^```/.test(lines[i])) { buf.push(lines[i]); i++; }
      i++;
      out.push('<pre><code>' + buf.map(esc).join('\n') + '</code></pre>\n');
      continue;
    }
    if (/^#{1,6}\s/.test(line)) {
      const lvl = Math.min((line.match(/^#{1,6}/) as RegExpMatchArray)[0].length, 4);
      const txt = line.replace(/^#{1,6}\s/, '');
      out.push('<h' + lvl + '>' + inline(txt) + '</h' + lvl + '>\n');
      i++; continue;
    }
    if (line.trim() === '---') { out.push('<hr>\n'); i++; continue; }
    if (/^> /.test(line)) {
      const buf: string[] = [];
      while (i < lines.length && /^> /.test(lines[i])) { buf.push(lines[i].slice(2)); i++; }
      out.push('<blockquote>' + inline(buf.join(' ')) + '</blockquote>\n');
      continue;
    }
    if (/^\s*\|/.test(line)) {
      const rows: string[][] = [];
      while (i < lines.length && /^\s*\|/.test(lines[i])) {
        rows.push(lines[i].replace(/^\s*\|/, '').replace(/\|\s*$/, '').split('|').map((c: string) => c.trim()));
        i++;
      }
      let h = '<table>\n';
      if (rows.length > 1 && rows[1].every((c: string) => /^-+$/.test(c))) {
        h += '<thead><tr><th>' + rows[0].map(inline).join('</th><th>') + '</th></tr></thead>\n';
        rows.splice(0, 2);
      }
      h += '<tbody>\n' + rows.map((r: string[]) => '<tr><td>' + r.map(inline).join('</td><td>') + '</td></tr>').join('\n') + '\n</tbody>\n</table>\n';
      out.push(h); continue;
    }
    if (isItem(line)) {
      const tag = /^\s*\d+\.\s/.test(line) ? 'ol' : 'ul';
      out.push('<' + tag + '>\n');
      let inSub = false, subTag = 'ol';
      while (i < lines.length) {
        const l = lines[i];
        if (!l.trim()) { i++; continue; }  // a blank line does NOT close a list (loose lists)
        if (!isItem(l)) break;
        const indented = /^\s/.test(l);
        const m = l.match(/^\s*(\d+\.|[-*])\s/) as RegExpMatchArray;
        const content = l.slice(m[0].length).trim();
        if (indented) {
          if (!inSub) { subTag = tag; out.push('<' + subTag + '>\n'); inSub = true; }  // sub-list opens with the PARENT tag
          out.push('<li>' + inline(content) + '</li>\n');
        } else {
          if (inSub) { out.push('</' + subTag + '></li>\n<li><li>' + inline(content) + '</li>\n'); inSub = false; }  // the session-108 double-li artifact, reproduced faithfully
          else out.push('<li>' + inline(content) + '</li>\n');
        }
        i++;
      }
      if (inSub) out.push('</' + subTag + '></li>\n');
      out.push('</' + tag + '>\n');
      continue;
    }
    // paragraph: consecutive plain lines, each trimmed, joined with a single space
    const buf: string[] = [];
    while (i < lines.length) {
      const l = lines[i];
      if (!l.trim()) break;
      if (/^```/.test(l) || l.trim() === '---' || /^#{1,6}\s/.test(l) || /^\s*\|/.test(l) || /^> /.test(l) || isItem(l)) break;
      buf.push(l.trim()); i++;
    }
    out.push('<p>' + inline(buf.join(' ')) + '</p>\n');
  }
  return out.join('');
}

function page(title: string, banner: string, body: string): string {
  return '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>' + title + '</title>\n<style>' + CSS + '</style>\n</head>\n<body>\n<main id="content">\n<p class="banner">' + banner + '</p>\n' + body + '<hr>\n<p class="banner no-print">HTML edition of the reviewed manuscript — the labels are the contract. Canon-Coverage and everything after it live in the .md master only.</p>\n</main>\n</body>\n</html>\n';
}

// Entry point: render one md master. Title = the frontmatter title verbatim.
function renderPage(md: string, banner: string): string {
  const title = (md.match(/^title:\s*"(.*)"$/m) as RegExpMatchArray)[1];
  return page(title, banner, blocks(md));
}

// Session-121 FC banner convention (a session-121 decision; see renderer-record.md §5):
//   The Everyday Chemist's Atlas — The Field Companion · FC{n} ({subtitle, the part of the
//   frontmatter title after "— "}). HTML reading edition, generated 2026-10-19 from the
//   manuscript master. The Canon-Coverage record and the review apparatus (forward flags,
//   back flags, chapter ledger, revision appendix) remain in the .md master.
// Chapter banners (session-108 ground truth) carry the form:
//   The Everyday Chemist's Atlas — Vol {N} · Chapter {n} ({volume name}). HTML reading
//   edition, generated {date} from the manuscript master. The Canon-Coverage record and the
//   review apparatus (forward flags, back flags, chapter ledger, revision appendix) remain
//   in the .md master.
