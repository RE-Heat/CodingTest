#백준 2644번 촌수계산
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = []

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(v, depth):
  depth +=1
  visited[v] = True

  if v == b:
    ans.append(depth)

  for i in graph[v]:
    if not visited[i]:
      dfs(i, depth)

dfs(a, 0)
if len(ans) == 0:
  print(-1)
else:
  print(ans[0]-1)