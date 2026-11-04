# Engine 64 record — the interval-certified big-decimal engine (session 170, the Ch 44 Phase-3 adversarial review)

## 1. Design spec

Engine 64, the interval-certified big-decimal engine — fresh at session 170, sharing zero code with Engines 1–63, and the engine series' first certified-enclosure engine. Every quantity a closed interval [lo, hi] of positive big-decimals, each bound a decimal significand held as base-10⁷ limbs (four kept, 28 significant digits) with a decimal exponent, and every operation rounding outward — the lower bound truncated, the upper bound pushed one ulp — so the true value is provably inside every printed interval. The transcendental lane: the logarithm an atanh series on z = (f−1)/(f+1) after range reduction into f ∈ [1, 2) by stripping powers of two and ten (j·ln2 and kk·ln10 carried exactly), with ln2 bootstrapped from z = 1/3 and ln5 from ln(1.25) via z = 1/9 plus 2·ln2, so ln10 = ln2 + ln5 closes with no circularity; the exponential range-reduced by 2¹³ with a nine-term series and thirteen interval squarings; powRat = exp((a/b)·ln base) on exact rational exponents. The certification criterion is the enclosure itself: a row passes only when round-half-up(lo) and round-half-up(hi) agree with each other and with the frozen print — every PASS a two-sided proof, not a match. No BigInt, no recursion, no Math.random; a float64 witness lane prints beside every row and never feeds one.

Distinctness from Engines 1–63: the whole prior series is point-value arithmetic with witness comparison — schoolbook digit strings (Engines 1–62: base-10 digit strings, exact rationals {n,d}, fixed-point families; Engine 62 the immediate-2 predecessor) and Engine 63's binary-limb mini-float (m·2^e, one 40-bit limb, float64 witnesses). Engine 64 is the series' first engine that never computes a point: it computes a proven enclosure, and its verdicts are interval certificates. Where Engine 63's rows read "value | witness | PASS", Engine 64's read "lo ≤ value ≤ hi with both bounds rounding to the frozen print | certificate PASS".

## 2. Honest run history

The kernel probe ran before any sheet row, and it caught three kernel defects before a single sheet row ran:

- (K1) the f≥2 range-reduction guard compared limbs without exponent alignment — the stripping loop could miss a power of two; found by inspection at rev-1, fixed pre-run;
- (K2) the positive-series term was divided in place (a divisor-carry slip: the term was divided where the quotient should have been accumulated) — every series after its first term collapsed; caught by the probe's own P2/P4 rows at rev-1; fixed with a separate power accumulator (`pw`);
- (K3) the exp recurrence divided by fact(n) instead of n — a defect whose biased e (2.7182818251) happened to PASS P3 by luck at the printed precision and was caught only by P4's 10^0.9 printing 7.94328226 against the frozen 7.94328235 at rev-2; fixed divide-by-n.

Six harness slips after that, each caught by the sheets' own verdicts:

- (H1, H2) probe-smoke authoring slips (rev-1), caught at the probe before anything downstream ran;
- (H3) Sheet 2 rev-1's D10d divisor built as constI("36", −5) instead of 3.6×10⁶ — a unit-scale slip in the harness only (the engine value was right all along); fixed rev-2;
- (H4) Sheet 5 rev-1's parse carried a 'mol basis' typo; fixed;
- (H5, H6) Sheet 5 rev-2's instance-B route slips — an abundance-row scale typo (8×1.947e−9 written as 8×1.947e−8) and the 110/3 route re-written as 220/6 (same value, wrong route) — fixed so the determinism run's independence claim is honest.

The probe's P5 CAUGHT and the 19/19 injection battery are the same discipline worn twice. Zero of the nine defects (K1–K3, H1–H6) touched a frozen chapter figure: all were caught before a verdict was recorded, per the standing gate.

The session's two platform-sync events, disclosed as run history: the first (~13:29) wiped the session buffer once and was recovered byte-exact from the master of record (every affected file re-fetched and md5-verified, nothing lost); the second wiped the buffer a second time, AFTER the battery had run and BEFORE this record was written — Engine 64's source files (the A1 arithmetic piece, the A2 transcendentals piece, the A3 probe) and all seven transcripts (lab64-s0 through s6) are gone from the filesystem. The full consequences are disclosed in §4 and §7; nothing below is reconstructed.

