# The Compound Register — the whole-Atlas compound census (session 186, 2026-11-05)

Scope: all 61 masters (manuscript/vol1 ch01–ch14, vol2 ch15–22, vol3 ch23–29, vol4 ch30–36, vol5 ch37–ch36+, vol6 ch37–44, vol7 ch45–50; field-companion fc1–fc11) — the repo masters, master-of-record.

Method (honest, register-level): pass 1 — a 287-row curated lexicon (727 case-insensitive aliases: formulas, trivial, mineral, brand and product names; word-boundary flags where substring collisions exist) matched on every line of every master; occurrence counts per compound per chapter. Pass 2 — a formula-shaped token sweep over the whole corpus, subtracting lexicon aliases, producing the phase-2 adjudication candidate list (not adjudicated here). Coverage tags — keyword-window, PROVISIONAL: a hit counts when procedure verbs (make/prepare/synthesize/distill/electrolyze/precipitate/calcine/smelt/…), sourcing verbs (buy/shelf/aisle/pharmacy/hardware/label/$/…), or recognition verbs (never/avoid/hazard/toxic/recognition/fence/…) appear within ±3 lines of a compound mention.

Tag classes: `manufactured+procured` / `manufactured` / `procured` (procedure- and/or sourcing-window evidence — the make-or-buy network working as designed); `recognition-only` (recognition-window only); `recognition-only-fence` (appears ONLY inside the fence chapters — Ch 28 hazard recognition, Ch 50 Cubane — covered BY CHARTER, not a gap); `MENTIONED-ONLY` (no window evidence anywhere — the provisional gap class, pending session-187 adjudication).

Known bounds (never laundered): pass-2 recall is bounded by the lexicon (an unnamed-in-lexicon compound is invisible to pass 1 — the candidate list is the catch-net); keyword-window tagging is proximity, not proof ("make-or-buy" lines tag both windows); hydrate formulas contain their anhydrous salts (cross-attribution, e.g. every CuSO4·5H2O mention also counts on the CuSO4 row); two rows share the alias "ferrioxalate" (cross-attribution noted); "bleach" attributes to NaOCl even on calcium-hypochlorite lines. Water is deliberately not a row (not a procurement problem). Every tag is provisional pending the session-187 adjudication unit.

## A. The register (by category)


### Category: acid-in

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| carbonic acid | H2CO3 | ch01,ch08,ch14,ch24 | 12 | manufactured+procured |
| hydrobromic acid | HBr | ch17,ch18,ch43,ch50 | 26 | manufactured+procured |
| hydrochloric acid | HCl | ch01,ch02,ch04,ch06,ch08,ch09,ch13,ch14,ch15,ch16,ch17,ch18,ch19,ch20,ch27,ch28,ch38,ch39,ch40,ch42,ch46,ch47,ch48 | 81 | manufactured+procured |
| nitric acid | HNO3 | ch04,ch05,ch15,ch20,ch23,ch32,ch39,ch43,ch45,ch49,fc5 | 91 | manufactured+procured |
| phosphoric acid | H3PO4 | ch01,fc8 | 4 | manufactured+procured |
| sulfuric acid | H2SO4 | ch02,ch06,ch08,ch09,ch12,ch13,ch14,ch15,ch16,ch17,ch18,ch19,ch20,ch22,ch23,ch25,ch27,ch28,ch36,ch43,ch45,ch46,ch48,ch49,ch50,fc7 | 261 | manufactured+procured |

### Category: acid-org

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| acetic acid | CH3COOH | ch01,ch02,ch03,ch04,ch05,ch08,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch18,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch31,ch33,ch34,ch35,ch36,ch42,ch45,ch46,ch47,fc10,fc4,fc6,fc7,fc8 | 557 | manufactured+procured |
| ascorbic acid | C6H8O6 | ch13,ch18,ch25,ch27,ch31,ch32,ch34 | 33 | manufactured+procured |
| benzoic acid | C7H6O2 | ch31 | 2 | procured |
| citric acid | C6H8O7 | ch08,ch25,ch26,ch31,ch33,ch34,ch47 | 24 | manufactured+procured |
| formic acid | CH2O2 | fc7 | 7 | manufactured+procured |
| lactic acid | C3H6O3 | ch31 | 4 | manufactured+procured |
| oxalic acid | H2C2O4 | ch02,ch04,ch09,ch15,ch20,ch23,ch24,ch40,ch50,fc2,fc3 | 51 | manufactured+procured |
| salicylic acid | C7H6O3 | ch01,ch13,ch23,ch34,ch45,fc7 | 34 | manufactured+procured |
| tannic acid | C76H52O46 | ch22,ch34,fc10,fc7,fc8,fc9 | 106 | manufactured+procured |

### Category: base

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| ammonia (aqueous) | NH3(aq) | ch01,ch03,ch08,ch09,ch10,ch13,ch14,ch16,ch18,ch19,ch20,ch21,ch24,ch28,ch29,ch31,ch33,ch35,ch36,ch46,ch47,ch49,ch50,fc1,fc10,fc3,fc5 | 280 | manufactured+procured |
| calcium hydroxide | Ca(OH)2 | ch02,ch09,ch10,ch13,ch14,ch15,ch20,ch21,ch22,ch23,ch24,ch26,ch28,ch29,ch30,ch31,ch32,ch34,ch35,ch37,ch40,ch41,fc3,fc5,fc6,fc8,fc9 | 259 | manufactured+procured |
| calcium oxide | CaO | ch02,ch14,ch15,ch21,ch24,ch26,ch29,ch30,ch34,ch40,fc5,fc6,fc9 | 243 | manufactured+procured |
| magnesium hydroxide | Mg(OH)2 | ch09,ch19,ch24,ch40 | 13 | manufactured+procured |
| potassium carbonate | K2CO3 | ch14,ch20,ch21,ch39,ch41,ch46,ch50,fc1,fc5,fc9 | 71 | manufactured+procured |
| potassium hydroxide | KOH | ch11,ch12,ch14,ch16,ch18,ch20,ch21,ch23,ch24,ch27,ch39,ch40,ch41,ch42,fc4,fc8 | 172 | manufactured+procured |
| sodium bicarbonate | NaHCO3 | ch01,ch02,ch03,ch04,ch08,ch09,ch10,ch11,ch13,ch14,ch15,ch17,ch19,ch20,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch31,ch37,ch45,ch47,ch50 | 185 | manufactured+procured |
| sodium carbonate | Na2CO3 | ch02,ch08,ch09,ch10,ch13,ch14,ch15,ch16,ch20,ch21,ch24,ch25,ch28,ch30,ch33,ch34,ch35,ch36,ch37,ch39,ch40,ch44,ch46,ch48,ch49,fc10,fc4,fc9 | 235 | manufactured+procured |
| sodium hydroxide | NaOH | ch01,ch02,ch03,ch08,ch09,ch11,ch12,ch13,ch14,ch15,ch16,ch17,ch18,ch19,ch20,ch21,ch23,ch24,ch25,ch26,ch27,ch28,ch30,ch31,ch33,ch34,ch35,ch36,ch37,ch38,ch39,ch40,ch41,ch42,ch43,ch44,ch45,ch46,ch48,ch49,ch50,fc3,fc4,fc5,fc7,fc8,fc9 | 810 | manufactured+procured |

### Category: construction

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| lime mortar | Ca(OH)2+sand | ch01,ch07,ch14,ch21,ch26,ch30,ch34,ch45,ch47,fc6,fc9 | 73 | manufactured+procured |
| portland cement | CaO·SiO2 etc. | ch01,ch03,ch05,ch10,ch11,ch12,ch14,ch15,ch18,ch19,ch20,ch21,ch24,ch27,ch30,ch32,ch35,ch36,ch37,ch38,ch39,ch40,ch41,ch42,ch43,ch44,ch45,ch46,ch50,fc11,fc2,fc5,fc6,fc7,fc9 | 229 | manufactured+procured |
| soda-lime glass | Na2O·CaO·SiO2 | ch01,ch07,ch14,ch30 | 6 | manufactured+procured |

### Category: element

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| bromine | Br2 | ch02,ch03,ch05,ch15,ch17,ch18,ch19,ch25,ch34,ch42,ch43,ch44,ch45,ch47,ch50,fc3 | 243 | manufactured+procured |
| carbon (charcoal/graphite) | C | ch01,ch02,ch03,ch04,ch05,ch07,ch10,ch11,ch12,ch13,ch14,ch16,ch17,ch18,ch22,ch26,ch27,ch28,ch29,ch37,ch38,ch39,ch40,ch42,ch43,ch49,ch50,fc1,fc11,fc2,fc3,fc5,fc7 | 166 | manufactured+procured |
| iodine | I2 | ch02,ch03,ch04,ch10,ch13,ch17,ch18,ch23,ch24,ch25,ch27,ch29,ch31,ch42,ch43,ch50,fc8 | 227 | manufactured+procured |
| lithium | Li | ch01,ch03,ch10,ch11,ch12,ch13,ch14,ch19,ch25,ch27,ch37,ch38,ch39,ch40,ch41 | 185 | manufactured+procured |
| silicon (element) | Si | ch40 | 2 | manufactured+procured |
| sulfur | S8 | ch01,ch02,ch03,ch04,ch06,ch08,ch09,ch10,ch12,ch13,ch14,ch15,ch16,ch17,ch18,ch19,ch20,ch21,ch23,ch24,ch25,ch27,ch28,ch31,ch32,ch34,ch36,ch43,ch45,ch46,ch48,ch49,ch50,fc1,fc10,fc11,fc7 | 373 | manufactured+procured |
| white phosphorus | P4 | fc2 | 9 | manufactured+procured |

