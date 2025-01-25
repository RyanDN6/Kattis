s = input()
t = input()
code = {}

i = 0
while i < len(s):
    code[str(1001 + i)[1:]] = s[i]
    i = i + 1

decode = ""
i = 0
while i < len(t) // 3:
    id = t[i] + t[i + 1] + t[i + 2]
    decode = decode + code[id]
    i = i + 3
print(decode)
