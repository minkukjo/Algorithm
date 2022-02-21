import collections
import re


def slice(s: str):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]


def solve(s: str):
    strs = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


test_case_1 = "A man, a plan, a canal: Panama"
test_case_2 = "race a car"

print(solve(test_case_1))
print(solve(test_case_2))

print(slice(test_case_1))
print(slice(test_case_2))
