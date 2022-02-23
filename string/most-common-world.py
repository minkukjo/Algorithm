import collections
import re
from typing import List


def answer(s: str, bans: List[str]):
    words = [word for word in re.sub(r'[^\w]', ' ', s).lower().split() if word not in bans]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


def solve(s: str, bans: List[str]):
    words = []
    lower_bans = []
    for word in s.split():
        word = word.lower()
        if not word.isalpha():
            chars = list(filter(str.isalpha, word))
            word = ''.join(chars)
        words.append(word)

    for ban in bans:
        lower_bans.append(ban.lower())

    hash = {}
    for word in words:
        if word in bans:
            continue
        elif word in hash:
            hash[word] += 1
        else:
            hash[word] = 1

    return max(hash, key=hash.get)


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(solve(paragraph, banned))
print(answer(paragraph, banned))
