player = int(input())
n = int(input())
i = 0
bomb = 210
while i < n:
    line = input().split()
    time = int(line[0])
    bomb -= time
    if bomb <= 0:
        print(player)
        break
    ans = line[1]
    if ans == "T":
        player += 1
        if player == 9:
            player = 1
    i = i + 1