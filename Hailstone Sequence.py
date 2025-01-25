n = int(input())
seq = 0
while n != 1:
    seq += 1
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3) + 1

print(seq + 1)