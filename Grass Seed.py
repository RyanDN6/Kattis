cost = float(input())
lawns = float(input())
total = 0
i = 0
while i < lawns:
    lawn = input().split()
    area = float(lawn[0]) * float(lawn[1])
    total += area
    i = i + 1

print(total * cost)