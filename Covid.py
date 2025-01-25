s = input()

i = 0
while i < len(s):
    if s[i] == "V" and s[i - 1] == "O" and s[i - 2] == "C":
        print("Veikur!")
        break
    else:
        i = i + 1

if len(s) == i:
    print("Ekki veikur!")