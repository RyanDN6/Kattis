n = int(input())
names = []
i = 0
while i < n:
    line = input()
    names.append(line)
    i = i + 1
i = 0
while i < len(names):
    if names[i][-1] != "!" and line[i + 1][-1] == "!":
        names.pop(i)
        names.pop(i + 1)
        i = i - 1
    else:
        i = i + 1
    i = i + 1

print(names)        