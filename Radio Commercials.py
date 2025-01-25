c, p = map(int, input().split())

commercials = input().split()
profit = []

for i in range(0, c):
    profit.append(int(commercials[i]) - p)

while int(profit[0]) < 1:
    profit.pop(0)

money = 0

boolean = True
while boolean:

    j = 0
    total = 0

    while j < len(profit):
        total += profit[j]
        j = j + 1

    if total > 0:
        money += profit[0]
        profit.pop(0)
    else:
        boolean = False

print(money)