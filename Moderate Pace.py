n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in range(n-1):
    print(sorted([a[i], b[i], c[i]])[1], end=" ")

print(sorted([a[-1], b[-1], c[-1]])[1])
