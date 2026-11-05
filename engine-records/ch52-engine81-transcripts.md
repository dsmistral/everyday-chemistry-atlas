# Engine 81 — Chapter 52, Lab 52.2 — The Transcripts (Outputs Verbatim)

Session 195 (2026-11-05). Engine 81-DE, the double-entry engine: a fresh build, zero code shared with Engines 1–80. The five frozen pieces below are the binding evidence, embedded verbatim; each block md5-gated against its frozen scratch receipt at splice time (the gate run in the same pass as this push). Digest convention: md5 over the artifact as frozen (trailing newline included); sdbm(body) over the body excluding the digest tail line (h = c + (h<<6) + (h<<16) − h, UTF-8 bytes, |0 lane, printed >>>0). The bodies' own md5s, the second gate: probe 718 B (a26aa91df73073942abbfc1dec46a788); Sheet 1 2,252 B (33f14e8b3d4bc5fcfee317f0d0776b1c); Sheet 2 1,914 B (93aa347a29fa78eab14353055215b0fc); Sheet 3 1,801 B (b810441fc0f01266f01b8710df9bea15); Sheet 4 1,609 B (092341a35f64cd82f39b6f19e6fb1caf).

## The probe

```
=== E81-DE PROBE (pre-flight, 5 rows, 3 injections) ===
P1 add: 234343 + 36458 = 270801 [inverse: r-36458=234343, r-234343=36458]
P1-INJ harness expected 270802 -> CAUGHT (engine: 270801, verified by inverse both lanes)
P2 mul: 6500 x 270801 = 1760206500 [inverse: r/270801=6500, r/6500=270801]
P3 divmod: 1760206500 / 234343 -> q=7511 r=56227 [witness: q*d+r=1760206500 == n]
P3-INJ harness expected r=56228 -> CAUGHT (engine r=56227, witness triple holds)
P4 parse "C14H22N2O.ClH" -> H23C14N2O1Cl1 molar=270801
P4-INJ harness expected H22 -> CAUGHT (engine H=23: the salt proton counted)
P5 element table: Bi=208980 held; 208980 + 1008 = 209988 [inverse ok]
PROBE VERDICT: 5/5 rows, 3/3 injections CAUGHT, deFails=0
sdbm(body)=4028545b
```

## Sheet 1 — the molar book

```
=== E81-DE SHEET 1: THE MOLAR BOOK (the shelf ledger, 13 rows at rev-1) ===
convention: my computed from the held element table (my = mg/mol x 1000); every add/mul inverse-checked (deFails must stay 0); printed = q + "." + r from divmod(my, 1000), witness tripled; published gate |my - pub| <= 10 (0.01 g/mol)
lidocaine | C14H22N2O -> H22C14N2O1 | my=234343 | printed 234.343 [witness 234x1000+343=234343] | |my-pub|=3 PASS | MATCH
lidocaine hydrochloride | C14H22N2O.ClH -> H23C14N2O1Cl1 | my=270801 | printed 270.801 [witness 270x1000+801=270801] | |my-pub|=1 PASS | MATCH
MEGX | C12H18N2O -> H18C12N2O1 | my=206289 | printed 206.289 [witness 206x1000+289=206289] | |my-pub|=9 PASS | MATCH
2,6-dimethylaniline (xylidine) | C8H11N -> H11C8N1 | my=121183 | printed 121.183 [witness 121x1000+183=121183] | |my-pub|=3 PASS | MATCH
chloroacetyl chloride | C2H2Cl2O -> H2C2O1Cl2 | my=112937 | printed 112.937 [witness 112x1000+937=112937] | |my-pub|=3 PASS | MATCH
chloroacetamide (the N-(2,6-dimethylphenyl) intermediate) | C10H12ClNO -> H12C10N1O1Cl1 | my=197662 | printed 197.662 [witness 197x1000+662=197662] | |my-pub|=2 PASS | MATCH
diethylamine | C4H11N -> H11C4N1 | my=73139 | printed 73.139 [witness 73x1000+139=73139] | |my-pub|=1 PASS | MATCH
benzocaine | C9H11NO2 -> H11C9N1O2 | my=165192 | printed 165.192 [witness 165x1000+192=165192] | |my-pub|=2 PASS | MATCH
procaine | C13H20N2O2 -> H20C13N2O2 | my=236315 | printed 236.315 [witness 236x1000+315=236315] | |my-pub|=5 PASS | MATCH
PABA (4-aminobenzoic acid) | C7H7NO2 -> H7C7N1O2 | my=137138 | printed 137.138 [witness 137x1000+138=137138] | |my-pub|=2 PASS | MATCH
diethylaminoethanol (DEAE) | C6H15NO -> H15C6N1O1 | my=117192 | printed 117.192 [witness 117x1000+192=117192] | |my-pub|=2 PASS | MATCH
cocaine | C17H21NO4 -> H21C17N1O4 | my=303358 | printed 303.358 [witness 303x1000+358=303358] | |my-pub|=8 PASS | MATCH
diethylamine hydrochloride | C4H11N.ClH -> H12C4N1Cl1 | my=109597 | printed 109.597 [witness 109x1000+597=109597] | no published gate (balance-lane only) | MATCH
INJECTION row (MEGX, harness expectation 206298) -> CAUGHT (engine 206289, digit-slip caught; engine verified by inverse lanes)
SHEET 1 VERDICT: 13/13 rows MATCH, injections caught 1, deFails=0 (must be 0)
sdbm(body)=d751a36b
```

