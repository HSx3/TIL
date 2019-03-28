def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        print("Stack is Empty!")
        return
    else:
        return stack.pop(-1)


str = "2+3*4/5"
stack = []

for i in range(len(str)):
    if str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
        push(str[i])
    else:
        print(str[i], end="")

while len(stack) != 0:
    print(pop(), end="")