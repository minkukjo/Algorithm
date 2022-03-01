# 큐를 이용해 스택을 만들어보자
import collections


class MyStack:
    q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            return None
        return self.q.popleft()

    def top(self):
        if not self.q:
            return None

        return self.q[0]

    def empty(self):
        if not self.q:
            return True

        return False


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())
