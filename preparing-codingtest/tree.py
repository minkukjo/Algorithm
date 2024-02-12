# 예상 대진표

# a와 b를 적절히 나눠서 둘이 0이 될 때 까지 반복. 근데 이게 왜 트리 문제지?
def solution(n,a,b):
    answer = 0

    while a != b:
        
        a = (a+1) // 2
        b = (b+1) // 2
        
        answer += 1
    return answer
    

    return answer

