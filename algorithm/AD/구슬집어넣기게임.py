import sys
sys.stdin = open("구슬집어넣기게임_input.txt")


def BFS():
    global Rr, Rc, Br, Bc, Hr, Hc
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    que = [(Rr, Rc, Br, Bc, 0)]
    chk[Rr][Rc][Br][Bc] = 1

    while que:
        Rr, Rc, Br, Bc, cnt = que.pop(0)

        # 기울임 횟수가 10회를 넘어서면 게임 실패
        for i in range(4):
            Rnr, Rnc = Rr+dr[i], Rc+dc[i]
            Bnr, Bnc = Br+dr[i], Bc+dc[i]

            # 이동방향에 벽이 있는 구슬은 움직일 수 없다. 다음 위치가 벽이면 현재 위치로
            if arr[Rnr][Rnc] == '#':
                Rnr, Rnc = Rr, Rc
            if arr[Bnr][Bnc] == '#':
                Bnr, Bnc = Br, Bc

            # 빨간 구슬과 파란 구슬이 같은 위치이면 스킵
            if arr[Rnr][Rnc] == arr[Bnr][Bnc]:
                continue

            # 파란 구슬이 목표 구멍이면 스킵
            if Bnr == Hr and Bnc == Hc:
                continue

            # 빨간 구슬이 목표 구멍이면 리턴
            if Rnr == Hr and Rnc == Hc:
                return cnt+1

            # 방문했었으면 스킵
            if chk[Rnr][Rnc][Bnr][Bnc] == 1:
                continue

            # 큐에 저장하고 방문표시
            que.append((Rnr, Rnc, Bnr, Bnc, cnt+1))
            chk[Rnr][Rnc][Bnr][Bnc] = 1


T = int(input())
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
chk = [[[[0]*C for _ in range(R)] for _ in range(C)] for _ in range(R)]
Rr, Rc, Br, Bc, Hr, Hc = 0, 0, 0, 0, 0, 0

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'R':
            Rr, Rc = i, j
        elif arr[i][j] == 'B':
            Br, Bc = i, j
            arr[i][j] = '.'
        elif arr[i][j] =='H':
            Hr, Hc = i, j
            arr[i][j] = '.'
print(BFS())