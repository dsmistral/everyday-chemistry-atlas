#!/usr/bin/env python3
"""Session 207 close recipe — fails rather than writes.
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

P = load("PROJECT.md", 764801, "3bca87b6ce72da6a471770bbc8c380a1", "PROJECT.md")
K = load("KNOWLEDGE.md", 706088, "89c7c0149c85772bfd53fca0ec2fee78", "KNOWLEDGE.md")
R = load("repair/row207.txt", 3699, "4accbe887e6b0585f72fd2179f8c17a6", "row207")
X = load("repair/x207.txt", 1142, "f925f9e2630aab06c3928347d44b12fe", "x207")
Q = load("repair/queue208.txt", 289, "6bb62e56386c9ad9e460962a248ca87b", "queue208")
PP = load("repair/p207.txt", 1929, "775a893c1eb270778f488aecb4879e08", "p207")

# --- PROJECT transforms (line-based, startswith semantics) ---
out, n_row, n_x, n_q, n_map = [], 0, 0, 0, 0
for line in P.split("\n"):
    if line.startswith("| 206 |"):
        out.append(line); out.append(R); n_row += 1
    elif line.startswith("- [x] NEXT UNIT (session 206"):
        out.append(line); out.append(X); n_x += 1
    elif line.startswith("- [ ] NEXT UNIT") and "session 207" in line:
        out.append(Q); n_q += 1
    elif line.startswith("54. The Product Deconstructions"):
        n_map += 1
        if line.count("`drafted`") != 1:
            fail("map line drafted count != 1")
        out.append(line.replace("`drafted`", "`reviewed`"))
    else:
        out.append(line)
if (n_row, n_x, n_q, n_map) != (1, 1, 1, 1):
    fail("transform counts %r" % ((n_row, n_x, n_q, n_map),))
POUT = "\n".join(out)
if POUT.count("session 208") != 3: fail("session 208 census")
if POUT.count("Session 207 (") != 0: fail("Session 207 ( in PROJECT")

# --- KNOWLEDGE transform (line 10 append) ---
kl = K.split("\n")
kl[9] = kl[9] + " " + PP
KOUT = "\n".join(kl)
if KOUT.count("Session 207 (") != 1: fail("Session 207 ( in KNOWLEDGE")

# --- output gates (the awk-sim receipts) ---
for name, data, size, want in (
    ("PROJECT out", POUT, 769671, "75fde93a0dd00469793f7095373e3f1d"),
    ("KNOWLEDGE out", KOUT, 708018, "d915efb696a0e804a9fb777033daef45"),
):
    b = data.encode("utf-8")
    if len(b) != size or md5(b) != want:
        fail(name + " (size %d, md5 %s)" % (len(b), md5(b)))

with open("PROJECT.md", "w", encoding="utf-8", newline="\n") as f: f.write(POUT)
with open("KNOWLEDGE.md", "w", encoding="utf-8", newline="\n") as f: f.write(KOUT)
print("Session 207 close applied: row/x/queue/map-flip/KNOWLEDGE, all gates PASS")
