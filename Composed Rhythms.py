n = int(input())

if n == 3:
    print(1)
    print(3)

elif n % 2 == 0:

    print(n // 2)

    for i in range(1, n // 2):
        print(2, end=" ")
    
    print(2)

else:
    print(n // 2)
    print(3, end=" ")

    for i in range(2, n // 2):
        print(2, end=" ")
    
    print(2)