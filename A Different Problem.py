import sys

lines = sys.stdin.readlines()
i = 0
while i < len(lines):
    line = lines[i]
    x, y = line.split()
    x = int(x)
    y = int(y)
    print(abs(x - y))
    i = i + 1