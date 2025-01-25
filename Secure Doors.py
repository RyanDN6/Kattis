n = int(input())
entry = []

i = 0
while i < n:
    s = input().split()
    if s[0] == "entry":
        if s[1] not in entry:
            entry.append(s[1])
            print(s[1], "entered")
        else:
            print(s[1], "entered", "(ANOMALY)")
    else:
        if s[1] in entry:
            entry.remove(s[1])
            print(s[1], "exited")
        else:
            print(s[1], "exited", "(ANOMALY)")
    i = i + 1