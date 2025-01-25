n = int(input())

i = 0
while i < n:
    m = int(input())
    line = input().split()
    j = 0
    while j < m:
        k = 0
        while k < m:
            if line[k] == line[j] and k != j:
                k = m + 1
            else:
                k = k + 1
        if k == m:
            print("Case #" + str(i + 1) + ":", line[j])
            j = m
        else:
            j = j + 1
    i = i + 1