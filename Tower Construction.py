n = int(input())
bricks = input().split()
width = int(bricks[0])
towers = 1
i = 1
while i < n:
    if int(bricks[i]) > width:
        towers += 1
    width = int(bricks[i])
    i = i + 1
print(towers)