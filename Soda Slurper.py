a, b, cost = map(int,input().split())

bottles = a + b
drank = 0
while bottles >= cost:
    drank += 1
    bottles = bottles + 1 - cost
print(drank)