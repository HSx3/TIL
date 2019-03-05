# def find():     # 마지막 노드의 조상노드 찾기
#     global N
#     c = N
#     p = c // 2
#     s = 0
#     while p > 0:
#         s += Q[p]   # 조상 노드 값을 더함



import sys
sys.stdin = open("이진힙_input.txt")

T = int(input())
N = int(input())
data = list(map(int, input().split()))
print(data)