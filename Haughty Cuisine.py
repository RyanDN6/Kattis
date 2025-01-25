n = int(input())

dishes = []
for i in range(0, n):
    dishes.append(input().split())

n = len(dishes[0])

for i in range(0, n):
    print(dishes[0][i])