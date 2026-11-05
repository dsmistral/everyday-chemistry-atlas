# Engine 69 — the source record (session 175)

*The first source record in the atlas to carry the actual engine code. Engines 67 and 68 lost their sources to session compactions — the E68 record closed with the promoted protocol lesson, and this session executed it: the source was written to scratch disk at build time, before the battery ran, and it survived. What follows is the E69-XR source verbatim (24,009 bytes, md5 433a602a9b19490a4cf73773f174c351 at splice time), unmodified except for this paragraph and the fence. The sR expectations in the file are the corrected rev-2 values — the file's own history: it was written with the five hand-frozen rev-1 expectations, the machine caught them at sR rev-1, and they were corrected to the machine's dual-lane values in place, which is the run history the transcripts record preserves.*

## The source (E69-XR, as run)

```ts
// ============================================================
// E69-XR — the exact-rational engine (session 175; Vol VII Ch 47 authoring)
// Fresh build: ZERO code shared with Engines 1-68.
// Lattice: charges in integer micrograms; molar masses in integer mg/mol
// on Chapter 3's held element table, plus this chapter's three convergent
// pins (Ni 58.693, Sn 118.710, Br 79.904 g/mol) and the aniline density
// pin 1.0217 g/mL.
// Every quantity is an exact rational [num, den]. The DS lane prints by
// long division, half-up decided at the (k+1)-th generated digit. The XR
// lane prints the reduced fraction (gcd-reduced, iterative Euclid). The
// FL lane recomputes in float64 from an independent decimal table and
// must agree at the printed granularity or the row FAILS.
// Balance gates: atom multisets (exact integer counts) + distributive
// mass sums, both sides, both must agree.
// Negative lanes REFUSED by design (E69-D1). Guards at 9.0e15 on every
// stored integer. Iterative only: no recursion, no BigInt, no eval.
// Digest: FNV-1a 32-bit (h=2166136261, h^=c, h=imul(h,16777619)).
// ============================================================

const E: Record<string, number> = {
  H: 1008, B: 10810, C: 12011, N: 14007, O: 15999, Na: 22990,
  Mg: 24305, Al: 26982, S: 32060, Cl: 35450, K: 39098, Ca: 40078,
  Fe: 55845, Cu: 63546,
  Ni: 58693, Sn: 118710, Br: 79904, // the chapter's convergent pins
};
const EF: Record<string, number> = {
  H: 1.008, B: 10.81, C: 12.011, N: 14.007, O: 15.999, Na: 22.990,
  Mg: 24.305, Al: 26.982, S: 32.06, Cl: 35.45, K: 39.098, Ca: 40.078,
  Fe: 55.845, Cu: 63.546,
  Ni: 58.693, Sn: 118.71, Br: 79.904,
};
const GUARD = 9.0e15;
const UGC = 1000000; // micrograms per gram

function gu(x: number, w: string): number {
  if (!isFinite(x) || Math.abs(x) > GUARD) throw new Error("GUARD " + w + " " + x);
  return x;
}
type Rat = [number, number];
function gcd(a: number, b: number): number {
  let x = Math.abs(a), y = Math.abs(b);
  while (y) { const t = x % y; x = y; y = t; }
  return x || 1;
}
function rred(n: number, d: number): Rat {
  gu(n, "rred-n"); gu(d, "rred-d");
  if (d === 0) throw new Error("ZERO-DEN");
  let s = 1; if (d < 0) { s = -1; d = -d; }
  n = n * s; const g = gcd(n, d);
  return [n / g, d / g];
}
function rmul(x: Rat, y: Rat): Rat { return rred(gu(x[0] * y[0], "rmul-n"), gu(x[1] * y[1], "rmul-d")); }
function rdiv(x: Rat, y: Rat): Rat { return rred(gu(x[0] * y[1], "rdiv-n"), gu(x[1] * y[0], "rdiv-d")); }

// ---- long-division half-up print lane (DS) ----
function xprint(x: Rat, k: number): string {
  const n = x[0], d = x[1];
  if (n < 0 || d <= 0) return "REFUSED"; // E69-D1
  let ip = Math.floor(n / d); let r = n - ip * d;
  let ds = "";
  for (let i = 0; i <= k; i++) {
    r *= 10;
    const dig = Math.floor(r / d);
    ds += String.fromCharCode(48 + dig);
    r -= dig * d;
  }
  if (ds.charCodeAt(k) >= 53) { // witness digit >= '5' -> half-up
    let fr = ds.slice(0, k); let j = k - 1; let carry = true;
    while (j >= 0 && carry) {
      const c = fr.charCodeAt(j);
      if (c === 57) { fr = fr.slice(0, j) + "0" + fr.slice(j + 1); j--; }
      else { fr = fr.slice(0, j) + String.fromCharCode(c + 1) + fr.slice(j + 1); carry = false; }
    }
    if (carry) ip += 1;
    ds = fr;
  } else { ds = ds.slice(0, k); }
  let out = String(ip);
  if (k > 0) out += "." + ds;
  return out;
}
// ---- float64 witness lane (FL) ----
function fprint(x: Rat, k: number): string {
  const scaled = (x[0] * Math.pow(10, k)) / x[1];
  const v = Math.floor(scaled + 0.5);
  const ip = Math.floor(v / Math.pow(10, k));
  const fr = String(v - ip * Math.pow(10, k));
  if (k === 0) return String(ip);
  return String(ip) + "." + (fr.length < k ? "0".repeat(k - fr.length) + fr : fr);
}

// ---- formula parser (segment stack; hydrate dots via split; iterative) ----
function parseSeg(seg: string): Record<string, number> {
  const st: Record<string, number>[] = [{}];
  let i = 0;
  while (i < seg.length) {
    const c = seg[i];
    if (c === "(") { st.push({}); i++; }
    else if (c === ")") {
      i++; let j = i, ds = "";
      while (j < seg.length && seg[j] >= "0" && seg[j] <= "9") { ds += seg[j]; j++; }
      const mult = ds === "" ? 1 : parseInt(ds, 10); i = j;
      const top = st.pop() as Record<string, number>;
      const cur = st[st.length - 1];
      for (const kk in top) cur[kk] = (cur[kk] || 0) + top[kk] * mult;
    } else if (c >= "A" && c <= "Z") {
      let sym = c; i++;
      if (i < seg.length && seg[i] >= "a" && seg[i] <= "z") { sym += seg[i]; i++; }
      let j = i, ds = "";
      while (j < seg.length && seg[j] >= "0" && seg[j] <= "9") { ds += seg[j]; j++; }
      const mult = ds === "" ? 1 : parseInt(ds, 10); i = j;
      const cur = st[st.length - 1];
      cur[sym] = (cur[sym] || 0) + mult;
    } else throw new Error("PARSE " + seg + " @" + i);
  }
  if (st.length !== 1) throw new Error("PARSE-OPEN " + seg);
  return st[0];
}
function atoms(f: string): Record<string, number> {
  const total: Record<string, number> = {};
  const parts = f.split(".");
  for (let p = 0; p < parts.length; p++) {
    let seg = parts[p]; let mult = 1;
    const m = /^([0-9]+)(.*)$/.exec(seg);
    if (m && m[1] !== "") { mult = parseInt(m[1], 10); seg = m[2]; }
    const one = parseSeg(seg);
    for (const kk in one) total[kk] = (total[kk] || 0) + one[kk] * mult;
  }
  return total;
}
function mass(f: string): number { // mg/mol
  const a = atoms(f); let m = 0;
  for (const kk in a) m = gu(m + gu(a[kk] * E[kk], "mass-el " + f), "mass " + f);
  return m;
}
function fmass(f: string): number { // float witness from the decimal table
  const a = atoms(f); let m = 0;
  for (const kk in a) m += a[kk] * EF[kk];
  return m;
}
function compStr(f: string): string {
  const a = atoms(f); const ks: string[] = [];
  for (const kk in a) ks.push(kk);
  return ks.map(kk => kk + a[kk]).join(" ");
}

// ---- FNV-1a ----
function fnv(s: string): string {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
  return (h >>> 0).toString(16);
}

// ============ SHEET BUILDERS ============

function molRow(id: string, name: string, f: string): string {
  const M = mass(f);
  const xr = rred(M, 1000); // g/mol
  const ds = xprint(xr, 3);
  const fl = fmass(f).toFixed(3);
  const ok = ds === fl ? "PASS" : "FAIL";
  return id + "  " + name + "  " + f + "  = " + compStr(f) + "  M = " + ds + " g/mol  xr " + xr[0] + "/" + xr[1] + "  fl " + fl + "  " + ok;
}

type Side = [string, number][];
function sideAtoms(s: Side): Record<string, number> {
  const t: Record<string, number> = {};
  for (const e of s) { const a = atoms(e[0]); for (const kk in a) t[kk] = (t[kk] || 0) + a[kk] * e[1]; }
  return t;
}
function sideMass(s: Side): number {
  let m = 0;
  for (const e of s) m = gu(m + gu(mass(e[0]) * e[1], "smass " + e[0]), "smass-sum");
  return m;
}
function balRow(id: string, lhs: Side, rhs: Side): string {
  const la = sideAtoms(lhs), ra = sideAtoms(rhs);
  const keys: string[] = [];
  for (const kk in la) keys.push(kk);
  for (const kk in ra) if (!(kk in la)) keys.push(kk);
  keys.sort();
  let atomsOk = true; let lcomp = "", rcomp = "";
  for (const kk of keys) {
    const l = la[kk] || 0, r = ra[kk] || 0;
    lcomp += kk + l + " "; rcomp += kk + r + " ";
    if (l !== r) atomsOk = false;
  }
  const lm = sideMass(lhs), rm = sideMass(rhs);
  const massOk = lm === rm;
  const verdict = atomsOk && massOk ? "PASS" : "BROKEN";
  return id + "  atoms[L] " + lcomp.trim() + "  atoms[R] " + rcomp.trim() + "  mass " + lm + " vs " + rm + " mg/mol  " + verdict;
}
function balEq(lhs: Side, rhs: Side): string {
  const j = (s: Side) => s.map(e => (e[1] === 1 ? "" : e[1] + " ") + e[0]).join(" + ");
  return j(lhs) + " -> " + j(rhs);
}

// ledger row kinds
function molRowL(id: string, desc: string, ug: number, f: string, k: number): string {
  const r = rred(ug, mass(f) * 1000);
  const ds = xprint(r, k), fl = fprint(r, k);
  return id + "  " + desc + "  n = " + ds + " mol  xr " + r[0] + "/" + r[1] + "  fl " + fl + "  " + (ds === fl ? "PASS" : "FAIL");
}
function eqRowL(id: string, desc: string, ugA: number, fA: string, ugB: number, fB: string, k: number): string {
  const r = rred(gu(ugA * mass(fB), "eq-n"), gu(ugB * mass(fA), "eq-d"));
  const ds = xprint(r, k), fl = fprint(r, k);
  return id + "  " + desc + "  eq = " + ds + "  xr " + r[0] + "/" + r[1] + "  fl " + fl + "  " + (ds === fl ? "PASS" : "FAIL");
}
function theoRowL(id: string, desc: string, ug: number, fCharge: string, fProd: string, k: number): string {
  const r = rred(gu(ug * mass(fProd), "theo-n"), gu(mass(fCharge) * UGC, "theo-d")); // grams
  const ds = xprint(r, k), fl = fprint(r, k);
  return id + "  " + desc + "  theo = " + ds + " g  xr " + r[0] + "/" + r[1] + "  fl " + fl + "  " + (ds === fl ? "PASS" : "FAIL");
}
function pctRowL(id: string, desc: string, numA: number, denA: number, k: number): string {
  const r = rred(gu(numA * 100, "pct-n"), gu(denA, "pct-d"));
  const ds = xprint(r, k), fl = fprint(r, k);
  const flag = r[0] / r[1] > 100 ? " CONTAMINATED(>100)" : "";
  return id + "  " + desc + "  pct = " + ds + "%" + flag + "  xr " + r[0] + "/" + r[1] + "  fl " + fl + "  " + (ds === fl ? "PASS" : "FAIL");
}
function ratRowL(id: string, desc: string, n: number, d: number, k: number): string {
  const r = rred(n, d);
  const ds = xprint(r, k), fl = fprint(r, k);
  return id + "  " + desc + "  = " + ds + "  xr " + r[0] + "/" + r[1] + "  fl " + fl + "  " + (ds === fl ? "PASS" : "FAIL");
}

// ============ THE SHEETS ============

function s0(): string {
  const L: string[] = [];
  L.push("E69-XR s0 probe — " + "fresh-build gates, seeded must-fail first in the order run");
  const p1 = xprint(rred(mass("NaCl"), 1000), 3);
  const p1f = fmass("NaCl").toFixed(3);
  L.push("P1  NaCl on the held table  M = " + p1 + " g/mol  fl " + p1f + "  " + (p1 === "58.440" && p1 === p1f ? "PASS" : "FAIL"));
  const p2 = xprint([5, 4], 1);
  const p2f = fprint([5, 4], 1);
  L.push("P2  half-up seam  5/4 at 1 dp  = " + p2 + "  fl " + p2f + "  " + (p2 === "1.3" && p2 === p2f ? "PASS" : "FAIL"));
  const p3 = xprint(rred(291000, mass("C3H6O") * 1000), 4);
  const p3f = fprint(rred(291000, mass("C3H6O") * 1000), 4);
  L.push("P3  trailing-zero seam  0.291 g C3H6O n at 4 dp  = " + p3 + "  fl " + p3f + "  " + (p3 === "0.0050" && p3 === p3f ? "PASS" : "FAIL"));
  const p4 = balRow("P4", [["C6H8N2", 1], ["C3H6O", 1]], [["C9H9N", 1], ["NH3", 1], ["H2O", 1]]);
  L.push(p4 + "  (Fischer gate)");
  const claim = 22990 + 35540; // transposed Cl pin 35.540 asserted
  const truth = mass("NaCl");
  L.push("P5  seeded fault  NaCl with Cl=35.540 asserted  M = " + claim + " vs machine " + truth + "  " + (claim !== truth ? "CAUGHT" : "ESCAPED"));
  const txt = L.join("\n");
  return txt + "\nfnv " + fnv(txt) + "\n";
}

function s1(): string {
  const L: string[] = [];
  L.push("E69-XR s1 — the molar book (held table + the chapter's three convergent pins Ni/Sn/Br)");
  const rows: [string, string, string][] = [
    ["S1-01", "sodium bicarbonate", "NaHCO3"],
    ["S1-02", "ornithine", "C5H12N2O2"],
    ["S1-03", "ornithine hydrochloride", "C5H13ClN2O2"],
    ["S1-04", "putrescine", "C4H12N2"],
    ["S1-05", "lysine", "C6H14N2O2"],
    ["S1-06", "lysine hydrochloride", "C6H15ClN2O2"],
    ["S1-07", "5-aminopentanenitrile", "C5H10N2"],
    ["S1-08", "N-bromosuccinimide", "C4H4BrNO2"],
    ["S1-09", "nickel chloride hexahydrate", "NiCl2.6H2O"],
    ["S1-10", "sodium borohydride", "NaBH4"],
    ["S1-11", "cadaverine", "C5H14N2"],
    ["S1-12", "aniline", "C6H7N"],
    ["S1-13", "sodium nitrite", "NaNO2"],
    ["S1-14", "benzenediazonium chloride", "C6H5N2Cl"],
    ["S1-15", "tin(II) chloride", "SnCl2"],
    ["S1-16", "tin(IV) chloride", "SnCl4"],
    ["S1-17", "phenylhydrazine", "C6H8N2"],
    ["S1-18", "phenylhydrazine hydrochloride", "C6H9N2Cl"],
    ["S1-19", "propionaldehyde", "C3H6O"],
    ["S1-20", "p-toluenesulfonic acid monohydrate", "C7H10O4S"],
    ["S1-21", "skatole", "C9H9N"],
    ["S1-22", "ammonia", "NH3"],
    ["S1-23", "vanillin", "C8H8O3"],
    ["S1-24", "hydroxylamine hydrochloride", "NH2OH.HCl"],
    ["S1-25", "sodium acetate (anhydrous)", "NaC2H3O2"],
    ["S1-26", "sodium acetate trihydrate", "NaC2H3O2.3H2O"],
    ["S1-27", "vanillin oxime", "C8H9NO3"],
    ["S1-28", "vanillylamine", "C8H11NO2"],
    ["S1-29", "8-methyl-6-nonenoic acid", "C10H18O2"],
    ["S1-30", "capsaicin", "C18H27NO3"],
  ];
  for (const r of rows) L.push(molRow(r[0], r[1], r[2]));
  const txt = L.join("\n");
  const passes = (txt.match(/PASS/g) || []).length;
  const fails = (txt.match(/FAIL/g) || []).length;
  return txt + "\nrows " + rows.length + "  pass " + passes + "  fail " + fails + "\nfnv " + fnv(txt) + "\n";
}

function s2(): string {
  const L: string[] = [];
  L.push("E69-XR s2 — the lineage's balances (atom-multiset + distributive mass gates)");
  const B: [string, Side, Side][] = [
    ["B1", [["C5H12N2O2", 1]], [["C4H12N2", 1], ["CO2", 1]]],
    ["B2", [["C6H14N2O2", 1]], [["C5H10N2", 1], ["CO2", 1], ["H2", 2]]],
    ["B3", [["C5H10N2", 1], ["H2", 2]], [["C5H14N2", 1]]],
    ["B4", [["C6H8N2", 1], ["C3H6O", 1]], [["C9H9N", 1], ["NH3", 1], ["H2O", 1]]],
    ["B5", [["C6H7N", 1], ["NaNO2", 1], ["HCl", 2]], [["C6H5N2Cl", 1], ["NaCl", 1], ["H2O", 2]]],
    ["B6", [["C6H5N2Cl", 1], ["SnCl2", 2], ["HCl", 4]], [["C6H9N2Cl", 1], ["SnCl4", 2]]],
    ["B7", [["C8H8O3", 1], ["NH3O", 1]], [["C8H9NO3", 1], ["H2O", 1]]],
    ["B8", [["C8H11NO2", 1], ["C10H18O2", 1]], [["C18H27NO3", 1], ["H2O", 1]]],
  ];
  for (const b of B) { L.push(balEq(b[1], b[2])); L.push(balRow(b[0], b[1], b[2])); }
  const txt = L.join("\n");
  const passes = (txt.match(/PASS/g) || []).length;
  const broken = (txt.match(/BROKEN/g) || []).length;
  return txt + "\nbalances " + B.length + "  pass " + passes + "  broken " + broken + "\nfnv " + fnv(txt) + "\n";
}

function s3(): string {
  const L: string[] = [];
  L.push("E69-XR s3 — the lineage ledgers (charges -> moles -> theoreticals -> yields; lattice: micrograms)");
  L.push(molRowL("L01", "ornithine.HCl charge 1.3 g", 1300000, "C5H13ClN2O2", 6));
  L.push(eqRowL("L02", "NaHCO3 0.9 g vs ornithine.HCl (the 'probably not even necessary' 1.39x)", 900000, "NaHCO3", 1300000, "C5H13ClN2O2", 3));
  L.push(theoRowL("L03", "putrescine theoretical from ornithine.HCl", 1300000, "C5H13ClN2O2", "C4H12N2", 4));
  L.push(molRowL("L04", "lysine.HCl charge 3.53 g", 3530000, "C6H15ClN2O2", 6));
  L.push(eqRowL("L05", "NBS 10.3 g vs lysine.HCl (stated 3.0 eq)", 10300000, "C4H4BrNO2", 3530000, "C6H15ClN2O2", 3));
  L.push(eqRowL("L06", "NiCl2.6H2O 22.9 g vs lysine.HCl (stated 5.0 eq)", 22900000, "NiCl2.6H2O", 3530000, "C6H15ClN2O2", 3));
  L.push(eqRowL("L07", "NaBH4 5.84 g vs lysine.HCl (stated 8.0 eq)", 5840000, "NaBH4", 3530000, "C6H15ClN2O2", 3));
  L.push(theoRowL("L08", "5-aminopentanenitrile theoretical from lysine.HCl", 3530000, "C6H15ClN2O2", "C5H10N2", 4));
  L.push(theoRowL("L09", "cadaverine theoretical, HCl-form charge basis (the stated '~2.0 g')", 3530000, "C6H15ClN2O2", "C5H14N2", 4));
  L.push(pctRowL("L10", "cadaverine yield 0.5 g vs the HCl-form theoretical (vs the paper's 77%)", 500000 * 182648, 3530000 * 102181, 2));
  L.push(theoRowL("L11", "RULED-OUT lane: cadaverine theoretical on the lysine free-base mis-basis", 3530000, "C6H14N2O2", "C5H14N2", 4));
  L.push(molRowL("L12", "phenylhydrazine charge 0.5 g", 500000, "C6H8N2", 6));
  L.push(eqRowL("L13", "propionaldehyde 0.291 g vs phenylhydrazine (the 'bit less than 10% excess')", 291000, "C3H6O", 500000, "C6H8N2", 4));
  L.push(eqRowL("L14", "p-TSA.H2O 0.761 g vs phenylhydrazine (the near-stoichiometric 'catalyst')", 761000, "C7H10O4S", 500000, "C6H8N2", 3));
  L.push(theoRowL("L15", "skatole theoretical from phenylhydrazine (the honest P12 zero)", 500000, "C6H8N2", "C9H9N", 4));
  const aniUg = 1021700 * 46 / 10; // 4.6 mL x 1.0217 g/mL, exact on the lattice
  L.push(molRowL("L16", "aniline 4.6 mL at the density pin 1.0217 g/mL", aniUg, "C6H7N", 6));
  L.push(eqRowL("L17", "NaNO2 procedure figure 3.63 g vs aniline (the charge-matched 1.04 eq)", 3630000, "NaNO2", aniUg, "C6H7N", 3));
  L.push(eqRowL("L18", "NaNO2 list figure 8 g vs aniline (the UNEXPLAINED list-vs-procedure discrepancy)", 8000000, "NaNO2", aniUg, "C6H7N", 3));
  L.push(eqRowL("L19", "tin metal 12 g vs aniline (the 2.00-eq reductant charge)", 12000000, "Sn", aniUg, "C6H7N", 3));
  L.push(theoRowL("L20", "phenylhydrazine.HCl theoretical from aniline", aniUg, "C6H7N", "C6H9N2Cl", 4));
  L.push(pctRowL("L21", "the stated 10 g product vs the theoretical (the register's first above-theoretical yield)", 10000000 * 93129, aniUg * 144602, 2));
  L.push(molRowL("L22", "vanillin charge 9.8 g", 9800000, "C8H8O3", 6));
  L.push(eqRowL("L23", "hydroxylamine.HCl 5 g vs vanillin (the 1.12-eq excess)", 5000000, "NH2OH.HCl", 9800000, "C8H8O3", 3));
  L.push(eqRowL("L24", "sodium acetate 10.55 g vs hydroxylamine.HCl (the 1.79-eq acid scavenger)", 10550000, "NaC2H3O2", 5000000, "NH2OH.HCl", 3));
  L.push(theoRowL("L25", "vanillin oxime theoretical from vanillin", 9800000, "C8H8O3", "C8H9NO3", 4));
  L.push(pctRowL("L26", "oxime yield 8.85 g vs theoretical (the stated 'about 82%')", 8850000 * 152149, 9800000 * 167164, 2));
  L.push(ratRowL("L27", "capsaicinoid scale check: 14 g dried peppers at the 1% literature verdict", 14000000, 100000000, 2));
  L.push(ratRowL("L28", "N260 yield vs the brand range's 4 g ceiling", 400000 * 100, 4000000, 2));
  L.push(ratRowL("L29", "N260 yield vs the brand range's 1 g floor", 400000 * 100, 1000000, 2));
  L.push(ratRowL("L30", "N261 vanillin wt% (1.5 g from 162 g vanilla sugar)", 1500000 * 100, 162000000, 3));
  L.push(ratRowL("L31", "N261 methanol recovery (325 of 350 mL)", 325000 * 100, 350000, 2));
  L.push(ratRowL("L32", "N254/N255 pair: solvent economy (1 L soak vs 250 mL Soxhlet)", 1000000, 250000, 2));
  L.push(ratRowL("L33", "N254/N255 pair: time economy (168 h soak vs 3 h Soxhlet)", 168, 3, 1));
  const txt = L.join("\n");
  const passes = (txt.match(/PASS/g) || []).length;
  const fails = (txt.match(/FAIL/g) || []).length;
  return txt + "\nrows " + (L.length - 1) + "  pass " + passes + "  fail " + fails + "\nfnv " + fnv(txt) + "\n";
}

function s4(): string {
  const L: string[] = [];
  L.push("E69-XR s4 — fresh-keyed injections (each must be CAUGHT; keyed to this chapter's own seams)");
  const aniUg = 1021700 * 46 / 10;
  // I01 transposed charge
  const m1 = xprint(rred(3100000, mass("C5H13ClN2O2") * 1000), 6);
  L.push("I01  claim: ornithine.HCl 3.1 g (transposed) still gives n = 0.007710 mol  machine: n(3.1 g) = " + m1 + "  " + (m1 !== "0.007710" ? "CAUGHT" : "ESCAPED"));
  // I02 free-base mis-basis asserted
  const m2 = xprint(rred(gu(3530000 * mass("C5H14N2")), gu(mass("C6H15ClN2O2") * UGC)), 4);
  L.push("I02  claim: cadaverine theoretical = 2.4673 g (the lysine free-base mis-basis)  machine: HCl-form theoretical = " + m2 + " g  " + (m2 !== "2.4673" ? "CAUGHT" : "ESCAPED"));
  // I03 Fischer with NH3 dropped
  const a3 = balRow("I03", [["C6H8N2", 1], ["C3H6O", 1]], [["C9H9N", 1], ["H2O", 1]]);
  L.push(a3 + "  " + (a3.indexOf("BROKEN") >= 0 ? "CAUGHT" : "ESCAPED"));
  // I04 NaNO2 list figure asserted charge-matched
  const m4 = xprint(rred(gu(8000000 * mass("C6H7N")), gu(aniUg * mass("NaNO2"))), 3);
  L.push("I04  claim: the 8 g list figure is the 1.04-eq charge  machine: 8 g = " + m4 + " eq  " + (m4 !== "1.043" ? "CAUGHT" : "ESCAPED"));
  // I05 the 137% asserted clean
  const p5 = rred(10000000 * 93129 * 100, aniUg * 144602);
  const v5 = p5[0] / p5[1] > 100;
  L.push("I05  claim: the 137.01% phenylhydrazine.HCl yield is a clean yield  machine: pct > 100 -> CONTAMINATED  " + (v5 ? "CAUGHT" : "ESCAPED"));
  // I06 oxime balance with H2O dropped
  const a6 = balRow("I06", [["C8H8O3", 1], ["NH3O", 1]], [["C8H9NO3", 1]]);
  L.push(a6 + "  " + (a6.indexOf("BROKEN") >= 0 ? "CAUGHT" : "ESCAPED"));
  // I07 hydroxylamine-basis yield asserted
  const m7 = xprint(rred(gu(8850000 * mass("NH2OH.HCl") * 100), gu(5000000 * mass("C8H9NO3"))), 2);
  L.push("I07  claim: the oxime yield is " + m7 + "% on the hydroxylamine.HCl basis  machine: vanillin is limiting; the vanillin-basis yield = 82.19%  " + (m7 !== "82.19" ? "CAUGHT" : "ESCAPED"));
  // I08 capsaicin coupling uncondensed
  const a8 = balRow("I08", [["C8H11NO2", 1], ["C10H18O2", 1]], [["C18H27NO4", 1]]);
  L.push(a8 + "  " + (a8.indexOf("BROKEN") >= 0 ? "CAUGHT" : "ESCAPED"));
  const txt = L.join("\n");
  const caught = (txt.match(/CAUGHT/g) || []).length;
  const escaped = (txt.match(/ESCAPED/g) || []).length;
  return txt + "\ninjections 8  caught " + caught + "  escaped " + escaped + "\nfnv " + fnv(txt) + "\n";
}

function sR(): string {
  const L: string[] = [];
  L.push("E69-XR sR — the literal-settlement sheet (the chapter's printed literals, machine-settled)");
  const aniUg = 1021700 * 46 / 10;
  const r1 = xprint(rred(gu(1300000 * mass("C4H12N2")), gu(mass("C5H13ClN2O2") * UGC)), 4);
  L.push("R01  putrescine theoretical  expect 0.6796 g  machine " + r1 + "  " + (r1 === "0.6796" ? "PASS" : "MISMATCH"));
  const r2 = xprint(rred(gu(3530000 * mass("C5H14N2")), gu(mass("C6H15ClN2O2") * UGC)), 4);
  L.push("R02  cadaverine theoretical (HCl-form basis)  expect 1.9748 g  machine " + r2 + "  " + (r2 === "1.9748" ? "PASS" : "MISMATCH"));
  const r3 = xprint(rred(500000 * 182648 * 100, 3530000 * 102181), 2);
  L.push("R03  cadaverine yield  expect 25.32%  machine " + r3 + "  " + (r3 === "25.32" ? "PASS" : "MISMATCH"));
  const r4 = xprint(rred(gu(500000 * mass("C9H9N")), gu(mass("C6H8N2") * UGC)), 4);
  L.push("R04  skatole theoretical  expect 0.6065 g (the register's 0.607 named as the double-round)  machine " + r4 + "  " + (r4 === "0.6065" ? "PASS" : "MISMATCH"));
  const r5 = xprint(rred(gu(aniUg * mass("C6H9N2Cl")), gu(mass("C6H7N") * UGC)), 4);
  L.push("R05  phenylhydrazine.HCl theoretical  expect 7.2974 g  machine " + r5 + "  " + (r5 === "7.2974" ? "PASS" : "MISMATCH"));
  const r6 = xprint(rred(10000000 * 93129 * 100, aniUg * 144602), 2);
  L.push("R06  the stated 10 g as percent  expect 137.03%  machine " + r6 + "  " + (r6 === "137.03" ? "PASS" : "MISMATCH"));
  const r7 = xprint(rred(gu(9800000 * mass("C8H9NO3")), gu(mass("C8H8O3") * UGC)), 4);
  L.push("R07  vanillin oxime theoretical  expect 10.7671 g  machine " + r7 + "  " + (r7 === "10.7671" ? "PASS" : "MISMATCH"));
  const r8 = xprint(rred(8850000 * 152149 * 100, 9800000 * 167164), 2);
  L.push("R08  oxime yield  expect 82.19%  machine " + r8 + "  " + (r8 === "82.19" ? "PASS" : "MISMATCH"));
  const r9 = xprint(rred(1500000 * 100, 162000000), 3);
  L.push("R09  N261 vanillin wt%  expect 0.926  machine " + r9 + "  " + (r9 === "0.926" ? "PASS" : "MISMATCH"));
  const r10 = xprint(rred(325000 * 100, 350000), 2);
  L.push("R10  N261 methanol recovery  expect 92.86%  machine " + r10 + "  " + (r10 === "92.86" ? "PASS" : "MISMATCH"));
  const txt = L.join("\n");
  const passes = (txt.match(/PASS/g) || []).length;
  const mm = (txt.match(/MISMATCH/g) || []).length;
  return txt + "\nrows 10  pass " + passes + "  mismatch " + mm + "\nfnv " + fnv(txt) + "\n";
}

function battery(): string {
  return [s0(), s1(), s2(), s3(), s4(), sR()].join("\n");
}

async function main() {
  const t0 = s0(), t1 = s1(), t2 = s2(), t3 = s3(), t4 = s4(), tR = sR();
  // s5: determinism — the full battery built twice, byte-compared
  const b1 = battery();
  const b2 = battery();
  const ident = b1 === b2;
  const s5 = "E69-XR s5 — determinism: full battery built twice in-run\nbyte-identical " + ident + "\nfnv-pass1 " + fnv(b1) + "\nfnv-pass2 " + fnv(b2) + "\nbattery bytes " + b1.length + " and " + b2.length + "\n";
  return {
    s0: t0, s1: t1, s2: t2, s3: t3, s4: t4, sR: tR, s5: s5,
    digests: { s0: fnv(t0), s1: fnv(t1), s2: fnv(t2), s3: fnv(t3), s4: fnv(t4), sR: fnv(tR), battery: fnv(b1) },
  };
}
```
