#백준 1325번 효율적인 해킹
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def bfs(v):
  queue = deque([v])
  cnt = 1
  visited = [False] * (n + 1)
  visited[v] = True
  while queue:
    x = queue.popleft()
    for i in graph[x]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
        cnt += 1
  return cnt

for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

ans = []
for i in range(1, n + 1):
  ans.append(bfs(i))

max = max(ans)
for i in range(len(ans)):
  if max == ans[i]:
    print(i + 1, end=' ')