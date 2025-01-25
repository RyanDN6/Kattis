n = int(input())
courses = {}
seen = []


for i in range(0, n):
    line = input()
    if line not in seen:
        seen.append(line)

for c in seen:
    if c.split()[2] in courses.keys():
        courses[c.split()[2]] += 1
    else:
        courses[c.split()[2]] = 1

for item in courses.keys():
    print(f'{item} {courses[item]}')