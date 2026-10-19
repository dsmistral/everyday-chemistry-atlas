# FC2 Engine 29 — the parallel-rounds rewriter (durable record)

Session 113, part 1 of 2 (the split-on-trouble amendment). Written at the run-7 close so a context compaction can no longer lose this engine — the engine was lost twice to compaction this session before this record existed. Repo mirror: engine-records/fc2-engine29.md (repo dsmistral/everyday-chemistry-atlas). Status at this close: RUN 8 CLEAN 56/56 (run 7 was 55/56 — the S2 expectation slip, named in the history below).

## Design (the binding spec — rebuild from this alone)
- Parallel-rounds rewriter: every innermost bracket group (both () and []) expanded simultaneously, one regex-global round /(\(([^()]*)\)|\[([^\[\]]*)\])(\d*)/g (g2 paren inner, g3 bracket inner, g4 trailing digits); inner element tokens /([A-Z][a-z]?)(\d*)/g scaled by the group multiplier (k="" -> 1n, multi-digit OK); loop while brackets remain; a round with no progress while brackets are present -> "UNCLOSED/UNMATCHED BRACKET refused: '<formula>'"; more than 24 rounds -> the NON-TERMINATION guard.
- Exact BigInt rationals; masses in myu (1 myu = 1e-4 g/mol); element table {C: 120110, H: 10080, O: 159990} — the {C,H,O} chapter, the 13th zero-admission chapter.
- P18 restricted names = ["smoke grenade","signal flare composition","white phosphorus","tracer round","firework salute"], exact-match lowercase gate fired FIRST in compose() (verified by R2: "white phosphorus" would otherwise die as BAD CHAR 'w').
- Hydrate dot · (U+00B7) splits segments; each segment = optional leading coefficient (decimal OK, exact decRat) + element tokens. Unconsumed char -> "BAD CHAR '<c>' refused at position <segOff+i>"; unknown symbol -> "TABLE REFUSES <sym>" (gate fires post-bracket-expansion, R1).
- SINGLE integrality gate on total mass (atom counts stay rational): CH4·0.35H2O -> 223482.5 myu -> "NON-EXACT refused: total mass 223482.5000 myu" (4-dp exact rational display).
- Dimension lattice: exponent objects over {M, L, T, cd}; DORDER = ["M","L","T","cd"]; display "Sym^e" joined with · (e.g. M^1·L^2·T^-3).
- Display: fmtMyu = thousands separator '.' on BigInt (11164320 -> "11.164.320"); gmol3(myu) = round-half-up myu/1e4 at 3 dp ((2*myu+10)/20 -> fmtDPraw(q,3)); π = 355/113 labeled; roundScaled(r, dp) half-up at stated dp.
- Run-7 comparator: R1/R3/R4/R5/R6 compared by SUBSTRING match (got.includes(expect)); R2 exact equality for all five names; all other rows exact equality.

