# Engine 67 — the frozen transcripts (session 173)

*All six transcripts, spliced verbatim from the session's saved runs (the e67 scratch). The rev-1 runs are preserved per the honest-history rule: the frozen battery in the chapter master is rev-2 + s5, and the rev-1 failures with their named repairs are the record of how it got there. File md5s at splice time: s0 9655aa2b6582951ab550ba45e06f032b · s1s2(rev-1) 08b07ca4254442b62bed827c37a66cfd · s1s2(rev-2) ac816b403a4cf3ff199a5cb77502a412 · s3s4(rev-1) b0d922a44fc6bc0d3e6942a867818889 · s3s4(rev-2) ac5ba26a2c8db02f556b4ce54fedd71a · s5 332d68e7817a8a62e8f9559f7bd3da46. Digest convention: sdbm, charCode lane, unpadded hex, text without trailing newline.*

## s0 — the probe

```
E67 s0 probe (the CF convergent engine, session 173)
P1 got=32.046 detW:true rt:true frozen=32.046 detW:true rt:true | PASS
P2 got=214.492==214.492 exact:true frozen=214.492==214.492 exact:true | PASS
P3 got=0.2246 f:0.2246 frozen=0.2246 f:0.2246 | PASS
P4 got=21.2 f:21.2 frozen=21.2 f:21.2 | PASS
P5 got=74.43 frozen=74.44 | CAUGHT

```

## s1 + s2 — the molar book and the balances (rev-1)

```
E67 s1 — Sheet 1: the molar book (held-22 basis; CF lane + det witness + float witness)
S1-01 N2H4 got=32.046 f:32.046 detW:true rt:true frozen=32.046 f:32.046 detW:true rt:true | PASS
S1-02 NH3 got=17.031 f:17.031 detW:true rt:true frozen=17.031 f:17.031 detW:true rt:true | PASS
S1-03 NH2Cl got=51.476 f:51.476 detW:true rt:true frozen=51.476 f:51.476 detW:true rt:true | PASS
S1-04 CH4N2O got=60.056 f:60.056 detW:true rt:true frozen=60.056 f:60.056 detW:true rt:true | PASS
S1-05 NaOCl got=74.44 f:74.44 detW:true rt:true frozen=74.44 f:74.44 detW:true rt:true | PASS
S1-06 NaOH got=39.997 f:39.997 detW:true rt:true frozen=39.997 f:39.997 detW:true rt:true | PASS
S1-07 NaCl got=58.443 f:58.443 detW:true rt:true frozen=58.443 f:58.443 detW:true rt:true | PASS
S1-08 Na2CO3 got=105.988 f:105.988 detW:true rt:true frozen=105.988 f:105.988 detW:true rt:true | PASS
S1-09 H2SO4 got=98.072 f:98.072 detW:true rt:true frozen=98.072 f:98.072 detW:true rt:true | PASS
S1-10 N2H6SO4 got=130.118 f:130.118 detW:true rt:true frozen=130.118 f:130.118 detW:true rt:true | PASS
S1-11 C4H8O got=72.107 f:72.107 detW:true rt:true frozen=72.107 f:72.107 detW:true rt:true | PASS
S1-12 C8H16N2 got=140.230 f:140.230 detW:true rt:true frozen=140.23 f:140.230 detW:true rt:true | FAIL
S1-13 K2CO3 got=138.204 f:138.204 detW:true rt:true frozen=138.204 f:138.204 detW:true rt:true | PASS
S1-14 CH3ClN2O got=94.501 f:94.501 detW:true rt:true frozen=94.501 f:94.501 detW:true rt:true | PASS
S1-15 KCl got=74.551 f:74.551 detW:true rt:true frozen=74.551 f:74.551 detW:true rt:true | PASS
S1-16 H2O got=18.015 f:18.015 detW:true rt:true frozen=18.015 f:18.015 detW:true rt:true | PASS
E67 s2 — Sheet 2: the balances (atom-multiset gate + exact mass equality)
B1 got=214.492==214.492 atoms:true exact:true frozen=214.492==214.492 atoms:true exact:true | PASS
B2 got=91.473==91.473 atoms:true exact:true frozen=91.473==91.473 atoms:true exact:true | PASS
B3 got=68.507==68.507 atoms:true exact:true frozen=68.507==68.507 atoms:true exact:true | PASS
B4 got=76.458==76.458 atoms:true exact:true frozen=76.458==76.458 atoms:true exact:true | PASS
B5 got=176.260==176.260 atoms:true exact:true frozen=176.260==176.260 atoms:true exact:true | PASS
B6 got=274.332==274.332 atoms:true exact:true frozen=386.875==386.875 atoms:true exact:true | FAIL

```

## s1 + s2 — rev-2 (the frozen battery)

