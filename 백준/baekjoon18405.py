#백준 18405번 경쟁적 전염
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
graph = []
virus = []
for i in range(N):
  graph.append(list(map(int,input().split())))
  for j in range(N):
    virus.append((graph[i][j], i, j))
S, X, Y = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, X, Y):
  q = deque((virus))
  second = 0
  while q:
    if second == s:
      break
    for _ in range(len(q)):
      prev, x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
          if graph[nx][ny] == 0:
            graph[nx][ny] = prev
            q.append((graph[nx][ny], nx, ny))
    second +=1 
  return graph[X-1][Y-1]

virus.sort()
print(bfs(S, X, Y))
