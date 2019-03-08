import sys
sys.stdin = open("경비원.txt")


site = []
width , height = map(int, input().split())
N = int(input())        # 상점의 개수
for i in range(N):
    site_d, site_s = map(int, input().split())
    site.append((site_d, site_s))
guard_d, guard_s = map(int, input().split())
print(site)

distance = 2*width + 2*height
print(distance)

# 상점 변환
for i in range(len(site)):
    if site[i][0] == 1:                     # 북
        site[i] = (0, site[i][1])
    elif site[i][0] == 2:                   # 남
        site[i] = (height, site[i][1])
    elif site[i][0] == 3:                   # 서
        site[i] = (site[i][1], 0)
    elif site[i][0] == 4:                   # 동
        site[i] = (width, site[i][1])
    # check_distance
print(site)

# 경비 변환
if guard_d == 1:  # 북
    guard_d = 0
elif guard_d == 2:  # 남
    guard_d = height
elif guard_d == 3:  # 서
    guard_d = 0
elif guard_d == 4:  # 동
    guard_d = width
print(guard_d, guard_s)
# 거리계산
check_distance = []
# for i in range(len(site)):
#     distance1 = abs(guard_d - site[i][0])
#     distance2 = abs(guard_s - site[i][1])
#     if guard_d == 0 and site[i][0] == height:
#         distance
#     print(distance1 + distance2)

temp = [[0 for _ in range(width)] for _ in range(height)]
print(temp)