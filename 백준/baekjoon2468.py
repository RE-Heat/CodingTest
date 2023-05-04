#백준 2468번 안전영역
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = []
max_num = 0
result = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
  low = list(map(int, input().split()))
  graph.append(low)
  for i in low:
    if i > max_num:
      max_num = i

def dfs(x, y, num):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
      if graph[nx][ny] > num:
        visited[nx][ny] = 1
        dfs(nx, ny, num)

for num in range(max_num):
  visited = [[0] * n for _ in range(n)]
  cnt = 0

  for i in range(n):
    for j in range(n):
      if graph[i][j] > num and visited[i][j] == 0:
        cnt += 1
        dfs(i, j, num)

  result = max(result, cnt)

print(result)