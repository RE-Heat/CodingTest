#백준 1260번 DFS와 BFS
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end = ' ')
  graph[v].sort() # 여기서 sort()해주는 게 특이점
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start,visited):
  visited[start] = True
  queue = deque([start])

  while queue:
    v = queue.popleft()
    print(v, end= ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)