## Engine source (verbatim — ENGINE29.toString() of the executed function)
```typescript
function ENGINE29() {
  'use strict';
  // ===== Engine 29 — the parallel-rounds rewriter (FC2, session 113) =====
  // Fresh engine: zero code shared with Engines 1-28. Exact BigInt rationals;
  // masses in myu (1 myu = 1e-4 g/mol); held table {C,H,O} (the 13th zero-admission chapter).
  const ELM = {
    C: 120110n,
    H: 10080n,
    O: 159990n
  };
  const ELORDER = [
    'C',
    'H',
    'O'
  ];
  const P18 = [
    'smoke grenade',
    'signal flare composition',
    'white phosphorus',
    'tracer round',
    'firework salute'
  ];
  const DORDER = [
    'M',
    'L',
    'T',
    'cd'
  ];
  function bgcd(a, b) {
    a = a < 0n ? -a : a;
    b = b < 0n ? -b : b;
    while(b){
      const t = a % b;
      a = b;
      b = t;
    }
    return a;
  }
  function rat(n, d) {
    if (d === undefined) d = 1n;
    if (d < 0n) {
      n = -n;
      d = -d;
    }
    if (n === 0n) return {
      n: 0n,
      d: 1n
    };
    const g = bgcd(n, d) || 1n;
    return {
      n: n / g,
      d: d / g
    };
  }
  function rAdd(x, y) {
    return rat(x.n * y.d + y.n * x.d, x.d * y.d);
  }
  function rSub(x, y) {
    return rat(x.n * y.d - y.n * x.d, x.d * y.d);
  }
  function rMul(x, y) {
    return rat(x.n * y.n, x.d * y.d);
  }
  function rDiv(x, y) {
    return rat(x.n * y.d, x.d * y.n);
  }
  function rIsInt(x) {
    return x.d === 1n;
  }
  function decRat(s) {
    const i = s.indexOf('.');
    if (i < 0) return rat(BigInt(s));
    const ip = s.slice(0, i);
    const fp = s.slice(i + 1);
    const ipn = ip === '' ? 0n : BigInt(ip);
    const den = 10n ** BigInt(fp.length);
    return rat(ipn * den + (fp === '' ? 0n : BigInt(fp)), den);
  }
  function fmtMyu(v) {
    const s = v.toString();
    const L = s.length;
    let out = '';
    for(let i = 0; i < L; i++){
      out += s[i];
      const rem = L - 1 - i;
      if (rem > 0 && rem % 3 === 0) out += '.';
    }
    return out;
  }
  function fmtDPraw(q, dp) {
    const p = 10n ** BigInt(dp);
    const whole = q / p;
    const frac = q % p;
    if (dp === 0) return whole.toString();
    return whole.toString() + '.' + frac.toString().padStart(dp, '0');
  }
  function gmol3(myu) {
    return fmtDPraw((2n * myu + 10n) / 20n, 3);
  } // round-half-up myu/1e4 at 3 dp
  function roundScaled(x, dp) {
    const p = 10n ** BigInt(dp);
    const s = x.n * p;
    return (2n * s + x.d) / (2n * x.d);
  }
  function fmtRat(x, dp) {
    return fmtDPraw(roundScaled(x, dp), dp);
  }
  function ratExact4(x) {
    const whole = x.n / x.d;
    const rem = x.n % x.d;
    const f4 = rem * 10000n / x.d;
    const exact = rem * 10000n % x.d === 0n;
    const q = exact ? f4 : (2n * rem * 10000n + x.d) / (2n * x.d);
    return fmtDPraw(whole * 10000n + q, 4);
  }
  // --- parallel-rounds bracket rewriter ---
  function expandBrackets(f) {
    let cur = f;
    let rounds = 0;
    while(/[\[\]()]/.test(cur)){
      if (rounds >= 24) throw new Error('NON-TERMINATION refused: ' + f + ' (bracket rounds > 24)');
      let progress = false;
      cur = cur.replace(/(\(([^()]*)\)|\[([^[\]]*)\])(\d*)/g, function(m, g1, g2, g3, g4) {
        progress = true;
        const inner = g2 !== undefined ? g2 : g3;
        const k = g4 === '' ? 1n : BigInt(g4);
        return inner.replace(/([A-Z][a-z]?)(\d*)/g, function(s, sym, num) {
          const scaled = k * (num === '' ? 1n : BigInt(num));
          return sym + (scaled === 1n ? '' : scaled.toString());
        });
      });
      if (!progress) throw new Error("UNCLOSED/UNMATCHED BRACKET refused: '" + f + "'");
      rounds++;
    }
    return {
      flat: cur,
      rounds: rounds
    };
  }
  function compose(input) {
    if (P18.indexOf(input) !== -1) throw new Error("P18 REFUSES: '" + input + "'");
    const eb = expandBrackets(input);
    const segs = eb.flat.split('\u00B7');
    let total = {
      n: 0n,
      d: 1n
    };
    const counts = {};
    let off = 0;
    for(let si = 0; si < segs.length; si++){
      const seg = segs[si];
      let i = 0;
      const mc = /^(\d+(?:\.\d+)?)/.exec(seg);
      let coef = {
        n: 1n,
        d: 1n
      };
      if (mc) {
        coef = decRat(mc[1]);
        i = mc[1].length;
      }
      const segCounts = {};
      while(i < seg.length){
        const c = seg[i];
        if (c >= 'A' && c <= 'Z') {
          let sym = c;
          let j = i + 1;
          if (j < seg.length && seg[j] >= 'a' && seg[j] <= 'z') {
            sym += seg[j];
            j++;
          }
          if (!(sym in ELM)) throw new Error('TABLE REFUSES ' + sym);
          let nums = '';
          while(j < seg.length && seg[j] >= '0' && seg[j] <= '9'){
            nums += seg[j];
            j++;
          }
          segCounts[sym] = (segCounts[sym] || 0n) + (nums === '' ? 1n : BigInt(nums));
          i = j;
        } else {
          throw new Error("BAD CHAR '" + c + "' refused at position " + (off + i));
        }
      }
      let sm = 0n;
      for(const sym in segCounts)sm += segCounts[sym] * ELM[sym];
      total = rAdd(total, rMul(coef, rat(sm)));
      for(const sym in segCounts)counts[sym] = rAdd(counts[sym] || {
        n: 0n,
        d: 1n
      }, rMul(coef, rat(segCounts[sym])));
      off += seg.length + 1;
    }
    if (!rIsInt(total)) throw new Error('NON-EXACT refused: total mass ' + ratExact4(total) + ' myu');
    return {
      counts: counts,
      mass: total.n,
      rounds: eb.rounds,
      flat: eb.flat
    };
  }
  function formulaOf(counts) {
    let out = '';
    for(let k = 0; k < ELORDER.length; k++){
      const sym = ELORDER[k];
      const c = counts[sym];
      if (!c || c.n === 0n) continue;
      if (c.d !== 1n) return '<rational counts>';
      out += sym + (c.n === 1n ? '' : c.n.toString());
    }
    return out;
  }
  // --- dimension lattice {M, L, T, cd} ---
  function dimMul(a, b) {
    const r = {};
    for(let k = 0; k < DORDER.length; k++){
      const e = (a[DORDER[k]] || 0) + (b[DORDER[k]] || 0);
      if (e) r[DORDER[k]] = e;
    }
    return r;
  }
  function dimDiv(a, b) {
    const r = {};
    for(let k = 0; k < DORDER.length; k++){
      const e = (a[DORDER[k]] || 0) - (b[DORDER[k]] || 0);
      if (e) r[DORDER[k]] = e;
    }
    return r;
  }
  function dimStr(a) {
    const parts = [];
    for(let k = 0; k < DORDER.length; k++){
      const s = DORDER[k];
      if (a[s]) parts.push(s + '^' + a[s]);
    }
    return parts.length ? parts.join('\u00B7') : '1';
  }
  function errMsg(f) {
    try {
      f();
    } catch (e) {
      return String(e && e.message ? e.message : e);
    }
    return '<NO THROW>';
  }
  // --- reaction balance ---
  function sideMass(side) {
    let m = 0n;
    const terms = side.split('+');
    for(let t = 0; t < terms.length; t++){
      const term = terms[t].trim();
      const mt = /^(\d+)\s+(.+)$/.exec(term);
      const coef = mt ? BigInt(mt[1]) : 1n;
      const f = mt ? mt[2] : term;
      m += coef * compose(f).mass;
    }
    return m;
  }
  function balance(reaction) {
    const parts = reaction.split('->');
    const lhs = sideMass(parts[0].trim());
    const rhs = sideMass(parts[1].trim());
    if (lhs === rhs) return fmtMyu(lhs) + ' EXACT';
    const gap = lhs > rhs ? lhs - rhs : rhs - lhs;
    return 'CAUGHT gap ' + fmtMyu(gap) + ' myu (' + gmol3(gap) + ' g)';
  }
  // ===== the 56-row verification battery =====
  const rows = [];
  const R = {
    pass: 0,
    total: 0
  };
  function check(id, label, got, expect, mode) {
    R.total++;
    const g = String(got);
    const e = String(expect);
    const ok = mode === 'substr' ? g.indexOf(e) !== -1 : g === e;
    rows.push((ok ? 'PASS ' : 'FAIL ') + id + ' | ' + label + ' | got ' + JSON.stringify(g) + ' | expect ' + JSON.stringify(e));
    if (ok) R.pass++;
  }
  // TRANSCRIPTION 2
  const t1 = ELM.C + ELM.H + ELM.O;
  check('T1', 'table checksum \u03A3myu', fmtMyu(t1), '290.180');
  const t2 = 1n * ELM.C + 2n * ELM.H + 3n * ELM.O;
  check('T2', 'positional checksum \u03A3(i+1)\u00B7myu, i zero-based', fmtMyu(t2), '620.240');
  // SELF 7
  check('S1', 'admission C', gmol3(ELM.C), '12.011');
  check('S2', 'admission H', gmol3(ELM.H), '1.008');
  check('S3', 'admission O', gmol3(ELM.O), '15.999');
  {
    const s4 = compose('CH3(CH2)16COOH');
    check('S4', 'CH3(CH2)16COOH', formulaOf(s4.counts) + ' ' + gmol3(s4.mass) + ' rounds=' + s4.rounds, 'C18H36O2 284.484 rounds=1');
    const s5 = compose('C2H2O4\u00B72H2O');
    check('S5', 'C2H2O4\u00B72H2O', formulaOf(s5.counts) + ' ' + gmol3(s5.mass) + ' rounds=' + s5.rounds, 'C2H6O6 126.064 rounds=0');
    const s6 = compose('2(CH3)2CHOH');
    check('S6', '2(CH3)2CHOH', formulaOf(s6.counts) + ' ' + gmol3(s6.mass) + ' rounds=' + s6.rounds, 'C6H16O2 120.192 rounds=1');
    const s7 = compose('(C(H)4)2');
    check('S7', '(C(H)4)2', formulaOf(s7.counts) + ' ' + gmol3(s7.mass) + ' rounds=' + s7.rounds, 'C2H8 32.086 rounds=2');
  }
  // REFUSALS 6
  check('R1', 'Ag(S2O3)2 — gate fires post-bracket-expansion', errMsg(function() {
    compose('Ag(S2O3)2');
  }), 'TABLE REFUSES Ag', 'substr');
  {
    const gotS = [];
    const expS = [];
    for(let k = 0; k < P18.length; k++){
      const nm = P18[k];
      gotS.push(errMsg(function() {
        compose(nm);
      }));
      expS.push("P18 REFUSES: '" + nm + "'");
    }
    check('R2', 'the five P18 restricted names (exact each)', gotS.join(' ; '), expS.join(' ; '));
  }
  check('R3', 'CH4\u00B70.35H2O — single integrality gate on total mass', errMsg(function() {
    compose('CH4\u00B70.35H2O');
  }), 'NON-EXACT refused: total mass 223482.5000 myu', 'substr');
  check('R4', "'(CH3' — unclosed bracket", errMsg(function() {
    compose('(CH3');
  }), "UNCLOSED/UNMATCHED BRACKET refused: '(CH3'", 'substr');
  check('R5', 'WO3 — unknown symbol', errMsg(function() {
    compose('WO3');
  }), 'TABLE REFUSES W', 'substr');
  check('R6', 'C2H5@H — bad char', errMsg(function() {
    compose('C2H5@H');
  }), "BAD CHAR '@' refused at position 4", 'substr');
  // PINS 15 (raw grep counts re-verified session 113)
  const PINS = [
    [
      'P1',
      'H2O',
      '18.015',
      'Ch 4 grep\u00D71'
    ],
    [
      'P2',
      'O2',
      '31.998',
      'Ch 10 grep\u00D74'
    ],
    [
      'P3',
      'CO2',
      '44.009',
      'Ch 20 grep\u00D76'
    ],
    [
      'P4',
      'C2H6O',
      '46.069',
      'Ch 21 grep\u00D722'
    ],
    [
      'P5',
      'C3H8O3',
      '92.094',
      'Ch 23 grep\u00D77'
    ],
    [
      'P6',
      'C6H10O5',
      '162.141',
      'Ch 25 grep\u00D71'
    ],
    [
      'P7',
      'C25H52',
      '352.691',
      'Ch 23 grep\u00D72'
    ],
    [
      'P8',
      'C46H92O2',
      '677.240',
      'Ch 23 grep\u00D73 myricyl palmitate'
    ],
    [
      'P9',
      'C57H104O6',
      '885.453',
      'Ch 23 grep\u00D79 triolein'
    ],
    [
      'P10',
      'C57H110O6',
      '891.501',
      'Ch 23 grep\u00D73 tristearin'
    ],
    [
      'P11',
      'C18H36O2',
      '284.484',
      'Ch 23 grep\u00D76 stearic'
    ],
    [
      'P12',
      'C18H34O2',
      '282.468',
      'Ch 23 grep\u00D73 oleic'
    ],
    [
      'P13',
      'C2H2O4\u00B72H2O',
      '126.064',
      'Ch 15 grep\u00D73'
    ],
    [
      'P14',
      'C3H8O',
      '60.096',
      'Ch 21 grep\u00D73 IPA'
    ],
    [
      'P15',
      'C3H6O',
      '58.080',
      'Ch 21 grep\u00D75 acetone'
    ]
  ];
  for(let k = 0; k < PINS.length; k++){
    const p = PINS[k];
    check(p[0], p[1] + ' pin (' + p[3] + ')', gmol3(compose(p[1]).mass), p[2]);
  }
  // NEW 1
  check('N1', 'C12H26 dodecane NEW-candidate (zero-hit local ch03-ch30 confirmed session 113; repo greps ch01/ch02/ch31-ch36/FC1 owed to part 2 pre-freeze)', gmol3(compose('C12H26').mass), '170.340');
  // BALANCES 8
  const BAL = [
    [
      'B1',
      'C18H36O2 + 26 O2 -> 18 CO2 + 18 H2O',
      'stearic complete combustion',
      '11.164.320 EXACT'
    ],
    [
      'B2',
      'C25H52 + 38 O2 -> 25 CO2 + 26 H2O',
      'paraffin wax',
      '15.686.150 EXACT'
    ],
    [
      'B3',
      'C2H6O + 3 O2 -> 2 CO2 + 3 H2O',
      'ethanol',
      '1.420.630 EXACT'
    ],
    [
      'B4',
      'C57H104O6 + 80 O2 -> 57 CO2 + 52 H2O',
      'triolein',
      '34.452.930 EXACT'
    ],
    [
      'B5',
      '2 C57H110O6 + 163 O2 -> 114 CO2 + 110 H2O',
      'tristearin x2',
      '69.986.760 EXACT'
    ],
    [
      'B6',
      '2 C12H26 + 37 O2 -> 24 CO2 + 26 H2O',
      'dodecane x2',
      '15.246.060 EXACT'
    ],
    [
      'B7',
      'C2H6O + O2 -> 2 C + 3 H2O',
      'dark-smoke model (label harness-side — the run-2 lesson)',
      '780.670 EXACT'
    ],
    [
      'B8',
      'MUST-FAIL: C2H6O + 3 O2 -> 2 CO2 + 2 H2O',
      'one-H2O-short must-fail (MUST-FAIL label stripped by the harness before parsing)',
      'CAUGHT gap 180.150 myu (18.015 g)'
    ]
  ];
  for(let k = 0; k < BAL.length; k++){
    const b = BAL[k];
    const rxn = b[1].replace(/^MUST-FAIL: /, '');
    check(b[0], b[2] + ' :: ' + rxn, balance(rxn), b[3]);
  }
  // O2 DEBTS 5
  const mO2 = compose('O2').mass;
  function debt(coefS, fuel) {
    return rDiv(rMul(decRat(coefS), rat(mO2)), rat(compose(fuel).mass));
  }
  check('X1', 'stearic O2 debt 26 O2, g/g at 4 dp', fmtRat(debt('26', 'C18H36O2'), 4), '2.9244');
  check('X2', 'wax O2 debt 38 O2, g/g at 4 dp', fmtRat(debt('38', 'C25H52'), 4), '3.4476');
  check('X3', 'ethanol O2 debt 3 O2, g/g at 4 dp', fmtRat(debt('3', 'C2H6O'), 4), '2.0837');
  check('X4', 'dodecane O2 debt 18.5 O2, g/g at 4 dp', fmtRat(debt('18.5', 'C12H26'), 4), '3.4752');
  check('X5', 'tristearin O2 debt 81.5 O2, g/g at 4 dp', fmtRat(debt('81.5', 'C57H110O6'), 4), '2.9252');
  // LIGHT/SOUND 8
  const PI = rat(355n, 113n);
  check('L1', '4\u03C0 sr isotropic point candle (\u03C0 = 355/113)', fmtRat(rMul(rat(4n), PI), 4) + ' lm', '12.5664 lm');
  {
    const a = fmtRat(rat(1n), 2);
    const b = fmtRat(rDiv(rat(1n), rat(4n)), 2);
    const c = fmtRat(rDiv(rat(1n), rat(100n)), 2);
    check('L2', 'illuminance at 1/2/10 m (cd/r\u00B2)', a + '/' + b + '/' + c + ' lx', '1.00/0.25/0.01 lx');
  }
  check('L3', 'candle 6 g/h at 42 MJ/kg', fmtRat(rDiv(rMul(rat(6n), rat(42000n)), rat(3600n)), 1) + ' W', '70.0 W');
  check('L4', 'light fraction: 4\u03C0 lm of 683 lm/W at 70 W', fmtRat(rMul(rDiv(rMul(rat(4n), PI), rat(683n * 70n)), rat(100n)), 4) + '%', '0.0263%');
  {
    const th = rat(3763n, 813600n); // 0.265 degrees in rad, exact
    const th2 = rMul(th, th);
    const th3 = rMul(th2, th);
    const th5 = rMul(th3, th2);
    const tanv = rAdd(rAdd(th, rDiv(th3, rat(3n))), rDiv(rMul(rat(2n), th5), rat(15n)));
    check('L5', 'heliograph cone at 1.000 km, 0.265\u00B0 half-angle (tan series \u03B8+\u03B8\u00B3/3+2\u03B8\u2075/15)', fmtRat(rMul(tanv, rat(1000n)), 2) + ' m', '4.63 m');
  }
  check('L6', 'echo 2.000 s at 343 m/s', fmtRat(rDiv(rMul(rat(343n), rat(2n)), rat(2n)), 0) + ' m', '343 m');
  check('L7', 'whistle 100 dB at 100 m (20\u00B7log10(100) = 40.0 drop)', fmtRat(rSub(rat(100n), rMul(rat(20n), rat(2n))), 1) + ' dB', '60.0 dB');
  check('L8', 'kerosene lamp 5 g/h at 46 MJ/kg', fmtRat(rDiv(rMul(rat(5n), rat(46000n)), rat(3600n)), 1) + ' W', '63.9 W');
  // WICK 1
  check('W1', 'Jurin wick rise r = 50 \u00B5m, \u03B8 = 0 [flagged model: circular pore, \u03B8 = 0]', fmtRat(rDiv(rat(1456n, 10000n), rat(981n, 2000n)), 3) + ' m', '0.297 m');
  // DIMS 3
  {
    const gamma = {
      M: 1,
      T: -2
    };
    const rho = {
      M: 1,
      L: -3
    };
    const g = {
      L: 1,
      T: -2
    };
    const r = {
      L: 1
    };
    const res = dimDiv(gamma, dimMul(dimMul(rho, g), r));
    check('D1', 'dim(wick rise): \u03B3 \u00F7 (\u03C1\u00B7g\u00B7r), density L\u207B\u00B3 in the walk (the run-3 real fix)', dimStr(res), 'L^1');
  }
  {
    const Fc = {
      M: 1,
      L: 1,
      T: -2
    };
    const work = dimMul(Fc, {
      L: 1
    });
    const Pw = dimDiv(work, {
      T: 1
    });
    check('D2', 'dim(power): (force\u00B7distance) \u00F7 time', dimStr(Pw), 'M^1\u00B7L^2\u00B7T^-3');
  }
  {
    const cd = {
      cd: 1
    };
    const E = dimDiv(cd, {
      L: 2
    });
    check('D3', 'dim(illuminance): cd \u00F7 L\u00B2, canonical DORDER (the run-4 residual)', dimStr(E), 'L^-2\u00B7cd^1');
  }
  const lines = [];
  lines.push('ENGINE 29 RUN 8 \u2014 the repair pass: the S2 expectation corrected, the machine vindicated (the session-104 precedent)');
  for(let i = 0; i < rows.length; i++)lines.push(rows[i]);
  const summary = 'RUN 8 SUMMARY: ' + R.pass + '/' + R.total + (R.pass === R.total ? ' PASS \u2014 CLEAN' : ' \u2014 FAILURES ABOVE');
  lines.push(summary);
  return {
    pass: R.pass,
    total: R.total,
    text: lines.join('\n'),
    summary: summary
  };
}
```

