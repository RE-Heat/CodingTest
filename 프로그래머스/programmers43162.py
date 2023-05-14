#프로그래머스 DFS/BFS 네트워크
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(si, sj, visited, n, computers):
    queue = deque()    
    queue.append((si, sj))
    visited[si][sj] = 1
    while queue:
        ci, cj = queue.popleft()
        for num in range(4):
            ni = ci + dx[num]
            nj = cj + dy[num]
            if 0<=ni<n and 0<=nj<n and computers[ni][nj] == 1:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))    

def solution(n, computers):
    answer = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and computers[i][j] == 1:
                bfs(i, j, visited, n, computers)
                answer +=1    
    return answer