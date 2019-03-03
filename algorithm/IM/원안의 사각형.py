import sys
sys.stdin = open("원안의 사각형.txt")

R = int(input())

count = 0
for i in range(1, R):
    for j in range(1, R):
        if i**2 + j**2 <= R**2:
            count += 1
print(4*count)