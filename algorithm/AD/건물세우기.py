import sys
sys.stdin = open("건물세우기_input.txt")

def DFS(no, nsum):
    global nmin
    if nsum > nmin:
        return
    if no >= n:
        # for i in range(n):
        #     print(rec[i], end=' ')
        # print(nsum)
        if nsum < nmin:
            nmin = nsum
        return
    for i in range(n):
        if chk[i]:
            continue
        chk[i] = 1
        rec[no] = data[no][i]
        DFS(no + 1, nsum + data[no][i])
        chk[i] = 0


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
rec = [0] * n
chk = [0] * n
nmin = 987654321
DFS(0, 0)
print(nmin)