### Category: fence

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| black powder | KNO3+S+C | ch11,ch17,ch21,fc1,fc6 | 31 | manufactured+procured |
| cubane | C8H8 | ch43,ch50 | 69 | manufactured+procured |
| mercuric chloride | HgCl2 | ch43 | 6 | manufactured+procured |
| nitrocellulose | [C6H7O2(ONO2)3]n | ch15,ch16 | 5 | manufactured+procured |
| nitroglycerin | C3H5N3O9 | ch23,fc6 | 11 | manufactured+procured |
| octanitrocubane | C8(NO2)8 | ch50 | 14 | recognition-only-fence |
| potassium chlorate | KClO3 | ch16,ch42 | 21 | manufactured+procured |
| sodium chlorate | NaClO3 | ch16,ch42 | 5 | manufactured+procured |
| thermite | Fe2O3+Al | ch06,ch11,ch19,ch20,ch21,ch23,ch24,ch28 | 45 | manufactured+procured |
| trinitrotoluene (TNT) | C7H5N3O6 | fc6 | 10 | manufactured+procured |

### Category: fence-adj

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| ammonium nitrate | NH4NO3 | ch09,ch15,ch20,ch26,ch28,ch29,ch49,fc5 | 76 | manufactured+procured |

### Category: fertilizer

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| ammonium phosphate | (NH4)3PO4 | ch20 | 8 | manufactured+procured |
| superphosphate | Ca(H2PO4)2 | fc5 | 3 | manufactured+procured |

### Category: food

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| glucose | C6H12O6 | ch10,ch21,ch22,ch25,ch26,ch27,ch31,ch34,ch35,ch36,ch48,fc10,fc5,fc6,fc7 | 156 | manufactured+procured |
| starch | (C6H10O5)n | ch01,ch02,ch13,ch17,ch18,ch24,ch25,ch27,ch31,ch34,ch35,ch36,fc7 | 75 | manufactured+procured |
| sucrose | C12H22O11 | ch02,ch03,ch04,ch05,ch07,ch21,ch26,ch31,ch34,fc10,fc7,fc8 | 102 | manufactured+procured |

### Category: gas

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| acetylene | C2H2 | ch35,ch45,fc2,fc3 | 21 | manufactured+procured |
| ammonia gas | NH3 | ch20 | 2 | manufactured+procured |
| butane | C4H10 | ch01,ch07,ch21,fc1 | 11 | manufactured+procured |
| carbon dioxide | CO2 | ch02,ch03,ch04,ch07,ch08,ch09,ch10,ch11,ch13,ch14,ch15,ch19,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch30,ch31,ch33,ch34,ch35,ch36,ch37,ch38,ch39,ch40,ch45,ch47,ch49,ch50,fc1,fc10,fc11,fc2,fc3,fc5,fc6,fc7,fc8,fc9 | 503 | manufactured+procured |
| carbon monoxide | CO | ch07,ch10,ch28,ch40,fc1,fc11 | 24 | manufactured+procured |
| chlorine | Cl2 | ch01,ch02,ch03,ch04,ch08,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch17,ch18,ch19,ch20,ch22,ch24,ch25,ch26,ch27,ch28,ch30,ch31,ch32,ch33,ch40,ch41,ch42,ch43,ch44,ch45,ch46,ch47,fc11,fc3,fc4 | 334 | manufactured+procured |
| ethylene | C2H4 | ch02,ch14,ch15,ch21,ch34,ch35,ch45,ch47,ch50,fc3 | 54 | manufactured+procured |
| hydrogen | H2 | ch03,ch04,ch06,ch07,ch08,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch18,ch19,ch20,ch21,ch23,ch25,ch26,ch27,ch31,ch32,ch34,ch35,ch37,ch38,ch39,ch42,ch43,ch44,ch47,ch48,ch50,fc11,fc3,fc4,fc5 | 240 | manufactured+procured |
| hydrogen sulfide | H2S | ch10,ch17,ch18,ch19 | 18 | manufactured+procured |
| methane | CH4 | ch03,ch07,ch10,ch21,ch26,ch28,ch34,ch45,fc1,fc11,fc2,fc5 | 83 | manufactured+procured |
| nitric oxide | NO | ch20,ch49 | 4 | manufactured+procured |
| nitrogen | N2 | ch02,ch03,ch04,ch10,ch13,ch15,ch19,ch20,ch22,ch26,ch29,ch30,ch34,ch35,ch46,ch47,ch48,ch49,fc11,fc5,fc7,fc8,fc9 | 119 | manufactured+procured |
| nitrogen dioxide | NO2 | ch03,ch15,ch20,ch49 | 28 | manufactured+procured |
| nitrous oxide | N2O | ch03,ch20,ch28,ch49 | 21 | manufactured+procured |
| oxygen | O2 | ch03,ch04,ch07,ch08,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch17,ch18,ch19,ch20,ch21,ch22,ch23,ch25,ch26,ch27,ch28,ch30,ch31,ch32,ch33,ch34,ch35,ch37,ch38,ch39,ch40,ch41,ch42,ch43,ch44,ch46,ch47,ch48,ch49,ch50,fc1,fc10,fc11,fc2,fc3,fc4,fc5,fc6,fc7,fc8 | 777 | manufactured+procured |
| propane | C3H8 | ch01,ch07,ch21,ch49,fc11 | 39 | manufactured+procured |
| sulfur dioxide | SO2 | ch17,ch18,ch24,ch25,ch26,ch31,fc10 | 44 | manufactured+procured |
| sulfur trioxide | SO3 | ch06,ch17 | 4 | recognition-only |

### Category: indicator

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| litmus | dye | ch10,ch20,ch22,ch27,fc10 | 34 | manufactured+procured |
| methyl orange | indicator | ch08,ch14,ch22 | 25 | manufactured+procured |
| phenolphthalein | C20H14O4 | ch08,ch09,ch14,ch22,ch23,ch27,fc10 | 49 | manufactured+procured |

### Category: metal

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| aluminum (metal) | Al | ch07,ch11,ch14,ch19,ch43,ch49 | 16 | manufactured+procured |
| antimony (metal) | Sb | ch03,ch11,ch19 | 4 | manufactured+procured |
| bismuth (metal) | Bi | ch02,ch13,ch29 | 11 | manufactured+procured |
| cadmium | Cd | ch22,ch31 | 3 | manufactured+procured |
| chromium (metal) | Cr | ch01,ch03,ch09,ch11,ch12,ch19,ch20,ch21,ch23,ch24,fc8 | 21 | manufactured+procured |
| copper (metal) | Cu | ch01,ch03,ch11,ch12,ch19,ch27,ch32,ch39,ch43 | 29 | manufactured+procured |
| gold | Au | ch03 | 1 | manufactured+procured |
| iron (metal) | Fe | ch01,ch02,ch11,ch19,ch40 | 9 | manufactured+procured |
| lead (metal) | Pb | ch44 | 1 | manufactured+procured |
| magnesium (metal) | Mg | ch19,ch37,ch40,ch41 | 13 | manufactured+procured |
| manganese (metal) | Mn | ch03,ch10,ch12,ch16,ch18,ch19,ch23,ch25,ch26,ch27,ch31,ch32,ch39,ch43,fc1 | 38 | manufactured+procured |
| mercury | Hg | ch11,ch19,ch20,ch26,ch31,ch37,ch40,ch41,ch42,ch43,ch44,ch45,ch50 | 152 | manufactured+procured |
| nickel (metal) | Ni | ch02,ch08,ch12,ch20,ch23,ch27,ch28,ch37,ch39,ch43,ch47 | 44 | manufactured+procured |
| platinum | Pt | ch40,ch41,ch42,ch43 | 6 | manufactured+procured |
| silver (metal) | Ag | ch13,ch32 | 3 | manufactured+procured |
| sodium (metal) | Na | ch21,ch37,ch40,ch41,ch45,ch50 | 17 | manufactured+procured |
| tin (metal) | Sn | ch01,ch02,ch19,ch39,ch44,ch47,fc3 | 39 | manufactured+procured |
| zinc (metal) | Zn | ch02,ch11 | 2 | manufactured+procured |

