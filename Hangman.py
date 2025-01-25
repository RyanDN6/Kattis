word = set(input())
alphabet = input()

count = 0

for i in range(26):
    if alphabet[i] in word:
        word.remove(alphabet[i])
        if len(word) == 0:
            print("WIN")
            break
    else:
        count += 1
        if count == 10:
            print("LOSE")
            break