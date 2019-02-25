import sys
sys.stdin = open("행렬찾기_input.txt")

T = int(input())
# for test_case in range(1, T+1):
for test_case in range(1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)

    '''
    # 튜플로 만들어 리스트에 넣기
    checklist = []
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                checklist.append((i,j))
    print(checklist)
    # print(checklist[1][1])

    # 튜플 비교
    # for i in range(len(checklist)):
    #     if checklist[0][i]
    '''

    checklist = []
    arr = []


    while data != [[0 for _ in range(N)] for _ in range(N)]:
        for i in range(N):
            for j in range(N):
                if data[i][j] != 0:
                    start_x = i
                    start_y = j
                break
            break

        count_y = 0
        while data[start_x][start_y] != 0:
            if data[start_x][start_y] != 0:
                data[start_x][start_y] = 0
                start_y += 1
                count_y += 1
            else:
                break

        count_x = 0
        while data[start_x][start_y] != 0:
            if data[start_x][start_y] != 0:
                data[start_x][start_y] = 0
                start_x += 1
                count_x += 1
            else:
                break

        arr.append((count_x, count_y))
        print(arr)

        print(data)




    print(f'#{test_case}')


