# FC3 Engine 31 — the RPN shunting-yard integer-lattice verifier (durable record, session 115 part 1)

The FC3 authoring engine. Fresh code, zero shared with Engines 1–30: two-pass parse (lexer → a materialized postfix token program → value-stack evaluation — no recursive descent, no regex rounds, no in-place frame walk); exact integer ratios (BigInt num/den) reduced by Euclidean MODULAR gcd (not Stein binary, not LCM scaling, not prime-product, not decimal fixed-scale); dimension lattice {M, L, T, Θ} (the heat chapter; cd dropped, Θ added).

## Design (the binding spec — rebuild from this alone)

- Element table {C: 120110, H: 10080, O: 159990, Na: 229900, Cl: 354530, Ca: 400780} myu — the water chapter's six, book-verified against Ch 25/16/24's printed values (NaOCl 74.442, OCl 51.452, NaCl 58.443, Ca(OCl)2 142.982, Ca(OH)2 74.092 all reproduce exactly).
- Canonical formula = ALPHABETICAL symbol order (declared convention; NaOCl → ClNaO, Ca(OH)2 → CaH2O2).
- Postfix program: symbol tokens carry their own subscript (operand scaling bound at lex — the run-1 fix); open markers; grp tokens carry the group multiplier. JUXTAPOSITION = ADDITION at both levels: group close pops-until-marker and sums; end-of-program folds all top-level entries (the run-1 defect: top-level adjacency was never summed — caught by all 17 composition-bearing rows, with the fully-bracketed S10 passing, which localized it).
- rounds ≡ max open-marker depth during lexing (S10 exercises depth 2 on a real composition).
- P18 gate FIRED FIRST (exact lowercase match): FC3's restricted names = [pool shock, trichlor tabs, chlorine gas generator, calcium hypochlorite granules] — the trade's items and the fence, recognized and refused.
- Hydrate dot · splits segments; each segment = optional leading decimal coefficient + tokens; SINGLE integrality gate on total mass (atom counts stay ratios).
- Refusals: unknown symbol -> TABLE REFUSES <sym> (Mg honestly out of scope); non-integer total -> NON-EXACT refused: total mass <x> myu (4 dp exact); bad char -> BAD CHAR '<c>' refused at position <i> (segment-relative); unclosed/mismatched bracket -> UNCLOSED/UNMATCHED BRACKET refused: '<formula>'.
- Display: gmol3 = half-up myu/10⁴ at 3 dp; checksum display myu/1000 at 3 dp; thou '.' separator for balance totals; CAUGHT gap = gap/1000 at 3 dp + g at 3 dp.
- Battery: 46 rows — T2 checksums, S6 admissions + S4 parses, R5 refusals, P9 pins (anchor-grepped session 115: H2O Ch 4 ×1; NaOCl 74.442 ×2 / OCl 51.452 ×1 / NaCl 58.443 ×2 / C6H10O5 ×1 Ch 25; oxalic dihydrate Ch 15 ×3; Ca(OCl)2 Ch 16 ×3; Ca(OH)2 Ch 24 ×5; Cl2 Ch 16 ×3), N1, B4 balances (one must-fail), H7 heat rows (Ch 7's [convergent] 4.184 J/(g·K) ×10 and 2,256 J/g ×4 anchors; kettle totals recomputed fresh — zero-hit in ch06/ch07, they are FC1's figures), D5 dosing rows (the stoichiometric floor priced exactly; guidance doses carry margin — [convergent] inputs verified at part 2), W3 dimension rows.
- N1: PET C10H8O4 = 1,921,700 myu = 192.170 g/mol — the SODIS bottle's polymer. ZERO-HIT locally (ch03–ch30; patterns 192.169/192.17/C10H8O4/polyethylene terephthalate, case-insensitive); repo greps owed at part 2 BEFORE the freeze. The Ca(OCl)2 trap avoided: checked before claiming NEW (Ch 16/18/28 own it).

## Engine source (verbatim — ENGINE31.toString() of the executed function, run-2 form)

