# Engine 87 — E87-DL — transcripts (session 202, Vol IX Ch 55 review)

Outputs Verbatim, spliced from the frozen scratch files, never retyped: tP.txt
(308 B, md5 538917a273a354421ff0644950c664a2), tAB.txt (1,364 B, md5
1c691a40deb24c27cf1974dc689c16db), tCD.txt (1,484 B, md5
00a624db60b6b6b08a8c24f306c03f2a), tEF.txt (2,115 B, md5
903615fc3dec080d527e14bdbdefdb67), tJ.txt (1,165 B, md5
6aa7b10bd6323591d886fffadd0eeba9). The disclosure headers between blocks are
authoring annotations; the R87- lines are the verbatim engine output — the E84
balance book's standing practice. One census disclosure, standing: the tAB census
lines below are the engine's own miscounted output (the count filter could not see
the verdict token's trailing parenthetical) — the census-defect class disclosed in
ch55-engine87.md; the authoritative counts, bash-counted from the frozen rows:
Book A 10 rows, 10 PASS, 0 SUSTAINED; Book B 5 rows, 3 PASS, 2 SUSTAINED.

## The probe (tP.txt, rev-1, first run)

R87-P: P1 | lane1 C->K 77.36 K | lane2 K-entry -195.79 C, K->F -320.422 F | printed 77.36 K / -320.42 F | PASS
R87-P: P2 | lane1 C->F -320.42 F | printed -320.42 | PASS
R87-P: P3 | laneAgreement fL1=-3204220 fL2=-3204220 | PASS
R87-P: P4 | bracket [693,705] contains 696 | PASS
R87-P: P0 PROBE rows=4 PASS=4

## Books A+B (tAB.txt, rev-2 — rev-1's A1 dual-lane comparison bug, the s=0 format
## bug, and Book B's 10x scale slip fixed in-session, disclosed above)

R87-A: A1 | lane1 77.36 | lane2 -195.79 C | printed 77.36 | PASS
R87-A: A2 | lane1 -320.42 | lane2 -320.42 | printed -320.42 | PASS
R87-A: A3 | lane1 -112.00 | lane2 -112.00 | printed -112.00 | PASS
R87-A: A4 | lane1 -109.30 | lane2 -109.30 | printed -109.30 | PASS
R87-A: A5 | lane1 -138.82 | lane2 -138.82 | printed -138.82 | PASS
R87-A: A6 | lane1 379.4 F | lane2 reverse 193.00 C | printed 379.4 | PASS
R87-A: A7 | lane1 prints-delta 211.12 F | lane2 dC*1.8 211.12 F (dC 117.29) | printed 211.12 = 117.29 x 1.8 | PASS
R87-A: A8 | bracket [77.2, 77.5] contains 77.36 | PASS
R87-A: A9a | freezer-cryogen gap 177.79 -> 178 printed 178 | PASS
R87-A: A9b | freezer-kettle gap 118 printed 118 | PASS
R87-B: B1 | lane1 mol/L 28.81 | lane2 remainder q=2880 r=214080 -> 28.81 | printed 28.81 | PASS
R87-B: B2 | lane1 full-precision 692.82 L | lane2 displayed-intermediate 692.88 L | printed 692.93 | OBJECTION SUSTAINED (witnesses q=69282 r=106212)
R87-B: B3 | lane1 full-precision 704.63 L | lane2 displayed-intermediate 704.69 L | printed 704.75 | OBJECTION SUSTAINED (witnesses q=70463 r=137958)
R87-B: B4 | corrected band [692.82, 704.63] contains the table 696 | PASS (the headline survives)
R87-B: B5 | the ~693 shorthand: 692.82 rounds to 693 | PASS
R87-A: census: rows 10 | PASS 10 | OBJECTION SUSTAINED 0
R87-B: census: rows 5 | PASS 2 | OBJECTION SUSTAINED 0

## Books C+D (tCD.txt, rev-1) — the displacement chain and the heat chain

