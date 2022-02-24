from typing import List


def solve(nums: List[int], target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and nums_map[target - num] != i:
            return nums.index(num), nums_map[target - num]


nums = [2, 7, 11, 15]
target = 9

print(solve(nums, target))
