# f = open("new.txt", "w")    # 만들면서 열고, 내용 쓰기
# f.write("Hello!")           # 내용
# f.close()

# with open("new.txt", "w") as f:
#     f.write("Hello!")

# f = open("new.txt", "r")    # f = 그냥 변수명, 파일 조작시 주로 사용
# data = f.read()
# print(data)
# f.close()

# with open("new.txt", "r") as f:
#     data = f.read()
#     print(data)


# f = open("new.txt", "w", encoding='utf-8')
# # numbers = range(1,101)
# for n in range(1,51):
#     data = f'{n}번째 줄입니다.\n'
#     f.write(data)
# f.close()

# with open("new.txt", "w", encoding='utf-8') as f:
#     for n in range(1,31):
#         data = f'{n}번째 줄입니다.\n'
#         f.write(data)

# menu = ["카레\n", "짜장\n", "탕수육\n"]
# f = open("menu.txt", "w", encoding='utf-8')
# f.writelines(menu)
# f.close()


menu = ["카레\n", "짜장\n", "새우\n"]
with open("menu.txt", "w", encoding='utf-8') as f:
    f.writelines(menu)