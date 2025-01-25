array = input().split()

while array != sorted(array):
    if array[0] > array[1]:
        temp = array[0]
        array[0] = array[1]
        array[1] = temp
        print(" ".join(array))
        continue
    if array[1] > array[2]:
        temp = array[1]
        array[1] = array[2]
        array[2] = temp
        print(" ".join(array))
        continue
    if array[2] > array[3]:
        temp = array[2]
        array[2] = array[3]
        array[3] = temp
        print(" ".join(array))
        continue
    if array[3] > array[4]:
        temp = array[3]
        array[3] = array[4]
        array[4] = temp
        print(" ".join(array))
        continue