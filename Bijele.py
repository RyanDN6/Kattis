line = input().split()
chess = [1, 1, 2, 2, 2, 8]

i = 0
while i < len(line):
    line[i] = int(line[i])
    i = i + 1

tmp = chess
chess = line
line = tmp
print(line[0] - chess[0], line[1] - chess[1], line[2] - chess[2], line[3] - chess[3], line[4] - chess[4], line[5] - chess[5])
