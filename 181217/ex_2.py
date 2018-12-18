# 2
# 주어진 리스트의 요소들 중에서 자연수가 홀수인지
# 짝수인지 판별하여 각각의 리스트로 출력하여라.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(even, "짝수입니다")
print(odd, "홀수입니다")