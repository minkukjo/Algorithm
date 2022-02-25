import sys
from typing import List


def niceSolve(arr: List[int]):
    profit = 0
    min_price = sys.maxsize

    for price in arr:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit


def solve(arr: List[int]):
    min_value = min(arr)
    index = arr.index(min_value)
    higher = 0
    for i in range(index, len(arr)):
        higher = max(higher, arr[i])
    return higher - min_value


test_input = [7, 1, 5, 3, 6, 4]
print(solve(test_input))
print(niceSolve(test_input))
