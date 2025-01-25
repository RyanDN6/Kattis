n = int(input())
m = input().split()
total = 0

i = 0
while i < n:
    if int(m[i]) < 0:
        total = total + 1
    i = i + 1

print(total)