n = int(input())

i = 0
while i < n:
    line = input()
    noAd, Ad, cost = line.split()
    noAd = int(noAd)
    Ad = int(Ad)
    cost = int(cost)
    if Ad - cost > noAd:
        print("advertise")
    elif Ad - cost < noAd:
        print("do not advertise")
    else:
        print("does not matter")
    i = i + 1