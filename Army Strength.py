import sys
lines = sys.stdin.readlines()
rounds = lines[0].strip()
a = []

i = 0
while i < int(rounds):
    army = lines[2 + (i * 4)].strip()
    godzilla = lines[3 + (i * 4)].strip().split()
    mech = lines[4 + (i * 4)].strip().split()
    god = 0
    while god < len(godzilla):
        a.append(int(godzilla[god]))
        god += 1
    god = 0
    while god < len(mech):
        a.append(int(mech[god]))
        god += 1
    a.sort(reverse=True)

    if str(a[0]) in godzilla:
        print("Godzilla")
    else:
        print("MechaGodzilla")
    a = []
    i = i + 1
