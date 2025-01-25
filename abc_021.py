l = input().split()
l[0] = int(l[0])
l[1] = int(l[1])
l[2] = int(l[2])

i = 0
while i < len(l):
    p = i
    j = i + 1
    while j < len(l):
        if int(l[p]) > int(l[j]):
            p = j
        j = j + 1
    tmp = int(l[i])
    l[i] = int(l[p])
    l[p] = tmp
    i = i + 1
a, b, c = map(str,l)

result = ""

line = input()
i = 0
while i < len(line):
    if line[i] == "A":
        result += a + " "
    elif line[i] == "B":
        result += b + " "
    else:
        result += c + " "
    i = i + 1

print(result.strip())