## Honest run history (runs 1–8 — the chapter’s Lab record)
- Runs 1–4 (the first build): run 1 a syntax error; run 2 B7’s "(dark-smoke model)" prose parenthetical reached the parser; run 3 46/56 — TWO REAL ENGINE DEFECTS fixed (the P18 gate moved FIRST in compose(); D1’s dimension walk omitting density’s L⁻³) + five harness display defects; run 4 55/56 (D3 display-order artifact).
- Runs 5–6 (the post-compaction-1 re-execution): 43/56, then 51/56 — every fail comparator-side harness defects, the engine core clean on all rows.
- Run 7 (the post-compaction-2 rebuild + the substring comparator fix for R1/R3/R4/R5/R6): 55/56 — S2 FAILED with the machine right and the expectation wrong: the engine computed H = 10080 myu = 1.008 g/mol (matching FC1’s recorded admission set 12.011/1.008/15.999, session-111 row), while the expectation 10.080 was a 10× slip carried in the handoff — the session-28 lesson caught at an admissions row; the other 55 rows PASS, the engine core clean on every row.
- Run 8 (this close, the repair pass — the S2 expectation corrected to 1.008, nothing else touched): 56/56 CLEAN. Per the session-104 precedent, the battery printed in the chapter is the run-8 output, recorded as the final post-compaction re-execution.

