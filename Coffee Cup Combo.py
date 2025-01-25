n = int(input())
line = input()
awake = 0
coffee = 0

i = 0
while i < n:
    if line[i] == "1":
        coffee = 3
    else:
        coffee -= 1
    if coffee > 0:
        awake += 1
    i = i + 1

print(awake)