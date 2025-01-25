line = input().split(";")
total = 0

i = 0
while i < len(line):
    j = 0
    while j < len(line[i]):
        if line[i][j] == "-":
            total = total + (int(line[i][j + 1:]) - int(line[i][0:j])) + 1
            j = 1000
        j = j + 1
    if j == len(line[i]):
        total = total + 1
    i = i + 1

print(total)