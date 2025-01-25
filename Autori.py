s = input()
t = ""

i = 0
while i < len(s):
    if s[i] >= "A" and s[i] <= "Z":
        t = t + s[i]
    i = i + 1

print(t)