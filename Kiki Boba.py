word = input()
boba = 0
kiki = 0

i = 0
while i < len(word):
    if word[i] == "b":
        boba += 1
    if word[i] == "k":
        kiki += 1
    i += 1
    
if boba > kiki:
    print("boba")
elif kiki > boba:
    print("kiki")
elif boba == 0 and kiki == 0:
    print("none")
else:
    print("boki")