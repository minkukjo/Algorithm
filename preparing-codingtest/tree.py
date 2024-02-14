# 예상 대진표

# a와 b를 적절히 나눠서 둘이 0이 될 때 까지 반복. 근데 이게 왜 트리 문제지?

def solution(n,a,b):
    answer = 0

    while a != b:
        
        a = (a+1) // 2
        b = (b+1) // 2
        
        answer += 1
    return answer
    
# 미로 탈출

from collections import deque

def solution(maps):

    def bfs(start, end):
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = [[0]*len(maps[0]) for _ in range(len(maps))]
        q = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = 1

        while q:
            (x,y, time) = q.popleft()

            if (x,y) == end:
                return time

            for (dx,dy) in direction:
                nx = x + dx
                ny = y + dy

                if nx >= 0 and nx < len(maps) and ny >= 0  and ny < len(maps[0]) and maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny,time+1))
        return 0


    start, lebber, exit = (),(),()
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = (i,j)
            elif maps[i][j] == "L":
                lebber = (i,j)
            elif maps[i][j] == "E":
                exit = (i,j)
                
    result1 = bfs(start,lebber)
    result2 = bfs(lebber,exit)

    if result1 == 0 or result2 == 0:
        return -1
    
    return result1 + result2