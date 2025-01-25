m = int(input())
numbers = input().split()
i = 0
while i < m:
    numbers[i] = int(numbers[i])
    i = i + 1

n = int(input())

i = 0
while i < n:
    line = input().split()
    total = 0
    if len(line) == 2:
        inflation = int(line[1])
        j = 0
        while j < m:
            numbers[j] += inflation
            total = total + numbers[j]
            j = j + 1
    else:
        x = int(line[1])
        y = int(line[2])
        j = 0
        while j < m:
            if numbers[j] == x:
                numbers[j] = y
            total = total + numbers[j]
            j = j + 1
    print(total)
    i = i + 1