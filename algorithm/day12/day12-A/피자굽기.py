def solve():
    global N, M
    Q = []
    for i in range(1, N+1):  # 화덕에 N개를 채움
        Q.append(i)
    idx = N + 1              # 아직 화덕에 넣지 않은 피자
    t = 0
    while len(Q) != 0:
        t = Q.pop(0)         # 입구로 돌아온 피자를 꺼내 치즈 확인
        if arr[t]//2 != 0:   # 치즈가 남아 있으면
            arr[t] //= 2
            Q.append(t)      # 다시 넣기
        elif idx <= M:       # 치즈가 녹았으면 남은 피자를 넣음
            Q.append(idx)
            idx += 1
    return t                 # 마지막으로 나온 피자 번호

import sys
sys.stdin = open("피자굽기_input.txt", "r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split()) #화덕, 피자
    arr = [0] + list(map(int, input().split()))
    print(f"#{tc+1} {solve()}")