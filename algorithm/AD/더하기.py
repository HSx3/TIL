import sys
sys.stdin = open("더하기_input.txt")

def DFS(no, nsum):
    global flag
    if nsum == K:
        flag = 1
        return
    if nsum>K or flag:
        return
    if no>=N:
        return

    rec[no] = di[no]
    DFS(no+1, nsum+di[no])
    rec[no] = 0
    DFS(no+1, nsum)


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    di = list(map(int, input().split()))
    flag = 0
    rec = [0] * N
    DFS(0, 0)
    if flag:
        print("YES")
    else:
        print("NO")



'''
def johab(no, nsum):
    global flag
    if nsum > K: return
    if no >= N:
        if nsum == K: flag = 1
        return
    a[no] = data[no]
    johab(no + 1, nsum + data[no])
    a[no] = 0
    johab(no + 1, nsum)

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    a = [0] * N
    flag = 0
    johab(0, 0)
    if flag: print('YES')
    else: print('NO')
'''