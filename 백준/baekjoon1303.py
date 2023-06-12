#백준 1303번 전쟁
import sys
from collections import deque
input = sys.stdin.readline

def bfsW(i, j):
  q = deque([])
  q.append((i, j))
  cnt = 1
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
        if graph[nx][ny] == 'W':
          visited[nx][ny] = 1
          cnt +=1
          q.append((nx, ny))
  return cnt

def bfsB(i, j):
  q = deque([])
  q.append((i, j))
  cnt = 1
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
        if graph[nx][ny] == 'B':
          visited[nx][ny] = 1
          cnt +=1
          q.append((nx, ny))
  return cnt

N, M = map(int, input().split())
graph = []
for _ in range(M):
  graph.append(list(map(str, input().rstrip())))
visited = [[0] * N for _ in range(M)]

cnt = 0
ansW = []
ansB = []

for i in range(M):  
  for j in range(N):
    if graph[i][j] == 'W' and not visited[i][j]:
      visited[i][j] = 1
      ansW.append(bfsW(i, j))
    elif graph[i][j] == 'B' and not visited[i][j]:
      visited[i][j] = 1
      ansB.append(bfsB(i, j))

ansW = [x ** 2 for x in ansW]
ansB = [x ** 2 for x in ansB]
print(sum(ansW), sum(ansB))