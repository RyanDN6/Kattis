import math

a = []
b = []
s = input()

rank = {
    1: 100,
    2: 75,
    3: 60,
    4: 50,
    5: 45,
    6: 40,
    7: 36,
    8: 32,
    9: 29,
    10: 26,
    11: 24,
    12: 22,
    13: 20,
    14: 18,
    15: 16,
    16: 15,
    17: 14,
    18: 13,
    19: 12,
    20: 11,
    21: 10,
    22: 9,
    23: 8,
    24: 7,
    25: 6,
    26: 5,
    27: 4,
    28: 3,
    29: 2,
    30: 1,
}

contests = int(s.split()[0])
people = int(s.split()[1])
i = 0
while i < people:
    fuck = input().strip().split()
    scores = [int(fuck[i]) for i in range(contests -1)]
    j = 0
    p = 0
    while j < len(scores):
        p = j
        k = j + 1
        while k < len(scores):
            if scores[k] > scores[p]:
                p = k
            k = k + 1
        tmp = scores[p]
        scores[p] = scores[j]
        scores[j] = tmp
        j = j + 1
    total = 0
    if len(scores) > 3:
        total = scores[0] + scores[1] + scores[2] + scores[3]
    else:
       j = 0
    
       while j < len(scores):
          total = total + scores[j]
          j = j + 1
    if i != 0:
        a.append(total)
    else:
        b.append(total)  # a = aggregate
    i = i + 1

i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] > a[p]:
            p = j
        j = j + 1
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp
    i = i + 1
total = rank[1]
i = 0
while i < len(a) and (a[i] + total) // (1 + i) > b[0]:
    print((a[i] + total) // (1 + i))
    total = total + rank[1 + i]
    i = i + 1

print(i)

    #if i != 0:
    #    scores.append(rank[i] + 1)
    #else:
    #    scores.append(0)