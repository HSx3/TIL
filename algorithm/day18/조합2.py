def Combination(n, r, q):
    if r == 0:
        return 1
    else:
        if n < r:
            return 0
        else:
            # T[r-1] = A[n-1]
            # Combination(n-1, r-1, q)
            # Combination(n-1, r, q)
            return Combination(n-1, r-1, q) + Combination(n-1, r, q)

def myprint(q):
    while q != 0:
        q = q-1
        print(" %d" % (T[q]), end='')
    print("")


A = [1, 2, 3, 4]
T = [0] * 3

print(Combination(50, 3, 3))    # q : 출력 시작점 (T의 인덱스)