def encrypt(s):
    out = ""

    i = 0
    while i < len(s):
        total = 1
        start = s[i]
        j = i + 1

        while j < len(s) and s[j] == start:
            total += 1
            j += 1

        out += start + str(total)


        i = j

    return out   

def decrypt(s):
    out = ""

    for i in range(0, len(s), 2):
        out += s[i] * int(s[i + 1])
    
    return out

line = input().split()

if line[0] == "E":
    print(encrypt(line[1]))
else:
    print(decrypt(line[1]))