### Category: mineral

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| alumina (Al2O3) | Al2O3 | ch11,ch14,ch19,ch22,ch28,ch30,ch38,ch39,fc9 | 138 | manufactured+procured |
| calcium carbonate | CaCO3 | ch01,ch02,ch03,ch04,ch06,ch08,ch09,ch10,ch13,ch14,ch15,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch28,ch30,ch31,ch33,ch37,ch38,ch39,ch40,ch41,fc3,fc5,fc6,fc8,fc9 | 278 | manufactured+procured |
| calcium phosphate | Ca3(PO4)2 | ch22,ch40,fc5,fc8 | 16 | manufactured+procured |
| calcium sulfate (gypsum) | CaSO4·2H2O | ch01,ch02,ch03,ch04,ch05,ch09,ch10,ch13,ch14,ch15,ch17,ch22,ch24,ch30,ch31,ch32,ch37,ch42,fc10,fc9 | 158 | manufactured+procured |
| cinnabar | HgS | ch22,ch43 | 3 | manufactured+procured |
| clay minerals | hydrous phyllosilicates | ch05,ch07,ch17,ch30,ch38,ch42,fc3,fc5,fc8,fc9 | 111 | manufactured+procured |
| diatomaceous earth | SiO2 (amorphous) | fc4 | 8 | manufactured+procured |
| dolomite | CaMg(CO3)2 | ch30,ch40,fc5,fc9 | 47 | manufactured+procured |
| feldspar | tectosilicates | ch30,fc9 | 14 | manufactured+procured |
| galena | PbS | ch09,ch13 | 18 | manufactured+procured |
| iron sulfide | FeS | ch17 | 4 | manufactured+procured |
| kaolinite | Al2Si2O5(OH)4 | ch30,ch38,ch49,fc9 | 129 | manufactured+procured |
| plaster of Paris | CaSO4·½H2O | ch01,ch02,ch03,ch05,fc8,fc9 | 20 | manufactured+procured |
| silica (SiO2) | SiO2 | ch01,ch02,ch05,ch06,ch07,ch09,ch14,ch26,ch30,ch38,ch50,fc4,fc5,fc6,fc9 | 192 | manufactured+procured |

### Category: misc

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| iron gall ink | FeSO4+tannin | fc7 | 1 | manufactured+procured |

### Category: organic

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| beeswax | wax | ch23,fc2,fc8 | 32 | manufactured+procured |
| casein | protein | ch31,fc8,fc9 | 36 | manufactured+procured |
| cellulose | (C6H10O5)n | ch07,ch16,ch45,fc1,fc10,fc2,fc3,fc5,fc7 | 45 | manufactured+procured |
| formaldehyde | CH2O | ch13,ch21,ch35 | 9 | manufactured+procured |
| gelatin | protein | ch31,ch32,ch35,ch36,ch39,ch42,ch46,fc8,fc9 | 48 | manufactured+procured |
| glycerin | C3H8O3 | ch21,ch22,ch23,ch24,ch31,ch33,ch34,ch36,fc1,fc4,fc6,fc8 | 157 | manufactured+procured |
| hydrazine | N2H4 | ch16,ch18,ch20,ch21,ch22,ch36,ch46,ch47 | 127 | manufactured+procured |
| ketazine | organic | ch16,ch20,ch21,ch46 | 19 | manufactured+procured |
| lignin | organic | ch34,fc1 | 2 | manufactured+procured |
| linseed oil | oil | ch23 | 2 | manufactured+procured |
| menthol | C10H20O | ch34,ch37 | 17 | manufactured+procured |
| paraffin wax | wax | ch07,fc2 | 6 | manufactured+procured |
| pectin | polysaccharide | ch31,ch39,ch40,fc9 | 12 | manufactured+procured |
| phenol | C6H5OH | ch08,ch09,ch14,ch22,ch23,ch25,ch27,ch31,ch34,ch35,ch45,fc10,fc7,fc8 | 96 | manufactured+procured |
| rosin | resin | ch34,ch35,fc7 | 21 | manufactured+procured |
| shellac | resin | ch31,ch35,fc8 | 33 | manufactured+procured |
| sodium ethoxide | C2H5ONa | ch21 | 2 | manufactured+procured |
| tallow | fat | ch23,ch31,fc8 | 57 | manufactured+procured |
| urea | CH4N2O | ch02,ch16,ch20,ch35,ch36,ch46,ch49,fc10,fc11,fc5 | 227 | manufactured+procured |

### Category: oxide

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| antimony trioxide | Sb2O3 | ch02 | 1 | manufactured+procured |
| chromium(III) oxide | Cr2O3 | ch02,ch11,ch19,fc9 | 10 | manufactured+procured |
| cobalt oxide | CoO | ch39 | 1 | manufactured+procured |
| copper(I) oxide | Cu2O | ch11,ch19,ch22 | 6 | manufactured |
| copper(II) oxide | CuO | ch11,ch15,ch19,ch20,ch22,ch34,fc5,fc9 | 58 | manufactured+procured |
| iron(II,III) oxide | Fe3O4 | ch03,ch11,ch19,ch22,fc9 | 38 | manufactured+procured |
| iron(III) oxide | Fe2O3 | ch03,ch11,ch12,ch19,ch22,ch25,ch26,ch28,ch30,ch32,ch38,fc6,fc9 | 70 | manufactured+procured |
| lead dioxide | PbO2 | ch12,ch19 | 6 | recognition-only |
| lead(II) oxide | PbO | ch12,ch19,ch22,ch23,ch30,ch44,fc4 | 38 | manufactured+procured |
| manganese dioxide | MnO2 | ch10,ch12,ch16,ch18,ch19,ch25,ch26,ch39,fc1 | 46 | manufactured+procured |
| red lead | Pb3O4 | ch13,ch37,ch38,ch39,ch40,ch41,ch42 | 81 | manufactured+procured |
| silver(I) oxide | Ag2O | ch12,ch32 | 4 | manufactured+procured |
| titanium dioxide | TiO2 | ch22,fc9 | 4 | manufactured+procured |
| vanadium pentoxide | V2O5 | ch02,ch11,ch17 | 10 | manufactured+procured |
| zinc oxide | ZnO | ch11,ch12,ch19,ch22,ch34 | 28 | manufactured+procured |

### Category: oxidizer

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| calcium hypochlorite | Ca(OCl)2 | ch16,ch18,ch28,fc3 | 13 | manufactured+procured |
| hydrogen peroxide | H2O2 | ch01,ch02,ch03,ch04,ch10,ch11,ch13,ch15,ch16,ch17,ch18,ch19,ch22,ch25,ch26,ch28,ch31,ch32,ch33,ch39,ch48,fc7 | 95 | manufactured+procured |
| potassium dichromate | K2Cr2O7 | ch21 | 2 | manufactured+procured |
| potassium permanganate | KMnO4 | ch08,ch13,ch16,ch17,ch18,ch21,ch28,ch32,ch43,fc1 | 90 | manufactured+procured |
| sodium percarbonate | 2Na2CO3·3H2O2 | ch16,ch33 | 3 | manufactured+procured |
| trichloroisocyanuric acid | TCCA | ch02,ch08,ch10,ch16,ch18,ch20,ch28,ch33,ch42,fc3 | 64 | manufactured+procured |

### Category: pharma

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| aspirin (acetylsalicylic acid) | C9H8O4 | ch01,ch02,ch03,ch08,ch13,ch23,ch31,ch34,ch36,ch45,ch46,fc7 | 113 | manufactured+procured |
| bismuth subsalicylate | C7H5BiO4 | ch02,ch13 | 8 | manufactured+procured |
| caffeine | C8H10N4O2 | ch21,ch31,ch34 | 55 | manufactured+procured |
| gentian violet | C25H30ClN3 | ch02,ch13,ch16 | 9 | manufactured+procured |
| glyphosate | C3H8NO5P | fc4 | 9 | manufactured+procured |
| sodium fluoride | NaF | ch18 | 1 | manufactured+procured |

### Category: pigment

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| alizarin | C14H8O4 | ch22 | 6 | manufactured+procured |
| bone black | C+Ca3(PO4)2 | ch22 | 2 | manufactured+procured |
| cochineal | dye | ch13,ch39,ch48 | 49 | manufactured+procured |
| indigo | C16H10N2O2 | ch22,ch48,fc7 | 117 | manufactured+procured |
| lead white | 2PbCO3·Pb(OH)2 | ch22,ch23 | 10 | manufactured+procured |
| lithopone | BaSO4+ZnS | ch22 | 3 | manufactured+procured |
| ochre | Fe2O3+clay | ch22 | 1 | manufactured+procured |
| prussian blue | Fe4[Fe(CN)6]3 | ch22,ch23,ch24,ch32,ch36,ch40,ch48,ch49,fc10,fc8,fc9 | 58 | manufactured+procured |

