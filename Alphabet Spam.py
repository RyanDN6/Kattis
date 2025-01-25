line = input()
length = len(line)
spaces = 0
lower = 0
upper = 0
symbols = 0
i = 0
while i < len(line):
    if line[i] == "_":
        spaces += 1
    elif line[i] <= "Z" and line[i] >= "A":
        upper += 1
    elif line[i] <= "z" and line[i] >= "a":
        lower += 1
    else:
        symbols += 1
    i = i + 1

print(spaces / length)
print(lower / length)
print(upper / length)
print(symbols / length)