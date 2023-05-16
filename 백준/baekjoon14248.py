#백준 14248번 점프점프
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

visited = [0 for _ in range(n)]
cnt = 1

def bfs(s):
  global cnt
  q = deque()
  q.append(s)
  while q:
    x = q.popleft()
    for nx in (x+arr[x], x-arr[x]):
      if 0<=nx<n and visited[nx] == 0:
        visited[nx] = 1
        cnt +=1
        q.append(nx)

bfs(s-1)
print(cnt)