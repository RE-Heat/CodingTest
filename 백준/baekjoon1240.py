#백준 1240 노드사이의 거리
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

def bfs(start, end):
  q = deque([])
  q.append((start, 0))

  visited = [False] * (n+1)
  visited[start] = True

  while q:
    v, d = q.popleft()
    if v == end:
      return d

    for w, dist in graph[v]:
      if not visited[w]:
        visited[w] = True
        q.append((w, d+dist))  

for _ in range(n-1):
  a, b, dist = map(int, input().split())
  graph[a].append((b, dist))
  graph[b].append((a, dist))

for _ in range(m):
  a, b = map(int, input().split())
  print(bfs(a, b))