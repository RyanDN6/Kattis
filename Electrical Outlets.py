n = int(input())

i = 0
while i < n:
    total = 0
    line = input().split()
    j = 1
    while j < int(line[0]) + 1:
        total += int(line[j])
        j = j + 1
    print(total - int(line[0]) + 1)
    i = i + 1