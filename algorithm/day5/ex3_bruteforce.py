# def bruteForce(text, pattern, start):
#     i, j = start, 0
#     while j < len(pattern) and i < len(text):
#         if text[i] != pattern[j]:
#             i = i - j
#             j = -1
#         i = i + 1
#         j = j +1
#     if j == len(pattern):
#         return i
#     else:
#         return -1



# def BruteForce(p, t):
#     i = 0 # t의 인덱스
#     j = 0 # p의 인덱스
#     while j < M and i < N:
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#         i = i + 1
#         j = j + 1
#     if j == M:
#         return i - M # 검색 성공
#     else:
#         return -1 # 검색 실패
#
# p = 'is' # 찾을 패턴
# t = 'This is a book~!' # 전체 텍스트
# M = len(p) # 찾을 패턴의 길이
# N = len(t) # 전체 텍스트의 길이
# print(BruteForce(p, t))



def bruteForce2(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else:
                cnt += 1
        if(cnt >= len(pattern)):
            return i

text = 'This is a book. This is a computer'
pattern = 'is'

start = 0
while True:
    start = bruteForce(text, pattern, start)
    print(start)
    start = start + len(pattern)
    if start > len(text) - len(pattern):
        break
