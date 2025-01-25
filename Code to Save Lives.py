n = int(input())
i = 0
while i < n:
    line1 = input().split()
    num1 = int("".join(line1))
    line2 = input().split()
    num2 = int("".join(line2))
    sum = str(num1 + num2)
    j = 0
    output = ""
    while j < len(sum):
        output += sum[j] + " "
        j = j + 1
    print(output.strip())
    i = i + 1