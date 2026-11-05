import hashlib

def md5b(b): return hashlib.md5(b).hexdigest()
def rd(p):
    with open(p, 'rb') as f: return f.read()
def die(msg):
    print('RECIPE FAIL: ' + msg)
    raise SystemExit(1)

F = 'or whatever the user calls instead.**'

# ---- spans ----
row193 = rd('repair/row193.txt').decode('utf-8')
x193 = rd('repair/x193.txt').decode('utf-8')
queue194 = rd('repair/queue194.txt').decode('utf-8')
p193 = rd('repair/p193.txt').decode('utf-8')
for name, s, want in (('row193', row193, 4346), ('x193', x193, 761), ('queue194', queue194, 682), ('p193', p193, 1908)):
    if len(s.encode('utf-8')) != want: die('%s size %d' % (name, len(s.encode('utf-8'))))
    if '\n' in s: die('newline in ' + name)

# ---- PROJECT.md ----
pr = rd('PROJECT.md')
if len(pr) != 664197: die('PROJECT input size %d' % len(pr))
if md5b(pr) != '6dffeaff86d6ad38a09117f21c2235e2': die('PROJECT input md5')
P = pr.decode('utf-8')
lines = P.split('\n')
r = [i for i, l in enumerate(lines) if l.startswith('| 192 |')]
if len(r) != 1: die('row192 anchor %d' % len(r))
lines.insert(r[0] + 1, row193)
x = [i for i, l in enumerate(lines) if l.startswith('- [x] NEXT UNIT (session 192')]
if len(x) != 1: die('x192 anchor %d' % len(x))
lines.insert(x[0] + 1, x193)
q = [i for i, l in enumerate(lines) if l.startswith('- [ ] NEXT UNIT') and 'session 193' in l]
if len(q) != 1: die('queue anchor %d' % len(q))
lines[q[0]:q[0] + 1] = [queue194]
P2 = '\n'.join(lines)
if P2.count('| 193 |') != 1: die('| 193 | count %d' % P2.count('| 193 |'))
if P2.count('- [x] NEXT UNIT (session 193') != 1: die('x193 count %d' % P2.count('- [x] NEXT UNIT (session 193'))
if P2.count('session 194') != 3: die('session194 count %d' % P2.count('session 194'))
if P2.count('| 192 |') != 1: die('| 192 | count %d' % P2.count('| 192 |'))
pb = P2.encode('utf-8')
if len(pb) != 669488: die('PROJECT final size %d' % len(pb))
if md5b(pb) != '379384b44fe2b96fb8f232d60efe5f8e': die('PROJECT final md5')
open('PROJECT.md', 'wb').write(pb)

# ---- KNOWLEDGE.md ----
kr = rd('KNOWLEDGE.md')
if len(kr) != 678666: die('KNOWLEDGE input size %d' % len(kr))
if md5b(kr) != '1a59542244fd941c481ddd43e14bc04b': die('KNOWLEDGE input md5')
K = kr.decode('utf-8')
J = F + '\n\n## Routing'
if K.count(J) != 1: die('J anchor %d' % K.count(J))
if K.count('Session 193 (') != 0: die('s193 pre %d' % K.count('Session 193 ('))
idx = K.index(J) + len(F)
K2 = K[:idx] + ' ' + p193 + K[idx:]
if K2.count('Session 193 (') != 1: die('s193 post %d' % K2.count('Session 193 ('))
if K2.count(J) != 1: die('J post %d' % K2.count(J))
kb = K2.encode('utf-8')
if len(kb) != 680575: die('KNOWLEDGE final size %d' % len(kb))
if md5b(kb) != '5c0f865b5adf0bd2fa2c0a3746e00df9': die('KNOWLEDGE final md5')
open('KNOWLEDGE.md', 'wb').write(kb)

print('RECIPE OK: PROJECT.md 669488 379384b44fe2b96fb8f232d60efe5f8e; KNOWLEDGE.md 680575 5c0f865b5adf0bd2fa2c0a3746e00df9')
