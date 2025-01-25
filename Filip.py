line = input()
a, b = line.split()
c = ""
d = ""
i = 0
while i < 3:
    c = c + a[len(a) - 1 - i] 
    d = d + b[len(b) - 1 - i]
    i = i + 1

if c > d:
    print(c)
else:
    print(d)