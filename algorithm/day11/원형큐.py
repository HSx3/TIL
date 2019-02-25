SIZE = 4
Q = [0] * SIZE
front = 0
rear = 0

def isFull():
    return (rear+1) % len(Q) == front

def isEmpty():
    global front, rear
    return front == rear

def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = (rear+1) % len(Q)
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front+1) % len(Q)
        return Q[front]

enQueue(1)
enQueue(2)
enQueue(3)
print(deQueue())
print(deQueue())
print(deQueue())
# enQueue(4)
# print(deQueue())
# enQueue(5)
# print(deQueue())



#####################
# import queue
# q = queue.Queue() # 큐 생성
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())