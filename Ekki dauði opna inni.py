line1 = ""
line2 = ""

i = 0
while i < 2:
    line = input().split("|")
    line1 += line[0]
    line2 += line[1]
    i = i + 1

print(line1, line2)