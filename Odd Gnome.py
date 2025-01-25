n = int(input())
i = 0
while i < n:
    s = input().split()
    list = s[1:]
    gnomes = int(s[0])
    j = 0
    while j < gnomes:
        if int(list[j]) != int(list[j + 1]) - 1:
            print(j + 2)
            break
        j = j + 1
    i = i + 1
