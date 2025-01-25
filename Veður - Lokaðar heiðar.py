wind = int(input())
n = int(input())

i = 0
while i < n:
    line = input().split()
    if int(line[1]) >= wind:
        print(line[0], "opin")
    else:
        print(line[0], "lokud")
    i = i + 1