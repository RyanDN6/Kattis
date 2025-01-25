x1, y1, x2, y2 = map(float, input().split())

length = abs(x1) + abs(x2)
width = abs(y1) + abs(y2)

area = length * width

print(round(area, ndigits=3))