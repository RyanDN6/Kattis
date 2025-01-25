n = int(input())

data = []

for i in range(n):
    point = list(map(float, input().split()))
    data.append(point)

area = 0
for i in range(1, n):
    prev = data[i - 1]
    curr = data[i]

    area += (curr[0] - prev[0]) * ((curr[1] + prev[1]) / 2000)

print(area)