# 어려운 문제다.
# 슬라이딩 윈도우와 투 포인터를 사용해야하는 문제.
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


s = "abcabcfb"
s2 = "tmmzuxt"
print(solve(s))
