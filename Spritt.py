line = input()
a = line.split()[0]
b = line.split()[1]
a = int(a)
b = int(b)

total = 0

i = 0
while i < a:
    classroom = int(input())
    total = total + classroom
    i = i + 1

if total <= b:
    print("Jebb")
else:
    print("Neibb")