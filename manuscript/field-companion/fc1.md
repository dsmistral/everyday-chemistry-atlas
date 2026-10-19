---
name: "everyday-chem-atlas-fc1"
title: "The Field Companion · FC1 — Fire: The Oldest Reaction"
type: "text/markdown"
---

# The Field Companion · FC1 — Fire: The Oldest Reaction

*Of every chemical reaction the ruined world's chemist must own, fire was the first one anybody owned. It is also the most misunderstood: a flame is not a thing that fuel does, it is a gas that fuel becomes — every solid and every liquid must first turn itself into vapor before it can burn, and every skill in this chapter is a way of paying that transformation's bill. This is the Field Companion's first chapter: ignition taught as chemistry (a threshold, not a trick), fuel taught as arithmetic (megajoules per kilogram, honestly banded), and the fire lay taught as engineering (P17 — the same energy, released at the rate you choose). The Charter fence holds here exactly as it held for thirty-six chapters: energetics, propellants, ammunition, and poisons are excluded absolutely, and the refusal itself is taught as content (P18). What remains is the oldest reaction, done safely, at the bench and at the fire ring.*

**Chapter status: drafted 2026-10-19 (session 111); adversarially reviewed 2026-10-19 (session 112) — PASS WITH CORRECTIONS, RA-1…RA-6 (Revision Appendix below). Engine 27 (the unit-lattice engine) run 1 verified 39/44 — five harness-side defects, the engine core clean on every row; run 2 (the repair pass) verified 44/44 CLEAN; the review engine (Engine 28, the prime-product review engine, fresh build, zero code shared with Engines 1–27) re-derived the whole battery independently — run 1 61/63, two harness-side counting defects, the engine core clean; run 2 63/63 CLEAN. Verification labels per the binding ladder: [computed] for every battery figure, [convergent] for web-verified datums, [register] for the canon register, [flagged model] for stated models, [speculative] nowhere.**

---

## Lecture 0 — Blow out the candle, then relight its smoke

Do this one first, because it resets what a fire is.

Light a candle and let it burn a minute. Blow it out. A ribbon of white smoke rises off the still-hot wick — unburned paraffin vapor and wax particles. Now bring a lit match to that ribbon, a hand's breadth above the wick. The flame jumps down the smoke like a fuse and the candle relights.

The lesson is not the trick; it is what the trick proves. **The flame was never burning the wick, and it was never burning the wax.** It was burning gas — vapor driven off the wax by the heat of the flame itself. The wick's only job is to hold the melt pool in the heat; the wax's only job is to evaporate. When you blow the candle out you stop the reaction but not the supply: the smoke ribbon is fuel that has already been gasified, and a single flame applied anywhere along it runs back to the source.

Generalize and you have the operating principle of this whole chapter, and of every fire you will ever build: **solids do not burn as solids; liquids do not burn as liquids. Fuel burns as gas.** Wood, charcoal, wax, fat, cloth — all of it must first be dried, then heated to gasification, before a flame can exist. Everything in fire-lighting is the management of that gasification: the heat that starts it, the tinder small enough to need almost none, the fire lay that feeds it.

One more reading from the same candle: the smoke you relit is *unburned* fuel. A flame is incomplete by nature; the smoke is the receipt. When you meet smoke pouring off a fire, you are watching fuel leave unspent — the fire-lay engineer's first diagnostic, and a flag we will return to when the wet-day arithmetic prices rain-soaked wood in Lecture 5.

## Lecture 1 — The ignition threshold: the tetrahedron at the bench

Fire needs four things at once, and the classic picture draws them as a tetrahedron: **fuel, oxidizer, heat, and an uninhibited chain of reactions** — the fourth face is the one the older triangle lacked, and it is the face that explains why some hot fuel-oxygen mixtures still refuse to burn ([register]: the fire-science page of the session-110 canon register; the tetrahedron's chain-reaction face is also the reason a halon-class agent can snuff a fire that is already hot enough).

The three faces you can manipulate at a bench are fuel, oxidizer, and heat — and of the three, **heat is the one you control at the moment of ignition**. A fuel does not ignite at any temperature at all; it ignites when it is heated past a threshold. Paper's measured ignition temperature is about **233 °C / 451 °F** ([convergent]: the commonly cited figure sits within the measured range; sources include the classic "ignition temperature of paper" compilations, hypertextbook and ftloscience). That number is famous for the wrong reason (a novel's title) and useful for the right one: it is astonishingly hot. You cannot hold a match under a thermometer and read 233 °C — the threshold is not reachable by "making the room warm." Ignition is always a *local* event: a small place, pushed past a big temperature, by a concentrated source.

Two thresholds, honestly distinguished:

- **Piloted ignition** — a spark, ember, or small flame delivers the needed heat to a tiny spot. The fuel around that spot is still cool; only the micro-region must pass the threshold. This is every fire-lighting method: match, ferrocerium spark, ember from friction, coal from a carried fire.
- **Autoignition** — the whole fuel mass is heated until it lights itself, with no pilot. Higher temperature, much bigger energy bill, and (for our purposes) the class of event you *avoid* creating by accident: oily rags in a pile, hay bales gone damp, the self-heating corner of the compost heap that FC5 will meet as slow oxidation's failure mode.

The tetrahedron reads in reverse as well, and this is the whole of firefighting: remove any face and the fire dies. Starve the fuel, smother the oxidizer, cool the heat, or break the chain (the agent class the register records). Every extinguishing technique in the safety table at this chapter's end is one of those four removals, named.

And the honest boundary of this lecture: **a threshold temperature is a property of the fuel and the geometry together**, not a single universal constant — thickness, moisture, and the pilot's power all move the number a real fire demands. The 233 °C datum is the paper's band under controlled conditions; you treat it as the order of magnitude of the bill, and you pay it locally. [convergent band, honestly stated]

## Lecture 2 — The pyrolysis ladder: char, tinder, and the geometry of starting

Heat a stick of wood and it climbs a ladder, in strict order:

1. **Free water boils off** first, at ~100 °C — and this is why wet wood hisses before it burns, and why the fire's first minutes are spent on drying, not on flame (the steam you hear is energy leaving as somebody else's phase change).
2. **Pyrolysis** begins as the dry wood passes a couple hundred degrees: the long molecules of cellulose and lignin crack, and the crack vents **flammable gases** — the true fuel of any wood fire, per Lecture 0.
3. **Char** remains when the volatiles are spent: nearly pure carbon, which burns at the surface as a glow, slowly, hot and smokeless — the coal, the bed, the carried fire.
4. **Ash** is what the char leaves when its surface oxidation finishes: the mineral fraction that was in the wood all along.

The ladder is a *distillation train that builds itself*, and each rung is a fuel with different properties. The gases flame; the char glows; the ash is spent. A wood fire is all three at once, in a gradient from the flame tips down to the grate.

**Char cloth is the ladder's rung two, harvested.** Take woven cotton (a slice of old jean or tee), pack it loosely in a small lidded tin, and set the tin in the coals of an existing fire: the cotton pyrolyzes in the tin's poor oxygen, the flammable gases vent as smoke past the lid's edge, and what remains is a black, fragile cloth that has lost its volatiles but kept its geometry ([register]: the standard preparation, field canon; performed with the same discipline as any pyrolysis — vented, never sealed, cooled before opening; a sealed tin is a pressure vessel and the Charter's never-sealed rule owns it absolutely). Char cloth's virtue is that it is *already at rung two*: it needs no drying and no cracking — the smallest honest spark pushes a fiber past glowing, and it does so at a surface-to-mass ratio woven cloth gives for free.

That last phrase is P17, promoted at the session-110 bootstrap and load-bearing from this page forward: **release-rate control** — need energy from a fuel without losing control of it; set the release rate by *geometry and form*, not by changing the chemistry. Tinder, kindling, and fuel are the same chemistry at three geometries:

- **Tinder** — char cloth, dry grass, shredded bark, cotton: maximal surface per gram; ignites from a spark's few watts and, burning fast, produces the concentrated heat that nothing larger can produce from so little.
- **Kindling** — pencil-lead to finger-thin dry sticks: enough mass to carry flame, enough surface to catch from tinder.
- **Fuel** — wrist-thick and up: the burn you actually want, which will not light from a spark no matter how long you hold it there — not because the spark isn't hot enough, but because it cannot deliver its heat to enough wood at once. The spark's power, not its temperature, is the shortfall.