```
function ENGINE31() {
    const gE = (a, b)=>{
      while(b){
        const t = a % b;
        a = b;
        b = t;
      }
      return a;
    };
    const Q = (n, d = 1n)=>{
      let N = BigInt(n), M = BigInt(d);
      if (M < 0n) {
        M = -M;
        N = -N;
      }
      const g = gE(N < 0n ? -N : N, M) || 1n;
      return {
        n: N / g,
        d: M / g
      };
    };
    const qA = (a, b)=>Q(a.n * b.d + b.n * a.d, a.d * b.d);
    const qM = (a, b)=>Q(a.n * b.n, a.d * b.d);
    const qD = (a, b)=>qM(a, Q(b.d, b.n));
    const qIsInt = (a)=>a.n % a.d === 0n;
    const qInt = (a)=>a.n / a.d;
    const qHU = (a, dp)=>{
      const k = a.n * 10n ** BigInt(dp);
      const q = (2n * k + a.d) / (2n * a.d);
      const s = q.toString().padStart(dp + 1, '0');
      return dp > 0 ? s.slice(0, -dp) + '.' + s.slice(-dp) : s;
    };
    const thou = (n)=>{
      let s = n.toString(), o = '';
      while(s.length > 3){
        o = '.' + s.slice(-3) + o;
        s = s.slice(0, -3);
      }
      return s + o;
    };
    const gmol3 = (m)=>qHU(Q(m, 10000n), 3);
    const tdisp = (n)=>qHU(Q(n, 1000n), 3);
    const r4 = (a)=>qInt(Q(a.n * 10n ** 4n, a.d)).toString().padStart(5, '0').replace(/(\d*)(\d{4})/, '$1.$2');
    // ===== the table {C,H,O,Na,Cl,Ca} myu =====
    const TABLE = {
      C: 120110n,
      H: 10080n,
      O: 159990n,
      Na: 229900n,
      Cl: 354530n,
      Ca: 400780n
    };
    const SYMS = Object.keys(TABLE).sort(); // canonical = ALPHABETICAL
    const P18 = [
      'pool shock',
      'trichlor tabs',
      'chlorine gas generator',
      'calcium hypochlorite granules'
    ];
    const lex = (seg)=>{
      const rpn = [];
      const opens = [];
      let depth = 0;
      let i = 0;
      while(i < seg.length){
        const c = seg[i];
        if (c === '(' || c === '[') {
          opens.push(c);
          rpn.push({
            t: 'open'
          });
          if (opens.length > depth) depth = opens.length;
          i++;
          continue;
        }
        if (c === ')' || c === ']') {
          if (opens.length === 0 || opens[opens.length - 1] !== (c === ')' ? '(' : '[')) return {
            ok: false,
            msg: 'UNCLOSED/UNMATCHED BRACKET refused'
          };
          opens.pop();
          let k = Q(1n);
          let j = i + 1, ds = '';
          while(j < seg.length && seg[j] >= '0' && seg[j] <= '9'){
            ds += seg[j];
            j++;
          }
          if (ds !== '') k = Q(BigInt(ds));
          rpn.push({
            t: 'grp',
            k
          });
          i = j;
          continue;
        }
        if (c >= 'A' && c <= 'Z') {
          let sym = c, ni = i + 1;
          if (ni < seg.length && seg[ni] >= 'a' && seg[ni] <= 'z') {
            sym += seg[ni];
            ni++;
          }
          if (!(sym in TABLE)) return {
            ok: false,
            msg: 'TABLE REFUSES ' + sym
          };
          let k = Q(1n);
          if (ni < seg.length && seg[ni] >= '0' && seg[ni] <= '9') {
            let ds = '';
            while(ni < seg.length && seg[ni] >= '0' && seg[ni] <= '9'){
              ds += seg[ni];
              ni++;
            }
            k = Q(BigInt(ds));
          }
          rpn.push({
            t: 'sym',
            s: sym,
            k
          });
          i = ni;
          continue;
        }
        return {
          ok: false,
          msg: "BAD CHAR '" + c + "' refused at position " + i
        };
      }
      if (opens.length > 0) return {
        ok: false,
        msg: 'UNCLOSED/UNMATCHED BRACKET refused'
      };
      return {
        ok: true,
        rpn,
        depth
      };
    };
    const evalRpn = (rpn)=>{
      const st = [];
      const addInto = (acc, m)=>{
        for (const [s, v] of m)acc.set(s, qA(acc.get(s) ?? Q(0n), v));
      };
      for (const t of rpn){
        if (t.t === 'open') st.push(null);
        else if (t.t === 'sym') st.push(new Map([
          [
            t.s,
            t.k
          ]
        ]));
        else {
          const acc = new Map();
          let m = st.pop();
          while(m !== null && m !== undefined){
            addInto(acc, m);
            m = st.pop();
          }
          if (m === undefined) return {
            ok: false,
            msg: 'CLOSE WITHOUT OPEN'
          };
          const o = new Map();
          for (const [s, v] of acc)o.set(s, qM(v, t.k));
          st.push(o);
        }
      }
      if (st.length === 0) return {
        ok: false,
        msg: 'EMPTY PROGRAM'
      };
      const total = new Map(); // the run-1 fix: top-level juxtaposition also sums
      for (const m of st){
        if (m === null) return {
          ok: false,
          msg: 'UNCLOSED/UNMATCHED BRACKET refused'
        };
        addInto(total, m);
      }
      return {
        ok: true,
        counts: total
      };
    };
    const compose = (input)=>{
      const trimmed = input.trim();
      if (P18.indexOf(trimmed.toLowerCase()) >= 0) return {
        ok: false,
        msg: "P18 REFUSES: '" + trimmed + "'"
      }; // gate FIRST
      const segs = trimmed.split('\u00B7');
      const totals = new Map();
      let overall = 0;
      for (const seg of segs){
        let j = 0, dot = false, dig = false;
        while(j < seg.length){
          const c = seg[j];
          if (c >= '0' && c <= '9') {
            dig = true;
            j++;
          } else if (c === '.' && !dot && dig) {
            dot = true;
            j++;
          } else break;
        }
        let coef = Q(1n), i = 0;
        if (dig) {
          const s = seg.slice(0, j);
          const dpos = s.indexOf('.');
          coef = dpos < 0 ? Q(BigInt(s)) : Q(BigInt(s.replace('.', '')), 10n ** BigInt(s.length - dpos - 1));
          i = j;
        }
        const L = lex(seg.slice(i));
        if (!L.ok) return {
          ok: false,
          msg: L.msg + (L.msg.startsWith('UNCLOSED') ? ": '" + trimmed + "'" : '')
        };
        const E = evalRpn(L.rpn);
        if (!E.ok) return {
          ok: false,
          msg: E.msg
        };
        for (const [s, v] of E.counts)totals.set(s, qA(totals.get(s) ?? Q(0n), qM(v, coef)));
        if (L.depth > overall) overall = L.depth;
      }
      let canon = '';
      let mass = Q(0n);
      for (const s of SYMS){
        const v = totals.get(s);
        if (v && v.n !== 0n) {
          canon += s + (qIsInt(v) ? qInt(v) === 1n ? '' : qInt(v).toString() : r4(v));
          mass = qA(mass, qM(v, Q(TABLE[s])));
        }
      }
      if (!qIsInt(mass)) return {
        ok: false,
        msg: 'NON-EXACT refused: total mass ' + r4(mass) + ' myu'
      };
      return {
        ok: true,
        canon,
        mass,
        depth: overall
      };
    };
    const sideTotal = (side)=>{
      let t = Q(0n);
      for (const term of side.split('+')){
        const x = term.trim();
        let k = 0, ds = '';
        while(k < x.length && x[k] >= '0' && x[k] <= '9'){
          ds += x[k];
          k++;
        }
        const coef = ds === '' ? Q(1n) : Q(BigInt(ds));
        const r = compose(x.slice(k).trim());
        if (!r.ok) return r;
        t = qA(t, qM(coef, r.mass));
      }
      return {
        ok: true,
        m: qInt(t)
      };
    };
    const equation = (eq)=>{
      const [l, rr] = eq.split('->');
      const L = sideTotal(l), R2 = sideTotal(rr);
      if (!L.ok) return L.msg;
      if (!R2.ok) return R2.msg;
      if (L.m === R2.m) return thou(L.m) + ' EXACT';
      const gap = L.m > R2.m ? L.m - R2.m : R2.m - L.m;
      return 'CAUGHT gap ' + tdisp(gap) + ' myu (' + gmol3(gap) + ' g)';
    };
    const DK = [
      'M',
      'L',
      'T',
      'Θ'
    ];
    const dComb = (parts)=>{
      const o = {
        M: 0,
        L: 0,
        T: 0,
        Θ: 0
      };
      for (const p of parts)for (const k of DK)o[k] += p.s * p.d[k];
      return o;
    };
    const dStr = (d)=>DK.filter((k)=>d[k] !== 0).map((k)=>k + '^' + d[k]).join('\u00B7');
    // ===== the battery =====
    const lines = [];
    let pass = 0;
    const fails = [];
    const row = (id, label, got, expect)=>{
      const ok = got === expect;
      if (ok) pass++;
      else fails.push(id);
      lines.push((ok ? 'PASS ' : 'FAIL ') + id + ' | ' + label + ' | got "' + got + '" | expect "' + expect + '"');
    };
    const massOf = (f)=>{
      const r = compose(f);
      return r.ok ? gmol3(qInt(r.mass)) : r.msg;
    };
    row('T1', 'table checksum \u03A3myu (6 elements)', tdisp(120110n + 10080n + 159990n + 229900n + 354530n + 400780n), '1275.390');
    row('T2', 'positional checksum \u03A3(i+1)\u00B7myu, i zero-based (run-1 hand-sum corrected)', tdisp(1n * 120110n + 2n * 10080n + 3n * 159990n + 4n * 229900n + 5n * 354530n + 6n * 400780n), '5717.170');
    row('S1', 'admission C', gmol3(120110n), '12.011');
    row('S2', 'admission H', gmol3(10080n), '1.008');
    row('S3', 'admission O', gmol3(159990n), '15.999');
    row('S4', 'admission Na', gmol3(229900n), '22.990');
    row('S5', 'admission Cl', gmol3(354530n), '35.453');
    row('S6', 'admission Ca', gmol3(400780n), '40.078');
    {
      const r = compose('NaOCl');
      row('S7', 'NaOCl', r.ok ? r.canon + ' ' + gmol3(qInt(r.mass)) + ' rounds=' + r.depth : r.msg, 'ClNaO 74.442 rounds=0');
    }
    {
      const r = compose('Ca(OCl)2');
      row('S8', 'Ca(OCl)2', r.ok ? r.canon + ' ' + gmol3(qInt(r.mass)) + ' rounds=' + r.depth : r.msg, 'CaCl2O2 142.982 rounds=1');
    }
    {
      const r = compose('C2H2O4\u00B72H2O');
      row('S9', 'C2H2O4\u00B72H2O', r.ok ? r.canon + ' ' + gmol3(qInt(r.mass)) + ' rounds=' + r.depth : r.msg, 'C2H6O6 126.064 rounds=0');
    }
    {
      const r = compose('(Na(OCl))2');
      row('S10', '(Na(OCl))2 — redundant-nesting probe on a real composition', r.ok ? r.canon + ' ' + gmol3(qInt(r.mass)) + ' rounds=' + r.depth : r.msg, 'Cl2Na2O2 148.884 rounds=2');
    }
    {
      const got = P18.map((n)=>compose(n)).map((r)=>r.msg).join(' ; ');
      row('R1', 'the four P18 restricted names (exact each — gate fires FIRST)', got, "P18 REFUSES: 'pool shock' ; P18 REFUSES: 'trichlor tabs' ; P18 REFUSES: 'chlorine gas generator' ; P18 REFUSES: 'calcium hypochlorite granules'");
    }
    {
      const r = compose('MgSO4');
      row('R2', 'MgSO4 — element honestly out of scope this chapter', r.ok ? 'PARSED?!' : r.msg, 'TABLE REFUSES Mg');
    }
    {
      const r = compose('NaCl\u00B70.35H2O');
      row('R3', 'NaCl\u00B70.35H2O — single integrality gate on total mass', r.ok ? 'PARSED?!' : r.msg, 'NON-EXACT refused: total mass 647482.5000 myu');
    }
    {
      const r = compose('(NaOCl');
      row('R4', "'(NaOCl' — unclosed bracket", r.ok ? 'PARSED?!' : r.msg, "UNCLOSED/UNMATCHED BRACKET refused: '(NaOCl'");
    }
    {
      const r = compose('NaOCl@H2O');
      row('R5', 'NaOCl@H2O — bad char', r.ok ? 'PARSED?!' : r.msg, "BAD CHAR '@' refused at position 5");
    }
    const pins = [
      [
        'P1',
        'H2O pin (Ch 4 grep\u00D71)',
        'H2O',
        '18.015'
      ],
      [
        'P2',
        'NaOCl pin (Ch 25 grep\u00D72)',
        'NaOCl',
        '74.442'
      ],
      [
        'P3',
        'OCl pin (Ch 25 grep\u00D71)',
        'OCl',
        '51.452'
      ],
      [
        'P4',
        'NaCl pin (Ch 25 grep\u00D72)',
        'NaCl',
        '58.443'
      ],
      [
        'P5',
        'C2H2O4\u00B72H2O pin (Ch 15 grep\u00D73)',
        'C2H2O4\u00B72H2O',
        '126.064'
      ],
      [
        'P6',
        'C6H10O5 pin (Ch 25 grep\u00D71)',
        'C6H10O5',
        '162.141'
      ],
      [
        'P7',
        'Ca(OCl)2 pin (Ch 16 grep\u00D73)',
        'Ca(OCl)2',
        '142.982'
      ],
      [
        'P8',
        'Ca(OH)2 pin (Ch 24 grep\u00D75)',
        'Ca(OH)2',
        '74.092'
      ],
      [
        'P9',
        'Cl2 pin (Ch 16 grep\u00D73)',
        'Cl2',
        '70.906'
      ]
    ];
    for (const [id, lab, f, exp] of pins)row(id, lab, massOf(f), exp);
    {
      const r = compose('C10H8O4');
      row('N1', 'C10H8O4 PET NEW-candidate (zero-hit local ch03\u2013ch30 confirmed session 115; repo greps ch01/ch02/ch31\u2013ch36/fc1/fc2 owed at part 2 pre-freeze)', r.ok ? gmol3(qInt(r.mass)) : r.msg, '192.170');
    }
    row('B1', 'hypochlorite decomposition :: 2 NaOCl -> 2 NaCl + O2', equation('2 NaOCl -> 2 NaCl + O2'), '1.488.840 EXACT');
    row('B2', 'calcium hypochlorite decomposition :: Ca(OCl)2 -> CaCl2 + O2', equation('Ca(OCl)2 -> CaCl2 + O2'), '1.429.820 EXACT');
    row('B3', 'the storage-scale chemistry :: Ca(OH)2 + CO2 -> CaCO3 + H2O', equation('Ca(OH)2 + CO2 -> CaCO3 + H2O'), '1.181.010 EXACT');
    row('B4', 'oxygen-overstated must-fail :: NaOCl -> NaCl + 2 O2', equation('NaOCl -> NaCl + 2 O2'), 'CAUGHT gap 479.970 myu (47.997 g)');
    row('H1', 'c_p delivery: 1,000 g \u00D7 4.184 J/(g\u00B7K) \u00D7 1.0 K (Ch 7 [convergent])', qHU(Q(1000n * 4184n, 1000n * 1000n), 3) + ' kJ', '4.184 kJ');
    row('H2', '20.0 -> 100.0 \u00B0C: 1,000 g \u00D7 4.184 \u00D7 80.0', qHU(Q(1000n * 4184n * 80n, 1000n * 1000n), 3) + ' kJ', '334.720 kJ');
    row('H3', 'the phase change: 1,000 g \u00D7 2,256 J/g (Ch 7 pin)', qHU(Q(1000n * 2256n, 1000n), 3) + ' kJ', '2256.000 kJ');
    row('H4', 'total to boil 1 L from 20.0 \u00B0C', qHU(Q(1000n * 4184n * 80n + 1000n * 2256n * 1000n, 1000n * 1000n), 3) + ' kJ', '2590.720 kJ');
    row('H5', 'altitude boil point [flagged model: the 300 m rule]: 3,000 m', qHU(Q(100n - 10n, 1n), 1) + ' \u00B0C', '90.0 \u00B0C');
    row('H6', 'altitude total [flagged model: latent held at 2,256 J/g]: 20 -> 90 \u00B0C', qHU(Q(1000n * 4184n * 70n + 1000n * 2256n * 1000n, 1000n * 1000n), 3) + ' kJ', '2548.880 kJ');
    {
      const latent = Q(1000n * 2256n);
      const sensible = Q(1000n * 4184n * 70n, 1000n);
      const tot = qA(latent, sensible);
      row('H7', 'latent share at altitude: 2,256,000 / 2,548,880 (run-1 formula corrected)', qHU(qM(qD(latent, tot), Q(100n)), 1) + '%', '88.5%');
    }
    row('D1', '2 mg/L as Cl2 -> NaOCl (stoichiometric floor)', qHU(Q(2n * 744420n, 709060n), 4) + ' mg/L', '2.0997 mg/L');
    row('D2', 'as 5% w/w household bleach (run-1 rounding corrected)', qHU(Q(2n * 744420n * 20n, 709060n), 3) + ' mg/L', '41.995 mg/L');
    row('D3', 'per drop [convergent inputs: 0.05 mL, 1.08 g/mL, 5%]: NaOCl per drop (run-1 conversion corrected)', qHU(Q(27n, 10n), 2) + ' mg', '2.70 mg');
    row('D4', 'one drop per 2 L, expressed as Cl2', qHU(qM(Q(27n, 10n), Q(709060n, 744420n * 2n)), 3) + ' mg/L', '1.286 mg/L');
    row('D5', 'two drops per 1 L (CDC-style guidance), expressed as Cl2', qHU(qM(Q(54n, 10n), Q(709060n, 744420n)), 3) + ' mg/L', '5.143 mg/L');
    {
      const m = {
        M: 1,
        L: 0,
        T: 0,
        Θ: 0
      }, l3 = {
        M: 0,
        L: 3,
        T: 0,
        Θ: 0
      };
      row('W1', 'dim(dose): mg/L', dStr(dComb([
        {
          d: m,
          s: 1
        },
        {
          d: l3,
          s: -1
        }
      ])), 'M^1\u00B7L^-3');
    }
    {
      const J = {
        M: 1,
        L: 2,
        T: -2,
        Θ: 0
      }, gK = {
        M: 1,
        L: 0,
        T: 0,
        Θ: 1
      };
      row('W2', 'dim(c_p): J \u00F7 (g\u00B7K)', dStr(dComb([
        {
          d: J,
          s: 1
        },
        {
          d: gK,
          s: -1
        }
      ])), 'L^2\u00B7T^-2\u00B7\u0398^-1');
    }
    {
      const J = {
        M: 1,
        L: 2,
        T: -2,
        Θ: 0
      }, g = {
        M: 1,
        L: 0,
        T: 0,
        Θ: 0
      };
      row('W3', 'dim(latent heat): J \u00F7 g', dStr(dComb([
        {
          d: J,
          s: 1
        },
        {
          d: g,
          s: -1
        }
      ])), 'L^2\u00B7T^-2');
    }
    lines.push('RUN 2 SUMMARY: ' + pass + '/46 PASS' + (fails.length === 0 ? ' \u2014 CLEAN' : ' \u2014 FAILS: ' + fails.join(',')));
    return {
      lines,
      pass,
      fails
    };
  }
```

