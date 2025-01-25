n = int(input())
factors = 0
i = 2
while i < (n // 2) + 1:
    if n % i == 0:
        factors += 1
        n = n // i
        i = 2
    else:
       i = i + 1
print(factors + 1)
        