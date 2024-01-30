import operator
from itertools import permutations


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

# 주식
def solution(prices):
    answer = [0 for i in range(len(prices))]
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
    
    while stack:
        i = stack.pop()
        answer[i] = len(prices) - i -1
    
    return answer

def solution1(board, moves):
    answer = 0
    stack = [[] for row in range(len(board))]
    baguni = []
    # 2차원 스택 구성 stack
    x = len(board)
    y = len(board[0])
    for j in range(y):
        for i in range(x-1, -1, -1):
            if board[i][j] != 0:
                stack[j].append(board[i][j])
    
    for move in moves:
        i = move -1
        if stack[i]:
            doll = stack[i].pop()
            if baguni and baguni[-1] == doll:
                baguni.pop()
                answer += 2
            else:
                baguni.append(doll)
    return answer

def solution3(n, k, cmd):
    answer = ['O'] * n
    
    table = { i:[i-1, i+1] for i in range(n)}
    stack = []
    
    for cm in cmd:
        cm = cm.split()
        
        if cm[0] == 'U':
            for _ in range(int(cm[1])):
                k = table[k][0]
            
        elif cm[0] == 'D':
            for _ in range(int(cm[1])):
                k = table[k][1]
            
        elif cm[0] == 'C':
            print(table[k][0])
            prev = table[k][0]
            next = table[k][1]
            answer[k] = 'X'
            stack.append((prev,next,k))
            
            if next == n:
                # 맨 마지막이면 위에꺼 선택
                k = table[k][0]
            else:
                # 아니라면 아래꺼 선택
                k = table[k][1]
            
            if prev == -1:
                ## 제일 꼭대기인 경우 그 다음꺼가 -1이 됨 (꼭대기니까)                
                table[next][0] = prev
            elif next == n:
                ## 다음이 제일 마지막인 경우라면, 이전 꺼의 다음은 현재 위치의 다음이 됨
                table[prev][1] = next
            else:
                table[next][0] = prev
                table[prev][1] = next
        elif cm[0] == 'Z':
            prev, next, cur = stack.pop()
            answer[cur] = 'O'
            
            if prev == -1:
                table[next][0] = cur
            elif next == n:
                table[prev][1] = cur
            else:
                table[next][0] = cur
                table[prev][1] = cur
    
    return ''.join([i for i in answer])

solution3(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])