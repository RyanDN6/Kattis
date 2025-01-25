a, b = map(int, input().split())

if a > b:
    if a - b == 1:
        print(f'Dr. Chaz needs 1 more piece of chicken!')
    else:
        print(f'Dr. Chaz needs {a - b} more pieces of chicken!')
else:
    if b - a == 1:
        print(f'Dr. Chaz will have 1 piece of chicken left over!')
    else:
        print(f'Dr. Chaz will have {b - a} pieces of chicken left over!')