import sys
sys.stdin = open("input.txt", "r")

T = int(input())

r, c = list(map(int, input().split()))

arr = [list(map(int, input())) for _ in range(r)]


print (T)
print (r, c)
for i in range(0, r):
    for j in range(0, c):
	    print (arr[i][j], end="")
    print()
