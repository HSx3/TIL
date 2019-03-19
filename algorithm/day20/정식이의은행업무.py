import copy
import sys
sys.stdin = open("정식이의은행업무_input.txt")

T = int(input())

for test_case in range(1, T+1):
    bi = list(str(input()))
    tri = list(str(input()))
    print('#{}'.format(test_case), end=' ')
    for i in range(len(bi)):
        for j in range(len(tri)):
            temp_bi = copy.deepcopy(bi)
            temp_tri = copy.deepcopy(tri)
            if bi[i] == '1' and tri[j] == '2':
                temp_bi[i] = '0'
                temp_tri[j] = '1'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))
                    # break
                temp_tri[j] = '0'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))
                    # break
            elif temp_bi[i] == '1' and temp_tri[j] == '1':
                temp_bi[i] = '0'
                temp_tri[j] = '2'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))
                temp_tri[j] = '0'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))

            elif temp_bi[i] == '1' and temp_tri[j] == '0':
                temp_bi[i] = '0'
                temp_tri[j] = '2'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))

                temp_tri[j] = '1'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))

            elif bi[i] == '0' and tri[j] == '2':
                temp_bi[i] = '1'
                temp_tri[j] = '1'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))
                    # break
                temp_tri[j] = '0'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))
                    # break
            elif temp_bi[i] == '0' and temp_tri[j] == '1':
                temp_bi[i] = '1'
                temp_tri[j] = '2'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))
                temp_tri[j] = '0'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))

            elif temp_bi[i] == '0' and temp_tri[j] == '0':
                temp_bi[i] = '1'
                temp_tri[j] = '2'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))

                temp_tri[j] = '1'
                if int(''.join(temp_bi), 2) == int(''.join(temp_tri), 3):
                    print(int(''.join(temp_bi), 2))