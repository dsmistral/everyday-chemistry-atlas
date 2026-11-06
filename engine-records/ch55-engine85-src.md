# Engine 85 — E85-DC — the as-run design source (session 200)

The design source (src.txt, md5 30040449cbd5c5ed1f9a79af454cd59e) was written to disk
BEFORE any run — the Engine 82 source-loss lesson, standing practice since E83. This file
preserves it splice-verbatim. The honest history (the unit ladder's rev-1/rev-2 harness
defects and the expansion book's rev-1 harness defects, all disclosed) lives in
ch55-engine85-transcripts.md; the design below is the design that produced the PASS
rows.

E85-DC — THE DIMENSION-CHAIN ENGINE (Vol IX Ch 55, session 200)
THE SIXTH VERIFICATION PARADIGM: every quantity is a (magnitude, dimension) pair;
every conversion applies an EXPLICIT factor chain (affine conversions carry a
reverse-application witness: the chain must invert); every equation's dimensions
must REDUCE to identity (a tiny string-symbol algebra, numerator/denominator
cancellation, iterative); a claim PASSES iff the printed figure is reproduced
through the chain at its stated precision AND the dimension gate holds. Zero code
shared with Engines 1-84 (E84-IR was interval containment; E85-DC is the chain).
DESIGN (written to disk BEFORE any run):
- dim = {num:[symbols], den:[symbols]}; mult/div concat + cancel identical symbols;
  add/sub require EQUAL dims; reduce-to-1 = both lists empty (ratios, percent).
- affine chain: C->K: +273.15 (witness: K-273.15 = C, |delta| < 1e-9);
  C->F: x*1.8+32 (witness: (F-32)/1.8 = C). DELTAS convert x*1.8 exactly (no offset).
- BOOKS: B1 the unit ladder (LN2 bp -195.79 C -> 77.36 K -> -320.42 F; the touch-pain
  -80 C -> -112 F; dry ice -78.5 C; acetone -94.9 C; Leidenfrost 193 C; the 77 K band);
  B2 the expansion (0.807 g/mL -> 807 g/L; /28.0134 g/mol -> 28.8075 mol/L; x24.055
  L/mol at 20 C -> 692.9 L; x24.465 at 25 C -> 704.8 L; the dewar table 1:696 inside;
  the 3.5-m3-closet O2 drop to 17.4% < 19.5%; the threshold room ~9.65 m3);
  B3 the thermo (ice cp 2.09 J/gK x 196 K = 409.64 J/g; + fusion 334 = 743.64; ratio
  2.2259 = "only lasts twice as long"; the alt cp 2.1 lane);
  B4 the economics ($5,600 + $1,100 + $10,000 = $16,700; $24,000-$16,700 = $7,300;
  the five watch ratios 7.2396 / 1.009 / 0.98 / 0.99 / 0.996; the N403 live
  like-ratio 2.972% = 435,000/14,637,979);
  B5 the calendar (the series spans 181/216/157/289/374/555 days; N290->N294 2,563;
  N384's 366-day age), via an iterative day-number function, NO date libraries.
- INJECTIONS J1-J4 MUST BE CAUGHT: J1 the affine slip (F = x*1.8, the +32 dropped —
  the reverse witness fails); J2 a dimension-unreduced sum (J/gK + J/g refused);
  J3 the corrupted molar mass (N2 as 14.007, the atom for the molecule — the
  expansion lands at ~1,386 L, outside the verified band); J4 the inverted date
  span (negative, refused).
- DETERMINISM: one book re-run must be byte-identical against its frozen file.
- PIECES: p0, b1, b2, b3, b4, b5, j, d. Scratch under /home/user/e85/, transcripts
  md5-recorded, spliced programmatically.
