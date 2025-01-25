n = int(input())

i = 0
while i < n:
    line = input()
    beats, seconds = line.split()
    beats = int(beats)
    seconds = float(seconds)
    print(str((beats - 1) * (60 / seconds)), str(beats * (60 / seconds)), str((beats + 1) * (60/seconds)))
    i = i + 1