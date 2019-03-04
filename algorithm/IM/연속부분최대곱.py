import sys
sys.stdin = open("연속부분최대곱.txt")

N = int(input())
data = []
for i in range(N):
    data.append(float(input()))
print(data)

check = []

