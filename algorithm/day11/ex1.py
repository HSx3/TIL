SIZE = 100
Q = [0] * SIZE
front = -1
rear = -1

def isFull():
    return rear == len(Q) -1

def isEmpty():
    global front, rear
    return front == rear

def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear += 1;
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front += 1
        return Q[front]

def Qpeek():
    global front, rear
    if isEmpty():
        print("Queue_Empty")
    else:
        return Q[front+1]

enQueue(1)
enQueue(2)
enQueue(3)
print(deQueue())
print(deQueue())
print(deQueue())



#####################
# import queue
# q = queue.Queue() # 큐 생성
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())