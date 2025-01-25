n = int(input())
count = input().split()

boolean = True

curr = 1

for c in count:
    if c == "mumble":
        curr += 1
    else:
        if int(c) != curr:
            boolean = False
            break
        curr += 1

if boolean == False:
    print("something is fishy")
else:
    if curr - 1 == n:
        print("makes sense")
    else:
        print("something is fishy")