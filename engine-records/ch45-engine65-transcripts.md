# Engine 65 — the six run transcripts, spliced verbatim (session 171, the Ch 45 Solvent Shelf authoring)

The buffer files e65-s0-probe.md through e65-s5-determinism.md are the runs of record. They are spliced here in run order, byte-for-byte, each with its own header line. The chapter master (manuscript/vol7/ch45.md) splices the same outputs into Labs 45.1 and 45.2; the engine record (ch45-engine65.md) carries the design and the honest run history; the source (ch45-engine65-src.md) is the re-keyed, re-verified regeneration credential.

# E65 s0 probe (the rational-tape engine, session 171)

P1 PASS 1/3+1/6=1/2
P2 PASS rPr: 0.6667 0.125 60.053
P3 PASS CH3COOH=60.052
P4 PASS reparse round-trip C2H4O2 vs CH3COOH
P5 CAUGHT injected 60.522 vs true 60.052

probe: 4 PASS, 1 CAUGHT, 0 bad

# E65 s1 rev-2 — Sheet 1: compositions (H1 fixed: hydrate segments; probe gap H1 disclosed — the s0 probe never tested the hydrate form)
HP PASS hydrate regression C2H3NaO2·3H2O = 136.079
C01 C2H4O2 M= 60.052 exp 60.052 PASS
C02 C2H3NaO2 M= 82.034 exp 82.034 PASS
C03 C2H3NaO2·3H2O M= 136.079 exp 136.079 PASS
C04 NaHCO3 M= 84.006 exp 84.006 PASS
C05 H2SO4 M= 98.072 exp 98.072 PASS
C06 Na2SO4 M= 142.036 exp 142.036 PASS
C07 NaHSO4 M= 120.054 exp 120.054 PASS
C08 C4H6O3 M= 102.089 exp 102.089 PASS
C09 C4H8O2 M= 88.106 exp 88.106 PASS
C10 C2H6O2 M= 62.068 exp 62.068 PASS
C11 C2H4O M= 44.053 exp 44.053 PASS
C12 C2H2O M= 42.037 exp 42.037 PASS
C13 C2H3ClO M= 78.498 exp 78.498 PASS
C14 CH4 M= 16.043 exp 16.043 PASS
C15 C3H6O M= 58.080 exp 58.080 PASS
C16 NaCl M= 58.443 exp 58.443 PASS
C17 H2O M= 18.015 exp 18.015 PASS
C18 CO2 M= 44.009 exp 44.009 PASS
C19 C9H8O4 M= 180.159 exp 180.159 PASS
C20 C7H6O3 M= 138.122 exp 138.122 PASS

sheet1 rev-2: 20/20 PASS; fails: none

# E65 s2 — Sheet 2: balances, atom multisets + exact mass ledgers
B01 vinegar + soda: atoms OK | mass L 144.058 R 144.058 EXACT
B02 regeneration (excess-acid sulfate): atoms OK | mass L 262.140 R 262.140 EXACT
B03 regeneration (bisulfate variant): atoms OK | mass L 180.106 R 180.106 EXACT
B04 dioxane condensation: atoms OK | mass L 124.136 R 124.136 EXACT
B05 acetaldehyde side-route: atoms OK | mass L 62.068 R 62.068 EXACT
B06 acetone pyrolysis (ketene): atoms OK | mass L 58.080 R 58.080 EXACT
B07 ketene + acid = anhydride: atoms OK | mass L 102.089 R 102.089 EXACT
B08 classic salt + acetyl chloride: atoms OK | mass L 160.532 R 160.532 EXACT
B09 anhydride hydrolysis: atoms OK | mass L 120.104 R 120.104 EXACT
B10 net dehydration (the thermodynamic point): atoms OK | mass L 120.104 R 120.104 EXACT
B11 aspirin door (Ch 34 pin): atoms OK | mass L 240.211 R 240.211 EXACT
B12 excess-acid bisulfate face: atoms OK | mass L 240.108 R 240.108 EXACT
B13 hydrate-carried regeneration (N159 reality): atoms OK | mass L 370.230 R 370.230 EXACT

sheet2: 13/13 PASS; fails: none

