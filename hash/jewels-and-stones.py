import collections


def solve(J, S: str):
    counter = collections.Counter(S)
    result = 0
    for word in list(J):
        result += counter.get(word)
    return result


J = "aA"
S = "aAAbbbb"

print(solve(J, S))
