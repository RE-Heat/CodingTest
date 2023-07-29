#백준 13549번 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
  q = deque([(start, 0)])
  while q:
    v, time = q.popleft()

    if v == end:
      return time

    for next in (v - 1, v + 1, v * 2):
      if 0 <= next <= 100000 and next not in visited:
        visited.add(next)
        if next == v * 2:
          q.appendleft((next, time))
        else:
          q.append((next, time + 1))
  return -1

N, K = map(int, input().split())
visited = set([N])
print(bfs(N, K))
