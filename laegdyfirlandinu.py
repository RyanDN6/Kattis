rows, columns = map(int, input().split())

matrix = []
for r in range(rows):
    matrix.append(list(map(int, input().split())))

for r in range(1, rows - 1):
    for c in range(1, columns - 1):
        if matrix[r][c] < matrix[r - 1][c] and matrix[r][c] < matrix[r + 1][c] and matrix[r][c] < matrix[r][c + 1] and matrix[r][c] < matrix[r][c - 1]:
            print("Jebb")
            exit()

print("Neibb")