n = int(input())
i = 0
while i < n:
    problem = input()
    if "=" in problem:
        print("skipped")
    else:
        a, b = map(int,problem.split("+"))
        print(a + b)
    i = i + 1