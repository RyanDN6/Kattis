line = input().split()
i = 0
l = 0
w = 0
while i < 10:
    if i % 2 == 0:
        l += int(line[i])       
    else:
        w += int(line[i])
    i += 1

total = (l / 5) * (w / 5)
line2 = input().split()
print(((total * int(line2[0])) // int(line2[1])))
print(round((total * int(line2[0])) / int(line2[1])))