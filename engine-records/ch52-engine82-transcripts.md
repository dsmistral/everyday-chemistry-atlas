# Engine 82 — Chapter 52, the Phase-3 Adversarial Review — Transcripts (Outputs Verbatim)

Session 196 (2026-11-05). **E82-RD, the rational-display engine** — fresh, zero code shared with Engines 1–81. The review battery for the two-experts protocol (prover vs. skeptic): every quantity in the chapter carried as an exact rational lane [n, d] of integers, each printed decimal audited against round-half-up of the exact lane at the printed precision, a separate truncation detector (a print equal to the floor of the exact lane at that precision flagged TRUNC), the element table independently re-transcribed; no recursion, no BigInt, no floats in the value path. Six pieces, each frozen to scratch with md5 receipts before this splice, never retyped: the probe 549 B (md5 c205424e8e70dab28cea991869c848c2); Sheet A 1,939 B (88ff538b57a30e664ad0d39937954f78); Sheet B 1,409 B (682754e8ac5fccd958c4159910346cb1); Sheet C 1,395 B (d58f3c0dcb08fe8e25f88010067dc33c); Sheet D 1,706 B (4487565257c39c521030e71b8fb881f8); Sheet D2 831 B (7ab6eb2cdaac7202238a25fc10a95ff7) — 7,829 B of transcript total. The honest history is disclosed in the headers of Sheets B, C, D, and D2 themselves; the design and the verdict live in ch52-engine82.md; the source record — an honest reconstruction, the as-run literal lost to the session-196 context compaction — lives in ch52-engine82-src.md.

**The probe (7 rows, 3 injections CAUGHT):**

```
=== E82-RD PROBE (pre-flight, 7 rows, 3 injections) ===
P1 rhu(1/8,2dp)=13 PASS got 13
P2 rhu(1/3,4dp)=3333 PASS got 3333
P3 rhu(2/3,4dp)=6667 PASS got 6667
P4 trc(2/3,4dp)=6666 PASS got 6666
P5 dc("1.804",325000/180159)=PASS PASS PASS
P6 dc("9.28",6500/700)=TRUNC PASS TRUNC (round is 929)
P7 dc("9.29",6500/700)=PASS PASS PASS
I1 wrong display 1.8035 vs 325000/180159 -> FAIL
I2 wrong display 0.2739 vs 210*180159*100/13816481000 -> FAIL
I3 transposed 125.52 vs 33*14360675000/21000/180159 -> FAIL
PROBE VERDICT: 7/7 rows, injections caught: true
```

