import sys
sys.stdin = open("비밀금고.txt")

N = int(input())
data = list(map(int, input().split()))
print(data)

arr = [[0 for _ in range(2*N-1)] for _ in range(2*N-1)]
# print(arr)
#
arr[0][(2*N-1)//2] = data[0]
for i in range(1, (2*N-1)//2+1):
    for j in range((2*N-1)//2-i, 2*N-1, 2):
        arr[i][j] = 1
        # for k in data[1:]:
        #     arr[i][j] = k
        #     break
print(arr)

# for i in range(2*N-1):
#     for j in range(2*N-1):
#          arr[i][j] = 0
