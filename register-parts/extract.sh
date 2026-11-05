#!/usr/bin/env bash
# Session 186 — the Compound Audit extractor (register-level, provisional keyword-window tags)
# Runs in-repo over the 61 masters. Writes COMPOUND-REGISTER.md + audit/compound-register/*.
set -euo pipefail
export LC_ALL=C
cd "$GITHUB_WORKSPACE"

FENCE_FILES="manuscript/vol3/ch28.md manuscript/vol7/ch50.md"

# --- 1. master census (61) ---
find manuscript -name 'ch[0-9][0-9].md' | sort > /tmp/allfiles.txt
find manuscript/field-companion -name 'fc*.md' | sort >> /tmp/allfiles.txt
NF=$(wc -l < /tmp/allfiles.txt)
if [ "$NF" -ne 61 ]; then echo "MASTER CENSUS FAIL: $NF (expected 61)"; exit 1; fi
echo "masters: 61"

# --- 2. flatten lexicon ---
awk -F"\\|\\|" '{
  wb=$4; sub(/;;.*/,"",wb);
  n=split($5,a,";;");
  for(i=1;i<=n;i++){ if(length(a[i])>0) print a[i] "\t" wb "\t" NR > "/tmp/aliases.txt" }
  print NR "\t" $1 "\t" $2 "\t" $3 > "/tmp/rows.txt"
}' register-parts/lexicon.txt
NROW=$(wc -l < /tmp/rows.txt)
NAL=$(wc -l < /tmp/aliases.txt)
echo "lexicon rows: $NROW aliases: $NAL"

# --- 3. occurrence + window pass (one awk per master) ---
rm -f /tmp/occ.tsv
while IFS= read -r f; do
  awk -v FC="$f" '
  BEGIN {
    nA=0; while((getline l < "/tmp/aliases.txt")>0){ split(l,f2,"\t"); nA++; AL[nA]=f2[1]; WB[nA]=f2[2]; RID[nA]=f2[3] }
  }
  {
    L=tolower($0); TXT[NR]=L
    PV[NR] = (L ~ /make|prepar|synthes|distill|electroly|precipitat|crystalliz|dehydrat|calcin|smelt|refin|generat|convert|evaporat|reflux|oxidiz|reduc|leach|roast|sinter|ferment|pyrolys|carboniz|resublim|cast|formed in situ/) ? 1:0
    SV[NR] = (L ~ /buy|bought|purchas|shelf|aisle|hardware|pharmacy|grocery|retail|price|label|census|drugstore|pottery|catalog|supermarket|hobby supplier|online|\$/) ? 1:0
    RV[NR] = (L ~ /never|avoid|exclud|hazard|toxic|poison|danger|recognition|fence|prohibit|illegal|restricted|do not|banned/) ? 1:0
  }
  END {
    for(i=1;i<=NR;i++){
      wp=0;ws=0;wr=0
      for(j=i-3;j<=i+3;j++){ if(j>=1&&j<=NR){ if(PV[j])wp=1; if(SV[j])ws=1; if(RV[j])wr=1 } }
      L=TXT[i]
      for(a=1;a<=nA;a++){
        la=length(AL[a]); rest=L; c=0
        while((ix=index(rest,AL[a]))>0){
          ok=1
          if(WB[a]=="1"){
            pre = (ix==1) ? "" : substr(rest,ix-1,1)
            post = (ix+la > length(rest)) ? "" : substr(rest,ix+la,1)
            if((pre!="" && pre ~ /[a-z0-9]/) || (post!="" && post ~ /[a-z0-9]/)) ok=0
          }
          if(ok)c++
          rest=substr(rest,ix+la)
        }
        if(c>0){ rid=RID[a]; key=rid SUBSEP FC; OCC[key]+=c; if(wp)PW[key]=1; if(ws)SW[key]=1; if(wr)RW[key]=1 }
      }
    }
    for(k in OCC){
      split(k,p2,SUBSEP)
      printf "%s\t%s\t%d\t%d\t%d\t%d\n", p2[1], p2[2], OCC[k], (PW[k]?1:0), (SW[k]?1:0), (RW[k]?1:0)
    }
  }' "$f" >> /tmp/occ.tsv || true
done < /tmp/allfiles.txt
NPAIR=$(wc -l < /tmp/occ.tsv)
echo "compound-chapter pairs: $NPAIR"

# --- 4. unknown-formula candidate sweep (phase-2 adjudication list) ---
: > /tmp/cand_raw.txt
while IFS= read -r f; do
  grep -ohE '\b([A-Z][a-z]?[0-9]{0,2}){2,7}\b' "$f" 2>/dev/null | grep -E '[0-9]' >> /tmp/cand_raw.txt || true
done < /tmp/allfiles.txt
sort /tmp/cand_raw.txt | uniq -c | sort -rn > /tmp/cand_counts.txt
awk 'BEGIN{ while((getline l < "/tmp/aliases.txt")>0){ split(l,f2,"\t"); A[f2[1]]=1 } }
  { t=$2; tl=tolower(t); if(!(tl in A) && length(t)>=3) print }' /tmp/cand_counts.txt > /tmp/cand_new.txt
