# Engine 66 transcripts — the Ch 45 Phase-3 adversarial review (session 172)

The seven runs of record, spliced verbatim from the session buffer. Digests (djb2, charCode lane, unpadded hex, over the text without its trailing newline): probe 482e641a; Piece B (Sheet 1 + Sheet 2, blank-line joined in the piece buffer) c58739a7; Sheet 3 part 1 34b4f545; Sheet 3 part 2 2560f746; Sheet 4 (the engine portion, the build-2 rebuild) 93457459; Sheet 6 520fae2. The build-1 Sheet 4 transcript (djb2 3f15c044) was lost at the session's context compaction before it could be byte-archived — the honest-history precedent, disclosed at the sheet itself and in the engine record. At record time the engine's own dispatch text was also gone (the same compaction); the source was re-keyed from the design spec and these frozen transcripts, re-run in full, and reproduced all seven byte-identically — the re-keying credential, recorded in ch45-engine66-src.md.


---

# E66 s0 probe (the modular-witness engine, session 172)
mods (prime by trial division, each < 2^26): 67108859 67108837 67108819 67108777 67108763
P1 PASS invmod identity 7*inv(7)=1 on 5/5 mods
P2 PASS chain 53000/84006 = ef 26500/42003 on 5/5 mods
P3 PASS halfUp edge 1/8@2dp: 13 accepted, 12 rejected
P4 PASS hydrate tokenizer C2H3NaO2·3H2O = C2 H9 Na O5, M 13607877 -> pin 136.079 (k3)
P5 CAUGHT injected ef 26503/42003 vs chain 53000/84006

probe: 4 PASS, 1 CAUGHT, 0 bad

---

# E66 s1 — Sheet 1: compositions re-derived (atom-exact at the 1e5 basis; pin = half-up at 3dp)
C01 C2H4O2 M= 60.05200 -> pin 60.052 PASS
C02 C2H3NaO2 M= 82.03377 -> pin 82.034 PASS
C03 C2H3NaO2·3H2O M= 136.07877 -> pin 136.079 PASS
C04 NaHCO3 M= 84.00577 -> pin 84.006 PASS
C05 H2SO4 M= 98.07200 -> pin 98.072 PASS
C06 Na2SO4 M= 142.03554 -> pin 142.036 PASS
C07 NaHSO4 M= 120.05377 -> pin 120.054 PASS
C08 C4H6O3 M= 102.08900 -> pin 102.089 PASS
C09 C4H8O2 M= 88.10600 -> pin 88.106 PASS
C10 C2H6O2 M= 62.06800 -> pin 62.068 PASS
C11 C2H4O M= 44.05300 -> pin 44.053 PASS
C12 C2H2O M= 42.03700 -> pin 42.037 PASS
C13 C2H3ClO M= 78.49800 -> pin 78.498 PASS
C14 CH4 M= 16.04300 -> pin 16.043 PASS
C15 C3H6O M= 58.08000 -> pin 58.080 PASS
C16 NaCl M= 58.44277 -> pin 58.443 PASS
C17 H2O M= 18.01500 -> pin 18.015 PASS
C18 CO2 M= 44.00900 -> pin 44.009 PASS
C19 C9H8O4 M= 180.15900 -> pin 180.159 PASS
C20 C7H6O3 M= 138.12200 -> pin 138.122 PASS

sheet1: 20/20 PASS; fails: none

---

