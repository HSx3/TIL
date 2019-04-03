import sys
sys.stdin = open("NQUEEN_input.txt")

dr = [-1, -1, -1]
dc = [-1, 0, 1]

def check(r, c):
    # 현재 좌표에 퀸을 놓을 수 있는지 여부 체크
    for i in range(3):  # 3방향
        for k in range(1, N):   # 1배, 2배 ... 증감치의 배수계산
            nr = r + dr[i]*k
            nc = c + dc[i]*k
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break
            if arr[nr][nc] == 1:
                return 0    # 놓을 수 없음, 실패
    return 1    # 놓을 수 있음, 성공

def DFS(no):    # 현재 행에서 모든 열에 퀸을 놓아보는 경우
    global sol
    if no >= N:
        sol += 1
        return
    for i in range(N):  # 열
        if check(no, i):    # 퀸을 놓을 수 있으면
            arr[no][i] = 1 # 퀸 놓기
            DFS(no+1)
            arr[no][i] = 0 # 퀸 빼기

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
sol = 0
DFS(0)  # 0행부터 시작
print(sol)