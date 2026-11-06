#!/usr/bin/env python3
"""Session 202 close recipe — fails rather than writes.
Every input and output is byte/md5-gated; any mismatch exits non-zero
with nothing written. The transforms mirror the awk sim exactly."""
import hashlib, sys

def md5(b): return hashlib.md5(b).hexdigest()

def fail(msg):
    print("GATE FAIL: " + msg, file=sys.stderr)
    sys.exit(1)

def load(path, size, want, name):
    try:
        with open(path, "rb") as f: b = f.read()
    except OSError as e:
        fail(name + " unreadable: " + str(e))
    if len(b) != size or md5(b) != want:
        fail(name + " input gate (size %d, md5 %s)" % (len(b), md5(b)))
    return b.decode("utf-8")

P = load("PROJECT.md", 734982, "4b9871aa7cbe395552c736ba8639efc1", "PROJECT.md")
K = load("KNOWLEDGE.md", 699622, "0d22df660a25413ebcd788c2ac4ca8d4", "KNOWLEDGE.md")
R = load("repair/row202.txt", 7193, "9194b1d74a33ef17c73f24d2afb43750", "row202")
X = load("repair/x202.txt", 1520, "bd59996e80d0b85f122c9c56ce129e2b", "x202")
Q = load("repair/queue203.txt", 358, "5580129a8bf16f792cb159b0e6daa1f2", "queue203")
PP = load("repair/p202.txt", 1586, "61316ac5b16dc2586ba333fc58c08834", "p202")

# --- PROJECT transforms (line-based, startswith semantics) ---
out, n_row, n_x, n_q, n_map = [], 0, 0, 0, 0
for line in P.split("\n"):
    if line.startswith("| 201 |"):
        out.append(line); out.append(R); n_row += 1
    elif line.startswith("- [x] NEXT UNIT (session 201"):
        out.append(line); out.append(X); n_x += 1
    elif line.startswith("- [ ] NEXT UNIT") and "session 202" in line:
        out.append(Q); n_q += 1
    elif line.startswith("55. Cryogens"):
        if "`drafted`" not in line: fail("map line lacks `drafted`")
        out.append(line.replace("`drafted`", "`reviewed`", 1)); n_map += 1
    else:
        out.append(line)
if (n_row, n_x, n_q, n_map) != (1, 1, 1, 1):
    fail("transform counts %r" % ((n_row, n_x, n_q, n_map),))
POUT = "\n".join(out)
if POUT.count("session 203") != 3: fail("session 203 census")
if POUT.count("Session 202 (") != 0: fail("Session 202 ( in PROJECT")

# --- KNOWLEDGE transform (line 10 append) ---
kl = K.split("\n")
kl[9] = kl[9] + " " + PP
KOUT = "\n".join(kl)
if KOUT.count("Session 202 (") != 1: fail("Session 202 ( in KNOWLEDGE")

# --- output gates (the awk-sim receipts) ---
for name, data, size, want in (
    ("PROJECT out", POUT, 743622, "22af1142e22b234918cf1c5279ae59f1"),
    ("KNOWLEDGE out", KOUT, 701209, "7976c6708abf7173e0a9919457ae57fd"),
):
    b = data.encode("utf-8")
    if len(b) != size or md5(b) != want:
        fail(name + " (size %d, md5 %s)" % (len(b), md5(b)))

with open("PROJECT.md", "w", encoding="utf-8", newline="\n") as f: f.write(POUT)
with open("KNOWLEDGE.md", "w", encoding="utf-8", newline="\n") as f: f.write(KOUT)
print("Session 202 close applied: row/x/queue/map/KNOWLEDGE, all gates PASS")
