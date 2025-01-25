import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    line = lines[i].split()
    name = []
    j = 0
    while j < len(line):
        if line[j][0] >= "A" and line[j][0] <= "Z":
            name.append(line[j])
            line.pop(j)
        else:
            j = j + 1
    name = " ".join(name)
    total = 0
    j = 0
    while j < len(line):
        total += float(line[j])
        j = j + 1
    print((total / len(line)), name)
    i = i + 1