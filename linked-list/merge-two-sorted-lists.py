def solve(s: str):
    s = s.replace(" ", "")
    split = s.split(",")
    first = split[0].split("->")
    second = split[1].split("->")

    first_list = []
    for num in first:
        first_list.append(int(num))

    second_list = []
    for num in second:
        second_list.append(int(num))

    result = []
    while first_list and second_list:
        if first_list[0] <= second_list[0]:
            result.append(first_list.pop(0))
        elif first_list[0] > second_list[0]:
            result.append(second_list.pop(0))

    while first_list:
        result.append(first_list.pop(0))
    while second_list:
        result.append(second_list.pop(0))

    return result


test_input = "1->2->4, 1->3->4"
print(solve(test_input))
