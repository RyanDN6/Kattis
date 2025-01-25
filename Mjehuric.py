a = input().split()
line = ""
while line != "1 2 3 4 5":
    if a[0] > a[1]:
        tmp = a[0]
        a[0] = a[1]
        a[1] = tmp

    elif a[1] > a[2]:
        tmp = a[1]
        a[1] = a[2]
        a[2] = tmp

    elif a[2] > a[3]:
        tmp = a[2]
        a[2] = a[3]
        a[3] = tmp

    else:
        tmp = a[3]
        a[3] = a[4]
        a[4] = tmp
    line = " ".join(a)
    print(line)