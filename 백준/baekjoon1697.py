#백준 1697번 숨바꼭질
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * 200001

def bfs(start, end):
  queue = deque([start])
  
  while queue:
    v = queue.popleft()
    if v == k:
     return visited[k] -1

    for n in (v-1, v+1, v*2):
      if 0<=n<=200000 and visited[n] == 0:
        queue.append(n)
        visited[n] = visited[v] + 1
  return -1

print(bfs(n, k))