```
E67 s1 rev-2 — Sheet 1: the molar book (S1-12 frozen repaired: the trailing zero, a dispatch slip)
E67 s2 rev-2 — Sheet 2: the balances (B6 frozen repaired: the true balanced mass 274.332, a hand-sum slip)
S1-01 N2H4 got=32.046 f:32.046 detW:true rt:true frozen=32.046 f:32.046 detW:true rt:true | PASS
S1-02 NH3 got=17.031 f:17.031 detW:true rt:true frozen=17.031 f:17.031 detW:true rt:true | PASS
S1-03 NH2Cl got=51.476 f:51.476 detW:true rt:true frozen=51.476 f:51.476 detW:true rt:true | PASS
S1-04 CH4N2O got=60.056 f:60.056 detW:true rt:true frozen=60.056 f:60.056 detW:true rt:true | PASS
S1-05 NaOCl got=74.44 f:74.44 detW:true rt:true frozen=74.44 f:74.44 detW:true rt:true | PASS
S1-06 NaOH got=39.997 f:39.997 detW:true rt:true frozen=39.997 f:39.997 detW:true rt:true | PASS
S1-07 NaCl got=58.443 f:58.443 detW:true rt:true frozen=58.443 f:58.443 detW:true rt:true | PASS
S1-08 Na2CO3 got=105.988 f:105.988 detW:true rt:true frozen=105.988 f:105.988 detW:true rt:true | PASS
S1-09 H2SO4 got=98.072 f:98.072 detW:true rt:true frozen=98.072 f:98.072 detW:true rt:true | PASS
S1-10 N2H6SO4 got=130.118 f:130.118 detW:true rt:true frozen=130.118 f:130.118 detW:true rt:true | PASS
S1-11 C4H8O got=72.107 f:72.107 detW:true rt:true frozen=72.107 f:72.107 detW:true rt:true | PASS
S1-12 C8H16N2 got=140.230 f:140.230 detW:true rt:true frozen=140.230 f:140.230 detW:true rt:true | PASS
S1-13 K2CO3 got=138.204 f:138.204 detW:true rt:true frozen=138.204 f:138.204 detW:true rt:true | PASS
S1-14 CH3ClN2O got=94.501 f:94.501 detW:true rt:true frozen=94.501 f:94.501 detW:true rt:true | PASS
S1-15 KCl got=74.551 f:74.551 detW:true rt:true frozen=74.551 f:74.551 detW:true rt:true | PASS
S1-16 H2O got=18.015 f:18.015 detW:true rt:true frozen=18.015 f:18.015 detW:true rt:true | PASS
B1 got=214.492==214.492 atoms:true exact:true frozen=214.492==214.492 atoms:true exact:true | PASS
B2 got=91.473==91.473 atoms:true exact:true frozen=91.473==91.473 atoms:true exact:true | PASS
B3 got=68.507==68.507 atoms:true exact:true frozen=68.507==68.507 atoms:true exact:true | PASS
B4 got=76.458==76.458 atoms:true exact:true frozen=76.458==76.458 atoms:true exact:true | PASS
B5 got=176.260==176.260 atoms:true exact:true frozen=176.260==176.260 atoms:true exact:true | PASS
B6 got=274.332==274.332 atoms:true exact:true frozen=274.332==274.332 atoms:true exact:true | PASS

```

## s3 + s4 — the lineage ledgers and the injection battery (rev-1)

```
E67 s3 — Sheet 3: the lineage ledgers (exact chain, printed once; the float witness an independent path from the original charges)
L01 got=0.5273 f:0.5273 frozen=0.5273 f:0.5273 | PASS
L02 got=1.3251 f:1.3251 frozen=1.3251 f:1.3251 | PASS
L03 got=0.6494 f:0.6494 frozen=0.6494 f:0.6494 | PASS
L04 got=1.0679 f:1.0679 frozen=1.0679 f:1.0679 | PASS
L05 got=76.04 f:76.04 frozen=76.04 f:76.04 | PASS
L06 got=1.0127 f:1.0127 frozen=1.0126 f:1.0126 | FAIL
L07 got=68.61 f:68.61 frozen=68.61 f:68.61 | PASS
L08 got=0.2246 f:0.2246 frozen=0.2246 f:0.2246 | PASS
L09 got=42.60 f:42.60 frozen=42.60 f:42.60 | PASS
L10 got=34.59 f:34.59 frozen=34.59 f:34.59 | PASS
L11 got=30.81 f:30.81 frozen=30.81 f:30.81 | PASS
L12 got=55.88 f:55.88 frozen=55.88 f:55.88 | PASS
L13 got=-99.-63 f:36.56 frozen=36.55 f:36.55 | FAIL
L14 got=24.63 f:24.63 frozen=24.63 f:24.63 | PASS
L15 got=21.53 f:21.53 frozen=21.53 f:21.53 | PASS
L16 got=21226.7 f:21226.7 frozen=21226.7 f:21226.7 | PASS
L17 got=1.3099 f:1.3099 frozen=1.3099 f:1.3099 | PASS
L18 got=73.94 f:73.94 frozen=73.94 f:73.94 | PASS
L19 got=1.54 f:1.54 frozen=1.54 f:1.54 | PASS
E67 s4 — Sheet 4: the injection battery (all rows MUST be CAUGHT)
I01 got=74.33 frozen=74.44 | CAUGHT
I02 got=130.123 frozen=130.118 | CAUGHT
I03 got=34.59 frozen=42.60 | CAUGHT
I05 got=10.6 frozen=21.2 | CAUGHT
I06 got=51.373 frozen=51.476 | CAUGHT
I08 got=142.246 frozen=140.230 | CAUGHT

```

