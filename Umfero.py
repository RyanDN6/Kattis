cells = int(input())
lanes = int(input())
total = cells * lanes
empty = 0

i = 0
while i < lanes:
    line = input()
    j = 0
    while j < cells:
        if line[j] == ".":
            empty += 1
        j = j + 1
    i = i + 1

print(empty / total)