line = input().split()
n = int(line[0])
suit = line[1]

total = 0

i = 0
while i < (n * 4):
    card = input()
    if card[0] == "A":
        total += 11
    elif card[0] == "K":
        total += 4
    elif card[0] == "Q":
        total += 3
    elif card[0] == "J":
        if card[1] == suit:
            total += 20
        else:
            total += 2
    elif card[0] == "T":
        total += 10
    elif card[0] == "9":
        if card[1] == suit:
            total += 14
    i = i + 1

print(total)