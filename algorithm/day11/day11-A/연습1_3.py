import sys
import queue
q = queue.Queue()   # 큐 생성
q.put(1)   #enQueue
q.put(2)
q.put(3)
print(q.get()) #deQueue
print(q.get())
print(q.get())
