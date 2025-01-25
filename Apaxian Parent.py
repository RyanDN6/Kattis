y, p = input().split()

if y[-1] == "e":
    print(f'{y}x{p}')

elif y[-1] in "aiou":
    print(f'{y[:-1]}ex{p}')

elif y[-2:] == "ex":
    print(y + p)

else:
    print(f'{y}ex{p}')
