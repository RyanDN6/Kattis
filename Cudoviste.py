rows, columns = map(int , input().split())
matrix = []

for r in range(rows):
    matrix.append(input())

cars = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

for r in range(rows - 1):
    for c in range(columns - 1):
        parking = str(matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1])
        if not parking.count("#"):
            cars[parking.count("X")] += 1

spaces = list(cars.values())

for c in spaces:
    print(c)