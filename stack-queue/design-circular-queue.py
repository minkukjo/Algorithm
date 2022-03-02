from typing import List


class MyCircularQueue:
    q: List
    size = 0
    front = 0
    rear = 0

    def __init__(self, size):
        self.size = size
        self.q = [None] * size

    def enQueue(self, v):
        if self.q[self.rear] is None:
            self.q[self.rear] = v
            self.rear = (self.rear + 1) % self.size
            return True
        else:
            return False

    def Front(self):
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self):
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

    def isFull(self):
        return self.front == self.rear and self.q[self.front] is not None

    def deQueue(self):
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.size
            return True


queue = MyCircularQueue(5)
queue.enQueue(10)
queue.enQueue(20)
queue.enQueue(30)
queue.enQueue(40)
print(queue.Rear())
print(queue.isFull())
queue.deQueue()
queue.deQueue()
queue.enQueue(50)
queue.enQueue(60)
print(queue.Rear())
print(queue.Front())
