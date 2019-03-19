import sys
sys.stdin = open("input.txt", "r")

T = int(input())

r, c = list(map(int, input().split(' ')))

field = []
for i in range(0, r):
	row = input()
	field.append(row)

print (T)
print (str(r) + " " + str(c))
for i in range(0, r):
	print (field[i])
