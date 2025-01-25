n = 10
seen = []

i = 0
while i < n:
    m = int(input())
    if m % 42 not in seen:
        seen.append(m % 42)
    i = i + 1

print(len(seen))
