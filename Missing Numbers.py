n = int(input())
numbers= []

i = 0
while i < n:
    s = int(input())
    numbers.append(s)
    i = i + 1

boolean = False
i = 1
while i < numbers[-1]:
    if i not in numbers:
        print(i)
        boolean = True
    i = i + 1

if boolean == False:
    print("good job")
