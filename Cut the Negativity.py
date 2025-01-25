n = int(input())
a = []
i = 0

count = 0
while i < n:
    line = input().split()
    j = 0
    while j < n:
        if line[j] != "-1":
            flight = str(i + 1) + " " + str(j + 1) + " " + str(line[j])
            a.append(flight)
            count += 1
        j = j + 1
    i = i + 1

print(count)

i = 0
while i < len(a):
    print(a[i])
    i = i + 1