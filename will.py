import sys
lines = sys.stdin.readlines()
i = 0
while i < len(lines):
    line = lines[i].strip().split(":")
    surname = line[0].split()[1][0]
    pets = str(line[1:])
    print(pets.split(","))
    i = i + 1
