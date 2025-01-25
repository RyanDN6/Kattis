s = input()

i = 0
while i < len(s):
    if s[i] == "s" and s[i - 1] == "s" or s[i] == "S" and s[i - 1] == "S":
        print("hiss")
        break
    else:
       i = i + 1

if i == len(s):
    print("no hiss")