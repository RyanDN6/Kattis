m = int(input())

words = input().split()

n = int(input())

trans = {}

for i in range(n):
    s = input().split()
    trans[s[0]] = s[1]

for i in range(m):
    words[i] = trans[words[i]]

print(" ".join(words))