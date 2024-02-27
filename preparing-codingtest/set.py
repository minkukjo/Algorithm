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
