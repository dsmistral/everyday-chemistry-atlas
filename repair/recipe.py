#!/usr/bin/env python3
"""Session 205 close recipe — fails rather than writes.
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

P = load("PROJECT.md", 755230, "28ce06814955075d68e06922c4c5a35d", "PROJECT.md")
K = load("KNOWLEDGE.md", 703765, "5f7773ed1cafe2c294fffec13cc42c28", "KNOWLEDGE.md")
R = load("repair/row205.txt", 2807, "818fd02ff2152e1ad8b4818b37a05eb6", "row205")
X = load("repair/x205.txt", 805, "2fce307a8960f65b90fab974efd01ba6", "x205")
Q = load("repair/queue206.txt", 307, "6aa25524cab9d8350bebd147daef7085", "queue206")
PP = load("repair/p205.txt", 727, "2d2b4ff9e3930deb8d6c480805d6384d", "p205")
M = load("repair/map205.txt", 1722, "2cf7b9af26c2236ff707427f205fd11f", "map205")

# --- PROJECT transforms (line-based, startswith semantics) ---
out, n_row, n_x, n_q, n_map = [], 0, 0, 0, 0
for line in P.split("\n"):
    if line.startswith("| 204 |"):
        out.append(line); out.append(R); n_row += 1
    elif line.startswith("- [x] NEXT UNIT (session 204"):
        out.append(line); out.append(X); n_x += 1
    elif line.startswith("- [ ] NEXT UNIT") and "session 205" in line:
        out.append(Q); n_q += 1
    elif line.startswith("56. The Exotic"):
        out.append(line); out.append(M); n_map += 1
    else:
        out.append(line)
if (n_row, n_x, n_q, n_map) != (1, 1, 1, 1):
    fail("transform counts %r" % ((n_row, n_x, n_q, n_map),))
POUT = "\n".join(out)
if POUT.count("session 206") != 3: fail("session 206 census")
if POUT.count("Session 205 (") != 0: fail("Session 205 ( in PROJECT")

# --- KNOWLEDGE transform (line 10 append) ---
kl = K.split("\n")
kl[9] = kl[9] + " " + PP
KOUT = "\n".join(kl)
if KOUT.count("Session 205 (") != 1: fail("Session 205 ( in KNOWLEDGE")

# --- output gates (the awk-sim receipts) ---
for name, data, size, want in (
    ("PROJECT out", POUT, 760645, "3ee434f3942498e22e33a57f21622a95"),
    ("KNOWLEDGE out", KOUT, 704493, "0bd29c1df6a663f277252552ceeaef64"),
):
    b = data.encode("utf-8")
    if len(b) != size or md5(b) != want:
        fail(name + " (size %d, md5 %s)" % (len(b), md5(b)))

with open("PROJECT.md", "w", encoding="utf-8", newline="\n") as f: f.write(POUT)
with open("KNOWLEDGE.md", "w", encoding="utf-8", newline="\n") as f: f.write(KOUT)
print("Session 205 close applied: row/x/queue/map/KNOWLEDGE, all gates PASS")
