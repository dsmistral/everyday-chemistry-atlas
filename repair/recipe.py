import hashlib, sys

def md5(b):
    return hashlib.md5(b).hexdigest()

def gate(data, size, h, name):
    if len(data) != size or md5(data) != h:
        sys.stderr.write("GATE FAIL: %s (got %d bytes %s)\n" % (name, len(data), md5(data)))
        sys.exit(1)

project = open("PROJECT.md", "rb").read()
know = open("KNOWLEDGE.md", "rb").read()
row = open("repair/row200.txt", "rb").read()
x200 = open("repair/x200.txt", "rb").read()
queue = open("repair/queue201.txt", "rb").read()
p200 = open("repair/p200.txt", "rb").read()

gate(project, 712869, "1e621331405e240148ab5dea190ff97b", "PROJECT.md input")
gate(know, 695195, "7645b8541ed5b4c513c21b43a7125cb5", "KNOWLEDGE.md input")
gate(row, 8874, "17d2bb869bd351d8a77217b11d691bd1", "repair/row200.txt")
gate(x200, 1666, "32fa83551be3180876287da42c961884", "repair/x200.txt")
gate(queue, 404, "f6c2728b067cf4da5577b3c72a1a9b0c", "repair/queue201.txt")
gate(p200, 2818, "3c0cb6074f193a766edfafc81ee49346", "repair/p200.txt")

row_s = row.decode("utf-8")
x_s = x200.decode("utf-8")
q_s = queue.decode("utf-8")
p_s = p200.decode("utf-8")

pl = project.decode("utf-8").split("\n")
out = []
n_row = n_x = n_q = n_map = 0
for line in pl:
    if line.startswith("| 199 |"):
        out.append(line)
        out.append(row_s)
        n_row += 1
        continue
    if line.startswith("55. Cryogens") and "planned" in line:
        out.append(line.replace("planned", "drafted", 1))
        n_map += 1
        continue
    if line.startswith("- [ ] NEXT UNIT") and "session 200" in line:
        out.append(q_s)
        n_q += 1
        continue
    if line.startswith("- [x] NEXT UNIT (session 199"):
        out.append(line)
        out.append(x_s)
        n_x += 1
        continue
    out.append(line)

new_project = "\n".join(out).encode("utf-8")
kl = know.decode("utf-8").split("\n")
kl[9] = kl[9] + " " + p_s
new_know = "\n".join(kl).encode("utf-8")

gate(new_project, 723206, "1db0dde23157c70bfb985383596659fa", "PROJECT.md output")
gate(new_know, 698014, "a973b6bb7a1d4ae960fa1100e33e5473", "KNOWLEDGE.md output")

if not (n_row == 1 and n_x == 1 and n_q == 1 and n_map == 1):
    sys.stderr.write("GATE FAIL: transform counts row=%d x=%d queue=%d map=%d\n" % (n_row, n_x, n_q, n_map))
    sys.exit(1)

open("PROJECT.md", "wb").write(new_project)
open("KNOWLEDGE.md", "wb").write(new_know)
print("Session 200 close applied: row200, x200, queue201, map 55->drafted, KNOWLEDGE p200.")
print("PROJECT.md %d bytes %s" % (len(new_project), md5(new_project)))
print("KNOWLEDGE.md %d bytes %s" % (len(new_know), md5(new_know)))
