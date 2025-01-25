line = input()
maximum, truck, n = line.split()
maximum = int(maximum)
truck = int(truck)
n = int(n)
total = 0
capacity = (maximum - truck) 

items = input().split()

i = 0
while i < n:
    item = int(items[i])
    total += item
    i = i + 1

print(int(capacity - total))
