# 피로도
def solution(k, dungeons):
    answer = []
    visited = [0] * len(dungeons)
    def dfs(cur, dungeons, count):
        answer.append(count)
        
        for i, dungeon in enumerate(dungeons):
            yogu = dungeon[0]
            somo = dungeon[1]
            if visited[i] == 0 and cur >= yogu:
                visited[i] = 1
                dfs(cur-somo, dungeons, count+1)
                visited[i] = 0

    dfs(k, dungeons, 0)

    return max(answer)

# N-퀸
def solution(n):
    arr = [0] *n
    def isExistQueen(position):
        for i in range(position):
            if arr[position] == arr[i] or abs(arr[position]-arr[i]) == abs(position - i):
                return False
        return True

    def dfs(cur):
        answer = 0
        if cur == n:
            return 1
        else:
            for i in range(n):
                arr[cur] = i
                if isExistQueen(cur):
                    answer += dfs(cur+1)
        return answer

    return dfs(0)

# 양궁 대회

def solution(n, info):
    answer = []
    ryan = [0 for i in range(11)]
    max_score = [0]

    def dfs(arrow, ryan, index):
        if arrow == 0:
            ryan_score = 0
            apeach_score = 0
            for i in range(11):
                if ryan[i] == 0 and info[i] == 0:
                    continue

                if ryan[i] > info[i]:
                    ryan_score += (10-i)
                else:
                    apeach_score += (10-i)
            if ryan_score > apeach_score:
                dif = ryan_score - apeach_score

                if dif > max_score[0]:
                    max_score[0] = dif
                    answer = list(ryan)
                elif dif == max_score[0]:
                    for i in range(11):
                        if ryan[-1] > answer[-1]:
                            answer = list(ryan)
                            return
                        else:
                            return
        if index == 11:
            return
        for i in range(index, n+1):
            if i <= n:
                ryan[index] = i
                dfs(arrow-i,ryan, index+1)
                ryan[index] = 0
    
    dfs(n, ryan, 0)

    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))