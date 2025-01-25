n, prize = input().split()
n = int(n)
prize = int(prize)

a = input().split()
i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if int(a[p]) > int(a[j]):
            p = j
        j = j + 1
    tmp = int(a[i])
    a[i] = int(a[p])
    a[p] = tmp
    i = i + 1

total = 0
i = 0
while total <= prize:
    i = i + 1
    total += a[i]

print(i)