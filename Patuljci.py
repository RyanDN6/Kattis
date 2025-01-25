i = 0
total = 0
data = []
while i < 9:
    n = int(input())
    total += n
    data.append(n)
    i = i + 1
over = total - 100
i = 0
while i < 9:
    if over - data[i] in data:
        data.remove(over - data[i])
        data.pop(i)
        break
    i = i + 1

i = 0
while i < len(data):
    print(data[i])
    i = i + 1