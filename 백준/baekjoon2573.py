#백준 2573번 빙산
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(si, sj, visited):
  queue = deque()
  queue.append([si, sj])
  visited[si][sj] = 1
  while queue:
    ci, cj = queue.popleft()
    for i in range(4):
      ni = ci + dx[i]
      nj = cj + dy[i]
      if visited[ni][nj] == 0 and arr[ni][nj] > 0:
        visited[ni][nj] = 1
        queue.append([ni, nj])

def solve():
  for year in range(1, 900000):
    # 상하좌우 0 개수 카운트
    a_sub = [[0] * m for _ in range(n)]
    for i in range(1, n - 1):
      for j in range(1, m - 1):
        if arr[i][j] == 0:
          continue
        for k in range(4):
          ni = i + dx[k]
          nj = j + dy[k]
          if arr[ni][nj] == 0:
            a_sub[i][j] += 1
    # 빙산 깎기
    for i in range(1, n - 1):
      for j in range(1, m - 1):
        if a_sub[i][j] > 0:
          arr[i][j] = max(0, arr[i][j] - a_sub[i][j])

    #빙산 덩어리 개수 카운트
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(1, n - 1):
      for j in range(1, m - 1):
        if visited[i][j] == 0 and arr[i][j] > 0:
          bfs(i, j, visited)
          cnt += 1
          if cnt > 1:
            return year
    if cnt == 0:
      return 0
  return -1

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = solve()
print(ans)
