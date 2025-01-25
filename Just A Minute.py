n = int(input())

times = []
for i in range(0, n):
    a, b = map(int, input().split())
    times.append(b / (a * 60))

average = 0

for time in times:
    average += time / len(times)

print(average)