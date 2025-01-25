n = int(input())
i = 0
grid = []
while i < n:
    s = input()
    grid.append(s)
    i = i + 1
i = 0
while i < n:
    j = 0
    line = ""
    while j < n:
        line += grid[j][i]
        j = j + 1
    grid.append(line)
    i = i + 1
i = 0
boolean = True
while i < n * 2 and boolean:
    w = 0
    b = 0
    s = grid[i]
    j = 0
    while j < n:
        if s[j] == "W":
            w += 1
        else:
            b += 1
        j = j + 1
    if w == b:
        j = 0
        while j + 2 < n:
            if s[j] == s[j + 1] == s[j + 2]:
                boolean = False
                break
            j = j + 1
    else:
        boolean = False
        break
    i = i + 1
if boolean == True:
    print(1)
else:
    print(0)