# E66 s2 — Sheet 2: balances re-derived (atom multisets; pin masses at 1e3; exact masses at 1e5)
B01 vinegar + soda: atoms OK | pin L 144.058 R 144.058 EXACT | exact L 144.05777 R 144.05777 EXACT | frozen 144.058 MATCH PASS
B02 regeneration (excess-acid sulfate): atoms OK | pin L 262.140 R 262.140 EXACT | exact L 262.13954 R 262.13954 EXACT | frozen 262.140 MATCH PASS
B03 regeneration (bisulfate variant): atoms OK | pin L 180.106 R 180.106 EXACT | exact L 180.10577 R 180.10577 EXACT | frozen 180.106 MATCH PASS
B04 dioxane condensation: atoms OK | pin L 124.136 R 124.136 EXACT | exact L 124.13600 R 124.13600 EXACT | frozen 124.136 MATCH PASS
B05 acetaldehyde side-route: atoms OK | pin L 62.068 R 62.068 EXACT | exact L 62.06800 R 62.06800 EXACT | frozen 62.068 MATCH PASS
B06 acetone pyrolysis (ketene): atoms OK | pin L 58.080 R 58.080 EXACT | exact L 58.08000 R 58.08000 EXACT | frozen 58.080 MATCH PASS
B07 ketene + acid = anhydride: atoms OK | pin L 102.089 R 102.089 EXACT | exact L 102.08900 R 102.08900 EXACT | frozen 102.089 MATCH PASS
B08 classic salt + acetyl chloride: atoms OK | pin L 160.532 R 160.532 EXACT | exact L 160.53177 R 160.53177 EXACT | frozen 160.532 MATCH PASS
B09 anhydride hydrolysis: atoms OK | pin L 120.104 R 120.104 EXACT | exact L 120.10400 R 120.10400 EXACT | frozen 120.104 MATCH PASS
B10 net dehydration (the thermodynamic point): atoms OK | pin L 120.104 R 120.104 EXACT | exact L 120.10400 R 120.10400 EXACT | frozen 120.104 MATCH PASS
B11 aspirin door (Ch 34 pin): atoms OK | pin L 240.211 R 240.211 EXACT | exact L 240.21100 R 240.21100 EXACT | frozen 240.211 MATCH PASS
B12 excess-acid bisulfate face: atoms OK | pin L 240.108 R 240.108 EXACT | exact L 240.10754 R 240.10754 EXACT | frozen 240.108 MATCH PASS
B13 hydrate-carried regeneration (N159 reality): atoms OK | pin L 370.230 R 370.230 EXACT | exact L 370.22954 R 370.22954 EXACT | frozen 370.230 MATCH PASS

sheet2: 13/13 PASS; fails: none

---

# E66 s3a — Sheet 3 part 1: the register yield ledgers (L01-L08d)
# Certificate: chain ≡ exactfrac on 5 independently-proven primes (CRT bound >> row magnitudes);
# print lane: the frozen string is the round-half-up of the proven rational at its own k;
# reduced-form witness: no prime < 1000 divides both exactfrac terms.
L01 mol NaHCO3 in the 53-g charge (N159): mods 5/5 | print 0.6309 half-up OK | ef 26500/42003 reduced PASS
L02 theoretical anhydrous NaOAc from it: mods 5/5 | print 51.76 half-up OK | ef 2173901/42003 reduced PASS
L03 43 g on the bicarbonate basis: mods 5/5 | print 83.1 half-up OK | ef 180612900/2173901 reduced PASS
L04a acetic in 350 mL of 10% w/w at rho 1.006 (Ch 4 chain): mods 5/5 | print 35.21 half-up OK | ef 3521/100 reduced PASS
L04b mol acetic on that basis: mods 5/5 | print 0.5863 half-up OK | ef 17605/30026 reduced PASS
L04c theoretical NaOAc on the vinegar basis: mods 5/5 | print 48.10 half-up OK | ef 144420857/3002600 reduced PASS
L04d 43 g on the vinegar basis: mods 5/5 | print 89.4 half-up OK | ef 12911180000/144420857 reduced PASS
L05a mol NaOAc in the 99-g pool (N159): mods 5/5 | print 1.207 half-up OK | ef 49500/41017 reduced PASS
L05b theoretical AcOH from the pool: mods 5/5 | print 72.5 half-up OK | ef 2972574/41017 reduced PASS
L05c 62 g on the regeneration step: mods 5/5 | print 85.6 half-up OK | ef 127152700/1486287 reduced PASS
L06 62 g at rho 1.049 in mL: mods 5/5 | print 59.1 half-up OK | ef 62000/1049 reduced PASS
L07a 48 mL product at rho 1.049 (N212): mods 5/5 | print 50.35 half-up OK | ef 6294/125 reduced PASS
L07b yield on the register 73-g basis: mods 5/5 | print 69.0 half-up OK | ef 25176/365 reduced PASS
L07c yield on the 10% w/w extended basis: mods 5/5 | print 68.6 half-up OK | ef 2517600/36719 reduced PASS
L08a glycol mass: 600 mL at rho 1.113 (N170): mods 5/5 | print 667.8 half-up OK | ef 3339/5 reduced PASS
L08b mol glycol: mods 5/5 | print 10.759 half-up OK | ef 166950/15517 reduced PASS
L08c theoretical dioxane (half the moles): mods 5/5 | print 474.0 half-up OK | ef 147092967/310340 reduced PASS
L08d theoretical volume at rho 1.033: mods 5/5 | print 458.8 half-up OK | ef 7354648350/16029061 reduced PASS

