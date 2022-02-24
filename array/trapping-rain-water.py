# 42 빗물 트래핑 개어렵다...
from typing import List


def solve(height: List[int]):
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)

    return


test_input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
solve(test_input)
