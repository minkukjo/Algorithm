def solve(s: str, m, n):
    split = s.split("->")
    m = m - 1

    sub = split[m:n]
    return split[:m] + sub[::-1] + split[n:]


test_input = "1->2->3->4->5->NULL"
m = 2
n = 4
print(solve(test_input, m, n))