## 3. The gates

- Kernel probe (rev-3): smokes 2/2; P1 D₂O 20.027, P2 ln2 0.69314718, P3 e 2.71828183, P4 10^0.9 7.94328235 — all PASS, each with the interval certified closed at the printed digit; P5 injection (1.1076 vs injected 1.2133) CAUGHT. Probe verdict PASS.
- Sheet 1 (the molar book re-derivation) 13/13.
- Sheet 2 rev-2 (the campaign ledger) 19/19 — including D10's floor: D10a 1,110.2 mol, D10b 214,232,584 C, D10c 59,509 A·h, D10d 297.5 kWh, D10e 354.2 d.
- Sheet 3 17/17 — the Rayleigh E-rows verified two-method (closed form against the 8-stage staged product: 8.6547, 4,690.975, 25.577, 13,862.897, 6,839.904) and the S_eff inversion re-priced (S1 2.63, S2 3.62; round-trips S1b 713.3, S2b 2,140.0).
- Sheet 4: 19/19 engineered injections and corrupted-literal claims CAUGHT.
- Sheet 5 rev-3 (determinism): two engine instances built independently in one run, the 30 canonical values byte-identical between them — PASS. (The planned cross-run grep — every canonical value string re-found in the transcripts on disk — could NOT be run after the second sync wipe; disclosed in §4. The in-run determinism evidence stands.)
- Sheet 6 8/8 — ST1 83.1, ST2 81.3, ST3 1.88, ST4 8.16, MT1 0.382, MT2 0.955, MT3 1.91, T1 435.

## 4. The frozen runblock — LOST, and what stands in its place

Engine 63's record spliced its seven transcripts verbatim; this record cannot. The session's second platform-sync wipe took the buffer directory entire — lab64-s0-probe.txt, lab64-s1..s6.txt, the frozen-transcripts.txt concatenation, and the three source files — and they are gone. Nothing in this section is retyped as verbatim: the verdicts below are recorded as HISTORY from the session's own runs, clearly labeled as such, never as surviving transcript text.

What was hashed before the loss (md5, recorded as history):

- lab64-s2.txt 3fb8c69998aaed860fa3654289af162f
- lab64-s3.txt 0b56e4f8b84d695a5d197201ea18209b
- lab64-s4.txt 4ab125b20dd67467895ab2de099147df
- lab64-s5.txt a61775d3c3e2419ce07362e46b6b95f7
- engine64-a3-probe.ts 1fca08eca1bcbe5690d6368c5937c3a5
- lab64-s0, lab64-s1, lab64-s6, engine64-a1.ts, engine64-a2.ts, frozen-transcripts.txt: never hashed before the wipe — md5s unknown, recorded as unknown.

What survives elsewhere: the frozen prints Engine 64 scored against are intact and re-derivable — engine-records/ch44-engine63.md §4 holds Engine 63's seven transcripts verbatim (they are the master of record for every frozen value), and the manuscript master's Revision Appendix (Ch 44, session 170) carries the battery's verdicts as the correction-of-record document. The Sheet-5 cross-run transcript grep is recorded as NOT-RUN, never as passed.

## 5. Expectations provenance

The expected values beside every row are the frozen prints of the authoring battery — Engine 63's transcripts, verbatim in engine-records/ch44-engine63.md §4 — plus the chapter's own rows as printed in manuscript/vol6/ch44.md. The review scored every row against those frozen prints, never against a re-reading of the drafted prose alone: re-verify, never re-author. The chapter's load-bearing convergent claims were re-confirmed by the session's fresh web battery (thirteen searches plus the Wikipedia heavy-water and VSMOW page-opens): mp 3.82 °C / bp 101.4 °C / ρ 1.1056 / H₂O 0.9982; M 20.0276 (NIST); D/H 155.76 ± 0.05 ppm = 1-in-6,420 (VSMOW, exact); Vemork α 5–7; Girdler 30/130 °C (Spevack 1943); Urey 1931 / Nobel 1934; the toxicity ladder; mild steel ~8 (Armco iron) with α rising on current density. Findings: the max-density spread (11.185→11.2 °C vs 11.6 °C — RF-2, watch-note) and the PEM separation-factor band 3.6–7.47 naming the chapter's 6.3 (RF-3).

## 6. The session-170 checks (all PAID at this close)

