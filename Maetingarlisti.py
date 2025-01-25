n, r, c = map(int, input().split())

students = []
for i in range(r):
    students.append(input().split())

attendence = []

for i in range(r):
    a = []
    for j in range(c):
        a.append(input())
    attendence.append(a)

for i in range(r):
    if students[i] == attendence[i]:
        print("left")
    else:
        print("right")