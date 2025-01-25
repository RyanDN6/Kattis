rows, columns = map(int, input().split())

matrix = []

for r in range(rows):
    matrix.append(list(input()))

swapped = True

while swapped:
    swapped = False
    for r in range(rows - 1):
        for c in range(columns):
            if matrix[r][c] == "S" and matrix[r + 1][c] == ".":
                matrix[r][c] = "."
                matrix[r + 1][c] = "S"
                swapped = True

for r in range(rows):
    print("".join(matrix[r]))