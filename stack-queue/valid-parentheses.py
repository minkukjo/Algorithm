def solve(s: str):
    stack = []
    for bracket in s:
        if bracket == '(' or bracket == '[' or bracket == '{':
            stack.append(bracket)
        else:
            if len(stack) <= 0:
                return False
            if bracket == ')' and stack[-1] != '(':
                return False
            if bracket == ']' and stack[-1] != '[':
                return False
            if bracket == '}' and stack[-1] != '{':
                return False
            stack.pop()

    if len(stack) > 0:
        return False

    return True


test_input = "()[]{{}}"
print(solve(test_input))
