r, c, zr, zc = map(int, input().split())
original = [input().strip() for _ in range(r)]

result = []

for row in original:

    expanded_row = ''.join([char * zc for char in row])
    
    for _ in range(zr):
        result.append(expanded_row)

for line in result:
    print(line)