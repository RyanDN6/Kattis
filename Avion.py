blimps = 0
i = 0
while i < 5:
    line = input()
    j = 0
    while j < len(line) - 3:
        if line[j] == "F" and line[j + 1] == "B" and line[j + 2] == "I":
            blimps += 1
            j = len(line)
        j = j + 1
    i = i + 1

if blimps != 0:
    print(blimps)
else:
    print("HE GOT AWAY!")