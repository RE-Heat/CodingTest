#백준 11724번 연결 요소의 개수
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(start, depth):
  visited[start] = True
  
  for i in graph[start]:
    if not visited[i]:
      dfs(i, depth+1)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)
cnt = 0

for i in range(1, n+1):
  if not visited[i]:
    if not graph[i]:
      cnt += 1
      visited[i] = True
    else:
      dfs(i, 0)
      cnt += 1

print(cnt)