R87-C: C1 | lane1 X=692.93 -> 16.76% | lane2 X=693 -> 16.76% | printed 17.4 | OBJECTION SUSTAINED
R87-C: C2 | additive model: lane1 X=692.93 -> 17.45% | lane2 X=693 -> 17.45% | printed 17.4 follows ONLY this model | OBJECTION SUSTAINED
R87-C: C3 | the corrected closet 16.76% < 19.5% threshold (and Model B's 17.45% also < 19.5) | PASS
R87-C: C4 | lane1 X=692.93 -> 10344.5 L | lane2 X=693 -> 10345.5 L | printed 9,651.6 L | OBJECTION SUSTAINED
R87-C: C5 | additive-model threshold: 19.5 x 692.93/1.4 -> 9651.5 L | printed 9,651.6 L (0.1 off even here) | OBJECTION SUSTAINED
R87-C: C6 | machine: 20.9 x 693 -> 14483.7 | printed 14,533.7 | OBJECTION SUSTAINED
R87-C: C7 | machine: 14,533.7/1.4 -> 10381.2 | printed 9,651.6 | OBJECTION SUSTAINED
R87-C: C8 | all models: threshold rooms in [9651.5, 10345.5] L, closet O2 all < 19.5% | the safety conclusion robust | PASS
R87-D: D1 | lane1 2.09x196 -> 409.64 J/g | lane2 2.09x(200-4) -> 409.64 J/g | printed 409.64 | PASS
R87-D: D2 | lane1 409.64+334 -> 743.64 J/g | lane2 swap 334+409.64 -> 743.64 J/g | printed 743.64 | PASS
R87-D: D3 | lane1 743.64/334 -> 2.23 | lane2 409.64/334 + 1 -> 2.23 | printed 2.23 (~2.2x, 'twice as long') | PASS
R87-D: D4 | lane1 2.1x196 -> 411.6 J/g | lane2 (411.6+334)/334 -> 2.23 | printed 411.6, ratio 2.23 | PASS
R87-D: D5 | warming 409.64 J/g > melting 334 J/g — the lecture's point | PASS
R87-C: census: rows 8 | PASS 2 | OBJECTION SUSTAINED 6
R87-D: census: rows 5 | PASS 5 | OBJECTION SUSTAINED 0

## Books E+F (tEF.txt, rev-2 — rev-1's E8 percent-scale slip fixed, disclosed) —
## the economics ledger and the calendar

R87-E: E1 | lane1 5600+1100+10000 -> 16700 | lane2 5600+(1100+10000) -> 16700 | printed 16700 ("nearly $17,000" EXACT) | PASS | the build cost
R87-E: E2 | lane1 24000-16700 -> 7300 | lane2 24000-5600-1100-10000 -> 7300 | printed 7300 ("over $7,000 less" EXACT) | PASS | the Alibaba wall
R87-E: E3 | lane1 -> 7.2396 | lane2 witness q=72396 r=150000 (q*d+r==n: true) | printed 7.2396 | PASS | N384 vs 1.6M crawl, the ratio class' biggest member
R87-E: E4 | lane1 -> 1.009 | lane2 witness q=1008 r=3791000 (q*d+r==n: true) | printed 1.009 | PASS | N298 vs 6.5M crawl
R87-E: E5 | lane1 -> 0.98 | lane2 witness q=98 r=482400 (q*d+r==n: true) | printed 0.98 | PASS | N295 vs 2M crawl
R87-E: E6 | lane1 -> 0.99 | lane2 witness q=99 r=1162700 (q*d+r==n: true) | printed 0.99 | PASS | N297 vs 3.7M crawl
R87-E: E7 | lane1 -> 0.996 | lane2 witness q=995 r=1953000 (q*d+r==n: true) | printed 0.996 | PASS | N294 vs 3.2M crawl
R87-E: E8 | lane1 -> 2.972 | lane2 witness q=2971 r=10564391 (q*d+r==n: true) | printed 2.972 | PASS | N403 live like-ratio, percent (x100 scale; rev-1 spec slip fixed)
R87-F: F1 | lane1 closed-form = 181 | lane2 day-walk = 181 | printed 181 | PASS | the series opener N295 -> N298
R87-F: F2 | lane1 closed-form = 217 | lane2 day-walk = 217 | printed 217 | PASS | N298 -> N290 (the 216-corrected span)
R87-F: F3 | lane1 closed-form = 157 | lane2 day-walk = 157 | printed 157 | PASS | N290 -> N297
R87-F: F4 | lane1 closed-form = 289 | lane2 day-walk = 289 | printed 289 | PASS | N296 -> N297
R87-F: F5 | lane1 closed-form = 374 | lane2 day-walk = 374 | printed 374 | PASS | the Leidenfrost redo pair N298 -> N297
R87-F: F6 | lane1 closed-form = 555 | lane2 day-walk = 555 | printed 555 | PASS | the 555-day LN2 series N295 -> N297
R87-F: F7 | lane1 closed-form = 2563 | lane2 day-walk = 2563 | printed 2563 | PASS | the cross-channel bidirectional pair N290 -> N294
R87-F: F8 | lane1 closed-form = 366 | lane2 day-walk = 366 | printed 366 | PASS | N384's age at gather (the youngest paper)
R87-E: census: rows 8 | PASS 8 | OBJECTION SUSTAINED 0
R87-F: census: rows 8 | PASS 8 | OBJECTION SUSTAINED 0

## The injections and the determinism receipt (tJ.txt)

R87-J: J1 | served "1 L -> 696.0 L at exactly 20 C" | machine: 807/28.0134 x 24.05 -> 692.82 L | REFUSED | the dewar table's 1:696 is a nominal, not a 20 C derivation — the engine refuses the false provenance
R87-J: J2 | served "17.4% from the chapter's own formula" | machine: 20.9 x (3500-692.93)/3500 -> 16.76% | REFUSED | Model A prints 16.76, not 17.4 — the false bridge refused
R87-J: J3 | served "N298 -> N290 = 216 days" | machine: closed-form = 217 | REFUSED | the corrected-of-record 217 stands (both lanes); the pre-correction 216 refused
R87-J: J4 | served "2.09 x 196 = 419.64 J/g" | machine: 2.09 x 196 -> 409.64 J/g | REFUSED | the real product is 409.64; the injected slip refused
R87-J: census: injections 4 | REFUSED 4 | ACCEPTED 0
R87-D: determinism | Book E replay vs frozen tEF.txt | replay lines 9 | frozen lines 9 | byte-identical true | the first replay attempt printed not-identical: its own lane1 token read undefined (a transcription slip in the replay harness — the object-returning halfUp's .out carried into a string-returning copy); the determinism gate did its job, the slip disclosed here, the corrected replay byte-identical
