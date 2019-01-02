# 자연수 N이 주어졌을 때,
# 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# item = int(input("번호를 입력하세요 : "))
# for i in range(item):
#     print(i+1)

#for i in range(1, item+1):
#    print(i)



# Lv 2-1.
# 투자 경고 종목 리스트가 있을 떄 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면
# '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.

# warn_investment_list = ["microsoft", "google", "naver", "kakao", "samsung", "lg"]
# print(f"경고 종목 리스트 : {warn_investment_list}")
# item = input('투자 종목이 무엇입니까?: ')

# if item.lower() in warn_investment_list:
#     print('투자 경고 종목입니다')

# else:
#     print("투자 경고 종목이 아닙니다.")



# Lv 3-1.
# colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
# 다음 리스트에서 0번째 4번째 5번째 요소를 지운 새로운 리스트를 생성하시오.

# Q
# colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']

# fruit = []
# deleteindex = [0, 4, 5]

# for i in range(0, len(colors)):
#     if i not in deleteindex:
#         fruit.append(colors[i])
# print(fruit)


# ssafy의 semester1의 기간을 출력하세요.
# ssafy dictionary 안에 들어있는 '대전'을 출력하세요.
# daejeon의 매니저 이름을 출력하세요.
# hint : dict = ["key" : value]
#        print(dict["key"])

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}

print(ssafy["duration"]["semester1"])
print(ssafy["location"][1])
print(ssafy["classes"]["daejeon"]["manager"])