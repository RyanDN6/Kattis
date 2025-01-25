import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    line = lines[i]
    s = ""
    j = 0
    while j < len(line) - 1:
        num = 1
        if line[j] == line[j + 1]:
            while line[j] == line[j + 1] and j < len(line) - 2:
                num += 1
                j = j + 1
        if line[-1] == line[-2]:
            num += 1
        s += str(num) + line[j]
        j = j + 1
    print(s)
    i = i + 1