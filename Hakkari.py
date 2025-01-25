rows, columns = map(int, input().split())

matrix = []
mines = 0

for row in range(rows):    
    a = []
    data = input()
    # A for loop for column entries
    for column in range(columns):
        if data[column] != ".":
            mines += 1

        a.append(data[column])
    matrix.append(a)

for row in range(rows):
    for column in range(columns):
        if matrix[row][column] != ".":
            mines += 1
            print(row + 1, column + 1)