blocks = int(input())

h = 0
i = 0
while blocks > 0:
    if blocks - ((1 + (i * 2)) ** 2) >= 0:
        h = h + 1
    blocks = blocks - ((1 + (i * 2)) ** 2)
    i = i + 1

print(h)