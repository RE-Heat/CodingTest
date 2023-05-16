#백준 2583번 영역 구하기
import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

def bfs(x, y):
  q = deque()
  q.append((x,y))

  cnt = 1
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
        graph[nx][ny] = 1
        cnt +=1
        q.append((nx, ny))
  return cnt

for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      graph[i][j] = 1

ans = []

for i in range(m):
  for j in range(n):
    if graph[i][j] == 0:
      graph[i][j] = 1
      ans.append(bfs(i, j))

print(len(ans))
print(*sorted(ans))