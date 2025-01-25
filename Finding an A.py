line = input()

i = 0
while i < len(line):
    if line[i] == "a":
        print(line[i:])
        break
    i = i + 1