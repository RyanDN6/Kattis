a, b, c, d = map(float, input().split())

s = (a + b + c + d) / 2

print(((s - a)*(s - b)*(s - c)*(s - d)) ** 0.5)