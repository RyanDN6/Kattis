import math

line = input()
h = int(line.split()[0])
angle = int(line.split()[1])


print(math.ceil((h / math.sin(math.pi * angle / 180.0))))