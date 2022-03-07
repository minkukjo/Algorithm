from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, value):
        self.next = None
        self.value = value


queue = PriorityQueue()


def solve(lists: List[ListNode]):
    for k in lists:
        while k != None:
            queue.put(k.value)
            k = k.next

    print(queue.get(0), end="")
    for i in range(1, queue.qsize() + 1):
        print("->", queue.get(i), end="")


node = ListNode(1)
node.next = ListNode(4)
node.next.next = ListNode(5)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

node3 = ListNode(2)
node3.next = ListNode(6)

lists = [node, node2, node3]

solve(lists)