Grade the geometry and the same log is a hazard (unsplit, in a hurry) or a dinner (split, stacked, fed). P17 will return in every fire lay, in FC2's wicks and lamps, in FC5's compost, and in FC6's rock work; here it is first taught as the tinder ladder.

## Lecture 3 — The ignition menu: friction, percussion, and the sun

Every way of starting a fire without a match is a way of delivering **power** — watts, concentrated into a place small enough that the temperature can pass the threshold of Lecture 1 before the heat drains away. The menu has three honest chemistries:

**Friction (the bow drill, the hand drill).** Mechanical work becomes heat at the interface of two dry, soft-ish woods; the drill's tip and the hearth's notch fill with char-powder — rung two of the ladder, manufactured on the spot. If the set is dry and the stroke honest, the powder's finest grains reach glowing; gathered into a tinder bundle and breathed upon (air: the oxidizer face, delivered at the rate your lungs choose — P17 again), the glow becomes flame. The chemistry is pyrolysis plus surface oxidation of char; the engineering is the notch, the bearing block, the string's tension. Field canon owns the technique in detail ([register]: SAS Survival Handbook, Bushcraft 101 — practice at home before you need it; the honest datum is that friction fire is a *skill*, not a fact, and its failure modes are moisture and fatigue, not chemistry).

**Percussion (flint-and-steel, ferrocerium).** Here is the beautiful one, and it is almost always told wrong. When hardened steel meets a sharp flint edge, the flint *shaves the steel*: the sparks are **burning iron particles**, torn off hot, oxidizing in air as they fly. The stone does not burn; the stone is the knife. The modern "flint" rod — ferrocerium — runs the same play with a better alloy: **mischmetal**, a rare-earth blend dominated by cerium and lanthanum, with iron for body ([register]: ferrocerium/mischmetal at the register level, session 110). Shavings of it ignite in air at very low mass and very high temperature, and a struck rod throws a fistful of them. Either way the lesson of Lecture 1 lands exactly: the spark's temperature is enormous, its power is tiny — so it lights char cloth and shreds of tinder, and it lights nothing else, ever. Match the pilot to the geometry, not to the temperature.

