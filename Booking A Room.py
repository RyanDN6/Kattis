rooms, n = map(int,input().split())
if rooms == n:
    print("too late")
else:
    booked = []
    i = 0
    while i < n:
        room = int(input())
        booked.append(room)
        i = i + 1
    i = 1
    boolean = True
    while boolean:
        if i not in booked:
            print(i)
            boolean = False
        i = i + 1