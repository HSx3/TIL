# python 과거
# '일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')

# pyformat
# '{} {}'.format('one', 'two')

# name = '서호성'
# e_name = 'Seo'
# print('안녕하세요. {}입니다. My name is {}'.format(name, e_name))

# f-string python 3.6
# print(f'안녕하세요. {name}입니다. My name is {e_name}')

# lotto
import random
numbers = list(range(1,46))
number = random.sample(numbers,6)
# number.sort()
print(f'오늘의 행운 번호는 {number}입니다.')
# print(f'오늘의 행운 번호는 {number[0]}, {number[1]}, {number[2]}, {number[3]}, {number[4]}, {number[5]}입니다.')

# print(f'오늘의 행운 번호는 {sorted(number)}입니다.')
# print('오늘의 행운 번호는 {}입니다.'.format(number))

# name = "홍길동"
# print("안녕하세요. " + name + "입니다.")