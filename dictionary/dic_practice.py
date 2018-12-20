"""
파이썬 dictionary 활용 기초!
"""

# # 1. 평균을 구하세요.
# scores = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }

# total = 0
# print(scores.values())
# for score in scores.values():
#     # print(i)
#     total += score
# avg = total/len(scores)
# print(avg)

# print(sum(scores.values()))




# 2. 반 평균을 구하시오
# scores = {
#     "철수" : {
#         "수학" : 80,
#         "국어" : 90,
#         "음악" : 100
#     },
#     "영희" : {
#         "수학" : 70,
#         "국어" : 60,
#         "음악" : 50
#     }
# }

# total_score = 0
# count = 0

# for person_score in scores.values():
#     print(person_score)
#     for indivisual_score in person_score.values():
#         print(indivisual_score)
#         total_score += indivisual_score
#         count += 1

# average_score = total_score / count
# print(average_score)




# 3. 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
# hint. max, min
# scores = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }

# for key, value in scores.items():
#     print(key)
#     print(value)

cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0

for name, temp in cities.items():
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가 cold보다 더 추우면, cold에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1

print(f"{hot_city}, {cold_city}")







    # print(name)
    # print(temp)
    # print(f"{name}의 최저기온은 {min(temp)}도 입니다.")
    # print(f"{name}의 최고기온은 {max(temp)}도 입니다.")
    # for i in cities.values():
    #     print(i)
    # print(cities["서울"])
    # print(temp[0])
    # print(min(temp))
    # print(max(cities["서울"]))
    
        
    








