class MyQueue:
    stack1 = []
    stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return None
        return self.stack2.pop()

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        return self.stack1[0]

    def empty(self):
        return not self.stack1 and not self.stack2


queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())
