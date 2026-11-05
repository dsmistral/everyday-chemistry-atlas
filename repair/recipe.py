import hashlib

def md5b(b): return hashlib.md5(b).hexdigest()
def rd(p):
    with open(p, 'rb') as f: return f.read()
def die(msg):
    print('RECIPE FAIL: ' + msg)
    raise SystemExit(1)

F = 'or whatever the user calls instead.**'

# ---- spans ----
row194 = rd('repair/row194.txt').decode('utf-8')
x194 = rd('repair/x194.txt').decode('utf-8')
queue195 = rd('repair/queue195.txt').decode('utf-8')
p194 = rd('repair/p194.txt').decode('utf-8')
for name, s, want in (('row194', row194, 6206), ('x194', x194, 975), ('queue195', queue195, 547), ('p194', p194, 2690)):
    if len(s.encode('utf-8')) != want: die('%s size %d' % (name, len(s.encode('utf-8'))))
    if '\n' in s: die('newline in ' + name)

# ---- PROJECT.md ----
pr = rd('PROJECT.md')
if len(pr) != 669488: die('PROJECT input size %d' % len(pr))
if md5b(pr) != '379384b44fe2b96fb8f232d60efe5f8e': die('PROJECT input md5')
P = pr.decode('utf-8')
lines = P.split('\n')
r = [i for i, l in enumerate(lines) if l.startswith('| 193 |')]
if len(r) != 1: die('row193 anchor %d' % len(r))
lines.insert(r[0] + 1, row194)
x = [i for i, l in enumerate(lines) if l.startswith('- [x] NEXT UNIT (session 193')]
if len(x) != 1: die('x193 anchor %d' % len(x))
lines.insert(x[0] + 1, x194)
q = [i for i, l in enumerate(lines) if l.startswith('- [ ] NEXT UNIT') and 'session 194' in l]
if len(q) != 1: die('queue anchor %d' % len(q))
lines[q[0]:q[0] + 1] = [queue195]
P2 = '\n'.join(lines)
if P2.count('| 194 |') != 1: die('| 194 | count %d' % P2.count('| 194 |'))
if P2.count('- [x] NEXT UNIT (session 194') != 1: die('x194 count %d' % P2.count('- [x] NEXT UNIT (session 194'))
if P2.count('session 195') != 3: die('session195 count %d' % P2.count('session 195'))
if P2.count('| 193 |') != 1: die('| 193 | count %d' % P2.count('| 193 |'))
pb = P2.encode('utf-8')
if len(pb) != 676536: die('PROJECT final size %d' % len(pb))
if md5b(pb) != '13e0df884f1c765b9caa992088229f62': die('PROJECT final md5')
open('PROJECT.md', 'wb').write(pb)

# ---- KNOWLEDGE.md ----
kr = rd('KNOWLEDGE.md')
if len(kr) != 680575: die('KNOWLEDGE input size %d' % len(kr))
if md5b(kr) != '5c0f865b5adf0bd2fa2c0a3746e00df9': die('KNOWLEDGE input md5')
K = kr.decode('utf-8')
J = F + '\n\n## Routing'
if K.count(J) != 1: die('J anchor %d' % K.count(J))
if K.count('Session 194 (') != 0: die('s194 pre %d' % K.count('Session 194 ('))
idx = K.index(J) + len(F)
K2 = K[:idx] + ' ' + p194 + K[idx:]
if K2.count('Session 194 (') != 1: die('s194 post %d' % K2.count('Session 194 ('))
if K2.count(J) != 1: die('J post %d' % K2.count(J))
kb = K2.encode('utf-8')
if len(kb) != 683266: die('KNOWLEDGE final size %d' % len(kb))
if md5b(kb) != '4d01b4888972fb2807b62725b1da57d1': die('KNOWLEDGE final md5')
open('KNOWLEDGE.md', 'wb').write(kb)

print('RECIPE OK: PROJECT.md 676536 13e0df884f1c765b9caa992088229f62; KNOWLEDGE.md 683266 4d01b4888972fb2807b62725b1da57d1')
