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