## Sheet 2 — the balance book

```
=== E81-DE SHEET 2: THE BALANCE BOOK (7 balances at rev-1) ===
convention: mass lanes summed add()-verified both sides; element counts merged per side then compared; every balance must hold on counts AND mass
B1 C13H20N2O2 + H2O -> C7H7NO2 + C6H15NO | L my=254330 R my=254330 | counts L=H22C13N2O3 R=H22C13N2O3 | counts BALANCED mass BALANCED | MATCH | procaine + water -> PABA + DEAE (the ester hydrolysis)
B2 C14H22N2O -> C12H18N2O + C2H4 | L my=234343 R my=234343 | counts L=H22C14N2O1 R=H22C14N2O1 | counts BALANCED mass BALANCED | MATCH | lidocaine -> MEGX + C2H4 (formal mass bookkeeping only; in vivo the ethyl is oxidized further, not free ethylene)
B3 C14H22N2O + ClH -> C14H22N2O.ClH | L my=270801 R my=270801 | counts L=H23C14N2O1Cl1 R=H23C14N2O1Cl1 | counts BALANCED mass BALANCED | MATCH | lidocaine + HCl -> lidocaine hydrochloride (the salt)
B4 C9H11NO2 + H2O -> C7H7NO2 + C2H6O | L my=183207 R my=183207 | counts L=H13C9N1O3 R=H13C9N1O3 | counts BALANCED mass BALANCED | MATCH | benzocaine + water -> PABA + ethanol (the ester hydrolysis)
B5 C8H11N + C2H2Cl2O -> C10H12ClNO + ClH | L my=234120 R my=234120 | counts L=H13C10N1O1Cl2 R=H13C10N1O1Cl2 | counts BALANCED mass BALANCED | MATCH | xylidine + chloroacetyl chloride -> chloroacetamide + HCl (arrow one, NAMED not transcribed)
B6 C10H12ClNO + C4H11N + C4H11N -> C14H22N2O + C4H11N.ClH | L my=343940 R my=343940 | counts L=H34C18N3O1Cl1 R=H34C18N3O1Cl1 | counts BALANCED mass BALANCED | MATCH | chloroacetamide + 2 diethylamine -> lidocaine + diethylamine.HCl (arrow two, NAMED not transcribed)
B7 the family read: PABA present in B1 products=true, in B4 products=true, in B2 (amide) products=false | CLASSIFICATION CONFIRMED: esters hydrolyze to PABA, the amide does not
INJECTION row (B3, harness expectation L=270802) -> CAUGHT (engine L=270801)
SHEET 2 VERDICT: 7/7 balances hold on counts and mass, injection caught, deFails=0 (must be 0)
sdbm(body)=e13e9e27
```

## Sheet 3 — the dose/economics book (rev-2)

