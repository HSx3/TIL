import sys
sys.stdin = open("NQUEEN_input.txt")


def DFS(no):    # 현재 행에서 모든 열에 퀸을 놓아보는 경우
    global sol
    if no >= N:
        sol += 1
        return
    for i in range(N):
        if chk1[i]:      # 세로방향 체크
            continue
        if chk2[no + i]:      # 오른쪽대각선방향 체크
            continue
        if chk3[(N-1)-(no-i)]:      # 왼쪽대각선방향 체크
            continue
        chk1[i] = chk2[no+i] = chk3[(N-1)-(no-i)] = 1
        DFS(no+1)
        chk1[i] = chk2[no+i] = chk3[(N-1)-(no-i)] = 0


N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
chk1 = [0] * (N + 1)
chk2 = [0] * (N*2 + 1)
chk3 = [0] * (N*2 + 1)
sol = 0
DFS(0)  # 0행부터 시작
print(sol)