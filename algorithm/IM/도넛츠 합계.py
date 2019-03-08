import sys
sys.stdin = open("도넛츠 합계.txt")

def donut(i, j):
    global sum_edge_list
    sum_edge = 0

    for x in range(i, i+K):
        for y in range(j, j+K):
            if x == i or x == i+K-1:
                sum_edge += data[x][y]
            if y == j or y == j+K-1:
                sum_edge += data[x][y]
            if x == i and y == j:
                sum_edge -= data[x][y]
            if x == i and y == j+K-1:
                sum_edge -= data[x][y]
            if x == i+K-1 and y == j:
                sum_edge -= data[x][y]
            if x == i+K-1 and y == j+K-1:
                sum_edge -= data[x][y]
    sum_edge_list.append(sum_edge)
    return sum_edge_list

N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
# print(data)

sum_edge_list = []
for i in range(0, N-K+1):
    for j in range(0, N-K+1):
        donut(i, j)
print((max(sum_edge_list)))