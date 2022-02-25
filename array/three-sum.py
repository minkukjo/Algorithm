from typing import List


# N^2의 투포인터 풀이
def twoPointer(nums: List[int]):
    sorted_num = sorted(nums)
    result = []
    for i in range(len(sorted_num) - 2):
        if i > 0 and sorted_num[i] == sorted_num[i - 1]:
            continue
        left = i + 1
        right = len(sorted_num) - 1
        while left < right:
            if sorted_num[i] + sorted_num[left] + sorted_num[right] > 0:
                left += 1
            elif sorted_num[i] + sorted_num[left] + sorted_num[right] < 0:
                right -= 1
            elif sorted_num[i] + sorted_num[left] + sorted_num[right] == 0:
                result.append((sorted_num[i], sorted_num[left], sorted_num[right]))
                while left < right and sorted_num[left] == sorted_num[left + 1]:
                    left += 1
                while left < right and sorted_num[right] == sorted_num[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result


# N^3의 브루트포스 풀이
def solve(nums: List[int]):
    result = []

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    list = sorted((nums[i], nums[j], nums[k]))
                    result.append(list)

    tuple_list = [tuple(l) for l in result]
    return set(tuple_list)


nums = [-1, 0, 1, 2, -1, -4]

print(twoPointer(nums))
