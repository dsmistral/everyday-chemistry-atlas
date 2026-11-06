#!/usr/bin/env python3
"""Session 206 close recipe — fails rather than writes.
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

P = load("PROJECT.md", 760645, "3ee434f3942498e22e33a57f21622a95", "PROJECT.md")
K = load("KNOWLEDGE.md", 704493, "0bd29c1df6a663f277252552ceeaef64", "KNOWLEDGE.md")
R = load("repair/row206.txt", 3146, "449c136d92a47c43961809bac74ae274", "row206")
X = load("repair/x206.txt", 1051, "0a3a1312f5c6c040bca35cee04a2fde0", "x206")
Q = load("repair/queue207.txt", 263, "f9ab61c2800f9d1c395c91258d512266", "queue207")
PP = load("repair/p206.txt", 1594, "5cc45c3ded999acdb6dfcc4d2aa091ae", "p206")

# --- PROJECT transforms (line-based, startswith semantics) ---
out, n_row, n_x, n_q, n_map = [], 0, 0, 0, 0
for line in P.split("\n"):
    if line.startswith("| 205 |"):
        out.append(line); out.append(R); n_row += 1
    elif line.startswith("- [x] NEXT UNIT (session 205"):
        out.append(line); out.append(X); n_x += 1
    elif line.startswith("- [ ] NEXT UNIT") and "session 206" in line:
        out.append(Q); n_q += 1
    elif line.startswith("53. Citric, Starch, and Vanillin"):
        n_map += 1
        if line.count("`drafted`") != 1:
            fail("map line drafted count != 1")
        out.append(line.replace("`drafted`", "`reviewed`"))
    else:
        out.append(line)
if (n_row, n_x, n_q, n_map) != (1, 1, 1, 1):
    fail("transform counts %r" % ((n_row, n_x, n_q, n_map),))
POUT = "\n".join(out)
if POUT.count("session 207") != 3: fail("session 207 census")
if POUT.count("Session 206 (") != 0: fail("Session 206 ( in PROJECT")

# --- KNOWLEDGE transform (line 10 append) ---
kl = K.split("\n")
kl[9] = kl[9] + " " + PP
KOUT = "\n".join(kl)
if KOUT.count("Session 206 (") != 1: fail("Session 206 ( in KNOWLEDGE")

# --- output gates (the awk-sim receipts) ---
for name, data, size, want in (
    ("PROJECT out", POUT, 764801, "3bca87b6ce72da6a471770bbc8c380a1"),
    ("KNOWLEDGE out", KOUT, 706088, "89c7c0149c85772bfd53fca0ec2fee78"),
):
    b = data.encode("utf-8")
    if len(b) != size or md5(b) != want:
        fail(name + " (size %d, md5 %s)" % (len(b), md5(b)))

with open("PROJECT.md", "w", encoding="utf-8", newline="\n") as f: f.write(POUT)
with open("KNOWLEDGE.md", "w", encoding="utf-8", newline="\n") as f: f.write(KOUT)
print("Session 206 close applied: row/x/queue/map-flip/KNOWLEDGE, all gates PASS")
