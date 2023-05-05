#백준 9205번 맥주 마시면서 걸어가기
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs():
  queue = deque()
  queue.append((home_x, home_y))
  while queue:
    x, y = queue.popleft()
    if abs(x - festival_x) + abs(y - festival_y) <= 1000:
      return 'happy'
    for i in range(n):
      if not visited[i]:
        nx, ny = store[i]
        if abs(x - nx) + abs(y - ny) <= 1000:
          queue.append((nx, ny))
          visited[i] = True
  return 'sad'

t = int(input())

for _ in range(t):
  n = int(input())
  home_x, home_y = map(int, input().split())
  visited = [0 for _ in range(n + 1)]
  #편의점
  store = []
  for _ in range(n):
    x, y = map(int, input().split())
    store.append((x, y))
  #페스티벌 좌표
  festival_x, festival_y = map(int, input().split())
  print(bfs())
