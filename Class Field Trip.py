a = input()
b = input()
c = a + b
my = []
i = 0
while i < len(c):
    my.append(c[i])
    i = i + 1

my.sort()
sorted = ""
i = 0
while i < len(my):
    sorted += my[i]
    i += 1
print(sorted)