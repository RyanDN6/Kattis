one = input().split()
two = input().split()
three = input().split()

x1 = int(one[0])
y1 = int(one[1])

x2 = int(two[0])
y2 = int(two[1])

x3 = int(three[0])
y3 = int(three[1])

if x1 == x2:
    x4 = x3
elif x3 == x1:
    x4 = x2
elif x3 == x2:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y3 == y1:
    y4 = y2
elif y3 == y2:
    y4 = y1

print(x4, y4)