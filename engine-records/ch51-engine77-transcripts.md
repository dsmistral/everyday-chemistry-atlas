# Engine 77 — the transcripts (session 190, Ch 51 part 1 of 2)

*The three receipts frozen into `manuscript/vol8/ch51.md`'s Lab 51.1 verbatim. Digest lane: sdbm over the transcript text without the trailing newline (the Engine-66 convention, inherited); md5 over the receipt files as stored. All three pieces are receipt re-executions at part-1 close on the identical corrected kernel — the disclosure is printed in the transcript headers themselves and in the record's §3.*

## Piece A — the kernel probe (engine77-a.txt, 1,085 B, md5 071397613bf4153d993e597f7df2c077, sdbm f0ad2d2c)

```
ENGINE 77 PIECE A — REV-2: THE KERNEL PROBE (receipt re-executed at part-1 close: the in-session rev-2 transcripts for Pieces A and B were not persisted; this fresh run uses the same corrected kernel [K1 fixed: back-substitution sums over j != pc, the pivot column, not over j != free] and reproduces the in-session results; two independent passes, byte-identical)
  K1R-1 synthetic [[1,0,0],[0,0,1]]: kernel (0,1,0) — expected (0,1,0): PASS
  K1R-2 synthetic [[2,4,0],[0,0,3]]: kernel (-2,1,0) — expected (-2,1,0): PASS
  P1 H2 + O2 -> H2O: engine 2:1:2 — expected 2:1:2: PASS
  P2 N2 + H2 -> NH3: engine 1:3:2 — expected 1:3:2: PASS
  P3 NaCl + H2O -> NaOH + H2 + Cl2: engine 2:2:2:1:1 — expected 2:2:2:1:1: PASS
  INJ-A1 wrong-basis claim H2:O2:H2O = 1:1:1: residual NONZERO on 1 element rows -> CAUGHT; engine prints 2:1:2
  INJ-A2 digit-slip claim N2:H2:NH3 = 1:3:3: residual NONZERO on 2 element rows -> CAUGHT; engine prints 1:3:2
  INJ-A3 unbalanceable set (H2O2 posed for the water): NO NONZERO KERNEL — formula set unbalanceable -> CAUGHT
PIECE A VERDICT: PASS
```

## Piece B — Sheet 1, the chain's seven balances (engine77-b.txt, 919 B, md5 70005602c81e1710dc22b62459a749e6, sdbm 56672e17)

```
ENGINE 77 PIECE B — REV-2: SHEET 1, THE MOLAR BOOK BALANCES (receipt re-executed at part-1 close per the Piece A disclosure; the seven chain balances + injections; exact integer-pair rationals, iterative Gauss-Jordan, no BigInt, no recursion)
  B1 decarboxylation (Organikum make-lead): engine 1:1:1:1 — stated 1:1:1:1: PASS
  B2 nitration: engine 1:1:1:1 — stated 1:1:1:1: PASS
  B3 tin dissolution: engine 1:2:1:1 — stated 1:2:1:1: PASS
  B4 SnCl2-mediated reduction: engine 1:3:6:1:3:2 — stated 1:3:6:1:3:2: PASS
  B5 Sn-metal reduction: engine 2:3:12:2:3:4 — stated 2:3:12:2:3:4: PASS
  B6 diazotization: engine 1:1:2:1:1:2 — stated 1:1:2:1:1:2: PASS
  B7 azo coupling (para red): engine 1:1:1:1:1:1 — stated 1:1:1:1:1:1: PASS
  INJ-B1 mis-stated nitration 1:1:1:2 -> CAUGHT; engine prints 1:1:1:1
  INJ-B2 digit-slip reduction 1:3:7:1:3:2 -> CAUGHT; engine prints 1:3:6:1:3:2
PIECE B VERDICT: PASS
```

## Piece C — Sheet 2, the charge/yield ledger (engine77-c.txt, 2,407 B, md5 55435710319fbb21ee16ba77fb0fd606, sdbm 528ebd92)

```
ENGINE 77 PIECE C — SHEET 2: THE CHARGE/YIELD LEDGER (rev-2: harness fix H1 the percent rows scaled x100 [rev-1 printed ratios]; kernel fix H2 the S element restored to the table [the H2SO4 mass row crashed the rev-2 first attempt]; two independent passes, transcripts BYTE-IDENTICAL (determinism PASS))
MOLAR MASSES (fresh transcription of the held element table; 2 dp round-half-up):
  sodium benzoate C6H5COONa = 144.11
  NaOH = 40.00
  Na2CO3 = 105.99
  benzene C6H6 = 78.11
  HNO3 = 63.01
  H2SO4 = 98.07
  nitrobenzene C6H5NO2 = 123.11
  H2O = 18.02
  SnCl2 = 189.61
  SnCl4 = 260.51
  aniline C6H5NH2 = 93.13
  HCl = 36.46
  NaCl = 58.44
  NaNO2 = 69.00
  2-naphthol C10H8O = 144.17
  p-nitroaniline C6H6N2O2 = 138.13
  p-nitrobenzenediazonium chloride C6H4N3O2Cl = 185.57
  para red C16H11N3O3 = 293.28
CHARGE/YIELD LEDGER:
  L1 100 g sodium benzoate = 0.6939 mol (register 0.6939)
  L2 NaOH 60 g = 2.16 eq vs benzoate (the Organikum experimental excess)
  L3 benzene theoretical 54.21 g = 61.84 mL at 0.8765; stated 43 mL -> yield 69.53% (stated ~70)
  L4 benzene charge 30 mL = 26.30 g = 0.3366 mol (limiting)
  L5 HNO3 35 mL at 1.51 = 0.8387 mol = 2.49 eq
  L6 H2SO4 40 mL at 1.84 = 0.7505 mol = 2.23 eq
  L7 nitrobenzene theoretical 41.44 g = 34.56 mL at 1.199; stated 20 mL -> yield 57.86% (stated ~57)
  L8 nitrobenzene 15 mL = 0.1461 mol
  L9 aniline theoretical 13.60 g = 13.32 mL at 1.0217; stated 10 mL -> yield 75.10% (stated ~78; the density/measurement rounding spread disclosed)
  L10 tin 34 g = 0.2864 mol = 1.96 eq vs nitrobenzene
  L11 tin ledger: Sn(II) reading 3x = 52.03 g; Sn(IV) reading 1.5x = 26.01 g; used 34 g (between, near the Sn(IV) reading + mediator excess)
  L12 HCl 85 mL of 31.45% (d 1.155) = 30.88 g HCl = 0.8469 mol = 5.80 eq
  L13 salt rule: 200 mL x 20 g/100 mL = 40 g (the stated 40 g, rule applied exact)
  L14 p-nitroaniline 5 g = 0.0362 mol; para red theoretical 10.62 g (diazonium limiting)
  L15 bp identity set: benzene fraction 79-80 C vs lit 80.1 (delta 0.6-1.1); nitrobenzene ~208 vs lit 210.9 (delta ~2.9); aniline 180-184 vs lit 184.1 (delta 0.1-4.1) — all wet-product consistent
  INJ1 wrong-base yield claim (43/54.21 g = 79.3%): engine prints 79.3% — the claim reproduces its own wrong base -> CAUGHT (correct base the 61.84 mL volume)
  INJ2 digit-slip theoretical (nitrobenzene 41.34 g): CAUGHT (engine prints 41.44)
PIECE C VERDICT: PASS
```

*Battery digest (A+B+C concatenated, newline-separated, no trailing newlines): sdbm d3f6e3e7.*
