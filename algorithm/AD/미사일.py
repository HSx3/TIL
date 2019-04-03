import sys
sys.stdin = open("미사일_input.txt")

def clear(no):      # 현재 군함위치 no에서 반경이내 에너지 모두 차감
    for i in range(N):  # i, 주변에 있는 군함
        temp = abs(arr[no][0] - arr[i][0]) + abs(arr[no][1] - arr[i][1])
        if temp <= R:   # 반경이내이면
            arr[i][2] -= P

def update(no):     # 현재 군함위치에서 반경이내 에너지 모두 복원
    for i in range(N):  # i, 주변에 있는 군함
        temp = abs(arr[no][0] - arr[i][0]) + abs(arr[no][1] - arr[i][1])
        if temp <= R:   # 반경이내이면
            arr[i][2] += P

def DFS(no):        # no, 미사일
    # 현재 미사일을 모든 군함에 쏘아보는 경우의 수 시도
    global sol

    if no == M:
        cnt = 0     # 남아있는 군함의 수
        for i in range(N):
            if arr[i][2] > 0:
                cnt += 1
        if cnt < sol:
            sol = cnt
        return
    for i in range(N):  # i, 군함
        if arr[i][2] <= 0:
            continue    # 단, 군함이 침몰하지 않은 군함에만 시도
        clear(i)        # 현재 군함반경이내 모든 군함에너지 차감
        DFS(no+1)       # 다음 미사일로
        update(i)       # 현재 군함반경이내 모든 군함에너지 복원

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))     # 열, 행, 에너지
M, P, R = map(int, input().split())     # 미사일개수, 화력, 화력이 미치는 범위
sol = 16
DFS(0)  # 미사일 0번부터 시작
print(sol)