- The review census at the STRONGER corpus of 73 files — all 43 chapter masters, the 11 FC masters, and the 19 FC engine records, fetched fresh from the master of record: every hit adjudicated; the zero-hit claim holds for every new literal except one, printed as RF-1 (20.12 — Chapter 6's azeotrope water leg, "19.88 g HCl + 20.12 g water = 49.7% HCl", a named digit coincidence the authoring census missed); the pins re-proved at their owners (18.015 book-wide; 96,485 Ch 12/27; 192,970 Ch 19; 105.99 Ch 14 with its full-precision form 105.988 adjudicated book-wide as the same pin's identity; 120.361; 98.072; 142.036 six-strong; 286.138 Ch 14/33/37); the pure substrings named (81.3, 435, 1.88, 8.16, 3.82, 83.1, 1.91, 0.312, 3.62, 2.63 — each inside a longer number at its owner); the real coincidences held (3.82 Ch 29 radon; 3.62 Ch 1/4 drop datum, the class Ch 40's census names; 354.2 Ch 9 soda-water).
- The got-strings: 15/15 verified verbatim at the survey register (batch-31b/31c; fourteen unique strings, "under ideal circumstances" cited at its two owners) and nowhere else in the corpus.
- [speculative] appears exactly once in the chapter (its single Sources declaration); 0.917 appears nowhere in the chapter (0 hits).
- The render oracle: the frozen web/ch44-web.html (72,776 B, md5 14a9284e03b01d480c18abe1a2463214) reproduced BYTE-IDENTICALLY from the pre-edit drafted master through the session-121-validated renderer with the drafted tail word — renderer faithful, frozen edition stale-free (the session-168 staleness class does not exist here). The reviewed edition then rendered from the reviewed master: 72,840 B, md5 c4219c5b23d7e29f48a8d2bff4c56626, differing from the frozen edition in exactly two lines (the flipped status-line paragraph, the reviewed tail banner) — diff-gated before install.
- The web battery: 13 searches + 2 page-opens, all convergent; findings RF-2 (max-density spread, named — no correction owed) and RF-3 (PEM band 3.6–7.47 named around the chapter's 6.3 — no contradiction); zero corrections owed to any frozen figure.

## 7. The source disclosure (the session-108 and Engine-63 lessons, worn a third way)

The full Engine 64 source is NOT printed here, and no reconstruction is printed as verbatim — this time not because it was never saved, but because it WAS saved, per Engine 63's standing instruction, and then lost anyway: the source (engine64-a1.ts, a2, a3) lived in the session buffer as instructed, and the session's second platform-sync wipe deleted the buffer directory before the close could carry the source to durable storage. The same for the seven transcripts and the frozen-transcripts.txt concatenation. What survives is this record: the design spec (§1), the defect history (§2), the gates and verdicts (§3), the known hashes (§4), and the session checks (§6) — plus the master of record's own Revision Appendix, which carries the same history as the chapter's correction-of-record document. Standing instruction recorded for the next engine: Engine 65 (the Ch 45 authoring engine) must hash AND durably save its source and transcripts to the REPO (a session-buffer save alone has now failed twice); the engine record must be written BEFORE the battery's transcripts leave the session, not at close.

## 8. Session 170 close summary

VERDICT: the Ch 44 Phase-3 adversarial review closes PASS WITH CORRECTIONS (RF-1..RF-3, each printed in the chapter's Revision Appendix as the correction of record). The frozen battery is arithmetically faithful — zero frozen-print mismatches across two independent architectures (Engine 63's binary-limb mini-float; Engine 64's interval-certified big-decimals, every PASS an enclosure proof) — probe rev-3 PASS (P1–P4 certified, P5 CAUGHT), Sheets 1–6 all PASS at final revisions (13/13; 19/19; 17/17 two-method; 19/19 CAUGHT; determinism in-run byte-identical, cross-run grep honestly not-run; 8/8). The census holds at the stronger 73-file corpus with one named exception (RF-1, the 20.12 azeotrope coincidence). The engine's own honest negatives — K1–K3, H1–H6, the two platform-sync wipes, the lost transcripts and source — are printed, never laundered. Engine 64 is retired at this close; Vol VI is complete (44 of 44 chapters reviewed); the next unit per the map is Vol VII Ch 45 authoring on a fresh Engine 65, zero code shared with Engines 1–64.
