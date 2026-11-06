#!/usr/bin/env python3
"""Session 203 close recipe — fails rather than writes.
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

P = load("PROJECT.md", 743622, "22af1142e22b234918cf1c5279ae59f1", "PROJECT.md")
K = load("KNOWLEDGE.md", 701209, "7976c6708abf7173e0a9919457ae57fd", "KNOWLEDGE.md")
R = load("repair/row203.txt", 4668, "d376d20f0ebc1571b2ebd48cdec42c76", "row203")
X = load("repair/x203.txt", 1625, "aa8b57a7d5d9fcef3bc4247536da9367", "x203")
Q = load("repair/queue204.txt", 290, "9bba5e5d4ea44eab185ee2add82ec89e", "queue204")
PP = load("repair/p203.txt", 1570, "63345a9aee1bf2fd2dd138ae26f63338", "p203")

# --- PROJECT transforms (line-based, startswith semantics) ---
out, n_row, n_x, n_q, n_map = [], 0, 0, 0, 0
for line in P.split("\n"):
    if line.startswith("| 202 |"):
        out.append(line); out.append(R); n_row += 1
    elif line.startswith("- [x] NEXT UNIT (session 202"):
        out.append(line); out.append(X); n_x += 1
    elif line.startswith("- [ ] NEXT UNIT") and "session 203" in line:
        out.append(Q); n_q += 1
    elif line.startswith("56. The Exotic"):
        if "`drafted`" not in line: fail("map line lacks `drafted`")
        out.append(line.replace("`drafted`", "`reviewed`", 1)); n_map += 1
    else:
        out.append(line)
if (n_row, n_x, n_q, n_map) != (1, 1, 1, 1):
    fail("transform counts %r" % ((n_row, n_x, n_q, n_map),))
POUT = "\n".join(out)
if POUT.count("session 204") != 3: fail("session 204 census")
if POUT.count("Session 203 (") != 0: fail("Session 203 ( in PROJECT")

# --- KNOWLEDGE transform (line 10 append) ---
kl = K.split("\n")
kl[9] = kl[9] + " " + PP
KOUT = "\n".join(kl)
if KOUT.count("Session 203 (") != 1: fail("Session 203 ( in KNOWLEDGE")

# --- output gates (the awk-sim receipts) ---
for name, data, size, want in (
    ("PROJECT out", POUT, 749850, "008c97e8bad2c6053a5bac91babb979d"),
    ("KNOWLEDGE out", KOUT, 702780, "40f03f93a3d17daf8b22a3d87a925727"),
):
    b = data.encode("utf-8")
    if len(b) != size or md5(b) != want:
        fail(name + " (size %d, md5 %s)" % (len(b), md5(b)))

with open("PROJECT.md", "w", encoding="utf-8", newline="\n") as f: f.write(POUT)
with open("KNOWLEDGE.md", "w", encoding="utf-8", newline="\n") as f: f.write(KOUT)
print("Session 203 close applied: row/x/queue/map/KNOWLEDGE, all gates PASS")
