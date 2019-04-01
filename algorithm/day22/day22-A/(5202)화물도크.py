import sys
sys.stdin = open('(5202)화물도크_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N =int(input())
    t = [list(map(int, input().split())) for i in range(N)]
    t.sort(key=lambda x : x[1])                 # 종료 시간 순으로 정렬
    cnt = 0                                     # 작업수
    end = 0                                     # 앞 작업의 종료 시간
    for i in range(N):                          # 모든 작업에 대해
        if end <= t[i][0]:                      # 앞 작업 이후에 시작하면
            cnt += 1                            # 작업을 추가하고
            end = t[i][1]                       # 종료시간을 새 작업으로 수정
    print('#{} {}'.format(tc, cnt))
