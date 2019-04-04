import sys
sys.stdin = open("바이러스_input.txt")

def FF(no):
    # 현재 컴퓨터에서 방문하지 않은 연결된 컴퓨터를 따라가면서 방문표시하고 카운트
    # global sol
    # if chk[no] == 0:
    #     chk[no] = 1
    #     sol += 1
    #     for i in range(1, N+1):
    #         if arr[no][i] == 1:
    #             FF(i)
    global sol
    for i in range(1, N+1): # 연결된 컴퓨터(열)
        if arr[no][i] and chk[i] == 0:
            chk[no] = 1
            sol += 1
            FF(i)

N = int(input())
M = int(input())
chk = [0] * (N+1)   # 방문표시
arr = [[0]*(N+1) for _ in range(N+1)]   # 인접행렬
for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = arr[e][s] = 1   # 연결 체크

print(arr)

sol = 0
FF(1)   # 1번 컴퓨터부터 시작
# print(sol-1)
print(sol)