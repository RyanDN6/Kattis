n = h = l = int(input())
high = 0
low = 0

while str(h)[-2:] != "99":
    h = h + 1
    high += 1

while str(l)[-2:] != "99" and l != -1:
    l = l - 1
    low += 1

if l == -1:
    print(h)
else:
    if high == low:
        print(h)
    elif high < low:
        print(h)
    else:
        print(l)