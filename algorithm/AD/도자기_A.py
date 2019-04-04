import sys
sys.stdin = open("도자기_input.txt")

def DFS(start, cnt):
    global sol
    if cnt == M:
        # for i in range(cnt): print(rec[i], end=' ')
        # print()
        sol += 1
        return
    for i in range(start, N):   # 흙의 재료
        if rec[cnt] == arr[i]: continue # 같은 재료이면 스킵
        rec[cnt] = arr[i]
        DFS(i+1, cnt+1)
    rec[cnt] = 0

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    rec = [0] * N
    sol = 0
    DFS(0, 0)
    print(sol)


'''
def DFS(start, cnt):
    global sol
    if cnt == M:
        # for i in range(cnt):
        #     print(rec[i], end=' ')
        # print()
        sol+=1
        return
    back = 0
    for i in range(start, N):   # 재료
        if back == arr[i]:
            continue
        # if rec[cnt] == arr[i]:  # 같은 재료이면 스킵
        #     continue
        # rec[cnt]=arr[i]
        back=arr[i]
        DFS(i+1, cnt+1)
    rec[cnt] = 0

T = int(input())
for tc in range(1):
    N, M = map(int, input().split())    # N:흙종류, M:흙을섞을수있는개수
    arr = list(map(int, input().split()))
    arr.sort()

    rec = [0]*N
    sol = 0
    DFS(0, 0)
    print(sol)
'''