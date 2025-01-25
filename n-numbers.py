n = int(input())
odd1 = 0
odd2 = 0
tmp = 0

i = 0
while i < n:
    m = int(input())
    if m % 2 == 1:
        if odd1 == 0:
            odd1 = m
        elif odd2 == 0:
            odd2 = m
        else:
            odd2 = tmp
            odd2 = m
            odd1 = tmp
    i = i + 1

print(odd2, odd1)