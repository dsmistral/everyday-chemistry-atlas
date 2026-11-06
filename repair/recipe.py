#!/usr/bin/env python3
# Session 201 close recipe (Vol IX Ch 56 "The Exotic Metals Annex").
# Fails rather than writes: every gate must pass before PROJECT.md / KNOWLEDGE.md are touched.
import hashlib, sys

def md5(b):
    return hashlib.md5(b).hexdigest()

def gate(name, data, size, digest):
    if len(data) != size or md5(data) != digest:
        print("GATE FAILED: " + name)
        sys.exit(1)

def read(p):
    with open(p, "rb") as f:
        return f.read()

# --- input gates (the repo state this recipe is certified against) ---
P = read("PROJECT.md")
K = read("KNOWLEDGE.md")
gate("PROJECT.md input", P, 723206, "1db0dde23157c70bfb985383596659fa")
gate("KNOWLEDGE.md input", K, 698014, "a973b6bb7a1d4ae960fa1100e33e5473")
ROW = read("repair/row201.txt")
X = read("repair/x201.txt")
Q = read("repair/queue202.txt")
PAR = read("repair/p201.txt")
gate("row201 span", ROW, 9875, "f1c0d814a2af5d6aa6f515eb6ab1ecc4")
gate("x201 span", X, 1869, "b09065db5c11235320067325a323931e")
gate("queue202 span", Q, 434, "b5907365ab681ded2f2043d546308fda")
gate("p201 span", PAR, 1607, "5f972bfc7ddf3e3b9405298b2abbebf5")
for nm, sp in (("row201", ROW), ("x201", X), ("queue202", Q), ("p201", PAR)):
    if b"\n" in sp:
        print("GATE FAILED: " + nm + " not single-line")
        sys.exit(1)

# --- transforms (line-based, startswith semantics, each exactly once) ---
pl = P.decode("utf-8").split("\n")
i200 = [i for i, l in enumerate(pl) if l.startswith("| 200 |")]
imap = [i for i, l in enumerate(pl) if l.startswith("56. The Exotic Metals")]
iqueue = [i for i, l in enumerate(pl) if l.startswith("- [ ] NEXT UNIT") and "session 201" in l]
ix200 = [i for i, l in enumerate(pl) if l.startswith("- [x] NEXT UNIT (session 200")]
if len(i200) != 1 or len(imap) != 1 or len(iqueue) != 1 or len(ix200) != 1:
    print("GATE FAILED: anchor counts")
    sys.exit(1)
row = ROW.decode("utf-8")
x = X.decode("utf-8")
q = Q.decode("utf-8")
par = PAR.decode("utf-8")
mline = pl[imap[0]]
if "planned" not in mline:
    print("GATE FAILED: map line state")
    sys.exit(1)
pl[imap[0]] = mline.replace("planned", "drafted", 1)
pl[i200[0] + 1:i200[0] + 1] = [row]
ix200 = [i for i, l in enumerate(pl) if l.startswith("- [x] NEXT UNIT (session 200")]
iqueue = [i for i, l in enumerate(pl) if l.startswith("- [ ] NEXT UNIT") and "session 201" in l]
if len(ix200) != 1 or len(iqueue) != 1:
    print("GATE FAILED: anchor counts after insert")
    sys.exit(1)
pl[iqueue[0]] = q
pl[ix200[0] + 1:ix200[0] + 1] = [x]
newP = "\n".join(pl).encode("utf-8")
kl = K.decode("utf-8").split("\n")
kl[9] = kl[9] + " " + par
newK = "\n".join(kl).encode("utf-8")

# --- output gates (the sim-verified bytes) ---
gate("PROJECT.md output", newP, 734982, "4b9871aa7cbe395552c736ba8639efc1")
gate("KNOWLEDGE.md output", newK, 699622, "0d22df660a25413ebcd788c2ac4ca8d4")
t = newP.decode("utf-8")
if t.count("session 202") != 3:
    print("GATE FAILED: session 202 census")
    sys.exit(1)
if "Session 201 (" in t:
    print("GATE FAILED: open marker present")
    sys.exit(1)

with open("PROJECT.md", "wb") as f:
    f.write(newP)
with open("KNOWLEDGE.md", "wb") as f:
    f.write(newK)
print("Session 201 close applied: PROJECT.md and KNOWLEDGE.md updated.")
