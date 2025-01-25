width, partitions = map(int,input().split())
rooms = input().split()
prev = 0
numbers = []
i = 0
while i < partitions:
    curr = int(rooms[i])
    numbers.append(curr - prev)
    prev = curr
    i = i + 1
numbers.append(width - int(rooms[-1]))
numbers.sort()
room = []
i = 0
while i + 1 < len(numbers):
    j = i + 1
    while j < len(numbers):
        room.append(numbers[i] + numbers[j])
        j = j + 1
    room.append(numbers[i])
    i = i + 1
print(sorted(room))