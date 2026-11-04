# Engine 66 source (re-keyed at record time) — the modular-witness engine, session 172

> **DISCLOSURE.** The original Engine 66 dispatch text was destroyed by the session's context compaction, as was the build-1 Sheet 4 transcript. This source was re-keyed at record time from the design spec and the frozen transcripts (the Engine 65 precedent, session 171), re-run in full, and verified against the runs of record: all seven transcripts reproduced **byte-identically** — probe djb2 482e641a; Piece B (Sheet 1 + Sheet 2, blank-line joined) c58739a7; Sheet 3 part 1 34b4f545; part 2 2560f746; Sheet 4 (engine portion) 93457459; Sheet 6 520fae2 — every recorded digest matched under the discovered convention: djb2, charCode lane, unpadded hex, over the piece text without its trailing newline. The re-key was caught twice by its own byte-gates before running clean (the multiset printer's count-one format — the bare element, not "Na1"; the Sheet 4 injection mass printed at k3 of the 1e5-scaled value, not of the raw integer) and once by the apostrophe lane (two curly apostrophes typed where the frozen header carries ASCII) — recorder defects, the frozen battery untouched, printed here per the honest-history precedent. The transcripts on disk remain the runs of record.

## 1. Kernel (verbatim, the code as re-run)

```ts
// five primes by trial division just under 2^26
const isPrime = (n) => { if (n < 2) return false; for (let i = 2; i * i <= n; i++) if (n % i === 0) return false; return true; };
const primes = [];
for (let n = 67108863; primes.length < 5; n--) if (isPrime(n)) primes.push(n);
// -> 67108859 67108837 67108819 67108777 67108763 (scan order, descending)

const mulmod = (a, b, m) => { a %= m; b %= m; let r = 0; while (b) { if (b & 1) r = (r + a) % m; a = (a + a) % m; b >>>= 1; } return r; };
const powmod = (a, e, m) => { a %= m; let r = 1; while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>>= 1; } return r; };
const invmod = (a, m) => powmod(a, m - 2, m);            // m prime
const resQ = (x, m) => mulmod(((x.n % m) + m) % m, invmod(((x.d % m) + m) % m, m), m);  // n*d^-1 mod m

// exact rationals (iterative gcd; no BigInt, no recursion in the value path)
const gcd = (a, b) => { a = Math.abs(a); b = Math.abs(b); while (b) { const t = a % b; a = b; b = t; } return a; };
const Q = (n, d) => { const g = gcd(n, d) || 1; return { n: n / g, d: d / g }; };
const addQ = (x, y) => Q(x.n * y.d + y.n * x.d, x.d * y.d);
const subQ = (x, y) => Q(x.n * y.d - y.n * x.d, x.d * y.d);
const mulQ = (x, y) => Q(x.n * y.n, x.d * y.d);
const divQ = (x, y) => Q(x.n * y.d, x.d * y.n);
const I = (n) => Q(n, 1);
const q = (n, d) => Q(n, d);        // pin constants as exact decimals: q(84006,1000) = 84.006

// round-half-up print lane: A = 2n*10^k + d - 2cd must lie in [0, 2d)
const halfUpC = (x, k) => { const num = x.n * Math.pow(10, k); const c = Math.floor((2 * num + x.d) / (2 * x.d));
  const A = 2 * num + x.d - 2 * c * x.d; if (A < 0 || A >= 2 * x.d) throw new Error('halfUp lane'); return c; };
const fmt = (c, k) => { let s = String(c); if (k === 0) return s; while (s.length <= k) s = '0' + s;
  return s.slice(0, s.length - k) + '.' + s.slice(s.length - k); };
const printAt = (x, k) => fmt(halfUpC(x, k), k);

// reduced-form witness: no prime < 1000 divides both exactfrac terms
const smallPrimes = []; for (let n = 2; n < 1000; n++) if (isPrime(n)) smallPrimes.push(n);
const reducedOk = (x) => smallPrimes.every((p) => !(x.n % p === 0 && x.d % p === 0));

// digest: djb2, charCode lane, unpadded hex, over the text WITHOUT its trailing newline
const djb2 = (s) => { let h = 5381; for (let i = 0; i < s.length; i++) h = ((h * 33) + s.charCodeAt(i)) >>> 0;
  return h.toString(16); };

// tokenizer with hydrate support (Engine 65's H1 lesson as a first-class probe row)
const BASIS = { H: 100800, C: 1201100, O: 1599900, Na: 2298977, S: 3206000, Cl: 3545300 }; // 1e5-scaled
const DOT = '\u00B7';
function tokenizeSeg(seg) { const re = /([A-Z][a-z]?)(\d*)/g; const out = {}; let m;
  while ((m = re.exec(seg))) { if (!m[0]) break; out[m[1]] = (out[m[1]] || 0) + (m[2] ? parseInt(m[2], 10) : 1); } return out; }
function parseFormula(f) { const segs = f.split(DOT); const ms = {}; const order = [];
  for (let si = 0; si < segs.length; si++) { let seg = segs[si]; let mult = 1;
    if (si > 0) { const mm = seg.match(/^(\d+)/); if (mm) { mult = parseInt(mm[1], 10); seg = seg.slice(mm[0].length); } }
    const counts = tokenizeSeg(seg);
    for (const e of Object.keys(counts)) { if (!(e in ms)) order.push(e); ms[e] = (ms[e] || 0) + counts[e] * mult; } }
  let mass = 0; for (const e of Object.keys(ms)) mass += ms[e] * BASIS[e];
  return { ms, order, mass }; }
// count 1 prints the bare element: "C2 H9 Na O5", "C3H6O" — the re-key's own first byte-gate catch
const cnt = (n) => n > 1 ? String(n) : '';
```

