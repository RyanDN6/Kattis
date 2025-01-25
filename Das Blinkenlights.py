a, b, total = map(int, input().split())
i = a
j = b

alist = []
blist = []

while a <= total:
    alist.append(a)
    a += i

while b <= total:
    blist.append(b)
    b += j


boolean = True
for c in alist:
    if c in blist:
        boolean = False
        break

if boolean == False:
    print("yes")
else:
    print("no")