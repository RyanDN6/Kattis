rods = int(input())
total = 0

i = 0
while i < rods:
    rod = int(input())
    total = total + rod
    i = i + 1

print(total - rods + 1)