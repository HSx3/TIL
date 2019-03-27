import sys
sys.stdin = open("도약_input.txt")

def lowerSearch(s, e, data):
    # data 이상에서 가장 작은 값의 위치 리턴
    sol = -1
    while s<=e:
        m = (s+e) // 2
        if arr[m] >= data:  # 데이터 이상이면 왼쪽영역 재탐색
            sol = m
            e = m-1
        else:
            s = m+1         # 오른쪽 탐색
    return sol

def upperSearch(s, e, data):
    # data 이상에서 가장 큰 값의 위치 리턴
    sol = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] <= data:  # 데이터 이하이면 오른쪽영역 재탐색
            sol = m
            s = m+1
        else:
            e = m-1
    return sol
    # main
N = int(input())
arr = []
for i in range(N):
    i = int(input())
    arr.append(i)

arr.sort()
cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        start = arr[j] + (arr[j] - arr[i])
        end = arr[j] + (arr[j] - arr[i])*2
        lo = lowerSearch(j+1, N-1, start)
        # 예외 : 못찾았거나 2배이상 초과시 스킵
        if lo == -1 or arr[lo] > end:
            continue
        up = upperSearch(j+1, N-1, end)
        cnt += (up-lo+1)
print(cnt)