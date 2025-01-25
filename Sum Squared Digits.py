def SSD(b, n):

    decimal = n
    base = ""
    code = "0123456789abcdef"

    while decimal != 0:
        base += code[decimal % b]
        decimal //= b

    n = base[::-1]

    sum = 0
    for i in range(len(n)):
        digit = code.index(n[i])
        sum += digit * digit
    
    return sum


n = int(input())

for i in range(n):
    k, b, n = map(int, input().split())
    print(k, SSD(b, n))