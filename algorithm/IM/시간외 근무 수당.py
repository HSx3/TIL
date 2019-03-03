import sys
sys.stdin = open("시간외 근무 수당.txt")

sum = 0
time = 0
gross = 0

for i in range(5):
    s, e = map(float, input().split())
    time = e-s
    if time <= 1:
        sum += 0
    elif time >= 5:
        sum += 4
    else:
        sum += time - 1

if sum >= 15:
    sum = (sum*2)*5000*0.95
    print(int(sum))

elif sum <= 5:
    sum = (sum*2)*5000*1.05
    print(int(sum))

else:
    print(int((sum/0.5)*5000))