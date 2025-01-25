decimal = int(input())
binary = ""

while decimal > 0:
    if decimal % 2 == 1:
        binary += "1"
    else:
        binary += "0"
    decimal //= 2

number = 0

i = 0
while i < len(binary):
    if binary[i] == "1":
        number += 2 ** (len(binary) - i - 1)
    i = i + 1

print(number)