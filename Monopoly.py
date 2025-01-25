n = int(input())

dice = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36,
}

probability = 0
line = input().split()
i = 0
while i < n:
    probability += dice[int(line[i])]
    i = i + 1

print(probability)