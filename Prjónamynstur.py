d = {
    ".": 20,
    "O": 10,
    "/": 25,
    "A": 35,
    "^": 5,
    "v": 22,
}

line = input()
a, b = line.split()
a = int(a)
b = int(b)

total = 0

i = 0
while i < a:
    line = input()
    j = 0
    while j < b:
        if line[j] in d:
            total = total + d[line[j]]
        else:
            total = total + 25
        j = j + 1
    i = i + 1

print(total)