## Run-8 battery block (the frozen record — the chapter’s Lab FC2.1 prints this verbatim)
```
ENGINE 29 RUN 8 — the repair pass: the S2 expectation corrected, the machine vindicated (the session-104 precedent)
PASS T1 | table checksum Σmyu | got "290.180" | expect "290.180"
PASS T2 | positional checksum Σ(i+1)·myu, i zero-based | got "620.240" | expect "620.240"
PASS S1 | admission C | got "12.011" | expect "12.011"
PASS S2 | admission H | got "1.008" | expect "1.008"
PASS S3 | admission O | got "15.999" | expect "15.999"
PASS S4 | CH3(CH2)16COOH | got "C18H36O2 284.484 rounds=1" | expect "C18H36O2 284.484 rounds=1"
PASS S5 | C2H2O4·2H2O | got "C2H6O6 126.064 rounds=0" | expect "C2H6O6 126.064 rounds=0"
PASS S6 | 2(CH3)2CHOH | got "C6H16O2 120.192 rounds=1" | expect "C6H16O2 120.192 rounds=1"
PASS S7 | (C(H)4)2 | got "C2H8 32.086 rounds=2" | expect "C2H8 32.086 rounds=2"
PASS R1 | Ag(S2O3)2 — gate fires post-bracket-expansion | got "TABLE REFUSES Ag" | expect "TABLE REFUSES Ag"
PASS R2 | the five P18 restricted names (exact each) | got "P18 REFUSES: 'smoke grenade' ; P18 REFUSES: 'signal flare composition' ; P18 REFUSES: 'white phosphorus' ; P18 REFUSES: 'tracer round' ; P18 REFUSES: 'firework salute'" | expect "P18 REFUSES: 'smoke grenade' ; P18 REFUSES: 'signal flare composition' ; P18 REFUSES: 'white phosphorus' ; P18 REFUSES: 'tracer round' ; P18 REFUSES: 'firework salute'"
PASS R3 | CH4·0.35H2O — single integrality gate on total mass | got "NON-EXACT refused: total mass 223482.5000 myu" | expect "NON-EXACT refused: total mass 223482.5000 myu"
PASS R4 | '(CH3' — unclosed bracket | got "UNCLOSED/UNMATCHED BRACKET refused: '(CH3'" | expect "UNCLOSED/UNMATCHED BRACKET refused: '(CH3'"
PASS R5 | WO3 — unknown symbol | got "TABLE REFUSES W" | expect "TABLE REFUSES W"
PASS R6 | C2H5@H — bad char | got "BAD CHAR '@' refused at position 4" | expect "BAD CHAR '@' refused at position 4"
PASS P1 | H2O pin (Ch 4 grep×1) | got "18.015" | expect "18.015"
PASS P2 | O2 pin (Ch 10 grep×4) | got "31.998" | expect "31.998"
PASS P3 | CO2 pin (Ch 20 grep×6) | got "44.009" | expect "44.009"
PASS P4 | C2H6O pin (Ch 21 grep×22) | got "46.069" | expect "46.069"
PASS P5 | C3H8O3 pin (Ch 23 grep×7) | got "92.094" | expect "92.094"
PASS P6 | C6H10O5 pin (Ch 25 grep×1) | got "162.141" | expect "162.141"
PASS P7 | C25H52 pin (Ch 23 grep×2) | got "352.691" | expect "352.691"
PASS P8 | C46H92O2 pin (Ch 23 grep×3 myricyl palmitate) | got "677.240" | expect "677.240"
PASS P9 | C57H104O6 pin (Ch 23 grep×9 triolein) | got "885.453" | expect "885.453"
PASS P10 | C57H110O6 pin (Ch 23 grep×3 tristearin) | got "891.501" | expect "891.501"
PASS P11 | C18H36O2 pin (Ch 23 grep×6 stearic) | got "284.484" | expect "284.484"
PASS P12 | C18H34O2 pin (Ch 23 grep×3 oleic) | got "282.468" | expect "282.468"
PASS P13 | C2H2O4·2H2O pin (Ch 15 grep×3) | got "126.064" | expect "126.064"
PASS P14 | C3H8O pin (Ch 21 grep×3 IPA) | got "60.096" | expect "60.096"
PASS P15 | C3H6O pin (Ch 21 grep×5 acetone) | got "58.080" | expect "58.080"
PASS N1 | C12H26 dodecane NEW-candidate (zero-hit local ch03-ch30 confirmed session 113; repo greps ch01/ch02/ch31-ch36/FC1 owed to part 2 pre-freeze) | got "170.340" | expect "170.340"
PASS B1 | stearic complete combustion :: C18H36O2 + 26 O2 -> 18 CO2 + 18 H2O | got "11.164.320 EXACT" | expect "11.164.320 EXACT"
PASS B2 | paraffin wax :: C25H52 + 38 O2 -> 25 CO2 + 26 H2O | got "15.686.150 EXACT" | expect "15.686.150 EXACT"
PASS B3 | ethanol :: C2H6O + 3 O2 -> 2 CO2 + 3 H2O | got "1.420.630 EXACT" | expect "1.420.630 EXACT"
PASS B4 | triolein :: C57H104O6 + 80 O2 -> 57 CO2 + 52 H2O | got "34.452.930 EXACT" | expect "34.452.930 EXACT"
PASS B5 | tristearin x2 :: 2 C57H110O6 + 163 O2 -> 114 CO2 + 110 H2O | got "69.986.760 EXACT" | expect "69.986.760 EXACT"
PASS B6 | dodecane x2 :: 2 C12H26 + 37 O2 -> 24 CO2 + 26 H2O | got "15.246.060 EXACT" | expect "15.246.060 EXACT"
PASS B7 | dark-smoke model (label harness-side — the run-2 lesson) :: C2H6O + O2 -> 2 C + 3 H2O | got "780.670 EXACT" | expect "780.670 EXACT"
PASS B8 | one-H2O-short must-fail (MUST-FAIL label stripped by the harness before parsing) :: C2H6O + 3 O2 -> 2 CO2 + 2 H2O | got "CAUGHT gap 180.150 myu (18.015 g)" | expect "CAUGHT gap 180.150 myu (18.015 g)"
PASS X1 | stearic O2 debt 26 O2, g/g at 4 dp | got "2.9244" | expect "2.9244"
PASS X2 | wax O2 debt 38 O2, g/g at 4 dp | got "3.4476" | expect "3.4476"
PASS X3 | ethanol O2 debt 3 O2, g/g at 4 dp | got "2.0837" | expect "2.0837"
PASS X4 | dodecane O2 debt 18.5 O2, g/g at 4 dp | got "3.4752" | expect "3.4752"
PASS X5 | tristearin O2 debt 81.5 O2, g/g at 4 dp | got "2.9252" | expect "2.9252"
PASS L1 | 4π sr isotropic point candle (π = 355/113) | got "12.5664 lm" | expect "12.5664 lm"
PASS L2 | illuminance at 1/2/10 m (cd/r²) | got "1.00/0.25/0.01 lx" | expect "1.00/0.25/0.01 lx"
PASS L3 | candle 6 g/h at 42 MJ/kg | got "70.0 W" | expect "70.0 W"
PASS L4 | light fraction: 4π lm of 683 lm/W at 70 W | got "0.0263%" | expect "0.0263%"
PASS L5 | heliograph cone at 1.000 km, 0.265° half-angle (tan series θ+θ³/3+2θ⁵/15) | got "4.63 m" | expect "4.63 m"
PASS L6 | echo 2.000 s at 343 m/s | got "343 m" | expect "343 m"
PASS L7 | whistle 100 dB at 100 m (20·log10(100) = 40.0 drop) | got "60.0 dB" | expect "60.0 dB"
PASS L8 | kerosene lamp 5 g/h at 46 MJ/kg | got "63.9 W" | expect "63.9 W"
PASS W1 | Jurin wick rise r = 50 µm, θ = 0 [flagged model: circular pore, θ = 0] | got "0.297 m" | expect "0.297 m"
PASS D1 | dim(wick rise): γ ÷ (ρ·g·r), density L⁻³ in the walk (the run-3 real fix) | got "L^1" | expect "L^1"
PASS D2 | dim(power): (force·distance) ÷ time | got "M^1·L^2·T^-3" | expect "M^1·L^2·T^-3"
PASS D3 | dim(illuminance): cd ÷ L², canonical DORDER (the run-4 residual) | got "L^-2·cd^1" | expect "L^-2·cd^1"
RUN 8 SUMMARY: 56/56 PASS — CLEAN
```

