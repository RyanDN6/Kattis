n, zoom = map(int,input().split())

data = input().split()
new = []
i = 0
while i < n:
    if (i + 1) % zoom == 0:
        new.append(data[i])        
    i = i + 1
print(" ".join(new))