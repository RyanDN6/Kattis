mb = int(input())
n = int(input())
total = mb

i = 0
while i < n:
    m = int(input())
    total += (mb - m)
    i = i + 1

print(total)