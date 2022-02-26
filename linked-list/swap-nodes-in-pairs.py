def solve(s: str):
    split = s.split("->")

    result = []
    for i in range(0, len(split), 2):
        result.append(split[i + 1])
        result.append(split[i])
        
    return '->'.join(result)


test_input = "1->2->3->4"

print(solve(test_input))
