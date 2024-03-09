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
answer = []
score = 0
def solution(n, info):
    
    ryan = [0 for i in range(11)]
    
    def dfs(arrow, ryan, index):
        global answer, score
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

                if dif > score:
                    score = dif
                    answer = list(ryan)
                elif dif == score:
                    for i in range(11):
                        if ryan[-i] > answer[-i]:
                            answer = list(ryan)
                            return
                        elif ryan[-i] < answer[-i]:
                            return
        if index == 11:
            return
        
        for i in range(info[index]+2):
            if i <= n:
                ryan[index] = i
                dfs(arrow-i,ryan, index+1)
                ryan[index] = 0
    
    dfs(n, ryan, 0)
    
    if(len(answer) == 0):
        return [-1]

    return answer

# 외벽점검
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = float('inf')

    for i in range(length):
        for j in list(permutations(dist, len(dist))):
            used_friend = 1
            cur = weak[i] + j[used_friend-1]
            for k in range(i, i+length):
                if cur < weak[k]:
                    used_friend += 1
                    if used_friend > len(dist):
                        break
                    cur = weak[k] + j[used_friend-1]
            answer = min(answer, used_friend)
    if answer > len(dist):
        return -1

    return answer

# 게임 맵 최단 거리
from collections import deque

def solution(maps):
    start = (0,0,0)
    goal = (len(maps)-1, len(maps[0])-1)

    q = deque()
    q.append(start)

    visited = []

    answer = float('inf')

    dist = [(0,1), (1,0), (-1,0), (0,-1)]
    while q:
        x,y, step = q.pop()

        if (x,y) == goal:
            answer = min(answer, step)

        for dx,dy in dist:
            nx = x+dx
            ny = y+dy

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and (nx,ny) not in visited:
                visited.append((nx,ny))
                q.append((nx,ny, step+1))

    if answer == float('inf'):
        return -1

    return answer

# 네트워크

def solution(n, computers):
    answer = 0

    adj = [[] for i in range (n)]

    for i, computer in enumerate(computers):
        for j in range(n):
             if i != j and computer[j] == 1:
                 adj[i].append(j)

    visited= [0] * n

    def dfs(index):
        visited[index] = 1

        for target_index in adj[index]:
            if visited[target_index] == 0:
                dfs(target_index)
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1

    return answer

# 배달

import heapq

def solution(N, road, K):
    answer = 0

    dist = [float('inf')] *(N+1)
    dist[1] = 0
    village = [[] for i in range(N)]

    for i in range(N):
        a,b,w = road[i]
        village[a].append((b, w))
        village[b].append((a, w))
    
    def dijkstra(dist):
        heap =[]
        heapq.heappush(heap, (0,1))

        while heap:
            weight, node = heapq.heappop(heap)
            for connected_node, connected_weight in village[node]:
                if connected_weight + weight < dist[connected_node]:
                    dist[connected_node] = connected_weight + weight
                    heapq.heappush(heap, (connected_weight + weight, connected_node))

    answer = []

    for i in range(N):
        if dist[i] <= K:
            answer.append(i)

    return len(answer)