n = int(input())
a = []
i = 0
while i < n:
    num = int(input())
    a.append(num)
    i = i + 1
a.sort()
sales = len(a) // 3
i = 0
while i < sales:
    a.pop(0)
    i = i + 1
total = 0
i = 0
while i < len(a):
    total += a[i]
    i = i + 1

print(total)