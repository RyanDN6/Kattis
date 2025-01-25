s = input()
vowels = ["a","A","e","E","i","I","o","O","u","U"]
count = 0

i = 0 
while i < len(s):
    if s[i] in vowels:
        count += 1
    i += 1

print(count)