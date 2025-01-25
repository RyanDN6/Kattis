n = int(input())

i = 0
while i < n:
    candles = 0
    line = input().split()
    days = line[1]
    j = 1
    while j < int(days) + 1:
        candles += j + 1
        j = j + 1
    print(i + 1, candles)
    i = i + 1
