#백준 1707 이분 그래프
import sys
from collections import deque
input = sys.stdin.readline

#이분 그래프
#BFS
def bfs(start, group):
  q = deque([start])
  visited[start] = group #1, -1로 그룹나눔
  while q:
    x = q.popleft()
    for i in graph[x]:
      if not visited[i]:
        q.append(i)
        visited[i] = -1 * visited[x] #인접 점정과 다른그룹으로
      elif visited[i] == visited[x]: #정점들이 같은 그룹이면 실패
        return False
  return True

K = int(input()) #테스트 케이스 개수
for _ in range(K):
  V, E = map(int, input().split()) #정점개수 #간선개수
  graph = [[] for _ in range(V + 1)]
  visited = [False] * (V+1)
  
  for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  for i in range(1, V+1):
    if not visited[i]:
      result = bfs(i, 1)
      if not result:
        break
  print("YES") if result else print("NO")
