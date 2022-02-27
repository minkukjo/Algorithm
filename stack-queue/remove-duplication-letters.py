def solve2(s: str):
    stack = []
    checker = set()

    for word in s:
        if len(stack) == 0:
            stack.append(word)
            checker.add(word)
        else:
            while stack and stack[-1] > word and word not in checker:
                stack.pop()

            if word in stack:
                continue
            
            stack.append(word)
            checker.add(word)

    return ''.join(stack)


def solve(s: str):
    result = set()

    for word in s:
        result.add(word)

    sorted_set = sorted(result)

    return ''.join(sorted_set)


test_input = "bcabc"
test_input2 = "cbacdcbc"
# print(solve2(test_input))
print(solve2(test_input2))
