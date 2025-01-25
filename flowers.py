flowers = int(input())
type = 0
rows = 1



if flowers % 5 == 0:
    num_rows = flowers // 5
    print(num_rows)
    print("DA")
else:
    num_rows = (flowers // 5) + 1
    print(num_rows)
    print("NU")


while flowers > 0:
    flowers = flowers - (5 * rows)
    rows += 1
    type += 1

if type % 2 == 1:
    print("ROSES")
else:
    print("SUNFLOWERS")