sheet3a: 18/18 PASS; fails: none

---

# E66 s3b rev-2 — Sheet 3 part 2: the register yield ledgers (L09a-L16e)
# rev-1 history: 17/21; four re-keying slips caught by the engine (L12 ef scale, L13a/L13b sum-as-product, L14c scale) — verifier defects, battery vindicated.
L09a 220 mL at his measured rho 1.036: mods 5/5 | print 227.92 half-up OK | ef 5698/25 reduced PASS
L09b yield on the measured-density basis: mods 5/5 | print 48.1 half-up OK | ef 1010467040/21013281 reduced PASS
L09c yield at the tabulated rho 1.033: mods 5/5 | print 47.9 half-up OK | ef 7052786840/147092967 reduced PASS
L10 implied pycnometer product charge (rho_w 0.9982, Ch 44 pin): mods 5/5 | print 10.15 half-up OK | ef 36186/3565 reduced PASS
L11 naive linear water fraction at the 1 C freeze test (N212): mods 5/5 | print 78.0 half-up OK | ef 78/1 reduced PASS
L12 the N271 molten-spheres window: dioxane bp minus Na mp: mods 5/5 | print 3.29 half-up OK | ef 329/100 reduced PASS
L14a azeotrope: mol dioxane per 100 g (82.1 g): mods 5/5 | print 0.932 half-up OK | ef 41050/44053 reduced PASS
L14b azeotrope: mol water per 100 g (17.9 g): mods 5/5 | print 0.994 half-up OK | ef 3580/3603 reduced PASS
L15a mol NaOAc in the 43-g batch (N159): mods 5/5 | print 0.5242 half-up OK | ef 21500/41017 reduced PASS
L15b 1:1 sulfuric for it: mods 5/5 | print 51.41 half-up OK | ef 2108548/41017 reduced PASS
L15c at rho 1.84 in mL: mods 5/5 | print 27.9 half-up OK | ef 1145950/41017 reduced PASS
L15d the stated 36 mL implied-acid moles: mods 5/5 | print 0.6754 half-up OK | ef 360/533 reduced PASS
L15e implied NaOAc covered at 1:1: mods 5/5 | print 55.4 half-up OK | ef 738306/13325 reduced PASS
L16a N270 charge: 300 mL antifreeze at rho 1.113: mods 5/5 | print 333.9 half-up OK | ef 3339/10 reduced PASS
L16b mol glycol: mods 5/5 | print 5.380 half-up OK | ef 83475/15517 reduced PASS
L16c theoretical dioxane from it: mods 5/5 | print 237.0 half-up OK | ef 147092967/620680 reduced PASS
L16d 30 mL acid catalyst mol%: mods 5/5 | print 10.5 half-up OK | ef 6206800/593229 reduced PASS
L16e 40 mL acid catalyst mol%: mods 5/5 | print 14.0 half-up OK | ef 24827200/1779687 reduced PASS
L13a the aspirin door: anhydride + salicylic (sum row): mods 5/5 | print 240.211 half-up OK | ef 240211/1000 reduced PASS
L13b the door out: aspirin + acetic (sum row): mods 5/5 | print 240.211 half-up OK | ef 240211/1000 reduced PASS
L14c azeotrope: mole fraction dioxane (sum row): mods 5/5 | print 0.484 half-up OK | ef 14790315/30561289 reduced PASS

sheet3b: 21/21 PASS; fails: none

---

