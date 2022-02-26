import collections


def deque(s: str):
    s = s.split("->")
    q = collections.deque()

    for word in s:
        q.append(word)

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True


def solve(s: str):
    str_split = s.split("->")
    return str_split == str_split[::-1]


test_input = "1->2"
test_input2 = "1->2->2->1"

print(solve(test_input))
print(solve(test_input2))
print(deque(test_input2))
