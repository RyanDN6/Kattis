n = int(input())
i = 0
line = input().split()
while i < n:
    line[i] = int(line[i])
    i = i + 1

line.sort()
alice = 0
bob = 0

i = 0
while i < n:
    if i % 2 == 0:
        alice += line[i]
    else:
        bob += line[i]
    i = i + 1
print(alice,bob)