# stoplist: register/meta tokens that look formula-like but are not compounds
grep -viE '^[[:space:]]*[0-9]+ (Lab|Vol|II|III|IV|VI|VII|VIII|IX|XI|XII|Ex|Fig|RA|RF|SDS|PPE|GHS|CAS|OTC|NPK|TLV|PEL)$' /tmp/cand_new.txt > /tmp/cand_final.txt || true
NCAND=$(wc -l < /tmp/cand_final.txt)
echo "phase-2 candidates: $NCAND"

# --- 5. aggregate + tag ---
awk -v FENCE="$FENCE_FILES" -v OUTROW=/tmp/agg.tsv '
BEGIN{ while((getline l < "/tmp/rows.txt")>0){ split(l,f2,"\t"); R[f2[1]]=f2[2]; FORM[f2[1]]=f2[3]; CAT[f2[1]]=f2[4] } }
{
  rid=$1; file=$2; cnt=$3; pw=$4; sw=$5; rw=$6
  base=file; sub(/^.*\//,"",base)
  key=rid; OCC[key]+=cnt; NCH[key]++
  if(!(key in FIRST) || file < CH[key,1]) {} 
  CH[key, NCH[key]] = file
  if(pw)P[key]=1; if(sw)S[key]=1; if(rw)RC[key]=1
  nonfence=0; isfence=0
  split(FENCE,FF," ")
  for(x in FF){ if(file==FF[x]) isfence=1 }
  if(!isfence) NONF[key]=1
}
END{
  for(k in OCC){
    tag=""
    if(!(k in NONF)) tag="recognition-only-fence"
    else if(P[k] && S[k]) tag="manufactured+procured"
    else if(P[k]) tag="manufactured"
    else if(S[k]) tag="procured"
    else if(RC[k]) tag="recognition-only"
    else tag="MENTIONED-ONLY"
    chap=""
    for(i=1;i<=NCH[k];i++){ c=CH[k,i]; sub(/^.*\//,"",c); sub(/\.md$/,"",c); chap = chap (i>1?",":"") c }
    print k "\t" R[k] "\t" FORM[k] "\t" CAT[k] "\t" OCC[k] "\t" NCH[k] "\t" chap "\t" tag
  }
}' /tmp/occ.tsv | sort -t$'\t' -k4,4 -k2,2 > /tmp/agg.tsv || true
NAGG=$(wc -l < /tmp/agg.tsv)
echo "aggregated compounds: $NAGG"
if [ "$NAGG" -lt 100 ]; then echo "AGGREGATE FAIL (too few)"; exit 1; fi

# --- 6. build COMPOUND-REGISTER.md ---
{
echo "# The Compound Register — the whole-Atlas compound census (session 186, 2026-11-05)"
echo
echo "Scope: all 61 masters (manuscript/vol1 ch01–ch14, vol2 ch15–22, vol3 ch23–29, vol4 ch30–36, vol5 ch37–ch36+, vol6 ch37–44, vol7 ch45–50; field-companion fc1–fc11) — the repo masters, master-of-record."
echo
echo "Method (honest, register-level): pass 1 — a 287-row curated lexicon (727 case-insensitive aliases: formulas, trivial, mineral, brand and product names; word-boundary flags where substring collisions exist) matched on every line of every master; occurrence counts per compound per chapter. Pass 2 — a formula-shaped token sweep over the whole corpus, subtracting lexicon aliases, producing the phase-2 adjudication candidate list (not adjudicated here). Coverage tags — keyword-window, PROVISIONAL: a hit counts when procedure verbs (make/prepare/synthesize/distill/electrolyze/precipitate/calcine/smelt/…), sourcing verbs (buy/shelf/aisle/pharmacy/hardware/label/$/…), or recognition verbs (never/avoid/hazard/toxic/recognition/fence/…) appear within ±3 lines of a compound mention."
echo
echo "Tag classes: \`manufactured+procured\` / \`manufactured\` / \`procured\` (procedure- and/or sourcing-window evidence — the make-or-buy network working as designed); \`recognition-only\` (recognition-window only); \`recognition-only-fence\` (appears ONLY inside the fence chapters — Ch 28 hazard recognition, Ch 50 Cubane — covered BY CHARTER, not a gap); \`MENTIONED-ONLY\` (no window evidence anywhere — the provisional gap class, pending session-187 adjudication)."
echo
echo "Known bounds (never laundered): pass-2 recall is bounded by the lexicon (an unnamed-in-lexicon compound is invisible to pass 1 — the candidate list is the catch-net); keyword-window tagging is proximity, not proof (\"make-or-buy\" lines tag both windows); hydrate formulas contain their anhydrous salts (cross-attribution, e.g. every CuSO4·5H2O mention also counts on the CuSO4 row); two rows share the alias \"ferrioxalate\" (cross-attribution noted); \"bleach\" attributes to NaOCl even on calcium-hypochlorite lines. Water is deliberately not a row (not a procurement problem). Every tag is provisional pending the session-187 adjudication unit."
echo
echo "## A. The register (by category)"
echo
lastcat=""
while IFS=$'\t' read -r rid canon form cat tot nch chap tag; do
  if [ "$cat" != "$lastcat" ]; then echo ""; echo "### Category: $cat"; echo ""; echo "| Compound | Formula | Chapters (mentions) | Total | Tag |"; echo "|---|---|---|---|---|"; lastcat="$cat"; fi
  echo "| $canon | $form | $chap | $tot | $tag |"
done < /tmp/agg.tsv
echo
echo "## B. The MENTIONED-ONLY list (the provisional gap class — session 187's adjudication queue)"
echo
awk -F'\t' '$8=="MENTIONED-ONLY" { print "| " $2 " | " $3 " | " $7 " | " $5 " |" }' /tmp/agg.tsv
echo
echo "## C. Phase-2 candidates (formula-shaped tokens in the corpus, NOT matched by the lexicon — counts are corpus-wide; adjudication pending)"
echo
echo "| Count | Token |"
echo "|---|---|"
head -150 /tmp/cand_final.txt | awk '{ $1=substr($1,1,length($1)); t=$2; print "| " $1 " | " t " |" }'
echo
echo "## D. Per-chapter compound counts"
echo
awk -F'\t' '{ split($2,p,"/"); f=p[length(p)]; sub(/\.md$/,"",f); T[f]+=$3; D[f]++ } END { for(k in T) print "| " k " | " D[k] " | " T[k] " |" }' /tmp/occ.tsv | sort -t'|' -k2
echo
echo "*Register built in-repo by session 186's extractor; every count reproducible from audit/compound-register/occurrences.tsv + lexicon.txt. The register is a records artifact, not a chapter: extend, never rewrite.*"
} > COMPOUND-REGISTER.md
REGSIZE=$(wc -c < COMPOUND-REGISTER.md)
echo "register bytes: $REGSIZE"
if [ "$REGSIZE" -lt 20000 ]; then echo "REGISTER FAIL (too small)"; exit 1; fi

# --- 7. SUMMARY.md (small, for the session record) ---
{
echo "# Compound Register — session-186 summary (for the records)"
echo
NGAP=$(awk -F'\t' '$8=="MENTIONED-ONLY"' /tmp/agg.tsv | wc -l)
NMAN=$(awk -F'\t' '$8=="manufactured"||$8=="manufactured+procured"' /tmp/agg.tsv | wc -l)
NPRO=$(awk -F'\t' '$8=="procured"' /tmp/agg.tsv | wc -l)
NREC=$(awk -F'\t' '$8=="recognition-only"||$8=="recognition-only-fence"' /tmp/agg.tsv | wc -l)
echo "Compounds found: $NAGG (287-row lexicon; 727 aliases). Tags: manufactured/manufactured+procured $NMAN, procured $NPRO, recognition-only (both) $NREC, MENTIONED-ONLY $NGAP. Phase-2 candidates: $NCAND."
echo
echo "## The MENTIONED-ONLY provisional gap list (adjudication queue for session 187)"
echo
awk -F'\t' '$8=="MENTIONED-ONLY" { print $2 " (" $3 ", " $7 ") — " $5 " mentions" }' /tmp/agg.tsv
echo
echo "## Top 40 by total mentions"
echo
sort -t$'\t' -k5,5rn /tmp/agg.tsv | head -40 | awk -F'\t' '{ print $5 " — " $2 " (" $7 ") [" $8 "]" }'
echo
echo "## Phase-2 candidates (top 80)"
echo
head -80 /tmp/cand_final.txt | awk '{ print $1 " — " $2 }'
echo
echo "## Per-category counts"
echo
awk -F'\t' '{ C[$4]++ } END { for(k in C) print k ": " C[k] }' /tmp/agg.tsv | sort
} > SUMMARY.md
SUMSIZE=$(wc -c < SUMMARY.md)
echo "summary bytes: $SUMSIZE"

# --- 8. commit ---
mkdir -p audit/compound-register
cp register-parts/lexicon.txt audit/compound-register/lexicon.txt
cp register-parts/extract.sh audit/compound-register/extract.sh
cp /tmp/occ.tsv audit/compound-register/occurrences.tsv
cp /tmp/agg.tsv audit/compound-register/aggregate.tsv
cp SUMMARY.md audit/compound-register/SUMMARY.md
git config user.name "dsmistral"
git config user.email "deepsudden@gmail.com"
git add COMPOUND-REGISTER.md audit/compound-register
git rm -r -q register-parts || true
git commit -q -m "Session 186: the Compound Register built in-repo (61 masters, 287-row lexicon, ${NAGG} compounds, ${NGAP} mentioned-only provisional gaps, ${NCAND} phase-2 candidates) + the audit evidence pack"
git push
echo "PUSH DONE"
