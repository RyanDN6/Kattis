n, m = map(int,input().split())
i = 0
grid = []
while i < n:
    s = input()
    grid.append(s)
    i = i + 1
i = 0
while i < m:
    j = 0
    line = ""
    while j < n:
        line += grid[j][i]
        j = j + 1
    grid.append(line)
    i = i + 1
data = []
i = 0
while i < len(grid):
    word = grid[i].split("#")
    if len(word) == 1:
        data.append(word[0])
    else:
        j = 0
        while j < len(word):
            if len(word[j]) > 1:
                data.append(word[j])
            j = j + 1
    i = i + 1
print(sorted(data)[0])