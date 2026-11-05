import hashlib

def md5b(b): return hashlib.md5(b).hexdigest()
def rd(p):
    with open(p, 'rb') as f: return f.read()
def die(msg):
    print('RECIPE FAIL: ' + msg)
    raise SystemExit(1)

F = 'or whatever the user calls instead.**'

# ---- spans ----
row196 = rd('repair/row196.txt').decode('utf-8')
x196 = rd('repair/x196.txt').decode('utf-8')
queue197 = rd('repair/queue197.txt').decode('utf-8')
p196 = rd('repair/p196.txt').decode('utf-8')
for name, s, want in (('row196', row196, 6956), ('x196', x196, 1564), ('queue197', queue197, 527), ('p196', p196, 3300)):
    if len(s.encode('utf-8')) != want: die('%s size %d' % (name, len(s.encode('utf-8'))))
    if '\n' in s: die('newline in ' + name)

# ---- PROJECT.md ----
pr = rd('PROJECT.md')
if len(pr) != 684628: die('PROJECT input size %d' % len(pr))
if md5b(pr) != '0beb69228a507c4811ae53db55cc7d08': die('PROJECT input md5')
P = pr.decode('utf-8')
lines = P.split('\n')
r = [i for i, l in enumerate(lines) if l.startswith('| 195 |')]
if len(r) != 1: die('row195 anchor %d' % len(r))
lines.insert(r[0] + 1, row196)
x = [i for i, l in enumerate(lines) if l.startswith('- [x] NEXT UNIT (session 195')]
if len(x) != 1: die('x195 anchor %d' % len(x))
lines.insert(x[0] + 1, x196)
q = [i for i, l in enumerate(lines) if l.startswith('- [ ] NEXT UNIT') and 'session 196' in l]
if len(q) != 1: die('queue anchor %d' % len(q))
lines[q[0]:q[0] + 1] = [queue197]
# NO map flip this close: the review's part 2 flips `drafted`->`reviewed`
mm = [l for l in lines if '52. The Medicine Shelf' in l and 'planned' in l]
if len(mm) != 0: die('map planned present %d' % len(mm))
md = [l for l in lines if '52. The Medicine Shelf' in l and 'drafted' in l]
if len(md) != 1: die('map drafted %d' % len(md))
P2 = '\n'.join(lines)
if P2.count('| 196 |') != 1: die('| 196 | count %d' % P2.count('| 196 |'))
if P2.count('| 195 |') != 1: die('| 195 | count %d' % P2.count('| 195 |'))
if P2.count('- [x] NEXT UNIT (session 196') != 1: die('x196 count %d' % P2.count('- [x] NEXT UNIT (session 196'))
if P2.count('- [x] NEXT UNIT (session 195') != 1: die('x195 count %d' % P2.count('- [x] NEXT UNIT (session 195'))
if P2.count('session 197') != 3: die('session197 count %d' % P2.count('session 197'))
if P2.count('Session 196 (') != 0: die('Session196 in PROJECT %d' % P2.count('Session 196 ('))
pb = P2.encode('utf-8')
if len(pb) != 693172: die('PROJECT final size %d' % len(pb))
if md5b(pb) != '659e2bed710860871356c9f1156b5070': die('PROJECT final md5')
open('PROJECT.md', 'wb').write(pb)

# ---- KNOWLEDGE.md ----
kr = rd('KNOWLEDGE.md')
if len(kr) != 686309: die('KNOWLEDGE input size %d' % len(kr))
if md5b(kr) != '124106f0ea07e691ef47a94b1a31e33c': die('KNOWLEDGE input md5')
K = kr.decode('utf-8')
J = F + '\n\n## Routing'
if K.count(J) != 1: die('J anchor %d' % K.count(J))
if K.count('Session 196 (') != 0: die('s196 pre %d' % K.count('Session 196 ('))
idx = K.index(J) + len(F)
K2 = K[:idx] + ' ' + p196 + K[idx:]
if K2.count('Session 196 (') != 1: die('s196 post %d' % K2.count('Session 196 ('))
if K2.count(J) != 1: die('J post %d' % K2.count(J))
if K2.count('**Session 196 (2026-11-05):') != 1: die('p196 junction %d' % K2.count('**Session 196 (2026-11-05):'))
kb = K2.encode('utf-8')
if len(kb) != 689610: die('KNOWLEDGE final size %d' % len(kb))
if md5b(kb) != 'bc154af59b69a081eaf412e92020f46d': die('KNOWLEDGE final md5')
open('KNOWLEDGE.md', 'wb').write(kb)

print('RECIPE OK: PROJECT.md 693172 659e2bed710860871356c9f1156b5070; KNOWLEDGE.md 689610 bc154af59b69a081eaf412e92020f46d')