**Sheet A — the molar book (32/32 MATCH, both parts' every mass recomputed exact; the salt identity re-proved):**

```
=== E82-RD SHEET A: THE MOLAR BOOK (32 rows, exact integer lanes) ===
A aspirin computed=180159 master=180159 -> MATCH
A salicylic acid computed=138122 master=138122 -> MATCH
A salicin computed=286280 master=286280 -> MATCH
A salicyl alcohol computed=124139 master=124139 -> MATCH
A acetic anhydride computed=102089 master=102089 -> MATCH
A acetic acid computed=60052 master=60052 -> MATCH
A phenol computed=94113 master=94113 -> MATCH
A p-nitrophenol computed=139110 master=139110 -> MATCH
A p-aminophenol computed=109128 master=109128 -> MATCH
A acetaminophen computed=151165 master=151165 -> MATCH
A acetanilide computed=135166 master=135166 -> MATCH
A phenacetin computed=179219 master=179219 -> MATCH
A pyrimethamine computed=248714 master=248714 -> MATCH
A bismuth subsalicylate computed=362093 master=362093 -> MATCH
A BiOCl computed=260429 master=260429 -> MATCH
A chlorobutanol computed=177449 master=177449 -> MATCH
A phenytoin computed=252273 master=252273 -> MATCH
A aniline computed=93129 master=93129 -> MATCH
A glucose computed=180156 master=180156 -> MATCH
A lidocaine computed=234343 master=234343 -> MATCH
A lidocaine HCl computed=270801 master=270801 -> MATCH
A MEGX computed=206289 master=206289 -> MATCH
A xylidine computed=121183 master=121183 -> MATCH
A chloroacetyl chloride computed=112937 master=112937 -> MATCH
A chloroacetamide computed=197662 master=197662 -> MATCH
A diethylamine computed=73139 master=73139 -> MATCH
A benzocaine computed=165192 master=165192 -> MATCH
A procaine computed=236315 master=236315 -> MATCH
A PABA computed=137138 master=137138 -> MATCH
A DEAE computed=117192 master=117192 -> MATCH
A cocaine computed=303358 master=303358 -> MATCH
A diethylamine HCl computed=109597 master=109597 -> MATCH
A.x salt identity lidocaine+HCl=270801 -> MATCH
A.INJ transposed MEGX lane 206298 vs computed 206289 -> CAUGHT
SHEET A VERDICT: 32/32 MATCH, salt identity ok, injections caught 1, failRows=0
```

**Sheet B — the dose/economics display audit (run-1: 20 PASS / 1 TRUNC / 7 FAIL plus 3 fixed-lane rows; five of the FAILs harness-side lane slips fixed in Sheet D; the TRUNC and two FAILs the real findings RA-2, RA-1, RA-3):**

```
=== E82-RD SHEET B: THE DOSE/ECONOMICS DISPLAY AUDIT (round-half-up vs print) ===
B.1 325mg aspirin mmol (master "1.804") -> PASS
B.2 S2.1 mmol 4dp ("1.8040") -> PASS
B.3 500mg acetaminophen ("3.308") -> PASS
B.4 S2.2 4dp ("3.3076") -> PASS
B.5 3g window mmol ("19.85") -> PASS
B.6 4g window mmol ("26.46") -> PASS
B.7 tracked theoretical g ("76.690") -> PASS
B.8 tracked efficiency % ("0.2738") -> PASS
B.9 spoken theoretical g ("79.711") -> PASS
B.10 spoken efficiency % ("0.2635") -> PASS
B.11 headline miss ("126.9") -> PASS
B.12 exact-basis miss (master "125.25") -> FAIL
B.13 exact-basis miss rounded ("125.26") -> PASS
B.14 last-step theoretical ("1.167") -> PASS
B.15 S3.1 mmol 2dp ("507.33") -> FAIL
B.16 Bi pct ("57.7") -> FAIL
B.17 Bi in label charge g ("18.145") -> PASS
B.18 S2.10 witness remainder -> PASS
B.19 22% theoretical ("22.727") -> FAIL
B.20 label-Bi basis ("27.6") -> FAIL
B.21 salt conversion mg ("7511.24") -> PASS
B.22 tube-equivalents ("5.42") -> PASS
B.23 patch loads (master "9.28") -> TRUNC
B.24 patch loads rounded ("9.29") -> PASS
B.25 price spike pct (master "5500") -> FAIL
B.26 price spike exact 1dp ("5455.6") -> FAIL
B.27 $/g demo ("12222.22") -> PASS
B.28 S2.14 mmol ("2.3530") -> PASS
B.2-fix mmol 4dp lane -> PASS
B.28-fix salicylic mmol 4dp -> PASS
B.17-fix S2.10 witness 18145*362093+153715=HOLDS
SHEET B VERDICT: 20 PASS / 1 TRUNC / 7 FAIL (plus 3 fixed-lane rows)
```

**Sheet C — the balance book (run-1: 15/16 PASS + 1 injection CAUGHT; the FAIL row and one wrong-lane PASS harness-side, fixed in Sheet D):**

```
=== E82-RD SHEET C: THE BALANCE BOOK (16 balances, counts + mass both) ===
C.1 salicin hydrolysis (E80 B1) Lmass=304295 Rmass=304295 counts=BAL -> PASS
C.2 ASA acetylation (E80 B2) Lmass=240211 Rmass=240211 counts=BAL -> PASS
C.3 ASA hydrolysis (E80 B3) Lmass=198174 Rmass=198174 counts=BAL -> PASS
C.4 decarboxylation (E80 B4) Lmass=138122 Rmass=138122 counts=BAL -> PASS
C.5 mono-nitration (E80 B5) Lmass=157125 Rmass=157125 counts=BAL -> PASS
C.6 reduction (E80 B6) Lmass=145158 Rmass=143142 counts=OFF -> FAIL
C.7 p-aminophenol acetylation (E80 B7) Lmass=211217 Rmass=211217 counts=BAL -> PASS
C.8 acetanilide formation (E80 B8) Lmass=153181 Rmass=153181 counts=BAL -> PASS
C.9 subsalicylate in acid (E80 B9) Lmass=471467 Rmass=471467 counts=BAL -> PASS
C.10 BiOCl white flash (E80 B10) Lmass=349344 Rmass=349344 counts=BAL -> PASS
C.11 procaine hydrolysis (E81 B1) Lmass=254330 Rmass=254330 counts=BAL -> PASS
C.12 lidocaine->MEGX formal (E81 B2) Lmass=234343 Rmass=234343 counts=BAL -> PASS
C.13 the salt (E81 B3) Lmass=270801 Rmass=270801 counts=BAL -> PASS
C.14 benzocaine hydrolysis (E81 B4) Lmass=183207 Rmass=183207 counts=BAL -> PASS
C.15 arrow one (E81 B5) Lmass=234120 Rmass=234120 counts=BAL -> PASS
C.16 arrow two (E81 B6) Lmass=343940 Rmass=343940 counts=BAL -> PASS
C.INJ procaine hydrolysis without water -> CAUGHT
SHEET C VERDICT: 15/16 PASS, injections caught 1, failRows=1
```

**Sheet D (rev-2) — the fixed harness lanes, the suspect lanes at full witness precision, determinism 13/13 MATCH, 2 injections CAUGHT:**

```
=== E82-RD SHEET D (rev-2): the fixed harness lanes + the suspect lanes at full precision + determinism ===
rev-2 disclosure: run-1 (Sheet B) carried five HARNESS-SIDE lane slips (B.15 n off 10x; B.16/B.20 missing the x100 percent factor; B.19 n off 10x; B.26 n off 10x) and Sheet C carried two (C.6 the reduction encoded with H2O2 instead of 2 H2O; C.10 built on the wrong coincidence-balanced equation instead of the standard BiCl3 + H2O -> BiOCl + 2 HCl). The engine value path (rhu/trc/mass lanes) was proven by the probe and the 20 clean Sheet-B rows; no engine value moved.
D.1 (fix B.15) mmol 91.4g aspirin "507.33" -> PASS
D.2 (fix B.16) Bi percent "57.7" -> PASS
D.3 (fix B.19) 22pct theoretical "22.727" -> FAIL
D.4 (fix B.20) label-Bi basis "27.6" -> PASS
D.5 (fix B.26) spike exact "5455.6" -> PASS
D.6 (fix C.6) reduction C6H5NO3+3H2 -> C6H7NO+2H2O: L=145158 R=145158 -> PASS
D.7 (fix C.10) BiCl3+H2O -> BiOCl+2HCl: L=333345 R=333345 -> PASS
D.8 F1 the exact-basis miss = 33*t/21000, t=95000*151165/180159: q=125 r=984900000 (witness 125*3783339000+984900000=473902275000 == 473902275000) value=125.26032 -> master "125.25" FAIL / "125.26" PASS
D.9 F1b the spoken-basis efficiency x10^5 % = 21000*t_den/t_num = 2 (S3.7 printed divisor 26,347; the exact lane is 2) -> SHEET LANE WRONG (off by 26345)
D.10 F2 patch loads exact 6500/700 = 9 r200, value 9.28 -> master "9.28" TRUNC / "9.29" PASS (the E81 transcript rev-2 note itself says ~9.29)
D.11 F3 spike exact (750-13.5)/13.5 = 54.55555555555556 percent -> whole-percent round 5456; master "5,500" FAIL
DETERMINISM: 13/13 MATCH (reversed iteration orders)
D.INJ1 wrong miss display "125.24" -> FAIL
D.INJ2 wrong patch display "9.30" -> FAIL
```

**Sheet D2 (rev-3) — the two remaining harness lanes fixed:**

```
=== E82-RD SHEET D2 (rev-3): the two remaining harness lanes fixed ===
D2 disclosure: D.3 was slipped twice in a row harness-side (n=50000/22 then 5000/22 — the true lane is 500/22: 5/0.22 = 5x100/22); D.9 was computed with a 10^4-short factor (the true lane reduces by 1000 first to stay under 2^53). Engine value path unchanged.
D2.1 (fix D.3) the 22pct theoretical lane 500/22 -> master "22.727" PASS
D2.2 (fix D.9) spoken-basis efficiency x10^5 % = 378,333,900,000/14,360,675 = 26345 r1917125 (witness 26345x14360675+1917125=378333900000) value=26345.13 -> S3.7 printed divisor 26,347 WRONG (the exact lane is 26345.13, off by +2 near-units)
D2.3 the S3.7 primary "125.25x" divides by the wrong divisor 26,347; the true divisor 26,345.17 gives 3,300,000/26,345 = 125.26 -> 125.26 (consistent with D.8 witness 125 r984900000)
```

**The receipts, restated.** Every piece above was frozen to scratch before this splice and digest-recorded in the header paragraph; the splice gates the bytes against those receipts. A small-case test is a detector, not a proof: the audit's identities are exact-rational witnesses, checked by round-half-up against exact lanes, never float agreement. The verdict — PASS WITH CORRECTIONS, the three findings RA-1/RA-2/RA-3, zero frozen-figure chemistry moved — is recorded with its witness arithmetic in ch52-engine82.md, and the corrections live in the master's Revision Appendix per the extend-never-rewrite rule.
