rows, columns, mines = map(int, input().split())

grid = []

for r in range(rows):
    a = []
    for c in range(columns):
        a.append(".")
    grid.append(a)

for mine in range(mines):
    location = input().split()
    r = int(location[0]) - 1
    c = int(location[1]) - 1

    grid[r][c] = "*"

for i in range(rows):
    print("".join(grid[i]))
