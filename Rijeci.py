n = int(input())
prev = 0
curr = 1
i = 1
while i < n:
    tmp = curr
    curr = curr + prev
    prev = tmp
    i = i + 1
print(prev, curr)