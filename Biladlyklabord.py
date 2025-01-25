s = " " + input()
prev = s[0]
new = []

for i in range(1, len(s)):
    curr = s[i]
    if curr != prev:
        new.append(s[i])
    
    prev = curr

print("".join(new))