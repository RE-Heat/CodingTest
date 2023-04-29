#백준 11725번 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
parent = [0] * (n + 1)

for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      parent[i] = v
      dfs(graph, i, visited)


dfs(graph, 1, visited)

for num in range(2, len(parent)):
  print(parent[num])
