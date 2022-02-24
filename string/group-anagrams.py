from typing import List


def solve(words: List[str]):
    map = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in map:
            map[sorted_word] += [word]
        else:
            map[sorted_word] = [word]

    return map.values()


test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solve(test_input))
