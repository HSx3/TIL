import sys
sys.stdin = open("어디에단어가들어갈수있을까_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited_row = [[0 for _ in range(N)] for _ in range(N)]
    visited_col = [[0 for _ in range(N)] for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(N):
            # 가로
            if data[i][j] == 1 and visited_row[i][j] == 0:
                visited_row[i][j] = 1
                length = 1
                k = j
                while k < N-1:
                    k = k+1
                    if data[i][k] == 1:
                        visited_row[i][k] = 1
                        length += 1
                    elif data[i][k] == 0:
                        break
                if length == K:
                    count += 1

    for i in range(N):
        for j in range(N):
            # 세로
            if data[j][i] == 1 and visited_col[j][i] == 0:
                visited_col[j][i] = 1
                length = 1
                k = j
                while k < N-1:
                    k = k+1
                    if data[k][i] == 1:
                        visited_col[k][i] = 1
                        length += 1
                    elif data[k][i] == 0:
                        break
                if length == K:
                    count += 1

    print('#{} {}'.format(test_case, count))