import sys


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'<Node: value={self.value}, left={self.left}, right={self.right}>'


def bfs(node: Node):
    result = sys.maxsize
    q = [(node, node.value)]

    while q:
        pop_node, cur_sum = q.pop()

        if not pop_node.left and not pop_node.right:
            if result > cur_sum:
                result = cur_sum
            continue

        if pop_node.left:
            q.append((pop_node.left, cur_sum + pop_node.left.value))
        if pop_node.right:
            q.append((pop_node.right, cur_sum + pop_node.right.value))

    return result


test_input = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1), None)))
print(bfs(test_input))
