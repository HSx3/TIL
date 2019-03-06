import sys
sys.stdin = open("창고다각형.txt")

N = int(input())

L_list = []
H_list = []
LH = []
for i in range(N):
    L, H = map(int, input().split()) # L : 위치 H : 높이
    L_list.append(L)
    H_list.append(H)
    LH.append((L, H))
print(L_list)
print(H_list)
print(LH)

height = H_list[0]
area = 0

array = sorted(LH)
print(array)

print(array[0][1])
print(array[1][1])


for i in range(4):
    if array[i][1] < array[i+1][1]:
        height = array[i][1]
        width = array[i+1][0] - array[i][0]
        area += (array[i+1][0] - array[i][0])*height
        print("{}".format(area))
    else:
        height = H_list[i]
        width = L_list[i]
        # area += (array[i+1][0] - array[i][0])*height
print(area)

