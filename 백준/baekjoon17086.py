#백준 17086번 아기 상어
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque([])

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      q.append((i, j))

ans = 0
while q:
  x, y = q.popleft()
  dx = [-1, 1, 0, 0, -1, -1, 1, 1]
  dy = [0, 0, -1, 1, 1, -1, 1, -1]
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
      q.append((nx, ny))
      graph[nx][ny] = graph[x][y] + 1
      ans = max(ans, graph[x][y] + 1)

print(ans-1)
print(graph)