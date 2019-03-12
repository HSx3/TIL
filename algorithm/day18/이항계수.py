# DP를 이용한 이항계수 계산

def bino(n, k):
    # B[][]
    for i in range(n+1):
        for j in range(i+1):
            if j==0 or j==i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]

    return B[n][k]


B = [[0]*5 for _ in range(5)]
print(bino(4, 3))