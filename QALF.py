periods = int(input())
total = 0

i = 0
while i < periods:
    period = input().split()
    quality = float(period[0])
    years = float(period[1])
    total = total + (quality * years)
    i = i + 1

print(total)
