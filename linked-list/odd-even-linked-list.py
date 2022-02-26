def solve(s: str):
    split = s.split("->")
    null = split.pop()

    odd = []
    even = []
    for i in range(len(split)):
        if (i + 1) % 2 == 0:
            even.append(split[i])
        elif (i + 1) % 2 == 1:
            odd.append(split[i])

    even.append(null)

    return '->'.join(odd + even)


test_input = "1->2->3->4->5->NULL"
test_input2 = "2->1->3->5->6->4->7->NULL"
print(solve(test_input))
print(solve(test_input2))
