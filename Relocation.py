n, requests = map(int, input().split())

companies = list(map(int, input().split()))


for i in range(requests):
    q, a, b = map(int, input().split())

    if q == 1:
        companies[a - 1] = b
    else:
        print(abs(companies[a - 1] - companies[b - 1]))