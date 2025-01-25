n = int(input())
prevtime, prevspeed = map(int,input().split())
i = 1
data = []
while i < n:
    time, speed = map(int,input().split())
    hours = time - prevtime
    miles = speed - prevspeed
    mph = miles // hours
    data.append(mph)
    prevtime = time
    prevspeed = speed
    i = i + 1

print(sorted(data)[-1])