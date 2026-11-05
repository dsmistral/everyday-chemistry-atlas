import hashlib

def md5b(b): return hashlib.md5(b).hexdigest()
def rd(p):
    with open(p, 'rb') as f: return f.read()
def die(msg):
    print('RECIPE FAIL: ' + msg)
    raise SystemExit(1)

F = 'or whatever the user calls instead.**'

# ---- spans ----
p190 = rd('repair/p190.txt').decode('utf-8')
p191 = rd('repair/p191.txt').decode('utf-8')
old_seg = rd('repair/p-oldseg.txt').decode('utf-8')
new_seg = rd('repair/p-amend.txt').decode('utf-8')
if len(p190.encode()) != 2524: die('p190 size %d' % len(p190.encode()))
if len(p191.encode()) != 4211: die('p191 size %d' % len(p191.encode()))
if len(old_seg.encode()) != 465: die('p-oldseg size %d' % len(old_seg.encode()))
if len(new_seg.encode()) != 1600: die('p-amend size %d' % len(new_seg.encode()))
if not p190.startswith('**Session 190 (2026-11-05):'): die('p190 head')
if not p191.startswith('**Session 191 (2026-11-05):'): die('p191 head')
if not p190.endswith(F) or not p191.endswith(F): die('span tail')
anchor = 'reverted byte-exact (648,148 B restored) before this push.'
if not old_seg.startswith(anchor) or not new_seg.startswith(anchor): die('segment anchor head')
flip = 'The map line flips `drafted` at this push.'
if flip not in old_seg or flip not in new_seg: die('segment flip anchor')

# ---- KNOWLEDGE.md repair (E-chain, sim-proven md5-exact) ----
k = rd('KNOWLEDGE.md').decode('utf-8')
if len(k.encode()) != 671807: die('KNOWLEDGE input size %d' % len(k.encode()))
if not k.endswith('\n\n## Routing'): die('KNOWLEDGE input tail signature')
if k.count(F + '\n\n## Routing') != 2: die('KNOWLEDGE junction count != 2')
if k.count('**Session 191 (2026-11-05):') != 0: die('KNOWLEDGE unexpected 191 paragraph')
old2 = 'from Househ' + F + ' ' + p190
new2 = 'from Household Materials* (working title; user may rename).'
if k.count(old2) != 1: die('E2 anchor != 1')
k = k.replace(old2, new2)
if not k.endswith('\n\n## Routing'): die('E3 pre-tail')
k = k[:-12] + '\n'
if not k.endswith('rename).\n'): die('E3 post-tail')
J = F + '\n\n## Routing'
if k.count(J) != 1: die('E1 anchor != 1')
i = k.index(J)
k = k[:i] + F + ' ' + p190 + '\n\n## Routing' + k[i + len(J):]
if k.count(J) != 1: die('E4 anchor != 1')
i2 = k.index(J)
k = k[:i2] + F + ' ' + p191 + '\n\n## Routing' + k[i2 + len(J):]
kb = k.encode('utf-8')
if len(kb) != 676019: die('KNOWLEDGE final size %d' % len(kb))
if md5b(kb) != 'ea048b8b0773e52f2e5e3c651bc3ecb6': die('KNOWLEDGE final md5')
if k.count('\n## Routing\n') != 1: die('routing header count')
if k.count('**Session 190 (2026-11-05):') != 1: die('190 count')
if k.count('**Session 191 (2026-11-05):') != 1: die('191 count')
if k.count('(working title; user may rename).') != 1: die('title tail count')
if not k.endswith('\n'): die('final newline')
with open('KNOWLEDGE.md', 'wb') as f: f.write(kb)

# ---- PROJECT.md amendment ----
pr = rd('PROJECT.md').decode('utf-8')
if len(pr.encode()) != 656542: die('PROJECT input size %d' % len(pr.encode()))
if pr.count(old_seg) != 1: die('PROJECT amend anchor != 1')
pr = pr.replace(old_seg, new_seg)
pb = pr.encode('utf-8')
if len(pb) != 657677: die('PROJECT final size %d' % len(pb))
if md5b(pb) != '23f245a5eadb91a17897201e30bec870': die('PROJECT final md5')
with open('PROJECT.md', 'wb') as f: f.write(pb)

print('RECIPE OK: KNOWLEDGE.md 676019 ea048b8b0773e52f2e5e3c651bc3ecb6; PROJECT.md 657677 23f245a5eadb91a17897201e30bec870')
