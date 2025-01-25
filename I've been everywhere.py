n = int(input())
seen = []

i = 0
while i < n:
    m = int(input())
    j = 0
    count = 0
    while j < m:
        city = input()
        if city not in seen:
            seen.append(city)
            count += 1
        j = j + 1
    print(count)
    i = i + 1