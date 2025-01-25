n = int(input())
knots = input().split()
learnt = input().split()

i = 0
while i < len(knots):
    if knots[i] not in learnt:
        print(knots[i])
        break
    else:
        i = i + 1
