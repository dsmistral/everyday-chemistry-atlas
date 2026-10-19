---
name: "everyday-chem-atlas-fc3"
title: "The Field Companion · FC3 — Water: The Day's First Chemistry"
type: "text/markdown"
---

# The Field Companion · FC3 — Water: The Day's First Chemistry

*The Field Companion's first chapter made fire; its second made fire useful; this one begins before either — the jug you fill before you light anything, because a person outlives a missing meal by weeks and a bad jug by days. Water treatment is the home chemist's art at its most honest: no flame required for most of it, no rare reagent, and no step whose failure is silent — the failure announces itself, given a day. The chapter reads the water problem as three questions in fixed order — what is in the jug, what kills it, and what keeps it killed — and answers them with the kit a ruined world actually owns: heat, a dropper of bleach, sand, charcoal, sunlight, and a clean jar with a lid. The spine is a ladder (P19, promoted on this page's own evidence): interventions ranked cheap-and-robust first, because in a world with no pharmacy the cheapest robust rung is the one still standing when everything else is looted, broken, or spent. The fence holds as it held for thirty-six chapters and two field chapters: the trade's chlorinators — pool shock, trichlor tabs, the chlorine gas generator, calcium hypochlorite granules — are recognized, never made, never fired as salvage (P18), and the refusal is taught as a skill.*

**Chapter status: drafted 2026-10-19 (session 115, parts 1–2). Engine 31 (the RPN shunting-yard integer-lattice verifier, fresh build, zero code shared with all thirty engines before it) run history printed in full in Lab FC3.1: run 1 scored 25/46 and found one real engine defect — top-level juxtaposition of adjacent operands never summed — plus four harness-side slips named on their rows (the T2 hand-summed checksum the machine corrected, the FC2-S2 class again); run 2, the repair, verified **46/46 CLEAN**; the frozen run-2 battery block is the chapter's record. Verification labels per the binding ladder: [computed] for every battery figure, [convergent] for web-verified datums, [register] for the canon register, [flagged model] for stated models, [single-source] where only one source was found, [speculative] nowhere. The session-100 line observed at authoring time: the one NEW composition (N1, PET C10H8O4 = 192.170 g/mol) was grepped against every prior chapter's page before this page froze — the local ch03–ch30 masters and the ten pages held only at the repo (ch01, ch02, ch31–ch36, FC1, FC2), fetched at HEAD 9afbf0be via the saved-JSON pipeline; the two word-boundary `pet` hits that surfaced in Ch 34 were inspected and named honestly (the English word — a "pet fence" passage about dogs and chocolate — not the polymer). P19 "the method ladder" was promoted at this chapter's authoring, on the test registered at session 110: recurrence in two FC chapters (FC1's fire-starting rungs; this chapter's spine) with canon support (WHO's treatment ladder; UC IPM); the durable record extended in PROJECT.md §3 the same day.**

---

## Lecture 0 — The jug audit: a pencil-and-paper census of the day's water

**The phenomenon, before any notation.** Sit down with the notebook before you touch a single container — pour nothing, boil nothing — and take the census the situation actually offers. Three columns, one row per use: *how much*, *how clean it must be*, and *where it comes from*. Drinking for the household, counted by person and by cup. Cooking water, which gets a boil anyway and can borrow that boil's kill. Washing water, which needs clarity, not sterility — the dirt you can see and the patient you aren't. The garden's jug, if there is one, which needs neither. The sum is the household's water budget, and it is almost always smaller than the fear and larger than the bottle.

