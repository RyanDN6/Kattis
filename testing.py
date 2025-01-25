n = 0
i = 0
x = 0
gmin = 1000001
gmax = -1
g1 = 0
g2 = 0
k = 0
g = 0

line = input().split()

k = int(line[0])
while x != 0:
    g += 1
    if x % 10 == k:
        if x > gmax:
            gmax = x
            g1 = g
        if x < gmin:
            gmin = x
            g2 = g
    x = int(input())