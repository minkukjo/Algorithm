# 투포인터 방식
def solve(s):
    for i in range(0, int(len(s) / 2)):
        first = s[i]
        last = s[len(s) - 1 - i]
        s[i] = last
        s[len(s) - 1 - i] = first


test_input = ["h", "e", "l", "l", "o"]
test_ipunt2 = ["H", "a", "n", "n", "a", "h"]
# 파이썬에서 제공하는 메소드로도 해결 가능
test_ipunt2.reverse()

solve(test_input)
print(test_input)
