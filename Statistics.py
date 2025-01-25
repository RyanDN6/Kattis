import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    line = lines[i].split()
    n = int(line[0])
    sample = line[1:]
    j = 0
    while j < n:
        sample[j] = int(sample[j])
        j = j + 1
    sample.sort()
    x = str(i + 1)
    min = sample[0]
    max = sample[-1]
    range = max - min
    print("Case " + x + ":", str(min), str(max), str(range))
    i = i + 1