## Run-1 battery block (verbatim — the honest history)

```
PASS T1 | table checksum Σmyu (6 elements) | got "1275.390" | expect "1275.390"
FAIL T2 | positional checksum Σ(i+1)·myu, i zero-based | got "5717.170" | expect "5717.070"
PASS S1 | admission C | got "12.011" | expect "12.011"
PASS S2 | admission H | got "1.008" | expect "1.008"
PASS S3 | admission O | got "15.999" | expect "15.999"
PASS S4 | admission Na | got "22.990" | expect "22.990"
PASS S5 | admission Cl | got "35.453" | expect "35.453"
PASS S6 | admission Ca | got "40.078" | expect "40.078"
FAIL S7 | NaOCl | got "STACK NOT SINGLETON" | expect "ClNaO 74.442 rounds=0"
FAIL S8 | Ca(OCl)2 | got "STACK NOT SINGLETON" | expect "CaCl2O2 142.982 rounds=1"
FAIL S9 | C2H2O4·2H2O | got "STACK NOT SINGLETON" | expect "C2H6O6 126.064 rounds=0"
PASS S10 | (Na(OCl))2 — redundant-nesting probe on a real composition | got "Cl2Na2O2 148.884 rounds=2" | expect "Cl2Na2O2 148.884 rounds=2"
PASS R1 | the four P18 restricted names (exact each — gate fires FIRST) | got "P18 REFUSES: 'pool shock' ; P18 REFUSES: 'trichlor tabs' ; P18 REFUSES: 'chlorine gas generator' ; P18 REFUSES: 'calcium hypochlorite granules'" | expect "P18 REFUSES: 'pool shock' ; P18 REFUSES: 'trichlor tabs' ; P18 REFUSES: 'chlorine gas generator' ; P18 REFUSES: 'calcium hypochlorite granules'"
PASS R2 | MgSO4 — element honestly out of scope this chapter | got "TABLE REFUSES Mg" | expect "TABLE REFUSES Mg"
FAIL R3 | NaCl·0.35H2O — single integrality gate on total mass | got "STACK NOT SINGLETON" | expect "NON-EXACT refused: total mass 647482.5000 myu"
PASS R4 | '(NaOCl' — unclosed bracket | got "UNCLOSED/UNMATCHED BRACKET refused: '(NaOCl'" | expect "UNCLOSED/UNMATCHED BRACKET refused: '(NaOCl'"
PASS R5 | NaOCl@H2O — bad char | got "BAD CHAR '@' refused at position 5" | expect "BAD CHAR '@' refused at position 5"
FAIL P1 | H2O pin (Ch 4 grep×1) | got "STACK NOT SINGLETON" | expect "18.015"
FAIL P2 | NaOCl pin (Ch 25 grep×2) | got "STACK NOT SINGLETON" | expect "74.442"
FAIL P3 | OCl pin (Ch 25 grep×1) | got "STACK NOT SINGLETON" | expect "51.452"
FAIL P4 | NaCl pin (Ch 25 grep×2) | got "STACK NOT SINGLETON" | expect "58.443"
FAIL P5 | C2H2O4·2H2O pin (Ch 15 grep×3) | got "STACK NOT SINGLETON" | expect "126.064"
FAIL P6 | C6H10O5 pin (Ch 25 grep×1) | got "STACK NOT SINGLETON" | expect "162.141"
FAIL P7 | Ca(OCl)2 pin (Ch 16 grep×3) | got "STACK NOT SINGLETON" | expect "142.982"
FAIL P8 | Ca(OH)2 pin (Ch 24 grep×5) | got "STACK NOT SINGLETON" | expect "74.092"
PASS P9 | Cl2 pin (Ch 16 grep×3) | got "70.906" | expect "70.906"
FAIL N1 | C10H8O4 PET NEW-candidate (zero-hit local ch03–ch30 confirmed session 115; repo greps ch01/ch02/ch31–ch36/fc1/fc2 owed at part 2 pre-freeze) | got "STACK NOT SINGLETON" | expect "192.170"
FAIL B1 | hypochlorite decomposition :: 2 NaOCl -> 2 NaCl + O2 | got "STACK NOT SINGLETON" | expect "1.488.840 EXACT"
FAIL B2 | calcium hypochlorite decomposition :: Ca(OCl)2 -> CaCl2 + O2 | got "STACK NOT SINGLETON" | expect "1.429.820 EXACT"
FAIL B3 | the storage-scale chemistry :: Ca(OH)2 + CO2 -> CaCO3 + H2O | got "STACK NOT SINGLETON" | expect "1.181.010 EXACT"
FAIL B4 | oxygen-overstated must-fail :: NaOCl -> NaCl + 2 O2 | got "STACK NOT SINGLETON" | expect "CAUGHT gap 479.970 myu (47.997 g)"
PASS H1 | c_p delivery: 1,000 g × 4.184 J/(g·K) × 1.0 K (Ch 7 [convergent]) | got "4.184 kJ" | expect "4.184 kJ"
PASS H2 | 20.0 -> 100.0 °C: 1,000 g × 4.184 × 80.0 | got "334.720 kJ" | expect "334.720 kJ"
PASS H3 | the phase change: 1,000 g × 2,256 J/g (Ch 7 pin) | got "2256.000 kJ" | expect "2256.000 kJ"
PASS H4 | total to boil 1 L from 20.0 °C | got "2590.720 kJ" | expect "2590.720 kJ"
PASS H5 | altitude boil point [flagged model: the 300 m rule]: 3,000 m | got "90.0 °C" | expect "90.0 °C"
PASS H6 | altitude total [flagged model: latent held at 2,256 J/g]: 20 -> 90 °C | got "2548.880 kJ" | expect "2548.880 kJ"
FAIL H7 | latent share at altitude: 2,256,000 / 2,548,880 | got "0.1%" | expect "88.5%"
PASS D1 | 2 mg/L as Cl2 -> NaOCl (stoichiometric floor) | got "2.0997 mg/L" | expect "2.0997 mg/L"
FAIL D2 | as 5% w/w household bleach | got "41.995 mg/L" | expect "41.994 mg/L"
FAIL D3 | per drop [convergent inputs: 0.05 mL, 1.08 g/mL, 5%]: NaOCl per drop | got "0.00 mg" | expect "2.70 mg"
PASS D4 | one drop per 2 L, expressed as Cl2 | got "1.286 mg/L" | expect "1.286 mg/L"
PASS D5 | two drops per 1 L (CDC-style guidance), expressed as Cl2 | got "5.143 mg/L" | expect "5.143 mg/L"
PASS W1 | dim(dose): mg/L | got "M^1·L^-3" | expect "M^1·L^-3"
PASS W2 | dim(c_p): J ÷ (g·K) | got "L^2·T^-2·Θ^-1" | expect "L^2·T^-2·Θ^-1"
PASS W3 | dim(latent heat): J ÷ g | got "L^2·T^-2" | expect "L^2·T^-2"
RUN 1 SUMMARY: 25/46 PASS — FAILS: T2,S7,S8,S9,R3,P1,P2,P3,P4,P5,P6,P7,P8,N1,B1,B2,B3,B4,H7,D2,D3
```

