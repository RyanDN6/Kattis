minimum = int(input())
maximum = int(input())
x = int(input())
a = []

i = minimum
while i <= maximum:
    i = str(i)
    j = 0
    total = 0
    while j < len(i):
        total = total + int(i[j])
        j = j + 1
    i = int(i)
    if total == x:
        a.append(i)
    i = i + 1

print(a[0])
print(a[-1])