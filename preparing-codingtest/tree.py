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

# 양과 늑대
def solution(info, edges):
    answer = []

    visited = [0] * len(info)

    def dfs(s, w):
        if s > w:
            answer.append(s)
        else:
            return

        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                # 1은 늑대인 경우, 0이 양
                if info[c] == 1:
                    dfs(s,w+1)
                else:
                    # 양
                    dfs(s+1,w)
                visited[c] = 0

    visited[0] = 1
    dfs(1,0)

    return max(answer)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))


import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, key):
        self.base = x
        self.key = key
        self.left = None
        self.right = None

def solution(nodeinfo):
    for i, node in enumerate(nodeinfo):
        node.append(i+1)

    nodeinfo.sort(key= lambda x: -x[1])

    root = Node(nodeinfo[0][0], nodeinfo[0][2])
    cur = root
    for base,height,key in nodeinfo[1:]:
        new = Node(base, key)
        cur = root
        while True:
            if cur.base > base:
                if cur.left is None:
                    cur.left = new
                    break
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = new
                    break
                else:
                    cur = cur.right
    
    pre = []
    def preorder(node):
        if node is None:
            return
        pre.append(node.key)
        preorder(node.left)
        preorder(node.right)
    
    post = []
    def postorder(node):
        if node is None:
            return
        postorder(node.left)
        postorder(node.right)
        post.append(node.key)
    
    preorder(root)
    postorder(root)
    answer = []
    answer.append(pre)
    answer.append(post)
    return answer
