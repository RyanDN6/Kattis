n = int(input())
total = 0
i = 0
line = input().split()
while i < n:
    total += int(line[i])
    i = i + 1

print(total)