```
=== E81-DE SHEET 3: THE DOSE/ECONOMICS BOOK (5 rows at rev-2) ===
rev-2 note (freeze discipline): run-1 carried three harness-side slips the engine exposed - the D1 unit label printed g for an mg value, the D4 text said ~9.14 for 6500/700=~9.29, and the D4 injection was mis-armed (stated 200, the TRUE remainder, and so missed); rev-2 fixes the labels and re-arms the injection at the original mistaken hand value 100; the engine value path identical and defect-free in both revs (deFails=0); no check moved
convention: every division returns the witness triple (q, r) with q*d+r==n verified; all lanes integer, no floats in the value path
D1 the salt-form conversion: 6500 mg lidocaine freebase x (270801/234343) -> n=1760206500 = 7511 + 56227/234343 [witness 7511x234343+56227=1760206500 == n] => ~7511.24 mg lidocaine.HCl-equivalent (~7.51 g)
D2 the OTC-tube equivalence: 6500 mg / 1200 mg-per-30g-tube (4% gel) -> q=5 r=500 [witness 5x1200+500=6500] => 5 tubes + 500 mg, ~5.42 tube-equivalents
D3 the product lower bound: 6500 mg / 50 mg-per-g (5% product) -> q=130 r=0 [witness 130x50+0=6500] => >= 130 g of 5% product at 100% recovery (N383 honest zero: no input masses, true yield% unknowable)
D4 the Rx-patch load: 6500 mg / 700 mg-per-patch (5% Lidoderm, Rx) -> q=9 r=200 [witness 9x700+200=6500] => ~9.28 patch loads
D5 the make-or-buy verdict: BUY - the 4% OTC gel carries the active at ~1.2 g per 30-g tube; ~5.4 tubes cover 6.5 g; the extraction (N383) is the demonstration, not the economical route (its economics unpriceable: no denominator)
INJECTION row (D4, harness expectation r=100) -> CAUGHT (engine r=200, the run-1 mistaken hand value now correctly serving as the injection; witness triple holds)
SHEET 3 VERDICT (rev-2): 5/5 rows, injections caught 1/1, deFails=0 (must be 0)
sdbm(body)=36959f2a
```

## Sheet 4 — determinism

```
=== E81-DE SHEET 4: DETERMINISM (two independent passes, reversed iteration orders) ===
DET lidocaine: pass1=234343 pass2=234343 -> MATCH
DET lidocaine hydrochloride: pass1=270801 pass2=270801 -> MATCH
DET MEGX: pass1=206289 pass2=206289 -> MATCH
DET 2,6-dimethylaniline (xylidine): pass1=121183 pass2=121183 -> MATCH
DET chloroacetyl chloride: pass1=112937 pass2=112937 -> MATCH
DET chloroacetamide (the N-(2,6-dimethylphenyl) intermediate): pass1=197662 pass2=197662 -> MATCH
DET diethylamine: pass1=73139 pass2=73139 -> MATCH
DET benzocaine: pass1=165192 pass2=165192 -> MATCH
DET procaine: pass1=236315 pass2=236315 -> MATCH
DET PABA (4-aminobenzoic acid): pass1=137138 pass2=137138 -> MATCH
DET diethylaminoethanol (DEAE): pass1=117192 pass2=117192 -> MATCH
DET cocaine: pass1=303358 pass2=303358 -> MATCH
DET diethylamine hydrochloride: pass1=109597 pass2=109597 -> MATCH
DET B1 mass: pass1 L=254330 R=254330 | pass2 L=254330 R=254330 -> MATCH
DET B2 mass: pass1 L=234343 R=234343 | pass2 L=234343 R=234343 -> MATCH
DET B3 mass: pass1 L=270801 R=270801 | pass2 L=270801 R=270801 -> MATCH
DET B4 mass: pass1 L=183207 R=183207 | pass2 L=183207 R=183207 -> MATCH
DET B5 mass: pass1 L=234120 R=234120 | pass2 L=234120 R=234120 -> MATCH
DET B6 mass: pass1 L=343940 R=343940 | pass2 L=343940 R=343940 -> MATCH
DET dose 1760206500/234343: pass1=(7511,56227) pass2=(7511,56227) -> MATCH
DET dose 6500/1200: pass1=(5,500) pass2=(5,500) -> MATCH
DET dose 6500/50: pass1=(130,0) pass2=(130,0) -> MATCH
DET dose 6500/700: pass1=(9,200) pass2=(9,200) -> MATCH
DETERMINISM VERDICT: 23/23 MATCH, deFails=0 (must be 0)
sdbm(body)=912c192f
```

## The receipts

| Piece | Artifact size | Artifact md5 | Body md5 | sdbm(body) |
|---|---|---|---|---|
| probe | 738 B | 2b68065d88be659604f646de718485d9 | a26aa91df73073942abbfc1dec46a788 | 4028545b |
| Sheet 1 | 2,272 B | 97b250868fecb92871bf7a8bf1ca6df7 | 33f14e8b3d4bc5fcfee317f0d0776b1c | d751a36b |
| Sheet 2 | 1,934 B | 399805263149c5e4549eab52336dbac8 | 93aa347a29fa78eab14353055215b0fc | e13e9e27 |
| Sheet 3 | 1,821 B | 6caa6401cfc656718c1abd4575548015 | b810441fc0f01266f01b8710df9bea15 | 36959f2a |
| Sheet 4 | 1,629 B | 7b4938af99d40aba0ff24754e737d599 | 092341a35f64cd82f39b6f19e6fb1caf | 912c192f |

8,394 B of transcript total. The design and verdict record (ch52-engine81.md) and the source record (ch52-engine81-src.md — the source preserved this session, the Engine 80 full-loss event not repeated) complete the set.
