import sys
sys.stdin = open("미로탈출로봇_input.txt")

def BFS():
    que = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 1. 시작점을 큐에 저장(방문표시)
    que.append((sr, sc, 0))     # 행, 열, 시간 큐에 저장
    arr[sr][sc] = 1             # 맵에 방문표시
    while que:                  # 큐가 있으면 반복
        # 2. 큐에서 데이터 읽기
        r, c, time = que.pop(0)

        if r == er and c == ec:
            return time
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 3-1. 맵의 범위 체크
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            # 3-2. 연결점을 찾아 큐에 저장(방문표시)
            if arr[nr][nc] != 0:    # 길이 아니면 스킵
                continue
            arr[nr][nc] = 1  # 맵에 방문표시
            que.append((nr, nc, time+1))
    return -1 # 4. 큐가 빈 상태


C, R = map(int, input().split())                # x = C, y = R
sc, sr, ec, er = map(int, input().split())
sc -= 1
sr -= 1
ec -= 1
er -= 1
arr = [list(map(int, input())) for _ in range(R)]
print(BFS())