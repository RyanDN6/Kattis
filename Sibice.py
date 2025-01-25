line = input()
n, a, b = line.split()
n = int(n)
a = int(a)
b = int(b)
c = ((a * a) + (b * b)) ** 0.5

i = 0
while i < n:
    m = int(input())
    if m <= c:
        print("DA")
    else:
        print("NE")
    i = i + 1

    