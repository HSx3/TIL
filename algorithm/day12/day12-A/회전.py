import sys
sys.stdin = open("회전_input.txt","r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    for i in range(M):
        t = Q.pop(0)
        Q.append(t)
    print(f"#{tc+1} {Q.pop(0)}")