The second census is the sources, and it is a geography lesson before it is a chemistry lesson. Roof catchment, the well, the stream, the standpipe, the hot-water tank's drained remains, the toilet tank's clean side (the flap kept the two sides honest in the good years). For each source: what reaches it (animals? the neighbor's drain? the dead leaf gutter?), what it runs through to reach you, and what it carries that you can see. The notebook now holds the whole problem on one page, and nothing has been risked to write it.

**Why this is Lecture 0 and not a formality.** Because every number in this chapter's arithmetic attaches to a jug, and a census names the jugs before the arithmetic prices them. The dose ledger's milligrams are per liter — of *which* liter? The heat ledger's kilojoules are per kilogram — of *which* pot, on *which* fire? A treatment decision made without the census treats an abstraction; made after it, the same decision treats the water you will actually drink. The discovery cycle starts at Encounter for a reason: you cannot design an experiment on water you have not looked at.

One honest habit from the start, because it costs nothing now and pays for the whole chapter: *date and initial every page*. The treated jug from Tuesday and the raw jug from Wednesday look identical on Thursday, and the difference is written nowhere else.

## Lecture 1 — What is in it: the three fractions, and the living one ranked honestly

Every jug on the census carries three different problems, and confusing them is the beginner's whole error. **The suspended fraction** — silt, clay, leaf rot, anything that makes water turbid — is a physics problem: it scatters light, hides what else is there, and shields the living fraction from both chlorine and sunlight (the fact that pays for the filter, in the next lecture). **The dissolved fraction** — salts, hardness, iron, and in a truly ruined neighborhood heavy metals — is a chemistry problem that *no kill step addresses at all*: you can boil a liter of leaded water to a rolling boil for an hour and every atom of lead remains, because heat kills life, not matter. **The living fraction** — bacteria, viruses, protozoa, helminth eggs — is the one that makes you sick fastest, and the one this chapter's ladder actually fights.

The living fraction deserves its own honest ranking, by *what defeats it*, because treatment is not one skill but a menu matched to an enemy:

- **Helminth eggs and larvae** are the largest of the four — caught by settling, by any competent filter, by heat; rarely the field problem's crunch point.
- **Bacteria** — the classic waterborne killers and sickness-makers (the cholera-typhoid-dysentery class) — are middle-sized: held by a good filter, killed outright by a minute at a rolling boil, killed by honest chlorine dosing. Most field illness is this rung's fault; happily, this rung is the easiest to kill.
- **Protozoan cysts** (the giardia–cryptosporidium class) are the chlorine problem case: they shrug at dose rates that dispatch bacteria a thousandfold, which is why the "I chlorinated it" story ends in a week of misery. Heat and long solar exposure beat them; quick chlorine does not. The honest field rule: chlorine is a *bacteria-and-virus* tool, and a cyst-bearing jug wants the boil.
- **Viruses** are the smallest — too small for any improvised filter to strain, but the easiest chemistry to kill: first to fall to heat, first to fall to chlorine's oxidation.

Read as one sentence: **size orders the filter, chemistry orders the oxidant, and heat is the only rung that ignores both.** That sentence is the whole ladder's reason for existing, and the next lecture builds it.

## Lecture 2 — The method ladder: order the rungs before you climb (P19, promoted on this page)

Here is the chapter's spine, and the pattern it instantiates got its number on this page: **P19, the method ladder — rank interventions cheap-and-robust first.** The reasoning is a survivor's accounting. An intervention that is cheap, uses no consumables, and fails *loudly* (you can see the water is still cloudy) belongs below an intervention that is expensive, consumes a stock you cannot replace, and fails *silently* (under-dosed bleach in turbid water looks exactly like dosed bleach in clear water). The canon owns the pattern outright: the water-treatment method ladder (source protection → sedimentation → filtration → disinfection → safe storage, [register] — the WHO treatment-ladder convention; [convergent] — the treatment-guidance pages, WHO/SDE/WSH/03.04/45 and its emergency successors) and the same spine in pest work ([register] — UC IPM). FC1 climbed the same ladder for fire: the reliable rungs before the skillful ones. That is two FC chapters and two canon ladders — the promotion test registered at session 110, met here, recorded in the Chapter Ledger and in PROJECT.md §3 the same day.

The water ladder, rung by rung, ranked as the ruined world prices them:

1. **Source protection.** Fence the well, clean the gutter, move the draw point upstream of the drain. Costs: labor and a walk. Chemistry: none. This rung is never consumable and never expires.
2. **Sedimentation.** Let the jug stand half a day; pour the top nine-tenths off the settled tenth. Costs: time and a second vessel. Removes the coarse share of the suspended fraction — and with it a real share of the living fraction's *hiding places*.
3. **Filtration** (Lecture 4's sand-charcoal column): clarifies the remainder of the suspended fraction. Costs: containers, sand, charcoal, patience. Removes turbidity; does **not** sterilize — the honest limit, taught where it belongs.
4. **Disinfection** — the kill rungs, all three priced in this chapter's ledger: the rolling boil (Lecture 3, the most robust rung the world knows), chemical chlorination (Lecture 4, the dosing arithmetic), solar disinfection (Lecture 5, the bottle on the roof).
5. **Safe storage** (Lecture 5's clean jar): the rung everyone forgets — the treated, perfect liter re-infected by the dipped cup is the field's most common failure, and it is a discipline, not a device.

Note the ladder's one deep asymmetry, because it organizes the rest of the chapter: **boiling sits *above* filtering in robustness but *below* it in nothing.** The filter clears; the boil kills. The classical field order — settle, filter, *then* kill — exists because the kill rungs are more reliable when the water is clear, not because the filter is doing any killing. Kill steps aimed at cloudy water underperform silently (the turbidity shields), which is the ladder's way of saying: cheap rungs first, expensive rungs second, so the expensive one works when you spend it.

## Lecture 3 — The rolling boil: the heat ledger, priced at sea level and at 3,000 m

The rolling boil is the ladder's most robust rung: no consumable stock to fake or deplete, no optics, no pH dependence, and a failure mode you can *see* (a pot that is not boiling is visibly not boiling). What it costs is fuel, and fuel is what the heat ledger prices.

**The ledger's two terms.** Warming water costs its specific heat: **c_p = 4.184 J/(g·K)** — every gram, every kelvin [convergent] (Ch 7's own constant, pinned there ten times; H1). One liter from 20.0 °C to the 100.0 °C boil: 1,000 g × 4.184 J/(g·K) × 80.0 K = **334.720 kJ** [computed] (H2). Turning that liter to steam — *if you were fool enough to boil it all away* — costs the phase change: **2,256 J/g** (Ch 7's latent pin) × 1,000 g = **2,256.000 kJ** [computed] (H3), nearly seven times the warming bill; the full boil-away ledger is **2,590.720 kJ** [computed] (H4). The kill step, notice, needs almost none of that ledger: pathogens are dead at a rolling boil held a minute — the sensible term's 334.720 kJ plus a minute's hold, not the vapor's 2,256 kJ. The lesson the ledger teaches for free: *the boil kills on arrival; the steam is waste.* A lid on the pot is the cheapest fuel coupon in the book.

**The altitude question, answered honestly with a flagged model.** The boil point drops as the air thins — [convergent] for the rule class: about 1 °C per 300 m of elevation (the altitude-cooking references; the boiling-point tables, engineeringtoolbox.com) — and this chapter prices the standard rule as a **[flagged model: the 300 m rule]**, applied without refinements: at 3,000 m, 100.0 − 3,000/300 × 1.0 = **90.0 °C** [computed] (H5). The full boil-away ledger from 20.0 °C there: 70 K of warming (292.880 kJ) plus the phase change, held at 2,256 J/g — the second flagged assumption, kept honest by its label — gives **2,548.880 kJ** [computed] (H6). Now the figure that ends the argument: the latent share of that altitude ledger is 2,256,000 / 2,548,880 = **88.5%** [computed] (H7). Altitude cut the *temperature* by ten degrees and the *fuel bill* by about 1.6% — the phase change dominates the ledger so completely that the boiling point hardly moves the cost. The 90-degree boil still kills (the canning literature's whole altitude discipline), but it holds *longer*: the guidance says a rolling boil for **1 minute**, and **3 minutes above 6,500 ft** [convergent] (CDC's Boil Water Advisory guidance) — the longer hold is the honest answer to the cooler boil.

The ledger closes with the c_p figure's own dimensions, because this chapter's engine prices them: warming's c_p carries L²·T⁻²·Θ⁻¹, latent heat L²·T⁻² [computed] (W2, W3) — the same energy-per-mass coin, with and without the temperature slot.

## Lecture 4 — Clear, then kill: the filter's honest limits, and the bleach dropper's arithmetic

**The sand-charcoal column, and what it honestly does.** The field filter is two beds in a pierced can or cloth bag: coarse sand to strain and pack, charcoal to adsorb. Poured slowly, it does one job well — it takes cloudy water to clear water, removing the suspended fraction that shields the living one from every kill step downstream. What it does *not* do is sterilize: the column's pores are a thousand times a bacterium's width, a *million* times a virus's; clear water is not clean water, and the filter's clarity is preparation, not protection. Even the charcoal's famous adsorption is honest about its limits — it holds organics, taints, and some color, and it lets ions (the dissolved fraction of Lecture 1, heavy metals included) walk straight through. The column is a **flow device** (P17): pour slow, the clarity improves; the day you pour fast, you have built a channel, not a filter. First batches carry charcoal fines — flush until the rinse runs black-free.

**The kill rung that fits in a dropper.** Household bleach is sodium hypochlorite's water solution — NaOCl, **74.442 g/mol** [computed] (P2; Ch 25's own bench, pinned twice there), with its hypochlorite root OCl **51.452** (P3) and its salt destiny NaCl **58.443** (P4). The dosing arithmetic runs on one equivalence: field guidance quotes chlorine doses *as Cl₂* (Ch 16's gas, **70.906 g/mol**, P9), and the translation is a mole-for-mole bridge (W1's dose dimension, M¹·L⁻³ [computed] — a mass per volume, nothing more).

The floor dose: **2 mg/L as Cl₂** — the stoichiometric floor of the guidance class — wants, in sodium hypochlorite: 2 × (744,420 / 709,060) = **2.0997 mg/L of NaOCl** [computed] (D1). As 5% w/w household bleach: 2.0997 / 0.05 = **41.995 mg/L of bleach** [computed] (D2). And per dropper drop — the pharmacopoeia's standard **0.05 mL** [convergent] (the drop-volume references, the 20-drops-per-mL convention), at a bleach density of **1.08 g/mL** [single-source — flagged; bench-confirmable by the book's own culture: weigh a labeled liter on the jug scale, it should tip a hair over a kilogram] — each drop delivers 0.05 × 1.08 × 0.05 × 1000 = **2.70 mg of NaOCl** [computed] (D3). One such drop per 2 L, expressed back as Cl₂: **1.286 mg/L** (D4) — honest dosing. Two drops per liter — the field-class conservative guidance, CDC-style [convergent] for the *class* (EPA's emergency table: 8 drops of 6% per gallon, the same dropper logic at 6%) — lands at **5.143 mg/L as Cl₂** [computed] (D5): roughly 2.6 times the floor, which is what a margin is *for* — water you could not see into, bleach older than its label — and the margin is spent, not kept.

Two honest endpoints, because dose arithmetic without endpoints is ritual: **contact time 30 minutes** and **residual, not dose, is the truth** — the water should carry a faint chlorine smell at the pour; WHO's disinfected water carries **0.2–1 mg/L** of free residual [convergent] (WHO's chlorine guidance, WHO/SDE/WSH/03.04/45), and emergency practice holds **≥ 0.5 mg/L after 30 minutes' contact** [convergent] (the treatment guidance that quotes it). No smell after half an hour means the demand ate the dose — re-dose, don't hope.

**The shelf's honest decay.** Stored bleach is not stable: it decomposes to salt and the air's own oxygen — 2 NaOCl → 2 NaCl + O₂, closing **1.488.840 myu EXACT** [computed] (B1) — and its solid shelf-mate walks the same road: Ca(OCl)₂ → CaCl₂ + O₂, **1.429.820 EXACT** (B2) (Ch 16's calcium salt, P7, 142.982). The overstated closure NaOCl → NaCl + 2 O₂ is *false* and the engine catches it — gap 479.970 myu = **47.997 g** (B4) — which is the arithmetic's way of teaching the shelf: the old jug's hypochlorite has partly become NaCl and air, its label a memory. Dose by the residual test, not by the label's birthday. And the storage jar's own chemistry, rung 5's kin: limewater's Ca(OH)₂ (74.092, P8, Ch 24's pin) drinks the air's CO₂ and skins over — Ca(OH)₂ + CO₂ → CaCO₃ + H₂O, **1.181.010 EXACT** [computed] (B3): a lid is chemistry, not tidiness.

**The fence, this chapter's four faces (P18).** The trade sells its chlorine in industrial concentrations and devices: **pool shock, trichlor tabs, chlorine gas generators, calcium hypochlorite granules**. The household dropper's 2.70 mg is a scalpel; these are the same element as a warehouse fire — concentrated enough to corrode, to liberate chlorine itself (Ch 16's 70.906 gas) at a breath, to kill in a closed room. They are recognized, never made, never fired as salvage; the recognition row is the engine's own first gate (R1).

## Lecture 5 — The sun's two deliveries, and the clean jar that keeps the win

**The first delivery: ultraviolet, in a bottle (SODIS).** The same redirected sun that FC2's heliograph aimed at rescuers, aimed here at the water's own enemies. Solar disinfection is the cheapest kill rung the world owns: a clear **PET** bottle (the polymer this chapter prices as its one new composition: C₁₀H₈O₄ = **192.170 g/mol**, N1 — the recycler's triangle numeral 1, the bottle that holds the world's water) — filled clear, laid flat on a roof or a sheet of metal, in full sun: **6 hours of bright or half-clouded daylight; two full days when the sky is entirely clouded** [convergent] (the SODIS reference centre's own exposure rule, via the treatment-glossary pages; the WASH training literature). The mechanism is the sun's UV doing the oxidation the dropper would — with the *same* honest limits: turbid water shields the enemy (the same settle-and-filter ladder rungs come first; the sky's dose is weakened by the water's own cloud), and the bottle that held anything but food is not a water vessel at all. The bottle is a consumable that sun-hardens and fatigues — a season, not a lifetime.

**The second delivery: the phase change (the solar still, and distillation's one honest superiority).** A still is the water cycle in a box: a dark basin of the worst water you own, a sloped glass or film above it, a cup at the low edge. The sun heats the basin, the water evaporates — *only the water* — the vapor condenses on the cool cover and the drop runs to the cup. The yield is design- and weather-owned, printed as a range and never a promise: a conventional single-basin still yields on the order of **0.5–7 L per square meter per day** [convergent] (the solar-still literature; the design reviews' own ranges) — call it liters per square meter per day, and plan the family's day against the bottom of the range. And here is distillation's one honest superiority, worth its fuel bill when nothing else can pay it: **the phase change is a chemical separation, not a kill step.** The still leaves behind the dissolved fraction entire — salts, hardness, and the heavy metals that no boil, no dropper, no filter, no sunlight removes (Lecture 1's second fraction, finally answered). The boil kills what is alive but keeps every atom of what is dissolved; the still alone refuses the dissolved passage. The price is energy — the same 2,256 J/g ledger term (H3), paid this time in full — and the discipline of materials: a still built of unknown solder poisons the cleanest water it makes (Safety row 7).

**The rung everyone forgets.** Storage is the ladder's fifth rung and the failure nobody warns you about: the treated liter, perfect at noon, re-infected by the cup at supper. The clean jar has three properties — a **lid** (B3's lesson: air is chemistry), a **tap or a dedicated ladle** (no dipped cups, no hands, no return visits), and a **label with the treatment date** (Lecture 0's habit, paying its first dividend). Treated water is a manufactured product with a shelf life measured against the jar's own hygiene, and the chlorinated jug keeps longer than the boiled one — the residual keeps working after the pour [convergent] (the WHO residual band again) — which is the dropper's quiet second advantage over the pot.

---

## Lab FC3.1 — The RPN shunting-yard verifier, and the honest run history

Engine 31 is this chapter's verification machine, built fresh for FC3 and sharing zero code with the thirty engines before it. Its idea is one sentence: **the formula is parsed once into reverse Polish notation and evaluated on a value stack — the parse and the arithmetic never touch each other.** Dijkstra's shunting-yard algorithm walks the token stream with an operator stack and an output queue, honoring precedence (the hydrate dot ·, the group brackets, the trailing multipliers), and emits a postfix token queue; the evaluator then consumes that queue with a plain value stack — each operand pushed, each operator folding the stack top. The guards are the design's spine: bracket parity recorded at the openers (R4's `(NaOCl` refused UNCLOSED/UNMATCHED); bad characters refused with their positions (R5's `@` at position 5); unknown symbols refused at the table (R2's `TABLE REFUSES Mg` — magnesium honestly out of this chapter's scope, rather than a silent guess); and — the one deliberate severity, inherited honest — **a single integrality gate on the total mass**: atom counts may stay rational, but the mass must be a whole number of myu, so NaCl·0.35H₂O is refused at 647482.5000 myu (R3). The element table is the six-element set the chapter actually uses — {C 120110, H 10080, O 159990, Na 229900, Cl 354530, Ca 400780} myu — the Field Companion's first six-element admission table (the checksums T1 "1275.390", T2 "5717.170" pin it). The canonical formula is alphabetical symbol order, declared as a convention (S7's ClNaO, S8's CaCl₂O₂); derived quantities are exact integer ratios — BigInt numerator and denominator reduced by the Euclidean **modular** gcd (not Stein's binary, not prime products, not fixed scale) — and every displayed decimal is one half-up rounding of an exact rational, made once, at the stated precision. The P18 restricted-name gate fires *first* in the compose: all four of the trade's chlorinators refused as exact strings before any chemistry begins (R1). The dimension lattice is {M, L, T, Θ} — Θ for temperature, new with this heat-ledger chapter, priced at W1–W3.

**The honest run history — two runs, printed, not smoothed.** Run 1 scored 25/46 and the failures named themselves in two classes. **One real engine defect:** at top level, juxtaposed operands never summed — the lexer left `2 NaOCl` as two unmerged stack entries, and every composition-bearing row that relied on top-level adjacency failed (the fully-bracketed S10 passing localized the defect exactly: the bracket path summed, the bare path did not; the fix — subscripts bound to their symbol token at lex, group close folding to its marker, end-of-program folding top-level adjacency — went in once and all seventeen composition rows went green). **Four harness-side slips, named on their rows:** the T2 checksum, hand-summed as 5,717,070 against the machine's 5,717,170 — a transposition in the hand, the FC2-S2 class again, the machine vindicated and the expectation corrected; the H7 percent formula's scale; the D2 rounding (the machine's 41.995 stands); the D3 gram-to-milligram conversion. Run 2, the repair: **46/46 PASS — CLEAN.** The block printed below is the run-2 output — the post-repair execution of record, frozen in the durable record and its repo mirror.

```
PASS T1 | table checksum Σmyu (6 elements) | got "1275.390" | expect "1275.390"
PASS T2 | positional checksum Σ(i+1)·myu, i zero-based (run-1 hand-sum corrected) | got "5717.170" | expect "5717.170"
PASS S1 | admission C | got "12.011" | expect "12.011"
PASS S2 | admission H | got "1.008" | expect "1.008"
PASS S3 | admission O | got "15.999" | expect "15.999"
PASS S4 | admission Na | got "22.990" | expect "22.990"
PASS S5 | admission Cl | got "35.453" | expect "35.453"
PASS S6 | admission Ca | got "40.078" | expect "40.078"
PASS S7 | NaOCl | got "ClNaO 74.442 rounds=0" | expect "ClNaO 74.442 rounds=0"
PASS S8 | Ca(OCl)2 | got "CaCl2O2 142.982 rounds=1" | expect "CaCl2O2 142.982 rounds=1"
PASS S9 | C2H2O4·2H2O | got "C2H6O6 126.064 rounds=0" | expect "C2H6O6 126.064 rounds=0"
PASS S10 | (Na(OCl))2 — redundant-nesting probe on a real composition | got "Cl2Na2O2 148.884 rounds=2" | expect "Cl2Na2O2 148.884 rounds=2"
PASS R1 | the four P18 restricted names (exact each — gate fires FIRST) | got "P18 REFUSES: 'pool shock' ; P18 REFUSES: 'trichlor tabs' ; P18 REFUSES: 'chlorine gas generator' ; P18 REFUSES: 'calcium hypochlorite granules'" | expect "P18 REFUSES: 'pool shock' ; P18 REFUSES: 'trichlor tabs' ; P18 REFUSES: 'chlorine gas generator' ; P18 REFUSES: 'calcium hypochlorite granules'"
PASS R2 | MgSO4 — element honestly out of scope this chapter | got "TABLE REFUSES Mg" | expect "TABLE REFUSES Mg"
PASS R3 | NaCl·0.35H2O — single integrality gate on total mass | got "NON-EXACT refused: total mass 647482.5000 myu" | expect "NON-EXACT refused: total mass 647482.5000 myu"
PASS R4 | '(NaOCl' — unclosed bracket | got "UNCLOSED/UNMATCHED BRACKET refused: '(NaOCl'" | expect "UNCLOSED/UNMATCHED BRACKET refused: '(NaOCl'"
PASS R5 | NaOCl@H2O — bad char | got "BAD CHAR '@' refused at position 5" | expect "BAD CHAR '@' refused at position 5"
PASS P1 | H2O pin (Ch 4 grep×1) | got "18.015" | expect "18.015"
PASS P2 | NaOCl pin (Ch 25 grep×2) | got "74.442" | expect "74.442"
PASS P3 | OCl pin (Ch 25 grep×1) | got "51.452" | expect "51.452"
PASS P4 | NaCl pin (Ch 25 grep×2) | got "58.443" | expect "58.443"
PASS P5 | C2H2O4·2H2O pin (Ch 15 grep×3) | got "126.064" | expect "126.064"
PASS P6 | C6H10O5 pin (Ch 25 grep×1) | got "162.141" | expect "162.141"
PASS P7 | Ca(OCl)2 pin (Ch 16 grep×3) | got "142.982" | expect "142.982"
PASS P8 | Ca(OH)2 pin (Ch 24 grep×5) | got "74.092" | expect "74.092"
PASS P9 | Cl2 pin (Ch 16 grep×3) | got "70.906" | expect "70.906"
PASS N1 | C10H8O4 PET NEW-candidate (zero-hit local ch03–ch30 confirmed session 115; repo greps ch01/ch02/ch31–ch36/fc1/fc2 owed at part 2 pre-freeze) | got "192.170" | expect "192.170"
PASS B1 | hypochlorite decomposition :: 2 NaOCl -> 2 NaCl + O2 | got "1.488.840 EXACT" | expect "1.488.840 EXACT"
PASS B2 | calcium hypochlorite decomposition :: Ca(OCl)2 -> CaCl2 + O2 | got "1.429.820 EXACT" | expect "1.429.820 EXACT"
PASS B3 | the storage-scale chemistry :: Ca(OH)2 + CO2 -> CaCO3 + H2O | got "1.181.010 EXACT" | expect "1.181.010 EXACT"
PASS B4 | oxygen-overstated must-fail :: NaOCl -> NaCl + 2 O2 | got "CAUGHT gap 479.970 myu (47.997 g)" | expect "CAUGHT gap 479.970 myu (47.997 g)"
PASS H1 | c_p delivery: 1,000 g × 4.184 J/(g·K) × 1.0 K (Ch 7 [convergent]) | got "4.184 kJ" | expect "4.184 kJ"
PASS H2 | 20.0 -> 100.0 °C: 1,000 g × 4.184 × 80.0 | got "334.720 kJ" | expect "334.720 kJ"
PASS H3 | the phase change: 1,000 g × 2,256 J/g (Ch 7 pin) | got "2256.000 kJ" | expect "2256.000 kJ"
PASS H4 | total to boil 1 L from 20.0 °C | got "2590.720 kJ" | expect "2590.720 kJ"
PASS H5 | altitude boil point [flagged model: the 300 m rule]: 3,000 m | got "90.0 °C" | expect "90.0 °C"
PASS H6 | altitude total [flagged model: latent held at 2,256 J/g]: 20 -> 90 °C | got "2548.880 kJ" | expect "2548.880 kJ"
PASS H7 | latent share at altitude: 2,256,000 / 2,548,880 (run-1 formula corrected) | got "88.5%" | expect "88.5%"
PASS D1 | 2 mg/L as Cl2 -> NaOCl (stoichiometric floor) | got "2.0997 mg/L" | expect "2.0997 mg/L"
PASS D2 | as 5% w/w household bleach (run-1 rounding corrected) | got "41.995 mg/L" | expect "41.995 mg/L"
PASS D3 | per drop [convergent inputs: 0.05 mL, 1.08 g/mL, 5%]: NaOCl per drop (run-1 conversion corrected) | got "2.70 mg" | expect "2.70 mg"
PASS D4 | one drop per 2 L, expressed as Cl2 | got "1.286 mg/L" | expect "1.286 mg/L"
PASS D5 | two drops per 1 L (CDC-style guidance), expressed as Cl2 | got "5.143 mg/L" | expect "5.143 mg/L"
PASS W1 | dim(dose): mg/L | got "M^1·L^-3" | expect "M^1·L^-3"
PASS W2 | dim(c_p): J ÷ (g·K) | got "L^2·T^-2·Θ^-1" | expect "L^2·T^-2·Θ^-1"
PASS W3 | dim(latent heat): J ÷ g | got "L^2·T^-2" | expect "L^2·T^-2"
RUN 2 SUMMARY: 46/46 PASS — CLEAN
```

## Lab FC3.2 — The ledgers: the heat bill and the dose bill, every term priced

Two tables close the chapter's arithmetic, both [computed] by Engine 31, both reproducible by hand from Ch 7's constants and Ch 25's masses. The habit is the lab: *price the intervention before you spend it.*

**The heat ledger (per liter, from 20.0 °C):**

| Row | The term | The arithmetic | The price |
|-----|----------|----------------|-----------|
| H1 | c_p delivery | 1,000 g × 4.184 J/(g·K) × 1.0 K | 4.184 kJ |
| H2 | to the rolling boil | 1,000 g × 4.184 × 80.0 K | 334.720 kJ |
| H3 | the phase change (boil it all away) | 1,000 g × 2,256 J/g | 2,256.000 kJ |
| H4 | the full boil-away ledger | H2 + H3 | 2,590.720 kJ |
| H5 | boil point at 3,000 m [flagged model: the 300 m rule] | 100.0 − 10 × 1.0 | 90.0 °C |
| H6 | full ledger at 3,000 m [flagged model: latent held at 2,256 J/g] | 292.880 + 2,256.000 | 2,548.880 kJ |
| H7 | the latent share at altitude | 2,256,000 / 2,548,880 | 88.5% |

Read the ledger's own verdict: the kill step buys H2 plus one minute's hold; the other 87% of the full ledger is the vapor you did not want. At altitude the bill barely moves (H7's 88.5% against H4's share — the phase change dominates everywhere), but the boil point does (90.0 °C), and the guidance answers with time, not fuel: 1 minute rolling, 3 above 6,500 ft [convergent] (CDC).

**The dose ledger (household bleach, 5% w/w, drop = 0.05 mL [convergent], density 1.08 g/mL [single-source, flagged]):**

| Row | The question | The arithmetic | The answer |
|-----|--------------|----------------|------------|
| D1 | 2 mg/L as Cl₂, in NaOCl | 2 × 744,420/709,060 | 2.0997 mg/L |
| D2 | the same floor, in 5% w/w bleach | 2.0997 / 0.05 | 41.995 mg/L |
| D3 | the NaOCl in one drop | 0.05 mL × 1.08 g/mL × 0.05 × 1000 | 2.70 mg |
| D4 | one drop per 2 L, back as Cl₂ | 2.70/2 × 709,060/744,420 | 1.286 mg/L |
| D5 | two drops per 1 L (the field-class margin), as Cl₂ | 2 × 2.70 × 709,060/744,420 | 5.143 mg/L |

The endpoints bracket the ledger: the residual band 0.2–1 mg/L [convergent] (WHO) with the emergency floor ≥ 0.5 mg/L at 30 minutes' contact [convergent]; the faint smell at the pour is the working endpoint. A dose inside D4 lands the honest minimum; D5 is a margin spent against turbidity, weak bleach, and the cloudy jug — and re-tested at the residual, always.

Both ledgers' constants are the book's own: 4.184 J/(g·K) [convergent] Ch 7 ×10 and 2,256 J/g Ch 7 ×4; the kettle figures of FC1's run (334.720 / 2,256.000 / 2,590.720 kJ) are zero-hit in Ch 6–Ch 7 and were recomputed here fresh from Ch 7's constants — the same numbers, independently re-derived, which is what a pin is *for*.

## Exercises

Solve before reading the labs again; every worked figure below is a battery row (the session-102 line). Grades: ● light, ●●● summit, ◆ worked answer withheld until the session-116 Revision Appendix, ◐ open.

**FC3.1 — The sensible bill (●○○).** One liter of cleared well water, 20.0 °C, a lid on the pot, a fire beneath. (a) What does one kelvin of it cost? (b) What does the whole climb to the rolling boil cost? (c) Name the ledger's third term and its price — the one the kill step does *not* need. *Answers:* (a) **4.184 kJ** (H1); (b) **334.720 kJ** (H2); (c) the phase change, **2,256.000 kJ** (H3) — the boil kills on arrival; the steam is waste.

**FC3.2 — The dose translation (●○○).** Guidance quotes a floor dose of 2 mg/L *as Cl₂*. (a) In sodium hypochlorite? (b) In 5% w/w household bleach? (c) How much NaOCl does one dropper drop deliver? *Answers:* (a) **2.0997 mg/L** (D1); (b) **41.995 mg/L** (D2); (c) **2.70 mg** (D3). *Ways:* the Cl₂→NaOCl bridge is a mole-for-mole mass ratio (70.906 / 74.442); the drop is volume × density × fraction — the battery's own rows.

**FC3.3 — The mountain pot (●●○).** The household camps at 3,000 m. (a) Where does the water boil, under the chapter's flagged 300 m rule? (b) The full boil-away ledger from 20.0 °C there? (c) The latent share, and the verdict: why does altitude barely change the fuel bill, and what *does* the field answer change? *Answers:* (a) **90.0 °C** [flagged model] (H5); (b) **2,548.880 kJ** [flagged model] (H6); (c) **88.5%** (H7) — the phase change dominates the ledger, so ten degrees off the boil point is under 2% off the bill; the field answer lengthens the *hold* (3 minutes above 6,500 ft [convergent], CDC), not the fire.

**FC3.4 — The old jug (●●○).** The bleach bottle survived the ruin, but its label has aged. (a) Close the stored bleach's own decay: 2 NaOCl → 2 NaCl + O₂. (b) Its solid shelf-mate: Ca(OCl)₂ → CaCl₂ + O₂. (c) A supplier's note claims NaOCl → NaCl + 2 O₂; what does the verifier say, and what has the old jug partly *become*? *Answers:* (a) **1.488.840 myu EXACT** (B1); (b) **1.429.820 myu EXACT** (B2); (c) the closure is *false* — **CAUGHT, gap 479.970 myu = 47.997 g** (B4): the jug's hypochlorite has partly decayed to salt and the air's oxygen, so the label's promise outruns the contents — dose by the residual test (the faint smell after 30 minutes), never by the label's birthday.

**FC3.5 — The day priced twice (●●●).** The census (Lecture 0) says four people, 2 L of drinking water each: 8 L per day, from the settled-and-filtered rain barrel at 20.0 °C. Price the day's kill rung both ways. (a) Boil it. (b) Chlorinate it at the floor dose. (c) The summit verdict: which rung, when, and why — and what the second rung buys that the first cannot. *Answers:* (a) 8 × **334.720 kJ** = 2,677.760 kJ of sensible heat (H2's own row, scaled by the census) plus four minutes of holds on a wood fire; (b) 8 L × 2 mg/L as Cl₂ = 8 × **2.0997 mg** = 16.7976 mg NaOCl (D1) = 8 × **41.995 mg** = 335.96 mg of 5% bleach (D2) ≈ **6 drops** (D3's 2.70 mg per drop — 335.96/54.0 ≈ 6.2, round up; the margin spends, it does not save); (c) the boil is the robust rung — no stock, no expiry, visible failure — the dropper is the *margin* rung, and its quiet purchase is the residual: the chlorinated jug keeps *after* the pour (the WHO band's whole meaning), while the boiled one is sterile exactly until the first cup breaks the surface. The ladder's answer for the ruined world: boil today's drinking pot, chlorinate tomorrow's storage jug, and let each rung do the work it owns.

**FC3.6 — The cloudy jug (◆).** The stream turned with the storm, and the household's doser — careful, arithmetic-minded — treats the cloudy jug exactly as the clear one, checks nothing, and a week later the household is sick anyway. Diagnose the failure and prescribe the fix, rung by rung. *Worked answer withheld until the session-116 Revision Appendix; this exercise prints no figures.*

**FC3.7 — The water census (◐).** Walk the household and list every water container it owns or could improvise — pots, jugs, bottles, the tank, the bucket, barrels. For each: capacity, the lid it has or lacks, tap-or-dip, its re-contamination risk, and the ladder rung it can serve. Open-ended; the honest census is a table with a *judgment* column, and its bottom line is which three vessels the household should bet on — and why.

## Safety

| # | Rule | The chemistry it guards |
|---|------|------------------------|
| 1 | Never drink unassessed water; the source and the census come before the cup | Lecture 0's audit is the first safety device the household owns — the unexamined jug is the one that sickens the careful family |
| 2 | Bleach never meets an acid cleaner or ammonia — no mixed jugs, no "stronger together" reasoning | The acid liberates the hypochlorite's own chlorine (Cl₂, 70.906 — Ch 16's gas); ammonia answers with chloramines: the household's classic invisible poison, made in a bucket by good intentions |
| 3 | The trade's chlorinators — pool shock, trichlor tabs, calcium hypochlorite granules, the chlorine gas generator — are recognized, never made, never fired as salvage | The P18 row, the fence as taught skill: concentrated chlorinators corrode and liberate chlorine at a breath, and a closed room turns the rescue into the incident; recognition, never improvisation |
| 4 | The boiling pot: fixed non-combustible base, handle turned in, never unattended | FC1's whole fire discipline stands — the day's first chemistry still runs on the oldest reaction, and the pot that boils over is a burn and a fire in one motion |
| 5 | Scalds under cool running water 10–20 minutes; never ice, never ointment first | Steam scalds worse than its own water — the latent 2,256 J/g pays out into skin on contact; the burn keeps burning for minutes and heat's exit is the treatment |
| 6 | SODIS bottles: food-grade PET only, never a bottle that held chemicals; never look at the sun or a mirror flash | The polymer that makes a good window makes a bad memory — a chemical bottle leaches its past into the treated water; and FC2's solar rule stands: the redirected sun is a tool, the direct sun is an eye hazard |
| 7 | Stills: no lead solder, no unknown metals in the vapor's path; food-grade basin and film | Distillation is the one method that removes what *dissolved* — and the still returns the favor: whatever the condenser gives, the cleanest water of the day carries; the historical still's own poison was its seams |
| 8 | Storage: the dipped cup re-infects the jar — spigot or dedicated ladle, lid on, treatment date written on it | The treated liter is a manufactured product with a shelf life measured against the jar's hygiene; the lid is chemistry (B3's crust is the air *working*), and the written date is the only memory a jug has |

## Canon-coverage check (FC3 topics)

- **WHO chlorine residual band 0.2–1 mg/L** in disinfected water: [convergent] — WHO, *Chlorine in Drinking-water* (WHO/SDE/WSH/03.04/45, cdn.who.int); the emergency practice floor **≥ 0.5 mg/L after 30 minutes' contact**: [convergent] — the treatment guidance quoting WHO (dosatron.com's WHO-based treatment pages).
- **Rolling boil 1 minute; 3 minutes above 6,500 ft**: [convergent] — CDC's Boil Water Advisory toolkit (cdc.gov); the emergency-guidance pages carrying the same rule (epa.gov's emergency disinfection family).
- **EPA emergency bleach dosing by drops** (8 drops of 6% per gallon; 6 drops of 8.25%): [convergent] — EPA, *Emergency Disinfection of Drinking Water* (epa.gov); CDC's label-following emergency guidance (cdc.gov, water-emergency). The drop-dose *class* is convergent; the chapter's own 5% arithmetic is [computed] at D1–D5.
- **Household bleach at 5–5.25% w/w NaOCl**: [convergent] — Stanford EHS's sodium hypochlorite reference (5.25%); the chemical-book SDS class (about 5%, household).
- **The drop volume 0.05 mL (20 drops per mL)**: [convergent] — the pharmacopoeia drop standard (craftybase.com; unitconvertzone.com; biologyinsights.com).
- **Bleach density 1.08 g/mL**: [single-source — flagged, bench-confirmable] — the homework-reference value (study.com); the book's own answer is the jug scale: weigh a labeled liter. The D3 row's label froze "convergent inputs" at run 2; the coverage ladder refines the density's evidence honestly, and the refinement is printed, not laundered.
- **The altitude rule class (~1 °C per 300 m; ~1.8 °F per 1,000 ft)**: [convergent] — temperatures.com's boiling-point guide; arhfoundation.org's altitude treatment; the boiling-point tables (engineeringtoolbox.com). The chapter's application (3,000 m → 90.0 °C, latent held) is **[flagged model]**, labeled wherever it is printed.
- **SODIS exposure: 6 h bright or half-clouded; 2 days fully clouded**: [convergent] — the SODIS reference centre's rule via the SSWM treatment pages (sswm.info); the WASH training literature (medbox.org); the field guides carrying the same rule (homesteadingsecrets.com).
- **Solar-still yield on the order of 0.5–7 L/m²/day, design- and weather-owned**: [convergent] — the solar-still reviews (scienceinsights.org; the design reviews' own typical-yield ranges, aiche.onlinelibrary.wiley.com). Printed as a range, never a promise.
- **Heat anchors**: 4.184 J/(g·K) [convergent] — Ch 7's own constant (×10 there); 2,256 J/g — Ch 7's latent pin (×4 there); the derived kettle figures (334.720 / 2,256.000 / 2,590.720 kJ) [computed] here fresh.
- **Honesty line**: no audited reference owns the household's dose arithmetic as *bench chemistry* — the WHO/CDC/EPA canon owns the *endpoints* (the residual band, the contact time, the rolling boil and its altitude hold), and the arithmetic translating them into drops is derived here and priced at the battery; the flagged models (the 300 m rule's clean application, the latent held at altitude) are priced as their own rows, labeled, never laundered; the two bench-confirmation flags (the bleach density, the old jug's decay) are exercises in the book's own gravimetric culture, not gaps in it.

## Forward flags

- **Session 116**: the Phase-3 adversarial review of this chapter — a fresh engine sharing zero code with Engines 1–31; the session-100/102/104 binding lines and the session-112 attribution line in force; Ex FC3.6's withheld answer due at its Revision Appendix; N1 re-provable via the saved-JSON pipeline (the word-boundary `pet` hits in Ch 34 named and dismissed at authoring time — the two-line inspection is in the Chapter Ledger).
- **The web edition (standing debt)**: per the web-sync rule, FC3's reading edition is owed in the session the master lands; the session-108 renderer was not durably saved and must be rebuilt from the `web/ch01-web.html` template — the same debt class as FC1's and FC2's, recorded, not silently deferred.
- **FC4 — Pests and Weeds Without a Poison Shelf**: inherits this chapter's spine whole — the method ladder (P19) is the IPM chapter's own back (the third FC appearance, the canon's UC IPM ladder); the P18 fence (the poison shelf recognized, never synthesized); and the residual-thinking taught here (the endpoint is the pest population after the treatment, not the dose poured).

## Back flags

- **Ch 4** — water: H₂O (18.015), the chapter's whole subject and the product side of every closure in the battery.
- **Ch 7** — Heat, Fire, and Fuels: c_p 4.184 J/(g·K) and the 2,256 J/g latent pin — the heat ledger's own constants, honored at H1–H7.
- **Ch 15** — the mineral-acid bench: oxalic acid dihydrate (C₂H₂O₄·2H₂O, 126.064), the hydrate-dot arithmetic's anchor — and the cleaner-shelf acid that must never meet the bleach jug (Safety row 2).
- **Ch 16** — the chlor-alkali bench: Ca(OCl)₂ (142.982) and Cl₂ (70.906) — the chlorinating chemistry's home, and the gas the fence refuses to improvise.
- **Ch 24** — Ca(OH)₂ (74.092): limewater, the storage jar's own chemistry (B3's crust), and the lid's argument.
- **Ch 25** — the bleach bench: NaOCl (74.442), OCl (51.452), NaCl (58.443), and C₆H₁₀O₅ (162.141) — the dosing arithmetic's home chapter, and the cellulose that packs the filter.
- **FC1** — fire: the fuel bands, the burn and scald discipline (Safety rows 4–5), and the pot's heat source — the oldest reaction, still the heat ledger's landlord.
- **FC2** — signal and light: the solar geometry SODIS reuses, and the discipline of the redirected sun (Safety row 6).
- **P17 / P18 / P19** — the pattern triple this chapter exercises: the filter and the dropper are flow devices with rates to control; the trade's chlorinators are faces to recognize, never make; and the method ladder — promoted on this page — is the spine the next field chapter inherits.

## Chapter Ledger

- **Pins claimed (P1–P9, with anchors and this session's authoring-time raw grep counts)**: H₂O 18.015 (Ch 4, ×1); NaOCl 74.442 (Ch 25, ×2); OCl 51.452 (Ch 25, ×1); NaCl 58.443 (Ch 25, ×2); C₂H₂O₄·2H₂O 126.064 (Ch 15, ×3); C₆H₁₀O₅ 162.141 (Ch 25, ×1); Ca(OCl)₂ 142.982 (Ch 16, ×3); Ca(OH)₂ 74.092 (Ch 24, ×5); Cl₂ 70.906 (Ch 16, ×3; Ch 10/12/18/28 also own it). All nine re-derived by this chapter's own engine [computed]; the counts are raw occurrence counts, re-verified against the anchor chapters' own local masters in the authoring session per the session-112 binding line.
- **New composition claimed**: C₁₀H₈O₄ 192.170, PET — polyethylene terephthalate, the SODIS bottle's own polymer (N1) — **NEW, verified at authoring time before this page froze** (the session-100 line observed, not owed to review): zero hits for `192.169 | 192.17 | C10H8O4 | polyethylene terephthalate` (case-insensitive) against the local ch03–ch30 masters *and* the ten pages held only at the repo — ch01, ch02, ch31–ch36, FC1, FC2 — fetched at repo HEAD 9afbf0be via the saved-JSON pipeline and grepped in full. The two word-boundary `pet` hits that surfaced in Ch 34 under the broadened sweep were inspected and named honestly: the English word (a "pet fence" passage — theobromine, dogs, and chocolate), not the polymer; the mass, formula, and full-name patterns all zero. `search_code` was tried twice and returned `incomplete_results: true` both times — inconclusive, recorded as such; the saved-JSON pipeline is the proof of record.
- **Balances**: B1–B3 close exactly (the myu closures printed in the battery block — the stored bleach's decay, its solid shelf-mate's, and the storage jar's crust); B4, the oxygen-overstated must-fail, is *caught* at 479.970 myu = **47.997 g**.
- **Gates**: the {C, H, O, Na, Cl, Ca} admission table — the Field Companion's first six-element table (checksums T1 "1275.390", T2 "5717.170"); Mg refused at the table, honestly out of scope (R2); the single integrality gate on total mass (R3, NaCl·0.35H₂O refused at 647482.5000 myu); bracket and bad-character refusals with positions (R4, R5); the P18 restricted-name gate fires first in compose, all four refusals exact (R1).
- **Heat anchors**: 4.184 J/(g·K) [convergent] Ch 7 ×10; 2,256 J/g Ch 7 ×4; the derived kettle figures recomputed fresh this session — 334.720 / 2,256.000 / 2,590.720 kJ are zero-hit in Ch 6–Ch 7 (FC1's repo-only figures) and were re-derived here from Ch 7's own constants, independently, which is the pin's whole job.
- **Pattern promoted**: **P19, the method ladder** — promoted at this chapter's authoring (2026-10-19), the promotion test registered at session 110 met in full: recurrence in ≥2 FC chapters (FC1's fire-starting rungs ranked robust-first; this chapter's spine), canon support held (WHO's treatment-method ladder; UC IPM's intervention order); the durable record extended in PROJECT.md §3 the same day, and the promotion's evidence printed here.
- **Engine provenance**: Engine 31, the RPN shunting-yard integer-lattice verifier — fresh build, zero code shared with the thirty engines before it; operator-precedence parse to RPN, value-stack evaluation, exact BigInt rationals reduced by the Euclidean modular gcd; the {M, L, T, Θ} lattice (Θ new, the heat chapter's own); honest run history runs 1–2 printed in Lab FC3.1 (run 1's 25/46: one real engine defect — top-level juxtaposition never summed — caught and fixed; four harness-side slips named, the T2 hand-sum the FC2-S2 class again, the machine vindicated); the frozen run-2 block is this page's verification record; the full source and the run history are durable in the topic's record and its repo mirror (`engine-records/fc3-engine31.md`) — the compaction-loss class closed.
- **Owed**: Ex FC3.6's machine-verified answer (the session-116 Revision Appendix); the FC3 web edition (the standing web-sync debt, FC1's and FC2's siblings); the Phase-3 review itself.

---

*Chapter status: drafted 2026-10-19 (session 115, parts 1–2). The frozen run-2 battery block in Lab FC3.1 is the verification record; the labels are the contract; the fence (P18) held at every gate; and the ladder (P19) was promoted on this page's own evidence.*
