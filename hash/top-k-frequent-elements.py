import collections


def solve(nums, k):
    counter = collections.Counter(nums)
    most_common = counter.most_common(k)
    print(most_common)
    answer = [num[0] for num in most_common]
    return answer


nums = [1, 2]
k = 2

print(solve(nums, k))
