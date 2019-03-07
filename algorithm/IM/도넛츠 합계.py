import sys
sys.stdin = open("도넛츠 합계.txt")

# def sum_edge(i,j):



N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
print(data)

for_sum = []
for i in range(0, N-K+1+1):
    for j in range(0, N-K+1+1):
        for_sum.append((i, j, data[i][j]))
print(for_sum)