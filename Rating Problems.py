line = input()
judges, n = line.split()
judges = int(judges)
n = int(n)
total = 0

i = 0
while i < n:
    rating = int(input())
    total += rating
    i = i + 1

min = (total + (-3 * (judges - n))) / judges
max = (total + (3 * (judges - n))) / judges

print(min, max)