**Solar (the lens).** Sunlight arrives at roughly a kilowatt per square meter on a clear day ([convergent]: the solar constant's surface-level share, the standard planning figure); a lens does not create that power, it *concentrates* it — trading area for temperature, the same trade as tinder. A magnifier, a pair of reading glasses, a clear bottle of water, even a polished can bottom, focused onto black char or dark tinder, will pass paper's threshold in seconds. The requirements are honest and rare in the field: sun, a focusing geometry, and something dark at the focus (dark, because ignition begins with absorption). When the sun is available it is the gentlest ignition of all: no consumables, no skill decay, no fatigue — only patience and geometry.

What the menu does not include, and why, is a chapter-level honesty: matches and lighters are *stored* ignition (sulfur/match-head chemistry and liquefied-butane delivery — shelf items you should carry, and whose chemistry Ch 16 and the household-shelf chapters already own). The menu above is the chemistry of ignition when nothing consumable remains. And the fence: **no energetic or pyrotechnic ignition method exists in this book** — not because the chemistry is unknown, but because it is excluded by the binding Charter (P18); the refusal is itself the skill, taught in the safety table's last row.

## Lecture 4 — Chemical ignition at the demonstration tier: permanganate and glycerin

There is one class of chemical ignition that belongs in a bench book, at a stated tier, with full hazard discipline: the **delayed exothermic oxidation** of glycerin by potassium permanganate. Ch 13 pinned the permanganate (KMnO4, 158.032 g/mol) as the analyst's oxidizer; Ch 23 pinned the glycerin (C3H8O3, 92.094 g/mol) as the soap-maker's byproduct. Set a gram-scale cone of dry KMnO4 crystals on a non-combustible surface, add a few drops of glycerin, and step back: nothing happens — for seconds to a minute — and then violet flame, smoke, and a spent black mass ([convergent]: the classic demonstration-tier reaction, documented on university demo sheets, chem.washington.edu and colorado.edu; the delay varies and **crystal size affects the rate** — coarse grains react more slowly than fine, which is this book's kinetics chapter in one gesture).

The delay is the lesson, and kinetics names it. The oxidation is exothermic, but at ambient temperature it starts *slowly*: the first oxidation steps release heat, the heat accelerates the next steps (reaction rate climbs with temperature, the Arrhenius behavior Ch 25 taught as "kinetics you can watch"), and the system runs up its own hill until the surface reaches the ignition threshold of the mixture's vapors. That is an **induction period** — a reaction that must heat itself into a faster version of itself, the fire tetrahedron's heat corner built from the reaction's own exotherm. Every fire is a delayed reaction; this one just wears its delay on the outside, at gram scale, where the delay can be watched from a safe distance.

For the ledger, the reaction's outcome is bookkept as a **formal ash model** [flagged model]: the glycerin oxidized fully by the permanganate, ashed to potassium carbonate and manganese dioxide, venting carbon dioxide and water:

> 6 C3H8O3 + 28 KMnO4 → 14 K2CO3 + 28 MnO2 + 4 CO2 + 24 H2O — closes at **4,977.460 g** per the model's stoichiometric charge [computed, B4]

Read that label carefully, because it is the honesty line of this lecture: the *bookkeeping closure* is exact — every C, H, O, K, and Mn atom accounted, both sides 4,977.460 g to the ten-thousandth of a gram (Lab FC1.1's row X4 proves the closure as raw integers, no rounding) — but the *real* reaction is messier than the model: an actual demonstration's residue is a mixture of manganese oxides in several oxidation states, carbonates, and carbonized organics, and the gases include carbon monoxide from incomplete oxidation. The formal model exists so the demonstration can be priced and checked at the bench tier; it does not claim the mechanism. When the ash model's row was deliberately drafted one CO2 short, the gate caught a gap of exactly **44.009 g** [computed, B5] — the mass of one CO2, which is the arithmetic of *why* the ledger can be trusted to catch what the hand slips.

MnO2 enters this chapter as a **reused pin, 86.936 g/mol** [computed, P9] — the session-112 grep discharged the new-composition debt *against* the claim: the mass was first priced in Ch 12 (the alkaline cathode's own pin), re-used recognition-only in Ch 16/18/19, and cross-referenced in Ch 25/26. The N1 row therefore converts to a pin per the session-100 line's pre-printed correction protocol (RA-4); the battery blocks below keep the candidate label verbatim as the honest history of the claim's life.

**The tier, and its boundary.** This reaction appears in this book at one scale only: **gram-scale demonstration, outdoors or in a fume hood, on a non-combustible surface** (a steel lid or a brick), no confining vessel ever (the spent mass and any steam must vent freely; the Charter's never-sealed rule), full eye and hand protection, nothing added to the pile (no fuels, no powders, no "improvements"), and the residue allowed to cool completely before disposal. Never scale up: the induction period that is a curiosity at one gram becomes, at larger charge, a self-accelerating oxidation you cannot stop — this is Lecture 1's autoignition lesson wearing a lab coat. And the boundary past this tier is P18, absolute: the oxidizer shelf above the demonstration tier (Ch 16's fence), any energetic mixture, any propellant or pyrotechnic composition — recognized, never made (the safety table's row 8).

Why teach it at all? Because it is the *cleanest visible instance* of what every ignition is: an oxidation whose own heat runs its rate past its threshold. Watch the delay once and you understand the ember, the coal, the self-heating rag pile, and the compost heap's warm core as members of one family.

## Lecture 5 — Fuels, fire lays, and carrying fire

### The fuel arithmetic

A fuel's heating value is its price per kilogram, honestly banded because wood is a variable material [convergent bands, with the chapter's model inputs stated]:

| Fuel | Model input | Measured band |
|---|---|---|
| Rain-wet wood | 8 MJ/kg | moisture costs up to half the dry value |
| Seasoned (air-dry) wood | 16 MJ/kg | 15–19 MJ/kg across species and seasoning |
| Oven-dry wood | 20 MJ/kg | 18.5–19 MJ/kg for oven-dry woods |
| Charcoal | 30 MJ/kg | the standard figure for lump charcoal |

The wet row's honesty is the one that matters outdoors: **moisture attacks twice** — it subtracts flammable mass (water is not fuel), and it demands heat to boil off (the hiss of Lecture 2), and the literature's "up to half" is the band's honest spread [convergent: seasoned 15–19, oven-dry 18.5–19, wet loses up to half]. The band's edges, not its middle, are what the fire-builder must survive — which is why the exercises price the same kettle at all four model inputs, and why the answer is not one number but a discipline: split it, shelter it, stand dead wood over ground wood.

To these the fire adds the oils and fats of the reagent network: **fatwood** — pine stumps resin-soaked over years, the tree's own wound chemistry concentrated — is kindling with both high energy density *and* volatile ignitables (resin is a terpene chemistry the extraction chapter already knows how to read; [register]: field canon's standard natural kindling, used as *kindling*, never as a poured accelerant). Fats and oils (Ch 23's shelf) burn with a sootier flame and a wick's help — the lamp chemistry FC2 will build on. Resin, fat, and the alcohol shelf's clean flames are the household shelf's contribution to the fuel table, each already owned by its chapter; here they only join the budget.

### The fire lay: P17's engineering exam

A fire lay is not a stack of wood; it is a **chosen release-rate curve**, drawn in sticks. The field canon's standard lays, each a rate choice [register: SAS Survival Handbook, Bushcraft 101]:

- **The teepee** — maximal surface, fast flame, radiant ignition of each successive stick: the highest rate; the fire that must work *now* (and the one that must be fed constantly — rate cuts both ways).
- **The log cabin** — a lattice of graduated thicknesses: coals built in the middle while flame works the corners; the cooking fire's steady middle rate.
- **The star** — thick logs fed inward from points of a star, pushed in as they burn: rate control by *position*, the longest sleep a fuel load can give you.
- **The long fire** — the group-warmth lay: a wall of flame the length of the sleepers, with the night's fuel measured by the log, not the armload.

Wet weather is where the geometry earns its keep: the **split-wood technique** — standing dead wood, split open, because the outside of a branch that has rained all day is wet but the heart of a standing dead branch is dry; and **feather sticks** — dry heartwood shaved into a fan of curls, which is nothing but tinder manufactured from fuel stock, surface-to-mass restored by the knife. The platform and the windbreak are the same lesson in a different axis: keep the fire's heat under the fire and the wind from stealing it.

### Carrying fire: the coal box

The last skill of the chapter dissolves the line between fire and chemistry entirely. **Fire can be carried — not as flame but as banked char**, a slow surface oxidation held at the rate you choose: coals buried in ash or dry earth in a ventilated tin, or a smoldering punk-and-charcoal charge in a "fire can," breathing through a lid gap sized to the burn you want (P17 to the last: the lid gap is the wick). The coal box is Lecture 4's lesson inverted — instead of an oxidation accelerating itself past ignition, you hold one *just below* flame, for hours, and call on it when you want flame again. Banking the evening fire into the morning's coals is the same move without the tin. Carried fire is fire as *infrastructure* — the difference between owning a reaction and owning a skill — and it is the practical answer to the field question "what if the ignition menu fails?" You do not relight from scratch; you never let the flame be the only copy.

---

## Lab FC1.1 — The unit-lattice engine, and the honest run history

**Engine 27 — the unit-lattice engine** — built fresh for this chapter, sharing zero code with the twenty-six prior engines of the Atlas sessions. Design: every quantity the battery computes is an **exact BigInt rational** (no floating point anywhere in the arithmetic; a value is displayed only at its final, stated precision, rounded once); every derived quantity carries its **unit-lattice dimension** — a 4-component exponent vector (M, L, T, Θ) walked by two operations, multiply (add exponents) and divide (subtract them) — so that a flux is *proven* to be M·T⁻³ rather than asserted to be; the element tables are **dual transcribed** (two independently typed tables, {C, H, O, K, Mn}, admitted in myria-units, cross-checked at row S6 before any use) behind an **admission gate** — phosphorus and any other unlisted element refused at the parser, the twelfth zero-admission chapter's discipline continued; and the **P18 restricted-name gate** refuses the charter-listed classes by name before any formula is evaluated.

**The honest run history.** Run 1 executed 39/44: five failures, every one of them a harness-side defect — the engine core clean on every computation — caught, recorded, and repaired:

1. **L6** — the charcoal-fuel row's rational was written 100× heavy (the numerator scaled ×1000 against a denominator scaled ×100): 8,635.733 g printed against the kettle's true 863.573 g.
2. **F2/F3** — the radiant-flux divisor used 4π·r where the model needs 4π·r²; row F1 passed anyway, because at r = 1 m the two forms are equal — the defect hid behind its own special case, exactly why F2 and F3 existed.
3. **X5** — the harness expected its figure in kilograms from a helper that returns grams: 10794.667 printed against an expected 10.795.
4. **PR1** — the dimension probe's *expectation* was built by dividing by TIME once where the quantity needs twice (kg·m²/s is not yet a power): the engine's lattice answer M·L²·T⁻³ stood and the hand's expectation fell.
5. The display layer's dimension renderer printed "M\*L2\*T-2\*" — cosmetic, but repaired with the rest: the clean form is M^1·L^2·T^-2.

A note in the same spirit, recorded once and not smoothed over: **the engine was rebuilt after a mid-session context compaction** (the first execution's code did not survive the compaction; the recorded defect list above is what did). The rebuild's own first drafts carried three fresh defects — a myu scale written as 1e-5 against the tables' true 1e-4, a lattice-operation arity slip, and a TIME over-division — every one caught at the self-test rows (S1–S6, F4, PR1) before any value reached the page, the session-28 lesson in the rebuild's hands too. The battery history printed below is the documented two-run record, re-executed faithfully by the rebuilt engine.

**Run 1, verbatim (the five harness defects present):**

```
T1   transcription checksum (table A, x100 scale)                      123054000 myu       PASS
S1   element admission  C (table A)                                    12.011 g/mol        PASS
S2   element admission  H (table A)                                    1.008 g/mol         PASS
S3   element admission  O (table A)                                    15.999 g/mol        PASS
S4   element admission  K (table A)                                    39.098 g/mol        PASS
S5   element admission  Mn (table A)                                   54.938 g/mol        PASS
S6   dual transcription: table A vs table B                            IDENTICAL           PASS
P1   pin C6H10O5 (Ch 25 cellulose)                                     162.141 g/mol       PASS
P2   pin CO2 (Ch 20)                                                   44.009 g/mol        PASS
P3   pin H2O (Ch 4)                                                    18.015 g/mol        PASS
P4   pin O2 (Ch 10)                                                    31.998 g/mol        PASS
P5   pin CH4 (Ch 7)                                                    16.043 g/mol        PASS
P6   pin KMnO4 (Ch 13)                                                 158.032 g/mol       PASS
P7   pin K2CO3 (Ch 14)                                                 138.204 g/mol       PASS
P8   pin C3H8O3 (Ch 23 glycerin)                                       92.094 g/mol        PASS
N1   NEW-CANDIDATE MnO2 (zero-hit grep owed to review)                 86.936 g/mol        PASS
B1   cellulose + its 6 O2 air debt -> 6 CO2 + 5 H2O                    354.129 g CLOSES    PASS
B2   methane + its 2 O2 air debt -> CO2 + 2 H2O                        80.039 g CLOSES     PASS
B3   char + its O2 air debt -> CO2                                     44.009 g CLOSES     PASS
B4   formal ash: 6 C3H8O3 + 28 KMnO4 -> 14 K2CO3 + 28 MnO2 + 4 CO2 + 244977.460 g CLOSES   PASS
B5   MUST-FAIL: the ash row drafted one CO2 short                      GAP 44.009 g CAUGHT PASS
R1   'P' at the admission gate                                         REFUSED: element not admitted: 'P'PASS
R2   gunpowder at the P18 restricted gate                              REFUSED (P18)       PASS
R3   black powder at the P18 restricted gate                           REFUSED (P18)       PASS
R4   rat poison at the P18 restricted gate                              REFUSED (P18)       PASS
R5   fireworks mix at the P18 restricted gate                           REFUSED (P18)       PASS
R6   dynamite at the P18 restricted gate                               REFUSED (P18)       PASS
L1   heat 1.000 kg water 20->100 C (cp 4184 J/kg/K)                    334720 J            PASS
L2   vaporize 1.000 kg water (2256 J/g)                                2256000 J           PASS
L3   the kettle total (L1 + L2)                                        2590720 J            PASS
L4   wood fuel, 16 MJ/kg at 5% efficiency                              3238.400 g          PASS
L5   wood fuel, 20 MJ/kg at 10% efficiency                             1295.360 g          PASS
L6   charcoal fuel, 30 MJ/kg at 10% efficiency                         8635.733 g          FAIL  expected: 863.573 g
F1   flux at r = 1 m from a 1000 W point source                        79.58 W/m2          PASS
F2   pain-band radius (2500 W/m2)                                      0.0318 m            FAIL  expected: 0.1784 m
F3   10 kW/m2 band radius                                              0.0080 m            FAIL  expected: 0.0892 m
F4   flux dimension = power / area (lattice)                           M*T-3*              PASS
F5   power for the pain band at r = 1 m                                31416 W             PASS
X1   cellulose massed from table B (dual check)                        162.141 g/mol       PASS
X2   mol air per mol CH4 (21% O2 v/v, Ch 7 exception)                  9.524               PASS
X3   g O2 per kg cellulose                                             1184.081 g          PASS
X4   B4 exact closure as integers (no rounding)                        EXACT 49774600 myu  PASS
X5   wet-wood fuel for the kettle (8 MJ/kg at 3%)                      10794.667 g         FAIL  expected: 10.795 g
PR1  power's dimension from the lattice (kg*m2/s, /T twice)            M*L2*T-3*           FAIL  expected: M*L2*T-2*
RUN 1 VERDICT: 39/44 PASS, 5 FAIL — L6, F2, F3, X5, PR1
```

**Run 2, verbatim (the repair pass):**

```
T1   transcription checksum (table A, x100 scale)                      123054000 myu       PASS
S1   element admission  C (table A)                                    12.011 g/mol        PASS
S2   element admission  H (table A)                                    1.008 g/mol         PASS
S3   element admission  O (table A)                                    15.999 g/mol        PASS
S4   element admission  K (table A)                                    39.098 g/mol        PASS
S5   element admission  Mn (table A)                                   54.938 g/mol        PASS
S6   dual transcription: table A vs table B                            IDENTICAL           PASS
P1   pin C6H10O5 (Ch 25 cellulose)                                     162.141 g/mol       PASS
P2   pin CO2 (Ch 20)                                                   44.009 g/mol        PASS
P3   pin H2O (Ch 4)                                                    18.015 g/mol        PASS
P4   pin O2 (Ch 10)                                                    31.998 g/mol        PASS
P5   pin CH4 (Ch 7)                                                    16.043 g/mol        PASS
P6   pin KMnO4 (Ch 13)                                                 158.032 g/mol       PASS
P7   pin K2CO3 (Ch 14)                                                 138.204 g/mol       PASS
P8   pin C3H8O3 (Ch 23 glycerin)                                       92.094 g/mol        PASS
N1   NEW-CANDIDATE MnO2 (zero-hit grep owed to review)                 86.936 g/mol        PASS
B1   cellulose + its 6 O2 air debt -> 6 CO2 + 5 H2O                    354.129 g CLOSES    PASS
B2   methane + its 2 O2 air debt -> CO2 + 2 H2O                        80.039 g CLOSES     PASS
B3   char + its O2 air debt -> CO2                                     44.009 g CLOSES     PASS
B4   formal ash: 6 C3H8O3 + 28 KMnO4 -> 14 K2CO3 + 28 MnO2 + 4 CO2 + 244977.460 g CLOSES   PASS
B5   MUST-FAIL: the ash row drafted one CO2 short                      GAP 44.009 g CAUGHT PASS
R1   'P' at the admission gate                                         REFUSED: element not admitted: 'P'PASS
R2   gunpowder at the P18 restricted gate                              REFUSED (P18)       PASS
R3   black powder at the P18 restricted gate                           REFUSED (P18)       PASS
R4   rat poison at the P18 restricted gate                             REFUSED (P18)       PASS
R5   fireworks mix at the P18 restricted gate                          REFUSED (P18)       PASS
R6   dynamite at the P18 restricted gate                              REFUSED (P18)       PASS
L1   heat 1.000 kg water 20->100 C (cp 4184 J/kg/K)                    334720 J            PASS
L2   vaporize 1.000 kg water (2256 J/g)                                2256000 J           PASS
L3   the kettle total (L1 + L2)                                        2590720 J            PASS
L4   wood fuel, 16 MJ/kg at 5% efficiency                              3238.400 g          PASS
L5   wood fuel, 20 MJ/kg at 10% efficiency                             1295.360 g          PASS
L6   charcoal fuel, 30 MJ/kg at 10% efficiency                         863.573 g           PASS
F1   flux at r = 1 m from a 1000 W point source                        79.58 W/m2          PASS
F2   pain-band radius (2500 W/m2)                                      0.1784 m            PASS
F3   10 kW/m2 band radius                                              0.0892 m            PASS
F4   flux dimension = power / area (lattice)                           M^1·T^-3            PASS
F5   power for the pain band at r = 1 m                                31416 W             PASS
X1   cellulose massed from table B (dual check)                        162.141 g/mol       PASS
X2   mol air per mol CH4 (21% O2 v/v, Ch 7 exception)                  9.524               PASS
X3   g O2 per kg cellulose                                             1184.081 g          PASS
X4   B4 exact closure as integers (no rounding)                        EXACT 49774600 myu  PASS
X5   wet-wood fuel for the kettle (8 MJ/kg at 3%)                      10794.667 g         PASS
PR1  power's dimension from the lattice (kg*m2/s, /T twice)            M^1·L^2·T^-3        PASS
RUN 2 VERDICT: 44/44 PASS — CLEAN
```

**How to read the battery.** T1–S6 are the transcription discipline (the ×100 checksum guards dropped-digit slips; the dual tables are proven identical before use). P1–P8 are regression pins — eight compositions whose masses earlier chapters own, re-derived from this engine's own tables, the chapter claiming nothing on loan. N1 was the one candidate mass, honestly labeled pending its grep; the session-112 grep discharged the debt against the claim and the row converts to a reused pin (Ch 12) — RA-4. B1–B5 price the "air debt" of each fuel (the oxygen it must borrow to burn) and close the formal-ash model, with B5 a deliberately wrong row proving the gate still bites. R1–R6 are the refusal battery — the admission gate and the P18 gate, refusals printed as content. L1–L6 are the kettle arithmetic of the exercises (c_p 4,184 J/kg·K and latent heat 2,256 J/g — Ch 7's and Ch 6/7's own figures respectively, reused as pins; the c_p attribution corrected by RA-5, the latent-heat precision by RA-6). F1–F5 and PR1 are the ignition-distance model of Lab FC1.2. X1–X5 are the cross-checks. The π of the flux rows is carried as the exact rational 355/113, labeled on the page — the engine keeps even its transcendental concessions honest.

## Lab FC1.2 — The ignition-distance table, and one model's honesty

How close is too close? For a small flame, the question has a model: treat the source as a point radiating power P uniformly in all directions; the radiant flux at distance r is P divided by the sphere it has filled:

> **flux = P / (4π·r²)** [flagged model: the point-source radiant model; π = 355/113, labeled]

The battery prices it [computed]: at **1 m from a 1 kW point source, 79.58 W/m²** (F1) — warm, harmless. Turn the model around and ask what distance a small source needs for a given band: the **pain band at 2.5 kW/m² sits at 0.1784 m** (F2) and the **10 kW/m² injury band at 0.0892 m** (F3) — for that same 1 kW source. Ask it the other way — what source power would put the pain band a full meter out — and the model answers **31,416 W** (F5): thirty-one kilowatts, a bonfire, not a burner. The 1/r² law is fierce in both directions: distance is cheap protection, and doubling your standoff quarters your dose.

The literature anchors the bands [convergent]: a flare-exposure study's pain cases sit around **3.16 kW/m²**, squarely in the model's pain-band neighborhood, and the burn-tolerance literature's exposure times fall from minutes at the pain band to seconds at the ~10 kW/m² band — the reason "close enough to be burned" and "too close" are separated by centimeters, not meters, for small sources.

**The model's honesty line, stated before you use it.** A real flame is not a point: it has geometry, it convects (the plume above a fire carries far more heat than the radiation sideways from it), and near-field flux concentrates — which means the point-source numbers are *fair for sizing distance from a small, calm source* and *under-warn for anything bigger or closer*, where flame contact, not radiation, does the harm. Use it for the discipline it teaches — keep hands and sleeves out of the sub-decimeter zone of any burner, respect the plume above — and then trust the tetrahedron's simpler rule: if you can be touched by the flame, you are inside every band at once.

---

## Exercises

Solve before reading the answers already printed in the labs; every worked figure below is a battery row (session-102 line). Grades: ● light, ●●● summit, ◆ worked answer withheld until the session-112 Revision Appendix, ◐ open.

**FC1.1 — The kettle's ledger (●○○).** One liter of water (1.000 kg) starts at 20 °C in a pot over an open fire. (a) How much heat brings it to 100 °C? (b) How much heat boils it all away? (c) The total? *Answers:* (a) 4,184 J/kg·K × 80 K = **334,720 J**; (b) **2,256,000 J** (2,256 J/g, Ch 6/7's pin — Ch 6 states 2.26 MJ/kg, the exact 2,256 J/g form is Ch 7's RA-1-corrected pin; RA-6); (c) **2,590,720 J** (L1–L3). *Ways:* the band arithmetic per row, or the engine's exact rationals re-added — L3 is the proof that both routes close identically. [computed]

**FC1.2 — Air debts (●○○).** (a) A mole of methane plus the oxygen it must borrow from the air to burn completely — CH4 + 2 O2 → CO2 + 2 H2O — has what total charge? (b) Expressed as moles of *air* per mole of methane (air is 21% O2 by volume — the same convention Ch 7's combustion table used, its one exception to weighing everything it burns)? (c) And for a mole of char (carbon): C + O2 → CO2, what charge? *Answers:* (a) **80.039 g** (B2); (b) **9.524 mol air** (X2); (c) **44.009 g** (B3). *Ways:* per-species masses summed, or the whole-side total from the balance row — the same number both ways is what "closes" means. [computed]

**FC1.3 — The firewood budget (●●○).** The same kettle (2,590,720 J delivered to the pot) over two fires: seasoned wood at 16 MJ/kg burned at 5% pot-capture efficiency, and oven-dry wood at 20 MJ/kg burned at 10%. (a) The fuel price of each. (b) Which input — energy density or efficiency — moved the price more? *Answers:* (a) **3,238.400 g** and **1,295.360 g** (L4, L5). (b) The 25% gain in fuel quality bought exactly a **20% price cut** (3,238.400 → 2,590.720 g, efficiency held — the review battery's RD1); doubling efficiency alone bought exactly **50%** (→ 1,619.200 g at 16 MJ/kg — RD2); the two together cut the price 60% (→ 1,295.360 g, L5) — *efficiency dominates*, which is why the fire lay (heat under the pot, windbreak, platform) is worth more than the woodpile's pedigree. (Percentages corrected by the session-112 review, RA-1; every figure battery-derived.) *Ways:* the direct rows L4/L5, or the ratio chain from L3 — the same figures both ways. The efficiency assumptions are [flagged model] inputs, stated as such. [computed]

**FC1.4 — Charcoal, and the must-fail that guards it (●●○).** (a) The same kettle over charcoal at 30 MJ/kg, 10% efficiency: the fuel price? (b) A drafted ash-model ledger, closing test run, comes up exactly 44.009 g short — what does the gate's arithmetic tell you the drafter did? *Answers:* (a) **863.573 g** (L6). (b) One CO2 vanished from the product side — the gap *is* one CO2's mass, the same 44.009 g that B5 catches by design (the must-fail row is the gate's proof-of-work: a ledger that cannot catch a deliberate one-molecule slip cannot be trusted with an accidental one). *Ways:* (a) the L6 rational 25,907,200/30,000,000 kg read straight, or L3 ÷ (30,000 J/g × 0.10). [computed]

**FC1.5 — The wet-day summit (●●●).** The rain has been falling for two days and your fuel is rain-wet wood at the table's 8 MJ/kg; the fire is a wind-battered open cook-fire managing 3% capture. (a) The fuel price of the kettle? (b) Compare all four fuels' prices for this one kettle and locate where the loss actually lives — moisture, efficiency, or energy density. *Answer (a):* **10,794.667 g — about 10.795 kg of rain-wet wood to boil one liter of water** (X5). (b) The full ladder: 1,295.360 g (dry wood, good fire) → 3,238.400 g (seasoned, careless fire) → 863.573 g (charcoal, good fire) → 10,794.667 g (wet wood, bad fire): the 8× spread from best to worst is owned *mostly* by moisture-plus-efficiency, not by the fuels' intrinsic energy (16 vs 20 MJ/kg never exceeds a 25% swing); **the discipline, not the woodpile, is the expensive variable** — which is Lecture 5's split-wood and feather-stick technique priced in kilograms. *Ways:* X5 direct, or L6's 863.573 g scaled by (30/8) × (0.10/0.03) = 12.5 — the same 10,794.667 g both ways *through the unrounded rational only*: the displayed 863.573 scaled by 12.5 gives 10,794.663, and the session-104 line rests the claim on the exact value, not the displayed one (RA-2; the review battery's RX6). [computed]

**FC1.6 — The fire that will not light (◆).** A competent practitioner, dry spruce kindling, a ferrocerium rod throwing excellent sparks, char cloth that takes a spark and then dies — three times in a row, the ember forms and the tinder bundle goes out. Diagnose the failure and prescribe the fix. *The worked answer is withheld until the session-112 Revision Appendix* (this exercise prints no figures); form your own answer from Lectures 2 and 5 before the review delivers its.

**FC1.7 — The fire census (◐).** Open, no answer promised: audit one dwelling or landscape you know. Where do the tetrahedron's four faces already meet *without* you — the heat corner (sun through glass, friction, sparks), the fuel corner, the oxidizer corner, the chain? Where is the nearest point at which you could add one face and have fire? Write the audit as a page; it is the recognition skill (P18) pointed at the oldest reaction instead of the newest container.

---

## Safety

| # | Rule | The chemistry behind it |
|---|---|---|
| 1 | **No liquid accelerants — ever.** Never start or feed any fire with gasoline, alcohol, or any flammable liquid; the fire lay is the accelerant. | Lecture 0: liquids burn as *vapor*; a poured accelerant flash-vaporizes all at once — a rate you cannot divide (P17's uncontrolled end of the scale). |
| 2 | **Oil fires: never water.** Smother (lid, larger pan), starve, cool the container. | Water dropped into burning oil flash-boils beneath the surface and ejects the oil as a fireball — Lecture 2's phase-change arithmetic, weaponized by accident. |
| 3 | **Burns: cool 10–20 minutes** under cool running water; never ice, never grease. | The skin's heat capacity is small; uncooled, the burn keeps cooking. The pain band of Lab FC1.2 (2.5 kW/m²) is the distance-discipline this row prices. [convergent first-aid guidance] |
| 4 | **Chemical ignition: gram scale, outdoors or hooded, non-combustible surface, full PPE, never sealed, never scaled up, cool fully before disposal.** | Lecture 4's tier and its boundary: the induction period is a self-accelerating oxidation — a large charge is an autoignition event you cannot call back (Lecture 1). |
| 5 | **Sparks burn what they land on.** Ferrocerium and flint-and-steel work at arm's length over a cleared base; eye protection; nothing flammable downwind. | The sparks *are* burning metal (Lecture 3) — high temperature at tiny mass, which is precisely why they start fires. |
| 6 | **Carbon monoxide: never an enclosed fire without ventilation.** No tent stoves, no indoor hearths without draft; headaches and nausea end the experiment. | Incomplete oxidation (Lecture 0's smoke) makes CO — the fire you cannot see; the oxidizer corner failing quietly. |
| 7 | **Extinguish by the tetrahedron: drown, stir, feel.** Every fire dead cold before you leave it; carried fire in rated containers with lid discipline. | Removing the oxidizer corner, then proving it with a hand (the heat corner's testimony); the coal box's lid is P17 — sized, not shut. |
| 8 | **Unknowns and the excluded classes: recognition only (P18, absolute).** Unknown containers, commercial poisons, energetic materials: identify by label, hazard class, and behavior; respond with distance, PPE, and decontamination knowledge — never make, handle, or "improve." The Charter fence is not a gap in this book; the refusal is the lesson. | Lecture 3's honest boundary and Lecture 4's tier line; the twelfth chapter whose engine refuses the restricted names at the gate (battery rows R1–R6). |

## Canon-coverage check (FC1 topics)

- **The fire tetrahedron** and the triangle-to-tetrahedron history: [register] — the fire-science entry of the session-110 canon register (URL verified at the bootstrap).
- **Paper's ignition temperature, 233 °C / 451 °F**: [convergent] — the commonly cited figure, within the measured range, per the classic compilations (the "ignition temperature of paper" pages of hypertextbook and ftloscience).
- **Wood heating values**: [convergent] — seasoned 15–19 MJ/kg, oven-dry 18.5–19 MJ/kg, wet wood losing up to half; the model inputs sit honestly against the bands — 16 mid-band (seasoned 15–19), 20 the conventional round planning figure at/just above the oven-dry band top (18.5–19), 8 half of 16 per the wet-loss datum (RA-3) — and are labeled as model inputs, not measurements.
- **Charcoal ~30 MJ/kg**: [convergent] — the standard lump-charcoal figure.
- **KMnO4 + glycerin demonstration behavior and crystal-size dependence**: [convergent] — university demonstration sheets (chem.washington.edu; colorado.edu), demonstration tier only.
- **The pain band and tolerance times**: [convergent] — the flare-exposure literature (~3.16 kW/m² case; the burn-tolerance review) anchors the 2.5 kW/m² model band and the falling exposure times.
- **Ferrocerium / mischmetal**: [register] — register level (the summary recorded at the bootstrap; no bench claim hangs on it).
- **Field technique — fire lays, feather sticks, split-wood, friction fire, coal carrying**: [register] — the field canon (SAS Survival Handbook; Bushcraft 101) owns the technique layer; this chapter owns the *chemistry* under it, and copies no procedure whose only authority is a tip.
- **Thermochemistry (heat capacity, latent heat, heating values)**: owned by Ch 7 (and Ch 26's calorimetry), reused here as pins (4,184 J/kg·K; 2,256 J/g; the combustion meter's MJ/kg rows) — no re-derivation claimed.
- **Honesty line**: no audited reference owns fire-lighting as bench chemistry — the tetrahedron-to-tinder synthesis of this chapter is the Atlas's own, every claim labeled; where the field canon and the chemistry differ in emphasis, both are stated (the technique is a skill; the skill's failure modes are chemical).

## Forward flags

- **Session 112**: the Phase-3 adversarial review of this chapter — a fresh engine sharing zero code with Engine 27; the session-100/102/104 binding lines in force; the MnO2 zero-hit grep and all pin-anchor re-greps owed there (the in-sandbox page-text grep is unavailable per the session-107 tooling record; the session-108 saved-JSON fetch pipeline is the candidate method; a code-search attempt this session returned `total_count: 0` with `incomplete_results: true` — inconclusive, recorded as such).
- **The web edition (standing debt)**: per the web-sync rule (every chapter master's update owes its web/ HTML counterpart in the same session), FC1 owes a rendered reading edition; the session-108 renderer was not durably saved and must be rebuilt from the `web/ch01-web.html` template — recorded as a debt in the project records, not silently deferred.
- **FC2 — Signal and Light**: the oil lamp and wick-sizing lecture inherits this chapter's P17 rate control (the wick is the release rate), the fuel table's fats and oils, and Lab FC1.2's radiant-flux model (night vision and signal visibility are flux questions too).

## Back flags

- **Ch 4** — water: the composition pin H2O (18.015), the kettle arithmetic's foundation; the c_p pin (4,184 J/kg·K) lives in Ch 7, whose calorimetry owns it (attribution corrected, RA-5).
- **Ch 6** — distillation: the latent-heat datum (2.26 MJ/kg) reused as L2; the exact 2,256 J/g form is Ch 7's pin (RA-6).
- **Ch 7** — Heat, Fire, and Fuels: the ancestor chapter; the combustion meter's MJ/kg convention, CH4 (16.043), and the air-debt exception (X2's 21% v/v air) are its rulings, honored here.
- **Ch 13** — Analysis Without Instruments: KMnO4 (158.032) pinned at the analyst's bench; the permanganate's discipline re-referenced at the demonstration tier.
- **Ch 14** — Alkalis and Carbonates: K2CO3 (138.204), the formal ash's carbonate row.
- **Ch 20** — Nitrogen and Ammonia: CO2 (44.009), the gas the ash model vents.
- **Ch 23** — Fats, Soaps, and Esters: glycerin (C3H8O3, 92.094) and the fats shelf that joins the fuel table.
- **Ch 25** — Kinetics You Can Watch: cellulose (C6H10O5, 162.141); and the Arrhenius ladder that Lecture 4's induction period walks.
- **Ch 28** — Hazard Recognition and Neutralization: P18's Vol III ancestor — the recognition apparatus this chapter's safety row 8 inherits and extends to the Charter fence.
- **Ch 33** — Cleaning-Product Chemistry: the surfactant shelf's wetting chemistry, adjacent to wet-weather technique's real enemy (water's skin).
- **Ch 34** — Plant and Medicinal Extractions: the resin chemistry that fatwood and the pitch shelf embody.
- **P17** (release-rate control) and **P18** (recognition-not-synthesis): both load-bearing from their first chapter.

## Chapter Ledger

- **Pins claimed (P1–P8, with anchors)**: C6H10O5 162.141 (Ch 25); CO2 44.009 (Ch 20); H2O 18.015 (Ch 4); O2 31.998 (Ch 10); CH4 16.043 (Ch 7); KMnO4 158.032 (Ch 13); K2CO3 138.204 (Ch 14); C3H8O3 92.094 (Ch 23). All eight re-derived from this chapter's own dual tables [computed]; the anchor re-greps are discharged at the session-112 review — every anchor verified present in its named chapter (counts in the Revision Appendix's grep table).
- **New composition claimed**: MnO2 86.936 [computed] — the claim is **withdrawn by the session-112 grep**: the mass was already pinned in Ch 12 (the alkaline cathode), re-used recognition-only in Ch 16/18/19, and cross-referenced in Ch 25/26; the row converts to a reused pin (Ch 12) per the session-100 line's pre-printed correction protocol (RA-4).
- **Balances**: B1–B4 close; B5 the must-fail caught at exactly one CO2 (44.009 g). The formal-ash model is [flagged model] — bookkeeping exact, mechanism disclaimed.
- **Gates**: the admission gate ('P' refused — the twelfth zero-admission chapter) and the P18 restricted-name gate (five refusals) — both printed as battery rows, not asserted.
- **Engine provenance**: Engine 27, the unit-lattice engine — fresh build, zero code shared with the twenty-six prior engines; exact BigInt rationals; 4-D unit lattice (M, L, T, Θ) carried and proven on derived quantities; dual transcribed admission-gated element tables in myu (checksum row T1: 123,054,000 myu; dual tables identical, S6); honest run history 39/44 → 44/44 with the five harness defects named; post-compaction rebuild provenance recorded in Lab FC1.1, the rebuild's own three gate-caught defects printed, not smoothed.
- **Figures discipline**: every decimal figure outside the battery block is either a battery value, a battery value's labeled unit restatement, or a [convergent]/[register] datum named to its source; the model inputs (16/20/8/30 MJ/kg; 5%/10%/3%; 2.5 kW/m²; 21% v/v) are [flagged model] or [convergent] inputs, stated where used. [speculative] nowhere.
- **Owed**: the FC1 web edition only (web-sync debt, renderer rebuild required from the web/ch01-web.html template — standing). The MnO2 zero-hit grep and the pin-anchor re-greps are discharged (session 112; grep table in the Revision Appendix); Ex FC1.6's withheld worked answer is delivered in the Revision Appendix, machine-verified.

*The oldest reaction, then: a threshold, a ladder, a menu of concentrated heat, and a rate you choose. Everything else in the Field Companion is downstream of a lit fire.*

## Revision Appendix (session 112 — the adversarial review)

**The review engine.** Engine 28, the prime-product review engine — a fresh build sharing zero code with Engines 1–27: compositions and reaction balance as prime products (C=2, H=3, O=5, K=7, Mn=11 — balance is product equality by unique factorization); masses as BigInt myu displayed by digit-wise long division (no rational type anywhere); heat and flux as fixed-point BigInt at 10^9 with an integer Newton square root (no Math.*); dimensions as prime products (M=2, L=3, T=5, Θ=7), factorized for display; a regex-free parser, admission gate, and P18 restricted gate. The element tables {C,H,O,K,Mn} were re-transcribed independently — twice, identity-proved (RS6) — and the chapter's own two printed battery blocks were read in-sandbox and verified row by row (MV1–MV9).

**Honest run history.** Run 1 verified **61/63** — both FAILs were harness-side counting defects in the manuscript-verification rows (the must-fail row's own "MUST-FAIL:" label polluted a naive substring count of the printed blocks; the engine core was clean on all 63 rows). The two failing rows, verbatim:

```
MV8  manuscript run-1 block FAIL rows counted                      6 FAIL rows                             FAIL: expected 5
MV9  manuscript run-2 block rows counted                           44 PASS rows, 1 FAIL                    FAIL: expected 44/0

ENGINE 28 RUN 1 VERDICT: 61/63 PASS, 2 FAIL
CANVAS READ: 51219 chars (FC1 manuscript, in-sandbox verification)
```

Repaired per the house precedent and re-run. **Run 2 verified 63/63 — CLEAN**, verbatim:

```
ENGINE 28 — the prime-product review engine (session 112; fresh build, zero code shared with Engines 1-27)
Design: prime-product compositions and balance (unique factorization); BigInt myu masses with
digit-wise long division (no rationals); fixed-point 10^9 heat/flux with integer Newton sqrt (no Math.*);
prime-product dimensions factorized for display; regex-free parser, admission gate, and P18 gate.

RT0  T1 formula re-derived independently (sum table A, x100)     123054000                                     PASS
RT1  review checksum, positional (myu_i x (i+1), order C..Mn)    4931060 myu                                   PASS
RS1  element admission C (table A)                               12.011 g/mol                                  PASS
RS2  element admission H (table A)                               1.008 g/mol                                   PASS
RS3  element admission O (table A)                               15.999 g/mol                                  PASS
RS4  element admission K (table A)                               39.098 g/mol                                  PASS
RS5  element admission Mn (table A)                              54.938 g/mol                                  PASS
RS6  dual transcription: table A vs table B re-transcribed       IDENTICAL                                     PASS
RP1  pin C6H10O5 (Ch 25 cellulose)                               162.141 g/mol                                 PASS
RP2  pin CO2 (Ch 20)                                             44.009 g/mol                                  PASS
RP3  pin H2O (Ch 4)                                              18.015 g/mol                                  PASS
RP4  pin O2 (Ch 10)                                              31.998 g/mol                                  PASS
RP5  pin CH4 (Ch 7)                                              16.043 g/mol                                  PASS
RP6  pin KMnO4 (Ch 13)                                           158.032 g/mol                                 PASS
RP7  pin K2CO3 (Ch 14)                                           138.204 g/mol                                 PASS
RP8  pin C3H8O3 (Ch 23 glycerin)                                 92.094 g/mol                                  PASS
RP9  pin MnO2 (Ch 12 — RA-4 conversion: reuse, not new)          86.936 g/mol                                  PASS
RB1  cellulose + its 6 O2 air debt -> 6 CO2 + 5 H2O              354.129 g CLOSES                              PASS
RB2  methane + its 2 O2 air debt -> CO2 + 2 H2O                  80.039 g CLOSES                               PASS
RB3  char + its O2 air debt -> CO2                               44.009 g CLOSES                               PASS
RB4  formal ash charge (the B4 equation) closes                  4977.460 g CLOSES                             PASS
RB5  MUST-FAIL: the ash row drafted one CO2 short                GAP 44.009 g CAUGHT                           PASS
RR1  'P' at the admission gate                                   REFUSED: element not admitted: 'P'            PASS
RR2  gunpowder at the P18 restricted gate                        REFUSED (P18): recognition-only               PASS
RR3  black powder at the P18 restricted gate                     REFUSED (P18): recognition-only               PASS
RR4  rat poison at the P18 restricted gate                       REFUSED (P18): recognition-only               PASS
RR5  fireworks mix at the P18 restricted gate                    REFUSED (P18): recognition-only               PASS
RR6  dynamite at the P18 restricted gate                         REFUSED (P18): recognition-only               PASS
RL1  heat 1.000 kg water 20->100 C (cp 4184 J/kg/K x 80 K)       334720 J                                      PASS
RL2  boil it away (2256 J/g x 1000 g)                            2256000 J                                     PASS
RL3  the kettle total (RL1 + RL2)                                2590720 J                                     PASS
RL4  wood 16 MJ/kg at 5% capture                                 3238.400 g                                    PASS
RL5  wood 20 MJ/kg at 10% capture                                1295.360 g                                    PASS
RL6  charcoal 30 MJ/kg at 10% capture                            863.573 g                                     PASS
RD1  RA-1 row: the fuel-only cut (20 MJ/kg, efficiency held 5%)  2590.720 g                                    PASS
RD2  RA-1 row: the efficiency-only cut (16 MJ/kg, 5%->10%)       1619.200 g                                    PASS
RD3  RA-1 percent check: RD1/RL4 = 0.800 exact (a 20% cut)       0.800 EXACT (20% cut)                         PASS
RD4  RA-1 percent check: RD2/RL4 = 0.500 exact (a 50% cut)       0.500 EXACT (50% cut)                         PASS
RF1  flux at r = 1 m from a 1000 W point source                  79.58 W/m2                                    PASS
RF2  pain-band radius (2500 W/m2), Newton isqrt                  0.1784 m                                      PASS
RF3  10 kW/m2 band radius                                        0.0892 m                                      PASS
RF4  flux dimension = power / area (prime-product lattice)       M^1·T^-3                                      PASS
RF5  power for the pain band at r = 1 m (2500 x 4pi)             31416 W                                       PASS
RPR1 power's dimension = energy / time (J / T from the lattice)  M^1·L^2·T^-3                                  PASS
RX1  cellulose massed from table B (dual check)                  162.141 g/mol                                 PASS
RX2  mol air per mol CH4 (2 / 0.21, Ch 7 exception)              9.524                                         PASS
RX3  g O2 per kg cellulose (6 x 31.998 / 162.141 x 1000)         1184.081 g                                    PASS
RX4  RB4 exact closure as integers (no rounding)                 EXACT 49774600 myu                            PASS
RX5  wet-wood summit: 8 MJ/kg at 3% capture                      10794.667 g                                   PASS
RX6  RA-2 check: the DISPLAYED 863.573 scaled by 12.5            10794.663 ≠ 10794.667 — CAUGHT (session-104)  PASS
INJ1 injected digit slip: cellulose claimed as 162.411           162.411 vs computed 162.141 — CAUGHT          PASS
INJ2 injected 100x slip: RL6 claimed as 8635.733 g               8635.733 g vs computed 863.573 g — CAUGHT     PASS
INJ3 injected swapped coefficient (13 K2CO3 + 5 CO2)             SIG MISMATCH + GAP 94.195 g — CAUGHT          PASS
INJ4 injected closure clamp: 4977.461 g claimed                  49774610 myu vs exact 49774600 myu — CAUGHT   PASS
MV1  manuscript run-1 verdict line, verbatim                     FOUND                                         PASS
MV2  manuscript run-2 verdict line, verbatim                     FOUND                                         PASS
MV3  run-1 L6 defect row, verbatim (8635.733 g FAIL)             FOUND                                         PASS
MV4  run-1 F2/F3 defect rows, verbatim (0.0318 / 0.0080)         FOUND                                         PASS
MV5  run-1 X5 kg-vs-g slip, verbatim (expected: 10.795 g)        FOUND                                         PASS
MV6  run-1 PR1 expected-dimension slip, verbatim (M*L2*T-2*)     FOUND                                         PASS
MV7  run-2 battery figures, verbatim (30 strings)                30/30 FOUND                                   PASS
MV8  run-1 block FAIL rows counted (status-only)                 5 FAIL rows                                   PASS
MV9  run-2 block rows counted (status-only)                      44 PASS rows, 0 FAIL                          PASS

ENGINE 28 RUN 2 VERDICT: 63/63 PASS — CLEAN
CANVAS READ: 51219 chars (FC1 manuscript, in-sandbox verification)
```

**The findings (each corrected in the body above; every corrected figure battery-derived — the session-102 line in force).**

- **RA-1 (REAL — arithmetic; Ex FC1.3(b)).** The drafted prose said the 25% fuel-quality gain "bought a 22% price cut" and the doubled efficiency "bought 60%." The exact arithmetic: the 25% density gain buys exactly a **20% cut** (3,238.400 → 2,590.720 g, efficiency held — RD1); doubling efficiency alone buys exactly **50%** (→ 1,619.200 g at 16 MJ/kg — RD2); 60% is the *combined* cut (→ 1,295.360 g, L5). Prose corrected in the body; RD1–RD4 added to the review battery so every corrected figure is a battery row.
- **RA-2 (REAL — the session-104 displayed-precision line; Ex FC1.5).** The drafted "*Ways*" claimed "the same 10,794.667 g both ways at displayed precision." Scaling the *displayed* 863.573 by 12.5 gives 10,794.663 — the two ways agree only through the unrounded rational. Corrected wording follows the Ch 36 precedent; the review battery's RX6 prints the slip.
- **RA-3 (REAL — canon-coverage honesty).** "The model inputs 16/20/8 MJ/kg sit inside the bands" — 20 MJ/kg sits *above* the stated oven-dry band (18.5–19). Corrected: 16 mid-band (seasoned 15–19); 20 the conventional round planning figure at/just above the band top; 8 half of 16 per the wet-loss datum.
- **RA-4 (REAL — ledger; the new-composition claim).** The MnO2 zero-hit grep — owed since session 111, discharged this session across all 36 prior masters — returned a verdict *against* the claim: MnO2 at 86.936 g/mol was first priced in **Ch 12** (the alkaline cathode's own pin), re-used recognition-only in Ch 16/18/19, and cross-referenced in Ch 25/26. The N1 row converts to a reused pin per the session-100 line's pre-printed correction protocol; the claim is withdrawn and the ledger corrected.
- **RA-5 (REAL — attribution; c_p).** The chapter attributed c_p 4,184 J/kg·K to Ch 4. The grep: Ch 4 contains no c_p anywhere (no 4,184, no 4184); the pin lives in **Ch 7** (its calorimetry and specific-heat table, web-verified in its RA-7 row) — and Ch 26's "4184" is the food kilocalorie, a different quantity. Back-flags and the battery-reading prose reattributed.
- **RA-6 (MINOR — attribution precision; latent heat).** The chapter attributed 2,256 J/g to "Ch 6's own figure." Ch 6 states the latent heat as 2.26 MJ/kg (40.65 kJ/mol); the exact 2,256 J/g form is **Ch 7's** RA-1-corrected pin (Ch 21 cross-references it as "Chapter 6/7's pin"). Reattributed jointly.

**The grep table (the session-111 debts, discharged).** All 36 prior masters were greppable this session: 28 verified local copies (repo blob sizes matched), and ch01/ch02/ch31–ch36 fetched via the saved-JSON pipeline, their plain-ASCII anchors surviving JSON escaping.

| Anchor | Named chapter | Hits | Verdict |
| --- | --- | --- | --- |
| MnO2 / MnO₂ / "manganese dioxide" / 86.936 | all 36 | 86.936 present in Ch 12, 16, 18, 19, 25, 26; text mentions in Ch 10/12/17 | **not new** — RA-4, claim withdrawn |
| H2O 18.015 | Ch 4 | 1 | anchor verified |
| latent 2,256/2256 | Ch 6 | 0 (Ch 6 prints 2.26 MJ/kg; 2256 lives in Ch 7/21) | RA-6, precision reattributed |
| CH4 16.043 | Ch 7 | 2 | anchor verified |
| O2 31.998 | Ch 10 | 3 | anchor verified |
| KMnO4 158.032 | Ch 13 | 1 | anchor verified |
| K2CO3 138.204 | Ch 14 | 2 | anchor verified |
| CO2 44.009 | Ch 20 | 6 | anchor verified |
| C3H8O3 92.094 | Ch 23 | 6 | anchor verified |
| C6H10O5 162.141 | Ch 25 | 1 | anchor verified |
| c_p 4,184/4184 | Ch 4 | 0 (Ch 7 owns it; Ch 26's 4184 is the kilocalorie) | RA-5, misattribution |

**Web spot-checks (the convergent labels re-verified this session).** Paper ignition 233 °C/451 °F remains the commonly cited figure, within the measured range (hypertextbook.com; knowscape.blog; scienceonblog.wordpress.com). The wood bands hold — seasoned 15–19 MJ/kg with wet wood losing up to half (stalmark.pl; cfnielsen.com), and FAO's ~8.2 MJ/kg for green wood independently supports the chapter's 8 MJ/kg wet model input. KMnO4 + glycerin: the university demonstration sheets and the standard write-up confirm the delayed, violent, violet-flame reaction and its kinetics dependence (chem.wisc.edu; Wikipedia). The pain band: the ~3.16 kW/m² flare case and the pain-threshold tolerance tables unchanged (mdpi.com/1996-1073/14/17/5474; PMC5718773). All convergent labels hold; no finding.

**Ex FC1.6 — the withheld worked answer, delivered (◆).** The ember forms and dies three times: the char cloth is *working* — the spark is caught, the ember exists — so the failure is downstream, in the bundle. Diagnosis: the bundle fails the **heat budget**. An ember delivers watts-scale power; damp or coarse spruce kindling demands kilojoules of drying-plus-pyrolysis before it will flame (Lecture 2's hiss — the same bill Lab FC1.1's kettle arithmetic prices), and a bundle packed tight starves the reaction of air — the oxidizer corner of the tetrahedron (Lecture 1). Prescribe: reshape the bundle into a loose bird's-nest with a cavity for the ember, finest tinder at the core graded outward (Lecture 5's split-wood and feather-stick discipline), shelter it from the wind, and feed the ember gentle, *timed* breaths — P17's release-rate control applied to the air feed. The variable that failed is technique, not materials — the same lesson the fuel-price ladder priced in Ex FC1.5. (This answer prints no new figures; the exercise's no-figures constraint stands for the exercise as printed.)

**Withdrawn objections.** None. All six findings were confirmed at the machine; no review objection was raised and withdrawn.

**Verdict: PASS WITH CORRECTIONS.** The engine core of the chapter — every battery figure, every balance, every gate, both printed run histories — verified exactly by an independent engine with a different arithmetic architecture (prime products and fixed-point against Engine 27's rationals and 4-D unit lattice). The six findings were prose, attribution, and ledger defects, all corrected in the body above. [speculative] appears nowhere in the chapter; the fence (P18) held at every gate.

**Binding line for the next review (standing, session 113 and onward):** every cross-chapter *attribution* claim — pin anchors, back-flag chapter names, "Ch N's own figure" phrases — is grep-verified against the named chapter's master **in the authoring session itself**, not owed to review. RA-4, RA-5, and RA-6 were all authoring-session-checkable with the tooling that existed; the review engine now carries attribution-verification rows (MV-style), and every future authoring battery will include them.
