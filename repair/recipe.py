#!/usr/bin/env python3
"""Session 208 close recipe — fails rather than writes.
Every input and output is byte/md5-gated; any mismatch exits non-zero
with nothing written. The transforms mirror the awk sim exactly.
No map flip: the volume-close changes no chapter status."""
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

P = load("PROJECT.md", 769671, "75fde93a0dd00469793f7095373e3f1d", "PROJECT.md")
K = load("KNOWLEDGE.md", 708018, "d915efb696a0e804a9fb777033daef45", "KNOWLEDGE.md")
R = load("repair/row208.txt", 2665, "3225df6101b71815566fe99dbc4f5a5c", "row208")
X = load("repair/x208.txt", 1083, "3658669faa4fb903229d59805961bc78", "x208")
Q = load("repair/queue209.txt", 454, "0f6281614d55dcc0466261ae6cc4de59", "queue209")
PP = load("repair/p208.txt", 1649, "b5effba51636fc76e790df305ae38e94", "p208")

# --- PROJECT transforms (line-based, startswith semantics) ---
out, n_row, n_x, n_q = [], 0, 0, 0
for line in P.split("\n"):
    if line.startswith("| 207 |"):
        out.append(line); out.append(R); n_row += 1
    elif line.startswith("- [x] NEXT UNIT (session 207"):
        out.append(line); out.append(X); n_x += 1
    elif line.startswith("- [ ] NEXT UNIT") and "session 208" in line:
        out.append(Q); n_q += 1
    else:
        out.append(line)
if (n_row, n_x, n_q) != (1, 1, 1):
    fail("transform counts %r" % ((n_row, n_x, n_q),))
POUT = "\n".join(out)
if POUT.count("session 209") != 3: fail("session 209 census")
if POUT.count("Session 208 (") != 0: fail("Session 208 ( in PROJECT")

# --- KNOWLEDGE transform (line 10 append) ---
kl = K.split("\n")
kl[9] = kl[9] + " " + PP
KOUT = "\n".join(kl)
if KOUT.count("Session 208 (") != 1: fail("Session 208 ( in KNOWLEDGE")

# --- output gates (the awk-sim receipts) ---
for name, data, size, want in (
    ("PROJECT out", POUT, 773586, "176bddc4438f2ca607c9ab2e4ea360e6"),
    ("KNOWLEDGE out", KOUT, 709668, "1c4478d28eb2841321870e91deaa6d44"),
):
    b = data.encode("utf-8")
    if len(b) != size or md5(b) != want:
        fail(name + " (size %d, md5 %s)" % (len(b), md5(b)))

with open("PROJECT.md", "w", encoding="utf-8", newline="\n") as f: f.write(POUT)
with open("KNOWLEDGE.md", "w", encoding="utf-8", newline="\n") as f: f.write(KOUT)
print("Session 208 close applied: row/x/queue/KNOWLEDGE, all gates PASS")
