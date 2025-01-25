s = input()
cup = 1

i = 0
while i < len(s):
    if s[i] == "A":
        if cup == 1:
            cup = 2
        elif cup == 2:
            cup = 1
    elif s[i] == "B":
        if cup == 2:
            cup = 3
        elif cup == 3:
            cup = 2
    else:
        if cup == 3:
            cup = 1
        elif cup == 1:
            cup = 3
    i = i + 1

print(cup)