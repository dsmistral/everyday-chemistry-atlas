import hashlib

def md5b(b): return hashlib.md5(b).hexdigest()
def rd(p):
    with open(p, 'rb') as f: return f.read()
def die(msg):
    print('RECIPE FAIL: ' + msg)
    raise SystemExit(1)

F = 'or whatever the user calls instead.**'

# ---- spans ----
row197 = rd('repair/row197.txt').decode('utf-8')
x197 = rd('repair/x197.txt').decode('utf-8')
queue198 = rd('repair/queue198.txt').decode('utf-8')
p197 = rd('repair/p197.txt').decode('utf-8')
for name, s, want in (('row197', row197, 3405), ('x197', x197, 881), ('queue198', queue198, 560), ('p197', p197, 1934)):
    if len(s.encode('utf-8')) != want: die('%s size %d' % (name, len(s.encode('utf-8'))))
    if '\n' in s: die('newline in ' + name)

# ---- PROJECT.md ----
pr = rd('PROJECT.md')
if len(pr) != 693172: die('PROJECT input size %d' % len(pr))
if md5b(pr) != '659e2bed710860871356c9f1156b5070': die('PROJECT input md5')
P = pr.decode('utf-8')
lines = P.split('\n')
# THE MAP FLIP: Ch 52 `drafted` -> `reviewed` (the review part 2 close)
mp = [i for i, l in enumerate(lines) if '52. The Medicine Shelf' in l and '`drafted`' in l]
if len(mp) != 1: die('map flip anchor %d' % len(mp))
lines[mp[0]] = lines[mp[0]].replace('`drafted`', '`reviewed`')
r = [i for i, l in enumerate(lines) if l.startswith('| 196 |')]
if len(r) != 1: die('row196 anchor %d' % len(r))
lines.insert(r[0] + 1, row197)
x = [i for i, l in enumerate(lines) if l.startswith('- [x] NEXT UNIT (session 196')]
if len(x) != 1: die('x196 anchor %d' % len(x))
lines.insert(x[0] + 1, x197)
q = [i for i, l in enumerate(lines) if l.startswith('- [ ] NEXT UNIT') and 'session 197' in l]
if len(q) != 1: die('queue anchor %d' % len(q))
lines[q[0]:q[0] + 1] = [queue198]
P2 = '\n'.join(lines)
if P2.count('| 197 |') != 1: die('| 197 | count %d' % P2.count('| 197 |'))
if P2.count('| 196 |') != 1: die('| 196 | count %d' % P2.count('| 196 |'))
if P2.count('- [x] NEXT UNIT (session 197') != 1: die('x197 count %d' % P2.count('- [x] NEXT UNIT (session 197'))
if P2.count('- [x] NEXT UNIT (session 196') != 1: die('x196 count %d' % P2.count('- [x] NEXT UNIT (session 196'))
if P2.count('session 198') != 3: die('session198 count %d' % P2.count('session 198'))
mrev = [l for l in lines if '52. The Medicine Shelf' in l and '`reviewed`' in l]
if len(mrev) != 1: die('map reviewed %d' % len(mrev))
mdr = [l for l in lines if '52. The Medicine Shelf' in l and '`drafted`' in l]
if len(mdr) != 0: die('map drafted present %d' % len(mdr))
if P2.count('Session 197 (') != 0: die('Session197 in PROJECT %d' % P2.count('Session 197 ('))
pb = P2.encode('utf-8')
if len(pb) != 697494: die('PROJECT final size %d' % len(pb))
if md5b(pb) != '7ee30fd1a951632f5cabbc15dcfb749e': die('PROJECT final md5')
open('PROJECT.md', 'wb').write(pb)

# ---- KNOWLEDGE.md ----
kr = rd('KNOWLEDGE.md')
if len(kr) != 689610: die('KNOWLEDGE input size %d' % len(kr))
if md5b(kr) != 'bc154af59b69a081eaf412e92020f46d': die('KNOWLEDGE input md5')
K = kr.decode('utf-8')
J = F + '\n\n## Routing'
if K.count(J) != 1: die('J anchor %d' % K.count(J))
if K.count('Session 197 (') != 0: die('s197 pre %d' % K.count('Session 197 ('))
idx = K.index(J) + len(F)
K2 = K[:idx] + ' ' + p197 + K[idx:]
if K2.count('Session 197 (') != 1: die('s197 post %d' % K2.count('Session 197 ('))
if K2.count(J) != 1: die('J post %d' % K2.count(J))
if K2.count('**Session 197 (2026-11-05):') != 1: die('p197 junction %d' % K2.count('**Session 197 (2026-11-05):'))
kb = K2.encode('utf-8')
if len(kb) != 691545: die('KNOWLEDGE final size %d' % len(kb))
if md5b(kb) != '72c3763e31b195d14227c428da5c5297': die('KNOWLEDGE final md5')
open('KNOWLEDGE.md', 'wb').write(kb)

print('RECIPE OK: PROJECT.md 697494 7ee30fd1a951632f5cabbc15dcfb749e; KNOWLEDGE.md 691545 72c3763e31b195d14227c428da5c5297')
