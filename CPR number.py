s = input()
number = s[:-5] + s[-4:]
total = 0

total = total + int(number[0]) * 4
total = total + int(number[1]) * 3
total = total + int(number[2]) * 2
total = total + int(number[3]) * 7
total = total + int(number[4]) * 6
total = total + int(number[5]) * 5
total = total + int(number[6]) * 4
total = total + int(number[7]) * 3
total = total + int(number[8]) * 2
total = total + int(number[9]) * 1

if total % 11 == 0:
    print(1)
else:
    print(0)
