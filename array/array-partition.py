def solve(num):
    # 1,2,3,4
    nums = sorted(num)
    result = 0
    for num in range(0, len(nums), 2):
        result += nums[num]
    return result


test_input = [1, 4, 3, 2, 6, 5]

print(solve(test_input))