### Category: polymer

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| natural rubber | polyisoprene | ch06,ch10,ch14,ch15,ch21,ch34,ch35,ch36,ch39,ch42,ch43,ch46,fc7,fc8 | 109 | manufactured+procured |
| polyethylene | [C2H4]n | ch14,ch15,ch35,fc3 | 7 | manufactured+procured |
| polyethylene terephthalate (PET) | [C10H8O4]n | fc3 | 3 | manufactured+procured |
| polypropylene | [C3H6]n | ch35 | 1 | manufactured+procured |
| polystyrene | [C8H8]n | ch21 | 7 | manufactured+procured |
| polyvinyl chloride | [C2H3Cl]n | ch42 | 1 | manufactured+procured |
| silicone | polysiloxane | ch35,ch36 | 14 | manufactured+procured |

### Category: salt

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| aluminum sulfate | Al2(SO4)3 | ch22 | 1 | manufactured+procured |
| ammonium chloride | NH4Cl | ch12,ch14,ch15,ch19,ch20,ch49 | 45 | manufactured+procured |
| ammonium metavanadate | NH4VO3 | ch02,ch09,ch13,ch17,ch20 | 10 | manufactured+procured |
| ammonium sulfate | (NH4)2SO4 | ch02,ch03,ch04,ch20,ch32,ch34,ch35,fc5 | 40 | manufactured+procured |
| barium sulfate | BaSO4 | ch04,ch09,ch13,ch15,ch22,ch24 | 15 | manufactured+procured |
| borax (sodium tetraborate decahydrate) | Na2B4O7·10H2O | ch01,ch02,ch03,ch04,ch08,ch13,ch22,ch24,ch33,ch37,ch40,ch41,ch42,fc4,fc8 | 116 | manufactured+procured |
| boric acid | H3BO3 | ch24,fc4 | 8 | manufactured+procured |
| calcium carbide | CaC2 | ch09,ch15,ch20,ch38,ch40 | 22 | manufactured+procured |
| calcium chloride | CaCl2 | ch06,ch09,ch13,ch14,ch15,ch16,ch20,ch21,ch26,ch28,ch33,ch40,fc3,fc4 | 71 | manufactured+procured |
| calcium oxalate | CaC2O4 | ch04,ch15,ch40 | 8 | manufactured+procured |
| copper nitrate | Cu(NO3)2 | ch15,ch20 | 4 | manufactured+procured |
| copper(I) chloride | CuCl | ch05,ch09,ch43 | 5 | manufactured+procured |
| copper(II) acetate | Cu(C2H3O2)2 | ch11,ch22 | 10 | manufactured+procured |
| copper(II) carbonate | CuCO3 | ch01,ch02,ch04,ch05,ch09,ch14,ch19,ch22 | 39 | manufactured+procured |
| copper(II) chloride | CuCl2 | ch05,ch09,ch12,ch43 | 5 | procured |
| copper(II) sulfate (anhydrous) | CuSO4 | ch01,ch02,ch03,ch05,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch17,ch19,ch20,ch22,ch27,ch34,ch35 | 112 | manufactured+procured |
| copper(II) sulfate pentahydrate | CuSO4·5H2O | ch01,ch02,ch03,ch04,ch05,ch08,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch17,ch19,ch20,ch22,ch27 | 104 | manufactured+procured |
| iron(II) sulfate | FeSO4 | ch11,ch13,ch19,ch22,fc7,fc8,fc9 | 99 | manufactured+procured |
| iron(III) chloride | FeCl3 | ch11,ch13,ch15,ch22 | 12 | manufactured+procured |
| iron(III) oxalate | Fe2(C2O4)3 | ch15 | 4 | manufactured+procured |
| lead sulfate | PbSO4 | ch12,ch19 | 12 | manufactured+procured |
| magnesium chloride | MgCl2 | ch26,ch40 | 11 | manufactured+procured |
| magnesium nitrate | Mg(NO3)2 | ch20 | 9 | manufactured+procured |
| magnesium sulfate (anhydrous) | MgSO4 | ch02,ch03,ch04,ch09,ch13,ch15,ch17,ch19,ch20,ch21,ch26,ch27,ch34,ch35,ch49,fc3,fc5 | 77 | manufactured+procured |
| magnesium sulfate heptahydrate | MgSO4·7H2O | ch01,ch02,ch03,ch04,ch05,ch06,ch07,ch09,ch12,ch13,ch15,ch17,ch19,ch20,ch21,ch26,ch27,ch34,ch35,ch39,ch40,ch42,ch49,fc5 | 177 | manufactured+procured |
| potash alum | KAl(SO4)2·12H2O | ch01,ch02,ch03,ch04,ch10,ch13,ch14,ch15,ch17,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch32,fc8,fc9 | 122 | manufactured+procured |
| potassium bitartrate | KHC4H4O6 | ch02 | 2 | manufactured+procured |
| potassium bromide | KBr | ch18,ch32,ch43 | 12 | manufactured+procured |
| potassium chloride | KCl | ch13,ch14,ch16,ch17,ch18,ch20,ch22,ch25,ch27,ch29,ch40,ch41,ch46 | 133 | manufactured+procured |
| potassium ferricyanide | K3[Fe(CN)6] | ch22,ch32,ch36 | 16 | manufactured+procured |
| potassium ferrocyanide | K4[Fe(CN)6] | ch22,ch28,ch32 | 38 | manufactured+procured |
| potassium iodide | KI | ch13,ch18,ch25 | 5 | manufactured+procured |
| potassium manganate | K2MnO4 | ch08,ch16,ch17,ch18,ch21,ch43,fc1 | 53 | manufactured+procured |
| potassium nitrate | KNO3 | ch04,ch05,ch09,ch13,ch15,ch16,ch18,ch20,ch28,ch29,ch30,ch31,ch49,fc10 | 104 | manufactured+procured |
| silver chloride | AgCl | ch04,ch09,ch12,ch13,ch14,ch18,ch20,ch24,ch27,ch31,ch32,ch35,ch36 | 93 | manufactured+procured |
| silver nitrate | AgNO3 | ch02,ch09,ch11,ch13,ch15,ch18,ch19,ch20,ch27,ch32 | 45 | manufactured+procured |
| sodium acetate | CH3COONa | ch08,ch23,ch26,ch31,ch35,ch36,ch45,ch47,ch48 | 56 | manufactured+procured |
| sodium bisulfate | NaHSO4 | ch01,ch02,ch15,ch17,ch18,ch20,ch24,ch42,ch45 | 29 | manufactured+procured |
| sodium bisulfite | NaHSO3 | ch17,ch18,ch22,ch25,ch31 | 10 | procured |
| sodium bromide | NaBr | ch02,ch18,ch25,ch43,ch50 | 46 | manufactured+procured |
| sodium chloride | NaCl | ch01,ch02,ch03,ch04,ch05,ch08,ch09,ch10,ch12,ch13,ch14,ch15,ch16,ch17,ch18,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch29,ch30,ch31,ch32,ch33,ch34,ch35,ch37,ch38,ch40,ch41,ch42,ch45,ch46,ch47,ch48,ch49,fc3,fc4 | 437 | manufactured+procured |
| sodium hypochlorite | NaOCl | ch01,ch02,ch04,ch08,ch09,ch10,ch12,ch13,ch14,ch15,ch16,ch17,ch18,ch20,ch21,ch22,ch24,ch25,ch26,ch27,ch28,ch29,ch31,ch32,ch33,ch36,ch42,ch46,fc10,fc3,fc4,fc5,fc8 | 500 | manufactured+procured |
| sodium iodide | NaI | ch18 | 2 | manufactured+procured |
| sodium metabisulfite | Na2S2O5 | ch17,ch25,ch26,ch31 | 20 | manufactured+procured |
| sodium nitrate | NaNO3 | ch02,ch09,ch13,ch15,ch18,ch20,ch27,ch31,ch49 | 39 | manufactured+procured |
| sodium nitrite | NaNO2 | ch20,ch31,ch47,ch48 | 11 | manufactured+procured |
| sodium oxalate | Na2C2O4 | ch09,ch40 | 5 | manufactured+procured |
| sodium silicate | Na2SiO3 | ch09,ch14,ch24,ch30,fc9 | 23 | manufactured+procured |
| sodium sulfate | Na2SO4 | ch02,ch05,ch09,ch13,ch14,ch15,ch17,ch19,ch20,ch21,ch23,ch25,ch27,ch28,ch37,ch44,ch45,ch48,ch49,ch50 | 63 | manufactured+procured |
| sodium sulfide | Na2S | ch13,ch17,ch48 | 5 | manufactured+procured |
| sodium sulfite | Na2SO3 | ch17,ch48 | 2 | manufactured+procured |
| sodium thiosulfate | Na2S2O3 | ch01,ch17,ch18,ch25,ch26,ch32,ch33,fc9 | 45 | manufactured+procured |
| sodium tripolyphosphate | Na5P3O10 | ch33 | 8 | manufactured+procured |
| sodium vanadate | NaVO3 | ch02 | 1 | manufactured+procured |
| tin(II) chloride | SnCl2 | ch11,ch19,ch47 | 12 | manufactured+procured |
| zinc chloride | ZnCl2 | ch10,ch12,ch15,ch19,ch20 | 9 | manufactured |
| zinc sulfate | ZnSO4 | ch19,ch27 | 2 | manufactured+procured |

