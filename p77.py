def solve(arr):
    arr.sort(key=lambda x: x[0])
    merged_intervals = []
    for interval in arr:
        if merged_intervals and interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
        else:
            merged_intervals.append(interval)
    return merged_intervals


test_input = [(1, 3), (5, 8), (4, 10), (20, 25)]
print(solve(test_input))
