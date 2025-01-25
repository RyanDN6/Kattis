h, w, n = map(int,input().split())
bricks = input().split()
length = 0
i = 0
j = 0
while i < n:
    length += int(bricks[i])
    if length > w:
        break
    elif length == w:
        j = j + 1
        if j == h:
            break
        length = 0
    i = i + 1

if j >= h:
    print("YES")
else:
    print("NO")