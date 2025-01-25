n = int(input())
line = input().split()
s = ""

i = 0
while i < n:
    word = line[i]
    if word[0] <= "Z" and word[0] >= "A":
        s = s + word[0]
    i = i + 1
print(s)