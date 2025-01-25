import math
n = int(input())
line = input().split()
a = int(line[0])
i = 1
while i < n:
    b = int(line[i])
    gcd = math.gcd(a,b)
    print(str(a // gcd) + "/" + str(b // gcd))
    i = i + 1