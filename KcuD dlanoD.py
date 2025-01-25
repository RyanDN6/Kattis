line = input().split()
a = line[0]
a1 = ""
b1 = ""

i = 0
while i < len(a):
    if a[-i - 1] == "2":
        a[-i - 1] = "5"
    elif a[-i - 1] == "5":
        a[-i - 1] = "2"
    a1 += a[-1 - i]
    i = i + 1
print(a1)