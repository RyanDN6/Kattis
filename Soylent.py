n = int(input())
i = 0
while i < n:
    m = int(input())
    if m % 400 == 0:
        print(m // 400)
    else:
        print((m // 400) + 1)
    i = i + 1