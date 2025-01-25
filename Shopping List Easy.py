n, m = map(int,input().split())
i = 0
list = input().split()
while i < n - 1:
    line = input().split()
    j = 0
    while j < len(list):
        if list[j] not in line:
            list.pop(j)
            j = j
        else:
            j = j + 1
    i = i + 1
print(len(list))
i = 0
while i < len(list):
    print(sorted(list)[i])
    i = i + 1