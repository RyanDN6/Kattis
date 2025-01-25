t, s = map(int, input().split())

t = t * 60

songlist = input().split()
songs = []

for i in range(0, s):
    songs.append(int(songlist[i]))

total = 0
i = 0
try:
    while total < t:
        total += sorted(songs)[i]
        i = i + 1
    print(total - sorted(songs)[i - 1])
except IndexError:
    print(total)