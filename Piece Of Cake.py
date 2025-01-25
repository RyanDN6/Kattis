line = input()
length, x, y = line.split()
length = int(length)
x = int(x)
y = int(y)
z = 4
a = []
one = x * y * z
a.append(one)
two = (length - x) * y * z
a.append(two)
three = x * (length - y) * z
a.append(three)
four = (length - x) * (length - y) * z
a.append(four)

a.sort()

print(a[-1])