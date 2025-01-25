redact = input()
message = input().split()

i = 0
while i < len(message):
    j = 0
    while j < len(redact):
        if redact[j] in message[i]:
            message[i] = "*" * len(message[i])
            break
        j = j + 1
    i = i + 1

print(" ".join(message))