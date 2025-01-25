line = input()
a, b = line.split()
a = int(a)
b = int(b)

if a < b:
    print(b + (b - a))
else:
    print(b - (a - b))