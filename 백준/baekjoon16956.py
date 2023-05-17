#백준 16956번 늑대와 양
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = False

for _ in range(r):
  graph.append(list(input().rstrip()))

for i in range(r):
  for j in range(c):
    if graph[i][j] == 'W':
      for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<r and 0<=ny<c and graph[nx][ny] == 'S':
          flag = True
          break
    elif graph[i][j] == 'S':
      continue
    elif graph[i][j] == '.':
      graph[i][j] = 'D'

if flag:
  print(0)
else:
  print(1)
  for c in graph:
    print(''.join(c))