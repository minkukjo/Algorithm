def solve(arr):
    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(1)
        else:
            result.append(result[i - 1] * arr[i - 1])

    temp = 1
    for i in range(len(arr) - 1, -1, -1):
        result[i] = result[i] * temp
        temp = temp * arr[i]

    return result


test_input = [1, 2, 3, 4]
print(solve(test_input))
