#백준 2589번 보물섬
import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
  q = deque()
  q.append((i, j))
  visited = [[0] * n for _ in range(m)]
  visited[i][j] = 1
  cnt = 0  
  while q:
    x, y = q.popleft()    
    for dir in range(4):
      nx = x + dx[dir]
      ny = y + dy[dir]      
      if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
        if graph[nx][ny] == 'L':
          visited[nx][ny] = visited[x][y] + 1
          cnt = max(cnt, visited[nx][ny])
          q.append((nx, ny))
  return cnt - 1

ans = 0
for i in range(m):
  for j in range(n):
    if graph[i][j] == 'L':
      ans = max(ans, bfs(i, j))

print(ans)