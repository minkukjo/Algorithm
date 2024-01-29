from itertools import permutations
import operator

def number1(arr):
    arr.sort()
    return arr

def number2(arr):
    not_duplicated_list = list(set(arr))
    not_duplicated_list.sort(reverse=True)
    return not_duplicated_list

def number3(numbers):
    pms = permutations(numbers,2)
    result = []
    for pm in pms:
        sum = pm[0] + pm[1]
        if sum not in result:
            result.append(sum)
    result.sort()
    return result


def number4(answers):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    right_answers = [0,0,0]

    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                right_answers[j] += 1
    max_right = max(right_answers)

    results = []
    for i, right_answer in enumerate(right_answers):
        if right_answer == max_right:
            results.append(i+1)
    return results

def number5(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


number5([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])

def number6(n,stages):

    dic = {}

    for i in range(n):
        cur_stage = i +1

        filtered_stages = list(filter(lambda item: item >= cur_stage,stages))

        count_cur_stage_in_filtered_stages = filtered_stages.count(cur_stage)

        dic[cur_stage] = count_cur_stage_in_filtered_stages / len(filtered_stages)
    
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    return [i[0] for i in sorted_dic]



number6(5, [2,1,2,6,2,4,3,3])

number6(4, [4,4,4,4,4])

def solution(dirs):
    x = 0
    y = 0
    
    ans = set()

    position = {
        'U' : (-1,0),
        'D' : (1,0),
        'R' : (0,1),
        'L' : (0,-1)
    }


    for char in dirs:

        (dx,dy) = position[char]
        nx = x + dx
        ny = y + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            ans.add(((x, y), (nx, ny)))
            ans.add(((nx, ny), (x, y)))
            x,y = nx,ny
    return len(ans)/2

def solution(s):
    answer = True
    
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    
    if stack:
        return False

    return True

def isPair(s):
    stack = []
    
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if not stack:
                return False
            top = stack.pop()
            if c == ')' and top != '(':
                return False
            elif c == ']' and top != '[': 
                return False
            elif c == '}' and top != '{': 
                 return False
    if stack:
        return False
    return True
    
def solution(s):
    
    answer = 0
    
    for i in range(len(s)):
        a = s[:i]
        b = s[i:]
        
        if isPair(b+a):
            answer += 1        
                
    return answer

def yosepush(n,k):

    q = [(i+1) for i in range(n)]
    
    cur = 1
    while len(q) != 1:

        item = q.pop(0)

        if cur == k:
            cur = 0
        else:
            cur += 1
            q.append(item)
    print(q)

yosepush(5,2)

