line = input()
w = 0
b = 0
i = 0
while i < len(line):
    if line[i] == "W":
        w += 1
    else:
        b += 1
    i = i + 1

if w == b:
    print(1)
else:
    print(0)