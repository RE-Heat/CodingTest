#백준 13565번 침투
import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  q = deque([])
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
        graph[nx][ny] = 7
        q.append((nx, ny))

for _ in range(m):
  graph.append(list(map(int, input().rstrip())))

for i in range(n):
  if graph[0][i] == 0:
    bfs(0, i)

print("YES" if 7 in graph[-1] else "NO")