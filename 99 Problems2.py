n, q = input().split()
n = int(n)
q = int(q)
problems = input().split()

i = 0
while i < q:
    line = input().split()
    d = int(line[1])
    j = 0
    if line[0] == "1":
        while j < len(problems) and d >= int(problems[j]):
            j = j + 1
    else:
        while j < len(problems) and d < int(problems[j]):
            j = j + 1
    if j == len(problems):
        print(-1)
    else:
        print(problems[j])
        problems.pop(j)
    i = i + 1