## Honest run history (runs 1–2)

- Run 1 (2026-10-19): 25/46 — ONE REAL ENGINE DEFECT + FOUR HARNESS-SIDE SLIPS, all named. The engine defect: top-level juxtaposition (adjacent operands like Na·O·Cl in NaOCl) was pushed as separate stack entries and never summed — 17 rows failed (every composition-bearing row: S7–S9, R3, P1–P8, N1, B1–B4), while the fully-bracketed S10 passed, localizing the defect exactly; free postfix subscripts would also have mis-bound (CH3 read as (CH)3). The fix (run 2): subscripts bound to their symbol token at lex; group close sums until its marker; end-of-program folds all top-level entries. The four harness-side slips: T2 the hand-summed positional checksum (hand 5,717,070 vs machine 5,717,170 — the FC2-S2 class again, the machine vindicated); H7 the percent formula (an extra ×1000 in the numerator scale); D2 the rounding (hand 41.994 vs machine 41.99475 -> 41.995 at 3 dp); D3 the gram->mg conversion (27/10⁷ instead of 27/10).
- Run 2 (2026-10-19): RUN 2 SUMMARY: 46/46 PASS — CLEAN

## Run-2 battery block (frozen — the chapter's Lab FC3.1 prints this verbatim)

```
PASS T1 | table checksum Σmyu (6 elements) | got "1275.390" | expect "1275.390"
PASS T2 | positional checksum Σ(i+1)·myu, i zero-based (run-1 hand-sum corrected) | got "5717.170" | expect "5717.170"
PASS S1 | admission C | got "12.011" | expect "12.011"
PASS S2 | admission H | got "1.008" | expect "1.008"
PASS S3 | admission O | got "15.999" | expect "15.999"
PASS S4 | admission Na | got "22.990" | expect "22.990"
PASS S5 | admission Cl | got "35.453" | expect "35.453"
PASS S6 | admission Ca | got "40.078" | expect "40.078"
PASS S7 | NaOCl | got "ClNaO 74.442 rounds=0" | expect "ClNaO 74.442 rounds=0"
PASS S8 | Ca(OCl)2 | got "CaCl2O2 142.982 rounds=1" | expect "CaCl2O2 142.982 rounds=1"
PASS S9 | C2H2O4·2H2O | got "C2H6O6 126.064 rounds=0" | expect "C2H6O6 126.064 rounds=0"
PASS S10 | (Na(OCl))2 — redundant-nesting probe on a real composition | got "Cl2Na2O2 148.884 rounds=2" | expect "Cl2Na2O2 148.884 rounds=2"
PASS R1 | the four P18 restricted names (exact each — gate fires FIRST) | got "P18 REFUSES: 'pool shock' ; P18 REFUSES: 'trichlor tabs' ; P18 REFUSES: 'chlorine gas generator' ; P18 REFUSES: 'calcium hypochlorite granules'" | expect "P18 REFUSES: 'pool shock' ; P18 REFUSES: 'trichlor tabs' ; P18 REFUSES: 'chlorine gas generator' ; P18 REFUSES: 'calcium hypochlorite granules'"
PASS R2 | MgSO4 — element honestly out of scope this chapter | got "TABLE REFUSES Mg" | expect "TABLE REFUSES Mg"
PASS R3 | NaCl·0.35H2O — single integrality gate on total mass | got "NON-EXACT refused: total mass 647482.5000 myu" | expect "NON-EXACT refused: total mass 647482.5000 myu"
PASS R4 | '(NaOCl' — unclosed bracket | got "UNCLOSED/UNMATCHED BRACKET refused: '(NaOCl'" | expect "UNCLOSED/UNMATCHED BRACKET refused: '(NaOCl'"
PASS R5 | NaOCl@H2O — bad char | got "BAD CHAR '@' refused at position 5" | expect "BAD CHAR '@' refused at position 5"
PASS P1 | H2O pin (Ch 4 grep×1) | got "18.015" | expect "18.015"
PASS P2 | NaOCl pin (Ch 25 grep×2) | got "74.442" | expect "74.442"
PASS P3 | OCl pin (Ch 25 grep×1) | got "51.452" | expect "51.452"
PASS P4 | NaCl pin (Ch 25 grep×2) | got "58.443" | expect "58.443"
PASS P5 | C2H2O4·2H2O pin (Ch 15 grep×3) | got "126.064" | expect "126.064"
PASS P6 | C6H10O5 pin (Ch 25 grep×1) | got "162.141" | expect "162.141"
PASS P7 | Ca(OCl)2 pin (Ch 16 grep×3) | got "142.982" | expect "142.982"
PASS P8 | Ca(OH)2 pin (Ch 24 grep×5) | got "74.092" | expect "74.092"
PASS P9 | Cl2 pin (Ch 16 grep×3) | got "70.906" | expect "70.906"
PASS N1 | C10H8O4 PET NEW-candidate (zero-hit local ch03–ch30 confirmed session 115; repo greps ch01/ch02/ch31–ch36/fc1/fc2 owed at part 2 pre-freeze) | got "192.170" | expect "192.170"
PASS B1 | hypochlorite decomposition :: 2 NaOCl -> 2 NaCl + O2 | got "1.488.840 EXACT" | expect "1.488.840 EXACT"
PASS B2 | calcium hypochlorite decomposition :: Ca(OCl)2 -> CaCl2 + O2 | got "1.429.820 EXACT" | expect "1.429.820 EXACT"
PASS B3 | the storage-scale chemistry :: Ca(OH)2 + CO2 -> CaCO3 + H2O | got "1.181.010 EXACT" | expect "1.181.010 EXACT"
PASS B4 | oxygen-overstated must-fail :: NaOCl -> NaCl + 2 O2 | got "CAUGHT gap 479.970 myu (47.997 g)" | expect "CAUGHT gap 479.970 myu (47.997 g)"
PASS H1 | c_p delivery: 1,000 g × 4.184 J/(g·K) × 1.0 K (Ch 7 [convergent]) | got "4.184 kJ" | expect "4.184 kJ"
PASS H2 | 20.0 -> 100.0 °C: 1,000 g × 4.184 × 80.0 | got "334.720 kJ" | expect "334.720 kJ"
PASS H3 | the phase change: 1,000 g × 2,256 J/g (Ch 7 pin) | got "2256.000 kJ" | expect "2256.000 kJ"
PASS H4 | total to boil 1 L from 20.0 °C | got "2590.720 kJ" | expect "2590.720 kJ"
PASS H5 | altitude boil point [flagged model: the 300 m rule]: 3,000 m | got "90.0 °C" | expect "90.0 °C"
PASS H6 | altitude total [flagged model: latent held at 2,256 J/g]: 20 -> 90 °C | got "2548.880 kJ" | expect "2548.880 kJ"
PASS H7 | latent share at altitude: 2,256,000 / 2,548,880 (run-1 formula corrected) | got "88.5%" | expect "88.5%"
PASS D1 | 2 mg/L as Cl2 -> NaOCl (stoichiometric floor) | got "2.0997 mg/L" | expect "2.0997 mg/L"
PASS D2 | as 5% w/w household bleach (run-1 rounding corrected) | got "41.995 mg/L" | expect "41.995 mg/L"
PASS D3 | per drop [convergent inputs: 0.05 mL, 1.08 g/mL, 5%]: NaOCl per drop (run-1 conversion corrected) | got "2.70 mg" | expect "2.70 mg"
PASS D4 | one drop per 2 L, expressed as Cl2 | got "1.286 mg/L" | expect "1.286 mg/L"
PASS D5 | two drops per 1 L (CDC-style guidance), expressed as Cl2 | got "5.143 mg/L" | expect "5.143 mg/L"
PASS W1 | dim(dose): mg/L | got "M^1·L^-3" | expect "M^1·L^-3"
PASS W2 | dim(c_p): J ÷ (g·K) | got "L^2·T^-2·Θ^-1" | expect "L^2·T^-2·Θ^-1"
PASS W3 | dim(latent heat): J ÷ g | got "L^2·T^-2" | expect "L^2·T^-2"
RUN 2 SUMMARY: 46/46 PASS — CLEAN
```

## Part-2 owed list (session 115 part 2)

- Repo N1 zero-hit greps (ch01, ch02, ch31–ch36, fc1, fc2 at a fresh HEAD, saved-JSON pipeline) BEFORE the freeze.
- [convergent] web battery: WHO/CDC chlorination doses + 5% household bleach + drop volume 0.05 mL + density 1.08 + the 300 m altitude rule [flagged model] + SODIS 6 h/2-day cloud + solar-still yield + rolling-boil guidance.
- P19 promotion decision: the method ladder's load-bearing recurrence test (FC1's ladder + UC IPM + WHO ladder + FC3's own).
- Chapter prose: six lectures (pathogen census; the method ladder; boiling + heat math at altitude; filtration + the charcoal pin; SODIS + the PET N1; solar stills + distillation + storage/re-contamination), Labs FC3.1/FC3.2, seven exercises (every worked figure battery-derived; one ◆ withheld to review), 8-row safety, canon coverage, flags, Chapter Ledger; canvas + manuscript push byte-verified; map FC3 planned -> drafted; row 115 close; scratch deleted.
