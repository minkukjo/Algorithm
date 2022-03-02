class ListNode:
    def __init__(self, v):
        self.left = None
        self.value = v
        self.right = None

    def __str__(self):
        return self.value


class MyCircularDeque:
    def __init__(self, k):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.k = k
        self.len = 0
        self.head.right = self.tail
        self.tail.left = self.head

    def _add(self, node: ListNode, new: ListNode):
        right_node = node.right
        node.right = new
        new.left = node
        new.right = right_node
        right_node.left = new

    def _del(self, node: ListNode):
        target_node = node.right.right
        target_node.left = node
        node.right = target_node

    def insertFront(self, v):
        if self.k == self.len:
            return False
        self._add(self.head, ListNode(v))
        self.len += 1
        return True

    def insertLast(self, v):
        if self.k == self.len:
            return False
        self._add(self.tail.left, ListNode(v))
        self.len += 1
        return True

    def deleteFront(self):
        if self.len == 0:
            return False

        self._del(self.head)
        self.len -= 1
        return True

    def deleteLast(self):
        if self.len == 0:
            return False

        self._del(self.tail.left.left)
        self.len -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.head.right.value

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.tail.left.value

    def isEmpty(self):
        if self.len == 0:
            return True
        return False

    def isFull(self):
        if self.len == self.k:
            return True
        return False


deque = MyCircularDeque(5)
deque.insertLast(5)
deque.insertLast(10)
print(deque.getFront())
print(deque.getRear())

deque.insertFront(10)

print(deque.getFront())
