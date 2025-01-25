n = int(input())

students = []

for i in range(n):
    students.append(sorted(list(map(int, input().split()))))

seen = []
max = [n, 0]
for i in range(n):
    count = 0
    
    if students[i] not in seen:
        for j in range(i + 1, n):
            
            if students[i] == students[j]:
                count += 1

        popularity = n - count
        seen.append(students[i])

        if popularity <= max[0]:
            max[0] = popularity
            max[1] = students[i]
