n = int(input())
s = input()
numbers = []
i = 0
while i < n:
    number = ""
    if s[i] <= "9" and s[i] >= "0":
        j = i
        while j < n and s[j] <= "9" and s[j] >= "0":
            j = j + 1
        numbers.append(int(s[i:j]))
        i = j
    i = i + 1

print(sorted(numbers)[-1])