### Category: solvent

| Compound | Formula | Chapters (mentions) | Total | Tag |
|---|---|---|---|---|
| acetone | C3H6O | ch02,ch06,ch13,ch21,ch23,ch28,ch35,ch36,ch45,ch47,ch48,ch49,fc2 | 146 | manufactured+procured |
| benzene | C6H6 | ch21,ch31,ch44,ch50 | 8 | manufactured+procured |
| chloroform | CHCl3 | ch21 | 12 | manufactured+procured |
| diethyl ether | C4H10O | ch21,ch49,ch50 | 28 | manufactured+procured |
| ethanol | C2H5OH | ch02,ch06,ch07,ch10,ch14,ch16,ch18,ch21,ch23,ch24,ch25,ch26,ch31,ch34,ch35,ch36,ch39,ch40,ch41,ch42,ch47,ch48,ch49,ch50,fc10,fc11,fc2,fc6,fc7,fc8 | 420 | manufactured+procured |
| ethylene glycol | C2H6O2 | ch02,ch21,ch35,ch45,ch50 | 54 | manufactured+procured |
| isopropyl alcohol | C3H8O | ch01,ch02,ch21,ch33,ch41,ch48,fc2 | 27 | manufactured+procured |
| kerosene | mixture | ch07,fc2 | 16 | manufactured+procured |
| methanol | CH3OH | ch21,ch23,ch24,ch47,ch48,ch50,fc7 | 91 | manufactured+procured |
| methyl ethyl ketone | C4H8O | ch21,ch46 | 65 | manufactured+procured |
| mineral spirits | mixture | ch02 | 1 | manufactured+procured |
| naphtha | mixture | ch07,ch34 | 2 | procured |
| toluene | C7H8 | ch35,ch41,ch47,ch50 | 23 | manufactured+procured |
| turpentine | mixture | fc7 | 17 | manufactured+procured |

## B. The MENTIONED-ONLY list (the provisional gap class — session 187's adjudication queue)


## C. Phase-2 candidates (formula-shaped tokens in the corpus, NOT matched by the lexicon — counts are corpus-wide; adjudication pending)

| Count | Token |
|---|---|
| 614 | H2O |
| 132 | NH3 |
| 118 | FC1 |
| 90 | CaSO4 |
| 78 | SO4 |
| 63 | FC2 |
| 61 | C6H12O6 |
| 52 | FC7 |
| 52 | FC3 |
| 51 | NO3 |
| 51 | NH4 |
| 51 | C2H5OH |
| 50 | CO3 |
| 48 | FC10 |
| 46 | FC9 |
| 43 | FC5 |
| 39 | C6H10O5 |
| 37 | NH2 |
| 35 | CH3COONa |
| 34 | K2O |
| 34 | FC6 |
| 33 | C2H4O2 |
| 32 | C12H22O11 |
| 31 | FC4 |
| 31 | C3H8O3 |
| 30 | FC11 |
| 29 | FC8 |
| 28 | PR1 |
| 26 | CH3 |
| 24 | Li2CO3 |
| 24 | C2H6O |
| 24 | C18H36O2 |
| 23 | C3H6O |
| 23 | C2H3O2 |
| 22 | Na2O |
| 22 | Na2B4O7 |
| 22 | C2H4O |
| 19 | PR3 |
| 19 | CaC2O4 |
| 19 | C6H7NO2 |
| 19 | Al2Si2O5 |
| 18 | MgCO3 |
| 18 | C9H8O4 |
| 18 | C7H8O2 |
| 18 | C4H6O2 |
| 17 | NaC2H3O2 |
| 17 | C3H8 |
| 17 | C25H52 |
| 17 | C18H34O2 |
| 16 | NH2Cl |
| 16 | NCl3 |
| 15 | S2O3 |
| 15 | C6H8O6 |
| 14 | LiCoO2 |
| 14 | CoCl2 |
| 14 | C4H8O2 |
| 13 | CuC2O4 |
| 13 | C5H8 |
| 13 | Al2Si2O7 |
| 12 | KIO3 |
| 12 | HCO3 |
| 12 | C8H13NO5 |
| 12 | C7H6O3 |
| 11 | ZnSO4 |
| 11 | PR2 |
| 11 | K2CaSi2O6 |
| 11 | H2O1 |
| 11 | CaSiO3 |
| 11 | C76H52O46 |
| 11 | C18H33KO2 |
| 11 | C13H18O7 |
| 11 | AlCl3 |
| 10 | NaNO2 |
| 10 | NaClO3 |
| 10 | MgCl2 |
| 10 | KHSO4 |
| 10 | K2SiO3 |
| 10 | HNO2 |
| 10 | CH2 |
| 10 | C2H2O4 |
| 10 | C28H44O |
| 10 | Al6Si2O13 |
| 10 | Al2S3 |
| 9 | Na2SO3 |
| 9 | Na2S4O6 |
| 9 | H2SO3 |
| 9 | D2O |
| 9 | C2H5N3O2 |
| 9 | C18H35NaO2 |
| 9 | C18H33NaO2 |
| 9 | C16H10N2O2 |
| 9 | C10H8O4 |
| 8 | PbI2 |
| 8 | PbCrO4 |
| 8 | Na0Cl |
| 8 | Li2O2 |
| 8 | K2SO4 |
| 8 | FeCl2 |
| 8 | C6H6O6 |
| 8 | C46H92O2 |
| 8 | C3H8O |
| 8 | C2V2 |
| 8 | C2H6O2 |
| 8 | C18H35O2 |
| 8 | B2O3 |
| 7 | TRPV1 |
| 7 | Si4O10 |
| 7 | PbCl2 |
| 7 | NaBO2 |
| 7 | HSO3 |
| 7 | Ca3SiO5 |
| 7 | Ca2SiO4 |
| 7 | CH4O |
| 7 | C8H15NO6 |
| 7 | C6H11NO4 |
| 7 | C16H32O5 |
| 7 | C10H16 |
| 6 | Na2Zn |
| 6 | NHCl2 |
| 6 | Li2O |
| 6 | H2SO5 |
| 6 | Ca3Si2O7 |
| 6 | CH4N2O |
| 6 | CH3COO |
| 6 | CH2O |
| 6 | C4H8O |
| 6 | C4H10 |
| 6 | C3N3O3H3 |
| 6 | C3N3O3Cl3 |
| 6 | C2H6O6 |
| 6 | C1V1 |
| 6 | C12H26 |
| 5 | ST2 |
| 5 | ST1 |
| 5 | RD1 |
| 5 | PO4 |
| 5 | Na3AlF6 |
| 5 | Na2S |
| 5 | MnSO4 |
| 5 | Mn2O3 |
| 5 | K2CrO4 |
| 5 | H3O |
| 5 | C8H8O3 |
| 5 | C7H6O5 |
| 5 | C4H6O3 |
| 5 | C39H54N10O14S |
| 5 | C32H60O8 |
| 5 | C30H62O |
| 5 | C28H24N2O7 |
| 5 | C26H52O2 |

## D. Per-chapter compound counts

| ch01 | 39 | 131 |
| ch02 | 60 | 315 |
| ch03 | 39 | 204 |
| ch04 | 30 | 211 |
| ch05 | 19 | 120 |
| ch06 | 13 | 96 |
| ch07 | 20 | 172 |
| ch08 | 28 | 263 |
| ch09 | 42 | 250 |
| ch10 | 34 | 237 |
| ch11 | 36 | 205 |
| ch12 | 31 | 175 |
| ch13 | 55 | 287 |
| ch14 | 46 | 529 |
| ch15 | 49 | 368 |
| ch16 | 34 | 336 |
| ch17 | 39 | 369 |
| ch18 | 43 | 468 |
| ch19 | 50 | 379 |
| ch20 | 58 | 485 |
| ch21 | 52 | 623 |
| ch22 | 54 | 347 |
| ch23 | 37 | 308 |
| ch24 | 35 | 209 |
| ch25 | 35 | 178 |
| ch26 | 36 | 202 |
| ch27 | 37 | 147 |
| ch28 | 33 | 239 |
| ch29 | 12 | 40 |
| ch30 | 24 | 405 |
| ch31 | 45 | 239 |
| ch32 | 28 | 119 |
| ch33 | 20 | 200 |
| ch34 | 38 | 347 |
| ch35 | 35 | 302 |
| ch36 | 24 | 202 |
| ch37 | 21 | 208 |
| ch38 | 17 | 235 |
| ch39 | 28 | 256 |
| ch40 | 37 | 209 |
| ch41 | 20 | 173 |
| ch42 | 28 | 321 |
| ch43 | 28 | 332 |
| ch44 | 13 | 45 |
| ch45 | 26 | 265 |
| ch46 | 22 | 294 |
| ch47 | 24 | 176 |
| ch48 | 23 | 318 |
| ch49 | 29 | 224 |
| ch50 | 29 | 221 |
| fc1 | 17 | 175 |
| fc10 | 20 | 155 |
| fc11 | 13 | 162 |
| fc2 | 15 | 114 |
| fc3 | 24 | 205 |
| fc4 | 17 | 169 |
| fc5 | 28 | 216 |
| fc6 | 16 | 197 |
| fc7 | 27 | 313 |
| fc8 | 30 | 437 |
| fc9 | 32 | 637 |

