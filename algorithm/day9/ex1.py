data = '2+3*4/5'
operator = ['+', '-', '*', '/']
stack = []

for i in range(len(data)):
    if data[i] not in operator:
        print(data[i], end = "")
    else:
        stack.append(data[i])

for i in range(len(stack)):
    print(stack.pop(), end = "")