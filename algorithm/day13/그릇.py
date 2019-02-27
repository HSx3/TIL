import sys
sys.stdin = open("그릇.txt")

T = input()

height = 0
stack = []
for i in T:
    if not stack:
        stack.append(i)
        height += 10
    else:
        if i == stack[-1]:
            stack.append(i)
            height += 5
        else:
            stack.append(i)
            height += 10
print(height)


'''
arr = input()
'''