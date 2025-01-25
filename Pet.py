highest = "0 0"
i = 0
while i < 5:
    ratings = input().split()
    total = 0
    j = 0
    while j < 4:
        total += int(ratings[j])
        j = j + 1
    if total > int(highest.split()[1]):
        highest = str(i + 1) + " " + str(total)
    i = i + 1

print(highest)