# E65 s3 rev-2 — Sheet 3: the register yield ledgers
# Expected strings from an INDEPENDENT float witness path (plain formulas, .toFixed),
# superseding the lost hand-derived dispatch (30/39; the 9 disagreements were hand-transcription
# defects — the engine was vindicated on each by the witness).
L01 mol NaHCO3 in the 53-g charge (N159): exact=0.6309 witness=0.6309 PASS exactfrac=26500/42003
L02 theoretical anhydrous NaOAc from it: exact=51.76 witness=51.76 PASS exactfrac=2173901/42003
L03 43 g on the bicarbonate basis: exact=83.1 witness=83.1 PASS exactfrac=180612900/2173901
L04a acetic in 350 mL of 10% w/w at rho 1.006 (Ch 4 chain): exact=35.21 witness=35.21 PASS exactfrac=3521/100
L04b mol acetic on that basis: exact=0.5863 witness=0.5863 PASS exactfrac=17605/30026
L04c theoretical NaOAc on the vinegar basis: exact=48.10 witness=48.10 PASS exactfrac=144420857/3002600
L04d 43 g on the vinegar basis: exact=89.4 witness=89.4 PASS exactfrac=12911180000/144420857
L05a mol NaOAc in the 99-g pool (N159): exact=1.207 witness=1.207 PASS exactfrac=49500/41017
L05b theoretical AcOH from the pool: exact=72.5 witness=72.5 PASS exactfrac=2972574/41017
L05c 62 g on the regeneration step: exact=85.6 witness=85.6 PASS exactfrac=127152700/1486287
L06 62 g at rho 1.049 in mL: exact=59.1 witness=59.1 PASS exactfrac=62000/1049
L07a 48 mL product at rho 1.049 (N212): exact=50.35 witness=50.35 PASS exactfrac=6294/125
L07b yield on the register 73-g basis: exact=69.0 witness=69.0 PASS exactfrac=25176/365
L07c yield on the 10% w/w extended basis: exact=68.6 witness=68.6 PASS exactfrac=2517600/36719
L08a glycol mass: 600 mL at rho 1.113 (N170): exact=667.8 witness=667.8 PASS exactfrac=3339/5
L08b mol glycol: exact=10.759 witness=10.759 PASS exactfrac=166950/15517
L08c theoretical dioxane (half the moles): exact=474.0 witness=474.0 PASS exactfrac=147092967/310340
L08d theoretical volume at rho 1.033: exact=458.8 witness=458.8 PASS exactfrac=7354648350/16029061
L09a 220 mL at his measured rho 1.036: exact=227.92 witness=227.92 PASS exactfrac=5698/25
L09b yield on the measured-density basis: exact=48.1 witness=48.1 PASS exactfrac=1010467040/21013281
L09c yield at the tabulated rho 1.033: exact=47.9 witness=47.9 PASS exactfrac=7052786840/147092967
L10 implied pycnometer product charge (rho_w 0.9982, Ch 44 pin): exact=10.15 witness=10.15 PASS exactfrac=36186/3565
L11 naive linear water fraction at the 1 C freeze test (N212): exact=78.0 witness=78.0 PASS exactfrac=78/1
L12 the N271 molten-spheres window: dioxane bp minus Na mp: exact=3.29 witness=3.29 PASS exactfrac=329/100
L13a the aspirin door: anhydride + salicylic: exact=240.211 witness=240.211 PASS exactfrac=240211/1000
L13b the door out: aspirin + acetic: exact=240.211 witness=240.211 PASS exactfrac=240211/1000
L14a azeotrope: mol dioxane per 100 g (82.1 g): exact=0.932 witness=0.932 PASS exactfrac=41050/44053
L14b azeotrope: mol water per 100 g (17.9 g): exact=0.994 witness=0.994 PASS exactfrac=3580/3603
L14c azeotrope: mole fraction dioxane: exact=0.484 witness=0.484 PASS exactfrac=14790315/30561289
L15a mol NaOAc in the 43-g batch (N159): exact=0.5242 witness=0.5242 PASS exactfrac=21500/41017
L15b 1:1 sulfuric for it: exact=51.41 witness=51.41 PASS exactfrac=2108548/41017
L15c at rho 1.84 in mL: exact=27.9 witness=27.9 PASS exactfrac=1145950/41017
L15d the stated 36 mL implied-acid moles: exact=0.6754 witness=0.6754 PASS exactfrac=360/533
L15e implied NaOAc covered at 1:1: exact=55.4 witness=55.4 PASS exactfrac=738306/13325
L16a N270 charge: 300 mL antifreeze at rho 1.113: exact=333.9 witness=333.9 PASS exactfrac=3339/10
L16b mol glycol: exact=5.380 witness=5.380 PASS exactfrac=83475/15517
L16c theoretical dioxane from it: exact=237.0 witness=237.0 PASS exactfrac=147092967/620680
L16d 30 mL acid catalyst mol%: exact=10.5 witness=10.5 PASS exactfrac=6206800/593229
L16e 40 mL acid catalyst mol%: exact=14.0 witness=14.0 PASS exactfrac=24827200/1779687