*Register built in-repo by session 186's extractor; every count reproducible from audit/compound-register/occurrences.tsv + lexicon.txt. The register is a records artifact, not a chapter: extend, never rewrite.*

## E. Session 204 (2026-11-06) — the docket-E mechanical register upgrade

*Executed as the standing docket E ("execute and finish mechanical register upgrade" — the user's call at session 204). Scope per the ACTIVE-SESSION state: the lexicon/alias upgrades, the phase-2 candidate adjudication, and the discard rules — the register's pass-2 machinery brought current. Method: the fresh census re-swept all 61 masters of the 186 scope (ch01–ch50 + fc1–fc11) on the 186 extractor's own token rule; every disposition below cites that census; and every naming resolution was made by grepping the token's own source chapter before any row was written — no name invented, no count laundered. Deliverables: `audit/compound-register/lexicon-upgrade-204.txt` (NEW rows plus alias additions, pure lexicon format, the pass-1 matcher's upgrade) and this section, the adjudication of record.*

### E.1 The fresh census (receipts)

- Batch gates, exact: Region A 421 + 828 = 1,249; Region B 767 + 363 = 1,130; Region C 25 + 375 + 79 + 152 = 631; Region D 142 + 109 + 188 + 178 + 219 + 160 + 94 = 1,090.
- occTotal 4,100; distinct 562 — distinct matching the 186 candidate census exactly (SUMMARY.md: "Phase-2 candidates: 562.").
- The local fc1/fc2 mirrors byte-verified against the repo masters before the sweep (68,696 and 52,809 bytes, every count identical).

### E.2 The Section-C comparison, and the one finding

- 146 of the 150 Section-C rows reproduce exactly.
- Fold-attributed deltas (the session-189 Coverage Fold edits): H2O 614 → 617 (+3), NH3 132 → 133 (+1), Mn2O3 5 → 6 (+1), HgCl2 3 → 4 (below the Section-C cut; the fold's ch43 edit — dispositioned as an alias addition to the mercuric chloride row below).
- **THE FINDING (unattributed): FC2 63 → 62 (−1).** Not fold-attributed — the folds only added tokens. A real corpus change since 186; the most plausible cause is the session-189 ch43 fold edit dropping one "FC2" label mention (ch43 is the only FC2-bearing chapter among the six fold-edited masters; its fresh count is 1). Disclosed as found; never laundered.

### E.3 The naming resolutions (greps at the sources, this session)

| Token | The source names it | Disposition |
| --- | --- | --- |
| C6H7NO2 | ethyl cyanoacrylate — Ch 36's polymer-pair node, Ch 25's 125.127 pin (19 mentions, the largest former tail token) | NEW row |
| C4H6O2 | vinyl acetate — Ch 36's binder-wing gateway (E6: C4H6O2 + NaOH → C2H4O + CH3COONa) | NEW row |
| C2H4O | acetaldehyde — E6's product, its formula also the PVA repeat Ch 35 pinned at 44.053 (cross-attribution) | NEW row |
| C16H32O5 | aleuritic acid — FC8's N1 (304.427), the shellac monomer | NEW row |
| C30H50O2 | betulin — FC7's N2 (442.728), the birch-bark triterpene | NEW row |
| C8H15NO6 | N-acetylglucosamine — FC10's S2 (221.209), the chitin monomer | NEW row |
| C32H60O8 | FC8's own label: "the labeled polyester dimer model" (N5) — a LABELED MODEL, not a compound | reclassified: model artifact, discarded (the binding's NEW-row expectation corrected by the source grep; disclosed) |
| C7H8O2 | the orcinol / salicyl-alcohol isomer class — FC10's S11 prints 124.139, the same number Ch 34 pinned to willow's salicyl alcohol | NEW row, named as class |
| C10H16 | the limonene / α-pinene isomer class — FC7's I1 prints α-pinene as Ch 34's limonene twin | NEW row, named as class |
| C14H28O2 | myristic acid — FC8's N4, by F1 a Ch 23 pin | NEW row |
| C6H10OS2 / C6H10S2 / C3H6OS / C3H5NS | Ch 34's sulfur militia, all named at their own battery: allicin, diallyl disulfide, allylsulfenic acid, allyl isothiocyanate | NEW rows |
| C8H11N4O2Cl | caffeine hydrochloride — Ch 34's E2 row | NEW row |

### E.4 The discard rules (binding, by class)

- **D1 — water-class:** H2O, D2O, H3O, NH3O, H2O1 (the water-family convention).
- **D2 — label/identifier:** the FC/PR/ST/RD/MT/MV/RL/RX/RPb/RPR/RP/RR/RS/RB/RC/RE/RT/INJ/PB/RA label families (regex `^(FC|PR|ST|RD|MT|MV|RL|RX|RPb|RPR|RP|RR|RS|RB|RC|RE|RT|INJ|PB|RA)\d*$`), plus C3S, C2S, TRPV1, TRPA1, C1V1, C2V2, AX2E, AX2E2, M2O, LN2, NWc9BGMDaA, OrZ5Oa9K1R0, P10P, E10E, Na0Cl, PBk9, PR83 — engine/battery labels and notation shorthands, never compounds.
- **D3 — ion-fragment:** SO4, NO3, NH4, CO3, HCO3, NH2, CH3, CH3COO, HSO3, HSO4, HSO5, PO4, S2O3, S2O4, S4O6, CH2, C2O4, C2H3O2, MnO4, B4O7, ClO3, IO3, BrO3, OCH3, CH2OH, C6H3, C6H4, C6H5O7, C6H11O7, C18H35O2, C17H35COO, C7H5O3, K4Fe, NH4Al, OH4, C2H6OSi, C2H8O2Si, C6H12O4Si, C7H12O6Si, C2H5, HO2 — each owned by its parent row (citrate → citric acid; stearate → the stearate rows; salicylate → salicylic acid; gluconate → gluconate chemistry; the silicone oligomer fragments → the silicone row; the kaolinite (OH)4 artifact → kaolinite).
- **D4 — parser-battery / reversed / model artifacts:** the explicit-1 battery tokens whose stripped base matches an existing or new row were CONVERTED to alias additions (E.6); the remainder are discarded: SO42, Na2Zn, K2Zn, C33H81O2, NH4NH4, C2H4N3O2, C2H8, C4H12O2, C32H60O8, C18N18Fe7, H10O8Na2S2, O6Na4S4Cl1Ag1, C24N24Fe8, H1O4, Cu2C1O5H2, Fe1O2H1, Fe1O2H2, Fe1O3H3, Na1Al1O4H4 — engine artifacts (the fc4 2×ethanol sum row C4H12O2; FC8's labeled polyester dimer model C32H60O8; the malachite battery form Cu2C1O5H2 with no register row; the iron-complex battery sums).

### E.5 The tail (below-cut unnamed)

Retained as candidates, no row written, no name invented: C9H6O4, C8H5NO4, C19H14O5S, C8H7N3O2, C32H22N6Na2O6S2, C18H31O2, C19H36O2, C7H14O2, C6H12O2, C5H5NO2, C15H16O2, C21H24O4, C2H6N2O2, C10H11NaO2, C5H10S, C8H9NO3, C7H10O4S, C9H9N, C6H9N2Cl, C4H4BrNO2, C5H12N2O2, C5H13ClN2O2, C4H12N2, C6H15ClN2O2, C5H10N2, C5H14N2, C8H16N2, CH3ClN2O, C6H16O2, C6H6N2O2, C16H11N3O3, C12H9N3O4, C12H11N, C8H11NO2, C7H5NO3, C10H18O2, C15H20O5, C15H20O4, C4H12O4. (C15H20O5 and C15H20O4 are FC8's shellac hydroxy-fatty-acid family members — the family the chapter itself refuses to name at its own gate; that refusal is inherited here.)

### E.6 The alias additions (the mechanical upgrade)

| Row | Added alias(es) | Note |
| --- | --- | --- |
| ammonia (aqueous) | nh3, nh4oh, n1h3 | the NH3 / NH4OH faces |
| calcium sulfate (gypsum) | caso4, ca1s1o6h4 | the anhydrous and dihydrate notation |
| ethanol | c2h5oh, c2h6o, c2h6o1 | three notation faces |
| glucose | c6h12o6, o6c6h12 | incl. the reversed battery form; lactose/trehalose isomers cross-attributed |
| sodium acetate | ch3coona, nac2h3o2, c2h3nao2 | three notation faces |
| sucrose | c12h22o11 | lactose (FC8) and trehalose (FC10) are same-formula isomers |
| glycerin | c3h8o3 | the C3H8O3 face |
| aspirin (acetylsalicylic acid) | c9h8o4 | the formula face |
| salicylic acid | c7h6o3 | the formula face |
| ascorbic acid | c6h8o6 | the formula face |
| tannic acid | c76h52o46 | the ten-galloyl convention's formula face |
| indigo | c16h10n2o2 | the formula face |
| polyethylene terephthalate (PET) | c10h8o4 | repeat unit; Ch 50's cubane diacid is the same formula — cross-attribution |
| ethylene glycol | c2h6o2 | the formula face |
| propane | c3h8 | the formula face |
| kerosene | c25h52 | the formula face |
| silicone | c5h8 | isoprene repeat |
| methanol | ch4o, c1h4o1 | Hill + battery faces |
| formaldehyde | ch2o | the formula face |
| urea | ch4n2o | the formula face |
| butane | c4h10 | the formula face |
| calcium oxalate | cac2o4 | the formula face |
| sodium oxalate | na2c2o4 | the formula face |
| borax (sodium tetraborate decahydrate) | na2b4o7, b4h20na2o17 | anhydrous + decahydrate notation |
| kaolinite | al2si2o5, oh4 | the dehydroxylated sheet + the (OH)4 battery artifact |
| sodium nitrite | nano2 | the formula face |
| sodium chlorate | naclo3 | the formula face |
| magnesium chloride | mgcl2 | the formula face |
| zinc sulfate | znso4 | the formula face |
| sodium sulfite | na2so3 | the formula face |
| sodium sulfide | na2s | the formula face |
| potassium dichromate | k2cr2o7 | the formula face |
| potassium manganate | k2mno4 | the formula face |
| sodium tripolyphosphate | na5p3o10 | the formula face |
| oxalic acid | c2h2o4, c2h6o6 | anhydrous + dihydrate notation |
| trichloroisocyanuric acid | c3n3o3cl3 | the formula face |
| acetic acid | c2h4o2 | the formula face |
| formic acid | ch2o2 | the formula face |
| caffeine | c8h10n4o2 | the formula face |
| alizarin | c14h8o4 | the formula face |
| phenolphthalein | c20h14o4 | the formula face |
| beeswax | c46h92o2 | myricyl palmitate face |
| chloroform | chcl3 | the formula face |
| acetone | ch3coch3, c3h6o | two notation faces |
| methyl ethyl ketone | c4h8o | the formula face |
| diethyl ether | c4h10o | the formula face |
| benzoic acid | c7h6o2 | the formula face |
| menthol | c10h20o | the formula face |
| phenol | c6h6o | the formula face |
| lactic acid | c3h6o3 | the formula face |
| starch | c6h10o5 | repeat unit; cellulose cross-attribution |
| cellulose | c6h10o5 | repeat unit; starch cross-attribution |
| cubane | c8h8 | the formula face; polystyrene cross-attribution |
| octanitrocubane | c8n8o16 | the formula face |
| toluene | c7h8 | the formula face |
| mercuric chloride | hgcl2 | the formula face (the audit's ch43 row) |
| methyl orange | c14h14n3nao3s | the formula face |
| sodium ethoxide | nac2h5o | the formula face |
| isopropyl alcohol | c3h8o | the formula face |
| boric acid | bh3o3 | the Hill face |
| sodium silicate | o2si | the reversed face |
| sodium hypochlorite | cl2na2o2 | the (NaOCl)2 battery form |
| calcium hypochlorite | cacl2o2 | the notation face |
| sodium sulfate | na2o4s | the Hill face |
| sulfuric acid | h2o4s | the Hill face |
| potassium carbonate | k2c1o3 | the battery face |
| carbon dioxide | c1o2 | the battery face |
| sodium bromide | na1br1 | the battery face |
| hydrochloric acid | h1cl1 | the battery face |
| sodium chloride | na1cl1, na1o1cl1 | the battery faces |
| sodium hydroxide | na1h1o1, na1o1h1 | the battery faces |
| hydrobromic acid | h1br1 | the battery face |
| calcium hydroxide | cao2h2, ca1o2h2, h2o2ca1 | three battery faces |
| aluminum sulfate | k1al1s2o20h24, h24o20al1s2k1 | the written-out dodecahydrate forms |
| copper(II) sulfate pentahydrate | cu1s1o4, cu1s1o9h10 | anhydrous + pentahydrate battery forms |
| iron(II) sulfate | fe1s1o4, fe1s1o11h14 | anhydrous + heptahydrate battery forms |
| iron(III) chloride | fe1cl3 | the battery face |
| zinc oxide | zn1o1 | the battery face |
| copper(II) oxide | cu1o1 | the battery face |
| copper(I) oxide | cu2o1 | the battery face |
| calcium carbonate | ca1c1o3 | the battery face |
| sodium bicarbonate | na1h1c1o3 | the battery face |
| hydrogen peroxide | o2h2 | the reversed face |
| hydrazine | nh2nh2 | the written-out face |
| rosin | c20h30o2, c19h29co2h | abietic acid + its written-out face |
| silver chloride | cl2ag2 | the doubled battery form |
| ammonium sulfate | h8n2o4s1 | the written-out form |
| ferric ammonium sulfate | o12s3fe2 | the written-out form |
| tin(II) chloride | sn1cl2 | the battery face |
| methane | c1h4 | the battery face |
| ethylene | c2h4 | the formula face |

### E.7 The NEW rows

| Name | Formula | Category | Fresh count |
| --- | --- | --- | --- |
| lithium carbonate | Li2CO3 | salt | 24 |
| lithium cobalt oxide | LiCoO2 | mineral | 14 |
| monochloramine | NH2Cl | fence | 16 |
| nitrogen trichloride | NCl3 | fence | 16 |
| dichloramine | NHCl2 | fence | 6 |
| potassium bisulfate | KHSO4 | salt | 10 |
| potassium iodate | KIO3 | oxidizer | 12 |
| copper(II) oxalate | CuC2O4 | salt | 13 |
| cobalt(II) chloride | CoCl2 | salt | 14 |
| magnesium carbonate | MgCO3 | mineral | 18 |
| aluminum chloride | AlCl3 | salt | 11 |
| cryolite | Na3AlF6 | mineral | 5 |
| lead iodide | PbI2 | fence | 8 |
| lead chromate | PbCrO4 | fence | 8 |
| lead chloride | PbCl2 | fence | 7 |
| iron(II) chloride | FeCl2 | salt | 8 |
| manganese(II) sulfate | MnSO4 | salt | 5 |
| manganese(III) oxide | Mn2O3 | mineral | 6 |
| boron trioxide | B2O3 | mineral | 8 |
| nitrous acid | HNO2 | acid-in | 10 |
| sulfurous acid | H2SO3 | acid-in | 9 |
| Caro's acid | H2SO5 | acid-in | 6 |
| sodium metaborate | NaBO2 | salt | 7 |
| metakaolin | Al2Si2O7 | mineral | 13 |
| mullite | Al6Si2O13 | mineral | 10 |
| potassium silicate | K2SiO3 | mineral | 10 |
| potassium calcium silicate | K2CaSi2O6 | mineral | 11 |
| wollastonite (calcium silicate) | CaSiO3 | mineral | 11 |
| alite (tricalcium silicate) | Ca3SiO5 | mineral | 7 |
| belite (dicalcium silicate) | Ca2SiO4 | mineral | 7 |
| rankinite (tricalcium disilicate) | Ca3Si2O7 | mineral | 6 |
| lithium peroxide | Li2O2 | oxidizer | 8 |
| lithium oxide | Li2O | mineral | 6 |
| chitin | C8H13NO5 | polymer | 12 |
| chitosan | C6H11NO4 | polymer | 7 |
| ergosterol | C28H44O | organic | 10 |
| alpha-amanitin | C39H54N10O14S | fence | 5 |
| dehydroascorbic acid | C6H6O6 | organic | 8 |
| stearic acid | C18H36O2 | organic | 24 |
| oleic acid | C18H34O2 | organic | 17 |
| myristic acid | C14H28O2 | organic | below cut |
| palmitic acid | C16H32O2 | organic | 4 |
| lauric acid | C12H24O2 | organic | 1 |
| linoleic acid | C18H32O2 | organic | 2 |
| linolenic acid | C18H30O2 | organic | 1 |
| sodium stearate | C18H35NaO2 | salt | 9 |
| sodium oleate | C18H33NaO2 | salt | 9 |
| potassium stearate | C18H35KO2 | salt | below cut |
| potassium oleate | C18H33KO2 | salt | below cut |
| sodium laurate | C12H23NaO2 | salt | 1 |
| potassium palmitate | C16H31KO2 | salt | 2 |
| orcinol (C7H8O2 isomer class) | C7H8O2 | organic | 18 |
| potassium chromate | K2CrO4 | oxidizer | 5 |
| curcumin | C21H20O6 | organic | 4 |
| aleuritic acid | C16H32O5 | organic | 7 |
| betulin | C30H50O2 | organic | 4 |
| triacontanol | C30H62O | organic | 5 |
| cerotic acid | C26H52O2 | organic | 5 |
| limonene (C10H16 terpene class) | C10H16 | organic | 7 |
| sheet silicate unit | Si4O10 | mineral | 7 |
| biuret | C2H5N3O2 | organic | 9 |
| acetaldehyde | C2H4O | organic | 22 |
| melamine | C3H6N6 | organic | 2 |
| hydroquinone | C6H6O2 | organic | 1 |
| benzoquinone | C6H4O2 | organic | 1 |
| sodium benzoate | NaC7H5O2 | salt | 1 |
| potassium sorbate | C6H7KO2 | salt | 1 |
| sodium lactate | C3H5NaO3 | salt | 1 |
| glycine | C2H5NO2 | organic | 1 |
| riboflavin | C17H20N4O6 | organic | 1 |
| trisodium citrate | Na3C6H5O7 | salt | 2 |
| EDTA | C10H16N2O8 | organic | 2 |
| disodium EDTA | Na2C10H14N2O8 | salt | 2 |
| sodium dodecyl sulfate | C12H25NaO4S | salt | 2 |
| sodium dodecylbenzenesulfonate | C18H29NaO3S | salt | 2 |
| theophylline | C7H8N4O2 | organic | 2 |
| eugenol | C10H12O2 | organic | 2 |
| thymol (C10H14O isomer class) | C10H14O | organic | 2 |
| cinnamaldehyde | C9H8O | organic | 2 |
| capsaicin | C18H27NO3 | organic | 7 |
| acetic anhydride | C4H6O3 | organic | 5 |
| morphine (C17H19NO3 class) | C17H19NO3 | fence | 2 |
| leucoindigo | C16H12N2O2 | organic | 5 |
| methyl red | C15H15N3O2 | organic | 1 |
| indigo carmine | C16H10N2O8S2 | organic | 10 |
| cyclohexane | C6H12 | solvent | 2 |
| pentanol (amyl alcohol class) | C5H12O | solvent | 1 |
| ethyl acetate (C4H8O2 class) | C4H8O2 | solvent | 14 |
| vinyl acetate | C4H6O2 | organic | 18 |
| ethyl cyanoacrylate | C6H7NO2 | polymer | 19 |
| acrolein | C3H4O | fence | 2 |
| trilaurin | C39H74O6 | organic | 1 |
| tripalmitin | C51H98O6 | organic | 4 |
| methyl salicylate (C8H8O3 class) | C8H8O3 | organic | 5 |
| salicin | C13H18O7 | organic | 11 |
| gallic acid | C7H6O5 | organic | 5 |
| pentose sugars (C5H10O5 class) | C5H10O5 | organic | 4 |
| quinine | C20H24N2O2 | organic | 3 |
| naphthoquinone | C10H6O3 | organic | 1 |
| sodium salicylate | NaC7H5O3 | salt | 2 |
| octane | C8H18 | solvent | 4 |
| potassium sulfate | K2SO4 | salt | 8 |
| potassium metabisulfite | K2S2O5 | salt | 2 |
| sodium pyrosulfate | Na2S2O7 | salt | 2 |
| cyanuric acid | C3H3N3O3 | organic | 6 |
| sodium tetrathionate | Na2S4O6 | salt | 9 |
| potassium peroxymonosulfate | KHSO5 | oxidizer | 3 |
| sodium iodate | NaIO3 | salt | 1 |
| manganese(II) chloride | MnCl2 | salt | 2 |
| potassium triiodide | KI3 | salt | 2 |
| sodium bromate | NaBrO3 | oxidizer | 4 |
| zinc carbonate | ZnCO3 | mineral | 1 |
| aluminum sulfide | Al2S3 | salt | 10 |
| tin(II) sulfate | SnSO4 | salt | 2 |
| tin(IV) chloride | SnCl4 | salt | 3 |
| silver sulfide | Ag2S | mineral | 5 |
| tin(II) fluoride | SnF2 | salt | 1 |
| ammonium bicarbonate | NH4HCO3 | salt | 4 |
| ammonium carbamate | NH2COONH4 | salt | 2 |
| potassium tetraiodomercurate | K2HgI4 | fence | 1 |
| phosphorus pentoxide | P2O5 | mineral | 1 |
| hexane | C6H14 | solvent | 2 |
| sodium dithionite | Na2S2O4 | salt | 4 |
| disodium phosphate | Na2HPO4 | salt | 2 |
| potassium phosphate | K2HPO4 | salt | 2 |
| iodic acid | HIO3 | acid-in | 1 |
| chloric acid | HClO3 | acid-in | 1 |
| uranium dioxide | UO2 | mineral | 1 |
| thorium dioxide | ThO2 | mineral | 1 |
| americium dioxide | AmO2 | mineral | 1 |
| lead silicate | PbSiO3 | fence | 4 |
| cortisol | C21H30O5 | organic | 1 |
| diethylene glycol | C4H10O3 | solvent | 1 |
| ketene | C2H2O | organic | 3 |
| acetyl chloride | C2H3ClO | organic | 2 |
| lysine | C6H14N2O2 | organic | 2 |
| hydroxylamine | NH2OH | base | 1 |
| aniline | C6H7N | organic | 3 |
| benzenediazonium chloride | C6H5N2Cl | organic | 3 |
| p-phenylenediamine | C6H8N2 | organic | 2 |
| isatin | C8H5NO2 | organic | 1 |
| pyridine | C5H5N | solvent | 1 |
| naphthol | C10H8O | organic | 2 |
| hydrazine sulfate | N2H6SO4 | fence | 4 |
| sodium gluconate | C6H11NaO7 | salt | 2 |
| tungsten trioxide | WO3 | mineral | 1 |
| nickel(II) chloride | NiCl2 | salt | 4 |
| gold(III) chloride | AuCl3 | salt | 4 |
| calomel | Hg2Cl2 | fence | 2 |
| potassium oxide | K2O | mineral | 34 |
| sodium oxide | Na2O | mineral | 22 |
| potassium bicarbonate | KHCO3 | salt | 4 |
| barium chloride | BaCl2 | fence | 2 |
| lead carbonate | PbCO3 | fence | 1 |
| aluminum fluoride | AlF3 | salt | 4 |
| lithium nitrate | LiNO3 | oxidizer | 2 |
| lithium sulfate | Li2SO4 | salt | 2 |
| lithium aluminate | LiAlO2 | mineral | 2 |
| potassium superoxide | KO2 | oxidizer | 2 |
| sodium borohydride | NaBH4 | salt | 2 |
| ethylenediamine | C2H8N2 | base | 4 |
| chloroprene | C4H5Cl | organic | 2 |
| dodecane | C12H26 | solvent | 6 |
| adipic acid | C6H10O4 | organic | 2 |
| cyclopentanone | C5H8O | solvent | 3 |
| cyclopentanone ethylene ketal | C7H12O2 | organic | 3 |
| tribromoketal (Ch 50 route) | C7H9Br3O2 | organic | 3 |
| bromocyclopentadienone ketal (Ch 50 route) | C7H7BrO2 | organic | 1 |
| dimer diketal (Ch 50 route) | C14H14Br2O4 | organic | 3 |
| dibromo diketone (Ch 50 route) | C10H6Br2O2 | organic | 5 |
| dimethyl cubane-1,4-dicarboxylate | C12H12O4 | organic | 2 |
| benzophenone | C13H10O | organic | 1 |
| acetonitrile | C2H3N | solvent | 1 |
| disodium cubane-1,4-dicarboxylate | Na2C10H6O4 | salt | 2 |
| N-acetylglucosamine | C8H15NO6 | organic | below cut |
| usnic acid | C18H16O7 | organic | below cut |
| orcein | C28H24N2O7 | organic | below cut |
| glucosamine | C6H13NO5 | organic | below cut |
| zircon (zirconium silicate) | ZrSiO4 | mineral | below cut |
| orthoclase feldspar | KAlSi3O8 | mineral | below cut |
| nepheline | NaAlSiO4 | mineral | below cut |
| spodumene | LiAlSi2O6 | mineral | below cut |
| caffeine hydrochloride | C8H11N4O2Cl | organic | 2 |
| allicin | C6H10OS2 | organic | 2 |
| diallyl disulfide | C6H10S2 | organic | 2 |
| allylsulfenic acid | C3H6OS | organic | 2 |
| allyl isothiocyanate | C3H5NS | organic | 2 |

### E.8 Standing notes

- The mention-only class stands (empty).
- The isomer classes are carried as cross-attribution notes on their rows, per the register's isomer convention: lactose/trehalose ↔ sucrose; vanillin ↔ methyl salicylate; orcinol ↔ salicyl alcohol; limonene ↔ α-pinene; morphine ↔ piperine; the PVA repeat ↔ acetaldehyde; the cubane diacid ↔ PET's repeat unit.
- Composition is not destiny (Ch 34's own lesson): the morphine/piperine row carries both names because the corpus prints both for the same formula.
- This section was composed and pushed from the repository directly; the local mirror sync was not possible this session (a sandbox symlink defect, disclosed) — the repository is the source of record.
