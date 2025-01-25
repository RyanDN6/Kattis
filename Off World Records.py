jumps, curr, prev = map(int, input().split())

records = 0
for i in range(jumps):
    jump = int(input())

    if jump > curr + prev:
        records += 1
        prev = curr
        curr = jump

print(records)