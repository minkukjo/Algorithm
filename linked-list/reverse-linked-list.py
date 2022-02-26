def solve(s: str):
    split = s.split("->")
    null = split.pop()
    reverse = split[::-1]
    reverse.append(null)

    result = ""
    result += reverse[0]
    for i in range(1, len(reverse)):
        result += "->" + reverse[i]

    return result


test_input = "1->2->3->4->5->NULL"
print(solve(test_input))
