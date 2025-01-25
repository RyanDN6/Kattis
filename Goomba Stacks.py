n = int(input())
i = 0
j = 0
total = 0
while i < n:
    line = input()
    a, b = line.split()
    a = int(a)
    b = int(b)
    total += a
    if total < b:
        print("impossible")
        i = 100000000000000
    i = i + 1
if i == n:
   print("possible")