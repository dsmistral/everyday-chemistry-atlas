#!/usr/bin/env python3
"""Session 204 close recipe — fails rather than writes.
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

P = load("PROJECT.md", 749850, "008c97e8bad2c6053a5bac91babb979d", "PROJECT.md")
K = load("KNOWLEDGE.md", 702780, "40f03f93a3d17daf8b22a3d87a925727", "KNOWLEDGE.md")
R = load("repair/row204.txt", 4178, "7d192fc9d4fb5c83adbae1fd3288b4fe", "row204")
X = load("repair/x204.txt", 1261, "c0f257c24defa6c0205ba93babf644d7", "x204")
Q = load("repair/queue205.txt", 229, "89f15fa5ac97ed32506264b7ef7e8c6c", "queue205")
PP = load("repair/p204.txt", 984, "c0f3c0eec503fe7cdb14acc0fd823df8", "p204")

# --- PROJECT transforms (line-based, startswith semantics) ---
out, n_row, n_x, n_q = [], 0, 0, 0
for line in P.split("\n"):
    if line.startswith("| 203 |"):
        out.append(line); out.append(R); n_row += 1
    elif line.startswith("- [x] NEXT UNIT (session 203"):
        out.append(line); out.append(X); n_x += 1
    elif line.startswith("- [ ] NEXT UNIT") and "session 204" in line:
        out.append(Q); n_q += 1
    else:
        out.append(line)
if (n_row, n_x, n_q) != (1, 1, 1):
    fail("transform counts %r" % ((n_row, n_x, n_q),))
POUT = "\n".join(out)
if POUT.count("session 205") != 3: fail("session 205 census")
if POUT.count("Session 204 (") != 0: fail("Session 204 ( in PROJECT")

# --- KNOWLEDGE transform (line 10 append) ---
kl = K.split("\n")
kl[9] = kl[9] + " " + PP
KOUT = "\n".join(kl)
if KOUT.count("Session 204 (") != 1: fail("Session 204 ( in KNOWLEDGE")

# --- output gates (the awk-sim receipts) ---
for name, data, size, want in (
    ("PROJECT out", POUT, 755230, "28ce06814955075d68e06922c4c5a35d"),
    ("KNOWLEDGE out", KOUT, 703765, "5f7773ed1cafe2c294fffec13cc42c28"),
):
    b = data.encode("utf-8")
    if len(b) != size or md5(b) != want:
        fail(name + " (size %d, md5 %s)" % (len(b), md5(b)))

with open("PROJECT.md", "w", encoding="utf-8", newline="\n") as f: f.write(POUT)
with open("KNOWLEDGE.md", "w", encoding="utf-8", newline="\n") as f: f.write(KOUT)
print("Session 204 close applied: row/x/queue/KNOWLEDGE, all gates PASS")
