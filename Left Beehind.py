s = input()
while s != "0 0":
    sweet, sour = map(int, s.split())
    if sweet + sour == 13:
        print("Never speak again.")
    elif sweet > sour:
        print("To the convention.")
    elif sweet == sour:
        print("Undecided.")
    else:
        print("Left beehind.")
    s = input()