s1 = input()
s2 = ""
i = 1

while len(s2) < len(s1):
    s2 += str(i)
    i += 1

if s2 == s1:
    print(i - 1)
else:
    print("-1")
