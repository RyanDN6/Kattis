line = input()
a,b,c = line.split()
a = int(a)
b = int(b)
c = int(c)

if a + b == c:
    print("correct!")
else:
    print("wrong!")