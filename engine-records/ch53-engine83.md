# Engine 83 — E83-MC — design and verdict (session 198, Vol VIII Ch 53)

**Engine 83** — the modular cross-check engine, fresh, sharing zero code with Engines 1–82.
Design: every identity verified in three independent lanes — (L1) the exact integer lane,
all masses in integer my-units (mg/mol), every division printing an integer witness triple
[q, r, d]; (L2) modulo p1 = 65537; (L3) modulo p2 = 1000003 — with the two modular residues
required to be mutually consistent with the integer lane. No recursion anywhere (the formula
parser is an iterative character walk over an explicit group stack); no BigInt; no floats
in any value path. The display paradigm is truncation-with-witness (the half-up printed as
a comparison display only) — deliberately distinct from Engine 82's round-half-up display
paradigm and Engine 81's double-entry and Engine 80's integer-lane ledger: the fourth
distinct verification paradigm in the series, chosen so a corruption invisible to one prime
is caught by the second and by the exact lane, which the J4 injection demonstrated live:
the +65537 corruption left the mod-65537 residue unchanged (the single-prime design would
have passed it), the mod-1000003 lane and the integer lane both caught it.

The battery, split into pieces per the binding runtime constraints, each piece's output
frozen to scratch with md5 receipts before any splice, never retyped; the design source
written to disk (src.txt, md5 b8613fd6944fdc9bcd32d66ce6fb532f) BEFORE any run — the
Engine 82 source-loss lesson made procedural. The honest history, entire: probe rev-2 PASS
5/5 (rev-1: one harness defect, the census line sweeping the header into the every-PASS
check); molar book rev-1 22/22 PASS first run; balance book rev-1 7/7 PASS first run;
dose/economics rev-2 15/15 PASS plus the D12 honest-gap row PASS by refusal (rev-1 8/15 —
seven FAILs, every one harness-side: four percent rows missing their ×100, D13
double-scaled, the display helper at the wrong decimal place, and two expectation
hand-slips at D9 and D10 where the engine had been right all along, 1538 and 9999 — the
value path defect-free in every run); injections rev-1 4/4 CAUGHT; determinism rev-3 PASS,
both runs byte-identical, sdbm 820233240 (rev-1: the precedence ternary that collapsed to
an unconditional PASS; rev-2: the compact mirror omitting the 10^dp scaling on four dose
rows, the frozen main sheet standing 15/15 throughout).

Verdict: **PASS**. The figures this chapter's prose prints are the battery's rows: the
molar book (22 compounds, citric acid 192.12/210.14, trisodium citrate 258.07/294.10,
calcium citrate 498.43, gypsum 172.17, the starch unit 162.14, glucose 180.16, vanillin
152.15, guaiacol 124.14, glyoxylic acid 74.04, VMA 198.17, DCM 84.93, eugenol 164.20), the
balance book (B1–B7, from the citric neutralization through the starch hydrolysis to the
guaiacol route's oxidative decarboxylation), and the dose/economics audit (the 21.91 g
theoretical and the 82.6 percent register figure behind the video's stated 83; the 92.9
methanol recovery; the 0.93 wt% vanilla-sugar yield; the 10–40 percent brand-range band;
the 15.38× Madagascar peak multiple; the FDA unit at 99.99 g of beans per liter; the 4.86
g/100 mL citric premise inside the convergent 4.5–5 band; and the starch axis's honest gap
honored by refusal — 47 g stated, input mass unstated, no recovery fabricated).

The transcripts, Outputs Verbatim, and the receipts: ch53-engine83-transcripts.md. The
as-run source: ch53-engine83-src.md.
