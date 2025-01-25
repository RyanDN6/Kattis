n = int(input())
line = input().split()
count = 0
total = 0

i = 0
while i < len(line):
    if line[i] != "-1":
        total += int(line[i])
        count += 1
    i = i + 1

print(total / count)