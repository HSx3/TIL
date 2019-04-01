import sys
sys.stdin = open("사람네트워크2_input.txt")

T = int(input())
for tc in range(T):
    data = list(map(int, input().split()))
    n = data.pop(0)
    arr=[]

    for i in range(n):
        arr.append(data[i*n:i*n+n])

    for i in range(n):
        for j in range(n):
            if i==j:continue
            if arr[i][j]:continue
            arr[i][j] = 1001

    for k in range(n):
        for i in range(n):
            if i==k:continue
            for j in range(n):
                if j==k:continue
                if j==i:continue
                arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

    cc=[0]*n
    for i in range(n):
        cc[i]=sum(arr[i])
    print('#{} {}'.format(tc+1, min(cc)))