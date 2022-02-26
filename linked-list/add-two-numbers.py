def solve(s: str):
    s = s.replace(" ", "")
    list = s.split("+")
    first = list[0].replace("(", "").replace(")", "").split("->")
    second = list[1].replace("(", "").replace(")", "").split("->")

    first_list = first[::-1]
    second_list = second[::-1]
    sum = int(''.join(s for s in first_list)) + int(''.join(s for s in second_list))
    string_ints = [int(i) for i in str(sum)]
    reverse = string_ints[::-1]
    result = ""
    result += str(reverse[0])
    for i in range(1, len(reverse)):
        result += " -> " + str(reverse[i])

    return result


test_input = "(2 -> 4 ->3) + (5 -> 6 -> 4)"
print(solve(test_input))
