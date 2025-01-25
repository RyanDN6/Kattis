n = int(input())
names = {}
i = 0
while i < n:
    name = input()
    names[name] = 0
    i = i + 1

n = int(input())
i = 0
while i < n:
    line = input().split()
    j = 0
    while j < len(line):
        if line[j] in names:
            names[line[j]] += 1
        j = j + 1
    i = i + 1
sorted = []
i = n
while i >= 0:
    for key in names:
        if names[key] == i:
            print(i, key)
    i = i - 1