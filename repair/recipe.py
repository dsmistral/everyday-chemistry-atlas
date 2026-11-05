import hashlib

def md5b(b): return hashlib.md5(b).hexdigest()
def rd(p):
    with open(p, 'rb') as f: return f.read()
def die(msg):
    print('RECIPE FAIL: ' + msg)
    raise SystemExit(1)

F = 'or whatever the user calls instead.**'

# ---- spans ----
row195 = rd('repair/row195.txt').decode('utf-8')
x195 = rd('repair/x195.txt').decode('utf-8')
queue196 = rd('repair/queue196.txt').decode('utf-8')
p195 = rd('repair/p195.txt').decode('utf-8')
for name, s, want in (('row195', row195, 7152), ('x195', x195, 980), ('queue196', queue196, 505), ('p195', p195, 3042)):
    if len(s.encode('utf-8')) != want: die('%s size %d' % (name, len(s.encode('utf-8'))))
    if '\n' in s: die('newline in ' + name)

# ---- PROJECT.md ----
pr = rd('PROJECT.md')
if len(pr) != 676536: die('PROJECT input size %d' % len(pr))
if md5b(pr) != '13e0df884f1c765b9caa992088229f62': die('PROJECT input md5')
P = pr.decode('utf-8')
lines = P.split('\n')
r = [i for i, l in enumerate(lines) if l.startswith('| 194 |')]
if len(r) != 1: die('row194 anchor %d' % len(r))
lines.insert(r[0] + 1, row195)
x = [i for i, l in enumerate(lines) if l.startswith('- [x] NEXT UNIT (session 194')]
if len(x) != 1: die('x194 anchor %d' % len(x))
lines.insert(x[0] + 1, x195)
q = [i for i, l in enumerate(lines) if l.startswith('- [ ] NEXT UNIT') and 'session 195' in l]
if len(q) != 1: die('queue anchor %d' % len(q))
lines[q[0]:q[0] + 1] = [queue196]
m = [i for i, l in enumerate(lines) if '52. The Medicine Shelf' in l and 'planned' in l]
if len(m) != 1: die('map anchor %d' % len(m))
if lines[m[0]].count('planned') != 1: die('map planned count %d' % lines[m[0]].count('planned'))
lines[m[0]] = lines[m[0]].replace('planned', 'drafted')
P2 = '\n'.join(lines)
if P2.count('| 195 |') != 1: die('| 195 | count %d' % P2.count('| 195 |'))
if P2.count('| 194 |') != 1: die('| 194 | count %d' % P2.count('| 194 |'))
if P2.count('- [x] NEXT UNIT (session 195') != 1: die('x195 count %d' % P2.count('- [x] NEXT UNIT (session 195'))
if P2.count('- [x] NEXT UNIT (session 194') != 1: die('x194 count %d' % P2.count('- [x] NEXT UNIT (session 194'))
if P2.count('session 196') != 3: die('session196 count %d' % P2.count('session 196'))
mm = [l for l in lines if '52. The Medicine Shelf' in l and 'planned' in l]
if len(mm) != 0: die('map planned post %d' % len(mm))
md = [l for l in lines if '52. The Medicine Shelf' in l and 'drafted' in l]
if len(md) != 1: die('map drafted %d' % len(md))
pb = P2.encode('utf-8')
if len(pb) != 684628: die('PROJECT final size %d' % len(pb))
if md5b(pb) != '0beb69228a507c4811ae53db55cc7d08': die('PROJECT final md5')
open('PROJECT.md', 'wb').write(pb)

# ---- KNOWLEDGE.md ----
kr = rd('KNOWLEDGE.md')
if len(kr) != 683266: die('KNOWLEDGE input size %d' % len(kr))
if md5b(kr) != '4d01b4888972fb2807b62725b1da57d1': die('KNOWLEDGE input md5')
K = kr.decode('utf-8')
J = F + '\n\n## Routing'
if K.count(J) != 1: die('J anchor %d' % K.count(J))
if K.count('Session 195 (') != 0: die('s195 pre %d' % K.count('Session 195 ('))
idx = K.index(J) + len(F)
K2 = K[:idx] + ' ' + p195 + K[idx:]
if K2.count('Session 195 (') != 1: die('s195 post %d' % K2.count('Session 195 ('))
if K2.count(J) != 1: die('J post %d' % K2.count(J))
kb = K2.encode('utf-8')
if len(kb) != 686309: die('KNOWLEDGE final size %d' % len(kb))
if md5b(kb) != '124106f0ea07e691ef47a94b1a31e33c': die('KNOWLEDGE final md5')
open('KNOWLEDGE.md', 'wb').write(kb)

print('RECIPE OK: PROJECT.md 684628 0beb69228a507c4811ae53db55cc7d08; KNOWLEDGE.md 686309 124106f0ea07e691ef47a94b1a31e33c')
