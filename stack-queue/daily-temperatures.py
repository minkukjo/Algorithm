def solve(t):
    stack = []
    result = [0] * len(t)
    for i, cur in enumerate(t):
        while stack and cur > t[stack[-1]]:
            last = stack.pop()
            result[last] = i - last
        stack.append(i)

    return result


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(solve(T))
