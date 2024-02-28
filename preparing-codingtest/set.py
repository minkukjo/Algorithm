# 폰켓몬

def solution(nums):
    answer = 0

    dic = {}

    for num in nums:
        dic[num] = 1
    
    if len(dic.keys()) > len(nums) // 2:
        return len(nums) // 2
    else:
        return len(dic.keys())
    
# 영어 끝말잇기
def solution(n, words):

    dic = {}

    last_char = None
    for i, word in enumerate(words):
        if word in dic or (last_char is not None and last_char != word[0]):
            return [((i+1)/n), i+1]
        else:
            dic[word] = 1
            last_char = word[-1]

# 섬 연결하기
            
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    s = set(costs[0][0])

    while len(s) != n:
        for cost in costs:
            if cost[0] in s and cost[1] in s:
                continue
            elif cost[0] in s or cost[1] in s:
                s.add([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer