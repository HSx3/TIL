# 다음 내용을 표준 입력으로 읽어 들여 변수에 저장 후 출력하시오.
'''
10
5 10
0000000000
0123456789
0000000000
0000000000
0000000000
'''

import sys
sys.stdin = open("input.txt")

T = int(input())

r, c = list(map(int, input().split(' ')))

field = []
for i in range(0, r):
    row = input()
    field.append(row)

print(T)
print(str(r) + " " + str(c))
for i in range(0, r):
    print(field[i])