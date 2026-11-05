#!/usr/bin/env python3
# repair/recipe.py — the session-199 close recipe (the proven 191-198 in-repo Actions route).
# Every gate byte/md5-exact; FAILS RATHER THAN WRITES on any miss.
import hashlib, sys

def md5(b): return hashlib.md5(b).hexdigest()
def die(m): print("RECIPE-FAIL: " + m); sys.exit(1)

P = open("PROJECT.md", "rb").read()
K = open("KNOWLEDGE.md", "rb").read()
row = open("repair/row199.txt", "rb").read()
x   = open("repair/x199.txt", "rb").read()
q   = open("repair/queue200.txt", "rb").read()
p   = open("repair/p199.txt", "rb").read()

# ---- input gates
if len(P) != 703451 or md5(P) != "f54d927d2260fbb18f8c6e51c9d49996": die("PROJECT.md input gate (703451 B / f54d927d expected)")
if len(K) != 693596 or md5(K) != "d838a1093f1c0aa3f983eb971c0634ad": die("KNOWLEDGE.md input gate (693596 B / d838a109 expected)")
if len(row) != 7839: die("row199.txt size gate (7839 expected)")
if len(x) != 1562: die("x199.txt size gate (1562 expected)")
if len(q) != 609: die("queue200.txt size gate (609 expected)")
if len(p) != 1598: die("p199.txt size gate (1598 expected)")
for nm, s in [("row199", row), ("x199", x), ("queue200", q)]:
    if b"Session 199 (" in s: die("'Session 199 (' in " + nm)
    if b"\n" in s: die("newline in " + nm)
if b"\n" in p: die("newline in p199")
if p.count(b"**Session 199 (2026-11-05):") != 1 or p.count(b"Session 199 (") != 1: die("p199 anchors")
if not p.endswith(b"or whatever the user calls instead.**"): die("p199 tail anchor")
if row.count(b"session 200") != 2: die("row199 'session 200' count (2 expected)")
if q.count(b"session 200") != 1: die("queue200 'session 200' count (1 expected)")

Pt = P.decode("utf-8"); Kt = K.decode("utf-8")
rowt = row.decode("utf-8"); xt = x.decode("utf-8"); qt = q.decode("utf-8"); pt = p.decode("utf-8")

# ---- pre-state gates
if Pt.count("| 199 |") != 0: die("row 199 already present")
if Pt.count("| 198 |") != 1: die("row-198 anchor (exactly 1 expected)")
if Pt.count("- [x] NEXT UNIT (session 198") != 1: die("x-198 anchor")
if Pt.count("- [ ] NEXT UNIT") != 3: die("queue-line count (3 expected)")
if Pt.count("session 199") != 3: die("PROJECT 'session 199' pre-count (3 expected)")
if Pt.count("session 200") != 0: die("PROJECT 'session 200' pre-count (0 expected)")
if "Session 199 (" in Pt: die("'Session 199 (' in PROJECT pre-state")
F = "or whatever the user calls instead.**"
J = F + "\n\n## Routing"
if Kt.count(J) != 1: die("KNOWLEDGE junction (exactly 1 expected)")
if Kt.count("Session 199 (") != 0: die("'Session 199 (' in KNOWLEDGE pre-state")
if Kt.count("Session 198 (") != 1: die("'Session 198 (' pre-count (1 expected)")
if Kt.count("session 200") != 0: die("KNOWLEDGE 'session 200' pre-count (0 expected)")

# ---- PROJECT edits
lines = Pt.split("\n")
trailing = lines[-1] == ""
if trailing: lines.pop()
res = []
queue_done = row_done = x_done = map_done = False
for l in lines:
    if l.startswith("- [ ] NEXT UNIT") and "session 199" in l:
        res.append(qt); queue_done = True; continue
    if l.startswith("| 198 |"):
        res.append(l); res.append(rowt); row_done = True; continue
    if l.startswith("- [x] NEXT UNIT (session 198"):
        res.append(l); res.append(xt); x_done = True; continue
    if l.startswith("54. ") and "The Product Deconstructions" in l and "`planned`" in l:
        if l.count("`planned`") != 1: die("map-line 'planned' count (1 expected)")
        l = l.replace("`planned`", "`drafted`")
        if "`planned`" in l or "`drafted`" not in l: die("map-line flip failed")
        map_done = True
    res.append(l)
for ok, nm in [(queue_done, "queue replace"), (row_done, "row insert"), (x_done, "x insert"), (map_done, "map flip")]:
    if not ok: die("edit not fired: " + nm)
P2 = "\n".join(res) + ("\n" if trailing else "")

# ---- PROJECT post gates
if P2.count("| 199 |") != 1: die("post: row 199 count")
if P2.count("| 198 |") != 1: die("post: row 198 count")
if P2.count("- [x] NEXT UNIT (session 199") != 1: die("post: x-199 count")
if P2.count("- [x] NEXT UNIT (session 198") != 1: die("post: x-198 count")
if P2.count("- [ ] NEXT UNIT") != 3: die("post: queue-line count (3 expected)")
if P2.count("session 200") != 3: die("post: 'session 200' count (3 expected)")
if "Session 199 (" in P2: die("post: 'Session 199 (' in PROJECT")

# ---- KNOWLEDGE edit
K2 = Kt.replace(J, F + " " + pt + "\n\n## Routing", 1)
# ---- KNOWLEDGE post gates
if K2.count("Session 199 (") != 1: die("post: 'Session 199 (' count")
if K2.count("**Session 199 (2026-11-05):") != 1: die("post: p199 start marker")
if K2.count("Session 198 (") != 1: die("post: 'Session 198 (' count")
if K2.count(J) != 1: die("post: junction rebuilt (1 expected)")
if K2.count("session 200") != 1: die("post: 'session 200' count (1 expected)")

# ---- final gates (from the frozen awk simulation) — then write
P2b = P2.encode("utf-8"); K2b = K2.encode("utf-8")
if len(P2b) != 712869 or md5(P2b) != "1e621331405e240148ab5dea190ff97b": die("PROJECT final gate (712869 B / 1e621331 expected)")
if len(K2b) != 695195 or md5(K2b) != "7645b8541ed5b4c513c21b43a7125cb5": die("KNOWLEDGE final gate (695195 B / 7645b854 expected)")
open("PROJECT.md", "wb").write(P2b)
open("KNOWLEDGE.md", "wb").write(K2b)
print("RECIPE-OK session-199 close: PROJECT.md 712869 B (md5 1e621331) + KNOWLEDGE.md 695195 B (md5 7645b854) written")