## Pin raw grep counts (re-verified session 113 against the local ch03–ch30 manuscripts)
These are RAW occurrence counts (grep -o); the pre-compaction handoff’s earlier counts were word-context counts and differ for six pins — context inspection shows the extras are legitimate in-equation occurrences (e.g. "46.069" inside "1367/46.069").
- H2O 18.015 ch04 ×1; O2 31.998 ch10 ×4; CO2 44.009 ch20 ×6; C2H6O 46.069 ch21 ×22; C3H8O3 92.094 ch23 ×7; C6H10O5 162.141 ch25 ×1; C25H52 352.691 ch23 ×2; C46H92O2 677.240 ch23 ×3; C57H104O6 885.453 ch23 ×9; C57H110O6 891.501 ch23 ×3; C18H36O2 284.484 ch23 ×6; C18H34O2 282.468 ch23 ×3; C2H2O4·2H2O 126.064 ch15 ×3; C3H8O 60.096 ch21 ×3; C3H6O 58.080 ch21 ×5.

## N1 status (session-100 line)
N1 dodecane C12H26 170.340 g/mol: zero-hit CONFIRMED against the local ch03–ch30 manuscripts (grep -l -E "170\.33|C12H26" — zero hits). The repo greps on ch01/ch02/ch31–ch36/FC1 are OWED to part 2, BEFORE the page freezes; if any prior page prices dodecane, convert N1 to a reused pin per the session-100 protocol.

## Binding lines in force for FC2
session-100 (NEW-composition zero-hit greps before freeze; every composition row grepped against every prior chapter’s page), session-102 (every worked figure a battery row), session-104 (convergence claims at displayed precision), session-112 (every cross-chapter attribution grep-verified in the authoring session itself).
