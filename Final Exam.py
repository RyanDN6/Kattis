n = int(input())
s = ""
i = 0
while i < n:
    t = input()
    s += t
    i = i + 1

grade = 0

i = 0
while i < n - 1:
    if s[i] == s[i + 1]:
        grade += 1
    i = i + 1
print(grade)