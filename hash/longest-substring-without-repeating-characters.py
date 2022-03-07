import collections


def solve(s: str):
    if len(s) <= 0:
        return 0
    used = {}
    result = 0
    start = 0
    for index, char in enumerate(s):
        if char in used and used[char] >= start:
            start = used[char] + 1
        else:
            result = max(result, index - start + 1)
        used[char] = index
    return result


s = "abcabcbb"
s2 = "tmmzuxt"
print(solve(s2))