## s3 + s4 — rev-2 (the frozen battery)

```
E67 s3 rev-2 — Sheet 3: the lineage ledgers (L06 frozen repaired 1.0126 -> 1.0127, a hand slip; L13 exact chain repaired: the percent multiply misplaced, and the printK negative lane it exposed refused by design — D2)
E67 s4 rev-2 — Sheet 4: the injection battery, now EIGHT rows (I04/I07 omitted in rev-1, the harness slip named)
L01 got=0.5273 f:0.5273 frozen=0.5273 f:0.5273 | PASS
L02 got=1.3251 f:1.3251 frozen=1.3251 f:1.3251 | PASS
L03 got=0.6494 f:0.6494 frozen=0.6494 f:0.6494 | PASS
L04 got=1.0679 f:1.0679 frozen=1.0679 f:1.0679 | PASS
L05 got=76.04 f:76.04 frozen=76.04 f:76.04 | PASS
L06 got=1.0127 f:1.0127 frozen=1.0127 f:1.0127 | PASS
L07 got=68.61 f:68.61 frozen=68.61 f:68.61 | PASS
L08 got=0.2246 f:0.2246 frozen=0.2246 f:0.2246 | PASS
L09 got=42.60 f:42.60 frozen=42.60 f:42.60 | PASS
L10 got=34.59 f:34.59 frozen=34.59 f:34.59 | PASS
L11 got=30.81 f:30.81 frozen=30.81 f:30.81 | PASS
L12 got=55.88 f:55.88 frozen=55.88 f:55.88 | PASS
L13 got=36.56 f:36.56 frozen=36.56 f:36.56 | PASS
L14 got=24.63 f:24.63 frozen=24.63 f:24.63 | PASS
L15 got=21.53 f:21.53 frozen=21.53 f:21.53 | PASS
L16 got=21226.7 f:21226.7 frozen=21226.7 f:21226.7 | PASS
L17 got=1.3099 f:1.3099 frozen=1.3099 f:1.3099 | PASS
L18 got=73.94 f:73.94 frozen=73.94 f:73.94 | PASS
L19 got=1.54 f:1.54 frozen=1.54 f:1.54 | PASS
I01 got=74.33 frozen=74.44 | CAUGHT
I02 got=130.123 frozen=130.118 | CAUGHT
I03 got=34.59 frozen=42.60 | CAUGHT
I04 got=atoms:false frozen=atoms:true | CAUGHT
I05 got=10.6 frozen=21.2 | CAUGHT
I06 got=51.373 frozen=51.476 | CAUGHT
I07 got=atoms:false frozen=atoms:true | CAUGHT
I08 got=142.246 frozen=140.230 | CAUGHT

```

## s5 — determinism (the full 54-row battery built twice in-run)