sheet3 rev-2: 39/39 PASS; fails: none
corrected hand-defects: L01→0.6309 L02→51.76 L04c→48.10 L05c→85.6 L09c→47.9 L14a→0.932 L15b→51.41 L15d→0.6754 L16b→5.380

# E65 s4 — Sheet 4: injection battery (all rows MUST be CAUGHT)
I01 digit-transposed AcOH pin 61.052 vs computed C2H4O2: CAUGHT [60.052]
I02 digit-transposed dioxane pin 86.106 vs computed C4H8O2: CAUGHT [88.106]
I03 digit-transposed anhydride pin 102.098 vs computed C4H6O3: CAUGHT [102.089]
I04 broken dioxane balance: 2 C2H6O2 -> C4H8O2 + H2O (one water): CAUGHT [multiset C4H12O4 vs C4H10O3; mass 124.136 vs 106.121]
I05 old hand string 51.73 vs exact 53/84.006*82.034: CAUGHT [51.76]
I06 register rounded-intermediate 85.5 vs exact 62/(99/82.034*60.052)*100: CAUGHT [85.6]
I07 digit-transposed trihydrate pin 136.097 vs computed NaC2H3O2·3H2O: CAUGHT [136.079]
I08 swapped-arguments azeotrope mole fraction (dioxane claimed 0.043): CAUGHT [0.043]
I09 digit-transposed ketene pin 42.073 vs computed C2H2O: CAUGHT [42.037]
I10 ketene/acetaldehyde confusion in acetone pyrolysis: C3H6O -> C2H4O + CH4: CAUGHT [multiset C3H6O vs C3H8O]
I11 flat-density vinegar basis (rho 1.000) vs the Ch 4 rho-1.006 chain: CAUGHT [35.00]

sheet4: 11/11 CAUGHT; escapes: none

# E65 s5 — full battery transcript (determinism build)
C01 C2H4O2: 60.052 PASS
C02 NaC2H3O2: 82.034 PASS
C03 NaC2H3O2·3H2O: 136.079 PASS
C04 NaHCO3: 84.006 PASS
C05 H2SO4: 98.072 PASS
C06 Na2SO4: 142.036 PASS
C07 NaHSO4: 120.054 PASS
C08 C4H6O3: 102.089 PASS
C09 C4H8O2: 88.106 PASS
C10 C2H6O2: 62.068 PASS
C11 C2H4O: 44.053 PASS
C12 C2H2O: 42.037 PASS
C13 C2H3ClO: 78.498 PASS
C14 CH4: 16.043 PASS
C15 C3H6O: 58.080 PASS
C16 NaCl: 58.443 PASS
C17 H2O: 18.015 PASS
C18 CO2: 44.009 PASS
C19 C9H8O4: 180.159 PASS
C20 C7H6O3: 138.122 PASS
L01: 0.6309 PASS
L02: 51.76 PASS
L03: 83.1 PASS
L04a: 35.21 PASS
L04b: 0.5863 PASS
L04c: 48.10 PASS
L04d: 89.4 PASS
L05a: 1.207 PASS
L05b: 72.5 PASS
L05c: 85.6 PASS
L06: 59.1 PASS
L07a: 50.35 PASS
L07b: 69.0 PASS
L07c: 68.6 PASS
L08a: 667.8 PASS
L08b: 10.759 PASS
L08c: 474.0 PASS
L08d: 458.8 PASS
L09a: 227.92 PASS
L09b: 48.1 PASS
L09c: 47.9 PASS
L10: 10.15 PASS
L11: 78.0 PASS
L12: 3.29 PASS
L13a: 240.211 PASS
L13b: 240.211 PASS
L14a: 0.932 PASS
L14b: 0.994 PASS
L14c: 0.484 PASS
L15a: 0.5242 PASS
L15b: 51.41 PASS
L15c: 27.9 PASS
L15d: 0.6754 PASS
L15e: 55.4 PASS
L16a: 333.9 PASS
L16b: 5.380 PASS
L16c: 237.0 PASS
L16d: 10.5 PASS
L16e: 14.0 PASS
I01: CAUGHT
I02: CAUGHT
I03: CAUGHT
I04: CAUGHT
I05: CAUGHT
I06: CAUGHT
I07: CAUGHT
I08: CAUGHT
I09: CAUGHT
I10: CAUGHT
I11: CAUGHT
battery: 70/70

determinism: build1 fnv=12ec9146 build2 fnv=12ec9146 byte-identical=true

