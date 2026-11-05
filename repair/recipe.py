import hashlib

def md5b(b): return hashlib.md5(b).hexdigest()
def rd(p):
    with open(p, 'rb') as f: return f.read()
def die(msg):
    print('RECIPE FAIL: ' + msg)
    raise SystemExit(1)

F = 'or whatever the user calls instead.**'

# ---- spans ----
row198 = rd('repair/row198.txt').decode('utf-8')
x198 = rd('repair/x198.txt').decode('utf-8')
queue199 = rd('repair/queue199.txt').decode('utf-8')
p198 = rd('repair/p198.txt').decode('utf-8')
for name, s, want in (('row198', row198, 5016), ('x198', x198, 905), ('queue199', queue199, 594), ('p198', p198, 2050)):
    if len(s.encode('utf-8')) != want: die('%s size %d' % (name, len(s.encode('utf-8'))))
    if '\n' in s: die('newline in ' + name)

# ---- PROJECT.md ----
pr = rd('PROJECT.md')
if len(pr) != 697494: die('PROJECT input size %d' % len(pr))
if md5b(pr) != '7ee30fd1a951632f5cabbc15dcfb749e': die('PROJECT input md5')
P = pr.decode('utf-8')
lines = P.split('\n')
# THE MAP FLIP: Ch 53 `planned` -> `drafted` + the citation corrected (N365–366 -> N260–261)
mp = [i for i, l in enumerate(lines) if '53. Citric, Starch, and Vanillin' in l and '`planned`' in l]
if len(mp) != 1: die('map flip anchor %d' % len(mp))
lines[mp[0]] = lines[mp[0]].replace('`planned`', '`drafted`').replace('N365–366', 'N260–261')
if 'N260–261' not in lines[mp[0]]: die('map citation correction missing')
r = [i for i, l in enumerate(lines) if l.startswith('| 197 |')]
if len(r) != 1: die('row197 anchor %d' % len(r))
lines.insert(r[0] + 1, row198)
x = [i for i, l in enumerate(lines) if l.startswith('- [x] NEXT UNIT (session 197')]
if len(x) != 1: die('x197 anchor %d' % len(x))
lines.insert(x[0] + 1, x198)
q = [i for i, l in enumerate(lines) if l.startswith('- [ ] NEXT UNIT') and 'session 198' in l]
if len(q) != 1: die('queue anchor %d' % len(q))
lines[q[0]:q[0] + 1] = [queue199]
P2 = '\n'.join(lines)
if P2.count('| 198 |') != 1: die('| 198 | count %d' % P2.count('| 198 |'))
if P2.count('| 197 |') != 1: die('| 197 | count %d' % P2.count('| 197 |'))
if P2.count('- [x] NEXT UNIT (session 198') != 1: die('x198 count %d' % P2.count('- [x] NEXT UNIT (session 198'))
if P2.count('- [x] NEXT UNIT (session 197') != 1: die('x197 count %d' % P2.count('- [x] NEXT UNIT (session 197'))
if P2.count('session 199') != 3: die('session199 count %d' % P2.count('session 199'))
mdr = [l for l in lines if '53. Citric, Starch, and Vanillin' in l and '`drafted`' in l]
if len(mdr) != 1: die('map drafted %d' % len(mdr))
mdp = [l for l in lines if '53. Citric, Starch, and Vanillin' in l and '`planned`' in l]
if len(mdp) != 0: die('map planned present %d' % len(mdp))
if 'N260–261' not in mdr[0]: die('map citation missing post')
if P2.count('Session 198 (') != 0: die('Session198 in PROJECT %d' % P2.count('Session 198 ('))
pb = P2.encode('utf-8')
if len(pb) != 703451: die('PROJECT final size %d' % len(pb))
if md5b(pb) != 'f54d927d2260fbb18f8c6e51c9d49996': die('PROJECT final md5')
open('PROJECT.md', 'wb').write(pb)

# ---- KNOWLEDGE.md ----
kr = rd('KNOWLEDGE.md')
if len(kr) != 691545: die('KNOWLEDGE input size %d' % len(kr))
if md5b(kr) != '72c3763e31b195d14227c428da5c5297': die('KNOWLEDGE input md5')
K = kr.decode('utf-8')
J = F + '\n\n## Routing'
if K.count(J) != 1: die('J anchor %d' % K.count(J))
if K.count('Session 198 (') != 0: die('s198 pre %d' % K.count('Session 198 ('))
idx = K.index(J) + len(F)
K2 = K[:idx] + ' ' + p198 + K[idx:]
if K2.count('Session 198 (') != 1: die('s198 post %d' % K2.count('Session 198 ('))
if K2.count(J) != 1: die('J post %d' % K2.count(J))
if K2.count('**Session 198 (2026-11-05):') != 1: die('p198 junction %d' % K2.count('**Session 198 (2026-11-05):'))
kb = K2.encode('utf-8')
if len(kb) != 693596: die('KNOWLEDGE final size %d' % len(kb))
if md5b(kb) != 'd838a1093f1c0aa3f983eb971c0634ad': die('KNOWLEDGE final md5')
open('KNOWLEDGE.md', 'wb').write(kb)

print('RECIPE OK: PROJECT.md 703451 f54d927d2260fbb18f8c6e51c9d49996; KNOWLEDGE.md 693596 d838a1093f1c0aa3f983eb971c0634ad')
