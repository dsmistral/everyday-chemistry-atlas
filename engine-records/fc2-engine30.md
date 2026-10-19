# FC2 Engine 30 — the stack-descent fixed-scale verifier (durable review record, session 114 part 1)

The FC2 Phase-3 adversarial review's engine. Fresh code, zero shared with Engines 1–29: written from the recorded design spec + the frozen run-8 strings only (Engine 29's source section was never opened this session).

## Design (the binding spec — rebuild from this alone)

- Stack-descent parser: an explicit frame stack walked left-to-right (zero regex, zero parallel rounds) — the inverse strategy to Engine 29's simultaneous innermost-group regex rewriter. Frames carry their opener character; a closing bracket with the wrong opener or an empty stack is the UNCLOSED/UNMATCHED refusal; a non-empty stack at end-of-string likewise. rounds ≡ max bracket-nesting depth (equal to Engine 29's round count on all four S rows).
- Exact decimal fixed-scale arithmetic: values are {m, s} = m·10^−s (BigInt mantissa, trailing-zero-normalized); derived rows use exact rationals reduced by Stein's binary GCD — no LCM scaling (Engine 29), no prime-product encoding (Engine 28), no digit-wise long division (Engine 27).
- Same physics, independently transcribed: element table {C: 120110, H: 10080, O: 159990} myu; masses in myu; gmol3 = half-up myu/10⁴ at 3 dp; checksum display = myu/1000 at 3 dp (the frozen T-row convention); π = 355/113; half-up rounding at the stated dp throughout.
- P18 restricted names = [smoke grenade, signal flare composition, white phosphorus, tracer round, firework salute], exact-match lowercase gate fired FIRST in compose() — the Engine-29 run-3 lesson held: R2 re-proves 'white phosphorus' dies as P18, not as BAD CHAR 'w'.
- Hydrate dot · splits segments; each segment = optional leading decimal coefficient + element tokens; SINGLE integrality gate on total mass (atom counts stay fixed-scale rationals); unknown symbol -> TABLE REFUSES <sym>; anything else -> BAD CHAR '<c>' refused at position <segOff+i>.
- Equations: each side summed over terms (integer coefficient × parsed mass); equal sides -> thou(total) + " EXACT" ('.' thousands separator); unequal -> CAUGHT gap <gap/1000 at 3 dp> myu (<gap/10⁴ at 3 dp> g) — B8's one-H2O-short must-fail recomputes to exactly 180150 myu.
- Dimension rows recomputed as vectors over {M, L, T, cd} with signed combination, printed in canonical DORDER.
- Expectations = the frozen run-8 battery strings (Engine 29's record, the chapter's Lab FC2.1) — the review target itself. All rows compared by exact equality.

## Engine source (verbatim — ENGINE30.toString() of the executed function)

