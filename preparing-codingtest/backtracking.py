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