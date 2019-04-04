import sys
sys.stdin = open("해밀턴순환회로_input.txt")

def DFS(city, cnt, hap):
    global sol
    if hap > sol:
        return

    if cnt==N:  # 마지막 도시에서 집으로 가는 최소비용 비교
        if arr[city][0]:    # 단, 집으로 가는 비용이 있는 경우
            if hap + arr[city][0] < sol:
                sol = hap + arr[city][0]
        return

    # 현재 도시에서 비용이 있고 방문안한 도시를 모두 시도하는 경우의 수
    for i in range(1, N):   # 가볼도시(열)
        if arr[city][i] and not chk[i]:
            chk[i] = 1
            DFS(i, cnt+1, hap+arr[city][i])
            chk[i] = 0



# main ----------------------
N = int(input())
rec = [0] * N     # 색상기록
chk = [0] * N
arr = [list(map(int, input().split())) for _ in range(N)]

sol = 100000
DFS(0, 1, 0)    # 첫번째 도시부터 시작, 순회회수 1회, 비용 0원
print(sol)