```
function ENGINE30() {
    const Dc = (m, s = 0)=>({
        m: BigInt(m),
        s: BigInt(s)
      });
    const dNorm = (a)=>{
      let m = a.m, s = a.s;
      while(s > 0n && m % 10n === 0n){
        m /= 10n;
        s -= 1n;
      }
      return {
        m,
        s
      };
    };
    const dAdd = (a, b)=>{
      const s = a.s > b.s ? a.s : b.s;
      return dNorm({
        m: a.m * 10n ** (s - a.s) + b.m * 10n ** (s - b.s),
        s
      });
    };
    const dMul = (a, b)=>dNorm({
        m: a.m * b.m,
        s: a.s + b.s
      });
    const dIsInt = (a)=>a.s === 0n || a.m % 10n ** a.s === 0n;
    const dInt = (a)=>a.m / 10n ** a.s;
    // ===== exact rationals, Stein binary gcd (zero code shared with any prior engine) =====
    const bgcd = (a, b)=>{
      a = a < 0n ? -a : a;
      b = b < 0n ? -b : b;
      if (a === 0n) return b;
      if (b === 0n) return a;
      let sh = 0n;
      while(((a | b) & 1n) === 0n){
        a >>= 1n;
        b >>= 1n;
        sh++;
      }
      while((a & 1n) === 0n)a >>= 1n;
      for(;;){
        while((b & 1n) === 0n)b >>= 1n;
        if (a > b) {
          const t = a;
          a = b;
          b = t;
        }
        b -= a;
        if (b === 0n) break;
      }
      return a << sh;
    };
    const Rr = (n, d = 1)=>{
      const N = BigInt(n), M = BigInt(d);
      const g = bgcd(N, M);
      return {
        n: N / g,
        d: M / g
      };
    };
    const rM = (a, b)=>Rr(a.n * b.n, a.d * b.d);
    const rD = (a, b)=>Rr(a.n * b.d, a.d * b.n);
    const rA = (a, b)=>Rr(a.n * b.d + b.n * a.d, a.d * b.d);
    const rHU = (r, dp)=>{
      const k = r.n * 10n ** BigInt(dp);
      const q = (2n * k + r.d) / (2n * r.d);
      const s = q.toString().padStart(dp + 1, '0');
      return dp > 0 ? s.slice(0, -dp) + '.' + s.slice(-dp) : s;
    };
    // ===== display =====
    const thou = (n)=>{
      let s = n.toString(), o = '';
      while(s.length > 3){
        o = '.' + s.slice(-3) + o;
        s = s.slice(0, -3);
      }
      return s + o;
    };
    const gmol3 = (x)=>rHU(Rr(x.m, 10n ** (x.s + 4n)), 3); // myu -> g/mol, half-up 3 dp
    const tdisp = (myuSum)=>rHU(Rr(myuSum, 1000n), 3); // checksum display (the T-row convention)
    const dEx4 = (x)=>{
      const t = x.s < 4n ? x.m * 10n ** (4n - x.s) : x.m;
      const s = t.toString().padStart(5, '0');
      return s.slice(0, -4) + '.' + s.slice(-4);
    };
    // ===== the stack-descent parser (recursive descent by explicit frame stack, zero regex) =====
    const TABLE = {
      C: 120110n,
      H: 10080n,
      O: 159990n
    }; // {C,H,O}: the 13th zero-admission chapter
    const SYMS = [
      'C',
      'H',
      'O'
    ];
    const P18NAMES = [
      'smoke grenade',
      'signal flare composition',
      'white phosphorus',
      'tracer round',
      'firework salute'
    ];
    const compose = (input)=>{
      const trimmed = input.trim();
      if (P18NAMES.indexOf(trimmed.toLowerCase()) >= 0) return {
        ok: false,
        msg: "P18 REFUSES: '" + trimmed + "'"
      }; // gate FIRST — the run-3 lesson, re-proven by R2
      const segs = trimmed.split('\u00B7');
      const totals = new Map();
      let overallDepth = 0;
      for(let si = 0; si < segs.length; si++){
        const seg = segs[si];
        const segOff = segs.slice(0, si).reduce((a, s)=>a + s.length + 1, 0);
        let i = 0, j = 0, sawDot = false, sawDigit = false;
        while(j < seg.length){
          const c = seg[j];
          if (c >= '0' && c <= '9') {
            sawDigit = true;
            j++;
          } else if (c === '.' && !sawDot && sawDigit) {
            sawDot = true;
            j++;
          } else break;
        }
        let coef;
        if (sawDigit) {
          const str = seg.slice(0, j);
          const dot = str.indexOf('.');
          coef = dot < 0 ? Dc(BigInt(str)) : Dc(BigInt(str.replace('.', '')), str.length - dot - 1);
          i = j;
        } else coef = Dc(1n);
        const stack = [
          {
            opener: '',
            counts: new Map()
          }
        ];
        const cur = ()=>stack[stack.length - 1];
        const bump = (sym, c)=>{
          const m = cur().counts;
          m.set(sym, dAdd(m.get(sym) ?? Dc(0n), c));
        };
        let maxDepth = 0;
        while(i < seg.length){
          const c = seg[i];
          if (c === '(' || c === '[') {
            stack.push({
              opener: c,
              counts: new Map()
            });
            if (stack.length - 1 > maxDepth) maxDepth = stack.length - 1;
            i++;
            continue;
          }
          if (c === ')' || c === ']') {
            if (stack.length === 1 || cur().opener !== (c === ')' ? '(' : '[')) return {
              ok: false,
              msg: "UNCLOSED/UNMATCHED BRACKET refused: '" + trimmed + "'"
            };
            let k = i + 1, mstr = '';
            while(k < seg.length && seg[k] >= '0' && seg[k] <= '9'){
              mstr += seg[k];
              k++;
            }
            const mult = mstr === '' ? Dc(1n) : Dc(BigInt(mstr));
            const frame = stack.pop();
            const top = cur().counts;
            for (const [sym, cnt] of frame.counts)top.set(sym, dAdd(top.get(sym) ?? Dc(0n), dMul(cnt, mult)));
            i = k;
            continue;
          }
          if (c >= 'A' && c <= 'Z') {
            let sym = c;
            let ni = i + 1;
            if (ni < seg.length && seg[ni] >= 'a' && seg[ni] <= 'z') {
              sym += seg[ni];
              ni++;
            }
            if (!(sym in TABLE)) return {
              ok: false,
              msg: 'TABLE REFUSES ' + sym
            };
            i = ni;
            let k = i, dstr = '';
            while(k < seg.length && seg[k] >= '0' && seg[k] <= '9'){
              dstr += seg[k];
              k++;
            }
            bump(sym, dstr === '' ? Dc(1n) : Dc(BigInt(dstr)));
            i = k;
            continue;
          }
          return {
            ok: false,
            msg: "BAD CHAR '" + c + "' refused at position " + (segOff + i)
          };
        }
        if (stack.length > 1) return {
          ok: false,
          msg: "UNCLOSED/UNMATCHED BRACKET refused: '" + trimmed + "'"
        };
        for (const [sym, cnt] of stack[0].counts)totals.set(sym, dAdd(totals.get(sym) ?? Dc(0n), dMul(cnt, coef)));
        if (maxDepth > overallDepth) overallDepth = maxDepth;
      }
      let canon = '', mass = Dc(0n);
      for (const sym of SYMS){
        const c = totals.get(sym);
        if (c && c.m !== 0n) {
          canon += sym + (dIsInt(c) && dInt(c) === 1n ? '' : dIsInt(c) ? dInt(c).toString() : dEx4(c));
          mass = dAdd(mass, dMul(c, Dc(TABLE[sym])));
        }
      }
      if (!dIsInt(mass)) return {
        ok: false,
        msg: 'NON-EXACT refused: total mass ' + dEx4(mass) + ' myu'
      }; // SINGLE integrality gate, on total mass
      return {
        ok: true,
        canon,
        mass,
        depth: overallDepth
      };
    };
    // ===== equation sides =====
    const sideTotal = (side)=>{
      let total = Dc(0n);
      for (const term of side.split('+')){
        const t = term.trim();
        let k = 0, cstr = '';
        while(k < t.length && t[k] >= '0' && t[k] <= '9'){
          cstr += t[k];
          k++;
        }
        const coef = cstr === '' ? Dc(1n) : Dc(BigInt(cstr));
        const r = compose(t.slice(k).trim());
        if (!r.ok) return r;
        total = dAdd(total, dMul(coef, r.mass));
      }
      return {
        ok: true,
        total
      };
    };
    const equation = (eq)=>{
      const parts = eq.split('->');
      const L = sideTotal(parts[0]), R2 = sideTotal(parts[1]);
      if (!L.ok) return L.msg;
      if (!R2.ok) return R2.msg;
      const lt = dInt(L.total), rt = dInt(R2.total);
      if (lt === rt) return thou(lt) + ' EXACT';
      const gap = lt > rt ? lt - rt : rt - lt;
      return 'CAUGHT gap ' + rHU(Rr(gap, 1000n), 3) + ' myu (' + gmol3(Dc(gap)) + ' g)';
    };
    const DKEYS = [
      'M',
      'L',
      'T',
      'cd'
    ];
    const dimComb = (parts)=>{
      const o = {
        M: 0,
        L: 0,
        T: 0,
        cd: 0
      };
      for (const p of parts)for (const k of DKEYS)o[k] += p.s * p.d[k];
      return o;
    };
    const dimStr = (d)=>DKEYS.filter((k)=>d[k] !== 0).map((k)=>k + '^' + d[k]).join('\u00B7');
    // ===== the battery =====
    const lines = [];
    const fails = [];
    let pass = 0;
    const row = (id, label, got, expect)=>{
      const ok = got === expect;
      if (ok) pass++;
      else fails.push(id);
      lines.push((ok ? 'PASS ' : 'FAIL ') + id + ' | ' + label + ' | got "' + got + '" | expect "' + expect + '"');
    };
    const massOf = (f)=>{
      const r = compose(f);
      if (!r.ok) return r.msg;
      return gmol3(r.mass);
    };
    // T — table checksums
    row('T1', 'table checksum \u03A3myu', tdisp(TABLE.C + TABLE.H + TABLE.O), '290.180');
    row('T2', 'positional checksum \u03A3(i+1)\u00B7myu, i zero-based', tdisp(1n * TABLE.C + 2n * TABLE.H + 3n * TABLE.O), '620.240');
    // S — admissions and parses
    row('S1', 'admission C', gmol3(Dc(TABLE.C)), '12.011');
    row('S2', 'admission H', gmol3(Dc(TABLE.H)), '1.008'); // the run-8 vindication, recomputed by a second machine
    row('S3', 'admission O', gmol3(Dc(TABLE.O)), '15.999');
    for (const [id, f, exp] of [
      [
        'S4',
        'CH3(CH2)16COOH',
        'C18H36O2 284.484 rounds=1'
      ],
      [
        'S5',
        'C2H2O4\u00B72H2O',
        'C2H6O6 126.064 rounds=0'
      ],
      [
        'S6',
        '2(CH3)2CHOH',
        'C6H16O2 120.192 rounds=1'
      ],
      [
        'S7',
        '(C(H)4)2',
        'C2H8 32.086 rounds=2'
      ]
    ]){
      const r = compose(f);
      row(id, f, r.ok ? r.canon + ' ' + gmol3(r.mass) + ' rounds=' + r.depth : r.msg, exp);
    }
    // R — refusals
    {
      const r = compose('Ag(S2O3)2');
      row('R1', 'Ag(S2O3)2 \u2014 gate fires post-bracket-expansion', r.ok ? 'PARSED?!' : r.msg, 'TABLE REFUSES Ag');
    }
    {
      const got = [
        'smoke grenade',
        'signal flare composition',
        'white phosphorus',
        'tracer round',
        'firework salute'
      ].map((n)=>compose(n)).map((r)=>r.msg).join(' ; ');
      row('R2', 'the five P18 restricted names (exact each)', got, "P18 REFUSES: 'smoke grenade' ; P18 REFUSES: 'signal flare composition' ; P18 REFUSES: 'white phosphorus' ; P18 REFUSES: 'tracer round' ; P18 REFUSES: 'firework salute'");
    }
    {
      const r = compose('CH4\u00B70.35H2O');
      row('R3', 'CH4\u00B70.35H2O \u2014 single integrality gate on total mass', r.ok ? 'PARSED?!' : r.msg, 'NON-EXACT refused: total mass 223482.5000 myu');
    }
    {
      const r = compose('(CH3');
      row('R4', "'(CH3' \u2014 unclosed bracket", r.ok ? 'PARSED?!' : r.msg, "UNCLOSED/UNMATCHED BRACKET refused: '(CH3'");
    }
    {
      const r = compose('WO3');
      row('R5', 'WO3 \u2014 unknown symbol', r.ok ? 'PARSED?!' : r.msg, 'TABLE REFUSES W');
    }
    {
      const r = compose('C2H5@H');
      row('R6', 'C2H5@H \u2014 bad char', r.ok ? 'PARSED?!' : r.msg, "BAD CHAR '@' refused at position 4");
    }
    // P + N — pins
    const pins = [
      [
        'P1',
        'H2O',
        '18.015'
      ],
      [
        'P2',
        'O2',
        '31.998'
      ],
      [
        'P3',
        'CO2',
        '44.009'
      ],
      [
        'P4',
        'C2H6O',
        '46.069'
      ],
      [
        'P5',
        'C3H8O3',
        '92.094'
      ],
      [
        'P6',
        'C6H10O5',
        '162.141'
      ],
      [
        'P7',
        'C25H52',
        '352.691'
      ],
      [
        'P8',
        'C46H92O2',
        '677.240'
      ],
      [
        'P9',
        'C57H104O6',
        '885.453'
      ],
      [
        'P10',
        'C57H110O6',
        '891.501'
      ],
      [
        'P11',
        'C18H36O2',
        '284.484'
      ],
      [
        'P12',
        'C18H34O2',
        '282.468'
      ],
      [
        'P13',
        'C2H2O4\u00B72H2O',
        '126.064'
      ],
      [
        'P14',
        'C3H8O',
        '60.096'
      ],
      [
        'P15',
        'C3H6O',
        '58.080'
      ],
      [
        'N1',
        'C12H26',
        '170.340'
      ]
    ];
    for (const [id, f, exp] of pins)row(id, id === 'N1' ? 'C12H26 dodecane NEW (zero-hit verified session 113)' : f + ' pin', massOf(f), exp);
    // B — combustion mass balances
    const eqs = [
      [
        'B1',
        'C18H36O2 + 26 O2 -> 18 CO2 + 18 H2O',
        '11.164.320 EXACT'
      ],
      [
        'B2',
        'C25H52 + 38 O2 -> 25 CO2 + 26 H2O',
        '15.686.150 EXACT'
      ],
      [
        'B3',
        'C2H6O + 3 O2 -> 2 CO2 + 3 H2O',
        '1.420.630 EXACT'
      ],
      [
        'B4',
        'C57H104O6 + 80 O2 -> 57 CO2 + 52 H2O',
        '34.452.930 EXACT'
      ],
      [
        'B5',
        '2 C57H110O6 + 163 O2 -> 114 CO2 + 110 H2O',
        '69.986.760 EXACT'
      ],
      [
        'B6',
        '2 C12H26 + 37 O2 -> 24 CO2 + 26 H2O',
        '15.246.060 EXACT'
      ],
      [
        'B7',
        'C2H6O + O2 -> 2 C + 3 H2O',
        '780.670 EXACT'
      ],
      [
        'B8',
        'C2H6O + 3 O2 -> 2 CO2 + 2 H2O',
        'CAUGHT gap 180.150 myu (18.015 g)'
      ]
    ];
    for (const [id, eq, exp] of eqs)row(id, eq, equation(eq), exp);
    // X — O2 debts (g/g, half-up 4 dp)
    const o2mass = dInt(compose('O2').ok ? compose('O2').mass : Dc(0n));
    const debts = [
      [
        'X1',
        'stearic O2 debt 26 O2, g/g at 4 dp',
        26n,
        2844840n,
        '2.9244'
      ],
      [
        'X2',
        'wax O2 debt 38 O2, g/g at 4 dp',
        38n,
        3526910n,
        '3.4476'
      ],
      [
        'X3',
        'ethanol O2 debt 3 O2, g/g at 4 dp',
        3n,
        460690n,
        '2.0837'
      ],
      [
        'X4',
        'dodecane O2 debt 18.5 O2, g/g at 4 dp',
        37n,
        2n * 1703400n,
        '3.4752'
      ],
      [
        'X5',
        'tristearin O2 debt 81.5 O2, g/g at 4 dp',
        163n,
        2n * 8915010n,
        '2.9252'
      ]
    ];
    for (const [id, lab, n, d, exp] of debts)row(id, lab, rHU(Rr(n * o2mass, d), 4), exp);
    // L — the photometric/sound chain
    const PI = Rr(355n, 113n);
    row('L1', '4\u03C0 sr isotropic point candle (\u03C0 = 355/113)', rHU(rM(Rr(4n), PI), 4) + ' lm', '12.5664 lm');
    row('L2', 'illuminance at 1/2/10 m (cd/r\u00B2)', rHU(Rr(1n), 2) + '/' + rHU(Rr(1n, 4n), 2) + '/' + rHU(Rr(1n, 100n), 2) + ' lx', '1.00/0.25/0.01 lx');
    row('L3', 'candle 6 g/h at 42 MJ/kg', rHU(Rr(6n * 42n * 10n ** 6n, 1000n * 3600n), 1) + ' W', '70.0 W');
    row('L4', 'light fraction: 4\u03C0 lm of 683 lm/W at 70 W', rHU(rM(rM(Rr(1420n, 113n), Rr(100n, 683n * 70n)), Rr(1n)), 4) + '%', '0.0263%');
    {
      const th = Rr(94075n, 20340000n); // 0.265 deg in rad, pi = 355/113
      const t2 = rM(th, th), t3 = rM(t2, th), t5 = rM(t3, t2);
      const tan = rA(th, rA(rD(t3, Rr(3n)), rM(Rr(2n, 15n), t5))); // theta + theta^3/3 + 2 theta^5/15
      row('L5', 'heliograph cone at 1.000 km, 0.265\u00B0 half-angle (tan series \u03B8+\u03B8\u00B3/3+2\u03B8\u2075/15)', rHU(rM(tan, Rr(1000n)), 2) + ' m', '4.63 m');
    }
    row('L6', 'echo 2.000 s at 343 m/s', rM(Rr(343n), Rr(2n, 2n)).n.toString() + ' m', '343 m');
    row('L7', 'whistle 100 dB at 100 m (20\u00B7log10(100) = 40.0 drop)', rHU(Rr(100n * 1n - 20n * 2n, 1n), 1) + ' dB', '60.0 dB'); // log10(100) = 2 exactly: 100 = 10^2
    row('L8', 'kerosene lamp 5 g/h at 46 MJ/kg', rHU(Rr(5n * 46n * 10n ** 6n, 1000n * 3600n), 1) + ' W', '63.9 W');
    // W1 — Jurin wick rise [flagged model]
    {
      const gam = Rr(728n, 10000n), rho = Rr(1000n), g = Rr(981n, 100n), r = Rr(5n, 100000n);
      const h = rD(rM(Rr(2n), gam), rM(rho, rM(g, r)));
      row('W1', 'Jurin wick rise r = 50 \u00B5m, \u03B8 = 0 [flagged model: circular pore, \u03B8 = 0]', rHU(h, 3) + ' m', '0.297 m');
    }
    // D — dimension walks (vectors over {M, L, T, cd}, canonical DORDER)
    {
      const gamma = {
        M: 1,
        L: 0,
        T: -2,
        cd: 0
      }, rho2 = {
        M: 1,
        L: -3,
        T: 0,
        cd: 0
      }, g2 = {
        M: 0,
        L: 1,
        T: -2,
        cd: 0
      }, r3 = {
        M: 0,
        L: 1,
        T: 0,
        cd: 0
      };
      row('D1', 'dim(wick rise): \u03B3 \u00F7 (\u03C1\u00B7g\u00B7r), density L\u207B\u00B3 in the walk (the run-3 real fix)', dimStr(dimComb([
        {
          d: gamma,
          s: 1
        },
        {
          d: rho2,
          s: -1
        },
        {
          d: g2,
          s: -1
        },
        {
          d: r3,
          s: -1
        }
      ])), 'L^1');
    }
    {
      const force = {
        M: 1,
        L: 1,
        T: -2,
        cd: 0
      }, dist = {
        M: 0,
        L: 1,
        T: 0,
        cd: 0
      }, time = {
        M: 0,
        L: 0,
        T: 1,
        cd: 0
      };
      row('D2', 'dim(power): (force\u00B7distance) \u00F7 time', dimStr(dimComb([
        {
          d: force,
          s: 1
        },
        {
          d: dist,
          s: 1
        },
        {
          d: time,
          s: -1
        }
      ])), 'M^1\u00B7L^2\u00B7T^-3');
    }
    {
      const cdv = {
        M: 0,
        L: 0,
        T: 0,
        cd: 1
      }, l2 = {
        M: 0,
        L: 2,
        T: 0,
        cd: 0
      };
      row('D3', 'dim(illuminance): cd \u00F7 L\u00B2, canonical DORDER (the run-4 residual)', dimStr(dimComb([
        {
          d: cdv,
          s: 1
        },
        {
          d: l2,
          s: -1
        }
      ])), 'L^-2\u00B7cd^1');
    }
    lines.push('RUN 1 SUMMARY: ' + pass + '/56 PASS' + (fails.length === 0 ? ' \u2014 CLEAN' : ' \u2014 FAILS: ' + fails.join(',')));
    return {
      lines,
      pass,
      fails
    };
  }
```

