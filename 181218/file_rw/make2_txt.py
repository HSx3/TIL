# f = open("review.txt", "w", encoding='utf-8')
# for i in range(1,6):
#     data = f'{i}번째 입니다.\t'
#     f.write(data)
# f.close()

# with open("review.txt", "w", encoding='utf-8') as f:
#     for i in range(1,6):
#         data = f'{i}번째 입니다.\t'
#         f.write(data)

# with open("new2.txt", "r", encoding='utf-8') as f:
#     line = f.readline()
#     print(line.strip())

with open("new2.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:          # for i in lines[:]:
        print(line.strip())