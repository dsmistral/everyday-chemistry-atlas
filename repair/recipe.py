import hashlib

def md5b(b): return hashlib.md5(b).hexdigest()
def rd(p):
    with open(p, 'rb') as f: return f.read()
def die(msg):
    print('RECIPE FAIL: ' + msg)
    raise SystemExit(1)

F = 'or whatever the user calls instead.**'

# ---- spans ----
row192 = rd('repair/row192.txt').decode('utf-8')
x191 = rd('repair/x191.txt').decode('utf-8')
x192 = rd('repair/x192.txt').decode('utf-8')
queue193 = rd('repair/queue193.txt').decode('utf-8')
mapnew = rd('repair/map-new.txt').decode('utf-8')
p192 = rd('repair/p192.txt').decode('utf-8')
for name, s, want in (('row192', row192, 5089), ('x191', x191, 708), ('x192', x192, 661), ('queue193', queue193, 500), ('map-new', mapnew, 449), ('p192', p192, 2646)):
    if len(s.encode('utf-8')) != want: die('%s size %d' % (name, len(s.encode('utf-8'))))
    if '\n' in s: die('newline in ' + name)

# ---- PROJECT.md ----
pr = rd('PROJECT.md')
if len(pr) != 657677: die('PROJECT input size %d' % len(pr))
if md5b(pr) != '23f245a5eadb91a17897201e30bec870': die('PROJECT input md5')
P = pr.decode('utf-8')
lines = P.split('\n')
m = [i for i, l in enumerate(lines) if l.startswith('51. The Aniline Chain')]
if len(m) != 1: die('map anchor %d' % len(m))
if '`drafted`' not in lines[m[0]]: die('map not drafted')
lines[m[0]] = mapnew
r = [i for i, l in enumerate(lines) if l.startswith('| 191 |')]
if len(r) != 1: die('row191 anchor %d' % len(r))
lines.insert(r[0] + 1, row192)
q = [i for i, l in enumerate(lines) if l.startswith('- [ ] NEXT UNIT: AWAITING USER DIRECTION') and 'session 192' in l]
if len(q) != 1: die('queue anchor %d' % len(q))
lines[q[0]:q[0] + 1] = [x191, x192, queue193]
P2 = '\n'.join(lines)
if P2.count('| 192 |') != 1: die('| 192 | count %d' % P2.count('| 192 |'))
if P2.count('- [x] NEXT UNIT (session 191') != 1: die('x191 count %d' % P2.count('- [x] NEXT UNIT (session 191'))
if P2.count('- [x] NEXT UNIT (session 192') != 1: die('x192 count %d' % P2.count('- [x] NEXT UNIT (session 192'))
if P2.count('session 193') != 2: die('session193 count %d' % P2.count('session 193'))
pb = P2.encode('utf-8')
if len(pb) != 664197: die('PROJECT final size %d' % len(pb))
if md5b(pb) != '6dffeaff86d6ad38a09117f21c2235e2': die('PROJECT final md5')
open('PROJECT.md', 'wb').write(pb)

# ---- KNOWLEDGE.md ----
kr = rd('KNOWLEDGE.md')
if len(kr) != 676019: die('KNOWLEDGE input size %d' % len(kr))
if md5b(kr) != 'ea048b8b0773e52f2e5e3c651bc3ecb6': die('KNOWLEDGE input md5')
K = kr.decode('utf-8')
J = F + '\n\n## Routing'
if K.count(J) != 1: die('J anchor %d' % K.count(J))
if K.count('Session 192 (') != 0: die('s192 pre %d' % K.count('Session 192 ('))
idx = K.index(J) + len(F)
K2 = K[:idx] + ' ' + p192 + K[idx:]
if K2.count('Session 192 (') != 1: die('s192 post %d' % K2.count('Session 192 ('))
if K2.count(J) != 1: die('J post %d' % K2.count(J))
kb = K2.encode('utf-8')
if len(kb) != 678666: die('KNOWLEDGE final size %d' % len(kb))
if md5b(kb) != '1a59542244fd941c481ddd43e14bc04b': die('KNOWLEDGE final md5')
open('KNOWLEDGE.md', 'wb').write(kb)

print('RECIPE OK: PROJECT.md 664197 6dffeaff86d6ad38a09117f21c2235e2; KNOWLEDGE.md 678666 1a59542244fd941c481ddd43e14bc04b')