# E66 s4 — Sheet 4: injection battery (re-keyed from the frozen Engine 65 battery; all rows MUST be CAUGHT)
I01 digit-transposed AcOH pin 61.052 vs computed C2H4O2: CAUGHT [60.052]
I02 digit-transposed dioxane pin 86.106 vs computed C4H8O2: CAUGHT [88.106]
I03 digit-transposed anhydride pin 102.098 vs computed C4H6O3: CAUGHT [102.089]
I04 broken dioxane balance: 2 C2H6O2 -> C4H8O2 + H2O (one water): CAUGHT [multiset C4H12O4 vs C4H10O3; mass 124.136 vs 106.121]
I05 old hand string 51.73 vs exact 53/84.006*82.034: CAUGHT [51.76]
I06 register rounded-intermediate 85.5 vs exact 62/(99/82.034*60.052)*100: CAUGHT [85.6]
I07 digit-transposed trihydrate pin 136.097 vs computed NaC2H3O2·3H2O: CAUGHT [136.079]
I08 swapped-arguments azeotrope mole fraction (dioxane claimed 0.043): CAUGHT [0.484]
I09 digit-transposed ketene pin 42.073 vs computed C2H2O: CAUGHT [42.037]
I10 ketene/acetaldehyde confusion in acetone pyrolysis: C3H6O -> C2H4O + CH4: CAUGHT [multiset C3H6O vs C3H8O]
I11 flat-density vinegar basis (rho 1.000) vs the Ch 4 rho-1.006 chain: CAUGHT [35.21]

sheet4: 11/11 CAUGHT; escapes: none

[Session-172 record note: the build-1 s4 run returned djb2 3f15c044 with 11/11 CAUGHT, no escapes; its verbatim transcript text was lost at the context compaction (the honest-history precedent). This transcript is the build-2 rebuild (determinism sheet, same re-keyed injections, every verdict computed in-run); its djb2 is 93457459. The verdict set is identical: 11/11 CAUGHT; no frozen figure is affected.]

---

# E66 s5a — determinism build 2, part 1 (session 172)

