import sys
sys.stdin = open("배부른 돼지.txt")

data = int(input())
YoN = [list(map(str, input().split())) for _ in range(data)]

for_Y = []
for_Yt = []
for_N = []
for_Nt = []

for i in YoN:
    if 'Y' in i:
        for_Y.append(i)
        for_Yt.append(i[0])
    else:
        for_N.append(i)
        for_Nt.append(i[0])

if len(for_Y) == 0:
    print('F')

else:
    for i in for_Yt:
        for j in for_Nt:
            if i < j:
                print('F')
                break
        else:
            if int(sorted(for_Y)[0][0]) >= 10 or int(sorted(for_Y)[0][0]) <= 2:
                print('F')
                break
            else:
                print(sorted(for_Y)[0][0])
                break

'''
N=int(input())
Ymin=9
Nmax=2
if N==0:
    print('F')
else:
    for i in range(N):
        cnt, yn = input().split()
        cnt = int(cnt)
        if yn is 'Y':
            if Ymin > cnt: Ymin = cnt
        else:
            if Nmax < cnt: Nmax = cnt
    
'''