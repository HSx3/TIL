# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 부분집합의 합 10 출력하기
# count = 0
N = 10
A = [0 for _ in range(N)]
# data = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printSet(n):
    sum = 0
    answer = []
    # global count
    # count += 1
    # print('%d : ' % (count), end='')        # 생성되는 부분 배열의 개수 출력
    for i in range(n):                      # 각 부분 배열의 원소 출력
        if A[i] == 1:                       # A[i]가 1이면 포함된 것이므로 출력
            # print('%d ' % data[i], end='')
            sum += data[i]
            answer.append(data[i])
    if sum == 10:
        # print(*answer)
        for i in range(n):
            if A[i] == 1:
                print('%d ' % data[i], end='')
        print()
    # print()

def powerset(n, k):         # n: 원소의 개수, k: 현재 depth
    if n == k:              # Basis Part
        printSet(n)
    else:                   # Inductive Part
        A[k] = 1            # k번 요소 o
        powerset(n, k+1)    # 다음 요소 포함 여부 결정
        A[k] = 0            # k번 요소 x
        powerset(n, k+1)    # 다음 요소 포함 여부 결정

powerset(N, 0)