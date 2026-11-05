#!/usr/bin/env bash
# Session 186 diagnostic: run the extractor's compute stages (commit stage stubbed), capture all output
set -uo pipefail
export LC_ALL=C
cd "$GITHUB_WORKSPACE"
{
echo "=== DIAG $(date -u) ==="
echo "--- head:"; git log -1 --format='%h %s'
echo "--- masters ch:"; find manuscript -name 'ch[0-9][0-9].md' | wc -l
echo "--- masters fc:"; find manuscript/field-companion -name 'fc*.md' | wc -l
echo "--- parts:"; ls register-parts/ || echo "NO register-parts"
echo "--- stubbing commit section and running the extractor:"
sed '/# --- 8\. commit/,$d' register-parts/extract.sh > /tmp/extract-nocommit.sh
echo "stub lines: $(wc -l < /tmp/extract-nocommit.sh) (orig $(wc -l < register-parts/extract.sh))"
bash /tmp/extract-nocommit.sh
echo "EXIT: $?"
echo "--- agg rows: $(wc -l < /tmp/agg.tsv 2>/dev/null || echo none)"
echo "--- register bytes: $(wc -c < COMPOUND-REGISTER.md 2>/dev/null || echo none)"
echo "--- summary bytes: $(wc -c < SUMMARY.md 2>/dev/null || echo none)"
echo "--- occ head:"; head -3 /tmp/occ.tsv 2>/dev/null
} > DIAG.txt 2>&1
git config user.name "dsmistral"
git config user.email "deepsudden@gmail.com"
git add DIAG.txt
git commit -q -m "[diag] session 186 extractor stage trace"
git push
