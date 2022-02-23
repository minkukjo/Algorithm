from typing import List


def sortKey(s: str):
    return s.split()[1], s.split()[0]


def solve(logs: List[str]):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=sortKey)
    return letters + digits


logs = ["dig1 8 1 5 1", "let4 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(solve(logs))
