SIZE = 4
Q = [0]*SIZE
front, rear = 0, 0
def isFull():
    global front, rear
    return (rear+1) % len(Q) == front
def isEmpty():
    global front, rear
    return front == rear
def enQueue(item):
    global rear
    if isFull(): print("Queue Full")
    else:
        rear = (rear+1) % len(Q)
        Q[rear] = item
def deQueue():
    global front
    if isEmpty() : print("Queue Empty")
    else:
        front = (front+1)%len(Q)
        return Q[front]


enQueue(1)
enQueue(2)
enQueue(3)
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(4)
print(deQueue())
enQueue(5)
print(deQueue())
print(Q)