```
E67 s5 — Sheet 5: determinism (the full 54-row battery built twice in-run)
rows=54 passOrCaught=54 byteIdentical=true sdbm1=c98d820d sdbm2=c98d820d
P1 got=32.046 detW:true rt:true frozen=32.046 detW:true rt:true | PASS
P2 got=214.492==214.492 exact:true frozen=214.492==214.492 exact:true | PASS
P3 got=0.2246 f:0.2246 frozen=0.2246 f:0.2246 | PASS
P4 got=21.2 f:21.2 frozen=21.2 f:21.2 | PASS
P5 got=74.43 frozen=74.44 | CAUGHT
S1-01 N2H4 got=32.046 f:32.046 detW:true rt:true frozen=32.046 f:32.046 detW:true rt:true | PASS
S1-02 NH3 got=17.031 f:17.031 detW:true rt:true frozen=17.031 f:17.031 detW:true rt:true | PASS
S1-03 NH2Cl got=51.476 f:51.476 detW:true rt:true frozen=51.476 f:51.476 detW:true rt:true | PASS
S1-04 CH4N2O got=60.056 f:60.056 detW:true rt:true frozen=60.056 f:60.056 detW:true rt:true | PASS
S1-05 NaOCl got=74.44 f:74.44 detW:true rt:true frozen=74.44 f:74.44 detW:true rt:true | PASS
S1-06 NaOH got=39.997 f:39.997 detW:true rt:true frozen=39.997 f:39.997 detW:true rt:true | PASS
S1-07 NaCl got=58.443 f:58.443 detW:true rt:true frozen=58.443 f:58.443 detW:true rt:true | PASS
S1-08 Na2CO3 got=105.988 f:105.988 detW:true rt:true frozen=105.988 f:105.988 detW:true rt:true | PASS
S1-09 H2SO4 got=98.072 f:98.072 detW:true rt:true frozen=98.072 f:98.072 detW:true rt:true | PASS
S1-10 N2H6SO4 got=130.118 f:130.118 detW:true rt:true frozen=130.118 f:130.118 detW:true rt:true | PASS
S1-11 C4H8O got=72.107 f:72.107 detW:true rt:true frozen=72.107 f:72.107 detW:true rt:true | PASS
S1-12 C8H16N2 got=140.230 f:140.230 detW:true rt:true frozen=140.230 f:140.230 detW:true rt:true | PASS
S1-13 K2CO3 got=138.204 f:138.204 detW:true rt:true frozen=138.204 f:138.204 detW:true rt:true | PASS
S1-14 CH3ClN2O got=94.501 f:94.501 detW:true rt:true frozen=94.501 f:94.501 detW:true rt:true | PASS
S1-15 KCl got=74.551 f:74.551 detW:true rt:true frozen=74.551 f:74.551 detW:true rt:true | PASS
S1-16 H2O got=18.015 f:18.015 detW:true rt:true frozen=18.015 f:18.015 detW:true rt:true | PASS
B1 got=214.492==214.492 atoms:true exact:true frozen=214.492==214.492 atoms:true exact:true | PASS
B2 got=91.473==91.473 atoms:true exact:true frozen=91.473==91.473 atoms:true exact:true | PASS
B3 got=68.507==68.507 atoms:true exact:true frozen=68.507==68.507 atoms:true exact:true | PASS
B4 got=76.458==76.458 atoms:true exact:true frozen=76.458==76.458 atoms:true exact:true | PASS
B5 got=176.260==176.260 atoms:true exact:true frozen=176.260==176.260 atoms:true exact:true | PASS
B6 got=274.332==274.332 atoms:true exact:true frozen=274.332==274.332 atoms:true exact:true | PASS
L01 got=0.5273 f:0.5273 frozen=0.5273 f:0.5273 | PASS
L02 got=1.3251 f:1.3251 frozen=1.3251 f:1.3251 | PASS
L03 got=0.6494 f:0.6494 frozen=0.6494 f:0.6494 | PASS
L04 got=1.0679 f:1.0679 frozen=1.0679 f:1.0679 | PASS
L05 got=76.04 f:76.04 frozen=76.04 f:76.04 | PASS
L06 got=1.0127 f:1.0127 frozen=1.0127 f:1.0127 | PASS
L07 got=68.61 f:68.61 frozen=68.61 f:68.61 | PASS
L08 got=0.2246 f:0.2246 frozen=0.2246 f:0.2246 | PASS
L09 got=42.60 f:42.60 frozen=42.60 f:42.60 | PASS
L10 got=34.59 f:34.59 frozen=34.59 f:34.59 | PASS
L11 got=30.81 f:30.81 frozen=30.81 f:30.81 | PASS
L12 got=55.88 f:55.88 frozen=55.88 f:55.88 | PASS
L13 got=36.56 f:36.56 frozen=36.56 f:36.56 | PASS
L14 got=24.63 f:24.63 frozen=24.63 f:24.63 | PASS
L15 got=21.53 f:21.53 frozen=21.53 f:21.53 | PASS
L16 got=21226.7 f:21226.7 frozen=21226.7 f:21226.7 | PASS
L17 got=1.3099 f:1.3099 frozen=1.3099 f:1.3099 | PASS
L18 got=73.94 f:73.94 frozen=73.94 f:73.94 | PASS
L19 got=1.54 f:1.54 frozen=1.54 f:1.54 | PASS
I01 got=74.33 frozen=74.44 | CAUGHT
I02 got=130.123 frozen=130.118 | CAUGHT
I03 got=34.59 frozen=42.60 | CAUGHT
I04 got=atoms:false frozen=atoms:true | CAUGHT
I05 got=10.6 frozen=21.2 | CAUGHT
I06 got=51.373 frozen=51.476 | CAUGHT
I07 got=atoms:false frozen=atoms:true | CAUGHT
I08 got=142.246 frozen=140.230 | CAUGHT

```
