#백준 11279번 최대 힙
import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_heap = []

for _ in range(n):
  num = int(input())
  if num == 0:
    if len(max_heap):
      print(-heapq.heappop(max_heap))
    else:
      print(0)
  else:
    heapq.heappush(max_heap, -num)