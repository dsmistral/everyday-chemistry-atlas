# ch47-engine70-transcripts.md — the seven E70 transcripts: the digest manifest and the settled values — the verbatim texts lost to the session-176 platform incident (disclosed, never laundered)

This file departs from the series convention, honestly. Every prior transcripts file carries the engine's sheets verbatim with their digest anchors. This one cannot: the platform's sandbox worker died mid-session ("worker generation 1 was lost") and the scratch layer holding Engine 70's seven transcript files — and the engine's 36,433-B source (md5 676c1555f7e85fb0fd6bacf2a57cd7a2) — was destroyed with it. What stands, and why it stands: before the incident the transcripts were regenerated in pure TypeScript from the saved source and verified byte-identical against all eight frozen digests, twice, and the battery was built twice byte-identically in-run. The digests below are therefore not claims but certificates of texts that existed and were proven. No transcript text is reconstructed here — a reconstruction would be re-authoring, not recovery, and this project does not launder loss.

## The digest manifest (each transcript = body + "\nj31 <hex>\n"; file md5s as saved before the loss)

| sheet | bytes | j31 (body) | file md5 |
|---|---|---|---|
| s0 probe (4 PASS + 1 CAUGHT) | 520 | c6c8cdf8 | 550955c08278bf3818438277d36c453b |
| s1 molar book (30/30) | 3,046 | cbd9f09d | 3d916b5dca950840f667a8f62691d00a |
| s2 balances (8/8) | 1,134 | 86e9f205 | 22a234bd184e97aea89e3e4baccca402 |
| s3 ledgers (33/33) | 3,498 | f0be5386 | 41265e8c978ca9c34559f435da0d155c |
| s4 injections (8/8 CAUGHT, 0 escaped) | 1,020 | a4067c3b | 97f3e123e84a80019c0c05781ae9b11d |
| sR literal settlement (12/12) | 1,482 | abd61781 | d3ab409d9c45371dc4a0446cc42547ac |
| s5 determinism (byte-identical twice) | 158 | f2febed2 | 22e25350b0a5812ed5363f003719608d |
| full battery | 10,621 | 73dff36 | — |

## The settled values the sheets carry (machine-verified, both print lanes and the float witness agreeing)

- s0: 4 PASS + 1 CAUGHT — the seeded must-fail refused at the probe.
- s1: the molar book re-derived, 30/30 — every row the master's Sheet 1 value on the held table plus the Ni/Sn/Br pins (Ni 58.693, Sn 118.710, Br 79.904) and Ch 34's capsaicin pin 305.418.
- s2: the lineage's eight balances, 8/8, atom-multiset-gated — B1 132163, B2 146190, B3 102181, B4 166224, B5 235040, B6 665622, B7 185179, B8 323433 mg/mol, each side element-identical.
- s3: the ledgers, 33/33 — the master's L01–L33 values re-derived on the microgram lattice, L11's ruled-out mis-basis printed by design, L21's 137.03% CONTAMINATED flag held.
- s4: eight fresh-keyed injections, 8/8 CAUGHT, zero escaped — the fresh-keyed broken-atom values: I03 atoms[R] C9 H16 N2 O2, mass 166224 vs 184239; I06 atoms[R] C8 H13 N1 O4, 185179 vs 187195; I08 atoms[R] C18 H29 N1 O5, 323433 vs 339432.
- sR: R01 0.6796; R02 1.9748 / 2.4673 / inflation 24.94% (= 36.458×100/146.190); R03 25.32% + paper-promise 1.5206 g + recovered fraction 32.88%; R04 0.6065 (direct 3dp 0.606; the register's 0.607 the named double-round); R05 7.2974 g / 137.03% CONTAMINATED; R06 water 10 − 7.2974 = 2.7026 g = 27.03%; R07 demand 0.302794 mol (one-shot; the termwise 6 × 0.050466 = 0.302796, the seam named, neither averaged), supply@31.45% 0.319521 mol → 1.055× (the register's 1.06 at 2dp), supply@20% 0.193099 mol → 0.638×; R08 10.7671 / 82.19% / the wrong-basis 73.58% refuted; R09 0.926 (= 25/27) and 92.86 (= 650/7); R10 4.00× / 56.0×; R11 10.00 / 40.00; R12 1.043 / 2.298 / 2.003.
- s5: the full battery built twice in-run, byte-identical, j31 73dff36 over the 10,621-byte battery both passes.

The lesson this file exists to carry, already promoted to the project's runtime log: a review engine's outputs are durable only once spliced into the records or pushed — scratch is not storage.
