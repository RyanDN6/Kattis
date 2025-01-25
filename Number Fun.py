n = int(input())

i = 0
while i < n :
    a, b, c = map(int,input().split())
    if a + b == c or a * b == c:
        print("Possible")
    else:
        if a - b == c or b - a == c:
            print("Possible")
        else:
            if a % b == 0 or b % a == 0:
                if a // b == c or b // a == c:
                    print("Possible")
                else:
                    print("Impossible")
            else:
                print("Impossible")
    i = i + 1