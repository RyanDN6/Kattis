n = int(input())

i = 0
while i < n:
    m = int(input())
    j = 1
    sum = 1
    while j < m + 1:
        sum = sum * j
        j = j + 1
    print(str(sum)[-1])
    i = i + 1