## Run-1 battery block (frozen — the review recomputation of the frozen run-8 block)

```
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
PASS P1 | H2O pin | got "18.015" | expect "18.015"
PASS P2 | O2 pin | got "31.998" | expect "31.998"
PASS P3 | CO2 pin | got "44.009" | expect "44.009"
PASS P4 | C2H6O pin | got "46.069" | expect "46.069"
PASS P5 | C3H8O3 pin | got "92.094" | expect "92.094"
PASS P6 | C6H10O5 pin | got "162.141" | expect "162.141"
PASS P7 | C25H52 pin | got "352.691" | expect "352.691"
PASS P8 | C46H92O2 pin | got "677.240" | expect "677.240"
PASS P9 | C57H104O6 pin | got "885.453" | expect "885.453"
PASS P10 | C57H110O6 pin | got "891.501" | expect "891.501"
PASS P11 | C18H36O2 pin | got "284.484" | expect "284.484"
PASS P12 | C18H34O2 pin | got "282.468" | expect "282.468"
PASS P13 | C2H2O4·2H2O pin | got "126.064" | expect "126.064"
PASS P14 | C3H8O pin | got "60.096" | expect "60.096"
PASS P15 | C3H6O pin | got "58.080" | expect "58.080"
PASS N1 | C12H26 dodecane NEW (zero-hit verified session 113) | got "170.340" | expect "170.340"
PASS B1 | C18H36O2 + 26 O2 -> 18 CO2 + 18 H2O | got "11.164.320 EXACT" | expect "11.164.320 EXACT"
PASS B2 | C25H52 + 38 O2 -> 25 CO2 + 26 H2O | got "15.686.150 EXACT" | expect "15.686.150 EXACT"
PASS B3 | C2H6O + 3 O2 -> 2 CO2 + 3 H2O | got "1.420.630 EXACT" | expect "1.420.630 EXACT"
PASS B4 | C57H104O6 + 80 O2 -> 57 CO2 + 52 H2O | got "34.452.930 EXACT" | expect "34.452.930 EXACT"
PASS B5 | 2 C57H110O6 + 163 O2 -> 114 CO2 + 110 H2O | got "69.986.760 EXACT" | expect "69.986.760 EXACT"
PASS B6 | 2 C12H26 + 37 O2 -> 24 CO2 + 26 H2O | got "15.246.060 EXACT" | expect "15.246.060 EXACT"
PASS B7 | C2H6O + O2 -> 2 C + 3 H2O | got "780.670 EXACT" | expect "780.670 EXACT"
PASS B8 | C2H6O + 3 O2 -> 2 CO2 + 2 H2O | got "CAUGHT gap 180.150 myu (18.015 g)" | expect "CAUGHT gap 180.150 myu (18.015 g)"
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
RUN 1 SUMMARY: 56/56 PASS — CLEAN
```

## Honest run history

- Run 1 (2026-10-19): RUN 1 SUMMARY: 56/56 PASS — CLEAN

## Part-2 owed list (session 114 part 2)

- The repo-side N1 + attribution re-greps (fetched at a fresh HEAD, saved-JSON pipeline).
- Ex FC2.6's withheld ◆ answer machine-verified against this engine.
- The frozen-block byte-compare (record vs chapter vs repo master) and the chapter-side RX checks.
- The Revision Appendix appended to fc2.md; the map FC2 drafted -> reviewed; row 114 DONE.
