# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 부분집합의 합 10 출력하기
count = 0
total = 0
N = 10
A = [0 for _ in range(N)]
# data = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printSet(n, sum):
    global count
    if sum == 10:
        count += 1
        print('%d : ' % count, end='')
        for i in range(n):
            if A[i] == 1:
                print('%d ' % data[i], end='')
        print()

def powerset(n, k, sum):         # n: 원소의 개수, k: 현재 depth
    global total
    if sum > 10:
        return
    total += 1
    if n == k:              # Basis Part
        printSet(n, sum)
    else:                   # Inductive Part
        A[k] = 1            # k번 요소 o
        powerset(n, k+1, sum + data[k])    # 다음 요소 포함 여부 결정
        A[k] = 0            # k번 요소 x
        powerset(n, k+1, sum)    # 다음 요소 포함 여부 결정

powerset(N, 0, 0)
print("호출회수 : {}".format(total))