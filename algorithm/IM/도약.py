import sys
sys.stdin = open("도약.txt")

N = int(input())
data = []
for i in range(N):
    data.append(int(input()))
sorted_data = sorted(data)
print(sorted_data)

count = 0
count_jump = 0
for i in range(len(sorted_data)-2):
    start = sorted_data[i]
    for j in range(i+1, len(sorted_data)):
        jump1 = sorted_data[j]
        for k in range(j+1, len(sorted_data)):
            jump2 = sorted_data[k]
            if jump1 - start <= jump2 - jump1 <= 2*(jump1 - start):
                count += 1
print(count)