## 2. The row contract (the s3/s6 evaluator)

```ts
const cert = (chain, efN, efD) => { const ef = Q(efN, efD); let n = 0;
  for (const m of primes) if (resQ(chain, m) === resQ(ef, m)) n++; return n; };   // "mods n/5"
const ledgerLine = (label, desc, chain, k, efN, efD, frozenPrint, suffixExpr) => {
  const mods = cert(chain, efN, efD);
  const pr = printAt(chain, k);
  const ok = mods === 5 && pr === frozenPrint && reducedOk(chain) && chain.n === efN && chain.d === efD;
  let suffix = '';
  if (suffixExpr) suffix = ' | frozen ' + suffixExpr[0] + ' ' + cert(chain, suffixExpr[1], suffixExpr[2]) + '/5';
  return { line: label + ' ' + desc + ': mods ' + mods + '/5 | print ' + pr + ' half-up OK | ef '
    + chain.n + '/' + chain.d + ' reduced PASS' + suffix, ok };
};
// Sheet 1: M = parseFormula(f).mass (1e5 integer), "M= " + fmt(M,5) + " -> pin " + printAt(Q(M,100000),3)
// Sheet 2: per-side multisets merged; pin = printAt(Q(mass,100000),3); exact = fmt(mass,5); frozen pin matched
// Sheet 4: each injection's verdict computed in-run (pinOf, multiset compare, chain re-derivation); bracket printed
```

## 3. The battery (the chains, re-keyed)

The chains are rebuilt from the chapter's own constants as exact decimals — pin constants at q(n, 1000) unless noted; every row's frozen exactfrac and print come from the transcripts of record and act as the expectation lane. Representative rows (the full 39 + 25 + 20 + 13 + 11 live in the transcripts, one line each):

```ts
c.L01  = divQ(I(53), q(84006, 1000));                      // 53/84.006        -> ef 26500/42003, print 0.6309 (k4)
c.L02  = mulQ(c.L01, q(82034, 1000));                      // x 82.034         -> ef 2173901/42003, print 51.76 (k2)
c.L05c = mulQ(divQ(I(62), c.L05b), I(100));                // 62/theoretical   -> ef 127152700/1486287, print 85.6 (k1)
c.L10  = divQ(mulQ(q(978,100), q(1036,1000)), q(9982,10000)); // 9.78x1.036/0.9982 -> ef 36186/3565, print 10.15 (k2)
c.L13a = addQ(q(102089,1000), q(138122,1000));             // the door, a sum  -> ef 240211/1000, print 240.211 (k3)
c.L14c = divQ(c.L14a, addQ(c.L14a, c.L14b));               // X_dioxane        -> ef 14790315/30561289, print 0.484 (k3)
c.L16d = mulQ(divQ(divQ(mulQ(I(30), q(184,100)), q(98072,1000)), c.L16b), I(100)); // -> ef 6206800/593229, print 10.5 (k1)
c.R03d = divQ(c.R03b, I(73));                              // 73.20/73          -> ef 3002600/2994241, print 1.003 (k3)
c.R04d = mulQ(c.R04c, q(39, 10));                          // x Kf 3.9         -> ef 260000/1199799, print 0.2167 (k4)
c.R05d = mulQ(q(5035,100), q(15,100));                     // 50.35 x 15%      -> ef 3021/400, print 7.55 (k2)
```

## 4. The re-verification run (record time, build independent of builds 1 and 2)

Read the seven frozen transcripts; rebuild every piece from the chains; byte-compare each against its file; hash with the discovered convention. Result: s0, s1, s2, s3a, s3b, s4 (engine portion), s6 all byte-identical; digests 482e641a / c58739a7 (s1+s2 blank-line joined) / 34b4f545 / 2560f746 / 93457459 / 520fae2 — all six recorded digests reproduced. The s4 file's record note (the build-1 transcript-loss disclosure) sits outside the engine portion and is excluded from the digest, exactly as the build-2 record states. The Piece B scope (c58739a7) was itself re-derived: the piece buffer joins the two sheets with a blank line — the one scope fact the compaction had taken, recovered by a variant scan against the recorded digest and named here.
