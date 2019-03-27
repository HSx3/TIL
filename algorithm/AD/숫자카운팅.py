import sys
sys.stdin = open("숫자카운팅_input.txt")

def lowerSearch(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        # data가 mid번째값이면 왼쪽영역 재탐색
        if data == arr[m]:
            sol = m
            e = m-1
        # data가 mid번째보다 크면 오른쪽영역 재탐색
        elif data > arr[m]:
            s = m+1
        # data가 mid번째보다 작으면 왼쪽영역 재탐색
        else:
            e = m-1
    return sol # 못찾았으므로 -1 리턴

def upperSearch(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        # data가 mid번째값이면 오른쪽영역 재탐색
        if data == arr[m]:
            sol = m
            s = m+1
        # data가 mid번째보다 크면 오른쪽영역 재탐색
        elif data > arr[m]:
            s = m+1
        # data가 mid번째보다 작으면 왼쪽영역 재탐색
        else:
            e = m-1
    return sol


N = int(input())
arr = list(map(int, input().split()))
T = int(input())
Tarr = list(map(int, input().split()))

for i in range(T):
    lo = lowerSearch(0, N-1, Tarr[i])
    if lo >= 0:
        up = upperSearch(0, N-1, Tarr[i])
        print(up-lo+1, end=' ')
    else:
        print(0, end=' ')