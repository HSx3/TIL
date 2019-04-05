import sys
sys.stdin = open("건물세우기_2.txt")

def DFS(no, nsum):
    global nmin
    if nmin < nsum:
        return
    if no >= n:
        if nsum < nmin:
            nmin = nsum
        # for i in range(n):
        #     print(rec[i], end=' ')
        # print()
        return

    for i in range(n):
        if check[i]:
            continue
        check[i] = 1
        rec[no] = data[no][i]
        DFS(no+1, nsum + data[no][i])
        check[i] = 0



n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

nmin = 987654321
rec = [0] * n
check = [0] * n

DFS(0, 0)
print(nmin)