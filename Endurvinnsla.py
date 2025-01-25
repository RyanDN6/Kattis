city = input()
p = float(input())
n = int(input())
a = b = 0

for i in range(0, n):
    s = input()
    if s == "plast":
        a += 1
    else:
        b += 1

c = b/n

if c <= p:
    print("Jebb")
else:
    print("Neibb")