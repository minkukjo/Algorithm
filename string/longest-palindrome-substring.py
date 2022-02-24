def longestPalindrome(s: str):
    def expand(left: int, right: int):
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


def isPalindrome(s):
    return s == s[::-1]


def solve(s):
    answer = ""
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if isPalindrome(s[i:j]):
                answer = max(s[i:j], answer, key=len)
    return answer


test_input = "babad"

test_input2 = "cbbd"

test_input3 = "78943412345432153421"

print(longestPalindrome(test_input3))
