capacity, crowds = map(int, input().split())

people = input().split()
total = 0
i = 0
while capacity > total and i < crowds:
    total += int(people[i])
    i = i + 1

print(crowds - i)