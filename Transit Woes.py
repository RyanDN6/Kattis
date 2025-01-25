start, end, transits = map(int, input().split())
walking = list(map(int, input().split()))
buses = list(map(int, input().split()))
interval = list(map(int, input().split()))

time = start

i = 0
try:
    
    while time <= end:
        time += walking[i]
        
        while time % interval[i] != 0:
            time += 1
        
        time += buses[i]
        i += 1

except IndexError:
    pass

if time <= end:
    print("yes")
else:
    print("no")