Rebuild of the probe, Sheet 1+2 (Piece B), and Sheet 3 part 1 under a freshly re-derived kernel: the five primes were re-found by trial division just under 2^26 — rediscovered: 67108859 67108837 67108819 67108777 67108763 (identical to build-1's).

Piece djb2 comparison (build-1 recorded at the piece runs; build-2 from the rebuild):
- probe: build-1 482e641a, build-2 482e641a — BYTE-IDENTICAL
- s1+s2 (Piece B): build-1 c58739a7, build-2 c58739a7 — BYTE-IDENTICAL
- s3a: build-1 34b4f545, build-2 34b4f545 — BYTE-IDENTICAL

determinism build-2 part 1: 3/3 parts byte-identical; no divergence.

# E66 s5b — determinism build 2, part 2 (session 172)

Rebuild of s3b rev-2 and s4 under the same fresh kernel.

s3b rev-2: the first rebuild attempt ran 15/21 — the engine CAUGHT four re-keying slips in the rebuild's own chains (L10 missing the x10000/[100,1000] scale; L16b missing the /10; L13a/L13b gram terms written at the 1e-5 basis instead of /1000). All four were verifier transcription defects; the frozen exactfracs were untouched. After the chain corrections the rebuild ran 21/21 PASS with djb2 2560f746 — BYTE-IDENTICAL to build-1 (2560f746).

s4: build-1 returned djb2 3f15c044, 11/11 CAUGHT, no escapes; its verbatim transcript was lost at the context compaction and could not be byte-compared (disclosed; the honest-history precedent). The build-2 rebuild re-keyed the same eleven injections from the frozen Engine 65 battery and re-computed every verdict in-run: 11/11 CAUGHT, no escapes; build-2 djb2 93457459. Verdict set identical; transcript not byte-compared — recorded as such.

determinism build-2 part 2: s3b byte-identical; s4 verdict-identical (transcript loss disclosed).

determinism overall: 4/5 pieces byte-identical (probe, s1+s2, s3a, s3b); s4 verdict-identical with the build-1 transcript lost at compaction; zero effect on any frozen figure.

---

# E66 s6 rev-2 — Sheet 6: the review rows (the skeptic findings, machine-verified)
# rev-1 history: 20/25 — five caught by the engine: three verifier chain slips (R02a/R02b missing
# the 98.072 x1000 scale, R04b with the 10 on the wrong side) and two candidate-print corrections where
# the machine overruled the session's own hand numbers (R03c 99.70 → 99.72, R03g 44.12 → 44.13).
# Each chain is a re-derivation from first principles; the claimed print is the finding's number;
# PASS = the claimed print is the round-half-up of the exact chain value at its own k, with the
# residue certificate (chain = reduced ef on 5 independently-proven primes) and the reduced-form witness.
R01a the literal pycnometer division 9.78/0.9982 (mL of bottle volume): mods 5/5 | print 9.7976 half-up OK | ef 48900/4991 reduced PASS
R01b the full round-trip 9.78 x 1.036 / 0.9982 (g of dioxane): mods 5/5 | print 10.15 half-up OK | ef 36186/3565 reduced PASS | frozen L10 5/5
R02a the 36-mL charge priced at the 96% reagent (mol acid): mods 5/5 | print 0.6484 half-up OK | ef 1728/2665 reduced PASS
R02b implied NaOAc covered at 1:1 on the 96% basis (g): mods 5/5 | print 53.2 half-up OK | ef 17719344/333125 reduced PASS
R03a mass of AcOH in 48 mL of 98% at rho 1.049 (g): mods 5/5 | print 49.345 half-up OK | ef 154203/3125 reduced PASS
R03b the 100-g anhydrous goal priced in AcOH demand (g): mods 5/5 | print 73.20 half-up OK | ef 3002600/41017 reduced PASS
R03c NaOAc makeable from the shown 73 g of AcOH (g): mods 5/5 | print 99.72 half-up OK | ef 2994241/30026 reduced PASS
R03d the goal-vs-available plan ratio (the honest one): mods 5/5 | print 1.003 half-up OK | ef 3002600/2994241 reduced PASS
R03e the printed 1.37 decomposed: 100 g salt goal over 73 g acid: mods 5/5 | print 1.370 half-up OK | ef 100/73 reduced PASS
R03f 100 g trihydrate priced as anhydrous (g): mods 5/5 | print 60.28 half-up OK | ef 8203400/136079 reduced PASS
R03g AcOH carried by the trihydrate goal (g): mods 5/5 | print 44.13 half-up OK | ef 6005200/136079 reduced PASS
R03h the trihydrate goal as 98% product (mL): mods 5/5 | print 42.9 half-up OK | ef 300260000000/6994596679 reduced PASS
R03i the trihydrate goal as 85% product (mL): mods 5/5 | print 49.5 half-up OK | ef 120104000000/2426696807 reduced PASS
R03j the near-pure linear freeze of a true 98% acid (C): mods 5/5 | print 12.6 half-up OK | ef 63/5 reduced PASS
R04a the linear tangent slope (C per 1% water): mods 5/5 | print 2.0 half-up OK | ef 2/1 reduced PASS
R04b the average curve slope 0-15% water (C per 1%): mods 5/5 | print 1.04 half-up OK | ef 26/25 reduced PASS
R04c the molality of 0.1% w/w water in AcOH (mol/kg): mods 5/5 | print 0.0556 half-up OK | ef 200000/3599397 reduced PASS
R04d the Kf tangent at 0.1% water (C): mods 5/5 | print 0.2167 half-up OK | ef 260000/1199799 reduced PASS
R05a water in 48 mL of product at 95% (mL): mods 5/5 | print 2.52 half-up OK | ef 1007/400 reduced PASS
R05b at 98% (mL): mods 5/5 | print 1.01 half-up OK | ef 1007/1000 reduced PASS
R05c at 90% (mL): mods 5/5 | print 5.04 half-up OK | ef 1007/200 reduced PASS
R05d at 85% (mL): mods 5/5 | print 7.55 half-up OK | ef 3021/400 reduced PASS
R06a the 150-mL charge over the 1:1 demand (L15c): mods 5/5 | print 5.4 half-up OK | ef 500/93 reduced PASS
R06b the 150-mL charge over the stated 36-mL plan: mods 5/5 | print 4.2 half-up OK | ef 25/6 reduced PASS
R07 the frozen L15d basis named: 36 mL at rho 1.84, 100% acid (mol): mods 5/5 | print 0.6754 half-up OK | ef 360/533 reduced PASS | frozen L15d 5/5

sheet6: 25/25 PASS; fails: none

---
