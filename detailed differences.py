n = int(input())

i = 0
while i < n:
    line1 = input()
    line2 = input()
    j = 0
    diff = ""
    while j < len(line1):
        if line1[j] == line2[j]:
            diff = diff + "."
        else:
            diff = diff + "*"
        j = j + 1
    diff = diff + "\n"
    print(line1)
    print(line2)
    print(diff)
    i = i + 1